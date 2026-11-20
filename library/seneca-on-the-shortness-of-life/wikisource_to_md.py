#!/usr/bin/env python3
"""Turn the Wikisource wikitext of Basore's On the Shortness of Life into Markdown.

Usage: python3 library/seneca-on-the-shortness-of-life/wikisource_to_md.py   (from the repo root)

Reads wikisource/chapter-*.wiki (the source as fetched) and prints, for each chapter, its
paragraphs as Markdown, followed by all of Basore's notes as footnotes [^1]..[^n] in order.
Used once to make the first draft of the essay section of seneca-on-the-shortness-of-life.md,
and again by compare.py, which compares the edition's words with this output.

What it does to the wikitext, and nothing more:
- drops the {{header}} block, the chapter number ('''1.'''), ==Footnotes== and {{reflist}};
- {{sc|x}} and {{smaller|x}} -> x; {{tooltip|original|English}} -> original (the English
  glosses are Wikisource contributors' additions, not Basore's); {{em|n}} and {{left|..}} dropped;
- ''x'' -> *x*; <br/> -> a Markdown line break; {{center block|..}} -> a blockquote;
- <ref>..</ref> -> footnote markers and definitions.
Quote marks are left straight here; the edition makes them curly (compare.py normalises them).
"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
CHAPTERS = "I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI XVII XVIII XIX XX".split()


def inline(s):
    s = re.sub(r"\{\{tooltip\|([^|{}]*)\|[^{}]*\}\}", r"\1", s)
    s = re.sub(r"\{\{(?:sc|smaller)\|([^{}]*)\}\}", r"\1", s)
    s = re.sub(r"\{\{em\|\d+\}\}", "", s)
    s = re.sub(r"\{\{left\|(.*?)\|offset=[^}]*\}\}", r"\1", s, flags=re.S)
    s = re.sub(r"''(.+?)''", r"*\1*", s)
    return s


def chapter(c):
    t = (HERE / "wikisource" / ("chapter-%s.wiki" % c)).read_text(encoding="utf-8")
    t = re.sub(r"(?s)\A\{\{header.*?\n\}\}\n", "", t)
    t = re.sub(r"(?s)==Footnotes==.*", "", t)
    t = re.sub(r"\A'''\d+\.'''\s*", "", t.strip())
    notes = []

    def ref(m):
        notes.append(inline(m.group(1)).strip().replace("<br/>", "  \n    "))
        return "[^%d]" % (len(notes))

    t = re.sub(r"(?s)<ref>(.*?)</ref>", ref, t)
    paras = []
    for p in re.split(r"\n\s*\n", t):
        p = p.strip()
        if not p:
            continue
        m = re.match(r"(?s)\{\{center block\|(.*)\}\}\Z", p)
        if m:
            lines = [l.strip() for l in m.group(1).split("<br/>")]
            p = "\n".join("> " + inline(l) + ("  " if i < len(lines) - 1 else "") for i, l in enumerate(lines))
        else:
            p = inline(p).replace("<br/>", "  \n")
        paras.append(p)
    return paras, notes


def build():
    """[(roman, [paragraphs])], [notes], with footnote markers numbered through the whole essay."""
    out, allnotes = [], []
    for c in CHAPTERS:
        paras, notes = chapter(c)
        base = len(allnotes)
        paras = [re.sub(r"\[\^(\d+)\]", lambda m: "[^%d]" % (base + int(m.group(1))), p) for p in paras]
        out.append((c, paras))
        allnotes += notes
    return out, allnotes


if __name__ == "__main__":
    chapters, notes = build()
    for n, (c, paras) in enumerate(chapters, 1):
        print('<h3 id="%d">%s</h3>\n' % (n, c))
        for p in paras:
            print(p + "\n")
    for i, note in enumerate(notes, 1):
        print("[^%d]: %s\n" % (i, note))
