#!/usr/bin/env python3
"""YouTube banner safe-area audit + clean rebuild + X header, from the real file.

Usage:
    python3 banner.py BANNER_2560x1440.jpg OUTDIR

Writes:
    youtube-banner-audit.png        zones drawn on the live banner
    youtube-banner-device-views.png what mobile / tablet / desktop / TV show
    youtube-banner-clean-2560x1440.png/.jpg
                                    same text pixels, centered in the safe strip,
                                    stray hairline removed
    x-header-1500x500.png/.jpg      same text pixels, scaled, clear of the avatar
    x-header-audit.png              avatar overlap + mobile crop zones
    banner-report.txt               every measurement

Zones follow YouTube's published spec: 2560x1440 upload; the text/logo safe
area is 1546x423 centered (1235x338 at the 2048x1152 minimum). Desktop shows
the full-width 2560x423 strip, tablet 1855x423, TV the whole image.
"""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
W, H = 2560, 1440
ZONES = [  # name, width, height (centered)
    ("TV (full image)", 2560, 1440),
    ("Desktop", 2560, 423),
    ("Tablet", 1855, 423),
    ("Mobile = safe area", 1546, 423),
]
ZONE_COLORS = [(120, 120, 120), (0, 160, 255), (255, 170, 0), (0, 210, 110)]

# X header: 1500x500. Avatar overlap in the bottom-left, measured from the
# current layouts (desktop web: 133.5px avatar + 4px ring on a 600px-wide
# header, 16px from the left, overlapping the bottom ~50%; iOS/Android: ~80pt
# avatar on a 390pt header, same 16pt inset). Both scaled to 1500 wide.
XW, XH = 1500, 500
X_AVATAR_DESKTOP = (30, 333, 394, 500)
X_AVATAR_MOBILE = (52, 346, 410, 500)
X_MOBILE_CROP = 60   # some apps trim ~50-60px top and bottom: keep text inside
X_TEXT_WIDTH = 0.56  # solid text width as a share of the header width


def font(px):
    return ImageFont.truetype(FONT, px)


def zone_box(zw, zh):
    return ((W - zw) / 2, (H - zh) / 2, (W + zw) / 2, (H + zh) / 2)


def text_block(lum):
    """Bbox of the wordmark (solid letters + echo strokes), ignoring stray lines."""
    rows = np.flatnonzero((lum > 200).sum(1) > 20)       # rows with real letters
    y0, y1 = rows.min(), rows.max()
    band = lum[max(0, y0 - 40):y1 + 40]
    ys, xs = np.nonzero(band > 6)
    ys = ys + max(0, y0 - 40)
    sy, sx = np.nonzero(lum[y0:y1 + 1] > 200)
    return ((xs.min(), ys.min(), xs.max(), ys.max()),
            (sx.min(), sy.min() + y0, sx.max(), sy.max() + y0))


def stray_marks(lum, block, pad=12):
    """Anything brighter than the background outside the wordmark."""
    m = lum > 6
    x0, y0, x1, y1 = block
    m[max(0, y0 - pad):y1 + pad, max(0, x0 - pad):x1 + pad] = False
    ys, xs = np.nonzero(m)
    if not len(xs):
        return None
    return (xs.min(), ys.min(), xs.max(), ys.max(), float(lum[m].max()))


