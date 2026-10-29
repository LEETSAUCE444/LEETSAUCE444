
# Retroid Pocket 3 / 3+ report: hardware check, Wii and GameCube, getting more speed, emulators and frontends (fact-checked)

*Fact-checked 2026-10-29. Each claim was re-checked against the linked page, a GitHub tag listing (`git ls-remote`), or a GitHub releases page. Anything I could not confirm is marked **UNVERIFIED**. Emulator apps change quickly, so check the linked page before you rely on a version number.*

**The most important point:** the two models use different chips. The **3+** has a Unisoc **T618**. The original **Retroid Pocket 3** has a Unisoc **T310**, which is much weaker. Which one Wil owns decides how much Wii he can play on it.

---

## 1. Specs, and how to tell which one Wil has

### Spec comparison

| | **Retroid Pocket 3 (original)** | **Retroid Pocket 3+** |
|---|---|---|
| Chip | Unisoc **T310**: 1× Cortex-A75 @ 2 GHz + 3× Cortex-A55 @ 1.8 GHz | Unisoc **T618**: 2× Cortex-A75 @ 2 GHz + 6× Cortex-A55 @ 2 GHz |
| Graphics | PowerVR GE8300 @ 800 MHz | Mali-G52 MC2 @ 850 MHz |
| RAM | **2 GB or 3 GB** LPDDR4x | **4 GB** LPDDR4x-1866 |
| Storage | **32 GB** eMMC + microSD | **128 GB** eMMC 5.1 + microSD |
| Screen | 4.7", 1334×750, touch (same panel on both) | same, 450 nits |
| Battery | 4,000 mAh | 4,500 mAh |
| Android | Android 11 | Android 11. At review time Retroid "hasn't yet confirmed" an Android 12/13 update. Whether one ever shipped is **UNVERIFIED**. |
| Cooling | Passive (Liliputing: metal frame + aluminum heat sink) | Passive, no fan. Based on GoRetroid's listing as it appeared in search results; the page returned 404 when fetched. |
| Launch price | $119 and up (3 GB model: $129), shipping from Aug 20, 2022 | $149, shipping from Nov 18, 2022 |

