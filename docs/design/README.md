# Sutras design

Status, 2026-11-21: **round 2 is live**: Emergence's Red Pine page in the Seeds of Renaissance faces (decision [0006](../decisions/0006-red-pine-seeds.md)), chosen by Rufus. `css/direction-seeds.css` is selected by the last `@import` in `custom.css`; direction A (decision 0005, described below) is the one-line fallback. Bead: sutras-m2v.3. Process: the `designing-look-and-feel` skill.

## The direction

Emergence Magazine's Red Pine poem page as the base (warm grey paper, one open-licence image per text given room, a small label, the title, then the text in a narrow serif column), held to Kaikado's restraint. The apparatus (stanza and passage numbers, note marks, the "In brief" label, the mark in the navbar) is the only place the warm red appears. Literata for the text, Instrument Sans for the one tracked label, Noto Serif TC for Chinese and the mark 慧. The home page is a shelf: one image per text, title, author line.

## How it is wired, and how to undo or swap it

- `css/direction-a.css` holds the whole direction: tokens, Flowershow's navbar and footer, the image above the title, the apparatus colours, the home shelf. It is selected by the **last `@import` line of `custom.css`**. Remove that line and the site returns to the stand-in look (EB Garamond on the reading system's personal theme). Swap the file for another direction's CSS to try it live; the samples' CSS is in `directions/` (`base.css` + `a.css`, `b.css`, `c.css`).
- Each edition page carries two pieces of markup, and nothing else changed in its words: a `<figure class="sd-art">` (image, credit) just before its `<header class="rs-head">`, and a label in its `.rs-kicker` ("Zen · a poem") in place of the old "Sutras" link. `faith-in-mind.md` is the model.
- Images: `assets/images/<slug>.jpg`, each under 150 KB; every one's source, licence, credit and reason is in [images.md](images.md). Add an image for a new text there first. Scans whose own paper shows through the multiply blend are cleaned (greys pushed to white) before use.
- The mark: the CSS variable `--sutras-mark` in `direction-a.css` is `"慧"`; set it to `""` for the wordmark alone. Both are screenshotted in `shots/mark-with.jpg` and `shots/mark-without.jpg`; the choice is filed for Rufus as a needs-rufus bead.
- The home shelf: `README.md` keeps the landing session's copy and structure; each entry is a list item (`<ul class="sd-shelf">`, one per group) with image, title link, author line and one-line description.
- Checks after a change: `scripts/check`, then every page at 390 (device emulation, `scrollWidth` must equal 390) and 1280; the audit script used is in the session scratch, its rule is simple: no element's right edge past the viewport, and the title on the first screen.

## History: every round and where it is

| Date | Round | What Rufus said | Where |
|---|---|---|---|
| 2026-11-20 | First design page: feel, measured research, eight directions | "mood board is weak. where is the true beauty in this" | `archive/2026-11-20-first-page/` (not republished) |
| 2026-11-20 | First mood board: six references, two anti-references | Loves Kaikado and Emergence's Red Pine page; Co–Star's images; Plum Village too warm; wants something funkier | [Mood board](https://claude.ai/artifact/Wv1GFH5C3QQtXykof4eSrg) (since republished as the second board) |
| 2026-11-20 | Second mood board, widened | "i like sesshu"; "if i were basing off something it would be that one emergence page of red pine" | [Mood board](https://claude.ai/artifact/Wv1GFH5C3QQtXykof4eSrg) |
| 2026-11-21 | Three directions as sample sites, with marks and fonts | Not seen before the choice; agents chose A (decision 0005) | [Summary page: directions, marks, fonts](https://claude.ai/artifact/P76Wz3n8TeN2CXTrgbYnwr) · [A warm red](https://claude.ai/artifact/FrqFoG8gtKYvTyApm4h3K8) · [B blue](https://claude.ai/artifact/WFPMxwZ9UNWuFJyenM4uUc) · [C gold on indigo](https://claude.ai/artifact/FLoxRQmuVwdcpHwh4yZD4F) |
| 2026-11-21 | A live on the site; home page rewritten as a shelf | "the site isn't bad, but it's not great… not nearly as beautiful" as Emergence | https://sutras.lifeitself.org |
| 2026-11-21 | Round 2: Faith in Mind as a near-copy of the Red Pine page, in open-licence faces and in the Seeds of Renaissance faces | "this direction is the way to go, and probably the Seeds of Renaissance fonts"; but "quite elaborate… not going to work for general text pages" | [Open faces](https://claude.ai/artifact/1EWyZdNMhjruSC3YTUN7Ta) · [Seeds faces](https://claude.ai/artifact/HDLYRfSpMtc2Sn8C13mxnh) · built by `redpine/build.py` |

| 2026-11-21 | Round 2 sample site, Seeds faces: home; feature (Faith in Mind); plain reading page with contents rail and margin notes (Seneca); three columns, Chinese, English, notes (Mumonkan); Restora or Fraunces | "good enough to ship for now"; the mark 道 in a stamp; home picture beside the name; Fraunces to compare |  [Sample site](https://claude.ai/artifact/2bxZGknNTrPacMyfcq9iyb) · built by `round2/build.py` |

Why the first rounds missed: [the lesson](../lessons/2026-11-21-copy-the-reference-before-interpreting-it.md).

| 2026-11-21 | Round 2 live (decision 0006) | (pending) | https://sutras.lifeitself.org |

## Pages

- **The direction, three sample sites, marks, fonts, recommendation:** https://claude.ai/artifact/P76Wz3n8TeN2CXTrgbYnwr. Sample sites: [A warm red](https://claude.ai/artifact/FrqFoG8gtKYvTyApm4h3K8) (live), [B blue](https://claude.ai/artifact/WFPMxwZ9UNWuFJyenM4uUc) (set aside), [C gold on indigo](https://claude.ai/artifact/FLoxRQmuVwdcpHwh4yZD4F) (the backup). Built by `directions/build.py` from snapshots of the live pages plus the direction CSS.
- **Mood board (pictures to look at):** https://claude.ai/artifact/Wv1GFH5C3QQtXykof4eSrg, second board, widened from Rufus's reactions.

## Files

- [brief.md](brief.md): the design brief, with Rufus's reactions to both boards quoted at the end.
- `brief.src.html` → `brief.html`: the direction page; `moodboard.src.html` → `moodboard.html`: the board. `python3 docs/design/build.py [moodboard]` inlines `shots/` and writes the built file; republish with the Artifact tool at the page's URL.
- [moodboard-candidates.md](moodboard-candidates.md): every candidate scanned (about 130), one line each.
- [images.md](images.md): the site's images, sources and licences.
- [research-reading-features.md](research-reading-features.md): verse setting, margin notes, measurements, phones. For the site and notes work.
- `directions/`: the direction CSS, the sample-site builder, DOM snapshots and images.
- `archive/`: the rejected first page and the earlier "five directions" page.

## Open, for Rufus

- The mark: 慧 (default, live) or the wordmark alone; also 道 or an italic initial as alternatives. The objection on record: on Seneca's and Marcus's pages a Chinese character claims them for the East.
- Whether C's gold-on-indigo front matter should return for the Buddhist texts only.
- Better images for the Dhammapada (a Pali leaf) and Seneca (a Seneca manuscript or early edition), if open-licence ones can be found; the Tao Te Ching needs one.
- A drawn mark, the EPUB cover in the direction, and the paper's warmth on cheap screens.
