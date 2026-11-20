# The Diamond Sutra (Thich Nhat Hanh) — how this edition was made

Edition: `/diamond.md` (live at https://sutras.lifeitself.org/diamond). Made 2026-11-20 by an AI agent (Claude), track `diamond`, bead sutras-m2v.7.3. Sister edition: `/diamond-red-pine.md`, notes in `sutras-library/diamond-red-pine/NOTES.md`.

## Sources

- `terebess-diamond-that-cuts-through-illusion.pdf`: the source, as fetched on 2026-11-20 from https://terebess.hu/zen/mesterek/Thich%20Nhat%20Hanh%20-%20The%20Diamond%20That%20Cuts%20Through%20I.pdf (Terebess Asia Online). A calibre conversion (2013) of the ebook of Thich Nhat Hanh, *The Diamond That Cuts through Illusion* (Parallax Press, 2010 edition; eISBN 978-1-937-00601-3; catalogue data also names Annabel Laity and Anh Huong Nguyen). It holds the whole book: a short "Welcome", the sutra in 32 numbered sections, then the commentaries.
- `source.txt`: `pdftotext -layout` (poppler) of that PDF, unedited. This is what the script reads.
- `plumvillage-2026-11-20.html`: the Plum Village web page https://plumvillage.org/library/sutras/the-diamond-that-cuts-through-illusion as fetched on 2026-11-20. It is a **shortened** version (about 1,500 words) and is what this page carried until 2026-11-20. Kept for reference only; not used for the text. It also has small revisions of wording (e.g. "went into the town of Shravasti to beg for alms" where the book has "went into the city of Shravasti to seek alms food").

The earlier `diamond.md` was a copy of an older state of that Plum Village page (it named `plumvillage.org/sutra/the-diamond-that-cuts-through-illusion/` and an unchecked "alternative translation" at buddhasutra.com). Both are dropped: the book is the better source and the full text.

## How it was made

1. `sutras-library/diamond/compare.py diamond --emit` reads the sutra out of `source.txt` (between the second "THE VAJRACCHEDIKA PRAJÑAPARAM ITA" heading and the second "COMMENTARIES"), by the PDF layout: a centred number starts a section, an indented line starts a paragraph, an indented block after a blank line is a verse. It joins wrapped lines and prints the text as edition Markdown. The text was made from that output, not retyped.
2. Each of the 32 sections has a passage id, its number: `/diamond#14`. The numbers are the book's, and follow the traditional 32-chapter division of the Chinese text (credited by Red Pine to Prince Chao-ming, 501–531). They are the same as in the Red Pine edition, so `#n` is the same passage in both.
3. Verses (section 26, section 32) are set line by line, as in the source. Five footnote markers were added.
4. `python3 sutras-library/diamond/compare.py diamond` compares the edition with `source.txt` word for word and fails on any difference not listed here. Result on 2026-11-20: 32 sections, 126 paragraphs and verses, 0 differences.

## Every change to the words

- No word changed.
- Conversion faults put right while reading the source (in `repair()` of the script): the converter splits a capital M from the rest of its word ("M oreover", "M ount Sumeru"); joined.
- Line breaks inside paragraphs joined. A line ending in a hyphen was joined keeping the hyphen (the PDF is a reflowed ebook, so these are the book's own): "World-Honored" (twice), "No-Return", "thirty-two", "non-life". No other line ends in a hyphen inside the sutra.
- Page breaks inside paragraphs joined (e.g. section 2, "we are so happy / to hear your teachings").

Left as in the source: American spelling ("realize", "practicing"), romanisation without diacritics ("Tathagata", "Shravasti"), "ashuras" (section 32).

Not the translator's words (ours): the title block, the in brief, the editors' introduction, the five notes, About this translation, Source and licence.

## Facts used in the introduction and notes, and where each comes from

- Sanskrit title *Vajracchedikā Prajñāpāramitā*; Chinese 金剛經; one of the Perfection of Wisdom (Prajñāpāramitā) sutras; date of composition uncertain, "arguments for the 2nd and 5th centuries have been made"; Kumārajīva's Chinese translation of 401, "the most widely used and chanted Chinese version"; prominent in Chan/Zen; the Dunhuang printed copy dated 11 May 868, "the earliest example which bears an actual date" of block printing: English Wikipedia, "Diamond Sutra", read 2026-11-20. ("The oldest dated printed book we have" is our short form of "broadly considered to be the oldest extant printed book" and "earliest example which bears an actual date".)
- Thich Nhat Hanh, 1926–2022, Vietnamese Thiền (Zen) monk, founded the Plum Village tradition: English Wikipedia, "Thich Nhat Hanh", read 2026-11-20.
- Translated from the Sanskrit and the Chinese Taishō No. 235: the Plum Village page (`plumvillage-2026-11-20.html`): "Translated by Thich Nhat Hanh from the Vajracchedikā Prajñāpāramitā Sūtra (in Sanskrit), and the Chinese Taishō Revised Tripitaka, No. 235."
- "Don’t rush into the commentaries…": the book's "Welcome" (`source.txt`), verbatim.
- "a raft", "that is why it is called": the sutra itself (sections 6, 8 and throughout).
- About 6,000 words: counted (the sutra section is 5,880 words).
- Prince Chao-ming and the 32 chapters: Red Pine's commentary to chapter 1 (`sutras-library/diamond-red-pine/source.txt`).
- The notes quote Thich Nhat Hanh's commentaries in `source.txt` verbatim: on section 5 (Tathagata), section 6 (raft, Alaggadupama Sutta), section 8 (chiliocosm), section 26 (Cakravartin). Note 5 cites Red Pine's text of section 32.

## Copyright

The translation is in copyright (Parallax Press, the publishing division of the Unified Buddhist Church; "All Rights Reserved"). Published in full under decision 0001 point 5, with the status stated on the page. The terebess copy is not an authorised edition.

## Open

- Plum Village's own web text is a revised, shortened version. If the full text is ever wanted in its latest wording, it needs the current Parallax edition.
