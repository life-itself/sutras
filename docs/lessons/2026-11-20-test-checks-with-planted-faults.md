# Test a check script by planting faults in a copy

Date: 2026-11-20. Track: site (`scripts/check`).

A check that passes on the live files proves little. `scripts/check` was run on a scratch copy of the repo with one fault of each kind planted (a stanza without its link, a duplicate id, an href that does not match its id, a vanished published id, a missing and an unused footnote, a bad fragment, an empty frontmatter field, a link into `docs/`). Every one was reported; that is the test. Do the same after changing the script.

Also: a screenshot script that adds a cache-busting `?nc=` *after* the `#fragment` silently stops testing passage links. Put the query before the hash, and print where the target element lands (`getBoundingClientRect().top`), not just the picture.
