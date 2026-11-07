// The kit quiz. One short question per screen, tap an icon tile, branches by kit.
// Everything runs in the browser: answers live in memory only and are never sent anywhere.
(function () {
  "use strict";

  var EMAIL = "adhdentrepreneurhq@gmail.com";
  var TINTS = ["t-warm", "t-gold", "t-green", "t-cyan", "t-violet"];

  // ---------- the kits (same as the catalog) ----------
  var KITS = {
    service: {
      name: "Local Service Kit", icon: "spray-can", tint: "t-warm",
      pitch: "Your AI handles the messages, quotes and follow-ups after the work.",
      inside: [["message-square", "Reply and quote templates"], ["star", "Follow-up and review scripts"], ["calendar", "Daily scheduling notes"], ["users", "The six-role AI crew"]]
    },
    store: {
      name: "Product Store Kit", icon: "package", tint: "t-gold",
      pitch: "Test a product with your numbers and spending limits worked out first.",
      inside: [["list-checks", "Product checklist and cost sheet"], ["search", "Ad-library product research"], ["shield-check", "Spending limits and stop rules"], ["users", "The six-role AI crew"]]
    },
    content: {
      name: "Content Brand Kit", icon: "clapperboard", tint: "t-cyan",
      pitch: "Post every day and keep it up. Faceless works.",
      inside: [["pencil", "Line bank and 30-day calendar"], ["message-circle", "Captions for each platform"], ["chart-column", "The weekly scorecard"], ["users", "The six-role AI crew"]]
    },
    digital: {
      name: "Digital Product Kit", icon: "file-down", tint: "t-violet",
      pitch: "Turn what you know into a product, with checkout and delivery set up.",
      inside: [["layout-template", "Product build setups"], ["mail", "Sales page and emails"], ["credit-card", "Checkout and delivery guide"], ["users", "The six-role AI crew"]]
    }
  };

  // ---------- the questions ----------
  var Q = {
    build: {
      title: "What are you building?",
      options: [
        { v: "service", t: "A service business", d: "Cleaning, trades, lawns", i: "spray-can" },
        { v: "store", t: "An online store", d: "Physical products", i: "package" },
        { v: "content", t: "A content account", d: "Faceless is fine", i: "smartphone" },
        { v: "digital", t: "A digital product", d: "Templates, guides", i: "file-down" },
        { v: "unsure", t: "Not sure yet", i: "compass" }
      ]
    },
    stage: {
      title: "Where are you at?",
      options: [
        { v: "zero", t: "Not started", i: "sprout" },
        { v: "stalled", t: "Started, then stalled", i: "circle-pause" },
        { v: "running", t: "Up and running", i: "rocket" }
      ]
    },
    vibe: {
      title: "Which sounds like you?",
      options: [
        { v: "service", t: "Good at the work, buried in admin", i: "wrench" },
        { v: "store", t: "I spot products to sell", i: "lightbulb" },
        { v: "content", t: "I've got lots to say", i: "message-circle" },
        { v: "digital", t: "I could teach what I know", i: "graduation-cap" },
        { v: "custom", t: "None of these", i: "puzzle" }
      ]
    },
    service_a: {
      title: "What eats your week?",
      options: [
        { v: "dms", t: "Messages", i: "message-square" },
        { v: "quotes", t: "Quotes", i: "calculator" },
        { v: "follow", t: "Follow-ups and reviews", i: "star" },
        { v: "schedule", t: "Scheduling", i: "calendar" }
      ]
    },
    service_b: {
      title: "Where do leads come from?",
      options: [
        { v: "social", t: "Instagram or Facebook", i: "at-sign" },
        { v: "text", t: "Texts and calls", i: "phone" },
        { v: "google", t: "Google", i: "search" },
        { v: "referral", t: "Word of mouth", i: "users" }
      ]
    },
    store_a: {
      title: "Got a product yet?",
      options: [
        { v: "own", t: "Yes, my own", i: "package-check" },
        { v: "ideas", t: "A few ideas", i: "lightbulb" },
        { v: "none", t: "Not yet", i: "circle-dashed" }
      ]
    },
    store_b: {
      title: "Run ads before?",
      options: [
        { v: "never", t: "Never", i: "sprout" },
        { v: "lost", t: "Yes, and lost money", i: "trending-down" },
        { v: "yes", t: "Yes, I'm comfortable", i: "target" }
      ]
    },
    content_a: {
      title: "Why do you stop posting?",
      options: [
        { v: "ideas", t: "Nothing to say", i: "pencil" },
        { v: "visuals", t: "Visuals take forever", i: "image" },
        { v: "dropoff", t: "I lose steam", i: "battery-low" },
        { v: "unclear", t: "Can't tell if it works", i: "chart-column" }
      ]
    },
    content_b: {
      title: "Show your face?",
      options: [
        { v: "faceless", t: "No, faceless", i: "eye-off" },
        { v: "sometimes", t: "Sometimes", i: "contrast" },
        { v: "yes", t: "Yes", i: "camera" }
      ]
    },
    digital_a: {
      title: "What would you sell?",
      options: [
        { v: "template", t: "A template", i: "layout-template" },
        { v: "guide", t: "A guide or course", i: "book-open" },
        { v: "newsletter", t: "A newsletter", i: "mail" },
        { v: "unsure", t: "Not sure", i: "circle-help" }
      ]
    },
    digital_b: {
      title: "Can you take payments?",
      options: [
        { v: "yes", t: "Yes", i: "credit-card" },
        { v: "no", t: "Not yet", i: "circle-dashed" },
        { v: "unsure", t: "Not sure", i: "circle-help" }
      ]
    },
    ai: {
      title: "Which AI do you use?",
      options: [
        { v: "claude", t: "Claude", i: "sparkles" },
        { v: "chatgpt", t: "ChatGPT", i: "message-circle" },
        { v: "gemini", t: "Gemini", i: "gem" },
        { v: "none", t: "None yet", i: "circle-plus" }
      ]
    },
    hours: {
      title: "Time per week?",
      options: [
        { v: "1", t: "1 to 2 hours", i: "clock-2" },
        { v: "3", t: "3 to 5 hours", i: "clock-5" },
        { v: "6", t: "6 to 10 hours", i: "clock-10" },
        { v: "10", t: "10+ hours", i: "timer" }
      ]
    }
  };

  // ---------- what each answer changes on the result ----------
  var FIRST_UP = {
    service_a: { dms: "First up: replies to new messages, in your voice.", quotes: "First up: quotes your AI drafts from a few details.", follow: "First up: follow-up and review-request scripts.", schedule: "First up: a daily plan drafted from your bookings." },
    store_a: { own: "First up: the cost sheet for your product.", ideas: "First up: scoring your ideas with the checklist.", none: "First up: finding products people already buy." },
    content_a: { ideas: "First up: your line bank. No more blank page.", visuals: "First up: card templates you reuse every day.", dropoff: "First up: a 30-day calendar, built before day one.", unclear: "First up: the weekly scorecard." },
    digital_a: { template: "First up: building your template.", guide: "First up: outlining your guide.", newsletter: "First up: your first three issues.", unsure: "First up: picking what to sell." }
  };
  var SOURCE = { social: "Instagram or Facebook", text: "a text", google: "Google", referral: "a referral" };
  var NOTES = {
    store_b: { never: ["shield-check", "Spending limits get written before any ad money goes out."], lost: ["shield-check", "This time, stop rules come first."], yes: ["shield-check", "You'll still write stop rules first. They're part of the goal."] },
    content_b: { faceless: ["eye-off", "Faceless, like this brand."], sometimes: ["contrast", "Faceless by default, on camera when you want."], yes: ["camera", "On camera works too."] },
    digital_b: { yes: ["credit-card", "Plug in the checkout you already have."], no: ["credit-card", "The kit walks you through taking payments."], unsure: ["credit-card", "The kit walks you through taking payments."] }
  };
  var STAGE = { zero: ["sprout", "Starting from zero is fine."], stalled: ["flag", "Stalled before? The deadline keeps you moving."], running: ["rocket", "You'll build on what you already have."] };
  var AI = {
    claude: ["sparkles", "Built for Claude. Ready to paste."],
    chatgpt: ["message-circle", "Written for Claude. Before you buy, we list what carries over to ChatGPT."],
    gemini: ["gem", "Written for Claude. Before you buy, we list what carries over to Gemini."],
    none: ["circle-plus", "You'll start with Claude, from making the account."]
  };
  var PACE = { "1": "Short sessions. Small steps you can pause.", "3": "A few focused sessions a week.", "6": "Room to finish early.", "10": "You could finish well before the deadline." };

  // ---------- state ----------
  var answers = {};
  var stack = ["build"];
  var busy = false;
  var stage = document.getElementById("stage");
  var bar = document.getElementById("bar");
  var progress = document.getElementById("progress");

  function kitKey() {
    if (answers.build && answers.build !== "unsure") return answers.build;
    return answers.vibe || null;
  }

  function nextOf(id) {
    var k = kitKey();
    switch (id) {
      case "build": return "stage";
      case "stage": return answers.build === "unsure" ? "vibe" : k + "_a";
      case "vibe": return k === "custom" ? "ai" : k + "_a";
      case "service_a": case "store_a": case "content_a": case "digital_a": return k + "_b";
      case "service_b": case "store_b": case "content_b": case "digital_b": return "ai";
      case "ai": return "hours";
    }
    return "result";
  }

  function totalQuestions() {
    if (answers.build !== "unsure") return 6;
    return answers.vibe === "custom" ? 5 : 7;
  }
  function questionNumber() {
    return stack.filter(function (id) { return id !== "result"; }).length;
  }

  // ---------- helpers ----------
  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }
  var SVGNS = "http://www.w3.org/2000/svg";
  function icon(name) {
    var svg = document.createElementNS(SVGNS, "svg");
    svg.setAttribute("class", "ic");
    svg.setAttribute("aria-hidden", "true");
    var use = document.createElementNS(SVGNS, "use");
    use.setAttribute("href", "assets/icons.svg#" + name);
    svg.append(use);
    return svg;
  }
  function chip(name, cls) {
    var c = el("span", "chip" + (cls ? " " + cls : ""));
    c.append(icon(name));
    return c;
  }
  function splitButton(label, href) {
    var b = el(href ? "a" : "button", "btn-split");
    if (href) b.href = href; else b.type = "button";
    var fx = el("span", "fx");
    fx.setAttribute("aria-hidden", "true");
    fx.append(el("i"), el("i"), el("i"));
    b.append(fx, el("span", "lbl", label));
    return b;
  }
  function glassButton(label, href) {
    var b = el(href ? "a" : "button", "btn glass", label);
    if (href) b.href = href; else b.type = "button";
    return b;
  }
  function setProgress(fraction) {
    var pct = Math.round(Math.max(0, Math.min(1, fraction)) * 100);
    bar.style.width = pct + "%";
    progress.setAttribute("aria-valuenow", String(pct));
  }
  function pad(n) { return (n < 10 ? "0" : "") + n; }

  // ---------- navigation ----------
  function go(id) {
    stack.push(id);
    history.pushState({ n: stack.length }, "");
    render();
  }
  window.addEventListener("popstate", function (e) {
    var n = (e.state && e.state.n) || 1;
    while (stack.length > n) stack.pop();
    busy = false;
    render();
  });

  function meta(id) {
    var row = el("div", "qmeta");
    if (stack.length > 1) {
      var back = el("button", "back", "← Back");
      back.type = "button";
      back.addEventListener("click", function () { history.back(); });
      row.append(back);
    } else {
      row.append(el("span"));
    }
    if (id !== "result") row.append(el("span", "label", pad(questionNumber()) + " / " + pad(totalQuestions())));
    return row;
  }

  // ---------- screens ----------
  function render() {
    var id = stack[stack.length - 1];
    stage.textContent = "";
    var screen = el("div", "screen");
    stage.append(screen);
    screen.append(meta(id));
    if (id === "result") { renderResult(screen); setProgress(1); }
    else { renderChoice(screen, id); setProgress((questionNumber() - 1) / totalQuestions()); }
    var h = stage.querySelector("h1");
    if (h) { h.setAttribute("tabindex", "-1"); h.focus({ preventScroll: true }); }
    window.scrollTo(0, 0);
  }

  function renderChoice(screen, id) {
    var q = Q[id];
    screen.append(el("h1", "qtitle", q.title));
    var list = el("div", "tiles");
    list.setAttribute("role", "group");
    list.setAttribute("aria-label", q.title);
    q.options.forEach(function (o, i) {
      var b = el("button", "tile glass tinted " + TINTS[i % TINTS.length]);
      b.type = "button";
      b.append(chip(o.i));
      var txt = el("span", "ttext");
      txt.append(el("span", "t", o.t));
      if (o.d) txt.append(el("span", "d", o.d));
      b.append(txt, el("span", "key", String(i + 1)));
      if (answers[id] === o.v) b.classList.add("was");
      b.addEventListener("click", function () { choose(id, o.v, b); });
      list.append(b);
    });
    screen.append(list);
  }

  function choose(id, v, tile) {
    if (busy) return;
    busy = true;
    answers[id] = v;
    stage.querySelectorAll(".tile").forEach(function (t) { t.classList.remove("was"); });
    tile.classList.add("picked");
    tile.setAttribute("aria-pressed", "true");
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    setTimeout(function () { busy = false; go(nextOf(id)); }, reduce ? 60 : 340);
  }

  function block(iconName, title) {
    var b = el("section", "rblock glass");
    var h = el("div", "rbhead");
    h.append(chip(iconName, "sm"), el("span", "label", title));
    b.append(h);
    return b;
  }
  function line(list, iconName, text) {
    var li = el("li");
    li.append(icon(iconName), el("span", null, text));
    list.append(li);
  }

  function renderResult(screen) {
    var key = kitKey();
    if (!KITS[key]) { renderCustom(screen); return; }
    var k = KITS[key];

    // 1. The kit
    var head = el("div", "rhead glass tinted " + k.tint);
    head.append(chip(k.icon, "lg"));
    var ht = el("div");
    ht.append(el("span", "label", "Your kit"), el("h1", "qtitle", k.name), el("p", "qsub", k.pitch));
    head.append(ht);
    screen.append(head);

    var inside = block("layers", "What's inside");
    inside.classList.add("tinted", k.tint);
    var first = FIRST_UP[key + "_a"] && FIRST_UP[key + "_a"][answers[key + "_a"]];
    if (first) inside.append(el("p", "strong", first));
    var ul = el("ul", "inside");
    k.inside.forEach(function (x) { line(ul, x[0], x[1]); });
    inside.append(ul);
    screen.append(inside);

    // 2. The goal and deadline
    var goal = block("flag", "Your goal");
    goal.append(el("p", "strong", goalFor(key)));
    var gl = el("ul", "inside plain");
    line(gl, "clock", "Deadline: set when you buy, shown before you pay.");
    line(gl, "badge-check", "Proof: screenshots or a short screen recording.");
    goal.append(gl);
    screen.append(goal);

    // 3. Setup for their AI, plus what their answers changed
    var plan = block("compass", "Your setup");
    var pl = el("ul", "inside plain");
    var ai = AI[answers.ai] || AI.claude;
    line(pl, ai[0], ai[1]);
    if (answers.hours) line(pl, "clock", PACE[answers.hours]);
    var note = NOTES[key + "_b"] && NOTES[key + "_b"][answers[key + "_b"]];
    if (note) line(pl, note[0], note[1]);
    if (answers.stage) line(pl, STAGE[answers.stage][0], STAGE[answers.stage][1]);
    plan.append(pl);
    screen.append(plan);

    // 4. Price and terms
    var price = block("credit-card", "Price and guarantee");
    var prl = el("ul", "inside plain");
    line(prl, "tag", "Price: set at launch, shown before you pay.");
    line(prl, "badge-check", "Finish on time and send the proof: full refund.");
    line(prl, "circle-dashed", "Miss the deadline: no refund, and the kit stays yours.");
    price.append(prl);
    var terms = el("p", "muted");
    terms.append(document.createTextNode("Not on sale yet, so nothing is charged here. "));
    var a = el("a", null, "Full terms");
    a.href = "policies.html#refunds";
    terms.append(a, document.createTextNode("."));
    price.append(terms);
    screen.append(price);

    var actions = el("div", "qactions");
    actions.append(splitButton("Email me at launch", launchMail(k.name)), glassButton("Browse the catalog", "kits.html"));
    screen.append(actions, retake());
  }

  function renderCustom(screen) {
    var head = el("div", "rhead glass tinted t-green");
    head.append(chip("puzzle", "lg"));
    var ht = el("div");
    ht.append(el("span", "label", "Your kit"), el("h1", "qtitle", "A custom kit"), el("p", "qsub", "You don't fit a category yet. Tell us what you're building. New kits come from requests like yours."));
    head.append(ht);
    screen.append(head);
    var actions = el("div", "qactions");
    actions.append(splitButton("Tell us what you're building", "mailto:" + EMAIL + "?subject=" + encodeURIComponent("Kit idea")), glassButton("Browse the catalog", "kits.html"));
    screen.append(actions, retake());
  }

  function goalFor(key) {
    if (key === "service") {
      var src = SOURCE[answers.service_b];
      return "A test lead " + (src ? "from " + src + " " : "") + "goes from first message to quote, follow-up and review request. Then it's switched on for real leads.";
    }
    if (key === "store") return "Your store is live with one product page, your cost sheet and written spending limits, and a test order goes through.";
    if (key === "content") return "14 posts in 14 days on your own accounts, with your weekly scorecard filled in.";
    return "Your product is live with a working checkout, and a test purchase gets delivered automatically.";
  }

  function launchMail(name) {
    var body = "Please email me when the " + name + " launches.\n\n(We only use your address to tell you about kit launches. Ask us anytime and we'll delete it.)";
    return "mailto:" + EMAIL + "?subject=" + encodeURIComponent("Launch list: " + name) + "&body=" + encodeURIComponent(body);
  }
  function retake() {
    var p = el("p", "retake");
    var b = el("button", "linkish", "Retake the quiz");
    b.type = "button";
    b.addEventListener("click", function () { window.location.replace("quiz.html"); });
    p.append(b);
    return p;
  }

  // Number keys pick an option.
  document.addEventListener("keydown", function (e) {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    var n = parseInt(e.key, 10);
    if (!n) return;
    var tiles = stage.querySelectorAll(".tile");
    if (tiles[n - 1]) tiles[n - 1].click();
  });

  history.replaceState({ n: 1 }, "");
  render();
})();
