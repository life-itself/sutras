"""Build dhammapada.md (the reading page) from edition-draft.md and page-template.md.

usage: python3 -I library/dhammapada/build_page.py   (run from the repo root)

Words are taken from edition-draft.md by script, never retyped. What changes is layout only:
- each verse gets a passage link (<a class="v" id="N" href="#N">N</a>), in a <div class="rs-verse">
  per chapter; the book's cite lines ("1-2") are dropped, since every verse now has its own number;
- chapter headings become ### headings, so they can be linked;
- the translator's end notes become Markdown footnotes, each opening "Translator’s note.";
- the translator's front and back matter go under About this translation, as ### headings;
- the copyright page's licence statement is quoted in full under Source and licence.
Placeholders in page-template.md: {{VERSES}}, {{TRANSLATOR}}, {{LICENCE}}, {{NOTES}}.
"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
DRAFT = HERE / "edition-draft.md"
TEMPLATE = HERE / "page-template.md"
OUT = HERE.parent.parent / "dhammapada.md"

ANCHOR = re.compile(r'^<a id="(\d+)"></a>((?:<a id="\d+"></a>)*)$')
BLANK = "&nbsp;"
CITE = re.compile(r'^<p class="cite">[^<]*</p>$')


def stanza(lines):
    """One verse (or merged verses): link lines first, then the verse lines, as the draft has them.

    A blank line inside a verse (the book sets off a list or a second voice) becomes a line holding
    a non-breaking space, so the verse stays one stanza for scripts/check and still shows a gap."""
    ids, body = [], []
    for line in lines:
        m = ANCHOR.match(line)
        if m:
            ids += re.findall(r'id="(\d+)"', line)
        else:
            body.append(line)
    out = [f'<a class="v" id="{i}" href="#{i}">{i}</a>' for i in ids]
    for line in body:
        if line.strip():
            out.append(line)
        elif out and out[-1] != BLANK:
            out.append(BLANK)
    while out and out[-1] == BLANK:
        out.pop()
    return "\n".join(l if i == len(out) - 1 or l.endswith("  ") else l + "  " for i, l in enumerate(out))


def verses(block):
    """Split the draft's verse region into chapters, each a list of stanzas."""
    chapters, current = [], None
    stanzas, cur = [], None
    out = []
    for line in block.split("\n"):
        if line.startswith("## "):
            if cur:
                stanzas.append(cur)
                cur = None
            if current is not None:
                out.append((current, stanzas))
            current, stanzas = line[3:].strip(), []
            continue
        if CITE.match(line):
            continue
        if ANCHOR.match(line):
            if cur:
                stanzas.append(cur)
            cur = [line]
            continue
        if cur is not None:
            cur.append(line)
    if cur:
        stanzas.append(cur)
    out.append((current, stanzas))
    chapters = []
    for title, sts in out:
        rendered = []
        for st in sts:
            while st and st[-1] == "":
                st.pop()
            rendered.append(stanza(st))
        chapters.append(f"### {title}\n\n<div class=\"rs-verse\">\n\n" + "\n\n".join(rendered) + "\n</div>")
    return "\n\n".join(chapters)


def main():
    text = DRAFT.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    body = text[m.end():]

    first = body.index("\n## I : Pairs\n") + 1
    preface = body.index("\n## Preface\n") + 1
    copyright_at = body.index("\n## Copyright\n") + 1
    notes_at = body.index("\n[^1-2]:")
    verse_block = body[first:preface]
    front_back = body[preface:copyright_at]
    copy_block = body[copyright_at:notes_at]
    note_block = body[notes_at:].strip("\n")

    # Translator's matter: the book's headings one level down, Introduction renamed to avoid
    # clashing with our own Introduction.
    translator = front_back.strip("\n")
    translator = re.sub(r"^## Introduction$", "### Translator’s introduction", translator, flags=re.M)
    translator = re.sub(r"^## ", "### ", translator, flags=re.M)
    translator = re.sub(r"^### Preface$", "### Translator’s preface", translator, flags=re.M)

    # The licence: the copyright page from its first line to Additional Resources, in full,
    # quoted (the "For Free Distribution" heading becomes a plain line inside the quote).
    cl = copy_block.strip("\n")
    cl = cl[:cl.index("\n### Additional Resources")].rstrip()
    cl = cl.replace("## Copyright\n\n", "", 1)
    cl = cl.replace("### For Free Distribution", "For Free Distribution")
    licence = "\n".join(("> " + l).rstrip() for l in cl.split("\n"))

    # Footnotes: label each as the translator's note.
    notes = []
    for para in re.split(r"\n(?=\[\^)", note_block):
        para = para.rstrip()
        mm = re.match(r"\[\^([^\]]+)\]: (.*)", para, re.S)
        if not mm:
            raise SystemExit("unexpected note: " + para[:60])
        notes.append(f"[^{mm.group(1)}]: *Translator’s note.* {mm.group(2)}")

    template = TEMPLATE.read_text(encoding="utf-8")
    page = (template.replace("{{VERSES}}", verses(verse_block))
            .replace("{{TRANSLATOR}}", translator)
            .replace("{{LICENCE}}", licence)
            .replace("{{NOTES}}", "\n\n".join(notes) + "\n"))
    OUT.write_text(page, encoding="utf-8")
    print("wrote", OUT.relative_to(HERE.parent.parent), len(page), "chars")
    assert not re.search(r"\{\{\w+\}\}", page), "placeholder left in page"


if __name__ == "__main__":
    main()
