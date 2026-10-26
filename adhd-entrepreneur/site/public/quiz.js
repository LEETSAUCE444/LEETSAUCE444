// The kit quiz. One question per screen, tap to answer, branches by kit.
// Everything runs in the browser: answers live in memory only and are never sent anywhere.
(function () {
  "use strict";

  var EMAIL = "adhdentrepreneurhq@gmail.com";

  // ---------- the kits ----------
  var KITS = {
    service: {
      num: "01", name: "Local Service Kit", leans: "Physical",
      pitch: "Your AI handles the messages, quotes and follow-ups that pile up after the work.",
      box: ["Quote and reply templates in your own voice", "Follow-up and review-request scripts", "Daily scheduling notes", "The six-role AI crew, set up for a service business"],
      next: "content",
      placeholder: "e.g. Every new lead gets a quote the same day, without me typing it."
    },
    store: {
      num: "02", name: "Product Store Kit", leans: "Physical",
      pitch: "Test a physical product online with the numbers and your spending limits worked out first.",
      box: ["Product checklist and cost sheet", "How to research products in public ad libraries", "Spending-limit and stop-rule templates", "The six-role AI crew, set up for a store"],
      next: "content",
      placeholder: "e.g. My store is live and I know my numbers before I spend anything."
    },
    content: {
      num: "03", name: "Content Brand Kit", leans: "Digital",
      pitch: "Post every day and keep it up. Faceless works, and this brand runs on the same setup.",
      box: ["Line bank and 30-day calendar builder", "Captions for each platform", "The weekly scorecard: saves and shares, not vanity numbers", "The six-role AI crew, set up for a content brand"],
      next: null,
      placeholder: "e.g. I post every day without staring at a blank screen."
    },
    digital: {
      num: "04", name: "Digital Product Kit", leans: "Digital",
      pitch: "Turn what you know into a template, guide or small newsletter, with checkout and delivery set up.",
      box: ["Product build setups", "Sales page template and email sequence", "Checkout and delivery guide", "The six-role AI crew, set up for a digital product"],
      next: "content",
      placeholder: "e.g. My template is for sale and delivers itself after checkout."
    }
  };

  // ---------- the questions ----------
  var Q = {
    build: {
      title: "What do you want AI to help you build?",
      sub: "Pick the closest one.",
      options: [
        { v: "service", t: "Run my service business with less admin", d: "Cleaning, washing, landscaping, trades" },
        { v: "store", t: "Sell a physical product online", d: "Your own product, or one you want to test" },
        { v: "content", t: "An account that posts every day", d: "Faceless is fine" },
        { v: "digital", t: "Sell something digital", d: "A template, a guide or a small newsletter" },
        { v: "unsure", t: "Not sure yet", d: "We'll narrow it down" }
      ]
    },
    stage: {
      title: "Where are you right now?",
      options: [
        { v: "zero", t: "Haven't started" },
        { v: "stalled", t: "Started, then stalled" },
        { v: "running", t: "It's running. I want it automated." }
      ]
    },
    how: { type: "info" },
    vibe: {
      title: "Which one sounds most like you?",
      options: [
        { v: "service", t: "I'm good at the work. The texts, quotes and follow-ups bury me." },
        { v: "store", t: "I see products and think: I could sell that." },
        { v: "content", t: "I have plenty to say. I just never keep posting." },
        { v: "digital", t: "I know how to do something people would pay to learn." },
        { v: "custom", t: "None of these" }
      ]
    },
    service_a: {
      title: "What eats most of your week?",
      options: [
        { v: "dms", t: "Answering messages and texts" },
        { v: "quotes", t: "Writing quotes" },
        { v: "follow", t: "Following up and asking for reviews" },
        { v: "schedule", t: "Scheduling and planning the day" }
      ]
    },
    service_b: {
      title: "Where do most of your leads come from?",
      options: [
        { v: "social", t: "Instagram or Facebook messages" },
        { v: "text", t: "Texts and calls" },
        { v: "google", t: "Google" },
        { v: "referral", t: "Word of mouth" }
      ]
    },
    store_a: {
      title: "Do you have a product yet?",
      options: [
        { v: "own", t: "Yes, my own product" },
        { v: "ideas", t: "A few ideas I want to test" },
        { v: "none", t: "Not yet" }
      ]
    },
    store_b: {
      title: "Have you run paid ads before?",
      options: [
        { v: "never", t: "Never" },
        { v: "lost", t: "Tried it and lost money" },
        { v: "yes", t: "Yes, I'm comfortable with them" }
      ]
    },
    content_a: {
      title: "What usually makes you stop posting?",
      options: [
        { v: "ideas", t: "I run out of things to say" },
        { v: "visuals", t: "Making the visuals takes forever" },
        { v: "dropoff", t: "I start strong, then drop off" },
        { v: "unclear", t: "I can't tell if it's working" }
      ]
    },
    content_b: {
      title: "Do you want to show your face?",
      options: [
        { v: "faceless", t: "No, faceless" },
        { v: "sometimes", t: "Sometimes" },
        { v: "yes", t: "Yes" }
      ]
    },
    digital_a: {
      title: "What would you sell?",
      options: [
        { v: "template", t: "A template or toolkit" },
        { v: "guide", t: "A guide or short course" },
        { v: "newsletter", t: "A small paid newsletter" },
        { v: "unsure", t: "Not sure yet" }
      ]
    },
    digital_b: {
      title: "Can you take payments online yet?",
      options: [
        { v: "yes", t: "Yes" },
        { v: "no", t: "Not yet" },
        { v: "unsure", t: "Not sure" }
      ]
    },
    ai: {
      title: "Which AI do you use now?",
      options: [
        { v: "claude", t: "Claude" },
        { v: "chatgpt", t: "ChatGPT" },
        { v: "gemini", t: "Gemini" },
        { v: "none", t: "None yet" }
      ]
    },
    hours: {
      title: "How many hours a week can you give this?",
      options: [
        { v: "1", t: "1 to 2 hours" },
        { v: "3", t: "3 to 5 hours" },
        { v: "6", t: "6 to 10 hours" },
        { v: "10", t: "More than 10" }
      ]
    },
    finish: {
      type: "text",
      title: "Last one. In your own words, what would “done” look like?",
      sub: "Optional. It shows up on your result and stays on this device."
    }
  };

  // ---------- what each answer changes on the result ----------
  var FIRST_UP = {
    service_a: {
      dms: "First up: replies to new messages, drafted the way you talk.",
      quotes: "First up: quote templates your AI fills in from a few details.",
      follow: "First up: follow-up and review-request scripts, and when to send each one.",
      schedule: "First up: a daily plan your AI drafts from your bookings."
    },
    store_a: {
      own: "First up: your cost sheet, to check the numbers on your product before any spending.",
      ideas: "First up: the product checklist, to score your ideas against the same rules.",
      none: "First up: finding products people already buy, using public ad libraries. No paid research tools needed."
    },
    content_a: {
      ideas: "First up: your line bank, so you never start from a blank page.",
      visuals: "First up: card templates you reuse every day.",
      dropoff: "First up: a 30-day calendar built before day one, so every day is already decided.",
      unclear: "First up: the weekly scorecard, so you know what's working."
    },
    digital_a: {
      template: "First up: building the template itself, with your AI doing the first drafts.",
      guide: "First up: outlining the guide, then drafting it section by section.",
      newsletter: "First up: your first three issues, drafted before launch.",
      unsure: "First up: picking the product, from what you already know how to do."
    }
  };

  var SOURCE = { social: "Instagram or Facebook", text: "a text", google: "Google", referral: "a referral" };

  var NOTES = {
    store_b: {
      never: "Never run ads? You don't need to have. Your spending limit and stop rules get written before a single dollar goes out.",
      lost: "Lost money on ads before? This time the stop rules come first, written down before anything is spent.",
      yes: "You know ads already. The kit still has you write your spending limit and stop rules first. They're part of the goal."
    },
    content_b: {
      faceless: "Faceless is how this brand runs too.",
      sometimes: "Faceless by default, with room for you on camera when you want it.",
      yes: "On camera works too. The line bank and calendar don't care either way."
    },
    digital_b: {
      yes: "You can take payments already, so you'll plug your checkout straight in.",
      no: "The checkout and delivery guide walks you through taking payments.",
      unsure: "The checkout and delivery guide walks you through taking payments."
    }
  };

  var STAGE_NOTE = {
    zero: "Starting from zero is fine. The checklist starts at step one.",
    stalled: "Stalled before? That's what the deadline and the money on the line are for.",
    running: "Already running? You'll set the kit up on top of what you have."
  };

  var AI_NOTE = {
    claude: "You're on Claude, which the kit is written for. The six crew roles are ready to paste in.",
    chatgpt: "The kit is written for Claude. Before you buy, it lists exactly what carries over to ChatGPT and what doesn't.",
    gemini: "The kit is written for Claude. Before you buy, it lists exactly what carries over to Gemini and what doesn't.",
    none: "You'll start with Claude. The setup guide begins at making the account, then the crew."
  };

  var PACE = {
    "1": "At 1 to 2 hours a week, plan on short sessions. The checklist is split into small steps you can stop and pick back up.",
    "3": "At 3 to 5 hours a week, a few focused sessions keeps you on pace.",
    "6": "At 6 to 10 hours a week, you have room to finish early. Do the setup in week one.",
    "10": "With 10+ hours a week, you could finish well before the deadline. Do the setup in week one."
  };

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
      case "stage": return "how";
      case "how": return answers.build === "unsure" ? "vibe" : k + "_a";
      case "vibe": return k === "custom" ? "ai" : k + "_a";
      case "service_a": case "store_a": case "content_a": case "digital_a": return k + "_b";
      case "service_b": case "store_b": case "content_b": case "digital_b": return "ai";
      case "ai": return "hours";
      case "hours": return "finish";
      case "finish": return "result";
    }
    return "result";
  }

  // Questions on this path (the heads-up screen doesn't count).
  function totalQuestions() {
    var n = 7;
    if (answers.build === "unsure") n += 1;
    if (answers.vibe === "custom" && answers.build === "unsure") n -= 2;
    return n;
  }
  function questionNumber() {
    return stack.filter(function (id) { return id !== "how" && id !== "result"; }).length;
  }

  // ---------- helpers ----------
  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
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
  function focusTitle() {
    var h = stage.querySelector("h1");
    if (h) { h.setAttribute("tabindex", "-1"); h.focus({ preventScroll: true }); }
    window.scrollTo(0, 0);
  }

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

  function meta() {
    var row = el("div", "qmeta");
    if (stack.length > 1) {
      var back = el("button", "back", "← Back");
      back.type = "button";
      back.addEventListener("click", function () { history.back(); });
      row.append(back);
    } else {
      row.append(el("span"));
    }
    var id = stack[stack.length - 1];
    if (id !== "how" && id !== "result") {
      var num = questionNumber(), tot = totalQuestions();
      row.append(el("span", "label", pad(num) + " / " + pad(tot)));
    }
    return row;
  }
  function pad(n) { return (n < 10 ? "0" : "") + n; }

  // ---------- screens ----------
  function render() {
    var id = stack[stack.length - 1];
    stage.textContent = "";
    var screen = el("div", "screen");
    stage.append(screen);
    screen.append(meta());

    if (id === "result") { renderResult(screen); setProgress(1); }
    else if (id === "how") { renderInfo(screen); setProgress((questionNumber()) / totalQuestions()); }
    else if (Q[id].type === "text") { renderText(screen, id); setProgress((questionNumber() - 1) / totalQuestions()); }
    else { renderChoice(screen, id); setProgress((questionNumber() - 1) / totalQuestions()); }
    focusTitle();
  }

  function renderChoice(screen, id) {
    var q = Q[id];
    screen.append(el("h1", "qtitle", q.title));
    if (q.sub) screen.append(el("p", "qsub", q.sub));
    var list = el("div", "options");
    list.setAttribute("role", "group");
    list.setAttribute("aria-label", q.title);
    q.options.forEach(function (o, i) {
      var b = el("button", "opt glass");
      b.type = "button";
      b.dataset.v = o.v;
      var txt = el("span", "otext");
      txt.append(el("span", "t", o.t));
      if (o.d) txt.append(el("span", "d", o.d));
      b.append(txt, el("span", "key", String(i + 1)));
      if (answers[id] === o.v) { b.classList.add("was"); b.setAttribute("aria-pressed", "true"); }
      b.addEventListener("click", function () { choose(id, o.v, b); });
      list.append(b);
    });
    screen.append(list);
  }

  function choose(id, v, button) {
    if (busy) return;
    busy = true;
    answers[id] = v;
    stage.querySelectorAll(".opt").forEach(function (o) { o.classList.remove("was"); o.removeAttribute("aria-pressed"); });
    button.classList.add("picked");
    button.setAttribute("aria-pressed", "true");
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    setTimeout(function () { busy = false; go(nextOf(id)); }, reduce ? 60 : 300);
  }

  function renderInfo(screen) {
    screen.append(el("h1", "qtitle", "Quick heads-up on how every kit works"));
    var card = el("div", "infocard glass");
    var lines = [
      ["One goal", "Each kit has one build goal and one deadline, shown before you pay."],
      ["Finish it", "Hit the goal on time, send the proof, and you get your money back."],
      ["Miss it", "You keep the kit and get 50% off your next one."]
    ];
    lines.forEach(function (l) {
      var row = el("div", "inforow");
      row.append(el("span", "label", l[0]), el("p", null, l[1]));
      card.append(row);
    });
    screen.append(card);
    if (answers.stage) screen.append(el("p", "qsub", STAGE_NOTE[answers.stage]));
    var actions = el("div", "qactions");
    var ok = splitButton("Got it");
    ok.addEventListener("click", function () {
      if (busy) return;
      busy = true;
      setTimeout(function () { busy = false; go(nextOf("how")); }, 300);
    });
    actions.append(ok);
    screen.append(actions);
  }

  function renderText(screen, id) {
    var q = Q[id];
    var k = KITS[kitKey()];
    screen.append(el("h1", "qtitle", q.title));
    screen.append(el("p", "qsub", q.sub));
    var label = el("label", "sr-only", "Your answer");
    label.htmlFor = "finishline";
    var ta = el("textarea", "finish glass");
    ta.id = "finishline";
    ta.rows = 3;
    ta.maxLength = 200;
    ta.placeholder = k ? k.placeholder : "e.g. The thing I keep putting off is finally live.";
    ta.value = answers[id] || "";
    screen.append(label, ta);
    var actions = el("div", "qactions");
    var next = splitButton("See my kit");
    var skip = glassButton("Skip");
    function done(save) {
      if (busy) return;
      busy = true;
      answers[id] = save ? ta.value.trim() : "";
      setTimeout(function () { busy = false; go("result"); }, 300);
    }
    next.addEventListener("click", function () { done(true); });
    skip.addEventListener("click", function () { done(false); });
    actions.append(next, skip);
    screen.append(actions);
  }

  function block(n, title) {
    var b = el("section", "rblock glass");
    b.append(el("span", "label", n + " · " + title));
    return b;
  }

  function renderResult(screen) {
    var key = kitKey();
    var head = el("div", "rhead");
    var tag = el("div", "rtag");
    var bar5 = el("div", "splitbar");
    bar5.setAttribute("aria-hidden", "true");
    for (var i = 0; i < 5; i++) bar5.append(el("i"));
    tag.append(el("span", "label", "Your match"), bar5);
    head.append(tag);

    if (key === "custom" || !KITS[key]) { renderCustom(screen, head); return; }
    var k = KITS[key];
    var h = el("h1", "qtitle rtitle");
    h.append(el("span", "rnum", k.num), document.createTextNode(k.name));
    head.append(h, el("p", "qsub", k.pitch));
    screen.append(head);

    var first = FIRST_UP[key + "_a"] && FIRST_UP[key + "_a"][answers[key + "_a"]];

    // 1. The kit
    var b1 = block("1", "The kit");
    if (first) b1.append(el("p", "strong", first));
    var ul = el("ul", "ticks");
    k.box.forEach(function (x) { ul.append(el("li", null, x)); });
    b1.append(ul);
    var extra = NOTES[key + "_b"] && NOTES[key + "_b"][answers[key + "_b"]];
    if (extra) b1.append(el("p", "muted", extra));
    screen.append(b1);

    // 2. The goal and deadline
    var b2 = block("2", "Your build goal");
    b2.append(el("p", "strong", goalFor(key)));
    var dl = el("dl", "rlist");
    addRow(dl, "Deadline", "Fixed when you buy, and shown before you pay.");
    addRow(dl, "Proof", "Screenshots or a short screen recording.");
    if (answers.hours) addRow(dl, "Your pace", PACE[answers.hours]);
    b2.append(dl);
    if (answers.finish) {
      var mine = el("blockquote", "mine");
      mine.append(el("span", "label", "Done, in your words"), el("p", null, "“" + answers.finish + "”"));
      b2.append(mine);
    }
    if (answers.stage) b2.append(el("p", "muted", STAGE_NOTE[answers.stage]));
    screen.append(b2);

    // 3. Setup for their AI
    var b3 = block("3", "Setup for your AI");
    b3.append(el("p", null, AI_NOTE[answers.ai] || AI_NOTE.claude));
    b3.append(el("p", "muted", "You sign up for your AI yourself and pay for it directly."));
    screen.append(b3);

    // 4. Price and terms
    var b4 = block("4", "Price and terms");
    var dl4 = el("dl", "rlist");
    addRow(dl4, "Price", "Set at launch. Shown before you pay, with every term below.");
    addRow(dl4, "Finish on time", "Send the proof and get a full refund.");
    addRow(dl4, "Miss it", "Keep the kit and get 50% off " + (k.next ? "the " + KITS[k.next].name : "the kit that fits your next step") + ".");
    b4.append(dl4);
    var terms = el("p", "muted");
    terms.append(document.createTextNode("Not on sale yet, so there's no checkout here and nothing is charged. Full terms: "));
    var a = el("a", null, "refund policy");
    a.href = "policies.html#refunds";
    terms.append(a, document.createTextNode("."));
    b4.append(terms);
    screen.append(b4);

    var actions = el("div", "qactions");
    actions.append(splitButton("Email me when it launches", launchMail(k.name)), glassButton("See all kits", "./#kits"));
    screen.append(actions);
    screen.append(retake());
  }

  function renderCustom(screen, head) {
    var h = el("h1", "qtitle rtitle", "A kit built around you");
    head.append(h, el("p", "qsub", "What you're building doesn't fit one of the four kits yet. More kits get added based on what people ask for, so tell us about it."));
    screen.append(head);
    var b = block("1", "What to send us");
    var ul = el("ul", "ticks");
    ["What you're building, in a sentence or two", "Which AI you use now: " + optLabel("ai", answers.ai), "How much time you have: " + optLabel("hours", answers.hours)].forEach(function (x) { ul.append(el("li", null, x)); });
    b.append(ul);
    if (answers.finish) {
      var mine = el("blockquote", "mine");
      mine.append(el("span", "label", "Done, in your words"), el("p", null, "“" + answers.finish + "”"));
      b.append(mine);
    }
    screen.append(b);
    var actions = el("div", "qactions");
    actions.append(splitButton("Tell us what you're building", "mailto:" + EMAIL + "?subject=" + encodeURIComponent("Kit idea")), glassButton("See the 4 kits", "./#kits"));
    screen.append(actions);
    screen.append(retake());
  }

  function goalFor(key) {
    if (key === "service") {
      var src = SOURCE[answers.service_b];
      return "A test lead " + (src ? "from " + src + " " : "") + "goes from first message to a quote, a follow-up and a review request, start to finish. Then you switch it on for real leads.";
    }
    if (key === "store") return "Your store is live with one product page, your cost sheet and your written spending limits, and a test order goes through.";
    if (key === "content") return "14 posts in 14 days on your own accounts, with your weekly scorecard filled in.";
    return "Your product is live with a working checkout, and a test purchase gets delivered automatically.";
  }

  function addRow(dl, term, def) {
    var row = el("div", "rrow");
    row.append(el("dt", null, term), el("dd", null, def));
    dl.append(row);
  }
  function optLabel(qid, v) {
    var o = (Q[qid].options || []).filter(function (x) { return x.v === v; })[0];
    return o ? o.t : "not answered";
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
    if (e.target && (e.target.tagName === "TEXTAREA" || e.target.tagName === "INPUT")) return;
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    var n = parseInt(e.key, 10);
    if (!n) return;
    var opts = stage.querySelectorAll(".opt");
    if (opts[n - 1]) opts[n - 1].click();
  });

  history.replaceState({ n: 1 }, "");
  render();
})();
