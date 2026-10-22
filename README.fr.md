<div align="center">

<a href="https://alexgaoth.github.io/awesome-reverse-engineered/"><img src="assets/banner.svg" alt="Awesome Reverse-Engineered" width="100%"></a>

<p><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <b>Français</b> · <a href="README.es.md">Español</a></p>

## Ne faites pas la rétro-ingénierie deux fois.

12,865 outils open source qui existent parce que quelqu'un a fait la rétro-ingénierie d'un produit fermé : application, API, appareil, protocole, format de fichier, jeu ou outil d'IA.

**[Rechercher dans l'index](https://alexgaoth.github.io/awesome-reverse-engineered/)** ou confiez-le à votre agent : `npx skills add alexgaoth/awesome-reverse-engineered`

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) [![Projects](https://img.shields.io/badge/projects-12%2C865-ffb000?style=flat-square&labelColor=0e0f0d)](#contenu) [![Nightly refresh](https://img.shields.io/github/actions/workflow/status/alexgaoth/awesome-reverse-engineered/refresh.yml?style=flat-square&label=nightly%20refresh&labelColor=0e0f0d)](.github/workflows/refresh.yml) [![Stars](https://img.shields.io/github/stars/alexgaoth/awesome-reverse-engineered?style=flat-square&labelColor=0e0f0d&color=ffb000)](https://github.com/alexgaoth/awesome-reverse-engineered/stargazers) [![License: MIT + CC0 data](https://img.shields.io/badge/license-MIT%20%2B%20CC0%20data-30363d?style=flat-square&labelColor=0e0f0d)](LICENSE)

**[Skill pour agents](#donnez-tout-lindex-à-votre-agent-ia)** · **[Catégories](#contenu)** · **[Populaires cette semaine](#populaires-cette-semaine)** · **[Proposer un projet](#contribuer)**

<sub>Les noms et descriptions des projets restent en anglais.</sub>

</div>

---

## Avant de faire de la rétro-ingénierie

Les agents et des outils comme [REA](https://github.com/morluto/rea) et [Ghidra](https://github.com/NationalSecurityAgency/ghidra) rendent la rétro-ingénierie plus rapide que jamais. Pourtant, l'application, l'API, l'appareil ou le format de fichier que vous allez ouvrir a souvent déjà été étudié, et le travail dort dans un dépôt que personne ne cite.

1. **Cherchez d'abord.** Sur le [site](https://alexgaoth.github.io/awesome-reverse-engineered/) ou avec le [skill pour agents](#donnez-tout-lindex-à-votre-agent-ia), par produit, fabricant ou protocole.
2. **Trouvé ?** Utilisez-le, corrigez-le et signalez les problèmes en amont. Un client maintenu vaut mieux que dix scripts privés.
3. **Rien trouvé ?** Faites le travail, publiez-le en open source, puis [ajoutez-le ici](#contribuer) pour que la personne suivante reparte de là où vous vous êtes arrêté.

## Contenu

**12,865 projets** qui cumulent **10.7 M** d'étoiles GitHub : 7,080 actifs, 1,947 au ralenti, 2,492 en sommeil, 898 archivés. Langages principaux : Python (3,298), C++ (1,859), C (1,693), JavaScript (841), TypeScript (736).

| Catégorie | Projets | Sélection |
|---|--:|---|
| [**Outils d'IA et clients LLM**](categories/ai-tools-llm-clients.md) | 737 | [claw-code](https://github.com/ultraworkers/claw-code), [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools), [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) |
| [**Décompilations et réimplémentations de jeux**](categories/game-decompilations-reimplementations.md) | 3,034 | [shadPS4](https://github.com/shadps4-emu/shadPS4), [v86](https://github.com/copy/v86), [RPCS3](https://github.com/RPCS3/rpcs3) |
| [**Appareils, IoT et matériel**](categories/devices-iot-hardware.md) | 3,028 | [KOReader](https://github.com/koreader/koreader), [LibrePods](https://github.com/librepods-org/librepods), [OpenLogi](https://github.com/AprilNEA/OpenLogi) |
| [**Clients d'API web et mobiles non officielles**](categories/unofficial-web-app-api-clients.md) | 904 | [yt-dlp](https://github.com/yt-dlp/yt-dlp), [youtube-dl](https://github.com/ytdl-org/youtube-dl), [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) |
| [**Messageries et réseaux sociaux**](categories/messaging-social-apps.md) | 296 | [WeChatMsg](https://github.com/LC044/WeChatMsg), [ItChat](https://github.com/littlecodersh/ItChat), [wechaty](https://github.com/wechaty/wechaty) |
| [**Clients tiers**](categories/third-party-clients.md) | 190 | [spotify-tui](https://github.com/Rigellute/spotify-tui), [nuclear](https://github.com/nukeop/nuclear), [SimpMusic](https://github.com/maxrave-dev/SimpMusic) |
| [**Plateformes chinoises et asiatiques**](categories/chinese-asian-platforms.md) | 324 | [lx-music-desktop](https://github.com/lyswhut/lx-music-desktop), [alist](https://github.com/AlistGo/alist), [12306](https://github.com/testerSunshine/12306) |
| [**Écosystème Apple**](categories/apple-ecosystem.md) | 340 | [fastlane](https://github.com/fastlane/fastlane), [homebridge](https://github.com/homebridge/homebridge), [OSX-KVM](https://github.com/kholia/OSX-KVM) |
| [**Pilotes et matériel bas niveau**](categories/drivers-low-level-hardware.md) | 432 | [MonitorControl](https://github.com/MonitorControl/MonitorControl), [tinygrad](https://github.com/tinygrad/tinygrad), [G-Helper](https://github.com/seerge/g-helper) |
| [**Automobile**](categories/automotive.md) | 520 | [openpilot](https://github.com/commaai/openpilot), [evcc](https://github.com/evcc-io/evcc), [VESC firmware](https://github.com/vedderb/bldc) |
| [**Automatisation industrielle et du bâtiment**](categories/industrial-building-automation.md) | 291 | [HslCommunication](https://github.com/dathlin/HslCommunication), [plc4x](https://github.com/apache/plc4x), [IoTClient](https://github.com/zhaopeiym/IoTClient) |
| [**Firmware et embarqué**](categories/firmware-embedded.md) | 472 | [LEDE (Lean)](https://github.com/coolsnowwolf/lede), [OpenWrt](https://github.com/openwrt/openwrt), [Tasmota](https://github.com/arendst/Tasmota) |
| [**Protocoles réseau et filaires**](categories/network-wire-protocols.md) | 422 | [Sunshine](https://github.com/LizardByte/Sunshine), [moonlight-qt](https://github.com/moonlight-stream/moonlight-qt), [Impacket](https://github.com/fortra/impacket) |
| [**Formats de fichiers**](categories/file-formats.md) | 435 | [FFmpeg](https://github.com/FFmpeg/FFmpeg), [ImHex](https://github.com/WerWolv/ImHex), [SheetJS](https://github.com/SheetJS/sheetjs) |
| [**Services en ligne ressuscités**](categories/online-service-revivals.md) | 173 | [NoLongerEvil Thermostat](https://github.com/codykociemba/NoLongerEvil-Thermostat), [Legacy Update](https://github.com/LegacyUpdate/LegacyUpdate), [wire-pod](https://github.com/kercre123/wire-pod) |
| [**Réimplémentations de logiciels de bureau**](categories/desktop-software-reimplementations.md) | 201 | [PhotoCraft](https://github.com/storytold/photocraft), [vaultwarden](https://github.com/dani-garcia/vaultwarden), [Proton](https://github.com/ValveSoftware/Proton) |
| [**Frontends alternatifs**](categories/alternative-frontends.md) | 121 | [searxng](https://github.com/searxng/searxng), [searx](https://github.com/searx/searx), [Whoogle Search](https://github.com/benbusby/whoogle-search) |
| [**Applications mobiles**](categories/mobile-apps.md) | 102 | [revanced-manager](https://github.com/ReVanced/revanced-manager), [Metrolist](https://github.com/MetrolistGroup/Metrolist), [LibreTube](https://github.com/libre-tube/LibreTube) |
| [**Outils de rétro-ingénierie**](categories/re-tooling.md) | 740 | [rea](https://github.com/morluto/rea), [Ghidra](https://github.com/NationalSecurityAgency/ghidra), [jadx](https://github.com/skylot/jadx) |
| [**Collections et listes Awesome**](categories/collections-awesome-lists.md) | 103 | [awesome reverse-engineering (wtsxDev)](https://github.com/wtsxDev/reverse-engineering), [android-security-awesome](https://github.com/ashishb/android-security-awesome), [mendel5/alternative-front-ends](https://github.com/mendel5/alternative-front-ends) |

## Donnez tout l'index à votre agent IA

Quand une tâche doit communiquer avec quelque chose qui n'a pas d'API officielle (une prise connectée, une voiture, une messagerie, un format de fichier), votre agent cherche dans cet index, trie par étoiles, activité et licence, lit le README et choisit le bon outil.

```bash
npx skills add alexgaoth/awesome-reverse-engineered
```

<details><summary><b>Autres méthodes d'installation</b></summary>

**Plugin Claude Code**

```
/plugin install reverse-engineered --marketplace alexgaoth/awesome-reverse-engineered
```

**Serveur MCP (Claude Desktop, Cursor, tout client MCP)**

```bash
claude mcp add reverse-engineered -- uvx --from "git+https://github.com/alexgaoth/awesome-reverse-engineered#subdirectory=mcp" reverse-engineered-mcp
```

```json
{"mcpServers": {"reverse-engineered": {"command": "uvx", "args": ["--from", "git+https://github.com/alexgaoth/awesome-reverse-engineered#subdirectory=mcp", "reverse-engineered-mcp"]}}}
```

**N'importe quel agent ou terminal (un seul fichier, uniquement la bibliothèque standard Python)**

```bash
curl -sL https://raw.githubusercontent.com/alexgaoth/awesome-reverse-engineered/main/plugin/skills/find-reverse-engineered/scripts/re_index.py -o re_index.py
python3 re_index.py search tuya local          # ranked matches
python3 re_index.py info make-all/tuya-local   # entry + README excerpt
python3 re_index.py clone make-all/tuya-local  # shallow clone into vendor/
```

</details>

<p align="center"><img src="assets/demo.svg" alt="find-reverse-engineered" width="820"></p>
<p align="center"><sub>Sortie réelle du skill sur les données actuelles.</sub></p>

## Rechercher sur le web

Filtrez 12,865 projets par catégorie, langage et état de santé, triés par étoiles ou par activité récente. Chaque recherche a un lien partageable.

<p align="center"><a href="https://alexgaoth.github.io/awesome-reverse-engineered/"><img src="assets/site.png" alt="Rechercher sur le web" width="820"></a></p>

<p align="center"><a href="https://alexgaoth.github.io/awesome-reverse-engineered/"><b>Ouvrir la recherche →</b></a></p>

## Populaires cette semaine

Les projets les plus étoilés qui ont reçu des commits ces 7 derniers jours.

| Projet | Ce qu'il fait | ★ | Santé | Langage |
|---|---|--:|:-:|---|
| [rea](https://github.com/morluto/rea) | Agentic tool to reverse engineer apps from behavior down to native binaries | 362,229 | 🟢 | TypeScript |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | A feature-rich command-line audio/video downloader | 200,290 | 🟢 | Python |
| [claw-code](https://github.com/ultraworkers/claw-code) | Clean-room Rust/Python rewrite of the Claude Code agent harness after the source leak | 195,073 | 🟢 | Rust |
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | NSA's software reverse engineering framework with decompiler | 92,885 | 🟢 | Java |
| [PhotoCraft](https://github.com/storytold/photocraft) | Clean-room Photoshop-style photo editor written from scratch in pure Rust | 70,984 | 🟢 | Rust |
| [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Archive of extracted system prompts from ChatGPT, Claude, Gemini, Grok and others, per vendor with history | 70,024 | 🟢 | Python |
| [vaultwarden](https://github.com/dani-garcia/vaultwarden) | Unofficial Bitwarden-compatible server written in Rust | 69,455 | 🟢 | Rust |
| [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | Crawler for Xiaohongshu, Douyin, Kuaishou, Bilibili and Weibo posts and comments | 67,681 | 🟢 | Python |
| [gpt4free](https://github.com/xtekky/gpt4free) | Reverse-engineered third-party provider APIs giving free access to GPT-4 and other LLMs | 66,921 | 🟢 | Python |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Multimedia framework with many reverse-engineered proprietary codecs and containers | 65,556 | 🟢 | C |

## Les plus étoilés

| # | Projet | Ce qu'il fait | ★ | Santé | Langage |
|--:|---|---|--:|:-:|---|
| 1 | [rea](https://github.com/morluto/rea) | Agentic tool to reverse engineer apps from behavior down to native binaries | 362,229 | 🟢 | TypeScript |
| 2 | [yt-dlp](https://github.com/yt-dlp/yt-dlp) | A feature-rich command-line audio/video downloader | 200,290 | 🟢 | Python |
| 3 | [claw-code](https://github.com/ultraworkers/claw-code) | Clean-room Rust/Python rewrite of the Claude Code agent harness after the source leak | 195,073 | 🟢 | Rust |
| 4 | [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Extracted system prompts and tool definitions for Cursor, Claude Code, Devin, Windsurf, Kiro, v0, Lovable and more | 144,171 | 🟢 |  |
| 5 | [youtube-dl](https://github.com/ytdl-org/youtube-dl) | Command-line program to download videos from YouTube.com and other video sites | 141,372 | 🟢 | Python |
| 6 | [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | NSA's software reverse engineering framework with decompiler | 92,885 | 🟢 | Java |
| 7 | [PhotoCraft](https://github.com/storytold/photocraft) | Clean-room Photoshop-style photo editor written from scratch in pure Rust | 70,984 | 🟢 | Rust |
| 8 | [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Archive of extracted system prompts from ChatGPT, Claude, Gemini, Grok and others, per vendor with history | 70,024 | 🟢 | Python |
| 9 | [vaultwarden](https://github.com/dani-garcia/vaultwarden) | Unofficial Bitwarden-compatible server written in Rust | 69,455 | 🟢 | Rust |
| 10 | [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | Crawler for Xiaohongshu, Douyin, Kuaishou, Bilibili and Weibo posts and comments | 67,681 | 🟢 | Python |
| 11 | [gpt4free](https://github.com/xtekky/gpt4free) | Reverse-engineered third-party provider APIs giving free access to GPT-4 and other LLMs | 66,921 | 🟢 | Python |
| 12 | [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Multimedia framework with many reverse-engineered proprietary codecs and containers | 65,556 | 🟢 | C |
| 13 | [openpilot](https://github.com/commaai/openpilot) | Open-source driver assistance system for 300+ car models | 63,964 | 🟢 | Python |
| 14 | [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | Wraps Codex, Claude Code, Antigravity, Grok and Gemini CLI OAuth backends as OpenAI/Claude-compatible APIs | 55,961 | 🟢 | Go |
| 15 | [ImHex](https://github.com/WerWolv/ImHex) | Hex editor for reverse engineers with a pattern language for binary formats | 55,512 | 🟢 | C++ |
| 16 | [lx-music-desktop](https://github.com/lyswhut/lx-music-desktop) | LX Music: desktop music player aggregating Chinese music platform sources | 54,647 | 🟢 | TypeScript |
| 17 | [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | Leaked system prompts and tool specs for ChatGPT, Claude, Gemini, Grok, Perplexity, Cursor, Lovable, Replit and others | 51,440 | 🟢 |  |
| 18 | [jadx](https://github.com/skylot/jadx) | Dex to Java decompiler for Android apps | 51,183 | 🟢 | Java |
| 19 | [alist](https://github.com/AlistGo/alist) | AList: file list and WebDAV server that mounts many cloud drives through their private APIs | 50,338 | 🟢 | Go |
| 20 | [Spotube](https://github.com/team-spotube/spotube) | Cross-platform Spotify client that streams audio from other sources | 50,191 | 🟢 | Dart |
| 21 | [x64dbg](https://github.com/x64dbg/x64dbg) | Open source user-mode debugger for Windows | 49,984 | 🟢 | C++ |
| 22 | [mitmproxy](https://github.com/mitmproxy/mitmproxy) | Interactive TLS-capable intercepting HTTP proxy | 46,045 | 🟢 | Python |
| 23 | [sub2api](https://github.com/Wei-Shaw/sub2api) | Relay that exposes Claude, OpenAI, Gemini and Grok subscriptions as unified APIs | 44,590 | 🟢 | Go |
| 24 | [Sunshine](https://github.com/LizardByte/Sunshine) | Self-hosted game stream host that implements the NVIDIA GameStream protocol for Moonlight clients | 42,498 | 🟢 | C++ |
| 25 | [fastlane](https://github.com/fastlane/fastlane) | iOS/Android release automation; its spaceship module wraps Apple's private developer portal and App Store Connect APIs | 42,279 | 🟢 | Ruby |

## Santé

| | Signification |
|:-:|---|
| 🟢 | Actif : push dans les 12 derniers mois |
| 🟡 | Au ralenti : dernier push il y a 1 à 3 ans |
| 🔴 | En sommeil : aucun push depuis plus de 3 ans |
| 🗄️ | Archivé par son propriétaire |
| ⚪ | Inconnu : non hébergé sur GitHub |

Les API non officielles cassent dès que l'éditeur change quelque chose de son côté. Vérifiez la santé d'un projet avant d'en dépendre.

## Comment c'est construit

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

Données brutes : [`data/entries.json`](data/entries.json). Dépôts retirés : [`data/removed.json`](data/removed.json). Listes importées et recherches : [SOURCES.md](SOURCES.md).

### Comment nous filtrons

| | |
|--:|---|
| 2,458 | recherches sur GitHub, Hacker News, Reddit et le web |
| 290 | listes et collections existantes importées |
| 147 | dépôts écartés par le filtre de périmètre (exploits, jailbreaks, contournements, DRM, triche). Les agents de recherche les écartent aussi en amont. |
| 12,865 | dépôts dans l'index, chacun vérifié avec l'API GitHub (existence, URL canonique, étoiles, licence) |
| 898 | archivés par leurs propriétaires : conservés et marqués 🗄️ |
| 35 | retirés par la vérification nocturne car le dépôt a été supprimé ou rendu privé ([liste](data/removed.json)) |

<p align="center"><img src="assets/categories.svg" alt="Projects per category" width="820"></p>

## Périmètre

Cet index recense des projets d'**interopérabilité, de préservation et de recherche** : clients et SDK non officiels, pilotes libres, bibliothèques de contrôle local, parseurs de formats de fichiers, documentation de protocoles, réimplémentations et décompilations. La rétro-ingénierie à des fins d'interopérabilité est protégée dans de nombreux pays (par exemple 17 U.S.C. §1201(f) et l'article 6 de la directive européenne sur les programmes d'ordinateur).

**Exclus volontairement :** exploits et jailbreaks, contournement de sécurité ou de certificate pinning, outils de déchiffrement, triche, suppression de DRM ou de paywall, solveurs de CAPTCHA, bots de comptes et outils d'identifiants.

Utiliser un client non officiel peut enfreindre les conditions d'utilisation d'un service. Utilisez ces projets avec vos propres comptes, appareils et données.

## Contribuer

Vous connaissez un projet qui a sa place ici ? [Ouvrez une issue](https://github.com/alexgaoth/awesome-reverse-engineered/issues/new?title=Add%3A%20&body=Repo%3A%20%0AWhat%20it%20reverse%20engineers%3A%20) avec le lien du dépôt et une ligne sur ce qu'il rétro-conçoit, ou envoyez une PR qui l'ajoute à `data/entries.json`. Mauvaise catégorie, lien mort ou hors périmètre ? Ouvrez aussi une issue.

Organisé par [@alexgaoth](https://github.com/alexgaoth) avec des agents de recherche. Chaque entrée est vérifiée avec l'API GitHub.

## Votre projet est référencé ?

[![Listed in Awesome Reverse-Engineered](https://img.shields.io/badge/listed%20in-awesome--reverse--engineered-ffb000?style=flat-square&labelColor=0e0f0d)](https://github.com/alexgaoth/awesome-reverse-engineered)

Ajoutez ce badge à votre README. Sur le [site](https://alexgaoth.github.io/awesome-reverse-engineered/), chaque projet a un bouton **badge** qui copie une version pointant vers sa propre fiche.

```markdown
[![Listed in Awesome Reverse-Engineered](https://img.shields.io/badge/listed%20in-awesome--reverse--engineered-ffb000?style=flat-square&labelColor=0e0f0d)](https://github.com/alexgaoth/awesome-reverse-engineered)
```

## Historique des étoiles

<a href="https://star-history.com/#alexgaoth/awesome-reverse-engineered&Date"><img src="https://api.star-history.com/svg?repos=alexgaoth/awesome-reverse-engineered&type=Date" alt="Star history" width="600"></a>

## Licence

Code (scripts, site, skill pour agents) : [MIT](LICENSE). Liste et données : [CC0 1.0](LICENSE-DATA). Chaque projet référencé a sa propre licence.

<div align="center">

**Si cet index vous a évité de faire de la rétro-ingénierie vous-même, [mettez-lui une étoile](https://github.com/alexgaoth/awesome-reverse-engineered).**

</div>
