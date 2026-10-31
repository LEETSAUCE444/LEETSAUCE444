#!/usr/bin/env python3
"""Rebuild the AE profile picture so the white circle IS the platform crop.

Usage:
    python3 avatar.py SOURCE.jpg OUTDIR [--size 1080] [--pad 0.04]

What it does, from the real file (nothing is redrawn):
  1. Finds the white circle in SOURCE with a least-squares fit on its edge.
  2. Finds the solid black AE letters and centers them on the new canvas.
     The grey echo strokes ride along untouched (they are part of the mark).
  3. Scales so the source circle diameter = canvas width. Letters keep their
     exact size relative to the circle.
  4. Writes:
       ae-avatar-fullbleed-SIZE.png/.jpg     upload this one everywhere
       ae-avatar-safe4-SIZE.png/.jpg         fallback: circle at 92% + black ring
       ae-avatar-circle-on-black-SIZE.png    square contexts only (site, favicon)
       report.txt                            every measurement, for the record

The full-bleed master has NO black anywhere outside the letters. Every
platform crops a circle inscribed in the square, so the visible circle edge is
the platform's own edge: nothing to misalign, no black hairline possible.
"""
import argparse
import os

import numpy as np
from PIL import Image, ImageDraw

BLACK = (0, 0, 0)


def fit_circle(lum):
    """Least-squares circle through the left/right edge of the white disc."""
    h, w = lum.shape
    white = lum > 128
    pts = []
    for y in range(h):
        xs = np.flatnonzero(white[y])
        if len(xs):
            for x in (xs[0], xs[-1]):
                # Points on the frame border are the frame, not the circle.
                if 0 < x < w - 1 and 0 < y < h - 1:
                    pts.append((x, y))
    p = np.asarray(pts, float)
    a = np.c_[2 * p[:, 0], 2 * p[:, 1], np.ones(len(p))]
    sol = np.linalg.lstsq(a, (p ** 2).sum(1), rcond=None)[0]
    cx, cy = sol[:2]
    r = np.sqrt(sol[2] + cx ** 2 + cy ** 2)
    resid = np.abs(np.hypot(p[:, 0] - cx, p[:, 1] - cy) - r)
    return cx, cy, r, float(np.median(resid))


def measure(src):
    rgb = np.asarray(src.convert("RGB")).astype(float)
    lum = rgb @ [0.299, 0.587, 0.114]
    h, w = lum.shape
    cx, cy, r, resid = fit_circle(lum)
    yy, xx = np.mgrid[0:h, 0:w]
    dist = np.hypot(xx - cx, yy - cy)

    ring = (dist > 0.80 * r) & (dist < 0.95 * r)
    fill = tuple(int(round(v)) for v in np.median(rgb[ring], axis=0))
    fill_lum = float(np.median(lum[ring]))

    inside = dist < 0.95 * r
    ink = inside & (lum < fill_lum - 12)      # letters + echo strokes
    solid = inside & (lum < 60)               # the solid black letters only
    iy, ix = np.nonzero(ink)
    sy, sx = np.nonzero(solid)
    weight = (fill_lum - lum)[ink]
    corners = [rgb[2, 2], rgb[2, -3], rgb[-3, 2], rgb[-3, -3]]
    return {
        "size": (w, h),
        "cx": cx, "cy": cy, "r": r, "fit_residual_px": resid,
        "frame_cx": (w - 1) / 2, "frame_cy": (h - 1) / 2,
        "fill": fill,
        "outside": tuple(int(v) for v in np.median(corners, axis=0)),
        "ink_bbox": (ix.min(), iy.min(), ix.max(), iy.max()),
        "solid_bbox": (sx.min(), sy.min(), sx.max(), sy.max()),
        "solid_center": ((sx.min() + sx.max()) / 2, (sy.min() + sy.max()) / 2),
        "ink_centroid": ((ix * weight).sum() / weight.sum(),
                         (iy * weight).sum() / weight.sum()),
        "ink_reach": float(dist[ink].max() / r),
    }


