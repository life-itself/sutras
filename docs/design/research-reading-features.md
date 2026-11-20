# Research: how reading pages work on screen

Status: 2026-11-20. Moved out of the design page, where it crowded the mood board. This is a separate research thread for the **site** and **notes** tracks: how verse is set on screen, how margin notes are done, what the reference sites measure, what happens on a phone. It feeds the specimen stage (stage 2) and the build, not the mood board. Measurements were read from the live pages with headless Chrome at 1440×900 on 2026-11-20; characters per line are estimates, plus or minus five. Faces marked * are licensed.

## What the admired pages measure

| Page | Text face | Size / line | Ratio | Column | Chars | Ground | Ink |
|---|---|---|---|---|---|---|---|
| Sutras today | Flowershow default serif | 16 / 28 | 1.75 | 672px | 89 | #FFFFFF | dark grey |
| Co–Star, home | Akkurat* sans; Romana* display 40/40; mono 12/16 | 14 / 20 | 1.43 | centred | n/a | #F7F7F7 | #575657 |
| Reports That Matter, report | EB Garamond title 56/59; Inter intro; IBM Plex Mono labels 12 | 20 / 30 (Garamond), 16.8 / 28.6 (Inter) | 1.5, 1.7 | 564px | 70–73 | #F7F7F7 | #252525 and #575657 |
| Plum Village, a sutra | Gentium Plus; Cormorant Garamond title 42.75 | 20.25 / 28.35 | 1.4 | 657px | 78 | #FFFFFF (home #FAF1EB) | #222222 |
| SuttaCentral, Dhammapada | Skolar*; title 44.8 in grey small capitals | 16 / 24 | 1.5 | 394px | 56 | #FFF8F3 | #201B13 |
| Standard Ebooks, Meditations | Georgia | 18 / 27 | 1.5 | 608px | 75 | white | black |
| Sefaria, Pirkei Avot | Cardo, justified | 22 / 35.2 | 1.6 | 700px | 81 | white | black |
| 84000, Heart Sutra | Noto Serif, justified | 16 / 28 | 1.75 | 616px | 78 | near white | near black |
| Craig Mod, essay | FF Meta Serif* | 20 / 30 | 1.5 | 746px | 85 | white | #333333 |
| Public Domain Review, essay | Alegreya | 19.6 / 32.4 | 1.65 | 665px | 82 | white | #1D2731 |
| Tufte CSS | ET Book; sidenote 16.5 / 21.45 | 21 / 30 | 1.43 | 693px | 81 | #FFFFF8 | #111111 |
| Lotsawa House, a verse text | Spectral | 18.6 / normal | n/a | 800px | 96 | white | #444444 |
| Ink & Switch, essay | Merriweather; notes Merriweather Sans 13 / 20 in a 168px margin | 16 / 24 | 1.5 | | | #FCFCFC | black |
| Poetry Foundation, a poem | | 20 / 32 | 1.6 | | | white | black |
| dhammatalks.org, Dhammapada | Source Serif | 19.2 / 28.8 | 1.5 | | | white | #212529 |
| Access to Insight, Dhammapada | Verdana | 14.4 / 18.7 | 1.3 | | | white | black |

What follows, one factor at a time:

- **Type.** Every one sets its text in a single book-weight serif and keeps a second voice for everything else. The second voice is where each gets its character: Co–Star's mono, Plum Village's handwriting, SuttaCentral's grey small capitals. None gets it from the text face.
- **Size.** The pages that feel generous are 20 to 22px (Plum Village, Craig Mod, Tufte, Sefaria). The 16px pages are the archives. Take 19–20px on a laptop, 17–18px on a phone.
- **Measure.** Prose runs 70 to 85 characters, wider than the textbook 66. The calmest page here, SuttaCentral, is 56. Take about 65–70 for prose, and let verse set its own width from its longest line (50 characters in *Faith in Mind*).
- **Line height.** 1.4 to 1.6 at 20px. Only the 16px pages go to 1.75, to make up for size. Take 1.5–1.6.
- **Space.** Co–Star and Reports That Matter use no rules, boxes or shadows; things are parted by distance. SuttaCentral sets its title small and grey and leaves a long pause before the first line. Space does the work of hierarchy.
- **Colour.** All the grounds sit within a hair of white, and none of the reading pages uses colour inside the text. Co–Star's mid-grey ink is for short marketing lines; Reports That Matter went to #252525 for reading. Warmth in the admired pages is never a palette: at Plum Village it is a handwritten name and people's faces; at SuttaCentral a faint tint.

