# EPUBs

Status: v2, 2026-11-21: design direction A (cover, title page, stylesheet) and the frontispiece. Track `epub` (beads sutras-m2v.8.3, 8.21, 3.2). Every published edition has a plain EPUB at `downloads/<slug>.epub`, linked from its page as Download. This guide says how they are made and how they stay current.

## How it works

`scripts/epub` (Python, with Pandoc) reads the same `<slug>.md` the site publishes and writes the EPUB:

- **Text:** the web layout (header, contents rail) is dropped; verse (`rs-verse`) and prose (`rs-passages`, `rs-gatha`) become Pandoc containers; passage numbers become spans that links point at (`#s4.3`); linkable headings and contents lists become Markdown links, so they reach the file that holds their target.
- **Structure:** one file per chapter. Level-3 headings split the text where the text has them (Dhammapada, Seneca, the Mumonkan's cases); otherwise level 2 (Meditations' books, the Diamond sutras, Faith in Mind, Shodoka). The contents list is generated from the same headings.
- **Metadata:** title; creator is the author without the bracketed dates and notes (the frontmatter keeps them); translator is a contributor with role `trl`; language `en-GB`; rights from the licence line; source; subject from `tradition`; publisher is the site. The identifier is a UUID made from the site address and the slug, so it never changes.
- **Date:** dc:date and the zip timestamps come from the source's last commit, not the clock. An unchanged source gives a byte-identical EPUB; a rebuild on another machine gives the same file.
- **Cover:** in the manner of Fitzcarraldo Editions' covers, which Rufus liked for the EPUBs: one flat colour (the warm red), the name above and the title below, both in spaced capitals, centred in the upper half, nothing else. The name is the author's, or for the anonymous and traditional texts (the Diamond Sutras, the Dhammapada) "Translated by" the translator, which also tells the two Diamond Sutras apart. It is a 1600×2400 PNG drawn by `cover()` with Pillow in Literata (`scripts/fonts/Literata-cover.ttf`, a 54 KB Latin-capitals subset, OFL): a raster because Kindle and Kobo need one for the library thumbnail, where an SVG with live text fails or falls back to another font. The PNG is kept in `downloads/covers/<slug>.png` and redrawn only when its words, colours, font or `cover()` change (it carries a hash of them), because Pillow on a Mac and on Linux anti-alias slightly differently; so a build here and the Action's give the same EPUB. Recolour every cover with `COVER_GROUND` and `COVER_INK` above `cover()` (the paper `#ebe7e0` with ink `#211e1b` is the quiet alternative).
- **Frontispiece and title page:** the page's image (`<figure class="sd-art">`, from `assets/images/<slug>.jpg`) is packaged in the book and set at the top of the title page with its credit, then the label ("Zen · a poem") in red, the title, the author and the translator, as the site's head is. The publisher, date and rights are left off it (they are in the metadata and the book's Source and licence section) so the title stays on a phone's first screen. The image is not on the cover: a cover is seen as a thumbnail, where an ink painting turns to mud and its credit cannot go; inside it is seen whole, and credited.
- **Style:** `scripts/epub.css`, deliberately small, following direction A (decision 0005). Literata if the reader has it, else the reader's serif (no fonts embedded: each would add about a megabyte to every book, and most readers let the reader choose). No background or text colour: readers' white, sepia and night themes are the paper. The red `#c9502f` only on passage and stanza numbers, note marks and numbers, the "In brief." label and the title-page label. Each verse line is a `span.l` with a hanging indent, so a wrapped line can be told from a new one (the `<br />` stays for readers that ignore the stylesheet); stanza numbers sit on their own line; labels in the text (the Mumonkan's "Mumon's comment") are red italic; original-language text (`p.orig`, Chinese) is a little smaller with a CJK face, notes are EPUB pop-up notes (`aside epub:type="footnote"`); in readers that show the list at a chapter's end instead, each note is numbered with a link back to its mark.
- **Check:** if `epubcheck` is on the PATH, every EPUB is validated and the build fails on errors.

The output is committed because Flowershow has no build step: the site serves whatever is in the repo.

## Rebuild

```sh
scripts/epub --all                 # every edition with status: published
scripts/epub seneca-on-the-shortness-of-life   # one edition
```

Needs `pandoc` (3.10.1 is what the Action uses; output can differ between Pandoc versions), `pyyaml`, Pillow (11.3.0 locally and in the Action), and `epubcheck` (`brew install epubcheck` on the Mac). Then commit the changed `downloads/` files with the change to the source.

## The Action

`.github/workflows/epub.yml` runs on a push to `main` that touches a root `*.md`, `scripts/epub`, `scripts/epub.css` or the workflow itself:

1. installs Pandoc 3.10.1 (the release `.deb`), epubcheck 5.4.0 (the release zip, run through a small wrapper), PyYAML and Pillow 11.3.0;
2. runs `scripts/epub --all`, which fails the job if any EPUB has an epubcheck error;
3. commits the changed `downloads/` files as `EPUB: rebuild from source [skip ci]` and pushes to `main`. If nothing changed, it stops without a commit.

It cannot loop: a push made with the workflow's token starts no other workflow, and the commit touches only `downloads/`, which the paths filter leaves out. If `main` moves while it runs, the push is rejected and the job drops its commit, resets to the new `main`, rebuilds and tries again (three attempts).

Every push to `main` that changes an edition therefore ends with the EPUB rebuilt and committed. Look at a run with `gh run list --workflow=epub.yml` and `gh run view <id> --log`.

**No git hook.** A local hook would run only on machines that have it installed; the Action runs on every push. Add a hook only if the Action is ever unavailable.

## Editing the look

Change `scripts/epub.css`, then either run `scripts/epub --all` locally or push: the Action rebuilds. The stylesheet is one file with a comment at the top saying which classes exist.

## Limits and open items

- Checked with epubcheck 5.4.0 (0 errors, 0 warnings for all nine). The pages have been looked at only in headless Chrome with the EPUB stylesheet (600×900: cover, title page, verse, prose, notes, the Mumonkan's Chinese), not in a reading system: Apple Books cannot be screenshotted from an agent on this Mac (no Screen Recording permission). Looking in Apple Books is bead sutras-m2v.6.6, for Rufus.
- **New markup on edition pages needs a line in `to_book()`**, or it may break the build (lesson 2026-11-21-new-page-markup-breaks-the-epub).
- Mumonkan's "Online" line says "stanza", because its cases are verse blocks; the frontmatter should say `passageUnit: case` (a bead for its track).
- Pandoc's footnote numbers restart in each chapter file; the pop-up shows the note whatever its number.
- Apple Books screenshots were not taken (see the epub track's bead comment for what was blocked).
