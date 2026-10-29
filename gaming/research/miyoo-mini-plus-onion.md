IMPORTANT ADDENDUM: SEE THE OTA AND "4.3.1-1 IS 2+ YEARS OLD" NOTES BELOW.

# Miyoo Mini Plus improvements after installing Onion OS v4.3.x (fact-checked 2026-10-29)

I re-checked every claim against the pages linked here on 2026-10-29. Claims are marked as follows:
- **Confirmed** if the cited page says it.
- **Corrected** if the page says something different.
- **UNVERIFIED** if I could not confirm it from a primary source.

This report covers only the Miyoo Mini Plus. The Retroid Pocket 3/3+ and the Galaxy S24 need their own check.

Onion's docs site shows the label "Version: 4.3", with older doc sets for 4.2, 4.1 and 4.0. Source: https://onionui.github.io/docs/faq

**Where things stand (confirmed via the releases page and its Atom feed):**
- **v4.3.1-1 is the latest stable Onion release.** It was published **2024-06-24**, so it is more than two years old.
- **A newer pre-release exists:** V4.4.0-beta-20260120, published 2026-01-21. It adds:
  - RetroArch 1.22.2
  - CPU overclock hotkeys with an on-screen display, plus a Tweaks toggle to turn the hotkeys on or off
  - Real-time-clock detection for newer Mini Plus units
  - gpSP updated and made the default GBA core, with netplay support
- No stable Onion release has shipped in over two years. Allium and spruceOS are releasing more often (see section 6).
- Sources: https://github.com/OnionUI/Onion/releases and https://github.com/OnionUI/Onion/releases.atom

---

## 1. Which systems run well, and which struggle

**How to read Onion's markers** (confirmed, https://onionui.github.io/docs/emulators):
- **✔ Verified:** these systems are in Package Manager's "Verified" section and install to the Games tab.
- **⚠ Experimental:** these are in the "Expert" section and install to the Expert tab, which is hidden by default.
- A system is marked ⚠ when its integration is imperfect (for example, no automatic save states or no Game Switcher support), when it is slow, or when it is untested.

| System | Onion status | Emulator / cores (from Onion docs) | Notes | Source |
|---|---|---|---|---|
| Game Boy / Game Boy Color | ✔ | lr-gambatte, lr-gearboy, lr-tgbdual | In game, L2/R2 change the palette ("For GB only") | https://onionui.github.io/docs/emulators/handhelds, https://onionui.github.io/docs/apps/shortcuts |
| GBA | ✔ | lr-gpsp, lr-mgba, lr-meteor, lr-mednafen-gba, lr-vba_next | The docs say "The default GBA emulator on Onion is currently mGBA". gpSP is "preferable for the most demanding, slow or games requiring a better Fast Forward". `gba_bios.bin` is required for lr-gpsp and optional for the other cores | https://onionui.github.io/docs/emulators/gba |
| NES | ✔ | Not named on the consoles index page | | https://onionui.github.io/docs/emulators/consoles |
| SNES | ✔ | lr-mednafen-supafaust, snes9x, lr-snes9x2005PLUS, lr-snes9x2010, lr-snes9x2002, lr-snes9x2005 | "Bios: None". No default core is stated, and there are no performance notes | https://onionui.github.io/docs/emulators/snes |
| Genesis / Mega Drive | ✔ | lr-picodrive, lr-genesis_plus_gx | `bios_MD.bin` is optional. No default core is stated | https://onionui.github.io/docs/emulators/genesis |
| PS1 | ✔ | lr-pcsx-rearmed, km_duckswanstation_xtreme_amped, PCSX-ReARMed standalone | See the details below | https://onionui.github.io/docs/emulators/psx |
| Nintendo DS | ✔ | DraStic, "ported to Miyoo Mini by Steward-Fu" | See the details below | https://onionui.github.io/docs/emulators/nds |
| Others (all ✔) | ✔ | Neo Geo: lr_fbalpha2012_neogeo, GnGeo. Lynx: lr-handy, lr-mednafen_lynx. WonderSwan: lr-mednafen-wswan. Game Gear: lr-picodrive, lr-genesisplusgx, lr-gearsystem. NGP: lr-mednafen-ngp | Game Gear, Neo Geo Pocket, WonderSwan, Lynx, TurboGrafx-16, Neo Geo, Atari 2600/5200/7800 | https://onionui.github.io/docs/emulators/handhelds, https://onionui.github.io/docs/emulators/consoles |
| **N64, Dreamcast, PSP, Saturn** | **Not in Onion's docs** | none | See the details below | https://onionui.github.io/sitemap.xml, https://onionui.github.io/docs/emulators/add-ons/dreamcast-vmu, https://handheldindex.pages.dev/comparisons/miyoo-mini-plus-vs-rg35xx-plus/ |

