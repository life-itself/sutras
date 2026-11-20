"""Compare the words of dhammapada.md with edition-draft.md (the 2011 text, unchanged).

usage: python3 -I library/dhammapada/compare.py   (run from the repo root; exit status 1 on any unlisted difference)

Checks, word by word (punctuation, markup, layout and labels ignored):
- the verses: every verse of the draft, 1 to 423, against the page's verses;
- the translator's matter (preface, introduction, historical notes, abbreviations, glossary,
  bibliography) against the draft;
- the end notes, with the "Translator’s note." label removed, against the draft's notes;
- the licence quote against the copyright page of the draft.
Headings are compared not at all: the page renames two of them (see NOTES.md).
"""
import difflib, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
PAGE = HERE.parent.parent / "dhammapada.md"
DRAFT = HERE / "edition-draft.md"

LABEL = re.compile(r"\*Translator’s note( on [^*]+)?\.\*\s*")
CITE = re.compile(r'^<p class="cite">.*</p>$')


def tokens(text):
    lines = []
    for line in text.split("\n"):
        if line.startswith("#") or CITE.match(line.strip()):
            continue
        lines.append(line)
    text = "\n".join(lines)
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("&emsp;", " ").replace("&nbsp;", " ")
    text = re.sub(r"\[\^[^\]]+\]:?", " ", text)
    text = LABEL.sub("", text)
    text = text.replace("’", "'").replace("‘", "'")
    return re.findall(r"[\w']+", text.lower())


def between(text, start, end):
    i = text.index(start)
    j = text.index(end, i) if end else len(text)
    return text[i:j]


def footnotes(text):
    return "\n".join(m.group(0) for m in re.finditer(r"^\[\^[^\n]*(?:\n    [^\n]*)*", text, re.M))


def compare(name, a, b, report):
    ta, tb = tokens(a), tokens(b)
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    diffs = [op for op in sm.get_opcodes() if op[0] != "equal"]
    report.append(f"{name}: {len(ta)} words on the page, {len(tb)} in the draft, {len(diffs)} differing span(s)")
    for tag, i1, i2, j1, j2 in diffs[:20]:
        report.append(f"  {tag}: page {' '.join(ta[i1:i2])!r} / draft {' '.join(tb[j1:j2])!r}")
    return len(diffs)


def main():
    page = PAGE.read_text(encoding="utf-8")
    draft = DRAFT.read_text(encoding="utf-8")
    draft = draft[draft.index("\n## I : Pairs\n") + 1:]
    report, failed = [], 0

    # the passage numbers are the page's own links; the draft has them only as anchors
    page_verses = re.sub(r'<a class="v"[^>]*>\d+</a>', "", between(page, "## The verses", "## About this translation"))
    draft_verses = between(draft, "## I : Pairs", "## Preface")
    failed += compare("verses", page_verses, draft_verses, report) > 0

    page_about = between(page, "## About this translation", "## Source and licence")
    page_about = page_about[page_about.index("### Translator’s preface"):].replace("[^e1]", "").replace("| Abbreviation | Stands for |", "| | |")
    draft_about = between(draft, "## Preface", "## Copyright")
    draft_about = draft_about[:draft_about.index("\n[^1-2]:")] if "\n[^1-2]:" in draft_about else draft_about
    notes_at = draft.index("\n[^1-2]:")
    draft_notes = draft[notes_at:]
    page_notes = "\n".join(l for l in page[page.index("\n[^1-2]:"):].split("\n") if "[^e1]:" not in l)
    failed += compare("translator's matter", page_about, draft_about, report) > 0
    failed += compare("end notes", page_notes, draft_notes, report) > 0

    page_licence = between(page, "> Copyright ©", "This edition is free of charge.")
    draft_licence = between(draft, "Copyright ©", "### Additional Resources").replace("### For Free Distribution", "For Free Distribution")
    failed += compare("licence", page_licence, draft_licence, report) > 0

    # Footnote markers: the same labels, each used once, on the page and in the draft.
    labels_page = re.findall(r"\[\^([^\]]+)\]", page_verses)
    labels_draft = re.findall(r"\[\^([^\]]+)\]", draft_verses)
    same = labels_page == labels_draft
    report.append(f"footnote markers in the verses: {len(labels_page)} on the page, {len(labels_draft)} in the draft, same order: {same}")
    failed += not same

    print("\n".join(report))
    print("\nfailed" if failed else "\n0 unlisted differences")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
