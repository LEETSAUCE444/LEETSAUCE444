# ADHD Entrepreneur: AI Starter Kits site

**Live:** https://adhd-entrepreneur-starter-kit-store.netlify.app
**Netlify project:** `adhd-entrepreneur-starter-kit-store` (team leetsauce444, free plan)

**Status (Oct 26, 2026):** live on the Netlify address. Nothing is for sale: no checkout, no prices, no forms. It's the business website Stripe needs, plus the kit quiz.

## What's on it

- `public/index.html`: the home page
  - hero and sample build brief
  - the 4 kits, plus "suggest a kit"
  - the AI crew
  - the guarantee
  - the quiz call-out, FAQ, about and contact
- `public/quiz.html` + `quiz.js` + `quiz.css`: the kit quiz
- `public/policies.html`: refund and guarantee, terms, privacy
- `public/404.html`
- `netlify.toml`: publishes `public/` only, plus security headers

Netlify publishes only `public/`. This README and `extras/` are never served.

## Design (Wil, Oct 26)

- **Midnight dark,** with liquid-glass panels: blur, a specular rim and a top highlight. A blueprint grid sits over soft light that drifts behind the glass.
- **The color split is the brand's own RGB split,** sampled from the wordmark: warm trails on the left, cool on the right.
  - ARC Raiders was the reference for keeping the color split simple and retro-futuristic.
  - Nothing is copied: not their stripes, not their typeface (ITC Avant Garde), not their palette.
- **The split button,** per Wil's call on `q-accent`:
  - It's three tinted glass layers (red, green, blue), offset like the logo.
  - Pressing it slides the layers into line, and they add up to one pane of white glass.
  - `site.js` holds the link for 0.32 s so the merge shows, and skips the delay for reduced motion.
  - Quiz answers use the same merge when tapped.
- **Fonts:** Space Grotesk (display), Inter (body) and JetBrains Mono (labels). They're self-hosted in `public/assets/fonts` under the SIL Open Font License, so the site makes no third-party requests.

## The quiz

It follows Zucc's Hims-style breakdown: archetypes first, then one easy question per screen.

**Path:** 7 questions (8 if "Not sure yet")
1. What do you want to build?
2. Where are you now?
3. A short heads-up on how the guarantee works
4. Two branch questions, worded for that kit's type of person
5. Which AI do you use?
6. Hours per week
7. An optional "what does done look like?" in your own words

**"Not sure yet"** adds a "which sounds like you?" question. Its "None of these" option leads to a custom-kit result, matching Wil's note on `q-kits`.

**The result** shows, in order:
1. the kit
2. the build goal and deadline
3. the setup for their AI
4. the price and terms

Then comes "Email me when it launches", a pre-filled email to the brand inbox. There's no checkout yet.

**Every answer changes the result.** For example, the "first up" line, the lead source in the service goal, the spending-limit note, the AI setup note and the pace note.

**Privacy:** answers live in memory only. Nothing is stored or sent, and no analytics run. There's no medical or ADHD question.

**Not built yet** (needs Wil's go, and a privacy-policy update first):
- answer logging under an anonymous ID
- per-answer classification with a Claude call

Both need a server function and an API key in Netlify's environment variables.

## Free-plan notes

- Netlify injects a "Powered by Netlify" badge and an HTML comment on the free plan. The badge can't be hidden on that plan. A paid plan removes it.
- The badge's inline script is allowed in the CSP by hash. If Netlify changes the badge, the browser console shows the new hash to put in `netlify.toml`.

## Before anything goes on sale

1. **Register "ADHD Entrepreneur"** as a DBA or LLC (Wil's pick on `q-legal`). Once it's filed, put the registered name in `policies.html`.
2. **Confirm the draft terms:**
   - a 14-day claim window after the deadline
   - the 50%-off code valid 60 days
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
