# Sutras design

Status, 2026-11-20 (second pass): **brief and mood board published, waiting for Rufus's reaction.** The first design page was rejected ("mood board is weak. where is the true beauty in this") and is archived in [archive/2026-11-20-first-page/](archive/2026-11-20-first-page/). Nothing is settled until Rufus picks. Bead: sutras-m2v.3. Process: the `designing-look-and-feel` skill, one stage at a time; this is the end of stage 1 (mood board), and the gate is his reaction.

**The living page:** https://claude.ai/artifact/P76Wz3n8TeN2CXTrgbYnwr (private to Rufus). It holds, and only holds: the brief in three lines and the feel bullets; the site today as "before"; eight directions, one large image each with take → and leave →; ten details worth stealing; three anti-references; a shortlist of three and four questions for Rufus.

## Files

- [brief.md](brief.md): the design brief (goal, who for, kinds of page, Rufus's references decoded, the feel, what is fixed, mood-board rules, done-check, open questions). Sparse on purpose; grows with feedback.
- `brief.src.html` → `brief.html`: the page. Edit the source, never the built file. Screenshots in `shots/` (JPEG, about 1100px wide) are written as `{{shot:name}}`; `python3 docs/design/build.py` inlines them; then republish `brief.html` with the Artifact tool, passing the URL above as `url` so the link stays the same.
- [moodboard-candidates.md](moodboard-candidates.md): every one of the 100-odd candidates scanned, one line each on kept, held or dropped.
- [research-reading-features.md](research-reading-features.md): how verse is set on screen, margin notes, measurements of reference sites, phone behaviour. A separate research thread for the site and notes tracks, not part of the mood board.
- `archive/`: earlier versions of the page.

## The eight directions on the board

1. The empty room (Co–Star). 2. The sober document (Reports That Matter), the floor. 3. The warm page (Emergence Magazine). 4. The hand (Plum Village). 5. Red and black, the inherited page (Zhao Mengfu's Heart Sutra). 6. The pocket classic (Aldus, 1501). 7. The text as object (Fitzcarraldo). 8. Seeds of Renaissance, adapted (added at Rufus's suggestion: keep the ink-and-paper system, swap in a reading serif, drop the movement's imagery).

Shortlist proposed: A the warm page (3 with 4), B red and black (5 held to 1, with 6), C Seeds of Renaissance adapted (8). Default if Rufus does not answer: A and B go to specimens.

## What is next

Rufus reacts to the board ("these references, these takes") and picks two or three directions. Only then: stage 2, two or three specimen cards side by side on the same page, each showing the first screen of *Faith in Mind* at phone width, the same stanza at desk width with a margin note, and a few lines of Seneca; one recommended. Then his pick, then the build on the live site.

## How the images were made

Headless Chromium (Playwright) at 1440×900, scrolled to the moment that matters, never the mere top of the page; downscaled to about 1100px JPEG. Museum images from Wikimedia Commons and the Cleveland Museum of Art under the licences stated in their captions. Nothing is mocked up; what would not capture was dropped and is listed in the candidates file.
