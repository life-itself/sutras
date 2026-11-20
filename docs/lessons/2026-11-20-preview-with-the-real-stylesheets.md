# Preview with the real stylesheets, at the real specificity

Date: 2026-11-20. Track: landing (home page and its sketches).

A first preview loaded `reading.css` and `home.css` directly and skipped `custom.css`. It showed small caps on the first line of every paragraph after a heading, and hyphenated words the site never hyphenates, because `custom.css` turns both off. The screenshots looked wrong in a way the live site is not.

Also, a home-only rule for the shelf headings lost to the theme's `.rs[data-rs-theme="personal"] .rs-text h2` (same specificity, loaded earlier), so the group labels rendered at display size. Only the screenshot showed it.

- Preview through the same chain the site uses: serve the repo, and link `custom.css` (its `@import`s pull in `reading.css` and `home.css`). Do not hand-pick the files.
- A rule scoped to a page must match the specificity of the theme rule it overrides, and load after it. Check the computed size in a screenshot, not in the CSS.
- Take the sketch and the live screenshots at the same two widths (1280 and 390) so they compare directly.
