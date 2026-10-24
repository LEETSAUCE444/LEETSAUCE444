#!/usr/bin/env python3
"""Build the approved upload set in one go.

Usage:
    python3 final.py LOGO_SOURCE.jpg BANNER_DIR OUTDIR [--size 1080]

Approved Oct 23, 2026:
  - avatar: full-bleed (A) + bold color split on the whole A (echo strokes included)
  - YouTube banner + X header: bold color split on the whole word "ADHD"

Writes to OUTDIR:
    ae-avatar-SIZE.png/.jpg            profile picture, all four platforms
    youtube-banner-2560x1440.jpg       YouTube banner
    x-header-1500x500.jpg              X header
    preview-all-platforms.png          the set on IG / YouTube / TikTok / X, light + dark
    report.txt                         avatar measurements from avatar.py
BANNER_DIR is banner.py's output (clean banner + X header).
"""
import argparse
import os
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from avatar import measure, render  # noqa: E402
from colorsplit import split_first_group  # noqa: E402
from mockups import PLATFORMS, THEMES, sheet  # noqa: E402

SPLIT_AVATAR = 14 / 1080   # bold, as a share of avatar width
SPLIT_BANNER = 6           # px at 2560 wide
SPLIT_XHEADER = 4          # px at 1500 wide


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("banner_dir")
    ap.add_argument("outdir")
    ap.add_argument("--size", type=int, default=1080)
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    n = a.size

    src = Image.open(a.source)
    m = measure(src)
    av = split_first_group(render(src, m, n, 1.0), round(SPLIT_AVATAR * n))
    av.save(os.path.join(a.outdir, f"ae-avatar-{n}.png"), optimize=True)
    av.save(os.path.join(a.outdir, f"ae-avatar-{n}.jpg"), quality=95, subsampling=0)

    ban = split_first_group(Image.open(os.path.join(a.banner_dir, "youtube-banner-clean-2560x1440.png")),
                            SPLIT_BANNER)
    xh = split_first_group(Image.open(os.path.join(a.banner_dir, "x-header-1500x500.png")), SPLIT_XHEADER)
    ban.save(os.path.join(a.outdir, "youtube-banner-2560x1440.jpg"), quality=95, subsampling=0)
    xh.save(os.path.join(a.outdir, "x-header-1500x500.jpg"), quality=95, subsampling=0)

    rows = [(name, {th: fn(av, xh if key == "x" else ban, THEMES[key][th]) for th in ("light", "dark")})
            for key, name, fn in PLATFORMS]
    sheet("Final set - full-bleed avatar, bold split", rows,
          os.path.join(a.outdir, "preview-all-platforms.png"))

    scale = n / (2 * m["r"])
    with open(os.path.join(a.outdir, "report.txt"), "w") as fh:
        fh.write(f"source: {os.path.basename(a.source)} {m['size'][0]}x{m['size'][1]}\n"
                 f"circle diameter in source: {2 * m['r']:.1f} px -> scale x{scale:.3f} to {n}px"
                 f"{' (upscaled)' if scale > 1.02 else ''}, rendered directly from the source file"
                 f" (no intermediate copies)\n"
                 f"avatar split: {round(SPLIT_AVATAR * n)} px per channel on the whole A\n"
                 f"banner split: {SPLIT_BANNER} px (2560 wide), X header split: {SPLIT_XHEADER} px (1500 wide)\n")
    print(open(os.path.join(a.outdir, "report.txt")).read(), end="")


if __name__ == "__main__":
    main()
