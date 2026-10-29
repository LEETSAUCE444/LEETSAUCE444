
# Fact-checked report: open-source "hub" tools for Miyoo Mini Plus, Retroid Pocket 3/3+ and Galaxy S24, and legal ways to get games

Re-verified 2026-10-29 against live pages, git tag listings (`git ls-remote`), raw repo files and Google Play listing HTML. Anything I could not confirm is marked **UNVERIFIED**. This report names no site that distributes commercial ROMs, ISOs or BIOS files.

---

## 0. The plan for Wil in plain words

1. **Install Obtainium on the Retroid and the phone.** It installs emulators from their official release pages and checks for updates.
2. **Pick one "front door" app (a frontend)** so all your games show up in one menu with box art. ES-DE is paid on Android. Daijishō is free, but its developer says he is taking a break. Beacon costs $2.99. The Miyoo already has its own frontend, Onion.
3. **Sync in-game saves, not save states.** Save states can break between core versions. Use the same emulator core on every device.
4. **Get box art** with each frontend's scraper and a free ScreenScraper account.
5. **Get games legally.** Dump the carts and discs you own (section 5) or play free homebrew. **There is no legal all-in-one ROM pack.**

**Device notes:**
- **Galaxy S24:** there is no "S24 Pro". Check *Settings → About phone* for S24, S24+ or S24 Ultra. Reports say all three use Snapdragon 8 Gen 3 for Galaxy in the US and Canada. Outside North America, the S24 and S24+ use Exynos 2400, while the Ultra uses Snapdragon everywhere. These come from press reports; I did not check Samsung's own spec sheet. (https://www.tomsguide.com/news/samsung-galaxy-s24s-performance-could-vary-by-region-unless-you-go-ultra , https://androidauthority.com/samsung-galaxy-s24-snapdragon-vs-exynos-countries-3402659)
- **Retroid Pocket 3 vs 3+:** the 3+ has a Unisoc T618 with 4 GB RAM and 128 GB storage. The original RP3 has a Unisoc T310 with 2 or 3 GB RAM. Liliputing's comparison table lists Android 11 in one row shared by both models. (https://liliputing.com/retroid-pocket-3-is-a-149-handheld-game-console-with-a-unisoc-t618-processor/) The official goretroid.com product page returned 404 today, so I could not confirm these specs from the maker.
- **Wii on the Retroid:** I verified no source on how well Wii games run on the T618 or T310, so that is **UNVERIFIED**. Dolphin's Android build needs 64-bit Android (section 1).

---

## 1. Obtainium: install and update emulators from the source

- **What it is:** a free Android app that installs apps from their release pages and alerts you to updates. It supports GitHub, GitLab, F-Droid and others. License: GPL-3.0-only (per F-Droid). Sources: https://github.com/ImranR98/Obtainium , https://f-droid.org/packages/dev.imranr.obtainium.fdroid/
- **Latest release:** v1.7.3 (Oct 25, 2026), after v1.7.2 (Oct 24) and v1.7.1 (Oct 18). The v1.7.3 release includes `app-arm64-v8a-release.apk`. F-Droid added 1.7.3 on Oct 27, 2026. Sources: https://github.com/ImranR98/Obtainium/releases and the F-Droid page above.
- **Where to install it from:** GitHub Releases, IzzyOnDroid or F-Droid (package `dev.imranr.obtainium.fdroid`). Source: https://wiki.obtainium.imranr.dev/
- **Ready-made configs:** https://apps.obtainium.imranr.dev/ is a crowdsourced directory of about 480 apps with one-tap "add to Obtainium" links. Its data lives at https://github.com/ImranR98/apps.obtainium.imranr.dev

