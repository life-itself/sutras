# Landing page: opening-screen alternatives

Status, 2026-11-20: three sketches of the home page's first screen, for Rufus to choose from. Brief: [../../plans/2026-11-20-landing-page-brief.md](../../plans/2026-11-20-landing-page-brief.md). Track: `landing` (bead sutras-m2v.8.19).

The live home page is sketch **A**. The sketches are static HTML that load the same `css/reading.css` and `css/home.css` as the site, so the look is the real one; they are not the live page, and the sketch C image is public domain from the moodboard, not a site choice.

| Sketch | What it is | Screenshot |
|---|---|---|
| **A, text first** (live, recommended) | The first words are a line from *Faith in Mind*, large; attribution small; then one plain sentence on what this is; then the shelf. | [a-text-first-1280.png](a-text-first-1280.png), [a-text-first-390.png](a-text-first-390.png) |
| **B, statement first** (the page as it was) | The old "In brief" box: the site's name, then one long sentence in a tinted box. | [b-statement-first-1280.png](b-statement-first-1280.png), [b-statement-first-390.png](b-statement-first-390.png) |
| **C, image led** | The same opening line beside one public-domain ink landscape (Sesshū, *Haboku Sansui*, 1495). Shows what a picture could do; not for the live site until each text's licence and caption are checked. | [c-image-led-1280.png](c-image-led-1280.png), [c-image-led-390.png](c-image-led-390.png) |

Files: [a-text-first.html](a-text-first.html), [b-statement-first.html](b-statement-first.html), [c-image-led.html](c-image-led.html). Each file's first comment says what it is.

## Recommendation

A. It puts the reader inside a text on the first screen, which is what the design brief asks for, and it is the least decoration. B is the sober floor; C is the first look at what a picture could do, and is worth a decision only once there is a set of images with licences.

## What the design track needs from this

1. The opening line: a serif setting, large, no box. Hook: `.rs-home .rs-lead` in `css/home.css`.
2. A decision on images: one per text, or none. The shelf already has a slot per group (`.rs-shelf`).
3. Colour: the accent is the theme's `--rs-accent`; to change it for the home page only, override on `.rs.rs-home[data-rs-theme="personal"]`.
4. A mark: the plain "Sutras" kicker is the place for one (`.rs-home .rs-kicker`).
5. Type: the mono labels (IBM Plex Mono) come from the current reading look; they can change in one place (`--rs-ui` on the theme).
