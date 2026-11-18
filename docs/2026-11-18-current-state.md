# Sutras: current state (2026-11-18)

Facts only, to feed a purpose-and-direction session.

## Inventory

Repo `~/src/life-itself/sutras` is flat: 7 text files, `README.md`, `config.json`, no folders. Last content change was 2022-12 (Red Pine); the repo was refactored to "just the content" in 2024-04 after an earlier Nuxt build. The only 2026 commit adds Umami analytics.

- `diamond.md`: Diamond Sutra, Thich Nhat Hanh translation, about 1,600 words. Frontmatter `title`; source URL in body.
- `diamond-red-pine.md`: Diamond Sutra, Red Pine (Bill Porter), about 600 words (looks partial or condensed). Frontmatter `title`; source is a book title only.
- `gateless-gate-mumonkan.md`: Mumonkan with Chinese characters, Sekida translation, about 9,600 words. `title`; source URL in body.
- `faith-in-mind.md`: Seng Ts'an, trans. Master Sheng-yen, about 2,100 words. `title`; source URL; includes a translator preface.
- `shodoka.md`: Yoka Genkaku Daishi, trans. Senzaki/Aitken, about 2,600 words. Fullest frontmatter: `title`, `author`, `source`.
- `seneca-on-the-shortness-of-life.md`: Seneca, trans. Basore (Loeb 1932), about 11,800 words, footnotes, chapter headings. `title`; source in body.
- `yogins-of-ladakh.md`: Crook and Low book, about 130,000 words (760 KB), raw OCR-like text with no frontmatter. Untracked in git (never committed) and not published.

No intros, summaries, dates, tags, themes, or per-text notes exist. Attribution is inconsistent (URL, book title, or none). Seneca is not a sutra, so the name already stretches to "wisdom teachings".

## Publishing

- Flowershow site at sutras.lifeitself.org (the page title suffix and 404 page are Flowershow's). Earlier hosting was Nuxt on GitHub Pages (2021 to 2024).
- `config.json` holds only Umami analytics. There is no nav, siteName, description, logo, `contentExclude` or footer.
- `README.md` doubles as the home page (title "Sutras - Curated Wisdom Teachings"). It is a bare link list and ends with a stray trailing `"` after the GitHub URL.
- Because there is no `contentExclude`, a `notes/` folder would be published (including this note) unless config is changed. Not edited here.

## Live site

- Home loads and lists the six tracked texts as links; `/diamond`, `/faith-in-mind`, `/shodoka` return 200 with correct titles. Content matches the repo.
- `/README` and `/yogins-of-ladakh` return 404 (the latter is untracked, so as expected).
- No navbar links, no site description, no index beyond the README list, no about page, no per-text intro or attribution block, and the footer is the default "sutras © 2026 sutras".

## Wilber-wiki patterns

`~/src/life-itself/wilber-wiki` is a Flowershow site built mainly by an AI agent, with `AGENTS.md` (conventions, publishing), `NEXT.md` (map of work streams), and Beads for tasks. Possible carry-overs:

1. **Typed folders with index pages**: `works/`, `concepts/`, `people/`, each with `index.md`. Sutras could split `texts/`, `concepts/` (emptiness, non-attachment, impermanence), `teachers/`.
2. **Frontmatter schema**: `title`, `slug`, `aliases`, `category`, `status`, `works`. Sutras has `title` only; a schema would enable filtering and indexes.
3. **Concept pages with verified excerpts**: each page has a synthesis plus excerpts, checked by `skills/add-excerpt-page/scripts/verify_quotes.py` so no quote is fabricated. This is the strongest AI-safety pattern to copy.
4. **Repo-local skills** (`skills/add-excerpt-page`, `write-book-summary`) that AI agents must read before editing.
5. **Config-driven nav, footer and roadmap/changelog pages** in `config.json`, which makes the site legible to a learner.
6. **Source text kept in `library/` and excluded from publishing** via `contentExclude`. This would suit Yogins of Ladakh and copyrighted material.

## Gaps & opportunities

- No stated purpose, audience or learning path; nothing says which text to read first or why.
- No reading guides, glossaries (Sanskrit/Chinese terms), cross-text concept links, or practice notes.
- No place for Rufus's own notes, questions or practice log; no annotation layer (wilber-wiki has one).
- Copyright and provenance are undocumented for several texts; Yogins of Ladakh looks like a copyrighted book and should not be published as-is.
- No AGENTS.md or Beads, so AI sessions have no conventions.
- Red Pine text looks incomplete; Seneca fits awkwardly under "sutras".

## Open questions for Rufus

- Is Sutras a public site, a private learning notebook, or both?
- Is scope Buddhist sutras only, or wider wisdom texts (Stoics and others)?
- Should Yogins of Ladakh stay in the repo, move to a private library, or be deleted?
- Do you want concept pages with verified excerpts, as in wilber-wiki?
- Should the site rename or keep the "Sutras" name?
