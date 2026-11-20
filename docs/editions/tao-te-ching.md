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
- English against Standard Ebooks, by script, chapter by chapter (Standard Ebooks marks each chapter, so this also checks where our chapters begin and end): spelling and compounding only (“non existence” / “nonexistence”, “fulness” / “fullness”, “waggons” / “wagons”, “any one” / “anyone”, “war horses” / “warhorses”, “by ways” / “byways”, “court yard” / “courtyard”, “Now a days” / “Nowadays”, “out stretched” / “outstretched”, “Every one” / “Everyone”, “acknowledgment” / “acknowledgement”, “non existent” / “nonexistent”), Standard Ebooks’ dropping of single quotation marks inside the text, and four readings:
  - Chapter 44, “Or fame or life” (Gutenberg) / “Of fame or life” (SE).
  - Chapter 44, “Or life or wealth” (Gutenberg) / “Of life or wealth” (SE).
  - Chapter 64, “does not lose his hold” (Gutenberg) / “bold” (SE).
  - Chapter 74, “presides over the infliction of death” (Gutenberg) / “the infliction death” (SE).
  The first version of these notes listed one of the chapter 44 readings under chapter 43; chapter 43 has no difference.
- The four readings against the 1891 printing: *The Sacred Books of China: The Texts of Taoism*, part 1 (Sacred Books of the East, vol. 39, Oxford: Clarendon Press, 1891), archive.org scan `sacredbookschin00legggoog` (Google scan), book pages 87, 108 and 117. The page images show “Or fame or life,” and “Or life or wealth,” (ch. 44), “does not lose his hold” (ch. 64) and “presides over the in-fliction of death” (ch. 74). Gutenberg is right in all four; no change. Crops of the four places are in the private library (`scans/`).
- English against the 1891 printing, by script: every word of the edition compared with the text layer (OCR) of the same scan, in order. 56 places differ, and every one is an OCR error in the scan's text (“T o” for “Tao”, “mukiplication”, “energry”, “diflsculty”, “bests” for “hests”, words joined at line ends such as “warhorses” and “lealheartedness”) or the OCR's running heads and notes. No word of the edition differs from the printed book.
- Passage ids: 81, numbered 1 to 81 in order, each once; all 81 are in `scripts/published-ids.txt`.
- Notes: the Gutenberg text has none of Legge's notes or chapter titles (in the 1891 book these follow each chapter), so the edition has none. Nothing to attach.
- Chinese against the Wang Bi text on Chinese Wikisource, by script (characters only, Wikisource commentary removed): most chapters agree apart from variant forms (矣/已, 于/於, 朴/樸, 兮/焉, 形/較). Wording differs in several chapters, most of all 15, 28, 45 and 71. Chapter 81 cannot be compared: the Wikisource page runs on past the text. Re-run 2026-11-21 by a second script: the chapters most different are 71, 45, 37, 28, 23 and 15. The Chinese is shown as a witness to the Wang Bi tradition, not as the text Legge translated.

## Every change to the words

- Typography only: curly apostrophes, spaced em dashes for “--”.
- Legge’s paragraph numbers are kept as printed.
- The Gutenberg header, the “PART” headings and the Chinese section headings are left out.
- Chapter numbers are the passage links (`id="1"` … `id="81"`).
- No word is changed in the English (checked again 2026-11-21 against the 1891 scan: 0 words changed). The Standard Ebooks differences above are not changes we made.

## The comparison page

