# AGENTS.md

## What this project is

Sutras (sutras.lifeitself.org) — a library of wisdom teachings, published with Flowershow. Being re-visioned from November 2026: see `docs/vision.md` (purpose, audience, what it is not), `docs/brand.md`, the open epic in Beads (`bd list`) and `docs/2026-11-18-current-state.md`. Sister project and pattern reference: `life-itself/wilber-wiki`.

## How we work

Start with `git pull` and `bd ready`. The map of the work is `docs/plans/2026-11-20-workstreams.md`, with a brief per workstream in `docs/plans/workstreams/`; decisions are in `docs/decisions/`, lessons in `docs/lessons/` (one file each).

- **Don't block on Rufus.** Draft, have a subagent (or Codex) critique it, integrate, build, keep going. Make a judgement call on anything that can be undone. Questions only he can answer go in a bead labelled `needs-rufus`, with a recommendation and the default you are taking.
- **`main` is the live site and you may push to it.** Nobody depends on the site yet, so anything on it may change (decision 0001). If something breaks, revert and push, then fix.
- **Design needs Rufus's taste.** Have a go, and show him the design page early. Use the `designing-look-and-feel` skill.
- **Limits:** no new paid services or spending; no edits to other repos (wilber-wiki, ux-patterns, planning, Flowershow) without Rufus's OK.
- Parallel workers use their own git worktree; the coordinator merges.

## Work tracking

Use Beads (`bd`) for all tasks; no TODO lists in Markdown. `git push` also pushes Beads (pre-push hook runs `bd dolt push`).

## Publishing

`README.md` is the home page. `config.json` `contentExclude` keeps `docs/`, `.beads/`, `AGENTS.md` and `CLAUDE.md` off the live site. Don't publish new top-level folders without checking that list. `yogins-of-ladakh.md` is an untracked source dump with unclear copyright: don't commit or publish it.

## Docs

`docs/` holds analyses and references (dated `YYYY-MM-DD-<topic>.md`); `docs/plans/` holds plans and vision docs. Not published. Don't use a `notes/` folder.
