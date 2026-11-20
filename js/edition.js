/* Sutras edition pages: page script, listed after reading.js in a page's frontmatter.
   A passage link such as /faith-in-mind#3 is scrolled to by the browser before the web font has
   loaded and before reading.js has moved the notes into the margin, so the page shifts and the
   stanza ends up a little off. Scroll to it again once the fonts are in, unless the reader has
   already started moving. Safe to run more than once (Flowershow re-runs page scripts). */
(() => {
  if (!document.currentScript?.isConnected) return;
  const id = decodeURIComponent(location.hash.slice(1));
  const target = id && document.getElementById(id);
  if (!target || !target.closest(".rs")) return;
  let cancelled = false;
  const cancel = () => { cancelled = true; };
  const events = ["wheel", "touchstart", "keydown", "mousedown"];
  events.forEach((e) => window.addEventListener(e, cancel, { passive: true, once: true }));
  const stop = () => events.forEach((e) => window.removeEventListener(e, cancel));
  document.addEventListener("flowershow:page-leave", () => { cancel(); stop(); }, { once: true });
  const ready = document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve();
  ready.then(() => requestAnimationFrame(() => { if (!cancelled) target.scrollIntoView(); stop(); }));
})();
