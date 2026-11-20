# Shodoka — how this edition was made

Edition: `/shodoka.md` (live at https://sutras.lifeitself.org/shodoka). Made 2026-11-20 by an AI agent (Claude), track `shodoka`, bead sutras-m2v.7.2.

## Sources

- `Daily-Zen-Sutras.html`: the source, as fetched on 2026-11-20 from http://www.ciolek.com/WWWVLPages/ZenPages/Daily-Zen-Sutras.html (anchor `#SHODO`). The Diamond Sangha *Daily Zen Sutras*, "December 1991 version, Translations/revisions by Robert Aitken Roshi", HTML by Daniel Prosser and T. Matthew Ciolek. The page footer: "Copyright (c) 1991 by the Diamond Sangha Zen Buddhist Society. This Web page may be linked to any other Web pages. Contents may not be altered." Only the Shodoka section is used.
- `terebess-sodoka.html`: a second witness, used for checking and for facts. Fetched 2026-11-20 from https://terebess.hu/zen/sodoka.html (Terebess Asia Online). It prints the same translation under "Translated by Robert Aitken and Eido Shimano", with a note by T. Matthew Ciolek (19 November 1993) on its history, Hu Shih's doubts on authorship, and the *Zenshū Shiburoku*. It also has other translations of the poem (Suzuki, Senzaki and McCandless, Hoshin, Luk and others), not used.
- `compare.py`: the word-for-word check (a copy of `scripts/compare-source` adapted to this text; to be folded into a general script, bead sutras-m2v.7.8).

## How it was made

1. The poem was extracted from `Daily-Zen-Sutras.html` by script (`<P>` paragraphs and `<BR>` line breaks as in the HTML), not retyped.
2. Each of the 64 paragraphs became a verse, numbered 1 to 64 with a link target (`/shodoka#18`). The numbers are ours: the source does not number the verses, but calls the poem "a collection of 64 verses", and the 64 paragraphs match that. The Terebess copy has the same division.
3. The earlier page split the text into 33 numbered sections: 1–32 were the first 32 paragraphs, and "33" held paragraphs 33–64. So ids 1–33 keep the start of the same verse; only 33 is now shorter. Nobody depended on the old ids (decision 0001).
4. Typography and the fixes below were applied.
5. `python3 library/shodoka/compare.py` compares the edition with the source word for word and fails on any difference not listed here. Result on 2026-11-20: 64 verses, 343 source lines (344 in the edition, one line split), 0 unlisted differences.
6. The Terebess copy was diffed line by line against the source: the only differences are the two marked "as in the second copy" below.

## Every change to the words

- Verse 16, last line: "the some way" to "the same way". In both copies.
- Verse 36: one source line, "The Dharma-body of all Buddhas has entered my own nature, And my nature becomes one with the Tathagata.", split into two lines at the comma (a lost `<BR>`; the capital "And" shows it). As in the second copy.
- Verse 38, line 2: "What relation have have these" to "What relation have these". In both copies.
- Verse 42, line 3: "vWhich I found" to "Which I found" (stray letter). As in the second copy.
- Typography: "--" (with or without spaces) set as a spaced em dash " — ", keeping any comma before it (", —" in verses 8, 10, 20, 26, 38, 60, as in the source); the backtick in "don`t" (verse 8) and straight quotation marks and apostrophes made curly.

Left as in the source, though possibly slips: verse 62's last line "Wise sages are all like flashes of lightning" has no end punctuation; "Sambogakaya" (usually Sambhogakaya); "Hui Neng" (verse 42) beside "Kwan-Yin"; "Shravaka" (verse 53) beside "Sravaka" (verse 34); "But they cannot accept, what a pity!" (verse 46); "If someone asks, what is your sect" (verse 40, no question mark before the line break); American spelling ("honor", "realize"), as in the source.

Not the translators' words (ours): the headings, the in brief, the editors' introduction, the notes, About this translation, Source and licence.

## Translator: a correction

The earlier page said "Translated by Nyogen Senzaki and revised by Robert Aitken Roshi". No source for that was found. The source names only Aitken; the Terebess note says the translation was "prepared in the 1960s by Mr Robert Aitken and Eido Shimano Sensei for the Diamond Sangha Zen Buddhist Society", reprinted in *Daily Sutras for Chanting and Recitation* (New York Zendo, n.d.), and "In December 1991 the Aitken-Shimano's translation was revised by Robert Aitken Roshi". The page now credits Aitken and Shimano.

The old credit was not baseless, though: Senzaki's own version ("Song of Realization", with Ruth Stout McCandless, *Buddhism and Zen*, 1953, excerpted on the same Terebess page) shares wording with this one, e.g. "the six noble deeds and the ten thousand good actions are already complete within you" and "Ask a robot whether it is happy or not". The page says so in About this translation and in note 1. Whether Aitken and Shimano worked from Senzaki's text is not known.

## Facts used in the editors' introduction, notes and About, and where each comes from

- Yung-chia's dates (665–713), Tiantai training, the one night with Hui-neng ("Yongjia was convinced to stay just one night, during which his enlightenment was acknowledged"), Chinese title 證道歌: English Wikipedia, "Yongjia Xuanjue", read 2026-11-20. The dates are also in the source's own heading.
- "64 verses", "Song of Enlightenment", "T'ang Dynasty": the source's heading.
- Hu Shih's doubts (a Dunhuang manuscript naming the author as Chao-chiao ta-shih; a monk who died in 713 "could not have sung about 'the 28 Patriarchs'", "The myth of the 28 Patriarchs had not been invented until many decades later"): Hu Shih (1960), quoted on `terebess-sodoka.html`. He calls it "the 37th verse" in another numbering; the line is in verse 42 here ("Twenty-eight generations of teachers in India").
- The *Zenshū Shiburoku* (Ten Oxherding Pictures, Faith in Mind, Shodoka, Zazengi) "used in Japan as introductory texts in the education of novice Zen monks": `terebess-sodoka.html`.
- Sheng-yen on *Faith in Mind* and Yung Chia's *Song of Enlightenment* as "the most highly regarded" poems on enlightenment: his introduction, `library/faith-in-mind/hsin3.html`.
- The translation's history: Ciolek's note on `terebess-sodoka.html` (quoted above) and the source's header ("translated from Japanese", "used in Zen centers and communities affiliated within the framework of the Diamond Sangha").
- Aitken's dates (1917–2010) and co-founding the Honolulu Diamond Sangha in 1959: English Wikipedia, "Robert Baker Aitken", read 2026-11-20.
- Note 1, "robot": the Senzaki and McCandless excerpt on `terebess-sodoka.html` ("Ask a robot whether it is happy or not"); "wooden puppet" from the Hoshin translation there ("Can a wooden puppet attain Buddhahood").
- Note 2, Mani-jewel: English Wikipedia, "Mani Jewel" ("The Mani Jewel itself represents each being's Buddha-nature"; "One version is the Cintamani or wish-fulfilling jewel"); Balcom's note 12 on `terebess-sodoka.html` ("A mythical pearl capable of fulfilling wishes"). It recurs in verses 10, 25 and 61.
- Note 3, the three bodies: English Wikipedia, "Trikaya" (which spells Sambhogakaya).
- Note 4, Ts'ao Ch'i: Balcom's note 23 on `terebess-sodoka.html` ("Where Huineng taught; also used to refer to Huineng himself") and Suzuki's note there.
- Note 5, the dragon girl: Balcom's note 44 on `terebess-sodoka.html` ("Reference to the Devadatta Chapter of the Lotus Sutra, where a young dragon girl becomes a Buddha, though Sariputra, one of the Buddha's disciples, claims that women are incapable of attaining Buddhahood").
- Note 6, Upali and Vimalakirti: Balcom's note 49 on `terebess-sodoka.html` ("Upali explains their transgressions according to the monastic rules, while Vimalakirti states that their transgressions are as illusory as all phenomena"); "cleared their doubts" is the poem's own phrase.
- Sheng-yen's reason, "because of the clear guidance they provide on the method of Ch'an": his introduction in `library/faith-in-mind/hsin3.html`.
- "Hu Shih, writing in 1960": the citation on `terebess-sodoka.html` (*Bukkyō to bunka*, Kyoto, 1960). Tunhuang and T'ien-t'ai are given in Wade-Giles, as on that page and in *Faith in Mind*.

Not given a note, for want of a source read: "Pradhanashura" (verse 57), "fei-ni grass" (verse 35; probably the Nirvana Sutra's Himalayan grass "patience", unconfirmed), "the burning iron ring" (verse 63). Worth adding when a source is found.

Critique: a fresh subagent reviewed the page on 2026-11-20. Applied: comma splice; Hu Shih's claim attributed to him; "chanted" softened to what the sources say; "boastful" and "thunder" dropped; the Senzaki wording; translator named in the in brief; romanisation made consistent; the "robot" point moved to a note; source-and-licence slips sentence rewritten.

## Copyright

The translation is in copyright (© 1991 Diamond Sangha Zen Buddhist Society, per the source page). The page says "Contents may not be altered"; we have corrected four slips and changed typography, all listed here. Published in full under decision 0001 point 5, with the status stated on the page.
