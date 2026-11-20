# Flowershow adds its own link to every heading with an id

A heading such as `<h3 id="12">…</h3>` comes out of Flowershow as `<h3 id="12"><a class="heading-link" href="#12"><svg…/></a>…</h3>`. So:

- don't wrap the heading text in your own `<a href="#12">`: it is no longer the only child, the template's quiet-heading rule (`:only-child`) misses it, and the whole heading renders as a red underlined link (the Mumonkan's first version);
- a plain `<h3 id="…">` is already a passage link: the id is the target and Flowershow supplies the link;
- check the live DOM, not the Markdown, when a style does not apply: one `page.evaluate(() => el.outerHTML)` in Playwright showed it at once.
