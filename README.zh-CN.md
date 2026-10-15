<div align="center">

<a href="https://alexgaoth.github.io/awesome-reverse-engineered/"><img src="assets/banner.svg" alt="Awesome Reverse-Engineered" width="100%"></a>

<p><a href="README.md">English</a> · <b>简体中文</b> · <a href="README.fr.md">Français</a> · <a href="README.es.md">Español</a></p>

## 同一个东西，不必逆向两次。

12,880 个开源工具，它们之所以存在，是因为有人逆向了某个封闭的应用、API、设备、协议、文件格式、游戏或 AI 产品。

**[搜索索引](https://alexgaoth.github.io/awesome-reverse-engineered/)**，或者交给你的智能体：`npx skills add alexgaoth/awesome-reverse-engineered`

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) [![Projects](https://img.shields.io/badge/projects-12%2C880-ffb000?style=flat-square&labelColor=0e0f0d)](#收录内容) [![Nightly refresh](https://img.shields.io/github/actions/workflow/status/alexgaoth/awesome-reverse-engineered/refresh.yml?style=flat-square&label=nightly%20refresh&labelColor=0e0f0d)](.github/workflows/refresh.yml) [![Stars](https://img.shields.io/github/stars/alexgaoth/awesome-reverse-engineered?style=flat-square&labelColor=0e0f0d&color=ffb000)](https://github.com/alexgaoth/awesome-reverse-engineered/stargazers) [![License: MIT + CC0 data](https://img.shields.io/badge/license-MIT%20%2B%20CC0%20data-30363d?style=flat-square&labelColor=0e0f0d)](LICENSE)

**[智能体技能](#让你的-ai-智能体使用整个索引)** · **[分类](#收录内容)** · **[本周热门](#本周热门)** · **[提交项目](#参与贡献)**

<sub>项目名称和描述保留英文原文。 · 社区：<a href="https://linux.do">LINUX DO</a></sub>

</div>

---

## 动手逆向之前

有了智能体，以及 [REA](https://github.com/morluto/rea)、[Ghidra](https://github.com/NationalSecurityAgency/ghidra) 这样的工具，逆向工程比以往任何时候都快。但你准备拆解的应用、API、设备或文件格式，往往已经有人做过，成果就放在某个没人链接的仓库里。

1. **先搜索。** 用[网站](https://alexgaoth.github.io/awesome-reverse-engineered/)或[智能体技能](#让你的-ai-智能体使用整个索引)，按产品、厂商或协议搜索。
2. **找到了？** 直接用、帮忙修，有问题向上游反馈。一个持续维护的客户端，胜过十个私人脚本。
3. **没找到？** 自己动手，以开源形式发布，然后[提交到这里](#参与贡献)，让下一个人从你停下的地方继续。

## 收录内容

共 **12,880 个项目**，合计 **10.5M** 个 GitHub 星标：活跃 7,086 个，放缓 1,961 个，停滞 2,488 个，已归档 897 个。主要语言：Python (3,299), C++ (1,867), C (1,694), JavaScript (840), TypeScript (736)。

| 分类 | 项目数 | 精选 |
|---|--:|---|
| [**AI 工具与大模型客户端**](categories/ai-tools-llm-clients.md) | 739 | [claw-code](https://github.com/ultraworkers/claw-code), [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools), [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) |
| [**游戏反编译与重新实现**](categories/game-decompilations-reimplementations.md) | 3,043 | [shadPS4](https://github.com/shadps4-emu/shadPS4), [v86](https://github.com/copy/v86), [RPCS3](https://github.com/RPCS3/rpcs3) |
| [**设备、物联网与硬件**](categories/devices-iot-hardware.md) | 3,029 | [KOReader](https://github.com/koreader/koreader), [LibrePods](https://github.com/librepods-org/librepods), [OpenLogi](https://github.com/AprilNEA/OpenLogi) |
| [**非官方 Web/应用 API 客户端**](categories/unofficial-web-app-api-clients.md) | 904 | [yt-dlp](https://github.com/yt-dlp/yt-dlp), [youtube-dl](https://github.com/ytdl-org/youtube-dl), [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) |
| [**即时通讯与社交应用**](categories/messaging-social-apps.md) | 296 | [WeChatMsg](https://github.com/LC044/WeChatMsg), [ItChat](https://github.com/littlecodersh/ItChat), [wechaty](https://github.com/wechaty/wechaty) |
| [**第三方客户端**](categories/third-party-clients.md) | 190 | [spotify-tui](https://github.com/Rigellute/spotify-tui), [nuclear](https://github.com/nukeop/nuclear), [SimpMusic](https://github.com/maxrave-dev/SimpMusic) |
| [**中国及亚洲平台**](categories/chinese-asian-platforms.md) | 324 | [lx-music-desktop](https://github.com/lyswhut/lx-music-desktop), [alist](https://github.com/AlistGo/alist), [12306](https://github.com/testerSunshine/12306) |
| [**苹果生态**](categories/apple-ecosystem.md) | 340 | [fastlane](https://github.com/fastlane/fastlane), [homebridge](https://github.com/homebridge/homebridge), [OSX-KVM](https://github.com/kholia/OSX-KVM) |
| [**驱动与底层硬件**](categories/drivers-low-level-hardware.md) | 433 | [MonitorControl](https://github.com/MonitorControl/MonitorControl), [tinygrad](https://github.com/tinygrad/tinygrad), [G-Helper](https://github.com/seerge/g-helper) |
| [**汽车**](categories/automotive.md) | 520 | [openpilot](https://github.com/commaai/openpilot), [evcc](https://github.com/evcc-io/evcc), [VESC firmware](https://github.com/vedderb/bldc) |
| [**工业与楼宇自动化**](categories/industrial-building-automation.md) | 291 | [HslCommunication](https://github.com/dathlin/HslCommunication), [plc4x](https://github.com/apache/plc4x), [IoTClient](https://github.com/zhaopeiym/IoTClient) |
| [**固件与嵌入式**](categories/firmware-embedded.md) | 472 | [LEDE (Lean)](https://github.com/coolsnowwolf/lede), [OpenWrt](https://github.com/openwrt/openwrt), [Tasmota](https://github.com/arendst/Tasmota) |
| [**网络与通信协议**](categories/network-wire-protocols.md) | 422 | [Sunshine](https://github.com/LizardByte/Sunshine), [moonlight-qt](https://github.com/moonlight-stream/moonlight-qt), [Impacket](https://github.com/fortra/impacket) |
| [**文件格式**](categories/file-formats.md) | 436 | [FFmpeg](https://github.com/FFmpeg/FFmpeg), [ImHex](https://github.com/WerWolv/ImHex), [SheetJS](https://github.com/SheetJS/sheetjs) |
| [**停服在线服务复活**](categories/online-service-revivals.md) | 173 | [NoLongerEvil Thermostat](https://github.com/codykociemba/NoLongerEvil-Thermostat), [Legacy Update](https://github.com/LegacyUpdate/LegacyUpdate), [wire-pod](https://github.com/kercre123/wire-pod) |
| [**桌面软件重新实现**](categories/desktop-software-reimplementations.md) | 201 | [vaultwarden](https://github.com/dani-garcia/vaultwarden), [PhotoCraft](https://github.com/storytold/photocraft), [Proton](https://github.com/ValveSoftware/Proton) |
| [**替代前端**](categories/alternative-frontends.md) | 121 | [searxng](https://github.com/searxng/searxng), [searx](https://github.com/searx/searx), [Whoogle Search](https://github.com/benbusby/whoogle-search) |
| [**移动应用**](categories/mobile-apps.md) | 102 | [revanced-manager](https://github.com/ReVanced/revanced-manager), [Metrolist](https://github.com/MetrolistGroup/Metrolist), [LibreTube](https://github.com/libre-tube/LibreTube) |
| [**逆向工程工具**](categories/re-tooling.md) | 741 | [rea](https://github.com/morluto/rea), [Ghidra](https://github.com/NationalSecurityAgency/ghidra), [jadx](https://github.com/skylot/jadx) |
| [**合集与 Awesome 列表**](categories/collections-awesome-lists.md) | 103 | [awesome reverse-engineering (wtsxDev)](https://github.com/wtsxDev/reverse-engineering), [android-security-awesome](https://github.com/ashishb/android-security-awesome), [mendel5/alternative-front-ends](https://github.com/mendel5/alternative-front-ends) |

## 让你的 AI 智能体使用整个索引

当任务需要对接没有官方 API 的东西（智能插座、汽车、聊天应用、文件格式）时，你的智能体会搜索这个索引，按星标数、活跃度和许可证排序，阅读 README，然后挑选合适的工具。

```bash
npx skills add alexgaoth/awesome-reverse-engineered
```

<details><summary><b>其他安装方式</b></summary>

**Claude Code 插件**

```
/plugin install reverse-engineered --marketplace alexgaoth/awesome-reverse-engineered
```

**任意智能体或终端（单个文件，仅依赖 Python 标准库）**

```bash
curl -sL https://raw.githubusercontent.com/alexgaoth/awesome-reverse-engineered/main/plugin/skills/find-reverse-engineered/scripts/re_index.py -o re_index.py
python3 re_index.py search tuya local          # ranked matches
python3 re_index.py info make-all/tuya-local   # entry + README excerpt
python3 re_index.py clone make-all/tuya-local  # shallow clone into vendor/
```

</details>

<p align="center"><img src="assets/demo.svg" alt="find-reverse-engineered" width="820"></p>
<p align="center"><sub>该技能在当前数据上的真实输出。</sub></p>

## 在网页上搜索

按分类、语言和健康状态筛选 12,880 个项目，可按星标数或最近活跃度排序。每次搜索都有可分享的链接。

<p align="center"><a href="https://alexgaoth.github.io/awesome-reverse-engineered/"><img src="assets/site.png" alt="在网页上搜索" width="820"></a></p>

<p align="center"><a href="https://alexgaoth.github.io/awesome-reverse-engineered/"><b>打开搜索 →</b></a></p>

## 本周热门

最近 7 天内有提交、星标最多的项目。

| 项目 | 用途 | ★ | 健康 | 语言 |
|---|---|--:|:-:|---|
| [rea](https://github.com/morluto/rea) | Agentic tool to reverse engineer apps from behavior down to native binaries | 257,688 | 🟢 | TypeScript |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | A feature-rich command-line audio/video downloader | 197,934 | 🟢 | Python |
| [claw-code](https://github.com/ultraworkers/claw-code) | Clean-room Rust/Python rewrite of the Claude Code agent harness after the source leak | 194,910 | 🟢 | Rust |
| [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Extracted system prompts and tool definitions for Cursor, Claude Code, Devin, Windsurf, Kiro, v0, Lovable and more | 144,036 | 🟢 |  |
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | NSA's software reverse engineering framework with decompiler | 88,122 | 🟢 | Java |
| [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Archive of extracted system prompts from ChatGPT, Claude, Gemini, Grok and others, per vendor with history | 69,676 | 🟢 | Python |
| [vaultwarden](https://github.com/dani-garcia/vaultwarden) | Unofficial Bitwarden-compatible server written in Rust | 69,078 | 🟢 | Rust |
| [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | Crawler for Xiaohongshu, Douyin, Kuaishou, Bilibili and Weibo posts and comments | 66,910 | 🟢 | Python |
| [gpt4free](https://github.com/xtekky/gpt4free) | Reverse-engineered third-party provider APIs giving free access to GPT-4 and other LLMs | 66,865 | 🟢 | Python |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Multimedia framework with many reverse-engineered proprietary codecs and containers | 65,205 | 🟢 | C |

## 最新收录

| 项目 | 用途 | ★ | 健康 | 语言 |
|---|---|--:|:-:|---|
| [v86](https://github.com/copy/v86) | v86, an x86 PC emulator and x86-to-wasm JIT running in the browser | 23,581 | 🟢 | JavaScript |
| [claude-code-best](https://github.com/claude-code-best/claude-code) | Reverse-engineered rebuild of the Anthropic Claude Code CLI as an open terminal coding assistant | 22,916 | 🟢 | TypeScript |
| [ppsspp](https://github.com/hrydgard/ppsspp) | PPSSPP, a PSP emulator for Android, Windows, macOS, Linux and iOS | 14,657 | 🟢 | C++ |
| [electronic-wechat](https://github.com/zhongyi-tong/electronic-wechat) | Electron WeChat client for macOS and Linux wrapping web WeChat | 13,815 | 🗄️ | JavaScript |
| [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) | Exports Discord chat logs to HTML, JSON, CSV or text files | 12,187 | 🟢 | C# |
| [mame](https://github.com/mamedev/mame) | MAME, the multi-system arcade and computer emulator | 10,606 | 🟢 | C++ |
| [xiaomusic](https://github.com/hanxi/xiaomusic) | Plays music on Xiaomi XiaoAI speakers through their unofficial cloud API | 10,033 | 🗄️ | Python |
| [Cemu](https://github.com/cemu-project/Cemu) | Cemu, a Wii U emulator | 9,989 | 🟢 | C++ |
| [wechatDownload](https://github.com/qiye45/wechatDownload) | Batch downloader for WeChat Official Account articles with comments and collections | 9,775 | 🟢 | HTML |
| [universal-modder](https://github.com/rehan-remade/universal-modder) | Skills and tools that let AI coding agents reverse engineer and mod almost any PC game | 7,776 | 🟢 | Python |
| [mgba](https://github.com/mgba-emu/mgba) | mGBA, an accurate Game Boy Advance emulator | 7,499 | 🟢 | C |
| [WeixinBot](https://github.com/Urinx/WeixinBot) | Web WeChat API with a terminal client and bot | 7,410 | 🔴 | Python |
| [xiaogpt](https://github.com/yihong0618/xiaogpt) | Connects ChatGPT and other LLMs to Xiaomi XiaoAI speakers via the unofficial MiService API | 6,942 | 🟢 | Python |
| [spacebarchat](https://github.com/spacebarchat/spacebarchat) | Free, self-hostable reimplementation of a Discord-compatible chat platform and API | 6,717 | 🟢 |  |
| [jsnes](https://github.com/bfirsh/jsnes) | jsnes, a JavaScript NES emulator | 6,426 | 🟢 | JavaScript |

## 星标最多

| # | 项目 | 用途 | ★ | 健康 | 语言 |
|--:|---|---|--:|:-:|---|
| 1 | [rea](https://github.com/morluto/rea) | Agentic tool to reverse engineer apps from behavior down to native binaries | 257,688 | 🟢 | TypeScript |
| 2 | [yt-dlp](https://github.com/yt-dlp/yt-dlp) | A feature-rich command-line audio/video downloader | 197,934 | 🟢 | Python |
| 3 | [claw-code](https://github.com/ultraworkers/claw-code) | Clean-room Rust/Python rewrite of the Claude Code agent harness after the source leak | 194,910 | 🟢 | Rust |
| 4 | [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Extracted system prompts and tool definitions for Cursor, Claude Code, Devin, Windsurf, Kiro, v0, Lovable and more | 144,036 | 🟢 |  |
| 5 | [youtube-dl](https://github.com/ytdl-org/youtube-dl) | Command-line program to download videos from YouTube.com and other video sites | 141,312 | 🟢 | Python |
| 6 | [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | NSA's software reverse engineering framework with decompiler | 88,122 | 🟢 | Java |
| 7 | [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Archive of extracted system prompts from ChatGPT, Claude, Gemini, Grok and others, per vendor with history | 69,676 | 🟢 | Python |
| 8 | [vaultwarden](https://github.com/dani-garcia/vaultwarden) | Unofficial Bitwarden-compatible server written in Rust | 69,078 | 🟢 | Rust |
| 9 | [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | Crawler for Xiaohongshu, Douyin, Kuaishou, Bilibili and Weibo posts and comments | 66,910 | 🟢 | Python |
| 10 | [gpt4free](https://github.com/xtekky/gpt4free) | Reverse-engineered third-party provider APIs giving free access to GPT-4 and other LLMs | 66,865 | 🟢 | Python |
| 11 | [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Multimedia framework with many reverse-engineered proprietary codecs and containers | 65,205 | 🟢 | C |
| 12 | [openpilot](https://github.com/commaai/openpilot) | Open-source driver assistance system for 300+ car models | 63,910 | 🟢 | Python |
| 13 | [PhotoCraft](https://github.com/storytold/photocraft) | Clean-room Photoshop-style photo editor written from scratch in pure Rust | 62,189 | 🟢 | Rust |
| 14 | [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | Wraps Codex, Claude Code, Antigravity, Grok and Gemini CLI OAuth backends as OpenAI/Claude-compatible APIs | 55,306 | 🟢 | Go |
| 15 | [ImHex](https://github.com/WerWolv/ImHex) | Hex editor for reverse engineers with a pattern language for binary formats | 55,207 | 🟢 | C++ |
| 16 | [lx-music-desktop](https://github.com/lyswhut/lx-music-desktop) | LX Music: desktop music player aggregating Chinese music platform sources | 54,457 | 🟢 | TypeScript |
| 17 | [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | Leaked system prompts and tool specs for ChatGPT, Claude, Gemini, Grok, Perplexity, Cursor, Lovable, Replit and others | 51,266 | 🟢 |  |
| 18 | [jadx](https://github.com/skylot/jadx) | Dex to Java decompiler for Android apps | 50,975 | 🟢 | Java |
| 19 | [alist](https://github.com/AlistGo/alist) | AList: file list and WebDAV server that mounts many cloud drives through their private APIs | 50,296 | 🟢 | Go |
| 20 | [Spotube](https://github.com/team-spotube/spotube) | Cross-platform Spotify client that streams audio from other sources | 49,947 | 🟢 | Dart |
| 21 | [x64dbg](https://github.com/x64dbg/x64dbg) | Open source user-mode debugger for Windows | 49,881 | 🟢 | C++ |
| 22 | [mitmproxy](https://github.com/mitmproxy/mitmproxy) | Interactive TLS-capable intercepting HTTP proxy | 45,623 | 🟢 | Python |
| 23 | [sub2api](https://github.com/Wei-Shaw/sub2api) | Relay that exposes Claude, OpenAI, Gemini and Grok subscriptions as unified APIs | 44,090 | 🟢 | Go |
| 24 | [fastlane](https://github.com/fastlane/fastlane) | iOS/Android release automation; its spaceship module wraps Apple's private developer portal and App Store Connect APIs | 42,245 | 🟢 | Ruby |
| 25 | [Sunshine](https://github.com/LizardByte/Sunshine) | Self-hosted game stream host that implements the NVIDIA GameStream protocol for Moonlight clients | 42,232 | 🟢 | C++ |

## 健康状态

| | 含义 |
|:-:|---|
| 🟢 | 活跃：过去 12 个月内有推送 |
| 🟡 | 放缓：最后一次推送在 1 到 3 年前 |
| 🔴 | 停滞：超过 3 年没有推送 |
| 🗄️ | 已被所有者归档 |
| ⚪ | 未知：不在 GitHub 上托管 |

厂商一改动，非官方 API 就可能失效。依赖某个项目之前，请先看它的健康状态。

## 构建方式

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

原始数据：[`data/entries.json`](data/entries.json)。已移除的仓库：[`data/removed.json`](data/removed.json)。导入的列表和搜索记录：[SOURCES.md](SOURCES.md)。

### 筛选方式

| | |
|--:|---|
| 2,458 | 次搜索，覆盖 GitHub、Hacker News、Reddit 和网页 |
| 290 | 个已有列表和合集被导入 |
| 147 | 个仓库被范围过滤器排除（漏洞利用、越狱、绕过、DRM、外挂）。研究智能体在这一步之前也会跳过这类项目。 |
| 12,880 | 个仓库收录在索引中，每个都经过 GitHub API 核验（是否存在、规范 URL、星标、许可证） |
| 897 | 个已被所有者归档：保留并标记为 🗄️ |
| 20 | 个因仓库被删除或设为私有，被每晚检查移除（[列表](data/removed.json)） |

<p align="center"><img src="assets/categories.svg" alt="Projects per category" width="820"></p>

## 收录范围

本索引收录以**互操作、保存和研究**为目的的项目：非官方客户端和 SDK、开源驱动、本地控制库、文件格式解析器、协议文档、重新实现和反编译项目。许多地区的法律保护以互操作为目的的逆向工程（例如美国法典第 17 编第 1201(f) 条和欧盟软件指令第 6 条）。

**有意不收录：**漏洞利用和越狱、安全机制或证书固定绕过、解密工具、外挂、DRM 或付费墙移除、验证码破解、账号机器人和凭据工具。

使用非官方客户端可能违反服务条款。请只在你自己的账号、设备和数据上使用这些项目。

## 参与贡献

知道应该收录的项目？请[提交 issue](https://github.com/alexgaoth/awesome-reverse-engineered/issues/new?title=Add%3A%20&body=Repo%3A%20%0AWhat%20it%20reverse%20engineers%3A%20)，附上仓库链接和一句话说明它逆向了什么，或者发 PR 把它加入 `data/entries.json`。分类错误、链接失效或超出范围，也请提交 issue。

由 [@alexgaoth](https://github.com/alexgaoth) 借助研究智能体整理。每个条目都经过 GitHub API 核验。

## 你的项目被收录了吗？

[![Listed in Awesome Reverse-Engineered](https://img.shields.io/badge/listed%20in-awesome--reverse--engineered-ffb000?style=flat-square&labelColor=0e0f0d)](https://github.com/alexgaoth/awesome-reverse-engineered)

可以把这个徽章加到你的 README 里。在[网站](https://alexgaoth.github.io/awesome-reverse-engineered/)上，每个项目都有一个 **badge** 按钮，可以复制指向该项目条目的版本。

```markdown
[![Listed in Awesome Reverse-Engineered](https://img.shields.io/badge/listed%20in-awesome--reverse--engineered-ffb000?style=flat-square&labelColor=0e0f0d)](https://github.com/alexgaoth/awesome-reverse-engineered)
```

## 星标历史

<a href="https://star-history.com/#alexgaoth/awesome-reverse-engineered&Date"><img src="https://api.star-history.com/svg?repos=alexgaoth/awesome-reverse-engineered&type=Date" alt="Star history" width="600"></a>

## 许可证

代码（脚本、网站、智能体技能）采用 [MIT](LICENSE)，列表和数据采用 [CC0 1.0](LICENSE-DATA)。每个链接的项目有各自的许可证。

<div align="center">

**如果它让你省去了亲自逆向的麻烦，[请给它一个星标](https://github.com/alexgaoth/awesome-reverse-engineered)。**

</div>
