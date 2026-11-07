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
- `public/kits.html` + `catalog.js`: the kit catalog
  - Categories: Service & trades, Stores & products, Content & audience, Digital products, and Custom.
  - Filter chips show one category at a time. Without JavaScript, every category stays visible.
  - New kits slot into their category.
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
