# 0005 · Design direction: A, warm red, with C as the backup

Date: 2026-11-21. Decided by the design session with the coordinator's agreement, on Rufus's instruction of 2026-11-20 night ("build out full sample sites in all three directions… if you have to choose have a discussion amongst yourselves and decide and you can always build several options for me to later compare, or rather one backup").

## The decision

Direction **A, warm red**, goes live: Emergence Magazine's Red Pine poem page as the base (warm grey paper, one open-licence ink image per text given room, a small label, the title, then the text in a narrow serif column), held to Kaikado's restraint; the apparatus (stanza and passage numbers, note marks, the label before "In brief", the mark) in a warm, slightly orange red; Literata for the text; labels in the text face, italic, not tracked capitals; the mark 慧 (wisdom) printed in Noto Serif TC in the red beside the wordmark "Sutras". The home page becomes a shelf: one image per text, title, author line.

Direction **C, gold on indigo** (same page with the front matter of each text in an indigo band with the title in gold, Newsreader), is kept as the backup for Rufus to compare: https://claude.ai/artifact/FLoxRQmuVwdcpHwh4yZD4F. Direction B, blue, is set aside: https://claude.ai/artifact/WFPMxwZ9UNWuFJyenM4uUc.

Sample site A: https://claude.ai/artifact/FrqFoG8gtKYvTyApm4h3K8. The page comparing them, with marks and fonts: https://claude.ai/artifact/P76Wz3n8TeN2CXTrgbYnwr. The CSS: `docs/design/directions/base.css` and `a.css`.

## Why

- A is the direction Rufus reacted to most directly: "I love the emergence magazine, particularly that page" (the Red Pine poem), "I love the tea caddies in a row" (Kaikado), "if i were basing off something it would be that one emergence page of red pine", and the red is the colour he liked on that page.
- It is the best of the three to read on a phone, which the brief set as the test; a fresh agent's critique agreed ("the only one that looks like the Red Pine page… better than the live site").
- It asks the least of Seneca and Marcus Aurelius, which have no ink painting of their own. C makes them "wear a Buddhist robe" (the critique) and its gold is weak for numbers and notes; B's blue reads as links and is cold, as Rufus feared.
- C is the backup because it is Rufus's own idea ("borrow the gold on indigo") and a real alternative, not a variant.

## Open, for Rufus

- The mark: 慧 printed in red is the default. The critique's objection stands: on the Stoic pages it claims them for the East. Alternatives shown on the directions page: the wordmark alone; 慧 only on the East Asian texts; 道; an italic initial.
- Whether C's indigo band should return as a treatment for the Buddhist texts only.
- The exact warmth of the paper on a cheap screen.

## What this changes

The design session owns `css/` and `custom.css` (coordinator, 2026-11-21) and applies A to the live site in small commits, checking all nine editions plus home and about at 390 and 1280 wide; the home page is restyled with the landing session, which owns `README.md`, `about.md` and `css/home.css`. The EPUB cover follows later (bead sutras-m2v.8.3).

## Outcome (2026-11-21, 01:00)

Applied. Direction A is live on all eleven pages (nine editions including the two Tao Te Ching pages, home, About): `css/direction-a.css` selected by the last `@import` in `custom.css`; a figure and label on every edition; `assets/images/` with credits in `docs/design/images.md`; the home shelf. Checked with device emulation at 390×844 (no horizontal overflow on any page, title on the first screen) and at 1280×800. The coordinator's three live-review fixes (title at the fold, phone overflow verification, the Meditations scan's paper) were made the same night. Open for Rufus, filed as a needs-rufus bead: the mark (慧 live, wordmark alone as the one-line alternative). Filed: the EPUB cover and stylesheet to follow the direction. The home page's words and structure were being rewritten by the landing session at the time; design restyles after it lands. Backup C remains at its artifact link.
