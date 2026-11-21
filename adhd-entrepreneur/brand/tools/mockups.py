#!/usr/bin/env python3
"""Circular-crop previews of the avatar masters on each platform, light + dark.

Usage:
    python3 mockups.py AVATAR_DIR BANNER_DIR OUTDIR [--before YT_LIVE TIKTOK_LIVE]

Layouts are simplified wireframes at approximate on-screen sizes (pt, drawn
at 2x). The avatar crop itself is exact: a circle inscribed in the square
upload, which is what every platform does. Counts show "-" on purpose: no
made-up numbers.
"""
import argparse
import glob
import os

from PIL import Image, ImageDraw, ImageFont

S = 2                       # px per pt
PW, PH = 390, 400           # phone screen, pt
INTER = "/usr/share/fonts/opentype/inter/Inter-{}.otf"
BIO = ("write that down.", "follow for daily posts")

THEMES = {
    "instagram": {"light": dict(bg="#FFFFFF", fg="#000000", sub="#737373", ui="#EFEFEF", ring="#FFFFFF"),
                  "dark": dict(bg="#000000", fg="#F5F5F5", sub="#A8A8A8", ui="#363636", ring="#000000")},
    "youtube": {"light": dict(bg="#FFFFFF", fg="#0F0F0F", sub="#606060", ui="#F2F2F2", ring="#FFFFFF"),
                "dark": dict(bg="#0F0F0F", fg="#F1F1F1", sub="#AAAAAA", ui="#272727", ring="#0F0F0F")},
    "tiktok": {"light": dict(bg="#FFFFFF", fg="#161823", sub="#75767B", ui="#F1F1F2", ring="#FFFFFF"),
               "dark": dict(bg="#121212", fg="#FFFFFF", sub="#A2A2A2", ui="#2F2F2F", ring="#121212")},
    "x": {"light": dict(bg="#FFFFFF", fg="#0F1419", sub="#536471", ui="#EFF3F4", ring="#FFFFFF"),
          "dark": dict(bg="#000000", fg="#E7E9EA", sub="#71767B", ui="#2F3336", ring="#000000")},
}


def font(weight, pt):
    return ImageFont.truetype(INTER.format(weight), round(pt * S))


def circle(img, d_pt):
    """Exact platform crop: inscribed circle, antialiased via 4x mask."""
    d = round(d_pt * S)
    art = img.convert("RGB").resize((d, d), Image.LANCZOS)
    mask = Image.new("L", (4 * d, 4 * d), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, 4 * d - 1, 4 * d - 1), fill=255)
    return art, mask.resize((d, d), Image.LANCZOS)


class Screen:
    def __init__(self, t):
        self.t = t
        self.im = Image.new("RGB", (PW * S, PH * S), t["bg"])
        self.d = ImageDraw.Draw(self.im)

    def text(self, x, y, s, weight="Regular", pt=14, color="fg", anchor="la"):
        self.d.text((x * S, y * S), s, fill=self.t.get(color, color),
                    font=font(weight, pt), anchor=anchor)

    def bar(self, x, y, w, h, color="ui", r=None):
        r = h / 2 if r is None else r
        self.d.rounded_rectangle((x * S, y * S, (x + w) * S, (y + h) * S),
                                 radius=r * S, fill=self.t.get(color, color))

    def avatar(self, img, x, y, d, ring=0):
        if ring:
            self.d.ellipse(((x - ring) * S, (y - ring) * S, (x + d + ring) * S,
                            (y + d + ring) * S), fill=self.t["ring"])
        art, mask = circle(img, d)
        self.im.paste(art, (round(x * S), round(y * S)), mask)

    def feed_row(self, img, y, d, handle):
        self.d.line((0, (y - 14) * S, PW * S, (y - 14) * S), fill=self.t["ui"], width=S)
        self.avatar(img, 16, y, d)
        self.text(16 + d + 10, y + d / 2 - 9, handle, "SemiBold", 14)
        self.bar(16 + d + 10, y + d / 2 + 9, 180, 7)
        self.text(PW - 16, y + d / 2, f"small size: {d}pt", pt=10, color="sub", anchor="rm")


def instagram(av, ban, t):
    s = Screen(t)
    s.text(16, 14, "adhdentrepreneurhq", "Bold", 20)
    s.avatar(av, 16, 56, 88)
    for i, lab in enumerate(("posts", "followers", "following")):
        cx = 150 + i * 82
        s.text(cx, 80, "-", "SemiBold", 17, anchor="ma")
        s.text(cx, 102, lab, pt=13, anchor="ma")
    s.text(16, 160, BIO[0], pt=14)
    s.text(16, 179, BIO[1], pt=14)
    s.bar(16, 212, 175, 32, r=8)
    s.bar(199, 212, 175, 32, r=8)
    s.text(103, 228, "Follow", "SemiBold", 14, anchor="mm")
    s.text(286, 228, "Message", "SemiBold", 14, anchor="mm")
    s.feed_row(av, 290, 32, "adhdentrepreneurhq")
    return s.im


