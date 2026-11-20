# 4 Design — brief

Status: draft, 2026-11-20. Part of [workstreams](../2026-11-20-workstreams.md). Bead: sutras-m2v.3 (mood board and design directions). Process: the `designing-look-and-feel` skill; this file is its stage-1 brief and is to be critiqued and reviewed before any mockup.

## Goal

A look and feel for Sutras that is the thing it shows: "we want to *be* zen, to be the tao somehow in what we are building" (Rufus, in [brand](../../brand.md)). The text is the design.

## Who and what for

- Rufus reading slowly, on a phone as much as a laptop (guess), sometimes for an hour.
- A stranger arriving from a search for a text, who should feel within seconds that this is a good place to read it.

Kinds of page, and what each needs:

| Page | Needs |
|---|---|
| Reading page (verse) | Line breaks kept, generous space, stanza numbers barely there, notes beside the lines |
| Reading page (prose, e.g. Seneca) | A comfortable measure, chapters, footnotes |
| Reading page (cases, e.g. Mumonkan) | Case, comment and verse told apart; Chinese characters set well |
| Home | A contemplative front door on an orderly list |
| Text front matter | Title, author, translator, in brief, introduction |
| Notes and highlights | Rufus's hand visible but quiet; clearly not part of the text |

## Fixed

- Flowershow, with the reading system (`~/src/rufuspollock/ux-patterns/reading-system`) as the base to restyle, not replace.
- Light only for now. Serif body. Free fonts.
- Direction given by Rufus: stripped down; Reports That Matter and Co–Star as references "but a little warmer"; a little Plum Village, though that "can get a little twee". Warm, not cute.

## Stages (from the skill), fitted to Rufus being away

| Stage | Output | Gate |
|---|---|---|
| 0 Feel | One phrase, three notes, "what we are not" | shown with 1 and 2 |
| 1 Research and mood board | Why the admired sites work, measured (type, measure, space, colour), one factor at a time. 6–12 real references with take and leave, 2–3 anti-references, the current site as "before". Boards for parts too: verse setting, margin notes | shown with 0 and 2 |
| 2 Directions | 2–3 specimen cards side by side, each a different reading of the feel, set with real lines from *Faith in Mind*; one recommended | **Rufus picks once (D8)** |
| 3 Mark | Parked with the name (D10). The site title is set in the chosen type | none |
| 4 Build | Chosen direction on the preview site: reading page, home page; then live | Rufus reviews the preview |

All on one living page, republished at the same link. Stages 0–2 are prepared without Rufus and shown together; a critique by a fresh agent comes before he sees it.

## Read first

- `~/src/rufuspollock/ux-patterns`: `reading-system/`, `essay-pages/`, `typography.md`, `signs-of-taste.md`, `how-to-go-beyond-good-average-ai-design.md`.
- Reports That Matter's Co–Star direction: `~/src/reportsthatmatter/reportsthatmatter/docs/design/2026-08-01-costar-direction/README.md` (what worked: one exemplar, measured).
- `docs/2026-11-18-inspirations.md` and `docs/brand.md`.

## Done-check

- Rufus has said "yes, that's us" to a feel and picked a direction.
- The chosen direction is live on the reading page and the home page, and Rufus has read *Faith in Mind* on his phone in it and has no changes he wants before the next text.
- The decisions are written in `docs/design/` so no later agent reopens them.

## Independent of the rest

Design does not block milestones 1 and 2: editions ship in the stand-in theme. It needs only real text to set specimens with, which exists today.
