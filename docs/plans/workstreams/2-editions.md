# 2 Editions — brief

Status: draft, 2026-11-20. Part of [workstreams](../2026-11-20-workstreams.md).

## Goal

Turn a source into a clean, faithful Markdown text with stable passage links and honest metadata. Cheap enough that an agent does one text in a sitting.

## What an edition file is

One Markdown file per text, at its public URL. It has:

- **Frontmatter:** `title`, `author`, `translator`, `date` (of the original), `tradition`, `source` (URL or book), `licence` (status of the translation), `status` (`draft` or `published`).
- **The text,** structured as the tradition structures it (chapters, cases, stanzas), with a link target on every passage (D6): the number a reader would cite, levels joined by dots (`4.3`, `11`), or stanza and paragraph numbers where there is no tradition. Ids never change once published.
- **Nothing else added to the words.** Fixes to obvious source errors (typos, OCR slips) are allowed and listed; silent rewording is not.

Beside it, in `library/<slug>/`: the source as fetched, and a short `NOTES.md` saying how the edition was made and what was fixed.

## The cleanup, step by step

1. Start from the source in `library/<slug>/`.
2. Structure: headings, stanza and line breaks, passage ids, footnotes as footnotes.
3. Typography: quotes, dashes, diacritics (Skt., Pāli, Chinese names) made consistent; original-language characters kept where the source has them.
4. Compare with the source: a script reports every difference in the words, so that each is either reverted or listed in `NOTES.md`. For a scanned source, also compare with a second edition if one exists.
5. Run the checks.

## Checks (what `scripts/check` must do; the Site workstream owns the script, from milestone 2)

- Frontmatter complete.
- Every passage has an id; ids unique; no id from `published-ids.txt` has vanished (the list is added to at publish).
- Internal links resolve.

This is deliberately far less than Reports That Matter's fidelity tooling, which exists for 500-page scanned PDFs. Our texts are short and mostly clean; the word-level comparison in step 4 is the fidelity check.

## Borrow

- Reports That Matter: passage ids as the product, the published-ids list from day one (`docs/decisions/0008`, `0012`; `docs/design/lessons/` in that repo), a per-text processing note.
- wilber-wiki: text normalisation rules in `verify_quotes.py` (curly quotes, dashes, whitespace) for the comparison script.
- `~/src/life-itself/library`: `books-for-bots` conversion and its `NOTES.md` habit.

## Order of work

*Faith in Mind* first (it defines the template). Then a one-page guide, `docs/guides/making-an-edition.md`, written from that experience. Then the other five existing texts, one agent each: Shodoka, Diamond Sutra (Thich Nhat Hanh), Seneca (footnotes, chapters), Mumonkan (cases, Chinese characters, the longest), Red Pine (kept, marked partial). Then new texts as Library supplies them.

## Done-check

- *Faith in Mind* passes the checks and its `NOTES.md` lists every change from the source.
- The guide exists and a fresh agent, given only the guide and a source, has made the second edition and it passes the checks.
- All six existing texts are editions.

## Open, decided inside the workstream

- Whether the Yogins of Ladakh dump is worth cleaning for Rufus's private use (default: no, parked).
