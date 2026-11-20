# Faith in Mind spike — plan

Status: OK'd by Rufus to go ahead, 2026-11-20. Milestone 1 of the [workstreams plan](2026-11-20-workstreams.md). Epic: sutras-m2v. Vision: [docs/vision.md](../vision.md). SCQ: [2026-11-20-sutras-scq.md](2026-11-20-sutras-scq.md).

## Goal

Make *Faith in Mind* into one text "done well", and so answer two questions with something to look at rather than argue about:

1. What does a Sutras edition look like (page, notes, links, download)?
2. Can Flowershow do it, or do we need our own site?

KISS, then iterate: use what already exists before building anything.

## Done-check

On a preview site (not the live one), all pass:

- the page has our intro, the poem, About this translation, Source and licence, and a Download link, in that order;
- the reading layout loads: EB Garamond renders and the poem keeps its line breaks;
- `…/faith-in-mind#3` lands on stanza 3, not hidden under the navbar;
- at least two margin notes sit beside their lines at 1280px wide and open on tap at 390px;
- the EPUB downloads and opens in Apple Books;
- Rufus has added at least one note of his own (if he hasn't by Monday, it ships with the editorial glosses and his notes follow);
- the stay-or-leave decision on Flowershow is recorded below.

Target: ready for Rufus by Sunday 2026-11-22, so the result can go live by Monday 2026-11-23 (the SCQ date).

## Approach: Flowershow first, with the reading system

The earlier idea of a small custom site (Astro) is dropped for now. Flowershow already has most of what we need:

- **Reading layout:** Rufus's reading system (`~/src/rufuspollock/ux-patterns/reading-system`, v0.1) is one CSS file and one script, already documented for Flowershow (`layout: plain`, page scripts). It does margin notes from Markdown footnotes. Theme: `personal` (EB Garamond), as a stand-in until the moodboard (sutras-m2v.3).
- **Notes:** Markdown footnotes become margin notes. Simple, in the text file, versioned. Rufus writes them himself (or dictates them to an agent). Flowershow's annotations feature is not used: it is a review-comments tool, not a reader's notes on a text.
- **Stanza links:** an inline `<a id="3"></a>` at the start of each stanza: it keeps the Markdown line breaks and works without JavaScript. Fallback: add the ids in the page script.
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

## Result (2026-11-20)

**Decision: stay on Flowershow.** Every item of the stay-or-leave rule works on the live site after about half a day, with small work-rounds and nothing Flowershow could not do. Built by an AI agent (Claude); checked on https://sutras.lifeitself.org/faith-in-mind with headless Chrome at 1280px and 390px.

Changes to this plan as built (decision 0001 and the coordinator's brief): no preview site, `main` is the preview; stanza ids are plain numbers (`#3`); the EPUB carries the full text.

### Done-check

| Item | Result | Evidence |
| --- | --- | --- |
| Intro, poem, About this translation, Source and licence, Download, in that order | Pass | Headings on the live page, in order: In brief, Introduction, The poem, About this translation, Source and licence, Download |
| Reading layout loads: EB Garamond renders, poem keeps its line breaks | Pass | `document.fonts` reports EB Garamond loaded and it is the computed font; 146 lines in the source, 146 rendered (15 stanzas) |
| `/faith-in-mind#3` lands on stanza 3, clear of the navbar | Pass | Stanza 3's number sits 84px from the top of the window at both widths, 20px below the 64px navbar (added by the Site work during the spike; the offset uses Flowershow's `--navbar-height`) |
| Two or more margin notes beside their lines at 1280px; open on tap at 390px | Pass | Three notes, each 220px wide in the right margin, level with its line; at 390px hidden until tapped, then open under the line |
| EPUB downloads and opens in Apple Books | Part | Downloads from the page link as `application/epub+zip`, identical to the committed file; valid container, well-formed XHTML, reads back through Pandoc. **Not opened in Apple Books by the agent**: Rufus to open it once |
| Rufus's own note | Not done (left out of this pass) | Follows with notes as data, milestone 2 |
| Stay-or-leave recorded | Pass | This section |

Also checked: going to the page from the home page and back and forward again re-runs the page scripts cleanly (three notes each time, no console errors); the home page and `/shodoka` look as before; `library/`, `scripts/` and `docs/` return 404 on the live site.

### What Flowershow needed (work-rounds, none blocking)

1. The site parses `.md` as MDX, so the first push showed an error card. Fixed with `syntaxMode: md` on the page.
2. Footnotes are rendered outside the page's wrapper, so the reading system did not find them. Two-line change in our copy of `reading.js`, one rule in `custom.css`.
3. `reading.js` was not written as a page script (no clean-up on leaving the page). Patched in our copy.
4. A passage link is scrolled to before the font loads; `js/edition.js` scrolls again.
5. Verse needed its own small style, and the note number a real tap target on phones.

Each is written up in `docs/lessons/`. Things that simply worked: raw `id`s on inline anchors, `layout: plain`, page scripts (including on in-site navigation), `@import` of Google Fonts and of a CSS file in the repo from `custom.css`, `.epub` served as a download, `contentExclude`.

A second agent critiqued the introduction and the live page; its points were applied (introduction keeps to what Sheng-yen reports and quotes; shorter source note; no small-caps first lines or automatic hyphenation; the empty band under the page removed). Not applied: a hanging indent for wrapped verse lines (not possible with `<br>` line breaks) and more notes on terms (Rufus's notes come in milestone 2).

### What Flowershow cannot do (the list that would argue for leaving)

Nothing found in this spike. Known limits to design round, not hit here: no build step (the EPUB and any generated file are committed), and a page cannot fetch a data file from the repo (matters for notes as data, milestone 2).

### Left for others

- Flowershow's default footer line, "© 2026 Sutras. All rights reserved.", contradicts the page's licence. `custom.css` hides `.site-footer-copyright` on every page; the Site workstream should write the real line (or a `_footer.html`).
- The licence paragraph sends rights holders to GitHub issues. An email address would be better; Rufus to say which.
- `"syntaxMode": "md"` site-wide in `config.json` would remove work-round 1 for every edition (Site workstream; check no page needs MDX).
- The five reading-system changes should go upstream (needs Rufus's OK to edit `ux-patterns`).
- `scripts/compare-source` is written for this one text; generalise with the second edition (workstream 2).
