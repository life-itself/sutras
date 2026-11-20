# Meditations source: Gregory Hays

The chosen translation (Rufus, 2026-11-20): Rufus's own notes quote Hays (see `rufus-notes-match.md`).

## The file

- **Book:** Marcus Aurelius, *Meditations: A New Translation, with an Introduction, by Gregory Hays*. Publisher: The Modern Library, New York (a division of Random House). "2002 Modern Library Edition"; e-ISBN 1-58836-173-X; ebook "v1.0". The upload's file name says 1984; the book itself says 2002.
- **EPUB:** a Calibre 2.3.0 conversion (2015-06-30) of the Kindle edition (ASIN B000FC1JAI), itself made "using ReaderWorks Publisher Preview, produced by OverDrive, Inc." (the book's last page). Metadata date 2002-05-13.
- **Supplied by:** Rufus, 2026-11-20. Kept here as `hays-meditations-2002.epub` (SHA-256 `401cde5e34b5d2cc2c0904a0c7f4d48e0526244755ef690a822993c164379859`). EPUBs are git-ignored (`library/**/*.epub`), so the file stays on this machine only.

## Copyright, as stated in the book

The copyright page, in full apart from the catalogue data:

> 2002 Modern Library Edition
>
> Introduction and notes copyright © 2002 by Gregory Hays
>
> All rights reserved under International and Pan-American Copyright Conventions. Published in the United States by Modern Library, a division of Random House, Inc., New York, and simultaneously in Canada by Random House of Canada Limited, Toronto.

There is no licence and no separate line for the translation itself; "All rights reserved" covers the book. Status: in copyright (Hays, Modern Library / Random House). Per decision 0001.5 it can be published with that status stated; the draft's frontmatter says so.

## How it was converted

1. Unpacked in a scratch folder and converted with Pandoc 3.10.1: `pandoc <epub> -t gfm --wrap=none -o source.md`. That is `source.md`, unedited. Pandoc's output is noisy (Calibre's `div`/`span` wrappers survive, and small capitals come out split, e.g. "B ook 2", "Z EUS"), but the words are all there.
2. The draft (`edition-draft.md`) was built by script from the EPUB's HTML, not from `source.md`: `library/tools/epub-editions/med_build.py` (helpers in `common.py`, `med_parse.py`). `books-for-bots` was not needed.
3. Checked by script (`check_ids.py`, `compare.py`, `scan.py`, `joined2.py`). Results below.

## Structure found

- **Front matter:** cover; title page; contents; a Chronology that is **only an image** (a two-column timeline, 500 B.C. to A.D. 200, of historical and philosophical names; not converted); half title.
- **Introduction by Gregory Hays** (about 15,000 words): "Marcus Aurelius Antoninus" (with an epigraph from Plato), "Philosophical Background" (sub-headed "Stoicism", "Stoicism and the Meditations", "Other Influences"), "The Meditations: Genre, Structure, and Style", "Recurring Themes", "Later Influence", the short poem "On the Book of Marcus", "Further Reading", "Acknowledgments", then "Introduction Notes" 1–13, keyed to superscript numbers in the text.
- **The text:** Books 1–12, each on its own title page ("Book 1 / Debts and Lessons", "Book 2 / On the River Gran, Among the Quadi", "Book 3 / In Carnuntum"; Books 4–12 untitled). Each section starts a paragraph with its number ("3. People try to get away…"). Book 1's sections each start with a heading in small capitals ("1. MY GRANDFATHER VERUS"). Lists are set with a hanging indent, sometimes with bullets ("• that rational beings exist for one another;"); quoted verse is set as separate lines. Lacunae are marked with Hays's obelus `< . . . >`.
- **Hays's split entries:** in 11 places Hays splits a traditional section in two and numbers the second part with "a": 4.49a, 5.28a, 5.36a, 6.36a, 7.17a, 7.31a, 7.51a, 8.22a, 10.11a, 10.12a, 12.11a. His Introduction (note 8) says the numbering goes back to Gataker (1652) and that he has "occasionally split up a single entry into two". The standard numbers are otherwise unchanged.
- **Notes** (back of the book): 134 notes, keyed by book.section and a lemma in italics ("4.3 *to ward off all < . . . >:* The missing word must be something like 'anxiety.'"), plus two book-level notes ("2." and "3.", on the book titles). There are no note markers in the text itself.
- **Back matter:** Index of Persons (names in capitals, each entry ending with the book.sections where the person appears); About the Translator; The Modern Library Editorial Board; Copyright; "About this Title" (the ebook production note).

