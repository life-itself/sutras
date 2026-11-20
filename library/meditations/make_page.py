#!/usr/bin/env python3
"""Build meditations.md (the published edition) from library/meditations/edition-draft.md.

Usage: python3 library/meditations/make_page.py      (writes meditations.md at the repo root)

The draft holds the words (text, Hays's introduction, index, translator, copyright) and his notes as
footnote definitions. This script only changes markup and places the pieces: the page header, our
in brief, our introduction, the text with a passage link on every section, About this translation,
Source and licence, Download. It never edits a word. compare.py checks the result against the draft.

Passage markup (see docs/guides/making-an-edition.md, "Prose"): each section is its own
<div class="rs-passages">, starting with <a class="v" id="4.3" href="#4.3">4.3</a>. The printed
number ("3\\.") is dropped; the link shows the id a reader would cite.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
DRAFT = ROOT / "library" / "meditations" / "edition-draft.md"
OUT = ROOT / "meditations.md"

FRONTMATTER = """---
title: Meditations
description: "Marcus Aurelius’s notes to himself, written in Greek in the 170s, in Gregory Hays’s translation (2002). Complete, in twelve books, with Hays’s introduction and notes and an EPUB."
author: Marcus Aurelius (Marcus Aurelius Antoninus, 121–180 CE)
translator: Gregory Hays
date: "Written in Greek, probably in the 170s CE (Marcus died in 180)"
tradition: Stoicism
source: "Marcus Aurelius, Meditations: A New Translation, with an Introduction, by Gregory Hays (Modern Library, 2002; e-ISBN 1-58836-173-X). The EPUB of this book was supplied for this edition."
licence: "In copyright. The 2002 Modern Library edition (Random House) is marked all rights reserved; introduction and notes © 2002 Gregory Hays. Reproduced in full without permission. Editorial additions CC BY 4.0."
status: published
layout: plain
syntaxMode: md
scripts:
  - /js/reading.js
  - /js/edition.js
  - /js/notes/meditations.js
  - /js/notes.js
---
"""

HEADER = """
<div class="rs" data-rs-theme="personal" data-rs-rail="on" data-rs-dropcap="off">
<header class="rs-head"><div class="rs-wrap"><div class="rs-head-text">
<a class="rs-kicker" href="/">Sutras</a>
<h1>Meditations</h1>
<p class="rs-subtitle">Also known as <span lang="grc">Eis heauton</span>, “To Himself”</p>
<p class="rs-attribution">Marcus Aurelius<br>Translated by Gregory Hays</p>
</div></div></header>
<div class="rs-body"><div class="rs-wrap">
<nav class="rs-rail" aria-label="Contents"><p class="rs-rail-label">Contents</p><ol class="rs-toc" data-rs-auto></ol></nav>
<article class="rs-text">

<p class="rs-inbrief"><span class="rs-inbrief-label">In brief</span> Marcus Aurelius’s notes to himself, written as he ruled the Roman Empire and fought on its northern frontier. Complete, in twelve books, in Gregory Hays’s translation, with his introduction and notes; about 35,000 words.</p>

## Introduction

The *Meditations* are short entries that Marcus Aurelius, Roman emperor from 161 to 180, wrote for himself, in Greek, probably in the 170s. They were not written for publication, and the title is not his. Hays says the lost Greek manuscript used for the first printed edition was entitled *Eis heauton*, “To Himself,” and that the English title *Meditations* is “not only not original, but positively misleading.”

Hays calls the entries “spiritual exercises,” after Pierre Hadot: short pieces to hold steady against the stress and confusion of a day. Most are a line or a paragraph. Book 1 is the exception. In it Marcus lists what he owes to his family and teachers, one entry for each, and ends with the gods. The title “Debts and Lessons” is Hays’s, not Marcus’s. Books 2 to 12 have no such plan, and Hays finds no argument running through the whole.

