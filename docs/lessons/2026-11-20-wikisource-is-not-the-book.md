# A cleaned-up online copy can still drop notes: diff it against a second copy

From the Seneca edition (2026-11-20). Wikisource's text of Basore's translation is cleaner than the old Forum Romanum page it seems to derive from: it fixes a dozen OCR slips. But it has lost one of Basore's notes (Liternum), attached the next note in its place, and put another marker on the wrong word. Only a word-and-marker diff against the dead page (read through the Internet Archive) showed this; reading either copy alone did not.

**Lesson:** when the source has notes, compare where each marker sits and each note's words, not just the running text (`library/seneca-on-the-shortness-of-life/compare.py` does both, ignoring numbering). A dead source link is often still in the Wayback Machine: fetch it with the `id_` URL form to get the raw page. Counts in a brief are claims too: "67 footnotes" was 47.
