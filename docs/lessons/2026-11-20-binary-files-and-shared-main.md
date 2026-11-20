# Committed EPUBs conflict; chain ship commands with `&&`

Date: 2026-11-20. Track: site.

Several tracks rebuild EPUBs into `downloads/` and push to `main` at the same time. A rebase then stops on a binary conflict, and a later `git commit -a` in the same `;`-chained command quietly commits in the middle of the rebase. Nothing broke, because the conflicted file kept the other track's version, but the commit message was wrong.

- Chain every step of shipping with `&&`, so a failed rebase stops the rest.
- Rebuild only EPUBs whose text changes, compare the words with the committed one (unzip, strip tags, diff), and say on the owning track's bead that you rebuilt it.
