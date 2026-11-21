# Winter ark: niche account network (Claude's feedback and workflow)

**Status:** design only (Nov 4, 2026). Nothing gets created from this file. Each creation step waits for Wil's yes.
**Source:** Wil's plan, relayed by Zucc on PR #1 (Nov 4): about 20 niche accounts that send people to the starter kits.

## The short answer

**Right instinct, wrong size and wrong order.** Niche accounts beat one broad account. But 20 accounts now has three problems:
1. Nothing is for sale yet.
2. The one-account pipeline still breaks every day (wrong lines, baked-in songs, no evening reel).
3. Running 20 accounts honestly would take more hours than a winter with a newborn allows.

**Recommendation: 4 accounts, one per catalog category, openly branded as part of ADHD Entrepreneur, opened after the first kit and checkout ship.** Add more only when one of the four proves itself.

## Answers to Zucc's flags

### 1. Platform risk: does "different content plus different emails" make it safe?

**No, and hiding the link is the risky part.**
- Meta's Inauthentic Behavior policy targets networks of accounts that mislead people about who runs them, or that fake popularity (fake distribution, audience building or engagement). See the [Meta Transparency Center](https://transparency.meta.com/policies/community-standards/inauthentic-behavior).
- Meta links accounts by device, network and behavior, not just email. Separate emails don't hide a network. Trying to look unlinked is exactly the pattern the policy describes.
- **The safe version is the opposite: openly linked accounts.** Each bio says "Part of ADHD Entrepreneur". All are managed from the same Accounts Center, post original content, and never like, comment on or share each other's posts to boost them. Brands run sub-accounts this way all the time.
- **If a satellite gets flagged:** a network judged inauthentic can be actioned as a whole, and that could include the main account. Honest, branded accounts with original posts and no fake engagement don't fit that pattern.
- **Account creation:** Instagram's terms bar creating accounts "in an automated way" without permission ([Instagram help](https://help.instagram.com/581066165581870)). **Wil creates each account himself, by hand in the app.** Zucc doesn't create them.

### 2. Are iCloud emails "more legit"?

There's no evidence that Meta trusts an email domain more. Any real email Wil controls is fine. The email isn't what keeps accounts safe; honest behavior is.

### 3. FTC disclosure for 20 accounts promoting the same kits

- If an account looks like an independent creator recommending "a great kit" that we sell, that's a hidden material connection, so it's deceptive.
- The FTC's 2024 rule on reviews and testimonials also covers undisclosed insider endorsements and fake social proof, such as bought or bot followers and views ([summary, Locke Lord](https://lockelord.com/newsandevents/publications/2024/08/new-ftc-rule-consumer-reviews-and-testimonials)).
- **Rules for every account:**
  - The bio names the brand.
  - Kit mentions say "our kit".
  - No account reviews or vouches for another account's kit as if it were independent.
  - No cross-engagement between our accounts.
  - No fake testimonials, ever.

### 4. Workload reality check

- The one account today gets 3 posts a day plus 12–13 outbound comments a day, and outbound comments are the only proven follower driver so far.
- **20 accounts at even 1 post plus 10 comments each would be 20 posts and 200 comments a day.** That can't be done honestly by hand, and automating it is the spam pattern platforms ban.
- **4 accounts at 1 post plus 5 niche comments each is 4 posts and 20 comments a day.** That fits Zucc's runs.
- Wil's time stays at approvals only, about 10–15 minutes a day with no evening work. X and Stories stay on the main account only, so the phone steps don't multiply.

## The workflow (with gates)

### Phase 0: ship the product first (now to early December)

Gate: these must be true before any new account exists.
- Kit 01 is built and tested, with a working checkout (Stripe connected) and the policies reviewed.
- "ADHD Entrepreneur" is filed as a DBA or LLC.
- The domain is bought.
- The repo is private.
- **The current pipeline runs clean for 7 days in a row:**
  - the right lines (the run reads the branch)
  - no baked-in songs
  - the evening reel live

Why this order: distribution with nothing to sell only builds followers, and multiplying a broken pipeline multiplies the errors.

### Phase 1: setup (about one week, once Phase 0 passes)

- **4 accounts, one per catalog category:**
  - Service & trades
  - Stores & products
  - Content & audience
  - Digital products

  Each one points at that category's kit.
- **Names:** "ADHD Entrepreneur · Trades" and so on (handles to pick). The bio reads "Part of ADHD Entrepreneur", in the same black-and-white split style.
- **Platforms:** Instagram and Threads first, since Threads has shown the best reach. TikTok waits until its 0-play problem is solved. YouTube waits.
- **Who:** Wil creates each account by hand in the app (about an hour total). Claude writes each account's positioning: who it's for, 3 themes, and a 30-line starter bank.

### Phase 2: content engine

- **Posting:** each account posts **1 a day**, in that niche's real situations. For trades, that's quotes, missed calls and reviews. It's not a reworded copy of the main account.
- **Lines:** Claude writes from a bank for each niche, with original wording and no income claims. Zucc posts them, with the same peer edit as now.
- **Outbound:** about 5 genuine comments a day in that niche's own community, never on our other accounts.
- **Scoring:** a weekly row per account in the scorecard.
- **Stop rule:** an account with no follower growth after 30 days gets paused, not pushed.

### Phase 3: funnel (only after Wil says links can go live)

- One CTA per surface: the bio link goes to the quiz, starting in that account's category (Claude can build `quiz.html?start=service`).
- Or "comment QUIZ" with the link sent by hand. Never both in one caption.
- No automated DMs.

### Phase 4: website live

- The domain is connected, the Stripe checkout is on each kit's page, and the catalog category pages are the landing pages for each account.
- **Expand only on data:** a category account that grows for 2 weeks running can get a second, sharper sub-niche account. The total is capped at what the pipeline can run cleanly.

## What this means for Wil now

Nothing new to do for the fleet until Phase 0 is done. The Phase 0 items already on his list are what unlock it:
- the run instructions
- the repo going private
- prices and deadlines
- the DBA or LLC
