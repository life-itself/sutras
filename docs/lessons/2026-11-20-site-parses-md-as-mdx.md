# The site parses `.md` as MDX: set `syntaxMode: md` on pages with raw HTML

The Sutras site's Flowershow setting is MDX for every file (set in the dashboard, not in `config.json`). A page with ordinary raw HTML (`<p class="…">`, `<br>`, a wrapper `<div>`) fails to compile and the live page shows an error card in place of the text. This happened to `/faith-in-mind` on the first push and was live for about five minutes.

What to do:

- Any page that uses raw HTML (every edition on the reading layout does) needs `syntaxMode: md` in its frontmatter.
- After every push, fetch the live page and look for `error compiling MDX` before doing anything else: `curl -s https://sutras.lifeitself.org/<page> | grep -c "error compiling"`.
- Better fix, for the Site workstream: set `"syntaxMode": "md"` in `config.json` once it is checked that no existing page relies on MDX, and add the grep to `scripts/check`.
