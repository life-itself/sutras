# A blank line inside a verse makes a new stanza, and the check fails it

From the Dhammapada edition (2026-11-20). The book sets off a list or a second voice inside a verse with a blank line (verses 137-140: the opening, then a list of ten things, then the close). Markdown reads a blank line as the end of a paragraph, and `scripts/check` reads it as the end of a stanza, so the list and the close failed with "passage without an id".

Fix used: a blank line inside a verse becomes a line holding `&nbsp;`, with the usual two trailing spaces. The verse stays one stanza with one passage link, and the gap still shows.

Two related things from the same edition:

- A page with one `rs-verse` block per chapter (26 blocks, with `###` headings between them) passes the check, but `scripts/epub` only handles one block. It leaves 25 `:::` divs unclosed, so the EPUB's verses and About section end up in one file. Filed as bead `sutras-m2v.8.11`.
- Building a page from a verified draft by script (`library/dhammapada/build_page.py`) and comparing its words by script (`compare.py`) took less time than checking an edition by hand, and found the blank-line problem at once. Keep both scripts with the edition.
