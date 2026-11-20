# Sutras design

Status: stages 0–2 drafted by an agent on 2026-11-20 and critiqued by a fresh agent; **not yet seen or decided by Rufus**. Nothing here is settled until he picks. Brief: [4-design.md](../plans/workstreams/4-design.md). Bead: sutras-m2v.3. Process: the `designing-look-and-feel` skill.

**The living page:** https://claude.ai/artifact/P76Wz3n8TeN2CXTrgbYnwr (private to Rufus). It holds the feel, the measured research, the mood board, three directions and the decisions needed, in that order.

## How to change the page

Edit `brief.src.html`, never `brief.html`. Screenshots live in `shots/` (720px JPEG, about q60) and are written in the source as `{{shot:name}}`. Then run `python3 docs/design/build.py` and republish `docs/design/brief.html` with the Artifact tool, passing the URL above as `url` so the link stays the same. Each later stage adds a section to this page; it does not get a new page.

## Feel (proposed)

**"Without lack, without excess"**, a line from *Faith in Mind* itself. It tests both ways: would the reader miss this (if not, it goes), and is the reader missing something (then it is added, plainly). Alternatives offered: "A plain room with good light", "Ordinary mind".

- Space is the material: calm and hierarchy come from position and room before size, rule or colour.
- One hand: the only personality on the page is the reader's marks; warmth comes from that, never from decoration.
- The page waits: nothing moves, pops up or asks.
- Character: a well-made paperback someone has read with a pencil.
- Not: a temple gift shop, a wellness app, a scholar's apparatus, a tasteful AI landing page.

## What was measured

Computed styles read from the live pages with headless Chrome (Playwright) at 1440×900 on 2026-11-20. Characters per line are estimates, plus or minus five.

| Page | Text face | Size / line | Column | Chars | Ground | Ink |
|---|---|---|---|---|---|---|
| Sutras today | Flowershow default | 16 / 28 | 672px | 89 | #FFFFFF | dark grey |
| Co–Star, home | Akkurat sans; Romana display 40/40; mono 12/16 | 14 / 20 | centred | n/a | #F7F7F7 | #575657 |
| Reports That Matter, report | EB Garamond 20/30; Inter 16.8/28.6; IBM Plex Mono 12 | see left | 564px | 70–73 | #F7F7F7 | #252525, #575657 |
| Plum Village, a sutra | Gentium Plus; Cormorant Garamond title | 20.25 / 28.35 | 657px | 78 | #FFFFFF (home #FAF1EB) | #222222 |
| SuttaCentral, Dhammapada | Skolar | 16 / 24 | 394px | 56 | #FFF8F3 | #201B13 |
| Standard Ebooks | Georgia | 18 / 27 | 608px | 75 | white | black |
| Sefaria | Cardo, justified | 22 / 35.2 | 700px | 81 | white | black |
| 84000 | Noto Serif, justified | 16 / 28 | 616px | 78 | near white | near black |
| Craig Mod | FF Meta Serif | 20 / 30 | 746px | 85 | white | #333333 |
| Public Domain Review | Alegreya | 19.6 / 32.4 | 665px | 82 | white | #1D2731 |
| Tufte CSS | ET Book; sidenote 16.5 / 21.45 in a 347px margin | 21 / 30 | 693px | 81 | #FFFFF8 | #111111 |
| Ink & Switch | Merriweather; notes Merriweather Sans 13 / 20 in a 168px margin | 16 / 24 | | | #FCFCFC | black |
| Poetry Foundation (verse) | | 20 / 32 | | | white | black |
| dhammatalks.org (verse) | Source Serif | 19.2 / 28.8 | | | white | #212529 |

What follows from it:

- One book-weight text serif, and a second voice for everything else; character comes from the second voice, not the text face.
- 19–20px on a laptop, 17–18px on a phone; line height 1.5–1.6.
- Prose about 65–70 characters. Verse sets its own width from its longest line (50 characters in *Faith in Mind*), and a turned line hangs in by 1.5em.
- Space, not rules or boxes, makes the hierarchy. Grounds sit within a hair of white. Warmth in the admired pages is never a palette.
- Verse: lines left aligned, one line between stanzas, numbers outside the block.
- Margin notes: about 0.8–0.85 of the text size, tighter lines, a 13–16rem margin, level with the line they are about; on a phone shown in place under the line.

