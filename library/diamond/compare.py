#!/usr/bin/env python3
"""Compare a Diamond Sutra edition with its source, word for word.

Usage (from the repo root):
  python3 library/diamond/compare.py diamond            # Thich Nhat Hanh: diamond.md
  python3 library/diamond/compare.py diamond-red-pine   # Red Pine: diamond-red-pine.md
  python3 library/diamond/compare.py <slug> --emit      # print the source as edition Markdown

The sources are ebook PDFs from terebess.hu, kept in library/<slug>/. `source.txt` beside each is
`pdftotext -layout` of the PDF (poppler), unedited. This script reads the sutra out of it (the 32
sections, their paragraphs and verses), joins lines, and compares the words with the section
"## The sutra" of <slug>.md. Quote style, dashes and whitespace are normalised first. Every
difference must be either reverted or listed in library/<slug>/NOTES.md and in EXPECTED below.
Exit status 1 if there are unlisted differences.

A per-text stand-in for scripts/compare-source until that is generalised (bead sutras-m2v.7.8).
"""
import difflib, re, sys

NUMBERS = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "ELEVEN",
           "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN", "EIGHTEEN",
           "NINETEEN", "TWENTY"]
NUMBERS += ["TWENTY-" + n for n in NUMBERS[:9]] + ["THIRTY"] + ["THIRTY-" + n for n in NUMBERS[:2]]

# Changes we made on purpose, per text (all listed in NOTES.md): (source words, edition words)
EXPECTED = {
    "diamond": set(),
    "diamond-red-pine": {
        ("'billionworld", "'billion-world"),  # chapter 30; hyphenated two lines earlier
    },
}

