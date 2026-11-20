# The Diamond Sutra (Red Pine) — how this edition was made

Edition: `/diamond-red-pine.md` (live at https://sutras.lifeitself.org/diamond-red-pine). Made 2026-11-20 by an AI agent (Claude), track `diamond`, bead sutras-m2v.7.6. Sister edition: `/diamond.md` (Thich Nhat Hanh), notes in `sutras-library/diamond/NOTES.md`. The comparison script is shared: `sutras-library/diamond/compare.py`.

## The missing chapters: what was found

Until 2026-11-20 the page had chapters 1, 2 and 32 only (about 590 words), and the shortlist expected the rest to need Rufus's copy of the book. A search found the whole book online:

- **terebess.hu** hosts an ebook PDF of the full book (all 32 chapters of the sutra, then the translator's preface and the chapters again with commentary): https://terebess.hu/zen/mesterek/Diamond-Sutra.pdf. Chosen as the source. Rights unclear: not an authorised edition.
- **Austin Zen Center** has "Diamond Sutra for chanting", "Translated by Red Pine, edited by Kokyo": https://austinzencenter.org/wp-content/uploads/2021/12/Diamond-Sutra-for-chanting.pdf. All 32 chapters, but edited for chanting (e.g. "monks" for "bhikshus", "Arhat" for "Arhan", "enter the stream" for "find the river", "verse" for "gatha", diacritics added). Not used for the text; used as a second witness (below).
- Also seen in search, not fetched: a "Diamond-Sutra-Red-Pine.pdf" at crisrieder.org.

So the edition is now **complete**, not partial.

## Sources

- `terebess-red-pine-diamond-sutra.pdf`: the source, as fetched on 2026-11-20 from the terebess URL above. Its copyright page: "Copyright © 2001 Red Pine … All rights reserved", Counterpoint, eISBN 978-1-582-43953-2. PDF metadata: created 2017, title "The Diamond Sutra", author "Buddha & Red Pine (tr)".
- `source.txt`: `pdftotext -layout` (poppler) of that PDF, unedited. This is what the script reads.

The earlier `diamond-red-pine.md` (chapters 1, 2, 32) named the book only. It agrees with this source except "teaching of the perfection of wisdom" (source: "teaching on"), the verse's capitals and closing quotation marks, and a footnote quoting a "classic translation" of the verse with no source named. The footnote is dropped.

## How it was made

1. `sutras-library/diamond/compare.py diamond-red-pine --emit` reads the sutra out of `source.txt` (from "ONE: Thus have I heard" to the "TRANSLATOR’S PREFACE"). Chapter heads are "ONE:", "TWO:" … "THIRTY-TWO:"; paragraphs are separated by blank lines (or, after a page break, start with an indent); an indented block after a blank line is a verse. It joins wrapped lines and prints edition Markdown. The text was made from that output, not retyped.
2. Each of the 32 chapters has a passage id, its number: `/diamond-red-pine#14`. Red Pine's chapters are the traditional ones, which he credits to Prince Chao-ming (501–531). The numbers match the Thich Nhat Hanh edition (checked by comparing the opening of each chapter).
3. The "ONE:" … labels are dropped (the number is in the margin). Verses (chapters 26 and 32) are set line by line, as in the source. Five footnote markers were added.
4. `python3 sutras-library/diamond/compare.py diamond-red-pine` compares the edition with `source.txt` word for word and fails on any difference not listed here. Result on 2026-11-20: 32 chapters, 0 unlisted differences, 1 listed.

## Every change to the words

- Chapter 30: "‘billionworld universe.’" to "‘billion-world universe.’". The same phrase is hyphenated two lines earlier ("this ‘billion-world universe’") and in chapter 13; the hyphen was lost at a line end in making the ebook. (The Austin Zen Center text has the same slip, which suggests it was made from the same ebook.)
- A space before a closing quotation mark removed in four places: chapter 3 "‘bodhisattva.’", chapter 10 "‘self-existence.’", chapter 14 "‘best of perfections.’" and chapter 23 "‘auspicious dharmas.’”" (source: "bodhisattva. ’" etc.). Typesetting, not words; the script ignores it.
- Line breaks inside paragraphs joined; a line ending in a hyphen joined keeping the hyphen ("Fully-Enlightened", "self-existence", "billion-world": all hyphenated elsewhere in the book).

Left as in the source: "Arhan" (Red Pine's spelling throughout), "1250 bhikshus", American spelling, romanisation without diacritics.

Not the translator's words (ours): the title block, the in brief, the editors' introduction, the five notes, About this translation, Source and licence.

## Second witness: Austin Zen Center chanting text

Compared word for word (diacritics removed) on 2026-11-20. Every difference is one of Kokyo's edits listed above, a chapter number, or a punctuation change in the verse; none points to an error in our source except the shared "billionworld".

## Facts used in the introduction and notes, and where each comes from

- Sanskrit and Chinese titles, Perfection of Wisdom, date of composition uncertain (2nd–5th century), Kumārajīva 401 and the most chanted Chinese version: English Wikipedia, "Diamond Sutra", read 2026-11-20.
- Red Pine is the pen name of Bill Porter, born 1943, American, translates Chinese Taoist and Buddhist texts: English Wikipedia, "Red Pine (author)", read 2026-11-20.
- First read some thirty years before ("Not long after I first read it thirty years ago"); told it was about emptiness; the sutra "originally in verse … its meaning still depended on its poetry"; translated from the Sanskrit editions of Müller (1881) and Conze (1957); compared "the six extant Chinese translations"; "It turns out the sutra isn’t about emptiness…"; "can be read in half an hour": Red Pine's preface (`source.txt`), verbatim where quoted.
- Prince Chao-ming (501–531), eldest son of Emperor Wu of the Liang, divided the text into 32 chapters and titled them: Red Pine's commentary to chapter 1.
- The commentators named in About this translation: Asanga, Vasubandhu and "several dozen monks" from the preface; Hui-neng from the commentaries (e.g. chapters 6 and 31).
- The notes quote Red Pine's commentary verbatim: chapter 2 ("Bhagavan is a general expression…", note on chapter 1), chapter 1 ("mahasattva", "fearless"), chapter 8 (the gatha), chapter 32 (on the gatha of chapter 26; on the cataract and the star; Kumārajīva's six similes instead of nine).

## Copyright

The translation is in copyright (© 2001 Red Pine; Counterpoint). Published in full under decision 0001 point 5, with the status stated on the page.
