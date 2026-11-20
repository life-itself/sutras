# Library shortlist

Status: draft for Rufus, 2026-11-20. Library workstream ([brief](plans/workstreams/1-library.md)), bead sutras-m2v.4. Facts were checked on the source pages on 2026-11-20 unless marked **unverified**. Project Gutenberg was down for maintenance that day, and sacred-texts.com blocks scripts, so neither could be checked directly.

## In brief

- **Dhammapada:** build on Bhikkhu Sujato's translation (CC0, SuttaCentral). It wins on openness and data: it is public domain and comes with the Pāli aligned line by line. It does not win on reading, where Fronsdal and Munindo are better. Compare them in the side-by-side table in section 1 and choose by ear. Backup: Thanissaro Bhikkhu (CC BY-NC 4.0). Sujato's text is saved in `library/dhammapada/`.
- **Nothing found locally:** no Dhammapada file, and no Zotero library on this Mac. The "good open-source translation" Rufus remembers is most likely Sujato's (guess).
- **Existing texts:** three problems need fixing. Seneca is missing its chapter XVII heading, and its source link now goes to a hijacked domain. The Plum Village *Diamond Sutra* is a short version of about 1,500 words, not the full sutra. Red Pine has only chapters 1, 2 and 32 of 32.
- **Do first:** Dhammapada, Heart Sutra (Thich Nhat Hanh, CC BY-NC), Tao Te Ching, *Meditations*.
- **Rufus's notes:** the big one is `rufuspollock.com/Meditations.md`. It holds about 7,400 words of quotes from the Hays translation, each with a heading and a comment.

## 1. The Dhammapada

423 short verses in 26 chapters, from the Pāli Canon (Khuddaka Nikāya). It is the best-loved early Buddhist text and the obvious first new text. Every translation numbers the verses 1–423 straight through the book, so a link like `/dhammapada#183` works whichever one we choose. The chapters (vaggas) are numbered 1–26.

### What is on this machine

- No Dhammapada file. `mdfind -name dhammapada` finds nothing. `mdfind dhammapada` finds only passing mentions: the title in `~/src/life-itself/next.lifeitself.org/blog/wise-booklist.md` (line 43, no translator named), a footnote in `~/src/life-itself/library/books/thich-nhat-hanh/art-of-power/markdown/art-of-power.md`, and our own decision 0001.
- No Zotero library. Neither `~/Zotero` nor `~/Library/Application Support/Zotero` exists. `~/src/datasets/library/docs/zotero-source-inventory.json` (checked 2026-10-24) names the database as `/Users/rgrp/Zotero/zotero.sqlite`, but lists only 19 design and data-visualisation books and no Dhammapada. If the Zotero library lives on another machine or in Zotero's cloud, it was not reachable from here. No Zotero API key is in the secrets file.
- Spotlight finds nothing for the translator names Buddharakkhita, Munindo or Sujato.

### Candidates compared

The same verses in each translation: 1–2 (the opening pair), 5 (on hatred) and 183 (the summary of the teaching). The verses are quoted from the pages named; " / " marks a line break.

**Bhikkhu Sujato (SuttaCentral, 2018 onwards)**

- Licence: CC0, public domain. The SuttaCentral data repository's `LICENSE.md` says "All translations created in Bilara and supported by SuttaCentral are dedicated to the Public Domain by means of the Creative Commons Public Domain (CC0) license" (https://github.com/suttacentral/bilara-data/blob/published/LICENSE.md). The page https://suttacentral.net/licensing could not be read by script.
- Verses 1–2: "Intention is the leader of things; / intention is first, they're made by intention. / If with corrupt intent / you speak or act, / suffering follows you, / like a wheel, the ox's foot." and "Intention is the leader of things; / intention is first, they're made by intention. / If with pure intent / you speak or act, / happiness follows you / like a shadow that never leaves."
- Verse 5: "For never is hatred / laid to rest by hate, / it's laid to rest by love: / this is an ancient teaching."
- Verse 183: "Not to do any evil; / to embrace the good; / to purify one's mind: / this is the instruction of the Buddhas."
- Readability: plain, modern and short-lined. "Intention" for *mano* (usually "mind") is a deliberate choice, explained in his note on verse 1. Some readers will miss the familiar "mind" opening.
- Clean text: JSON keyed by line (`dhp1:1`), with the Pāli root, notes and an HTML template sharing the same keys. API: `https://suttacentral.net/api/bilarasuttas/dhp1-20/sujato?lang=en`. Raw files: `github.com/suttacentral/bilara-data`, under `translation/en/sujato/sutta/kn/dhp/`.
- Numbering: verse and line (`dhp183:1`). The files are grouped by chapter (`dhp1-20`, `dhp21-32` and so on).

