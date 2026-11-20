# Notes: match the words, not the markup

Date: 2026-11-20. Track: notes (`scripts/notes`, `js/notes.js`).

While the notes script was being built, another track changed the verse DOM (edition.js now wraps each line in a span and removes the `<br>`s). Notes kept working where they matched on the page's words, and broke only where code had assumed a `<br>` (where to put the mark, and the space between two lines). So: find quotes in a flat string of the page's text, built by walking text nodes and treating line and block edges as a space; keep markup assumptions to the one place that needs them (where the mark goes), and keep the demo page loading the same scripts as a real edition so such a change shows up there first.

Two smaller ones. Insert the marks first (last in the page first, so earlier positions stay valid), then find the quotes again to make the highlight ranges: inserting elements after building ranges moves text nodes under them. And keep the checker's idea of "the passage" the same as the page's: start after the passage's own number or heading, end at the next passage of the same kind or at the end of the article.
