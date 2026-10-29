
# Samsung Galaxy S24 / S24+ / S24 Ultra as an emulation device (re-checked 2026-10-29)

**Before you start:** there is no "S24 Pro." Wil's phone is an S24, S24+ or S24 Ultra, and which one it is decides the chip inside. I re-checked every claim against official pages, GitHub release pages and news reports on 2026-10-29. Anything I could not confirm is marked **UNVERIFIED**. This report names no site that distributes ROMs, ISOs, BIOS files, keys or firmware.

---

## 1. Which chip he has, and why it matters

### Chip by model and region

| Model | Chip | GPU | Where it's sold |
|---|---|---|---|
| S24 Ultra | Snapdragon 8 Gen 3 for Galaxy | Adreno 750 | Every region |
| S24 / S24+ | Snapdragon 8 Gen 3 for Galaxy | Adreno 750 | Android Authority lists US, Canada, China, Taiwan and Hong Kong. Wikipedia says "North America and East Asia (China, Macau, Hong Kong, Taiwan, Japan)", excluding South Korea |
| S24 / S24+ | Exynos 2400 | Xclipse 940 (Wikipedia: based on AMD RDNA 3) | Everywhere else, including Europe, the UK, India and South Korea |
| S24 (India, from Sept 2025) | Snapdragon 8 Gen 3 | Adreno 750 | Wikipedia says a Snapdragon S24 went on sale in India from September 2025. The January 2024 Indian S24 used Exynos |
| S24 FE (a different phone) | Exynos 2400e | Xclipse 940 | Every region, including North America |

