# ADHD Entrepreneur: AI Starter Kits site

**Live:** https://adhd-entrepreneur-starter-kit-store.netlify.app
**Netlify project:** `adhd-entrepreneur-starter-kit-store` (team leetsauce444, free plan)

**Status (Oct 27, 2026):** live on the Netlify address. Nothing is for sale: no checkout, no prices, no forms. It's the business website Stripe needs, plus the kit quiz.

## What's on it

- `public/index.html`: the home page
  - hero and sample build brief
  - the catalog by category
  - the AI crew
  - the guarantee
  - the quiz call-out, FAQ, about and contact
- `public/kits.html` + `kits.css` + `kits.js`: the kit storefront, themed as an early-2000s console startup menu (Wil, Nov 17; see the kit page design below)
  - Four kit tiles (Service & trades, Stores & products, Content & audience, Digital products), plus a "doesn't fit?" bar (`#custom`).
  - Each tile opens a detail sheet with the price and every item inside, before any checkout.
  - Home-page links like `kits.html#service` open that kit's sheet.
  - Without JavaScript, tiles still open their sheets through the URL hash.
- `public/quiz.html` + `quiz.js` + `quiz.css`: the kit quiz
- `public/policies.html`: refund and guarantee, terms, privacy
- `public/404.html`
- `public/assets/icons.svg`: the icon sprite
  - 61 icons from [Lucide](https://lucide.dev), ISC license (`assets/LICENSE-lucide.txt`)
  - Use one with `<svg class="ic"><use href="assets/icons.svg#name"/></svg>`.
- `netlify.toml`: publishes `public/` only, plus security headers

Netlify publishes only `public/`. This README and `extras/` are never served.

## Design (Wil, Oct 26–27)

- **Midnight dark,** with liquid-glass panels: blur, a specular rim and a top highlight. A blueprint grid sits over soft light that drifts behind the glass.
- **The color split is the brand's own RGB split.** ARC Raiders was the reference for keeping the split simple and retro-futuristic. Nothing is copied: not their stripes, not their typeface, not their palette.
- **The split button** (Wil's call on `q-accent`, softened on Oct 27):
  - Red, green and blue glass layers sit behind a frosted pane, offset and slightly out of focus. The color bleeds softly round the edges and sways a little.
  - Pressing it slides the layers into line and snaps them into focus: one pane of white glass.
  - `site.js` holds the link for 0.32 s so the effect shows, and skips the delay for reduced motion.
- **Colored glass:** the tints come from the split's family: warm, gold, green, cyan and violet (`.t-*` classes plus `.tinted`).
  - Each quiz answer and each catalog category gets its own tint.
  - A picked answer fills with its color.
- **Icons** on every quiz answer, kit, category, crew role and guarantee step.
- **Fonts:** Space Grotesk, Inter and JetBrains Mono, self-hosted under the SIL Open Font License.

## Kit page design (Wil, Nov 17)

The kit page has its own look, separate from the rest of the site. The reference is the preview at https://claude.ai/artifact/5NVdjExFHeDiH7pPi2g2Fh. Zucc's full brief is in the shared sheet, Handoffs tab, row 46.

- **The look:**
  - a black canvas with a faint 48 px grid
  - a floating glass cube whose faces are the section nav: Kits, How it works, What's inside, FAQ
  - a PRESS START pixel button
  - item-shop kit tiles with a white triangle cursor
  - a glass detail sheet
- **Colors:**
  - violet `#7B61FF` (primary)
  - green `#22C55E` (confirm; only the buy button)
  - red `#EF4444` (back)
  - supporting blue `#2E4BFF` → `#1E3A8A` (tile borders and the contents bar)
- **Fonts:** Nunito and Press Start 2P, self-hosted under the SIL Open Font License. Pixel type appears only on the start button, eyebrows and small tags.
- **Fully original:**
  - No console maker's name, logo, cube-in-cube mark, sounds, fonts or art.
  - No game-store assets.
  - Confirm and back are plain green and red dots, not lettered buttons.
- **Motion:**
  - The cube turns once every 14 seconds and eases to a face when picked.
  - A boot screen of about 1 second plays once per browser session. It's skippable, and it's skipped on deep links.
  - No audio, ever.
  - With reduced motion: no boot screen, a still cube, and no blinking or bobbing.
- **Phones:** a small spinning cube sits above a swipeable row of sections. Tiles go 2 across, and the detail sheet goes full screen.
- **Live since Nov 18, 2026** (Netlify deploy `6afd10b2fa5505a9c3aa915c`).
- **Placeholders to replace before launch:**
  - the price ($49)
  - the 30-day deadline

  Both are in `kits.html` and are marked PLACEHOLDER on the page.
- **The buy button doesn't check out.** Until checkout exists, it shows "Kits aren't on sale yet" with an email-at-launch link.

## The quiz

It follows Zucc's Hims-style breakdown, simplified on Oct 27 at Wil's request. Each question is a short line, and each answer is an icon tile.

**Path:** 6 taps
1. What are you building?
2. Where are you at?
3. Two questions for that kit
4. Which AI do you use?
5. Time per week

"Not sure yet" adds "Which sounds like you?", for 7 taps. Its "None of these" option goes to the custom kit, for 5 taps.

**The result** shows, in order:
1. the kit and what's inside
2. the goal and deadline
3. the setup for their AI
4. the price and guarantee

Then an "Email me at launch" pre-filled email. There's no checkout yet.

**Every answer changes the result:** the "first up" line, the lead source in the service goal, the setup notes and the pace.

**The miss discount is never shown** on the site, the quiz or the policies (Wil, Oct 27). It goes only in the follow-up email after a miss (`kits/emails/miss-followup.md`). Buyers still see that a miss means no refund.

**Privacy:** answers live in memory only. Nothing is stored or sent, and no analytics run. There's no medical or ADHD question.

**Not built yet** (needs Wil's go, and a privacy-policy update first):
- answer logging under an anonymous ID
- per-answer classification with a Claude call

## Free-plan notes

- Netlify injects a "Powered by Netlify" badge and an HTML comment on the free plan. The badge can't be hidden on that plan. A paid plan removes it.
- The badge's inline script is allowed in the CSP by hash. If Netlify changes the badge, the browser console shows the new hash to put in `netlify.toml`.

## Before anything goes on sale

1. **Register "ADHD Entrepreneur"** as a DBA or LLC (Wil's pick on `q-legal`). Once it's filed, put the registered name in `policies.html`.
2. **Confirm the draft terms:**
   - a 14-day claim window after the deadline
   - the 7-day fix-or-refund
3. **Set the prices, deadlines and proof per kit.** They go on each kit's page before checkout.
4. **Have someone qualified read** `policies.html`.
5. **Domain:** `adhdentrepreneurhq.com` isn't registered yet. Netlify can attach it once it's bought.

## Deploy

From this folder, run the command the Netlify MCP `deploy-site` tool returns for project `be879c26-3e8f-408d-b0c1-8fc66b47fa52`. It uploads this folder, and Netlify publishes `public/`.

## Rules this site keeps

- **Faceless.** No personal name or photo.
- **No income or medical claims.** Goals are always something built.
- **Price and full terms before payment.**
- **No ad pixels, no analytics.** Quiz answers never leave the browser.
