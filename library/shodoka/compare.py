#!/usr/bin/env python3
"""Compare the Shodoka edition with its source, word for word.

Usage: python3 library/shodoka/compare.py      (run from the repo root)

A copy of scripts/compare-source adapted to this text, kept here until that script is generalised
(bead filed for the site track). Reads shodoka.md and library/shodoka/Daily-Zen-Sutras.html (the
source as fetched) and prints every difference in the words of the poem. Quote style, dashes and
whitespace are normalised first, so only real changes show. Each difference must be either
reverted or listed in library/shodoka/NOTES.md. Exit status 1 if there are differences that are
not in the EXPECTED list below.
"""
import difflib, html, re, sys

EDITION = "shodoka.md"
SOURCE = "library/shodoka/Daily-Zen-Sutras.html"

# Changes we made on purpose (all listed in NOTES.md): (source words, edition words)
EXPECTED = {
    ("some", "same"),            # 16: "in exactly the some way"
    ("have", ""),               # 38: "What relation have have these"
    ("vWhich", "Which"),         # 42: stray "v"
}
# Lines split in two where the source has lost a line break: (stanza, source line number)
SPLIT = {(36, 3)}


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("`", "'")
    s = s.replace("—", " - ").replace("–", " - ").replace("--", " - ").replace("\xa0", " ")
    return re.sub(r"\s+", " ", s).strip()


def source_poem():
    h = open(SOURCE, encoding="latin-1").read()
    seg = h[h.index("<A NAME=SHODO>"):]
    seg = seg[seg.index("</EM>"):seg.index("Back to Index")]
    out = []
    for p in re.split(r"(?i)<P>", seg):
        lines = [norm(html.unescape(re.sub(r"<[^>]+>", "", l))) for l in re.split(r"(?i)<BR>", p)]
        lines = [l for l in lines if l]
        if lines:
            out.append(lines)
    return out


def edition_poem():
    t = open(EDITION, encoding="utf-8").read()
    t = t[t.index("## The poem"):t.index("## About this translation")]
    stanzas = []
    for block in t.split("\n\n"):
        m = re.match(r'\s*<a class="v" id="(\d+)" href="#\1">\1</a>\n', block)
        if not m:
            continue
        lines = [norm(re.sub(r"<[^>]+>", "", re.sub(r"\[\^[^\]]+\]", "", l))) for l in block[m.end():].split("\n")]
        stanzas.append((int(m.group(1)), [l for l in lines if l]))
    return stanzas


def diff_words(label, a, b, problems):
    aw, bw = a.split(), b.split()
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, aw, bw, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        pair = (" ".join(aw[i1:i2]), " ".join(bw[j1:j2]))
        known = pair in EXPECTED
        print("%s %s: source %r -> edition %r" % ("listed  " if known else "UNLISTED", label, pair[0], pair[1]))
        if not known:
            problems.append((label, pair))


def main():
    s_poem, e_poem = source_poem(), edition_poem()
    problems = []
    print("Poem: source %d stanzas, %d lines; edition %d stanzas, %d lines" % (
        len(s_poem), sum(map(len, s_poem)), len(e_poem), sum(len(l) for _, l in e_poem)))
    if [n for n, _ in e_poem] != list(range(1, len(e_poem) + 1)):
        problems.append(("poem", "stanza ids are not 1..n in order"))
    if len(s_poem) != len(e_poem):
        problems.append(("poem", "stanza count differs"))
    for (n, el), sl in zip(e_poem, s_poem):
        # undo the listed line splits so lines can be compared one to one
        joined, k = [], 0
        for i in range(len(sl)):
            if (n, i + 1) in SPLIT:
                print("listed   stanza %d line %d: split in two" % (n, i + 1))
                joined.append(el[k] + " " + el[k + 1]); k += 2
            elif k < len(el):
                joined.append(el[k]); k += 1
        joined += el[k:]
        if len(joined) != len(sl):
            problems.append(("stanza %d" % n, "line count differs: source %d, edition %d" % (len(sl), len(joined))))
            print("UNLISTED stanza %d: line count differs" % n)
        for i, (a, b) in enumerate(zip(sl, joined), 1):
            if a != b:
                diff_words("stanza %d line %d" % (n, i), a, b, problems)
    print("\n%d unlisted difference(s)." % len(problems))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