## Verse on screen

Looked at: Poetry Foundation (title, author, poem, close together; lines left aligned; a full line between stanzas), dhammatalks.org (indents that show how the verse is phrased, verse number small after the verse), Access to Insight (the same verses at 14px in a screen sans with tight lines, much harder to read as verse), SuttaCentral (a narrow column on a faintly warm ground, numbers hidden until asked), Lotsawa House (verse left aligned with EPUB and PDF beside it, but a 96-character line).

- Lines left aligned, never centred. A block narrower than prose, set by the longest line. Line height 1.5 to 1.6. One line of space between stanzas and nothing else between them.
- Numbers outside the block, small, in the second voice. Ours must be visible because the stanza number is the link (`/faith-in-mind#3`): in the left margin.
- The turnover: on a 390px phone at 17–18px about 38 to 42 characters fit, and *Faith in Mind* has lines of up to 50 ("The erring mind begets tranquillity and confusion;"). A turned line hangs in by about 1.5em so it cannot be mistaken for a new line. Stepped indents (dhammatalks) belong to a translator, not a house style.

## Notes in the margin

Looked at: Tufte CSS (note 16.5/21.45 beside text 21/30: 0.79 of the text size, tighter lines, a margin half the column, level with its line; superscript numbers), Ink & Switch (no markers at all; the note is tied to its paragraph by position and told apart by face and size; a 168px margin makes notes into ribbons), 84000 (passage numbers 1.1, 1.2 in the left margin, small and pale), Sefaria (touch a passage and what others have said opens beside it: the model for reader annotation later), Gwern (sidenotes plus link popups; dense).

- About 0.8–0.85 of the text size, tighter lines, a margin of 13–16rem, first line level with the line it is about. Told apart by at least two of size, face, colour and position.
- None of these marks the passage itself; they rely on a superscript or on position. For a reader's notes on verse the mark matters, since it says "he stopped here". This is where directions can differ most: an underline, a dot in the margin, a change of ink.
- A mark in prose shows where a marked passage begins, not where it ends. To solve in the build.
- On a phone there is no margin. Rufus's notes are few, so show them in place under the line, indented, with no tap needed.

## Legibility floors

Floors a direction should not break without saying why:

- Prose: 60–72 characters a line on a laptop, about 35–45 on a phone; line height about 1.5–1.7 (less for a face with a small x-height); body 18–21px on a laptop and no smaller than 17px on a phone.
- Verse: the same size as prose or a step larger; line height about 1.4–1.6; a line of space between stanzas; the turnover designed as above.
- Notes told apart from the text by at least two of size, face, colour and position.
- "Better to read" is judged against the current site at 390px wide.

Defaults (break with a reason): stanzas separated by space, not rules; numbers small and grey in the margin; notes in the margin on wide screens and in place on a phone; at most three colours, the accent with one job; no boxes.

## Fonts checked

In headless Chrome, Spectral, Alegreya and Gentium Book Plus (roman and italic, as served by Google Fonts) all carry the Pali and Sanskrit marks ā ī ū ṛ ṝ ḷ ṅ ñ ṭ ḍ ṇ ś ṣ ṃ ḥ and ō. Not yet checked: how any of them feels after an hour of reading on a real phone.

## Still to research

- A Mumonkan case (case, comment, verse, Chinese) on one screen; which Chinese face (Noto Serif TC or SC, or a Song face) sits well beside a Latin serif.
- Front matter for a long text (*Meditations*: twelve books) and the chapter picker.
- The EPUB: whether the type choices carry into reading apps.
- Rufus's notes as data: how the margin display (notes track) reads a notes file and places a note level with its line.
- A real example of a Chinese page with red reading marks (圈點), to check the "red and black" claim against an object before anything is built on it.
