#!/usr/bin/env python3
"""Exploration: RGB color split (chromatic aberration) on part of the wordmark.

Usage:
    python3 colorsplit.py AVATAR_DIR BANNER_DIR OUTDIR

Splits only the first glyph group: the "A" in the avatar, "ADHD" in the banner
and the X header. Red trails left (with the echo strokes), blue leads right,
green stays put, so the split reads as motion in the same direction the echo
strokes already imply. Writes variant files plus two comparison sheets.
"""
import glob
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
from mockups import INTER, circle  # noqa: E402

LEVELS = [("now", 0), ("subtle", 1), ("bold", 2)]


def shift(ch, dx, fill):
    out = np.full_like(ch, fill)
    if dx > 0:
        out[:, dx:] = ch[:, :-dx]
    elif dx < 0:
        out[:, :dx] = ch[:, -dx:]
    else:
        out[:] = ch
    return out


def split_first_group(img, d, solid_only=False):
    """Color-split everything left of the widest gap in the ink.

    solid_only: split just the solid letters; the grey echo strokes stay grey
    (they carry the hidden "AI" read in the avatar).
    """
    if d == 0:
        return img.convert("RGB")
    arr = np.asarray(img.convert("RGB")).astype(float)
    lum = arr @ [0.299, 0.587, 0.114]
    border = np.concatenate([arr[0], arr[-1], arr[:, 0], arr[:, -1]])
    bg = np.median(border, axis=0)
    dark_on_light = bg.mean() > 128
    ink = np.abs(lum - bg.mean()) > 6
    cols = ink.sum(0)
    xs = np.flatnonzero(cols)
    best, run = (0, 0), None
    for x in range(xs.min(), xs.max()):
        if cols[x] == 0:
            run = (run[0], x) if run else (x, x)
            if run[1] - run[0] > best[1] - best[0]:
                best = run
        else:
            run = None
    cut = (best[0] + best[1]) // 2
    left = arr.copy()
    left[:, cut:] = bg
    rest = arr.copy()
    rest[:, :cut] = bg
    if solid_only:
        # Soft mask: full-contrast pixels are the letter, everything lighter is echo.
        a = np.clip((np.abs(lum - bg.mean()) - 150) / 60, 0, 1)[..., None]
        a[:, cut:] = 0
        echo = left * (1 - a) + bg * a
        left = left * a + bg * (1 - a)
        rest = np.minimum(rest, echo) if dark_on_light else np.maximum(rest, echo)
    moved = np.stack([shift(left[..., 0], -d, bg[0]),     # red trails
                      left[..., 1],                        # green stays
                      shift(left[..., 2], d, bg[2])], -1)  # blue leads
    out = np.minimum(moved, rest) if dark_on_light else np.maximum(moved, rest)
    return Image.fromarray(np.clip(out + 0.5, 0, 255).astype(np.uint8))


def label(d, xy, s, size=24, color="#DDDDDD", weight="SemiBold", anchor="la"):
    d.text(xy, s, fill=color, font=ImageFont.truetype(INTER.format(weight), size), anchor=anchor)


def disc_on(img, d_pt, bg, pad=14):
    art, mask = circle(img, d_pt)
    tile = Image.new("RGB", (art.size[0] + 2 * pad, art.size[1] + 2 * pad), bg)
    tile.paste(art, (pad, pad), mask)
    return tile


