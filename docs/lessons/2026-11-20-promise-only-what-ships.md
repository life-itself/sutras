# Promise only what every listed page already does

Date: 2026-11-20. Track: site (home and about pages).

The first home page said every text had passage links, margin notes and an EPUB. Only *Faith in Mind* did. A critique subagent caught it in one pass, along with a wrong translator credit copied from an old page (Shodoka) and a missing co-translator.

- Describe the library as it stands: "being made into editions", "notes to come", "shortened version", "partial".
- Take credits and one-line descriptions from each edition's frontmatter and `NOTES.md`, not from the old page or memory. Edition tracks correct credits (the Shodoka's changed the same day), so the home page line is updated when an edition lands.
- Markdown is not parsed inside a raw HTML element (`<p class="rs-inbrief">`): use `<em>`, not `*…*`.
