# ADHD Entrepreneur: brand assets

Profile picture fix (Job #1), banner audit and X header (Job #2). Everything here is built from the real files. Nothing is redrawn.

## Status (Oct 23, 2026)

| Item | State |
|---|---|
| Avatar masters | **Wil picked A (full-bleed), Oct 23.** Still a draft built from the copy YouTube serves (980 px). Final masters get rebuilt from `logo-final-perfect.jpg` once Wil uploads it, with one command (below). |
| Avatar previews (IG / YT / TikTok / X, light + dark) | Ready for approval, in `previews/` |
| YouTube banner audit | Done. Passes on every device. One stray hairline, TV only. |
| Clean YouTube banner | Ready for approval, in `banner/` |
| X header 1500×500 | Ready for approval, in `banner/` |

## What was wrong with the profile picture

The circle was being lined up by hand inside each app's crop tool, so each platform ended up a few pixels off. Measured on the live files:

- **YouTube:** the circle is 2–3 px narrower than the frame and sits 1.8 px high, so a thin dark arc shows on the left and right edges. Darkest edge pixel: 132/255.
- **TikTok:** the circle is 1% oversized and 6 px low. Close, but the top edge is only just tangent. Darkest edge pixel: 223/255.
- **Instagram and X:** the live files couldn't be pulled without logging in, so they were not measured.

**The fix:** the new master has no black outside the letters at all. The whole square is the circle's own fill color, `#EFEFEF`, the same off-white as the original. Every platform crops a circle inscribed in the square upload, so the platform's own crop line is the edge, and a black sliver cannot happen. The new file's darkest edge pixel is 239/255, which is just the fill color.

The AE letters and echo strokes are the original pixels, scaled with the circle. The solid letters are centered exactly. They were already within 0.3% of center. The farthest ink reaches 73% of the radius, so nothing gets clipped.

## Files

```
avatar/draft/  ae-avatar-fullbleed-1080.png/.jpg   A. upload this everywhere
               ae-avatar-safe4-1080.png/.jpg       B. fallback: circle at 92%, thin black ring
               ae-avatar-circle-on-black-1080.png  square places only (website, favicon). NOT for profiles
               report.txt                          every measurement
banner/        youtube-banner-audit.png            safe zones drawn on the live banner
               youtube-banner-device-views.png     what mobile / tablet / desktop / TV show
               youtube-banner-clean-2560x1440.*    same letters, centered, hairline removed
               x-header-1500x500.*                 X header, clear of the avatar overlap
               x-header-audit.png                  avatar zones + mobile trim band
               banner-report.txt                   every measurement
previews/      preview-{instagram,youtube,tiktok,x}.png   A vs B, light + dark mode
               edge-check-before-after.png         live crops vs new, all 4 edges magnified
source/        the live files pulled from YouTube and TikTok (for the record)
tools/         avatar.py, banner.py, mockups.py
```

## Rebuild from the original logo (one command)

```bash
cd adhd-entrepreneur/brand
cp /path/to/logo-final-perfect.jpg source/
python3 tools/avatar.py source/logo-final-perfect.jpg avatar/final
python3 tools/mockups.py avatar/final banner previews \
  --before source/youtube-avatar-live-980.jpg source/tiktok-avatar-live-968.jpg
```

Requires Python 3 with Pillow and NumPy. The mockups use the Inter font.

## Upload steps for Zucc (only after Wil approves A or B)

1. Use the same file on all four platforms: `ae-avatar-fullbleed-1080.jpg`, or the `safe4` file if Wil picks B.
2. When the app shows its crop/zoom box, **leave it at full size. Don't zoom and don't drag.** The file is already exact, so any zoom cuts into it.
3. Go one platform per run, signed-in account verified first, as usual. TikTok: confirm it is **@adhdentrepreneurhq** and not the trap account.
4. The X banner goes in X's header slot, `x-header-1500x500.jpg`. X is phone-only for Wil right now, so send him the file.
5. YouTube banner (optional): `youtube-banner-clean-2560x1440.jpg`. It only matters on TV, where it removes the hairline, and it centers the wordmark 26 px lower.

## YouTube banner audit, from the live 2560×1440 file

Zones follow YouTube's published spec: a 2560×1440 upload, with a 1546×423 safe area for text and logos (1235×338 at the 2048×1152 minimum). Desktop shows 2560×423, tablet 1855×423 and TV the full image. The file limit is 6 MB.

- The wordmark is 1170×78 px, inside the safe area on every device. Margins in the mobile view are 187 / 148 / 190 / 198 px (L/T/R/B). **Pass.**
- The wordmark sits **26 px above** the center of the strip. That's minor, and fixed in the clean version.
- **Stray hairline:** a faint grey line at y≈1000–1005, x 560–1999 (peak 37/255). It is outside every crop except TV, probably left over from generation. Removed in the clean version.
- The background is pure black, `#000`.

## X header, 1500×500

- Same wordmark pixels, scaled ×0.73, centered at x 317–1171, y 222–279.
- Clears the avatar overlap zone (bottom-left, about x 30–410, y 333+) by 54 px vertically.
- Sits inside the y 60–440 band that survives the top and bottom trim on mobile.
- No official X safe-area spec was found. The overlap and trim zones come from measured layouts and third-party guides, so check the mockup on Wil's phone after upload.
