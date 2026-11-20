# JavaScript `\s` matches em spaces

Date: 2026-11-20. Track: site (`js/edition.js`).

Wrapping verse lines in spans, the script trimmed leading `\s` from each line. In JavaScript `\s` includes U+2003, so the Dhammapada's `&emsp;` indents vanished on the live page; the newtexts track found it. Trim only `[ \t\r\n]` when the text may carry typographic spaces, and when a template script changes, check every edition that uses it, not only the one you were looking at.
