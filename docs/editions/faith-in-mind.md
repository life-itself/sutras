# Faith in Mind — how this edition was made

Edition: `/faith-in-mind.md` (live at https://sutras.lifeitself.org/faith-in-mind). Made 2026-11-20 by an AI agent (Claude) for milestone 1.

## Sources

- `hsin3.html`: the source, as fetched on 2026-11-20 from https://terebess.hu/english/hsin3.html (Terebess Asia Online). It is the whole of Sheng-yen's book *Faith in Mind: A Guide to Ch'an Practice*: preface, introduction, the poem, and twenty retreat talks. The edition uses the preface, the introduction and the poem; the talks are not published, only quoted in three notes.
- `dharmanet-1994.pdf`: a second witness, used for checking only. The DharmaNet electronic edition (1994) of the same book, "by arrangement with the publisher", fetched 2026-11-20 from https://dlbs.liberal.ntu.edu.tw/FULLTEXT/JR-MISC/misc38333.pdf (National Taiwan University Digital Library of Buddhist Studies). Its front matter gives: Copyright 1987 by Dharma Drum Publications; first printing 1987, second 1993; ISBN 0-9609854-2-5; translator (poem) Master Sheng-Yen, co-translator Paul Kennedy; editor Karen Zinn.

## How it was made

1. The poem, preface and introduction were extracted from `hsin3.html` by script (paragraphs and `<br>` line breaks as in the HTML), not retyped.
2. Each of the 15 paragraphs of the poem on the source page became a stanza, numbered 1 to 15 with a link target (`/faith-in-mind#3`). The numbers are ours: the poem has no traditional stanza numbering, and the DharmaNet edition prints it as one block of 146 lines.
3. Typography and the fixes below were applied.
4. `scripts/compare-source` compares the edition with `hsin3.html` word for word and fails on any difference not listed here. Result on 2026-11-20: 15 stanzas, 146 lines, 0 unlisted differences.

## Every change to the words

The poem:

- No word changed.
- Five line-end dashes restored (as " —"): stanza 1 line 9 ("For and against opposing each other —"), stanza 7 line 9 ("Using mind to cultivate mind —"), stanza 8 lines 5 and 7 ("A dream, an illusion, a flower in the sky —", "Gain and loss, right and wrong —"), stanza 12 line 7 ("This principle is neither hurried nor slow —"). The verses section of the source page has no punctuation there, but the same page prints the dash where it quotes these lines in the talks, and the DharmaNet edition has "--" in all five places.
- Straight apostrophes made curly ("mind's" to "mind’s").

Preface and introduction:

- "he Founded" to "he founded" (preface).
- "Nui Neng" to "Hui Neng" (introduction; the talks on the same page have "Hui-Neng, the Sixth Patriarch").
- "does not discriminates" to "does not discriminate" (introduction).
- "(ping deng hsin is realized" to "(ping deng hsin) is realized" (introduction; missing bracket).
- " - " to " — " in that same sentence; straight quotation marks and apostrophes made curly.
- The earlier version of the page had added "(1931-2009)" after Sheng-yen's name in the preface. Removed: it is not in the source. The dates are now in our own paragraph above the preface.

Left as in the source, though possibly slips: "Kao Seng Chua", "fundamental unmoving" (preface, no comma), "practice" and "practicing" (American spelling, as in the book), romanisation without diacritics ("Soto", "Tathagatagarbha").

Not the translator's words (ours): all headings ("The poem", "Preface to the 1987 book (unsigned)", "Sheng-yen’s introduction"), the in brief, the editors' introduction, the three notes, About this translation's first paragraph, Source and licence.

## Where the DharmaNet edition differs in the poem

Not followed; recorded so nobody "corrects" one from the other. The Terebess text is the named source. DharmaNet reading first, ours second:

- Stanza 1: "And you are as far apart as heaven from earth." / "And you are as far from it as heaven from earth."
- Stanza 1: "If you want it to appear," / "If you want the Way to appear,"
- Stanza 2: "Only stagnating in duality," / "Merely stagnating in duality,"
- Stanza 12: "Only refer to "not-two."" / "Only refer to not-two."
- Stanza 12: "Nothing is not included." / "Nothing is excluded."
- Spelling or typing only: "take care" (lower case), "one wit true enlightenment", "tranquility", "visable".

Which wording is the later revision is not known. Worth checking against a printed copy.

## Facts used in the editors' introduction and notes, and where each comes from

- Seng Ts'an as Third Patriarch, died 606; scholars doubt his authorship, and some place the poem after the Sixth Patriarch; the two poems as "the most highly regarded"; Sheng-yen lectured on the poem only during seven-day retreats; the pairing with Yung Chia's *Song of Enlightenment*; the later importance of "One thought for ten thousand years" in the Ts'ao-tung school: Sheng-yen's introduction (`hsin3.html`).
- The three quotations from Sheng-yen in the notes: his talks in `hsin3.html` (chapters 1, 16 and 20), verbatim; note 1 leaves out a passage, marked […].
- Chinese title 信心銘, *Hsin Hsin Ming*: English Wikipedia, "Xinxin Ming", read 2026-11-20. (It also says the poem was "written well after Sengcan's death, probably during the Tang dynasty (618–907)"; not used on the page, which keeps to what Sheng-yen reports.)
- Sheng-yen's dates (1931–2009): English Wikipedia, "Sheng-yen", read 2026-11-20.
- Publisher, year, co-translator: front matter of `dharmanet-1994.pdf`.
- "146 lines", "fifteen stanzas": counted by `scripts/compare-source`.

## Copyright

The translation, preface and introduction are in copyright (© 1987 Dharma Drum Publications). Published in full under decision 0001 point 5, with the status stated on the page. The DharmaNet edition's own notice allows a single printed copy for personal use, "otherwise, all rights reserved".
