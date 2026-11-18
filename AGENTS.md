# AGENTS.md

## What this project is

Sutras (sutras.lifeitself.org) — a library of wisdom teachings, published with Flowershow. Being re-visioned from November 2026: see the open epic in Beads (`bd list`) and `notes/2026-11-18-current-state.md`. Sister project and pattern reference: `life-itself/wilber-wiki`.

## Work tracking

Use Beads (`bd`) for all tasks; no TODO lists in Markdown. `git push` also pushes Beads (pre-push hook runs `bd dolt push`).

## Publishing

`README.md` is the home page. `config.json` `contentExclude` keeps `notes/`, `.beads/`, `AGENTS.md` and `CLAUDE.md` off the live site. Don't publish new top-level folders without checking that list. `yogins-of-ladakh.md` is an untracked source dump with unclear copyright: don't commit or publish it.
