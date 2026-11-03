# goodguyswash.com — full site review (Nov 3, 2026)

Review only. Nothing on the live site, Netlify, the server functions or Flyra was changed. All form tests ran on a localhost copy in preview mode (the site's own code sent nothing). No phone numbers were typed on the live site.

## 1. Summary

1. One real broken link: the "text us for partner pricing" link on /commercial points to a leftover placeholder (`${PARTNER_SMS}`) and 404s. One-minute fix.
2. Three pages the gate requires are missing: privacy policy, terms, and a branded 404 page (visitors see Netlify's teal default). Drafts are below.
3. Share previews are broken on the home page, /holiday and all 39 Christmas-lights pages (relative image path, no og:url), so texted or Facebook-posted links show no picture.
4. Text-message consent: the game's "Text me" box starts checked, and people who leave a form unfinished can be texted even if they never ticked consent. Both matter for 10DLC registration.
5. Speed and SEO housekeeping: no caching headers on any asset, oversized images (the 960px logo is the first thing every page paints), Google Fonts blocking render, canonical URLs that don't match the links, and 78 city pages that differ by only the city name.

## 2. The 20-item gate (run against the live site)

LEGAL + TRUST
1. Privacy policy — FAIL, no page, no footer link (checked /privacy, /privacy.html: 404). See #3.
2. Terms page — FAIL, no page (checked /terms, /terms.html: 404). See #3.

CONVERSION
3. One clear call to action — PASS. "Get my free quote" + "Text us" on every page type (/, /window-cleaning, /holiday, city pages). /referral has three competing actions; see #44.
4. FAQ — PASS. FAQs exist on 93 of 96 pages with matching FAQ structured data. /about, /gallery, /referral have none, which is fine.

SEO + TECHNICAL
5. robots.txt — PASS (allows all, lists sitemap).
6. sitemap.xml — PASS, 96 URLs, all return 200. Uses .html URLs; see #8.
7. Custom 404 — FAIL. /nonexistent-page shows Netlify's default "Page not found". See #2.
8. Alt text — PASS. 0 images missing alt across all 96 pages; logos repeated in header/footer correctly use alt="".
9. Analytics — FAIL. Click events are coded but no tag loads on any page (/, /gallery, /holiday). See #29.
10. Meta titles — PASS with one fix: /holiday title is 26 characters. See #17.
11. Meta descriptions — FAIL (partial). The 39 window-cleaning city pages have 43–57 character descriptions ("Family-owned window cleaning in Lehi, Utah."). See #17.
12. Social share previews — FAIL. /, /holiday and 39 Christmas pages use og:image="assets/logo.png" (relative), no og:url, no twitter:card. See #6.
13. Favicon — PASS (PNG). No apple-touch-icon; see #41.
14. Canonical URLs — FAIL. Every page has one, but they point at .html URLs while every link on the site uses clean URLs, and both versions load with 200. See #8.

PRIVACY + EXPERIENCE
15. Cookie consent — N/A. The site sets no cookies and loads no analytics or ad pixels. It becomes needed if GA4, a Meta pixel or Google Ads tag is added (then a notice + privacy policy update; a full banner is only required if EU/UK visitors matter).
16. Mobile — FAIL (minor). No sideways scroll at 360/390, but the home page scrolls 4px sideways at 768px, and several tap targets are under 44px. See #10, #11, #22, #23.
17. Accessibility — FAIL (minor). Lighthouse 91–100, but: star ratings use aria-label on a div, the "Good Guys 5" slideshow auto-advances with no pause, errors aren't tied to fields, 56 pages have no skip link. See #19.
18. Forms end to end — localhost: PASS (every step of the home quote form, holiday form and AI preview walked, the game bubble opened and its prize-form code read; validation messages and thank-you screens work). Live submissions: NOT RUN, needs Wil's OK (Q1).
19. Broken links — FAIL. 1 of 115 internal targets is broken (/commercial partner-pricing link). All 4 external links could not be verified from this sandbox (Google Maps, Flyra review card, Facebook, Instagram). See #1.
20. Performance — FAIL. Lighthouse mobile (local copy, simulated throttling): home 79, /holiday 74 (LCP 7.0 s), /window-cleaning 84, city page 89, /gallery 92. No asset caching, oversized images, render-blocking fonts. See #12–#14, #24.

## 3. Findings

Format: what and where · why it matters · fix · size S/M/L · needs Wil?

### Must fix

**1. Broken partner-pricing link on /commercial.** The FAQ answer "Builders and cleaning companies can text us for partner pricing" links to the literal text `${PARTNER_SMS}`, a template placeholder that never got filled in. It returns a 404. · A builder trying to reach Wil hits a dead end. · Point it at `sms:+18015155588?&body=Hi%20Good%20Guys%2C%20I%27m%20a%20builder%2Fcleaner%20and%20I%27d%20like%20partner%20pricing.` · S · No.

**2. No custom 404 page.** Any mistyped or old URL shows Netlify's grey-and-teal "Page not found" with a link to Netlify's support guide. · Off-brand dead end; the gate requires one. · Add 404.html in the brand (cream paper, navy border, mascot) with: heading "Well, that's a streak."; text "That page isn't here. Let's get you back to clean windows."; buttons "Go to the home page", "Get my free quote", "Text us at (801) 515-5588". Netlify serves 404.html automatically. · S · No.

**3. No privacy policy or terms pages, and no footer links to them.** · Required by the gate, expected by phone carriers for text-message (10DLC) registration, and the site already collects names, phones, addresses, home photos, unfinished form answers and ad-click IDs. · Add /privacy and /terms (drafts in section 7), link both in the footer of all 97 pages, and link the privacy policy next to every text-consent checkbox. · M · Yes, Q2–Q4.

**4. The game's "Text me" consent box starts checked, and that carries into the quote form.** (`<input type="checkbox" name="sms" checked>` in assets/squeegee-game.js.) The two quote forms and the AI preview start unchecked, which is right. · Pre-checked consent is not valid consent under carrier 10DLC rules or the TCPA, and it is the one place on the site where it happens. · Remove `checked`. Keep the prize flow otherwise. · S · No.

**5. People who leave a form unfinished can be texted without consent.** When a name and 10-digit phone are typed and the dialog closes or the page is left, the site sends an "unfinished" lead (home quote and holiday forms). The consent box is on the last step, so almost every unfinished lead has consent = no, and the site sends it anyway. Flyra may auto-text that number. · A text to someone who never agreed is the exact pattern carriers reject. · Two parts: (a) site: send the lead but include `sms_consent` plainly, and change the consent copy so it covers follow-ups (section 8); (b) Flyra: make the "unfinished lead" automation text only when consent is yes, or have it notify Wil instead of texting the customer. Part (b) is a Flyra setting, not a site change, so it needs Wil. · M · Yes, Q5.

**6. Share previews broken on /, /holiday and the 39 Christmas-lights pages.** og:image is the relative path `assets/logo.png` (Facebook, iMessage and WhatsApp need a full https URL); there is no og:url and no twitter:card on any page; the home og:title is just "Good Guys Window Washing". /lights-quote is the only page done fully right. · Every link Wil texts to a customer or posts on Facebook shows as a bare grey link. · On every page add `og:url` (the canonical), `og:type`, `og:image` as `https://goodguyswash.com/assets/og-default.jpg` (new 1200×630 image: mascot on cream with "Good Guys Window Washing · Salt Lake & Utah County"), `og:image:width/height`, `twitter:card=summary_large_image`. Holiday pages get a holiday version. Home og:title: "Window Cleaning in Salt Lake & Utah County | Good Guys". · M · Needs a 1200×630 image (Website chat can make it from logo.png).

**7. Deal text the Nov 16 script can't hide.** The date-hiding script works: with the clock set to Nov 16 every `[data-deal]` element disappeared on /, /holiday and the Christmas pages, and the FAQ structured data contains no date. Still showing after Nov 15: (a) llms-full.txt lines 985 and 1097 ("15% off installation · Book by November 15th"); (b) /lights-quote meta description, og:title "Holiday Lights: 15% Off Install (Book by Nov 15)", og:description, og:image:alt and the image itself (lights-quote/og-holiday-lights.jpg has the deadline printed on it); (c) the home FAQ answer "Book by November 15, 2026 for 15% off installation" is hidden on the page but still printed in llms-full.txt. · AI answer engines and texted links will keep advertising an expired deal. · On Nov 16: remove those two llms-full.txt lines, rewrite /lights-quote meta to the post-deal wording (section 9), swap the og image for one without a date. · S · No, but it is a dated task (see section 9).

**8. Canonical URLs, sitemap and links disagree.** Canonicals and sitemap say `/about.html`; every link on the site says `/about`; both load with 200 and neither redirects. og:url (when added) and llms.txt also use .html. · Google can index two copies of each page and split signals; it also makes the share-preview fix inconsistent. · Pick the clean URL everywhere: canonical `https://goodguyswash.com/about`, sitemap and llms.txt the same, and add a Netlify `_redirects` rule `/*.html /:splat 301` for everything except 404.html (Netlify's "Pretty URLs" can do this too). Keep `/holiday.html`-style links working via the redirect. · M · No.

**9. The 78 city pages are the same page with the city name swapped.** Measured: each window-cleaning city page shares 73–85% of its 8-word phrases with every other one and has 0–2 unique words out of ~1,290; the Christmas pages share 87–90%. The only local text is "Lehi is part of our regular service area in Utah County, along with American Fork, Highland, Saratoga Springs, Cedar Hills and more." · Google treats this as doorway/duplicate content; at best only a few of the 78 rank. · Make each page earn its spot: 3–4 sentences only true of that city (hard-water and sprinkler-spot notes for its water, typical home style and stories, HOA areas, a landmark or two, drive time from Lehi), one real photo of a job done there when Wil has one, a city-specific FAQ ("Do you clean windows in Traverse Mountain?"), and a full-length meta description. Start with the 10 cities where Wil actually works most, and leave the rest as they are rather than deleting them. · L · Yes, Q6.

**10. Tap targets under 44px on phones.** Services dropdown items are 38px tall on every page; the header phone link is 22px tall; the game's pixel guy is 36×40; the "How plans work and what you save" link is 23px; the service-area map's city links are about 49×10px and there are 39 of them in the tab order. · Mis-taps, and the map links are unusable by touch or screen reader. · Dropdown items `min-height:44px`; phone link `padding:8px 0`; game button `min-width:44px;min-height:44px` with the sprite centered; make the SVG map decorative (`aria-hidden="true"`, no tabindex, no links) and rely on the city lists under it. · S · No.

**11. Sideways scroll on the home page at tablet width (768px).** The reviews carousel figure runs 4px past the viewport (`FIGURE.review right=1109` at 768). · The whole page wobbles sideways on iPads and large phones in landscape. · `#rv{overflow-x:clip}` and give `.review` cards `max-width:calc(100vw - 48px)` or use scroll-snap with `overscroll-behavior-x:contain`. · S · No.

### Should fix

**12. No caching on any asset.** All 42 assets (images, fonts, the 3MB solar video, the game script) are served with `Cache-Control: public,max-age=0,must-revalidate`, so a return visitor re-downloads everything. · Slower repeat visits and higher Netlify bandwidth; Lighthouse flags 0.1–1.1MB of avoidable transfer per page. · Add a `_headers` file: `/assets/*  Cache-Control: public, max-age=31536000, immutable` and `/lights-quote/*.jpg` the same. When an asset changes, change its filename (logo-v2.png). · S · No.

**13. Oversized images, and the logo is the slowest first paint.** The 960×960 PNG logo (60KB) is the Largest Contentful Paint element on every page and renders at 300–480px; on holiday pages the four style photos are 1380px JPEGs (220–260KB each) shown at 688px and again as 128px thumbnails; gallery WebPs are 300–400KB; the solar video is 3MB and set to autoplay. Lighthouse mobile LCP: home 4.3 s, /holiday 7.0 s. · Slow first impression on phones, which is most of the traffic. · Export logo.webp at 480px (~10KB) and add `fetchpriority="high"` on the hero mascot; convert style-*.jpg to WebP at 900px plus 200px thumbs; recompress gallery images to ~120KB; re-encode the solar video to 720p ~1MB with `preload="none"` and a poster, and only autoplay when in view. · M · No.

**14. Google Fonts block render and over-request.** The stylesheet costs 450–790 ms before text can paint; it asks for 12 Barlow variants but the CSS only uses weights 400/500/600/700 and italic in three places. · Delays every page; causes the heading reflow in #24. · Request only the used weights, or self-host the Barlow woff2 files in /assets like Magneto already is, with `<link rel="preload" as="font">` for the two hero fonts and `font-display: swap`. · S/M · No.

**15. Security headers: only HSTS is set.** · Cheap protection against clickjacking and MIME sniffing; some scanners mark the site down for it. · In `_headers` add: `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy: geolocation=(), microphone=()`. Leave camera alone (the photo upload uses a file picker, not the camera API, so it is fine either way). Skip a Content-Security-Policy for now because every page has inline scripts. · S · No.

**16. Structured data gaps.** LocalBusiness has no address, no geo, hours Mon–Fri 8–5 (unverified against Google Business Profile), sameAs lists Instagram and the Maps link but not the Facebook page the footer links to. /holiday, /commercial, the 11 service pages and the 39 Christmas pages reference `provider: {"@id": ".../#business"}` without that entity on the page, so the reference dangles. The window-cleaning city pages embed the full business, which is right. · Google can't connect the pages to the business profile; address and hours are the local-ranking fields. · Put the same compact LocalBusiness node (name, url, telephone, address with at least Lehi/UT/postal code, geo, hours, sameAs with Facebook) on every page, keep the Service node pointing at it. Also give it a more specific type: `"@type": ["LocalBusiness","HomeAndConstructionBusiness"]`. · M · Yes, Q7 (address to publish, exact GBP hours).

**17. Titles and descriptions that need work.** /holiday title "Good Guys Holiday Lighting" (26 chars, no location or service). 39 window-cleaning city descriptions at 43–57 chars. /window-cleaning (78), /window-cleaning-plans (84) and /gallery (93) descriptions are short. The home H1 is "Window Washing". · Titles and descriptions are the search ad. · /holiday title: "Christmas Light Installation in Salt Lake & Utah County | Good Guys". City description template (fill the city): "Window cleaning in Lehi, UT from Good Guys Window Washing. Exterior cleaning from $200, screens, sills and hard water spots, plans that save every visit. Text (801) 515-5588 for a quote in minutes." /gallery: "Real before and after photos from Good Guys Window Washing jobs in Salt Lake and Utah County: hard water spots, screens, sliding doors and basement windows, same glass, same angle." Home H1: keep the script "Window Washing" and add a second line inside the H1 in the condensed face: "in Salt Lake & Utah County". · S · No.

**18. Invalid page structure on 41 pages, missing landmarks.** The home page, /holiday and the 39 Christmas pages have no `</head>` and no `<body>` tag (browsers recover, validators and some crawlers don't). No page uses a `<header>` element (the top bar is a div), and the skip link exists only on those 41 pages, not the other 56. · Clean HTML is cheap insurance for SEO tools and screen readers. · Add `</head><body>` after the last `<style>`; change `<div class="top">` to `<header class="top">`; copy the skip link to the 56 pages. · S · No.

**19. Accessibility details (WCAG 2.2 AA).** (a) `.stars` is a `<div aria-label="5 stars">`, which assistive tech ignores on a div: add `role="img"`. (b) Holiday style buttons carry both `aria-pressed` and `aria-checked` with `role="radio"`: drop `aria-pressed`. (c) The "Good Guys 5" slideshow auto-advances every 5 s with no pause control (WCAG 2.2.2): add a Pause button or stop auto-advance after one loop, and stop it on hover/focus (it already stops under reduce-motion). (d) Form errors ("Tap at least one service.", "Pick how many stories your home has.") appear at the bottom of the step and aren't linked to the field: add `role="alert"` and `aria-describedby`, and on the long holiday step 3 show the error under the field group it belongs to. (e) The two range sliders have no `aria-valuetext` ("50% after"). (f) The hidden "Leave this empty" honeypot labels should get `aria-hidden="true"`. (g) Brand link `aria-label` should start with its visible text exactly: "Good Guys Window Washing, home". Keyboard: dialog is a true modal, Escape closes, focus ring is visible on every control including tiles, dropdown and mobile menu close on Escape. · M · No.

**20. No way to call from the main site.** Every phone link on all 96 pages is `sms:`; `tel:` exists only on /contact and /commercial. The business rule is "text or call". · Older homeowners and anyone on a desktop can't tap to call. · Footer line becomes "Text or call: (801) 515-5588" with the number as a `tel:` link and a separate "Text us" button; add "Or call" under "Or text us at" in the closing CTA band and the thank-you screens. · S · No.

**21. Service names don't match across the site.** Nav: "Soft washing". Footer and city pages: "House washing" and "Roof washing". Quote form tiles: "House soft wash", "Roof washing". Home services grid: "Soft washing — House & roof". Page titles: "House Washing", "Roof Washing". · Customers don't know "soft washing"; consistency builds trust. · Use "House washing" and "Roof washing" everywhere customers see a name, and explain "a gentle soft wash" in the body copy. Nav gets two entries or "House & roof washing". · S · No.

**22. Mobile hero puts the call to action below the first screen.** On a 390×780 viewport the mascot is 340px tall, so the headline sits below it and "Get my free quote" lands at the very bottom edge of the first screen. The eyebrow wraps "SALT / LAKE & UTAH COUNTY" and the sub-headline leaves "GUYS!" alone on its line. · The first screen on a phone is mostly a logo. · Under 480px: mascot `max-width:200px`, eyebrow with a forced break before "Salt Lake", `text-wrap:balance` on the sub-headline, and the two buttons side by side. Same on /holiday and the Christmas pages (mascot 340px there too). · S · No.

**23. Mobile nav strip is clipped with no hint it scrolls.** At 360–390px the row shows "Holiday Lighting · Services · PLAN…" cut off (holiday: "Styles · Your home · OU…"). · Looks broken; "Plans", "Commercial", "Reviews" are invisible on phones unless you guess to swipe. · Add a right-edge fade mask (`mask-image: linear-gradient(90deg,#000 85%,transparent)`) and `scroll-padding`, or drop the strip on phones since the hamburger menu already lists everything. · S · No.

**24. Layout shift on desktop.** Measured CLS: home 0.07, /holiday 0.16–0.19, Christmas city pages 0.10–0.12 (over the 0.1 "good" line). Causes: web-font swap on the script headings, the game adding `padding-top:72px` to the hero after it loads, and the holiday nav squeegee animating `left`. · Google's Core Web Vitals; visible jump on load. · Reserve the hero padding in CSS from the start (`.hero{padding-top:72px}` whether or not the game loads), preload the two display fonts (#14), and animate the squeegee blade with `transform:translateX()` instead of `left`. · M · No.

**25. Animations that paint or reflow, and pulses that never stop.** `ctaPulse` and `popPulse` animate outline-color/outline-offset; `planGlow` and `planAura` animate box-shadow on an infinite loop; `gg5Timer` animates width; `sqBlade` animates left. The plan cards glow and twinkle forever (2.6 s and 2.8 s loops) and `popPulse` loops forever on hover. Easing uses four different curves and durations from 100 ms to 700 ms. Reduced-motion is handled well: 0 running animations under "reduce" on every page tested. · Jank on low-end phones (Lighthouse's simulated 4× slowdown measured 2.1 s of main-thread work on the home page), and constant motion pulls the eye off the buttons. · Rebuild these on transform/opacity only: pulses as a scaled pseudo-element ring, glow as an opacity fade of a pre-rendered shadow layer, the timer as `scaleX` on a bar, the blade with `translateX`. Run plan twinkles 3 cycles then stop (`animation-iteration-count:3`). One easing (`cubic-bezier(.2,.8,.3,1)`) and three durations (150/220/320 ms) via custom properties. · M · No.

**26. Reviews section while the Google API key is pending.** Six built-in quotes with first names, no source or date. · Fine as a stopgap; once live reviews arrive, keep both. · Add "Google review" and the month under each name once Wil confirms they are Google reviews (Q8); show the real rating and count next to "Read our Google reviews" only from the live feed, never typed in. · S · Yes, Q8.

**27. Quote form length and the long step 3.** The home form is 4 steps; step 3 holds plan choice, preferred days, address, "who referred you" and notes. The holiday form's step 3 holds style, stories, the wash upsell, address and notes, and its error appears under the notes box. · The more scrolling per step, the more drop-off on phones; the contact step is last, so unfinished leads rarely have consent (see #5). · Move the address into the contact step, keep plan + days on step 3, put "who referred you" behind a small "Were you referred?" toggle, and show errors next to the group they belong to. Consider moving name + phone to step 2 like the holiday form does, with consent, so the unfinished-lead text has consent attached. · M · No.

**28. Light-preview wait and error screens.** Good copy ("Hanging your lights… This takes about 20 seconds", four clear error messages). Missing: a progress bar or countdown, a Cancel, and a line saying the photo is discarded on failure. · 20 seconds with no movement feels broken on a phone. · Add a thin animated bar (transform only) and "Cancel"; on error add "Your photo wasn't kept." · S · No.

**29. Analytics not set up.** Events are coded (`quote_open`, `quote_unfinished`, `preview_photo_added`…) but fire only if a tag exists. · Wil can't see which pages or buttons produce quotes. · Add GA4 (one snippet in the shared head), then update the privacy policy. Cookie banner not required for a US local business, but say it in the policy. · S · Yes, Q9 (GA4 measurement ID).

**30. www and http redirects could not be verified** from this sandbox (its proxy blocks www.goodguyswash.com). The vCard on /contact lists `https://www.goodguyswash.com`. · If www doesn't redirect to the bare domain, the contact card sends people to a different host. · Website chat: confirm `http://`, `http://www.` and `https://www.` all 301 to `https://goodguyswash.com/`; change the vCard URL to the bare domain. · S · No.

**31. Every page loads about 65KB of inline CSS, 32–52KB of it unused on that page**, and 97 copies of the same header, footer and base styles. · With no caching (#12) a 5-page visit downloads ~300KB of CSS; also makes every site-wide fix a 97-file edit. · Move the shared CSS to `/assets/site.css` (cached, versioned) and keep only page-specific rules inline; same for the shared nav/footer JS. Minify squeegee-game.js (78KB → ~40KB). · M · No.

**32. Sitemap uses .html URLs and no lastmod.** · Tied to #8. · After the clean-URL switch, regenerate with clean URLs and `<lastmod>`. · S · No.

### Polish

**33. Services grid cards misalign.** "Solar & skylights" and "Pressure washing" wrap to two lines, so the "ADD-ON" badges and descriptions sit at different heights across the grid. · Fix: `.svc{display:grid;grid-template-rows:auto auto auto 1fr}` or shorter labels ("Solar panels", "Pressure wash").

**34. Review cards on phones leave a big empty block** under short reviews because all cards share one fixed height. Let height fit content and align with `align-items:stretch` only on desktop.

**35. Service-area map labels.** A dot near Orem/Vineyard has no label at phone width, Lindon's dot sits off its label, labels are 10px. Tie in with #10: keep the map as a picture, make the lists the interface.

**36. Heading breaks.** "DON'T WORRY, WE'RE THE GOOD / GUYS!" at 390px; "See It on / a Home" on /holiday. Add `text-wrap:balance` to `.hero .sub` and section h2s (already used on some).

**37. /contact page drifts from the brand.** 14px rounded corners and black (#151515) borders/shadows, while the rest of the site uses square corners and navy. Switch to the navy border + offset block shadow. Also set the vCard `N:` field (it's empty) to "Good Guys Window Washing" so iPhones sort it correctly.

**38. Type scale.** The home page CSS uses 20 distinct pixel sizes (11–56px). Define a scale as custom properties (12, 14, 16, 18, 21, 26, 34, 42, 56) and map everything to it.

**39. Icons.** The stroke icon set is consistent and fits each service; no emoji anywhere (good). Two outliers: the "Sill & track detailing" dropdown icon is heavier (filled rects) than its neighbours, and the "+" in "+ Add to my quote" is a text character rather than an icon. Redraw the track icon on the same 2px stroke; use the same plus icon as the mobile menu.

**40. Hero bullets.** "5-star service" is a claim the live reviews should back; keep it, but once GA/reviews are live consider "5-star Google reviews" only with the real count.

**41. Favicons.** Only a 160px PNG. Add `apple-touch-icon` (180×180 PNG), an SVG favicon, and a 32px PNG so iPhone home-screen bookmarks and Google's tab icon look right.

**42. "Learn more" link** in the home commercial band → "About commercial cleaning" (Lighthouse flags it; screen readers hear it out of context).

**43. Two cost FAQs on the home page** ("How much does window cleaning cost?" and "How much does window cleaning cost in Utah County?") say overlapping things. Rename the second to "What does a typical home cost?" and keep the worked numbers there.

**44. /referral has three main actions** (Get my free quote, Share your link, Start my quote). Lead with "Share your link" for customers and "Start my quote" for referred visitors; move "Get my free quote" to the closing band only.

**45. Holiday page says "Most homes run $600 and up"** but llms.txt, llms-full.txt and /lights-quote don't mention it, and the holiday FAQ says pricing is per home. Confirm the number (Q10) and then say it in all four places or none.

**46. Holiday and Christmas footers lack the hours line** that the main footer shows ("Mon–Fri, 8 AM–5 PM"). Add it.

**47. Game button hit area and label.** The pixel guy is a `<button>` with a good label; make the hit area 44px (#10) and give the speech bubble `role="status"` so screen readers hear it.

**48. The game loads its own 8-bit font and 78KB script on every home visit** even for people who never tap the guy. Load the script only on first tap or after `requestIdleCallback`.

**49. Hidden footer line `<span class="f-ins" hidden>`**: present on the expected 56 pages, absent on /holiday and the 39 Christmas pages. Left as is on purpose; noted only so nobody "fixes" it.

**50. Prices**: all whole dollars, no cents anywhere (checked all 96 pages and both llms files). "From $200", plan numbers ($50/$100/$150, 10/15/20%, $228/$242/$256/$285, $235), referral $50 and the 7-Day Rain Guarantee wording agree everywhere, including llms.txt. No "licensed", "insured" or "bonded" in visible text on any page. Nothing to fix; recorded so the next review can skip it.

## 4. Questions for Wil

- **Q1.** May the Website & Files chat run one real submission per form (home quote, holiday quote, a Christmas-city form, the AI preview, the game prize screen) using "Wil TEST" and your own number? You'd then delete those 5 test leads in Flyra.
- **Q2.** Which AI image service makes the light preview (needed for the privacy policy)?
- **Q3.** Legal business name and the address or at least city/ZIP you want printed in the privacy policy, terms and structured data. Is it a registered LLC?
- **Q4.** Is goodguyswindowwash@gmail.com the right contact email to publish for privacy requests (it's already in the vCard on /contact)?
- **Q5.** In Flyra, does the "unfinished lead" automation text the customer? If yes, are you OK changing it to text only when the consent box was ticked, or to notify you instead?
- **Q6.** Which 10 cities do you actually serve most? Any job photos with the city known? This decides where the city-page rewrite starts.
- **Q7.** Your Google Business Profile: exact hours, the address or service-area setting, and the Facebook page URL to list. The sandbox couldn't open maps.app.goo.gl to compare.
- **Q8.** Are the six built-in reviews copied from Google? OK to label them "Google review" with the month?
- **Q9.** Do you want Google Analytics 4 added now? If yes, create the property and give the Website chat the "G-" measurement ID (never paste keys into chat).
- **Q10.** Is "Most homes run $600 and up" for lights still right for this season?
- **Q11.** After Nov 15: keep "50% off a window wash with every install" through the season? And do you want a "book for next year" list after January?

## 5. What was checked, and what couldn't be

Checked: all 96 sitemap pages plus /contact, /lights-quote, /lights, 404 behaviour, _redirects/_headers (404 as expected), robots.txt, sitemap.xml, llms.txt, llms-full.txt, the vCard, all 42 assets with sizes and headers, 115 internal link targets, every page's title/description/canonical/og/structured data/headings/alt text/forms/forbidden words/prices, city-page similarity across all 78, screenshots of 16 page types at 360/390/768/1280/1440 (console, failed requests, overflow, tap targets, layout shift, animations with and without reduce-motion), every step of both quote forms, the AI preview form (upload, validation, busy and result screens), the game's bubble and prize form code, the Services dropdown and mobile menu by keyboard, Escape handling, focus rings, Nov 16 clock test on three page types, Lighthouse mobile on 5 pages (local copy, simulated throttling, so treat scores as relative).

Couldn't: (a) the 4 external links (Google Maps, Flyra review card, Facebook, Instagram) and the www/http redirects, because this sandbox's proxy blocks those hosts; (b) Google Business Profile match and "how the site appears in Google" (web search returned no listing for the business; Semrush had no API units left); (c) competitor sites could not be fetched, so the competitor ideas in section 10 come from search-result snippets only; (d) real Core Web Vitals from PageSpeed Insights (no field data accessible); (e) a real iPhone/Android (used Playwright's iPhone 13 emulation); (f) live form submissions (rule 3, needs Q1); (g) the three server functions (left alone by design).

## 6. Copy for Website & Files chat (build spec, all items pending Wil)

Finding → files → where → change. Everything below is PENDING WIL until he replies "approve".

- **#1** · commercial.html · `<a href="${PARTNER_SMS}">text us for partner pricing</a>` · replace href with `sms:+18015155588?&amp;body=Hi%20Good%20Guys%2C%20I%27m%20a%20builder%2Fcleaner%20and%20I%27d%20like%20partner%20pricing.`
- **#2** · new 404.html at site root · brand shell (same head/footer as about.html), `<main>` with h1 "Well, that's a streak.", p "That page isn't here. Let's get you back to clean windows.", buttons: `<a class="btn red" href="/">Go to the home page</a> <a class="btn" href="/#quote">Get my free quote</a> <a class="btn ghost" href="sms:+18015155588">Text us at (801) 515-5588</a>`; add `<meta name="robots" content="noindex">`.
- **#3** · new privacy.html and terms.html (text in section 7); all 97 pages footer: append `<a href="/privacy">Privacy</a> · <a href="/terms">Terms</a>` to the footer links row; index.html, holiday.html, 39 christmas-*.html: after each `label.check` consent label add `<a class="fine" href="/privacy">Privacy policy</a>`.
- **#4** · assets/squeegee-game.js · `<input type="checkbox" name="sms" checked>` → remove `checked`; label text per section 8.
- **#5** · index.html + holiday.html + 39 christmas pages, function `sendUnfinished()` · ensure payload includes `sms_consent: $("qSms").checked ? "yes" : "no"` and `lead_state: "unfinished"`; consent copy per section 8. Flyra automation change is Wil's.
- **#6** · all 97 pages `<head>` · add `<meta property="og:type" content="website">`, `<meta property="og:url" content="https://goodguyswash.com/PATH">` (canonical, clean URL), `<meta property="og:image" content="https://goodguyswash.com/assets/og-default.jpg">`, `og:image:width 1200`, `og:image:height 630`, `<meta name="twitter:card" content="summary_large_image">`; holiday pages use assets/og-holiday.jpg (no date on it). index.html og:title → "Window Cleaning in Salt Lake & Utah County | Good Guys". New assets: og-default.jpg, og-holiday.jpg (1200×630).
- **#7** · llms-full.txt lines 985, 1097 → delete on Nov 16; lights-quote/index.html meta description/og:title/og:description/og:image:alt → section 9 wording; lights-quote/og-holiday-lights.jpg → version without the date.
- **#8** · all 97 pages `<link rel="canonical">` → clean URL (`/about`, `/holiday`, `/window-cleaning-lehi-ut`); sitemap.xml and llms.txt/llms-full.txt links → clean URLs; new `_redirects`: `/index.html / 301` and `/*.html /:splat 301` placed after any `/lights` and `/lights-quote` rules; keep 404.html served by Netlify.
- **#9** · window-cleaning-{city}-ut.html, christmas-lights-{city}-ut.html · new `<section class="block local">` after the hero with 3–4 city-specific sentences from Wil, optional `<figure>` photo, one extra FAQ `<details>`; `<meta name="description">` per #17 template.
- **#10** · shared CSS · `.nav-dd-menu a{min-height:44px;display:flex;align-items:center}`; `.hphone a{padding:8px 0;display:inline-block}`; `.gg8-guy{min-width:44px;min-height:44px}`; service-area.html + index.html map `<svg>`: add `aria-hidden="true"`, replace `<a class="city" href tabindex="0">` with `<g class="city">`.
- **#11** · index.html CSS · `#rv{overflow-x:clip}` and `.review{max-width:calc(100vw - 48px)}` inside `@media (max-width:900px)`.
- **#12 / #15** · new `_headers`:
  ```
  /assets/*
    Cache-Control: public, max-age=31536000, immutable
  /lights-quote/*.jpg
    Cache-Control: public, max-age=31536000, immutable
  /*
    X-Content-Type-Options: nosniff
    X-Frame-Options: DENY
    Referrer-Policy: strict-origin-when-cross-origin
    Permissions-Policy: geolocation=(), microphone=()
  ```
- **#13** · assets · logo-480.webp (from logo.png), logo-holiday-480.webp; style-{before,warm,classic,multi}-900.webp + -200.webp; gallery WebPs recompressed (quality 75, max 1400px); solar-panel-cleaning-720.mp4 (~1MB). Pages: hero `<img class="mascot" src="assets/logo-480.webp" fetchpriority="high" width="300" height="300">`; holiday slider/thumbs use the new files; solar `<video preload="none" poster=…>` with an IntersectionObserver that calls play() when visible.
- **#14** · all pages `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?...">` → `family=Barlow+Semi+Condensed:ital,wght@0,400;0,500;0,700;1,400&family=Barlow+Condensed:wght@500;600;700&display=swap`, or self-host woff2 under /assets/fonts/ with `<link rel="preload" as="font" type="font/woff2" crossorigin>` for Barlow Condensed 700 and Magneto.
- **#16** · all pages JSON-LD · one shared node: `{"@type":["LocalBusiness","HomeAndConstructionBusiness"],"@id":"https://goodguyswash.com/#business","name":"Good Guys Window Washing","url":"https://goodguyswash.com/","telephone":"+1-801-515-5588","image":"https://goodguyswash.com/assets/logo.png","address":{"@type":"PostalAddress","addressLocality":"Lehi","addressRegion":"UT","postalCode":"ZIP from Q3","addressCountry":"US"},"geo":{…from Q7},"openingHoursSpecification":[…from Q7],"sameAs":["https://www.instagram.com/goodguyswindowwash/","https://www.facebook.com/profile.php?id=61567287296885","https://maps.app.goo.gl/mk9BBK3YKBvJpU4bA"]}`; Service nodes keep `"provider":{"@id":"https://goodguyswash.com/#business"}`.
- **#17** · holiday.html `<title>` → "Christmas Light Installation in Salt Lake & Utah County | Good Guys"; 39 window-cleaning city pages `<meta name="description">` → template in #17; gallery.html, window-cleaning.html, window-cleaning-plans.html descriptions → longer versions; index.html `<h1>Window Washing<span class="h1-sub">in Salt Lake &amp; Utah County</span></h1>` with `.h1-sub{display:block;font-family:var(--font);font-size:.4em;letter-spacing:.06em}`.
- **#18** · index.html, holiday.html, 39 christmas pages: insert `</head>\n<body>` before `<div class="top">`; all 97 pages: `<div class="top">` → `<header class="top">` (and closing tag); 56 pages missing it: add `<a class="skip" href="#top">Skip to content</a>` as the first child of the header.
- **#19** · `.stars` → `<div class="stars" role="img" aria-label="5 stars">`; holiday.html style buttons: remove `aria-pressed` where `role="radio"`; gg5: add `<button class="gg5-pause" aria-pressed="false">Pause</button>` and stop the timer on `mouseenter`/`focusin`; form error `<p class="qerr">` → add `role="alert"` and `aria-describedby` on the fieldset; `#baSlider`, `#slider`, `#pvSlider`: set `aria-valuetext` on input ("50% after"); honeypot `<label>` → `aria-hidden="true"`; `a.brand` aria-label → "Good Guys Window Washing, home".
- **#20** · footer on all pages: `Text or call: <a href="tel:+18015155588">(801) 515-5588</a> · <a href="sms:+18015155588?&amp;body=…">Text us</a>`; closing CTA band: add `<a href="tel:+18015155588">or call</a>`.
- **#21** · nav dropdown "Soft washing" → "House washing" (link /house-washing) and add "Roof washing" (/roof-washing); home services grid card title "Soft washing" → "House & roof washing"; quote tile "House soft wash" → "House washing".
- **#22** · CSS `@media (max-width:480px){.hero .mascot{max-width:200px}.hero .sub{text-wrap:balance}.hero .eyebrow .brk{display:block}}` and wrap "Salt Lake & Utah County" in `<span class="brk">`.
- **#23** · `.nav` on `max-width:900px`: `mask-image:linear-gradient(90deg,#000 85%,transparent);padding-right:24px` or `display:none` with the hamburger menu as the only nav.
- **#24** · index.html `.hero{padding-top:72px}` always (drop the `.gg8-on` toggle); holiday.html `@keyframes sqBlade` → use `transform:translateX()` instead of `left`.
- **#25** · replace keyframes: `ctaPulse`/`popPulse` → scale/opacity on `::after` ring; `planGlow`/`planAura` → opacity on a pre-shadowed `::before`; `gg5Timer` → `transform:scaleX()` with `transform-origin:left`; `.plan-tiles .spark`, `.tile.hot::before` → `animation-iteration-count:3`; tokens `--ease:cubic-bezier(.2,.8,.3,1); --t-fast:150ms; --t-med:220ms; --t-slow:320ms` applied to every transition.
- **#27** · index.html quote dialog: move `#qAddr` field into step 4; wrap `#qRef` in `<details><summary>Were you referred?</summary>…</details>`; error `<p>` placed directly after each fieldset.
- **#28** · holiday.html + 39 christmas pages `#pvBusy`: add `<div class="pv-bar"><i></i></div>` (CSS `scaleX` animation, 20 s) and `<button type="button" id="pvCancel">Cancel</button>`; `PV_ERR.failed` → append " Your photo wasn't kept."
- **#29** · shared head: GA4 snippet with Wil's measurement ID (from Q9); keep existing `track()` calls.
- **#30** · good-guys-window-washing.vcf: `URL:https://goodguyswash.com`; `N:Good Guys Window Washing;;;;`.
- **#31** · extract shared CSS to assets/site.css?v=1, link it in all 97 pages; minify squeegee-game.js.
- **#32** · sitemap.xml: clean URLs + `<lastmod>`.
- **#33–#48** · as written in the findings (CSS-only or copy changes).

## 7. Draft privacy policy and terms (for Wil to review; not legal advice)

### Privacy policy (draft)

**Good Guys Window Washing — Privacy Policy.** Last updated: [date]. This policy explains what we collect on goodguyswash.com and how we use it. Questions: text or call (801) 515-5588 or email [Q4 email].

**What we collect.** When you ask for a quote, book holiday lights, play the squeegee game or use the "light up my home" preview, we collect what you type: your name, mobile number, email (optional), home address, what you'd like cleaned or lit, notes you add, and whether you agreed to texts. If you refer a neighbor, we collect the name you enter.

**Unfinished forms.** If you type your name and phone number into a quote form and leave before pressing Send, the form sends what you entered so we can follow up. If you did not tick the text-message box, we will not text you; we may call or email if you gave us an email.

**Home photos (light preview).** A photo you upload is sent to [AI service from Q2] to create a preview picture of your home with lights. We keep the photo and preview with your quote so we can design your display. If you add an email, we send you the preview. Do not upload photos of people.

**How it's used.** To send your quote (by text if you agreed, otherwise by call or email), schedule and do the work, answer questions, and keep records of jobs and payments. We do not sell your information. We do not share your phone number or text-message consent with anyone for their marketing.

**Who handles it for us.** Flyra (our scheduling and messaging system) stores your details and sends our texts and emails. Netlify hosts the site. Google provides the fonts the site uses and the reviews we display. [Google Analytics, if added: it records page views and button taps using a cookie.] [AI service from Q2] makes light previews.

**Visit information.** With each quote we save the page you came from, the page you landed on, and ad-click codes in the link you used (utm tags, gclid, fbclid) so we know which ads work. Your browser stores a small amount of data on your own device: your squeegee-game progress and prize, the referral name you entered, and a flag that a quote was started. You can clear it in your browser settings.

**Text messages.** By ticking the "Text me" box you agree to receive texts from Good Guys Window Washing about your quote, appointment reminders, service updates and occasional offers. Message frequency varies. Message and data rates may apply. Reply STOP at any time to stop, or HELP for help. Consent is not required to buy anything; you can always get a quote by calling instead.

**Your choices.** Text or email us to see, correct or delete what we hold about you. We keep job records as long as we need them for taxes and warranties.

**Children.** The site is for adults arranging home services.

**Changes.** We'll post updates here with a new date.

### Terms of service (draft)

**Good Guys Window Washing — Terms.** Last updated: [date].

1. **Quotes.** Quotes are free and based on what you tell us (window count, stories, add-ons) and, for holiday lights, a look at your home. The final price is confirmed before work starts. Exterior window cleaning starts at $200 per visit, including the first visit of a plan.
2. **Plans.** Bi-annual, Quarterly and Monthly plans are standing schedules; we book visits for you and text or call the day before. Plan discounts apply to window cleaning. You can pause or cancel a plan by texting us before the next visit is booked.
3. **7-Day Rain Guarantee.** For Quarterly and Monthly plan members only: if it rains within 7 days of your exterior wash, we re-wash the outside of your windows free.
4. **Referrals.** When a neighbor you refer completes their first wash, you get $50 off your next window wash. One $50 credit per completed first wash, no limit on referrals, and a wash never goes below $200. Credits apply to window washing by Good Guys.
5. **Holiday lighting.** Installation price covers design, hanging, repairs of our lights during the season, takedown after the holidays and storage until next season. Seasonal offers (such as 15% off installation or 50% off a window wash) apply only to bookings made within the dates shown on the site at booking time.
6. **Squeegee game prizes.** One play per day, one prize per device. A prize is applied to one quote within 30 days and can't be exchanged for cash.
7. **Payment.** Cash, card, Venmo, check or Zelle. We invoice after each visit; commercial accounts may be invoiced on terms we agree in writing.
8. **Access and safety.** Please tell us about gate codes, pets and fragile items. We may postpone work for lightning, high wind, ice or unsafe access.
9. **Photos.** We may take before-and-after photos of the work. We will ask before using a photo that shows your home's address or your family on the site.
10. **Problems.** If something isn't right, text us within 7 days and we'll come back and fix it. Our responsibility is limited to redoing the work or refunding the amount paid for it.
11. **Contact.** Good Guys Window Washing, [legal name/entity from Q3], Lehi, Utah. (801) 515-5588.

## 8. Text-message consent wording (drafts; not legal advice)

Quote forms (home, holiday, Christmas pages), unchecked by default:
"Text me my quote and updates from Good Guys Window Washing at this number. Message frequency varies. Msg & data rates may apply. Reply STOP to opt out, HELP for help. Consent isn't required to get a quote. Privacy policy."

Light preview form: "Text me about my lights preview and quote. Message frequency varies. Msg & data rates may apply. Reply STOP to opt out. Privacy policy."

Game prize form (unchecked): "Text me my prize and quote at this number. Msg & data rates may apply. Reply STOP to opt out. Privacy policy."

Under the Send button on each form (small text): "No text consent? No problem, we'll call or email your quote instead."

Rule for unfinished forms: text only when `sms_consent` = yes; otherwise notify Wil to call.

## 9. Seasonal plan for the holiday pages

**Nov 16 → end of season (after the 15% deal ends).** The script already hides the deal blocks. Replace, don't blank: hero pill becomes "Now booking · Limited December dates" (data-deal-after), and "Plus 50% off a window wash with every install" stays if Wil keeps it (Q11). Home holiday section eyebrow "Now booking · Pre-season" → "Now booking · This season". Lights menu link unchanged. /lights-quote meta: title "Holiday Lights Quote | Good Guys Window Washing"; description "Free consultation: we measure your home, then text you an exact price. 50% off a window wash with your install. Salt Lake & Utah County."; og:title "Holiday Lights: Free Consultation"; og:image without a date. llms-full.txt: delete the two deadline lines. FAQ "When do you hang the lights?" answer drops the deadline sentence (already in data-deal).

**January → September (off season).** Keep all 40 pages live (they rank; deleting loses it). Hero: "Lights are down and stored. Book 2027 early and get first pick of dates." Button: "Reserve my spot for 2027" (opens the same form with `season=2027`). Hide the AI preview section or label it "Try a look for next year". Home holiday band shrinks to one line: "Holiday lights: book 2027 early" linking to /holiday. Add a short "What happens after the holidays" block: takedown, storage, re-hang next year.

**September → Nov 15.** Flip back to pre-season copy with the new year's deal and dates, update llms files and /lights-quote the same day.

## 10. Competitor notes (search snippets only; sites couldn't be opened from here)

From search listings: Squeegee Clean Crew (American Fork) shows a 5.0 rating from 20 Google reviews in its listing; Royal Slopes advertises "licensed and insured" (a claim Good Guys must not make until insurance is active); Cascade and Window Genie push "free estimate" and online request forms; Window Cleaning Utah County in Lehi lists Mon–Sat 8–7 hours. Ideas worth borrowing, not copying: (1) show the real Google rating and count next to the reviews once the API key is in; (2) an "instant estimate" expectation is already Wil's edge ("quote in minutes by text"), so say it in the title tag and hero; (3) a short "what a visit looks like" video on the home page (the solar video shows Wil does this well); (4) a service-area page per county with a map and drive-time promise; (5) a "book next year's lights" list for the off season.

## 11. One more polish pass (what each reviewer would still complain about)

- Picky designer: the mobile sticky bar's buttons use a 3px block shadow while every other button uses 4px (pick one); the ghost button's hover only changes colour on dark bands while the red one lifts (give both the same lift); the "Up to $150 off" price block breaks "UP / TO" onto two short lines beside the number; the game bubble's monospace text is the only place body copy isn't Barlow (fine inside the game, but the bubble sits on the main page).
- Local-SEO expert: no `address` in the business schema, no Facebook in sameAs, no per-page `og:url`, 78 near-duplicate city pages, home H1 without a location, no NAP line in the footer (name, Lehi UT, phone, hours together).
- Screen-reader user: "Leave this empty" announced in every form; star ratings silent; slideshow moves on its own; 56 pages with no skip link; map with 39 unlabeled link targets.
- Homeowner on a phone in the sun: the tan-on-cream "ADD-ON" badges and the tan section rules are the lowest-contrast elements (no WCAG failures found by the automated contrast scan, but they are faint outdoors; a touch more weight helps); first screen is a logo, the quote button is at the fold; nav strip looks cut off; the phone number is too small to tap in the header.
