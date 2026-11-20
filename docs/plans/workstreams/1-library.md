# 1 Library — brief

Status: draft, 2026-11-20. Part of [workstreams](../2026-11-20-workstreams.md). Bead: sutras-m2v.4 (structure, shortlist, cadence).

## Goal

A curated shortlist of texts worth making, each with a chosen translation, a source we can get, and a plain statement of its copyright status. Curated, not complete.

## Scope

- **Shortlist:** 15–20 candidates across the traditions the vision names (Buddhist and Zen, Stoic, Taoist), in a rough order, each with one line on why it is here. Rufus's taste decides; the agent proposes.
- **Per text, a source record:** title, author, date; candidate translations with a recommendation (readability first, then licence); where the text can be had (URL, book, EPUB); copyright status of the translation; the traditional way it is cited (chapters, verses, cases).
- **Acquisition:** fetch or convert the chosen source into `library/<slug>/` (unpublished, excluded from the site), with the source URL and date recorded. EPUB and PDF sources convert with the tools in `~/src/life-itself/library` (`books-for-bots`); web sources are saved as fetched.
- **Cadence:** a proposed rhythm (guess: one new text a week once the pipeline works).

Not in scope: cleaning the text (2), writing about it (3), a complete catalogue.

## Borrow

- Reports That Matter's source checklist, shrunk: `~/src/reportsthatmatter/reportsthatmatter/.claude/skills/report-source/SKILL.md` (pick the best original, record where it came from, compare against another edition).
- wilber-wiki's edition-choice note: `~/src/life-itself/library/docs/plans/2026-09-18-wilber-source-acquisition.md`.
- Reference sites for what exists: terebess.hu, SuttaCentral, Standard Ebooks, Project Gutenberg, Access to Insight (see `docs/2026-11-18-inspirations.md`).

## Decided by default

- First new texts: Heart Sutra, Tao Te Ching, *Meditations* (D4).
- Not gated on permission; status always stated (D5).
- Where a good public-domain or freely licensed translation exists and reads well, prefer it; where the best translation is in copyright, say so and recommend anyway.

## Needs Rufus

- The shortlist itself: he adds, cuts and reorders. Asked once, as one page.
- The Red Pine Diamond Sutra looks partial: complete it or leave it (default: keep it, marked as partial, and look for the full text).

## Done-check

- `docs/library-shortlist.md` exists, with a source record per text, and is filed for Rufus as a `needs-rufus` bead. Work on the first three (D4) does not wait for his reply.
- The first three new texts have a chosen translation and a source file in `library/`.
- The six existing texts each have a source record (several lack one today).
