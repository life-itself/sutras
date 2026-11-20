# Raw HTML links do not cross EPUB files

Date: 2026-11-20. Track: epub.

Pandoc splits an EPUB into one file per chapter and fixes Markdown links (`[x](#17)`) to point at the right file (`ch005.xhtml#s17`). It does not touch links written as raw HTML (`<a href="#s17">`), so a contents list in raw HTML pointed at ids in other files, and epubcheck failed with "Fragment identifier is not defined" (48 errors in the Mumonkan).

- Turn a list of links into Markdown (`- [Case 1](#1)`) before Pandoc sees it, and take the raw `<ol>`/`<li>` wrapper off.
- After any change to the builder, run epubcheck on every EPUB; a missing fragment is an error, not a warning.
- A Markdown list inside a raw HTML block is not parsed; the blank lines around it are what let Pandoc read it.
