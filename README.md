<div align="center">

<a href="https://alexgaoth.github.io/awesome-reverse-engineered/"><img src="assets/banner.svg" alt="Awesome Reverse-Engineered" width="100%"></a>

<p><b>English</b> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.fr.md">Français</a> · <a href="README.es.md">Español</a></p>

### 10,238 open-source tools that exist because someone reverse engineered a closed app, API, device, protocol, file format, game or AI product.

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) [![Projects](https://img.shields.io/badge/projects-10%2C238-ffb000?style=flat-square&labelColor=0e0f0d)](#whats-inside) [![Categories](https://img.shields.io/badge/categories-20-ffb000?style=flat-square&labelColor=0e0f0d)](#whats-inside) [![Nightly refresh](https://img.shields.io/github/actions/workflow/status/alexgaoth/awesome-reverse-engineered/refresh.yml?style=flat-square&label=nightly%20refresh&labelColor=0e0f0d)](.github/workflows/refresh.yml) [![Updated](https://img.shields.io/badge/updated-2026--10--13-30363d?style=flat-square&labelColor=0e0f0d)](data/entries.json) [![License: CC0](https://img.shields.io/badge/license-CC0-30363d?style=flat-square&labelColor=0e0f0d)](LICENSE)

[![Agent skill](https://img.shields.io/badge/agent%20skill-npx%20skills%20add-7ee787?style=flat-square&labelColor=0e0f0d)](#give-your-ai-agent-the-whole-index) [![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-d97757?style=flat-square&labelColor=0e0f0d)](#give-your-ai-agent-the-whole-index) [![Stars](https://img.shields.io/github/stars/alexgaoth/awesome-reverse-engineered?style=flat-square&labelColor=0e0f0d&color=ffb000)](https://github.com/alexgaoth/awesome-reverse-engineered/stargazers)

**[Search the index](https://alexgaoth.github.io/awesome-reverse-engineered/)** · **[Agent skill](#give-your-ai-agent-the-whole-index)** · **[Categories](#whats-inside)** · **[Hot this week](#hot-this-week)** · **[Add a project](#contributing)**

</div>

---

## Give your AI agent the whole index

When a task needs to talk to something with no official API (a smart plug, a car, a chat app, a file format), your agent searches this index, ranks by stars, activity and license, reads the README, and picks the right tool.

```bash
npx skills add alexgaoth/awesome-reverse-engineered
```

<details><summary><b>Other ways to install</b></summary>

**Claude Code plugin**

```
/plugin install reverse-engineered --marketplace alexgaoth/awesome-reverse-engineered
```

**Any agent or shell (one file, Python standard library only)**

```bash
curl -sL https://raw.githubusercontent.com/alexgaoth/awesome-reverse-engineered/main/plugin/skills/find-reverse-engineered/scripts/re_index.py -o re_index.py
python3 re_index.py search tuya local          # ranked matches
python3 re_index.py info make-all/tuya-local   # entry + README excerpt
python3 re_index.py clone make-all/tuya-local  # shallow clone into vendor/
```

</details>

<p align="center"><img src="assets/demo.svg" alt="find-reverse-engineered" width="820"></p>
<p align="center"><sub>Real output of the skill on the current data.</sub></p>

## Search it on the web

Filter 10,238 projects by category, language and health, sorted by stars or recent activity. Every search has a shareable link.

<p align="center"><a href="https://alexgaoth.github.io/awesome-reverse-engineered/"><img src="assets/site.png" alt="Search it on the web" width="820"></a></p>

<p align="center"><a href="https://alexgaoth.github.io/awesome-reverse-engineered/"><b>Open the search →</b></a></p>

## What's inside

**10,238 projects** with **9.9M** GitHub stars between them: 5,801 active, 1,587 slowing down, 1,955 dormant, 718 archived. Top languages: Python (2,590), C (1,502), C++ (1,443), JavaScript (611), TypeScript (537).

<p align="center"><img src="assets/categories.svg" alt="Projects per category" width="820"></p>

| Category | Projects | Top picks |
|---|--:|---|
| [**AI Tools & LLM Clients**](categories/ai-tools-llm-clients.md) | 683 | [claw-code](https://github.com/ultraworkers/claw-code), [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools), [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) |
| [**Game Decompilations & Reimplementations**](categories/game-decompilations-reimplementations.md) | 2,644 | [shadPS4](https://github.com/shadps4-emu/shadPS4), [RPCS3](https://github.com/RPCS3/rpcs3), [OpenRA](https://github.com/OpenRA/OpenRA) |
| [**Devices, IoT & Hardware**](categories/devices-iot-hardware.md) | 1,877 | [KOReader](https://github.com/koreader/koreader), [LibrePods](https://github.com/librepods-org/librepods), [OpenLogi](https://github.com/AprilNEA/OpenLogi) |
| [**Unofficial Web/App API Clients**](categories/unofficial-web-app-api-clients.md) | 653 | [yt-dlp](https://github.com/yt-dlp/yt-dlp), [youtube-dl](https://github.com/ytdl-org/youtube-dl), [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) |
| [**Messaging & Social Apps**](categories/messaging-social-apps.md) | 255 | [WeChatMsg](https://github.com/LC044/WeChatMsg), [ItChat](https://github.com/littlecodersh/ItChat), [wechaty](https://github.com/wechaty/wechaty) |
| [**Third-party Clients**](categories/third-party-clients.md) | 163 | [spotify-tui](https://github.com/Rigellute/spotify-tui), [nuclear](https://github.com/nukeop/nuclear), [SimpMusic](https://github.com/maxrave-dev/SimpMusic) |
| [**Chinese & Asian Platforms**](categories/chinese-asian-platforms.md) | 293 | [lx-music-desktop](https://github.com/lyswhut/lx-music-desktop), [alist](https://github.com/AlistGo/alist), [12306](https://github.com/testerSunshine/12306) |
| [**Apple Ecosystem**](categories/apple-ecosystem.md) | 326 | [fastlane](https://github.com/fastlane/fastlane), [homebridge](https://github.com/homebridge/homebridge), [OSX-KVM](https://github.com/kholia/OSX-KVM) |
| [**Drivers & Low-level Hardware**](categories/drivers-low-level-hardware.md) | 376 | [MonitorControl](https://github.com/MonitorControl/MonitorControl), [tinygrad](https://github.com/tinygrad/tinygrad), [G-Helper](https://github.com/seerge/g-helper) |
| [**Automotive**](categories/automotive.md) | 355 | [openpilot](https://github.com/commaai/openpilot), [evcc](https://github.com/evcc-io/evcc), [VESC firmware](https://github.com/vedderb/bldc) |
| [**Industrial & Building Automation**](categories/industrial-building-automation.md) | 196 | [HslCommunication](https://github.com/dathlin/HslCommunication), [plc4x](https://github.com/apache/plc4x), [IoTClient](https://github.com/zhaopeiym/IoTClient) |
| [**Firmware & Embedded**](categories/firmware-embedded.md) | 350 | [LEDE (Lean)](https://github.com/coolsnowwolf/lede), [OpenWrt](https://github.com/openwrt/openwrt), [Tasmota](https://github.com/arendst/Tasmota) |
| [**Network & Wire Protocols**](categories/network-wire-protocols.md) | 376 | [Sunshine](https://github.com/LizardByte/Sunshine), [moonlight-qt](https://github.com/moonlight-stream/moonlight-qt), [Impacket](https://github.com/fortra/impacket) |
| [**File Formats**](categories/file-formats.md) | 379 | [FFmpeg](https://github.com/FFmpeg/FFmpeg), [ImHex](https://github.com/WerWolv/ImHex), [SheetJS](https://github.com/SheetJS/sheetjs) |
| [**Online Service Revivals**](categories/online-service-revivals.md) | 168 | [NoLongerEvil Thermostat](https://github.com/codykociemba/NoLongerEvil-Thermostat), [Legacy Update](https://github.com/LegacyUpdate/LegacyUpdate), [wire-pod](https://github.com/kercre123/wire-pod) |
| [**Desktop Software Reimplementations**](categories/desktop-software-reimplementations.md) | 174 | [vaultwarden](https://github.com/dani-garcia/vaultwarden), [PhotoCraft](https://github.com/storytold/photocraft), [Proton](https://github.com/ValveSoftware/Proton) |
| [**Alternative Frontends**](categories/alternative-frontends.md) | 113 | [searxng](https://github.com/searxng/searxng), [searx](https://github.com/searx/searx), [Whoogle Search](https://github.com/benbusby/whoogle-search) |
| [**Mobile Apps**](categories/mobile-apps.md) | 86 | [revanced-manager](https://github.com/ReVanced/revanced-manager), [Metrolist](https://github.com/MetrolistGroup/Metrolist), [LibreTube](https://github.com/libre-tube/LibreTube) |
| [**RE Tooling**](categories/re-tooling.md) | 693 | [rea](https://github.com/morluto/rea), [Ghidra](https://github.com/NationalSecurityAgency/ghidra), [jadx](https://github.com/skylot/jadx) |
| [**Collections & Awesome Lists**](categories/collections-awesome-lists.md) | 78 | [awesome reverse-engineering (wtsxDev)](https://github.com/wtsxDev/reverse-engineering), [android-security-awesome](https://github.com/ashishb/android-security-awesome), [mendel5/alternative-front-ends](https://github.com/mendel5/alternative-front-ends) |

## Hot this week

The most-starred projects with commits in the last 7 days.

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | A feature-rich command-line audio/video downloader | 197,375 | 🟢 | Python |
| [claw-code](https://github.com/ultraworkers/claw-code) | Clean-room Rust/Python rewrite of the Claude Code agent harness after the source leak | 194,915 | 🟢 | Rust |
| [rea](https://github.com/morluto/rea) | Agentic tool to reverse engineer apps from behavior down to native binaries | 192,052 | 🟢 | TypeScript |
| [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Extracted system prompts and tool definitions for Cursor, Claude Code, Devin, Windsurf, Kiro, v0, Lovable and more | 143,992 | 🟢 |  |
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | NSA's software reverse engineering framework with decompiler | 85,939 | 🟢 | Java |
| [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Archive of extracted system prompts from ChatGPT, Claude, Gemini, Grok and others, per vendor with history | 69,540 | 🟢 | Python |
| [vaultwarden](https://github.com/dani-garcia/vaultwarden) | Unofficial Bitwarden-compatible server written in Rust | 68,967 | 🟢 | Rust |
| [gpt4free](https://github.com/xtekky/gpt4free) | Reverse-engineered third-party provider APIs giving free access to GPT-4 and other LLMs | 66,818 | 🟢 | Python |
| [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | Crawler for Xiaohongshu, Douyin, Kuaishou, Bilibili and Weibo posts and comments | 66,768 | 🟢 | Python |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Multimedia framework with many reverse-engineered proprietary codecs and containers | 65,091 | 🟢 | C |

## Just added

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [ps2-web-recomp](https://github.com/snuri00/ps2-web-recomp) | PS2 games statically recompiled to WebAssembly with a native runtime to run in the browser | 579 | 🟢 | C++ |
| [Black-2006-Recomp](https://github.com/portingpete/Black-2006-Recomp) | Native Windows static recompilation of BLACK (2006) for the original Xbox | 44 | 🟢 | C |
| [Little Planet](https://github.com/carlosrmz009/littleplanet) | Sonic CD (Mega-CD) byte-identical disassembly plus static recompilation into a native PC port | 28 | 🟢 | Assembly |
| [Geometry Wars: Retro Evolved 2 Recompiled](https://github.com/saulob/geometry-wars-retro-evolved-2-recompiled) | Native PC port of Geometry Wars: Retro Evolved 2 (Xbox 360) via static recompilation | 26 | 🟢 | C++ |
| [AVP Ports Index](https://github.com/edgytoast/avp-ports-index) | Link-only index of community game ports (decomps, recomps) running natively on Apple Vision Pro | 20 | 🟢 | Python |
| [LightCraft Android](https://github.com/artcraft-android/lightcraft-android) | Reimplementation of Adobe Lightroom in Rust with a Kotlin Android UI | 17 | 🟢 | Rust |
| [ffta-recomp](https://github.com/james2doyle/ffta-recomp) | Native recompilation of Final Fantasy Tactics Advance (GBA) built on the gbarecomp framework | 16 | 🟢 | Python |
| [TooTawersRecomp](https://github.com/Gumpolas/TooTawersRecomp) | Native Windows port of The Lord of the Rings: The Two Towers (Xbox, 2002) via static recompilation | 15 | 🟢 |  |
| [dw2003recomp](https://github.com/gascarcella/dw2003recomp) | Decompilation of Digimon World 2003 (PS1, EU) with reference tests; PC port in progress | 14 | 🟢 | C |
| [MailCraft](https://github.com/MonkeySaint/mailcraft) | Clean-room reimplementation of Microsoft Outlook (classic) in pure Rust | 14 | 🟢 | Rust |
| [asmsense](https://github.com/krxi/asmsense) | Small model that names and describes functions in stripped x86-64 binaries, with open dataset | 13 | 🟢 | Python |
| [defjam_recomp](https://github.com/comoria08/defjam_recomp) | Static recompilation of Def Jam: Fight for NY (Xbox) for Windows | 13 | 🟢 | C |
| [Glover-R](https://github.com/ThatGuyMcd/Glover-R) | Static recompilation of the N64 game Glover to native PC | 12 | 🟢 | Python |
| [WWE-SVR2008-RECOMP](https://github.com/nefariousjosiah/WWE-SVR2008-RECOMP) | Native PC port of WWE SmackDown vs. Raw 2008 (Xbox 360) via static recompilation | 12 | 🟢 | C++ |
| [WWE-SVR2009-RECOMP](https://github.com/nefariousjosiah/WWE-SVR2009-RECOMP) | Native PC port of WWE SmackDown vs. Raw 2009 (Xbox 360) via static recompilation | 12 | 🟢 | C++ |

## Most starred

| # | Project | What it does | ★ | Health | Lang |
|--:|---|---|--:|:-:|---|
| 1 | [yt-dlp](https://github.com/yt-dlp/yt-dlp) | A feature-rich command-line audio/video downloader | 197,375 | 🟢 | Python |
| 2 | [claw-code](https://github.com/ultraworkers/claw-code) | Clean-room Rust/Python rewrite of the Claude Code agent harness after the source leak | 194,915 | 🟢 | Rust |
| 3 | [rea](https://github.com/morluto/rea) | Agentic tool to reverse engineer apps from behavior down to native binaries | 192,052 | 🟢 | TypeScript |
| 4 | [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Extracted system prompts and tool definitions for Cursor, Claude Code, Devin, Windsurf, Kiro, v0, Lovable and more | 143,992 | 🟢 |  |
| 5 | [youtube-dl](https://github.com/ytdl-org/youtube-dl) | Command-line program to download videos from YouTube.com and other video sites | 141,287 | 🟢 | Python |
| 6 | [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | NSA's software reverse engineering framework with decompiler | 85,939 | 🟢 | Java |
| 7 | [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Archive of extracted system prompts from ChatGPT, Claude, Gemini, Grok and others, per vendor with history | 69,540 | 🟢 | Python |
| 8 | [vaultwarden](https://github.com/dani-garcia/vaultwarden) | Unofficial Bitwarden-compatible server written in Rust | 68,967 | 🟢 | Rust |
| 9 | [gpt4free](https://github.com/xtekky/gpt4free) | Reverse-engineered third-party provider APIs giving free access to GPT-4 and other LLMs | 66,818 | 🟢 | Python |
| 10 | [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | Crawler for Xiaohongshu, Douyin, Kuaishou, Bilibili and Weibo posts and comments | 66,768 | 🟢 | Python |
| 11 | [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Multimedia framework with many reverse-engineered proprietary codecs and containers | 65,091 | 🟢 | C |
| 12 | [openpilot](https://github.com/commaai/openpilot) | Open-source driver assistance system for 300+ car models | 63,891 | 🟢 | Python |
| 13 | [PhotoCraft](https://github.com/storytold/photocraft) | Clean-room Photoshop-style photo editor written from scratch in pure Rust | 56,243 | 🟢 | Rust |
| 14 | [ImHex](https://github.com/WerWolv/ImHex) | Hex editor for reverse engineers with a pattern language for binary formats | 55,127 | 🟢 | C++ |
| 15 | [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | Wraps Codex, Claude Code, Antigravity, Grok and Gemini CLI OAuth backends as OpenAI/Claude-compatible APIs | 55,055 | 🟢 | Go |
| 16 | [lx-music-desktop](https://github.com/lyswhut/lx-music-desktop) | LX Music: desktop music player aggregating Chinese music platform sources | 54,409 | 🟢 | TypeScript |
| 17 | [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | Leaked system prompts and tool specs for ChatGPT, Claude, Gemini, Grok, Perplexity, Cursor, Lovable, Replit and others | 51,183 | 🟢 |  |
| 18 | [jadx](https://github.com/skylot/jadx) | Dex to Java decompiler for Android apps | 50,892 | 🟢 | Java |
| 19 | [alist](https://github.com/AlistGo/alist) | AList: file list and WebDAV server that mounts many cloud drives through their private APIs | 50,285 | 🟢 | Go |
| 20 | [Spotube](https://github.com/team-spotube/spotube) | Cross-platform Spotify client that streams audio from other sources | 49,857 | 🟢 | Dart |
| 21 | [x64dbg](https://github.com/x64dbg/x64dbg) | Open source user-mode debugger for Windows | 49,831 | 🟢 | C++ |
| 22 | [mitmproxy](https://github.com/mitmproxy/mitmproxy) | Interactive TLS-capable intercepting HTTP proxy | 45,494 | 🟢 | Python |
| 23 | [sub2api](https://github.com/Wei-Shaw/sub2api) | Relay that exposes Claude, OpenAI, Gemini and Grok subscriptions as unified APIs | 43,885 | 🟢 | Go |
| 24 | [fastlane](https://github.com/fastlane/fastlane) | iOS/Android release automation; its spaceship module wraps Apple's private developer portal and App Store Connect APIs | 42,242 | 🟢 | Ruby |
| 25 | [Sunshine](https://github.com/LizardByte/Sunshine) | Self-hosted game stream host that implements the NVIDIA GameStream protocol for Moonlight clients | 42,178 | 🟢 | C++ |

## Health

| | Meaning |
|:-:|---|
| 🟢 | Active: pushed in the last 12 months |
| 🟡 | Slowing: last push 1 to 3 years ago |
| 🔴 | Dormant: no push for over 3 years |
| 🗄️ | Archived by its owner |
| ⚪ | Unknown: not hosted on GitHub |

Unofficial APIs break when the vendor changes their side, so check health before you depend on a project.

## How it's built

```mermaid
flowchart LR
  A[Research agents<br/>GitHub, HN, Reddit,<br/>awesome-lists] --> B[Scope filter<br/>interoperability only]
  B --> C[GitHub API check<br/>exists, stars, license]
  C --> D[(data/entries.json)]
  D --> E[README and<br/>category pages]
  D --> F[Search website]
  D --> G[Agent skill]
  H[Nightly refresh<br/>GitHub Action] -->|stars, archived,<br/>dead links| D
```

Raw data: [`data/entries.json`](data/entries.json). Removed repos: [`data/removed.json`](data/removed.json). Imported lists and searches: [SOURCES.md](SOURCES.md).

## Scope

This index lists **interoperability, preservation and research** projects: unofficial clients and SDKs, open drivers, local-control libraries, file-format parsers, protocol documentation, reimplementations and decompilations. Reverse engineering for interoperability is protected in many places (for example 17 U.S.C. §1201(f) and Article 6 of the EU Software Directive).

**Left out on purpose:** exploits and jailbreaks, security or certificate-pinning bypasses, decryption tools, cheats, DRM or paywall removal, CAPTCHA solvers, account bots and credential tools.

Using an unofficial client can break a service's terms of use. Use these projects with your own accounts, devices and data.

## Contributing

Know a project that belongs here? [Open an issue](https://github.com/alexgaoth/awesome-reverse-engineered/issues/new?title=Add%3A%20&body=Repo%3A%20%0AWhat%20it%20reverse%20engineers%3A%20) with the repo link and one line on what it reverse engineers, or send a PR that adds it to `data/entries.json`. Wrong category, dead link, or out of scope? Open an issue too.

Curated by [@alexgaoth](https://github.com/alexgaoth) with research agents. Every entry is checked against the GitHub API.

## Star history

<a href="https://star-history.com/#alexgaoth/awesome-reverse-engineered&Date"><img src="https://api.star-history.com/svg?repos=alexgaoth/awesome-reverse-engineered&type=Date" alt="Star history" width="600"></a>

## License

[CC0 1.0](LICENSE) for the list itself. Each linked project has its own license.

<div align="center">

**If this saved you from reverse engineering something yourself, [give it a star](https://github.com/alexgaoth/awesome-reverse-engineered).**

</div>
