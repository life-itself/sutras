/* Sutras edition pages: page script, listed after reading.js in a page's frontmatter.

   1. Verse lines. Each line of a stanza (lines end in <br>) is wrapped in <span class="rs-line">, so a long line
   wraps on a phone with a hanging indent (custom.css). The stanza number (a.v) stays outside the lines.
   Only stanzas with more than one line are touched. Safe to run more than once.

   2. Passage links.
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

(() => {
  if (!document.currentScript?.isConnected) return;
  document.querySelectorAll(".rs .rs-verse p").forEach((p) => {
    if (p.dataset.rsLines || !p.querySelector(":scope > br")) return;
    p.dataset.rsLines = "1";
    const nodes = Array.from(p.childNodes);
    let line = null;
    const start = () => { line = document.createElement("span"); line.className = "rs-line"; p.appendChild(line); };
    nodes.forEach((n) => {
      if (n.nodeName === "BR") { n.remove(); line = null; return; }
      if (n.nodeType === 1 && n.matches("a.v")) { p.appendChild(n); return; }
      if (n.nodeType === 3 && !line) {
        n.nodeValue = n.nodeValue.replace(/^\s+/, "");
        if (!n.nodeValue) { n.remove(); return; }
      }
      if (!line) start();
      line.appendChild(n);
    });
  });
})();
