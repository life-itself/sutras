# A passage link lands in the wrong place unless you scroll again after the fonts load

The browser jumps to `/faith-in-mind#3` as soon as the HTML is in. Then EB Garamond arrives and `reading.js` moves the notes, the page above the stanza changes height, and the stanza ends up partly off the top of the window (13px off in the first test; more on slow connections).

Fix: `js/edition.js`, a page script listed after `reading.js`. It waits for `document.fonts.ready`, then scrolls to the hash target again, unless the reader has already touched the page. `scroll-margin-top` on the stanza number (in `custom.css`) keeps it clear of the navbar.

Also learnt: an inline `<a class="v" id="3" href="#3">3</a>` at the start of a stanza survives Flowershow's Markdown mode untouched, numeric id and all, keeps the line breaks, and works without JavaScript. No script is needed to add ids.
