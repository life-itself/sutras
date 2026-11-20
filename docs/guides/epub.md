# EPUBs

Status: v1, 2026-11-20. Track `epub` (bead sutras-m2v.8.3). Every published edition has a plain EPUB at `downloads/<slug>.epub`, linked from its page as Download. This guide says how they are made and how they stay current.

## How it works

`scripts/epub` (Python, with Pandoc) reads the same `<slug>.md` the site publishes and writes the EPUB:

- **Text:** the web layout (header, contents rail) is dropped; verse (`rs-verse`) and prose (`rs-passages`, `rs-gatha`) become Pandoc containers; passage numbers become spans that links point at (`#s4.3`); linkable headings and contents lists become Markdown links, so they reach the file that holds their target.
- **Structure:** one file per chapter. Level-3 headings split the text where the text has them (Dhammapada, Seneca, the Mumonkan's cases); otherwise level 2 (Meditations' books, the Diamond sutras, Faith in Mind, Shodoka). The contents list is generated from the same headings.
- **Metadata:** title; creator is the author without the bracketed dates and notes (the frontmatter keeps them); translator is a contributor with role `trl`; language `en-GB`; rights from the licence line; source; subject from `tradition`; publisher is the site. The identifier is a UUID made from the site address and the slug, so it never changes.
- **Date:** dc:date and the zip timestamps come from the source's last commit, not the clock. An unchanged source gives a byte-identical EPUB; a rebuild on another machine gives the same file.
- **Cover:** a typographic SVG made from the title and author (no picture). It is generated, so the title and author in the cover are the frontmatter's.
- **Style:** `scripts/epub.css`, deliberately small. Verse lines break with `<br />`, stanza numbers sit on their own line, prose passages and original-language text (`p.orig`, Chinese) are set quieter, notes are EPUB pop-up notes (`aside epub:type="footnote"`).
- **Check:** if `epubcheck` is on the PATH, every EPUB is validated and the build fails on errors.

The output is committed because Flowershow has no build step: the site serves whatever is in the repo.

## Rebuild

```sh
scripts/epub --all                 # every edition with status: published
scripts/epub seneca-on-the-shortness-of-life   # one edition
```

Needs `pandoc` (3.10.1 is what the Action uses; output can differ between Pandoc versions), `pyyaml`, and `epubcheck` (`brew install epubcheck` on the Mac). Then commit the changed `downloads/` files with the change to the source.

## The Action

`.github/workflows/epub.yml` runs on a push to `main` that touches a root `*.md`, `scripts/epub`, `scripts/epub.css` or the workflow itself:

1. installs Pandoc 3.10.1 (the release `.deb`), epubcheck 5.4.0 (the release zip, run through a small wrapper) and PyYAML;
2. runs `scripts/epub --all`, which fails the job if any EPUB has an epubcheck error;
3. commits the changed `downloads/` files as `EPUB: rebuild from source [skip ci]` and pushes to `main`. If nothing changed, it stops without a commit.

It cannot loop: a push made with the workflow's token starts no other workflow, and the commit touches only `downloads/`, which the paths filter leaves out. If `main` moves while it runs, the push is rejected and the job drops its commit, resets to the new `main`, rebuilds and tries again (three attempts).

Every push to `main` that changes an edition therefore ends with the EPUB rebuilt and committed. Look at a run with `gh run list --workflow=epub.yml` and `gh run view <id> --log`.

**No git hook.** A local hook would run only on machines that have it installed; the Action runs on every push. Add a hook only if the Action is ever unavailable.

## Editing the look

Change `scripts/epub.css`, then either run `scripts/epub --all` locally or push: the Action rebuilds. The stylesheet is one file with a comment at the top saying which classes exist.

## Limits and open items

- Checked with epubcheck 5.4.0 (0 errors, 0 warnings for all eight). Not yet checked on a phone reader.
- Mumonkan's "Online" line says "stanza", because its cases are verse blocks; the frontmatter should say `passageUnit: case` (a bead for its track).
- Pandoc's footnote numbers restart in each chapter file; the pop-up shows the note whatever its number.
- Apple Books screenshots were not taken (see the epub track's bead comment for what was blocked).
