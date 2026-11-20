# 4 Design — brief

Status: draft 3, 2026-11-20. The first design page built from draft 2 was rejected by Rufus ("mood board is weak. where is the true beauty in this… start with clear brief and moodboard"); the restart is in `docs/design/brief.md` (the brief) and the mood board page. Rufus also asked (same day) for at most 5–10 directions on the board, a few details and a shortlist of 3–4, and for Seeds of Renaissance, adapted, as one direction. This file keeps the fuller specification for the specimen and build stages; where it differs from `docs/design/brief.md`, the brief wins. Part of [workstreams](../2026-11-20-workstreams.md). Bead: sutras-m2v.3 (mood board and design directions). Process: the `designing-look-and-feel` skill; this file is its stage-1 brief. Output of stages 0–2: [docs/design/](../../design/README.md).

## Goal

A look and feel for Sutras that is the thing it shows: "we want to *be* zen, to be the tao somehow in what we are building" (Rufus, in [brand](../../brand.md)). The text is the design.

The bar, in Rufus's words (2026-11-20): Reports That Matter "has a pretty sober version, you could follow that… I think we do want our distinctive design here, and that often takes real work." So **sober is the floor, distinctive is the aim**: a page that is only tasteful and quiet has not met the brief.

## Who and what for

- Rufus reading slowly, on a phone as much as a laptop (guess), sometimes for an hour; and returning to a text he has read before.
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

The verse reading page is the test page: if a direction does not make *Faith in Mind* better to read, it fails, whatever else it does.

## Fixed

- Flowershow, with the reading system (`~/src/rufuspollock/ux-patterns/reading-system`) as the base to restyle, not replace. A direction is a set of tokens (fonts, sizes, colours, spacing) and at most one small custom piece on top of it.
- Light only for now. Serif body. Open-licence fonts (Google Fonts on the design page; self-hosting is fine in the build). The face for Chinese characters is named, not left to the system.
- EPUB: the type choices should carry over to the download where reading apps allow it; styling the EPUB is not part of this pass.
- No logo or wordmark work: the name is parked (decision 10). The site title is set in the chosen type.
- No pictures are assumed. A direction may propose one kind of image (for example a public-domain ink painting per text) but must stand without it.
- Direction given by Rufus: stripped down; Reports That Matter and Co–Star as references "but a little warmer"; "a little more Plum Village", though that "can get a little twee". Warm, not cute.

## Legibility floors (rules) and defaults (a direction may break one if it says why)

Floors:

- Prose: 60–72 characters a line on a laptop, about 35–45 on a phone; line height about 1.5–1.7 (less for a face with a small x-height); body 18–21px on a laptop and no smaller than 17px on a phone.
- Verse: the same size as prose or a step larger; line height about 1.4–1.6; the gap between stanzas about one line. The longest line of *Faith in Mind* is 50 characters ("The erring mind begets tranquillity and confusion;"), which will not fit a 390px phone at 18px, so the turnover is designed: a wrapped line hangs in by about 1.5em, never back to the left edge.
- Notes are told apart from the text by at least two of size, face, colour and position.
- "Better to read" is judged against the current site at 390px wide.

Defaults (break with a reason): stanzas separated by space, not rules; numbers small and grey in the margin; notes in the margin on wide screens and opened in place on a phone; at most three colours, the accent with one job; no boxes.

## What forces the directions apart

Three poles, each a different reading of "be zen" and a different source of warmth:

| Pole | Reads zen as | Warmth comes from | Measured exemplar |
|---|---|---|---|
| Austere | emptiness: take away until only the text is left | the ground and the wording | Co–Star, Reports That Matter |
| The warm hand | intimacy: someone has read this before you | the reader's notes | Plum Village with the twee removed; a read paperback |
| The inherited book | lineage: the forms these texts were handed down in | the page's own conventions (red and black, the block) | printed sutra books, rubricated pages, fine-press poetry |

The directions must differ on at least three of: composition (where the column sits), type voice, where the notes live, how a highlight is shown, how hierarchy is made. Each names its principle and its one source of warmth. One direction may break a Fixed rule or default as a wildcard, and says so.

## Habits to name and avoid

Generic AI-site habits: cream ground with a terracotta accent and a serif headline; tracked-caps eyebrows over every heading; an italic accent word in each headline; triads of cards; identical section rhythm; rounded cards with soft shadows; everything centred. Spiritual-site habits: lotus and ensō clip art, brush-script fonts, sage-green and sand "wellness" palettes, stock photos of stones and mist, gradient skies. And the likeliest dull result of this very brief: a Garamond-like serif on off-white with grey numerals, which is Tufte CSS or Standard Ebooks again.

## Stages (from the skill), fitted to Rufus being away

| Stage | Output | Gate |
|---|---|---|
| 0 Feel | Two or three candidate phrases, one recommended; three notes; character; "what we are not" | shown with 1 and 2 |
| 1 Research and mood board | Why the admired sites work, measured (type, size, measure, line height, space, colour), one factor at a time. 6–12 real references with take and leave, 2–3 anti-references, the current site as "before". Boards for parts too: verse setting, margin notes | shown with 0 and 2 |
| 2 Directions | 2–3 specimen cards side by side, each a different reading of the feel, set with real lines from *Faith in Mind*; one recommended | **Rufus picks once (D8)** |
| 3 Mark | Parked with the name (D10) | none |
| 4 Build | Chosen direction on the live site (decision 2: the live site is its own preview): reading page, home page | Rufus reviews it live |

Each specimen card shows, at phone width: site title, nav line, a text's title block, an "in brief" line, a verse block with a stanza number and one note, hex swatches, the type pairing, and one named signature element; underneath, says / risk / draws on. The same stanza is then shown at desk width with its margin note, and a few lines of Seneca to test prose.

All on one living page (`docs/design/brief.html`, published as an artifact and republished at the same link). Stages 0–2 are prepared without Rufus and shown together; a critique by a fresh agent comes before he sees it.

## Read first

- `~/src/rufuspollock/ux-patterns`: `reading-system/`, `essay-pages/`, `typography.md`, `signs-of-taste.md`, `how-to-go-beyond-good-average-ai-design.md`, `howto-moodboards.md`.
- Reports That Matter's Co–Star direction: `~/src/reportsthatmatter/reportsthatmatter/docs/design/2026-08-01-costar-direction/README.md` (what worked: one exemplar, measured).
- `docs/2026-11-18-inspirations.md` and `docs/brand.md`.

## Done-check

For this pass (stages 0–2):

- The living page exists at one link, with feel, measured research, mood board (real screenshots only), 2–3 directions and decisions, each decision with a recommendation.
- A reviewer who has not seen the work can say in a sentence how each direction differs from the others without naming a colour or a typeface, and can still tell them apart in greyscale.
- With the site title covered, no direction would be mistaken for Tufte CSS, Standard Ebooks or a Substack post.
- Each direction shows the first screen of *Faith in Mind* at phone width and the same stanza at desk width with a margin note. (A Mumonkan case and the home list are left to stage 4, on the chosen direction.)
- The page and `docs/design/README.md` are committed.

For the workstream:

- Rufus has said "yes, that's us" to a feel and picked a direction (or a blend).
- The chosen direction is live on the reading page and the home page, and Rufus has read *Faith in Mind* on his phone in it and has no changes he wants before the next text.
- The decisions are written in `docs/design/` so no later agent reopens them.

## Independent of the rest

Design does not block milestones 1 and 2: editions ship in the stand-in theme. It needs only real text to set specimens with, which exists today.
