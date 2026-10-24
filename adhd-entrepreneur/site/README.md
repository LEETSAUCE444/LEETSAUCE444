# ADHD Entrepreneur: brand site (draft)

**Purpose:** unblock Stripe activation. Stripe's setup is paused at the business-website step.

The site is two static pages: `index.html` (home) and `policies.html` (refund and guarantee, terms, privacy). It has no forms, tracking or checkout. The quiz and funnel come later.

**Status (Oct 24, 2026):** draft. There's a private preview for Wil at https://claude.ai/artifact/X3WQmrLBMWafffwTsH55Nr. Nothing is public yet.

## Before it goes public, Wil decides

1. **Button color.** Brand white, or the violet from the reference (`q-accent` on the Questions tab). It's a one-line switch: `--accent` in `style.css`.
2. **The name on the policies.** "ADHD Entrepreneur" with a DBA or LLC, or his legal name for now (`q-legal`).
3. **Draft policy terms.** These are reasonable defaults, not decisions yet:
   - the refund claim window: 14 days after the deadline
   - the 50%-off code: valid for 60 days
   - the fix-or-refund window when something doesn't work: 7 days
4. **Hosting** for the preview URL. Netlify, Cloudflare Pages and GitHub Pages all serve these files as they are.

**Recommended:** have someone qualified read `policies.html` before launch. It's plain-language and not legal advice.

## Rules this site keeps

- **Faceless.** No personal name or photo.
- **No income claims.** The guarantee's goal is always something built.
- **The price and full terms show before payment,** once kits go on sale.
- **No ad-platform pixels.** Visitor data never goes to ad platforms.
- **Brand lock.** Black and white, with the RGB split on "ADHD" (real pixels from `brand/upload/`) as the only color, unless Wil picks violet.

## Files

- `index.html`: the home page
- `policies.html`: refund and guarantee, terms, privacy
- `style.css`: the shared styles
- `assets/wordmark.png`: the split wordmark, cut from `brand/upload/youtube-banner-2560x1440.jpg` with a transparent background
- `assets/favicon.png`, `assets/apple-touch-icon.png`: from `brand/upload/ae-avatar-1080.png`
- `assets/ae-512.png`: a larger copy of the avatar, for the Stripe branding settings if needed
