<div align="center">

<a href="https://alexgaoth.github.io/awesome-reverse-engineered/"><img src="assets/banner.svg" alt="Awesome Reverse-Engineered" width="100%"></a>

<p><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.fr.md">Français</a> · <a href="README.es.md">Español</a> · <a href="README.vi.md">Tiếng Việt</a> · <b>Português (BR)</b></p>

## Não faça engenharia reversa duas vezes.

16,811 ferramentas de código aberto que existem porque alguém fez engenharia reversa de um produto fechado: um app, uma API, um dispositivo, um protocolo, um formato de arquivo, um jogo ou uma ferramenta de IA.

**[Buscar no índice](https://alexgaoth.github.io/awesome-reverse-engineered/)** ou entregue ao seu agente: `npx skills add alexgaoth/awesome-reverse-engineered`

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) [![Projects](https://img.shields.io/badge/projects-16%2C811-ffb000?style=flat-square&labelColor=0e0f0d)](#o-que-tem-aqui) [![Nightly refresh](https://img.shields.io/github/actions/workflow/status/alexgaoth/awesome-reverse-engineered/refresh.yml?style=flat-square&label=nightly%20refresh&labelColor=0e0f0d)](.github/workflows/refresh.yml) [![Stars](https://img.shields.io/github/stars/alexgaoth/awesome-reverse-engineered?style=flat-square&labelColor=0e0f0d&color=ffb000)](https://github.com/alexgaoth/awesome-reverse-engineered/stargazers) [![License: MIT + CC0 data](https://img.shields.io/badge/license-MIT%20%2B%20CC0%20data-30363d?style=flat-square&labelColor=0e0f0d)](LICENSE)

**[Skill para agentes](#dê-o-índice-inteiro-ao-seu-agente-de-ia)** · **[Categorias](#o-que-tem-aqui)** · **[Em alta nesta semana](#em-alta-nesta-semana)** · **[Sugerir um projeto](#como-contribuir)**

<sub>Os nomes e as descrições dos projetos estão em inglês.</sub>

</div>

---

## Antes de fazer engenharia reversa de algo

Agentes e ferramentas como [REA](https://github.com/morluto/rea) e [Ghidra](https://github.com/NationalSecurityAgency/ghidra) deixam a engenharia reversa mais rápida do que nunca. Ainda assim, o app, a API, o dispositivo ou o formato de arquivo que você vai abrir muitas vezes já foi resolvido, e o trabalho está num repo que ninguém linka.

1. **Busque primeiro.** Use o [site](https://alexgaoth.github.io/awesome-reverse-engineered/) ou a [skill para agentes](#dê-o-índice-inteiro-ao-seu-agente-de-ia). Busque por produto, fabricante ou protocolo.
2. **Achou?** Use, corrija e reporte os problemas no projeto original. Um cliente mantido vale mais que dez scripts particulares.
3. **Não está aqui?** Faça o trabalho, publique como código aberto e [adicione aqui](#como-contribuir) para que a próxima pessoa comece de onde você parou.

## O que tem aqui

**16,811 projetos** que somam **11.2 mi** de estrelas no GitHub: 9,695 ativos, 2,373 desacelerando, 3,235 parados, 1,051 arquivados. Principais linguagens: Python (3,791), C++ (2,609), C (2,497), JavaScript (984), C# (901).

| Categoria | Projetos | Destaques |
|---|--:|---|
| [**Ferramentas de IA e clientes de LLM**](categories/ai-tools-llm-clients.md) | 740 | [claw-code](https://github.com/ultraworkers/claw-code), [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools), [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) |
| [**Decompilações e reimplementações de jogos**](categories/game-decompilations-reimplementations.md) | 6,073 | [shadPS4](https://github.com/shadps4-emu/shadPS4), [v86](https://github.com/copy/v86), [RPCS3](https://github.com/RPCS3/rpcs3) |
| [**Dispositivos, IoT e hardware**](categories/devices-iot-hardware.md) | 3,059 | [KOReader](https://github.com/koreader/koreader), [LibrePods](https://github.com/librepods-org/librepods), [OpenLogi](https://github.com/AprilNEA/OpenLogi) |
| [**Clientes de APIs web e de apps não oficiais**](categories/unofficial-web-app-api-clients.md) | 908 | [yt-dlp](https://github.com/yt-dlp/yt-dlp), [youtube-dl](https://github.com/ytdl-org/youtube-dl), [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) |
| [**Mensageiros e redes sociais**](categories/messaging-social-apps.md) | 297 | [WeChatMsg](https://github.com/LC044/WeChatMsg), [ItChat](https://github.com/littlecodersh/ItChat), [wechaty](https://github.com/wechaty/wechaty) |
| [**Clientes de terceiros**](categories/third-party-clients.md) | 190 | [spotify-tui](https://github.com/Rigellute/spotify-tui), [nuclear](https://github.com/nukeop/nuclear), [SimpMusic](https://github.com/maxrave-dev/SimpMusic) |
| [**Plataformas chinesas e asiáticas**](categories/chinese-asian-platforms.md) | 325 | [lx-music-desktop](https://github.com/lyswhut/lx-music-desktop), [alist](https://github.com/AlistGo/alist), [12306](https://github.com/testerSunshine/12306) |
| [**Ecossistema Apple**](categories/apple-ecosystem.md) | 344 | [fastlane](https://github.com/fastlane/fastlane), [homebridge](https://github.com/homebridge/homebridge), [OSX-KVM](https://github.com/kholia/OSX-KVM) |
| [**Drivers e hardware de baixo nível**](categories/drivers-low-level-hardware.md) | 442 | [MonitorControl](https://github.com/MonitorControl/MonitorControl), [tinygrad](https://github.com/tinygrad/tinygrad), [G-Helper](https://github.com/seerge/g-helper) |
| [**Automotivo**](categories/automotive.md) | 525 | [openpilot](https://github.com/commaai/openpilot), [evcc](https://github.com/evcc-io/evcc), [VESC firmware](https://github.com/vedderb/bldc) |
| [**Automação industrial e predial**](categories/industrial-building-automation.md) | 291 | [HslCommunication](https://github.com/dathlin/HslCommunication), [plc4x](https://github.com/apache/plc4x), [IoTClient](https://github.com/zhaopeiym/IoTClient) |
| [**Firmware e sistemas embarcados**](categories/firmware-embedded.md) | 494 | [LEDE (Lean)](https://github.com/coolsnowwolf/lede), [OpenWrt](https://github.com/openwrt/openwrt), [Tasmota](https://github.com/arendst/Tasmota) |
| [**Protocolos de rede e de comunicação**](categories/network-wire-protocols.md) | 426 | [Sunshine](https://github.com/LizardByte/Sunshine), [moonlight-qt](https://github.com/moonlight-stream/moonlight-qt), [Impacket](https://github.com/fortra/impacket) |
| [**Formatos de arquivo**](categories/file-formats.md) | 439 | [FFmpeg](https://github.com/FFmpeg/FFmpeg), [ImHex](https://github.com/WerWolv/ImHex), [SheetJS](https://github.com/SheetJS/sheetjs) |
| [**Serviços online ressuscitados**](categories/online-service-revivals.md) | 639 | [NoLongerEvil Thermostat](https://github.com/codykociemba/NoLongerEvil-Thermostat), [Legacy Update](https://github.com/LegacyUpdate/LegacyUpdate), [DeskThing](https://github.com/ItsRiprod/DeskThing) |
| [**Reimplementações de software desktop**](categories/desktop-software-reimplementations.md) | 226 | [PhotoCraft](https://github.com/storytold/photocraft), [vaultwarden](https://github.com/dani-garcia/vaultwarden), [Proton](https://github.com/ValveSoftware/Proton) |
| [**Frontends alternativos**](categories/alternative-frontends.md) | 121 | [searxng](https://github.com/searxng/searxng), [searx](https://github.com/searx/searx), [Whoogle Search](https://github.com/benbusby/whoogle-search) |
| [**Apps móveis**](categories/mobile-apps.md) | 102 | [revanced-manager](https://github.com/ReVanced/revanced-manager), [Metrolist](https://github.com/MetrolistGroup/Metrolist), [LibreTube](https://github.com/libre-tube/LibreTube) |
| [**Ferramentas de engenharia reversa**](categories/re-tooling.md) | 1,031 | [rea](https://github.com/morluto/rea), [Ghidra](https://github.com/NationalSecurityAgency/ghidra), [jadx](https://github.com/skylot/jadx) |
| [**Coleções e listas Awesome**](categories/collections-awesome-lists.md) | 139 | [Corkami pics](https://github.com/corkami/pics), [awesome reverse-engineering (wtsxDev)](https://github.com/wtsxDev/reverse-engineering), [android-security-awesome](https://github.com/ashishb/android-security-awesome) |

## Ressuscitados

130 produtos que o fabricante matou, mantidos vivos por projetos de código aberto feitos com engenharia reversa.

| Produto | Encerrado por | Ano | Revivido por |
|---|---|--:|---|
| Spotify Car Thing | Spotify | 2024 | [DeskThing](https://github.com/ItsRiprod/DeskThing) |
| Amazon Dash Button | Amazon | 2019 | [node-dash-button](https://github.com/hortinstein/node-dash-button) |
| Nest Learning Thermostat (1st and 2nd gen) | Google | 2025 | [NoLongerEvil Thermostat](https://github.com/codykociemba/NoLongerEvil-Thermostat) |
| AOL Instant Messenger (AIM) | AOL | 2017 | [Open OSCAR Server (Retro AIM Server)](https://github.com/mk6i/open-oscar-server) |
| Nintendo Wi-Fi Connection (DS and Wii online) | Nintendo | 2014 | [DWC Network Server Emulator](https://github.com/barronwaffles/dwc_network_server_emulator) |
| Pebble smartwatch | Fitbit | 2018 | [mobile-app](https://github.com/pebble-dev/mobile-app) |
| ICQ | VK | 2024 | [Open OSCAR Server (Retro AIM Server)](https://github.com/mk6i/open-oscar-server) |
| Neato robot vacuums | Neato Robotics / Vorwerk | 2025 | [fang](https://github.com/vacuula/fang) |

**[Veja os 130 na página Ressuscitados →](https://alexgaoth.github.io/awesome-reverse-engineered/resurrected/)**

## Dê o índice inteiro ao seu agente de IA

Quando uma tarefa precisa conversar com algo sem API oficial (uma tomada inteligente, um carro, um app de mensagens, um formato de arquivo), seu agente busca neste índice, ordena por estrelas, atividade e licença, lê o README e escolhe a ferramenta certa.

```bash
npx skills add alexgaoth/awesome-reverse-engineered
```

<details><summary><b>Outras formas de instalar</b></summary>

**Plugin do Claude Code**

```
/plugin install reverse-engineered --marketplace alexgaoth/awesome-reverse-engineered
```

**Servidor MCP (Claude Desktop, Cursor, qualquer cliente MCP)**

```bash
claude mcp add reverse-engineered -- uvx --from "git+https://github.com/alexgaoth/awesome-reverse-engineered#subdirectory=mcp" reverse-engineered-mcp
```

```json
{"mcpServers": {"reverse-engineered": {"command": "uvx", "args": ["--from", "git+https://github.com/alexgaoth/awesome-reverse-engineered#subdirectory=mcp", "reverse-engineered-mcp"]}}}
```

**Qualquer agente ou terminal (um único arquivo, só a biblioteca padrão do Python)**

```bash
curl -sL https://raw.githubusercontent.com/alexgaoth/awesome-reverse-engineered/main/plugin/skills/find-reverse-engineered/scripts/re_index.py -o re_index.py
python3 re_index.py search tuya local          # ranked matches
python3 re_index.py info make-all/tuya-local   # entry + README excerpt
python3 re_index.py clone make-all/tuya-local  # shallow clone into vendor/
```

</details>

<p align="center"><img src="assets/demo.svg" alt="find-reverse-engineered" width="820"></p>
<p align="center"><sub>Saída real da skill com os dados atuais.</sub></p>

## Busque na web

Filtre 16,811 projetos por categoria, linguagem e saúde, ordenados por estrelas ou atividade recente. Toda busca tem um link para compartilhar.

<p align="center"><a href="https://alexgaoth.github.io/awesome-reverse-engineered/"><img src="assets/site.png" alt="Busque na web" width="820"></a></p>

<p align="center"><a href="https://alexgaoth.github.io/awesome-reverse-engineered/"><b>Abrir a busca →</b></a></p>

## Em alta nesta semana

Os projetos com mais estrelas que receberam commits nos últimos 7 dias.

| Projeto | O que faz | ★ | Saúde | Linguagem |
|---|---|--:|:-:|---|
| [rea](https://github.com/morluto/rea) | Agentic tool to reverse engineer apps from behavior down to native binaries | 375,489 | 🟢 | TypeScript |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | A feature-rich command-line audio/video downloader | 201,235 | 🟢 | Python |
| [claw-code](https://github.com/ultraworkers/claw-code) | Clean-room Rust/Python rewrite of the Claude Code agent harness after the source leak | 195,068 | 🟢 | Rust |
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | NSA's software reverse engineering framework with decompiler | 93,800 | 🟢 | Java |
| [PhotoCraft](https://github.com/storytold/photocraft) | Clean-room Photoshop-style photo editor written from scratch in pure Rust | 72,140 | 🟢 | Rust |
| [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Archive of extracted system prompts from ChatGPT, Claude, Gemini, Grok and others, per vendor with history | 70,126 | 🟢 | Python |
| [vaultwarden](https://github.com/dani-garcia/vaultwarden) | Unofficial Bitwarden-compatible server written in Rust | 69,572 | 🟢 | Rust |
| [gpt4free](https://github.com/xtekky/gpt4free) | Reverse-engineered third-party provider APIs giving free access to GPT-4 and other LLMs | 66,918 | 🟢 | Python |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Multimedia framework with many reverse-engineered proprietary codecs and containers | 65,627 | 🟢 | C |
| [openpilot](https://github.com/commaai/openpilot) | Open-source driver assistance system for 300+ car models | 63,986 | 🟢 | Python |

## Adicionados recentemente

| Projeto | O que faz | ★ | Saúde | Linguagem |
|---|---|--:|:-:|---|
| [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | Static and dynamic analysis framework for Android and iOS app packages | 22,025 | 🟢 | Python |
| [YoutubeDownloader](https://github.com/Tyrrrz/YoutubeDownloader) | Desktop app that downloads YouTube videos and playlists via YouTube's internal API | 16,522 | 🟢 | C# |
| [LunaTranslator](https://github.com/HIllya51/LunaTranslator) | Visual novel translator that hooks game text from running Windows games | 13,877 | 🟢 | C++ |
| [Corkami pics](https://github.com/corkami/pics) | Visual dissections and posters of binary file formats | 11,498 | 🟡 | Assembly |
| [FLARE-VM](https://github.com/mandiant/flare-vm) | Installer that sets up a Windows VM for reverse engineering and malware analysis | 9,182 | 🟢 | PowerShell |
| [GEF](https://github.com/hugsy/gef) | GDB extension that adds dynamic-analysis commands and context views | 8,403 | 🟢 | Python |
| [Minecraft Forge](https://github.com/MinecraftForge/MinecraftForge) | Modding API and loader for Minecraft: Java Edition | 7,834 | 🟢 | Java |
| [hooker](https://github.com/CreditTone/hooker) | Frida-based Android reverse engineering toolkit with CLI and universal scripts | 5,330 | 🟢 | JavaScript |
| [replica-skill](https://github.com/Jakeschincariol/replica-skill) | Claude skills that reverse engineer an app, rebuild it, test it and fix user-reported issues | 5,120 | 🟢 | Python |
| [dlssg-to-fsr3](https://github.com/Nukem9/dlssg-to-fsr3) | Replaces DLSS Frame Generation with FSR 3 frame generation in games | 4,977 | 🟡 | C++ |
| [GDA](https://github.com/charles2gan/GDA-android-reversing-Tool) | Windows-native Dalvik decompiler and Android analysis workbench | 4,868 | 🟢 | Python |
| [D2R Mobile](https://github.com/jhaizhou-ops/d2r-mobile) | Runs the Switch build of Diablo II: Resurrected natively on iPhone, iPad and Apple silicon Macs | 4,518 | 🟢 | C |
| [Zydis](https://github.com/zyantific/zydis) | Fast x86/x86-64 disassembler and encoder library in C | 4,395 | 🟢 | C |
| [wxapkg](https://github.com/wux1an/wxapkg) | Desktop GUI that unpacks WeChat mini-program .wxapkg packages | 4,301 | 🟢 | Vue |
| [FLOSS](https://github.com/mandiant/flare-floss) | Extracts obfuscated, stack and tight strings from malware binaries | 4,199 | 🟢 | Python |

## Mais estrelados

| # | Projeto | O que faz | ★ | Saúde | Linguagem |
|--:|---|---|--:|:-:|---|
| 1 | [rea](https://github.com/morluto/rea) | Agentic tool to reverse engineer apps from behavior down to native binaries | 375,489 | 🟢 | TypeScript |
| 2 | [yt-dlp](https://github.com/yt-dlp/yt-dlp) | A feature-rich command-line audio/video downloader | 201,235 | 🟢 | Python |
| 3 | [claw-code](https://github.com/ultraworkers/claw-code) | Clean-room Rust/Python rewrite of the Claude Code agent harness after the source leak | 195,068 | 🟢 | Rust |
| 4 | [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Extracted system prompts and tool definitions for Cursor, Claude Code, Devin, Windsurf, Kiro, v0, Lovable and more | 144,212 | 🟢 |  |
| 5 | [youtube-dl](https://github.com/ytdl-org/youtube-dl) | Command-line program to download videos from YouTube.com and other video sites | 141,376 | 🟢 | Python |
| 6 | [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | NSA's software reverse engineering framework with decompiler | 93,800 | 🟢 | Java |
| 7 | [PhotoCraft](https://github.com/storytold/photocraft) | Clean-room Photoshop-style photo editor written from scratch in pure Rust | 72,140 | 🟢 | Rust |
| 8 | [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Archive of extracted system prompts from ChatGPT, Claude, Gemini, Grok and others, per vendor with history | 70,126 | 🟢 | Python |
| 9 | [vaultwarden](https://github.com/dani-garcia/vaultwarden) | Unofficial Bitwarden-compatible server written in Rust | 69,572 | 🟢 | Rust |
| 10 | [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | Crawler for Xiaohongshu, Douyin, Kuaishou, Bilibili and Weibo posts and comments | 68,072 | 🟢 | Python |
| 11 | [gpt4free](https://github.com/xtekky/gpt4free) | Reverse-engineered third-party provider APIs giving free access to GPT-4 and other LLMs | 66,918 | 🟢 | Python |
| 12 | [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Multimedia framework with many reverse-engineered proprietary codecs and containers | 65,627 | 🟢 | C |
| 13 | [openpilot](https://github.com/commaai/openpilot) | Open-source driver assistance system for 300+ car models | 63,986 | 🟢 | Python |
| 14 | [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | Wraps Codex, Claude Code, Antigravity, Grok and Gemini CLI OAuth backends as OpenAI/Claude-compatible APIs | 56,122 | 🟢 | Go |
| 15 | [ImHex](https://github.com/WerWolv/ImHex) | Hex editor for reverse engineers with a pattern language for binary formats | 55,543 | 🟢 | C++ |
| 16 | [lx-music-desktop](https://github.com/lyswhut/lx-music-desktop) | LX Music: desktop music player aggregating Chinese music platform sources | 54,715 | 🟢 | TypeScript |
| 17 | [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | Leaked system prompts and tool specs for ChatGPT, Claude, Gemini, Grok, Perplexity, Cursor, Lovable, Replit and others | 51,473 | 🟢 |  |
| 18 | [jadx](https://github.com/skylot/jadx) | Dex to Java decompiler for Android apps | 51,229 | 🟢 | Java |
| 19 | [alist](https://github.com/AlistGo/alist) | AList: file list and WebDAV server that mounts many cloud drives through their private APIs | 50,350 | 🟢 | Go |
| 20 | [Spotube](https://github.com/team-spotube/spotube) | Cross-platform Spotify client that streams audio from other sources | 50,263 | 🟢 | Dart |
| 21 | [x64dbg](https://github.com/x64dbg/x64dbg) | Open source user-mode debugger for Windows | 50,007 | 🟢 | C++ |
| 22 | [mitmproxy](https://github.com/mitmproxy/mitmproxy) | Interactive TLS-capable intercepting HTTP proxy | 46,266 | 🟢 | Python |
| 23 | [sub2api](https://github.com/Wei-Shaw/sub2api) | Relay that exposes Claude, OpenAI, Gemini and Grok subscriptions as unified APIs | 44,741 | 🟢 | Go |
| 24 | [Sunshine](https://github.com/LizardByte/Sunshine) | Self-hosted game stream host that implements the NVIDIA GameStream protocol for Moonlight clients | 42,566 | 🟢 | C++ |
| 25 | [fastlane](https://github.com/fastlane/fastlane) | iOS/Android release automation; its spaceship module wraps Apple's private developer portal and App Store Connect APIs | 42,292 | 🟢 | Ruby |

## Saúde

| | Significado |
|:-:|---|
| 🟢 | Ativo: push nos últimos 12 meses |
| 🟡 | Desacelerando: último push há 1 a 3 anos |
| 🔴 | Parado: sem push há mais de 3 anos |
| 🗄️ | Arquivado pelo dono |
| ⚪ | Desconhecido: não hospedado no GitHub |

APIs não oficiais quebram quando o fabricante muda algo do lado dele. Confira a saúde de um projeto antes de depender dele.

## Como é feito

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

Dados brutos: [`data/entries.json`](data/entries.json). Repos removidos: [`data/removed.json`](data/removed.json). Listas importadas e buscas: [SOURCES.md](SOURCES.md).

### Como filtramos

| | |
|--:|---|
| 3,099 | buscas no GitHub, Hacker News, Reddit e na web |
| 348 | listas e coleções existentes importadas |
| 173 | repos descartados pelo filtro de escopo (exploits, jailbreaks, burlas de segurança, DRM, cheats). Os agentes de pesquisa também os descartam antes desta etapa. |
| 16,811 | repos no índice, cada um verificado pela API do GitHub (existência, URL canônica, estrelas, licença) |
| 1,051 | arquivados pelos donos: mantidos e marcados com 🗄️ |
| 45 | removidos pela verificação noturna porque o repo foi apagado ou ficou privado ([lista](data/removed.json)) |

<p align="center"><img src="assets/categories.svg" alt="Projects per category" width="820"></p>

## Escopo

Este índice reúne projetos de **interoperabilidade, preservação e pesquisa**: clientes e SDKs não oficiais, drivers abertos, bibliotecas de controle local, leitores de formatos de arquivo, documentação de protocolos, reimplementações e decompilações. A engenharia reversa para fins de interoperabilidade é protegida em muitos lugares (por exemplo, 17 U.S.C. §1201(f) e o artigo 6 da Diretiva Europeia de Software).

**Deixado de fora de propósito:** exploits e jailbreaks, burla de segurança ou de certificate pinning, ferramentas de descriptografia, cheats, remoção de DRM ou paywall, resolvedores de CAPTCHA, bots de contas e ferramentas de credenciais.

Usar um cliente não oficial pode violar os termos de uso de um serviço. Use estes projetos com suas próprias contas, dispositivos e dados.

## Como contribuir

Conhece um projeto que deveria estar aqui? [Abra uma issue](https://github.com/alexgaoth/awesome-reverse-engineered/issues/new?title=Add%3A%20&body=Repo%3A%20%0AWhat%20it%20reverse%20engineers%3A%20) com o link do repo e uma linha dizendo de que produto ele faz engenharia reversa, ou envie um PR que o adicione a `data/entries.json`. Categoria errada, link quebrado ou fora do escopo? Abra uma issue também.

Curadoria de [@alexgaoth](https://github.com/alexgaoth) com agentes de pesquisa. Cada entrada é verificada pela API do GitHub.

## Seu projeto está na lista?

[![Listed in Awesome Reverse-Engineered](https://img.shields.io/badge/listed%20in-awesome--reverse--engineered-ffb000?style=flat-square&labelColor=0e0f0d)](https://github.com/alexgaoth/awesome-reverse-engineered)

Adicione este selo ao seu README. No [site](https://alexgaoth.github.io/awesome-reverse-engineered/), cada projeto tem um botão **badge** que copia uma versão com link para a própria entrada.

```markdown
[![Listed in Awesome Reverse-Engineered](https://img.shields.io/badge/listed%20in-awesome--reverse--engineered-ffb000?style=flat-square&labelColor=0e0f0d)](https://github.com/alexgaoth/awesome-reverse-engineered)
```

## Histórico de estrelas

<a href="https://star-history.com/#alexgaoth/awesome-reverse-engineered&Date"><img src="https://api.star-history.com/svg?repos=alexgaoth/awesome-reverse-engineered&type=Date" alt="Star history" width="600"></a>

## Licença

Código (scripts, site, skill para agentes): [MIT](LICENSE). Lista e dados: [CC0 1.0](LICENSE-DATA). Cada projeto listado tem sua própria licença.

<div align="center">

**Se isso te poupou de fazer engenharia reversa por conta própria, [deixe uma estrela](https://github.com/alexgaoth/awesome-reverse-engineered).**

</div>