Hays picks out the sense of mortality that runs through the book, and with it the worthlessness of worldly concerns. He points out that neither is peculiar to the Stoics; ancient literature is full of both. The book can be read a few entries at a time. If you want somewhere to start, [4.15](/meditations#4.15) (the lumps of incense on an altar) and [5.9](/meditations#5.9) (philosophy as “the sponge and egg white that relieve ophthalmia”) are short and typical.

<p class="rs-signed">Editors’ introduction, drafted with an AI assistant. November 2026.</p>

## The text

Each entry is numbered as Hays numbers it: book and entry, so [4.3](/meditations#4.3) is the third entry of Book 4. In eleven places Hays splits one traditional entry in two and numbers the second part with an “a” (4.49a, for example); his introduction explains this, and the ids follow him. Hays’s notes are footnotes, placed beside the words they explain.

Jump to a book:

- [Book 1: Debts and Lessons](/meditations#1)
- [Book 2: On the River Gran, Among the Quadi](/meditations#2)
- [Book 3: In Carnuntum](/meditations#3)
- [Book 4](/meditations#4)
- [Book 5](/meditations#5)
- [Book 6](/meditations#6)
- [Book 7](/meditations#7)
- [Book 8](/meditations#8)
- [Book 9](/meditations#9)
- [Book 10](/meditations#10)
- [Book 11](/meditations#11)
- [Book 12](/meditations#12)

"""

ABOUT = """
## About this translation

*Meditations: A New Translation, with an Introduction, by Gregory Hays* was published by The Modern Library in 2002. Hays wrote its introduction, its notes and an index of persons. The book also has a short note on the translator (he was then assistant professor of classics at the University of Virginia). All of them are here, after the text: his introduction in full, then the index, then the note on the translator. The index gives, for each person, the entries where they appear, and those numbers link to the text.

"""

SOURCE = """
## Source and licence

**Source.** The text was taken from the EPUB of the 2002 Modern Library edition (a conversion of the Kindle edition) on 20 November 2026, and checked against it word for word by script. Its words are Hays’s, as printed, except for the few fixes listed in the [edition notes](https://github.com/life-itself/sutras/blob/main/library/meditations/NOTES.md). Small capitals are set as capitals; nothing else in the words has been changed.

**Licence.** The 2002 Modern Library edition is marked “All rights reserved,” and its introduction and notes are © 2002 Gregory Hays. The book is in copyright. It is published here in full, without the permission of the rights holder. If you hold the rights and want this changed, please [open an issue](https://github.com/life-itself/sutras/issues). Our own additions (the in brief, the editors’ introduction, the contents list and this section) are free to reuse under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Download

[Meditations (EPUB)](/downloads/meditations.epub): everything on this page, including the translation, which is in copyright (see above).

</article></div></div>
</div>

"""

BOOK_NOTE = re.compile(r"\[\^book\d\]")
FIRST_NOTE = re.compile(r"^\[\^[^\]]+\]:")
SECTION_ANCHOR = re.compile(r'^<a id="([^"]+)"></a>$')
PRINTED_NUMBER = re.compile(r"^(\d+a?)\\\.\s*")
BOOK_ID = re.compile(r"^\d+$")
INDEX_REF = re.compile(r"\((\d+\.\d+[a-z]?(?:, \d+\.\d+[a-z]?)*)\)")


def split_draft(text):
    """Return (text_lines, intro_lines, index_lines, translator_lines, copyright_lines, notes_lines)."""
    lines = text.split("\n")
    marks = {}
    for i, line in enumerate(lines):
        if line in ("## Introduction", "## Index of Persons", "## About the Translator", "## Copyright"):
            marks[line] = i
        if FIRST_NOTE.match(line) and "first_note" not in marks:
            marks["first_note"] = i
    start = lines.index('<a id="1"></a>')
    text_end = marks["## Introduction"]
    return (
        lines[start:text_end],
        lines[marks["## Introduction"]:marks["## Index of Persons"]],
        lines[marks["## Index of Persons"]:marks["## About the Translator"]],
        lines[marks["## About the Translator"]:marks["## Copyright"]],
        lines[marks["## Copyright"]:marks["first_note"]],
        lines[marks["first_note"]:],
    )


def build_text(lines):
    """The twelve books, each section in its own passage container."""
    out, ids, open_section, pending_note = [], [], False, ""

    def close():
        nonlocal open_section
        if open_section:
            while out and out[-1] == "":
                out.pop()
            out.extend(["", "</div>", ""])
            open_section = False

    i = 0
    while i < len(lines):
        line = lines[i]
        m = SECTION_ANCHOR.match(line)
        if m and BOOK_ID.match(m.group(1)):
            close()
            out.extend([line, ""])
            i += 1
            while lines[i] == "":
                i += 1
            assert lines[i].startswith("## Book "), lines[i]
            # A note on a book title cannot sit in the heading: the contents rail copies the heading's text.
            # It goes on the book's first entry instead.
            bm = BOOK_NOTE.search(lines[i])
            if bm:
                pending_note = bm.group(0)
            out.extend([BOOK_NOTE.sub("", lines[i]), ""])
            i += 1
            continue
        if m:
            close()
            pid = m.group(1)
            ids.append(pid)
            i += 1
            while lines[i] == "":
                i += 1
            first = lines[i]
            pm = PRINTED_NUMBER.match(first)
            assert pm and pm.group(1) == pid.split(".", 1)[1], (pid, first[:60])
            rest = first[pm.end():]
            if pending_note:
                rest += pending_note
                pending_note = ""
            out.extend(['<div class="rs-passages">', "", f'<a class="v" id="{pid}" href="#{pid}">{pid}</a>', rest])
            open_section = True
            i += 1
            continue
        if open_section and line == "" and out[-1] == "":
            i += 1
            continue
        out.append(line)
        i += 1
    close()
    # The book heading must not sit inside a passage container.
    body = "\n".join(out).strip("\n") + "\n"
    if len(ids) != 499:  # 488 standard sections and 11 split entries (a)
        raise SystemExit(f"expected 499 sections, found {len(ids)}")
    return body


def demote(lines):
    """Hays's sub-headings move down a level, under our About this translation."""
    return ["#" + l if l.startswith("### ") else l for l in lines]


def link_index(lines):
    out = []
    for line in lines:
        out.append(INDEX_REF.sub(lambda m: "(" + ", ".join(f"[{n}](/meditations#{n})" for n in m.group(1).split(", ")) + ")", line))
    return out


def main():
    draft = DRAFT.read_text(encoding="utf-8")
    text_lines, intro, index, translator, _copyright, notes = split_draft(draft)

    # Hays's byline and the intro heading go; the heading is ours.
    intro = [l for l in intro if l not in ("## Introduction", "*Gregory Hays*")]
    intro = demote(intro)
    index = [l for l in index if l != "## Index of Persons"]
    index = link_index(index)
    translator = [l for l in translator if l != "## About the Translator"]

    body_text = build_text(text_lines)
    parts = [
        FRONTMATTER,
        HEADER,
        body_text,
        "\n",
        ABOUT.strip("\n") + "\n\n",
        "### Introduction by Gregory Hays\n\n",
        "\n".join(intro).strip("\n") + "\n\n",
        "### Index of Persons\n\n",
        "\n".join(index).strip("\n") + "\n\n",
        "### About the translator\n\n",
        "\n".join(translator).strip("\n") + "\n\n",
        SOURCE.lstrip("\n"),
        "\n".join(notes).strip("\n") + "\n",
    ]
    OUT.write_text("".join(parts), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
