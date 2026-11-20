# Prose editions: one passage container per section, and what the contents rail copies

From the Meditations edition (2026-11-20, sutras-m2v.7.13).

- **One `<div class="rs-passages">` per section,** with the link `<a class="v" id="4.3" href="#4.3">4.3</a>` on the first line of the first paragraph and a blank line before the closing `</div>`. The check then tests every section's first block (499 of them), not just one per book. The `<div>` opener needs a blank line after it, or Flowershow reads the Markdown inside as raw HTML.
- **The contents rail copies heading text.** A footnote marker in a heading (`## Book 2: …[^book2]`) put the footnote text into the rail. Put the note on the first entry instead (`make_page.py` does this).
- **Pandoc keeps raw HTML.** `scripts/epub` leaves the `<a class="v">` links and the `<nav class="rs-rail">` in the EPUB; the links work, the nav shows an empty "Contents" label (sutras-ypl).
- **Headless screenshots lie about width.** `chrome --window-size=390` gave a layout wider than 390px, and the phone view looked cut off although the page had no overflow. Use Playwright with `channel="chrome"` and read `document.documentElement.scrollWidth` as well as the picture. Chrome's `--screenshot` also hangs unless given its own `--user-data-dir`.
