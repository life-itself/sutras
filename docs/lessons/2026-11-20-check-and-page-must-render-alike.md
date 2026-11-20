# A quote check must see the text as the page shows it

Date: 2026-11-20. Track: notes.

`scripts/notes` passed all 122 of Rufus's *Meditations* quotes, yet nine were "not found" on the live page. Flowershow runs a typography step (remark-smartypants, `quotes: false`) that turns `...` and Hays's spaced `. . .` into `…` and `--` into a dash, outside raw HTML. The check read the Markdown; the page script read the rendered text. Both now fold `…`, `...` and `. . .` to the same thing, and dash runs to one dash. The one remaining miss is an edition bug the check cannot see: `spring*.*` renders with visible asterisks (bead sutras-m2v.7.15).

So: after shipping notes, open the page and read the console (`notes.js: <id>: quote not found`), not just the check's "ok". The live page is the test; the check is the fast first pass. A code review by a fresh subagent found the other half of the same class of bug (the page's passage ran past the next stanza, the check's did not): give the reviewer both sides and ask where they disagree.
