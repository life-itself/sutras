# Sutras design

Status, 2026-11-20 (evening): **a first small mood board is with Rufus; the gate is his reaction.** Bead: sutras-m2v.3. Process: the `designing-look-and-feel` skill, revised today with him: a raw board of 4–6 references first, feedback, then widen; pictures and directions kept on separate pages.

## The two pages

- **Mood board (pictures to look at):** https://claude.ai/artifact/Wv1GFH5C3QQtXykof4eSrg. Six existing things (Emergence's poem opening, Plum Village's sutra page, Co–Star's black band, Kaikado, Zhao Mengfu's Heart Sutra, Fitzcarraldo's covers) and two anti-patterns (Terebess, Daily Zen), each one large image with a line of take and leave, the site today, and three questions. It widens from what Rufus says.
- **Five directions (my reading of the wider scan):** https://claude.ai/artifact/P76Wz3n8TeN2CXTrgbYnwr. Ink and space; the warm page; the hand; red and black; Seeds of Renaissance adapted; Co–Star and Reports That Matter as the floor; eight details; a shortlist of four with a recommendation. Kept as is, to be revised after his reaction to the pictures. It was first published as "the mood board", which confused the two; renamed.

## How it got here today

The first design page (feel, measured research, a thumbnail board and three directions on one page) was rejected: "mood board is weak. where is the true beauty in this." It is in [archive/2026-11-20-first-page/](archive/2026-11-20-first-page/). A second pass scanned about a hundred candidates and published five directions with one image each, which Rufus liked but read as directions, not a mood board: "where's the actual mood board of existing sites that I'm looking at?" He then asked to start with a basic board of 4–6 sites and 1–2 anti-patterns and get feedback before spending more time. That is the current state.

## Files

- [brief.md](brief.md): the design brief (goal, who for, kinds of page, Rufus's references decoded, the feel, what is fixed, mood-board rules, done-check, open questions). Sparse on purpose.
- `moodboard.src.html` → `moodboard.html`: the mood board. `brief.src.html` → `brief.html`: the five directions. Edit the sources, never the built files. Screenshots in `shots/` are written as `{{shot:name}}`; `python3 docs/design/build.py` builds the directions page and `python3 docs/design/build.py moodboard` the board; republish each built file with the Artifact tool at its URL above.
- [moodboard-candidates.md](moodboard-candidates.md): every candidate scanned, one line each on kept, held or dropped. The pool the board widens from.
- [research-reading-features.md](research-reading-features.md): how verse is set on screen, margin notes, measurements of reference sites, phone behaviour. A separate thread for the site and notes tracks.
- `archive/`: earlier versions.

## What is next

1. Rufus reacts to the six and two: which he feels something for, where to look further.
2. Widen the board where he points (the candidates file and the raw captures are ready), to 10–20 images, grouped. Have a fresh agent review it as an art director before he sees it.
3. Revise the five directions page from his reactions; he picks two or three.
4. Only then: stage 2, specimen cards side by side with real lines from *Faith in Mind* and Seneca; then his pick; then the build on the live site.

## How the images were made

Headless Chromium (Playwright) at 1440×900, scrolled to the moment that matters; downscaled to about 1100px JPEG. Museum images from Wikimedia Commons and the Cleveland Museum of Art under the licences stated in their captions. Nothing is mocked up.
