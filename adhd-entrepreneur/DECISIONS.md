# ADHD Entrepreneur: decisions log

Locked decisions only, newest first. Claude and Zucc build on these and don't reopen them unless Wil does. Anything still open is listed at the bottom.

## Oct 27, 2026: the private offer after a missed goal (Wil, on the Questions tab)

- **50% off a continuation of the same kit, with a fresh deadline** (`q-miss-offer`, option a). It goes only in the follow-up email after a miss, never on the site, quiz or policies. Logged Oct 30, when the check-in found the pick.

## Oct 29, 2026 (evening): calendar rewrites, Days 11–27 (Wil)

- **8 calendar lines rewritten to the new quote bar,** approved as a set ("approve all"):
  - Days 11, 15, 17, 18, 20, 23, 26 and 27.
  - Days 26 and 27 also get new questions.
  - The old wording is kept as `was` in `content/calendar-30.json`.
- **The Day 15 founder line is settled:** "Two weeks of posting to almost nobody. That's what starting looks like. I'm not stopping." This closes the Nov 4 pre-post item.
- **The other 14 lines stay as written:** Days 9, 10, 12, 13, 14, 16, 19, 21, 22, 24, 25, 28, 29 and 30. Day 8 had already posted.

## Oct 29, 2026: scope of this chat and PR #1 (Wil)

- **ADHD Entrepreneur only.** The brand-launch chat and PR #1 are for the ADHD Entrepreneur brand alone. Wil: "this chat isn't for anything good guys related … don't ask me anything about good guys on this chat."
  - Claude doesn't raise, relay or ask about Wil's other business here.
  - Zucc sends those topics to their own chats, not to PR #1.

## Oct 28, 2026 (evening): posting cadence and quote bar (Wil, relayed by Zucc)

- **More posts a day, starting Day 8 (Thu Oct 29).** Wil proposed 2–3 a day in a morning, afternoon and evening window. Claude agreed with two conditions (Wil can overrule either):
  - The **morning reel** (calendar hero), the **afternoon collage** and an **evening second reel** make 3 posts a day on IG, and 2 reels a day on YouTube and Threads.
  - **TikTok's second reel waits** until the 0-play cause is found. More posts don't fix distribution.
  - Times vary inside the windows. X stays Wil's phone post.
- **Extra lines come from Claude,** so the brand keeps one voice. Zucc peer-edits them. Days 8–14 are in `content/reel2-week2.md`. Days 15–30 follow the Thursday Oct 29 review.
- **Quote bar raised (Wil):** one idea, blunt, said to "you", concrete, zero filler, useful in a Gen Z starter's day (starting, overthinking, building next to a 9-to-5). No slang or gimmicks. Gen Z is the expected starter-kit buyer.
  - **The brand rules still hold:** original wording, never naming or paraphrasing the people the bar is modeled on, and no income or medical claims.
- **Music:** in-app platform libraries only. No commercial songs baked into video files. "Louise" drew a YouTube copyright claim on Day 7.

## Oct 27, 2026: TikTok posting route (Wil)

- **No TikTok posts from the phone app.** Wil: "I don't want to post anything from the actual phone app for TikTok." TikTok stays web-posted by Zucc.
  - The phone-app test Claude proposed for the Thursday Oct 29 review is dropped.
  - The 0-play problem gets worked on with web-side checks only: TikTok Studio on the web, account status, post settings and captions.

## Oct 27, 2026: site changes after Wil took the quiz

- **The miss discount is private.** No page on the site, quiz or policies mentions a discount for missing the goal. After a miss, the buyer gets a follow-up email with a private offer: a discount on the next kit, or on a continuation of the same kit.
  - The size is open: 50% or 75% (`q-miss-offer`).
  - The draft is in `kits/emails/miss-followup.md`.
  - The site still says, before payment, that a miss means no refund and the kit stays theirs. That's a purchase term, so it has to be shown.
- **Buttons:** the RGB split is softer, a slightly out-of-focus liquid-glass glow. Pressing a button brings it into focus as white glass.
- **Quiz:**
  - Each answer is its own color of glass, with a simple icon.
  - Questions are shorter: 6 taps (7 for "Not sure yet", 5 for the custom path).
  - The typed question and the heads-up screen are gone.
