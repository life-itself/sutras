#!/usr/bin/env python3
"""Compare the words of meditations.md with the draft they were built from, word for word.

Usage: python3 library/meditations/compare.py      (run from the repo root; exit status 1 on any unlisted difference)

Compared: the twelve books, and Hays's introduction, index and note on the translator. Not compared: our own
parts (the header, in brief, introduction, contents list, About this translation, Source and licence, Download),
which are ours and not Hays's words. Markup is removed on both sides: passage links (their numbers are ids, not
words), footnote markers and definitions, the printed section numbers, links and emphasis, and the book title
notes that make_page.py moves onto each book's first entry.

Any difference must be listed in KNOWN below, with the reason; the script fails on anything else.
"""
import difflib, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DRAFT = ROOT / "library" / "meditations" / "edition-draft.md"
PAGE = ROOT / "meditations.md"

# Differences that are expected, with the reason. Each is a heading we wrote over Hays's, not his words.
KNOWN = [
    ("insert", "", "by", "our heading “Introduction by Gregory Hays”; Hays's own heading is “Introduction”"),
    ("replace", "Translator", "translator", "our heading “About the translator”; Hays's is “About the Translator”"),
]


def body(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n.*?\n---\n", text, re.S)
    return text[m.end():] if m else text


def sections(text, start, end):
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j]


def footnote_free(text):
    """Drop footnote definitions (from the first one to the end)."""
    m = re.search(r"^\[\^[^\]]+\]:", text, re.M)
    return text[: m.start()] if m else text


def words(text):
    t = text
    t = re.sub(r"<a [^>]*>.*?</a>", " ", t)               # passage links and anchors: ids, not words
    t = re.sub(r"<[^>]+>", " ", t)                        # any other tag
    t = re.sub(r"\[\^[^\]]+\]", "", t)                    # footnote markers
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)        # links: keep the words
    t = re.sub(r"(?m)^\s*(\d+a?)\\\.\s*", "", t)          # printed section numbers at the start of a line
    t = re.sub(r"(?m)^\s*\d+a?\\\.\s*", "", t)
    t = re.sub(r"(?m)^#+\s*", "", t)                      # heading marks
    t = t.replace("\\", "")                               # escapes (\[ and the like)
    t = re.sub(r"[*_`>]", " ", t)                         # emphasis, quotes-as-blockquotes
    t = t.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    t = re.sub(r"[‘’]", "'", t)
    t = re.sub(r"[“”]", '"', t)
    t = re.sub(r"\s+", " ", t)
    return t.split(" ")


def main():
    draft = footnote_free(body(DRAFT))
    page = footnote_free(body(PAGE))

    # the draft's text and Hays's back matter, in the order they appear in the draft
    d = (sections(draft, '<a id="1"></a>', "## Introduction")
         + sections(draft, "## Introduction", "## Copyright"))
    # the same parts on the page: the books, then Hays's introduction, index and translator note
    p = (sections(page, '<a id="1"></a>', "## About this translation")
         + sections(page, "### Introduction by Gregory Hays", "## Source and licence"))
    # the page's copy of the draft's introduction drops its own heading and byline, and the index and
    # translator note are headed differently; drop headings on both sides so only the words are compared
    dw = [w for w in words(d) if w]
    pw = [w for w in words(p) if w]

    unlisted = []
    for op, a1, a2, b1, b2 in difflib.SequenceMatcher(None, dw, pw, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        a, b = " ".join(dw[a1:a2]), " ".join(pw[b1:b2])
        if any(op == k[0] and a == k[1] and b == k[2] for k in KNOWN):
            continue
        unlisted.append((op, a, b))

    print(f"draft words: {len(dw)}; page words: {len(pw)}")
    for op, a, b in unlisted:
        print(f"  {op}: draft {a[:80]!r} / page {b[:80]!r}")
    if not unlisted:
        print(f"0 unlisted differences ({len(KNOWN)} listed in KNOWN)")
    return 1 if unlisted else 0


if __name__ == "__main__":
    sys.exit(main())