**PS1 details** (https://onionui.github.io/docs/emulators/psx):
- "Most of PSX games run at 60 FPS natively on the Miyoo Mini."
- Turn off rewind and fast-forward for PS1, because "performance may suffer greatly".
- The standalone emulator performs better, but its integration is "not perfect : no automatic save states, no resume at boot, different shortcuts".
- DuckStation/SwanStation is "slower than PCSX" but runs a few games PCSX can't.

**Nintendo DS details:**
- DraStic is "the first standalone emulator (not RetroArch core) which is compatible with Onion game Switcher", and it supports resume at boot. No BIOS is needed. https://onionui.github.io/docs/emulators/nds
- Onion's DS page makes no performance claims.
- A third-party comparison rates DS "Variable / Choppy" and says "heavy 3D titles do not run". This is a community source, so it is **UNVERIFIED**. https://handheldindex.pages.dev/comparisons/miyoo-mini-plus-vs-rg35xx-plus/

**N64, Dreamcast, PSP and Saturn details:**
- Onion's sitemap has no page for any of these four systems.
- The only Dreamcast entry is "Dreamcast – VMU ⚠" (lr-vemulator). It emulates the VMU memory-card unit, not Dreamcast games.
- A third-party source rates N64 "Not practical / Broken" and Dreamcast "Not supported". That source doesn't mention PSP. These are community claims, not official.

**Bottom line:** the Mini Plus is very good up to PS1. DS works but varies by game (community reports). Play N64, Dreamcast and PSP on the Retroid or the S24.

---

## 2. Settings for smoothness and battery

### CPU clock (overclock)
- **Support:** overclocking is available "starting from Onion 4.2.0". The docs say "The speed improvement can be up to 20%". https://onionui.github.io/docs/faq
- **No menu in 4.3.** The RetroArch page says: "Onion's RetroArch includes overclocking feature. There's no UI for it currently." https://onionui.github.io/docs/apps/retroarch
- **How to set it by hand (confirmed in the FAQ):**
  - **All RetroArch cores:** create `RetroArch/cpuclock.txt` containing only a 4-digit MHz number, for example `1800`.
  - **One core:** put `cpuclock.txt` in that core's folder under `Saves/CurrentProfile/config/<core>/`.
  - Note: I did not confirm the exact example path `Saves/CurrentProfile/config/PCSX-ReARMed/` against the docs (**UNVERIFIED**).
- **Mini Plus limits (confirmed):** "1900Mhz (1800 recommended for optimal stability)". The docs also warn: "Using values higher than the recommended ones will impact stability or damage your device."
- **Advice:** overclock only the cores that need it, not everything. That a higher clock costs battery is **UNVERIFIED**; the docs don't say so.
- **Netplay:** it has its own overclock setting in `netplay_cores.conf`. https://onionui.github.io/docs/multiplayer
- **4.4 beta:** adds overclock hotkeys with an on-screen display. https://github.com/OnionUI/Onion/releases

### Core choice per system
- **GBA:** stay on mGBA, the 4.3 default. If a game is slow, or you want faster fast-forward, use the GLO menu to switch that game's core to gpSP. You can also install gpSP from Package Manager's Expert section.
  - gpSP needs your own `gba_bios.bin`.
  - The Scraper and Netplay pages say "press Y" to open GLO on a game. https://onionui.github.io/docs/emulators/gba, https://onionui.github.io/docs/apps/scraper
- **PS1:** use PCSX-ReARMed and overclock to 1800 for heavy games. Use the standalone version only if you accept losing auto-save and resume.
  - Some games slow down and crash unless SMC checks are disabled. The docs list Jedi Power Battles, Looney Tunes Sheep Raider (spelled "Sheep Rider" in the docs) and 2Xtreme/ESPN Extreme Games.
  - Fix: open the Quick Menu (MENU+SELECT), go to Options, and turn on "(Speed Hack) Disable SMC Checks".
  - Source: https://onionui.github.io/docs/emulators/psx
- **SNES and Genesis:** Onion lists the core options but gives no per-core speed comparison.
  - Retro Game Corps recommends Integer Scaling ("Native" in the options menu) for SNES performance.
  - That advice was written for **MinUI**, not Onion, so it is **UNVERIFIED for Onion**. https://retrogamecorps.com/2022/05/15/miyoo-mini-v2-guide/

### Frame skip and shaders
- Onion's docs recommend no frame-skip value. If you try frameskip, set it per game and save it as an override. Whether it helps on this device is **UNVERIFIED**.
- Onion's RetroArch page lists "Custom video filters" and bundled Jeltr0n overlays and filters. It does not mention shaders. That heavy filters cost performance is **UNVERIFIED**. https://onionui.github.io/docs/apps/retroarch

### Saving RetroArch changes the right way (confirmed)
- Apply changes through **Quick Menu › Overrides**. The FAQ says "Content Overrides are recommended over Core Overrides since some cores serve multiple systems". A Content Override applies to everything in the same ROM folder.
- **To reset:** use Tweaks › Advanced › Reset settings › Reset RetroArch main configuration. Resetting from inside RetroArch "will break Onion functionality".
- Sources: https://onionui.github.io/docs/faq, https://onionui.github.io/docs/apps/tweaks

### Tweaks app: options worth knowing
Source for all of these: https://onionui.github.io/docs/apps/tweaks
- **System › Startup › Auto-resume last game** (confirmed).
- **Low batt.: Save and exit** (confirmed).
- **Network › Disable services in-game:** "Disable all network services (except WiFi) while playing games". The page says this saves battery and keeps performance at a maximum. **Turn this on.**
- **Button shortcuts › Power single press** (confirmed).
- **Advanced:**
  - Fast forward rate.
  - PWM frequency: "a lower value will result in less 'whine' from the devices speaker". That it can cause flicker is **UNVERIFIED**; the docs don't say so.
  - LCD undervolt: "Use this option if you're seeing small artifacts on the display (MMP only)".
- **Tools (corrected list).** The 4.3 Tools section contains:
  - Generate CUE files for PSX games
  - Generate M3U files for PSX games
  - Generate game list for short name roms
  - Generate miyoogamelist with digest names
  - Screen recorder
  - Regenerate game switcher list
  - Sort applist A-Z / Z-A
- "Sort favorites, fix thumbnails, remove OSX system files" appear in the page's Features list, **not** under Tools. Where those options live in the menu is **UNVERIFIED**.

### Sleep, Game Switcher, save states
Sources: https://onionui.github.io/docs/apps/game-switcher, https://onionui.github.io/docs/apps/shortcuts, https://onionui.github.io/docs/faq, https://onionui.github.io/docs/emulators/nds
- **Game Switcher:** press MENU in game. It saves your place and shows your recent games and playtimes.
  - Below 4% battery, the device saves and exits automatically.
  - Below 15%, a red frame appears. You can change that threshold in Tweaks.
- **Sleep:** a single press of POWER.
- **Shutting down (confirmed):**
  - Hold POWER to save and turn off. This is the safe shutdown.
  - Hold for 5 seconds to force a shutdown.
  - Hold for 10 seconds to cut power completely (Mini Plus only).
- **Save-state keys (confirmed):**
  - MENU+R2 saves a state, MENU+L2 loads one, and MENU+Left/Right picks the slot.
  - Slot -1 "is reserved for Onion's Auto-Save feature".
  - "RetroArch will only retain the last 10 files" of incremental states.
- **Standalone emulators:** the Game Switcher page says "standalone emulators are not compatible". DraStic for DS is the documented exception.
- **After an Onion upgrade:** if games run at the wrong speed, the FAQ says to "create an in-game Save and then delete your Save States". Save states can be incompatible between core versions.
  - Practical advice: always make an in-game save before upgrading.

### Battery tips from the FAQ (confirmed)
https://onionui.github.io/docs/faq
- Keep brightness below about 70%.
- Use headphones: "the speaker is the most battery-hungry component!"
- Turn Wi-Fi off when you're not using it.
- Battery % is estimated from voltage, because there is no battery management system, so it fluctuates. That is normal.

---

## 3. Extras

### Package Manager (confirmed)
https://onionui.github.io/docs/apps/package-manager
- Three tabs: Verified, Apps, Expert.
- **X button:** since 4.3.0 it cycles between none, auto and all. "Auto" selects every emulator that has ROMs on the card (marked with a cartridge icon).
- Expert items appear only after you turn on **Tweaks › Appearance › Show expert mode**.
- "Removing an emulator or an app will not remove the associated roms and data."

### Ports Collection (confirmed)
https://onionui.github.io/docs/ports, repo https://github.com/OnionUI/Ports-Collection
- 61 ports in total. **24 are free and complete.**
- The other 37 are engines that need data files from games you own. Each has a `_required_files.txt` in `Roms/PORTS/Games/[Game folder]/` listing what you need.
- **To install:**
  1. Turn on Ports Collection in Package Manager › Verified.
  2. Download the 7z (the full collection or a single port).
  3. Extract it to the SD card root.

### Themes (confirmed)
- Onion has a Themes app that previews and applies themes. https://onionui.github.io/docs/features
- Get themes from https://github.com/OnionUI/Themes, which is active; themes were updated as recently as March 2025.
- To install: extract the theme into `Themes/`, or leave it zipped. The Themes app unpacks zips when you apply them.

### Box art: the Scraper app (Mini Plus only, needs Wi-Fi)
https://onionui.github.io/docs/apps/scraper
- **How to run it:** in the Games list select a ROM, press Y (GLO menu), then choose Scraper.
- **Sources:** ScreenScraper, LaunchBox or RetroArch.
  - ScreenScraper has the broadest coverage and can match by CRC.
  - A ScreenScraper account reduces errors and speeds up scraping.
- You can set a preferred region and media type, and run the scraper in the background.
- **Where images go:** the Scraper page doesn't say. The Advanced scraping page says images belong in `Roms/<gamesystem>/Imgs`, with a capital "I". https://onionui.github.io/docs/advanced/scraping
- For big collections, the docs say scraping on a PC with Skraper is "probably faster". https://onionui.github.io/docs/advanced/scraping

### RetroAchievements (works, with caveats)
- Onion's docs have no dedicated guide.
- A 2023 user discussion describes the setup:
  1. In RetroArch settings, turn on Achievements.
  2. Enter your RetroAchievements login.
  3. Save the config.
- If it works, a message such as "Achievements unlocked: 0 out of 250" appears when a game starts.
- The same thread reports that Wi-Fi plus RetroAchievements slowed performance for one user. https://github.com/OnionUI/Onion/discussions/1114
- Wi-Fi has to stay on while you play, which "will result in higher battery usage". https://techtactician.com/miyoo-mini-setup-starter-guide/
- **Wi-Fi band:** the Mini Plus connects only on **2.4 GHz**, so a 5 GHz-only network won't work. Check this first if achievements won't sync. Source: a community guide, https://handheldindex.pages.dev/firmware/onionos-setup-guide-miyoo-mini-plus/
  - The original report cited a RetroAchievements forum post (https://retroachievements.org/forums/topic/30636). It returned 403 Forbidden, so that report is **UNVERIFIED**.
- **Open bug, filed 2026-06-21 (confirmed):** RetroArch issue #19128, "Retroachievements doesn't work on miyoo mini+".
  - Reported setup: Onion 4.4.0-beta-20260120 with RetroArch 1.22.2.
  - Symptom: achievements get stuck on "starting session" or "identifying game".
  - The reporter's bisect says RetroArch 1.20.0 worked.
  - This is one more reason to stay on 4.3.1-1 for now. https://github.com/libretro/RetroArch/issues/19128

### Wi-Fi features
- **HTTP file server** (Tweaks › Network › HTTP):
  - Open the device's IP address in a browser to upload, download and edit files. It also has a terminal.
  - The default login is admin/admin. The docs recommend changing it at first login, and avoiding public or open Wi-Fi.
  - https://onionui.github.io/docs/network/http
- **FTP:**
  - The default login is onion/onion.
  - In FileZilla, set the transfer type to **Binary**, or binary files can be damaged.
  - Don't use FTP on open or public Wi-Fi; it is unencrypted.
  - https://onionui.github.io/docs/network/ftp
- **Also available:** Samba (default login onion/onion), SSH, Telnet, VNC, and Hotspot/WPS. https://onionui.github.io/docs/apps/tweaks, https://onionui.github.io/docs/network/samba
- **Time sync (corrected):** Tweaks › System › Date and time has "Set automatically via the internet", "Wait for sync on startup" and "Emulated time skip".
  - The FAQ says the Mini "does not have a built-in clock". By default Onion adds 4 hours to the clock at each boot; you can change this in Tweaks.
  - **However:** the 4.4 beta adds detection for a real-time clock on **newer Mini Plus units**. So "the Mini Plus has no hardware clock" may not be true for every unit.
  - Time sync matters for Pokémon-style clock games.
  - https://onionui.github.io/docs/apps/tweaks, https://onionui.github.io/docs/faq, https://github.com/OnionUI/Onion/releases
- **OTA update app:**
  - Install it from Package Manager (Mini Plus with Wi-Fi). It needs 1 GB free and runs `fsck.fat` before applying, "to avoid SD card FAT file system corruption".
  - **WARNING (new):** the docs say the app offers stable and beta channels, and **"The beta channel is the current default."**
  - To stay on 4.3.1-1, switch the OTA app to the **stable** channel before updating. Otherwise it may install the 4.4 beta.
  - https://onionui.github.io/docs/apps/ota-update
- **Netplay:** start it from the GLO menu (press Y on a game, then Netplay). There are three modes:
  - Standard Netplay over Wi-Fi.
  - Easy Netplay between two Mini Plus units in the same room.
  - Easy Netplay Pokémon trade/battle, for GB/GBC only.
  - https://onionui.github.io/docs/multiplayer

### Save sync
- Onion's docs list two community apps:
  - **Syncthing** by XK9274: "Sets up Syncthing and injects into Onion 4.2.0 beta runtime.sh". https://onionui.github.io/docs/apps/syncthing
  - **Cloud Saves** by hotcereal, which uses rclone. https://onionui.github.io/docs/apps/cloud-saves
- Neither docs page links to the app's own repository or states which Onion versions it supports.
- Whether either app works on 4.3.1-1 is **UNVERIFIED**.
- **The safe manual method (confirmed):** "Your saves and most of your preferences are now in /Saves … Simply copy this folder when you want to backup your data." https://onionui.github.io/docs/features

---

## 4. Avoiding SD-card corruption

- **Card:**
  - The installation guide says the included card "is known to be slow, and will likely ruin your experience and/or data". It recommends "reputable brands (e.g. SanDisk or Samsung)". https://onionui.github.io/docs/installation/fresh
  - The FAQ also says: "It is strongly advised not to use the Miyoo provided SD card or USB Card Reader". https://onionui.github.io/docs/faq
- **File system:** "Format your SD card as FAT32 (not exFAT!)." https://onionui.github.io/docs/installation/fresh
  - **Windows, card over 32 GB:** use Rufus (https://rufus.ie/). Settings:
    - Boot selection: Non bootable
    - Partition scheme: MBR
    - File system: Large FAT32
    - Cluster size: "Cluster size at 32 kilobytes should be fine (16 kilobytes might extend the life of your SD card)"
  - "We do not recommend using GUIFormat / fat32format, since many users are reporting file system errors on cards above 128 GB."
  - **Mac:** in Disk Utility, choose the root drive (not a partition), Format MS-DOS (FAT), Scheme Master Boot Record.
  - **Easier Windows option:** Onion Desktop Tools, a Windows PowerShell program. Its README says it can "format SD card in FAT32" and "download, install, update and configure Onion"; the latest linked release is v0.0.9. Onion's fresh-install page does not mention it, so this is a community tool. https://github.com/schmurtzm/Onion-Desktop-Tools/blob/main/README.md
- **Shutdown:** hold POWER, which saves and then turns off. Use the 5-second force shutdown only when the device is frozen. https://onionui.github.io/docs/apps/shortcuts
- **On the computer:** always eject the card before removing it.
  - The Allium README says "Eject the disk (important!)". Onion's install page doesn't say this. https://github.com/goweiwen/Allium
  - On a Mac, also remove macOS hidden files. Onion's Tweaks page lists "remove OSX system files" among its features, but the exact menu location is **UNVERIFIED** (it is not under Tools in the 4.3 docs). https://onionui.github.io/docs/apps/tweaks
- **Use Wi-Fi to avoid wear:** moving files with the HTTP, FTP or Samba server means you take the card out less often. This is a common-sense suggestion, not stated in the docs.
- **Backups:** copy `/Saves` to your PC regularly (confirmed). Also back up `BIOS/`; this is a reasonable suggestion, but the docs don't state it. https://onionui.github.io/docs/features

---

## 5. Firmware update (only needed if older than 20230505)

**1. Check your version** (confirmed, https://onionui.github.io/docs/installation):
- In Onion: Settings › About device › Firmware version.
- On stock firmware: Settings › Device Info › Version.
- The Mini Plus needs at least `20230505****`.
- Versions marked ✔ in Onion's list: 20230505 2130, 20230609 2122, 20230628 2128.
- Versions marked ⚠: 20230218 1113, 20230302 1817, 20230312 1739, 20230326 2339, 20230329 2051.
- If yours is ✔, there is no need to update. This is a reasonable inference; the docs list the versions but give no explicit "don't update" instruction.

**2. Download:**
- Onion's install page links Mini Plus firmware here: https://drive.google.com/drive/folders/1zPk9t10AiRsjYKjIRrg8XbPUh0Nm2ej0
- lomiyoo.com lists "0628 Firmware" for the Mini Plus. It presents itself as Miyoo's official site ("Official Firmware", support@lomiyoo.com, copyright "Miyoo"), but no legal entity is named. Its official status is **UNVERIFIED**. https://lomiyoo.com/pages/firmware
- Onion notes that its linked guide image contains an outdated lemiyoo.cn link. Use the links above instead.

**3. Steps.** These come from lomiyoo's "Standard Update Method" and the guide image linked from Onion. The image was made for the original Mini (`miyoo283_fw.img`). For the Mini Plus, community guides say the file is `miyoo354_fw.img`; this is **UNVERIFIED** from a primary source. https://retrohandhelds.gg/miyoo-mini-plus-setup-guide/
1. Back up the card. (Guide image: back up games, saves and BIOS.)
2. Format it FAT32. Neither the lomiyoo steps nor the guide image include this step, so it is **UNVERIFIED** as required.
3. Put the `.img` file in the card root, "do not place it inside any folder" (lomiyoo). That nothing else may be on the card is **UNVERIFIED**.
4. With the device **off**, insert the card and connect a USB charger.
5. Hold POWER. A rocket logo or "System Upgrade" screen appears (the guide image shows "System Upgrade" with a rocket). lomiyoo says the update takes about 5–8 minutes.
   - If it doesn't start: power off, then press and hold MENU and POWER together (lomiyoo).
6. **Don't touch the device or unplug it** until the charging screen appears (guide image: "DO NOT TOUCH", then "SAFE TO UNPLUG" at the Charging screen).
7. Afterwards, delete the `.img` file from the card (guide image, Part 3; Retro Game Corps).

Sources: https://lomiyoo.com/pages/firmware, the guide image https://user-images.githubusercontent.com/16885275/170205258-8add4be7-1a1e-4ae5-a8f2-cb13c6703e06.png, https://retrogamecorps.com/2022/05/15/miyoo-mini-v2-guide/

**Risks:**
- Onion: "We can't take responsibility if your device is bricked in the process of upgrading the firmware." https://onionui.github.io/docs/installation
- The guide image says: "Be careful not to lose power during the upgrade process or it may brick."
- The guide image also says to use a power plug "no more than 5V" and **not** a cable with USB-C on both ends.
- Retro Game Corps says to use "a 5W USB-A to USB-C cable" for the Mini Plus.
- Flash only if your version is ⚠ or older than 20230505.

---

## 6. Alternatives to Onion (all confirmed to support the Mini Plus)

| OS | Mini Plus support | Honest one-liner | Source |
|---|---|---|---|
| **MinUI** | Yes, status "Legacy" ("will be retired in a future update") | "No settings or configuration". The repo was **archived on Nov 27, 2025** and is read-only | https://github.com/shauninman/MinUI |
| **Allium** | Yes (Mini, Mini Plus, Mini Flip) | Latest release **v1.0.2, 2026-09-08**, with nightly builds as recent as 2026-10-26. Fewer features than Onion; "Metadata/box art scraper" is still under Planned Features | https://github.com/goweiwen/Allium, https://github.com/goweiwen/Allium/releases.atom |
| **spruceOS** | Yes. The v4.5.4 table says "Stable", no TF1 image required | Actively developed: v4.5.6 released 2026-10-26. Its notes add a Firmware Update feature that covers "Miyoo Mini Plus and Mini Flip OEM firmware" | https://github.com/spruceUI/spruceOS/releases, https://github.com/spruceUI/spruceOS/releases.atom |

**Recommendation:** stay on Onion 4.3.1-1. It has the most documented features for the Mini Plus: Wi-Fi tools, Scraper, Game Switcher, DS and Netplay.
- Hold off on the 4.4 beta until it is stable and the RetroAchievements bug is fixed.
- If you use the OTA app, switch it to the **stable** channel first.
- Onion's last stable release is from June 2024. If you want a more actively updated OS later, spruceOS is the one releasing most often. That is a judgment call, not a performance claim.

---

## Legal note on games and BIOS

- **Onion's exact BIOS file names:**
  - **PS1:** `PSXONPSP660.bin` (recommended), `scph101.bin`, `scph7001.bin`, `scph5501.bin`, `scph1001.bin`. Names are case-sensitive. https://onionui.github.io/docs/emulators/psx
  - **GBA:** `gba_bios.bin`, required only for lr-gpsp. https://onionui.github.io/docs/emulators/gba
- **Only use BIOS files dumped from hardware Wil owns.** Libretro's BIOS hub explains how to check a file by name, location and MD5 hash, and links to each core's BIOS page. It links to no downloads. https://docs.libretro.com/library/bios/
- **Dumping your own cartridges:** the open-source Sanni Cart Reader is "A shield for the Arduino Mega that can back up video game cartridges", ROMs and saves.
  - It lists NES/Famicom, SNES, N64, Game Boy Color, GBA, Mega Drive/Genesis and Master System.
  - The old repo is archived and says "We have moved, please visit us at https://github.com/oscartreader".
  - https://github.com/sanni/cartreader
- **Free legal games:** the 24 complete free ports in Onion's Ports Collection. https://onionui.github.io/docs/ports

---

## Sources
- https://github.com/OnionUI/Onion/releases
- https://github.com/OnionUI/Onion/releases.atom
- https://onionui.github.io/docs/faq
- https://onionui.github.io/docs/emulators
- https://onionui.github.io/docs/emulators/handhelds
- https://onionui.github.io/docs/emulators/consoles
- https://onionui.github.io/docs/emulators/gba
- https://onionui.github.io/docs/emulators/snes
- https://onionui.github.io/docs/emulators/genesis
- https://onionui.github.io/docs/emulators/psx
- https://onionui.github.io/docs/emulators/nds
- https://onionui.github.io/docs/emulators/add-ons/dreamcast-vmu
- https://onionui.github.io/sitemap.xml
- https://onionui.github.io/docs/apps/retroarch
- https://onionui.github.io/docs/apps/tweaks
- https://onionui.github.io/docs/apps/shortcuts
- https://onionui.github.io/docs/apps/game-switcher
- https://onionui.github.io/docs/apps/package-manager
- https://onionui.github.io/docs/apps/scraper
- https://onionui.github.io/docs/advanced/scraping
- https://onionui.github.io/docs/apps/ota-update
- https://onionui.github.io/docs/apps/syncthing
- https://onionui.github.io/docs/apps/cloud-saves
- https://onionui.github.io/docs/features
- https://onionui.github.io/docs/ports
- https://github.com/OnionUI/Ports-Collection
- https://github.com/OnionUI/Themes
- https://onionui.github.io/docs/network/http
- https://onionui.github.io/docs/network/ftp
- https://onionui.github.io/docs/network/samba
- https://onionui.github.io/docs/multiplayer
- https://onionui.github.io/docs/installation
- https://onionui.github.io/docs/installation/fresh
- https://github.com/schmurtzm/Onion-Desktop-Tools/blob/main/README.md
- https://rufus.ie/
- https://lomiyoo.com/pages/firmware
- https://user-images.githubusercontent.com/16885275/170205258-8add4be7-1a1e-4ae5-a8f2-cb13c6703e06.png
- https://retrogamecorps.com/2022/05/15/miyoo-mini-v2-guide/
- https://retrohandhelds.gg/miyoo-mini-plus-setup-guide/
- https://handheldindex.pages.dev/comparisons/miyoo-mini-plus-vs-rg35xx-plus/
- https://handheldindex.pages.dev/firmware/onionos-setup-guide-miyoo-mini-plus/
- https://github.com/OnionUI/Onion/discussions/1114
- https://techtactician.com/miyoo-mini-setup-starter-guide/
- https://github.com/libretro/RetroArch/issues/19128
- https://github.com/shauninman/MinUI
- https://github.com/goweiwen/Allium
- https://github.com/goweiwen/Allium/releases.atom
- https://github.com/spruceUI/spruceOS/releases
- https://github.com/spruceUI/spruceOS/releases.atom
- https://docs.libretro.com/library/bios/
- https://github.com/sanni/cartreader
- https://github.com/oscartreader