Sources: [Wikipedia: Samsung Galaxy S24](https://en.wikipedia.org/wiki/Samsung_Galaxy_S24), [Android Authority country list](https://androidauthority.com/samsung-galaxy-s24-snapdragon-vs-exynos-countries-3402659). Android Authority puts the UK on Exynos and notes that Qualcomm never published an exact country list. The earlier claim that "Qualcomm's own list reportedly included the UK" is **UNVERIFIED**: the PhoneArena page returned HTTP 403 when I tried to open it.

**RAM and storage.** Wikipedia gives:
- S24: 8 or 12 GB RAM; 128, 256 or 512 GB storage
- S24+: 12 GB RAM only; 256 or 512 GB
- S24 Ultra: 12 GB RAM only; 256 GB, 512 GB or 1 TB

Samsung's own UAE support page lists only 8 GB and 128/256 GB for the S24, so the S24 configurations differ by region ([Samsung AE](https://www.samsung.com/ae/support/mobile-devices/what-are-the-s24-external-memory-limits-and-memory-sizes-of-different-s24-variants/)). Check your own phone under Settings > About phone.

**If Wil bought the phone in the US, it has the Snapdragon chip whichever of the three models it is. The S24 FE is a different phone and uses Exynos.**

### How to check which one he has

1. Go to **Settings > About phone** and read the **Model number**.
   - **S921 = S24, S926 = S24+, S928 = S24 Ultra.** FCC-filing coverage lists SM-S926B/U as the S24+ and SM-S928B/U as the Ultra ([SammyFans](https://www.sammyfans.com/2023/11/30/samsung-galaxy-s24-series-gets-approval-for-launch-in-the-us/amp/), [iFixit S24+](https://www.ifixit.com/Device/Samsung_Galaxy_S24_Plus)). **S721 = S24 FE** (Samsung retailer link on [Wikipedia](https://en.wikipedia.org/wiki/Samsung_Galaxy_S24)).
   - Ending in **U** (for example SM-S921U) is the US model, which is Snapdragon ([SammyFans](https://www.sammyfans.com/2023/11/30/samsung-galaxy-s24-series-gets-approval-for-launch-in-the-us/amp/)). **U1** (US unlocked) and **W** (Canada) are also Snapdragon by the usual Samsung naming, but I only found retailer listings for these, so treat that as **UNVERIFIED**.
   - **SM-S9210** is the China/Hong Kong Snapdragon model ([phonemore](https://www.phonemore.com/models/samsung/galaxy-s24/), via search; the page itself returned HTTP 403).
   - Ending in **B** (for example SM-S921B or SM-S926B) is the international Exynos 2400 model ([SammyFans](https://www.sammyfans.com/2023/10/12/samsung-galaxy-s24-plus-with-exynos-2400-fails-to-fade-snapdragons-lead/)). **N** is the Korean model, which is Exynos per Wikipedia's "exc. South Korea" note (**UNVERIFIED** as a suffix rule).
2. Or install PPSSPP and open **Settings > Tools > System Information**, which shows the GPU name ([PPSSPP docs](https://www.ppsspp.org/docs/reference/custom-drivers/)). "Adreno 750" means Snapdragon. "Xclipse 940" means Exynos.

### Why the chip matters

- **Snapdragon (Adreno) phones can load custom GPU drivers.** Several Android emulators use libadrenotools to load a replacement Vulkan driver. The usual choice is **Mesa Turnip**, an open-source Adreno driver.
  - **Dolphin** added this in build 5.0-19611. Its progress report says libadrenotools lets users load open-source drivers that are "substantially better than their official counterparts" ([Dolphin Progress Report: May, June and July 2023](https://dolphin-emu.org/blog/6V); the page returned HTTP 403 to my fetcher, so I confirmed the wording through search results).
  - **PPSSPP** says Turnip "supports more features and extensions than the official driver" and that "performance varies but is often somewhat faster." These drivers "only apply to Vulkan, not OpenGL," and the feature exists in PPSSPP 1.17 and later ([PPSSPP custom drivers](https://www.ppsspp.org/docs/reference/custom-drivers/)).
  - **Vita3K:** in its Android Release 6 notes (June 2023), the Vita3K Android developer wrote, "I strongly recommend using turnip drivers on Adreno devices" ([Vita3K-Android releases](https://github.com/Vita3K/Vita3K-Android/releases)).
  - **ARMSX2 2.9** (Oct 26, 2026): first-run setup "offers the GPU driver ARMSX2 builds for your device: ARMSX2 Turnip on Adreno 6xx and 7xx," and "one tap downloads it." It is downloaded during setup, not bundled in the app ([ARMSX2 releases](https://github.com/ARMSX2/ARMSX2/releases)).
- **Exynos (Xclipse 940) phones cannot use custom drivers.** PPSSPP says the feature is for Adreno only, and on other GPUs "this option will simply not be visible" ([PPSSPP](https://www.ppsspp.org/docs/reference/custom-drivers/)).
- **Switch emulation is the risky case on Exynos.** Eden's system requirements page puts Exynos 2400 in its "Recommended" Android tier and Snapdragon 8 Gen 3 in its "Optimal" tier. The same page also says "most PowerVR and Xclipse GPUs are unsupported," which contradicts its own tiers ([Eden system requirements](https://eden-emu.dev/system-requirements)).
  - For RAM, Eden lists 8 GB as the Android minimum, 12 GB as recommended and 16 GB as optimal. **An 8 GB S24 only meets the minimum.**
  - The claim that one user ran many games on an Exynos S24 FE in Eden and Citron is **UNVERIFIED**: it is a single anecdote, and the Reddit mirror link (redlib.ssps.io) could not be reached from this session.
- **Dolphin on Exynos: use Vulkan.** The Dolphin wiki says "RDNA2 or Snapdragon based graphics processors give the best performance." It says OpenGL is "not recommended on current RDNA2 Android devices as they do not ship a dedicated OpenGL driver, and instead rely on ANGLE" ([Dolphin Performance Guide](https://wiki.dolphin-emu.org/index.php?title=Performance_Guide)). The wiki says RDNA2. That the same advice applies to the RDNA 3-based Xclipse 940 is a reasonable inference, not something the wiki states.

### Where to get Turnip driver packages (Snapdragon only)

| Project | Notes (checked Oct 29, 2026) |
|---|---|
| [K11MCH1/AdrenoToolsDrivers](https://github.com/K11MCH1/AdrenoToolsDrivers/releases/) | The source PPSSPP's docs link to. The README says it hosts drivers for Dolphin, PPSSPP, Vita3K and others. Latest release date: **UNVERIFIED**, because the page did not show it |
| [The412Banner/Banners-Turnip](https://github.com/The412Banner/Banners-Turnip) | "Automated bleeding-edge Mesa Turnip" builds. The Standard build is "compatible with Adreno 600–700 series," including 8 Gen 1–3. Latest build is tagged v27.0.0-20261029-r3 (Oct 29, 2026). Its "8 Gen 2 One UI" variant is for the Adreno 740, **not** the S24's Adreno 750 |
| [StevenMXZ/Adreno-Tools-Drivers](https://github.com/StevenMXZ/Adreno-Tools-Drivers) | A script that builds Turnip from Mesa every 2 weeks. Variants: A7xx, "A7xx OneUI Glitch", and two A8xx builds. The A8xx builds are for Adreno 8xx and are **not** for the S24. Whether the S24 needs the One UI variant is **UNVERIFIED** |

How to install, using PPSSPP's steps ([PPSSPP](https://www.ppsspp.org/docs/reference/custom-drivers/)):
1. Download the driver ZIP and **do not unzip it**.
2. In PPSSPP, open Settings > Tools > Developer Tools > **AdrenoTools Driver Manager**.
3. Choose **Install custom driver**, pick the ZIP, then press Select next to it.
4. To undo, choose **Default GPU Driver**.

Treat drivers as trial and error. If a game breaks, switch back to the stock driver.

---

## 2. What runs well on the S24, system by system

I found no published emulator benchmarks for the S24 itself. The ratings below come from each project's requirements and the chip tier, not from S24 frame-rate tests.

| System | Expected on Snapdragon 8 Gen 3 | Basis |
|---|---|---|
| NES through PS1, N64, Dreamcast, PSP | Should run comfortably | A 2026 guide lists "Good on mid-range and up: N64, Dreamcast, Saturn" ([heldgames](https://heldgames.com/guides/how-to-emulate-retro-games-on-android)). Per-game results are **UNVERIFIED** |
| Saturn | Playable, but accuracy varies | Yaba Sanshiro 2 got a major Android update in April 2025, its first significant one in over a year ([segasaturnshiro](https://www.segasaturnshiro.com/2025/04/18/yaba-sanshiro-updates-game-list-reviews-on-android/)). Whether it is still actively developed in Oct 2026 is **UNVERIFIED** |
| PS2 | Strong | ARMSX2 is active (2.9.1 on Oct 28, 2026) and lists "Custom Adreno and Mali drivers" ([ARMSX2](https://github.com/ARMSX2/ARMSX2)). Per-game FPS is **UNVERIFIED** |
| GameCube / Wii | Strong. Above native resolution should be possible (**UNVERIFIED**) | Dolphin wiki: Snapdragon GPUs "give the best performance" ([Dolphin](https://wiki.dolphin-emu.org/index.php?title=Performance_Guide)) |
| 3DS | Strong | Azahar is active (2126.2 stable, Oct 8, 2026) ([releases](https://github.com/azahar-emu/azahar/releases)) |
| PS Vita | Mixed. The emulator is experimental | Vita3K's Android build now ships from the main repo's continuous builds (Build 4242, Oct 29, 2026) ([Vita3K releases](https://github.com/Vita3K/Vita3K/releases)). A secondary 2026 article puts compatibility at about 56% playable, based mostly on PC results ([tech-insider](https://tech-insider.org/vita3k-android-emulateur-ps-vita-2026/)). Android-specific compatibility is **UNVERIFIED** |
| Switch | Some games playable, many are not. The S24's chip is in Eden's top tier | Eden puts Snapdragon 8 Gen 3 in its "Optimal" tier ([Eden](https://eden-emu.dev/system-requirements)) |

### Switch: which projects are maintained (late October 2026)

Background: Android Authority reported on Feb 13, 2026 that Nintendo had sent a DMCA notice the day before. It covered every Switch emulator on GitHub: the active ones (Eden, Citron, Kenji-NX, MeloNX) and inactive ones (Sudachi, Skyline). Citron and Eden moved their repositories to their own servers. The article warns that moving off GitHub can expose users "to malware from sketchy sources" ([Android Authority, Feb 13 2026](https://www.androidauthority.com/nintendo-switch-emulator-github-dmca-3640722/)). **Only download from the official sites below.**

| Project | Status (Oct 2026) | Official source |
|---|---|---|
| **Eden** (yuzu-based) | **Active. Best choice.** Stable v0.2.1 came out 2026-06-01. Nightly builds are still shipping; the latest I found is Oct 18, 2026. The v0.2.1 release has standard, optimized, legacy and chromeos Android APKs. The downloads page mentions Standard ("most users"), Legacy (Snapdragon 865 or older) and a "Genshin Spoof" APK for flagship devices. Needs Vulkan 1.1 and at least 8 GB RAM (12 GB recommended). | [eden-emu.dev/downloads](https://eden-emu.dev/downloads), [stable releases](https://git.eden-emu.dev/eden-emu/eden/releases), [nightly](https://git.eden-emu.dev/eden-ci/nightly/releases) |
| **Citron** | **Status unclear (UNVERIFIED).** Android Authority covered v0.11.0 in Nov 2025 ([AA](https://www.androidauthority.com/citron-switch-emulator-snapdragon-8-elite-3614894)). The "Pathfinder" update (about Feb 1, 2026) shipped an Android build, but its headline features were PC-only ([Android Authority](https://www.androidauthority.com/citron-pathfinder-update-3637142/)). citron-emu.org returned an empty page. A separate "Citron NEO" fork wrote on 2026-03-20 that "continuity of android support is on the line" ([newreleases](https://newreleases.io/project/github/citron-neo/emulator/release/2026-03-20)). | citron-emu.org (not checked) |
| **Kenji-NX** (Ryujinx-based) | **Status unclear (UNVERIFIED).** v2.1.0 shipped as an Android pre-release around Feb 11, 2026, with Snapdragon 8 Elite fixes and "up to 10%" better performance ([Android Authority](https://www.androidauthority.com/kenji-nx-android-emulator-updates-3639823/)). The official host (git.ryujinx.app) blocked automated access, so I found nothing newer. | git.ryujinx.app (per [Android Authority](https://www.androidauthority.com/nintendo-switch-emulator-github-dmca-3640722/)) |
| **Sudachi** | **Dead.** The last version came out July 2, 2025, and the developer says it is "no longer in-development." He recommends Eden and now contributes to it. | [Android Authority, Aug 25 2025](https://www.androidauthority.com/sudachi-end-development-3590776/) |
| **Torzu** | **Dormant (UNVERIFIED).** No 2026 release found. The GitHub page (github.com/litucks/torzu) now returns **HTTP 451 "Unavailable For Legal Reasons."** Do not hunt for copies. | none found |
| **Yuzu** | Shut down March 2024 in a $2.4M settlement with Nintendo | [PC Gamer](https://pcgamer.com/software/nintendo-v-yuzu-switch-emulator-shut-down-settlement) |
| **Skyline** | Development ceased in 2023 | [Android Authority](https://androidauthority.com/nintendo-switch-skyline-emulator-android-dead-3321391) |
| **Strato** (Skyline fork) | Never shipped a public release as far as I found; its lead developer left in March 2024. "Discontinued" is **UNVERIFIED** | [Emulation General wiki](https://emulation.gametechwiki.com/index.php/Strato) |

**Switch legal note:** Eden includes no firmware, keys or games. A 2026 guide says these files must come from your own console, dumped by you ([tech-insider (FR)](https://tech-insider.org/fr/eden-emulateur-switch-android-2026/)). Another guide says "your firmware needs to match the version of your prod.keys" ([joeysretrohandhelds](https://www.joeysretrohandhelds.com/guides/eden-android-setup-guide/)). Dumping them requires a Switch that can run homebrew, which many consoles cannot. The exact dumping steps are **UNVERIFIED** here.

---

## 3. Best emulator per system on Android, and where to install it

| System | Pick | Install from | Status / notes |
|---|---|---|---|
| **PS2** | **ARMSX2** | [GitHub releases](https://github.com/ARMSX2/ARMSX2/releases); latest **2.9.1 (Oct 28, 2026)**. Also on the Play Store: v2.6.5.1 was released to "GitHub and the Play Store" around Jul 25, 2026 ([Android Authority](https://www.androidauthority.com/armsx2-ps2-emulator-android-system-link-3691396/)). Whether 2.9.1 is on Play yet, and when Play distribution began, is **UNVERIFIED** | Open-source (GPL-3.0) and "based on PCSX2." Offers a Turnip download for Adreno 6xx/7xx on first run. Needs "a BIOS dump from a legitimately-owned PS2 console" ([README](https://github.com/ARMSX2/ARMSX2)) |
| PS2 (older option) | NetherSX2 | [Trixarian/NetherSX2-patch](https://github.com/Trixarian/NetherSX2-patch) | "Continuation of NetherSX2 based on AetherSX2 4248," which is closed-source. Stable v2.1 (Sep 27, 2025); dev v2.2n (Dec 25, 2025); no 2026 release. The repo now links prebuilt NetherSX2 APKs (earlier releases were patch-and-builder kits). The original AetherSX2 Play listing returns 404. **ARMSX2 is the better pick in 2026.** |
| PS2 (official PCSX2) | none | — | The ARMSX2 README says upstream PCSX2 ships only an ARM64 *interpreter* build, because its JIT recompilers "are x86-64 only." That is the gap ARMSX2 fills. I found no official PCSX2 Android app. |
| **GameCube / Wii** | **Dolphin** | Play Store (org.dolphinemu.dolphinemu), [F-Droid](https://f-droid.org/en/packages/org.dolphinemu.dolphinemu) or the official site. Latest tag **2609a (Oct 8, 2026)** ([tags](https://github.com/dolphin-emu/dolphin/tags)) | F-Droid still lists 2603a (added Mar 24, 2026). The current Play version is **UNVERIFIED**; a third-party tracker shows a June 25, 2026 update. Supports custom drivers. |
| **3DS** | **Azahar** (continues Citra) | Play Store (package `io.github.lime3ds.android`, which the README recommends), or the "vanilla" APK from [GitHub releases](https://github.com/azahar-emu/azahar/releases), which the README calls "technically superior." Latest stable **2126.2 (Oct 8, 2026)**; **2127.0 Alpha 3** came out Oct 16, 2026 | Azahar "continues the legacy of Citra" ([azahar-emu.org](https://azahar-emu.org/)). Neither the site nor the README mentions Lime3DS, apart from the package name. |
| **PS1** | **DuckStation**: still works, but gets no more Android updates | Play Store link in the [README](https://github.com/stenzek/duckstation) | On Mar 11, 2026 the developer said there will be no more Android updates ([Android Authority](https://www.androidauthority.com/p-3648430/)). The README says "No support is provided for the Android app." |
| PS1 alternatives | SwanStation or Beetle PSX HW cores in **RetroArch**; ePSXe (paid) | RetroArch: use the **APK from retroarch.com, not the Play Store**. The site says "The Google Play Store version has not been updated in over a year." Stable is **1.22.2** ([retroarch.com](https://www.retroarch.com/?page=platforms)) | An April 2026 forum post says SwanStation "didn't see much progress for a while" (**UNVERIFIED**). ePSXe 2.0.19 (May 2026) appeared in a search summary of epsxe.com, but I could not load the page, so **UNVERIFIED** ([epsxe.com/android](https://epsxe.com/android/)) |
| **PSP** | **PPSSPP** | Play Store (free, or paid Gold), APK or F-Droid. Latest **1.20.4** ([ppsspp.org](https://www.ppsspp.org/download/)) | Supports Adreno custom drivers from 1.17 on |
| **PS Vita** | **Vita3K** (experimental) | `android-latest.apk` from the main repo's "Automatic CI builds" release (Build 4242, Oct 29, 2026) ([Vita3K releases](https://github.com/Vita3K/Vita3K/releases)) | The separate Vita3K-Android repo stopped at Release 12 on **June 6, 2024** ([Vita3K-Android releases](https://github.com/Vita3K/Vita3K-Android/releases)), so don't use it. Turnip was recommended on Adreno back in 2023. The PS Vita firmware "can be downloaded from the official PlayStation website" ([Vita3K quickstart](https://vita3k.org/quickstart.html)) |
| **Switch** | **Eden** | [eden-emu.dev/downloads](https://eden-emu.dev/downloads) | See section 2 |
| **Dreamcast** | **Flycast** | Play Store (package `com.flycast.emulator`; v2.4 was titled "Google Play release") or [GitHub releases](https://github.com/flyinghead/flycast/releases). Latest **v2.7 (Aug 19, 2026)** | Active (v2.6 Jan 2026, v2.7 Aug 2026) |
| **Saturn** | **Yaba Sanshiro 2** (free, or paid Pro) | Play Store ([segasaturnshiro, Apr 2025](https://www.segasaturnshiro.com/2025/04/18/yaba-sanshiro-updates-game-list-reviews-on-android/)) | That article puts Pro at US$5. The current price is **UNVERIFIED** |
| **N64** | **Mupen64Plus FZ** (M64Plus FZ) | Play Store (package `org.mupen64plusae.v3.fzurita`, per secondary guides); source at [fzurita/mupen64plus-ae](https://github.com/fzurita/mupen64plus-ae) | A 2026 guide calls it a "mature dedicated N64 app available through Google Play" ([cloudspress](https://www.cloudspress.com/best-emulators-for-android-in-2026/)). Mupen64Plus-Next in RetroArch is an alternative (**UNVERIFIED**) |

### Getting games and BIOS files legally

Use dumps from games and consoles Wil owns, or free homebrew.

- **PS2 BIOS:** softmod the PS2 with FreeMcBoot (a memory card, about US$15) or FreeDVDBoot (free; a burned disc). Then copy **biosdrain.elf** to a FAT32 USB stick and run it from **uLaunchELF**. It writes files ending in .rom0, .rom1, .nvm and so on to the stick ([PCSX2 docs](https://pcsx2.net/docs/setup/bios/)).
- **GameCube / Wii discs:** run **CleanRip** on a Wii or vWii with the Homebrew Channel, or on a GameCube. It rips to SD or USB. USB Loader GX also works, but the wiki says "CleanRip is recommended." On a PC, certain Hitachi-LG Blu-ray drives flashed with OmniDrive can rip discs using redumper b699 or newer ([Dolphin wiki](https://wiki.dolphin-emu.org/index.php?title=Ripping_Games)).
- **3DS:** use **GodMode9** on a modded 3DS. Cartridges dump as `.trim.3ds`; installed titles go through Title manager > Build CIA. The output lands in `/gm9/out/` ([3ds.hacks.guide](https://3ds.hacks.guide/dumping-titles-and-game-cartridges)). Secondary sources say Azahar may need .3ds files renamed to .cci, or compressed to its Z3DS formats (.zcci and others) (**UNVERIFIED**; [joeysretrohandhelds](https://www.joeysretrohandhelds.com/guides/recommended-rom-file-types/)).
- **PS Vita:** on a Vita running HENkaku (firmware 3.60–3.65), use **GcToolKit** for cartridges or **VitaShell + FAGDec** ([Vita3K quickstart](https://vita3k.org/quickstart.html)).
- **PS1, Saturn, Dreamcast BIOS:** I did not verify the dumping tools (**UNVERIFIED**).

---

## 4. Samsung-specific tips

- **Gaming Hub.** Samsung says "all games downloaded from the app store are added to Gaming Hub by default." Other apps, such as sideloaded emulators, can be added by hand. The steps differ by version:
  - Samsung PH: My games > ⋮ > Add games > pick the app > Add to Gaming Hub ([Samsung PH](https://www.samsung.com/ph/support/apps-services/how-to-add-and-remove-apps-in-the-gaming-hub-app/)).
  - Samsung UK: My Games > Add Games > pick the app > + ([Samsung UK](https://www.samsung.com/uk/support/apps-services/how-to-delete-and-add-apps-in-the-game-launcher-app/)).

  Neither page says some third-party apps may not appear. Whether Game Booster's settings then apply to an emulator is **UNVERIFIED**.
- **Pause USB PD charging when gaming (bypass charging).** The phone runs off the charger instead of charging the battery, which keeps it cooler. Samsung's requirements:
  - a PD charger of 25 W or more with PPS (not included in the box)
  - a game running
  - at least 20% battery

  To turn it on: Gaming Hub > More > Game Booster > "Pause USB PD charging when gaming." Samsung says support "varies by model" ([Samsung AU](https://www.samsung.com/au/support/apps-services/pause-usb-pd-power-delivery-charging-when-gaming-feature-on-your-galaxy-device)). Samsung UK's supported-model list (dated Feb 2024) stops at the S23 ([Samsung UK](https://www.samsung.com/uk/support/mobile-devices/what-is-the-pause-usb-power-delivery-feature)). An S24 owner on Samsung's US community forum refers to the option, so it probably exists on the S24, but that is **UNVERIFIED** officially ([Samsung US community](https://us.community.samsung.com/t5/Galaxy-S24/Add-the-option-to-pause-power-delivery-as-a-general-setting/m-p/2830872)). Check whether the toggle appears with a PD charger connected.
- **Game Optimization Service (GOS).** GOS limits performance in games. After the 2022 throttling controversy, Samsung added user control: a "game performance management mode" in Game Booster ([9to5Google, Mar 2022](https://9to5google.com/2022/03/10/samsung-gos-update-coming-throttling/)). In Feb 2024, a Game Booster update fixed an S24 bug where Genshin Impact ran at the same frame rate with GOS on or off ([SamMobile](https://sammobile.com/news/game-booster-update-fixes-genshin-impact-galaxy-s24-performance-issues), confirmed via search results because the page returned HTTP 403). Whether fully disabling GOS still needs ADB commands is **UNVERIFIED**, and I wouldn't recommend that for a beginner anyway.
- **Performance profile.** It is at Settings > Device care > Performance profile. Leave it on **Standard**. Samsung says "Light performance mode is automatically disabled while playing games" ([Samsung UK](https://www.samsung.com/uk/support/mobile-devices/how-to-use-galaxy-s24-light-mode)). I found no current S24 setting called "Adaptive performance" (**UNVERIFIED**).
- **Heat (general advice, UNVERIFIED for the S24 specifically).** Take the case off during long sessions, use bypass charging, and cap frame rate or internal resolution rather than running at maximum. I found no source that measured sustained throttling on the S24.
- **Controllers.**
  - **Backbone One (USB-C):** Backbone's help page requires Android 10 or later, USB-C and USB OTG. A retailer Q&A says the S24 Ultra fits, and Verizon lists the S24 Ultra as supported. Thick cases may not fit. One Samsung community user reported that it stopped working on an S24 Ultra after the Android 15 (One UI 7) update. These came via search results; the pages themselves returned 403/503 ([Backbone help](https://help.backbone.com/hc/en-us/articles/13658397209367-Which-Android-phones-are-compatible-with-the-Backbone-One), [digitec Q&A](https://www.digitec.ch/en/s1/questionandanswer/will-the-samsung-galaxy-s24-ultra-fit-in-749680), [Samsung community](https://eu.community.samsung.com/t5/galaxy-s24-series/backbone-one-usb-c/m-p/13023781/highlight/true)).
  - **GameSir and 8BitDo** USB-C or Bluetooth controllers are commonly used, but I did not verify S24 compatibility (**UNVERIFIED**).
  - **Real Wii Remotes in Dolphin on Android:** forum posts from 2017 and 2020 say to connect a **Mayflash DolphinBar** over USB and set the Wii Remote option to the DolphinBar / real Wii Remote. Plain Bluetooth pairing didn't work on stock Android then ([Dolphin forums](https://forums.dolphin-emu.org/Thread-how-to-conect-real-dolphin-bar-in-android)). This is **UNVERIFIED** for 2026.
- **Storage.** The S24 has **no microSD slot**. Samsung says the series "does not support expandable storage via microSD cards" ([Samsung support](https://www.samsung.com/ae/support/mobile-devices/what-are-the-s24-external-memory-limits-and-memory-sizes-of-different-s24-variants/)).
  - On a 128 GB S24, PS2, GameCube/Wii and Switch libraries will fill the phone quickly.
  - Azahar's Z3DS compression shrinks 3DS files. One example given is 350 MB down to 242 MB ([Eneba news](https://www.eneba.com/hub/news/3ds-emulator-azahar-hits-release-milestone/), [Android Authority](https://androidauthority.com/azahar-2123-3ds-emulator-full-release-3588435)).
  - The claim that only .chd files work with Yaba Sanshiro launched from ES-DE has no source (**UNVERIFIED**).
  - A USB-C flash drive is an option, but whether each emulator can load games from one is **UNVERIFIED**.

---

## 5. Dolphin settings for Snapdragon 8 Gen 3

**I found no published Dolphin benchmark for the S24 or the 8 Gen 3.** The resolution numbers below are starting points to test, not measured results (**UNVERIFIED**). The setting descriptions come from the [Dolphin Performance Guide](https://wiki.dolphin-emu.org/index.php?title=Performance_Guide) unless noted.

| Setting | Recommendation | Why (per Dolphin wiki) |
|---|---|---|
| Video backend | **Vulkan** | Needed for custom drivers. OpenGL is "not recommended on current RDNA2 Android devices" because they rely on ANGLE |
| GPU driver (Snapdragon only) | Start on the system driver. Try a Turnip build if you see glitches or slowdowns | Custom driver support since 5.0-19611 ([blog](https://dolphin-emu.org/blog/6V)) |
| Internal resolution | **Start at 2x.** Try 3x per game while watching FPS. The "2x ≈ 720p, 3x ≈ 1080p" mapping is **UNVERIFIED** | The wiki warns "even setting the Internal Resolution to 2x may result in noticeable slowdown" on weaker hardware |
| Shader compilation | **Hybrid Ubershaders**, optionally with "Compile Shaders Before Starting" | Hybrid cuts stutter. Exclusive Ubershaders are "incredibly demanding at higher resolutions." Pre-compiling "may result in a lengthy wait to boot a game" |
| Dual Core | On (default) | "A powerful option for gaining performance." It can cause crashes, and Dolphin usually disables it for sensitive games |
| DSP | DSP-HLE | "DSP-HLE is many times faster" and safe in about 99% of games |
| CPU clock override | 100% | Going below 100% "can cause the game itself to lag" |
| Store EFB Copies to Texture Only | On (default) | The wiki calls it fairly demanding. Many games need it off; Dolphin's per-game defaults handle most of these |
| Skip EFB Access from CPU | Leave at the game's default | Speeds up games that read the screen, but can make games that rely on it unplayable |
| Texture Cache | Fast | "Can improve performance greatly, but it may cause graphical glitches" |
| Skip Presenting Duplicate Frames | **Off** | "On more powerful graphics cards, you want this unchecked" for better frame pacing |
| Anisotropic filtering | 4x–16x | "Does not usually impact performance" |
| Anti-aliasing (MSAA/SSAA) | Off at first | Comes "at the cost of increased GPU usage" |

**Wii games:** the same settings apply. If one game misbehaves, change that game's settings only. Dolphin's bug tracker confirms that long-pressing a game on Android opens game-specific overrides ([Dolphin issue #10897](https://bugs.dolphin-emu.org/issues/10897)). The exact menu label ("Properties > Edit Game Settings", per a third-party guide) is **UNVERIFIED**.

---

## Bottom line for Wil

1. **Check the model number first.**
   - Ending in **U** (US): Snapdragon. You get the full custom-driver options.
   - Ending in **B** (international): Exynos. Still capable, but no Turnip drivers, and Switch emulation is riskier.
   - An 8 GB S24 meets only Eden's minimum RAM.
2. **Core apps to install, from official sources only:**
   - **Dolphin** (GameCube/Wii)
   - **ARMSX2** (PS2)
   - **Azahar** (3DS)
   - **PPSSPP** (PSP)
   - **Eden** (Switch), from eden-emu.dev only
   - **RetroArch**, the APK from retroarch.com, for older systems
   - **Flycast** (Dreamcast)
   - **Yaba Sanshiro 2** (Saturn)
   - **Mupen64Plus FZ** (N64)
   - **Vita3K** (Vita, experimental), the `android-latest.apk` from the main Vita3K GitHub releases, not the old Vita3K-Android repo
3. **Avoid** Sudachi (dead), Torzu (GitHub page blocked for legal reasons), NetherSX2 (built on closed-source AetherSX2) and any unofficial "repack" or mirror sites.
4. **Storage is fixed**, with no SD card, so plan the game library around free space on the phone.

## Sources
- https://en.wikipedia.org/wiki/Samsung_Galaxy_S24
- https://androidauthority.com/samsung-galaxy-s24-snapdragon-vs-exynos-countries-3402659
- https://www.sammyfans.com/2023/11/30/samsung-galaxy-s24-series-gets-approval-for-launch-in-the-us/amp/
- https://www.sammyfans.com/2023/10/12/samsung-galaxy-s24-plus-with-exynos-2400-fails-to-fade-snapdragons-lead/
- https://www.ifixit.com/Device/Samsung_Galaxy_S24_Plus
- https://www.phonemore.com/models/samsung/galaxy-s24/
- https://www.ppsspp.org/docs/reference/custom-drivers/
- https://www.ppsspp.org/download/
- https://dolphin-emu.org/blog/6V
- https://wiki.dolphin-emu.org/index.php?title=Performance_Guide
- https://wiki.dolphin-emu.org/index.php?title=Ripping_Games
- https://github.com/dolphin-emu/dolphin/tags
- https://f-droid.org/en/packages/org.dolphinemu.dolphinemu
- https://bugs.dolphin-emu.org/issues/10897
- https://forums.dolphin-emu.org/Thread-how-to-conect-real-dolphin-bar-in-android
- https://github.com/ARMSX2/ARMSX2 and https://github.com/ARMSX2/ARMSX2/releases
- https://www.androidauthority.com/armsx2-ps2-emulator-android-system-link-3691396/
- https://github.com/Trixarian/NetherSX2-patch
- https://eden-emu.dev/system-requirements, https://eden-emu.dev/downloads, https://git.eden-emu.dev/eden-emu/eden/releases, https://git.eden-emu.dev/eden-ci/nightly/releases
- https://www.androidauthority.com/nintendo-switch-emulator-github-dmca-3640722/
- https://www.androidauthority.com/citron-pathfinder-update-3637142/
- https://www.androidauthority.com/citron-switch-emulator-snapdragon-8-elite-3614894
- https://newreleases.io/project/github/citron-neo/emulator/release/2026-03-20
- https://www.androidauthority.com/kenji-nx-android-emulator-updates-3639823/
- https://www.androidauthority.com/sudachi-end-development-3590776/
- https://pcgamer.com/software/nintendo-v-yuzu-switch-emulator-shut-down-settlement
- https://androidauthority.com/nintendo-switch-skyline-emulator-android-dead-3321391
- https://emulation.gametechwiki.com/index.php/Strato
- https://github.com/azahar-emu/azahar and https://github.com/azahar-emu/azahar/releases, https://azahar-emu.org/
- https://www.eneba.com/hub/news/3ds-emulator-azahar-hits-release-milestone/
- https://androidauthority.com/azahar-2123-3ds-emulator-full-release-3588435
- https://www.joeysretrohandhelds.com/guides/recommended-rom-file-types/
- https://github.com/stenzek/duckstation
- https://www.androidauthority.com/p-3648430/
- https://www.retroarch.com/?page=platforms
- https://epsxe.com/android/
- https://github.com/Vita3K/Vita3K/releases, https://github.com/Vita3K/Vita3K-Android/releases, https://vita3k.org/quickstart.html
- https://tech-insider.org/vita3k-android-emulateur-ps-vita-2026/
- https://github.com/flyinghead/flycast/releases
- https://www.segasaturnshiro.com/2025/04/18/yaba-sanshiro-updates-game-list-reviews-on-android/
- https://github.com/fzurita/mupen64plus-ae
- https://www.cloudspress.com/best-emulators-for-android-in-2026/
- https://heldgames.com/guides/how-to-emulate-retro-games-on-android
- https://pcsx2.net/docs/setup/bios/
- https://3ds.hacks.guide/dumping-titles-and-game-cartridges
- https://tech-insider.org/fr/eden-emulateur-switch-android-2026/
- https://www.joeysretrohandhelds.com/guides/eden-android-setup-guide/
- https://github.com/K11MCH1/AdrenoToolsDrivers, https://github.com/The412Banner/Banners-Turnip, https://github.com/StevenMXZ/Adreno-Tools-Drivers
- https://www.samsung.com/ae/support/mobile-devices/what-are-the-s24-external-memory-limits-and-memory-sizes-of-different-s24-variants/
- https://www.samsung.com/au/support/apps-services/pause-usb-pd-power-delivery-charging-when-gaming-feature-on-your-galaxy-device
- https://www.samsung.com/uk/support/mobile-devices/what-is-the-pause-usb-power-delivery-feature
- https://us.community.samsung.com/t5/Galaxy-S24/Add-the-option-to-pause-power-delivery-as-a-general-setting/m-p/2830872
- https://www.samsung.com/ph/support/apps-services/how-to-add-and-remove-apps-in-the-gaming-hub-app/
- https://www.samsung.com/uk/support/apps-services/how-to-delete-and-add-apps-in-the-game-launcher-app/
- https://www.samsung.com/uk/support/mobile-devices/how-to-use-galaxy-s24-light-mode
- https://9to5google.com/2022/03/10/samsung-gos-update-coming-throttling/
- https://sammobile.com/news/game-booster-update-fixes-genshin-impact-galaxy-s24-performance-issues
- https://help.backbone.com/hc/en-us/articles/13658397209367-Which-Android-phones-are-compatible-with-the-Backbone-One
- https://www.digitec.ch/en/s1/questionandanswer/will-the-samsung-galaxy-s24-ultra-fit-in-749680
- https://eu.community.samsung.com/t5/galaxy-s24-series/backbone-one-usb-c/m-p/13023781/highlight/true
