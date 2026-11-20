# The Gateless Gate (Mumonkan) — how this edition was made

Edition: `/gateless-gate-mumonkan.md` (live at https://sutras.lifeitself.org/gateless-gate-mumonkan). Made 2026-11-20 by an AI agent (Claude), track `mumonkan`, bead sutras-m2v.7.5.

## Sources

- `sacred-texts-mumonkan.htm`: the source, as fetched on 2026-11-20 from the Wayback Machine's copy of https://www.sacred-texts.com/bud/zen/mumonkan.htm dated 2026-05-01 (http://web.archive.org/web/20260501170316id_/https://www.sacred-texts.com/bud/zen/mumonkan.htm). The live page answers automated requests with a Cloudflare challenge (HTTP 403). The archive holds the same page back to 2003. It is a Microsoft Word export: Sekida's English with the Chinese sentence by sentence, Mumon's preface, the 48 cases (each: case, "Mumon's Comment", "Mumon's Verse 頌曰") and Mumon's postscript. Its head note says: author "Chinese Ch'an master Wu-men Hui-hai (無門慧開 Mumon Ekai, 1183-1260)" ("Hui-hai" is a slip for Hui-k'ai); "English Translation By late Zen master Katsuki Sekida (Two Zen Classics 26-137)"; Chinese "taken from the following Japanese web site: https://homepage1.nifty.com/poem-club/mumonnkan/mumonkanwoyomu.htm", whose texts "are taken from the book titled Mumonkan, published in Japan by Iwanami Bunkõ"; characters the site could not give appear as empty boxes.
- `cbeta-T48n2005.xml`: a second witness for the Chinese, used for checking and for filling the boxes. The Taishō text, T48 no. 2005 *Wumen guan* 無門關, in CBETA's TEI XML, fetched 2026-11-20 from https://raw.githubusercontent.com/cbeta-org/xml-p5/master/T/T48/T48n2005.xml.
- The translator was checked: Open Library (https://openlibrary.org/works/OL8599181W) records *Two Zen classics: Mumonkan and Hekiganroku*, "translated with commentaries by Katsuki Sekida; edited and introduced by A.V. Grimstone", Weatherhill, New York, 1977, 413 p.; and a 2005 Shambhala edition (ISBN 1590302826). Sekida's dates (1893–1987) are from the Library of Congress name authority n80164936 (heading "Sekida, Kazuki, 1893-1987", 関田一喜; it cites *A Guide to Zen*, 2003: "modern Zen master"). The old file `gateless-gate-mumonkan.md` named only sacred-texts; its English words were identical to this source.

Not used: Senzaki and Reps's 1934 translation (possibly public domain in the US, unverified) is the open alternative noted in `docs/library-shortlist.md`. Sekida reads better and is what the site already had.

## Scripts (in this folder; run from the repo root)

- `parse_source.py`: reads the source page into preface, 48 cases and postscript, each in parts (case, comment, verse) of Chinese–English sentence pairs. Changes no words.
- `compare_chinese.py`: compares the source's Chinese with the Taishō, section by section, punctuation dropped and common variant forms treated as equal. `--boxes` lists the boxes and the Taishō character at each; `--kept` lists the differences left after the fixes (saved as `chinese-differences.txt`).
- `fixes.py`: every correction to the source's words, used by the two scripts below.
- `extract.py`: made the first version of the text section of the page (run once; the page has since been edited by hand, so do not overwrite it).
- `compare.py`: compares the page with the source, word for word (English) and character by character (Chinese), and fails on any difference not accounted for here. `scripts/compare-source` is written for *Faith in Mind* only; this is its approach for this text. Result on 2026-11-20: 50 sections (preface, 48 cases, postscript), 8,342 English words, 7,899 Chinese characters, 35 boxes filled, 0 unexpected differences.

## How it was made

1. The text was extracted from the source by script (`extract.py`), not retyped.
2. Each case got the case number as its link target (`/gateless-gate-mumonkan#1` … `#48`); Mumon's preface is `#preface` and his postscript `#postscript`. The numbers are the traditional ones, given in the source's headings.
3. Each case is marked in three parts: `<div class="koan-case">`, `<div class="koan-comment">`, `<div class="koan-verse rs-verse">`; the preface and postscript prose are `<div class="koan-prose">`. The Chinese of each part is a `<p class="orig" lang="zh">`. Part labels use the existing `rs-label` style until the site track styles `koan-label` (bead filed).
4. Layout: the source sets each Chinese sentence above its English. Here the English sentences of each part are run together as a paragraph (the source's paragraph breaks kept), and the Chinese of that paragraph follows it as one paragraph. Verses are four English lines, then the four Chinese lines. Three places are set as the source sets them rather than run together: the poem Fuketsu quotes (case 24, as lines), the three barriers of case 47 (one paragraph each), and the date and signature at the end of the postscript (as lines).
5. Typography and the fixes below were applied; `compare.py` was run.

## Every change to the words

English:

- No word of the translation changed, except: case 10 title "Seizei Is Utterly Destitude" to "Destitute".
- Long vowels: the source's "õ", "û" and "Õ" (a conversion slip in the Word export: Jõshû, Hyakujõ, Õbai) printed as "ō", "ū", "Ō" (Jōshū, Hyakujō, Ōbai), the standard Hepburn macrons, throughout (148, 56 and 4 times).
- Straight quotation marks and apostrophes made curly.
- "1.", "2.", "3." in case 47 escaped so Markdown does not make them a list; not a change to the words.
- Left as in the source: "Oshō" and "Osho" both occur (case 44 has "Bashō Osho"); "Bunkō", "rises towering waves" (case 48), "This moment's thoughts sees" (case 47 verse), "you are a Buddha himself" (case 30), American spelling.

Chinese:

- The source's stray spaces inside Chinese sentences dropped (for example 從　前 in case 1, 驚天　動地, 三　十三天 in case 48). They are not characters of the text. The full-width space between number and title in each case title is kept.
- 36 empty boxes filled from the Taishō: case 4 懵; 6 謼; 9 兮; 11 誵; 12 喏, 喏, 喏, 𦗚; 17 飡, 撑, 拄; 20 𦗚; 21 撑; 23 蹰; 25 謼; 28 悱, 悱, 匾; 31 爾; 40 𣔻, 趯, 𦗚, 趯, and 趯 in the title (四十　趯倒淨瓶, as in the Taishō contents list); 41 缺, 咦, 爾; 42 匝; 44 撑, 并; 47 飡, 覻, 覻, 覻; 48 𨁝, 簸. Three of these (𦗚, 𣔻, 𨁝) are outside the basic Unicode plane and may not display in every font.
- 40 slips corrected (39 entries in `fixes.py`; one covers both the title and the text of case 10), each where the source has a character of similar shape that makes no sense in place, and the Taishō has the character the sense and Sekida's English require. Listed with context in `fixes.py`. In short: 堅 for 竪 "raise" (case 3 title and twice in the case, three times in case 11); 方 for 法 in 正法眼藏 "True Dharma Eye" (four times, case 6); 興 for 與 (cases 3, 44); 其 for 某 in 某甲 "I" (cases 7, 23); 貶 for 眨 "blink" (preface, case 21); 巳 for 已 (21); 化 for 火 (21); 挂 for 拄 "support" (21); 既 for 即 (twice, case 9); 候 for 侯 (9); 弧 for 孤 "destitute" (case 10, title and case); 未 for 末 "last" (13); 遂 for 逐 (16); 鷹 for 應 "answers" (22); 白 for 曰 "said" (23); 問 for 門 in 無門曰 (23); 末 for 未 (26); 君 for 吾 "our" (28); 晴 for 睛 "eye" (28); 輻 for 軸 "axle" (8); 綾 for 稜 (32); 抗 for 坑 "ditch" (38); 欄 for 攔 "stop" (40); a dash printed for 一 (case 1, 打成一片); and three characters missing from the source, added: 尊 (case 6, 迦葉尊者), 開 (case 40, 開山 "founder"), 立 (case 48).
- Kept as in the source: the Japanese edition's character forms (爲, 説, 衆, 擧 and the like, where the Taishō has 為, 說, 眾, 舉), and 21 differences of reading where either could stand (for example 抉瘡 for the Taishō's 剜瘡 and 擱他不在 for 攔他不住 in the preface; 髭 for 鬚 "beard" in case 4; 輸 "loses" in case 40, where the Taishō's 輪 is the slip). All are in `chinese-differences.txt`.

Not the translator's words (ours): all headings except the case titles ("The text", "Mumon’s preface", "Mumon’s comment", "Mumon’s verse", "Mumon’s postscript"; the source has "Mumon's Preface", "Mumon's Comment", "Mumon's Verse" and "Mumon's Postscript"), the contents list, the in brief, the editors' introduction, the three notes, About this translation, Source and licence.

## What the source leaves out

The source gives Mumon's preface and verse, the 48 cases and his postscript. The Taishō text (and Wikipedia's account of the 1246 Japanese woodblock edition) also has: an introduction by Xi'an Chen Xun (習菴陳塤) and Wumen's dedication to the emperor (before the preface); the table of contents; and after the postscript the "Zen Warnings" (禪箴), Huanglong's Three Barriers (黄龍三關) by Wuliang Zongshou, Menggong's addendum and a 49th case by Anwan. Not given here; could be added from the Taishō with a translation if one is found.

## Facts used in the introduction, About this translation and the notes, and where each comes from

- Wumen Huikai, 1183–1260, Mumon Ekai in Japanese; 48 koans; compiled in the summer of 1228 at Longxiang; "Wumen" means "no gate" and the title also reads "Wumen's Barrier"; each koan has a comment and a verse; dropped from the Chinese canon after the Song, taken to Japan by his disciples and reprinted many times; with the Blue Cliff Record central in Rinzai practice; the extra material in printed editions: English Wikipedia, "The Gateless Barrier", read 2026-11-20.
- "as brickbats to batter the gate" (preface), “the front gate to Zen” (case 1 comment), “Your direct realization is demanded; it should not be sought through others” (postscript): the text, verbatim.
- Sekida's dates, *Zen Training* (1975): Library of Congress name authority n80164936 (it cites "His Zen training, 1975"). "Japanese Zen teacher": the same record cites *A Guide to Zen* (2003) calling him a "modern Zen master". Book details: Open Library, above. Pages 26–137: the source's head note.
- Note on Mu: English Wikipedia, "Mu (negative)": 無, *wu* in Chinese, *mu* in Japanese, "'to lack' or 'without'".
- Note on Jōshū: English Wikipedia, "Zhaozhou Congshen" (778–897; Japanese Jōshū Jūshin). The five cases with his name in their titles (1, 7, 11, 31, 37) were counted from the text.
- Note on the patriarchs: the Shodoka in this library, verse 42, quoted verbatim ("Twenty-eight generations of teachers in India", "passed through six teachers here"); that Bodhidharma is counted the 28th in India and first in China is also in English Wikipedia, "Lineage (Buddhism)".
- Note on samadhi: English Wikipedia, "Samadhi" ("a state of meditative consciousness").

## Copyright

Sekida's translation (1977) is in copyright. Published in full under decision 0001 point 5, with the status stated on the page. The Chinese text is 13th-century and in the public domain; the Taishō and CBETA were used to check it and to fill 36 characters, not copied as a text.
