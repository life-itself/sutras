/* Sutras notes: highlights and margin notes from a text's notes file. A Flowershow page script.
   List it after /js/reading.js and the text's generated notes, e.g.
     scripts: [/js/reading.js, /js/notes/meditations.js, /js/notes.js]
   js/notes/<slug>.js (written by scripts/notes from annotations/<slug>.yaml) sets window.SutrasNotes.

   For each note: find its quote in its passage (the element with that id, up to the next element of
   the same kind), highlight it, and add a mark at the end of the line with the note beside it. The
   mark and note reuse the reading system's sidenote classes (rs-sn, rs-sn-ref, rs-sn-note), so they
   share the margin with the footnotes on a wide screen and open under the line on a tap on a phone.
   Highlights use the CSS Custom Highlight API, which leaves the page's HTML alone; older browsers
   get <mark> elements. A quote that is not found exactly once is skipped with a console warning,
   never shown against the wrong words (scripts/notes catches it first).
   Safe to run more than once: Flowershow re-runs page scripts on every visit. Styles: css/notes.css,
   loaded here unless the site's CSS already imports it. Matching rules are the same as scripts/notes. */
(function () {
  "use strict";
  if (document.currentScript && !document.currentScript.isConnected) return;
  var data = window.SutrasNotes;
  var root = document.querySelector(".rs .rs-text");
  if (!data || !data.notes || !root || root.__sutrasNotes) return;
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
  var FOLD = { "‘": "'", "’": "'", "‚": "'", "′": "'", "“": '"', "”": '"', "„": '"', "″": '"',
    "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-", "―": "-", "−": "-", " ": " " };
  function fold(s) { return s.replace(/[‘’‚′“”„″‐-―− ]/g, function (c) { return FOLD[c]; }).replace(/\s+/g, " "); }
  var SKIP = ".rs-sn, .nt-switch, a.v, sup, .footnotes, [data-footnotes], script, style, button";
  var BLOCK = /^(P|DIV|LI|UL|OL|H[1-6]|BLOCKQUOTE|SECTION|HEADER|TABLE|TR|TD|TH)$/;

  // Text of root from just after `from` up to `to` (or the end): {s, at}, where at[i] = [node, offset]
  // for each character of s (null for a space standing in for a line break or a block edge).
  function textOf(from, to) {
    var s = "", at = [], on = !from;
    function space(pos) { if (s && s[s.length - 1] !== " ") { s += " "; at.push(pos); } }
    var w = document.createTreeWalker(root, NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (n === from) { on = true; return NodeFilter.FILTER_REJECT; }
        if (n.nodeType === 1 && n.matches(SKIP)) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    for (var n = w.nextNode(); n; n = w.nextNode()) {
      if (n === to) break;
      if (!on) continue;
      if (n.nodeType === 1) { if (n.tagName === "BR" || BLOCK.test(n.tagName)) space(null); continue; }
      var t = n.nodeValue;
      for (var i = 0; i < t.length; i++) {
        var c = fold(t[i]);
        if (c === " ") space([n, i]); else { s += c; at.push([n, i]); }
      }
    }
    return { s: s, at: at };
  }

  function passageBounds(pid) {
    if (pid == null) return { from: null, to: null };
    var el = root.querySelector("[id='" + String(pid).replace(/'/g, "\\'") + "']");
    if (!el) return null;
    var sel = el.tagName.toLowerCase() + (el.className ? "." + el.className.trim().split(/\s+/).join(".") : "") + "[id]";
    var all = Array.prototype.slice.call(root.querySelectorAll(sel));
    return { from: el, to: all[all.indexOf(el) + 1] || null };
  }

  // The one place the note's quote is, as [startNode, startOffset, endNode, endOffset], or a reason.
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
    return [a[0], a[1], z[0], z[1] + 1];
  }

  // ---------- marks and margin notes ----------
  function esc(s) { var d = document.createElement("span"); d.textContent = s; return d.innerHTML; }
  function byName(by) { return (by || "").replace(/\(.*?\)/g, "").trim(); }

  function makeNote(note, n) {
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

  // Where the mark goes: at the end of the quote's line in verse (before the <br>, after any
  // footnote mark), at the end of the quote in prose. Keeps the mark with the word before it.
  function place(sn, endNode, endOffset) {
    var verse = endNode.parentNode.closest(".rs-verse");
    var before = null, block = endNode.parentNode.closest("p, li, blockquote, h2, h3, h4, div") || root;
    if (verse) {
      var w = document.createTreeWalker(block, NodeFilter.SHOW_ELEMENT);
      w.currentNode = endNode;
      for (var n = w.nextNode(); n; n = w.nextNode()) if (n.tagName === "BR" && !n.closest(".rs-sn")) { before = n; break; }
      var prev = before ? before.previousSibling : block.lastChild;
      while (prev && prev.nodeType === 3 && !/\S/.test(prev.nodeValue)) prev = prev.previousSibling;
      if (prev && prev.nodeType === 1 && prev.classList.contains("rs-nw")) { prev.appendChild(sn); return; }
      if (prev && prev.nodeType === 3) { wrapLastWord(prev, prev.nodeValue.replace(/\s+$/, "").length, sn); return; }
      block.insertBefore(sn, before);
      return;
    }
    // prose: the quote ends a word already kept with a mark (a footnote's, or another note's)
    var nw = endNode.parentNode.closest(".rs-nw");
    if (nw && endOffset === endNode.nodeValue.length) { nw.appendChild(sn); return; }
    var next = endNode.nextSibling;
    if (endOffset === endNode.nodeValue.length && next && next.nodeType === 1 && next.classList.contains("rs-nw")) { next.appendChild(sn); return; }
    wrapLastWord(endNode, endOffset, sn);
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

  // ---------- run ----------
  var notes = data.notes.filter(function (n) { return n && n.quote; });
  // pass 1: find each quote and put its mark in the page (last first, so earlier positions stay put)
  var found = [];
  notes.forEach(function (note) {
    var loc = locate(note);
    if (typeof loc === "string") { console.warn("notes.js: " + note.id + ": " + loc); return; }
    found.push({ note: note, end: [loc[2], loc[3]] });
  });
  found.sort(function (x, y) {
    if (x.end[0] === y.end[0]) return y.end[1] - x.end[1];
    return x.end[0].compareDocumentPosition(y.end[0]) & Node.DOCUMENT_POSITION_FOLLOWING ? 1 : -1;
  });
  found.forEach(function (f, i) { if (f.note.note) { f.sn = makeNote(f.note, i); place(f.sn, f.end[0], f.end[1]); } });
  // pass 2: the marks are not part of the text, so the quotes are found again in the same places
  found.forEach(function (f) {
    var loc = locate(f.note);
    if (typeof loc === "string") return;
    var r = document.createRange();
    r.setStart(loc[0], loc[1]); r.setEnd(loc[2], loc[3]);
    f.range = r;
  });
  found = found.filter(function (f) { return f.range; });
  if (!found.length) return;

  var native = !!(window.CSS && CSS.highlights && window.Highlight);
  var NAME = "sutras-note", ACTIVE = "sutras-note-active";
  function paint(on) {
    if (native) {
      if (on) CSS.highlights.set(NAME, new Highlight(...found.map(function (f) { return f.range; })));
      else CSS.highlights.delete(NAME);
    }
  }
  if (native) {
    paint(true);
    offs.push(function () { CSS.highlights.delete(NAME); CSS.highlights.delete(ACTIVE); });
  } else {
    // <mark> fallback: wrap each run of text in the range, last first
    var runs = [];
    found.forEach(function (f) {
      var w = document.createTreeWalker(f.range.commonAncestorContainer.nodeType === 3 ? f.range.commonAncestorContainer.parentNode : f.range.commonAncestorContainer, NodeFilter.SHOW_TEXT);
      for (var n = w.nextNode(); n; n = w.nextNode()) {
        if (!f.range.intersectsNode(n) || n.parentNode.closest(".rs-sn")) continue;
        var a = n === f.range.startContainer ? f.range.startOffset : 0, z = n === f.range.endContainer ? f.range.endOffset : n.nodeValue.length;
        if (z > a && /\S/.test(n.nodeValue.slice(a, z))) runs.push([n, a, z, f.note.id]);
      }
    });
    runs.reverse().forEach(function (r) {
      var n = r[0];
      if (r[2] < n.nodeValue.length) n.splitText(r[2]);
      var mid = r[1] ? n.splitText(r[1]) : n;
      var mark = document.createElement("mark");
      mark.className = "nt-mark"; mark.setAttribute("data-note", r[3]);
      mid.parentNode.insertBefore(mark, mid); mark.appendChild(mid);
    });
  }

  function setActive(f) {
    found.forEach(function (g) { if (g.sn) g.sn.classList.toggle("nt-active", g === f); });
    root.querySelectorAll(".nt-mark").forEach(function (m) { m.classList.toggle("nt-active", !!f && m.getAttribute("data-note") === f.note.id); });
    if (native) { if (f) CSS.highlights.set(ACTIVE, new Highlight(f.range)); else CSS.highlights.delete(ACTIVE); }
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
  function noteAt(x, y) {
    var pos = document.caretPositionFromPoint ? document.caretPositionFromPoint(x, y) : null;
    var node = pos ? pos.offsetNode : null, off = pos ? pos.offset : 0;
    if (!pos && document.caretRangeFromPoint) { var cr = document.caretRangeFromPoint(x, y); if (cr) { node = cr.startContainer; off = cr.startOffset; } }
    if (!node) return null;
    for (var i = 0; i < found.length; i++) {
      try { if (found[i].range.isPointInRange(node, off) && !(node === found[i].range.endContainer && off === found[i].range.endOffset)) return found[i]; } catch (e) {}
    }
    return null;
  }
  function onClick(e) {
    if (rs.classList.contains("nt-off") || e.target.closest("a, button, .rs-sn")) return;
    var sel = window.getSelection && window.getSelection();
    if (sel && !sel.isCollapsed) return;
    var f = noteAt(e.clientX, e.clientY);
    if (!f || !f.sn) return;
    if (wide()) { setActive(f); setTimeout(function () { setActive(null); }, 1600); }
    else toggle(f.sn);
  }
  root.addEventListener("click", onClick);

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
