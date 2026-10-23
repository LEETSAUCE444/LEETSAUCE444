#!/usr/bin/env python3
"""Build the 30-day calendar outputs from calendar-30.json.

Usage:
    python3 build_calendar.py

Writes, next to this script:
    calendar-30.md    full per-platform copy, one block per day (for Zucc)
    calendar-30.csv   one row per day (for sheets / automation)
and prints a lint report: mix counts, word counts, title/post lengths, and any
phrase the house style or the guardrails rule out.
"""
import csv
import datetime as dt
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
YT_TITLE_MAX = 100
X_MAX = 280
# House style + guardrails (no hedging, no tips-voice, no income or medical claims)
BANNED = [r"\byou should\b", r"\bmaybe\b", r"\bsometimes\b", r"\btry to\b", r"\$",
          r"\bincome\b", r"\brevenue\b", r"\bprofit", r"\bmoney\b", r"\bguarantee",
          r"\bcure", r"\btreat", r"\bdiagnos", r"\bmedicat", r"\bsymptom", r"\bdisorder\b"]


def load():
    with open(os.path.join(HERE, "calendar-30.json")) as fh:
        return json.load(fh)


def flat(line):
    return " ".join(part.strip() for part in line.split("\n"))


def words(line):
    return len(flat(line).split())


def yt_title(line):
    """The quote as the title; if it runs long, keep whole sentences that fit."""
    t = flat(line)
    if len(t) <= YT_TITLE_MAX:
        return t
    out = ""
    for s in re.split(r"(?<=[.!?\"])\s+", t):
        if len((out + " " + s).strip()) > YT_TITLE_MAX:
            break
        out = (out + " " + s).strip()
    return out


def expand(cal):
    start = dt.date.fromisoformat(cal["start"])
    live = dt.date.fromisoformat(cal["links_live"])
    rows = []
    for d in cal["days"]:
        n = d["day"]
        date = start + dt.timedelta(days=n - 1)
        m = cal["music"][((n - 1) // 3) % 3]
        cta = d.get("cta") and date >= live
        r = dict(d)
        r.update(date=date.isoformat(), weekday=date.strftime("%a"),
                 date_label=date.strftime("%a %b %-d"),
                 slot_name=cal["slots"][d["slot"]],
                 music=f'{m["track"]} from {m["start"]}',
                 links="yes" if date >= live else "no",
                 words=words(d["line"]))
        if d["source"] == "live":
            r.update(ig="(already written)", tiktok="(already written)",
                     yt_title=yt_title(d["line"]), yt_desc="", x=d["line"])
            rows.append(r)
            continue
        ig = [d["line"], "", f'Day {n}. {cal["tagline"]}', d["question"]]
        if cta:
            ig.append(cal["cta_long"])
        ig += ["", cal["hashtags"]]
        tt = f'{flat(d["line"])} Day {n}. {d["question"]}'
        if cta:
            tt += f' {cal["cta_short"]}'
        r.update(ig="\n".join(ig), tiktok=f'{tt} {cal["hashtags"]}',
                 yt_title=yt_title(d["line"]), yt_desc=f'Day {n}. {cal["tagline"]}',
                 x=d["line"])
        rows.append(r)
    return rows


def lint(cal, rows):
    rep = []
    counts = {}
    for r in rows:
        counts[r["slot"]] = counts.get(r["slot"], 0) + 1
    total = len(rows)
    rep.append("mix: " + ", ".join(
        f'{cal["slots"][k]} {counts.get(k, 0)}/{total} ({100 * counts.get(k, 0) / total:.0f}%)'
        for k in "RTAF"))
    seen = {}
    for r in rows:
        key = flat(r["line"]).lower()
        if key in seen:
            rep.append(f'DUPLICATE line: day {r["day"]} = day {seen[key]}')
        seen[key] = r["day"]
        texts = [r["line"], r.get("question", "")] + r.get("variants", [])
        for t in texts:
            for pat in BANNED:
                if re.search(pat, t, re.I):
                    rep.append(f'day {r["day"]}: banned pattern {pat!r} in: {flat(t)}')
        if r["words"] > 15 and r["source"] != "live":
            rep.append(f'day {r["day"]}: {r["words"]} words (house max 15)')
        if len(flat(r["line"])) > YT_TITLE_MAX:
            rep.append(f'day {r["day"]}: YouTube title shortened to {len(r["yt_title"])} chars')
        if len(r["x"]) > X_MAX:
            rep.append(f'day {r["day"]}: X post over {X_MAX} chars')
        if r["links"] == "no" and "bio" in r["ig"].lower():
            rep.append(f'day {r["day"]}: link mention before links go live')
    banks = sorted(int(r["source"].split()[1]) for r in rows if r["source"].startswith("bank"))
    rep.append(f"bank lines used: {len(banks)}/13" + ("" if banks == list(range(1, 14)) else f" MISSING {sorted(set(range(1, 14)) - set(banks))}"))
    return rep


def write_md(cal, rows, path):
    o = ["# ADHD Entrepreneur: 30-day calendar (Day 1 Oct 22 to Day 30 Nov 20, 2026)", "",
         "Built from calendar-30.json by build_calendar.py. Card text line breaks are real line breaks.",
         "X = the line as plain text, no music, no hashtags. Links stay out of everything until Day 15 (Nov 5).", ""]
    for r in rows:
        o.append(f'## Day {r["day"]} · {r["date_label"]} · {r["slot_name"]}')
        o.append("")
        meta = [f'Music: {r["music"]}', f'Links: {r["links"]}']
        if r["source"] != "live":
            meta.insert(0, f'Source: {r["source"]}')
        if r.get("status"):
            meta.insert(0, f'**{r["status"]}**')
        if r.get("pattern"):
            meta.append(f'Pattern: {r["pattern"]}')
        o.append(" · ".join(meta))
        o.append("")
        o.append("**Card / X**")
        o.append("")
        o += [f"> {ln}" for ln in r["line"].split("\n")]
        o.append("")
        if r["source"] != "live":
            o += ["**Instagram caption**", "", "```", r["ig"], "```", "",
                  "**TikTok caption**", "", "```", r["tiktok"], "```", "",
                  f'**YouTube Short** title: `{r["yt_title"]}` · description: `{r["yt_desc"]}`', ""]
        if r.get("variants"):
            o.append("**Hook variants** (reruns after Day 30 or a swap if Wil prefers; never both in one week)")
            o.append("")
            o += [f"- {v}" for v in r["variants"]]
            o.append("")
        if r.get("condition"):
            o += [f'**Condition:** {r["condition"]}', ""]
        if r.get("note"):
            o += [f'**Note:** {r["note"]}', ""]
    with open(path, "w") as fh:
        fh.write("\n".join(o))


def write_csv(rows, path):
    cols = ["day", "date", "weekday", "slot_name", "source", "pattern", "music", "links",
            "line", "words", "question", "ig", "tiktok", "yt_title", "yt_desc", "x",
            "variants", "condition", "note", "status"]
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            r = dict(r, variants=" | ".join(r.get("variants", [])))
            w.writerow(r)


def main():
    cal = load()
    rows = expand(cal)
    write_md(cal, rows, os.path.join(HERE, "calendar-30.md"))
    write_csv(rows, os.path.join(HERE, "calendar-30.csv"))
    with open(os.path.join(HERE, "calendar-30.rows.json"), "w") as fh:
        json.dump(rows, fh, indent=1)
    print("\n".join(lint(cal, rows)))


if __name__ == "__main__":
    main()
