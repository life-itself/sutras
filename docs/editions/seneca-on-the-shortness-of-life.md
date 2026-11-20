# On the Shortness of Life — how this edition was made

Edition: `/seneca-on-the-shortness-of-life.md` (live at https://sutras.lifeitself.org/seneca-on-the-shortness-of-life). Made 2026-11-20 by an AI agent (Claude) for milestone 1, track `seneca`, bead sutras-m2v.7.4.

## Sources

- `wikisource/`: the source, as fetched on 2026-11-20 from https://en.wikisource.org/wiki/On_the_shortness_of_life (raw wikitext of the index page and the twenty chapter pages, `action=raw`). Wikisource's header gives: translated by John W. Basore, Loeb Classical Library, London: William Heinemann, 1932. It does not say what it was transcribed from; its text is the Forum Romanum text below with that page's OCR slips corrected (see the list under "Where the two copies differ").
- `forumromanum-brev_e.html`: a second witness, used for checking. The Forum Romanum (Corpus Scriptorum Latinorum) page that the earlier version of our page was made from and linked to. The site is gone (the domain now redirects elsewhere), so this is the Internet Archive copy of 2006-12-07: http://web.archive.org/web/20061207132316/http://www.forumromanum.org/literature/seneca_younger/brev_e.html. It names the same edition.
- Neither copy is the printed book. The Loeb scans on archive.org (`moralessays0002sene`, `moralessays0002sene_o1d8`) are lending-only and their text could not be read; an item titled "L 254 … De Brevitate Vitae" turned out to be the *Epistles* volume II. So the edition has not been checked against a printed page.

## How it was made

1. `wikisource_to_md.py` turns the wikitext into Markdown: paragraphs as on Wikisource, Basore's `<ref>` notes as footnotes, the Virgil quotation in chapter 9 as a block quote. It drops the Wikisource page furniture and Wikisource's own English glosses of the Latin and Greek in the notes (`{{tooltip}}`: contributors' additions, not Basore's).
2. Each chapter became `<h3 id="N">` with its Roman numeral, under "## The essay". **Passage ids are chapter numbers, 1 to 20** (`/seneca-on-the-shortness-of-life#17`). The printed Loeb numbers sections within each chapter (cited as 13.8 and the like), but neither online copy carries them, and guessing their boundaries from the Latin would risk ids that disagree with the book. Section ids can be added later without breaking these (bead filed).
3. The fixes below were applied, quotation marks and apostrophes made curly.
4. `compare.py` compares the edition with the Wikisource text word for word, including where each note marker sits and the words of every note, and fails on any difference not listed here. Result on 2026-11-20: 20 chapters, 47 notes from Basore, 0 unlisted differences.

## Every change to the words

Against the Wikisource text:

- **Note on Liternum restored** (note 40, chapter 17, after "his ambition will take delight in stubborn exile."): "Disgusted with politics, he died in exile at Liternum." Wikisource has lost this note and attached the next one there instead. Followed Forum Romanum.
- **Note on Caligula moved back** (note 41, chapter 18): its marker belongs after "he knew that the Roman people were alive", as in Forum Romanum; the note is about Caligula's wish that the Roman people had one neck.
- **Note on Antony moved** (note 10, chapter 4): from after "there was Paulus," to after "a woman in league with an Antony.", as in Forum Romanum. The note is about Mark Antony and Iullus Antonius, not about Paulus.
- **Opening quotation mark added**, chapter 17: "the anxious thought comes over them: “How long will these things last?”" Both copies have the closing mark only.
- **Doubled full stop** in note 29 ("societatem.." to "societatem.").
- Straight quotation marks and apostrophes made curly. Dashes, "to-day", "close-fisted" and British spellings ("labour", "favour") as in the source.

Left as in the source, though possibly slips: "when a gladiatorial exhibition is been announced" (chapter 16; both copies; "has been" likely); Greek in notes 2, 4 and 5 as transcribed, not checked against the book.

The earlier version of our page (from Forum Romanum) had three slips that this edition no longer has: "Jove39" (a note marker run into the text, chapter 17), "lake delight" for "take delight", and the chapter XVII heading run into chapter XVI.

Not Basore's words (ours): the headings, the in brief, the editors' introduction, the four editors' notes, About this translation, Source and licence.

## Where the two copies differ

Forum Romanum reading first, Wikisource (followed) second. All are OCR slips in Forum Romanum: "closefisted" / "close-fisted"; "When be had cut" / "When he had cut"; "the refuse. have been" / "the refuse, have been"; "nay be censured" / "may be censured"; "to our shame I we labour" / "to our shame! we labour"; "he then believed" / "He then believed"; "the Roman's who" / "the Romans who"; "ever age" / "every age"; "gone ore them" / "gone before them"; "lake delight" / "take delight"; "When we are" / "when we are"; "ether matters" / "other matters". In the notes: note 1 ends "xv." in Forum Romanum, "xv. 18. 4" in Wikisource; Forum Romanum has the Liternum note, Wikisource does not.

## Notes: Basore's and ours

- The brief for this track said 67 footnotes. There are 47: the old page had 47, Forum Romanum has 47, Wikisource 46 (one lost, above).
- **Basore's 47 notes are unlabelled**, as in the book. **Our four notes start with "*Editors’ note.*"**, the same label *Faith in Mind* uses. In the Markdown, Basore's are `[^1]`..`[^47]` and ours `[^e1]`..`[^e4]`, but the page and the EPUB number them all in one sequence, so the label is what tells them apart. A distinct style for editorial notes is asked of the site track (bead filed).

## Facts used in the introduction, the editors' notes and About this translation, and where each comes from

- Paulinus in charge of the grain supply (*praefectus annonae*), probably a relative of Seneca's wife Pompeia Paulina; the essay written "in or about A.D. 49": Basore's note 1.
- *occupati*, "the engrossed"; *otiosi*, "the leisured", defined at the start of chapter 14: Basore's notes 14 and 25.
- Seneca c. 4 BCE – 65 CE; Stoic philosopher, statesman, dramatist; exiled to Corsica in 41, recalled in 49 to tutor Nero: English Wikipedia, "Seneca the Younger", read 2026-11-20.
- Usually dated to about 49; the *pomerium* argument (Claudius extended it in 49/50); Miriam Griffin's reading of that passage and her suggestion of 55 as an excuse for Paulinus to retire early; the outline (chapters 2–9, 10–17, 18–20): English Wikipedia, "De Brevitate Vitae (Seneca)", read 2026-11-20.
- Basore 1870–1959: Wikidata Q59631295 (birth and death years), read 2026-11-20; the Wikisource copyright tag `PD-US-no-renewal|1959|1932` gives the same death year.
- Loeb Classical Library, *Moral Essays* volume II, 1932, London: William Heinemann: Wikisource header; volume II from the archive.org Loeb listings (`moralessays0002sene`, "Moral essays", volume 2). New York: G. P. Putnam's Sons as co-publisher of the set: Open Library edition OL6716657M (LCCN 28016432, "W. Heinemann, ltd.; G. P. Putnam's Sons", London and New York), read 2026-11-20.
- "47 notes", "20 chapters", "about an hour" (10,700 words): counted by script.

## Copyright

US: **probably** public domain. Wikisource tags it `PD-US-no-renewal` (published 1932, not renewed); we did not check the renewal records ourselves. The set was published in London and New York (Open Library record above), so it counts as a US publication and the 1994 URAA restoration for foreign works should not apply. Against that: HathiTrust (catalog record 001182035, checked 2026-11-20) shows volume 1 (1928) as full view but every copy of volume II as "Limited (search-only)", i.e. not (yet) cleared as public domain. Hence "probably" on the page. Basore died in 1959, so in life-plus-70 countries (UK, EU) it is in copyright until 31 December 2029. Published in full under decision 0001 point 5, with the status stated on the page. Wikisource's transcription adds no copyright of its own to a public-domain text; its English tooltip glosses (CC BY-SA) are not used.
