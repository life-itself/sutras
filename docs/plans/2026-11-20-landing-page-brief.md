# Landing page brief

Status: draft 1, 2026-11-20. Track `landing` (bead sutras-m2v.8.19, under the site epic). Owns `README.md` (the home page), `about.md`, `css/home.css`, and one `@import` line in `custom.css`. The coordinator authorised the `css/home.css` file and that one import; the Faith in Mind track (sutras-m2v.6) still holds the rest of `css/` and `custom.css`, so nothing else in them changes. The look is the design track's to choose (see [design brief](../design/brief.md)); this page uses the current reading look and leaves hooks for it.

## Goal and done-check

The home page is the first thing a stranger reads. Within ten seconds it should say what this is, show the texts, and let the reader start one.

Done-check:

1. Opens with words from a teaching, then one plain sentence saying what Sutras is.
2. Lists the eight editions in a small shelf: title, translator, a reason to read, reading time, a link.
3. States that each text is complete, free to read, linkable to the line, and downloadable as an EPUB; and that a reader's notes sit in the margin.
4. Says who is behind it, in one short paragraph that points to `/about`.
5. Reads well at 390px and at 1280px: the track has taken both screenshots and looked at them, and the page has no horizontal scroll at 390px. Measured: the opening line and the sentence fit one 1280px screen; the shelf takes no more than about two 390px screens.
6. `scripts/check` passes (links, fragments, verbatim quotations).
7. Three alternatives of the opening screen committed under `docs/design/landing/`; the recommended one is live.
8. A `needs-rufus` bead holds the choices that are his.

## Who arrives

1. **Rufus, returning.** Knows everything. Wants to see the page as a reader would, and to find the text he is working on in one click. Ten seconds: he sees the shelf, the texts are where he left them, and the page does not get in the way. He should be able to tell it apart from a blank template at a glance.
2. **A stranger who searched for one text** (for example "Meditations Hays" or "Faith in Mind text"). Assumption, not data (there is no traffic yet): they probably land on a text page first, so the home page serves the second visit and the one who wants to look around. Ten seconds: they see that this is a serious edition, not a scan dump, and that the text they want is here, complete and free.
3. **Someone who heard of the project** from a friend, a post or a link to a passage. Ten seconds: they understand the idea (a few texts, read slowly, with notes and links to lines) and feel invited to start one, with no sign-up or pitch.

What all three should feel: that someone chose these texts and set them carefully; that nothing is asking them for anything. What they should be able to do straight away: open a text; open the shelf in full; read the one-paragraph "how to read here".

## What the page must say

- **What this is, in a sentence:** a small library of wisdom texts, from Zen poems to the Stoics, each made into an edition to read slowly.
- **The texts:** all eight, with translator, a reason to read, and length.
- **Complete, free to read, linkable to the line, downloadable:** each text is whole, not an excerpt; free to read here; every line has a number to link to; each has an EPUB. "Complete" describes the texts, not the library: [brand.md](../brand.md) says "curated, not complete", and the page keeps both.
- **Notes in the margin:** a reader's notes sit beside the passage they are about; on *Meditations* these are Rufus's own.
- **Who is behind it:** Rufus Pollock with AI assistants, as part of Life Itself, with a pointer to `/about` for copyright and how editions are made.

## What it must not be