def main():
    src_path, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    img = Image.open(src_path).convert("RGB")
    assert img.size == (W, H), f"expected {W}x{H}, got {img.size}"
    rgb = np.asarray(img).astype(float)
    lum = rgb @ [0.299, 0.587, 0.114]
    block, solid = text_block(lum)
    stray = stray_marks(lum, block)
    bx0, by0, bx1, by1 = block
    sx0, sy0, sx1, sy1 = solid
    safe = zone_box(1546, 423)

    rep = [f"source: {os.path.basename(src_path)}  {W}x{H}",
           f"background: min {lum.min():.0f} / median {np.median(lum):.0f} (0 = pure black)",
           f"wordmark incl. echo strokes: x {bx0}-{bx1}, y {by0}-{by1}"
           f"  ({bx1 - bx0 + 1}x{by1 - by0 + 1} px)",
           f"solid white letters: x {sx0}-{sx1}, y {sy0}-{sy1}"
           f"  (cap height {sy1 - sy0 + 1} px)",
           f"solid letters center: ({(sx0 + sx1) / 2:.1f}, {(sy0 + sy1) / 2:.1f})"
           f"  vs strip center ({(W - 1) / 2:.1f}, {(H - 1) / 2:.1f})"]
    for name, zw, zh in ZONES:
        z = zone_box(zw, zh)
        inside = bx0 >= z[0] and by0 >= z[1] and bx1 <= z[2] and by1 <= z[3]
        margins = (bx0 - z[0], by0 - z[1], z[2] - bx1, z[3] - by1)
        rep.append(f"{name:<20} {zw}x{zh}: wordmark fully inside = {inside};"
                   f" margins L/T/R/B = " + "/".join(f"{v:.0f}" for v in margins))
    if stray:
        x0, y0, x1, y1, peak = stray
        seen = [n for n, zw, zh in ZONES
                if not (x1 < zone_box(zw, zh)[0] or x0 > zone_box(zw, zh)[2]
                        or y1 < zone_box(zw, zh)[1] or y0 > zone_box(zw, zh)[3])]
        rep.append(f"stray mark outside wordmark: x {x0}-{x1}, y {y0}-{y1},"
                   f" peak brightness {peak:.0f}/255; visible on: {', '.join(seen)}")
    else:
        rep.append("stray marks outside wordmark: none")

    # --- audit overlay --------------------------------------------------
    sc = 0.5
    aud = img.resize((int(W * sc), int(H * sc)), Image.LANCZOS)
    d = ImageDraw.Draw(aud)
    for i, ((name, zw, zh), col) in enumerate(zip(ZONES, ZONE_COLORS)):
        z = [v * sc for v in zone_box(zw, zh)]
        d.rectangle(z, outline=col, width=3)
        row = max(0, i - 1)  # the three 423-high strips share a top edge
        d.text((z[0] + 10, z[1] + 8 + 26 * row), f"{name}  {zw}x{zh}", fill=col, font=font(20))
    d.rectangle([v * sc for v in block], outline=(255, 60, 60), width=2)
    d.text((bx0 * sc, by1 * sc + 8), "wordmark", fill=(255, 60, 60), font=font(18))
    if stray:
        x0, y0, x1, y1, _ = stray
        d.rectangle((x0 * sc - 6, y0 * sc - 6, x1 * sc + 6, y1 * sc + 6),
                    outline=(255, 60, 60), width=2)
        d.text((x0 * sc, y1 * sc + 10), "stray hairline (TV view only)",
               fill=(255, 60, 60), font=font(18))
    aud.save(os.path.join(out, "youtube-banner-audit.png"), optimize=True)

    # --- device views (each scaled to the same on-screen width) --------
    pw, gap = 1200, 36
    views = []
    for (name, zw, zh), col in zip(ZONES[::-1], ZONE_COLORS[::-1]):
        crop = img.crop(tuple(int(round(v)) for v in zone_box(zw, zh)))
        views.append((name, zw, zh, crop.resize((pw, round(pw * zh / zw)), Image.LANCZOS)))
    tot = sum(v[3].size[1] + 44 + gap for v in views) + gap
    sheet = Image.new("RGB", (pw + 2 * gap, tot), (24, 24, 24))
    d = ImageDraw.Draw(sheet)
    y = gap
    for name, zw, zh, v in views:
        d.text((gap, y), f"{name}: {zw}x{zh} of the banner, shown at phone/screen width",
               fill=(230, 230, 230), font=font(22))
        y += 44
        sheet.paste(v, (gap, y))
        d.rectangle((gap - 1, y - 1, gap + pw, y + v.size[1]), outline=(90, 90, 90))
        y += v.size[1] + gap
    sheet.save(os.path.join(out, "youtube-banner-device-views.png"), optimize=True)

    # --- clean rebuild: same pixels, centered in the strip, nothing stray ---
    pad = 6
    wm = img.crop((bx0 - pad, by0 - pad, bx1 + pad + 1, by1 + pad + 1))
    dy = int(round((H - 1) / 2 - (sy0 + sy1) / 2))
    clean = Image.new("RGB", (W, H), (0, 0, 0))
    clean.paste(wm, (bx0 - pad, by0 - pad + dy))
    clean.save(os.path.join(out, "youtube-banner-clean-2560x1440.png"), optimize=True)
    clean.save(os.path.join(out, "youtube-banner-clean-2560x1440.jpg"), quality=95, subsampling=0)
    rep.append(f"clean rebuild: wordmark moved {dy:+d} px vertically (now centered in the"
               f" safe strip), everything else pure black")

    # --- X header --------------------------------------------------------
    k = XW * X_TEXT_WIDTH / (sx1 - sx0 + 1)
    wmx = wm.resize((round(wm.size[0] * k), round(wm.size[1] * k)), Image.LANCZOS)
    scx = ((sx0 + sx1) / 2 - (bx0 - pad)) * k     # solid center inside wmx
    scy = ((sy0 + sy1) / 2 - (by0 - pad)) * k
    px, py = round((XW - 1) / 2 - scx), round((XH - 1) / 2 - scy)
    xh = Image.new("RGB", (XW, XH), (0, 0, 0))
    xh.paste(wmx, (px, py))
    xh.save(os.path.join(out, "x-header-1500x500.png"), optimize=True)
    xh.save(os.path.join(out, "x-header-1500x500.jpg"), quality=95, subsampling=0)
    xl = np.asarray(xh.convert("L")).astype(float)
    ys, xs = np.nonzero(xl > 6)
    tb = (xs.min(), ys.min(), xs.max(), ys.max())
    gap_v = min(X_AVATAR_DESKTOP[1], X_AVATAR_MOBILE[1]) - tb[3]
    rep.append(f"X header: wordmark scaled x{k:.3f}, occupies x {tb[0]}-{tb[2]}, y {tb[1]}-{tb[3]};"
               f" clearance above the avatar zone {gap_v} px; inside the mobile-safe band"
               f" (y {X_MOBILE_CROP}-{XH - X_MOBILE_CROP}) = {tb[1] >= X_MOBILE_CROP and tb[3] <= XH - X_MOBILE_CROP}")

    xa = xh.copy()
    d = ImageDraw.Draw(xa)
    d.rectangle((0, X_MOBILE_CROP, XW - 1, XH - X_MOBILE_CROP), outline=(0, 210, 110), width=3)
    d.text((10, X_MOBILE_CROP + 6), "keep text inside this band (mobile trim)", fill=(0, 210, 110), font=font(20))
    for box, col, lab in ((X_AVATAR_DESKTOP, (255, 170, 0), "avatar - desktop"),
                          (X_AVATAR_MOBILE, (0, 160, 255), "avatar - mobile")):
        d.rectangle(box, outline=col, width=3)
        ty = box[1] + 10 if col[0] == 0 else box[1] - 26   # mobile inside, desktop above
        d.text((box[0] + 8, ty), lab, fill=col, font=font(18))
    d.rectangle(tb, outline=(255, 60, 60), width=2)
    xa.save(os.path.join(out, "x-header-audit.png"), optimize=True)

    with open(os.path.join(out, "banner-report.txt"), "w") as fh:
        fh.write("\n".join(rep) + "\n")
    print("\n".join(rep))


if __name__ == "__main__":
    main()
