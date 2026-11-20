# Versions side by side map by passage, not by number

Learned building the Tao Te Ching comparison page (bead sutras-m2v.7.19).

- **Numbers do not carry across translations.** Giles (1904) groups the sayings into his own thematic chapters; his “chapter 1” holds Tao Te Ching chapters 1, 4, 14 and others. Carus’s headings are numbered, but the scan reads one chapter as “II.” Medhurst numbers by the book's own chapters. A side-by-side feature cannot assume that passage 11 in one version is passage 11 in another. It needs a map from each version's passages to the text's passage ids, kept as data, with the matching method (by wording, or by number) recorded.
- **A version has its own source and rights, and both must be on the page.** Public-domain status went by publication date (the US rule), and Giles's translator died in 1958, so his text may be in copyright elsewhere. The feature needs a rights field per version, not one per text.
- **Verbatim is a property of the copy.** Carus and Medhurst came from OCR text layers; broken words, line-end hyphens and note markers had to be cleaned before the lines matched their source. The feature should keep the cleaned text and the source it came from, so a reader can check a line against the scan.
- **Samples, not full text, for in-copyright versions.** The page quotes only what we can show verbatim from a source we read. A translation with no such text is listed as wanted, not left out silently. The feature should show that state.
- **Check by script, per block.** Comparing each quoted paragraph (letters only, so OCR hyphens and page headers do not matter) against its saved source caught nothing wrong in the final page but caught a page header inside a quote; a check on the whole page would have hidden it.

How it should work as a feature: a text has passages with ids; each version maps its own passages to those ids (by wording where numbers differ); each version carries source, licence and status (full, sample, wanted); the reader sees the same passage in each version, one after another, with the translator, year and status on each block.
