# Making an edition

Status: v1, 2026-11-20, written from *Faith in Mind* (`faith-in-mind.md`, `library/faith-in-mind/NOTES.md`) and the Shodoka. Copy those two; this guide says why they are the way they are. Rules come from the [goal](../plans/2026-11-20-goal.md) and [decision 0001](../decisions/0001-founding-decisions.md).

## What an edition is

One page per text at the root (`/<slug>`, the URL never changes), in this order:

1. **Header:** kicker linking home, title, subtitle with the original title, attribution and translator.
2. **In brief:** two or three sentences: what it is, who it is attributed to, what this edition holds.
3. **Introduction:** ours, short, signed "Editors’ introduction, drafted with an AI assistant. Month YYYY."
4. **The text,** every passage with a link.
5. **About this translation:** who translated it, from what book, and any front matter of theirs (preface, translator's introduction).
6. **Source and licence:** where the words came from, how they were checked, a short summary of the changes linking to `library/<slug>/NOTES.md` on GitHub, and the copyright status.
7. **Download:** the EPUB.

Plus `library/<slug>/` (unpublished): the source as fetched, any second copy used for checking, and `NOTES.md`.

## Steps

1. **Claim the bead** (`bd update <id> --status in_progress`) and read `faith-in-mind.md` end to end.
2. **Fetch the source** into `library/<slug>/`, unchanged, and note the URL and date in `NOTES.md`. Get a second copy (another site, a PDF of the book) if one exists: it catches typos and settles credits. Treat every credit on the old page as unverified: the Shodoka's was wrong.
3. **Extract the text by script, never retype it.** Keep the source's paragraphs and line breaks.
4. **Number the passages.** The id is the number a reader would cite, levels joined by dots: `/dhammapada#183`, `/meditations#4.3`. Use the traditional numbering if there is one; otherwise number the source's own paragraphs and say in `NOTES.md` that the numbers are ours. **An id never changes once live.** If the old page had numbers, keep them where you can and record any that moved.
5. **Build the page** (template below). Typography only: curly quotes and apostrophes, spaced em dashes. Fix a word only for an obvious slip, and list every fix.
6. **Compare with the source by script.** Zero differences that are not listed in `NOTES.md`. `scripts/compare-source` does *Faith in Mind*; copy it as `library/<slug>/compare.py` (as the Shodoka did) until the general one exists (bead sutras-m2v.7.8). Record the result (passage and line counts, "0 unlisted differences") in `NOTES.md`.
7. **Write the in brief and introduction** (see Writing). Have a fresh subagent critique them, against the sources, before you ship.
8. **Make the EPUB:** `scripts/epub <slug>` writes `downloads/<slug>.epub`; commit it. For now it handles verse only (numeric ids, `## About this translation` straight after the verse `</div>`). For prose or dotted ids, open the EPUB and check it; if it is broken, say so on bead sutras-m2v.8.3 (site track).
9. **Check:** `scripts/check` must pass.
10. **Ship:** commit only your files, then `git fetch origin && git rebase origin/main && git push origin HEAD:main`. Look at the live page at phone and desktop width, and open a passage link (`/<slug>#3`).
11. **Record the ids:** `scripts/check --record`, commit `scripts/published-ids.txt` and push. From now on the check fails if any of them vanishes.
12. **Tell the site track** (a comment on its bead, or a new bead) so the home page line can link to the edition and use its credit.

## The page

Frontmatter (all of it is checked by `scripts/check`, including `syntaxMode` and both scripts):

```yaml
title: Faith in Mind
description: "One sentence: what it is, whose translation, what is included."
author: "Seng Ts’an (attributed; doubtful)"
translator: Master Sheng-yen, with Paul Kennedy
date: "Unknown. Attributed to Seng Ts’an (d. 606); probably Tang dynasty (618–907)"
tradition: Ch’an (Zen) Buddhism
source: https://terebess.hu/english/hsin3.html
licence: "Translation © 1987 Dharma Drum Publications: in copyright, reproduced in full without permission. Editorial additions CC BY 4.0."
status: published        # or partial (e.g. Red Pine), or draft
layout: plain
syntaxMode: md
scripts:
  - /js/reading.js
  - /js/edition.js
```

The body is the `.rs` wrapper copied from `faith-in-mind.md` (header, then `rs-body` / `rs-wrap` / `article.rs-text`), with Markdown inside. Things that bit us:

- **`syntaxMode: md` is required.** The site default is MDX, which breaks on raw HTML mixed with Markdown.
- **Blank lines round any Markdown inside raw HTML**, or Flowershow renders it as literal text. Inside an HTML element (`<p class="rs-inbrief">`), Markdown is not parsed: use `<em>`, not `*…*`.
- **Verse:** wrap the text in `<div class="rs-verse">`. Each stanza starts with its link on its own line, `<a class="v" id="3" href="#3">3</a>`, then the lines, each ending in two spaces. `scripts/check` fails any stanza without one.
- **Prose** (Seneca, *Meditations*): the template style for numbered prose passages is not settled yet; ask the site track (bead) before inventing one. Use `<div class="rs-passages">` with the same `<a class="v">` link at the start of each numbered paragraph, so the check covers it.
- **Links to a passage** from the introduction or notes: write `/<slug>#18`, not `#18`, which breaks in the EPUB (bead sutras-m2v.7.9).
- **Notes** are Markdown footnotes, `[^1]`, starting "*Editors’ note.*". reading.js moves them into the margin. Put the marker at the **end of a line**, never mid-line, or an opened note splits the line on a phone. Every quotation in a note is verbatim and its source is listed in `NOTES.md`.
- Don't edit `css/`, `js/`, `custom.css` or `scripts/` from an edition track: file a bead for the site track.

## NOTES.md

Copy the headings of `library/faith-in-mind/NOTES.md`: sources, how it was made, every change to the words, left as in the source, not the translator's words, facts and where each comes from, copyright. Add a section for anything special (a translator correction, where a second copy differs).

## Writing

- **Voice:** plain, quiet, personal. A reader's notes, not a scholar's apparatus or a teacher's sermon. No superlatives ("the best-loved", "profound").
- **Facts only from a source you read,** each listed in `NOTES.md`. If tradition and scholarship disagree (authorship, dates), say so plainly: "Tradition gives it to…, though he probably did not write it."
- **Every quotation verbatim,** from the text or a named source.
- **The introduction** says what the text is, what it says (its first lines often do), how its translator or teachers used it, and one way to read it. A few short paragraphs.
- **Copyright:** per decision 0001.5, an in-copyright translation is published in full with its status stated. Use the Faith in Mind wording: "© year holder and remain in copyright. They are published here in full, without the permission of the rights holder. If you hold the rights and want this changed or taken down, please open an issue." Our additions are CC BY 4.0.

## Done-check for an edition

Every part in the order above; compared by script with 0 unlisted differences; `scripts/check` passes; live page seen at phone and desktop width; ids recorded and pushed; lessons in `docs/lessons/` (one short file each); bead closed with a comment.
