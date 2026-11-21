# Weekly review: Week 1 (Days 1–7, Thu Oct 22 – Wed Oct 28)

Run by Claude on Thu Oct 29 from `daily.csv`, following `SCORECARD.md`. Every number is a same-day read: the 35-hour re-reads haven't happened yet. Blank means it wasn't read.

## Problems first (the scorecard says fix these before reading anything else)

1. **TikTok shows 0 plays on 10 of 12 posts.** Only Day 1 has a real number: 55 plays in TikTok Studio. Every 0 since then is a **public-page** read, and the scorecard warns that public pages lag on TikTok. Fix the measurement before calling it a distribution problem: read each post in **TikTok Studio on the web** at about 35 hours. If Studio also says 0, it's real, and the web-side checks follow (account status, content-check results).
2. **The headline number couldn't be read anywhere this week.** Saves and shares aren't shown on public pages, and Instagram Insights isn't available on the web.
   - **YouTube:** Studio on the web shows shares per Short, so it's readable from next week.
   - **Instagram:** Insights is phone-only. The cheapest fix is Wil sending one weekly screenshot of each post's Insights, about 5 minutes. That's Wil's call.
3. **The collage drifted from the agreed lines 4 days running (Days 4–7).** The build read a stale local file. From Day 8, the build fetches from the branch or stops.

## Platform table

| Platform | Posts | Median views | Median SSR | Best post | Real comments | Followers start → end |
|---|---|---|---|---|---|---|
| YouTube Shorts | 7 | 49 (6 read) | unread | Day 2: 301 views, 11 likes | 0 | 0 → 1 sub |
| Instagram | 12 (7 reels, 5 collages) | unread | unread | Days 2–3 reels: 3 likes | 0 (3 spam on collages) | 0 → 4 |
| TikTok | 12 (7 reels, 5 collages) | 0 (public reads) | unread | Day 1: 55 plays (Studio) | 0 | 0 → 0 |
| Threads | 3 (Days 5–7) | 3 | unread | Day 6: 14 views | 0 | 0 → 0 |
| X | Wil's phone posts | unread | unread | unread | unread | 3 → 4 |

Profile visits were not read on any platform.

**YouTube views by day:** 5, 301, 21, unread, 2, 130, 77. Some reads came 4 hours after posting and some 10, so they aren't strictly comparable.

## By content type

**Not measurable this week.** The scorecard ranks types by SSR, and SSR was unread everywhere.

- **Reel vs collage:** neither drew real engagement. Collage comments were all spam.
- **The calendar's types (reminders, tips, AI, founder):** one post each, too few to compare.

## One sentence

YouTube Shorts is the only place with measured reach (median 49 same-day views). Instagram followers went 0 → 4 on the days with outbound comments. TikTok's 0s may be a reading problem, not a reach problem. Nothing this week shows which content works, because saves and shares were never read.

## One experiment for Week 2 (Days 8–14)

**Evening Reel 2 (new quote bar: concrete, blunt, to "you") vs morning Reel 1 (calendar hero), compared on YouTube.**
- Measure views and shares at the 35-hour read in YouTube Studio, logged as `reel1` / `reel2` in the format column.
- This is the one change for the week, since the cadence change came with it.
- It also tests Zucc's "concrete hook beats abstract" idea, without touching Wil's approved hero lines.
- **Caveat:** the post time differs as well, so a gap could be the slot, not the wording. If Reel 2 wins clearly, the follow-up test is a concrete line in the morning slot.

## One thing to stop

**Follow-unfollow.** The follow log schedules unfollows (for example "unfollow-due Nov 14"), and the scorecard's never-list bans follow-unfollow.
- Follow only accounts we'd keep following, and cancel the scheduled unfollows.
- A plain unfollow of an account that's become irrelevant is fine. Cycling is not.

## Next review: Thu Nov 5 (Days 8–14)

Before then:
- 35-hour re-reads from Studio for YouTube and TikTok, logged in `daily.csv`.
- Wil's call on the weekly Instagram Insights screenshot.
- Slot labels on every row.

## Update: later reads (Thu Oct 29, ~01:05 MDT, public pages)

These reads came after the review above. They correct two things and change nothing in the experiment or the stop.

- **Threads had 4 posts, not 3.** A Day 4 post (390 views, 5 likes) was never logged. Threads now reads: 4 posts, median views 8.5 (390, 2, 14, 3), best post Day 4.
- **YouTube, all 7 Shorts read:** 101, 390, 27, 14, 10, 161, 84. Median 84. Read ages vary (15 hours to about 6 days), so treat it as rough.
- **First on-topic Instagram comment:** a reply to the Day 6 collage's "start messy or wait" vote.
- **A hunch, not a finding:** the two best posts of the week (YouTube Day 2, Threads Day 4) are both "finish what you started" lines. Too few posts to act on; watch it in Week 2.
