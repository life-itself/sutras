#!/usr/bin/env python3
"""Compare the Seneca edition with its source, word for word.

Usage: python3 library/seneca-on-the-shortness-of-life/compare.py     (from the repo root)

Reads seneca-on-the-shortness-of-life.md and the Wikisource wikitext in wikisource/ (via
wikisource_to_md.py) and prints every difference in the words of the essay, in where Basore's
note markers sit, and in the words of his notes. Quote style, dashes, italics and whitespace are
normalised first, so only real changes show. The editors' notes ([^e1].. and their text) are
ours and are left out. Each difference must be either reverted or listed in NOTES.md; exit
status 1 if there is one that is not in EXPECTED below.

A stopgap until scripts/compare-source handles more than one text (bead for the site track).
"""
import difflib, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import wikisource_to_md as W  # noqa: E402

EDITION = HERE.parent.parent / "seneca-on-the-shortness-of-life.md"

# Changes we made on purpose, all listed in NOTES.md: (where, source words, edition words)
EXPECTED = {
    # note 10 sits on "Antony", as in Forum Romanum, not on "Paulus"
    ("essay", "Paulus, [^] and", "Paulus, and"),
    ("essay", "Antony. When", "Antony. [^] When"),
    # Basore's note on Liternum restored; the Caligula note moved back to "alive" (chapter 17/18)
    ("essay", "alive and", "alive [^] and"),
    ("note 40", "", "Disgusted with politics, he died in exile at Liternum."),
    # opening quotation mark restored, chapter 17
    ("essay", "them: How long", 'them: "How long'),
    # doubled full stop in note 29
    ("note 29", 'humana societatem.."', 'humana societatem."'),
}


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("—", " — ").replace("–", "-").replace("\xa0", " ").replace("*", "")
    s = re.sub(r"\[\^\d+\]", " [^] ", s)    # note markers, numbering ignored, placement kept
    s = re.sub(r"(?m)^> ?", "", s)
    return re.sub(r"\s+", " ", s).strip()


def source():
    chapters, notes = W.build()
    return " ".join(norm(p) for _, ps in chapters for p in ps), [norm(n) for n in notes]


def edition():
    t = EDITION.read_text(encoding="utf-8")
    essay = t[t.index("## The essay"):t.index("## About this translation")]
    essay = re.sub(r"\[\^e\d+\]", "", essay)
    essay = re.sub(r'<h3 id="\d+">[IVXL]+</h3>', "", essay).replace("## The essay", "")
    notes = {}
    for m in re.finditer(r"(?ms)^\[\^(\d+)\]: (.*?)(?=^\[\^|\Z)", t):
        notes[int(m.group(1))] = norm(m.group(2))
    ids = [int(i) for i in re.findall(r'<h3 id="(\d+)">', t)]
    return norm(essay), [notes[k] for k in sorted(notes)], ids


def diff(label, a, b, problems):
    aw, bw = a.split(), b.split()
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, aw, bw, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        pair = (label, " ".join(aw[max(i1 - 1, 0):i2 + 1]), " ".join(bw[max(j1 - 1, 0):j2 + 1]))  # one word of context
        known = pair in EXPECTED
        print("%s %s: source %r -> edition %r" % ("listed  " if known else "UNLISTED", *pair))
        if not known:
            problems.append(pair)


def main():
    s_essay, s_notes = source()
    e_essay, e_notes, ids = edition()
    problems = []
    print("Chapters: edition ids %s" % ("1..20 in order" if ids == list(range(1, 21)) else ids))
    if ids != list(range(1, 21)):
        problems.append(("ids", "", ""))
    print("Notes: source %d, edition %d" % (len(s_notes), len(e_notes)))
    diff("essay", s_essay, e_essay, problems)
    # line the notes up: the edition restores note 40, which the source lacks
    s_notes = s_notes[:39] + [""] + s_notes[39:]
    for k, (a, b) in enumerate(zip(s_notes, e_notes), 1):
        if a != b:
            if not a:
                pair = ("note %d" % k, "", b)
                known = pair in EXPECTED
                print("%s note %d: missing in source -> edition %r" % ("listed  " if known else "UNLISTED", k, b))
                if not known:
                    problems.append(pair)
            else:
                diff("note %d" % k, a, b, problems)
    if len(s_notes) != len(e_notes):
        problems.append(("notes", "count", ""))
    print("\n%d unlisted difference(s)." % len(problems))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
