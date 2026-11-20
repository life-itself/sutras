# Two Pandoc EPUB traps with raw HTML in the page

`scripts/epub` feeds the page's Markdown, raw HTML and all, to Pandoc. Two things broke in the Mumonkan EPUB and passed silently (Pandoc did not warn):

- `<br>` inside a raw HTML block is passed through as is, which is invalid XHTML, so a strict reader rejects the chapter. Write `<br />` in raw HTML (it is valid HTML too).
- Pandoc rewrites Markdown links to numeric targets (`[Case 1](#1)` becomes `#id_1`) but leaves raw-HTML ids (`<h3 id="1">`) alone, so the links miss. Write the link list as raw HTML (`<a href="#1">`), or give the targets Markdown ids.

Check: unzip the EPUB and parse each `EPUB/text/*.xhtml` with an XML parser (`python3 -c "import xml.dom.minidom as m; m.parse(f)"`); grep the hrefs against the ids.