- A marketing page: no feature cards, no triad of benefits, no "why choose", no buttons shouting for attention.
- A catalogue: no grid of covers, no filter, no search, no "browse by" sidebar. The shelf is a short list, with headings only as far as they help.
- A sermon: no daily quote or aphorism set apart for the day, no exhortation ("begin your practice"), no praise adjectives about the texts ("beautiful", "timeless", "profound"). The opening line is the first line of a text, with its source named beneath it; it is not commentary.
- A temple gift shop or a wellness app (see the design brief's "not" list).
- Longer than needed to choose. Measured, not felt: the opening line and the sentence fit one 1280px screen, and the shelf takes no more than about two 390px screens.

## What the references do

From a survey of the home pages of Standard Ebooks, SuttaCentral, Sefaria, Emergence, Public Domain Review, Fitzcarraldo, 84000, Lotsawa House and Reports That Matter (some blocked or not rendered; Poetry Foundation returned 403, SuttaCentral an unsupported-browser page):

- **Standard Ebooks** opens on a single sentence of purpose ("Free and liberated ebooks, carefully produced for the true book lover") and one button to the library. No book text on the front.
- **Sefaria** opens on a plain heading and a list of categories, each with a one-line description. Texts are named, not shown.
- **84000** and **Lotsawa House** open on the institution's statement, then a short list of recent texts with blurbs and a search.
- **Reports That Matter** opens on the problem in one sentence ("Reports that shaped history are still trapped in PDFs") and the solution in a second; then a plain list with cover thumbnails.
- **Emergence** and **Public Domain Review** lead with one featured piece and a short blurb, image-led.
- **Fitzcarraldo** leads with the books (covers, prices, "add to basket"); the front is a shop.

The pattern worth taking: a plain statement of purpose in the first lines, a short list that names each text with a line of blurb, and nothing on the front that is not a text or a way into one. The best ones (Standard Ebooks, Reports That Matter) do not show the texts on the front, which is a choice the Sutras page can make differently: the first words are the text itself.

## Opening line: three options

1. **A line from a text, as the first words.** "The Supreme Way is not difficult / If only you do not pick and choose." (*Faith in Mind*, the first stanza, verbatim.) The page starts inside a teaching, which is the design brief's "the first screen shows words from a teaching". Attribution small beneath it.
2. **A line from a text, Seneca's.** "It is not that we have a short space of time, but that we waste much of it." (*On the Shortness of Life*, verbatim.) Strong and well known, but it is already the current page's most-quoted line, it is a claim about the reader, and it leads with a Stoic text, which tilts the library.
3. **A plain statement in the site's own voice.** "Eight old texts, each complete, set to be read slowly, with a link to every line." It says what the site does in one breath. It is honest and could not be mistaken for another site, but it is a description, not a teaching.

**Chosen: option 1**, because it puts the reader inside a text on the first screen, which is what the design brief asks for, and it makes the library's claim by showing one of its texts rather than describing them. The risk is that it reads as a quote for the day; the fix is that it is named and linked to its edition at once. Options 2 and 3 are the fallbacks; the choice is listed as a `needs-rufus` question, with this default taken.

## Copy rules

- Plain, quiet, personal (from [brand.md](../brand.md)). First person singular only where Rufus is speaking, and then sparingly.
- No praise adjectives. No "explore", "discover", "dive in", "journey". No exclamation marks. No emoji.
- Every quotation is verbatim from the edition it is taken from; `scripts/check` enforces this.
- **Reading time** is shown on the page. Method: the words of the edition's page (text, introduction and notes, markup stripped) divided by 240 words a minute, then rounded to the nearest 5 minutes. Computed by script on the day, not by hand. It is a reading time for the whole edition, not the poem alone. *Faith in Mind*'s introduction says "ten minutes to read through", which the rule gives too.
- Figures as computed on 2026-11-20: *Faith in Mind* 10 min (2,863 words); Shodoka 15 (3,573); Mumonkan 45 (10,311); Diamond, Thich Nhat Hanh 30 (6,747); Diamond, Red Pine 35 (8,186); Dhammapada 110 (26,475); Seneca 50 (12,587); Meditations 235 (56,754). If an edition changes, the figure is recomputed in the same commit.

| Text | Length | Note |
|---|---|---|
| *Faith in Mind* | about 10 min | Seng Ts’an (attributed); Sheng-yen with Kennedy |
| *Shodoka* | about 15 min | Yung-chia; Aitken and Shimano |
| *The Gateless Gate* (Mumonkan) | about 45 min | Wumen Huikai; Sekida, with the Chinese |
| *The Diamond Sutra* (Thich Nhat Hanh) | about 30 min | Thich Nhat Hanh |
| *The Diamond Sutra* (Red Pine) | about 35 min | Red Pine (Bill Porter) |
| *The Dhammapada* | about 110 min | Thanissaro Bhikkhu, 2011 revised |
| *On the Shortness of Life* | about 50 min | Seneca; Basore |
| *Meditations* | about 235 min | Marcus Aurelius; Hays |

Note on the goal document: it still says the Red Pine Diamond is "marked partial". The page is complete (all 32 chapters, status published), so the shelf does not mark it partial; that goal line is stale (bead sutras-m2v.6.7).

## Shelf: order and grouping

- Grouped by tradition, as now: Zen, Mahayana, Early Buddhism, Stoicism. Headings only; each group a short run of entries.
- **Order** (chosen, default): *Faith in Mind* first, because it is the test page and the shortest; then the rest of the tradition order as now. Alternative: by length, shortest first, which makes the shelf read as "start here". Rufus's call; listed.
- Each entry: title (the link), one quiet line (author, translator), one line reason (from the edition's own description, kept to one sentence), reading time in the same quiet line.

## Reading here: the short section

Three short items, each one or two sentences, in order:

1. **Every line has a number.** Click it to get a link to that line, such as `/faith-in-mind#1` or `/meditations#1.1`. Numbers do not change once published.
2. **Notes sit in the margin.** Translators' and editors' notes beside the passage they are about; on *Meditations*, Rufus's own notes.
3. **Each text is also an EPUB.** Download from its page, for an e-reader.

## About and footer

- One short paragraph on the home page, linking to `/about`: who makes it, copyright in one line, and that the source is on GitHub.
- `about.md` stays the full answer (purpose, who it is for, copyright, what it is not). Its text is the vision and was accepted; it gets only a light edit if the landing copy changes a fact.

## The design track: what the landing page needs from it

The page is built in the current reading look (`data-rs-theme="personal"`, EB Garamond, IBM Plex Mono labels, warm paper, one red accent) and does not invent a competing look. It needs from the design:

1. **The opening screen as a place, not a box.** Today's "In brief" box (tinted, red rule) is the most likely thing to change. The home page puts the first words in a large serif setting with room around it. Hook: `.rs-home .rs-lead`.
2. **Room for one image per text.** Each shelf group is wrapped in `.rs-shelf`, so a picture can be given room beside an entry without touching the others. None is added yet: the page has no image until the design decides the licence and caption for each text.
3. **Colour.** The accent is the theme's `--rs-accent`. To change it for the home page only, set it on `.rs.rs-home[data-rs-theme="personal"]` in `css/home.css`; the edition pages are untouched. The warm red, the Fitzcarraldo blue and the gold-on-indigo idea can be tried there.
4. **A mark or a wordmark** would replace the plain "Sutras" kicker. Hook: `.rs-home .rs-kicker`.
5. **Type.** The lead and the shelf titles are the only display sizes on the page. Changing the display face is one variable (`--rs-display`, already defined by the theme).

## Alternatives

Three sketches of the opening screen at 1280px, committed as screenshots under `docs/design/landing/` (see the README there):

- **A, text first (shipped):** the *Faith in Mind* line large, attribution small, one plain sentence of what this is, then the shelf begins.
- **B, statement first:** the current "In brief" box with the sentence at its head, then the shelf. This is what is live now.
- **C, image led:** a public-domain ink landscape (Sesshū, *Haboku Sansui*, 1495, from `docs/design/shots/`) beside the first line. Shows what a picture could do; not a candidate for the live site until the licence and the caption are checked for each text.

## Done-check for this stage

- This brief is critiqued by a fresh subagent and the critique is applied (see the bead comment).
- Home page live; screenshots at 390px and 1280px read well (looked at).
- `scripts/check` passes.
- Alternatives committed; `needs-rufus` bead filed with the live URL, the screenshots and the three choices (opening line, which line of which text, shelf order).

## Open questions (all go to Rufus as a `needs-rufus` bead, with the default)

1. Opening line: option 1 (default), 2 or 3.
2. Shelf order: tradition with *Faith in Mind* first (default), or shortest first.
3. Whether the home page should show the first line of each text beneath its title (default: no; the shelf stays short).
