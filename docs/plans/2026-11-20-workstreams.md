# Sutras — workstreams and plan of work

Status: draft for sign-off, 2026-11-20. Built on [vision](../vision.md), [brand](../brand.md) and the [SCQ](2026-11-20-sutras-scq.md). Each workstream has a brief in [workstreams/](workstreams/). Tasks live in Beads, not here.

## The shape

Sutras is a small factory with one product: **an edition** (a text, cleaned, introduced, annotated, linkable, downloadable). Six workstreams make editions and the place they live. A seventh thing, coordination, is how the work is run.

| # | Workstream | Question it answers | Brief |
|---|---|---|---|
| 1 | Library | Which texts, which translation, from where, under what licence? | [1-library](workstreams/1-library.md) |
| 2 | Editions | How does a source become a clean text with stable passage links? | [2-editions](workstreams/2-editions.md) |
| 3 | Editorial | What goes round the text (intro, reading guide, highlights), and how does it ship? | [3-editorial](workstreams/3-editorial.md) |
| 4 | Design | What does it look and feel like? | [4-design](workstreams/4-design.md) |
| 5 | Site | Where do editions live: pages, home, links, downloads, checks, preview? | [5-site](workstreams/5-site.md) |
| 6 | Annotation | How do Rufus's notes, and later other readers' notes, live with the text? | [6-annotation](workstreams/6-annotation.md) |
| — | Coordination | How do agents work without Rufus, and how does this feed wilber-wiki and Open Literature? | [0-coordination](workstreams/0-coordination.md) |

How they fit:

```
1 Library ──▶ 2 Editions ──▶ 3 Editorial ──▶ live edition
 (which text)   (clean text,    (intro, highlights,
                 passage ids)    ship)
                     │                ▲
                     ▼                │
              6 Annotation ───────────┤   (notes anchor to passage ids and quotes)
                                      │
4 Design ──▶ 5 Site ──────────────────┘   (the page every edition is poured into)
```

- 1 → 2 → 3 is a pipeline: each text moves through it. Once the first text has been through, texts can go through in parallel.
- 4 Design runs on its own track. Until a direction is chosen, the site uses the reading system's `personal` theme as a stand-in.
- 5 Site and 6 Annotation are built once, then improved. Both are first proven on one text.
- Parked (no workstream yet): concept wiki, side-by-side translations, a new name, PDF. Each stays an idea in the SCQ until editions are flowing.

## Plan of work

**Milestone 1 — one text, end to end (target: live Monday 2026-11-23).** *Faith in Mind* is made into a full edition exactly as in the [Faith in Mind spike](2026-11-20-faith-in-mind-spike.md) plan: its five beads are the milestone. Notes are Markdown footnotes shown in the margin, which already works; no new scripts beyond the EPUB one. If Rufus has not added a note of his own by Monday, it ships with the editorial glosses and his notes follow. In parallel, with no dependency on it: the Library shortlist (1), the Design brief, feel and mood board (4), and the reader-annotation options paper (6).

**Milestone 2 — the six existing texts as editions (target: week of 2026-11-30).** What milestone 1 taught is written down as a short guide and a check script, then applied to Shodoka, the two Diamond Sutras, the Mumonkan and Seneca, one agent per text. Notes move from footnotes to the notes file (D3), built and proven on *Faith in Mind* and Seneca. A plain home page (texts grouped, one line each), about page, nav and footer. A Hypothesis trial on the preview site, so Rufus can feel reader annotation early. The design page is ready for Rufus to pick a direction; until he does, the stand-in stays.

**Milestone 3 — new texts and the chosen design (December).** First three new texts from the shortlist go through the whole pipeline. The chosen design goes live. Owner note capture in the browser (select, write, export) if Rufus finds editing files a drag.

**Milestone 4 — reader annotation (after the above; January).** A time-boxed prototype of our own small notes service, set beside the Hypothesis trial from milestone 2; then Rufus decides. Lessons written up for wilber-wiki and Open Literature.

Milestones 1 and 2 are KISS on purpose: Flowershow, Markdown, two small scripts. Anything heavier has to earn its place by a failure we actually hit.

## Decisions to sign off now

Rufus will be less available, so these are proposed as defaults. Each stands unless he says otherwise; the three marked **ask** are the ones worth his attention.

| # | Decision | Proposed default |
|---|---|---|
| D1 | Platform | Stay on Flowershow. Leave only if the Faith in Mind spike fails its stay-or-leave rule. |
| D2 | **ask** — What may go live without asking | Agents may merge and push to `main` (which is the live site). Edition pages (text, intro, notes, EPUB) in the stand-in reading theme go live once checks pass; Rufus reviews them live and anything he flags is fixed first. So may a plain home page, about page, nav and footer. A new look, a new name, or anything reader-facing beyond that goes to the preview site and waits for him, with no time limit. |
| D3 | **ask** — Rufus's notes format (direction; built in milestone 2) | Notes are data: one file per text, each entry a quoted passage plus an optional comment. Shown as a highlight with a margin note. Same shape as wilber-wiki's prototype and as a reader's annotation later. Translators' own footnotes stay footnotes. |
| D4 | **ask** — First new texts, and publishing in-copyright translations in full | Heart Sutra, Tao Te Ching, Marcus Aurelius's *Meditations* (the vision names the last two). Per the vision, not gated on permission: where the best translation is in copyright, agents publish it in full, on the page and in the EPUB, with source and status stated plainly. This covers Sheng-yen's *Faith in Mind* now. Backup: full text only for public-domain translations, samples for the rest, until Rufus OKs each text. |
| D5 | Unpublished sources | Yogins of Ladakh and all source files stay in an excluded `library/` folder. |
| D6 | Passage links | The id is the number a reader would cite, levels joined by dots: `/meditations#4.3`, `/tao-te-ching#11`, `/gateless-gate-mumonkan#1`. Texts with no traditional numbering get stanza or paragraph numbers (`/faith-in-mind#3`). One page per text, always, so a passage link never moves. An id never changes once published; a check enforces it from milestone 2. |
| D7 | Reader annotation | Hypothesis trial in milestone 2 (preview site only); our own prototype in milestone 4; decided by Rufus on the two, not in the abstract. Invite-only when it comes. A small notes service is not the "custom reading platform" the SCQ rules out (as a guess): the texts stay on Flowershow. |
| D8 | Design gates | Feel, mood board and directions are shown together on one page with a recommendation, so Rufus chooses once. Until he does, nothing visual beyond the stand-in goes live. |
| D9 | URLs and layout | Texts keep their current URLs (`/faith-in-mind`). Supporting files go in folders. No move to `texts/` until there are a dozen texts. The partial Red Pine Diamond Sutra stays, marked as partial. |
| D10 | Name | "Sutras" stays for now. Renaming is parked, and so is a logo or wordmark. |
| D11 | Reuse | Anything general (edition checks, the notes script, the reading setup) starts in this repo and is extracted only when wilber-wiki or another project actually uses it. |

## What Rufus is needed for

1. Now: OK this plan and D2, D3, D4.
2. Around Sunday 2026-11-22: read *Faith in Mind* on the preview, add a note or two.
3. Once, when the design page is ready: pick a direction.
4. Later: the reader-annotation decision after the prototypes.

Everything else runs without him. Questions that come up are filed as Beads labelled `needs-rufus` with a recommendation and a default. A default on something small and easy to undo is taken after two days of silence; anything D2 holds back waits for him however long. Open questions are listed at the end of every report to him. See [coordination](workstreams/0-coordination.md).
