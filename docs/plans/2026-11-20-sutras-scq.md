# Sutras re-vision — SCQ

Status: draft outline, 2026-11-20. Not signed off. Situation is from the interview and repo review; the complication, question and criteria were drafted by the agent, and items marked `(guess)` await Rufus.
Source: bead sutras-m2v.1 (epic sutras-m2v). Vision: [docs/vision.md](../vision.md). Parent: Unified Text / Open Literature initiatives in `rufuspollock/planning`.

## SCQ

### Situation

- Sutras (sutras.lifeitself.org) is a public Flowershow site with six texts: five Buddhist/Zen and one Seneca.
  - Flat repo; the home page is a bare list of links; each page is the raw text.
- No text has been added since 2022-12.
- Rufus wants it to be a curated library of wisdom texts he wants to read, in beautiful editions with his annotations, public, for himself first ([vision](../vision.md)).
- It is meant as a first experiment in the Open Literature / Unified Text direction: accessible, annotatable, linkable, downloadable.
- AI agents and nearby pipelines (wilber-wiki, Reports That Matter, pdf-report-publishing) now make a good edition of a text much cheaper to produce than in 2022.

### Complication

- The one person the site is for has not used it in four years. (guess)
  - Why it stalled: unknown — Rufus to say. Where he reads these texts today: unknown — Rufus to say.
- It is pulled two ways: a personal library (a few texts done beautifully, for Rufus) and an experiment (general machinery for open literature: annotation, linking, downloads). The second can swallow the first. (guess)
- If nothing changes, the site stays a dormant list of six raw texts and the Open Literature direction gets no first test. (guess)

### Question

What is the smallest Sutras that Rufus himself reads from and adds his notes to?

Criteria:
- By when: 2027-01-31 (guess)
- For whom: Rufus first — decided (Rufus, 2026-11-20). It must also be a good place for a stranger to read the same texts.
- Effort: built mainly by AI agents on Flowershow, a few hours a week of Rufus's time (guess)
- Off the table: a complete catalogue; an academic archive — decided (Rufus, 2026-11-20). Building a custom reading platform (guess)

Issue tree:
- What is Sutras for, and for whom? — decided: see [vision](../vision.md) (Rufus, 2026-11-20)
  - Public or private? — decided: public (Rufus, 2026-11-20)
  - Buddhist only or wider? — decided: wisdom texts in general, Rufus's curated set (Rufus, 2026-11-20)
  - Keep the name "Sutras"? — open; Rufus leans to a better name
- What is in the first version: editions only, editions plus notes, or also a concept wiki? — open
- What does one text "done well" look like? — open
  - What is on the reading page (intro, attribution, metadata)? — open
  - Which download formats in the first version (EPUB, PDF)? — open
  - How are passages addressed so they can be linked? — open
- How do annotations live with the text? — open
  - Are they public from the start? — proposed: yes (Rufus said "possibly publicly", 2026-11-20)
  - When, if ever, do other people annotate? — open
- Which texts first? — open (bead sutras-m2v.4)
- What is the working policy for in-copyright texts and translations? — open
  - Stance — decided: not gated on permission (Rufus, 2026-11-20)
  - Full text, samples, or unpublished library, per text? — open
  - What happens to the Yogins of Ladakh dump? — open
- How does a text get from source to published, and who does what (AI, Rufus)? — open
  - What cadence keeps it alive? — open (bead sutras-m2v.4)
- What would count as having learned something for Open Literature / Unified Text? — open
- What should it look and feel like? — open (bead sutras-m2v.3; [brand](../brand.md))

## Ideas offered (parked)

- Side-by-side versions of a text, e.g. Tao Te Ching translations, as samples where in copyright (Rufus).
- A concept wiki for Buddhist ideas with verified excerpts, as in wilber-wiki (Rufus).
- Annotating publicly and with others (Rufus).
- Borrow from Reports That Matter's document-to-page approach (Rufus).
- EPUB and PDF output; `life-itself/pdf-report-publishing` already has a Typst pipeline (agent).
- A new name (Rufus).

## Next

LTP not yet run. Run `ltp-project` (or `reason-commons`) on this file in a new thread once the complication and criteria are confirmed.