## How the draft is laid out

- Frontmatter: title, author, translator, date, tradition, source, licence, status: draft.
- `<a id="4"></a>` before each book heading (`## Book 4`; Books 1–3 with their titles, as in the contents).
- `<a id="4.3"></a>` before each section; the printed number stays at the start of the paragraph, escaped as `3\.` so Markdown does not make it a list. Hays's split entries get ids like `4.49a`.
- Lists: one line each, with hard breaks. Quoted verse: a blockquote with hard breaks, or, where the quotation starts inside the section's opening paragraph (7.50, 7.51, 7.51a), further lines of that paragraph.
- Notes are Markdown footnotes labelled by section (`[^4.3]`, a second note on the same section `[^4.3-2]`). Each reference is placed right after the lemma's words in the section (131 of 134). For three lemmas the words could not be matched, so the reference goes at the end of the section's first paragraph: 8.57 ("Its beams get their name . . ."; the text has "Its beams (*aktai*) get their name"), 11.30 ("For you/Are but a slave . . ."; the reference lands at the end of that line anyway) and 11.39 ("Socrates: What do you want?"; the text continues "…, rational minds or irrational ones?"). The book-level notes sit on the Book 2 and Book 3 headings. Introduction notes are `[^i1]`–`[^i13]`, where the superscripts were.
- After the twelve books, under their own headings: Introduction (Hays), Index of Persons, About the Translator, Copyright. Left out: cover, title page, contents, the Chronology image, half title, the Modern Library Editorial Board list and "About this Title". Footnote definitions come last.

## Fixes and doubts

Fixed (conversion or typesetting damage in the EPUB; the words are otherwise exactly as in the book):

- 1.2: "REPUTATIONf)" → "REPUTATION)" (a stray "f").
- 1.15: "MAXIMUSMaximus" → "MAXIMUS" (heading doubled).
- 4.48: "upwithout" → "up without".
- 5.2: "2.To shrug" → "2. To shrug" (missing space after the number).
- 6.47: "thewhole" → "the whole". Rufus's own notes quote this line with the same typo, so his quotes were taken from an ebook of this edition.

Typographic only: small capitals are written as capitals ("ZEUS", "B.C."), whitespace is collapsed, square brackets in the text are escaped (`\[MY BROTHER\]`), and `< . . . >` is written `&lt; . . . &gt;` so that it shows as typed.

Doubtful, left as in the source:

- 11.30: "“. . . For you/Are but a slave and have no claim to *logos.*”" The slash marks a verse line break inside the quotation; it is kept as printed.
- Where a lemma occurs more than once in a section, the footnote goes on the first occurrence. Placement is editorial and can be moved without touching the text.

## Checks (2026-11-20)

- Ids: 511 (12 books, 488 standard sections, 11 split entries), all unique.
- Sections per book, against the standard counts 17, 17, 16, 51, 37, 59, 75, 61, 42, 38, 39, 36: **all twelve match**. The only difference from the standard numbering is the 11 "a" entries above, which are additions, not renumberings.
- Footnotes: 147 references (134 notes + 13 introduction notes), 147 definitions, none missing either way.
- Words, Books 1–12: `source.md` 34,923, draft 34,912, after normalising quotes, dashes, Markdown and HTML. All 17 differences are explained: the book headings (Pandoc splits the small capitals into "B ook 2" and the draft writes "Book 2: On the River Gran, Among the Quadi"; Book 1's title words sit before the first section in the source: 14 fewer words in the draft) and the five fixes above (three of them split a joined word: 3 more words).
- Words, Introduction, Notes and Index: the only differences are small capitals that Pandoc splits ("A LEXANDER") and the note numbers and lemma keys that became footnote labels.
