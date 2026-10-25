<div align="center">

<a href="https://alexgaoth.github.io/awesome-reverse-engineered/"><img src="assets/banner.svg" alt="Awesome Reverse-Engineered" width="100%"></a>

<p><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.fr.md">Français</a> · <b>Español</b> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.pt-BR.md">Português (BR)</a></p>

## No hagas ingeniería inversa dos veces.

16,809 herramientas de código abierto que existen porque alguien hizo ingeniería inversa de un producto cerrado: una app, una API, un dispositivo, un protocolo, un formato de archivo, un juego o una herramienta de IA.

**[Buscar en el índice](https://alexgaoth.github.io/awesome-reverse-engineered/)** o dáselo a tu agente: `npx skills add alexgaoth/awesome-reverse-engineered`

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) [![Projects](https://img.shields.io/badge/projects-16%2C809-ffb000?style=flat-square&labelColor=0e0f0d)](#qué-contiene) [![Nightly refresh](https://img.shields.io/github/actions/workflow/status/alexgaoth/awesome-reverse-engineered/refresh.yml?style=flat-square&label=nightly%20refresh&labelColor=0e0f0d)](.github/workflows/refresh.yml) [![Stars](https://img.shields.io/github/stars/alexgaoth/awesome-reverse-engineered?style=flat-square&labelColor=0e0f0d&color=ffb000)](https://github.com/alexgaoth/awesome-reverse-engineered/stargazers) [![License: MIT + CC0 data](https://img.shields.io/badge/license-MIT%20%2B%20CC0%20data-30363d?style=flat-square&labelColor=0e0f0d)](LICENSE)

**[Skill para agentes](#dale-el-índice-completo-a-tu-agente-de-ia)** · **[Categorías](#qué-contiene)** · **[Populares esta semana](#populares-esta-semana)** · **[Proponer un proyecto](#contribuir)**

<sub>Los nombres y descripciones de los proyectos están en inglés.</sub>

</div>

---

## Antes de hacer ingeniería inversa

Los agentes y herramientas como [REA](https://github.com/morluto/rea) y [Ghidra](https://github.com/NationalSecurityAgency/ghidra) hacen que la ingeniería inversa sea más rápida que nunca. Aun así, la app, la API, el dispositivo o el formato de archivo que vas a abrir muchas veces ya está resuelto, y el trabajo está en un repo que nadie enlaza.

1. **Busca primero.** En la [web](https://alexgaoth.github.io/awesome-reverse-engineered/) o con el [skill para agentes](#dale-el-índice-completo-a-tu-agente-de-ia), por producto, fabricante o protocolo.
2. **¿Lo encontraste?** Úsalo, mejóralo y reporta los fallos al proyecto original. Un cliente mantenido vale más que diez scripts privados.
3. **¿No está?** Haz el trabajo, publícalo como código abierto y [añádelo aquí](#contribuir) para que la siguiente persona empiece donde tú terminaste.

## Qué contiene

**16,809 proyectos** que suman **11.2 M** de estrellas en GitHub: 9,691 activos, 2,370 en desaceleración, 3,236 inactivos, 1,055 archivados. Lenguajes principales: Python (3,792), C++ (2,610), C (2,495), JavaScript (983), C# (902).

| Categoría | Proyectos | Destacados |
|---|--:|---|
| [**Herramientas de IA y clientes de LLM**](categories/ai-tools-llm-clients.md) | 740 | [claw-code](https://github.com/ultraworkers/claw-code), [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools), [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) |
| [**Decompilaciones y reimplementaciones de juegos**](categories/game-decompilations-reimplementations.md) | 6,071 | [shadPS4](https://github.com/shadps4-emu/shadPS4), [v86](https://github.com/copy/v86), [RPCS3](https://github.com/RPCS3/rpcs3) |
| [**Dispositivos, IoT y hardware**](categories/devices-iot-hardware.md) | 3,059 | [KOReader](https://github.com/koreader/koreader), [LibrePods](https://github.com/librepods-org/librepods), [OpenLogi](https://github.com/AprilNEA/OpenLogi) |
| [**Clientes de API web y de apps no oficiales**](categories/unofficial-web-app-api-clients.md) | 908 | [yt-dlp](https://github.com/yt-dlp/yt-dlp), [youtube-dl](https://github.com/ytdl-org/youtube-dl), [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) |
| [**Mensajería y redes sociales**](categories/messaging-social-apps.md) | 297 | [WeChatMsg](https://github.com/LC044/WeChatMsg), [ItChat](https://github.com/littlecodersh/ItChat), [wechaty](https://github.com/wechaty/wechaty) |
| [**Clientes de terceros**](categories/third-party-clients.md) | 190 | [spotify-tui](https://github.com/Rigellute/spotify-tui), [nuclear](https://github.com/nukeop/nuclear), [SimpMusic](https://github.com/maxrave-dev/SimpMusic) |
| [**Plataformas chinas y asiáticas**](categories/chinese-asian-platforms.md) | 325 | [lx-music-desktop](https://github.com/lyswhut/lx-music-desktop), [alist](https://github.com/AlistGo/alist), [12306](https://github.com/testerSunshine/12306) |
| [**Ecosistema Apple**](categories/apple-ecosystem.md) | 344 | [fastlane](https://github.com/fastlane/fastlane), [homebridge](https://github.com/homebridge/homebridge), [OSX-KVM](https://github.com/kholia/OSX-KVM) |
| [**Drivers y hardware de bajo nivel**](categories/drivers-low-level-hardware.md) | 442 | [MonitorControl](https://github.com/MonitorControl/MonitorControl), [tinygrad](https://github.com/tinygrad/tinygrad), [G-Helper](https://github.com/seerge/g-helper) |
| [**Automoción**](categories/automotive.md) | 525 | [openpilot](https://github.com/commaai/openpilot), [evcc](https://github.com/evcc-io/evcc), [VESC firmware](https://github.com/vedderb/bldc) |
| [**Automatización industrial y de edificios**](categories/industrial-building-automation.md) | 291 | [HslCommunication](https://github.com/dathlin/HslCommunication), [plc4x](https://github.com/apache/plc4x), [IoTClient](https://github.com/zhaopeiym/IoTClient) |
| [**Firmware y sistemas embebidos**](categories/firmware-embedded.md) | 494 | [LEDE (Lean)](https://github.com/coolsnowwolf/lede), [OpenWrt](https://github.com/openwrt/openwrt), [Tasmota](https://github.com/arendst/Tasmota) |
| [**Protocolos de red y de comunicación**](categories/network-wire-protocols.md) | 426 | [Sunshine](https://github.com/LizardByte/Sunshine), [moonlight-qt](https://github.com/moonlight-stream/moonlight-qt), [Impacket](https://github.com/fortra/impacket) |
| [**Formatos de archivo**](categories/file-formats.md) | 439 | [FFmpeg](https://github.com/FFmpeg/FFmpeg), [ImHex](https://github.com/WerWolv/ImHex), [SheetJS](https://github.com/SheetJS/sheetjs) |
| [**Servicios en línea revividos**](categories/online-service-revivals.md) | 639 | [NoLongerEvil Thermostat](https://github.com/codykociemba/NoLongerEvil-Thermostat), [Legacy Update](https://github.com/LegacyUpdate/LegacyUpdate), [DeskThing](https://github.com/ItsRiprod/DeskThing) |
| [**Reimplementaciones de software de escritorio**](categories/desktop-software-reimplementations.md) | 226 | [PhotoCraft](https://github.com/storytold/photocraft), [vaultwarden](https://github.com/dani-garcia/vaultwarden), [Proton](https://github.com/ValveSoftware/Proton) |
| [**Frontends alternativos**](categories/alternative-frontends.md) | 121 | [searxng](https://github.com/searxng/searxng), [searx](https://github.com/searx/searx), [Whoogle Search](https://github.com/benbusby/whoogle-search) |
| [**Apps móviles**](categories/mobile-apps.md) | 102 | [revanced-manager](https://github.com/ReVanced/revanced-manager), [Metrolist](https://github.com/MetrolistGroup/Metrolist), [LibreTube](https://github.com/libre-tube/LibreTube) |
| [**Herramientas de ingeniería inversa**](categories/re-tooling.md) | 1,031 | [rea](https://github.com/morluto/rea), [Ghidra](https://github.com/NationalSecurityAgency/ghidra), [jadx](https://github.com/skylot/jadx) |
| [**Colecciones y listas Awesome**](categories/collections-awesome-lists.md) | 139 | [Corkami pics](https://github.com/corkami/pics), [awesome reverse-engineering (wtsxDev)](https://github.com/wtsxDev/reverse-engineering), [android-security-awesome](https://github.com/ashishb/android-security-awesome) |

## Resucitados

130 productos que su fabricante abandonó, mantenidos con vida por proyectos de código abierto hechos con ingeniería inversa.

| Producto | Cerrado por | Año | Revivido por |
|---|---|--:|---|
| Spotify Car Thing | Spotify | 2024 | [DeskThing](https://github.com/ItsRiprod/DeskThing) |
| Amazon Dash Button | Amazon | 2019 | [node-dash-button](https://github.com/hortinstein/node-dash-button) |
| Nest Learning Thermostat (1st and 2nd gen) | Google | 2025 | [NoLongerEvil Thermostat](https://github.com/codykociemba/NoLongerEvil-Thermostat) |
| AOL Instant Messenger (AIM) | AOL | 2017 | [Open OSCAR Server (Retro AIM Server)](https://github.com/mk6i/open-oscar-server) |
| Nintendo Wi-Fi Connection (DS and Wii online) | Nintendo | 2014 | [DWC Network Server Emulator](https://github.com/barronwaffles/dwc_network_server_emulator) |
| Pebble smartwatch | Fitbit | 2018 | [mobile-app](https://github.com/pebble-dev/mobile-app) |
| ICQ | VK | 2024 | [Open OSCAR Server (Retro AIM Server)](https://github.com/mk6i/open-oscar-server) |
| Neato robot vacuums | Neato Robotics / Vorwerk | 2025 | [fang](https://github.com/vacuula/fang) |

**[Ver los 130 en la página Resucitados →](https://alexgaoth.github.io/awesome-reverse-engineered/resurrected/)**

## Dale el índice completo a tu agente de IA

Cuando una tarea necesita comunicarse con algo sin API oficial (un enchufe inteligente, un coche, una app de mensajería, un formato de archivo), tu agente busca en este índice, ordena por estrellas, actividad y licencia, lee el README y elige la herramienta adecuada.

```bash
npx skills add alexgaoth/awesome-reverse-engineered
```

<details><summary><b>Otras formas de instalarlo</b></summary>

**Plugin de Claude Code**

```
/plugin install reverse-engineered --marketplace alexgaoth/awesome-reverse-engineered
```

**Servidor MCP (Claude Desktop, Cursor, cualquier cliente MCP)**

```bash
claude mcp add reverse-engineered -- uvx --from "git+https://github.com/alexgaoth/awesome-reverse-engineered#subdirectory=mcp" reverse-engineered-mcp
```

```json
{"mcpServers": {"reverse-engineered": {"command": "uvx", "args": ["--from", "git+https://github.com/alexgaoth/awesome-reverse-engineered#subdirectory=mcp", "reverse-engineered-mcp"]}}}
```

**Cualquier agente o terminal (un solo archivo, solo la biblioteca estándar de Python)**

```bash
curl -sL https://raw.githubusercontent.com/alexgaoth/awesome-reverse-engineered/main/plugin/skills/find-reverse-engineered/scripts/re_index.py -o re_index.py
python3 re_index.py search tuya local          # ranked matches
python3 re_index.py info make-all/tuya-local   # entry + README excerpt
python3 re_index.py clone make-all/tuya-local  # shallow clone into vendor/
```

</details>

<p align="center"><img src="assets/demo.svg" alt="find-reverse-engineered" width="820"></p>
<p align="center"><sub>Salida real del skill con los datos actuales.</sub></p>

## Búscalo en la web

Filtra 16,809 proyectos por categoría, lenguaje y estado de salud, ordenados por estrellas o actividad reciente. Cada búsqueda tiene un enlace para compartir.

<p align="center"><a href="https://alexgaoth.github.io/awesome-reverse-engineered/"><img src="assets/site.png" alt="Búscalo en la web" width="820"></a></p>

<p align="center"><a href="https://alexgaoth.github.io/awesome-reverse-engineered/"><b>Abrir el buscador →</b></a></p>

## Populares esta semana

Los proyectos con más estrellas que recibieron commits en los últimos 7 días.

| Proyecto | Qué hace | ★ | Salud | Lenguaje |
|---|---|--:|:-:|---|
| [rea](https://github.com/morluto/rea) | Agentic tool to reverse engineer apps from behavior down to native binaries | 381,341 | 🟢 | TypeScript |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | A feature-rich command-line audio/video downloader | 201,784 | 🟢 | Python |
| [claw-code](https://github.com/ultraworkers/claw-code) | Clean-room Rust/Python rewrite of the Claude Code agent harness after the source leak | 195,063 | 🟢 | Rust |
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | NSA's software reverse engineering framework with decompiler | 94,120 | 🟢 | Java |
| [PhotoCraft](https://github.com/storytold/photocraft) | Clean-room Photoshop-style photo editor written from scratch in pure Rust | 72,590 | 🟢 | Rust |
| [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Archive of extracted system prompts from ChatGPT, Claude, Gemini, Grok and others, per vendor with history | 70,169 | 🟢 | Python |
| [vaultwarden](https://github.com/dani-garcia/vaultwarden) | Unofficial Bitwarden-compatible server written in Rust | 69,630 | 🟢 | Rust |
| [gpt4free](https://github.com/xtekky/gpt4free) | Reverse-engineered third-party provider APIs giving free access to GPT-4 and other LLMs | 66,927 | 🟢 | Python |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Multimedia framework with many reverse-engineered proprietary codecs and containers | 65,704 | 🟢 | C |
| [openpilot](https://github.com/commaai/openpilot) | Open-source driver assistance system for 300+ car models | 63,988 | 🟢 | Python |

## Recién añadidos

| Proyecto | Qué hace | ★ | Salud | Lenguaje |
|---|---|--:|:-:|---|
| [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | Static and dynamic analysis framework for Android and iOS app packages | 22,032 | 🟢 | Python |
| [YoutubeDownloader](https://github.com/Tyrrrz/YoutubeDownloader) | Desktop app that downloads YouTube videos and playlists via YouTube's internal API | 16,527 | 🟢 | C# |
| [LunaTranslator](https://github.com/HIllya51/LunaTranslator) | Visual novel translator that hooks game text from running Windows games | 13,891 | 🟢 | C++ |
| [Corkami pics](https://github.com/corkami/pics) | Visual dissections and posters of binary file formats | 11,500 | 🟡 | Assembly |
| [FLARE-VM](https://github.com/mandiant/flare-vm) | Installer that sets up a Windows VM for reverse engineering and malware analysis | 9,187 | 🟢 | PowerShell |
| [GEF](https://github.com/hugsy/gef) | GDB extension that adds dynamic-analysis commands and context views | 8,401 | 🟢 | Python |
| [Minecraft Forge](https://github.com/MinecraftForge/MinecraftForge) | Modding API and loader for Minecraft: Java Edition | 7,834 | 🟢 | Java |
| [replica-skill](https://github.com/Jakeschincariol/replica-skill) | Claude skills that reverse engineer an app, rebuild it, test it and fix user-reported issues | 5,362 | 🟢 | Python |
| [hooker](https://github.com/CreditTone/hooker) | Frida-based Android reverse engineering toolkit with CLI and universal scripts | 5,330 | 🟢 | JavaScript |
| [dlssg-to-fsr3](https://github.com/Nukem9/dlssg-to-fsr3) | Replaces DLSS Frame Generation with FSR 3 frame generation in games | 4,977 | 🟡 | C++ |
| [GDA](https://github.com/charles2gan/GDA-android-reversing-Tool) | Windows-native Dalvik decompiler and Android analysis workbench | 4,867 | 🟢 | Python |
| [D2R Mobile](https://github.com/jhaizhou-ops/d2r-mobile) | Runs the Switch build of Diablo II: Resurrected natively on iPhone, iPad and Apple silicon Macs | 4,598 | 🟢 | C |
| [Zydis](https://github.com/zyantific/zydis) | Fast x86/x86-64 disassembler and encoder library in C | 4,394 | 🟢 | C |
| [wxapkg](https://github.com/wux1an/wxapkg) | Desktop GUI that unpacks WeChat mini-program .wxapkg packages | 4,304 | 🟢 | Vue |
| [FLOSS](https://github.com/mandiant/flare-floss) | Extracts obfuscated, stack and tight strings from malware binaries | 4,199 | 🟢 | Python |

## Con más estrellas

| # | Proyecto | Qué hace | ★ | Salud | Lenguaje |
|--:|---|---|--:|:-:|---|
| 1 | [rea](https://github.com/morluto/rea) | Agentic tool to reverse engineer apps from behavior down to native binaries | 381,341 | 🟢 | TypeScript |
| 2 | [yt-dlp](https://github.com/yt-dlp/yt-dlp) | A feature-rich command-line audio/video downloader | 201,784 | 🟢 | Python |
| 3 | [claw-code](https://github.com/ultraworkers/claw-code) | Clean-room Rust/Python rewrite of the Claude Code agent harness after the source leak | 195,063 | 🟢 | Rust |
| 4 | [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Extracted system prompts and tool definitions for Cursor, Claude Code, Devin, Windsurf, Kiro, v0, Lovable and more | 144,236 | 🟢 |  |
| 5 | [youtube-dl](https://github.com/ytdl-org/youtube-dl) | Command-line program to download videos from YouTube.com and other video sites | 141,391 | 🟢 | Python |
| 6 | [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | NSA's software reverse engineering framework with decompiler | 94,120 | 🟢 | Java |
| 7 | [PhotoCraft](https://github.com/storytold/photocraft) | Clean-room Photoshop-style photo editor written from scratch in pure Rust | 72,590 | 🟢 | Rust |
| 8 | [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Archive of extracted system prompts from ChatGPT, Claude, Gemini, Grok and others, per vendor with history | 70,169 | 🟢 | Python |
| 9 | [vaultwarden](https://github.com/dani-garcia/vaultwarden) | Unofficial Bitwarden-compatible server written in Rust | 69,630 | 🟢 | Rust |
| 10 | [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | Crawler for Xiaohongshu, Douyin, Kuaishou, Bilibili and Weibo posts and comments | 68,469 | 🟢 | Python |
| 11 | [gpt4free](https://github.com/xtekky/gpt4free) | Reverse-engineered third-party provider APIs giving free access to GPT-4 and other LLMs | 66,927 | 🟢 | Python |
| 12 | [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Multimedia framework with many reverse-engineered proprietary codecs and containers | 65,704 | 🟢 | C |
| 13 | [openpilot](https://github.com/commaai/openpilot) | Open-source driver assistance system for 300+ car models | 63,988 | 🟢 | Python |
| 14 | [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | Wraps Codex, Claude Code, Antigravity, Grok and Gemini CLI OAuth backends as OpenAI/Claude-compatible APIs | 56,180 | 🟢 | Go |
| 15 | [ImHex](https://github.com/WerWolv/ImHex) | Hex editor for reverse engineers with a pattern language for binary formats | 55,558 | 🟢 | C++ |
| 16 | [lx-music-desktop](https://github.com/lyswhut/lx-music-desktop) | LX Music: desktop music player aggregating Chinese music platform sources | 54,761 | 🟢 | TypeScript |
| 17 | [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | Leaked system prompts and tool specs for ChatGPT, Claude, Gemini, Grok, Perplexity, Cursor, Lovable, Replit and others | 51,494 | 🟢 |  |
| 18 | [jadx](https://github.com/skylot/jadx) | Dex to Java decompiler for Android apps | 51,253 | 🟢 | Java |
| 19 | [alist](https://github.com/AlistGo/alist) | AList: file list and WebDAV server that mounts many cloud drives through their private APIs | 50,358 | 🟢 | Go |
| 20 | [Spotube](https://github.com/team-spotube/spotube) | Cross-platform Spotify client that streams audio from other sources | 50,302 | 🟢 | Dart |
| 21 | [x64dbg](https://github.com/x64dbg/x64dbg) | Open source user-mode debugger for Windows | 50,019 | 🟢 | C++ |
| 22 | [mitmproxy](https://github.com/mitmproxy/mitmproxy) | Interactive TLS-capable intercepting HTTP proxy | 46,315 | 🟢 | Python |
| 23 | [sub2api](https://github.com/Wei-Shaw/sub2api) | Relay that exposes Claude, OpenAI, Gemini and Grok subscriptions as unified APIs | 44,801 | 🟢 | Go |
| 24 | [Sunshine](https://github.com/LizardByte/Sunshine) | Self-hosted game stream host that implements the NVIDIA GameStream protocol for Moonlight clients | 42,608 | 🟢 | C++ |
| 25 | [fastlane](https://github.com/fastlane/fastlane) | iOS/Android release automation; its spaceship module wraps Apple's private developer portal and App Store Connect APIs | 42,301 | 🟢 | Ruby |

## Salud

| | Significado |
|:-:|---|
| 🟢 | Activo: push en los últimos 12 meses |
| 🟡 | En desaceleración: último push hace 1 a 3 años |
| 🔴 | Inactivo: sin push desde hace más de 3 años |
| 🗄️ | Archivado por su propietario |
| ⚪ | Desconocido: no alojado en GitHub |

Las API no oficiales se rompen cuando el fabricante cambia algo. Revisa la salud de un proyecto antes de depender de él.

## Cómo se construye

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

Datos en bruto: [`data/entries.json`](data/entries.json). Repos eliminados: [`data/removed.json`](data/removed.json). Listas importadas y búsquedas: [SOURCES.md](SOURCES.md).

### Cómo filtramos

| | |
|--:|---|
| 3,099 | búsquedas en GitHub, Hacker News, Reddit y la web |
| 348 | listas y colecciones existentes importadas |
| 173 | repos descartados por el filtro de alcance (exploits, jailbreaks, evasiones, DRM, trampas). Los agentes de investigación también los descartan antes. |
| 16,809 | repos en el índice, cada uno verificado con la API de GitHub (existe, URL canónica, estrellas, licencia) |
| 1,055 | archivados por sus propietarios: se mantienen y se marcan con 🗄️ |
| 47 | eliminados por la comprobación nocturna porque el repo se borró o pasó a ser privado ([lista](data/removed.json)) |

<p align="center"><img src="assets/categories.svg" alt="Projects per category" width="820"></p>

## Alcance

Este índice recoge proyectos de **interoperabilidad, preservación e investigación**: clientes y SDK no oficiales, drivers libres, bibliotecas de control local, parsers de formatos de archivo, documentación de protocolos, reimplementaciones y decompilaciones. La ingeniería inversa con fines de interoperabilidad está protegida en muchos lugares (por ejemplo, 17 U.S.C. §1201(f) y el artículo 6 de la Directiva europea sobre programas de ordenador).

**Excluido a propósito:** exploits y jailbreaks, evasión de seguridad o de certificate pinning, herramientas de descifrado, trampas, eliminación de DRM o paywalls, solucionadores de CAPTCHA, bots de cuentas y herramientas de credenciales.

Usar un cliente no oficial puede incumplir los términos de uso de un servicio. Usa estos proyectos con tus propias cuentas, dispositivos y datos.

## Contribuir

¿Conoces un proyecto que debería estar aquí? [Abre un issue](https://github.com/alexgaoth/awesome-reverse-engineered/issues/new?title=Add%3A%20&body=Repo%3A%20%0AWhat%20it%20reverse%20engineers%3A%20) con el enlace del repo y una línea sobre qué le hace ingeniería inversa, o envía un PR que lo añada a `data/entries.json`. ¿Categoría incorrecta, enlace roto o fuera de alcance? Abre un issue también.

Curado por [@alexgaoth](https://github.com/alexgaoth) con agentes de investigación. Cada entrada se verifica con la API de GitHub.

## ¿Tu proyecto está en la lista?

[![Listed in Awesome Reverse-Engineered](https://img.shields.io/badge/listed%20in-awesome--reverse--engineered-ffb000?style=flat-square&labelColor=0e0f0d)](https://github.com/alexgaoth/awesome-reverse-engineered)

Añade esta insignia a tu README. En la [web](https://alexgaoth.github.io/awesome-reverse-engineered/), cada proyecto tiene un botón **badge** que copia una versión que enlaza a su propia ficha.

```markdown
[![Listed in Awesome Reverse-Engineered](https://img.shields.io/badge/listed%20in-awesome--reverse--engineered-ffb000?style=flat-square&labelColor=0e0f0d)](https://github.com/alexgaoth/awesome-reverse-engineered)
```

## Historial de estrellas

<a href="https://star-history.com/#alexgaoth/awesome-reverse-engineered&Date"><img src="https://api.star-history.com/svg?repos=alexgaoth/awesome-reverse-engineered&type=Date" alt="Star history" width="600"></a>

## Licencia

Código (scripts, web, skill para agentes): [MIT](LICENSE). Lista y datos: [CC0 1.0](LICENSE-DATA). Cada proyecto enlazado tiene su propia licencia.

<div align="center">

**Si esto te ahorró hacer ingeniería inversa por tu cuenta, [dale una estrella](https://github.com/alexgaoth/awesome-reverse-engineered).**

</div>
