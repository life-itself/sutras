# How notes live with the text: options

Status: options paper and recommendation, 2026-11-20. Bead sutras-m2v.9.1, workstream [6 Annotation](plans/workstreams/6-annotation.md). Builds on decision 0001: D3 (Rufus's notes are data) and D7 (readers' notes invite-only; a Hypothesis trial early, our own later). Revised after a critique by a subagent.

## The answer in short

There are three ways for notes to live with a text. They use the same shape of note, so we can move from one to the next without starting again.

1. **Notes file (now).** Rufus's notes are kept in the repo, one file per text. Each note is a few quoted words plus an optional comment. A script checks that every quote is still in the text; the page highlights the words and shows the note in the margin, beside the translator's footnotes. Nothing to run or pay for. Built alongside this paper; first used for Rufus's notes on *Meditations*.
2. **Hypothesis (a trial, later).** An established free service for notes on any web page. One line on the page adds its note-taking sidebar. Cheap to try with a few invited readers; not the long-term answer, because the notes live on its servers, its sidebar is not our margin, and every reader needs a Hypothesis account.
3. **Our own notes service (only if readers want to write).** A small service of our own that stores readers' notes in the same shape and shows them in the same margin as Rufus's. Weeks of work, then ongoing care: sign-in, privacy, moderation.

**What Rufus decides:**

- **Now:** nothing blocks. The notes format (D3) is taken as agreed; say if the example below looks wrong.
- **For the Hypothesis trial:** create a Hypothesis account and a private group, or say no to the trial (a `needs-rufus` bead).
- **After the trial:** Hypothesis, our own service, or neither.

## What a note is

A note is a quoted passage plus an optional comment. A note with no comment is a plain highlight. In the notes file:

```yaml
- id: fim-8-dream
  passage: "8"                      # the passage it is in, as in /faith-in-mind#8
  quote: A dream, an illusion, a flower in the sky
  note: Sheng-yen saw these flowers himself, all his life.
  by: Rufus Pollock
  date: 2026-11-20
```

(Illustrative: Rufus has not written this note.) Two optional fields, `prefix` and `suffix`, hold a few words before or after the quote; they are only needed when the same words appear twice in one passage.

Why notes are kept apart from the text:

- **The text stays clean.** Nothing is written into the edition. Translators' footnotes stay footnotes.
- **Notes survive corrections.** A note points at words, not at a position. Fix a typo elsewhere in the stanza and the note still finds its words. If the quoted words themselves change, the check fails and names the note, so it is fixed by hand. A note is never quietly shown against the wrong words.
- **The passage narrows the search.** A phrase that occurs five times in a book usually occurs once in a passage. If it occurs twice even there, the check fails until a `prefix` or `suffix` tells them apart; it never guesses.
- **The same shape serves everyone.** It is the standard shape for web annotation (W3C), used by Hypothesis, by wilber-wiki's prototype and by Reports That Matter. Rufus's notes now, readers' notes later, and other projects can all use it.

Why not footnotes, which the reading page already shows in the margin? Footnotes are written into the text, so the edition is no longer just the translation; they can't be switched off; they mark a point, not a span of words; and they can't be checked. For notes that are commentary rather than editing, a notes file is better. *Faith in Mind*'s three editors' notes can stay footnotes, since they gloss the translation; they could move to a notes file later.

## The three options

### 1. Notes file

