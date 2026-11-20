# 3 Editorial — brief

Status: draft, 2026-11-20. Part of [workstreams](../2026-11-20-workstreams.md). Bead: sutras-m2v.5 (publish first new text).

## Goal

Put round each text what a reader needs to start and to stay: a short introduction, a way in, a few highlights, and plain facts about the edition. Then ship it.

## What goes round the text

In page order:

1. **In brief:** one or two sentences. What this is and why read it.
2. **Introduction** (150–300 words): who wrote it and when, what it is about, why it has lasted, how to read it (slowly, aloud, a verse a day, with which other text).
3. **The text,** with editor's highlights: 3–8 passages worth stopping at, some with a note. In milestone 1 these are footnotes shown in the margin; from milestone 2 they are entries in the notes file (workstream 6).
4. **About this translation:** the translator, and any preface of theirs, below the text.
5. **Source and licence.**
6. **Download:** EPUB.

A longer text may add a reading guide ("if you read only three chapters"). No summaries that replace reading.

## Voice

From the [brand](../../brand.md): plain, quiet, personal; a reader's notes, not a scholar's apparatus or a teacher's sermon. British spelling. No praise adjectives. Facts (dates, names, attributions) come from a named source, never from memory, and doubtful attributions are said to be doubtful. The introduction is signed as editorial; Rufus's own notes are marked as his.

## Rules that are not negotiable

- **Every quotation is verbatim.** A check fails if a highlighted or quoted passage is not found word for word in the text (wilber-wiki's `verify_quotes.py` logic; Reports That Matter's `pnpm editorial`). Misquoting is the one error that must never ship.
- **AI drafts, and says so.** Introductions are drafted by an agent, critiqued by a second agent, and shipped (D2). Rufus reviews live and edits; his edits are kept as examples for the next one.
- **Text first, introduction second.** Each is a complete release: a clean text can go live before its introduction.

## Borrow

- Reports That Matter: `docs/report-introductions.md` (structure, voice, the verbatim check, approved-on-ship) and editor's highlights (decision 0014 there), at about a quarter of the length.
- Brand voice: `docs/brand.md`. The voice is marked "guess" there; the first two introductions are how it gets tested.

## Publishing

- EPUB per text from the same Markdown with Pandoc, with title, author, translator, source and licence inside (the Site workstream owns the script). Plain styling for now. PDF is parked.
- On publish: `status: published`, passage ids added to `published-ids.txt`, home page list updated, a line in the changelog.

## Done-check

- *Faith in Mind* is live with all six parts, quotes verified, EPUB opening in Apple Books.
- `docs/guides/writing-an-introduction.md` exists, with the *Faith in Mind* introduction as its example.
- Rufus has edited at least one introduction, and the guide reflects what he changed.

## Needs Rufus

- Reading the first two introductions and saying what is off. This sets the voice for the rest.
