/* Questions for Wil: tabs, plus decision cards stored in the artifact db.
   questions/<id> = { title, context, topic, created: "YYYY-MM-DD",
     status: "open" | "decided",
     options: [{ id, by: "claude" | "zucc" | "both" | "alt", label, why }],
     zucc: "pending" | "in",
     pick: { option, label, note, at } }
   Claude seeds and reads these with ArtifactData; the page only writes `status` and `pick`. */
(function () {
  var views = { calendar: document.getElementById("view-calendar"), questions: document.getElementById("view-questions") };
  var tabs = document.querySelectorAll(".tab");
  function show(name) {
    if (!views[name]) name = "calendar";
    Object.keys(views).forEach(function (k) { views[k].hidden = k !== name; });
    tabs.forEach(function (t) { t.setAttribute("aria-pressed", t.dataset.view === name ? "true" : "false"); });
  }
  tabs.forEach(function (t) {
    t.addEventListener("click", function () {
      show(t.dataset.view);
      try { history.replaceState(null, "", "#" + t.dataset.view); } catch (e) {}
    });
  });
  show((location.hash || "").slice(1));

  var BY = { claude: "Claude's pick", zucc: "Zucc's pick", both: "Both agree", alt: "Other option", own: "You" };
  var MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  var stateEl = document.getElementById("q-state");
  var openEl = document.getElementById("q-open");
  var doneEl = document.getElementById("q-done");
  var doneH = document.getElementById("q-done-h");
  var countEl = document.getElementById("q-count");
  var drafts = {}, editing = {}, db = null, latest = [];

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }
  function day(iso) {
    var m = /^(\d{4})-(\d{2})-(\d{2})/.exec(String(iso || ""));
    return m ? MONTHS[+m[2] - 1] + " " + (+m[3]) : "";
  }

  function card(id, q) {
    var c = el("article", "q");
    var meta = el("div", "q-meta");
    if (q.topic) meta.appendChild(el("span", "chip", q.topic));
    if (q.created) meta.appendChild(el("span", "mono", "asked " + day(q.created)));
    c.appendChild(meta);
    c.appendChild(el("h3", null, q.title || "Untitled question"));
    if (q.context) c.appendChild(el("p", "q-ctx", q.context));

    var d = drafts[id] || (drafts[id] = { option: q.pick ? q.pick.option : "", note: q.pick ? q.pick.note || "" : "" });
    var fs = el("fieldset");
    fs.appendChild(el("legend", null, "Options"));
    var opts = (Array.isArray(q.options) ? q.options : []).concat([{ id: "own", by: "own", label: "My own call", why: "Write it in the note below." }]);
    opts.forEach(function (o) {
      var lab = el("label", "opt");
      var inp = document.createElement("input");
      inp.type = "radio"; inp.name = "q-" + id; inp.value = o.id; inp.id = "q-" + id + "-" + o.id;
      inp.checked = d.option === o.id;
      inp.addEventListener("change", function () { d.option = o.id; });
      lab.appendChild(inp);
      lab.appendChild(el("span", "by by-" + (BY[o.by] ? o.by : "alt"), BY[o.by] || BY.alt));
      lab.appendChild(el("b", null, o.label || ""));
      if (o.why) lab.appendChild(el("span", "why", o.why));
      fs.appendChild(lab);
    });
    c.appendChild(fs);
    if (q.zucc !== "in") c.appendChild(el("p", "zucc-wait", "Zucc hasn't weighed in yet."));

    var nw = el("div", "q-note");
    var nl = el("label", null, "Note (optional, required for your own call)");
    nl.htmlFor = "note-" + id;
    var ta = document.createElement("textarea");
    ta.id = "note-" + id; ta.value = d.note;
    ta.addEventListener("input", function () { d.note = ta.value; });
    nw.appendChild(nl); nw.appendChild(ta);
    c.appendChild(nw);

    var act = el("div", "q-actions");
    var btn = el("button", "primary", "Approve my choice");
    btn.type = "button";
    var msg = el("span", "q-msg mono");
    msg.setAttribute("aria-live", "polite");
    btn.addEventListener("click", function () { save(id, q, opts, btn, msg); });
    act.appendChild(btn);
    if (editing[id]) {
      var cancel = el("button", null, "Keep my earlier answer");
      cancel.type = "button";
      cancel.addEventListener("click", function () { delete editing[id]; delete drafts[id]; render(latest); });
      act.appendChild(cancel);
    }
    act.appendChild(msg);
    c.appendChild(act);
    return c;
  }

  function doneCard(id, q) {
    var c = el("article", "q done");
    var meta = el("div", "q-meta");
    if (q.topic) meta.appendChild(el("span", "chip", q.topic));
    if (q.pick && q.pick.at) meta.appendChild(el("span", "mono", "decided " + day(q.pick.at)));
    c.appendChild(meta);
    c.appendChild(el("h3", null, q.title || "Untitled question"));
    var p = el("div", "picked");
    p.appendChild(el("b", null, "You picked: " + ((q.pick && q.pick.label) || "")));
    if (q.pick && q.pick.note) p.appendChild(el("span", null, q.pick.note));
    c.appendChild(p);
    var act = el("div", "q-actions");
    var b = el("button", null, "Change my answer");
    b.type = "button";
    b.addEventListener("click", function () { editing[id] = true; render(latest); });
    act.appendChild(b);
    c.appendChild(act);
    return c;
  }

  function save(id, q, opts, btn, msg) {
    var d = drafts[id] || {};
    msg.classList.remove("err");
    if (!d.option) { msg.textContent = "Pick an option first."; return; }
    var note = (d.note || "").trim();
    if (d.option === "own" && !note) { msg.textContent = "Write your own call in the note."; return; }
    var chosen = opts.filter(function (o) { return o.id === d.option; })[0];
    var pick = { option: d.option, label: d.option === "own" ? "My own call" : chosen ? chosen.label : d.option, note: note, at: new Date().toISOString() };
    btn.disabled = true;
    msg.textContent = "Saving…";
    var ref = db.doc("questions/" + id);
    function attempt(retry) {
      return ref.update({ status: "decided", pick: pick }).then(function () {
        delete editing[id]; delete drafts[id];
        stateEl.textContent = "Saved. Claude will pass it to Zucc on PR #1.";
      }, function (e) {
        if (e && e.code === "unavailable" && retry) {
          return new Promise(function (r) { setTimeout(r, 600 + Math.random() * 900); }).then(function () { return attempt(false); });
        }
        btn.disabled = false;
        msg.classList.add("err");
        msg.textContent = e && e.code === "invalid_argument" ? "Only Wil's account can vote here." : "Couldn't save. Try again.";
      });
    }
    attempt(true);
  }

  function render(docs) {
    latest = docs;
    var open = [], done = [];
    docs.forEach(function (s) {
      var q = s.data() || {};
      (q.status === "decided" && !editing[s.id] ? done : open).push([s.id, q]);
    });
    open.sort(function (a, b) { return String(a[1].created || "").localeCompare(String(b[1].created || "")); });
    done.sort(function (a, b) { return String((b[1].pick || {}).at || "").localeCompare(String((a[1].pick || {}).at || "")); });
    openEl.replaceChildren.apply(openEl, open.map(function (x) { return card(x[0], x[1]); }));
    doneEl.replaceChildren.apply(doneEl, done.map(function (x) { return doneCard(x[0], x[1]); }));
    doneH.hidden = done.length === 0;
    var n = open.filter(function (x) { return x[1].status !== "decided"; }).length;
    countEl.textContent = String(n);
    countEl.hidden = n === 0;
    if (!docs.length) stateEl.textContent = "No questions right now. New ones show up here when Claude or Zucc need your call.";
    else if (!n) stateEl.textContent = stateEl.textContent.indexOf("Saved") === 0 ? stateEl.textContent : "Nothing waiting on you.";
    else stateEl.textContent = n === 1 ? "1 question waiting on you." : n + " questions waiting on you.";
  }

  if (!window.claude || typeof window.claude.use !== "function") {
    stateEl.textContent = "Voting works when this page is open in claude.ai while you're signed in.";
    return;
  }
  window.claude.use("db").then(function (handle) {
    if (!handle) {
      stateEl.textContent = "Voting works when this page is open in claude.ai while you're signed in.";
      return;
    }
    db = handle;
    db.collection("questions").onSnapshot(function (snap) { render(snap.docs); }, function () {
      stateEl.textContent = "Questions couldn't load. Reload the page.";
    });
  }, function () {
    stateEl.textContent = "Voting works when this page is open in claude.ai while you're signed in.";
  });
})();
