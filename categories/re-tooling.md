# RE Tooling

[← All categories](../README.md#whats-inside) · [Search this category on the website](https://alexgaoth.github.io/awesome-reverse-engineered/#c=re-tooling) · 1,174 projects · [Listed here? Get the badge](../README.md#is-your-project-listed)

Health: 🟢 pushed in the last year · 🟡 1 to 3 years · 🔴 over 3 years · 🗄️ archived · ⚪ unknown

- [AI-assisted RE](#ai-assisted-re) (179)
- [Binary & Format Analysis](#binary--format-analysis) (174)
- [Decompilation Project Tooling](#decompilation-project-tooling) (89)
- [Disassemblers & Decompilers](#disassemblers--decompilers) (337)
- [Dynamic Instrumentation](#dynamic-instrumentation) (120)
- [Mobile RE](#mobile-re) (187)
- [Other](#other) (26)
- [Traffic Interception](#traffic-interception) (62)

## AI-assisted RE

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [rea](https://github.com/morluto/rea) | Agentic tool to reverse engineer apps from behavior down to native binaries | 413,997 | 🟢 | TypeScript |
| [ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) | MCP bridge between IDA Pro and LLM clients | 13,236 | 🟢 | Python |
| [GhidraMCP](https://github.com/LaurieWired/GhidraMCP) | MCP server exposing Ghidra to LLM clients | 11,672 | 🟢 | Java |
| [universal-modder](https://github.com/rehan-remade/universal-modder) | Skills and tools that let AI coding agents reverse engineer and mod almost any PC game | 9,252 | 🟢 | Python |
| [android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | Claude Code skill for reverse engineering Android apps | 8,585 | 🟢 | Shell |
| [replica-skill](https://github.com/Jakeschincariol/replica-skill) | Claude skills that reverse engineer an app, rebuild it, test it and fix user-reported issues | 6,729 | 🟢 | Python |
| [LeanREA](https://github.com/aicodeking/leanrea) | Agent skill that routes app and binary investigations through command-line RE tools | 3,769 | 🟢 | Python |
| [Gepetto](https://github.com/JusticeRage/Gepetto) | IDA Pro plugin using LLMs to explain and rename decompiled functions | 3,488 | 🟢 | Python |
| [humanify](https://github.com/jehna/humanify) | Renames identifiers in minified JavaScript with LLM-suggested names via AST rewriting | 3,292 | 🟢 | Rust |
| [js-reverse-mcp](https://github.com/zhizhuodemao/js-reverse-mcp) | MCP server for JavaScript reverse engineering with Chrome debugging, breakpoints and network analysis | 3,025 | 🟢 | TypeScript |
| [jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | JADX plugin exposing an MCP server for AI-assisted Android RE | 2,961 | 🟢 | Java |
| [x64dbg-MCP Server](https://github.com/duty1g/x64dbg-mcp-server) | x64dbg plugin written in Zig that serves an MCP endpoint for AI-driven debugging | 2,639 | 🟢 | Zig |
| [reagent](https://github.com/Dryxio/reagent) | Reconstruct and validate C/C++ code from compiled programs with AI | 2,402 | 🟢 | Python |
| [reverse-skills](https://github.com/P4nda0s/reverse-skills) | Reverse engineering skills plugin for Claude Code | 2,337 | 🟢 |  |
| [jshookmcp](https://github.com/vmoranv/jshookmcp) | MCP server with hundreds of tools for agent-driven web and JavaScript reverse engineering | 2,091 | 🟢 | TypeScript |
| [IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP) | Exports IDA Pro databases to files that AI agents can analyze without MCP | 2,073 | 🟢 | Python |
| [Seep Reverse Lab](https://github.com/angusdevgo/Seep-Reverse-Lab) | Agent-driven multi-platform RE workbench for client-side authorization (CWE-602) audits | 1,987 | 🟢 | Lua |
| [Co-op Anything](https://github.com/cranebeaker/coop-anything) | Agent playbook, skills and MCP server for adding online co-op to single-player games | 1,688 | 🟢 | Python |
| [mcp-windbg](https://github.com/svnscha/mcp-windbg) | MCP server that runs Microsoft cdb/kd headless so agents can analyze crash dumps and debug | 1,637 | 🟢 | Python |
| [website-rebuild-skill](https://github.com/boyang-hu/website-rebuild-skill) | Agent skill that rebuilds websites from captured output, including React Server Component streams | 1,595 | 🟢 | JavaScript |
| [ida-mcp](https://github.com/HexRaysSA/ida-mcp) | Official Hex-Rays MCP extension that exposes IDA Pro to AI assistants | 1,490 | 🟢 | Python |
| [WPeGPT](https://github.com/WPeace-HcH/WPeGPT) | IDA plugin for AI-assisted binary analysis with OpenAI and DeepSeek models | 1,422 | 🟢 | Python |
| [hello_js_reverse_skill](https://github.com/WhiteNightShadow/hello_js_reverse_skill) | AI agent skill for JavaScript reverse engineering: crypto recovery, deobfuscation and WASM | 1,386 | 🟢 | Python |
| [open-reverselab](https://github.com/LING71671/open-reverselab) | AI reverse-engineering agent platform and MCP server for Ghidra, Frida, x64dbg, Rizin | 1,327 | 🟢 | Python |
| [Reverify](https://github.com/2akouwu/reverify) | CLI and MCP server that checks a model's claims about a binary against the binary | 1,321 | 🟢 | Python |
| [Kong](https://github.com/amruth-sn/kong) | Agentic, fully automated binary reverse engineering | 1,238 | 🟢 | Python |
| [reverser_ai](https://github.com/mrphrazer/reverser_ai) | Automated reverse engineering assistance with local LLMs (Binary Ninja plugin) | 1,168 | 🟢 | Python |
| [Reverse-Engineer-anything](https://github.com/NabilRFG12/Reverse-Engineer-anything) | Agent-based workflow to reverse engineer app behavior down to native binaries | 1,134 | 🟢 | TypeScript |
| [JSReverser-MCP](https://github.com/NoOne-hub/JSReverser-MCP) | MCP tool for JavaScript reverse engineering in a real browser with breakpoints and script search | 1,043 | 🟢 | TypeScript |
| [firefox-reverse](https://github.com/WhiteNightShadow/firefox-reverse) | Firefox build with an AI agent that traces JS, JSVMP and WASM at the SpiderMonkey engine level | 961 | 🟢 | JavaScript |
| [Eleven](https://github.com/Zfinix/eleven) | Agent-first desktop RE app for Mach-O, ELF and PE binaries, Android packages and GPU code | 941 | 🟢 | TypeScript |
| [ida-mcp-rs](https://github.com/blacktop/ida-mcp-rs) | Headless IDA Pro MCP server written in Rust | 890 | 🟢 | Rust |
| [reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant) | MCP server exposing Ghidra reverse engineering tasks to LLM agents | 886 | 🟢 | Java |
| [GhidraGPT](https://github.com/weirdmachine64/GhidraGPT) | Integrates LLMs into Ghidra for AI-assisted reverse engineering | 836 | 🟢 | Java |
| [unbrowse](https://github.com/unbrowse-ai/unbrowse) | Reverse engineers websites' internal APIs so agents can call them directly | 823 | 🟢 | TypeScript |
| [jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server) | MCP server for the JADX-AI plugin for Android RE | 822 | 🟢 | Python |
| [GhidrAssistMCP](https://github.com/symgraph/GhidrAssistMCP) | MCP server extension for Ghidra | 800 | 🟢 | Java |
| [jadx-gui-ai](https://github.com/cncsnet1/jadx-gui-ai) | jadx-gui decompiler fork with AI-assisted analysis | 788 | 🟢 | Java |
| [GhidrAssist](https://github.com/symgraph/GhidrAssist) | LLM assistant plugin for Ghidra | 774 | 🟢 | Java |
| [AI_JS_DEBUGGER](https://github.com/Valerian7/AI_JS_DEBUGGER) | AI-driven JavaScript reverse engineering tool built on the Chrome DevTools Protocol | 771 | 🟢 | Python |
| [x64DbgMCPServer](https://github.com/AgentSmithers/x64DbgMCPServer) | MCP server for x64dbg | 744 | 🟢 | C# |
| [SpecterOps RE skills](https://github.com/SpecterOps/skills) | Binary Ninja and Ghidra analysis skills for AI agents from SpecterOps | 737 | 🟢 | Python |
| [REA](https://github.com/bbylw/rea-cn) | MCP server for reverse engineering binaries, apps and runtime behavior | 734 | 🟢 | Astro |
| [DAILA](https://github.com/mahaloz/DAILA) | Decompiler-agnostic AI assistant plugin for IDA, Ghidra, Binja and angr | 711 | 🟢 | Python |
| [Rikugan](https://github.com/buzzer-re/Rikugan) | Reverse engineering agent for IDA Pro and Binary Ninja | 703 | 🟢 | Python |
| [js-reverse-automation skill](https://github.com/Fausto-404/js-reverse-automation--skill) | AI skill using chrome-devtools-mcp to automate JavaScript reverse engineering | 609 | 🟢 | Python |
| [0](https://github.com/0sec-labs/0) | AI security harness with web UI, CLI and MCP for code analysis and reverse engineering | 567 | 🟢 | TypeScript |
| [Hermes Agent official plugins](https://github.com/NousResearch/hermes-official-plugins) | Nous Research plugin package for Hermes Agent, including an REA MCP server integration | 556 | 🟢 | Python |
| [x64dbg-mcp](https://github.com/SetsunaYukiOvO/x64dbg-mcp) | x64dbg plugin that lets AI agents control the debugger over MCP | 541 | 🟢 | C++ |
| [re-shell](https://github.com/schlarpc/re-shell) | Nix-powered agentic reverse engineering environment | 536 | 🟢 | Nix |
| [spider-king-skill](https://github.com/aoyunyang/spider-king-skill) | AI skill that reverse engineers web client protocols into Python collectors | 521 | 🟢 | Python |
| [GhidraMCP-AI-rename](https://github.com/guanyue91141/GhidraMCP-AI-rename) | Scripts using GhidraMCP to batch rename and export functions with AI | 497 | 🟢 | Python |
| [r2ai](https://github.com/radareorg/r2ai) | LLM integration for radare2 | 490 | 🟢 | C |
| [ai-reverse-toolkit](https://github.com/zhizhuodemao/ai-reverse-toolkit) | Skills, rules and prompts for AI-assisted reverse engineering | 471 | 🟢 | Python |
| [ida-multi-mcp](https://github.com/MeroZemory/ida-multi-mcp) | Multi-instance IDA Pro MCP server | 468 | 🟢 | Python |
| [OGhidra](https://github.com/llnl/OGhidra) | LLNL plugin that connects Ollama LLMs to Ghidra for AI-driven binary analysis | 464 | 🟢 | Python |
| [pyghidra-mcp](https://github.com/clearbluejar/pyghidra-mcp) | Command-line Python Ghidra MCP server | 457 | 🟢 | Python |
| [binary_ninja_mcp](https://github.com/fosdickio/binary_ninja_mcp) | Binary Ninja plugin with MCP server for LLM clients | 456 | 🟢 | Python |
| [Debin](https://github.com/eth-sri/debin) | Predicts debug information such as names and types in stripped binaries | 454 | 🟡 | Python |
| [Hycli](https://github.com/Hybirdss/Hycli) | Turns website tasks into verified CLI and MCP actions for AI agents | 444 | 🟢 | Rust |
| [idasql](https://github.com/allthingsida/idasql) | SQL interface over IDA Pro databases via live virtual tables for agent-driven RE | 430 | 🟢 | C++ |
| [gpt-wpre](https://github.com/moyix/gpt-wpre) | Whole-program reverse engineering of binaries with GPT-3 summaries of decompiled code | 409 | 🔴 | Python |
| [GptHidra](https://github.com/evyatar9/GptHidra) | Ghidra plugin using ChatGPT to explain functions | 405 | 🔴 | Python |
| [ghidra-rpc](https://github.com/cellebrite-labs/ghidra-rpc) | Ghidra RPC server and agent skill for AI-assisted reverse engineering | 394 | 🟢 | Python |
| [reverse-skill (715494637)](https://github.com/715494637/reverse-skill) | Agent skills for web JS reverse engineering: JSVMP, workers, WASM and webpack | 382 | 🟢 | JavaScript |
| [xbsReverseSkill](https://github.com/lwjjike/xbsReverseSkill) | Modular agent skills for web reverse engineering: AST, algorithms and protocol analysis | 381 | 🟢 | JavaScript |
| [radare2-mcp](https://github.com/radareorg/radare2-mcp) | MCP server that exposes radare2 binary analysis to AI agents | 340 | 🟢 | C |
| [Recurse](https://github.com/Recurse-Labs/recurse) | AI-native IDE for reverse engineering | 296 | 🟢 | Rust |
| [idapromcp_333](https://github.com/namename333/idapromcp_333) | Extended IDA Pro MCP server for AI-assisted reverse engineering | 287 | 🟢 | Python |
| [jshook-skill](https://github.com/wuji66dde/jshook-skill) | AI skill for JS reverse engineering: deobfuscation, crypto detection, CDP debugging and hooks | 271 | 🟢 | TypeScript |
| [ghidra-cli](https://github.com/akiselev/ghidra-cli) | CLI for headless Ghidra analysis and decompilation with JSON output for AI agents | 263 | 🟢 | Rust |
| [jebmcp](https://github.com/flankerhqd/jebmcp) | MCP server for the JEB decompiler | 263 | 🟢 | Python |
| [binary-ninja-headless-mcp](https://github.com/mrphrazer/binary-ninja-headless-mcp) | Headless Binary Ninja MCP server for AI agents | 261 | 🟢 | Python |
| [DecompAI](https://github.com/louisgthier/decompai) | LangGraph agent that disassembles and decompiles uploaded x86 Linux ELF binaries | 243 | 🟢 | Python |
| [RES](https://github.com/alextnetto/res) | Agent skill that documents a SaaS web app's screens, rules, data model and APIs via the browser | 242 | 🟢 | JavaScript |
| [rikune](https://github.com/Last-emo-boy/rikune) | MCP server for Windows binary RE: PE triage, Ghidra analysis and reconstruction | 240 | 🗄️ | TypeScript |
| [CLI-Anything-WEB](https://github.com/ItamarZand88/CLI-Anything-WEB) | Claude Code plugin that generates Python CLIs for web apps by reversing their traffic | 239 | 🟢 | Python |
| [ida_copilot](https://github.com/DearVa/ida_copilot) | ChatGPT agent analysing IDA pseudocode | 235 | 🟡 | Python |
| [ApkMCP-Auto](https://github.com/kggzs/ApkMCP-Auto) | MCP toolkit for Android reverse engineering | 228 | 🟢 | Python |
| [bn](https://github.com/banteg/bn) | Binary Ninja CLI for coding agents | 219 | 🟢 | Python |
| [Reversecore_MCP](https://github.com/sjkim1127/Reversecore_MCP) | MCP server that lets AI agents run reverse engineering and binary analysis tools | 215 | 🟢 | Python |
| [BINNY](https://github.com/openbin-ai/binny) | Terminal agent harness that runs hosted or local models over binary-analysis tools | 212 | 🟢 | Go |
| [Nero](https://github.com/tech-srl/Nero) | Neural reverse engineering of stripped binaries via augmented control flow graphs | 208 | 🔴 | Python |
| [RevEng.AI Ghidra plugin](https://github.com/RevEngAI/plugin-ghidra) | Ghidra plugin for RevEng.AI function similarity, recovered names and AI explanations | 201 | 🟢 | Java |
| [ghidra-headless-mcp](https://github.com/mrphrazer/ghidra-headless-mcp) | Headless Ghidra MCP server for AI agents | 196 | 🟢 | Python |
| [console-skill](https://github.com/Jakeschincariol/console-skill) | Claude skills that port PS2 games you own to PC | 195 | 🟢 | Python |
| [DIRTY](https://github.com/CMUSTRUDEL/DIRTY) | Neural model that augments decompiler output with learned variable names and types | 191 | 🔴 | Python |
| [re-skill](https://github.com/vgrichina/re-skill) | Claude Code skill for reverse engineering retro games | 181 | 🟢 | Shell |
| [HopperMCP](https://github.com/MxIris-Reverse-Engineering/HopperMCP) | MCP server for Hopper Disassembler | 163 | 🗄️ | Objective-C |
| [RevEng.AI IDA plugin](https://github.com/RevEngAI/plugin-ida) | IDA Pro plugin for RevEng.AI function similarity and AI-assisted analysis | 163 | 🟢 | Python |
| [GhidrOllama](https://github.com/lr-m/GhidrOllama) | Ghidra script analysing functions with local Ollama LLMs | 156 | 🟡 | Python |
| [GhidraChatGPT](https://github.com/likvidera/GhidraChatGPT) | Brings ChatGPT into Ghidra | 151 | 🗄️ | Java |
| [oneiromancer](https://github.com/0xdea/oneiromancer) | Reverse engineering assistant using a local LLM to analyse pseudocode | 146 | 🟢 | Rust |
| [decyx](https://github.com/philsajdak/decyx) | AI-powered Ghidra extension | 140 | 🟢 | Python |
| [ai-code-decompile](https://github.com/zhongguagua/ai-code-decompile) | AI and AST based JavaScript decompiler and deobfuscator for built bundles | 139 | 🟢 | TypeScript |
| [ReSym](https://github.com/lt-asset/resym) | LLM-based recovery of variable and data structure symbols in stripped binaries | 139 | 🟡 | Makefile |
| [x64dbg_mcp](https://github.com/bromoket/x64dbg_mcp) | MCP server for the x64dbg debugger for AI-assisted reverse engineering | 137 | 🟢 | C++ |
| [polar](https://github.com/ant4g0nist/polar) | LLDB plugin bringing LLMs to LLDB | 132 | 🟡 | Python |
| [DeGPT](https://github.com/PeiweiHu/DeGPT) | Optimizes decompiler output with an LLM (NDSS 2024) | 131 | 🟡 | Python |
| [claude-reverse-skills](https://github.com/haikow/claude-reverse-skills) | Claude Code reverse engineering skills (APK, IDA, radare2, JS) with IDA MCP | 130 | 🟢 | PowerShell |
| [DecompilerServer](https://github.com/pardeike/DecompilerServer) | MCP server for decompiling and analysing .NET assemblies | 126 | 🟢 | C# |
| [ida-re-mcp](https://github.com/yexi-by/ida-re-mcp) | stdio MCP server for IDA Pro 9.3+ reverse engineering | 122 | 🟢 | Python |
| [metis-reverse](https://github.com/Wholiver/metis-reverse) | AI-assisted deterministic reverse engineering FastMCP server | 122 | 🟢 | Python |
| [REA Reconstruction Companion](https://github.com/ShadowSwaps/REA-Reconstruction-Companion) | Teaching case and companion for REA-assisted reconstruction of a small command-line app | 122 | 🟢 | JavaScript |
| [iOS-reverse-engineering-claude-skill](https://github.com/incogbyte/iOS-reverse-engineering-claude-skill) | Claude Code skill to extract and reverse engineer iOS apps | 118 | 🟢 | Shell |
| [windbg-decompile-ext](https://github.com/kernullist/windbg-decompile-ext) | WinDbg extension that disassembles live functions and decompiles with an LLM | 112 | 🟢 | C++ |
| [kernagent](https://github.com/Karib0u/kernagent) | Headless AI agent for deterministic reverse engineering | 103 | 🟢 | Python |
| [mcp-server-idapro](https://github.com/fdrechsler/mcp-server-idapro) | MCP server letting AI assistants interact with IDA Pro | 103 | 🟡 | Python |
| [dsh-rea (Fanqi89)](https://github.com/Fanqi89/dsh-rea) | REA MCP bridge plugin for DeepSeek Harness | 94 | 🟢 | PowerShell |
| [revula](https://github.com/president-xd/revula) | Reverse engineering MCP server | 85 | 🟢 | Python |
| [IDA-Assistant](https://github.com/stuxnet147/IDA-Assistant) | IDA plugin for automatic AI-assisted reverse engineering | 82 | 🟡 | Python |
| [r0idamcp](https://github.com/r0ysue/r0idamcp) | SSE MCP server plugin for IDA Pro | 82 | 🟡 | Python |
| [algokiller-plugin](https://github.com/icloudza/algokiller-plugin) | ARM64 trace analysis and cipher algorithm recovery plugin for Claude Desktop | 80 | 🟢 | Python |
| [MirrorCode](https://github.com/epoch-research/MirrorCode) | Benchmark of AI agents rebuilding whole programs from observed behavior alone | 79 | 🟢 | C |
| [Ryuumonbuchi](https://github.com/elliottophellia/Ryuumonbuchi) | Headless Ghidra MCP server | 79 | 🟢 | Python |
| [binaryninja-openai](https://github.com/WhatTheFuzz/binaryninja-openai) | Integrates OpenAI with Binary Ninja | 77 | 🟡 | Python |
| [ILSpy-Mcp](https://github.com/bivex/ILSpy-Mcp) | MCP server exposing ILSpy .NET decompilation to AI assistants | 76 | 🟢 | C# |
| [VarBERT](https://github.com/sefcom/VarBERT) | Predicts variable names in decompiled code with a BERT model | 69 | 🟢 | Python |
| [BinAssist](https://github.com/symgraph/BinAssist) | Binary Ninja plugin providing LLM assistance | 68 | 🟢 | Python |
| [recopilot](https://github.com/XingTuLab/recopilot) | ReCopilot reverse engineering copilot for binary analysis | 66 | 🟢 | Python |
| [SymLM](https://github.com/OSUSecLab/SymLM) | Predicts function names in stripped binaries from context-sensitive semantics | 64 | 🟡 | Python |
| [super-trouper](https://github.com/crissyfield/super-trouper) | MCP server exposing Frida dynamic instrumentation to AI agents | 62 | 🟢 | Go |
| [x64dbg-rippy](https://github.com/dariushoule/x64dbg-rippy) | AI reverse engineering assistant chat panel for x64dbg | 62 | 🟢 | C++ |
| [Vibe-Reverse-Engineering](https://github.com/Ekozmaster/Vibe-Reverse-Engineering) | LLM-friendly tools for Cursor to reverse engineer binaries, especially games | 61 | 🟢 | C++ |
| [DeepExtractIDA](https://github.com/marcosd4h/DeepExtractIDA) | IDA Pro plugin and batch extractor that turns Windows PE files into material for AI agents | 59 | 🟢 | Python |
| [game-client-to-server-reverse](https://github.com/ShrugYu/game-client-to-server-reverse) | Agent skill that infers a game's server protocol from its client and rebuilds a deployable server | 59 | 🟢 | Python |
| [dsh-plugin-rea](https://github.com/czcdr/dsh-plugin-rea) | Adapter that brings the REA MCP server into DeepSeek Harness | 56 | 🟢 | JavaScript |
| [ida-free-mcp](https://github.com/0xshlomil/ida-free-mcp) | Native MCP bridge for IDA Free, used as an REA provider | 49 | 🟢 | C++ |
| [SymGen](https://github.com/OSUSecLab/SymGen) | Generative model that infers function names in stripped binaries | 46 | 🟡 | Python |
| [DIRE](https://github.com/pcyin/dire) | Neural variable renaming for decompiled binaries | 45 | 🔴 | Python |
| [windbg-mcp](https://github.com/memoryforensics1/windbg-mcp) | C# MCP server for kernel and user-mode Windows debugging via DbgEng, TTD and Frida | 44 | 🟢 | C# |
| [Reverse-engineering-agent](https://github.com/The-Arabi/Reverse-engineering-agent) | MCP server giving AI agents 46 RE tools (Ghidra, GDB, Binwalk) | 38 | 🟢 | Python |
| [grokathon (Nova)](https://github.com/theodorechapman/grokathon) | Grok Build harness that reverse engineers old binaries; Grokathon winner | 37 | 🟢 | Python |
| [renderdoc-mcp](https://github.com/scarletfantasy/renderdoc-mcp) | MCP server that exposes RenderDoc frame captures, pipelines and shaders to AI agents | 31 | 🟢 | Python |
| [reu](https://github.com/rancy777/reu) | Evidence-driven reverse engineering and unpacking workflows for AI agents | 31 | 🟢 | Python |
| [ReverseLoom](https://github.com/KuiChi-x/reverseloom) | AI browser agent that turns websites into browser-free API clients | 31 | 🟢 | Python |
| [vmp-reverse-skill](https://github.com/wul7chaos/vmp-reverse-skill) | Devirtualization pipeline for VMProtect-style binaries with P-code IR and LLM assistance | 29 | 🟢 | Python |
| [DecompileBench](https://github.com/vul337/DecompileBench) | Benchmark for evaluating decompilers on real-world code | 27 | 🟡 | C |
| [Idioms](https://github.com/squaresLab/idioms) | Framework for local neural decompilation that recovers code and user-defined types | 27 | 🟢 | Python |
| [JsDeObsBench](https://github.com/Ch3nYe/JsDeObsBench) | Benchmark of LLMs on JavaScript deobfuscation | 27 | 🟡 | JavaScript |
| [romdev](https://github.com/monteslu/romdev) | Tool server for agents doing homebrew ROM development and romhacking on 18 retro platforms | 27 | 🟢 | JavaScript |
| [copyapp](https://github.com/everettjf/copyapp) | Analyzes iOS and macOS apps and builds and verifies independent implementations of their behavior | 26 | 🟢 | Python |
| [reverse-engineer-everything](https://github.com/gryszzz/reverse-engineer-everything) | Local workbench for evidence-backed software investigation built on the REA engine | 25 | 🟢 | TypeScript |
| [CREBench](https://github.com/wangyu-ovo/CREBench) | Benchmark of LLMs on cryptographic binary reverse engineering | 24 | 🟢 | Standard ML |
| [claude-reverse-engineering-skill](https://github.com/EncidXVII/claude-reverse-engineering-skill) | Claude agent skill for binary triage, headless exports and evidence-based RE reports | 22 | 🟢 | Python |
| [ERA](https://github.com/dav1dngy/era-agent) | Evidence-driven AI reverse engineering agent with a self-improvement lab | 22 | 🟢 | JavaScript |
| [diaphora-mcp](https://github.com/xTeardx/diaphora-mcp) | MCP server for automated binary diffing with Diaphora | 20 | 🟢 | Python |
| [QNX-Agent](https://github.com/Shiyou-Qi/QNX-Agent) | Reverse engineering agent presets for DeepSeek Harness | 20 | 🟢 | Python |
| [XFL](https://github.com/lmu-plai/xfl) | Names functions in binaries with extreme multi-label learning | 20 | 🟢 | Python |
| [FidelityGPT](https://github.com/ZhouZhiping045/FidelityGPT) | Corrects decompilation distortions with retrieval-augmented LLM prompts | 19 | 🟡 | Python |
| [REAgraph](https://github.com/Graphify-Labs/REAgraph) | Persistent graph memory and structural diff for REA reverse engineering findings | 19 | 🟢 | Python |
| [deobfuscate-mcp-server](https://github.com/MadeByTokens/deobfuscate-mcp-server) | MCP server helping LLMs reverse-engineer minified JavaScript | 18 | 🟢 | TypeScript |
| [rea-python](https://github.com/kandada/rea-python) | Unofficial Python port of the REA reverse engineering agent toolkit | 18 | 🟢 | Python |
| [asmsense](https://github.com/krxi/asmsense) | Small model that names and describes functions in stripped x86-64 binaries, with open dataset | 17 | 🟢 | Python |
| [retro-port](https://github.com/Dhaiwat10/retro-port) | Claude Code skill that ports old Windows games to the browser via static recompilation to WebAssembly | 17 | 🟢 | C |
| [XYREVERSE](https://github.com/nesaon03/XYREVERSE) | Agent skill pack for reverse engineering with IDA, Ghidra, Frida, x64dbg and REA | 16 | 🟢 |  |
| [2api-skill](https://github.com/69gg/2api-skill) | Agent skill to reverse-engineer any webchat into an OpenAI/Anthropic API | 15 | 🟢 | Python |
| [rea-agent-docker](https://github.com/alexmi256/rea-agent-docker) | Docker images for REA with Ghidra, Hopper or IDA analysis engines | 14 | 🟢 | Shell |
| [C64ReverseEngineeringMCP](https://github.com/Jondalar/C64ReverseEngineeringMCP) | MCP server for C64 reverse engineering: disassembly and semantic analysis | 13 | 🟢 | TypeScript |
| [GenNm](https://github.com/XZ-X/gennm-ndss-ae) | Generative model that recovers variable names in stripped binaries (NDSS artifact) | 13 | 🟢 | Python |
| [rc-devtools-mcp](https://github.com/reverse-craft/rc-devtools-mcp) | MCP server for browser debugging and web reverse engineering by AI agents | 13 | 🟢 | TypeScript |
| [decomp-goal-harness](https://github.com/Muhtasham/decomp-goal-harness) | Harness for coding agents working on matching decompilation goals | 10 | 🟢 | Python |
| [revenant](https://github.com/DatanoiseTV/revenant) | LLM-powered reverse engineering engine for vendor-abandoned hardware and software | 10 | 🟢 | Python |
| [Corvus](https://github.com/Albasha0x0/Corvus) | MCP server for AI agents: .NET and native PE/ELF/Mach-O analysis and decompilation | 9 | 🟢 | C# |
| [GameOfflinerSkill](https://github.com/LunarConcerto/GameOfflinerSkill) | Agent skill for reviving shut-down online games against a self-hosted server | 9 | 🟢 |  |
| [ghidra-llm-pipeline](https://github.com/HappyTotoro116/ghidra-llm-pipeline) | PyGhidra extraction and local LLM pipeline for C reimplementation of binaries | 9 | 🟢 | Python |
| [x64dbg-mcp](https://github.com/ouonet/x64dbg-mcp) | MCP server for x64dbg reverse engineering and debugging | 8 | 🟢 | TypeScript |
| [rea-safe-agents](https://github.com/dagoSte/rea-safe-agents) | Contained static analysis with REA, Ghidra and JADX in restricted Docker containers | 7 | 🟢 | Python |
| [ReaFuse](https://github.com/sickpyramid/ReaFuse) | Tool built on REA that dissects two JS/TS projects and fuses their capabilities | 7 | 🟢 | JavaScript |
| [MCP-UAsset-Toolkit](https://github.com/ShadowNineX/MCP-UAsset-Toolkit) | MCP tools that automate Unreal Engine asset reverse engineering with UAsset API and CUE4Parse | 6 | 🟢 | C# |
| [bsu-tool](https://github.com/bsu-tool/bsu-tool) | AI-assisted USB protocol analysis tool and MCP server | 5 | 🟢 | Python |
| [clean-roomer](https://github.com/osi1880vr/clean-roomer) | Skill set for LLMs to produce clean-room implementations of existing tools | 5 | 🟢 | Python |
| [PistonDecompiler](https://github.com/AlexProgrammerDE/PistonDecompiler) | Persistent AI-assisted binary analysis with Ghidra and a web workbench | 5 | 🟢 | Rust |
| [Reverseport](https://github.com/laaielichter/Reverseport) | CLI and MCP server for porting reverse-engineering results to Godot, Unity, Unreal and three.js | 5 | 🟢 | TypeScript |
| [rea-casebook](https://github.com/pablodiazjorge/rea-casebook) | Claude Code mod that collects REA evidence, tracks unknowns and records cited findings | 4 | 🟢 | TypeScript |
| [rea-jev](https://github.com/juan-viox/rea-jev) | Claude Code plugin that adds routing and evidence checks around the REA MCP integration | 3 | 🟢 | JavaScript |
| [usb-rea](https://github.com/emirmrkaljevic/usb-rea) | Infers USB device protocols from labelled captures and generates pyusb drivers and dissectors | 2 | 🟢 | Python |
| [mcp_reverse_engineering](https://github.com/daedalus/mcp_reverse_engineering) | MCP server exposing reverse engineering tools | 1 | 🟢 | Python |
| [DAITK](https://github.com/Grien25/DAITK) | AI-assisted GameCube decompilation pipeline with objdiff verification | 0 | 🟡 | Assembly |

## Binary & Format Analysis

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Detect-It-Easy](https://github.com/horsicq/Detect-It-Easy) | Program for determining file types, compilers and packers | 11,835 | 🟢 | JavaScript |
| [capa](https://github.com/mandiant/capa) | FLARE tool that identifies capabilities in executable files | 6,289 | 🟢 | Python |
| [LIEF](https://github.com/lief-project/LIEF) | Library to parse and modify ELF, PE and Mach-O binaries | 5,616 | 🟢 | C++ |
| [binsider](https://github.com/orhun/binsider) | Terminal UI to analyze ELF binaries | 4,504 | 🟢 | Rust |
| [FLOSS](https://github.com/mandiant/flare-floss) | Extracts obfuscated, stack and tight strings from malware binaries | 4,206 | 🟢 | Python |
| [PE-sieve](https://github.com/hasherezade/pe-sieve) | Scans a running process for injected or modified code and dumps it | 3,934 | 🟢 | C++ |
| [PE-bear](https://github.com/hasherezade/pe-bear) | Multiplatform PE file reversing tool | 3,871 | 🟢 | C++ |
| [DIE-engine](https://github.com/horsicq/DIE-engine) | Detect It Easy engine for identifying file types, packers and compilers | 3,330 | 🟢 | C++ |
| [rehex](https://github.com/solemnwarning/rehex) | Reverse-engineers' hex editor with structure annotation | 2,483 | 🟢 | C++ |
| [pefile](https://github.com/erocarrera/pefile) | Python module to read and work with PE files | 2,081 | 🟢 | Python |
| [bincat](https://github.com/airbus-seclab/bincat) | Static binary analyser with value/taint analysis and type reconstruction for IDA | 1,881 | 🟡 | OCaml |
| [pharos](https://github.com/cmu-sei/pharos) | Automated static analysis tools for binary programs | 1,739 | 🟢 | C++ |
| [pbtk](https://github.com/marin-m/pbtk) | Toolset to extract .proto definitions from apps and fuzz Protobuf-based endpoints | 1,695 | 🟢 | Python |
| [BinAbsInspector](https://github.com/KeenSecurityLab/BinAbsInspector) | Ghidra-based static vulnerability scanner for binaries using abstract interpretation | 1,684 | 🟡 | Java |
| [VTIL-Core](https://github.com/vtil-project/VTIL-Core) | Intermediate language and optimizer for devirtualizing and deobfuscating binaries | 1,617 | 🟢 | C++ |
| [XELFViewer](https://github.com/horsicq/XELFViewer) | ELF file viewer and editor | 1,589 | 🟢 | C++ |
| [ngrev](https://github.com/mgechev/ngrev) | Tool for reverse engineering the structure of Angular applications | 1,572 | 🔴 | TypeScript |
| [goblin](https://github.com/m4b/goblin) | Cross-platform Rust crate to parse ELF, PE, Mach-O and archive binaries | 1,559 | 🟢 | Rust |
| [VMProtect-devirtualization](https://github.com/JonathanSalwan/VMProtect-devirtualization) | Automatic deobfuscation of VMProtect-protected functions with symbolic execution and LLVM | 1,543 | 🔴 | Roff |
| [cwe_checker](https://github.com/fkie-cad/cwe_checker) | Ghidra-based tool that finds vulnerable patterns (CWEs) in binary executables | 1,363 | 🟢 | Rust |
| [binocle](https://github.com/sharkdp/binocle) | Graphical tool to visualize binary data | 1,327 | 🟡 | Rust |
| [XPEViewer](https://github.com/horsicq/XPEViewer) | PE file viewer and editor | 1,244 | 🟢 | QMake |
| [Veles](https://github.com/codilime/veles) | Binary data visualization and analysis tool | 1,239 | 🗄️ | C++ |
| [PE Tools](https://github.com/petoolse/petools) | Portable executable (PE) manipulation toolkit | 1,204 | 🟡 |  |
| [e9patch](https://github.com/GJDuck/e9patch) | Static binary rewriting tool for x86-64 ELF binaries | 1,161 | 🟢 | C |
| [AsmResolver](https://github.com/Washi1337/AsmResolver) | Library for reading, editing and writing PE files and .NET modules | 1,135 | 🟢 | C# |
| [protobuf-inspector](https://github.com/mildsunrise/protobuf-inspector) | Tool to reverse engineer Protocol Buffers messages with unknown definitions | 1,130 | 🔴 | Python |
| [GoReSym](https://github.com/mandiant/GoReSym) | Recovers Go build metadata, function names, line tables and types from binaries | 1,121 | 🟢 | Go |
| [HexWalk](https://github.com/gcarmix/HexWalk) | Hex viewer, editor and analyzer with binwalk integration | 1,028 | 🟢 | C++ |
| [XMachOViewer](https://github.com/horsicq/XMachOViewer) | Mach-O file viewer for Windows, Linux and macOS | 970 | 🟢 | C++ |
| [WpfHexEditor Studio](https://github.com/abbaye/WpfHexEditorIDE) | WPF/.NET hex editor IDE for binary analysis with .NET assembly inspection | 939 | 🟢 | C# |
| [Tigress_protection](https://github.com/JonathanSalwan/Tigress_protection) | Symbolic-execution deobfuscation of Tigress-protected binaries and its RE challenges | 931 | 🟡 | LLVM |
| [Mergen](https://github.com/NaC-L/Mergen) | Deobfuscation via LLVM IR optimization of lifted assembly | 920 | 🟢 | C++ |
| [PDBRipper](https://github.com/horsicq/PDBRipper) | Extracts type and symbol information from PDB files | 908 | 🟢 | C++ |
| [biodiff](https://github.com/8051Enthusiast/biodiff) | Hex diff viewer using sequence alignment algorithms | 896 | 🟡 | Rust |
| [VulHunt](https://github.com/vulhunt-re/vulhunt) | Binarly vulnerability detection framework for binaries and firmware | 896 | 🟢 | C++ |
| [hal](https://github.com/emsec/hal) | Hardware netlist reverse engineering and analysis framework | 841 | 🟢 | C++ |
| [readpe](https://github.com/mentebinaria/readpe) | PE file analysis toolkit | 793 | 🟢 | C |
| [hobbits](https://github.com/Mahlet-Inc/hobbits) | Multi-platform GUI for bit-level analysis and visualization of data | 755 | 🟡 | Python |
| [retrowrite](https://github.com/HexHive/retrowrite) | Static binary rewriting to retrofit compiler passes into binaries | 755 | 🟡 | Python |
| [malcontent](https://github.com/chainguard-dev/malcontent) | Chainguard tool that detects supply-chain compromise behaviors in binaries | 680 | 🟢 | Go |
| [fickling](https://github.com/trailofbits/fickling) | Python pickle decompiler and static analyzer | 676 | 🟢 | Python |
| [JSIR](https://github.com/google/jsir) | Google JavaScript analysis IR used for LLM-powered deobfuscation (CASCADE) | 676 | 🟢 | C++ |
| [pigaios](https://github.com/joxeankoret/pigaios) | Matches and diffs source code directly against binaries | 651 | 🔴 | Python |
| [machoexplorer](https://github.com/everettjf/machoexplorer) | Mach-O file explorer for macOS and Windows | 645 | 🟢 | C++ |
| [Kam1n0-Community](https://github.com/McGill-DMaS/Kam1n0-Community) | Assembly code clone search and analysis platform | 627 | 🔴 | C |
| [AngryGhidra](https://github.com/Nalen98/AngryGhidra) | Ghidra plugin that runs angr symbolic execution | 623 | 🟡 | Java |
| [binlex](https://github.com/c3rb3ru5d3d53c/binlex) | Binary genetic traits lexer framework for function similarity | 606 | 🟢 | Rust |
| [binglide](https://github.com/wapiflapi/binglide) | Visual reverse engineering tool that plots binary data patterns | 594 | 🔴 | Python |
| [Falcon](https://github.com/falconre/falcon) | Binary analysis framework in Rust | 592 | 🟢 | Rust |
| [Nauz-File-Detector](https://github.com/horsicq/Nauz-File-Detector) | Linker, compiler and tool detector for binaries | 586 | 🟢 | C++ |
| [ERESI](https://github.com/thorkill/eresi) | ERESI reverse engineering software interface for ELF binaries | 577 | 🔴 | C |
| [sasquatch](https://github.com/devttys0/sasquatch) | Patched unsquashfs that handles vendor-modified SquashFS images | 569 | 🔴 | Shell |
| [pixd](https://github.com/FireyFly/pixd) | Colourful visualization tool for binary files | 564 | 🟡 | C |
| [fuzzable](https://github.com/ex0dus-0x/fuzzable) | Static-analysis framework to find fuzzable targets in binaries | 549 | 🟢 | Python |
| [Sibyl](https://github.com/cea-sec/Sibyl) | Miasm-based function divination to identify known functions in binaries | 545 | 🔴 | Python |
| [ktool](https://github.com/0cyn/ktool) | pip install k2l \| Mach-O + Obj-C analysis TUI / CLI kit and library. Zero compiled deps, runs anywhere with a python... | 526 | 🟢 | Python |
| [OpenREIL](https://github.com/Cr4sh/openreil) | Translator and tools for REIL, the Reverse Engineering Intermediate Language | 511 | 🗄️ | C |
| [amoco](https://github.com/bdcht/amoco) | Python framework for static symbolic binary analysis | 493 | 🟡 | Python |
| [SHAREM](https://github.com/Bw3ll/sharem) | Shellcode analysis framework that emulates Windows APIs and syscalls | 492 | 🟢 | Python |
| [pdb](https://github.com/getsentry/pdb) | Rust parser for Microsoft PDB (Program Database) debug information | 468 | 🟢 | Rust |
| [debloat](https://github.com/Squiblydoo/debloat) | GUI and CLI tool that removes bloat padding from executables for analysis | 458 | 🟢 | Python |
| [ollvm-breaker](https://github.com/amimo/ollvm-breaker) | Binary Ninja script that removes OLLVM control-flow flattening | 447 | 🔴 | Python |
| [Fhex](https://github.com/echo-devim/fhex) | Cross-platform hex editor with disassembler and assembler support | 436 | 🟡 | C++ |
| [VmpHelper](https://github.com/fjqisba/VmpHelper) | IDA plugin that decompiles VMProtect-virtualized code | 418 | 🟢 | C++ |
| [lscan](https://github.com/maroueneboubakri/lscan) | Library identification tool for statically linked stripped binaries | 409 | 🔴 | Max |
| [Cerberus](https://github.com/h311d1n3r/Cerberus) | Unstrips Rust and Go binaries (ELF and PE) | 407 | 🟡 | C++ |
| [pe](https://github.com/saferwall/pe) | Go package to parse and analyze PE files | 397 | 🟢 | Go |
| [idenLib](https://github.com/secrary/idenLib) | Library function identification for stripped binaries | 395 | 🔴 | C++ |
| [windiff](https://github.com/ergrelet/windiff) | Compare symbols, types and syscalls across Windows builds | 395 | 🟢 | Rust |
| [knife](https://github.com/bl4ckr0ss3/knife) | Terminal-first Rust RE toolkit for PE/ELF/Mach-O analysis via CLI, TUI and MCP | 384 | 🟢 | Rust |
| [gtirb](https://github.com/GrammaTech/gtirb) | Intermediate representation for binary analysis and rewriting | 382 | 🟢 | C++ |
| [UE Explorer](https://github.com/UE-Explorer/UE-Explorer) | Browser and decompiler for Unreal Engine packages and UnrealScript classes | 377 | 🟢 | C# |
| [resym](https://github.com/ergrelet/resym) | Browse and extract C/C++ type declarations from PDB files | 374 | 🟡 | Rust |
| [hexerator](https://github.com/crumblingstatue/hexerator) | GUI hex editor focused on binary file exploration and pattern recognition | 372 | 🟢 | Rust |
| [CoBRA](https://github.com/trailofbits/CoBRA) | Mixed Boolean-Arithmetic expression deobfuscation via coefficient reconstruction | 362 | 🟢 | C++ |
| [sass-king](https://github.com/florianmattana/sass-king) | Reverse engineered NVIDIA SASS instruction dictionary and kernel audit patterns across GPU architectures | 350 | 🟢 | Cuda |
| [PEiD (app-peid)](https://github.com/wolfram77web/app-peid) | PEiD detector for packers, cryptors and compilers in PE files | 347 | 🔴 | HTML |
| [HexPatch](https://github.com/Etto48/HexPatch) | Rust TUI binary patcher and hex editor with disassembly for ELF, PE and Mach-O | 337 | 🟢 | Rust |
| [cc-reverse](https://github.com/Crain99/cc-reverse) | Reverse engineering tool that restores Cocos Creator game builds to projects | 335 | 🟢 | JavaScript |
| [evbunpack](https://github.com/mos9527/evbunpack) | Enigma Virtual Box unpacker | 333 | 🗄️ | Python |
| [dynStruct](https://github.com/ampotos/dynStruct) | DynamoRIO-based tool for automatic structure recovery | 330 | 🔴 | C |
| [D810-ng](https://github.com/w00tzenheimer/d810-ng) | IDA Pro plugin that deobfuscates code at decompilation time | 328 | 🟢 | Python |
| [dnpatch](https://github.com/ioncodes/dnpatch) | .NET patcher library built on dnlib | 328 | 🔴 | C# |
| [Kaitai Struct Web IDE](https://github.com/kaitai-io/kaitai_struct_webide) | Browser IDE for writing and testing Kaitai Struct format specs | 319 | 🟢 | TypeScript |
| [ghidra-findcrypt](https://github.com/TorgoTorgo/ghidra-findcrypt) | Ghidra plugin that locates cryptographic constants | 302 | 🔴 | Java |
| [BinDiffHelper](https://github.com/ubfx/BinDiffHelper) | Ghidra extension integrating BinDiff function matching | 298 | 🟢 | Java |
| [regenny](https://github.com/cursey/regenny) | Interactive tool to reconstruct structures and generate C headers while reverse engineering | 297 | 🟢 | C++ |
| [hexabyte](https://github.com/thetacom/hexabyte) | Modular TUI hex editor with binary diffing | 295 | 🟢 | Python |
| [veles](https://github.com/wapiflapi/veles) | Visual binary analysis and reverse engineering tool | 287 | 🔴 | C++ |
| [ollvm-unflattener](https://github.com/cdong1012/ollvm-unflattener) | Deobfuscator for Obfuscator-LLVM control-flow flattening | 284 | 🟡 | Python |
| [MachOKit](https://github.com/p-x9/MachOKit) | Swift library for parsing Mach-O files | 282 | 🟢 | Swift |
| [SWFREtools](https://github.com/sporst/SWFREtools) | Tools for reverse engineering Flash SWF files | 278 | 🔴 | Java |
| [ApiScout](https://github.com/danielplohmann/apiscout) | Recovers Windows API imports from arbitrary memory dumps | 270 | 🔴 | Python |
| [macaw](https://github.com/GaloisInc/macaw) | Open source binary analysis and symbolic execution tools | 258 | 🟢 | Haskell |
| [senseye](https://github.com/letoram/senseye) | Dynamic visual debugging and data reverse engineering tool suite | 253 | 🔴 |  |
| [GAMBA](https://github.com/DenuvoSoftwareSolutions/GAMBA) | Simplifier for general mixed Boolean-arithmetic (MBA) obfuscated expressions | 251 | 🟡 | Python |
| [qbindiff](https://github.com/quarkslab/qbindiff) | Binary diffing framework | 248 | 🟡 | Python |
| [quokka](https://github.com/quarkslab/quokka) | Fast and accurate binary exporter from IDA | 229 | 🟢 | Python |
| [Shiva](https://github.com/advanced-microcode-patching/shiva) | Custom ELF linker/loader that installs ET_REL binary patches at runtime | 228 | 🟢 | C |
| [VMAttack (.NET)](https://github.com/void-stack/VMAttack) | Research on devirtualizing .NET code virtualization protectors | 224 | 🔴 | C# |
| [dz6](https://github.com/mentebinaria/dz6) | Vim-inspired terminal hex editor | 217 | 🟢 | Rust |
| [HexCtrl](https://github.com/jovibor/HexCtrl) | Fully featured GUI hex control for Windows (MFC) | 216 | 🟢 | C++ |
| [SiMBA](https://github.com/DenuvoSoftwareSolutions/SiMBA) | Efficient deobfuscation of linear mixed Boolean-arithmetic expressions | 199 | 🔴 | Python |
| [jTrans](https://github.com/vul337/jTrans) | Jump-aware transformer for binary code similarity detection | 196 | 🟡 | Python |
| [hexd](https://github.com/FireyFly/hexd) | Colour hexdump tool for inspecting binary files | 192 | 🟡 | C |
| [javascript-deobfuscator](https://github.com/LostMyCode/javascript-deobfuscator) | Deobfuscator for JavaScript produced by obfuscator.io | 191 | 🟡 | JavaScript |
| [fugue-core](https://github.com/fugue-re/fugue-core) | Binary analysis framework written in Rust | 185 | 🟢 | Rust |
| [Pepper](https://github.com/jovibor/Pepper) | PE32/PE32+ binary analysis tool and resource viewer | 179 | 🟢 | C++ |
| [degate](https://github.com/nitram2342/degate) | Open source software for chip reverse engineering from die images | 175 | 🗄️ | C++ |
| [qiew](https://github.com/mtivadar/qiew) | Hex/file format viewer for reverse engineering | 175 | 🟢 | Python |
| [delsum](https://github.com/8051Enthusiast/delsum) | Checksum reverse engineering toolbox that finds checksum parameters from samples | 168 | 🟡 | Rust |
| [Stadeo](https://github.com/eset/stadeo) | Control-flow-flattening and string deobfuscator | 165 | 🔴 | Python |
| [idbutil](https://github.com/nlitsme/idbutil) | Library and tool for reading IDA Pro databases | 164 | 🟢 | C++ |
| [pyidbutil](https://github.com/nlitsme/pyidbutil) | Python library for reading IDA Pro databases | 161 | 🟢 | Python |
| [resource_dasm](https://github.com/fuzziqersoftware/resource_dasm) | Classic Mac OS resource fork decoder and 68K/PPC disassembler with format-specific RE tools | 159 | 🟢 | C++ |
| [rematch](https://github.com/nirizr/rematch) | Open binary diffing framework | 156 | 🔴 | Python |
| [bcov](https://github.com/abenkhadra/bcov) | Static binary instrumentation for coverage analysis | 153 | 🔴 | C++ |
| [uniref](https://github.com/in1nit1t/uniref) | Python framework for analyzing Unity applications | 153 | 🟡 | Python |
| [obfDetect](https://github.com/mcdulltii/obfDetect) | IDA plugin that pinpoints obfuscated code | 145 | 🔴 | Python |
| [PREF](https://github.com/PREF/PREF) | Portable reverse engineering framework | 145 | 🔴 | C++ |
| [mmo-chip](https://github.com/giulioz/mmo-chip) | Multiplayer CMOS standard cell chip reverse engineering tool | 144 | 🟢 | TypeScript |
| [pdb-decompiler](https://github.com/camden-smallwood/pdb-decompiler) | Decompiles MSVC PDB files into C++ source declarations | 139 | 🟢 | Rust |
| [Simplifier](https://github.com/mazeworks-security/Simplifier) | Efficient general mixed Boolean-arithmetic (MBA) simplifier | 137 | 🟢 | C# |
| [Anti-BR-Obf](https://github.com/Aar0n3906/Anti-BR-Obf) | Removes BR-register control flow obfuscation from Android native code using unidbg | 128 | 🟡 | Java |
| [AST-based JS deobfuscation materials](https://github.com/SteakEnthusiast/Supplementary-AST-Based-Deobfuscation-Materials) | AST-based JavaScript deobfuscator source code from the ReverseJS blog | 125 | 🔴 | JavaScript |
| [Il2CppInspectorPlugins](https://github.com/djkaty/Il2CppInspectorPlugins) | Plugins for the Il2CppInspector Unity IL2CPP analysis tool | 116 | 🟡 | C# |
| [Mach-O-Scope](https://github.com/smorr/Mach-O-Scope) | Browser for Mach-O disassembly dumps generated by otx and otool | 114 | 🔴 | Objective-C |
| [ProtobufDecoder](https://github.com/sandermvanvliet/ProtobufDecoder) | Protobuf payload decoder and analyzer without schema | 104 | 🟡 | C# |
| [minusone](https://github.com/airbus-cert/minusone) | PowerShell and JavaScript deobfuscator based on tree-sitter | 102 | 🟢 | Rust |
| [crcbeagle](https://github.com/colinoflynn/crcbeagle) | CRC reverse engineering tool in Python | 97 | 🔴 | Python |
| [nuitka-helper](https://github.com/goatmilkkk/nuitka-helper) | Symbol recovery tool for Nuitka-compiled Python binaries | 94 | 🟡 | Python |
| [rustbinsign](https://github.com/N0fix/rustbinsign) | Rust symbol recovery tool | 93 | 🟢 | Python |
| [patternsleuth](https://github.com/trumank/patternsleuth) | Unreal Engine address scanner and test suite for game binaries | 90 | 🟢 | Rust |
| [patchestry](https://github.com/lifting-bits/patchestry) | Binary patching framework built with MLIR and Ghidra | 89 | 🟢 | C++ |
| [retools](https://github.com/agustingianni/retools) | Reverse engineering toolkit including ARM emulator and spec-derived disassembler | 89 | 🔴 | C++ |
| [QtMetaParser](https://github.com/fjqisba/QtMetaParser) | IDA plugin that parses Qt meta-object data | 87 | 🟡 | C++ |
| [pbd](https://github.com/rsc-dev/pbd) | Disassembles serialized protobuf descriptors back to .proto | 86 | 🔴 | Python |
| [nimfilt](https://github.com/eset/nimfilt) | Modules and scripts for analyzing Nim binaries | 84 | 🟡 | Python |
| [JSRETK](https://github.com/SeanPesce/JSRETK) | Experimental tools for analyzing minified or obfuscated JavaScript | 81 | 🟢 | JavaScript |
| [protodec](https://github.com/Xpl0itR/protodec) | Derives Protobuf schemas from compiled protoc output in binaries | 81 | 🟢 | C# |
| [ReGAL](https://github.com/psurply/ReGAL) | Scripts to reverse engineer old programmable logic devices (PAL/GAL) | 79 | 🔴 | Python |
| [Deroute](https://github.com/emu-russia/Deroute) | Tool to untangle wires for chip die reverse engineering | 76 | 🟢 | C# |
| [psr](https://github.com/nccgroup/psr) | Pointer Sequence Reverser for Windows C++ application structures | 76 | 🔴 | C++ |
| [recover](https://github.com/huku-/recover) | Recovers compile units from stripped binaries | 75 | 🟢 | Python |
| [protodec](https://github.com/schdub/protodec) | Protobuf decompiler recovering .proto from binaries | 74 | 🟡 | C++ |
| [ninjadiff](https://github.com/riverloopsec/ninjadiff) | Binary diffing plugin for Binary Ninja | 71 | 🔴 | Python |
| [Il2CppParser](https://github.com/tacesrever/Il2CppParser) | libil2cpp symbol parser for IDA | 69 | 🔴 | C++ |
| [Virtual-File-System-Editor](https://github.com/extremecoders-re/Virtual-File-System-Editor) | Extracts embedded files from application virtualizers | 64 | 🔴 | Pascal |
| [js-deobfuscator (0x1Avram)](https://github.com/0x1Avram/js-deobfuscator) | Deobfuscator for JavaScript samples obfuscated by obfuscator.io | 62 | 🔴 | JavaScript |
| [prawntools](https://github.com/JohnDMcMaster/prawntools) | Integrated circuit reverse engineering software | 62 | 🔴 | Python |
| [NEMESYS](https://github.com/vs-uulm/nemesys) | Network message syntax reverse engineering by analysis of message value structure | 58 | 🟢 | Python |
| [TypeTreeDumper](https://github.com/DaZombieKiller/TypeTreeDumper) | Exports type tree information from the Unity editor | 57 | 🟢 | C# |
| [mrcrowbar](https://github.com/moralrecordings/mrcrowbar) | Library and model framework for reverse engineering binary file formats | 55 | 🟢 | Python |
| [ReverseBox](https://github.com/bartlomiejduda/ReverseBox) | Python library of checksums, compression and encryption helpers for game file reverse engineering | 55 | 🟢 | Python |
| [JSDefender-Deobfuscator](https://github.com/0v41n/JSDefender-Deobfuscator) | Deobfuscator for JavaScript protected by JSDefender | 42 | 🟡 | JavaScript |
| [BinPRE](https://github.com/ecnusse/BinPRE) | Binary-analysis-based protocol reverse engineering with improved field inference | 39 | 🟡 | Python |
| [ciqdb](https://github.com/pzl/ciqdb) | Parser and debugger for Garmin Connect IQ compiled PRG binaries | 39 | 🟡 | Go |
| [BinaryInferno](https://github.com/binaryinferno/binaryinferno) | Semantic field inference for reverse engineering binary message formats (research code) | 38 | 🔴 | Python |
| [dotscope](https://github.com/ATRAPSLLC/dotscope) | Rust framework for analyzing and reverse engineering .NET PE executables | 30 | 🟢 | Rust |
| [XboxImageXploder](https://github.com/grimdoomer/XboxImageXploder) | Utility for adding sections to and modifying original Xbox executables | 29 | 🟡 | C++ |
| [PowerBuilder-decompile](https://github.com/sijms/PowerBuilder-decompile) | Python module that parses PowerBuilder PBD files and analyzes the code | 27 | 🔴 | Python |
| [ue-version](https://github.com/AniLeo/ue-version) | Determines the Unreal Engine 4/5 version a game was built with | 25 | 🟡 | Shell |
| [Mapr](https://github.com/redstone-md/Mapr) | Bun CLI/TUI for reverse engineering frontend bundles, WASM and service workers | 23 | 🟢 | TypeScript |
| [netlifter](https://github.com/qingkaishi/netlifter) | Lifts network protocol implementations to precise message format specifications | 23 | 🟡 | C++ |
| [PRE Workbench](https://github.com/luelista/pre_workbench) | Protocol reverse engineering workbench | 22 | 🟡 | Python |
| [FieldHunter](https://github.com/vs-uulm/fieldhunter) | Reimplementation of the FieldHunter protocol reverse engineering approach | 18 | 🔴 | Python |
| [gore](https://github.com/figurophobia/gore) | Godot RE toolkit that turns a Godot game (PCK/EXE) into an openable project | 13 | 🟢 | Rust |
| [mootool](https://github.com/hack-different/mootool) | MachO's Other Tooling | 12 | 🟢 | Ruby |
| [Unigen](https://github.com/Razzile/Unigen) | Generates IDC scripts from Unity IL2CPP metadata | 10 | 🔴 | C |
| [hexvero](https://github.com/maximilianfeix/hexvero) | Static triage of Electron archives, JS bundles and ELF/Mach-O/PE binaries, with CLI and MCP | 9 | 🟢 | TypeScript |
| [D810G](https://github.com/overkazaf/D810G) | Ghidra deobfuscation framework: OLLVM/Tigress deflattening and MBA simplification | 6 | 🟢 | Python |
| [nibkit](https://github.com/tokenbleed/nibkit) | Decoder for compiled iOS/macOS NIB interface archives into object trees and connections | 6 | 🟢 | Go |
| [SpaceJunk](https://codeberg.org/SpaceBusCO/SpaceJunk) | Suite of binary reverse engineering tools written in Zig |  | ⚪ |  |

## Decompilation Project Tooling

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Diaphora](https://github.com/joxeankoret/diaphora) | Program diffing plugin for IDA, Ghidra-compatible exports | 4,447 | 🟢 | Python |
| [PS2Recomp](https://github.com/ran-j/PS2Recomp) | Playstation 2 Static Recompiler & Runtime Tool to make native PC ports | 3,746 | 🟢 | C++ |
| [BinDiff](https://github.com/google/bindiff) | Binary diffing tool for comparing disassembled code | 3,225 | 🟢 | Java |
| [ghidriff](https://github.com/clearbluejar/ghidriff) | Ghidra-based command-line binary diffing engine | 816 | 🟢 | Python |
| [BinSync](https://github.com/binsync/binsync) | Reverse-engineering collaboration and sync across decompilers | 758 | 🟢 | Python |
| [DecompilerMC](https://github.com/hube12/DecompilerMC) | Decompiles any Minecraft version using official mappings | 720 | 🗄️ | Python |
| [m2c](https://github.com/matt-kempster/m2c) | MIPS/PowerPC/ARM assembly to C decompiler aimed at matching output | 670 | 🟢 | Python |
| [objdiff](https://github.com/encounter/objdiff) | Local object-file diffing tool for matching decompilation projects | 615 | 🟢 | Rust |
| [ghidra-delinker-extension](https://github.com/boricj/ghidra-delinker-extension) | Ghidra extension exporting relocatable object files for delinking | 607 | 🟢 | Assembly |
| [RecompOne](https://github.com/BlackLabelHQ/RecompOne) | PSX Static Recompiler and Runtime, Not Affiliated With Sony or PlayStation | 606 | 🟢 | C# |
| [decomp.wtf](https://github.com/i12bp8/decomp.wtf) | Local app and MCP server that gives AI agents one console-game function at a time to decompile | 545 | 🗄️ | Python |
| [XenosRecomp](https://github.com/hedge-dev/XenosRecomp) | A tool for converting Xbox 360 shaders to HLSL. | 506 | 🟢 | C++ |
| [MinecraftDecompiler](https://github.com/MaxPixelStudios/MinecraftDecompiler) | Deobfuscates and decompiles Minecraft (or any jar) through popular mappings | 493 | 🟢 | Java |
| [splat](https://github.com/ethteck/splat) | Binary splitting tool for N64, PS1, PS2 and PSP decompilation projects | 375 | 🟢 | Python |
| [pokemon-reverse-engineering-tools](https://github.com/pret/pokemon-reverse-engineering-tools) | Tools for building and disassembling Pokemon Red and Crystal | 354 | 🗄️ | Python |
| [mgbdis](https://github.com/mattcurrie/mgbdis) | Game Boy ROM disassembler with RGBDS-compatible output | 330 | 🟢 | Assembly |
| [Ghidra-GameCube-Loader](https://github.com/Cuyler36/Ghidra-GameCube-Loader) | Nintendo GameCube binary (DOL/REL) loader for Ghidra | 325 | 🟢 | Java |
| [decomp-toolkit](https://github.com/encounter/decomp-toolkit) | GameCube/Wii decompilation toolkit: splits binaries and generates build configs | 321 | 🟢 | Rust |
| [xboxrecomp](https://github.com/sp00nznet/xboxrecomp) | Static recompiler turning original Xbox game binaries into native Windows executables | 313 | 🟢 | C |
| [poryscript](https://github.com/huderlem/poryscript) | High-level scripting language for Gen 3 Pokemon decompilation projects | 312 | 🟢 | Go |
| [decomp-permuter](https://github.com/simonlindholm/decomp-permuter) | Randomly permutes C code to find a match with target assembly | 239 | 🟢 | Python |
| [6502bench](https://github.com/fadden/6502bench) | Code workbench and disassembler (SourceGen) for 6502 software | 212 | 🟢 | Assembly |
| [psx-modding-toolchain](https://github.com/mateusfavarin/psx-modding-toolchain) | Tools to mod and reverse engineer PlayStation 1 games | 195 | 🟢 | C |
| [wibo](https://github.com/decompals/wibo) | Minimal Windows binary loader to run old Win32 compilers on Linux | 190 | 🟢 | C++ |
| [rabbitizer](https://github.com/Decompollaborate/rabbitizer) | MIPS instruction decoder library used by decomp tooling | 184 | 🟢 | C |
| [asm-differ](https://github.com/simonlindholm/asm-differ) | Assembly differ for matching decompilation work | 182 | 🟢 | Python |
| [N64LoaderWV](https://github.com/zeroKilo/N64LoaderWV) | Ghidra loader module for Nintendo 64 ROMs | 172 | 🟢 | Java |
| [XboxXBERecomp](https://github.com/TGP482/XboxXBERecomp) | Tool for statically recompiling original Xbox games into native executables | 168 | 🟢 | C++ |
| [Game-Decompilation-Skill-For-Claude](https://github.com/lemiur/Game-Decompilation-Skill-For-Claude) | Claude skill for creating byte-matching decompilations of games | 166 | 🟢 |  |
| [reccmp](https://github.com/isledecomp/reccmp) | Tools for comparing recompiled code against original binaries | 166 | 🟢 | Python |
| [SkoolKit](https://github.com/skoolkid/skoolkit) | Tools for creating disassemblies of ZX Spectrum games | 165 | 🟢 | Python |
| [regenerator2000](https://github.com/ricardoquesada/regenerator2000) | Interactive 6502 disassembler for Commodore 8-bit software with a TUI | 164 | 🟢 | Rust |
| [ghidra-allegrex](https://github.com/kotcrab/ghidra-allegrex) | Ghidra processor module for the PSP Allegrex CPU | 136 | 🟢 | Kotlin |
| [SwitchRecomp](https://github.com/bgyss/SwitchRecomp) | Preservation-focused static recompilation research for Nintendo Switch. | 122 | 🟢 | Rust |
| [ccc](https://github.com/chaoticgd/ccc) | Library and tools for parsing PS2 debugging symbols | 109 | 🟢 | C++ |
| [ds-decomp](https://github.com/AetiasHax/ds-decomp) | Toolkit for decompiling Nintendo DS games | 105 | 🟢 | Rust |
| [llvm8](https://github.com/ioncodes/llvm8) | Statically recompiling CHIP8 to Windows and macOS using LLVM | 99 | 🔴 | C++ |
| [dtk-template](https://github.com/encounter/dtk-template) | Project template for decomp-toolkit GameCube/Wii decompilations | 90 | 🟢 | Python |
| [ido-static-recomp](https://github.com/decompals/ido-static-recomp) | Static recompilation of the IDO 5.3 and 7.1 compilers for modern platforms | 85 | 🟡 | C++ |
| [spimdisasm](https://github.com/Decompollaborate/spimdisasm) | MIPS disassembler that produces matching-ready assembly for decomp projects | 83 | 🟢 | Python |
| [porytiles](https://github.com/grunt-lucas/porytiles) | Overworld tileset compiler for Gen III Pokemon decompilation projects | 82 | 🟢 | C++ |
| [Mizuchi](https://github.com/macabeus/mizuchi) | Pipeline that combines m2c, permuter, objdiff and AI to auto-decompile functions | 77 | 🟢 | TypeScript |
| [mzretools](https://github.com/neuviemeporte/mzretools) | Tools for reversing DOS games via MZ executable inspection | 75 | 🟢 | C++ |
| [ZomboidDecompiler](https://github.com/demiurgeQuantified/ZomboidDecompiler) | Decompilation tool specialised for Project Zomboid using Vineflower | 70 | 🟢 | Java |
| [decomp.anything](https://github.com/giveen/decomp.anything) | decomp.wtf variant with Windows PE matching, MinGW/clang-cl toolchains and an REA bridge | 66 | 🟢 | Python |
| [3dsrecomp](https://github.com/fearkov/3dsrecomp) | Static recompiler for Nintendo 3DS games, from ARM to C | 65 | 🟢 | Rust |
| [Ghidra-SegaSaturn-Loader](https://github.com/VGKintsugi/Ghidra-SegaSaturn-Loader) | Sega Saturn loader for Ghidra | 60 | 🟢 | Java |
| [ds_disassembly_tools](https://github.com/pret/ds_disassembly_tools) | Scripts to set up a Nintendo DS disassembly project | 58 | 🔴 | Python |
| [pmdsky-debug](https://github.com/UsernameFodder/pmdsky-debug) | Debug info for reverse engineering Pokemon Mystery Dungeon: Explorers of Sky | 55 | 🟢 | C |
| [psretrox](https://github.com/cualquiercosa327/psretrox) | PlayStation 2 decompilation and recompilation tool | 55 | 🟡 | C++ |
| [NESgen](https://github.com/Xenomega/NESgen) | Static Recompilation of NES ROMs to C code | 53 | 🗄️ | C |
| [gba-recomp](https://github.com/JRickey/gba-recomp) | Static recompilation tool and runtime for the GBA | 52 | 🟢 | Rust |
| [Kappa](https://github.com/macabeus/kappa) | VS Code extension assisting matching decompilation work | 52 | 🟢 | TypeScript |
| [PSP-recompilation-project](https://github.com/sal063/PSP-recompilation-project) | Static recompiler for PSP games with native rendering | 49 | 🟢 | C |
| [n64sym](https://github.com/shygoo/n64sym) | Symbol identification tool for N64 ROMs | 46 | 🔴 | Standard ML |
| [retrokit](https://github.com/nautilusbits/retrokit) | Headless Ghidra toolkit for reversing 32-bit DOS and Win32 games, with an LE/LX loader | 43 | 🟢 | Python |
| [sega2asm](https://github.com/hansbonini/sega2asm) | Sega Genesis / Mega Drive disassembler and splitter in Go | 42 | 🟢 | Go |
| [gilgamesh](https://github.com/AndreaOrru/gilgamesh) | SNES reverse engineering toolkit with static recompilation support | 37 | 🔴 | C++ |
| [NWiiRecomp](https://github.com/BlackLineInteractive/NWiiRecomp) | Static recompilation and runtime toolkit for Nintendo GameCube and Wii to make native PC ports (and not only) | 35 | 🟢 | C++ |
| [mapfile_parser](https://github.com/Decompollaborate/mapfile_parser) | Parses linker map files for decomp progress tracking | 31 | 🟢 | Rust |
| [ppcdis](https://github.com/SeekyCt/ppcdis) | GameCube/Wii PowerPC disassembly and decompilation tools | 31 | 🟡 | Python |
| [gamedb](https://github.com/smileybaal/gamedb) | CLI that indexes decompiled C/C++/Java/C# source into SQLite for search and call graphs | 30 | 🟢 | Rust |
| [DecompPipeline](https://github.com/GeneralAtrox/DecompPipeline) | LLM-driven matching decompilation pipeline with Ghidra and an emulator-based test oracle | 27 | 🟢 | Python |
| [PS4Recomp](https://github.com/wie-project/PS4Recomp) | Experimental macOS Apple Silicon first recompiler of PS4 programs | 27 | 🟢 | C |
| [SaturnRecomp](https://github.com/sonsegajp/SaturnRecomp) | Experimental clean-room Sega Saturn runtime and static recompilation toolkit | 27 | 🟢 | C |
| [delink](https://github.com/HaydnTrigg/delink) | Splitting tool for decompilation projects | 26 | 🟢 | Rust |
| [nWiiURecomp](https://github.com/BlackLineInteractive/nWiiURecomp) | Static recompilation and runtime toolkit for Nintendo Wii U (based on NWiiRecomp) to make native PC ports (and not only) | 24 | 🟢 | C++ |
| [RecompCore](https://github.com/aharonahdoot/RecompCore) | A static-recompilation CPU core for Dolphin — run GameCube games as native code, with transparent interpreter fallback | 22 | 🟢 | C++ |
| [n64-decomp-workbench](https://github.com/akratch/n64-decomp-workbench) | Relocation-aware diffs to find late-stage MIPS decompilation mismatches | 20 | 🟢 | Python |
| [gba-matching-decomp-skill](https://github.com/FacundoMainere/gba-matching-decomp-skill) | Claude Code skill for matching decompilation of GBA ROMs with agbcc, from splitting to decomp.dev | 18 | 🟢 | Python |
| [game-frame](https://github.com/tanepiper/game-frame) | Framework for AI agents and people to reverse engineer games from shipped files | 17 | 🟢 | Rust |
| [model3recomp](https://github.com/sp00nznet/model3recomp) | Sega Model 3 hardware runtime and PowerPC 603e static recompiler. Link a recompiled Model 3 game against native C har... | 16 | 🟢 | C |
| [m3c](https://github.com/ethteck/m3c) | Assists N64 decompilation by running m2c and decomp-permuter to find matches | 13 | 🟡 | Python |
| [Exhume](https://github.com/abedegno/Exhume) | Toolkit and Claude Code skills for byte-matching decompilation of old DOS games | 12 | 🟢 | Python |
| [NDS-Decompilation-Project-Maker](https://github.com/Ed-1T/NDS-Decompilation-Project-Maker) | Creates an XML decompilation project from a Nintendo DS ROM | 12 | 🔴 | C# |
| [model2recomp](https://github.com/sp00nznet/model2recomp) | A Sega Model 2 hardware runtime for statically recompiled games: geometry engine, rasterizer, tilemaps and TGP coproc... | 11 | 🟢 | C |
| [nakagawa-recomp](https://github.com/Jstar269/nakagawa-recomp) | Experimental PSP static recompiler and native runtime using user-supplied lawful inputs. | 11 | 🟢 | C |
| [SwitchRecomp](https://github.com/kaiyao7/SwitchRecomp) | Static recompilation research framework for Nintendo Switch AArch64 binaries | 11 | 🟢 | C++ |
| [ps2-port-engine](https://github.com/danielgomesvieira2000/ps2-port-engine) | Toolchain and runtime for native PC ports of PS2 games from verified decompilation | 10 | 🟢 | C++ |
| [RetroRecomp](https://github.com/ArthurReboulSalze/RetroRecomp) | Multi-console game recompilation into standalone Windows and Linux executables | 10 | 🟢 | Python |
| [GXRuntime](https://github.com/aharonahdoot/GXRuntime) | Game-agnostic GameCube static-recompilation runtime: CPU semantics, devices, GX renderer (work in progress) | 8 | 🟢 | C++ |
| [psprism](https://github.com/anthonyhfm/psprism) | A tool for recompiling PlayStation Portable games to native executables. | 8 | 🟢 | C++ |
| [UnityRift](https://github.com/Diphome/UnityRift) | Toolkit for reverse engineering and porting Unity games to Godot 4 | 8 | 🟢 | C# |
| [touhou-reconstruction-factory](https://github.com/N0zoM1z0/touhou-reconstruction-factory) | Evidence-first control plane for agent-driven Touhou source reconstruction projects | 7 | 🟢 | Python |
| [mweppc](https://github.com/doldecomp/mweppc) | Decompilation of the Metrowerks CodeWarrior PowerPC toolchain | 6 | 🟢 | C |
| [shader-compiler-rs](https://github.com/DCNick3/shader-compiler-rs) | A tool to recompile binary maxwell shaders (found on nintendo switch) to glsl | 6 | 🟡 | C++ |
| [xenon-jumptables](https://github.com/xdzleo/xenon-jumptables) | Recover Xbox 360 / Xenon PowerPC jump tables for static recompilation (XenonRecomp / ReXGlue) — resolves the switch i... | 6 | 🟢 | Python |
| [v64recomp](https://github.com/polaco1782/v64recomp) | N64 static recompiler | 5 | 🟢 | C |
| [pdtools](https://gitlab.com/ryandwyer/pdtools) | Tooling for the Perfect Dark decompilation project |  | ⚪ |  |

## Disassemblers & Decompilers

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | NSA's software reverse engineering framework with decompiler | 96,341 | 🟢 | Java |
| [x64dbg](https://github.com/x64dbg/x64dbg) | Open source user-mode debugger for Windows | 50,084 | 🟢 | C++ |
| [dnSpy](https://github.com/dnSpy/dnSpy) | .NET debugger, decompiler and assembly editor | 29,660 | 🗄️ | C# |
| [ILSpy](https://github.com/icsharpcode/ILSpy) | Cross-platform .NET decompiler | 26,889 | 🟢 | C# |
| [radare2](https://github.com/radareorg/radare2) | UNIX-like reverse engineering framework and toolset | 25,217 | 🟢 | C |
| [Cutter](https://github.com/rizinorg/cutter) | Free RE platform/GUI powered by rizin | 20,121 | 🟢 | C++ |
| [bytecode-viewer](https://github.com/Konloch/bytecode-viewer) | Java JAR and Android APK reverse engineering suite with multiple decompilers, editor and debugger | 15,700 | 🟢 | Java |
| [JD-GUI](https://github.com/java-decompiler/jd-gui) | Standalone GUI Java decompiler | 15,223 | 🟡 | Java |
| [dnSpyEx](https://github.com/dnSpyEx/dnSpy) | Revival of dnSpy .NET debugger and assembly editor | 11,371 | 🟢 | C# |
| [angr](https://github.com/angr/angr) | Python binary analysis framework with symbolic execution and decompiler | 9,270 | 🟢 | Python |
| [Capstone](https://github.com/capstone-engine/capstone) | Multi-architecture disassembly framework | 9,157 | 🟢 | C |
| [RetDec](https://github.com/avast/retdec) | Retargetable machine-code decompiler based on LLVM | 8,665 | 🟢 | C++ |
| [Recaf](https://github.com/Col-E/Recaf) | Java bytecode editor and decompiler front end | 7,449 | 🟢 | Java |
| [LLM4Decompile](https://github.com/albertan017/LLM4Decompile) | LLMs that decompile binary code to C | 7,195 | 🟢 | Python |
| [GhidraMCP (bethington)](https://github.com/bethington/ghidra-mcp) | Ghidra MCP server exposing 200+ tools for AI-assisted reverse engineering | 6,024 | 🟢 | Java |
| [JPEXS FFDec](https://github.com/jindrapetrik/jpexs-decompiler) | Open-source Flash SWF decompiler and editor | 5,993 | 🟢 | Java |
| [pycdc](https://github.com/zrax/pycdc) | C++ Python bytecode disassembler and decompiler | 4,669 | 🟢 | C++ |
| [pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor) | Extractor for PyInstaller-generated executables | 4,514 | 🟢 | Python |
| [Fernflower](https://github.com/JetBrains/fernflower) | Analytical Java bytecode decompiler used in IntelliJ IDEA | 4,433 | 🟢 | Java |
| [Zydis](https://github.com/zyantific/zydis) | Fast x86/x86-64 disassembler and encoder library in C | 4,403 | 🟢 | C |
| [uncompyle6](https://github.com/rocky/python-uncompyle6) | Cross-version Python bytecode decompiler | 4,330 | 🟢 | Python |
| [AsmDude](https://github.com/HJLebbink/asm-dude) | Visual Studio extension for assembly syntax highlighting and completion in the disassembly window | 4,179 | 🟢 | C# |
| [rizin](https://github.com/rizinorg/rizin) | UNIX-like reverse engineering framework (radare2 fork) | 4,081 | 🟢 | C |
| [Miasm](https://github.com/cea-sec/miasm) | Python reverse engineering framework: disassembly, IR, symbolic execution, emulation | 4,004 | 🟢 | Python |
| [iced](https://github.com/icedland/iced) | x86/x64 instruction decoder, formatter, assembler and encoder library | 3,613 | 🟢 | Rust |
| [Plasma](https://github.com/plasma-disassembler/plasma) | Interactive disassembler for x86/ARM/MIPS with pseudo-C output | 3,070 | 🔴 | Python |
| [Mono.Cecil](https://github.com/jbevain/cecil) | Library to inspect and modify .NET CIL assemblies | 3,008 | 🟢 | C# |
| [webcrack](https://github.com/j4k0xb/webcrack) | Deobfuscates obfuscator.io output and unpacks bundled JavaScript | 3,006 | 🟢 | TypeScript |
| [binnavi](https://github.com/google/binnavi) | Binary analysis IDE for inspecting and annotating control flow graphs | 2,887 | 🗄️ | Java |
| [CFR](https://github.com/leibnitz27/cfr) | Java decompiler supporting modern Java features | 2,738 | 🟢 | Java |
| [Decompiler Explorer](https://github.com/decompiler-explorer/decompiler-explorer) | Dogbolt: compare output of many decompilers in the browser | 2,724 | 🟢 | Python |
| [Keystone](https://github.com/keystone-engine/keystone) | Multi-architecture assembler framework | 2,653 | 🟢 | C++ |
| [Reko](https://github.com/uxmal/reko) | General-purpose binary decompiler supporting many CPU architectures | 2,629 | 🟢 | C# |
| [dnlib](https://github.com/0xd4d/dnlib) | Library to read and write .NET assemblies and modules | 2,495 | 🟢 | C# |
| [flare-ida](https://github.com/mandiant/flare-ida) | IDA Pro utilities from the FLARE team | 2,450 | 🗄️ | Python |
| [Vineflower](https://github.com/Vineflower/vineflower) | Modern Java decompiler (Fernflower fork, formerly Quiltflower) | 2,441 | 🟢 | Java |
| [ret-sync](https://github.com/bootleg/ret-sync) | Synchronizes debugger sessions with IDA, Ghidra and Binary Ninja | 2,406 | 🟢 | C |
| [BAP](https://github.com/BinaryAnalysisPlatform/bap) | Binary Analysis Platform for lifting and analysing binaries | 2,264 | 🟢 | OCaml |
| [Snowman](https://github.com/yegord/snowman) | Native code to C/C++ decompiler for x86, x86-64 and ARM | 2,245 | 🗄️ |  |
| [hrtng](https://github.com/KasperskyLab/hrtng) | IDA plugin from Kaspersky that extends the Hex-Rays decompiler with RE helpers | 1,956 | 🟢 | C++ |
| [remill](https://github.com/lifting-bits/remill) | Library lifting machine code to LLVM bitcode | 1,887 | 🟢 | C++ |
| [keypatch](https://github.com/keystone-engine/keypatch) | Multi-architecture assembler plugin for IDA Pro | 1,881 | 🟡 | Python |
| [REDasm](https://github.com/redasm-dev/redasm) | Interactive multi-architecture disassembler | 1,825 | 🟢 | C++ |
| [AvaloniaILSpy](https://github.com/icsharpcode/AvaloniaILSpy) | Cross-platform Avalonia GUI for the ILSpy .NET decompiler | 1,813 | 🗄️ | C# |
| [rev.ng](https://github.com/revng/revng) | Binary analysis framework and decompiler based on LLVM and QEMU | 1,765 | 🟢 | C++ |
| [iaito](https://github.com/radareorg/iaito) | Official Qt GUI for radare2 | 1,733 | 🟢 | C++ |
| [PowerUp](https://github.com/badamczewski/PowerUp) | Decompilation and JIT/assembly inspection utilities for .NET, Go and Rust | 1,661 | 🟡 | C# |
| [heimdall-rs](https://github.com/Jon-Becker/heimdall-rs) | EVM smart contract toolkit that decompiles and analyzes unverified bytecode | 1,637 | 🟢 | Rust |
| [Ponce](https://github.com/illera88/Ponce) | IDA plugin for one-click symbolic execution | 1,636 | 🟡 | C++ |
| [HexRaysPyTools](https://github.com/igogo-x86/HexRaysPyTools) | IDA Pro plugin for reconstructing structures and classes in the Hex-Rays decompiler | 1,545 | 🟡 | Python |
| [iaito](https://github.com/hteso/iaito) | Official Qt GUI for the radare2 reverse engineering framework | 1,459 | 🔴 | C++ |
| [BARF](https://github.com/programa-stic/barf-project) | Binary Analysis and Reverse engineering Framework for x86/ARM | 1,456 | 🔴 | Python |
| [LazyIDA](https://github.com/L4ys/LazyIDA) | IDA Pro plugin with convenience features for analysis | 1,446 | 🟢 | Python |
| [panopticon](https://github.com/das-labor/panopticon) | Libre cross-platform disassembler | 1,446 | 🗄️ | Rust |
| [pylingual](https://github.com/syssec-utd/pylingual) | Python decompiler for modern Python bytecode versions | 1,432 | 🟢 | Python |
| [Virtuailor](https://github.com/0xgalz/Virtuailor) | IDAPython tool reconstructing C++ virtual tables in IDA Pro | 1,407 | 🔴 | Python |
| [FLIRTDB](https://github.com/Maktm/FLIRTDB) | Community collection of IDA FLIRT library signature files | 1,365 | 🔴 | Max |
| [diStorm](https://github.com/gdabah/distorm) | Fast x86/AMD64 disassembler library | 1,342 | 🔴 | C |
| [luadec](https://github.com/viruscamp/luadec) | Lua decompiler for Lua 5.1, 5.2 and 5.3 bytecode | 1,339 | 🟡 | Lua |
| [binaryninja-api](https://github.com/Vector35/binaryninja-api) | Public API, examples and docs for the Binary Ninja reverse-engineering platform | 1,332 | 🟢 | C++ |
| [patching](https://github.com/gaasedelen/patching) | Interactive binary patching plugin for IDA Pro | 1,292 | 🟡 | Python |
| [NETReactorSlayer](https://github.com/SychicBoy/NETReactorSlayer) | Deobfuscator and unpacker for Eziriz .NET Reactor | 1,277 | 🟢 | C# |
| [decompile3](https://github.com/rocky/python-decompile3) | Python 3.7+ bytecode decompiler | 1,276 | 🟢 | Python |
| [shuji](https://github.com/paazmaya/shuji) | Recovers original JavaScript and CSS sources from source maps | 1,248 | 🟢 | JavaScript |
| [xAnalyzer](https://github.com/ThunderCls/xAnalyzer) | x64dbg plugin for automatic API call and function analysis | 1,242 | 🟡 | C |
| [Procyon](https://github.com/mstrobel/procyon) | Java metaprogramming suite and decompiler | 1,227 | 🔴 | Java |
| [binexport](https://github.com/google/binexport) | Exports disassemblies from IDA, Ghidra and Binary Ninja into Protocol Buffers | 1,218 | 🟢 | C++ |
| [angr-management](https://github.com/angr/angr-management) | GUI for the angr binary analysis framework | 1,198 | 🟢 | Python |
| [ghidraninja ghidra_scripts](https://github.com/ghidraninja/ghidra_scripts) | Scripts for the Ghidra reverse engineering suite | 1,179 | 🔴 | YARA |
| [lumen](https://github.com/naim94a/lumen) | Private reimplementation of IDA Pro's Lumina server | 1,176 | 🟢 | Rust |
| [IDR](https://github.com/crypto2011/IDR) | Interactive Delphi Reconstructor: decompiler for Delphi executables | 1,171 | 🔴 | C++ |
| [javascript-deobfuscator](https://github.com/ben-sb/javascript-deobfuscator) | General purpose JavaScript deobfuscator | 1,157 | 🟡 | TypeScript |
| [ViperMonkey](https://github.com/decalage2/ViperMonkey) | VBA parser and emulation engine for analysing Office macros | 1,133 | 🟡 | Python |
| [bddisasm](https://github.com/bitdefender/bddisasm) | Fast, lightweight x86/x64 instruction decoder and emulator | 1,089 | 🟢 | C |
| [medusa](https://github.com/wisk/medusa) | Open source interactive disassembler | 1,089 | 🟢 | C++ |
| [wakaru](https://github.com/pionxzh/wakaru) | JavaScript decompiler and unpacker for modern frontend bundles | 1,070 | 🟢 | Rust |
| [de4py](https://github.com/Fadi002/de4py) | Toolkit for Python reverse engineering: deobfuscation, unpacking and analysis of Python executables | 1,010 | 🟢 | Python |
| [vivisect](https://github.com/vivisect/vivisect) | Python binary analysis framework, disassembler and debugger | 1,003 | 🟢 | Python |
| [rz-ghidra](https://github.com/rizinorg/rz-ghidra) | Ghidra decompiler and Sleigh disassembler integration for Rizin and Cutter | 1,002 | 🟢 | C++ |
| [idacode](https://github.com/ioncodes/idacode) | VS Code integration for running and debugging IDAPython scripts | 996 | 🟡 | Python |
| [Porosity](https://github.com/msuiche/porosity) | Decompiler and security analysis tool for Ethereum smart contracts | 934 | 🔴 | C++ |
| [Karta](https://github.com/CheckPointSW/Karta) | Source-code-assisted binary matching plugin for IDA | 914 | 🟢 | Python |
| [IDAssist](https://github.com/symgraph/IDAssist) | AI-augmented reverse engineering plugin for IDA Pro | 901 | 🟢 | Python |
| [VMAttack](https://github.com/anatolikalysch/VMAttack) | IDA Pro plugin for analysing virtualization-based obfuscation | 892 | 🔴 | Python |
| [ddisasm](https://github.com/GrammaTech/ddisasm) | Fast reassembleable disassembler | 882 | 🟢 | C++ |
| [JByteMod-Beta](https://github.com/loerting/JByteMod-Beta) | Java bytecode editor | 859 | 🔴 | Java |
| [ipyida](https://github.com/eset/ipyida) | IPython console integration for IDA Pro | 857 | 🟢 | Python |
| [decomp2dbg](https://github.com/mahaloz/decomp2dbg) | Syncs decompiler symbols and types into GDB | 828 | 🟢 | Python |
| [BiTE](https://github.com/WINSDK/bite) | Cross-platform executable viewer and disassembler with strong Rust support | 825 | 🟢 | Rust |
| [GhIDA](https://github.com/Cisco-Talos/GhIDA) | GhIDA | 822 | 🔴 | Python |
| [obfuscator-io-deobfuscator](https://github.com/ben-sb/obfuscator-io-deobfuscator) | Deobfuscator for scripts obfuscated by Obfuscator.io | 808 | 🟢 | TypeScript |
| [retdec-idaplugin](https://github.com/avast/retdec-idaplugin) | RetDec plugin for IDA | 799 | 🟡 | C++ |
| [Ghidrathon](https://github.com/mandiant/Ghidrathon) | Python 3 scripting support for Ghidra | 791 | 🗄️ | Java |
| [fcd](https://github.com/fay59/fcd) | LLVM-based optimizing native-code decompiler | 773 | 🔴 | C++ |
| [rzweb](https://github.com/IndAlok/rzweb) | Browser-based reverse engineering platform built on Rizin compiled to WebAssembly | 770 | 🟢 | TypeScript |
| [Kuna](https://github.com/Noelo-Lab/kuna) | Agent-first decompiler written in Rust | 764 | 🟢 | Rust |
| [pyinstxtractor-ng](https://github.com/pyinstxtractor/pyinstxtractor-ng) | PyInstaller extractor next generation | 746 | 🟢 | Python |
| [debundle](https://github.com/1egoman/debundle) | Debundler that recreates source trees from Browserify or Webpack bundles | 738 | 🔴 | JavaScript |
| [Xori](https://github.com/endgameinc/xori) | Disassembly and static analysis library for PE32, PE32+ and shellcode | 723 | 🔴 | Rust |
| [NtRays](https://github.com/can1357/NtRays) | Hex-Rays microcode plugin simplifying Windows kernel decompilation | 682 | 🟡 | C++ |
| [lucid](https://github.com/gaasedelen/lucid) | Interactive Hex-Rays microcode explorer | 681 | 🟡 | Python |
| [AlphaGolang](https://github.com/SentineLabs/AlphaGolang) | IDAPython scripts for analysing Go binaries | 675 | 🟡 | Python |
| [Sark](https://github.com/tmr232/Sark) | Pythonic library simplifying IDAPython | 671 | 🟡 | Python |
| [IDArling](https://github.com/IDArlingTeam/IDArling) | Collaborative reverse engineering plugin for IDA Pro and Hex-Rays | 670 | 🗄️ | Python |
| [golang_loader_assist](https://github.com/strazzere/golang_loader_assist) | IDA Pro script making Go binary reversing easier | 662 | 🔴 | Python |
| [Ghidra-Cpp-Class-Analyzer](https://github.com/astrelsky/Ghidra-Cpp-Class-Analyzer) | Ghidra C++ class and RTTI analyzer | 650 | 🗄️ | Java |
| [Rellic](https://github.com/lifting-bits/rellic) | Produces goto-free C output from LLVM bitcode for decompilation | 623 | 🟢 | C++ |
| [r2dec-js](https://github.com/wargio/r2dec-js) | Pseudo-C decompiler plugin for radare2 and rizin | 613 | 🟢 | JavaScript |
| [XLMMacroDeobfuscator](https://github.com/DissectMalware/XLMMacroDeobfuscator) | Extracts and emulates Excel 4.0 (XLM) macros from XLS, XLSM and XLSB files | 591 | 🟡 | Python |
| [r2ghidra](https://github.com/radareorg/r2ghidra) | Native Ghidra decompiler integration for radare2 | 567 | 🟢 | C++ |
| [B2R2](https://github.com/B2R2-org/B2R2) | Binary analysis framework in F# with disassembly, lifting and analysis for many ISAs | 552 | 🟢 | F# |
| [FindCrypt-Ghidra](https://github.com/d3v1l401/FindCrypt-Ghidra) | FindCrypt port for Ghidra with updated crypto signatures | 552 | 🔴 | C++ |
| [beaengine](https://github.com/BeaEngine/beaengine) | BeaEngine x86/x64 disassembler library | 549 | 🔴 | Python |
| [unwebpack-sourcemap](https://github.com/rarecoil/unwebpack-sourcemap) | Extracts uncompiled SPA source code from Webpack source maps | 544 | 🗄️ | Python |
| [E-Decompiler](https://github.com/fjqisba/E-Decompiler) | IDA plugin to analyse programs written in E-language (Yi Yuyan) | 541 | 🟢 | C++ |
| [Diobf Deobfuscator](https://github.com/Diobf/Deobfuscator) | Deobfuscators for common Java bytecode obfuscators | 540 | 🟢 | Java |
| [decompiler](https://github.com/EiNSTeiN-/decompiler) | Python decompiler with multiple backends for IDA and Capstone | 535 | 🔴 | Python |
| [Yagi](https://github.com/airbus-cert/Yagi) | Ghidra decompiler integration for IDA | 511 | 🟡 | C++ |
| [IFL](https://github.com/hasherezade/ida_ifl) | Interactive functions list plugin for IDA Pro | 502 | 🟢 | Python |
| [grayhatacademy ghidra_scripts](https://github.com/grayhatacademy/ghidra_scripts) | Ghidra ports of devttyS0's IDA plugins plus new plugins | 501 | 🔴 | Python |
| [decomp](https://github.com/decomp/decomp) | Components of a decompilation pipeline (LLVM IR to Go) | 499 | 🔴 | Go |
| [Unreal-Library](https://github.com/EliotVU/Unreal-Library) | Decompiler and parser for Unreal Engine package files | 494 | 🟢 | C# |
| [pcodedmp](https://github.com/bontchev/pcodedmp) | Disassembler for undocumented VBA p-code in Office macro documents | 491 | 🔴 | Python |
| [luajit-decompiler-v2](https://github.com/marsinator358/luajit-decompiler-v2) | LuaJIT bytecode decompiler | 489 | 🟢 | C++ |
| [HexraysToolbox](https://github.com/patois/HexraysToolbox) | Finds code patterns in the Hex-Rays ctree | 484 | 🔴 | Python |
| [sigmakerex](https://github.com/kweatherman/sigmakerex) | Enhanced IDA Pro signature generator plugin | 484 | 🟡 | C++ |
| [IDA-Pro-SigMaker](https://github.com/A200K/IDA-Pro-SigMaker) | Signature maker plugin for IDA Pro | 480 | 🟡 | C++ |
| [Driver Buddy Reloaded](https://github.com/VoidSec/DriverBuddyReloaded) | IDA Pro plugin that automates Windows kernel driver reverse engineering tasks | 473 | 🟢 | Python |
| [r2pipe](https://github.com/radareorg/radare2-r2pipe) | Access radare2 from any programming language through a pipe | 468 | 🟢 | JavaScript |
| [mdec](https://github.com/mborgerson/mdec) | Compare output of multiple decompilers side by side | 460 | 🗄️ | Python |
| [dsync](https://github.com/patois/dsync) | IDAPython plugin that synchronizes disassembler and decompiler views | 459 | 🔴 | Python |
| [RABCDAsm](https://github.com/CyberShadow/RABCDAsm) | ActionScript 3 bytecode (ABC) assembler and disassembler | 457 | 🔴 | D |
| [HRDevHelper](https://github.com/patois/HRDevHelper) | Hex-Rays ctree visualization plugin | 443 | 🟡 | Python |
| [zasm](https://github.com/zyantific/zasm) | x86-64 assembler library based on Zydis | 435 | 🟢 | C++ |
| [wasmdec](https://github.com/wwwg/wasmdec) | WebAssembly to C decompiler | 430 | 🟡 | C++ |
| [ddc](https://github.com/ejfkdev/ddc) | Fast Android DEX to Java decompiler in Rust | 427 | 🟢 | Rust |
| [nyxstone](https://github.com/emproof-com/nyxstone) | LLVM-based assembly and disassembly library with Rust and Python bindings | 427 | 🟢 | Rust |
| [IDAObjcTypes](https://github.com/PoomSmart/IDAObjcTypes) | Type and function definitions for analysing iOS/macOS binaries in IDA | 425 | 🟢 | Objective-C |
| [ScratchABit](https://github.com/pfalcon/ScratchABit) | Retargetable interactive disassembler with IDAPython-compatible plugin API | 413 | 🔴 | Python |
| [Boomerang](https://github.com/BoomerangDecompiler/boomerang) | General open-source machine-code decompiler | 405 | 🔴 | C++ |
| [CodemerxDecompile](https://github.com/codemerx/CodemerxDecompile) | Standalone cross-platform .NET decompiler | 401 | 🟡 | C# |
| [pydumpck](https://github.com/serfend/pydumpck) | Decompiler for Python-packed exe, elf, pyz and pyc files | 400 | 🟡 | Python |
| [radeco](https://github.com/radareorg/radeco) | radare2-based decompiler and symbolic executor in Rust | 399 | 🟢 | Rust |
| [aiDAPal](https://github.com/atredispartners/aidapal) | IDA Pro plugin with fine-tuned local LLM for Hex-Rays pseudocode | 393 | 🟡 | Python |
| [dnSpy.Extension.HoLLy](https://github.com/holly-hacker/dnSpy.Extension.HoLLy) | dnSpy extension to aid reversing obfuscated assemblies | 390 | 🔴 | C# |
| [GhidRust](https://github.com/DMaroo/GhidRust) | Rust decompiler plugin for Ghidra | 387 | 🟡 | Java |
| [OldRod](https://github.com/Washi1337/OldRod) | Automated KoiVM disassembler and devirtualizer | 387 | 🔴 | C# |
| [anvill](https://github.com/lifting-bits/anvill) | Lifts raw machine code to LLVM bitcode for decompilation | 385 | 🟡 | LLVM |
| [Ghidra-Switch-Loader](https://github.com/Adubbz/Ghidra-Switch-Loader) | Nintendo Switch binary loader for Ghidra | 381 | 🟢 | Java |
| [ghidra_kernelcache](https://github.com/0x36/ghidra_kernelcache) | a Ghidra framework for iOS kernelcache reverse engineering | 373 | 🔴 | Python |
| [xdis](https://github.com/rocky/python-xdis) | Cross-version Python bytecode library and disassembler | 372 | 🟢 | Python |
| [rattle](https://github.com/crytic/rattle) | EVM binary static analysis framework | 367 | 🔴 | Python |
| [ghidra_bridge](https://github.com/justfoxing/ghidra_bridge) | Python 3 bridge to Ghidra's Python scripting | 364 | 🔴 | Python |
| [Sekiryu (GhidrAI)](https://github.com/20urc3/Sekiryu) | Ghidra headless toolkit with automatic decompilation and LLM analysis | 360 | 🗄️ | Python |
| [seninja](https://github.com/borzacchiello/seninja) | Symbolic execution plugin for Binary Ninja | 358 | 🟢 | Python |
| [classinformer-ida7](https://github.com/rcx/classinformer-ida7) | ClassInformer RTTI plugin backported for IDA Pro 7 | 354 | 🔴 | C++ |
| [luadec51](https://github.com/sztupy/luadec51) | Lua decompiler for Lua 5.1 bytecode | 353 | 🔴 | C |
| [SkidSuite](https://github.com/GenericException/SkidSuite) | Collection of Java reverse engineering tools and reference links | 353 | 🟡 | Java |
| [IDA_ClassInformer_PlugIn](https://github.com/kweatherman/IDA_ClassInformer_PlugIn) | IDA ClassInformer plugin for MSVC RTTI and vftables | 351 | 🟢 | C++ |
| [abyss](https://github.com/patois/abyss) | Augments Hex-Rays decompiler output | 349 | 🔴 | Python |
| [DiztinGUIsh](https://github.com/DizTools/DiztinGUIsh) | Super NES ROM disassembler | 346 | 🟢 | C# |
| [gotools](https://github.com/felberj/gotools) | Ghidra plugin that helps reverse Go binaries | 344 | 🔴 | Java |
| [ida-minsc](https://github.com/arizvisa/ida-minsc) | Functional DWIM IDAPython plugin | 336 | 🟢 | Python |
| [d810](https://github.com/joydo/d810) | IDA Pro plugin to deobfuscate code at decompilation time | 335 | 🟡 | Python |
| [jsxer](https://github.com/AngeloD2022/jsxer) | Decompiler for Adobe ExtendScript JSXBIN files | 331 | 🟢 | C++ |
| [microavx](https://github.com/gaasedelen/microavx) | AVX lifter for the Hex-Rays decompiler | 331 | 🔴 | Python |
| [XRefer](https://github.com/mandiant/xrefer) | FLARE team binary navigator plugin for IDA Pro | 324 | 🟢 | Python |
| [replica](https://github.com/reb311ion/replica) | Ghidra analysis enhancer | 318 | 🔴 | Python |
| [ida_medigate](https://github.com/medigateio/ida_medigate) | IDA plugin for C++ class and vtable reverse engineering | 311 | 🔴 | Python |
| [super-jadx](https://github.com/pkilller/super-jadx) | Fork-style JADX extension adding renaming, reference graphs and other RE features | 311 | 🔴 | Java |
| [GhydraMCP](https://github.com/starsong-consulting/GhydraMCP) | Ghidra plugin with REST API and MCP bridge for agentic multi-binary reverse engineering | 306 | 🟢 | Python |
| [ProjectorRays](https://github.com/ProjectorRays/ProjectorRays) | Decompiler for Macromedia/Adobe Director and Shockwave Lingo | 306 | 🟢 | C++ |
| [0xdea ghidra-scripts](https://github.com/0xdea/ghidra-scripts) | Ghidra scripts for reverse engineering and vulnerability research | 302 | 🟢 | Java |
| [ida-batch_decompile](https://github.com/tintinweb/ida-batch_decompile) | IDA batch decompile plugin for Hex-Rays | 299 | 🔴 | Python |
| [ghidra-nativeaot](https://github.com/Washi1337/ghidra-nativeaot) | Ghidra plugin that analyzes .NET Native AOT binaries | 296 | 🟢 | Java |
| [IDACyber](https://github.com/patois/IDACyber) | Data visualization plugin for IDA Pro | 296 | 🔴 | Python |
| [LuaAssemblyTools](https://github.com/efrederickson/LuaAssemblyTools) | Lua bytecode assembly and disassembly tools | 286 | 🔴 | Lua |
| [abi-guesser](https://github.com/openchainxyz/abi-guesser) | Guesses Ethereum ABI from calldata without the contract ABI | 285 | 🔴 | TypeScript |
| [GhidraBoy](https://github.com/Gekkio/GhidraBoy) | Sharp SM83 / Game Boy extension for Ghidra | 285 | 🗄️ | Kotlin |
| [luajit-decomp](https://github.com/bobsayshilol/luajit-decomp) | LuaJIT decompiler | 272 | 🔴 | AutoIt |
| [Cafebabe](https://github.com/GraxCode/Cafebabe) | Java bytecode editor and decompiler GUI | 271 | 🔴 | Java |
| [jd-gui-duo](https://github.com/nbauma109/jd-gui-duo) | Multi-decompiler Java GUI supporting JD-Core, CFR, Procyon and Fernflower | 267 | 🟢 | Java |
| [Ghidra_GolangAnalyzerExtension](https://github.com/mooncat-greenpy/Ghidra_GolangAnalyzerExtension) | Ghidra extension to analyze Go binaries | 266 | 🟢 | Java |
| [iBoot64helper](https://github.com/argp/iBoot64helper) | IDAPython loader for AArch64 iBoot, iBEC and SecureROM reverse engineering | 266 | 🔴 | Python |
| [SMDA](https://github.com/danielplohmann/smda) | Recursive disassembler library optimized for accurate CFG recovery | 264 | 🟢 | Python |
| [ghidra-emotionengine-reloaded](https://github.com/chaoticgd/ghidra-emotionengine-reloaded) | Ghidra extension adding PlayStation 2 Emotion Engine support | 262 | 🟢 | Java |
| [sleighcraft](https://github.com/StarCrossPortal/sleighcraft) | Rust bindings and tools for Ghidra's SLEIGH disassembler | 262 | 🔴 | C++ |
| [friday](https://github.com/zifeihan/friday) | Java runtime decompiler for classes loaded in a running JVM | 248 | 🟡 | Java |
| [hexagon](https://github.com/gsmk/hexagon) | IDA processor module for the hexagon (QDSP6) processor | 241 | 🟡 | C |
| [eBPF-for-Ghidra](https://github.com/Nalen98/eBPF-for-Ghidra) | eBPF processor module for Ghidra | 237 | 🟡 | Java |
| [fadec](https://github.com/aengelke/fadec) | Fast, lightweight x86 and x86-64 decoder and encoder | 237 | 🟢 | Assembly |
| [dewolf](https://github.com/fkie-cad/dewolf) | Research decompiler implemented as a Binary Ninja plugin | 236 | 🟢 | Python |
| [abi-decompiler](https://github.com/Decurity/abi-decompiler) | Ethereum EVM smart contract ABI recovery helper | 231 | 🔴 | C |
| [FunctionInliner](https://github.com/cellebrite-labs/FunctionInliner) | An IDA plugin that eases reversing of binaries that have been code-size-optimized with function outlining | 230 | 🟡 | C |
| [hyperion-disassembler](https://github.com/Sidenai/hyperion-disassembler) | Native multi-arch disassembler and decompiler for PE, ELF and Mach-O | 230 | 🟢 | C++ |
| [NTRGhidra](https://github.com/pedro-javierf/NTRGhidra) | Nintendo DS binary loader for Ghidra | 229 | 🟢 | Java |
| [ghidra2dwarf](https://github.com/cesena/ghidra2dwarf) | Exports Ghidra decompiled code to DWARF sections in an ELF binary | 227 | 🟡 | Python |
| [ida-sigmaker](https://github.com/mahmoudimus/ida-sigmaker) | Cross-platform IDA Pro 9 signature maker plugin | 227 | 🟢 | Python |
| [bun-demincer](https://github.com/vicnaum/bun-demincer) | Decompiler and deobfuscator for Bun-compiled standalone JavaScript binaries | 225 | 🟢 | JavaScript |
| [pypcode](https://github.com/angr/pypcode) | Python bindings to Ghidra's SLEIGH for disassembly and P-Code lifting | 224 | 🟢 | C++ |
| [holodec](https://github.com/Cararasu/holodec) | Decompiler for x86 and x86-64 ELF binaries | 220 | 🔴 | C++ |
| [idaxex](https://github.com/emoose/idaxex) | XEX/XBE loader plugin for IDA supporting Xbox and Xbox 360 executables | 218 | 🟢 | C++ |
| [ApplySig](https://github.com/NWMonster/ApplySig) | Applies IDA FLIRT signatures in Ghidra | 214 | 🔴 | Python |
| [ai-reverse-engineering](https://github.com/biniamf/ai-reverse-engineering) | AI-assisted binary reverse engineering with Ghidra and LLMs | 213 | 🟢 | Python |
| [pyhidra](https://github.com/dod-cyber-crime-center/pyhidra) | Python library for direct access to the Ghidra API from CPython | 212 | 🟡 | Python |
| [rePy2exe](https://github.com/4w4k3/rePy2exe) | Reverse engineering tool for py2exe applications | 210 | 🔴 | Python |
| [AMIE](https://github.com/NeatMonster/AMIE) | Minimalist ARM instruction extender for IDA Pro | 204 | 🟡 | Python |
| [unfuck](https://github.com/landaire/unfuck) | Deobfuscator for obfuscated Python 2.7 bytecode | 204 | 🟢 | Rust |
| [BTD DNN decompiler](https://github.com/monkbai/DNN-decompiler) | Decompiles x86 deep neural network executables back to model structure and weights | 199 | 🟢 | Python |
| [standalone-app](https://github.com/helios-decompiler/standalone-app) | All-in-one Java reverse engineering tool | 196 | 🔴 | Java |
| [Dhrake](https://github.com/huettenhain/dhrake) | Ghidra scripts for reverse engineering Delphi binaries | 194 | 🟡 | Java |
| [sleigh](https://github.com/lifting-bits/sleigh) | Unofficial CMake build of Ghidra's C++ SLEIGH disassembly library | 194 | 🟢 | CMake |
| [java-disassembler](https://github.com/LLVM-but-worse/java-disassembler) | Java bytecode disassembler and class file viewer | 192 | 🟡 | Java |
| [ghidralib](https://github.com/msm-code/ghidralib) | Pythonic Ghidra standard library | 191 | 🟢 | Python |
| [capstone.js](https://github.com/AlexAltea/capstone.js) | JavaScript port of the Capstone disassembler framework | 190 | 🟢 | JavaScript |
| [jsc-decompile-mozjs-34](https://github.com/irelance/jsc-decompile-mozjs-34) | SpiderMonkey 34 JavaScript bytecode decoder and decompiler | 190 | 🔴 | PHP |
| [ida-iboot-loader](https://github.com/matteyeux/ida-iboot-loader) | IDA loader for Apple's 64 bits iBoot, SecureROM and AVPBooter | 182 | 🟡 | Python |
| [reverse_pyinstaller](https://github.com/MrWQ/reverse_pyinstaller) | Restores Python source from PyInstaller-packed executables | 181 | 🔴 | Python |
| [ceasta](https://github.com/ngwg/ceasta) | Disassembler, decompiler and debugger with built-in MCP server | 179 | 🟢 | C++ |
| [slicer](https://github.com/katana-project/slicer) | Web-based Java reverse engineering tool with multiple decompilers | 179 | 🟢 | Svelte |
| [vscode-decompiler](https://github.com/tintinweb/vscode-decompiler) | Decompile binaries and bytecode directly from VS Code | 179 | 🟢 | Python |
| [DelphiHelper](https://github.com/eset/DelphiHelper) | IDA Pro plugin for analysing Delphi binaries | 174 | 🟢 | Python |
| [SuperGhidra](https://github.com/yuatemycat/SuperGhidra) | Python RE suite: P-Code IR lifter, Z3 prover, binary loader, CFG deflattener and Ghidra tools | 170 | 🟢 | Python |
| [IDA-For-Delphi](https://github.com/Coldzer0/IDA-For-Delphi) | IDAPython script recovering Delphi VCL event function names | 169 | 🟡 | Python |
| [evm](https://github.com/MrLuit/evm) | Ethereum virtual machine (EVM) bytecode decompiler | 168 | 🔴 | TypeScript |
| [CrowdDetox](https://github.com/CrowdStrike/CrowdDetox) | Hex-Rays plugin removing junk code and variables | 166 | 🗄️ | C++ |
| [binja-retdec](https://github.com/hugsy/binja-retdec) | Binary Ninja plugin using RetDec to decompile | 165 | 🗄️ | Python |
| [Py2ExeDecompiler](https://github.com/endgameinc/Py2ExeDecompiler) | Decompiler for py2exe executables | 165 | 🔴 | C# |
| [semblance](https://github.com/zfigura/semblance) | Disassembler for 16-bit NE, MZ (DOS) and PE Windows executables | 163 | 🟡 | C |
| [ghidrecomp](https://github.com/clearbluejar/ghidrecomp) | Python command-line Ghidra decompiler | 160 | 🟢 | Python |
| [LazyGhidra](https://github.com/AllsafeCyberSecurity/LazyGhidra) | Ghidra plugin with helper scripts for common analysis tasks | 160 | 🔴 | Python |
| [PacXplorer](https://github.com/cellebrite-labs/PacXplorer) | IDA plugin to find code cross references to virtual functions using PAC codes | 160 | 🟢 | Python |
| [emilpro](https://github.com/SimonKagstrom/emilpro) | Graphical multi-architecture disassembler | 157 | 🟡 | C++ |
| [Semi-VB-Decompiler](https://github.com/VBGAMER45/Semi-VB-Decompiler) | Partial decompiler for Visual Basic 5/6 executables and their file structure | 157 | 🟢 | Visual Basic 6.0 |
| [gapstone](https://github.com/bnagy/gapstone) | Go bindings for the Capstone disassembly framework | 155 | 🔴 | Go |
| [ida_kernelcache](https://github.com/cellebrite-labs/ida_kernelcache) | An IDA Toolkit for analyzing iOS kernelcaches. | 155 | 🟢 | Python |
| [ida_missinglink](https://github.com/kweatherman/ida_missinglink) | IDA plugin filling in missing indirect CALL and JMP targets | 153 | 🟢 | C++ |
| [Capstone.NET](https://github.com/9ee1/Capstone.NET) | .NET bindings for the Capstone disassembly framework | 151 | 🟡 | C# |
| [IDA-VTableExplorer](https://github.com/K4ryuu/IDA-VTableExplorer) | IDA plugin for automatic vtable detection and inheritance analysis | 150 | 🟢 | C++ |
| [kaiju](https://github.com/cmu-sei/kaiju) | CERT Kaiju binary analysis extension for Ghidra | 148 | 🟢 | Java |
| [LabSync](https://github.com/cellebrite-labs/LabSync) | IDA plugin to partially synchronize IDBs between researchers | 146 | 🟡 | Python |
| [CollaRE](https://github.com/Martyx00/CollaRE) | Multi-tool reverse engineering collaboration solution | 143 | 🟡 | Python |
| [pyc2bytecode](https://github.com/knight0x07/pyc2bytecode) | Python bytecode disassembler for analysing compiled Python binaries | 143 | 🔴 | Python |
| [ghostrings](https://github.com/nccgroup/ghostrings) | Ghidra scripts recovering string definitions in Go binaries | 141 | 🟢 | Java |
| [Despector](https://github.com/Despector/Despector) | Java and Kotlin decompiler and AST library | 140 | 🗄️ | Java |
| [idp_hexagon](https://github.com/n-o-o-n/idp_hexagon) | Hexagon processor module for IDA Pro disassembler | 138 | 🟢 | C++ |
| [QtREAnalyzer](https://github.com/diommsantos/QtREAnalyzer) | Ghidra extension to reverse engineer Qt binaries | 138 | 🟡 | Java |
| [nuitka-static-unpacker](https://github.com/DimaReverse/nuitka-static-unpacker) | Static unpacker for analysing Nuitka-compiled binaries | 137 | 🟢 | Python |
| [pkg-unpacker](https://github.com/LockBlock-dev/pkg-unpacker) | Unpacks Node.js applications packaged with pkg | 136 | 🟢 | TypeScript |
| [ghidra-gekko-broadway-lang](https://github.com/aldelaro5/ghidra-gekko-broadway-lang) | Ghidra language for GameCube/Wii Gekko and Broadway CPUs | 135 | 🔴 |  |
| [ghidra-xbe](https://github.com/XboxDev/ghidra-xbe) | Xbox XBE executable loader for Ghidra | 130 | 🟢 | Java |
| [ghidrasql](https://github.com/0xeb/ghidrasql) | SQL interface for querying Ghidra program databases | 130 | 🟢 | C++ |
| [ObjCGraphView](https://github.com/trailofbits/ObjCGraphView) | Binary Ninja graph view plugin for Objective-C | 130 | 🔴 | Python |
| [x86devirt](https://github.com/JeremyWildsmith/x86devirt) | Automatic devirtualization of x86 VM-protected code | 129 | 🔴 | C++ |
| [dnEditor](https://github.com/ViRb3/dnEditor) | .NET assembly editor based on dnlib | 128 | 🗄️ | C# |
| [JavaDecompileTool-GUI](https://github.com/MountCloud/JavaDecompileTool-GUI) | GUI Java decompiler tool | 127 | 🔴 |  |
| [vm_jit](https://github.com/archercreat/vm_jit) | VM devirtualization proof of concept based on AsmJit and LLVM | 126 | 🔴 | C++ |
| [STRIDE](https://github.com/hgarrereyn/STRIDE) | Type recognition in decompiled executables | 125 | 🟡 | Python |
| [augur](https://github.com/0xdea/augur) | IDA assistant extracting strings and related pseudocode | 123 | 🟢 | Rust |
| [hexag00n](https://github.com/programa-stic/hexag00n) | Hexag00n: A collection of reverse engineering tools for the Qualcomm Digital Signal Proccesor (QDSP6) | 121 | 🔴 | Python |
| [jsdeob-workbench](https://github.com/Owl4444/jsdeob-workbench) | Visual workbench for deobfuscating JavaScript with chained AST transforms | 120 | 🟢 | JavaScript |
| [striga](https://github.com/LLVMParty/striga) | Experimental x86_64 to LLVM IR lifter in Python | 120 | 🟢 | Python |
| [binja-hexagon](https://github.com/google/binja-hexagon) | binja-hexagon | 118 | 🗄️ | Python |
| [idasec](https://github.com/RobinDavid/idasec) | IDA plugin for dynamic analysis with the Binsec platform | 117 | 🔴 | Python |
| [decompiler](https://github.com/ant4g0nist/decompiler) | Ghidra decompiler plugin for LLDB | 116 | 🟢 | C++ |
| [lst2x64dbg](https://github.com/utkonos/lst2x64dbg) | Exports labels from IDA, Ghidra, Binary Ninja and Relyze to x64dbg databases | 116 | 🟡 | Python |
| [pcode2code](https://github.com/Big5-sec/pcode2code) | Decompiles VBA p-code back to source, based on pcodedmp | 116 | 🔴 | Python |
| [decompile-py2exe](https://github.com/NVISOsecurity/decompile-py2exe) | Decompiles py2exe-generated Python 3 executables | 115 | 🔴 | Python |
| [HLSL-Decompiler](https://github.com/YYadorigi/HLSL-Decompiler) | Converts DXBC/DXIL/SPIR-V shaders to HLSL | 113 | 🟢 | CMake |
| [sol-azy](https://github.com/FuzzingLabs/sol-azy) | Static analysis and reverse engineering toolchain for Solana sBPF programs | 112 | 🟢 | Python |
| [fa](https://github.com/doronz88/fa) | Automation tool for locating symbols and structs in binaries | 111 | 🟢 | Python |
| [ScratchABlock](https://github.com/pfalcon/ScratchABlock) | Experimental decompiler framework | 110 | 🔴 | Python |
| [spedi](https://github.com/abenkhadra/spedi) | Speculative disassembly and CFG recovery from stripped binaries | 109 | 🔴 | C++ |
| [ida_gel](https://github.com/aerosoul94/ida_gel) | IDA loaders for game console ELFs (PS3, PS Vita, Wii U) | 106 | 🔴 | C |
| [erays](https://github.com/teamnsrg/erays) | Ethereum smart contract reverse engineering tool | 105 | 🔴 | Python |
| [nampa](https://github.com/thebabush/nampa) | FLIRT signatures for Binary Ninja | 102 | 🟢 | Python |
| [dsc_fix](https://github.com/deepinstinct/dsc_fix) | Aids reversing dyld_shared_cache libraries in IDA | 101 | 🔴 | Python |
| [revsync](https://github.com/lunixbochs/revsync) | Realtime cross-tool collaborative reverse engineering | 100 | 🔴 | Python |
| [NeverD](https://github.com/NeverSight/NeverD) | AI-friendly binary analysis and decompilation engine | 99 | 🟢 | C++ |
| [collabREate](https://github.com/cseagle/collabREate) | Collaborative reverse engineering plugin for IDA Pro | 98 | 🔴 | C++ |
| [GhidraFindcrypt](https://github.com/antoniovazquezblanco/GhidraFindcrypt) | Ghidra plugin locating cryptographic constants | 98 | 🟢 | Java |
| [ghidra-snes](https://github.com/joshleaves/ghidra-snes) | Ghidra scripts for SNES ROM reverse engineering | 95 | 🟢 | Java |
| [HlslDecompiler](https://github.com/AndresTraks/HlslDecompiler) | Decompiles Shader Model 1-5 shader bytecode into HLSL | 95 | 🟢 | C# |
| [NotDec](https://github.com/NotDec/NotDec) | WebAssembly decompiler and static analysis framework on LLVM IR | 95 | 🟢 | C++ |
| [Trinity](https://github.com/firstfault/Trinity) | Software reverse engineering tool for Java | 94 | 🟢 | Java |
| [wcdatool](https://github.com/fonic/wcdatool) | Watcom disassembly tool for DOS applications | 92 | 🟢 | Python |
| [bn-dyldsharedcache](https://github.com/0cyn/bn-dyldsharedcache) | this was a single-image DSC parser predating official support for DSC support in binaryninja. | 91 | 🟢 | Python |
| [GhidraVitaLoader](https://github.com/xerpi/GhidraVitaLoader) | VitaLoader script for loading PS Vita binaries in Ghidra | 86 | 🔴 | Java |
| [ghidra-lx-loader](https://github.com/yetmorecode/ghidra-lx-loader) | Ghidra loader for LX/LE executables (OS/2, DOS4GW, VxD) | 85 | 🟢 | Java |
| [RET](https://github.com/futo-org/ret) | FUTO's reverse-engineering tool | 85 | 🟢 | C |
| [DnD](https://github.com/purseclab/DnD) | Decompiler that recovers DNN model semantics from compiled binaries | 83 | 🟡 | Python |
| [ObjectiveNinja](https://github.com/jonpalmisc/ObjectiveNinja) | Binary Ninja plugin & workflow to help analyze Objective-C code | 82 | 🗄️ | C++ |
| [ida-nativeaot](https://github.com/Dump-GUY/ida-nativeaot) | IDA Pro plugin that recovers .NET Native AOT metadata | 79 | 🟢 | Python |
| [PjOrion-Deobfuscator](https://github.com/extremecoders-re/PjOrion-Deobfuscator) | Deobfuscator for PjOrion-protected Python scripts | 78 | 🔴 | Python |
| [webpackTools](https://github.com/moonlight-mod/webpackTools) | Userscript for reverse engineering and modifying production webpack apps | 78 | 🟢 | JavaScript |
| [herast](https://github.com/Mizari/herast) | Framework to automate Hex-Rays AST work in IDA Pro | 76 | 🟡 | Python |
| [IFPSTools.NET](https://github.com/Wack0/IFPSTools.NET) | Tools to assemble and disassemble RemObjects PascalScript (Inno Setup) files | 76 | 🟢 | C# |
| [awake](https://github.com/devdri/awake) | Decompiler for Game Boy ROMs | 75 | 🔴 | Python |
| [QtRE](https://github.com/OSUSecLab/QtRE) | Ghidra headless analyzer for Qt binaries | 75 | 🟡 | Java |
| [aevt_decompile](https://github.com/SentineLabs/aevt_decompile) | Decompiler for run-only AppleScript files | 74 | 🔴 | Objective-C |
| [unluac-rs](https://github.com/x3zvawq/unluac-rs) | Cross-platform Rust Lua decompilation library for multiple dialects | 73 | 🟢 | Rust |
| [idapcode](https://github.com/binarly-io/idapcode) | IDA plugin displaying Ghidra P-code for the current function | 72 | 🟢 | Python |
| [dynlib](https://github.com/aerosoul94/dynlib) | IDA Pro plugin for PS4 user-mode ELF reverse engineering | 71 | 🔴 | C |
| [ghidra-wasm-plugin](https://github.com/garrettgu10/ghidra-wasm-plugin) | Ghidra WebAssembly plugin with disassembly and decompilation | 69 | 🔴 | Java |
| [jsdec](https://github.com/rizinorg/jsdec) | Simple decompiler for Rizin | 67 | 🟢 | JavaScript |
| [JustDecompileEngine](https://github.com/codemerx/JustDecompileEngine) | Decompilation engine of CodemerxDecompile | 66 | 🟡 | C# |
| [ptxNinja](https://github.com/seekbytes/ptxNinja) | Binary Ninja plugin for NVIDIA PTX | 65 | 🟢 | Rust |
| [dx-shader-decompiler](https://github.com/aizvorski/dx-shader-decompiler) | Decompiler for DirectX 9 shaders | 64 | 🔴 | Python |
| [pdbgen](https://github.com/wandel/pdbgen) | Generates PDB files from Ghidra | 62 | 🟡 | C++ |
| [seprom-loader](https://github.com/matteyeux/seprom-loader) | Binary Ninja loader for 64 bits Apple SEPROMs | 61 | 🟡 | Python |
| [waterbear](https://github.com/wtetzner/waterbear) | Assembler and disassembler for the Dreamcast VMU's LC86K CPU | 60 | 🟢 | Rust |
| [MBBSDASM](https://github.com/mbbsemu/MBBSDASM) | x86 disassembler for 16-bit NE executables, used to emulate The Major BBS | 56 | 🟢 | C# |
| [IDR](https://github.com/tmcdos/IDR) | Interactive Delphi Reconstructor (Pascal version) | 54 | 🔴 | Pascal |
| [TypeForge](https://github.com/noobone123/TypeForge) | Synthesizes composite data types for stripped binaries (Ghidra-based research tool) | 53 | 🟢 | Java |
| [gm81decompiler](https://github.com/WastedMeerkat/gm81decompiler) | GameMaker 8.1 decompiler | 52 | 🔴 | C++ |
| [PbdViewer](https://github.com/Hucxy/PbdViewer) | Decompiler and viewer for PowerBuilder PBD/PBL libraries | 50 | 🟢 | C# |
| [ghidra-fr60](https://github.com/desrdev/ghidra-fr60) | Ghidra processor plugin for Fujitsu FR60 CPUs, focused on the Sony PSX DVR MB91302A | 45 | 🟢 | Java |
| [paranoia](https://github.com/Altumptic/paranoia) | Offline RE tool for PE/ELF/Mach-O on x86/x64/AArch64 with graphs and pseudocode | 44 | 🟢 | Rust |
| [r2unity](https://github.com/radareorg/r2unity) | Reverse engineer Unity games with radare2 | 42 | 🟢 | C |
| [ida-swarm](https://github.com/shells-above/ida-swarm) | Multi-agent AI system for automated reverse engineering in IDA | 41 | 🟢 | C++ |
| [binja_kc](https://github.com/skr0x1c0/binja_kc) | Plugin for loading MachO kernelcache and dSYM files to Binary Ninja | 38 | 🟡 | C++ |
| [sephelper](https://github.com/haiyuidesu/sephelper) | IDA loader to help with SEPROM reverse engineering. | 36 | 🟡 | Python |
| [iBoot-Binja-Loader](https://github.com/EliseZeroTwo/iBoot-Binja-Loader) | iBoot/SecureROM Loader | 35 | 🔴 | Python |
| [jscd](https://github.com/ejfkdev/jscd) | Static Rust decompiler from bytenode .jsc (V8 code cache) back to JavaScript | 33 | 🟢 | Rust |
| [hexpyrion](https://github.com/DimaReverse/hexpyrion) | Static source recovery for Nuitka-compiled Python binaries | 25 | 🟢 | Python |
| [jsd](https://github.com/jar-analyzer/jsd) | Pure TypeScript Java class file decompiler with no native dependencies | 22 | 🟢 | TypeScript |
| [BinaryNinja-PSVitaLoader](https://github.com/computerman00/BinaryNinja-PSVitaLoader) | PS Vita ELF/PRX2 loader plugin with symbol resolution for Binary Ninja | 21 | 🟡 | Python |
| [Acrab](https://github.com/SpartanB312/Acrab) | JVM and Android reverse engineering toolkit | 14 | 🟢 | Kotlin |
| [GhidraGarminApp](https://github.com/anvilsecure/GhidraGarminApp) | Ghidra processor and loader for Garmin Connect IQ watch applications | 13 | 🟢 | HTML |
| [f2mc8dasm](https://github.com/mnaberez/f2mc8dasm) | Disassembler for Cypress (Fujitsu) F2MC-8 microcontrollers | 12 | 🟢 | Python |
| [tonguetwister](https://github.com/lham/tonguetwister) | Macromedia Director file disassembler, Lingo decompiler and format documentation | 12 | 🔴 | Python |
| [ghidra-decompiler (Rust)](https://github.com/koute/ghidra-decompiler) | Pure Rust port of the Ghidra decompiler | 9 | 🟢 | Rust |
| [visualbasic-rs](https://github.com/ATRAPSLLC/visualbasic-rs) | Rust library to parse and inspect compiled Visual Basic 6 binaries | 3 | 🟢 | Rust |
| [dzasm](https://gitlab.com/b4works/dzasm) | Reverse engineering tool for Z80 executable binaries |  | ⚪ |  |
| [PyReveng3](https://codeberg.org/Datamuseum-dk/PyReveng3) | Python toolkit for reverse engineering old computer artifacts and firmware |  | ⚪ |  |
| [reoxide](https://codeberg.org/ReOxide/reoxide) | Plugin system for the Ghidra decompiler |  | ⚪ |  |
| [unkempt86](https://codeberg.org/NonSquarePixels/unkempt86) | Interpreter-driven disassembler and reverse engineering tool for MS-DOS MZ executables |  | ⚪ |  |

## Dynamic Instrumentation

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Frida](https://github.com/frida/frida) | Dynamic instrumentation toolkit for native apps | 22,569 | 🟢 | Meson |
| [rr](https://github.com/rr-debugger/rr) | Record and replay debugger for Linux | 10,728 | 🟢 | C++ |
| [Unicorn](https://github.com/unicorn-engine/unicorn) | Lightweight multi-architecture CPU emulator framework | 9,518 | 🟢 | C |
| [GEF](https://github.com/hugsy/gef) | GDB extension that adds dynamic-analysis commands and context views | 8,415 | 🟢 | Python |
| [Triton](https://github.com/JonathanSalwan/Triton) | Dynamic binary analysis library with symbolic execution | 4,353 | 🟢 | C++ |
| [HyperDbg](https://github.com/HyperDbg/HyperDbg) | Hypervisor-based native debugger for reverse engineering | 4,168 | 🟢 | C |
| [QIRA](https://github.com/geohot/qira) | Timeless debugger that records and lets you browse full program execution | 4,070 | 🔴 | C |
| [sogen](https://github.com/momo5502/sogen) | Windows and Linux userspace emulator for analysis | 3,870 | 🟢 | C++ |
| [DynamoRIO](https://github.com/DynamoRIO/dynamorio) | Dynamic binary instrumentation tool platform | 3,194 | 🟢 | C |
| [PINCE](https://github.com/korcankaraokcu/PINCE) | GDB front-end and memory scanner for reverse engineering games on Linux | 3,137 | 🟢 | Python |
| [edb](https://github.com/eteran/edb-debugger) | Cross-platform x86/x86-64 GUI debugger | 2,979 | 🟢 | C++ |
| [panda](https://github.com/panda-re/panda) | Platform for architecture-neutral dynamic analysis built on QEMU | 2,793 | 🟢 | C |
| [Textractor](https://github.com/Artikash/Textractor) | Text hooker that extracts text from running games and visual novels on Windows | 2,711 | 🟡 | C++ |
| [NPatch](https://github.com/7723mod/NPatch) | Rootless Xposed framework based on LSPosed, recreated from LSPatch | 2,651 | 🟢 | Kotlin |
| [lighthouse](https://github.com/gaasedelen/lighthouse) | Code coverage explorer plugin for IDA and Binary Ninja | 2,609 | 🟢 | Python |
| [frida-snippets](https://github.com/iddoeldor/frida-snippets) | Hand-crafted Frida examples | 2,540 | 🟡 | JavaScript |
| [Speakeasy](https://github.com/mandiant/speakeasy) | Windows kernel and user-mode emulation framework for PE files and shellcode | 2,096 | 🟢 | Python |
| [QBDI](https://github.com/QBDI/QBDI) | LLVM-based dynamic binary instrumentation framework | 1,834 | 🟢 | C++ |
| [tiny_tracer](https://github.com/hasherezade/tiny_tracer) | Intel Pin tool for tracing API calls | 1,713 | 🟢 | C++ |
| [PyREBox](https://github.com/Cisco-Talos/pyrebox) | Python-scriptable RE sandbox built on QEMU for VM instrumentation and inspection | 1,685 | 🗄️ | C |
| [0xdea frida-scripts](https://github.com/0xdea/frida-scripts) | Frida instrumentation scripts for reverse engineering mobile apps | 1,683 | 🟢 | JavaScript |
| [tenet](https://github.com/gaasedelen/tenet) | Execution trace explorer plugin for IDA Pro | 1,547 | 🔴 | Python |
| [r2frida](https://github.com/nowsecure/r2frida) | Radare2 and Frida integration | 1,450 | 🟢 | TypeScript |
| [TinyInst](https://github.com/googleprojectzero/TinyInst) | Lightweight dynamic instrumentation library for Windows, macOS, Linux | 1,360 | 🟢 | C++ |
| [Dwarf](https://github.com/iGio90/Dwarf) | Multi-arch debugger built on PyQt5 and Frida | 1,321 | 🟡 | Python |
| [frida-ios-hook](https://github.com/yazgx97/frida-ios-hook) | Frida-based tool to trace and modify iOS app methods | 1,192 | 🟢 | JavaScript |
| [dumpulator](https://github.com/mrexodia/dumpulator) | Library for emulating code from Windows memory dumps | 890 | 🟡 | C |
| [ksm](https://github.com/asamy/ksm) | x64 VT-x hypervisor for Windows and Linux with sandbox and introspection engine | 870 | 🔴 | C |
| [HookCase](https://github.com/steven-michaud/HookCase) | Tool for hooking and reverse engineering macOS / OS X processes | 842 | 🟢 | C++ |
| [Dyninst](https://github.com/dyninst/dyninst) | Binary instrumentation, analysis and modification libraries | 840 | 🟢 | C |
| [hyper-reV](https://github.com/noahware/hyper-reV) | Hyper-V based hypervisor for memory introspection and reverse engineering | 835 | 🟢 | C++ |
| [iMonitor](https://github.com/wecooperate/iMonitor) | Windows endpoint behavior monitor (open procmon) for system activity analysis | 835 | 🟢 | C++ |
| [ReverseKit](https://github.com/zer0condition/ReverseKit) | x64 dynamic reverse engineering toolkit with import, syscall and hook views | 793 | 🔴 | C++ |
| [deREferencing](https://github.com/danigargu/deREferencing) | IDA Pro plugin with friendlier register and stack views while debugging | 778 | 🟢 | Python |
| [lisa.py](https://github.com/ant4g0nist/lisa.py) | LLDB MCP integration and helper commands for reverse engineering | 756 | 🟡 | Python |
| [makin](https://github.com/secrary/makin) | Tool that reveals anti-debugging and anti-VM checks in Windows binaries | 743 | 🔴 | C++ |
| [ellekit](https://github.com/tealbathingsuit/ellekit) | yet another tweak injector / tweak hooking library for darwin systems | 729 | 🟢 | Swift |
| [Spice86](https://github.com/OpenRakis/Spice86) | PC emulator built for reverse engineering and rewriting real-mode DOS programs | 671 | 🟢 | C# |
| [Il2CppHookScripts](https://github.com/axhlzy/Il2CppHookScripts) | Frida scripts that parse libil2cpp.so at runtime in Unity games | 664 | 🟢 | TypeScript |
| [frinet](https://github.com/synacktiv/frinet) | Frida-based execution tracer for Android, iOS, Linux and Windows | 637 | 🟢 | Rust |
| [unicorn.js](https://github.com/AlexAltea/unicorn.js) | JavaScript port of the Unicorn CPU emulator framework | 606 | 🟢 | JavaScript |
| [cryptoshark](https://github.com/frida-labs/cryptoshark) | Self-optimizing code tracer based on dynamic recompilation | 602 | 🗄️ | C++ |
| [ttddbg](https://github.com/airbus-cert/ttddbg) | Time Travel Debugging trace plugin for IDA | 598 | 🟡 | C++ |
| [PinTools](https://github.com/JonathanSalwan/PinTools) | Intel Pin tools for dynamic binary analysis | 593 | 🔴 | C++ |
| [vscode-frida](https://github.com/ChiChou/vscode-frida) | Unofficial Frida extension for VS Code | 591 | 🟢 | TypeScript |
| [substitute](https://github.com/comex/substitute) | A free runtime modification library. | 589 | 🔴 | C |
| [binee](https://github.com/carbonblack/binee) | Binary emulation environment for Windows PE files | 531 | 🔴 | Go |
| [s2e](https://github.com/S2E/s2e) | Platform for multi-path program analysis with selective symbolic execution | 527 | 🟢 | C++ |
| [wirebrowser](https://github.com/fcavallarin/wirebrowser) | CDP-based runtime instrumentation platform for browsers | 509 | 🟢 | JavaScript |
| [PaiMei](https://github.com/OpenRCE/paimei) | Python reverse engineering framework (debugger, stalker, IDA integration) | 508 | 🔴 | Python |
| [PinCTF](https://github.com/ChrisTheCoolHut/PinCTF) | Uses Intel PIN instruction counting to solve CTF reversing challenges | 507 | 🔴 | Python |
| [llef](https://github.com/foundryzero/llef) | LLDB plugin making it more useful for reverse engineering | 490 | 🟢 | Python |
| [xpcspy](https://github.com/ab-rizk/xpcspy) | Bidirectional XPC message interception on macOS/iOS, powered by Frida | 452 | 🟢 | TypeScript |
| [udbserver](https://github.com/bet4it/udbserver) | GDB debug server for the Unicorn emulator | 436 | 🟢 | Rust |
| [Zelos](https://github.com/zeropointdynamics/zelos) | Binary emulation and instrumentation platform | 420 | 🔴 | Python |
| [drltrace](https://github.com/mxmssh/drltrace) | DynamoRIO-based library call tracer for Windows and Linux | 419 | 🔴 | HTML |
| [Simpleator](https://github.com/ionescu007/Simpleator) | Windows x64 user-mode application emulator using Hyper-V | 404 | 🔴 | C++ |
| [XprobePlugin](https://github.com/johnno1962/XprobePlugin) | Live memory browser for iOS and macOS apps in Xcode | 398 | 🟡 | Objective-C++ |
| [heretek](https://github.com/wcampbell0x2a/heretek) | GDB TUI dashboard for remote debugging of embedded targets | 397 | 🟢 | Rust |
| [gdb-static](https://github.com/hugsy/gdb-static) | Statically compiled GDB and gdbserver binaries for many architectures | 396 | 🔴 |  |
| [Frida-Script-Runner](https://github.com/z3n70/Frida-Script-Runner) | Web-based Frida toolkit for Android and iOS | 383 | 🟢 | JavaScript |
| [crawler-js-hook-framework](https://github.com/JSREI/crawler-js-hook-framework-public) | JavaScript hook toolkit for web reverse engineering | 382 | 🔴 |  |
| [STrace](https://github.com/mandiant/STrace) | DTrace on Windows reimplementation for syscall tracing | 379 | 🟢 | C++ |
| [rgat](https://github.com/ncatlin/rgat) | Instruction trace visualisation tool for dynamic analysis | 371 | 🔴 | C# |
| [Interruptor](https://github.com/FrenchYeti/interruptor) | System call tracing and hooking library based on Frida's Stalker | 361 | 🟢 | TypeScript |
| [agent (text hooker)](https://github.com/0xDC00/agent) | Frida-based text hooker for games and visual novels on emulators | 359 | 🟡 |  |
| [Binary Ninja debugger](https://github.com/Vector35/debugger) | Open-source debugger plugin for Binary Ninja | 338 | 🟢 | C++ |
| [JDBG](https://github.com/roger1337/JDBG) | Java dynamic reverse engineering and debugging tool via injected DLL | 332 | 🟡 | C++ |
| [bread](https://github.com/Theldus/bread) | BIOS reverse engineering and debugging over serial with GDB support | 329 | 🟡 | C |
| [execution-trace-viewer](https://github.com/teemu-l/execution-trace-viewer) | Tool for viewing and analyzing execution traces | 324 | 🔴 | Python |
| [gdbghidra](https://github.com/Comsecuris/gdbghidra) | Visual bridge between a GDB session and Ghidra | 324 | 🔴 | Java |
| [mwemu](https://github.com/mwemuorg/mwemu) | x86/x64 and AArch64 emulator for PE, ELF and Mach-O investigation with Windows API models | 319 | 🟢 | Rust |
| [libdebug](https://github.com/libdebug/libdebug) | Python library to script debugging of Linux binary executables | 315 | 🟢 | Python |
| [GhidraEmu](https://github.com/Nalen98/GhidraEmu) | Native P-code emulator plugin for Ghidra | 308 | 🟡 | Java |
| [Cmulator](https://github.com/Coldzer0/Cmulator) | Scriptable x86/x64 sandbox emulator for shellcode and PE binaries (Unicorn) | 304 | 🗄️ | Pascal |
| [GodHook](https://github.com/Szymou/GodHook) | Xposed plugin that exposes Android app functions over HTTP | 302 | 🟡 |  |
| [Syser](https://github.com/marakew/syser) | Syser ring-3 debugger for x86/x64 Windows with source-level debugging | 301 | 🟡 | C++ |
| [frick](https://github.com/iGio90/frick) | Debugger built on top of Frida | 296 | 🔴 | Python |
| [Shed](https://github.com/enkomio/shed) | .NET runtime inspector that dumps objects and assemblies from running processes | 275 | 🔴 | C# |
| [Reloaded.Hooks](https://github.com/Reloaded-Project/Reloaded.Hooks) | Native x86/x64 function hooking library for C# | 253 | 🟡 | C# |
| [fripack](https://github.com/std-microblock/fripack) | Packages Frida scripts into standalone executables | 232 | 🟢 | Rust |
| [flameox](https://github.com/morluto/flameox) | Runtime profiler from the REA author that gives agents traces and hotspot evidence | 228 | 🟢 | Python |
| [goauld](https://github.com/androguard/goauld) | Dynamic injection tool for Linux and Android | 228 | 🟡 | Rust |
| [ntoseye](https://github.com/dmaivel/ntoseye) | WinDbg-like Windows kernel debugger that runs from Linux and macOS | 228 | 🟢 | Rust |
| [emudbg](https://github.com/mojtabafalleh/emudbg) | Windows emulator and debugger for reverse engineering executables | 214 | 🟢 | C++ |
| [Unicorn-Trace](https://github.com/chenxvb/Unicorn-Trace) | Unicorn-based ARM64 dynamic tracing tool with IDA integration | 211 | 🟢 | Python |
| [AndroidPrybar](https://github.com/GitKittys/AndroidPrybar) | Android native tracing and reverse engineering tool for function wrapping and instruction tracing | 204 | 🟢 | C++ |
| [vegvisir](https://github.com/ant4g0nist/vegvisir) | Browser-based GUI for the LLDB debugger | 198 | 🗄️ | JavaScript |
| [RESim](https://github.com/mfthomps/RESim) | Reverse engineering software using a full-system Simics simulator | 195 | 🟢 | Python |
| [uDdbg](https://github.com/iGio90/uDdbg) | GDB-like debugger for the Unicorn emulator | 195 | 🔴 | Python |
| [FridaHooker](https://github.com/wrlu/FridaHooker) | Android Frida GUI manager | 183 | 🗄️ | Java |
| [fridax](https://github.com/NorthwaveSecurity/fridax) | Frida tooling to read variables and hook functions in Xamarin/Mono apps | 181 | 🔴 | JavaScript |
| [EHook](https://github.com/nevermoe/EHook) | Hooking framework for commercial Android emulators (LDPlayer, NOX, BlueStacks) | 174 | 🔴 | C |
| [gxpc](https://github.com/ReverseApple/gxpc) | Sniffs macOS/iOS XPC communication using Frida and Go | 167 | 🟢 | TypeScript |
| [pyda](https://github.com/ndrewh/pyda) | Write dynamic binary analysis tools in Python | 158 | 🟡 | C |
| [frida-analykit](https://github.com/ZSA233/frida-analykit) | Frida toolkit for Android reverse engineering | 156 | 🟢 | Python |
| [iostrace](https://github.com/sh1ma/iostrace) | strace alternative for 64-bit iOS devices using Frida | 154 | 🗄️ | JavaScript |
| [ida-splode](https://github.com/zachriggle/ida-splode) | Augments IDA static analysis with Pin-based dynamic instrumentation | 133 | 🔴 | C++ |
| [Gx64Sync](https://github.com/diommsantos/Gx64Sync) | Plugins that synchronize Ghidra and x64dbg | 131 | 🟢 | C++ |
| [Frida-Beautify-Output](https://github.com/Miracles666/Frida-Beautify-Output) | Vue web UI that runs Android Frida hooks and pretty-prints results | 125 | 🔴 | JavaScript |
| [ghostwire](https://github.com/sofianeelhor/ghostwire) | Stealth runtime instrumentation and CDP for web reverse engineering | 125 | 🟢 | Python |
| [jdwp-injector-for-android](https://github.com/wuyr/jdwp-injector-for-android) | Debugger-based code injection on Android via ADB and JDWP | 118 | 🟡 | Kotlin |
| [frida-il2cpp](https://github.com/AeonLucid/frida-il2cpp) | Helper library for inspecting Unity IL2CPP games with Frida | 109 | 🔴 | TypeScript |
| [Taint-Rev-Trace](https://github.com/Aar0n3906/Taint-Rev-Trace) | ARM trace taint tracking and search tool with MCP support | 100 | 🟢 | Rust |
| [XPCSniffer](https://github.com/evilpenguin/XPCSniffer) | Sniffs XPC messages on iOS devices | 95 | 🔴 | C |
| [frida-inject](https://github.com/freehuntx/frida-inject) | Injects JavaScript or TypeScript agents into processes with Frida, bundled on the fly | 81 | 🟢 | TypeScript |
| [jvm-dump-proxy](https://github.com/ViRb3/jvm-dump-proxy) | Proxy DLL dumping JVM classes at the JNI level on Windows | 81 | 🗄️ | C |
| [koidbg](https://github.com/keowu/koidbg) | Debugger for Windows ARM64 aimed at reverse engineers | 73 | 🗄️ | C++ |
| [frida-stack](https://github.com/rednaga/frida-stack) | Better stacks and backtraces in Frida | 64 | 🟢 | TypeScript |
| [frida-js](https://github.com/httptoolkit/frida-js) | Pure-JS bindings to control Frida from Node.js and browsers | 49 | 🟢 | TypeScript |
| [snixpc](https://github.com/tony-go/snixpc) | XPC message sniffer for macOS using LLDB | 49 | 🟡 | Python |
| [vutrace](https://github.com/chaoticgd/vutrace) | PlayStation 2 vector unit tracing debugger | 38 | 🟡 | C |
| [kvdb](https://github.com/DaveeFTW/kvdb) | GDB-compatible debugger for the PS Vita | 35 | 🔴 | C++ |
| [WinTTD](https://github.com/Colton1skees/WinTTD) | Reverse-engineered API for Microsoft's Time Travel Debugger | 35 | 🟡 | C++ |
| [NitroDebugger](https://github.com/pleonex/NitroDebugger) | Remote debugger for Nintendo DS games running in emulators | 33 | 🗄️ | C# |
| [frida-mcp](https://github.com/yfe404/frida-mcp) | Frida MCP server with persistent instrumentation sessions for runtime inspection of apps | 26 | 🟢 | TypeScript |
| [FridaForge](https://github.com/noobexon1/FridaForge) | Plugin that generates Frida snippets from IDA Pro, Binary Ninja and Ghidra | 10 | 🟢 | Python |
| [frida-il2cpp-proto-dumper](https://github.com/repinek/frida-il2cpp-proto-dumper) | Dumps protobuf-net messages from IL2CPP Unity games into .proto files with Frida | 9 | 🟢 | TypeScript |
| [NitroFilcher](https://github.com/pleonex/NitroFilcher) | Finds which files a Nintendo DS game reads at runtime | 5 | 🗄️ | C# |
| [xiotrace](https://codeberg.org/neuschaefer/xiotrace) | XNU I/O tracer based on xnuspy for tracing Apple device drivers |  | ⚪ |  |

## Mobile RE

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [jadx](https://github.com/skylot/jadx) | Dex to Java decompiler for Android apps | 51,405 | 🟢 | Java |
| [Apktool](https://github.com/iBotPeaches/Apktool) | Tool for reverse engineering Android APK files | 26,853 | 🟢 | Java |
| [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | Static and dynamic analysis framework for Android and iOS app packages | 22,085 | 🟢 | Python |
| [dex2jar](https://github.com/pxb1988/dex2jar) | Tools to convert Android .dex to Java .class files | 13,156 | 🟡 | Java |
| [Il2CppDumper](https://github.com/Perfare/Il2CppDumper) | Unity il2cpp metadata dumper for reverse engineering | 9,587 | 🟡 | C# |
| [objection](https://github.com/sensepost/objection) | Runtime mobile exploration toolkit powered by Frida | 9,476 | 🟢 | Python |
| [AssetRipper](https://github.com/AssetRipper/AssetRipper) | Extracts Unity serialized assets and projects | 8,788 | 🟢 | C# |
| [LAMDA](https://github.com/firerpa/lamda) | Android device control platform with remote desktop, automation, MITM and built-in Frida | 8,695 | 🟢 | Python |
| [Androguard](https://github.com/androguard/androguard) | Python toolkit for Android app analysis | 6,392 | 🟢 | Python |
| [hooker](https://github.com/CreditTone/hooker) | Frida-based Android reverse engineering toolkit with CLI and universal scripts | 5,334 | 🟢 | JavaScript |
| [unidbg](https://github.com/zhkl0228/unidbg) | Emulates Android native libraries (and experimentally iOS) to run app signing code | 5,300 | 🟢 | Java |
| [GDA](https://github.com/charles2gan/GDA-android-reversing-Tool) | Windows-native Dalvik decompiler and Android analysis workbench | 4,873 | 🟢 | Python |
| [apkstudio](https://github.com/vaibhavpandeyvpz/apkstudio) | Cross-platform Qt IDE for reverse engineering and rebuilding Android APKs | 4,708 | 🟢 | C++ |
| [simplify](https://github.com/CalebFenton/simplify) | Android virtual machine and generic Dalvik deobfuscator | 4,676 | 🔴 | Java |
| [WeChatOpenDevTools-Python](https://github.com/JaveleyQAQ/WeChatOpenDevTools-Python) | Forces the developer tools open in WeChat mini programs and built-in browser | 4,232 | 🟡 | Python |
| [APKLab](https://github.com/APKLab/APKLab) | Android reverse-engineering workbench for VS Code (apktool, jadx, smali) | 4,047 | 🟢 | TypeScript |
| [apk.sh](https://github.com/ax/apk.sh) | Bash script automating pull, decode, rebuild and Frida-gadget patching of Android APKs | 3,860 | 🟢 | Shell |
| [android-hidden-api](https://github.com/anggrayudi/android-hidden-api) | Library providing access to Android hidden APIs and internal resources | 3,625 | 🟢 | Java |
| [class-dump](https://github.com/nygard/class-dump) | Generates Objective-C headers from Mach-O files | 3,587 | 🔴 | Objective-C |
| [wedecode](https://github.com/biggerstar/wedecode) | Decompiler that restores WeChat mini program .wxapkg packages to source code | 3,354 | 🟢 | TypeScript |
| [Zygisk-Il2CppDumper](https://github.com/Perfare/Zygisk-Il2CppDumper) | Dumps IL2CPP metadata at runtime on Android via Zygisk | 3,352 | 🟡 | C |
| [Malimite](https://github.com/LaurieWired/Malimite) | Decompiler for iOS and macOS apps (IPA/Mach-O) built on Ghidra | 3,234 | 🟡 | Java |
| [RMS-Runtime-Mobile-Security](https://github.com/m0bilesecurity/RMS-Runtime-Mobile-Security) | Frida-based web UI to manipulate Android and iOS apps at runtime | 3,138 | 🟢 | JavaScript |
| [Cpp2IL](https://github.com/SamboyCoding/Cpp2IL) | Recovers managed .NET assemblies from Unity IL2CPP builds | 3,076 | 🟢 | C# |
| [Il2CppInspector](https://github.com/djkaty/Il2CppInspector) | Automated reverse-engineering tool for Unity IL2CPP binaries | 3,061 | 🔴 | C |
| [blutter](https://github.com/worawit/blutter) | Flutter app reverse engineering tool that recovers Dart objects and functions from libapp.so | 2,797 | 🟢 | C++ |
| [reFlutter](https://github.com/Impact-I/reFlutter) | Flutter reverse engineering framework that patches libflutter to expose Dart snapshot info | 2,793 | 🟢 | Python |
| [ASC](https://github.com/MG1937/ASC) | On-demand Android decompiler front-end, much faster than JADX | 2,612 | 🟢 | Python |
| [UABEA](https://github.com/nesrak1/UABEA) | Unity Asset Bundle Extractor Avalonia: view and edit Unity assets | 2,467 | 🟢 | C# |
| [APKEditor](https://github.com/REAndroid/APKEditor) | APK editor that decodes binary resources and DEX into editable JSON, XML and smali | 2,395 | 🟢 | Java |
| [MEDUSA](https://github.com/Ch0pin/medusa) | Modular Frida-based framework for runtime analysis of Android and iOS apps | 2,365 | 🟢 | JavaScript |
| [jnitrace](https://github.com/chame1eon/jnitrace) | Frida-based tracer for JNI API usage in Android apps | 1,865 | 🔴 | TypeScript |
| [frida-il2cpp-bridge](https://github.com/vfsfitvnm/frida-il2cpp-bridge) | Frida module to dump and trace IL2CPP Unity apps at runtime | 1,761 | 🟢 | TypeScript |
| [AppMon](https://github.com/dpnishant/appmon) | Frida-based monitoring and tampering of system API calls in Android, iOS and macOS apps | 1,634 | 🗄️ | JavaScript |
| [AndroidAppRE](https://github.com/maddiestone/AndroidAppRE) | Android app reverse engineering workshop | 1,570 | 🟡 |  |
| [FridaContainer](https://github.com/deathmemory/FridaContainer) | Modular Frida scripts for Android Java and JNI tracing | 1,521 | 🟢 | TypeScript |
| [wxapkg-convertor](https://github.com/ezshine/wxapkg-convertor) | Tool that decompiles WeChat mini program and mini game .wxapkg files | 1,500 | 🔴 | JavaScript |
| [ApkToolPlus](https://github.com/CYRUS-STUDIO/ApkToolPlus) | GUI APK reverse engineering and analysis toolkit | 1,494 | 🟡 | Java |
| [magisk-frida](https://github.com/ViRb3/magisk-frida) | Magisk module running frida-server on boot | 1,480 | 🟢 | Shell |
| [House](https://github.com/nccgroup/house) | Runtime mobile app analysis toolkit with a web GUI, powered by Frida | 1,468 | 🔴 | JavaScript |
| [reFlutter](https://github.com/ptswarm/reFlutter) | Framework that patches the Flutter engine to help reverse engineer Flutter apps | 1,464 | 🗄️ | Python |
| [Grapefruit](https://github.com/ChiChou/grapefruit) | Runtime iOS application analysis tool built on Frida | 1,403 | 🟢 | TypeScript |
| [restore-symbol](https://github.com/tobefuturer/restore-symbol) | Restores the stripped symbol table of iOS app binaries | 1,337 | 🔴 | Objective-C |
| [hermes-dec](https://github.com/P1sec/hermes-dec) | Disassembler and decompiler for React Native Hermes bytecode | 1,230 | 🟢 | Python |
| [Reversense (Dexcalibur)](https://github.com/reversenseorg/dexcalibur) | Platform that automates reverse engineering of Android and embedded apps with Frida | 1,183 | 🟢 | TypeScript |
| [android-unpacker](https://github.com/strazzere/android-unpacker) | Android unpacker presented at DEF CON 22 | 1,182 | 🔴 | C |
| [vdexExtractor](https://github.com/anestisb/vdexExtractor) | Extracts and decompiles Android Dex bytecode from Vdex files | 1,146 | 🟡 | C |
| [ZygiskFrida](https://github.com/lico-n/ZygiskFrida) | Zygisk module that injects Frida gadget into Android apps | 1,098 | 🟡 | C++ |
| [DexKit](https://github.com/LuckyPray/DexKit) | High-performance dex deobfuscation and search library | 1,076 | 🟢 | Kotlin |
| [TTDeDroid](https://github.com/tp7309/TTDeDroid) | One-click decompiler for apk/aar/dex/jar using jadx, dex2jar and enjarify | 947 | 🟢 | Python |
| [ReverseAPK](https://github.com/1N3/ReverseAPK) | Script to quickly analyze and decompile Android APK packages | 881 | 🔴 | Shell |
| [frida-skeleton](https://github.com/Margular/frida-skeleton) | Frida-based Android hooking framework | 880 | 🔴 | Python |
| [garlic](https://github.com/neocanable/garlic) | Fast Java/Android APK and DEX decompiler written in pure C | 880 | 🟢 | C |
| [ReArk](https://github.com/lkimuk/ReArk) | AI-assisted reverse engineering tool for HarmonyOS NEXT (HAP/ABC), Android and iOS packages | 870 | 🟢 | C++ |
| [Wallbreaker](https://github.com/hluwa/Wallbreaker) | Frida-based tool to inspect Java classes and objects in Android app memory | 869 | 🗄️ | Python |
| [Doldrums](https://github.com/rscloura/Doldrums) | Reverse engineering tool that parses Flutter/Dart AOT snapshots | 863 | 🔴 | Python |
| [eDBG](https://github.com/ShinoLeah/eDBG) | eBPF-based lightweight Android debugger with MCP support | 856 | 🟢 | C |
| [decompile-apk](https://github.com/venshine/decompile-apk) | Scripts to decompile APKs | 823 | 🟢 | Shell |
| [app2dylib](https://github.com/tobefuturer/app2dylib) | Tool that converts an iOS app executable into a loadable dylib | 812 | 🔴 | C++ |
| [onekey-decompile-apk](https://github.com/ufologist/onekey-decompile-apk) | One-step APK decompilation tool | 799 | 🔴 | Batchfile |
| [binder-trace](https://github.com/foundryzero/binder-trace) | Intercepts and parses Android Binder messages, like Wireshark for Binder | 772 | 🟡 | Python |
| [JADXecute](https://github.com/LaurieWired/JADXecute) | JADX-gui plugin for dynamic scripting of the decompiler | 751 | 🟡 | Java |
| [Il2CppInspectorRedux](https://github.com/LukeFZ/Il2CppInspectorRedux) | Maintained continuation of Il2CppInspector supporting newer metadata | 744 | 🟢 | C# |
| [Android-Disassembler](https://github.com/yhs0602/Android-Disassembler) | Android app that disassembles .so, PE and ELF files on the device | 721 | 🟢 | Kotlin |
| [Andromeda](https://github.com/secrary/Andromeda) | Interactive reverse engineering tool for Android applications | 714 | 🔴 | C++ |
| [wxappUnpacker](https://github.com/system-cpu/wxappUnpacker) | Node-based WeChat mini program unpacker and decompiler | 704 | 🔴 | JavaScript |
| [apk2gold](https://github.com/lxdvs/apk2gold) | CLI tool that decompiles Android APKs to Java source and resources | 702 | 🟡 | Shell |
| [apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server) | MCP server that drives Apktool so agents can decode, search and edit Android APKs | 699 | 🟢 | Python |
| [XAPKDetector](https://github.com/horsicq/XAPKDetector) | APK/DEX packer and compiler detector | 696 | 🟢 | C++ |
| [ios-mcp](https://github.com/witchan/ios-mcp) | MCP server that lets AI agents read the iPhone screen, tap, type and read logs | 695 | 🟢 | Objective-C |
| [jni_helper](https://github.com/evilpan/jni_helper) | Finds JNI function signatures in APKs and applies them to RE tools | 676 | 🟡 | C++ |
| [MARA Framework](https://github.com/xtiankisutsa/MARA_Framework) | Mobile app reverse engineering and analysis framework combining common tools | 673 | 🔴 | Python |
| [MikRom](https://github.com/dqzg12300/MikRom) | Custom Android ROM with built-in tracing and unpacking for app reverse engineering | 667 | 🟡 | Java |
| [hbctool](https://github.com/bongtrop/hbctool) | Assembler/disassembler for React Native Hermes bytecode | 644 | 🟡 | Python |
| [chomper](https://github.com/sledgeh4w/chomper) | Lightweight framework for emulating crypto algorithms in iOS executables | 635 | 🟢 | Python |
| [AndBug](https://github.com/swdunlop/AndBug) | Scriptable Android debugger for reverse engineering | 600 | 🔴 | Python |
| [abc-decompiler](https://github.com/ohos-decompiler/abc-decompiler) | Decompiler for HarmonyOS ABC bytecode | 590 | 🟡 | Java |
| [android-reverse-engineering-skill](https://github.com/CreditTone/android-reverse-engineering-skill) | Agent skill that decompiles APKs and extracts endpoints, auth headers and signing logic | 564 | 🟢 | JavaScript |
| [abcde](https://github.com/Yricky/abcde) | OpenHarmony reverse engineering toolkit with early decompilation support | 546 | 🟢 | Kotlin |
| [dex-oracle](https://github.com/CalebFenton/dex-oracle) | Pattern-based Dalvik deobfuscator using limited execution | 504 | 🔴 | Ruby |
| [DroidSword](https://github.com/githubwing/DroidSword) | Xposed module that shows current activities and enables disabled views for Android RE | 502 | 🔴 | Kotlin |
| [android-killer](https://github.com/lumirelle/android-killer) | Revived classic Android decompilation tool | 496 | 🟢 | Smali |
| [elf-dump-fix](https://github.com/maiyao1988/elf-dump-fix) | Dumps Android ELF libraries from memory and rebuilds section headers | 488 | 🔴 | C |
| [deoptfuscator](https://github.com/Gyoonus/deoptfuscator) | Deobfuscator for Android applications | 482 | 🔴 | C++ |
| [MagiskHluda](https://github.com/youssefnoser/MagiskHluda) | Magisk module running a less detectable Frida server on boot | 437 | 🟢 | Shell |
| [ARSCLib](https://github.com/REAndroid/ARSCLib) | Android binary resources (ARSC/AXML) read and write library | 421 | 🟢 | Java |
| [theos-jailed](https://github.com/kabiroberai/theos-jailed) | Theos module for developing jailed iOS tweaks | 408 | 🟡 | Shell |
| [Il2CppInterop](https://github.com/BepInEx/Il2CppInterop) | Interop between CoreCLR and IL2CPP at runtime for modding | 404 | 🟢 | C# |
| [phantom-frida](https://github.com/TheQmaks/phantom-frida) | Builds a Frida server from source with anti-detection patches | 403 | 🟢 | Python |
| [ApkToolBoxGUI](https://github.com/AloysHF/ApkToolBoxGUI) | GUI toolbox around apktool and related APK tools | 375 | 🟢 | Java |
| [react-native-decompiler](https://github.com/numandev1/react-native-decompiler) | Decompiles React Native Android/iOS bundles | 372 | 🔴 | TypeScript |
| [JNIAnalyzer](https://github.com/Ayrx/JNIAnalyzer) | Ghidra scripts for analysing Android NDK libraries | 364 | 🔴 | Java |
| [Il2cppSpy](https://github.com/yukiarrr/Il2cppSpy) | Unity IL2CPP disassembler for APK files | 360 | 🔴 | Python |
| [brut.apktool](https://github.com/broo2s/brut.apktool) | Apktool for decoding and rebuilding Android APK files | 358 | 🔴 | Java |
| [darter](https://github.com/mildsunrise/darter) | Dart / Flutter VM snapshot analyzer | 346 | 🟢 | Jupyter Notebook |
| [ReaverAPKTools](https://github.com/HangZhouCat/ReaverAPKTools) | APK reverse engineering toolkit | 341 | 🔴 | HTML |
| [jaysenwxapkg](https://github.com/Jaysen13/jaysenwxapkg) | Auto-unpacks WeChat mini programs and extracts sensitive data and API endpoints | 336 | 🟢 | Java |
| [jnitrace-engine](https://github.com/chame1eon/jnitrace-engine) | Engine used by jnitrace to intercept JNI API calls | 335 | 🔴 | TypeScript |
| [smalisca](https://github.com/dorneanu/smalisca) | Static code analysis for Smali files | 323 | 🗄️ | Python |
| [apkx](https://github.com/muellerberndt/apkx) | One-step APK decompilation with multiple backends | 321 | 🔴 | Python |
| [droidlysis](https://github.com/cryptax/droidlysis) | Property extractor for Android apps | 312 | 🟢 | Python |
| [Pithus Bazaar](https://github.com/Pithus/bazaar) | Android app security and privacy analysis platform | 303 | 🟢 | Python |
| [NinjaDroid](https://github.com/rovellipaolo/NinjaDroid) | Tool to analyze Android APK packages (manifest, dex, certificates) | 287 | 🟢 | Python |
| [WTFJH](https://github.com/Naville/WTFJH) | One-step iOS binary runtime instrumentation | 283 | 🗄️ | Python |
| [wxapkg-unpacker](https://github.com/zgqwork/wxapkg-unpacker) | WeChat mini program decompiler | 282 | 🔴 | JavaScript |
| [dalvikus](https://github.com/loerting/dalvikus) | Android reverse engineering tool and smali editor | 274 | 🟢 | Java |
| [dexsql](https://github.com/LSPosed/dexsql-release) | SQL queries over Android apk and dex files | 265 | 🟢 | Python |
| [appdbg](https://github.com/asmjmp0/appdbg) | Runs Android app methods on a standard JVM for analysis | 262 | 🟡 | Kotlin |
| [axmlprinter](https://github.com/rednaga/axmlprinter) | Library for parsing compiled Android XML manifests | 262 | 🟢 | Java |
| [renef](https://github.com/Byterialab/renef) | Mobile reverse engineering framework | 259 | 🟢 | C++ |
| [apk-utilities](https://github.com/ViRb3/apk-utilities) | Tools and scripts to manipulate Android APKs | 252 | 🟡 | Python |
| [apkfile](https://github.com/CalebFenton/apkfile) | Android APK analysis and feature extraction library | 228 | 🔴 | Java |
| [resymbol](https://github.com/paradiseduo/resymbol) | Restores stripped Mach-O symbols and dumps Objective-C/Swift types | 228 | 🟢 | Swift |
| [android-lkms](https://github.com/strazzere/android-lkms) | Android loadable kernel modules for reversing and debugging | 226 | 🔴 | C |
| [unidbg-server](https://github.com/cxapython/unidbg-server) | Spring Boot service wrapping unidbg to run Android native code | 222 | 🟡 | Java |
| [Dex-Editor-Android](https://github.com/developer-krushna/Dex-Editor-Android) | Android Dalvik bytecode (DEX) editor | 220 | 🟢 | Java |
| [SOMCP](https://github.com/bilieebiliee1-design/SOMCP) | On-device MCP server for reverse engineering Android native .so libraries | 218 | 🟢 | Kotlin |
| [legu_unpacker_2019](https://github.com/quarkslab/legu_unpacker_2019) | Scripts to unpack APKs protected by Tencent Legu | 214 | 🔴 | Python |
| [unidbgweb](https://github.com/zhaoboy9692/unidbgweb) | unidbg as a service for computing request signatures of Chinese apps | 210 | 🗄️ | Java |
| [Il2CppMemoryDumper](https://github.com/MlgmXyysd/Il2CppMemoryDumper) | Dumps IL2CPP executables and metadata from Android process memory | 209 | 🟢 | Shell |
| [arkdecompiler](https://github.com/jd-opensource/arkdecompiler) | HarmonyOS NEXT ArkTS bytecode decompiler | 206 | 🟢 | C++ |
| [ProbeDroid](https://github.com/ZSShen/ProbeDroid) | SDK for building Android app runtime instrumentation tools without source | 204 | 🔴 | C++ |
| [revengi-app](https://github.com/RevEngiSquad/revengi-app) | Toolkit app for smali grammar, DEX repair and Flutter analysis | 203 | 🟢 | Dart |
| [Obfu[DE]scate](https://github.com/user1342/Obfu-DE-Scate) | Android APK deobfuscation tool based on fuzzy comparison between builds | 200 | 🟡 | Python |
| [UnityReverseEngine](https://github.com/IIIImmmyyy/UREngine) | Decompiles Unity APK/IPA builds back into a Unity project | 200 | 🟢 |  |
| [hermes-decomp](https://github.com/SymbioticSec/hermes-decomp) | Decompiler for React Native Hermes bytecode (.hbc) | 198 | 🟢 | Rust |
| [android_analysis](https://github.com/xbyl1234/android_analysis) | Android analysis tools: JNI tracing by native hook and Java object to JSON | 194 | 🟡 | C++ |
| [ida-ios-helper](https://github.com/yoavst/ida-ios-helper) | IDA plugin that eases reversing iOS binaries | 193 | 🟢 | Python |
| [Termux-Apktool](https://github.com/Lexiie/Termux-Apktool) | Decompile and recompile Android apps in Termux without OpenJDK | 190 | 🔴 |  |
| [AndroidReverseEngineering](https://github.com/kenny67/AndroidReverseEngineering) | Android RE toolset with ELF reader, Frida dump scripts, DexDump and SO dumping | 188 | 🔴 | JavaScript |
| [ttpkUnpacker](https://github.com/geek-bigniu/ttpkUnpacker) | Unpacker for Douyin (ByteDance) mini program TTPKG packages | 182 | 🟡 | Python |
| [native-shim](https://github.com/rednaga/native-shim) | Shim for loading native JNI libraries for Android active debugging | 181 | 🔴 | C |
| [flutter-re-demo](https://github.com/Guardsquare/flutter-re-demo) | Experiments on reverse engineering Flutter applications | 178 | 🔴 | Python |
| [iCDump](https://github.com/romainthomas/iCDump) | Modern Objective-C class dump based on LIEF and LLVM | 172 | 🗄️ | C++ |
| [Gwxapkg](https://github.com/25smoking/Gwxapkg) | Go WeChat mini program wxapkg unpacker with auto scanning | 171 | 🟢 | Go |
| [rnidbg](https://github.com/fuqiuluo/rnidbg) | Rust Android ARM64 emulator rewritten from unidbg | 165 | 🟢 | Rust |
| [Katalina](https://github.com/huuck/Katalina) | Emulator that executes Android Dalvik bytecode instruction by instruction | 162 | 🟢 | Python |
| [xpanda](https://github.com/asmjmp0/xpanda) | Decompiler for HarmonyOS Next Panda (.abc) executables | 157 | 🟢 | TypeScript |
| [iOSreExtension](https://github.com/Lakr233/iOSreExtension) | VS Code extension for iOS reverse engineering projects | 155 | 🗄️ | TypeScript |
| [anti_sign](https://github.com/sumous/anti_sign) | Reimplementations of app request signature algorithms | 154 | 🔴 | Python |
| [Dexter](https://github.com/omeraydindev/Dexter) | Advanced DEX editor for Android | 153 | 🟢 | Kotlin |
| [dsdump](https://github.com/paradiseduo/dsdump) | Improved nm plus Objective-C and Swift class-dump | 147 | 🟡 | Python |
| [LeguDecompile](https://github.com/dzx1994/LeguDecompile) | Static unpacker for Tencent Legu-protected .so libraries | 142 | 🔴 | Python |
| [FakerAndroid](https://github.com/nisemoe/FakerAndroid) | Converts an APK into an editable Android project with native hook support | 133 | 🔴 | Java |
| [androidReverse](https://github.com/UltraSina/androidReverse) | On-device Android reverse engineering with radare2 and Java decompilers | 130 | 🟢 |  |
| [Jarida](https://github.com/BitTheByte/Jarida) | Jadx GUI plugin to trace and hook methods with Frida | 130 | 🟢 | Java |
| [flutterdec](https://github.com/caverav/flutterdec) | Decompiles Flutter Android AOT libapp.so into Dart-like pseudocode | 129 | 🟢 | Rust |
| [noia](https://github.com/0x742/noia) | Frida-powered mobile app sandbox file browser | 129 | 🔴 | JavaScript |
| [PulseAPK-Core](https://github.com/deemoun/PulseAPK-Core) | Cross-platform APK decompilation and rebuilding tool | 126 | 🟢 | C# |
| [AndroidKillerPlugin](https://github.com/supperlitt/AndroidKillerPlugin) | Android Killer plugin for APKs it cannot decompile | 125 | 🔴 | C# |
| [r0dump](https://github.com/tiwe0/r0dump) | ART-integrated DEX dumper and repair toolkit for Android 16 | 125 | 🟢 | JavaScript |
| [dexdec](https://github.com/asLody/dexdec) | Fast Android decompiler for humans and AI agents | 122 | 🟢 | Rust |
| [binder-trace](https://github.com/fuqiuluo/binder-trace) | Kernel-based Android Binder transaction observer | 119 | 🟢 | Rust |
| [PulseAPK](https://github.com/deemoun/PulseAPK) | WPF frontend for apktool and signing | 118 | 🟢 | C# |
| [unveilr](https://github.com/0day404/unveilr) | WeChat mini program decompiler | 118 | 🟡 | TypeScript |
| [rust_ASC](https://github.com/MG1937/rust_ASC) | Fast, lightweight Android decompiler for agents and mobile researchers | 115 | 🟢 | Rust |
| [Dexplore](https://github.com/NeonOrbit/Dexplore) | Dex analyzer for finding obfuscated code dynamically | 107 | 🟡 | Java |
| [react-native-decompiler](https://github.com/richardfuca/react-native-decompiler) | Decompile React Native JavaScript bundles | 107 | 🗄️ | TypeScript |
| [reverse_flutter](https://github.com/Neoxs/reverse_flutter) | Tools and guidelines for reverse engineering Flutter apps | 107 | 🟡 | Smali |
| [autojs-unpacker](https://github.com/imlk0/autojs-unpacker) | Reverse engineering tool for Android AutoJS applications | 105 | 🔴 | Python |
| [android-jar-with-hidden-api](https://github.com/JetpackDuba/android-jar-with-hidden-api) | Steps to build an android.jar exposing AOSP hidden APIs | 104 | 🟡 | Shell |
| [mobile-network-traffic](https://github.com/ddxv/mobile-network-traffic) | Guide to sniff Android HTTPS traffic with Waydroid and mitmproxy | 103 | 🟢 | Shell |
| [ghidra-jni](https://github.com/extremecoders-re/ghidra-jni) | jni.h compiled as a Ghidra data type archive | 100 | 🔴 | C |
| [paranoid-deobfuscator](https://github.com/giacomoferretti/paranoid-deobfuscator) | Deobfuscates Android apps protected with the Paranoid string obfuscator | 90 | 🟡 | Python |
| [il2Fusion](https://github.com/PenguinAndy/il2Fusion) | Unity and Cocos2d-x Lua game reverse engineering toolkit for Android | 88 | 🟢 | C |
| [mp-wxapkg-unpacker](https://github.com/halo951/mp-wxapkg-unpacker) | WeChat mini program and mini game wxapkg unpacker with PC encrypted package support | 86 | 🔴 | JavaScript |
| [DECX](https://github.com/jygzyc/decx) | Decompiler plus extensions for Android app analysis | 77 | 🟢 | TypeScript |
| [jadx-type-diagram-plugin](https://github.com/timschneeb/jadx-type-diagram-plugin) | Type diagram plugin for the JADX decompiler | 73 | 🟢 | Java |
| [FLEXLoader](https://github.com/buginux/FLEXLoader) | Loads FLEX to debug arbitrary third-party iOS apps | 70 | 🔴 | Shell |
| [soSaver](https://github.com/TheQmaks/soSaver) | Frida-based tool that extracts native .so libraries from Android apps at runtime | 70 | 🟢 | Python |
| [banjo](https://github.com/ivision-research/banjo) | Android DEX disassembler and Binary Ninja plugin | 68 | 🟡 | Python |
| [jscHookR](https://github.com/Mas0nShi/jscHookR) | Reverse engineering tool for Android Cocos2d-JS apps | 67 | 🗄️ | Python |
| [AndroidRunnableJadx](https://github.com/asmjmp0/AndroidRunnableJadx) | Run Android Java methods inside Jadx without a device | 61 | 🔴 | Java |
| [r2garlic](https://github.com/radareorg/r2garlic) | Fast Android DEX decompiler integrated into radare2 | 44 | 🟢 | C |
| [hasmer](https://github.com/lucasbaizer/hasmer) | Command-line tool for reverse engineering Hermes (React Native) bytecode | 42 | 🗄️ | C# |
| [AOTopsy](https://github.com/BroNils/aotopsy) | Static inspector for Flutter/Dart AOT libapp.so files that recovers classes and call edges | 41 | 🟢 | Go |
| [REMAUI (pixtoapp)](https://github.com/soumikmohianuta/pixtoapp) | Reverse engineers mobile app user interfaces from screenshots into code | 36 | 🔴 | Python |
| [droidsaw](https://github.com/droidsaw/droidsaw) | Unified Android RE CLI for Hermes bytecode, DEX and APK signing, with JSON output and MCP server | 35 | 🟢 | Rust |
| [molt-dex](https://github.com/ReSo7200/molt-dex) | Agent skill for Android reverse engineering and modding with apktool, DexKit and Xposed | 23 | 🟢 | Shell |
| [Jadart](https://github.com/IR0NBYTE/Jadart) | Fast Flutter/Dart AOT decompiler for agents and mobile researchers | 22 | 🟢 | Python |
| [grida](https://github.com/pluggyai/grida) | Graphical reverse engineering UI for Frida on Android | 16 | 🗄️ | TypeScript |
| [BlutterAndroid](https://github.com/AcE77505/BlutterAndroid) | On-device Flutter/Dart AOT reverse engineering for Android, based on Blutter | 15 | 🟢 | C++ |
| [frida-hook-engine](https://github.com/muhammadrizwan87/frida-hook-engine) | Config-driven Frida instrumentation engine for Android | 15 | 🟢 | JavaScript |
| [Frida0xKit](https://github.com/allelloo/Frida0xKit) | Modular toolkit for Android runtime instrumentation with Frida | 14 | 🟢 | JavaScript |
| [VortexDBG](https://github.com/carlosadrianosj/VortexDBG) | Emulates Android native libraries and DEX/Java classes off-device, driven by AI through MCP | 13 | 🟢 | Kotlin |
| [Hermit](https://github.com/xV4L3x/hermit) | Toolkit to inspect, disassemble, decompile and patch React Native Hermes bytecode | 6 | 🟢 | C++ |
| [Talaria](https://github.com/moleium/talaria) | Decompiles React Native Hermes bytecode to pseudocode | 2 | 🟢 | C++ |

## Other

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [FLARE-VM](https://github.com/mandiant/flare-vm) | Installer that sets up a Windows VM for reverse engineering and malware analysis | 9,227 | 🟢 | PowerShell |
| [ESP32 Bus Pirate](https://github.com/geo-tp/ESP32-Bit-Pirate) | ESP32 hardware hacking tool that speaks I2C, SPI, UART, IR, RF and more protocols | 6,301 | 🟢 | C++ |
| [FISSURE](https://github.com/ainfosec/FISSURE) | RF and reverse engineering framework for signal detection, protocol discovery and attacks | 2,076 | 🟢 | Python |
| [ctftool](https://github.com/taviso/ctftool) | Interactive tool to explore the Windows Text Services Framework (CTF) protocol | 1,670 | 🔴 | C |
| [PowerShellArsenal](https://github.com/mattifestation/PowerShellArsenal) | PowerShell module with reverse engineering utilities | 902 | 🔴 | PowerShell |
| [x86-64 Playground](https://github.com/robalb/x86-64-playground) | Online x86-64 assembly editor, emulator and debugger | 768 | 🟢 | C |
| [avscript](https://github.com/taviso/avscript) | Interactive shell for Avast's JavaScript engine extracted via reverse engineering | 674 | 🗄️ | C |
| [samytools](https://github.com/samyk/samytools) | Shell tools for data translation and manipulation during reverse engineering | 621 | 🟢 | Perl |
| [win32-darkmode](https://github.com/ysc3839/win32-darkmode) | Example using the undocumented Windows dark mode API in Win32 apps | 526 | 🔴 | C++ |
| [WaveConverter](https://github.com/paulgclark/waveconverter) | Tool to decode digital RF signals for RF reverse engineering | 440 | 🔴 | Python |
| [Twonkie](https://github.com/dojoe/Twonkie) | USB-PD sniffer/injector/sink based on Google's Twinkie for protocol analysis | 415 | 🟡 | C |
| [PSVita-RE-tools](https://github.com/TeamFAPS/PSVita-RE-tools) | Bundle of RE tools for analyzing and modding the PS Vita OS | 396 | 🔴 | C |
| [Musa.Veil](https://github.com/MiroKaku/Musa.Veil) | Collection of undocumented Windows API declarations | 371 | 🟢 | C |
| [AutoProber](https://github.com/GainSec/AutoProber) | Flying-probe automation stack for agent-driven hardware target discovery and pin probing | 336 | 🟢 | Python |
| [etw-providers-docs](https://github.com/repnz/etw-providers-docs) | Documentation of undocumented Windows ETW providers | 307 | 🔴 | C |
| [VM-Packages](https://github.com/mandiant/VM-Packages) | Chocolatey packages for the FLARE-VM and Commando VM analysis environments | 248 | 🟢 | PowerShell |
| [cobol-rekt](https://github.com/avishek-sen-gupta/cobol-rekt) | Toolkit for analysing and reverse engineering legacy COBOL code (flowcharts, CFGs) | 168 | 🟢 | COBOL |
| [re_sysdiag](https://github.com/stonedreamforest/re_sysdiag) | Reverse-engineered source of the Huorong security sysdiag driver | 159 | 🗄️ | C |
| [Windows-Insight](https://github.com/ernw/Windows-Insight) | Research on the inner workings of Windows components | 153 | 🔴 | JavaScript |
| [rea (mytechnotalent)](https://github.com/mytechnotalent/rea) | Portable reverse engineering framework that runs without installation | 98 | 🟢 | Rust |
| [WarbirdExamples](https://github.com/DownWithUp/WarbirdExamples) | Examples of using Microsoft's undocumented Warbird technology | 97 | 🔴 | C |
| [WslReverse](https://github.com/Biswa96/WslReverse) | Experiments with hidden WSL COM interfaces and LxBus IPC | 88 | 🔴 | C |
| [wesp-research](https://github.com/marcosd4h/wesp-research) | Reverse engineering research and tools for Windows Event Streaming Protocols | 81 | 🟢 | C++ |
| [windows-native](https://github.com/NiiightmareXD/windows-native) | Rust bindings for undocumented Windows native (ntdll) APIs | 47 | 🟡 | Rust |
| [dfuexplorer](https://github.com/travisgoodspeed/dfuexplorer) | USB DFU client for reverse engineers | 38 | 🟢 | C++ |
| [FalsoJNI](https://github.com/v-atamanenko/FalsoJNI) | Fake JVM/JNI interface in C for porting JNI-heavy Android games to PS Vita | 36 | 🟢 | C |

## Traffic Interception

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [mitmproxy](https://github.com/mitmproxy/mitmproxy) | Interactive TLS-capable intercepting HTTP proxy | 46,511 | 🟢 | Python |
| [mitmproxy2swagger](https://github.com/alufers/mitmproxy2swagger) | Reverse-engineers REST APIs into OpenAPI specs from captured mitmproxy/HAR traffic | 9,683 | 🟢 | HTML |
| [spy-debugger](https://github.com/wuchangming/spy-debugger) | Remote WebView debugger and HTTPS capture proxy for WeChat and mobile pages | 7,620 | 🟡 | JavaScript |
| [apk-mitm](https://github.com/niklashigi/apk-mitm) | CLI that prepares Android APKs for HTTPS inspection by removing pinning | 5,131 | 🟡 | TypeScript |
| [AndroidHttpCapture](https://github.com/JZ-Darkal/AndroidHttpCapture) | Android on-device HTTP packet capture and network diagnosis app | 4,614 | 🟢 | Java |
| [Anything Analyzer](https://github.com/Mouseww/anything-analyzer) | Protocol analysis workstation: browser capture, MITM proxy, AI analysis and MCP server | 3,814 | 🟢 | TypeScript |
| [ssl-kill-switch2](https://github.com/nabla-c0d3/ssl-kill-switch2) | Disables SSL certificate validation and pinning in iOS and macOS apps | 3,324 | 🔴 | Objective-C |
| [reverse-api-engineer](https://github.com/kalil0321/reverse-api-engineer) | Agent that captures website traffic and turns it into API clients | 2,254 | 🟢 | Python |
| [Knot](https://github.com/Lojii/Knot) | iOS MITM-based HTTPS packet capture app | 1,801 | 🟢 | Swift |
| [go-mitmproxy](https://github.com/lqqyt2423/go-mitmproxy) | mitmproxy-style HTTPS interception proxy implemented in Go | 1,581 | 🟢 | Go |
| [USBPcap](https://github.com/desowin/usbpcap) | USB packet capture for Windows, used for driver protocol analysis | 1,153 | 🟡 | C |
| [Proxelar](https://github.com/emanuele-em/proxelar) | MitM proxy in Rust with TUI, terminal and web interfaces | 1,100 | 🟢 | Rust |
| [android-unpinner](https://github.com/mitmproxy/android-unpinner) | Removes certificate pinning from Android APKs | 1,055 | 🟡 | Python |
| [Facedancer](https://github.com/greatscottgadgets/facedancer) | Python USB device emulation and proxy framework for reverse engineering USB devices | 1,040 | 🟢 | Python |
| [Netzob](https://github.com/netzob/netzob) | Protocol reverse engineering, modeling and fuzzing tool | 840 | 🟡 | Python |
| [tokentap (Sherlock)](https://github.com/jmuncor/tokentap) | MitM proxy that intercepts LLM tool API traffic to show what coding agents send | 811 | 🟢 | Python |
| [js-cookie-monitor-debugger-hook](https://github.com/JSREI/js-cookie-monitor-debugger-hook) | Userscript to monitor and breakpoint JavaScript cookie changes for web RE | 782 | 🟢 | TypeScript |
| [Blackbox Protobuf](https://github.com/nccgroup/blackboxprotobuf) | Decodes and re-encodes Protocol Buffers messages without the .proto definitions | 743 | 🟢 | Python |
| [HTTP Toolkit](https://github.com/httptoolkit/httptoolkit-desktop) | Desktop app for intercepting and debugging HTTP(S) traffic | 739 | 🟢 | TypeScript |
| [USB Sniffer Lite](https://github.com/ataradov/usb-sniffer-lite) | Simple USB sniffer based on the Raspberry Pi RP2040 | 704 | 🟡 | C |
| [Protobuf Decoder](https://github.com/pawitp/protobuf-decoder) | Web app that decodes Protobuf messages without a schema | 678 | 🟢 | JavaScript |
| [esp32_bluetooth_classic_sniffer](https://github.com/Matheus-Garbelini/esp32_bluetooth_classic_sniffer) | Active Bluetooth BR/EDR sniffer and injector on ESP32 | 615 | 🔴 | C |
| [JS-Forward](https://github.com/G-Security-Team/JS-Forward) | Tool for testing web apps whose front end encrypts request parameters | 579 | 🔴 | Python |
| [httptoolkit-server](https://github.com/httptoolkit/httptoolkit-server) | Backend of HTTP Toolkit HTTP(S) interception and debugging tool | 569 | 🟢 | JavaScript |
| [USBProxy-legacy](https://github.com/usb-tools/USBProxy-legacy) | Proxy for USB devices using libUSB and gadgetFS to sniff and modify traffic | 471 | 🔴 | C++ |
| [SunnyNetTools](https://github.com/qtgolang/SunnyNetTools) | Packet capture tool built on the SunnyNet network middleware | 415 | 🟢 | JavaScript |
| [frida-flutterproxy](https://github.com/hackcatml/frida-flutterproxy) | Frida script to proxy Flutter app traffic through Burp | 362 | 🟡 | JavaScript |
| [Wireshark MCP](https://github.com/bx33661/Wireshark-MCP) | MCP server that wraps tshark so agents can query packet captures | 361 | 🟢 | Python |
| [usbrply](https://github.com/JohnDMcMaster/usbrply) | Converts USB pcaps into Python/C replay scripts for driver reverse engineering | 340 | 🟡 | Python |
| [frida-intercept-encrypted-api](https://github.com/yazgx97/frida-intercept-encrypted-api) | Frida tool to intercept encrypted APIs in iOS and Android apps | 334 | 🟡 | JavaScript |
| [Charles MCP](https://github.com/heizaheiza/Charles-mcp) | Charles Proxy MCP server for AI agents with live capture and traffic analysis | 332 | 🟢 | Python |
| [tcpproxy](https://github.com/ickerwx/tcpproxy) | Intercepting TCP proxy that modifies raw TCP streams with modules | 315 | 🟡 | Python |
| [Packetry](https://github.com/greatscottgadgets/packetry) | USB 2.0 protocol analyzer for Cynthion captures and PCAP files | 296 | 🟢 | Rust |
| [shermie-proxy](https://github.com/kxg3030/shermie-proxy) | Go packet capture proxy for HTTP, HTTPS, WebSocket and TCP | 268 | 🔴 | Go |
| [android_proxy_mcp](https://github.com/zhizhuodemao/android_proxy_mcp) | MCP-based Android packet capture service for AI assistants | 243 | 🟢 | Python |
| [Deluder](https://github.com/Warxim/deluder) | Intercepts traffic of proxy-unaware applications by hooking TLS libraries | 217 | 🟢 | Python |
| [xepor](https://github.com/xepor/xepor) | Flask-style web routing framework on mitmproxy for reverse engineers | 215 | 🟢 | Python |
| [bluebox (web-hacker)](https://github.com/VectorlyApp/bluebox) | Reverse engineers web apps' undocumented APIs from browser traffic | 203 | 🟢 | Python |
| [mars](https://github.com/ouqiang/mars) | HTTP(S) proxy for packet capture and debugging | 180 | 🔴 | Go |
| [AutomatiQ](https://github.com/StoneSteel27/AutomatiQ) | Reverse-engineering agent that turns web app traffic into APIs | 178 | 🟢 | Python |
| [mitmproxy-mcp](https://github.com/snapspecter/mitmproxy-mcp) | MCP server wrapping mitmproxy for AI clients | 134 | 🟢 | Python |
| [FlutterTap](https://github.com/script-or-script/FlutterTap) | Zygisk module redirecting Flutter app traffic to a proxy | 129 | 🟢 | C++ |
| [spectral](https://github.com/spectral-mcp/spectral) | Captures app traffic and infers the underlying API | 121 | 🟢 | Python |
| [Android-Request-Inspector-WebView](https://github.com/acsbendi/Android-Request-Inspector-WebView) | Inspect and intercept full HTTP requests from Android WebViews | 117 | 🟢 | Kotlin |
| [usbsnoop](https://github.com/yeet-src/usbsnoop) | Live system-wide USB transfer sniffer in eBPF with inline protocol decoding | 88 | 🟢 | JavaScript |
| [Android-BLE-Monitor](https://github.com/mx0c/Android-BLE-Monitor) | BLE reverse engineering tool for Android | 80 | 🔴 | C++ |
| [BLE-Analyzer-pro-linux-capture](https://github.com/xecaz/BLE-Analyzer-pro-linux-capture) | Linux capture tool for the reverse-engineered BLE Analyzer Pro USB sniffer | 79 | 🟢 | C |
| [NetPlier](https://github.com/yapengye/NetPlier) | Probabilistic network protocol reverse engineering from message traces | 76 | 🟡 | Python |
| [mitmcloak](https://github.com/sardanioss/mitmcloak) | mitmproxy addon mirroring real browser TLS/H2/H3 fingerprints upstream | 69 | 🟢 | Python |
| [http-breakout-proxy](https://github.com/jbsouthe/http-breakout-proxy) | HTTP proxy for reverse engineering protocol communication | 61 | 🟢 | Go |
| [Protocol Informatics](https://github.com/bitpeach/Protocol-Informatics) | Automatic network protocol reverse engineering from captured traffic | 53 | 🔴 |  |
| [rever-browser](https://github.com/greekr4/rever-browser) | AI-agent browser for web API reverse engineering | 49 | 🟢 | TypeScript |
| [impersonate-proxy](https://github.com/ytkoka/impersonate-proxy) | Local MitM proxy to control TLS (JA3/JA4) and HTTP/2 fingerprints | 46 | 🟢 | Go |
| [api-reverse-engineer](https://github.com/ctala/api-reverse-engineer) | Chrome extension capturing fetch/XHR calls to reverse engineer site APIs | 36 | 🟢 | JavaScript |
| [Browser Reverse Engineering Toolkit](https://github.com/Dvurechensky/Browser.Reverse.Engineering.Toolkit) | Captures browser-session evidence and crawls sites to document web app architecture | 32 | 🟢 | JavaScript |
| [fritm](https://github.com/louisabraham/fritm) | Cross-platform network reverse engineering framework hooking processes with Frida | 26 | 🔴 | Python |
| [ble-learning](https://github.com/apferscher/ble-learning) | Automata-learning framework that fingerprints Bluetooth Low Energy devices (research code) | 21 | 🟡 | C |
| [state-inspector](https://github.com/ChrisMcMStone/state-inspector) | Grey-box protocol state machine learning from CCS research | 14 | 🔴 | C |
| [Claude Intercept](https://github.com/whaesemeyer/claude-intercept) | Local MITM proxy and dashboard that captures and decodes HTTP/S traffic from your own computer | 10 | 🟢 | JavaScript |
| [SniffUSB / usbsnoop](https://sourceforge.net/projects/usbsnoop/) | Windows USB traffic sniffer used to reverse engineer USB device protocols for Linux drivers |  | ⚪ |  |
| [usbsniff](https://codeberg.org/lubko666/usbsniff) | USB reverse engineering utilities: capture, replay and analysis |  | ⚪ |  |
| [Wireshark](https://gitlab.com/wireshark/wireshark) | Network protocol analyzer with dissectors for many reverse-engineered protocols |  | ⚪ |  |
