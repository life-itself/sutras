# Goal check, 2026-11-20 (site track)

Checked against the live site (sutras.lifeitself.org) and the repo at `main` after dbf348c. Live pages were screenshotted and measured by script in headless Chrome at 1280px and 390px (the screenshots and scripts are in the session scratchpad, not committed). Done-check items are from [the goal](plans/2026-11-20-goal.md).

## Done-check

1. **Eight editions live: pass, with one wording to settle.**
   - All eight pages return 200 and have In brief, Introduction, the text with passage links, About this translation, Source and licence, and Download.
   - Each EPUB link resolves to an `application/epub+zip` file (8 of 8).
   - A passage link (`/<slug>#id`) lands with its target below the navbar on all eight; measured after the page settles, at both widths.
   - No page scrolls sideways at 390px (checked on all ten pages, home and about included).
   - The goal says Red Pine is "marked partial". The page is the whole sutra (32 chapters, the notes say "complete, not partial") and its status is `published`. Left as published; bead sutras-m2v.6.7 (needs-rufus) asks for the wording to be settled.
2. **Each edition faithful: pass.**
   - Each source is in its own folder in the private library (`life-itself/sutras-library`).
   - Every compare script was run against its edition, on a copy of the source folder: Faith in Mind (`scripts/compare-source`), Shodoka, Diamond, Diamond (Red Pine), Seneca, Mumonkan (Japanese text too), Meditations, Dhammapada. Each reports 0 unlisted differences.
   - Every change is listed in the public note `docs/editions/<slug>.md` (8 notes).
   - Caveat: the compare scripts don't run from the repo root as the notes say; bead sutras-m2v.7.17.
3. **Home, about, nav and footer live; `scripts/check` passes: pass.**
   - The home page lists all eight texts; about is live; the navbar has Texts, About and the GitHub link; the footer's links are on the page.
   - Navbar and footer take the page colour, with no white bands (checked at both widths).
   - `scripts/check` passes on every text, page and note set (`scripts/notes --check` now runs inside it, and so do the quotation checks).
4. **Rufus's notes on one text: pass, with a placement bead.**
   - Meditations: 122 notes in `annotations/meditations.yaml`, generated into `js/notes/meditations.js` and loaded on the live page. The margin shows the note for 4.3 at 1280px.
   - Open problem: at 1280px the note for 4.3 shows only its byline at the navbar's lower edge, its text above that under the bar. Bead sutras-m2v.8.18. Not checked: how notes show at 390px.
5. **The design page is with Rufus: not checked by the site track.**
   - `docs/design/README.md` links a mood board and a five-direction page, and says the gate is Rufus's reaction. Whether those pages contain the recommendation the goal asks for was not checked here; that is the design track's.
6. **Written down: pass.**
   - The guide: `docs/guides/making-an-edition.md` (v2 this pass, with the private-library steps).
   - The annotation options paper: `docs/2026-11-annotation-options.md`.
   - Lessons: 25 files in `docs/lessons/`.
   - Beads: each track's beads are up to date in Beads; see the list below.

## Done in this pass

- `library/` is out of the public repo (d9f0659). The private repo already held every source file, checked identical; `library/tools` moved there (7c856e0). Git history is not rewritten.
- `scripts/compare-source` reads `SUTRAS_LIBRARY`, and skips with a warning if the library is absent. Its output is unchanged.
- `scripts/check` now runs `scripts/notes --check`, and checks quotations in introductions, notes and about sections against the text, other editions and the private sources (f755659, 2681b1e). Tested with a planted fake quotation, which fails.
- Chinese titles in four introductions are set as `lang="zh"` spans, so they no longer break between characters on a phone.
- The phone footer lines up with the page's 20px gutter (it was 32px).
- Faith in Mind has the Sutras kicker link the other seven have.
- Every Download line now gives the same formula, which matches what each EPUB holds (checked in the built files).
- Mumonkan has `passageUnit: case`. The EPUB shows it after its next rebuild, which is the EPUB track's.

## Left

- sutras-m2v.8.14 (needs Rufus): rewrite public history to remove the whole-book PDFs. Not done.
- sutras-m2v.6.7 (needs Rufus): Red Pine wording, "marked partial" or "complete".
- sutras-m2v.8.18: margin note under the navbar at 4.3 (Meditations, 1280px).
- sutras-m2v.7.17: compare scripts in the private library don't run from the repo root.
- sutras-m2v.7.8 (not site track): generalise the compare script.
- Not mine, still open: sutras-m2v.8.3 (EPUB pipeline, in progress with the EPUB track); sutras-m2v.7.15 (Meditations 4.14 asterisks); the Faith in Mind EPUB and rights items under 6.6; the editorial items under 5.

## Beads closed this pass

sutras-m2v.8.13, sutras-m2v.8.4, sutras-m2v.9.7, sutras-m2v.8.15, sutras-m2v.8.16, sutras-m2v.8.17, sutras-1i9. Sutras-m2v.8.10 and sutras-12n were already closed.