def avatar_sheet(variants, out, title="Color split on the A - same file, three strengths"):
    cols = [(110, "#000000", "profile, dark"), (88, "#FFFFFF", "profile, light"),
            (32, "#000000", "feed, dark"), (32, "#FFFFFF", "feed, light"),
            (24, "#FFFFFF", "comment, light")]
    g, rowh, head = 30, 2 * 110 + 28 + 60, 110
    w = 260 + sum(2 * c[0] + 28 + g for c in cols) + g
    im = Image.new("RGB", (w, head + len(variants) * rowh + g), "#1A1A1A")
    d = ImageDraw.Draw(im)
    label(d, (g, 22), title, 34, "#FFFFFF", "Bold")
    y = head
    for name, img in variants:
        label(d, (g, y + rowh // 2 - 30), name, 24)
        x = 260
        for pt, bg, cap in cols:
            t = disc_on(img, pt, bg)
            im.paste(t, (x, y + (2 * 110 + 28 - t.size[1]) // 2))
            if name == variants[0][0]:
                label(d, (x, y - 26), cap, 18, "#999999", "Regular")
            x += 2 * pt + 28 + g
        y += rowh
    im.save(out, optimize=True)


def banner_sheet(variants, out):
    pw, g, head = 780, 30, 80
    rows = []
    for name, ban, xh in variants:
        mob = ban.crop((507, 508, 2053, 931)).resize((pw, round(pw * 423 / 1546)), Image.LANCZOS)
        xs = xh.resize((pw, pw // 3), Image.LANCZOS)
        rows.append((name, xs, mob))
    rowh = 44 + max(max(r[1].size[1], r[2].size[1]) for r in rows) + g
    im = Image.new("RGB", (2 * pw + 3 * g, head + len(rows) * rowh), "#1A1A1A")
    d = ImageDraw.Draw(im)
    label(d, (g, 22), "Color split on ADHD - X header and YouTube (phone width)", 34, "#FFFFFF", "Bold")
    y = head
    for name, xs, mob in rows:
        label(d, (g, y), f"{name}:  X header", 24)
        label(d, (2 * g + pw, y), "YouTube mobile banner", 24)
        im.paste(xs, (g, y + 40))
        im.paste(mob, (2 * g + pw, y + 40))
        y += rowh
    im.save(out, optimize=True)


def main():
    avatar_dir, banner_dir, out = sys.argv[1:4]
    os.makedirs(out, exist_ok=True)
    av = Image.open(glob.glob(os.path.join(avatar_dir, "ae-avatar-fullbleed-*.png"))[0])
    ban = Image.open(os.path.join(banner_dir, "youtube-banner-clean-2560x1440.png"))
    xh = Image.open(os.path.join(banner_dir, "x-header-1500x500.png"))
    # shift in px per level, sized to each asset's letter height
    px = {"avatar": (0, 7, 14), "banner": (0, 3, 6), "x": (0, 2, 4)}
    av_vars, ban_vars = [], []
    for name, i in LEVELS:
        a = split_first_group(av, px["avatar"][i])
        b = split_first_group(ban, px["banner"][i])
        x = split_first_group(xh, px["x"][i])
        if i:
            a.save(os.path.join(out, f"avatar-split-{name}.png"), optimize=True)
            b.save(os.path.join(out, f"youtube-banner-split-{name}.png"), optimize=True)
            x.save(os.path.join(out, f"x-header-split-{name}.png"), optimize=True)
        av_vars.append((name, a))
        ban_vars.append((name, b, x))
    avatar_sheet(av_vars, os.path.join(out, "compare-avatar.png"))
    # close-up of the A: now vs subtle, same crop
    n = av.size[0]
    box = tuple(round(v * n / 1080) for v in (180, 280, 620, 800))
    pair = [dict(av_vars)[k].crop(box) for k in ("now", "subtle")]
    cu = Image.new("RGB", (2 * pair[0].size[0] + 20, pair[0].size[1]), "#FFFFFF")
    cu.paste(pair[0], (0, 0))
    cu.paste(pair[1], (pair[0].size[0] + 20, 0))
    cu.save(os.path.join(out, "avatar-A-closeup-now-vs-subtle.png"), optimize=True)
    banner_sheet(ban_vars, os.path.join(out, "compare-banner.png"))

    # bold, letters only: the grey echo strokes stay grey
    a = split_first_group(av, px["avatar"][2], solid_only=True)
    a.save(os.path.join(out, "avatar-split-bold-letters-only.png"), optimize=True)
    for key, src, name in (("banner", ban, "youtube-banner"), ("x", xh, "x-header")):
        split_first_group(src, px[key][2], solid_only=True).save(
            os.path.join(out, f"{name}-split-bold-letters-only.png"), optimize=True)
    bold = dict(av_vars)["bold"]
    avatar_sheet([("now", dict(av_vars)["now"]), ("bold, whole A", bold), ("bold, letter only", a)],
                 os.path.join(out, "compare-avatar-bold.png"),
                 "Bold split: whole A vs letter only (echo stays grey)")
    pair = [bold.crop(box), a.crop(box)]
    cu = Image.new("RGB", (2 * pair[0].size[0] + 20, pair[0].size[1]), "#FFFFFF")
    cu.paste(pair[0], (0, 0))
    cu.paste(pair[1], (pair[0].size[0] + 20, 0))
    cu.save(os.path.join(out, "avatar-A-closeup-bold-whole-vs-letter-only.png"), optimize=True)


if __name__ == "__main__":
    main()
