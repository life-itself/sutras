# Ebook PDFs parse cleanly by layout, but watch page breaks

Calibre-made ebook PDFs (both Diamond Sutras) give clean text with `pdftotext -layout`: paragraphs start with an indent, verses are indented blocks after a blank line, chapter numbers are centred lines. A small parser (`library/diamond/compare.py`) turns that into edition Markdown and later checks the edition against it, so the text is never retyped.

Three traps, each caught only by looking:

- **Page breaks.** A form feed can replace the blank line between two paragraphs, so a parser that splits on blank lines merges them. Treat an indented line after a page break as a new paragraph. A planted fault showed the checker catches the merge (block counts per section differ).
- **Split capitals.** The converter writes "M oreover", "M ount". Repair at read time and say so in `NOTES.md`.
- **Line-end hyphens.** In a reflowed ebook a hyphen at a line end is the book's own ("World-/Honored"): keep it when joining. But the ebook itself can have lost one ("billionworld"); a second witness shows it.

And a style trap: the personal theme decorates every blockquote with a red opening quote mark, so a blockquote is wrong for a verse inside the text. Set verses as line-broken paragraphs until the template has a verse-in-prose style (bead sutras-m2v.7.14).
