# RE Tooling

[← All categories](../README.md) · 664 projects

- [AI-assisted RE](#ai-assisted-re) (56)
- [Binary & Format Analysis](#binary--format-analysis) (84)
- [Decompilation Project Tooling](#decompilation-project-tooling) (49)
- [Disassemblers & Decompilers](#disassemblers--decompilers) (236)
- [Dynamic Instrumentation](#dynamic-instrumentation) (61)
- [Mobile RE](#mobile-re) (106)
- [Other](#other) (37)
- [Traffic Interception](#traffic-interception) (35)

## AI-assisted RE

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| ida-pro-mcp | MCP bridge between IDA Pro and LLM clients | 12,654 | <https://github.com/mrexodia/ida-pro-mcp> |
| GhidraMCP | MCP server exposing Ghidra to LLM clients | 11,058 | <https://github.com/LaurieWired/GhidraMCP> |
| android-reverse-engineering-skill | Claude Code skill for reverse engineering Android apps | 8,047 | <https://github.com/SimoneAvogadro/android-reverse-engineering-skill> |
| Gepetto | IDA Pro plugin using LLMs to explain and rename decompiled functions | 3,477 | <https://github.com/JusticeRage/Gepetto> |
| jadx-ai-mcp | JADX plugin exposing an MCP server for AI-assisted Android RE | 2,878 | <https://github.com/zinja-coder/jadx-ai-mcp> |
| reagent | Reconstruct and validate C/C++ code from compiled programs with AI | 2,060 | <https://github.com/Dryxio/reagent> |
| WPeGPT | IDA plugin for AI-assisted binary analysis with OpenAI and DeepSeek models | 1,426 | <https://github.com/WPeace-HcH/WPeGPT> |
| open-reverselab | AI reverse-engineering agent platform and MCP server for Ghidra, Frida, x64dbg, Rizin | 1,250 | <https://github.com/LING71671/open-reverselab> |
| reverse-engineering-assistant | MCP server exposing Ghidra reverse engineering tasks to LLM agents | 867 | <https://github.com/cyberkaida/reverse-engineering-assistant> |
| GhidraGPT | Integrates LLMs into Ghidra for AI-assisted reverse engineering | 826 | <https://github.com/weirdmachine64/GhidraGPT> |
| jadx-mcp-server | MCP server for the JADX-AI plugin for Android RE | 794 | <https://github.com/zinja-coder/jadx-mcp-server> |
| unbrowse | Reverse engineers websites' internal APIs so agents can call them directly | 784 | <https://github.com/unbrowse-ai/unbrowse> |
| GhidrAssistMCP | MCP server extension for Ghidra | 769 | <https://github.com/symgraph/GhidrAssistMCP> |
| GhidrAssist | LLM assistant plugin for Ghidra | 756 | <https://github.com/symgraph/GhidrAssist> |
| x64DbgMCPServer | MCP server for x64dbg | 731 | <https://github.com/AgentSmithers/x64DbgMCPServer> |
| DAILA | Decompiler-agnostic AI assistant plugin for IDA, Ghidra, Binja and angr | 710 | <https://github.com/mahaloz/DAILA> |
| Rikugan | Reverse engineering agent for IDA Pro and Binary Ninja | 680 | <https://github.com/buzzer-re/Rikugan> |
| r2ai | LLM integration for radare2 | 487 | <https://github.com/radareorg/r2ai> |
| ida-multi-mcp | Multi-instance IDA Pro MCP server | 452 | <https://github.com/MeroZemory/ida-multi-mcp> |
| binary_ninja_mcp | Binary Ninja plugin with MCP server for LLM clients | 450 | <https://github.com/fosdickio/binary_ninja_mcp> |
| pyghidra-mcp | Command-line Python Ghidra MCP server | 441 | <https://github.com/clearbluejar/pyghidra-mcp> |
| idasql | SQL interface over IDA Pro databases via live virtual tables for agent-driven RE | 422 | <https://github.com/allthingsida/idasql> |
| GptHidra | Ghidra plugin using ChatGPT to explain functions | 404 | <https://github.com/evyatar9/GptHidra> |
| jebmcp | MCP server for the JEB decompiler | 261 | <https://github.com/flankerhqd/jebmcp> |
| binary-ninja-headless-mcp | Headless Binary Ninja MCP server for AI agents | 256 | <https://github.com/mrphrazer/binary-ninja-headless-mcp> |
| ghidra-cli | CLI for headless Ghidra analysis and decompilation with JSON output for AI agents | 239 | <https://github.com/akiselev/ghidra-cli> |
| ida_copilot | ChatGPT agent analysing IDA pseudocode | 234 | <https://github.com/DearVa/ida_copilot> |
| bn | Binary Ninja CLI for coding agents | 219 | <https://github.com/banteg/bn> |
| ghidra-headless-mcp | Headless Ghidra MCP server for AI agents | 190 | <https://github.com/mrphrazer/ghidra-headless-mcp> |
| re-skill | Claude Code skill for reverse engineering retro games | 168 | <https://github.com/vgrichina/re-skill> |
| HopperMCP *(archived)* | MCP server for Hopper Disassembler | 162 | <https://github.com/MxIris-Reverse-Engineering/HopperMCP> |
| GhidrOllama | Ghidra script analysing functions with local Ollama LLMs | 154 | <https://github.com/lr-m/GhidrOllama> |
| GhidraChatGPT *(archived)* | Brings ChatGPT into Ghidra | 152 | <https://github.com/likvidera/GhidraChatGPT> |
| oneiromancer | Reverse engineering assistant using a local LLM to analyse pseudocode | 146 | <https://github.com/0xdea/oneiromancer> |
| decyx | AI-powered Ghidra extension | 139 | <https://github.com/philsajdak/decyx> |
| polar | LLDB plugin bringing LLMs to LLDB | 132 | <https://github.com/ant4g0nist/polar> |
| DecompilerServer | MCP server for decompiling and analysing .NET assemblies | 117 | <https://github.com/pardeike/DecompilerServer> |
| windbg-decompile-ext | WinDbg extension that disassembles live functions and decompiles with an LLM | 111 | <https://github.com/kernullist/windbg-decompile-ext> |
| kernagent | Headless AI agent for deterministic reverse engineering | 103 | <https://github.com/Karib0u/kernagent> |
| mcp-server-idapro | MCP server letting AI assistants interact with IDA Pro | 102 | <https://github.com/fdrechsler/mcp-server-idapro> |
| iOS-reverse-engineering-claude-skill | Claude Code skill to extract and reverse engineer iOS apps | 101 | <https://github.com/incogbyte/iOS-reverse-engineering-claude-skill> |
| r0idamcp | SSE MCP server plugin for IDA Pro | 82 | <https://github.com/r0ysue/r0idamcp> |
| revula | Reverse engineering MCP server | 82 | <https://github.com/president-xd/revula> |
| IDA-Assistant | IDA plugin for automatic AI-assisted reverse engineering | 81 | <https://github.com/stuxnet147/IDA-Assistant> |
| binaryninja-openai | Integrates OpenAI with Binary Ninja | 77 | <https://github.com/WhatTheFuzz/binaryninja-openai> |
| Ryuumonbuchi | Headless Ghidra MCP server | 75 | <https://github.com/elliottophellia/Ryuumonbuchi> |
| ILSpy-Mcp | MCP server exposing ILSpy .NET decompilation to AI assistants | 70 | <https://github.com/bivex/ILSpy-Mcp> |
| BinAssist | Binary Ninja plugin providing LLM assistance | 67 | <https://github.com/symgraph/BinAssist> |
| recopilot | ReCopilot reverse engineering copilot for binary analysis | 66 | <https://github.com/XingTuLab/recopilot> |
| x64dbg-rippy | AI reverse engineering assistant chat panel for x64dbg | 62 | <https://github.com/dariushoule/x64dbg-rippy> |
| Vibe-Reverse-Engineering | LLM-friendly tools for Cursor to reverse engineer binaries, especially games | 59 | <https://github.com/Ekozmaster/Vibe-Reverse-Engineering> |
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
| binsider | Terminal UI to analyze ELF binaries | 4,476 | <https://github.com/orhun/binsider> |
| PE-bear | Multiplatform PE file reversing tool | 3,836 | <https://github.com/hasherezade/pe-bear> |
| DIE-engine | Detect It Easy engine for identifying file types, packers and compilers | 3,301 | <https://github.com/horsicq/DIE-engine> |
| rehex | Reverse-engineers' hex editor with structure annotation | 2,481 | <https://github.com/solemnwarning/rehex> |
| pefile | Python module to read and work with PE files | 2,075 | <https://github.com/erocarrera/pefile> |
| bincat | Static binary analyser with value/taint analysis and type reconstruction for IDA | 1,877 | <https://github.com/airbus-seclab/bincat> |
| pharos | Automated static analysis tools for binary programs | 1,739 | <https://github.com/cmu-sei/pharos> |
| pbtk | Toolset to extract .proto definitions from apps and fuzz Protobuf-based endpoints | 1,689 | <https://github.com/marin-m/pbtk> |
| XELFViewer | ELF file viewer and editor | 1,586 | <https://github.com/horsicq/XELFViewer> |
| binocle | Graphical tool to visualize binary data | 1,324 | <https://github.com/sharkdp/binocle> |
| XPEViewer | PE file viewer and editor | 1,240 | <https://github.com/horsicq/XPEViewer> |
| Veles *(archived)* | Binary data visualization and analysis tool | 1,238 | <https://github.com/codilime/veles> |
| e9patch | Static binary rewriting tool for x86-64 ELF binaries | 1,156 | <https://github.com/GJDuck/e9patch> |
| protobuf-inspector | Tool to reverse engineer Protocol Buffers messages with unknown definitions | 1,128 | <https://github.com/mildsunrise/protobuf-inspector> |
| AsmResolver | Library for reading, editing and writing PE files and .NET modules | 1,127 | <https://github.com/Washi1337/AsmResolver> |
| HexWalk | Hex viewer, editor and analyzer with binwalk integration | 1,026 | <https://github.com/gcarmix/HexWalk> |
| XMachOViewer | Mach-O file viewer for Windows, Linux and macOS | 968 | <https://github.com/horsicq/XMachOViewer> |
| PDBRipper | Extracts type and symbol information from PDB files | 908 | <https://github.com/horsicq/PDBRipper> |
| biodiff | Hex diff viewer using sequence alignment algorithms | 894 | <https://github.com/8051Enthusiast/biodiff> |
| hal | Hardware netlist reverse engineering and analysis framework | 835 | <https://github.com/emsec/hal> |
| readpe | PE file analysis toolkit | 789 | <https://github.com/mentebinaria/readpe> |
| hobbits | Multi-platform GUI for bit-level analysis and visualization of data | 754 | <https://github.com/Mahlet-Inc/hobbits> |
| retrowrite | Static binary rewriting to retrofit compiler passes into binaries | 751 | <https://github.com/HexHive/retrowrite> |
| fickling | Python pickle decompiler and static analyzer | 670 | <https://github.com/trailofbits/fickling> |
| pigaios | Matches and diffs source code directly against binaries | 651 | <https://github.com/joxeankoret/pigaios> |
| machoexplorer | Mach-O file explorer for macOS and Windows | 642 | <https://github.com/everettjf/machoexplorer> |
| Kam1n0-Community | Assembly code clone search and analysis platform | 627 | <https://github.com/McGill-DMaS/Kam1n0-Community> |
| Nauz-File-Detector | Linker, compiler and tool detector for binaries | 584 | <https://github.com/horsicq/Nauz-File-Detector> |
| sasquatch | Patched unsquashfs that handles vendor-modified SquashFS images | 567 | <https://github.com/devttys0/sasquatch> |
| pixd | Colourful visualization tool for binary files | 564 | <https://github.com/FireyFly/pixd> |
| Sibyl | Miasm-based function divination to identify known functions in binaries | 544 | <https://github.com/cea-sec/Sibyl> |
| ktool | pip install k2l \| Mach-O + Obj-C analysis TUI / CLI kit and library. Zero compiled deps, runs anywhere with a python... | 525 | <https://github.com/0cyn/ktool> |
| amoco | Python framework for static symbolic binary analysis | 493 | <https://github.com/bdcht/amoco> |
| pdb | Rust parser for Microsoft PDB (Program Database) debug information | 467 | <https://github.com/getsentry/pdb> |
| lscan | Library identification tool for statically linked stripped binaries | 409 | <https://github.com/maroueneboubakri/lscan> |
| Cerberus | Unstrips Rust and Go binaries (ELF and PE) | 407 | <https://github.com/h311d1n3r/Cerberus> |
| pe | Go package to parse and analyze PE files | 397 | <https://github.com/saferwall/pe> |
| idenLib | Library function identification for stripped binaries | 395 | <https://github.com/secrary/idenLib> |
| windiff | Compare symbols, types and syscalls across Windows builds | 390 | <https://github.com/ergrelet/windiff> |
| gtirb | Intermediate representation for binary analysis and rewriting | 381 | <https://github.com/GrammaTech/gtirb> |
| resym | Browse and extract C/C++ type declarations from PDB files | 372 | <https://github.com/ergrelet/resym> |
| hexerator | GUI hex editor focused on binary file exploration and pattern recognition | 371 | <https://github.com/crumblingstatue/hexerator> |
| CoBRA | Mixed Boolean-Arithmetic expression deobfuscation via coefficient reconstruction | 352 | <https://github.com/trailofbits/CoBRA> |
| sass-king | Reverse engineered NVIDIA SASS instruction dictionary and kernel audit patterns across GPU architectures | 343 | <https://github.com/florianmattana/sass-king> |
| evbunpack *(archived)* | Enigma Virtual Box unpacker | 334 | <https://github.com/mos9527/evbunpack> |
| dynStruct | DynamoRIO-based tool for automatic structure recovery | 329 | <https://github.com/ampotos/dynStruct> |
| Kaitai Struct Web IDE | Browser IDE for writing and testing Kaitai Struct format specs | 318 | <https://github.com/kaitai-io/kaitai_struct_webide> |
| regenny | Interactive tool to reconstruct structures and generate C headers while reverse engineering | 302 | <https://github.com/cursey/regenny> |
| BinDiffHelper | Ghidra extension integrating BinDiff function matching | 297 | <https://github.com/ubfx/BinDiffHelper> |
| veles | Visual binary analysis and reverse engineering tool | 287 | <https://github.com/wapiflapi/veles> |
| SWFREtools | Tools for reverse engineering Flash SWF files | 278 | <https://github.com/sporst/SWFREtools> |
| macaw | Open source binary analysis and symbolic execution tools | 257 | <https://github.com/GaloisInc/macaw> |
| senseye | Dynamic visual debugging and data reverse engineering tool suite | 252 | <https://github.com/letoram/senseye> |
| qbindiff | Binary diffing framework | 246 | <https://github.com/quarkslab/qbindiff> |
| quokka | Fast and accurate binary exporter from IDA | 227 | <https://github.com/quarkslab/quokka> |
| fugue-core | Binary analysis framework written in Rust | 186 | <https://github.com/fugue-re/fugue-core> |
| degate *(archived)* | Open source software for chip reverse engineering from die images | 175 | <https://github.com/nitram2342/degate> |
| qiew | Hex/file format viewer for reverse engineering | 174 | <https://github.com/mtivadar/qiew> |
| delsum | Checksum reverse engineering toolbox that finds checksum parameters from samples | 169 | <https://github.com/8051Enthusiast/delsum> |
| idbutil | Library and tool for reading IDA Pro databases | 165 | <https://github.com/nlitsme/idbutil> |
| pyidbutil | Python library for reading IDA Pro databases | 161 | <https://github.com/nlitsme/pyidbutil> |
| resource_dasm | Classic Mac OS resource fork decoder and 68K/PPC disassembler with format-specific RE tools | 158 | <https://github.com/fuzziqersoftware/resource_dasm> |
| rematch | Open binary diffing framework | 156 | <https://github.com/nirizr/rematch> |
| bcov | Static binary instrumentation for coverage analysis | 153 | <https://github.com/abenkhadra/bcov> |
| PREF | Portable reverse engineering framework | 145 | <https://github.com/PREF/PREF> |
| mmo-chip | Multiplayer CMOS standard cell chip reverse engineering tool | 140 | <https://github.com/giulioz/mmo-chip> |
| pdb-decompiler | Decompiles MSVC PDB files into C++ source declarations | 138 | <https://github.com/camden-smallwood/pdb-decompiler> |
| ProtobufDecoder | Protobuf payload decoder and analyzer without schema | 104 | <https://github.com/sandermvanvliet/ProtobufDecoder> |
| crcbeagle | CRC reverse engineering tool in Python | 97 | <https://github.com/colinoflynn/crcbeagle> |
| rustbinsign | Rust symbol recovery tool | 91 | <https://github.com/N0fix/rustbinsign> |
| patchestry | Binary patching framework built with MLIR and Ghidra | 88 | <https://github.com/lifting-bits/patchestry> |
| retools | Reverse engineering toolkit including ARM emulator and spec-derived disassembler | 88 | <https://github.com/agustingianni/retools> |
| pbd | Disassembles serialized protobuf descriptors back to .proto | 86 | <https://github.com/rsc-dev/pbd> |
| ReGAL | Scripts to reverse engineer old programmable logic devices (PAL/GAL) | 78 | <https://github.com/psurply/ReGAL> |
| Deroute | Tool to untangle wires for chip die reverse engineering | 76 | <https://github.com/emu-russia/Deroute> |
| psr | Pointer Sequence Reverser for Windows C++ application structures | 76 | <https://github.com/nccgroup/psr> |
| recover | Recovers compile units from stripped binaries | 75 | <https://github.com/huku-/recover> |
| protodec | Protobuf decompiler recovering .proto from binaries | 74 | <https://github.com/schdub/protodec> |
| ninjadiff | Binary diffing plugin for Binary Ninja | 71 | <https://github.com/riverloopsec/ninjadiff> |
| Virtual-File-System-Editor | Extracts embedded files from application virtualizers | 64 | <https://github.com/extremecoders-re/Virtual-File-System-Editor> |
| prawntools | Integrated circuit reverse engineering software | 62 | <https://github.com/JohnDMcMaster/prawntools> |
| mootool | MachO's Other Tooling | 12 | <https://github.com/hack-different/mootool> |

## Decompilation Project Tooling

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| Diaphora | Program diffing plugin for IDA, Ghidra-compatible exports | 4,422 | <https://github.com/joxeankoret/diaphora> |
| PS2Recomp | Playstation 2 Static Recompiler & Runtime Tool to make native PC ports | 3,370 | <https://github.com/ran-j/PS2Recomp> |
| BinDiff | Binary diffing tool for comparing disassembled code | 3,204 | <https://github.com/google/bindiff> |
| ghidriff | Ghidra-based command-line binary diffing engine | 812 | <https://github.com/clearbluejar/ghidriff> |
| BinSync | Reverse-engineering collaboration and sync across decompilers | 750 | <https://github.com/binsync/binsync> |
| DecompilerMC *(archived)* | Decompiles any Minecraft version using official mappings | 722 | <https://github.com/hube12/DecompilerMC> |
| m2c | MIPS/PowerPC/ARM assembly to C decompiler aimed at matching output | 655 | <https://github.com/matt-kempster/m2c> |
| ghidra-delinker-extension | Ghidra extension exporting relocatable object files for delinking | 608 | <https://github.com/boricj/ghidra-delinker-extension> |
| objdiff | Local object-file diffing tool for matching decompilation projects | 574 | <https://github.com/encounter/objdiff> |
| RecompOne | PSX Static Recompiler and Runtime, Not Affiliated With Sony or PlayStation | 557 | <https://github.com/BlackLabelHQ/RecompOne> |
| XenosRecomp | A tool for converting Xbox 360 shaders to HLSL. | 499 | <https://github.com/hedge-dev/XenosRecomp> |
| splat | Binary splitting tool for N64, PS1, PS2 and PSP decompilation projects | 366 | <https://github.com/ethteck/splat> |
| pokemon-reverse-engineering-tools *(archived)* | Tools for building and disassembling Pokemon Red and Crystal | 351 | <https://github.com/pret/pokemon-reverse-engineering-tools> |
| mgbdis | Game Boy ROM disassembler with RGBDS-compatible output | 327 | <https://github.com/mattcurrie/mgbdis> |
| decomp-toolkit | GameCube/Wii decompilation toolkit: splits binaries and generates build configs | 306 | <https://github.com/encounter/decomp-toolkit> |
| poryscript | High-level scripting language for Gen 3 Pokemon decompilation projects | 305 | <https://github.com/huderlem/poryscript> |
| decomp-permuter | Randomly permutes C code to find a match with target assembly | 230 | <https://github.com/simonlindholm/decomp-permuter> |
| psx-modding-toolchain | Tools to mod and reverse engineer PlayStation 1 games | 193 | <https://github.com/mateusfavarin/psx-modding-toolchain> |
| rabbitizer | MIPS instruction decoder library used by decomp tooling | 181 | <https://github.com/Decompollaborate/rabbitizer> |
| wibo | Minimal Windows binary loader to run old Win32 compilers on Linux | 179 | <https://github.com/decompals/wibo> |
| asm-differ | Assembly differ for matching decompilation work | 175 | <https://github.com/simonlindholm/asm-differ> |
| reccmp | Tools for comparing recompiled code against original binaries | 157 | <https://github.com/isledecomp/reccmp> |
| ccc | Library and tools for parsing PS2 debugging symbols | 108 | <https://github.com/chaoticgd/ccc> |
| llvm8 | Statically recompiling CHIP8 to Windows and macOS using LLVM | 99 | <https://github.com/ioncodes/llvm8> |
| dtk-template | Project template for decomp-toolkit GameCube/Wii decompilations | 84 | <https://github.com/encounter/dtk-template> |
| ido-static-recomp | Static recompilation of the IDO 5.3 and 7.1 compilers for modern platforms | 83 | <https://github.com/decompals/ido-static-recomp> |
| spimdisasm | MIPS disassembler that produces matching-ready assembly for decomp projects | 83 | <https://github.com/Decompollaborate/spimdisasm> |
| decomp.dev | Decompilation progress website and GitHub bot | 80 | <https://github.com/encounter/decomp.dev> |
| porytiles | Overworld tileset compiler for Gen III Pokemon decompilation projects | 80 | <https://github.com/grunt-lucas/porytiles> |
| Mizuchi | Pipeline that combines m2c, permuter, objdiff and AI to auto-decompile functions | 76 | <https://github.com/macabeus/mizuchi> |
| mzretools | Tools for reversing DOS games via MZ executable inspection | 72 | <https://github.com/neuviemeporte/mzretools> |
| ZomboidDecompiler | Decompilation tool specialised for Project Zomboid using Vineflower | 67 | <https://github.com/demiurgeQuantified/ZomboidDecompiler> |
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
| bytecode-viewer | Java JAR and Android APK reverse engineering suite with multiple decompilers, editor and debugger | 15,665 | <https://github.com/Konloch/bytecode-viewer> |
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
| pyinstxtractor | Extractor for PyInstaller-generated executables | 4,500 | <https://github.com/extremecoders-re/pyinstxtractor> |
| Fernflower | Analytical Java bytecode decompiler used in IntelliJ IDEA | 4,420 | <https://github.com/JetBrains/fernflower> |
| uncompyle6 | Cross-version Python bytecode decompiler | 4,331 | <https://github.com/rocky/python-uncompyle6> |
| Miasm | Python reverse engineering framework: disassembly, IR, symbolic execution, emulation | 3,988 | <https://github.com/cea-sec/miasm> |
| rizin | UNIX-like reverse engineering framework (radare2 fork) | 3,951 | <https://github.com/rizinorg/rizin> |
| Plasma | Interactive disassembler for x86/ARM/MIPS with pseudo-C output | 3,070 | <https://github.com/plasma-disassembler/plasma> |
| Mono.Cecil | Library to inspect and modify .NET CIL assemblies | 3,005 | <https://github.com/jbevain/cecil> |
| binnavi *(archived)* | Binary analysis IDE for inspecting and annotating control flow graphs | 2,885 | <https://github.com/google/binnavi> |
| CFR | Java decompiler supporting modern Java features | 2,715 | <https://github.com/leibnitz27/cfr> |
| Decompiler Explorer | Dogbolt: compare output of many decompilers in the browser | 2,704 | <https://github.com/decompiler-explorer/decompiler-explorer> |
| Keystone | Multi-architecture assembler framework | 2,644 | <https://github.com/keystone-engine/keystone> |
| Reko | General-purpose binary decompiler supporting many CPU architectures | 2,612 | <https://github.com/uxmal/reko> |
| dnlib | Library to read and write .NET assemblies and modules | 2,489 | <https://github.com/0xd4d/dnlib> |
| flare-ida *(archived)* | IDA Pro utilities from the FLARE team | 2,450 | <https://github.com/mandiant/flare-ida> |
| ret-sync | Synchronizes debugger sessions with IDA, Ghidra and Binary Ninja | 2,395 | <https://github.com/bootleg/ret-sync> |
| Vineflower | Modern Java decompiler (Fernflower fork, formerly Quiltflower) | 2,395 | <https://github.com/Vineflower/vineflower> |
| BAP | Binary Analysis Platform for lifting and analysing binaries | 2,262 | <https://github.com/BinaryAnalysisPlatform/bap> |
| Snowman *(archived)* | Native code to C/C++ decompiler for x86, x86-64 and ARM | 2,243 | <https://github.com/yegord/snowman> |
| keypatch | Multi-architecture assembler plugin for IDA Pro | 1,878 | <https://github.com/keystone-engine/keypatch> |
| remill | Library lifting machine code to LLVM bitcode | 1,858 | <https://github.com/lifting-bits/remill> |
| REDasm | Interactive multi-architecture disassembler | 1,821 | <https://github.com/redasm-dev/redasm> |
| AvaloniaILSpy *(archived)* | Cross-platform Avalonia GUI for the ILSpy .NET decompiler | 1,810 | <https://github.com/icsharpcode/AvaloniaILSpy> |
| rev.ng | Binary analysis framework and decompiler based on LLVM and QEMU | 1,749 | <https://github.com/revng/revng> |
| iaito | Official Qt GUI for radare2 | 1,719 | <https://github.com/radareorg/iaito> |
| Ponce | IDA plugin for one-click symbolic execution | 1,632 | <https://github.com/illera88/Ponce> |
| BARF | Binary Analysis and Reverse engineering Framework for x86/ARM | 1,455 | <https://github.com/programa-stic/barf-project> |
| panopticon *(archived)* | Libre cross-platform disassembler | 1,446 | <https://github.com/das-labor/panopticon> |
| pylingual | Python decompiler for modern Python bytecode versions | 1,418 | <https://github.com/syssec-utd/pylingual> |
| Virtuailor | IDAPython tool reconstructing C++ virtual tables in IDA Pro | 1,403 | <https://github.com/0xgalz/Virtuailor> |
| FLIRTDB | Community collection of IDA FLIRT library signature files | 1,365 | <https://github.com/Maktm/FLIRTDB> |
| binaryninja-api | Public API, examples and docs for the Binary Ninja reverse-engineering platform | 1,324 | <https://github.com/Vector35/binaryninja-api> |
| patching | Interactive binary patching plugin for IDA Pro | 1,290 | <https://github.com/gaasedelen/patching> |
| decompile3 | Python 3.7+ bytecode decompiler | 1,276 | <https://github.com/rocky/python-decompile3> |
| NETReactorSlayer | Deobfuscator and unpacker for Eziriz .NET Reactor | 1,270 | <https://github.com/SychicBoy/NETReactorSlayer> |
| xAnalyzer | x64dbg plugin for automatic API call and function analysis | 1,238 | <https://github.com/ThunderCls/xAnalyzer> |
| Procyon | Java metaprogramming suite and decompiler | 1,222 | <https://github.com/mstrobel/procyon> |
| binexport | Exports disassemblies from IDA, Ghidra and Binary Ninja into Protocol Buffers | 1,212 | <https://github.com/google/binexport> |
| angr-management | GUI for the angr binary analysis framework | 1,189 | <https://github.com/angr/angr-management> |
| IDR | Interactive Delphi Reconstructor: decompiler for Delphi executables | 1,166 | <https://github.com/crypto2011/IDR> |
| lumen | Private reimplementation of IDA Pro's Lumina server | 1,162 | <https://github.com/naim94a/lumen> |
| ViperMonkey | VBA parser and emulation engine for analysing Office macros | 1,129 | <https://github.com/decalage2/ViperMonkey> |
| medusa | Open source interactive disassembler | 1,089 | <https://github.com/wisk/medusa> |
| vivisect | Python binary analysis framework, disassembler and debugger | 1,002 | <https://github.com/vivisect/vivisect> |
| idacode | VS Code integration for running and debugging IDAPython scripts | 993 | <https://github.com/ioncodes/idacode> |
| rz-ghidra | Ghidra decompiler and Sleigh disassembler integration for Rizin and Cutter | 990 | <https://github.com/rizinorg/rz-ghidra> |
| Porosity | Decompiler and security analysis tool for Ethereum smart contracts | 934 | <https://github.com/msuiche/porosity> |
| Karta | Source-code-assisted binary matching plugin for IDA | 912 | <https://github.com/CheckPointSW/Karta> |
| VMAttack | IDA Pro plugin for analysing virtualization-based obfuscation | 890 | <https://github.com/anatolikalysch/VMAttack> |
| ddisasm | Fast reassembleable disassembler | 874 | <https://github.com/GrammaTech/ddisasm> |
| IDAssist | AI-augmented reverse engineering plugin for IDA Pro | 871 | <https://github.com/symgraph/IDAssist> |
| JByteMod-Beta | Java bytecode editor | 859 | <https://github.com/loerting/JByteMod-Beta> |
| BiTE | Cross-platform executable viewer and disassembler with strong Rust support | 826 | <https://github.com/WINSDK/bite> |
| decomp2dbg | Syncs decompiler symbols and types into GDB | 824 | <https://github.com/mahaloz/decomp2dbg> |
| GhIDA | GhIDA | 820 | <https://github.com/Cisco-Talos/GhIDA> |
| retdec-idaplugin | RetDec plugin for IDA | 798 | <https://github.com/avast/retdec-idaplugin> |
| Ghidrathon *(archived)* | Python 3 scripting support for Ghidra | 790 | <https://github.com/mandiant/Ghidrathon> |
| fcd | LLVM-based optimizing native-code decompiler | 773 | <https://github.com/fay59/fcd> |
| rzweb | Browser-based reverse engineering platform built on Rizin compiled to WebAssembly | 763 | <https://github.com/IndAlok/rzweb> |
| pyinstxtractor-ng | PyInstaller extractor next generation | 737 | <https://github.com/pyinstxtractor/pyinstxtractor-ng> |
| NtRays | Hex-Rays microcode plugin simplifying Windows kernel decompilation | 682 | <https://github.com/can1357/NtRays> |
| lucid | Interactive Hex-Rays microcode explorer | 678 | <https://github.com/gaasedelen/lucid> |
| AlphaGolang | IDAPython scripts for analysing Go binaries | 675 | <https://github.com/SentineLabs/AlphaGolang> |
| Sark | Pythonic library simplifying IDAPython | 672 | <https://github.com/tmr232/Sark> |
| IDArling *(archived)* | Collaborative reverse engineering plugin for IDA Pro and Hex-Rays | 670 | <https://github.com/IDArlingTeam/IDArling> |
| golang_loader_assist | IDA Pro script making Go binary reversing easier | 661 | <https://github.com/strazzere/golang_loader_assist> |
| Ghidra-Cpp-Class-Analyzer *(archived)* | Ghidra C++ class and RTTI analyzer | 651 | <https://github.com/astrelsky/Ghidra-Cpp-Class-Analyzer> |
| Rellic | Produces goto-free C output from LLVM bitcode for decompilation | 619 | <https://github.com/lifting-bits/rellic> |
| r2dec-js | Pseudo-C decompiler plugin for radare2 and rizin | 610 | <https://github.com/wargio/r2dec-js> |
| XLMMacroDeobfuscator | Extracts and emulates Excel 4.0 (XLM) macros from XLS, XLSM and XLSB files | 590 | <https://github.com/DissectMalware/XLMMacroDeobfuscator> |
| Kuna | Agent-first decompiler written in Rust | 583 | <https://github.com/Noelo-Lab/kuna> |
| r2ghidra | Native Ghidra decompiler integration for radare2 | 559 | <https://github.com/radareorg/r2ghidra> |
| beaengine | BeaEngine x86/x64 disassembler library | 549 | <https://github.com/BeaEngine/beaengine> |
| FindCrypt-Ghidra | FindCrypt port for Ghidra with updated crypto signatures | 549 | <https://github.com/d3v1l401/FindCrypt-Ghidra> |
| E-Decompiler | IDA plugin to analyse programs written in E-language (Yi Yuyan) | 537 | <https://github.com/fjqisba/E-Decompiler> |
| decompiler | Python decompiler with multiple backends for IDA and Capstone | 535 | <https://github.com/EiNSTeiN-/decompiler> |
| Yagi | Ghidra decompiler integration for IDA | 510 | <https://github.com/airbus-cert/Yagi> |
| decomp | Components of a decompilation pipeline (LLVM IR to Go) | 492 | <https://github.com/decomp/decomp> |
| pcodedmp | Disassembler for undocumented VBA p-code in Office macro documents | 492 | <https://github.com/bontchev/pcodedmp> |
| Unreal-Library | Decompiler and parser for Unreal Engine package files | 488 | <https://github.com/EliotVU/Unreal-Library> |
| luajit-decompiler-v2 | LuaJIT bytecode decompiler | 485 | <https://github.com/marsinator358/luajit-decompiler-v2> |
| HexraysToolbox | Finds code patterns in the Hex-Rays ctree | 483 | <https://github.com/patois/HexraysToolbox> |
| sigmakerex | Enhanced IDA Pro signature generator plugin | 483 | <https://github.com/kweatherman/sigmakerex> |
| mdec *(archived)* | Compare output of multiple decompilers side by side | 460 | <https://github.com/mborgerson/mdec> |
| RABCDAsm | ActionScript 3 bytecode (ABC) assembler and disassembler | 457 | <https://github.com/CyberShadow/RABCDAsm> |
| wasmdec | WebAssembly to C decompiler | 428 | <https://github.com/wwwg/wasmdec> |
| nyxstone | LLVM-based assembly and disassembly library with Rust and Python bindings | 426 | <https://github.com/emproof-com/nyxstone> |
| IDAObjcTypes | Type and function definitions for analysing iOS/macOS binaries in IDA | 420 | <https://github.com/PoomSmart/IDAObjcTypes> |
| ScratchABit | Retargetable interactive disassembler with IDAPython-compatible plugin API | 413 | <https://github.com/pfalcon/ScratchABit> |
| Boomerang | General open-source machine-code decompiler | 406 | <https://github.com/BoomerangDecompiler/boomerang> |
| CodemerxDecompile | Standalone cross-platform .NET decompiler | 399 | <https://github.com/codemerx/CodemerxDecompile> |
| radeco | radare2-based decompiler and symbolic executor in Rust | 399 | <https://github.com/radareorg/radeco> |
| aiDAPal | IDA Pro plugin with fine-tuned local LLM for Hex-Rays pseudocode | 394 | <https://github.com/atredispartners/aidapal> |
| dnSpy.Extension.HoLLy | dnSpy extension to aid reversing obfuscated assemblies | 389 | <https://github.com/holly-hacker/dnSpy.Extension.HoLLy> |
| OldRod | Automated KoiVM disassembler and devirtualizer | 386 | <https://github.com/Washi1337/OldRod> |
| GhidRust | Rust decompiler plugin for Ghidra | 384 | <https://github.com/DMaroo/GhidRust> |
| ddc | Fast Android DEX to Java decompiler in Rust | 376 | <https://github.com/ejfkdev/ddc> |
| Ghidra-Switch-Loader | Nintendo Switch binary loader for Ghidra | 373 | <https://github.com/Adubbz/Ghidra-Switch-Loader> |
| ghidra_kernelcache | a Ghidra framework for iOS kernelcache reverse engineering | 373 | <https://github.com/0x36/ghidra_kernelcache> |
| rattle | EVM binary static analysis framework | 366 | <https://github.com/crytic/rattle> |
| ghidra_bridge | Python 3 bridge to Ghidra's Python scripting | 364 | <https://github.com/justfoxing/ghidra_bridge> |
| Sekiryu (GhidrAI) *(archived)* | Ghidra headless toolkit with automatic decompilation and LLM analysis | 360 | <https://github.com/20urc3/Sekiryu> |
| seninja | Symbolic execution plugin for Binary Ninja | 357 | <https://github.com/borzacchiello/seninja> |
| classinformer-ida7 | ClassInformer RTTI plugin backported for IDA Pro 7 | 354 | <https://github.com/rcx/classinformer-ida7> |
| abyss | Augments Hex-Rays decompiler output | 349 | <https://github.com/patois/abyss> |
| IDA_ClassInformer_PlugIn | IDA ClassInformer plugin for MSVC RTTI and vftables | 348 | <https://github.com/kweatherman/IDA_ClassInformer_PlugIn> |
| ida-minsc | Functional DWIM IDAPython plugin | 335 | <https://github.com/arizvisa/ida-minsc> |
| d810 | IDA Pro plugin to deobfuscate code at decompilation time | 332 | <https://github.com/joydo/d810> |
| microavx | AVX lifter for the Hex-Rays decompiler | 331 | <https://github.com/gaasedelen/microavx> |
| replica | Ghidra analysis enhancer | 314 | <https://github.com/reb311ion/replica> |
| super-jadx | Fork-style JADX extension adding renaming, reference graphs and other RE features | 312 | <https://github.com/pkilller/super-jadx> |
| ida_medigate | IDA plugin for C++ class and vtable reverse engineering | 310 | <https://github.com/medigateio/ida_medigate> |
| GhydraMCP | Ghidra plugin with REST API and MCP bridge for agentic multi-binary reverse engineering | 303 | <https://github.com/starsong-consulting/GhydraMCP> |
| ida-batch_decompile | IDA batch decompile plugin for Hex-Rays | 299 | <https://github.com/tintinweb/ida-batch_decompile> |
| ProjectorRays | Decompiler for Macromedia/Adobe Director and Shockwave Lingo | 299 | <https://github.com/ProjectorRays/ProjectorRays> |
| GhidraBoy *(archived)* | Sharp SM83 / Game Boy extension for Ghidra | 286 | <https://github.com/Gekkio/GhidraBoy> |
| abi-guesser | Guesses Ethereum ABI from calldata without the contract ABI | 285 | <https://github.com/openchainxyz/abi-guesser> |
| LuaAssemblyTools | Lua bytecode assembly and disassembly tools | 284 | <https://github.com/efrederickson/LuaAssemblyTools> |
| Cafebabe | Java bytecode editor and decompiler GUI | 271 | <https://github.com/GraxCode/Cafebabe> |
| luajit-decomp | LuaJIT decompiler | 271 | <https://github.com/bobsayshilol/luajit-decomp> |
| iBoot64helper | IDAPython loader for AArch64 iBoot, iBEC and SecureROM reverse engineering | 266 | <https://github.com/argp/iBoot64helper> |
| jd-gui-duo | Multi-decompiler Java GUI supporting JD-Core, CFR, Procyon and Fernflower | 265 | <https://github.com/nbauma109/jd-gui-duo> |
| Ghidra_GolangAnalyzerExtension | Ghidra extension to analyze Go binaries | 261 | <https://github.com/mooncat-greenpy/Ghidra_GolangAnalyzerExtension> |
| ghidra-emotionengine-reloaded | Ghidra extension adding PlayStation 2 Emotion Engine support | 247 | <https://github.com/chaoticgd/ghidra-emotionengine-reloaded> |
| hexagon | IDA processor module for the hexagon (QDSP6) processor | 241 | <https://github.com/gsmk/hexagon> |
| eBPF-for-Ghidra | eBPF processor module for Ghidra | 237 | <https://github.com/Nalen98/eBPF-for-Ghidra> |
| dewolf | Research decompiler implemented as a Binary Ninja plugin | 236 | <https://github.com/fkie-cad/dewolf> |
| abi-decompiler | Ethereum EVM smart contract ABI recovery helper | 232 | <https://github.com/Decurity/abi-decompiler> |
| FunctionInliner | An IDA plugin that eases reversing of binaries that have been code-size-optimized with function outlining | 230 | <https://github.com/cellebrite-labs/FunctionInliner> |
| ida-sigmaker | Cross-platform IDA Pro 9 signature maker plugin | 226 | <https://github.com/mahmoudimus/ida-sigmaker> |
| holodec | Decompiler for x86 and x86-64 ELF binaries | 220 | <https://github.com/Cararasu/holodec> |
| idaxex | XEX/XBE loader plugin for IDA supporting Xbox and Xbox 360 executables | 215 | <https://github.com/emoose/idaxex> |
| rePy2exe | Reverse engineering tool for py2exe applications | 209 | <https://github.com/4w4k3/rePy2exe> |
| AMIE | Minimalist ARM instruction extender for IDA Pro | 203 | <https://github.com/NeatMonster/AMIE> |
| ai-reverse-engineering | AI-assisted binary reverse engineering with Ghidra and LLMs | 199 | <https://github.com/biniamf/ai-reverse-engineering> |
| BTD DNN decompiler | Decompiles x86 deep neural network executables back to model structure and weights | 199 | <https://github.com/monkbai/DNN-decompiler> |
| Dhrake | Ghidra scripts for reverse engineering Delphi binaries | 195 | <https://github.com/huettenhain/dhrake> |
| standalone-app | All-in-one Java reverse engineering tool | 194 | <https://github.com/helios-decompiler/standalone-app> |
| ghidralib | Pythonic Ghidra standard library | 191 | <https://github.com/msm-code/ghidralib> |
| jsc-decompile-mozjs-34 | SpiderMonkey 34 JavaScript bytecode decoder and decompiler | 189 | <https://github.com/irelance/jsc-decompile-mozjs-34> |
| vscode-decompiler | Decompile binaries and bytecode directly from VS Code | 179 | <https://github.com/tintinweb/vscode-decompiler> |
| DelphiHelper | IDA Pro plugin for analysing Delphi binaries | 173 | <https://github.com/eset/DelphiHelper> |
| ida-iboot-loader | IDA loader for Apple's 64 bits iBoot, SecureROM and AVPBooter | 172 | <https://github.com/matteyeux/ida-iboot-loader> |
| IDA-For-Delphi | IDAPython script recovering Delphi VCL event function names | 171 | <https://github.com/Coldzer0/IDA-For-Delphi> |
| CrowdDetox *(archived)* | Hex-Rays plugin removing junk code and variables | 166 | <https://github.com/CrowdStrike/CrowdDetox> |
| Py2ExeDecompiler | Decompiler for py2exe executables | 165 | <https://github.com/endgameinc/Py2ExeDecompiler> |
| binja-retdec *(archived)* | Binary Ninja plugin using RetDec to decompile | 164 | <https://github.com/hugsy/binja-retdec> |
| ceasta | Disassembler, decompiler and debugger with built-in MCP server | 164 | <https://github.com/ngwg/ceasta> |
| PacXplorer | IDA plugin to find code cross references to virtual functions using PAC codes | 159 | <https://github.com/cellebrite-labs/PacXplorer> |
| emilpro | Graphical multi-architecture disassembler | 157 | <https://github.com/SimonKagstrom/emilpro> |
| Semi-VB-Decompiler | Partial decompiler for Visual Basic 5/6 executables and their file structure | 155 | <https://github.com/VBGAMER45/Semi-VB-Decompiler> |
| ida_kernelcache | An IDA Toolkit for analyzing iOS kernelcaches. | 153 | <https://github.com/cellebrite-labs/ida_kernelcache> |
| ida_missinglink | IDA plugin filling in missing indirect CALL and JMP targets | 150 | <https://github.com/kweatherman/ida_missinglink> |
| IDA-VTableExplorer | IDA plugin for automatic vtable detection and inheritance analysis | 148 | <https://github.com/K4ryuu/IDA-VTableExplorer> |
| kaiju | CERT Kaiju binary analysis extension for Ghidra | 147 | <https://github.com/cmu-sei/kaiju> |
| LabSync | IDA plugin to partially synchronize IDBs between researchers | 144 | <https://github.com/cellebrite-labs/LabSync> |
| CollaRE | Multi-tool reverse engineering collaboration solution | 143 | <https://github.com/Martyx00/CollaRE> |
| pyc2bytecode | Python bytecode disassembler for analysing compiled Python binaries | 143 | <https://github.com/knight0x07/pyc2bytecode> |
| ghostrings | Ghidra scripts recovering string definitions in Go binaries | 141 | <https://github.com/nccgroup/ghostrings> |
| Despector *(archived)* | Java and Kotlin decompiler and AST library | 140 | <https://github.com/Despector/Despector> |
| idp_hexagon | Hexagon processor module for IDA Pro disassembler | 138 | <https://github.com/n-o-o-n/idp_hexagon> |
| ghidra-gekko-broadway-lang | Ghidra language for GameCube/Wii Gekko and Broadway CPUs | 135 | <https://github.com/aldelaro5/ghidra-gekko-broadway-lang> |
| QtREAnalyzer | Ghidra extension to reverse engineer Qt binaries | 134 | <https://github.com/diommsantos/QtREAnalyzer> |
| nuitka-static-unpacker | Static unpacker for analysing Nuitka-compiled binaries | 133 | <https://github.com/DimaReverse/nuitka-static-unpacker> |
| ObjCGraphView | Binary Ninja graph view plugin for Objective-C | 131 | <https://github.com/trailofbits/ObjCGraphView> |
| dnEditor *(archived)* | .NET assembly editor based on dnlib | 128 | <https://github.com/ViRb3/dnEditor> |
| x86devirt | Automatic devirtualization of x86 VM-protected code | 128 | <https://github.com/JeremyWildsmith/x86devirt> |
| ghidra-xbe | Xbox XBE executable loader for Ghidra | 126 | <https://github.com/XboxDev/ghidra-xbe> |
| vm_jit | VM devirtualization proof of concept based on AsmJit and LLVM | 125 | <https://github.com/archercreat/vm_jit> |
| ghidrasql | SQL interface for querying Ghidra program databases | 124 | <https://github.com/0xeb/ghidrasql> |
| augur | IDA assistant extracting strings and related pseudocode | 123 | <https://github.com/0xdea/augur> |
| STRIDE | Type recognition in decompiled executables | 123 | <https://github.com/hgarrereyn/STRIDE> |
| hexag00n | Hexag00n: A collection of reverse engineering tools for the Qualcomm Digital Signal Proccesor (QDSP6) | 120 | <https://github.com/programa-stic/hexag00n> |
| binja-hexagon *(archived)* | binja-hexagon | 118 | <https://github.com/google/binja-hexagon> |
| idasec | IDA plugin for dynamic analysis with the Binsec platform | 117 | <https://github.com/RobinDavid/idasec> |
| striga | Experimental x86_64 to LLVM IR lifter in Python | 117 | <https://github.com/LLVMParty/striga> |
| decompiler | Ghidra decompiler plugin for LLDB | 116 | <https://github.com/ant4g0nist/decompiler> |
| pcode2code | Decompiles VBA p-code back to source, based on pcodedmp | 116 | <https://github.com/Big5-sec/pcode2code> |
| decompile-py2exe | Decompiles py2exe-generated Python 3 executables | 115 | <https://github.com/NVISOsecurity/decompile-py2exe> |
| fa | Automation tool for locating symbols and structs in binaries | 112 | <https://github.com/doronz88/fa> |
| sol-azy | Static analysis and reverse engineering toolchain for Solana sBPF programs | 111 | <https://github.com/FuzzingLabs/sol-azy> |
| HLSL-Decompiler | Converts DXBC/DXIL/SPIR-V shaders to HLSL | 110 | <https://github.com/YYadorigi/HLSL-Decompiler> |
| ScratchABlock | Experimental decompiler framework | 110 | <https://github.com/pfalcon/ScratchABlock> |
| spedi | Speculative disassembly and CFG recovery from stripped binaries | 109 | <https://github.com/abenkhadra/spedi> |
| ida_gel | IDA loaders for game console ELFs (PS3, PS Vita, Wii U) | 106 | <https://github.com/aerosoul94/ida_gel> |
| erays | Ethereum smart contract reverse engineering tool | 104 | <https://github.com/teamnsrg/erays> |
| dsc_fix | Aids reversing dyld_shared_cache libraries in IDA | 101 | <https://github.com/deepinstinct/dsc_fix> |
| nampa | FLIRT signatures for Binary Ninja | 101 | <https://github.com/thebabush/nampa> |
| revsync | Realtime cross-tool collaborative reverse engineering | 100 | <https://github.com/lunixbochs/revsync> |
| collabREate | Collaborative reverse engineering plugin for IDA Pro | 98 | <https://github.com/cseagle/collabREate> |
| GhidraFindcrypt | Ghidra plugin locating cryptographic constants | 98 | <https://github.com/antoniovazquezblanco/GhidraFindcrypt> |
| NotDec | WebAssembly decompiler and static analysis framework on LLVM IR | 94 | <https://github.com/NotDec/NotDec> |
| bn-dyldsharedcache | this was a single-image DSC parser predating official support for DSC support in binaryninja. | 92 | <https://github.com/0cyn/bn-dyldsharedcache> |
| wcdatool | Watcom disassembly tool for DOS applications | 91 | <https://github.com/fonic/wcdatool> |
| ghidra-snes | Ghidra scripts for SNES ROM reverse engineering | 89 | <https://github.com/joshleaves/ghidra-snes> |
| NeverD | AI-friendly binary analysis and decompilation engine | 88 | <https://github.com/NeverSight/NeverD> |
| Trinity | Software reverse engineering tool for Java | 86 | <https://github.com/firstfault/Trinity> |
| ghidra-lx-loader | Ghidra loader for LX/LE executables (OS/2, DOS4GW, VxD) | 85 | <https://github.com/yetmorecode/ghidra-lx-loader> |
| ObjectiveNinja *(archived)* | Binary Ninja plugin & workflow to help analyze Objective-C code | 84 | <https://github.com/jonpalmisc/ObjectiveNinja> |
| DnD | Decompiler that recovers DNN model semantics from compiled binaries | 83 | <https://github.com/purseclab/DnD> |
| herast | Framework to automate Hex-Rays AST work in IDA Pro | 76 | <https://github.com/Mizari/herast> |
| QtRE | Ghidra headless analyzer for Qt binaries | 75 | <https://github.com/OSUSecLab/QtRE> |
| aevt_decompile | Decompiler for run-only AppleScript files | 74 | <https://github.com/SentineLabs/aevt_decompile> |
| idapcode | IDA plugin displaying Ghidra P-code for the current function | 72 | <https://github.com/binarly-io/idapcode> |
| dynlib | IDA Pro plugin for PS4 user-mode ELF reverse engineering | 71 | <https://github.com/aerosoul94/dynlib> |
| ghidra-wasm-plugin | Ghidra WebAssembly plugin with disassembly and decompilation | 69 | <https://github.com/garrettgu10/ghidra-wasm-plugin> |
| unluac-rs | Cross-platform Rust Lua decompilation library for multiple dialects | 68 | <https://github.com/x3zvawq/unluac-rs> |
| jsdec | Simple decompiler for Rizin | 67 | <https://github.com/rizinorg/jsdec> |
| JustDecompileEngine | Decompilation engine of CodemerxDecompile | 66 | <https://github.com/codemerx/JustDecompileEngine> |
| ptxNinja | Binary Ninja plugin for NVIDIA PTX | 66 | <https://github.com/seekbytes/ptxNinja> |
| pdbgen | Generates PDB files from Ghidra | 62 | <https://github.com/wandel/pdbgen> |
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
| HyperDbg | Hypervisor-based native debugger for reverse engineering | 4,124 | <https://github.com/HyperDbg/HyperDbg> |
| QIRA | Timeless debugger that records and lets you browse full program execution | 4,072 | <https://github.com/geohot/qira> |
| sogen | Windows and Linux userspace emulator for analysis | 3,688 | <https://github.com/momo5502/sogen> |
| DynamoRIO | Dynamic binary instrumentation tool platform | 3,178 | <https://github.com/DynamoRIO/dynamorio> |
| PINCE | GDB front-end and memory scanner for reverse engineering games on Linux | 3,123 | <https://github.com/korcankaraokcu/PINCE> |
| edb | Cross-platform x86/x86-64 GUI debugger | 2,974 | <https://github.com/eteran/edb-debugger> |
| panda | Platform for architecture-neutral dynamic analysis built on QEMU | 2,784 | <https://github.com/panda-re/panda> |
| lighthouse | Code coverage explorer plugin for IDA and Binary Ninja | 2,604 | <https://github.com/gaasedelen/lighthouse> |
| frida-snippets | Hand-crafted Frida examples | 2,539 | <https://github.com/iddoeldor/frida-snippets> |
| QBDI | LLVM-based dynamic binary instrumentation framework | 1,825 | <https://github.com/QBDI/QBDI> |
| tiny_tracer | Intel Pin tool for tracing API calls | 1,708 | <https://github.com/hasherezade/tiny_tracer> |
| tenet | Execution trace explorer plugin for IDA Pro | 1,546 | <https://github.com/gaasedelen/tenet> |
| r2frida | Radare2 and Frida integration | 1,448 | <https://github.com/nowsecure/r2frida> |
| TinyInst | Lightweight dynamic instrumentation library for Windows, macOS, Linux | 1,359 | <https://github.com/googleprojectzero/TinyInst> |
| Dwarf | Multi-arch debugger built on PyQt5 and Frida | 1,322 | <https://github.com/iGio90/Dwarf> |
| frida-ios-hook | Frida-based tool to trace and modify iOS app methods | 1,188 | <https://github.com/yazgx97/frida-ios-hook> |
| dumpulator | Library for emulating code from Windows memory dumps | 888 | <https://github.com/mrexodia/dumpulator> |
| HookCase | Tool for hooking and reverse engineering macOS / OS X processes | 841 | <https://github.com/steven-michaud/HookCase> |
| lisa.py | LLDB MCP integration and helper commands for reverse engineering | 756 | <https://github.com/ant4g0nist/lisa.py> |
| ellekit | yet another tweak injector / tweak hooking library for darwin systems | 723 | <https://github.com/tealbathingsuit/ellekit> |
| Spice86 | PC emulator built for reverse engineering and rewriting real-mode DOS programs | 660 | <https://github.com/OpenRakis/Spice86> |
| cryptoshark | Self-optimizing code tracer based on dynamic recompilation | 602 | <https://github.com/frida/cryptoshark> |
| ttddbg | Time Travel Debugging trace plugin for IDA | 595 | <https://github.com/airbus-cert/ttddbg> |
| vscode-frida | Unofficial Frida extension for VS Code | 593 | <https://github.com/ChiChou/vscode-frida> |
| substitute | A free runtime modification library. | 589 | <https://github.com/comex/substitute> |
| s2e | Platform for multi-path program analysis with selective symbolic execution | 525 | <https://github.com/S2E/s2e> |
| wirebrowser | CDP-based runtime instrumentation platform for browsers | 508 | <https://github.com/fcavallarin/wirebrowser> |
| llef | LLDB plugin making it more useful for reverse engineering | 491 | <https://github.com/foundryzero/llef> |
| udbserver | GDB debug server for the Unicorn emulator | 435 | <https://github.com/bet4it/udbserver> |
| drltrace | DynamoRIO-based library call tracer for Windows and Linux | 419 | <https://github.com/mxmssh/drltrace> |
| Simpleator | Windows x64 user-mode application emulator using Hyper-V | 404 | <https://github.com/ionescu007/Simpleator> |
| Frida-Script-Runner | Web-based Frida toolkit for Android and iOS | 381 | <https://github.com/z3n70/Frida-Script-Runner> |
| STrace | DTrace on Windows reimplementation for syscall tracing | 379 | <https://github.com/mandiant/STrace> |
| rgat | Instruction trace visualisation tool for dynamic analysis | 371 | <https://github.com/ncatlin/rgat> |
| JDBG | Java dynamic reverse engineering and debugging tool via injected DLL | 331 | <https://github.com/roger1337/JDBG> |
| bread | BIOS reverse engineering and debugging over serial with GDB support | 328 | <https://github.com/Theldus/bread> |
| execution-trace-viewer | Tool for viewing and analyzing execution traces | 325 | <https://github.com/teemu-l/execution-trace-viewer> |
| GhidraEmu | Native P-code emulator plugin for Ghidra | 308 | <https://github.com/Nalen98/GhidraEmu> |
| frick | Debugger built on top of Frida | 296 | <https://github.com/iGio90/frick> |
| fripack | Packages Frida scripts into standalone executables | 232 | <https://github.com/std-microblock/fripack> |
| goauld | Dynamic injection tool for Linux and Android | 227 | <https://github.com/androguard/goauld> |
| Unicorn-Trace | Unicorn-based ARM64 dynamic tracing tool with IDA integration | 208 | <https://github.com/chenxvb/Unicorn-Trace> |
| RESim | Reverse engineering software using a full-system Simics simulator | 195 | <https://github.com/mfthomps/RESim> |
| uDdbg | GDB-like debugger for the Unicorn emulator | 195 | <https://github.com/iGio90/uDdbg> |
| FridaHooker *(archived)* | Android Frida GUI manager | 183 | <https://github.com/wrlu/FridaHooker> |
| fridax | Frida tooling to read variables and hook functions in Xamarin/Mono apps | 181 | <https://github.com/NorthwaveSecurity/fridax> |
| gxpc | Sniffs macOS/iOS XPC communication using Frida and Go | 167 | <https://github.com/ReverseApple/gxpc> |
| pyda | Write dynamic binary analysis tools in Python | 158 | <https://github.com/ndrewh/pyda> |
| frida-analykit | Frida toolkit for Android reverse engineering | 155 | <https://github.com/ZSA233/frida-analykit> |
| iostrace *(archived)* | strace alternative for 64-bit iOS devices using Frida | 154 | <https://github.com/sh1ma/iostrace> |
| ida-splode | Augments IDA static analysis with Pin-based dynamic instrumentation | 133 | <https://github.com/zachriggle/ida-splode> |
| ghostwire | Stealth runtime instrumentation and CDP for web reverse engineering | 126 | <https://github.com/sofianeelhor/ghostwire> |
| Taint-Rev-Trace | ARM trace taint tracking and search tool with MCP support | 113 | <https://github.com/Aar0n3906/Taint-Rev-Trace> |
| XPCSniffer | Sniffs XPC messages on iOS devices | 95 | <https://github.com/evilpenguin/XPCSniffer> |
| koidbg *(archived)* | Debugger for Windows ARM64 aimed at reverse engineers | 73 | <https://github.com/keowu/koidbg> |
| frida-stack | Better stacks and backtraces in Frida | 64 | <https://github.com/rednaga/frida-stack> |
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
| apkstudio | Cross-platform Qt IDE for reverse engineering and rebuilding Android APKs | 4,677 | <https://github.com/vaibhavpandeyvpz/apkstudio> |
| simplify | Android virtual machine and generic Dalvik deobfuscator | 4,670 | <https://github.com/CalebFenton/simplify> |
| APKLab | Android reverse-engineering workbench for VS Code (apktool, jadx, smali) | 4,004 | <https://github.com/APKLab/APKLab> |
| apk.sh | Bash script automating pull, decode, rebuild and Frida-gadget patching of Android APKs | 3,842 | <https://github.com/ax/apk.sh> |
| android-hidden-api | Library providing access to Android hidden APIs and internal resources | 3,623 | <https://github.com/anggrayudi/android-hidden-api> |
| class-dump | Generates Objective-C headers from Mach-O files | 3,586 | <https://github.com/nygard/class-dump> |
| Zygisk-Il2CppDumper | Dumps IL2CPP metadata at runtime on Android via Zygisk | 3,335 | <https://github.com/Perfare/Zygisk-Il2CppDumper> |
| Malimite | Decompiler for iOS and macOS apps (IPA/Mach-O) built on Ghidra | 3,215 | <https://github.com/LaurieWired/Malimite> |
| RMS-Runtime-Mobile-Security | Frida-based web UI to manipulate Android and iOS apps at runtime | 3,110 | <https://github.com/m0bilesecurity/RMS-Runtime-Mobile-Security> |
| Il2CppInspector | Automated reverse-engineering tool for Unity IL2CPP binaries | 3,053 | <https://github.com/djkaty/Il2CppInspector> |
| Cpp2IL | Recovers managed .NET assemblies from Unity IL2CPP builds | 2,947 | <https://github.com/SamboyCoding/Cpp2IL> |
| reFlutter | Flutter reverse engineering framework that patches libflutter to expose Dart snapshot info | 2,769 | <https://github.com/Impact-I/reFlutter> |
| blutter | Flutter app reverse engineering tool that recovers Dart objects and functions from libapp.so | 2,732 | <https://github.com/worawit/blutter> |
| UABEA | Unity Asset Bundle Extractor Avalonia: view and edit Unity assets | 2,450 | <https://github.com/nesrak1/UABEA> |
| ASC | On-demand Android decompiler front-end, much faster than JADX | 2,281 | <https://github.com/MG1937/ASC> |
| jnitrace | Frida-based tracer for JNI API usage in Android apps | 1,865 | <https://github.com/chame1eon/jnitrace> |
| frida-il2cpp-bridge | Frida module to dump and trace IL2CPP Unity apps at runtime | 1,756 | <https://github.com/vfsfitvnm/frida-il2cpp-bridge> |
| AndroidAppRE | Android app reverse engineering workshop | 1,565 | <https://github.com/maddiestone/AndroidAppRE> |
| magisk-frida | Magisk module running frida-server on boot | 1,470 | <https://github.com/ViRb3/magisk-frida> |
| Grapefruit | Runtime iOS application analysis tool built on Frida | 1,392 | <https://github.com/ChiChou/grapefruit> |
| restore-symbol | Restores the stripped symbol table of iOS app binaries | 1,339 | <https://github.com/tobefuturer/restore-symbol> |
| hermes-dec | Disassembler and decompiler for React Native Hermes bytecode | 1,208 | <https://github.com/P1sec/hermes-dec> |
| android-unpacker | Android unpacker presented at DEF CON 22 | 1,181 | <https://github.com/strazzere/android-unpacker> |
| ZygiskFrida | Zygisk module that injects Frida gadget into Android apps | 1,095 | <https://github.com/lico-n/ZygiskFrida> |
| garlic | Fast Java/Android APK and DEX decompiler written in pure C | 852 | <https://github.com/neocanable/garlic> |
| eDBG | eBPF-based lightweight Android debugger with MCP support | 851 | <https://github.com/ShinoLeah/eDBG> |
| decompile-apk | Scripts to decompile APKs | 824 | <https://github.com/venshine/decompile-apk> |
| onekey-decompile-apk | One-step APK decompilation tool | 800 | <https://github.com/ufologist/onekey-decompile-apk> |
| binder-trace | Intercepts and parses Android Binder messages, like Wireshark for Binder | 771 | <https://github.com/foundryzero/binder-trace> |
| JADXecute | JADX-gui plugin for dynamic scripting of the decompiler | 751 | <https://github.com/LaurieWired/JADXecute> |
| Il2CppInspectorRedux | Maintained continuation of Il2CppInspector supporting newer metadata | 730 | <https://github.com/LukeFZ/Il2CppInspectorRedux> |
| apk2gold | CLI tool that decompiles Android APKs to Java source and resources | 700 | <https://github.com/lxdvs/apk2gold> |
| XAPKDetector | APK/DEX packer and compiler detector | 694 | <https://github.com/horsicq/XAPKDetector> |
| jni_helper | Finds JNI function signatures in APKs and applies them to RE tools | 674 | <https://github.com/evilpan/jni_helper> |
| hbctool | Assembler/disassembler for React Native Hermes bytecode | 643 | <https://github.com/bongtrop/hbctool> |
| chomper | Lightweight framework for emulating crypto algorithms in iOS executables | 631 | <https://github.com/sledgeh4w/chomper> |
| AndBug | Scriptable Android debugger for reverse engineering | 599 | <https://github.com/swdunlop/AndBug> |
| abc-decompiler | Decompiler for HarmonyOS ABC bytecode | 586 | <https://github.com/ohos-decompiler/abc-decompiler> |
| android-reverse-engineering-skill | Agent skill that decompiles APKs and extracts endpoints, auth headers and signing logic | 540 | <https://github.com/CreditTone/android-reverse-engineering-skill> |
| dex-oracle | Pattern-based Dalvik deobfuscator using limited execution | 504 | <https://github.com/CalebFenton/dex-oracle> |
| elf-dump-fix | Dumps Android ELF libraries from memory and rebuilds section headers | 486 | <https://github.com/maiyao1988/elf-dump-fix> |
| MagiskHluda | Magisk module running a less detectable Frida server on boot | 433 | <https://github.com/Exo1i/MagiskHluda> |
| ARSCLib | Android binary resources (ARSC/AXML) read and write library | 415 | <https://github.com/REAndroid/ARSCLib> |
| theos-jailed | Theos module for developing jailed iOS tweaks | 409 | <https://github.com/kabiroberai/theos-jailed> |
| Il2CppInterop | Interop between CoreCLR and IL2CPP at runtime for modding | 398 | <https://github.com/BepInEx/Il2CppInterop> |
| phantom-frida | Builds a Frida server from source with anti-detection patches | 392 | <https://github.com/TheQmaks/phantom-frida> |
| ApkToolBoxGUI | GUI toolbox around apktool and related APK tools | 374 | <https://github.com/AloysHF/ApkToolBoxGUI> |
| react-native-decompiler | Decompiles React Native Android/iOS bundles | 371 | <https://github.com/numandev1/react-native-decompiler> |
| JNIAnalyzer | Ghidra scripts for analysing Android NDK libraries | 366 | <https://github.com/Ayrx/JNIAnalyzer> |
| darter | Dart / Flutter VM snapshot analyzer | 345 | <https://github.com/mildsunrise/darter> |
| jnitrace-engine | Engine used by jnitrace to intercept JNI API calls | 335 | <https://github.com/chame1eon/jnitrace-engine> |
| smalisca *(archived)* | Static code analysis for Smali files | 323 | <https://github.com/dorneanu/smalisca> |
| apkx | One-step APK decompilation with multiple backends | 320 | <https://github.com/muellerberndt/apkx> |
| droidlysis | Property extractor for Android apps | 312 | <https://github.com/cryptax/droidlysis> |
| WTFJH *(archived)* | One-step iOS binary runtime instrumentation | 282 | <https://github.com/Naville/WTFJH> |
| dalvikus | Android reverse engineering tool and smali editor | 272 | <https://github.com/loerting/dalvikus> |
| axmlprinter | Library for parsing compiled Android XML manifests | 263 | <https://github.com/rednaga/axmlprinter> |
| appdbg | Runs Android app methods on a standard JVM for analysis | 262 | <https://github.com/asmjmp0/appdbg> |
| renef | Mobile reverse engineering framework | 256 | <https://github.com/Byterialab/renef> |
| apk-utilities | Tools and scripts to manipulate Android APKs | 252 | <https://github.com/ViRb3/apk-utilities> |
| resymbol | Restores stripped Mach-O symbols and dumps Objective-C/Swift types | 229 | <https://github.com/paradiseduo/resymbol> |
| android-lkms | Android loadable kernel modules for reversing and debugging | 226 | <https://github.com/strazzere/android-lkms> |
| unidbg-server | Spring Boot service wrapping unidbg to run Android native code | 222 | <https://github.com/cxapython/unidbg-server> |
| legu_unpacker_2019 | Scripts to unpack APKs protected by Tencent Legu | 214 | <https://github.com/quarkslab/legu_unpacker_2019> |
| Dex-Editor-Android | Android Dalvik bytecode (DEX) editor | 212 | <https://github.com/developer-krushna/Dex-Editor-Android> |
| revengi-app | Toolkit app for smali grammar, DEX repair and Flutter analysis | 201 | <https://github.com/RevEngiSquad/revengi-app> |
| arkdecompiler | HarmonyOS NEXT ArkTS bytecode decompiler | 199 | <https://github.com/jd-opensource/arkdecompiler> |
| Termux-Apktool | Decompile and recompile Android apps in Termux without OpenJDK | 190 | <https://github.com/Lexiie/Termux-Apktool> |
| hermes-decomp | Decompiler for React Native Hermes bytecode (.hbc) | 184 | <https://github.com/SymbioticSec/hermes-decomp> |
| native-shim | Shim for loading native JNI libraries for Android active debugging | 181 | <https://github.com/rednaga/native-shim> |
| flutter-re-demo | Experiments on reverse engineering Flutter applications | 178 | <https://github.com/Guardsquare/flutter-re-demo> |
| iCDump *(archived)* | Modern Objective-C class dump based on LIEF and LLVM | 171 | <https://github.com/romainthomas/iCDump> |
| rnidbg | Rust Android ARM64 emulator rewritten from unidbg | 164 | <https://github.com/fuqiuluo/rnidbg> |
| iOSreExtension *(archived)* | VS Code extension for iOS reverse engineering projects | 155 | <https://github.com/Lakr233/iOSreExtension> |
| Dexter | Advanced DEX editor for Android | 153 | <https://github.com/omeraydindev/Dexter> |
| LeguDecompile | Static unpacker for Tencent Legu-protected .so libraries | 142 | <https://github.com/dzx1994/LeguDecompile> |
| Jarida | Jadx GUI plugin to trace and hook methods with Frida | 128 | <https://github.com/BitTheByte/Jarida> |
| noia | Frida-powered mobile app sandbox file browser | 128 | <https://github.com/0x742/noia> |
| PulseAPK-Core | Cross-platform APK decompilation and rebuilding tool | 127 | <https://github.com/deemoun/PulseAPK-Core> |
| androidReverse | On-device Android reverse engineering with radare2 and Java decompilers | 120 | <https://github.com/UltraSina/androidReverse> |
| Zygisk-Loader | Zygisk module hot-swapping native libraries into Android apps | 118 | <https://github.com/HanSoBored/Zygisk-Loader> |
| binder-trace | Kernel-based Android Binder transaction observer | 115 | <https://github.com/fuqiuluo/binder-trace> |
| PulseAPK | WPF frontend for apktool and signing | 115 | <https://github.com/deemoun/PulseAPK> |
| dexdec | Fast Android decompiler for humans and AI agents | 111 | <https://github.com/asLody/dexdec> |
| r0dump | ART-integrated DEX dumper and repair toolkit for Android 16 | 106 | <https://github.com/tiwe0/r0dump> |
| autojs-unpacker | Reverse engineering tool for Android AutoJS applications | 105 | <https://github.com/imlk0/autojs-unpacker> |
| reverse_flutter | Tools and guidelines for reverse engineering Flutter apps | 105 | <https://github.com/Neoxs/reverse_flutter> |
| android-jar-with-hidden-api | Steps to build an android.jar exposing AOSP hidden APIs | 104 | <https://github.com/JetpackDuba/android-jar-with-hidden-api> |
| mobile-network-traffic | Guide to sniff Android HTTPS traffic with Waydroid and mitmproxy | 102 | <https://github.com/ddxv/mobile-network-traffic> |
| ghidra-jni | jni.h compiled as a Ghidra data type archive | 98 | <https://github.com/extremecoders-re/ghidra-jni> |
| il2Fusion | Unity and Cocos2d-x Lua game reverse engineering toolkit for Android | 84 | <https://github.com/PenguinAndy/il2Fusion> |
| FLEXLoader | Loads FLEX to debug arbitrary third-party iOS apps | 70 | <https://github.com/buginux/FLEXLoader> |
| banjo | Android DEX disassembler and Binary Ninja plugin | 68 | <https://github.com/ivision-research/banjo> |
| jscHookR *(archived)* | Reverse engineering tool for Android Cocos2d-JS apps | 67 | <https://github.com/Mas0nShi/jscHookR> |
| AndroidRunnableJadx | Run Android Java methods inside Jadx without a device | 62 | <https://github.com/asmjmp0/AndroidRunnableJadx> |
| r2garlic | Fast Android DEX decompiler integrated into radare2 | 43 | <https://github.com/radareorg/r2garlic> |
| grida *(archived)* | Graphical reverse engineering UI for Frida on Android | 16 | <https://github.com/pluggyai/grida> |
| Talaria | Decompiles React Native Hermes bytecode to pseudocode | 2 | <https://github.com/moleium/talaria> |

## Other

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| rea | Agentic tool to reverse engineer apps from behavior down to native binaries | 100,604 | <https://github.com/morluto/rea> |
| ESP32 Bus Pirate | ESP32 hardware hacking tool that speaks I2C, SPI, UART, IR, RF and more protocols | 5,968 | <https://github.com/geo-tp/ESP32-Bit-Pirate> |
| webcrack | Deobfuscates obfuscator.io output and unpacks bundled JavaScript | 2,958 | <https://github.com/j4k0xb/webcrack> |
| FISSURE | RF and reverse engineering framework for signal detection, protocol discovery and attacks | 2,064 | <https://github.com/ainfosec/FISSURE> |
| shuji | Recovers original JavaScript and CSS sources from source maps | 1,244 | <https://github.com/paazmaya/shuji> |
| Kong | Agentic, fully automated binary reverse engineering | 1,220 | <https://github.com/amruth-sn/kong> |
| javascript-deobfuscator | General purpose JavaScript deobfuscator | 1,153 | <https://github.com/ben-sb/javascript-deobfuscator> |
| wakaru | JavaScript decompiler and unpacker for modern frontend bundles | 1,012 | <https://github.com/pionxzh/wakaru> |
| Netzob | Protocol reverse engineering, modeling and fuzzing tool | 838 | <https://github.com/netzob/netzob> |
| obfuscator-io-deobfuscator | Deobfuscator for scripts obfuscated by Obfuscator.io | 807 | <https://github.com/ben-sb/obfuscator-io-deobfuscator> |
| debundle | Debundler that recreates source trees from Browserify or Webpack bundles | 739 | <https://github.com/1egoman/debundle> |
| avscript *(archived)* | Interactive shell for Avast's JavaScript engine extracted via reverse engineering | 673 | <https://github.com/taviso/avscript> |
| unwebpack-sourcemap *(archived)* | Extracts uncompiled SPA source code from Webpack source maps | 545 | <https://github.com/rarecoil/unwebpack-sourcemap> |
| re-shell | Nix-powered agentic reverse engineering environment | 532 | <https://github.com/schlarpc/re-shell> |
| win32-darkmode | Example using the undocumented Windows dark mode API in Win32 apps | 523 | <https://github.com/ysc3839/win32-darkmode> |
| Twonkie | USB-PD sniffer/injector/sink based on Google's Twinkie for protocol analysis | 415 | <https://github.com/dojoe/Twonkie> |
| Musa.Veil | Collection of undocumented Windows API declarations | 372 | <https://github.com/MiroKaku/Musa.Veil> |
| etw-providers-docs | Documentation of undocumented Windows ETW providers | 306 | <https://github.com/repnz/etw-providers-docs> |
| Degate | Software for reverse engineering integrated circuits from die images | 294 | <https://github.com/DegateCommunity/Degate> |
| cobol-rekt | Toolkit for analysing and reverse engineering legacy COBOL code (flowcharts, CFGs) | 167 | <https://github.com/avishek-sen-gupta/cobol-rekt> |
| Windows-Insight | Research on the inner workings of Windows components | 153 | <https://github.com/ernw/Windows-Insight> |
| pkg-unpacker | Unpacks Node.js applications packaged with pkg | 134 | <https://github.com/LockBlock-dev/pkg-unpacker> |
| jsdeob-workbench | Visual workbench for deobfuscating JavaScript with chained AST transforms | 120 | <https://github.com/Owl4444/jsdeob-workbench> |
| pcb-tracer | Tool aiding reverse engineering and documentation of PCBs | 118 | <https://github.com/rpelorosso/pcb-tracer> |
| WarbirdExamples | Examples of using Microsoft's undocumented Warbird technology | 97 | <https://github.com/DownWithUp/WarbirdExamples> |
| WslReverse | Experiments with hidden WSL COM interfaces and LxBus IPC | 88 | <https://github.com/Biswa96/WslReverse> |
| icestick-lpc-tpm-sniffer | FPGA-based LPC bus sniffer to extract TPM secrets | 84 | <https://github.com/SySS-Research/icestick-lpc-tpm-sniffer> |
| pcbre | Integrated printed circuit board reverse engineering toolkit | 84 | <https://github.com/pcbre/pcbre> |
| jvm-dump-proxy *(archived)* | Proxy DLL dumping JVM classes at the JNI level on Windows | 80 | <https://github.com/ViRb3/jvm-dump-proxy> |
| wesp-research | Reverse engineering research and tools for Windows Event Streaming Protocols | 80 | <https://github.com/marcosd4h/wesp-research> |
| RET | FUTO's reverse-engineering tool | 79 | <https://github.com/futo-org/ret> |
| webpackTools | Userscript for reverse engineering and modifying production webpack apps | 77 | <https://github.com/moonlight-mod/webpackTools> |
| depcb | PCB reverse engineering tool | 74 | <https://github.com/unixdj/depcb> |
| windows-native | Rust bindings for undocumented Windows native (ntdll) APIs | 46 | <https://github.com/NiiightmareXD/windows-native> |
| dfuexplorer | USB DFU client for reverse engineers | 38 | <https://github.com/travisgoodspeed/dfuexplorer> |
| Reverse-engineering-agent | MCP server giving AI agents 46 RE tools (Ghidra, GDB, Binwalk) | 35 | <https://github.com/The-Arabi/Reverse-engineering-agent> |
| mcp_reverse_engineering | MCP server exposing reverse engineering tools | 1 | <https://github.com/daedalus/mcp_reverse_engineering> |

## Traffic Interception

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| mitmproxy | Interactive TLS-capable intercepting HTTP proxy | 45,419 | <https://github.com/mitmproxy/mitmproxy> |
| mitmproxy2swagger | Reverse-engineers REST APIs into OpenAPI specs from captured mitmproxy/HAR traffic | 9,642 | <https://github.com/alufers/mitmproxy2swagger> |
| apk-mitm | CLI that prepares Android APKs for HTTPS inspection by removing pinning | 5,125 | <https://github.com/niklashigi/apk-mitm> |
| ssl-kill-switch2 | Disables SSL certificate validation and pinning in iOS and macOS apps | 3,323 | <https://github.com/nabla-c0d3/ssl-kill-switch2> |
| reverse-api-engineer | Agent that captures website traffic and turns it into API clients | 1,265 | <https://github.com/kalil0321/reverse-api-engineer> |
| USBPcap | USB packet capture for Windows, used for driver protocol analysis | 1,138 | <https://github.com/desowin/usbpcap> |
| Proxelar | MitM proxy in Rust with TUI, terminal and web interfaces | 1,077 | <https://github.com/emanuele-em/proxelar> |
| android-unpinner | Removes certificate pinning from Android APKs | 1,051 | <https://github.com/mitmproxy/android-unpinner> |
| tokentap (Sherlock) | MitM proxy that intercepts LLM tool API traffic to show what coding agents send | 813 | <https://github.com/jmuncor/tokentap> |
| HTTP Toolkit | Desktop app for intercepting and debugging HTTP(S) traffic | 736 | <https://github.com/httptoolkit/httptoolkit-desktop> |
| USB Sniffer Lite | Simple USB sniffer based on the Raspberry Pi RP2040 | 701 | <https://github.com/ataradov/usb-sniffer-lite> |
| esp32_bluetooth_classic_sniffer | Active Bluetooth BR/EDR sniffer and injector on ESP32 | 611 | <https://github.com/Matheus-Garbelini/esp32_bluetooth_classic_sniffer> |
| httptoolkit-server | Backend of HTTP Toolkit HTTP(S) interception and debugging tool | 567 | <https://github.com/httptoolkit/httptoolkit-server> |
| USBProxy-legacy | Proxy for USB devices using libUSB and gadgetFS to sniff and modify traffic | 471 | <https://github.com/usb-tools/USBProxy-legacy> |
| frida-flutterproxy | Frida script to proxy Flutter app traffic through Burp | 361 | <https://github.com/hackcatml/frida-flutterproxy> |
| usbrply | Converts USB pcaps into Python/C replay scripts for driver reverse engineering | 339 | <https://github.com/JohnDMcMaster/usbrply> |
| frida-intercept-encrypted-api | Frida tool to intercept encrypted APIs in iOS and Android apps | 332 | <https://github.com/yazgx97/frida-intercept-encrypted-api> |
| xepor | Flask-style web routing framework on mitmproxy for reverse engineers | 215 | <https://github.com/xepor/xepor> |
| bluebox (web-hacker) | Reverse engineers web apps' undocumented APIs from browser traffic | 202 | <https://github.com/VectorlyApp/bluebox> |
| AutomatiQ | Reverse-engineering agent that turns web app traffic into APIs | 172 | <https://github.com/StoneSteel27/AutomatiQ> |
| FlutterTap | Zygisk module redirecting Flutter app traffic to a proxy | 125 | <https://github.com/script-or-script/FlutterTap> |
| mitmproxy-mcp | MCP server wrapping mitmproxy for AI clients | 125 | <https://github.com/snapspecter/mitmproxy-mcp> |
| spectral | Captures app traffic and infers the underlying API | 120 | <https://github.com/spectral-mcp/spectral> |
| Android-Request-Inspector-WebView | Inspect and intercept full HTTP requests from Android WebViews | 117 | <https://github.com/acsbendi/Android-Request-Inspector-WebView> |
| usbsnoop | Live system-wide USB transfer sniffer in eBPF with inline protocol decoding | 87 | <https://github.com/yeet-src/usbsnoop> |
| Android-BLE-Monitor | BLE reverse engineering tool for Android | 79 | <https://github.com/mx0c/Android-BLE-Monitor> |
| BLE-Analyzer-pro-linux-capture | Linux capture tool for the reverse-engineered BLE Analyzer Pro USB sniffer | 77 | <https://github.com/xecaz/BLE-Analyzer-pro-linux-capture> |
| NetPlier | Probabilistic network protocol reverse engineering from message traces | 75 | <https://github.com/yapengye/NetPlier> |
| mitmcloak | mitmproxy addon mirroring real browser TLS/H2/H3 fingerprints upstream | 64 | <https://github.com/sardanioss/mitmcloak> |
| http-breakout-proxy | HTTP proxy for reverse engineering protocol communication | 62 | <https://github.com/jbsouthe/http-breakout-proxy> |
| impersonate-proxy | Local MitM proxy to control TLS (JA3/JA4) and HTTP/2 fingerprints | 40 | <https://github.com/ytkoka/impersonate-proxy> |
| rever-browser | AI-agent browser for web API reverse engineering | 34 | <https://github.com/greekr4/rever-browser> |
| api-reverse-engineer | Chrome extension capturing fetch/XHR calls to reverse engineer site APIs | 32 | <https://github.com/ctala/api-reverse-engineer> |
| fritm | Cross-platform network reverse engineering framework hooking processes with Frida | 26 | <https://github.com/louisabraham/fritm> |
| Wireshark | Network protocol analyzer with dissectors for many reverse-engineered protocols |  | <https://gitlab.com/wireshark/wireshark> |