# Artefacts of the PDF conversion, repaired while reading the source (listed in NOTES.md)
def repair(s):
    s = re.sub(r"\bM ([a-z])", r"M\1", s)       # the converter splits a capital M from its word
    return s


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-").replace("\xa0", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return re.sub(r"([.,?!]) (['\"])(?=['\"]*( |$))", r"\1\2", s)  # "bodhisattva. '": a space before a closing quote


def join(lines):
    """Join wrapped lines. A line ending in a hyphen keeps it and joins without a space: the PDF
    is a reflowed ebook, so a hyphen at a line end is the book's own (e.g. World-/Honored)."""
    out = ""
    for l in lines:
        l = l.strip()
        if not out:
            out = l
        elif out.endswith("-") and not out.endswith(" -"):
            out += l
        else:
            out += " " + l
    return out


def read_tnh(text):
    start = text.index("THE VAJRACCHEDIKA PRAJÑAPARAM ITA\n", text.index("COMMENTARIES") + 1)
    end = text.index("COMMENTARIES", start)
    lines = text[start:end].split("\n")[2:]
    sections, blocks, cur, verse = [], None, [], None

    def flush():
        nonlocal cur
        if cur:
            blocks.append(("p", join(cur)))
        cur = []

    prev_blank = False
    for raw in lines:
        raw = repair(raw.replace("\f", ""))
        m = re.fullmatch(r"\s{10,}(\d{1,2})\s*", raw)
        if m:
            flush()
            if verse:
                blocks.append(("v", verse)); verse = None
            blocks = []
            sections.append((int(m.group(1)), blocks))
            prev_blank = True  # the blank line after a number is not a verse break
            after_number = True
            continue
        if not raw.strip():
            if verse:
                blocks.append(("v", verse)); verse = None
            elif not (sections and not blocks and not cur):
                flush()
                prev_blank = "verse-next"
            continue
        indent = len(raw) - len(raw.lstrip())
        if prev_blank == "verse-next" and indent >= 4 or verse is not None:
            verse = (verse or []) + [raw.strip()]
            prev_blank = False
            continue
        prev_blank = False
        if indent >= 2 and cur:
            flush()
        cur.append(raw)
    flush()
    return sections


def read_red_pine(text):
    start = text.index("ONE: Thus have I heard")
    end = text.index("TRANSLATOR’S PREFACE", start)
    lines = text[start:end].split("\n")
    sections, blocks, cur, verse = [], None, [], None
    head = re.compile(r"(%s): " % "|".join(re.escape(n) for n in sorted(NUMBERS, key=len, reverse=True)))

    def flush():
        nonlocal cur
        if cur:
            blocks.append(("p", join(cur)))
        cur = []

    for raw in lines:
        raw = repair(raw.replace("\f", ""))
        m = head.match(raw.strip())
        if m and raw.strip() == raw.strip() and m.start() == 0 and len(raw) - len(raw.lstrip()) == 0:
            flush()
            if verse:
                blocks.append(("v", verse)); verse = None
            blocks = []
            sections.append((NUMBERS.index(m.group(1)) + 1, blocks))
            cur = [raw.strip()[m.end():]]
            continue
        if not raw.strip():
            if verse:
                blocks.append(("v", verse)); verse = None
            flush()
            continue
        indent = len(raw) - len(raw.lstrip())
        if indent >= 5 and not cur or verse is not None:
            verse = (verse or []) + [raw.strip()]
            continue
        if indent >= 2 and cur:  # a new paragraph straight after a page break, with no blank line
            flush()
        cur.append(raw)
    flush()
    return sections


def source(slug):
    text = open("library/%s/source.txt" % slug, encoding="utf-8").read()
    return read_tnh(text) if slug == "diamond" else read_red_pine(text)


def emit(sections):
    out = []
    for n, blocks in sections:
        first = True
        for kind, b in blocks:
            if kind == "p":
                out.append(('<a class="v" id="%d" href="#%d">%d</a>\n' % (n, n, n) if first else "") + b)
            else:
                out.append("  \n".join("> " + l for l in b))  # a verse (gatha): a block quote
            first = False
    return "\n\n".join(out)


def edition(slug):
    t = open(slug + ".md", encoding="utf-8").read()
    body = t[t.index("## The sutra"):t.index("## About this translation")]
    body = re.sub(r"\[\^[^\]]+\]", "", body)
    sections = []
    for block in body.split("\n\n"):
        m = re.match(r'\s*<a class="v" id="(\d+)" href="#\1">\1</a>\n', block)
        if m:
            sections.append((int(m.group(1)), []))
            block = block[m.end():]
        if not sections or not block.strip() or block.lstrip().startswith(("<", "#")):
            continue
        lines = block.strip().split("\n")
        if lines[0].startswith("> "):
            sections[-1][1].append(("v", [l[2:].strip() for l in lines]))
        else:
            sections[-1][1].append(("p", " ".join(l.strip() for l in lines)))
    return sections


def words(blocks):
    return norm(" ".join(b if k == "p" else " ".join(b) for k, b in blocks))


def main(slug):
    src, ed = source(slug), edition(slug)
    expected = EXPECTED[slug]
    problems = []
    print("Source: %d sections, %d paragraphs/verses; edition: %d sections, %d" % (
        len(src), sum(len(b) for _, b in src), len(ed), sum(len(b) for _, b in ed)))
    if [n for n, _ in src] != list(range(1, 33)):
        problems.append(("source", "sections are not 1..32: %s" % [n for n, _ in src]))
    if [n for n, _ in ed] != list(range(1, 33)):
        problems.append(("edition", "section ids are not 1..32"))
    for (n, sb), (m, eb) in zip(src, ed):
        if len(sb) != len(eb):
            print("UNLISTED section %d: block count differs: source %d, edition %d" % (n, len(sb), len(eb)))
            problems.append((n, "blocks"))
        sk, ek = [k for k, _ in sb], [k for k, _ in eb]
        if sk != ek:
            print("UNLISTED section %d: verse/paragraph pattern differs: %s / %s" % (n, sk, ek))
            problems.append((n, "pattern"))
        aw, bw = words(sb).split(), words(eb).split()
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, aw, bw, autojunk=False).get_opcodes():
            if op == "equal":
                continue
            pair = (" ".join(aw[i1:i2]), " ".join(bw[j1:j2]))
            if i1 == i2 or j1 == j2:
                pair = (" ".join(aw[max(i1 - 1, 0):i2]), " ".join(bw[max(j1 - 1, 0):j2]))
            known = pair in expected
            print("%s section %d: source %r -> edition %r" % ("listed  " if known else "UNLISTED", n, pair[0], pair[1]))
            if not known:
                problems.append((n, pair))
    print("\n%d unlisted difference(s)." % len(problems))
    return 1 if problems else 0


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in EXPECTED:
        sys.exit(__doc__)
    if "--emit" in sys.argv:
        print(emit(source(sys.argv[1])))
    else:
        sys.exit(main(sys.argv[1]))
