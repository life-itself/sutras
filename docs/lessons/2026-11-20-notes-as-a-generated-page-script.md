# Data on a Flowershow page travels as a generated page script

Date: 2026-11-20. Track: notes.

A Flowershow page cannot `fetch()` a data file from its own site (files are served through a redirect without CORS headers, flowershow#1373), and inline `<script>` in Markdown does not run after in-site navigation. What works: a script generates `js/notes/<slug>.js` (`window.SutrasNotes = {...}`) from the YAML, the page lists it as a page script before the code that reads it, and the generated file is committed. The same trick suits any per-page data (wilber-wiki pastes JSON into each page instead). A page script can also load its own stylesheet (`<link>` added to `<head>`, removed on `flowershow:page-leave`), which lets a feature ship without editing the site's shared CSS.
