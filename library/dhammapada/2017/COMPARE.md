# 2011 edition-draft vs 2017 revision: verse comparison

Compared: `../edition-draft.md` (2011, verses 1-423) against `dhammapada-2017.pdf` (Revised edition 2017, text extracted to `verses.txt`). Normalised: curly and straight quotes, dashes, `&emsp;` indentation, line breaks, hard breaks, footnote markers, extra spaces. Comparison is by word tokens (punctuation ignored). Scripts: `extract.py` and `compare.py` in the session scratchpad (not in the repo).

Unit note: the 2011 file prints ten groups under joint anchors (58-59, 137-140, 188-192, 195-196, 229-230, 244-245, 246-248, 256-257, 271-272, 360-361). These are compared as groups, so a difference inside a group counts all its verses as differing.

## Numbers

- Verses identical after normalisation: 413 of 423.
- Verses differing in words: 10 (9 verses on their own, plus verse 271 and its partner 272 as one group where only 271 changes). Without the group rule: 9 verses.
- Verses that differ only in punctuation or spacing (words identical): 8.
- Total differing word tokens: 19 (counted as the larger side of each changed span).

## The nine changes

| Verse | 2011 | 2017 | Tokens |
|---|---|---|---|
| 90 | is fully released in all respects | is everywhere fully released | 4 |
| 203 | as it actually is | as it has come to be | 4 |
| 411 | has come ashore in the Deathless | has gained a footing in the Deathless | 3 |
| 20 | his mind well-released | his mind well released | 2 |
| 75 | should not relish offerings | shouldn't relish offerings | 2 |

Ties at 2 tokens were broken by lowest verse number. Four one-token changes follow, not in the table: 92 "trail" to "course"; 271 "precepts" to "habits"; 348 "let-go" to "released"; 368 "kindness" to "goodwill". (Verse 20 and 75 are small; the largest difference anywhere is 4 tokens.)

## Structure

- Chapter headings: identical, 26 of 26 ("I : Pairs" to "XXVI : Brahmans"; 2017 prints them as "Dhp I : Pairs").
- Verse numbering: identical, 1 to 423, same order, no gaps, no verse present in one and missing from the other.
- Grouping: the 2017 PDF prints verses in numbered blocks (e.g. "1-2*", "3-6") with a stanza per verse; 9 of the 10 joint groups above are one stanza for the whole range in 2017 as well; 229-230 are two stanzas in 2017. No extra or missing lines were found: every difference is a word-level substitution or the one insertion/deletion in verse 90.
- Asterisks in 2017 mark verses discussed in End Notes; the 2011 draft carries footnote markers instead (not compared).

## Front and back matter (cheap check only)

- Preface: 97% word match; differs only in the signature block (2017 adds "Geoffrey DeGraff" and prints the place in capitals).
- Introduction: 99.5% word match by token ratio; differences seen are verse reference formatting only.
- The 2017 PDF carries End Notes (from p. 134) and a Glossary and Bibliography; the 2011 draft has footnotes and no End Notes section. These were not compared.
- Copyright: 2017 says "Copyright 2014 ... Revised edition 2017" under CC BY-NC 4.0; the 2011 draft says "Copyright 1998 (Revised edition, 2011), For Free Distribution".
