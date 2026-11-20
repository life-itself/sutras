# 6 Annotation — brief

Status: draft, 2026-11-20. Part of [workstreams](../2026-11-20-workstreams.md). This is the workstream Rufus is most interested in, and the one that matters most to wilber-wiki and Open Literature.

## Goal

Rufus's highlights and notes live with the text, look like a reader's marginalia, and survive the text being edited. Later, other readers can add theirs. What we learn is reusable.

What it is not: review comments on a draft (Flowershow's annotations, Google Docs). Rejected by Rufus, 2026-11-20.

## The model (D3)

A note is **a quoted passage plus an optional comment**: `id`, `passage` (the passage id it sits in), `quote` (the exact words), optional `prefix` and `suffix` (to tell repeats apart), optional `note`, `by`, `date`. A highlight is a note with no comment. This is the W3C Web Annotation "text quote" shape, the shape wilber-wiki's prototype already uses, and the shape Reports That Matter anchors highlights with. One file per text, in the repo.

Why data rather than footnotes in the text: the text stays clean; the same shape serves Rufus now and readers later; a check can prove every quote still matches; wilber-wiki can use the same script. Translators' own footnotes remain footnotes.

## Stages

**A0. Footnotes (milestone 1).** For Monday, notes on *Faith in Mind* are Markdown footnotes, which the reading system already shows in the margin. Nothing new is built.

**A. Owner notes as data, shown (milestone 2).** The notes file for *Faith in Mind* (its footnote notes moved over) and for Seneca; our own small script that finds each quote on the page, highlights it and puts the note in the margin. It starts from wilber-wiki's `assets/annotator/annotator.js` (plain JavaScript, no library), and uses the reading system's margin so that a text with both translator's footnotes and Rufus's notes (Seneca has 67 footnotes) shows them in one column, told apart. How the data reaches the page: `scripts/notes` writes a generated script file per text (see the Site brief). The check fails when a quote no longer matches. Rufus adds notes by editing the file or telling an agent "this line, this thought". Recogito's `text-annotator-js`, which wilber-wiki's research favoured, is only needed for selecting text in the page, so it is looked at in stage B, not here.

**B. Owner notes, captured in the page (milestone 3, only if editing files is a drag).** Select text on the page, write a note, it is kept in the browser and exported as entries for the notes file. No server, no accounts. This is Reports That Matter's "local highlights with export" phase.

**C. Reader annotation (Hypothesis trial in milestone 2; our own in milestone 4).** An options paper first (`docs/2026-11-annotation-options.md`, from the research already done), then two time-boxed prototypes on the preview site:

1. *Hypothesis*, clean theme, a restricted group. Cheap to try, so it comes early (it needs Rufus to make or share a Hypothesis account and group: a `needs-rufus` bead). Known costs: their sidebar and look, their servers, readers need an account, weak on phones.
2. *Our own*: a small service (guess: a Cloudflare Worker and database) storing the same note shape, invite-only, shown by the same script as Rufus's notes. Costs: a week or two, then accounts and moderation as the long tail.

Rufus decides after using both. The working guess is that our own wins on look and on notes living with the text, and that Hypothesis is the fallback if the long tail looks too long.

## Questions this workstream must answer

- Do notes still find their passage when a text is corrected? (The check shows any that don't; the passage id narrows the search.)
- How do margin notes work on a phone? (Reading system: tap to open.)
- How are Rufus's notes told apart from editorial glosses and, later, from readers'?
- Who may write when readers can (D7: invite-only first), and are their notes public?
- Can a note link to another text or passage, and is that the seed of the concept wiki?
- What exactly does wilber-wiki need, and can one script serve both?

## Borrow

- wilber-wiki: `docs/annotation-system.md` (research; it chose Recogito's `text-annotator-js` as an engine and Hypothesis as fallback), `docs/annotatable-reading-layer-vision.md`, `annotator.js`.
- Reports That Matter: `docs/plans/2026-08-21-highlights-design.md` (anchor shape, re-anchoring, "show as lost, never a wrong span"), `docs/design/2026-10-03-annotation-format.md` (the same own-or-Hypothesis question, still open there).
- Passage addressing precedents: SuttaCentral's segment ids with parallel layers (text, translation, comment) joined on the id; Sefaria's commentary as a text linked to a base text.
- Browser: the CSS Custom Highlight API paints highlights without touching the page's HTML (in all current browsers since 2025).

## Done-check

- A: on *Faith in Mind* and Seneca, Rufus's notes show beside their lines on desktop and on tap on a phone; breaking a quote in the file fails the check.
- C: both prototypes usable on the preview; a decision record; a lessons note written for wilber-wiki and Open Literature.

## Needs Rufus

- D3 now. A few real notes on *Faith in Mind* (stage A is not proven until the notes are his). The decision after stage C.
