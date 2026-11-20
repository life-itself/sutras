# Coordination — brief

Status: draft, 2026-11-20. Part of [workstreams](../2026-11-20-workstreams.md).

## Goal

Agents keep building editions and the site while Rufus is mostly away, without surprising him and without losing what is learned.

## How work runs

A shrunken version of the Reports That Matter protocol (`~/src/reportsthatmatter/reportsthatmatter/docs/agent-protocol.md`):

- **One coordinator session** plans, briefs workers, reviews and merges. **Workers** (subagents) each take one bead, work in their own git worktree and branch, and never merge or publish.
- **Beads is the state.** One epic per workstream, tasks ordered with `bd dep`. A worker writes what it did on its bead. Questions for Rufus are beads labelled `needs-rufus`, each with a recommendation and the default that will be taken if he is silent.
- **`main` is the live site** (Flowershow publishes from GitHub). Under decision D2 the coordinator may merge and push to `main`; this is written into `AGENTS.md` once signed off. Checks must pass before any merge. What D2 holds back goes to the preview site (`fl`, a separate Flowershow site) and waits.
- **Undoing:** if something wrong goes live, revert the commit and push first, then fix on a branch.
- **Limits:** no new accounts or paid services, no spending, and no edits to other repos (wilber-wiki, ux-patterns, planning, Flowershow) without Rufus's OK. Needs in those repos are filed as `needs-rufus` beads here.
- **Decisions** get one short file each in `docs/decisions/` (`NNNN-title.md`: decision, why, date, who). **Lessons** get one file each in `docs/lessons/`. Not settled in chat, not appended to shared files.
- **Critique before showing:** any substantial draft (an intro, a design page, a plan) is critiqued by a fresh subagent before Rufus sees it.
- **Who starts the work:** sessions run when Rufus starts or resumes one; nothing here runs on a schedule. (A scheduled daily run is possible later if he wants it.) Each session begins with `git pull`, `bd ready` and the open `needs-rufus` beads, and ends with a report that lists those beads.
- **Silence:** a `needs-rufus` default on something small and easy to undo is taken after two days. Anything D2 holds back waits.
- **Status:** when Rufus asks "where are we?", use the `project-status-report` skill. At the end of a session, use `close-out`.

## Fit with the sister projects

- **wilber-wiki** already has: verified quotes (`skills/add-excerpt-page/scripts/verify_quotes.py`), a margin-notes prototype (`docs/annotation-system.md`, `annotator.js`), source texts in an unpublished `library/`. Sutras takes these as starting points and gives back a notes script both can share.
- **Open Literature / Unified Text** (`~/src/rufuspollock/planning/initiatives/`) are stubs. Sutras is their first experiment. What it should hand them: an edition template, a passage-link scheme, an annotation approach, and a list of what was hard. Written as lessons here; a one-line pointer is added to the planning files at each milestone.
- **Reports That Matter** is the source of patterns (passage ids, introductions, editor's highlights, approved-on-ship), taken at a fraction of the size.

## Done-check

- A new agent can start from `AGENTS.md` and `bd ready` and know what to do and what it may not do.
- Nothing has gone live that D2 doesn't cover.
- Each milestone ends with a status report and the lessons written down.

## First steps

Create one child epic per workstream under the existing epic (sutras-m2v) with its first tasks; add the working rules to `AGENTS.md` (short, linking here); add `docs/decisions/` with D1–D11 as signed off.