## Directions (proposed; Rufus picks one or a blend)

| | Reads zen as | Type | Colours | Signature |
|---|---|---|---|---|
| A · Bare | taking away | Spectral, one size, one weight | #F3F2EF, #33312E, #66625C | **One size**: hierarchy by space and two greys only; no accent, no mark on the text |
| B · The read copy | the warm hand | Alegreya, italic for notes, Alegreya Sans labels | #FBF9F4, #2A2622, #2F4A6D | **The pen line**: marked words underlined in blue-black, the line running out to the note |
| C · Red and black | the inherited book | Gentium Book Plus, Noto Serif TC for Chinese | #F5F4F0, #161514, #C22D1C | **The red dot**: black is the text; red does one job, the apparatus (stanza numbers, and a small dot in the margin beside whatever Rufus has marked) |

**Recommended: C, held to A's restraint.** Its distinctive mark comes from the texts' own world and does a job (it shows Rufus's hand in the smallest possible way); it answers "warmer" without a warm palette; its parts are shapes that still read without colour; and red numbering is as much the Western scribe's habit as the Chinese printer's, so it should carry to Seneca. A is the sober floor and the fallback. B is the nearest to twee and to Tufte CSS, and its blue underline looks like a link.

The historical claim is deliberately modest: red numbering is rubrication; the dot is loosely after 圈點, the marks Chinese readers brushed beside characters they valued (ours is one per line in the margin, theirs ran beside each character and were not always red).

## What the review changed

A fresh agent reviewed the page as a tough design critic. Applied: the mark became a solid dot on the numeral axis (hollow circles read as list bullets); red was cut back to numbers and dots only; a marked sentence and note were added to the Seneca test in all three; the Chinese and Western history was restated more carefully; the title block was added at desk width so the compositions part; the "recommended" pill and outline became a plain word; the boards were trimmed; A's grey was darkened. Not applied: moving the directions above the research (the skill fixes the page order; jump links at the top go straight to them instead), and shrinking A's notes (one size is A's whole idea). Still true after the changes: on a phone the three share one skeleton and differ mainly in type and mark.

## References captured

Real screenshots in `shots/`: the current site (home, *Faith in Mind*), Reports That Matter, Co–Star, Plum Village (home and a sutra), SuttaCentral, Standard Ebooks, Craig Mod, The Public Domain Review, Lotsawa House; anti-references Terebess, Daily Zen, Headspace; verse board Poetry Foundation, dhammatalks.org, Access to Insight; margin-notes board Tufte CSS, Ink & Switch, 84000, Sefaria. Captured but left off to keep the board short: Organism.earth, Emergence Magazine, Gwern, Goodreads quotes. Two photographs of printed pages from Wikimedia Commons: the Doves Press Bible (1903) and the Diamond Sutra (868).

Failed or blocked, so not shown: Calm, BrainyQuote, iA, Fermat's Library (only its home page loaded), poets.org, sacred-texts.com, Tiny Buddha.

## Still open

- Rufus's answers to the six decisions on the page: the feel phrase; the direction; whether Chinese appears (title and author only is proposed); near-black or mid-grey text; notes shown at once on a phone; pictures (none for now).
- No image was found of a Chinese page with red reading marks (圈點); the convention is described on the page but not shown. Worth finding a real one before C is built, to check the claim against an example.
- C's mark in prose: a dot shows where a marked passage begins, not where it ends. To solve in the build.
- A reading order for Rufus in a hurry: the review argued for directions first and research as an appendix. Easy to switch if he prefers.
- The "in brief" line and the margin note on the specimens were written by the agent to show the form. They are not Rufus's.
- Not yet designed: a Mumonkan case (case, comment, verse, Chinese), the home page, front matter for a long text, and the EPUB. These are for stage 4, on the chosen direction.
- Checked in headless Chrome: Spectral, Alegreya and Gentium Book Plus (roman and italic, as served by Google Fonts) all carry the Pali and Sanskrit marks ā ī ū ṛ ṝ ḷ ṅ ñ ṭ ḍ ṇ ś ṣ ṃ ḥ and ō. Not yet checked: how the directions feel after an hour of reading on a real phone.
- The live `/faith-in-mind` page showed an "Error parsing MDX" message during this work (another workstream's build), so there is no phone or close-up "before" shot of the verse.
