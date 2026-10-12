# AI Tools & LLM Clients

[← All categories](../README.md) · 683 projects

- [AI Hardware & On-device Models](#ai-hardware--on-device-models) (45)
- [Chatbot Web APIs](#chatbot-web-apis) (174)
- [Chinese LLM Web APIs](#chinese-llm-web-apis) (48)
- [Coding Agents (Claude Code, Cursor, Copilot…)](#coding-agents-claude-code-cursor-copilot) (243)
- [Image/Audio/Video Gen APIs](#imageaudiovideo-gen-apis) (61)
- [MCP Servers for Private APIs](#mcp-servers-for-private-apis) (57)
- [Other AI](#other-ai) (26)
- [System Prompt Leaks & Extractions](#system-prompt-leaks--extractions) (29)

## AI Hardware & On-device Models

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| meta-glasses-api | Messenger browser extension acting as an unofficial API for Meta Ray-Ban glasses | 693 | <https://github.com/dcrebbin/meta-glasses-api> |
| riffado | Self-hosted transcription interface for Plaud Note recordings | 407 | <https://github.com/riffado/riffado> |
| reverse-engineering-gemma-3n | Reverse engineering of Google's Gemma 3n edge-optimized model architecture | 278 | <https://github.com/antimatter15/reverse-engineering-gemma-3n> |
| dot2api | Turns the OpenAI Dot device into an OpenAI- and Claude-compatible API | 201 | <https://github.com/Pluviobyte/dot2api> |
| even-g2-protocol (i-soxi) | Reverse-engineered BLE protocol of Even Realities G2 smart glasses | 189 | <https://github.com/i-soxi/even-g2-protocol> |
| TotalRecall | Extracts and displays data from Windows 11 Copilot+ Recall snapshots database | 167 | <https://github.com/xaitax/TotalRecall> |
| ANE-LM | LLM inference on the Apple Neural Engine | 144 | <https://github.com/johnmai-dev/ANE-LM> |
| rk3588-npu | Reverse engineering the Rockchip RK3588 NPU | 130 | <https://github.com/mtx512/rk3588-npu> |
| Orion | Local runtime for training and running small LLMs on the Apple Neural Engine | 129 | <https://github.com/mechramc/Orion> |
| applaud | n8n support and local sync for Plaud devices | 99 | <https://github.com/rsteckler/applaud> |
| v831-npu | Reverse engineering the Allwinner V831 NPU | 95 | <https://github.com/mtx512/v831-npu> |
| plaud-sync-for-obsidian | Obsidian plugin syncing Plaud recordings via reverse-engineered API | 89 | <https://github.com/leonardsellem/plaud-sync-for-obsidian> |
| codex-micro-4-core2 | Unofficial BLE Codex Micro firmware turning M5Stack Core2 into a ChatGPT Desktop controller | 78 | <https://github.com/imliubo/codex-micro-4-core2> |
| npunlock | Write and run custom C kernels on Intel Core Ultra NPUs | 67 | <https://github.com/hsfzxjy/npunlock> |
| rokid-docs | Community docs for Rokid AR glasses incl. YodaOS internals and reverse-engineered details | 51 | <https://github.com/buildwithfenna/rokid-docs> |
| plaud-toolkit | TypeScript library, CLI and MCP server for the Plaud API | 44 | <https://github.com/sergivalverde/plaud-toolkit> |
| mabl *(archived)* | Modular assistant replacing Humane's cloud assistant on the jailbroken Ai Pin | 41 | <https://github.com/PenumbraOS/mabl> |
| ane-infer | Apple Neural Engine LLM inference using reverse-engineered private APIs | 30 | <https://github.com/thebasedcapital/ane-infer> |
| omibutfree | Free alternative app for the Omi AI wearable | 29 | <https://github.com/kbdevs/omibutfree> |
| CodexMacro | Android BLE controller implementing ChatGPT Desktop's Codex Micro HID-over-GATT protocol | 20 | <https://github.com/Patchself/CodexMacro> |
| locus-tether | Self-hosted replacement for the Omi wearable's cloud pipeline | 17 | <https://github.com/thecloudcowboy/locus-tether> |
| tinycoral | tinygrad on Coral Edge TPU with reverse-engineered ISA and USB driver | 17 | <https://github.com/FrederikRogalski/tinycoral> |
| OpenPlod | Local-first Plaud Note Pro vault with direct Bluetooth import | 15 | <https://github.com/RemiPelloux/OpenPlod> |
| cppRecall | C++ dumper for Microsoft Recall database and screenshots | 14 | <https://github.com/otterpwn/cppRecall> |
| evenRealities-webflasher | Browser flasher and recovery console for Even Realities G2 and R1 | 14 | <https://github.com/AM-Guru/evenRealities-webflasher> |
| plaud-api | Unofficial Python client for Plaud AI recorders | 12 | <https://github.com/arbuzmell/plaud-api> |
| openplaudit | macOS app/CLI for PLAUD Note: BLE sync, Opus decode, Whisper | 11 | <https://github.com/mar-maradnus/openplaudit> |
| rabbit-r1-firmware | Rabbit R1 flashing guides, scripts and hardware docs (CipherOS, LK analysis) | 10 | <https://github.com/TurboTheTurtle/rabbit-r1-firmware> |
| ai-pin-interposer | Hardware interposer for Humane AI Pin debug access | 8 | <https://github.com/agg23/ai-pin-interposer> |
| humane-system-hook | Hooks Humane's Ai Pin software so it functions after the cloud shutdown | 8 | <https://github.com/PenumbraOS/humane-system-hook> |
| mic-rs | Downloads and decodes audio from Anker Soundcore Work and Plaud | 8 | <https://github.com/dariofinardi/mic-rs> |
| even-g2-patched | Patched Even app + frida-gadget routing G2 voice commands to a custom AI agent | 7 | <https://github.com/cokeeffekt/even-g2-patched> |
| luma | Self-hosted cloud and device runtime for an operator-owned Humane Ai Pin | 7 | <https://github.com/TheAndersMadsen/luma> |
| plaud-direct-pc-research | Direct-to-PC BLE interoperability research for PLAUD Note Pro/NotePin S | 7 | <https://github.com/Shawn-TKD/plaud-direct-pc-research> |
| even-g2-protocol (ithinkthisiscool) | Python implementation and protocol map of Even Realities G2 glasses | 6 | <https://github.com/ithinkthisiscool/even-g2-protocol> |
| unofficial-even-g2-local-assistant | Local-first assistant talking to Even Realities G2 over BLE | 6 | <https://github.com/marienbaptiste/unofficial-even-g2-local-assistant> |
| installer *(archived)* | Installer for the PenumbraOS platform on the Humane Ai Pin | 5 | <https://github.com/PenumbraOS/installer> |
| interposer | USB interposer hardware for accessing the Humane Ai Pin | 5 | <https://github.com/PenumbraOS/interposer> |
| rabbit-r1-hooks | Impersonates an OpenClaw gateway so a Rabbit R1 can drive Claude Code/Codex | 5 | <https://github.com/sarkarsaurabh27/rabbit-r1-hooks> |
| openrabbit | Clean-room Rabbit R1 node client bridging to agents | 4 | <https://github.com/vcruz305/openrabbit> |
| plaud (danielgwilson) | Agent-first CLI to export and download Plaud recordings | 4 | <https://github.com/danielgwilson/plaud> |
| Even-G2-RE | Reverse engineering the Even G2 app and BLE system | 3 | <https://github.com/lonelyobserver0/Even-G2-RE> |
| g2-r1-re-tools-and-guide | RE tools and guides for Even G2 glasses and R1 health ring | 3 | <https://github.com/Commute773/g2-r1-re-tools-and-guide> |
| plaude-cli | Offline CLI for the Plaud Note voice recorder, no cloud or app | 3 | <https://github.com/Sumatoshi-tech/plaude-cli> |
| r1tool | CLI for hole.rabbit.tech: export Rabbit R1 photos and journal | 3 | <https://github.com/nesdeq/r1tool> |

## Chatbot Web APIs

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| gpt4free | Reverse-engineered third-party provider APIs giving free access to GPT-4 and other LLMs | 66,802 | <https://github.com/xtekky/gpt4free> |
| ChatGPT (revChatGPT) *(archived)* | Reverse engineered ChatGPT web API client in Python (archived) | 27,900 | <https://github.com/acheong08/ChatGPT> |
| EdgeGPT *(archived)* | Reverse engineered API of Microsoft's Bing Chat (Sydney) AI | 7,831 | <https://github.com/acheong08/EdgeGPT> |
| grok2api | Multi-account API gateway for Grok Web, Grok Build and Grok Console | 7,805 | <https://github.com/chenyme/grok2api> |
| gpt4free-ts | TypeScript replication of gpt4free reverse-engineered free GPT-4 provider API | 7,657 | <https://github.com/xiangsx/gpt4free-ts> |
| chatgpt2api (basketikun) | Pure-protocol reverse implementation of ChatGPT web incl. GPT-Image-2, OpenAI-compatible | 6,592 | <https://github.com/basketikun/chatgpt2api> |
| openclaw-zero-token | OpenClaw using Claude/ChatGPT/Gemini/DeepSeek/Doubao web sessions, no API token | 5,201 | <https://github.com/linuxhsj/openclaw-zero-token> |
| Bard-API *(archived)* | Unofficial Python package returning Google Bard responses via cookie value | 5,164 | <https://github.com/dsdanielpark/Bard-API> |
| PyChatGPT | Python client for the unofficial ChatGPT web API | 4,183 | <https://github.com/rawandahmad698/PyChatGPT> |
| node-chatgpt-api | Node.js client for ChatGPT and Bing AI with reverse-engineered endpoints | 4,149 | <https://github.com/waylaidwanderer/node-chatgpt-api> |
| chat2api | Converts ChatGPT web into OpenAI API format | 3,835 | <https://github.com/lanqian528/chat2api> |
| Gemini-API | Reverse-engineered async Python API for the Google Gemini web app | 3,572 | <https://github.com/HanaokaYuzu/Gemini-API> |
| gemini-web2api | Converts Google Gemini web into an OpenAI-compatible API | 3,405 | <https://github.com/Sophomoresty/gemini-web2api> |
| FreeGPT35 *(archived)* | Free GPT-3.5 API from the login-free ChatGPT web | 3,213 | <https://github.com/missuo/FreeGPT35> |
| aurora | Free ChatGPT API from the login-free ChatGPT web | 2,564 | <https://github.com/aurora-develop/aurora> |
| poe-api *(archived)* | Reverse engineered Python API wrapper for Quora's Poe (unmaintained) | 2,461 | <https://github.com/ading2210/poe-api> |
| perplexity-ai | Unofficial API wrapper for the Perplexity.ai web interface | 1,971 | <https://github.com/helallao/perplexity-ai> |
| grok2api | Grok web to OpenAI-compatible API proxy | 1,876 | <https://github.com/jiujiu532/grok2api> |
| ninja *(archived)* | Reverse engineered ChatGPT web proxy (Rust) | 1,674 | <https://github.com/0x676e67/ninja> |
| ChatGPT-Mirror | Self-hosted ChatGPT web mirror site | 1,405 | <https://github.com/dairoot/ChatGPT-Mirror> |
| Bard *(archived)* | Python SDK for reverse engineered Google Bard | 1,390 | <https://github.com/acheong08/Bard> |
| WebAI-to-API | Exposes web chat UIs (Gemini, etc.) as an API | 1,390 | <https://github.com/Amm1rr/WebAI-to-API> |
| pyChatGPT *(archived)* | Unofficial Python wrapper for ChatGPT web via browser session | 1,336 | <https://github.com/terry3041/pyChatGPT> |
| clewdr | High-performance Claude.ai web and Claude Code reverse proxy (Rust) | 1,281 | <https://github.com/Xerxes-2/clewdr> |
| PandoraNext-TokensTool *(archived)* | Manages and refreshes PandoraNext ChatGPT web tokens to run a free OpenAI-style relay | 1,276 | <https://github.com/Yanyutin753/PandoraNext-TokensTool> |
| Windows-Copilot-API | Reverse engineered Windows (Microsoft) Copilot into an OpenAI-compatible REST API | 1,250 | <https://github.com/sums001/Windows-Copilot-API> |
| bing-chat *(archived)* | Reverse-engineered Bing AI Chat Node.js client | 1,205 | <https://github.com/transitive-bullshit/bing-chat> |
| Proxima | MCP server driving ChatGPT, Claude, Gemini and Perplexity web sessions without API keys | 1,194 | <https://github.com/Zen4-bit/Proxima> |
| ChatGPT-to-API *(archived)* | Go proxy turning the ChatGPT website into an OpenAI-compatible API | 1,138 | <https://github.com/acheong08/ChatGPT-to-API> |
| poe-api-wrapper *(archived)* | Python API wrapper for Poe.com web giving access to GPT-4, Claude, Gemini and more | 1,092 | <https://github.com/snowby666/poe-api-wrapper> |
| hugging-chat-api *(archived)* | Unofficial Python API for HuggingChat web | 938 | <https://github.com/Soulter/hugging-chat-api> |
| free-one-api | Manages reverse-engineered LLM web APIs (ChatGPT, Bard, Claude, HuggingChat, Qwen) behind an OpenAI API | 918 | <https://github.com/RockChinQ/free-one-api> |
| Claude-API | Unofficial Python API for claude.ai web using session cookie | 914 | <https://github.com/KoushikNavuluri/Claude-API> |
| Grok-Mirror | Self-hosted Grok web mirror via reverse proxy | 914 | <https://github.com/dairoot/Grok-Mirror> |
| SydneyQt | Desktop client for jailbroken Bing AI / Copilot (Sydney) via its reverse engineered API | 874 | <https://github.com/juzeon/SydneyQt> |
| ds-free-api | DeepSeek web API proxy with OpenAI and Anthropic compatible interfaces | 802 | <https://github.com/NIyueeE/ds-free-api> |
| claude-unofficial-api | Unofficial API client and CLI for Claude via the claude.ai web interface | 742 | <https://github.com/Explosion-Scratch/claude-unofficial-api> |
| chat2api | ChatGPT web to API converter | 716 | <https://github.com/aurorax-neo/chat2api> |
| Gemini-FastAPI | Web-based Gemini wrapped into an OpenAI-compatible API | 710 | <https://github.com/Nativu5/Gemini-FastAPI> |
| grok2api | Grok2API on Cloudflare Workers | 708 | <https://github.com/TQZHR/grok2api> |
| unofficial-chatgpt-api | Unofficial ChatGPT API via browser automation | 700 | <https://github.com/taranjeet/unofficial-chatgpt-api> |
| web2api | Turns web AI chat interfaces (e.g. Claude) into APIs | 651 | <https://github.com/caiwuu/web2api> |
| claude2api | Turns Claude.ai web into an API with image recognition and file upload | 642 | <https://github.com/yushangxiao/claude2api> |
| everything-chatgpt | Documents the ChatGPT web app internals and its backend-api calls | 593 | <https://github.com/terminalcommandnewsletter/everything-chatgpt> |
| react-native-chatgpt | Reverse-engineered ChatGPT web to provide a React Native wrapper | 584 | <https://github.com/rgommezz/react-native-chatgpt> |
| grok2api_python | Python Grok web to OpenAI API proxy | 572 | <https://github.com/xLmiler/grok2api_python> |
| M365-Copilot2API | Microsoft 365 Copilot exposed as an OpenAI/Anthropic-compatible API gateway | 553 | <https://github.com/HEXUXIU/M365-Copilot2API> |
| grok3-api *(archived)* | Unofficial Python client for Grok 3 reverse-engineering grok.com browser requests | 543 | <https://github.com/mem0ai/grok3-api> |
| CharacterAI (kramcat) | Unofficial Python API for character.ai using direct HTTP requests | 542 | <https://github.com/kramcat/CharacterAI> |
| gemini-web-to-api | Reverse-engineered Gemini web app API usable as an OpenAI/Gemini/Claude API key | 512 | <https://github.com/ntthanh2603/gemini-web-to-api> |
| gemini-web2api-go | Self-hosted OpenAI-compatible API proxying Gemini web | 512 | <https://github.com/zexadev/gemini-web2api-go> |
| business2api | OpenAI/Gemini-compatible proxy for the Gemini Business web API | 497 | <https://github.com/XxxXTeam/business2api> |
| poe-openai-proxy | Exposes the reverse-engineered poe-api library as an OpenAI-compatible API | 455 | <https://github.com/juzeon/poe-openai-proxy> |
| GoogleBard | Reverse engineered Google Bard API for Node.js | 419 | <https://github.com/PawanOsman/GoogleBard> |
| meta-ai-api | Reverse engineered Meta AI (Llama 3) web chat API | 409 | <https://github.com/Strvm/meta-ai-api> |
| Gemi2Api-Server | Server built on the reverse-engineered Gemini-API web client | 405 | <https://github.com/zhiyu1998/Gemi2Api-Server> |
| webchat2api | Self-hosted proxy unifying ChatGPT, Grok and Gemini web sessions into OpenAI API | 392 | <https://github.com/zqbxdev/webchat2api> |
| deepseek4free | DeepSeek private web chat API with reversed proof-of-work challenge | 386 | <https://github.com/xtekky/deepseek4free> |
| node_characterai | Unofficial Character.AI wrapper for Node.js | 376 | <https://github.com/realcoloride/node_characterai> |
| llm4free | Python toolkit for free LLM web providers and search | 371 | <https://github.com/OEvortex/llm4free> |
| FreeQwenApi | Local API proxy for Qwen AI web chat with session management | 333 | <https://github.com/y13sint/FreeQwenApi> |
| Claude2-PyAPI | Python API for Claude.ai web sessions, chat, attachments and history | 319 | <https://github.com/wwwzhouhui/Claude2-PyAPI> |
| Grok-Api | Python wrapper and FastAPI server for the Grok web interface (discontinued) | 316 | <https://github.com/realasfngl/Grok-Api> |
| Deepseek-API | Reverse engineered DeepSeek chat into an OpenAI-compatible REST API | 308 | <https://github.com/sums001/Deepseek-API> |
| Poe | Reverse engineered API for Quora's Poe chatbot service | 304 | <https://github.com/vaibhavk97/Poe> |
| reverse-engineered-chatgpt *(archived)* | Unofficial reverse-engineered ChatGPT web API in Python | 293 | <https://github.com/Zai-Kun/reverse-engineered-chatgpt> |
| sydney.py *(archived)* | Python client for Microsoft Copilot (Bing Chat / Sydney) web | 292 | <https://github.com/vsakkas/sydney.py> |
| perplexityai | Python API for perplexity.ai web | 288 | <https://github.com/nathanrchn/perplexityai> |
| doubao2api | Reverse-engineered Doubao API as OpenAI-compatible REST service incl. image/video generation | 277 | <https://github.com/wangchuxiaoji-oss/doubao2api> |
| yuanbao-free-api | Access Tencent Yuanbao web chat through an OpenAI-compatible interface | 275 | <https://github.com/chenwr727/yuanbao-free-api> |
| refresh-gpt-chat | Relay for ChatGPT web v1 APIs using refresh tokens as keys | 244 | <https://github.com/Yanyutin753/refresh-gpt-chat> |
| cpp-freegpt-webui *(archived)* | C++ web UI and server using free reverse-engineered GPT providers | 236 | <https://github.com/fantasy-peak/cpp-freegpt-webui> |
| notebooklm-client | NotebookLM CLI/library via reverse-engineered Boq RPC, incl. audio podcasts | 227 | <https://github.com/icebear0828/notebooklm-client> |
| doubao-free-api | Reverse-engineered ByteDance Doubao chat API with search and image generation | 222 | <https://github.com/Bitsea1/doubao-free-api> |
| chat2api *(archived)* | ChatGPT web interface to API conversion gateway | 218 | <https://github.com/xyhelper/chat2api> |
| bing-chat-sidebar-for-chrome | Edge's Bing AI sidebar reverse engineered for Chrome | 213 | <https://github.com/wong2/bing-chat-sidebar-for-chrome> |
| Gemini-API *(archived)* | Unofficial Python package returning Google Gemini web responses via cookies | 208 | <https://github.com/dsdanielpark/Gemini-API> |
| revLibs | Reverse-engineering library plugin for ChatGPT, Claude, Bard and gpt4free in QQ bots | 200 | <https://github.com/RockChinQ/revLibs> |
| intense-rp-next *(archived)* | Desktop app and OpenAI-compatible API proxying LLM web UIs | 199 | <https://github.com/LyubomirT/intense-rp-next> |
| vercel-llm-api | Reverse engineered Python wrapper for the Vercel AI Playground | 188 | <https://github.com/ading2210/vercel-llm-api> |
| gpt4-openai-api | Unofficial Python access to GPT-4 through chat.openai.com, works with LangChain | 184 | <https://github.com/Erol444/gpt4-openai-api> |
| chatbang | CLI to use ChatGPT from the terminal without an API key via the web app | 181 | <https://github.com/ahmedhosssam/chatbang> |
| grok2api-rs | Rust rewrite of Grok2API | 179 | <https://github.com/XeanYu/grok2api-rs> |
| python-tgpt | Terminal AI chat and REST API using free LLM web providers | 177 | <https://github.com/Simatwa/python-tgpt> |
| CatDesk | Uses ChatGPT web chat as a local coding agent | 173 | <https://github.com/Xeift/CatDesk> |
| bingchat-api *(archived)* | Unofficial Bing Chat API | 157 | <https://github.com/tuhinpal/bingchat-api> |
| ReEdgeGPT *(archived)* | Maintained reverse-engineered Microsoft Bing Chat / Copilot API | 155 | <https://github.com/Integration-Automation/ReEdgeGPT> |
| claude2api-deploy | Claude.ai web to API proxy | 154 | <https://github.com/realnoob007/claude2api-deploy> |
| EdgeGPT-Go | Go port of the reverse engineered Bing Chat API with gRPC and CLI | 151 | <https://github.com/pavel-one/EdgeGPT-Go> |
| grok2api | Grok web to OpenAI API reverse proxy | 151 | <https://github.com/aurora-develop/grok2api> |
| GPT_scraper | Scrapes full ChatGPT user history through the hidden frontend backend API | 138 | <https://github.com/rodolflying/GPT_scraper> |
| llm-web-api | Converts the ChatGPT web page into an API | 137 | <https://github.com/adryfish/llm-web-api> |
| perplexity-webui-scraper | Python client, MCP server and REST API for Perplexity web UI | 136 | <https://github.com/henrique-coder/perplexity-webui-scraper> |
| grok2api_new | Grok web reverse proxy to OpenAI API with multi-account pooling | 135 | <https://github.com/Tomiya233/grok2api_new> |
| claude2api | Go Claude.ai web to API gateway with account pool and web mirror | 131 | <https://github.com/basketikun/claude2api> |
| WebChatGPT | Python SDK for the ChatGPT web version | 124 | <https://github.com/Simatwa/WebChatGPT> |
| grok2api | Rewrite of Grok2API reverse proxy | 122 | <https://github.com/VeroFess/grok2api> |
| gpt4free.js | JavaScript port of gpt4free reverse-engineered providers | 115 | <https://github.com/zachey01/gpt4free.js> |
| poe *(archived)* | Reverse engineered API for Quora Poe | 115 | <https://github.com/muharamdani/poe> |
| ChatGPT-PHP *(archived)* | PHP SDK for ChatGPT with reverse engineered web API support | 112 | <https://github.com/tnborg/ChatGPT-PHP> |
| ChatGPT | API wrapper for using ChatGPT web for free without paid API | 111 | <https://github.com/realasfngl/ChatGPT> |
| duck_chat | Reverse engineered DuckDuckGo AI Chat API client | 111 | <https://github.com/mrgick/duck_chat> |
| gemini2api | Gemini web to OpenAI/Claude/Gemini-compatible API via browser cookies | 105 | <https://github.com/xwteam/gemini2api> |
| m365-copilot-bridge | Microsoft 365 Copilot to OpenAI-compatible API gateway | 105 | <https://github.com/shenping1200/m365-copilot-bridge> |
| chatgpt-java | Java library for ChatGPT via the reverse engineered web API | 104 | <https://github.com/arctisio/chatgpt-java> |
| LMarenaBridge | Desktop app exposing LMArena.ai models as an OpenAI-compatible API | 103 | <https://github.com/jtostrings/LMarenaBridge> |
| PyCharacterAI | Unofficial Python API wrapper for character.ai | 97 | <https://github.com/Xtr4F/PyCharacterAI> |
| WebModel | Use major AI models through their web sessions without API tokens | 97 | <https://github.com/linuxhsj/WebModel> |
| metaai-api | FastAPI wrapper for Meta AI chat, image and video generation via cookies | 96 | <https://github.com/mir-ashiq/metaai-api> |
| Bing-Chat-API | Unofficial API for Bing Chat (GPT-4) | 91 | <https://github.com/Agora-Lab-AI/Bing-Chat-API> |
| ProGPT | Reverse engineered Python client for ChatGPT web conversations | 90 | <https://github.com/diezo/ProGPT> |
| notebooklm-rest-api | REST API wrapper for Google NotebookLM built on notebooklm-py | 89 | <https://github.com/gnh1201/notebooklm-rest-api> |
| Gemini-Link-System | Gateway converting Gemini Business API to OpenAI-compatible interface | 87 | <https://github.com/qxd-ljy/Gemini-Link-System> |
| Google-Bard *(archived)* | Java library for the reverse engineered Google Bard API | 86 | <https://github.com/LarryDpk/Google-Bard> |
| ChatGPTReversed | Free ChatGPT API reversed from the web client | 85 | <https://github.com/gin337/ChatGPTReversed> |
| NChatGPTRev *(archived)* | C# ChatGPT SDK using the reverse engineered web API | 84 | <https://github.com/BruceQiu1996/NChatGPTRev> |
| edgegpt *(archived)* | Reverse engineering of the new Bing chat feature (Node.js) | 77 | <https://github.com/KeJunMao/edgegpt> |
| apibeam | Converts a ChatGPT or Claude web account into an API | 76 | <https://github.com/NiteshSingh17/apibeam> |
| chatgpt-web-voice | Reverse-engineered ChatGPT.com web voice (realtime WebRTC + DataChannel) protocol | 76 | <https://github.com/dyhhhhhh/chatgpt-web-voice> |
| unofficial-chatgpt-api | Node.js client for the ChatGPT web API | 76 | <https://github.com/abacaj/unofficial-chatgpt-api> |
| openplayground-api *(archived)* | Reverse engineered Python wrapper for OpenPlayground (nat.dev) | 74 | <https://github.com/ading2210/openplayground-api> |
| Claude2api | Claude.ai web to API proxy | 69 | <https://github.com/aurora-develop/Claude2api> |
| PoeAPI | Self-hostable reverse engineered Poe.com API | 69 | <https://github.com/aspekts/PoeAPI> |
| m365-copilot-openai-proxy | Local proxy exposing Microsoft 365 Copilot as an OpenAI-compatible API | 65 | <https://github.com/kuchris/m365-copilot-openai-proxy> |
| DuckDuckGo-AI | DuckDuckGo AI chat reverse engineered API on Cloudflare Workers | 64 | <https://github.com/HuggingBear/DuckDuckGo-AI> |
| GLM-Free-API | Reverse-engineered Zhipu ChatGLM web API with streaming and agent support | 63 | <https://github.com/xiaoY233/GLM-Free-API> |
| gemini-webapi-mcp | MCP server for Gemini web via browser cookies (chat and image generation) | 59 | <https://github.com/AndyShaman/gemini-webapi-mcp> |
| Grok3API | Async Python client for the Grok mobile private gRPC API | 59 | <https://github.com/boykopovar/Grok3API> |
| node-character.ai *(archived)* | Unofficial API wrapper for Character.AI | 58 | <https://github.com/RichardDorian/node-character.ai> |
| CAINode | Lightweight unofficial Character.AI API for Node.js, Deno and Bun | 57 | <https://github.com/KevinAdhaikal/CAINode> |
| chat2api | Simple framework for reversing web chat services into APIs | 57 | <https://github.com/qy527145/chat2api> |
| cto | Proxies cto.new chat into OpenAI ChatCompletion format | 57 | <https://github.com/Luotianyi-0712/cto> |
| Gemini-1.5-Pro AI Studio Reverse Engineered API | Reverse engineered Google AI Studio endpoint for Gemini 1.5 Pro | 57 | <https://github.com/SreejanPersonal/Gemini-1.5-Pro-Google-AI-Studio-Reverse-Engineered-API> |
| geminiweb2api | OpenAI-compatible proxy for the Gemini web app | 55 | <https://github.com/XxxXTeam/geminiweb2api> |
| LlM-Api-Open | Unofficial open APIs for ChatGPT and Microsoft Copilot with self-hosting | 44 | <https://github.com/F33RNI/LlM-Api-Open> |
| pi-oracle | ChatGPT and Grok web-session oracle extension for the Pi agent | 39 | <https://github.com/fitchmultz/pi-oracle> |
| Gemini-Chat-API | Unofficial API for interacting with Google Gemini web chat | 38 | <https://github.com/OEvortex/Gemini-Chat-API> |
| claude-ai-re-client | CLI client built on Claude.ai's reverse-engineered HTTPS completion API | 37 | <https://github.com/Adithyan-Defender/claude-ai-re-client> |
| CLOVA-X | Unofficial API for Naver CLOVA X | 37 | <https://github.com/mirusu400/CLOVA-X> |
| pi-perplexity | Pi extension searching via your Perplexity Pro/Max web subscription | 32 | <https://github.com/ivanrvpereira/pi-perplexity> |
| grok2api | FastAPI Grok2API compatible with OpenAI calls | 31 | <https://github.com/sodikinnaa/grok2api> |
| MetaAI-Free-Hermes-Agent | Runs Meta AI's web model in Hermes Agent without API keys | 30 | <https://github.com/compnew2006/MetaAI-Free-Hermes-Agent> |
| Perplexity-Reverse-Engineered-API | Reverse-engineered Perplexity API client in Python over WebSocket | 28 | <https://github.com/SreejanPersonal/Perplexity-Reverse-Engineered-API> |
| grok2api-pro | Grok web to OpenAI-style API with image/video generation and account pool | 27 | <https://github.com/miuzhaii/grok2api-pro> |
| chatgptproxy | ChatGPT web to OpenAI API proxy with Sentinel PoW solver | 25 | <https://github.com/acruz6421-bot/chatgptproxy> |
| gemini-claude-web2api | OpenAI-compatible proxy for Gemini and Claude web APIs via cookie auth | 24 | <https://github.com/cyberanrhy/gemini-claude-web2api> |
| prism2api | Reverse-engineered Python API for prism.openai.com | 24 | <https://github.com/Robinfxa/prism2api> |
| Gemini-Reverse | Unofficial Node.js client for gemini.google.com | 23 | <https://github.com/rynn-k/Gemini-Reverse> |
| EdgeGPT *(archived)* | Bing AI chatbot WebSocket API wrapper for PHP | 22 | <https://github.com/IhsanDevs/EdgeGPT> |
| grokforge | Go rewrite of grok2api (Grok web to API) | 22 | <https://github.com/crmmc/grokforge> |
| EdgeGPTJs | Node.js port of the reverse-engineered EdgeGPT Bing Chat API | 21 | <https://github.com/lonelam/EdgeGPTJs> |
| node_perplexityai | Unofficial Node.js API based on the Perplexity.AI website and mobile app | 21 | <https://github.com/Parking-Master/node_perplexityai> |
| chatgpt-export (hoya98) | Bulk-export all ChatGPT conversations incl. Team/Business workspaces via backend API | 20 | <https://github.com/hoya98/chatgpt-export> |
| chatgpt-turnstile-reversed | Reverse engineered ChatGPT Turnstile anti-bot token used for login and chat | 18 | <https://github.com/jonathanyly/chatgpt-turnstile-reversed> |
| muse-client | Unofficial TypeScript SDK for Muse chat using the Muse Gadget SDK protocol | 17 | <https://github.com/wong2/muse-client> |
| chatgpt-exporter (ezwep) | Self-hosted backup of ChatGPT conversations, projects and custom GPTs | 16 | <https://github.com/ezwep/chatgpt-exporter> |
| Go-EdgeGPT | Go reverse-engineered API of Microsoft's Bing Chat | 16 | <https://github.com/billikeu/Go-EdgeGPT> |
| Discord-C.AI-Wrapper | Brings Character.AI personas into Discord via the unofficial API | 15 | <https://github.com/walterwhite-69/Discord-C.AI-Wrapper> |
| grok-web-api | Lightweight proxy for the grok.com web API | 15 | <https://github.com/imjustprism/grok-web-api> |
| huggingchat-api *(archived)* | HuggingChat web API client with streaming and web search | 15 | <https://github.com/ogios/huggingchat-api> |
| SydneyGPT | Sydney persona decorator for the reverse-engineered EdgeGPT API | 15 | <https://github.com/rafaelcalleja/SydneyGPT> |
| chatgptAPI_unof | Unofficial ChatGPT web API client | 14 | <https://github.com/0xMesto/chatgptAPI_unof> |
| gemini-free-api | Reverse-engineered Gemini web interface as a streaming API with tools | 14 | <https://github.com/XD06/gemini-free-api> |
| UnofficialClaude | Unofficial Claude web API with OpenAI-like structure | 14 | <https://github.com/0xMesto/UnofficialClaude> |
| Claude-API (cyber-wojtek) | Reverse-engineered Python wrapper for the Claude web app | 13 | <https://github.com/cyber-wojtek/Claude-API> |
| chatgpt-exporter (thiscantbeserious) | Exports ChatGPT Business account data via the web backend | 12 | <https://github.com/thiscantbeserious/chatgpt-exporter> |
| reverse-chatgpt | Reverse-engineered ChatGPT web interface with streaming automation API | 12 | <https://github.com/s5treak/reverse-chatgpt> |
| genspark-py | Unofficial Python client for Genspark.ai login and streaming chat | 9 | <https://github.com/SharpWizard/genspark-py> |
| grok-web-to-api | OpenAI-compatible proxy for grok.com web sessions | 9 | <https://github.com/Agelakz/grok-web-to-api> |
| gemini-web-api (qutek) | OpenAI-compatible proxy and Node.js SDK for the Gemini web app | 6 | <https://github.com/qutek/gemini-web-api> |
| genspark-gateway | OpenAI-compatible proxy for the Genspark.ai web session | 6 | <https://github.com/chnd372/genspark-gateway> |
| node_characterai-2.0 | Unofficial Character.AI wrapper for Node | 6 | <https://github.com/Skidy89/node_characterai-2.0> |
| chatgpt2api-cf | Cloudflare Workers gateway reverse-engineered from the anonymous ChatGPT Android API | 5 | <https://github.com/6Kmfi6HP/chatgpt2api-cf> |
| gemini-web-api (FarisHijazi) | OpenAI-compatible API over gemini.google.com including images and Veo video | 5 | <https://github.com/FarisHijazi/gemini-web-api> |

## Chinese LLM Web APIs

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| Chat2API | Zero-cost access to GLM, Kimi, Qwen and other models via their official web UIs | 1,695 | <https://github.com/xiaoY233/Chat2API> |
| qwen2API | Converts the Qwen web chat into an API | 965 | <https://github.com/YuJunZhiXue/qwen2API> |
| Qwen2API | QwenLM web chat to OpenAI-compatible API | 835 | <https://github.com/Rfym21/Qwen2API> |
| deepseek2api *(archived)* | DeepSeek web reverse API | 632 | <https://github.com/iidamie/deepseek2api> |
| DeeperSeek | Unofficial Python wrapper for the DeepSeek web chat | 311 | <https://github.com/theAbdoSabbagh/DeeperSeek> |
| deepseek-free-api | Converts chat.deepseek.com web chat into OpenAI and Anthropic compatible APIs | 307 | <https://github.com/Fly143/deepseek-free-api> |
| doubao-2api | Doubao web to API with Playwright a_bogus signature reversing | 286 | <https://github.com/lza6/doubao-2api> |
| kimi2api | Kimi web chat reverse proxy with OpenAI-compatible interface | 247 | <https://github.com/chopper1026/kimi2api> |
| deepseek-web2api-free | FastAPI reverse proxy turning DeepSeek web chat into OpenAI-compatible API | 174 | <https://github.com/snake-aabb-wtf/deepseek-web2api-free> |
| 2025doubao-free-api | Doubao web reverse API | 170 | <https://github.com/1994qrq/2025doubao-free-api> |
| qwen2api | Proxy converting Qwen Chat to an OpenAI-compatible API | 168 | <https://github.com/smanx/qwen2api> |
| Z.ai2api *(archived)* | Proxies Z.ai (GLM) chat into OpenAI/Anthropic-compatible format without tokens | 153 | <https://github.com/hmjz100/Z.ai2api> |
| GLM-Free-API | OpenAI-compatible API proxy for chat.z.ai (GLM) web | 141 | <https://github.com/izaart95-jpg/GLM-Free-API> |
| glm2api | Converts chatglm.com web into a standard OpenAI API | 128 | <https://github.com/XxxXTeam/glm2api> |
| deepseek2api | DeepSeek web to API proxy | 123 | <https://github.com/TQZHR/deepseek2api> |
| zai2api | Proxy converting Z.AI chat into an OpenAI-compatible API | 116 | <https://github.com/XxxXTeam/zai2api> |
| doubao2API (robinxplorer) | Converts the Doubao web chat into an OpenAI-compatible API | 109 | <https://github.com/robinxplorer/doubao2API> |
| yuanbao-chat2api | Tencent Yuanbao web chat reverse-engineered to an OpenAI-style API | 100 | <https://github.com/juzeon/yuanbao-chat2api> |
| Qwen2API_Go | Go service converting Qwen.AI web into an API | 91 | <https://github.com/XxxXTeam/Qwen2API_Go> |
| DoubaoFreeApi *(archived)* | Lightweight Doubao web API proxy | 90 | <https://github.com/XilyFeAAAA/DoubaoFreeApi> |
| qwen-api | Qwen web API proxy with OpenAI-compatible chat, image and video endpoints | 89 | <https://github.com/encryptarun/qwen-api> |
| deepseek-api *(archived)* | Unofficial API wrapper for chat.deepseek.com | 81 | <https://github.com/rabilrbl/deepseek-api> |
| revTongYi | Reverse engineered Python API for Alibaba Tongyi Qianwen and Wanxiang | 72 | <https://github.com/leeeduke/revTongYi> |
| kimi2api | Kimi web to API proxy | 63 | <https://github.com/XxxXTeam/kimi2api> |
| Kimi-Free-API | Kimi web reverse API (successor to LLM-Red-Team kimi-free-api) | 61 | <https://github.com/xiaoY233/Kimi-Free-API> |
| Qwen-Free-API | Qwen web reverse API (successor to LLM-Red-Team qwen-free-api) | 53 | <https://github.com/xiaoY233/Qwen-Free-API> |
| qwen2api-rs | Rust qwen2API gateway disguising Qwen Web as OpenAI/Anthropic/Gemini APIs | 51 | <https://github.com/123hi123/qwen2api-rs> |
| qwen2api (map-A) | chat.qwen.ai web to OpenAI API | 38 | <https://github.com/map-A/qwen2api> |
| doubao-free-api | Wraps the Doubao desktop client as an OpenAI-compatible API | 34 | <https://github.com/5201213/doubao-free-api> |
| doubao2API (HongYan789) | Reverse-engineered Doubao web API gateway | 34 | <https://github.com/HongYan789/doubao2API> |
| DeepSeek-API-Unofficial-v2 | Unofficial reverse-engineered API for DeepSeek Chat and Coder | 32 | <https://github.com/SreejanPersonal/DeepSeek-API-Unofficial-v2> |
| deepseek-web-api | Unofficial local OpenAI-compatible API for DeepSeek web sessions | 30 | <https://github.com/kittors/deepseek-web-api> |
| KimiFreeAPI | OpenAI-compatible free API for Kimi web | 29 | <https://github.com/izaart95-jpg/KimiFreeAPI> |
| qwen-free-api | Go bridge exposing chat.qwen.ai as OpenAI and Anthropic APIs | 28 | <https://github.com/Godde3s/qwen-free-api> |
| qwen-free-api-worker | Cloudflare Worker exposing chat.qwenlm.ai as an OpenAI-compatible API | 28 | <https://github.com/aigem/qwen-free-api-worker> |
| zai-openai-proxy | chat.z.ai reverse-engineered OpenAI-compatible proxy with thinking and tools | 27 | <https://github.com/xaoLiu1222/zai-openai-proxy> |
| deepseek-free-api | OpenAI-compatible free API via DeepSeek web | 21 | <https://github.com/Ametist298/deepseek-free-api> |
| doubao2api (SeiShonagon520) | OpenAI-compatible service rebuilt on the latest Doubao web client | 21 | <https://github.com/SeiShonagon520/doubao2api> |
| minimax2api (juangchuank-ops) | MiniMax Agent reverse gateway with OpenAI-compatible API | 20 | <https://github.com/juangchuank-ops/minimax2api> |
| qwen_free_api | Python client for Qwen web through an OpenAI-compatible API | 20 | <https://github.com/Staks-sor/qwen_free_api> |
| deepseek-api (smkttl) | Unofficial DeepSeek API by reverse-engineering its web interface | 16 | <https://github.com/smkttl/deepseek-api> |
| qwen2api (annewj023) | Converts chat.qwen.ai web into an external API | 13 | <https://github.com/annewj023/qwen2api> |
| Doubao2api (Hu410) | Lightweight proxy reversing Doubao Web API into Chat Completions | 12 | <https://github.com/Hu410/Doubao2api> |
| minimaxM3-web2api | MiniMax Agent web chat to OpenAI API, reimplementing the JS signature algorithm | 12 | <https://github.com/snake-aabb-wtf/minimaxM3-web2api> |
| deepseek2api (0xgetz) | Pure-Go OpenAI-compatible proxy for chat.deepseek.com | 11 | <https://github.com/0xgetz/deepseek2api> |
| FreeTokenAPI | DeepSeek2API/Qwen2API with OpenAI and Anthropic-compatible endpoints | 10 | <https://github.com/mmmlllnnn/FreeTokenAPI> |
| minimax2api (0xgetz) | OpenAI-compatible proxy for the MiniMax Agent web API | 9 | <https://github.com/0xgetz/minimax2api> |
| deepseek-2api | DeepSeek web API to OpenAI REST gateway on Cloudflare Workers | 5 | <https://github.com/zxy1994/deepseek-2api> |

## Coding Agents (Claude Code, Cursor, Copilot…)

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| claw-code | Clean-room Rust/Python rewrite of the Claude Code agent harness after the source leak | 194,968 | <https://github.com/ultraworkers/claw-code> |
| CLIProxyAPI | Wraps Codex, Claude Code, Antigravity, Grok and Gemini CLI OAuth backends as OpenAI/Claude-compatible APIs | 54,940 | <https://github.com/router-for-me/CLIProxyAPI> |
| sub2api | Relay that exposes Claude, OpenAI, Gemini and Grok subscriptions as unified APIs | 43,805 | <https://github.com/Wei-Shaw/sub2api> |
| claude-code-router | Proxy that routes Claude Code's Anthropic API traffic to other model providers | 37,637 | <https://github.com/musistudio/claude-code-router> |
| Antigravity-Manager | Antigravity account manager with local OpenAI/Anthropic/Gemini proxy | 32,112 | <https://github.com/lbjlaq/Antigravity-Manager> |
| opencode-antigravity-auth *(archived)* | OpenCode plugin authenticating against Antigravity to use its Gemini/Claude quota | 10,937 | <https://github.com/NoeFabris/opencode-antigravity-auth> |
| claude-code-sourcemap | Claude Code 2.1.88 TypeScript source restored from sourcesContent in the leaked cli.js.map | 9,704 | <https://github.com/ChinaSiro/claude-code-sourcemap> |
| AIClient2API | Multi-protocol proxy for Antigravity, Codex, Grok, Kiro and Claude client backends | 8,872 | <https://github.com/justlovemaki/AIClient2API> |
| gcli2api | Converts Gemini CLI and Antigravity credentials into OpenAI, Gemini and Claude APIs | 5,240 | <https://github.com/su-kaka/gcli2api> |
| antigravity-proxy (yuaotian) | DLL-injection proxy forcer for Google Antigravity IDE without TUN mode | 4,437 | <https://github.com/yuaotian/antigravity-proxy> |
| copilot-api | Reverse-engineered GitHub Copilot API exposed as OpenAI- and Anthropic-compatible proxy (works with Claude Code) | 4,149 | <https://github.com/ericc-ch/copilot-api> |
| antigravity-claude-proxy | Anthropic-compatible proxy for Claude/Gemini models through Antigravity's Cloud Code | 4,004 | <https://github.com/badrisnarayanan/antigravity-claude-proxy> |
| codex-desktop-linux | Unofficial Linux build of OpenAI's Codex/ChatGPT desktop app from the macOS bundle | 3,893 | <https://github.com/ilysenko/codex-desktop-linux> |
| claude-code-proxy | Run Claude Code on OpenAI models by translating its API traffic | 3,752 | <https://github.com/1rgs/claude-code-proxy> |
| how-claude-code-works | Deep dive into Claude Code internals: agent loop, context engineering, tools | 3,723 | <https://github.com/Windy3f3f3f3f/how-claude-code-works> |
| vibeproxy | macOS menu bar proxy reusing Claude Code and ChatGPT subscription OAuth for other AI tools | 3,384 | <https://github.com/automazeio/vibeproxy> |
| claude-tap | Intercepts and inspects API traffic of Claude Code, Codex CLI, Gemini CLI, Cursor CLI and other agents | 3,277 | <https://github.com/liaohch3/claude-tap> |
| WindsurfAPI | Reverse-engineered Windsurf/Devin Desktop model access exposed as OpenAI/Anthropic/Gemini-compatible API | 3,079 | <https://github.com/dwgx/WindsurfAPI> |
| claude-code-from-source | Architecture, patterns and internals of Claude Code reverse engineered from source maps | 2,960 | <https://github.com/alejandrobalderas/claude-code-from-source> |
| claude-code-proxy | Claude Code to OpenAI API translation proxy | 2,799 | <https://github.com/fuergaosi233/claude-code-proxy> |
| tweakcc | Patches Claude Code's minified cli.js to customize system prompts, toolsets, themes and UI | 2,541 | <https://github.com/Piebald-AI/tweakcc> |
| claude-code-reverse | Uses LLMs to analyze minified Claude Code and visualize its LLM interactions and prompts | 2,435 | <https://github.com/Yuyz0112/claude-code-reverse> |
| AntigravityManager | Electron app managing accounts and processes for Google Antigravity | 2,364 | <https://github.com/Draculabo/AntigravityManager> |
| claude_code_src | Claude Code source restored from the sourcesContent of the leaked 2.1.88 source map | 2,335 | <https://github.com/ponponon/claude_code_src> |
| copilot.el | Unofficial GitHub Copilot plugin for Emacs | 2,330 | <https://github.com/copilot-emacs/copilot.el> |
| kiro-gateway | Proxy gateway for Kiro IDE & CLI (Amazon Q Developer) exposing OpenAI/Anthropic-compatible APIs | 2,311 | <https://github.com/jwadow/kiro-gateway> |
| codex2api (james-6-23) | Go Codex reverse proxy with admin dashboard | 2,276 | <https://github.com/james-6-23/codex2api> |
| opencode-openai-codex-auth | OpenCode plugin using ChatGPT Plus/Pro OAuth via Codex backend | 2,211 | <https://github.com/numman-ali/opencode-openai-codex-auth> |
| kiro.rs | Rust service translating the Kiro backend API to Anthropic format with token refresh | 1,940 | <https://github.com/hank9999/kiro.rs> |
| cursor2api (7836246) *(archived)* | Proxy converting Cursor's web docs API into OpenAI/Anthropic-compatible format | 1,893 | <https://github.com/7836246/cursor2api> |
| ChatMock | OpenAI-compatible API served from a ChatGPT subscription via Codex auth | 1,556 | <https://github.com/RayBytes/ChatMock> |
| cursor-reset | Resets Cursor's device identification to work around trial restrictions | 1,513 | <https://github.com/ultrasev/cursor-reset> |
| openai-oauth | Local proxy that reuses Codex CLI ChatGPT OAuth tokens as an OpenAI-compatible API | 1,398 | <https://github.com/EvanZhouDev/openai-oauth> |
| Kiro-Go | Converts Kiro accounts into OpenAI/Anthropic APIs with pooling and streaming | 1,175 | <https://github.com/Quorinex/Kiro-Go> |
| pi-generative-ui | Claude.ai's generative UI widgets reverse engineered and rebuilt for the pi agent | 1,161 | <https://github.com/Michaelliv/pi-generative-ui> |
| copilot-api | GitHub Copilot and Codex gateway exposing OpenAI/Anthropic-compatible APIs | 1,082 | <https://github.com/caozhiyuan/copilot-api> |
| cursor2api-go | Go proxy that converts Cursor's internal chat API into an OpenAI-compatible endpoint | 1,053 | <https://github.com/Xchat1/cursor2api-go> |
| claude-code-source-code-deobfuscation *(archived)* | Cleanroom deobfuscation of the Claude Code npm package cli.js into readable source | 991 | <https://github.com/ghuntley/claude-code-source-code-deobfuscation> |
| gemini-cli-openai | Cloudflare Worker exposing Gemini CLI endpoints as an OpenAI API | 895 | <https://github.com/GewoonJaap/gemini-cli-openai> |
| antigravity2api-nodejs | Node.js proxy translating Google Antigravity's API into OpenAI format | 815 | <https://github.com/liuw1535/antigravity2api-nodejs> |
| claude-code-source | Claude Code v2.1.88 TypeScript source recovered from the leaked npm source map | 798 | <https://github.com/hangsman/claude-code-source> |
| HitCC | Reverse-engineering documentation of the full logic of the Claude Code CLI Node.js version | 747 | <https://github.com/hitmux/HitCC> |
| OpenCodex | Middleware to remotely access and operate Codex/ChatGPT Desktop from other devices | 721 | <https://github.com/RyensX/OpenCodex> |
| copilot-explorer | Reverse engineers the Copilot VS Code extension JS bundle: module graph, prompt building, inline completion | 705 | <https://github.com/thakkarparth007/copilot-explorer> |
| cursor-api (wisdgod) *(archived)* | Reverse-engineered Cursor API turned into an OpenAI-compatible service | 693 | <https://github.com/wisdgod/cursor-api> |
| claude-desktop-extra | Patched Claude Desktop builds for Arch/Fedora/NixOS/AppImage with Computer Use and extras | 672 | <https://github.com/patrickjaja/claude-desktop-extra> |
| zerogravity | Proxy disguising requests as Antigravity traffic for OpenAI/Anthropic/Gemini APIs | 652 | <https://github.com/NikkeTryHard/zerogravity> |
| agent2api | Local gateway reusing desktop AI coding clients' login state (WorkBuddy, CatPaw…) | 650 | <https://github.com/aimod-cc/agent2api> |
| cursor-deepseek | HTTP/2 proxy that lets Cursor Composer talk to DeepSeek and other OpenAI-style backends | 646 | <https://github.com/danilofalcao/cursor-deepseek> |
| kiro2api | Go gateway converting Kiro (CodeWhisperer) auth into Anthropic/OpenAI APIs | 636 | <https://github.com/caidaoli/kiro2api> |
| CometixCode | Unofficial Rust reimplementation of the Claude Code terminal UI | 613 | <https://github.com/Haleclipse/CometixCode> |
| geminicli2api | FastAPI proxy turning Gemini CLI OAuth into OpenAI and Gemini API endpoints | 590 | <https://github.com/gzzhongqi/geminicli2api> |
| open-claude-code | Nightly Claude Code CLI decompile, reverse engineered and rebuilt as an open clean-room implementation | 529 | <https://github.com/ruvnet/open-claude-code> |
| anti-api | Turns Antigravity, Codex and Copilot into Anthropic/OpenAI-compatible servers | 520 | <https://github.com/silasxbt/anti-api> |
| openclaw-billing-proxy | Proxy that makes third-party requests look like Claude Code to use subscription billing | 518 | <https://github.com/zacdcook/openclaw-billing-proxy> |
| claude-code-proxy | Proxy that captures and visualizes in-flight Claude Code requests | 510 | <https://github.com/seifghazi/claude-code-proxy> |
| Antigravity-Tools-LS | Local proxy bridge for the Antigravity IDE language server | 430 | <https://github.com/lbjlaq/Antigravity-Tools-LS> |
| claude-cowork-linux | Runs Claude Desktop's Cowork mode natively on Linux | 423 | <https://github.com/johnzfitch/claude-cowork-linux> |
| KiroGate *(archived)* | OpenAI and Anthropic compatible Kiro IDE API proxy gateway | 421 | <https://github.com/aliom-v/KiroGate> |
| anthropic-proxy *(archived)* | Converts Claude Code's Anthropic requests to OpenAI format for OpenRouter | 413 | <https://github.com/maxnowack/anthropic-proxy> |
| KiroProxy | Compatibility and routing layer exposing Kiro IDE models as standard APIs | 390 | <https://github.com/xu-yuanhao/KiroProxy> |
| kiro2cc | Kiro token manager and proxy that lets Claude Code use the Kiro backend | 367 | <https://github.com/bestK/kiro2cc> |
| fast-context-mcp | Semantic code search MCP tool powered by Windsurf's reverse-engineered SWE-grep protocol | 363 | <https://github.com/SammySnake-d/fast-context-mcp> |
| ccproxy | Intercepting proxy to hook and rewrite Claude Code requests and responses | 352 | <https://github.com/starbaser/ccproxy> |
| composer-api | OpenAI-compatible API proxy for Cursor's Composer model | 345 | <https://github.com/standardagents/composer-api> |
| claude-code (T-Lab-CUHKSZ) | Buildable research fork of leaked Claude Code source with a reverse-engineered Bun build system | 329 | <https://github.com/T-Lab-CUHKSZ/claude-code> |
| copilot-api | Reverse-engineered GitHub Copilot API client and server | 322 | <https://github.com/B00TK1D/copilot-api> |
| api2cursor | Adapter that lets Cursor Pro use third-party relay APIs by rewriting its requests | 300 | <https://github.com/h88782481/api2cursor> |
| claude-code-reverse | Source analysis report of Claude Code from its bundled CLI | 288 | <https://github.com/ghboke/claude-code-reverse> |
| cursor-api-proxy | OpenAI-style API proxy that drives Cursor's `agent` CLI | 277 | <https://github.com/anyrobert/cursor-api-proxy> |
| claude-worker-proxy | Cloudflare Worker proxy translating Claude Code's Anthropic requests to other providers | 276 | <https://github.com/glidea/claude-worker-proxy> |
| ccproxy-api | Local reverse proxy reusing Claude Code and Codex subscriptions as APIs | 275 | <https://github.com/CaddyGlow/ccproxy-api> |
| cursor-api | Reverse-engineered Cursor API converted to an OpenAI-compatible service | 269 | <https://github.com/zhx47/cursor-api> |
| cursortab.nvim *(archived)* | Reverse engineered Cursor Tab completion API brought to Neovim | 268 | <https://github.com/reachingforthejack/cursortab.nvim> |
| background-computer-use | Reverse-engineered OpenAI Codex background computer-use feature | 251 | <https://github.com/actuallyepic/background-computer-use> |
| cli2api | OpenAI-compatible API from Qoder CLI and WorkBuddy logins | 251 | <https://github.com/caigee-cmd/cli2api> |
| cocopilot2gpt | Converts a GitHub Copilot subscription into a ChatGPT-style API | 247 | <https://github.com/ljnchn/cocopilot2gpt> |
| claude-code-source-analysis (catyans) | Module-by-module analysis of the leaked Claude Code TypeScript source | 218 | <https://github.com/catyans/claude-code-source-analysis> |
| Antigravity2Api | Proxies Antigravity into Claude and Gemini APIs with thought-signature handling | 209 | <https://github.com/znlsl/Antigravity2Api> |
| qoder-proxy | Local OpenAI-compatible proxy for Qoder CN CLI | 209 | <https://github.com/avaritiachaos/qoder-proxy> |
| open-claude-code (xtherk) | Claude Code 2.1.88 source recovered from sourcemaps and build-fixed as a research reference | 207 | <https://github.com/xtherk/open-claude-code> |
| ungate | Use Claude and ChatGPT subscriptions inside Cursor instead of paid API tokens | 206 | <https://github.com/orchidfiles/ungate> |
| augment2api | Middle layer that exposes Augment Code's API as OpenAI-compatible | 192 | <https://github.com/linqiu919/augment2api> |
| pi-black | Use a Claude Max/Pro subscription inside the Pi coding agent | 191 | <https://github.com/paoloanzn/pi-black> |
| claude-code-analysis | Reverse engineering analysis of Claude Code's internal architecture | 188 | <https://github.com/ComeOnOliver/claude-code-analysis> |
| kiro2cc-proxy | Kiro reverse proxy for Claude Code and Codex with SSE streaming | 186 | <https://github.com/TsinHzl/kiro2cc-proxy> |
| cursor-unchained | Reverse-engineered Cursor's AI tab completion to use in other editors | 179 | <https://github.com/dcrebbin/cursor-unchained> |
| CAS | Orchestrator built by reverse engineering Claude Code internals | 176 | <https://github.com/codingagentsystem/cas> |
| trae-api | Exposes Trae IDE's builtin models through an OpenAI-compatible API | 175 | <https://github.com/A-23187/trae-api> |
| claude-code-research | Independent research on Claude Code and Claude Agent SDK internals | 172 | <https://github.com/cablate/claude-code-research> |
| claude-cowork-service | Linux daemon reimplementing Claude Desktop Cowork's reverse-engineered vsock RPC protocol | 167 | <https://github.com/patrickjaja/claude-cowork-service> |
| claude-code-sourcemap-learning-notebook | Reverse-engineering notes on Claude Code's 512K lines of TypeScript: architecture and design decisions | 166 | <https://github.com/dadiaomengmeimei/claude-code-sourcemap-learning-notebook> |
| gemini-cli-proxy | Wraps Gemini CLI as an OpenAI-compatible API to use its free Gemini Pro quota | 153 | <https://github.com/nettee/gemini-cli-proxy> |
| github-copilot | Analysis of the GitHub Copilot extension internals | 148 | <https://github.com/saschaschramm/github-copilot> |
| KiroaaS | Desktop app exposing Kiro's models through local OpenAI/Anthropic-compatible API | 146 | <https://github.com/hnewcity/KiroaaS> |
| cursorweb2api | Converts Cursor's web chat into an OpenAI-compatible API | 142 | <https://github.com/jhhgiyv/cursorweb2api> |
| opencode-antigravity-quota | OpenCode plugin reading Antigravity/Gemini CLI quota endpoints across accounts | 142 | <https://github.com/frieser/opencode-antigravity-quota> |
| QoderGateway | Turns Alibaba Qoder accounts into one OpenAI-compatible API | 141 | <https://github.com/bzym2/QoderGateway> |
| copilot2api-go | Turns GitHub Copilot into OpenAI/Anthropic-compatible server for Claude Code, Codex, OpenCode | 140 | <https://github.com/StarryKira/copilot2api-go> |
| pi-gpt-search | Reverse-engineered Codex's web search to use with Claude and local models | 140 | <https://github.com/mateusdcc/pi-gpt-search> |
| m365-copilot-proxy | OpenAI-compatible proxy using a Microsoft 365 Copilot licence as a model backend | 138 | <https://github.com/cramt/m365-copilot-proxy> |
| qoder2api-hub | Qoder gateway reimplementing COSY request signing and device fingerprint | 137 | <https://github.com/shuishuipingan/qoder2api-hub> |
| claude-source-leaked | Claude Code v2.1.88 source analysis: system prompts, hidden feature flags and architecture | 133 | <https://github.com/noya21th/claude-source-leaked> |
| github-copilot-api-vscode | Exposes GitHub Copilot as a local OpenAI-compatible API gateway from VS Code | 129 | <https://github.com/suhaibbinyounis/github-copilot-api-vscode> |
| claude-code-working | Working Claude Code CLI rebuilt from reverse-engineered source analysis | 122 | <https://github.com/777genius/claude-code-working> |
| Kiro2api-Node | Node.js Kiro-to-API proxy | 118 | <https://github.com/lulistart/Kiro2api-Node> |
| cursor-api | Relay that converts Cursor's chat API into OpenAI format | 117 | <https://github.com/waitkafuka/cursor-api> |
| subrouter | Routes Codex/Claude Code traffic across multiple ChatGPT Pro and Claude Max subscriptions | 117 | <https://github.com/manaflow-ai/subrouter> |
| cloclo (claude-code-sdk) | Reverse-engineered Claude Code to build single-file SDK CLIs in Node, Python, Go, Rust | 114 | <https://github.com/SeifBenayed/cloclo> |
| eclipse-github-copilot-integration | Open source GitHub Copilot integration for Eclipse | 114 | <https://github.com/masecla22/eclipse-github-copilot-integration> |
| llm-openai-via-codex | Reverse-engineered Codex CLI auth to call OpenAI models via a Codex subscription | 114 | <https://github.com/simonw/llm-openai-via-codex> |
| AntigravityProxyLauncher | DYLD-injection transparent proxy for Antigravity/Gemini with MITM of AI traffic | 106 | <https://github.com/OpsinTech/AntigravityProxyLauncher> |
| xcode-copilot-server | GitHub Copilot proxy for Xcode with Claude Agent and Codex Agent support | 105 | <https://github.com/theblixguy/xcode-copilot-server> |
| zcode-cli | Unofficial terminal client for the agent runtime shipped with ZCode Desktop | 102 | <https://github.com/kingsword09/zcode-cli> |
| claude-codex | Adapter letting the Codex desktop app drive Claude Code via the Codex app-server protocol | 99 | <https://github.com/fuergaosi233/claude-codex> |
| clodex | Bridges Claude Code to OpenAI models via API key or ChatGPT/Codex-plan OAuth | 99 | <https://github.com/bman654/clodex> |
| zemote | Remote control client for ZCode Desktop on phones and tablets, built by replicating its protocol | 99 | <https://github.com/HumanAILoop/zemote> |
| cursoride2api | Tutorial on reverse engineering the Cursor IDE API | 96 | <https://github.com/7836246/cursoride2api> |
| claude-meter | Reverse engineering Claude Code usage limits to track remaining quota | 91 | <https://github.com/abhishekray07/claude-meter> |
| claude-code-source-analysis (xiaonancs) | Architecture breakdown of 23 Claude Code subsystems from source study | 90 | <https://github.com/xiaonancs/claude-code-source-analysis> |
| qoder2api | Qoder reverse engineering and Qoder-to-API demo | 90 | <https://github.com/cubk1/qoder2api> |
| cursorcli2api | OpenAI- and Anthropic-compatible HTTP API in front of the Cursor Agent CLI | 89 | <https://github.com/Azhi-ss/cursorcli2api> |
| cpa-multi-plugins | CLIProxyAPI OAuth provider plugins for CodeBuddy, Trae and Qoder | 87 | <https://github.com/mmqz/cpa-multi-plugins> |
| kiro2api | Kiro to Anthropic/OpenAI API proxy | 83 | <https://github.com/nineyuanz/kiro2api> |
| cursor-grpc | Reverse engineered Cursor IDE gRPC / protobuf definitions | 81 | <https://github.com/Jordan-Jarvis/cursor-grpc> |
| antigravity-proxy *(archived)* | Gateway exposing Google Antigravity's internal Gemini and Claude APIs | 79 | <https://github.com/frieser/antigravity-proxy> |
| antigravity-add-model | Patch for Google Antigravity that intercepts its internal Cloud Code API to add other LLM providers | 76 | <https://github.com/vahapogut/antigravity-add-model> |
| Antigravity-Database-Manager | Database manager and recovery tool for the Google Antigravity IDE conversation store | 76 | <https://github.com/ag-donald/Antigravity-Database-Manager> |
| cursor-tab *(archived)* | Protocol Buffers definitions for Cursor Tab | 75 | <https://github.com/wisdgod/cursor-tab> |
| Cursor2API | Lightweight gateway exposing Cursor's tools/models as an API | 75 | <https://github.com/NGLSG/Cursor2API> |
| cursor_api_demo | Cursor IDE backend endpoint API reverse engineered (v2.6.22) | 73 | <https://github.com/eisbaw/cursor_api_demo> |
| kiro-reverse-api | Reverse-engineered Kiro API with a provider management console | 72 | <https://github.com/dangweilinshinidie/kiro-reverse-api> |
| copilot-api | GitHub Copilot to OpenAI/Responses/Anthropic API server | 71 | <https://github.com/QLHazyCoder/copilot-api> |
| cursor-account-api | API for obtaining free Cursor trial accounts | 69 | <https://github.com/Elawen-Carl/cursor-account-api> |
| qoder2api | Converts Qoder AI service to OpenAI/Claude/Codex-format API | 66 | <https://github.com/Zhengyuuuui/qoder2api> |
| codex-app-linux | Unofficial Codex App for Linux with npm, AUR and Nix packaging | 65 | <https://github.com/better-slop/codex-app-linux> |
| cursor-agent-api-proxy | Wraps Cursor CLI as an OpenAI-compatible API for any client | 64 | <https://github.com/tageecc/cursor-agent-api-proxy> |
| kirocc | Local proxy forwarding Anthropic Messages API calls to Kiro's backend using Kiro CLI credentials | 64 | <https://github.com/d-kuro/kirocc> |
| cursor-opencode-auth | Use a Cursor account inside the OpenCode TUI | 63 | <https://github.com/Infiland/cursor-opencode-auth> |
| copilot-api (prassaaa) | Exposes GitHub Copilot as OpenAI/Anthropic-compatible API for Claude Code | 62 | <https://github.com/prassaaa/copilot-api> |
| cc-copilot-bridge | Route Claude Code CLI through a Copilot subscription, Ollama or Anthropic | 61 | <https://github.com/FlorianBruniaux/cc-copilot-bridge> |
| copilot-openai-api | FastAPI proxy turning GitHub Copilot chat completions/embeddings into an OpenAI-compatible service | 60 | <https://github.com/yuchanns/copilot-openai-api> |
| coxy | GitHub Copilot exposed as OpenAI-compatible APIs | 60 | <https://github.com/coxy-proxy/coxy> |
| cursor-rpc | Reverse engineered RPC client for Cursor.sh cloud services | 60 | <https://github.com/everestmz/cursor-rpc> |
| Antigravity-Proxy | OpenAI/Anthropic/Gemini-compatible Antigravity reverse gateway | 59 | <https://github.com/Kazuki-0147/Antigravity-Proxy> |
| copilot-proxy | Make the GitHub Copilot extension work with any LLM by proxying its traffic | 59 | <https://github.com/jjleng/copilot-proxy> |
| claude-code-reverse | Reverse analysis of Claude Code | 58 | <https://github.com/injekt/claude-code-reverse> |
| Qoder-2API-Go | Go OpenAI-compatible API for Qoder | 58 | <https://github.com/EchoPing07/Qoder-2API-Go> |
| AgentHub | Reverse proxy turning local Trae, WorkBuddy and Zcode into OpenAI API | 57 | <https://github.com/HUIdada1/AgentHub> |
| antigravity-proxy *(archived)* | Intercepts Google Antigravity IDE API calls to use your own Gemini key | 57 | <https://github.com/elad12390/antigravity-proxy> |
| Codex-App-Linux | Codex App (macOS) ported to Linux | 57 | <https://github.com/areu01or00/Codex-App-Linux> |
| codex-asr | Unofficial CLI and Whisper-compatible shim for Codex Desktop speech recognition | 57 | <https://github.com/Wangnov/codex-asr> |
| qoder-proxy | OpenAI API wrapper around the Qoder CLI | 57 | <https://github.com/foxy1402/qoder-proxy> |
| claw-decode | Decodes leaked Claude Code source: hidden features, 43 tool definitions, system prompts | 56 | <https://github.com/fattail4477/claw-decode> |
| cursor2api *(archived)* | Converts Cursor chat into an OpenAI-compatible API | 56 | <https://github.com/mt-altman/cursor2api> |
| copilot-proxy | HTTP proxy exposing GitHub Copilot free quota as an OpenAI-compatible API | 55 | <https://github.com/hankchiutw/copilot-proxy> |
| cursor2api | Proxy converting Cursor's docs chat endpoint to an OpenAI-compatible API | 55 | <https://github.com/gopkg-dev/cursor2api> |
| copilot-api-plus | GitHub Copilot proxy with OpenAI Responses and Anthropic Messages APIs | 53 | <https://github.com/imbuxiangnan-cyber/copilot-api-plus> |
| copilot-proxy-api | Self-hosted GitHub Copilot bridge for Claude Code and Codex CLI | 51 | <https://github.com/voidsteed/copilot-proxy-api> |
| lingma-proxy | OpenAI/Anthropic-compatible proxy for Alibaba Lingma and QoderCN | 46 | <https://github.com/Lutiancheng1/lingma-proxy> |
| claude-max-api-proxy (sethschnrt) | Exposes a Claude Max subscription as an OpenAI-compatible API | 45 | <https://github.com/sethschnrt/claude-max-api-proxy> |
| kiro2api-deno | Deno Kiro-to-API proxy | 45 | <https://github.com/AAEE86/kiro2api-deno> |
| claude-code-reverse | Claude Code reverse engineering notes on prompts, tool design and flow | 43 | <https://github.com/V1ki/claude-code-reverse> |
| copilot-proxy (Jer-y) | Turns GitHub Copilot into an OpenAI/Anthropic-compatible server | 43 | <https://github.com/Jer-y/copilot-proxy> |
| antigravity-proxy | Proxy intercepting Antigravity's Gemini API and rerouting to other providers | 40 | <https://github.com/12errh/antigravity-proxy> |
| ampcode-connector | Routes AmpCode requests through local Claude Code, Codex CLI and Gemini OAuth credentials | 38 | <https://github.com/nghyane/ampcode-connector> |
| expose-github-copilot-http-api | Exposes VS Code's GitHub Copilot as an HTTP API | 38 | <https://github.com/purocean/expose-github-copilot-http-api> |
| kiro2Api | Kiro to API proxy | 38 | <https://github.com/Lavender3533/kiro2Api> |
| claude-code-copilot | Local proxy translating Claude Code's Anthropic API to GitHub Copilot | 37 | <https://github.com/samarth777/claude-code-copilot> |
| gemini-cli-proxy | Uses Gemini CodeAssist (Gemini CLI) through OpenAI/Anthropic API interfaces | 36 | <https://github.com/ubaltaci/gemini-cli-proxy> |
| kiro2api-rs | Rust Kiro-to-Anthropic API proxy with account pool | 35 | <https://github.com/vagmr/kiro2api-rs> |
| agent-hop | Reverse-engineered coding agents' session formats to resume sessions across agents | 34 | <https://github.com/hetpatel-11/agent-hop> |
| copilot2api | Go proxy exposing GitHub Copilot as OpenAI and Anthropic endpoints | 34 | <https://github.com/whtsky/copilot2api> |
| Kiro-Go | Go/Gin Kiro API proxy with OpenAI and Anthropic compatibility | 34 | <https://github.com/hj01857655/Kiro-Go> |
| claude-agent-sdk-go (character-ai) | Go SDK for Claude agents over the Claude Code CLI | 32 | <https://github.com/character-ai/claude-agent-sdk-go> |
| claude-code-reverse-engineering | Reverse-engineered design documents and specs of the Claude Code CLI | 32 | <https://github.com/jung-wan-kim/claude-code-reverse-engineering> |
| cliproxy-rs | Rust port of CLIProxyAPI, the LLM-subscription-to-API proxy | 32 | <https://github.com/vayungodara/cliproxy-rs> |
| raven | GitHub Copilot proxy translating to Anthropic/OpenAI APIs with usage dashboard | 32 | <https://github.com/nocoo/raven> |
| cursorToApi | Converts Cursor into an OpenAI-compatible API | 30 | <https://github.com/dreamhartley/cursorToApi> |
| claude-code-reverse | Claude Code reverse engineering | 29 | <https://github.com/apstenku123/claude-code-reverse> |
| codebuddy2api | Proxies Tencent CodeBuddy with OpenAI and Anthropic compatible APIs | 28 | <https://github.com/orangeboyChen/codebuddy2api> |
| claude-code (nadonghuang) | Deobfuscated Claude Code v2.1.76 TypeScript reconstructed from the npm package | 26 | <https://github.com/nadonghuang/claude-code> |
| claude-code-haha | Locally runnable build of the leaked Claude Code source | 26 | <https://github.com/jiahuangzheng/claude-code-haha> |
| claude_agent_sdk_rust | Unofficial Rust SDK speaking the Claude Code CLI control protocol | 26 | <https://github.com/Wally869/claude_agent_sdk_rust> |
| codex2api (rokyplay) | OpenAI Codex API proxy with format conversion and dashboard | 25 | <https://github.com/rokyplay/codex2api> |
| cursor-api | Cursor chat API reverse proxy | 24 | <https://github.com/zeke-chin/cursor-api> |
| kiro-proxy | Kiro API proxy with OpenAI and Anthropic compatible endpoints | 24 | <https://github.com/Colin3191/kiro-proxy> |
| claude-agent-sdk-go (schlunsen) | Go port of the Claude Agent SDK driving the Claude Code CLI protocol | 23 | <https://github.com/schlunsen/claude-agent-sdk-go> |
| minimax-agent-linux | Unofficial Linux port of the MiniMax Agent desktop app | 22 | <https://github.com/unn-Known1/minimax-agent-linux> |
| trae-api-proxy | Go proxy bridging the Trae IDE API to the OpenAI standard API | 22 | <https://github.com/muskke/trae-api-proxy> |
| claude-agent-sdk-go (Roasbeef) | Go SDK for Claude Code with tool use, MCP and streaming | 20 | <https://github.com/Roasbeef/claude-agent-sdk-go> |
| codex-browser-bridge | Exposes ChatGPT desktop app's internal browser bridge as an MCP server | 20 | <https://github.com/DeliciousBuding/codex-browser-bridge> |
| copilot-proxy-go | Go server turning GitHub Copilot into OpenAI/Anthropic-compatible API | 20 | <https://github.com/tonghaoch/copilot-proxy-go> |
| cursor2api-go | Go Cursor-to-OpenAI API bridge with Messages/Responses/Tools support | 20 | <https://github.com/yourChainGod/cursor2api-go> |
| Antigravity2Api | Transforms Antigravity into standard Claude and Gemini APIs | 18 | <https://github.com/anshulrules/Antigravity2Api> |
| Deno-Augment2Api | Deno port of Augment2Api | 18 | <https://github.com/xiaojia21190/Deno-Augment2Api> |
| qodercli-reverse | Reverse engineering of the Qoder CLI | 18 | <https://github.com/alingse/qodercli-reverse> |
| copilot-api | GitHub Copilot to OpenAI API | 17 | <https://github.com/patchescamerababy/copilot-api> |
| dsh-trae-api | Exposes Trae Work CN credits as local OpenAI/Anthropic API | 17 | <https://github.com/Wang-JQ77/dsh-trae-api> |
| claude-code-leaked-source *(archived)* | Mirror of the leaked Claude Code source | 16 | <https://github.com/sleeplessai/claude-code-leaked-source> |
| codexfast-current-launcher | Runtime launcher enabling hidden client flags (Fast mode) in Codex/ChatGPT Desktop | 16 | <https://github.com/qiaojiangwink/codexfast-current-launcher> |
| copilot-RE | Reverse engineered GitHub Copilot API plus CLI | 16 | <https://github.com/rohitaryal/copilot-RE> |
| cursor2api (AstroQore) | Cursor subscription as OpenAI API via direct agent.v1 protocol | 16 | <https://github.com/AstroQore/cursor2api> |
| kiro-reverse-api | Self-hosted Kiro API proxy with OpenAI/Anthropic endpoints and admin dashboard | 16 | <https://github.com/tanu360/kiro-reverse-api> |
| windsurf-api | REST API that sends prompts with images to Windsurf chat | 16 | <https://github.com/AlexStrNik/windsurf-api> |
| Copilot_Proxy | Self-hosted GitHub Copilot to OpenAI-compatible proxy with OAuth | 15 | <https://github.com/Open-Copilot-Proxy/Copilot_Proxy> |
| windsurf-proxy | MITM proxy for Windsurf IDE that swaps the LLM backend for your own Anthropic key | 15 | <https://github.com/pqhaz3925/windsurf-proxy> |
| claude-max-api-proxy (GodYeh) | Claude Max subscription as OpenAI-compatible API with tool calling | 13 | <https://github.com/GodYeh/claude-max-api-proxy> |
| codex-harness-internals | Reverse-engineered spec of the OpenAI Codex CLI harness: loop, tools, compaction | 13 | <https://github.com/AlexKenbo/codex-harness-internals> |
| copilot-api-proxy *(archived)* | Reverse proxy for GitHub Copilot API with OpenAI/Anthropic endpoints | 13 | <https://github.com/messense/copilot-api-proxy> |
| kiro2api (xwteam) | Rust Kiro relay speaking Anthropic, OpenAI, Responses and Gemini protocols | 13 | <https://github.com/xwteam/kiro2api> |
| learn-claude-code | Research repo for @anthropic-ai/claude-code v2.1.88 reconstructed from the npm package and sourcemap | 12 | <https://github.com/cnlnlhb/learn-claude-code> |
| noclick | Agent runtime that runs on your ChatGPT or Claude subscription | 12 | <https://github.com/noclickapp/noclick> |
| gemini-3-github-copilot-proxy | Use a Gemini plan via Gemini CLI auth inside GitHub Copilot | 11 | <https://github.com/Apothic-AI/gemini-3-github-copilot-proxy> |
| agy-tools-rust *(archived)* | Rust CLI reverse proxy exposing Antigravity Cloud Code as OpenAI/Claude/Gemini APIs | 9 | <https://github.com/ChrAlpha/agy-tools-rust> |
| antigravity-proxy (sortedcord) | Go proxy to Antigravity's internal Gemini API with quota tracking | 9 | <https://github.com/sortedcord/antigravity-proxy> |
| claude-buddy-hatchery | Reverse-engineered Claude Code /buddy companion generation algorithm | 9 | <https://github.com/cminn10/claude-buddy-hatchery> |
| kiro2api-rs | Rust Anthropic-compatible proxy over Kiro accounts with web panel | 9 | <https://github.com/gdtiti/kiro2api-rs> |
| claude-max-api-proxy-rs | Rust proxy translating OpenAI/Anthropic APIs to Claude Code CLI subscription | 8 | <https://github.com/thhuang/claude-max-api-proxy-rs> |
| gh_copilot_chat | Unofficial GitHub Copilot Chat SDK built on the reverse engineered API | 8 | <https://github.com/rabilrbl/gh_copilot_chat> |
| antigravity-proxy (usamashehab) | OpenAI-compatible proxy for Antigravity's Gemini and Claude models via OAuth | 7 | <https://github.com/usamashehab/antigravity-proxy> |
| claude-cli-protocol | Protocol documentation for the Claude Code CLI stream-json interface | 7 | <https://github.com/mzhaom/claude-cli-protocol> |
| claude-code-decompiled | Research reports from Claude Code source analysis: agent loop, telemetry, permissions | 7 | <https://github.com/alanisme/claude-code-decompiled> |
| cursor2api (KonghaYao) | Cursor subscription to Anthropic/OpenAI endpoint on Cloudflare or Deno | 7 | <https://github.com/KonghaYao/cursor2api> |
| kiro-proxy (bigdata2211it-web) | OpenAI-compatible local proxy for Kiro CLI (Amazon CodeWhisperer) | 7 | <https://github.com/bigdata2211it-web/kiro-proxy> |
| windsurf-api (imbuxiangnan) | Turns a Windsurf subscription into an OpenAI/Anthropic-compatible API | 7 | <https://github.com/imbuxiangnan-cyber/windsurf-api> |
| claude-code-internals (eran-broder) | Undocumented Claude Code internals found by having Claude reverse-engineer itself | 6 | <https://github.com/eran-broder/claude-code-internals> |
| claude-code-internals (swyxio) | Evidence-linked reconstruction of Claude Code internals from the native Bun executable | 6 | <https://github.com/swyxio/claude-code-internals> |
| augloop-copilot-proxy | Reverse proxy turning Microsoft 365 Excel Copilot (AugLoop) into an OpenAI API | 5 | <https://github.com/suimi8/augloop-copilot-proxy> |
| Claude-Chrome-Reverse | Reverse-engineered Claude for Chrome extension modified to accept an API key | 5 | <https://github.com/Elity/Claude-Chrome-Reverse> |
| cursor2api (Yuki13929) | Anthropic Messages / OpenAI API for Cursor models via the reverse-engineered agent protocol | 5 | <https://github.com/Yuki13929/cursor2api> |
| ferridex | Local Codex and Claude subscription proxy with web dashboard | 5 | <https://github.com/afengleafs/ferridex> |
| cursor-tab | Reverse-engineered Cursor tab completion client | 4 | <https://github.com/abyesilyurt/cursor-tab> |
| niri-computer-use | Patched Codex Desktop Computer Use backend for NixOS + niri | 4 | <https://github.com/lihaoze123/niri-computer-use> |
| anti-client | Async Python client for Google Antigravity's internal API | 2 | <https://github.com/Makobcki/anti-client> |
| claude-rc-api | Reverse-engineered Claude Code Remote Control / Sessions API | 2 | <https://github.com/ThatCrispyToast/claude-rc-api> |
| claudex | Translates Anthropic Messages API to the Codex backend Responses API via Codex device-flow auth | 2 | <https://github.com/m0n0x41d/claudex> |
| codex-openai-proxy | OpenAI-compatible proxy over ChatGPT/Codex subscription backend using the Codex CLI OAuth flow | 1 | <https://github.com/0oAstro/codex-openai-proxy> |
| pollux | Gemini CLI reverse proxy speaking to raw Cloud Code Gemini endpoints | 1 | <https://github.com/yeshanjun/pollux> |
| claude-cleanroom-2.1.83 | Architecture docs reverse-engineered from Claude Code v2.1.83 | 0 | <https://github.com/nwyin/claude-cleanroom-2.1.83> |
| claude-code-diff-plugin | Diffs Claude Code binaries between releases to surface unreleased features | 0 | <https://github.com/takuyanagai0213/claude-code-diff-plugin> |
| claude-code-reverse (hqman) | Reverse engineering Claude Code's minified cli.mjs with LLMs | 0 | <https://github.com/hqman/claude-code-reverse> |
| codex-subscription-proxy | OpenAI Responses-compatible proxy using Codex/ChatGPT subscription auth | 0 | <https://github.com/Caleb0796/codex-subscription-proxy> |

## Image/Audio/Video Gen APIs

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| midjourney-proxy | Proxies Midjourney's Discord channel to provide an HTTP API for image generation | 5,365 | <https://github.com/novicezk/midjourney-proxy> |
| suno-api | Unofficial self-hostable REST API for Suno music generation via its internal endpoints | 3,255 | <https://github.com/gcui-art/suno-api> |
| flow2api | Reverse-engineered Google Flow API for Nano Banana Pro and Veo generation | 3,034 | <https://github.com/TheSmallHanCat/flow2api> |
| midjourney-api (zcpua) | Unofficial Node.js Midjourney client over Discord | 1,868 | <https://github.com/zcpua/midjourney-api> |
| Suno-API | Unofficial Suno music generation API | 1,812 | <https://github.com/SunoAI-API/Suno-API> |
| sora2api *(archived)* | Reverse-engineered Sora web API with account pool | 1,235 | <https://github.com/TheSmallHanCat/sora2api> |
| jimeng-api *(archived)* | Reverse-engineered Jimeng/Dreamina text-to-image, image-to-image and video API | 1,040 | <https://github.com/iptag/jimeng-api> |
| midjourney-api (yokonsan) | Midjourney Discord API wrapper as REST service: imagine, upscale, variation, describe | 891 | <https://github.com/yokonsan/midjourney-api> |
| midjourney-proxy | Midjourney Discord proxy exposing an image generation API | 820 | <https://github.com/trueai-org/midjourney-proxy> |
| ttsfm | OpenAI-compatible TTS API mirroring the free openai.fm service | 738 | <https://github.com/dbccccccc/ttsfm> |
| jimeng-free-api-all | Jimeng (ByteDance) image and video generation reverse API, OpenAI-compatible | 613 | <https://github.com/zhizinan1997/jimeng-free-api-all> |
| midjourney-proxy-plus | Extended Midjourney Discord proxy API | 575 | <https://github.com/litter-coder/midjourney-proxy-plus> |
| Midjourney_api | Unofficial Midjourney API via Discord sender/receiver (research only) | 419 | <https://github.com/George-iam/Midjourney_api> |
| SunoSongsCreator | Reverse engineered Suno song generation API (Python library and CLI) | 366 | <https://github.com/yihong0618/SunoSongsCreator> |
| sora-downloader | Extracts watermark-free Sora video links | 306 | <https://github.com/tibbar213/sora-downloader> |
| BingImageCreator *(archived)* | Reverse engineered API for Microsoft Bing Image Creator (DALL-E) | 300 | <https://github.com/acheong08/BingImageCreator> |
| capcut-tts-api | Reverse-engineered CapCut TTS and STT API | 296 | <https://github.com/K07VN/capcut-tts-api> |
| gflow-cli | Unofficial reverse-engineered CLI for Google Flow (Veo video, Imagen) | 279 | <https://github.com/ffroliva/gflow-cli> |
| Suno2openai | Calls the Suno web API in OpenAI format with a cookie pool | 275 | <https://github.com/wlhtea/Suno2openai> |
| imagineapi | Unofficial Midjourney API | 227 | <https://github.com/imagineapi/imagineapi> |
| klingCreator | Reverse engineered API for Kling AI image and video generation | 222 | <https://github.com/yihong0618/klingCreator> |
| UdioWrapper | Python package generating music tracks through Udio's unofficial API | 182 | <https://github.com/flowese/UdioWrapper> |
| Suno-API (Go) | Unofficial Suno AI API in Go supporting songs, lyrics and OpenAI chat format | 159 | <https://github.com/Suno-API/Suno-API> |
| midjourney-discord-api-php *(archived)* | Generate Midjourney images through the Discord API (PHP) | 135 | <https://github.com/ferranfg/midjourney-discord-api-php> |
| imageFX-api | Unofficial reverse-engineered API for Google Labs ImageFX | 133 | <https://github.com/rohitaryal/imageFX-api> |
| Luma-API | Unofficial Luma Dream Machine video generation API | 130 | <https://github.com/LumaAI-API/Luma-API> |
| Suno-API (Malith-Rukshan) | Unofficial Suno.ai Python library and REST API | 128 | <https://github.com/Malith-Rukshan/Suno-API> |
| notebooklm-podcast-automator | REST API automating NotebookLM sources and Audio Overview generation | 116 | <https://github.com/israelbls/notebooklm-podcast-automator> |
| Midjourney-Web-API | Unofficial Midjourney web API using captured browser request headers | 115 | <https://github.com/CelestialRipple/Midjourney-Web-API> |
| CapCut-TTS | CapCut text-to-speech wrapper API | 112 | <https://github.com/kuwacom/CapCut-TTS> |
| midjourney-proxy | Full-featured Midjourney Discord proxy (PHP/webman) | 105 | <https://github.com/webman-php/midjourney-proxy> |
| whisk-api | Unofficial reverse-engineered API for Google Labs Whisk | 101 | <https://github.com/rohitaryal/whisk-api> |
| vidai | Unofficial RunwayML Gen-2/Gen-3 video generation client | 97 | <https://github.com/igolaizola/vidai> |
| suno-api | Suno music generation API wrapper | 88 | <https://github.com/gochendong/suno-api> |
| IdeoImageCreator | Reverse engineered API for Ideogram image generation | 78 | <https://github.com/yihong0618/IdeoImageCreator> |
| Bimg | Reverse-engineered Bing Image Creator API as an NPM package | 76 | <https://github.com/nociza/Bimg> |
| IdeogramWrapper | Python wrapper for Ideogram image generation | 76 | <https://github.com/flowese/IdeogramWrapper> |
| craiyon.py | Unofficial API wrapper for Craiyon image generation | 70 | <https://github.com/FireHead90544/craiyon.py> |
| suno-api-private | Suno API with JWT token authentication support | 69 | <https://github.com/joeseesun/suno-api-private> |
| bingart | Unofficial async API wrapper for Bing Image and Video Creator | 58 | <https://github.com/DedInc/bingart> |
| suno-cli | Terminal client for Suno music generation | 58 | <https://github.com/paperfoot/suno-cli> |
| Comfyui-GeminiWeb | ComfyUI node using the Gemini web API for image generation and chat | 52 | <https://github.com/Koko-boya/Comfyui-GeminiWeb> |
| dreamina-api | Dreamina (CapCut AI) image generation API on Cloudflare Workers | 49 | <https://github.com/LiJunYi2/dreamina-api> |
| Suno-API | Unofficial Suno AI API | 48 | <https://github.com/imyizhang/Suno-API> |
| Lexica.art | Reverse-engineered Python API wrapper for Lexica.art image generation | 41 | <https://github.com/NotCookey/Lexica.art> |
| py-midjourney-proxy | Python Midjourney Discord proxy | 41 | <https://github.com/Anychnn/py-midjourney-proxy> |
| stable-diffusion-xl-api | Reverse-engineered API for Stable Diffusion XL 1.0 text-to-image | 41 | <https://github.com/KoushikNavuluri/stable-diffusion-xl-api> |
| wombot | Unofficial API and Discord bot for Wombo Dream art generation | 34 | <https://github.com/adri326/wombot> |
| suno-ai | JavaScript API for generating songs on suno.ai | 26 | <https://github.com/hissincn/suno-ai> |
| Msdesigner-api *(archived)* | Reverse-engineered API for Microsoft Designer image generation | 25 | <https://github.com/imnotdev25/Msdesigner-api> |
| suno-ai-proxy | Unofficial Suno AI Node.js API | 23 | <https://github.com/MelohubAI/suno-ai-proxy> |
| flow2api (HL320217) | Multi-user platform over the Google Flow / Labs FX protocol for image and video | 20 | <https://github.com/HL320217/flow2api> |
| suno-mcp | MCP server for generating songs through Suno's web API | 14 | <https://github.com/CodeKeanu/suno-mcp> |
| SunoApiManager | Unofficial Suno backend API with websocket, FastAPI and Swagger | 12 | <https://github.com/serkansmg/SunoApiManager> |
| opensuno | Open Suno API and MCP server for AI agents | 11 | <https://github.com/paean-ai/opensuno> |
| go-sora2api | Go reimplementation of sora2api, OpenAI-compatible wrapper for Sora app | 7 | <https://github.com/DouDOU-start/go-sora2api> |
| UdioOfflineLibrary | Desktop app to browse and download your full Udio library | 7 | <https://github.com/SirBitesalot/UdioOfflineLibrary> |
| unofficial-suno-api | Unofficial Suno API for research | 7 | <https://github.com/sunyujingmusic-alt/unofficial-suno-api> |
| chatgpt2api (fran0220) | Reverse proxy turning ChatGPT web image generation into OpenAI API endpoints | 6 | <https://github.com/fran0220/chatgpt2api> |
| Prisma-Python | Reverse-engineered Prisma style-transfer API from the Android app | 5 | <https://github.com/arunKumarNOP/Prisma-Python> |
| SunoAPI (tinyfeng) | Unofficial Suno API in Python/FastAPI with token keep-alive | 1 | <https://github.com/tinyfeng/SunoAPI> |

## MCP Servers for Private APIs

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| xiaohongshu-mcp | MCP server for Xiaohongshu (RedNote): login, publish, search, comment | 16,231 | <https://github.com/xpzouying/xiaohongshu-mcp> |
| whatsapp-mcp | WhatsApp MCP server built on whatsmeow web multidevice protocol | 6,551 | <https://github.com/lharries/whatsapp-mcp> |
| gemini-notebook-mcp-cli | CLI and MCP server for Gemini Notebook (NotebookLM) via its internal RPC API | 6,287 | <https://github.com/jacob-bd/gemini-notebook-mcp-cli> |
| linkedin-mcp-server | LinkedIn MCP server for profiles, companies, jobs and messages via browser session | 3,833 | <https://github.com/stickerdaniel/linkedin-mcp-server> |
| notebooklm-mcp *(archived)* | MCP server letting agents query Google NotebookLM with citations | 3,435 | <https://github.com/PleasePrompto/notebooklm-mcp> |
| garmin_mcp | MCP server for Garmin Connect data via unofficial API | 1,325 | <https://github.com/Taxuspt/garmin_mcp> |
| douyin-mcp-server *(archived)* | Douyin MCP extracting watermark-free video links and transcripts | 1,277 | <https://github.com/yzfly/douyin-mcp-server> |
| mcp-server-weread (freestylefly) | MCP server for WeChat Read (WeRead) shelf and notes | 578 | <https://github.com/freestylefly/mcp-server-weread> |
| Agentify Desktop | Lets coding agents drive logged-in ChatGPT, Claude, Gemini, Grok, Perplexity web sessions via MCP | 567 | <https://github.com/agentify-sh/desktop> |
| mcp-server-12306 | MCP server for China Railway 12306 ticket and station queries | 407 | <https://github.com/drfccv/mcp-server-12306> |
| mac_messages_mcp | MCP server for macOS Messages: read chat.db and send iMessages | 331 | <https://github.com/carterlasalle/mac_messages_mcp> |
| WeChat-MCP | Lets AI assistants read and reply to WeChat on desktop | 276 | <https://github.com/BiboyQG/WeChat-MCP> |
| whatsapp-mcp (verygoodplugins) | WhatsApp MCP server for reading and sending personal messages | 234 | <https://github.com/verygoodplugins/whatsapp-mcp> |
| perplexity-web-mcp (jacob-bd) | MCP server and Anthropic-compatible API over the Perplexity web interface | 199 | <https://github.com/jacob-bd/perplexity-web-mcp> |
| bilibili-mcp-js | Bilibili video search MCP service | 194 | <https://github.com/34892002/bilibili-mcp-js> |
| linkedin-mcp-server (eliasbiondo) | LinkedIn MCP server scraping people, companies and jobs | 194 | <https://github.com/eliasbiondo/linkedin-mcp-server> |
| notebooklm-mcp (roomi-fields) | NotebookLM over MCP plus local REST API, audio/video generation | 193 | <https://github.com/roomi-fields/notebooklm-mcp> |
| netease-music-mcp (Vael-KY) | MCP server reading and managing a NetEase Cloud Music account | 191 | <https://github.com/Vael-KY/netease-music-mcp> |
| bilibili-mcp-server | MCP server for Bilibili web API operations | 190 | <https://github.com/huccihuang/bilibili-mcp-server> |
| comet-mcp | MCP server driving Perplexity Comet browser over CDP | 181 | <https://github.com/hanzili/comet-mcp> |
| trainingpeaks-mcp | TrainingPeaks MCP server using the private web API, no API approval needed | 180 | <https://github.com/JamsusMaximus/trainingpeaks-mcp> |
| mcp-server-weread (ChenyqThu) | MCP server exposing WeRead books, highlights and notes | 172 | <https://github.com/ChenyqThu/mcp-server-weread> |
| apple-notes-mcp (sweetrb) | MCP server to read, search, edit and export Apple Notes on macOS | 152 | <https://github.com/sweetrb/apple-notes-mcp> |
| xiaohongshu-mcp-python | Python Xiaohongshu MCP for automated posting of notes and videos | 146 | <https://github.com/luyike221/xiaohongshu-mcp-python> |
| apple-notes-mcp (sirmews) *(archived)* | MCP server reading the Apple Notes SQLite store | 131 | <https://github.com/sirmews/apple-notes-mcp> |
| totem | MCP server with read/write access to Whoop data via the private reverse-engineered API | 127 | <https://github.com/thebriangao/totem> |
| netease-music-mcp (Cheiineeey) | NetEase Cloud Music MCP for song requests, lyrics and playlists | 113 | <https://github.com/Cheiineeey/netease-music-mcp> |
| perplexity-web-api-mcp *(archived)* | Perplexity AI MCP using the web API, no API key | 106 | <https://github.com/mishamyrt/perplexity-web-api-mcp> |
| bilibili-mcp (adoresever) | Bilibili MCP with search, comments, subtitles and danmaku | 104 | <https://github.com/adoresever/bilibili-mcp> |
| whatsapp-mcp-ts | WhatsApp MCP server in TypeScript on Baileys | 76 | <https://github.com/jlucaso1/whatsapp-mcp-ts> |
| tradingview-mcp-server | Unofficial MCP and CLI for TradingView's internal API | 53 | <https://github.com/fiale-plus/tradingview-mcp-server> |
| Perplexity-Comet-MCP | MCP server connecting Claude Code to Perplexity Comet browser | 51 | <https://github.com/RapierCraft/Perplexity-Comet-MCP> |
| blinkit-mcp | Unofficial MCP server to search, cart and order on Blinkit | 50 | <https://github.com/hereisSwapnil/blinkit-mcp> |
| wechat-mcp | MCP server for the WeChat desktop client | 47 | <https://github.com/JettChenT/wechat-mcp> |
| mobbin-mcp *(archived)* | Unofficial MCP for Mobbin's design library, no public API required | 46 | <https://github.com/pdcolandrea/mobbin-mcp> |
| tbank-mcp | Unofficial MCP server for T-Bank (Tinkoff) mobile banking private API | 36 | <https://github.com/icyberdeveloper/tbank-mcp> |
| whatsapp-mcp-extended | Maintained WhatsApp MCP with 26 tools, webhooks and Docker | 36 | <https://github.com/FelixIsaac/whatsapp-mcp-extended> |
| apple-photos-mcp | MCP server querying and exporting the macOS Photos library database | 30 | <https://github.com/sweetrb/apple-photos-mcp> |
| imessage-mcp (wyattjoh) | MCP server reading macOS iMessage chat.db | 29 | <https://github.com/wyattjoh/imessage-mcp> |
| imessage-mcp (anipotts) | Search and read Messages history from MCP clients | 27 | <https://github.com/anipotts/imessage-mcp> |
| signal-mcp | MCP server for Signal messaging via signal-cli | 26 | <https://github.com/rymurr/signal-mcp> |
| wamcp | WhatsApp MCP server with 61 tools over Baileys | 24 | <https://github.com/delltrak/wamcp> |
| perplexity-web-wrapper | Use a Perplexity subscription with MCP via a web wrapper | 23 | <https://github.com/balakumardev/perplexity-web-wrapper> |
| yandex-lavka-mcp | Unofficial MCP server for ordering Yandex Lavka groceries | 22 | <https://github.com/Dudude-bit/yandex-lavka-mcp> |
| notebooklm-mcp (m4yk3ldev) | NotebookLM MCP with 32 tools for notebooks, sources and studio content | 20 | <https://github.com/m4yk3ldev/notebooklm-mcp> |
| wechat-mcp (lw396) | WeChat chat MCP tool based on WeChatFerry hooking | 18 | <https://github.com/lw396/wechat-mcp> |
| Douyin-mcp | MCP server to search Douyin users and read/send direct messages | 17 | <https://github.com/Lozzi1910/Douyin-mcp> |
| twitter-mcp-server (gkydev) | Unofficial Twitter/X MCP server using cookie auth | 16 | <https://github.com/gkydev/twitter-mcp-server> |
| stays | Google Hotels MCP server and library via reverse-engineered batchexecute | 14 | <https://github.com/him229/stays> |
| instagram-dms-mcp | MCP server for reading and sending Instagram DMs via the private API | 10 | <https://github.com/braindead-dev/instagram-dms-mcp> |
| threads-mcp-crawler | MCP crawler extracting data from Meta Threads | 10 | <https://github.com/dkyazzentwatwa/threads-mcp-crawler> |
| substack-mcp-plus | Unofficial Substack MCP with publishing and analytics | 8 | <https://github.com/abanoub-ashraf/substack-mcp-plus> |
| MCP_Trenitalia | Unofficial Trenitalia MCP using viaggiatreno endpoints | 7 | <https://github.com/Fanfulla/MCP_Trenitalia> |
| perplexity-webui-mcp | MCP server querying Perplexity Pro via WebUI session token | 5 | <https://github.com/Microck/perplexity-webui-mcp> |
| sber-mcp | Unofficial MCP and async SDK for SberBank Online with browserless auth | 5 | <https://github.com/ex3lite/sber-mcp> |
| google-flow-mcp | Unofficial MCP for Google Flow (Veo / Nano Banana) through your Chrome session | 4 | <https://github.com/ParkSangGwon/google-flow-mcp> |
| notion-private-api-mcp | Notion MCP server via the private API (token_v2), no integration token | 4 | <https://github.com/kirvigen/notion-private-api-mcp> |

## Other AI

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| notebooklm-py | Unofficial NotebookLM Python API/CLI built on its undocumented internal RPC protocol | 19,706 | <https://github.com/teng-lin/notebooklm-py> |
| claude-desktop-zh-cn | Chinese localization patch for Claude Desktop on macOS, Windows and Linux | 7,570 | <https://github.com/javaht/claude-desktop-zh-cn> |
| claude-desktop-debian | Repackages the Windows Claude Desktop app to run on Debian/Linux | 5,449 | <https://github.com/aaddrick/claude-desktop-debian> |
| reverse-SynthID | Reverse engineering Google Gemini's SynthID image watermark detection | 4,954 | <https://github.com/aloshdenny/reverse-SynthID> |
| chatgpt-exporter | Export ChatGPT conversation history from the web app | 2,801 | <https://github.com/pionxzh/chatgpt-exporter> |
| convoviz | Converts ChatGPT export ZIPs into Markdown with media and usage visualizations | 889 | <https://github.com/mohamed-chs/convoviz> |
| cc-desktop-switch | Configures DeepSeek, Kimi, GLM and Bailian providers inside Claude Desktop | 800 | <https://github.com/lonr-6/cc-desktop-switch> |
| claude-desktop_win-zh_cn | Claude Desktop Windows zh-CN patch translating keys and JS chunk labels | 674 | <https://github.com/Jyy1529/claude-desktop_win-zh_cn> |
| S3Tokenizer | Reverse engineered reimplementation of CosyVoice's supervised semantic speech tokenizer | 535 | <https://github.com/xingchensong/S3Tokenizer> |
| MackingJAI | Exposes Apple Intelligence and ChatGPT desktop app through OpenAI / Ollama APIs | 355 | <https://github.com/0ssamaak0/MackingJAI> |
| open-claude-in-chrome | Reverse-engineered Claude in Chrome extension, open source for any Chromium browser | 246 | <https://github.com/noemica-io/open-claude-in-chrome> |
| claude-desktop-rtl-patch | CSS patch adding RTL support to Claude Desktop on Windows | 209 | <https://github.com/shraga100/claude-desktop-rtl-patch> |
| anthropic-tokenizer | Approximates the Claude 3 tokenizer by inspecting the generation stream | 173 | <https://github.com/javirandor/anthropic-tokenizer> |
| claude-export | Browser script to export Claude.ai chats to Markdown, JSON or PNG | 164 | <https://github.com/ryanschiang/claude-export> |
| gradio-chatbot | Converts Hugging Face Spaces, ModelScope and Gradio chatbots into free APIs | 164 | <https://github.com/weaigc/gradio-chatbot> |
| ModelLink | Local proxy routing third-party models through Claude Desktop | 140 | <https://github.com/Win-Hao/ModelLink> |
| Claude-Conversation-Exporter | Chrome extension for bulk-exporting Claude.ai conversations | 128 | <https://github.com/socketteer/Claude-Conversation-Exporter> |
| reverse-SynthID-text | Reverse engineering Google's SynthID text watermarking | 127 | <https://github.com/aloshdenny/reverse-SynthID-text> |
| snowman | Reimplementation of the Snowboy hotword detection engine | 96 | <https://github.com/Thalhammer/snowman> |
| claude-chromium-native-messaging | Makes Claude in Chrome's native messaging work in Brave, Arc, Vivaldi, Edge | 82 | <https://github.com/stolot0mt0m/claude-chromium-native-messaging> |
| openai-sentinel | Generates ChatGPT/Sora Sentinel and proof-of-work tokens | 78 | <https://github.com/leetanshaj/openai-sentinel> |
| chatgpt-rtl | RTL and UI patcher for the ChatGPT desktop application | 58 | <https://github.com/mmnaderi/chatgpt-rtl> |
| grokipedia-api | Unofficial API for xAI's Grokipedia | 50 | <https://github.com/jasonniebauer/grokipedia-api> |
| wisprflow-sdk | Python SDK over Wispr Flow's reverse-engineered audio transcription API | 15 | <https://github.com/ThisisShashwat/wisprflow-sdk> |
| chatgpt_desktop_ubuntu | Repackages the ChatGPT Windows MSIX as an Ubuntu .deb | 9 | <https://github.com/johnohhh1/chatgpt_desktop_ubuntu> |
| Mnemos | Reverse-engineered Claude Desktop's local storage to add persistent memory | 5 | <https://github.com/foufouadi/Mnemos> |

## System Prompt Leaks & Extractions

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| system-prompts-and-models-of-ai-tools | Extracted system prompts and tool definitions for Cursor, Claude Code, Devin, Windsurf, Kiro, v0, Lovable and more | 143,957 | <https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools> |
| system_prompts_leaks | Archive of extracted system prompts from ChatGPT, Claude, Gemini, Grok and others, per vendor with history | 69,466 | <https://github.com/asgeirtj/system_prompts_leaks> |
| CL4R1T4S | Leaked system prompts and tool specs for ChatGPT, Claude, Gemini, Grok, Perplexity, Cursor, Lovable, Replit and others | 51,156 | <https://github.com/elder-plinius/CL4R1T4S> |
| leaked-system-prompts | Collection of leaked system prompts from LLM-based services, with verifiable sources | 14,962 | <https://github.com/jujumilk3/leaked-system-prompts> |
| claude-code-system-prompts | Claude Code system prompt, builtin tool descriptions and sub-agent prompts extracted per release | 12,888 | <https://github.com/Piebald-AI/claude-code-system-prompts> |
| chatgpt_system_prompt | Collection of extracted GPT system prompts plus prompt injection / prompt leaking techniques | 10,807 | <https://github.com/LouisShark/chatgpt_system_prompt> |
| awesome-ai-system-prompts | Curated collection of system prompts for top AI tools (v0, Manus, Claude Code, ChatGPT, Perplexity) | 6,247 | <https://github.com/dontriskit/awesome-ai-system-prompts> |
| system-prompts-and-models-of-ai-tools-chinese | Chinese translation of extracted prompts from Cursor, Devin, VSCode Agent and other AI coding tools | 1,246 | <https://github.com/IsHexx/system-prompts-and-models-of-ai-tools-chinese> |
| cc | Extracted Claude Code system prompt | 714 | <https://github.com/kn1026/cc> |
| CLAUDE-CODE-SYSTEM-PROMPT | Living document of the extracted Claude Code system prompt | 388 | <https://github.com/elder-plinius/CLAUDE-CODE-SYSTEM-PROMPT> |
| v0prompt | Extracted full system prompt of Vercel v0 | 305 | <https://github.com/sharkqwy/v0prompt> |
| Google-Gemini-System-Prompt | Prompt leak of Google Gemini Pro (Bard version) system prompts, instructions and guidelines | 289 | <https://github.com/elder-plinius/Google-Gemini-System-Prompt> |
| awesome-system-prompts (EliFuzz) | System prompts and tool definitions extracted from AI coding agents (Augment, Claude Code, Cursor, Devin, Kiro) | 278 | <https://github.com/EliFuzz/awesome-system-prompts> |
| awesome-system-prompts (langgptai) | System prompts of LLMs and AI products: DeepSeek, ChatGPT, Gemini, Grok, Qwen | 229 | <https://github.com/langgptai/awesome-system-prompts> |
| apple-intelligence-prompts | Apple Intelligence system prompts extracted from macOS Sequoia | 221 | <https://github.com/Explosion-Scratch/apple-intelligence-prompts> |
| claude-fable-5-system-prompt | Extracted system prompt of Claude Fable 5 | 217 | <https://github.com/KalarisLabs/claude-fable-5-system-prompt> |
| LEAKHUB | Leaderboard and community hub for system prompt leaks | 179 | <https://github.com/elder-plinius/LEAKHUB> |
| leaked-system-prompts (YeeKal) | Leaked system prompts for ChatGPT, Claude, Grok, Gemini, DeepSeek, Manus, v0, Lovable, Cursor | 174 | <https://github.com/YeeKal/leaked-system-prompts> |
| claude-hidden-toolkit | Reverse engineering of Claude.ai's internal tool definitions | 171 | <https://github.com/N1-AI/claude-hidden-toolkit> |
| claude-code-system-prompts | Analysis and documentation of Claude Code's internal prompt architecture | 155 | <https://github.com/lucas-flatwhite/claude-code-system-prompts> |
| claude-code-system-prompt | Dump of the Claude Code system prompt | 154 | <https://github.com/matthew-lim-matthew-lim/claude-code-system-prompt> |
| GPTsSystemPrompts | Database of leaked system instructions for popular custom GPTs in the ChatGPT GPT store | 85 | <https://github.com/0xAb1d/GPTsSystemPrompts> |
| Grok-System-Prompt-Leak | Extracted system prompt of xAI's Grok on X (Twitter) | 72 | <https://github.com/elder-plinius/Grok-System-Prompt-Leak> |
| awesome-llm-system-prompts | System prompts from major LLMs: official releases, leaks and reverse-engineered discoveries | 34 | <https://github.com/ManuelSLemos/awesome-llm-system-prompts> |
| antigravity_prompts | Reverse-engineered prompts and analysis from Google Antigravity | 29 | <https://github.com/tfriedel/antigravity_prompts> |
| claude-system-prompt (zep-us) | Reverse-engineered claude.ai and Claude Code system prompts validated against official ones | 18 | <https://github.com/zep-us/claude-system-prompt> |
| claude-code-system-prompts | Collection of Claude Code system prompts | 16 | <https://github.com/changjonathanc/claude-code-system-prompts> |
| prompt-stash | Cursor internal prompts extracted through MCP | 8 | <https://github.com/maxockner/prompt-stash> |
| claude-code-playbook | Reverse-engineered Claude Code system prompts and prompt-building logic | 4 | <https://github.com/acelest/claude-code-playbook> |
