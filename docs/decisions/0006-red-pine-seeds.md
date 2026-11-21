# 0006 · Design: the Red Pine page in the Seeds of Renaissance faces

Date: 2026-11-21. Decided by Rufus. Replaces direction A (decision 0005), which stays one line away in `custom.css`.

## The decision

Rufus, after seeing a measured near-copy of Emergence Magazine's Red Pine poem page: "this direction is the way to go, and probably the Seeds of Renaissance fonts", then, on the round 2 sample site (https://claude.ai/artifact/2bxZGknNTrPacMyfcq9iyb): "for now i think this is good enough to ship".

- Every word slate blue (`#3c586b` text, `#5a7a8f` titles) on grey paper `#ece9e4`; coral (`#c45a3e`, light `#ee8a70`) only for the apparatus: note marks, labels, the current place in the contents.
- Faces: Polyamine for titles, Restora for the poetic voice (subtitles, verse, numbers, chapter and case heads), Bricolage Grotesque for reading text, Apfel Grotezk capitals for labels, Noto Serif TC for Chinese. Polyamine, Restora and Apfel are served from `assets/fonts/` (Rufus: "we don't need a license check. the fonts are fine."). Fraunces is being compared as a stand-in for Restora: https://claude.ai/artifact/2bxZGknNTrPacMyfcq9iyb (the "Restora or Fraunces" page).
- Images toned in slate or coral, on white, so the multiply blend leaves the page's own paper (`assets/images/`, originals in git history before this commit; sources in `docs/design/images.md`).
- A contents rail on the left of every edition (the reading system's `.rs-rail`, filled and tracked by `js/reading.js`); notes in the right margin as before.
- The Gateless Gate: the Chinese beside the English on wide screens (`data-rs-layout="parallel"`).
- The mark: 道, the Way, in a square stamp line (Rufus: "i think cleaner").
- The home page: the picture beside the name, then a teaching's first lines, the intro and the shelf. Colophon: "Made by Rufus Pollock at Life Itself" (Rufus: "please don't mention this was built with AI assistants"); the coordinator extended this to the editions' "Editors' introduction" lines and the About page.

## Not yet

- The feature treatment (the full Red Pine page, Chinese down the centre) for Faith in Mind: in the sample, not live; it needs the Chinese text in the edition.
- Contents on a phone.

## How to undo

In `custom.css`, swap the last `@import` back to `/css/direction-a.css`. The images and fonts can stay.
