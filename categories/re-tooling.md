# RE Tooling

[← All categories](../README.md) · 254 projects

- [AI-assisted RE](#ai-assisted-re) (21)
- [Binary & Format Analysis](#binary--format-analysis) (13)
- [Decompilation Project Tooling](#decompilation-project-tooling) (35)
- [Disassemblers & Decompilers](#disassemblers--decompilers) (99)
- [Dynamic Instrumentation](#dynamic-instrumentation) (17)
- [Mobile RE](#mobile-re) (34)
- [Other](#other) (14)
- [Traffic Interception](#traffic-interception) (21)

## AI-assisted RE

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| ida-pro-mcp | MCP bridge between IDA Pro and LLM clients | 12,654 | <https://github.com/mrexodia/ida-pro-mcp> |
| GhidraMCP | MCP server exposing Ghidra to LLM clients | 11,058 | <https://github.com/LaurieWired/GhidraMCP> |
| Gepetto | IDA Pro plugin using LLMs to explain and rename decompiled functions | 3,477 | <https://github.com/JusticeRage/Gepetto> |
| reagent | Reconstruct and validate C/C++ code from compiled programs with AI | 2,060 | <https://github.com/Dryxio/reagent> |
| open-reverselab | AI reverse-engineering agent platform and MCP server for Ghidra, Frida, x64dbg, Rizin | 1,250 | <https://github.com/LING71671/open-reverselab> |
| jadx-mcp-server | MCP server for the JADX-AI plugin for Android RE | 794 | <https://github.com/zinja-coder/jadx-mcp-server> |
| unbrowse | Reverse engineers websites' internal APIs so agents can call them directly | 784 | <https://github.com/unbrowse-ai/unbrowse> |
| GhidrAssistMCP | MCP server extension for Ghidra | 769 | <https://github.com/symgraph/GhidrAssistMCP> |
| GhidrAssist | LLM assistant plugin for Ghidra | 756 | <https://github.com/symgraph/GhidrAssist> |
| DAILA | Decompiler-agnostic AI assistant plugin for IDA, Ghidra, Binja and angr | 710 | <https://github.com/mahaloz/DAILA> |
| r2ai | LLM integration for radare2 | 487 | <https://github.com/radareorg/r2ai> |
| binary_ninja_mcp | Binary Ninja plugin with MCP server for LLM clients | 450 | <https://github.com/fosdickio/binary_ninja_mcp> |
| pyghidra-mcp | Command-line Python Ghidra MCP server | 441 | <https://github.com/clearbluejar/pyghidra-mcp> |
| idasql | SQL interface over IDA Pro databases via live virtual tables for agent-driven RE | 422 | <https://github.com/allthingsida/idasql> |
| binary-ninja-headless-mcp | Headless Binary Ninja MCP server for AI agents | 256 | <https://github.com/mrphrazer/binary-ninja-headless-mcp> |
| ghidra-headless-mcp | Headless Ghidra MCP server for AI agents | 190 | <https://github.com/mrphrazer/ghidra-headless-mcp> |
| grokathon (Nova) | Grok Build harness that reverse engineers old binaries; Grokathon winner | 37 | <https://github.com/theodorechapman/grokathon> |
| deobfuscate-mcp-server | MCP server helping LLMs reverse-engineer minified JavaScript | 18 | <https://github.com/MadeByTokens/deobfuscate-mcp-server> |
| 2api-skill | Agent skill to reverse-engineer any webchat into an OpenAI/Anthropic API | 14 | <https://github.com/69gg/2api-skill> |
| decomp-goal-harness | Harness for coding agents working on matching decompilation goals | 8 | <https://github.com/Muhtasham/decomp-goal-harness> |
| DAITK | AI-assisted GameCube decompilation pipeline with objdiff verification | 0 | <https://github.com/Grien25/DAITK> |

## Binary & Format Analysis

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| Detect-It-Easy | Program for determining file types, compilers and packers | 11,671 | <https://github.com/horsicq/Detect-It-Easy> |
| LIEF | Library to parse and modify ELF, PE and Mach-O binaries | 5,584 | <https://github.com/lief-project/LIEF> |
| PE-bear | Multiplatform PE file reversing tool | 3,836 | <https://github.com/hasherezade/pe-bear> |
| rehex | Reverse-engineers' hex editor with structure annotation | 2,481 | <https://github.com/solemnwarning/rehex> |
| pefile | Python module to read and work with PE files | 2,075 | <https://github.com/erocarrera/pefile> |
| XPEViewer | PE file viewer and editor | 1,240 | <https://github.com/horsicq/XPEViewer> |
| Veles *(archived)* | Binary data visualization and analysis tool | 1,238 | <https://github.com/codilime/veles> |
| sasquatch | Patched unsquashfs that handles vendor-modified SquashFS images | 567 | <https://github.com/devttys0/sasquatch> |
| ktool | pip install k2l \| Mach-O + Obj-C analysis TUI / CLI kit and library. Zero compiled deps, runs anywhere with a python... | 525 | <https://github.com/0cyn/ktool> |
| pdb | Rust parser for Microsoft PDB (Program Database) debug information | 467 | <https://github.com/getsentry/pdb> |
| Kaitai Struct Web IDE | Browser IDE for writing and testing Kaitai Struct format specs | 318 | <https://github.com/kaitai-io/kaitai_struct_webide> |
| resource_dasm | Classic Mac OS resource fork decoder and 68K/PPC disassembler with format-specific RE tools | 158 | <https://github.com/fuzziqersoftware/resource_dasm> |
| mootool | MachO's Other Tooling | 12 | <https://github.com/hack-different/mootool> |

## Decompilation Project Tooling

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| Diaphora | Program diffing plugin for IDA, Ghidra-compatible exports | 4,422 | <https://github.com/joxeankoret/diaphora> |
| PS2Recomp | Playstation 2 Static Recompiler & Runtime Tool to make native PC ports | 3,370 | <https://github.com/ran-j/PS2Recomp> |
| BinDiff | Binary diffing tool for comparing disassembled code | 3,204 | <https://github.com/google/bindiff> |
| ghidriff | Ghidra-based command-line binary diffing engine | 812 | <https://github.com/clearbluejar/ghidriff> |
| BinSync | Reverse-engineering collaboration and sync across decompilers | 750 | <https://github.com/binsync/binsync> |
| m2c | MIPS/PowerPC/ARM assembly to C decompiler aimed at matching output | 655 | <https://github.com/matt-kempster/m2c> |
| objdiff | Local object-file diffing tool for matching decompilation projects | 574 | <https://github.com/encounter/objdiff> |
| RecompOne | PSX Static Recompiler and Runtime, Not Affiliated With Sony or PlayStation | 557 | <https://github.com/BlackLabelHQ/RecompOne> |
| XenosRecomp | A tool for converting Xbox 360 shaders to HLSL. | 499 | <https://github.com/hedge-dev/XenosRecomp> |
| splat | Binary splitting tool for N64, PS1, PS2 and PSP decompilation projects | 366 | <https://github.com/ethteck/splat> |
| decomp-toolkit | GameCube/Wii decompilation toolkit: splits binaries and generates build configs | 306 | <https://github.com/encounter/decomp-toolkit> |
| decomp-permuter | Randomly permutes C code to find a match with target assembly | 230 | <https://github.com/simonlindholm/decomp-permuter> |
| rabbitizer | MIPS instruction decoder library used by decomp tooling | 181 | <https://github.com/Decompollaborate/rabbitizer> |
| wibo | Minimal Windows binary loader to run old Win32 compilers on Linux | 179 | <https://github.com/decompals/wibo> |
| asm-differ | Assembly differ for matching decompilation work | 175 | <https://github.com/simonlindholm/asm-differ> |
| llvm8 | Statically recompiling CHIP8 to Windows and macOS using LLVM | 99 | <https://github.com/ioncodes/llvm8> |
| spimdisasm | MIPS disassembler that produces matching-ready assembly for decomp projects | 83 | <https://github.com/Decompollaborate/spimdisasm> |
| Mizuchi | Pipeline that combines m2c, permuter, objdiff and AI to auto-decompile functions | 76 | <https://github.com/macabeus/mizuchi> |
| SwitchRecomp | Preservation-focused static recompilation research for Nintendo Switch. | 65 | <https://github.com/bgyss/SwitchRecomp> |
| NESgen *(archived)* | Static Recompilation of NES ROMs to C code | 53 | <https://github.com/Xenomega/NESgen> |
| Kappa | VS Code extension assisting matching decompilation work | 51 | <https://github.com/macabeus/kappa> |
| 3dsrecomp | Static recompiler for Nintendo 3DS games, from ARM to C | 33 | <https://github.com/fearkov/3dsrecomp> |
| mapfile_parser | Parses linker map files for decomp progress tracking | 30 | <https://github.com/Decompollaborate/mapfile_parser> |
| NWiiRecomp | Static recompilation and runtime toolkit for Nintendo GameCube and Wii to make native PC ports (and not only) | 28 | <https://github.com/BlackLineInteractive/NWiiRecomp> |
| n64-decomp-workbench | Relocation-aware diffs to find late-stage MIPS decompilation mismatches | 20 | <https://github.com/akratch/n64-decomp-workbench> |
| RecompCore | A static-recompilation CPU core for Dolphin — run GameCube games as native code, with transparent interpreter fallback | 20 | <https://github.com/aharonahdoot/RecompCore> |
| nWiiURecomp | Static recompilation and runtime toolkit for Nintendo Wii U (based on NWiiRecomp) to make native PC ports (and not only) | 14 | <https://github.com/BlackLineInteractive/nWiiURecomp> |
| model3recomp | Sega Model 3 hardware runtime and PowerPC 603e static recompiler. Link a recompiled Model 3 game against native C har... | 13 | <https://github.com/sp00nznet/model3recomp> |
| PS4Recomp | Experimental macOS Apple Silicon first recompiler of PS4 programs | 11 | <https://github.com/wie-project/PS4Recomp> |
| GXRuntime | Game-agnostic GameCube static-recompilation runtime: CPU semantics, devices, GX renderer (work in progress) | 8 | <https://github.com/aharonahdoot/GXRuntime> |
| model2recomp | A Sega Model 2 hardware runtime for statically recompiled games: geometry engine, rasterizer, tilemaps and TGP coproc... | 8 | <https://github.com/sp00nznet/model2recomp> |
| nakagawa-recomp | Experimental PSP static recompiler and native runtime using user-supplied lawful inputs. | 8 | <https://github.com/Jstar269/nakagawa-recomp> |
| psprism | A tool for recompiling PlayStation Portable games to native executables. | 7 | <https://github.com/anthonyhfm/psprism> |
| xenon-jumptables | Recover Xbox 360 / Xenon PowerPC jump tables for static recompilation (XenonRecomp / ReXGlue) — resolves the switch i... | 6 | <https://github.com/xdzleo/xenon-jumptables> |
| shader-compiler-rs | A tool to recompile binary maxwell shaders (found on nintendo switch) to glsl | 5 | <https://github.com/DCNick3/shader-compiler-rs> |

## Disassemblers & Decompilers

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| Ghidra | NSA's software reverse engineering framework with decompiler | 83,381 | <https://github.com/NationalSecurityAgency/ghidra> |
| x64dbg | Open source user-mode debugger for Windows | 49,784 | <https://github.com/x64dbg/x64dbg> |
| dnSpy *(archived)* | .NET debugger, decompiler and assembly editor | 29,672 | <https://github.com/dnSpy/dnSpy> |
| ILSpy | Cross-platform .NET decompiler | 26,546 | <https://github.com/icsharpcode/ILSpy> |
| radare2 | UNIX-like reverse engineering framework and toolset | 24,995 | <https://github.com/radareorg/radare2> |
| Cutter | Free RE platform/GUI powered by rizin | 19,980 | <https://github.com/rizinorg/cutter> |
| JD-GUI | Standalone GUI Java decompiler | 15,210 | <https://github.com/java-decompiler/jd-gui> |
| dnSpyEx | Revival of dnSpy .NET debugger and assembly editor | 11,233 | <https://github.com/dnSpyEx/dnSpy> |
| angr | Python binary analysis framework with symbolic execution and decompiler | 9,141 | <https://github.com/angr/angr> |
| Capstone | Multi-architecture disassembly framework | 9,078 | <https://github.com/capstone-engine/capstone> |
| RetDec | Retargetable machine-code decompiler based on LLVM | 8,644 | <https://github.com/avast/retdec> |
| Recaf | Java bytecode editor and decompiler front end | 7,421 | <https://github.com/Col-E/Recaf> |
| LLM4Decompile | LLMs that decompile binary code to C | 7,111 | <https://github.com/albertan017/LLM4Decompile> |
| JPEXS FFDec | Open-source Flash SWF decompiler and editor | 5,927 | <https://github.com/jindrapetrik/jpexs-decompiler> |
| GhidraMCP (bethington) | Ghidra MCP server exposing 200+ tools for AI-assisted reverse engineering | 5,442 | <https://github.com/bethington/ghidra-mcp> |
| pycdc | C++ Python bytecode disassembler and decompiler | 4,645 | <https://github.com/zrax/pycdc> |
| Fernflower | Analytical Java bytecode decompiler used in IntelliJ IDEA | 4,420 | <https://github.com/JetBrains/fernflower> |
| uncompyle6 | Cross-version Python bytecode decompiler | 4,331 | <https://github.com/rocky/python-uncompyle6> |
| Miasm | Python reverse engineering framework: disassembly, IR, symbolic execution, emulation | 3,988 | <https://github.com/cea-sec/miasm> |
| rizin | UNIX-like reverse engineering framework (radare2 fork) | 3,951 | <https://github.com/rizinorg/rizin> |
| Plasma | Interactive disassembler for x86/ARM/MIPS with pseudo-C output | 3,070 | <https://github.com/plasma-disassembler/plasma> |
| Mono.Cecil | Library to inspect and modify .NET CIL assemblies | 3,005 | <https://github.com/jbevain/cecil> |
| CFR | Java decompiler supporting modern Java features | 2,715 | <https://github.com/leibnitz27/cfr> |
| Decompiler Explorer | Dogbolt: compare output of many decompilers in the browser | 2,704 | <https://github.com/decompiler-explorer/decompiler-explorer> |
| Keystone | Multi-architecture assembler framework | 2,644 | <https://github.com/keystone-engine/keystone> |
| Reko | General-purpose binary decompiler supporting many CPU architectures | 2,612 | <https://github.com/uxmal/reko> |
| dnlib | Library to read and write .NET assemblies and modules | 2,489 | <https://github.com/0xd4d/dnlib> |
| Vineflower | Modern Java decompiler (Fernflower fork, formerly Quiltflower) | 2,395 | <https://github.com/Vineflower/vineflower> |
| BAP | Binary Analysis Platform for lifting and analysing binaries | 2,262 | <https://github.com/BinaryAnalysisPlatform/bap> |
| Snowman *(archived)* | Native code to C/C++ decompiler for x86, x86-64 and ARM | 2,243 | <https://github.com/yegord/snowman> |
| remill | Library lifting machine code to LLVM bitcode | 1,858 | <https://github.com/lifting-bits/remill> |
| REDasm | Interactive multi-architecture disassembler | 1,821 | <https://github.com/redasm-dev/redasm> |
| AvaloniaILSpy *(archived)* | Cross-platform Avalonia GUI for the ILSpy .NET decompiler | 1,810 | <https://github.com/icsharpcode/AvaloniaILSpy> |
| rev.ng | Binary analysis framework and decompiler based on LLVM and QEMU | 1,749 | <https://github.com/revng/revng> |
| iaito | Official Qt GUI for radare2 | 1,719 | <https://github.com/radareorg/iaito> |
| BARF | Binary Analysis and Reverse engineering Framework for x86/ARM | 1,455 | <https://github.com/programa-stic/barf-project> |
| Virtuailor | IDAPython tool reconstructing C++ virtual tables in IDA Pro | 1,403 | <https://github.com/0xgalz/Virtuailor> |
| binaryninja-api | Public API, examples and docs for the Binary Ninja reverse-engineering platform | 1,324 | <https://github.com/Vector35/binaryninja-api> |
| decompile3 | Python 3.7+ bytecode decompiler | 1,276 | <https://github.com/rocky/python-decompile3> |
| Procyon | Java metaprogramming suite and decompiler | 1,222 | <https://github.com/mstrobel/procyon> |
| angr-management | GUI for the angr binary analysis framework | 1,189 | <https://github.com/angr/angr-management> |
| IDR | Interactive Delphi Reconstructor: decompiler for Delphi executables | 1,166 | <https://github.com/crypto2011/IDR> |
| ViperMonkey | VBA parser and emulation engine for analysing Office macros | 1,129 | <https://github.com/decalage2/ViperMonkey> |
| rz-ghidra | Ghidra decompiler and Sleigh disassembler integration for Rizin and Cutter | 990 | <https://github.com/rizinorg/rz-ghidra> |
| Porosity | Decompiler and security analysis tool for Ethereum smart contracts | 934 | <https://github.com/msuiche/porosity> |
| IDAssist | AI-augmented reverse engineering plugin for IDA Pro | 871 | <https://github.com/symgraph/IDAssist> |
| BiTE | Cross-platform executable viewer and disassembler with strong Rust support | 826 | <https://github.com/WINSDK/bite> |
| decomp2dbg | Syncs decompiler symbols and types into GDB | 824 | <https://github.com/mahaloz/decomp2dbg> |
| GhIDA | GhIDA | 820 | <https://github.com/Cisco-Talos/GhIDA> |
| retdec-idaplugin | RetDec plugin for IDA | 798 | <https://github.com/avast/retdec-idaplugin> |
| Ghidrathon *(archived)* | Python 3 scripting support for Ghidra | 790 | <https://github.com/mandiant/Ghidrathon> |
| fcd | LLVM-based optimizing native-code decompiler | 773 | <https://github.com/fay59/fcd> |
| rzweb | Browser-based reverse engineering platform built on Rizin compiled to WebAssembly | 763 | <https://github.com/IndAlok/rzweb> |
| Rellic | Produces goto-free C output from LLVM bitcode for decompilation | 619 | <https://github.com/lifting-bits/rellic> |
| r2dec-js | Pseudo-C decompiler plugin for radare2 and rizin | 610 | <https://github.com/wargio/r2dec-js> |
| XLMMacroDeobfuscator | Extracts and emulates Excel 4.0 (XLM) macros from XLS, XLSM and XLSB files | 590 | <https://github.com/DissectMalware/XLMMacroDeobfuscator> |
| Kuna | Agent-first decompiler written in Rust | 583 | <https://github.com/Noelo-Lab/kuna> |
| r2ghidra | Native Ghidra decompiler integration for radare2 | 559 | <https://github.com/radareorg/r2ghidra> |
| decomp | Components of a decompilation pipeline (LLVM IR to Go) | 492 | <https://github.com/decomp/decomp> |
| pcodedmp | Disassembler for undocumented VBA p-code in Office macro documents | 492 | <https://github.com/bontchev/pcodedmp> |
| Unreal-Library | Decompiler and parser for Unreal Engine package files | 488 | <https://github.com/EliotVU/Unreal-Library> |
| mdec *(archived)* | Compare output of multiple decompilers side by side | 460 | <https://github.com/mborgerson/mdec> |
| RABCDAsm | ActionScript 3 bytecode (ABC) assembler and disassembler | 457 | <https://github.com/CyberShadow/RABCDAsm> |
| Boomerang | General open-source machine-code decompiler | 406 | <https://github.com/BoomerangDecompiler/boomerang> |
| radeco | radare2-based decompiler and symbolic executor in Rust | 399 | <https://github.com/radareorg/radeco> |
| aiDAPal | IDA Pro plugin with fine-tuned local LLM for Hex-Rays pseudocode | 394 | <https://github.com/atredispartners/aidapal> |
| ghidra_kernelcache | a Ghidra framework for iOS kernelcache reverse engineering | 373 | <https://github.com/0x36/ghidra_kernelcache> |
| Sekiryu (GhidrAI) *(archived)* | Ghidra headless toolkit with automatic decompilation and LLM analysis | 360 | <https://github.com/20urc3/Sekiryu> |
| GhydraMCP | Ghidra plugin with REST API and MCP bridge for agentic multi-binary reverse engineering | 303 | <https://github.com/starsong-consulting/GhydraMCP> |
| ProjectorRays | Decompiler for Macromedia/Adobe Director and Shockwave Lingo | 299 | <https://github.com/ProjectorRays/ProjectorRays> |
| hexagon | IDA processor module for the hexagon (QDSP6) processor | 241 | <https://github.com/gsmk/hexagon> |
| FunctionInliner | An IDA plugin that eases reversing of binaries that have been code-size-optimized with function outlining | 230 | <https://github.com/cellebrite-labs/FunctionInliner> |
| holodec | Decompiler for x86 and x86-64 ELF binaries | 220 | <https://github.com/Cararasu/holodec> |
| ai-reverse-engineering | AI-assisted binary reverse engineering with Ghidra and LLMs | 199 | <https://github.com/biniamf/ai-reverse-engineering> |
| BTD DNN decompiler | Decompiles x86 deep neural network executables back to model structure and weights | 199 | <https://github.com/monkbai/DNN-decompiler> |
| Dhrake | Ghidra scripts for reverse engineering Delphi binaries | 195 | <https://github.com/huettenhain/dhrake> |
| DelphiHelper | IDA Pro plugin for analysing Delphi binaries | 173 | <https://github.com/eset/DelphiHelper> |
| ida-iboot-loader | IDA loader for Apple's 64 bits iBoot, SecureROM and AVPBooter | 172 | <https://github.com/matteyeux/ida-iboot-loader> |
| PacXplorer | IDA plugin to find code cross references to virtual functions using PAC codes | 159 | <https://github.com/cellebrite-labs/PacXplorer> |
| Semi-VB-Decompiler | Partial decompiler for Visual Basic 5/6 executables and their file structure | 155 | <https://github.com/VBGAMER45/Semi-VB-Decompiler> |
| ida_kernelcache | An IDA Toolkit for analyzing iOS kernelcaches. | 153 | <https://github.com/cellebrite-labs/ida_kernelcache> |
| idp_hexagon | Hexagon processor module for IDA Pro disassembler | 138 | <https://github.com/n-o-o-n/idp_hexagon> |
| STRIDE | Type recognition in decompiled executables | 123 | <https://github.com/hgarrereyn/STRIDE> |
| hexag00n | Hexag00n: A collection of reverse engineering tools for the Qualcomm Digital Signal Proccesor (QDSP6) | 120 | <https://github.com/programa-stic/hexag00n> |
| binja-hexagon *(archived)* | binja-hexagon | 118 | <https://github.com/google/binja-hexagon> |
| pcode2code | Decompiles VBA p-code back to source, based on pcodedmp | 116 | <https://github.com/Big5-sec/pcode2code> |
| bn-dyldsharedcache | this was a single-image DSC parser predating official support for DSC support in binaryninja. | 92 | <https://github.com/0cyn/bn-dyldsharedcache> |
| Trinity | Software reverse engineering tool for Java | 86 | <https://github.com/firstfault/Trinity> |
| ObjectiveNinja *(archived)* | Binary Ninja plugin & workflow to help analyze Objective-C code | 84 | <https://github.com/jonpalmisc/ObjectiveNinja> |
| iBoot-IDA *(archived)* | 32/64 bit SecureROM/iBoot loader for IDA Pro. Also supports loading and decrypting encrypted .im4ps within IDA. | 73 | <https://github.com/0cyn/iBoot-IDA> |
| seprom-loader | Binary Ninja loader for 64 bits Apple SEPROMs | 61 | <https://github.com/matteyeux/seprom-loader> |
| PbdViewer | Decompiler and viewer for PowerBuilder PBD/PBL libraries | 49 | <https://github.com/Hucxy/PbdViewer> |
| ida-swarm | Multi-agent AI system for automated reverse engineering in IDA | 41 | <https://github.com/shells-above/ida-swarm> |
| binja_kc | Plugin for loading MachO kernelcache and dSYM files to Binary Ninja | 39 | <https://github.com/skr0x1c0/binja_kc> |
| r2unity | Reverse engineer Unity games with radare2 | 38 | <https://github.com/radareorg/r2unity> |
| sephelper | IDA loader to help with SEPROM reverse engineering. | 36 | <https://github.com/haiyuidesu/sephelper> |
| iBoot-Binja-Loader | iBoot/SecureROM Loader | 35 | <https://github.com/EliseZeroTwo/iBoot-Binja-Loader> |
| tonguetwister | Macromedia Director file disassembler, Lingo decompiler and format documentation | 12 | <https://github.com/lham/tonguetwister> |
| visualbasic-rs | Rust library to parse and inspect compiled Visual Basic 6 binaries | 2 | <https://github.com/ATRAPSLLC/visualbasic-rs> |

## Dynamic Instrumentation

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| Frida | Dynamic instrumentation toolkit for native apps | 22,188 | <https://github.com/frida/frida> |
| rr | Record and replay debugger for Linux | 10,701 | <https://github.com/rr-debugger/rr> |
| Unicorn | Lightweight multi-architecture CPU emulator framework | 9,421 | <https://github.com/unicorn-engine/unicorn> |
| Triton | Dynamic binary analysis library with symbolic execution | 4,325 | <https://github.com/JonathanSalwan/Triton> |
| QIRA | Timeless debugger that records and lets you browse full program execution | 4,072 | <https://github.com/geohot/qira> |
| DynamoRIO | Dynamic binary instrumentation tool platform | 3,178 | <https://github.com/DynamoRIO/dynamorio> |
| PINCE | GDB front-end and memory scanner for reverse engineering games on Linux | 3,123 | <https://github.com/korcankaraokcu/PINCE> |
| edb | Cross-platform x86/x86-64 GUI debugger | 2,974 | <https://github.com/eteran/edb-debugger> |
| QBDI | LLVM-based dynamic binary instrumentation framework | 1,825 | <https://github.com/QBDI/QBDI> |
| r2frida | Radare2 and Frida integration | 1,448 | <https://github.com/nowsecure/r2frida> |
| TinyInst | Lightweight dynamic instrumentation library for Windows, macOS, Linux | 1,359 | <https://github.com/googleprojectzero/TinyInst> |
| Dwarf | Multi-arch debugger built on PyQt5 and Frida | 1,322 | <https://github.com/iGio90/Dwarf> |
| ellekit | yet another tweak injector / tweak hooking library for darwin systems | 723 | <https://github.com/tealbathingsuit/ellekit> |
| Spice86 | PC emulator built for reverse engineering and rewriting real-mode DOS programs | 660 | <https://github.com/OpenRakis/Spice86> |
| substitute | A free runtime modification library. | 589 | <https://github.com/comex/substitute> |
| JDBG | Java dynamic reverse engineering and debugging tool via injected DLL | 331 | <https://github.com/roger1337/JDBG> |
| snixpc | XPC message sniffer for macOS using LLDB | 50 | <https://github.com/tony-go/snixpc> |

## Mobile RE

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| jadx | Dex to Java decompiler for Android apps | 50,837 | <https://github.com/skylot/jadx> |
| Apktool | Tool for reverse engineering Android APK files | 25,817 | <https://github.com/iBotPeaches/Apktool> |
| dex2jar | Tools to convert Android .dex to Java .class files | 13,143 | <https://github.com/pxb1988/dex2jar> |
| Il2CppDumper | Unity il2cpp metadata dumper for reverse engineering | 9,493 | <https://github.com/Perfare/Il2CppDumper> |
| objection | Runtime mobile exploration toolkit powered by Frida | 9,436 | <https://github.com/sensepost/objection> |
| AssetRipper | Extracts Unity serialized assets and projects | 8,556 | <https://github.com/AssetRipper/AssetRipper> |
| Androguard | Python toolkit for Android app analysis | 6,341 | <https://github.com/androguard/androguard> |
| unidbg | Emulates Android native libraries (and experimentally iOS) to run app signing code | 5,261 | <https://github.com/zhkl0228/unidbg> |
| APKLab | Android reverse-engineering workbench for VS Code (apktool, jadx, smali) | 4,004 | <https://github.com/APKLab/APKLab> |
| apk.sh | Bash script automating pull, decode, rebuild and Frida-gadget patching of Android APKs | 3,842 | <https://github.com/ax/apk.sh> |
| class-dump | Generates Objective-C headers from Mach-O files | 3,586 | <https://github.com/nygard/class-dump> |
| Zygisk-Il2CppDumper | Dumps IL2CPP metadata at runtime on Android via Zygisk | 3,335 | <https://github.com/Perfare/Zygisk-Il2CppDumper> |
| Malimite | Decompiler for iOS and macOS apps (IPA/Mach-O) built on Ghidra | 3,215 | <https://github.com/LaurieWired/Malimite> |
| Il2CppInspector | Automated reverse-engineering tool for Unity IL2CPP binaries | 3,053 | <https://github.com/djkaty/Il2CppInspector> |
| Cpp2IL | Recovers managed .NET assemblies from Unity IL2CPP builds | 2,947 | <https://github.com/SamboyCoding/Cpp2IL> |
| UABEA | Unity Asset Bundle Extractor Avalonia: view and edit Unity assets | 2,450 | <https://github.com/nesrak1/UABEA> |
| ASC | On-demand Android decompiler front-end, much faster than JADX | 2,281 | <https://github.com/MG1937/ASC> |
| jnitrace | Frida-based tracer for JNI API usage in Android apps | 1,865 | <https://github.com/chame1eon/jnitrace> |
| frida-il2cpp-bridge | Frida module to dump and trace IL2CPP Unity apps at runtime | 1,756 | <https://github.com/vfsfitvnm/frida-il2cpp-bridge> |
| AndroidAppRE | Android app reverse engineering workshop | 1,565 | <https://github.com/maddiestone/AndroidAppRE> |
| Grapefruit | Runtime iOS application analysis tool built on Frida | 1,392 | <https://github.com/ChiChou/grapefruit> |
| hermes-dec | Disassembler and decompiler for React Native Hermes bytecode | 1,208 | <https://github.com/P1sec/hermes-dec> |
| garlic | Fast Java/Android APK and DEX decompiler written in pure C | 852 | <https://github.com/neocanable/garlic> |
| JADXecute | JADX-gui plugin for dynamic scripting of the decompiler | 751 | <https://github.com/LaurieWired/JADXecute> |
| Il2CppInspectorRedux | Maintained continuation of Il2CppInspector supporting newer metadata | 730 | <https://github.com/LukeFZ/Il2CppInspectorRedux> |
| apk2gold | CLI tool that decompiles Android APKs to Java source and resources | 700 | <https://github.com/lxdvs/apk2gold> |
| android-reverse-engineering-skill | Agent skill that decompiles APKs and extracts endpoints, auth headers and signing logic | 540 | <https://github.com/CreditTone/android-reverse-engineering-skill> |
| Il2CppInterop | Interop between CoreCLR and IL2CPP at runtime for modding | 398 | <https://github.com/BepInEx/Il2CppInterop> |
| hermes-decomp | Decompiler for React Native Hermes bytecode (.hbc) | 184 | <https://github.com/SymbioticSec/hermes-decomp> |
| rnidbg | Rust Android ARM64 emulator rewritten from unidbg | 164 | <https://github.com/fuqiuluo/rnidbg> |
| mobile-network-traffic | Guide to sniff Android HTTPS traffic with Waydroid and mitmproxy | 102 | <https://github.com/ddxv/mobile-network-traffic> |
| r2garlic | Fast Android DEX decompiler integrated into radare2 | 43 | <https://github.com/radareorg/r2garlic> |
| grida *(archived)* | Graphical reverse engineering UI for Frida on Android | 16 | <https://github.com/pluggyai/grida> |
| Talaria | Decompiles React Native Hermes bytecode to pseudocode | 2 | <https://github.com/moleium/talaria> |

## Other

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| rea | Agentic tool to reverse engineer apps from behavior down to native binaries | 100,604 | <https://github.com/morluto/rea> |
| ESP32 Bus Pirate | ESP32 hardware hacking tool that speaks I2C, SPI, UART, IR, RF and more protocols | 5,968 | <https://github.com/geo-tp/ESP32-Bit-Pirate> |
| FISSURE | RF and reverse engineering framework for signal detection, protocol discovery and attacks | 2,064 | <https://github.com/ainfosec/FISSURE> |
| Kong | Agentic, fully automated binary reverse engineering | 1,220 | <https://github.com/amruth-sn/kong> |
| Netzob | Protocol reverse engineering, modeling and fuzzing tool | 838 | <https://github.com/netzob/netzob> |
| re-shell | Nix-powered agentic reverse engineering environment | 532 | <https://github.com/schlarpc/re-shell> |
| Twonkie | USB-PD sniffer/injector/sink based on Google's Twinkie for protocol analysis | 415 | <https://github.com/dojoe/Twonkie> |
| Degate | Software for reverse engineering integrated circuits from die images | 294 | <https://github.com/DegateCommunity/Degate> |
| cobol-rekt | Toolkit for analysing and reverse engineering legacy COBOL code (flowcharts, CFGs) | 167 | <https://github.com/avishek-sen-gupta/cobol-rekt> |
| icestick-lpc-tpm-sniffer | FPGA-based LPC bus sniffer to extract TPM secrets | 84 | <https://github.com/SySS-Research/icestick-lpc-tpm-sniffer> |
| RET | FUTO's reverse-engineering tool | 79 | <https://github.com/futo-org/ret> |
| dfuexplorer | USB DFU client for reverse engineers | 38 | <https://github.com/travisgoodspeed/dfuexplorer> |
| Reverse-engineering-agent | MCP server giving AI agents 46 RE tools (Ghidra, GDB, Binwalk) | 35 | <https://github.com/The-Arabi/Reverse-engineering-agent> |
| mcp_reverse_engineering | MCP server exposing reverse engineering tools | 1 | <https://github.com/daedalus/mcp_reverse_engineering> |

## Traffic Interception

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| mitmproxy | Interactive TLS-capable intercepting HTTP proxy | 45,419 | <https://github.com/mitmproxy/mitmproxy> |
| mitmproxy2swagger | Reverse-engineers REST APIs into OpenAPI specs from captured mitmproxy/HAR traffic | 9,642 | <https://github.com/alufers/mitmproxy2swagger> |
| PCAPdroid | No-root Android network capture and traffic analysis | 4,898 | <https://github.com/emanuele-f/PCAPdroid> |
| reverse-api-engineer | Agent that captures website traffic and turns it into API clients | 1,265 | <https://github.com/kalil0321/reverse-api-engineer> |
| USBPcap | USB packet capture for Windows, used for driver protocol analysis | 1,138 | <https://github.com/desowin/usbpcap> |
| Proxelar | MitM proxy in Rust with TUI, terminal and web interfaces | 1,077 | <https://github.com/emanuele-em/proxelar> |
| tokentap (Sherlock) | MitM proxy that intercepts LLM tool API traffic to show what coding agents send | 813 | <https://github.com/jmuncor/tokentap> |
| HTTP Toolkit | Desktop app for intercepting and debugging HTTP(S) traffic | 736 | <https://github.com/httptoolkit/httptoolkit-desktop> |
| USB Sniffer Lite | Simple USB sniffer based on the Raspberry Pi RP2040 | 701 | <https://github.com/ataradov/usb-sniffer-lite> |
| httptoolkit-server | Backend of HTTP Toolkit HTTP(S) interception and debugging tool | 567 | <https://github.com/httptoolkit/httptoolkit-server> |
| usbrply | Converts USB pcaps into Python/C replay scripts for driver reverse engineering | 339 | <https://github.com/JohnDMcMaster/usbrply> |
| bluebox (web-hacker) | Reverse engineers web apps' undocumented APIs from browser traffic | 202 | <https://github.com/VectorlyApp/bluebox> |
| AutomatiQ | Reverse-engineering agent that turns web app traffic into APIs | 172 | <https://github.com/StoneSteel27/AutomatiQ> |
| usbsnoop | Live system-wide USB transfer sniffer in eBPF with inline protocol decoding | 87 | <https://github.com/yeet-src/usbsnoop> |
| BLE-Analyzer-pro-linux-capture | Linux capture tool for the reverse-engineered BLE Analyzer Pro USB sniffer | 77 | <https://github.com/xecaz/BLE-Analyzer-pro-linux-capture> |
| mitmcloak | mitmproxy addon mirroring real browser TLS/H2/H3 fingerprints upstream | 64 | <https://github.com/sardanioss/mitmcloak> |
| impersonate-proxy | Local MitM proxy to control TLS (JA3/JA4) and HTTP/2 fingerprints | 40 | <https://github.com/ytkoka/impersonate-proxy> |
| rever-browser | AI-agent browser for web API reverse engineering | 34 | <https://github.com/greekr4/rever-browser> |
| api-reverse-engineer | Chrome extension capturing fetch/XHR calls to reverse engineer site APIs | 32 | <https://github.com/ctala/api-reverse-engineer> |
| fritm | Cross-platform network reverse engineering framework hooking processes with Frida | 26 | <https://github.com/louisabraham/fritm> |
| Wireshark | Network protocol analyzer with dissectors for many reverse-engineered protocols |  | <https://gitlab.com/wireshark/wireshark> |
