// Kit page: cube nav, tile cursor, detail sheets and the boot screen.
// Without JavaScript the page still works: tiles link to each kit's sheet by URL hash,
// the section links scroll, and nothing animates.
(function () {
  document.documentElement.classList.add("js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- kit tiles: a selection cursor you move with arrows, mouse or focus ---- */
  var grid = document.getElementById("tiles");
  var tiles = Array.prototype.slice.call(grid.querySelectorAll(".tile"));
  var sel = 0;
  function select(i) {
    sel = i;
    tiles.forEach(function (t, j) { t.classList.toggle("is-sel", j === i); });
  }
  function cols() {
    var top = tiles[0].offsetTop, n = 0;
    tiles.forEach(function (t) { if (t.offsetTop === top) n++; });
    return n || 1;
  }
  tiles.forEach(function (t, i) {
    t.addEventListener("mouseenter", function () { select(i); });
    t.addEventListener("focus", function () { select(i); });
    t.addEventListener("click", function (e) {
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      e.preventDefault();
      select(i);
      openKit(t.dataset.kit, t);
    });
  });
  grid.addEventListener("keydown", function (e) {
    var c = cols(), n = sel;
    if (e.key === "ArrowRight") n = Math.min(tiles.length - 1, sel + 1);
    else if (e.key === "ArrowLeft") n = Math.max(0, sel - 1);
    else if (e.key === "ArrowDown") n = Math.min(tiles.length - 1, sel + c);
    else if (e.key === "ArrowUp") n = Math.max(0, sel - c);
    else return;
    e.preventDefault();
    select(n);
    tiles[n].focus();
  });
  select(0);

  /* ---- detail sheets: price and every item are in the sheet before any checkout ---- */
  var opener = null;
  function openKit(id, from) {
    var dlg = document.getElementById(id);
    if (!dlg || dlg.tagName !== "DIALOG") return false;
    opener = from || null;
    var note = dlg.querySelector(".notice");
    if (note) note.hidden = true;
    if (typeof dlg.showModal === "function") { if (!dlg.open) dlg.showModal(); }
    else dlg.setAttribute("open", "");
    dlg.scrollTop = 0;
    history.replaceState(null, "", "#" + id);
    return true;
  }
  function closeKit(dlg) {
    if (typeof dlg.close === "function") dlg.close(); else dlg.removeAttribute("open");
  }
  Array.prototype.forEach.call(document.querySelectorAll("dialog.detail"), function (dlg) {
    dlg.addEventListener("close", function () {
      history.replaceState(null, "", location.pathname + location.search);
      var back = opener || tiles.filter(function (t) { return t.dataset.kit === dlg.id; })[0];
      if (back) back.focus({ preventScroll: true });
      opener = null;
    });
    dlg.addEventListener("click", function (e) { if (e.target === dlg) closeKit(dlg); });
    var x = dlg.querySelector("[data-close]");
    if (x) x.addEventListener("click", function (e) { e.preventDefault(); closeKit(dlg); });
    var buy = dlg.querySelector(".buy");
    var note = dlg.querySelector(".notice");
    if (buy && note) buy.addEventListener("click", function () { note.hidden = false; });
  });

  /* ---- cube nav: idles slowly, turns to a face when you pick a section ---- */
  var cube = document.getElementById("cube");
  var SECTIONS = ["kits", "how", "inside", "faq"];
  var navLinks = Array.prototype.slice.call(document.querySelectorAll(".facenav a"));
  var angle = -30, target = null, from = 0, t0 = 0, last = performance.now(), idleAt = 0;
  function draw() { cube.style.transform = "rotateX(-20deg) rotateY(" + angle + "deg)"; }
  function markNav(f) { navLinks.forEach(function (a) { a.setAttribute("aria-current", String(+a.dataset.face === f)); }); }
  function rotateTo(f) {
    var goal = -f * 90, d = ((goal - angle) % 360 + 540) % 360 - 180;
    if (reduce) { angle += d; draw(); return; }
    from = angle; target = angle + d; t0 = performance.now(); idleAt = t0 + 4000;
  }
  function tick(now) {
    var dt = now - last; last = now;
    if (target !== null) {
      var p = Math.min(1, (now - t0) / 600), e = p < .5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;
      angle = from + (target - from) * e;
      if (p >= 1) target = null;
    } else if (now > idleAt && !document.hidden) {
      angle -= dt * 360 / 14000; // one turn every 14 seconds
    }
    draw();
    requestAnimationFrame(tick);
  }
  draw();
  if (!reduce) requestAnimationFrame(tick);
  function go(f, e) {
    if (e) e.preventDefault();
    rotateTo(f);
    markNav(f);
    var el = document.getElementById(SECTIONS[f]);
    if (el) el.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
  }
  navLinks.forEach(function (a) {
    a.addEventListener("click", function (e) {
      go(+a.dataset.face, e);
      a.scrollIntoView({ block: "nearest", inline: "center", behavior: reduce ? "auto" : "smooth" });
    });
  });
  Array.prototype.forEach.call(document.querySelectorAll(".cube .face[data-face]"), function (b) {
    b.addEventListener("click", function () { go(+b.dataset.face); });
  });
  document.getElementById("press-start").addEventListener("click", function (e) {
    go(0, e);
    setTimeout(function () { select(0); tiles[0].focus({ preventScroll: true }); }, reduce ? 0 : 500);
  });

  /* ---- deep links from the home page (kits.html#service etc.) open that kit ---- */
  var hash = location.hash.slice(1);
  var deepKit = hash && tiles.some(function (t) { return t.dataset.kit === hash; });
  if (deepKit) {
    tiles.forEach(function (t, i) { if (t.dataset.kit === hash) select(i); });
    openKit(hash, tiles[sel]);
  }

  /* ---- boot screen: first visit per session only, about 1 second, skippable ---- */
  var boot = document.getElementById("boot"), seen = false;
  try { seen = sessionStorage.getItem("loadout-boot") === "1"; } catch (err) {}
  if (!reduce && !seen && !hash) {
    boot.hidden = false;
    var done = false;
    var end = function () {
      if (done) return;
      done = true;
      boot.classList.add("out");
      setTimeout(function () { boot.hidden = true; }, 380);
      try { sessionStorage.setItem("loadout-boot", "1"); } catch (err) {}
      document.removeEventListener("keydown", end);
    };
    boot.addEventListener("click", end);
    document.addEventListener("keydown", end);
    setTimeout(end, 1150);
  }
})();
