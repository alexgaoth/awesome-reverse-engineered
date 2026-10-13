# 🎮 Game Decompilations & Reimplementations

[← All categories](../README.md#-whats-inside) · [Search this category on the website](https://alexgaoth.github.io/awesome-reverse-engineered/#c=game-decompilations-reimplementations) · 2,644 projects

Health: 🟢 pushed in the last year · 🟡 1 to 3 years · 🔴 over 3 years · 🗄️ archived · ⚪ unknown

- [Asset & File-Format Tools](#asset--file-format-tools) (165)
- [Console Emulators](#console-emulators) (30)
- [Engine Reimplementations](#engine-reimplementations) (642)
- [Game Network Protocols & APIs](#game-network-protocols--apis) (88)
- [Launchers & Store Clients](#launchers--store-clients) (45)
- [Matching Decompilations — Arcade](#matching-decompilations--arcade) (3)
- [Matching Decompilations — Atari](#matching-decompilations--atari) (2)
- [Matching Decompilations — Game Boy / GBA / DS](#matching-decompilations--game-boy--gba--ds) (109)
- [Matching Decompilations — GameCube & Wii](#matching-decompilations--gamecube--wii) (116)
- [Matching Decompilations — Mobile](#matching-decompilations--mobile) (24)
- [Matching Decompilations — Nintendo 64](#matching-decompilations--nintendo-64) (89)
- [Matching Decompilations — Other / Multi-platform](#matching-decompilations--other--multi-platform) (180)
- [Matching Decompilations — PC / DOS / Windows](#matching-decompilations--pc--dos--windows) (115)
- [Matching Decompilations — PSP / Vita / PS3](#matching-decompilations--psp--vita--ps3) (2)
- [Matching Decompilations — PlayStation 1](#matching-decompilations--playstation-1) (62)
- [Matching Decompilations — PlayStation 2](#matching-decompilations--playstation-2) (58)
- [Matching Decompilations — SNES / NES](#matching-decompilations--snes--nes) (37)
- [Matching Decompilations — Sega](#matching-decompilations--sega) (4)
- [Matching Decompilations — Switch](#matching-decompilations--switch) (9)
- [Matching Decompilations — Xbox](#matching-decompilations--xbox) (15)
- [Mod Loaders & Script Extenders](#mod-loaders--script-extenders) (98)
- [Open-source Game Clones](#open-source-game-clones) (58)
- [Other](#other) (95)
- [Private Servers](#private-servers) (179)
- [Static Recompilations & PC Ports](#static-recompilations--pc-ports) (419)

## Asset & File-Format Tools

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [PKHeX](https://github.com/kwsch/PKHeX) | Pokemon save file editor built on reverse-engineered save formats | 5,187 | 🟢 | C# |
| [gdsdecomp (GDRE Tools)](https://github.com/GDRETools/gdsdecomp) | Godot reverse-engineering tools: PCK extraction and GDScript decompiler | 4,320 | 🟢 | C++ |
| [noclip.website](https://github.com/magcius/noclip.website) | Web-based viewer for levels from many games via reverse-engineered formats | 4,283 | 🟢 | TypeScript |
| [UABE](https://github.com/SeriousCache/UABE) | Unity Asset Bundle Extractor (archived) | 4,135 | 🗄️ | C++ |
| [repkg](https://github.com/notscuffed/repkg) | Wallpaper Engine PKG extractor and TEX-to-image converter | 3,786 | 🟡 | C# |
| [GARbro](https://github.com/morkt/GARbro) | Resource browser and extractor for visual novel archive formats | 3,329 | 🟡 | C# |
| [uTinyRipper](https://github.com/mafaca/UtinyRipper) | GUI and library to extract Unity serialized and bundle assets | 3,103 | 🔴 | C# |
| [UE Viewer (UModel)](https://github.com/gildor2/UEViewer) | Viewer and exporter for Unreal Engine 1-4 assets | 2,948 | 🟡 | C++ |
| [DisUnity](https://github.com/ata4/disunity) | Experimental toolset for Unity asset and bundle files (archived) | 2,698 | 🗄️ | Java |
| [Source 2 Viewer](https://github.com/ValveResourceFormat/ValveResourceFormat) | Browse VPKs and view, extract and decompile Source 2 assets | 2,497 | 🟢 | C# |
| [vgmstream](https://github.com/vgmstream/vgmstream) | Library for playback of hundreds of streamed video game audio formats | 2,287 | 🟢 | C |
| [UndertaleModTool](https://github.com/UnderminersTeam/UndertaleModTool) | Modding, decompiling and unpacking tool for GameMaker games such as Undertale | 2,078 | 🟢 | C# |
| [KrkrExtract](https://github.com/xmoezzz/KrkrExtract) | Extracts and packs Kirikiri (krkr2/krkrz) XP3 archives | 1,426 | 🗄️ | C++ |
| [unrpyc](https://github.com/CensoredUsername/unrpyc) | Ren'Py compiled script (.rpyc) decompiler | 1,265 | 🟢 | Ren'Py |
| [NHSE](https://github.com/kwsch/NHSE) | Animal Crossing: New Horizons save editor | 1,252 | 🟢 | C# |
| [Switch Toolbox](https://github.com/KillzXGaming/Switch-Toolbox) | Tool to edit many Nintendo game file formats | 1,215 | 🟢 | C# |
| [WolvenKit](https://github.com/WolvenKit/WolvenKit) | Mod editor/creator for REDengine games (Cyberpunk 2077, Witcher 3) | 1,211 | 🟢 | C# |
| [extract-xiso](https://github.com/XboxDev/extract-xiso) | Xbox ISO creation and extraction utility | 1,206 | 🟢 | C |
| [UAssetGUI](https://github.com/atenfyr/UAssetGUI) | Tool for low-level examination and editing of Unreal Engine assets | 1,076 | 🟢 | C# |
| [demoinfocs-golang](https://github.com/markus-wa/demoinfocs-golang) | Counter-Strike 2 and CS:GO demo parser for Go | 1,066 | 🟢 | Go |
| [SourceIO](https://github.com/REDxEYE/SourceIO) | Blender addon importing Source engine textures, models and maps | 978 | 🟢 | Python |
| [LSLib](https://github.com/Norbyte/lslib) | Tools for Larian Studios game formats (Divinity: Original Sin, Baldur's Gate 3) | 947 | 🟢 | C# |
| [xEdit](https://github.com/TES5Edit/TES5Edit) | Module editor and conflict detector for Bethesda games | 905 | 🟢 | Pascal |
| [BSPSource](https://github.com/ata4/bspsrc) | Source engine map decompiler (BSP to VMF) | 873 | 🟢 | Java |
| [Crowbar](https://github.com/ZeqMacaw/Crowbar) | GoldSource and Source engine modding tool: model decompiler and compiler front-end | 839 | 🟢 | Visual Basic .NET |
| [PalworldSaveTools](https://github.com/deafdudecomputers/PalworldSaveTools) | Toolkit to fix, transfer and edit Palworld save files | 821 | 🟢 | Python |
| [Wwise-Unpacker](https://github.com/Vextil/Wwise-Unpacker) | Unpacks Wwise .pck/.bnk audio into playable files | 801 | 🟢 | Batchfile |
| [Frosty Toolsuite](https://github.com/CadeEvs/FrostyToolsuite) | Modding tools for Frostbite engine games | 778 | 🟡 | C# |
| [clarity](https://github.com/skadistats/clarity) | Fast replay parser for Dota 2, CS:GO, CS2 and Deadlock in Java | 770 | 🟢 | Java |
| [unrpa](https://github.com/Lattyware/unrpa) | Extracts files from the Ren'Py RPA archive format | 766 | 🔴 | Python |
| [VPKEdit](https://github.com/craftablescience/VPKEdit) | CLI/GUI tool to create, read and write VPK and other pack formats | 766 | 🟢 | C++ |
| [CodeWalker](https://github.com/dexyfex/CodeWalker) | Interactive 3D map and asset editor for GTA V files | 760 | 🟡 | C# |
| [UnityPack](https://github.com/HearthSim/UnityPack) | Python deserialization library for Unity3D asset bundles | 752 | 🔴 | Python |
| [Smithbox](https://github.com/vawser/Smithbox) | Modding tool for Elden Ring, Sekiro, Dark Souls and Armored Core VI | 735 | 🟢 | C# |
| [demoparser](https://github.com/LaihoE/demoparser) | Counter-Strike 2 replay parser for Python and JavaScript | 732 | 🟢 | Rust |
| [AssetsTools.NET](https://github.com/nesrak1/AssetsTools.NET) | Library to read and write Unity assets and bundle files | 692 | 🟢 | C# |
| [manta](https://github.com/dotabuff/manta) | Dota 2 replay parser in Go | 692 | 🟢 | Go |
| [DSMapStudio](https://github.com/soulsmods/DSMapStudio) | Map and level editor for Demon's Souls, Dark Souls, Bloodborne, Sekiro and Elden Ring | 675 | 🟡 | C# |
| [Obsidian](https://github.com/Crauzer/Obsidian) | WAD archive editor for League of Legends | 668 | 🟢 | TypeScript |
| [StormLib](https://github.com/ladislav-zezula/StormLib) | Library for reading and writing Blizzard MPQ archives | 655 | 🟢 | C |
| [NifSkope](https://github.com/niftools/nifskope) | Viewer and editor for NetImmerse/Gamebryo NIF files | 638 | 🟡 | C++ |
| [rpatool](https://github.com/shizmob/rpatool) | Tool to work with Ren'Py RPA archives | 632 | 🗄️ | Python |
| [OWLib / DataTool](https://github.com/overtools/OWLib) | Overwatch game data extraction library and tools | 612 | 🟢 | C# |
| [jPSXdec](https://github.com/m35/jpsxdec) | Cross-platform PlayStation 1 audio and video converter | 607 | 🟢 | Java |
| [DS Anim Studio](https://github.com/Meowmaritus/DSAnimStudio) | Dark Souls TAE animation event editor | 585 | 🟢 | C# |
| [repak](https://github.com/trumank/repak) | Unreal Engine .pak archive library and CLI in Rust | 582 | 🟢 | Rust |
| [io_import_psk_psa](https://github.com/Befzz/blender3d_import_psk_psa) | Blender addon to import Unreal PSK/PSA meshes, skeletons and animations | 566 | 🟡 | Python |
| [wow.export](https://github.com/Kruithne/wow.export) | Export toolkit for World of Warcraft models, textures and maps | 566 | 🟢 | JavaScript |
| [u4pak](https://github.com/panzi/u4pak) | Unpack, pack and mount Unreal Engine 4 .pak archives | 564 | 🔴 | Python |
| [Godot PCK Explorer](https://github.com/DmitriySalnikov/GodotPCKExplorer) | Explorer, extractor and packer for Godot .pck files | 556 | 🟢 | C# |
| [ninfs](https://github.com/ihaveamac/ninfs) | FUSE filesystem for Nintendo console file formats (3DS, Wii U, Switch) | 544 | 🟢 | Python |
| [NSTool](https://github.com/jakcron/nstool) | General-purpose read/extract tool for Nintendo Switch file formats | 542 | 🟡 | C++ |
| [RPFM](https://github.com/Frodo45127/rpfm) | Rusted PackFile Manager for Total War game PackFiles | 521 | 🟢 | Rust |
| [redscript](https://github.com/jac3km4/redscript) | Compiler/decompiler toolkit for Cyberpunk 2077's redscript | 520 | 🟢 | Rust |
| [UAssetAPI](https://github.com/atenfyr/UAssetAPI) | Low-level .NET library for reading and writing Unreal Engine assets | 509 | 🟢 | C# |
| [CascLib](https://github.com/ladislav-zezula/CascLib) | Library for reading Blizzard CASC storages | 497 | 🟢 | C++ |
| [demofile](https://github.com/saul/demofile) | Node.js parser for CS:GO demo files | 495 | 🗄️ | JavaScript |
| [QuickBMS](https://github.com/LittleBigBug/QuickBMS) | GitHub mirror of QuickBMS game archive extractor | 494 | 🟡 | C |
| [pkNX](https://github.com/kwsch/pkNX) | Pokemon (Nintendo Switch) ROM editor and randomizer | 453 | 🟢 | C# |
| [OpenKH](https://github.com/OpenKH/OpenKh) | Kingdom Hearts libraries, tools, game engine and format documentation | 452 | 🟢 | C# |
| [Kuriimu2](https://github.com/FanTranslatorsInternational/Kuriimu2) | Fan translation project manager and game format toolkit | 443 | 🟢 | C# |
| [Blender Niftools Addon](https://github.com/niftools/blender_niftools_addon) | Blender import/export of NetImmerse/Gamebryo NIF files | 437 | 🟡 | Python |
| [FFXIV TexTools](https://github.com/TexTools/FFXIV_TexTools_UI) | Texture and model modding tool for Final Fantasy XIV | 433 | 🟢 | C# |
| [VNTranslationTools](https://github.com/arcusmaximus/VNTranslationTools) | Text extraction and reinsertion tools for many visual novel engines | 424 | 🗄️ | C# |
| [3dstool](https://github.com/dnasdw/3dstool) | All-in-one tool for extracting and creating 3DS ROM formats | 414 | 🟢 | C |
| [REE.PAK.Tool](https://github.com/Ekey/REE.PAK.Tool) | Extract and repack PAK archives from RE Engine games | 413 | 🟢 | C# |
| [ww2ogg](https://github.com/hcs64/ww2ogg) | Converts Wwise RIFF/RIFX Vorbis to standard Ogg Vorbis | 401 | 🟡 | C++ |
| [SaintCoinach](https://github.com/xivapi/SaintCoinach) | .NET library for extracting Final Fantasy XIV game assets and data | 385 | 🟢 | C# |
| [Kuriimu](https://github.com/IcySon55/Kuriimu) | General purpose game file and translation toolkit for fan translators | 374 | 🔴 | C# |
| [wwiser](https://github.com/bnnm/wwiser) | Audiokinetic Wwise .bnk explorer and audio simulator | 373 | 🟢 | Python |
| [LibOrbisPkg](https://github.com/maxton/LibOrbisPkg) | Library and tools for PS4 PKG, SFO and PFS formats | 362 | 🟡 | C# |
| [LibGGPK3](https://github.com/aianlinb/LibGGPK3) | Library for Path of Exile Content.ggpk and bundle files | 342 | 🟢 | C# |
| [WoWDBDefs](https://github.com/wowdev/WoWDBDefs) | Client database (DB2) definitions for World of Warcraft | 326 | 🟢 | C# |
| [demoinfo](https://github.com/StatsHelix/demoinfo) | C# library to analyze CS:GO demos | 320 | 🗄️ | C# |
| [SC2k-docs](https://github.com/OpenCity2k/SC2k-docs) | Documentation of SimCity 2000 internals and file formats | 288 | 🟡 |  |
| [Assembly](https://github.com/XboxChaos/Assembly) | Multi-generation Blam engine (Halo) map research and editing tool | 268 | 🟢 | C# |
| [Decima Workshop](https://github.com/ShadelessFox/decima-workshop) | Asset viewer and modding tool for Decima engine games | 265 | 🟢 | Java |
| [VGAudio](https://github.com/Thealexbarney/VGAudio) | Library for encoding and decoding video game audio formats (ADX, HCA, DSP, etc.) | 265 | 🔴 | C# |
| [CriPakTools](https://github.com/esperknight/CriPakTools) | List, extract and update CRIWARE CPK archives | 257 | 🔴 | C# |
| [NMSE](https://github.com/vectorcmdr/NMSE) | Open source save editor for No Man's Sky | 252 | 🟢 | C# |
| [Sims4Tools](https://github.com/s4ptacle/Sims4Tools) | s4pe package editor and tools for The Sims 4 formats | 251 | 🟡 | C# |
| [retoc](https://github.com/trumank/retoc) | Tool for packing and unpacking Unreal Engine IoStore (.utoc/.ucas) containers | 243 | 🟢 | Rust |
| [aoc-mgz](https://github.com/happyleavesaoc/aoc-mgz) | Age of Empires II recorded game parser in Python | 234 | 🟢 | Python |
| [NebulaFD](https://github.com/AITYunivers/NebulaFD) | Decompiler for Clickteam Fusion games | 225 | 🟢 | C# |
| [RE-Mesh-Editor](https://github.com/NSACloud/RE-Mesh-Editor) | Blender addon to import/export RE Engine mesh and mdf2 files | 217 | 🗄️ | Python |
| [Tools](https://github.com/bartlomiejduda/Tools) | Tools to extract and modify files from many games | 217 | 🟢 | Python |
| [vdf](https://github.com/ValvePython/vdf) | Python package for Valve's text and binary KeyValue (VDF) format | 214 | 🟡 | Python |
| [MeltyTool](https://github.com/MeltyPlayer/MeltyTool) | Multitool to view and extract assets from N64, GameCube, 3DS and PC games | 213 | 🟢 | GLSL |
| [wow.tools.local](https://github.com/Marlamin/wow.tools.local) | Locally runnable version of wow.tools for browsing WoW data | 207 | 🟢 | C# |
| [Yabber](https://github.com/JKAnderson/Yabber) | Unpacker/repacker for FromSoftware container formats | 206 | 🗄️ | C# |
| [GM8Decompiler](https://github.com/OpenGMK/GM8Decompiler) | Decompiler for GameMaker 8.x executables | 201 | 🟡 |  |
| [sm64tools](https://github.com/queueRAM/sm64tools) | Collection of tools for Super Mario 64 ROM hacking | 199 | 🟢 | C |
| [SoulsFormats](https://github.com/JKAnderson/SoulsFormats) | .NET library for reading and writing FromSoftware file formats | 197 | 🗄️ | C# |
| [ValveKeyValue](https://github.com/ValveResourceFormat/ValveKeyValue) | .NET library for Valve's KeyValues text and binary formats | 193 | 🟢 | C# |
| [NDSFactory](https://github.com/Luca1991/NDSFactory) | Unpack and repack Nintendo DS ROMs | 192 | 🟢 | C++ |
| [soulstruct-blender](https://github.com/Grimrukh/soulstruct-blender) | Blender plugins for FromSoftware game formats via soulstruct | 189 | 🟢 | Python |
| [PDTools](https://github.com/Nenkai/PDTools) | Tools and libraries for Gran Turismo (Polyphony Digital) file formats | 182 | 🟢 | C# |
| [xvdtool](https://github.com/emoose/xvdtool) | Command-line tool for manipulating Xbox One XVD and XVC files | 179 | 🟢 | C# |
| [Mutagen](https://github.com/Mutagen-Modding/Mutagen) | .NET library for analyzing and creating Bethesda plugin files | 176 | 🟢 | C# |
| [Charm](https://github.com/MontagueM/Charm) | Destiny 2 reverse engineering tool for extracting game files | 175 | 🟢 | C# |
| [GCFT](https://github.com/LagoLunatic/GCFT) | GameCube File Tools GUI for common GameCube game formats | 174 | 🟢 | Python |
| [klo-gba.js](https://github.com/macabeus/klo-gba.js) | Reverse engineering tool and level editor for Klonoa GBA | 166 | 🔴 | JavaScript |
| [rust-u4pak](https://github.com/panzi/rust-u4pak) | Rust tool to unpack, pack and mount Unreal Engine 4 .pak archives | 165 | 🔴 | Rust |
| [d2s](https://github.com/nokka/d2s) | Diablo II save file binary parser in Go | 163 | 🔴 | Go |
| [DSLuaDecompiler](https://github.com/katalash/DSLuaDecompiler) | Lua/HavokScript decompiler for Dark Souls, Bloodborne and Sekiro scripts | 163 | 🟡 | C# |
| [MafiaToolkit](https://github.com/Greavesy1899/MafiaToolkit) | Open source toolkit for Mafia II, III and Definitive Edition files | 157 | 🟢 | C# |
| [UnrealLocres](https://github.com/akintos/UnrealLocres) | Reads and writes Unreal Engine .locres localization files | 157 | 🔴 | C# |
| [GBFRDataTools](https://github.com/Nenkai/GBFRDataTools) | Data tools for Granblue Fantasy: Relink archives and formats | 156 | 🟢 | C# |
| [Legendary Explorer](https://github.com/ME3Tweaks/LegendaryExplorer) | Editor toolset for Mass Effect Trilogy and Legendary Edition packages | 156 | 🟢 | C# |
| [CDTB](https://github.com/CommunityDragon/CDTB) | CommunityDragon toolbox for extracting League of Legends client files | 155 | 🟢 | Python |
| [Cyberpunk-Blender-add-on](https://github.com/WolvenKit/Cyberpunk-Blender-add-on) | Blender add-on for Cyberpunk 2077 asset formats | 154 | 🟢 | Python |
| [Smash Forge](https://github.com/jam1garner/Smash-Forge) | Open-source editor for Smash 4 file types | 152 | 🟢 | C# |
| [boxcars](https://github.com/nickbabcock/boxcars) | Rocket League replay parser in Rust | 151 | 🟢 | Rust |
| [Reverence](https://github.com/ntt/reverence) | Python library for EVE Online cache and bulkdata files | 151 | 🔴 | Python |
| [Ruri.ShaderDecompiler](https://github.com/ShiyumeMeguri/Ruri.ShaderDecompiler) | Unity shader decompiler | 148 | 🟢 | C# |
| [MidiConverters](https://github.com/ValleyBell/MidiConverters) | Tools converting game music data into MIDI files | 146 | 🟢 | C |
| [liblcf](https://github.com/EasyRPG/liblcf) | Library to read and write RPG Maker 2000/2003 data formats | 144 | 🟢 | C++ |
| [sourcepp](https://github.com/craftablescience/sourcepp) | C++ parsers for Source engine and related formats (VPK, VTF, MDL, BSP) | 141 | 🟢 | C++ |
| [FortniteReplayDecompressor](https://github.com/Shiqan/FortniteReplayDecompressor) | Reads Fortnite replay files | 139 | 🟢 | C# |
| [d2s-format](https://github.com/krisives/d2s-format) | Diablo II save file format documentation | 136 | 🟡 |  |
| [StarBreaker](https://github.com/diogotr7/StarBreaker) | Star Citizen game file reverse engineering toolkit (P4k, DCB) | 136 | 🟢 | Rust |
| [Lumina](https://github.com/NotAdam/Lumina) | Framework for reading Final Fantasy XIV game data | 133 | 🟢 | C# |
| [vstools](https://github.com/morris/vstools) | Toolset for Vagrant Story file formats in JavaScript | 132 | 🔴 | JavaScript |
| [RocketLeagueReplayParser](https://github.com/jjbott/RocketLeagueReplayParser) | Rocket League replay parser in C# | 129 | 🟢 | C# |
| [mhrice](https://github.com/wwylele/mhrice) | Monster Hunter Rise data extraction and information website | 127 | 🟢 | Rust |
| [OpenMF-Archived](https://github.com/MafiaHub/OpenMF-Archived) | Format utilities and parsers for Mafia: The City of Lost Heaven | 127 | 🗄️ | C++ |
| [CommunityDragon Docs](https://github.com/CommunityDragon/Docs) | Documentation of League of Legends file formats and data | 124 | 🟡 |  |
| [LeagueToolkit](https://github.com/LeagueToolkit/LeagueToolkit) | Library for parsing and editing League of Legends assets | 124 | 🟢 | C# |
| [kismet-analyzer](https://github.com/trumank/kismet-analyzer) | Unreal Engine Blueprint/Kismet script reverse engineering and modding utility | 123 | 🟢 | C# |
| [HedgeLib](https://github.com/Radfordhound/HedgeLib) | C++ library and tools for Sonic the Hedgehog game formats | 121 | 🟢 | C++ |
| [gbx-net](https://github.com/BigBang1112/gbx-net) | Library for Gbx files from Nadeo games like Trackmania | 120 | 🟢 | C# |
| [GTA-V-Script-Decompiler](https://github.com/njames93/GTA-V-Script-Decompiler) | Decompiles GTA V script resources (xsc, csc, ysc) | 118 | 🔴 | C# |
| [ForzaTech-extraction-tools](https://github.com/Doliman100/ForzaTech-extraction-tools) | Reverse engineered .carbin and .modelbin formats from Forza games | 114 | 🟢 | Python |
| [Atlus Script Tools](https://github.com/tge-was-taken/Atlus-Script-Tools) | Compiler/decompiler for Atlus flowscript and message script formats | 106 | 🟢 | C# |
| [pfs_upk](https://github.com/nextgal/pfs_upk) | Artemis engine PFS archive packer and unpacker | 104 | 🔴 | C++ |
| [screp](https://github.com/icza/screp) | StarCraft: Brood War replay parser in Go | 104 | 🟢 | Go |
| [alkahest](https://github.com/cohaereo/alkahest) | Destiny 2 asset viewer with accurate rendering recreation | 96 | 🟢 | Rust |
| [vgm_ripping](https://github.com/hcs64/vgm_ripping) | Tools for ripping video game music formats | 95 | 🔴 | C |
| [Amicitia](https://github.com/tge-was-taken/Amicitia) | Editor for file formats used in Atlus' Persona games | 92 | 🟡 | C# |
| [PS1-Argonaut-Reverse](https://github.com/OverSurge/PS1-Argonaut-Reverse) | Reverse engineering of Argonaut PS1 game formats (Harry Potter, Croc 2) | 88 | 🟡 | Python |
| [runescape-cache-tools](https://github.com/villermen/runescape-cache-tools) | .NET library and CLI for the RuneScape cache | 85 | 🔴 | C# |
| [SporeModder FX](https://github.com/Spore-Community/SporeModder-FX) | Modding tool for Spore package and data formats | 85 | 🟢 | Java |
| [Makou Reactor](https://github.com/myst6re/makoureactor) | Final Fantasy VII field archive editor | 82 | 🟢 | C++ |
| [xbox-reversing](https://github.com/emoose/xbox-reversing) | Information and parsers for under-documented Xbox 360 structures and file formats | 81 | 🟡 | Python |
| [dat-schema](https://github.com/poe-tool-dev/dat-schema) | Community schema for Path of Exile .dat data files | 78 | 🟢 | TypeScript |
| [RPKG Tool](https://github.com/glacier-modding/RPKG-Tool) | Extracts and repacks Glacier 2 engine RPKG archives (Hitman) | 78 | 🟢 | C++ |
| [HSDLib](https://github.com/Ploaj/HSDLib) | Library for HAL Sysdolphin (HSD) DAT files used in Melee and others | 76 | 🟢 | C# |
| [w3gjs](https://github.com/PBug90/w3gjs) | Warcraft III replay parser in JavaScript | 73 | 🟢 | TypeScript |
| [Alpha](https://github.com/NotNite/Alpha) | Final Fantasy XIV toolkit for modding and datamining | 72 | 🟢 | C# |
| [dungeon-siege-re](https://github.com/glampert/dungeon-siege-re) | Reverse engineering of Dungeon Siege game asset formats | 72 | 🟢 | C++ |
| [NeoXResearch](https://github.com/ZhangFengze/NeoXResearch) | Reverse engineering of NetEase's NeoX game engine | 70 | 🔴 | Python |
| [HZDCoreEditor](https://github.com/Nukem9/HZDCoreEditor) | Tools for editing Decima engine files (Horizon Zero Dawn) | 69 | 🔴 | C# |
| [NewWorldUnpacker](https://github.com/MontagueM/NewWorldUnpacker) | .pak unpacker for Amazon's New World | 66 | 🟡 | Python |
| [IG_tools](https://github.com/lennylxx/IG_tools) | Tools to process Innocent Grey and Noesis game files | 65 | 🟢 | C++ |
| [bayonetta_tools](https://github.com/Kerilk/bayonetta_tools) | Tools for PlatinumGames formats (Bayonetta, Nier Automata) | 56 | 🟢 | Ruby |
| [Deling](https://github.com/myst6re/deling) | Final Fantasy VIII field and worldmap archive editor | 52 | 🟢 | C++ |
| [oead](https://github.com/zeldamods/oead) | Library for Nintendo EPD file formats (SARC, BYML, AAMP, Yaz0) | 51 | 🟢 | C++ |
| [Fmod5Sharp](https://github.com/SamboyCoding/Fmod5Sharp) | Managed decoder for FMOD 5 sound banks (FSB files) | 48 | 🟢 | C# |
| [StudioSB](https://github.com/Ploaj/StudioSB) | Model application for Super Smash Bros. Ultimate formats | 46 | 🔴 | C# |
| [JFortniteParse](https://github.com/FabianFG/JFortniteParse) | Kotlin/Java library to parse Unreal Engine pak/asset files from Fortnite | 45 | 🟢 | Kotlin |
| [Torch](https://github.com/HarbourMasters/Torch) | N64 ROM asset extractor and converter used by fan PC ports | 38 | 🟢 | C++ |
| [ZenTools](https://github.com/WistfulHopes/ZenTools-UE4) | Tools for extracting Unreal Engine IoStore (Zen) packages | 28 | 🟡 | C++ |
| [TACTSharp](https://github.com/wowdev/TACTSharp) | C# library for Blizzard's TACT/CASC content distribution | 12 | 🟢 | C# |
| [smash-arc](https://github.com/jam1garner/smash-arc) | Library for Super Smash Bros. Ultimate's ARC archive format | 9 | 🟡 | Rust |
| [Cathedral Assets Optimizer](https://github.com/Guekka/Cathedral_Assets_Optimizer) | Optimizes Bethesda game assets (BSA, NIF, DDS) | 0 | 🔴 |  |

## Console Emulators

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [shadPS4](https://github.com/shadps4-emu/shadPS4) | PlayStation 4 emulator for Windows, Linux and macOS | 33,505 | 🟢 | C++ |
| [RPCS3](https://github.com/RPCS3/rpcs3) | PlayStation 3 emulator and debugger | 20,050 | 🟢 | C++ |
| [PCSX2](https://github.com/PCSX2/pcsx2) | PlayStation 2 emulator | 15,792 | 🟢 | C++ |
| [Dolphin](https://github.com/dolphin-emu/dolphin) | GameCube and Wii emulator | 15,648 | 🟢 | C++ |
| [DuckStation](https://github.com/stenzek/duckstation) | PlayStation 1 emulator focused on accuracy and speed | 10,832 | 🟢 | C++ |
| [Vita3K](https://github.com/Vita3K/Vita3K) | Experimental PlayStation Vita emulator | 5,825 | 🟢 | C++ |
| [Xenia Canary](https://github.com/xenia-canary/xenia-canary) | Experimental fork of the Xenia Xbox 360 emulator | 2,635 | 🟢 | C++ |
| [Panda3DS](https://github.com/wheremyfoodat/Panda3DS) | HLE 3DS emulator | 1,402 | 🟢 | C++ |
| [metroboy](https://github.com/aappleby/metroboy) | Gate-level simulators and tools for the original Game Boy | 1,173 | 🟡 | C++ |
| [pcsx-redux](https://github.com/grumpycoders/pcsx-redux) | PlayStation 1 emulator and toolset for development and reverse engineering | 1,014 | 🟢 | C++ |
| [cen64](https://github.com/n64dev/cen64) | Cycle-accurate Nintendo 64 emulator | 842 | 🟢 | C |
| [obliteration](https://github.com/obhq/obliteration) | Experimental open-source PlayStation 4 kernel reimplementation and emulator | 819 | 🟢 | Rust |
| [Supermodel](https://github.com/trzy/Supermodel) | Sega Model 3 arcade emulator | 662 | 🟢 | C++ |
| [mikage-dev](https://github.com/mikage-emu/mikage-dev) | Mikage Developer Edition | 418 | 🟡 | C++ |
| [Nuked-MD-FPGA](https://github.com/nukeykt/Nuked-MD-FPGA) | Mega Drive/Genesis Verilog core derived from die-level reverse engineering | 318 | 🟡 | Verilog |
| [Xenon](https://github.com/xenon-emu/xenon) | Low-level Xbox 360 emulator for researching Xenon hardware | 311 | 🟢 | C++ |
| [breaks](https://github.com/emu-russia/breaks) | Transistor-level reverse engineering of NES/Famicom chips | 218 | 🟢 | Verilog |
| [pureikyubu](https://github.com/emu-russia/pureikyubu) | Nintendo GameCube emulator | 197 | 🟢 | C++ |
| [Nuked-MD](https://github.com/nukeykt/Nuked-MD) | Cycle-accurate Mega Drive emulator from die-level reverse engineering | 185 | 🟢 | C |
| [psxrev](https://github.com/emu-russia/psxrev) | Sony PlayStation PCB and chip reverse engineering | 160 | 🟡 | C# |
| [PPU-LITE](https://github.com/andkorzh/PPU-LITE) | Clock-accurate FPGA replacement for the NES PPU from reverse engineering | 119 | 🟢 | Verilog |
| [Cxbx-Reloaded](https://github.com/Cxbx-Reloaded/Cxbx-Reloaded) | Original Xbox emulator via HLE of reverse engineered XDK libraries | 69 | 🟢 | C++ |
| [SEGAChips](https://github.com/emu-russia/SEGAChips) | Reverse engineering of SEGA chips | 69 | 🟢 | Verilog |
| [cor64](https://github.com/bdragoncore/cor64) | N64 Emulator written in C# | 54 | 🟡 | C# |
| [dmgcpu](https://github.com/emu-russia/dmgcpu) | Reverse engineering of the Game Boy DMG CPU from the die | 48 | 🟢 | Verilog |
| [SNES_S-CPU_Schematics](https://github.com/rgalland/SNES_S-CPU_Schematics) | Reverse engineering of the SNES CPU from die shots | 40 | 🟡 | KiCad Schematic |
| [biostation](https://github.com/Ravenslofty/biostation) | Clean-room PlayStation 2 BIOS | 26 | 🔴 | Assembly |
| [zakuro](https://github.com/fearkov/zakuro) | A Nintendo 3DS emulator in Rust, using AOT recompilation | 20 | 🟢 | Rust |
| [Model2EmuEx](https://github.com/octavioCuatrochio/Model2EmuEx) | Decompiled Sega Model 2 emulator modified to run on Linux and Android | 16 | 🟢 | C |
| [Snaggletooth](https://github.com/etroimcasso/Snaggletooth) | An embeddable, clean-room MIT-licensed SNES (5A22 + SPC700) virtual machine, with a source-recovery and decompilation... | 5 | 🟢 | C++ |

## Engine Reimplementations

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [OpenRA](https://github.com/OpenRA/OpenRA) | RTS engine reimplementing early Westwood games such as C&C Red Alert | 17,553 | 🟢 | C# |
| [OpenRCT2](https://github.com/OpenRCT2/OpenRCT2) | Open-source reimplementation of RollerCoaster Tycoon 2 | 16,423 | 🟢 | C++ |
| [openage](https://github.com/SFTtech/openage) | Free clone of the Genie engine used by Age of Empires II | 14,499 | 🟢 | Python |
| [OpenDiablo2](https://github.com/OpenDiablo2/OpenDiablo2) | Open-source re-implementation of Diablo 2 | 11,103 | 🗄️ | Go |
| [DevilutionX](https://github.com/diasurgical/DevilutionX) | Diablo and Hellfire port for modern systems built on the Devilution reverse engineering | 9,831 | 🟢 | C++ |
| [OpenTTD](https://github.com/OpenTTD/OpenTTD) | Open-source transport simulation game based on Transport Tycoon Deluxe | 8,364 | 🟢 | C++ |
| [OpenMW](https://github.com/OpenMW/openmw) | Open-source engine reimplementation for The Elder Scrolls III: Morrowind | 6,621 | 🟢 | C++ |
| [VCMI](https://github.com/vcmi/vcmi) | Open-source engine for Heroes of Might and Magic III | 5,940 | 🟢 | C++ |
| [RuneLite](https://github.com/runelite/runelite) | Open source Old School RuneScape client | 5,485 | 🟢 | Java |
| [OpenSC2K](https://github.com/nicholas-ochoa/OpenSC2K) | OpenSC2K - Open Source remake of Sim City 2000 using rust and godot. Available for macOS, Windows and Linux | 5,292 | 🟢 | Rust |
| [OpenLara](https://github.com/XProger/OpenLara) | Classic Tomb Raider open-source engine | 5,118 | 🟢 | C |
| [zelda3](https://github.com/snesrev/zelda3) | C reimplementation of Zelda: A Link to the Past from reverse-engineered SNES code | 4,847 | 🟢 | C |
| [CorsixTH](https://github.com/CorsixTH/CorsixTH) | Open-source clone of Theme Hospital | 4,592 | 🟢 | Lua |
| [PythonPlantsVsZombies](https://github.com/marblexu/PythonPlantsVsZombies) | a simple PlantsVsZombies game | 3,769 | 🟡 | Python |
| [OpenXRay](https://github.com/OpenXRay/xray-16) | Improved version of the X-Ray Engine, the game engine used in the world-famous S.T.A.L.K.E.R. game series by GSC Game... | 3,578 | 🟢 | C++ |
| [OpenGOAL (jak-project)](https://github.com/open-goal/jak-project) | Reimplements the GOAL language/runtime to port Jak and Daxter 1-3 to PC | 3,565 | 🟢 | Common Lisp |
| [Daggerfall Unity](https://github.com/Interkarma/daggerfall-unity) | Recreation of The Elder Scrolls II: Daggerfall in Unity | 3,519 | 🟢 | C# |
| [fheroes2](https://github.com/ihhub/fheroes2) | Recreation of the Heroes of Might and Magic II game engine | 3,503 | 🟢 | C++ |
| [Julius](https://github.com/bvschaik/julius) | Open-source reimplementation of Caesar III with the original game logic | 3,394 | 🟢 | C |
| [Super Mario Bros Remastered](https://github.com/JHDev2006/Super-Mario-Bros.-Remastered-Public) | A Remake / Celebration of the original 'Super Mario Bros.' games. Features new levels, custom modes, new characters,... | 3,201 | 🟢 | GDScript |
| [WipEout (wipeout-rewrite)](https://github.com/phoboslab/wipeout-rewrite) | Reverse-engineered reimplementation / port of WipEout (wipeout-rewrite) | 2,975 | 🟢 | C |
| [kys-cpp](https://github.com/scarsty/kys-cpp) | 《金庸群侠传》c++复刻版，已完工 | 2,970 | 🟢 | C++ |
| [Fallout Community Edition](https://github.com/alexbatalov/fallout1-ce) | Fully working reimplementation of Fallout 1 engine | 2,944 | 🟡 | C++ |
| [ScummVM](https://github.com/scummvm/scummvm) | Reimplements engines of classic point-and-click adventure games | 2,843 | 🟢 | C++ |
| [Xash3D FWGS](https://github.com/FWGS/xash3d-fwgs) | Open-source reimplementation of the GoldSrc engine that runs Half-Life | 2,843 | 🟢 | C |
| [ioquake3](https://github.com/ioquake/ioq3) | Community continuation of id's Quake III Arena engine | 2,841 | 🟢 | C |
| [SanAndreasUnity](https://github.com/in0finite/SanAndreasUnity) | Open source reimplementation of GTA San Andreas game engine in Unity | 2,643 | 🔴 | C# |
| [Fallout 2 CE](https://github.com/alexbatalov/fallout2-ce) | Fallout 2 engine re-implementation for modern desktop and mobile | 2,454 | 🟡 | C++ |
| [OpenJK](https://github.com/JACoders/OpenJK) | Community-maintained Jedi Academy / Jedi Outcast engine | 2,298 | 🟢 | C++ |
| [OpenRW](https://github.com/rwengine/openrw) | Open-source re-implementation of Rockstar's GTA III | 2,240 | 🟡 | C++ |
| [OpenXcom](https://github.com/OpenXcom/OpenXcom) | Open-source clone of UFO: Enemy Unknown and X-COM: Terror from the Deep | 2,229 | 🟢 | C++ |
| [Freeablo](https://github.com/wheybags/freeablo) | Open-source implementation of the Diablo engine. | 2,171 | 🔴 | C++ |
| [Augustus](https://github.com/Keriew/augustus) | An open source re-implementation of Caesar III | 2,116 | 🟢 | C |
| [ClassiCube](https://github.com/ClassiCube/ClassiCube) | Custom Minecraft Classic-compatible game client in C | 2,073 | 🟢 | C |
| [SDLPAL](https://github.com/sdlpal/sdlpal) | SDL-based reimplementation of the classic Chinese-language RPG known as PAL. | 1,976 | 🟢 | C |
| [OpenLoco](https://github.com/OpenLoco/OpenLoco) | Open-source reimplementation of Chris Sawyer's Locomotion | 1,935 | 🟢 | C++ |
| [Hematite](https://github.com/PistonDevelopers/hematite) | A simple Minecraft written in Rust with the Piston game engine | 1,918 | 🟢 | Rust |
| [OpenDUNE](https://github.com/OpenDUNE/OpenDUNE) | Recreation of the popular game Dune II. | 1,694 | 🟢 | C |
| [Pokémon Polished Crystal](https://github.com/Rangi42/polishedcrystal) | An upgrade to Pokémon Crystal. Brings features and content up to date, and adds some original content. | 1,666 | 🟢 | Assembly |
| [roBrowser](https://github.com/vthibault/roBrowser) | Ragnarok Online client reimplemented for web browsers in JavaScript/WebGL | 1,658 | 🗄️ | JavaScript |
| [Clumsy Bird](https://github.com/ellisonleao/clumsy-bird) | :bird: :video_game: A MelonJS port of the famous Flappy Bird Game | 1,629 | 🗄️ | JavaScript |
| [OpenGothic](https://github.com/Try/OpenGothic) | Open-source reimplementation of Gothic I and II | 1,618 | 🟢 | C++ |
| [Ikemen GO](https://github.com/ikemen-engine/Ikemen-GO) | Open-source reimplementation of the MUGEN fighting game engine | 1,617 | 🟢 | Go |
| [openblack](https://github.com/openblack/openblack) | Open-source reimplementation of Black & White (2001) | 1,577 | 🟢 | C++ |
| [OpenTomb](https://github.com/opentomb/OpenTomb) | Open-source Tomb Raider 1-5 engine remake (archived) | 1,445 | 🗄️ | C++ |
| [OpenTESArena](https://github.com/afritz1/OpenTESArena) | Modern engine reimplementation of The Elder Scrolls: Arena by Bethesda Softworks. | 1,430 | 🟢 | C++ |
| [doukutsu-rs](https://github.com/doukutsu-rs/doukutsu-rs) | Rust reimplementation of the Cave Story engine | 1,309 | 🟢 | Rust |
| [Minosoft](https://github.com/Bixilon/Minosoft) | Open source Minecraft client reimplementation written from scratch | 1,308 | 🟢 | Kotlin |
| [GemRB](https://github.com/gemrb/gemrb) | Portable open-source reimplementation of the Infinity Engine (used by Baldur's Gate, Icewind Dale and more). | 1,256 | 🟢 | C++ |
| [Diablerie](https://github.com/mofr/Diablerie) | Diablo 2 reimplementation on unity | 1,241 | 🔴 | C# |
| [Carmageddon (dethrace)](https://github.com/dethrace-labs/dethrace) | Reverse-engineered reimplementation / port of Carmageddon (dethrace) | 1,216 | 🟢 | C |
| [xoreos](https://github.com/xoreos/xoreos) | Reimplementation of BioWare's Aurora engine (KotOR, NWN, Jade Empire) | 1,182 | 🟢 | C++ |
| [The Force Engine](https://github.com/TheForceEngine/TheForceEngine) | Reimplementation of LucasArts' Jedi engine for Dark Forces and Outlaws | 1,163 | 🟢 | C++ |
| [RA2](https://github.com/OpenRA/ra2) | A Red Alert 2 mod for the OpenRA game engine | 1,138 | 🟢 | C# |
| [SurrealEngine](https://github.com/dpjudas/SurrealEngine) | Open-source reimplementation of Unreal Engine 1 that plays Unreal Tournament 99 | 1,115 | 🟢 | C++ |
| [Riiablo](https://github.com/collinsmith/riiablo) | Diablo II remade using Java and LibGDX | 1,105 | 🟡 | Java |
| [pikachu-volleyball](https://github.com/gorisanson/pikachu-volleyball) | Pikachu Volleyball reimplemented in JavaScript by reverse engineering the original game | 1,088 | 🟢 | JavaScript |
| [OpenHV](https://github.com/OpenHV/OpenHV) | Open-source implementation of Hard Vacuum. | 1,080 | 🟢 | C# |
| [Pal3.Unity](https://github.com/0x7c13/Pal3.Unity) | Unity reimplementation of The Legend of Sword and Fairy 3 and its expansion | 1,055 | 🟢 | C# |
| [Tomb Raider I & II (TRX)](https://github.com/LostArtefacts/TRX) | Reverse-engineered reimplementation / port of Tomb Raider I & II (TRX) | 1,009 | 🟢 | C |
| [RigelEngine](https://github.com/lethal-guitar/RigelEngine) | Modern re-implementation of Duke Nukem II | 1,007 | 🟢 | C++ |
| [RA2Web React](https://github.com/huangkaoya/ts-redalert2) | 红色警戒2源代码 Red Alert2 Source Code | 1,003 | 🟢 | TypeScript |
| [FreeSO](https://github.com/riperiperi/FreeSO) | Reimplementation of The Sims Online, targetted mainly at mobile devices. | 983 | 🟢 | C# |
| [Crispy Doom](https://github.com/fabiangreffrath/crispy-doom) | Crispy Doom is a limit-removing enhanced-resolution Doom source port based on Chocolate Doom. | 957 | 🟢 | C |
| [NEO-RAW](https://github.com/fabiensanglard/Another-World-Bytecode-Interpreter) | "Fabother World" an interpreter for Another World (Out of this world). | 920 | 🟡 | C++ |
| [PICOLOVE](https://github.com/picolove/picolove) | PICO-8 fantasy console reimplementation in LÖVE | 891 | 🟡 | Lua |
| [Falltergeist](https://github.com/falltergeist/falltergeist) | Opensource crossplatform Fallout 2™ game engine writen in C++ and SDL. | 887 | 🔴 | C++ |
| [Raze](https://github.com/ZDoom/Raze) | Build engine port backed by GZDoom tech. Currently supports Duke Nukem 3D, Blood, Shadow Warrior, Redneck Rampage and... | 886 | 🟢 | C++ |
| [Cannonball](https://github.com/djyt/cannonball) | OutRun arcade engine reimplementation | 880 | 🟡 | C++ |
| [OpenEnroth](https://github.com/OpenEnroth/OpenEnroth) | Open reimplementation of the Might and Magic 6/7/8 game engine | 871 | 🟢 | C++ |
| [ReHLDS](https://github.com/rehlds/ReHLDS) | Reverse engineered, enhanced Half-Life Dedicated Server engine | 864 | 🟢 | C++ |
| [OpenNFS](https://github.com/OpenNFS/OpenNFS) | Attempt to recreate the classic Need for Speed Games (1-6). | 845 | 🟢 | C++ |
| [OpenMoHAA](https://github.com/openmoh/openmohaa) | Open re-implementation of Medal of Honor: Allied Assault | 830 | 🟢 | C |
| [librw](https://github.com/aap/librw) | A re-implementation of the RenderWare Graphics engine | 826 | 🟢 | C++ |
| [NBlood](https://github.com/NBlood/NBlood) | Reverse-engineered ports of Build games using EDuke32 engine technology and development principles (NBlood/Rednukem/P... | 809 | 🟢 | C++ |
| [uMario](https://github.com/jakowskidev/uMario_Jakowski) | uMario C++/SDL2 Game by Łykasz Jakowski | 803 | 🔴 | C++ |
| [ReGameDLL_CS](https://github.com/rehlds/ReGameDLL_CS) | Reverse engineered server-side GameDLL for Counter-Strike 1.6 | 799 | 🟢 | C++ |
| [si78c](https://github.com/loadzero/si78c) | Memory-accurate C reimplementation of the Space Invaders arcade ROM | 798 | 🔴 | C |
| [metaforce](https://github.com/AxioDL/metaforce) | A native reimplementation of the Metroid Prime engine | 797 | 🟢 | C++ |
| [PvZ-Portable](https://github.com/wszqkzqk/PvZ-Portable) | Cross-platform reimplementation of Plants vs. Zombies | 796 | 🟢 | C++ |
| [SuperMarioBros-C](https://github.com/MitchellSternke/SuperMarioBros-C) | An attempt to translate the original Super Mario Bros. for the NES to readable C/C++ | 787 | 🔴 | C++ |
| [NFSIISE](https://github.com/zaps166/NFSIISE) | Need For Speed™ II SE - Cross-platform wrapper with 3D acceleration and TCP protocol! | 769 | 🟢 | C |
| [OpenJKDF2](https://github.com/shinyquagsire23/OpenJKDF2) | Cross-platform reimplementation of Star Wars Jedi Knight: Dark Forces II in C | 764 | 🟢 | C |
| [skate-3-rust-engine](https://github.com/SK8-ENGINE/skate-3-rust-engine) | Rust/Bevy skating engine based on Skate 3 reverse engineering research | 737 | 🟢 | Rust |
| [ClassicUO](https://github.com/ClassicUO/ClassicUO) | Open-source reimplementation of the Ultima Online Classic client | 734 | 🟢 | C# |
| [jazz2-native](https://github.com/deathkiller/jazz2-native) | 🎮 · Jazz² Resurrection: Native C++ reimplementation of Jazz Jackrabbit 2 | 714 | 🟢 | C++ |
| [Memoria](https://github.com/Albeoris/Memoria) | Final Fantasy IX tools | 708 | 🟢 | C# |
| [OTClient](https://github.com/edubart/otclient) | Alternative Tibia client for OpenTibia servers in C++ and Lua | 707 | 🟡 | C++ |
| [Thyme](https://github.com/TheAssemblyArmada/Thyme) | Open-source re-implementation of Command & Conquer Generals: Zero Hour | 693 | 🟡 | C++ |
| [Exult](https://github.com/exult/exult) | Engine reimplementation for Ultima VII: The Black Gate and Serpent Isle | 692 | 🟢 | C++ |
| [OpenVIII](https://github.com/MaKiPL/OpenVIII-monogame) | Open source Final Fantasy VIII engine implementation in C# working on Windows and Linux (Android and iOS planned too!... | 673 | 🗄️ | C# |
| [REGoth](https://github.com/REGoth-project/REGoth) | OpenSource-Reimplementation of the zEngine, used by the game "Gothic" | 654 | 🔴 | C++ |
| [Sonic 3 A.I.R.](https://github.com/Eukaryot/sonic3air) | Sonic 3 & Knuckles engine reimplementation (Angel Island Revisited) | 653 | 🟢 | C++ |
| [GLSMAC](https://github.com/afwbkbc/glsmac) | Open-source reimplementation of Sid Meier's Alpha Centauri | 638 | 🟢 | C++ |
| [Portal 64: Still Alive](https://github.com/mwpenny/portal64-still-alive) | A demake of Portal for the Nintendo 64 | 624 | 🟢 | C |
| [Librelancer](https://github.com/Librelancer/Librelancer) | Reimplementation of the 2003 space game Freelancer. | 612 | 🗄️ |  |
| [OpenD2](https://github.com/eezstreet/OpenD2) | A project to open source Diablo 2. | 605 | 🔴 | C |
| [OpenFodder](https://github.com/OpenFodder/openfodder) | Open-source reimplementation of Cannon Fodder | 605 | 🟢 | C++ |
| [OpenSkyscraper](https://github.com/fabianschuiki/OpenSkyscraper) | Open source tower simulation game inspired by SimTower. | 590 | 🔴 | C++ |
| [Jazz² Resurrection](https://github.com/deathkiller/jazz2) | Reimplementation of Jazz Jackrabbit 2. | 575 | 🟢 |  |
| [Warsmash](https://github.com/Retera/WarsmashModEngine) | Warcraft III engine emulation for modding | 575 | 🟢 | Java |
| [OpenTS](https://github.com/OpenTS-Developers/OpenTS) | Open-source, reverse-engineered rebuild of the Command & Conquer: Tiberian Sun engine | 572 | 🟢 | C++ |
| [Carnage3D](https://github.com/codenamecpp/carnage3d) | Reimplementation of Grand Theft Auto 1 | 568 | 🟢 | C++ |
| [sm (Super Metroid)](https://github.com/snesrev/sm) | C reimplementation of Super Metroid from reverse-engineered SNES code | 556 | 🔴 | C |
| [NXEngine-evo](https://github.com/nxengine/nxengine-evo) | Engine rewrite of Cave Story (Doukutsu Monogatari) | 549 | 🟢 | C |
| [The Legend of Dragoon (Severed Chains)](https://github.com/Legend-of-Dragoon-Modding/Severed-Chains) | Reverse-engineered reimplementation / port of The Legend of Dragoon (Severed Chains) | 549 | 🟢 | Java |
| [Ambermoon.net](https://github.com/Pyrdacor/Ambermoon.net) | Ambermoon rewrite in C# | 540 | 🟢 | C# |
| [OTClient (Redemption)](https://github.com/opentibiabr/otclient) | Modern C++20 fork-successor of OTClient for Tibia-compatible servers | 537 | 🟢 | Lua |
| [TOMB5](https://github.com/TOMB5/TOMB5) | Tomb Raider: Chronicles Disassembly translated to C source code. | 520 | 🔴 | C |
| [OpenClaw](https://github.com/pjasicek/OpenClaw) | Reimplementation of the Captain Claw (1997) platformer | 515 | 🔴 | C++ |
| [Akhenaten](https://github.com/dalerank/Akhenaten) | Open-source reimplementation of Pharaoh (Impressions Games) | 512 | 🟢 | C++ |
| [KisakCOD](https://github.com/SwagSoftware/KisakCOD) | Open-source reimplementation of Call of Duty 4 multiplayer | 511 | 🟢 | C++ |
| [REGoth](https://github.com/REGoth-project/REGoth-bs) | An open source reimplementation of zEngine the engine behind Gothic and Gothic II. | 499 | 🔴 | C++ |
| [Simitone](https://github.com/riperiperi/Simitone) | Re-implementation of The Sims 1, based off of FreeSO. | 499 | 🟡 | C# |
| [FreeSpace 2 Source Code Project](https://github.com/scp-fs2open/fs2open.github.com) | Origin Repository for SCP FreeSpace 2 Open | 490 | 🟢 | C++ |
| [Vange-rs](https://github.com/kvark/vange-rs) | Rusty Vangers clone | 488 | 🟢 | Rust |
| [donut](https://github.com/plowteam/donut) | Reimplementation of The Simpsons: Hit & Run in modern C++ and modern OpenGL. | 485 | 🟡 | C++ |
| [Miu2D](https://github.com/luckyyyyy/miu2d) | Miu2D is a 2D RPG game engine built with Rust + TypeScript + React + Canvas, designed for the Web platform. 剑侠情缘2/月影传... | 479 | 🟢 | TypeScript |
| [Nanosaur](https://github.com/jorio/Nanosaur) | Nanosaur source port 🦖 | 474 | 🟢 | C |
| [OpenVic](https://github.com/OpenVicProject/OpenVic) | Main Repo for the OpenVic Project | 473 | 🟢 | GDScript |
| [McOsu](https://github.com/McKay42/McOsu) | Unofficial osu! practice client with VR support | 470 | 🟢 | C++ |
| [OpenLiberty](https://github.com/openfw-game/OpenLiberty) | GTA III reimplementation in the Godot engine loading original assets | 468 | 🟢 | GDScript |
| [Super Mario 64 (DualShock Version)](https://github.com/malucard/sm64-psx) | A very WIP port of https://www.github.com/n64decomp/sm64 for the PlayStation 1 | 464 | 🗄️ | C |
| [cs16-client](https://github.com/Velaron/cs16-client) | Reverse engineered Counter-Strike 1.6 client for the Xash3D engine | 454 | 🟢 | C++ |
| [Alive Reversing](https://github.com/AliveTeam/alive_reversing) | Reimplementation of Oddworld: Abe's Exoddus. | 441 | 🟢 | C++ |
| [Wargus](https://github.com/Wargus/wargus) | Importer and scripts for Warcraft II: Tides of Darkness, the expansion Beyond the Dark Portal, and Aleonas Tales | 441 | 🟢 | C |
| [Chariot](https://github.com/ChariotEngine/Chariot) | Reimplementation of the Age of Empires (1997) engine in Rust | 431 | 🔴 | Rust |
| [OpenTS2](https://github.com/LazyDuchess/OpenTS2) | Open source re-implementation of The Sims 2 in Unity | 431 | 🟢 | C# |
| [cinnamon](https://github.com/Project-Sunshine-Native/cinnamon) | GameMaker GML runner reimplementation in C for 3DS and Wii U | 411 | 🟢 | C |
| [OpenJazz](https://github.com/AlisterT/openjazz) | Engine reimplementation of Jazz Jackrabbit; uses original game data (C++) | 409 | 🟢 | C |
| [ResidualVM](https://github.com/residualvm/residualvm) | Engine reimplementation for 3D adventures like Grim Fandango (archived; merged into ScummVM) | 401 | 🗄️ | C++ |
| [Butterscotch](https://github.com/ButterscotchRunner/Butterscotch) | Open source reimplementation of the GameMaker: Studio runner | 393 | 🟢 | C |
| [Duke Nukem II (Reconstructed)](https://github.com/lethal-guitar/Duke2Reconstructed) | Reverse-engineered reimplementation / port of Duke Nukem II (Reconstructed) | 370 | 🟡 | C |
| [BStone](https://github.com/bibendovsky/bstone) | Unofficial source port for Blake Stone series | 369 | 🟢 | C |
| [PokeSwift](https://github.com/Dimillian/PokeSwift) | Reimplementation of the Pokemon Red/Blue engine in Swift | 363 | 🟢 | Assembly |
| [OpenMW for Android](https://github.com/xyzz/openmw-android) | OpenMW for Android | 362 | 🗄️ | Java |
| [OpenSWE1R](https://github.com/OpenSWE1R/openswe1r) | Open-source reimplementation of Star Wars Episode I: Racer | 350 | 🔴 | C |
| [3SX](https://github.com/crowded-street/3sx) | "The Third of the Third" ported to modern platforms | 349 | 🟢 | C |
| [pikachu-volleyball-p2p-online](https://github.com/gorisanson/pikachu-volleyball-p2p-online) | Peer-to-peer online play for the reverse engineered Pikachu Volleyball | 343 | 🟢 | JavaScript |
| [Tomb Engine](https://github.com/TombEngine/TombEngine) | A new and modern engine for custom Tomb Raider levels incorporating classic features and new enhancements. | 343 | 🟢 | C++ |
| [open-realm](https://github.com/corepunch/open-realm) | Open-source reimplementation of the Warcraft III engine | 342 | 🟢 | C |
| [UnderworldExporter](https://github.com/hankmorgan/UnderworldExporter) | Updated Release 27th Oct 2018 Unity based port of Ultima Underworld I and II. Download under releases | 340 | 🗄️ | C# |
| [Freeserf](https://github.com/freeserf/freeserf) | Settlers 1 (Serf City) clone. | 339 | 🟢 | C++ |
| [FreeSims](https://github.com/francot514/FreeSims) | Open source engine used for The Sims | 330 | 🟢 | C# |
| [UnderworldGodot](https://github.com/hankmorgan/UnderworldGodot) | An engine recreation of Ultima Underworld and Ultima Underworld 2 in the Godot Engine. | 328 | 🟢 | C# |
| [open-ig](https://github.com/akarnokd/open-ig) | Open-source reimplementation of Imperium Galactica | 326 | 🟢 | Java |
| [FreeHL](https://github.com/eukara/freehl) | Clean-room reimplementation of Half-Life and HL: Deathmatch in QuakeC | 322 | 🟢 | QuakeC |
| [Omnispeak](https://github.com/sulix/omnispeak) | Reimplementation of Commander Keen in Goodbye Galaxy. | 316 | 🟢 | C |
| [reone](https://github.com/seedhartha/reone) | Game engine reimplementation for Star Wars: KotOR I and II | 315 | 🟡 | C++ |
| [Abyss Engine](https://github.com/AbyssEngine/AbyssEngine) | Abyss Engine clean-room reimplementation of Diablo 2, written in C. The goal is to recreate the original game engine,... | 310 | 🟡 | C |
| [CroftEngine](https://github.com/stohrendorf/CroftEngine) | An open-source Tomb Raider 1 engine remake | 310 | 🟢 | C++ |
| [open-supaplex](https://github.com/sergiou87/open-supaplex) | Reverse engineered open source port of Supaplex | 304 | 🟢 | C |
| [freecs](https://github.com/eukara/freecs) | Clean-room Counter-Strike 1.5 in QuakeC using the Nuclide SDK | 302 | 🟢 | QuakeC |
| [Theseus](https://github.com/MrMilenko/Theseus) | Reverse-engineered reconstruction of the original Xbox 5960 dashboard | 302 | 🟢 | C++ |
| [MafiaUnity](https://github.com/MafiaHub/MafiaUnity) | 🕹 Open-source Mafia game framework | 294 | 🗄️ | C# |
| [Resident Evil 2 (OpenBiohazard2)](https://github.com/OpenBiohazard2/OpenBiohazard2) | Reverse-engineered reimplementation / port of Resident Evil 2 (OpenBiohazard2) | 292 | 🟢 | Go |
| [lba2remake](https://github.com/LBALab/lba2remake) | A Little Big Adventure 2 / Twinsen's Odyssey reimplementation in JavaScript / Three.js / React | 286 | 🟢 | TypeScript |
| [Wowser](https://github.com/wowserhq/wowser) | World of Warcraft client in the browser using JavaScript and WebGL | 285 | 🔴 | JavaScript |
| [PrinceJS](https://github.com/ultrabolido/PrinceJS) | Prince of Persia reimplementation in HTML5/JavaScript | 282 | 🟡 | JavaScript |
| [Super-Mario-World-Remastered-Public](https://github.com/JHDev2006/Super-Mario-World-Remastered-Public) | A Remake / Remaster of the original Super Mario World, in Godot. Adds new features / improvements! | 280 | 🗄️ | GDScript |
| [Sourcehold](https://github.com/sourcehold/Sourcehold) | Open source re-implementation of Stronghold 1 | 279 | 🟡 | C++ |
| [spearmint](https://github.com/clover-moe/spearmint) | Spearmint — an updated id Tech 3 engine for continuing the classics and creating new games. | 279 | 🟢 | C |
| [Doom64EX](https://github.com/svkaiser/Doom64EX) | Reverse engineered recreation of Doom 64 with modding features | 274 | 🟢 | C++ |
| [The Eternity Engine](https://github.com/team-eternity/eternity) | The Eternity Engine | 271 | 🟢 | C++ |
| [DGEngine](https://github.com/dgcor/DGEngine) | Implementation of the Diablo game engine. | 270 | 🟡 | C++ |
| [Heretic2R](https://github.com/m-x-d/Heretic2R) | Heretic II (1998, Raven Software) reverse-engineered source port. | 267 | 🟢 | C |
| [CivOne](https://github.com/Solen1985/CivOne) | Implementation of Sid Meier's Civilization. | 262 | 🔴 | C# |
| [OpenMBU](https://github.com/MBU-Team/OpenMBU) | OpenMBU is a revival of Marble Blast Ultra, the 2006 Xbox 360 arcade classic. | 258 | 🟢 | C++ |
| [OpenBW](https://github.com/OpenBW/openbw) | Open-source StarCraft: Brood War engine reimplementation | 254 | 🟢 | C++ |
| [OpenGD](https://github.com/Open-GD/OpenGD) | Open source implementation of Geometry Dash | 249 | 🟡 | C++ |
| [undertale](https://github.com/fachinformatiker/undertale) | Undertale src code | 247 | 🔴 | Game Maker Language |
| [2006scape](https://github.com/2006-Scape/2006Scape) | A 2006 Runescape Emulation Server | 242 | 🟢 | Java |
| [freeaoe](https://github.com/sandsmark/freeaoe) | A free game engine capable of running Age of Empires 2 and Star Wars: Galactic Battlegrounds | 241 | 🔴 | C++ |
| [KisakBlack](https://github.com/SwagSoftware/KisakBlack) | Open source reimplementation of Call of Duty: Black Ops | 232 | 🟢 | C++ |
| [Doom 64 EX+](https://github.com/atsb/Doom64EX-Plus) | An improved modern version of Doom64EX. | 230 | 🗄️ | C |
| [Kinoko](https://github.com/vabold/Kinoko) | Reimplementation of Mario Kart Wii's physics engine in C++ | 230 | 🟢 | C++ |
| [srceng-android](https://github.com/nillerusr/srceng-android) | Android launcher for source engine | 230 | 🔴 | Java |
| [OpenAWE](https://github.com/OpenAWE-Project/OpenAWE) | A reimplementation of Remedy Entertainments Alan Wake Engine, in later iterations known as the Northlight Engine | 220 | 🟢 | C++ |
| [rawgl](https://github.com/cyxx/rawgl) | Another World/Out of This World engine reimplementation (SDL, OpenGL) | 209 | 🗄️ | C++ |
| [impacto](https://github.com/CommitteeOfZero/impacto) | Reimplementation of the MAGES. visual novel engine | 199 | 🟢 | C++ |
| [Cave Story (CSE2)](https://github.com/gameblabla/CSE2) | Reverse-engineered reimplementation / port of Cave Story (CSE2) | 198 | 🟢 | C++ |
| [Duck Game Rebuilt](https://github.com/TheFlyingFoool/DuckGameRebuilt) | Duck Game decompiled & rebuilt with some added features, | 195 | 🟢 | C# |
| [OpenNFS1](https://github.com/jeff-1amstudios/OpenNFS1) | Remake of the original EA Need for Speed 1 using c# and Monogame | 195 | 🔴 | C# |
| [FreeFT](https://github.com/nadult/FreeFT) | Isometric action game engine | 193 | 🟢 | C++ |
| [XL Engine](https://github.com/Mindwerks/XLEngine) | XLEngine allows you to play Dark Forces, Daggerfall and soon Outlaws and Blood with modern technology. | 193 | 🔴 | C++ |
| [nanolathe](https://github.com/nanolathe-gg/nanolathe) | Total Annihilation engine reimplementation in Go | 191 | 🟢 | Go |
| [Reburn 3](https://github.com/reburndev/reburn3) | A work-in-progress open source reimplementation of Burnout 3: Takedown. | 189 | 🟡 | C++ |
| [Vib-Ribbon (open-ribbon)](https://github.com/open-ribbon/open-ribbon) | Reverse-engineered reimplementation / port of Vib-Ribbon (open-ribbon) | 188 | 🟡 | C |
| [sh3redux](https://github.com/Palm-Studios/sh3redux) | SILENT HILL 3 Engine Remake in OpenGL and C++ | 187 | 🟡 | C++ |
| [KaM Remake](https://github.com/reyandme/kam_remake) | "KaM Remake" is an RTS game remake written in Delphi from scratch. | 183 | 🟢 | Pascal |
| [Powerslave EX](https://github.com/svkaiser/PowerslaveEX) | Powerslave EX is a unofficial recreation of Lobotomy Software’s obscured FPS game, Powerslave (also known as Exhumed... | 183 | 🔴 | C |
| [lofp](https://github.com/jonradoff/lofp) | Recreation of Legends of Future Past, the 1990s commercial MUD | 180 | 🟢 | HTML |
| [pokered-gbc](https://github.com/dannye/pokered-gbc) | Pokémon Red/Blue overhauled with full GBC support. Made by FroggestSpirit, Drenn, and dannye. Also check out the crys... | 180 | 🟢 | Assembly |
| [Chasm-Reverse](https://github.com/Panzerschrek/Chasm-Reverse) | "PanzerChasm" is a free recreation of the game "Chash: - The Rift" by "ActionForms" using the original game data (CSM... | 179 | 🟢 | C++ |
| [Vault13](https://github.com/pingw33n/vault13) | Reimplementation of the Fallout 2 engine in Rust | 179 | 🟢 | Rust |
| [MegaManXSNESRecomp](https://github.com/mstan/MegaManXSNESRecomp) | Mega Man X recompiled for the Super Nintendo using snesrecomp · Part of the R.A.I.D. community | 178 | 🟢 | C |
| [Open Horizon](https://github.com/undefined-darkness/open-horizon) | Engine reimplementation of Ace Combat: Assault Horizon; uses original game data (C++) | 177 | 🔴 | C++ |
| [z2rs](https://github.com/troyedwardsjr/z2rs) | Clean-room reconstruction of Zelda II: The Adventure of Link in Rust | 175 | 🟢 | Rust |
| [eZeus](https://github.com/MaurycyLiebner/eZeus) | Open-source implementation of Zeus: Master of Olympus. | 174 | 🟢 | C++ |
| [Legacy of Kain: Soul Reaver Decompile](https://github.com/Gh0stBlade/KAIN2) | Legacy of Kain: Soul Reaver Decompile | 174 | 🟡 | C |
| [OpenMC2](https://github.com/OpenMC2/OpenMC2) | An Open Source Re-Implementation of Midnight Club 2 | 173 | 🔴 | C++ |
| [Panzer Dragoon Saga (Azel)](https://github.com/yaz0r/Azel) | Reverse-engineered reimplementation / port of Panzer Dragoon Saga (Azel) | 173 | 🟢 | C++ |
| [OpenHoW](https://github.com/hogsy/OpenHoW) | Open-source reimplementation of Gremlin's Hogs of War (PC/PSX). | 170 | 🗄️ | C |
| [OUO](https://github.com/draxinar/ouo) | OUO: reverse engineering of Ultima Online: The Second Age server | 170 | 🟢 | C |
| [rlvm](https://github.com/eglaysher/rlvm) | RealLive clone for Linux and OSX | 170 | 🟡 | C++ |
| [JXQY-all-in-one](https://github.com/Upwinded/JXQY-all-in-one) | 剑侠情缘 Sword Heroes' Fate | 168 | 🟢 | C++ |
| [OpenC1](https://github.com/jeff-1amstudios/OpenC1) | Remake of Carmageddon 1 engine | 168 | 🔴 | C# |
| [Arcanum Community Edition](https://github.com/alexbatalov/arcanum-ce) | Arcanum for modern operating systems | 167 | 🟢 | C |
| [whoa](https://github.com/whoahq/whoa) | Unofficial open-source reimplementation of the World of Warcraft 3.3.5 client | 167 | 🟢 | C++ |
| [ElonaFoobar](https://github.com/elonafoobar/elonafoobar) | One of the Elona variants | 164 | 🗄️ | C++ |
| [Nuvie](https://github.com/nuvie/nuvie) | Nuvie - New Ultima VI Engine | 164 | 🟡 | C++ |
| [dunedynasty](https://github.com/gameflorist/dunedynasty) | Remaster of Dune II built on the OpenDUNE reverse engineered codebase | 160 | 🟢 | C |
| [OpenTPW](https://github.com/OpenTPW/OpenTPW) | An open-source re-implementation of Bullfrog's Sim Theme Park / Theme Park World (1999). | 160 | 🟢 | C# |
| [SeriousSamClassic-VK](https://github.com/tx00100xt/SeriousSamClassic-VK) | Open source game engine for Serious Sam Classic with Vulkan support. | 160 | 🟢 | C++ |
| [Free in the Dark](https://github.com/yaz0r/FITD) | Free in the Dark, a Alone in the Dark engine reimplementation. | 158 | 🟡 | C++ |
| [Stargus](https://github.com/Wargus/stargus) | Importer and scripts for Starcraft | 157 | 🟢 | C++ |
| [OpenNefia](https://github.com/OpenNefia/OpenNefia) | Moddable engine reimplementation of the Japanese roguelike Elona. | 156 | 🟡 | C# |
| [OpenAG](https://github.com/YaLTeR/OpenAG) | Open-source reimplementation of the Adrenaline Gamer client library | 155 | 🟡 | C++ |
| [Zuma-Deluxe-HD](https://github.com/GalaxyShad/Zuma-Deluxe-HD) | A remake of the legendary 2003 PopCap game with improved textures and support for 16:9 aspect ratio. | 153 | 🟡 | C |
| [OGS](https://github.com/headcrab-junkyard/OGS) | An open-source GoldSrc engine clone (Clean authentic reimplementation without using reverse-engineered code) | 152 | 🟡 | C |
| [engge](https://github.com/scemino/engge) | Open source remake of Thimbleweed Park's engine | 151 | 🗄️ | C++ |
| [remc2](https://github.com/turican0/remc2) | Reverse engineering of Magic Carpet 2 from Assembler. | 151 | 🟢 | C++ |
| [hode](https://github.com/usineur/hode) | hode is a rewrite (made by Grégory Montoir) of the engine used in the game Heart of Darkness made by Amazing Studio. | 150 | 🟡 | C++ |
| [KotOR.js](https://github.com/KobaltBlu/KotOR.js) | A remake of the Odyssey Game Engine that powered KotOR I & II written in JavaScript | 149 | 🟢 | TypeScript |
| [kys-pascal](https://github.com/scarsty/kys-pascal) | 《金庸群侠传》Pascal重制版 | 149 | 🟢 | Pascal |
| [openQ4](https://github.com/themuffinator/openQ4) | Open-source reimplementation of Quake 4 | 149 | 🟢 | C++ |
| [rfvp](https://github.com/xmoezzz/rfvp) | Non-official Rust implementation of the FVP visual novel engine | 146 | 🟢 | Rust |
| [darkfo](https://github.com/darkf/darkfo) | DarkFO, a post-nuclear RPG remake (of Fallout 2) | 145 | 🗄️ | TypeScript |
| [JSettlers](https://github.com/paulwedeck/settlers-remake) | A Remake of "The Settlers III" for Windows, Linux and Android | 144 | 🗄️ | Java |
| [Strife: Veteran Edition](https://github.com/svkaiser/strife-ve) | Strife Veteran Edition GPL Source Release | 143 | 🔴 | C |
| [OpenMB](https://github.com/cookgreen/OpenMB) | Role-playing game engine for Taleworlds' Mount&Blade Series. | 142 | 🟢 | C# |
| [Q-Gears](https://github.com/q-gears/q-gears) | Q-Gears is an RPG engine for games like Squaresoft's Final Fantasy 7, 8, 9, or Xenogears. It is designed to be cross-... | 141 | 🔴 | C++ |
| [Litecraft](https://github.com/KernelFreeze/Litecraft) | Clean-room open source Minecraft client implementation | 138 | 🗄️ | Rust |
| [UA_source](https://github.com/Marisa-Chan/UA_source) | Mod for UrbanAssault (Replace original game engine) | 138 | 🟡 | C++ |
| [Free Heroes 2 - Enhanced](https://github.com/ciplogic/fheroes2enh) | Free Heroes 2 - Enhanced | 135 | 🔴 | C++ |
| [Uncharted waters 2 remake](https://github.com/JohanLi/uncharted-waters-2) | Browser-based remake of Uncharted Waters: New Horizons (大航海時代II) | 134 | 🟢 | TypeScript |
| [unity-arcanum](https://github.com/Suvitruf/unity-arcanum) | Fan-made reimplementation of the Arcanum engine in Unity | 134 | 🟢 | C# |
| [War1gus](https://github.com/Wargus/war1gus) | Importer and scripts for Warcraft: Orcs and Humans | 134 | 🟢 | Lua |
| [Test Drive Unlimited (OpenTestDriveUnlimited)](https://github.com/opentestdriveunlimited/OpenTestDriveUnlimited) | Reverse-engineered reimplementation / port of Test Drive Unlimited (OpenTestDriveUnlimited) | 133 | 🟢 | C++ |
| [The-Great-Escape-in-C](https://github.com/dpt/The-Great-Escape-in-C) | Classic ZX Spectrum game "The Great Escape" rewritten in portable C | 132 | 🟢 | C |
| [aoe](https://github.com/FolkertVanVerseveld/aoe) | Re-implementation of Age of Empires and the Rise of Rome expansion | 131 | 🟢 | C++ |
| [nv-rs](https://github.com/slaterain/nv-rs) | Experimental Fallout: New Vegas engine reimplementation in Rust and Bevy | 131 | 🟢 | Rust |
| [Galaxy on Fire 2 Unity Remake](https://github.com/JoppieToppie/Galaxy-on-Fire-2-Unity-Remake) | Galaxy on Fire 2 decompilation and Unity remake | 130 | 🟢 | C |
| [Raptor](https://github.com/skynettx/raptor) | Reversed-engineered source port from Raptor Call Of The Shadows | 130 | 🟢 | C |
| [Yukon](https://github.com/wizguin/yukon) | HTML5 Club Penguin client reimplementation | 130 | 🟡 | JavaScript |
| [lttp-phaser](https://github.com/englercj/lttp) | An incomplete remake of The Legend of Zelda - A Link to the Past using WebGL and the browser. | 126 | 🔴 | TypeScript |
| [Ozymandias (Julius)](https://github.com/Banderi/Ozymandias_Julius) | An open source re-implementation of Pharaoh (1999) in the Julius/Augustus engine | 126 | 🟢 | C++ |
| [Robot War Engine](https://github.com/MHeasell/rwe) | Robot War Engine - Real-time strategy game engine compatible with Total Annihilation | 126 | 🟢 | C++ |
| [Umineko Project](https://github.com/umineko-project/onscripter-ru) | ONScripter-RU game engine | 125 | 🔴 | C++ |
| [Paper Mario DX](https://github.com/bates64/papermario-dx) | Improved Paper Mario (N64) engine for your next romhack | 124 | 🟢 | C |
| [Prey 2006: A Talon Brave Game](https://github.com/FriskTheFallenHuman/Prey2006) | Prey 2006 SDK integrated with Doom 3 GPL release | 122 | 🟢 | C |
| [lain-bootleg-bootleg](https://github.com/ad044/lain-bootleg-bootleg) | Reverse engineering and remake of Lain Bootleg | 121 | 🟢 | C |
| [OpenNefia](https://github.com/Ruin0x11/OpenNefia) | Moddable engine reimplementation of the roguelike Elona | 121 | 🟡 | Lua |
| [MikuPan](https://github.com/Mikompilation/MikuPan) | PC Port Of Fatal Frame 1 Based On Himuro | 118 | 🟢 | C++ |
| [Apolyton Call to Power II Source Code Project](https://github.com/civctp2/civctp2) | Call to Power II: Apolyton Edition source code project. Call to Power II (CTP2) is a civilization computer game, whos... | 115 | 🟢 | C |
| [siglus_rs](https://github.com/xmoezzz/siglus_rs) | Unofficial Rust implementation of the SiglusEngine visual novel engine | 114 | 🟢 | Rust |
| [Dune2JS](https://github.com/oklemenz/Dune2JS) | Dune II reimplementation in HTML5/JavaScript | 112 | 🟡 | JavaScript |
| [Javascript BoulderDash](https://github.com/jakesgordon/javascript-boulderdash) | An HTML5 implementation of the c64 classic Boulderdash game | 112 | 🟡 | JavaScript |
| [Ambermoon](https://github.com/Pyrdacor/Ambermoon) | Resources and reimplementation for the Amiga game Ambermoon | 111 | 🟢 | Assembly |
| [Magic Carpet 2 HD](https://github.com/thobbsinteractive/magic-carpet-2-hd) | Recode Binary code of game Magic Carpet2 to C/C++ language(remake MC2 for any platform) | 111 | 🟢 | C++ |
| [1oom](https://github.com/1oom-fork/1oom) | 1oom is a Master of Orion Classic (1993) game engine recreation that requires the original files to run. | 110 | 🟢 | C |
| [Gorc](https://github.com/jdmclark/gorc) | Early-development Jedi Knight: Dark Forces 2 game engine recreation | 110 | 🔴 | C++ |
| [Lemmings.ts](https://github.com/tomsoftware/Lemmings.ts) | A Web Lemmings Clone/Remake in TypeScript | 109 | 🔴 | TypeScript |
| [Civ2-clone](https://github.com/axx0/Civ2-clone) | Open-source re-implementation of Civilization 2 | 108 | 🟢 | C# |
| [CrossCraft](https://github.com/CrossCraft/CrossCraft) | Open-source Minecraft reimplementation | 108 | 🟢 | Zig |
| [lithtech](https://github.com/Katana-Steel/lithtech) | Engine reimplementation of F.E.A.R., The Operative: No One Lives Forever; uses original game data (C++) | 102 | 🟢 | C++ |
| [neo](https://github.com/NeotokyoRebuild/neo) | NEOTOKYO;REBUILD: reimplementation and continuation of the NEOTOKYO mod on a TF2 engine branch | 102 | 🟢 | C++ |
| [cavestory-sdl2](https://github.com/JIghtuse/cavestory-sdl2) | Reconstructing Cave Story with SDL 2.0 and C++14 | 101 | 🔴 | C++ |
| [DreeRally](https://github.com/enriquesomolinos/DreeRally) | Death Rally engine reimplementation | 101 | 🔴 | C |
| [Redguard Unity](https://github.com/RGUnity/redguard-unity) | Main repository containing the Unity project and the wiki | 99 | 🟢 | C# |
| [OpenCity2k](https://github.com/OpenCity2k/OpenCity2k) | Open source reimplementation of SimCity 2000 | 97 | 🟡 | Python |
| [tf15-client](https://github.com/Velaron/tf15-client) | Reverse engineered Team Fortress Classic client for Xash3D | 96 | 🟡 | C++ |
| [ko](https://github.com/ko4life-net/ko) | Open source reverse engineered recreation of an old Knight Online version | 94 | 🟡 | C++ |
| [UchuServer](https://github.com/UchuServer/Uchu) | LEGO Universe server written in C# | 93 | 🟡 | C# |
| [Executive Man](https://github.com/CamHenlin/ExecutiveMan) | ExecutiveMan, a JavaScript MegaMan clone | 92 | 🔴 | JavaScript |
| [OpenVice](https://github.com/clashbyte/openvice) | Grand Theft Auto: Vice City Open Source port to C# | 92 | 🟡 | C# |
| [OpenCrystalCaves](https://github.com/OpenCrystalCaves/OpenCrystalCaves) | OCC is an unofficial open source engine reimplementation of the game trilogy Crystal Caves. | 91 | 🟢 | C++ |
| [PC port of Animal Crossing](https://github.com/ACreTeam/forest) | PC Port of Animal Crossing | 91 | 🟢 | C |
| [OpenUG2](https://github.com/whoismept/OpenUG2) | From-scratch reimplementation of Need for Speed: Underground 2 | 90 | 🟢 | C |
| [The Great Escape](https://github.com/dpt/The-Great-Escape) | Classic ZX Spectrum game "The Great Escape" reverse engineered | 90 | 🟡 | Assembly |
| [Barnyard (OpenBarnyard)](https://github.com/InfiniteC0re/OpenBarnyard) | Reverse-engineered reimplementation / port of Barnyard (OpenBarnyard) | 89 | 🟢 | C++ |
| [dejavu](https://github.com/rpjohnst/dejavu) | Game Maker runtime reimplementation | 89 | 🟡 | Rust |
| [librwgta](https://github.com/aap/librwgta) | GTA-specific extensions to librw (RenderWare reimplementation) and tools using it | 89 | 🟢 | C++ |
| [OpenSC4](https://github.com/OpenSC4-org/OpenSC4) | Open source reimplementation of SimCity 4 | 89 | 🟡 | GDScript |
| [glfrontier](https://github.com/pcercuei/glfrontier) | Reverse engineered version of Frontier: Elite II | 88 | 🔴 | C |
| [MegaManX4Recomp](https://github.com/mstan/MegaManX4Recomp) | Mega Man X4 (USA, SLUS-00561) statically recompiled to a native PC executable with PSXRecomp | 88 | 🟢 | C |
| [Pizza Tower (OpenTower)](https://github.com/femloy/OpenTower) | Reverse-engineered reimplementation / port of Pizza Tower (OpenTower) | 88 | 🟢 | Game Maker Language |
| [OpenRaider](https://github.com/xythobuz/OpenRaider) | Open Source Tomb Raider Engine | 86 | 🟡 | C++ |
| [Worldstone](https://github.com/Lectem/Worldstone) | Diablo 2 tools and engine reimplementation in C++ | 82 | 🔴 | C++ |
| [f2bgl](https://github.com/cyxx/f2bgl) | Fade To Black engine reimplementation (SDL, OpenGL) | 81 | 🗄️ | C++ |
| [u4-decompiled](https://github.com/ergonomy-joe/u4-decompiled) | Decompiled source code for the PC version of Ultima IV - Quest Of The Avatar | 81 | 🔴 | C |
| [xoreos-tools](https://github.com/xoreos/xoreos-tools) | Tools for BioWare Aurora engine game formats, companion to the xoreos reimplementation | 81 | 🟢 | C++ |
| [Ultima 5 Redux](https://github.com/bradhannah/Ultima5Redux) | A mostly true to the original Ultima 5 remake in C# using the original U5 data files. | 80 | 🟡 | C# |
| [WinWar](https://github.com/CAMongrel/WinWar) | WarCraft Orcs & Humans remake using the original assets | 80 | 🗄️ | C# |
| [OpenSR](https://github.com/ObKo/OpenSR) | Opensource multi-genre game based upon "Space Rangers 2: Dominators" | 77 | 🗄️ | C++ |
| [tower-together](https://github.com/phulin/tower-together) | Clone of the 1993 game SimTower | 77 | 🟢 | TypeScript |
| [Xenogears (Noah, non-matching)](https://github.com/yaz0r/Noah) | Reverse-engineered reimplementation / port of Xenogears (Noah, non-matching) | 77 | 🟢 | C++ |
| [openstrike](https://github.com/AMDmi3/openstrike) | Libre reimplementation of Jungle and Desert Strike games | 76 | 🟡 | C++ |
| [FreeHeroes](https://github.com/mapron/FreeHeroes) | FreeHeroes is a free engine for Heroes of Might and Magic 3, similar to VCMI project. | 75 | 🟢 | C++ |
| [OpenMoonstone](https://github.com/joetsoi/OpenMoonstone) | Open source reimplementation of Moonstone: A Hard Day's Knight | 75 | 🔴 | Rust |
| [ppengine](https://github.com/jonathanopalise/ppengine) | 3D remake of Pole Position using game logic reverse engineered from the arcade ROMs | 75 | 🔴 | C |
| [Snipes](https://github.com/Davidebyzero/Snipes) | The classic 1982 text-mode game Snipes, ported from the original DOS executable with 100% identical game logic, with... | 75 | 🟡 | C++ |
| [Underworld Adventures](https://github.com/vividos/UnderworldAdventures) | Underworld Adventures is a project to recreate Ultima Underworld 1 on modern operating systems, using the original ga... | 75 | 🟢 | C++ |
| [dRally](https://github.com/urxp/dRally) | Open Source Engine / Death Rally [1996] | 74 | 🔴 | C |
| [MegaManX6Recomp](https://github.com/mstan/MegaManX6Recomp) | Mega Man X6 (USA) recompiled for the Sony PlayStation using psxrecomp · Part of the R.A.I.D. community | 73 | 🟢 | Python |
| [OpenAOE](https://github.com/angered-ghandi/OpenAOE) | Open source reimplementation of Age of Empires (1997) | 73 | 🔴 | Rust |
| [openbgi](https://github.com/Cytlan/openbgi) | Open source reimplementation of the Ethornell Buriko General Interpreter | 73 | 🟢 | C |
| [SCSharp](https://github.com/toshok/scsharp) | Starcraft reimplementation in C# | 73 | 🔴 | C# |
| [OpenFNaF](https://github.com/MotoLegacy/OpenFNaF) | Open source reimplementation of Five Nights at Freddy's | 72 | 🔴 | C |
| [Wolfenshine](https://github.com/deanthecoder/Wolfenshine) | Modern C# reimplementation of Wolfenstein 3D | 72 | 🟢 | C# |
| [LTJS](https://github.com/bibendovsky/ltjs) | LithTech Jupiter System | 71 | 🟢 | C++ |
| [Mario Kart 64 for Dreamcast](https://github.com/jnmartin84/mk64-dc) | Sega Dreamcast port of Mario Kart 64 decompilation | 70 | 🟢 | C |
| [OpenPigeon](https://github.com/OpenBubbles/OpenPigeon) | Open-source GamePigeon reimplementation | 70 | 🟢 | Kotlin |
| [steins-gate](https://github.com/FGRE/steins-gate) | Reimplementation of Steins;Gate visual novel | 70 | 🔴 | C++ |
| [VitalWear](https://github.com/cfogrady/VitalWear) | Wear OS engine recreation of the Bandai Vital Bracelet BE | 70 | 🟡 | Kotlin |
| [Another World JS](https://github.com/cyxx/another_js) | Another World/Out of This World (HTML5) | 69 | 🗄️ | JavaScript |
| [NFS Recompiled](https://github.com/motor-dev/nfs-recompiled) | Engine reimplementation of Need For Speed II, Need For Speed III: Hot Pursuit; uses original game data (C++) | 69 | 🟢 | C++ |
| [Test-Drive-3-Maps](https://github.com/s-macke/Test-Drive-3-Maps) | Reverse-engineered and extracted the world maps of the 1990 DOS game Test Drive III | 69 | 🟢 | Assembly |
| [chronon](https://github.com/hogsy/chronon) | Open-source reimplementation of Anachronox | 68 | 🟡 | C++ |
| [Loderunner](https://github.com/Piddewitt/Loderunner) | Reverse engineered C64 assembler source code to recreate a bit for bit identical version of the original game. | 67 | 🟡 | Assembly |
| [Cosmo-Engine](https://github.com/yuv422/cosmo-engine) | A new game engine to play the MS-DOS game "Cosmo's Cosmic Adventure" on modern systems | 66 | 🟢 | C |
| [Dangerous Dave 2: Modification Edition](https://github.com/Harchvertelol/Dangerous-Dave-2-Modification-Edition) | This is an open-source remake of a well-known platform game Dangerous Dave 2 with flexible and highly customizable co... | 66 | 🟢 | HTML |
| [Another World Suite](https://github.com/malandrin/another-world-suite) | A Rust implementation of the "Another World" ("Out of This World" in the USA) game engine, compiled to WebAssembly to... | 65 | 🔴 | Rust |
| [libnpengine](https://github.com/FGRE/libnpengine) | Free implementation of Nitroplus/5pb. Visual Novel game engine | 65 | 🔴 | C++ |
| [TombaRecomp](https://github.com/mstan/TombaRecomp) | Tomba! (USA) recompiled for the Sony PlayStation using psxrecomp · Part of the R.A.I.D. community | 65 | 🟢 | C++ |
| [OpenDance](https://github.com/WodsonKun/OpenDance) | Recreation of the Just Dance engine in GameMaker | 64 | 🟢 | Game Maker Language |
| [Total Annihilation 3D](https://github.com/zuzuf/TA3D) | Portable remake of Total Annihilation in 3D | 64 | 🔴 | C |
| [shin](https://github.com/DCNick3/shin) | A reimplementation of VN engine primarily used by 07-th expansion releases on consoles (and some other entergram games) | 63 | 🟢 | Rust |
| [Open76](https://github.com/r1sc/Open76) | Interstate '76 engine reimplementation | 62 | 🔴 | C# |
| [scion](https://github.com/nsgomez/scion) | Reimplementation of the Maxis engine used by The Sims 2 and SimCity 4 | 62 | 🟡 | C++ |
| [Nitro](https://github.com/billsonnn/nitro-react) | HTML5 Habbo Hotel client reimplementation in React | 61 | 🟢 | TypeScript |
| [Blues](https://github.com/cyxx/blues) | Blues Brothers, Jukebox Adventure & Prehistorik 2 engine reimplementation (PSP, SDL2) | 60 | 🗄️ | C |
| [redstone-js](https://github.com/LostMyCode/redstone-js) | Play RED STONE ONLINE in the browser | 60 | 🟢 | JavaScript |
| [OpenDrakan](https://github.com/Zalasus/opendrakan) | A work-in-progress recreation of Surreal Software's Riot Engine | 59 | 🟡 | C++ |
| [OpenWar](https://github.com/andreas-jonsson/openwar) | Classic fantasy RTS game in the spirit of Warcraft: Orcs & Humans. | 59 | 🔴 | Go |
| [Colditz Escape](https://github.com/aperture-software/colditz-escape) | Amiga's "Escape From Colditz" ported to Windows, Linux, macOS and PSP | 58 | 🟢 | C |
| [Cryogenic](https://github.com/OpenRakis/Cryogenic) | An open-source reimplementation of Cryo's DUNE game (WIP) | 58 | 🟢 | C# |
| [FPC Atomic](https://github.com/PascalCorpsman/fpc_atomic) | Playable clone of the legendary Atomic Bomberman including Network and Ai https://en.wikipedia.org/wiki/Atomic_Bomberman | 58 | 🟢 | Pascal |
| [lilium-voyager](https://github.com/clover-moe/lilium-voyager) | An engine replacement for Star Trek Voyager: Elite Force Holomatch (multiplayer). | 58 | 🟢 | C |
| [rock-raiders-remake](https://github.com/rystills/rock-raiders-remake) | Partial HTML5 remake of the classic game "Lego Rock Raiders". | 58 | 🔴 | JavaScript |
| [u6-decompiled](https://github.com/ergonomy-joe/u6-decompiled) | Decompiled code for PC/MSDOS version of Ultima VI - The False Prophet | 58 | 🔴 | C |
| [freeage](https://github.com/puzzlepaint/freeage) | Open-source reimplementation of the Age of Empires 2: Definitive Edition engine | 57 | 🗄️ |  |
| [LasMarionetas](https://github.com/OmniBlade/LasMarionetas) | Open-source reimplementation of The Sims | 57 | 🔴 | C++ |
| [Mikompilation](https://github.com/Mikompilation/Mikompilation) | Reimplementation project for the Fatal Frame 2 : Crimson Butterfly (Project Zero 2/零～紅い蝶) game engine | 57 | 🟡 | C |
| [Nitrosharp](https://github.com/CommitteeOfZero/nitrosharp) | Open-source N2System reimplementation | 57 | 🟢 | C# |
| [OpenCrashWOC](https://github.com/Open-Travelers/OpenCrashWOC) | Reverse engineered reimplementation of Crash Bandicoot: The Wrath of Cortex | 57 | 🟢 | C |
| [REminiscence / REinforced](https://github.com/chermenin/REminiscence) | REminiscence is a re-implementation of the engine used in the game Flashback made by Delphine Software. | 57 | 🟢 | C++ |
| [sioux](https://github.com/hanatos/sioux) | Open-source reimplementation of the Comanche 3 helicopter sim engine | 56 | 🟡 | C |
| [TOD_tools](https://github.com/Michael0ne/TOD_tools) | Reversed engine and tools of Total Overdose (2005, PC) | 56 | 🟡 | C++ |
| [WolfensteinRPG-RE](https://github.com/Erick194/WolfensteinRPG-RE) | Wolfenstein RPG reverse engineering and reimplementation | 56 | 🟡 | C++ |
| [RSDKv2 Decompilation](https://github.com/RSDKModding/RSDKv2-Decompilation) | a Decompilation of the 2008 Retro-Sonic Engine Demo of Sonic Nexus | 55 | 🟢 | C++ |
| [Stardust rebuilt](https://github.com/TheJare/stardust-48k) | Reverse engineered source for the 1987 Sinclair Spectrum game "Stardust" | 55 | 🔴 | Assembly |
| [SF2DISASM](https://github.com/ShiningForceCentral/SF2DISASM) | A disassembly of the game "Shining Force II" for documentation and fan-project purposes. | 54 | 🟢 | Assembly |
| [Airline Tycoon](https://github.com/openairlinetycoon/AirlineTycoon) | Source code of Airline Tycoon based on the GOG source code release | 53 | 🔴 | C++ |
| [engge2](https://github.com/scemino/engge2) | Open source remake of Thimbleweed Park's engine | 53 | 🟡 | Nim |
| [open-rct3](https://github.com/open-rct3/open-rct3) | Open-source re-implementation of RollerCoaster Tycoon 3 | 53 | 🟢 | C# |
| [Prince-Monogame](https://github.com/salvadorc17/Prince-Monogame) | Monogame implementation of Prince of Persia 2. | 53 | 🟢 | C# |
| [ReksioEngine](https://github.com/ReksioEngine/ReksioEngine) | Reimplementation of the BlooMoo and Piklib engines for the Reksio PC games | 53 | 🟢 | TypeScript |
| [MegaManX5Recomp](https://github.com/mstan/MegaManX5Recomp) | Mega Man X5 (USA, SLUS-01334) statically recompiled to a native Windows executable with the PSXRecomp framework. | 52 | 🟢 | PowerShell |
| [open-reckless-drivin](https://github.com/natecraddock/open-reckless-drivin) | Open-source reimplementation of the Macintosh shareware game Reckless Drivin' | 52 | 🟡 | Zig |
| [SimUnity2](https://github.com/LazyDuchess/SimUnity2) | Attempt at a reimplementation of The Sims 2 Ultimate Collection in the Unity Engine... | 52 | 🗄️ | C# |
| [wacki](https://github.com/mszula/wacki) | From-scratch C/SDL2 reimplementation of Wacki (1998) from reverse-engineered opcodes | 52 | 🟢 | C |
| [OpenNitemare3D](https://github.com/BBQGiraffe/OpenNitemare3D) | reimplementation of the 1994 FPS Nitemare 3D | 51 | 🔴 | C# |
| [BtBuilder](https://github.com/dulsi/btbuilder) | An open source implementation of the Bard's Tale Construction Set. | 50 | 🟢 | C |
| [DesktopAdventures](https://github.com/shinyquagsire23/DesktopAdventures) | A recreation of the Desktop Adventures engine in C | 50 | 🔴 | C |
| [femto8](https://github.com/benbaker76/femto8) | Open-source reimplementation of the PICO-8 fantasy console for embedded systems | 50 | 🟢 | C |
| [OpenRayman](https://github.com/imaginaryPineapple/OpenRayman) | Open-source reimplementation of the Rayman 2 engine | 50 | 🔴 | C |
| [CorrinoEngine](https://github.com/cookgreen/CorrinoEngine) | CorrinoEngine is an open-source RTS engine inspired by Emperor: Battle for Dune, with Emperor: Battle for Dune compat... | 49 | 🟢 | C# |
| [jsFO](https://github.com/ajxs/jsFO) | Fallout 2 Javascript port | 48 | 🟢 | JavaScript |
| [OpenLGR](https://github.com/james-knippes/openlgr) | Engine reimplementation of Lego Racers; uses original game data (C) | 48 | 🗄️ | C |
| [ReChan](https://github.com/SilverwireGames/ReChan) | Jackie Chan Stuntmaster reimplementation | 48 | 🟢 | C++ |
| [de Blob (OpenToshi)](https://github.com/AdventureT/OpenToshi) | Reverse-engineered reimplementation / port of de Blob (OpenToshi) | 47 | 🟢 | C++ |
| [Mechanized Assault & eXploration Reloaded](https://github.com/maxr-dot-org/maxr) | A turn based strategy game | 47 | 🟢 | C++ |
| [Lemmix](https://github.com/ericlangedijk/Lemmix) | Lemmix Main Source Code - Lemmings Clone | 45 | 🔴 | Pascal |
| [libRealSpace](https://github.com/remileonard/libRealSpace) | Tools to parse and render Origin Systems RealSpace engine assets. | 45 | 🟢 | C++ |
| [sacengine](https://github.com/tg-2/sacengine) | Engine reimplementation for Sacrifice by Shiny Entertainment | 45 | 🟢 | D |
| [OpenGTA](https://github.com/madebr/OpenGTA) | OpenGTA: copy of http://ogta.fifengine.de/ | 44 | 🔴 | C++ |
| [RAD](https://github.com/jval1972/Rad-X) | RAD: Remake of the game "Radix - Beyond the void" | 44 | 🟡 | Pascal |
| [reevengi](https://github.com/pmandin/reevengi) | Resident Evil engine reimplementation | 44 | 🔴 | C |
| [Blast Corps](https://github.com/retroplastic/blastcorps) | A Blast Corps decompilation. | 43 | 🔴 | C |
| [GLKeeper](https://github.com/codenamecpp/GLKeeper) | Open Source Dungeon Keeper 2 Reimplementation | 43 | 🟢 | C++ |
| [OpenBattlefield2](https://github.com/Moxnatiy/OpenBattlefield2) | Clean-room reimplementation of DICE's Refractor 2 engine (Battlefield 2) | 42 | 🟢 | C++ |
| [Chrono Trigger C](https://github.com/buzzer-re/Chrono-Trigger-C) | A simple remake of Chrono Trigger written in C, using the SDL API | 41 | 🗄️ | C |
| [OpenSith](https://github.com/r1sc/OpenSith) | Jedi Knight: Dark Forces II engine reimplementation | 41 | 🟡 | C# |
| [pfr](https://github.com/wanda-phi/pfr) | Pinball Fantasies (1992) reverse engineered and re-created | 41 | 🟡 | Rust |
| [Phoenix](https://github.com/joulupunikki/Phoenix) | Java clone/remake/patch of the game Emperor of the Fading Suns | 41 | 🔴 | Java |
| [abyssal](https://github.com/TheWWWorm/abyssal) | Godot engine edition of Deep 3D: Submarine Odyssey by Fishlabs | 40 | 🟢 | GDScript |
| [F-Zero X (USA)](https://github.com/BttrDrgn/f-zerox) | F-Zero X Decompilation | 40 | 🔴 | C |
| [FelineSystem2](https://github.com/kokseen1/FelineSystem2) | Open-source remake of the CatSystem2 visual novel engine | 40 | 🔴 | C++ |
| [JLud2D](https://github.com/rafael-esper/JLud2D) | 2D old-school Engine for Games | 40 | 🟢 | TypeScript |
| [Jurassic Park: Operation Genesis (OpenJPOG)](https://github.com/AdventureT/OpenJPOG) | Reverse-engineered reimplementation / port of Jurassic Park: Operation Genesis (OpenJPOG) | 40 | 🟢 | C++ |
| [OpenSHC](https://github.com/sourcehold/OpenSHC) | An open source re-implementation of Stronghold Crusader | 40 | 🟢 | C++ |
| [openSMB2](https://github.com/Matriks404/openSMB2) | Open-source reimplementation of Super Mario Bros. 2 in Lua and LOVE | 39 | 🗄️ | Lua |
| [Quest 64 Decompilation](https://github.com/Mallos31/Quest) | decompilation of Quest64 | 39 | 🟡 | C |
| [smb1-disasm](https://github.com/laura240406/smb1-disasm) | A collection to build SMB1 from the disassembly | 39 | 🔴 | Assembly |
| [Super Mario Bros. 3Mix](https://github.com/captainsouthbird/3Mix) | Super Mario Bros 3Mix hack | 39 | 🔴 | Assembly |
| [ChronoStorm](https://github.com/cookgreen/ChronoStorm) | Open-source engine reimplementation of Command & Conquer: Red Alert 2 and Yuri's Revenge | 38 | 🟢 | Python |
| [freevgui](https://github.com/FWGS/freevgui) | Free and open-source reimplementation of the Half-Life VGUI library | 38 | 🟢 | C++ |
| [ChaseHQ](https://github.com/dpt/ChaseHQ) | Chase H.Q. for ZX Spectrum — reverse-engineered and reconstructed in portable C | 37 | 🟢 | C |
| [earthbound](https://github.com/Herringway/earthbound) | attempt at decompiling+porting earthbound | 37 | 🟡 | D |
| [OpenRakis](https://github.com/OpenRakis/OpenRakis) | Tools for an open-source reimplementation of Cryo's Dune (1992) | 37 | 🟢 | Assembly |
| [OpenXeen](https://github.com/busyDuckman/OpenXeen) | Might and Magic engine rewrite. | 37 | 🔴 | Java |
| [openzt](https://github.com/openzt1/openzt) | WIP Reimplimentation of Zoo Tycoon (2001) | 37 | 🟢 | Rust |
| [JJFFE](https://github.com/videogamepreservation/jjffe) | John Jordan's reverse engineering of Frontier: First Encounters. | 35 | 🗄️ | Assembly |
| [Pokémon Anniversary Red](https://github.com/TwitchPlaysPokemon/pokemonAnniversaryRed) | Anniversary Red dissassembly | 35 | 🔴 | Assembly |
| [reb3](https://github.com/lolz0r/reb3) | Partial reverse-engineered rebuild of Burnout 3: Takedown | 35 | 🟢 | C |
| [sadx_decomp](https://github.com/FraGag/sadx_decomp) | Sonic Adventure DX Decompilation | 35 | 🗄️ | C |
| [PyTouhou](https://github.com/GovanifY/PyTouhou) | Open-source reimplementation of the Touhou Generation 1 Windows engine | 34 | 🔴 | Python |
| [rsc-remastered](https://github.com/Danjb1/rsc-remastered) | Reverse-engineered implementation of the RuneScape Classic client | 34 | 🔴 | Java |
| [Contra_remake](https://github.com/EmileSonneveld/Contra_remake) | The first level of a cool arcade game remade in c++ | 33 | 🔴 | JavaScript |
| [F.LF](https://github.com/tyt2y3/F.LF) | Clean-room implementation of the fighting game Little Fighter 2 | 33 | 🔴 | HTML |
| [OpenTitus](https://github.com/stople/OpenTitus) | A port of the game engine behind the DOS versions of Titus the Fox and Moktar | 33 | 🔴 |  |
| [mdk-sdl](https://github.com/nemo22/mdk-sdl) | Port of Shiny's MDK (1997) to C# and SDL3 based on reverse engineering | 32 | 🟢 | C# |
| [Re-Comprehend](https://github.com/RyanMallon/recomprehend) | Open source implementation of the Comprehend adventure game engine used by the games Transylvania, Crimson Crown, and... | 32 | 🔴 | C |
| [The Castles of Dr. Creep](https://github.com/segrax/DrCreep) | The Castles of Dr. Creep | 32 | 🔴 | C++ |
| [Dungeon Craft](https://github.com/grannypron/uaf) | Engine reimplementation of Forgotten Realms: Unlimited Adventures; uses original game data (C++) | 31 | 🟢 | C++ |
| [Lode Runner 2020](https://github.com/Ma-Pe-Ma/Lode-Runner-2020) | A remake of the classic '80s puzzle game! | 31 | 🟢 | C++ |
| [Mario-Bros.-Dis](https://github.com/RussianManSMWC/Mario-Bros.-Dis) | Mario Bros. (NES) Disassembly | 31 | 🟢 | Assembly |
| [REminiscence](https://github.com/cyxx/REminiscence) | Flashback engine reimplementation (Android, SDL) | 31 | 🗄️ | C++ |
| [Rosebed](https://github.com/mdmrk/rosebed) | From-scratch Zig reimplementation of Minecraft Beta 1.7.3 client and server, protocol-compatible | 31 | 🟢 | Zig |
| [Shining Force 2 Reverse Engineer (SF2RE)](https://github.com/ShiningForceCentral/SF2RE) | Collaborative work on reverse-engineering Shining Force II, and source of main project SF2DISASM (see website link) | 31 | 🟡 | C |
| [OpenMM2](https://github.com/0x1F9F1/OpenMM2) | Open-source re-implementation of Midtown Madness 2 | 30 | 🗄️ | C |
| [Doom 64 for Dreamcast](https://github.com/jnmartin84/doom64-dc) | Doom 64 port for Sega Dreamcast / KallistiOS | 29 | 🟢 | C |
| [Future Cop: MIT](https://github.com/Ghoster738/Future-Cop-MIT) | Open Source Game Engine Project | 29 | 🟢 | C++ |
| [OpenOrion2](https://github.com/nextghost/openorion2) | Open-source remake of Master of Orion II: Battle at Antares | 29 | 🟢 | C++ |
| [beatfever](https://github.com/Sulunia/beatfever) | Partial open-source reimplementation of the osu! game engine in Lua/LOVE | 28 | 🔴 | Lua |
| [Bermuda Syndrome](https://github.com/cyxx/bermuda) | Bermuda Syndrome engine reimplementation (Emscripten, libretro, SDL2) | 28 | 🗄️ | C++ |
| [Magnetar](https://github.com/joankaradimov/Magnetar) | Magnetar is a StarCraft: Brood War mod/reimplementation. | 28 | 🟡 | C++ |
| [mengde](https://github.com/wateret/mengde) | A turn-based RPG game engine inspired by 三國志曹操傳. | 28 | 🔴 | C++ |
| [freetfc](https://github.com/eukara/freetfc) | Clean-room reimplementation of Team Fortress Classic in QuakeC | 27 | 🟡 | C |
| [Heroes Of JinYong](https://github.com/soarqin/HeroesOfJinYong) | A reimplementation of the DOS game `The legend of Jin Yong Heroes(金庸群侠传)` | 27 | 🟢 | C++ |
| [kys-js](https://github.com/kt2/kys-js) | 《金庸群侠传》kys-js (pixijs) | 27 | 🔴 | JavaScript |
| [linyaga](https://github.com/cyxx/linyaga) | Humongous Yaga engine reimplementation | 27 | 🗄️ | C |
| [OpenCloud](https://github.com/Gundorada-Workshop/OpenCloud) | Open source reimplementation of the Dark Cloud games | 27 | 🟡 | C++ |
| [opengta2](https://github.com/ikkentim/opengta2) | Open-source re-implementation of GTA II in C# using the original assets | 27 | 🟢 | C# |
| [WinTex](https://github.com/ElakaSnarne/WinTex) | Engine reimplementation of Under a Killing Moon; uses original game data (C++) | 27 | 🟢 | C++ |
| [vigasocosdl-la-abadia-del-crimen](https://github.com/luzbel/vigasocosdl-la-abadia-del-crimen) | Automatically exported from code.google.com/p/vigasocosdl-la-abadia-del-crimen | 26 | 🔴 | Assembly |
| [DungeonMaster.NET](https://github.com/ggrrin/DungeonMaster.NET) | Reimplementation of famous old Dungeon Master game. | 25 | 🔴 | C# |
| [freegunman](https://github.com/eukara/freegunman) | Clean-room reimplementation of Gunman Chronicles in QuakeC | 25 | 🟡 | C |
| [Iris2](https://github.com/kblaschke/Iris2) | An Open-Source 3D Ultima Online(tm) Client. No active development, mostly for archival purposes as the original proje... | 25 | 🔴 | C |
| [SiegeFX](https://github.com/codingncaffeine/SiegeFX) | Open-source reimplementation of Dungeon Siege (2002) in C# | 25 | 🟢 | C# |
| [Thirdeye](https://github.com/psi29a/thirdeye) | Reimplementation of AESOP that runs Eye of the Beholder 3 and Dungeon Hack. | 25 | 🟢 | C++ |
| [Harold](https://github.com/OldGamesLab/Harold) | Open-source Fallout 2 engine implementation, a revival of darkfo project | 24 | 🔴 | TypeScript |
| [skyroads-port](https://github.com/ammaarreshi/skyroads-port) | 1:1 reverse-engineered portable port of SkyRoads (1993) in C11 + SDL2 | 24 | 🟢 | C |
| [Bedlam 2: Absolute Bedlam](https://github.com/8street/Bedlam2) | Source code for Bedlam 2 (1997) game executable file. | 23 | 🔴 | Assembly |
| [F-Zero Clone](https://github.com/chipbell4/F-Zero-Clone) | A WebGL F-Zero clone. Show ya moves! | 23 | 🔴 | JavaScript |
| [OpenMM1](https://github.com/0x1F9F1/OpenMM1) | Open-source re-implementation of Midtown Madness 1 | 23 | 🗄️ | C++ |
| [OpenNox](https://github.com/noxworld-dev/opennox) | Open-source reimplementation of Nox | 23 | 🗄️ | C |
| [cc94](https://github.com/institution/cc94) | Remake of 1994 Sid Meier's Colonization game | 22 | 🔴 | C++ |
| [DuckHunt](https://github.com/grosbouddha/duckhunt) | Canvas based remake of the NES DuckHunt game. | 22 | 🔴 | JavaScript |
| [Igor](https://github.com/cyxx/igor) | Igor: Objetivo Uikokahonia game interpreter (Android, SDL) | 22 | 🗄️ | C++ |
| [SF1DISASM](https://github.com/ShiningForceCentral/SF1DISASM) | A disassembly of the game "Shining Force" for documentation and fan-project purposes. | 22 | 🟢 | Assembly |
| [wkbre2](https://github.com/AdrienTD/wkbre2) | WK Engine Reimplementation Rewrite with Multiplayer support! | 22 | 🟢 | C++ |
| [captain-bible-re](https://github.com/peterkelly/captain-bible-re) | Reverse engineering of the 1994 DOS game Captain Bible in the Dome of Darkness | 21 | 🟢 | Rust |
| [LOZ](https://github.com/aldonunez/Loz) | A remake of The Legend of Zelda | 21 | 🔴 | C++ |
| [REminiscence](https://github.com/libretro/REminiscence) | Flashback engine reimplementation | 21 | 🟢 | C++ |
| [shock2quest](https://github.com/tommy-xr/shock2quest) | Unofficial recreation of the Dark engine for System Shock 2 on Quest | 21 | 🟢 | Rust |
| [7k2](https://github.com/7k2/7k2) | Experimental fork of Seven Kingdoms II: The Fryhtan Wars | 20 | 🔴 | C++ |
| [Chocolate Blood](https://github.com/NBlood/chocolate-blood) | Chocolate Doom inspired Blood port (heavily WIP) | 20 | 🟡 | C |
| [OpenBreed](https://github.com/mrpetro/OpenBreed) | Open source reimplementation of classic Alien Breed 2D games and editor. | 20 | 🟢 | C# |
| [Q2RTXPerimental](https://github.com/PolyhedronStudio/Q2RTXPerimental) | My 'Experimental' fork of NVIDIA’s implementation of RTX ray-tracing in Quake II | 20 | 🟢 | C++ |
| [Sonic Lost World (OpenLW)](https://github.com/Radfordhound/OpenLW) | Reverse-engineered reimplementation / port of Sonic Lost World (OpenLW) | 20 | 🟡 | C++ |
| [wkbre](https://github.com/AdrienTD/wkbre) | Warrior Kings (Battles) game engine reimplementation / recreation | 20 | 🟡 | C++ |
| [Amiga Cannonball-C](https://github.com/lantus/Cannonball-C) | Cannonball for the Amiga ported to C | 19 | 🔴 | C |
| [COD4-Rewrite](https://github.com/Nilbong/COD4-Rewrite) | Call of Duty 4 multiplayer reimplemented in Rust on Bevy. Bring your own game files. | 19 | 🟢 | Rust |
| [jy-remake](https://github.com/scarsty/jy-remake) | Zgames制作的《金庸群侠传》复刻版 | 19 | 🟢 | C |
| [piney_apples](https://github.com/Toyz/piney_apples) | Native Rust port of the PS2 .hack engine from reverse engineering | 19 | 🟢 | Rust |
| [RPG-X](https://github.com/UberGames/rpgxEF) | A modifaction of ioEF with increased limits for RPG-X2, now including the gamecode | 19 | 🟢 | C |
| [T.O.R.E Fighters](https://github.com/john-overton/T.O.R.E-Fighters) | Reverse-engineered rebuild of Jane's Fighters Anthology flight sim | 19 | 🟢 | Rust |
| [zorkClone](https://github.com/vatbub/zorkClone) | Reimplementation of the original Zork game developed by Infocom. | 19 | 🔴 | Java |
| [Daikatana Restoration Project](https://github.com/atsb/daikatana-restoration-project) | Daikatana restoration aiming to have a clean 1.2 source and to support modern systems | 17 | 🟢 | C++ |
| [invaders (in C)](https://github.com/herrecito/invaders) | A Space Invaders / Intel 8080 emulator | 17 | 🔴 | C |
| [Octopus](https://github.com/roger-wetzel/Octopus) | Remake of Nintendo's Octopus Game & Watch device for Apple TV 4 | 17 | 🔴 | Swift |
| [Pokémon Red++](https://github.com/jayceekaycee/RedPlusPlus) | An upgrade to Pokémon Red. Fixes several bugs and adds a lot of new features. Now a standalone repository, so you can... | 17 | 🔴 | Assembly |
| [WoodyRE](https://github.com/jjmhalew/WoodyRE) | Engine reimplementation of Woody Woodpecker: Escape from Buzz Buzzard Park (PC, 2001) - plays the original game from... | 17 | 🟢 | C |
| [Arcanum on iOS](https://github.com/arcanum-project/game) | Engine reimplementation of Arcanum: Of Steamworks and Magick Obscura; uses original game data (C++) | 16 | 🔴 | C++ |
| [Castlekeep](https://github.com/leidav/Castlekeep) | Reimplementation of Stronghold 1 | 16 | 🔴 | C++ |
| [Desktop Adventures Engine for ScummVM](https://github.com/digitall/scummvm-deskadv) | Desktop Adventures Engine for ScummVM | 16 | 🔴 | C++ |
| [OpenOP2](https://github.com/OpenOP2/OpenOP2) | OpenOP2 is a re-implementation of the gameplay inspired by colony building games like Outpost 2, using the OpenRA eng... | 16 | 🟢 | C# |
| [Project ANISE](https://github.com/tomyun/anise) | 🦋 Project ANISE (A Newly Implemented Scripting Engine for AI5V) | 16 | 🔴 | C++ |
| [realice](https://github.com/FWGS/realice) | Heavy Metal F.A.K.K. 2 / American McGee's Alice reverse engineered. | 16 | 🟢 | C |
| [Command Series Engine](https://github.com/pwiecz/command_series) | Engine for playing Command Series games by Sid Meier/Microprose | 15 | 🟢 | Go |
| [Concilia Tower](https://github.com/Jonahss/concilia-tower) | Ground-up rewrite of SimTower (1994) from decompilation, playable in the browser | 15 | 🟢 | C |
| [ktes2](https://github.com/sonicretro/ktes2) | Knucles the Echidna in Sonic 2 | 15 | 🔴 | Assembly |
| [Minecraft: Pocket Edition (mcpe-engine)](https://github.com/BrentDaMage/mcpe-engine) | Reverse-engineered reimplementation / port of Minecraft: Pocket Edition (mcpe-engine) | 15 | 🟢 | C++ |
| [SFCDDISASM](https://github.com/ShiningForceCentral/SFCDDISASM) | A disassembly of the game "Shining Force CD" for documentation and fan-project purposes. | 15 | 🔴 | Assembly |
| [earth-shaker](https://github.com/Palevolg/earth-shaker) | Remake of an old ZX-spectrum game "EarthShaker" on Unity | 14 | 🔴 | C# |
| [OpenBound](https://github.com/WickedPeanuts/OpenBound) | This project aims to mimic the older PC versions of Gunbound with optimized behavior, engine and gameplay elements. T... | 14 | 🟡 | C# |
| [Zuma Portable](https://github.com/kyle-sylvestre/CircleShootApp) | Zuma Deluxe (1.0.0) decompilation ported to newer platforms | 14 | 🟢 | C++ |
| [Atari8bit_StarRaiders](https://github.com/sidneycadot/Atari8bit_StarRaiders) | A repository dedicated to reverse engineering the classic 1979 game Star Raiders for the Atari 400/800/XL/XE platform. | 13 | 🔴 | Assembly |
| [Cannon Fodder](https://github.com/krazyjakee/CannonFodder) | HTML5 Remake of an Amiga Classic | 13 | 🔴 | JavaScript |
| [mhlib](https://github.com/Theaninova/mhlib) | A project to make the old classic Moorhuhn Games playable on modern systems via an engine reimplementation, written i... | 13 | 🔴 | Rust |
| [Tile World 2](https://github.com/SicklySilverMoon/tworld) | The current fork of Tile World 2, including Qt6 support, and other game patches | 13 | 🟢 | C |
| [Ultima 5](https://github.com/synthwave-pixel/ultima5) | Modern engine for Ultima 5. | 13 | 🟢 | TypeScript |
| [Arkanum](https://github.com/vleon1/Arkanum) | Arcanum game engine recreation | 12 | 🔴 | Python |
| [DNF-reimposition](https://github.com/vini1264/DNF-Enhanced) | Set of gameplay enhancements for Duke Nukem Forever (2011) | 12 | 🔴 | C |
| [EF2GameSource](https://github.com/UberGames/EF2GameSource) | The original EF2GameSource updated so it compiles under Visual Studio 2012 and Linux | 12 | 🔴 | C++ |
| [erampage](https://github.com/ttyborg/erampage) | Automatically exported from code.google.com/p/erampage | 12 | 🔴 | C |
| [OpenKingdoms](https://github.com/OpenKingdoms/OpenKingdoms) | Open-source engine reimplementation of Total Annihilation: Kingdoms (C11, native + WebAssembly). Bring your own game... | 12 | 🟢 | C |
| [ReDMCSB](https://github.com/gondur/ReDMCSB_Release2) | ReDMCSB Release2 source code by Christophe Fontanel | 12 | 🔴 | Assembly |
| [remc1](https://github.com/turican0/remc1) | Recode Binary code of game Magic Carpet1 to C/C++ language(remake MC1 for any platform) | 12 | 🔴 | C++ |
| [SuperLemminiToo](https://github.com/Blazingstix/SuperLemminiToo) | My personal fork of SuperLemmini, which itself is a fork of Lemmini | 12 | 🔴 | Java |
| [Amber](https://github.com/Pyrdacor/Amber) | Engine for the Amber trilogy | 11 | 🟢 | C# |
| [openDOW](https://github.com/rofl0r/openDOW) | remake of the classic amiga game "dogs of war" (C) 1989 elite | 11 | 🟡 | C |
| [Plants vs. Zombies GOTY (re-plants-vs-zombies)](https://github.com/Bamcane/re-plants-vs-zombies) | Reverse-engineered reimplementation / port of Plants vs. Zombies GOTY (re-plants-vs-zombies) | 11 | 🟢 | C++ |
| [X-Settlers](https://github.com/skarmux/x-settlers) | Re-implementation of classic "TheSettlers" game series using modern technologies like hardware accelerated graphics a... | 11 | 🔴 | C++ |
| [DCSpeedBall2](https://github.com/LemonHaze420/DCSpeedBall2) | SpeedBall 2 for Pocket PC/Dreamcast (WCE), with special thanks to Comby Laurent and LemonHaze | 10 | 🔴 | C++ |
| [gta1_re](https://github.com/CriminalRETeam/gta1_re) | Engine reimplementation of Grand Theft Auto; uses original game data (C++) | 10 | 🟢 | C++ |
| [Heart of the Alien Redux](https://github.com/carstene1ns/hota-redux) | Heart of The Alien - Redux (forked from https://hota.sf.net) | 10 | 🟢 | C |
| [sm64js](https://github.com/sm64jsarchive/sm64jsarchive) | Super Mario 64 reimplementation in JavaScript. | 10 | 🟡 | JavaScript |
| [dizgruntled-java](https://github.com/Hugheth/dizgruntled-java) | A java open source remake of Monolith Gruntz (1999) | 9 | 🔴 | Java |
| [ebbsrc](https://github.com/Herringway/ebbsrc) | earthbound beginnings source recreation | 9 | 🟡 | Assembly |
| [firestaff](https://github.com/yeager/firestaff) | 🔥 Source-faithful Dungeon Master engine — DM1, CSB, DM2, DM Nexus and Theron's Quest on modern hardware. macOS, Windo... | 9 | 🟢 | C |
| [olduvai](https://github.com/ksokolowski/olduvai) | From-scratch C++/SDL2 reimplementation of the Prehistorik (1991) engine — bring your own game files. | 9 | 🟢 | C++ |
| [opendaed](https://github.com/AMDmi3/opendaed) | Libre reimplementation of The Daedalus Encounter game | 9 | 🔴 | C++ |
| [Powerslide remake](https://github.com/dm999/powerslideremake) | Project remakes main features of video game Powerslide | 9 | 🟢 | C++ |
| [re3-Resurrected](https://github.com/cinchitsolutions/re3-Resurrected) | Clean-room reverse engineering of GTA III / Vice City for PC | 9 | 🟡 | C++ |
| [rust-theft-auto](https://github.com/gaudecker/rust-theft-auto) | Grand Theft Auto engine reimplementation in Rust | 9 | 🔴 | Rust |
| [Chuckie-Egg](https://github.com/pbrook/Chuckie-Egg) | Reverse-engineered Chuckie Egg with ASCII and 3D renderers | 8 | 🔴 | C |
| [LibertyFlux](https://github.com/monstercameron/LibertyFlux) | GTA IV engine rewritten in Rust function by function by AI agents for Windows x64 and ARM | 8 | 🟢 | Rust |
| [Lupin Sansei - Pandora no Isan](https://github.com/PavelSha/Lupin-Sansei---Pandora-no-Isan) | An annotated disassembly of the famicom game "Lupin Sansei - Pandora no Isan" (1987). | 8 | 🟢 | Assembly |
| [Prehistorik_js](https://github.com/cyxx/prehistorik_js) | Prehistorik (Demo) engine reimplementation (Emscripten, SDL2) | 8 | 🗄️ | C |
| [rustyworld](https://github.com/EdMcBane/rustyworld) | Frame-accurate Another World engine reimplementation in Rust | 8 | 🟡 | Rust |
| [WAGE](https://github.com/asvitkine/wage-engine) | World Builder game engine | 8 | 🔴 | Java |
| [Balloon Fight](https://github.com/MikeDX/balloon-fight) | Remake of Balloon fight by Groovy Gecko, created for the Retro Remakes competition 2003 | 7 | 🔴 | xBase |
| [chaos-head](https://github.com/FGRE/chaos-head) | Reimplementation of Chaos;Head visual novel | 7 | 🔴 | CMake |
| [Cut the Rope](https://github.com/Bingies24/cuttherope-dx) | Reverse-engineered reimplementation / port of Cut the Rope | 7 | 🟢 | C# |
| [Dungeon Strikes Back](https://github.com/sparkletwist/DSB) | Dungeon Strikes Back | 7 | 🟡 | C |
| [Megaman3NESRecomp](https://github.com/mstan/Megaman3NESRecomp) | Mega Man 3 recompiled for the NES using nesrecomp · Part of the R.A.I.D. community | 7 | 🟢 | C |
| [Minecraft-4K-Decompilation](https://github.com/CelestialAmber/Minecraft-4K-Decompilation) | Decompilation of Minecraft 4K, updated to be a regular application | 7 | 🟢 | Java |
| [Ozymandias](https://github.com/Banderi/Ozymandias) | An open source re-implementation of Pharaoh (1999)'s game engine in Godot 3.6 | 7 | 🟢 | GDScript |
| [re3bevy](https://github.com/imbevystar/re3bevy) | Unofficial GTA III reimplementation in Rust with the Bevy engine and ECS | 7 | 🟢 | Rust |
| [sims-3-bevy](https://github.com/Eamo5/sims-3-bevy) | Work-in-progress reimplementation of The Sims 3 in the Bevy game engine | 7 | 🟢 | Rust |
| [Starfox 64: Recompiled](https://github.com/worleydl/Starfox64Recomp-uwp) | Static recompilation of Starfox 64 for PC (Windows/Linux) (Unofficial UWP) | 7 | 🟢 | C |
| [SuperStarTrek25thGMS](https://github.com/JeodC/SuperStarTrek25thGMS) | A port of Super Star Trek Meets 25th Anniversary to Game Maker Studio 2 | 7 | 🟢 | Game Maker Language |
| [th10](https://github.com/YomotsuHisami/th10) | A high-fidelity, portable reimplementation of 東方風神録 ～ Mountain of Faith ver 1.00a. | 7 | 🟢 | C++ |
| [timeco](https://github.com/LBALab/timeco) | Time Commando Reimplementation | 7 | 🟢 | C |
| [jy2-copy](https://github.com/MngYou/jy2-copy) | Engine reimplementation of Heroes of Jin Yong 2; uses original game data (JavaScript) | 6 | 🔴 | JavaScript |
| [OpenJill](https://github.com/emeric-martineau/openjill) | Official OpenJill project source repository to understand how Jill of the Jungle game engine work and rewrite it in J... | 6 | 🗄️ | Java |
| [rechelon](https://github.com/pkulev/rechelon) | Echelon: free engine reimplementation | 6 | 🔴 | C# |
| [remc1hw](https://github.com/turican0/remc1hw) | Recode Binary code of game/datadisk Magic Carpet1 Hidden Words to C/C++ language(remake MC1 for any platform) | 6 | 🔴 | C++ |
| [retruxx](https://github.com/mindflower/retruxx) | Reverse engineered Hard Truck Apocalypse. | 6 | 🟢 | C++ |
| [scale-miniatures](https://github.com/hivvu/scale-miniatures) | Micro Machines (PC, 1994) rewritten in TypeScript from the disassembly, running natively in the browser. No emulator.... | 6 | 🟢 | TypeScript |
| [sm_rewrite](https://github.com/enderandrew/sm_rewrite) | Super Metroid rewrite project | 6 | 🟡 | C |
| [TetrisGBRecomp](https://github.com/mstan/TetrisGBRecomp) | Tetris recompiled for the Game Boy using a fork of gb-recompiled · Part of the R.A.I.D. community | 6 | 🟢 | C |
| [The Bard's Tale III](https://github.com/Drunella/bt3-easyflash) | Bard's Tale III Easyflash Version | 6 | 🔴 | C |
| [TsumuLightRecomp](https://github.com/mstan/TsumuLightRecomp) | Tsumu Light (Japan) recompiled for the Sony PlayStation using psxrecomp, with an English fan-translation · Part of th... | 6 | 🟢 | PowerShell |
| [wanderer](https://github.com/vinceh121/wanderer) | A reimplementation of the 2002 video game Project Nomads by Radon Labs | 6 | 🟢 | Java |
| [demcstify](https://github.com/stevefan1999-personal/demcstify) | Decompiles Minecraft with Vineflower and reconstructs code with an LLM | 5 | 🟢 | Shell |
| [open-northland](https://github.com/s-nems/open-northland) | A modern, open-source reimplementation of the Cultures game series | 5 | 🟢 | TypeScript |
| [openpol](https://github.com/jstasiak/openpol) | An open source reimplementation of the first Polish RTS video game Polanie (also known as VICTORY, OSADNICI) | 5 | 🟡 | Rust |
| [RetroLemmini](https://github.com/Willicious/RetroLemmini) | A newly-maintained version of Lemmini | 5 | 🟢 | Java |
| [hugo.js](https://github.com/cyxx/hugo_js) | Hugo pa Nye Eventyr/Hugo Délire player (Emscripten) | 4 | 🗄️ | C |
| [Jet-Story](https://github.com/adamenkov/jet-story) | Remake of the ZX Spectrum game "Jet-Story" | 4 | 🟢 | Assembly |
| [lilium-salvation](https://github.com/clover-moe/lilium-salvation) | An engine replacement for Dark Salvation | 4 | 🟢 | C |
| [Marble Love](https://github.com/magno73/marble-love) | TypeScript reimplementation of Atari's Marble Madness (1984), incl. Slapstic behaviour | 4 | 🟢 | TypeScript |
| [mb-decomp](https://github.com/Yoshimaster96/mb-decomp) | Engine reimplementation of Super Monkey Ball; uses original game data (C, Assembly) | 4 | 🔴 | C |
| [Soul Blazer (RustyBlazer)](https://github.com/hellow554/RustyBlazer) | Reverse-engineered reimplementation / port of Soul Blazer (RustyBlazer) | 4 | 🟡 | Assembly |
| [SuperFoulEgg](https://github.com/ant512/SuperFoulEgg) | Port of Super Foul Egg to MacOSX. | 4 | 🔴 | Objective-C |
| [Trashman](https://github.com/pobtastic/trashman) | A disassembly of Trashman, created using SkoolKit. | 4 | 🟡 | Visual Basic 6.0 |
| [v64tng](https://github.com/mattseabrook/v64tng) | Game Engine re-creation of The 7th Guest | 4 | 🟢 | Assembly |
| [xclannad](https://github.com/weimingtom/xclannad_fork) | My xclannad fork for study | 4 | 🔴 | C |
| [FFED3D](https://github.com/corpsofengineers/ffed3d) | Automatically exported from code.google.com/p/ffed3d | 3 | 🔴 | Assembly |
| [GumshoeNESRecomp](https://github.com/mstan/GumshoeNESRecomp) | Gumshoe recompiled for the NES using nesrecomp · Part of the R.A.I.D. community | 3 | 🟢 | C |
| [kys-promise](https://github.com/scarsty/kys-promise) | Engine reimplementation of Heroes of Jin Yong; uses original game data (Pascal) | 3 | 🟢 | Pascal |
| [LostVikings](https://github.com/akaWolf/LostVikings) | Translated and rewritten DOS version of Lost Vikings | 3 | 🟢 | C++ |
| [Oblivion-Reconstructed](https://github.com/themuffinator/Oblivion-Reconstructed) | Reverse-engineered Oblivion Extension Pack source code for original Quake II. | 3 | 🟢 | C |
| [S2HD](https://github.com/SonicOrcaModding/S2HD) | A decompile of Sonic 2 HD (Build 2.0.1012-rc2) and port to Linux, Android and iOS. | 3 | 🟢 | C# |
| [SF1RE](https://github.com/ShiningForceCentral/SF1RE) | Collaborative work on reverse-engineering Shining Force. | 3 | 🟡 | C |
| [Another World for the Commander X16](https://github.com/cosmicr/anotherx16) | Commander X16 Port of the Amiga Game Another World | 2 | 🟢 | Assembly |
| [Hopmon (OpenHopmon)](https://github.com/Teofil98/OpenHopmon) | Reverse-engineered reimplementation / port of Hopmon (OpenHopmon) | 2 | 🟢 | C++ |
| [MechCommander2HD](https://github.com/Ariemeth/MechCommander2HD) | Pending approval, this will be the place where the HD revamp will be tracked. | 2 | 🔴 | C++ |
| [Open76](https://github.com/rob518183/Open76) | Interstate '76 engine reimplementation | 2 | 🟢 | C# |
| [Ozymandias](https://github.com/dalerank/Ozymandias) | An open source re-implementation of Pharaoh in the Julius/Augustus engine. | 2 | 🟡 |  |
| [Quarantine](https://github.com/mattseabrook/Quarantine) | Game Engine re-creation of Quarantine by Imagexcel | 2 | 🟢 |  |
| [SITDDISASM](https://github.com/ShiningForceCentral/SITDDISASM) | A disassembly of the game "Shining in the Darkness" for documentation and fan-project purposes. | 2 | 🟡 | Assembly |
| [Super Star Trek meets 25th Anniversary](https://github.com/emabolo/sst25th) | source code of Super Star Trek 1978 meets 25th Anniversary | 2 | 🟡 | AGS Script |
| [tetris_nes](https://github.com/sanghoonio/nes-tetris) | NES Tetris decompiled and rebuilt in readable Rust | 2 | 🟢 | Rust |
| [Travel With Trashman](https://github.com/pobtastic/travelwithtrashman) | A disassembly of Travel With Trashman, created using SkoolKit. | 2 | 🟡 | Visual Basic 6.0 |
| [ult3src](https://github.com/gondur/ult3src) | ultima 3 exodus reverse enigneered by Sven Carlberg for GBC http://sven.50webs.org/ultima3.html | 2 | 🔴 | C |
| [Uplink](https://github.com/AdrUlb/Uplink) | Decompilation of Uplink by Introversion Software (GOG Linux version, installer gog_uplink_hacker_elite_2.0.0.4.sh) | 2 | 🟢 | C++ |
| [xkanon](https://github.com/weimingtom/xkanon_fork) | My fork of xkanon | 2 | 🔴 | C |
| [Chameleon Twist 2: Recompiled](https://github.com/Rainchus/ChameleonTwist2-JP-Recomp) | Engine reimplementation of Chameleon Twist 2; uses original game data (C++) | 1 | 🟡 | C |
| [earthbound_beginnings](https://github.com/Herringway/earthbound_beginnings) | Unfinished port of Earthbound Beginnings | 1 | 🟢 | D |
| [EarthShakerDS](https://github.com/ant512/EarthShakerDS) | Port of the classic ZX Spectrum game Earth Shaker to the Nintendo DS. | 1 | 🔴 | C++ |
| [ff1snes](https://github.com/Entroper/ff1snes) | FF1 for SNES, written from scratch. | 1 | 🟡 | Assembly |
| [NHL94](https://github.com/abdulahmad/NHL94Genesis) | Work In Progress reverse engineered source of NHL 94 for Sega Genesis. Requires original ROM file to build. | 1 | 🟢 | Assembly |
| [PanzerMortyr](https://github.com/Panzerschrek/PanzerMortyr) | Reimplementation of the Mortyr 2093-1944 game engine | 1 | 🟢 | GLSL |
| [Quake4Doom](https://github.com/Kasreyn/Quake4Doom) | Engine reimplementation of Quake 4; uses original game data (C++) | 1 | 🟡 | C++ |
| [Soul Reaverse](https://github.com/Mc-muffin/kain2-splatdisasm) | Engine reimplementation of Legacy of Kain: Soul Reaver; uses original game data (C) | 1 | 🟡 | C |
| [StawdewValley](https://github.com/E-riCA0/StawdewValley) | Decompiled Stardew Valley source code | 1 | 🔴 | C# |
| [1oom](https://gitlab.com/KilgoreTroutMaskReplicant/1oom) | Engine reimplementation of Master of Orion; uses original game data (C) |  | ⚪ |  |
| [2ooM](https://sourceforge.net/projects/toom/) | Engine reimplementation of Master of Orion 2; uses original game data (C++, C) |  | ⚪ |  |
| [AGE](https://github.com/weimingtom/air-galgame-engine) | Automatically exported from code.google.com/p/air-galgame-engine | 0 | 🔴 | ActionScript |
| [Blake4SDL](https://bitbucket.org/ks-presto/blake4sdl) | Engine reimplementation of Blake Stone: Planet Strike, Blake Stone: Aliens of Gold; uses original game data (C) |  | ⚪ |  |
| [BloodGDX](https://gitlab.com/m210/BloodGDX) | Engine reimplementation of Blood; uses original game data (Java) |  | ⚪ |  |
| [bumpy-reverse](https://github.com/GeReV/bumpy-reverse) | Decompilation of Bumpy's Arcade Fantasy, lead by Claude | 0 | 🟢 | C |
| [djavul](https://github.com/Happy-Ferret/djavul) | An open source reference re-implementation of the Diablo 1 game engine (work in progress). | 0 | 🔴 | Go |
| [DMOE](https://sourceforge.net/projects/dmle/) | Engine reimplementation of Dungeon Master; uses original game data (C) |  | ⚪ |  |
| [Dragonball Z 3: Killer Androids ASM Source Code](https://www.romhacking.net/documents/312/) | Engine reimplementation of Dragon Ball Z III: Ressen Jinzō Ningen; uses original game data (Assembly) |  | ⚪ |  |
| [Dragonball Z Gaiden: Plan to Eliminate the Saiyans Source Code](https://www.romhacking.net/documents/319/) | Engine reimplementation of Dragon Ball Z Side Story: Plan to Eradicate the Saiyans; uses original game data |  | ⚪ |  |
| [Dragonball Z: Assault of the Saiyans Source Code](https://www.romhacking.net/documents/313/) | Engine reimplementation of Dragon Ball Z: Kyōshū! Saiyajin; uses original game data (Assembly) |  | ⚪ |  |
| [FreeCS](https://sourceforge.net/projects/freecs-1-5/) | Free-software re-implementation of Counter-Strike 1.5 running on the FTEQW engine. |  | ⚪ |  |
| [FreeSynd](https://sourceforge.net/projects/freesynd/) | Engine reimplementation of Syndicate; uses original game data (C++) |  | ⚪ |  |
| [FTEQW](https://fte.triptohell.info/) | FPS Engine for Quake 1, QuakeWorld, Quake 2, Hexen II & Quake III Arena. |  | ⚪ |  |
| [glFFE](https://web.archive.org/web/20211123060910/https://nic.dnsalias.com/FFE.html) | Engine reimplementation of Elite III; uses original game data (C, Assembly) |  | ⚪ |  |
| [HELLRAIDER](https://github.com/ergonomy-joe/HELLRAIDER) | MS-DOS version of the game HELLRAIDER, disassembled, ready for build ! | 0 | 🔴 | Assembly |
| [jminequest](https://codeberg.org/glowiak/jminequest) | ) - A Java reimplementation of the 2014 mobile game Mine Quest by Tapps Tecnologia da Informacao Ltda |  | ⚪ |  |
| [LastNinja](https://sourceforge.net/projects/lastninja/) | Engine reimplementation of The Last Ninja; uses original game data (C++) |  | ⚪ |  |
| [Leaflitter](https://codeberg.org/Ivylag/leaflitter) | Engine reimplementation of Paper Mario: Sticker Star; uses original game data (C++) |  | ⚪ |  |
| [Leftovers Decomp](https://github.com/Koichive/Leftovers-Old) | The old version of our Leftovers decompile. This was in collaboration with me & FreddySP. | 0 | 🟢 | ShaderLab |
| [Lemmini](https://bitbucket.org/fade0ff/lemmini) | Engine reimplementation of Lemmings; uses original game data (Java) |  | ⚪ |  |
| [LibDay](https://github.com/gitter-badger/LibDay) | Liberation Day remake from 1998 | 0 | 🔴 | C# |
| [Loap](https://bitbucket.org/namida42/loap/) | Engine reimplementation of 3D Lemmings; uses original game data (C#) |  | ⚪ |  |
| [LSPGDX](https://gitlab.com/m210/LSPGDX) | Engine reimplementation of Rock'n Shaolin: Legend of Seven Paladins 3D; uses original game data (Java) |  | ⚪ |  |
| [Minosoft](https://gitlab.bixilon.de/bixilon/minosoft) | Engine reimplementation of Minecraft; uses original game data (Kotlin) |  | ⚪ |  |
| [New RAW](https://sourceforge.net/projects/newraw/) | Engine reimplementation of Another World; uses original game data (C++) |  | ⚪ |  |
| [NHLPA93Genesis](https://github.com/abdulahmad/NHLPA93Genesis) | Work In Progress reverse engineered source of NHLPA Hockey 93 for Sega Genesis. Requires original ROM file to build. | 0 | 🟢 | Assembly |
| [opene2140](https://gitlab.com/opene2140/opene2140) | Engine reimplementation of Earth 2140; uses original game data (C++) |  | ⚪ |  |
| [OpenLRR](https://github.com/vs49688/OpenLRR) | An open source re-implementation of LEGO Rock Raiders | 0 | 🟢 | C++ |
| [OpenRW](https://openrw.org/) | A cross-platform, open source re-implementation of Rockstar Games' Grand Theft Auto III. |  | ⚪ |  |
| [Ordoor](https://code.ur.gs/lupine/ordoor) | Engine reimplementation of Warhammer 40,000: Chaos Gate; uses original game data (Go) |  | ⚪ |  |
| [Phavon](https://sourceforge.net/projects/phavon/) | Engine reimplementation of Xenon 2 Megablast; uses original game data (C) |  | ⚪ |  |
| [PowerslaveGDX](https://gitlab.com/m210/PowerslaveGDX) | Engine reimplementation of Powerslave; uses original game data (Java) |  | ⚪ |  |
| [Project Aedra](https://sourceforge.net/projects/aedra/) | Engine reimplementation of The Elder Scrolls III: Morrowind; uses original game data (C++, C) |  | ⚪ |  |
| [RedneckGDX](https://gitlab.com/m210/RedneckGDX) | Engine reimplementation of Redneck Rampage; uses original game data (Java) |  | ⚪ |  |
| [RVGL](https://rvgl.org/) | Cross-platform engine for Re-Volt. |  | ⚪ |  |
| [Scheddy Kong Racing](https://gitlab.com/ryandwyer/scheddy-kong-racing) | Engine reimplementation of Diddy Kong Racing; uses original game data (Assembly, C) |  | ⚪ |  |
| [SITDRE](https://github.com/ShiningForceCentral/SITDRE) | Collaborative work on reverse-engineering Shining in the Darkness. | 0 | 🟡 | C |
| [soniccdrespinned](https://git.sr.ht/~benoitren/soniccdrespinned) | Engine reimplementation of Sonic CD; uses original game data (C) |  | ⚪ |  |
| [Super Mario 68K](http://tifreakware.net/lachprog/dold.htm) | Engine reimplementation of Super Mario Bros.; uses original game data (C) |  | ⚪ |  |
| [Super-Mario-Bros-Java](https://sourceforge.net/projects/super-mario-bros-java/) | Engine reimplementation of Super Mario Bros.; uses original game data (Java) |  | ⚪ |  |
| [supercopter_decompiled](https://github.com/ergonomy-joe/supercopter_decompiled) | Engine reimplementation of Supercopter; uses original game data (Pascal) | 0 | 🟡 | Pascal |
| [SuperLemmini](https://www.lemmingsforums.net/index.php?topic=1793.0) | Engine reimplementation of Lemmings; uses original game data (Java) |  | ⚪ |  |
| [The Crystal Scrolls](https://sourceforge.net/projects/crystalscrolls/) | Engine reimplementation of The Elder Scrolls III: Morrowind; uses original game data (C++) |  | ⚪ |  |
| [The System Shock Hack Project](https://sourceforge.net/projects/tsshp/) | Engine reimplementation of System Shock, Ultima Underworld; uses original game data (C++) |  | ⚪ |  |
| [Thunder Force IV Rebirth](https://github.com/Fissuras/tf4r) | Automatically exported from code.google.com/p/tf4r | 0 | 🔴 | ASP |
| [Transfusion](https://sourceforge.net/projects/blood/) | Engine reimplementation of Blood; uses original game data (QuakeC, C) |  | ⚪ |  |
| [Wages of War](https://github.com/suhteevah/wages-of-war) | A clean-room, open-source Rust reverse enginering of the Wages of War: The Business of Battle (1996) engine. | 0 | 🟢 | Rust |
| [WayneGretzky3dHockey](https://github.com/Rainchus/WayneGretzky3dHockey) | Decomp of wayne gretzky hockey for the n64 | 0 | 🔴 | C |
| [Wing Commander 1 Reloaded](https://wingcomreloaded.itch.io/wingcommander1reloaded) | Modern recreation of Wing Commander I. |  | ⚪ |  |
| [Winter Jumper](https://os4depot.net/?function=showfile&file=game/platform/winterjumper.lha) | Engine reimplementation of The Great Giana Sisters; uses original game data (C++) |  | ⚪ |  |

## Game Network Protocols & APIs

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [mineflayer](https://github.com/PrismarineJS/mineflayer) | High-level JavaScript API for creating Minecraft bots | 7,577 | 🟢 | JavaScript |
| [Geyser](https://github.com/GeyserMC/Geyser) | Proxy translating Minecraft Bedrock clients to Java Edition servers | 5,902 | 🟢 | Java |
| [Hearthstone Deck Tracker](https://github.com/HearthSim/Hearthstone-Deck-Tracker) | Deck tracker for Hearthstone on Windows that reads game logs and memory | 4,922 | 🟢 | C# |
| [Velocity](https://github.com/PaperMC/Velocity) | High-performance Minecraft Java proxy server | 2,272 | 🟢 | Java |
| [Minecraft Console Client](https://github.com/MCCTeam/Minecraft-Console-Client) | Lightweight console Minecraft client for chat and automated scripts | 2,161 | 🟢 | C# |
| [Deceive](https://github.com/molenzwiebel/Deceive) | XMPP proxy that lets you appear offline in League of Legends, VALORANT and LoR | 1,728 | 🟢 | C# |
| [ViaVersion](https://github.com/ViaVersion/ViaVersion) | Lets newer Minecraft clients connect to older server versions by translating packets | 1,643 | 🟢 | Java |
| [OpenKore](https://github.com/OpenKore/openkore) | Open-source custom client and automation tool for Ragnarok Online | 1,530 | 🟢 | Perl |
| [node-minecraft-protocol](https://github.com/PrismarineJS/node-minecraft-protocol) | Parse and serialize Minecraft Java packets, with auth and encryption | 1,421 | 🟢 | JavaScript |
| [HSTracker](https://github.com/HearthSim/HSTracker) | Hearthstone deck tracker for macOS | 1,257 | 🟢 | Swift |
| [node-steam](https://github.com/seishun/node-steam) | Interface directly with Steam CM servers from Node.js (archived) | 999 | 🗄️ | JavaScript |
| [go-mc](https://github.com/Tnze/go-mc) | Collection of Go libraries for the Minecraft Java protocol and data formats | 982 | 🟢 | Go |
| [GameTracking-CS2](https://github.com/SteamTracking/GameTracking-CS2) | Automated tracking of Counter-Strike 2 game file, string and protobuf changes | 968 | 🟢 | Slang |
| [minecraft-data](https://github.com/PrismarineJS/minecraft-data) | Language-independent Minecraft protocol and game data for clients, servers and libraries | 952 | 🟢 | JavaScript |
| [MCProtocolLib](https://github.com/GeyserMC/MCProtocolLib) | Java library for Minecraft Java client/server protocol communication | 908 | 🟢 | Java |
| [pyCraft](https://github.com/ammaraskar/pyCraft) | Minecraft Java client networking library in Python | 847 | 🟡 | Python |
| [NintendoClients](https://github.com/kinnay/NintendoClients) | Python package to communicate with Switch, Wii U and 3DS servers | 763 | 🟢 | Python |
| [steampy](https://github.com/bukson/steampy) | Python Steam trading library using Steam's internal web endpoints | 667 | 🟡 | Python |
| [ViaProxy](https://github.com/ViaVersion/ViaProxy) | Standalone proxy translating between Minecraft protocol versions, including Bedrock and classic | 660 | 🟢 | Java |
| [steam-tradeoffer-manager](https://github.com/DoctorMcKay/node-steam-tradeoffer-manager) | Node.js Steam trade offer management library | 606 | 🟢 | JavaScript |
| [valorant-api-docs](https://github.com/techchrism/valorant-api-docs) | Documentation for internal VALORANT client API endpoints | 593 | 🟡 | TypeScript |
| [SteamTracking Protobufs](https://github.com/SteamTracking/Protobufs) | Auto-tracked protobuf definitions extracted from Steam, CS2, Dota 2, Deadlock and TF2 | 586 | 🟢 | Shell |
| [node-steamcommunity](https://github.com/DoctorMcKay/node-steamcommunity) | Node.js module to interact with Steam Community web interfaces | 578 | 🟢 | JavaScript |
| [gophertunnel](https://github.com/Sandertv/gophertunnel) | Go library for Minecraft Bedrock Edition networking, clients and proxies | 575 | 🟢 | Go |
| [unofficial-valorant-api](https://github.com/Henrik-3/unofficial-valorant-api) | Unofficial VALORANT API built on the in-game API endpoints | 560 | 🟢 | JavaScript |
| [bedrock-protocol](https://github.com/PrismarineJS/bedrock-protocol) | Minecraft Bedrock protocol library with authentication and encryption | 485 | 🟢 | JavaScript |
| [Fortnite Endpoints Documentation](https://github.com/LeleDerGrasshalmi/FortniteEndpointsDocumentation) | Unofficial documentation of Fortnite and Epic Games API endpoints | 483 | 🟢 |  |
| [go-steam](https://github.com/Philipp15b/go-steam) | Steam's network protocol implemented in Go for automation without a Steam client | 434 | 🟡 | Go |
| [psn-api](https://github.com/achievements-app/psn-api) | JavaScript library to get trophy, user and game data from the PlayStation Network | 427 | 🟢 | TypeScript |
| [EpicResearch](https://github.com/MixV2/EpicResearch) | Research and documentation of Epic Games' undocumented APIs | 425 | 🟡 |  |
| [Cloudburst Protocol](https://github.com/CloudburstMC/Protocol) | Java protocol library for Minecraft Bedrock Edition | 418 | 🟢 | Java |
| [prismarine-viewer](https://github.com/PrismarineJS/prismarine-viewer) | Web-based 3D viewer for Minecraft servers and bots | 397 | 🟢 | JavaScript |
| [NSO-RPC](https://github.com/MCMi460/NSO-RPC) | Shows Nintendo Switch playing status in Discord using the Nintendo Switch Online app API | 384 | 🟡 | Python |
| [psn-php](https://github.com/Tustin/psn-php) | PHP wrapper for the PlayStation Network API | 374 | 🟢 | PHP |
| [node-globaloffensive](https://github.com/DoctorMcKay/node-globaloffensive) | Node.js client for the CS2 game coordinator protocol | 367 | 🟢 | JavaScript |
| [gumer-psn](https://github.com/jhewt/gumer-psn) | PlayStation Network API written in Node.js | 348 | 🗄️ | JavaScript |
| [splatnet2statink](https://github.com/frozenpandaman/splatnet2statink) | Fetches Splatoon 2 battle data from the SplatNet 2 app API and uploads to stat.ink | 344 | 🟡 | Python |
| [rustplus.js](https://github.com/liamcottle/rustplus.js) | Unofficial Node.js library for the Rust+ companion protocol | 322 | 🟢 | JavaScript |
| [GameTracking](https://github.com/SteamTracking/GameTracking) | Automated dumps of Valve game files and protos to track changes | 307 | 🟢 | Shell |
| [RiiConnect24 Patcher](https://github.com/KcrPL/RiiConnect24-Patcher) | Patches Wii channels to use RiiConnect24's revived WiiConnect24 services | 306 | 🟢 | Batchfile |
| [api](https://github.com/helldivers-2/api) | Community API for Helldivers 2 game data | 297 | 🟢 | C# |
| [python-hearthstone](https://github.com/HearthSim/python-hearthstone) | Hearthstone Python library: card defs, DBF, enums and log parser | 277 | 🟢 | Python |
| [steam-totp](https://github.com/DoctorMcKay/node-steam-totp) | Node.js generator for Steam Guard mobile TOTP codes and confirmation keys | 257 | 🔴 | JavaScript |
| [steam.py](https://github.com/Gobot1234/steam.py) | Async Python wrapper for the Steam API and Steam CM protocol | 239 | 🟢 | Python |
| [Inkay](https://github.com/PretendoNetwork/Inkay) | Wii U Aroma plugin that patches the console to use Pretendo Network servers | 232 | 🟢 | C++ |
| [rustplus-desktop](https://github.com/Pronwan/rustplus-desktop) | Unofficial Rust+ desktop app | 214 | 🟢 | C# |
| [steam-session](https://github.com/DoctorMcKay/node-steam-session) | Node.js module implementing Steam's auth server login to obtain refresh and web tokens | 199 | 🟢 | TypeScript |
| [go-dota2](https://github.com/paralin/go-dota2) | Go client for the Dota 2 game coordinator protocol | 183 | 🟢 | Go |
| [BedrockProtocol](https://github.com/pmmp/BedrockProtocol) | PHP implementation of the Minecraft Bedrock network protocol | 177 | 🗄️ | PHP |
| [slippi-js](https://github.com/project-slippi/slippi-js) | JavaScript parser for Super Smash Bros. Melee Slippi replay files | 168 | 🟢 | TypeScript |
| [GOG DB](https://github.com/Yepoleb/gogdb) | Website and scraper collecting GOG game data from GOG's internal APIs | 164 | 🟢 | Python |
| [LCU and Riot Client API docs](https://github.com/KebsCS/lcu-and-riotclient-api) | Documentation of League of Legends LCU and Riot Client local API endpoints | 160 | 🟢 | HTML |
| [psn-api (Python)](https://github.com/mgp25/psn-api) | PlayStation Network API client in Python | 134 | 🗄️ | Python |
| [squid-tracks](https://github.com/hymm/squid-tracks) | Unofficial desktop client for Nintendo SplatNet 2 | 134 | 🔴 | JavaScript |
| [csgo (python)](https://github.com/ValvePython/csgo) | Python module to interact with the CS:GO game coordinator | 133 | 🔴 | Python |
| [SteamWebPipes](https://github.com/xPaw/SteamWebPipes) | Pipes Steam PICS changelist events to websockets using SteamKit | 133 | 🗄️ | C# |
| [lcu-driver](https://github.com/sousa-andre/lcu-driver) | Python interface for the League of Legends client local API | 123 | 🟡 | Python |
| [lcu-connector](https://github.com/Pupix/lcu-connector) | Node.js connector for the League of Legends client (LCU) local API | 116 | 🟢 | JavaScript |
| [ShinraMeter](https://github.com/neowutran/ShinraMeter) | TERA DPS meter based on decoded game packets | 115 | 🟡 | C# |
| [xboxlive-auth](https://github.com/XboxReplay/xboxlive-auth) | Xbox Live authentication library for Node.js | 115 | 🟢 | TypeScript |
| [valorant.js](https://github.com/liamcottle/valorant.js) | Unofficial Node.js library for the VALORANT client API | 111 | 🟡 | JavaScript |
| [xbox-smartglass-nano-python](https://github.com/OpenXbox/xbox-smartglass-nano-python) | Python implementation of the Xbox One NANO game-streaming protocol | 104 | 🗄️ | Python |
| [nex-go](https://github.com/PretendoNetwork/nex-go) | Go implementation of Nintendo's PRUDP/NEX game server protocol for Pretendo | 102 | 🟢 | Go |
| [axie-graphql-documentation](https://github.com/ShaneMaglangit/axie-graphql-documentation) | Unofficial documentation of Axie Infinity's GraphQL endpoint | 97 | 🗄️ | JavaScript |
| [openspy-client](https://github.com/anzz1/openspy-client) | Patch for old PC games replacing defunct GameSpy services with OpenSpy | 97 | 🟢 | C |
| [Agar.io-Reverse-Engineering](https://github.com/DnAp/Agar.io-Reverse-Engineering) | Agar.io protocol reverse engineering | 96 | 🗄️ | JavaScript |
| [python-screeps](https://github.com/screepers/python-screeps) | Python client for the unofficial Screeps API | 91 | 🟢 | Python |
| [runescape-api](https://github.com/Astrect/runescape-api) | Node.js library for RuneScape and Old School unofficial API endpoints | 86 | 🟢 | TypeScript |
| [HearthDb](https://github.com/HearthSim/HearthDb) | .NET Hearthstone card database extracted from game data | 80 | 🟢 | C# |
| [prismarine-auth](https://github.com/PrismarineJS/prismarine-auth) | Microsoft/Xbox Live authentication flow for Minecraft clients | 77 | 🟢 | JavaScript |
| [xbox-smartglass-core-python](https://github.com/OpenXbox/xbox-smartglass-core-python) | Python implementation of the Xbox One SmartGlass core protocol | 75 | 🗄️ | Python |
| [FFXIVOpcodeWizard](https://github.com/karashiiro/FFXIVOpcodeWizard) | Automated Final Fantasy XIV network opcode discovery | 68 | 🔴 | C# |
| [MoeXCOM](https://github.com/hdk5/MoeXCOM) | Reverse engineering Blue Archive | 67 | 🔴 | C# |
| [node-haxball](https://github.com/wxyz-abcd/node-haxball) | API to build Haxball clients and bots via its reversed protocol | 63 | 🟢 | JavaScript |
| [Haruki-Sekai-API](https://github.com/Team-Haruki/Haruki-Sekai-API) | Unofficial API proxy for Project Sekai game data | 62 | 🟢 | Rust |
| [rlapi](https://github.com/dank/rlapi) | Reverse engineered Rocket League internal HTTP and WebSocket API | 59 | 🟢 | Go |
| [pyremoteplay](https://github.com/ktnrg45/pyremoteplay) | Python library implementing the PlayStation Remote Play protocol | 56 | 🗄️ | Python |
| [XiPackets](https://github.com/atom0s/XiPackets) | Reverse engineered packet documentation for Final Fantasy XI | 55 | 🟢 |  |
| [wot-api-description](https://github.com/thunder-spb/wot-api-description) | World of Tanks unofficial API description | 45 | 🗄️ | PHP |
| [openfoxwq_client](https://github.com/openfoxwq/openfoxwq_client) | Multiplatform unofficial client for the Fox Go server | 44 | 🗄️ | Dart |
| [xboxlive-api](https://github.com/XboxReplay/xboxlive-api) | Simple Xbox Live API wrapper for Node.js | 44 | 🔴 | TypeScript |
| [trackmania2020apidocumentation](https://github.com/The-Firexx/trackmania2020apidocumentation) | Trackmania 2020 unofficial API documentation | 43 | 🗄️ |  |
| [Useful-ValorantAPI-Info](https://github.com/Soneliem/Useful-ValorantAPI-Info) | Resources and code for Valorant's unofficial API | 40 | 🔴 | Python |
| [BNETDocs](https://github.com/BNETDocs/bnetdocs-web) | Documentation website for Blizzard's Battle.net classic protocols | 36 | 🟢 | JavaScript |
| [pyps4-2ndscreen](https://github.com/ktnrg45/pyps4-2ndscreen) | Python library to control a PS4 via the PS4 Second Screen protocol | 20 | 🗄️ | Python |
| [OpenSpartan Workshop](https://github.com/OpenSpartan/openspartan-workshop) | Desktop app to track Halo Infinite stats and progression via the unofficial Halo API | 19 | 🟢 | C# |
| [valorant-xmpp-watcher](https://github.com/techchrism/valorant-xmpp-watcher) | Connects to and logs VALORANT XMPP presence and roster events | 4 | 🟡 | TypeScript |
| [Grunt](https://github.com/dend/grunt) | Unofficial API wrapper and documentation for the Halo Infinite web services | 0 | 🟢 | C# |

## Launchers & Store Clients

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Playnite](https://github.com/JosefNemec/Playnite) | Open-source game library manager integrating Steam, Epic, GOG, EA, Ubisoft and more store libraries | 14,198 | 🟢 | C# |
| [ArchiSteamFarm](https://github.com/JustArchiNET/ArchiSteamFarm) | C# Steam client application built on SteamKit2 for multi-account card farming and automation | 13,751 | 🟢 | C# |
| [Heroic Games Launcher](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher) | Open-source launcher for Epic, GOG and Amazon Games libraries on Linux, Windows and macOS | 12,382 | 🟢 | TypeScript |
| [Prism Launcher](https://github.com/PrismLauncher/PrismLauncher) | Open-source Minecraft launcher managing multiple instances and Microsoft account login | 10,644 | 🟢 | C++ |
| [HMCL](https://github.com/HMCL-dev/HMCL) | Hello Minecraft! Launcher, a cross-platform third-party Minecraft launcher | 10,233 | 🟢 | Java |
| [Decky Loader](https://github.com/SteamDeckHomebrew/decky-loader) | Plugin loader for the Steam Deck that injects into the Steam client UI | 7,354 | 🟢 | TypeScript |
| [Legendary](https://github.com/legendary-gl/legendary) | Open-source CLI replacement for the Epic Games Launcher built on Epic's undocumented APIs | 5,326 | 🟢 | Python |
| [MultiMC](https://github.com/MultiMC/Launcher) | Custom Minecraft launcher for managing multiple isolated installations | 4,673 | 🟢 | C++ |
| [Millennium](https://github.com/SteamClientHomebrew/Millennium) | Framework for Steam client themes and plugins via injection into the CEF UI | 4,437 | 🟢 | C++ |
| [Steam Desktop Authenticator](https://github.com/Jessecar96/SteamDesktopAuthenticator) | Desktop implementation of Steam's mobile authenticator (Steam Guard) app | 3,827 | 🟡 | C# |
| [DepotDownloader](https://github.com/SteamRE/DepotDownloader) | Steam depot downloader built on the SteamKit2 reverse-engineered Steam protocol library | 3,462 | 🟢 | C# |
| [XIVLauncher](https://github.com/goatcorp/FFXIVQuickLauncher) | Custom third-party launcher for Final Fantasy XIV that reimplements the login flow | 3,189 | 🟢 | C# |
| [Bloxstrap](https://github.com/bloxstraplabs/bloxstrap) | Alternative bootstrapper for the Roblox client with extra configuration | 3,174 | 🟢 | C# |
| [GameHub](https://github.com/tkashkin/GameHub) | Unified game library for Steam, GOG and Humble Bundle (archived) | 2,846 | 🗄️ | Vala |
| [chiaki-ng](https://github.com/chiaki-ng/chiaki-ng) | Open-source PlayStation 4/5 Remote Play client, successor of Chiaki | 2,827 | 🟢 | C |
| [BoilR](https://github.com/PhilipK/BoilR) | Syncs games from Epic, GOG, Origin, Amazon and other launchers into the Steam library | 1,907 | 🟢 | Rust |
| [Pluvia](https://github.com/oxters168/Pluvia) | Lightweight unofficial Steam client for Android | 1,724 | 🟢 | C |
| [mcpelauncher](https://github.com/minecraft-linux/mcpelauncher-manifest) | Runs the Android build of Minecraft Bedrock natively on Linux and macOS | 1,687 | 🟢 | CMake |
| [Minigalaxy](https://github.com/sharkwouter/minigalaxy) | Simple unofficial GOG client for Linux | 1,333 | 🟢 | Python |
| [steamguard-cli](https://github.com/dyc3/steamguard-cli) | Linux CLI for Steam Guard 2FA codes and trade/market confirmations | 1,063 | 🟢 | Rust |
| [MC Bedrock Version Launcher](https://github.com/MCMrARM/mc-w10-version-launcher) | Installs and switches between multiple Minecraft Bedrock (Windows 10) versions | 1,062 | 🟢 | C++ |
| [steam-tui](https://github.com/dmadisetti/steam-tui) | Rust TUI Steam client driving steamcmd | 1,039 | 🟢 | Rust |
| [Rare](https://github.com/RareDevs/Rare) | Qt GUI alternative to the Epic Games Launcher, built on Legendary | 933 | 🟢 | Python |
| [LGOGDownloader](https://github.com/Sude-/lgogdownloader) | Unofficial GOG.com downloader for Linux using the same API as GOG Galaxy | 917 | 🟢 | C++ |
| [Vinegar](https://github.com/vinegarhq/vinegar) | Open-source launcher/manager for running Roblox Studio on Linux | 787 | 🟢 | Go |
| [humblebundle-downloader](https://github.com/xtream1101/humblebundle-downloader) | Downloads a Humble Bundle library via Humble's internal API | 610 | 🗄️ | Python |
| [gogrepo](https://github.com/eddie3/gogrepo) | Python tool to download a full GOG.com game and bonus collection for offline use | 544 | 🔴 | Python |
| [SBRW GameLauncher](https://github.com/SoapboxRaceWorld/GameLauncher_NFSW) | Unofficial launcher for Need for Speed: World community servers | 533 | 🟡 | C# |
| [steamctl](https://github.com/ValvePython/steamctl) | Command-line tool to control Steam: download depots, workshop items, manage apps and accounts | 377 | 🟡 | Python |
| [comet](https://github.com/imLinguin/comet) | Open source implementation of the GOG Galaxy communication service | 370 | 🟢 | Rust |
| [nile](https://github.com/imLinguin/nile) | Unofficial Amazon Games client (CLI) reimplementing the Amazon Games app's protocol | 362 | 🟢 | Python |
| [CnCNet Client](https://github.com/CnCNet/xna-cncnet-client) | Online multiplayer client for classic Command & Conquer games on the CnCNet service | 310 | 🟢 | C# |
| [Slippi Launcher](https://github.com/project-slippi/slippi-launcher) | Launcher for Project Slippi, the rollback netplay and replay system for Super Smash Bros. Melee | 310 | 🟢 | TypeScript |
| [open-steamworks](https://github.com/SteamRE/open-steamworks) | Reverse engineered headers for Valve's Steam client interfaces | 263 | 🗄️ | C# |
| [xcloud-shield](https://github.com/mistertest/xcloud-shield) | Unofficial Xbox Cloud Gaming app for Nvidia Shield TV | 235 | 🔴 | Java |
| [Maxima](https://github.com/ArmchairDevelopers/Maxima) | Free open-source replacement for the EA Desktop launcher for Linux and Windows | 232 | 🟢 | Rust |
| [cordial](https://github.com/luohoa97/cordial) | Open-source runtime to run the Roblox client natively on Linux | 200 | 🟢 | Rust |
| [xbox-xcloud-player](https://github.com/unknownskl/xbox-xcloud-player) | Library implementing the Xbox Cloud Gaming / home streaming WebRTC protocol | 197 | 🟢 | TypeScript |
| [heroic-gogdl](https://github.com/Heroic-Games-Launcher/heroic-gogdl) | GOG download/install module for Heroic using GOG Galaxy's content-system APIs | 178 | 🟢 | Python |
| [games_nebula](https://github.com/yancharkin/games_nebula) | Unofficial GOG client for Linux | 160 | 🟡 | Python |
| [SteamAppInfo](https://github.com/xPaw/SteamAppInfo) | Parser for Steam client appinfo.vdf and packageinfo.vdf files | 143 | 🟢 | C# |
| [libnxbox](https://github.com/ursusworks/libnxbox) | Xbox Cloud Gaming streaming client for Nintendo Switch homebrew | 131 | 🟢 |  |
| [RA3Bar-RA3Launcher](https://github.com/lanyizi/RA3Bar-RA3Launcher) | Reimplementation of the Red Alert 3 game launcher | 130 | 🔴 | C++ |
| [jetisteam](https://github.com/iTaysonLab/jetisteam) | Unofficial Steam mobile client | 125 | 🟢 | Kotlin |
| [wyvern](https://github.com/nicohman/wyvern) | Simple CLI client for installing and maintaining Linux GOG games | 100 | 🔴 | Rust |

## Matching Decompilations — Arcade

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [namco22-decompile](https://github.com/spacestate1/namco22-decompile) | Decompilation of Namco System 22 arcade games | 172 | 🟢 | C |
| [Sonic the Fighters](https://github.com/biggestsonicfan/stfdecomp) | Matching decompilation of Sonic the Fighters (Sega Model 2 arcade, 1996) | 109 | 🟢 | Assembly |
| [F-Zero AX](https://github.com/TheInfiniteLegend/f-0-ax) | Matching decompilation of F-Zero AX (Triforce arcade, 2003) | 3 | 🟡 | C |

## Matching Decompilations — Atari

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [StarRaiders](https://github.com/lwiest/StarRaiders) | Reverse-engineered, fully documented 6502 source of Star Raiders | 183 | 🟡 |  |
| [Raiders2600](https://github.com/halkuncode/Raiders2600) | Reverse-engineered, commented source of Raiders of the Lost Ark for Atari 2600 | 174 | 🟢 | Assembly |

## Matching Decompilations — Game Boy / GBA / DS

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [pokered](https://github.com/pret/pokered) | Disassembly of Pokemon Red/Blue | 4,983 | 🟢 | Assembly |
| [pokeemerald](https://github.com/pret/pokeemerald) | Decompilation of Pokemon Emerald | 3,576 | 🟢 | C |
| [pokecrystal](https://github.com/pret/pokecrystal) | Disassembly of Pokemon Crystal | 2,522 | 🟢 | Assembly |
| [Pokémon FireRed/LeafGreen](https://github.com/pret/pokefirered) | Matching decompilation of Pokémon FireRed/LeafGreen (Game Boy Advance, 2004) | 1,655 | 🟢 | C |
| [Pokémon Ruby/Sapphire](https://github.com/pret/pokeruby) | Matching decompilation of Pokémon Ruby/Sapphire (Game Boy Advance, 2002) | 1,000 | 🟢 | C |
| [The Legend of Zelda: The Minish Cap](https://github.com/zeldaret/tmc) | Matching decompilation of The Legend of Zelda: The Minish Cap (Game Boy Advance, 2004) | 914 | 🟢 | C |
| [LADX-Disassembly](https://github.com/zladx/LADX-Disassembly) | Disassembly of The Legend of Zelda: Link's Awakening DX | 911 | 🟢 | Assembly |
| [Pokémon Yellow](https://github.com/pret/pokeyellow) | Disassembly of Pokémon Yellow (Game Boy, 1998) | 888 | 🟢 | Assembly |
| [Pokémon Gold/Silver](https://github.com/pret/pokegold) | Disassembly of Pokémon Gold/Silver (Game Boy Color, 1999) | 726 | 🟢 | Assembly |
| [sa2](https://github.com/SAT-R/sa2) | Decompilation and port of Sonic Advance 1 & 2 (GBA) | 675 | 🟢 | C |
| [Pokémon HeartGold/SoulSilver](https://github.com/pret/pokeheartgold) | Matching decompilation of Pokémon HeartGold/SoulSilver (Nintendo DS, 2009) | 616 | 🟢 | Assembly |
| [pokeplatinum](https://github.com/pret/pokeplatinum) | Decompilation of Pokemon Platinum | 559 | 🟢 | C |
| [Pokémon Diamond/Pearl](https://github.com/pret/pokediamond) | Matching decompilation of Pokémon Diamond/Pearl (Nintendo DS, 2006) | 536 | 🟢 | Assembly |
| [Pokémon Gold (SpaceWorld Demo)](https://github.com/pret/pokegold-spaceworld) | Disassembly of Pokémon Gold and Silver (Game Boy, 1997; Space World 1997 demo) | 402 | 🟢 | Assembly |
| [Pokémon TCG](https://github.com/pret/poketcg) | Disassembly of Pokémon Trading Card Game (Game Boy Color, 1998) | 329 | 🟢 | Assembly |
| [Pokémon Mystery Dungeon: Red Rescue Team](https://github.com/pret/pmd-red) | Matching decompilation of Pokémon Mystery Dungeon: Red Rescue Team (Game Boy Advance, 2005) | 284 | 🟢 | C |
| [Fire Emblem: The Sacred Stones (FEU)](https://github.com/FireEmblemUniverse/fireemblem8u) | Matching decompilation of Fire Emblem: The Sacred Stones (Game Boy Advance, 2004) | 225 | 🟢 | Assembly |
| [oracles-disasm](https://github.com/Stewmath/oracles-disasm) | Disassembly of Zelda: Oracle of Ages and Seasons | 219 | 🟢 | Assembly |
| [Pokémon Pinball](https://github.com/pret/pokepinball) | Disassembly of Pokémon Pinball (Game Boy Color, 1999) | 200 | 🟢 | Assembly |
| [sm64ds-decomp](https://github.com/tangosdev/sm64ds-decomp) | Byte-matching decompilation of Super Mario 64 DS | 193 | 🟢 | C++ |
| [Kirby & The Amazing Mirror](https://github.com/jiangzhengwenjz/katam) | Matching decompilation of Kirby & The Amazing Mirror (Game Boy Advance, 2004) | 157 | 🟢 | C |
| [Metroid: Zero Mission](https://github.com/metroidret/mzm) | Matching decompilation of Metroid: Zero Mission (Game Boy Advance, 2004) | 147 | 🟢 | C |
| [Pokémon Pinball Ruby & Sapphire](https://github.com/pret/pokepinballrs) | Matching decompilation of Pokémon Pinball Ruby & Sapphire (Game Boy Advance, 2003) | 147 | 🟢 | Assembly |
| [Golden Sun](https://github.com/PascalPixel/alchemy) | Matching decompilation of Golden Sun (Game Boy Advance, 2001) | 144 | 🟢 | Assembly |
| [Pokémon Mystery Dungeon: Explorers of Sky](https://github.com/pret/pmd-sky) | Matching decompilation of Pokémon Mystery Dungeon: Explorers of Sky (Nintendo DS, 2009) | 141 | 🟢 | Assembly |
| [Super Mario 3D Land](https://github.com/3dsdecomp/RedPepper) | Matching decompilation of Super Mario 3D Land (Nintendo 3DS, 2011) | 110 | 🟡 | C++ |
| [The Legend of Zelda: Phantom Hourglass](https://github.com/zeldaret/ph) | Matching decompilation of The Legend of Zelda: Phantom Hourglass (Nintendo DS, 2007) | 110 | 🟢 | C++ |
| [Pokémon Snap](https://github.com/ethteck/pokemonsnap) | Decompilation of Pokémon Snap | 107 | 🟢 | C |
| [Pokémon TCG 2](https://github.com/pret/poketcg2) | Disassembly of Pokémon Card GB2 (Game Boy Color, 2001) | 94 | 🟢 | Assembly |
| [The Legend of Zelda: Ocarina of Time 3D](https://github.com/zeldaret/oot3d) | Matching decompilation of The Legend of Zelda: Ocarina of Time 3D (Nintendo 3DS, 2011) | 88 | 🟢 | C++ |
| [Kingdom Hearts 358/2 Days](https://github.com/Yokimitsuro/khdays-decomp) | Matching decompilation of Kingdom Hearts 358/2 Days (Nintendo DS, 2009) | 85 | 🟢 | C |
| [Sonic Advance 3](https://github.com/SAT-R/sa3) | Matching decompilation of Sonic Advance 3 (Game Boy Advance, 2004) | 85 | 🟢 | C |
| [Sonic Advance](https://github.com/SAT-R/sa1) | Matching decompilation of Sonic Advance (Game Boy Advance, 2001) | 77 | 🗄️ | C |
| [Pokémon Emerald (JP)](https://github.com/pret/pokeemerald-jp) | Matching decompilation of Pokémon Emerald (Game Boy Advance, 2004; Japanese version) | 68 | 🔴 | Assembly |
| [Metroid Fusion](https://github.com/metroidret/mf) | Matching decompilation of Metroid Fusion (Game Boy Advance, 2002) | 67 | 🟢 | C |
| [The Legend of Zelda: Spirit Tracks](https://github.com/zeldaret/st) | Matching decompilation of The Legend of Zelda: Spirit Tracks (Nintendo DS, 2009) | 65 | 🟢 | C++ |
| [New Super Mario Bros.](https://github.com/NSMB-Decomp/nsmb) | Matching decompilation of New Super Mario Bros. (Nintendo DS, 2006) | 64 | 🟢 | C++ |
| [Mario Kart DS](https://github.com/XorTroll/mkds-re) | Decompilation of Mario Kart DS | 62 | 🟡 | C |
| [Pokémon Black](https://github.com/squiddonaut/pokeblack) | Matching decompilation of Pokémon Black (Nintendo DS, 2010) | 58 | 🟢 | Assembly |
| [Kingdom Hearts: Chain of Memories](https://github.com/Pheenoh/khcom) | Matching decompilation of Kingdom Hearts: Chain of Memories (Game Boy Advance, 2004) | 52 | 🟢 | C |
| [Phoenix Wright: Ace Attorney](https://github.com/atasro2/pwaa1) | Matching decompilation of Phoenix Wright: Ace Attorney (Game Boy Advance, 2001; Japanese Gyakuten Saiban) | 52 | 🟢 | C |
| [Rhythm Heaven (DS)](https://github.com/patataofcourse/rhgold) | Decompilation of Rhythm Heaven (DS) | 48 | 🟢 | C |
| [Dragon Quest IX](https://github.com/DQIX/dqix-decomp) | Matching decompilation of Dragon Quest IX: Sentinels of the Starry Skies (Nintendo DS, 2009) | 45 | 🟢 | C++ |
| [Mega Man Zero 3](https://github.com/mmzret/rmz3) | Matching decompilation of Mega Man Zero 3 (Game Boy Advance, 2004) | 45 | 🟢 | Assembly |
| [Sonic Rush Adventure](https://github.com/RushRE/SonicRushAdventure-Decomp) | Matching decompilation of Sonic Rush Adventure (Nintendo DS, 2007) | 44 | 🟢 | C |
| [Banjo-Kazooie: Grunty's Revenge](https://github.com/jellees/bkgr) | Matching decompilation of Banjo-Kazooie: Grunty's Revenge (Game Boy Advance, 2003) | 43 | 🟢 | Assembly |
| [Harvest Moon: Friends of Mineral Town](https://github.com/StanHash/fomt) | Matching decompilation of Harvest Moon: Friends of Mineral Town (Game Boy Advance, 2003) | 41 | 🟢 | Assembly |
| [pokemonstadium](https://github.com/ethteck/pokemonstadium) | Decompilation of Pokemon Stadium | 41 | 🔴 | Assembly |
| [berry-fix](https://github.com/pret/berry-fix) | Decompilation of the Berry Fix Program in Pokemon Emerald and FireRed/LeafGreen | 39 | 🔴 | C |
| [Mario & Luigi: Superstar Saga](https://github.com/jellees/mlss) | Matching decompilation of Mario & Luigi: Superstar Saga (Game Boy Advance, 2003) | 37 | 🟢 | Assembly |
| [Fire Emblem: The Blazing Blade (JP)](https://github.com/MokhaLeee/FireEmblem7J) | Matching decompilation of Fire Emblem: Rekka no Ken (Game Boy Advance, 2003; Japanese Blazing Blade) | 36 | 🟢 | Assembly |
| [colosseum-mb](https://github.com/pret/colosseum-mb) | Decompilation of the GBA multiboot for Pokemon Colosseum | 34 | 🟡 | C++ |
| [Mario Kart: Super Circuit](https://github.com/jellees/mksc) | Matching decompilation of Mario Kart: Super Circuit (Game Boy Advance, 2001) | 34 | 🟡 | Assembly |
| [mksc-decompilation](https://github.com/XOlifreX/mksc-decompilation) | Decompilation of Mario Kart Super Circuit (GBA) | 32 | 🔴 | Assembly |
| [Castlevania: Order of Ecclesia](https://github.com/LagoLunatic/ooe) | Matching decompilation of Castlevania: Order of Ecclesia (Nintendo DS, 2008) | 31 | 🟡 | C |
| [The World Ends With You](https://github.com/Yotona/twewy) | Matching decompilation of The World Ends With You (Nintendo DS, 2007) | 31 | 🟢 | C |
| [Mother 1+2](https://github.com/Normmatt/m12) | Matching decompilation of Mother 1+2 (Game Boy Advance, 2003) | 29 | 🟢 | C |
| [Golden Sun: The Broken Seal](https://github.com/Coaltergeist/goldensun-decomp) | Matching decompilation of Golden Sun: The Broken Seal (Game Boy Advance, 2001) | 28 | 🟢 | Assembly |
| [Donkey Kong '94](https://github.com/CelestialAmber/DKGBDisasm) | Disassembly of Donkey Kong (Game Boy, 1994) | 26 | 🔴 | Assembly |
| [Castlevania: Aria of Sorrow](https://github.com/testyourmine/cvaos) | Matching decompilation of Castlevania: Aria of Sorrow (Game Boy Advance, 2003) | 25 | 🟢 | Assembly |
| [Fire Emblem: Seima no Kouseki (JP)](https://github.com/laqieer/fireemblem8j) | Matching decompilation of Fire Emblem: Seima no Kouseki (Game Boy Advance, 2004; Japanese Sacred Stones) | 23 | 🟢 | C |
| [Mario Party DS](https://github.com/mariopartyrd/mariopartyDS) | Decompilation of Mario Party DS | 23 | 🟡 | Python |
| [ZoidsLegacyDecomp](https://github.com/jmacato/ZoidsLegacyDecomp) | Matched decompilation of Zoids Legacy (GBA) | 21 | 🟢 | C |
| [pokemoon](https://github.com/gradenGnostic/pokemoon) | Decompilation of Pokemon Moon | 20 | 🟢 | C++ |
| [Fire Emblem: The Sacred Stones](https://github.com/laqieer/fireemblem8u) | Matching decompilation of Fire Emblem: The Sacred Stones (Game Boy Advance, 2004) | 19 | 🟢 | Assembly |
| [Klonoa: Empire of Dreams](https://github.com/testyourmine/kleod) | Matching decompilation of Klonoa: Empire of Dreams (Game Boy Advance, 2001) | 18 | 🟢 | C |
| [Summon Night: Craft Sword Monogatari](https://github.com/jiangzhengwenjz/csm3) | Matching decompilation of Summon Night: Craft Sword Monogatari (Game Boy Advance, 2003) | 18 | 🟡 | Assembly |
| [Kirby: Nightmare in Dream Land](https://github.com/overjt/knidl) | Matching decompilation of Kirby: Nightmare in Dream Land (Game Boy Advance, 2002) | 17 | 🟢 | C |
| [Star Ocean: Blue Sphere](https://github.com/animaone/star-ocean-blue-sphere-source-code) | Source code of Star Ocean: Blue Sphere (Game Boy Color, 2001) | 17 | 🟡 | Assembly |
| [Fire Emblem: Shadow Dragon](https://github.com/Eebit/fe11-us) | Matching decompilation of Fire Emblem: Shadow Dragon (Nintendo DS, 2008) | 16 | 🟢 | C++ |
| [Phoenix Wright: Ace Attorney – Justice for All](https://github.com/atasro2/pwaa2) | Matching decompilation of Phoenix Wright: Ace Attorney – Justice for All (Game Boy Advance, 2002; Japanese Gyakuten Saiban 2) | 16 | 🟢 | Assembly |
| [Wario Land 4](https://github.com/TsilaAllaoui/warioland4) | Matching decompilation of Wario Land 4 (Game Boy Advance, 2001) | 16 | 🟢 | C |
| [Klonoa: Empire of Dreams](https://github.com/Dream-Atelier/kl-eod-decomp) | Matching decompilation of Klonoa: Empire of Dreams (Game Boy Advance, 2001) | 15 | 🟢 | C |
| [Inazuma Eleven 3: The Ogre](https://github.com/CacaBueno64/ie3ogres) | Matching decompilation of Inazuma Eleven 3: The Ogre (Nintendo DS, 2011) | 13 | 🟢 | Assembly |
| [WarioWare, Inc.: Mega Microgames!](https://github.com/ShaffySwitcher/wariowareinc) | Matching decompilation of WarioWare, Inc.: Mega Microgames! (Game Boy Advance, 2003) | 13 | 🟢 | Assembly |
| [Advance Wars 2: Black Hole Rising](https://github.com/Eebit/aw2bhr) | Matching decompilation of Advance Wars 2: Black Hole Rising (Game Boy Advance, 2003) | 12 | 🟡 | Assembly |
| [Mario & Luigi: Partners in Time](https://github.com/Rainchus/PartnersInTime-Decomp) | Matching decompilation of Mario & Luigi: Partners in Time (Nintendo DS, 2005) | 12 | 🟢 | Python |
| [Paper Mario: Sticker Star](https://github.com/Darxoon/leaflitter) | Matching decompilation of Paper Mario: Sticker Star (Nintendo 3DS, 2012) | 12 | 🗄️ | Python |
| [Pokémon Black 2 and White 2](https://github.com/fuddlesworth/pokebw2) | Matching decompilation of Pokémon Black 2 and White 2 (Nintendo DS, 2012) | 12 | 🟢 | C |
| [Pokémon Rumble](https://github.com/KooShnoo/pokemon-rumble) | Decompilation of Pokémon Rumble | 12 | 🟢 | C++ |
| [Dragon Quest IV](https://github.com/GoldieLeGenie/DQIV-DECOMP) | Matching decompilation of Dragon Quest IV (Nintendo DS, 2007) | 11 | 🟢 | C++ |
| [Wario Land 4 (lilDavid)](https://github.com/lilDavid/warioland4) | Matching decompilation of Wario Land 4 (Game Boy Advance, 2001) | 11 | 🟢 | Assembly |
| [Super Mario 64 DS](https://github.com/matty45/sm64ds-decomp) | Decompilation of Super Mario 64 DS | 10 | 🗄️ | Assembly |
| [DWM](https://github.com/Mallos31/dwm) | Disassembly of Dragon Warrior Monsters 1 for the GBC | 9 | 🔴 | Assembly |
| [Kingdom Hearts Re:coded](https://github.com/kh-recoded-decomp/kh-recoded-decomp) | Matching decompilation of Kingdom Hearts Re:coded (Nintendo DS, 2010) | 9 | 🟢 | C |
| [Sonic Battle](https://github.com/cypressru/SonicBattleDecomp) | Matching decompilation of Sonic Battle (Game Boy Advance, 2003) | 9 | 🟢 | C++ |
| [Custom Robo GX](https://github.com/pizdex/robogx) | Matching decompilation of Custom Robo GX (Game Boy Advance, 2004) | 8 | 🟡 | Assembly |
| [Dragon Warrior Monsters](https://github.com/NiyaDev/DWM) | Matching decompilation of Dragon Warrior Monsters (Game Boy Color, 1998) | 8 | 🟢 | Assembly |
| [LEGO Battles](https://github.com/LiruJ/Lego-Battles-Decomp) | Matching decompilation of LEGO Battles (Nintendo DS, 2009) | 8 | 🟢 | C++ |
| [Monster Hunter 4 Ultimate](https://github.com/mhvuze/mh4u-decomp) | Matching decompilation of Monster Hunter 4 Ultimate (Nintendo 3DS, 2014) | 8 | 🟢 |  |
| [The Urbz: Sims in the City (GBA)](https://github.com/SimsAdvanceRet/UrbzGBADecomp) | Decompilation of The Urbz: Sims in the City (GBA) | 8 | 🟡 |  |
| [Yu-Gi-Oh! The Eternal Duelist Soul](https://github.com/CosmicScribe64/eds-decomp) | Matching decompilation of Yu-Gi-Oh! The Eternal Duelist Soul (Game Boy Advance, 2002) | 8 | 🟢 | Assembly |
| [Beyblade VForce: Ultimate Blader Jam](https://github.com/marijnvdwerf/gba-beyblade-vforce) | Decompilation of Beyblade VForce: Ultimate Blader Jam | 7 | 🟢 | C |
| [Bomberman Land Touch! 2](https://github.com/gamemasterplc/bltouch2) | Matching decompilation of Bomberman Land Touch! 2 (Nintendo DS, 2008) | 6 | 🟢 | C |
| [eCrew Development Program](https://github.com/imavie/ecdpdecomp) | Matching decompilation of eCrew Development Program (Nintendo DS, 2010; McDonald's training game) | 6 | 🟡 |  |
| [Frogger's Adventures: Temple of the Frog](https://github.com/JRickey/frog-adv-temple-decomp) | Matching decompilation of Frogger's Adventures: Temple of the Frog (Game Boy Advance, 2001) | 5 | 🟢 | Assembly |
| [The Sims 2 (GBA)](https://github.com/SimsAdvanceRet/S2GBADecomp) | Decompilation of The Sims 2 (GBA) | 5 | 🟡 |  |
| [The Sims: Bustin' Out (GBA)](https://github.com/SimsAdvanceRet/BustinOutGBADecomp) | Decompilation of The Sims: Bustin' Out (GBA) | 5 | 🟡 |  |
| [Harry Potter and the Prisoner of Azkaban (GBA)](https://github.com/holly-hacker/hp3-gba-decomp) | Decompilation of Harry Potter and the Prisoner of Azkaban (GBA) | 3 | 🟢 | C |
| [Princess Maker 4](https://github.com/Yanis002/pm4) | Matching decompilation of Princess Maker 4 (Nintendo DS; Japanese version) | 3 | 🟢 | C |
| [Air Traffic Chaos](https://github.com/sasja-san/atc) | Matching decompilation of Air Traffic Chaos (Nintendo DS, 2007) | 2 | 🟢 | Python |
| [DuckTales (Game Boy) Disassembly](https://github.com/RussianManSMWC/DuckTales-of-Disassembly-GB) | A disassembly of DuckTales for the Game Boy | 2 | 🟢 | Assembly |
| [New Super Mario Bros. 2](https://github.com/T3CHNOLOG1C/BigRed) | Matching decompilation of New Super Mario Bros. 2 (Nintendo 3DS, 2012) | 1 | 🟢 | C++ |
| [Digimon World DS](https://github.com/ReGame-Labs/dwds_decomp) | Decompilation of Digimon World DS | 0 | 🟢 | C |
| [GT Advance 3: Pro Concept Racing](https://github.com/722rsr/gtadv3-decomp) | Matching decompilation of GT Advance 3: Pro Concept Racing (Game Boy Advance, 2003) | 0 | 🟢 | C |
| [Lock's Quest](https://github.com/redraincatching/locksmith) | Matching decompilation of Lock's Quest (Nintendo DS, 2008) | 0 | 🟡 |  |
| [NASCAR Heat 2002](https://github.com/shohamc1/heat2002) | Matching decompilation of NASCAR Heat 2002 (Game Boy Advance, 2001) | 0 | 🟢 | C |
| [Okamiden](https://github.com/dothacktranslate/okamiden-decomp) | Matching decompilation of Okamiden (Nintendo DS, 2010) | 0 | 🟢 | C |
| [Shin Bokura no Taiyou: Gyakushuu no Sabata](https://github.com/moozilla/boktai3-decomp) | Matching decompilation of Shin Bokura no Taiyou: Gyakushuu no Sabata (Game Boy Advance, 2005) | 0 | 🟢 | C |

## Matching Decompilations — GameCube & Wii

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Super Smash Bros. Melee](https://github.com/doldecomp/melee) | Matching decompilation of Super Smash Bros. Melee (GameCube, 2001) | 2,401 | 🟢 | C |
| [ac-decomp](https://github.com/ACreTeam/ac-decomp) | Decompilation of Animal Crossing for GameCube | 1,407 | 🟢 | C |
| [Super Mario Galaxy](https://github.com/SMGCommunity/Petari) | Matching decompilation of Super Mario Galaxy (Wii, 2007) | 1,198 | 🟢 | C++ |
| [Mario Party 4](https://github.com/mariopartyrd/marioparty4) | Matching decompilation of Mario Party 4 (GameCube, 2002) | 864 | 🟢 | C |
| [Mario Kart Wii (riidefi)](https://github.com/snailspeed3/mkw) | Decompilation of Mario Kart Wii (riidefi) | 466 | 🟡 | C |
| [Pikmin 2](https://github.com/projectPiki/pikmin2) | Matching decompilation of Pikmin 2 (GameCube, 2004) | 376 | 🟢 | C++ |
| [Metroid Prime](https://github.com/PrimeDecomp/prime) | Matching decompilation of Metroid Prime (GameCube, 2002) | 361 | 🟢 | C++ |
| [Super Mario Sunshine](https://github.com/doldecomp/sms) | Matching decompilation of Super Mario Sunshine (GameCube, 2002) | 345 | 🟢 | C++ |
| [re4 decomp](https://github.com/adonis-singh/re4) | Byte-identical decompilation of Resident Evil 4 (GameCube debug build) to C/C++ | 343 | 🟢 | C++ |
| [Pikmin](https://github.com/projectPiki/pikmin) | Matching decompilation of Pikmin (GameCube, 2001) | 315 | 🟢 | C |
| [Wii Menu](https://github.com/koopthekoopa/wii-ipl) | Decompilation of Wii Menu | 214 | 🟢 | C |
| [Mario Kart: Double Dash!!](https://github.com/doldecomp/mkdd) | Matching decompilation of Mario Kart: Double Dash!! (GameCube, 2003) | 198 | 🟢 | C++ |
| [SpongeBob SquarePants: Battle for Bikini Bottom](https://github.com/bfbbdecomp/bfbb) | Matching decompilation of SpongeBob SquarePants: Battle for Bikini Bottom (GameCube, 2003) | 191 | 🟢 | C++ |
| [The Legend of Zelda: Skyward Sword](https://github.com/zeldaret/ss) | Matching decompilation of The Legend of Zelda: Skyward Sword (Wii, 2011) | 189 | 🟢 | C++ |
| [Wii Sports](https://github.com/doldecomp/ogws) | Decompilation of Wii Sports | 172 | 🟢 | C |
| [Paper Mario: The Thousand-Year Door](https://github.com/doldecomp/ttyd) | Matching decompilation of Paper Mario: The Thousand-Year Door (GameCube, 2004) | 141 | 🟢 | C |
| [Xenoblade Chronicles](https://github.com/xbret/xenoblade) | Matching decompilation of Xenoblade Chronicles (Wii, 2010) | 141 | 🟢 | C |
| [New Super Mario Bros. Wii](https://github.com/NSMBW-Community/NSMBW-Decomp) | Decompilation of New Super Mario Bros. Wii | 139 | 🟢 | C |
| [Rock Band 3 decomp](https://github.com/DarkRTA/rb3) | Decompilation of Rock Band 3 (Wii) | 121 | 🟢 | C++ |
| [Super Mario Strikers](https://github.com/yannicksuter/smstrikers-decomp) | Matching decompilation of Super Mario Strikers (GameCube, 2005) | 101 | 🟢 | C++ |
| [Super Paper Mario](https://github.com/SeekyCt/spm-decomp) | Matching decompilation of Super Paper Mario (Wii, 2007) | 99 | 🟢 | C |
| [Super Smash Bros. Brawl](https://github.com/doldecomp/brawl) | Matching decompilation of Super Smash Bros. Brawl (Wii, 2008) | 97 | 🟢 | C++ |
| [FRAY](https://github.com/PsiLupan/FRAY) | Recompilable Super Smash Bros. Melee 1.02 based on libOGC | 94 | 🔴 | C |
| [SMGDecompilation](https://github.com/snailspeed3/SMGDecompilation) | Work-in-progress decompilation of Super Mario Galaxy | 94 | 🔴 | Assembly |
| [Kirby Air Ride (doldecomp)](https://github.com/doldecomp/kar) | Matching decompilation of Kirby Air Ride (GameCube, 2003) | 88 | 🟡 | Assembly |
| [Star Fox Adventures](https://github.com/zcanann/SFA-Decomp) | Matching decompilation of Star Fox Adventures (GameCube, 2002) | 73 | 🟢 | C |
| [Super Mario Galaxy 2](https://github.com/SMGCommunity/Garigari) | Matching decompilation of Super Mario Galaxy 2 (Wii, 2010) | 69 | 🟢 | C |
| [Mario Kart Wii](https://github.com/doldecomp/mkw) | Decompilation of Mario Kart Wii | 53 | 🟢 | C |
| [Kirby's Epic Yarn](https://github.com/Swiftshine/key) | Matching decompilation of Kirby's Epic Yarn (Wii, 2010) | 51 | 🟢 | C++ |
| [Animal Forest e+](https://github.com/ACreTeam/afe-decomp) | Matching decompilation of Animal Forest e+ (GameCube, 2003) | 50 | 🟢 | C |
| [Sonic Adventure DX](https://github.com/doldecomp/sadx) | Matching decompilation of Sonic Adventure DX (GameCube, 2003) | 48 | 🟡 | Python |
| [Final Fantasy Crystal Chronicles](https://github.com/zcanann/FFCC-Decomp) | Matching decompilation of Final Fantasy Crystal Chronicles (GameCube, 2003) | 40 | 🟢 | C |
| [Chibi-Robo!](https://github.com/eavpsp/cbr_decomp) | Matching decompilation of Chibi-Robo! (GameCube, 2005) | 39 | 🟢 | C++ |
| [Mario Party 5](https://github.com/mariopartyrd/marioparty5) | Matching decompilation of Mario Party 5 (GameCube, 2003) | 38 | 🟢 | C |
| [Ratatouille](https://github.com/ZounaModding/RatDecomp) | Matching decompilation of Ratatouille (GameCube, 2007) | 36 | 🟢 | C++ |
| [recvx-gc-decomp](https://github.com/fmil95/recvx-gc-decomp) | Decompilation of Resident Evil Code: Veronica X (GameCube) | 36 | 🟢 | C |
| [Sonic Riders](https://github.com/doldecomp/sonicriders) | Matching decompilation of Sonic Riders (GameCube, 2006) | 36 | 🔴 | Assembly |
| [TY the Tasmanian Tiger](https://github.com/1superchip/ty-decomp) | Matching decompilation of TY the Tasmanian Tiger (GameCube, 2002) | 36 | 🟢 | C++ |
| [Need for Speed: Underground](https://github.com/dbalatoni13/nfsug) | Matching decompilation of Need for Speed: Underground (GameCube, 2003) | 35 | 🟢 | C |
| [Pokémon XD: Gale of Darkness](https://github.com/TeamOrre/xd-decomp) | Matching decompilation of Pokémon XD: Gale of Darkness (GameCube, 2005) | 35 | 🟢 | C |
| [Luigi's Mansion (zmansion)](https://github.com/Sage-of-Mirrors/zmansion) | Matching decompilation of Luigi's Mansion (GameCube, 2001) | 34 | 🟡 | C |
| [Mario Strikers Charged](https://github.com/yannicksuter/mscharged-decomp) | Matching decompilation of Mario Strikers Charged (Wii, 2007) | 32 | 🟢 | C++ |
| [dolsdk2001](https://github.com/doldecomp/dolsdk2001) | Decompilation of the 2001 Dolphin (GameCube) SDK libraries | 30 | 🟡 | C |
| [Mario Party 7](https://github.com/mariopartyrd/marioparty7) | Matching decompilation of Mario Party 7 (GameCube, 2005) | 28 | 🟢 | C |
| [Rhythm Heaven Fever](https://github.com/conhlee/rhf) | Matching decompilation of Rhythm Heaven Fever (Wii, 2011) | 27 | 🟢 | C++ |
| [Sonic Heroes](https://github.com/Jovinull/sonicheroes) | Matching decompilation of Sonic Heroes (GameCube, 2003) | 26 | 🟢 | C++ |
| [Star Fox Adventures (sfadebug)](https://github.com/RenaKunisaki/sfadebug) | Matching decompilation of Star Fox Adventures (GameCube, 2002; debug version) | 25 | 🟢 | C |
| [Harvest Moon: A Wonderful Life](https://github.com/ChrisNonyminus/hmawl) | Matching decompilation of Harvest Moon: A Wonderful Life (GameCube, 2003) | 24 | 🔴 | Assembly |
| [Pokémon Colosseum](https://github.com/dougchansan/pkmn-colosseum) | Matching decompilation of Pokémon Colosseum (GameCube, 2003) | 24 | 🟢 | C |
| [The Incredibles](https://github.com/seilc/incredibles) | Matching decompilation of The Incredibles (GameCube, 2004) | 24 | 🔴 | Assembly |
| [Gauntlet: Dark Legacy](https://github.com/sabishii-bit/Gauntlet-Dark-Legacy-Decompilation) | Matching decompilation of Gauntlet: Dark Legacy (GameCube, 2001) | 23 | 🟢 | C |
| [Mario Party 8](https://github.com/mariopartyrd/marioparty8) | Matching decompilation of Mario Party 8 (Wii, 2007) | 23 | 🟢 | Python |
| [Naruto: Gekitō Ninja Taisen! 4](https://github.com/doldecomp/gnt4) | Matching decompilation of Naruto: Gekitō Ninja Taisen! 4 (GameCube, 2005) | 23 | 🔴 | Assembly |
| [The SpongeBob SquarePants Movie](https://github.com/bfbbdecomp/tssm) | Matching decompilation of The SpongeBob SquarePants Movie (GameCube, 2004) | 23 | 🟢 | C++ |
| [open_rvl](https://github.com/kiwi515/open_rvl) | Decompilation of the Wii RVL SDK | 22 | 🗄️ | C |
| [Mario Party 6 (mariopartyrd)](https://github.com/mariopartyrd/marioparty6) | Matching decompilation of Mario Party 6 (GameCube, 2004) | 21 | 🟢 | C |
| [New Play Control! Pikmin 2](https://github.com/projectPiki/pik2wii) | Matching decompilation of New Play Control! Pikmin 2 (Wii, 2009) | 21 | 🟢 | C++ |
| [The Sims 2 (GameCube)](https://github.com/natebag/Sims2DECOMP) | Decompilation of The Sims 2 (GameCube) | 21 | 🟢 | C++ |
| [Mario Party 9 (mariopartyrd)](https://github.com/mariopartyrd/marioparty9) | Matching decompilation of Mario Party 9 (Wii, 2012) | 20 | 🟡 | C |
| [LEGO Star Wars III: The Clone Wars (Wii)](https://github.com/ThePlayerRolo/LegoCloneWarsWii) | Decompilation of LEGO Star Wars III: The Clone Wars (Wii) | 19 | 🟢 | C |
| [Pokémon Battle Revolution](https://github.com/bgsamm/pbr-dtk) | Matching decompilation of Pokémon Battle Revolution (Wii, 2006) | 19 | 🟢 | C |
| [Forecast Channel (Wii)](https://github.com/GuestDreemurr/forecast) | Decompilation of Forecast Channel (Wii) | 18 | 🟢 | C |
| [The Sims 2: Castaway](https://github.com/HaydnTrigg/Castaway) | Matching decompilation of The Sims 2: Castaway (Wii, 2007) | 17 | 🟢 | C |
| [Disney's Piglet's Big Game](https://github.com/tgsm/pbg) | Matching decompilation of Disney's Piglet's Big Game (GameCube, 2003) | 16 | 🟢 | C |
| [Hagi (GameCube/Wii emulator in Super Mario 3D All-Stars)](https://github.com/GRAnimated/Hagi) | Decompilation of Hagi (GameCube/Wii emulator in Super Mario 3D All-Stars) | 16 | 🟢 | C |
| [Ratchet & Clank: Going Commando (USA v1.01)](https://github.com/OpenRAC/rac2-gc-decomp) | Decompilation of Ratchet & Clank: Going Commando (USA v1.01) | 16 | 🟢 | C |
| [Inazuma Eleven Strikers](https://github.com/SwareJonge/IEStrikers) | Matching decompilation of Inazuma Eleven Strikers (Wii, 2012) | 15 | 🟡 | C |
| [Mario Superstar Baseball (dtk)](https://github.com/roeming/mssb-dtk) | Matching decompilation of Mario Superstar Baseball (GameCube, 2005) | 15 | 🟢 | C |
| [PokéPark Wii: Pikachu's Adventure](https://github.com/SephDB/pokepark-wii-decomp) | Decompilation of PokéPark Wii: Pikachu's Adventure | 15 | 🟢 | C |
| [Skies of Arcadia Legends](https://github.com/Rainchus/SkiesOfArcadiaLegends) | Matching decompilation of Skies of Arcadia Legends (GameCube, 2002) | 15 | 🟡 | Python |
| [Tiger Woods PGA Tour 2004](https://github.com/mitsevox/tw2004) | Matching decompilation of Tiger Woods PGA Tour 2004 (GameCube, 2003) | 15 | 🟢 | C |
| [Wii Play](https://github.com/akiramusic000/Rhae) | Decompilation of Wii Play | 15 | 🟢 | C |
| [Sonic Riders: Zero Gravity](https://github.com/KidWizardOfTheWeb/SRZGDecomp) | Matching decompilation of Sonic Riders: Zero Gravity (Wii, 2008) | 14 | 🔴 | Assembly |
| [Crash Bandicoot: The Wrath of Cortex (GameCube)](https://github.com/denzi-gh/crashwoc-decomp-gc) | Decompilation of Crash Bandicoot: The Wrath of Cortex (GameCube) | 13 | 🟢 | C |
| [Kirby's Dream Collection Special Edition](https://github.com/Swiftshine/kdc) | Matching decompilation of Kirby's Dream Collection Special Edition (Wii, 2012) | 13 | 🟢 | C |
| [New Play Control! Pikmin](https://github.com/projectPiki/pik1wii) | Matching decompilation of New Play Control! Pikmin (Wii, 2008) | 13 | 🟢 | C |
| [Alice in Wonderland (2010)](https://github.com/Alice-2010/Decomp) | Matching decompilation of Alice in Wonderland (Wii, 2010) | 12 | 🟢 | C |
| [Doshin the Giant](https://github.com/break-core/doshin-gc) | Decompilation of Doshin the Giant | 12 | 🟢 | Python |
| [Sonic Adventure 2: Battle](https://github.com/roeming/SA2B) | Matching decompilation of Sonic Adventure 2: Battle (GameCube, 2001) | 12 | 🟢 | C |
| [Crash Tag Team Racing](https://github.com/bluisblu/cttr) | Matching decompilation of Crash Tag Team Racing (GameCube, 2005) | 11 | 🟢 | C |
| [F-Zero GX (alt)](https://github.com/karamzov123/fzero-gx-decomp) | Matching decompilation of F-Zero GX (GameCube, 2003) | 10 | 🟢 | C |
| [Mortal Kombat: Deception](https://github.com/ShulkMaster/mk-deception) | Matching decompilation of Mortal Kombat: Deception (GameCube, 2004) | 10 | 🟢 | C |
| [F-Zero GX](https://github.com/rayanht/fzgx) | Matching decompilation of F-Zero GX (GameCube, 2003) | 9 | 🟢 | C |
| [Digimon World 4](https://github.com/ivanno4317/dw4-gc) | Decompilation of Digimon World 4 | 8 | 🟢 | C |
| [Luigi's Mansion](https://github.com/SomeJakeGuy/lm-decomp) | Matching decompilation of Luigi's Mansion (GameCube, 2001) | 8 | 🟢 | C |
| [Kirby Air Ride](https://github.com/wowjinxy/KAR) | Matching decompilation of Kirby Air Ride (GameCube, 2003) | 7 | 🟢 | C |
| [Metrowerks CodeWarrior for GameCube (compiler)](https://github.com/rayanht/mwcc) | Decompilation of Metrowerks CodeWarrior for GameCube (compiler) | 7 | 🟢 | C |
| [Summoner: A Goddess Reborn](https://github.com/Charlese2/sgr) | Matching decompilation of Summoner: A Goddess Reborn (GameCube, 2002) | 7 | 🟢 | C |
| [Big Brain Academy: Wii Degree](https://github.com/vabold/bba-wd) | Decompilation of Big Brain Academy: Wii Degree | 6 | 🟡 | Python |
| [Eternal Darkness: Sanity's Requiem](https://github.com/PattyTrish/unending-occlusion) | Matching decompilation of Eternal Darkness: Sanity's Requiem (GameCube, 2002) | 6 | 🟢 | C |
| [Homeland](https://github.com/BttrDrgn/homeland) | Matching decompilation of HomeLand (GameCube, 2005) | 6 | 🔴 | Assembly |
| [Donkey Kong Country Returns](https://github.com/Wexos/DKCR-Decompilation) | Matching decompilation of Donkey Kong Country Returns (Wii, 2010) | 5 | 🟡 | Python |
| [Nintendo Puzzle Collection: Dr. Mario 64](https://github.com/NewGBAXL/drmario64-gc) | Decompilation of Nintendo Puzzle Collection: Dr. Mario 64 | 5 | 🟢 | C |
| [Wario World](https://github.com/sabishii-bit/wwdcmp) | Matching decompilation of Wario World (GameCube, 2003) | 5 | 🟡 | Assembly |
| [Dragon Ball Z: Budokai 2](https://github.com/TotallyNotMichael-GH/dbz2) | Matching decompilation of Dragon Ball Z: Budokai 2 (GameCube, 2004) | 4 | 🟡 | Python |
| [Go Vacation](https://github.com/Moddimation/GoVacation-Decompilation) | Matching decompilation of Go Vacation (Wii, 2011) | 4 | 🗄️ | C |
| [Medal of Honor: Frontline](https://github.com/kyleckroeger/moh-frontline-decomp) | Matching decompilation of Medal of Honor: Frontline (GameCube, 2002) | 4 | 🟢 | C |
| [Medal of Honor: Rising Sun](https://github.com/lifewillbeokay/moh-rising-sun) | Matching decompilation of Medal of Honor: Rising Sun (GameCube, 2003) | 4 | 🟢 | C |
| [I Spy Spooky Mansion](https://github.com/AM7999/ISpy-SM-Decomp) | Decompilation of I Spy Spooky Mansion (Wii), based on the included debug executable | 3 | 🟡 | C++ |
| [Mario Party 6](https://github.com/iirg4x/marioparty6) | Matching decompilation of Mario Party 6 (GameCube, 2004) | 3 | 🟢 | C |
| [NFL Street 2](https://github.com/mitsevox/nflstreet2) | Matching decompilation of NFL Street 2 (GameCube, 2004) | 3 | 🟢 | C++ |
| [Fortune Street](https://github.com/FortuneStreetModding/boom-street-decomp) | Matching decompilation of Fortune Street (Wii, 2011; Boom Street) | 2 | 🟡 | C |
| [Freedom Fighters](https://github.com/andresj-sanchez/frfi-decomp) | Matching decompilation of Freedom Fighters (GameCube, 2003) | 2 | 🟢 | Python |
| [Mario Party 9](https://github.com/ricky074game/marioparty9) | Matching decompilation of Mario Party 9 (Wii, 2012) | 2 | 🟢 | C |
| [Mario Sports Mix](https://github.com/EltyDev/MSM-decomp) | Matching decompilation of Mario Sports Mix (Wii, 2010) | 2 | 🟡 | Python |
| [MVP Baseball 2005](https://github.com/mitsevox/mvp2005) | Matching decompilation of MVP Baseball 2005 (GameCube, 2005) | 2 | 🟢 | C |
| [Wii Fit Plus](https://github.com/Tanline666/veryfat-dungeon) | Decompilation of Wii Fit Plus | 2 | 🟢 | C |
| [Excite Truck](https://github.com/orangedude27/excite-truck) | Matching decompilation of Excite Truck (Wii, 2006) | 1 | 🟢 | Python |
| [Mortal Kombat: Deadly Alliance](https://github.com/ShulkMaster/mk-da) | Matching decompilation of Mortal Kombat: Deadly Alliance (GameCube, 2002) | 1 | 🟢 | C |
| [Radio Helicopter](https://github.com/Bsquo/pcopter_wii) | Decompilation of Radio Helicopter | 1 | 🟡 | C |
| [Super Mario All-Stars 25th Anniversary Edition](https://github.com/ThePlayerRolo/Super-Mario-All-Star-Decomp) | Matching decompilation of Super Mario All-Stars 25th Anniversary Edition (Wii, 2010) | 1 | 🟢 | C |
| [World of Goo (WiiWare)](https://github.com/Fancy2209/wog-wiiware) | Matching decompilation of World of Goo (Wii, 2008; WiiWare) | 1 | 🟡 | C++ |
| [Amazing Island](https://github.com/EltaleLibrarian/Amazing) | Matching decompilation of Amazing Island (GameCube, 2004) | 0 | 🟡 | Python |
| [Mario Superstar Baseball](https://github.com/nlopez99/mssb-decomp) | Matching decompilation of Mario Superstar Baseball (GameCube, 2005) | 0 | 🟢 | C |
| [Taiko no Tatsujin Wii: Ketteiban](https://github.com/CalebPancake/Taiko-No-Tatsujin-Wii-Ketteiban) | Decompilation of Taiko no Tatsujin Wii: Ketteiban | 0 | 🟡 |  |
| [Wario Land: Shake It!](https://github.com/Swiftshine/wlsi) | Matching decompilation of Wario Land: Shake It! (Wii, 2008) | 0 | 🟢 | C |

## Matching Decompilations — Mobile

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Sonic CD (2011 mobile)](https://github.com/RSDKModding/RSDKv3-Decompilation) | Decompilation of Sonic CD (2011 remaster) and Retro Engine v3 (Mobile, 2011) | 709 | 🟢 | C++ |
| [Sonic Runners](https://github.com/itsmattkc/RunnersDecomp) | Matching decompilation of Sonic Runners (Mobile, 2015) | 243 | 🔴 | C# |
| [DoomRPG-RE](https://github.com/Erick194/DoomRPG-RE) | Reverse engineered source of Doom RPG | 159 | 🟡 | C |
| [DoomIIRPG-RE](https://github.com/Erick194/DoomIIRPG-RE) | Reverse engineered source of Doom II RPG | 98 | 🟡 | C++ |
| [Angry Birds](https://github.com/jooapa/Angry_Birds_Decompilation) | Decompilation scripts and instructions for the six classic Angry Birds games (Mobile, 2009–2014) | 50 | 🟡 | Python |
| [Sonic the Hedgehog (J2ME)](https://github.com/Iso-Kilo/Sonic-1-J2ME-Decompilation) | Matching decompilation of Sonic the Hedgehog (J2ME mobile, 2005) | 36 | 🔴 | Java |
| [Geometry Dash](https://github.com/aloaf812/GD) | Decompilation of Geometry Dash v1.710 (Mobile, 2013) | 35 | 🟢 | C++ |
| [Samurai vs Zombies Defense](https://github.com/Decomp-And-Recomp/Samurai-Vs-Zombies) | Decompilation of Samurai vs Zombies Defense by Glu (Mobile, 2012) | 25 | 🟢 | C# |
| [Dragon Ball Legends](https://github.com/GodkuHacking/Dragon-Ball-Legends) | APK decompilation of Dragon Ball Legends (Mobile, 2018) | 16 | 🟡 | Smali |
| [Brave Frontier](https://github.com/decompfrontier/client) | Decompilation of the Brave Frontier client (Mobile, 2013) | 13 | 🟡 | C |
| [SpongeBob Moves In!](https://github.com/Juanen100/SBMI-Decomp) | Decompilation of the Android client of SpongeBob Moves In! (Mobile, 2013) | 13 | 🟢 | C# |
| [Diamond Rush](https://github.com/palaceswitcher/Diamond-Rush-Decomp) | Matching decompilation of Diamond Rush (J2ME mobile, 2006) | 8 | 🟢 | Java |
| [Idle Office Tycoon](https://github.com/Avenze/ios_reverse_engineering) | Reverse engineering notes and decompilation of the iOS game Idle Office Tycoon (Mobile) | 4 | 🟡 | Lua |
| [Skylanders: Cloud Patrol](https://github.com/spyrosadventure/cloud-patrol-decomp) | Decompilation of Skylanders: Cloud Patrol (Mobile, 2012) | 4 | 🟡 | C# |
| [Flappy Bird](https://github.com/fr3dsp/FlappyBird-Decomp) | Decompilation of Flappy Bird (Windows Phone, 2013) | 3 | 🟢 | C# |
| [Bounce](https://github.com/misterjdrg/Bouncer) | Decompilation of Bounce (J2ME mobile, 2001) | 2 | 🟡 | Java |
| [Ancient Empires](https://github.com/Atomk/ancient-empires-1-decompilation) | Matching decompilation of Ancient Empires (J2ME mobile, 2004) | 1 | 🟡 | Java |
| [Defenders & Dragons](https://github.com/Lindarychwalski/Defenders-Dragons) | Decompilation of Defenders & Dragons by Glu (Mobile) | 1 | 🟡 |  |
| [Five Nights at Freddy's](https://github.com/fr3dsp/FNaF-Decomp) | Decompilation of Five Nights at Freddy's (Windows Phone, 2014) | 1 | 🟢 | C# |
| [Five Nights at Freddy's 2](https://github.com/fr3dsp/FNaF-2-Decomp) | Decompilation of Five Nights at Freddy's 2 (Windows Phone, 2014) | 1 | 🟢 | C# |
| [Green Farm 3](https://github.com/SmithGoll/Greenier-Farm-3-Decomp) | Non-matching decompilation of Gameloft's Green Farm 3 (J2ME mobile) | 1 | 🟡 | Java |
| [Mixels Rush](https://github.com/Nugetinc/MixelsRushDecompilation) | Experimental decompilation of Mixels Rush (Mobile, 2015) | 1 | 🟡 |  |
| [Chiki's Chase](https://github.com/gays-studio/ChikisChaseAPK) | Decompiled (apktool) Android build of Chiki's Chase (Mobile) | 0 | 🟡 | Smali |
| [Super Cat Tales: PAWS](https://codeberg.org/heathercat123/PAWS-Decomp) | Decompilation of Super Cat Tales: PAWS (Mobile) |  | ⚪ |  |

## Matching Decompilations — Nintendo 64

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Perfect Dark PC port](https://github.com/perfect-dark-pc-port/perfect_dark) | Port of the Perfect Dark N64 decompilation to modern platforms | 2,049 | 🟢 | C |
| [Paper Mario](https://github.com/pmret/papermario) | Matching decompilation of Paper Mario (Nintendo 64, 2000) | 1,631 | 🟢 | C |
| [Mario Kart 64](https://github.com/n64decomp/mk64) | Matching decompilation of Mario Kart 64 (Nintendo 64, 1996) | 1,310 | 🟢 | C |
| [Perfect Dark decompilation (n64decomp)](https://github.com/n64decomp/perfect_dark) | Matching decompilation of Perfect Dark (N64) | 869 | 🟡 | C |
| [GoldenEye 007 decomp](https://github.com/n64decomp/007) | Matching decompilation of GoldenEye 007 | 798 | 🟢 | C |
| [banjo-kazooie](https://github.com/n64decomp/banjo-kazooie) | Decompilation of Banjo-Kazooie | 650 | 🟢 | C |
| [HackerSM64](https://github.com/HackerN64/HackerSM64) | Super Mario 64 decompilation fork tuned for romhacking | 536 | 🟢 | C |
| [Diddy Kong Racing](https://github.com/DavidSM64/Diddy-Kong-Racing) | Matching decompilation of Diddy Kong Racing (Nintendo 64, 1997) | 422 | 🟢 | C |
| [Star Fox 64](https://github.com/sonicdcer/sf64) | Matching decompilation of Star Fox 64 (Nintendo 64, 1997) | 350 | 🟢 | C |
| [Animal Forest](https://github.com/zeldaret/af) | Matching decompilation of Animal Forest (Nintendo 64, 2001) | 300 | 🟢 | C |
| [oot](https://github.com/n64decomp/oot) | Decompilation of Ocarina of Time Master Quest debug build | 285 | 🗄️ | Assembly |
| [Duke Nukem: Zero Hour](https://github.com/Gillou68310/DukeNukemZeroHour) | Matching decompilation of Duke Nukem: Zero Hour (Nintendo 64, 1999) | 275 | 🟢 | C |
| [Super Smash Bros.](https://github.com/VetriTheRetri/ssb-decomp-re) | Matching decompilation of Super Smash Bros. (Nintendo 64, 1999) | 266 | 🟢 | C |
| [Conker's Bad Fur Day (mkst)](https://github.com/mkst/conker) | Matching decompilation of Conker's Bad Fur Day (Nintendo 64, 2001) | 238 | 🗄️ | C |
| [Doom 64 (DOOM64-RE)](https://github.com/Erick194/DOOM64-RE) | Reverse-engineered source of Doom 64 (Nintendo 64, 1997) | 235 | 🟡 | C |
| [Kirby 64: The Crystal Shards](https://github.com/Kirby64Ret/kirby64) | Matching decompilation of Kirby 64: The Crystal Shards (Nintendo 64, 2000) | 233 | 🟢 | Assembly |
| [Harvest Moon 64](https://github.com/harvestwhisperer/hm64-decomp) | Matching decompilation of Harvest Moon 64 (Nintendo 64, 1999) | 222 | 🟢 | C |
| [Dinosaur Planet](https://github.com/zestydevy/dinosaur-planet) | Matching decompilation of Dinosaur Planet (Nintendo 64, unreleased 2000 build) | 216 | 🟢 | C |
| [Pokémon Stadium](https://github.com/pret/pokestadium) | Matching decompilation of Pokémon Stadium (Nintendo 64, 1999) | 210 | 🟢 | C |
| [Snowboard Kids 2](https://github.com/cdlewis/snowboardkids2-decomp) | Matching decompilation of Snowboard Kids 2 (Nintendo 64, 1999) | 192 | 🟢 | C |
| [libreultra](https://github.com/n64decomp/libreultra) | Matching decompilation of the N64 libultra SDK library | 184 | 🔴 | C |
| [N64 Emulator for GameCube (OoT Master Quest)](https://github.com/zeldaret/oot-gc) | Decompilation of N64 Emulator for GameCube (OoT Master Quest) | 149 | 🟡 | C |
| [Banjo-Tooie](https://github.com/Mr-Wiseguy/banjo-tooie) | Matching decompilation of Banjo-Tooie (Nintendo 64, 2000) | 147 | 🟢 | C |
| [sdk-tools](https://github.com/n64decomp/sdk-tools) | Decompilation of the Nintendo 64 SDK developer tools | 146 | 🔴 | C |
| [majora](https://github.com/n64decomp/majora) | Decompilation of The Legend of Zelda: Majora's Mask | 138 | 🗄️ | C |
| [Wave Race 64](https://github.com/LLONSIT/Wave-Race-64) | Matching decompilation of Wave Race 64 (Nintendo 64, 1996) | 110 | 🟢 | Assembly |
| [F-Zero X](https://github.com/inspectredc/fzerox) | Matching decompilation of F-Zero X (Nintendo 64, 1998) | 106 | 🟢 | C |
| [N64 Emulator for Wii (OoT Virtual Console)](https://github.com/zeldaret/oot-vc) | Decompilation of N64 Emulator for Wii (OoT Virtual Console) | 93 | 🟢 | C |
| [HackerOoT](https://github.com/HackerN64/HackerOoT) | Ocarina of Time decompilation fork tuned for romhacking | 92 | 🟢 | C |
| [Mario Party](https://github.com/mariopartyrd/marioparty) | Matching decompilation of Mario Party (Nintendo 64, 1998) | 81 | 🟢 | C |
| [Dr. Mario 64](https://github.com/AngheloAlf/drmario64) | Matching decompilation of Dr. Mario 64 (Nintendo 64, 2001) | 80 | 🟢 | C |
| [Yoshi's Story](https://github.com/decompals/yoshis-story) | Matching decompilation of Yoshi's Story (Nintendo 64, 1997) | 80 | 🟢 | C |
| [Pilotwings 64](https://github.com/gcsmith/Pilotwings64Decomp) | Matching decompilation of Pilotwings 64 (Nintendo 64, 1996) | 79 | 🟢 | C |
| [Mischief Makers](https://github.com/Drahsid/mischief-makers) | Matching decompilation of Mischief Makers (Nintendo 64, 1997) | 71 | 🟢 | C |
| [Mario Party 3](https://github.com/mariopartyrd/marioparty3) | Matching decompilation of Mario Party 3 (Nintendo 64, 2000) | 69 | 🟢 | C |
| [ultralib](https://github.com/decompals/ultralib) | Reverse engineering of the N64 libultra library | 68 | 🟢 | C |
| [Space Station Silicon Valley](https://github.com/mkst/sssv) | Matching decompilation of Space Station Silicon Valley (Nintendo 64, 1998) | 65 | 🟢 | C |
| [Castlevania 64](https://github.com/k64ret/cv64) | Matching decompilation of Castlevania 64 (Nintendo 64, 1999) | 64 | 🟢 | C |
| [Bomberman Hero](https://github.com/Bomberhackers/bmhero) | Matching decompilation of Bomberman Hero (Nintendo 64, 1998) | 61 | 🟢 | C |
| [Pokémon Stadium 2](https://github.com/pret/pokestadiumgs) | Matching decompilation of Pokémon Stadium 2 (Nintendo 64, 2000) | 57 | 🟢 | C |
| [Jet Force Gemini](https://github.com/Ryan-Myers/Jet-Force-Gemini) | Matching decompilation of Jet Force Gemini (Nintendo 64, 1999) | 53 | 🟢 | C |
| [Mario Party 2](https://github.com/mariopartyrd/marioparty2) | Matching decompilation of Mario Party 2 (Nintendo 64, 1999) | 51 | 🟢 | C |
| [Snowboard Kids](https://github.com/cdlewis/snowboardkids-decomp) | Matching decompilation of Snowboard Kids (Nintendo 64, 1997) | 49 | 🟢 | C |
| [Rocket: Robot on Wheels](https://github.com/RocketRet/Rocket-Robot-On-Wheels) | Matching decompilation of Rocket: Robot on Wheels (Nintendo 64, 1999) | 47 | 🔴 | C |
| [Body Harvest](https://github.com/jaytheham/body-harvest-decompilation) | Matching decompilation of Body Harvest (Nintendo 64, 1998) | 45 | 🟢 | C |
| [Aidyn Chronicles](https://github.com/blackgamma7/Aidyn) | Matching decompilation of Aidyn Chronicles: The First Mage (Nintendo 64, 2001) | 41 | 🟢 | C++ |
| [Pokémon Puzzle League](https://github.com/AngheloAlf/puzzleleague64) | Matching decompilation of Pokémon Puzzle League (Nintendo 64, 1999) | 40 | 🟢 | C |
| [Bomberman 64](https://github.com/Bomberhackers/bm64) | Matching decompilation of Bomberman 64 (Nintendo 64, 1997) | 34 | 🟢 | C |
| [AeroGauge](https://github.com/LLONSIT/AeroGauge) | Matching decompilation of AeroGauge (Nintendo 64, 1997) | 31 | 🟢 | C |
| [F-Zero X (Expansion Kit)](https://github.com/inspectredc/fzerox-expansion-kit) | Matching decompilation of F-Zero X Expansion Kit (Nintendo 64, 2000) | 29 | 🟢 | C |
| [Conker's Bad Fur Day](https://github.com/DevOldSchool/conkers-bfd-decomp) | Matching decompilation of Conker's Bad Fur Day (Nintendo 64, 2001) | 27 | 🟢 | Python |
| [Gauntlet Legends](https://github.com/Drahsid/gauntlet-legends) | Matching decompilation of Gauntlet Legends (Nintendo 64, 1999) | 27 | 🟢 | C |
| [Gex: Enter the Gecko (N64)](https://github.com/MatBourgon/Gex64Decomp) | Decompilation of Gex: Enter the Gecko (N64) | 27 | 🟢 | C |
| [Virtual Pro Wrestling 2](https://github.com/AKI-Club/vpw2) | Matching decompilation of Virtual Pro Wrestling 2 (Nintendo 64, 2000) | 27 | 🟢 | Assembly |
| [Turok 3: Shadow of Oblivion](https://github.com/Drahsid/turok3) | Matching decompilation of Turok 3: Shadow of Oblivion (Nintendo 64, 2000) | 26 | 🗄️ | C |
| [Mario Golf (N64)](https://github.com/monde-lointain/mariogolf64) | Decompilation of Mario Golf (N64) | 23 | 🟢 | C |
| [Superman 64](https://github.com/farisawan-2000/superman) | Matching decompilation of Superman 64 (Nintendo 64, 1999) | 22 | 🔴 | Assembly |
| [Star Wars: Shadows of the Empire](https://github.com/EltaleLibrarian/SotE) | Matching decompilation of Star Wars: Shadows of the Empire (Nintendo 64, 1996) | 20 | 🟡 | C |
| [Star Wars: Rogue Squadron](https://github.com/Tmcg2/rogue_squadron64) | Matching decompilation of Star Wars: Rogue Squadron (Nintendo 64, 1998) | 19 | 🟢 | C |
| [Duke Nukem 64](https://github.com/NBlood/Duke64-RE) | Matching decompilation of Duke Nukem 64 (Nintendo 64, 1997) | 18 | 🟡 | C |
| [Beetle Adventure Racing!](https://github.com/synamaxmusic/bar-decomp) | Matching decompilation of Beetle Adventure Racing! (Nintendo 64, 1999) | 17 | 🟢 | C |
| [Quest 64](https://github.com/Rainchus/Quest64-Decomp) | Matching decompilation of Quest 64 (Nintendo 64, 1998) | 17 | 🟢 | C |
| [Bomberman 64: The Second Attack!](https://github.com/Bomberhackers/bm64tsa) | Matching decompilation of Bomberman 64: The Second Attack! (Nintendo 64, 2000) | 13 | 🟢 | C |
| [Glover (rainchus)](https://github.com/Rainchus/Glover) | Matching decompilation of Glover (Nintendo 64, 1998) | 12 | 🟡 | C |
| [Mario Tennis (N64)](https://github.com/DellM-79/MarioTennisN64) | Decompilation of Mario Tennis (N64) | 12 | 🟡 | C |
| [Chameleon Twist](https://github.com/chameleonTwistRet/chameleonTwistv1.0-JP) | Matching decompilation of Chameleon Twist (Nintendo 64, 1997) | 11 | 🟢 | C |
| [Blast Corps](https://github.com/SlaveOfIDO/blastcorps) | Matching decompilation of Blast Corps (Nintendo 64, 1997) | 10 | 🟢 | C |
| [Mystical Ninja Starring Goemon](https://github.com/klorfmorf/mnsg) | Matching decompilation of Mystical Ninja Starring Goemon (Nintendo 64, 1997) | 10 | 🟢 | C |
| [Doraemon: Nobita to Mittsu no Seireiseki](https://github.com/adipocira/doraemon1) | Matching decompilation of Doraemon: Nobita to Mittsu no Seireiseki (Nintendo 64, 1997) | 8 | 🟢 | C |
| [Virtual Pool 64](https://github.com/LLONSIT/VirtualPool64) | Matching decompilation of Virtual Pool 64 (Nintendo 64, 1998) | 8 | 🔴 | Assembly |
| [LEGO Racers](https://github.com/marijnvdwerf/lego-racers) | Matching decompilation of LEGO Racers (Nintendo 64, 1999) | 7 | 🟡 | Python |
| [Shadowgate 64](https://github.com/Rainchus/ShadowGate64) | Matching decompilation of Shadowgate 64 (Nintendo 64, 1999) | 7 | 🔴 | C |
| [The New Tetris](https://github.com/KiritoDv/tnt) | Matching decompilation of The New Tetris (Nintendo 64, 1999) | 6 | 🗄️ | C |
| [Wonder Project J2](https://github.com/LLONSIT-glitch/wonder) | Matching decompilation of Wonder Project J2 (Nintendo 64, 1996) | 6 | 🟢 | C |
| [Chameleon Twist 2](https://github.com/chameleonTwistRet/chameleonTwist2v1.0-JP) | Matching decompilation of Chameleon Twist 2 (Nintendo 64, 1998) | 5 | 🟢 | C |
| [Paperboy (N64)](https://github.com/marijnvdwerf/paperboy-n64) | Decompilation of Paperboy (N64) | 5 | 🟢 | C |
| [BattleTanx](https://github.com/AbuN64/battletanx-decomp) | Matching decompilation of BattleTanx (Nintendo 64, 1998) | 4 | 🟢 | Linker Script |
| [BattleTanx: Global Assault](https://github.com/TheGh0stShip/BattleTanx-Global-Assault) | Matching decompilation of BattleTanx: Global Assault (Nintendo 64, 1999) | 4 | 🟢 | C |
| [Ridge Racer 64](https://github.com/jvicu2001/rr64-decomp) | Matching decompilation of Ridge Racer 64 (Nintendo 64, 2000) | 4 | 🟡 | Linker Script |
| [Snowboard Kids (sonicdcer)](https://github.com/sonicdcer/sk) | Matching decompilation of Snowboard Kids (Nintendo 64, 1997) | 4 | 🟡 | C |
| [Dark Rift](https://github.com/Unnunu/darkrift) | Matching decompilation of Dark Rift (Nintendo 64, 1997) | 3 | 🟢 | C |
| [Glover](https://github.com/bigyoshi51/glover-decomp) | Matching decompilation of Glover (Nintendo 64, 1998) | 2 | 🟢 | C |
| [Hybrid Heaven](https://github.com/southcitycapture/hybridheaven-decomp) | Matching decompilation of Hybrid Heaven (Nintendo 64, 1999) | 2 | 🟢 | C |
| [Onegai Monsters](https://github.com/Ryan-Myers/onegaimonsters) | Matching decompilation of Onegai Monsters (Nintendo 64, 1999) | 2 | 🟢 | C |
| [Banjo-Kazooie](https://gitlab.com/banjo.decomp/banjo-kazooie) | Matching decompilation of Banjo-Kazooie (Nintendo 64, 1998) |  | ⚪ |  |
| [Donkey Kong 64](https://gitlab.com/dk64_decomp/dk64) | Matching decompilation of Donkey Kong 64 (Nintendo 64, 1999) |  | ⚪ |  |
| [GoldenEye 007](https://gitlab.com/kholdfuzion/goldeneye_src) | Matching decompilation of GoldenEye 007 (Nintendo 64, 1997) |  | ⚪ |  |
| [Perfect Dark](https://gitlab.com/ryandwyer/perfect-dark) | Matching decompilation of Perfect Dark (Nintendo 64, 2000) |  | ⚪ |  |
| [Shiren the Wanderer 2](https://github.com/mschienbein/shiren2-decomp) | Matching decompilation of Shiren the Wanderer 2 (Nintendo 64, 2000) | 0 | 🟢 | C |

## Matching Decompilations — Other / Multi-platform

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Super Mario 64 decomp](https://github.com/n64decomp/sm64) | Matching decompilation of Super Mario 64 | 8,863 | 🟡 | C |
| [Ocarina of Time decomp](https://github.com/zeldaret/oot) | Decompilation of The Legend of Zelda: Ocarina of Time | 5,583 | 🟢 | C |
| [Twilight Princess decomp](https://github.com/zeldaret/tp) | Decompilation of The Legend of Zelda: Twilight Princess | 2,088 | 🟢 | C++ |
| [Majora's Mask decomp](https://github.com/zeldaret/mm) | Decompilation of The Legend of Zelda: Majora's Mask | 1,742 | 🟢 | C |
| [UnityDecompiled](https://github.com/MattRix/UnityDecompiled) | Decompiled C# source of the Unity editor and engine assemblies (now superseded by official reference source) | 1,483 | 🗄️ |  |
| [sm64-port](https://github.com/sm64-port/sm64-port) | Port of the SM64 decompilation to modern devices | 1,309 | 🟡 | C |
| [RSDKv4 Decompilation](https://github.com/RSDKModding/RSDKv4-Decompilation) | Decompilation of Sonic 1 & 2 (2013) and Retro Engine v4 | 1,145 | 🟢 | C++ |
| [Wind Waker decomp](https://github.com/zeldaret/tww) | Decompilation of The Legend of Zelda: The Wind Waker | 1,089 | 🟢 | C++ |
| [RSDKv5-Decompilation](https://github.com/RSDKModding/RSDKv5-Decompilation) | Complete decompilation of Retro Engine v5 (Sonic Mania) | 565 | 🟢 | C++ |
| [s1disasm](https://github.com/sonicretro/s1disasm) | Sonic 1 Disassembly | 449 | 🟢 | Assembly |
| [s2disasm](https://github.com/sonicretro/s2disasm) | Sonic 2 Disassembly | 315 | 🟢 | Assembly |
| [zelda1-disassembly](https://github.com/aldonunez/zelda1-disassembly) | A complete disassembly of The Legend of Zelda | 275 | 🔴 | Assembly |
| [Sonic 3/Sonic & Knuckles Disassembly](https://github.com/sonicretro/skdisasm) | Sonic and Knuckles Disassembly | 263 | 🟢 | Assembly |
| [smb3](https://github.com/captainsouthbird/smb3) | Disassembly of Super Mario Bros 3 | 247 | 🟡 | Assembly |
| [overpy](https://github.com/Zezombye/overpy) | High-level language for the Overwatch Workshop with compile and decompile support | 238 | 🟢 | OverPy |
| [bo1-zombies-decompiled](https://github.com/MisaDev4/bo1-zombies-decompiled) | Decompiled GSC scripts of Call of Duty: Black Ops 1 Zombies | 209 | 🟢 | C++ |
| [v-decompiled-scripts](https://github.com/root-cause/v-decompiled-scripts) | Decompiled GTA V game scripts | 162 | 🗄️ | C |
| [WorldOfTanks-Decompiled](https://github.com/StranikS-Scan/WorldOfTanks-Decompiled) | Unpacked and decompiled versions of xml- and pyc-files of WorldOfTanks | 149 | 🟢 | Python |
| [RSDKv4-Script-Decompilation](https://github.com/RSDKModding/RSDKv4-Script-Decompilation) | Decompiled scripts of Retro Engine v4 games (Sonic 1/2 mobile) | 141 | 🟢 |  |
| [RSDKv3-Script-Decompilation](https://github.com/RSDKModding/RSDKv3-Script-Decompilation) | Decompiled scripts of Retro Engine v3 (Sonic CD) | 138 | 🟢 |  |
| [RuneScape Classic client (2003scape rsc-c)](https://github.com/2003scape/rsc-c) | RuneScape Classic client ported to C, with builds for PC, Wii, 3DS and Switch | 134 | 🟢 | C |
| [FF Disassembly](https://github.com/Entroper/FF1Disassembly) | Disassembly of Final Fantasy (Assembly) | 106 | 🟢 | Assembly |
| [YandereSimulatorDecompiled](https://github.com/LordEnma/YandereSimulatorDecompiled) | Decompiled code of the game Yandere Simulator | 101 | 🟢 | C# |
| [ChoplifterReverse](https://github.com/blondie7575/ChoplifterReverse) | Full reverse engineered source of the Apple II game Choplifter | 99 | 🟡 | Assembly |
| [CircleShootApp](https://github.com/alula/CircleShootApp) | Zuma Deluxe 1.0.0 decompilation | 98 | 🟢 | C++ |
| [lode_runner_reveng](https://github.com/XekriRedmane/lode_runner_reveng) | Reverse engineering of Lode Runner for the Apple II | 96 | 🟢 | TeX |
| [Paleblood](https://github.com/Yharnam-Hunters/Paleblood) | Decompilation of Bloodborne v1.09 with its own runtime | 88 | 🟢 | Python |
| [Final Fantasy VI Disassembly](https://github.com/everything8215/ff6) | Disassembly and ROM info for Final Fantasy VI | 87 | 🟢 | Assembly |
| [PvZ-TV-Touch](https://github.com/WuDi-ZhanShen/PvZ-TV-Touch) | Decompiled Java source of Android Plants vs. Zombies TV edition, adapted for touch | 82 | 🟡 |  |
| [Pokémon Puzzle Challenge](https://github.com/pret/pokepuzzle) | Disassembly of Pokémon Puzzle Challenge | 80 | 🟢 | Assembly |
| [GTA-V-Decompiled-Scripts](https://github.com/calamity-inc/GTA-V-Decompiled-Scripts) | All decompiled GTA V .ysc game scripts, including native tables | 79 | 🟢 | C |
| [StardewValleyDecompiled](https://github.com/Dannode36/StardewValleyDecompiled) | Stardew Valley 1.6 decompiled to .NET 6 | 79 | 🟡 | C# |
| [The Legend of Zelda](https://github.com/camthesaxman/zeldasource) | Disassembly of Legend of Zelda | 77 | 🔴 | Assembly |
| [gridrunner](https://github.com/mwenge/gridrunner) | Reverse-engineered source of Gridrunner (1982) by Jeff Minter | 75 | 🔴 | Assembly |
| [jetpac-disassembly](https://github.com/mrcook/jetpac-disassembly) | Fully annotated disassembly of JETPAC (ZX Spectrum) | 75 | 🟢 | Assembly |
| [re47](https://github.com/0danny/re47) | Hitman: Codename 47 decompilation project (archived) | 75 | 🗄️ | C++ |
| [Terraria (Old-Gen Console)](https://github.com/PPrism/TerrariaOGC) | Functional decompilation and PC port of the Xbox 360 / PS3 version of Terraria (2013) | 65 | 🟢 | C# |
| [smb-decomp](https://github.com/camthesaxman/smb-decomp) | Decompilation of Super Monkey Ball | 64 | 🔴 | Assembly |
| [bookstory-en](https://github.com/xraymemory/bookstory-en) | Decompilation and English translation of the game BookStory | 61 | 🔴 | VBA |
| [s2smsdisasm](https://github.com/sonicretro/s2smsdisasm) | Sonic 2 SMS Disassembly | 59 | 🔴 | Assembly |
| [th07](https://github.com/some100/th07) | Decompilation of Touhou 7 Perfect Cherry Blossom 1.00b | 57 | 🟢 | C++ |
| [th105](https://github.com/N0zoM1z0/th105) | Source reconstruction of Touhou Scarlet Weather Rhapsody 1.06a | 57 | 🟢 | C++ |
| [BldMystery](https://github.com/smartblade/BldMystery) | Source code recovery of Severance: Blade of Darkness | 56 | 🟢 | Assembly |
| [Guitar Hero: Warriors of Rock](https://github.com/kernaltrap8/WoR-Plus) | Quality-of-life mod for Guitar Hero: Warriors of Rock (PS3 / Xbox 360, 2010) | 54 | 🟡 | HiveQL |
| [sead](https://github.com/aboood40091/sead) | Decompilation of Nintendo EAD's sead engine library | 54 | 🟢 | C++ |
| [BounceTales](https://github.com/HelloOO7/BounceTales) | Decompilation of Rovio's Bounce Tales (2008) for Nokia phones | 52 | 🔴 | Java |
| [Thunderball](https://github.com/teampopwork/Thunderball) | Decompilation of Peggle Deluxe 1.01 | 51 | 🟢 | C++ |
| [stfdisasm](https://github.com/biggestsonicfan/stfdisasm) | Sonic the Fighters Disassembly | 49 | 🟢 | Assembly |
| [dx-ball](https://github.com/N0zoM1z0/dx-ball) | Source reconstruction of DX-Ball 1.07 verified against the original binary | 47 | 🟢 | Python |
| [hmfomt](https://github.com/not-alons/hmfomt) | Disassembly/decompilation of Harvest Moon: Friends of Mineral Town | 47 | 🔴 | Assembly |
| [mp3](https://github.com/PartyPlanner64/mp3) | Mario Party 3 decompilation | 47 | 🗄️ | C |
| [agl](https://github.com/open-ead/agl) | Decompilation of agl, a graphics library used in first-party Nintendo games | 46 | 🟢 | C++ |
| [Ballanced](https://github.com/doyaGu/Ballanced) | Reversed source code of the game Ballance | 45 | 🟢 | CMake |
| [Source-2-Decompiler](https://github.com/Dingf/Source-2-Decompiler) | Decompiler for Source 2 file formats | 45 | 🔴 | C++ |
| [Celeste_Decompiled](https://github.com/TheCyndaquilDecompilers/Celeste_Decompiled) | Decompiled source of Celeste (XNA build 1.4.0.0) | 44 | 🔴 | C# |
| [bn6f](https://github.com/dism-exe/bn6f) | Disassembly of MegaMan Battle Network 6 Cybeast Falzar | 43 | 🟢 | Assembly |
| [New Super Mario Bros. U](https://github.com/aboood40091/red-pro2) | Matching decompilation of New Super Mario Bros. U (Wii U, 2012; v1.3.0) | 43 | 🟢 | C++ |
| [EoSDecomp](https://github.com/wearrrrr/EoSDecomp) | Byte-accurate decompilation of Touhou 6 Embodiment of Scarlet Devil | 42 | 🟡 | C++ |
| [GD-2.206-Decompiled](https://github.com/CallocGD/GD-2.206-Decompiled) | Decompilation attempt of Geometry Dash 2.206 | 42 | 🟡 | C++ |
| [SCI-Decompilation-Archive](https://github.com/EricOakford/SCI-Decompilation-Archive) | Collection of decompiled source code for Sierra's SCI games | 41 | 🟡 | Scala |
| [Knuckles' Chaotix Disassembly](https://github.com/sonicretro/chaotix) | Knuckles' Chaotix Disassembly & Toolkit | 40 | 🟢 | Assembly |
| [rr-decomp](https://github.com/kazuyette/rr-decomp) | Matching decompilation of Ridge Racer (PlayStation, Namco, 1994, SLPS-00001), and a static recompilation that boots a... | 40 | 🟢 | C |
| [spindisasm](https://github.com/sonicretro/spindisasm) | Sonic Spinball Disassembly | 40 | 🔴 | Assembly |
| [SCUMM-Decompilation-Archive](https://github.com/EricOakford/SCUMM-Decompilation-Archive) | Collection of decompiled source code for Lucasfilm's SCUMM games | 39 | 🟡 | C |
| [habbo_src](https://github.com/Quackster/habbo_src) | Archive of decompiled Habbo client files from 2001-2009 | 37 | 🟢 | LiveScript |
| [lm-decomp](https://github.com/ThePlayerRolo/lm-decomp) | Decompilation of Luigi's Mansion | 37 | 🗄️ | C |
| [samp-source](https://github.com/Dryxio/samp-source) | Byte-for-byte source rebuild of SA-MP 0.3.7 R5 | 37 | 🟢 | C++ |
| [deltamodkit](https://github.com/deltamodders/deltamodkit) | DELTARUNE GameMaker decompilation/port with modding support | 36 | 🟢 | Game Maker Language |
| [Blood-RE](https://github.com/NBlood/Blood-RE) | Blood source code reconstruction (matching decompilation) | 35 | 🟢 | C++ |
| [byte-tactics](https://github.com/HectorBailey/byte-tactics) | Matching decompilation of Total Annihilation | 35 | 🟢 | C++ |
| [Final Fantasy IV Disassembly](https://github.com/everything8215/ff4) | Final Fantasy IV Disassembly | 35 | 🔴 | Assembly |
| [C64 Wizard of Wor Disassembly](https://github.com/dabadab/wizardofwor) | Wizard of Wor for C64 disassembly | 33 | 🔴 | Assembly |
| [decomp](https://github.com/cuellius/decomp) | Mount & Blade: Warband module decompiler | 33 | 🔴 | C# |
| [Metroid Disassembly](https://github.com/nmikstas/metroid-disassembly) | Metroid software disassembly | 32 | 🟡 | Assembly |
| [PaRappaSource](https://github.com/cuckydev/PaRappaSource) | PaRappa the Rapper decompilation | 32 | 🔴 | C |
| [Most-Wanted-Vehicles-Decomp](https://github.com/Brawltendo/Most-Wanted-Vehicles-Decomp) | Matching decompilation of Need for Speed Most Wanted vehicle physics | 31 | 🔴 | C++ |
| [s3ddisasm](https://github.com/sonicretro/s3ddisasm) | Sonic 3D Blast Disassembly | 30 | 🔴 | Assembly |
| [SADX-cutscene-decompilation](https://github.com/X-Hax/SADX-cutscene-decompilation) | Decompilation of Sonic Adventure DX cutscenes | 30 | 🟡 | C++ |
| [th04](https://github.com/N0zoM1z0/th04) | Source reconstruction of Touhou 4 Lotus Land Story | 30 | 🟢 | Python |
| [Exile disassembly](https://github.com/tom-seddon/exile_disassembly) | Commented, buildable disassembly of the classic BBC Micro game | 29 | 🗄️ | TypeScript |
| [RDR3-Decompiled-Scripts](https://github.com/kepmehz/RDR3-Decompiled-Scripts) | Red Dead Redemption 2 .ysc game scripts decompiled to C with natives and strings | 28 | 🔴 | C |
| [RedCarpet-S](https://github.com/fruityloops1/RedCarpet-S) | Super Mario 3D World + Bowser's Fury 1.1 decompilation | 28 | 🟡 | C++ |
| [sbk-decomp](https://github.com/tenry92/sbk-decomp) | Snowboard Kids decompilation | 28 | 🔴 | C |
| [Pizza-Tower-EXtracted](https://github.com/setupwitch/Pizza-Tower-EXtracted) | Semi-accurate decompilation of Pizza Tower | 26 | 🟢 | Game Maker Language |
| [Thrust Disassembly](https://github.com/kieranhj/thrust-disassembly) | Reverse engineered source to BBC Thrust | 26 | 🟢 | Assembly |
| [spyro-3](https://github.com/TheMobyCollective/spyro-3) | Spyro: Year of the Dragon decompilation project | 25 | 🟢 | Assembly |
| [Manic Miner disassembly](https://github.com/skoolkid/manicminer) | A disassembly of Manic Miner, created using SkoolKit. | 24 | 🟢 | Python |
| [totkol](https://github.com/jiangzhengwenjz/totkol) | Decompilation of Tactics Ogre: The Knight of Lodis (USA) | 24 | 🟡 | Assembly |
| [bomberman-64](https://github.com/MarioMaster96/bomberman-64) | Bomberman 64 decompilation | 23 | 🔴 | Assembly |
| [Eushully-Decompiler](https://github.com/Kelebek1/Eushully-Decompiler) | Decompiler and recompiler for Eushully AGE engine scripts | 23 | 🟡 | C++ |
| [fft_decomp](https://github.com/adamrt/fft_decomp) | Decompilation of Final Fantasy Tactics (PlayStation, NA) | 23 | 🟢 | C |
| [th095](https://github.com/N0zoM1z0/th095) | Source reconstruction of Touhou Shoot the Bullet 1.02a | 23 | 🟢 | C++ |
| [WinFish](https://github.com/Vindirect/WinFish) | Insaniquarium Deluxe 1.1 decompilation | 23 | 🟢 | C |
| [Burnout Paradise](https://github.com/BurnoutHints/b5-decomp) | Decompilation of Burnout Paradise | 22 | 🟡 | C++ |
| [Ultimate Play the Game disassemblies](https://github.com/pobtastic/ultimate) | A disassembly of various "Ultimate Play the Game" games, created using SkoolKit. | 22 | 🟡 | Visual Basic 6.0 |
| [BBTools](https://github.com/JonMagon/BBTools) | Disassembly analysis and collection of tools for Beasts and Bumpkins (1997) | 21 | 🟢 | C# |
| [DiamondRushSource](https://github.com/kubikaugustyn/DiamondRushSource) | Decompilation of Gameloft's Diamond Rush (2006) for Nokia phones | 21 | 🟡 | Java |
| [gcx_decompiler](https://github.com/oct0xor/gcx_decompiler) | Decompiler for GCX/GCL scripts in Metal Gear Solid games | 21 | 🔴 | Python |
| [Mario vs. Donkey Kong](https://github.com/camthesaxman/mariovsdk) | Disassembly of Mario vs. Donkey Kong | 21 | 🟡 | Assembly |
| [Cave-Story-Decompilation](https://github.com/GabrielRavier/Cave-Story-Decompilation) | Decompilation of Cave Story | 20 | 🗄️ | Assembly |
| [Cuphead-Decomp](https://github.com/tanosshi/Cuphead-Decomp) | Unofficial decompilation of Cuphead | 20 | 🟢 | C# |
| [n64dd](https://github.com/Decompollaborate/n64dd) | Decompilation of the n64dd file in Ocarina of Time | 20 | 🟡 | C |
| [Sonic CD Disassembly](https://github.com/sonicretro/scddisasm) | Disassembly of Sonic CD (Assembly) | 20 | 🟢 | Assembly |
| [Donkey-Kong-Country-2-Disassembly](https://github.com/Yoshifanatic1/Donkey-Kong-Country-2-Disassembly) | Disassembly of Donkey Kong Country 2 (Assembly) | 19 | 🔴 | Assembly |
| [Final Fantasy V Disassembly](https://github.com/everything8215/ff5) | Disassembly and ROM info for Final Fantasy V | 19 | 🟢 | Assembly |
| [Jet Set Willy disassembly](https://github.com/skoolkid/jetsetwilly) | A disassembly of Jet Set Willy, created using SkoolKit. | 19 | 🟢 | Python |
| [Manic Miner (BBC)](https://github.com/TobyLobster/ManicMiner) | Disassembly of the original BBC Micro version of Manic Miner | 17 | 🟡 |  |
| [psychonauts-decomp](https://github.com/DrDecki/psychonauts-decomp) | Decompilation project for Psychonauts | 16 | 🟢 | C |
| [shiren](https://github.com/CelestialAmber/shiren) | Disassembly of Fushigi no Dungeon 2: Fuurai no Shiren | 15 | 🔴 | Assembly |
| [smb2j-disassembly](https://github.com/threecreepio/smb2j-disassembly) | ca65 version of doppelgangers fantastic smb2j disassembly | 15 | 🟡 | Assembly |
| [raymanarenadecomp](https://github.com/zZeck/raymanarenadecomp) | Rayman Arena decompilation early WIP made possible with Frida, Ghidra, Clang tools, and brains. | 14 | 🔴 | C++ |
| [Splatoon](https://github.com/Dexx-io/Splatoon-Decomp) | Matching decompilation of Splatoon (Wii U, 2015) | 14 | 🟡 |  |
| [Pokered-Pro](https://github.com/Kamy41/Pokered-Pro) | Disassembly of Pokémon Red/Blue with some fixies and improvements (and a little surprise at Vermilion Dock if you tal... | 13 | 🟢 | Assembly |
| [The Hobbit disassembly](https://github.com/pobtastic/hobbit) | A disassembly of The Hobbit, created using SkoolKit. | 13 | 🟡 | Visual Basic 6.0 |
| [Rex disassembly](https://github.com/ultrabolido/skRex) | A disassembly of Rex, created using SkoolKit. | 11 | 🔴 | CSS |
| [The Way of the Exploding Fist disassembly](https://github.com/pobtastic/wayoftheexplodingfist) | A disassembly of The Way of the Exploding Fist, created using SkoolKit. | 11 | 🟡 | Visual Basic 6.0 |
| [Skate](https://github.com/Skate-Modding-Team/Skate-Decompilation-Project) | Decompilation of Skate | 10 | 🟢 | C++ |
| [Disassembly of Boulder Dash for the BBC Micro](https://github.com/TobyLobster/Boulderdash) | Disassembly of the game Boulderdash on the BBC Micro | 9 | 🟡 | Assembly |
| [chuckie](https://github.com/Ritchie333/chuckie) | Disassembly of the classic 1983 ZX Spectrum game "Chuckie Egg" | 8 | 🟡 | Visual Basic 6.0 |
| [nhl94-disassembly](https://github.com/Chaos81/nhl94-disassembly) | Attempt to reverse engineer the disassembled ROM of NHL94 using the NHL Hockey source code | 8 | 🟢 | Assembly |
| [Soulcalibur II](https://github.com/Soulcalibur-II-Research-Group/scII_re) | Decompilation of Soulcalibur II | 8 | 🟢 |  |
| [Batty disassembly](https://github.com/pobtastic/batty) | A disassembly of Batty, created using SkoolKit. | 7 | 🟡 | Visual Basic 6.0 |
| [Kirby's Dream Land 3 Disassembly](https://github.com/Yoshifanatic1/Kirbys-Dream-Land-3-Disassembly) | Disassembly of Kirby's Dream Land 3 (Assembly) | 7 | 🔴 | Assembly |
| [Mortal Kombat 3D-era](https://github.com/cScarletter/MK-3D-Era-Decompilation) | Research and decompilation of Mortal Kombat: Deadly Alliance, Deception and Armageddon (multi-platform, 2002–2006) | 7 | 🟡 | C |
| [West Bank](https://github.com/pobtastic/westbank) | A disassembly of West Bank, created using SkoolKit. | 7 | 🔴 | Visual Basic 6.0 |
| [Yoshi's Woolly World](https://github.com/Swiftshine/yww) | Matching decompilation of Yoshi's Woolly World (Wii U, 2015) | 7 | 🟡 | C++ |
| [Alphabet Park Adventure](https://github.com/unspDecomp/abcParkDecomp) | Matching decompilation of Alphabet Park Adventure (V.Smile, 2004) | 6 | 🟡 | C |
| [Back to Skool disassembly](https://github.com/skoolkid/backtoskool) | A disassembly of Back to Skool, created using SkoolKit. | 6 | 🟢 | Python |
| [Booty disassembly](https://github.com/pobtastic/booty) | A disassembly of Booty, created using SkoolKit. | 6 | 🟡 | Visual Basic 6.0 |
| [Hungry Horace disassembly](https://github.com/skoolkid/hungryhorace) | A disassembly of Hungry Horace, created using SkoolKit. | 6 | 🟢 | Shell |
| [mm4](https://github.com/captainsouthbird/mm4) | Disassembly of Mega Man 4 | 6 | 🔴 | Assembly |
| [Phantasy Star IV Disassembly](https://github.com/squidfeatures/ps4disasm) | Phantasy Star IV Disassembly | 6 | 🔴 | Assembly |
| [Skool Daze disassembly](https://github.com/skoolkid/skooldaze) | A disassembly of Skool Daze, created using SkoolKit. | 6 | 🟢 | Python |
| [Battlezone disassembly (ZX Spectrum)](https://github.com/pobtastic/battlezone) | A disassembly of Battlezone, created using SkoolKit. | 5 | 🟡 | Visual Basic 6.0 |
| [Jason's Gem disassembly](https://github.com/pobtastic/jasons-gem) | A disassembly of Jason's Gem, created using SkoolKit. | 5 | 🟡 | Visual Basic 6.0 |
| [Rampage disassembly](https://github.com/pobtastic/rampage) | A disassembly of Rampage, created using SkoolKit. | 5 | 🟡 | Visual Basic 6.0 |
| [Wheelie disassembly](https://github.com/pobtastic/wheelie) | A disassembly of Wheelie, created using SkoolKit. | 5 | 🟡 | Visual Basic 6.0 |
| [Contact Sam Cruise disassembly](https://github.com/skoolkid/contactsamcruise) | A disassembly of Contact Sam Cruise, created using SkoolKit. | 4 | 🟢 | Python |
| [Harrier Attack disassembly](https://github.com/pobtastic/harrierattack) | A disassembly of Harrier Attack, created using SkoolKit. | 4 | 🟡 | Visual Basic 6.0 |
| [Speedy Gonzales: Los Gatos Banditos Disassembly](https://github.com/Yoshifanatic1/Speedy-Gonzales-Los-Gatos-Banditos-Disassembly) | Disassembly of Speedy Gonzales: Los Gatos Bandidos (Assembly) | 4 | 🔴 | Assembly |
| [The Lord of the Rings: The Return of the King](https://github.com/crimsonmagick/lotr-rotk) | Decompilation of The Lord of the Rings: The Return of the King | 4 | 🟡 |  |
| [Phantasy Star Disassembly](https://github.com/sung3r/ps1disasm) | Phantasy Star Disassembly | 3 | 🔴 | Assembly |
| [180 disassembly](https://github.com/pobtastic/180) | A disassembly of 180, created using SkoolKit. | 2 | 🟡 | Visual Basic 6.0 |
| [Armored Unit](https://github.com/Normmatt/unarmoredunit) | Matching decompilation of Armored Unit (WonderSwan, 2000) | 2 | 🟢 | C |
| [Dragster-Disassembly](https://github.com/CelestialAmber/Dragster-Disassembly) | Disassembly of Dragster | 2 | 🔴 | Assembly |
| [Fate/EXTELLA](https://github.com/bIue9076r/fate-extella-decompilation) | Decompilation of Fate/EXTELLA | 2 | 🟡 | C |
| [Hollywood Poker disassembly](https://github.com/pobtastic/hollywoodpoker) | A disassembly of Hollywood Poker, created using SkoolKit. | 2 | 🟡 | Visual Basic 6.0 |
| [How to be a Complete Bastard disassembly](https://github.com/pobtastic/howtobeacompletebastard) | A disassembly of How To Be A Complete Bastard, created using SkoolKit. | 2 | 🟢 | Python |
| [Mario Teaches Typing 3](https://github.com/EliasFever/MarioTeachesTyping3Decomp) | Decompilation of Mario Teaches Typing 3 | 2 | 🟢 | GDScript |
| [Phantasy Star III Disassembly](https://github.com/brecert/ps3disasm) | Phantasy Star III Disassembly | 2 | 🔴 | Assembly |
| [Splitting Images/ Split Personalities disassembly](https://github.com/pobtastic/splittingimages) | A disassembly of Splitting Images, created using SkoolKit. | 2 | 🟡 | Visual Basic 6.0 |
| [Terminator Salvation](https://github.com/connieprice/Terminator-Salvation-Lua) | Decompilation of Terminator Salvation | 2 | 🟡 | Lua |
| [Percy the Potty Pigeon disassembly](https://github.com/pobtastic/percythepottypigeon) | A disassembly of Percy The Potty Pigeon, created using SkoolKit. | 1 | 🟢 | Visual Basic 6.0 |
| [Sonic the Hedgehog (DIDJ)](https://github.com/ArchiverXP/sncdecomp) | Matching decompilation of Sonic the Hedgehog (LeapFrog Didj, 2008) | 1 | 🟡 | C++ |
| [ABM Disassembly](https://6502disassembly.com/a2-abm/ABM.html) | Disassembly of ABM (Assembly) |  | ⚪ |  |
| [Adventure Disassembly](https://www.qotile.net/minidig/disassembly/adventure.asm) | Disassembly of Adventure (Assembly) |  | ⚪ |  |
| [Air-Sea Battle Disassembly](https://www.qotile.net/minidig/disassembly/air_sea_battle.asm) | Disassembly of Air-Sea Battle (Assembly) |  | ⚪ |  |
| [Alleyway](https://github.com/CelestialAmber/alleyway) | Disassembly of Alleyway | 0 | 🔴 | Assembly |
| [Berzerk Disassembly](https://www.qotile.net/minidig/disassembly/berzerk.asm) | Disassembly of Berzerk (Assembly) |  | ⚪ |  |
| [Bomber Disassembly](https://6502disassembly.com/a2-bomber/Bomber.html) | Disassembly of Bomber (Assembly) |  | ⚪ |  |
| [Chernobyl Neighbor: Clown Gang](https://github.com/smolkrieger/nuclear-neighbor) | Decompilation of Chernobyl Neighbor: Clown Gang | 0 | 🟡 |  |
| [Combat Disassembly](https://www.qotile.net/minidig/disassembly/dicombat.asm) | Disassembly of Combat (Assembly) |  | ⚪ |  |
| [Cosmic Ark Disassembly](https://www.qotile.net/minidig/disassembly/CosmicArk.asm) | Disassembly of Cosmic Ark (Assembly) |  | ⚪ |  |
| [CSBwin](http://www.dianneandpaul.net/CSBwin/) | Disassembly of Dungeon Master (C++) |  | ⚪ |  |
| [Disassemblies of classic BBC Micro games](https://www.level7.org.uk/miscellany) | Disassembly of Atic Atac, Boffin (Assembly) |  | ⚪ |  |
| [Donkey Kong Disassembly](https://www.qotile.net/minidig/disassembly/dk.asm) | Disassembly of Donkey Kong (Assembly) |  | ⚪ |  |
| [Exile (Enhanced version) disassembly](https://level7.org.uk/miscellany/exile-enhanced-disassembly.txt) | Disassembly of Exile (Assembly) |  | ⚪ |  |
| [Indy 500 Disassembly](https://www.qotile.net/minidig/disassembly/indy_500_pass_01.asm) | Disassembly of Indy 500 (Assembly) |  | ⚪ |  |
| [Jawbreaker Disassembly](https://www.qotile.net/minidig/disassembly/jaw_breaker.asm) | Disassembly of Jawbreaker (Assembly) |  | ⚪ |  |
| [Kaboom! Disassembly](https://www.qotile.net/minidig/disassembly/kaboom.asm) | Disassembly of Kaboom! (Assembly) |  | ⚪ |  |
| [Outlaw Disassembly](https://www.qotile.net/minidig/disassembly/outlaw.asm) | Disassembly of Outlaw (Assembly) |  | ⚪ |  |
| [Pitfall! Disassembly](https://www.qotile.net/minidig/disassembly/pitfall.asm) | Disassembly of Pitfall! (Assembly) |  | ⚪ |  |
| [Red vs. Blue Disassembly](https://www.qotile.net/minidig/disassembly/redblue.asm) | Disassembly of RealSports Football (Assembly) |  | ⚪ |  |
| [Riddle of the Sphinx Disassembly](https://www.qotile.net/minidig/disassembly/riddle-pal.asm) | Disassembly of Riddle of the Sphinx (Assembly) |  | ⚪ |  |
| [River Raid Disassembly](https://www.qotile.net/minidig/disassembly/RiverRaid.asm) | Disassembly of River Raid (Assembly) |  | ⚪ |  |
| [Space Jockey Disassembly](https://www.qotile.net/minidig/disassembly/space_jockey.asm) | Disassembly of Space Jockey (Assembly) |  | ⚪ |  |
| [Starmaster Disassembly](https://www.qotile.net/minidig/disassembly/Starmaster.asm) | Disassembly of Starmaster (Assembly) |  | ⚪ |  |
| [Surround Disassembly](https://www.qotile.net/minidig/disassembly/surround.asm) | Disassembly of Surround (Assembly) |  | ⚪ |  |
| [The A-Team Disassembly](https://www.qotile.net/minidig/disassembly/a-team.asm) | Disassembly of The A-Team (Assembly) |  | ⚪ |  |
| [Venture Disassembly](https://www.qotile.net/minidig/disassembly/venture.asm) | Disassembly of Venture (Assembly) |  | ⚪ |  |

## Matching Decompilations — PC / DOS / Windows

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Devilution](https://github.com/diasurgical/devilution) | Reverse-engineered Diablo 1 source reconstructed from the original binary | 9,001 | 🟡 | C++ |
| [Ship of Harkinian](https://github.com/HarbourMasters/Shipwright) | PC port of Ocarina of Time built on the OoT decompilation | 5,581 | 🟢 | C |
| [Space Cadet Pinball](https://github.com/k4zmu2a/SpaceCadetPinball) | Decompilation of 3D Pinball for Windows – Space Cadet (PC, 1995) | 4,698 | 🟡 | C++ |
| [LEGO Island](https://github.com/isledecomp/isle) | Matching decompilation of LEGO Island (PC, 1997) | 3,485 | 🟢 | C++ |
| [2 Ship 2 Harkinian](https://github.com/2ship2harkinian/2ship2harkinian) | PC port of Majora's Mask built on the MM decompilation | 2,313 | 🟢 | C |
| [SDLPoP](https://github.com/NagyD/SDLPoP) | An open-source port of Prince of Persia, based on the disassembly of the DOS version. | 1,296 | 🟢 | C |
| [gta-reversed](https://github.com/gta-reversed/gta-reversed) | Reimplementation of GTA San Andreas 1.0 US via reverse engineering | 1,044 | 🟢 | C++ |
| [Touhou (PC-98) (ReC98)](https://github.com/nmlgc/ReC98) | Decompilation of Touhou (PC-98) (ReC98) | 876 | 🟢 | Assembly |
| [Sonic Mania (RSDKModding)](https://github.com/RSDKModding/Sonic-Mania-Decompilation) | Matching decompilation of Sonic Mania and its Retro Engine (RSDKv5) (PC, 2017) | 815 | 🟢 | C |
| [Touhou 06: The Embodiment of Scarlet Devil](https://github.com/GensokyoClub/th06) | Matching decompilation of Touhou 06: The Embodiment of Scarlet Devil (PC, 2002) | 613 | 🟢 | C++ |
| [reVC](https://github.com/mrxenginner/reVC) | Reverse engineered source of GTA Vice City (reVC) | 418 | 🟢 | C++ |
| [Fallout 2 (fallout2-re)](https://github.com/alexbatalov/fallout2-re) | Reverse-engineered source of Fallout 2 (PC, 1998) | 409 | 🟡 | C |
| [reconstruction-of-zzt](https://github.com/asiekierka/reconstruction-of-zzt) | Reconstructed source code of ZZT | 385 | 🟡 | Pascal |
| [Deus Ex: Human Revolution (cdcEngine)](https://github.com/rrika/cdcEngineDXHR) | Decompilation of Deus Ex: Human Revolution and its cdcEngine (PC, 2011) | 323 | 🟢 | C++ |
| [starflight-reverse](https://github.com/s-macke/starflight-reverse) | Reverse-engineered Forth source of the 1986 DOS game Starflight | 236 | 🟢 | C |
| [re-plants-vs-zombies](https://github.com/Patoke/re-plants-vs-zombies) | Rebuild of Plants vs. Zombies GOTY functionality via reverse engineering | 233 | 🟢 | C++ |
| [Need for Speed: Most Wanted](https://github.com/dbalatoni13/nfsmw) | Matching decompilation of Need for Speed: Most Wanted (PC, 2005) | 219 | 🟢 | C++ |
| [Crimsonland](https://github.com/banteg/crimson) | Matching decompilation of Crimsonland (PC, 2003) | 186 | 🟢 | Python |
| [D2MOO](https://github.com/ThePhrozenKeep/D2MOO) | Reimplementation of Diablo II game code with patching facilities for modders | 181 | 🟢 | C++ |
| [fallout1-re](https://github.com/alexbatalov/fallout1-re) | Reverse engineered source of Fallout 1 | 177 | 🔴 | C |
| [Chronoshift](https://github.com/TheAssemblyArmada/Chronoshift) | Open source reimplementation of Red Alert in C++ | 175 | 🗄️ | C++ |
| [sci-scripts](https://github.com/sluicebox/sci-scripts) | Decompiled scripts of Sierra SCI adventure games | 151 | 🟢 | SuperCollider |
| [SA-MP](https://github.com/dashr9230/SA-MP) | Matching decompilation of San Andreas Multiplayer 0.3.7 | 147 | 🟢 | C |
| [GD-Decompiled](https://github.com/Wyliemaster/GD-Decompiled) | Attempt to recover Geometry Dash 2.11 source through reverse engineering | 146 | 🗄️ | C++ |
| [Cosmo's Cosmic Adventure](https://github.com/smitelli/cosmore) | Matching decompilation of Cosmo's Cosmic Adventure (DOS, 1992) | 145 | 🟡 | C |
| [Spider-Man (2000)](https://github.com/krystalgamer/spidey-decomp) | Decompilation of the PC port of Neversoft's Spider-Man (PC, 2000) | 136 | 🟢 | C |
| [resident-evil-pc-decomp](https://github.com/ecruells/resident-evil-pc-decomp) | Decompilation of the Resident Evil 1 PC port | 132 | 🟢 | C++ |
| [devilution](https://github.com/galaxyhaxz/devilution) | Original Devilution reverse engineered Diablo source | 129 | 🔴 | C |
| [PlantsVsZombies-decompilation](https://github.com/ruslan831/PlantsVsZombies-decompilation) | Decompilation of Plants vs. Zombies 0.9.9 | 117 | 🟢 | C |
| [Grand Theft Auto 2 (gta2_re)](https://github.com/CriminalRETeam/gta2_re) | Reimplementation of Grand Theft Auto 2 v10.5 from the PC version (PC, 1999) | 115 | 🟢 | C++ |
| [nfsu2-re](https://github.com/yugecin/nfsu2-re) | Reverse engineering project for Need for Speed Underground 2 | 113 | 🟡 | C |
| [th08](https://github.com/N0zoM1z0/th08) | Source reconstruction of Touhou 8 Imperishable Night | 111 | 🟢 | C++ |
| [RBXGSdecomp](https://github.com/RBLXDecomp/RBXGSdecomp) | Decompilation of the November 2007 Roblox client | 103 | 🟢 | C++ |
| [msgi](https://github.com/MrSapps/msgi) | Metal Gear Solid Integral PC reverse engineering | 95 | 🗄️ | C++ |
| [Black & White](https://github.com/openblack/bw1-decomp) | Matching decompilation of Black & White (PC, 2001) | 92 | 🟢 | C++ |
| [racers](https://github.com/isledecomp/racers) | Decompilation of LEGO Racers (1999) | 92 | 🟢 | C++ |
| [dangerous-dave-re](https://github.com/gmegidish/dangerous-dave-re) | Reverse engineering of Dangerous Dave in the Haunted Mansion | 90 | 🔴 | Python |
| [iwd2-re](https://github.com/alexbatalov/iwd2-re) | Reverse engineered source of Icewind Dale 2 | 87 | 🟡 | C++ |
| [OpenLRR](https://github.com/trigger-segfault/OpenLRR) | Open source reimplementation of LEGO Rock Raiders | 87 | 🟡 | C++ |
| [chocolatekeen](https://github.com/jamesfmackenzie/chocolatekeen) | Reverse engineered Commander Keen in C/C++ and SDL | 83 | 🟢 | C |
| [gdp](https://github.com/camila314/gdp) | Decompilations of Geometry Dash physics functions | 72 | 🟡 | C++ |
| [ReHitman](https://github.com/ReGlacier/ReHitman) | Hitman Codename 47 reverse engineering project | 72 | 🟢 | C++ |
| [TR2X](https://github.com/LostArtefacts/TR2X) | Decompilation project for Tomb Raider II (1997) | 72 | 🗄️ | C |
| [SkiFree](https://github.com/yuv422/skifree_decomp) | Matching decompilation of SkiFree (PC, 1991) | 70 | 🔴 | Assembly |
| [Star Wars Episode I: Racer](https://github.com/tim-tim707/SW_RACER_RE) | Matching decompilation of Star Wars Episode I: Racer (PC, 1999) | 70 | 🟢 | C |
| [saga](https://github.com/opensagadev/saga) | Matching decompilation of LEGO Star Wars: The Complete Saga | 63 | 🟢 | C++ |
| [half-life1_win32_722](https://github.com/ScriptedSnark/half-life1_win32_722) | Reverse-engineered source of Half-Life 1 Net Test 1 (build 722) | 59 | 🟢 | C |
| [Buckshot Roulette](https://github.com/uncreativeCultist/buckshot-decomp-public) | Decompilation of Buckshot Roulette (PC, 2023) | 51 | 🟡 | GDScript |
| [Space Rangers HD: A War Apart](https://github.com/pakompom/SpaceRangersHD_decomp) | Matching decompilation of Space Rangers HD: A War Apart (PC, 2013) | 48 | 🟢 | Pascal |
| [Battlefield 2](https://github.com/kiwidoggie/breadflowerdos) | Matching decompilation of Battlefield 2 and Battlefield 2142 (PC, 2005) | 44 | 🟢 | C++ |
| [FlatOut 2](https://github.com/ZackWilde27/FlatOut-2-decomp) | Decompilation of FlatOut 2 (PC, 2006) | 43 | 🟢 | C |
| [nolfsrc](https://github.com/nolffan/nolfsrc) | Decompiled source code of No One Lives Forever | 41 | 🟢 | C++ |
| [Colin McRae Rally 2.0 (CMR2Decomp)](https://github.com/CMR2Decomp/CMR2Decomp) | Matching decompilation of Colin McRae Rally 2.0 (PC, 2000) | 40 | 🟢 | HTML |
| [ShortLine (reSL)](https://github.com/konovalov-aleks/reSL) | Reversed source code of ShortLine v1.1 (DOS) | 39 | 🟢 | C++ |
| [FUEL](https://github.com/widberg/FUELDecompilation) | Matching decompilation of FUEL (PC, 2009) | 27 | 🟢 | C++ |
| [Deltarune](https://github.com/TeamBlossomDevs/DeltaruneDecomp_beta) | Decompilation of Deltarune (PC, 2018) | 26 | 🟢 | Game Maker Language |
| [Tube](https://github.com/rep-stosw/tube64) | 64-bit port of the decompiled DOS game Tube (DOS, 1994) | 26 | 🟡 | C++ |
| [Tomb Raider: Legend (cdcEngine)](https://github.com/TheIndra55/cdcEngine) | Decompilation of Tomb Raider: Legend (PC, 2006) | 23 | 🟡 | C++ |
| [Oregon Trail II](https://github.com/katstasaph/otii) | Matching decompilation of Oregon Trail II (PC, 1995) | 21 | 🟡 | C |
| [Plants vs. Zombies](https://github.com/bluisblu/pvz) | Matching decompilation of Plants vs. Zombies (PC, 2009) | 21 | 🟢 | C |
| [Touhou 08: Imperishable Night](https://github.com/GensokyoClub/th08) | Matching decompilation of Touhou 08: Imperishable Night (PC, 2004) | 21 | 🟢 | C++ |
| [Bugs Bunny: Lost in Time](https://github.com/quantumdude836/BugsDecomp) | Matching decompilation of Bugs Bunny: Lost in Time (PC, 1999) | 17 | 🟡 | C |
| [Bio Menace](https://github.com/lethal-guitar/BioMenaceDecomp) | Matching decompilation of Bio Menace (DOS, 1993) | 15 | 🟡 | C |
| [Real War](https://github.com/Francessco121/real-war-decomp) | Matching decompilation of Real War (PC, 2001) | 15 | 🟡 | Dart |
| [Colin McRae Rally 2.0](https://github.com/pablocpas/CMR2Decomp) | Matching decompilation of Colin McRae Rally 2.0 (PC, 2000) | 14 | 🟢 | C++ |
| [Alien vs. Predator 2](https://github.com/lemiur/AVP2-Reconstructed) | Matching decompilation of Alien vs. Predator 2 (PC, 2001) | 13 | 🟢 | C++ |
| [Bloons TD 5](https://github.com/NKHook/BTD5-Decomp) | Matching decompilation of Bloons TD 5 (PC, 2011) | 13 | 🟡 | C++ |
| [FlatOut: Ultimate Carnage](https://github.com/ZackWilde27/FlatOut-UC-Decomp) | Decompilation of FlatOut: Ultimate Carnage (PC, 2008) | 13 | 🟢 | C++ |
| [Space Rangers](https://github.com/pakompom/SpaceRangers1_decomp) | Matching decompilation of Space Rangers (PC, 2002) | 13 | 🟢 | Pascal |
| [Ys VI: The Ark of Napishtim](https://github.com/GrantBenR/YsViDecomp) | Ghidra decompilation of Ys VI: The Ark of Napishtim, Steam version (PC, 2003) | 12 | 🟡 |  |
| [LEGO Batman: The Videogame (mariopossamato)](https://github.com/mariopossamato/LEGO-Batman) | Matching decompilation of LEGO Batman: The Videogame (Mac OS X, 2008) | 11 | 🟡 |  |
| [Mafia: The City of Lost Heaven](https://github.com/Marvisak/mafia-re) | Matching decompilation of Mafia: The City of Lost Heaven (PC, 2002) | 11 | 🟢 | C++ |
| [Okami HD](https://github.com/Shintensu/OkamiHD-Decomp) | Decompilation of Okami HD (PC, 2017) | 11 | 🟡 | C++ |
| [Cuphead](https://github.com/jmxamongusmodder/cuphead-decomp) | Decompilation of Cuphead (PC, 2017) | 10 | 🟡 | GLSL |
| [Happy Wheels](https://github.com/Afterflash/HappyWheels) | Decompilation of Happy Wheels (Flash, 2010) | 10 | 🟡 | ActionScript |
| [Legoland](https://github.com/marijnvdwerf/legoland) | Matching decompilation of Legoland (PC, 1999) | 10 | 🟢 | C |
| [Undertale Yellow](https://github.com/burnedpopcorn/UnderTale-Yellow-Decompilation) | Decompilation of Undertale Yellow v1.2.1 (PC, 2023) | 10 | 🟡 | Game Maker Language |
| [Nocturne](https://github.com/NearlyTRex/NocturneDecomp) | Decompilation of Nocturne (PC, 1999) | 7 | 🟢 | Assembly |
| [Homeworld 2](https://github.com/HaydnTrigg/Homeworld2Classic) | Matching decompilation of Homeworld 2 (PC, 2003) | 6 | 🟢 | C++ |
| [LEGO Creator: Knights' Kingdom](https://github.com/DavidGrice/knightskingdom) | Matching decompilation of LEGO Creator: Knights' Kingdom (PC, 2000) | 6 | 🟢 | JavaScript |
| [Thief: Deadly Shadows](https://github.com/Veradictus/Thief3-Decomp) | Matching decompilation of Thief: Deadly Shadows (PC, 2004) | 6 | 🟢 | C++ |
| [Final Fantasy IV (3D Remake)](https://github.com/GlitchedDeveloper/Babil-Decompilation-Project) | Decompilation of Final Fantasy IV (3D Remake) Steam version (PC, 2014) | 5 | 🟡 | C++ |
| [Krush Kill 'N Destroy Xtreme](https://github.com/Wyrelade/KKND-Decomp) | Matching decompilation of Krush Kill 'N Destroy Xtreme (PC, 1997) | 5 | 🟢 | C |
| [Lemmings Paintball](https://github.com/vonhoff/lemball-decomp) | Matching decompilation of Lemmings Paintball (PC, 1996) | 5 | 🟢 | C++ |
| [Costume Quest](https://github.com/Costume-Quest-Modding/CostumeQuest-Decomp) | Matching decompilation of Costume Quest (PC, 2010) | 4 | 🟡 | C++ |
| [Magiczna Kula Papatki](https://github.com/regratka/mkp) | Matching decompilation of Magiczna Kula Papatki (PC) | 4 | 🟢 | C++ |
| [Snail Mail](https://github.com/banteg/snail) | Matching decompilation of Snail Mail (PC) | 4 | 🟢 | C |
| [Sonic Generations](https://github.com/Luigi587/GenerationsDecomp) | Matching decompilation of Sonic Generations (PC, 2011) | 4 | 🟢 |  |
| [Stronghold (1993)](https://github.com/NancySadkov/dest) | Matching decompilation of AD&D Stronghold (DOS, 1993) | 4 | 🟡 | C |
| [The Italian Job](https://github.com/dashr9230/Caper) | Non-matching decompilation of The Italian Job (PC, 2001) | 4 | 🟢 | C |
| [Blasterball Revolution 2](https://github.com/KoboDev/BBR2Decompile) | Decompilation of Blasterball Revolution 2 (PC) | 3 | 🟡 |  |
| [Harvest: Massive Encounter](https://github.com/banteg/harvest) | Matching decompilation of Harvest: Massive Encounter (PC, 2008) | 3 | 🟢 | C++ |
| [Sonic the Hedgehog 4: Episode I (Windows Phone)](https://github.com/fr3dsp/Sonic4Ep1-Decomp) | Decompilation of Sonic the Hedgehog 4: Episode I (Windows Phone) | 3 | 🟢 | C# |
| [Summoner](https://github.com/AARosson48/SummonerDecomp) | Matching decompilation of Summoner (PC, 2000) | 3 | 🟢 | C++ |
| [DOMA Days](https://github.com/iestyn129/DOMADays) | Decompilation of the Ren'Py game DOMA Days by Big Blue Bubble (PC) | 2 | 🟢 | Ren'Py |
| [Ford Racing](https://github.com/dashr9230/Gt2) | Non-matching decompilation of Ford Racing (PC, 2000) | 2 | 🟢 | C |
| [Granny](https://github.com/scd5dev/GrannyDecompilationLegacy) | Decompilation of Granny PC v1.2.2 (PC) | 2 | 🗄️ | C# |
| [Jazz Jackrabbit 2](https://github.com/Mustafa1177/jazzjackrabbit2-decompiled) | Ghidra decompilation project of Jazz Jackrabbit 2: The Secret Files (PC, 1998) | 2 | 🟡 |  |
| [NavyField 2000](https://github.com/rbxrootx/MissionFleet) | Matching decompilation of NavyField 2000 (PC) | 2 | 🟢 | C++ |
| [Rumble Fighter](https://github.com/Primitheus/rumbledecomp) | Decompilation of Rumble Fighter (PC, 2006) | 2 | 🟡 | C++ |
| [The Oregon Trail (Windows 95)](https://github.com/emoluvjd2/oregontrail-win32-decomp) | Decompilation of The Oregon Trail (Windows 95) | 2 | 🟢 | C++ |
| [Creatures 2](https://github.com/adamcolquhoun/Creatures-2-Decompilation) | Matching decompilation of Creatures 2 (PC, 1998) | 1 | 🟢 |  |
| [Harry Potter and the Half-Blood Prince](https://github.com/MidacoYT/HarryPotterAndTheHalfBloodPrince-Decompilation) | Matching decompilation of Harry Potter and the Half-Blood Prince (PC, 2009) | 1 | 🟢 | C |
| [Hazard](https://github.com/EuclidVsGauss/HazardRevenge) | Matching decompilation of Hazard (PC) | 1 | 🟢 | C++ |
| [On The Run 2](https://github.com/caramelcupcakes842/On-The-Run-2-Decomp) | Decompilation of Miniclip's On The Run 2 (Adobe Shockwave, PC) | 1 | 🟡 |  |
| [On The Run: The Getaway](https://github.com/caramelcupcakes842/On-The-Run-The-Getaway) | Decompilation of Miniclip's On The Run: The Getaway (Adobe Shockwave, PC) | 1 | 🟡 |  |
| [The Journeyman Project Turbo!](https://github.com/disinvite/jman-decomp) | Matching decompilation of The Journeyman Project Turbo! (PC, 1994) | 1 | 🟢 | C++ |
| [Age of Speed 2](https://github.com/Llamaware/age-of-speed2) | Decompilation of the Shockwave racing game Age of Speed 2 (Macromedia Director, PC) | 0 | 🟡 | Python |
| [Dr. Brain Action Reaction](https://github.com/SirHenricus/DrBrainActionReaction_PackageDecomp) | Decompiled assets and UnrealScript from Dr. Brain Action Reaction (PC, 1999) | 0 | 🟡 | UnrealScript |
| [Johnny Herbert's Grand Prix Championship 1998](https://github.com/danvratil/jhgpc98decomp) | Matching decompilation of Johnny Herbert's Grand Prix Championship 1998 (PC, 1998) | 0 | 🟡 | C++ |
| [LEGO Batman: The Videogame](https://github.com/wasdhjklxyz/lbtvg) | Matching decompilation of LEGO Batman: The Videogame (PC, 2008) | 0 | 🟢 | C++ |
| [On The Run Vegas](https://github.com/caramelcupcakes842/On-The-Run-Vegas-Decomp) | Decompilation of Miniclip's On The Run Vegas (Adobe Shockwave, PC) | 0 | 🟡 |  |
| [Sonic & Knuckles Collection (1997)](https://git.sr.ht/~benoitren/skccport) | Matching decompilation of Sonic & Knuckles Collection (PC, 1997) |  | ⚪ |  |
| [Sonic CD (PC / Gems Collection)](https://git.sr.ht/~benoitren/soniccddecompilation) | Decompilation of Sonic CD (PC / Gems Collection) |  | ⚪ |  |
| [TwinBee Paradise in Donburi Shima](https://github.com/Jhuyghue/donburi-decomp) | Decompilation of TwinBee Paradise in Donburi Shima (Windows 95) | 0 | 🟡 | HTML |

## Matching Decompilations — PSP / Vita / PS3

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Monster Hunter Portable 2nd G](https://github.com/tclamb/mhp2g-decomp) | Matching decompilation of Monster Hunter Portable 2nd G (PSP, 2008) | 30 | 🟢 | C++ |
| [Bakugan: Defenders of the Core](https://github.com/Vawlpe/BakuganDotC-decomp) | Decompilation of Bakugan: Defenders of the Core (PSP, 2010) | 10 | 🟡 | C |

## Matching Decompilations — PlayStation 1

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Castlevania: Symphony of the Night](https://github.com/Xeeynamo/sotn-decomp) | Matching decompilation of Castlevania: Symphony of the Night (PlayStation, 1997) | 1,137 | 🟢 | C |
| [Silent Hill](https://github.com/shdecompilations/silent-hill-decomp) | Matching decompilation of Silent Hill (PlayStation, 1999) | 899 | 🟢 | C |
| [Metal Gear Solid](https://github.com/FoxdieTeam/mgs_reversing) | Reimplementation of Metal Gear Solid (PlayStation, 1998) | 804 | 🟢 | C |
| [Crash Team Racing (CTR-ModSDK)](https://github.com/CTR-tools/CTR-ModSDK) | Mod SDK and decompilation of Crash Team Racing (PlayStation, 1999) | 451 | 🟢 | C |
| [Spyro the Dragon](https://github.com/TheMobyCollective/spyro-1) | Matching decompilation of Spyro the Dragon (PlayStation, 1998) | 175 | 🟢 | C |
| [Final Fantasy VII](https://github.com/Xeeynamo/ff7-decomp) | Matching decompilation of Final Fantasy VII (PlayStation, 1997) | 168 | 🟢 | C |
| [Vagrant Story](https://github.com/ser-pounce/rood-reverse) | Matching decompilation of Vagrant Story (PlayStation, 2000) | 166 | 🟢 | C |
| [PSX Doom (PSXDOOM-RE)](https://github.com/Erick194/PSXDOOM-RE) | Decompilation of PSX Doom (PSXDOOM-RE) | 161 | 🟡 | C |
| [Xenogears](https://github.com/ladysilverberg/xenogears-decomp) | Matching decompilation of Xenogears (PlayStation, 1998) | 121 | 🟢 | C |
| [Serial Experiments Lain](https://github.com/Y0oshi/lain-psx-decompiled) | Decompilation of Serial Experiments Lain | 119 | 🟢 | C |
| [Crash Bandicoot 2: Cortex Strikes Back](https://github.com/ughman/c2c) | Matching decompilation of Crash Bandicoot 2: Cortex Strikes Back (PlayStation, 1997) | 94 | 🔴 | C |
| [mml1](https://github.com/ChrisNonyminus/mml1) | Decompilation of Mega Man Legends for PlayStation | 85 | 🔴 | C |
| [Legacy of Kain: Soul Reaver](https://github.com/fmil95/soul-re) | Matching decompilation of Legacy of Kain: Soul Reaver (PlayStation, 1999) | 82 | 🟢 | C |
| [Digimon World](https://github.com/jype0/dw_decomp) | Matching decompilation of Digimon World (PlayStation, 1999) | 75 | 🟢 | C |
| [Chrono Cross](https://github.com/jdperos/chrono-cross-decomp) | Matching decompilation of Chrono Cross (PlayStation, 1999) | 72 | 🟢 | C |
| [MediEvil](https://github.com/MediEvilDecompilation/medievil-decomp) | Matching decompilation of MediEvil (PlayStation, 1998) | 70 | 🟢 | C |
| [Brave Fencer Musashi](https://github.com/Druthulu/BFM-decomp) | Matching decompilation of Brave Fencer Musashi (PlayStation, 1998) | 60 | 🟢 | C |
| [Parasite Eve II](https://github.com/GabeRealB/parasite-eve-2-decomp) | Matching decompilation of Parasite Eve II (PlayStation, 1999) | 60 | 🟢 | C |
| [Frogger (1997)](https://github.com/HighwayFrogs/frogger-psx) | Decompilation of Frogger (1997) | 59 | 🟡 | C |
| [Parasite Eve](https://github.com/khasinski/parasite-eve-decomp) | Matching decompilation of Parasite Eve (PlayStation, 1998) | 59 | 🟢 | C |
| [Final Fantasy VIII](https://github.com/roengstrom/ff8-decomp) | Matching decompilation of Final Fantasy VIII (PlayStation, 1999) | 54 | 🟢 | C |
| [Need for Speed: High Stakes](https://github.com/Caesar0007/NFSHS-PSX-decomp) | Decompilation of Need for Speed: High Stakes | 46 | 🟢 | Assembly |
| [Digimon World 3 (ddw3)](https://github.com/markisha64/ddw3) | Matching decompilation of Digimon World 3 (PlayStation, 2002) | 43 | 🟢 | Assembly |
| [ffvii](https://github.com/Drahsid/ffvii) | In-progress matching decompilation of Final Fantasy VII (PSX) | 43 | 🗄️ | C |
| [Croc: Legend of the Gobbos](https://github.com/Xeeynamo/croc) | Matching decompilation of Croc: Legend of the Gobbos (PlayStation, 1997) | 38 | 🟡 | C |
| [Legend of Mana](https://github.com/celophi/lom-decomp) | Matching decompilation of Legend of Mana (PlayStation, 1999) | 37 | 🟢 | C |
| [Mega Man X4](https://github.com/sozud/mmx4) | Matching decompilation of Mega Man X4 (PlayStation, 1997) | 34 | 🟢 | C |
| [Brightis-fan-translation](https://github.com/Dickdebonair/Brightis-fan-translation) | Decompilation and fan translation of the PSX game Brightis | 33 | 🟢 | Assembly |
| [Vandal Hearts](https://github.com/shao113/vh) | Matching decompilation of Vandal Hearts (PlayStation, 1996) | 31 | 🟡 | C |
| [PS1 Psy-Q SDK Libraries](https://github.com/sozud/psy-q-decomp) | Decompilation of PS1 Psy-Q SDK Libraries | 29 | 🟢 | C |
| [Rage Racer](https://github.com/khasinski/rage-racer-decomp) | Matching decompilation of Rage Racer (PlayStation, 1996) | 29 | 🟢 | C |
| [Tomba!](https://github.com/hansbonini/psx_tomba) | Decompilation of Tomba! | 28 | 🟢 | C |
| [Twisted Metal](https://github.com/abelbriggs1/tm1_decomp) | Matching decompilation of Twisted Metal (PlayStation, 1995) | 22 | 🟢 | C |
| [Jumping Flash!](https://github.com/NotExactlySiev/aloha) | Matching decompilation of Jumping Flash! (PlayStation, 1995) | 21 | 🟢 | Assembly |
| [LSD: Dream Emulator](https://github.com/brian-oblivion/lsddecomp) | Matching decompilation of LSD: Dream Emulator (PlayStation, 1998) | 15 | 🟢 | C |
| [Lunar 2: Eternal Blue Complete](https://github.com/Zackmon/lunar2-psx-decomp) | Decompilation of Lunar 2: Eternal Blue Complete | 15 | 🔴 | C |
| [Digimon World 2](https://github.com/Wyrelade/Digimon-World-2-Decomp) | Matching decompilation of Digimon World 2 (PlayStation, 2000) | 14 | 🟢 | C |
| [dw2003recomp](https://github.com/gascarcella/dw2003recomp) | Decompilation of Digimon World 2003 (PS1, EU) with reference tests; PC port in progress | 14 | 🟢 | C |
| [LSD: Dream Emulator (FirecatFG)](https://github.com/FirecatFG/lsddecomp) | Matching decompilation of LSD: Dream Emulator (PlayStation, 1998) | 14 | 🟡 | C |
| [Evo's Space Adventures](https://github.com/mkst/esa) | Matching decompilation of Evo's Space Adventures (PlayStation, 1999) | 13 | 🟢 | C |
| [Digimon World (solidheron)](https://github.com/solidheron/Digimon_World_1_decompolation) | Matching decompilation of Digimon World (PlayStation, 1999) | 11 | 🟡 | C |
| [Megami Ibunroku Persona](https://github.com/daanhenke/persona-psx) | Decompilation of Megami Ibunroku Persona | 11 | 🟢 | C |
| [Digimon World 3 (2003)](https://github.com/ReGame-Labs/dw3_decomp) | Matching decompilation of Digimon World 3 (PlayStation, 2002) | 8 | 🟢 | C |
| [Azure Dreams](https://github.com/forestbelton/azure) | Matching decompilation of Azure Dreams (PlayStation, 1997) | 7 | 🟡 | Python |
| [WCW/nWo Thunder](https://github.com/martinbean/thunder) | Matching decompilation of WCW/nWo Thunder (PlayStation, 1999) | 7 | 🟡 | Makefile |
| [Aironauts](https://github.com/bismurphy/Aironauts-decomp) | Matching decompilation of Aironauts (PlayStation, 1999) | 6 | 🟡 | C |
| [Pop'n Music](https://github.com/Erizur/slpm86183) | Matching decompilation of Pop'n Music (PlayStation, 1999) | 6 | 🟢 | C |
| [Tony Hawk's Pro Skater 2 (Competition Demo)](https://github.com/emoluvjd2/thps2-demo-decomp) | Matching decompilation of Tony Hawk's Pro Skater 2 (PlayStation, 2000; competition demo) | 5 | 🟢 | C++ |
| [Armored Core](https://github.com/Wyrelade/Armored-Core-Decomp) | Matching decompilation of Armored Core (PlayStation, 1997) | 4 | 🟢 | C |
| [Wild 9](https://github.com/plinkr/Wild9-Decompilation) | Matching decompilation of Wild 9 (PlayStation, 1998) | 4 | 🟢 | C |
| [Digimon: Digital Card Battle](https://github.com/ReGame-Labs/dcb_decomp) | Matching decompilation of Digimon: Digital Card Battle (PlayStation, 2000) | 3 | 🟢 | C |
| [WCW Nitro](https://github.com/martinbean/nitro) | Matching decompilation of WCW Nitro (PlayStation, 1998) | 3 | 🟢 | C |
| [Bubsy 3D: Furbitten Planet](https://github.com/EiscremeWaffle/bubsy3d-decomp) | Matching decompilation of Bubsy 3D: Furbitten Planet (PlayStation, 1996) | 2 | 🟢 | C |
| [Digimon Rumble Arena](https://github.com/ReGame-Labs/dtbe_decomp) | Matching decompilation of Digimon Rumble Arena (PlayStation, 2001) | 2 | 🟢 | C |
| [Kaze no Notam](https://github.com/aaaaaaaaaaway/kaze-no-notam-decomp) | Matching decompilation of Kaze no Notam (PlayStation, 2001) | 1 | 🟢 | C |
| [Tokimeki Memorial: Forever with You](https://github.com/CosmicScribe64/tokimemo-ps1-decomp) | Decompilation of Tokimeki Memorial: Forever with You | 1 | 🟢 | C |
| [Tokimeki Memorial: Forever With You (CelestialAmber)](https://github.com/CelestialAmber/tokimemo) | Matching decompilation of Tokimeki Memorial: Forever With You (PlayStation, 1995) | 1 | 🟡 | Python |
| [Dino Crisis 2](https://github.com/anzaldoivan/dino-crisis-2-decomp) | Matching decompilation of Dino Crisis 2 (PlayStation, 2000) | 0 | 🟢 | Python |
| [Mega Man X5](https://github.com/anzaldoivan/mmx5) | Matching decompilation of Mega Man X5 (PlayStation, 2000) | 0 | 🟢 | C |
| [Mega Man X6](https://github.com/anzaldoivan/mmx6) | Matching decompilation of Mega Man X6 (PlayStation, 2001) | 0 | 🟢 | C |
| [Shin Megami Tensei](https://codeberg.org/chickenzes/smt-decomp) | Matching decompilation of Shin Megami Tensei (PlayStation, 2001) |  | ⚪ |  |
| [Tombi!](https://github.com/afsenovilla/Tombi-Decomp) | Matching decompilation of Tombi! (PlayStation, 1997) | 0 | 🟢 | C |

## Matching Decompilations — PlayStation 2

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Street Fighter III: 3rd Strike](https://github.com/crowded-street/3s-decomp) | Matching decompilation of Street Fighter III: 3rd Strike (PlayStation 2, 2004) | 279 | 🟢 | C |
| [Resident Evil – Code: Veronica X](https://github.com/AshfordFamily/recvx-decomp) | Matching decompilation of Resident Evil – Code: Veronica X (PlayStation 2, 2001) | 273 | 🟢 | C |
| [Sly Cooper and the Thievius Raccoonus](https://github.com/TheOnlyZac/sly1) | Matching decompilation of Sly Cooper and the Thievius Raccoonus (PlayStation 2, 2002) | 273 | 🟢 | C++ |
| [PaRappa the Rapper 2](https://github.com/parappadev/parappa2) | Matching decompilation of PaRappa the Rapper 2 (PlayStation 2, 2001) | 202 | 🟢 | C |
| [Silent Hill 3](https://github.com/dreamingmoths/memory-of-alessa) | Matching decompilation of Silent Hill 3 (PlayStation 2, 2003) | 141 | 🟢 | C |
| [Fatal Frame](https://github.com/Mikompilation/Himuro) | Matching decompilation of Fatal Frame (PlayStation 2, 2001) | 127 | 🟢 | C |
| [Shadow of the Colossus](https://github.com/Fantaskink/SOTC) | Matching decompilation of Shadow of the Colossus (PlayStation 2, 2005; preview build) | 118 | 🟢 | C |
| [Kingdom Hearts](https://github.com/ethteck/kh1) | Matching decompilation of Kingdom Hearts (PlayStation 2, 2002) | 104 | 🟢 | C |
| [Dark Cloud](https://github.com/TheMoonPeople/Chronicle) | Matching decompilation of Dark Cloud (PlayStation 2, 2000) | 87 | 🟢 | C++ |
| [Persona3-FES-Decompilation](https://github.com/snaku/Persona3-FES-Decompilation) | Decompilation of Shin Megami Tensei: Persona 3 FES | 64 | 🟢 | C |
| [God Hand](https://github.com/LucasPicoli/god-hand-decomp) | Matching decompilation of God Hand (PlayStation 2, 2006) | 52 | 🟢 | C |
| [Klonoa 2: Lunatea's Veil](https://github.com/entriphy/kl2_lv_decomp) | Matching decompilation of Klonoa 2: Lunatea's Veil (PlayStation 2, 2001) | 44 | 🟡 | C |
| [Ratchet & Clank (PAL)](https://github.com/OpenRAC/rac1-decomp) | Matching decompilation of Ratchet & Clank (PlayStation 2, 2002; PAL version) | 42 | 🟢 | C |
| [Monster Hunter (JP)](https://github.com/2Tie/mh1j) | Matching decompilation of Monster Hunter (PlayStation 2, 2004; Japanese version) | 41 | 🟢 | C |
| [ico](https://github.com/nathanialf/ico) | Decompilation of ICO (PS2) | 36 | 🟢 | C |
| [Ratchet & Clank (USA)](https://github.com/lombyte-project/Lombyte) | Matching decompilation of Ratchet & Clank (PlayStation 2, 2002; USA version) | 36 | 🟢 | C |
| [Shin Megami Tensei: Persona 4](https://github.com/Raikaru/Persona4-Decompilation) | Matching decompilation of Shin Megami Tensei: Persona 4 (PlayStation 2, 2008) | 36 | 🟢 | C |
| [Ico](https://github.com/RossyDoubleUnderscore/ICO-decomp) | Matching decompilation of Ico (PlayStation 2, 2001) | 32 | 🟢 | C |
| [Yakuza](https://github.com/Hamzaxx370/Ogre-Decomp) | Matching decompilation of Yakuza (PlayStation 2, 2005) | 30 | 🟢 | C++ |
| [SSX 3](https://github.com/ssxdecomp/ssx3) | Matching decompilation of SSX 3 (PlayStation 2, 2003) | 29 | 🟢 | Python |
| [Dark Cloud 2](https://github.com/TheMoonPeople/ChronicleTwo) | Matching decompilation of Dark Cloud 2 (PlayStation 2, 2002) | 26 | 🟢 | C++ |
| [Ratchet & Clank: Up Your Arsenal](https://github.com/OpenRAC/rac3-uya-decomp) | Matching decompilation of Ratchet & Clank: Up Your Arsenal (PlayStation 2, 2004) | 24 | 🟢 | C |
| [Shin Megami Tensei: Digital Devil Saga](https://github.com/Megami-Decomps/dds-decomp) | Matching decompilation of Shin Megami Tensei: Digital Devil Saga (PlayStation 2, 2004) | 24 | 🟢 | C |
| [Gran Turismo 4](https://github.com/gustavocanepa/gt4-decomp) | Matching decompilation of Gran Turismo 4 (PlayStation 2, 2004) | 23 | 🟢 | C |
| [REOF2](https://github.com/caprado/REOF2) | Resident Evil Outbreak File #2 (PS2) decompilation and preservation project | 21 | 🟢 | C |
| [BT3-Decompiled](https://github.com/z3xox/BT3-Decompiled) | Matching decompilation of Dragon Ball Z: Budokai Tenkaichi 3 (PS2) | 20 | 🟢 | C |
| [Twisted Metal: Black](https://github.com/abelbriggs1/tmb_decomp) | Matching decompilation of Twisted Metal: Black (PlayStation 2, 2001) | 18 | 🟢 | C |
| [Twisted Metal: Harbor City](https://github.com/jacobleeharris/tmhc) | Matching decompilation of Twisted Metal: Harbor City (PlayStation 2, unreleased) | 17 | 🟢 | C |
| [Xenosaga Episode I (squareman)](https://github.com/SquareMan/xenosaga) | Matching decompilation of Xenosaga Episode I (PlayStation 2, 2002) | 17 | 🟡 | C |
| [Resident Evil: Dead Aim](https://github.com/cakehonolulu/Bullseye) | Matching decompilation of Resident Evil: Dead Aim (PlayStation 2, 2003) | 16 | 🟢 | C++ |
| [SSX](https://github.com/ssxdecomp/ssx) | Matching decompilation of SSX (PlayStation 2, 2000) | 16 | 🟢 | Python |
| [Crash Bandicoot: The Wrath of Cortex (crash-ps2)](https://github.com/calmsacibis995/crash-ps2) | Decompilation of Crash Bandicoot: The Wrath of Cortex (crash-ps2) | 14 | 🟡 | C |
| [Kuon](https://github.com/weirdbeardgame/Mulberry) | Matching decompilation of Kuon (PlayStation 2, 2004) | 14 | 🟢 | C |
| [Silent Hill 2](https://github.com/dreamingmoths/mirror-of-alessa) | Matching decompilation of Silent Hill 2 (PlayStation 2, 2001) | 14 | 🟢 |  |
| [Dog's Life](https://github.com/IWILLCRAFT-M0d/dogcomp) | Matching decompilation of Dog's Life (PlayStation 2, 2003) | 13 | 🟢 | C++ |
| [Crash Bandicoot: The Wrath of Cortex (PS2)](https://github.com/denzi-gh/crashwoc-decomp-ps2) | Decompilation of Crash Bandicoot: The Wrath of Cortex (PS2) | 12 | 🟢 | C |
| [Marvel vs. Capcom 2 (PS2)](https://github.com/g-guthrie/mvc2-ps2-decomp) | Decompilation of Marvel vs. Capcom 2 (PS2) | 11 | 🟢 | C |
| [Ratchet & Clank PS2 quadrilogy (Pyrocitor)](https://github.com/VELD-Dev/Pyrocitor) | Decompilation of Ratchet & Clank PS2 quadrilogy (Pyrocitor) | 11 | 🗄️ | C++ |
| [Ratchet: Deadlocked](https://github.com/OpenRAC/rac-deadlocked-decomp) | Matching decompilation of Ratchet: Deadlocked (PlayStation 2, 2005) | 11 | 🟢 | C |
| [Star Ocean: Till the End of Time](https://github.com/celophi/so3-decomp) | Matching decompilation of Star Ocean: Till the End of Time (PlayStation 2, 2003) | 11 | 🟢 | C++ |
| [Guilty Gear X Plus](https://github.com/WistfulHopes/ggx) | Matching decompilation of Guilty Gear X Plus (PlayStation 2, 2001; Korean version) | 10 | 🟡 | Python |
| [Xenosaga Episode I](https://github.com/OpokXeno/xsg-i-decomp) | Matching decompilation of Xenosaga Episode I (PlayStation 2, 2002) | 10 | 🟢 | Java |
| [SSX Tricky](https://github.com/ssxdecomp/ssxtricky) | Matching decompilation of SSX Tricky (PlayStation 2, 2001) | 9 | 🟢 | Python |
| [Sonic Riders: Zero Gravity (PS2 prototype)](https://github.com/KidWizardOfTheWeb/SR2) | Decompilation of Sonic Riders: Zero Gravity (PS2 prototype) | 7 | 🟢 | C++ |
| [Shaun Palmer's Pro Snowboarder](https://github.com/Daniel-McCarthy/SPPS) | Matching decompilation of Shaun Palmer's Pro Snowboarder (PlayStation 2, 2001) | 6 | 🟢 | C |
| [Phantasy Star II Disassembly](https://github.com/jon13doe/SEGA_ps2_disasm) | Phantasy Star II Disassembly | 5 | 🔴 | Assembly |
| [Amplitude](https://github.com/ieee802dot11ac/amp) | Matching decompilation of Amplitude (PlayStation 2, 2003) | 4 | 🟡 | Python |
| [Syphon Filter: The Omega Strain](https://github.com/zm2283145/syphon-filter-omega-strain-decomp) | Matching decompilation of Syphon Filter: The Omega Strain (PlayStation 2, 2004) | 3 | 🟢 | C |
| [Treasure Planet](https://github.com/Colt-Zero/Thousand-Worlds) | Asset and level editor for Disney's Treasure Planet (PlayStation 2, 2002) | 3 | 🟡 | Python |
| [Drakan: The Ancients' Gates](https://github.com/cScarletter/Drakan-The-Ancient-Gates-Decompilation-) | Matching decompilation of Drakan: The Ancients' Gates (PlayStation 2, 2002) | 2 | 🟡 |  |
| [Ar tonelico II: Melody of Metafalica](https://github.com/USED255/artonelico2-decomp) | Matching decompilation of Ar tonelico II: Melody of Metafalica (PlayStation 2, 2007) | 1 | 🟢 | C |
| [Are You Smarter Than a 5th Grader: Make the Grade](https://github.com/Gmon20/makethedecomp) | Matching decompilation of Are You Smarter Than a 5th Grader: Make the Grade (PlayStation 2, 2009) | 1 | 🟡 | C |
| [Chulip](https://github.com/aaaaaaaaaaway/chulip-decomp) | Matching decompilation of Chulip (PlayStation 2, 2002) | 1 | 🟢 | C |
| [George of the Jungle and the Search for the Secret](https://github.com/2gifts/george-decomp) | Matching decompilation of George of the Jungle and the Search for the Secret (PlayStation 2, 2008) | 1 | 🟢 | C |
| [Stretch Panic](https://github.com/Harskov/stretch-panic-usa) | Matching decompilation of Stretch Panic (PlayStation 2, 2001) | 1 | 🟢 | C |
| [Tourist Trophy](https://github.com/gustavocanepa/tt-decomp) | Matching decompilation of Tourist Trophy (PlayStation 2, 2006) | 1 | 🟢 | C |
| [PS2 OSDSYS (system menu)](https://github.com/JeanxPereira/CrystalOSD) | Decompilation of PS2 OSDSYS (system menu) | 0 | 🟢 | JavaScript |
| [Shadow Hearts](https://git.sr.ht/~benoitren/shadowheartsdecompilation) | Matching decompilation of Shadow Hearts (PlayStation 2, 2001) |  | ⚪ |  |

## Matching Decompilations — SNES / NES

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Battle City (NES disassembly)](https://github.com/cyneprepou4uk/NES-Games-Disassembly) | Disassembly / decompilation of Battle City (NES disassembly) | 292 | 🟢 | Assembly |
| [Contra (NES)](https://github.com/vermiceli/nes-contra-us) | Decompilation of Contra (NES) | 231 | 🟢 | Assembly |
| [EarthBound](https://github.com/Herringway/ebsrc) | Source code recreation of EarthBound (SNES, 1994) | 183 | 🟢 | Assembly |
| [Super Mario World 2: Yoshi's Island (SNES) Disassembly](https://github.com/brunovalads/yoshisisland-disassembly) | Full disassembly of Yoshi's Island (SNES) version U 1.0 | 161 | 🟢 | Assembly |
| [supermetroid](https://github.com/strager/supermetroid) | Super Metroid SNES disassembly | 160 | 🔴 | Assembly |
| [superbomberman](https://github.com/LIJI32/superbomberman) | Disassembly and remade build system for SNES game Super Bomberman | 109 | 🟢 | Assembly |
| [TetrisNESDisasm](https://github.com/CelestialAmber/TetrisNESDisasm) | Disassembly of Tetris (NES) | 108 | 🟡 | Assembly |
| [smb2](https://github.com/Xkeeper0/smb2) | Super Mario Bros. 2 (NES) disassembly | 102 | 🔴 | Assembly |
| [dragon-warrior-disassembly](https://github.com/nmikstas/dragon-warrior-disassembly) | NES Dragon Warrior software disassembly | 88 | 🔴 | Assembly |
| [Donkey Kong Country 2](https://github.com/p4plus2/DKC2-disassembly) | Disassembly of Donkey Kong Country 2 (SNES, 1995) | 76 | 🟡 | Assembly |
| [Tecmo_Super_Bowl_NES_Disassembly](https://github.com/bruddog/Tecmo_Super_Bowl_NES_Disassembly) | Rebuildable 6502 disassembly of Tecmo Super Bowl (NES) | 62 | 🟡 | Assembly |
| [Mega Man 3 (NES) Disassembly](https://github.com/refreshing-lemonade/megaman3-disassembly) | Full disassembly of Mega Man 3 (NES) | 52 | 🔴 | Assembly |
| [mike-tysons-punch-out-disassembly](https://github.com/nmikstas/mike-tysons-punch-out-disassembly) | Reverse engineering effort of the NES game Mike Tyson's Punch-Out. | 46 | 🔴 | Assembly |
| [Balloon Fight](https://github.com/LuigiBlood/balloonfight_dis) | Disassembly of Balloon Fight (NES, 1984) | 43 | 🔴 | Assembly |
| [Mega Man 5 (NES) Disassembly](https://github.com/refreshing-lemonade/megaman5-disassembly) | Full disassembly of Mega Man 5 (NES) | 34 | 🟡 | Assembly |
| [Donkey Kong Country](https://github.com/Yoshifanatic1/Donkey-Kong-Country-1-Disassembly) | Disassembly of Donkey Kong Country (SNES, 1994) | 30 | 🔴 | Assembly |
| [Donkey Kong (NES)](https://github.com/RussianManSMWC/Donkey-Kong-NES-Disassembly) | Disassembly / decompilation of Donkey Kong (NES) | 29 | 🟡 | Assembly |
| [Mega Man 4 (NES) Disassembly](https://github.com/refreshing-lemonade/megaman4-disassembly) | Full disassembly of Mega Man 4 (NES) | 29 | 🔴 | Assembly |
| [Super C / Probotector (NES)](https://github.com/vermiceli/nes-super-c) | Decompilation of Super C / Probotector (NES) | 26 | 🟢 | Assembly |
| [ff3](https://github.com/everything8215/ff3) | Disassembly and ROM info for Final Fantasy III (NES) | 24 | 🔴 | Assembly |
| [Dr. Mario (NES)](https://github.com/Nostaljipi/dr-mario-disassembly) | Disassembly / decompilation of Dr. Mario (NES) | 22 | 🔴 | Assembly |
| [ff2](https://github.com/everything8215/ff2) | Disassembly and ROM Info for Final Fantasy II (NES) | 22 | 🔴 | Assembly |
| [Donkey Kong Country 3](https://github.com/Yoshifanatic1/Donkey-Kong-Country-3-Disassembly) | Disassembly of Donkey Kong Country 3 (SNES, 1996) | 21 | 🔴 | Assembly |
| [Ghosts and Graves](https://github.com/AnthonyBongers/GhostsAndGraves) | Ghosts and Graves, a Tents and Trees demake written in 6502 assembly (NES homebrew) | 20 | 🟢 | Assembly |
| [Mega Man 6 (NES) Disassembly](https://github.com/refreshing-lemonade/megaman6-disassembly) | Full disassembly of Mega Man 6 (NES) | 20 | 🔴 | Assembly |
| [Donald Land](https://github.com/brunovalads/donald-land) | Disassembly of Donald Land (NES, 1988) | 16 | 🔴 | Assembly |
| [crystalisdisassembly](https://github.com/crystalisdisassembly/crystalisdisassembly) | Disassembly of the NES Game Crystalis | 14 | 🔴 | Assembly |
| [English Translation of Captain Tsubasa 2](https://github.com/cyneprepou4uk/Captain-Tsubasa-2-English-Translation) | Captain Tsubasa 2 [NES] disassembly | 12 | 🟢 | Assembly |
| [Battle City](https://github.com/vgrichina/battlecity) | Disassembly of Battle City (NES, 1985) | 10 | 🟢 | JavaScript |
| [EarthBound Beginnings](https://github.com/GrasonHumphrey/Earthbound-Zero-Decomp) | Ghidra decompilation of EarthBound Beginnings / Mother (NES, 1989) | 7 | 🟡 | HTML |
| [Ultima 3 Disassembly](https://github.com/nmikstas/nes_ultima_3_disassembly) | Disassembly of the nes version of Ultima Exodus | 7 | 🔴 | Assembly |
| [Ms. Pac-Man NES Tengen Disassembly](https://github.com/RussianManSMWC/Ms.-Pac-Man-NES-Tengen-Disassembly) | A disassembly of Ms. Pac-Man for NES, Tengen version. | 6 | 🟢 | Assembly |
| [SimCity (SNES) Disassembly](https://github.com/Yoshifanatic1/SimCity-SNES-Disassembly) | Disassembly of SimCity (Assembly) | 6 | 🔴 | Assembly |
| [Ms. Pac-Man (SNES) Disassembly](https://github.com/Yoshifanatic1/Ms-Pac-Man-SNES-Disassembly) | Disassembly of Ms. Pac-Man (Assembly) | 5 | 🔴 | Assembly |
| [Duck Hunt Disassembly](https://github.com/RussianManSMWC/Duck-ssembly-Hunt) | A disassembly of Duck Hunt for the NES. | 3 | 🟡 | Assembly |
| [Ms. Pac-Man NES Namco Disassembly](https://github.com/RussianManSMWC/Ms.-Pac-Man-NES-Namco-Disassembly) | A disassembly of Ms. Pac-Man for NES, Namco/Now Production version. | 3 | 🟡 | Assembly |
| [Spider-Man & the X-Men in Arcade's Revenge (SNES) Disassembly](https://github.com/Yoshifanatic1/Spider-Man-X-Men-Arcades-Revenge-SNES-Disassembly) | Disassembly of Spider-Man and the X-Men in Arcade's Revenge (Assembly) | 2 | 🔴 | Assembly |

## Matching Decompilations — Sega

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Neon Genesis Evangelion 64](https://github.com/farisawan-2000/evangelion) | Decompilation of Neon Genesis Evangelion 64 | 36 | 🟡 | C |
| [Resident Evil – Code: Veronica (Dreamcast)](https://github.com/fmil95/recv-dc-decomp) | Decompilation of Resident Evil – Code: Veronica (Dreamcast) | 36 | 🟢 | C |
| [Tokyo Bus Guide](https://github.com/lhsazevedo/tbg-decomp) | Matching decompilation of Tokyo Bus Guide (Dreamcast, 1999) | 34 | 🟢 | PHP |
| [Flicky-Disassembly](https://github.com/Dandaman955/Flicky-Disassembly) | Disassembly of Flicky on the Mega Drive. | 7 | 🔴 | Assembly |

## Matching Decompilations — Switch

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Breath of the Wild decomp](https://github.com/zeldaret/botw) | Decompilation of The Legend of Zelda: Breath of the Wild (Switch 1.5.0) | 2,209 | 🟢 | C++ |
| [Minecraft: Nintendo Switch Edition](https://github.com/GRAnimated/MinecraftLCE) | Decompilation of Minecraft: Nintendo Switch Edition | 617 | 🟢 | C++ |
| [Super Mario Odyssey](https://github.com/MonsterDruide1/OdysseyDecomp) | Matching decompilation of Super Mario Odyssey (Switch, 2017) | 452 | 🟢 | C++ |
| [sead](https://github.com/open-ead/sead) | Decompilation of sead, Nintendo's first-party C++ standard library | 251 | 🟢 | C++ |
| [LEGO City Undercover](https://github.com/Nintendocustom/Lego-City-Undercover-Decompilation) | Matching decompilation of LEGO City Undercover (Switch, 2017) | 28 | 🟢 | C++ |
| [cttt-decomp](https://github.com/shibbo/cttt-decomp) | Decompilation of Captain Toad: Treasure Tracker (Switch, v1.3.0) | 20 | 🔴 | C++ |
| [Super Mario 3D World + Bowser's Fury](https://github.com/shibbo/3DWDecomp) | Matching decompilation of Super Mario 3D World + Bowser's Fury (Switch, 2021) | 18 | 🟢 | C++ |
| [The Legend of Zelda: Link's Awakening (Switch)](https://github.com/Owen-Splat/las-decomp) | Decompilation of The Legend of Zelda: Link's Awakening (Switch) | 9 | 🟢 |  |
| [Pokémon Sword](https://github.com/charlieduzstuf/pokesword) | Matching decompilation of Pokémon Sword (Switch, 2019) | 4 | 🟢 | C |

## Matching Decompilations — Xbox

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Halo CE decomp](https://github.com/halo-re/halo) | Halo: Combat Evolved (Xbox) decompilation research project | 447 | 🔴 | C |
| [Halo: Combat Evolved (Xbox)](https://github.com/punpckhdq/halo) | Decompilation of Halo: Combat Evolved (Xbox) | 184 | 🟢 | C |
| [Undertale (Xbox One)](https://github.com/kittibyte/UndertaleDecomp) | Decompilation of Undertale (Xbox One) | 126 | 🟡 | Game Maker Language |
| [Minecraft: Xbox 360 Edition](https://github.com/LCERD/Minecraft-Xbox-360-Decompilation) | Decompilation of Minecraft: Xbox 360 Edition | 68 | 🟡 | C++ |
| [Halo: Reach](https://github.com/ChimpsAtSea/Reach) | Matching decompilation of Halo: Reach (Xbox 360, 2010) | 67 | 🟢 | C++ |
| [halo2-decompiled](https://github.com/kirklandsig/halo2-decompiled) | Matching decompilation of Halo 2 for the original Xbox | 63 | 🟢 | C++ |
| [Dance Central 3](https://github.com/rjkiv/dc3-decomp) | Matching decompilation of Dance Central 3 (Xbox 360, 2012) | 40 | 🟢 | C++ |
| [TerrariaXDK](https://github.com/dptug/TerrariaXDK) | Decompiled Terraria Xbox 360 Edition source code | 35 | 🟢 | C# |
| [halocea](https://github.com/surreptitiousresearch/halocea) | Decompiled source of Halo: Combat Evolved Anniversary (Xbox 360) | 33 | 🟢 | C |
| [Fallout: New Vegas](https://github.com/ieee802dot11ac/fnv) | Matching decompilation of Fallout: New Vegas (Xbox 360, 2010) | 32 | 🟢 | C++ |
| [Xbox 360 Kernel](https://github.com/AleBello7276/xkrnl-decomp) | Decompilation of Xbox 360 Kernel | 24 | 🟢 | Python |
| [Banjo-Kazooie (Xbox 360)](https://github.com/banjo360/bk360) | Decompilation of Banjo-Kazooie (Xbox 360) | 21 | 🟢 | C |
| [Sonic the Hedgehog (2006)](https://github.com/rjkiv/sonic06) | Matching decompilation of Sonic the Hedgehog (Xbox 360, 2006) | 14 | 🟢 | C |
| [Kinect Sports](https://github.com/SebaaMG/Kinect-Sports-Decomp) | Matching decompilation of Kinect Sports (Xbox 360, 2010) | 3 | 🟢 | C |
| [Jet Set Radio Future](https://codeberg.org/KeybadeBlox/JSRF-Decompilation) | Matching decompilation of Jet Set Radio Future (Xbox, 2002) |  | ⚪ |  |

## Mod Loaders & Script Extenders

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [BepInEx](https://github.com/BepInEx/BepInEx) | Plugin/modding framework for Unity Mono, IL2CPP and XNA games | 8,831 | 🟢 | C# |
| [Harmony](https://github.com/pardeike/Harmony) | Library for patching and decorating .NET/Mono methods at runtime, widely used for game mods | 6,683 | 🟢 | C# |
| [tModLoader](https://github.com/tModLoader/tModLoader) | Mod loader and API for Terraria | 5,722 | 🟢 | C# |
| [REFramework](https://github.com/praydog/REFramework) | Mod loader, scripting platform and VR support for Capcom RE Engine games | 5,627 | 🟢 | C++ |
| [Cyber Engine Tweaks](https://github.com/maximegmd/CyberEngineTweaks) | Cyberpunk 2077 scripting framework and fixes | 4,810 | 🟢 | C++ |
| [UEVR](https://github.com/praydog/UEVR) | Universal VR mod injector for Unreal Engine 4.8-5.x games | 4,611 | 🟢 | C++ |
| [FiveM / Cfx.re](https://github.com/citizenfx/fivem) | Multiplayer modification frameworks for GTA V (FiveM) and RDR2 (RedM) | 4,285 | 🟢 | C++ |
| [MelonLoader](https://github.com/LavaGang/MelonLoader) | Universal mod loader for Unity games (Il2Cpp and Mono) | 4,253 | 🟢 | C# |
| [cnc-ddraw](https://github.com/FunkyFr3sh/cnc-ddraw) | DirectDraw reimplementation fixing old games such as Command & Conquer on modern systems | 3,528 | 🟢 | C |
| [Widescreen Fixes Pack](https://github.com/ThirteenAG/WidescreenFixesPack) | Plugins adding or fixing widescreen support and bugs in many PC games | 3,236 | 🟢 | C++ |
| [UnityExplorer](https://github.com/sinai-dev/UnityExplorer) | In-game UI for exploring and modifying IL2CPP and Mono Unity games | 3,152 | 🗄️ | C# |
| [RE-UE4SS](https://github.com/UE4SS-RE/RE-UE4SS) | Injectable Lua scripting, SDK generator and live property editor for UE4/UE5 games | 3,002 | 🟢 | C++ |
| [TShock](https://github.com/Pryaxis/TShock) | Terraria server modification and plugin API | 2,898 | 🟢 | C# |
| [SMAPI](https://github.com/Pathoschild/SMAPI) | Modding API and loader for Stardew Valley | 2,756 | 🟢 | C# |
| [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader) | Proxy DLL that loads custom .asi plugins into any game process | 2,339 | 🟢 | C++ |
| [Multi Theft Auto](https://github.com/multitheftauto/mtasa-blue) | Multiplayer engine for GTA: San Andreas | 1,874 | 🟢 | C++ |
| [BWAPI](https://github.com/bwapi/bwapi) | Brood War API for writing StarCraft: Brood War AI bots | 1,709 | 🟢 | C++ |
| [LeviLamina](https://github.com/LiteLDev/LeviLamina) | Mod loader for Minecraft Bedrock Edition dedicated server | 1,694 | 🟢 | C++ |
| [Dalamud](https://github.com/goatcorp/Dalamud) | Plugin framework and API for Final Fantasy XIV | 1,640 | 🟢 | C |
| [MCP-Reborn](https://github.com/Hexeption/MCP-Reborn) | Modern Mod Coder Pack for decompiling and modding Minecraft Java | 1,565 | 🟢 |  |
| [BG3SE](https://github.com/Norbyte/bg3se) | Baldur's Gate 3 Script Extender | 1,525 | 🟢 | C++ |
| [CounterStrikeSharp](https://github.com/roflmuffin/CounterStrikeSharp) | C# server plugin framework for Counter-Strike 2 built on reverse engineered Source 2 internals | 1,373 | 🟢 | C# |
| [Yarn](https://github.com/FabricMC/yarn) | Open Minecraft deobfuscation mappings for modding | 1,226 | 🟢 | Java |
| [TiltedEvolution](https://github.com/tiltedphoques/TiltedEvolution) | Skyrim Together multiplayer mod built on reverse engineered engine internals | 1,184 | 🟢 | C++ |
| [ModEngine2](https://github.com/soulsmods/ModEngine2) | Runtime injection library for modding FromSoftware Souls games | 1,144 | 🗄️ | C++ |
| [RuntimeUnityEditor](https://github.com/ManlyMarco/RuntimeUnityEditor) | In-game inspector and debugging tools for Unity games | 1,121 | 🟢 | C# |
| [Reloaded-II](https://github.com/Reloaded-Project/Reloaded-II) | Universal .NET-powered modding framework for native x86/x64 games | 1,043 | 🟢 | C# |
| [Steamodded](https://github.com/Steamodded/smods) | Mod loader for Balatro | 987 | 🟢 | Lua |
| [xNVSE](https://github.com/xNVSE/NVSE) | New Vegas Script Extender | 851 | 🟢 | C++ |
| [Penumbra](https://github.com/xivdev/Penumbra) | Runtime mod loader for Final Fantasy XIV | 790 | 🟢 | C# |
| [Pengu Loader](https://github.com/PenguLoader/PenguLoader) | JavaScript plugin loader for the League of Legends client | 741 | 🟢 | C++ |
| [Godot Mod Loader](https://github.com/GodotModding/godot-mod-loader) | Generic mod loader for Godot games | 685 | 🟢 | GDScript |
| [plugin-sdk](https://github.com/DK22Pac/plugin-sdk) | SDK for ASI/CLEO plugins for GTA III, Vice City and San Andreas | 667 | 🟢 | C |
| [open.mp](https://github.com/openmultiplayer/open.mp) | Multiplayer mod for GTA San Andreas, backwards compatible with SA-MP | 652 | 🟢 | C++ |
| [me3](https://github.com/garyttierney/me3) | Mod Engine 3, a framework for modding and instrumenting FromSoftware games | 645 | 🟢 | Rust |
| [Lovely](https://github.com/ethangreen-dev/lovely-injector) | Runtime Lua injector for LOVE2D games such as Balatro | 610 | 🟢 | Rust |
| [Unity Mod Manager](https://github.com/newman55/unity-mod-manager) | Mod manager and loader for Unity games | 548 | 🟢 | C# |
| [FFNx](https://github.com/julianxhokaxhiu/FFNx) | Next-generation modding platform and driver for Final Fantasy VII and VIII PC | 523 | 🟢 | C++ |
| [Everest](https://github.com/EverestAPI/Everest) | Celeste mod loader and mod API | 519 | 🟢 | C# |
| [ModTheSpire](https://github.com/kiooeht/ModTheSpire) | External mod loader for Slay the Spire | 519 | 🟡 | Java |
| [BDSX](https://github.com/bdsx/bdsx) | Minecraft Bedrock Dedicated Server modding with Node.js | 491 | 🗄️ | TypeScript |
| [Phobos](https://github.com/Phobos-developers/Phobos) | Engine extension for C&C Red Alert 2: Yuri's Revenge | 462 | 🟢 | C++ |
| [RED4ext](https://github.com/wopss/RED4ext) | Script extender for REDengine 4 (Cyberpunk 2077) | 444 | 🟢 | C++ |
| [RetroMCP](https://github.com/MCPHackers/RetroMCP-Java) | Mod Coder Pack for decompiling and recompiling old Minecraft versions | 409 | 🟢 | Java |
| [ARCropolis](https://github.com/Raytwo/ARCropolis) | Modding framework for Super Smash Bros. Ultimate file replacement | 392 | 🟢 | Rust |
| [Oxide.Rust](https://github.com/OxideMod/Oxide.Rust) | Rust game extension for the Oxide modding framework | 388 | 🟢 | C# |
| [anno1800-mod-loader](https://github.com/magicalcookie/anno1800-mod-loader) | Mod loader for Anno 1800 | 368 | 🗄️ | C++ |
| [SFSE](https://github.com/ianpatt/sfse) | Starfield Script Extender | 359 | 🟢 | C++ |
| [SKSE64](https://github.com/ianpatt/skse64) | Skyrim Special Edition Script Extender | 358 | 🟢 | C++ |
| [REPENTOGON](https://github.com/TeamREPENTOGON/REPENTOGON) | Script extender for The Binding of Isaac: Repentance | 351 | 🟢 | C++ |
| [SatisfactoryModLoader](https://github.com/satisfactorymodding/SatisfactoryModLoader) | Unofficial mod loader for Satisfactory | 343 | 🟢 | C++ |
| [FFXIVClientStructs](https://github.com/aers/FFXIVClientStructs) | Reverse engineered native class layouts of the Final Fantasy XIV client | 342 | 🟢 | C# |
| [Hollow Knight Modding API](https://github.com/hk-modding/api) | Modding API for Hollow Knight built by patching game assemblies | 341 | 🟢 | C# |
| [Skyline](https://github.com/skyline-dev/skyline) | Runtime hooking and code patching environment for Nintendo Switch games | 314 | 🟢 | C++ |
| [xOBSE](https://github.com/llde/xOBSE) | Oblivion Script Extender | 312 | 🟢 | C++ |
| [unreal-vr](https://github.com/TheNewJavaman/unreal-vr) | Adds VR support to flatscreen Unreal Engine games | 301 | 🔴 | C++ |
| [ZHMModSDK](https://github.com/OrfeasZ/ZHMModSDK) | Modding SDK and mod loader for Hitman World of Assassination | 285 | 🟢 | C++ |
| [BakkesModSDK](https://github.com/bakkesmodorg/BakkesModSDK) | Unofficial SDK for Rocket League modding with BakkesMod | 283 | 🟢 | C++ |
| [MetaHookSv](https://github.com/MetaHookSv/MetaHookSv) | MetaHook plugin loader ported to the Sven Co-op GoldSrc engine | 260 | 🟢 | Python |
| [Reactor](https://github.com/NuclearPowered/Reactor) | Modding API for Among Us | 255 | 🟢 | C# |
| [UnrealModLoader](https://github.com/RussellJerome/UnrealModLoader) | Universal mod loader for Unreal Engine 4 games | 246 | 🔴 | C++ |
| [CommonLibSSE](https://github.com/Ryan-rsm-McKenzie/CommonLibSSE) | Reverse-engineered C++ library of Skyrim SE game types for plugin development | 241 | 🔴 | C++ |
| [BSIPA](https://github.com/nike4613/BeatSaber-IPA-Reloaded) | Unity mod injector built for Beat Saber | 204 | 🟢 | C# |
| [D2RMM](https://github.com/olegbl/d2rmm) | Mod manager for Diablo II: Resurrected | 201 | 🟢 | TypeScript |
| [Hedge Mod Manager](https://github.com/hedge-dev/HedgeModManager) | Mod manager and code loader for Sonic the Hedgehog PC games | 199 | 🟢 | C# |
| [CLEO 5](https://github.com/cleolibrary/CLEO5) | Script extension library for GTA San Andreas | 184 | 🟢 | C++ |
| [ME3Tweaks Mod Manager](https://github.com/ME3Tweaks/ME3TweaksModManager) | Mod manager for Mass Effect trilogy and Legendary Edition | 178 | 🟢 | C# |
| [R2API](https://github.com/risk-of-thunder/R2API) | Modding API for Risk of Rain 2 | 167 | 🟢 | C# |
| [RE_Kenshi](https://github.com/BFrizzleFoShizzle/RE_Kenshi) | Plugin loader and engine fixes for Kenshi | 166 | 🟢 | C++ |
| [kanan-new](https://github.com/cursey/kanan-new) | Quality-of-life mod framework for Mabinogi | 161 | 🗄️ | C++ |
| [F4SE](https://github.com/ianpatt/f4se) | Fallout 4 Script Extender | 156 | 🟢 | C++ |
| [Slippi ASM](https://github.com/project-slippi/slippi-ssbm-asm) | ASM codes adding rollback netplay and replay recording to Super Smash Bros. Melee | 154 | 🟢 | Assembly |
| [Creation-Kit-Platform-Extended](https://github.com/Perchik71/Creation-Kit-Platform-Extended) | Fixes and extensions for Bethesda's Creation Kit built from reverse engineering | 146 | 🟢 | C++ |
| [Dark-Souls-1-Overhaul](https://github.com/metal-crow/Dark-Souls-1-Overhaul) | Gameplay overhaul mod for Dark Souls built via reverse engineering | 140 | 🟢 | C++ |
| [FF8_demaster](https://github.com/MaKiPL/FF8_demaster) | Unofficial Final Fantasy VIII Remastered core mod | 137 | 🟢 | C |
| [skyrimse-test](https://github.com/Nukem9/skyrimse-test) | Reverse engineering and fixes for Skyrim Special Edition | 137 | 🟡 | C++ |
| [AutomataMP](https://github.com/praydog/AutomataMP) | NieR: Automata multiplayer mod | 134 | 🟡 | C++ |
| [MWSE](https://github.com/MWSE/MWSE) | Morrowind Script Extender with Lua scripting | 133 | 🟢 | C++ |
| [OTAPI](https://github.com/SignatureBeef/Open-Terraria-API) | Patched Terraria server assembly exposing hooks for modding | 124 | 🟢 | C# |
| [ACUFixes](https://github.com/NameTaken3125/ACUFixes) | Add-on and fixes for Assassin's Creed Unity | 113 | 🟡 | C++ |
| [TRLAU-menu-hook](https://github.com/TheIndra55/TRLAU-menu-hook) | Reverse engineering, menu and patches for Tomb Raider Legend/Anniversary/Underworld | 113 | 🟢 | C++ |
| [OWML](https://github.com/ow-mods/owml) | Mod loader and library for Outer Wilds | 109 | 🟢 | C# |
| [CommonLibSF](https://github.com/Starfield-Reverse-Engineering/CommonLibSF) | Collaborative reverse engineered library for Starfield modding | 100 | 🗄️ | C++ |
| [MKW-SP](https://github.com/mkw-sp/mkw-sp) | Mario Kart Wii mod with features built on reverse-engineered game code | 100 | 🟢 | C++ |
| [RB3Enhanced](https://github.com/RBEnhanced/RB3Enhanced) | Open-source plugin providing fixes and features for Rock Band 3 | 97 | 🟢 | C |
| [Installer](https://github.com/SteamClientHomebrew/Installer) | Installer for Millennium, a Steam client theming and plugin loader | 95 | 🟢 | C++ |
| [M2TWEOP-library](https://github.com/EOP-Labs/M2TWEOP-library) | Medieval II: Total War Engine Overhaul Project | 95 | 🟢 | C++ |
| [CommonLibF4](https://github.com/Ryan-rsm-McKenzie/CommonLibF4) | Reverse engineered library for Fallout 4 modding | 93 | 🟢 | C++ |
| [FA2sp](https://github.com/secsome/FA2sp) | Extension for the Red Alert 2 Final Alert 2 map editor | 88 | 🗄️ | C++ |
| [unrealmodding](https://github.com/AstroTechies/unrealmodding) | Rust tools and integrator for modding Unreal Engine games | 88 | 🟢 | Rust |
| [Spore ModAPI](https://github.com/Spore-Community/Spore-ModAPI) | C++ SDK for creating code mods for Spore | 86 | 🟢 | C++ |
| [libER](https://github.com/Dasaav-dsv/libER) | Elden Ring API library focused on binary compatibility | 76 | 🟡 | C++ |
| [fromsoftware-rs](https://github.com/vswarte/fromsoftware-rs) | Rust bindings to Elden Ring, Dark Souls 3, Nightreign and Sekiro internals | 74 | 🟢 | Rust |
| [SADX Mod Loader](https://github.com/X-Hax/sadx-mod-loader) | Mod loader for Sonic Adventure DX PC | 69 | 🟢 | C |
| [OBSE64](https://github.com/ianpatt/obse64) | Oblivion Remastered Script Extender | 64 | 🟡 | C++ |
| [SA2 Mod Loader](https://github.com/X-Hax/sa2-mod-loader) | Mod loader for Sonic Adventure 2 PC | 64 | 🟢 | C++ |
| [bg3se-macos](https://github.com/tdimino/bg3se-macos) | Baldur's Gate 3 Script Extender replication for macOS | 62 | 🟢 | C |
| [SharpPluginLoader](https://github.com/Fexty12573/SharpPluginLoader) | C# plugin loader for Monster Hunter World | 62 | 🟢 | C# |

## Open-source Game Clones

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Unciv](https://github.com/yairm210/Unciv) | Open-source Android/Desktop remake of Civ V. | 11,432 | 🟢 | Kotlin |
| [Space Station 14](https://github.com/space-wizards/space-station-14) | Space Station 14 is a revived attempt at a Space Station 13 remake. | 3,858 | 🟢 | C# |
| [Taisei](https://github.com/taisei-project/taisei) | Fan-made, open-source clone of the Touhou series. | 1,646 | 🟢 | C |
| [KeeperFX](https://github.com/dkfans/keeperfx) | Open source remake and Fan Expansion of Dungeon Keeper. | 1,018 | 🟢 | C |
| [OpenCiv3](https://github.com/C7-Game/OpenCiv3) | OpenCiv3 is an open-source, cross-platform, mod-oriented, modernized remake of Civilization III by the fan community... | 665 | 🟢 | C# |
| [OpenApocalypse](https://github.com/OpenApoc/OpenApoc) | Rebuild of the X-COM: Apocalypse engine. | 597 | 🟢 | C++ |
| [OpenKeeper](https://github.com/tonihele/OpenKeeper) | Dungeon Keeper II remake in Java. | 506 | 🟢 | Java |
| [openomf](https://github.com/omf2097/openomf) | One Must Fall 2097 Remake. | 484 | 🟢 | C |
| [KaM Remake](https://github.com/Kromster80/kam_remake) | RTS game remake of Knights and Merchants written in Delphi from scratch. | 377 | 🗄️ | Pascal |
| [Dune-II---The-Maker](https://github.com/stefanhendriks/Dune-II---The-Maker) | A remake of the classic Dune 2 - The Building of a Dynasty (by Westwood Studios) with several enhancements. Like: hig... | 368 | 🟢 | C++ |
| [Romanov's Vengeance](https://github.com/MustaphaTR/Romanovs-Vengeance) | Remake of C&C Red Alert 2 based on the OpenRA engine | 344 | 🟡 | C# |
| [Syndicate Wars](https://github.com/swfans/syndwarsfx) | Syndicate Wars Fan Expansion, Open Source remake of the classic Bullfrog game. | 261 | 🟢 | C |
| [Mr.Boom](https://github.com/Javanaise/mrboom-libretro) | 8-player Bomberman clone for RetroArch/Libretro. | 228 | 🟢 | C |
| [freeserf.net](https://github.com/Pyrdacor/freeserf.net) | Settlers 1 clone written in C# | 173 | 🟢 | C# |
| [UAlbion](https://github.com/csinkers/ualbion) | Remake of 1995 Albion. | 168 | 🟢 | C# |
| [war1](https://github.com/acoto87/war1) | A remake of Warcraft: Orcs & Humans written in C | 152 | 🟢 | C |
| [OPHD](https://github.com/OutpostUniverse/OPHD) | OutpostHD - Open source remake of Sierra On-Line's Outpost. | 145 | 🟢 | C++ |
| [OpenKrush](https://github.com/IceReaper/OpenKrush) | Remake of KKnD (Krush, Kill 'n' Destroy) and KKnD2 based on the OpenRA engine | 127 | 🟢 | C# |
| [OpenSA](https://github.com/Dzierzan/OpenSA) | Remake of Swarm Assault based on the OpenRA engine | 124 | 🔴 | C# |
| [Antares](https://github.com/arescentral/antares) | Remake of Ares, a tactical space combat game. | 111 | 🟡 | C++ |
| [Lionheart Remake](https://github.com/b3dgs/lionheart-remake) | Java remake of Lionheart Amiga game. | 86 | 🟢 | Java |
| [vera20k](https://github.com/YuriPlanet/vera20k) | Red Alert 2: Yuri's Revenge — rebuilt from scratch in Rust for large multiplayer battles. | 84 | 🟢 | Rust |
| [Shattered Paradise](https://github.com/ABrandau/Shattered-Paradise-SDK) | Remake of C&C Tiberian Sun based on the OpenRA engine | 82 | 🟡 | C# |
| [OpenE2140](https://github.com/OpenE2140/OpenE2140) | Remake of Earth 2140 based on the OpenRA engine | 72 | 🟢 | C# |
| [Dungeon Keeper Remake](https://github.com/Themperror/Dungeon-Keeper-Remake) | A modern remake of Dungeon Keeper | 36 | 🟢 | C++ |
| [SeriousSamAlphaRemake](https://github.com/tx00100xt/SeriousSamAlphaRemake) | Serious Sam Alpha Remake open source project based. | 31 | 🟡 | C++ |
| [O21](https://github.com/ForNeVeR/O21) | FOSS remake of U95, an old submarine arcade game from 1995. | 30 | 🟢 | F# |
| [OpenReliant](https://github.com/OpenReliant/openreliant) | Rebuild of Starlancer in Zig and SDL3. | 27 | 🟢 | Zig |
| [parabellum](https://github.com/andreapavoni/parabellum) | An attempt to build a #Travian 3.x clone written in #Rust. | 27 | 🟢 | Rust |
| [rebellion2](https://github.com/davidadas/rebellion2) | Remake of the classic Star Wars Rebellion game for PC using Unity | 27 | 🟢 | C# |
| [Space Empires 4](https://github.com/lowlevelmetal/OpenSE4) | Spec-based remake of Space Empires 4. | 14 | 🟢 | C++ |
| [open-iw](https://github.com/TambourineReindeer/open-iw) | Remake/rebuild of Sleepless Software's fantasy platformer Inner Worlds. | 8 | 🔴 | C++ |
| [DetectiveDS](https://github.com/benbaker76/DetectiveDS) | A remake of the original C64 classic The Detective Game for Nintendo DS. | 6 | 🟢 | C++ |
| [starcup](https://github.com/teamstarcup/starcup) | A fork of the multiplayer game Space Station 14, a remake of the cult-classic Space Station 13. | 6 | 🟢 | C# |
| [Heart-of-Africa-Remake](https://github.com/PatrickVonMassow/Heart-of-Africa-Remake) | Single-player 3D web remake of the 1985 classic The Heart of Africa: real ~1890 geography, living wildlife, period jo... | 5 | 🟢 | JavaScript |
| [Transarctica-2](https://github.com/SembeiNorimaki/Transarctica-2) | Remake of the classic game Transarctica (In development) | 3 | 🟢 | GDScript |
| [atomiks](https://github.com/carstene1ns/atomiks) | A remake of the classic Atomix game for modern platforms. | 2 | 🟢 | C |
| [Retro-Arcade-Remakes](https://github.com/danywaked/Retro-Arcade-Remakes) | C++ retro arcade remakes showcasing clean OOP design, game loops, collision systems, and state management. | 2 | 🟢 | C++ |
| [WarhawkDS](https://github.com/benbaker76/WarhawkDS) | Warhawk DS remake of the C64 game Warhawk to the Nintendo DS in native assembler. | 2 | 🟢 | Assembly |
| [AcidDrop](https://github.com/lostjared/AcidDrop) | Remake of classic Atari 2600 game "Acid Drop". | 1 | 🟢 | C++ |
| [blips](https://github.com/joyrider3774/blips) | A Remake of the dos Bips, Bips Gold and Bips Platinum game from Bryant Brownell. It is a Puzzle game which is a varia... | 1 | 🟢 | C++ |
| [galaxy-eggbert](https://github.com/openeggbert/galaxy-eggbert) | 3D remake of Speedy Blupi / Mobile Eggbert, moving from Urho3D toward a native CNA + Easy3D engine. | 1 | 🟢 | C++ |
| [2004scape](https://2004scape.org) | A free & open-source remake of 2004 era RuneScape 2. |  | ⚪ |  |
| [2009scape](https://2009scape.org) | A free & open-source remake of 2009 era RuneScape 2. |  | ⚪ |  |
| [Barbarian](http://barbarian.1987.free.fr/indexEN.htm) | Open-source clone of Barbarian: The Ultimate Warrior. |  | ⚪ |  |
| [darknova2](https://github.com/deadjim/darknova2) | Dark Nova ][ — cross-platform space trading game (Space Trader remake) | 0 | 🟢 | Dart |
| [Dune Legacy](https://sourceforge.net/projects/dunelegacy/) | Updated clone of Westood Studios' Dune2 which uses data files from the original game. |  | ⚪ |  |
| [GradiusRemake](https://github.com/luisfae/GradiusRemake) | Remake of the game Gradius (NES - 1986) | 0 | 🟢 | GDScript |
| [guardian](https://github.com/LaughingInPurgatory/guardian) | A modern, endless remake of the classic arcade game Defender | 0 | 🟢 | JavaScript |
| [Maze-Runner-FPS](https://github.com/IbsYoussef/Maze-Runner-FPS) | Remake of classic Maze Runner game from the 70s -- written in Rust | 0 | 🟢 | Rust |
| [Opengate](https://sourceforge.net/projects/opengate/) | Remake of Jumpgate. |  | ⚪ |  |
| [OpenPrivateer](https://openprivateer.org/) | Open-source remake of Wing Commander: Privateer (1993). Requires original game files. |  | ⚪ |  |
| [OrbitalDecay](https://github.com/LeineckerGames/OrbitalDecay) | This is a 3D remake of the old Lunar Lander game | 0 | 🟢 | HTML |
| [Project Wormhole](https://gitlab.com/znixian/xftl) | Rebuild of FTL (Subset Games). Ported to Android in Pocket Wormhole. |  | ⚪ |  |
| [Sunny-Survival-Remake-Code](https://github.com/Kynwi/Sunny-Survival-Remake-Code) | Code for my game called "Sunny Survival Remake" | 0 | 🟢 | C# |
| [VoxeLibre](https://git.minetest.land/VoxeLibre/VoxeLibre) | Stable, moddable & free/libre clone of Minecraft based on the Luanti engine. |  | ⚪ |  |
| [wedges-trial](https://github.com/begiedz/wedges-trial) | [WIP] Browser logic puzzle game inspired by Gothic's Remake lockpicking mechanism. | 0 | 🟢 | TypeScript |
| [Zed Online](https://sourceforge.net/projects/zedonline/) | Remake of the 1996 classic game Z. |  | ⚪ |  |

## Other

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Zelda64Recomp](https://github.com/Zelda64Recomp/Zelda64Recomp) | Static recompilation of Majora's Mask for PC | 7,394 | 🟢 | C |
| [VoxelSpace](https://github.com/s-macke/VoxelSpace) | Reverse engineered Comanche Voxel Space terrain rendering algorithm | 6,809 | 🟡 | C |
| [UnleashedRecomp](https://github.com/hedge-dev/UnleashedRecomp) | Unofficial PC port of Xbox 360 Sonic Unleashed via static recompilation | 5,162 | 🟢 | C++ |
| [REDRIVER2](https://github.com/OpenDriver2/REDRIVER2) | Driver 2 PlayStation reverse engineering and PC port | 1,397 | 🟢 | C |
| [project-restoration](https://github.com/leoetlino/project-restoration) | Majora's Mask 3D patch restoring original mechanics via reverse engineering | 805 | 🔴 | C++ |
| [GameTracking-Dota2](https://github.com/SteamTracking/GameTracking-Dota2) | Automated tracker of Dota 2 game file and protobuf changes | 770 | 🟢 | C++ |
| [Silent Hill 2 Enhanced Edition](https://github.com/elishacloud/Silent-Hill-2-Enhancements) | A project designed to enhance Silent Hill 2 (SH2) graphics and audio for the PC. It also includes scripts to build or... | 712 | 🟢 | C |
| [smw](https://github.com/snesrev/smw) | Super Mario World reimplementation in C | 639 | 🟡 | C |
| [Plants-vs.-Zombies-Online-Battle](https://github.com/Zhuagenborn/Plants-vs.-Zombies-Online-Battle) | Two-player online battle mode for Plants vs. Zombies built via reverse engineering and DLL injection | 627 | 🟡 | C++ |
| [Roblox-Client-Tracker](https://github.com/MaximumADHD/Roblox-Client-Tracker) | Automated tracker extracting information about each Roblox client version | 558 | 🟢 | Assembly |
| [HiveWE](https://github.com/stijnherfst/HiveWE) | A Warcraft III world editor. | 483 | 🟢 | C++ |
| [HaloCEVR](https://github.com/LivingFray/HaloCEVR) | VR conversion of the original PC Halo: Combat Evolved | 443 | 🟢 | C++ |
| [sfall](https://github.com/sfall-team/sfall) | sfall - Engine modifications for Fallout 2 | 440 | 🟢 | C++ |
| [UnofficialCrusaderPatch2](https://github.com/UnofficialCrusaderPatch/UnofficialCrusaderPatch2) | Unofficial balancing and bugfix patch installer for Stronghold Crusader | 433 | 🟡 | C# |
| [Wind Waker Randomizer](https://github.com/LagoLunatic/wwrando) | Wind Waker Randomizer | 427 | 🟢 | Python |
| [SR](https://github.com/M-HT/SR) | A project to statically recompile following games to create Windows or Linux (x86 or arm) versions of the games - Alb... | 426 | 🟢 | C |
| [mgs2sos](https://github.com/oct0xor/mgs2sos) | Mod adding third-person camera and controls to MGS2: Substance | 311 | 🔴 | C++ |
| [PAL3patch](https://github.com/zhangboyang/PAL3patch) | Resolution patch for Chinese Paladin 3 | 250 | 🟡 | C |
| [Prepare Carefully](https://github.com/edbmods/EdBPrepareCarefully) | EdB Prepare Carefully, a RimWorld mod | 249 | 🟡 | C# |
| [sc2kfix](https://github.com/sc2kfix/sc2kfix) | Bugfix and modding plugin for SimCity 2000 Special Edition | 210 | 🟢 | C++ |
| [popcap-patches](https://github.com/cheez3d/popcap-patches) | Patched executables and research notes for PopCap games | 195 | 🔴 |  |
| [psx-spx.github.io](https://github.com/psx-spx/psx-spx.github.io) | Technical reference for the original PlayStation hardware | 164 | 🟢 | Awk |
| [wiki](https://github.com/xboxoneresearch/wiki) | Xbox One research wiki | 149 | 🟢 | Dockerfile |
| [ReversingMinesweeper](https://github.com/repnz/ReversingMinesweeper) | Reverse Engineering Minesweeper: Reconstruct Minesweeper Source Code | 146 | 🔴 | C |
| [x360-research](https://github.com/InvoxiPlayGames/x360-research) | Xbox 360 reverse engineering notes and utilities | 134 | 🟢 |  |
| [Sonic Adventure Toolset](https://github.com/X-Hax/sa_tools) | Sonic Adventure Toolset | 131 | 🟢 | C# |
| [Quad64](https://github.com/DavidSM64/Quad64) | An open-source Super Mario 64 level editor | 128 | 🔴 | C# |
| [Grit Game Engine](https://github.com/grit-engine/grit-engine) | Grit Game Engine | 125 | 🔴 | C++ |
| [Ultima IV Remastered](https://github.com/MagerValp/u4remastered) | Ultima IV Remastered for the C64 | 123 | 🔴 | Assembly |
| [SAMP-Mobile](https://github.com/kuzia15/SAMP-Mobile) | Open-source SA:MP mobile multiplayer client | 117 | 🟢 |  |
| [botw-re-notes](https://github.com/leoetlino/botw-re-notes) | Reverse engineering notes and tools for Zelda: Breath of the Wild | 110 | 🔴 | C |
| [grand-theft-auto-for-unity](https://github.com/mukaschultze/grand-theft-auto-for-unity) | Loads original Grand Theft Auto map and model formats into Unity | 105 | 🟡 | C# |
| [Chunithm-Research](https://github.com/Suprnova/Chunithm-Research) | In-depth reverse engineering documentation of SEGA Chunithm | 94 | 🔴 |  |
| [opendpr](https://github.com/TeamLumi/opendpr) | Reverse engineered recreation of Pokemon Brilliant Diamond and Shining Pearl | 94 | 🟢 | C# |
| [Max_Vita](https://github.com/fgsfdsfgs/max_vita) | Tool for Max Payne game data (osgameclones) (C) | 93 | 🔴 | C |
| [VTXCart](https://github.com/xvortex/VTXCart) | Reverse engineering a Neo Geo 161-in-1 cartridge to change ROMs | 90 | 🟡 | C |
| [GameTracking-TF2](https://github.com/SteamTracking/GameTracking-TF2) | Automated tracker of Team Fortress 2 game file changes | 89 | 🟢 | Shell |
| [re_nfpii](https://github.com/GaryOderNichts/re_nfpii) | Reimplementation of the Wii U nn_nfp amiibo library | 88 | 🟡 | C++ |
| [tentacli](https://github.com/tench-rt/tentacli) | Tentacli is a framework for building extensible network protocol clients via modular plugins | 83 | 🟢 | Rust |
| [The Lost Vikings/Blackthorne Tools](https://github.com/RyanMallon/TheLostVikingsTools) | Reverse Engineered Tools/Library for the DOS game The Lost Vikings | 83 | 🔴 | C |
| [agario-client](https://github.com/pulviscriptor/agario-client) | Node.js agar.io client implementation | 82 | 🔴 | JavaScript |
| [GameTracking-Deadlock](https://github.com/SteamTracking/GameTracking-Deadlock) | Automated tracker of Deadlock game file and protobuf changes | 81 | 🟢 | C++ |
| [GuildWarsMapBrowser](https://github.com/Jonathan-Greve/GuildWarsMapBrowser) | Browse Guild Wars maps from the game's .dat file | 81 | 🟢 | C++ |
| [magicka-patch](https://github.com/Alexander-Aue-Johr/magicka-patch) | Reverse engineered fixes and optimisations for Magicka | 81 | 🟢 | C# |
| [nge_2_re](https://github.com/rezual/nge_2_re) | Neon Genesis Evangelion 2 reverse engineering and translation | 78 | 🟢 | Python |
| [ReMasters](https://github.com/kwsch/ReMasters) | Reverse engineering Pokemon Masters | 74 | 🔴 | C# |
| [tekken3-expanded](https://github.com/omarma/tekken3-expanded) | Adds Tekken Tag Tournament characters to Tekken 3 | 68 | 🟢 | C++ |
| [sf4e](https://github.com/fabeloper/sf4e) | Rollback netcode mod for Ultra Street Fighter IV (Steam) | 62 | 🟢 | C++ |
| [xbox-board-re](https://github.com/LoveMHz/xbox-board-re) | Board-level reverse engineering of the original Xbox | 62 | 🔴 | Python |
| [XboxSeries](https://github.com/DanielLMcGuire/XboxSeries) | Research into the Xbox Series architecture | 62 | 🟢 |  |
| [gctools](https://github.com/fuzziqersoftware/gctools) | Video game file translation tools | 60 | 🟡 |  |
| [v-on-patcher](https://github.com/pairomaniac/v-on-patcher) | Patcher for Cyber Troopers Virtual-On (PC, 1997) with modern hardware and online support | 60 | 🟢 | Python |
| [DarkSoulsIII.FileFormats](https://github.com/Atvaark/DarkSoulsIII.FileFormats) | Dark Souls III archive file format information | 59 | 🔴 |  |
| [3DSort](https://github.com/SalustLab/3DSort) | Rearrange the Nintendo 3DS HOME menu from a PC | 58 | 🟢 | Python |
| [DecimaTools](https://github.com/Wunkolo/DecimaTools) | Tools and research for reverse engineering the Decima game engine | 57 | 🔴 | C++ |
| [phoenixtools](https://github.com/Missingmew/phoenixtools) | Tools and documentation for the Ace Attorney game series | 55 | 🟡 | C++ |
| [OpenDriver2Tools](https://github.com/OpenDriver2/OpenDriver2Tools) | Tools for Driver 1 and Driver 2 game formats | 54 | 🟢 | C++ |
| [Silent-Hill](https://github.com/Sparagas/Silent-Hill) | Silent Hill file format reverse engineering | 54 | 🟢 | C |
| [silent-hill-museum](https://github.com/dreamingmoths/silent-hill-museum) | Web museum and viewer of Silent Hill models from the original game files | 54 | 🟢 | TypeScript |
| [KingsFieldRE](https://github.com/IvanDSM/KingsFieldRE) | King's Field II reverse engineering tools and documentation | 53 | 🔴 | C++ |
| [reevengi-tools](https://github.com/pmandin/reevengi-tools) | Tools to check reverse engineering of Resident Evil file formats | 53 | 🟢 | C |
| [Vagrant-Story-Unity-Parser](https://github.com/korobetski/Vagrant-Story-Unity-Parser) | Unity editor scripts that read original Vagrant Story data | 51 | 🟡 | C# |
| [NFSPluginSDK](https://github.com/berkayylmao/NFSPluginSDK) | Reversed types of BlackBox-era Need for Speed games for plugin and script mods | 50 | 🟡 | C++ |
| [driver-tools](https://github.com/Fireboyd78/driver-tools) | Modding tools for DRIV3R, Driver: Parallel Lines and Driver: San Francisco | 48 | 🔴 | C# |
| [bedrock-headers](https://github.com/mcbedrock/bedrock-headers) | Reverse-engineered modding headers for Minecraft: Bedrock Edition | 47 | 🔴 | C++ |
| [mkw-structures](https://github.com/SeekyCt/mkw-structures) | Documentation of Mario Kart Wii internal structures | 46 | 🟡 | C++ |
| [Super-Mario-64-DS-Remastered](https://github.com/ExcellentGamer/Super-Mario-64-DS-Remastered) | **OPEN SOURCE EPIC** | 46 | 🔴 | C |
| [Medal-Of-Honor-PSX-File-Viewer](https://github.com/AdrianoDiDio/Medal-Of-Honor-PSX-File-Viewer) | Tools to open and view files from the PSX Medal of Honor games | 45 | 🟢 | C |
| [OpenAdhoc](https://github.com/Nenkai/OpenAdhoc) | Open-source re-implementation of Gran Turismo Adhoc scripts | 44 | 🟢 | C |
| [Genesis 68K Static Recompiler](https://github.com/mstan/segagenesisrecomp) | Sega Genesis / Mega Drive game static recompiler ecosystem · Part of the R.A.I.D. community | 43 | 🟢 | C |
| [Lotus STE](https://github.com/jonathanopalise/lotus-ste) | Enhancements to the Atari ST version of Lotus Esprit Turbo Challenge to support STE hardware features | 42 | 🔴 | Assembly |
| [DRV3-Sharp](https://github.com/CaptainSwag101/DRV3-Sharp) | Tools for working with Danganronpa V3 PC files | 39 | 🟡 | C# |
| [SilentHillMapExaminer](https://github.com/ItEndsWithTens/SilentHillMapExaminer) | BizHawk utility to reverse engineer the Silent Hill map format | 39 | 🟢 | C# |
| [ExCrypt](https://github.com/emoose/ExCrypt) | Open-source replacement for the Xbox 360 XeCrypt suite | 37 | 🟢 | C |
| [lba-engine-architecture](https://github.com/LBALab/lba-engine-architecture) | Little Big Adventure engine architecture documentation | 35 | 🟡 | Ruby |
| [osdbits](https://github.com/aap/osdbits) | Parts of the PlayStation 2 OSDSYS reverse engineered | 33 | 🟢 | C |
| [MiiJS](https://github.com/Stewared/MiiJS) | JavaScript library for reading, writing and rendering Nintendo Mii data | 32 | 🟢 | JavaScript |
| [Ultima V Remastered](https://github.com/Drunella/u5remastered) | Ultima V remastered for EasyFlash and 1581 | 32 | 🟡 | Assembly |
| [plugin-sdk-sa](https://github.com/Dryxio/plugin-sdk-sa) | GTA San Andreas plugin SDK extended from a fully reverse-engineered codebase | 31 | 🟢 | C |
| [Beasts and Bumpkins Fan Patch](https://github.com/bb-patch/bb-patch) | Tool for Beasts and Bumpkins game data (osgameclones) (Go) | 29 | 🔴 | Go |
| [AWTools](https://github.com/Nostritius/AWTools) | Tools for reverse-engineered file formats of Alan Wake and later Remedy games | 27 | 🔴 | Python |
| [darkstone-re](https://github.com/glampert/darkstone-re) | Tools to reverse engineer the file formats of the game Darkstone | 21 | 🟢 | C |
| [ShinDataUtil](https://github.com/DCNick3/ShinDataUtil) | This is an utility for working with game files of Higurashi no Naku Koro ni and Kono Subarashii Sekai ni Shukufuku wo... | 20 | 🟢 | C# |
| [DarkReignLauncher](https://github.com/Nielk1/DarkReignLauncher) | Tool for Dark Reign: The Future of War game data (osgameclones) (C#) | 19 | 🔴 | C# |
| [hobbitgfx](https://github.com/richcarl/hobbitgfx) | The Hobbit graphics engine | 19 | 🔴 | JavaScript |
| [Princed Resources](https://github.com/NagyD/PR) | Princed Resources is a tool to export and import graphics and other data from and to DAT files of Prince of Persia 1... | 19 | 🔴 | C |
| [Siege Studio](https://github.com/open-siege/siege-studio) | Siege Studio is a desktop application for previewing, modifying and converting reverse engineered file formats for ga... | 18 | 🟢 | C++ |
| [utkencode](https://github.com/daddesio/utkencode) | Encoder for EA MicroTalk, a speech codec based on multi-pulse linear prediction used in various EA games. This encode... | 16 | 🔴 | C |
| [re-virtua-cop-2](https://github.com/jevarg/re-virtua-cop-2) | Reverse engineering of Virtua Cop 2 PC (1997) | 12 | 🟢 | TypeScript |
| [TTDPatch](https://github.com/ttdpatch/ttdpatch) | The master TTDPatch repository | 11 | 🔴 | Assembly |
| [TD3Extract](https://github.com/yuv422/TD3Extract) | A tool for extracting data files from the game - Test Drive III "The Passion" | 7 | 🔴 | C++ |
| [Fantastic Dizzy Tools](https://github.com/RyanMallon/dizzy) | Reverse engineering tools for Fantastic Dizzy | 6 | 🔴 | Python |
| [mpromtool](https://github.com/gamemasterplc/mpromtool) | Mario Party 1-3 ROM Extractor/Rebuilder Tool | 6 | 🟡 | C++ |
| [Super Mario Brothers High Level Disassembly](https://github.com/NexusEast/Console_Development) | My attempt to develop every single console i can | 2 | 🔴 | Assembly |
| [VBEditor](https://github.com/kran27/VBEditor) | A heavily work-in-progress editor for the proprietary file formats used in Fallout Van Buren | 1 | 🗄️ | Visual Basic .NET |

## Private Servers

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [TrinityCore](https://github.com/TrinityCore/TrinityCore) | World of Warcraft server emulator (MaNGOS fork) | 10,819 | 🟢 | C++ |
| [AzerothCore](https://github.com/azerothcore/azerothcore-wotlk) | Modular World of Warcraft 3.3.5a server emulator | 9,029 | 🟢 | C++ |
| [Cuberite](https://github.com/cuberite/cuberite) | Lightweight extensible Minecraft server in C++ | 5,455 | 🟢 | C++ |
| [rAthena](https://github.com/rathena/rathena) | Ragnarok Online server emulator in C++ | 3,602 | 🟢 | C++ |
| [PocketMine-MP](https://github.com/pmmp/PocketMine-MP) | Minecraft Bedrock server software built from scratch in PHP | 3,580 | 🗄️ | PHP |
| [Minestom](https://github.com/Minestom/Minestom) | Lightweight Minecraft Java server written from scratch without vanilla code | 3,305 | 🟢 | Java |
| [Valence](https://github.com/valence-rs/valence) | Rust framework for building Minecraft Java servers | 3,279 | 🟢 | Rust |
| [FerrumC](https://github.com/ferrumc-rs/ferrumc) | Reimplementation of the Minecraft server in Rust | 2,428 | 🟢 | Rust |
| [Impostor](https://github.com/Impostor/Impostor) | Open-source reimplementation of the Among Us game server | 2,373 | 🟢 | C# |
| [Glowstone](https://github.com/GlowstoneMC/Glowstone) | Open-source Minecraft Java server implementation | 2,011 | 🟢 | Java |
| [The Forgotten Server](https://github.com/otland/forgottenserver) | Open Tibia MMORPG server emulator in C++ | 1,842 | 🟢 | C++ |
| [LunarCore](https://github.com/Melledy/LunarCore) | A game server reimplementation for a certain turn-based anime game | 1,430 | 🟢 | Java |
| [YgoMaster](https://github.com/pixeltris/YgoMaster) | Offline Yu-Gi-Oh! Master Duel | 1,382 | 🟢 | C# |
| [Nukkit](https://github.com/CloudburstMC/Nukkit) | Minecraft Bedrock Edition server software in Java | 1,358 | 🟢 | Java |
| [HeavenMS](https://github.com/ronancpl/HeavenMS) | MapleStory v83 private server emulator (archived) | 1,215 | 🗄️ | Java |
| [OpenMU](https://github.com/MUnique/OpenMU) | Server for the MMORPG MU Online | 1,211 | 🟢 | C# |
| [DWC Network Server Emulator](https://github.com/barronwaffles/dwc_network_server_emulator) | Nintendo Wi-Fi Connection server emulator for DS and Wii games | 1,183 | 🟡 | Python |
| [CMaNGOS Classic](https://github.com/cmangos/mangos-classic) | Continued MaNGOS World of Warcraft Classic server emulator | 1,091 | 🟢 | C++ |
| [lunar-tear](https://github.com/Walter-Sparrow/lunar-tear) | Private server research project for a certain discontinued mobile game | 1,079 | 🟢 | Go |
| [MaNGOS Zero](https://github.com/mangoszero/server) | World of Warcraft vanilla server emulator | 1,035 | 🟢 | C++ |
| [Hercules](https://github.com/HerculesWS/Hercules) | Ragnarok Online server emulator | 1,017 | 🟢 | C++ |
| [VMaNGOS](https://github.com/vmangos/core) | Progressive vanilla World of Warcraft server emulator for patches 1.2-1.12 | 963 | 🟢 | C++ |
| [Dragonfly](https://github.com/df-mc/dragonfly) | Minecraft Bedrock Edition server software in Go | 850 | 🟢 | Go |
| [Sapphire](https://github.com/SapphireServer/Sapphire) | Final Fantasy XIV server emulator (4.0+) in C++ | 835 | 🟢 | C++ |
| [ds3os](https://github.com/TLeonardUK/ds3os) | Dark Souls 3 and Dark Souls 2 private server emulator | 785 | 🟢 | CMake |
| [Darkflame Server](https://github.com/DarkflameUniverse/DarkflameServer) | LEGO Universe server emulator | 759 | 🟢 | C++ |
| [ServUO](https://github.com/ServUO/ServUO) | Ultima Online server emulator in C# | 757 | 🟢 | C# |
| [ageLANServer](https://github.com/luskaner/ageLANServer) | Web server and launcher for offline/LAN multiplayer in Age of Empires titles | 740 | 🟢 | Go |
| [NexusForever](https://github.com/NexusForever/NexusForever) | Server emulator for the defunct MMORPG WildStar | 675 | 🟢 | C# |
| [Canary](https://github.com/opentibiabr/canary) | OpenTibia server emulator for modern Tibia protocol versions | 654 | 🟢 | Lua |
| [PvPGN](https://github.com/pvpgn/pvpgn-server) | Player vs Player Gaming Network: Battle.net and Westwood Online server emulator | 647 | 🟢 | C++ |
| [EQEmu](https://github.com/EQEmu/EQEmu) | EverQuest server emulator | 635 | 🟢 | C++ |
| [flying-squid](https://github.com/PrismarineJS/flying-squid) | Minecraft Java server implemented in Node.js | 610 | 🟢 | JavaScript |
| [EpinelPS](https://github.com/EpinelPS/EpinelPS) | A private server for some anime game | 566 | 🟢 | C# |
| [MHServerEmu](https://github.com/Crypto137/MHServerEmu) | Server emulator for Marvel Heroes | 565 | 🟢 | C# |
| [CMaNGOS WotLK](https://github.com/cmangos/mangos-wotlk) | World of Warcraft 3.3.5 server emulator (C(ontinued)-MaNGOS) | 556 | 🟢 | C++ |
| [CMaNGOS TBC](https://github.com/cmangos/mangos-tbc) | World of Warcraft 2.4.3 server emulator (C(ontinued)-MaNGOS) | 521 | 🟢 | C++ |
| [LandSandBoat](https://github.com/LandSandBoat/server) | Final Fantasy XI server emulator | 512 | 🟢 | Lua |
| [Arcaea-server](https://github.com/Lost-MSth/Arcaea-server) | 一个微型的 Arcaea 本地服务器 A small local server for Arcaea | 488 | 🟢 | Python |
| [OpenCoreMMO](https://github.com/OpenCoreMMO/OpenCoreMMO) | Modern C# MMORPG server emulator for an OpenTibia-style client | 481 | 🟢 | C# |
| [POGOserver](https://github.com/maierfelix/POGOserver) | Pokemon GO server emulator | 476 | 🔴 | JavaScript |
| [PyRoyale](https://github.com/Igoorx/PyRoyale) | Open-source server emulator for the Mario Royale browser game | 455 | 🗄️ | Python |
| [Darkstar Project](https://github.com/DarkstarProject/darkstar) | Deprecated Final Fantasy XI server emulator | 450 | 🗄️ | TSQL |
| [Houdini](https://github.com/solero/houdini) | Club Penguin private server written in Python 3 | 423 | 🟢 | Python |
| [OpenKO](https://github.com/Open-KO/KnightOnline) | Knight Online server and client reimplementation project | 367 | 🟢 | C++ |
| [ModernUO](https://github.com/modernuo/ModernUO) | High-performance Ultima Online server emulator in C# | 362 | 🟢 | C# |
| [ACE](https://github.com/ACEmulator/ACE) | Asheron's Call server emulator | 345 | 🟢 | C# |
| [Kepler](https://github.com/Quackster/Kepler) | Java server reviving Habbo Hotel v14 (2007 era) | 329 | 🟢 | Java |
| [entralinked](https://github.com/kuroppoi/entralinked) | Standalone Game Sync server emulator for Pokémon Black & White | 321 | 🟢 | Java |
| [Melia](https://github.com/NoCode-NoLife/Melia) | Open-source MMORPG server emulator (Tree of Savior) | 301 | 🟢 | C# |
| [starpoint](https://github.com/duosii/starpoint) | Server emulator for a mobile pinball game. | 291 | 🟡 | TypeScript |
| [bancho.py](https://github.com/osuAkatsuki/bancho.py) | A private osu! server for everyone. Simpler than Akatsuki's production stack, while maintaining core functionality, p... | 287 | 🟢 | Python |
| [Lost City Server](https://github.com/LostCityRS/Server) | RuneScape 2004-era server emulator | 279 | 🟢 | JavaScript |
| [newserv](https://github.com/fuzziqersoftware/newserv) | Phantasy Star Online game server, proxy and reverse-engineering tools | 277 | 🟢 | C++ |
| [dndserver](https://github.com/Snaacky/dndserver) | Dark and Darker private server implementation in Python | 275 | 🗄️ | Python |
| [Erupe](https://github.com/Mezeporta/Erupe) | Monster Hunter Frontier server emulator in Go | 275 | 🗄️ | Go |
| [RPCN](https://github.com/RipleyTom/rpcn) | PSN-compatible server used by RPCS3 for online play | 270 | 🟢 | Rust |
| [bemaniutils](https://github.com/DragonMinded/bemaniutils) | Hobby game services network for Konami Bemani arcade games | 263 | 🟢 | Python |
| [RunUO](https://github.com/runuo/runuo) | Classic Ultima Online server emulator in C# | 258 | 🟡 | C# |
| [MCGalaxy](https://github.com/ClassiCube/MCGalaxy) | Minecraft Classic protocol server software | 234 | 🟢 | C# |
| [PayCheck3](https://github.com/SlejmUr/PayCheck3) | Payday 3 server emulator | 216 | 🟢 | C# |
| [Open Toontown](https://github.com/open-toontown/open-toontown) | Open-source Toontown Online based on the final Disney client version | 206 | 🟢 | Python |
| [bravo](https://github.com/bravoserver/bravo) | Reverse engineered Minecraft server implementation (1.4.x protocol) | 205 | 🔴 | Python |
| [Apollo](https://github.com/apollo-rsps/apollo) | RuneScape private server suite in Java | 194 | 🔴 | Java |
| [OpenSpy Core](https://github.com/openspy/openspy-core) | GameSpy replacement backend services (master server, NAT negotiation, presence) | 191 | 🟢 | C++ |
| [SWGEmu Core3](https://github.com/swgemu/Core3) | Star Wars Galaxies pre-CU server emulator core | 189 | 🟢 | Lua |
| [Maple2](https://github.com/MS2Community/Maple2) | Server emulator for MapleStory 2 | 188 | 🟢 | C# |
| [Classic-Brawl](https://github.com/PhoenixFire6934/Classic-Brawl) | Python Brawl Stars server emulator for v26 | 186 | 🟡 | Python |
| [LawinServer](https://github.com/Lawin0129/LawinServer) | Local single-user Fortnite backend server emulator | 186 | 🟢 | JavaScript |
| [rsmod](https://github.com/rsmod/rsmod) | Old School RuneScape game server emulator | 181 | 🟡 | Kotlin |
| [AGS-GC](https://github.com/Anime-Game-Servers/AGS-GC) | A server software implementation, ineroperable with a certain anime game client. The code in this repository is fully... | 176 | 🟢 | Java |
| [aion-server](https://github.com/beyond-aion/aion-server) | Aion server emulator | 173 | 🟢 | Java |
| [cuwo](https://github.com/matpow2/cuwo) | Open server and utilities for Cube World | 173 | 🔴 | C |
| [topaz](https://github.com/project-topaz/topaz) | Final Fantasy XI server emulator | 164 | 🗄️ | Lua |
| [OregonCore](https://github.com/OregonCore/OregonCore) | World of Warcraft 2.4.3 server emulator | 162 | 🔴 | C++ |
| [LawinServerV2](https://github.com/Lawin0129/LawinServerV2) | Fortnite backend emulator with matchmaking and XMPP support | 159 | 🟡 | JavaScript |
| [VanillaReimplementation](https://github.com/Minestom/VanillaReimplementation) | Reimplementation of vanilla Minecraft features on Minestom | 159 | 🗄️ | Java |
| [L2dotNET](https://github.com/Elfocrash/L2dotNET) | Lineage II Interlude server emulator in C# | 157 | 🔴 | C# |
| [UniSpyServer](https://github.com/GameProgressive/UniSpyServer) | Open-source GameSpy backend emulator | 155 | 🟢 | Python |
| [desse](https://github.com/ymgve/desse) | Demon's Souls private server emulator | 152 | 🔴 | Python |
| [Dawnshard](https://github.com/SapiensAnatis/Dawnshard) | Server emulator for Dragalia Lost | 151 | 🟢 | C# |
| [MuEmu](https://github.com/Yomalex/MuEmu) | C# MU Online server supporting multiple client versions | 148 | 🟢 | C# |
| [POL](https://github.com/polserver/polserver) | PenUltima Online server compatible with most Ultima Online clients | 147 | 🟢 | C++ |
| [Dawn of Light](https://github.com/Dawn-of-Light/DOLSharp) | Dark Age of Camelot server emulator | 137 | 🟢 | C# |
| [server](https://github.com/sp-tarkov/server) | The Server project for SPT | 134 | 🗄️ | TypeScript |
| [Nebula](https://github.com/Melledy/Nebula) | A server emulator for the game Stella Sora | 130 | 🟢 | Java |
| [Kawari](https://github.com/redstrate/Kawari) | Unofficial Final Fantasy XIV server emulator for 7.x | 127 | 🗄️ | Rust |
| [WiiLink WFC Server](https://github.com/WiiLink24/wfc-server) | Nintendo Wi-Fi Connection replacement server by WiiLink | 125 | 🟢 | Go |
| [belfast](https://github.com/ggmolly/belfast) | Reimplementation of a server for Azur Lane | 117 | 🗄️ | Go |
| [Edelstein](https://github.com/Kaioru/Edelstein) | MapleStory v95 server emulator in C# | 114 | 🟢 | C# |
| [SeventhUmbral](https://github.com/jpd002/SeventhUmbral) | Final Fantasy XIV v1.23b server emulator | 112 | 🔴 | C |
| [zombie-cafe-revival](https://github.com/Airyzz/zombie-cafe-revival) | Reverse engineering and reviving the mobile game Zombie Cafe | 111 | 🟡 | Smali |
| [BaPs](https://github.com/gucooing/BaPs) | BaPs | 109 | 🗄️ | Go |
| [Pretendo account server](https://github.com/PretendoNetwork/account) | Replacement Nintendo Network account server for Wii U and 3DS | 108 | 🟢 | TypeScript |
| [quantum-core-x](https://github.com/MeikelLP/quantum-core-x) | Metin2 open source server emulator in C# | 107 | 🟢 | C# |
| [Cypress](https://github.com/PvZ-Cypress/Cypress) | Dedicated servers for Plants vs. Zombies: Garden Warfare 1, 2 and Battle for Neighborville | 106 | 🟢 | C++ |
| [EVESharp](https://github.com/Almamu/EVESharp) | EVE Online server emulator in C# | 104 | 🟡 | C# |
| [Orpheus](https://github.com/aatxe/Orpheus) | Open source MapleStory v83 server emulator | 104 | 🗄️ | Java |
| [kinoko](https://github.com/iw2d/kinoko) | MapleStory v95 server emulator | 101 | 🟢 | Java |
| [butterfly](https://github.com/skogaby/butterfly) | e-amusement server emulator for Dance Dance Revolution A | 99 | 🔴 | Java |
| [Prospect](https://github.com/AeonLucid/Prospect) | Server emulation for The Cycle: Frontier | 98 | 🟡 | C# |
| [Pirates-Online-Rewritten](https://github.com/PiratesOnlineRewritten/Pirates-Online-Rewritten) | Revival of Disney's Pirates of the Caribbean Online with a rewritten server | 96 | 🔴 | Python |
| [RestoRoom](https://github.com/RestoRoom/RestoRoom) | Community reimplementation of the Rec Room servers | 95 | 🟢 |  |
| [soapbox-race-core](https://github.com/SoapboxRaceWorld/soapbox-race-core) | Need for Speed: World server emulator core | 90 | 🔴 | Java |
| [AscNet](https://github.com/rafi1212122/AscNet) | Punishing: Gray Raven private server! | 89 | 🟢 | C# |
| [_archive_lineage2js](https://github.com/space2pacman-misc/_archive_lineage2js) | Node.js Lineage 2 server emulator (Chronicle 1) | 88 | 🗄️ | JavaScript |
| [server-csharp](https://github.com/sp-tarkov/server-csharp) | A C# rewrite of the SPT server project. | 85 | 🗄️ | C# |
| [SphereServer Source-X](https://github.com/Sphereserver/Source-X) | Ultima Online server emulator | 85 | 🟢 | C |
| [oxide](https://github.com/T-x-T/oxide) | Reimplementation of the Minecraft server in pure Rust | 79 | 🟢 | Rust |
| [NetspherePirates](https://github.com/wtfblub/NetspherePirates) | Experimental S4 League server emulator | 78 | 🗄️ | C# |
| [UOX3](https://github.com/UOX3DevTeam/UOX3) | Ultima Offline eXperiment 3 Ultima Online server emulator | 75 | 🟢 | C++ |
| [Juxtaposition](https://github.com/PretendoNetwork/juxtaposition) | Pretendo's Miiverse replacement service for Wii U and 3DS | 73 | 🟢 | TypeScript |
| [DBOGLOBAL](https://github.com/dboglobal/DBOGLOBAL) | Dragon Ball Online Global client and server emulator | 71 | 🟡 | C++ |
| [Hitman-5-Server](https://github.com/LennardF1989/Hitman-5-Server) | Emulated server for Hitman: Absolution and Hitman: Sniper Challenge | 71 | 🗄️ | HTML |
| [Bayshore](https://github.com/ProjectAsakura/Bayshore) | Server reimplementation for Wangan Midnight Maximum Tune 6 | 69 | 🟢 | TypeScript |
| [OpenDAoC](https://github.com/OpenDAoC/OpenDAoC-Core) | Free Dark Age of Camelot server emulator | 69 | 🟢 | C# |
| [BlueRebirth](https://github.com/LunarConcerto/BlueRebirth) | Offline restoration project for a discontinued mobile game | 67 | 🟢 | C# |
| [mxoemu](https://github.com/rajkosto/mxoemu) | Server emulator for the shut-down MMO The Matrix Online | 64 | 🔴 | C |
| [af-emulator](https://github.com/armangido/af-emulator) | Assault Fire PH preservation and server emulation project | 63 | 🟢 | Python |
| [cwk-server](https://github.com/shishkabob27/cwk-server) | Reverse engineered server for Card Wars Kingdom | 60 | 🗄️ | Python |
| [Freya](https://github.com/ubis/Freya) | Cabal Online server emulator | 60 | 🟡 | Go |
| [titanic](https://github.com/osuTitanic/titanic) | A private server that supports all osu! clients (2007-2026) | 60 | 🟢 | Go |
| [DragonFable-Private-Server](https://github.com/hiperesp/DragonFable-Private-Server) | DragonFable private server emulator for the current client | 59 | 🟢 | PHP |
| [puniemu](https://github.com/SuperTavor/puniemu) | Server emulator for Yo-kai Watch Puni Puni | 59 | 🟢 | C# |
| [perlica-rs](https://github.com/Yoshk4e/perlica-rs) | A server software reimplementation for an old version of a certain anime game about factories. | 58 | 🟢 | Rust |
| [OpenRS2](https://github.com/openrs2/openrs2) | Open-source multiplayer game server compatible with the RuneScape client | 56 | 🟢 | Kotlin |
| [NFS-Online-Server](https://github.com/moio9/NFS-Online-Server) | Online server emulator for NFS Most Wanted, Underground 2 and Carbon | 55 | 🟢 | Python |
| [topaz](https://github.com/topaz-next/topaz) | Server emulator for Final Fantasy XI | 55 | 🗄️ | Lua |
| [dream-server](https://github.com/NDSLink/dream-server) | Server for Pokemon Dream World | 54 | 🟡 | SCSS |
| [Maelstrom](https://github.com/Rawaho/Maelstrom) | Server emulator for Final Fantasy XIV (Stormblood 4.10) | 54 | 🔴 | C# |
| [Hardline Dreams](https://github.com/hdneo/mxo-hd) | C# server emulator for The Matrix Online | 53 | 🟢 | C# |
| [Infantry-Online-Server](https://github.com/InfantryOnline/Infantry-Online-Server) | Free Infantry Online server emulator | 53 | 🟢 | C# |
| [Holocore](https://github.com/ProjectSWGCore/Holocore) | Star Wars Galaxies server emulator for the JVM | 52 | 🟢 | Kotlin |
| [remielle](https://github.com/thexeondev/remielle) | Zenless Zone Zero server emulator focused on efficiency, stability and correctness. | 52 | 🟢 | Zig |
| [wrath-rs](https://github.com/Victov/wrath-rs) | A very functionally incomplete World of Warcraft: Wrath of the Lich King server emulator written in pure rust. | 52 | 🟢 | Rust |
| [Maple2](https://github.com/kOchirasu/Maple2) | Server emulator for MapleStory 2 | 51 | 🟡 | C# |
| [Modern-Brawl](https://github.com/PhoenixFire6934/Modern-Brawl) | Python Brawl Stars server emulator for version 28.189 | 51 | 🔴 | Python |
| [Sunrise](https://github.com/SunriseCommunity/Sunrise) | 🌅 Sunrise - osu! server written in C# | 50 | 🟢 | C# |
| [tpp-server-emulator](https://github.com/alicealys/tpp-server-emulator) | Reimplementation of the Metal Gear Solid V: The Phantom Pain backend server | 50 | 🟢 | C++ |
| [BetrockPlusPlus](https://github.com/OfficialPixelBrush/BetrockPlusPlus) | Minecraft Beta 1.7.3 compatible server written in C++ | 49 | 🟢 | C++ |
| [NTRSimulator](https://github.com/raphaeIl/NTRSimulator) | Server Emulator for a certain NTR game | 48 | 🟢 | C# |
| [waygate-server](https://github.com/vswarte/waygate-server) | Elden Ring custom matchmaking server implementation | 47 | 🟢 | Rust |
| [XboxLive.Server](https://github.com/zzVertigo/XboxLive.Server) | Revival server for Xbox Live 1.0 | 44 | 🗄️ | C# |
| [protanki-server](https://github.com/Assasans/protanki-server) | Open-source reimplementation of the ProTanki server | 43 | 🗄️ | Kotlin |
| [SporeServer](https://github.com/Rosalie241/SporeServer) | A WIP Spore Server Replacement | 41 | 🟡 | C# |
| [shiro](https://github.com/mellowagain/shiro) | High-performance osu! Bancho server re-implementation in C++ | 40 | 🗄️ | C++ |
| [azerust](https://github.com/arlyon/azerust) | An experimental World of Warcraft emulator in Rust | 39 | 🟡 | Rust |
| [g0v0-server](https://github.com/GooGuTeam/g0v0-server) | An osu!(lazer) private server that is easy to deploy, highly scalable, and fully featured to meet diverse operational... | 39 | 🟢 | Python |
| [Pocket Relay](https://github.com/PocketRelay/Server) | Mass Effect 3 EA Blaze server emulator for LAN and WAN play | 39 | 🟢 | Rust |
| [LuxonServer](https://github.com/niansa/LuxonServer) | Clean-room reimplementation of the Photon LoadBalancing server | 38 | 🟢 | C |
| [OpenBachelorS](https://github.com/pfyy/OpenBachelorS) | OpenBachelorS | 38 | 🟢 | Python |
| [PTCGP-Private-Server](https://github.com/Layen-lang/PTCGP-Private-Server) | Unofficial local compatibility server and profile editor for Pokémon TCG Pocket | 37 | 🟢 | Go |
| [2006rebotted](https://github.com/dginovker/2006rebotted) | A 2006 RuneScape 2 Emulation Server. | 36 | 🔴 | Java |
| [Hoshimi](https://github.com/Enigfrank/Hoshimi) | Unofficial local game emulation server for Hoshimi | 35 | 🟢 | PowerShell |
| [LibreKO](https://github.com/ZeusAFK/LibreKO) | From-scratch reimplementation of the Knight Online game server and client | 33 | 🟢 | C# |
| [EVEmu](https://github.com/evemuproject/evemu_crucible) | EVE Online server emulator for the Crucible client | 32 | 🔴 | C++ |
| [OpenPayload](https://github.com/CLF78/OpenPayload) | Open-source reimplementation of the Wiimmfi payload for Mario Kart Wii | 29 | 🟡 | C++ |
| [sonetto-rs](https://github.com/Yoshk4e/sonetto-rs) | a server software re-implementaion for R1999 | 29 | 🗄️ | Rust |
| [DoctoratePy](https://github.com/nonobject14514/DoctoratePy) | DoctoratePy | 26 | 🔴 | Python |
| [Batla-3D-server-emu](https://github.com/Serega25511s/Batla-3D-server-emu) | Clean-room server emulator for the shut-down arena shooter Batla 3D | 25 | 🟢 | C# |
| [Orchis](https://github.com/CerisWhite/Orchis) | A Dragalia Lost Private Server | 25 | 🟢 | JavaScript |
| [wow_vanilla_server](https://github.com/gtker/wow_vanilla_server) | WIP Rust server for WoW 1.12 | 23 | 🟡 | Rust |
| [OT6-Reconstruction](https://github.com/ApfelTeeSaft/OT6-Reconstruction) | Decompilation of Fortnite Alpha (2016) game server logic | 21 | 🟢 | C++ |
| [mooege](https://github.com/mooege/mooege) | Educational Diablo III game server emulator | 20 | 🔴 |  |
| [enigma](https://github.com/yoncodes/enigma) | server for that one card game | 19 | 🟢 | Rust |
| [KazusaGI_cb2](https://github.com/Hiro420/KazusaGI_cb2) | Server sofware reimplementation for an old version of a certain anime game | 18 | 🟢 | C# |
| [Lolo](https://github.com/BanterSR/Lolo) | 开放空间/OverField 服务端部分实现 | 18 | 🟢 | JavaScript |
| [spikewall](https://github.com/Ramen2X/spikewall) | An open source server for the defunct 2015 mobile game Sonic Runners. | 17 | 🟢 | C# |
| [assettocorsa_competizione_server](https://github.com/renaudallard/assettocorsa_competizione_server) | Assetto Corsa Competizione server | 16 | 🟢 | C |
| [Z7](https://github.com/Khysnik/Z7) | Reverse-engineered Blaze server for Plants vs Zombies: Garden Warfare 2 | 15 | 🟢 | C++ |
| [of-ps](https://github.com/byzp/of-ps) | overfield emu server | 12 | 🟢 | Python |
| [OpenLethe](https://github.com/LEAGUE-OF-NINE/OpenLethe) | OpenLethe | 10 | 🟢 | C# |
| [hk4e-go](https://github.com/Kei-Luna/hk4e-go) | 世҉̰̗͕́͢͡界҈̧̟͙̖̎̎̕遗҈͚̄̓̍̕͜忘҈̢͕̙̪̄͞我҉̛̰̯̊͢ | 9 | 🟡 | Go |
| [KazusaHSR_0.56](https://github.com/Hiro420/KazusaHSR_0.56) | Open-source server reimplementation for an early version of an anime game with stars and rails | 8 | 🟢 | C# |
| [ew](https://github.com/ethanaobrien/ew) | A sif2 server | 7 | 🟢 | Rust |
| [garcia](https://github.com/yoncodes/garcia) | server for a random 2d game | 2 | 🟢 | Rust |
| [dev_wow_auth_server](https://github.com/gtker/dev_wow_auth_server) | World of Warcraft authentication server for development | 1 | 🟡 | Rust |
| [2009scape](https://gitlab.com/2009scape/2009scape) | Open-source 2009-era RuneScape server remake |  | ⚪ |  |
| [ACEmulator](https://emulator.ac) | A custom, completely from-scratch open source server emulator for Asheron’s Call built on C#. |  | ⚪ |  |

## Static Recompilations & PC Ports

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [N64Recomp](https://github.com/N64Recomp/N64Recomp) | Static recompiler that turns N64 binaries into portable C code | 8,232 | 🟢 | C++ |
| [XenonRecomp](https://github.com/hedge-dev/XenonRecomp) | Converts Xbox 360 PowerPC executables into C++ for recompilation on modern platforms | 6,540 | 🟡 | C++ |
| [dusk](https://github.com/TwilitRealm/dusklight) | Twilight Princess PC port based on the zeldaret tp decompilation | 5,792 | 🟢 | C++ |
| [gen1recomp](https://github.com/bryanthaboi/gen1recomp) | Native recompilation of Pokemon Red/Blue/Yellow with mods | 3,912 | 🟢 | Lua |
| [SpaghettiKart](https://github.com/HarbourMasters/SpaghettiKart) | Mario Kart 64 PC port based on the mk64 decompilation, with track editor | 2,403 | 🟢 | C |
| [BloodBorne for Windows](https://github.com/Supermedo/bloodborne_pc) | Recomp of BloodBorne (PS4) to Windows. | 2,302 | 🟢 | C++ |
| [Starship](https://github.com/HarbourMasters/Starship) | Star Fox 64 PC port based on the sf64 decompilation | 2,089 | 🟢 | C |
| [BanjoRecomp](https://github.com/BanjoRecomp/BanjoRecomp) | Banjo-Kazooie static recompilation with mod support | 2,035 | 🟢 | C |
| [sm64ex](https://github.com/sm64pc/sm64ex) | Super Mario 64 PC port fork focused on easier modding | 1,861 | 🟡 | C |
| [N64RecompLauncher](https://github.com/SirDiabo/GithubLauncher) | Installs and updates N64 static recompilation ports in one place | 1,779 | 🟢 | C# |
| [P.T. for PC](https://github.com/LoreanXavier/pt-pc) | Native PC port of Kojima's P.T. with game logic rebuilt in C++, runs from your own PS4 files | 1,620 | 🟢 | C++ |
| [rt64](https://github.com/rt64/rt64) | N64 graphics renderer used by emulators and native recomp ports | 1,613 | 🟢 | C++ |
| [skate3recomp](https://github.com/mchughalex/skate3recomp) | Native Windows/Linux/macOS port of Skate 3 via static recompilation | 1,588 | 🟢 | C++ |
| [ACGC-PC-Port](https://github.com/flyngmt/ACGC-PC-Port) | Animal Crossing (GameCube) PC port from the ac-decomp decompilation | 1,483 | 🟢 | C |
| [OpenCE](https://github.com/OpenCommunityEdition/OpenCE) | Enhanced recomp of the original Xbox Halo: Combat Evolved to all Windows, Linux and Android. | 1,450 | 🟢 | C |
| [sm64coopdx](https://github.com/coop-deluxe/sm64coopdx) | Online multiplayer Super Mario 64 PC port based on the decompilation | 1,424 | 🟢 | C |
| [isle-portable](https://github.com/isledecomp/isle-portable) | Portable LEGO Island source port built from the isle decompilation | 1,065 | 🟢 | C++ |
| [ReXGlue SDK](https://github.com/rexglue/rexglue-sdk) | SDK for static recompilation of Xbox 360 games from PowerPC to portable C++ | 1,047 | 🟢 | C |
| [WipEout Phantom Edition](https://github.com/wipeout-phantom-edition/wipeout-phantom-edition) | WipEout PC port that runs from the original disc image | 972 | 🟡 |  |
| [devilution-nx](https://github.com/lantus/devilution-nx) | Diablo port for Nintendo Switch based on Devilution | 890 | 🔴 | C++ |
| [GoldenEye-Recomp](https://github.com/SunJaycy/GoldenEye-Recomp) | Recompilation of the cancelled Xbox 360 GoldenEye 007 for PC | 888 | 🟢 | C |
| [SymphonyRecomp](https://github.com/BlackLabelHQ/SymphonyRecomp) | Static recompilation of Castlevania: Symphony of the Night | 867 | 🟢 | C# |
| [Ghostship](https://github.com/HarbourMasters/Ghostship) | Harbour Masters Super Mario 64 source port with mods and modern graphics | 819 | 🟢 | C |
| [Blue Dragon (re:Blue)](https://github.com/zolaware/reblue) | Xbox 360 static recompilation of Blue Dragon (re:Blue) | 775 | 🟢 | C++ |
| [zelda-alttp-3ds](https://github.com/EstebanPdN/zelda-alttp-3ds) | Nintendo 3DS port of Zelda: A Link to the Past based on zelda3 | 709 | 🟢 | C |
| [Silent Hill native PC port](https://github.com/SlickAmogus/silent-hill-decomp) | Multiplatform port of the Silent Hill 1 PSX decompilation | 669 | 🟢 | C |
| [Marathon Recompiled](https://github.com/sonicnext-dev/MarathonRecomp) | Static recompilation PC port of Sonic the Hedgehog (2006) | 662 | 🟢 | C++ |
| [Mario Kart 64: Recompiled](https://github.com/sonicdcer/MarioKart64Recomp) | Static recompilation of Mario Kart 64 using N64Recomp and RT64 | 610 | 🟢 | C++ |
| [ps2-web-recomp](https://github.com/snuri00/ps2-web-recomp) | PS2 games statically recompiled to WebAssembly with a native runtime to run in the browser | 579 | 🟢 | C++ |
| [ZeldaWWHDRecomp](https://github.com/ZeldaWWHDRecomp/ZeldaWWHDRecomp) | Static recompilation of The Wind Waker HD (Wii U) | 563 | 🟢 | C |
| [LostOdysseyRecomp](https://github.com/freefrank/LostOdysseyRecomp) | Experimental native PC port of Lost Odyssey using static recompilation. No game assets included. | 560 | 🟢 | C++ |
| [Ace Combat 6: Fires of Liberation](https://github.com/sal063/AC6_recomp) | Xbox 360 static recompilation of Ace Combat 6: Fires of Liberation | 511 | 🟢 | C++ |
| [Donkey Kong 64: Recompiled](https://github.com/Rainchus/Donkey-Kong-64-Recompiled) | Donkey Kong 64 static recompilation with high-framerate support | 500 | 🟢 | C |
| [Lighthouse](https://github.com/HarbourMasters/Lighthouse) | Banjo-Kazooie PC port with multiplayer, romhacks and randomizer | 492 | 🟢 | C |
| [TriAevum](https://github.com/coccofresco/TriAevum) | Native PC recompilation runtime for Ocarina of Time 3D | 480 | 🟢 | C++ |
| [BattleShip](https://github.com/JRickey/BattleShip) | AI-assisted decomp-based PC/Mac/Linux port of Super Smash Bros | 477 | 🟢 | C++ |
| [PaperBoat](https://github.com/HarbourMasters/PaperBoat) | Paper Mario source port based on the decompilation | 458 | 🟢 | C |
| [hells-gate-recomp](https://github.com/florinp93/hells-gate-recomp) | Xbox 360 to PC port of Dante's Inferno using ReXGlue (static recompilation) | 453 | 🟢 | C++ |
| [MeleePC](https://github.com/999sian/melee-pc) | Recomp of Super Smash Bros Melee to PC. | 449 | 🟢 | C |
| [pinyon-shift](https://github.com/arcanite24/pinyon-shift) | A playable preview of Forza Horizon static recompilation | 449 | 🟢 | Python |
| [gb-recompiled](https://github.com/arcanite24/gb-recompiled) | Static recompiler for Game Boy/Color ROMs to portable C with SDL2 runtime | 439 | 🟢 | Python |
| [Yakumo](https://github.com/TeamGDB/Yakumo) | Static recompilation of a PSP game into a native executable. Vulkan and SDL3. Bring your own copy of the game. | 415 | 🟢 | C++ |
| [Fable-2-Recomp](https://github.com/himdo/Fable-2-Recomp) | Fable-2-Recomp | 413 | 🟢 | C++ |
| [ps3recomp](https://github.com/sp00nznet/ps3recomp) | Static recompilation runtime libraries for PlayStation 3 titles | 404 | 🟢 | C |
| [CTR Native](https://github.com/CTR-tools/ctr-native) | Native PC port based on the Crash Team Racing decompilation | 393 | 🟢 | C |
| [Metroid Prime Port](https://github.com/Odrannnn/MetroidPrimePort) | Recomp of Metroid Prime to PC and Android. | 387 | 🟢 | C++ |
| [Star Fox 64: Recompiled](https://github.com/sonicdcer/Starfox64Recomp) | Static recompilation of Star Fox 64 for Windows/Linux | 381 | 🟢 | C |
| [Fable2Recomp](https://github.com/Fable2Recomp/Fable2Recomp) | A Fable 2 Recomp | 364 | 🟢 | C++ |
| [NocturneRecomp](https://github.com/birabittoh/NocturneRecomp) | Static recompilation of Castlevania: Symphony of the Night (XBLA) for Windows and Linux, built on the ReXGlue SDK. | 362 | 🟢 | C++ |
| [sm64rt](https://github.com/DarioSamo/sm64rt) | Super Mario 64 PC port with ray tracing | 361 | 🟡 | C |
| [BlueWake](https://github.com/chrissotraidis/bluewake) | The Wind Waker (GameCube) static recompilation | 344 | 🟢 | C |
| [TheSimpsonsGameRecomp](https://github.com/YesterMester/TheSimpsonsGameRecomp) | The Simpsons Game Xbox 360 static recompilation | 332 | 🟢 | C++ |
| [OpenTIE](https://github.com/elyosh/OpenTIE) | Open-source recomp of TIE Fighter. | 328 | 🟢 | C |
| [Dinosaur Planet: Recompiled](https://github.com/DinosaurPlanetRecomp/dino-recomp) | Static recompilation of the unreleased N64 Dinosaur Planet | 324 | 🟢 | C++ |
| [Edge Of Time Recomp](https://github.com/goliathret/EdgeOfTimeRecomp) | Recomp of Spider Man: Edge of Time from Xbox 360. | 320 | 🟢 | C++ |
| [strikers](https://github.com/new-coke/strikers) | Mario Strikers Charged native PC port / recompilation | 314 | 🟢 | C++ |
| [Goemon64Recomp](https://github.com/klorfmorf/Goemon64Recomp) | Mystical Ninja Starring Goemon static recompilation | 311 | 🟢 | C |
| [pokeemerald-wasm](https://github.com/tripplyons/pokeemerald-wasm) | Pokemon Emerald decompilation recompiled to WebAssembly for the browser | 310 | 🟢 | C |
| [BM64Recomp](https://github.com/RevoSucks/BM64Recomp) | Bomberman 64 static recompilation with mod support | 294 | 🟢 | C++ |
| [Ico-PC](https://github.com/nathanialf/ico-pc) | Recomp of ICO (PS2) to PC. | 289 | 🟢 | C |
| [G-Diffuser](https://github.com/Zorkats/G-Diffuser) | Unofficial PC port of F-Zero X based on its decompilation | 281 | 🟢 | C |
| [Quest64-Recomp](https://github.com/Rainchus/Quest64-Recomp) | Quest 64 static recompilation with mod support | 278 | 🟢 | C++ |
| [psp-web-recomp](https://github.com/snuri00/psp-web-recomp) | Static recompilation of PSP games (God of War) to WebAssembly with HLE kernel | 277 | 🟢 | C++ |
| [DownpourRecomp](https://github.com/LittleBitUA/DownpourRecomp) | Silent Hill: Downpour Xbox 360 static recompilation | 275 | 🟢 | C++ |
| [MegaMan64Recompiled](https://github.com/MegaMan64Recomp/MegaMan64Recompiled) | Mega Man 64 static recompilation with mod support | 265 | 🟢 | C++ |
| [Tenkaichi3Decomp](https://github.com/z3xox/Tenkaichi3Decomp) | PC port of Dragon Ball Z: Budokai Tenkaichi 3 built on its decompilation | 257 | 🟢 | C |
| [CBFD-Recompiled](https://github.com/sciaschi/CBFD-Recompiled) | Static recompilation of Conker's Bad Fur Day (N64) to native PC | 254 | 🟢 | C |
| [The-Darkness-Recomp](https://github.com/portingpete/The-Darkness-Recomp) | The Darkness Xbox 360 static recompilation | 247 | 🟢 | C++ |
| [ProjectCane](https://github.com/theclub654/ProjectCane) | Playable PC port of Sly Cooper and the Thievius Raccoonus rebuilt via reverse engineering | 246 | 🟢 | C++ |
| [GoldenEye PC Port](https://github.com/jkdansereau/goldeneye-pc-port) | Recomp of GoldenEye 007 (N64). | 238 | 🟢 | C |
| [DKC1Recomp](https://github.com/elliotttate/DKC1Recomp) | Static recompilation of Donkey Kong Country (SNES) with widescreen | 234 | 🟢 | C |
| [speedbreaker](https://github.com/SpeedBreakerProject/speedbreaker) | Unofficial static recompilation of the Xbox 360 version of Need for Speed: Most Wanted (2005): a native port for Stea... | 233 | 🟢 | C++ |
| [PSPRecomp](https://github.com/jessicanataliagta/PSPRecomp) | Static recompilation framework for PSP software | 223 | 🟢 | C++ |
| [Skate3-Mobile](https://github.com/Buku313/Skate3-Mobile) | Play Skate 3 natively on Android. Download one APK, select your own ISO, and skate. ARM64 recompilation with Vulkan r... | 222 | 🟢 | C++ |
| [Condemned2Recomp](https://github.com/psxrestore/Condemned2Recomp) | A static recompilation of Condemned 2: Bloodshot done with RexGlue. | 214 | 🟢 | C++ |
| [LCS Recomp](https://github.com/elmasas/lcs-recomp) | Recomp of the PSP game GTA: Liberty City Stories to PC. | 214 | 🟢 | C++ |
| [daytona-xbla-recomp](https://github.com/Subarasheese/daytona-xbla-recomp) | A static recompilation of Daytona USA (Xbox 360 / XBLA, 2011) | 212 | 🟢 | C++ |
| [GoldenRecomp](https://github.com/kholdfuzion/GoldenRecomp) | WIP Recompilation of a game about a special agent who saves the world from a traitor. | 212 | 🟢 | C++ |
| [mario-kart-64-3ds](https://github.com/EstebanPdN/mario-kart-64-3ds) | Native Nintendo 3DS port based on the Mario Kart 64 decompilation | 208 | 🟢 | C++ |
| [Viva Piñata: Trouble in Paradise](https://github.com/SolarCookies/TiP-Recomp) | Xbox 360 static recompilation of Viva Piñata: Trouble in Paradise | 207 | 🟢 | C++ |
| [SMS Launcher](https://github.com/chasem-dev/sms-launcher) | Recomp of Super Mario Sunshine. | 203 | 🟢 | JavaScript |
| [Daytona Arcade Recomp](https://github.com/alphanu1/daytona-arcade-recomp) | Recomp of Daytona Racing to PC. | 191 | 🟢 | C++ |
| [SkyRoads-Codex](https://github.com/ammaarreshi/SkyRoads-Codex) | SkyRoads DOS game reverse engineered without source using Codex | 191 | 🟢 | Rust |
| [Duke Nukem Zero Hour: Recompiled](https://github.com/sonicdcer/DNZHRecomp) | Duke Nukem: Zero Hour static recompilation with gyro aiming and high FPS | 190 | 🟢 | C++ |
| [DimensionsRecomp](https://github.com/NeverCookFirst/DimensionsRecomp) | Proof that a toys-to-life game can be recompiled. A native PC build of LEGO Dimensions, made by statically recompilin... | 187 | 🟢 | C++ |
| [Crash Team Racing: High Octane](https://github.com/Rinnegatamante/Crash-Team-Racing-High-Octane) | CTR source port for PC, PS Vita and web | 184 | 🟢 | C |
| [sega-vr-disasm](https://github.com/matiaszanolli/sega-vr-disasm) | Complete static recompilation of Virtua Racing for the Sega 32X (optimization in progress) | 182 | 🟢 | Assembly |
| [N64ModernRuntime](https://github.com/N64Recomp/N64ModernRuntime) | Runtime for traditional ports and recompilations of N64 games | 179 | 🟢 | C++ |
| [sunpad](https://github.com/chrissotraidis/sunpad) | Super Mario Sunshine on iOS, macOS and tvOS via static recompilation | 179 | 🟢 | Objective-C++ |
| [goldenballoon](https://github.com/akratch/goldenballoon) | Native and browser port of the 1997 N64 kart racer Diddy Kong Racing | 176 | 🟢 | C |
| [Perfect Dark](https://github.com/DabDavis/perfect-dark-dabs-mod) | Recomp of the N64 game Perfect Dark to PC, with enhancements. | 173 | 🟢 | C |
| [PGR4-Recomp](https://github.com/beatrixzy/PGR4-Recomp) | A Recompilation of Project Gotham Racing 4 | 172 | 🟢 | C++ |
| [ModernGekko](https://github.com/ExpansionPak/ModernGekko) | Runtime for recompilations of GameCube games | 167 | 🟢 | C++ |
| [DPRecomp](https://github.com/LittleBitUA/DPRecomp) | Deadly Premonition Xbox 360 static recompilation | 159 | 🟢 | C++ |
| [Yu-Gi-Oh! Forbidden Memories Recompiled](https://github.com/Unchiga/Yu-Gi-Oh-Forbidden-Memories-Recompiled) | Yu-Gi-Oh! Forbidden Memories PlayStation static recompilation | 159 | 🟢 | C |
| [HarvestMoon64Recomp](https://github.com/HarvestMoon64Recomp/HarvestMoon64Recomp) | PC Port of Harvest Moon 64 made using N64: Recompiled (Windows/Linux/Mac) | 158 | 🟢 | C++ |
| [RingOut](https://github.com/jackpoison-prog/RingOut) | Native PC port of a GameCube fighting game via static recompilation | 158 | 🟢 | C |
| [Banjo-Kazooie: Nuts & Bolts](https://github.com/masterspike52/reNut) | Xbox 360 static recompilation of Banjo-Kazooie: Nuts & Bolts | 153 | 🟢 | C++ |
| [doaxvb-re](https://github.com/NoRain211/doaxvb-re) | Dead or Alive Xtreme Beach Volleyball original-Xbox static recompilation | 153 | 🟢 | C |
| [Parasite Eve HD Remaster](https://github.com/faligame/Parasite-Eve-HD-Remaster) | Recomp and enhancement of the PS1 game Parasite Eve. | 153 | 🟢 |  |
| [OpenXWA](https://github.com/elyosh/OpenXWA) | Open-source recomp of X-Wing Alliance. | 152 | 🟢 | C |
| [Dr. Mario 64 Recomp Plus](https://github.com/theboy181/drmario64_recomp_plus) | Dr. Mario 64 static recompilation with 4-player support | 151 | 🟢 | C++ |
| [SCDA-XBERecomp](https://github.com/TGP482/SCDA-XBERecomp) | Unofficial PC port of Splinter Cell: Double Agent (original Xbox) via static recompilation | 151 | 🟢 | C++ |
| [King Kong: Recompiled](https://github.com/TekRantGaming/king-kong-recompiled) | Peter Jackson's King Kong Xbox 360 static recompilation | 150 | 🟢 | C++ |
| [SDOJ-Recomp](https://github.com/eandis/SDOJ-Recomp) | SDOJ-Recomp | 149 | 🟢 | C++ |
| [Initial-D-Arcade-Stage-3-Native-SH-4-Recompilation-WIP-](https://github.com/distilledorion-sketch/Initial-D-Arcade-Stage-3-Native-SH-4-Recompilation-WIP-) | Native SH-4 AOT recompilation of Initial D Arcade Stage 3 (NAOMI 2) — BIOS-free Vulkan public early demo (WIP). | 145 | 🟢 | C++ |
| [F-15 II](https://github.com/neuviemeporte/f15se2-re) | Recomp of MicroProse F-15 II. | 144 | 🟢 | C |
| [YuGiOhForbiddenMemoriesRecomp](https://github.com/Unchiga/YuGiOhForbiddenMemoriesRecomp) | Static recompilation of Yu-Gi-Oh! Forbidden Memories (PS1) into a native executable - with a live duel-rank meter, a... | 133 | 🟢 | C |
| [Xbox360-Native-Ports](https://github.com/CrownParkComputing/Xbox360-Native-Ports) | Xbox 360 titles recompiled to native Linux with Vulkan renderer; launchers only | 130 | 🟢 | C++ |
| [DBZ1](https://github.com/WistfulHopes/DBZ1) | Dragon Ball Z Budokai HD Recompiled | 128 | 🟢 | C++ |
| [BMHeroRecomp](https://github.com/RevoSucks/BMHeroRecomp) | Bomberman Hero static recompilation with mod support | 125 | 🟢 | C++ |
| [sms-pc-port](https://github.com/chasem-dev/sms-pc-port) | Native PC port of Super Mario Sunshine | 125 | 🟢 | C++ |
| [snesrecomp](https://github.com/RetroPortingToolKit/snesrecomp) | Super Nintendo static recompiler ecosystem | 125 | 🟢 | C |
| [Flame](https://github.com/DiaLight/Flame) | Dungeon Keeper II partial recompilation with bug fixes. | 123 | 🟢 | C++ |
| [DKC3Recomp](https://github.com/elliotttate/DKC3Recomp) | Native recompilation of Donkey Kong Country 3 (SNES) | 120 | 🟢 | C |
| [MKW-3DS](https://github.com/MiniBandit/MKW-3DS) | Native Nintendo 3DS port of Mario Kart Wii, built from your own disc | 119 | 🟢 | C++ |
| [RaceWave46](https://github.com/DomazinUS/RaceWave46) | AI-assisted Wave Race 64 recompilation for Windows | 118 | 🟢 | C++ |
| [AloneInTheDarkReHaunted](https://github.com/spacefarergames/AloneInTheDarkReHaunted) | A heavily enhanced port and dynamic recomp of Alone In The Dark 1, with Textured Models, HD-4K background replacement... | 117 | 🟢 | C++ |
| [projectreach](https://github.com/chrissotraidis/projectreach) | Halo: Combat Evolved on iPhone, iPad and Mac. The Xbox edition with online matches of up to 128 players and the origi... | 117 | 🟢 | C |
| [NFSMW-Recompiled](https://github.com/madelrandel-blip/NFSMW-Recompiled) | Static native recompilation of Need for Speed: Most Wanted (Xbox 360) | 112 | 🟢 | C++ |
| [ValkyrieRecomp](https://github.com/Ed1z19/ValkyrieRecomp) | Native PC recompilation of Valkyrie Profile (PS1) | 111 | 🟢 | Python |
| [Mercenaries-Recompiled](https://github.com/KraftMacAndChee/Mercenaries-Recompiled) | Recompilation of Mercenaries: Playground of Destruction | 110 | 🟢 | C |
| [beanRecomp](https://github.com/Fable2Recomp/beanRecomp) | A static Recomp of 007 Goldeneye Remaster XBLA | 109 | 🟡 | C++ |
| [OpenXW](https://github.com/elyosh/OpenXW) | Open-source recomp of X-Wing. | 109 | 🟢 | C |
| [SuperMarioWorldRecomp](https://github.com/mstan/SuperMarioWorldRecomp) | Super Mario World recompiled using snesrecomp | 109 | 🟢 | C |
| [skate3-ios-setup](https://github.com/andrewnakas/skate3-ios-setup) | Builds the Skate 3 recompilation for iOS from your own disc image | 108 | 🟢 | Shell |
| [snowboardkids2-recomp](https://github.com/cdlewis/snowboardkids2-recomp) | Snowboard Kids 2 static recompilation with mod support | 106 | 🟢 | C |
| [melee-unlocked](https://github.com/Hero88go/melee-unlocked) | Native Windows source port of Super Smash Bros. Melee built from its decompiled C source | 105 | 🟢 | C++ |
| [Crash Team Racing: Turbocharged](https://github.com/CameronRedmore/Crash-Team-Racing-Turbocharged) | CTR PC source port with native 3D renderer and high frame rates | 104 | 🟢 | C |
| [SwitchWakerHD](https://github.com/centollOS/SwitchWakerHD) | Wind Waker HD (Wii U) static recompilation for Nintendo Switch, deko3d renderer. Requires your own game dump. | 103 | 🟢 | C |
| [Phase Distorter](https://github.com/TheRunaway5/Phase-Distorter) | Native C++20 PC port of EarthBound / Mother 2 for Linux and Windows | 102 | 🟢 | C++ |
| [psxrecomp-ports](https://github.com/alexbeavs-ps1-ports/psxrecomp-ports) | Unofficial noncommercial PlayStation recompilation releases | 102 | 🟢 | PowerShell |
| [silent-hill-pc-nightly](https://github.com/SlickAmogus/silent-hill-pc-nightly) | Nightly builds of a Silent Hill 1 PC port based on the PSX decompilation | 101 | 🟢 |  |
| [Snap64Recomp](https://github.com/JackandBeans/Snap64Recomp) | Pokémon Snap static recompilation | 101 | 🟢 | C++ |
| [SSSV_Recomp](https://github.com/Cellenseres/SSSV_Recomp) | Space Station Silicon Valley static recompilation | 100 | 🟢 | C++ |
| [CoD3Recomp](https://github.com/FrankHUN88453/CoD3Recomp) | Static recompilation of Call of Duty 3 (Xbox 360) with host runtime and tools | 92 | 🟢 | C++ |
| [UFO50AndroidUnofficial](https://github.com/Skyline969/UFO50AndroidUnofficial) | Tool to build your own Android version of UFO 50 | 90 | 🟡 | Shell |
| [Roller](https://github.com/FatalDecomp/ROLLER) | Recomp of the game Whiplash/Fatal Racing. Adds enhancements. Playable on PC or online. | 88 | 🟢 | C |
| [3dpinball-nds](https://github.com/headshot2017/3dpinball-nds) | Nintendo DS port of the Space Cadet Pinball decompilation | 86 | 🟡 | C++ |
| [Crash2Recomp](https://github.com/Zumbo06/Crash2Recomp) | Crash Bandicoot 2 (PS1) translated to native code instead of emulated | 86 | 🟢 | Python |
| [driftdroid](https://github.com/dorPXP/driftdroid) | A native Android port of Mario Kart Wii and Retro Rewind. Fast, easy. | 84 | 🟢 | C++ |
| [goldeneye-metal](https://github.com/ysrdevs/goldeneye-metal) | Experimental source-only static recompilation of GoldenEye 007 | 84 | 🟢 | C |
| [banjo-tooie-scurvy-dog-port](https://github.com/some-scurvy-dog/banjo-tooie-scurvy-dog-port) | Banjo-Tooie Recompiled: a native Windows PC port with widescreen, resolution and FPS options, controller support, and... | 83 | 🟢 | C++ |
| [Ace-Combat-5-Static-recompilation](https://github.com/sal063/Ace-Combat-5-Static-recompilation) | Static recompilation of Ace Combat 5 with native rendering | 79 | 🟢 | C |
| [ConkerBFDReloaded](https://github.com/DahSidiAbdallah/ConkerBFDReloaded) | Conker's Bad Fur Day running natively on PC: an N64 recompilation with a Classic mode true to the N64 and a Modern mo... | 79 | 🟢 | C++ |
| [SARecomp](https://github.com/sonicfreak1337/SARecomp) | A fully playable, work-in-progress native Sonic Adventure port for Windows, Linux and Steam Deck. Powered by KatanaRe... | 78 | 🟢 | C++ |
| [Wave Race 64 Recomp](https://github.com/danielgomesvieira2000/wave-race-64-recomp) | Native PC port of Wave Race 64 via N64 static recompilation | 78 | 🟢 | C++ |
| [Theft4](https://github.com/KoreanSeats1/Theft4) | Experimental static AOT recompilation of GTA IV's Xbox 360 build for ARM | 77 | 🟢 | C++ |
| [Ace-Combat-X-Recompilation](https://github.com/sal063/Ace-Combat-X-Recompilation) | Static recompilation of ACE COMBAT X with a native renderer | 75 | 🟢 | C |
| [Ogre Battle 64 Recompiled](https://github.com/lfarroco/ogre-battle-64-recomp) | Static recompilation of Ogre Battle 64 to native PC | 75 | 🟢 | Assembly |
| [nfs-most-wanted-mac](https://github.com/elforeign/nfs-most-wanted-mac) | Need for Speed: Most Wanted native on Apple Silicon via static recompilation | 74 | 🟢 | C++ |
| [Pilotwings 64 Recomp](https://github.com/danielgomesvieira2000/pilotwings-64-recomp) | Native PC port of Pilotwings 64 statically recompiled with N64Recomp, widescreen and high FPS | 74 | 🟢 | C++ |
| [Ultima 7 Decomp](https://github.com/Kitrinx/Ultima7_Decomp) | Recomp of Ultima 7. Bit exact to original. | 74 | 🟢 | C |
| [Dead Rising 2: Case Zero Recomp](https://github.com/wivi514/Dead_Rising_2_Case_Zero_Xenon_Recomp) | Dead Rising 2: Case Zero Xbox 360 static recompilation | 73 | 🟢 | C++ |
| [GalaxyQuest](https://github.com/bigmak94/GalaxyQuest) | Super Mario Galaxy native VR port for Meta Quest 3 | 73 | 🟢 | C++ |
| [fifa-street-pc-port](https://github.com/samuelit0davila/fifa-street-pc-port) | Experimental Windows PC port of FIFA Street (2012, Xbox 360) built with ReXGlue | 72 | 🟢 | C# |
| [Rayman3Readvanced](https://github.com/RayCarrot/Rayman3Readvanced) | PC port of Rayman 3 GBA | 72 | 🟢 | C# |
| [Free-Riders-Recompiled](https://github.com/YuutaTsubasa/Free-Riders-Recompiled) | Unofficial static recompilation of Sonic Free Riders for Windows, Linux and Android, with controller/keyboard support... | 71 | 🟢 | C++ |
| [nfsu2-recompiled](https://github.com/codepdbh/nfsu2-recompiled) | Static recompilation of Need for Speed Underground 2 (PC) | 71 | 🟢 | C++ |
| [oracles-decomp](https://github.com/kirby-letsgo/oracles-decomp) | Native app for the Game Boy Color Zelda Oracle games | 71 | 🟢 | C |
| [RidgeRacer6-Recompilation](https://github.com/Sirhalo23/RidgeRacer6-Recompilation) | Recompilation of Ridge Racer 6 (Xbox 360) for PC | 71 | 🟢 | C++ |
| [BT3-Recomp](https://github.com/z3xox/BT3-Recomp) | Dragon Ball Z: Budokai Tenkaichi 3 PC port via static recompilation | 70 | 🟢 | C++ |
| [MarioKartSuperCircuitRecomp](https://github.com/mstan/MarioKartSuperCircuitRecomp) | Static recompilation of Mario Kart: Super Circuit | 67 | 🟢 | PowerShell |
| [mw2-recompiled](https://github.com/PaulCombal/mw2-recompiled) | Call of Duty: Modern Warfare 2 (2009) for Xbox 360 recompiled for Windows & Linux | 67 | 🟢 | C++ |
| [ArmyOfTwoRecomp](https://github.com/nikolaygorb/ArmyOfTwoRecomp) | Army of Two (Army of 2) 2008 [Xbox360] game static recompilation project based on RexGlue-SDK | 65 | 🟢 | C++ |
| [foxhollow](https://github.com/JackPriceBurns/foxhollow) | Star Fox Adventures decompilation powering the FoxHollow native PC port | 64 | 🟢 | C |
| [khdays-port](https://github.com/Yokimitsuro/khdays-port) | Experimental native PC runtime for Kingdom Hearts 358/2 Days | 64 | 🟢 | C++ |
| [lost-odyssey-hd-remaster](https://github.com/faligame/lost-odyssey-hd-remaster) | Lost Odyssey HD Remaster: a native PC build of Lost Odyssey (Xbox 360) via static recompilation. 720p to 4K with an e... | 64 | 🟢 | C |
| [OpenCrossing-Anbernic](https://github.com/TechProGabe/OpenCrossing-Anbernic) | Animal Crossing running natively on Anbernic handhelds | 63 | 🟢 | C |
| [smash64r](https://github.com/zestydevy/smash64r) | Static recompilation of Super Smash Bros. for PC (Windows/Linux) | 63 | 🟡 | C++ |
| [beetle-adventure-racing-recomp](https://github.com/danielgomesvieira2000/beetle-adventure-racing-recomp) | Static recompilation port of Beetle Adventure Racing (N64) to native PC, with widescreen, high-FPS and modern input | 62 | 🟢 | C++ |
| [dusklight](https://github.com/HayatoG/dusklight) | Switch port of the Twilight Princess decompilation | 62 | 🟢 | C++ |
| [halo-ce-vita](https://github.com/BirchWoodGod/halo-ce-vita) | PS Vita port of Halo: Combat Evolved built on the decompilation | 62 | 🟢 | C |
| [sk82-recomp](https://github.com/Skate-2-Team/sk82-recomp) | A static recompilation of Skate 2 to build a PC port. | 61 | 🗄️ | C++ |
| [BloodyRoar2Recomp](https://github.com/novapowers0/BloodyRoar2Recomp) | Bloody Roar II PlayStation static recompilation | 60 | 🟢 | C |
| [Chameleon Twist: Recompiled](https://github.com/Rainchus/ChameleonTwist1-JP-Recomp) | Chameleon Twist static recompilation | 60 | 🟡 | C++ |
| [RoadRash64Recompiled](https://github.com/linkssy2/RoadRash64Recompiled) | Unofficial PC recompilation of Road Rash 64 | 60 | 🟢 | C++ |
| [wwe13-recomp](https://github.com/PromethenDev/wwe13-recomp) | Static recompilation of WWE '13 (Xbox 360) for Windows and Linux via ReXGlue | 60 | 🟢 | C++ |
| [Earthworm Jim HD: Recompiled](https://github.com/TekRantGaming/earthworm-jim-hd-recompiled) | Earthworm Jim HD (XBLA) static recompilation | 59 | 🟢 | C++ |
| [SMB-Vanilla](https://github.com/nukep/SMB-Vanilla) | C decompilation and port of NES Super Mario Bros and The Lost Levels | 59 | 🟢 | C |
| [wwe-svr2011-pc](https://github.com/KaikoClanworth1/wwe-svr2011-pc) | Unofficial native PC port of WWE SmackDown vs. Raw 2011 (Xbox 360). Bring your own disc. | 59 | 🟢 | C++ |
| [KameoRePowered](https://github.com/birabittoh/KameoRePowered) | Static recompilation of Kameo: Elements of Power (Xbox 360) for Windows and Linux | 57 | 🟢 | Python |
| [mk8-recomp](https://github.com/dougchansan/mk8-recomp) | Static recompilation of Mario Kart 8 AArch64 code to native x86-64 | 57 | 🟢 | C++ |
| [mkwii-ps5](https://github.com/Phi1ow/mkwii-ps5) | Mario Kart Wii PAL on PS5 via native static recompilation | 56 | 🟢 | C++ |
| [iPodClickWheelRecomps](https://github.com/DogParty/iPodClickWheelRecomps) | An assortment of iPod Classic games that have been recompiled to run on modern systems | 55 | 🟢 | Rust |
| [NaughtyBear_ReStuff](https://github.com/MaxDeadBear/NaughtyBear_ReStuff) | NaughtyBear_ReStuff | 55 | 🟢 | C++ |
| [OpenPhantom](https://github.com/OpenPhantom/OpenPhantom) | Star Wars Episode I: The Phantom Menace (1999) PC modernized with online co-op multiplayer for up to 4 players. Play... | 55 | 🟢 | C |
| [TWIPE_00Sheven](https://github.com/riseio/TWIPE_00Sheven) | Static recompilation of the N64 game The World Is Not Enough | 55 | 🟢 | C++ |
| [Estacado-The-Darkness-Recomp](https://github.com/invinceble55-wq/Estacado-The-Darkness-Recomp) | Estacado: a native PC recompilation of The Darkness (Xbox 360). Unofficial fan port; bring your own copy of the game. | 54 | 🟢 | C++ |
| [Project-2099](https://github.com/GenryTheFox0/Project-2099) | Spider-Man: Edge of Time Xbox 360 static recompilation | 54 | 🟢 | C# |
| [xenogears-recomp](https://github.com/OpokXeno/xenogears-recomp) | Static recompilation of Xenogears for PC | 54 | 🟢 | C |
| [DBZ-Burst-Limit-Recompiled](https://github.com/iExplosiveRage/DBZ-Burst-Limit-Recompiled) | Dragon Ball Z: Burst Limit Recompiled - native PC port via ReXGlue static recompilation | 53 | 🟢 | C++ |
| [DQ8-Recompiled](https://github.com/Sinan-Karakaya/DQ8-Recompiled) | Recompilation of Dragon Quest VIII (PS2) to run natively on PC and Mac | 52 | 🟢 | C++ |
| [naruto-rise-recomp](https://github.com/jorjbarbosa/naruto-rise-recomp) | Static PC recompilation of Naruto: Rise of a Ninja (Xbox 360) via ReXGlue | 52 | 🟢 | C++ |
| [Open Annihilation](https://github.com/open-annihilation/open-annihilation) | Recomp of Total Annihilation and Total Annihilation: Kingdoms (RTS). | 52 | 🟢 | C++ |
| [Rock Band 3 (Xbox 360)](https://github.com/ihatecompvir/band3_recomp) | Xbox 360 static recompilation of Rock Band 3 (Xbox 360) | 52 | 🟢 | C++ |
| [wc1-re](https://github.com/neuromancer/wc1-re) | Open-source recomp of Wing Commander I. | 52 | 🟢 | C |
| [Underworld Exhumed](https://github.com/abedegno/underworld-exhumed) | Bit-exact recomp of Ultima Underworld I and II. | 51 | 🟢 | C |
| [P3P3DS](https://github.com/endercodezz/P3P3DS) | Persona 3 Portable port for the New Nintendo 3DS | 50 | 🟢 | C++ |
| [Dead Rising 2: Case West Recomp](https://github.com/wivi514/Dead_Rising_2_Case_West_Xenon_Recomp) | Dead Rising 2: Case West Xbox 360 static recompilation | 49 | 🟢 | C++ |
| [god-of-war-recomp](https://github.com/KIexster/god-of-war-recomp) | Native PC port of God of War (PS2) via static recompilation with PS2Recomp | 48 | 🟢 | C++ |
| [NFS-CARBON-360-ANDROID-RECOMP](https://github.com/codepdbh/NFS-CARBON-360-ANDROID-RECOMP) | Static recompilation of Need for Speed Carbon (Xbox 360) for Windows and Android | 48 | 🟢 | JavaScript |
| [OpenXvT](https://github.com/elyosh/OpenXvT) | Open-source recomp of X-Wing vs Tie Fighter. | 48 | 🟢 | C |
| [regaiden-recomp](https://github.com/sergiomanzur/regaiden-recomp) | Native static recompilation of Resident Evil Gaiden (GBC) for PC | 48 | 🟢 | C |
| [VandalHearts-PcPort](https://github.com/HalmyLyseas/VandalHearts-PcPort) | Vandal Hearts native PC port based on a matching decompilation | 48 | 🟢 | C |
| [fukami](https://github.com/danisandoval/fukami) | Native macOS / Steam Deck port of Ridge Racer V by static recompilation | 47 | 🟢 | C++ |
| [sf64-dc](https://github.com/jnmartin84/sf64-dc) | Sega Dreamcast port of the Star Fox 64 decompilation | 47 | 🟢 | C |
| [th06-sdl2](https://github.com/CNTianQi233/th06-sdl2) | Rebuild of the Touhou 6 decompilation on SDL2 and OpenGL | 47 | 🟢 | C++ |
| [gears-judgement-recomp](https://github.com/OverkillLabs3/gears-judgement-recomp) | Native Windows recompilation of Gears of War: Judgment (Xbox 360) | 46 | 🟢 | C++ |
| [Kirby64Recomp](https://github.com/Kirby64Ret/Kirby64Recomp) | Kirby 64 Recomp (ok fine i'll use cmake) | 46 | 🟢 | C++ |
| [NHL Legacy Recomp](https://github.com/puckhead73/nhl-legacy-recomp) | Xbox 360 NHL Legacy recompiled to PC with ReXGlue | 46 | 🟢 | C++ |
| [Pilotwings64Recomp](https://github.com/gcsmith/Pilotwings64Recomp) | Static recompilation of Pilotwings 64 (WIP). | 46 | 🟢 | C++ |
| [Black-2006-Recomp](https://github.com/portingpete/Black-2006-Recomp) | Native Windows static recompilation of BLACK (2006) for the original Xbox | 44 | 🟢 | C |
| [OpenTricky](https://github.com/GiZcesi/OpenTricky) | OpenTricky is an unofficial PC port of SSX Tricky, made by static recompilation. Bring your own disc. | 44 | 🟢 | C |
| [pokeemerald-3d](https://github.com/tripplyons/pokeemerald-3d) | Pokemon Emerald in 3D (in WebAssembly) | 44 | 🟢 | C |
| [Tekken3Recompiled](https://github.com/FishB0nes98/Tekken3Recompiled) | Tekken 3 hybrid recompilation preview with Jun Kazama, widescreen, custom skins and local asset import tools. | 44 | 🟢 | C++ |
| [SWROTS-PC](https://github.com/jedijosh920/SWROTS-PC) | Unofficial native Windows port of Star Wars Episode III: Revenge of the Sith (Xbox) | 43 | 🟢 | C++ |
| [automobililamborghini-recomp](https://github.com/alondero/automobililamborghini-recomp) | Automobili Lamborghini (N64) static recompilation | 41 | 🟢 | C++ |
| [Destroy All Humans! Path of the Furon](https://github.com/masterspike52/reDAHM) | Xbox 360 static recompilation of Destroy All Humans! Path of the Furon | 41 | 🟢 | C++ |
| [MegaManX2Recomp](https://github.com/mstan/MegaManX2Recomp) | Static recompilation of Mega Man X2 (SNES) | 41 | 🟢 | Python |
| [pokerecomp](https://github.com/Decryptu/pokerecomp) | A native Godot 4 reimplementation of the Gen 1 and 2 Game Boy Color games. Not an emulator, bring your own ROM. | 41 | 🟢 | GDScript |
| [Re-Cherry](https://github.com/MaxDeadBear/Re-Cherry) | Re-Cherry | 41 | 🟢 | C++ |
| [Halo 3 (Delta)](https://github.com/twist84/halo3_cache_release_recomp) | Xbox 360 static recompilation of Halo 3 (Delta) | 40 | 🟢 | C++ |
| [MojoRecomp](https://github.com/OAleex/MojoRecomp) | Native PC recompilation project for Crash of the Titans | 40 | 🟢 | C++ |
| [fm4-recomp](https://github.com/Alexbeav/fm4-recomp) | Experimental static recompilation of Forza Motorsport 4 using ReXGlue. No game files included. | 39 | 🟢 | PowerShell |
| [re-wor](https://github.com/ronniecloud/re-wor) | Native recompilation of Guitar Hero: Warriors of Rock (Xbox 360) for PC | 39 | 🟢 | C++ |
| [WCWvsNWOWorldTourRecomp](https://github.com/jessetbh/WCWvsNWOWorldTourRecomp) | WCW vs. nWo: World Tour N64 static recompilation | 39 | 🟢 | C++ |
| [aerogauge-recomp](https://github.com/alondero/aerogauge-recomp) | Static recompilation of AeroGauge for the Nintendo 64 | 38 | 🟢 | C++ |
| [PlayStunts](https://github.com/ACatWithEbola/playstunts) | Recomp of Stunts to TypeScript, playable online. | 38 | 🟢 | TypeScript |
| [rush2recompiled](https://github.com/bryantmh/rush2recompiled) | Recompilation of the N64 game Rush 2 | 38 | 🟢 | C++ |
| [RB2](https://github.com/WistfulHopes/RB2) | Dragon Ball Raging Blast 2 Recompiled | 37 | 🟢 | C++ |
| [Rocket-R](https://github.com/ThatGuyMcd/Rocket-R) | Rocket: Robot on Wheels static recompilation | 37 | 🟢 | C++ |
| [.hack//Recompilation](https://github.com/dothacktranslate/dothack-recompilation) | Native recompilation project for the PS2 .hack//IMOQ quadrilogy | 36 | 🟢 | Python |
| [3dpinball-dc](https://github.com/headshot2017/3dpinball-dc) | Port of the Space Cadet Pinball decompilation to Dreamcast | 36 | 🟡 | C++ |
| [3dpinball-ps2](https://github.com/headshot2017/3dpinball-ps2) | Port of the Space Cadet Pinball decompilation to PlayStation 2 | 36 | 🟡 | C++ |
| [GSRecomp](https://github.com/Shmargus/GSRecomp) | Golden Sun GBA static recompilation | 36 | 🟢 | C++ |
| [mcla-recomp](https://github.com/holdmysocks/mcla-recomp) | Static recompilation of Midnight Club: Los Angeles (Xbox 360) for PC and PS5 | 36 | 🟢 | C++ |
| [Project8Recomp](https://github.com/theokyr/Project8Recomp) | Tony Hawk's Project 8 Xbox 360 static recompilation | 36 | 🟢 | C++ |
| [skyroads-sdl](https://github.com/pedrocatalao/skyroads-sdl) | SkyRoads (1993) reverse-engineered and ported natively to SDL2 | 36 | 🟢 | C |
| [ac3-remix](https://github.com/i5han/ac3-remix) | PC port and remaster of Ace Combat 3: Electrosphere | 35 | 🟢 |  |
| [MKVDCU-Recomp](https://github.com/KawaiiBunga/MKVDCU-Recomp) | Unofficial PC recompilation of Mortal Kombat vs. DC Universe | 35 | 🟢 | C++ |
| [skate3-android](https://github.com/andrewnakas/skate3-android) | Skate 3 on Android via native recompilation | 35 | 🟢 | Kotlin |
| [syphon-filter-2-recomp](https://github.com/alexbeavs-ps1-ports/syphon-filter-2-recomp) | Experimental Syphon Filter 2 static recompilation for Windows | 35 | 🟢 | Python |
| [Xerenge](https://github.com/shipa-2/Xerenge) | Burnout Revenge recompilation based on ReXGlue | 35 | 🟢 | C++ |
| [DefJamFFNY-recomp](https://github.com/vyanhursky/DefJamFFNY-recomp) | Def Jam: Fight for NY PC port — static recompilation of the original Xbox game for native Windows and macOS (Direct3D... | 34 | 🟢 | Python |
| [FFTARecomp](https://github.com/Jorge262007/FFTARecomp) | Native Windows port of Final Fantasy Tactics Advance (GBA) with widescreen | 34 | 🟢 | Rust |
| [Ultimate-Mortal-Kombat-3-iOS-Recomp](https://github.com/MaryNCRT/Ultimate-Mortal-Kombat-3-iOS-Recomp) | Ultimate Mortal Kombat 3 (iOS, EA Mobile 2011), fully decompiled: all 2,572 game functions are readable C, checked ag... | 34 | 🟢 | C |
| [EcstaticaRecompiled](https://github.com/spacefarergames/EcstaticaRecompiled) | This is a recomplimation and modern port of Ecstatica 1 and Ecstatica 2 that runs on modern Windows 10 / 11 systems f... | 33 | 🟢 | Assembly |
| [LASRecomp](https://github.com/peiikai/LASRecomp) | Static recompilation of Link's Awakening (Switch) to native macOS and Windows | 33 | 🟢 | C |
| [ChaotixRecompiled](https://github.com/YuutaTsubasa/ChaotixRecompiled) | Static recompilation of the Sega 32X game Knuckles' Chaotix into native C++ (Windows/Linux/macOS/Android), with true... | 32 | 🟢 | C++ |
| [HuntersRecomp](https://github.com/aabrole/HuntersRecomp) | Metroid Prime Hunters (DS) recompiled to a native dual-screen Android port | 32 | 🟢 | Java |
| [nfs-carbon-recomp](https://github.com/Sampreeth004/nfs-carbon-recomp) | Static recompilation of Need for Speed: Carbon (Xbox 360) to native C++ | 32 | 🟢 | C++ |
| [SM2-Recomp](https://github.com/SirSymo/SM2-Recomp) | Native recompilation of Spider-Man 2 (original Xbox) | 32 | 🟢 |  |
| [SotE-Recomp](https://github.com/GTTeancum/SotE-Recomp) | Static recompilation of Star Wars: Shadows of the Empire (N64) | 32 | 🟢 | C++ |
| [beanRecomp](https://github.com/kholdfuzion/beanRecomp) | In-progress recomp repo for Bean | 31 | 🟡 |  |
| [infinite-undiscovery-recomp](https://github.com/doc-haz/infinite-undiscovery-recomp) | Native PC recompilation of Infinite Undiscovery | 31 | 🟢 | C++ |
| [MK64 Portable](https://github.com/beckerd/psp_mk64_portable) | Native PSP port of Mario Kart 64 built on the n64decomp/mk64 decompilation | 31 | 🟢 | C |
| [outrun2-decomp](https://github.com/r4dius/outrun2-decomp) | OutRun 2006: Coast 2 Coast decompilation ported to many platforms | 31 | 🟢 | C++ |
| [Yakuza-Dead-Souls-EX](https://github.com/canersaka/Yakuza-Dead-Souls-EX) | Yakuza: Dead Souls recompilation effort | 31 | 🟢 | C |
| [mscharged-port](https://github.com/yannicksuter/mscharged-port) | Mario Strikers Charged ported to PC, Mac and Linux from decompiled code | 30 | 🟢 | C++ |
| [SanRecomp](https://github.com/OZORDI/SanRecomp) | Unofficial PC port of GTA V (Xbox 360) through static recompilation | 30 | 🟢 | C++ |
| [FZeroRecomp](https://github.com/craigshaw/FZeroRecomp) | Static recompilation of F-Zero to native PC | 29 | 🟢 | C |
| [mgb64](https://github.com/akratch/mgb64) | Decompilation-based native PC runtime for GoldenEye 007 | 29 | 🗄️ | C |
| [OpenCrossing-Xbox](https://github.com/TechProGabe/OpenCrossing-Xbox) | Native original Xbox port of Animal Crossing built from the GameCube decompilation | 29 | 🟢 | C |
| [RidgeRacer4Recomp](https://github.com/omegakatana92/RidgeRacer4Recomp) | Native PC port of R4: Ridge Racer Type 4 (PS1) built with PSXRecomp | 29 | 🟢 | PowerShell |
| [SpaceRangersHD_FPC](https://github.com/pakompom/SpaceRangersHD_FPC) | Cross-platform port of Space Rangers HD: A War Apart based on its decompilation | 29 | 🟢 | Pascal |
| [WindWakerHD-Android-Plus](https://github.com/Nycolazs/WindWakerHD-Android-Plus) | The Legend of Zelda: The Wind Waker HD natively on Android (static recompilation, Vulkan). Built-in Brazilian Portugu... | 29 | 🟢 | C++ |
| [betrayal-at-krondor](https://github.com/canassa/betrayal-at-krondor) | Betrayal at Krondor: A byte-perfect recompilation of the 1993 classic. | 28 | 🟢 | Assembly |
| [CV64-Recomp](https://github.com/spacefarergames/CV64-Recomp) | Static Recomp and Remaster of Castlevania 64 | 28 | 🟢 | C++ |
| [Guitar Hero II](https://github.com/YoshiCrystal9/re-gh2) | Xbox 360 static recompilation of Guitar Hero II | 28 | 🟢 | C++ |
| [Little Planet](https://github.com/carlosrmz009/littleplanet) | Sonic CD (Mega-CD) byte-identical disassembly plus static recompilation into a native PC port | 28 | 🟢 | Assembly |
| [nox-decomp](https://github.com/neuromancer/nox-decomp) | Unofficial Linux port of Nox (2000) from decompiled code | 28 | 🗄️ | C |
| [redalert2-recomp](https://github.com/sp00nznet/redalert2-recomp) | Static recompilation of Command & Conquer: Red Alert 2 / Yuri's Revenge (Westwood, 2000-01) to native C, with the rem... | 28 | 🟢 | C |
| [WWFNoMercyRecomp](https://github.com/jessetbh/WWFNoMercyRecomp) | WWF No Mercy N64 static recompilation | 28 | 🟢 | C |
| [conker64-recompiled](https://github.com/Conker64Recomp/conker64-recompiled) | Native PC port of Conker's Bad Fur Day (N64) via Static MIPS Recompilation. SDL2 engine with 3D UV texturing, N64 aud... | 27 | 🟢 | C |
| [DQIV-Recompiled](https://github.com/GoldieLeGenie/DQIV-Recompiled) | Native PC version of Dragon Quest IV (DS) via recompilation | 27 | 🟢 | C++ |
| [nfs-carbon-mac](https://github.com/vasist15-source/nfs-carbon-mac) | Need for Speed: Carbon (PC) natively on Apple Silicon Macs via static recompilation | 27 | 🟢 | C++ |
| [the-browsing-of-isaac](https://github.com/chiikabu/the-browsing-of-isaac) | The Binding of Isaac: Repentance+ recompiled to WebAssembly, playable in the browser. | 27 | 🟢 | JavaScript |
| [CTW-Native](https://github.com/official-kryo-to/ctw-native) | Recomp of GTA: Chinatown Wars from Android to Windows. | 26 | 🟢 | C++ |
| [DB-Final-Bout-Recomp](https://github.com/novapowers0/DB-Final-Bout-Recomp) | Static recompilation of Dragon Ball GT: Final Bout (PS1) for Windows | 26 | 🟢 | Python |
| [fuc-recomp](https://github.com/elprogramadorloco-arch/fuc-recomp) | Hybrid native Fate/unlimited codes project: PSP static-recompilation/gameplay base with PS2 assets and controls in de... | 26 | 🟢 | C++ |
| [Geometry Wars: Retro Evolved 2 Recompiled](https://github.com/saulob/geometry-wars-retro-evolved-2-recompiled) | Native PC port of Geometry Wars: Retro Evolved 2 (Xbox 360) via static recompilation | 26 | 🟢 | C++ |
| [wet-recomp](https://github.com/Supermedo/wet-recomp) | Fan PC port of WET (Xbox 360) via ReXGlue static recompilation | 26 | 🟢 | C# |
| [annepad](https://github.com/chrissotraidis/annepad) | Pokémon Stadium for iPhone and iPad via static recompilation, with native Metal rendering, touch controls, and ROM-fr... | 25 | 🟢 | Shell |
| [arcade-js](https://github.com/qarl/arcade-js) | Arcade ROMs decompiled to idiomatic JavaScript with LLMs, validated against MAME | 25 | 🟢 | JavaScript |
| [halo-ce-anbernic-rg35xx](https://github.com/kirklandsig/halo-ce-anbernic-rg35xx) | Halo: Combat Evolved running natively on Anbernic RG35XX H handhelds | 25 | 🟢 | C |
| [oot-dc](https://github.com/jnmartin84/oot-dc) | Port of the Ocarina of Time decompilation to the Sega Dreamcast | 25 | 🟢 | C |
| [wc2-re](https://github.com/neuromancer/wc2-re) | Open-source recomp of Wing Commander II. | 25 | 🟢 | C |
| [WCWnWoRevengeRecomp](https://github.com/jessetbh/WCWnWoRevengeRecomp) | WCW/nWo Revenge N64 static recompilation | 25 | 🟢 | Python |
| [xmd-recompiled](https://github.com/florinp93/xmd-recompiled) | Native PC port of X-Men Destiny via static recompilation | 25 | 🟢 | C |
| [asuras-wrath-recomp](https://github.com/PauloUbirajara/asuras-wrath-recomp) | Recomp of Asura's Wrath using RexGlue for PC (wip) | 24 | 🟢 | C++ |
| [DragonBallZBuusFuryRecomp](https://github.com/mstan/DragonBallZBuusFuryRecomp) | Static recompilation of Dragon Ball Z: Buu's Fury with Adaptive Widescreen · Part of the R.A.I.D. community | 24 | 🟢 | C++ |
| [ForzaRecomp](https://github.com/NerunSmarts/ForzaRecomp) | In-progress static recompilation of Forza Horizon 1 | 24 | 🟢 | C++ |
| [issd-native](https://github.com/sergiomanzur/issd-native) | Native recompilation of International Superstar Soccer Deluxe (SNES) | 24 | 🟢 | C |
| [master-chef](https://github.com/mitchaiet/master-chef) | Unofficial native Halo: Combat Evolved for Apple Vision Pro. Immersive panorama, controller support, and visual mods.... | 24 | 🟢 | C |
| [Mother3Recomp](https://github.com/agray0425/Mother3Recomp) | Static recompilation of MOTHER 3 (GBA) to native PC on the gbarecomp framework | 24 | 🟢 | C++ |
| [skifree_sdl](https://github.com/jeff-1amstudios/skifree_sdl) | SkiFree decompiled and ported to SDL2 | 24 | 🟡 | C |
| [Street-Fighter-EX2-Plus-Recompiled](https://github.com/strider973/Street-Fighter-EX2-Plus-Recompiled) | Static recompilation of Street Fighter EX2 Plus (PS1) | 24 | 🟢 | Python |
| [nfsmw-ios](https://github.com/bep1s69/nfsmw-ios) | Static recompilation port of Need for Speed Most Wanted (Xbox 360) for iOS | 23 | 🟢 | Python |
| [reo](https://github.com/sp00nznet/reo) | Static recompilation of Resident Evil Outbreak for modern Windows | 23 | 🟢 | C++ |
| [tomodachi-ltd-recomp](https://github.com/RussoPhone/tomodachi-ltd-recomp) | Native PC build of Tomodachi Life: Living the Dream via static recompilation. Bring your own copy — no game files inc... | 23 | 🟢 | Python |
| [castlevania-chronicles-recomp](https://github.com/Spicywonda/castlevania-chronicles-recomp) | Experimental Castlevania Chronicles (PS1) recompilation | 22 | 🟢 | C# |
| [NSMB-Wii-Multiplayer-Recompilation](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation) | Static recompilation of New Super Mario Bros. Wii for Android and Windows | 22 | 🟢 | C++ |
| [PerfectDarkRemasterRecomp](https://github.com/nikolaygorb/PerfectDarkRemasterRecomp) | Perfect Dark Remaster 2010 [Xbox360] game static recompilation project based on RexGlue-SDK | 22 | 🟢 | C++ |
| [pspoke](https://github.com/IbrahimIrfan/pspoke) | Pokemon Platinum and SoulSilver running natively on the PSP | 22 | 🟢 | C |
| [repentogxm](https://github.com/0xl0cal/repentogxm) | PS Vita port of The Binding of Isaac: Repentance by static recompilation of the PC executable to ARM. | 22 | 🟢 | C |
| [Superman64Recomp](https://github.com/gcsmith/Superman64Recomp) | Static recompilation of Superman 64 (WIP). | 22 | 🟢 | C++ |
| [ufc3recomp](https://github.com/paulogaab21/ufc3recomp) | Native recompilation of UFC 3 Undisputed for Windows, Linux and macOS | 22 | 🟢 | C++ |
| [demoscene-recomp](https://github.com/treylorswift/demoscene-recomp) | Classic DOS demoscene productions recompiled to run natively in the browser | 21 | 🟢 | JavaScript |
| [OpenJam](https://github.com/GTTeancum/OpenJam) | Native PC port of NBA JAM: On Fire Edition (Xbox 360) via static recompilation | 21 | 🟢 | Python |
| [Splatterhouse Recompiled](https://github.com/0c0de/splatterhouse-decomp) | Native PC port of Splatterhouse (2010, Xbox 360) via ReXGlue static recompilation | 21 | 🟢 | C++ |
| [Starfox Recomp](https://github.com/mstan/StarFoxSNESRecomp) | Recomp + enhancement of Starfox (SNES). | 21 | 🟢 | C |
| [ar-recomp](https://github.com/DerrickGold/ar-recomp) | ActRaiser (SNES) recompilation project | 20 | 🟢 | C |
| [Birdman64](https://github.com/NoahVl/Birdman64) | Pilotwings 64 as a native PC game for Windows and Linux: widescreen, 144 Hz+, gamepads. Bring your own ROM, no emulator. | 20 | 🟢 | Rust |
| [MCX360-EDITION](https://github.com/DevZer0D4Y/MCX360-EDITION) | ReXGlue recompilation of Minecraft Xbox 360 Edition running on iOS | 20 | 🟢 | C++ |
| [midnightclub](https://github.com/zarif98/midnightclub) | Static recompilation of Midnight Club: Los Angeles (Xbox 360) using rexGlu SDK | 20 | 🟢 | C++ |
| [Simpsons Wrestling Recompiled](https://github.com/TekRantGaming/simpsons-wrestling-recompiled) | Recomp of Simpsons Wrestling (PS1) to PC. | 20 | 🟢 | C++ |
| [snowboardkids-recomp](https://github.com/cdlewis/snowboardkids-recomp) | Native PC port of Snowboard Kids (N64) for Windows, Linux and macOS | 20 | 🟢 | C |
| [sonic-r-android](https://github.com/ZinexDa/sonic-r-android) | Native Android port of the Sonic R PC decompilation with GLES2 renderer | 20 | 🟢 | C |
| [Space-Channel-5](https://github.com/ZoomiesZaggy/Space-Channel-5) | Unofficial native Space Channel 5 port for Windows, Linux and macOS. Compiler-free downloads, display options, contro... | 20 | 🟢 | C |
| [srw64-recomp](https://github.com/dyzz/srw64-recomp) | Experimental native recompilation of Super Robot Wars 64 with translations and HD mode | 20 | 🟢 | Python |
| [gdx-3ds](https://github.com/cruxxxxxx/gdx-3ds) | Unofficial 3DS port of F-Zero X based on its decompilation | 19 | 🟢 | C |
| [gow2-recomp](https://github.com/andrebrumdev/gow2-recomp) | God of War II HD static recompilation — curated work artifacts (lift boundaries, SPU lift sources, scripts, findings)... | 19 | 🟢 | Python |
| [ReShadowTower](https://github.com/JFryy/reshadowtower) | Recompiled native port of Shadow Tower (PS1) with modern PC controls | 19 | 🟢 | Python |
| [AkiLauncher](https://github.com/jessetbh/AkiLauncher) | Launcher for the AKI N64 wrestling static recompilations | 18 | 🟢 | C++ |
| [ArmyOfTwo-Recomp](https://github.com/Genesis5500/ArmyOfTwo-Recomp) | Experimental native PC port of Army of Two (Xbox 360) via ReXGlue static recompilation | 18 | 🟢 | C++ |
| [Metal Gear Solid Recompiled](https://github.com/alexbeavs-ps1-ports/metal-gear-solid-recomp) | PSXRecomp native PC port of Metal Gear Solid (PS1) | 18 | 🟢 | Python |
| [OpenSpideyPS1](https://github.com/GTTeancum/SpideyPS1recomp) | Recomp of Spider-Man PS1 and Spider-Man 2: Enter Electro to PC. | 18 | 🟢 | C# |
| [Test Drive Unlimited](https://github.com/testdriveupgrade/TDURE) | Xbox 360 static recompilation of Test Drive Unlimited | 18 | 🟢 | C++ |
| [WWE-AllStars-Recomp](https://github.com/shaneomac1337/WWE-AllStars-Recomp) | Unofficial Windows version of WWE All Stars (Xbox 360), recompiled with ReXGlue. Bring your own disc image. | 18 | 🟢 | C++ |
| [Body Harvest Recompiled](https://github.com/danielgomesvieira2000/body-harvest-recomp) | Native PC port of Body Harvest (N64) built with N64Recomp and RT64 | 17 | 🟢 | C++ |
| [CafeRecomp](https://github.com/hardkiller2565123123/CafeRecomp) | Wii U static recompilation framework, starting with Breath of the Wild | 17 | 🟢 | C |
| [FinFanTacRecomp](https://github.com/NJH-1001/FinFanTacRecomp) | PSXRecomp native Windows port of Final Fantasy Tactics (PS1) with 16:9 option | 17 | 🟢 | Python |
| [moonpearl](https://github.com/DoutorRaposo/moonpearl) | Android port of snesrev/zelda3 (ALttP reimplementation): widescreen, rewind, shaders, MSU-1, save states, controller... | 17 | 🟢 | Kotlin |
| [scooby-doo-mystery port](https://github.com/janezkranjc/scooby-doo-mistery-mouse-version) | Native SFML port of Sega Genesis Scooby-Doo Mystery from reverse-engineered 68000 code | 17 | 🟢 | C++ |
| [twisted-metal-2012-ps3-native-port](https://github.com/franklincg/twisted-metal-2012-ps3-native-port) | Community native PC recompilation of Twisted Metal (2012, PS3) | 17 | 🟢 | C |
| [weltendaemmerung](https://github.com/s-macke/weltendaemmerung) | Reverse engineering a C64 game with AI and porting it to the web | 17 | 🟢 | Assembly |
| [xboxdashboard](https://github.com/sp00nznet/xboxdashboard) | The first-ever native PC port of the original Xbox Dashboard (build 3944) — static recompilation of xboxdash.xbe (x86... | 17 | 🟢 | C |
| [Earthbound Companion](https://github.com/rages4calm/earthbound-companion) | Recomp of Earthbound (SNES) to PC. | 16 | 🟢 | Python |
| [ffta-recomp](https://github.com/james2doyle/ffta-recomp) | Native recompilation of Final Fantasy Tactics Advance (GBA) built on the gbarecomp framework | 16 | 🟢 | Python |
| [PerfectDarkZeroRecomp](https://github.com/nikolaygorb/PerfectDarkZeroRecomp) | Perfect Dark Zero [Xbox360] game static recompilation project based on RexGlue-SDK | 16 | 🟢 | C++ |
| [socom-unzipped](https://github.com/Scotho/socom-unzipped) | SOCOM II: U.S. Navy SEALs, statically recompiled for PC with self-hosted online play | 15 | 🟢 | Python |
| [Sonic '06 Demo](https://github.com/PranchaD/re-Sonic06Demo) | Xbox 360 static recompilation of Sonic '06 Demo | 15 | 🟢 | CMake |
| [TooTawersRecomp](https://github.com/Gumpolas/TooTawersRecomp) | Native Windows port of The Lord of the Rings: The Two Towers (Xbox, 2002) via static recompilation | 15 | 🟢 |  |
| [OpenEmperor](https://github.com/oliverjessner/OpenEmperor) | 🤴🏼 Clean-room reimplementation of Emperor: Rise of the Middle Kingdom in C++20 and SDL3. Built for modern systems, st... | 14 | 🟢 | C++ |
| [Test Drive](https://github.com/kylofon/test-drive-sdl3) | Open-source recomp of Test Drive (1987). | 14 | 🟢 | C |
| [defjam_recomp](https://github.com/comoria08/defjam_recomp) | Static recompilation of Def Jam: Fight for NY (Xbox) for Windows | 13 | 🟢 | C |
| [doa3-recomp](https://github.com/parkerallan/doa3-recomp) | Dead or Alive 3 PC Port | 13 | 🟢 | Assembly |
| [MCLA-4iOS](https://github.com/KoreanSeats1/MCLA-4iOS) | Midnight Club: Los Angeles on iPhone and iPad — ARM64 static recompilation, native Metal, and an experimental 60 FPS... | 13 | 🟢 | Objective-C++ |
| [project-1944](https://github.com/zenit2893-cmyk/project-1944) | Unofficial native Windows PC port of Call of Duty 3 (Xbox 360) via static recompilation. Bring your own game. EN · RU... | 13 | 🟢 | Python |
| [re-stunts](https://github.com/CommonLoon102/restunts-bb11) | Recomp of the game Stunts. Original and enhanced versions. | 13 | 🟢 | C |
| [SVR2011-Recomp](https://github.com/shaneomac1337/SVR2011-Recomp) | Unofficial Windows version of WWE SmackDown vs. Raw 2011 (Xbox 360), recompiled with ReXGlue. Bring your own disc image. | 13 | 🟢 | C++ |
| [WetRecomp](https://github.com/nikolaygorb/WetRecomp) | Wet [Xbox360] game static recompilation project based on RexGlue-SDK | 13 | 🟢 | C++ |
| [WWFWrestleMania2000Recomp](https://github.com/jessetbh/WWFWrestleMania2000Recomp) | WWF WrestleMania 2000 N64 static recompilation | 13 | 🟢 | Python |
| [X-Men Mutant Academy 2](https://github.com/GTTeancum/xmen-mutant-academy-2-pc) | Recomp of the PS1 game X-Men Mutant Academy 2. | 13 | 🟢 | Python |
| [CV64Recomp](https://github.com/RevoSucks/CV64Recomp) | A recompilation of Castlevania for the N64. | 12 | 🟢 | C |
| [Glover-R](https://github.com/ThatGuyMcd/Glover-R) | Static recompilation of the N64 game Glover to native PC | 12 | 🟢 | Python |
| [hard-corps-uprising-recompiled](https://github.com/saulob/hard-corps-uprising-recompiled) | Native PC port of Hard Corps: Uprising (Xbox Live Arcade) via static recompilation, with the TRG launcher | 12 | 🟢 | C++ |
| [nfs-mw](https://github.com/47PADO47/nfs-mw) | 🦀 Rust rewrite of Need for Speed: Most Wanted (2005, PC v1.3 / Black Edition) with bevy engine | 12 | 🟢 | Rust |
| [nfsmw-recomp](https://github.com/veritr1x/nfsmw-recomp) | Recompilation of Need for Speed: Most Wanted (the 2005 PC Black Edition) built on recomp-kit: macOS, iPad, Linux, Win... | 12 | 🟢 | C |
| [WWE-SVR2008-RECOMP](https://github.com/nefariousjosiah/WWE-SVR2008-RECOMP) | Native PC port of WWE SmackDown vs. Raw 2008 (Xbox 360) via static recompilation | 12 | 🟢 | C++ |
| [WWE-SVR2009-RECOMP](https://github.com/nefariousjosiah/WWE-SVR2009-RECOMP) | Native PC port of WWE SmackDown vs. Raw 2009 (Xbox 360) via static recompilation | 12 | 🟢 | C++ |
| [WWE-SVR2010-RECOMP](https://github.com/nefariousjosiah/WWE-SVR2010-RECOMP) | Native PC port of WWE SmackDown vs. Raw 2010 (Xbox 360) via static recompilation | 11 | 🟢 | C++ |
| [Banjo-Tooie: Recompiled](https://github.com/Vidanox/BanjoTooieRecompiled) | Banjo-Tooie static recompilation for Windows/Linux | 10 | 🟢 | C |
| [mm3-recomp](https://github.com/MattSG/mm3-recomp) | Static recompilation of Midtown Madness 3 (Xbox) to native Windows x64 with a Direct3D 11 renderer | 10 | 🟢 | C |
| [burnout-crash-recomp](https://github.com/mpkonmbk/burnout-crash-recomp) | Native PC port of Burnout CRASH! (Xbox 360 XBLA) via ReXGlue static recompilation | 9 | 🟢 | C++ |
| [caesar2-port](https://github.com/second-impressions/caesar2-port) | Portable continuation of the Caesar II source reconstruction | 9 | 🟢 | C |
| [DAORecomp](https://github.com/96dot/DAORecomp) | Static recompilation of Dragon Age: Origins (Xbox 360) to native PC | 9 | 🟢 | C |
| [jsrf-recomp](https://github.com/andeecollard/jsrf-recomp) | Static recompilation of Jet Set Radio Future (Xbox) to native macOS — playable into chapter 2 at 60 fps via a Direct3... | 9 | 🟢 | C |
| [linksawakening-portable](https://github.com/sp00nznet/linksawakening-portable) | Link's Awakening DX statically recompiled to native C and ported to PlayStation 4, PlayStation 3, and Nintendo 3DS. N... | 9 | 🟢 | C |
| [muscle-march-recomp](https://github.com/tmcleroy/muscle-march-recomp) | Unofficial native PC port of Muscle March (WiiWare) via static recompilation: macOS, Linux, Steam Deck, Windows. Requ... | 9 | 🟢 | C++ |
| [RogueSquadron64Recomp](https://github.com/MikeSemicolonD/RogueSquadron64Recomp) | A fully playable (AI assisted) static recompilation of Star Wars: Rogue Squadron on N64 for the PC, Linux & Android | 9 | 🟢 | C++ |
| [Titanic: Adventure Out of Time](https://github.com/itskenny0/titanic-godot) | Recomp of Titanic Adventure Out of Time to Godot. | 9 | 🟢 | Go |
| [Warthog](https://github.com/ChupathingyCE/warthog) | Halo: Combat Evolved decompilation rebuilt for the original Xbox, playing online with PC builds | 9 | 🟢 | C |
| [SacredStonesRecomp](https://github.com/Lordingard/SacredStonesRecomp) | Playable Windows and Android ARM64 recompilation of Fire Emblem: The Sacred Stones (GBA). | 8 | 🟢 | PowerShell |
| [StrikersRecomp](https://github.com/aharonahdoot/StrikersRecomp) | Super Mario Strikers (G4QE01) recompilation project — the worked example for RecompCore and DolRuntime. No game data... | 8 | 🟢 | C |
| [Test Drive III](https://github.com/kylofon/test-drive-3-sdl3) | Recomp of Test Drive III: The Passion. | 8 | 🟢 | C |
| [TheDarknessRecomp](https://github.com/nikolaygorb/TheDarknessRecomp) | The Darkness [Xbox360] game static recompilation project based on RexGlue-SDK | 8 | 🟢 | C++ |
| [VPW64Recomp](https://github.com/jessetbh/VPW64Recomp) | Virtual Pro Wrestling 64 static recompilation | 8 | 🟢 | C++ |
| [aerobiz-disasm](https://github.com/matiaszanolli/aerobiz-disasm) | Complete static recompilation of Aerobiz Supersonic for the Sega Genesis | 7 | 🟢 | Assembly |
| [DoomSNESRecomp](https://github.com/Cacodemontube/DoomSNESRecomp) | This is a PC Recomp of the SNES Version of Doom using SNESrecomp. | 7 | 🟢 | C |
| [RROP](https://github.com/kruzeman/RROP) | Static recompilation of Rings of Power for Linux and Windows with widescreen and smooth scrolling | 7 | 🟢 | Python |
| [SHO-GTA-VCS-PS2Recomp](https://github.com/BlackLineInteractive/SHO-GTA-VCS-PS2Recomp) | Playstation 2 Static Recompiler Silent Hill Origins & GTA Vice City Stories | 7 | 🗄️ | C++ |
| [TDURecomp](https://github.com/testdriveupgrade/TDURecomp) | Recompilation of TDU | 7 | 🟢 | C++ |
| [WiiCompiled-Switch](https://github.com/yashin-sh/WiiCompiled-Switch) | Experimental native Nintendo Switch port of WiiCompiled, with GX capture/replay and GPU diagnostics. Recognizable gam... | 7 | 🟢 | C++ |
| [DeepSea](https://github.com/AH64-dll/DeepSea) | Deep Sea: The Wind Waker at 60 fps. A free, open-source native Windows port you build from your own disc. | 6 | 🟢 | C |
| [DragonBallZLegacyOfGokuRecomp](https://github.com/mstan/DragonBallZLegacyOfGokuRecomp) | Static recompilation of Dragon Ball Z: The Legacy of Goku with Adaptive Widescreen · Part of the R.A.I.D. community | 6 | 🟢 | C++ |
| [FFCCEOT-Recomp](https://github.com/JonathanDC64/FFCCEOT-Recomp) | Native PC port of Final Fantasy Crystal Chronicles: Echoes of Time (DS) by static recompilation. Bring your own ROM:... | 6 | 🟢 | C++ |
| [heavymetal](https://github.com/sp00nznet/heavymetal) | A static recompilation of Heavy Metal: FAKK2 (2000) targeting modern Windows 11 x86-64. | 6 | 🟢 | C |
| [Herculan](https://github.com/kevinfoley/Herculan) | Recomp of Earthsiege 2 by Dynamix. | 6 | 🟢 | C# |
| [Snapshot](https://github.com/dreamsailing59-ops/Snapshot) | Static recompilation of Pokémon Snap (N64, 1999) for PC platforms (Windows, Linux, macOS) | 6 | 🟢 | C++ |
| [Top-Gear-SNES-Static-Recomp](https://github.com/Junior-Jones/Top-Gear-SNES-Static-Recomp) | Static recompilation of Top Gear (SNES) for Windows 10 and 11. ROM not included. | 6 | 🟢 | C |
| [VeronicaRecomp](https://github.com/psxrestore/VeronicaRecomp) | A static recompilation of Resident Evil CODE:Veronica developed with RexGlue. | 6 | 🟢 | C++ |
| [WiiCompiled-Xbox-UWP](https://github.com/itzjuan612/WiiCompiled-Xbox-UWP) | Xbox Series / UWP port of WiiCompiled - a Mario Kart Wii static recompilation with a Dawn/D3D12 renderer | 6 | 🟢 | C++ |
| [ANIMANIACS-GC-RECOMP](https://github.com/ant0-blase/ANIMANIACS-GC-RECOMP) | Animaniacs: The Great Edgar Hunt — GameCube Static Recompilation | 5 | 🟢 | C++ |
| [caesar2-reconstruction](https://github.com/second-impressions/caesar2-reconstruction) | Clean-room reconstruction of Caesar II. | 5 | 🟢 | C |
| [pokemon](https://github.com/sp00nznet/pokemon) | Generation I Pokémon (Red/Blue/Yellow) statically recompiled to native C — no emulator at runtime. Plus a headless bu... | 5 | 🟢 | Python |
| [portemon](https://github.com/portemon-nitro/portemon) | Getting HeartGold/SoulSilver out of the DS | 5 | 🟢 | Lua |
| [Spider-Man-2-PS2-Recomp](https://github.com/saltyboosack-blip/Spider-Man-2-PS2-Recomp) | Open-source PS2 recompilation research checkpoint for Spider-Man 2 (USA), no rom included. | 5 | 🟢 | C++ |
| [xwa](https://github.com/sp00nznet/xwa) | A static recompilation of Star Wars: X-Wing Alliance (1999) by Totally Games / LucasArts, targeting modern Windows wi... | 5 | 🟢 | C |
| [3on3NHL-recomp](https://github.com/Wndwsqrrl/3on3NHL-recomp) | 3 on 3 NHL Arcade Xbox 360 static recompilation | 4 | 🟢 | C# |
| [Street Rod](https://github.com/kylofon/street-rod-sdl3) | Recomp of Street Rod. | 4 | 🟢 | C |
| [Test Drive II](https://github.com/kylofon/test-drive-2-sdl3) | Open-source recomp of Test Drive II: The Duel. | 4 | 🟢 | C |
| [CyberMage Modern](https://github.com/RoninSan369/CyberMageModern) | Recomp of the DOS game CyberMage. | 3 | 🟢 |  |
| [kf1-enhanced](https://github.com/Acranon/kf1-enhanced) | Enhanced native PC port of King's Field based on reverse engineering | 3 | 🟢 | C++ |
| [MarioGolf64](https://github.com/Rainchus/MarioGolf64) | MarioGolf64 | 3 | 🟢 | Python |
| [Metal Mutant-web](https://github.com/kznsq/metal-mutant-web) | Recomp of the Silmarils game Metal Mutant to Javascript. | 3 | 🟢 | JavaScript |
| [Aces of the Pacific](https://github.com/kylofon/aces-of-the-pacific-sdl3) | Recomp of Dynamix' Aces of the Pacific. | 2 | 🟢 | C |
| [Gunboat](https://github.com/PlasticCog/Gunboat) | Open-source recomp of the game Gunboat. | 2 | 🟢 | C++ |
| [KnowYourRoleRecomp](https://github.com/Comfubar/KnowYourRoleRecomp) | WWF SmackDown! 2 PlayStation static recompilation | 2 | 🟢 | C# |
| [Bak-Again](https://github.com/stellargames/bakagain) | Recomp + enhancement of Betrayal At Krondor by Dynamix. | 1 | 🟢 | C# |
| [F-19](https://github.com/xor2003/f19re) | Recomp of MicroProse F-19. | 1 | 🟢 | Assembly |
| [Vette](https://github.com/PlasticCog/Vette2026) | Recomp of the game Vette by Spectrum Holobyte. | 1 | 🟢 | C++ |
| [Airborn Ranger](https://github.com/xor2003/airborn-ranger) | Recomp of Airborn Ranger by MicroProse. | 0 | 🟢 | C |
| [DNZHRecomp](https://gitlab.com/sonicdcer/DNZHRecomp) | DNZHRecomp |  | ⚪ |  |
| [Extreme-G: Recompiled](https://gitlab.com/sonicdcer/ExtremeGRecomp) | Extreme-G N64 static recompilation |  | ⚪ |  |
| [Mad TV online](https://madtvgame-tribute.com) | Recomp and enhancement/fixes to the German DOS game Mad TV. No github available yet, but playable online. Mad TV is a... |  | ⚪ |  |
| [MarioKart64Recomp](https://gitlab.com/sonicdcer/MarioKart64Recomp) | MarioKart64Recomp |  | ⚪ |  |
| [Starfox64Recomp](https://gitlab.com/sonicdcer/Starfox64Recomp) | Starfox64Recomp |  | ⚪ |  |
