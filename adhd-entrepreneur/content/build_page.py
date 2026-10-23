#!/usr/bin/env python3
"""Render calendar-30.html (the approval page) from build_calendar.py's output.

Usage:
    python3 build_calendar.py && python3 build_page.py
"""
import base64
import html
import io
import json
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
AVATAR = os.path.join(HERE, "..", "brand", "avatar", "draft", "ae-avatar-fullbleed-1080.png")
SHORT = {"R": "Reminder", "T": "Tip", "A": "AI", "F": "Founder"}
TRACK = {"She": "she", "Potato Salad": "potato", "Louise": "louise"}


def esc(s):
    return html.escape(s, quote=True)


def lines_html(line):
    return "<br>".join(esc(p) for p in line.split("\n"))


def avatar_uri():
    im = Image.open(AVATAR).convert("RGB").resize((96, 96), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


def copy_block(label, text, key):
    return (f'<div class="copy"><div class="copy-head"><span>{label}</span>'
            f'<button type="button" class="btn-copy" data-copy="{key}">Copy</button></div>'
            f'<pre id="{key}">{esc(text)}</pre></div>')


def track_of(music):
    for name, cls in TRACK.items():
        if music.startswith(name):
            return name, cls
    return music, ""


def day_html(r, av):
    n = r["day"]
    name, cls = track_of(r["music"])
    start = r["music"].split(" from ")[-1]
    new = r["source"] == "new"
    tags = [f'<span class="chip chip-{r["slot"]}">{SHORT[r["slot"]]}</span>']
    if r.get("status"):
        tags.append(f'<span class="chip chip-status">{esc(r["status"].title())}</span>')
    elif new:
        tags.append('<span class="chip chip-new">New line</span>')
    else:
        tags.append(f'<span class="chip chip-src">Bank #{r["source"].split()[1]}</span>')
    meta = (f'<div class="meta"><span class="mono">{esc(r["date_label"])}</span>'
            f'<span class="track t-{cls}">{esc(name)} <span class="mono">{start}</span></span>'
            f'<span class="mono links">{"links on" if r["links"] == "yes" else "no links"}</span></div>')
    card = (f'<figure class="card"><div class="card-head"><span class="av" aria-hidden="true"></span>'
            f'<div><b>ADHD Entrepreneur</b><span>@adhdentrepreneurhq</span></div></div>'
            f'<blockquote>{lines_html(r["line"])}</blockquote>'
            f'<figcaption class="mono">{r["words"]} words{" · " + esc(r["pattern"]) if r.get("pattern") else ""}</figcaption></figure>')
    extra = []
    if r.get("condition"):
        extra.append(f'<p class="flag"><b>Condition.</b> {esc(r["condition"])}</p>')
    if r.get("note"):
        extra.append(f'<p class="flag"><b>Note.</b> {esc(r["note"])}</p>')
    detail = ""
    if r["source"] != "live":
        k = f"d{n}"
        blocks = [copy_block("Instagram caption", r["ig"], f"{k}-ig"),
                  copy_block("TikTok caption", r["tiktok"], f"{k}-tt"),
                  copy_block("YouTube Short title", r["yt_title"], f"{k}-yt"),
                  copy_block("X post (plain text)", r["x"], f"{k}-x")]
        if r.get("variants"):
            blocks.append('<div class="variants"><span>Hook variants</span><ul>'
                          + "".join(f"<li>{esc(v)}</li>" for v in r["variants"]) + "</ul></div>")
        detail = (f'<details id="det-{n}"><summary>Captions for Day {n}</summary>'
                  f'<div class="copies">{"".join(blocks)}</div></details>')
    else:
        detail = '<p class="done mono">Captions already written by Zucc.</p>'
    data = f'data-slot="{r["slot"]}" data-new="{"1" if new else "0"}" data-date="{r["date"]}"'
    return (f'<article class="day" id="day-{n}" {data}>'
            f'<div class="day-side"><div class="num">Day {n}</div>{"".join(tags)}{meta}</div>'
            f'<div class="day-main">{card}{"".join(extra)}{detail}</div></article>')


def strip_html(rows):
    cells = []
    for r in rows:
        name, cls = track_of(r["music"])
        cells.append(f'<a href="#day-{r["day"]}" class="cell t-{cls}{" on" if r["links"] == "yes" else ""}" '
                     f'data-date="{r["date"]}" title="Day {r["day"]}: {esc(name)}">{r["day"]}</a>')
    return "".join(cells)


def main():
    rows = json.load(open(os.path.join(HERE, "calendar-30.rows.json")))
    md = open(os.path.join(HERE, "calendar-30.md")).read()
    av = avatar_uri()
    counts = {k: sum(r["slot"] == k for r in rows) for k in "RTAF"}
    weeks = [(1, 7), (8, 14), (15, 21), (22, 28), (29, 30)]
    body = []
    for a, b in weeks:
        title = f"Days {a}–{b}"
        sub = {1: "Launch week · no links", 8: "Week 2 · no links", 15: "Links go live on Day 15 (Thu Nov 5)",
               22: "Week 4", 29: "Final two days"}[a]
        body.append(f'<section class="week"><header class="week-head"><h2>{title}</h2>'
                    f'<span class="mono">{sub}</span></header>')
        body += [day_html(r, av) for r in rows if a <= r["day"] <= b]
        body.append("</section>")
    page = TEMPLATE.format(
        strip=strip_html(rows), days="\n".join(body), md=esc(md), av=av,
        r=counts["R"], t=counts["T"], a=counts["A"], f=counts["F"],
        new=sum(r["source"] == "new" for r in rows))
    with open(os.path.join(HERE, "calendar-30.html"), "w") as fh:
        fh.write(page)
    print("wrote calendar-30.html", len(page) // 1024, "KB")


TEMPLATE = """<title>ADHD Entrepreneur 30-Day Calendar</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Layout: one column of days, each a tweet-card preview beside its schedule data; the brand's black/white only. */
:root {{
  --paper: #FFFFFF; --ink: #0B0B0B; --muted: #5F5F5F; --rule: #E2E2E2; --wash: #F2F2F2; --card: #FFFFFF;
  --mid: #8C8C8C;
  --display: "Archivo", "Helvetica Neue", Arial, sans-serif;
  --body: "Archivo", "Helvetica Neue", Arial, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --paper: #000000; --ink: #F2F2F2; --muted: #A0A0A0; --rule: #262626; --wash: #141414; --card: #0B0B0B; --mid: #6E6E6E; color-scheme: dark; }} }}
:root[data-theme="dark"] {{
  --paper: #000000; --ink: #F2F2F2; --muted: #A0A0A0; --rule: #262626; --wash: #141414; --card: #0B0B0B; --mid: #6E6E6E; color-scheme: dark; }}
body {{ background: var(--paper); color: var(--ink); font: 15px/1.5 var(--body); }}
.wrap {{ max-width: 980px; margin: 0 auto; padding-block: 28px 64px;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
.mono {{ font-family: var(--mono); font-size: 12px; letter-spacing: .01em; }}
h1 {{ font: 800 clamp(28px, 6vw, 44px)/1.05 var(--display); letter-spacing: -.02em; margin: 0; text-wrap: balance; }}
.lede {{ color: var(--muted); max-width: 62ch; margin: 10px 0 0; }}
.top {{ display: grid; gap: 22px; border-bottom: 2px solid var(--ink); padding-bottom: 26px; }}
.label {{ font: 700 11px/1 var(--display); text-transform: uppercase; letter-spacing: .12em; color: var(--muted); margin-bottom: 8px; }}
.mix {{ display: flex; height: 34px; border: 1.5px solid var(--ink); }}
.mix > div {{ display: flex; align-items: center; padding: 0 8px; font: 700 12px var(--display); white-space: nowrap; overflow: hidden; min-width: 0; }}
.mix .R {{ flex: {r}; background: var(--ink); color: var(--paper); }}
.mix .T {{ flex: {t}; background: var(--mid); color: var(--paper); }}
.mix .A {{ flex: {a}; background: var(--wash); }}
.mix .F {{ flex: {f}; background: var(--paper); border-left: 1.5px solid var(--ink); }}
.strip {{ display: grid; grid-template-columns: repeat(15, minmax(0, 1fr)); gap: 3px; }}
.cell {{ display: grid; place-items: center; aspect-ratio: 1; max-width: 100%; font: 500 12px var(--mono);
  color: var(--ink); text-decoration: none; border: 1.5px solid var(--ink); position: relative; }}
.cell.t-she {{ background: var(--ink); color: var(--paper); }}
.cell.t-potato {{ background: var(--mid); color: var(--paper); border-color: var(--mid); }}
.cell.t-louise {{ background: var(--paper); }}
.cell.on::after {{ content: ""; position: absolute; left: 3px; right: 3px; bottom: -6px; height: 2px; background: var(--ink); }}
.cell.today {{ outline: 2px solid var(--ink); outline-offset: 2px; }}
.legend {{ display: flex; flex-wrap: wrap; gap: 6px 16px; margin-top: 12px; color: var(--muted); }}
.legend i {{ display: inline-block; width: 12px; height: 12px; border: 1.5px solid var(--ink); vertical-align: -2px; margin-right: 6px; }}
.legend .she {{ background: var(--ink); }} .legend .potato {{ background: var(--mid); border-color: var(--mid); }}
.legend .ai {{ background: var(--wash); }}
.legend .bar {{ border: 0; height: 2px; background: var(--ink); vertical-align: 3px; }}
.rules {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px 28px; margin: 0; padding: 0; list-style: none; }}
.rules li {{ min-width: 0; color: var(--muted); }}
.rules b {{ color: var(--ink); display: block; font: 700 14px var(--display); }}
.tools {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; position: sticky; top: env(safe-area-inset-top, 0px);
  background: var(--paper); padding-block: 12px; z-index: 5; border-bottom: 1px solid var(--rule); }}
body::before {{ content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--paper); }}
button {{ font: 600 13px var(--display); color: var(--ink); background: var(--paper); border: 1.5px solid var(--ink);
  padding: 7px 12px; cursor: pointer; border-radius: 0; }}
button[aria-pressed="true"] {{ background: var(--ink); color: var(--paper); }}
button:focus-visible, summary:focus-visible, .cell:focus-visible {{ outline: 2px solid var(--ink); outline-offset: 2px; }}
.tools .spacer {{ flex: 1; }}
.status {{ color: var(--muted); min-height: 1em; }}
.week {{ margin-top: 34px; }}
.week-head {{ display: flex; flex-wrap: wrap; align-items: baseline; gap: 6px 14px; border-bottom: 1px solid var(--ink); padding-bottom: 8px; }}
.week-head h2 {{ font: 800 22px var(--display); margin: 0; letter-spacing: -.01em; }}
.week-head .mono {{ color: var(--muted); }}
.day {{ display: grid; grid-template-columns: 170px minmax(0, 1fr); gap: 20px; padding-block: 22px; border-bottom: 1px solid var(--rule); }}
.day.today .num::after {{ content: "today"; font: 500 11px var(--mono); margin-left: 8px; padding: 2px 6px; background: var(--ink); color: var(--paper); vertical-align: 4px; }}
.day-side {{ display: flex; flex-direction: column; align-items: flex-start; gap: 7px; min-width: 0; }}
.num {{ font: 800 26px/1 var(--display); letter-spacing: -.02em; }}
.chip {{ font: 600 11px/1 var(--display); text-transform: uppercase; letter-spacing: .08em; padding: 5px 7px; border: 1.5px solid var(--ink); }}
.chip-F {{ background: var(--ink); color: var(--paper); }}
.chip-A {{ border-style: dashed; }}
.chip-new {{ border-color: var(--mid); color: var(--muted); }}
.chip-src, .chip-status {{ border: 0; padding-left: 0; color: var(--muted); }}
.meta {{ display: grid; gap: 3px; color: var(--muted); }}
.meta .track {{ font: 600 13px var(--display); color: var(--ink); }}
.meta .track::before {{ content: ""; display: inline-block; width: 9px; height: 9px; border: 1.5px solid var(--ink); margin-right: 6px; }}
.meta .t-she::before {{ background: var(--ink); }} .meta .t-potato::before {{ background: var(--mid); border-color: var(--mid); }}
.day-main {{ display: grid; gap: 12px; min-width: 0; }}
.card {{ margin: 0; background: var(--card); border: 1px solid var(--rule); padding: 18px 20px 14px; max-width: 560px; }}
.card-head {{ display: flex; align-items: center; gap: 10px; }}
.card-head .av {{ width: 40px; height: 40px; border-radius: 50%; flex: none; background: url({av}) center / cover; }}
.card-head div {{ display: grid; line-height: 1.2; }}
.card-head b {{ font: 700 15px var(--display); }}
.card-head span {{ color: var(--muted); font-size: 14px; }}
blockquote {{ margin: 16px 0 12px; font: 700 clamp(19px, 3.6vw, 23px)/1.3 var(--display); letter-spacing: -.01em; }}
figcaption {{ color: var(--muted); }}
.flag {{ margin: 0; max-width: 62ch; padding-left: 12px; border-left: 2px solid var(--ink); }}
details {{ max-width: 680px; }}
summary {{ cursor: pointer; font: 600 14px var(--display); padding: 4px 0; }}
.copies {{ display: grid; gap: 12px; margin-top: 10px; }}
.copy {{ border: 1px solid var(--rule); background: var(--wash); min-width: 0; }}
.copy-head {{ display: flex; justify-content: space-between; align-items: center; padding: 6px 6px 6px 12px; border-bottom: 1px solid var(--rule);
  font: 700 11px var(--display); text-transform: uppercase; letter-spacing: .1em; color: var(--muted); }}
.copy-head button {{ padding: 4px 10px; font-size: 12px; }}
pre {{ margin: 0; padding: 12px; font: 13px/1.5 var(--mono); white-space: pre-wrap; overflow-wrap: anywhere; }}
.variants span {{ font: 700 11px var(--display); text-transform: uppercase; letter-spacing: .1em; color: var(--muted); }}
.variants ul {{ margin: 6px 0 0; padding-left: 18px; }}
.done {{ color: var(--muted); margin: 0; }}
#all-md {{ position: absolute; left: -9999px; }}
@media (max-width: 640px) {{
  .day {{ grid-template-columns: minmax(0, 1fr); gap: 12px; }}
  .day-side {{ flex-direction: row; flex-wrap: wrap; align-items: center; }}
  .meta {{ width: 100%; grid-auto-flow: column; justify-content: start; gap: 12px; }}
  .strip {{ grid-template-columns: repeat(10, minmax(0, 1fr)); }}
}}
@media (prefers-reduced-motion: reduce) {{ * {{ scroll-behavior: auto !important; }} }}
html {{ scroll-behavior: smooth; }}
</style>

<div class="wrap">
  <header class="top">
    <div>
      <div class="label">ADHD Entrepreneur · content calendar</div>
      <h1>30 days, one line a day</h1>
      <p class="lede">Day 1 was Thu Oct 22. Day 30 is Fri Nov 20, 2026. All 13 bank lines are used, plus {new} new lines for Wil's OK. Zucc builds and posts. Wil approves each post.</p>
    </div>
    <div>
      <div class="label">Content mix</div>
      <div class="mix" role="img" aria-label="Reminders {r}, tips {t}, AI {a}, founder {f}">
        <div class="R">{r}</div><div class="T">{t}</div><div class="A">{a}</div><div class="F">{f}</div>
      </div>
      <div class="legend mono"><span><i class="she"></i>Reminders {r}</span><span><i class="potato"></i>Tips {t}</span><span><i class="ai"></i>AI {a}</span><span><i></i>Founder {f}</span></div>
    </div>
    <div>
      <div class="label">Music rotation · tap a day to jump</div>
      <nav class="strip" aria-label="Days">{strip}</nav>
      <div class="legend mono">
        <span><i class="she"></i>She · from 0:35</span>
        <span><i class="potato"></i>Potato Salad · from 0:10</span>
        <span><i></i>Louise · from 0:53</span>
        <span><i class="bar"></i>links allowed (Nov 5 on)</span>
      </div>
    </div>
    <ul class="rules">
      <li><b>Same sentence everywhere</b>Card video on IG, TikTok and YouTube Shorts. X gets the line as plain text, with no music and no hashtags.</li>
      <li><b>No links before Day 15</b>From Nov 5, the "Quiz in bio" line goes on Day 15 and on the AI days. If the link hub isn't live yet, leave it off.</li>
      <li><b>AI news swap</b>On an AI day, the scout can swap in a fresh AI-news line if it comes from the primary source, is under 7 days old, is one 5–15 word law with no hype, and Wil approves it. The planned line becomes a spare.</li>
      <li><b>Founder posts carry conditions</b>Days 7, 15 and 30 state facts. Each one goes out only if the fact is true that day. Every condition is written on its day.</li>
    </ul>
  </header>

  <div class="tools" role="toolbar" aria-label="Filter days">
    <button type="button" id="f-all" data-filter="all" aria-pressed="true">All</button>
    <button type="button" id="f-new" data-filter="new" aria-pressed="false">New lines</button>
    <button type="button" id="f-R" data-filter="R" aria-pressed="false">Reminders</button>
    <button type="button" id="f-T" data-filter="T" aria-pressed="false">Tips</button>
    <button type="button" id="f-A" data-filter="A" aria-pressed="false">AI</button>
    <button type="button" id="f-F" data-filter="F" aria-pressed="false">Founder</button>
    <span class="spacer"></span>
    <span class="status mono" id="status" aria-live="polite"></span>
    <button type="button" id="copy-all">Copy all for Zucc</button>
  </div>

  {days}

  <textarea id="all-md" readonly aria-hidden="true" tabindex="-1">{md}</textarea>
</div>

<script>
(function () {{
  var status = document.getElementById("status");
  function say(msg) {{ status.textContent = msg; clearTimeout(say.t); say.t = setTimeout(function () {{ status.textContent = ""; }}, 2500); }}
  function copyText(text, fallbackEl) {{
    function fallback() {{
      try {{
        var r = document.createRange(); r.selectNodeContents(fallbackEl);
        var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
        say("Selected. Press copy.");
      }} catch (e) {{ say("Copy blocked here. Select the text by hand."); }}
    }}
    if (navigator.clipboard && navigator.clipboard.writeText) {{
      navigator.clipboard.writeText(text).then(function () {{ say("Copied"); }}, fallback);
    }} else {{ fallback(); }}
  }}
  document.addEventListener("click", function (e) {{
    var b = e.target.closest("[data-copy]");
    if (b) {{ var el = document.getElementById(b.getAttribute("data-copy")); copyText(el.textContent, el); }}
  }});
  document.getElementById("copy-all").addEventListener("click", function () {{
    var ta = document.getElementById("all-md"); copyText(ta.value, ta);
  }});
  var buttons = document.querySelectorAll("[data-filter]");
  buttons.forEach(function (btn) {{
    btn.addEventListener("click", function () {{
      var f = btn.getAttribute("data-filter");
      buttons.forEach(function (x) {{ x.setAttribute("aria-pressed", x === btn ? "true" : "false"); }});
      document.querySelectorAll(".day").forEach(function (d) {{
        var show = f === "all" || (f === "new" ? d.dataset.new === "1" : d.dataset.slot === f);
        d.hidden = !show;
      }});
      document.querySelectorAll(".week").forEach(function (w) {{
        w.hidden = !w.querySelector(".day:not([hidden])");
      }});
    }});
  }});
  var t = new Date(), iso = t.getFullYear() + "-" + String(t.getMonth() + 1).padStart(2, "0") + "-" + String(t.getDate()).padStart(2, "0");
  document.querySelectorAll('[data-date="' + iso + '"]').forEach(function (el) {{ el.classList.add("today"); }});
}})();
</script>
"""

if __name__ == "__main__":
    main()