- **How it works.** `annotations/<slug>.yaml` per text. `scripts/notes` checks every quote against the edition and writes a small generated JavaScript file holding the notes. The edition page loads that file and `js/notes.js`, which finds each quote on the page, highlights it, and shows the note in the margin (on a phone: under the line, when its mark is tapped).
- **Why a generated script file.** Flowershow will not let a page read a data file from the site (a missing web-server header; Flowershow issue #1373, found by wilber-wiki). It will load a script. So the notes travel as a script, generated from the YAML and committed with it.
- **How Rufus adds a note.** Edit the YAML, or tell an agent "this line, this thought". If that becomes a drag: select words on the page, write the note, copy out the YAML (the brief's stage B; kept in the browser, no server).
- **Cost.** A few days, already under way. Nothing to run. Only people with access to the repo can write.

### 2. Hypothesis

[Hypothesis](https://web.hypothes.is/) is a non-profit's open service for notes on web pages, widely used in teaching. A site adds one script tag; readers who have an account select words and write notes in a sidebar. What it gives us ([config](https://h.readthedocs.io/projects/client/en/latest/publishers/config.html), [groups](https://web.hypothes.is/help/annotating-with-groups/)):

- **A quieter look.** A "clean" theme removes most of its buttons; the sidebar can start closed; an experimental option sets its colours and fonts. It is still their sidebar sliding over the page, not notes beside their lines.
- **Private groups.** Anyone can make one; members join by an invite link; only members read and write; the group's creator can delete notes. (The brief said "restricted group"; those, readable by all and writable by members, are only made by Hypothesis for partner publishers on request, so a private group is what we can do ourselves.)
- **Our notes are retrievable.** Its public interface returns each note with its quote and the words around it, the same shape as ours, so notes written in a trial can be copied into the notes file.
- **Costs and catches.** Readers need a Hypothesis account and an invite: a real barrier for someone who came to read a poem. Phone use is unknown; check it in the trial. Notes live on Hypothesis's servers (its terms promise at least 30 days' notice to download them if the public service ends). Group notes stay their authors'; public notes are dedicated to the public domain. The [terms](https://web.hypothes.is/terms-of-service/) ask anyone using the service "within a commercial offering or entity, be it free or otherwise" to make an agreement; Sutras is free and non-commercial, but ask Hypothesis before going beyond a trial. Readers' data goes to a third party.
- **Cost (guess).** An afternoon to set up on one text, once Rufus has made the group. No fee.

### 3. Our own notes service

- **What it is.** A small web service storing readers' notes in the same shape as the notes file. Guess: a Cloudflare Worker (a small program on Cloudflare's network) with its database, as Reports That Matter uses for its reader highlights. The same `js/notes.js` shows readers' notes in the same margin, told apart from Rufus's.
- **What it needs.** Selecting words on the page and writing a note (hand-made, or with Recogito's text annotator, an open-source tool for exactly this which needs storage behind it). Sign-in for invited writers; the simplest kind for a reading site is a link sent by email, which needs an email-sending service (free tiers exist; check that it stays inside "no new paid services"). Moderation: with invited writers only, a delete button for Rufus is enough at first. A privacy notice, because we would hold readers' email addresses. A regular export of readers' notes into the repo, so nothing is lost if the service is switched off.
- **Cost (guess).** One to two weeks to a usable prototype; free tiers at our size. Then the long tail (sign-in problems, deleted accounts, privacy requests, someone to answer when it breaks), which never ends and is the real cost.

A fourth way was looked at and set aside: readers' notes through GitHub (comments per passage, or notes sent as changes to the notes file). No service to run, but every reader needs a GitHub account, which suits developers, not readers of sutras.

## Comparison

| | Notes file | Hypothesis | Our own service |
|---|---|---|---|
| Who writes | Rufus, and agents for him | Invited readers with a Hypothesis account | Invited readers |
| Where notes live | Our repo | Hypothesis's servers | Our database, copied to the repo |
| Look | Ours: words highlighted, note beside the line | Theirs: a sidebar over the page | Ours, as the notes file |
| On a phone | Tap the mark, the note opens under the line | Unknown: check in the trial | As the notes file |
| Reader needs an account | No | Yes, to read or write group notes | To write only |
| Work (guess) | Days | An afternoon | One to two weeks, then upkeep |
| Ongoing care | None | Theirs, plus moderating our group | Ours: sign-in, privacy, moderation |
| When the text is corrected | The check names any note that broke | Their fuzzy matching; lost notes are listed as "orphans" | As the notes file, once copied to the repo |

## Recommendation, in stages

1. **Now: the notes file, built and shown.** First on a demo page with passages from *Faith in Mind*, then Rufus's own notes on *Meditations* (his quotes and comments on the Hays translation, from rufuspollock.com) on the *Meditations* edition, which is goal item 4. The brief named *Faith in Mind* and Seneca; the Monday goal moved the first real notes to *Meditations* because those are notes Rufus has already written. Seneca (67 footnotes) stays the test of a crowded margin.
2. **When Rufus wants to write notes himself:** select-and-write in the page, with the YAML copied out. Only if editing the file or asking an agent is a drag.
3. **Milestone 2: the Hypothesis trial.** One text, a private group, the clean theme, Rufus and two or three friends, a week; look at it on a phone. D7 put the trial on a preview site; decision 0001 since made the live site its own preview, so it goes on one live text. We learn whether people write notes at all, how long they are, whether they answer each other.
4. **Milestone 4: our own prototype, only if the trial shows readers write.** If nobody writes in the trial, stop after step 3. Otherwise build the prototype, then Rufus decides between Hypothesis and our own with both in hand; that decision is recorded in `docs/decisions/`, and the lessons go to `docs/lessons/` for wilber-wiki and Open Literature. The working guess, unchanged from the brief: our own wins on look and on notes living with the text; Hypothesis is the fallback if the upkeep looks too heavy.

## Questions the brief asks

- **Do notes still find their passage when a text is corrected?** Yes, unless the quoted words change; then the check fails and names the note. Passage ids never change once published (D6); if a passage id goes missing, the check fails too.
- **How do margin notes work on a phone?** Like the footnotes: a small mark after the line; tap it and the note opens under the line.
- **How are Rufus's notes told apart?** Editors' notes are footnotes, with numbers. Rufus's notes are highlighted words with a mark (not a number) and his initials on the note. Readers' notes, when they come, get a different highlight and their author's name. A reader can switch notes off and read the clean text.
- **Who may write, and are readers' notes public?** Invite-only (D7). Proposed: readers' notes are visible to the group only, unless the writer makes one public. Decided when step 4 starts.
- **Can a note link to another passage?** Yes; a note can hold a link such as `/shodoka#12`. Gathering those links across notes is a seed of a concept index.
- **What does wilber-wiki need, and can one script serve both?** Yes, one script can; see below.

## Risks

- **Quotes break when an edition is corrected.** The check names the note; the fix is a one-line edit. Annoying, never wrong.
- **The page and the file differ.** On the page, Markdown markup, footnote numbers and line breaks are gone; the check and the page script both ignore them the same way, tested on real texts.
- **Crowded margins.** Where a stanza has a footnote and several notes, they stack in order down the margin. Seneca's 67 footnotes will test this.
- **Notes are public.** Rufus's notes are on the live site as soon as they ship, and in the repo's history for good.
- **Only with JavaScript.** Notes are added by script, so readers without JavaScript and search engines don't see them, and the EPUB doesn't have them (proposed: leave them out of the EPUB for now; a "with Rufus's notes" EPUB later). Highlights are invisible to screen readers, so each note's mark is a real button labelled with the quoted words.
- **Hypothesis:** its look, its accounts, its servers, its terms.
- **Our own service:** the long tail, for as long as it runs. Keep it invite-only and copy notes to the repo, so it can be switched off without loss.

## What wilber-wiki and Open Literature need

- **wilber-wiki** wants the same for Wilber's books: Rufus's notes as quote plus comment beside the text, later shared with a group. It already has the quote shape and a first display script. It lacks a check (its quotes are not verified), it pastes the notes into each page by hand, and its notes do not share a margin with footnotes. `scripts/notes` and `js/notes.js` contain nothing Sutras-specific beyond the reading page's class names, so they can be copied across once they work here (D11: extract when another project uses them). Its copyright question limits it to a private or group site; a Hypothesis private group or our service's group notes both fit.
- **Open Literature** (the wider idea Sutras is the first test of) needs the rules more than the code: passage ids a reader would cite; notes kept apart from the text, keyed by passage plus quote; a check that fails loudly; each layer (text, translation, editors' notes, readers' notes) in its own file. What this experiment should report back: how often notes broke when texts were corrected, whether the notes file was pleasant to write, and whether readers wrote anything.

## Appendix: technical notes and precedents

- **The shape in standard terms.** A W3C Web Annotation whose target is a FragmentSelector (the passage id) refined by a TextQuoteSelector (`exact` = `quote`, with `prefix` and `suffix`), and whose body is the comment. We write small YAML and can export standard JSON-LD for anyone who wants it, as Reports That Matter plans to.
- **Highlighting.** `js/notes.js` paints highlights with the browser's CSS Custom Highlight API, which colours a span of text without changing the page's HTML (in all current browsers since 2025), and falls back to wrapping the words in `<mark>`.
- **Hypothesis config.** One script tag (`https://hypothes.is/embed.js`) plus a JSON block: `theme: "clean"`, `openSidebar: false`, `showHighlights`, `groups` (limit to our group), experimental `branding` (accent and background colours, fonts) and `externalContainerSelector` (put the sidebar in our own element). Reading public notes through its API needs no key. Its own server can be self-hosted, but needs Postgres and Elasticsearch: far too heavy for us. Its pricing page lists education seats only, no publisher plan.
- **How Hypothesis re-finds notes.** It stores three anchors per note (a path through the page's HTML, a character position, and the quote) and tries them in turn, ending in a fuzzy search; a note that finds nothing is shown as an orphan, not dropped.
- **SuttaCentral** keeps every text as numbered segments (`dhp179:1`, `dhp179:2`, …) and keeps the original, each translation, the translator's comments and the HTML layout as separate files keyed by the same segment ids. We hold this for the Dhammapada in `library/dhammapada/sujato/` (`root/`, `translation/`, `comment/`, `html/`). It is the clearest example of layers joined on a passage id: a comment never touches the text, and a new layer is a new file. Our passages are coarser (a stanza or section), which is why we add the quote.
- **Sefaria** treats a commentary as a text in its own right ("Rashi on Genesis 1:1:1") and records links between references, shown beside the verse. The lesson for later: notes have ids, so they can be linked to and gathered.
- **Reports That Matter** anchors everything people add (editorial highlights, corrections, reader marks) as "paragraph id plus a quotation", checks each by script, and fails the build on a quote that no longer matches: "a stale anchor should degrade to 'this paragraph, roughly', never to a silent lie about which words were quoted." Its highlight design keeps readers' highlights in the browser with an export, and leaves accounts (by emailed link) to last.
- **wilber-wiki** built a first display (`assets/annotator/annotator.js`): finds each quote across the page's text, treating curly and straight quotes and dashes alike, and puts notes in a margin column. It found the Flowershow data-file problem and fell back to notes pasted into the page. `js/notes.js` starts from it.

## Sources

- wilber-wiki: `docs/annotation-system.md`, `docs/annotatable-reading-layer-vision.md`, `assets/annotator/annotator.js`.
- Reports That Matter: `docs/plans/2026-08-21-highlights-design.md`, `docs/design/2026-10-03-annotation-format.md`.
- Hypothesis, read 2026-11-20: [embedding](https://h.readthedocs.io/projects/client/en/latest/publishers/embedding.html), [config](https://h.readthedocs.io/projects/client/en/latest/publishers/config.html), [groups](https://web.hypothes.is/help/annotating-with-groups/), [publisher groups](https://web.hypothes.is/help/publisher-groups/), [API authorisation](https://h.readthedocs.io/en/latest/api/authorization/), [terms](https://web.hypothes.is/terms-of-service/), [pricing](https://web.hypothes.is/pricing-page/).
- W3C [Web Annotation Data Model](https://www.w3.org/TR/annotation-model/) (2017).
- SuttaCentral's data in `library/dhammapada/sujato/`; Sefaria's linked commentary.
- Flowershow page scripts reference (`flowershow-app/docs/reference/page-scripts.md`); Flowershow issue #1373.
