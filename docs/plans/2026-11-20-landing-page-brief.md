# Landing page brief

Status: draft 2, 2026-11-21, rewritten by the landing track after judging draft 1 and the page built from it (bead sutras-m2v.8.19). Owns the words and structure of `README.md` (the home page) and `about.md`. The look is the design track's (decision 0005: Emergence's Red Pine page as the base, warm grey paper, one image per text, Literata, a warm red used rarely, the mark 慧); it owns `css/` and the shelf's class names, and the two tracks agree markup changes by message.

## What the page is for

The home page is the front door of a small library. A stranger should know in one screen what this is and want to open a text; Rufus should find the text he is working on in one click and not be got in the way of. The page should feel like the texts: little on it, every word earning its place, nothing asking for anything.

## Done-check

1. **The first screen is a text, then a sentence.** The page opens on the first lines of one of the editions, verbatim, and the line beneath them says which text, what it is, how long it takes, and is the link into it. Then one short paragraph says what Sutras is. At 1280×800 the lines, the paragraph and the top of the shelf are on the first screen; at 390×844 the lines and the start of the paragraph are.
2. **The shelf is one shelf.** Every live edition (nine on 2026-11-21), in one run, no section headings. Each entry: its image, the edition's own label (as on its page: "Zen · a poem"), the title, author and translator, the time to read in the edition's own words, and one line that is a reason to read it, not a blurb.
3. **A short colophon after the shelf**, no headings: one paragraph on reading here (a link to every passage, notes in the margin where there are notes, translations compared, an EPUB) and one sentence on who makes it, pointing to `/about`. "Every line" is not true of the prose texts, which link by section or entry; say passage.
4. No horizontal scroll at 390; every link resolves; `scripts/check` passes with the private library present.
5. Before and after screenshots at both sizes under `docs/design/landing/`; the choices that are Rufus's in the `needs-rufus` bead with a recommendation and the default taken.

## Who arrives

Rufus, returning (knows everything; wants the shelf and no friction). A stranger who searched for one text (probably lands on the text; the home page is their second visit, and should show that the text they want is here, complete and free, and that there are others). Someone sent a link to a passage by a friend (should understand the idea in a screen: a few texts, read slowly, a link to every line, notes).

## Rules

- **Voice**: plain, quiet, personal; the voice the editions settled on in [writing an introduction](../guides/writing-an-introduction.md). Say what a text does, not what it is like. No praise adjectives, no "explore", "discover", "journey", no exclamation marks. "Worth reading slowly" is the one judgement the page makes, because it is the reason the library exists. Promise nothing of every text that is not true of every text ("every line", "notes in the margin").
- **Not** a marketing page (no cards, triads, buttons), a catalogue (no grid of covers with filters, no sections for two items), or a sermon (no quote of the day, no exhortation). The opening line is the beginning of a text the reader can go on reading, named and linked as such; that is what keeps it from being a quotation on a wall.
- **Every quotation verbatim** from the edition; `scripts/check` enforces it. Credits and titles come from each edition's frontmatter.
- **Reading time** on the shelf is the figure the edition's own in brief gives, in words ("ten minutes", "four or five hours"), so the shelf and the page the reader lands on agree. Draft 1's rule (words ÷ 240, rounded to five minutes, "about 235 min") is dropped: nobody says it and no edition does.
- **Promise only what every entry has** (lesson: [promise only what ships](../lessons/2026-11-20-promise-only-what-ships.md)).

## What the references do

Of the nine home pages looked at (Emergence, Standard Ebooks, Fitzcarraldo, Public Domain Review, SuttaCentral, Lotsawa House, 84000, Poetry Foundation, Sefaria), the ones to learn from open on one sentence of purpose and a short list (Standard Ebooks, Sefaria), or on one piece given room (Emergence, Public Domain Review). The ones to avoid open on a slogan ("Timeless wisdom for a changing world") or an institution's statement with a donate button. SuttaCentral is the one that puts the texts' own words on the front ("we let the Buddha speak for himself"). Sutras takes that further: the first words on the page are a text.

## Choices that are Rufus's (defaults taken)

1. **Which text opens the page.** Default taken after critique: the Shodoka's first two lines, "There is the leisurely one, / Walking the Tao, beyond philosophy,": a person in it, ending on a comma, so the page's first sentence is unfinished and the only way to finish it is to go in; and far less quoted. Alternative: *Faith in Mind*'s "The Supreme Way is not difficult / If only you do not pick and choose.", the test page and the shortest text, but the most-quoted couplet in Zen and complete in itself, so it reads as a plaque.
2. **One shelf or sections by tradition.** Default: one shelf of nine, east to west; the tradition is in each entry's label.
3. **Whether the home page names Rufus at all above the fold.** Default: no; he is in the Meditations entry's line and the closing sentence.
