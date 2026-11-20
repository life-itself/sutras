# Writing an introduction

Status: v1, 2026-11-20, written by the editorial track after reading and revising the eight editions as a set ([review](../2026-11-editorial-review.md)). The brief is [3-editorial.md](../plans/workstreams/3-editorial.md); the voice is [brand.md](../brand.md). The worked example is *Faith in Mind*, the first edition and still the best introduction of the eight. Rufus has not yet edited an introduction; when he does, his changes go into this guide.

## What an introduction is for

A reader has arrived at a text they may never have heard of. In 150–300 words, before the text itself, tell them three things: what this is, why anyone still reads it, and how to read it. Then get out of the way. The introduction is ours and says so; it is a reader's note left in the front of a book, not an encyclopaedia entry and not a teacher's talk.

## The shape

Every edition page has the same six parts (see [making an edition](making-an-edition.md)). The two that are written, not transcribed, are the in brief and the introduction.

**In brief** (two or three sentences, 30–60 words, inside `<p class="rs-inbrief">`): what it is; who it is attributed to, with the doubt if there is one; what this edition holds (whose translation, complete or not); how long it takes to read straight through. Example: "A short Ch’an (Zen) poem on the mind that does not pick and choose. Tradition gives it to Seng Ts’an, the Third Patriarch, though he probably did not write it. Complete, in Master Sheng-yen’s translation; ten minutes to read, though Sheng-yen taught from it only on retreat."

**Introduction** (150–300 words, three or four paragraphs):

1. **What it is, who and when.** Title, original title in its own script, the kind of thing it is (a poem, a sutra, an essay, notes to himself), its length in this translation, who wrote it and when. If the attribution is doubtful, say so in the same breath and name who doubts it: "Tradition gives it to Seng Ts’an… The attribution is doubtful: Sheng-yen himself reports that scholars doubt it."
2. **What it says.** The text's own first lines usually carry its claim; quote them, verbatim, and link to the passage. Then the shape of the whole in a sentence or two: what it keeps coming back to, how it turns.
3. **Why it has lasted, or how its translator used it.** Not our praise but someone's use: Sheng-yen taught it only on retreat; Red Pine changed his mind about what it was about; the Mumonkan is still used in Rinzai training. A reader's own judgement is allowed when it is plainly ours ("We find his the plainer of the two translations here").
4. **How to read it.** One concrete way in: straight through once, then a stanza a day; aloud; one case and then leave it alone. Say where the notes stand ("The three notes are ours; they can wait for a second reading") and name the sister text in the library if there is one.

Sign it: `<p class="rs-signed">Editors’ introduction, drafted with an AI assistant. Month YYYY.</p>`.

## The voice

- Plain, quiet, personal. Short sentences. Say what the text does, not what it is like.
- No praise adjectives: not "profound", "masterpiece", "best-loved", "timeless". If the text is good the reader will find out. A translator's praise may be quoted once if it says something specific; "one of the masterpieces of early Buddhist literature" says nothing and was cut.
- Not a scholar: Taishō numbers, manuscript sigla and editions used go under About this translation. Not a preacher: do not retell the teaching in the teaching's own register ("the fool's path leads to suffering and further entrapment"). Describe the move the text makes; let the text make it.
- British spelling in our prose; quotations keep their own.
- Numbers: counts of verses, chapters, cases, sections and books in digits (64 verses, 48 cases, 423 verses); other small numbers in words (three notes, one night).
- Names: follow the translator's romanisation on that page, so the page reads as one, and give the pinyin in brackets at a person's first mention so the texts can be connected: "Hui-neng (Huineng)". Hyphenate Wade-Giles in our own prose.
- Dates: "about 49 CE" in prose, "c." only in frontmatter; "CE" once where the century is not obvious.
- Time to read, not word counts: "ten minutes", "half an hour", "about an hour", "two hours straight through, though it is made for a verse at a time".

## Facts

Every date, name and attribution comes from a source you have read: the translator's own introduction or notes (the best source, since it is on the page), the book's front matter, or a reference you fetched and recorded in `library/<slug>/NOTES.md` under "Facts and where each comes from". Never from memory. Things that went wrong in the first eight and were caught on review:

- A name copied from a web page with a typo in it ("Ruth Stout McCandless" for Strout). Check names against a catalogue.
- A claim stronger than its source ("dropped out of the Chinese canon" when the source said the canon stopped including it; "first printed in a book for chanting" when the source said it was later reprinted in one).
- A traditional lifespan given as fact (Zhaozhou, 778–897). Write "traditionally".
- A story given as biography (Yung-chia's one night with Hui-neng). Write "the story told of him".
- A copyright status taken from one tag on Wikisource. Say "probably" and what each source says.

If you cannot support it, cut it. A shorter introduction with nothing wrong in it beats a fuller one with one unsupported sentence.

## Quotations

Every quotation is verbatim from the text on the page or from a named source, and the ones from the text link to their passage. Check them with grep before you ship, and again after any edit to the text. The editors' highlights (`annotations/<slug>.yaml`) are checked by `scripts/notes`; introductions are not yet checked by script (bead sutras-m2v.8.4), so check them by hand.

## Process

1. Read the whole text, and the translator's introduction and notes.
2. Draft the in brief and introduction to the shape above. Record every fact's source in `NOTES.md` as you go.
3. Have a fresh subagent critique it with the brief and this guide in hand: voice, missing elements, unsupported facts, quotations checked by grep. Apply what is right.
4. `scripts/check`, ship, read it on the live page at phone width.
5. When Rufus edits it, keep his edit and note what changed here.

## Worked example: *Faith in Mind*

The introduction as it stands on the page (243 words), with what each paragraph is doing.

> *Faith in Mind* (in Chinese *Hsin Hsin Ming*, 信心銘) is a short poem from the Ch’an (Zen) tradition: 146 lines in this translation, ten minutes to read through. Tradition gives it to Seng Ts’an (Sengcan), the Third Patriarch of Ch’an, who by Sheng-yen’s account died in 606. The attribution is doubtful: Sheng-yen himself reports that scholars doubt it, and that some place the poem after the time of the Sixth Patriarch, Hui-neng (Huineng).

What it is, how long, who and when. The date is attributed to Sheng-yen, whose introduction is on the same page; the doubt is his too, so no outside source is needed.

> Its opening lines carry the theme: “The Supreme Way is not difficult / If only you do not pick and choose.” The rest returns to it through pairs: love and hate, for and against, right and wrong, stillness and activity, existence and emptiness. Its last stanza begins “The path of words is cut off”.

What it says, in its own words, first and last. One sentence on the shape of the whole.

> Sheng-yen, whose translation this is, did not comment on it as a scholar. He spoke on it only during seven-day retreats, as instruction for people in the middle of practice. He writes that it and the *Song of Enlightenment* are the most highly regarded of the poems on enlightenment, “because of the clear guidance they provide on the method of Ch’an”. One way to read it in that spirit: slowly, aloud if you can, a stanza at a time, without stopping to work out every term. The three notes are ours; they can wait for a second reading.

Why it has lasted, as someone's use of it rather than our opinion; the one quoted judgement is specific and attributed. Then how to read it, and where the notes stand.

> His own introduction follows the poem. The *Song of Enlightenment* is also in this library, as the [Shodoka](/shodoka).

Where to go next on the page and in the library.

What it does not do: no biography of Seng Ts’an beyond his death date, no history of Ch’an, no account of what non-duality means, no adjectives. Everything a curious reader might want next is further down the same page, in Sheng-yen's own introduction.