- **Kits:**
  - Icons on everything kit-related.
  - A catalog page (`/kits`) sorted by category: Service & trades, Stores & products, Content & audience, Digital products, Custom.

## Oct 26, 2026: website, button, legal name, kits (Wil, on the Questions tab)

- **Website is live on Netlify** at https://adhd-entrepreneur-starter-kit-store.netlify.app (project `adhd-entrepreneur-starter-kit-store`). Nothing is for sale on it.
- **Design direction:**
  - midnight dark mode
  - a simple color split and a retro-futuristic feel, with ARC Raiders as the reference but nothing copied
  - iPhone-style liquid glass, kept clean
  - an easy, Hims-style quiz
- **Buttons (`q-accent`, Wil's own call):** the button carries the whole RGB split as liquid-glass layers. Pressing it lines the layers up into white glass. This is built. (Softened on Oct 27.)
- **Legal name (`q-legal`):** "ADHD Entrepreneur" only, registered as a DBA or LLC. Wil files it. The policies name the registered entity once it's filed.
- **Kits (`q-kits`):**
  - Build the 4: local service business, product store, content brand, digital product.
  - More premade kits get added later, from Zucc's research and Claude's ideas.
  - Custom-built kits exist alongside them.
  - The quiz points people to the premade kit that fits, and offers a custom path when none fits.

## Oct 24, 2026 (morning): relayed by Zucc from Wil

- **Instagram goes to a Creator account** (not Business, and not staying personal), switched in the app with the category Entrepreneur. Zucc checks the music library right after. From then on, the evening numbers come from Insights.
- **Goal timer.** The 30-day first-$100 clock starts only once a kit is built, live **and** Stripe is connected so buyers can pay.
- **Website moved up, for Stripe activation.** Stripe setup is paused at the website-URL step. Claude builds a simple brand site:
  - a home page and a policies page (refund and guarantee, terms, privacy), with no funnel yet
  - first on a preview URL, moving to the domain later
  - going public only after Wil approves where it's hosted
- **Design reference.** The "AuthKit, frosted glass cathedral at midnight" system, adapted with the ADHD Entrepreneur wordmark and none of WorkOS's branding.
  - The violet accent conflicts with the black-and-white brand lock, so it's a question for Wil (`q-accent`).
  - Higgsfield is ruled out.
  - Refero Styles is the candidate inspiration library, awaiting Wil's confirmation.
- **Kits direction (next week).**
  - About 4 kits for 4 scenarios under the AI-automated-business umbrella, some leaning toward physical businesses, automation-first throughout.
  - Stacks are Claude plus Meta AI tools (Meta AI, not Meta ads or social).
  - "Duet-aware" is still to be defined.
  - No Grokbot kit until there's real data on it.
- **Comment-to-quiz path approved.** Once the quiz is live, posts end with "comment QUIZ" and each person who asks gets a reply by hand with the link. There's no automation. Nov 5 (Day 15) is only the calendar's link date. Zucc corrected his own "hard deadline" wording on Oct 24, and Wil hasn't set a quiz deadline.
- **"Duet-aware" kits.** Duet is Claude's new product, announced Oct 21 as a research preview. Wil is on the waitlist. What "Duet-aware" means for the kits is still Wil's to define.

## Oct 24, 2026: first-$100 goal moved (Wil, relayed by Zucc on PR #1)

- **The first-$100 goal now runs from the first kit's launch.** The target is the first $100 earned within 30 days after the first starter kit goes on sale, with the exact date set on launch day.
- **Nov 20 no longer has a goal attached.** The posting calendar is unchanged: Day 30 is still Fri Nov 20.
- **Until a kit is on sale,** the account is judged by the weekly scorecard (`analytics/SCORECARD.md`).

## Oct 23, 2026 (evening): starter kits and website (Wil)

- **Claude is in charge** of the website, the tools and the AI starter kits. **Zucc helps** with research. **Wil oversees** and has the final say.
- **Nothing goes up yet.** The website, link hub, quiz and checkout are on hold until Wil says go. Calendar captions carry no links or "Quiz in bio" lines.
- **Offer direction** (details in `kits/PLAN.md`):
  - It's a challenge offer in the style of Gym Launch: the buyer pays up front.
  - Hit the agreed build goal by the deadline and get a full refund.
  - Miss it, and we keep the payment and give them 50% off the next kit that covers what stopped them.
  - A smart branching quiz, in the style of the Hims & Hers quiz, picks the kit and sets the goal.
- **Kit ideas by niche** live in `kits/IDEAS.md`. Zucc feeds research, and Claude fact-checks it.
- **Referral links** go to Wil's accounts where a tool offers a program, always disclosed.
- **Faceless.** Maybe a coaching program or community with a face later.
- **The 14-day refund question is withdrawn.** The challenge model replaces it.

## Oct 23, 2026: how Wil wants Zucc and Claude to work (Wil's own words, given to Claude)

- **Formats.**
  - **Reel:** one video goes to Instagram, TikTok and YouTube Shorts.
  - **X:** the line as plain text. Wil posts it from his phone for at least the first week, so the account doesn't get flagged; Zucc has no X access yet.
  - **Collage:** Instagram and TikTok also get a daily 6-slide swipe collage with music. It adds variety and shareability: a quote someone likes more than the others gets saved, shared or posted to their story.
- **Zucc and Claude write the lines together** and agree on what gets made.
  - **Before posting:** Zucc checks with Claude for a peer edit.
  - **After posting:** they review the analytics, what to improve, and Zucc's research.
- **Wil has the final say.**
  - Anything that needs Wil goes to him through the Zucc chat.
  - When Claude and Zucc disagree, or need his call, the question goes in the **"Questions for Wil" tab** on Claude's calendar page. The page shows Claude's option, Zucc's option, and an in-between option they both accept. Wil picks one or writes his own.
  - The page is private to Wil, so Zucc posts his vote on PR #1 as `[Zucc] vote: <question>: <option> because <one line>`. Claude adds it to the page and passes Wil's decision back on PR #1.

## Oct 23, 2026

- **Faceless brand.** No face on any account, card, video or site page. Founder posts are written in the first person, without a face.
- **30-day calendar approved.** All 15 new lines are approved as written (`content/calendar-30.md`).
- **Color split rule.** The bold RGB split appears only on the logo (the whole A, echo strokes included) and on the word "ADHD" in the banner and X header. Quote text on cards stays plain black on white, or plain white on black for the dark card.
- **Brand look.** The black/white base plus that split is the official look.
- **Profile picture.** Full-bleed avatar (A) with the bold split on the whole A, built from `brand/source/logo-final-perfect.jpg`. The files are in `brand/upload/`. Zucc swapped them in. Claude checked the public YouTube and TikTok profiles against the files. Instagram and X can't be checked without logging in.
- **Banners.** The bold "ADHD" split goes on both the YouTube banner and the X header (`brand/upload/`).
- **Zucc ↔ Claude channel.** Use comments on PR #1. Start each one with `[Zucc] question / update / request`. When Zucc drops files on the branch, he also leaves a comment pointing to them.

## Open

- **Website.** Live at https://adhd-entrepreneur-starter-kit-store.netlify.app. Before anything goes on sale (details in `site/README.md`):
  - register the DBA or LLC
  - confirm the draft policy terms
  - set prices, deadlines and proof per kit
  - have someone qualified read the policies
  - optionally, buy the domain
- **Starter kits (checked Fri Oct 30):**
  - the price per kit
  - the deadline length per kit
  - cash back vs 150% store credit for finishers
  - which AI tools run referral programs (Zucc researching)
  - Meta AI's real capabilities per kit (Zucc researching)
  - Kit 01's timed build goal (proposed: "a test lead gets a reply within 5 minutes")
  - GoHighLevel vs Claude-native for Kit 01
- **Content process (Wil's call):**
  - collages: Zucc owns them and Claude checks after posting, or Claude renders the images
  - a weekly Instagram Insights screenshot
  - follow-unfollow vs the Oct 26 follow experiment
- **Domain.** `adhdentrepreneurhq.com` was still unregistered on Oct 30 (.com registry lookup, RDAP 404). It isn't held until someone registers it.
- **From Zucc.**
  - his daily analytics log columns, for the scorecard
  - a screenshot of the quote-card template, for the dark and story variants
  - his exact Instagram tagline
