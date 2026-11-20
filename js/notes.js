/* Sutras notes: highlights and margin notes from a text's notes file. A Flowershow page script.
   List it after the reading scripts and the text's generated notes, e.g.
     scripts: [/js/reading.js, /js/edition.js, /js/notes/meditations.js, /js/notes.js]
   js/notes/<slug>.js (written by scripts/notes from annotations/<slug>.yaml) sets window.SutrasNotes.

   For each note: find its quote in its passage (from the element with that id to the next passage
   of the same kind or the next h2), highlight it, and add a mark at the end of the line with the
   note beside it. The mark and note reuse the reading system's sidenote classes (rs-sn, rs-sn-ref,
   rs-sn-note), so they share the margin with the footnotes on a wide screen and open under the line
   on a tap on a phone. Highlights use the CSS Custom Highlight API, which leaves the page's HTML
   alone; older browsers get <mark> elements. A quote that is not found exactly once is skipped with
   a console warning, never shown against the wrong words (scripts/notes catches it first).
   Safe to run more than once: Flowershow re-runs page scripts on every visit. Styles: css/notes.css,
   loaded here unless the site's CSS already imports it. Matching rules are the same as scripts/notes. */
(function () {
  "use strict";
  if (document.currentScript && !document.currentScript.isConnected) return;
  var data = window.SutrasNotes;
  window.SutrasNotes = null; // never reuse another page's notes if this page's notes script is missing
  var root = document.querySelector(".rs .rs-text");
  if (!data || !data.notes || !root || root.__sutrasNotes) return;
  var here = decodeURIComponent(location.pathname).replace(/\/+$/, "") || "/";
  if (data.page && data.page !== here) { console.warn("notes.js: notes are for " + data.page + ", not " + here); return; }
  root.__sutrasNotes = true;
  var rs = root.closest(".rs");

  var offs = [];
  document.addEventListener("flowershow:page-leave", function () { offs.forEach(function (f) { f(); }); offs = []; }, { once: true });

  // ---------- styles ----------
  if (!getComputedStyle(document.documentElement).getPropertyValue("--sutras-notes-css").trim()) {
    var link = document.createElement("link");
    link.rel = "stylesheet"; link.href = "/css/notes.css";
    document.head.appendChild(link);
    offs.push(function () { link.remove(); });
  }

  // ---------- the page's text, as matched ----------
  // Same folding as scripts/notes: quotes, dashes (a run of them is one), ellipsis, whitespace.
  var FOLD = { "‘": "'", "’": "'", "‚": "'", "′": "'", "“": '"', "”": '"', "„": '"', "″": '"',
    "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-", "―": "-", "−": "-", "…": "..." };
  function folder() {
    var f = { s: "", at: [] };
    f.add = function (ch, pos) {
      var c = FOLD[ch] || ch;
      if (/\s/.test(c)) c = " ";
      for (var k = 0; k < c.length; k++) {
        if (c[k] === " " && !f.s) continue;
        if ((c[k] === " " || c[k] === "-") && f.s[f.s.length - 1] === c[k]) continue;
        f.s += c[k]; f.at.push(pos);
      }
    };
    return f;
  }
  function fold(s) { var f = folder(); for (var i = 0; i < s.length; i++) f.add(s[i], null); return f.s; }
  var SKIP = ".rs-sn, .nt-switch, a.v, sup, .footnotes, [data-footnotes], script, style, button";
  var BLOCK = /^(P|DIV|LI|UL|OL|H[1-6]|BLOCKQUOTE|SECTION|HEADER|TABLE|TR|TD|TH)$/;
  function ownWordsSkipped(el) { return el.matches("a.v, h1, h2, h3, h4, h5, h6") || !el.textContent.trim(); }

  // Text of root from the passage element `from` up to `to` (or the end): {s, at}, where at[i] = [node, offset]
  // for each character of s (null for a space standing in for a line break or a block edge).
  function textOf(from, to) {
    var f = folder(), on = !from, stop = false;
    var w = document.createTreeWalker(root, NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (n === to) { stop = true; return NodeFilter.FILTER_REJECT; }
        if (n === from) { on = true; return ownWordsSkipped(n) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_SKIP; }
        if (n.nodeType === 1 && n.matches(SKIP)) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    for (var n = w.nextNode(); n && !stop; n = w.nextNode()) {
      if (!on) continue;
      if (n.nodeType === 1) { if (n.tagName === "BR" || BLOCK.test(n.tagName) || n.classList.contains("rs-line")) f.add(" ", null); continue; }
      for (var i = 0; i < n.nodeValue.length; i++) f.add(n.nodeValue[i], [n, i]);
    }
    return f;
  }

  // Passages of the same kind: a.v numbers; headings that link to themselves; else the same tag with an id.
  function kindOf(el) {
    if (el.matches("a.v")) return function (x) { return x.matches("a.v[id]"); };
    if (/^H[1-6]$/.test(el.tagName)) return function (x) { return x.tagName === el.tagName && !!x.id && !!x.querySelector("a[href='#" + CSS.escape(x.id) + "']"); };
    return function (x) { return x.tagName === el.tagName && !!x.id; };
  }
  function passageBounds(pid) {
    if (pid == null) return { from: null, to: null };
    var el = document.getElementById(String(pid));
    if (!el || !root.contains(el)) return null;
    var same = kindOf(el), to = null;
    var w = document.createTreeWalker(root, NodeFilter.SHOW_ELEMENT);
    w.currentNode = el;
    for (var n = w.nextNode(); n; n = w.nextNode()) {
      if (el.contains(n) || n.closest(".rs-sn")) continue;
      if (n.tagName === "H2" || same(n)) { to = n; break; } // a passage never runs past a section heading
    }
    return { from: el, to: to };
  }

  // The one place the note's quote is, as a Range, or a reason it was not found.
  function locate(note) {
    var b = passageBounds(note.passage);
    if (!b) return "passage " + note.passage + " not on the page";
    var t = textOf(b.from, b.to);
    var q = fold(note.quote).trim(), pre = fold(note.prefix || "").trim(), suf = fold(note.suffix || "").trim();
    var hits = [];
    for (var i = t.s.indexOf(q); q && i !== -1; i = t.s.indexOf(q, i + 1)) {
      if (pre && !t.s.slice(0, i).trimEnd().endsWith(pre)) continue;
      if (suf && !t.s.slice(i + q.length).trimStart().startsWith(suf)) continue;
      hits.push(i);
    }
    if (hits.length !== 1) return hits.length ? "quote found " + hits.length + " times" : "quote not found";
    var a = t.at[hits[0]], z = t.at[hits[0] + q.length - 1];
    var r = document.createRange();
    r.setStart(a[0], a[1]); r.setEnd(z[0], z[1] + 1);
    return r;
  }

  // The runs of text in a range, leaving out footnotes and marks: [Range] over single text nodes.
  function runsOf(range) {
    var out = [], c = range.commonAncestorContainer;
    var w = document.createTreeWalker(c.nodeType === 3 ? c.parentNode : c, NodeFilter.SHOW_TEXT);
    for (var n = w.nextNode(); n; n = w.nextNode()) {
      if (!range.intersectsNode(n) || n.parentNode.closest(".rs-sn")) continue;
      var a = n === range.startContainer ? range.startOffset : 0, z = n === range.endContainer ? range.endOffset : n.nodeValue.length;
      if (z > a && /\S/.test(n.nodeValue.slice(a, z))) { var r = document.createRange(); r.setStart(n, a); r.setEnd(n, z); out.push(r); }
    }
    return out;
  }

  // ---------- marks and margin notes ----------
  function esc(s) { var d = document.createElement("span"); d.textContent = s; return d.innerHTML; }
  function byName(by) { return (by || "").replace(/\(.*?\)/g, "").trim(); }

  function makeNote(note) {
    var id = "nt-" + note.id.replace(/[^A-Za-z0-9_-]/g, "-");
    var sn = document.createElement("span");
    sn.className = "rs-sn nt-sn";
    sn.setAttribute("data-note", note.id);
    var short = note.quote.length > 60 ? note.quote.slice(0, 57) + "…" : note.quote;
    sn.innerHTML = '<button type="button" class="rs-sn-ref nt-ref" aria-expanded="false" aria-controls="' + id + '"></button>' +
      '<span class="rs-sn-note nt-note" id="' + id + '" role="note"><span class="rs-sn-n nt-n">※</span> ' + note.note +
      (note.by ? ' <span class="nt-by">' + esc(byName(note.by)) + "</span>" : "") + "</span>";
    var btn = sn.firstChild;
    btn.textContent = "※";
    btn.setAttribute("aria-label", "Note on “" + short + "”");
    btn.addEventListener("click", function () { toggle(sn); });
    return sn;
  }

  function toggle(sn, force) {
    var open = sn.classList.toggle("rs-open", force);
    sn.firstChild.setAttribute("aria-expanded", String(open));
  }

  // Marks are placed last first, so a note placed later belongs before the notes already in a wrap
  // (after any footnote, which stays first).
  function addTo(nw, sn) { nw.insertBefore(sn, nw.querySelector(":scope > .nt-sn")); }
  function isNw(n) { return !!n && n.nodeType === 1 && n.classList.contains("rs-nw"); }

  // Put the mark after `prev` (the last thing before the mark's place, in `parent`), kept with its word.
  function after(prev, parent, before, sn) {
    while (prev && prev.nodeType === 3 && !/\S/.test(prev.nodeValue)) prev = prev.previousSibling;
    if (isNw(prev)) addTo(prev, sn);
    else if (prev && prev.nodeType === 3) wrapLastWord(prev, prev.nodeValue.replace(/\s+$/, "").length, sn);
    else if (prev && prev.nodeType === 1 && prev.matches("a:not(.v), em, strong, i, b")) wrapNode(prev, sn);
    else parent.insertBefore(sn, before);
  }

  // Where the mark goes: at the end of the quote's line in verse, at the end of the quote in prose.
  // `end` is a live, collapsed Range at the quote's end, which the DOM keeps right as later marks split text.
  function place(sn, end) {
    var node = end.endContainer, off = end.endOffset;
    var el = node.nodeType === 3 ? node.parentNode : node;
    var line = el.closest(".rs-line");
    if (line) { after(line.lastChild, line, null, sn); return; }   // verse, one span per line (edition.js)
    var block = el.closest("p, li, blockquote, h2, h3, h4, div") || root;
    if (el.closest(".rs-verse")) {                                  // verse with <br> between lines
      var br = null, w = document.createTreeWalker(block, NodeFilter.SHOW_ELEMENT);
      w.currentNode = node.nodeType === 3 ? node : (node.childNodes[off - 1] || node);
      for (var n = w.nextNode(); n; n = w.nextNode()) if (n.tagName === "BR" && !n.closest(".rs-sn")) { br = n; break; }
      after(br ? br.previousSibling : block.lastChild, block, br, sn);
      return;
    }
    if (node.nodeType !== 3) { after(node.childNodes[off - 1], node, node.childNodes[off] || null, sn); return; }
    // prose: a quote that ends a link or emphasis gets its mark after it (never inside a link)
    var inl = el.closest("a:not(.v), em, strong, i, b");
    if (inl && root.contains(inl) && off === node.nodeValue.length && !node.nextSibling) {
      var nwIn = inl.parentNode.closest(".rs-nw");
      if (nwIn) addTo(nwIn, sn); else wrapNode(inl, sn);
      return;
    }
    var nw = el.closest(".rs-nw");
    if (nw && off === node.nodeValue.length) { addTo(nw, sn); return; }
    if (off === node.nodeValue.length && isNw(node.nextSibling)) { addTo(node.nextSibling, sn); return; }
    wrapLastWord(node, off, sn);
  }

  // Split `node` at `offset`, move the word just before it into <span class="rs-nw"> with `sn`.
  function wrapLastWord(node, offset, sn) {
    if (offset < node.nodeValue.length) node.splitText(offset);
    var m = node.nodeValue.match(/\S+$/);
    var word = m ? node.splitText(node.nodeValue.length - m[0].length) : null;
    var nw = document.createElement("span");
    nw.className = "rs-nw nt-nw";
    node.parentNode.insertBefore(nw, word || node.nextSibling);
    if (word) nw.appendChild(word);
    nw.appendChild(sn);
  }
  function wrapNode(el, sn) {
    var nw = document.createElement("span");
    nw.className = "rs-nw nt-nw";
    el.parentNode.insertBefore(nw, el);
    nw.appendChild(el); nw.appendChild(sn);
  }

  function docOrder(a, b) { // [node, offset] pairs, later in the page first
    if (a[0] === b[0]) return b[1] - a[1];
    if (a[0].contains(b[0]) || b[0].contains(a[0])) return 0;
    return a[0].compareDocumentPosition(b[0]) & Node.DOCUMENT_POSITION_FOLLOWING ? 1 : -1;
  }

  // ---------- run ----------
  // pass 1: find each quote and put its mark in the page, last first
  var found = [];
  data.notes.forEach(function (note) {
    if (!note || !note.quote) return;
    var r = locate(note);
    if (typeof r === "string") { console.warn("notes.js: " + note.id + ": " + r); return; }
    var end = r.cloneRange(); end.collapse(false);
    found.push({ note: note, end: end, at: [r.endContainer, r.endOffset], from: [r.startContainer, r.startOffset] });
  });
  // last end first; where two quotes end together, the one that starts later is placed first (and shows second)
  found.sort(function (x, y) { return docOrder(x.at, y.at) || docOrder(x.from, y.from); });
  found.forEach(function (f) { if (f.note.note) { f.sn = makeNote(f.note); place(f.sn, f.end); } });
  // pass 2: marks are not part of the text, so each quote is found again, now in its final text nodes
  found.forEach(function (f) {
    var r = locate(f.note);
    if (typeof r !== "string") f.runs = runsOf(r);
  });
  found = found.filter(function (f) { return f.runs && f.runs.length; });
  found.reverse(); // page order
  if (!found.length) return;

  var native = !!(window.CSS && CSS.highlights && window.Highlight);
  var NAME = "sutras-note", ACTIVE = "sutras-note-active";
  var allRuns = [].concat.apply([], found.map(function (f) { return f.runs; }));
  function paint(on) {
    if (!native) return;
    if (on) CSS.highlights.set(NAME, new Highlight(...allRuns)); else CSS.highlights.delete(NAME);
  }
  if (native) offs.push(function () { CSS.highlights.delete(NAME); CSS.highlights.delete(ACTIVE); });
  else {
    // <mark> fallback: every run of every note, last in the page first, so earlier offsets stay valid
    var marks = [];
    found.forEach(function (f) { f.runs.forEach(function (r) { marks.push([r.startContainer, r.startOffset, r.endOffset, f.note.id]); }); });
    marks.sort(function (x, y) { return docOrder(x, y); });
    var low = new Map(); // text node -> lowest offset already wrapped (where notes overlap, one mark)
    marks.forEach(function (m) {
      var n = m[0], a = m[1], z = Math.min(m[2], low.has(n) ? low.get(n) : Infinity);
      if (z <= a || !n.parentNode) return;
      if (z < n.nodeValue.length) n.splitText(z);
      var mid = a ? n.splitText(a) : n;
      var mark = document.createElement("mark");
      mark.className = "nt-mark"; mark.setAttribute("data-note", m[3]);
      mid.parentNode.insertBefore(mark, mid); mark.appendChild(mid);
      low.set(n, a);
    });
  }

  function setActive(f) {
    found.forEach(function (g) { if (g.sn) g.sn.classList.toggle("nt-active", g === f); });
    root.querySelectorAll(".nt-mark").forEach(function (m) { m.classList.toggle("nt-active", !!f && m.getAttribute("data-note") === f.note.id); });
    if (native) { if (f) CSS.highlights.set(ACTIVE, new Highlight(...f.runs)); else CSS.highlights.delete(ACTIVE); }
  }
  function wide() { return rs.clientWidth >= 760; }

  // a margin note lights up its words
  found.forEach(function (f) {
    if (!f.sn) return;
    var note = f.sn.querySelector(".nt-note");
    note.addEventListener("mouseenter", function () { if (wide()) setActive(f); });
    note.addEventListener("mouseleave", function () { if (wide()) setActive(null); });
  });

  // tapping highlighted words opens (phone) or points out (wide screen) their note
  function noteAt(e) {
    var m = e.target.closest && e.target.closest("mark.nt-mark");
    if (m) return found.filter(function (f) { return f.note.id === m.getAttribute("data-note"); })[0] || null;
    var node = null, off = 0;
    if (document.caretPositionFromPoint) { var p = document.caretPositionFromPoint(e.clientX, e.clientY); if (p) { node = p.offsetNode; off = p.offset; } }
    else if (document.caretRangeFromPoint) { var cr = document.caretRangeFromPoint(e.clientX, e.clientY); if (cr) { node = cr.startContainer; off = cr.startOffset; } }
    if (!node) return null;
    for (var i = 0; i < found.length; i++) {
      for (var j = 0; j < found[i].runs.length; j++) {
        var r = found[i].runs[j];
        if (r.startContainer === node && off >= r.startOffset && off < r.endOffset) return found[i];
      }
    }
    return null;
  }
  var timer = null;
  function onClick(e) {
    if (rs.classList.contains("nt-off") || e.target.closest("a, button, .rs-sn")) return;
    var sel = window.getSelection && window.getSelection();
    if (sel && !sel.isCollapsed) return;
    var f = noteAt(e);
    if (f && !f.sn) { // a highlight with no comment: a note on a later quote in the same passage speaks for it
      var k = found.indexOf(f);
      while (k < found.length && !found[k].sn && found[k].note.passage === f.note.passage) k++;
      f = found[k] && found[k].sn && found[k].note.passage === f.note.passage ? found[k] : null;
    }
    if (!f) return;
    if (wide()) { setActive(f); clearTimeout(timer); timer = setTimeout(function () { setActive(null); }, 1600); }
    else toggle(f.sn);
  }
  root.addEventListener("click", onClick);
  offs.push(function () { clearTimeout(timer); });

  // on a wide screen the margin notes are always shown; the marks are not buttons there
  function mode() {
    var w = wide();
    found.forEach(function (f) {
      if (!f.sn) return;
      var b = f.sn.firstChild;
      if (w) { b.setAttribute("tabindex", "-1"); b.setAttribute("aria-expanded", "true"); }
      else { b.removeAttribute("tabindex"); b.setAttribute("aria-expanded", String(f.sn.classList.contains("rs-open"))); }
    });
  }
  if (window.ResizeObserver) { var ro = new ResizeObserver(mode); ro.observe(rs); offs.push(function () { ro.disconnect(); }); }
  else { window.addEventListener("resize", mode); offs.push(function () { window.removeEventListener("resize", mode); }); }
  mode();

  // a switch to read the text without notes, remembered in this browser
  var KEY = "sutras-notes-off";
  var who = Array.from(new Set(found.map(function (f) { return byName(f.note.by); }))).join(", ");
  var bar = document.createElement("p");
  bar.className = "nt-switch";
  bar.innerHTML = '<span class="nt-switch-label"></span> <button type="button" aria-pressed="false"></button>';
  bar.firstChild.textContent = "Notes by " + who + ".";
  var sw = bar.lastChild;
  function show(on) {
    rs.classList.toggle("nt-off", !on);
    sw.textContent = on ? "Hide notes" : "Show notes";
    sw.setAttribute("aria-pressed", String(!on));
    paint(on);
    if (!on) setActive(null);
  }
  sw.addEventListener("click", function () {
    var on = rs.classList.contains("nt-off");
    show(on);
    try { if (on) localStorage.removeItem(KEY); else localStorage.setItem(KEY, "1"); } catch (e) {}
  });
  var anchor = root.querySelector(".rs-inbrief");
  root.insertBefore(bar, anchor ? anchor.nextSibling : root.firstChild);
  var off = false;
  try { off = localStorage.getItem(KEY) === "1"; } catch (e) {}
  show(!off);
})();
