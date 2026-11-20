# Dhammapada source: Thanissaro Bhikkhu

The chosen translation (Rufus, 2026-11-20). Bhikkhu Sujato's CC0 translation is kept beside it in `sujato/` as a parallel, for a later side-by-side view (see `sujato/NOTES.md`).

## The file

- **Book:** *Dhammapada: A Translation*, by Thanissaro Bhikkhu (Geoffrey DeGraff). Publisher, as stated in the EPUB: Metta Forest Monastery, Valley Center, California. Preface dated December 1997.
- **Edition:** "Copyright © 1998 Thanissaro Bhikkhu (Revised edition, 2011)" (the book's copyright page). An EPUB made with Sigil 0.4.2.
- **Supplied by:** Rufus, 2026-11-20, as an EPUB downloaded from Anna's Archive (MD5 `a1ca4b839016df1f434e2a085f107bae`, per its file name). Kept here as `thanissaro-dhammapada-2011.epub` (SHA-256 `992740d7033628333bbb7b8f78441ccdebd10b4649b016c31eadcb0a10df8600`). EPUBs are git-ignored (`library/**/*.epub`), so the file stays on this machine only.

## Licence, as stated in the book

The copyright page:

> Copyright © 1998 Thanissaro Bhikkhu (Revised edition, 2011)
>
> For Free Distribution
>
> You may copy, reformat, reprint, republish, and redistribute this work in any medium whatsoever without the author's permission, provided that: (1) such copies, etc. are made available *free of any charge*; (2) any translations of this work state that they are derived herefrom; (3) any derivations of this work state that they are derived and differ herefrom; and (4) you include the full text of this license in any copies, translations or derivations of this work. Otherwise, all rights reserved.

The EPUB metadata (`dc:rights`): "Copyright 1998 Thanissaro Bhikkhu, Revised edition 2011. For free distribution, otherwise all rights reserved."

So this 2011 edition is **not** the CC BY-NC 4.0 text the shortlist describes. That licence is on the later revision (PDF dated 2017 on dhammatalks.org). The 2011 terms allow free republication if the site is free of charge, says the edition is derived and differs, and carries the full licence text. The draft keeps the copyright page, licence included, under "Copyright". The verses quoted in the shortlist from the 2017 PDF (1, 2, 5, 183) read the same here, apart from a spaced em dash in verse 1 where the PDF has an en dash. The two revisions were not compared in full.

## How it was converted

1. Unpacked in a scratch folder and converted with Pandoc 3.10.1: `pandoc <epub> -t gfm --wrap=none -o source.md`. That is `source.md`, unedited. The EPUB is clean (hand-made in Sigil), so `books-for-bots` was not needed.
2. The draft (`edition-draft.md`) was built by script from the EPUB's XHTML, not from `source.md`, because Pandoc drops the verse indentation classes. Script: `library/tools/epub-editions/dhp_build.py` (shared helpers in `common.py`, `dhp_parse.py`).
3. Checked by script (`check_ids.py`, `compare.py`, `scan.py`, `joined2.py` in the same folder). Results below.

## Structure found

- **Front matter:** title page; copyright and licence (with "Additional Resources", "Printed Copy", "Questions"); Abbreviations (a table); Preface (December 1997); Introduction.
- **The text:** 26 chapters (vaggas), headed "I : Pairs" to "XXVI : Brahmans". Each verse is its own `div class="verse"`, its lines one paragraph each, with indentation as classes `v1`–`v8` (steps of a quarter inch) and one `v-1` (an outdented list line in 137–140). After each group of verses that belong together the book prints the verse numbers as a cite line ("1-2", "3-6", "183-185"): 267 groups. Numbering runs 1–423 through the whole book.
- **Back matter:** "Historical Notes: The Text & the Translation" (comes after the verses in the EPUB, before the End Notes); End Notes; Glossary; Bibliography; Colophon (about the EPUB's typeface).
- **End notes:** 101 notes keyed by the verse or range they discuss ("1-2", "22", "153-154"), linked from the cite line of their group. Some notes have several paragraphs; three quote verse from other texts (143, 170, 385), as nested stanzas. Cross-references inside notes ("see note 22") are links in the EPUB.

## How the draft is laid out

- Frontmatter: title, author, translator, date, tradition, source, licence, status: draft.
- `## I : Pairs` and so on: the chapter headings as printed.
- `<a id="N"></a>` before each verse, N = 1–423. Each verse's lines are kept as lines (hard breaks), and indentation is kept as `&emsp;` per step (`v2` = two). The group's printed numbers follow it as `<p class="cite">1-2</p>`.
- **Ten groups print as fewer stanzas than verses**, so the verse boundary inside them is not marked in the EPUB. There every verse number gets its own target, all at the start of the group: 58-59, 188-192, 195-196, 229-230, 244-245, 256-257, 271-272, 360-361 (one stanza each), 137-140 (three stanzas: an opening, a list, a close) and 246-248 (two stanzas). A finer split could be made from the Pāli (for 58-59 the break falls at "so in the midst"), but that is an editorial choice, not the source.
- End notes are Markdown footnotes, labelled by their verse key (`[^1-2]`), placed at the end of the last line of the last verse they cover (for the merged groups, at the end of the group). All 101 placed.
- After the verses, under their own headings: Preface, Introduction, Historical Notes, Abbreviations, Glossary, Bibliography, Copyright. Left out: the title page (it is in the frontmatter) and the Colophon (only about the EPUB's font). Footnote definitions come last.

## Fixes and doubts

Words are as in the EPUB. Nothing was reworded. Differences from it, all typographic:

- Runs of spaces and non-breaking spaces are collapsed to one space. In verse 3 the EPUB has seven non-breaking spaces in "‘He       insulted me" (probably a layout gap); the draft has "‘He insulted me".
- Square brackets in the Introduction's verse references ("\[354\]") are escaped so Markdown leaves them alone.
- Links are dropped and their text kept: the note cross-references ("see note 22"), and dhammatalks.org and accesstoinsight.org on the copyright page.
- Verse indentation is shown with `&emsp;` entities. A page template may want to turn these into CSS classes.

Doubtful, left as in the source:

- Verse 4 lacks the opening quotation mark that verse 3 has ("He insulted me, … robbed me’—"). Probably a slip in the book.
- End note 37's link in the EPUB is broken (`../Text/#v-th-seven`); the note is keyed by its label, so the draft is not affected.
- The Preface says "Verses marked with an asterisk in the translation are discussed in the End Notes"; the EPUB uses linked cite lines instead of asterisks.

## Checks (2026-11-20)

- Verse ids: 423 found, 1–423 all present, unique and in order. 26 chapters.
- Footnotes: 101 references, 101 definitions, none missing either way.
- Words, verses only: `source.md` from "I : Pairs" to the start of Historical Notes, against the draft from "I : Pairs" to "Preface", after normalising quotes, dashes, Markdown and HTML: 10,260 words in each, no differences.
- Words, front and back matter: Preface and Introduction, Historical Notes, and Glossary to Bibliography match word for word. In the End Notes the only differences are the 101 note labels (now footnote labels) and the line "(Numbers refer and link to verses)", which is dropped.

## The edition page (`/dhammapada`)

Made 2026-11-20 by an AI agent (Claude) on the newtexts track, from `edition-draft.md` by `build_page.py` (words taken by script) with the hand-written parts in `page-template.md`. The page is now edited by hand: do not rerun `build_page.py` over it without copying the page first.

**Words.** No word, letter or punctuation mark of the translation, the translator's matter or the end notes has been changed. `compare.py` checks this against `edition-draft.md` word by word and fails on any difference. Result on 2026-11-20: verses 9,893 words, translator's matter 9,266, end notes 5,685, licence 90: **0 unlisted differences**. Listed, not compared: the table header of the abbreviations (a label), the editors' note `[^e1]` on the preface, the rename of two headings and the title-case "Historical Notes: The Text & the Translation" (the book's own heading, kept). Footnote markers: 101, in the same order as the draft.

**Layout and labels (every change, none to the words):**

1. Each verse has a passage link, `<a class="v" id="N">`, with ids 1 to 423, each once and in order. The book's cite lines ("1-2", "3-6") are dropped; every verse has its own number.
2. Ten groups the book prints under joint numbers (58-59, 137-140, 188-192, 195-196, 229-230, 244-245, 246-248, 256-257, 271-272, 360-361) show each number at the start of the group, one per line, as the draft already did. The Pāli would allow a finer split between verses; that is an editorial choice and was not made.
3. A blank line inside a verse (137-140, 188-192, and the other groups where the book sets off a list or a second voice) becomes a line holding a non-breaking space, so the verse stays one stanza for `scripts/check`. The gap still shows.
4. Chapters are `###` headings, one per chapter, each with its verses in a `rs-verse` block. Verse indentation is shown with `&emsp;`, as in the draft.
5. The translator's 101 end notes are Markdown footnotes at the last line of the verse or group they discuss, each labelled "*Translator’s note on N.*" with the verse or verses it is about (the label is ours). One editors' note, `[^e1]`, says that the notes sit beside their verses instead of at the back. Cross-references inside notes ("see note 22") are plain text.
6. The translator's preface, introduction, historical notes, abbreviations, glossary and bibliography sit under About this translation. Two headings are renamed to avoid clashing with ours: "Introduction" is "Translator’s introduction", "Preface" is "Translator’s preface". The rest keep the book's headings, one level down.
7. The copyright page is quoted in full under Source and licence (the copyright line and the "For Free Distribution" statement). Its "Additional Resources", "Printed Copy" and "Questions" blocks are not reproduced; they are not licence text. The title page is in the page header; the Colophon (about the EPUB's typeface) is not reproduced.

**Source and licence on the page.** It says the words are unmodified and the layout is ours, and quotes the licence statement in full. The page says the edition is derived from the 2011 text and differs from it in layout, labels and the editors’ words, as the licence asks of derivations.

## The 2017 revision (not used)

Fetched 2026-11-20 by a side-task worker, saved in `2017/` (`SOURCE.md`, the PDF, `verses.txt`, `COMPARE.md`). Its copyright line reads "Copyright 2014 Ṭhānissaro Bhikkhu, Revised edition 2017", licensed CC BY-NC 4.0. Compared with the 2011 verses: 413 of 423 identical after normalising; 10 verses differ in words (19 tokens in all; the largest is 4 tokens, in verses 90 and 203); 8 differ only in punctuation. Chapters and numbering are the same. Both the 2011 title page and the 2017 title page give the translator's legal name in brackets, "(Geoffrey DeGraff)"; the About section of the page gives it too.

Decision: the 2011 text stays, as supplied and as the coordinator decided. Switching would change ten verses and the licence (to non-commercial). Recommendation is on the bead.

## Checks (2026-11-20)

- `scripts/check`: dhammapada.md passes. (Failures elsewhere on main are other tracks' files.)
- `scripts/epub dhammapada` writes `downloads/dhammapada.epub`. Known problem: the page has one verse block per chapter (26), which the builder does not expect. It closes them implicitly with warnings, so the verses and About this translation end up in one EPUB file. The text reads correctly; the structure is untidy. Filed for the site track (see bead).
