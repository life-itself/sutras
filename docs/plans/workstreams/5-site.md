# 5 Site — brief

Status: draft, 2026-11-20. Part of [workstreams](../2026-11-20-workstreams.md).

## Goal

The place editions live: one reading page template that every text uses, a home page, passage links, downloads, checks, and a preview. As little machinery as does the job.

## Scope

- **Reading page:** the reading system on Flowershow (`layout: plain`, `custom.css`, a page script), with a verse style, passage link targets that land clear of the navbar, and margin notes. First proven in the [Faith in Mind spike](../2026-11-20-faith-in-mind-spike.md).
- **Home and the rest:** home page (texts grouped, one line each), an about page from the vision, nav, footer, site title and description in `config.json`.
- **Layout of the repo:** texts stay at the root (D9); `library/` (sources, unpublished), `annotations/` or similar (notes data), `downloads/` (EPUBs), `scripts/`, `js/` and `css/`. `contentExclude` kept right as folders are added.
- **Scripts (all owned here):** `scripts/epub` in milestone 1; from milestone 2, `scripts/check` (the checks workstream 2 lists, plus the verbatim-quote check from 3 and 6) and `scripts/notes`, which turns each text's notes file into a small generated script file that the page loads as a page script (Flowershow has no build step and a page cannot fetch a data file, so the generated file is committed). Plain scripts run by agents before merging; a GitHub Action only if something slips through.
- **Preview:** a separate Flowershow site published with `fl` from a small folder, for anything visual before it goes live.

Not in scope: the look (4), the notes model (6), search, accounts, a custom app.

## Stay-or-leave rule for Flowershow

Stay if, after a day's effort on *Faith in Mind*, the spike plan's pass/fail done-check passes. Whatever fails is listed, and only that list argues for anything else. If we ever do leave, the texts are plain Markdown and move unchanged.

## Known Flowershow facts to design around

- Page scripts and custom head code need Premium (Rufus has it); a new preview site must be set to Premium too.
- Page scripts are classic scripts, re-run on every in-site navigation, and must clean up on `flowershow:page-leave`.
- Repo files are served by redirect without CORS headers (flowershow#1373), so a page cannot fetch its notes file: notes data must be put into the page at build time.
- `fl` does not honour `contentExclude`: publish previews from a folder holding only what should go up.
- Raw HTML in Markdown needs blank lines round the Markdown inside it.
- Rufus controls Flowershow: a real gap can be raised there rather than worked round.

## Borrow

- The reading system and its Flowershow notes (`~/src/rufuspollock/ux-patterns/reading-system/README.md`).
- wilber-wiki's `config.json` (nav, footer) and its `annotator.js` loading.
- Reports That Matter's passage URL thinking, but only the simple half: an id in the fragment (`/faith-in-mind#s3`). Quote-level links and link previews are parked.

## Done-check

- Milestone 1: the *Faith in Mind* done-check in the spike plan passes, and the stay-or-leave decision is recorded.
- Milestone 2: home, about, nav and footer live (after Rufus has seen the preview); every edition uses the same page template; `scripts/check` and `scripts/epub` run clean on all texts.
