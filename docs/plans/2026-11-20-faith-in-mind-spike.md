# Faith in Mind spike — plan

Status: draft, 2026-11-20, awaiting Rufus's OK. Epic: sutras-m2v. Vision: [docs/vision.md](../vision.md). SCQ: [2026-11-20-sutras-scq.md](2026-11-20-sutras-scq.md).

## Goal

Make *Faith in Mind* into one text "done well", and so answer two questions with something to look at rather than argue about:

1. What does a Sutras edition look like (page, notes, links, download)?
2. Can Flowershow do it, or do we need our own site?

KISS, then iterate: use what already exists before building anything.

## Done-check

On a preview site (not the live one), all pass:

- the page has our intro, the poem, About this translation, Source and licence, and a Download link, in that order;
- the reading layout loads: EB Garamond renders and the poem keeps its line breaks;
- `…/faith-in-mind#s3` lands on stanza 3, not hidden under the navbar;
- at least two margin notes sit beside their lines at 1280px wide and open on tap at 390px;
- the EPUB downloads and opens in Apple Books;
- Rufus has added at least one note of his own;
- the stay-or-leave decision on Flowershow is recorded below.

Target: ready for Rufus by Sunday 2026-11-22, so the result can go live by Monday 2026-11-23 (the SCQ date).

## Approach: Flowershow first, with the reading system

The earlier idea of a small custom site (Astro) is dropped for now. Flowershow already has most of what we need:

- **Reading layout:** Rufus's reading system (`~/src/rufuspollock/ux-patterns/reading-system`, v0.1) is one CSS file and one script, already documented for Flowershow (`layout: plain`, page scripts). It does margin notes from Markdown footnotes. Theme: `personal` (EB Garamond), as a stand-in until the moodboard (sutras-m2v.3).
- **Notes:** Markdown footnotes become margin notes. Simple, in the text file, versioned. Rufus writes them himself (or dictates them to an agent). Flowershow's annotations feature is not used: it is a review-comments tool, not a reader's notes on a text.
- **Stanza links:** an inline `<a id="s3"></a>` at the start of each stanza: it keeps the Markdown line breaks and works without JavaScript. Fallback: add the ids in the page script.
- **EPUB:** Pandoc (installed) from the same Markdown, one short script. Committed as a file the page links to.

What Reports That Matter does that we skip: per-text repos, an ingest pipeline, fidelity gates, a custom app and database. Too much for short, already-clean texts. We keep only the ideas: a stable link per passage, a provenance note, a short intro.

## The edition

`faith-in-mind.md` stays at the root so its URL doesn't change. Folder structure for the library is decided later (sutras-m2v.4).

Page order:

1. Title, attribution (Seng Ts'an, trans. Master Sheng-yen), one-line "in brief".
2. A short intro by us: what the poem is, why read it, how to read it (about 150 words, AI-drafted, Rufus edits).
3. The poem, stanzas numbered and linkable, with two or three margin notes (glosses such as "the Supreme Way" = the Tao, marked as editorial) to show the mechanism. Rufus adds his own notes in step 4.
4. About this translation: Sheng-yen's preface and introduction (as now), moved below the poem.
5. Source and licence: where the text comes from, its copyright status (Sheng-yen's translation is in copyright; published under the "not gated on permission" stance in the vision), our additions CC BY 4.0.
6. Download: EPUB.

## Steps (each one a bead, in order)

1. **Edition text:** restructure `faith-in-mind.md` as above; check the poem against the source; stanza ids; intro; glosses; source and licence block.
2. **Reading page:** add `reading.css` and `reading.js` to the repo; `custom.css` with the Google Fonts `@import` first, then the reading CSS; `--rs-sticky-top` set to the navbar height; a small verse style (the reading system is built for prose); the page uses `layout: plain`, the `.rs` wrapper with blank lines around the Markdown inside it, and `reading.js` as a page script.
3. **EPUB:** `scripts/epub.sh` with Pandoc; output to `downloads/faith-in-mind.epub`; link from the page.
4. **Preview and notes:** publish a small folder (the page, `custom.css`, the reading files, the EPUB) to a separate preview site with `fl`, set to Premium so page scripts run, and add `.flowershow` to `.gitignore`; Rufus reads it and adds a few notes of his own (directly, or by telling an agent which line and what).
5. **Decide and ship:** compare preview with live; record the Flowershow decision in this file; merge to `main` so the live site updates.

## Stay-on-Flowershow rule

We stay on Flowershow if all of these work after a day's effort: stanza links, margin notes, the reading layout as good as the reading-system demo, the EPUB link. Anything that fails goes into a short list here, and only that list makes the case for a custom site.

## Out of scope

Other texts, home page redesign, new name, concept wiki, side-by-side translations, PDF, the moodboard. Each has or gets its own bead.

## Risks

- Flowershow strips raw `id`s or fights the reading CSS: fall back to the page script, or note it under the rule above.
- The preview site isn't Premium, so `reading.js` doesn't run and there are no margin notes. Check this first.
- The EPUB carries Sheng-yen's preface, introduction and translation, which is a further step than a web page. Rufus to OK; backup: an EPUB of the poem and our intro only.
- Page script on Flowershow must clean up on `flowershow:page-leave` (reading-system README says so).
- `custom.css` loads on every page; the reading CSS is scoped to `.rs`, so other texts should be unaffected. Check one.