**How to use it** (source: https://wiki.obtainium.imranr.dev/ui_overview/):
1. Tap **Add App** and paste the app's URL. Obtainium detects the source type and trims GitHub URLs to the base repo. A URL it doesn't recognize falls back to the HTML source, which the wiki says "may work in some cases."
2. Your apps appear on the main **Apps** list.
3. **Settings → Updates** has the background check interval and Wi-Fi/charging limits. Long-press an app (or use select-all) to update several at once.
4. **Settings → Source Specific** takes GitHub or GitLab tokens. The wiki does not discuss rate limits.
5. The wiki's Limitations section warns that sources which rely on web scraping "can easily break due to changes in website design." (https://wiki.obtainium.imranr.dev/)

**Don't mix install sources for one app.** Android installs an update only if its signing certificate matches the installed app. (https://developer.android.com/studio/publish/app-signing) If you got Dolphin from the Play Store, keep updating it there. To switch it to Obtainium, uninstall it first. Back up your saves before uninstalling.

### Emulator sources

| App | Where to get it / what to paste | Verified status | Source |
|---|---|---|---|
| **RetroArch** (multi-system) | The crowdsourced Obtainium config for `com.retroarch.aarch64` tracks `https://buildbot.libretro.com/stable/` and picks the aarch64 APK. retroarch.com also offers direct APKs (default, 64-bit, 32-bit) plus Amazon, Huawei, Samsung Galaxy Store and F-Droid. | Stable **1.22.2**. retroarch.com labels both Play listings "(Outdated)" and says the Play version "has not been updated in over a year." **Conflict:** the Play listings for RetroArch and RetroArch Plus both show "Updated on Aug 26, 2026." The ES-DE FAQ advises against the Play build because it relies on SAF storage access and has "a limited set of cores." | https://www.retroarch.com/?page=platforms ; https://gitlab.com/es-de/emulationstation-de/-/blob/master/FAQ-ANDROID.md ; https://play.google.com/store/apps/details?id=com.retroarch.aarch64 ; git tags libretro/RetroArch (latest v1.22.2) |
| **Dolphin** (GameCube/Wii) | Easiest: the Play Store listing (developer "Dolphin Emulator", updated Oct 8, 2026). The crowdsourced Obtainium config tracks `https://dolphin-emu.org/update/latest/beta` (or `/dev`). dolphin-emu.org returned 403 to me, so I could not check its download page directly (**UNVERIFIED**). | Stable **2609a** (Oct 8, 2026), preview **2609-119** (Oct 25, 2026), per Wikipedia. Requires Android 5.0+, 64-bit only; Android 10 recommended. F-Droid lags at **2603a** (added Mar 24, 2026). | https://en.wikipedia.org/wiki/Dolphin_(emulator) ; https://play.google.com/store/apps/details?id=org.dolphinemu.dolphinemu ; https://f-droid.org/packages/org.dolphinemu.dolphinemu/ |
| **PPSSPP** (PSP) | GitHub releases have **no Android APK**; the v1.20.4 assets are iOS, Linux, Windows, macOS and source. Use ppsspp.org (direct APK), Play (PPSSPP or PPSSPP Gold), F-Droid, or the crowdsourced config that tracks `https://www.ppsspp.org/download/`. | **1.20.4** (assets dated May 16, 2026). Play listing updated May 16, 2026. | https://www.ppsspp.org/download/ ; https://github.com/hrydgard/ppsspp/releases/expanded_assets/v1.20.4 |
| **Azahar** (3DS; the site says it "continues the legacy of Citra") | `https://github.com/azahar-emu/azahar` | Stable **2126.2** (Oct 8, 2026), with `azahar-android-vanilla-2126.2.apk` and `azahar-android-googleplay-2126.2.apk`. Tags 2127.0-alpha1 to alpha3 are pre-releases. Play listing "Azahar Emulator" (`io.github.lime3ds.android`) updated Oct 8, 2026. | https://github.com/azahar-emu/azahar/releases/expanded_assets/2126.2 ; https://azahar-emu.org/ |
| **Lemuroid** (easy all-in-one, libretro-based) | `https://github.com/Swordfish90/Lemuroid`, or Play | **1.17.0**. GitHub asset `lemuroid-app-free-dynamic-release.apk` uploaded May 31, 2026. Play listing updated Apr 19, 2026. F-Droid availability: **UNVERIFIED**. | https://github.com/Swordfish90/Lemuroid/releases/expanded_assets/1.17.0 |
| **Vita3K** (PS Vita) | **Correction:** the old `Vita3K/Vita3K-Android` repo stopped at "Release 12" (tag commit dated June 6, 2024). The official download page now links an **"Android Nightlies"** APK at `https://github.com/Vita3K/Vita3K/releases/download/continuous/android-latest.apk`, which was last modified Oct 29, 2026. Note that the crowdsourced Obtainium config still points to the old Vita3K-Android repo. | Nightly builds are active. There is no numbered version. Game compatibility on the RP3/3+: **UNVERIFIED**. | https://vita3k.org/download ; https://github.com/Vita3K/Vita3K-Android/releases |
| **DuckStation** (PS1) | Google Play (developer Stenzek, updated Oct 24, 2026), linked from the official site. The site also links an **Android Beta** page at `https://downloads.duckstation.org/android-testing/`, which describes a Jetpack Compose rewrite and calls itself "beta quality software." | README: "No support is provided for the Android app." | https://www.duckstation.org/ ; https://raw.githubusercontent.com/stenzek/duckstation/master/README.md |
| **ES-DE** (frontend) | Paid on Android; see section 2. | — | — |

**Avoid Switch emulator repos as the base of a "hub".** Nintendo keeps filing DMCA notices against them on GitHub. **Correction:** the Apr 28, 2026 notice targets only two things: the fork `sweetbai/ryujinx` and the whole `Ryubing/.github` repo (Ryubing). Names such as Citron, Eden, Kenji-NX, MeloNX, Pine, Skyline, Sudachi, Suyu and Yuzu appear only in a bracketed example list that looks like unfilled template text, so that notice does not target them. Source: https://github.com/github/dmca/blob/master/2026/04/2026-04-28-nintendo.md

---

## 2. Frontends that bring everything together on Android

| Frontend | Price / where to get it | Status | Source |
|---|---|---|---|
| **ES-DE** | **Paid on Android**, sold through **Patreon** (https://www.patreon.com/es_de), the **Samsung Galaxy Store** and **Huawei AppGallery**. Google Play is not listed as a source. The desktop versions (Windows, macOS, Linux) are free and open source. The Android release "is a paid app, and it's partially closed source." | Latest **3.5.0** (released 2026-09-30). Requires **64-bit Android 10 or later**. Buy once on Patreon and use it on all your devices, with no subscription. Updates arrive by email, and you can resend them at https://resend.es-de.org. Patreon refunds are available within one month if ES-DE won't run on your device; Galaxy Store and AppGallery purchases can't be refunded directly by ES-DE. **Price: UNVERIFIED** (Patreon returned 403). A Notebookcheck article of uncertain date cites $5.50 on Patreon. | https://es-de.org/ ; https://gitlab.com/es-de/emulationstation-de/-/blob/master/FAQ-ANDROID.md ; https://gitlab.com/es-de/emulationstation-de/-/blob/master/CHANGELOG.md ; https://www.notebookcheck.net/ES-DE-emulator-frontend-delisted-from-Amazon-App-Store-other-emulators-still-available.808680.0.html |
| **Daijishō** | **Free** on Google Play (developer TapiocaFox, last updated Jan 30, 2026). The repo says the app "is currently closed-source"; it holds only assets, docs and platform files. | The developer wrote: "I decided to take a break from the Daijishō project, probably for quarters." | https://github.com/TapiocaFox/Daijishou ; https://play.google.com/store/apps/details?id=com.magneticchen.daijishou |
| **Beacon Game Launcher** | **$2.99** on Google Play (developer "NERDS TAKE OVER", package `com.radikal.gamelauncher`, updated Oct 14, 2026) | Active. **Correction:** the third-party guide does not say Beacon scrapes art automatically. It says you can enable scraping sources (ScreenScraper and SteamGridDB) and add accounts for them in Beacon's settings. | https://play.google.com/store/apps/details?id=com.radikal.gamelauncher ; https://www.joeysretrohandhelds.com/?p=2503 |

Device notes:
- **Retroid Pocket 3+ and RP3:** both list Android 11 (Liliputing, section 0), which meets ES-DE's 64-bit Android 10+ requirement on paper. Whether the RP3 or RP3+ runs a 64-bit build of Android is **UNVERIFIED**.
- **Low RAM:** the ES-DE FAQ says that on a device with "4 GB or so" of RAM, "it's almost unavoidable that ES-DE will get stopped if you are running an emulator that also uses a lot of memory." A lighter theme can help. The FAQ also recommends keeping the ES-DE folder and `downloaded_media` on internal storage rather than an SD card. (FAQ-ANDROID.md above)
- **Galaxy S24:** the Galaxy Store sells ES-DE natively on this phone. A Patreon purchase covers all your devices, including the Retroid. The FAQ says store versions "may not be available on all your devices." Whether the Galaxy Store version can be installed on the Retroid is **UNVERIFIED**.
- **Miyoo Mini Plus:** Onion OS is its own frontend. v4.3.1-1 is the newest tag on https://github.com/OnionUI/Onion (confirmed with git tags).

---

## 3. Syncing saves across the Miyoo, Retroid and phone

### Syncthing on Android
- The **official app is discontinued.** Its repo was archived on Dec 3, 2024, with the notice "This app is discontinued." Source: https://github.com/syncthing/syncthing-android
- **Syncthing-Fork (originally by Catfriend1)** changed hands. On Dec 8, 2025, heise reported that the repo vanished and reappeared under the **researchxxl** account, with no publicly verifiable handover from Catfriend1. Reviewers found no malicious changes so far, and F-Droid builds the app reproducibly. heise stressed that this is not lasting proof of trust. Source: https://heise.de/-11107337
- On Jan 27, 2026, a Privacy Guides forum user posted: "The two developers have eventually joined hands, so there is only one actively developed version." That post doesn't name the developers; a Feb 2, 2026 post names researchxxl and nel0x. These are community claims, not official statements. Source: https://discuss.privacyguides.net/t/which-syncthing-fork-should-one-use-after-the-projects-handover/34966
- **What exists today:**
  - F-Droid: package `com.github.catfriend1.syncthingfork`, **v2.1.7.0, added Oct 25, 2026**, built from https://github.com/researchxxl/syncthing-android. Source: https://f-droid.org/packages/com.github.catfriend1.syncthingfork/
  - Google Play: "Syncthing-Fork" by **nel0x**, package `com.github.catfriend1.syncthingandroid`, updated Aug 14, 2026. Source: https://play.google.com/store/apps/details?id=com.github.catfriend1.syncthingandroid
  - These are different package IDs. Pick one and stick with it.
- **Recommendation for a beginner:** treat the trust question as open. Copying save folders by hand over USB is a perfectly good alternative.

### The Onion OS (Miyoo) side
- Onion's features doc says: "Your saves and most of your preferences are now in `/Saves`… Simply copy this folder when you want to backup your data." Save states live in `Saves/CurrentProfile/states/[CORENAME]/` and in-game saves in `Saves/CurrentProfile/saves/[CORENAME]`. Sources: https://onionui.github.io/docs (features page, repo file `website/docs/01-features/index.md`) and https://onionui.github.io/docs/faq
- Onion's docs list a community **Syncthing** app by XK9274 (https://onionui.github.io/docs/apps/syncthing), described as being for "Onion 4.2.0 beta". **The linked repo https://github.com/XK9274/syncthing-app-miyoo cannot be reached today** (git clone fails), so treat it as unavailable.
- Also listed: **Cloud Saves** by hotcereal, which uses rclone. Docs: https://onionui.github.io/docs/apps/cloud-saves ; the repo exists: https://github.com/hotcereal/cloud-saves-miyoo-mini-plus. Whether it works on 4.3.1-1: **UNVERIFIED**.

### Will saves move between devices?
- **Correction:** the quotes in the original report ("usually format-interchangeable across cores…" and "any change to a core") do not appear in the libretro threads it cited, and I could not find them anywhere. What those threads actually say: whether saves carry across devices "depends on the core… some cores can handle it, some can't." A libretro team member said Snes9x SRAM "should definitely go back and forth" and suggested turning off SRAM compression if transfers fail. These are forum posts, not official docs. Sources: https://forums.libretro.com/t/save-states-from-android-to-pc/21735 ; https://forums.libretro.com/t/save-files-from-these-cores-dont-work-with-their-emulators/32221
- Onion's FAQ: "Save states can, on occasion, be incompatible between core versions/updates." Source: https://onionui.github.io/docs/faq
- In practice: use the **same RetroArch core** for a system on all three devices, sync only in-game save files (`.srm`), and make an in-game save before switching devices. That this always works is **UNVERIFIED**; test it with one game first.

### RetroAchievements
- Create an account at https://retroachievements.org. A third-party guide says "A free RetroAchievements account is required" (https://docs.webrcade.com/userguide/retroachievements/). The official FAQ covers only voluntary Patreon support and gives no price, so "free" is confirmed only by third parties.
- In RetroArch, log in under **Settings → Achievements**. Hardcore mode "prevents you from using emulation features like slow motion, fast forwarding, cheats and savestates." Source: https://www.retroarch.com/?page=achievements
- Onion's features list links RetroAchievements (https://onionui.github.io/docs). It needs Wi-Fi. The Mini Plus "only connects on 2.4 GHz" according to a secondary guide: https://handheldindex.pages.dev/firmware/onionos-setup-guide-miyoo-mini-plus/
- **Dolphin supports RetroAchievements for GameCube and Wii.** **Correction:** the version minimums apply generally, not only to hardcore. Wii needs 2603a (stable) or 2603-81 (nightly) or newer; GameCube needs 2407-68 or newer. For both, "Enable Dual Core (speedup)" must be unchecked. Source: https://docs.retroachievements.org/general/emulator-support-and-issues.html

---

## 4. Box art and metadata scraping

| Tool | Facts | Source |
|---|---|---|
| **ScreenScraper account** | Free ("You are about to create a free account at ScreenScraper"). Optional monthly donor tiers (shown in both € and $): 1 or 2 gives up to 50,000 requests/day; 5 gives 100,000/day plus 1 extra thread; 10 gives 100,000/day plus 5 extra threads. The free-tier quota is not stated. | https://www.screenscraper.fr/membreinscription.php |
| **Skraper** (PC) | A "FREE, non-commercial, non-profit application." Runs on Windows (.NET Framework 4.8.1) and Linux (mono-complete). macOS has no native build and might run under WINE, untested. Download: `Skraper-1.4.1.7z`. Data comes from ScreenScraper. | https://www.skraper.net/ |
| **Onion's built-in Scraper** (Mini Plus, over Wi-Fi) | Pulls covers from ScreenScraper, LaunchBox and RetroArch. Logging in to ScreenScraper means "less errors and faster." Select a game, press **Y** to open Game List Options, then choose Scraper. | https://onionui.github.io/docs/apps/scraper |
| **Onion + Skraper PC guide** | PNG images, max 250×360 px, in `Roms/<system>/Imgs` (capital I, case-sensitive). In Skraper, choose "Recalbox", tick "Include non-Recalbox rom folders", and set the output folder to `%ROMROOTFOLDER%\Imgs`. | https://onionui.github.io/docs/advanced/scraping |
| **ES-DE built-in scraper** | Supports ScreenScraper and TheGamesDB, in single-game and multi-scraper modes. I did not re-fetch the details in this pass (the USERGUIDE page did not render for my fetcher), so treat the specifics as **UNVERIFIED**. | https://gitlab.com/es-de/emulationstation-de/-/blob/master/USERGUIDE.md |

---

## 5. Legal ways to get games

### a) Dump (copy) cartridges you own
| Hardware | What it does | Status / price | Source |
|---|---|---|---|
| **GB Operator** (Epilogue) | Game Boy, GBC and GBA. Backs up game and save data using the **Playback** desktop app (Windows 10+, macOS 12+, Linux via Flatpak). The page lists companion apps, Retrace and Flashback, on iOS and Android; whether they can dump a cartridge to Android is **UNVERIFIED**. | $49.99 | https://www.epilogue.co/product/gb-operator |
| **SN Operator** (Epilogue) | SNES / Super Famicom | $59.99 | https://www.epilogue.co/ |
| **Retrode3** | Reads Mega Drive/Genesis, SNES/SFC and NES cartridges. | "The Retrode3 cannot be ordered yet." | https://www.retrode.com/en/ |
| **Open Source Cartridge Reader** (formerly sanni/cartreader) | An Arduino Mega shield. Firmware is GPL v3, hardware CC BY 4.0, wiki CC0. Natively reads NES, SNES, N64, GBC, GBA, Mega Drive and Master System, plus about 40 more systems with adapters. | The old repo was **archived on Jun 15, 2026** with the notice "We have moved, please visit us at https://github.com/oscartreader." The oscr-firmware and oscr-databases repos exist. Whether assembled units are sold: **UNVERIFIED**. | https://github.com/sanni/cartreader ; https://github.com/oscartreader |

### b) Wii and GameCube discs (for the Wii-on-Retroid goal)
- **Homebrew your own Wii** with https://wii.hacks.guide/. It installs the Homebrew Channel and BootMii (via the HackMii Installer) and has you make a NAND backup ("crucially important to have on hand if anything goes wrong").
- **Dump discs with CleanRip:** https://wii.hacks.guide/dump-games. Save to an SD card or USB drive (FAT32), and verify each dump against Redump's DAT files. Space needed: Wii single-layer 4.7 GB, dual-layer 8.5 GB; a GameCube disc is "all 1.3 GB of the Mini DVD." **Wii Family Edition, Wii mini and the Wii U's vWii cannot dump GameCube discs.** CleanRip repo: https://github.com/emukidid/cleanrip (latest version tag 2.4).

### c) PS1 and PS2 discs on a PC
- Redump prefers **redumper**, with **DiscImageCreator** second. **MPF** is a graphical front end. Quote: "Redump usually doesn't accept dumps made with tools other than redumper or DiscImageCreator." Aaru 5.3.2-lts through 6.0.0-alpha9 dump audio sector data incorrectly on retry. Source: https://dumping.guide/discs/general. **Correction:** https://dumping.guide/discs/sony names no tools itself; it says PS1 and PS2 games "can be dumped with the methods in the general disc dumping guide."
- Repos exist: https://github.com/superg/redumper , https://github.com/saramibreak/DiscImageCreator , https://github.com/SabreTools/MPF
- **ImgBurn** is not mentioned in either guide. Whether it gives accurate PS1 dumps is **UNVERIFIED**, so use the tools above.

### d) BIOS files from your own consoles
- **PS2:** PCSX2 says BIOS files "are proprietary software and must therefore be dumped from your own console," and recommends **biosdrain**. It runs on a softmodded PS2 (FreeMcBoot or FreeDVDBoot, launched from uLaunchELF) and writes to a FAT32 USB drive. Source: https://pcsx2.net/docs/setup/bios/. The biosdrain README (https://github.com/F0bes/biosdrain, latest tag v2.2.2) lists what it dumps: ROM0, ROM1, ROM2, NVM and MEC.
- **PS1:** DuckStation needs "a PS1 or PS2 'BIOS' ROM image" and says "you should dump this from your own console using Caetla or other means." So a PS2 BIOS dumped with biosdrain also works in DuckStation. Source: https://raw.githubusercontent.com/stenzek/duckstation/master/README.md
- **Correction:** biosdrain's README explicitly says "I politely ask that you do not share your BIOS files!" PCSX2's page and DuckStation's README don't state that request in so many words; they say only that you must dump your own and that a BIOS isn't included for legal reasons.

### e) Free, legal homebrew
- **Homebrew Hub** (https://hh.gbdev.io/): 1,642 entries (GB 918, GBC 451, GBA 249, NES 24), with in-browser emulation.
- **itch.io tags:** https://itch.io/games/tag-homebrew and https://itch.io/games/tag-gameboy. Check each game's download terms.
- **PDRoms** (https://pdroms.de/): a homebrew news and download site ("homebrew 4 you", copyright 1998–2026). Its platform counts conflict (the footer says 46, the filter says 85), and its disclaimer page returned 404. Its hosting policy is **UNVERIFIED**, so check each file's license.

### f) Paid official routes
- **Nintendo Switch Online:** a "curated library of Super NES™, Game Boy™, and NES™ games"; the classics section says "over 150 favorites", without saying whether that count is the base library only. The Expansion Pack adds "additional libraries"; GameCube classics are Switch 2 only. Source: https://www.nintendo.com/us/online/nintendo-switch-online/
- **PlayStation Plus Premium** (includes the Classics Catalog): $19.99/month, $54.99/3 months, $159.99/12 months. Source: https://www.playstation.com/en-us/ps-plus/
- These run on Nintendo and Sony hardware, not on the Retroid or Miyoo.

---

## 6. There is no legal all-in-one "ROM pack"

- I found **no legal all-in-one ROM or BIOS pack**. Emulator projects tell you to dump your own (PCSX2: https://pcsx2.net/docs/setup/bios/ ; DuckStation README). Repos that offer "every ROM" or "all BIOS" packs are piracy, and none are linked here.
- **How GitHub handles it:** for a notice about specific files, GitHub gives the owner "approximately 1 business day" to remove them, then disables the repo. For a notice claiming a whole repo infringes, GitHub skips that step and disables the repo "expeditiously." Redacted notices are published at https://github.com/github/dmca. Source: https://docs.github.com/en/site-policy/content-removal-policies/dmca-takedown-policy
- **Caveat:** the notices checked here were about Switch emulators (for example, the Apr 28, 2026 notice targets `sweetbai/ryujinx` and Ryubing). Whether GitHub has recently taken down ROM-pack repos specifically is **UNVERIFIED**. Hosting copyrighted game files is infringement either way.

---

### UNVERIFIED items in one place
- ES-DE Android price on Patreon and the Galaxy Store ($5.50 comes only from an undated secondary source).
- Whether the Galaxy Store version of ES-DE installs on the Retroid, and whether the RP3/RP3+ run 64-bit Android.
- Retroid specs from the maker (the goretroid.com page returns 404); the specs above come from Liliputing and other secondary sources.
- How well Wii games run on the RP3+ (T618) or RP3 (T310).
- Whether the Onion Syncthing app still exists (its repo is unreachable), and whether Cloud Saves works on 4.3.1-1.
- Whether syncing `.srm` files between devices always works (forum guidance says it depends on the core).
- Vita3K nightly compatibility on the RP3/3+.
- Lemuroid on F-Droid; Dolphin's own download page (returned 403).
- Whether GB Operator's Android apps can dump cartridges; whether assembled Open Source Cartridge Readers are sold.
- Whether ImgBurn gives accurate PS1/PS2 dumps.
- RetroAchievements pricing (only third parties say it is free).
- The ES-DE scraper details (USERGUIDE not re-fetched).
- PDRoms' hosting policy.
- Whether GitHub has recently taken down ROM-pack repos.

### Sources
- https://github.com/ImranR98/Obtainium/releases
- https://f-droid.org/packages/dev.imranr.obtainium.fdroid/
- https://wiki.obtainium.imranr.dev/
- https://wiki.obtainium.imranr.dev/ui_overview/
- https://apps.obtainium.imranr.dev/
- https://github.com/ImranR98/apps.obtainium.imranr.dev
- https://developer.android.com/studio/publish/app-signing
- https://www.retroarch.com/?page=platforms
- https://play.google.com/store/apps/details?id=com.retroarch.aarch64
- https://en.wikipedia.org/wiki/Dolphin_(emulator)
- https://play.google.com/store/apps/details?id=org.dolphinemu.dolphinemu
- https://f-droid.org/packages/org.dolphinemu.dolphinemu/
- https://www.ppsspp.org/download/
- https://github.com/hrydgard/ppsspp/releases/expanded_assets/v1.20.4
- https://github.com/azahar-emu/azahar/releases/expanded_assets/2126.2
- https://azahar-emu.org/
- https://github.com/Swordfish90/Lemuroid/releases/expanded_assets/1.17.0
- https://github.com/Vita3K/Vita3K-Android/releases
- https://vita3k.org/download
- https://www.duckstation.org/
- https://downloads.duckstation.org/android-testing/
- https://raw.githubusercontent.com/stenzek/duckstation/master/README.md
- https://github.com/github/dmca/blob/master/2026/04/2026-04-28-nintendo.md
- https://es-de.org/
- https://gitlab.com/es-de/emulationstation-de/-/blob/master/FAQ-ANDROID.md
- https://gitlab.com/es-de/emulationstation-de/-/blob/master/CHANGELOG.md
- https://www.notebookcheck.net/ES-DE-emulator-frontend-delisted-from-Amazon-App-Store-other-emulators-still-available.808680.0.html
- https://github.com/TapiocaFox/Daijishou
- https://play.google.com/store/apps/details?id=com.magneticchen.daijishou
- https://play.google.com/store/apps/details?id=com.radikal.gamelauncher
- https://www.joeysretrohandhelds.com/?p=2503
- https://liliputing.com/retroid-pocket-3-is-a-149-handheld-game-console-with-a-unisoc-t618-processor/
- https://www.tomsguide.com/news/samsung-galaxy-s24s-performance-could-vary-by-region-unless-you-go-ultra
- https://androidauthority.com/samsung-galaxy-s24-snapdragon-vs-exynos-countries-3402659
- https://github.com/syncthing/syncthing-android
- https://heise.de/-11107337
- https://discuss.privacyguides.net/t/which-syncthing-fork-should-one-use-after-the-projects-handover/34966
- https://f-droid.org/packages/com.github.catfriend1.syncthingfork/
- https://play.google.com/store/apps/details?id=com.github.catfriend1.syncthingandroid
- https://onionui.github.io/docs
- https://onionui.github.io/docs/faq
- https://onionui.github.io/docs/apps/syncthing
- https://onionui.github.io/docs/apps/cloud-saves
- https://github.com/hotcereal/cloud-saves-miyoo-mini-plus
- https://onionui.github.io/docs/apps/scraper
- https://onionui.github.io/docs/advanced/scraping
- https://github.com/OnionUI/Onion
- https://forums.libretro.com/t/save-states-from-android-to-pc/21735
- https://forums.libretro.com/t/save-files-from-these-cores-dont-work-with-their-emulators/32221
- https://www.retroarch.com/?page=achievements
- https://docs.retroachievements.org/general/emulator-support-and-issues.html
- https://docs.retroachievements.org/general/faq.html
- https://docs.webrcade.com/userguide/retroachievements/
- https://handheldindex.pages.dev/firmware/onionos-setup-guide-miyoo-mini-plus/
- https://www.screenscraper.fr/membreinscription.php
- https://www.skraper.net/
- https://www.epilogue.co/product/gb-operator
- https://www.epilogue.co/
- https://www.retrode.com/en/
- https://github.com/sanni/cartreader
- https://github.com/oscartreader
- https://wii.hacks.guide/
- https://wii.hacks.guide/dump-games
- https://github.com/emukidid/cleanrip
- https://dumping.guide/discs/general
- https://dumping.guide/discs/sony
- https://github.com/superg/redumper
- https://github.com/saramibreak/DiscImageCreator
- https://github.com/SabreTools/MPF
- https://pcsx2.net/docs/setup/bios/
- https://github.com/F0bes/biosdrain
- https://hh.gbdev.io/
- https://itch.io/games/tag-homebrew
- https://itch.io/games/tag-gameboy
- https://pdroms.de/
- https://www.nintendo.com/us/online/nintendo-switch-online/
- https://www.playstation.com/en-us/ps-plus/
- https://docs.github.com/en/site-policy/content-removal-policies/dmca-takedown-policy