def render(src, m, size, circle_frac):
    """Sample SOURCE so the circle spans circle_frac of a size x size canvas.

    The letters (solid bbox center) land on the canvas center. Everything the
    source has outside 0.85 r is replaced by the flat fill, so the source's own
    edge and black margin can never leak in. Rendered at 2x then reduced with
    Lanczos for clean edges.
    """
    ss = 2 * size
    s = (2 * m["r"]) / (ss * circle_frac)          # source px per output px
    lx, ly = m["solid_center"]
    # PIL affine works in continuous coords; pixel i spans [i, i+1).
    c = lx + 0.5 - s * ss / 2
    f = ly + 0.5 - s * ss / 2
    big = src.convert("RGB").transform((ss, ss), Image.AFFINE,
                                       (s, 0, c, 0, s, f), Image.BICUBIC)
    arr = np.asarray(big).astype(float)

    yy, xx = np.mgrid[0:ss, 0:ss]
    sx_ = c + (xx + 0.5) * s - 0.5                  # source position of each px
    sy_ = f + (yy + 0.5) * s - 0.5
    d = np.hypot(sx_ - m["cx"], sy_ - m["cy"]) / m["r"]
    keep = np.clip((0.88 - d) / 0.03, 0, 1)[..., None]   # soft 0.85-0.88 r
    fill = np.asarray(m["fill"], float)
    arr = arr * keep + fill * (1 - keep)
    out = Image.fromarray(np.clip(arr + 0.5, 0, 255).astype(np.uint8))
    return out.resize((size, size), Image.LANCZOS)


def on_black(art, circle_frac):
    """Put black outside a centered circle (antialiased, no halo)."""
    size = art.size[0]
    ss = 4 * size
    inset = ss * (1 - circle_frac) / 2
    mask = Image.new("L", (ss, ss), 0)
    ImageDraw.Draw(mask).ellipse((inset, inset, ss - inset, ss - inset), fill=255)
    mask = mask.resize((size, size), Image.LANCZOS)
    return Image.composite(art, Image.new("RGB", (size, size), BLACK), mask)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("outdir")
    ap.add_argument("--size", type=int, default=1080)
    ap.add_argument("--pad", type=float, default=0.04,
                    help="safe variant black margin per side, fraction of width")
    args = ap.parse_args()
    os.makedirs(args.outdir, exist_ok=True)

    src = Image.open(args.source)
    m = measure(src)
    n = args.size

    full = render(src, m, n, 1.0)
    frac = 1 - 2 * args.pad
    safe = on_black(render(src, m, n, frac), frac)
    ring = on_black(full, 1.0)

    def save(img, name):
        img.save(os.path.join(args.outdir, name + ".png"), optimize=True)
        img.save(os.path.join(args.outdir, name + ".jpg"), quality=95,
                 subsampling=0)

    save(full, f"ae-avatar-fullbleed-{n}")
    save(safe, f"ae-avatar-safe{round(args.pad * 100)}-{n}")
    ring.save(os.path.join(args.outdir, f"ae-avatar-circle-on-black-{n}.png"),
              optimize=True)

    w, h = m["size"]
    lx, ly = m["solid_center"]
    gx, gy = m["ink_centroid"]
    scale = n / (2 * m["r"])
    lines = [
        f"source: {os.path.basename(args.source)}  {w}x{h}",
        f"white circle: center ({m['cx']:.1f}, {m['cy']:.1f})  radius {m['r']:.1f}"
        f"  diameter {2 * m['r']:.1f} px  (fit residual {m['fit_residual_px']:.2f} px)",
        f"circle offset from frame center: x {m['cx'] - m['frame_cx']:+.1f}"
        f"  y {m['cy'] - m['frame_cy']:+.1f} px",
        f"circle diameter as % of frame width: {200 * m['r'] / w:.1f}%",
        f"circle fill RGB {m['fill']}   outside RGB {m['outside']}",
        f"solid letters center vs circle center: x {lx - m['cx']:+.1f}  y {ly - m['cy']:+.1f} px"
        f"  ({100 * (lx - m['cx']) / (2 * m['r']):+.2f}% / {100 * (ly - m['cy']) / (2 * m['r']):+.2f}% of diameter)",
        f"ink centroid (incl. echo strokes) vs circle center: x {gx - m['cx']:+.1f}  y {gy - m['cy']:+.1f} px",
        f"farthest ink from center: {100 * m['ink_reach']:.1f}% of radius"
        f"  (crop clearance {100 * (1 - m['ink_reach']):.1f}% of radius)",
        f"scale to {n}px canvas: x{scale:.3f}"
        + ("  (UPSCALE - send the original file for a sharper master)" if scale > 1.02 else ""),
        "applied: solid letters centered exactly; circle diameter = canvas width;"
        " outside-circle area = circle fill (full-bleed)",
        f"safe variant: circle {100 * (1 - 2 * args.pad):.0f}% of width, black ring {100 * args.pad:.0f}% per side",
    ]
    with open(os.path.join(args.outdir, "report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