**Thanissaro Bhikkhu (dhammatalks.org; 1997, revised 2014 and 2017)**

- Licence: CC BY-NC. The current PDF (https://www.dhammatalks.org/Archive/Writings/Ebooks/Dhammapada_251113.pdf) says: "Copyright 2014 Ṭhānissaro Bhikkhu, Revised edition 2017. This work is licensed under the Creative Commons Attribution-NonCommercial 4.0 Unported [sic; 4.0 is 'International']… 'Commercial' shall mean any sale, whether for commercial or non-profit purposes or entities." The web chapter pages carry no licence statement. The older 1997 version on Access to Insight is under the older terms: free distribution only, other rights reserved.
- Verses 1–2: "Phenomena are / preceded by the heart, / ruled by the heart, / made of the heart. / If you speak or act / with a corrupted heart, / then suffering follows you – / as the wheel of the cart, / the track of the ox / that pulls it." and "…If you speak or act / with a calm, bright heart, / then happiness follows you, / like a shadow / that never leaves."
- Verse 5: "Hostilities aren't stilled / through hostility, / regardless. / Hostilities are stilled / through non-hostility: / this, an unending truth."
- Verse 183: "The non-doing / of any evil, / the performance / of what's skillful, / the cleansing / of one's own mind: / this is the teaching / of the Awakened."
- Readability: careful and exact, with good notes, but fragmented and sometimes odd ("regardless", "non-hostility").
- Clean text: HTML per chapter (https://www.dhammatalks.org/suttas/KN/Dhp/Ch01.html), plus PDF and EPUB.
- Numbering: the web page prints the number after each verse or group of verses ("1-2", "183-185"), so it needs care when parsing.

**Ajahn Munindo, *A Dhammapada for Contemplation* (Aruno Publications, 5th edition 2017)**

- Licence: CC BY-NC-ND. The PDF (https://cdn.amaravati.org/wp-content/uploads/2022/04/26/dhammapada-for-contemplation-5th-LARGE-WEB-2017-02-05.pdf) says: "Copyright © Aruno Publications 2016… This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License." "NoDerivs" means we may republish it unchanged, but not edit or adapt it.
- Verses 1–2: "All states of being are determined by the heart. / It is the heart that leads the way. / Just as the wheel of the oxcart follows / the hoof print of the animal that draws it, / so suffering will surely follow / when we speak or act impulsively / from an impure heart." and "…As surely as our shadow never leaves us, / so well-being will follow / when we speak or act / with a pure heart."
- Verse 183: "Refrain from doing evil, / cultivate that which is good, / purify the heart. / This is the Way of the Awakened Ones."
- Readability: the warmest and most contemplative of the open ones. It is a rendering for reflection rather than a close translation (Munindo says so himself).
- Clean text: PDF and EPUB (abhayagiri.org, amaravati.org). It would need converting.
- Numbering: verses 1–423.

**Acharya Buddharakkhita (Buddhist Publication Society, 1985)**

- Licence: free distribution with conditions. The Access to Insight page (https://www.accesstoinsight.org/tipitaka/kn/dhp/dhp.01.budd.html) says: "©1985 Buddhist Publication Society. You may copy, reformat, reprint, republish, and redistribute this work in any medium whatsoever, provided that: (1) you only make such copies, etc. available free of charge and, in the case of reprinting, only in quantities of no more than 50 copies; (2) you clearly indicate that any derivatives of this work (including translations) are derived from this source document; and (3) you include the full text of this license in any copies or derivatives of this work. Otherwise, all rights reserved."
- Verses 1–2: "Mind precedes all mental states. Mind is their chief; they are all mind-wrought. If with an impure mind a person speaks or acts suffering follows him like the wheel that follows the foot of the ox." and "…If with a pure mind a person speaks or acts happiness follows him like his never-departing shadow."
- Verse 5: "Hatred is never appeased by hatred in this world. By non-hatred alone is hatred appeased. This is a law eternal."
- Verse 183: "To avoid all evil, to cultivate good, and to cleanse one's mind — this is the teaching of the Buddhas."
- Readability: clear, classic and quotable, but set as prose, a little dated, and with "he" throughout.
- Clean text: Access to Insight HTML, one page per chapter.
- Numbering: verses 1–423, numbered inline.

**F. Max Müller (Sacred Books of the East, vol. 10, 1881)**

- Licence: public domain (translator died 1900). Wikisource: https://en.wikisource.org/wiki/Dhammapada_(Muller). The Gutenberg ebook #2017 was not reachable today.
- Verses 1–2: "All that we are is the result of what we have thought: it is founded on our thoughts, it is made up of our thoughts. If a man speaks or acts with an evil thought, pain follows him, as the wheel follows the foot of the ox that draws the carriage." and "…If a man speaks or acts with a pure thought, happiness follows him, like a shadow that never leaves him."
- Verse 5: "For hatred does not cease by hatred at any time: hatred ceases by love, this is an old rule."
- Verse 183: "Not to commit any sin, to do good, and to purify one's mind, that is the teaching of (all) the Awakened."
- Readability: Victorian prose, but the famous version. "All that we are is the result of what we have thought" is a free, idealist reading of the Pāli.
- Clean text: Wikisource wikitext with a `{{verse|chapter=I|verse=1}}` marker on every verse, so it is easy to parse.

**Gil Fronsdal (Shambhala, 2005)**

- Licence: in copyright, all rights reserved. Not online in full.
- Verse 1, as excerpted by Lion's Roar (https://www.lionsroar.com/in-translation-the-inexhaustable-dhammapada): "All experience is preceded by mind, / Led by mind, / Made by mind. / Speak or act with a corrupted mind, / And suffering follows / As the wagon wheel follows the hoof of the ox."
- Verse 5, from the same page: "Hatred never ends through hatred. / By non-hate alone does it end. / This is an ancient truth."
- Readability: perhaps the best balance of accuracy and grace. It would need the book itself, as an EPUB converted with `books-for-bots`.

**Others, not checked in depth.** Ānandajoti Bhikkhu has a Pāli–English line-by-line version (https://www.ancient-buddhist-texts.net/Texts-and-Translations/Dhammapada/index.htm, 2nd edition 2017, PDF and EPUB; licence **unverified**). Narada Thera (BPS) is free distribution (**unverified**). Eknath Easwaran (Nilgiri Press) and Valerie Roebuck (Penguin) are in copyright.

### Side by side

| | Verse 1 (opening) | Verse 5 | Verse 183 |
|---|---|---|---|
| Sujato (CC0) | Intention is the leader of things; intention is first, they're made by intention. If with corrupt intent you speak or act, suffering follows you, like a wheel, the ox's foot. | For never is hatred laid to rest by hate, it's laid to rest by love: this is an ancient teaching. | Not to do any evil; to embrace the good; to purify one's mind: this is the instruction of the Buddhas. |
| Thanissaro (CC BY-NC) | Phenomena are preceded by the heart, ruled by the heart, made of the heart. If you speak or act with a corrupted heart, then suffering follows you – as the wheel of the cart, the track of the ox that pulls it. | Hostilities aren't stilled through hostility, regardless. Hostilities are stilled through non-hostility: this, an unending truth. | The non-doing of any evil, the performance of what's skillful, the cleansing of one's own mind: this is the teaching of the Awakened. |
| Munindo (CC BY-NC-ND) | All states of being are determined by the heart. It is the heart that leads the way. Just as the wheel of the oxcart follows the hoof print of the animal that draws it, so suffering will surely follow when we speak or act impulsively from an impure heart. | (not extracted) | Refrain from doing evil, cultivate that which is good, purify the heart. This is the Way of the Awakened Ones. |
| Buddharakkhita (BPS, free distribution) | Mind precedes all mental states. Mind is their chief; they are all mind-wrought. If with an impure mind a person speaks or acts suffering follows him like the wheel that follows the foot of the ox. | Hatred is never appeased by hatred in this world. By non-hatred alone is hatred appeased. This is a law eternal. | To avoid all evil, to cultivate good, and to cleanse one's mind — this is the teaching of the Buddhas. |
| Müller (public domain) | All that we are is the result of what we have thought: it is founded on our thoughts, it is made up of our thoughts. If a man speaks or acts with an evil thought, pain follows him, as the wheel follows the foot of the ox that draws the carriage. | For hatred does not cease by hatred at any time: hatred ceases by love, this is an old rule. | Not to commit any sin, to do good, and to purify one's mind, that is the teaching of (all) the Awakened. |
| Fronsdal (in copyright) | All experience is preceded by mind, Led by mind, Made by mind. Speak or act with a corrupted mind, And suffering follows As the wagon wheel follows the hoof of the ox. | Hatred never ends through hatred. By non-hate alone does it end. This is an ancient truth. | (not available online) |

### Recommendation

**Build on Bhikkhu Sujato.** To be plain, this is a choice on openness and data, not on reading. Fronsdal reads best, Munindo is the most contemplative, and Sujato is plain and sometimes cramped ("like a wheel, the ox's foot"). The reasons:

1. It is the only modern translation we checked that is fully open (CC0; Ānandajoti's licence was not checked). That matches "a good translation that is open source" and the open-literature aim.
2. It comes as structured data, not a page to scrape. Every line has a stable ID, so passage links and Rufus's notes can attach to exact verses.
3. The Pāli is aligned line by line, which makes a later "show the original" view nearly free.
4. It is complete: all 423 verses, about 10,200 words. It is fetched and saved in `library/dhammapada/` (see `NOTES.md` there).

The weak point is its wording ("Intention is the leader of things"), which is less familiar than "mind". **Backup: Thanissaro Bhikkhu.** It is CC BY-NC 4.0, so a non-commercial site may adapt it. The NC licence would carry over to anything built from it, including the EPUB, and the text is fiddlier to parse. Munindo is the most beautiful to read. Its "NoDerivs" licence still allows republishing it whole and unchanged, and annotations kept in a separate layer are arguably not a change. So if Rufus prefers it by ear, it is a real option, not just a comparison sample. If Rufus prefers the "mind" wording, Buddharakkhita is the plain classic choice, but it comes with the BPS conditions.

## 2. Source records for the six existing texts

| Text (file) | Author, date | Translator | Source named in file | Better source | Translation status | Cited by | Problems |
|---|---|---|---|---|---|---|---|
| *Diamond Sutra* (`diamond.md`) | Anonymous Mahāyāna sutra, c. 2nd–5th century CE. Chinese: Kumārajīva, 401 CE (Taishō 235) | Thich Nhat Hanh | plumvillage.org/sutra/the-diamond-that-cuts-through-illusion/ (now redirects to /library/sutras/…) | https://plumvillage.org/library/sutras/the-diamond-that-cuts-through-illusion. Full text with commentary: *The Diamond That Cuts Through Illusion* (Parallax Press, 1992; revised 2010) | In copyright. The Plum Village page states no licence (its Heart Sutra page does) | 32 sections (Prince Zhaoming's division of the Chinese text). Scholars cite Taishō 235 | The file has about 1,570 words and the Plum Village page about 1,500, so they match. But it is a shortened version. It lacks well-known passages of the full sutra, such as the sands of the Ganges and the closing verse on the world as a dream. The full sutra runs several thousand words; the short one is probably Plum Village's chanting version (guess). It has no section numbers, so `#n` links cannot follow the usual 32 sections without the book. The "alternative translation" link (buddhasutra.com) is not checked. |
| *Diamond Sutra* (`diamond-red-pine.md`) | as above | Red Pine (Bill Porter) | Book title only | *The Diamond Sutra: The Perfection of Wisdom; Text and Commentaries Translated from Sanskrit and Chinese* (Counterpoint, 2001, ISBN 1582430594; paperback 2002, ISBN 1582432562), 32 chapters each followed by commentary | In copyright (Counterpoint). No authorised free text online. terebess.hu hosts a PDF that looks like a scan of the book (rights unclear, not opened) | 32 chapters (Red Pine follows Zhaoming's division) | **Partial:** chapters 1, 2 and 32 only (about 590 words). Completing it needs the book itself (EPUB or scan converted with `books-for-bots`). Per decision 0001 it stays, marked partial. |
| *Faith in Mind* (Xinxin Ming) (`faith-in-mind.md`) | Attributed to Jianzhi Sengcan, Third Patriarch of Chan (died 606) | Master Sheng-yen (1931–2009) | https://terebess.hu/english/hsin3.html (live, checked) | The book: Sheng-yen, *Faith in Mind: A Guide to Ch'an Practice* (Dharma Drum, 1987). terebess.hu also gathers many other English versions on its Sengcan page | In copyright (Dharma Drum). No licence stated on terebess | 146 four-character lines (73 couplets), cited by line. The spike numbers stanzas instead (`#3`) | The preface is the publisher's blurb and is out of date ("He now divides his time…"; Sheng-yen died in 2009). The verse is unnumbered. |
| *The Gateless Gate* (Wumenguan, Mumonkan) (`gateless-gate-mumonkan.md`) | Wumen Huikai, 1228 | Katsuki Sekida | https://www.sacred-texts.com/bud/zen/mumonkan.htm (confirmed through archive.org: Sekida, with Chinese from an Iwanami Bunko edition) | Sekida, *Two Zen Classics* (Weatherhill, 1977; Shambhala, 2005). Open alternative: Senzaki and Reps (1934), probably public domain in the US if not renewed (**unverified**) | In copyright | 48 cases plus a preface ("Case 1", Mu) | The file names sacred-texts, but the colophon names Sekida; record both. A few Chinese characters are boxes. |
| *Shodoka* (Zhengdaoge) (`shodoka.md`) | Attributed to Yongjia Xuanjue (665–713) | Nyogen Senzaki, revised by Robert Aitken (the file says so); the source says "translations/revisions by Robert Aitken Roshi", December 1991 | http://www.ciolek.com/WWWVLPages/ZenPages/Daily-Zen-Sutras.html#SHODO (live, checked: Diamond Sangha *Daily Zen Sutras*) | The same source is the best: the Diamond Sangha's own sutra book | Copyright Diamond Sangha (**unverified**: no licence on the page) | The source gives the verses unnumbered. The file's 33 sections are our own division. The source's note says "a collection of 64 verses" | The file's numbering (1–33) matches neither the source nor the 64-verse count. Decide once whether to keep it. |
| *On the Shortness of Life* (`seneca-on-the-shortness-of-life.md`) | Seneca the Younger, c. 49 CE | John W. Basore (Loeb, 1932) | forumromanum.org (**now dead**: it redirects to an unrelated site, survey-matt.com) | Wikisource: https://en.wikisource.org/wiki/On_the_shortness_of_life (Basore). Open alternative: Aubrey Stewart in Standard Ebooks' *Dialogues*, CC0 (https://standardebooks.org/ebooks/seneca/dialogues/aubrey-stewart) | Public domain in the US. Wikisource tags it `PD-US-no-renewal` (published 1932, copyright not renewed). UK status depends on Basore's death date (**unverified**) | 20 chapters (I–XX), then sections (e.g. 1.3) | **The chapter XVII heading is missing.** It appears as running text ("XVII. The very pleasures…") inside XVI, so `#17` would break. Replace the dead source link. |

## 3. Shortlist: 20 candidates

Ordered by a suggested sequence. "Best" is the best-reading translation; "open" is the best open one where it differs. Lengths are approximate. Licence statements marked ✓ were read on the source page; the others are by date or are **unverified**. "Standard Ebooks, PD-US" means the translation is public domain in the US (Standard Ebooks says "thought to be free of copyright restrictions in the United States"; it may not be elsewhere), and Standard Ebooks' own work on it is CC0.

| # | Text | Why it is here | Recommended translation and licence | Source | Length | Cited by |
|---|---|---|---|---|---|---|
| 1 | **Dhammapada** | The best-loved early Buddhist text; short verses that suit annotation | Sujato, CC0 ✓ (see section 1) | `library/dhammapada/` | 10,000 words | verse 1–423 |
| 2 | **Heart Sutra** | The core of Mahāyāna wisdom in one page; a companion to the Diamond Sutra | Thich Nhat Hanh, 2014, CC BY-NC 4.0 ✓ ("Translation is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License"). It deliberately departs from the standard wording (e.g. "the Insight that Brings Us to the Other Shore"), so its lines will not map onto other versions. The traditional alternative is Aitken's chant, in the Diamond Sangha *Daily Zen Sutras* (the same source as Shodoka) | https://plumvillage.org/library/sutras/the-heart-sutra | 300 words | by title (Taishō 251); line |
| 3 | **Tao Te Ching** | The Taoist classic; the vision names it; the natural text for a "compare translations" view | Best: Ursula K. Le Guin (Shambhala, 1997, in copyright). Open: James Legge (1891), Standard Ebooks, PD-US ✓ (dated). J. H. McDonald (1996) reads better and is labelled "A Translation for the PUBLIC DOMAIN", but only on third-party copies (**unverified**) | https://standardebooks.org/ebooks/laozi/tao-te-ching/james-legge | 5,000 words (text only) | chapter 1–81 |
| 4 | **Meditations**, Marcus Aurelius | The Stoic classic; Rufus already has long notes on it | Best: Gregory Hays (Modern Library, 2002, in copyright); Rufus's notes quote Hays. Open: George Long, Standard Ebooks, PD-US ✓ (stiff, Victorian) | https://standardebooks.org/ebooks/marcus-aurelius/meditations/george-long | 45,000 words (Long) | book.section (4.3) |
| 5 | **Enchiridion**, Epictetus | The shortest complete guide to Stoic practice | George Long, in Standard Ebooks' *Short Works*, PD-US ✓. Robin Hard (Oxford) reads better (in copyright) | https://standardebooks.org/ebooks/epictetus/short-works/george-long | 6,000 words (estimate) | chapter 1–53 |
| 6 | **First sermon** (SN 56.11, *Dhammacakkappavattana Sutta*) | The Four Noble Truths and the Middle Way, in the Buddha's own first teaching; short | Sujato, CC0 | `suttacentral.net/api/bilarasuttas/sn56.11/sujato?lang=en` | 1,000 words (estimate) | SN 56.11 + segment |
| 7 | **Satipaṭṭhāna Sutta** (MN 10) | The foundational meditation text; links to Rufus's practice | Sujato, CC0 (as for the Dhammapada) | `suttacentral.net/api/bilarasuttas/mn10/sujato?lang=en` | 3,100 words | MN 10 + segment |
| 8 | **Metta Sutta** (Snp 1.8) | The loving-kindness discourse; short and chanted daily | Sujato, CC0. Amaravati Sangha chanting version reads best: "©1994 English Sangha Trust", free-distribution terms ✓ | https://accesstoinsight.org/tipitaka/kn/snp/snp.1.08.amar.html | 250 words | Snp 1.8 (verses 143–152) |
| 9 | **Song of Zazen**, Hakuin | Short Zen chant; fits beside Shodoka | Aitken, Diamond Sangha *Daily Zen Sutras* (copyright, no licence stated) | http://www.ciolek.com/WWWVLPages/ZenPages/Daily-Zen-Sutras.html | 300 words | by line |
| 10 | **Ten Oxherding Pictures**, Kuoan Shiyuan | The stages of Zen practice in ten images and short verses; very visual, so a good test of the design | Paul Reps and Nyogen Senzaki, in *Zen Flesh, Zen Bones* (1957, in copyright). An open translation is not yet found; the old pictures themselves are public domain | terebess.hu (page **unverified**) | 1,000 words | picture 1–10 |
| 11 | **Platform Sutra**, Huineng | The founding text of Chan/Zen sudden awakening | Best: Red Pine (Counterpoint, 2006) or John McRae (BDK, 2000), both in copyright. Free online: A. F. Price and Wong Mou-lam (Shambhala, 1969; in copyright), hosted in full on terebess.hu, which also links PDFs of McRae and others. Wong Mou-lam's original 1930 Shanghai translation is probably public domain in the US by date (**unverified**) | https://terebess.hu/zen/huineng-eng.html | 15,000 words (**unverified**) | chapter (10) |
| 12 | **Genjōkōan**, Dōgen | Dōgen's most-read essay on practice and enlightenment | Aitken and Tanahashi, "Actualizing the Fundamental Point" (*Moon in a Dewdrop*, © 1985 San Francisco Zen Center) | https://terebess.hu/zen/dogen/KS-Genjo.html | 1,500 words | by paragraph |
| 13 | **Letters to Lucilius**, Seneca (a selection, about 20 letters) | Seneca at his most personal; pairs with the existing *Shortness of Life* | Richard M. Gummere (Loeb, 1917–25), Standard Ebooks, PD-US ✓ | https://standardebooks.org/ebooks/seneca/moral-letters-to-lucilius/richard-m-gummere | 213,000 words in all; 20 letters is about 30,000 | letter.section (Ep. 7.1) |
| 14 | **Zhuangzi**, Inner Chapters | The playful second Taoist classic | Best: Burton Watson (Columbia) or Brook Ziporyn (Hackett), in copyright. Open: Herbert Giles (1889), Wikisource | https://en.wikisource.org/wiki/Chuang_Tz%C5%AD_(Giles) | 15,000–25,000 words (estimate) | chapter 1–7 |
| 15 | **Bodhicaryāvatāra**, Śāntideva | The classic of the bodhisattva path; much loved in Tibetan practice | Adam Pearcey (Lotsawa House, 2007), CC BY-NC 4.0 ✓ on chapter 1 (whether all 10 chapters are there is **unverified**). Best-known: Padmakara (Shambhala, in copyright) | https://www.lotsawahouse.org/indian-masters/shantideva/bodhicharyavatara-1 | 12,000 words (estimate) | chapter.verse (8.90) |
| 16 | **Bhagavad Gita** | The central Hindu wisdom text; broadens the library beyond Buddhism | Best: Eknath Easwaran (Nilgiri, in copyright). Open: Edwin Arnold, *The Song Celestial* (1885, public domain, in verse) | Gutenberg (down today); Wikisource **unverified** | 20,000 words | chapter.verse (2.47) |
| 17 | **Ashtavakra Gita** | The most direct Advaita (non-dual) text; short | John Richards, "donated by him to the public domain" ✓ | https://realization.org/p/ashtavakra-gita/richards.ashtavakra-gita/richards.ashtavakra-gita.html | 7,500 words | chapter.verse |
| 18 | **Blue Cliff Record** | The great Zen koan collection, the elder sibling of the Mumonkan; Rufus's `Zen.md` quotes its introduction | Thomas and J. C. Cleary (Shambhala, 1977, in copyright). No good open version found | (book) | 100 cases; long | case 1–100 |
| 19 | **The Cloud of Unknowing** | The best Western contemplative manual | Evelyn Underhill (1922 edition), public domain by date | https://www.ccel.org/ccel/a/anonymous2/cloud/cache/cloud.txt | 45,000 words with introduction | chapter 1–75 |
| 20 | **Consolation of Philosophy**, Boethius | Western wisdom in the face of ruin; a bridge between Stoicism and Christianity | H. R. James, Standard Ebooks, PD-US ✓ | https://standardebooks.org/ebooks/boethius/the-consolation-of-philosophy/h-r-james | 42,000 words | book.prose/metre |

### What to do first

The focus now is the site, not many texts, so only four:

1. **Dhammapada** (the text is ready; Sujato).
2. **Heart Sutra**: tiny and openly licensed. It tests the "short text" layout, and Thich Nhat Hanh's version sits beside his Diamond Sutra.
3. **Tao Te Ching**: tests a chaptered text and, later, side-by-side translations.
4. ***Meditations***: tests a long text with book.section links, and is the first text where Rufus's existing notes can be brought in.

Numbers 5–10 are short, and most are openly licensed, so they are cheap to add once the pipeline works. Numbers 11–20 are for later and are the most open to cuts. Blue Cliff Record (long, no open text) and the four non-Buddhist texts at the end are the first candidates to drop. A cadence of about one new text a week, once the pipeline works, fits the brief's guess.

## 4. Rufus's existing notes (rufuspollock.com)

Searched `~/src/rufuspollock/rufuspollock.com` (read only) for meditations, aurelius, seneca, tao te ching, dhammapada, diamond sutra, zen, shodoka, mumonkan, stoic, heart sutra, faith in mind and epictetus. There are no hits for the Tao Te Ching, Dhammapada, Shodoka, Mumonkan, Heart Sutra or Faith in Mind.

- **`Meditations.md`**: the main one, about 7,400 words (created 2024-07-15; reflections dated 2022-05-30). It is notes on the **Gregory Hays** translation ("Thoughts and commentary on Marcus Aurelius' Meditations in the Hays translation"). The structure:
  - a short list of key themes and a prose "Reflections" section (for example, "Curious lack of joy… little of the self compassion and loving acceptance of Buddhism or IFS");
  - then sections by book ("Book 4", "Book 5"…), each made of a short heading that gives his gloss ("Memento mori and all is empty", "Positive fatalism"), a block quote from Hays in bold italic, and sometimes a line of comment.
  - It has about 196 quoted lines, cited by book and section ("Book 5, 23").

  This fits decision 0001.3's "quoted passage plus optional comment" model almost exactly, but the quotes will only match the text on the page if we publish Hays.
- **`Zen.md`** (360 words): general notes on Zen, with a long quote from the Clearys' introduction to the *Blue Cliff Record*. Quotes plus brief comments.
- **`Creating a Digital Garden for Life Itself.md`**: around line 150, an early statement of the Sutras idea: "When looking for a wisdom text e.g. diamond sutra, shortness of life etc I want an elegant, free, online (downloadable) all in one version…", plus "want the curation work done (why select this version)". Useful for the vision, not a text note.
- **`Yogins of Ladakh.md`** (5,600 words): excerpts and commentary on Crook and Low, under headings. Background for the Buddhist side, not a library text.
- Passing mentions only: `Atomic Habits.md` (a Seneca quote), `post/only-the-educated-are-free-epicetus.md` (one Epictetus line), `Sex, Ecology and Spirituality.md` (a Wilber quote that names the Diamond Sutra), `How Much is Enough.md` (Stoic aside), `post/tacitus-on-horoscopes-fate-and-happiness.md`. Other Zen-adjacent notes are `The Empty Mirror.md` and `mindfulness.md`.

Rufus's other notes may live elsewhere too, such as Zotero annotations or Kindle highlights. Nothing else was found on this machine.

## 5. Open questions for Rufus

1. **Which Dhammapada?** Recommendation: Sujato (CC0, structured, with Pāli). The default is to build with Sujato, and to show Thanissaro and Munindo as comparison samples later. Is Sujato the "open-source translation" you remembered, or was it another?
2. ***Meditations*: Hays or Long?** Recommendation: Hays, published with its status stated (per decision 0001.5). Your notes quote Hays, so his text is the only one their quotes will match, and Hays reads far better. But it is in copyright and needs your copy of the book, as an EPUB to convert. Can you supply it? The default: build with Long (public domain in the US) only as a stopgap until the EPUB arrives. Book.section links stay the same either way.
3. **Tao Te Ching: Le Guin or an open one?** Recommendation: Le Guin as the main text, with an open version alongside. Of the open ones, McDonald (1996) reads much better than Legge. The default is McDonald, if the next worker can confirm his public-domain release at its source; otherwise Legge, until a Le Guin EPUB is in hand.
4. **The Plum Village *Diamond Sutra* is a short version.** Recommendation: keep it but label it, and if you have *The Diamond That Cuts Through Illusion*, convert the full text. The default is to label it.
5. **Red Pine's full *Diamond Sutra*:** do you have the book (print or EPUB)? If so, the full 32 chapters can be converted. The default is to keep it marked as partial.
6. **The shortlist itself:** add, cut or reorder. In particular, are the non-Buddhist "wider" texts (Gita, Ashtavakra, Cloud of Unknowing, Boethius) wanted now? Recommendation: keep them, but at the end.
