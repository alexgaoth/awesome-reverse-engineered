# AI Tools & LLM Clients

[← All categories](../README.md#whats-inside) · [Search this category on the website](https://alexgaoth.github.io/awesome-reverse-engineered/#c=ai-tools-llm-clients) · 740 projects · [Listed here? Get the badge](../README.md#is-your-project-listed)

Health: 🟢 pushed in the last year · 🟡 1 to 3 years · 🔴 over 3 years · 🗄️ archived · ⚪ unknown

- [AI Hardware & On-device Models](#ai-hardware--on-device-models) (55)
- [Chatbot Web APIs](#chatbot-web-apis) (193)
- [Chinese LLM Web APIs](#chinese-llm-web-apis) (49)
- [Coding Agents (Claude Code, Cursor, Copilot…)](#coding-agents-claude-code-cursor-copilot) (251)
- [Image/Audio/Video Gen APIs](#imageaudiovideo-gen-apis) (69)
- [MCP Servers for Private APIs](#mcp-servers-for-private-apis) (74)
- [Other AI](#other-ai) (20)
- [System Prompt Leaks & Extractions](#system-prompt-leaks--extractions) (29)

## AI Hardware & On-device Models

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [meta-glasses-api](https://github.com/dcrebbin/meta-glasses-api) | Messenger browser extension acting as an unofficial API for Meta Ray-Ban glasses | 696 | 🟡 | TypeScript |
| [riffado](https://github.com/riffado/riffado) | Self-hosted transcription interface for Plaud Note recordings | 427 | 🟢 | TypeScript |
| [reverse-engineering-gemma-3n](https://github.com/antimatter15/reverse-engineering-gemma-3n) | Reverse engineering of Google's Gemma 3n edge-optimized model architecture | 278 | 🟡 | Python |
| [dot2api](https://github.com/Pluviobyte/dot2api) | Turns the OpenAI Dot device into an OpenAI- and Claude-compatible API | 209 | 🟢 | Python |
| [even-g2-protocol (i-soxi)](https://github.com/i-soxi/even-g2-protocol) | Reverse-engineered BLE protocol of Even Realities G2 smart glasses | 191 | 🟢 |  |
| [TotalRecall](https://github.com/xaitax/TotalRecall) | Extracts and displays data from Windows 11 Copilot+ Recall snapshots database | 171 | 🟢 | C++ |
| [ANE-LM](https://github.com/johnmai-dev/ANE-LM) | LLM inference on the Apple Neural Engine | 145 | 🟢 | C++ |
| [Orion](https://github.com/mechramc/Orion) | Local runtime for training and running small LLMs on the Apple Neural Engine | 131 | 🟢 | Objective-C |
| [rk3588-npu](https://github.com/mtx512/rk3588-npu) | Reverse engineering the Rockchip RK3588 NPU | 130 | 🟡 | C |
| [applaud](https://github.com/rsteckler/applaud) | n8n support and local sync for Plaud devices | 103 | 🟢 | TypeScript |
| [snowman](https://github.com/Thalhammer/snowman) | Reimplementation of the Snowboy hotword detection engine | 96 | 🔴 | C++ |
| [v831-npu](https://github.com/mtx512/v831-npu) | Reverse engineering the Allwinner V831 NPU | 95 | 🔴 | C++ |
| [plaud-sync-for-obsidian](https://github.com/leonardsellem/plaud-sync-for-obsidian) | Obsidian plugin syncing Plaud recordings via reverse-engineered API | 90 | 🟢 | TypeScript |
| [codex-micro-4-core2](https://github.com/imliubo/codex-micro-4-core2) | Unofficial BLE Codex Micro firmware turning M5Stack Core2 into a ChatGPT Desktop controller | 79 | 🟢 | C++ |
| [Rabbit-R1 (Pinball3D)](https://github.com/Pinball3D/Rabbit-R1) | Rabbit R1 reverse engineering; runs the R1 launcher on any Android device | 78 | 🟡 | Smali |
| [npunlock](https://github.com/hsfzxjy/npunlock) | Write and run custom C kernels on Intel Core Ultra NPUs | 73 | 🟢 | C |
| [rabbit_r1_boot_notes](https://github.com/DavidBuchanan314/rabbit_r1_boot_notes) | Documents the boot process of the Rabbit R1 (MediaTek mt6765, Android 13) | 71 | 🟡 | Python |
| [OpenPin](https://github.com/MaxMaeder/OpenPin) | Makes the discontinued Humane Ai Pin usable again with a replacement software stack | 57 | 🟡 | TypeScript |
| [rokid-docs](https://github.com/buildwithfenna/rokid-docs) | Community docs for Rokid AR glasses incl. YodaOS internals and reverse-engineered details | 51 | 🟢 | Smali |
| [plaud-toolkit](https://github.com/sergivalverde/plaud-toolkit) | TypeScript library, CLI and MCP server for the Plaud API | 45 | 🟢 | TypeScript |
| [mabl](https://github.com/PenumbraOS/mabl) | Modular assistant replacing Humane's cloud assistant on the jailbroken Ai Pin | 41 | 🗄️ | Kotlin |
| [ane-infer](https://github.com/thebasedcapital/ane-infer) | Apple Neural Engine LLM inference using reverse-engineered private APIs | 32 | 🟢 | Rust |
| [omibutfree](https://github.com/kbdevs/omibutfree) | Free alternative app for the Omi AI wearable | 32 | 🟢 | Swift |
| [OpenPlod](https://github.com/RemiPelloux/OpenPlod) | Local-first Plaud Note Pro vault with direct Bluetooth import | 23 | 🟢 | TypeScript |
| [CodexMacro](https://github.com/Patchself/CodexMacro) | Android BLE controller implementing ChatGPT Desktop's Codex Micro HID-over-GATT protocol | 20 | 🟢 | Kotlin |
| [locus-tether](https://github.com/thecloudcowboy/locus-tether) | Self-hosted replacement for the Omi wearable's cloud pipeline | 17 | 🟢 | Python |
| [tinycoral](https://github.com/FrederikRogalski/tinycoral) | tinygrad on Coral Edge TPU with reverse-engineered ISA and USB driver | 17 | 🟢 | Python |
| [plaud-direct-pc-research](https://github.com/Shawn-TKD/plaud-direct-pc-research) | Direct-to-PC BLE interoperability research for PLAUD Note Pro/NotePin S | 16 | 🟢 | Kotlin |
| [evenRealities-webflasher](https://github.com/AM-Guru/evenRealities-webflasher) | Browser flasher and recovery console for Even Realities G2 and R1 | 15 | 🟢 | JavaScript |
| [cppRecall](https://github.com/otterpwn/cppRecall) | C++ dumper for Microsoft Recall database and screenshots | 14 | 🟡 | C |
| [even-g2-protocol (ithinkthisiscool)](https://github.com/ithinkthisiscool/even-g2-protocol) | Python implementation and protocol map of Even Realities G2 glasses | 14 | 🟢 | Python |
| [plaud-api](https://github.com/arbuzmell/plaud-api) | Unofficial Python client for Plaud AI recorders | 12 | 🟢 | Python |
| [openplaudit](https://github.com/mar-maradnus/openplaudit) | macOS app/CLI for PLAUD Note: BLE sync, Opus decode, Whisper | 11 | 🟢 | Swift |
| [luma](https://github.com/TheAndersMadsen/luma) | Self-hosted cloud and device runtime for an operator-owned Humane Ai Pin | 10 | 🟢 | Rust |
| [rabbit-r1-firmware](https://github.com/TurboTheTurtle/rabbit-r1-firmware) | Rabbit R1 flashing guides, scripts and hardware docs (CipherOS, LK analysis) | 10 | 🟢 | Shell |
| [ai-pin-interposer](https://github.com/agg23/ai-pin-interposer) | Hardware interposer for Humane AI Pin debug access | 8 | 🟡 |  |
| [humane-system-hook](https://github.com/PenumbraOS/humane-system-hook) | Hooks Humane's Ai Pin software so it functions after the cloud shutdown | 8 | 🟢 | Rust |
| [mic-rs](https://github.com/dariofinardi/mic-rs) | Downloads and decodes audio from Anker Soundcore Work and Plaud | 8 | 🟢 | Rust |
| [even-g2-patched](https://github.com/cokeeffekt/even-g2-patched) | Patched Even app + frida-gadget routing G2 voice commands to a custom AI agent | 7 | 🟢 | JavaScript |
| [PenumbraOS docs](https://github.com/PenumbraOS/docs) | Reverse engineering findings on the Humane Ai Pin | 7 | 🟡 |  |
| [ai-pin-apk-environment](https://github.com/agg23/ai-pin-apk-environment) | Environment for reverse engineering Humane AI Pin APKs | 6 | 🟡 |  |
| [rabbitude-backend](https://github.com/KibbeWater/rabbitude-backend) | Go reimplementation of the Rabbit R1 backend and API endpoints | 6 | 🟡 | Go |
| [unofficial-even-g2-local-assistant](https://github.com/marienbaptiste/unofficial-even-g2-local-assistant) | Local-first assistant talking to Even Realities G2 over BLE | 6 | 🟢 | Python |
| [installer](https://github.com/PenumbraOS/installer) | Installer for the PenumbraOS platform on the Humane Ai Pin | 5 | 🗄️ | Rust |
| [interposer](https://github.com/PenumbraOS/interposer) | USB interposer hardware for accessing the Humane Ai Pin | 5 | 🟡 |  |
| [plaude-cli](https://github.com/Sumatoshi-tech/plaude-cli) | Offline CLI for the Plaud Note voice recorder, no cloud or app | 5 | 🟢 | Rust |
| [rabbit-r1-hooks](https://github.com/sarkarsaurabh27/rabbit-r1-hooks) | Impersonates an OpenClaw gateway so a Rabbit R1 can drive Claude Code/Codex | 5 | 🟢 | TypeScript |
| [openrabbit](https://github.com/vcruz305/openrabbit) | Clean-room Rabbit R1 node client bridging to agents | 4 | 🟢 | TypeScript |
| [plaud (danielgwilson)](https://github.com/danielgwilson/plaud) | Agent-first CLI to export and download Plaud recordings | 4 | 🟢 | TypeScript |
| [RabbitKit](https://github.com/KibbeWater/RabbitKit) | Swift library for the Rabbit R1 protocol, used by an iOS app emulating the R1 | 4 | 🟡 | Swift |
| [Even-G2-RE](https://github.com/lonelyobserver0/Even-G2-RE) | Reverse engineering the Even G2 app and BLE system | 3 | 🟢 | Java |
| [g2-r1-re-tools-and-guide](https://github.com/Commute773/g2-r1-re-tools-and-guide) | RE tools and guides for Even G2 glasses and R1 health ring | 3 | 🟢 | TypeScript |
| [r1tool](https://github.com/nesdeq/r1tool) | CLI for hole.rabbit.tech: export Rabbit R1 photos and journal | 3 | 🟢 | Python |
| [rabbithole-api](https://github.com/meowstercatel/rabbithole-api) | API client for the Rabbit R1 RabbitHole service | 2 | 🟡 | TypeScript |
| [rockwrap](https://gitlab.freedesktop.org/icecream95/rockwrap) | Reverse engineering tools for the Rockchip RK356x/RK3588 NPU |  | ⚪ |  |

## Chatbot Web APIs

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [gpt4free](https://github.com/xtekky/gpt4free) | Reverse-engineered third-party provider APIs giving free access to GPT-4 and other LLMs | 66,927 | 🟢 | Python |
| [ChatGPT (revChatGPT)](https://github.com/acheong08/ChatGPT) | Reverse engineered ChatGPT web API client in Python (archived) | 27,966 | 🗄️ | Python |
| [notebooklm-py](https://github.com/teng-lin/notebooklm-py) | Unofficial NotebookLM Python API/CLI built on its undocumented internal RPC protocol | 19,892 | 🟢 | Python |
| [grok2api](https://github.com/chenyme/grok2api) | Multi-account API gateway for Grok Web, Grok Build and Grok Console | 7,851 | 🟢 | Go |
| [EdgeGPT](https://github.com/acheong08/EdgeGPT) | Reverse engineered API of Microsoft's Bing Chat (Sydney) AI | 7,829 | 🗄️ | Python |
| [gpt4free-ts](https://github.com/xiangsx/gpt4free-ts) | TypeScript replication of gpt4free reverse-engineered free GPT-4 provider API | 7,648 | 🟡 | TypeScript |
| [chatgpt2api (basketikun)](https://github.com/basketikun/chatgpt2api) | Pure-protocol reverse implementation of ChatGPT web incl. GPT-Image-2, OpenAI-compatible | 6,735 | 🟢 | Python |
| [openclaw-zero-token](https://github.com/linuxhsj/openclaw-zero-token) | OpenClaw using Claude/ChatGPT/Gemini/DeepSeek/Doubao web sessions, no API token | 5,205 | 🟢 | TypeScript |
| [Bard-API](https://github.com/dsdanielpark/Bard-API) | Unofficial Python package returning Google Bard responses via cookie value | 5,160 | 🗄️ | Python |
| [PyChatGPT](https://github.com/rawandahmad698/PyChatGPT) | Python client for the unofficial ChatGPT web API | 4,184 | 🟢 | Python |
| [node-chatgpt-api](https://github.com/waylaidwanderer/node-chatgpt-api) | Node.js client for ChatGPT and Bing AI with reverse-engineered endpoints | 4,150 | 🟡 | JavaScript |
| [chat2api](https://github.com/lanqian528/chat2api) | Converts ChatGPT web into OpenAI API format | 3,837 | 🟡 | Python |
| [Gemini-API](https://github.com/HanaokaYuzu/Gemini-API) | Reverse-engineered async Python API for the Google Gemini web app | 3,637 | 🟢 | Python |
| [gemini-web2api](https://github.com/Sophomoresty/gemini-web2api) | Converts Google Gemini web into an OpenAI-compatible API | 3,510 | 🟢 | Python |
| [FreeGPT35](https://github.com/missuo/FreeGPT35) | Free GPT-3.5 API from the login-free ChatGPT web | 3,210 | 🗄️ | JavaScript |
| [aurora](https://github.com/aurora-develop/aurora) | Free ChatGPT API from the login-free ChatGPT web | 2,583 | 🟢 | Go |
| [poe-api](https://github.com/ading2210/poe-api) | Reverse engineered Python API wrapper for Quora's Poe (unmaintained) | 2,460 | 🗄️ | Python |
| [perplexity-ai](https://github.com/helallao/perplexity-ai) | Unofficial API wrapper for the Perplexity.ai web interface | 1,984 | 🟢 | Python |
| [grok2api](https://github.com/jiujiu532/grok2api) | Grok web to OpenAI-compatible API proxy | 1,863 | 🟢 | Python |
| [ninja](https://github.com/0x676e67/ninja) | Reverse engineered ChatGPT web proxy (Rust) | 1,672 | 🗄️ | Rust |
| [ChatGPT-Mirror](https://github.com/dairoot/ChatGPT-Mirror) | Self-hosted ChatGPT web mirror site | 1,405 | 🟢 | Vue |
| [WebAI-to-API](https://github.com/Amm1rr/WebAI-to-API) | Exposes web chat UIs (Gemini, etc.) as an API | 1,402 | 🟢 | Python |
| [Bard](https://github.com/acheong08/Bard) | Python SDK for reverse engineered Google Bard | 1,390 | 🗄️ | Python |
| [pyChatGPT](https://github.com/terry3041/pyChatGPT) | Unofficial Python wrapper for ChatGPT web via browser session | 1,335 | 🗄️ | Python |
| [clewdr](https://github.com/Xerxes-2/clewdr) | High-performance Claude.ai web and Claude Code reverse proxy (Rust) | 1,291 | 🟢 | Rust |
| [PandoraNext-TokensTool](https://github.com/Yanyutin753/PandoraNext-TokensTool) | Manages and refreshes PandoraNext ChatGPT web tokens to run a free OpenAI-style relay | 1,276 | 🗄️ | Java |
| [Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | Reverse engineered Windows (Microsoft) Copilot into an OpenAI-compatible REST API | 1,255 | 🟢 | Python |
| [bing-chat](https://github.com/transitive-bullshit/bing-chat) | Reverse-engineered Bing AI Chat Node.js client | 1,205 | 🗄️ | TypeScript |
| [Proxima](https://github.com/Zen4-bit/Proxima) | MCP server driving ChatGPT, Claude, Gemini and Perplexity web sessions without API keys | 1,199 | 🟢 | JavaScript |
| [ChatGPT-to-API](https://github.com/acheong08/ChatGPT-to-API) | Go proxy turning the ChatGPT website into an OpenAI-compatible API | 1,135 | 🗄️ | Go |
| [poe-api-wrapper](https://github.com/snowby666/poe-api-wrapper) | Python API wrapper for Poe.com web giving access to GPT-4, Claude, Gemini and more | 1,090 | 🗄️ | Python |
| [hugging-chat-api](https://github.com/Soulter/hugging-chat-api) | Unofficial Python API for HuggingChat web | 938 | 🗄️ | Python |
| [free-one-api](https://github.com/RockChinQ/free-one-api) | Manages reverse-engineered LLM web APIs (ChatGPT, Bard, Claude, HuggingChat, Qwen) behind an OpenAI API | 932 | 🟢 | Rust |
| [Claude-API](https://github.com/KoushikNavuluri/Claude-API) | Unofficial Python API for claude.ai web using session cookie | 914 | 🟡 | Python |
| [Grok-Mirror](https://github.com/dairoot/Grok-Mirror) | Self-hosted Grok web mirror via reverse proxy | 913 | 🟢 | Shell |
| [SydneyQt](https://github.com/juzeon/SydneyQt) | Desktop client for jailbroken Bing AI / Copilot (Sydney) via its reverse engineered API | 870 | 🟡 | Go |
| [ds-free-api](https://github.com/NIyueeE/ds-free-api) | DeepSeek web API proxy with OpenAI and Anthropic compatible interfaces | 838 | 🟢 | Rust |
| [claude-unofficial-api](https://github.com/Explosion-Scratch/claude-unofficial-api) | Unofficial API client and CLI for Claude via the claude.ai web interface | 743 | 🔴 | JavaScript |
| [chat2api](https://github.com/aurorax-neo/chat2api) | ChatGPT web to API converter | 722 | 🟢 | Go |
| [Gemini-FastAPI](https://github.com/Nativu5/Gemini-FastAPI) | Web-based Gemini wrapped into an OpenAI-compatible API | 719 | 🟢 | Python |
| [grok2api](https://github.com/TQZHR/grok2api) | Grok2API on Cloudflare Workers | 704 | 🟢 | Python |
| [unofficial-chatgpt-api](https://github.com/taranjeet/unofficial-chatgpt-api) | Unofficial ChatGPT API via browser automation | 701 | 🔴 | Python |
| [gemini-web2api-go](https://github.com/zexadev/gemini-web2api-go) | Self-hosted OpenAI-compatible API proxying Gemini web | 689 | 🟢 | Go |
| [web2api](https://github.com/caiwuu/web2api) | Turns web AI chat interfaces (e.g. Claude) into APIs | 655 | 🟢 | Python |
| [claude2api](https://github.com/yushangxiao/claude2api) | Turns Claude.ai web into an API with image recognition and file upload | 642 | 🟡 | Go |
| [gemini-web-to-api](https://github.com/ntthanh2603/gemini-web-to-api) | Reverse-engineered Gemini web app API usable as an OpenAI/Gemini/Claude API key | 614 | 🟢 | Go |
| [M365-Copilot2API](https://github.com/HEXUXIU/M365-Copilot2API) | Microsoft 365 Copilot exposed as an OpenAI/Anthropic-compatible API gateway | 598 | 🟢 | Go |
| [everything-chatgpt](https://github.com/terminalcommandnewsletter/everything-chatgpt) | Documents the ChatGPT web app internals and its backend-api calls | 593 | 🔴 |  |
| [react-native-chatgpt](https://github.com/rgommezz/react-native-chatgpt) | Reverse-engineered ChatGPT web to provide a React Native wrapper | 585 | 🔴 | TypeScript |
| [grok2api_python](https://github.com/xLmiler/grok2api_python) | Python Grok web to OpenAI API proxy | 570 | 🟡 | HTML |
| [CharacterAI (kramcat)](https://github.com/kramcat/CharacterAI) | Unofficial Python API for character.ai using direct HTTP requests | 542 | 🟡 | Python |
| [grok3-api](https://github.com/mem0ai/grok3-api) | Unofficial Python client for Grok 3 reverse-engineering grok.com browser requests | 540 | 🗄️ | Python |
| [business2api](https://github.com/XxxXTeam/business2api) | OpenAI/Gemini-compatible proxy for the Gemini Business web API | 497 | 🟢 | Go |
| [poe-openai-proxy](https://github.com/juzeon/poe-openai-proxy) | Exposes the reverse-engineered poe-api library as an OpenAI-compatible API | 456 | 🟡 | Go |
| [GoogleBard](https://github.com/PawanOsman/GoogleBard) | Reverse engineered Google Bard API for Node.js | 418 | 🟡 | TypeScript |
| [meta-ai-api](https://github.com/Strvm/meta-ai-api) | Reverse engineered Meta AI (Llama 3) web chat API | 407 | 🟡 | Python |
| [codex-chatgpt-control](https://github.com/adamallcock/codex-chatgpt-control) | Unofficial SDK that lets agents drive logged-in ChatGPT web sessions | 406 | 🟢 | JavaScript |
| [Gemi2Api-Server](https://github.com/zhiyu1998/Gemi2Api-Server) | Server built on the reverse-engineered Gemini-API web client | 404 | 🟢 | HTML |
| [webchat2api](https://github.com/zqbxdev/webchat2api) | Self-hosted proxy unifying ChatGPT, Grok and Gemini web sessions into OpenAI API | 394 | 🟢 | Python |
| [deepseek4free](https://github.com/xtekky/deepseek4free) | DeepSeek private web chat API with reversed proof-of-work challenge | 392 | 🟡 | Python |
| [node_characterai](https://github.com/realcoloride/node_characterai) | Unofficial Character.AI wrapper for Node.js | 376 | 🟢 | JavaScript |
| [llm4free](https://github.com/OEvortex/llm4free) | Python toolkit for free LLM web providers and search | 375 | 🟢 | Python |
| [MackingJAI](https://github.com/0ssamaak0/MackingJAI) | Exposes Apple Intelligence and ChatGPT desktop app through OpenAI / Ollama APIs | 353 | 🟡 | Python |
| [FreeQwenApi](https://github.com/y13sint/FreeQwenApi) | Local API proxy for Qwen AI web chat with session management | 335 | 🟢 | JavaScript |
| [Claude2-PyAPI](https://github.com/wwwzhouhui/Claude2-PyAPI) | Python API for Claude.ai web sessions, chat, attachments and history | 319 | 🔴 | Python |
| [Deepseek-API](https://github.com/sums001/Deepseek-API) | Reverse engineered DeepSeek chat into an OpenAI-compatible REST API | 319 | 🟢 | Python |
| [Grok-Api](https://github.com/realasfngl/Grok-Api) | Python wrapper and FastAPI server for the Grok web interface (discontinued) | 314 | 🟢 | Python |
| [Poe](https://github.com/vaibhavk97/Poe) | Reverse engineered API for Quora's Poe chatbot service | 305 | 🔴 | Python |
| [reverse-engineered-chatgpt](https://github.com/Zai-Kun/reverse-engineered-chatgpt) | Unofficial reverse-engineered ChatGPT web API in Python | 294 | 🗄️ | Python |
| [sydney.py](https://github.com/vsakkas/sydney.py) | Python client for Microsoft Copilot (Bing Chat / Sydney) web | 291 | 🗄️ | Python |
| [perplexityai](https://github.com/nathanrchn/perplexityai) | Python API for perplexity.ai web | 289 | 🟡 | Python |
| [doubao2api](https://github.com/wangchuxiaoji-oss/doubao2api) | Reverse-engineered Doubao API as OpenAI-compatible REST service incl. image/video generation | 288 | 🟢 | Python |
| [yuanbao-free-api](https://github.com/chenwr727/yuanbao-free-api) | Access Tencent Yuanbao web chat through an OpenAI-compatible interface | 278 | 🟢 | Python |
| [refresh-gpt-chat](https://github.com/Yanyutin753/refresh-gpt-chat) | Relay for ChatGPT web v1 APIs using refresh tokens as keys | 244 | 🟡 | Java |
| [cpp-freegpt-webui](https://github.com/fantasy-peak/cpp-freegpt-webui) | C++ web UI and server using free reverse-engineered GPT providers | 236 | 🗄️ | C++ |
| [notebooklm-client](https://github.com/icebear0828/notebooklm-client) | NotebookLM CLI/library via reverse-engineered Boq RPC, incl. audio podcasts | 229 | 🟢 | TypeScript |
| [doubao-free-api](https://github.com/Bitsea1/doubao-free-api) | Reverse-engineered ByteDance Doubao chat API with search and image generation | 222 | 🟢 | TypeScript |
| [chat2api](https://github.com/xyhelper/chat2api) | ChatGPT web interface to API conversion gateway | 217 | 🗄️ | Go |
| [bing-chat-sidebar-for-chrome](https://github.com/wong2/bing-chat-sidebar-for-chrome) | Edge's Bing AI sidebar reverse engineered for Chrome | 213 | 🟢 | JavaScript |
| [Gemini-API](https://github.com/dsdanielpark/Gemini-API) | Unofficial Python package returning Google Gemini web responses via cookies | 207 | 🗄️ | Python |
| [intense-rp-next](https://github.com/LyubomirT/intense-rp-next) | Desktop app and OpenAI-compatible API proxying LLM web UIs | 200 | 🗄️ | Python |
| [revLibs](https://github.com/RockChinQ/revLibs) | Reverse-engineering library plugin for ChatGPT, Claude, Bard and gpt4free in QQ bots | 200 | 🟡 | Python |
| [vercel-llm-api](https://github.com/ading2210/vercel-llm-api) | Reverse engineered Python wrapper for the Vercel AI Playground | 189 | 🟡 | Python |
| [gpt4-openai-api](https://github.com/Erol444/gpt4-openai-api) | Unofficial Python access to GPT-4 through chat.openai.com, works with LangChain | 184 | 🟡 | Python |
| [chatbang](https://github.com/ahmedhosssam/chatbang) | CLI to use ChatGPT from the terminal without an API key via the web app | 181 | 🟡 | Go |
| [grok2api-rs](https://github.com/XeanYu/grok2api-rs) | Rust rewrite of Grok2API | 179 | 🟢 | Rust |
| [CatDesk](https://github.com/Xeift/CatDesk) | Uses ChatGPT web chat as a local coding agent | 177 | 🟢 | Rust |
| [python-tgpt](https://github.com/Simatwa/python-tgpt) | Terminal AI chat and REST API using free LLM web providers | 176 | 🟢 | Python |
| [gradio-chatbot](https://github.com/weaigc/gradio-chatbot) | Converts Hugging Face Spaces, ModelScope and Gradio chatbots into free APIs | 164 | 🟡 | TypeScript |
| [bingchat-api](https://github.com/tuhinpal/bingchat-api) | Unofficial Bing Chat API | 157 | 🗄️ | TypeScript |
| [claude2api](https://github.com/basketikun/claude2api) | Go Claude.ai web to API gateway with account pool and web mirror | 156 | 🟢 | Go |
| [ReEdgeGPT](https://github.com/Integration-Automation/ReEdgeGPT) | Maintained reverse-engineered Microsoft Bing Chat / Copilot API | 155 | 🗄️ | Python |
| [claude2api-deploy](https://github.com/realnoob007/claude2api-deploy) | Claude.ai web to API proxy | 152 | 🟢 |  |
| [EdgeGPT-Go](https://github.com/pavel-one/EdgeGPT-Go) | Go port of the reverse engineered Bing Chat API with gRPC and CLI | 152 | 🔴 | Go |
| [grok2api](https://github.com/aurora-develop/grok2api) | Grok web to OpenAI API reverse proxy | 150 | 🟢 | Go |
| [GPT_scraper](https://github.com/rodolflying/GPT_scraper) | Scrapes full ChatGPT user history through the hidden frontend backend API | 139 | 🔴 | Python |
| [llm-web-api](https://github.com/adryfish/llm-web-api) | Converts the ChatGPT web page into an API | 139 | 🟡 |  |
| [perplexity-webui-scraper](https://github.com/henrique-coder/perplexity-webui-scraper) | Python client, MCP server and REST API for Perplexity web UI | 137 | 🟢 | Python |
| [grok2api_new](https://github.com/Tomiya233/grok2api_new) | Grok web reverse proxy to OpenAI API with multi-account pooling | 134 | 🟢 | Python |
| [gemini2api](https://github.com/xwteam/gemini2api) | Gemini web to OpenAI/Claude/Gemini-compatible API via browser cookies | 126 | 🟢 | Python |
| [export-chatgpt](https://github.com/brianjlacy/export-chatgpt) | Exports all ChatGPT conversations via the web app's internal API | 125 | 🟢 | JavaScript |
| [WebChatGPT](https://github.com/Simatwa/WebChatGPT) | Python SDK for the ChatGPT web version | 124 | 🟡 | Python |
| [grok2api](https://github.com/VeroFess/grok2api) | Rewrite of Grok2API reverse proxy | 121 | 🟡 | Python |
| [Claude_api](https://github.com/Nipun1212/Claude_api) | Unofficial Python API for the claude.ai web chat | 120 | 🟡 | Python |
| [bard-ai](https://github.com/EvanZhouDev/bard-ai) | Reverse-engineered JavaScript client for the Google Bard web chat | 116 | 🔴 | JavaScript |
| [gpt4free.js](https://github.com/zachey01/gpt4free.js) | JavaScript port of gpt4free reverse-engineered providers | 115 | 🟡 | JavaScript |
| [poe](https://github.com/muharamdani/poe) | Reverse engineered API for Quora Poe | 115 | 🗄️ | TypeScript |
| [ChatGPT-PHP](https://github.com/tnborg/ChatGPT-PHP) | PHP SDK for ChatGPT with reverse engineered web API support | 112 | 🗄️ | PHP |
| [duck_chat](https://github.com/mrgick/duck_chat) | Reverse engineered DuckDuckGo AI Chat API client | 111 | 🟡 | Python |
| [ChatGPT](https://github.com/realasfngl/ChatGPT) | API wrapper for using ChatGPT web for free without paid API | 110 | 🟡 | Python |
| [m365-copilot-bridge](https://github.com/shenping1200/m365-copilot-bridge) | Microsoft 365 Copilot to OpenAI-compatible API gateway | 105 | 🟢 | Go |
| [chatgpt-java](https://github.com/arctisio/chatgpt-java) | Java library for ChatGPT via the reverse engineered web API | 104 | 🔴 | Java |
| [WebModel](https://github.com/linuxhsj/WebModel) | Use major AI models through their web sessions without API tokens | 103 | 🟢 | TypeScript |
| [LMarenaBridge](https://github.com/jtostrings/LMarenaBridge) | Desktop app exposing LMArena.ai models as an OpenAI-compatible API | 102 | 🟢 | JavaScript |
| [metaai-api](https://github.com/mir-ashiq/metaai-api) | FastAPI wrapper for Meta AI chat, image and video generation via cookies | 97 | 🟢 | Python |
| [PyCharacterAI](https://github.com/Xtr4F/PyCharacterAI) | Unofficial Python API wrapper for character.ai | 97 | 🟡 | Python |
| [notebooklm-rest-api](https://github.com/gnh1201/notebooklm-rest-api) | REST API wrapper for Google NotebookLM built on notebooklm-py | 92 | 🟢 | Python |
| [Bing-Chat-API](https://github.com/Agora-Lab-AI/Bing-Chat-API) | Unofficial API for Bing Chat (GPT-4) | 91 | 🟡 | Python |
| [ProGPT](https://github.com/diezo/ProGPT) | Reverse engineered Python client for ChatGPT web conversations | 90 | 🟢 | Python |
| [Gemini-Link-System](https://github.com/qxd-ljy/Gemini-Link-System) | Gateway converting Gemini Business API to OpenAI-compatible interface | 87 | 🟢 | Python |
| [headless-chatgpt](https://github.com/HalilCan/headless-chatgpt) | Puppeteer-based local API for the ChatGPT web interface | 86 | 🟡 | JavaScript |
| [ChatGPTReversed](https://github.com/gin337/ChatGPTReversed) | Free ChatGPT API reversed from the web client | 85 | 🟢 | TypeScript |
| [Google-Bard](https://github.com/LarryDpk/Google-Bard) | Java library for the reverse engineered Google Bard API | 85 | 🗄️ | Java |
| [NChatGPTRev](https://github.com/BruceQiu1996/NChatGPTRev) | C# ChatGPT SDK using the reverse engineered web API | 84 | 🗄️ | C# |
| [apibeam](https://github.com/NiteshSingh17/apibeam) | Converts a ChatGPT or Claude web account into an API | 83 | 🟢 | TypeScript |
| [chatgpt-web-voice](https://github.com/dyhhhhhh/chatgpt-web-voice) | Reverse-engineered ChatGPT.com web voice (realtime WebRTC + DataChannel) protocol | 77 | 🟢 | HTML |
| [edgegpt](https://github.com/KeJunMao/edgegpt) | Reverse engineering of the new Bing chat feature (Node.js) | 77 | 🗄️ | TypeScript |
| [unofficial-chatgpt-api](https://github.com/abacaj/unofficial-chatgpt-api) | Node.js client for the ChatGPT web API | 76 | 🟡 | TypeScript |
| [Claude2api](https://github.com/aurora-develop/Claude2api) | Claude.ai web to API proxy | 75 | 🟢 | Go |
| [openplayground-api](https://github.com/ading2210/openplayground-api) | Reverse engineered Python wrapper for OpenPlayground (nat.dev) | 74 | 🗄️ | Python |
| [PoeAPI](https://github.com/aspekts/PoeAPI) | Self-hostable reverse engineered Poe.com API | 69 | 🔴 | Python |
| [DuckDuckGo-AI](https://github.com/HuggingBear/DuckDuckGo-AI) | DuckDuckGo AI chat reverse engineered API on Cloudflare Workers | 65 | 🟡 | TypeScript |
| [gemini-webapi-mcp](https://github.com/AndyShaman/gemini-webapi-mcp) | MCP server for Gemini web via browser cookies (chat and image generation) | 65 | 🟢 | Python |
| [GLM-Free-API](https://github.com/xiaoY233/GLM-Free-API) | Reverse-engineered Zhipu ChatGLM web API with streaming and agent support | 64 | 🟢 | TypeScript |
| [m365-copilot-openai-proxy](https://github.com/kuchris/m365-copilot-openai-proxy) | Local proxy exposing Microsoft 365 Copilot as an OpenAI-compatible API | 64 | 🟢 | Python |
| [notionai-py](https://github.com/vaayne/notionai-py) | Unofficial Python SDK for Notion AI | 63 | 🟡 | Python |
| [Grok3API](https://github.com/boykopovar/Grok3API) | Async Python client for the Grok mobile private gRPC API | 62 | 🟢 | Python |
| [NotionAI-go](https://github.com/jyz0309/NotionAI-go) | Unofficial Notion AI Go SDK | 61 | 🔴 | Go |
| [CAINode](https://github.com/KevinAdhaikal/CAINode) | Lightweight unofficial Character.AI API for Node.js, Deno and Bun | 58 | 🟢 | JavaScript |
| [node-character.ai](https://github.com/RichardDorian/node-character.ai) | Unofficial API wrapper for Character.AI | 58 | 🗄️ | TypeScript |
| [chat2api](https://github.com/qy527145/chat2api) | Simple framework for reversing web chat services into APIs | 57 | 🟡 | Python |
| [Gemini-1.5-Pro AI Studio Reverse Engineered API](https://github.com/SreejanPersonal/Gemini-1.5-Pro-Google-AI-Studio-Reverse-Engineered-API) | Reverse engineered Google AI Studio endpoint for Gemini 1.5 Pro | 57 | 🟡 | Jupyter Notebook |
| [cto](https://github.com/Luotianyi-0712/cto) | Proxies cto.new chat into OpenAI ChatCompletion format | 56 | 🟡 | TypeScript |
| [geminiweb2api](https://github.com/XxxXTeam/geminiweb2api) | OpenAI-compatible proxy for the Gemini web app | 55 | 🟢 | HTML |
| [LlM-Api-Open](https://github.com/F33RNI/LlM-Api-Open) | Unofficial open APIs for ChatGPT and Microsoft Copilot with self-hosting | 43 | 🟡 | Python |
| [claude-ai-re-client](https://github.com/Adithyan-Defender/claude-ai-re-client) | CLI client built on Claude.ai's reverse-engineered HTTPS completion API | 40 | 🟢 | Python |
| [Gemini-Chat-API](https://github.com/OEvortex/Gemini-Chat-API) | Unofficial API for interacting with Google Gemini web chat | 40 | 🟢 | Python |
| [pi-oracle](https://github.com/fitchmultz/pi-oracle) | ChatGPT and Grok web-session oracle extension for the Pi agent | 40 | 🟢 | TypeScript |
| [poe-node-api](https://github.com/AHGGG/poe-node-api) | Reverse-engineered Node.js client for Quora's Poe chatbot service | 38 | 🗄️ | TypeScript |
| [CLOVA-X](https://github.com/mirusu400/CLOVA-X) | Unofficial API for Naver CLOVA X | 37 | 🟡 | Python |
| [pi-perplexity](https://github.com/ivanrvpereira/pi-perplexity) | Pi extension searching via your Perplexity Pro/Max web subscription | 32 | 🟢 | TypeScript |
| [a4f-local](https://github.com/devsdocode/a4f-local) | Wrapper for several reverse-engineered AI provider web APIs with an OpenAI-compatible interface | 31 | 🟡 | Python |
| [grok2api](https://github.com/sodikinnaa/grok2api) | FastAPI Grok2API compatible with OpenAI calls | 31 | 🟢 | Python |
| [MetaAI-Free-Hermes-Agent](https://github.com/compnew2006/MetaAI-Free-Hermes-Agent) | Runs Meta AI's web model in Hermes Agent without API keys | 31 | 🟢 | TypeScript |
| [gemini-claude-web2api](https://github.com/cyberanrhy/gemini-claude-web2api) | OpenAI-compatible proxy for Gemini and Claude web APIs via cookie auth | 29 | 🟢 | Python |
| [Perplexity-Reverse-Engineered-API](https://github.com/SreejanPersonal/Perplexity-Reverse-Engineered-API) | Reverse-engineered Perplexity API client in Python over WebSocket | 29 | 🟡 | Jupyter Notebook |
| [grok2api-pro](https://github.com/miuzhaii/grok2api-pro) | Grok web to OpenAI-style API with image/video generation and account pool | 27 | 🟢 | Python |
| [notion-ai](https://github.com/albertcht/notion-ai) | Unofficial PHP client for the Notion AI API | 27 | 🔴 | PHP |
| [chatgptproxy](https://github.com/acruz6421-bot/chatgptproxy) | ChatGPT web to OpenAI API proxy with Sentinel PoW solver | 25 | 🟢 | Python |
| [copilot-api](https://github.com/OEvortex/copilot-api) | Unofficial Python API wrapper for the Microsoft Copilot web chat | 24 | 🟡 | Python |
| [Gemini-Reverse](https://github.com/rynn-k/Gemini-Reverse) | Unofficial Node.js client for gemini.google.com | 24 | 🟢 | JavaScript |
| [prism2api](https://github.com/Robinfxa/prism2api) | Reverse-engineered Python API for prism.openai.com | 24 | 🟢 | Python |
| [EdgeGPT](https://github.com/IhsanDevs/EdgeGPT) | Bing AI chatbot WebSocket API wrapper for PHP | 22 | 🗄️ | PHP |
| [grokforge](https://github.com/crmmc/grokforge) | Go rewrite of grok2api (Grok web to API) | 22 | 🟢 | Go |
| [chatgpt-export (hoya98)](https://github.com/hoya98/chatgpt-export) | Bulk-export all ChatGPT conversations incl. Team/Business workspaces via backend API | 21 | 🟢 | Swift |
| [EdgeGPTJs](https://github.com/lonelam/EdgeGPTJs) | Node.js port of the reverse-engineered EdgeGPT Bing Chat API | 21 | 🔴 | TypeScript |
| [muse-client](https://github.com/wong2/muse-client) | Unofficial TypeScript SDK for Muse chat using the Muse Gadget SDK protocol | 21 | 🟢 | TypeScript |
| [node_perplexityai](https://github.com/Parking-Master/node_perplexityai) | Unofficial Node.js API based on the Perplexity.AI website and mobile app | 21 | 🟡 | JavaScript |
| [chatgpt-exporter (ezwep)](https://github.com/ezwep/chatgpt-exporter) | Self-hosted backup of ChatGPT conversations, projects and custom GPTs | 18 | 🟢 | JavaScript |
| [chatgpt-turnstile-reversed](https://github.com/jonathanyly/chatgpt-turnstile-reversed) | Reverse engineered ChatGPT Turnstile anti-bot token used for login and chat | 18 | 🟢 | JavaScript |
| [gemini-free-api](https://github.com/XD06/gemini-free-api) | Reverse-engineered Gemini web interface as a streaming API with tools | 17 | 🟢 | Go |
| [Lovelace](https://github.com/rodyherrera/Lovelace) | Self-hosted API and web UI for ChatGPT via its web interface | 17 | 🟡 | JavaScript |
| [Go-EdgeGPT](https://github.com/billikeu/Go-EdgeGPT) | Go reverse-engineered API of Microsoft's Bing Chat | 16 | 🔴 | Go |
| [Discord-C.AI-Wrapper](https://github.com/walterwhite-69/Discord-C.AI-Wrapper) | Brings Character.AI personas into Discord via the unofficial API | 15 | 🟢 | Python |
| [huggingchat-api](https://github.com/ogios/huggingchat-api) | HuggingChat web API client with streaming and web search | 15 | 🗄️ | Python |
| [SydneyGPT](https://github.com/rafaelcalleja/SydneyGPT) | Sydney persona decorator for the reverse-engineered EdgeGPT API | 15 | 🔴 | Python |
| [chatgptAPI_unof](https://github.com/0xMesto/chatgptAPI_unof) | Unofficial ChatGPT web API client | 14 | 🟡 | JavaScript |
| [UnofficialClaude](https://github.com/0xMesto/UnofficialClaude) | Unofficial Claude web API with OpenAI-like structure | 14 | 🟡 | Python |
| [Claude-API (cyber-wojtek)](https://github.com/cyber-wojtek/Claude-API) | Reverse-engineered Python wrapper for the Claude web app | 13 | 🟢 | Python |
| [chatgpt-exporter (thiscantbeserious)](https://github.com/thiscantbeserious/chatgpt-exporter) | Exports ChatGPT Business account data via the web backend | 12 | 🟢 | JavaScript |
| [reverse-chatgpt](https://github.com/s5treak/reverse-chatgpt) | Reverse-engineered ChatGPT web interface with streaming automation API | 12 | 🟢 | Python |
| [blackbox-ai](https://github.com/OzRAGEHarm/blackbox-ai) | Reverse-engineered Node.js wrapper for the blackbox.ai chat API | 11 | 🟡 | JavaScript |
| [cleverbotfreeapi](https://github.com/Deftera186/cleverbotfreeapi) | Python package for the API that the Cleverbot website uses | 10 | 🔴 | Python |
| [genspark-py](https://github.com/SharpWizard/genspark-py) | Unofficial Python client for Genspark.ai login and streaming chat | 9 | 🟢 | Python |
| [grok-web-to-api](https://github.com/Agelakz/grok-web-to-api) | OpenAI-compatible proxy for grok.com web sessions | 9 | 🟢 | Go |
| [Inflection-Pi-API](https://github.com/hansfzlorenzana/Inflection-Pi-API) | Reverse-engineered API for Inflection AI's Pi chatbot | 8 | 🔴 | Python |
| [gemini-web-api (FarisHijazi)](https://github.com/FarisHijazi/gemini-web-api) | OpenAI-compatible API over gemini.google.com including images and Veo video | 7 | 🟢 | Python |
| [node-vercel-llm-api](https://github.com/0x6a69616e/node-vercel-llm-api) | Reverse-engineered Node.js wrapper for the Vercel AI Playground | 7 | 🔴 | JavaScript |
| [chatgpt2api-cf](https://github.com/6Kmfi6HP/chatgpt2api-cf) | Cloudflare Workers gateway reverse-engineered from the anonymous ChatGPT Android API | 6 | 🟢 | TypeScript |
| [gemini-web-api (qutek)](https://github.com/qutek/gemini-web-api) | OpenAI-compatible proxy and Node.js SDK for the Gemini web app | 6 | 🟢 | TypeScript |
| [genspark-gateway](https://github.com/chnd372/genspark-gateway) | OpenAI-compatible proxy for the Genspark.ai web session | 6 | 🟢 | Python |
| [node_characterai-2.0](https://github.com/Skidy89/node_characterai-2.0) | Unofficial Character.AI wrapper for Node | 6 | 🟢 | TypeScript |
| [ppxity](https://github.com/0xInception/ppxity) | CLI for the unofficial Perplexity Labs API | 6 | 🟡 | Go |

## Chinese LLM Web APIs

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Chat2API](https://github.com/xiaoY233/Chat2API) | Zero-cost access to GLM, Kimi, Qwen and other models via their official web UIs | 1,715 | 🟢 | TypeScript |
| [qwen2API](https://github.com/YuJunZhiXue/qwen2API) | Converts the Qwen web chat into an API | 976 | 🟢 | Go |
| [Qwen2API](https://github.com/Rfym21/Qwen2API) | QwenLM web chat to OpenAI-compatible API | 844 | 🟢 | JavaScript |
| [deepseek2api](https://github.com/iidamie/deepseek2api) | DeepSeek web reverse API | 636 | 🗄️ | Python |
| [deepseek-free-api](https://github.com/Fly143/deepseek-free-api) | Converts chat.deepseek.com web chat into OpenAI and Anthropic compatible APIs | 317 | 🟢 | Python |
| [DeeperSeek](https://github.com/theAbdoSabbagh/DeeperSeek) | Unofficial Python wrapper for the DeepSeek web chat | 311 | 🟡 | Python |
| [doubao-2api](https://github.com/lza6/doubao-2api) | Doubao web to API with Playwright a_bogus signature reversing | 292 | 🟡 | Python |
| [kimi2api](https://github.com/chopper1026/kimi2api) | Kimi web chat reverse proxy with OpenAI-compatible interface | 248 | 🟢 | Python |
| [deepseek-web2api-free](https://github.com/snake-aabb-wtf/deepseek-web2api-free) | FastAPI reverse proxy turning DeepSeek web chat into OpenAI-compatible API | 187 | 🟢 | Python |
| [2025doubao-free-api](https://github.com/1994qrq/2025doubao-free-api) | Doubao web reverse API | 172 | 🟢 | TypeScript |
| [qwen2api](https://github.com/smanx/qwen2api) | Proxy converting Qwen Chat to an OpenAI-compatible API | 168 | 🟢 | JavaScript |
| [Z.ai2api](https://github.com/hmjz100/Z.ai2api) | Proxies Z.ai (GLM) chat into OpenAI/Anthropic-compatible format without tokens | 152 | 🗄️ | Python |
| [GLM-Free-API](https://github.com/izaart95-jpg/GLM-Free-API) | OpenAI-compatible API proxy for chat.z.ai (GLM) web | 143 | 🗄️ | JavaScript |
| [glm2api](https://github.com/XxxXTeam/glm2api) | Converts chatglm.com web into a standard OpenAI API | 129 | 🟢 | Python |
| [deepseek2api](https://github.com/TQZHR/deepseek2api) | DeepSeek web to API proxy | 122 | 🟢 | JavaScript |
| [zai2api](https://github.com/XxxXTeam/zai2api) | Proxy converting Z.AI chat into an OpenAI-compatible API | 114 | 🟢 | Go |
| [doubao2API (robinxplorer)](https://github.com/robinxplorer/doubao2API) | Converts the Doubao web chat into an OpenAI-compatible API | 110 | 🟢 | Python |
| [yuanbao-chat2api](https://github.com/juzeon/yuanbao-chat2api) | Tencent Yuanbao web chat reverse-engineered to an OpenAI-style API | 100 | 🟡 | Rust |
| [qwen-api](https://github.com/encryptarun/qwen-api) | Qwen web API proxy with OpenAI-compatible chat, image and video endpoints | 93 | 🟢 |  |
| [Qwen2API_Go](https://github.com/XxxXTeam/Qwen2API_Go) | Go service converting Qwen.AI web into an API | 91 | 🟢 | Go |
| [DoubaoFreeApi](https://github.com/XilyFeAAAA/DoubaoFreeApi) | Lightweight Doubao web API proxy | 90 | 🗄️ | Python |
| [deepseek-api](https://github.com/rabilrbl/deepseek-api) | Unofficial API wrapper for chat.deepseek.com | 81 | 🗄️ | Python |
| [revTongYi](https://github.com/leeeduke/revTongYi) | Reverse engineered Python API for Alibaba Tongyi Qianwen and Wanxiang | 73 | 🟢 | Python |
| [kimi2api](https://github.com/XxxXTeam/kimi2api) | Kimi web to API proxy | 63 | 🟢 | Python |
| [Kimi-Free-API](https://github.com/xiaoY233/Kimi-Free-API) | Kimi web reverse API (successor to LLM-Red-Team kimi-free-api) | 61 | 🟢 | TypeScript |
| [Qwen-Free-API](https://github.com/xiaoY233/Qwen-Free-API) | Qwen web reverse API (successor to LLM-Red-Team qwen-free-api) | 55 | 🟢 | TypeScript |
| [qwen2api-rs](https://github.com/123hi123/qwen2api-rs) | Rust qwen2API gateway disguising Qwen Web as OpenAI/Anthropic/Gemini APIs | 54 | 🟢 | Rust |
| [qwen-free-api](https://github.com/Godde3s/qwen-free-api) | Go bridge exposing chat.qwen.ai as OpenAI and Anthropic APIs | 41 | 🟢 | Go |
| [qwen2api (map-A)](https://github.com/map-A/qwen2api) | chat.qwen.ai web to OpenAI API | 39 | 🟢 | Rust |
| [deepseek-web-api](https://github.com/kittors/deepseek-web-api) | Unofficial local OpenAI-compatible API for DeepSeek web sessions | 35 | 🟢 | TypeScript |
| [doubao-free-api](https://github.com/5201213/doubao-free-api) | Wraps the Doubao desktop client as an OpenAI-compatible API | 35 | 🟢 | Python |
| [doubao2API (HongYan789)](https://github.com/HongYan789/doubao2API) | Reverse-engineered Doubao web API gateway | 35 | 🟢 | Python |
| [DeepSeek-API-Unofficial-v2](https://github.com/SreejanPersonal/DeepSeek-API-Unofficial-v2) | Unofficial reverse-engineered API for DeepSeek Chat and Coder | 32 | 🟡 | Python |
| [doubao2api (SeiShonagon520)](https://github.com/SeiShonagon520/doubao2api) | OpenAI-compatible service rebuilt on the latest Doubao web client | 32 | 🟢 | Python |
| [KimiFreeAPI](https://github.com/izaart95-jpg/KimiFreeAPI) | OpenAI-compatible free API for Kimi web | 29 | 🗄️ | Go |
| [qwen-free-api-worker](https://github.com/aigem/qwen-free-api-worker) | Cloudflare Worker exposing chat.qwenlm.ai as an OpenAI-compatible API | 28 | 🟡 | JavaScript |
| [zai-openai-proxy](https://github.com/xaoLiu1222/zai-openai-proxy) | chat.z.ai reverse-engineered OpenAI-compatible proxy with thinking and tools | 27 | 🟢 | JavaScript |
| [qwen-api](https://github.com/arosyihuddin/qwen-api) | Unofficial Python client for the Qwen chat web API | 25 | 🟡 | Python |
| [deepseek-free-api](https://github.com/Ametist298/deepseek-free-api) | OpenAI-compatible free API via DeepSeek web | 22 | 🟢 | JavaScript |
| [minimax2api (juangchuank-ops)](https://github.com/juangchuank-ops/minimax2api) | MiniMax Agent reverse gateway with OpenAI-compatible API | 21 | 🟢 | Go |
| [qwen_free_api](https://github.com/Staks-sor/qwen_free_api) | Python client for Qwen web through an OpenAI-compatible API | 19 | 🟢 | Python |
| [deepseek-api (smkttl)](https://github.com/smkttl/deepseek-api) | Unofficial DeepSeek API by reverse-engineering its web interface | 18 | 🟢 | Shell |
| [Doubao2api (Hu410)](https://github.com/Hu410/Doubao2api) | Lightweight proxy reversing Doubao Web API into Chat Completions | 12 | 🟢 | Python |
| [FreeTokenAPI](https://github.com/mmmlllnnn/FreeTokenAPI) | DeepSeek2API/Qwen2API with OpenAI and Anthropic-compatible endpoints | 12 | 🟢 | Python |
| [minimaxM3-web2api](https://github.com/snake-aabb-wtf/minimaxM3-web2api) | MiniMax Agent web chat to OpenAI API, reimplementing the JS signature algorithm | 12 | 🟢 | Python |
| [qwen2api (annewj023)](https://github.com/annewj023/qwen2api) | Converts chat.qwen.ai web into an external API | 12 | 🟢 | JavaScript |
| [chat-deepseek-api](https://github.com/thinhdanggroup/chat-deepseek-api) | Unofficial Python API wrapper for the chat.deepseek.com web chat | 11 | 🗄️ | Python |
| [deepseek-2api](https://github.com/zxy1994/deepseek-2api) | DeepSeek web API to OpenAI REST gateway on Cloudflare Workers | 5 | 🟢 | TypeScript |
| [Qwen-Reverse](https://github.com/AnonymoDGH/Qwen-Reverse) | Reverse-engineered Python client for chat.qwen.ai: text, vision, image and video generation | 4 | 🟢 | Python |

## Coding Agents (Claude Code, Cursor, Copilot…)

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [claw-code](https://github.com/ultraworkers/claw-code) | Clean-room Rust/Python rewrite of the Claude Code agent harness after the source leak | 195,063 | 🟢 | Rust |
| [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | Wraps Codex, Claude Code, Antigravity, Grok and Gemini CLI OAuth backends as OpenAI/Claude-compatible APIs | 56,180 | 🟢 | Go |
| [sub2api](https://github.com/Wei-Shaw/sub2api) | Relay that exposes Claude, OpenAI, Gemini and Grok subscriptions as unified APIs | 44,801 | 🟢 | Go |
| [claude-code-router](https://github.com/musistudio/claude-code-router) | Proxy that routes Claude Code's Anthropic API traffic to other model providers | 37,840 | 🟢 | TypeScript |
| [Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | Antigravity account manager with local OpenAI/Anthropic/Gemini proxy | 32,542 | 🟢 | Rust |
| [claude-code-best](https://github.com/claude-code-best/claude-code) | Reverse-engineered rebuild of the Anthropic Claude Code CLI as an open terminal coding assistant | 23,035 | 🟢 | TypeScript |
| [opencode-antigravity-auth](https://github.com/NoeFabris/opencode-antigravity-auth) | OpenCode plugin authenticating against Antigravity to use its Gemini/Claude quota | 10,943 | 🟢 | TypeScript |
| [claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | Claude Code 2.1.88 TypeScript source restored from sourcesContent in the leaked cli.js.map | 9,722 | 🟢 | TypeScript |
| [AIClient2API](https://github.com/justlovemaki/AIClient2API) | Multi-protocol proxy for Antigravity, Codex, Grok, Kiro and Claude client backends | 8,927 | 🟢 | JavaScript |
| [gcli2api](https://github.com/su-kaka/agy2api) | Converts Gemini CLI and Antigravity credentials into OpenAI, Gemini and Claude APIs | 5,271 | 🟢 | Python |
| [antigravity-proxy (yuaotian)](https://github.com/yuaotian/antigravity-proxy) | DLL-injection proxy forcer for Google Antigravity IDE without TUN mode | 4,593 | 🟢 | C++ |
| [copilot-api](https://github.com/ericc-ch/copilot-api) | Reverse-engineered GitHub Copilot API exposed as OpenAI- and Anthropic-compatible proxy (works with Claude Code) | 4,147 | 🟢 | TypeScript |
| [antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | Anthropic-compatible proxy for Claude/Gemini models through Antigravity's Cloud Code | 4,021 | 🟢 | JavaScript |
| [codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | Unofficial Linux build of OpenAI's Codex/ChatGPT desktop app from the macOS bundle | 3,910 | 🟢 | JavaScript |
| [how-claude-code-works](https://github.com/Windy3f3f3f3f/how-claude-code-works) | Deep dive into Claude Code internals: agent loop, context engineering, tools | 3,778 | 🟢 |  |
| [claude-code-proxy](https://github.com/1rgs/claude-code-proxy) | Run Claude Code on OpenAI models by translating its API traffic | 3,760 | 🟢 | Python |
| [vibeproxy](https://github.com/automazeio/vibeproxy) | macOS menu bar proxy reusing Claude Code and ChatGPT subscription OAuth for other AI tools | 3,396 | 🟢 | Swift |
| [claude-tap](https://github.com/liaohch3/claude-tap) | Intercepts and inspects API traffic of Claude Code, Codex CLI, Gemini CLI, Cursor CLI and other agents | 3,308 | 🟢 | Python |
| [WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | Reverse-engineered Windsurf/Devin Desktop model access exposed as OpenAI/Anthropic/Gemini-compatible API | 3,107 | 🟢 | JavaScript |
| [claude-code-from-source](https://github.com/alejandrobalderas/claude-code-from-source) | Architecture, patterns and internals of Claude Code reverse engineered from source maps | 2,991 | 🟢 | TypeScript |
| [claude-code-proxy](https://github.com/fuergaosi233/claude-code-proxy) | Claude Code to OpenAI API translation proxy | 2,798 | 🟢 | Python |
| [tweakcc](https://github.com/Piebald-AI/tweakcc) | Patches Claude Code's minified cli.js to customize system prompts, toolsets, themes and UI | 2,561 | 🟢 | TypeScript |
| [claude-code-reverse](https://github.com/Yuyz0112/claude-code-reverse) | Uses LLMs to analyze minified Claude Code and visualize its LLM interactions and prompts | 2,441 | 🟡 | JavaScript |
| [AntigravityManager](https://github.com/Draculabo/AntigravityManager) | Electron app managing accounts and processes for Google Antigravity | 2,405 | 🟢 | TypeScript |
| [claude_code_src](https://github.com/ponponon/claude_code_src) | Claude Code source restored from the sourcesContent of the leaked 2.1.88 source map | 2,335 | 🟢 | TypeScript |
| [copilot.el](https://github.com/copilot-emacs/copilot.el) | Unofficial GitHub Copilot plugin for Emacs | 2,330 | 🟢 | Emacs Lisp |
| [kiro-gateway](https://github.com/jwadow/kiro-gateway) | Proxy gateway for Kiro IDE & CLI (Amazon Q Developer) exposing OpenAI/Anthropic-compatible APIs | 2,329 | 🟢 | Python |
| [codex2api (james-6-23)](https://github.com/james-6-23/codex2api) | Go Codex reverse proxy with admin dashboard | 2,312 | 🟢 | Go |
| [opencode-openai-codex-auth](https://github.com/numman-ali/opencode-openai-codex-auth) | OpenCode plugin using ChatGPT Plus/Pro OAuth via Codex backend | 2,211 | 🟢 | TypeScript |
| [meridian](https://github.com/rynfar/meridian) | Local API bridge that lets Pi, OpenCode and other clients use Claude and Antigravity subscriptions | 2,156 | 🟢 | TypeScript |
| [kiro.rs](https://github.com/hank9999/kiro.rs) | Rust service translating the Kiro backend API to Anthropic format with token refresh | 1,967 | 🟢 | Rust |
| [cursor2api (7836246)](https://github.com/7836246/cursor2api) | Proxy converting Cursor's web docs API into OpenAI/Anthropic-compatible format | 1,887 | 🗄️ | TypeScript |
| [ChatMock](https://github.com/RayBytes/ChatMock) | OpenAI-compatible API served from a ChatGPT subscription via Codex auth | 1,557 | 🟢 | Python |
| [cursor-reset](https://github.com/ultrasev/cursor-reset) | Resets Cursor's device identification to work around trial restrictions | 1,515 | 🟡 | Python |
| [openai-oauth](https://github.com/EvanZhouDev/openai-oauth) | Local proxy that reuses Codex CLI ChatGPT OAuth tokens as an OpenAI-compatible API | 1,409 | 🟢 | TypeScript |
| [Kiro-Go](https://github.com/Quorinex/Kiro-Go) | Converts Kiro accounts into OpenAI/Anthropic APIs with pooling and streaming | 1,193 | 🟢 | Go |
| [pi-generative-ui](https://github.com/Michaelliv/pi-generative-ui) | Claude.ai's generative UI widgets reverse engineered and rebuilt for the pi agent | 1,167 | 🟢 | TypeScript |
| [copilot-api](https://github.com/caozhiyuan/copilot-api) | GitHub Copilot and Codex gateway exposing OpenAI/Anthropic-compatible APIs | 1,092 | 🟢 | TypeScript |
| [cursor2api-go](https://github.com/Xchat1/cursor2api-go) | Go proxy that converts Cursor's internal chat API into an OpenAI-compatible endpoint | 1,051 | 🟢 | JavaScript |
| [claude-code-source-code-deobfuscation](https://github.com/ghuntley/claude-code-source-code-deobfuscation) | Cleanroom deobfuscation of the Claude Code npm package cli.js into readable source | 990 | 🗄️ | TypeScript |
| [gemini-cli-openai](https://github.com/GewoonJaap/gemini-cli-openai) | Cloudflare Worker exposing Gemini CLI endpoints as an OpenAI API | 895 | 🟢 | TypeScript |
| [antigravity2api-nodejs](https://github.com/liuw1535/antigravity2api-nodejs) | Node.js proxy translating Google Antigravity's API into OpenAI format | 817 | 🟢 | JavaScript |
| [claude-code-source](https://github.com/hangsman/claude-code-source) | Claude Code v2.1.88 TypeScript source recovered from the leaked npm source map | 799 | 🟢 | TypeScript |
| [HitCC](https://github.com/hitmux/HitCC) | Reverse-engineering documentation of the full logic of the Claude Code CLI Node.js version | 748 | 🟢 | Python |
| [OpenCodex](https://github.com/RyensX/OpenCodex) | Middleware to remotely access and operate Codex/ChatGPT Desktop from other devices | 723 | 🟢 | JavaScript |
| [copilot-explorer](https://github.com/thakkarparth007/copilot-explorer) | Reverse engineers the Copilot VS Code extension JS bundle: module graph, prompt building, inline completion | 705 | 🔴 | JavaScript |
| [claude-desktop-extra](https://github.com/patrickjaja/claude-desktop-extra) | Patched Claude Desktop builds for Arch/Fedora/NixOS/AppImage with Computer Use and extras | 696 | 🟢 | JavaScript |
| [cursor-api (wisdgod)](https://github.com/wisdgod/cursor-api) | Reverse-engineered Cursor API turned into an OpenAI-compatible service | 691 | 🗄️ | Rust |
| [zerogravity](https://github.com/NikkeTryHard/zerogravity) | Proxy disguising requests as Antigravity traffic for OpenAI/Anthropic/Gemini APIs | 648 | 🟢 | Dockerfile |
| [CometixCode](https://github.com/Haleclipse/CometixCode) | Unofficial Rust reimplementation of the Claude Code terminal UI | 645 | 🟢 | Rust |
| [cursor-deepseek](https://github.com/danilofalcao/cursor-deepseek) | HTTP/2 proxy that lets Cursor Composer talk to DeepSeek and other OpenAI-style backends | 645 | 🟢 | Go |
| [kiro2api](https://github.com/caidaoli/kiro2api) | Go gateway converting Kiro (CodeWhisperer) auth into Anthropic/OpenAI APIs | 638 | 🟢 | Go |
| [geminicli2api](https://github.com/gzzhongqi/geminicli2api) | FastAPI proxy turning Gemini CLI OAuth into OpenAI and Gemini API endpoints | 591 | 🟢 | Python |
| [open-claude-code](https://github.com/ruvnet/open-claude-code) | Nightly Claude Code CLI decompile, reverse engineered and rebuilt as an open clean-room implementation | 545 | 🟢 | JavaScript |
| [openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | Proxy that makes third-party requests look like Claude Code to use subscription billing | 519 | 🟢 | JavaScript |
| [anti-api](https://github.com/silasxbt/anti-api) | Turns Antigravity, Codex and Copilot into Anthropic/OpenAI-compatible servers | 517 | 🟢 | TypeScript |
| [claude-code-proxy](https://github.com/seifghazi/claude-code-proxy) | Proxy that captures and visualizes in-flight Claude Code requests | 513 | 🟢 | TypeScript |
| [Antigravity-Tools-LS](https://github.com/lbjlaq/Antigravity-Tools-LS) | Local proxy bridge for the Antigravity IDE language server | 436 | 🟢 | Rust |
| [claude-cowork-linux](https://github.com/johnzfitch/claude-cowork-linux) | Runs Claude Desktop's Cowork mode natively on Linux | 424 | 🟢 | JavaScript |
| [KiroGate](https://github.com/aliom-v/KiroGate) | OpenAI and Anthropic compatible Kiro IDE API proxy gateway | 420 | 🗄️ | Python |
| [anthropic-proxy](https://github.com/maxnowack/anthropic-proxy) | Converts Claude Code's Anthropic requests to OpenAI format for OpenRouter | 414 | 🗄️ | JavaScript |
| [KiroProxy](https://github.com/xu-yuanhao/KiroProxy) | Compatibility and routing layer exposing Kiro IDE models as standard APIs | 389 | 🟢 | Python |
| [qoder2api-hub](https://github.com/shuishuipingan/qoder2api-hub) | Qoder gateway reimplementing COSY request signing and device fingerprint | 370 | 🟢 | Python |
| [kiro2cc](https://github.com/bestK/kiro2cc) | Kiro token manager and proxy that lets Claude Code use the Kiro backend | 367 | 🟡 | Go |
| [fast-context-mcp](https://github.com/SammySnake-d/fast-context-mcp) | Semantic code search MCP tool powered by Windsurf's reverse-engineered SWE-grep protocol | 362 | 🟢 | JavaScript |
| [ccproxy](https://github.com/starbaser/ccproxy) | Intercepting proxy to hook and rewrite Claude Code requests and responses | 355 | 🟢 | Python |
| [composer-api](https://github.com/standardagents/composer-api) | OpenAI-compatible API proxy for Cursor's Composer model | 347 | 🟢 | Swift |
| [claude-code (T-Lab-CUHKSZ)](https://github.com/T-Lab-CUHKSZ/claude-code) | Buildable research fork of leaked Claude Code source with a reverse-engineered Bun build system | 328 | 🟢 | TypeScript |
| [copilot-api](https://github.com/B00TK1D/copilot-api) | Reverse-engineered GitHub Copilot API client and server | 323 | 🟡 | Python |
| [api2cursor](https://github.com/h88782481/api2cursor) | Adapter that lets Cursor Pro use third-party relay APIs by rewriting its requests | 298 | 🟢 | Python |
| [claude-code-reverse](https://github.com/ghboke/claude-code-reverse) | Source analysis report of Claude Code from its bundled CLI | 289 | 🟢 | TypeScript |
| [cursor-api-proxy](https://github.com/anyrobert/cursor-api-proxy) | OpenAI-style API proxy that drives Cursor's `agent` CLI | 283 | 🟢 | TypeScript |
| [ccproxy-api](https://github.com/CaddyGlow/ccproxy-api) | Local reverse proxy reusing Claude Code and Codex subscriptions as APIs | 277 | 🟢 | Python |
| [claude-worker-proxy](https://github.com/glidea/claude-worker-proxy) | Cloudflare Worker proxy translating Claude Code's Anthropic requests to other providers | 276 | 🟢 | TypeScript |
| [cli2api](https://github.com/caigee-cmd/cli2api) | OpenAI-compatible API from Qoder CLI and WorkBuddy logins | 276 | 🟢 | Go |
| [cursor-api](https://github.com/zhx47/cursor-api) | Reverse-engineered Cursor API converted to an OpenAI-compatible service | 268 | 🟡 | JavaScript |
| [cursortab.nvim](https://github.com/reachingforthejack/cursortab.nvim) | Reverse engineered Cursor Tab completion API brought to Neovim | 267 | 🗄️ | Go |
| [ProxyPilot](https://github.com/Finesssee/ProxyPilot) | Local API proxy that routes AI coding tools through existing subscriptions, with CLI control | 262 | 🟢 | Go |
| [kiro2cc-proxy](https://github.com/TsinHzl/kiro2cc-proxy) | Kiro reverse proxy for Claude Code and Codex with SSE streaming | 254 | 🟢 | Rust |
| [background-computer-use](https://github.com/actuallyepic/background-computer-use) | Reverse-engineered OpenAI Codex background computer-use feature | 251 | 🟢 | Swift |
| [cocopilot2gpt](https://github.com/ljnchn/cocopilot2gpt) | Converts a GitHub Copilot subscription into a ChatGPT-style API | 247 | 🟡 |  |
| [openusage](https://github.com/janekbaraniewski/openusage) | Usage tracker for AI coding tools, with a probe that reverse engineers Cursor IDE data sources | 233 | 🟢 | Go |
| [qoder-proxy](https://github.com/avaritiachaos/qoder-proxy) | Local OpenAI-compatible proxy for Qoder CN CLI | 223 | 🟢 | JavaScript |
| [ungate](https://github.com/orchidfiles/ungate) | Use Claude and ChatGPT subscriptions inside Cursor instead of paid API tokens | 221 | 🟢 | TypeScript |
| [claude-code-source-analysis (catyans)](https://github.com/catyans/claude-code-source-analysis) | Module-by-module analysis of the leaked Claude Code TypeScript source | 219 | 🟢 |  |
| [Antigravity2Api](https://github.com/znlsl/Antigravity2Api) | Proxies Antigravity into Claude and Gemini APIs with thought-signature handling | 208 | 🟢 | JavaScript |
| [open-claude-code (xtherk)](https://github.com/xtherk/open-claude-code) | Claude Code 2.1.88 source recovered from sourcemaps and build-fixed as a research reference | 206 | 🟢 | TypeScript |
| [pi-black](https://github.com/paoloanzn/pi-black) | Use a Claude Max/Pro subscription inside the Pi coding agent | 197 | 🟢 | TypeScript |
| [augment2api](https://github.com/linqiu919/augment2api) | Middle layer that exposes Augment Code's API as OpenAI-compatible | 191 | 🟡 | Go |
| [claude-code-analysis](https://github.com/ComeOnOliver/claude-code-analysis) | Reverse engineering analysis of Claude Code's internal architecture | 190 | 🟢 | TypeScript |
| [cursor-unchained](https://github.com/dcrebbin/cursor-unchained) | Reverse-engineered Cursor's AI tab completion to use in other editors | 181 | 🟢 | TypeScript |
| [claude-code-research](https://github.com/cablate/claude-code-research) | Independent research on Claude Code and Claude Agent SDK internals | 179 | 🟢 | HTML |
| [CAS](https://github.com/codingagentsystem/cas) | Orchestrator built by reverse engineering Claude Code internals | 176 | 🟢 | Rust |
| [trae-api](https://github.com/A-23187/trae-api) | Exposes Trae IDE's builtin models through an OpenAI-compatible API | 174 | 🟢 | Python |
| [claude-code-sourcemap-learning-notebook](https://github.com/dadiaomengmeimei/claude-code-sourcemap-learning-notebook) | Reverse-engineering notes on Claude Code's 512K lines of TypeScript: architecture and design decisions | 167 | 🟢 |  |
| [claude-cowork-service](https://github.com/patrickjaja/claude-cowork-service) | Linux daemon reimplementing Claude Desktop Cowork's reverse-engineered vsock RPC protocol | 167 | 🟢 | Go |
| [QoderGateway](https://github.com/bzym2/QoderGateway) | Turns Alibaba Qoder accounts into one OpenAI-compatible API | 163 | 🟢 | Python |
| [m365-copilot-proxy](https://github.com/cramt/m365-copilot-proxy) | OpenAI-compatible proxy using a Microsoft 365 Copilot licence as a model backend | 156 | 🟢 | TypeScript |
| [gemini-cli-proxy](https://github.com/nettee/gemini-cli-proxy) | Wraps Gemini CLI as an OpenAI-compatible API to use its free Gemini Pro quota | 152 | 🟢 | Python |
| [KiroaaS](https://github.com/hnewcity/KiroaaS) | Desktop app exposing Kiro's models through local OpenAI/Anthropic-compatible API | 149 | 🟢 | Python |
| [github-copilot](https://github.com/saschaschramm/github-copilot) | Analysis of the GitHub Copilot extension internals | 148 | 🔴 | Python |
| [cursorweb2api](https://github.com/jhhgiyv/cursorweb2api) | Converts Cursor's web chat into an OpenAI-compatible API | 143 | 🟢 | JavaScript |
| [copilot2api-go](https://github.com/StarryKira/copilot2api-go) | Turns GitHub Copilot into OpenAI/Anthropic-compatible server for Claude Code, Codex, OpenCode | 142 | 🟢 | Go |
| [opencode-antigravity-quota](https://github.com/frieser/opencode-antigravity-quota) | OpenCode plugin reading Antigravity/Gemini CLI quota endpoints across accounts | 142 | 🟢 | TypeScript |
| [pi-gpt-search](https://github.com/mateusdcc/pi-gpt-search) | Reverse-engineered Codex's web search to use with Claude and local models | 140 | 🟢 | TypeScript |
| [BYOKEY](https://github.com/AprilNEA/BYOKEY) | Unofficial Rust client and proxy for the Ampcode (ampcode.com) coding agent API | 138 | 🟢 | Rust |
| [claude-source-leaked](https://github.com/noya21th/claude-source-leaked) | Claude Code v2.1.88 source analysis: system prompts, hidden feature flags and architecture | 133 | 🟢 | TypeScript |
| [github-copilot-api-vscode](https://github.com/suhaibbinyounis/github-copilot-api-vscode) | Exposes GitHub Copilot as a local OpenAI-compatible API gateway from VS Code | 128 | 🟢 | TypeScript |
| [claude-code-working](https://github.com/777genius/claude-code-working) | Working Claude Code CLI rebuilt from reverse-engineered source analysis | 124 | 🟢 | TypeScript |
| [subrouter](https://github.com/manaflow-ai/subrouter) | Routes Codex/Claude Code traffic across multiple ChatGPT Pro and Claude Max subscriptions | 121 | 🟢 | Go |
| [cursor-api](https://github.com/waitkafuka/cursor-api) | Relay that converts Cursor's chat API into OpenAI format | 118 | 🟡 | JavaScript |
| [Kiro2api-Node](https://github.com/lulistart/Kiro2api-Node) | Node.js Kiro-to-API proxy | 118 | 🟢 | JavaScript |
| [zcode-cli](https://github.com/kingsword09/zcode-cli) | Unofficial terminal client for the agent runtime shipped with ZCode Desktop | 117 | 🟢 | TypeScript |
| [cloclo (claude-code-sdk)](https://github.com/SeifBenayed/cloclo) | Reverse-engineered Claude Code to build single-file SDK CLIs in Node, Python, Go, Rust | 116 | 🟢 | JavaScript |
| [eclipse-github-copilot-integration](https://github.com/masecla22/eclipse-github-copilot-integration) | Open source GitHub Copilot integration for Eclipse | 114 | 🔴 | Java |
| [llm-openai-via-codex](https://github.com/simonw/llm-openai-via-codex) | Reverse-engineered Codex CLI auth to call OpenAI models via a Codex subscription | 114 | 🟢 | Python |
| [cpa-multi-plugins](https://github.com/mmqz/cpa-multi-plugins) | CLIProxyAPI OAuth provider plugins for CodeBuddy, Trae and Qoder | 112 | 🟢 | Go |
| [AntigravityProxyLauncher](https://github.com/OpsinTech/AntigravityProxyLauncher) | DYLD-injection transparent proxy for Antigravity/Gemini with MITM of AI traffic | 109 | 🟢 | C++ |
| [clodex](https://github.com/bman654/clodex) | Bridges Claude Code to OpenAI models via API key or ChatGPT/Codex-plan OAuth | 106 | 🟢 | TypeScript |
| [xcode-copilot-server](https://github.com/theblixguy/xcode-copilot-server) | GitHub Copilot proxy for Xcode with Claude Agent and Codex Agent support | 105 | 🟢 | TypeScript |
| [antigravity-add-model](https://github.com/vahapogut/antigravity-add-model) | Patch for Google Antigravity that intercepts its internal Cloud Code API to add other LLM providers | 104 | 🟢 | TypeScript |
| [claude-codex](https://github.com/fuergaosi233/claude-codex) | Adapter letting the Codex desktop app drive Claude Code via the Codex app-server protocol | 103 | 🟢 | TypeScript |
| [qoder2api](https://github.com/Zhengyuuuui/qoder2api) | Converts Qoder AI service to OpenAI/Claude/Codex-format API | 98 | 🟢 | Go |
| [zemote](https://github.com/HumanAILoop/zemote) | Remote control client for ZCode Desktop on phones and tablets, built by replicating its protocol | 98 | 🟢 | Dart |
| [AgentHub](https://github.com/HUIdada1/AgentHub) | Reverse proxy turning local Trae, WorkBuddy and Zcode into OpenAI API | 97 | 🟢 | JavaScript |
| [claude-code-source-analysis (xiaonancs)](https://github.com/xiaonancs/claude-code-source-analysis) | Architecture breakdown of 23 Claude Code subsystems from source study | 94 | 🟢 | JavaScript |
| [cursoride2api](https://github.com/7836246/cursoride2api) | Tutorial on reverse engineering the Cursor IDE API | 92 | 🟢 | JavaScript |
| [claude-meter](https://github.com/abhishekray07/claude-meter) | Reverse engineering Claude Code usage limits to track remaining quota | 90 | 🟢 | Python |
| [qoder2api](https://github.com/cubk1/qoder2api) | Qoder reverse engineering and Qoder-to-API demo | 90 | 🟢 | Java |
| [cursorcli2api](https://github.com/Azhi-ss/cursorcli2api) | OpenAI- and Anthropic-compatible HTTP API in front of the Cursor Agent CLI | 89 | 🟢 | TypeScript |
| [kiro2api](https://github.com/nineyuanz/kiro2api) | Kiro to Anthropic/OpenAI API proxy | 82 | 🟢 | Go |
| [antigravity-proxy](https://github.com/frieser/antigravity-proxy) | Gateway exposing Google Antigravity's internal Gemini and Claude APIs | 80 | 🗄️ | TypeScript |
| [cursor-grpc](https://github.com/Jordan-Jarvis/cursor-grpc) | Reverse engineered Cursor IDE gRPC / protobuf definitions | 80 | 🟡 |  |
| [Qoder-2API-Go](https://github.com/EchoPing07/Qoder-2API-Go) | Go OpenAI-compatible API for Qoder | 78 | 🟢 | Go |
| [Antigravity-Database-Manager](https://github.com/ag-donald/Antigravity-Database-Manager) | Database manager and recovery tool for the Google Antigravity IDE conversation store | 77 | 🟢 | Python |
| [Cursor2API](https://github.com/NGLSG/Cursor2API) | Lightweight gateway exposing Cursor's tools/models as an API | 77 | 🟢 | TypeScript |
| [cursor-tab](https://github.com/wisdgod/cursor-tab) | Protocol Buffers definitions for Cursor Tab | 76 | 🗄️ |  |
| [Browserbase Claude Code plugin](https://github.com/browserbase/claude-code-plugin) | Stands in for the Claude in Chrome extension in Claude Code's local browser bridge, on Browserbase | 74 | 🗄️ | JavaScript |
| [cursor_api_demo](https://github.com/eisbaw/cursor_api_demo) | Cursor IDE backend endpoint API reverse engineered (v2.6.22) | 73 | 🟢 | JavaScript |
| [kiro-reverse-api](https://github.com/dangweilinshinidie/kiro-reverse-api) | Reverse-engineered Kiro API with a provider management console | 72 | 🟢 | JavaScript |
| [kirocc](https://github.com/d-kuro/kirocc) | Local proxy forwarding Anthropic Messages API calls to Kiro's backend using Kiro CLI credentials | 72 | 🟢 | Go |
| [copilot-api](https://github.com/QLHazyCoder/copilot-api) | GitHub Copilot to OpenAI/Responses/Anthropic API server | 71 | 🟢 | TypeScript |
| [cursor-account-api](https://github.com/Elawen-Carl/cursor-account-api) | API for obtaining free Cursor trial accounts | 69 | 🟡 | Python |
| [codex-app-linux](https://github.com/better-slop/codex-app-linux) | Unofficial Codex App for Linux with npm, AUR and Nix packaging | 65 | 🟢 | JavaScript |
| [cursor-agent-api-proxy](https://github.com/tageecc/cursor-agent-api-proxy) | Wraps Cursor CLI as an OpenAI-compatible API for any client | 64 | 🟢 | TypeScript |
| [cursor-opencode-auth](https://github.com/Infiland/cursor-opencode-auth) | Use a Cursor account inside the OpenCode TUI | 63 | 🟢 | TypeScript |
| [copilot-api (prassaaa)](https://github.com/prassaaa/copilot-api) | Exposes GitHub Copilot as OpenAI/Anthropic-compatible API for Claude Code | 62 | 🟢 | TypeScript |
| [Antigravity-Proxy](https://github.com/Kazuki-0147/Antigravity-Proxy) | OpenAI/Anthropic/Gemini-compatible Antigravity reverse gateway | 61 | 🟢 | JavaScript |
| [cc-copilot-bridge](https://github.com/FlorianBruniaux/cc-copilot-bridge) | Route Claude Code CLI through a Copilot subscription, Ollama or Anthropic | 61 | 🟢 | Shell |
| [cursor-rpc](https://github.com/everestmz/cursor-rpc) | Reverse engineered RPC client for Cursor.sh cloud services | 61 | 🟡 | JavaScript |
| [copilot-openai-api](https://github.com/yuchanns/copilot-openai-api) | FastAPI proxy turning GitHub Copilot chat completions/embeddings into an OpenAI-compatible service | 60 | 🟢 | Python |
| [coxy](https://github.com/coxy-proxy/coxy) | GitHub Copilot exposed as OpenAI-compatible APIs | 60 | 🟢 | TypeScript |
| [copilot-proxy](https://github.com/jjleng/copilot-proxy) | Make the GitHub Copilot extension work with any LLM by proxying its traffic | 59 | 🟡 | Python |
| [claude-code-reverse](https://github.com/injekt/claude-code-reverse) | Reverse analysis of Claude Code | 58 | 🟢 |  |
| [codex-asr](https://github.com/Wangnov/codex-asr) | Unofficial CLI and Whisper-compatible shim for Codex Desktop speech recognition | 58 | 🟢 | Rust |
| [qoder-proxy](https://github.com/foxy1402/qoder-proxy) | OpenAI API wrapper around the Qoder CLI | 58 | 🟢 | JavaScript |
| [Codex-App-Linux](https://github.com/areu01or00/Codex-App-Linux) | Codex App (macOS) ported to Linux | 57 | 🟢 | JavaScript |
| [cursor2api](https://github.com/gopkg-dev/cursor2api) | Proxy converting Cursor's docs chat endpoint to an OpenAI-compatible API | 57 | 🟡 | Go |
| [antigravity-proxy](https://github.com/elad12390/antigravity-proxy) | Intercepts Google Antigravity IDE API calls to use your own Gemini key | 56 | 🗄️ | Python |
| [claw-decode](https://github.com/fattail4477/claw-decode) | Decodes leaked Claude Code source: hidden features, 43 tool definitions, system prompts | 56 | 🟢 | TypeScript |
| [copilot-proxy](https://github.com/hankchiutw/copilot-proxy) | HTTP proxy exposing GitHub Copilot free quota as an OpenAI-compatible API | 55 | 🟡 | TypeScript |
| [cursor2api](https://github.com/mt-altman/cursor2api) | Converts Cursor chat into an OpenAI-compatible API | 55 | 🗄️ | JavaScript |
| [copilot-proxy-api](https://github.com/voidsteed/copilot-proxy-api) | Self-hosted GitHub Copilot bridge for Claude Code and Codex CLI | 54 | 🟢 | TypeScript |
| [copilot-api-plus](https://github.com/imbuxiangnan-cyber/copilot-api-plus) | GitHub Copilot proxy with OpenAI Responses and Anthropic Messages APIs | 53 | 🟢 | TypeScript |
| [lingma-proxy](https://github.com/Lutiancheng1/lingma-proxy) | OpenAI/Anthropic-compatible proxy for Alibaba Lingma and QoderCN | 50 | 🟢 | Go |
| [claude-max-api-proxy (sethschnrt)](https://github.com/sethschnrt/claude-max-api-proxy) | Exposes a Claude Max subscription as an OpenAI-compatible API | 49 | 🟢 | TypeScript |
| [cliproxy-rs](https://github.com/vayungodara/cliproxy-rs) | Rust port of CLIProxyAPI, the LLM-subscription-to-API proxy | 46 | 🟢 | Rust |
| [copilot-proxy (Jer-y)](https://github.com/Jer-y/copilot-proxy) | Turns GitHub Copilot into an OpenAI/Anthropic-compatible server | 45 | 🟢 | TypeScript |
| [kiro2api-deno](https://github.com/AAEE86/kiro2api-deno) | Deno Kiro-to-API proxy | 45 | 🟢 | TypeScript |
| [claude-code-reverse](https://github.com/V1ki/claude-code-reverse) | Claude Code reverse engineering notes on prompts, tool design and flow | 44 | 🟢 |  |
| [antigravity-proxy](https://github.com/12errh/antigravity-proxy) | Proxy intercepting Antigravity's Gemini API and rerouting to other providers | 41 | 🟢 | TypeScript |
| [ampcode-connector](https://github.com/nghyane/ampcode-connector) | Routes AmpCode requests through local Claude Code, Codex CLI and Gemini OAuth credentials | 38 | 🟢 | TypeScript |
| [expose-github-copilot-http-api](https://github.com/purocean/expose-github-copilot-http-api) | Exposes VS Code's GitHub Copilot as an HTTP API | 38 | 🟡 | JavaScript |
| [kiro2Api](https://github.com/Lavender3533/kiro2Api) | Kiro to API proxy | 38 | 🟢 | JavaScript |
| [claude-code-copilot](https://github.com/samarth777/claude-code-copilot) | Local proxy translating Claude Code's Anthropic API to GitHub Copilot | 37 | 🟢 | JavaScript |
| [copilot2api](https://github.com/whtsky/copilot2api) | Go proxy exposing GitHub Copilot as OpenAI and Anthropic endpoints | 37 | 🟢 | Go |
| [agent-hop](https://github.com/hetpatel-11/agent-hop) | Reverse-engineered coding agents' session formats to resume sessions across agents | 36 | 🟢 | Rust |
| [gemini-cli-proxy](https://github.com/ubaltaci/gemini-cli-proxy) | Uses Gemini CodeAssist (Gemini CLI) through OpenAI/Anthropic API interfaces | 36 | 🟡 | TypeScript |
| [kiro2api-rs](https://github.com/vagmr/kiro2api-rs) | Rust Kiro-to-Anthropic API proxy with account pool | 35 | 🟢 | Rust |
| [claude-code-reverse-engineering](https://github.com/jung-wan-kim/claude-code-reverse-engineering) | Reverse-engineered design documents and specs of the Claude Code CLI | 34 | 🟢 | HCL |
| [Kiro-Go](https://github.com/hj01857655/Kiro-Go) | Go/Gin Kiro API proxy with OpenAI and Anthropic compatibility | 34 | 🟢 | Go |
| [codebuddy2api](https://github.com/orangeboyChen/codebuddy2api) | Proxies Tencent CodeBuddy with OpenAI and Anthropic compatible APIs | 33 | 🟢 | TypeScript |
| [claude-agent-sdk-go (character-ai)](https://github.com/character-ai/claude-agent-sdk-go) | Go SDK for Claude agents over the Claude Code CLI | 32 | 🟢 | Go |
| [raven](https://github.com/nocoo/raven) | GitHub Copilot proxy translating to Anthropic/OpenAI APIs with usage dashboard | 32 | 🟢 | TypeScript |
| [claude-code-reverse](https://github.com/apstenku123/claude-code-reverse) | Claude Code reverse engineering | 30 | 🟡 | JavaScript |
| [cursorToApi](https://github.com/dreamhartley/cursorToApi) | Converts Cursor into an OpenAI-compatible API | 30 | 🟡 | JavaScript |
| [claude-code (nadonghuang)](https://github.com/nadonghuang/claude-code) | Deobfuscated Claude Code v2.1.76 TypeScript reconstructed from the npm package | 26 | 🟢 | TypeScript |
| [claude-code-haha](https://github.com/jiahuangzheng/claude-code-haha) | Locally runnable build of the leaked Claude Code source | 26 | 🟢 | TypeScript |
| [claude_agent_sdk_rust](https://github.com/Wally869/claude_agent_sdk_rust) | Unofficial Rust SDK speaking the Claude Code CLI control protocol | 26 | 🟢 | Rust |
| [claude-agent-sdk-go (schlunsen)](https://github.com/schlunsen/claude-agent-sdk-go) | Go port of the Claude Agent SDK driving the Claude Code CLI protocol | 25 | 🟢 | Go |
| [codex2api (rokyplay)](https://github.com/rokyplay/codex2api) | OpenAI Codex API proxy with format conversion and dashboard | 25 | 🟢 | JavaScript |
| [kiro-proxy](https://github.com/Colin3191/kiro-proxy) | Kiro API proxy with OpenAI and Anthropic compatible endpoints | 25 | 🟢 | JavaScript |
| [cursor-api](https://github.com/zeke-chin/cursor-api) | Cursor chat API reverse proxy | 24 | 🟡 | Rust |
| [codex2claudecode](https://github.com/alvin0/codex2claudecode) | Bun local API that exposes Codex, Kiro and Copilot subscriptions as a Claude-compatible endpoint | 23 | 🟢 | TypeScript |
| [minimax-agent-linux](https://github.com/unn-Known1/minimax-agent-linux) | Unofficial Linux port of the MiniMax Agent desktop app | 23 | 🟢 | JavaScript |
| [codex-browser-bridge](https://github.com/DeliciousBuding/codex-browser-bridge) | Exposes ChatGPT desktop app's internal browser bridge as an MCP server | 22 | 🟢 | Rust |
| [trae-api-proxy](https://github.com/muskke/trae-api-proxy) | Go proxy bridging the Trae IDE API to the OpenAI standard API | 22 | 🟢 | Go |
| [Antigravity2Api](https://github.com/anshulrules/Antigravity2Api) | Transforms Antigravity into standard Claude and Gemini APIs | 21 | 🟢 | JavaScript |
| [claude-agent-sdk-go (Roasbeef)](https://github.com/Roasbeef/claude-agent-sdk-go) | Go SDK for Claude Code with tool use, MCP and streaming | 21 | 🟢 | JavaScript |
| [copilot-proxy-go](https://github.com/tonghaoch/copilot-proxy-go) | Go server turning GitHub Copilot into OpenAI/Anthropic-compatible API | 21 | 🟢 | Go |
| [cursor2api-go](https://github.com/yourChainGod/cursor2api-go) | Go Cursor-to-OpenAI API bridge with Messages/Responses/Tools support | 20 | 🟢 | Go |
| [qodercli-reverse](https://github.com/alingse/qodercli-reverse) | Reverse engineering of the Qoder CLI | 19 | 🟢 | Go |
| [Deno-Augment2Api](https://github.com/xiaojia21190/Deno-Augment2Api) | Deno port of Augment2Api | 18 | 🟡 | TypeScript |
| [Harness Studio](https://github.com/vigneshv1cky/harness-studio) | Desktop coding agent app for macOS and Linux modeled on reverse-engineered Claude Code Desktop | 18 | 🟢 | JavaScript |
| [codexfast-current-launcher](https://github.com/qiaojiangwink/codexfast-current-launcher) | Runtime launcher enabling hidden client flags (Fast mode) in Codex/ChatGPT Desktop | 17 | 🟢 | JavaScript |
| [copilot-api](https://github.com/patchescamerababy/copilot-api) | GitHub Copilot to OpenAI API | 17 | 🟢 | Java |
| [dsh-trae-api](https://github.com/Wang-JQ77/dsh-trae-api) | Exposes Trae Work CN credits as local OpenAI/Anthropic API | 17 | 🟢 | JavaScript |
| [kiro-reverse-api](https://github.com/tanu360/kiro-reverse-api) | Self-hosted Kiro API proxy with OpenAI/Anthropic endpoints and admin dashboard | 17 | 🟢 | Go |
| [windsurf-api](https://github.com/AlexStrNik/windsurf-api) | REST API that sends prompts with images to Windsurf chat | 17 | 🟢 | JavaScript |
| [claude-code-leaked-source](https://github.com/sleeplessai/claude-code-leaked-source) | Mirror of the leaked Claude Code source | 16 | 🗄️ | TypeScript |
| [copilot-RE](https://github.com/rohitaryal/copilot-RE) | Reverse engineered GitHub Copilot API plus CLI | 16 | 🟡 | TypeScript |
| [windsurf-proxy](https://github.com/pqhaz3925/windsurf-proxy) | MITM proxy for Windsurf IDE that swaps the LLM backend for your own Anthropic key | 16 | 🟢 | JavaScript |
| [Copilot_Proxy](https://github.com/Open-Copilot-Proxy/Copilot_Proxy) | Self-hosted GitHub Copilot to OpenAI-compatible proxy with OAuth | 15 | 🟢 | Go |
| [cursor2api (AstroQore)](https://github.com/AstroQore/cursor2api) | Cursor subscription as OpenAI API via direct agent.v1 protocol | 15 | 🟢 | TypeScript |
| [codex-harness-internals](https://github.com/AlexKenbo/codex-harness-internals) | Reverse-engineered spec of the OpenAI Codex CLI harness: loop, tools, compaction | 14 | 🟢 |  |
| [claude-max-api-proxy (GodYeh)](https://github.com/GodYeh/claude-max-api-proxy) | Claude Max subscription as OpenAI-compatible API with tool calling | 13 | 🟢 | TypeScript |
| [copilot-api-proxy](https://github.com/messense/copilot-api-proxy) | Reverse proxy for GitHub Copilot API with OpenAI/Anthropic endpoints | 13 | 🗄️ | Rust |
| [kiro2api (xwteam)](https://github.com/xwteam/kiro2api) | Rust Kiro relay speaking Anthropic, OpenAI, Responses and Gemini protocols | 13 | 🟢 | Rust |
| [learn-claude-code](https://github.com/cnlnlhb/learn-claude-code) | Research repo for @anthropic-ai/claude-code v2.1.88 reconstructed from the npm package and sourcemap | 12 | 🟢 | TypeScript |
| [noclick](https://github.com/noclickapp/noclick) | Agent runtime that runs on your ChatGPT or Claude subscription | 12 | 🟢 | Python |
| [gemini-3-github-copilot-proxy](https://github.com/Apothic-AI/gemini-3-github-copilot-proxy) | Use a Gemini plan via Gemini CLI auth inside GitHub Copilot | 11 | 🟢 | TypeScript |
| [agy-tools-rust](https://github.com/ChrAlpha/agy-tools-rust) | Rust CLI reverse proxy exposing Antigravity Cloud Code as OpenAI/Claude/Gemini APIs | 9 | 🗄️ | Rust |
| [claude-buddy-hatchery](https://github.com/cminn10/claude-buddy-hatchery) | Reverse-engineered Claude Code /buddy companion generation algorithm | 9 | 🟢 | Python |
| [kiro2api-rs](https://github.com/gdtiti/kiro2api-rs) | Rust Anthropic-compatible proxy over Kiro accounts with web panel | 9 | 🟢 | Rust |
| [antigravity-proxy (sortedcord)](https://github.com/terastal-hq/antigravity-proxy) | Go proxy to Antigravity's internal Gemini API with quota tracking | 8 | 🟢 | Go |
| [claude-max-api-proxy-rs](https://github.com/thhuang/claude-max-api-proxy-rs) | Rust proxy translating OpenAI/Anthropic APIs to Claude Code CLI subscription | 8 | 🟢 | Rust |
| [cursor2api (KonghaYao)](https://github.com/KonghaYao/cursor2api) | Cursor subscription to Anthropic/OpenAI endpoint on Cloudflare or Deno | 8 | 🟢 | TypeScript |
| [gh_copilot_chat](https://github.com/rabilrbl/gh_copilot_chat) | Unofficial GitHub Copilot Chat SDK built on the reverse engineered API | 8 | 🟡 | Python |
| [antigravity-proxy (usamashehab)](https://github.com/usamashehab/antigravity-proxy) | OpenAI-compatible proxy for Antigravity's Gemini and Claude models via OAuth | 7 | 🟢 | Python |
| [claude-cli-protocol](https://github.com/mzhaom/claude-cli-protocol) | Protocol documentation for the Claude Code CLI stream-json interface | 7 | 🟢 | Go |
| [claude-code-decompiled](https://github.com/alanisme/claude-code-decompiled) | Research reports from Claude Code source analysis: agent loop, telemetry, permissions | 7 | 🟢 |  |
| [kiro-proxy (bigdata2211it-web)](https://github.com/bigdata2211it-web/kiro-proxy) | OpenAI-compatible local proxy for Kiro CLI (Amazon CodeWhisperer) | 7 | 🟢 | JavaScript |
| [open-claude-code](https://github.com/sweetcornna/open-claude-code) | Community reverse-engineered restoration of the Claude Code CLI | 7 | 🟢 | TypeScript |
| [windsurf-api (imbuxiangnan)](https://github.com/imbuxiangnan-cyber/windsurf-api) | Turns a Windsurf subscription into an OpenAI/Anthropic-compatible API | 7 | 🟢 | TypeScript |
| [augloop-copilot-proxy](https://github.com/suimi8/augloop-copilot-proxy) | Reverse proxy turning Microsoft 365 Excel Copilot (AugLoop) into an OpenAI API | 6 | 🟢 | Python |
| [claude-code-internals (eran-broder)](https://github.com/eran-broder/claude-code-internals) | Undocumented Claude Code internals found by having Claude reverse-engineer itself | 6 | 🟢 | Python |
| [claude-code-internals (swyxio)](https://github.com/swyxio/claude-code-internals) | Evidence-linked reconstruction of Claude Code internals from the native Bun executable | 6 | 🟢 | JavaScript |
| [Claude-Chrome-Reverse](https://github.com/Elity/Claude-Chrome-Reverse) | Reverse-engineered Claude for Chrome extension modified to accept an API key | 5 | 🟢 | JavaScript |
| [cursor2api (Yuki13929)](https://github.com/Yuki13929/cursor2api) | Anthropic Messages / OpenAI API for Cursor models via the reverse-engineered agent protocol | 5 | 🟢 | Python |
| [ferridex](https://github.com/afengleafs/ferridex) | Local Codex and Claude subscription proxy with web dashboard | 5 | 🟢 | Go |
| [niri-computer-use](https://github.com/lihaoze123/niri-computer-use) | Patched Codex Desktop Computer Use backend for NixOS + niri | 5 | 🟢 | Nix |
| [claude-rc-api](https://github.com/ThatCrispyToast/claude-rc-api) | Reverse-engineered Claude Code Remote Control / Sessions API | 4 | 🟢 | Python |
| [cursor-tab](https://github.com/abyesilyurt/cursor-tab) | Reverse-engineered Cursor tab completion client | 4 | 🟢 | Python |
| [anti-client](https://github.com/Makobcki/anti-client) | Async Python client for Google Antigravity's internal API | 2 | 🟢 | Python |
| [claudex](https://github.com/m0n0x41d/claudex) | Translates Anthropic Messages API to the Codex backend Responses API via Codex device-flow auth | 2 | 🟢 | Rust |
| [codex-openai-proxy](https://github.com/0oAstro/codex-openai-proxy) | OpenAI-compatible proxy over ChatGPT/Codex subscription backend using the Codex CLI OAuth flow | 2 | 🟢 | Rust |
| [pollux](https://github.com/yeshanjun/pollux) | Gemini CLI reverse proxy speaking to raw Cloud Code Gemini endpoints | 1 | 🟢 | Rust |
| [claude-cleanroom-2.1.83](https://github.com/nwyin/claude-cleanroom-2.1.83) | Architecture docs reverse-engineered from Claude Code v2.1.83 | 0 | 🟢 |  |
| [claude-code-diff-plugin](https://github.com/takuyanagai0213/claude-code-diff-plugin) | Diffs Claude Code binaries between releases to surface unreleased features | 0 | 🟢 |  |
| [claude-code-reverse (hqman)](https://github.com/hqman/claude-code-reverse) | Reverse engineering Claude Code's minified cli.mjs with LLMs | 0 | 🟡 | JavaScript |
| [codex-subscription-proxy](https://github.com/Caleb0796/codex-subscription-proxy) | OpenAI Responses-compatible proxy using Codex/ChatGPT subscription auth | 0 | 🟢 | JavaScript |

## Image/Audio/Video Gen APIs

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [midjourney-proxy](https://github.com/novicezk/midjourney-proxy) | Proxies Midjourney's Discord channel to provide an HTTP API for image generation | 5,370 | 🟡 | Java |
| [suno-api](https://github.com/gcui-art/suno-api) | Unofficial self-hostable REST API for Suno music generation via its internal endpoints | 3,278 | 🟢 | TypeScript |
| [flow2api](https://github.com/TheSmallHanCat/flow2api) | Reverse-engineered Google Flow API for Nano Banana Pro and Veo generation | 3,082 | 🟢 | Python |
| [midjourney-api (zcpua)](https://github.com/zcpua/midjourney-api) | Unofficial Node.js Midjourney client over Discord | 1,866 | 🟢 | TypeScript |
| [Suno-API](https://github.com/SunoAI-API/Suno-API) | Unofficial Suno music generation API | 1,815 | 🟡 | Python |
| [sora2api](https://github.com/TheSmallHanCat/sora2api) | Reverse-engineered Sora web API with account pool | 1,238 | 🗄️ | Python |
| [jimeng-api](https://github.com/iptag/jimeng-api) | Reverse-engineered Jimeng/Dreamina text-to-image, image-to-image and video API | 1,041 | 🗄️ | TypeScript |
| [midjourney-api (yokonsan)](https://github.com/yokonsan/midjourney-api) | Midjourney Discord API wrapper as REST service: imagine, upscale, variation, describe | 891 | 🟡 | Python |
| [midjourney-proxy](https://github.com/trueai-org/midjourney-proxy) | Midjourney Discord proxy exposing an image generation API | 824 | 🟢 | C# |
| [ttsfm](https://github.com/dbccccccc/ttsfm) | OpenAI-compatible TTS API mirroring the free openai.fm service | 739 | 🟢 | Python |
| [jimeng-free-api-all](https://github.com/zhizinan1997/jimeng-free-api-all) | Jimeng (ByteDance) image and video generation reverse API, OpenAI-compatible | 641 | 🟢 | TypeScript |
| [midjourney-proxy-plus](https://github.com/litter-coder/midjourney-proxy-plus) | Extended Midjourney Discord proxy API | 575 | 🟡 |  |
| [hass-edge-tts](https://github.com/hasscc/hass-edge-tts) | Microsoft Edge read-aloud TTS in Home Assistant via the unofficial Edge speech endpoint, no key | 488 | 🟢 | Python |
| [Midjourney_api](https://github.com/George-iam/Midjourney_api) | Unofficial Midjourney API via Discord sender/receiver (research only) | 419 | 🔴 | Python |
| [SunoSongsCreator](https://github.com/yihong0618/SunoSongsCreator) | Reverse engineered Suno song generation API (Python library and CLI) | 367 | 🟡 | Python |
| [gflow-cli](https://github.com/ffroliva/gflow-cli) | Unofficial reverse-engineered CLI for Google Flow (Veo video, Imagen) | 334 | 🟢 | Python |
| [capcut-tts-api](https://github.com/K07VN/capcut-tts-api) | Reverse-engineered CapCut TTS and STT API | 306 | 🟢 | Python |
| [sora-downloader](https://github.com/tibbar213/sora-downloader) | Extracts watermark-free Sora video links | 305 | 🟢 | Python |
| [BingImageCreator](https://github.com/acheong08/BingImageCreator) | Reverse engineered API for Microsoft Bing Image Creator (DALL-E) | 302 | 🗄️ | Python |
| [Suno2openai](https://github.com/wlhtea/Suno2openai) | Calls the Suno web API in OpenAI format with a cookie pool | 275 | 🟡 | Python |
| [imagineapi](https://github.com/imagineapi/imagineapi) | Unofficial Midjourney API | 227 | 🟡 | TypeScript |
| [klingCreator](https://github.com/yihong0618/klingCreator) | Reverse engineered API for Kling AI image and video generation | 223 | 🟡 | Python |
| [UdioWrapper](https://github.com/flowese/UdioWrapper) | Python package generating music tracks through Udio's unofficial API | 182 | 🟡 | Python |
| [Suno-API (Go)](https://github.com/Suno-API/Suno-API) | Unofficial Suno AI API in Go supporting songs, lyrics and OpenAI chat format | 159 | 🟡 | Go |
| [midjourney-discord-api-php](https://github.com/ferranfg/midjourney-discord-api-php) | Generate Midjourney images through the Discord API (PHP) | 135 | 🗄️ | PHP |
| [imageFX-api](https://github.com/rohitaryal/imageFX-api) | Unofficial reverse-engineered API for Google Labs ImageFX | 134 | 🟢 | TypeScript |
| [Luma-API](https://github.com/LumaAI-API/Luma-API) | Unofficial Luma Dream Machine video generation API | 130 | 🟡 | Go |
| [Suno-API (Malith-Rukshan)](https://github.com/Malith-Rukshan/Suno-API) | Unofficial Suno.ai Python library and REST API | 129 | 🟡 | Python |
| [notebooklm-podcast-automator](https://github.com/israelbls/notebooklm-podcast-automator) | REST API automating NotebookLM sources and Audio Overview generation | 117 | 🟢 | Python |
| [Midjourney-Web-API](https://github.com/CelestialRipple/Midjourney-Web-API) | Unofficial Midjourney web API using captured browser request headers | 115 | 🔴 | Python |
| [CapCut-TTS](https://github.com/kuwacom/CapCut-TTS) | CapCut text-to-speech wrapper API | 113 | 🟢 | TypeScript |
| [midjourney-proxy](https://github.com/webman-php/midjourney-proxy) | Full-featured Midjourney Discord proxy (PHP/webman) | 105 | 🟢 | PHP |
| [whisk-api](https://github.com/rohitaryal/whisk-api) | Unofficial reverse-engineered API for Google Labs Whisk | 101 | 🟢 | TypeScript |
| [vidai](https://github.com/igolaizola/vidai) | Unofficial RunwayML Gen-2/Gen-3 video generation client | 97 | 🟡 | Go |
| [suno-api](https://github.com/gochendong/suno-api) | Suno music generation API wrapper | 88 | 🟢 | Python |
| [midjourney-python-api](https://github.com/ezioruan/midjourney-python-api) | Python client for the unofficial Midjourney API through Discord | 87 | 🔴 | Python |
| [IdeoImageCreator](https://github.com/yihong0618/IdeoImageCreator) | Reverse engineered API for Ideogram image generation | 77 | 🟡 | Python |
| [Bimg](https://github.com/nociza/Bimg) | Reverse-engineered Bing Image Creator API as an NPM package | 76 | 🔴 | TypeScript |
| [IdeogramWrapper](https://github.com/flowese/IdeogramWrapper) | Python wrapper for Ideogram image generation | 76 | 🔴 | Python |
| [craiyon.py](https://github.com/FireHead90544/craiyon.py) | Unofficial API wrapper for Craiyon image generation | 70 | 🟡 | Python |
| [suno-api-private](https://github.com/joeseesun/suno-api-private) | Suno API with JWT token authentication support | 70 | 🟢 | TypeScript |
| [suno-cli](https://github.com/paperfoot/suno-cli) | Terminal client for Suno music generation | 60 | 🟢 | Rust |
| [bingart](https://github.com/DedInc/bingart) | Unofficial async API wrapper for Bing Image and Video Creator | 57 | 🟢 | Python |
| [Comfyui-GeminiWeb](https://github.com/Koko-boya/Comfyui-GeminiWeb) | ComfyUI node using the Gemini web API for image generation and chat | 52 | 🟢 | Python |
| [Suno-API](https://github.com/imyizhang/Suno-API) | Unofficial Suno AI API | 50 | 🟡 | Python |
| [dreamina-api](https://github.com/LiJunYi2/dreamina-api) | Dreamina (CapCut AI) image generation API on Cloudflare Workers | 49 | 🟢 | TypeScript |
| [Lexica.art](https://github.com/NotCookey/Lexica.art) | Reverse-engineered Python API wrapper for Lexica.art image generation | 41 | 🔴 | Python |
| [py-midjourney-proxy](https://github.com/Anychnn/py-midjourney-proxy) | Python Midjourney Discord proxy | 41 | 🟡 | Python |
| [stable-diffusion-xl-api](https://github.com/KoushikNavuluri/stable-diffusion-xl-api) | Reverse-engineered API for Stable Diffusion XL 1.0 text-to-image | 41 | 🔴 | Python |
| [wombot](https://github.com/adri326/wombot) | Unofficial API and Discord bot for Wombo Dream art generation | 34 | 🔴 | JavaScript |
| [reve-sdk](https://github.com/FlintSH/reve-sdk) | Unofficial SDK for the Reve AI image generation web service | 27 | 🟡 | TypeScript |
| [suno-ai](https://github.com/hissincn/suno-ai) | JavaScript API for generating songs on suno.ai | 26 | 🟡 | JavaScript |
| [Msdesigner-api](https://github.com/imnotdev25/Msdesigner-api) | Reverse-engineered API for Microsoft Designer image generation | 25 | 🗄️ | Python |
| [flow2api (HL320217)](https://github.com/HL320217/flow2api) | Multi-user platform over the Google Flow / Labs FX protocol for image and video | 23 | 🟢 |  |
| [suno-ai-proxy](https://github.com/MelohubAI/suno-ai-proxy) | Unofficial Suno AI Node.js API | 23 | 🟡 | TypeScript |
| [wombo-dream-api](https://github.com/leopoldhub/wombo-dream-api) | Unofficial API for the Wombo Dream image generator | 19 | 🗄️ | TypeScript |
| [wisprflow-sdk](https://github.com/ThisisShashwat/wisprflow-sdk) | Python SDK over Wispr Flow's reverse-engineered audio transcription API | 18 | 🟢 | Python |
| [suno-mcp](https://github.com/CodeKeanu/suno-mcp) | MCP server for generating songs through Suno's web API | 16 | 🟢 | Python |
| [suno-api](https://github.com/worthable/suno-api) | Unofficial API for Suno AI music generation | 15 | 🟡 | TypeScript |
| [SunoApiManager](https://github.com/serkansmg/SunoApiManager) | Unofficial Suno backend API with websocket, FastAPI and Swagger | 12 | 🟢 | HTML |
| [opensuno](https://github.com/paean-ai/opensuno) | Open Suno API and MCP server for AI agents | 11 | 🟢 | TypeScript |
| [chatgpt2api (fran0220)](https://github.com/fran0220/chatgpt2api) | Reverse proxy turning ChatGPT web image generation into OpenAI API endpoints | 7 | 🟢 | Go |
| [go-sora2api](https://github.com/DouDOU-start/go-sora2api) | Go reimplementation of sora2api, OpenAI-compatible wrapper for Sora app | 7 | 🟢 | TypeScript |
| [pixaiAPI](https://github.com/shidktbw/pixaiAPI) | Unofficial Python API for the pixai.art image generator | 7 | 🟡 | Python |
| [UdioOfflineLibrary](https://github.com/SirBitesalot/UdioOfflineLibrary) | Desktop app to browse and download your full Udio library | 7 | 🟢 | Python |
| [unofficial-suno-api](https://github.com/sunyujingmusic-alt/unofficial-suno-api) | Unofficial Suno API for research | 7 | 🟢 | TypeScript |
| [Prisma-Python](https://github.com/arunKumarNOP/Prisma-Python) | Reverse-engineered Prisma style-transfer API from the Android app | 5 | 🔴 |  |
| [AIKitchen-API](https://github.com/mir-ashiq/AIKitchen-API) | Unofficial API for Google AI Test Kitchen music and image generation | 3 | 🟡 | Python |
| [SunoAPI (tinyfeng)](https://github.com/tinyfeng/SunoAPI) | Unofficial Suno API in Python/FastAPI with token keep-alive | 1 | 🟡 | Python |

## MCP Servers for Private APIs

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | MCP server for Xiaohongshu (RedNote): login, publish, search, comment | 16,555 | 🟢 | Go |
| [whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) | WhatsApp MCP server built on whatsmeow web multidevice protocol | 6,717 | 🟡 | Go |
| [gemini-notebook-mcp-cli](https://github.com/jacob-bd/gemini-notebook-mcp-cli) | CLI and MCP server for Gemini Notebook (NotebookLM) via its internal RPC API | 6,389 | 🟢 | Python |
| [linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server) | LinkedIn MCP server for profiles, companies, jobs and messages via browser session | 4,009 | 🟢 | Python |
| [notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp) | MCP server letting agents query Google NotebookLM with citations | 3,440 | 🗄️ | TypeScript |
| [slack-mcp-server](https://github.com/korotovsky/slack-mcp-server) | Slack MCP server that can use browser session tokens and the undocumented Slack Edge API | 1,872 | 🟢 | Go |
| [garmin_mcp](https://github.com/Taxuspt/garmin_mcp) | MCP server for Garmin Connect data via unofficial API | 1,406 | 🟢 | Python |
| [douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server) | Douyin MCP extracting watermark-free video links and transcripts | 1,280 | 🗄️ | HTML |
| [mcp-server-weread (freestylefly)](https://github.com/freestylefly/mcp-server-weread) | MCP server for WeChat Read (WeRead) shelf and notes | 583 | 🟡 | JavaScript |
| [Agentify Desktop](https://github.com/agentify-sh/desktop) | Lets coding agents drive logged-in ChatGPT, Claude, Gemini, Grok, Perplexity web sessions via MCP | 570 | 🟢 | JavaScript |
| [mcp-server-12306](https://github.com/drfccv/mcp-server-12306) | MCP server for China Railway 12306 ticket and station queries | 414 | 🟢 | Python |
| [mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp) | MCP server for macOS Messages: read chat.db and send iMessages | 335 | 🟢 | Python |
| [WeChat-MCP](https://github.com/BiboyQG/WeChat-MCP) | Lets AI assistants read and reply to WeChat on desktop | 284 | 🟢 | Python |
| [whatsapp-mcp (verygoodplugins)](https://github.com/verygoodplugins/whatsapp-mcp) | WhatsApp MCP server for reading and sending personal messages | 262 | 🟢 | Go |
| [bambu-printer-mcp](https://github.com/DMontgomery40/bambu-printer-mcp) | MCP server controlling Bambu Lab 3D printers with slicing and print management | 237 | 🟢 | JavaScript |
| [notebooklm-mcp (roomi-fields)](https://github.com/roomi-fields/notebooklm-mcp) | NotebookLM over MCP plus local REST API, audio/video generation | 210 | 🟢 | TypeScript |
| [netease-music-mcp (Vael-KY)](https://github.com/Vael-KY/netease-music-mcp) | MCP server reading and managing a NetEase Cloud Music account | 208 | 🟢 | Python |
| [perplexity-web-mcp (jacob-bd)](https://github.com/jacob-bd/perplexity-web-mcp) | MCP server and Anthropic-compatible API over the Perplexity web interface | 204 | 🟢 | Python |
| [linkedin-mcp-server (eliasbiondo)](https://github.com/eliasbiondo/linkedin-mcp-server) | LinkedIn MCP server scraping people, companies and jobs | 201 | 🟢 | Python |
| [bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js) | Bilibili video search MCP service | 195 | 🟢 | TypeScript |
| [bilibili-mcp-server](https://github.com/huccihuang/bilibili-mcp-server) | MCP server for Bilibili web API operations | 192 | 🟡 | Python |
| [trainingpeaks-mcp](https://github.com/JamsusMaximus/trainingpeaks-mcp) | TrainingPeaks MCP server using the private web API, no API approval needed | 185 | 🟢 | Python |
| [comet-mcp](https://github.com/hanzili/comet-mcp) | MCP server driving Perplexity Comet browser over CDP | 180 | 🟢 | TypeScript |
| [mcp-server-weread (ChenyqThu)](https://github.com/ChenyqThu/mcp-server-weread) | MCP server exposing WeRead books, highlights and notes | 171 | 🟡 | JavaScript |
| [apple-notes-mcp (sweetrb)](https://github.com/sweetrb/apple-notes-mcp) | MCP server to read, search, edit and export Apple Notes on macOS | 170 | 🟢 | TypeScript |
| [xiaohongshu-mcp-python](https://github.com/luyike221/xiaohongshu-mcp-python) | Python Xiaohongshu MCP for automated posting of notes and videos | 146 | 🟢 | TypeScript |
| [bilibili-mcp (adoresever)](https://github.com/adoresever/bilibili-mcp) | Bilibili MCP with search, comments, subtitles and danmaku | 145 | 🟢 | Python |
| [totem](https://github.com/thebriangao/totem) | MCP server with read/write access to Whoop data via the private reverse-engineered API | 135 | 🟢 | TypeScript |
| [apple-notes-mcp (sirmews)](https://github.com/sirmews/apple-notes-mcp) | MCP server reading the Apple Notes SQLite store | 131 | 🗄️ | Python |
| [line-desktop-mcp](https://github.com/dtwang/line-desktop-mcp) | MCP server integrating AI tools with LINE Desktop to read and send messages | 126 | 🟢 | JavaScript |
| [netease-music-mcp (Cheiineeey)](https://github.com/Cheiineeey/netease-music-mcp) | NetEase Cloud Music MCP for song requests, lyrics and playlists | 114 | 🟢 | HTML |
| [perplexity-web-api-mcp](https://github.com/mishamyrt/perplexity-web-api-mcp) | Perplexity AI MCP using the web API, no API key | 107 | 🗄️ | Rust |
| [alza-mcp-community](https://github.com/lukabudik/alza-mcp-community) | Unofficial MCP server for Alza.cz: product search, reviews, account, cart and checkout | 88 | 🟢 | TypeScript |
| [whatsapp-mcp-ts](https://github.com/jlucaso1/whatsapp-mcp-ts) | WhatsApp MCP server in TypeScript on Baileys | 75 | 🟢 | TypeScript |
| [miot-mcp](https://github.com/javen-yan/miot-mcp) | MCP server for Mijia devices built on the unofficial MijiaAPI | 73 | 🟢 | Python |
| [garmin-connect-mcp](https://github.com/eddmann/garmin-connect-mcp) | MCP server for Garmin Connect activities, health metrics and sleep via the unofficial API | 64 | 🟢 | Python |
| [stockbit-mcp](https://github.com/INo-xious/stockbit-mcp) | MCP server for Stockbit (Indonesia) market data, charts and read-only portfolios via its app API | 54 | 🟢 | TypeScript |
| [tradingview-mcp-server](https://github.com/fiale-plus/tradingview-mcp-server) | Unofficial MCP and CLI for TradingView's internal API | 53 | 🟢 | TypeScript |
| [Perplexity-Comet-MCP](https://github.com/RapierCraft/Perplexity-Comet-MCP) | MCP server connecting Claude Code to Perplexity Comet browser | 52 | 🟢 | TypeScript |
| [blinkit-mcp](https://github.com/hereisSwapnil/blinkit-mcp) | Unofficial MCP server to search, cart and order on Blinkit | 51 | 🟢 | Python |
| [openevidence-mcp](https://github.com/bakhtiersizhaev/openevidence-mcp) | Unofficial MCP server for OpenEvidence medical search through the user's browser session | 48 | 🟢 | TypeScript |
| [wechat-mcp](https://github.com/JettChenT/wechat-mcp) | MCP server for the WeChat desktop client | 47 | 🟡 | Python |
| [mobbin-mcp](https://github.com/pdcolandrea/mobbin-mcp) | Unofficial MCP for Mobbin's design library, no public API required | 46 | 🗄️ | TypeScript |
| [whatsapp-mcp-extended](https://github.com/FelixIsaac/whatsapp-mcp-extended) | Maintained WhatsApp MCP with 26 tools, webhooks and Docker | 42 | 🟢 | Go |
| [robinhood-mcp](https://github.com/verygoodplugins/robinhood-mcp) | Read-only MCP server for Robinhood portfolio research | 40 | 🟢 | Python |
| [tbank-mcp](https://github.com/icyberdeveloper/tbank-mcp) | Unofficial MCP server for T-Bank (Tinkoff) mobile banking private API | 38 | 🟢 | Python |
| [apple-photos-mcp](https://github.com/sweetrb/apple-photos-mcp) | MCP server querying and exporting the macOS Photos library database | 33 | 🟢 | JavaScript |
| [imessage-mcp (wyattjoh)](https://github.com/wyattjoh/imessage-mcp) | MCP server reading macOS iMessage chat.db | 29 | 🟢 | TypeScript |
| [imessage-mcp (anipotts)](https://github.com/anipottsbuilds/imessage-mcp) | Search and read Messages history from MCP clients | 28 | 🟢 | TypeScript |
| [signal-mcp](https://github.com/rymurr/signal-mcp) | MCP server for Signal messaging via signal-cli | 26 | 🟡 | Python |
| [wamcp](https://github.com/delltrak/wamcp) | WhatsApp MCP server with 61 tools over Baileys | 26 | 🟢 | TypeScript |
| [substack-mcp-plus](https://github.com/ty13r/substack-mcp-plus) | Unofficial Substack MCP server that posts and edits through the browser session | 25 | 🟢 | Python |
| [yandex-lavka-mcp](https://github.com/Dudude-bit/yandex-lavka-mcp) | Unofficial MCP server for ordering Yandex Lavka groceries | 25 | 🟢 | Python |
| [perplexity-web-wrapper](https://github.com/balakumardev/perplexity-web-wrapper) | Use a Perplexity subscription with MCP via a web wrapper | 23 | 🟢 | Python |
| [rm-mcp](https://github.com/wavyrai/rm-mcp) | MCP server for accessing reMarkable tablet data | 21 | 🟢 | Python |
| [Douyin-mcp](https://github.com/Lozzi1910/Douyin-mcp) | MCP server to search Douyin users and read/send direct messages | 20 | 🟢 | Python |
| [notebooklm-mcp (m4yk3ldev)](https://github.com/m4yk3ldev/notebooklm-mcp) | NotebookLM MCP with 32 tools for notebooks, sources and studio content | 20 | 🟢 | TypeScript |
| [wechat-mcp (lw396)](https://github.com/lw396/wechat-mcp) | WeChat chat MCP tool based on WeChatFerry hooking | 18 | 🟡 | Go |
| [twitter-mcp-server (gkydev)](https://github.com/gkydev/twitter-mcp-server) | Unofficial Twitter/X MCP server using cookie auth | 16 | 🟢 | Python |
| [stays](https://github.com/him229/stays) | Google Hotels MCP server and library via reverse-engineered batchexecute | 14 | 🟢 | Python |
| [garmin-mcp](https://github.com/davidmosiah/garmin-mcp) | Local-first MCP server for Garmin Body Battery, HRV, sleep and training data | 13 | 🟢 | TypeScript |
| [linkedin-mcp](https://github.com/devag7/linkedin-mcp) | Unofficial local LinkedIn MCP server for profile, job, company and inbox reads | 12 | 🟢 | TypeScript |
| [robinhood-cli-mcp-api](https://github.com/zaydiscold/robinhood-cli-mcp-api) | Unofficial Robinhood API map with CLI and MCP server | 11 | 🟢 | TypeScript |
| [instagram-dms-mcp](https://github.com/braindead-dev/instagram-dms-mcp) | MCP server for reading and sending Instagram DMs via the private API | 10 | 🟢 | Go |
| [threads-mcp-crawler](https://github.com/dkyazzentwatwa/threads-mcp-crawler) | MCP crawler extracting data from Meta Threads | 10 | 🟢 | Python |
| [104-mcp-server](https://github.com/a7512cs/104-mcp-server) | Unofficial MCP server for the 104.com.tw Taiwan job board | 8 | 🟢 | TypeScript |
| [cookunity-mcp](https://github.com/ggonzalezaleman/cookunity-mcp) | Unofficial MCP server for CookUnity meal delivery: menus, carts, orders and skips | 8 | 🟢 | TypeScript |
| [substack-mcp-plus](https://github.com/abanoub-ashraf/substack-mcp-plus) | Unofficial Substack MCP with publishing and analytics | 8 | 🟢 | Python |
| [MCP_Trenitalia](https://github.com/Fanfulla/MCP_Trenitalia) | Unofficial Trenitalia MCP using viaggiatreno endpoints | 7 | 🟢 | Python |
| [eight-sleep-mcp](https://github.com/davidmosiah/eight-sleep-mcp) | Unofficial MCP server for the Eight Sleep mobile-app API | 6 | 🟢 | TypeScript |
| [google-flow-mcp](https://github.com/ParkSangGwon/google-flow-mcp) | Unofficial MCP for Google Flow (Veo / Nano Banana) through your Chrome session | 6 | 🟢 | TypeScript |
| [perplexity-webui-mcp](https://github.com/Microck/perplexity-webui-mcp) | MCP server querying Perplexity Pro via WebUI session token | 5 | 🟢 | JavaScript |
| [sber-mcp](https://github.com/ex3lite/sber-mcp) | Unofficial MCP and async SDK for SberBank Online with browserless auth | 5 | 🟢 | Python |
| [notion-private-api-mcp](https://github.com/kirvigen/notion-private-api-mcp) | Notion MCP server via the private API (token_v2), no integration token | 4 | 🟢 | JavaScript |

## Other AI

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | Chinese localization patch for Claude Desktop on macOS, Windows and Linux | 7,920 | 🟢 | PowerShell |
| [claude-desktop-debian](https://github.com/aaddrick/claude-desktop-debian) | Repackages the Windows Claude Desktop app to run on Debian/Linux | 5,481 | 🟢 | Shell |
| [chatgpt-exporter](https://github.com/pionxzh/chatgpt-exporter) | Export ChatGPT conversation history from the web app | 2,827 | 🟢 | TypeScript |
| [Open Claude UI](https://github.com/Caho1/open-claude-ui) | React components and design-system notes derived from REA investigation of the Claude app UI | 1,401 | 🟢 | TypeScript |
| [convoviz](https://github.com/mohamed-chs/convoviz) | Converts ChatGPT export ZIPs into Markdown with media and usage visualizations | 888 | 🟢 | Python |
| [cc-desktop-switch](https://github.com/lonr-6/cc-desktop-switch) | Configures DeepSeek, Kimi, GLM and Bailian providers inside Claude Desktop | 800 | 🟢 | Python |
| [claude-desktop_win-zh_cn](https://github.com/Jyy1529/claude-desktop_win-zh_cn) | Claude Desktop Windows zh-CN patch translating keys and JS chunk labels | 675 | 🟢 | Python |
| [S3Tokenizer](https://github.com/xingchensong/S3Tokenizer) | Reverse engineered reimplementation of CosyVoice's supervised semantic speech tokenizer | 535 | 🟢 | Python |
| [open-claude-in-chrome](https://github.com/noemica-io/open-claude-in-chrome) | Reverse-engineered Claude in Chrome extension, open source for any Chromium browser | 257 | 🟢 | HTML |
| [claude-desktop-rtl-patch](https://github.com/shraga100/claude-desktop-rtl-patch) | CSS patch adding RTL support to Claude Desktop on Windows | 209 | 🟢 | PowerShell |
| [anthropic-tokenizer](https://github.com/javirandor/anthropic-tokenizer) | Approximates the Claude 3 tokenizer by inspecting the generation stream | 173 | 🟡 | Python |
| [claude-export](https://github.com/ryanschiang/claude-export) | Browser script to export Claude.ai chats to Markdown, JSON or PNG | 164 | 🟡 | JavaScript |
| [ModelLink](https://github.com/Win-Hao/ModelLink) | Local proxy routing third-party models through Claude Desktop | 142 | 🟢 | Rust |
| [Claude-Conversation-Exporter](https://github.com/socketteer/Claude-Conversation-Exporter) | Chrome extension for bulk-exporting Claude.ai conversations | 130 | 🟢 | JavaScript |
| [claude-chromium-native-messaging](https://github.com/stolot0mt0m/claude-chromium-native-messaging) | Makes Claude in Chrome's native messaging work in Brave, Arc, Vivaldi, Edge | 82 | 🟢 | Shell |
| [chatgpt-rtl](https://github.com/mmnaderi/chatgpt-rtl) | RTL and UI patcher for the ChatGPT desktop application | 60 | 🟢 | JavaScript |
| [grokipedia-api](https://github.com/jasonniebauer/grokipedia-api) | Unofficial API for xAI's Grokipedia | 50 | 🟢 | Python |
| [chatgpt_desktop_ubuntu](https://github.com/johnohhh1/chatgpt_desktop_ubuntu) | Repackages the ChatGPT Windows MSIX as an Ubuntu .deb | 9 | 🟢 | Shell |
| [Mnemos](https://github.com/foufouadi/Mnemos) | Reverse-engineered Claude Desktop's local storage to add persistent memory | 5 | 🟢 | C# |
| [claude-code-background](https://github.com/Henry-fan88/claude-code-background) | Offline reimplementation of the Claude desktop app's glyph-wind session background | 3 | 🟢 | HTML |

## System Prompt Leaks & Extractions

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Extracted system prompts and tool definitions for Cursor, Claude Code, Devin, Windsurf, Kiro, v0, Lovable and more | 144,236 | 🟢 |  |
| [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Archive of extracted system prompts from ChatGPT, Claude, Gemini, Grok and others, per vendor with history | 70,169 | 🟢 | Python |
| [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | Leaked system prompts and tool specs for ChatGPT, Claude, Gemini, Grok, Perplexity, Cursor, Lovable, Replit and others | 51,494 | 🟢 |  |
| [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts) | Collection of leaked system prompts from LLM-based services, with verifiable sources | 14,976 | 🟢 |  |
| [claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | Claude Code system prompt, builtin tool descriptions and sub-agent prompts extracted per release | 12,992 | 🟢 | JavaScript |
| [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt) | Collection of extracted GPT system prompts plus prompt injection / prompt leaking techniques | 10,819 | 🟢 | HTML |
| [awesome-ai-system-prompts](https://github.com/dontriskit/awesome-ai-system-prompts) | Curated collection of system prompts for top AI tools (v0, Manus, Claude Code, ChatGPT, Perplexity) | 6,263 | 🟢 | TypeScript |
| [system-prompts-and-models-of-ai-tools-chinese](https://github.com/IsHexx/system-prompts-and-models-of-ai-tools-chinese) | Chinese translation of extracted prompts from Cursor, Devin, VSCode Agent and other AI coding tools | 1,255 | 🟢 |  |
| [cc](https://github.com/kn1026/cc) | Extracted Claude Code system prompt | 715 | 🟡 |  |
| [CLAUDE-CODE-SYSTEM-PROMPT](https://github.com/elder-plinius/CLAUDE-CODE-SYSTEM-PROMPT) | Living document of the extracted Claude Code system prompt | 390 | 🟢 |  |
| [v0prompt](https://github.com/sharkqwy/v0prompt) | Extracted full system prompt of Vercel v0 | 304 | 🟡 |  |
| [Google-Gemini-System-Prompt](https://github.com/elder-plinius/Google-Gemini-System-Prompt) | Prompt leak of Google Gemini Pro (Bard version) system prompts, instructions and guidelines | 292 | 🟡 |  |
| [awesome-system-prompts (EliFuzz)](https://github.com/EliFuzz/awesome-system-prompts) | System prompts and tool definitions extracted from AI coding agents (Augment, Claude Code, Cursor, Devin, Kiro) | 281 | 🟢 | JavaScript |
| [awesome-system-prompts (langgptai)](https://github.com/langgptai/awesome-system-prompts) | System prompts of LLMs and AI products: DeepSeek, ChatGPT, Gemini, Grok, Qwen | 231 | 🟢 |  |
| [apple-intelligence-prompts](https://github.com/Explosion-Scratch/apple-intelligence-prompts) | Apple Intelligence system prompts extracted from macOS Sequoia | 221 | 🟡 | JavaScript |
| [claude-fable-5-system-prompt](https://github.com/KalarisLabs/claude-fable-5-system-prompt) | Extracted system prompt of Claude Fable 5 | 220 | 🟢 | Python |
| [leaked-system-prompts (YeeKal)](https://github.com/YeeKal/leaked-system-prompts) | Leaked system prompts for ChatGPT, Claude, Grok, Gemini, DeepSeek, Manus, v0, Lovable, Cursor | 183 | 🟢 | TypeScript |
| [LEAKHUB](https://github.com/elder-plinius/LEAKHUB) | Leaderboard and community hub for system prompt leaks | 182 | 🟢 | TypeScript |
| [claude-hidden-toolkit](https://github.com/N1-AI/claude-hidden-toolkit) | Reverse engineering of Claude.ai's internal tool definitions | 172 | 🟢 |  |
| [claude-code-system-prompts](https://github.com/lucas-flatwhite/claude-code-system-prompts) | Analysis and documentation of Claude Code's internal prompt architecture | 156 | 🟢 |  |
| [claude-code-system-prompt](https://github.com/matthew-lim-matthew-lim/claude-code-system-prompt) | Dump of the Claude Code system prompt | 155 | 🟡 |  |
| [GPTsSystemPrompts](https://github.com/0xAb1d/GPTsSystemPrompts) | Database of leaked system instructions for popular custom GPTs in the ChatGPT GPT store | 85 | 🟡 |  |
| [Grok-System-Prompt-Leak](https://github.com/elder-plinius/Grok-System-Prompt-Leak) | Extracted system prompt of xAI's Grok on X (Twitter) | 73 | 🟡 |  |
| [awesome-llm-system-prompts](https://github.com/ManuelSLemos/awesome-llm-system-prompts) | System prompts from major LLMs: official releases, leaks and reverse-engineered discoveries | 34 | 🟡 |  |
| [antigravity_prompts](https://github.com/tfriedel/antigravity_prompts) | Reverse-engineered prompts and analysis from Google Antigravity | 31 | 🟢 |  |
| [claude-system-prompt (zep-us)](https://github.com/zep-us/claude-system-prompt) | Reverse-engineered claude.ai and Claude Code system prompts validated against official ones | 18 | 🟢 | HTML |
| [claude-code-system-prompts](https://github.com/changjonathanc/claude-code-system-prompts) | Collection of Claude Code system prompts | 16 | 🟢 | JavaScript |
| [prompt-stash](https://github.com/maxockner/prompt-stash) | Cursor internal prompts extracted through MCP | 8 | 🟡 |  |
| [claude-code-playbook](https://github.com/acelest/claude-code-playbook) | Reverse-engineered Claude Code system prompts and prompt-building logic | 4 | 🟢 | TypeScript |