Sources: [Liliputing, 3+ launch](https://liliputing.com/retroid-pocket-3-is-a-149-handheld-game-console-with-a-unisoc-t618-processor/) (full spec comparison of both models), [Liliputing, original RP3 (T310)](https://liliputing.com/retroid-pocket-3-handheld-retro-game-system-has-a-4-7-inch-display-unisoc-t310-chip-and-119-starting-price/), [Notebookcheck](https://www.notebookcheck.net/Retroid-Pocket-3-launches-with-performance-upgrades-in-multiple-colours.667092.0.html), [Reviewed.com review](https://reviewed.com/gaming/content/retroid-pocket-3-plus-review), [GoRetroid 3+ page](https://www.goretroid.com/en-ca/products/retroid-pocket-3-handheld-retro-gaming-system-1) (seen in search results only; returned 404 when fetched).

Smaller notes:
- DroiX and RetroABXY both label the GPU "Mali G52 MP2" ([DroiX](https://droix.net/blogs/en-gb/retroid-pocket-3-announced-specs-and-availability/)). It is the same GPU under a different label.
- DroiX says the 3+ "shares the Display, Buttons, Battery and Shell" with the RP3. That conflicts with the 4,000 vs 4,500 mAh figures from Liliputing, Notebookcheck and Reviewed.
- Gyroscope: [RetroCatalog](https://retrocatalog.com/retro-handhelds/retroid-pocket-3-plus) lists one. Testers in the community RP3+ sheet report gyro controls working in Moto GP '08 and New Super Mario Bros. Wii ([RP3+ sheet](https://docs.google.com/spreadsheets/d/1Vf7SIS7ecWa_J301h0mb2bxMWBMtKLvcpAFyaa5-LDc/htmlview), Wii tab). I could not read an official Retroid spec page, so treat the gyro as **probable but UNVERIFIED**.
- RetroCatalog gives the CPU as "Cortex-A75" with 8 cores, which is misleading. The real layout is 2× A75 + 6× A55.
- Hall-effect sticks came with the later **Metal Edition** ([Notebookcheck, Metal Edition](https://www.notebookcheck.com/Retroid-Pocket-3-Metal-Edition-Gaming-Handheld-startet-mit-Hall-Effekt-Joysticks.726236.0.html)). Reviewed.com also mentions a $10 Hall-stick upgrade option at checkout. The claim that L3/R3 exist only on the Metal Edition is **UNVERIFIED**.

### How Wil can tell which one he has

1. **Check storage (most reliable).** Open Settings > Storage. About **128 GB** total means a 3+. About **32 GB** means the original RP3 ([Liliputing](https://liliputing.com/retroid-pocket-3-is-a-149-handheld-game-console-with-a-unisoc-t618-processor/)).
2. **Check RAM or the chip.** 4 GB means 3+; 2 or 3 GB means RP3. A free system-info app shows the chip: "T618" means 3+, "T310" means RP3. This follows from the specs above. Which app to use, and whether Settings shows RAM, is **UNVERIFIED**.
3. **Settings > About phone > Model.** The exact text it shows is **UNVERIFIED**.
4. **Box or back label.** I found no source describing the label (**UNVERIFIED**). If the box says "3+" or "3 Plus", that settles it.

### Why it matters for Wii and GameCube

- Retro Game Corps' starter guide (marked "Last updated: 25SEP2026") recommends Dolphin internal resolution of "**.5x for RP3** and RP2+, **1x for RP3+/Flip**, 2x for RP4/Pro" ([RGC](https://retrogamecorps.com/2022/01/16/retroid-pocket-2-starter-guide/)).
- **Original RP3 (T310):** It has half the big CPU cores of the 3+ and a weaker GPU, and RGC tiers it at 0.5x. I found no Wii compatibility list for the original RP3. "Wii is mostly not realistic on the RP3" is therefore an **inference, not a tested result**.

---

## 2. Wii and GameCube on the 3+

### Which Dolphin build to use (as of October 29, 2026)

| Build | Status (verified) | Use it? |
|---|---|---|
| **Official Dolphin** (dolphin-emu.org, or Google Play) | Actively developed. Release **2609** was tagged Sep 23–24, 2026, and hotfix **2609a** ("First hotfix release for 2609") was tagged Oct 7, 2026, US Eastern time. Both dates come from the git tags. Whether 2609a is Android-only is **UNVERIFIED**. 2609 added Android NetPlay and Wii Balance Board support on Android. Dolphin requires Android 7.0+, a 64-bit CPU and OpenGL ES 3.0+, all of which the 3+ meets. One tutorial says Android NetPlay needs **Android 12L**; if that is true, it would not work on the Android 11 3+ (**UNVERIFIED**). | **Yes. This is the default.** |
| **"Dolphin for Handheld"** (offered in Retroid's setup wizard) | RGC says it "provides an excellent mix of accuracy and performance" and can be preinstalled during setup. RGC removed its APK links "at the request of the Dolphin team". The RP3+ sheet says it is "recommended for the best performance results on Gamecube games". Which Dolphin version it is based on is **UNVERIFIED**. | **Yes. Try it alongside official Dolphin.** |
| **MMJR / MMJR2** (old speed-focused forks) | Most Wii tests on the RP3+ sheet used these (about 49 of 74 rows), and the sheet's Wii tab says "My biggest Recommendation is Dolphin MMJR-11505!" The original GitHub repositories no longer resolve; I tested Bankaimaster999/Dolphin-MMJR and -MMJR2. Emulation General Wiki edit logs record the removals in March 2023. A community fork, **Medard22/Dolphin-MMJR2-VBI** (latest tag v2.3.000), calls itself "semi-actively maintained", warns it "is based on older source code", and tells newcomers to use official Dolphin. | Optional, for advanced users only |
| DolphinCS | A fork that "adds the ability to change where data is stored" (Joey) | Not needed |

Sources: Dolphin tags from [github.com/dolphin-emu/dolphin](https://github.com/dolphin-emu/dolphin) (`git ls-remote` plus tag dates). [Dolphin README system requirements](https://raw.githubusercontent.com/dolphin-emu/dolphin/master/Readme.md). Coverage of 2609: [UbuntuHandbook](https://ubuntuhandbook.org/index.php/2026/09/dolphin-emulator-2609-released-with-android-netplay/), [Notebookcheck](https://www.notebookcheck.net/Dolphin-Emulator-Android-update-adds-cross-platform-netplay-and-improved-rumble-amid-AI-attacks.1407268.0.html), [Wikipedia](https://en.wikipedia.org/wiki/Dolphin_(emulator)). Play Store distribution: [Dolphin forum, "distributed on Google Play again"](https://forums.dolphin-emu.org/Thread-dolphin-is-now-distributed-on-google-play-store-again?pid=476560). Builds and forks: [RGC](https://retrogamecorps.com/2022/01/16/retroid-pocket-2-starter-guide/), [RP3+ sheet](https://docs.google.com/spreadsheets/d/1Vf7SIS7ecWa_J301h0mb2bxMWBMtKLvcpAFyaa5-LDc/htmlview) (Welcome and Wii tabs), [MMJR2-VBI README](https://github.com/Medard22/Dolphin-MMJR2-VBI), [Emulation General Wiki: Dolphin MMJR](https://emulation.gametechwiki.com/index.php/Dolphin_MMJR) (blocked direct fetch; seen via search), [Joey's Dolphin guide](https://www.joeysretrohandhelds.com/guides/android-nintendo-gamecube-emulation-setup-guide-with-dolphin/). RetroAchievements for Wii needs Dolphin 2603 or later ([Held Games](https://heldgames.com/guides/dolphin-android-setup-guide)).

**Caution about uninstalling the preinstalled Dolphin.** On a Retroid Pocket 5, one owner deleted the preinstalled Dolphin **but kept its app data**. After that, the Play Store and APK installs failed with a package conflict. Another user explained the cause: the setup-wizard, Play Store and Obtainium builds are signed with different certificates. **No factory reset was needed.** The fix was to re-run the Retroid setup wizard (Settings > Handheld Settings > Advanced), re-select Dolphin, then uninstall it again **without** keeping data, after which the Play Store version installed ([Dolphin forum](https://forums.dolphin-emu.org/Thread-unable-to-reinstall-dolphin-on-retroid-pocket-5)). Whether the 3+ behaves the same way is **UNVERIFIED**. Simplest advice: keep the preinstalled Dolphin, and if you do remove it, don't keep its data.

### What runs well and what doesn't on the 3+

The main data source is the community **RP3+ Compatibility Sheet** ([Google Sheet](https://docs.google.com/spreadsheets/d/1Vf7SIS7ecWa_J301h0mb2bxMWBMtKLvcpAFyaa5-LDc/htmlview), maintained by "FruitLoops"). Its Wii tab says "Total Games Tested: 71". Tests are dated **November 2022 to May 2023**. **Most Wii tests used the MMJR/MMJR2 forks or Dolphin for Handheld; only a handful used official Dolphin.** Results on today's official Dolphin may differ in either direction.

The sheet's own words: "PS2, Wii and 3DS can be a hit-or-miss, don't expect 100% of their libraries playable, but lots of titles works just fine". It also says "Wii is a lot more settings-sensitive and is a lot more emulator sensitive compared to Gamecube."

| Rating in the sheet | Example games (1x unless noted) |
|---|---|
| **Perfect / Great** | New Super Mario Bros. Wii, Fire Emblem: Radiant Dawn, Muramasa, Wario Land: Shake It!, Klonoa, Rayman Origins (1.5x), Rhythm Heaven Fever (1.5x; turn Store EFB Copies to Texture Only **off** so Shrimp Shuffle works), Mega Man 9, Cave Story (1.5x), Animal Crossing: City Folk, Kirby's Epic Yarn, Kirby's Return to Dreamland (1.5x), Sonic Colors, Pandora's Tower, Monster Hunter Tri, Dragon Ball Z Budokai Tenkaichi 3, Super Paper Mario (2x), Tatsunoko vs. Capcom, Call of Duty: Black Ops |
| **Playable** | Mario Kart Wii (frame dips with many racers), Super Mario Galaxy 2, Xenoblade Chronicles (about 30 fps in the open world, about 90% speed in big fights), Skyward Sword (25–30 fps), Super Smash Bros. Brawl (needs OpenGL; some stages crash), Epic Mickey |
| **Somewhat** (70–89% speed) | Super Mario Galaxy, Donkey Kong Country Returns, GoldenEye 007, Metroid: Other M, Sonic & Sega All-Stars Racing |
| **Bad** | Wii Sports (half speed; motion controls "hellish to map"), The Last Story, Super Monkey Ball: Banana Blitz (crashes), Shiren the Wanderer |

**Pattern:** 2D platformers and lighter games usually run well. Big 3D or effects-heavy games and motion-control-heavy games struggle.

### Recommended Dolphin settings for the 3+

The setting names come from current official Dolphin Android source code ([strings.xml](https://raw.githubusercontent.com/dolphin-emu/dolphin/master/Source/Android/app/src/main/res/values/strings.xml), master branch). Menus in 2609a may differ slightly.

| Setting | Recommendation for the 3+ | Source |
|---|---|---|
| Video Backend | **Vulkan** first. Most sheet testers used it. Switch to **OpenGL** if a game glitches; Brawl needs OpenGL. Held Games' "use Vulkan" advice is written for Snapdragon devices, and the 3+ uses a Mali GPU. | RP3+ sheet, [Held Games](https://heldgames.com/guides/dolphin-android-setup-guide) |
| Internal Resolution | **1x Native.** 1.5x only for light games. | [RGC](https://retrogamecorps.com/2022/01/16/retroid-pocket-2-starter-guide/), RP3+ sheet |
| Shader Compilation Mode | Sources disagree. RGC recommends **Hybrid Ubershaders**. Dolphin's own text says **Specialized (Default)** is "Recommended for low-end hardware". Start with Specialized; try Hybrid if a game stutters. | RGC; strings.xml |
| Compile Shaders Before Starting | **ON.** Dolphin: "causes a delay when launching games, but will reduce stuttering early on". | RGC, Joey, strings.xml |
| VBI Skip | Per game. RGC: it "can significantly improve the gaming experience on lower-end devices like the Retroid Pocket 3+", but some games (Twilight Princess, Wind Waker) may not work with it. | RGC, strings.xml |
| Skip EFB Access from CPU / Store EFB Copies to Texture Only | Speed hacks, set per game. Sheet notes: in **Super Mario Galaxy 2**, Skip EFB Access from CPU breaks the Wii Remote pointer. In **Super Mario Galaxy** the tester blamed "Store EFB Copy to Texture only" for the pointer problem. Leave Store EFB Copies to Texture Only on by default, and turn it off only to fix glitches (The Last Story, Rhythm Heaven's Shrimp Shuffle). Turning it off can cost a lot of speed. | RP3+ sheet, strings.xml |
| Immediately Present XFB | Many testers turned it ON per game for speed. | RP3+ sheet |
| Dual Core + Synchronize GPU Thread | Keep Sync GPU Thread on **"On Idle Skipping"**. Dolphin says "Selecting 'Never' is risky and not recommended!" Some sheet testers turned it off for specific games and accepted occasional crashes. | strings.xml, RP3+ sheet |
| Override Emulated CPU Clock Speed | Per game. Testers often used **30–65% underclock**. Brawl (400%), Xenoblade (300%) and F-Zero-style racers used *over*clock. Dolphin warns that a non-default clock "WILL break games and cause glitches". | RP3+ sheet, strings.xml |
| Audio | "Audio Stretching" does not appear in current strings. Options: **Fill Audio Gaps** ("If unsure, leave this checked"), **Audio Buffer Size** ("If unsure, set this to 80 ms"; raising it can help crackling), **Preserve Audio Pitch**. Held Games also suggests the **OpenSL ES** audio backend for crackling. | strings.xml, Held Games |
| Per-game settings | Long-press a game, then Properties > Edit Game Settings | Held Games |

**About the PAL tip.** The sheet says "Use PAL roms when possible to maximize performance". RGC says PAL games "cap out at 50Hz". One sheet entry (Mario Kart Wii) found 50 Hz ran *worse* and used PAL60. This only helps if Wil owns PAL discs, because the legal route is dumping his own games (see the box at the end).

### Wii Remote controls on a handheld

- **Pointer on the right stick:** In Wii Input > Motion Simulation, map "Point" to the right analog stick and tick **Relative Input** ([Joey](https://www.joeysretrohandhelds.com/guides/android-nintendo-gamecube-emulation-setup-guide-with-dolphin/)). Held Games also maps the pointer to the right stick.
- **Pointer by touchscreen:** Dolphin Android has a "Touch IR Pointer" with IR Mode **Follow** or **Drag**, and an "Always recenter" option ([strings.xml](https://raw.githubusercontent.com/dolphin-emu/dolphin/master/Source/Android/app/src/main/res/values/strings.xml)).
- **Known conflicts:** One user found a stick-mapped pointer stopped working once they touched the screen ([Dolphin forum](https://forums.dolphin-emu.org/Thread-wii-mappings-for-ir-controls-stop-working-when-i-touch-the-screen); unresolved thread). Another reported the touch pointer only worked with device sensors off, but later said it worked. A developer said touch controls the pointer under "Use Device Sensors (Without Pointer Emulation)" ([Dolphin forum](https://forums.dolphin-emu.org/Thread-solved-touchirpointer-disabled-when-device-sensors-enabled?pid=502732)). Pick one pointer method per game.
- **Shake:** Joey maps Wii Remote "Shake XYZ" to R2 and Nunchuk shake to L3. Held Games maps shake to the left bumper.
- **Sideways games:** Make a separate profile with "Sideways Wii Remote" checked (Joey).

### Honest verdict on Wii

On the **3+**, about two-thirds of the sheet's tested Wii entries are rated Perfect or Great (49 of the 74 rated rows I counted; the sheet header says 71 games). Two caveats: testers chose which games to try, and most used MMJR builds that are no longer officially available. Realistically, expect lighter and 2D games to be good, along with games that use the pointer only lightly. Expect per-game tweaking, shader stutter and occasional crashes. Motion-heavy games (Wii Sports) and big 3D games (Galaxy, DKC Returns) are disappointing. The sheet's own comment on Wii Sports ends "at that point get a PC".

**The Galaxy S24-series phone is far stronger.** Held Games calls 2x "Good balance... on Snapdragon 8 Gen 1+" and reserves 3x for 8 Gen 2 or better ([Held Games](https://heldgames.com/guides/dolphin-android-setup-guide)). US S24, S24+ and S24 Ultra models use Snapdragon 8 Gen 3; the S24/S24+ in Europe, Korea and Australia use Exynos 2400 ([Android Authority](https://androidauthority.com/samsung-galaxy-s24-snapdragon-vs-exynos-countries-3402659)). Dolphin performance on the Exynos 2400 is **UNVERIFIED**. Play heavy Wii games on the phone.

---

## 3. "Make it run faster": what can actually be done

**The hardware can't be "recoded".** The T618's speed is fixed. Wil can change the settings, the system updates, and which emulator builds he uses.

| Action | Details | Source |
|---|---|---|
| **Performance mode** | Joey: "Balance or Performance mode unless you'll be doing GameCube/Wii/PS2 emulation", where Extreme helps some games. One Reddit test found Extreme drew the same power as Performance in a GameCube game (anecdotal). The exact menu path is **UNVERIFIED**; look in Retroid's Handheld Settings. The 3+ has no fan, so expect more heat. | [Joey's RP3+ guide](https://joeysretrohandhelds.com/guides/retroid-pocket-3-plus-setup-guide), [RetroCompass](https://retrocompass.web.app/en/retroid/pocket-3-plus/troubleshooting) |
| **System (OTA) update** | The guides give different paths: Settings > System > Updates (RGC), System > Updater (Joey), System > Advanced > Updater (RetroCompass). | [RGC](https://retrogamecorps.com/2022/01/16/retroid-pocket-2-starter-guide/), [Joey](https://joeysretrohandhelds.com/guides/retroid-pocket-3-plus-setup-guide), [RetroCompass](https://retrocompass.web.app/en/retroid/pocket-3-plus/troubleshooting) |
| **Battery Saver off** | Battery Saver "limits or turns off background activity", and apps "may experience delays". It is at Settings > Battery > Battery Saver. | [Google Android Help](https://support.google.com/android/answer/7664692?hl=en) |
| **Lower animation scales** | Tap Build number 7 times to enable Developer options, then lower Window and Transition animation scale. This makes menus feel snappier but does **not** raise game frame rates (my inference). | [Android Developers](https://developer.android.com/studio/debug/dev-options) |
| **Close background apps; Floating Icon off** | Close other apps before launching Dolphin (Held Games). The Floating Icon is "the white bar that shows on the right in-game" (Joey). RGC says to turn it off from the swipe-down panel. | [Held Games](https://heldgames.com/guides/dolphin-android-setup-guide), [Joey](https://joeysretrohandhelds.com/guides/retroid-pocket-3-plus-setup-guide), [RGC](https://retrogamecorps.com/2022/01/16/retroid-pocket-2-starter-guide/) |
| **Skip apps he won't use** | The setup wizard offers to preinstall "emulators, tools and media players". Skipping some frees storage; any speed gain is **UNVERIFIED**. | [DroiX guide](https://droix.net/knowledge-base/article/retroid-pocket-3-plus-and-flip/) |
| **Per-game emulator settings** | This is where most of the real speed comes from (section 2). | — |

**Custom firmware or ROMs for the 3+: nothing verified.**
- LineageOS officially supports the Retroid Pocket 6 ([9to5Google](https://9to5google.com/2026/07/01/the-retroid-pocket-6-now-officially-supports-lineageos/), which says "older handhelds are not yet supported"). It also supports the Pocket Nova ([LineageOS wiki, RPN](https://wiki.lineageos.org/devices/RPN/), [Android Authority](https://androidauthority.com/retroid-pocket-nova-android-16-lineageos-3693722)). No 3+ support was found.
- GammaOS targets Anbernic T618 handhelds (RG405M, RG405V, RG505). It used the RP3+'s GPU driver experimentally, has no Retroid release, and the repository was **archived May 2, 2026** ("Superceded by GammaOS Next") ([GammaOS repo](https://github.com/TheGammaSqueeze/GammaOS), [release notes](https://newreleases.io/project/github/TheGammaSqueeze/GammaOS/release/GammaOS_v1.1_RG405M)).
- I found no reliable rooting, Magisk or GSI source for the 3+. **UNVERIFIED, and not recommended for a beginner**: flashing system software can brick the device.

---

## 4. Best emulator for each system on the 3+

Picks mostly follow RGC's per-generation table ([RGC](https://retrogamecorps.com/2022/01/16/retroid-pocket-2-starter-guide/)). "Latest" means the newest GitHub tag found with `git ls-remote` on 2026-10-29.

| System | Pick for the 3+ | Install from | Notes |
|---|---|---|---|
| NES, SNES, GB/GBC/GBA, Genesis, Master System, arcade | **RetroArch** cores (e.g. FCEUmm, Snes9x, Gambatte, mGBA, Genesis Plus GX, FinalBurn Neo) | RGC links the libretro **buildbot (aarch64)**, not the Play Store. Latest stable tag v1.22.2. | Core names come from RGC and Joey; the exact core list is not re-verified. The sheet says "Everything up to Gamecube/PS2 works just perfect." |
| PS1 | **DuckStation** | Google Play, per its [README](https://raw.githubusercontent.com/stenzek/duckstation/master/README.md) | The README says "No support is provided for the Android app". The developer said there will be no more Android updates ([Android Authority, Mar 11, 2026](https://www.androidauthority.com/duckstation-ends-android-support-3648430/)). Whether it is still listed on Play is **UNVERIFIED**. Alternative: the RetroArch core **SwanStation** ("generally very good", Joey). |
| N64 | **Mupen64Plus FZ** (M64Plus FZ). Joey prefers the paid Pro version. | Google Play | RGC: standalone FZ "for RP4 and below". [Joey](https://joeysretrohandhelds.com/guides/retroid-pocket-3-plus-setup-guide) |
| PSP | **PPSSPP** (v1.20.4) | Google Play (free and Gold) | RGC: "3x+ resolution for RP3+". The sheet: almost all PSP games run at 3x. ([PPSSPP download page](https://www.ppsspp.org/download/)) |
| Nintendo DS | **melonDS (Android)** (latest tag beta-1.10.0) | Google Play **or** GitHub releases | [README](https://github.com/rafaelvcaetano/melonDS-android). DraStic was removed from Google Play in Feb 2025 ([Android Authority](https://www.androidauthority.com/drastic-ds-emulator-removed-3526330/)), so the sheet's DraStic advice is outdated. |
| Dreamcast | **Flycast** (v2.7) first; Redream as an alternative | Flycast: Google Play, per its [README](https://github.com/flyinghead/flycast), or as a RetroArch core. Redream on Android: **UNVERIFIED**. The official download page lists only Windows/Mac/Linux/RPi 4, and the newest Android APK I found dates from Sep 2023. | 960p on the 3+ (RGC, sheet) |
| Saturn | **Yaba Sanshiro 2** | Google Play: **UNVERIFIED** (third-party listings show the Pro version last updated Dec 2021) | Sheet: Saturn runs "at 2x all without problems". It also says Pro adds light-gun support (**UNVERIFIED** elsewhere). |
| GameCube / Wii | **Dolphin** (official 2609a) plus the preinstalled **Dolphin for Handheld** | dolphin-emu.org or Google Play | See section 2 |
| PS2 | **NetherSX2 Classic (3668)**. RGC prefers it "for most devices"; its own FAQ says "use 3668 with Mali or less powerful devices". Alternative: **ARMSX2** (GPL-3.0; v2.9.1 released Oct 28, 2026). | NetherSX2: APK from GitHub releases (sideload). ARMSX2: GitHub, and on Google Play since Nov 2025 ([Android Authority](https://www.androidauthority.com/ps2-emulator-armsx2-play-store-3615585/)). | Hit-or-miss. RGC: start with the "Fast Preset", "100% EE Cycle Rate and no underclocking under EE Cycle Skip". ARMSX2 2.9's IOP Thread option "needs four performance cores"; the T618 has two. ARMSX2's speed on the T618 is **UNVERIFIED**. ([NetherSX2-patch](https://github.com/Trixarian/NetherSX2-patch), [ARMSX2 releases](https://github.com/ARMSX2/ARMSX2/releases)) |
| 3DS | **Citra MMJ** (weihuoya/citra; latest release tag 20251112, Nov 12, 2025) | GitHub | RGC lists Citra MMJ "for older handhelds" and Azahar from RP4/Pro up. Azahar requires "Android 10.0+ (64-bit)" and a "Snapdragon 835 SoC or better" ([Azahar README](https://github.com/azahar-emu/azahar)). Expect hit-or-miss results (sheet). ([weihuoya/citra releases](https://github.com/weihuoya/citra/releases)) |
| Switch, Wii U, PS3, Vita | **Not realistic on the 3+.** Use the S24-series phone. | — | RGC lists Switch (a Yuzu Android-10 build) and Vita3K starting from the **RP4/Pro** tier, not the 3+. The RP3+ sheet's Switch tab used the discontinued Skyline emulator, and most entries are rated Bad. Wii U and PS3 being out of reach on the T618 is my inference. Joey's list names Cemu (Wii U) and ARMSX3 (PS3) without device-specific claims. |

**Keeping GitHub apps updated:** **Obtainium** (latest tag v1.7.3) installs and updates apps from GitHub. RGC: "My preferred way to side-load apps is Obtainium." Joey recommends it too, and the Azahar README documents using it. It "does not set them up for you" (Joey).

---

## 5. Frontends (the "game library" app)

| Frontend | Status (Oct 2026) | Verdict for Wil |
|---|---|---|
| **Retroid's built-in launcher** | Preinstalled. RGC: "one of the best built-in launchers available on retro handheld devices." | **Start here.** |
| **Daijishō** | Free (**UNVERIFIED** for the current build). GitHub tags (TapiocaFox/Daijishou) stop at v1.5.0. APKMirror lists **1.8.1, uploaded Jan 30, 2026**. | Good free upgrade. RGC: "pretty great too!" |
| **ES-DE** | Paid. The official site says "The latest version is 3.5.0 (released 2026-09-30)". The Android release is "available via Patreon, Samsung Galaxy Store and Huawei AppGallery", not Google Play. Whether the Android build number is also 3.5.0 is **UNVERIFIED**. | RGC's favorite. More setup up front. |
| **Beacon** | Google Play, by "NERDS TAKE OVER". Third-party listings show **paid** (about $2.99), version 1.8.22 (**UNVERIFIED**). | Easier to set up, but "will take more maintenance" (RGC). |
| **Pegasus** | Newest GitHub tag is weekly_2024w38. | Not recommended; development looks stalled. |

Sources: [RGC](https://retrogamecorps.com/2022/01/16/retroid-pocket-2-starter-guide/), [ES-DE](https://www.es-de.org/), [Daijishō on APKMirror](https://www.apkmirror.com/apk/tapiocafox/daijisho/), [Beacon listing](https://clickyourapp.com/gb/insights/details/beacon-game-launcher/) (blocked direct fetch; seen via search), [mmatyas/pegasus-frontend](https://github.com/mmatyas/pegasus-frontend). Joey: choose the **AOSP Launcher** in the setup wizard if you plan to use Daijishō or ES-DE ([Joey](https://joeysretrohandhelds.com/guides/retroid-pocket-3-plus-setup-guide)).

---

## Getting games and BIOS files legally (Wil's own copies)

Wil asked for a hub where he could download games. **This report deliberately does not point to any ROM, ISO or BIOS download site.** The legal route is copying games and BIOS files he owns:

- **GameCube and Wii discs: [CleanRip](https://github.com/emukidid/cleanrip)** (latest tag 2.4). It makes "1:1 backups" of GameCube and Wii discs. It runs on a Wii through the Homebrew Channel, or on a GameCube through Swiss, and writes to USB or SD. The drive needs more than 1.35 GB free and can be NTFS or exFAT. Whether Dolphin needs a BIOS for Wii games is **UNVERIFIED** here.
- **PS2 BIOS: [biosdrain](https://github.com/F0bes/biosdrain)** (latest tag v2.2.2). Run `biosdrain.elf` from a FAT32/exFAT USB drive using uLaunchELF; the dump goes to the root of the USB drive. It can also write to a PC over PS2LINK. The author asks users not to share their BIOS files.
- **3DS cartridges and system files: [GodMode9](https://github.com/d0k3/GodMode9)** (latest tag v2.2.3). The README lists "Dump 3DS / NDS / DSi type retail game cartridges". Dumping boot9/boot11/OTP needs a boot9strap (custom-firmware) setup.
- **Free games:** legitimately free homebrew games work in these emulators. I did not research specific titles.

---

## Quick setup order for Wil

1. Check storage or RAM to learn which model he has (section 1).
2. Run the Retroid system update and turn off Battery Saver.
3. Keep the preinstalled **Dolphin for Handheld** and also install **official Dolphin**. If he ever removes the preinstalled one, he should not keep its data.
4. Set Dolphin to **Vulkan, 1x, Compile Shaders Before Starting ON**, and start with **Specialized** shaders. Then adjust each game using the [RP3+ sheet](https://docs.google.com/spreadsheets/d/1Vf7SIS7ecWa_J301h0mb2bxMWBMtKLvcpAFyaa5-LDc/htmlview), remembering that most of its tests used MMJR builds.
5. Use **Balance or Performance** mode, and **Extreme** only for Wii, GameCube and PS2.
6. Start with the built-in launcher. Move to Daijishō (free) or ES-DE (paid) later.
7. Play the heavy Wii games (Galaxy, DKC Returns, Xenoblade) on the S24-series phone instead.

## Sources
- Liliputing RP3+: https://liliputing.com/retroid-pocket-3-is-a-149-handheld-game-console-with-a-unisoc-t618-processor/
- Liliputing RP3: https://liliputing.com/retroid-pocket-3-handheld-retro-game-system-has-a-4-7-inch-display-unisoc-t310-chip-and-119-starting-price/
- Notebookcheck RP3+: https://www.notebookcheck.net/Retroid-Pocket-3-launches-with-performance-upgrades-in-multiple-colours.667092.0.html
- Notebookcheck Metal Edition: https://www.notebookcheck.com/Retroid-Pocket-3-Metal-Edition-Gaming-Handheld-startet-mit-Hall-Effekt-Joysticks.726236.0.html
- Reviewed.com: https://reviewed.com/gaming/content/retroid-pocket-3-plus-review
- DroiX specs: https://droix.net/blogs/en-gb/retroid-pocket-3-announced-specs-and-availability/
- DroiX setup: https://droix.net/knowledge-base/article/retroid-pocket-3-plus-and-flip/
- RetroCatalog: https://retrocatalog.com/retro-handhelds/retroid-pocket-3-plus
- RP3+ Compatibility Sheet: https://docs.google.com/spreadsheets/d/1Vf7SIS7ecWa_J301h0mb2bxMWBMtKLvcpAFyaa5-LDc/htmlview
- Retro Game Corps starter guide: https://retrogamecorps.com/2022/01/16/retroid-pocket-2-starter-guide/
- Joey RP3+ guide: https://joeysretrohandhelds.com/guides/retroid-pocket-3-plus-setup-guide
- Joey Dolphin guide: https://www.joeysretrohandhelds.com/guides/android-nintendo-gamecube-emulation-setup-guide-with-dolphin/
- Held Games Dolphin guide: https://heldgames.com/guides/dolphin-android-setup-guide
- RetroCompass: https://retrocompass.web.app/en/retroid/pocket-3-plus/troubleshooting
- Dolphin repo / README / strings.xml: https://github.com/dolphin-emu/dolphin , https://raw.githubusercontent.com/dolphin-emu/dolphin/master/Readme.md , https://raw.githubusercontent.com/dolphin-emu/dolphin/master/Source/Android/app/src/main/res/values/strings.xml
- UbuntuHandbook 2609: https://ubuntuhandbook.org/index.php/2026/09/dolphin-emulator-2609-released-with-android-netplay/
- Notebookcheck 2609: https://www.notebookcheck.net/Dolphin-Emulator-Android-update-adds-cross-platform-netplay-and-improved-rumble-amid-AI-attacks.1407268.0.html
- Dolphin forum threads: https://forums.dolphin-emu.org/Thread-unable-to-reinstall-dolphin-on-retroid-pocket-5 , https://forums.dolphin-emu.org/Thread-wii-mappings-for-ir-controls-stop-working-when-i-touch-the-screen , https://forums.dolphin-emu.org/Thread-solved-touchirpointer-disabled-when-device-sensors-enabled?pid=502732 , https://forums.dolphin-emu.org/Thread-dolphin-is-now-distributed-on-google-play-store-again?pid=476560
- MMJR2-VBI: https://github.com/Medard22/Dolphin-MMJR2-VBI
- Emulation General Wiki MMJR: https://emulation.gametechwiki.com/index.php/Dolphin_MMJR
- 9to5Google LineageOS RP6: https://9to5google.com/2026/07/01/the-retroid-pocket-6-now-officially-supports-lineageos/
- LineageOS RPN wiki: https://wiki.lineageos.org/devices/RPN/
- Android Authority Nova: https://androidauthority.com/retroid-pocket-nova-android-16-lineageos-3693722
- GammaOS: https://github.com/TheGammaSqueeze/GammaOS
- Google battery saver: https://support.google.com/android/answer/7664692?hl=en
- Android developer options: https://developer.android.com/studio/debug/dev-options
- DuckStation README: https://raw.githubusercontent.com/stenzek/duckstation/master/README.md ; Android Authority: https://www.androidauthority.com/duckstation-ends-android-support-3648430/
- DraStic removal: https://www.androidauthority.com/drastic-ds-emulator-removed-3526330/
- melonDS Android: https://github.com/rafaelvcaetano/melonDS-android
- PPSSPP: https://www.ppsspp.org/download/
- Flycast: https://github.com/flyinghead/flycast
- NetherSX2-patch: https://github.com/Trixarian/NetherSX2-patch
- ARMSX2: https://github.com/ARMSX2/ARMSX2/releases ; Play Store coverage: https://www.androidauthority.com/ps2-emulator-armsx2-play-store-3615585/
- Citra MMJ: https://github.com/weihuoya/citra/releases ; Azahar: https://github.com/azahar-emu/azahar
- ES-DE: https://www.es-de.org/
- Daijishō: https://www.apkmirror.com/apk/tapiocafox/daijisho/
- Pegasus: https://github.com/mmatyas/pegasus-frontend
- CleanRip: https://github.com/emukidid/cleanrip ; biosdrain: https://github.com/F0bes/biosdrain ; GodMode9: https://github.com/d0k3/GodMode9
- S24 chip by region: https://androidauthority.com/samsung-galaxy-s24-snapdragon-vs-exynos-countries-3402659
