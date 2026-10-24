# AI starter kits: plan

**Who does what**
- **Claude** is in charge of the website, the quiz, the kits and the code.
- **Zucc** helps with research.
- **Wil** oversees and has the final say. His decisions go through the "Questions for Wil" tab.

**Faceless.** The brand stands behind every kit, and Wil's name appears nowhere.

**Goal (Wil, Oct 24):** the first $100 earned within 30 days after the first kit is live and Stripe can take payment.

**Direction (Wil, via Zucc, Oct 24):**
- About 4 kits for 4 scenarios under the AI-automated-business umbrella, some leaning toward physical businesses, automation-first throughout.
- Stacks: Claude plus Meta AI tools.
- "Duet-aware": to be defined.
- No Grokbot kit until there's real data on it.

**Status (Oct 23, 2026):** planning only. Nothing goes live until Wil says go. That covers the website, checkout, prices and refund mechanics.

---

## 1. The offer: pay up front, finish, get it all back

This is modeled on the challenge offer Alex Hormozi used to launch gym clients (Gym Launch).

1. The quiz matches the buyer to **one kit** and sets **one build goal** with a **deadline**.
2. The buyer pays the full price up front.
3. **Hit the goal by the deadline and show the proof: full refund.**
4. **Miss it: we keep the payment, and they get 50% off the next kit,** the one that covers what stopped them.

Why it works:
- The money in the pot is the motivation.
- Finishers get their goal and their money back, and they become customers for life.
- Non-finishers still got somewhere, and their next step is half price.

### Rules the offer has to follow

- **The goal is something built, never money earned.** For example: "your follow-up automation answers a test lead from start to finish". Never "make $X". An income goal would be an income claim, which breaks the brand's guardrails. It also can't be judged fairly, and it depends on luck.
- **Every goal is provable.** Each kit has a checklist and a proof step, such as screenshots or a short screen recording. The proof decides, not opinions.
- **The deadline is fixed at purchase** and set per kit, for example 30 days.
- **All terms are shown before payment:**
  - the price
  - the goal
  - the deadline
  - what counts as proof
  - how to claim the refund
  - what happens on a miss

  Consent comes before the charge, and claiming is one obvious step. These are Wil's funnel rules.
- **No "risk-free" wording,** because there are conditions.
- **The final terms get checked by someone qualified before launch.** Money-back guarantees fall under consumer-protection rules.

### The math to settle before setting a price

Every finisher gets a full refund, so **the better the kits work, the less the up-front price earns.** The money has to come from:

| Source | Per buyer |
|---|---|
| Buyers who miss the goal | price × share who miss |
| Next kit at 50% off | (next kit price ÷ 2) × share who buy it |
| AI-tool referral credits | credit per sign-up through our links |
| Later: coaching or a community | Wil's call, down the line |

Costs:
- support time
- processing fees on refunds (most payment processors keep their fee when you refund, so check ours)
- the tools we run

> Per buyer ≈ price × (1 − finish rate) + (next kit price ÷ 2) × next-kit rate + referral credit − fees − support

If that comes out thin at a realistic finish rate, there are three levers: raise the price, give finishers a choice of cash back or a larger store credit, or both.

**Option for Wil:** finishers choose between their money back and 150% of it as store credit. Many winners would stay in the ecosystem, and nobody loses the cash option.

**No numbers yet.** Prices, the finish rate and the credit size come from real quiz data and a small first batch, not from guesses.

---

## 2. The quiz: a branching flowchart, in the style of the Hims & Hers quiz

Its job is to send each person to one kit, set their goal, and show them the offer.

**Draft branches**

1. **What do you want to build?**
   - YouTube channel
   - short-form content account
   - all-in-one: socials, website and a product
   - online store or dropshipping
   - paid ads
   - AI help for a business you already run
2. **Where are you now?** Nothing yet, started but stalled, or running and want it automated.
3. **Which AI do you use?** ChatGPT, Claude, Gemini, or none. If none, we recommend one with our referral link, disclosed.
4. **Hours per week you can give it.**
5. **Monthly budget for tools.**
6. **Biggest blocker:** don't know where to start, start but don't finish, the tech setup, or no time.

**The result screen shows, in order:**
1. the kit
2. the goal in one sentence, with its deadline
3. the setup for their AI
4. the price and the guarantee terms

Checkout comes only after all of that.

**Rules**
- Quiz answers never go to ad platforms.
- No medical or ADHD questions. The brand doesn't diagnose anyone.
- Every question earns its place by changing the result.

**Build pattern**, from Zucc's breakdown in `research/hims-quiz-funnel-breakdown.md`:
- **Archetypes first.** Draft buyer types, refined later from real comments, DMs and buyer data, saved as `archetypes.md`.
- **Question count:** 6–8 questions. Two shared openers, then branches per type built from that type's pain points. Include 2 open questions, and word each question the way that type talks.
- **Classify after every answer** with a Claude call, not a third-party vendor, so prospect data stays with us. Switch to a type's branch once it is clearly ahead.
- **One result page per type.**
- **Log every answer under an anonymous ID** to see which questions lose people.
- **Price and exact terms shown before submit.**

Note: Zucc's breakdown cites a lawsuit against Hims & Hers over billing, cancellation and data sharing. Claude hasn't verified the case details. Its lessons are already in our rules either way.

---

## 3. What's in every kit

- **The goal,** with its checklist and proof steps.
- **A copy-paste setup for the buyer's AI** (Claude, ChatGPT or Gemini): prompts, project or agent instructions, and small scripts where a tool supports them. Claude writes and tests these on each platform.
- **Short how-to guides** in text and screenshots, faceless.
- **The next kit** it points to if they miss the goal.
- **The tool list,** with our referral links disclosed.

## 4. Referral links

- Where a tool runs a referral or affiliate program, the link goes to Wil's account. Which tools have programs is **still to verify**: Zucc researches, and Claude checks each program's terms.
- Disclose it on the site and in the kit: "We may get credit if you sign up through our link."
- Recommend the tool that fits the buyer. Add a link only if that tool has a program. A referral never decides the recommendation.

## 5. Research flow

1. Zucc collects research: creators' free information, competitor kits, quiz examples, tools and their referral programs.
2. It goes into `kits/IDEAS.md`, or on PR #1, always **with the source link and date**.
3. Claude fact-checks every claim before a kit, a page or a post uses it. Anything unverified stays marked as unverified.

## 6. Later, not now

- Website, checkout, prices and refund mechanics.
- Maybe a coaching program or community with a face attached, which is Wil's call down the line.