def youtube(av, ban, t):
    s = Screen(t)
    bw = PW - 32
    bh = bw * 423 / 1546                       # mobile shows the safe area
    strip = ban.crop((507, 508, 2053, 931)).resize((round(bw * S), round(bh * S)), Image.LANCZOS)
    m = Image.new("L", strip.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, strip.size[0] - 1, strip.size[1] - 1), radius=12 * S, fill=255)
    s.im.paste(strip, (16 * S, 12 * S), m)
    y = 12 + bh + 16
    s.avatar(av, 16, y, 72)
    s.text(100, y + 4, "ADHD Entrepreneur", "Bold", 20)
    s.text(100, y + 32, "@adhdentrepreneurhq", pt=13)
    s.text(100, y + 50, "- subscribers  ·  - videos", pt=13, color="sub")
    s.text(16, y + 88, f"{BIO[0]} {BIO[1]}", pt=13, color="sub")
    s.d.rounded_rectangle((16 * S, (y + 116) * S, (PW - 16) * S, (y + 152) * S),
                          radius=18 * S, fill=t["fg"])
    s.text(PW / 2, y + 134, "Subscribe", "SemiBold", 14, color=t["bg"], anchor="mm")
    s.feed_row(av, y + 182, 24, "@adhdentrepreneurhq")
    return s.im


def tiktok(av, ban, t):
    s = Screen(t)
    s.text(PW / 2, 14, "adhdentrepreneur.hq", "Bold", 17, anchor="ma")
    s.avatar(av, PW / 2 - 48, 46, 96)
    s.text(PW / 2, 154, "@adhdentrepreneurhq", "SemiBold", 15, anchor="ma")
    for i, lab in enumerate(("Following", "Followers", "Likes")):
        cx = PW / 2 + (i - 1) * 92
        s.text(cx, 184, "-", "Bold", 17, anchor="ma")
        s.text(cx, 206, lab, pt=13, color="sub", anchor="ma")
    s.bar(PW / 2 - 124, 236, 120, 40, r=4)
    s.bar(PW / 2 + 4, 236, 120, 40, r=4)
    s.text(PW / 2 - 64, 256, "Follow", "SemiBold", 15, anchor="mm")
    s.text(PW / 2 + 64, 256, "Message", "SemiBold", 15, anchor="mm")
    s.text(PW / 2, 290, BIO[0], pt=14, anchor="ma")
    s.text(PW / 2, 309, BIO[1], pt=14, anchor="ma")
    s.feed_row(av, 352, 32, "adhdentrepreneur.hq")
    return s.im


def xprofile(av, header, t):
    s = Screen(t)
    hh = PW / 3
    s.im.paste(header.resize((PW * S, round(hh * S)), Image.LANCZOS), (0, 0))
    s.avatar(av, 16, hh - 40, 80, ring=4)
    s.d.rounded_rectangle(((PW - 112) * S, (hh + 10) * S, (PW - 16) * S, (hh + 44) * S),
                          radius=17 * S, outline=t["ui"], width=S)
    s.text(PW - 64, hh + 27, "Follow", "Bold", 14, anchor="mm")
    s.text(16, hh + 58, "@adhdentreprenhq", "Bold", 20)
    s.text(16, hh + 92, BIO[0], pt=15)
    s.text(16, hh + 112, BIO[1], pt=15)
    s.text(16, hh + 144, "- Following    - Followers", pt=14, color="sub")
    s.feed_row(av, hh + 196, 40, "@adhdentreprenhq")
    return s.im


PLATFORMS = [("instagram", "Instagram", instagram), ("youtube", "YouTube", youtube),
             ("tiktok", "TikTok", tiktok), ("x", "X", xprofile)]


def sheet(title, rows, out):
    """rows: [(row label, {theme: image})]"""
    g, head, lab = 40, 90, 50
    w = 2 * PW * S + 3 * g
    h = head + len(rows) * (lab + PH * S + g)
    im = Image.new("RGB", (w, h), "#1A1A1A")
    d = ImageDraw.Draw(im)
    d.text((g, 26), title, fill="#FFFFFF", font=ImageFont.truetype(INTER.format("Bold"), 40))
    y = head
    for label, cells in rows:
        d.text((g, y + 8), label, fill="#DDDDDD", font=ImageFont.truetype(INTER.format("SemiBold"), 28))
        y += lab
        for i, theme in enumerate(("light", "dark")):
            x = g + i * (PW * S + g)
            im.paste(cells[theme], (x, y))
            d.rectangle((x - 1, y - 1, x + PW * S, y + PH * S), outline="#555555", width=2)
            d.text((x + PW * S - 12, y - 34), f"{theme} mode", fill="#999999",
                   font=ImageFont.truetype(INTER.format("Regular"), 22), anchor="ra")
        y += PH * S + g
    im.save(out, optimize=True)


