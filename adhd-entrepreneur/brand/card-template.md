# ADHD Entrepreneur — Quote-card template spec (text)

Derived from the actual build scripts in `assets/` (`make_tweetcard.py` is the
current white-card render; `make_card.py` is the earlier dark variant).
The PNG itself can't ride the connector's text-only push path — this spec is
the source of truth, and Wil can send the PNG in chat.

## Current render (white tweet-card look — Days 2–3)
- Canvas: 1080 × 1920 (9:16), white background (255, 255, 255).
- Avatar: 150 × 150 circular crop of the full-bleed split-AE avatar, pasted at (55, 585).
- Name/handle block (right of avatar): "ADHD Entrepreneur" (Liberation Sans Bold, 52) at y ≈ 602; "@adhdentrepreneurhq" (Liberation Sans Regular, 46, grey 83,100,113) below it.
- Quote: Liberation Sans Bold, 104, black (15, 20, 25), wrapped at width 19 characters, line height 126, starting at x = 70, y ≈ 790 (below the header block).
- Lines are width-checked to the card before render; quote text is centered-left aligned from x = 70 (not centered).
- Gold accent (201, 154, 44) is defined in the script but not used in the current render — the card is black-on-white only, matching the locked black/white + RGB-split brand (the RGB split lives in the avatar/logo, not the card body).

## Earlier dark variant (`make_card.py`, not current)
- Canvas: 1080 × 1920, near-black background (11, 11, 15).
- Header: "ADHD ENTREPRENEUR" centered (Liberation Sans Bold, 44, gold 255,209,102) at y = 150, thin rule below.
- Quote: Liberation Sans Bold, 96, off-white (245, 245, 245), wrapped at width 20, line height 118, centered block.
- Footer: "@adhdentrepreneurhq" centered (Liberation Sans Regular, 38, dim grey) at H − 170.

## Collage cards (`make_collage_card.py`)
- 1080 × 1350 (4:5), same tweet-card look, width-checked lines, 6 pages per set.