`/tao-te-ching-compared.md`, checked and revised 2026-11-21. 32 quoted blocks (about 2,630 words), every one read against a printed page: Legge against the edition; Giles against the Wikimedia Commons page images of the 1904 book; Carus (1898), Medhurst (1905) and Goddard (1919, Brentano's) against archive.org page images; the modern samples against scans or copies of the books, with a second copy where one could be found.

Corrected: Giles ch. 1 “dogged” → “clogged” and two stray marks in ch. 11 (Wikisource transcription errors; the first version printed them with *[sic]*); Medhurst ch. 8 “unmeasurable” → “immeasurable” (OCR); Carus ch. 1 rhyme set as lines and ch. 11 paragraph break, as printed; Medhurst ch. 76 dashes as printed. Restored: Legge ch. 1 paragraph 4, Medhurst ch. 1 paragraph 2, and the second half of Giles's ch. 8, which he put in a different chapter of his book. Giles's chapter labels now give his own chapter numbers and titles. Goddard's source changed from a sacred-texts mirror to the 1919 scan (no word differs).

Modern samples, in copyright, quoted as samples: Red Pine (Mercury House 1996), chapters 1 and 11; D. C. Lau (Penguin 1963), chapter 1; Feng and English (Vintage 1972), Mitchell (Harper & Row 1988), Addiss and Lombardo (Hackett 1993) and Le Guin (Shambhala 1997), chapter 11. Ellen M. Chen is not quoted: we could not tie the copies we found to her printed book. Where each was read is in the private library's notes (some are unauthorised copies, so they are not linked).

## Facts and where each comes from

Checked 2026-11-21 against the 1891 printing (archive.org `sacredbookschin00legggoog`, text layer and page images) and Standard Ebooks. Standard Ebooks modernises Legge's names (Laozi, Sima Qian); the 1891 book has Lâo-dze, Sze-mâ Khien, Wû Khäng.

- Legge (1815–1897), Scottish, missionary of the London Missionary Society, first professor of Chinese at Oxford (1876–1897): Gutenberg catalogue (“Legge, James, 1815-1897”); Wikipedia, James Legge (fetched 2026-11-21).
- Published 1891 as *The Sacred Books of China: The Texts of Taoism*, part 1, *Sacred Books of the East* vol. 39, Oxford, Clarendon Press: title page of the scan.
- Preface dated Oxford, 20 December 1890: the preface.
- Sima Qian, died about 85 BC; his account that Laozi was “a curator of the Royal Library of Chou”, wished to withdraw from the world, and wrote the book in two parts for the warden of the pass: Legge's introduction, ch. 2.
- Laozi's birth “probably” 604 BC: Legge's introduction, ch. 2 (“It has been said above that the year B.C. 604 was, probably, that of Lâo-dze's birth”).
- Herbert A. Giles, *China Review*, March and April 1886: Legge's introduction, ch. 2, and preface. “The work … is undoubtedly a forgery”: Giles as quoted in Legge's preface. Legge's reply in the *China Review*, January and February 1888, and “My confidence has never been shaken for a moment”: the preface.
- Ho-shang Kung's text, and “the division of the whole into parts and eighty-one chapters … all attributed to him”: the preface.
- Wu Ch’eng (1249–1333), whose commentary “has been of the highest service to me”: the preface.
- Wang Pi (died 249, “at the early age of twenty-four”): the preface. (No longer in the introduction.)
- Legge's rhymed chapters are the indented blocks in the Gutenberg text, and are set as verse in the 1891 book.
- “About forty minutes straight through”: our estimate, 10,407 words at about 250 words a minute.
- The introduction uses pinyin for Sima Qian and Wu Cheng, since Legge's text on the page names neither; Legge's 1891 spellings differ (Sze-mâ Khien for Sima Qian), and Standard Ebooks modernises them.

Cut from the first introduction (2026-11-21), because no source we read supports it: “an official at the Zhou court” (replaced by Sima Qian's account, as Legge gives it); “Legge worked chiefly from” Ho-shang Kung (he lists six sources); “Legge’s preface does not reargue that quarrel” (it is the introduction that says so); “Herbert Giles questioned it” (Legge calls him Herbert A. Giles, and the quotation is now given).

## Copyright

Legge died in 1897; the translation and the Gutenberg Chinese are in the public domain. Our additions are CC BY 4.0.
