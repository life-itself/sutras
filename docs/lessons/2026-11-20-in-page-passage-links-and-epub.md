# In-page passage links break in the EPUB

From the Shodoka edition (2026-11-20). `scripts/epub` gives stanzas the ids `s1`…`sN`, so a link like `[verse 18](#18)` in an introduction becomes a dead `#id_18` in the EPUB.

**Lesson:** until bead sutras-m2v.7.9 is done, write passage links as `/<slug>#N`. They work on the web and become links to the live site in the EPUB. Open the EPUB's XHTML and check `href`s before shipping.