def edge_darkness(img, n=1080):
    """Darkest pixel on the outer 1.5% of the platform crop (0 = black, 255 = white)."""
    import numpy as np
    a = np.asarray(img.convert("L").resize((n, n), Image.LANCZOS)).astype(float)
    yy, xx = np.mgrid[0:n, 0:n]
    r = np.hypot(xx + 0.5 - n / 2, yy + 0.5 - n / 2) / (n / 2)
    return int(a[(r > 0.985) & (r < 0.995)].min())


def edge_check(cands, out, d=420, zoom=6):
    """Each candidate cropped like a platform does, on white; all 4 edges magnified."""
    g, lab = 30, 96
    zw, zh = 70, 14                      # px window at each edge
    col = max(d, zw * zoom)
    w = len(cands) * (col + g) + g
    h = lab + d + 4 * (zh * zoom + 40) + 2 * g + 10
    im = Image.new("RGB", (w, h), "#FFFFFF")
    dr = ImageDraw.Draw(im)
    f = ImageFont.truetype(INTER.format("SemiBold"), 22)
    fs = ImageFont.truetype(INTER.format("Regular"), 18)
    for i, (label, img, note) in enumerate(cands):
        x = g + i * (col + g)
        dark = edge_darkness(img)
        dr.text((x, g), label, fill="#000000", font=f)
        dr.text((x, g + 30), f"darkest edge pixel: {dark}/255 {note}",
                fill="#B00020" if dark < 128 and not note else "#555555", font=fs)
        art, mask = circle(img, d / S)
        disc = Image.new("RGB", (d, d), "#FFFFFF")
        disc.paste(art, (0, 0), mask)
        im.paste(disc, (x + (col - d) // 2, g + lab - 20))
        y = g + lab - 10 + d
        a0, a1 = (d - zw) // 2, (d + zw) // 2
        for name, box, rot in (("top", (a0, 0, a1, zh), 0), ("bottom", (a0, d - zh, a1, d), 0),
                               ("left", (0, a0, zh, a1), 270), ("right", (d - zh, a0, d, a1), 90)):
            dr.text((x, y + 6), f"{name} edge, {zoom}x" + (" (rotated)" if rot else ""),
                    fill="#555555", font=fs)
            z = disc.crop(box).rotate(rot, expand=True).resize((zw * zoom, zh * zoom), Image.NEAREST)
            im.paste(z, (x, y + 30))
            dr.rectangle((x - 1, y + 29, x + zw * zoom, y + 30 + zh * zoom), outline="#BBBBBB")
            y += zh * zoom + 40
    im.save(out, optimize=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("avatar_dir")
    ap.add_argument("banner_dir")
    ap.add_argument("outdir")
    ap.add_argument("--before", nargs=2, metavar=("YT_LIVE", "TIKTOK_LIVE"))
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    full = Image.open(glob.glob(os.path.join(a.avatar_dir, "ae-avatar-fullbleed-*.png"))[0])
    safe = Image.open(glob.glob(os.path.join(a.avatar_dir, "ae-avatar-safe*-*.png"))[0])
    ban = Image.open(os.path.join(a.banner_dir, "youtube-banner-clean-2560x1440.png")).convert("RGB")
    xh = Image.open(os.path.join(a.banner_dir, "x-header-1500x500.png")).convert("RGB")
    for key, name, fn in PLATFORMS:
        bg = xh if key == "x" else ban
        rows = [(f"A. Full-bleed (recommended)", {th: fn(full, bg, THEMES[key][th]) for th in THEMES[key]}),
                (f"B. Safe 4% ring", {th: fn(safe, bg, THEMES[key][th]) for th in THEMES[key]})]
        sheet(f"{name} - avatar preview", rows, os.path.join(a.outdir, f"preview-{key}.png"))
    cands = []
    if a.before:
        cands += [("YouTube now (live file)", Image.open(a.before[0]), ""),
                  ("TikTok now (live file)", Image.open(a.before[1]), "")]
    cands += [("A. Full-bleed", full, ""), ("B. Safe 4%", safe, "(ring is on purpose)")]
    edge_check(cands, os.path.join(a.outdir, "edge-check-before-after.png"))


if __name__ == "__main__":
    main()
