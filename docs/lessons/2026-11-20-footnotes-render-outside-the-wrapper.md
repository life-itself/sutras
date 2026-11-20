# Flowershow puts the footnote list outside your wrapper `<div>`

Markdown footnote definitions are rendered as one `<section class="footnotes">` at the very end of the page, after the closing `</div>` of the `.rs` reading wrapper. Two things follow:

- The reading system's `reading.js` (v0.1) looks for the footnote text inside `.rs`, finds nothing, and makes no margin notes. Our copy in `js/reading.js` falls back to `document.getElementById` (marked `sutras: 2`).
- Its CSS hides the leftover list only inside `.rs`. `custom.css` hides `[data-rs-sidenoted]` anywhere and styles the bare list for readers without JavaScript.

Footnote ids come out as `user-content-fn-1`; the links match, so nothing else is needed. This goes away when notes become data (milestone 2), but any page that uses footnotes with the reading layout depends on it until then.
