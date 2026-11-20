# Tao Te Ching — how this edition was made

Edition: `/tao-te-ching.md` (live at https://sutras.lifeitself.org/tao-te-ching). Made 2026-11-21 by an AI agent (Claude), track `tao`, bead sutras-m2v.7.18. Comparison page: `/tao-te-ching-compared.md`.

## Sources

- `legge-gutenberg-216.txt`: James Legge, *The Tao Teh King, or the Tao and its Characteristics* (1891), Project Gutenberg eBook 216, produced by Gregory Walker and David Widger (released 1995, updated 2015). www.gutenberg.org was down for maintenance on 2026-11-20 and 2026-11-21 (503), so the file was fetched from the mirror at https://gutenberg.pglaf.org/cache/epub/216/pg216.txt.
- `legge-standardebooks-single-page.html`: a second copy for checking, Standard Ebooks’ edition of Legge (https://standardebooks.org/ebooks/laozi/tao-te-ching/james-legge), based on the same Gutenberg transcription and on Google Books scans. Also used for Legge’s preface (dated Oxford, 20 December 1890) and the colophon (“translated … in 1891”).
- `chinese-gutenberg-7337.txt`: 道德經, Project Gutenberg eBook 7337, produced by Ching-yi Chen (released 2005, updated 2020). It names no printed edition.
- `wang-bi` second copy: 道德經 (王弼本) on Chinese Wikisource (https://zh.wikisource.org/wiki/道德經_(王弼本)), used for checking the Chinese only.

## How it was made

1. The chapters were extracted from the Gutenberg file by script (`build_body.py` in the track’s scratch folder). Each chapter starts at its number: “N. 1.” or “Ch. 1. 1.”, or a bare “N.” before verse. Chapter 11 has no sub-number and chapter 6 is verse only; both were found by position, not by number alone.
2. Each chapter is one passage, id 1 to 81. The number is the passage link at the start of the chapter, in the margin. Legge’s own paragraph numbers stay in the text, escaped so Markdown does not make a list of them.
3. Verse (indented lines in Legge, 31 blocks) is set as `rs-gatha`, lines ending in two spaces.
4. The Chinese text for each chapter is one paragraph after the English (`p.orig`), joined from the Gutenberg lines. Gutenberg’s section headings (老子道經, 老子德經) are left out.
5. Typography: apostrophes made curly; the double hyphen made a spaced em dash.

## Checks

- English against the Gutenberg file, by script: every word in the edition is in the source, in order. The only words not in the edition are the Gutenberg header and the PART headings. 0 unlisted differences.
- English against Standard Ebooks, by script: 19 differences. Spelling and compounding (“non existence” / “nonexistence”, “fulness” / “fullness”, “waggons” / “wagons”, “any one” / “anyone”, “war horses” / “warhorses”, “by ways” / “byways”, “court yard” / “courtyard”, “Now a days” / “Nowadays”, “out stretched” / “outstretched”, “Every one” / “Everyone”, “acknowledgment” / “acknowledgement”, “non existent” / “nonexistent”); the heading “Part” (SE only); the Gutenberg header (Gutenberg only). Four readings differ, and we keep Gutenberg in each:
  - Chapter 43, the word after “non-action” (Gutenberg “Or”, SE “Of”).
  - Chapter 44, “Or fame or life” (Gutenberg) / “Of fame or life” (SE).
  - Chapter 64, “hold” (Gutenberg) / “bold” (SE): “does not lose his hold”.
  - Chapter 74, one “of” present in Gutenberg (“presides over the infliction of death”) and absent in SE.
  These need checking against a scan of the 1891 book.
- Chinese against the Wang Bi text on Chinese Wikisource, by script (characters only, Wikisource commentary removed): most chapters agree apart from variant forms (矣/已, 于/於, 朴/樸, 兮/焉, 形/較). Wording differs in several chapters, most of all 15, 28, 45 and 71. Chapter 81 cannot be compared: the Wikisource page runs on past the text. The Chinese is shown as a witness to the Wang Bi tradition, not as the text Legge translated.

## Every change to the words

- Typography only: curly apostrophes, spaced em dashes for “--”.
- Legge’s paragraph numbers are kept as printed.
- The Gutenberg header, the “PART” headings and the Chinese section headings are left out.
- Chapter numbers are the passage links (`id="1"` … `id="81"`).
- No word is changed in the English. The Standard Ebooks differences above are not changes we made.

## Facts and where each comes from

- Legge (1815–1897), Scottish sinologist, first professor of Chinese at Oxford: Standard Ebooks’ description of the book, and the Gutenberg catalogue (“Legge, James, 1815-1897”).
- Translation published 1891, *Sacred Books of the East* vol. 39: Standard Ebooks colophon and its note on Legge’s preface.
- Preface dated Oxford, 20 December 1890: Legge’s preface, as printed by Standard Ebooks.
- Laozi “sixth century BC”: Legge’s preface; Standard Ebooks’ description (“written around the 6th century BC by Laozi, a Zhou-dynasty courtier”).
- Herbert Giles’s questioning of authorship in 1886 (*China Review*) and “one of the ablest Chinese scholars living”: Legge’s preface.
- Ssŭ-ma Ch’ien, died about 85 BC, “well acquainted with our treatise”: Legge’s preface.
- Ho-shang Kung’s text and the division into eighty-one chapters, Wang Pi (died 249 at twenty-four), Wu Ch’eng (1249–1333): Legge’s preface.
- Legge’s rhymed chapters are the indented blocks in the text.

## Copyright

Legge died in 1897; the translation and the Gutenberg Chinese are in the public domain. Our additions are CC BY 4.0.
