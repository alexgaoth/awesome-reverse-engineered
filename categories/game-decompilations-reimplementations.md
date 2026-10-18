# Game Decompilations & Reimplementations

[← All categories](../README.md#whats-inside) · [Search this category on the website](https://alexgaoth.github.io/awesome-reverse-engineered/#c=game-decompilations-reimplementations) · 3,039 projects · [Listed here? Get the badge](../README.md#is-your-project-listed)

Health: 🟢 pushed in the last year · 🟡 1 to 3 years · 🔴 over 3 years · 🗄️ archived · ⚪ unknown

- [Asset & File-Format Tools](#asset--file-format-tools) (249)
- [Console Emulators](#console-emulators) (217)
- [Engine Reimplementations](#engine-reimplementations) (670)
- [Fan Patches & Enhancements](#fan-patches--enhancements) (22)
- [Game Network Protocols & APIs](#game-network-protocols--apis) (118)
- [Launchers & Store Clients](#launchers--store-clients) (47)
- [Matching Decompilations — Arcade](#matching-decompilations--arcade) (5)
- [Matching Decompilations — Atari](#matching-decompilations--atari) (3)
- [Matching Decompilations — Game Boy / GBA / DS](#matching-decompilations--game-boy--gba--ds) (119)
- [Matching Decompilations — GameCube & Wii](#matching-decompilations--gamecube--wii) (117)
- [Matching Decompilations — Mobile](#matching-decompilations--mobile) (25)
- [Matching Decompilations — Nintendo 64](#matching-decompilations--nintendo-64) (93)
- [Matching Decompilations — Other / Multi-platform](#matching-decompilations--other--multi-platform) (185)
- [Matching Decompilations — PC / DOS / Windows](#matching-decompilations--pc--dos--windows) (116)
- [Matching Decompilations — PSP / Vita / PS3](#matching-decompilations--psp--vita--ps3) (2)
- [Matching Decompilations — PlayStation 1](#matching-decompilations--playstation-1) (63)
- [Matching Decompilations — PlayStation 2](#matching-decompilations--playstation-2) (60)
- [Matching Decompilations — SNES / NES](#matching-decompilations--snes--nes) (47)
- [Matching Decompilations — Sega](#matching-decompilations--sega) (7)
- [Matching Decompilations — Switch](#matching-decompilations--switch) (9)
- [Matching Decompilations — Xbox](#matching-decompilations--xbox) (17)
- [Mod Loaders & Script Extenders](#mod-loaders--script-extenders) (105)
- [Open-source Game Clones](#open-source-game-clones) (58)
- [Other](#other) (48)
- [Private Servers](#private-servers) (183)
- [Static Recompilations & PC Ports](#static-recompilations--pc-ports) (454)

## Asset & File-Format Tools

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [PKHeX](https://github.com/kwsch/PKHeX) | Pokemon save file editor built on reverse-engineered save formats | 5,197 | 🟢 | C# |
| [gdsdecomp (GDRE Tools)](https://github.com/GDRETools/gdsdecomp) | Godot reverse-engineering tools: PCK extraction and GDScript decompiler | 4,349 | 🟢 | C++ |
| [noclip.website](https://github.com/magcius/noclip.website) | Web-based viewer for levels from many games via reverse-engineered formats | 4,288 | 🟢 | TypeScript |
| [UABE](https://github.com/SeriousCache/UABE) | Unity Asset Bundle Extractor (archived) | 4,133 | 🗄️ | C++ |
| [repkg](https://github.com/notscuffed/repkg) | Wallpaper Engine PKG extractor and TEX-to-image converter | 3,796 | 🟡 | C# |
| [GARbro](https://github.com/morkt/GARbro) | Resource browser and extractor for visual novel archive formats | 3,334 | 🟡 | C# |
| [uTinyRipper](https://github.com/mafaca/UtinyRipper) | GUI and library to extract Unity serialized and bundle assets | 3,105 | 🔴 | C# |
| [UE Viewer (UModel)](https://github.com/gildor2/UEViewer) | Viewer and exporter for Unreal Engine 1-4 assets | 2,951 | 🟡 | C++ |
| [DisUnity](https://github.com/ata4/disunity) | Experimental toolset for Unity asset and bundle files (archived) | 2,698 | 🗄️ | Java |
| [Source 2 Viewer](https://github.com/ValveResourceFormat/ValveResourceFormat) | Browse VPKs and view, extract and decompile Source 2 assets | 2,513 | 🟢 | C# |
| [vgmstream](https://github.com/vgmstream/vgmstream) | Library for playback of hundreds of streamed video game audio formats | 2,293 | 🟢 | C |
| [UndertaleModTool](https://github.com/UnderminersTeam/UndertaleModTool) | Modding, decompiling and unpacking tool for GameMaker games such as Undertale | 2,084 | 🟢 | C# |
| [KrkrExtract](https://github.com/xmoezzz/KrkrExtract) | Extracts and packs Kirikiri (krkr2/krkrz) XP3 archives | 1,427 | 🗄️ | C++ |
| [vgmtrans](https://github.com/vgmtrans/vgmtrans) | Converts proprietary sequenced video game music formats to MIDI and SoundFont | 1,283 | 🟢 | C++ |
| [unrpyc](https://github.com/CensoredUsername/unrpyc) | Ren'Py compiled script (.rpyc) decompiler | 1,268 | 🟢 | Ren'Py |
| [SwitchThemeInjector](https://github.com/exelix11/SwitchThemeInjector) | Create custom Nintendo Switch home-menu themes from the closed SZS layout format | 1,259 | 🟢 | C |
| [NHSE](https://github.com/kwsch/NHSE) | Animal Crossing: New Horizons save editor | 1,255 | 🟢 | C# |
| [extract-xiso](https://github.com/XboxDev/extract-xiso) | Xbox ISO creation and extraction utility | 1,225 | 🟢 | C |
| [Switch Toolbox](https://github.com/KillzXGaming/Switch-Toolbox) | Tool to edit many Nintendo game file formats | 1,214 | 🟢 | C# |
| [WolvenKit](https://github.com/WolvenKit/WolvenKit) | Mod editor/creator for REDengine games (Cyberpunk 2077, Witcher 3) | 1,214 | 🟢 | C# |
| [UAssetGUI](https://github.com/atenfyr/UAssetGUI) | Tool for low-level examination and editing of Unreal Engine assets | 1,084 | 🟢 | C# |
| [demoinfocs-golang](https://github.com/markus-wa/demoinfocs-golang) | Counter-Strike 2 and CS:GO demo parser for Go | 1,070 | 🟢 | Go |
| [SourceIO](https://github.com/REDxEYE/SourceIO) | Blender addon importing Source engine textures, models and maps | 978 | 🟢 | Python |
| [LSLib](https://github.com/Norbyte/lslib) | Tools for Larian Studios game formats (Divinity: Original Sin, Baldur's Gate 3) | 945 | 🟢 | C# |
| [xEdit](https://github.com/TES5Edit/TES5Edit) | Module editor and conflict detector for Bethesda games | 904 | 🟢 | Pascal |
| [BSPSource](https://github.com/ata4/bspsrc) | Source engine map decompiler (BSP to VMF) | 873 | 🟢 | Java |
| [Crowbar](https://github.com/ZeqMacaw/Crowbar) | GoldSource and Source engine modding tool: model decompiler and compiler front-end | 839 | 🟢 | Visual Basic .NET |
| [PalworldSaveTools](https://github.com/deafdudecomputers/PalworldSaveTools) | Toolkit to fix, transfer and edit Palworld save files | 820 | 🟢 | Python |
| [Wwise-Unpacker](https://github.com/Vextil/Wwise-Unpacker) | Unpacks Wwise .pck/.bnk audio into playable files | 803 | 🟢 | Batchfile |
| [Frosty Toolsuite](https://github.com/CadeEvs/FrostyToolsuite) | Modding tools for Frostbite engine games | 780 | 🟡 | C# |
| [clarity](https://github.com/skadistats/clarity) | Fast replay parser for Dota 2, CS:GO, CS2 and Deadlock in Java | 770 | 🟢 | Java |
| [VPKEdit](https://github.com/craftablescience/VPKEdit) | CLI/GUI tool to create, read and write VPK and other pack formats | 770 | 🟢 | C++ |
| [unrpa](https://github.com/Lattyware/unrpa) | Extracts files from the Ren'Py RPA archive format | 767 | 🔴 | Python |
| [CodeWalker](https://github.com/dexyfex/CodeWalker) | Interactive 3D map and asset editor for GTA V files | 760 | 🟡 | C# |
| [UnityPack](https://github.com/HearthSim/UnityPack) | Python deserialization library for Unity3D asset bundles | 752 | 🔴 | Python |
| [Smithbox](https://github.com/vawser/Smithbox) | Modding tool for Elden Ring, Sekiro, Dark Souls and Armored Core VI | 739 | 🟢 | C# |
| [demoparser](https://github.com/LaihoE/demoparser) | Counter-Strike 2 replay parser for Python and JavaScript | 733 | 🟢 | Rust |
| [manta](https://github.com/dotabuff/manta) | Dota 2 replay parser in Go | 694 | 🟢 | Go |
| [AssetsTools.NET](https://github.com/nesrak1/AssetsTools.NET) | Library to read and write Unity assets and bundle files | 692 | 🟢 | C# |
| [DSMapStudio](https://github.com/soulsmods/DSMapStudio) | Map and level editor for Demon's Souls, Dark Souls, Bloodborne, Sekiro and Elden Ring | 676 | 🟡 | C# |
| [Obsidian](https://github.com/Crauzer/Obsidian) | WAD archive editor for League of Legends | 668 | 🟢 | TypeScript |
| [StormLib](https://github.com/ladislav-zezula/StormLib) | Library for reading and writing Blizzard MPQ archives | 656 | 🟢 | C |
| [NifSkope](https://github.com/niftools/nifskope) | Viewer and editor for NetImmerse/Gamebryo NIF files | 638 | 🟡 | C++ |
| [rpatool](https://github.com/shizmob/rpatool) | Tool to work with Ren'Py RPA archives | 631 | 🗄️ | Python |
| [OWLib / DataTool](https://github.com/overtools/OWLib) | Overwatch game data extraction library and tools | 614 | 🟢 | C# |
| [jPSXdec](https://github.com/m35/jpsxdec) | Cross-platform PlayStation 1 audio and video converter | 607 | 🟢 | Java |
| [DS Anim Studio](https://github.com/Meowmaritus/DSAnimStudio) | Dark Souls TAE animation event editor | 586 | 🟢 | C# |
| [repak](https://github.com/trumank/repak) | Unreal Engine .pak archive library and CLI in Rust | 585 | 🟢 | Rust |
| [wow.export](https://github.com/Kruithne/wow.export) | Export toolkit for World of Warcraft models, textures and maps | 569 | 🟢 | JavaScript |
| [io_import_psk_psa](https://github.com/Befzz/blender3d_import_psk_psa) | Blender addon to import Unreal PSK/PSA meshes, skeletons and animations | 565 | 🟡 | Python |
| [u4pak](https://github.com/panzi/u4pak) | Unpack, pack and mount Unreal Engine 4 .pak archives | 562 | 🔴 | Python |
| [Godot PCK Explorer](https://github.com/DmitriySalnikov/GodotPCKExplorer) | Explorer, extractor and packer for Godot .pck files | 560 | 🟢 | C# |
| [NSTool](https://github.com/jakcron/nstool) | General-purpose read/extract tool for Nintendo Switch file formats | 547 | 🟡 | C++ |
| [fast64](https://github.com/Fast-64/fast64) | Blender editor for scenes and meshes in first-party N64 game formats | 546 | 🟢 | Python |
| [ninfs](https://github.com/ihaveamac/ninfs) | FUSE filesystem for Nintendo console file formats (3DS, Wii U, Switch) | 544 | 🟢 | Python |
| [RPFM](https://github.com/Frodo45127/rpfm) | Rusted PackFile Manager for Total War game PackFiles | 524 | 🟢 | Rust |
| [redscript](https://github.com/jac3km4/redscript) | Compiler/decompiler toolkit for Cyberpunk 2077's redscript | 520 | 🟢 | Rust |
| [UAssetAPI](https://github.com/atenfyr/UAssetAPI) | Low-level .NET library for reading and writing Unreal Engine assets | 511 | 🟢 | C# |
| [CascLib](https://github.com/ladislav-zezula/CascLib) | Library for reading Blizzard CASC storages | 498 | 🟢 | C++ |
| [QuickBMS](https://github.com/LittleBigBug/QuickBMS) | GitHub mirror of QuickBMS game archive extractor | 497 | 🟡 | C |
| [demofile](https://github.com/saul/demofile) | Node.js parser for CS:GO demo files | 495 | 🗄️ | JavaScript |
| [HiveWE](https://github.com/stijnherfst/HiveWE) | A Warcraft III world editor. | 484 | 🟢 | C++ |
| [OpenKH](https://github.com/OpenKH/OpenKh) | Kingdom Hearts libraries, tools, game engine and format documentation | 455 | 🟢 | C# |
| [pkNX](https://github.com/kwsch/pkNX) | Pokemon (Nintendo Switch) ROM editor and randomizer | 454 | 🟢 | C# |
| [Kuriimu2](https://github.com/FanTranslatorsInternational/Kuriimu2) | Fan translation project manager and game format toolkit | 447 | 🟢 | C# |
| [Blender Niftools Addon](https://github.com/niftools/blender_niftools_addon) | Blender import/export of NetImmerse/Gamebryo NIF files | 436 | 🟡 | Python |
| [FFXIV TexTools](https://github.com/TexTools/FFXIV_TexTools_UI) | Texture and model modding tool for Final Fantasy XIV | 433 | 🟢 | C# |
| [tinke](https://github.com/pleonex/tinke) | Viewer and editor for the files of Nintendo DS games | 429 | 🗄️ | C# |
| [VNTranslationTools](https://github.com/arcusmaximus/VNTranslationTools) | Text extraction and reinsertion tools for many visual novel engines | 424 | 🗄️ | C# |
| [REE.PAK.Tool](https://github.com/Ekey/REE.PAK.Tool) | Extract and repack PAK archives from RE Engine games | 417 | 🟢 | C# |
| [3dstool](https://github.com/dnasdw/3dstool) | All-in-one tool for extracting and creating 3DS ROM formats | 414 | 🟢 | C |
| [ww2ogg](https://github.com/hcs64/ww2ogg) | Converts Wwise RIFF/RIFX Vorbis to standard Ogg Vorbis | 401 | 🟡 | C++ |
| [SaintCoinach](https://github.com/xivapi/SaintCoinach) | .NET library for extracting Final Fantasy XIV game assets and data | 385 | 🟢 | C# |
| [Kuriimu](https://github.com/IcySon55/Kuriimu) | General purpose game file and translation toolkit for fan translators | 375 | 🔴 | C# |
| [wwiser](https://github.com/bnnm/wwiser) | Audiokinetic Wwise .bnk explorer and audio simulator | 374 | 🟢 | Python |
| [LibOrbisPkg](https://github.com/maxton/LibOrbisPkg) | Library and tools for PS4 PKG, SFO and PFS formats | 368 | 🟡 | C# |
| [LibGGPK3](https://github.com/aianlinb/LibGGPK3) | Library for Path of Exile Content.ggpk and bundle files | 343 | 🟢 | C# |
| [N64-Tools](https://github.com/jombo23/N64-Tools) | Tools for ripping and editing N64 game audio, graphics and data formats | 335 | 🟢 | C++ |
| [WoWDBDefs](https://github.com/wowdev/WoWDBDefs) | Client database (DB2) definitions for World of Warcraft | 329 | 🟢 | C# |
| [demoinfo](https://github.com/StatsHelix/demoinfo) | C# library to analyze CS:GO demos | 320 | 🗄️ | C# |
| [SC2k-docs](https://github.com/OpenCity2k/SC2k-docs) | Documentation of SimCity 2000 internals and file formats | 288 | 🟡 |  |
| [Assembly](https://github.com/XboxChaos/Assembly) | Multi-generation Blam engine (Halo) map research and editing tool | 269 | 🟢 | C# |
| [Decima Workshop](https://github.com/ShadelessFox/decima-workshop) | Asset viewer and modding tool for Decima engine games | 266 | 🟢 | Java |
| [VGAudio](https://github.com/Thealexbarney/VGAudio) | Library for encoding and decoding video game audio formats (ADX, HCA, DSP, etc.) | 265 | 🔴 | C# |
| [CriPakTools](https://github.com/esperknight/CriPakTools) | List, extract and update CRIWARE CPK archives | 259 | 🔴 | C# |
| [NMSE](https://github.com/vectorcmdr/NMSE) | Open source save editor for No Man's Sky | 256 | 🟢 | C# |
| [Sims4Tools](https://github.com/s4ptacle/Sims4Tools) | s4pe package editor and tools for The Sims 4 formats | 251 | 🟡 | C# |
| [retoc](https://github.com/trumank/retoc) | Tool for packing and unpacking Unreal Engine IoStore (.utoc/.ucas) containers | 249 | 🟢 | Rust |
| [aoc-mgz](https://github.com/happyleavesaoc/aoc-mgz) | Age of Empires II recorded game parser in Python | 234 | 🟢 | Python |
| [apicula](https://github.com/scurest/apicula) | Extract, view and convert Nintendo DS .nsbmd models | 230 | 🟡 | Rust |
| [NebulaFD](https://github.com/AITYunivers/NebulaFD) | Decompiler for Clickteam Fusion games | 226 | 🟢 | C# |
| [RE-Mesh-Editor](https://github.com/NSACloud/RE-Mesh-Editor) | Blender addon to import/export RE Engine mesh and mdf2 files | 218 | 🗄️ | Python |
| [Tools](https://github.com/bartlomiejduda/Tools) | Tools to extract and modify files from many games | 218 | 🟢 | Python |
| [lsdpatch](https://github.com/jkotlinski/lsdpatch) | LSDj ROM patcher for replacing kits, fonts and palettes | 217 | 🟢 | Java |
| [MeltyTool](https://github.com/MeltyPlayer/MeltyTool) | Multitool to view and extract assets from N64, GameCube, 3DS and PC games | 214 | 🟢 | GLSL |
| [vdf](https://github.com/ValvePython/vdf) | Python package for Valve's text and binary KeyValue (VDF) format | 214 | 🟡 | Python |
| [wow.tools.local](https://github.com/Marlamin/wow.tools.local) | Locally runnable version of wow.tools for browsing WoW data | 209 | 🟢 | C# |
| [BrawlCrate](https://github.com/soopercool101/BrawlCrate) | Wii file editor for Super Smash Bros. Brawl and other BRRES-format games | 208 | 🟢 | C# |
| [Yabber](https://github.com/JKAnderson/Yabber) | Unpacker/repacker for FromSoftware container formats | 206 | 🗄️ | C# |
| [Documentation](https://github.com/Team-Lodestone/Documentation) | Documentation of file formats and mechanics across many Minecraft versions and editions | 203 | 🟢 | TypeScript |
| [GM8Decompiler](https://github.com/OpenGMK/GM8Decompiler) | Decompiler for GameMaker 8.x executables | 201 | 🟡 |  |
| [EveryFileExplorer](https://github.com/Gericom/EveryFileExplorer) | EveryFileExplorer, a viewer and editor for many Nintendo DS and 3DS file formats | 199 | 🔴 | C# |
| [sm64tools](https://github.com/queueRAM/sm64tools) | Collection of tools for Super Mario 64 ROM hacking | 199 | 🟢 | C |
| [SoulsFormats](https://github.com/JKAnderson/SoulsFormats) | .NET library for reading and writing FromSoftware file formats | 197 | 🗄️ | C# |
| [ValveKeyValue](https://github.com/ValveResourceFormat/ValveKeyValue) | .NET library for Valve's KeyValues text and binary formats | 194 | 🟢 | C# |
| [NDSFactory](https://github.com/Luca1991/NDSFactory) | Unpack and repack Nintendo DS ROMs | 192 | 🟢 | C++ |
| [soulstruct-blender](https://github.com/Grimrukh/soulstruct-blender) | Blender plugins for FromSoftware game formats via soulstruct | 190 | 🟢 | Python |
| [PDTools](https://github.com/Nenkai/PDTools) | Tools and libraries for Gran Turismo (Polyphony Digital) file formats | 183 | 🟢 | C# |
| [xvdtool](https://github.com/emoose/xvdtool) | Command-line tool for manipulating Xbox One XVD and XVC files | 179 | 🟢 | C# |
| [Mutagen](https://github.com/Mutagen-Modding/Mutagen) | .NET library for analyzing and creating Bethesda plugin files | 177 | 🟢 | C# |
| [Charm](https://github.com/MontagueM/Charm) | Destiny 2 reverse engineering tool for extracting game files | 175 | 🟢 | C# |
| [GCFT](https://github.com/LagoLunatic/GCFT) | GameCube File Tools GUI for common GameCube game formats | 174 | 🟢 | Python |
| [klo-gba.js](https://github.com/macabeus/klo-gba.js) | Reverse engineering tool and level editor for Klonoa GBA | 166 | 🔴 | JavaScript |
| [seq64](https://github.com/sauraen/seq64) | Sequenced music editor for first-party N64 games | 166 | 🟢 | C++ |
| [rust-u4pak](https://github.com/panzi/rust-u4pak) | Rust tool to unpack, pack and mount Unreal Engine 4 .pak archives | 165 | 🔴 | Rust |
| [d2s](https://github.com/nokka/d2s) | Diablo II save file binary parser in Go | 163 | 🔴 | Go |
| [DSLuaDecompiler](https://github.com/katalash/DSLuaDecompiler) | Lua/HavokScript decompiler for Dark Souls, Bloodborne and Sekiro scripts | 163 | 🟡 | C# |
| [MafiaToolkit](https://github.com/Greavesy1899/MafiaToolkit) | Open source toolkit for Mafia II, III and Definitive Edition files | 157 | 🟢 | C# |
| [UnrealLocres](https://github.com/akintos/UnrealLocres) | Reads and writes Unreal Engine .locres localization files | 157 | 🔴 | C# |
| [GBFRDataTools](https://github.com/Nenkai/GBFRDataTools) | Data tools for Granblue Fantasy: Relink archives and formats | 156 | 🟢 | C# |
| [Legendary Explorer](https://github.com/ME3Tweaks/LegendaryExplorer) | Editor toolset for Mass Effect Trilogy and Legendary Edition packages | 156 | 🟢 | C# |
| [CDTB](https://github.com/CommunityDragon/CDTB) | CommunityDragon toolbox for extracting League of Legends client files | 155 | 🟢 | Python |
| [Cyberpunk-Blender-add-on](https://github.com/WolvenKit/Cyberpunk-Blender-add-on) | Blender add-on for Cyberpunk 2077 asset formats | 154 | 🟢 | Python |
| [Ruri.ShaderDecompiler](https://github.com/ShiyumeMeguri/Ruri.ShaderDecompiler) | Unity shader decompiler | 153 | 🟢 | C# |
| [Smash Forge](https://github.com/jam1garner/Smash-Forge) | Open-source editor for Smash 4 file types | 152 | 🟢 | C# |
| [boxcars](https://github.com/nickbabcock/boxcars) | Rocket League replay parser in Rust | 151 | 🟢 | Rust |
| [Reverence](https://github.com/ntt/reverence) | Python library for EVE Online cache and bulkdata files | 151 | 🔴 | Python |
| [MidiConverters](https://github.com/ValleyBell/MidiConverters) | Tools converting game music data into MIDI files | 146 | 🟢 | C |
| [liblcf](https://github.com/EasyRPG/liblcf) | Library to read and write RPG Maker 2000/2003 data formats | 144 | 🟢 | C++ |
| [sourcepp](https://github.com/craftablescience/sourcepp) | C++ parsers for Source engine and related formats (VPK, VTF, MDL, BSP) | 143 | 🟢 | C++ |
| [FortniteReplayDecompressor](https://github.com/Shiqan/FortniteReplayDecompressor) | Reads Fortnite replay files | 140 | 🟢 | C# |
| [StarBreaker](https://github.com/diogotr7/StarBreaker) | Star Citizen game file reverse engineering toolkit (P4k, DCB) | 140 | 🟢 | Rust |
| [d2s-format](https://github.com/krisives/d2s-format) | Diablo II save file format documentation | 136 | 🟡 |  |
| [Lumina](https://github.com/NotAdam/Lumina) | Framework for reading Final Fantasy XIV game data | 133 | 🟢 | C# |
| [vstools](https://github.com/morris/vstools) | Toolset for Vagrant Story file formats in JavaScript | 132 | 🔴 | JavaScript |
| [Sonic Adventure Toolset](https://github.com/X-Hax/sa_tools) | Sonic Adventure Toolset | 131 | 🟢 | C# |
| [RocketLeagueReplayParser](https://github.com/jjbott/RocketLeagueReplayParser) | Rocket League replay parser in C# | 130 | 🟢 | C# |
| [Quad64](https://github.com/DavidSM64/Quad64) | An open-source Super Mario 64 level editor | 129 | 🔴 | C# |
| [mhrice](https://github.com/wwylele/mhrice) | Monster Hunter Rise data extraction and information website | 127 | 🟢 | Rust |
| [OpenMF-Archived](https://github.com/MafiaHub/OpenMF-Archived) | Format utilities and parsers for Mafia: The City of Lost Heaven | 127 | 🗄️ | C++ |
| [CommunityDragon Docs](https://github.com/CommunityDragon/Docs) | Documentation of League of Legends file formats and data | 124 | 🟡 |  |
| [LeagueToolkit](https://github.com/LeagueToolkit/LeagueToolkit) | Library for parsing and editing League of Legends assets | 124 | 🟢 | C# |
| [DSVEdit](https://github.com/LagoLunatic/DSVEdit) | Multi-purpose ROM hacking editor for DS and GBA Castlevania games | 122 | 🟡 | Ruby |
| [kismet-analyzer](https://github.com/trumank/kismet-analyzer) | Unreal Engine Blueprint/Kismet script reverse engineering and modding utility | 122 | 🟢 | C# |
| [gbx-net](https://github.com/BigBang1112/gbx-net) | Library for Gbx files from Nadeo games like Trackmania | 121 | 🟢 | C# |
| [HedgeLib](https://github.com/Radfordhound/HedgeLib) | C++ library and tools for Sonic the Hedgehog game formats | 121 | 🟢 | C++ |
| [puyotools](https://github.com/nickworonekin/puyotools) | Tools and libraries to access archives and textures in various Sega games' formats | 121 | 🟢 | C# |
| [GTA-V-Script-Decompiler](https://github.com/njames93/GTA-V-Script-Decompiler) | Decompiles GTA V script resources (xsc, csc, ysc) | 118 | 🔴 | C# |
| [ForzaTech-extraction-tools](https://github.com/Doliman100/ForzaTech-extraction-tools) | Reverse engineered .carbin and .modelbin formats from Forza games | 115 | 🟢 | Python |
| [libLSDJ](https://github.com/stijnfrishert/libLSDJ) | Library for working with the LSDj (Little Sound Dj) save file format | 113 | 🟡 | C |
| [NitroPaint](https://github.com/Garhoogin/NitroPaint) | General-purpose Nintendo DS sprite, background and texture editor | 111 | 🟢 | C |
| [Atlus Script Tools](https://github.com/tge-was-taken/Atlus-Script-Tools) | Compiler/decompiler for Atlus flowscript and message script formats | 106 | 🟢 | C# |
| [grand-theft-auto-for-unity](https://github.com/mukaschultze/grand-theft-auto-for-unity) | Loads original Grand Theft Auto map and model formats into Unity | 105 | 🟡 | C# |
| [pfs_upk](https://github.com/nextgal/pfs_upk) | Artemis engine PFS archive packer and unpacker | 105 | 🔴 | C++ |
| [screp](https://github.com/icza/screp) | StarCraft: Brood War replay parser in Go | 104 | 🟢 | Go |
| [playnote-studio](https://github.com/jaames/playnote-studio) | Unofficial Flipnote Studio animation player for the Playdate | 103 | 🟢 | Lua |
| [Texture64](https://github.com/queueRAM/Texture64) | N64 texture ripper and editor | 101 | 🔴 | C# |
| [alkahest](https://github.com/cohaereo/alkahest) | Destiny 2 asset viewer with accurate rendering recreation | 96 | 🟢 | Rust |
| [vgm_ripping](https://github.com/hcs64/vgm_ripping) | Tools for ripping video game music formats | 95 | 🔴 | C |
| [Amicitia](https://github.com/tge-was-taken/Amicitia) | Editor for file formats used in Atlus' Persona games | 92 | 🟡 | C# |
| [ndspy](https://github.com/RoadrunnerWMC/ndspy) | Python library for many Nintendo DS file formats | 90 | 🟢 | Python |
| [PS1-Argonaut-Reverse](https://github.com/OverSurge/PS1-Argonaut-Reverse) | Reverse engineering of Argonaut PS1 game formats (Harry Potter, Croc 2) | 88 | 🟡 | Python |
| [runescape-cache-tools](https://github.com/villermen/runescape-cache-tools) | .NET library and CLI for the RuneScape cache | 86 | 🔴 | C# |
| [SporeModder FX](https://github.com/Spore-Community/SporeModder-FX) | Modding tool for Spore package and data formats | 85 | 🟢 | Java |
| [The Lost Vikings/Blackthorne Tools](https://github.com/RyanMallon/TheLostVikingsTools) | Reverse Engineered Tools/Library for the DOS game The Lost Vikings | 83 | 🔴 | C |
| [GuildWarsMapBrowser](https://github.com/Jonathan-Greve/GuildWarsMapBrowser) | Browse Guild Wars maps from the game's .dat file | 81 | 🟢 | C++ |
| [Makou Reactor](https://github.com/myst6re/makoureactor) | Final Fantasy VII field archive editor | 81 | 🟢 | C++ |
| [xbox-reversing](https://github.com/emoose/xbox-reversing) | Information and parsers for under-documented Xbox 360 structures and file formats | 81 | 🟡 | Python |
| [dat-schema](https://github.com/poe-tool-dev/dat-schema) | Community schema for Path of Exile .dat data files | 78 | 🟢 | TypeScript |
| [RPKG Tool](https://github.com/glacier-modding/RPKG-Tool) | Extracts and repacks Glacier 2 engine RPKG archives (Hitman) | 78 | 🟢 | C++ |
| [HSDLib](https://github.com/Ploaj/HSDLib) | Library for HAL Sysdolphin (HSD) DAT files used in Melee and others | 76 | 🟢 | C# |
| [ImageMagitek](https://github.com/stevemonaco/ImageMagitek) | .NET library for viewing and editing retro console game graphics in ROMs | 74 | 🟢 | C# |
| [w3gjs](https://github.com/PBug90/w3gjs) | Warcraft III replay parser in JavaScript | 73 | 🟢 | TypeScript |
| [Alpha](https://github.com/NotNite/Alpha) | Final Fantasy XIV toolkit for modding and datamining | 72 | 🟢 | C# |
| [dungeon-siege-re](https://github.com/glampert/dungeon-siege-re) | Reverse engineering of Dungeon Siege game asset formats | 72 | 🟢 | C++ |
| [mymcplus](https://github.com/thestr4ng3r/mymcplus) | PlayStation 2 memory card image manager (mymcplus) | 72 | 🗄️ | Python |
| [NeoXResearch](https://github.com/ZhangFengze/NeoXResearch) | Reverse engineering of NetEase's NeoX game engine | 71 | 🔴 | Python |
| [HZDCoreEditor](https://github.com/Nukem9/HZDCoreEditor) | Tools for editing Decima engine files (Horizon Zero Dawn) | 69 | 🔴 | C# |
| [NewWorldUnpacker](https://github.com/MontagueM/NewWorldUnpacker) | .pak unpacker for Amazon's New World | 66 | 🟡 | Python |
| [IG_tools](https://github.com/lennylxx/IG_tools) | Tools to process Innocent Grey and Noesis game files | 65 | 🟢 | C++ |
| [NSMB-Editor](https://github.com/Dirbaio/NSMB-Editor) | Level editor for New Super Mario Bros. DS | 65 | 🔴 | C# |
| [gctools](https://github.com/fuzziqersoftware/gctools) | Video game file translation tools | 60 | 🟡 |  |
| [DarkSoulsIII.FileFormats](https://github.com/Atvaark/DarkSoulsIII.FileFormats) | Dark Souls III archive file format information | 59 | 🔴 |  |
| [SM64DSe](https://github.com/Arisotura/SM64DSe) | Level, text and model editor for Super Mario 64 DS | 59 | 🔴 | C# |
| [DecimaTools](https://github.com/Wunkolo/DecimaTools) | Tools and research for reverse engineering the Decima game engine | 57 | 🔴 | C++ |
| [bayonetta_tools](https://github.com/Kerilk/bayonetta_tools) | Tools for PlatinumGames formats (Bayonetta, Nier Automata) | 56 | 🟢 | Ruby |
| [NitroStudio2](https://github.com/Gota7/NitroStudio2) | Editor for Nintendo DS Nitro sound archives (SDAT, SSEQ, SBNK) | 55 | 🟢 | C# |
| [OpenDriver2Tools](https://github.com/OpenDriver2/OpenDriver2Tools) | Tools for Driver 1 and Driver 2 game formats | 55 | 🟢 | C++ |
| [phoenixtools](https://github.com/Missingmew/phoenixtools) | Tools and documentation for the Ace Attorney game series | 55 | 🟡 | C++ |
| [Silent-Hill](https://github.com/Sparagas/Silent-Hill) | Silent Hill file format reverse engineering | 54 | 🟢 | C |
| [silent-hill-museum](https://github.com/dreamingmoths/silent-hill-museum) | Web museum and viewer of Silent Hill models from the original game files | 54 | 🟢 | TypeScript |
| [gbcamextract](https://github.com/jkbenaim/gbcamextract) | Extracts photos from Game Boy Camera save files | 53 | 🔴 | C |
| [KingsFieldRE](https://github.com/IvanDSM/KingsFieldRE) | King's Field II reverse engineering tools and documentation | 53 | 🔴 | C++ |
| [reevengi-tools](https://github.com/pmandin/reevengi-tools) | Tools to check reverse engineering of Resident Evil file formats | 53 | 🟢 | C |
| [Deling](https://github.com/myst6re/deling) | Final Fantasy VIII field and worldmap archive editor | 52 | 🟢 | C++ |
| [oead](https://github.com/zeldamods/oead) | Library for Nintendo EPD file formats (SARC, BYML, AAMP, Yaz0) | 52 | 🟢 | C++ |
| [Vagrant-Story-Unity-Parser](https://github.com/korobetski/Vagrant-Story-Unity-Parser) | Unity editor scripts that read original Vagrant Story data | 51 | 🟡 | C# |
| [Xbox-Live-Save-Exporter](https://github.com/Tom60chat/Xbox-Live-Save-Exporter) | Exports local saves from Xbox Live and Game Pass PC game containers | 51 | 🟢 | C# |
| [Fmod5Sharp](https://github.com/SamboyCoding/Fmod5Sharp) | Managed decoder for FMOD 5 sound banks (FSB files) | 49 | 🟢 | C# |
| [driver-tools](https://github.com/Fireboyd78/driver-tools) | Modding tools for DRIV3R, Driver: Parallel Lines and Driver: San Francisco | 48 | 🔴 | C# |
| [StudioSB](https://github.com/Ploaj/StudioSB) | Model application for Super Smash Bros. Ultimate formats | 46 | 🔴 | C# |
| [JFortniteParse](https://github.com/FabianFG/JFortniteParse) | Kotlin/Java library to parse Unreal Engine pak/asset files from Fortnite | 45 | 🟢 | Kotlin |
| [ltd-save-editor](https://github.com/alexislours/ltd-save-editor) | Reader, writer and reverse-engineered field schema for Tomodachi Life .sav save files | 45 | 🟢 | TypeScript |
| [Medal-Of-Honor-PSX-File-Viewer](https://github.com/AdrianoDiDio/Medal-Of-Honor-PSX-File-Viewer) | Tools to open and view files from the PSX Medal of Honor games | 45 | 🟢 | C |
| [NDS_Banner_Editor](https://github.com/TheGameratorT/NDS_Banner_Editor) | Tool to make animated Nintendo DS banners | 43 | 🟡 | C++ |
| [DRV3-Sharp](https://github.com/CaptainSwag101/DRV3-Sharp) | Tools for working with Danganronpa V3 PC files | 39 | 🟡 | C# |
| [SilentHillMapExaminer](https://github.com/ItEndsWithTens/SilentHillMapExaminer) | BizHawk utility to reverse engineer the Silent Hill map format | 39 | 🟢 | C# |
| [Torch](https://github.com/HarbourMasters/Torch) | N64 ROM asset extractor and converter used by fan PC ports | 38 | 🟢 | C++ |
| [Inject-pictures-in-your-Game-Boy-Camera-saves](https://github.com/Raphael-Boichot/Inject-pictures-in-your-Game-Boy-Camera-saves) | The Game Boy Camera save format explained, with tools to inject pictures | 37 | 🟢 | MATLAB |
| [gbcam2png](https://github.com/raphnet/gbcam2png) | Convert Game Boy Camera save RAM photos to PNG | 34 | 🔴 | C |
| [MiiJS](https://github.com/Stewared/MiiJS) | JavaScript library for reading, writing and rendering Nintendo Mii data | 32 | 🟢 | JavaScript |
| [PS1-Argonaut-Assets](https://github.com/OverSurge/PS1-Argonaut-Assets) | Extracted textures and 3D models from Argonaut's Croc 2 and Harry Potter PS1 formats | 32 | 🔴 |  |
| [blender-vagrant-story](https://github.com/korobetski/blender-vagrant-story) | Blender add-on importing and exporting Vagrant Story file formats | 29 | 🟡 | Python |
| [AWTools](https://github.com/Nostritius/AWTools) | Tools for reverse-engineered file formats of Alan Wake and later Remedy games | 28 | 🔴 | Python |
| [ZenTools](https://github.com/WistfulHopes/ZenTools-UE4) | Tools for extracting Unreal Engine IoStore (Zen) packages | 28 | 🟡 | C++ |
| [game-boy-camera-manager](https://github.com/marcrobledo/game-boy-camera-manager) | Swiss-army-knife manager for Game Boy Camera save SRAM and ROM | 24 | 🟢 | JavaScript |
| [darkstone-re](https://github.com/glampert/darkstone-re) | Tools to reverse engineer the file formats of the game Darkstone | 21 | 🟢 | C |
| [leotools](https://github.com/jkbenaim/leotools) | Tools for 64DD disk images and the files they contain | 20 | 🔴 | C |
| [ShinDataUtil](https://github.com/DCNick3/ShinDataUtil) | This is an utility for working with game files of Higurashi no Naku Koro ni and Kono Subarashii Sekai ni Shukufuku wo... | 20 | 🟢 | C# |
| [Princed Resources](https://github.com/NagyD/PR) | Princed Resources is a tool to export and import graphics and other data from and to DAT files of Prince of Persia 1... | 19 | 🔴 | C |
| [Siege Studio](https://github.com/open-siege/siege-studio) | Siege Studio is a desktop application for previewing, modifying and converting reverse engineered file formats for ga... | 19 | 🟢 | C++ |
| [MApRX](https://github.com/wwylele/MApRX) | Map editor for Kirby Super Star Ultra (DS) | 17 | 🔴 | C++ |
| [utkencode](https://github.com/daddesio/utkencode) | Encoder for EA MicroTalk, a speech codec based on multi-pulse linear prediction used in various EA games. This encode... | 16 | 🔴 | C |
| [vmu-tools](https://github.com/slurmking/vmu-tools) | Tools to read and modify Dreamcast VMU save files and file types | 15 | 🔴 | Python |
| [TACTSharp](https://github.com/wowdev/TACTSharp) | C# library for Blizzard's TACT/CASC content distribution | 13 | 🟢 | C# |
| [nitro-g3d-tools](https://github.com/Ermelber/nitro-g3d-tools) | Tools to convert models into the Nitro 3D formats used by DS games | 12 | 🔴 | C# |
| [romman](https://github.com/israpps/romman) | Image manager for PlayStation 2 BIOS ROM and IOPRP images | 10 | 🟢 | C++ |
| [smash-arc](https://github.com/jam1garner/smash-arc) | Library for Super Smash Bros. Ultimate's ARC archive format | 9 | 🟡 | Rust |
| [obscura](https://github.com/svendahlstrand/obscura) | Salvage photographs from a Game Boy Camera save file | 7 | 🔴 | C |
| [TD3Extract](https://github.com/yuv422/TD3Extract) | A tool for extracting data files from the game - Test Drive III "The Passion" | 7 | 🔴 | C++ |
| [Fantastic Dizzy Tools](https://github.com/RyanMallon/dizzy) | Reverse engineering tools for Fantastic Dizzy | 6 | 🔴 | Python |
| [mpromtool](https://github.com/gamemasterplc/mpromtool) | Mario Party 1-3 ROM Extractor/Rebuilder Tool | 6 | 🟡 | C++ |
| [blueshell](https://github.com/bbomb64/blueshell) | Cross-platform level editor for New Super Mario Bros. DS | 5 | 🔴 | C++ |
| [FNT-Tool](https://github.com/RoadrunnerWMC/FNT-Tool) | Converts Nintendo DS fnt.bin filename tables to and from JSON | 5 | 🔴 | Python |
| [PokemonDungeonExplorers](https://github.com/pleonex/PokemonDungeonExplorers) | Tools and documentation for the Pokemon Mystery Dungeon Explorers DS games | 5 | 🗄️ | C# |
| [NerdFontTerminatoR](https://github.com/pleonex/NerdFontTerminatoR) | Create, modify and view NFTR font files from Nintendo DS games | 4 | 🗄️ | C# |
| [SADL-Audio-format](https://github.com/pleonex/SADL-Audio-format) | Documentation and tools for the SADL audio format in Nintendo DS games | 4 | 🗄️ | C# |
| [NSBMD-NSBTX_Converter](https://github.com/TheGameratorT/NSBMD-NSBTX_Converter) | Converts models and textures to Nintendo DS NSBMD/NSBTX files | 3 | 🗄️ | C++ |
| [VBEditor](https://github.com/kran27/VBEditor) | A heavily work-in-progress editor for the proprietary file formats used in Fallout Van Buren | 1 | 🗄️ | Visual Basic .NET |
| [Cathedral Assets Optimizer](https://github.com/Guekka/Cathedral_Assets_Optimizer) | Optimizes Bethesda game assets (BSA, NIF, DDS) | 0 | 🔴 |  |
| [gamedefs](https://codeberg.org/modrepository/gamedefs) | Go packages and C headers for reverse-engineered game file formats, structs and constants |  | ⚪ |  |
| [GFXFileManager](https://gitlab.com/florian0/GFXFileManager) | Reverse-engineered interface for Silkroad Online's GFXFileManager.dll with an open implementation |  | ⚪ |  |
| [gta2-scr-decompiler](https://gitlab.com/classic-gta/gta2-scr-decompiler) | Decompiler for GTA2 SCR mission scripts |  | ⚪ |  |
| [kaleido](https://gitlab.com/Neurochitin/kaleido) | Reverse engineering the visual novel Gensou Rougoku no Kaleidoscope, with an SNR script parser |  | ⚪ |  |
| [ncs-decompiler](https://gitlab.com/nwn-utils/ncs-decompiler) | Decompiler for Neverwinter Nights NWScript bytecode |  | ⚪ |  |
| [qbee](https://codeberg.org/lyla/qbee) | Implementation of Neversoft's Q scripting language used in Tony Hawk and Guitar Hero games |  | ⚪ |  |
| [Scrapland-RE](https://gitlab.com/Earthnuker/Scrapland-RE) | Scrapland reverse engineering tools and notes |  | ⚪ |  |
| [strkexeu](https://gitlab.com/NY00123/strkexeu) | Standalone unpacker for Desert/Jungle Strike DOS EXEs with a disassembly of the loader |  | ⚪ |  |
| [untorque](https://gitlab.com/umod/tools/untorque) | Script DSO decompiler for the Torque3D engine |  | ⚪ |  |

## Console Emulators

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [shadPS4](https://github.com/shadps4-emu/shadPS4) | PlayStation 4 emulator for Windows, Linux and macOS | 33,707 | 🟢 | C++ |
| [v86](https://github.com/copy/v86) | v86, an x86 PC emulator and x86-to-wasm JIT running in the browser | 23,586 | 🟢 | JavaScript |
| [RPCS3](https://github.com/RPCS3/rpcs3) | PlayStation 3 emulator and debugger | 20,114 | 🟢 | C++ |
| [PCSX2](https://github.com/PCSX2/pcsx2) | PlayStation 2 emulator | 15,833 | 🟢 | C++ |
| [Dolphin](https://github.com/dolphin-emu/dolphin) | GameCube and Wii emulator | 15,677 | 🟢 | C++ |
| [ppsspp](https://github.com/hrydgard/ppsspp) | PPSSPP, a PSP emulator for Android, Windows, macOS, Linux and iOS | 14,678 | 🟢 | C++ |
| [DuckStation](https://github.com/stenzek/duckstation) | PlayStation 1 emulator focused on accuracy and speed | 10,856 | 🟢 | C++ |
| [mame](https://github.com/mamedev/mame) | MAME, the multi-system arcade and computer emulator | 10,634 | 🟢 | C++ |
| [Cemu](https://github.com/cemu-project/Cemu) | Cemu, a Wii U emulator | 9,996 | 🟢 | C++ |
| [mgba](https://github.com/mgba-emu/mgba) | mGBA, an accurate Game Boy Advance emulator | 7,507 | 🟢 | C |
| [jsnes](https://github.com/bfirsh/jsnes) | jsnes, a JavaScript NES emulator | 6,427 | 🟢 | JavaScript |
| [Vita3K](https://github.com/Vita3K/Vita3K) | Experimental PlayStation Vita emulator | 5,848 | 🟢 | C++ |
| [PyBoy](https://github.com/Baekalfen/PyBoy) | Game Boy emulator written in Python, with an API for scripting and AI agents | 5,227 | 🟢 | Python |
| [melonDS](https://github.com/melonDS-emu/melonDS) | melonDS, a Nintendo DS emulator with DSi and local wireless support | 5,121 | 🟢 | C++ |
| [SimpleNES](https://github.com/amhndu/SimpleNES) | SimpleNES, an NES emulator in C++ | 5,114 | 🟡 | C++ |
| [86Box](https://github.com/86Box/86Box) | 86Box, an emulator of x86-based machines | 4,929 | 🟢 | C |
| [xemu](https://github.com/xemu-project/xemu) | xemu, an original Xbox emulator built on low-level hardware emulation | 4,195 | 🟢 | C |
| [visualboyadvance-m](https://github.com/visualboyadvance-m/visualboyadvance-m) | VisualBoyAdvance-M, a Game Boy Advance emulator | 3,937 | 🟢 | C++ |
| [dosbox-x](https://github.com/joncampbell123/dosbox-x) | DOSBox-X, a DOS and PC-98 emulator | 3,776 | 🟢 | C |
| [desmume](https://github.com/TASEmulators/desmume) | DeSmuME, a Nintendo DS emulator | 3,659 | 🟢 | C++ |
| [orbital](https://github.com/AlexAltea/orbital) | Orbital, an experimental PlayStation 4 emulator | 3,649 | 🟡 | C |
| [snes9x](https://github.com/snes9xgit/snes9x) | Snes9x, a portable Super Nintendo emulator | 3,365 | 🟢 | C++ |
| [Main_MiSTer](https://github.com/MiSTer-devel/Main_MiSTer) | Main binary of MiSTer, the open FPGA platform for recreating retro consoles and computers | 3,303 | 🟢 | C++ |
| [project64](https://github.com/project64/project64) | Project64, a long-running Nintendo 64 emulator for Windows | 3,060 | 🟢 | C++ |
| [BizHawk](https://github.com/TASEmulators/BizHawk) | BizHawk, a multi-system emulator with TAS tools | 2,792 | 🟢 | C# |
| [Play-](https://github.com/jpd002/Play-) | Play!, a PlayStation 2 emulator | 2,712 | 🟢 | C++ |
| [Xenia Canary](https://github.com/xenia-canary/xenia-canary) | Experimental fork of the Xenia Xbox 360 emulator | 2,653 | 🟢 | C++ |
| [flycast](https://github.com/flyinghead/flycast) | Flycast, a Sega Dreamcast, Naomi and Atomiswave emulator | 2,602 | 🟢 | C++ |
| [Mesen2](https://github.com/SourMesen/Mesen2) | Mesen 2, a multi-system emulator (NES, SNES, GB, GBA, PCE, SMS, WS) | 2,416 | 🗄️ | C++ |
| [strato](https://github.com/strato-emu/strato) | Strato, a Nintendo Switch emulator for Android | 2,349 | 🟡 | C++ |
| [SameBoy](https://github.com/LIJI32/SameBoy) | Accuracy-focused Game Boy and Game Boy Color emulator written in C | 2,226 | 🟢 | C |
| [EKA2L1](https://github.com/EKA2L1/EKA2L1) | EKA2L1, a Symbian OS and N-Gage emulator | 2,044 | 🟢 | C++ |
| [GPCS4](https://github.com/Inori/GPCS4) | GPCS4, a work-in-progress PlayStation 4 emulator | 2,033 | 🔴 | C++ |
| [bsnes](https://github.com/bsnes-emu/bsnes) | bsnes, an accuracy-focused Super Nintendo emulator | 2,006 | 🟢 | C++ |
| [metalnes](https://github.com/iaddis/metalnes) | Transistor-level NES simulation | 1,955 | 🔴 | JavaScript |
| [pcem](https://github.com/sarah-walker-pcem/pcem) | PCem, an emulator of vintage x86 PCs | 1,946 | 🟢 | C |
| [simh](https://github.com/simh/simh) | SIMH, the Computer History Simulation Project for historic minicomputers and mainframes | 1,887 | 🟢 | C |
| [melonDS-android](https://github.com/rafaelvcaetano/melonDS-android) | Android port of the melonDS Nintendo DS emulator | 1,698 | 🟢 | Kotlin |
| [macemu](https://github.com/cebix/macemu) | Basilisk II and SheepShaver classic Macintosh emulators | 1,637 | 🟡 | C++ |
| [FBNeo](https://github.com/finalburnneo/FBNeo) | FinalBurn Neo, an arcade and console emulator | 1,541 | 🟢 | C++ |
| [LaiNES](https://github.com/AndreaOrru/LaiNES) | LaiNES, a compact cycle-accurate NES emulator | 1,518 | 🟢 | C++ |
| [Panda3DS](https://github.com/wheremyfoodat/Panda3DS) | HLE 3DS emulator | 1,408 | 🟢 | C++ |
| [higan](https://github.com/higan-emu/higan) | higan, an accuracy-focused multi-system emulator | 1,359 | 🟡 | GLSL |
| [js-dos](https://github.com/caiiiycuk/js-dos) | js-dos, an API for running DOS programs in the browser | 1,341 | 🟢 | TypeScript |
| [Mesen](https://github.com/SourMesen/Mesen) | Mesen, a cross-platform NES/Famicom emulator | 1,326 | 🗄️ | C++ |
| [NanoBoyAdvance](https://github.com/nba-emu/NanoBoyAdvance) | NanoBoyAdvance, a cycle-accurate Game Boy Advance emulator | 1,308 | 🗄️ | C++ |
| [SkyEmu](https://github.com/skylersaleh/SkyEmu) | SkyEmu, a Game Boy Advance, Game Boy and DS emulator | 1,303 | 🟢 | C |
| [gopher64](https://github.com/gopher64/gopher64) | gopher64, a highly compatible Nintendo 64 emulator | 1,299 | 🟢 | Rust |
| [decaf-emu](https://github.com/decaf-emu/decaf-emu) | decaf-emu, a Wii U emulator research project | 1,277 | 🟡 | C++ |
| [pcjs](https://github.com/jeffpar/pcjs) | PCjs, emulations of the original IBM PC and other machines in JavaScript | 1,221 | 🟢 | JavaScript |
| [Gearboy](https://github.com/drhelius/Gearboy) | Gearboy, a Game Boy / Color emulator and debugger | 1,218 | 🟢 | C++ |
| [dosbox-pure](https://github.com/schellingb/dosbox-pure) | DOSBox Pure, a DOSBox fork for libretro | 1,178 | 🟢 |  |
| [simple64](https://github.com/simple64/simple64) | simple64, an accuracy-focused Nintendo 64 emulator based on mupen64plus | 1,178 | 🗄️ | C |
| [metroboy](https://github.com/aappleby/metroboy) | Gate-level simulators and tools for the original Game Boy | 1,172 | 🟡 | C++ |
| [NooDS](https://github.com/Hydr8gon/NooDS) | NooDS, a fast Nintendo DS emulator | 1,164 | 🟢 | C++ |
| [CLK](https://github.com/TomHarte/CLK) | Clock Signal, an emulator of many 8- and 16-bit computers and consoles | 1,144 | 🟢 | C++ |
| [reicast-emulator](https://github.com/skmp/reicast-emulator) | Reicast, a multiplatform Sega Dreamcast emulator | 1,134 | 🗄️ | C++ |
| [RMG](https://github.com/Rosalie241/RMG) | Rosalie's Mupen GUI, a cross-platform mupen64plus-based N64 emulator | 1,125 | 🟢 | C++ |
| [gbajs](https://github.com/endrift/gbajs) | Game Boy Advance emulator in the browser | 1,091 | 🗄️ | JavaScript |
| [ProjectPSX](https://github.com/BluestormDNA/ProjectPSX) | ProjectPSX, an experimental PlayStation emulator in C# | 1,082 | 🟢 | C# |
| [pcsx-redux](https://github.com/grumpycoders/pcsx-redux) | PlayStation 1 emulator and toolset for development and reverse engineering | 1,022 | 🟢 | C++ |
| [mooneye-gb](https://github.com/Gekkio/mooneye-gb) | Game Boy research project and emulator written in Rust | 971 | 🔴 | Rust |
| [Genesis-Plus-GX](https://github.com/ekeeke/Genesis-Plus-GX) | Genesis Plus GX, an accurate Sega 8/16-bit and Mega CD emulator | 967 | 🟢 | C |
| [martypc](https://github.com/dbalsom/martypc) | MartyPC, a cycle-accurate IBM PC/XT/PCjr/Tandy emulator | 946 | 🟢 | Rust |
| [nestopia](https://github.com/0ldsk00l/nestopia) | Nestopia, a cross-platform NES emulator core with GUI | 943 | 🟢 | C++ |
| [AppleWin](https://github.com/AppleWin/AppleWin) | AppleWin, an Apple II emulator for Windows | 938 | 🟢 | C |
| [pce](https://github.com/jsdf/pce) | PCE, emulating the Mac Plus, IBM PC and Atari ST in the browser via WebAssembly | 917 | 🔴 | C |
| [fake-08](https://github.com/jtothebell/fake-08) | Pico-8 player and emulator for console homebrew | 884 | 🟢 | C++ |
| [cen64](https://github.com/n64dev/cen64) | Cycle-accurate Nintendo 64 emulator | 842 | 🟢 | C |
| [puNES](https://github.com/punesemu/puNES) | puNES, a Qt-based NES emulator and NSF player | 826 | 🟢 | C |
| [obliteration](https://github.com/obhq/obliteration) | Experimental open-source PlayStation 4 kernel reimplementation and emulator | 822 | 🟢 | Rust |
| [pinky](https://github.com/koute/pinky) | NES emulator written in Rust | 810 | 🟡 | Rust |
| [halfix](https://github.com/nepx/halfix) | Halfix, an x86 PC emulator that runs natively and in the browser | 789 | 🔴 | C |
| [stella](https://github.com/stella-emu/stella) | Stella, a multi-platform Atari 2600 emulator | 768 | 🟢 | C |
| [jsGB](https://github.com/Two9A/jsGB) | JavaScript emulation of the Game Boy | 752 | 🔴 | JavaScript |
| [bsnes-hd](https://github.com/DerKoun/bsnes-hd) | bsnes fork adding HD Mode 7 and widescreen features | 711 | 🟢 | GLSL |
| [WinUAE](https://github.com/tonioni/WinUAE) | WinUAE, an Amiga emulator for Windows | 691 | 🟢 | C++ |
| [daedalus](https://github.com/DaedalusX64/daedalus) | DaedalusX64, a Nintendo 64 emulator for PSP, Vita and desktop | 688 | 🟢 | C++ |
| [boytacean](https://github.com/joamag/boytacean) | Boytacean, a Game Boy emulator written in Rust | 683 | 🟢 | Rust |
| [N64Wasm](https://github.com/nbarkhina/N64Wasm) | Web-based Nintendo 64 emulator | 678 | 🟡 | C++ |
| [xqemu](https://github.com/xqemu/xqemu) | XQEMU, an original Xbox emulator based on QEMU | 670 | 🔴 | C |
| [Supermodel](https://github.com/trzy/Supermodel) | Sega Model 3 arcade emulator | 665 | 🟢 | C++ |
| [n64js](https://github.com/hulkholden/n64js) | n64js, a Nintendo 64 emulator in JavaScript | 656 | 🟢 | JavaScript |
| [binjgb](https://github.com/binji/binjgb) | Game Boy emulator in C that also runs in the browser | 610 | 🟢 | C |
| [gbe-plus](https://github.com/shonumi/gbe-plus) | DMG/GBC/GBA emulator with experimental NDS support and many peripheral emulations | 598 | 🟢 | C++ |
| [rustation](https://github.com/simias/rustation) | Rustation, a PlayStation emulator in Rust | 585 | 🟢 | Rust |
| [Avocado](https://github.com/JaCzekanski/Avocado) | Avocado, a PlayStation 1 emulator | 583 | 🔴 | C++ |
| [openMSX](https://github.com/openMSX/openMSX) | openMSX, an accuracy-focused MSX emulator | 557 | 🟢 | C++ |
| [VerilogBoy](https://github.com/zephray/VerilogBoy) | VerilogBoy, a Game Boy implemented in Verilog for FPGAs | 548 | 🔴 | Verilog |
| [DSVita](https://github.com/Grarak/DSVita) | Fast Nintendo DS emulator for ARM32 and PS Vita | 531 | 🟢 | Rust |
| [DobieStation](https://github.com/PSI-Rockin/DobieStation) | DobieStation, a PlayStation 2 emulator | 517 | 🔴 | C++ |
| [WebMSX](https://github.com/ppeccin/WebMSX) | WebMSX, an online MSX emulator | 480 | 🟢 | HTML |
| [GameLad](https://github.com/Dooskington/GameLad) | GameLad, an almost fully featured Game Boy emulator | 464 | 🟢 | C++ |
| [jsmess](https://github.com/jsmess/jsmess) | Efforts to port MESS to JavaScript | 447 | 🔴 | Shell |
| [pearpc](https://github.com/sebastianbiallas/pearpc) | PearPC, a PowerPC architecture emulator | 443 | 🟢 | C++ |
| [zesarux](https://github.com/chernandezba/zesarux) | ZEsarUX, a ZX Spectrum and Z88 emulator | 436 | 🟢 | C |
| [NP2kai](https://github.com/AZO234/NP2kai) | Neko Project II kai, an NEC PC-9801 emulator | 433 | 🟢 | C |
| [atari800](https://github.com/atari800/atari800) | Atari 8-bit computer and 5200 console emulator | 431 | 🟢 | C |
| [DaedalusX64-vitaGL](https://github.com/Rinnegatamante/DaedalusX64-vitaGL) | DaedalusX64 Nintendo 64 emulator ported to PS Vita through vitaGL | 428 | 🟢 | C++ |
| [mikage-dev](https://github.com/mikage-emu/mikage-dev) | Mikage Developer Edition | 421 | 🟡 | C++ |
| [Mesen-S](https://github.com/SourMesen/Mesen-S) | Mesen-S, a cross-platform SNES emulator | 417 | 🗄️ | C++ |
| [vAmiga](https://github.com/dirkwhoffmann/vAmiga) | vAmiga, an Amiga 500/1000/2000 emulator for macOS | 411 | 🟢 | C++ |
| [ANESE](https://github.com/daniel5151/ANESE) | ANESE, an NES emulator and first implementation of wideNES | 403 | 🔴 | C++ |
| [prosperity](https://github.com/Force67/prosperity) | Experimental emulator for Sony PS4 and PS5 consoles | 403 | 🟢 | C++ |
| [gambatte](https://github.com/sinamas/gambatte) | Gambatte, an accuracy-focused Game Boy Color emulator | 400 | 🔴 |  |
| [Gearsystem](https://github.com/drhelius/Gearsystem) | Gearsystem, a Sega Master System / Game Gear / SG-1000 emulator and debugger | 395 | 🟢 | C++ |
| [jsbeeb](https://github.com/mattgodbolt/jsbeeb) | jsbeeb, a JavaScript BBC Micro emulator | 394 | 🟢 | JavaScript |
| [Ishiiruka](https://github.com/Tinob/Ishiiruka) | Ishiiruka, a performance-focused Dolphin-based GameCube/Wii emulator | 373 | 🔴 | C++ |
| [not64](https://github.com/extremscorner/not64) | not64, an N64 emulator for GameCube and Wii based on Mupen64GC | 370 | 🟢 | C |
| [bsnes-plus](https://github.com/devinacker/bsnes-plus) | Debug-oriented fork of the bsnes SNES emulator | 365 | 🟡 | C++ |
| [meka](https://github.com/ocornut/meka) | MEKA, a Sega 8-bit emulator with debugging and hacking tools | 356 | 🟢 | C++ |
| [ScriptedAmigaEmulator](https://github.com/naTmeg/ScriptedAmigaEmulator) | Scripted Amiga Emulator in JavaScript and HTML5 | 354 | 🔴 | JavaScript |
| [wabbitemu](https://github.com/sputt/wabbitemu) | Wabbitemu, a Z80 TI calculator emulator | 334 | 🟢 | C |
| [sodium64](https://github.com/Hydr8gon/sodium64) | SNES emulator for the Nintendo 64, written in assembly | 333 | 🟡 | Assembly |
| [1964GEPD](https://github.com/Graslu/1964GEPD) | 1964 N64 emulator build tuned for GoldenEye 007 and Perfect Dark | 321 | 🗄️ | C |
| [Nuked-MD-FPGA](https://github.com/nukeykt/Nuked-MD-FPGA) | Mega Drive/Genesis Verilog core derived from die-level reverse engineering | 318 | 🟡 | Verilog |
| [Xenon](https://github.com/xenon-emu/xenon) | Low-level Xbox 360 emulator for researching Xenon hardware | 316 | 🟢 | C++ |
| [gameroy](https://github.com/Rodrigodd/gameroy) | Game Boy emulator, disassembler and debugger in Rust | 314 | 🟡 | Rust |
| [pinmame](https://github.com/vpinball/pinmame) | PinMAME, an emulator for pinball machine hardware | 311 | 🟢 | C |
| [IodineGBA](https://github.com/taisel/IodineGBA) | IodineGBA, a JavaScript Game Boy Advance emulator | 296 | 🔴 | JavaScript |
| [FBAlpha](https://github.com/barry65536/FBAlpha) | FB Alpha, an arcade emulator | 283 | 🗄️ | C++ |
| [Corgi3DS](https://github.com/PSI-Rockin/Corgi3DS) | Corgi3DS, a low-level Nintendo 3DS emulator | 249 | 🔴 | C++ |
| [enge-js](https://github.com/kootstra-rene/enge-js) | eNGE, a JavaScript PlayStation emulator | 246 | 🟢 | JavaScript |
| [ContrAlto](https://github.com/livingcomputermuseum/ContrAlto) | ContrAlto, an emulator of the Xerox Alto | 242 | 🟢 | C# |
| [flycast-dojo](https://github.com/blueminder/flycast-dojo) | Flycast fork with online netplay for Dreamcast, Naomi and Atomiswave games | 242 | 🟢 | C++ |
| [javatari.js](https://github.com/ppeccin/javatari.js) | Javatari, an online Atari 2600 emulator | 241 | 🟡 | HTML |
| [rustual-boy](https://github.com/emu-rs/rustual-boy) | Rustual Boy, a Virtual Boy emulator | 232 | 🗄️ | Rust |
| [MedNES](https://github.com/wpmed92/MedNES) | MedNES, a cycle-accurate cross-platform NES emulator | 226 | 🔴 | C++ |
| [breaks](https://github.com/emu-russia/breaks) | Transistor-level reverse engineering of NES/Famicom chips | 222 | 🟢 | Verilog |
| [xnes](https://github.com/tjwei/xnes) | JavaScript SNES emulator | 213 | 🔴 | C++ |
| [giibiiadvance](https://github.com/AntonioND/giibiiadvance) | GB, GBC and GBA emulator with Game Boy Camera support | 208 | 🟢 | C |
| [Mu](https://github.com/meepingsnesroms/Mu) | Mu, a Palm OS emulator | 206 | 🟡 | C |
| [pureikyubu](https://github.com/emu-russia/pureikyubu) | Nintendo GameCube emulator | 196 | 🟢 | C++ |
| [fpg1](https://github.com/hrvach/fpg1) | FPGA implementation of the DEC PDP-1 in Verilog | 195 | 🔴 | Verilog |
| [XTulator](https://github.com/mikechambers84/XTulator) | XTulator, a portable open-source 8086 PC emulator | 192 | 🟡 | C |
| [3dmoo](https://github.com/plutooo/3dmoo) | Early Nintendo 3DS emulator prototype | 186 | 🔴 | C |
| [Emulator.NES](https://github.com/Xyene/Emulator.NES) | Nintendo Entertainment System emulator written in C# | 186 | 🔴 | C# |
| [n64](https://github.com/Dillonb/n64) | Experimental low-level Nintendo 64 emulator | 186 | 🟢 | C++ |
| [nullDC-v1](https://github.com/skmp/nullDC-v1) | nullDC, a Sega Dreamcast emulator | 186 | 🗄️ | C++ |
| [Nuked-MD](https://github.com/nukeykt/Nuked-MD) | Cycle-accurate Mega Drive emulator from die-level reverse engineering | 185 | 🟢 | C |
| [r64emu](https://github.com/rasky/r64emu) | Nintendo 64 emulator written in Rust | 177 | 🔴 | Rust |
| [GBA_MiSTer](https://github.com/MiSTer-devel/GBA_MiSTer) | Game Boy Advance core for the MiSTer FPGA platform | 176 | 🟢 | VHDL |
| [jsspeccy3](https://github.com/gasman/jsspeccy3) | jsspeccy, a ZX Spectrum emulator for the browser | 169 | 🟢 | JavaScript |
| [vice.js](https://github.com/rjanicek/vice.js) | VICE Commodore emulator compiled to JavaScript | 166 | 🔴 | Shell |
| [psxrev](https://github.com/emu-russia/psxrev) | Sony PlayStation PCB and chip reverse engineering | 160 | 🟡 | C# |
| [jsSMS](https://github.com/gmarty/jsSMS) | JavaScript Sega Master System and Game Gear dynamic recompiling emulator | 152 | 🔴 | JavaScript |
| [neschan](https://github.com/yizhang82/neschan) | NES emulator written in C++ | 151 | 🟡 | C++ |
| [b2](https://github.com/tom-seddon/b2) | b2, a BBC Micro emulator for Windows, macOS and Linux | 140 | 🟢 | C++ |
| [jsgs](https://github.com/burakcan/jsgs) | JavaScript reimplementation of the closed Pico-8 fantasy console | 140 | 🔴 | JavaScript |
| [b-em](https://github.com/stardot/b-em) | B-em, a BBC Micro emulator | 136 | 🟢 | C |
| [r3Ddragon](https://github.com/mrdanielps/r3Ddragon) | Virtual Boy emulator for the Nintendo 3DS | 130 | 🗄️ | C |
| [NGEmu](https://github.com/NGEmu/NGEmu) | NGEmu, a Nokia N-Gage emulator | 127 | 🗄️ | C++ |
| [Arduino-C64-Emulator](https://github.com/michalin/Arduino-C64-Emulator) | Commodore 64 emulator running on an Arduino | 121 | 🔴 | C |
| [PPU-LITE](https://github.com/andkorzh/PPU-LITE) | Clock-accurate FPGA replacement for the NES PPU from reverse engineering | 120 | 🟢 | Verilog |
| [gb64](https://github.com/lambertjamesd/gb64) | Game Boy emulator that runs on real N64 hardware | 111 | 🟡 | C |
| [lcdgame.js](https://github.com/BdR76/lcdgame.js) | Library that recreates 1980s Game & Watch LCD games in HTML5 | 108 | 🟡 | JavaScript |
| [px68k](https://github.com/hissorii/px68k) | Portable Sharp X68000 emulator | 105 | 🔴 | C |
| [rokuyon](https://github.com/Hydr8gon/rokuyon) | rokuyon, an experimental N64 emulator | 105 | 🟢 | C++ |
| [jspspemu](https://github.com/soywiz-archive/jspspemu) | TypeScript PSP emulator | 102 | 🗄️ | TypeScript |
| [fpgaboy](https://github.com/trun/fpgaboy) | Implementation of Nintendo's Game Boy console on an FPGA | 99 | 🔴 | Verilog |
| [WinFellow](https://github.com/petschau/WinFellow) | WinFellow, an Amiga emulator for Windows | 97 | 🟢 | C |
| [CeDImu](https://github.com/Stovent/CeDImu) | Experimental Philips CD-i emulator in C++ | 96 | 🟢 | C++ |
| [hhugboy](https://github.com/tzlion/hhugboy) | Game Boy (Color) emulator with support for unlicensed mappers | 94 | 🟢 | C++ |
| [NuanceResurrection](https://github.com/andkrau/NuanceResurrection) | Nuance Resurrection, a Nuon console emulator | 93 | 🟢 | C++ |
| [raine](https://github.com/zelurker/raine) | Raine, an arcade emulator | 93 | 🟢 | C |
| [Wii-U-Firmware-Emulator](https://github.com/kinnay/Wii-U-Firmware-Emulator) | Emulates the Wii U's IOSU and part of Cafe OS | 93 | 🟡 | C++ |
| [oricutron](https://github.com/pete-gordon/oricutron) | Oricutron, an Oric-1/Atmos/Telestrat emulator | 90 | 🟢 | C |
| [wpc-emu](https://github.com/neophob/wpc-emu) | Williams WPC pinball machine emulator | 89 | 🟢 | JavaScript |
| [retro-b5500](https://github.com/pkimpel/retro-b5500) | Web-based emulator for the Burroughs B5500 mainframe | 81 | 🟡 | JavaScript |
| [ChonkyStation](https://github.com/liuk7071/ChonkyStation) | ChonkyStation, a PlayStation 1 emulator | 79 | 🟡 | C++ |
| [simcoupe](https://github.com/simonowen/simcoupe) | SimCoupe, a SAM Coupe emulator | 79 | 🟢 | C++ |
| [1964js](https://github.com/schibo/1964js) | Nintendo 64 emulator in JavaScript | 77 | 🟡 | CoffeeScript |
| [VisualNes](https://github.com/SourMesen/VisualNes) | Visual NES, simulating the NES CPU and PPU at transistor level | 77 | 🗄️ | C# |
| [libevmu](https://github.com/gyrovorbis/libevmu) | Accurate cross-platform library emulating the Dreamcast Visual Memory Unit (VMU) | 76 | 🟢 | C |
| [NitroSwan](https://github.com/FluBBaOfWard/NitroSwan) | WonderSwan and PocketChallenge V2 emulator for the Nintendo DS | 76 | 🟢 | C |
| [kpspemu](https://github.com/soywiz-archive/kpspemu) | PSP emulator written in Kotlin for JVM, JS and native | 75 | 🗄️ | Kotlin |
| [DSHBA](https://github.com/DenSinH/DSHBA) | Highly performant GBA emulator with a hardware renderer | 71 | 🔴 | C++ |
| [Cxbx-Reloaded](https://github.com/Cxbx-Reloaded/Cxbx-Reloaded) | Original Xbox emulator via HLE of reverse engineered XDK libraries | 70 | 🟢 | C++ |
| [SEGAChips](https://github.com/emu-russia/SEGAChips) | Reverse engineering of SEGA chips | 69 | 🟢 | Verilog |
| [ColecoDS](https://github.com/wavemotion-dave/ColecoDS) | ColecoVision emulator for the Nintendo DS/DSi | 63 | 🟢 | C |
| [PCSX-Reloaded](https://github.com/pcsxr/PCSX-Reloaded) | Mirror of PCSX-Reloaded, a PlayStation emulator | 62 | 🔴 | C |
| [nintendulator](https://github.com/quietust/nintendulator) | Nintendulator, an accurate NES emulator for Windows | 58 | 🟢 | C++ |
| [gngeo](https://github.com/linuxlinks/gngeo) | GnGeo, a Neo Geo emulator for Linux | 56 | 🔴 | Assembly |
| [cor64](https://github.com/bdragoncore/cor64) | N64 Emulator written in C# | 55 | 🟡 | C# |
| [StrikeBox](https://github.com/StrikerX3/StrikeBox) | StrikeBox, an original Xbox emulator | 55 | 🔴 | C++ |
| [Felix](https://github.com/laoo/Felix) | Felix, an Atari Lynx emulator | 53 | 🟡 | C++ |
| [js99er-angular](https://github.com/Rasmus-M/js99er-angular) | TI-99/4A emulator written in TypeScript | 52 | 🟢 | TypeScript |
| [dmgcpu](https://github.com/emu-russia/dmgcpu) | Reverse engineering of the Game Boy DMG CPU from the die | 48 | 🟢 | Verilog |
| [StoicGoose](https://github.com/xdanieldzd/StoicGoose) | WonderSwan and WonderSwan Color emulator in C# | 48 | 🟢 | C# |
| [Ryu64](https://github.com/Ryu64Emulator/Ryu64) | Nintendo 64 emulator written in C# | 45 | 🗄️ | C# |
| [FreeIntv](https://github.com/libretro/FreeIntv) | Libretro emulation core for the Mattel Intellivision | 44 | 🟢 | C |
| [lxdream](https://github.com/lxdream/lxdream) | Lxdream, a Sega Dreamcast emulator | 41 | 🔴 | C |
| [KanaStation](https://github.com/noumidev/KanaStation) | Experimental low-level PlayStation Portable emulator | 40 | 🟢 | C++ |
| [SNES_S-CPU_Schematics](https://github.com/rgalland/SNES_S-CPU_Schematics) | Reverse engineering of the SNES CPU from die shots | 40 | 🟡 | KiCad Schematic |
| [mvs64](https://github.com/rasky/mvs64) | Neo Geo emulator for the Nintendo 64 | 39 | 🟡 | C |
| [ProSystem1_3](https://github.com/gstanton/ProSystem1_3) | ProSystem, an Atari 7800 emulator | 39 | 🔴 | C++ |
| [DotN64](https://github.com/Nabile-Rahmani/DotN64) | Nintendo 64 emulator in C# | 38 | 🔴 | C# |
| [hyperscan-emulator](https://github.com/LiraNuna/hyperscan-emulator) | Emulator for the Mattel HyperScan console | 34 | 🟢 | C++ |
| [unununium](https://github.com/RebeccaRGB/unununium) | Disassembler and emulator for the Sunplus u'nSP CPU used in V.Smile and other toys | 34 | 🔴 | C |
| [kamo64](https://github.com/kmc-jp/kamo64) | Low-level Nintendo 64 emulator | 30 | 🟢 | C++ |
| [QuickNES](https://github.com/kode54/QuickNES) | QuickNES, a fast NES emulator | 27 | 🗄️ |  |
| [biostation](https://github.com/Ravenslofty/biostation) | Clean-room PlayStation 2 BIOS | 26 | 🔴 | Assembly |
| [zakuro](https://github.com/fearkov/zakuro) | A Nintendo 3DS emulator in Rust, using AOT recompilation | 24 | 🟢 | Rust |
| [pockystation](https://github.com/simias/pockystation) | Sony PocketStation emulator | 23 | 🟢 | Rust |
| [MoRePhun](https://github.com/Luca1991/MoRePhun) | Experimental emulator for the MoPhun mobile game platform | 18 | 🔴 | C++ |
| [Model2EmuEx](https://github.com/octavioCuatrochio/Model2EmuEx) | Decompiled Sega Model 2 emulator modified to run on Linux and Android | 16 | 🟢 | C |
| [papiGB](https://github.com/diegovalverde/papiGB) | Game Boy Classic FPGA implementation built from scratch | 16 | 🔴 | Verilog |
| [GA330-libretro](https://github.com/minexew/GA330-libretro) | Libretro core emulating the Gemei A330 handheld | 15 | 🔴 | C |
| [libgpu2](https://github.com/aap/libgpu2) | Reverse-engineered reference implementation of the PS2 Graphics Synthesizer | 14 | 🟢 | C |
| [wangemu](https://github.com/jtbattle/wangemu) | Wang 2200 computer emulator | 14 | 🔴 | C++ |
| [gambatte](https://github.com/gb-archive/gambatte) | Public mirror of the Gambatte accuracy-focused Game Boy Color emulator | 8 | 🔴 | Assembly |
| [Symulator3](https://github.com/GregorJ101/Symulator3) | IBM System/3 simulator and code disassembler | 6 | 🔴 | C# |
| [Snaggletooth](https://github.com/etroimcasso/Snaggletooth) | An embeddable, clean-room MIT-licensed SNES (5A22 + SPC700) virtual machine, with a source-recovery and decompilation... | 5 | 🟢 | C++ |
| [cps2-reverse](https://gitlab.com/loic.petit/cps2-reverse) | Capcom CPS2 arcade hardware reverse engineering project |  | ⚪ |  |
| [Hatari](https://framagit.org/hatari/hatari) | Atari ST/STE/TT/Falcon emulator |  | ⚪ |  |
| [VICE](https://sourceforge.net/projects/vice-emu/) | Versatile Commodore emulator for the C64, C128, VIC-20, PET and Plus/4 |  | ⚪ |  |
| [vmiv](https://codeberg.org/Sprite_tm/vmiv) | ViewMaster Interactive Vision emulator and reverse engineering |  | ⚪ |  |

## Engine Reimplementations

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [OpenRA](https://github.com/OpenRA/OpenRA) | RTS engine reimplementing early Westwood games such as C&C Red Alert | 17,585 | 🟢 | C# |
| [OpenRCT2](https://github.com/OpenRCT2/OpenRCT2) | Open-source reimplementation of RollerCoaster Tycoon 2 | 16,450 | 🟢 | C++ |
| [openage](https://github.com/SFTtech/openage) | Free clone of the Genie engine used by Age of Empires II | 14,517 | 🟢 | Python |
| [OpenDiablo2](https://github.com/OpenDiablo2/OpenDiablo2) | Open-source re-implementation of Diablo 2 | 11,107 | 🗄️ | Go |
| [DevilutionX](https://github.com/diasurgical/DevilutionX) | Diablo and Hellfire port for modern systems built on the Devilution reverse engineering | 9,891 | 🟢 | C++ |
| [OpenTTD](https://github.com/OpenTTD/OpenTTD) | Open-source transport simulation game based on Transport Tycoon Deluxe | 8,381 | 🟢 | C++ |
| [OpenMW](https://github.com/OpenMW/openmw) | Open-source engine reimplementation for The Elder Scrolls III: Morrowind | 6,644 | 🟢 | C++ |
| [VCMI](https://github.com/vcmi/vcmi) | Open-source engine for Heroes of Might and Magic III | 5,955 | 🟢 | C++ |
| [RuneLite](https://github.com/runelite/runelite) | Open source Old School RuneScape client | 5,494 | 🟢 | Java |
| [OpenSC2K](https://github.com/OpenSC2K/OpenSC2K) | OpenSC2K - Open Source remake of Sim City 2000 using rust and godot. Available for macOS, Windows and Linux | 5,308 | 🟢 | Rust |
| [OpenLara](https://github.com/XProger/OpenLara) | Classic Tomb Raider open-source engine | 5,127 | 🟢 | C |
| [zelda3](https://github.com/snesrev/zelda3) | C reimplementation of Zelda: A Link to the Past from reverse-engineered SNES code | 4,874 | 🟢 | C |
| [CorsixTH](https://github.com/CorsixTH/CorsixTH) | Open-source clone of Theme Hospital | 4,598 | 🟢 | Lua |
| [PythonPlantsVsZombies](https://github.com/marblexu/PythonPlantsVsZombies) | a simple PlantsVsZombies game | 3,769 | 🟡 | Python |
| [OpenXRay](https://github.com/OpenXRay/xray-16) | Improved version of the X-Ray Engine, the game engine used in the world-famous S.T.A.L.K.E.R. game series by GSC Game... | 3,588 | 🟢 | C++ |
| [OpenGOAL (jak-project)](https://github.com/open-goal/jak-project) | Reimplements the GOAL language/runtime to port Jak and Daxter 1-3 to PC | 3,582 | 🟢 | Common Lisp |
| [Daggerfall Unity](https://github.com/Interkarma/daggerfall-unity) | Recreation of The Elder Scrolls II: Daggerfall in Unity | 3,533 | 🟢 | C# |
| [fheroes2](https://github.com/ihhub/fheroes2) | Recreation of the Heroes of Might and Magic II game engine | 3,509 | 🟢 | C++ |
| [Julius](https://github.com/bvschaik/julius) | Open-source reimplementation of Caesar III with the original game logic | 3,401 | 🟢 | C |
| [Super Mario Bros Remastered](https://github.com/JHDev2006/Super-Mario-Bros.-Remastered-Public) | A Remake / Celebration of the original 'Super Mario Bros.' games. Features new levels, custom modes, new characters,... | 3,227 | 🟢 | GDScript |
| [WipEout (wipeout-rewrite)](https://github.com/phoboslab/wipeout-rewrite) | Reverse-engineered reimplementation / port of WipEout (wipeout-rewrite) | 2,982 | 🟢 | C |
| [kys-cpp](https://github.com/scarsty/kys-cpp) | 《金庸群侠传》c++复刻版，已完工 | 2,969 | 🟢 | C++ |
| [Fallout Community Edition](https://github.com/alexbatalov/fallout1-ce) | Fully working reimplementation of Fallout 1 engine | 2,948 | 🟡 | C++ |
| [ScummVM](https://github.com/scummvm/scummvm) | Reimplements engines of classic point-and-click adventure games | 2,858 | 🟢 | C++ |
| [Xash3D FWGS](https://github.com/FWGS/xash3d-fwgs) | Open-source reimplementation of the GoldSrc engine that runs Half-Life | 2,854 | 🟢 | C |
| [ioquake3](https://github.com/ioquake/ioq3) | Community continuation of id's Quake III Arena engine | 2,850 | 🟢 | C |
| [SanAndreasUnity](https://github.com/in0finite/SanAndreasUnity) | Open source reimplementation of GTA San Andreas game engine in Unity | 2,651 | 🔴 | C# |
| [Fallout 2 CE](https://github.com/alexbatalov/fallout2-ce) | Fallout 2 engine re-implementation for modern desktop and mobile | 2,464 | 🟡 | C++ |
| [OpenJK](https://github.com/JACoders/OpenJK) | Community-maintained Jedi Academy / Jedi Outcast engine | 2,307 | 🟢 | C++ |
| [OpenRW](https://github.com/rwengine/openrw) | Open-source re-implementation of Rockstar's GTA III | 2,242 | 🟡 | C++ |
| [OpenXcom](https://github.com/OpenXcom/OpenXcom) | Open-source clone of UFO: Enemy Unknown and X-COM: Terror from the Deep | 2,233 | 🟢 | C++ |
| [Freeablo](https://github.com/wheybags/freeablo) | Open-source implementation of the Diablo engine. | 2,170 | 🔴 | C++ |
| [Augustus](https://github.com/Keriew/augustus) | An open source re-implementation of Caesar III | 2,121 | 🟢 | C |
| [ClassiCube](https://github.com/ClassiCube/ClassiCube) | Custom Minecraft Classic-compatible game client in C | 2,079 | 🟢 | C |
| [SDLPAL](https://github.com/sdlpal/sdlpal) | SDL-based reimplementation of the classic Chinese-language RPG known as PAL. | 1,983 | 🟢 | C |
| [OpenLoco](https://github.com/OpenLoco/OpenLoco) | Open-source reimplementation of Chris Sawyer's Locomotion | 1,941 | 🟢 | C++ |
| [Hematite](https://github.com/PistonDevelopers/hematite) | A simple Minecraft written in Rust with the Piston game engine | 1,918 | 🟢 | Rust |
| [OpenDUNE](https://github.com/OpenDUNE/OpenDUNE) | Recreation of the popular game Dune II. | 1,696 | 🟢 | C |
| [Pokémon Polished Crystal](https://github.com/Rangi42/polishedcrystal) | An upgrade to Pokémon Crystal. Brings features and content up to date, and adds some original content. | 1,673 | 🟢 | Assembly |
| [roBrowser](https://github.com/vthibault/roBrowser) | Ragnarok Online client reimplemented for web browsers in JavaScript/WebGL | 1,658 | 🗄️ | JavaScript |
| [Clumsy Bird](https://github.com/ellisonleao/clumsy-bird) | :bird: :video_game: A MelonJS port of the famous Flappy Bird Game | 1,630 | 🗄️ | JavaScript |
| [OpenGothic](https://github.com/Try/OpenGothic) | Open-source reimplementation of Gothic I and II | 1,624 | 🟢 | C++ |
| [Ikemen GO](https://github.com/ikemen-engine/Ikemen-GO) | Open-source reimplementation of the MUGEN fighting game engine | 1,623 | 🟢 | Go |
| [openblack](https://github.com/openblack/openblack) | Open-source reimplementation of Black & White (2001) | 1,585 | 🟢 | C++ |
| [OpenTomb](https://github.com/opentomb/OpenTomb) | Open-source Tomb Raider 1-5 engine remake (archived) | 1,445 | 🗄️ | C++ |
| [OpenTESArena](https://github.com/afritz1/OpenTESArena) | Modern engine reimplementation of The Elder Scrolls: Arena by Bethesda Softworks. | 1,432 | 🟢 | C++ |
| [doukutsu-rs](https://github.com/doukutsu-rs/doukutsu-rs) | Rust reimplementation of the Cave Story engine | 1,314 | 🟢 | Rust |
| [Minosoft](https://github.com/Bixilon/Minosoft) | Open source Minecraft client reimplementation written from scratch | 1,313 | 🟢 | Kotlin |
| [GemRB](https://github.com/gemrb/gemrb) | Portable open-source reimplementation of the Infinity Engine (used by Baldur's Gate, Icewind Dale and more). | 1,263 | 🟢 | C++ |
| [Diablerie](https://github.com/mofr/Diablerie) | Diablo 2 reimplementation on unity | 1,240 | 🔴 | C# |
| [Player](https://github.com/EasyRPG/Player) | EasyRPG Player, an open reimplementation of the RPG Maker 2000/2003 runtime | 1,236 | 🟢 | C++ |
| [Carmageddon (dethrace)](https://github.com/dethrace-labs/dethrace) | Reverse-engineered reimplementation / port of Carmageddon (dethrace) | 1,222 | 🟢 | C |
| [xoreos](https://github.com/xoreos/xoreos) | Reimplementation of BioWare's Aurora engine (KotOR, NWN, Jade Empire) | 1,185 | 🟢 | C++ |
| [The Force Engine](https://github.com/TheForceEngine/TheForceEngine) | Reimplementation of LucasArts' Jedi engine for Dark Forces and Outlaws | 1,167 | 🟢 | C++ |
| [RA2](https://github.com/OpenRA/ra2) | A Red Alert 2 mod for the OpenRA game engine | 1,138 | 🟢 | C# |
| [SurrealEngine](https://github.com/dpjudas/SurrealEngine) | Open-source reimplementation of Unreal Engine 1 that plays Unreal Tournament 99 | 1,118 | 🟢 | C++ |
| [Riiablo](https://github.com/collinsmith/riiablo) | Diablo II remade using Java and LibGDX | 1,105 | 🟡 | Java |
| [pikachu-volleyball](https://github.com/gorisanson/pikachu-volleyball) | Pikachu Volleyball reimplemented in JavaScript by reverse engineering the original game | 1,089 | 🟢 | JavaScript |
| [OpenHV](https://github.com/OpenHV/OpenHV) | Open-source implementation of Hard Vacuum. | 1,082 | 🟢 | C# |
| [Pal3.Unity](https://github.com/0x7c13/Pal3.Unity) | Unity reimplementation of The Legend of Sword and Fairy 3 and its expansion | 1,057 | 🟢 | C# |
| [RA2Web React](https://github.com/huangkaoya/ts-redalert2) | 红色警戒2源代码 Red Alert2 Source Code | 1,014 | 🟢 | TypeScript |
| [Tomb Raider I & II (TRX)](https://github.com/LostArtefacts/TRX) | Reverse-engineered reimplementation / port of Tomb Raider I & II (TRX) | 1,012 | 🟢 | C |
| [RigelEngine](https://github.com/lethal-guitar/RigelEngine) | Modern re-implementation of Duke Nukem II | 1,008 | 🟢 | C++ |
| [FreeSO](https://github.com/riperiperi/FreeSO) | Reimplementation of The Sims Online, targetted mainly at mobile devices. | 986 | 🟢 | C# |
| [Crispy Doom](https://github.com/fabiangreffrath/crispy-doom) | Crispy Doom is a limit-removing enhanced-resolution Doom source port based on Chocolate Doom. | 963 | 🟢 | C |
| [NEO-RAW](https://github.com/fabiensanglard/Another-World-Bytecode-Interpreter) | "Fabother World" an interpreter for Another World (Out of this world). | 920 | 🟡 | C++ |
| [PICOLOVE](https://github.com/picolove/picolove) | PICO-8 fantasy console reimplementation in LÖVE | 891 | 🟡 | Lua |
| [Raze](https://github.com/ZDoom/Raze) | Build engine port backed by GZDoom tech. Currently supports Duke Nukem 3D, Blood, Shadow Warrior, Redneck Rampage and... | 889 | 🟢 | C++ |
| [Falltergeist](https://github.com/falltergeist/falltergeist) | Opensource crossplatform Fallout 2™ game engine writen in C++ and SDL. | 887 | 🔴 | C++ |
| [Cannonball](https://github.com/djyt/cannonball) | OutRun arcade engine reimplementation | 885 | 🟡 | C++ |
| [OpenEnroth](https://github.com/OpenEnroth/OpenEnroth) | Open reimplementation of the Might and Magic 6/7/8 game engine | 873 | 🟢 | C++ |
| [ReHLDS](https://github.com/rehlds/ReHLDS) | Reverse engineered, enhanced Half-Life Dedicated Server engine | 865 | 🟢 | C++ |
| [OpenNFS](https://github.com/OpenNFS/OpenNFS) | Attempt to recreate the classic Need for Speed Games (1-6). | 850 | 🟢 | C++ |
| [OpenMoHAA](https://github.com/openmoh/openmohaa) | Open re-implementation of Medal of Honor: Allied Assault | 837 | 🟢 | C |
| [librw](https://github.com/aap/librw) | A re-implementation of the RenderWare Graphics engine | 830 | 🟢 | C++ |
| [PvZ-Portable](https://github.com/wszqkzqk/PvZ-Portable) | Cross-platform reimplementation of Plants vs. Zombies | 823 | 🟢 | C++ |
| [NBlood](https://github.com/NBlood/NBlood) | Reverse-engineered ports of Build games using EDuke32 engine technology and development principles (NBlood/Rednukem/P... | 814 | 🟢 | C++ |
| [metaforce](https://github.com/AxioDL/metaforce) | A native reimplementation of the Metroid Prime engine | 808 | 🟢 | C++ |
| [uMario](https://github.com/jakowskidev/uMario_Jakowski) | uMario C++/SDL2 Game by Łykasz Jakowski | 803 | 🔴 | C++ |
| [ReGameDLL_CS](https://github.com/rehlds/ReGameDLL_CS) | Reverse engineered server-side GameDLL for Counter-Strike 1.6 | 799 | 🟢 | C++ |
| [si78c](https://github.com/loadzero/si78c) | Memory-accurate C reimplementation of the Space Invaders arcade ROM | 798 | 🔴 | C |
| [SuperMarioBros-C](https://github.com/MitchellSternke/SuperMarioBros-C) | An attempt to translate the original Super Mario Bros. for the NES to readable C/C++ | 786 | 🔴 | C++ |
| [NFSIISE](https://github.com/zaps166/NFSIISE) | Need For Speed™ II SE - Cross-platform wrapper with 3D acceleration and TCP protocol! | 772 | 🟢 | C |
| [OpenJKDF2](https://github.com/shinyquagsire23/OpenJKDF2) | Cross-platform reimplementation of Star Wars Jedi Knight: Dark Forces II in C | 768 | 🟢 | C |
| [skate-3-rust-engine](https://github.com/SK8-ENGINE/skate-3-rust-engine) | Rust/Bevy skating engine based on Skate 3 reverse engineering research | 761 | 🟢 | Rust |
| [ClassicUO](https://github.com/ClassicUO/ClassicUO) | Open-source reimplementation of the Ultima Online Classic client | 735 | 🟢 | C# |
| [jazz2-native](https://github.com/deathkiller/jazz2-native) | 🎮 · Jazz² Resurrection: Native C++ reimplementation of Jazz Jackrabbit 2 | 717 | 🟢 | C++ |
| [Memoria](https://github.com/Albeoris/Memoria) | Final Fantasy IX tools | 713 | 🟢 | C# |
| [OTClient](https://github.com/edubart/otclient) | Alternative Tibia client for OpenTibia servers in C++ and Lua | 707 | 🟡 | C++ |
| [Thyme](https://github.com/TheAssemblyArmada/Thyme) | Open-source re-implementation of Command & Conquer Generals: Zero Hour | 697 | 🟡 | C++ |
| [Exult](https://github.com/exult/exult) | Engine reimplementation for Ultima VII: The Black Gate and Serpent Isle | 694 | 🟢 | C++ |
| [OpenVIII](https://github.com/MaKiPL/OpenVIII-monogame) | Open source Final Fantasy VIII engine implementation in C# working on Windows and Linux (Android and iOS planned too!... | 673 | 🗄️ | C# |
| [Sonic 3 A.I.R.](https://github.com/Eukaryot/sonic3air) | Sonic 3 & Knuckles engine reimplementation (Angel Island Revisited) | 660 | 🟢 | C++ |
| [REGoth](https://github.com/REGoth-project/REGoth) | OpenSource-Reimplementation of the zEngine, used by the game "Gothic" | 653 | 🔴 | C++ |
| [GLSMAC](https://github.com/afwbkbc/glsmac) | Open-source reimplementation of Sid Meier's Alpha Centauri | 639 | 🟢 | C++ |
| [Portal 64: Still Alive](https://github.com/mwpenny/portal64-still-alive) | A demake of Portal for the Nintendo 64 | 625 | 🟢 | C |
| [Librelancer](https://github.com/Librelancer/Librelancer) | Reimplementation of the 2003 space game Freelancer. | 612 | 🗄️ |  |
| [OpenFodder](https://github.com/OpenFodder/openfodder) | Open-source reimplementation of Cannon Fodder | 606 | 🟢 | C++ |
| [OpenD2](https://github.com/eezstreet/OpenD2) | A project to open source Diablo 2. | 605 | 🔴 | C |
| [mkxp](https://github.com/Ancurio/mkxp) | mkxp, a free implementation of the RPG Maker Ruby Game Scripting System (RGSS) | 595 | 🟢 | C++ |
| [OpenSkyscraper](https://github.com/fabianschuiki/OpenSkyscraper) | Open source tower simulation game inspired by SimTower. | 591 | 🔴 | C++ |
| [OpenTS](https://github.com/OpenTS-Developers/OpenTS) | Open-source, reverse-engineered rebuild of the Command & Conquer: Tiberian Sun engine | 581 | 🟢 | C++ |
| [Jazz² Resurrection](https://github.com/deathkiller/jazz2) | Reimplementation of Jazz Jackrabbit 2. | 579 | 🟢 |  |
| [Warsmash](https://github.com/Retera/WarsmashModEngine) | Warcraft III engine emulation for modding | 579 | 🟢 | Java |
| [Carnage3D](https://github.com/codenamecpp/carnage3d) | Reimplementation of Grand Theft Auto 1 | 571 | 🟢 | C++ |
| [The Legend of Dragoon (Severed Chains)](https://github.com/Legend-of-Dragoon-Modding/Severed-Chains) | Reverse-engineered reimplementation / port of The Legend of Dragoon (Severed Chains) | 558 | 🟢 | Java |
| [sm (Super Metroid)](https://github.com/snesrev/sm) | C reimplementation of Super Metroid from reverse-engineered SNES code | 557 | 🔴 | C |
| [NXEngine-evo](https://github.com/nxengine/nxengine-evo) | Engine rewrite of Cave Story (Doukutsu Monogatari) | 552 | 🟢 | C |
| [Ambermoon.net](https://github.com/Pyrdacor/Ambermoon.net) | Ambermoon rewrite in C# | 542 | 🟢 | C# |
| [OTClient (Redemption)](https://github.com/opentibiabr/otclient) | Modern C++20 fork-successor of OTClient for Tibia-compatible servers | 538 | 🟢 | Lua |
| [TOMB5](https://github.com/TOMB5/TOMB5) | Tomb Raider: Chronicles Disassembly translated to C source code. | 520 | 🔴 | C |
| [Akhenaten](https://github.com/dalerank/Akhenaten) | Open-source reimplementation of Pharaoh (Impressions Games) | 518 | 🟢 | C++ |
| [KisakCOD](https://github.com/SwagSoftware/KisakCOD) | Open-source reimplementation of Call of Duty 4 multiplayer | 517 | 🟢 | C++ |
| [OpenClaw](https://github.com/pjasicek/OpenClaw) | Reimplementation of the Captain Claw (1997) platformer | 516 | 🔴 | C++ |
| [REGoth](https://github.com/REGoth-project/REGoth-bs) | An open source reimplementation of zEngine the engine behind Gothic and Gothic II. | 499 | 🔴 | C++ |
| [Simitone](https://github.com/riperiperi/Simitone) | Re-implementation of The Sims 1, based off of FreeSO. | 499 | 🟡 | C# |
| [FreeSpace 2 Source Code Project](https://github.com/scp-fs2open/fs2open.github.com) | Origin Repository for SCP FreeSpace 2 Open | 494 | 🟢 | C++ |
| [Vange-rs](https://github.com/kvark/vange-rs) | Rusty Vangers clone | 488 | 🟢 | Rust |
| [donut](https://github.com/plowteam/donut) | Reimplementation of The Simpsons: Hit & Run in modern C++ and modern OpenGL. | 486 | 🟡 | C++ |
| [Miu2D](https://github.com/luckyyyyy/miu2d) | Miu2D is a 2D RPG game engine built with Rust + TypeScript + React + Canvas, designed for the Web platform. 剑侠情缘2/月影传... | 483 | 🟢 | TypeScript |
| [Nanosaur](https://github.com/jorio/Nanosaur) | Nanosaur source port 🦖 | 474 | 🟢 | C |
| [OpenVic](https://github.com/OpenVicProject/OpenVic) | Main Repo for the OpenVic Project | 474 | 🟢 | GDScript |
| [McOsu](https://github.com/McKay42/McOsu) | Unofficial osu! practice client with VR support | 469 | 🟢 | C++ |
| [OpenLiberty](https://github.com/openfw-game/OpenLiberty) | GTA III reimplementation in the Godot engine loading original assets | 468 | 🟢 | GDScript |
| [Super Mario 64 (DualShock Version)](https://github.com/malucard/sm64-psx) | A very WIP port of https://www.github.com/n64decomp/sm64 for the PlayStation 1 | 464 | 🗄️ | C |
| [cs16-client](https://github.com/Velaron/cs16-client) | Reverse engineered Counter-Strike 1.6 client for the Xash3D engine | 460 | 🟢 | C++ |
| [Alive Reversing](https://github.com/AliveTeam/alive_reversing) | Reimplementation of Oddworld: Abe's Exoddus. | 444 | 🟢 | C++ |
| [Wargus](https://github.com/Wargus/wargus) | Importer and scripts for Warcraft II: Tides of Darkness, the expansion Beyond the Dark Portal, and Aleonas Tales | 442 | 🟢 | C |
| [OpenTS2](https://github.com/LazyDuchess/OpenTS2) | Open source re-implementation of The Sims 2 in Unity | 437 | 🟢 | C# |
| [Chariot](https://github.com/ChariotEngine/Chariot) | Reimplementation of the Age of Empires (1997) engine in Rust | 427 | 🔴 | Rust |
| [cinnamon](https://github.com/Project-Sunshine-Native/cinnamon) | GameMaker GML runner reimplementation in C for 3DS and Wii U | 415 | 🟢 | C |
| [OpenJazz](https://github.com/AlisterT/openjazz) | Engine reimplementation of Jazz Jackrabbit; uses original game data (C++) | 410 | 🟢 | C |
| [ResidualVM](https://github.com/residualvm/residualvm) | Engine reimplementation for 3D adventures like Grim Fandango (archived; merged into ScummVM) | 401 | 🗄️ | C++ |
| [Butterscotch](https://github.com/ButterscotchRunner/Butterscotch) | Open source reimplementation of the GameMaker: Studio runner | 396 | 🟢 | C |
| [Duke Nukem II (Reconstructed)](https://github.com/lethal-guitar/Duke2Reconstructed) | Reverse-engineered reimplementation / port of Duke Nukem II (Reconstructed) | 373 | 🟡 | C |
| [BStone](https://github.com/bibendovsky/bstone) | Unofficial source port for Blake Stone series | 370 | 🟢 | C |
| [PokeSwift](https://github.com/Dimillian/PokeSwift) | Reimplementation of the Pokemon Red/Blue engine in Swift | 363 | 🟢 | Assembly |
| [OpenMW for Android](https://github.com/xyzz/openmw-android) | OpenMW for Android | 362 | 🗄️ | Java |
| [3SX](https://github.com/crowded-street/3sx) | "The Third of the Third" ported to modern platforms | 358 | 🟢 | C |
| [open-realm](https://github.com/corepunch/open-realm) | Open-source reimplementation of the Warcraft III engine | 350 | 🟢 | C |
| [OpenSWE1R](https://github.com/OpenSWE1R/openswe1r) | Open-source reimplementation of Star Wars Episode I: Racer | 350 | 🔴 | C |
| [Tomb Engine](https://github.com/TombEngine/TombEngine) | A new and modern engine for custom Tomb Raider levels incorporating classic features and new enhancements. | 345 | 🟢 | C++ |
| [pikachu-volleyball-p2p-online](https://github.com/gorisanson/pikachu-volleyball-p2p-online) | Peer-to-peer online play for the reverse engineered Pikachu Volleyball | 343 | 🟢 | JavaScript |
| [Freeserf](https://github.com/freeserf/freeserf) | Settlers 1 (Serf City) clone. | 340 | 🟢 | C++ |
| [UnderworldExporter](https://github.com/hankmorgan/UnderworldExporter) | Updated Release 27th Oct 2018 Unity based port of Ultima Underworld I and II. Download under releases | 340 | 🗄️ | C# |
| [FreeSims](https://github.com/francot514/FreeSims) | Open source engine used for The Sims | 331 | 🟢 | C# |
| [UnderworldGodot](https://github.com/hankmorgan/UnderworldGodot) | An engine recreation of Ultima Underworld and Ultima Underworld 2 in the Godot Engine. | 331 | 🟢 | C# |
| [open-ig](https://github.com/akarnokd/open-ig) | Open-source reimplementation of Imperium Galactica | 326 | 🟢 | Java |
| [FreeHL](https://github.com/eukara/freehl) | Clean-room reimplementation of Half-Life and HL: Deathmatch in QuakeC | 321 | 🟢 | QuakeC |
| [Omnispeak](https://github.com/sulix/omnispeak) | Reimplementation of Commander Keen in Goodbye Galaxy. | 317 | 🟢 | C |
| [reone](https://github.com/seedhartha/reone) | Game engine reimplementation for Star Wars: KotOR I and II | 317 | 🟡 | C++ |
| [Abyss Engine](https://github.com/AbyssEngine/AbyssEngine) | Abyss Engine clean-room reimplementation of Diablo 2, written in C. The goal is to recreate the original game engine,... | 316 | 🟡 | C |
| [CroftEngine](https://github.com/stohrendorf/CroftEngine) | An open-source Tomb Raider 1 engine remake | 310 | 🟢 | C++ |
| [open-supaplex](https://github.com/sergiou87/open-supaplex) | Reverse engineered open source port of Supaplex | 309 | 🟢 | C |
| [Theseus](https://github.com/MrMilenko/Theseus) | Reverse-engineered reconstruction of the original Xbox 5960 dashboard | 308 | 🟢 | C++ |
| [freecs](https://github.com/eukara/freecs) | Clean-room Counter-Strike 1.5 in QuakeC using the Nuclide SDK | 301 | 🟡 | QuakeC |
| [MafiaUnity](https://github.com/MafiaHub/MafiaUnity) | 🕹 Open-source Mafia game framework | 294 | 🗄️ | C# |
| [Resident Evil 2 (OpenBiohazard2)](https://github.com/OpenBiohazard2/OpenBiohazard2) | Reverse-engineered reimplementation / port of Resident Evil 2 (OpenBiohazard2) | 294 | 🟢 | Go |
| [lba2remake](https://github.com/LBALab/lba2remake) | A Little Big Adventure 2 / Twinsen's Odyssey reimplementation in JavaScript / Three.js / React | 287 | 🟢 | TypeScript |
| [Wowser](https://github.com/wowserhq/wowser) | World of Warcraft client in the browser using JavaScript and WebGL | 286 | 🔴 | JavaScript |
| [PrinceJS](https://github.com/ultrabolido/PrinceJS) | Prince of Persia reimplementation in HTML5/JavaScript | 282 | 🟡 | JavaScript |
| [Sourcehold](https://github.com/sourcehold/Sourcehold) | Open source re-implementation of Stronghold 1 | 280 | 🟡 | C++ |
| [spearmint](https://github.com/clover-moe/spearmint) | Spearmint — an updated id Tech 3 engine for continuing the classics and creating new games. | 280 | 🟢 | C |
| [Super-Mario-World-Remastered-Public](https://github.com/JHDev2006/Super-Mario-World-Remastered-Public) | A Remake / Remaster of the original Super Mario World, in Godot. Adds new features / improvements! | 280 | 🗄️ | GDScript |
| [Doom64EX](https://github.com/svkaiser/Doom64EX) | Reverse engineered recreation of Doom 64 with modding features | 274 | 🟢 | C++ |
| [The Eternity Engine](https://github.com/team-eternity/eternity) | The Eternity Engine | 273 | 🟢 | C++ |
| [DGEngine](https://github.com/dgcor/DGEngine) | Implementation of the Diablo game engine. | 271 | 🟡 | C++ |
| [Heretic2R](https://github.com/m-x-d/Heretic2R) | Heretic II (1998, Raven Software) reverse-engineered source port. | 271 | 🟢 | C |
| [CivOne](https://github.com/Solen1985/CivOne) | Implementation of Sid Meier's Civilization. | 262 | 🔴 | C# |
| [OpenBW](https://github.com/OpenBW/openbw) | Open-source StarCraft: Brood War engine reimplementation | 259 | 🟢 | C++ |
| [OpenMBU](https://github.com/MBU-Team/OpenMBU) | OpenMBU is a revival of Marble Blast Ultra, the 2006 Xbox 360 arcade classic. | 258 | 🟢 | C++ |
| [OpenGD](https://github.com/Open-GD/OpenGD) | Open source implementation of Geometry Dash | 249 | 🟡 | C++ |
| [undertale](https://github.com/fachinformatiker/undertale) | Undertale src code | 248 | 🔴 | Game Maker Language |
| [2006scape](https://github.com/2006-Scape/2006Scape) | A 2006 Runescape Emulation Server | 244 | 🟢 | Java |
| [freeaoe](https://github.com/sandsmark/freeaoe) | A free game engine capable of running Age of Empires 2 and Star Wars: Galactic Battlegrounds | 241 | 🔴 | C++ |
| [Kinoko](https://github.com/vabold/Kinoko) | Reimplementation of Mario Kart Wii's physics engine in C++ | 236 | 🟢 | C++ |
| [KisakBlack](https://github.com/SwagSoftware/KisakBlack) | Open source reimplementation of Call of Duty: Black Ops | 234 | 🟢 | C++ |
| [srceng-android](https://github.com/nillerusr/srceng-android) | Android launcher for source engine | 233 | 🔴 | Java |
| [Doom 64 EX+](https://github.com/atsb/Doom64EX-Plus) | An improved modern version of Doom64EX. | 230 | 🗄️ | C |
| [nanolathe](https://github.com/nanolathe-gg/nanolathe) | Total Annihilation engine reimplementation in Go | 221 | 🟢 | Go |
| [OpenAWE](https://github.com/OpenAWE-Project/OpenAWE) | A reimplementation of Remedy Entertainments Alan Wake Engine, in later iterations known as the Northlight Engine | 221 | 🟢 | C++ |
| [rawgl](https://github.com/cyxx/rawgl) | Another World/Out of This World engine reimplementation (SDL, OpenGL) | 209 | 🗄️ | C++ |
| [impacto](https://github.com/CommitteeOfZero/impacto) | Reimplementation of the MAGES. visual novel engine | 203 | 🟢 | C++ |
| [Cave Story (CSE2)](https://github.com/gameblabla/CSE2) | Reverse-engineered reimplementation / port of Cave Story (CSE2) | 202 | 🟢 | C++ |
| [Duck Game Rebuilt](https://github.com/TheFlyingFoool/DuckGameRebuilt) | Duck Game decompiled & rebuilt with some added features, | 198 | 🟢 | C# |
| [OpenNFS1](https://github.com/jeff-1amstudios/OpenNFS1) | Remake of the original EA Need for Speed 1 using c# and Monogame | 198 | 🔴 | C# |
| [FreeFT](https://github.com/nadult/FreeFT) | Isometric action game engine | 194 | 🟢 | C++ |
| [MegaManXSNESRecomp](https://github.com/mstan/MegaManXSNESRecomp) | Mega Man X recompiled for the Super Nintendo using snesrecomp · Part of the R.A.I.D. community | 194 | 🟢 | C |
| [XL Engine](https://github.com/Mindwerks/XLEngine) | XLEngine allows you to play Dark Forces, Daggerfall and soon Outlaws and Blood with modern technology. | 193 | 🔴 | C++ |
| [Reburn 3](https://github.com/reburndev/reburn3) | A work-in-progress open source reimplementation of Burnout 3: Takedown. | 192 | 🟡 | C++ |
| [Vib-Ribbon (open-ribbon)](https://github.com/open-ribbon/open-ribbon) | Reverse-engineered reimplementation / port of Vib-Ribbon (open-ribbon) | 192 | 🟡 | C |
| [z2rs](https://github.com/troyedwardsjr/z2rs) | Clean-room reconstruction of Zelda II: The Adventure of Link in Rust | 189 | 🟢 | Rust |
| [sh3redux](https://github.com/Palm-Studios/sh3redux) | SILENT HILL 3 Engine Remake in OpenGL and C++ | 187 | 🟡 | C++ |
| [KaM Remake](https://github.com/reyandme/kam_remake) | "KaM Remake" is an RTS game remake written in Delphi from scratch. | 184 | 🟢 | Pascal |
| [lofp](https://github.com/metavert-io/lofp) | Recreation of Legends of Future Past, the 1990s commercial MUD | 183 | 🟢 | HTML |
| [Powerslave EX](https://github.com/svkaiser/PowerslaveEX) | Powerslave EX is a unofficial recreation of Lobotomy Software’s obscured FPS game, Powerslave (also known as Exhumed... | 183 | 🔴 | C |
| [pokered-gbc](https://github.com/dannye/pokered-gbc) | Pokémon Red/Blue overhauled with full GBC support. Made by FroggestSpirit, Drenn, and dannye. Also check out the crys... | 182 | 🟢 | Assembly |
| [Chasm-Reverse](https://github.com/Panzerschrek/Chasm-Reverse) | "PanzerChasm" is a free recreation of the game "Chash: - The Rift" by "ActionForms" using the original game data (CSM... | 180 | 🟢 | C++ |
| [Vault13](https://github.com/pingw33n/vault13) | Reimplementation of the Fallout 2 engine in Rust | 179 | 🟢 | Rust |
| [Open Horizon](https://github.com/undefined-darkness/open-horizon) | Engine reimplementation of Ace Combat: Assault Horizon; uses original game data (C++) | 178 | 🔴 | C++ |
| [eZeus](https://github.com/MaurycyLiebner/eZeus) | Open-source implementation of Zeus: Master of Olympus. | 177 | 🟢 | C++ |
| [Legacy of Kain: Soul Reaver Decompile](https://github.com/Gh0stBlade/KAIN2) | Legacy of Kain: Soul Reaver Decompile | 176 | 🟡 | C |
| [Panzer Dragoon Saga (Azel)](https://github.com/yaz0r/Azel) | Reverse-engineered reimplementation / port of Panzer Dragoon Saga (Azel) | 176 | 🟢 | C++ |
| [OpenMC2](https://github.com/OpenMC2/OpenMC2) | An Open Source Re-Implementation of Midnight Club 2 | 173 | 🔴 | C++ |
| [OUO](https://github.com/draxinar/ouo) | OUO: reverse engineering of Ultima Online: The Second Age server | 172 | 🟢 | C |
| [Arcanum Community Edition](https://github.com/alexbatalov/arcanum-ce) | Arcanum for modern operating systems | 171 | 🟢 | C |
| [JXQY-all-in-one](https://github.com/Upwinded/JXQY-all-in-one) | 剑侠情缘 Sword Heroes' Fate | 171 | 🟢 | C++ |
| [OpenHoW](https://github.com/hogsy/OpenHoW) | Open-source reimplementation of Gremlin's Hogs of War (PC/PSX). | 170 | 🗄️ | C |
| [rlvm](https://github.com/eglaysher/rlvm) | RealLive clone for Linux and OSX | 170 | 🟡 | C++ |
| [OpenC1](https://github.com/jeff-1amstudios/OpenC1) | Remake of Carmageddon 1 engine | 168 | 🔴 | C# |
| [whoa](https://github.com/whoahq/whoa) | Unofficial open-source reimplementation of the World of Warcraft 3.3.5 client | 168 | 🟢 | C++ |
| [Nuvie](https://github.com/nuvie/nuvie) | Nuvie - New Ultima VI Engine | 165 | 🟡 | C++ |
| [ElonaFoobar](https://github.com/elonafoobar/elonafoobar) | One of the Elona variants | 164 | 🗄️ | C++ |
| [dunedynasty](https://github.com/gameflorist/dunedynasty) | Remaster of Dune II built on the OpenDUNE reverse engineered codebase | 162 | 🟢 | C |
| [Galaxy on Fire 2 Unity Remake](https://github.com/JoppieToppie/Galaxy-on-Fire-2-Unity-Remake) | Galaxy on Fire 2 decompilation and Unity remake | 162 | 🟢 | C |
| [OpenTPW](https://github.com/OpenTPW/OpenTPW) | An open-source re-implementation of Bullfrog's Sim Theme Park / Theme Park World (1999). | 161 | 🟢 | C# |
| [SeriousSamClassic-VK](https://github.com/tx00100xt/SeriousSamClassic-VK) | Open source game engine for Serious Sam Classic with Vulkan support. | 161 | 🟢 | C++ |
| [Free in the Dark](https://github.com/yaz0r/FITD) | Free in the Dark, a Alone in the Dark engine reimplementation. | 158 | 🟡 | C++ |
| [openQ4](https://github.com/themuffinator/openQ4) | Open-source reimplementation of Quake 4 | 157 | 🟢 | C++ |
| [Stargus](https://github.com/Wargus/stargus) | Importer and scripts for Starcraft | 157 | 🟢 | C++ |
| [OpenNefia](https://github.com/OpenNefia/OpenNefia) | Moddable engine reimplementation of the Japanese roguelike Elona. | 156 | 🟡 | C# |
| [nv-rs](https://github.com/slaterain/nv-rs) | Experimental Fallout: New Vegas engine reimplementation in Rust and Bevy | 154 | 🟢 | Rust |
| [OpenAG](https://github.com/YaLTeR/OpenAG) | Open-source reimplementation of the Adrenaline Gamer client library | 154 | 🟡 | C++ |
| [Zuma-Deluxe-HD](https://github.com/GalaxyShad/Zuma-Deluxe-HD) | A remake of the legendary 2003 PopCap game with improved textures and support for 16:9 aspect ratio. | 154 | 🟢 | C |
| [OGS](https://github.com/headcrab-junkyard/OGS) | An open-source GoldSrc engine clone (Clean authentic reimplementation without using reverse-engineered code) | 153 | 🟡 | C |
| [remc2](https://github.com/turican0/remc2) | Reverse engineering of Magic Carpet 2 from Assembler. | 153 | 🟢 | C++ |
| [engge](https://github.com/scemino/engge) | Open source remake of Thimbleweed Park's engine | 151 | 🗄️ | C++ |
| [hode](https://github.com/usineur/hode) | hode is a rewrite (made by Grégory Montoir) of the engine used in the game Heart of Darkness made by Amazing Studio. | 151 | 🟡 | C++ |
| [KotOR.js](https://github.com/KobaltBlu/KotOR.js) | A remake of the Odyssey Game Engine that powered KotOR I & II written in JavaScript | 149 | 🟢 | TypeScript |
| [kys-pascal](https://github.com/scarsty/kys-pascal) | 《金庸群侠传》Pascal重制版 | 149 | 🟢 | Pascal |
| [rfvp](https://github.com/xmoezzz/rfvp) | Non-official Rust implementation of the FVP visual novel engine | 146 | 🟢 | Rust |
| [darkfo](https://github.com/darkf/darkfo) | DarkFO, a post-nuclear RPG remake (of Fallout 2) | 145 | 🗄️ | TypeScript |
| [JSettlers](https://github.com/paulwedeck/settlers-remake) | A Remake of "The Settlers III" for Windows, Linux and Android | 144 | 🗄️ | Java |
| [OpenMB](https://github.com/cookgreen/OpenMB) | Role-playing game engine for Taleworlds' Mount&Blade Series. | 144 | 🟢 | C# |
| [Strife: Veteran Edition](https://github.com/svkaiser/strife-ve) | Strife Veteran Edition GPL Source Release | 143 | 🔴 | C |
| [Q-Gears](https://github.com/q-gears/q-gears) | Q-Gears is an RPG engine for games like Squaresoft's Final Fantasy 7, 8, 9, or Xenogears. It is designed to be cross-... | 141 | 🔴 | C++ |
| [UA_source](https://github.com/Marisa-Chan/UA_source) | Mod for UrbanAssault (Replace original game engine) | 139 | 🟡 | C++ |
| [Litecraft](https://github.com/KernelFreeze/Litecraft) | Clean-room open source Minecraft client implementation | 138 | 🗄️ | Rust |
| [Test Drive Unlimited (OpenTestDriveUnlimited)](https://github.com/opentestdriveunlimited/OpenTestDriveUnlimited) | Reverse-engineered reimplementation / port of Test Drive Unlimited (OpenTestDriveUnlimited) | 138 | 🟢 | C++ |
| [Uncharted waters 2 remake](https://github.com/JohanLi/uncharted-waters-2) | Browser-based remake of Uncharted Waters: New Horizons (大航海時代II) | 137 | 🟢 | TypeScript |
| [unity-arcanum](https://github.com/Suvitruf/unity-arcanum) | Fan-made reimplementation of the Arcanum engine in Unity | 136 | 🟢 | C# |
| [Free Heroes 2 - Enhanced](https://github.com/ciplogic/fheroes2enh) | Free Heroes 2 - Enhanced | 135 | 🔴 | C++ |
| [War1gus](https://github.com/Wargus/war1gus) | Importer and scripts for Warcraft: Orcs and Humans | 135 | 🟢 | Lua |
| [The-Great-Escape-in-C](https://github.com/dpt/The-Great-Escape-in-C) | Classic ZX Spectrum game "The Great Escape" rewritten in portable C | 133 | 🟢 | C |
| [Raptor](https://github.com/skynettx/raptor) | Reversed-engineered source port from Raptor Call Of The Shadows | 132 | 🟢 | C |
| [Yukon](https://github.com/wizguin/yukon) | HTML5 Club Penguin client reimplementation | 130 | 🟡 | JavaScript |
| [aoe](https://github.com/FolkertVanVerseveld/aoe) | Re-implementation of Age of Empires and the Rise of Rome expansion | 128 | 🟢 | C++ |
| [lttp-phaser](https://github.com/englercj/lttp) | An incomplete remake of The Legend of Zelda - A Link to the Past using WebGL and the browser. | 126 | 🔴 | TypeScript |
| [Ozymandias (Julius)](https://github.com/Banderi/Ozymandias_Julius) | An open source re-implementation of Pharaoh (1999) in the Julius/Augustus engine | 126 | 🟢 | C++ |
| [Robot War Engine](https://github.com/MHeasell/rwe) | Robot War Engine - Real-time strategy game engine compatible with Total Annihilation | 126 | 🟢 | C++ |
| [Paper Mario DX](https://github.com/bates64/papermario-dx) | Improved Paper Mario (N64) engine for your next romhack | 125 | 🟢 | C |
| [Umineko Project](https://github.com/umineko-project/onscripter-ru) | ONScripter-RU game engine | 125 | 🔴 | C++ |
| [Prey 2006: A Talon Brave Game](https://github.com/FriskTheFallenHuman/Prey2006) | Prey 2006 SDK integrated with Doom 3 GPL release | 124 | 🟢 | C |
| [MikuPan](https://github.com/Mikompilation/MikuPan) | PC Port Of Fatal Frame 1 Based On Himuro | 122 | 🟢 | C++ |
| [lain-bootleg-bootleg](https://github.com/ad044/lain-bootleg-bootleg) | Reverse engineering and remake of Lain Bootleg | 121 | 🟢 | C |
| [OpenNefia](https://github.com/Ruin0x11/OpenNefia) | Moddable engine reimplementation of the roguelike Elona | 121 | 🟡 | Lua |
| [CrossCraft](https://github.com/CrossCraft/CrossCraft) | Open-source Minecraft reimplementation | 120 | 🟢 | Zig |
| [siglus_rs](https://github.com/xmoezzz/siglus_rs) | Unofficial Rust implementation of the SiglusEngine visual novel engine | 116 | 🟢 | Rust |
| [Apolyton Call to Power II Source Code Project](https://github.com/civctp2/civctp2) | Call to Power II: Apolyton Edition source code project. Call to Power II (CTP2) is a civilization computer game, whos... | 115 | 🟢 | C |
| [Magic Carpet 2 HD](https://github.com/thobbsinteractive/magic-carpet-2-hd) | Recode Binary code of game Magic Carpet2 to C/C++ language(remake MC2 for any platform) | 114 | 🟢 | C++ |
| [Dune2JS](https://github.com/oklemenz/Dune2JS) | Dune II reimplementation in HTML5/JavaScript | 112 | 🟡 | JavaScript |
| [Javascript BoulderDash](https://github.com/jakesgordon/javascript-boulderdash) | An HTML5 implementation of the c64 classic Boulderdash game | 112 | 🟡 | JavaScript |
| [1oom](https://github.com/1oom-fork/1oom) | 1oom is a Master of Orion Classic (1993) game engine recreation that requires the original files to run. | 111 | 🟢 | C |
| [Ambermoon](https://github.com/Pyrdacor/Ambermoon) | Resources and reimplementation for the Amiga game Ambermoon | 111 | 🟢 | Assembly |
| [Gorc](https://github.com/jdmclark/gorc) | Early-development Jedi Knight: Dark Forces 2 game engine recreation | 110 | 🔴 | C++ |
| [Lemmings.ts](https://github.com/tomsoftware/Lemmings.ts) | A Web Lemmings Clone/Remake in TypeScript | 109 | 🔴 | TypeScript |
| [Civ2-clone](https://github.com/axx0/Civ2-clone) | Open-source re-implementation of Civilization 2 | 108 | 🟢 | C# |
| [opendpr](https://github.com/TeamLumi/opendpr) | Reverse engineered recreation of Pokemon Brilliant Diamond and Shining Pearl | 106 | 🟢 | C# |
| [neo](https://github.com/NeotokyoRebuild/neo) | NEOTOKYO;REBUILD: reimplementation and continuation of the NEOTOKYO mod on a TF2 engine branch | 103 | 🟢 | C++ |
| [lithtech](https://github.com/Katana-Steel/lithtech) | Engine reimplementation of F.E.A.R., The Operative: No One Lives Forever; uses original game data (C++) | 102 | 🟢 | C++ |
| [cavestory-sdl2](https://github.com/JIghtuse/cavestory-sdl2) | Reconstructing Cave Story with SDL 2.0 and C++14 | 101 | 🔴 | C++ |
| [DreeRally](https://github.com/enriquesomolinos/DreeRally) | Death Rally engine reimplementation | 101 | 🔴 | C |
| [OpenUG2](https://github.com/whoismept/OpenUG2) | From-scratch reimplementation of Need for Speed: Underground 2 | 101 | 🟢 | C |
| [MegaManX4Recomp](https://github.com/mstan/MegaManX4Recomp) | Mega Man X4 (USA, SLUS-00561) statically recompiled to a native PC executable with PSXRecomp | 100 | 🟢 | C |
| [Redguard Unity](https://github.com/RGUnity/redguard-unity) | Main repository containing the Unity project and the wiki | 98 | 🟢 | C# |
| [OpenCity2k](https://github.com/OpenCity2k/OpenCity2k) | Open source reimplementation of SimCity 2000 | 97 | 🟡 | Python |
| [tf15-client](https://github.com/Velaron/tf15-client) | Reverse engineered Team Fortress Classic client for Xash3D | 97 | 🟡 | C++ |
| [ko](https://github.com/ko4life-net/ko) | Open source reverse engineered recreation of an old Knight Online version | 94 | 🟡 | C++ |
| [Barnyard (OpenBarnyard)](https://github.com/InfiniteC0re/OpenBarnyard) | Reverse-engineered reimplementation / port of Barnyard (OpenBarnyard) | 93 | 🟢 | C++ |
| [PC port of Animal Crossing](https://github.com/ACreTeam/forest) | PC Port of Animal Crossing | 93 | 🟢 | C |
| [UchuServer](https://github.com/UchuServer/Uchu) | LEGO Universe server written in C# | 93 | 🟡 | C# |
| [Executive Man](https://github.com/CamHenlin/ExecutiveMan) | ExecutiveMan, a JavaScript MegaMan clone | 92 | 🔴 | JavaScript |
| [OpenCrystalCaves](https://github.com/OpenCrystalCaves/OpenCrystalCaves) | OCC is an unofficial open source engine reimplementation of the game trilogy Crystal Caves. | 92 | 🟢 | C++ |
| [OpenVice](https://github.com/clashbyte/openvice) | Grand Theft Auto: Vice City Open Source port to C# | 92 | 🟡 | C# |
| [OpenSC4](https://github.com/OpenSC4-org/OpenSC4) | Open source reimplementation of SimCity 4 | 91 | 🟡 | GDScript |
| [The Great Escape](https://github.com/dpt/The-Great-Escape) | Classic ZX Spectrum game "The Great Escape" reverse engineered | 90 | 🟡 | Assembly |
| [dejavu](https://github.com/rpjohnst/dejavu) | Game Maker runtime reimplementation | 89 | 🟡 | Rust |
| [librwgta](https://github.com/aap/librwgta) | GTA-specific extensions to librw (RenderWare reimplementation) and tools using it | 89 | 🟢 | C++ |
| [Pizza Tower (OpenTower)](https://github.com/femloy/OpenTower) | Reverse-engineered reimplementation / port of Pizza Tower (OpenTower) | 89 | 🟢 | Game Maker Language |
| [glfrontier](https://github.com/pcercuei/glfrontier) | Reverse engineered version of Frontier: Elite II | 88 | 🔴 | C |
| [OpenRaider](https://github.com/xythobuz/OpenRaider) | Open Source Tomb Raider Engine | 86 | 🟡 | C++ |
| [Worldstone](https://github.com/Lectem/Worldstone) | Diablo 2 tools and engine reimplementation in C++ | 82 | 🔴 | C++ |
| [f2bgl](https://github.com/cyxx/f2bgl) | Fade To Black engine reimplementation (SDL, OpenGL) | 81 | 🗄️ | C++ |
| [OpenDriverEngine](https://github.com/OpenDriver2/OpenDriverEngine) | Research engine running Driver 1 and Driver 2 (PS1) on one codebase | 81 | 🟡 | C++ |
| [u4-decompiled](https://github.com/ergonomy-joe/u4-decompiled) | Decompiled source code for the PC version of Ultima IV - Quest Of The Avatar | 81 | 🔴 | C |
| [xoreos-tools](https://github.com/xoreos/xoreos-tools) | Tools for BioWare Aurora engine game formats, companion to the xoreos reimplementation | 81 | 🟢 | C++ |
| [Ultima 5 Redux](https://github.com/bradhannah/Ultima5Redux) | A mostly true to the original Ultima 5 remake in C# using the original U5 data files. | 80 | 🟢 |  |
| [WinWar](https://github.com/CAMongrel/WinWar) | WarCraft Orcs & Humans remake using the original assets | 80 | 🗄️ | C# |
| [Xenogears (Noah, non-matching)](https://github.com/yaz0r/Noah) | Reverse-engineered reimplementation / port of Xenogears (Noah, non-matching) | 78 | 🟢 | C++ |
| [NFS Recompiled](https://github.com/motor-dev/nfs-recompiled) | Engine reimplementation of Need For Speed II, Need For Speed III: Hot Pursuit; uses original game data (C++) | 77 | 🟢 | C++ |
| [OpenSR](https://github.com/ObKo/OpenSR) | Opensource multi-genre game based upon "Space Rangers 2: Dominators" | 77 | 🗄️ | C++ |
| [tower-together](https://github.com/phulin/tower-together) | Clone of the 1993 game SimTower | 77 | 🟢 | TypeScript |
| [openbgi](https://github.com/Cytlan/openbgi) | Open source reimplementation of the Ethornell Buriko General Interpreter | 76 | 🟢 | C |
| [openstrike](https://github.com/AMDmi3/openstrike) | Libre reimplementation of Jungle and Desert Strike games | 76 | 🟡 | C++ |
| [FreeHeroes](https://github.com/mapron/FreeHeroes) | FreeHeroes is a free engine for Heroes of Might and Magic 3, similar to VCMI project. | 75 | 🟢 | C++ |
| [MegaManX6Recomp](https://github.com/mstan/MegaManX6Recomp) | Mega Man X6 (USA) recompiled for the Sony PlayStation using psxrecomp · Part of the R.A.I.D. community | 75 | 🟢 | Python |
| [OpenMoonstone](https://github.com/joetsoi/OpenMoonstone) | Open source reimplementation of Moonstone: A Hard Day's Knight | 75 | 🔴 | Rust |
| [ppengine](https://github.com/jonathanopalise/ppengine) | 3D remake of Pole Position using game logic reverse engineered from the arcade ROMs | 75 | 🔴 | C |
| [Snipes](https://github.com/Davidebyzero/Snipes) | The classic 1982 text-mode game Snipes, ported from the original DOS executable with 100% identical game logic, with... | 75 | 🟡 | C++ |
| [Underworld Adventures](https://github.com/vividos/UnderworldAdventures) | Underworld Adventures is a project to recreate Ultima Underworld 1 on modern operating systems, using the original ga... | 75 | 🟢 | C++ |
| [dRally](https://github.com/urxp/dRally) | Open Source Engine / Death Rally [1996] | 74 | 🔴 | C |
| [OpenAOE](https://github.com/angered-ghandi/OpenAOE) | Open source reimplementation of Age of Empires (1997) | 74 | 🔴 | Rust |
| [SCSharp](https://github.com/toshok/scsharp) | Starcraft reimplementation in C# | 73 | 🔴 | C# |
| [LTJS](https://github.com/bibendovsky/ltjs) | LithTech Jupiter System | 72 | 🟢 | C++ |
| [Wolfenshine](https://github.com/deanthecoder/Wolfenshine) | Modern C# reimplementation of Wolfenstein 3D | 72 | 🟢 | C# |
| [Mario Kart 64 for Dreamcast](https://github.com/jnmartin84/mk64-dc) | Sega Dreamcast port of Mario Kart 64 decompilation | 71 | 🟢 | C |
| [OpenFNaF](https://github.com/MotoLegacy/OpenFNaF) | Open source reimplementation of Five Nights at Freddy's | 71 | 🔴 | C |
| [VitalWear](https://github.com/cfogrady/VitalWear) | Wear OS engine recreation of the Bandai Vital Bracelet BE | 71 | 🟡 | Kotlin |
| [OpenPigeon](https://github.com/OpenBubbles/OpenPigeon) | Open-source GamePigeon reimplementation | 70 | 🟢 | Kotlin |
| [steins-gate](https://github.com/FGRE/steins-gate) | Reimplementation of Steins;Gate visual novel | 70 | 🔴 | C++ |
| [Another World JS](https://github.com/cyxx/another_js) | Another World/Out of This World (HTML5) | 69 | 🗄️ | JavaScript |
| [chronon](https://github.com/hogsy/chronon) | Open-source reimplementation of Anachronox | 69 | 🟡 | C++ |
| [Test-Drive-3-Maps](https://github.com/s-macke/Test-Drive-3-Maps) | Reverse-engineered and extracted the world maps of the 1990 DOS game Test Drive III | 69 | 🟢 | Assembly |
| [TombaRecomp](https://github.com/mstan/TombaRecomp) | Tomba! (USA) recompiled for the Sony PlayStation using psxrecomp · Part of the R.A.I.D. community | 69 | 🟢 | C++ |
| [Loderunner](https://github.com/Piddewitt/Loderunner) | Reverse engineered C64 assembler source code to recreate a bit for bit identical version of the original game. | 67 | 🟡 | Assembly |
| [Cosmo-Engine](https://github.com/yuv422/cosmo-engine) | A new game engine to play the MS-DOS game "Cosmo's Cosmic Adventure" on modern systems | 66 | 🟢 | C |
| [Dangerous Dave 2: Modification Edition](https://github.com/Harchvertelol/Dangerous-Dave-2-Modification-Edition) | This is an open-source remake of a well-known platform game Dangerous Dave 2 with flexible and highly customizable co... | 66 | 🟢 | HTML |
| [Another World Suite](https://github.com/malandrin/another-world-suite) | A Rust implementation of the "Another World" ("Out of This World" in the USA) game engine, compiled to WebAssembly to... | 65 | 🔴 | Rust |
| [DirkSimple](https://github.com/icculus/DirkSimple) | DirkSimple, a minimal player for the Dragon's Lair laserdisc game | 65 | 🟢 | Assembly |
| [libnpengine](https://github.com/FGRE/libnpengine) | Free implementation of Nitroplus/5pb. Visual Novel game engine | 65 | 🔴 | C++ |
| [OpenDance](https://github.com/WodsonKun/OpenDance) | Recreation of the Just Dance engine in GameMaker | 65 | 🟢 | Game Maker Language |
| [Total Annihilation 3D](https://github.com/zuzuf/TA3D) | Portable remake of Total Annihilation in 3D | 64 | 🔴 | C |
| [Open76](https://github.com/r1sc/Open76) | Interstate '76 engine reimplementation | 63 | 🔴 | C# |
| [shin](https://github.com/DCNick3/shin) | A reimplementation of VN engine primarily used by 07-th expansion releases on consoles (and some other entergram games) | 63 | 🟢 | Rust |
| [scion](https://github.com/nsgomez/scion) | Reimplementation of the Maxis engine used by The Sims 2 and SimCity 4 | 62 | 🟡 | C++ |
| [Nitro](https://github.com/billsonnn/nitro-react) | HTML5 Habbo Hotel client reimplementation in React | 61 | 🟢 | TypeScript |
| [Blues](https://github.com/cyxx/blues) | Blues Brothers, Jukebox Adventure & Prehistorik 2 engine reimplementation (PSP, SDL2) | 60 | 🗄️ | C |
| [OpenDrakan](https://github.com/Zalasus/opendrakan) | A work-in-progress recreation of Surreal Software's Riot Engine | 60 | 🟡 | C++ |
| [redstone-js](https://github.com/LostMyCode/redstone-js) | Play RED STONE ONLINE in the browser | 60 | 🟢 | JavaScript |
| [lilium-voyager](https://github.com/clover-moe/lilium-voyager) | An engine replacement for Star Trek Voyager: Elite Force Holomatch (multiplayer). | 59 | 🟢 | C |
| [OpenWar](https://github.com/andreas-jonsson/openwar) | Classic fantasy RTS game in the spirit of Warcraft: Orcs & Humans. | 59 | 🔴 | Go |
| [Colditz Escape](https://github.com/aperture-software/colditz-escape) | Amiga's "Escape From Colditz" ported to Windows, Linux, macOS and PSP | 58 | 🟡 | C |
| [Cryogenic](https://github.com/OpenRakis/Cryogenic) | An open-source reimplementation of Cryo's DUNE game (WIP) | 58 | 🟢 | C# |
| [FPC Atomic](https://github.com/PascalCorpsman/fpc_atomic) | Playable clone of the legendary Atomic Bomberman including Network and Ai https://en.wikipedia.org/wiki/Atomic_Bomberman | 58 | 🟢 | Pascal |
| [LasMarionetas](https://github.com/OmniBlade/LasMarionetas) | Open-source reimplementation of The Sims | 58 | 🔴 | C++ |
| [Mikompilation](https://github.com/Mikompilation/Mikompilation) | Reimplementation project for the Fatal Frame 2 : Crimson Butterfly (Project Zero 2/零～紅い蝶) game engine | 58 | 🟡 | C |
| [REminiscence / REinforced](https://github.com/chermenin/REminiscence) | REminiscence is a re-implementation of the engine used in the game Flashback made by Delphine Software. | 58 | 🟢 | C++ |
| [rock-raiders-remake](https://github.com/rystills/rock-raiders-remake) | Partial HTML5 remake of the classic game "Lego Rock Raiders". | 58 | 🔴 | JavaScript |
| [u6-decompiled](https://github.com/ergonomy-joe/u6-decompiled) | Decompiled code for PC/MSDOS version of Ultima VI - The False Prophet | 58 | 🔴 | C |
| [freeage](https://github.com/puzzlepaint/freeage) | Open-source reimplementation of the Age of Empires 2: Definitive Edition engine | 57 | 🗄️ |  |
| [Nitrosharp](https://github.com/CommitteeOfZero/nitrosharp) | Open-source N2System reimplementation | 57 | 🟢 | C# |
| [OpenCrashWOC](https://github.com/Open-Travelers/OpenCrashWOC) | Reverse engineered reimplementation of Crash Bandicoot: The Wrath of Cortex | 57 | 🟢 | C |
| [WolfensteinRPG-RE](https://github.com/Erick194/WolfensteinRPG-RE) | Wolfenstein RPG reverse engineering and reimplementation | 57 | 🟡 | C++ |
| [RSDKv2 Decompilation](https://github.com/RSDKModding/RSDKv2-Decompilation) | a Decompilation of the 2008 Retro-Sonic Engine Demo of Sonic Nexus | 56 | 🟢 | C++ |
| [sioux](https://github.com/hanatos/sioux) | Open-source reimplementation of the Comanche 3 helicopter sim engine | 56 | 🟡 | C |
| [TOD_tools](https://github.com/Michael0ne/TOD_tools) | Reversed engine and tools of Total Overdose (2005, PC) | 56 | 🟡 | C++ |
| [ReChan](https://github.com/SilverwireGames/ReChan) | Jackie Chan Stuntmaster reimplementation | 55 | 🟢 | C++ |
| [SF2DISASM](https://github.com/ShiningForceCentral/SF2DISASM) | A disassembly of the game "Shining Force II" for documentation and fan-project purposes. | 55 | 🟢 | Assembly |
| [Stardust rebuilt](https://github.com/TheJare/stardust-48k) | Reverse engineered source for the 1987 Sinclair Spectrum game "Stardust" | 55 | 🔴 | Assembly |
| [MegaManX5Recomp](https://github.com/mstan/MegaManX5Recomp) | Mega Man X5 (USA, SLUS-01334) statically recompiled to a native Windows executable with the PSXRecomp framework. | 54 | 🟢 | PowerShell |
| [Prince-Monogame](https://github.com/salvadorc17/Prince-Monogame) | Monogame implementation of Prince of Persia 2. | 54 | 🟢 | C# |
| [Airline Tycoon](https://github.com/openairlinetycoon/AirlineTycoon) | Source code of Airline Tycoon based on the GOG source code release | 53 | 🔴 | C++ |
| [engge2](https://github.com/scemino/engge2) | Open source remake of Thimbleweed Park's engine | 53 | 🟡 | Nim |
| [open-rct3](https://github.com/open-rct3/open-rct3) | Open-source re-implementation of RollerCoaster Tycoon 3 | 53 | 🟢 | C# |
| [ReksioEngine](https://github.com/ReksioEngine/ReksioEngine) | Reimplementation of the BlooMoo and Piklib engines for the Reksio PC games | 53 | 🟢 | TypeScript |
| [wacki](https://github.com/mszula/wacki) | From-scratch C/SDL2 reimplementation of Wacki (1998) from reverse-engineered opcodes | 53 | 🟢 | C |
| [open-reckless-drivin](https://github.com/natecraddock/open-reckless-drivin) | Open-source reimplementation of the Macintosh shareware game Reckless Drivin' | 52 | 🟡 | Zig |
| [SimUnity2](https://github.com/LazyDuchess/SimUnity2) | Attempt at a reimplementation of The Sims 2 Ultimate Collection in the Unity Engine... | 52 | 🗄️ | C# |
| [BtBuilder](https://github.com/dulsi/btbuilder) | An open source implementation of the Bard's Tale Construction Set. | 51 | 🟢 | C |
| [femto8](https://github.com/benbaker76/femto8) | Open-source reimplementation of the PICO-8 fantasy console for embedded systems | 51 | 🟢 | C |
| [OpenNitemare3D](https://github.com/BBQGiraffe/OpenNitemare3D) | reimplementation of the 1994 FPS Nitemare 3D | 51 | 🔴 | C# |
| [DesktopAdventures](https://github.com/shinyquagsire23/DesktopAdventures) | A recreation of the Desktop Adventures engine in C | 50 | 🔴 | C |
| [Mechanized Assault & eXploration Reloaded](https://github.com/maxr-dot-org/maxr) | A turn based strategy game | 50 | 🟢 | C++ |
| [OpenRayman](https://github.com/imaginaryPineapple/OpenRayman) | Open-source reimplementation of the Rayman 2 engine | 50 | 🔴 | C |
| [CorrinoEngine](https://github.com/cookgreen/CorrinoEngine) | CorrinoEngine is an open-source RTS engine inspired by Emperor: Battle for Dune, with Emperor: Battle for Dune compat... | 49 | 🟢 | C# |
| [de Blob (OpenToshi)](https://github.com/AdventureT/OpenToshi) | Reverse-engineered reimplementation / port of de Blob (OpenToshi) | 49 | 🟢 | C++ |
| [jsFO](https://github.com/ajxs/jsFO) | Fallout 2 Javascript port | 48 | 🟢 | JavaScript |
| [OpenLGR](https://github.com/james-knippes/openlgr) | Engine reimplementation of Lego Racers; uses original game data (C) | 48 | 🗄️ | C |
| [libRealSpace](https://github.com/remileonard/libRealSpace) | Tools to parse and render Origin Systems RealSpace engine assets. | 47 | 🟢 | C++ |
| [OpenAdhoc](https://github.com/Nenkai/OpenAdhoc) | Open-source re-implementation of Gran Turismo Adhoc scripts | 46 | 🟢 | C |
| [sacengine](https://github.com/tg-2/sacengine) | Engine reimplementation for Sacrifice by Shiny Entertainment | 46 | 🟢 | D |
| [GLKeeper](https://github.com/codenamecpp/GLKeeper) | Open Source Dungeon Keeper 2 Reimplementation | 45 | 🟢 | C++ |
| [Lemmix](https://github.com/ericlangedijk/Lemmix) | Lemmix Main Source Code - Lemmings Clone | 45 | 🔴 | Pascal |
| [OpenBattlefield2](https://github.com/Moxnatiy/OpenBattlefield2) | Clean-room reimplementation of DICE's Refractor 2 engine (Battlefield 2) | 45 | 🟢 | C++ |
| [OpenSHC](https://github.com/sourcehold/OpenSHC) | An open source re-implementation of Stronghold Crusader | 45 | 🟢 | C++ |
| [OpenGTA](https://github.com/madebr/OpenGTA) | OpenGTA: copy of http://ogta.fifengine.de/ | 44 | 🔴 | C++ |
| [RAD](https://github.com/jval1972/Rad-X) | RAD: Remake of the game "Radix - Beyond the void" | 44 | 🟡 | Pascal |
| [reevengi](https://github.com/pmandin/reevengi) | Resident Evil engine reimplementation | 44 | 🔴 | C |
| [Blast Corps](https://github.com/retroplastic/blastcorps) | A Blast Corps decompilation. | 43 | 🔴 | C |
| [mdk-sdl](https://github.com/nemo22/mdk-sdl) | Port of Shiny's MDK (1997) to C# and SDL3 based on reverse engineering | 43 | 🟢 | C# |
| [abyssal](https://github.com/TheWWWorm/abyssal) | Godot engine edition of Deep 3D: Submarine Odyssey by Fishlabs | 42 | 🟢 | GDScript |
| [Chrono Trigger C](https://github.com/buzzer-re/Chrono-Trigger-C) | A simple remake of Chrono Trigger written in C, using the SDL API | 41 | 🗄️ | C |
| [Jurassic Park: Operation Genesis (OpenJPOG)](https://github.com/AdventureT/OpenJPOG) | Reverse-engineered reimplementation / port of Jurassic Park: Operation Genesis (OpenJPOG) | 41 | 🟢 | C++ |
| [OpenSith](https://github.com/r1sc/OpenSith) | Jedi Knight: Dark Forces II engine reimplementation | 41 | 🟡 | C# |
| [pfr](https://github.com/wanda-phi/pfr) | Pinball Fantasies (1992) reverse engineered and re-created | 41 | 🟡 | Rust |
| [Phoenix](https://github.com/joulupunikki/Phoenix) | Java clone/remake/patch of the game Emperor of the Fading Suns | 41 | 🔴 | Java |
| [F-Zero X (USA)](https://github.com/BttrDrgn/f-zerox) | F-Zero X Decompilation | 40 | 🔴 | C |
| [FelineSystem2](https://github.com/kokseen1/FelineSystem2) | Open-source remake of the CatSystem2 visual novel engine | 40 | 🔴 | C++ |
| [JLud2D](https://github.com/rafael-esper/JLud2D) | 2D old-school Engine for Games | 40 | 🟢 | TypeScript |
| [ChronoStorm](https://github.com/cookgreen/ChronoStorm) | Open-source engine reimplementation of Command & Conquer: Red Alert 2 and Yuri's Revenge | 39 | 🟢 | Python |
| [openSMB2](https://github.com/Matriks404/openSMB2) | Open-source reimplementation of Super Mario Bros. 2 in Lua and LOVE | 39 | 🗄️ | Lua |
| [Quest 64 Decompilation](https://github.com/Mallos31/Quest) | decompilation of Quest64 | 39 | 🟡 | C |
| [smb1-disasm](https://github.com/laura240406/smb1-disasm) | A collection to build SMB1 from the disassembly | 39 | 🔴 | Assembly |
| [Super Mario Bros. 3Mix](https://github.com/captainsouthbird/3Mix) | Super Mario Bros 3Mix hack | 39 | 🔴 | Assembly |
| [earthbound](https://github.com/Herringway/earthbound) | attempt at decompiling+porting earthbound | 38 | 🟡 | D |
| [freevgui](https://github.com/FWGS/freevgui) | Free and open-source reimplementation of the Half-Life VGUI library | 38 | 🟢 | C++ |
| [ChaseHQ](https://github.com/dpt/ChaseHQ) | Chase H.Q. for ZX Spectrum — reverse-engineered and reconstructed in portable C | 37 | 🟢 | C |
| [OpenRakis](https://github.com/OpenRakis/OpenRakis) | Tools for an open-source reimplementation of Cryo's Dune (1992) | 37 | 🟢 | Assembly |
| [OpenXeen](https://github.com/busyDuckman/OpenXeen) | Might and Magic engine rewrite. | 37 | 🔴 | Java |
| [openzt](https://github.com/openzt1/openzt) | WIP Reimplimentation of Zoo Tycoon (2001) | 37 | 🟢 | Rust |
| [JJFFE](https://github.com/videogamepreservation/jjffe) | John Jordan's reverse engineering of Frontier: First Encounters. | 35 | 🗄️ | Assembly |
| [Pokémon Anniversary Red](https://github.com/TwitchPlaysPokemon/pokemonAnniversaryRed) | Anniversary Red dissassembly | 35 | 🔴 | Assembly |
| [reb3](https://github.com/lolz0r/reb3) | Partial reverse-engineered rebuild of Burnout 3: Takedown | 35 | 🟢 | C |
| [sadx_decomp](https://github.com/FraGag/sadx_decomp) | Sonic Adventure DX Decompilation | 35 | 🗄️ | C |
| [rsc-remastered](https://github.com/Danjb1/rsc-remastered) | Reverse-engineered implementation of the RuneScape Classic client | 34 | 🔴 | Java |
| [Contra_remake](https://github.com/EmileSonneveld/Contra_remake) | The first level of a cool arcade game remade in c++ | 33 | 🔴 | JavaScript |
| [F.LF](https://github.com/tyt2y3/F.LF) | Clean-room implementation of the fighting game Little Fighter 2 | 33 | 🔴 | HTML |
| [OpenTitus](https://github.com/stople/OpenTitus) | A port of the game engine behind the DOS versions of Titus the Fox and Moktar | 33 | 🔴 |  |
| [PyTouhou](https://github.com/GovanifY/PyTouhou) | Open-source reimplementation of the Touhou Generation 1 Windows engine | 33 | 🔴 | Python |
| [Mario-Bros.-Dis](https://github.com/RussianManSMWC/Mario-Bros.-Dis) | Mario Bros. (NES) Disassembly | 32 | 🟢 | Assembly |
| [Re-Comprehend](https://github.com/RyanMallon/recomprehend) | Open source implementation of the Comprehend adventure game engine used by the games Transylvania, Crimson Crown, and... | 32 | 🔴 | C |
| [The Castles of Dr. Creep](https://github.com/segrax/DrCreep) | The Castles of Dr. Creep | 32 | 🔴 | C++ |
| [Dungeon Craft](https://github.com/grannypron/uaf) | Engine reimplementation of Forgotten Realms: Unlimited Adventures; uses original game data (C++) | 31 | 🟢 | C++ |
| [Lode Runner 2020](https://github.com/Ma-Pe-Ma/Lode-Runner-2020) | A remake of the classic '80s puzzle game! | 31 | 🟢 | C++ |
| [REminiscence](https://github.com/cyxx/REminiscence) | Flashback engine reimplementation (Android, SDL) | 31 | 🗄️ | C++ |
| [Rosebed](https://github.com/mdmrk/rosebed) | From-scratch Zig reimplementation of Minecraft Beta 1.7.3 client and server, protocol-compatible | 31 | 🟢 | Zig |
| [Shining Force 2 Reverse Engineer (SF2RE)](https://github.com/ShiningForceCentral/SF2RE) | Collaborative work on reverse-engineering Shining Force II, and source of main project SF2DISASM (see website link) | 31 | 🟡 | C |
| [Doom 64 for Dreamcast](https://github.com/jnmartin84/doom64-dc) | Doom 64 port for Sega Dreamcast / KallistiOS | 30 | 🟢 | C |
| [OpenMM2](https://github.com/0x1F9F1/OpenMM2) | Open-source re-implementation of Midtown Madness 2 | 30 | 🗄️ | C |
| [Future Cop: MIT](https://github.com/Ghoster738/Future-Cop-MIT) | Open Source Game Engine Project | 29 | 🟢 | C++ |
| [OpenOrion2](https://github.com/nextghost/openorion2) | Open-source remake of Master of Orion II: Battle at Antares | 29 | 🟢 | C++ |
| [beatfever](https://github.com/Sulunia/beatfever) | Partial open-source reimplementation of the osu! game engine in Lua/LOVE | 28 | 🔴 | Lua |
| [Bermuda Syndrome](https://github.com/cyxx/bermuda) | Bermuda Syndrome engine reimplementation (Emscripten, libretro, SDL2) | 28 | 🗄️ | C++ |
| [Magnetar](https://github.com/joankaradimov/Magnetar) | Magnetar is a StarCraft: Brood War mod/reimplementation. | 28 | 🟡 | C++ |
| [mengde](https://github.com/wateret/mengde) | A turn-based RPG game engine inspired by 三國志曹操傳. | 28 | 🔴 | C++ |
| [SiegeFX](https://github.com/codingncaffeine/SiegeFX) | Open-source reimplementation of Dungeon Siege (2002) in C# | 28 | 🟢 | C# |
| [freetfc](https://github.com/eukara/freetfc) | Clean-room reimplementation of Team Fortress Classic in QuakeC | 27 | 🟡 | C |
| [Heroes Of JinYong](https://github.com/soarqin/HeroesOfJinYong) | A reimplementation of the DOS game `The legend of Jin Yong Heroes(金庸群侠传)` | 27 | 🟢 | C++ |
| [kys-js](https://github.com/kt2/kys-js) | 《金庸群侠传》kys-js (pixijs) | 27 | 🔴 | JavaScript |
| [linyaga](https://github.com/cyxx/linyaga) | Humongous Yaga engine reimplementation | 27 | 🗄️ | C |
| [OpenCloud](https://github.com/Gundorada-Workshop/OpenCloud) | Open source reimplementation of the Dark Cloud games | 27 | 🟡 | C++ |
| [opengta2](https://github.com/ikkentim/opengta2) | Open-source re-implementation of GTA II in C# using the original assets | 27 | 🟢 | C# |
| [WinTex](https://github.com/ElakaSnarne/WinTex) | Engine reimplementation of Under a Killing Moon; uses original game data (C++) | 27 | 🟢 | C++ |
| [Thirdeye](https://github.com/psi29a/thirdeye) | Reimplementation of AESOP that runs Eye of the Beholder 3 and Dungeon Hack. | 26 | 🟢 | C++ |
| [vigasocosdl-la-abadia-del-crimen](https://github.com/luzbel/vigasocosdl-la-abadia-del-crimen) | Automatically exported from code.google.com/p/vigasocosdl-la-abadia-del-crimen | 26 | 🔴 | Assembly |
| [DungeonMaster.NET](https://github.com/ggrrin/DungeonMaster.NET) | Reimplementation of famous old Dungeon Master game. | 25 | 🔴 | C# |
| [freegunman](https://github.com/eukara/freegunman) | Clean-room reimplementation of Gunman Chronicles in QuakeC | 25 | 🟡 | C |
| [Iris2](https://github.com/kblaschke/Iris2) | An Open-Source 3D Ultima Online(tm) Client. No active development, mostly for archival purposes as the original proje... | 25 | 🔴 | C |
| [skyroads-port](https://github.com/ammaarreshi/skyroads-port) | 1:1 reverse-engineered portable port of SkyRoads (1993) in C11 + SDL2 | 25 | 🟢 | C |
| [goldsrc-reversed-steam_api](https://github.com/oxiKKK/goldsrc-reversed-steam_api) | Reverse-engineered steam_api module shipped with the GoldSource engine | 24 | 🔴 | C++ |
| [Harold](https://github.com/OldGamesLab/Harold) | Open-source Fallout 2 engine implementation, a revival of darkfo project | 24 | 🔴 | TypeScript |
| [zztjs](https://github.com/bstreiff/zztjs) | ZZT game engine reimplemented in JavaScript | 24 | 🗄️ | JavaScript |
| [Bedlam 2: Absolute Bedlam](https://github.com/8street/Bedlam2) | Source code for Bedlam 2 (1997) game executable file. | 23 | 🔴 | Assembly |
| [F-Zero Clone](https://github.com/chipbell4/F-Zero-Clone) | A WebGL F-Zero clone. Show ya moves! | 23 | 🔴 | JavaScript |
| [OpenMM1](https://github.com/0x1F9F1/OpenMM1) | Open-source re-implementation of Midtown Madness 1 | 23 | 🗄️ | C++ |
| [OpenNox](https://github.com/noxworld-dev/opennox) | Open-source reimplementation of Nox | 23 | 🗄️ | C |
| [SF1DISASM](https://github.com/ShiningForceCentral/SF1DISASM) | A disassembly of the game "Shining Force" for documentation and fan-project purposes. | 23 | 🟢 | Assembly |
| [WoodyRE](https://github.com/jjmhalew/WoodyRE) | Engine reimplementation of Woody Woodpecker: Escape from Buzz Buzzard Park (PC, 2001) - plays the original game from... | 23 | 🟢 | C |
| [cc94](https://github.com/institution/cc94) | Remake of 1994 Sid Meier's Colonization game | 22 | 🔴 | C++ |
| [DuckHunt](https://github.com/grosbouddha/duckhunt) | Canvas based remake of the NES DuckHunt game. | 22 | 🔴 | JavaScript |
| [Igor](https://github.com/cyxx/igor) | Igor: Objetivo Uikokahonia game interpreter (Android, SDL) | 22 | 🗄️ | C++ |
| [piney_apples](https://github.com/Toyz/piney_apples) | Native Rust port of the PS2 .hack engine from reverse engineering | 22 | 🟢 | Rust |
| [wkbre2](https://github.com/AdrienTD/wkbre2) | WK Engine Reimplementation Rewrite with Multiplayer support! | 22 | 🟢 | C++ |
| [captain-bible-re](https://github.com/peterkelly/captain-bible-re) | Reverse engineering of the 1994 DOS game Captain Bible in the Dome of Darkness | 21 | 🟢 | Rust |
| [COD4-Rewrite](https://github.com/Nilbong/COD4-Rewrite) | Call of Duty 4 multiplayer reimplemented in Rust on Bevy. Bring your own game files. | 21 | 🟢 | Rust |
| [LOZ](https://github.com/aldonunez/Loz) | A remake of The Legend of Zelda | 21 | 🔴 | C++ |
| [Q2RTXPerimental](https://github.com/PolyhedronStudio/Q2RTXPerimental) | My 'Experimental' fork of NVIDIA’s implementation of RTX ray-tracing in Quake II | 21 | 🟢 | C++ |
| [REminiscence](https://github.com/libretro/REminiscence) | Flashback engine reimplementation | 21 | 🟢 | C++ |
| [shock2quest](https://github.com/tommy-xr/shock2quest) | Unofficial recreation of the Dark engine for System Shock 2 on Quest | 21 | 🟢 | Rust |
| [7k2](https://github.com/7k2/7k2) | Experimental fork of Seven Kingdoms II: The Fryhtan Wars | 20 | 🔴 | C++ |
| [Chocolate Blood](https://github.com/NBlood/chocolate-blood) | Chocolate Doom inspired Blood port (heavily WIP) | 20 | 🟡 | C |
| [OpenBreed](https://github.com/mrpetro/OpenBreed) | Open source reimplementation of classic Alien Breed 2D games and editor. | 20 | 🟢 | C# |
| [Sonic Lost World (OpenLW)](https://github.com/Radfordhound/OpenLW) | Reverse-engineered reimplementation / port of Sonic Lost World (OpenLW) | 20 | 🟡 | C++ |
| [wkbre](https://github.com/AdrienTD/wkbre) | Warrior Kings (Battles) game engine reimplementation / recreation | 20 | 🟡 | C++ |
| [Amiga Cannonball-C](https://github.com/lantus/Cannonball-C) | Cannonball for the Amiga ported to C | 19 | 🔴 | C |
| [Daikatana Restoration Project](https://github.com/atsb/daikatana-restoration-project) | Daikatana restoration aiming to have a clean 1.2 source and to support modern systems | 19 | 🟢 | C++ |
| [hobbitgfx](https://github.com/richcarl/hobbitgfx) | The Hobbit graphics engine | 19 | 🔴 | JavaScript |
| [jy-remake](https://github.com/scarsty/jy-remake) | Zgames制作的《金庸群侠传》复刻版 | 19 | 🟢 | C |
| [RPG-X](https://github.com/UberGames/rpgxEF) | A modifaction of ioEF with increased limits for RPG-X2, now including the gamecode | 19 | 🟢 | C |
| [T.O.R.E Fighters](https://github.com/john-overton/T.O.R.E-Fighters) | Reverse-engineered rebuild of Jane's Fighters Anthology flight sim | 19 | 🟢 | Rust |
| [zorkClone](https://github.com/vatbub/zorkClone) | Reimplementation of the original Zork game developed by Infocom. | 19 | 🔴 | Java |
| [Concilia Tower](https://github.com/Jonahss/concilia-tower) | Ground-up rewrite of SimTower (1994) from decompilation, playable in the browser | 18 | 🟢 | C |
| [invaders (in C)](https://github.com/herrecito/invaders) | A Space Invaders / Intel 8080 emulator | 17 | 🔴 | C |
| [Octopus](https://github.com/roger-wetzel/Octopus) | Remake of Nintendo's Octopus Game & Watch device for Apple TV 4 | 17 | 🔴 | Swift |
| [Pokémon Red++](https://github.com/jayceekaycee/RedPlusPlus) | An upgrade to Pokémon Red. Fixes several bugs and adds a lot of new features. Now a standalone repository, so you can... | 17 | 🔴 | Assembly |
| [realice](https://github.com/FWGS/realice) | Heavy Metal F.A.K.K. 2 / American McGee's Alice reverse engineered. | 17 | 🟢 | C |
| [Arcanum on iOS](https://github.com/arcanum-project/game) | Engine reimplementation of Arcanum: Of Steamworks and Magick Obscura; uses original game data (C++) | 16 | 🔴 | C++ |
| [Castlekeep](https://github.com/leidav/Castlekeep) | Reimplementation of Stronghold 1 | 16 | 🔴 | C++ |
| [Desktop Adventures Engine for ScummVM](https://github.com/digitall/scummvm-deskadv) | Desktop Adventures Engine for ScummVM | 16 | 🔴 | C++ |
| [Minecraft: Pocket Edition (mcpe-engine)](https://github.com/BrentDaMage/mcpe-engine) | Reverse-engineered reimplementation / port of Minecraft: Pocket Edition (mcpe-engine) | 16 | 🟢 | C++ |
| [OpenOP2](https://github.com/OpenOP2/OpenOP2) | OpenOP2 is a re-implementation of the gameplay inspired by colony building games like Outpost 2, using the OpenRA eng... | 16 | 🟢 | C# |
| [Project ANISE](https://github.com/tomyun/anise) | 🦋 Project ANISE (A Newly Implemented Scripting Engine for AI5V) | 16 | 🔴 | C++ |
| [Command Series Engine](https://github.com/pwiecz/command_series) | Engine for playing Command Series games by Sid Meier/Microprose | 15 | 🟢 | Go |
| [ktes2](https://github.com/sonicretro/ktes2) | Knucles the Echidna in Sonic 2 | 15 | 🔴 | Assembly |
| [SFCDDISASM](https://github.com/ShiningForceCentral/SFCDDISASM) | A disassembly of the game "Shining Force CD" for documentation and fan-project purposes. | 15 | 🔴 | Assembly |
| [Ultima 5](https://github.com/synthwave-pixel/ultima5) | Modern engine for Ultima 5. | 15 | 🟢 | TypeScript |
| [earth-shaker](https://github.com/Palevolg/earth-shaker) | Remake of an old ZX-spectrum game "EarthShaker" on Unity | 14 | 🔴 | C# |
| [OpenBound](https://github.com/WickedPeanuts/OpenBound) | This project aims to mimic the older PC versions of Gunbound with optimized behavior, engine and gameplay elements. T... | 14 | 🟡 | C# |
| [sims-3-bevy](https://github.com/Eamo5/sims-3-bevy) | Work-in-progress reimplementation of The Sims 3 in the Bevy game engine | 14 | 🟢 | Rust |
| [Zuma Portable](https://github.com/kyle-sylvestre/CircleShootApp) | Zuma Deluxe (1.0.0) decompilation ported to newer platforms | 14 | 🟢 | C++ |
| [Atari8bit_StarRaiders](https://github.com/sidneycadot/Atari8bit_StarRaiders) | A repository dedicated to reverse engineering the classic 1979 game Star Raiders for the Atari 400/800/XL/XE platform. | 13 | 🔴 | Assembly |
| [Cannon Fodder](https://github.com/krazyjakee/CannonFodder) | HTML5 Remake of an Amiga Classic | 13 | 🔴 | JavaScript |
| [mhlib](https://github.com/Theaninova/mhlib) | A project to make the old classic Moorhuhn Games playable on modern systems via an engine reimplementation, written i... | 13 | 🔴 | Rust |
| [OpenKingdoms](https://github.com/OpenKingdoms/OpenKingdoms) | Open-source engine reimplementation of Total Annihilation: Kingdoms (C11, native + WebAssembly). Bring your own game... | 13 | 🟢 | C |
| [remc1](https://github.com/turican0/remc1) | Recode Binary code of game Magic Carpet1 to C/C++ language(remake MC1 for any platform) | 13 | 🔴 | C++ |
| [Tile World 2](https://github.com/SicklySilverMoon/tworld) | The current fork of Tile World 2, including Qt6 support, and other game patches | 13 | 🟢 | C |
| [Arkanum](https://github.com/vleon1/Arkanum) | Arcanum game engine recreation | 12 | 🔴 | Python |
| [DNF-reimposition](https://github.com/vini1264/DNF-Enhanced) | Set of gameplay enhancements for Duke Nukem Forever (2011) | 12 | 🔴 | C |
| [EF2GameSource](https://github.com/UberGames/EF2GameSource) | The original EF2GameSource updated so it compiles under Visual Studio 2012 and Linux | 12 | 🔴 | C++ |
| [erampage](https://github.com/ttyborg/erampage) | Automatically exported from code.google.com/p/erampage | 12 | 🔴 | C |
| [openDOW](https://github.com/rofl0r/openDOW) | remake of the classic amiga game "dogs of war" (C) 1989 elite | 12 | 🟡 | C |
| [Plants vs. Zombies GOTY (re-plants-vs-zombies)](https://github.com/Bamcane/re-plants-vs-zombies) | Reverse-engineered reimplementation / port of Plants vs. Zombies GOTY (re-plants-vs-zombies) | 12 | 🟢 | C++ |
| [ReDMCSB](https://github.com/gondur/ReDMCSB_Release2) | ReDMCSB Release2 source code by Christophe Fontanel | 12 | 🔴 | Assembly |
| [SuperLemminiToo](https://github.com/Blazingstix/SuperLemminiToo) | My personal fork of SuperLemmini, which itself is a fork of Lemmini | 12 | 🔴 | Java |
| [Amber](https://github.com/Pyrdacor/Amber) | Engine for the Amber trilogy | 11 | 🟢 | C# |
| [gta1_re](https://github.com/CriminalRETeam/gta1_re) | Engine reimplementation of Grand Theft Auto; uses original game data (C++) | 11 | 🟢 | C++ |
| [X-Settlers](https://github.com/skarmux/x-settlers) | Re-implementation of classic "TheSettlers" game series using modern technologies like hardware accelerated graphics a... | 11 | 🔴 | C++ |
| [DCSpeedBall2](https://github.com/LemonHaze420/DCSpeedBall2) | SpeedBall 2 for Pocket PC/Dreamcast (WCE), with special thanks to Comby Laurent and LemonHaze | 10 | 🔴 | C++ |
| [firestaff](https://github.com/yeager/firestaff) | 🔥 Source-faithful Dungeon Master engine — DM1, CSB, DM2, DM Nexus and Theron's Quest on modern hardware. macOS, Windo... | 10 | 🟢 | C |
| [Heart of the Alien Redux](https://github.com/carstene1ns/hota-redux) | Heart of The Alien - Redux (forked from https://hota.sf.net) | 10 | 🟢 | C |
| [LibertyFlux](https://github.com/monstercameron/LibertyFlux) | GTA IV engine rewritten in Rust function by function by AI agents for Windows x64 and ARM | 10 | 🟢 | Rust |
| [sm64js](https://github.com/sm64jsarchive/sm64jsarchive) | Super Mario 64 reimplementation in JavaScript. | 10 | 🟡 | JavaScript |
| [Cut the Rope](https://github.com/Bingies24/cuttherope-dx) | Reverse-engineered reimplementation / port of Cut the Rope | 9 | 🟢 | C# |
| [dizgruntled-java](https://github.com/Hugheth/dizgruntled-java) | A java open source remake of Monolith Gruntz (1999) | 9 | 🔴 | Java |
| [ebbsrc](https://github.com/Herringway/ebbsrc) | earthbound beginnings source recreation | 9 | 🟡 | Assembly |
| [Megaman3NESRecomp](https://github.com/mstan/Megaman3NESRecomp) | Mega Man 3 recompiled for the NES using nesrecomp · Part of the R.A.I.D. community | 9 | 🟢 | C |
| [olduvai](https://github.com/ksokolowski/olduvai) | From-scratch C++/SDL2 reimplementation of the Prehistorik (1991) engine — bring your own game files. | 9 | 🟢 | C++ |
| [opendaed](https://github.com/AMDmi3/opendaed) | Libre reimplementation of The Daedalus Encounter game | 9 | 🔴 | C++ |
| [Powerslide remake](https://github.com/dm999/powerslideremake) | Project remakes main features of video game Powerslide | 9 | 🟢 | C++ |
| [re3-Resurrected](https://github.com/cinchitsolutions/re3-Resurrected) | Clean-room reverse engineering of GTA III / Vice City for PC | 9 | 🟡 | C++ |
| [rust-theft-auto](https://github.com/gaudecker/rust-theft-auto) | Grand Theft Auto engine reimplementation in Rust | 9 | 🔴 | Rust |
| [Chuckie-Egg](https://github.com/pbrook/Chuckie-Egg) | Reverse-engineered Chuckie Egg with ASCII and 3D renderers | 8 | 🔴 | C |
| [free-heroes4](https://github.com/tallowmere/free-heroes4) | Open-source C++23 reimplementation of the Heroes of Might and Magic IV engine | 8 | 🟢 | C++ |
| [i76-everywhere](https://github.com/therealjkvalentine/i76-everywhere) | Interstate '76 on Apple Silicon, Steam Deck and modern Windows, with save editor and RE notes | 8 | 🟢 | Python |
| [Lupin Sansei - Pandora no Isan](https://github.com/PavelSha/Lupin-Sansei---Pandora-no-Isan) | An annotated disassembly of the famicom game "Lupin Sansei - Pandora no Isan" (1987). | 8 | 🟢 | Assembly |
| [open-northland](https://github.com/s-nems/open-northland) | A modern, open-source reimplementation of the Cultures game series | 8 | 🟢 | TypeScript |
| [Prehistorik_js](https://github.com/cyxx/prehistorik_js) | Prehistorik (Demo) engine reimplementation (Emscripten, SDL2) | 8 | 🗄️ | C |
| [rustyworld](https://github.com/EdMcBane/rustyworld) | Frame-accurate Another World engine reimplementation in Rust | 8 | 🟡 | Rust |
| [th10](https://github.com/YomotsuHisami/th10) | A high-fidelity, portable reimplementation of 東方風神録 ～ Mountain of Faith ver 1.00a. | 8 | 🟢 | C++ |
| [WAGE](https://github.com/asvitkine/wage-engine) | World Builder game engine | 8 | 🔴 | Java |
| [Balloon Fight](https://github.com/MikeDX/balloon-fight) | Remake of Balloon fight by Groovy Gecko, created for the Retro Remakes competition 2003 | 7 | 🔴 | xBase |
| [chaos-head](https://github.com/FGRE/chaos-head) | Reimplementation of Chaos;Head visual novel | 7 | 🔴 | CMake |
| [Dungeon Strikes Back](https://github.com/sparkletwist/DSB) | Dungeon Strikes Back | 7 | 🟡 | C |
| [Minecraft-4K-Decompilation](https://github.com/CelestialAmber/Minecraft-4K-Decompilation) | Decompilation of Minecraft 4K, updated to be a regular application | 7 | 🟢 | Java |
| [Ozymandias](https://github.com/Banderi/Ozymandias) | An open source re-implementation of Pharaoh (1999)'s game engine in Godot 3.6 | 7 | 🟢 | GDScript |
| [re3bevy](https://github.com/imbevystar/rust-gta-3) | Unofficial GTA III reimplementation in Rust with the Bevy engine and ECS | 7 | 🟢 | Rust |
| [remc1hw](https://github.com/turican0/remc1hw) | Recode Binary code of game/datadisk Magic Carpet1 Hidden Words to C/C++ language(remake MC1 for any platform) | 7 | 🔴 | C++ |
| [Starfox 64: Recompiled](https://github.com/worleydl/Starfox64Recomp-uwp) | Static recompilation of Starfox 64 for PC (Windows/Linux) (Unofficial UWP) | 7 | 🟢 | C |
| [SuperStarTrek25thGMS](https://github.com/JeodC/SuperStarTrek25thGMS) | A port of Super Star Trek Meets 25th Anniversary to Game Maker Studio 2 | 7 | 🟢 | Game Maker Language |
| [TetrisGBRecomp](https://github.com/mstan/TetrisGBRecomp) | Tetris recompiled for the Game Boy using a fork of gb-recompiled · Part of the R.A.I.D. community | 7 | 🟢 | C |
| [timeco](https://github.com/LBALab/timeco) | Time Commando Reimplementation | 7 | 🟢 | C |
| [TsumuLightRecomp](https://github.com/mstan/TsumuLightRecomp) | Tsumu Light (Japan) recompiled for the Sony PlayStation using psxrecomp, with an English fan-translation · Part of th... | 7 | 🟢 | PowerShell |
| [jy2-copy](https://github.com/MngYou/jy2-copy) | Engine reimplementation of Heroes of Jin Yong 2; uses original game data (JavaScript) | 6 | 🔴 | JavaScript |
| [OpenJill](https://github.com/emeric-martineau/openjill) | Official OpenJill project source repository to understand how Jill of the Jungle game engine work and rewrite it in J... | 6 | 🗄️ | Java |
| [rechelon](https://github.com/pkulev/rechelon) | Echelon: free engine reimplementation | 6 | 🔴 | C# |
| [retruxx](https://github.com/mindflower/retruxx) | Reverse engineered Hard Truck Apocalypse. | 6 | 🟢 | C++ |
| [scale-miniatures](https://github.com/hivvu/scale-miniatures) | Micro Machines (PC, 1994) rewritten in TypeScript from the disassembly, running natively in the browser. No emulator.... | 6 | 🟢 | TypeScript |
| [sm_rewrite](https://github.com/enderandrew/sm_rewrite) | Super Metroid rewrite project | 6 | 🟡 | C |
| [The Bard's Tale III](https://github.com/Drunella/bt3-easyflash) | Bard's Tale III Easyflash Version | 6 | 🔴 | C |
| [wanderer](https://github.com/vinceh121/wanderer) | A reimplementation of the 2002 video game Project Nomads by Radon Labs | 6 | 🟢 | Java |
| [demcstify](https://github.com/stevefan1999-personal/demcstify) | Decompiles Minecraft with Vineflower and reconstructs code with an LLM | 5 | 🟢 | Shell |
| [openpol](https://github.com/jstasiak/openpol) | An open source reimplementation of the first Polish RTS video game Polanie (also known as VICTORY, OSADNICI) | 5 | 🟡 | Rust |
| [RetroLemmini](https://github.com/Willicious/RetroLemmini) | A newly-maintained version of Lemmini | 5 | 🟢 | Java |
| [Soul Blazer (RustyBlazer)](https://github.com/hellow554/RustyBlazer) | Reverse-engineered reimplementation / port of Soul Blazer (RustyBlazer) | 5 | 🟡 | Assembly |
| [GumshoeNESRecomp](https://github.com/mstan/GumshoeNESRecomp) | Gumshoe recompiled for the NES using nesrecomp · Part of the R.A.I.D. community | 4 | 🟢 | C |
| [hugo.js](https://github.com/cyxx/hugo_js) | Hugo pa Nye Eventyr/Hugo Délire player (Emscripten) | 4 | 🗄️ | C |
| [Jet-Story](https://github.com/adamenkov/jet-story) | Remake of the ZX Spectrum game "Jet-Story" | 4 | 🟢 | Assembly |
| [lilium-salvation](https://github.com/clover-moe/lilium-salvation) | An engine replacement for Dark Salvation | 4 | 🟢 | C |
| [Marble Love](https://github.com/magno73/marble-love) | TypeScript reimplementation of Atari's Marble Madness (1984), incl. Slapstic behaviour | 4 | 🟢 | TypeScript |
| [mb-decomp](https://github.com/Yoshimaster96/mb-decomp) | Engine reimplementation of Super Monkey Ball; uses original game data (C, Assembly) | 4 | 🔴 | C |
| [SuperFoulEgg](https://github.com/ant512/SuperFoulEgg) | Port of Super Foul Egg to MacOSX. | 4 | 🔴 | Objective-C |
| [Trashman](https://github.com/pobtastic/trashman) | A disassembly of Trashman, created using SkoolKit. | 4 | 🟡 | Visual Basic 6.0 |
| [v64tng](https://github.com/mattseabrook/v64tng) | Game Engine re-creation of The 7th Guest | 4 | 🟢 | Assembly |
| [xclannad](https://github.com/weimingtom/xclannad_fork) | My xclannad fork for study | 4 | 🔴 | C |
| [FFED3D](https://github.com/corpsofengineers/ffed3d) | Automatically exported from code.google.com/p/ffed3d | 3 | 🔴 | Assembly |
| [Hopmon (OpenHopmon)](https://github.com/Teofil98/OpenHopmon) | Reverse-engineered reimplementation / port of Hopmon (OpenHopmon) | 3 | 🟢 | C++ |
| [kys-promise](https://github.com/scarsty/kys-promise) | Engine reimplementation of Heroes of Jin Yong; uses original game data (Pascal) | 3 | 🟢 | Pascal |
| [LostVikings](https://github.com/akaWolf/LostVikings) | Translated and rewritten DOS version of Lost Vikings | 3 | 🟢 | C++ |
| [Oblivion-Reconstructed](https://github.com/themuffinator/Oblivion-Reconstructed) | Reverse-engineered Oblivion Extension Pack source code for original Quake II. | 3 | 🟢 | C |
| [S2HD](https://github.com/SonicOrcaModding/S2HD) | A decompile of Sonic 2 HD (Build 2.0.1012-rc2) and port to Linux, Android and iOS. | 3 | 🟢 | C# |
| [SF1RE](https://github.com/ShiningForceCentral/SF1RE) | Collaborative work on reverse-engineering Shining Force. | 3 | 🟡 | C |
| [Another World for the Commander X16](https://github.com/cosmicr/anotherx16) | Commander X16 Port of the Amiga Game Another World | 2 | 🟢 | Assembly |
| [MechCommander2HD](https://github.com/Ariemeth/MechCommander2HD) | Pending approval, this will be the place where the HD revamp will be tracked. | 2 | 🔴 | C++ |
| [NHL94](https://github.com/abdulahmad/NHL94Genesis) | Work In Progress reverse engineered source of NHL 94 for Sega Genesis. Requires original ROM file to build. | 2 | 🟢 | Assembly |
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
| [bumpy-reverse](https://github.com/GeReV/bumpy-reverse) | Decompilation of Bumpy's Arcade Fantasy, lead by Claude | 1 | 🟢 | C |
| [Chameleon Twist 2: Recompiled](https://github.com/Rainchus/ChameleonTwist2-JP-Recomp) | Engine reimplementation of Chameleon Twist 2; uses original game data (C++) | 1 | 🟡 | C |
| [earthbound_beginnings](https://github.com/Herringway/earthbound_beginnings) | Unfinished port of Earthbound Beginnings | 1 | 🟢 | D |
| [EarthShakerDS](https://github.com/ant512/EarthShakerDS) | Port of the classic ZX Spectrum game Earth Shaker to the Nintendo DS. | 1 | 🔴 | C++ |
| [ff1snes](https://github.com/Entroper/ff1snes) | FF1 for SNES, written from scratch. | 1 | 🟡 | Assembly |
| [NHLPA93Genesis](https://github.com/abdulahmad/NHLPA93Genesis) | Work In Progress reverse engineered source of NHLPA Hockey 93 for Sega Genesis. Requires original ROM file to build. | 1 | 🟢 | Assembly |
| [PanzerMortyr](https://github.com/Panzerschrek/PanzerMortyr) | Reimplementation of the Mortyr 2093-1944 game engine | 1 | 🟢 | GLSL |
| [Quake4Doom](https://github.com/Kasreyn/Quake4Doom) | Engine reimplementation of Quake 4; uses original game data (C++) | 1 | 🟡 | C++ |
| [Soul Reaverse](https://github.com/Mc-muffin/kain2-splatdisasm) | Engine reimplementation of Legacy of Kain: Soul Reaver; uses original game data (C) | 1 | 🟡 | C |
| [StawdewValley](https://github.com/E-riCA0/StawdewValley) | Decompiled Stardew Valley source code | 1 | 🔴 | C# |
| [1oom](https://gitlab.com/KilgoreTroutMaskReplicant/1oom) | Engine reimplementation of Master of Orion; uses original game data (C) |  | ⚪ |  |
| [2ooM](https://sourceforge.net/projects/toom/) | Engine reimplementation of Master of Orion 2; uses original game data (C++, C) |  | ⚪ |  |
| [AGE](https://github.com/weimingtom/air-galgame-engine) | Automatically exported from code.google.com/p/air-galgame-engine | 0 | 🔴 | ActionScript |
| [Blake4SDL](https://bitbucket.org/ks-presto/blake4sdl) | Engine reimplementation of Blake Stone: Planet Strike, Blake Stone: Aliens of Gold; uses original game data (C) |  | ⚪ |  |
| [BloodGDX](https://gitlab.com/m210/BloodGDX) | Engine reimplementation of Blood; uses original game data (Java) |  | ⚪ |  |
| [Commander Genius](https://gitlab.com/Dringgstein/Commander-Genius) | Engine reimplementation of Commander Keen 1-6 and Cosmo's Cosmic Adventure |  | ⚪ |  |
| [dantelion](https://gitlab.com/somobu/dantelion) | Work-in-progress reimplementation of the FromSoftware Dark Souls engine |  | ⚪ |  |
| [djavul](https://github.com/Happy-Ferret/djavul) | An open source reference re-implementation of the Diablo 1 game engine (work in progress). | 0 | 🔴 | Go |
| [DMOE](https://sourceforge.net/projects/dmle/) | Engine reimplementation of Dungeon Master; uses original game data (C) |  | ⚪ |  |
| [Dragonball Z 3: Killer Androids ASM Source Code](https://www.romhacking.net/documents/312/) | Engine reimplementation of Dragon Ball Z III: Ressen Jinzō Ningen; uses original game data (Assembly) |  | ⚪ |  |
| [Dragonball Z Gaiden: Plan to Eliminate the Saiyans Source Code](https://www.romhacking.net/documents/319/) | Engine reimplementation of Dragon Ball Z Side Story: Plan to Eradicate the Saiyans; uses original game data |  | ⚪ |  |
| [Dragonball Z: Assault of the Saiyans Source Code](https://www.romhacking.net/documents/313/) | Engine reimplementation of Dragon Ball Z: Kyōshū! Saiyajin; uses original game data (Assembly) |  | ⚪ |  |
| [eggnogg-](https://codeberg.org/yx/eggnogg-) | FOSS reimplementation of the game EGGNOGG+ |  | ⚪ |  |
| [f3bfg](https://gitlab.com/the-big-mt/f3bfg) | Fallout 3 and Fallout: New Vegas game code reimplementation |  | ⚪ |  |
| [FreeCS](https://sourceforge.net/projects/freecs-1-5/) | Free-software re-implementation of Counter-Strike 1.5 running on the FTEQW engine. |  | ⚪ |  |
| [FreeSCI](https://sourceforge.net/projects/freesci/) | Reimplementation of the Sierra SCI adventure game interpreter |  | ⚪ |  |
| [FreeSynd](https://sourceforge.net/projects/freesynd/) | Engine reimplementation of Syndicate; uses original game data (C++) |  | ⚪ |  |
| [Frotz](https://gitlab.com/DavidGriffith/frotz) | Interpreter for Infocom's Z-machine story files |  | ⚪ |  |
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
| [open-badday](https://codeberg.org/idans320/open-badday) | Reverse engineering The Residents' 1995 PC game Bad Day on the Midway |  | ⚪ |  |
| [opene2140](https://gitlab.com/opene2140/opene2140) | Engine reimplementation of Earth 2140; uses original game data (C++) |  | ⚪ |  |
| [openguimo](https://gitlab.com/greyxor/openguimo) | Open-source reimplementation of the 1997 DOS platformer Guimo in Godot |  | ⚪ |  |
| [OpenLRR](https://github.com/vs49688/OpenLRR) | An open source re-implementation of LEGO Rock Raiders | 0 | 🟢 | C++ |
| [OpenRW](https://openrw.org/) | A cross-platform, open source re-implementation of Rockstar Games' Grand Theft Auto III. |  | ⚪ |  |
| [Ordoor](https://code.ur.gs/lupine/ordoor) | Engine reimplementation of Warhammer 40,000: Chaos Gate; uses original game data (Go) |  | ⚪ |  |
| [Pentagram](https://sourceforge.net/projects/pentagram/) | Engine reimplementation for Ultima VIII: Pagan |  | ⚪ |  |
| [Phavon](https://sourceforge.net/projects/phavon/) | Engine reimplementation of Xenon 2 Megablast; uses original game data (C) |  | ⚪ |  |
| [pizzalegacy](https://codeberg.org/cowomaly/pizzalegacy) | Open-source reimplementation of Pizza Connection / Pizza Tycoon (1994); needs original DOS assets |  | ⚪ |  |
| [PowerslaveGDX](https://gitlab.com/m210/PowerslaveGDX) | Engine reimplementation of Powerslave; uses original game data (Java) |  | ⚪ |  |
| [Project Aedra](https://sourceforge.net/projects/aedra/) | Engine reimplementation of The Elder Scrolls III: Morrowind; uses original game data (C++, C) |  | ⚪ |  |
| [pyDM](https://codeberg.org/CyCl0ne/pyDM) | Faithful Python reimplementation of Dungeon Master (Amiga, 1989) |  | ⚪ |  |
| [RedneckGDX](https://gitlab.com/m210/RedneckGDX) | Engine reimplementation of Redneck Rampage; uses original game data (Java) |  | ⚪ |  |
| [RVGL](https://rvgl.org/) | Cross-platform engine for Re-Volt. |  | ⚪ |  |
| [Sarien](https://sourceforge.net/projects/sarien/) | Reimplementation of the Sierra AGI adventure game interpreter |  | ⚪ |  |
| [Scheddy Kong Racing](https://gitlab.com/ryandwyer/scheddy-kong-racing) | Engine reimplementation of Diddy Kong Racing; uses original game data (Assembly, C) |  | ⚪ |  |
| [SITDRE](https://github.com/ShiningForceCentral/SITDRE) | Collaborative work on reverse-engineering Shining in the Darkness. | 0 | 🟡 | C |
| [sm64synth](https://gitlab.com/DeKrain/sm64synth) | Port/reimplementation of the Super Mario 64 audio engine |  | ⚪ |  |
| [soniccdrespinned](https://git.sr.ht/~benoitren/soniccdrespinned) | Engine reimplementation of Sonic CD; uses original game data (C) |  | ⚪ |  |
| [Super Mario 68K](http://tifreakware.net/lachprog/dold.htm) | Engine reimplementation of Super Mario Bros.; uses original game data (C) |  | ⚪ |  |
| [Super-Mario-Bros-Java](https://sourceforge.net/projects/super-mario-bros-java/) | Engine reimplementation of Super Mario Bros.; uses original game data (Java) |  | ⚪ |  |
| [supercopter_decompiled](https://github.com/ergonomy-joe/supercopter_decompiled) | Engine reimplementation of Supercopter; uses original game data (Pascal) | 0 | 🟡 | Pascal |
| [SuperLemmini](https://www.lemmingsforums.net/index.php?topic=1793.0) | Engine reimplementation of Lemmings; uses original game data (Java) |  | ⚪ |  |
| [The Crystal Scrolls](https://sourceforge.net/projects/crystalscrolls/) | Engine reimplementation of The Elder Scrolls III: Morrowind; uses original game data (C++) |  | ⚪ |  |
| [The System Shock Hack Project](https://sourceforge.net/projects/tsshp/) | Engine reimplementation of System Shock, Ultima Underworld; uses original game data (C++) |  | ⚪ |  |
| [Thunder Force IV Rebirth](https://github.com/Fissuras/tf4r) | Automatically exported from code.google.com/p/tf4r | 0 | 🔴 | ASP |
| [Transfusion](https://sourceforge.net/projects/blood/) | Engine reimplementation of Blood; uses original game data (QuakeC, C) |  | ⚪ |  |
| [twisted-metal](https://gitlab.com/goblindo/twisted-metal) | Native Rust reimplementation of Twisted Metal (2012, PS3); bring your own game |  | ⚪ |  |
| [viceroy](https://codeberg.org/ebbex/viceroy) | Reverse engineering project for Sid Meier's Colonization |  | ⚪ |  |
| [Wages of War](https://github.com/suhteevah/wages-of-war) | A clean-room, open-source Rust reverse enginering of the Wages of War: The Business of Battle (1996) engine. | 0 | 🟢 | Rust |
| [WayneGretzky3dHockey](https://github.com/Rainchus/WayneGretzky3dHockey) | Decomp of wayne gretzky hockey for the n64 | 0 | 🔴 | C |
| [WebFun](https://codeberg.org/cyco/WebFun) | Reimplementation of the engine behind Indiana Jones' Desktop Adventures and Yoda Stories |  | ⚪ |  |
| [Wing Commander 1 Reloaded](https://wingcomreloaded.itch.io/wingcommander1reloaded) | Modern recreation of Wing Commander I. |  | ⚪ |  |
| [Winter Jumper](https://os4depot.net/?function=showfile&file=game/platform/winterjumper.lha) | Engine reimplementation of The Great Giana Sisters; uses original game data (C++) |  | ⚪ |  |
| [xu4](https://sourceforge.net/projects/xu4/) | Remake of the Ultima IV engine that runs on modern systems with the original data |  | ⚪ |  |

## Fan Patches & Enhancements

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [project-restoration](https://github.com/leoetlino/project-restoration) | Majora's Mask 3D patch restoring original mechanics via reverse engineering | 808 | 🔴 | C++ |
| [Silent Hill 2 Enhanced Edition](https://github.com/elishacloud/Silent-Hill-2-Enhancements) | A project designed to enhance Silent Hill 2 (SH2) graphics and audio for the PC. It also includes scripts to build or... | 715 | 🟢 | C |
| [Plants-vs.-Zombies-Online-Battle](https://github.com/Zhuagenborn/Plants-vs.-Zombies-Online-Battle) | Two-player online battle mode for Plants vs. Zombies built via reverse engineering and DLL injection | 626 | 🟡 | C++ |
| [HaloCEVR](https://github.com/LivingFray/HaloCEVR) | VR conversion of the original PC Halo: Combat Evolved | 444 | 🟢 | C++ |
| [UnofficialCrusaderPatch2](https://github.com/UnofficialCrusaderPatch/UnofficialCrusaderPatch2) | Unofficial balancing and bugfix patch installer for Stronghold Crusader | 433 | 🟡 | C# |
| [Wind Waker Randomizer](https://github.com/LagoLunatic/wwrando) | Wind Waker Randomizer | 427 | 🟢 | Python |
| [mgs2sos](https://github.com/oct0xor/mgs2sos) | Mod adding third-person camera and controls to MGS2: Substance | 310 | 🔴 | C++ |
| [PAL3patch](https://github.com/zhangboyang/PAL3patch) | Resolution patch for Chinese Paladin 3 | 250 | 🟡 | C |
| [sc2kfix](https://github.com/sc2kfix/sc2kfix) | Bugfix and modding plugin for SimCity 2000 Special Edition | 217 | 🟢 | C++ |
| [popcap-patches](https://github.com/cheez3d/popcap-patches) | Patched executables and research notes for PopCap games | 195 | 🔴 |  |
| [gb-save-states](https://github.com/mattcurrie/gb-save-states) | Patches that add save-state support to Game Boy games on original hardware | 193 | 🟡 | Assembly |
| [Ultima IV Remastered](https://github.com/MagerValp/u4remastered) | Ultima IV Remastered for the C64 | 123 | 🔴 | Assembly |
| [magicka-patch](https://github.com/Alexander-Aue-Johr/magicka-patch) | Reverse engineered fixes and optimisations for Magicka | 87 | 🟢 | C# |
| [tekken3-expanded](https://github.com/omarma/tekken3-expanded) | Adds Tekken Tag Tournament characters to Tekken 3 | 87 | 🟢 | C++ |
| [nge_2_re](https://github.com/rezual/nge_2_re) | Neon Genesis Evangelion 2 reverse engineering and translation | 78 | 🟢 | Python |
| [sf4e](https://github.com/fabeloper/sf4e) | Rollback netcode mod for Ultra Street Fighter IV (Steam) | 63 | 🟢 | C++ |
| [v-on-patcher](https://github.com/pairomaniac/v-on-patcher) | Patcher for Cyber Troopers Virtual-On (PC, 1997) with modern hardware and online support | 62 | 🟢 | Python |
| [Lotus STE](https://github.com/jonathanopalise/lotus-ste) | Enhancements to the Atari ST version of Lotus Esprit Turbo Challenge to support STE hardware features | 42 | 🔴 | Assembly |
| [NewerSMBDS](https://github.com/Newer-Team/NewerSMBDS) | Newer Super Mario Bros. DS, a total-conversion mod built on reverse-engineered NSMB code | 39 | 🟢 | C |
| [Ultima V Remastered](https://github.com/Drunella/u5remastered) | Ultima V remastered for EasyFlash and 1581 | 32 | 🟡 | Assembly |
| [Beasts and Bumpkins Fan Patch](https://github.com/bb-patch/bb-patch) | Tool for Beasts and Bumpkins game data (osgameclones) (Go) | 29 | 🔴 | Go |
| [TTDPatch](https://github.com/ttdpatch/ttdpatch) | The master TTDPatch repository | 11 | 🔴 | Assembly |

## Game Network Protocols & APIs

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [mineflayer](https://github.com/PrismarineJS/mineflayer) | High-level JavaScript API for creating Minecraft bots | 7,597 | 🟢 | JavaScript |
| [Geyser](https://github.com/GeyserMC/Geyser) | Proxy translating Minecraft Bedrock clients to Java Edition servers | 5,923 | 🟢 | Java |
| [Hearthstone Deck Tracker](https://github.com/HearthSim/Hearthstone-Deck-Tracker) | Deck tracker for Hearthstone on Windows that reads game logs and memory | 4,922 | 🟢 | C# |
| [Greenlight](https://github.com/unknownskl/greenlight) | Open-source client for Xbox Cloud Gaming (xCloud) and Xbox home streaming | 2,896 | 🟢 | TypeScript |
| [Velocity](https://github.com/PaperMC/Velocity) | High-performance Minecraft Java proxy server | 2,275 | 🟢 | Java |
| [Minecraft Console Client](https://github.com/MCCTeam/Minecraft-Console-Client) | Lightweight console Minecraft client for chat and automated scripts | 2,164 | 🟢 | C# |
| [Deceive](https://github.com/molenzwiebel/Deceive) | XMPP proxy that lets you appear offline in League of Legends, VALORANT and LoR | 1,732 | 🟢 | C# |
| [ViaVersion](https://github.com/ViaVersion/ViaVersion) | Lets newer Minecraft clients connect to older server versions by translating packets | 1,642 | 🟢 | Java |
| [OpenKore](https://github.com/OpenKore/openkore) | Open-source custom client and automation tool for Ragnarok Online | 1,532 | 🟢 | Perl |
| [node-minecraft-protocol](https://github.com/PrismarineJS/node-minecraft-protocol) | Parse and serialize Minecraft Java packets, with auth and encryption | 1,421 | 🟢 | JavaScript |
| [HSTracker](https://github.com/HearthSim/HSTracker) | Hearthstone deck tracker for macOS | 1,258 | 🟢 | Swift |
| [PokeGOAPI-Java](https://github.com/Grover-c13/PokeGOAPI-Java) | Pokemon Go API | 1,046 | 🔴 | Java |
| [node-steam](https://github.com/seishun/node-steam) | Interface directly with Steam CM servers from Node.js (archived) | 999 | 🗄️ | JavaScript |
| [go-mc](https://github.com/Tnze/go-mc) | Collection of Go libraries for the Minecraft Java protocol and data formats | 982 | 🟡 | Go |
| [GameTracking-CS2](https://github.com/SteamTracking/GameTracking-CS2) | Automated tracking of Counter-Strike 2 game file, string and protobuf changes | 971 | 🟢 | Slang |
| [minecraft-data](https://github.com/PrismarineJS/minecraft-data) | Language-independent Minecraft protocol and game data for clients, servers and libraries | 956 | 🟢 | JavaScript |
| [MCProtocolLib](https://github.com/GeyserMC/MCProtocolLib) | Java library for Minecraft Java client/server protocol communication | 909 | 🟢 | Java |
| [pyCraft](https://github.com/ammaraskar/pyCraft) | Minecraft Java client networking library in Python | 846 | 🟡 | Python |
| [pgoapi](https://github.com/pogodevorg/pgoapi) | Unofficial Pokemon GO API in Python (archived) | 842 | 🗄️ | Python |
| [NintendoClients](https://github.com/kinnay/NintendoClients) | Python package to communicate with Switch, Wii U and 3DS servers | 765 | 🟢 | Python |
| [steampy](https://github.com/bukson/steampy) | Python Steam trading library using Steam's internal web endpoints | 667 | 🟡 | Python |
| [ViaProxy](https://github.com/ViaVersion/ViaProxy) | Standalone proxy translating between Minecraft protocol versions, including Bedrock and classic | 661 | 🟢 | Java |
| [NintendoSwitchRESTAPI](https://github.com/ZekeSnider/NintendoSwitchRESTAPI) | Reverse engineered REST API of the Nintendo Switch iOS app | 658 | 🔴 |  |
| [nxapi](https://github.com/samuelthomas2774/nxapi) | Nintendo Switch Online/Parental Controls app APIs. Show your Nintendo Switch presence in Discord, get friend... | 629 | 🟢 | TypeScript |
| [steam-tradeoffer-manager](https://github.com/DoctorMcKay/node-steam-tradeoffer-manager) | Node.js Steam trade offer management library | 606 | 🟢 | JavaScript |
| [valorant-api-docs](https://github.com/techchrism/valorant-api-docs) | Documentation for internal VALORANT client API endpoints | 594 | 🟡 | TypeScript |
| [SteamTracking Protobufs](https://github.com/SteamTracking/Protobufs) | Auto-tracked protobuf definitions extracted from Steam, CS2, Dota 2, Deadlock and TF2 | 585 | 🟢 | Shell |
| [node-steamcommunity](https://github.com/DoctorMcKay/node-steamcommunity) | Node.js module to interact with Steam Community web interfaces | 579 | 🟢 | JavaScript |
| [gophertunnel](https://github.com/Sandertv/gophertunnel) | Go library for Minecraft Bedrock Edition networking, clients and proxies | 576 | 🟢 | Go |
| [unofficial-valorant-api](https://github.com/Henrik-3/unofficial-valorant-api) | Unofficial VALORANT API built on the in-game API endpoints | 559 | 🟢 | JavaScript |
| [bedrock-protocol](https://github.com/PrismarineJS/bedrock-protocol) | Minecraft Bedrock protocol library with authentication and encryption | 485 | 🟢 | JavaScript |
| [Fortnite Endpoints Documentation](https://github.com/LeleDerGrasshalmi/FortniteEndpointsDocumentation) | Unofficial documentation of Fortnite and Epic Games API endpoints | 483 | 🟢 |  |
| [s3s](https://github.com/frozenpandaman/s3s) | Successor to splatnet2statink. Takes battle data from the SplatNet 3 app and uploads it to stat.ink! | 464 | 🟡 | Python |
| [go-steam](https://github.com/Philipp15b/go-steam) | Steam's network protocol implemented in Go for automation without a Steam client | 434 | 🟡 | Go |
| [psn-api](https://github.com/achievements-app/psn-api) | JavaScript library to get trophy, user and game data from the PlayStation Network | 428 | 🟢 | TypeScript |
| [EpicResearch](https://github.com/MixV2/EpicResearch) | Research and documentation of Epic Games' undocumented APIs | 425 | 🟡 |  |
| [Cloudburst Protocol](https://github.com/CloudburstMC/Protocol) | Java protocol library for Minecraft Bedrock Edition | 419 | 🟢 | Java |
| [prismarine-viewer](https://github.com/PrismarineJS/prismarine-viewer) | Web-based 3D viewer for Minecraft servers and bots | 398 | 🟢 | JavaScript |
| [NSO-RPC](https://github.com/MCMi460/NSO-RPC) | Shows Nintendo Switch playing status in Discord using the Nintendo Switch Online app API | 384 | 🟡 | Python |
| [psn-php](https://github.com/Tustin/psn-php) | PHP wrapper for the PlayStation Network API | 374 | 🟢 | PHP |
| [node-globaloffensive](https://github.com/DoctorMcKay/node-globaloffensive) | Node.js client for the CS2 game coordinator protocol | 368 | 🟢 | JavaScript |
| [gumer-psn](https://github.com/jhewt/gumer-psn) | PlayStation Network API written in Node.js | 348 | 🗄️ | JavaScript |
| [splatnet2statink](https://github.com/frozenpandaman/splatnet2statink) | Fetches Splatoon 2 battle data from the SplatNet 2 app API and uploads to stat.ink | 344 | 🟡 | Python |
| [rustplus.js](https://github.com/liamcottle/rustplus.js) | Unofficial Node.js library for the Rust+ companion protocol | 322 | 🟢 | JavaScript |
| [GameTracking](https://github.com/SteamTracking/GameTracking) | Automated dumps of Valve game files and protos to track changes | 307 | 🟢 | Shell |
| [RiiConnect24 Patcher](https://github.com/KcrPL/RiiConnect24-Patcher) | Patches Wii channels to use RiiConnect24's revived WiiConnect24 services | 306 | 🟢 | Batchfile |
| [api](https://github.com/helldivers-2/api) | Community API for Helldivers 2 game data | 298 | 🟢 | C# |
| [python-hearthstone](https://github.com/HearthSim/python-hearthstone) | Hearthstone Python library: card defs, DBF, enums and log parser | 277 | 🟢 | Python |
| [steam-totp](https://github.com/DoctorMcKay/node-steam-totp) | Node.js generator for Steam Guard mobile TOTP codes and confirmation keys | 257 | 🔴 | JavaScript |
| [steam.py](https://github.com/Gobot1234/steam.py) | Async Python wrapper for the Steam API and Steam CM protocol | 239 | 🟢 | Python |
| [Inkay](https://github.com/PretendoNetwork/Inkay) | Wii U Aroma plugin that patches the console to use Pretendo Network servers | 233 | 🟢 | C++ |
| [rustplus-desktop](https://github.com/Pronwan/rustplus-desktop) | Unofficial Rust+ desktop app | 215 | 🟢 | C# |
| [xbox-webapi-python](https://github.com/OpenXbox/xbox-webapi-python) | A python library to authenticate with Xbox Live via your Microsoft Account and provides Xbox related Web-API. | 209 | 🟢 | Python |
| [steam-session](https://github.com/DoctorMcKay/node-steam-session) | Node.js module implementing Steam's auth server login to obtain refresh and web tokens | 199 | 🟢 | TypeScript |
| [psnawp](https://github.com/isFakeAccount/psnawp) | [Mirror] PlayStation Network API Python | 196 | 🟢 | Python |
| [go-dota2](https://github.com/paralin/go-dota2) | Go client for the Dota 2 game coordinator protocol | 183 | 🟢 | Go |
| [BedrockProtocol](https://github.com/pmmp/BedrockProtocol) | PHP implementation of the Minecraft Bedrock network protocol | 177 | 🗄️ | PHP |
| [slippi-js](https://github.com/project-slippi/slippi-js) | JavaScript parser for Super Smash Bros. Melee Slippi replay files | 168 | 🟢 | TypeScript |
| [GOG DB](https://github.com/Yepoleb/gogdb) | Website and scraper collecting GOG game data from GOG's internal APIs | 163 | 🟢 | Python |
| [LCU and Riot Client API docs](https://github.com/KebsCS/lcu-and-riotclient-api) | Documentation of League of Legends LCU and Riot Client local API endpoints | 160 | 🟢 | HTML |
| [psn-api (Python)](https://github.com/mgp25/psn-api) | PlayStation Network API client in Python | 134 | 🗄️ | Python |
| [squid-tracks](https://github.com/hymm/squid-tracks) | Unofficial desktop client for Nintendo SplatNet 2 | 134 | 🔴 | JavaScript |
| [csgo (python)](https://github.com/ValvePython/csgo) | Python module to interact with the CS:GO game coordinator | 133 | 🔴 | Python |
| [SteamWebPipes](https://github.com/xPaw/SteamWebPipes) | Pipes Steam PICS changelist events to websockets using SteamKit | 133 | 🗄️ | C# |
| [lcu-driver](https://github.com/sousa-andre/lcu-driver) | Python interface for the League of Legends client local API | 123 | 🟡 | Python |
| [SAMP-Mobile](https://github.com/kuzia15/SAMP-Mobile) | Open-source SA:MP mobile multiplayer client | 122 | 🟢 |  |
| [green-vita](https://github.com/Day-OS/green-vita) | Xbox Cloud Gaming client for PlayStation Vita | 118 | 🟢 | Rust |
| [lcu-connector](https://github.com/Pupix/lcu-connector) | Node.js connector for the League of Legends client (LCU) local API | 116 | 🟢 | JavaScript |
| [ShinraMeter](https://github.com/neowutran/ShinraMeter) | TERA DPS meter based on decoded game packets | 115 | 🟡 | C# |
| [xboxlive-auth](https://github.com/XboxReplay/xboxlive-auth) | Xbox Live authentication library for Node.js | 115 | 🟢 | TypeScript |
| [valorant.js](https://github.com/liamcottle/valorant.js) | Unofficial Node.js library for the VALORANT client API | 111 | 🟡 | JavaScript |
| [xbox-smartglass-nano-python](https://github.com/OpenXbox/xbox-smartglass-nano-python) | Python implementation of the Xbox One NANO game-streaming protocol | 104 | 🗄️ | Python |
| [nex-go](https://github.com/PretendoNetwork/nex-go) | Go implementation of Nintendo's PRUDP/NEX game server protocol for Pretendo | 102 | 🟢 | Go |
| [openspy-client](https://github.com/anzz1/openspy-client) | Patch for old PC games replacing defunct GameSpy services with OpenSpy | 98 | 🟢 | C |
| [axie-graphql-documentation](https://github.com/ShaneMaglangit/axie-graphql-documentation) | Unofficial documentation of Axie Infinity's GraphQL endpoint | 97 | 🗄️ | JavaScript |
| [Agar.io-Reverse-Engineering](https://github.com/DnAp/Agar.io-Reverse-Engineering) | Agar.io protocol reverse engineering | 96 | 🗄️ | JavaScript |
| [PictoChat](https://github.com/Thesola10/PictoChat) | PictoChat protocol adapter implementing the Nintendo DS PictoChat wireless protocol | 91 | 🗄️ | C |
| [python-screeps](https://github.com/screepers/python-screeps) | Python client for the unofficial Screeps API | 91 | 🟢 | Python |
| [python-aternos](https://github.com/DarkCat09/python-aternos) | Unofficial Aternos API in Python | 89 | 🗄️ | Python |
| [MariOver](https://github.com/TheGreatRambler/MariOver) | Makes almost all of the data exposed by Mario Maker 2 servers public through an API | 88 | 🟢 | Python |
| [runescape-api](https://github.com/Astrect/runescape-api) | Node.js library for RuneScape and Old School unofficial API endpoints | 86 | 🟢 | TypeScript |
| [tentacli](https://github.com/tench-rt/tentacli) | Tentacli is a framework for building extensible network protocol clients via modular plugins | 83 | 🟢 | Rust |
| [agario-client](https://github.com/pulviscriptor/agario-client) | Node.js agar.io client implementation | 82 | 🔴 | JavaScript |
| [HearthDb](https://github.com/HearthSim/HearthDb) | .NET Hearthstone card database extracted from game data | 80 | 🟢 | C# |
| [hass-psn](https://github.com/JackJPowell/hass-psn) | Home Assistant integration for the PlayStation Network via its unofficial API | 79 | 🟢 | Python |
| [Kasumi](https://github.com/p0mpurin/Kasumi) | Unofficial native GeForce NOW and Xbox Cloud Gaming client for the New Nintendo 3DS | 78 | 🟢 | C |
| [prismarine-auth](https://github.com/PrismarineJS/prismarine-auth) | Microsoft/Xbox Live authentication flow for Minecraft clients | 77 | 🟢 | JavaScript |
| [xbox-smartglass-core-python](https://github.com/OpenXbox/xbox-smartglass-core-python) | Python implementation of the Xbox One SmartGlass core protocol | 75 | 🗄️ | Python |
| [FFXIVOpcodeWizard](https://github.com/karashiiro/FFXIVOpcodeWizard) | Automated Final Fantasy XIV network opcode discovery | 68 | 🔴 | C# |
| [MoeXCOM](https://github.com/hdk5/MoeXCOM) | Reverse engineering Blue Archive | 67 | 🔴 | C# |
| [Haruki-Sekai-API](https://github.com/Team-Haruki/Haruki-Sekai-API) | Unofficial API proxy for Project Sekai game data | 64 | 🟢 | Rust |
| [node-epicgames-fortnite-client](https://github.com/SzymonLisowiec/node-epicgames-fortnite-client) | Unofficial Fortnite client in JavaScript built on the Epic Games launcher protocol | 64 | 🔴 | JavaScript |
| [node-haxball](https://github.com/wxyz-abcd/node-haxball) | API to build Haxball clients and bots via its reversed protocol | 63 | 🟢 | JavaScript |
| [rlapi](https://github.com/dank/rlapi) | Reverse engineered Rocket League internal HTTP and WebSocket API | 59 | 🟢 | Go |
| [pyremoteplay](https://github.com/ktnrg45/pyremoteplay) | Python library implementing the PlayStation Remote Play protocol | 56 | 🗄️ | Python |
| [diveharder_api.py](https://github.com/helldivers-2/diveharder_api.py) | FastAPI proxy exposing Helldivers 2 API data for community developers | 55 | 🟡 | Python |
| [XiPackets](https://github.com/atom0s/XiPackets) | Reverse engineered packet documentation for Final Fantasy XI | 55 | 🟢 |  |
| [fut-api](https://github.com/lorenzh/fut-api) | Unofficial FIFA Ultimate Team API client | 54 | 🗄️ | JavaScript |
| [wot-api-description](https://github.com/thunder-spb/wot-api-description) | World of Tanks unofficial API description | 45 | 🗄️ | PHP |
| [openfoxwq_client](https://github.com/openfoxwq/openfoxwq_client) | Multiplatform unofficial client for the Fox Go server | 44 | 🗄️ | Dart |
| [xboxlive-api](https://github.com/XboxReplay/xboxlive-api) | Simple Xbox Live API wrapper for Node.js | 44 | 🔴 | TypeScript |
| [trackmania2020apidocumentation](https://github.com/The-Firexx/trackmania2020apidocumentation) | Trackmania 2020 unofficial API documentation | 43 | 🗄️ |  |
| [Useful-ValorantAPI-Info](https://github.com/Soneliem/Useful-ValorantAPI-Info) | Resources and code for Valorant's unofficial API | 40 | 🔴 | Python |
| [BNETDocs](https://github.com/BNETDocs/bnetdocs-web) | Documentation website for Blizzard's Battle.net classic protocols | 36 | 🟢 | JavaScript |
| [psn100](https://github.com/Ragowit/psn100) | PlayStation trophy tracking site with leaderboards built on the PSN API | 28 | 🟢 | PHP |
| [Steam-Client-Docs](https://github.com/Bluscream/Steam-Client-Docs) | Unofficial documentation of the Steam client | 28 | 🟡 |  |
| [fc27-clubs-api](https://github.com/1erkandogan/fc27-clubs-api) | Unofficial Python client for the EA Sports FC 27 Pro Clubs API | 23 | 🟢 | Python |
| [market-pricing](https://github.com/node-steam/market-pricing) | Wrapper for the unofficial Steam Market pricing API | 22 | 🔴 | TypeScript |
| [pyps4-2ndscreen](https://github.com/ktnrg45/pyps4-2ndscreen) | Python library to control a PS4 via the PS4 Second Screen protocol | 20 | 🗄️ | Python |
| [OpenSpartan Workshop](https://github.com/OpenSpartan/openspartan-workshop) | Desktop app to track Halo Infinite stats and progression via the unofficial Halo API | 19 | 🟢 | C# |
| [krunker.io](https://github.com/fasetto/krunker.io) | Unofficial API for the krunker.io game social page | 13 | 🔴 | JavaScript |
| [node-mojang](https://github.com/astra137/node-mojang) | Unofficial Node.js library for Mojang's HTTP APIs (auth, profiles, skins) | 12 | 🔴 | JavaScript |
| [growtopia-api](https://github.com/H-pun/growtopia-api) | Unofficial Growtopia API for item data and sprites | 7 | 🟡 | Python |
| [Durango](https://github.com/AlexArchive/Durango) | Unofficial read-only API client for Xbox LIVE | 6 | 🔴 | C# |
| [ffxiv](https://github.com/ffxiv/ffxiv) | Unofficial Final Fantasy XIV toolkit for Ruby with a Lodestone scraper | 4 | 🔴 | Ruby |
| [valorant-xmpp-watcher](https://github.com/techchrism/valorant-xmpp-watcher) | Connects to and logs VALORANT XMPP presence and roster events | 4 | 🟡 | TypeScript |
| [halo_api](https://github.com/nuzzles/halo_api) | Unofficial Halo Infinite REST API client for Rust: service record and match history | 3 | 🟢 | Rust |
| [Grunt](https://github.com/dend/grunt) | Unofficial API wrapper and documentation for the Halo Infinite web services | 0 | 🟢 | C# |

## Launchers & Store Clients

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Playnite](https://github.com/JosefNemec/Playnite) | Open-source game library manager integrating Steam, Epic, GOG, EA, Ubisoft and more store libraries | 14,239 | 🟢 | C# |
| [ArchiSteamFarm](https://github.com/JustArchiNET/ArchiSteamFarm) | C# Steam client application built on SteamKit2 for multi-account card farming and automation | 13,757 | 🟢 | C# |
| [Heroic Games Launcher](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher) | Open-source launcher for Epic, GOG and Amazon Games libraries on Linux, Windows and macOS | 12,450 | 🟢 | TypeScript |
| [Prism Launcher](https://github.com/PrismLauncher/PrismLauncher) | Open-source Minecraft launcher managing multiple instances and Microsoft account login | 10,685 | 🟢 | C++ |
| [HMCL](https://github.com/HMCL-dev/HMCL) | Hello Minecraft! Launcher, a cross-platform third-party Minecraft launcher | 10,258 | 🟢 | Java |
| [Decky Loader](https://github.com/SteamDeckHomebrew/decky-loader) | Plugin loader for the Steam Deck that injects into the Steam client UI | 7,386 | 🟢 | TypeScript |
| [Legendary](https://github.com/legendary-gl/legendary) | Open-source CLI replacement for the Epic Games Launcher built on Epic's undocumented APIs | 5,332 | 🟢 | Python |
| [MultiMC](https://github.com/MultiMC/Launcher) | Custom Minecraft launcher for managing multiple isolated installations | 4,674 | 🟢 | C++ |
| [Millennium](https://github.com/SteamClientHomebrew/Millennium) | Framework for Steam client themes and plugins via injection into the CEF UI | 4,472 | 🟢 | C++ |
| [Steam Desktop Authenticator](https://github.com/Jessecar96/SteamDesktopAuthenticator) | Desktop implementation of Steam's mobile authenticator (Steam Guard) app | 3,828 | 🟡 | C# |
| [DepotDownloader](https://github.com/SteamRE/DepotDownloader) | Steam depot downloader built on the SteamKit2 reverse-engineered Steam protocol library | 3,466 | 🟢 | C# |
| [XIVLauncher](https://github.com/goatcorp/FFXIVQuickLauncher) | Custom third-party launcher for Final Fantasy XIV that reimplements the login flow | 3,193 | 🟢 | C# |
| [Bloxstrap](https://github.com/bloxstraplabs/bloxstrap) | Alternative bootstrapper for the Roblox client with extra configuration | 3,174 | 🟢 | C# |
| [chiaki-ng](https://github.com/chiaki-ng/chiaki-ng) | Open-source PlayStation 4/5 Remote Play client, successor of Chiaki | 2,852 | 🟢 | C |
| [GameHub](https://github.com/tkashkin/GameHub) | Unified game library for Steam, GOG and Humble Bundle (archived) | 2,849 | 🗄️ | Vala |
| [BoilR](https://github.com/PhilipK/BoilR) | Syncs games from Epic, GOG, Origin, Amazon and other launchers into the Steam library | 1,911 | 🟢 | Rust |
| [Pluvia](https://github.com/oxters168/Pluvia) | Lightweight unofficial Steam client for Android | 1,727 | 🟢 | C |
| [mcpelauncher](https://github.com/minecraft-linux/mcpelauncher-manifest) | Runs the Android build of Minecraft Bedrock natively on Linux and macOS | 1,692 | 🟢 | CMake |
| [Minigalaxy](https://github.com/sharkwouter/minigalaxy) | Simple unofficial GOG client for Linux | 1,333 | 🟢 | Python |
| [steamguard-cli](https://github.com/dyc3/steamguard-cli) | Linux CLI for Steam Guard 2FA codes and trade/market confirmations | 1,066 | 🟢 | Rust |
| [MC Bedrock Version Launcher](https://github.com/MCMrARM/mc-w10-version-launcher) | Installs and switches between multiple Minecraft Bedrock (Windows 10) versions | 1,061 | 🟢 | C++ |
| [steam-tui](https://github.com/dmadisetti/steam-tui) | Rust TUI Steam client driving steamcmd | 1,039 | 🟢 | Rust |
| [Rare](https://github.com/RareDevs/Rare) | Qt GUI alternative to the Epic Games Launcher, built on Legendary | 939 | 🟢 | Python |
| [LGOGDownloader](https://github.com/Sude-/lgogdownloader) | Unofficial GOG.com downloader for Linux using the same API as GOG Galaxy | 919 | 🟢 | C++ |
| [Vinegar](https://github.com/vinegarhq/vinegar) | Open-source launcher/manager for running Roblox Studio on Linux | 792 | 🟢 | Go |
| [humblebundle-downloader](https://github.com/xtream1101/humblebundle-downloader) | Downloads a Humble Bundle library via Humble's internal API | 610 | 🗄️ | Python |
| [gogrepo](https://github.com/eddie3/gogrepo) | Python tool to download a full GOG.com game and bonus collection for offline use | 544 | 🔴 | Python |
| [SBRW GameLauncher](https://github.com/SoapboxRaceWorld/GameLauncher_NFSW) | Unofficial launcher for Need for Speed: World community servers | 534 | 🟡 | C# |
| [steamctl](https://github.com/ValvePython/steamctl) | Command-line tool to control Steam: download depots, workshop items, manage apps and accounts | 377 | 🟡 | Python |
| [comet](https://github.com/imLinguin/comet) | Open source implementation of the GOG Galaxy communication service | 371 | 🟢 | Rust |
| [nile](https://github.com/imLinguin/nile) | Unofficial Amazon Games client (CLI) reimplementing the Amazon Games app's protocol | 361 | 🟢 | Python |
| [CnCNet Client](https://github.com/CnCNet/xna-cncnet-client) | Online multiplayer client for classic Command & Conquer games on the CnCNet service | 318 | 🟢 | C# |
| [Slippi Launcher](https://github.com/project-slippi/slippi-launcher) | Launcher for Project Slippi, the rollback netplay and replay system for Super Smash Bros. Melee | 310 | 🟢 | TypeScript |
| [open-steamworks](https://github.com/SteamRE/open-steamworks) | Reverse engineered headers for Valve's Steam client interfaces | 263 | 🗄️ | C# |
| [xcloud-shield](https://github.com/mistertest/xcloud-shield) | Unofficial Xbox Cloud Gaming app for Nvidia Shield TV | 235 | 🔴 | Java |
| [Maxima](https://github.com/ArmchairDevelopers/Maxima) | Free open-source replacement for the EA Desktop launcher for Linux and Windows | 231 | 🟢 | Rust |
| [cordial](https://github.com/luohoa97/cordial) | Open-source runtime to run the Roblox client natively on Linux | 217 | 🟢 | Rust |
| [xbox-xcloud-player](https://github.com/unknownskl/xbox-xcloud-player) | Library implementing the Xbox Cloud Gaming / home streaming WebRTC protocol | 197 | 🟢 | TypeScript |
| [heroic-gogdl](https://github.com/Heroic-Games-Launcher/heroic-gogdl) | GOG download/install module for Heroic using GOG Galaxy's content-system APIs | 178 | 🟢 | Python |
| [games_nebula](https://github.com/yancharkin/games_nebula) | Unofficial GOG client for Linux | 160 | 🟡 | Python |
| [SteamAppInfo](https://github.com/xPaw/SteamAppInfo) | Parser for Steam client appinfo.vdf and packageinfo.vdf files | 143 | 🟢 | C# |
| [libnxbox](https://github.com/ursusworks/libnxbox) | Xbox Cloud Gaming streaming client for Nintendo Switch homebrew | 131 | 🟢 |  |
| [RA3Bar-RA3Launcher](https://github.com/lanyizi/RA3Bar-RA3Launcher) | Reimplementation of the Red Alert 3 game launcher | 130 | 🔴 | C++ |
| [jetisteam](https://github.com/iTaysonLab/jetisteam) | Unofficial Steam mobile client | 125 | 🟢 | Kotlin |
| [node-epicgames-client](https://github.com/SzymonLisowiec/node-epicgames-client) | Unofficial Epic Games Launcher client in JavaScript (login, friends, party, chat) | 112 | 🔴 | JavaScript |
| [wyvern](https://github.com/nicohman/wyvern) | Simple CLI client for installing and maintaining Linux GOG games | 100 | 🔴 | Rust |
| [steam-store](https://github.com/autarc/steam-store) | Client for the unofficial Steam storefront and Big Picture web API | 35 | 🔴 | JavaScript |

## Matching Decompilations — Arcade

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [namco22-decompile](https://github.com/spacestate1/namco22-decompile) | Decompilation of Namco System 22 arcade games | 224 | 🟢 | C |
| [Sonic the Fighters](https://github.com/biggestsonicfan/stfdecomp) | Matching decompilation of Sonic the Fighters (Sega Model 2 arcade, 1996) | 110 | 🟢 | Assembly |
| [F-Zero AX](https://github.com/TheInfiniteLegend/f-0-ax) | Matching decompilation of F-Zero AX (Triforce arcade, 2003) | 3 | 🟡 | C |
| [dk](https://gitlab.com/segaloco/dk) | Comprehensive disassembly of arcade Donkey Kong |  | ⚪ |  |
| [mb](https://gitlab.com/segaloco/mb) | Comprehensive disassembly of arcade Mario Bros. |  | ⚪ |  |

## Matching Decompilations — Atari

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [StarRaiders](https://github.com/lwiest/StarRaiders) | Reverse-engineered, fully documented 6502 source of Star Raiders | 183 | 🟡 |  |
| [Raiders2600](https://github.com/halkuncode/Raiders2600) | Reverse-engineered, commented source of Raiders of the Lost Ark for Atari 2600 | 175 | 🟢 | Assembly |
| [a26_mb](https://gitlab.com/segaloco/a26_mb) | Comprehensive disassembly of Mario Bros. for the Atari 2600 |  | ⚪ |  |

## Matching Decompilations — Game Boy / GBA / DS

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [pokered](https://github.com/pret/pokered) | Disassembly of Pokemon Red/Blue | 4,999 | 🟢 | Assembly |
| [pokeemerald](https://github.com/pret/pokeemerald) | Decompilation of Pokemon Emerald | 3,608 | 🟢 | C |
| [pokecrystal](https://github.com/pret/pokecrystal) | Disassembly of Pokemon Crystal | 2,531 | 🟢 | Assembly |
| [Pokémon FireRed/LeafGreen](https://github.com/pret/pokefirered) | Matching decompilation of Pokémon FireRed/LeafGreen (Game Boy Advance, 2004) | 1,671 | 🟢 | C |
| [Pokémon Ruby/Sapphire](https://github.com/pret/pokeruby) | Matching decompilation of Pokémon Ruby/Sapphire (Game Boy Advance, 2002) | 1,005 | 🟢 | C |
| [The Legend of Zelda: The Minish Cap](https://github.com/zeldaret/tmc) | Matching decompilation of The Legend of Zelda: The Minish Cap (Game Boy Advance, 2004) | 922 | 🟢 | C |
| [LADX-Disassembly](https://github.com/zladx/LADX-Disassembly) | Disassembly of The Legend of Zelda: Link's Awakening DX | 916 | 🟢 | Assembly |
| [Pokémon Yellow](https://github.com/pret/pokeyellow) | Disassembly of Pokémon Yellow (Game Boy, 1998) | 895 | 🟢 | Assembly |
| [Pokémon Gold/Silver](https://github.com/pret/pokegold) | Disassembly of Pokémon Gold/Silver (Game Boy Color, 1999) | 729 | 🟢 | Assembly |
| [Pokémon HeartGold/SoulSilver](https://github.com/pret/pokeheartgold) | Matching decompilation of Pokémon HeartGold/SoulSilver (Nintendo DS, 2009) | 704 | 🟢 | Assembly |
| [sa2](https://github.com/SAT-R/sa2) | Decompilation and port of Sonic Advance 1 & 2 (GBA) | 680 | 🟢 | C |
| [pokeplatinum](https://github.com/pret/pokeplatinum) | Decompilation of Pokemon Platinum | 573 | 🟢 | C |
| [Pokémon Diamond/Pearl](https://github.com/pret/pokediamond) | Matching decompilation of Pokémon Diamond/Pearl (Nintendo DS, 2006) | 543 | 🟢 | Assembly |
| [Pokémon Gold (SpaceWorld Demo)](https://github.com/pret/pokegold-spaceworld) | Disassembly of Pokémon Gold and Silver (Game Boy, 1997; Space World 1997 demo) | 403 | 🟢 | Assembly |
| [Pokémon TCG](https://github.com/pret/poketcg) | Disassembly of Pokémon Trading Card Game (Game Boy Color, 1998) | 333 | 🟢 | Assembly |
| [Pokémon Mystery Dungeon: Red Rescue Team](https://github.com/pret/pmd-red) | Matching decompilation of Pokémon Mystery Dungeon: Red Rescue Team (Game Boy Advance, 2005) | 287 | 🟢 | C |
| [Fire Emblem: The Sacred Stones (FEU)](https://github.com/FireEmblemUniverse/fireemblem8u) | Matching decompilation of Fire Emblem: The Sacred Stones (Game Boy Advance, 2004) | 228 | 🟢 | Assembly |
| [oracles-disasm](https://github.com/Stewmath/oracles-disasm) | Disassembly of Zelda: Oracle of Ages and Seasons | 221 | 🟢 | Assembly |
| [sm64ds-decomp](https://github.com/tangosdev/sm64ds-decomp) | Byte-matching decompilation of Super Mario 64 DS | 209 | 🟢 | C++ |
| [Pokémon Pinball](https://github.com/pret/pokepinball) | Disassembly of Pokémon Pinball (Game Boy Color, 1999) | 203 | 🟢 | Assembly |
| [Golden Sun](https://github.com/PascalPixel/alchemy) | Matching decompilation of Golden Sun (Game Boy Advance, 2001) | 181 | 🟢 | C |
| [Kirby & The Amazing Mirror](https://github.com/jiangzhengwenjz/katam) | Matching decompilation of Kirby & The Amazing Mirror (Game Boy Advance, 2004) | 159 | 🟢 | C |
| [Metroid: Zero Mission](https://github.com/metroidret/mzm) | Matching decompilation of Metroid: Zero Mission (Game Boy Advance, 2004) | 154 | 🟢 | C |
| [Pokémon Pinball Ruby & Sapphire](https://github.com/pret/pokepinballrs) | Matching decompilation of Pokémon Pinball Ruby & Sapphire (Game Boy Advance, 2003) | 149 | 🟢 | Assembly |
| [Pokémon Mystery Dungeon: Explorers of Sky](https://github.com/pret/pmd-sky) | Matching decompilation of Pokémon Mystery Dungeon: Explorers of Sky (Nintendo DS, 2009) | 144 | 🟢 | Assembly |
| [Pokémon Snap](https://github.com/ethteck/pokemonsnap) | Decompilation of Pokémon Snap | 113 | 🟢 | C |
| [The Legend of Zelda: Phantom Hourglass](https://github.com/zeldaret/ph) | Matching decompilation of The Legend of Zelda: Phantom Hourglass (Nintendo DS, 2007) | 113 | 🟢 | C++ |
| [Super Mario 3D Land](https://github.com/3dsdecomp/RedPepper) | Matching decompilation of Super Mario 3D Land (Nintendo 3DS, 2011) | 111 | 🟡 | C++ |
| [Kingdom Hearts 358/2 Days](https://github.com/Yokimitsuro/khdays-decomp) | Matching decompilation of Kingdom Hearts 358/2 Days (Nintendo DS, 2009) | 96 | 🟢 | C |
| [Pokémon TCG 2](https://github.com/pret/poketcg2) | Disassembly of Pokémon Card GB2 (Game Boy Color, 2001) | 96 | 🟢 | Assembly |
| [The Legend of Zelda: Ocarina of Time 3D](https://github.com/zeldaret/oot3d) | Matching decompilation of The Legend of Zelda: Ocarina of Time 3D (Nintendo 3DS, 2011) | 89 | 🟢 | C++ |
| [Sonic Advance 3](https://github.com/SAT-R/sa3) | Matching decompilation of Sonic Advance 3 (Game Boy Advance, 2004) | 87 | 🟢 | C |
| [Sonic Advance](https://github.com/SAT-R/sa1) | Matching decompilation of Sonic Advance (Game Boy Advance, 2001) | 77 | 🗄️ | C |
| [Metroid Fusion](https://github.com/metroidret/mf) | Matching decompilation of Metroid Fusion (Game Boy Advance, 2002) | 71 | 🟢 | C |
| [Pokémon Emerald (JP)](https://github.com/pret/pokeemerald-jp) | Matching decompilation of Pokémon Emerald (Game Boy Advance, 2004; Japanese version) | 69 | 🔴 | Assembly |
| [The Legend of Zelda: Spirit Tracks](https://github.com/zeldaret/st) | Matching decompilation of The Legend of Zelda: Spirit Tracks (Nintendo DS, 2009) | 67 | 🟢 | C++ |
| [New Super Mario Bros.](https://github.com/NSMB-Decomp/nsmb) | Matching decompilation of New Super Mario Bros. (Nintendo DS, 2006) | 65 | 🟢 | C++ |
| [Mario Kart DS](https://github.com/XorTroll/mkds-re) | Decompilation of Mario Kart DS | 64 | 🟡 | C |
| [Pokémon Black](https://github.com/squiddonaut/pokeblack) | Matching decompilation of Pokémon Black (Nintendo DS, 2010) | 62 | 🟢 | Assembly |
| [Phoenix Wright: Ace Attorney](https://github.com/atasro2/pwaa1) | Matching decompilation of Phoenix Wright: Ace Attorney (Game Boy Advance, 2001; Japanese Gyakuten Saiban) | 55 | 🟢 | C |
| [Kingdom Hearts: Chain of Memories](https://github.com/Pheenoh/khcom) | Matching decompilation of Kingdom Hearts: Chain of Memories (Game Boy Advance, 2004) | 54 | 🟢 | C |
| [Dragon Quest IX](https://github.com/DQIX/dqix-decomp) | Matching decompilation of Dragon Quest IX: Sentinels of the Starry Skies (Nintendo DS, 2009) | 50 | 🟢 | C++ |
| [Rhythm Heaven (DS)](https://github.com/patataofcourse/rhgold) | Decompilation of Rhythm Heaven (DS) | 50 | 🟢 | C |
| [Mega Man Zero 3](https://github.com/mmzret/rmz3) | Matching decompilation of Mega Man Zero 3 (Game Boy Advance, 2004) | 47 | 🟢 | Assembly |
| [Banjo-Kazooie: Grunty's Revenge](https://github.com/jellees/bkgr) | Matching decompilation of Banjo-Kazooie: Grunty's Revenge (Game Boy Advance, 2003) | 45 | 🟢 | Assembly |
| [Sonic Rush Adventure](https://github.com/RushRE/SonicRushAdventure-Decomp) | Matching decompilation of Sonic Rush Adventure (Nintendo DS, 2007) | 45 | 🟢 | C |
| [Harvest Moon: Friends of Mineral Town](https://github.com/StanHash/fomt) | Matching decompilation of Harvest Moon: Friends of Mineral Town (Game Boy Advance, 2003) | 42 | 🟢 | Assembly |
| [pokemonstadium](https://github.com/ethteck/pokemonstadium) | Decompilation of Pokemon Stadium | 41 | 🔴 | Assembly |
| [berry-fix](https://github.com/pret/berry-fix) | Decompilation of the Berry Fix Program in Pokemon Emerald and FireRed/LeafGreen | 39 | 🔴 | C |
| [Mario & Luigi: Superstar Saga](https://github.com/jellees/mlss) | Matching decompilation of Mario & Luigi: Superstar Saga (Game Boy Advance, 2003) | 38 | 🟢 | Assembly |
| [Fire Emblem: The Blazing Blade (JP)](https://github.com/MokhaLeee/FireEmblem7J) | Matching decompilation of Fire Emblem: Rekka no Ken (Game Boy Advance, 2003; Japanese Blazing Blade) | 37 | 🟢 | Assembly |
| [Mario Kart: Super Circuit](https://github.com/jellees/mksc) | Matching decompilation of Mario Kart: Super Circuit (Game Boy Advance, 2001) | 35 | 🟡 | Assembly |
| [Pokémon Black 2 and White 2](https://github.com/fuddlesworth/pokebw2) | Matching decompilation of Pokémon Black 2 and White 2 (Nintendo DS, 2012) | 35 | 🟢 | C |
| [colosseum-mb](https://github.com/pret/colosseum-mb) | Decompilation of the GBA multiboot for Pokemon Colosseum | 34 | 🟡 | C++ |
| [Castlevania: Order of Ecclesia](https://github.com/LagoLunatic/ooe) | Matching decompilation of Castlevania: Order of Ecclesia (Nintendo DS, 2008) | 32 | 🟡 | C |
| [mksc-decompilation](https://github.com/XOlifreX/mksc-decompilation) | Decompilation of Mario Kart Super Circuit (GBA) | 32 | 🔴 | Assembly |
| [tetris-gb-disasm](https://github.com/vinheim3/tetris-gb-disasm) | Complete disassembly of the Game Boy Tetris ROM | 32 | 🔴 | Assembly |
| [The World Ends With You](https://github.com/Yotona/twewy) | Matching decompilation of The World Ends With You (Nintendo DS, 2007) | 32 | 🟢 | C |
| [NSMB-Code-Reference](https://github.com/MammaMiaTeam/NSMB-Code-Reference) | Public code reference for patching New Super Mario Bros. DS (US) | 31 | 🟢 | C++ |
| [Golden Sun: The Broken Seal](https://github.com/Coaltergeist/goldensun-decomp) | Matching decompilation of Golden Sun: The Broken Seal (Game Boy Advance, 2001) | 30 | 🟢 | Assembly |
| [Mother 1+2](https://github.com/Normmatt/m12) | Matching decompilation of Mother 1+2 (Game Boy Advance, 2003) | 30 | 🟢 | C |
| [Reverse-Engineering-the-GameBoy-Tetris](https://github.com/h3nnn4n/Reverse-Engineering-the-GameBoy-Tetris) | Reverse engineering of the Game Boy Tetris ROM | 27 | 🔴 | Shell |
| [Castlevania: Aria of Sorrow](https://github.com/testyourmine/cvaos) | Matching decompilation of Castlevania: Aria of Sorrow (Game Boy Advance, 2003) | 26 | 🟢 | Assembly |
| [Donkey Kong '94](https://github.com/CelestialAmber/DKGBDisasm) | Disassembly of Donkey Kong (Game Boy, 1994) | 26 | 🔴 | Assembly |
| [Mario Party DS](https://github.com/mariopartyrd/mariopartyDS) | Decompilation of Mario Party DS | 24 | 🟡 | Python |
| [ZoidsLegacyDecomp](https://github.com/jmacato/ZoidsLegacyDecomp) | Matched decompilation of Zoids Legacy (GBA) | 23 | 🟢 | C |
| [pokemoon](https://github.com/gradenGnostic/pokemoon) | Decompilation of Pokemon Moon | 22 | 🟢 | C++ |
| [Fire Emblem: The Sacred Stones](https://github.com/laqieer/fireemblem8u) | Matching decompilation of Fire Emblem: The Sacred Stones (Game Boy Advance, 2004) | 20 | 🗄️ | Assembly |
| [hm3](https://github.com/Sanqui/hm3) | Partial disassembly of Harvest Moon 3 for Game Boy Color | 19 | 🔴 | Assembly |
| [Klonoa: Empire of Dreams](https://github.com/testyourmine/kleod) | Matching decompilation of Klonoa: Empire of Dreams (Game Boy Advance, 2001) | 19 | 🟢 | C |
| [Kirby: Nightmare in Dream Land](https://github.com/overjt/knidl) | Matching decompilation of Kirby: Nightmare in Dream Land (Game Boy Advance, 2002) | 18 | 🟢 | C |
| [Monster Hunter 4 Ultimate](https://github.com/mhvuze/mh4u-decomp) | Matching decompilation of Monster Hunter 4 Ultimate (Nintendo 3DS, 2014) | 18 | 🟢 |  |
| [Star Ocean: Blue Sphere](https://github.com/animaone/star-ocean-blue-sphere-source-code) | Source code of Star Ocean: Blue Sphere (Game Boy Color, 2001) | 18 | 🟡 | Assembly |
| [Summon Night: Craft Sword Monogatari](https://github.com/jiangzhengwenjz/csm3) | Matching decompilation of Summon Night: Craft Sword Monogatari (Game Boy Advance, 2003) | 18 | 🟡 | Assembly |
| [Fire Emblem: Shadow Dragon](https://github.com/Eebit/fe11-us) | Matching decompilation of Fire Emblem: Shadow Dragon (Nintendo DS, 2008) | 17 | 🟢 | C++ |
| [Phoenix Wright: Ace Attorney – Justice for All](https://github.com/atasro2/pwaa2) | Matching decompilation of Phoenix Wright: Ace Attorney – Justice for All (Game Boy Advance, 2002; Japanese Gyakuten Saiban 2) | 17 | 🟢 | Assembly |
| [Wario Land 4](https://github.com/TsilaAllaoui/warioland4) | Matching decompilation of Wario Land 4 (Game Boy Advance, 2001) | 17 | 🟢 | C |
| [Klonoa: Empire of Dreams](https://github.com/Dream-Atelier/kl-eod-decomp) | Matching decompilation of Klonoa: Empire of Dreams (Game Boy Advance, 2001) | 16 | 🟢 | C |
| [Inazuma Eleven 3: The Ogre](https://github.com/CacaBueno64/ie3ogres) | Matching decompilation of Inazuma Eleven 3: The Ogre (Nintendo DS, 2011) | 15 | 🟢 | Assembly |
| [Advance Wars 2: Black Hole Rising](https://github.com/Eebit/aw2bhr) | Matching decompilation of Advance Wars 2: Black Hole Rising (Game Boy Advance, 2003) | 14 | 🟡 | Assembly |
| [WarioWare, Inc.: Mega Microgames!](https://github.com/ShaffySwitcher/wariowareinc) | Matching decompilation of WarioWare, Inc.: Mega Microgames! (Game Boy Advance, 2003) | 14 | 🟢 | Assembly |
| [Kingdom Hearts Re:coded](https://github.com/kh-recoded-decomp/kh-recoded-decomp) | Matching decompilation of Kingdom Hearts Re:coded (Nintendo DS, 2010) | 13 | 🟢 | C |
| [Mario & Luigi: Partners in Time](https://github.com/Rainchus/PartnersInTime-Decomp) | Matching decompilation of Mario & Luigi: Partners in Time (Nintendo DS, 2005) | 13 | 🟢 | Python |
| [Pokémon Rumble](https://github.com/KooShnoo/pokemon-rumble) | Decompilation of Pokémon Rumble | 13 | 🟢 | C++ |
| [Dragon Quest IV](https://github.com/GoldieLeGenie/DQIV-DECOMP) | Matching decompilation of Dragon Quest IV (Nintendo DS, 2007) | 12 | 🟢 | C++ |
| [Paper Mario: Sticker Star](https://github.com/Darxoon/leaflitter) | Matching decompilation of Paper Mario: Sticker Star (Nintendo 3DS, 2012) | 12 | 🗄️ | Python |
| [Wario Land 4 (lilDavid)](https://github.com/lilDavid/warioland4) | Matching decompilation of Wario Land 4 (Game Boy Advance, 2001) | 12 | 🟢 | Assembly |
| [LEGO Battles](https://github.com/LiruJ/Lego-Battles-Decomp) | Matching decompilation of LEGO Battles (Nintendo DS, 2009) | 10 | 🟢 | C++ |
| [Sonic Battle](https://github.com/cypressru/SonicBattleDecomp) | Matching decompilation of Sonic Battle (Game Boy Advance, 2003) | 10 | 🟢 | C++ |
| [Super Mario 64 DS](https://github.com/matty45/sm64ds-decomp) | Decompilation of Super Mario 64 DS | 10 | 🗄️ | Assembly |
| [Custom Robo GX](https://github.com/pizdex/robogx) | Matching decompilation of Custom Robo GX (Game Boy Advance, 2004) | 9 | 🟢 | Assembly |
| [Dragon Warrior Monsters](https://github.com/NiyaDev/DWM) | Matching decompilation of Dragon Warrior Monsters (Game Boy Color, 1998) | 9 | 🟢 | Assembly |
| [DWM](https://github.com/Mallos31/dwm) | Disassembly of Dragon Warrior Monsters 1 for the GBC | 9 | 🔴 | Assembly |
| [FXHammer-Disasm](https://github.com/DevEd2/FXHammer-Disasm) | Disassembly of the FX Hammer Game Boy sound driver | 9 | 🔴 | Assembly |
| [The Urbz: Sims in the City (GBA)](https://github.com/SimsAdvanceRet/UrbzGBADecomp) | Decompilation of The Urbz: Sims in the City (GBA) | 9 | 🟡 |  |
| [Yu-Gi-Oh! The Eternal Duelist Soul](https://github.com/CosmicScribe64/eds-decomp) | Matching decompilation of Yu-Gi-Oh! The Eternal Duelist Soul (Game Boy Advance, 2002) | 9 | 🟢 | Assembly |
| [Beyblade VForce: Ultimate Blader Jam](https://github.com/marijnvdwerf/gba-beyblade-vforce) | Decompilation of Beyblade VForce: Ultimate Blader Jam | 8 | 🟢 | C |
| [Bomberman Land Touch! 2](https://github.com/gamemasterplc/bltouch2) | Matching decompilation of Bomberman Land Touch! 2 (Nintendo DS, 2008) | 7 | 🟢 | C |
| [eCrew Development Program](https://github.com/imavie/ecdpdecomp) | Matching decompilation of eCrew Development Program (Nintendo DS, 2010; McDonald's training game) | 6 | 🟡 |  |
| [Frogger's Adventures: Temple of the Frog](https://github.com/JRickey/frog-adv-temple-decomp) | Matching decompilation of Frogger's Adventures: Temple of the Frog (Game Boy Advance, 2001) | 6 | 🟢 | Assembly |
| [The Sims 2 (GBA)](https://github.com/SimsAdvanceRet/S2GBADecomp) | Decompilation of The Sims 2 (GBA) | 6 | 🟡 |  |
| [The Sims: Bustin' Out (GBA)](https://github.com/SimsAdvanceRet/BustinOutGBADecomp) | Decompilation of The Sims: Bustin' Out (GBA) | 6 | 🟡 |  |
| [GTPD-Code-Reference](https://github.com/Ed-1T/GTPD-Code-Reference) | Public decompilation reference for Ghost Trick: Phantom Detective (DS) | 5 | 🟡 | C++ |
| [jungle-book-gb-disassembly](https://github.com/not-chciken/jungle-book-gb-disassembly) | Disassembly of The Jungle Book (1994) for Game Boy | 5 | 🟢 | Assembly |
| [Harry Potter and the Prisoner of Azkaban (GBA)](https://github.com/holly-hacker/hp3-gba-decomp) | Decompilation of Harry Potter and the Prisoner of Azkaban (GBA) | 4 | 🟢 | C |
| [Princess Maker 4](https://github.com/Yanis002/pm4) | Matching decompilation of Princess Maker 4 (Nintendo DS; Japanese version) | 4 | 🟢 | C |
| [Air Traffic Chaos](https://github.com/sasja-san/atc) | Matching decompilation of Air Traffic Chaos (Nintendo DS, 2007) | 3 | 🟢 | Python |
| [Digimon World DS](https://github.com/ReGame-Labs/dwds_decomp) | Decompilation of Digimon World DS | 2 | 🟢 | C |
| [DuckTales (Game Boy) Disassembly](https://github.com/RussianManSMWC/DuckTales-of-Disassembly-GB) | A disassembly of DuckTales for the Game Boy | 2 | 🟢 | Assembly |
| [GT Advance 3: Pro Concept Racing](https://github.com/722rsr/gtadv3-decomp) | Matching decompilation of GT Advance 3: Pro Concept Racing (Game Boy Advance, 2003) | 2 | 🟢 | C |
| [Okamiden](https://github.com/dothacktranslate/okamiden-decomp) | Matching decompilation of Okamiden (Nintendo DS, 2010) | 2 | 🟢 | C |
| [NASCAR Heat 2002](https://github.com/shohamc1/heat2002) | Matching decompilation of NASCAR Heat 2002 (Game Boy Advance, 2001) | 1 | 🟢 | C |
| [DWM](https://codeberg.org/Emnity/DWM) | Decompilation of Dragon Warrior Monsters (Game Boy Color) |  | ⚪ |  |
| [kh-com](https://codeberg.org/aryan-sinhala349/kh-com) | Decompilation of Kingdom Hearts: Chain of Memories (GBA) |  | ⚪ |  |
| [Lock's Quest](https://github.com/redraincatching/locksmith) | Matching decompilation of Lock's Quest (Nintendo DS, 2008) | 0 | 🟡 |  |
| [ninjacop](https://gitlab.com/Fexean/ninjacop) | Disassembly of Ninja Cop (GBA) |  | ⚪ |  |
| [robogx](https://gitlab.com/Fexean/robogx) | Disassembly of Custom Robo GX (GBA) |  | ⚪ |  |
| [Shin Bokura no Taiyou: Gyakushuu no Sabata](https://github.com/moozilla/boktai3-decomp) | Matching decompilation of Shin Bokura no Taiyou: Gyakushuu no Sabata (Game Boy Advance, 2005) | 0 | 🟢 | C |
| [smbjr](https://gitlab.com/Fexean/smbjr) | Disassembly of Super Monkey Ball Jr. (GBA) |  | ⚪ |  |

## Matching Decompilations — GameCube & Wii

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Super Smash Bros. Melee](https://github.com/doldecomp/melee) | Matching decompilation of Super Smash Bros. Melee (GameCube, 2001) | 2,422 | 🟢 | C |
| [ac-decomp](https://github.com/ACreTeam/ac-decomp) | Decompilation of Animal Crossing for GameCube | 1,419 | 🟢 | C |
| [Super Mario Galaxy](https://github.com/SMGCommunity/Petari) | Matching decompilation of Super Mario Galaxy (Wii, 2007) | 1,259 | 🟢 | C++ |
| [Mario Party 4](https://github.com/mariopartyrd/marioparty4) | Matching decompilation of Mario Party 4 (GameCube, 2002) | 874 | 🟢 | C |
| [Mario Kart Wii (riidefi)](https://github.com/snailspeed3/mkw) | Decompilation of Mario Kart Wii (riidefi) | 471 | 🟡 | C |
| [Pikmin 2](https://github.com/projectPiki/pikmin2) | Matching decompilation of Pikmin 2 (GameCube, 2004) | 382 | 🟢 | C++ |
| [Metroid Prime](https://github.com/PrimeDecomp/prime) | Matching decompilation of Metroid Prime (GameCube, 2002) | 374 | 🟢 | C++ |
| [Super Mario Sunshine](https://github.com/doldecomp/sms) | Matching decompilation of Super Mario Sunshine (GameCube, 2002) | 356 | 🟢 | C++ |
| [re4 decomp](https://github.com/adonis-singh/re4) | Byte-identical decompilation of Resident Evil 4 (GameCube debug build) to C/C++ | 349 | 🟢 | C++ |
| [Pikmin](https://github.com/projectPiki/pikmin) | Matching decompilation of Pikmin (GameCube, 2001) | 323 | 🟢 | C |
| [Wii Menu](https://github.com/koopthekoopa/wii-ipl) | Decompilation of Wii Menu | 219 | 🟢 | C |
| [The Legend of Zelda: Skyward Sword](https://github.com/zeldaret/ss) | Matching decompilation of The Legend of Zelda: Skyward Sword (Wii, 2011) | 209 | 🟢 | C++ |
| [Mario Kart: Double Dash!!](https://github.com/doldecomp/mkdd) | Matching decompilation of Mario Kart: Double Dash!! (GameCube, 2003) | 200 | 🟢 | C++ |
| [SpongeBob SquarePants: Battle for Bikini Bottom](https://github.com/bfbbdecomp/bfbb) | Matching decompilation of SpongeBob SquarePants: Battle for Bikini Bottom (GameCube, 2003) | 192 | 🟢 | C++ |
| [Wii Sports](https://github.com/doldecomp/ogws) | Decompilation of Wii Sports | 175 | 🟢 | C |
| [Xenoblade Chronicles](https://github.com/xbret/xenoblade) | Matching decompilation of Xenoblade Chronicles (Wii, 2010) | 145 | 🟢 | C |
| [Paper Mario: The Thousand-Year Door](https://github.com/doldecomp/ttyd) | Matching decompilation of Paper Mario: The Thousand-Year Door (GameCube, 2004) | 144 | 🟢 | C |
| [New Super Mario Bros. Wii](https://github.com/NSMBW-Community/NSMBW-Decomp) | Decompilation of New Super Mario Bros. Wii | 143 | 🟢 | C |
| [Rock Band 3 decomp](https://github.com/DarkRTA/rb3) | Decompilation of Rock Band 3 (Wii) | 123 | 🟢 | C++ |
| [Super Mario Strikers](https://github.com/yannicksuter/smstrikers-decomp) | Matching decompilation of Super Mario Strikers (GameCube, 2005) | 105 | 🟢 | C++ |
| [Super Paper Mario](https://github.com/SeekyCt/spm-decomp) | Matching decompilation of Super Paper Mario (Wii, 2007) | 102 | 🟢 | C |
| [Super Smash Bros. Brawl](https://github.com/doldecomp/brawl) | Matching decompilation of Super Smash Bros. Brawl (Wii, 2008) | 102 | 🟢 | C++ |
| [SMGDecompilation](https://github.com/snailspeed3/SMGDecompilation) | Work-in-progress decompilation of Super Mario Galaxy | 95 | 🔴 | Assembly |
| [FRAY](https://github.com/PsiLupan/FRAY) | Recompilable Super Smash Bros. Melee 1.02 based on libOGC | 94 | 🔴 | C |
| [Kirby Air Ride (doldecomp)](https://github.com/doldecomp/kar) | Matching decompilation of Kirby Air Ride (GameCube, 2003) | 89 | 🟡 | Assembly |
| [Star Fox Adventures](https://github.com/zcanann/SFA-Decomp) | Matching decompilation of Star Fox Adventures (GameCube, 2002) | 79 | 🟢 | C |
| [Super Mario Galaxy 2](https://github.com/SMGCommunity/Garigari) | Matching decompilation of Super Mario Galaxy 2 (Wii, 2010) | 75 | 🟢 | C |
| [Mario Kart Wii](https://github.com/doldecomp/mkw) | Decompilation of Mario Kart Wii | 55 | 🟢 | C |
| [Kirby's Epic Yarn](https://github.com/Swiftshine/key) | Matching decompilation of Kirby's Epic Yarn (Wii, 2010) | 53 | 🟢 | C++ |
| [Animal Forest e+](https://github.com/ACreTeam/afe-decomp) | Matching decompilation of Animal Forest e+ (GameCube, 2003) | 51 | 🟢 | C |
| [Sonic Adventure DX](https://github.com/doldecomp/sadx) | Matching decompilation of Sonic Adventure DX (GameCube, 2003) | 48 | 🟡 | Python |
| [Final Fantasy Crystal Chronicles](https://github.com/zcanann/FFCC-Decomp) | Matching decompilation of Final Fantasy Crystal Chronicles (GameCube, 2003) | 44 | 🟢 | C |
| [Chibi-Robo!](https://github.com/eavpsp/cbr_decomp) | Matching decompilation of Chibi-Robo! (GameCube, 2005) | 40 | 🟢 | C++ |
| [Mario Party 5](https://github.com/mariopartyrd/marioparty5) | Matching decompilation of Mario Party 5 (GameCube, 2003) | 39 | 🟢 | C |
| [Pokémon XD: Gale of Darkness](https://github.com/TeamOrre/xd-decomp) | Matching decompilation of Pokémon XD: Gale of Darkness (GameCube, 2005) | 39 | 🟢 | C |
| [Need for Speed: Underground](https://github.com/dbalatoni13/nfsug) | Matching decompilation of Need for Speed: Underground (GameCube, 2003) | 38 | 🟢 | C |
| [recvx-gc-decomp](https://github.com/fmil95/recvx-gc-decomp) | Decompilation of Resident Evil Code: Veronica X (GameCube) | 37 | 🟢 | C |
| [Sonic Riders](https://github.com/doldecomp/sonicriders) | Matching decompilation of Sonic Riders (GameCube, 2006) | 37 | 🔴 | Assembly |
| [TY the Tasmanian Tiger](https://github.com/1superchip/ty-decomp) | Matching decompilation of TY the Tasmanian Tiger (GameCube, 2002) | 37 | 🟢 | C++ |
| [Luigi's Mansion (zmansion)](https://github.com/Sage-of-Mirrors/zmansion) | Matching decompilation of Luigi's Mansion (GameCube, 2001) | 36 | 🟡 | C |
| [Mario Strikers Charged](https://github.com/yannicksuter/mscharged-decomp) | Matching decompilation of Mario Strikers Charged (Wii, 2007) | 36 | 🟢 | C++ |
| [Sonic Heroes](https://github.com/Jovinull/sonicheroes) | Matching decompilation of Sonic Heroes (GameCube, 2003) | 32 | 🟢 | C++ |
| [dolsdk2001](https://github.com/doldecomp/dolsdk2001) | Decompilation of the 2001 Dolphin (GameCube) SDK libraries | 30 | 🟡 | C |
| [Mario Party 7](https://github.com/mariopartyrd/marioparty7) | Matching decompilation of Mario Party 7 (GameCube, 2005) | 29 | 🟢 | C |
| [Pokémon Colosseum](https://github.com/dougchansan/pkmn-colosseum) | Matching decompilation of Pokémon Colosseum (GameCube, 2003) | 29 | 🟢 | C |
| [Rhythm Heaven Fever](https://github.com/conhlee/rhf) | Matching decompilation of Rhythm Heaven Fever (Wii, 2011) | 29 | 🟢 | C++ |
| [Star Fox Adventures (sfadebug)](https://github.com/RenaKunisaki/sfadebug) | Matching decompilation of Star Fox Adventures (GameCube, 2002; debug version) | 27 | 🟢 | C |
| [Pokémon Battle Revolution](https://github.com/pbr-ret/pbr-decomp) | Matching decompilation of Pokémon Battle Revolution (Wii, 2006) | 25 | 🟢 | C |
| [Gauntlet: Dark Legacy](https://github.com/sabishii-bit/Gauntlet-Dark-Legacy-Decompilation) | Matching decompilation of Gauntlet: Dark Legacy (GameCube, 2001) | 24 | 🟢 | C |
| [Harvest Moon: A Wonderful Life](https://github.com/ChrisNonyminus/hmawl) | Matching decompilation of Harvest Moon: A Wonderful Life (GameCube, 2003) | 24 | 🔴 | Assembly |
| [Mario Party 8](https://github.com/mariopartyrd/marioparty8) | Matching decompilation of Mario Party 8 (Wii, 2007) | 24 | 🟢 | Python |
| [The Incredibles](https://github.com/seilc/incredibles) | Matching decompilation of The Incredibles (GameCube, 2004) | 24 | 🔴 | Assembly |
| [The SpongeBob SquarePants Movie](https://github.com/bfbbdecomp/tssm) | Matching decompilation of The SpongeBob SquarePants Movie (GameCube, 2004) | 24 | 🟢 | C++ |
| [Naruto: Gekitō Ninja Taisen! 4](https://github.com/doldecomp/gnt4) | Matching decompilation of Naruto: Gekitō Ninja Taisen! 4 (GameCube, 2005) | 23 | 🔴 | Assembly |
| [The Sims 2 (GameCube)](https://github.com/natebag/Sims2DECOMP) | Decompilation of The Sims 2 (GameCube) | 23 | 🟢 | C++ |
| [Mario Party 6 (mariopartyrd)](https://github.com/mariopartyrd/marioparty6) | Matching decompilation of Mario Party 6 (GameCube, 2004) | 22 | 🟢 | C |
| [Mario Party 9 (mariopartyrd)](https://github.com/mariopartyrd/marioparty9) | Matching decompilation of Mario Party 9 (Wii, 2012) | 22 | 🟡 | C |
| [New Play Control! Pikmin 2](https://github.com/projectPiki/pik2wii) | Matching decompilation of New Play Control! Pikmin 2 (Wii, 2009) | 22 | 🟢 | C++ |
| [open_rvl](https://github.com/kiwi515/open_rvl) | Decompilation of the Wii RVL SDK | 22 | 🗄️ | C |
| [LEGO Star Wars III: The Clone Wars (Wii)](https://github.com/ThePlayerRolo/LegoCloneWarsWii) | Decompilation of LEGO Star Wars III: The Clone Wars (Wii) | 21 | 🟢 | C |
| [Forecast Channel (Wii)](https://github.com/doldecomp/forecast) | Decompilation of Forecast Channel (Wii) | 20 | 🟢 | C |
| [Ratchet & Clank: Going Commando (USA v1.01)](https://github.com/OpenRAC/rac2-gc-decomp) | Decompilation of Ratchet & Clank: Going Commando (USA v1.01) | 20 | 🟢 | C |
| [The Sims 2: Castaway](https://github.com/HaydnTrigg/Castaway) | Matching decompilation of The Sims 2: Castaway (Wii, 2007) | 18 | 🟢 | C |
| [Disney's Piglet's Big Game](https://github.com/tgsm/pbg) | Matching decompilation of Disney's Piglet's Big Game (GameCube, 2003) | 17 | 🟢 | C |
| [Hagi (GameCube/Wii emulator in Super Mario 3D All-Stars)](https://github.com/GRAnimated/Hagi) | Decompilation of Hagi (GameCube/Wii emulator in Super Mario 3D All-Stars) | 17 | 🟢 | C |
| [PokéPark Wii: Pikachu's Adventure](https://github.com/SephDB/pokepark-wii-decomp) | Decompilation of PokéPark Wii: Pikachu's Adventure | 17 | 🟢 | C |
| [Skies of Arcadia Legends](https://github.com/Rainchus/SkiesOfArcadiaLegends) | Matching decompilation of Skies of Arcadia Legends (GameCube, 2002) | 17 | 🟡 | Python |
| [Tiger Woods PGA Tour 2004](https://github.com/mitsevox/tw2004) | Matching decompilation of Tiger Woods PGA Tour 2004 (GameCube, 2003) | 17 | 🟢 | C |
| [Inazuma Eleven Strikers](https://github.com/SwareJonge/IEStrikers) | Matching decompilation of Inazuma Eleven Strikers (Wii, 2012) | 16 | 🟡 | C |
| [Mario Superstar Baseball (dtk)](https://github.com/roeming/mssb-dtk) | Matching decompilation of Mario Superstar Baseball (GameCube, 2005) | 16 | 🟢 | C |
| [Mortal Kombat: Deception](https://github.com/ShulkMaster/mk-deception) | Matching decompilation of Mortal Kombat: Deception (GameCube, 2004) | 16 | 🟢 | C |
| [Wii Play](https://github.com/akiramusic000/Rhae) | Decompilation of Wii Play | 16 | 🟢 | C |
| [Sonic Adventure 2: Battle](https://github.com/roeming/SA2B) | Matching decompilation of Sonic Adventure 2: Battle (GameCube, 2001) | 15 | 🟢 | C |
| [Crash Bandicoot: The Wrath of Cortex (GameCube)](https://github.com/denzi-gh/crashwoc-decomp-gc) | Decompilation of Crash Bandicoot: The Wrath of Cortex (GameCube) | 14 | 🟢 | C |
| [Kirby's Dream Collection Special Edition](https://github.com/Swiftshine/kdc) | Matching decompilation of Kirby's Dream Collection Special Edition (Wii, 2012) | 14 | 🟢 | C |
| [New Play Control! Pikmin](https://github.com/projectPiki/pik1wii) | Matching decompilation of New Play Control! Pikmin (Wii, 2008) | 14 | 🟢 | C |
| [Sonic Riders: Zero Gravity](https://github.com/KidWizardOfTheWeb/SRZGDecomp) | Matching decompilation of Sonic Riders: Zero Gravity (Wii, 2008) | 14 | 🔴 | Assembly |
| [Alice in Wonderland (2010)](https://github.com/Alice-2010/Decomp) | Matching decompilation of Alice in Wonderland (Wii, 2010) | 13 | 🟢 | C |
| [Crash Tag Team Racing](https://github.com/bluisblu/cttr) | Matching decompilation of Crash Tag Team Racing (GameCube, 2005) | 13 | 🟢 | C |
| [Doshin the Giant](https://github.com/break-core/doshin-gc) | Decompilation of Doshin the Giant | 13 | 🟢 | Python |
| [F-Zero GX (alt)](https://github.com/karamzov123/fzero-gx-decomp) | Matching decompilation of F-Zero GX (GameCube, 2003) | 12 | 🟢 | C |
| [Digimon World 4](https://github.com/ivanno4317/dw4-gc) | Decompilation of Digimon World 4 | 10 | 🟢 | C |
| [F-Zero GX](https://github.com/rayanht/fzgx) | Matching decompilation of F-Zero GX (GameCube, 2003) | 10 | 🟢 | C |
| [Luigi's Mansion](https://github.com/SomeJakeGuy/lm-decomp) | Matching decompilation of Luigi's Mansion (GameCube, 2001) | 10 | 🟢 | C |
| [Eternal Darkness: Sanity's Requiem](https://github.com/PattyTrish/unending-occlusion) | Matching decompilation of Eternal Darkness: Sanity's Requiem (GameCube, 2002) | 8 | 🟢 | C |
| [Summoner: A Goddess Reborn](https://github.com/Charlese2/sgr) | Matching decompilation of Summoner: A Goddess Reborn (GameCube, 2002) | 8 | 🟢 | C |
| [Big Brain Academy: Wii Degree](https://github.com/vabold/bba-wd) | Decompilation of Big Brain Academy: Wii Degree | 7 | 🟡 | Python |
| [Kirby Air Ride](https://github.com/wowjinxy/KAR) | Matching decompilation of Kirby Air Ride (GameCube, 2003) | 7 | 🟢 | C |
| [Metrowerks CodeWarrior for GameCube (compiler)](https://github.com/rayanht/mwcc) | Decompilation of Metrowerks CodeWarrior for GameCube (compiler) | 7 | 🟢 | C |
| [Donkey Kong Country Returns](https://github.com/Wexos/DKCR-Decompilation) | Matching decompilation of Donkey Kong Country Returns (Wii, 2010) | 6 | 🟡 | Python |
| [Homeland](https://github.com/BttrDrgn/homeland) | Matching decompilation of HomeLand (GameCube, 2005) | 6 | 🔴 | Assembly |
| [Nintendo Puzzle Collection: Dr. Mario 64](https://github.com/NewGBAXL/drmario64-gc) | Decompilation of Nintendo Puzzle Collection: Dr. Mario 64 | 6 | 🟢 | C |
| [Wario World](https://github.com/sabishii-bit/wwdcmp) | Matching decompilation of Wario World (GameCube, 2003) | 6 | 🟡 | Assembly |
| [Dragon Ball Z: Budokai 2](https://github.com/TotallyNotMichael-GH/dbz2) | Matching decompilation of Dragon Ball Z: Budokai 2 (GameCube, 2004) | 5 | 🟡 | Python |
| [Mario Party 6](https://github.com/iirg4x/marioparty6) | Matching decompilation of Mario Party 6 (GameCube, 2004) | 5 | 🟢 | C |
| [Medal of Honor: Frontline](https://github.com/kyleckroeger/moh-frontline-decomp) | Matching decompilation of Medal of Honor: Frontline (GameCube, 2002) | 5 | 🟢 | C |
| [NFL Street 2](https://github.com/mitsevox/nflstreet2) | Matching decompilation of NFL Street 2 (GameCube, 2004) | 5 | 🟢 | C++ |
| [Go Vacation](https://github.com/Moddimation/GoVacation-Decompilation) | Matching decompilation of Go Vacation (Wii, 2011) | 4 | 🗄️ | C |
| [Medal of Honor: Rising Sun](https://github.com/lifewillbeokay/moh-rising-sun) | Matching decompilation of Medal of Honor: Rising Sun (GameCube, 2003) | 4 | 🟢 | C |
| [Fortune Street](https://github.com/FortuneStreetModding/boom-street-decomp) | Matching decompilation of Fortune Street (Wii, 2011; Boom Street) | 3 | 🟡 | C |
| [Freedom Fighters](https://github.com/andresj-sanchez/frfi-decomp) | Matching decompilation of Freedom Fighters (GameCube, 2003) | 3 | 🟢 | Python |
| [I Spy Spooky Mansion](https://github.com/AM7999/ISpy-SM-Decomp) | Decompilation of I Spy Spooky Mansion (Wii), based on the included debug executable | 3 | 🟡 | C++ |
| [Mario Party 9](https://github.com/ricky074game/marioparty9) | Matching decompilation of Mario Party 9 (Wii, 2012) | 3 | 🟢 | C++ |
| [Mario Sports Mix](https://github.com/EltyDev/MSM-decomp) | Matching decompilation of Mario Sports Mix (Wii, 2010) | 3 | 🟡 | Python |
| [Excite Truck](https://github.com/orangedude27/excite-truck) | Matching decompilation of Excite Truck (Wii, 2006) | 2 | 🟢 | Python |
| [MVP Baseball 2005](https://github.com/mitsevox/mvp2005) | Matching decompilation of MVP Baseball 2005 (GameCube, 2005) | 2 | 🟢 | C |
| [Radio Helicopter](https://github.com/Bsquo/pcopter_wii) | Decompilation of Radio Helicopter | 2 | 🟡 | C |
| [Super Mario All-Stars 25th Anniversary Edition](https://github.com/ThePlayerRolo/Super-Mario-All-Star-Decomp) | Matching decompilation of Super Mario All-Stars 25th Anniversary Edition (Wii, 2010) | 2 | 🟢 | C |
| [Wii Fit Plus](https://github.com/Tanline666/veryfat-dungeon) | Decompilation of Wii Fit Plus | 2 | 🟢 | C |
| [World of Goo (WiiWare)](https://github.com/Fancy2209/wog-wiiware) | Matching decompilation of World of Goo (Wii, 2008; WiiWare) | 2 | 🟡 | C++ |
| [Amazing Island](https://github.com/EltaleLibrarian/Amazing) | Matching decompilation of Amazing Island (GameCube, 2004) | 1 | 🟡 | Python |
| [Mortal Kombat: Deadly Alliance](https://github.com/ShulkMaster/mk-da) | Matching decompilation of Mortal Kombat: Deadly Alliance (GameCube, 2002) | 1 | 🟢 | C |
| [Taiko no Tatsujin Wii: Ketteiban](https://github.com/CalebPancake/Taiko-No-Tatsujin-Wii-Ketteiban) | Decompilation of Taiko no Tatsujin Wii: Ketteiban | 1 | 🟡 |  |
| [Wario Land: Shake It!](https://github.com/Swiftshine/wlsi) | Matching decompilation of Wario Land: Shake It! (Wii, 2008) | 1 | 🟢 | C |
| [Mario Superstar Baseball](https://github.com/nlopez99/mssb-decomp) | Matching decompilation of Mario Superstar Baseball (GameCube, 2005) | 0 | 🟢 | C |
| [pso-gc](https://gitlab.com/mrb0nk500/pso-gc) | Decompilation of Phantasy Star Online Episode I & II for the GameCube |  | ⚪ |  |
| [pyssg-decomp](https://codeberg.org/retreev/pyssg-decomp) | Work-in-progress decompilation of PangYa: Super Swing Golf (Wii) |  | ⚪ |  |

## Matching Decompilations — Mobile

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Sonic CD (2011 mobile)](https://github.com/RSDKModding/RSDKv3-Decompilation) | Decompilation of Sonic CD (2011 remaster) and Retro Engine v3 (Mobile, 2011) | 712 | 🟢 | C++ |
| [Sonic Runners](https://github.com/itsmattkc/RunnersDecomp) | Matching decompilation of Sonic Runners (Mobile, 2015) | 244 | 🔴 | C# |
| [DoomRPG-RE](https://github.com/Erick194/DoomRPG-RE) | Reverse engineered source of Doom RPG | 161 | 🟡 | C |
| [DoomIIRPG-RE](https://github.com/Erick194/DoomIIRPG-RE) | Reverse engineered source of Doom II RPG | 99 | 🟡 | C++ |
| [Angry Birds](https://github.com/jooapa/Angry_Birds_Decompilation) | Decompilation scripts and instructions for the six classic Angry Birds games (Mobile, 2009–2014) | 52 | 🟡 | Python |
| [Geometry Dash](https://github.com/aloaf812/GD) | Decompilation of Geometry Dash v1.710 (Mobile, 2013) | 36 | 🟢 | C++ |
| [Sonic the Hedgehog (J2ME)](https://github.com/Iso-Kilo/Sonic-1-J2ME-Decompilation) | Matching decompilation of Sonic the Hedgehog (J2ME mobile, 2005) | 36 | 🔴 | Java |
| [Samurai vs Zombies Defense](https://github.com/Decomp-And-Recomp/Samurai-Vs-Zombies) | Decompilation of Samurai vs Zombies Defense by Glu (Mobile, 2012) | 26 | 🟢 | C# |
| [Dragon Ball Legends](https://github.com/GodkuHacking/Dragon-Ball-Legends) | APK decompilation of Dragon Ball Legends (Mobile, 2018) | 16 | 🟡 | Smali |
| [Brave Frontier](https://github.com/decompfrontier/client) | Decompilation of the Brave Frontier client (Mobile, 2013) | 14 | 🟡 | C |
| [SpongeBob Moves In!](https://github.com/Juanen100/SBMI-Decomp) | Decompilation of the Android client of SpongeBob Moves In! (Mobile, 2013) | 14 | 🟢 | C# |
| [Diamond Rush](https://github.com/palaceswitcher/Diamond-Rush-Decomp) | Matching decompilation of Diamond Rush (J2ME mobile, 2006) | 9 | 🟢 | Java |
| [Idle Office Tycoon](https://github.com/Avenze/ios_reverse_engineering) | Reverse engineering notes and decompilation of the iOS game Idle Office Tycoon (Mobile) | 5 | 🟡 | Lua |
| [Flappy Bird](https://github.com/fr3dsp/FlappyBird-Decomp) | Decompilation of Flappy Bird (Windows Phone, 2013) | 4 | 🟢 | C# |
| [Skylanders: Cloud Patrol](https://github.com/spyrosadventure/cloud-patrol-decomp) | Decompilation of Skylanders: Cloud Patrol (Mobile, 2012) | 4 | 🟡 | C# |
| [Bounce](https://github.com/misterjdrg/Bouncer) | Decompilation of Bounce (J2ME mobile, 2001) | 3 | 🟡 | Java |
| [Ancient Empires](https://github.com/Atomk/ancient-empires-1-decompilation) | Matching decompilation of Ancient Empires (J2ME mobile, 2004) | 2 | 🟡 | Java |
| [Defenders & Dragons](https://github.com/Lindarychwalski/Defenders-Dragons) | Decompilation of Defenders & Dragons by Glu (Mobile) | 2 | 🟡 |  |
| [Five Nights at Freddy's](https://github.com/fr3dsp/FNaF-Decomp) | Decompilation of Five Nights at Freddy's (Windows Phone, 2014) | 2 | 🟢 | C# |
| [Five Nights at Freddy's 2](https://github.com/fr3dsp/FNaF-2-Decomp) | Decompilation of Five Nights at Freddy's 2 (Windows Phone, 2014) | 2 | 🟢 | C# |
| [Green Farm 3](https://github.com/SmithGoll/Greenier-Farm-3-Decomp) | Non-matching decompilation of Gameloft's Green Farm 3 (J2ME mobile) | 2 | 🟡 | Java |
| [Mixels Rush](https://github.com/Nugetinc/MixelsRushDecompilation) | Experimental decompilation of Mixels Rush (Mobile, 2015) | 2 | 🟡 |  |
| [Chiki's Chase](https://github.com/gays-studio/ChikisChaseAPK) | Decompiled (apktool) Android build of Chiki's Chase (Mobile) | 1 | 🟡 | Smali |
| [Smash-Hit-Decomp](https://codeberg.org/Shards/Smash-Hit-Decomp) | Decompilation of the mobile game Smash Hit |  | ⚪ |  |
| [Super Cat Tales: PAWS](https://codeberg.org/heathercat123/PAWS-Decomp) | Decompilation of Super Cat Tales: PAWS (Mobile) |  | ⚪ |  |

## Matching Decompilations — Nintendo 64

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Perfect Dark PC port](https://github.com/perfect-dark-pc-port/perfect_dark) | Port of the Perfect Dark N64 decompilation to modern platforms | 2,059 | 🟢 | C |
| [Paper Mario](https://github.com/pmret/papermario) | Matching decompilation of Paper Mario (Nintendo 64, 2000) | 1,636 | 🟢 | C |
| [Mario Kart 64](https://github.com/n64decomp/mk64) | Matching decompilation of Mario Kart 64 (Nintendo 64, 1996) | 1,313 | 🟢 | C |
| [Perfect Dark decompilation (n64decomp)](https://github.com/n64decomp/perfect_dark) | Matching decompilation of Perfect Dark (N64) | 871 | 🟡 | C |
| [GoldenEye 007 decomp](https://github.com/n64decomp/007) | Matching decompilation of GoldenEye 007 | 800 | 🟢 | C |
| [banjo-kazooie](https://github.com/n64decomp/banjo-kazooie) | Decompilation of Banjo-Kazooie | 655 | 🟢 | C |
| [HackerSM64](https://github.com/HackerN64/HackerSM64) | Super Mario 64 decompilation fork tuned for romhacking | 538 | 🟢 | C |
| [Diddy Kong Racing](https://github.com/DavidSM64/Diddy-Kong-Racing) | Matching decompilation of Diddy Kong Racing (Nintendo 64, 1997) | 423 | 🟢 | C |
| [Star Fox 64](https://github.com/sonicdcer/sf64) | Matching decompilation of Star Fox 64 (Nintendo 64, 1997) | 354 | 🟢 | C |
| [Animal Forest](https://github.com/zeldaret/af) | Matching decompilation of Animal Forest (Nintendo 64, 2001) | 301 | 🟢 | C |
| [oot](https://github.com/n64decomp/oot) | Decompilation of Ocarina of Time Master Quest debug build | 285 | 🗄️ | Assembly |
| [Duke Nukem: Zero Hour](https://github.com/Gillou68310/DukeNukemZeroHour) | Matching decompilation of Duke Nukem: Zero Hour (Nintendo 64, 1999) | 277 | 🟢 | C |
| [Super Smash Bros.](https://github.com/VetriTheRetri/ssb-decomp-re) | Matching decompilation of Super Smash Bros. (Nintendo 64, 1999) | 269 | 🟢 | C |
| [Conker's Bad Fur Day (mkst)](https://github.com/mkst/conker) | Matching decompilation of Conker's Bad Fur Day (Nintendo 64, 2001) | 239 | 🗄️ | C |
| [Doom 64 (DOOM64-RE)](https://github.com/Erick194/DOOM64-RE) | Reverse-engineered source of Doom 64 (Nintendo 64, 1997) | 237 | 🟡 | C |
| [Kirby 64: The Crystal Shards](https://github.com/Kirby64Ret/kirby64) | Matching decompilation of Kirby 64: The Crystal Shards (Nintendo 64, 2000) | 235 | 🟢 | Assembly |
| [Harvest Moon 64](https://github.com/harvestwhisperer/hm64-decomp) | Matching decompilation of Harvest Moon 64 (Nintendo 64, 1999) | 224 | 🟢 | C |
| [Dinosaur Planet](https://github.com/zestydevy/dinosaur-planet) | Matching decompilation of Dinosaur Planet (Nintendo 64, unreleased 2000 build) | 217 | 🟢 | C |
| [Pokémon Stadium](https://github.com/pret/pokestadium) | Matching decompilation of Pokémon Stadium (Nintendo 64, 1999) | 212 | 🟢 | C |
| [Snowboard Kids 2](https://github.com/cdlewis/snowboardkids2-decomp) | Matching decompilation of Snowboard Kids 2 (Nintendo 64, 1999) | 195 | 🟢 | C |
| [libreultra](https://github.com/n64decomp/libreultra) | Matching decompilation of the N64 libultra SDK library | 184 | 🔴 | C |
| [Banjo-Tooie](https://github.com/Mr-Wiseguy/banjo-tooie) | Matching decompilation of Banjo-Tooie (Nintendo 64, 2000) | 150 | 🟢 | C |
| [N64 Emulator for GameCube (OoT Master Quest)](https://github.com/zeldaret/oot-gc) | Decompilation of N64 Emulator for GameCube (OoT Master Quest) | 150 | 🟡 | C |
| [sdk-tools](https://github.com/n64decomp/sdk-tools) | Decompilation of the Nintendo 64 SDK developer tools | 146 | 🔴 | C |
| [majora](https://github.com/n64decomp/majora) | Decompilation of The Legend of Zelda: Majora's Mask | 138 | 🗄️ | C |
| [Wave Race 64](https://github.com/LLONSIT/Wave-Race-64) | Matching decompilation of Wave Race 64 (Nintendo 64, 1996) | 111 | 🟢 | Assembly |
| [F-Zero X](https://github.com/inspectredc/fzerox) | Matching decompilation of F-Zero X (Nintendo 64, 1998) | 108 | 🟢 | C |
| [N64 Emulator for Wii (OoT Virtual Console)](https://github.com/zeldaret/oot-vc) | Decompilation of N64 Emulator for Wii (OoT Virtual Console) | 95 | 🟢 | C |
| [HackerOoT](https://github.com/HackerN64/HackerOoT) | Ocarina of Time decompilation fork tuned for romhacking | 92 | 🟢 | C |
| [Mario Party](https://github.com/mariopartyrd/marioparty) | Matching decompilation of Mario Party (Nintendo 64, 1998) | 82 | 🟢 | C |
| [Yoshi's Story](https://github.com/decompals/yoshis-story) | Matching decompilation of Yoshi's Story (Nintendo 64, 1997) | 82 | 🟢 | C |
| [Dr. Mario 64](https://github.com/AngheloAlf/drmario64) | Matching decompilation of Dr. Mario 64 (Nintendo 64, 2001) | 81 | 🟢 | C |
| [Pilotwings 64](https://github.com/n64decomp/pw64) | Matching decompilation of Pilotwings 64 (Nintendo 64, 1996) | 81 | 🟢 | C |
| [Mischief Makers](https://github.com/Drahsid/mischief-makers) | Matching decompilation of Mischief Makers (Nintendo 64, 1997) | 72 | 🟢 | C |
| [Mario Party 3](https://github.com/mariopartyrd/marioparty3) | Matching decompilation of Mario Party 3 (Nintendo 64, 2000) | 71 | 🟢 | C |
| [ultralib](https://github.com/decompals/ultralib) | Reverse engineering of the N64 libultra library | 68 | 🟢 | C |
| [Castlevania 64](https://github.com/k64ret/cv64) | Matching decompilation of Castlevania 64 (Nintendo 64, 1999) | 66 | 🟢 | C |
| [Space Station Silicon Valley](https://github.com/mkst/sssv) | Matching decompilation of Space Station Silicon Valley (Nintendo 64, 1998) | 66 | 🟢 | C |
| [Bomberman Hero](https://github.com/Bomberhackers/bmhero) | Matching decompilation of Bomberman Hero (Nintendo 64, 1998) | 62 | 🟢 | C |
| [Pokémon Stadium 2](https://github.com/pret/pokestadiumgs) | Matching decompilation of Pokémon Stadium 2 (Nintendo 64, 2000) | 60 | 🟢 | C |
| [Jet Force Gemini](https://github.com/Ryan-Myers/Jet-Force-Gemini) | Matching decompilation of Jet Force Gemini (Nintendo 64, 1999) | 55 | 🟢 | C |
| [Snowboard Kids](https://github.com/cdlewis/snowboardkids-decomp) | Matching decompilation of Snowboard Kids (Nintendo 64, 1997) | 55 | 🟢 | C |
| [Mario Party 2](https://github.com/mariopartyrd/marioparty2) | Matching decompilation of Mario Party 2 (Nintendo 64, 1999) | 52 | 🟢 | C |
| [f3dex2](https://github.com/Mr-Wiseguy/f3dex2) | Matching, mostly documented disassemblies of the F3DEX2/F3DZEX2 N64 RSP microcode | 50 | 🟢 | C |
| [Body Harvest](https://github.com/jaytheham/body-harvest-decompilation) | Matching decompilation of Body Harvest (Nintendo 64, 1998) | 46 | 🟢 | C |
| [Rocket: Robot on Wheels](https://github.com/RocketRet/Rocket-Robot-On-Wheels) | Matching decompilation of Rocket: Robot on Wheels (Nintendo 64, 1999) | 46 | 🔴 | C |
| [Aidyn Chronicles](https://github.com/blackgamma7/Aidyn) | Matching decompilation of Aidyn Chronicles: The First Mage (Nintendo 64, 2001) | 42 | 🟢 | C++ |
| [Pokémon Puzzle League](https://github.com/AngheloAlf/puzzleleague64) | Matching decompilation of Pokémon Puzzle League (Nintendo 64, 1999) | 42 | 🟢 | C |
| [Bomberman 64](https://github.com/Bomberhackers/bm64) | Matching decompilation of Bomberman 64 (Nintendo 64, 1997) | 35 | 🟢 | C |
| [AeroGauge](https://github.com/LLONSIT/AeroGauge) | Matching decompilation of AeroGauge (Nintendo 64, 1997) | 32 | 🟢 | C |
| [F-Zero X (Expansion Kit)](https://github.com/inspectredc/fzerox-expansion-kit) | Matching decompilation of F-Zero X Expansion Kit (Nintendo 64, 2000) | 30 | 🟢 | C |
| [Conker's Bad Fur Day](https://github.com/DevOldSchool/conkers-bfd-decomp) | Matching decompilation of Conker's Bad Fur Day (Nintendo 64, 2001) | 29 | 🟢 | Python |
| [Virtual Pro Wrestling 2](https://github.com/AKI-Club/vpw2) | Matching decompilation of Virtual Pro Wrestling 2 (Nintendo 64, 2000) | 29 | 🟢 | Assembly |
| [Gauntlet Legends](https://github.com/Drahsid/gauntlet-legends) | Matching decompilation of Gauntlet Legends (Nintendo 64, 1999) | 28 | 🟢 | C |
| [Gex: Enter the Gecko (N64)](https://github.com/MatBourgon/Gex64Decomp) | Decompilation of Gex: Enter the Gecko (N64) | 28 | 🟢 | C |
| [Turok 3: Shadow of Oblivion](https://github.com/Drahsid/turok3) | Matching decompilation of Turok 3: Shadow of Oblivion (Nintendo 64, 2000) | 26 | 🗄️ | C |
| [Mario Golf (N64)](https://github.com/monde-lointain/mariogolf64) | Decompilation of Mario Golf (N64) | 24 | 🟢 | C |
| [Superman 64](https://github.com/farisawan-2000/superman) | Matching decompilation of Superman 64 (Nintendo 64, 1999) | 22 | 🔴 | Assembly |
| [Star Wars: Shadows of the Empire](https://github.com/EltaleLibrarian/SotE) | Matching decompilation of Star Wars: Shadows of the Empire (Nintendo 64, 1996) | 21 | 🟡 | C |
| [Star Wars: Rogue Squadron](https://github.com/Tmcg2/rogue_squadron64) | Matching decompilation of Star Wars: Rogue Squadron (Nintendo 64, 1998) | 20 | 🟢 | C |
| [Duke Nukem 64](https://github.com/NBlood/Duke64-RE) | Matching decompilation of Duke Nukem 64 (Nintendo 64, 1997) | 19 | 🟡 | C |
| [Beetle Adventure Racing!](https://github.com/synamaxmusic/bar-decomp) | Matching decompilation of Beetle Adventure Racing! (Nintendo 64, 1999) | 18 | 🟢 | C |
| [Quest 64](https://github.com/Rainchus/Quest64-Decomp) | Matching decompilation of Quest 64 (Nintendo 64, 1998) | 18 | 🟢 | C |
| [Bomberman 64: The Second Attack!](https://github.com/Bomberhackers/bm64tsa) | Matching decompilation of Bomberman 64: The Second Attack! (Nintendo 64, 2000) | 14 | 🟢 | C |
| [Chameleon Twist](https://github.com/chameleonTwistRet/chameleonTwistv1.0-JP) | Matching decompilation of Chameleon Twist (Nintendo 64, 1997) | 12 | 🟢 | C |
| [Glover (rainchus)](https://github.com/Rainchus/Glover) | Matching decompilation of Glover (Nintendo 64, 1998) | 12 | 🟡 | C |
| [Mario Tennis (N64)](https://github.com/DellM-79/MarioTennisN64) | Decompilation of Mario Tennis (N64) | 12 | 🟡 | C |
| [Blast Corps](https://github.com/SlaveOfIDO/blastcorps) | Matching decompilation of Blast Corps (Nintendo 64, 1997) | 11 | 🟢 | C |
| [Mystical Ninja Starring Goemon](https://github.com/klorfmorf/mnsg) | Matching decompilation of Mystical Ninja Starring Goemon (Nintendo 64, 1997) | 11 | 🟢 | C |
| [Doraemon: Nobita to Mittsu no Seireiseki](https://github.com/adipocira/doraemon1) | Matching decompilation of Doraemon: Nobita to Mittsu no Seireiseki (Nintendo 64, 1997) | 9 | 🟢 | C |
| [LEGO Racers](https://github.com/marijnvdwerf/lego-racers) | Matching decompilation of LEGO Racers (Nintendo 64, 1999) | 8 | 🟡 | Python |
| [Virtual Pool 64](https://github.com/LLONSIT/VirtualPool64) | Matching decompilation of Virtual Pool 64 (Nintendo 64, 1998) | 8 | 🔴 | Assembly |
| [Wonder Project J2](https://github.com/LLONSIT-glitch/wonder) | Matching decompilation of Wonder Project J2 (Nintendo 64, 1996) | 8 | 🟢 | C |
| [KE-NG_Reversing](https://github.com/disi33/KE-NG_Reversing) | Reverse engineering of the N64 game Knife Edge: Nose Gunner | 7 | 🔴 | Shell |
| [Shadowgate 64](https://github.com/Rainchus/ShadowGate64) | Matching decompilation of Shadowgate 64 (Nintendo 64, 1999) | 7 | 🔴 | C |
| [BodyHarvestDecomp](https://github.com/DeltaniumIndustries/BodyHarvestDecomp) | Decompilation of the N64 game Body Harvest | 6 | 🗄️ |  |
| [Chameleon Twist 2](https://github.com/chameleonTwistRet/chameleonTwist2v1.0-JP) | Matching decompilation of Chameleon Twist 2 (Nintendo 64, 1998) | 6 | 🟢 | C |
| [The New Tetris](https://github.com/KiritoDv/tnt) | Matching decompilation of The New Tetris (Nintendo 64, 1999) | 6 | 🗄️ | C |
| [BattleTanx: Global Assault](https://github.com/TheGh0stShip/BattleTanx-Global-Assault) | Matching decompilation of BattleTanx: Global Assault (Nintendo 64, 1999) | 5 | 🟢 | C |
| [Paperboy (N64)](https://github.com/marijnvdwerf/paperboy-n64) | Decompilation of Paperboy (N64) | 5 | 🟢 | C |
| [Ridge Racer 64](https://github.com/jvicu2001/rr64-decomp) | Matching decompilation of Ridge Racer 64 (Nintendo 64, 2000) | 5 | 🟡 | Linker Script |
| [Snowboard Kids (sonicdcer)](https://github.com/sonicdcer/sk) | Matching decompilation of Snowboard Kids (Nintendo 64, 1997) | 5 | 🟡 | C |
| [Dark Rift](https://github.com/Unnunu/darkrift) | Matching decompilation of Dark Rift (Nintendo 64, 1997) | 4 | 🟢 | C |
| [BattleTanx](https://github.com/AbuN64/battletanx-decomp) | Matching decompilation of BattleTanx (Nintendo 64, 1998) | 3 | 🟢 | C |
| [Onegai Monsters](https://github.com/Ryan-Myers/onegaimonsters) | Matching decompilation of Onegai Monsters (Nintendo 64, 1999) | 3 | 🟢 | C |
| [Glover](https://github.com/djsaunde/glover-decomp-1) | Matching decompilation of Glover (Nintendo 64, 1998) | 2 | 🟢 | C |
| [Hybrid Heaven](https://github.com/southcitycapture/hybridheaven-decomp) | Matching decompilation of Hybrid Heaven (Nintendo 64, 1999) | 2 | 🟢 | C |
| [Banjo-Kazooie](https://gitlab.com/banjo.decomp/banjo-kazooie) | Matching decompilation of Banjo-Kazooie (Nintendo 64, 1998) |  | ⚪ |  |
| [Donkey Kong 64](https://gitlab.com/dk64_decomp/dk64) | Matching decompilation of Donkey Kong 64 (Nintendo 64, 1999) |  | ⚪ |  |
| [GoldenEye 007](https://gitlab.com/kholdfuzion/goldeneye_src) | Matching decompilation of GoldenEye 007 (Nintendo 64, 1997) |  | ⚪ |  |
| [ogrebattle64](https://codeberg.org/hijsje/ogrebattle64) | Decompilation of Ogre Battle 64 for the Nintendo 64 |  | ⚪ |  |
| [Perfect Dark](https://gitlab.com/ryandwyer/perfect-dark) | Matching decompilation of Perfect Dark (Nintendo 64, 2000) |  | ⚪ |  |
| [Shiren the Wanderer 2](https://github.com/mschienbein/shiren2-decomp) | Matching decompilation of Shiren the Wanderer 2 (Nintendo 64, 2000) | 0 | 🟢 | C |

## Matching Decompilations — Other / Multi-platform

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Super Mario 64 decomp](https://github.com/n64decomp/sm64) | Matching decompilation of Super Mario 64 | 8,891 | 🟡 | C |
| [Ocarina of Time decomp](https://github.com/zeldaret/oot) | Decompilation of The Legend of Zelda: Ocarina of Time | 5,601 | 🟢 | C |
| [Twilight Princess decomp](https://github.com/zeldaret/tp) | Decompilation of The Legend of Zelda: Twilight Princess | 2,093 | 🟢 | C++ |
| [Majora's Mask decomp](https://github.com/zeldaret/mm) | Decompilation of The Legend of Zelda: Majora's Mask | 1,747 | 🟢 | C |
| [UnityDecompiled](https://github.com/MattRix/UnityDecompiled) | Decompiled C# source of the Unity editor and engine assemblies (now superseded by official reference source) | 1,483 | 🗄️ |  |
| [sm64-port](https://github.com/sm64-port/sm64-port) | Port of the SM64 decompilation to modern devices | 1,316 | 🟡 | C |
| [RSDKv4 Decompilation](https://github.com/RSDKModding/RSDKv4-Decompilation) | Decompilation of Sonic 1 & 2 (2013) and Retro Engine v4 | 1,148 | 🟢 | C++ |
| [Wind Waker decomp](https://github.com/zeldaret/tww) | Decompilation of The Legend of Zelda: The Wind Waker | 1,102 | 🟢 | C++ |
| [RSDKv5-Decompilation](https://github.com/RSDKModding/RSDKv5-Decompilation) | Complete decompilation of Retro Engine v5 (Sonic Mania) | 569 | 🟢 | C++ |
| [s1disasm](https://github.com/sonicretro/s1disasm) | Sonic 1 Disassembly | 453 | 🟢 | Assembly |
| [s2disasm](https://github.com/sonicretro/s2disasm) | Sonic 2 Disassembly | 318 | 🟢 | Assembly |
| [zelda1-disassembly](https://github.com/aldonunez/zelda1-disassembly) | A complete disassembly of The Legend of Zelda | 275 | 🔴 | Assembly |
| [Sonic 3/Sonic & Knuckles Disassembly](https://github.com/sonicretro/skdisasm) | Sonic and Knuckles Disassembly | 265 | 🟢 | Assembly |
| [bo1-zombies-decompiled](https://github.com/MisaDev4/bo1-zombies-decompiled) | Decompiled GSC scripts of Call of Duty: Black Ops 1 Zombies | 263 | 🟢 | C++ |
| [smb3](https://github.com/captainsouthbird/smb3) | Disassembly of Super Mario Bros 3 | 250 | 🟡 | Assembly |
| [overpy](https://github.com/Zezombye/overpy) | High-level language for the Overwatch Workshop with compile and decompile support | 238 | 🟢 | OverPy |
| [v-decompiled-scripts](https://github.com/root-cause/v-decompiled-scripts) | Decompiled GTA V game scripts | 161 | 🗄️ | C |
| [WorldOfTanks-Decompiled](https://github.com/StranikS-Scan/WorldOfTanks-Decompiled) | Unpacked and decompiled versions of xml- and pyc-files of WorldOfTanks | 149 | 🟢 | Python |
| [RSDKv4-Script-Decompilation](https://github.com/RSDKModding/RSDKv4-Script-Decompilation) | Decompiled scripts of Retro Engine v4 games (Sonic 1/2 mobile) | 140 | 🟢 |  |
| [RSDKv3-Script-Decompilation](https://github.com/RSDKModding/RSDKv3-Script-Decompilation) | Decompiled scripts of Retro Engine v3 (Sonic CD) | 139 | 🟢 |  |
| [RuneScape Classic client (2003scape rsc-c)](https://github.com/2003scape/rsc-c) | RuneScape Classic client ported to C, with builds for PC, Wii, 3DS and Switch | 136 | 🟢 | C |
| [Paleblood](https://github.com/Yharnam-Hunters/Paleblood) | Decompilation of Bloodborne v1.09 with its own runtime | 118 | 🟢 | Python |
| [FF Disassembly](https://github.com/Entroper/FF1Disassembly) | Disassembly of Final Fantasy (Assembly) | 107 | 🟢 | Assembly |
| [CircleShootApp](https://github.com/alula/CircleShootApp) | Zuma Deluxe 1.0.0 decompilation | 101 | 🟢 | C++ |
| [YandereSimulatorDecompiled](https://github.com/LordEnma/YandereSimulatorDecompiled) | Decompiled code of the game Yandere Simulator | 101 | 🟢 | C# |
| [ChoplifterReverse](https://github.com/blondie7575/ChoplifterReverse) | Full reverse engineered source of the Apple II game Choplifter | 100 | 🟡 | Assembly |
| [lode_runner_reveng](https://github.com/XekriRedmane/lode_runner_reveng) | Reverse engineering of Lode Runner for the Apple II | 97 | 🟢 | TeX |
| [Final Fantasy VI Disassembly](https://github.com/everything8215/ff6) | Disassembly and ROM info for Final Fantasy VI | 88 | 🟢 | Assembly |
| [GTA-V-Decompiled-Scripts](https://github.com/calamity-inc/GTA-V-Decompiled-Scripts) | All decompiled GTA V .ysc game scripts, including native tables | 83 | 🟢 | C |
| [PvZ-TV-Touch](https://github.com/WuDi-ZhanShen/PvZ-TV-Touch) | Decompiled Java source of Android Plants vs. Zombies TV edition, adapted for touch | 82 | 🟡 |  |
| [Pokémon Puzzle Challenge](https://github.com/pret/pokepuzzle) | Disassembly of Pokémon Puzzle Challenge | 81 | 🟢 | Assembly |
| [StardewValleyDecompiled](https://github.com/Dannode36/StardewValleyDecompiled) | Stardew Valley 1.6 decompiled to .NET 6 | 80 | 🟡 | C# |
| [jetpac-disassembly](https://github.com/mrcook/jetpac-disassembly) | Fully annotated disassembly of JETPAC (ZX Spectrum) | 77 | 🟢 | Assembly |
| [The Legend of Zelda](https://github.com/camthesaxman/zeldasource) | Disassembly of Legend of Zelda | 77 | 🔴 | Assembly |
| [gridrunner](https://github.com/mwenge/gridrunner) | Reverse-engineered source of Gridrunner (1982) by Jeff Minter | 75 | 🔴 | Assembly |
| [re47](https://github.com/0danny/re47) | Hitman: Codename 47 decompilation project (archived) | 74 | 🗄️ | C++ |
| [Terraria (Old-Gen Console)](https://github.com/PPrism/TerrariaOGC) | Functional decompilation and PC port of the Xbox 360 / PS3 version of Terraria (2013) | 67 | 🟢 | C# |
| [dx-ball](https://github.com/N0zoM1z0/dx-ball) | Source reconstruction of DX-Ball 1.07 verified against the original binary | 66 | 🟢 | Python |
| [smb-decomp](https://github.com/camthesaxman/smb-decomp) | Decompilation of Super Monkey Ball | 64 | 🔴 | Assembly |
| [bookstory-en](https://github.com/xraymemory/bookstory-en) | Decompilation and English translation of the game BookStory | 61 | 🔴 | VBA |
| [th07](https://github.com/some100/th07) | Decompilation of Touhou 7 Perfect Cherry Blossom 1.00b | 61 | 🟢 | C++ |
| [s2smsdisasm](https://github.com/sonicretro/s2smsdisasm) | Sonic 2 SMS Disassembly | 59 | 🔴 | Assembly |
| [th105](https://github.com/N0zoM1z0/th105) | Source reconstruction of Touhou Scarlet Weather Rhapsody 1.06a | 59 | 🟢 | C++ |
| [BldMystery](https://github.com/smartblade/BldMystery) | Source code recovery of Severance: Blade of Darkness | 57 | 🟢 | Assembly |
| [Guitar Hero: Warriors of Rock](https://github.com/kernaltrap8/WoR-Plus) | Quality-of-life mod for Guitar Hero: Warriors of Rock (PS3 / Xbox 360, 2010) | 57 | 🟡 | HiveQL |
| [sead](https://github.com/aboood40091/sead) | Decompilation of Nintendo EAD's sead engine library | 54 | 🟢 | C++ |
| [BounceTales](https://github.com/HelloOO7/BounceTales) | Decompilation of Rovio's Bounce Tales (2008) for Nokia phones | 53 | 🔴 | Java |
| [Thunderball](https://github.com/teampopwork/Thunderball) | Decompilation of Peggle Deluxe 1.01 | 53 | 🟢 | C++ |
| [stfdisasm](https://github.com/biggestsonicfan/stfdisasm) | Sonic the Fighters Disassembly | 49 | 🟢 | Assembly |
| [Ballanced](https://github.com/doyaGu/Ballanced) | Reversed source code of the game Ballance | 47 | 🟢 | CMake |
| [hmfomt](https://github.com/not-alons/hmfomt) | Disassembly/decompilation of Harvest Moon: Friends of Mineral Town | 47 | 🔴 | Assembly |
| [mp3](https://github.com/PartyPlanner64/mp3) | Mario Party 3 decompilation | 47 | 🗄️ | C |
| [agl](https://github.com/open-ead/agl) | Decompilation of agl, a graphics library used in first-party Nintendo games | 46 | 🟢 | C++ |
| [New Super Mario Bros. U](https://github.com/aboood40091/red-pro2) | Matching decompilation of New Super Mario Bros. U (Wii U, 2012; v1.3.0) | 45 | 🟢 | C++ |
| [Source-2-Decompiler](https://github.com/Dingf/Source-2-Decompiler) | Decompiler for Source 2 file formats | 45 | 🔴 | C++ |
| [bn6f](https://github.com/dism-exe/bn6f) | Disassembly of MegaMan Battle Network 6 Cybeast Falzar | 44 | 🟢 | Assembly |
| [Celeste_Decompiled](https://github.com/TheCyndaquilDecompilers/Celeste_Decompiled) | Decompiled source of Celeste (XNA build 1.4.0.0) | 44 | 🔴 | C# |
| [rr-decomp](https://github.com/kazuyette/rr-decomp) | Matching decompilation of Ridge Racer (PlayStation, Namco, 1994, SLPS-00001), and a static recompilation that boots a... | 43 | 🟢 | C |
| [EoSDecomp](https://github.com/wearrrrr/EoSDecomp) | Byte-accurate decompilation of Touhou 6 Embodiment of Scarlet Devil | 42 | 🟡 | C++ |
| [GD-2.206-Decompiled](https://github.com/CallocGD/GD-2.206-Decompiled) | Decompilation attempt of Geometry Dash 2.206 | 42 | 🟡 | C++ |
| [SCI-Decompilation-Archive](https://github.com/EricOakford/SCI-Decompilation-Archive) | Collection of decompiled source code for Sierra's SCI games | 42 | 🟡 | Scala |
| [byte-tactics](https://github.com/HectorBailey/byte-tactics) | Matching decompilation of Total Annihilation | 41 | 🟢 | C++ |
| [Knuckles' Chaotix Disassembly](https://github.com/sonicretro/chaotix) | Knuckles' Chaotix Disassembly & Toolkit | 41 | 🟢 | Assembly |
| [SCUMM-Decompilation-Archive](https://github.com/EricOakford/SCUMM-Decompilation-Archive) | Collection of decompiled source code for Lucasfilm's SCUMM games | 40 | 🟡 | C |
| [spindisasm](https://github.com/sonicretro/spindisasm) | Sonic Spinball Disassembly | 40 | 🔴 | Assembly |
| [deltamodkit](https://github.com/deltamodders/deltamodkit) | DELTARUNE GameMaker decompilation/port with modding support | 38 | 🟢 | Game Maker Language |
| [samp-source](https://github.com/Dryxio/samp-source) | Byte-for-byte source rebuild of SA-MP 0.3.7 R5 | 38 | 🟢 | C++ |
| [habbo_src](https://github.com/Quackster/habbo_src) | Archive of decompiled Habbo client files from 2001-2009 | 37 | 🟢 | LiveScript |
| [lm-decomp](https://github.com/ThePlayerRolo/lm-decomp) | Decompilation of Luigi's Mansion | 37 | 🗄️ | C |
| [Blood-RE](https://github.com/NBlood/Blood-RE) | Blood source code reconstruction (matching decompilation) | 35 | 🟢 | C++ |
| [Final Fantasy IV Disassembly](https://github.com/everything8215/ff4) | Final Fantasy IV Disassembly | 35 | 🔴 | Assembly |
| [PaRappaSource](https://github.com/cuckydev/PaRappaSource) | PaRappa the Rapper decompilation | 34 | 🔴 | C |
| [th04](https://github.com/N0zoM1z0/th04) | Source reconstruction of Touhou 4 Lotus Land Story | 34 | 🟢 | Python |
| [C64 Wizard of Wor Disassembly](https://github.com/dabadab/wizardofwor) | Wizard of Wor for C64 disassembly | 33 | 🔴 | Assembly |
| [decomp](https://github.com/cuellius/decomp) | Mount & Blade: Warband module decompiler | 33 | 🔴 | C# |
| [Metroid Disassembly](https://github.com/nmikstas/metroid-disassembly) | Metroid software disassembly | 33 | 🟡 | Assembly |
| [Most-Wanted-Vehicles-Decomp](https://github.com/Brawltendo/Most-Wanted-Vehicles-Decomp) | Matching decompilation of Need for Speed Most Wanted vehicle physics | 32 | 🔴 | C++ |
| [s3ddisasm](https://github.com/sonicretro/s3ddisasm) | Sonic 3D Blast Disassembly | 30 | 🔴 | Assembly |
| [SADX-cutscene-decompilation](https://github.com/X-Hax/SADX-cutscene-decompilation) | Decompilation of Sonic Adventure DX cutscenes | 30 | 🟡 | C++ |
| [Exile disassembly](https://github.com/tom-seddon/exile_disassembly) | Commented, buildable disassembly of the classic BBC Micro game | 29 | 🗄️ | TypeScript |
| [RedCarpet-S](https://github.com/fruityloops1/RedCarpet-S) | Super Mario 3D World + Bowser's Fury 1.1 decompilation | 29 | 🟡 | C++ |
| [RDR3-Decompiled-Scripts](https://github.com/kepmehz/RDR3-Decompiled-Scripts) | Red Dead Redemption 2 .ysc game scripts decompiled to C with natives and strings | 28 | 🔴 | C |
| [sbk-decomp](https://github.com/tenry92/sbk-decomp) | Snowboard Kids decompilation | 28 | 🔴 | C |
| [Pizza-Tower-EXtracted](https://github.com/setupwitch/Pizza-Tower-EXtracted) | Semi-accurate decompilation of Pizza Tower | 27 | 🟢 | Game Maker Language |
| [Thrust Disassembly](https://github.com/kieranhj/thrust-disassembly) | Reverse engineered source to BBC Thrust | 27 | 🟢 | Assembly |
| [fft_decomp](https://github.com/adamrt/fft_decomp) | Decompilation of Final Fantasy Tactics (PlayStation, NA) | 26 | 🟢 | C |
| [spyro-3](https://github.com/TheMobyCollective/spyro-3) | Spyro: Year of the Dragon decompilation project | 26 | 🟢 | Assembly |
| [Manic Miner disassembly](https://github.com/skoolkid/manicminer) | A disassembly of Manic Miner, created using SkoolKit. | 25 | 🟢 | Python |
| [th095](https://github.com/N0zoM1z0/th095) | Source reconstruction of Touhou Shoot the Bullet 1.02a | 25 | 🟢 | C++ |
| [totkol](https://github.com/jiangzhengwenjz/totkol) | Decompilation of Tactics Ogre: The Knight of Lodis (USA) | 24 | 🟡 | Assembly |
| [WinFish](https://github.com/Vindirect/WinFish) | Insaniquarium Deluxe 1.1 decompilation | 24 | 🟢 | C |
| [bomberman-64](https://github.com/MarioMaster96/bomberman-64) | Bomberman 64 decompilation | 23 | 🔴 | Assembly |
| [Burnout Paradise](https://github.com/BurnoutHints/b5-decomp) | Decompilation of Burnout Paradise | 23 | 🟡 | C++ |
| [Eushully-Decompiler](https://github.com/Kelebek1/Eushully-Decompiler) | Decompiler and recompiler for Eushully AGE engine scripts | 23 | 🟡 | C++ |
| [DiamondRushSource](https://github.com/kubikaugustyn/DiamondRushSource) | Decompilation of Gameloft's Diamond Rush (2006) for Nokia phones | 22 | 🟡 | Java |
| [gcx_decompiler](https://github.com/oct0xor/gcx_decompiler) | Decompiler for GCX/GCL scripts in Metal Gear Solid games | 22 | 🔴 | Python |
| [Ultimate Play the Game disassemblies](https://github.com/pobtastic/ultimate) | A disassembly of various "Ultimate Play the Game" games, created using SkoolKit. | 22 | 🟡 | Visual Basic 6.0 |
| [BBTools](https://github.com/JonMagon/BBTools) | Disassembly analysis and collection of tools for Beasts and Bumpkins (1997) | 21 | 🟢 | C# |
| [Cuphead-Decomp](https://github.com/tanosshi/Cuphead-Decomp) | Unofficial decompilation of Cuphead | 21 | 🟢 | C# |
| [Final Fantasy V Disassembly](https://github.com/everything8215/ff5) | Disassembly and ROM info for Final Fantasy V | 21 | 🟢 | Assembly |
| [Mario vs. Donkey Kong](https://github.com/camthesaxman/mariovsdk) | Disassembly of Mario vs. Donkey Kong | 21 | 🟡 | Assembly |
| [Sonic CD Disassembly](https://github.com/sonicretro/scddisasm) | Disassembly of Sonic CD (Assembly) | 21 | 🟢 | Assembly |
| [Cave-Story-Decompilation](https://github.com/GabrielRavier/Cave-Story-Decompilation) | Decompilation of Cave Story | 20 | 🗄️ | Assembly |
| [Jet Set Willy disassembly](https://github.com/skoolkid/jetsetwilly) | A disassembly of Jet Set Willy, created using SkoolKit. | 20 | 🟢 | Python |
| [n64dd](https://github.com/Decompollaborate/n64dd) | Decompilation of the n64dd file in Ocarina of Time | 20 | 🟡 | C |
| [Donkey-Kong-Country-2-Disassembly](https://github.com/Yoshifanatic1/Donkey-Kong-Country-2-Disassembly) | Disassembly of Donkey Kong Country 2 (Assembly) | 19 | 🔴 | Assembly |
| [Manic Miner (BBC)](https://github.com/TobyLobster/ManicMiner) | Disassembly of the original BBC Micro version of Manic Miner | 17 | 🟡 |  |
| [psychonauts-decomp](https://github.com/DrDecki/psychonauts-decomp) | Decompilation project for Psychonauts | 17 | 🟢 | C |
| [shiren](https://github.com/CelestialAmber/shiren) | Disassembly of Fushigi no Dungeon 2: Fuurai no Shiren | 16 | 🔴 | Assembly |
| [smb2j-disassembly](https://github.com/threecreepio/smb2j-disassembly) | ca65 version of doppelgangers fantastic smb2j disassembly | 16 | 🟡 | Assembly |
| [Splatoon](https://github.com/Dexx-io/Splatoon-Decomp) | Matching decompilation of Splatoon (Wii U, 2015) | 15 | 🟡 |  |
| [Pokered-Pro](https://github.com/Kamy41/Pokered-Pro) | Disassembly of Pokémon Red/Blue with some fixies and improvements (and a little surprise at Vermilion Dock if you tal... | 14 | 🟢 | Assembly |
| [raymanarenadecomp](https://github.com/zZeck/raymanarenadecomp) | Rayman Arena decompilation early WIP made possible with Frida, Ghidra, Clang tools, and brains. | 14 | 🔴 | C++ |
| [The Hobbit disassembly](https://github.com/pobtastic/hobbit) | A disassembly of The Hobbit, created using SkoolKit. | 13 | 🔴 | Visual Basic 6.0 |
| [UrnaDecomp](https://github.com/macabeus/UrnaDecomp) | Matching decompilation of the Brazilian TSE electronic voting machine simulator | 12 | 🟢 | C++ |
| [Rex disassembly](https://github.com/ultrabolido/skRex) | A disassembly of Rex, created using SkoolKit. | 11 | 🔴 | CSS |
| [The Way of the Exploding Fist disassembly](https://github.com/pobtastic/wayoftheexplodingfist) | A disassembly of The Way of the Exploding Fist, created using SkoolKit. | 11 | 🔴 | Visual Basic 6.0 |
| [Skate](https://github.com/Skate-Modding-Team/Skate-Decompilation-Project) | Decompilation of Skate | 10 | 🟢 | C++ |
| [Disassembly of Boulder Dash for the BBC Micro](https://github.com/TobyLobster/Boulderdash) | Disassembly of the game Boulderdash on the BBC Micro | 9 | 🟡 | Assembly |
| [Mortal Kombat 3D-era](https://github.com/cScarletter/MK-3D-Era-Decompilation) | Research and decompilation of Mortal Kombat: Deadly Alliance, Deception and Armageddon (multi-platform, 2002–2006) | 9 | 🟡 | C |
| [Soulcalibur II](https://github.com/Soulcalibur-II-Research-Group/scII_re) | Decompilation of Soulcalibur II | 9 | 🟢 |  |
| [chuckie](https://github.com/Ritchie333/chuckie) | Disassembly of the classic 1983 ZX Spectrum game "Chuckie Egg" | 8 | 🟡 | Visual Basic 6.0 |
| [nhl94-disassembly](https://github.com/Chaos81/nhl94-disassembly) | Attempt to reverse engineer the disassembled ROM of NHL94 using the NHL Hockey source code | 8 | 🟢 | Assembly |
| [Yoshi's Woolly World](https://github.com/Swiftshine/yww) | Matching decompilation of Yoshi's Woolly World (Wii U, 2015) | 8 | 🟡 | C++ |
| [Batty disassembly](https://github.com/pobtastic/batty) | A disassembly of Batty, created using SkoolKit. | 7 | 🟡 | Visual Basic 6.0 |
| [Kirby's Dream Land 3 Disassembly](https://github.com/Yoshifanatic1/Kirbys-Dream-Land-3-Disassembly) | Disassembly of Kirby's Dream Land 3 (Assembly) | 7 | 🔴 | Assembly |
| [The Lord of the Rings: The Return of the King](https://github.com/crimsonmagick/lotr-rotk) | Decompilation of The Lord of the Rings: The Return of the King | 7 | 🟡 |  |
| [West Bank](https://github.com/pobtastic/westbank) | A disassembly of West Bank, created using SkoolKit. | 7 | 🔴 | Visual Basic 6.0 |
| [Alphabet Park Adventure](https://github.com/unspDecomp/abcParkDecomp) | Matching decompilation of Alphabet Park Adventure (V.Smile, 2004) | 6 | 🟡 | C |
| [Back to Skool disassembly](https://github.com/skoolkid/backtoskool) | A disassembly of Back to Skool, created using SkoolKit. | 6 | 🟢 | Python |
| [Booty disassembly](https://github.com/pobtastic/booty) | A disassembly of Booty, created using SkoolKit. | 6 | 🟡 | Visual Basic 6.0 |
| [Hungry Horace disassembly](https://github.com/skoolkid/hungryhorace) | A disassembly of Hungry Horace, created using SkoolKit. | 6 | 🟢 | Shell |
| [mm4](https://github.com/captainsouthbird/mm4) | Disassembly of Mega Man 4 | 6 | 🔴 | Assembly |
| [Phantasy Star IV Disassembly](https://github.com/squidfeatures/ps4disasm) | Phantasy Star IV Disassembly | 6 | 🔴 | Assembly |
| [Skool Daze disassembly](https://github.com/skoolkid/skooldaze) | A disassembly of Skool Daze, created using SkoolKit. | 6 | 🟢 | Python |
| [Battlezone disassembly (ZX Spectrum)](https://github.com/pobtastic/battlezone) | A disassembly of Battlezone, created using SkoolKit. | 5 | 🟡 | Visual Basic 6.0 |
| [Jason's Gem disassembly](https://github.com/pobtastic/jasons-gem) | A disassembly of Jason's Gem, created using SkoolKit. | 5 | 🔴 | Visual Basic 6.0 |
| [Rampage disassembly](https://github.com/pobtastic/rampage) | A disassembly of Rampage, created using SkoolKit. | 5 | 🟡 | Visual Basic 6.0 |
| [Wheelie disassembly](https://github.com/pobtastic/wheelie) | A disassembly of Wheelie, created using SkoolKit. | 5 | 🟡 | Visual Basic 6.0 |
| [Contact Sam Cruise disassembly](https://github.com/skoolkid/contactsamcruise) | A disassembly of Contact Sam Cruise, created using SkoolKit. | 4 | 🟢 | Python |
| [Harrier Attack disassembly](https://github.com/pobtastic/harrierattack) | A disassembly of Harrier Attack, created using SkoolKit. | 4 | 🟡 | Visual Basic 6.0 |
| [Speedy Gonzales: Los Gatos Banditos Disassembly](https://github.com/Yoshifanatic1/Speedy-Gonzales-Los-Gatos-Banditos-Disassembly) | Disassembly of Speedy Gonzales: Los Gatos Bandidos (Assembly) | 4 | 🔴 | Assembly |
| [Armored Unit](https://github.com/Normmatt/unarmoredunit) | Matching decompilation of Armored Unit (WonderSwan, 2000) | 3 | 🟢 | C |
| [Fate/EXTELLA](https://github.com/bIue9076r/fate-extella-decompilation) | Decompilation of Fate/EXTELLA | 3 | 🟡 | C |
| [Mario Teaches Typing 3](https://github.com/EliasFever/MarioTeachesTyping3Decomp) | Decompilation of Mario Teaches Typing 3 | 3 | 🟢 | GDScript |
| [Phantasy Star Disassembly](https://github.com/sung3r/ps1disasm) | Phantasy Star Disassembly | 3 | 🔴 | Assembly |
| [180 disassembly](https://github.com/pobtastic/180) | A disassembly of 180, created using SkoolKit. | 2 | 🟡 | Visual Basic 6.0 |
| [Dragster-Disassembly](https://github.com/CelestialAmber/Dragster-Disassembly) | Disassembly of Dragster | 2 | 🔴 | Assembly |
| [Hollywood Poker disassembly](https://github.com/pobtastic/hollywoodpoker) | A disassembly of Hollywood Poker, created using SkoolKit. | 2 | 🟡 | Visual Basic 6.0 |
| [How to be a Complete Bastard disassembly](https://github.com/pobtastic/howtobeacompletebastard) | A disassembly of How To Be A Complete Bastard, created using SkoolKit. | 2 | 🟢 | Python |
| [Phantasy Star III Disassembly](https://github.com/brecert/ps3disasm) | Phantasy Star III Disassembly | 2 | 🔴 | Assembly |
| [Splitting Images/ Split Personalities disassembly](https://github.com/pobtastic/splittingimages) | A disassembly of Splitting Images, created using SkoolKit. | 2 | 🟡 | Visual Basic 6.0 |
| [Terminator Salvation](https://github.com/connieprice/Terminator-Salvation-Lua) | Decompilation of Terminator Salvation | 2 | 🟡 | Lua |
| [Chernobyl Neighbor: Clown Gang](https://github.com/smolkrieger/nuclear-neighbor) | Decompilation of Chernobyl Neighbor: Clown Gang | 1 | 🟡 |  |
| [Percy the Potty Pigeon disassembly](https://github.com/pobtastic/percythepottypigeon) | A disassembly of Percy The Potty Pigeon, created using SkoolKit. | 1 | 🟢 | Visual Basic 6.0 |
| [Sonic the Hedgehog (DIDJ)](https://github.com/ArchiverXP/sncdecomp) | Matching decompilation of Sonic the Hedgehog (LeapFrog Didj, 2008) | 1 | 🟡 | C++ |
| [ABM Disassembly](https://6502disassembly.com/a2-abm/ABM.html) | Disassembly of ABM (Assembly) |  | ⚪ |  |
| [Adventure Disassembly](https://www.qotile.net/minidig/disassembly/adventure.asm) | Disassembly of Adventure (Assembly) |  | ⚪ |  |
| [Air-Sea Battle Disassembly](https://www.qotile.net/minidig/disassembly/air_sea_battle.asm) | Disassembly of Air-Sea Battle (Assembly) |  | ⚪ |  |
| [Alleyway](https://github.com/CelestialAmber/alleyway) | Disassembly of Alleyway | 0 | 🔴 | Assembly |
| [Berzerk Disassembly](https://www.qotile.net/minidig/disassembly/berzerk.asm) | Disassembly of Berzerk (Assembly) |  | ⚪ |  |
| [Bomber Disassembly](https://6502disassembly.com/a2-bomber/Bomber.html) | Disassembly of Bomber (Assembly) |  | ⚪ |  |
| [Combat Disassembly](https://www.qotile.net/minidig/disassembly/dicombat.asm) | Disassembly of Combat (Assembly) |  | ⚪ |  |
| [Cosmic Ark Disassembly](https://www.qotile.net/minidig/disassembly/CosmicArk.asm) | Disassembly of Cosmic Ark (Assembly) |  | ⚪ |  |
| [CSBwin](http://www.dianneandpaul.net/CSBwin/) | Disassembly of Dungeon Master (C++) |  | ⚪ |  |
| [Disassemblies of classic BBC Micro games](https://www.level7.org.uk/miscellany) | Disassembly of Atic Atac, Boffin (Assembly) |  | ⚪ |  |
| [Donkey Kong Disassembly](https://www.qotile.net/minidig/disassembly/dk.asm) | Disassembly of Donkey Kong (Assembly) |  | ⚪ |  |
| [Exile (Enhanced version) disassembly](https://level7.org.uk/miscellany/exile-enhanced-disassembly.txt) | Disassembly of Exile (Assembly) |  | ⚪ |  |
| [GG-Notebook](https://codeberg.org/KeybadeBlox/GG-Notebook) | Reverse engineering notes for Jet Set Radio Future, companion to the JSRF decompilation |  | ⚪ |  |
| [Indy 500 Disassembly](https://www.qotile.net/minidig/disassembly/indy_500_pass_01.asm) | Disassembly of Indy 500 (Assembly) |  | ⚪ |  |
| [Jawbreaker Disassembly](https://www.qotile.net/minidig/disassembly/jaw_breaker.asm) | Disassembly of Jawbreaker (Assembly) |  | ⚪ |  |
| [Kaboom! Disassembly](https://www.qotile.net/minidig/disassembly/kaboom.asm) | Disassembly of Kaboom! (Assembly) |  | ⚪ |  |
| [m1-decomp](https://codeberg.org/marathon-speedrun-developers/m1-decomp) | Decompilation of PPC Marathon to compare Aleph One with the original Mac version |  | ⚪ |  |
| [Outlaw Disassembly](https://www.qotile.net/minidig/disassembly/outlaw.asm) | Disassembly of Outlaw (Assembly) |  | ⚪ |  |
| [Pitfall! Disassembly](https://www.qotile.net/minidig/disassembly/pitfall.asm) | Disassembly of Pitfall! (Assembly) |  | ⚪ |  |
| [Red vs. Blue Disassembly](https://www.qotile.net/minidig/disassembly/redblue.asm) | Disassembly of RealSports Football (Assembly) |  | ⚪ |  |
| [Riddle of the Sphinx Disassembly](https://www.qotile.net/minidig/disassembly/riddle-pal.asm) | Disassembly of Riddle of the Sphinx (Assembly) |  | ⚪ |  |
| [River Raid Disassembly](https://www.qotile.net/minidig/disassembly/RiverRaid.asm) | Disassembly of River Raid (Assembly) |  | ⚪ |  |
| [Space Jockey Disassembly](https://www.qotile.net/minidig/disassembly/space_jockey.asm) | Disassembly of Space Jockey (Assembly) |  | ⚪ |  |
| [spectrum-saboteur1-rev](https://gitlab.com/nzeemin/spectrum-saboteur1-rev) | Full disassembly of Saboteur for the ZX Spectrum |  | ⚪ |  |
| [Starmaster Disassembly](https://www.qotile.net/minidig/disassembly/Starmaster.asm) | Disassembly of Starmaster (Assembly) |  | ⚪ |  |
| [starquake](https://gitlab.com/reuben.scratton/starquake) | Disassembly of Starquake (1987) |  | ⚪ |  |
| [Surround Disassembly](https://www.qotile.net/minidig/disassembly/surround.asm) | Disassembly of Surround (Assembly) |  | ⚪ |  |
| [The A-Team Disassembly](https://www.qotile.net/minidig/disassembly/a-team.asm) | Disassembly of The A-Team (Assembly) |  | ⚪ |  |
| [Venture Disassembly](https://www.qotile.net/minidig/disassembly/venture.asm) | Disassembly of Venture (Assembly) |  | ⚪ |  |

## Matching Decompilations — PC / DOS / Windows

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Devilution](https://github.com/diasurgical/devilution) | Reverse-engineered Diablo 1 source reconstructed from the original binary | 9,006 | 🟡 | C++ |
| [Ship of Harkinian](https://github.com/HarbourMasters/Shipwright) | PC port of Ocarina of Time built on the OoT decompilation | 5,659 | 🟢 | C |
| [Space Cadet Pinball](https://github.com/k4zmu2a/SpaceCadetPinball) | Decompilation of 3D Pinball for Windows – Space Cadet (PC, 1995) | 4,711 | 🟡 | C++ |
| [LEGO Island](https://github.com/isledecomp/isle) | Matching decompilation of LEGO Island (PC, 1997) | 3,493 | 🟢 | C++ |
| [2 Ship 2 Harkinian](https://github.com/2ship2harkinian/2ship2harkinian) | PC port of Majora's Mask built on the MM decompilation | 2,339 | 🟢 | C |
| [SDLPoP](https://github.com/NagyD/SDLPoP) | An open-source port of Prince of Persia, based on the disassembly of the DOS version. | 1,301 | 🟢 | C |
| [gta-reversed](https://github.com/gta-reversed/gta-reversed) | Reimplementation of GTA San Andreas 1.0 US via reverse engineering | 1,082 | 🟢 | C++ |
| [Touhou (PC-98) (ReC98)](https://github.com/nmlgc/ReC98) | Decompilation of Touhou (PC-98) (ReC98) | 877 | 🟢 | Assembly |
| [Sonic Mania (RSDKModding)](https://github.com/RSDKModding/Sonic-Mania-Decompilation) | Matching decompilation of Sonic Mania and its Retro Engine (RSDKv5) (PC, 2017) | 819 | 🟢 | C |
| [Touhou 06: The Embodiment of Scarlet Devil](https://github.com/GensokyoClub/th06) | Matching decompilation of Touhou 06: The Embodiment of Scarlet Devil (PC, 2002) | 617 | 🟢 | C++ |
| [reVC](https://github.com/mrxenginner/reVC) | Reverse engineered source of GTA Vice City (reVC) | 434 | 🟢 | C++ |
| [Fallout 2 (fallout2-re)](https://github.com/alexbatalov/fallout2-re) | Reverse-engineered source of Fallout 2 (PC, 1998) | 412 | 🟡 | C |
| [reconstruction-of-zzt](https://github.com/asiekierka/reconstruction-of-zzt) | Reconstructed source code of ZZT | 385 | 🟡 | Pascal |
| [Deus Ex: Human Revolution (cdcEngine)](https://github.com/rrika/cdcEngineDXHR) | Decompilation of Deus Ex: Human Revolution and its cdcEngine (PC, 2011) | 325 | 🟢 | C++ |
| [starflight-reverse](https://github.com/s-macke/starflight-reverse) | Reverse-engineered Forth source of the 1986 DOS game Starflight | 239 | 🟢 | C |
| [re-plants-vs-zombies](https://github.com/Patoke/re-plants-vs-zombies) | Rebuild of Plants vs. Zombies GOTY functionality via reverse engineering | 237 | 🟢 | C++ |
| [Need for Speed: Most Wanted](https://github.com/dbalatoni13/nfsmw) | Matching decompilation of Need for Speed: Most Wanted (PC, 2005) | 228 | 🟢 | C++ |
| [Crimsonland](https://github.com/banteg/crimson) | Matching decompilation of Crimsonland (PC, 2003) | 189 | 🟢 | Python |
| [D2MOO](https://github.com/ThePhrozenKeep/D2MOO) | Reimplementation of Diablo II game code with patching facilities for modders | 185 | 🟢 | C++ |
| [fallout1-re](https://github.com/alexbatalov/fallout1-re) | Reverse engineered source of Fallout 1 | 179 | 🔴 | C |
| [Chronoshift](https://github.com/TheAssemblyArmada/Chronoshift) | Open source reimplementation of Red Alert in C++ | 175 | 🗄️ | C++ |
| [sci-scripts](https://github.com/sluicebox/sci-scripts) | Decompiled scripts of Sierra SCI adventure games | 154 | 🟢 | SuperCollider |
| [SA-MP](https://github.com/dashr9230/SA-MP) | Matching decompilation of San Andreas Multiplayer 0.3.7 | 148 | 🟢 | C |
| [Cosmo's Cosmic Adventure](https://github.com/smitelli/cosmore) | Matching decompilation of Cosmo's Cosmic Adventure (DOS, 1992) | 146 | 🟡 | C |
| [GD-Decompiled](https://github.com/Wyliemaster/GD-Decompiled) | Attempt to recover Geometry Dash 2.11 source through reverse engineering | 146 | 🗄️ | C++ |
| [resident-evil-pc-decomp](https://github.com/ecruells/resident-evil-pc-decomp) | Decompilation of the Resident Evil 1 PC port | 143 | 🟢 | C++ |
| [Spider-Man (2000)](https://github.com/krystalgamer/spidey-decomp) | Decompilation of the PC port of Neversoft's Spider-Man (PC, 2000) | 139 | 🟢 | C |
| [devilution](https://github.com/galaxyhaxz/devilution) | Original Devilution reverse engineered Diablo source | 131 | 🔴 | C |
| [PlantsVsZombies-decompilation](https://github.com/ruslan831/PlantsVsZombies-decompilation) | Decompilation of Plants vs. Zombies 0.9.9 | 121 | 🟢 | C |
| [Grand Theft Auto 2 (gta2_re)](https://github.com/CriminalRETeam/gta2_re) | Reimplementation of Grand Theft Auto 2 v10.5 from the PC version (PC, 1999) | 119 | 🟢 | C++ |
| [th08](https://github.com/N0zoM1z0/th08) | Source reconstruction of Touhou 8 Imperishable Night | 118 | 🟢 | C++ |
| [nfsu2-re](https://github.com/yugecin/nfsu2-re) | Reverse engineering project for Need for Speed Underground 2 | 114 | 🟡 | C |
| [RBXGSdecomp](https://github.com/RBLXDecomp/RBXGSdecomp) | Decompilation of the November 2007 Roblox client | 104 | 🟢 | C++ |
| [Black & White](https://github.com/openblack/bw1-decomp) | Matching decompilation of Black & White (PC, 2001) | 103 | 🟢 | C++ |
| [racers](https://github.com/isledecomp/racers) | Decompilation of LEGO Racers (1999) | 99 | 🟢 | C++ |
| [msgi](https://github.com/MrSapps/msgi) | Metal Gear Solid Integral PC reverse engineering | 95 | 🗄️ | C++ |
| [dangerous-dave-re](https://github.com/gmegidish/dangerous-dave-re) | Reverse engineering of Dangerous Dave in the Haunted Mansion | 90 | 🔴 | Python |
| [iwd2-re](https://github.com/alexbatalov/iwd2-re) | Reverse engineered source of Icewind Dale 2 | 89 | 🟡 | C++ |
| [OpenLRR](https://github.com/trigger-segfault/OpenLRR) | Open source reimplementation of LEGO Rock Raiders | 87 | 🟡 | C++ |
| [chocolatekeen](https://github.com/jamesfmackenzie/chocolatekeen) | Reverse engineered Commander Keen in C/C++ and SDL | 83 | 🟢 | C |
| [nolfsrc](https://github.com/nolffan/nolfsrc) | Decompiled source code of No One Lives Forever | 78 | 🟢 | C++ |
| [Star Wars Episode I: Racer](https://github.com/tim-tim707/SW_RACER_RE) | Matching decompilation of Star Wars Episode I: Racer (PC, 1999) | 76 | 🟢 | C |
| [gdp](https://github.com/camila314/gdp) | Decompilations of Geometry Dash physics functions | 73 | 🟡 | C++ |
| [ReHitman](https://github.com/ReGlacier/ReHitman) | Hitman Codename 47 reverse engineering project | 72 | 🟢 | C++ |
| [TR2X](https://github.com/LostArtefacts/TR2X) | Decompilation project for Tomb Raider II (1997) | 72 | 🗄️ | C |
| [saga](https://github.com/opensagadev/saga) | Matching decompilation of LEGO Star Wars: The Complete Saga | 70 | 🟢 | C++ |
| [SkiFree](https://github.com/yuv422/skifree_decomp) | Matching decompilation of SkiFree (PC, 1991) | 70 | 🔴 | Assembly |
| [half-life1_win32_722](https://github.com/ScriptedSnark/half-life1_win32_722) | Reverse-engineered source of Half-Life 1 Net Test 1 (build 722) | 60 | 🟢 | C |
| [Space Rangers HD: A War Apart](https://github.com/pakompom/SpaceRangersHD_decomp) | Matching decompilation of Space Rangers HD: A War Apart (PC, 2013) | 54 | 🟢 | Pascal |
| [Buckshot Roulette](https://github.com/uncreativeCultist/buckshot-decomp-public) | Decompilation of Buckshot Roulette (PC, 2023) | 52 | 🟡 | GDScript |
| [Battlefield 2](https://github.com/kiwidoggie/breadflowerdos) | Matching decompilation of Battlefield 2 and Battlefield 2142 (PC, 2005) | 45 | 🟢 | C++ |
| [FlatOut 2](https://github.com/ZackWilde27/FlatOut-2-decomp) | Decompilation of FlatOut 2 (PC, 2006) | 44 | 🟡 | C |
| [Colin McRae Rally 2.0 (CMR2Decomp)](https://github.com/CMR2Decomp/CMR2Decomp) | Matching decompilation of Colin McRae Rally 2.0 (PC, 2000) | 41 | 🟢 | HTML |
| [ShortLine (reSL)](https://github.com/konovalov-aleks/reSL) | Reversed source code of ShortLine v1.1 (DOS) | 41 | 🟢 | C++ |
| [Deltarune](https://github.com/TeamBlossomDevs/DeltaruneDecomp_beta) | Decompilation of Deltarune (PC, 2018) | 29 | 🟡 | Game Maker Language |
| [FUEL](https://github.com/widberg/FUELDecompilation) | Matching decompilation of FUEL (PC, 2009) | 28 | 🟢 | C++ |
| [Tube](https://github.com/rep-stosw/tube64) | 64-bit port of the decompiled DOS game Tube (DOS, 1994) | 26 | 🟡 | C++ |
| [Touhou 08: Imperishable Night](https://github.com/GensokyoClub/th08) | Matching decompilation of Touhou 08: Imperishable Night (PC, 2004) | 25 | 🟢 | C++ |
| [Tomb Raider: Legend (cdcEngine)](https://github.com/TheIndra55/cdcEngine) | Decompilation of Tomb Raider: Legend (PC, 2006) | 24 | 🟡 | C++ |
| [Colin McRae Rally 2.0](https://github.com/pablocpas/CMR2Decomp) | Matching decompilation of Colin McRae Rally 2.0 (PC, 2000) | 23 | 🟢 | C++ |
| [Oregon Trail II](https://github.com/katstasaph/otii) | Matching decompilation of Oregon Trail II (PC, 1995) | 22 | 🟡 | C |
| [Plants vs. Zombies](https://github.com/bluisblu/pvz) | Matching decompilation of Plants vs. Zombies (PC, 2009) | 22 | 🟢 | C |
| [Bugs Bunny: Lost in Time](https://github.com/quantumdude836/BugsDecomp) | Matching decompilation of Bugs Bunny: Lost in Time (PC, 1999) | 19 | 🟡 | C |
| [Mafia: The City of Lost Heaven](https://github.com/Marvisak/mafia-re) | Matching decompilation of Mafia: The City of Lost Heaven (PC, 2002) | 18 | 🟢 | C++ |
| [Alien vs. Predator 2](https://github.com/lemiur/AVP2-Reconstructed) | Matching decompilation of Alien vs. Predator 2 (PC, 2001) | 17 | 🟢 | C++ |
| [Bio Menace](https://github.com/lethal-guitar/BioMenaceDecomp) | Matching decompilation of Bio Menace (DOS, 1993) | 16 | 🟡 | C |
| [Space Rangers](https://github.com/pakompom/SpaceRangers1_decomp) | Matching decompilation of Space Rangers (PC, 2002) | 16 | 🟢 | Pascal |
| [Bloons TD 5](https://github.com/NKHook/BTD5-Decomp) | Matching decompilation of Bloons TD 5 (PC, 2011) | 15 | 🟡 | C++ |
| [Real War](https://github.com/Francessco121/real-war-decomp) | Matching decompilation of Real War (PC, 2001) | 15 | 🟡 | Dart |
| [FlatOut: Ultimate Carnage](https://github.com/ZackWilde27/FlatOut-UC-Decomp) | Decompilation of FlatOut: Ultimate Carnage (PC, 2008) | 14 | 🟢 | C++ |
| [Ys VI: The Ark of Napishtim](https://github.com/GrantBenR/YsViDecomp) | Ghidra decompilation of Ys VI: The Ark of Napishtim, Steam version (PC, 2003) | 13 | 🟡 |  |
| [Happy Wheels](https://github.com/Afterflash/HappyWheels) | Decompilation of Happy Wheels (Flash, 2010) | 12 | 🟡 | ActionScript |
| [LEGO Batman: The Videogame (mariopossamato)](https://github.com/mariopossamato/LEGO-Batman) | Matching decompilation of LEGO Batman: The Videogame (Mac OS X, 2008) | 12 | 🟡 |  |
| [Okami HD](https://github.com/Shintensu/OkamiHD-Decomp) | Decompilation of Okami HD (PC, 2017) | 12 | 🟡 | C++ |
| [Cuphead](https://github.com/jmxamongusmodder/cuphead-decomp) | Decompilation of Cuphead (PC, 2017) | 11 | 🟡 | GLSL |
| [Legoland](https://github.com/marijnvdwerf/legoland) | Matching decompilation of Legoland (PC, 1999) | 11 | 🟢 | C |
| [Undertale Yellow](https://github.com/burnedpopcorn/UnderTale-Yellow-Decompilation) | Decompilation of Undertale Yellow v1.2.1 (PC, 2023) | 11 | 🟡 | Game Maker Language |
| [Nocturne](https://github.com/NearlyTRex/NocturneDecomp) | Decompilation of Nocturne (PC, 1999) | 9 | 🟢 | Assembly |
| [Krush Kill 'N Destroy Xtreme](https://github.com/Wyrelade/KKND-Decomp) | Matching decompilation of Krush Kill 'N Destroy Xtreme (PC, 1997) | 8 | 🟢 | C |
| [Final Fantasy IV (3D Remake)](https://github.com/GlitchedDeveloper/Babil-Decompilation-Project) | Decompilation of Final Fantasy IV (3D Remake) Steam version (PC, 2014) | 7 | 🟡 | C++ |
| [LEGO Creator: Knights' Kingdom](https://github.com/DavidGrice/knightskingdom) | Matching decompilation of LEGO Creator: Knights' Kingdom (PC, 2000) | 7 | 🟢 | JavaScript |
| [Lemmings Paintball](https://github.com/vonhoff/lemball-decomp) | Matching decompilation of Lemmings Paintball (PC, 1996) | 7 | 🟢 | C++ |
| [Snail Mail](https://github.com/banteg/snail) | Matching decompilation of Snail Mail (PC) | 7 | 🟢 | C |
| [Thief: Deadly Shadows](https://github.com/Veradictus/Thief3-Decomp) | Matching decompilation of Thief: Deadly Shadows (PC, 2004) | 7 | 🟢 | C++ |
| [Homeworld 2](https://github.com/HaydnTrigg/Homeworld2Classic) | Matching decompilation of Homeworld 2 (PC, 2003) | 6 | 🟢 | C++ |
| [LEGO Batman: The Videogame](https://github.com/wasdhjklxyz/lbtvg) | Matching decompilation of LEGO Batman: The Videogame (PC, 2008) | 5 | 🟢 | C++ |
| [The Italian Job](https://github.com/dashr9230/Caper) | Non-matching decompilation of The Italian Job (PC, 2001) | 5 | 🟢 | C |
| [Blasterball Revolution 2](https://github.com/KoboDev/BBR2Decompile) | Decompilation of Blasterball Revolution 2 (PC) | 4 | 🟡 |  |
| [Magiczna Kula Papatki](https://github.com/regratka/mkp) | Matching decompilation of Magiczna Kula Papatki (PC) | 4 | 🟢 | C++ |
| [Sonic Generations](https://github.com/Luigi587/GenerationsDecomp) | Matching decompilation of Sonic Generations (PC, 2011) | 4 | 🟢 |  |
| [Stronghold (1993)](https://github.com/NancySadkov/dest) | Matching decompilation of AD&D Stronghold (DOS, 1993) | 4 | 🟡 | C |
| [DOMA Days](https://github.com/iestyn129/DOMADays) | Decompilation of the Ren'Py game DOMA Days by Big Blue Bubble (PC) | 3 | 🟢 | Ren'Py |
| [Ford Racing](https://github.com/dashr9230/Gt2) | Non-matching decompilation of Ford Racing (PC, 2000) | 3 | 🟢 | C |
| [Harvest: Massive Encounter](https://github.com/banteg/harvest) | Matching decompilation of Harvest: Massive Encounter (PC, 2008) | 3 | 🟢 | C++ |
| [Jazz Jackrabbit 2](https://github.com/Mustafa1177/jazzjackrabbit2-decompiled) | Ghidra decompilation project of Jazz Jackrabbit 2: The Secret Files (PC, 1998) | 3 | 🟡 |  |
| [Sonic the Hedgehog 4: Episode I (Windows Phone)](https://github.com/fr3dsp/Sonic4Ep1-Decomp) | Decompilation of Sonic the Hedgehog 4: Episode I (Windows Phone) | 3 | 🟢 | C# |
| [Summoner](https://github.com/AARosson48/SummonerDecomp) | Matching decompilation of Summoner (PC, 2000) | 3 | 🟢 | C++ |
| [Creatures 2](https://github.com/adamcolquhoun/Creatures-2-Decompilation) | Matching decompilation of Creatures 2 (PC, 1998) | 2 | 🟢 |  |
| [Granny](https://github.com/scd5dev/GrannyDecompilationLegacy) | Decompilation of Granny PC v1.2.2 (PC) | 2 | 🗄️ | C# |
| [Harry Potter and the Half-Blood Prince](https://github.com/MidacoYT/HarryPotterAndTheHalfBloodPrince-Decompilation) | Matching decompilation of Harry Potter and the Half-Blood Prince (PC, 2009) | 2 | 🟢 | C |
| [Hazard](https://github.com/EuclidVsGauss/HazardRevenge) | Matching decompilation of Hazard (PC) | 2 | 🟢 | C++ |
| [NavyField 2000](https://github.com/rbxrootx/MissionFleet) | Matching decompilation of NavyField 2000 (PC) | 2 | 🟢 | C++ |
| [Rumble Fighter](https://github.com/Primitheus/rumbledecomp) | Decompilation of Rumble Fighter (PC, 2006) | 2 | 🟡 | C++ |
| [The Journeyman Project Turbo!](https://github.com/disinvite/jman-decomp) | Matching decompilation of The Journeyman Project Turbo! (PC, 1994) | 2 | 🟢 | C++ |
| [The Oregon Trail (Windows 95)](https://github.com/emoluvjd2/oregontrail-win32-decomp) | Decompilation of The Oregon Trail (Windows 95) | 2 | 🟢 | C++ |
| [Age of Speed 2](https://github.com/Llamaware/age-of-speed2) | Decompilation of the Shockwave racing game Age of Speed 2 (Macromedia Director, PC) | 1 | 🟡 | Python |
| [Dr. Brain Action Reaction](https://github.com/SirHenricus/DrBrainActionReaction_PackageDecomp) | Decompiled assets and UnrealScript from Dr. Brain Action Reaction (PC, 1999) | 1 | 🟡 | UnrealScript |
| [On The Run 2](https://github.com/caramelcupcakes842/On-The-Run-2-Decomp) | Decompilation of Miniclip's On The Run 2 (Adobe Shockwave, PC) | 1 | 🟡 |  |
| [On The Run: The Getaway](https://github.com/caramelcupcakes842/On-The-Run-The-Getaway) | Decompilation of Miniclip's On The Run: The Getaway (Adobe Shockwave, PC) | 1 | 🟡 |  |
| [TwinBee Paradise in Donburi Shima](https://github.com/Jhuyghue/donburi-recomp) | Decompilation of TwinBee Paradise in Donburi Shima (Windows 95) | 1 | 🟢 |  |
| [blackhack](https://gitlab.com/bwrsandman/blackhack) | Launcher for and decompilation of Black & White's runblack.exe |  | ⚪ |  |
| [legord](https://codeberg.org/kant2002/legord) | Decompilation efforts for the BBS door game Legend of the Red Dragon |  | ⚪ |  |
| [On The Run Vegas](https://github.com/caramelcupcakes842/On-The-Run-Vegas-Decomp) | Decompilation of Miniclip's On The Run Vegas (Adobe Shockwave, PC) | 0 | 🟡 |  |
| [Sonic & Knuckles Collection (1997)](https://git.sr.ht/~benoitren/skccport) | Matching decompilation of Sonic & Knuckles Collection (PC, 1997) |  | ⚪ |  |
| [Sonic CD (PC / Gems Collection)](https://git.sr.ht/~benoitren/soniccddecompilation) | Decompilation of Sonic CD (PC / Gems Collection) |  | ⚪ |  |
| [ssgdecomp](https://codeberg.org/shuppy/ssgdecomp) | Decompilation of Super Solvers: Gizmos & Gadgets! (DOS) |  | ⚪ |  |

## Matching Decompilations — PSP / Vita / PS3

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Monster Hunter Portable 2nd G](https://github.com/tclamb/mhp2g-decomp) | Matching decompilation of Monster Hunter Portable 2nd G (PSP, 2008) | 32 | 🟢 | C++ |
| [Bakugan: Defenders of the Core](https://github.com/Vawlpe/BakuganDotC-decomp) | Decompilation of Bakugan: Defenders of the Core (PSP, 2010) | 10 | 🟡 | C |

## Matching Decompilations — PlayStation 1

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Castlevania: Symphony of the Night](https://github.com/Xeeynamo/sotn-decomp) | Matching decompilation of Castlevania: Symphony of the Night (PlayStation, 1997) | 1,153 | 🟢 | C |
| [Silent Hill](https://github.com/shdecompilations/silent-hill-decomp) | Matching decompilation of Silent Hill (PlayStation, 1999) | 916 | 🟢 | C |
| [Metal Gear Solid](https://github.com/FoxdieTeam/mgs_reversing) | Reimplementation of Metal Gear Solid (PlayStation, 1998) | 811 | 🟢 | C |
| [Crash Team Racing (CTR-ModSDK)](https://github.com/CTR-tools/CTR-ModSDK) | Mod SDK and decompilation of Crash Team Racing (PlayStation, 1999) | 455 | 🟢 | C |
| [Spyro the Dragon](https://github.com/TheMobyCollective/spyro-1) | Matching decompilation of Spyro the Dragon (PlayStation, 1998) | 176 | 🟢 | C |
| [Vagrant Story](https://github.com/ser-pounce/rood-reverse) | Matching decompilation of Vagrant Story (PlayStation, 2000) | 175 | 🟢 | C |
| [Final Fantasy VII](https://github.com/Xeeynamo/ff7-decomp) | Matching decompilation of Final Fantasy VII (PlayStation, 1997) | 173 | 🟢 | C |
| [PSX Doom (PSXDOOM-RE)](https://github.com/Erick194/PSXDOOM-RE) | Decompilation of PSX Doom (PSXDOOM-RE) | 163 | 🟡 | C |
| [Serial Experiments Lain](https://github.com/Y0oshi/lain-psx-decompiled) | Decompilation of Serial Experiments Lain | 129 | 🟢 | C |
| [Xenogears](https://github.com/ladysilverberg/xenogears-decomp) | Matching decompilation of Xenogears (PlayStation, 1998) | 123 | 🟢 | C |
| [Crash Bandicoot 2: Cortex Strikes Back](https://github.com/ughman/c2c) | Matching decompilation of Crash Bandicoot 2: Cortex Strikes Back (PlayStation, 1997) | 94 | 🔴 | C |
| [Legacy of Kain: Soul Reaver](https://github.com/fmil95/soul-re) | Matching decompilation of Legacy of Kain: Soul Reaver (PlayStation, 1999) | 85 | 🟢 | C |
| [mml1](https://github.com/ChrisNonyminus/mml1) | Decompilation of Mega Man Legends for PlayStation | 85 | 🔴 | C |
| [Digimon World](https://github.com/jype0/dw_decomp) | Matching decompilation of Digimon World (PlayStation, 1999) | 82 | 🟢 | C |
| [Chrono Cross](https://github.com/jdperos/chrono-cross-decomp) | Matching decompilation of Chrono Cross (PlayStation, 1999) | 75 | 🟢 | C |
| [Brave Fencer Musashi](https://github.com/Druthulu/BFM-decomp) | Matching decompilation of Brave Fencer Musashi (PlayStation, 1998) | 74 | 🟢 | C |
| [MediEvil](https://github.com/MediEvilDecompilation/medievil-decomp) | Matching decompilation of MediEvil (PlayStation, 1998) | 72 | 🟢 | C |
| [Parasite Eve II](https://github.com/GabeRealB/parasite-eve-2-decomp) | Matching decompilation of Parasite Eve II (PlayStation, 1999) | 67 | 🟢 | C |
| [Parasite Eve](https://github.com/khasinski/parasite-eve-decomp) | Matching decompilation of Parasite Eve (PlayStation, 1998) | 65 | 🟢 | C |
| [Frogger (1997)](https://github.com/HighwayFrogs/frogger-psx) | Decompilation of Frogger (1997) | 60 | 🟡 | C |
| [Final Fantasy VIII](https://github.com/roengstrom/ff8-decomp) | Matching decompilation of Final Fantasy VIII (PlayStation, 1999) | 57 | 🟢 | C |
| [Need for Speed: High Stakes](https://github.com/Caesar0007/NFSHS-PSX-decomp) | Decompilation of Need for Speed: High Stakes | 53 | 🟢 | Assembly |
| [Digimon World 3 (ddw3)](https://github.com/markisha64/ddw3) | Matching decompilation of Digimon World 3 (PlayStation, 2002) | 44 | 🟢 | Assembly |
| [ffvii](https://github.com/Drahsid/ffvii) | In-progress matching decompilation of Final Fantasy VII (PSX) | 43 | 🗄️ | C |
| [Legend of Mana](https://github.com/celophi/lom-decomp) | Matching decompilation of Legend of Mana (PlayStation, 1999) | 43 | 🟢 | C |
| [Croc: Legend of the Gobbos](https://github.com/Xeeynamo/croc) | Matching decompilation of Croc: Legend of the Gobbos (PlayStation, 1997) | 38 | 🟡 | C |
| [Mega Man X4](https://github.com/sozud/mmx4) | Matching decompilation of Mega Man X4 (PlayStation, 1997) | 35 | 🟢 | C |
| [Brightis-fan-translation](https://github.com/Dickdebonair/Brightis-fan-translation) | Decompilation and fan translation of the PSX game Brightis | 33 | 🟢 | Assembly |
| [Rage Racer](https://github.com/khasinski/rage-racer-decomp) | Matching decompilation of Rage Racer (PlayStation, 1996) | 31 | 🟢 | C |
| [Vandal Hearts](https://github.com/shao113/vh) | Matching decompilation of Vandal Hearts (PlayStation, 1996) | 31 | 🟡 | C |
| [PS1 Psy-Q SDK Libraries](https://github.com/sozud/psy-q-decomp) | Decompilation of PS1 Psy-Q SDK Libraries | 29 | 🟢 | C |
| [Tomba!](https://github.com/hansbonini/psx_tomba) | Decompilation of Tomba! | 29 | 🟢 | C |
| [Twisted Metal](https://github.com/abelbriggs1/tm1_decomp) | Matching decompilation of Twisted Metal (PlayStation, 1995) | 24 | 🟢 | C |
| [Jumping Flash!](https://github.com/NotExactlySiev/aloha) | Matching decompilation of Jumping Flash! (PlayStation, 1995) | 23 | 🟢 | Assembly |
| [dw2003recomp](https://github.com/gascarcella/dw2003recomp) | Decompilation of Digimon World 2003 (PS1, EU) with reference tests; PC port in progress | 19 | 🟢 | C |
| [LSD: Dream Emulator](https://github.com/brian-oblivion/lsddecomp) | Matching decompilation of LSD: Dream Emulator (PlayStation, 1998) | 17 | 🟢 | C |
| [Digimon World 2](https://github.com/Wyrelade/Digimon-World-2-Decomp) | Matching decompilation of Digimon World 2 (PlayStation, 2000) | 16 | 🟢 | C |
| [Lunar 2: Eternal Blue Complete](https://github.com/Zackmon/lunar2-psx-decomp) | Decompilation of Lunar 2: Eternal Blue Complete | 15 | 🔴 | C |
| [Evo's Space Adventures](https://github.com/mkst/esa) | Matching decompilation of Evo's Space Adventures (PlayStation, 1999) | 14 | 🟢 | C |
| [LSD: Dream Emulator (FirecatFG)](https://github.com/FirecatFG/lsddecomp) | Matching decompilation of LSD: Dream Emulator (PlayStation, 1998) | 14 | 🟡 | C |
| [Digimon World 3 (2003)](https://github.com/ReGame-Labs/dw3_decomp) | Matching decompilation of Digimon World 3 (PlayStation, 2002) | 13 | 🟢 | C |
| [Megami Ibunroku Persona](https://github.com/daanhenke/persona-psx) | Decompilation of Megami Ibunroku Persona | 13 | 🟢 | C |
| [Digimon World (solidheron)](https://github.com/solidheron/Digimon_World_1_decompolation) | Matching decompilation of Digimon World (PlayStation, 1999) | 11 | 🟡 | C |
| [Azure Dreams](https://github.com/forestbelton/azure) | Matching decompilation of Azure Dreams (PlayStation, 1997) | 8 | 🟡 | Python |
| [WCW/nWo Thunder](https://github.com/martinbean/thunder) | Matching decompilation of WCW/nWo Thunder (PlayStation, 1999) | 8 | 🟡 | Makefile |
| [Pop'n Music](https://github.com/Erizur/slpm86183) | Matching decompilation of Pop'n Music (PlayStation, 1999) | 7 | 🟢 | C |
| [Aironauts](https://github.com/bismurphy/Aironauts-decomp) | Matching decompilation of Aironauts (PlayStation, 1999) | 6 | 🟡 | C |
| [Armored Core](https://github.com/Wyrelade/Armored-Core-Decomp) | Matching decompilation of Armored Core (PlayStation, 1997) | 6 | 🟢 | C |
| [Tony Hawk's Pro Skater 2 (Competition Demo)](https://github.com/emoluvjd2/thps2-demo-decomp) | Matching decompilation of Tony Hawk's Pro Skater 2 (PlayStation, 2000; competition demo) | 6 | 🟢 | C++ |
| [Wild 9](https://github.com/plinkr/Wild9-Decompilation) | Matching decompilation of Wild 9 (PlayStation, 1998) | 5 | 🟢 | C |
| [Tokimeki Memorial: Forever with You](https://github.com/CosmicScribe64/tokimemo-ps1-decomp) | Decompilation of Tokimeki Memorial: Forever with You | 4 | 🟢 | C |
| [WCW Nitro](https://github.com/martinbean/nitro) | Matching decompilation of WCW Nitro (PlayStation, 1998) | 4 | 🟢 | C |
| [Bubsy 3D: Furbitten Planet](https://github.com/EiscremeWaffle/bubsy3d-decomp) | Matching decompilation of Bubsy 3D: Furbitten Planet (PlayStation, 1996) | 3 | 🟢 | C |
| [Digimon: Digital Card Battle](https://github.com/ReGame-Labs/dcb_decomp) | Matching decompilation of Digimon: Digital Card Battle (PlayStation, 2000) | 3 | 🟢 | C |
| [Digimon Rumble Arena](https://github.com/ReGame-Labs/dtbe_decomp) | Matching decompilation of Digimon Rumble Arena (PlayStation, 2001) | 2 | 🟢 | C |
| [Dino Crisis 2](https://github.com/anzaldoivan/dino-crisis-2-decomp) | Matching decompilation of Dino Crisis 2 (PlayStation, 2000) | 1 | 🟢 | Python |
| [Kaze no Notam](https://github.com/aaaaaaaaaaway/kaze-no-notam-decomp) | Matching decompilation of Kaze no Notam (PlayStation, 2001) | 1 | 🟢 | C |
| [Mega Man X6](https://github.com/anzaldoivan/mmx6) | Matching decompilation of Mega Man X6 (PlayStation, 2001) | 1 | 🟢 | C |
| [Tokimeki Memorial: Forever With You (CelestialAmber)](https://github.com/CelestialAmber/tokimemo) | Matching decompilation of Tokimeki Memorial: Forever With You (PlayStation, 1995) | 1 | 🟡 | Python |
| [Tombi!](https://github.com/afsenovilla/Tombi-Decomp) | Matching decompilation of Tombi! (PlayStation, 1997) | 1 | 🟢 | C |
| [croc_psx](https://codeberg.org/misbk/croc_psx) | Decompilation of the PSX demo of Croc: Legend of the Gobbos |  | ⚪ |  |
| [Mega Man X5](https://github.com/anzaldoivan/mmx5) | Matching decompilation of Mega Man X5 (PlayStation, 2000) | 0 | 🟢 | C |
| [Shin Megami Tensei](https://codeberg.org/chickenzes/smt-decomp) | Matching decompilation of Shin Megami Tensei (PlayStation, 2001) |  | ⚪ |  |

## Matching Decompilations — PlayStation 2

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Resident Evil – Code: Veronica X](https://github.com/AshfordFamily/recvx-decomp) | Matching decompilation of Resident Evil – Code: Veronica X (PlayStation 2, 2001) | 288 | 🟢 | C |
| [Street Fighter III: 3rd Strike](https://github.com/crowded-street/3s-decomp) | Matching decompilation of Street Fighter III: 3rd Strike (PlayStation 2, 2004) | 282 | 🟢 | C |
| [Sly Cooper and the Thievius Raccoonus](https://github.com/TheOnlyZac/sly1) | Matching decompilation of Sly Cooper and the Thievius Raccoonus (PlayStation 2, 2002) | 273 | 🟢 | C++ |
| [PaRappa the Rapper 2](https://github.com/parappadev/parappa2) | Matching decompilation of PaRappa the Rapper 2 (PlayStation 2, 2001) | 204 | 🟢 | C |
| [Silent Hill 3](https://github.com/dreamingmoths/memory-of-alessa) | Matching decompilation of Silent Hill 3 (PlayStation 2, 2003) | 150 | 🟢 | C |
| [Shadow of the Colossus](https://github.com/Fantaskink/SOTC) | Matching decompilation of Shadow of the Colossus (PlayStation 2, 2005; preview build) | 133 | 🟢 | C |
| [Fatal Frame](https://github.com/Mikompilation/Himuro) | Matching decompilation of Fatal Frame (PlayStation 2, 2001) | 129 | 🟢 | C |
| [Kingdom Hearts](https://github.com/ethteck/kh1) | Matching decompilation of Kingdom Hearts (PlayStation 2, 2002) | 110 | 🟢 | C |
| [Dark Cloud](https://github.com/TheMoonPeople/Chronicle) | Matching decompilation of Dark Cloud (PlayStation 2, 2000) | 94 | 🟢 | C++ |
| [Persona3-FES-Decompilation](https://github.com/snaku/Persona3-FES-Decompilation) | Decompilation of Shin Megami Tensei: Persona 3 FES | 68 | 🟢 | C |
| [God Hand](https://github.com/LucasPicoli/god-hand-decomp) | Matching decompilation of God Hand (PlayStation 2, 2006) | 58 | 🟢 | C |
| [Gran Turismo 4](https://github.com/gustavocanepa/gt4-decomp) | Matching decompilation of Gran Turismo 4 (PlayStation 2, 2004) | 55 | 🟢 | C |
| [Ratchet & Clank (PAL)](https://github.com/OpenRAC/rac1-decomp) | Matching decompilation of Ratchet & Clank (PlayStation 2, 2002; PAL version) | 55 | 🟢 | C |
| [Klonoa 2: Lunatea's Veil](https://github.com/entriphy/kl2_lv_decomp) | Matching decompilation of Klonoa 2: Lunatea's Veil (PlayStation 2, 2001) | 45 | 🟡 | C |
| [Ratchet & Clank (USA)](https://github.com/lombyte-project/Lombyte) | Matching decompilation of Ratchet & Clank (PlayStation 2, 2002; USA version) | 45 | 🟢 | C |
| [Monster Hunter (JP)](https://github.com/2Tie/mh1j) | Matching decompilation of Monster Hunter (PlayStation 2, 2004; Japanese version) | 43 | 🟢 | C |
| [Shin Megami Tensei: Persona 4](https://github.com/Raikaru/Persona4-Decompilation) | Matching decompilation of Shin Megami Tensei: Persona 4 (PlayStation 2, 2008) | 43 | 🟢 | C |
| [ico](https://github.com/nathanialf/ico) | Decompilation of ICO (PS2) | 40 | 🟢 | C |
| [Ico](https://github.com/RossyDoubleUnderscore/ICO-decomp) | Matching decompilation of Ico (PlayStation 2, 2001) | 33 | 🟢 | C |
| [SSX 3](https://github.com/ssxdecomp/ssx3) | Matching decompilation of SSX 3 (PlayStation 2, 2003) | 33 | 🟢 | Python |
| [Dark Cloud 2](https://github.com/TheMoonPeople/ChronicleTwo) | Matching decompilation of Dark Cloud 2 (PlayStation 2, 2002) | 31 | 🟢 | C++ |
| [Shin Megami Tensei: Digital Devil Saga](https://github.com/Megami-Decomps/dds-decomp) | Matching decompilation of Shin Megami Tensei: Digital Devil Saga (PlayStation 2, 2004) | 31 | 🟢 | C |
| [Yakuza](https://github.com/Hamzaxx370/Ogre-Decomp) | Matching decompilation of Yakuza (PlayStation 2, 2005) | 31 | 🟢 | C++ |
| [Ratchet & Clank: Up Your Arsenal](https://github.com/OpenRAC/rac3-uya-decomp) | Matching decompilation of Ratchet & Clank: Up Your Arsenal (PlayStation 2, 2004) | 28 | 🟢 | C |
| [REOF2](https://github.com/caprado/REOF2) | Resident Evil Outbreak File #2 (PS2) decompilation and preservation project | 27 | 🟢 | C |
| [BT3-Decompiled](https://github.com/z3xox/BT3-Decompiled) | Matching decompilation of Dragon Ball Z: Budokai Tenkaichi 3 (PS2) | 25 | 🟢 | C |
| [Twisted Metal: Black](https://github.com/abelbriggs1/tmb_decomp) | Matching decompilation of Twisted Metal: Black (PlayStation 2, 2001) | 21 | 🟢 | C |
| [SNESstation-Decomp](https://github.com/ReyFxck/SNESstation-Decomp) | Decompilation of the SNESStation PS2 emulator based on SNES9X 1.41 | 19 | 🟢 | Python |
| [Twisted Metal: Harbor City](https://github.com/jacobleeharris/tmhc) | Matching decompilation of Twisted Metal: Harbor City (PlayStation 2, unreleased) | 19 | 🟢 | C |
| [Resident Evil: Dead Aim](https://github.com/cakehonolulu/Bullseye) | Matching decompilation of Resident Evil: Dead Aim (PlayStation 2, 2003) | 18 | 🟢 | C++ |
| [SSX](https://github.com/ssxdecomp/ssx) | Matching decompilation of SSX (PlayStation 2, 2000) | 18 | 🟢 | Python |
| [Silent Hill 2](https://github.com/dreamingmoths/mirror-of-alessa) | Matching decompilation of Silent Hill 2 (PlayStation 2, 2001) | 17 | 🟢 |  |
| [Xenosaga Episode I (squareman)](https://github.com/SquareMan/xenosaga) | Matching decompilation of Xenosaga Episode I (PlayStation 2, 2002) | 17 | 🟡 | C |
| [Crash Bandicoot: The Wrath of Cortex (PS2)](https://github.com/denzi-gh/crashwoc-decomp-ps2) | Decompilation of Crash Bandicoot: The Wrath of Cortex (PS2) | 16 | 🟢 | C |
| [Ratchet: Deadlocked](https://github.com/OpenRAC/rac-deadlocked-decomp) | Matching decompilation of Ratchet: Deadlocked (PlayStation 2, 2005) | 16 | 🟢 | C |
| [Crash Bandicoot: The Wrath of Cortex (crash-ps2)](https://github.com/calmsacibis995/crash-ps2) | Decompilation of Crash Bandicoot: The Wrath of Cortex (crash-ps2) | 14 | 🟡 | C |
| [Dog's Life](https://github.com/IWILLCRAFT-M0d/dogcomp) | Matching decompilation of Dog's Life (PlayStation 2, 2003) | 14 | 🟢 | C++ |
| [Marvel vs. Capcom 2 (PS2)](https://github.com/g-guthrie/mvc2-ps2-decomp) | Decompilation of Marvel vs. Capcom 2 (PS2) | 14 | 🟢 | C |
| [Star Ocean: Till the End of Time](https://github.com/celophi/so3-decomp) | Matching decompilation of Star Ocean: Till the End of Time (PlayStation 2, 2003) | 14 | 🟢 | C++ |
| [Xenosaga Episode I](https://github.com/OpokXeno/xsg-i-decomp) | Matching decompilation of Xenosaga Episode I (PlayStation 2, 2002) | 14 | 🟢 | Java |
| [OpenHuey](https://github.com/ArnautDaniel/OpenHuey) | Haunting Ground (PS2) decompilation, PC port and actor-based rewrite | 12 | 🟢 | C |
| [Guilty Gear X Plus](https://github.com/WistfulHopes/ggx) | Matching decompilation of Guilty Gear X Plus (PlayStation 2, 2001; Korean version) | 11 | 🟡 | Python |
| [Ratchet & Clank PS2 quadrilogy (Pyrocitor)](https://github.com/VELD-Dev/Pyrocitor) | Decompilation of Ratchet & Clank PS2 quadrilogy (Pyrocitor) | 11 | 🗄️ | C++ |
| [SSX Tricky](https://github.com/ssxdecomp/ssxtricky) | Matching decompilation of SSX Tricky (PlayStation 2, 2001) | 10 | 🟢 | Python |
| [Shaun Palmer's Pro Snowboarder](https://github.com/Daniel-McCarthy/SPPS) | Matching decompilation of Shaun Palmer's Pro Snowboarder (PlayStation 2, 2001) | 7 | 🟢 | C |
| [Sonic Riders: Zero Gravity (PS2 prototype)](https://github.com/KidWizardOfTheWeb/SR2) | Decompilation of Sonic Riders: Zero Gravity (PS2 prototype) | 7 | 🟢 | C++ |
| [Amplitude](https://github.com/ieee802dot11ac/amp) | Matching decompilation of Amplitude (PlayStation 2, 2003) | 5 | 🟡 | Python |
| [Phantasy Star II Disassembly](https://github.com/jon13doe/SEGA_ps2_disasm) | Phantasy Star II Disassembly | 5 | 🔴 | Assembly |
| [Drakan: The Ancients' Gates](https://github.com/cScarletter/Drakan-The-Ancient-Gates-Decompilation-) | Matching decompilation of Drakan: The Ancients' Gates (PlayStation 2, 2002) | 4 | 🟡 |  |
| [Syphon Filter: The Omega Strain](https://github.com/zm2283145/syphon-filter-omega-strain-decomp) | Matching decompilation of Syphon Filter: The Omega Strain (PlayStation 2, 2004) | 4 | 🟢 | C |
| [Tourist Trophy](https://github.com/gustavocanepa/tt-decomp) | Matching decompilation of Tourist Trophy (PlayStation 2, 2006) | 3 | 🟢 | C |
| [Treasure Planet](https://github.com/Colt-Zero/Thousand-Worlds) | Asset and level editor for Disney's Treasure Planet (PlayStation 2, 2002) | 3 | 🟡 | Python |
| [Are You Smarter Than a 5th Grader: Make the Grade](https://github.com/Gmon20/makethedecomp) | Matching decompilation of Are You Smarter Than a 5th Grader: Make the Grade (PlayStation 2, 2009) | 2 | 🟡 | C |
| [Chulip](https://github.com/aaaaaaaaaaway/chulip-decomp) | Matching decompilation of Chulip (PlayStation 2, 2002) | 2 | 🟢 | C |
| [PS2 OSDSYS (system menu)](https://github.com/JeanxPereira/CrystalOSD) | Decompilation of PS2 OSDSYS (system menu) | 2 | 🟢 | JavaScript |
| [Stretch Panic](https://github.com/Harskov/stretch-panic-usa) | Matching decompilation of Stretch Panic (PlayStation 2, 2001) | 2 | 🟢 | C |
| [Ar tonelico II: Melody of Metafalica](https://github.com/USED255/artonelico2-decomp) | Matching decompilation of Ar tonelico II: Melody of Metafalica (PlayStation 2, 2007) | 1 | 🟢 | C |
| [George of the Jungle and the Search for the Secret](https://github.com/2gifts/george-decomp) | Matching decompilation of George of the Jungle and the Search for the Secret (PlayStation 2, 2008) | 1 | 🟢 | C |
| [Shadow Hearts](https://git.sr.ht/~benoitren/shadowheartsdecompilation) | Matching decompilation of Shadow Hearts (PlayStation 2, 2001) |  | ⚪ |  |
| [ts-ps2-decomp](https://codeberg.org/OpenMonkey/ts-ps2-decomp) | Decompilation of TimeSplitters 1 and 2 (PS2), part of the OpenMonkey project |  | ⚪ |  |

## Matching Decompilations — SNES / NES

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Battle City (NES disassembly)](https://github.com/cyneprepou4uk/NES-Games-Disassembly) | Disassembly / decompilation of Battle City (NES disassembly) | 298 | 🟢 | Assembly |
| [Contra (NES)](https://github.com/vermiceli/nes-contra-us) | Decompilation of Contra (NES) | 232 | 🟢 | Assembly |
| [EarthBound](https://github.com/Herringway/ebsrc) | Source code recreation of EarthBound (SNES, 1994) | 185 | 🟢 | Assembly |
| [Super Mario World 2: Yoshi's Island (SNES) Disassembly](https://github.com/brunovalads/yoshisisland-disassembly) | Full disassembly of Yoshi's Island (SNES) version U 1.0 | 162 | 🟢 | Assembly |
| [supermetroid](https://github.com/strager/supermetroid) | Super Metroid SNES disassembly | 160 | 🔴 | Assembly |
| [superbomberman](https://github.com/LIJI32/superbomberman) | Disassembly and remade build system for SNES game Super Bomberman | 110 | 🟢 | Assembly |
| [TetrisNESDisasm](https://github.com/CelestialAmber/TetrisNESDisasm) | Disassembly of Tetris (NES) | 109 | 🟡 | Assembly |
| [smb2](https://github.com/Xkeeper0/smb2) | Super Mario Bros. 2 (NES) disassembly | 102 | 🔴 | Assembly |
| [dragon-warrior-disassembly](https://github.com/nmikstas/dragon-warrior-disassembly) | NES Dragon Warrior software disassembly | 88 | 🔴 | Assembly |
| [Donkey Kong Country 2](https://github.com/p4plus2/DKC2-disassembly) | Disassembly of Donkey Kong Country 2 (SNES, 1995) | 76 | 🟡 | Assembly |
| [Tecmo_Super_Bowl_NES_Disassembly](https://github.com/bruddog/Tecmo_Super_Bowl_NES_Disassembly) | Rebuildable 6502 disassembly of Tecmo Super Bowl (NES) | 63 | 🟡 | Assembly |
| [Mega Man 3 (NES) Disassembly](https://github.com/refreshing-lemonade/megaman3-disassembly) | Full disassembly of Mega Man 3 (NES) | 52 | 🔴 | Assembly |
| [mike-tysons-punch-out-disassembly](https://github.com/nmikstas/mike-tysons-punch-out-disassembly) | Reverse engineering effort of the NES game Mike Tyson's Punch-Out. | 46 | 🔴 | Assembly |
| [Balloon Fight](https://github.com/LuigiBlood/balloonfight_dis) | Disassembly of Balloon Fight (NES, 1984) | 44 | 🔴 | Assembly |
| [Mega Man 5 (NES) Disassembly](https://github.com/refreshing-lemonade/megaman5-disassembly) | Full disassembly of Mega Man 5 (NES) | 34 | 🟡 | Assembly |
| [SMAS-Disassembly](https://github.com/Maseya/SMAS-Disassembly) | Disassembly of the Super Mario All-Stars SNES ROM | 32 | 🔴 | Assembly |
| [Donkey Kong Country](https://github.com/Yoshifanatic1/Donkey-Kong-Country-1-Disassembly) | Disassembly of Donkey Kong Country (SNES, 1994) | 30 | 🔴 | Assembly |
| [Donkey Kong (NES)](https://github.com/RussianManSMWC/Donkey-Kong-NES-Disassembly) | Disassembly / decompilation of Donkey Kong (NES) | 29 | 🟡 | Assembly |
| [Mega Man 4 (NES) Disassembly](https://github.com/refreshing-lemonade/megaman4-disassembly) | Full disassembly of Mega Man 4 (NES) | 29 | 🔴 | Assembly |
| [smb-disassembly](https://github.com/threecreepio/smb-disassembly) | ca65 disassembly of Super Mario Bros. for the NES | 27 | 🔴 | Assembly |
| [Super C / Probotector (NES)](https://github.com/vermiceli/nes-super-c) | Decompilation of Super C / Probotector (NES) | 27 | 🟢 | Assembly |
| [ff3](https://github.com/everything8215/ff3) | Disassembly and ROM info for Final Fantasy III (NES) | 24 | 🔴 | Assembly |
| [Dr. Mario (NES)](https://github.com/Nostaljipi/dr-mario-disassembly) | Disassembly / decompilation of Dr. Mario (NES) | 22 | 🔴 | Assembly |
| [ff2](https://github.com/everything8215/ff2) | Disassembly and ROM Info for Final Fantasy II (NES) | 22 | 🔴 | Assembly |
| [Donkey Kong Country 3](https://github.com/Yoshifanatic1/Donkey-Kong-Country-3-Disassembly) | Disassembly of Donkey Kong Country 3 (SNES, 1996) | 21 | 🔴 | Assembly |
| [Ghosts and Graves](https://github.com/AnthonyBongers/GhostsAndGraves) | Ghosts and Graves, a Tents and Trees demake written in 6502 assembly (NES homebrew) | 21 | 🟢 | Assembly |
| [Mega Man 6 (NES) Disassembly](https://github.com/refreshing-lemonade/megaman6-disassembly) | Full disassembly of Mega Man 6 (NES) | 20 | 🔴 | Assembly |
| [Donald Land](https://github.com/brunovalads/donald-land) | Disassembly of Donald Land (NES, 1988) | 16 | 🔴 | Assembly |
| [crystalisdisassembly](https://github.com/crystalisdisassembly/crystalisdisassembly) | Disassembly of the NES Game Crystalis | 14 | 🔴 | Assembly |
| [English Translation of Captain Tsubasa 2](https://github.com/cyneprepou4uk/Captain-Tsubasa-2-English-Translation) | Captain Tsubasa 2 [NES] disassembly | 14 | 🟢 | Assembly |
| [Battle City](https://github.com/vgrichina/battlecity) | Disassembly of Battle City (NES, 1985) | 11 | 🟢 | JavaScript |
| [EarthBound Beginnings](https://github.com/GrasonHumphrey/Earthbound-Zero-Decomp) | Ghidra decompilation of EarthBound Beginnings / Mother (NES, 1989) | 8 | 🟡 | HTML |
| [Ultima 3 Disassembly](https://github.com/nmikstas/nes_ultima_3_disassembly) | Disassembly of the nes version of Ultima Exodus | 7 | 🔴 | Assembly |
| [Ms. Pac-Man NES Tengen Disassembly](https://github.com/RussianManSMWC/Ms.-Pac-Man-NES-Tengen-Disassembly) | A disassembly of Ms. Pac-Man for NES, Tengen version. | 6 | 🟢 | Assembly |
| [SimCity (SNES) Disassembly](https://github.com/Yoshifanatic1/SimCity-SNES-Disassembly) | Disassembly of SimCity (Assembly) | 6 | 🔴 | Assembly |
| [Ms. Pac-Man (SNES) Disassembly](https://github.com/Yoshifanatic1/Ms-Pac-Man-SNES-Disassembly) | Disassembly of Ms. Pac-Man (Assembly) | 5 | 🔴 | Assembly |
| [Duck Hunt Disassembly](https://github.com/RussianManSMWC/Duck-ssembly-Hunt) | A disassembly of Duck Hunt for the NES. | 3 | 🟡 | Assembly |
| [Ms. Pac-Man NES Namco Disassembly](https://github.com/RussianManSMWC/Ms.-Pac-Man-NES-Namco-Disassembly) | A disassembly of Ms. Pac-Man for NES, Namco/Now Production version. | 3 | 🟡 | Assembly |
| [Spider-Man & the X-Men in Arcade's Revenge (SNES) Disassembly](https://github.com/Yoshifanatic1/Spider-Man-X-Men-Arcades-Revenge-SNES-Disassembly) | Disassembly of Spider-Man and the X-Men in Arcade's Revenge (Assembly) | 2 | 🔴 | Assembly |
| [Super Mario Brothers High Level Disassembly](https://github.com/NexusEast/Console_Development) | My attempt to develop every single console i can | 2 | 🔴 | Assembly |
| [doki](https://gitlab.com/segaloco/doki) | Comprehensive disassembly of Yume Kojo: Doki Doki Panic (Famicom Disk System) |  | ⚪ |  |
| [dq1disasm](https://gitlab.com/segaloco/dq1disasm) | Comprehensive disassembly of Dragon Quest 1 for the Famicom |  | ⚪ |  |
| [fc_dk](https://gitlab.com/segaloco/fc_dk) | Comprehensive disassembly of Donkey Kong for the Famicom |  | ⚪ |  |
| [fdsboot](https://gitlab.com/segaloco/fdsboot) | 6502 disassembly of the Famicom Disk System boot ROM |  | ⚪ |  |
| [smb](https://gitlab.com/segaloco/smb) | Disassembly combining multiple 8-bit versions of Super Mario Bros. |  | ⚪ |  |
| [smb3](https://gitlab.com/segaloco/smb3) | Disassembly of Super Mario Bros. 3 for the Famicom/NES |  | ⚪ |  |
| [zel2](https://gitlab.com/segaloco/zel2) | Disassembly of Zelda II: The Adventure of Link |  | ⚪ |  |

## Matching Decompilations — Sega

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Resident Evil – Code: Veronica (Dreamcast)](https://github.com/fmil95/recv-dc-decomp) | Decompilation of Resident Evil – Code: Veronica (Dreamcast) | 39 | 🟢 | C |
| [Neon Genesis Evangelion 64](https://github.com/farisawan-2000/evangelion) | Decompilation of Neon Genesis Evangelion 64 | 38 | 🟡 | C |
| [Tokyo Bus Guide](https://github.com/lhsazevedo/tbg-decomp) | Matching decompilation of Tokyo Bus Guide (Dreamcast, 1999) | 36 | 🟢 | PHP |
| [Flicky-Disassembly](https://github.com/Dandaman955/Flicky-Disassembly) | Disassembly of Flicky on the Mega Drive. | 7 | 🔴 | Assembly |
| [dataeast_snddrv](https://codeberg.org/techmetx11/dataeast_snddrv) | Reverse-engineered source of Data East's Sega Mega Drive sound driver |  | ⚪ |  |
| [Golden-Axe-2-Disassembly](https://gitlab.com/paulmcquad/Golden-Axe-2-Disassembly) | Disassembly of Golden Axe II for the Mega Drive |  | ⚪ |  |
| [scd-disasm](https://gitlab.com/segaloco/scd-disasm) | Disassembly of Sonic CD for the Sega Mega CD |  | ⚪ |  |

## Matching Decompilations — Switch

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Breath of the Wild decomp](https://github.com/zeldaret/botw) | Decompilation of The Legend of Zelda: Breath of the Wild (Switch 1.5.0) | 2,262 | 🟢 | C++ |
| [Minecraft: Nintendo Switch Edition](https://github.com/GRAnimated/MinecraftLCE) | Decompilation of Minecraft: Nintendo Switch Edition | 622 | 🟢 | C++ |
| [Super Mario Odyssey](https://github.com/MonsterDruide1/OdysseyDecomp) | Matching decompilation of Super Mario Odyssey (Switch, 2017) | 472 | 🟢 | C++ |
| [sead](https://github.com/open-ead/sead) | Decompilation of sead, Nintendo's first-party C++ standard library | 253 | 🟢 | C++ |
| [LEGO City Undercover](https://github.com/Nintendocustom/Lego-City-Undercover-Decompilation) | Matching decompilation of LEGO City Undercover (Switch, 2017) | 29 | 🟢 | C++ |
| [Super Mario 3D World + Bowser's Fury](https://github.com/shibbo/3DWDecomp) | Matching decompilation of Super Mario 3D World + Bowser's Fury (Switch, 2021) | 24 | 🟢 | C++ |
| [cttt-decomp](https://github.com/shibbo/cttt-decomp) | Decompilation of Captain Toad: Treasure Tracker (Switch, v1.3.0) | 20 | 🔴 | C++ |
| [Pokémon Sword](https://github.com/charlieduzstuf/pokesword) | Matching decompilation of Pokémon Sword (Switch, 2019) | 10 | 🟢 | C |
| [The Legend of Zelda: Link's Awakening (Switch)](https://github.com/Owen-Splat/las-decomp) | Decompilation of The Legend of Zelda: Link's Awakening (Switch) | 10 | 🟢 |  |

## Matching Decompilations — Xbox

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Halo CE decomp](https://github.com/halo-re/halo) | Halo: Combat Evolved (Xbox) decompilation research project | 452 | 🔴 | C |
| [Halo: Combat Evolved (Xbox)](https://github.com/punpckhdq/halo) | Decompilation of Halo: Combat Evolved (Xbox) | 194 | 🟢 | C |
| [Undertale (Xbox One)](https://github.com/kittibyte/UndertaleDecomp) | Decompilation of Undertale (Xbox One) | 127 | 🟡 | Game Maker Language |
| [halo2-decompiled](https://github.com/kirklandsig/halo2-decompiled) | Matching decompilation of Halo 2 for the original Xbox | 78 | 🟢 | C++ |
| [Halo: Reach](https://github.com/ChimpsAtSea/Reach) | Matching decompilation of Halo: Reach (Xbox 360, 2010) | 72 | 🟢 | C++ |
| [Minecraft: Xbox 360 Edition](https://github.com/LCERD/Minecraft-Xbox-360-Decompilation) | Decompilation of Minecraft: Xbox 360 Edition | 69 | 🟡 | C++ |
| [Dance Central 3](https://github.com/rjkiv/dc3-decomp) | Matching decompilation of Dance Central 3 (Xbox 360, 2012) | 43 | 🟢 | C++ |
| [TerrariaXDK](https://github.com/dptug/TerrariaXDK) | Decompiled Terraria Xbox 360 Edition source code | 35 | 🟢 | C# |
| [Fallout: New Vegas](https://github.com/ieee802dot11ac/fnv) | Matching decompilation of Fallout: New Vegas (Xbox 360, 2010) | 34 | 🟢 | C++ |
| [halocea](https://github.com/surreptitiousresearch/halocea) | Decompiled source of Halo: Combat Evolved Anniversary (Xbox 360) | 33 | 🟢 | C |
| [Xbox 360 Kernel](https://github.com/AleBello7276/xkrnl-decomp) | Decompilation of Xbox 360 Kernel | 24 | 🟢 | Python |
| [Banjo-Kazooie (Xbox 360)](https://github.com/banjo360/bk360) | Decompilation of Banjo-Kazooie (Xbox 360) | 22 | 🟢 | C |
| [Sonic the Hedgehog (2006)](https://github.com/rjkiv/sonic06) | Matching decompilation of Sonic the Hedgehog (Xbox 360, 2006) | 15 | 🟢 | C |
| [Kinect Sports](https://github.com/SebaaMG/Kinect-Sports-Decomp) | Matching decompilation of Kinect Sports (Xbox 360, 2010) | 5 | 🟢 | C |
| [Jet Set Radio Future](https://codeberg.org/KeybadeBlox/JSRF-Decompilation) | Matching decompilation of Jet Set Radio Future (Xbox, 2002) |  | ⚪ |  |
| [saints-row-1-decomp](https://gitlab.com/HttpAnimations/saints-row-1-decomp) | Matching decompilation of Saints Row (Xbox 360) |  | ⚪ |  |
| [XDemos-Decomp](https://codeberg.org/KeybadeBlox/XDemos-Decomp) | Decompilation of the original Xbox demo disc launcher |  | ⚪ |  |

## Mod Loaders & Script Extenders

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [BepInEx](https://github.com/BepInEx/BepInEx) | Plugin/modding framework for Unity Mono, IL2CPP and XNA games | 8,861 | 🟢 | C# |
| [Harmony](https://github.com/pardeike/Harmony) | Library for patching and decorating .NET/Mono methods at runtime, widely used for game mods | 6,694 | 🟢 | C# |
| [tModLoader](https://github.com/tModLoader/tModLoader) | Mod loader and API for Terraria | 5,737 | 🟢 | C# |
| [REFramework](https://github.com/praydog/REFramework) | Mod loader, scripting platform and VR support for Capcom RE Engine games | 5,652 | 🟢 | C++ |
| [Cyber Engine Tweaks](https://github.com/maximegmd/CyberEngineTweaks) | Cyberpunk 2077 scripting framework and fixes | 4,808 | 🟢 | C++ |
| [UEVR](https://github.com/praydog/UEVR) | Universal VR mod injector for Unreal Engine 4.8-5.x games | 4,629 | 🟢 | C++ |
| [FiveM / Cfx.re](https://github.com/citizenfx/fivem) | Multiplayer modification frameworks for GTA V (FiveM) and RDR2 (RedM) | 4,290 | 🟢 | C++ |
| [MelonLoader](https://github.com/LavaGang/MelonLoader) | Universal mod loader for Unity games (Il2Cpp and Mono) | 4,270 | 🟢 | C# |
| [cnc-ddraw](https://github.com/FunkyFr3sh/cnc-ddraw) | DirectDraw reimplementation fixing old games such as Command & Conquer on modern systems | 3,535 | 🟢 | C |
| [Widescreen Fixes Pack](https://github.com/ThirteenAG/WidescreenFixesPack) | Plugins adding or fixing widescreen support and bugs in many PC games | 3,248 | 🟢 | C++ |
| [UnityExplorer](https://github.com/sinai-dev/UnityExplorer) | In-game UI for exploring and modifying IL2CPP and Mono Unity games | 3,150 | 🗄️ | C# |
| [RE-UE4SS](https://github.com/UE4SS-RE/RE-UE4SS) | Injectable Lua scripting, SDK generator and live property editor for UE4/UE5 games | 3,022 | 🟢 | C++ |
| [TShock](https://github.com/Pryaxis/TShock) | Terraria server modification and plugin API | 2,899 | 🟢 | C# |
| [SMAPI](https://github.com/Pathoschild/SMAPI) | Modding API and loader for Stardew Valley | 2,763 | 🟢 | C# |
| [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader) | Proxy DLL that loads custom .asi plugins into any game process | 2,351 | 🟢 | C++ |
| [Multi Theft Auto](https://github.com/multitheftauto/mtasa-blue) | Multiplayer engine for GTA: San Andreas | 1,875 | 🟢 | C++ |
| [BWAPI](https://github.com/bwapi/bwapi) | Brood War API for writing StarCraft: Brood War AI bots | 1,712 | 🟢 | C++ |
| [LeviLamina](https://github.com/LiteLDev/LeviLamina) | Mod loader for Minecraft Bedrock Edition dedicated server | 1,695 | 🟢 | C++ |
| [Dalamud](https://github.com/goatcorp/Dalamud) | Plugin framework and API for Final Fantasy XIV | 1,644 | 🟢 | C |
| [MCP-Reborn](https://github.com/Hexeption/MCP-Reborn) | Modern Mod Coder Pack for decompiling and modding Minecraft Java | 1,566 | 🟢 |  |
| [BG3SE](https://github.com/Norbyte/bg3se) | Baldur's Gate 3 Script Extender | 1,526 | 🟢 | C++ |
| [CounterStrikeSharp](https://github.com/roflmuffin/CounterStrikeSharp) | C# server plugin framework for Counter-Strike 2 built on reverse engineered Source 2 internals | 1,373 | 🟢 | C# |
| [Yarn](https://github.com/FabricMC/yarn) | Open Minecraft deobfuscation mappings for modding | 1,228 | 🟢 | Java |
| [TiltedEvolution](https://github.com/tiltedphoques/TiltedEvolution) | Skyrim Together multiplayer mod built on reverse engineered engine internals | 1,188 | 🟢 | C++ |
| [ModEngine2](https://github.com/soulsmods/ModEngine2) | Runtime injection library for modding FromSoftware Souls games | 1,143 | 🗄️ | C++ |
| [RuntimeUnityEditor](https://github.com/ManlyMarco/RuntimeUnityEditor) | In-game inspector and debugging tools for Unity games | 1,124 | 🟢 | C# |
| [Reloaded-II](https://github.com/Reloaded-Project/Reloaded-II) | Universal .NET-powered modding framework for native x86/x64 games | 1,048 | 🟢 | C# |
| [Steamodded](https://github.com/Steamodded/smods) | Mod loader for Balatro | 991 | 🟢 | Lua |
| [xNVSE](https://github.com/xNVSE/NVSE) | New Vegas Script Extender | 851 | 🟢 | C++ |
| [Penumbra](https://github.com/xivdev/Penumbra) | Runtime mod loader for Final Fantasy XIV | 791 | 🟢 | C# |
| [Pengu Loader](https://github.com/PenguLoader/PenguLoader) | JavaScript plugin loader for the League of Legends client | 743 | 🟢 | C++ |
| [Godot Mod Loader](https://github.com/GodotModding/godot-mod-loader) | Generic mod loader for Godot games | 684 | 🟢 | GDScript |
| [plugin-sdk](https://github.com/DK22Pac/plugin-sdk) | SDK for ASI/CLEO plugins for GTA III, Vice City and San Andreas | 668 | 🟢 | C |
| [open.mp](https://github.com/openmultiplayer/open.mp) | Multiplayer mod for GTA San Andreas, backwards compatible with SA-MP | 655 | 🟢 | C++ |
| [me3](https://github.com/garyttierney/me3) | Mod Engine 3, a framework for modding and instrumenting FromSoftware games | 651 | 🟢 | Rust |
| [Lovely](https://github.com/ethangreen-dev/lovely-injector) | Runtime Lua injector for LOVE2D games such as Balatro | 612 | 🟢 | Rust |
| [Unity Mod Manager](https://github.com/newman55/unity-mod-manager) | Mod manager and loader for Unity games | 549 | 🟢 | C# |
| [FFNx](https://github.com/julianxhokaxhiu/FFNx) | Next-generation modding platform and driver for Final Fantasy VII and VIII PC | 523 | 🟢 | C++ |
| [ModTheSpire](https://github.com/kiooeht/ModTheSpire) | External mod loader for Slay the Spire | 519 | 🟡 | Java |
| [Everest](https://github.com/EverestAPI/Everest) | Celeste mod loader and mod API | 518 | 🟢 | C# |
| [BDSX](https://github.com/bdsx/bdsx) | Minecraft Bedrock Dedicated Server modding with Node.js | 491 | 🗄️ | TypeScript |
| [Phobos](https://github.com/Phobos-developers/Phobos) | Engine extension for C&C Red Alert 2: Yuri's Revenge | 468 | 🟢 | C++ |
| [RED4ext](https://github.com/wopss/RED4ext) | Script extender for REDengine 4 (Cyberpunk 2077) | 446 | 🟢 | C++ |
| [sfall](https://github.com/sfall-team/sfall) | sfall - Engine modifications for Fallout 2 | 443 | 🟢 | C++ |
| [RetroMCP](https://github.com/MCPHackers/RetroMCP-Java) | Mod Coder Pack for decompiling and recompiling old Minecraft versions | 410 | 🟢 | Java |
| [ARCropolis](https://github.com/Raytwo/ARCropolis) | Modding framework for Super Smash Bros. Ultimate file replacement | 392 | 🟢 | Rust |
| [Oxide.Rust](https://github.com/OxideMod/Oxide.Rust) | Rust game extension for the Oxide modding framework | 387 | 🟢 | C# |
| [anno1800-mod-loader](https://github.com/magicalcookie/anno1800-mod-loader) | Mod loader for Anno 1800 | 368 | 🗄️ | C++ |
| [SFSE](https://github.com/ianpatt/sfse) | Starfield Script Extender | 359 | 🟢 | C++ |
| [SKSE64](https://github.com/ianpatt/skse64) | Skyrim Special Edition Script Extender | 358 | 🟢 | C++ |
| [REPENTOGON](https://github.com/TeamREPENTOGON/REPENTOGON) | Script extender for The Binding of Isaac: Repentance | 354 | 🟢 | C++ |
| [SatisfactoryModLoader](https://github.com/satisfactorymodding/SatisfactoryModLoader) | Unofficial mod loader for Satisfactory | 344 | 🟢 | C++ |
| [Hollow Knight Modding API](https://github.com/hk-modding/api) | Modding API for Hollow Knight built by patching game assemblies | 342 | 🟢 | C# |
| [FFXIVClientStructs](https://github.com/aers/FFXIVClientStructs) | Reverse engineered native class layouts of the Final Fantasy XIV client | 341 | 🟢 | C# |
| [xOBSE](https://github.com/llde/xOBSE) | Oblivion Script Extender | 313 | 🟢 | C++ |
| [Skyline](https://github.com/skyline-dev/skyline) | Runtime hooking and code patching environment for Nintendo Switch games | 311 | 🟢 | C++ |
| [unreal-vr](https://github.com/TheNewJavaman/unreal-vr) | Adds VR support to flatscreen Unreal Engine games | 301 | 🔴 | C++ |
| [ZHMModSDK](https://github.com/OrfeasZ/ZHMModSDK) | Modding SDK and mod loader for Hitman World of Assassination | 285 | 🟢 | C++ |
| [BakkesModSDK](https://github.com/bakkesmodorg/BakkesModSDK) | Unofficial SDK for Rocket League modding with BakkesMod | 284 | 🟢 | C++ |
| [MetaHookSv](https://github.com/MetaHookSv/MetaHookSv) | MetaHook plugin loader ported to the Sven Co-op GoldSrc engine | 259 | 🟢 | Python |
| [Reactor](https://github.com/NuclearPowered/Reactor) | Modding API for Among Us | 254 | 🟢 | C# |
| [UnrealModLoader](https://github.com/RussellJerome/UnrealModLoader) | Universal mod loader for Unreal Engine 4 games | 246 | 🔴 | C++ |
| [CommonLibSSE](https://github.com/Ryan-rsm-McKenzie/CommonLibSSE) | Reverse-engineered C++ library of Skyrim SE game types for plugin development | 241 | 🔴 | C++ |
| [BSIPA](https://github.com/nike4613/BeatSaber-IPA-Reloaded) | Unity mod injector built for Beat Saber | 204 | 🟢 | C# |
| [D2RMM](https://github.com/olegbl/d2rmm) | Mod manager for Diablo II: Resurrected | 202 | 🟢 | TypeScript |
| [Hedge Mod Manager](https://github.com/hedge-dev/HedgeModManager) | Mod manager and code loader for Sonic the Hedgehog PC games | 199 | 🟢 | C# |
| [CLEO 5](https://github.com/cleolibrary/CLEO5) | Script extension library for GTA San Andreas | 184 | 🟢 | C++ |
| [ME3Tweaks Mod Manager](https://github.com/ME3Tweaks/ME3TweaksModManager) | Mod manager for Mass Effect trilogy and Legendary Edition | 178 | 🟢 | C# |
| [R2API](https://github.com/risk-of-thunder/R2API) | Modding API for Risk of Rain 2 | 167 | 🟢 | C# |
| [RE_Kenshi](https://github.com/BFrizzleFoShizzle/RE_Kenshi) | Plugin loader and engine fixes for Kenshi | 166 | 🟢 | C++ |
| [kanan-new](https://github.com/cursey/kanan-new) | Quality-of-life mod framework for Mabinogi | 161 | 🗄️ | C++ |
| [F4SE](https://github.com/ianpatt/f4se) | Fallout 4 Script Extender | 156 | 🟢 | C++ |
| [Slippi ASM](https://github.com/project-slippi/slippi-ssbm-asm) | ASM codes adding rollback netplay and replay recording to Super Smash Bros. Melee | 154 | 🟢 | Assembly |
| [Creation-Kit-Platform-Extended](https://github.com/Perchik71/Creation-Kit-Platform-Extended) | Fixes and extensions for Bethesda's Creation Kit built from reverse engineering | 147 | 🟢 | C++ |
| [Dark-Souls-1-Overhaul](https://github.com/metal-crow/Dark-Souls-1-Overhaul) | Gameplay overhaul mod for Dark Souls built via reverse engineering | 140 | 🟢 | C++ |
| [FF8_demaster](https://github.com/MaKiPL/FF8_demaster) | Unofficial Final Fantasy VIII Remastered core mod | 137 | 🟢 | C |
| [skyrimse-test](https://github.com/Nukem9/skyrimse-test) | Reverse engineering and fixes for Skyrim Special Edition | 137 | 🟡 | C++ |
| [AutomataMP](https://github.com/praydog/AutomataMP) | NieR: Automata multiplayer mod | 135 | 🟡 | C++ |
| [MWSE](https://github.com/MWSE/MWSE) | Morrowind Script Extender with Lua scripting | 133 | 🟢 | C++ |
| [OTAPI](https://github.com/SignatureBeef/Open-Terraria-API) | Patched Terraria server assembly exposing hooks for modding | 124 | 🟢 | C# |
| [ACUFixes](https://github.com/NameTaken3125/ACUFixes) | Add-on and fixes for Assassin's Creed Unity | 116 | 🟡 | C++ |
| [TRLAU-menu-hook](https://github.com/TheIndra55/TRLAU-menu-hook) | Reverse engineering, menu and patches for Tomb Raider Legend/Anniversary/Underworld | 113 | 🟢 | C++ |
| [OWML](https://github.com/ow-mods/owml) | Mod loader and library for Outer Wilds | 109 | 🟢 | C# |
| [MKW-SP](https://github.com/mkw-sp/mkw-sp) | Mario Kart Wii mod with features built on reverse-engineered game code | 101 | 🟢 | C++ |
| [CommonLibSF](https://github.com/Starfield-Reverse-Engineering/CommonLibSF) | Collaborative reverse engineered library for Starfield modding | 100 | 🗄️ | C++ |
| [M2TWEOP-library](https://github.com/EOP-Labs/M2TWEOP-library) | Medieval II: Total War Engine Overhaul Project | 100 | 🟢 | C++ |
| [RB3Enhanced](https://github.com/RBEnhanced/RB3Enhanced) | Open-source plugin providing fixes and features for Rock Band 3 | 99 | 🟢 | C |
| [Installer](https://github.com/SteamClientHomebrew/Installer) | Installer for Millennium, a Steam client theming and plugin loader | 96 | 🟢 | C++ |
| [CommonLibF4](https://github.com/Ryan-rsm-McKenzie/CommonLibF4) | Reverse engineered library for Fallout 4 modding | 93 | 🟢 | C++ |
| [FA2sp](https://github.com/secsome/FA2sp) | Extension for the Red Alert 2 Final Alert 2 map editor | 88 | 🗄️ | C++ |
| [unrealmodding](https://github.com/AstroTechies/unrealmodding) | Rust tools and integrator for modding Unreal Engine games | 88 | 🟢 | Rust |
| [Spore ModAPI](https://github.com/Spore-Community/Spore-ModAPI) | C++ SDK for creating code mods for Spore | 86 | 🟢 | C++ |
| [fromsoftware-rs](https://github.com/vswarte/fromsoftware-rs) | Rust bindings to Elden Ring, Dark Souls 3, Nightreign and Sekiro internals | 77 | 🟢 | Rust |
| [libER](https://github.com/Dasaav-dsv/libER) | Elden Ring API library focused on binary compatibility | 76 | 🟡 | C++ |
| [ModLoader64](https://github.com/hylian-modding/ModLoader64) | Game-agnostic N64 mod loader built on Mupen64Plus | 71 | 🔴 | TypeScript |
| [SADX Mod Loader](https://github.com/X-Hax/sadx-mod-loader) | Mod loader for Sonic Adventure DX PC | 69 | 🟢 | C |
| [OBSE64](https://github.com/ianpatt/obse64) | Oblivion Remastered Script Extender | 65 | 🟡 | C++ |
| [SharpPluginLoader](https://github.com/Fexty12573/SharpPluginLoader) | C# plugin loader for Monster Hunter World | 65 | 🟢 | C# |
| [SA2 Mod Loader](https://github.com/X-Hax/sa2-mod-loader) | Mod loader for Sonic Adventure 2 PC | 64 | 🟢 | C++ |
| [bg3se-macos](https://github.com/tdimino/bg3se-macos) | Baldur's Gate 3 Script Extender replication for macOS | 61 | 🟢 | C |
| [NFSPluginSDK](https://github.com/berkayylmao/NFSPluginSDK) | Reversed types of BlackBox-era Need for Speed games for plugin and script mods | 51 | 🟡 | C++ |
| [bedrock-headers](https://github.com/mcbedrock/bedrock-headers) | Reverse-engineered modding headers for Minecraft: Bedrock Edition | 47 | 🔴 | C++ |
| [plugin-sdk-sa](https://github.com/Dryxio/plugin-sdk-sa) | GTA San Andreas plugin SDK extended from a fully reverse-engineered codebase | 32 | 🟢 | C |
| [Fireflower](https://github.com/MammaMiaTeam/Fireflower) | Patching toolchain for injecting code into Nintendo DS games | 10 | 🔴 | C++ |
| [sro_devkit](https://gitlab.com/florian0/sro_devkit) | Whitebox reverse-engineered codebase of the Silkroad Online client |  | ⚪ |  |

## Open-source Game Clones

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Unciv](https://github.com/yairm210/Unciv) | Open-source Android/Desktop remake of Civ V. | 11,458 | 🟢 | Kotlin |
| [Space Station 14](https://github.com/space-wizards/space-station-14) | Space Station 14 is a revived attempt at a Space Station 13 remake. | 3,870 | 🟢 | C# |
| [Taisei](https://github.com/taisei-project/taisei) | Fan-made, open-source clone of the Touhou series. | 1,655 | 🟢 | C |
| [KeeperFX](https://github.com/dkfans/keeperfx) | Open source remake and Fan Expansion of Dungeon Keeper. | 1,022 | 🟢 | C |
| [OpenCiv3](https://github.com/C7-Game/OpenCiv3) | OpenCiv3 is an open-source, cross-platform, mod-oriented, modernized remake of Civilization III by the fan community... | 669 | 🟢 | C# |
| [OpenApocalypse](https://github.com/OpenApoc/OpenApoc) | Rebuild of the X-COM: Apocalypse engine. | 598 | 🟢 | C++ |
| [OpenKeeper](https://github.com/tonihele/OpenKeeper) | Dungeon Keeper II remake in Java. | 508 | 🟢 | Java |
| [openomf](https://github.com/omf2097/openomf) | One Must Fall 2097 Remake. | 486 | 🟢 | C |
| [KaM Remake](https://github.com/Kromster80/kam_remake) | RTS game remake of Knights and Merchants written in Delphi from scratch. | 377 | 🗄️ | Pascal |
| [Dune-II---The-Maker](https://github.com/stefanhendriks/Dune-II---The-Maker) | A remake of the classic Dune 2 - The Building of a Dynasty (by Westwood Studios) with several enhancements. Like: hig... | 369 | 🟢 | C++ |
| [Romanov's Vengeance](https://github.com/MustaphaTR/Romanovs-Vengeance) | Remake of C&C Red Alert 2 based on the OpenRA engine | 345 | 🟡 | C# |
| [Syndicate Wars](https://github.com/swfans/syndwarsfx) | Syndicate Wars Fan Expansion, Open Source remake of the classic Bullfrog game. | 264 | 🟢 | C |
| [Mr.Boom](https://github.com/Javanaise/mrboom-libretro) | 8-player Bomberman clone for RetroArch/Libretro. | 229 | 🟢 | C |
| [freeserf.net](https://github.com/Pyrdacor/freeserf.net) | Settlers 1 clone written in C# | 175 | 🟢 | C# |
| [UAlbion](https://github.com/csinkers/ualbion) | Remake of 1995 Albion. | 169 | 🟢 | C# |
| [war1](https://github.com/acoto87/war1) | A remake of Warcraft: Orcs & Humans written in C | 154 | 🟢 | C |
| [OPHD](https://github.com/OutpostUniverse/OPHD) | OutpostHD - Open source remake of Sierra On-Line's Outpost. | 146 | 🟢 | C++ |
| [OpenKrush](https://github.com/IceReaper/OpenKrush) | Remake of KKnD (Krush, Kill 'n' Destroy) and KKnD2 based on the OpenRA engine | 128 | 🟢 | C# |
| [OpenSA](https://github.com/Dzierzan/OpenSA) | Remake of Swarm Assault based on the OpenRA engine | 124 | 🔴 | C# |
| [Antares](https://github.com/arescentral/antares) | Remake of Ares, a tactical space combat game. | 112 | 🟡 | C++ |
| [vera20k](https://github.com/YuriPlanet/vera20k) | Red Alert 2: Yuri's Revenge — rebuilt from scratch in Rust for large multiplayer battles. | 107 | 🟢 | Rust |
| [Lionheart Remake](https://github.com/b3dgs/lionheart-remake) | Java remake of Lionheart Amiga game. | 87 | 🟢 | Java |
| [Shattered Paradise](https://github.com/ABrandau/Shattered-Paradise-SDK) | Remake of C&C Tiberian Sun based on the OpenRA engine | 83 | 🟡 | C# |
| [OpenE2140](https://github.com/OpenE2140/OpenE2140) | Remake of Earth 2140 based on the OpenRA engine | 74 | 🟢 | C# |
| [Dungeon Keeper Remake](https://github.com/Themperror/Dungeon-Keeper-Remake) | A modern remake of Dungeon Keeper | 38 | 🟢 | C++ |
| [OpenReliant](https://github.com/OpenReliant/openreliant) | Rebuild of Starlancer in Zig and SDL3. | 33 | 🟢 | Zig |
| [SeriousSamAlphaRemake](https://github.com/tx00100xt/SeriousSamAlphaRemake) | Serious Sam Alpha Remake open source project based. | 32 | 🟡 | C++ |
| [O21](https://github.com/ForNeVeR/O21) | FOSS remake of U95, an old submarine arcade game from 1995. | 31 | 🟢 | F# |
| [rebellion2](https://github.com/davidadas/rebellion2) | Remake of the classic Star Wars Rebellion game for PC using Unity | 30 | 🟢 | C# |
| [parabellum](https://github.com/andreapavoni/parabellum) | An attempt to build a #Travian 3.x clone written in #Rust. | 28 | 🟢 | Rust |
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
| [wedges-trial](https://github.com/begiedz/wedges-trial) | [WIP] Browser logic puzzle game inspired by Gothic's Remake lockpicking mechanism. | 1 | 🟢 | TypeScript |
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
| [Zed Online](https://sourceforge.net/projects/zedonline/) | Remake of the 1996 classic game Z. |  | ⚪ |  |

## Other

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [VoxelSpace](https://github.com/s-macke/VoxelSpace) | Reverse engineered Comanche Voxel Space terrain rendering algorithm | 6,817 | 🟡 | C |
| [libdragon](https://github.com/DragonMinded/libdragon) | libdragon, an open-source Nintendo 64 SDK written without Nintendo's libultra | 1,252 | 🗄️ | C |
| [pspsdk](https://github.com/pspdev/pspsdk) | Open-source PSP SDK for homebrew development, written without Sony's SDK | 1,195 | 🟢 | C |
| [rust-psp](https://github.com/overdrivenpotato/rust-psp) | Rust on the PSP with access to the system libraries | 827 | 🟢 | Rust |
| [GameTracking-Dota2](https://github.com/SteamTracking/GameTracking-Dota2) | Automated tracker of Dota 2 game file and protobuf changes | 771 | 🟢 | C++ |
| [vitaGL](https://github.com/Rinnegatamante/vitaGL) | OpenGL wrapper for PS Vita built on the reverse-engineered sceGxm GPU API | 645 | 🟢 | C |
| [Roblox-Client-Tracker](https://github.com/MaximumADHD/Roblox-Client-Tracker) | Automated tracker extracting information about each Roblox client version | 558 | 🟢 | Assembly |
| [ps2dev](https://github.com/ps2dev/ps2dev) | Open-source PlayStation 2 SDK (ps2sdk and toolchain) written without Sony's SDK | 499 | 🟢 | Shell |
| [Prepare Carefully](https://github.com/edbmods/EdBPrepareCarefully) | EdB Prepare Carefully, a RimWorld mod | 249 | 🟡 | C# |
| [gb-photo](https://github.com/untoxa/gb-photo) | Photo!, a full custom replacement ROM for the Game Boy Camera | 225 | 🟢 | C |
| [psx-spx.github.io](https://github.com/psx-spx/psx-spx.github.io) | Technical reference for the original PlayStation hardware | 165 | 🟢 | Awk |
| [wiki](https://github.com/xboxoneresearch/wiki) | Xbox One research wiki | 153 | 🟢 | Dockerfile |
| [ReversingMinesweeper](https://github.com/repnz/ReversingMinesweeper) | Reverse Engineering Minesweeper: Reconstruct Minesweeper Source Code | 146 | 🔴 | C |
| [x360-research](https://github.com/InvoxiPlayGames/x360-research) | Xbox 360 reverse engineering notes and utilities | 135 | 🟢 |  |
| [prussia](https://github.com/Ravenslofty/prussia) | Prussia, a Rust SDK for the PlayStation 2 | 132 | 🟡 | Rust |
| [Grit Game Engine](https://github.com/grit-engine/grit-engine) | Grit Game Engine | 125 | 🔴 | C++ |
| [2bit-pxlr-studio](https://github.com/HerrZatacke/2bit-pxlr-studio) | Custom ROM for the Game Boy Camera | 110 | 🗄️ | C |
| [botw-re-notes](https://github.com/leoetlino/botw-re-notes) | Reverse engineering notes and tools for Zelda: Breath of the Wild | 110 | 🔴 | C |
| [Chunithm-Research](https://github.com/Suprnova/Chunithm-Research) | In-depth reverse engineering documentation of SEGA Chunithm | 94 | 🔴 |  |
| [VTXCart](https://github.com/xvortex/VTXCart) | Reverse engineering a Neo Geo 161-in-1 cartridge to change ROMs | 90 | 🟡 | C |
| [GameTracking-TF2](https://github.com/SteamTracking/GameTracking-TF2) | Automated tracker of Team Fortress 2 game file changes | 89 | 🟢 | Shell |
| [re_nfpii](https://github.com/GaryOderNichts/re_nfpii) | Reimplementation of the Wii U nn_nfp amiibo library | 88 | 🟡 | C++ |
| [GameTracking-Deadlock](https://github.com/SteamTracking/GameTracking-Deadlock) | Automated tracker of Deadlock game file and protobuf changes | 85 | 🟢 | C++ |
| [ReMasters](https://github.com/kwsch/ReMasters) | Reverse engineering Pokemon Masters | 74 | 🔴 | C# |
| [xbox-tools](https://github.com/JayFoxRox/xbox-tools) | Collection of reverse-engineering tools for the original Xbox | 70 | 🔴 | Python |
| [xbox-board-re](https://github.com/LoveMHz/xbox-board-re) | Board-level reverse engineering of the original Xbox | 62 | 🔴 | Python |
| [3DSort](https://github.com/SalustLab/3DSort) | Rearrange the Nintendo 3DS HOME menu from a PC | 59 | 🟢 | Python |
| [mkw-structures](https://github.com/SeekyCt/mkw-structures) | Documentation of Mario Kart Wii internal structures | 46 | 🟡 | C++ |
| [Super-Mario-64-DS-Remastered](https://github.com/ExcellentGamer/Super-Mario-64-DS-Remastered) | **OPEN SOURCE EPIC** | 46 | 🔴 | C |
| [psp-media-engine-custom-core](https://github.com/mcidclan/psp-media-engine-custom-core) | PSP Media Engine library exposing the ME core's native functions | 40 | 🟢 | C |
| [ExCrypt](https://github.com/emoose/ExCrypt) | Open-source replacement for the Xbox 360 XeCrypt suite | 38 | 🟢 | C |
| [lba-engine-architecture](https://github.com/LBALab/lba-engine-architecture) | Little Big Adventure engine architecture documentation | 35 | 🟡 | Ruby |
| [osdbits](https://github.com/aap/osdbits) | Parts of the PlayStation 2 OSDSYS reverse engineered | 33 | 🟢 | C |
| [nnsdk-rs](https://github.com/ultimate-research/nnsdk-rs) | Unofficial Rust bindings for the Nintendo SDK, used for Switch game modding | 26 | 🟢 | Rust |
| [dump-dvd-kit](https://github.com/XboxDev/dump-dvd-kit) | Tool to dump the ROM of the Xbox DVD Movie Playback Kit dongle | 21 | 🔴 | Python |
| [DarkReignLauncher](https://github.com/Nielk1/DarkReignLauncher) | Tool for Dark Reign: The Future of War game data (osgameclones) (C#) | 19 | 🔴 | C# |
| [psp-media-engine-reload](https://github.com/mcidclan/psp-media-engine-reload) | Unofficial technical documentation and code for the Sony PSP Media Engine | 14 | 🟢 |  |
| [re-virtua-cop-2](https://github.com/jevarg/re-virtua-cop-2) | Reverse engineering of Virtua Cop 2 PC (1997) | 13 | 🟢 | TypeScript |
| [azrael-re](https://codeberg.org/lzmp/azrael-re) | Reverse engineering of Azrael's Tear (1996) |  | ⚪ |  |
| [c2erev](https://sr.ht/~cepheus/c2erev/) | Reverse engineering the Creatures Evolution Engine (Creatures 2/3/Docking Station) |  | ⚪ |  |
| [carrier-command-re](https://gitlab.com/nguillaumin/carrier-command-reverse-engineering) | Reverse engineering of the 1988 game Carrier Command (DOS and other versions) |  | ⚪ |  |
| [dogstuff-docs](https://gitlab.com/dogstuff/docs) | Reverse engineering documentation for 102 Dalmatians: Puppies to the Rescue |  | ⚪ |  |
| [kyrandia2_re](https://codeberg.org/desertear/kyrandia2_re) | Reverse engineering of Legend of Kyrandia II: Hand of Fate |  | ⚪ |  |
| [PixygaREden](https://codeberg.org/LiminaWayfarer/PixygaREden) | Reverse engineering project for the 1999 PS1 game PixyGarden |  | ⚪ |  |
| [pm3](https://codeberg.org/ebbex/pm3) | Reverse engineering project for Premier Manager 3 |  | ⚪ |  |
| [reDeuteros](https://codeberg.org/CyCl0ne/reDeuteros) | Reverse engineering Deuteros (Amiga, 1991) from preservation images |  | ⚪ |  |
| [reDM2](https://codeberg.org/CyCl0ne/reDM2) | Verified reverse engineering of Dungeon Master II |  | ⚪ |  |
| [sky-reenigne](https://codeberg.org/zhmu/sky-reenigne) | Reverse engineering of Beneath a Steel Sky (DOS) |  | ⚪ |  |

## Private Servers

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [TrinityCore](https://github.com/TrinityCore/TrinityCore) | World of Warcraft server emulator (MaNGOS fork) | 10,833 | 🟢 | C++ |
| [AzerothCore](https://github.com/azerothcore/azerothcore-wotlk) | Modular World of Warcraft 3.3.5a server emulator | 9,061 | 🟢 | C++ |
| [Cuberite](https://github.com/cuberite/cuberite) | Lightweight extensible Minecraft server in C++ | 5,454 | 🟢 | C++ |
| [rAthena](https://github.com/rathena/rathena) | Ragnarok Online server emulator in C++ | 3,617 | 🟢 | C++ |
| [PocketMine-MP](https://github.com/pmmp/PocketMine-MP) | Minecraft Bedrock server software built from scratch in PHP | 3,579 | 🗄️ | PHP |
| [Minestom](https://github.com/Minestom/Minestom) | Lightweight Minecraft Java server written from scratch without vanilla code | 3,309 | 🟢 | Java |
| [Valence](https://github.com/valence-rs/valence) | Rust framework for building Minecraft Java servers | 3,280 | 🟢 | Rust |
| [FerrumC](https://github.com/ferrumc-rs/ferrumc) | Reimplementation of the Minecraft server in Rust | 2,433 | 🟢 | Rust |
| [Impostor](https://github.com/Impostor/Impostor) | Open-source reimplementation of the Among Us game server | 2,371 | 🟢 | C# |
| [Glowstone](https://github.com/GlowstoneMC/Glowstone) | Open-source Minecraft Java server implementation | 2,015 | 🟢 | Java |
| [The Forgotten Server](https://github.com/otland/forgottenserver) | Open Tibia MMORPG server emulator in C++ | 1,843 | 🟢 | C++ |
| [LunarCore](https://github.com/Melledy/LunarCore) | A game server reimplementation for a certain turn-based anime game | 1,429 | 🟢 | Java |
| [YgoMaster](https://github.com/pixeltris/YgoMaster) | Offline Yu-Gi-Oh! Master Duel | 1,387 | 🟢 | C# |
| [Nukkit](https://github.com/CloudburstMC/Nukkit) | Minecraft Bedrock Edition server software in Java | 1,363 | 🟢 | Java |
| [OpenMU](https://github.com/MUnique/OpenMU) | Server for the MMORPG MU Online | 1,220 | 🟢 | C# |
| [HeavenMS](https://github.com/ronancpl/HeavenMS) | MapleStory v83 private server emulator (archived) | 1,216 | 🗄️ | Java |
| [DWC Network Server Emulator](https://github.com/barronwaffles/dwc_network_server_emulator) | Nintendo Wi-Fi Connection server emulator for DS and Wii games | 1,183 | 🟡 | Python |
| [CMaNGOS Classic](https://github.com/cmangos/mangos-classic) | Continued MaNGOS World of Warcraft Classic server emulator | 1,094 | 🟢 | C++ |
| [lunar-tear](https://github.com/Walter-Sparrow/lunar-tear) | Private server research project for a certain discontinued mobile game | 1,082 | 🟢 | Go |
| [MaNGOS Zero](https://github.com/mangoszero/server) | World of Warcraft vanilla server emulator | 1,035 | 🟢 | C++ |
| [Hercules](https://github.com/HerculesWS/Hercules) | Ragnarok Online server emulator | 1,019 | 🟢 | C++ |
| [VMaNGOS](https://github.com/vmangos/core) | Progressive vanilla World of Warcraft server emulator for patches 1.2-1.12 | 962 | 🟢 | C++ |
| [Dragonfly](https://github.com/df-mc/dragonfly) | Minecraft Bedrock Edition server software in Go | 853 | 🟢 | Go |
| [Sapphire](https://github.com/SapphireServer/Sapphire) | Final Fantasy XIV server emulator (4.0+) in C++ | 838 | 🟢 | C++ |
| [ds3os](https://github.com/TLeonardUK/ds3os) | Dark Souls 3 and Dark Souls 2 private server emulator | 785 | 🟢 | CMake |
| [Darkflame Server](https://github.com/DarkflameUniverse/DarkflameServer) | LEGO Universe server emulator | 759 | 🟢 | C++ |
| [ServUO](https://github.com/ServUO/ServUO) | Ultima Online server emulator in C# | 759 | 🟢 | C# |
| [ageLANServer](https://github.com/luskaner/ageLANServer) | Web server and launcher for offline/LAN multiplayer in Age of Empires titles | 742 | 🟢 | Go |
| [NexusForever](https://github.com/NexusForever/NexusForever) | Server emulator for the defunct MMORPG WildStar | 679 | 🟢 | C# |
| [Canary](https://github.com/opentibiabr/canary) | OpenTibia server emulator for modern Tibia protocol versions | 659 | 🟢 | Lua |
| [PvPGN](https://github.com/pvpgn/pvpgn-server) | Player vs Player Gaming Network: Battle.net and Westwood Online server emulator | 648 | 🟢 | C++ |
| [EQEmu](https://github.com/EQEmu/EQEmu) | EverQuest server emulator | 636 | 🟢 | C++ |
| [flying-squid](https://github.com/PrismarineJS/flying-squid) | Minecraft Java server implemented in Node.js | 610 | 🟢 | JavaScript |
| [EpinelPS](https://github.com/EpinelPS/EpinelPS) | A private server for some anime game | 568 | 🟢 | C# |
| [MHServerEmu](https://github.com/Crypto137/MHServerEmu) | Server emulator for Marvel Heroes | 566 | 🟢 | C# |
| [CMaNGOS WotLK](https://github.com/cmangos/mangos-wotlk) | World of Warcraft 3.3.5 server emulator (C(ontinued)-MaNGOS) | 561 | 🟢 | C++ |
| [CMaNGOS TBC](https://github.com/cmangos/mangos-tbc) | World of Warcraft 2.4.3 server emulator (C(ontinued)-MaNGOS) | 524 | 🟢 | C++ |
| [LandSandBoat](https://github.com/LandSandBoat/server) | Final Fantasy XI server emulator | 515 | 🟢 | Lua |
| [Arcaea-server](https://github.com/Lost-MSth/Arcaea-server) | 一个微型的 Arcaea 本地服务器 A small local server for Arcaea | 490 | 🟢 | Python |
| [OpenCoreMMO](https://github.com/OpenCoreMMO/OpenCoreMMO) | Modern C# MMORPG server emulator for an OpenTibia-style client | 485 | 🟢 | C# |
| [POGOserver](https://github.com/maierfelix/POGOserver) | Pokemon GO server emulator | 478 | 🔴 | JavaScript |
| [PyRoyale](https://github.com/Igoorx/PyRoyale) | Open-source server emulator for the Mario Royale browser game | 456 | 🗄️ | Python |
| [Darkstar Project](https://github.com/DarkstarProject/darkstar) | Deprecated Final Fantasy XI server emulator | 450 | 🗄️ | TSQL |
| [Houdini](https://github.com/solero/houdini) | Club Penguin private server written in Python 3 | 423 | 🟢 | Python |
| [OpenKO](https://github.com/Open-KO/KnightOnline) | Knight Online server and client reimplementation project | 371 | 🟢 | C++ |
| [ModernUO](https://github.com/modernuo/ModernUO) | High-performance Ultima Online server emulator in C# | 363 | 🟢 | C# |
| [ACE](https://github.com/ACEmulator/ACE) | Asheron's Call server emulator | 345 | 🟢 | C# |
| [Kepler](https://github.com/Quackster/Kepler) | Java server reviving Habbo Hotel v14 (2007 era) | 330 | 🟢 | Java |
| [entralinked](https://github.com/kuroppoi/entralinked) | Standalone Game Sync server emulator for Pokémon Black & White | 322 | 🟢 | Java |
| [Melia](https://github.com/NoCode-NoLife/Melia) | Open-source MMORPG server emulator (Tree of Savior) | 301 | 🟢 | C# |
| [starpoint](https://github.com/duosii/starpoint) | Server emulator for a mobile pinball game. | 292 | 🟡 | TypeScript |
| [bancho.py](https://github.com/osuAkatsuki/bancho.py) | A private osu! server for everyone. Simpler than Akatsuki's production stack, while maintaining core functionality, p... | 287 | 🟢 | Python |
| [Lost City Server](https://github.com/LostCityRS/Server) | RuneScape 2004-era server emulator | 281 | 🟢 | JavaScript |
| [newserv](https://github.com/fuzziqersoftware/newserv) | Phantasy Star Online game server, proxy and reverse-engineering tools | 279 | 🟢 | C++ |
| [Erupe](https://github.com/Mezeporta/Erupe) | Monster Hunter Frontier server emulator in Go | 275 | 🗄️ | Go |
| [dndserver](https://github.com/Snaacky/dndserver) | Dark and Darker private server implementation in Python | 274 | 🗄️ | Python |
| [RPCN](https://github.com/RipleyTom/rpcn) | PSN-compatible server used by RPCS3 for online play | 271 | 🟢 | Rust |
| [bemaniutils](https://github.com/DragonMinded/bemaniutils) | Hobby game services network for Konami Bemani arcade games | 265 | 🟢 | Python |
| [RunUO](https://github.com/runuo/runuo) | Classic Ultima Online server emulator in C# | 258 | 🟡 | C# |
| [MCGalaxy](https://github.com/ClassiCube/MCGalaxy) | Minecraft Classic protocol server software | 234 | 🟢 | C# |
| [PayCheck3](https://github.com/SlejmUr/PayCheck3) | Payday 3 server emulator | 216 | 🟢 | C# |
| [Open Toontown](https://github.com/open-toontown/open-toontown) | Open-source Toontown Online based on the final Disney client version | 206 | 🟢 | Python |
| [bravo](https://github.com/bravoserver/bravo) | Reverse engineered Minecraft server implementation (1.4.x protocol) | 205 | 🔴 | Python |
| [Apollo](https://github.com/apollo-rsps/apollo) | RuneScape private server suite in Java | 195 | 🔴 | Java |
| [OpenSpy Core](https://github.com/openspy/openspy-core) | GameSpy replacement backend services (master server, NAT negotiation, presence) | 191 | 🟢 | C++ |
| [SWGEmu Core3](https://github.com/swgemu/Core3) | Star Wars Galaxies pre-CU server emulator core | 190 | 🟢 | Lua |
| [LawinServer](https://github.com/Lawin0129/LawinServer) | Local single-user Fortnite backend server emulator | 188 | 🟢 | JavaScript |
| [Maple2](https://github.com/MS2Community/Maple2) | Server emulator for MapleStory 2 | 188 | 🟢 | C# |
| [rsmod](https://github.com/rsmod/rsmod) | Old School RuneScape game server emulator | 188 | 🟡 | Kotlin |
| [Classic-Brawl](https://github.com/PhoenixFire6934/Classic-Brawl) | Python Brawl Stars server emulator for v26 | 186 | 🟡 | Python |
| [AGS-GC](https://github.com/Anime-Game-Servers/AGS-GC) | A server software implementation, ineroperable with a certain anime game client. The code in this repository is fully... | 177 | 🟢 | Java |
| [aion-server](https://github.com/beyond-aion/aion-server) | Aion server emulator | 174 | 🟢 | Java |
| [cuwo](https://github.com/matpow2/cuwo) | Open server and utilities for Cube World | 173 | 🔴 | C |
| [topaz](https://github.com/project-topaz/topaz) | Final Fantasy XI server emulator | 164 | 🗄️ | Lua |
| [OregonCore](https://github.com/OregonCore/OregonCore) | World of Warcraft 2.4.3 server emulator | 162 | 🔴 | C++ |
| [LawinServerV2](https://github.com/Lawin0129/LawinServerV2) | Fortnite backend emulator with matchmaking and XMPP support | 160 | 🟡 | JavaScript |
| [VanillaReimplementation](https://github.com/Minestom/VanillaReimplementation) | Reimplementation of vanilla Minecraft features on Minestom | 159 | 🗄️ | Java |
| [L2dotNET](https://github.com/Elfocrash/L2dotNET) | Lineage II Interlude server emulator in C# | 157 | 🔴 | C# |
| [UniSpyServer](https://github.com/GameProgressive/UniSpyServer) | Open-source GameSpy backend emulator | 155 | 🟢 | Python |
| [desse](https://github.com/ymgve/desse) | Demon's Souls private server emulator | 153 | 🔴 | Python |
| [Dawnshard](https://github.com/SapiensAnatis/Dawnshard) | Server emulator for Dragalia Lost | 152 | 🟢 | C# |
| [MuEmu](https://github.com/Yomalex/MuEmu) | C# MU Online server supporting multiple client versions | 149 | 🟢 | C# |
| [POL](https://github.com/polserver/polserver) | PenUltima Online server compatible with most Ultima Online clients | 147 | 🟢 | C++ |
| [Dawn of Light](https://github.com/Dawn-of-Light/DOLSharp) | Dark Age of Camelot server emulator | 137 | 🟢 | C# |
| [server](https://github.com/sp-tarkov/server) | The Server project for SPT | 133 | 🗄️ | TypeScript |
| [Nebula](https://github.com/Melledy/Nebula) | A server emulator for the game Stella Sora | 131 | 🟢 | Java |
| [WiiLink WFC Server](https://github.com/WiiLink24/wfc-server) | Nintendo Wi-Fi Connection replacement server by WiiLink | 128 | 🟢 | Go |
| [Kawari](https://github.com/redstrate/Kawari) | Unofficial Final Fantasy XIV server emulator for 7.x | 127 | 🗄️ | Rust |
| [belfast](https://github.com/catgirl-systems/belfast) | Reimplementation of a server for Azur Lane | 117 | 🟢 | Go |
| [Edelstein](https://github.com/Kaioru/Edelstein) | MapleStory v95 server emulator in C# | 115 | 🟢 | C# |
| [SeventhUmbral](https://github.com/jpd002/SeventhUmbral) | Final Fantasy XIV v1.23b server emulator | 112 | 🔴 | C |
| [zombie-cafe-revival](https://github.com/Airyzz/zombie-cafe-revival) | Reverse engineering and reviving the mobile game Zombie Cafe | 112 | 🟡 | Smali |
| [BaPs](https://github.com/gucooing/BaPs) | BaPs | 109 | 🗄️ | Go |
| [Pretendo account server](https://github.com/PretendoNetwork/account) | Replacement Nintendo Network account server for Wii U and 3DS | 108 | 🟢 | TypeScript |
| [quantum-core-x](https://github.com/MeikelLP/quantum-core-x) | Metin2 open source server emulator in C# | 107 | 🟢 | C# |
| [Cypress](https://github.com/PvZ-Cypress/Cypress) | Dedicated servers for Plants vs. Zombies: Garden Warfare 1, 2 and Battle for Neighborville | 106 | 🟢 | C++ |
| [EVESharp](https://github.com/Almamu/EVESharp) | EVE Online server emulator in C# | 104 | 🟡 | C# |
| [Orpheus](https://github.com/aatxe/Orpheus) | Open source MapleStory v83 server emulator | 104 | 🗄️ | Java |
| [kinoko](https://github.com/iw2d/kinoko) | MapleStory v95 server emulator | 102 | 🟢 | Java |
| [butterfly](https://github.com/skogaby/butterfly) | e-amusement server emulator for Dance Dance Revolution A | 99 | 🔴 | Java |
| [Prospect](https://github.com/AeonLucid/Prospect) | Server emulation for The Cycle: Frontier | 98 | 🟡 | C# |
| [Pirates-Online-Rewritten](https://github.com/PiratesOnlineRewritten/Pirates-Online-Rewritten) | Revival of Disney's Pirates of the Caribbean Online with a rewritten server | 96 | 🔴 | Python |
| [RestoRoom](https://github.com/RestoRoom/RestoRoom) | Community reimplementation of the Rec Room servers | 95 | 🟢 |  |
| [soapbox-race-core](https://github.com/SoapboxRaceWorld/soapbox-race-core) | Need for Speed: World server emulator core | 90 | 🔴 | Java |
| [AscNet](https://github.com/rafi1212122/AscNet) | Punishing: Gray Raven private server! | 89 | 🟢 | C# |
| [_archive_lineage2js](https://github.com/space2pacman-misc/_archive_lineage2js) | Node.js Lineage 2 server emulator (Chronicle 1) | 88 | 🗄️ | JavaScript |
| [SphereServer Source-X](https://github.com/Sphereserver/Source-X) | Ultima Online server emulator | 86 | 🟢 | C |
| [server-csharp](https://github.com/sp-tarkov/server-csharp) | A C# rewrite of the SPT server project. | 85 | 🗄️ | C# |
| [oxide](https://github.com/T-x-T/oxide) | Reimplementation of the Minecraft server in pure Rust | 79 | 🟢 | Rust |
| [NetspherePirates](https://github.com/wtfblub/NetspherePirates) | Experimental S4 League server emulator | 78 | 🗄️ | C# |
| [UOX3](https://github.com/UOX3DevTeam/UOX3) | Ultima Offline eXperiment 3 Ultima Online server emulator | 75 | 🟢 | C++ |
| [Juxtaposition](https://github.com/PretendoNetwork/juxtaposition) | Pretendo's Miiverse replacement service for Wii U and 3DS | 73 | 🟢 | TypeScript |
| [DBOGLOBAL](https://github.com/dboglobal/DBOGLOBAL) | Dragon Ball Online Global client and server emulator | 71 | 🟡 | C++ |
| [Hitman-5-Server](https://github.com/LennardF1989/Hitman-5-Server) | Emulated server for Hitman: Absolution and Hitman: Sniper Challenge | 71 | 🗄️ | HTML |
| [Bayshore](https://github.com/ProjectAsakura/Bayshore) | Server reimplementation for Wangan Midnight Maximum Tune 6 | 70 | 🟢 | TypeScript |
| [BlueRebirth](https://github.com/LunarConcerto/BlueRebirth) | Offline restoration project for a discontinued mobile game | 69 | 🟢 | C# |
| [OpenDAoC](https://github.com/OpenDAoC/OpenDAoC-Core) | Free Dark Age of Camelot server emulator | 69 | 🟢 | C# |
| [mxoemu](https://github.com/rajkosto/mxoemu) | Server emulator for the shut-down MMO The Matrix Online | 64 | 🔴 | C |
| [cwk-server](https://github.com/shishkabob27/cwk-server) | Reverse engineered server for Card Wars Kingdom | 60 | 🗄️ | Python |
| [Freya](https://github.com/ubis/Freya) | Cabal Online server emulator | 60 | 🟡 | Go |
| [perlica-rs](https://github.com/Yoshk4e/perlica-rs) | A server software reimplementation for an old version of a certain anime game about factories. | 60 | 🟢 | Rust |
| [DragonFable-Private-Server](https://github.com/hiperesp/DragonFable-Private-Server) | DragonFable private server emulator for the current client | 59 | 🟢 | PHP |
| [puniemu](https://github.com/SuperTavor/puniemu) | Server emulator for Yo-kai Watch Puni Puni | 59 | 🟢 | C# |
| [titanic](https://github.com/osuTitanic/titanic) | A private server that supports all osu! clients (2007-2026) | 59 | 🟢 | Go |
| [NFS-Online-Server](https://github.com/moio9/NFS-Online-Server) | Online server emulator for NFS Most Wanted, Underground 2 and Carbon | 58 | 🟢 | Python |
| [OpenRS2](https://github.com/openrs2/openrs2) | Open-source multiplayer game server compatible with the RuneScape client | 58 | 🟢 | Kotlin |
| [remielle](https://github.com/thexeondev/remielle) | Zenless Zone Zero server emulator focused on efficiency, stability and correctness. | 55 | 🟢 | Zig |
| [topaz](https://github.com/topaz-next/topaz) | Server emulator for Final Fantasy XI | 55 | 🗄️ | Lua |
| [dream-server](https://github.com/NDSLink/dream-server) | Server for Pokemon Dream World | 54 | 🟡 | SCSS |
| [Maelstrom](https://github.com/Rawaho/Maelstrom) | Server emulator for Final Fantasy XIV (Stormblood 4.10) | 54 | 🔴 | C# |
| [Hardline Dreams](https://github.com/hdneo/mxo-hd) | C# server emulator for The Matrix Online | 53 | 🟢 | C# |
| [Hoshimi](https://github.com/Enigfrank/Hoshimi) | Unofficial local game emulation server for Hoshimi | 53 | 🟢 | PowerShell |
| [Infantry-Online-Server](https://github.com/InfantryOnline/Infantry-Online-Server) | Free Infantry Online server emulator | 53 | 🟢 | C# |
| [Holocore](https://github.com/ProjectSWGCore/Holocore) | Star Wars Galaxies server emulator for the JVM | 52 | 🟢 | Kotlin |
| [NTRSimulator](https://github.com/raphaeIl/NTRSimulator) | Server Emulator for a certain NTR game | 52 | 🟢 | C# |
| [wrath-rs](https://github.com/Victov/wrath-rs) | A very functionally incomplete World of Warcraft: Wrath of the Lich King server emulator written in pure rust. | 52 | 🟢 | Rust |
| [BetrockPlusPlus](https://github.com/OfficialPixelBrush/BetrockPlusPlus) | Minecraft Beta 1.7.3 compatible server written in C++ | 51 | 🟢 | C++ |
| [Maple2](https://github.com/kOchirasu/Maple2) | Server emulator for MapleStory 2 | 51 | 🟡 | C# |
| [Modern-Brawl](https://github.com/PhoenixFire6934/Modern-Brawl) | Python Brawl Stars server emulator for version 28.189 | 51 | 🔴 | Python |
| [Sunrise](https://github.com/SunriseCommunity/Sunrise) | 🌅 Sunrise - osu! server written in C# | 51 | 🟢 | C# |
| [tpp-server-emulator](https://github.com/alicealys/tpp-server-emulator) | Reimplementation of the Metal Gear Solid V: The Phantom Pain backend server | 50 | 🟢 | C++ |
| [waygate-server](https://github.com/vswarte/waygate-server) | Elden Ring custom matchmaking server implementation | 48 | 🟢 | Rust |
| [XboxLive.Server](https://github.com/zzVertigo/XboxLive.Server) | Revival server for Xbox Live 1.0 | 44 | 🗄️ | C# |
| [protanki-server](https://github.com/Assasans/protanki-server) | Open-source reimplementation of the ProTanki server | 43 | 🗄️ | Kotlin |
| [LibreKO](https://github.com/ZeusAFK/LibreKO) | From-scratch reimplementation of the Knight Online game server and client | 42 | 🟢 | C# |
| [SporeServer](https://github.com/Rosalie241/SporeServer) | A WIP Spore Server Replacement | 42 | 🟡 | C# |
| [OpenBachelorS](https://github.com/pfyy/OpenBachelorS) | OpenBachelorS | 40 | 🟢 | Python |
| [shiro](https://github.com/mellowagain/shiro) | High-performance osu! Bancho server re-implementation in C++ | 40 | 🗄️ | C++ |
| [azerust](https://github.com/arlyon/azerust) | An experimental World of Warcraft emulator in Rust | 39 | 🟡 | Rust |
| [g0v0-server](https://github.com/GooGuTeam/g0v0-server) | An osu!(lazer) private server that is easy to deploy, highly scalable, and fully featured to meet diverse operational... | 39 | 🟢 | Python |
| [Pocket Relay](https://github.com/PocketRelay/Server) | Mass Effect 3 EA Blaze server emulator for LAN and WAN play | 39 | 🟢 | Rust |
| [LuxonServer](https://github.com/niansa/LuxonServer) | Clean-room reimplementation of the Photon LoadBalancing server | 38 | 🟢 | C |
| [PTCGP-Private-Server](https://github.com/Layen-lang/PTCGP-Private-Server) | Unofficial local compatibility server and profile editor for Pokémon TCG Pocket | 37 | 🟢 | Go |
| [2006rebotted](https://github.com/dginovker/2006rebotted) | A 2006 RuneScape 2 Emulation Server. | 36 | 🔴 | Java |
| [EVEmu](https://github.com/evemuproject/evemu_crucible) | EVE Online server emulator for the Crucible client | 32 | 🔴 | C++ |
| [OpenPayload](https://github.com/CLF78/OpenPayload) | Open-source reimplementation of the Wiimmfi payload for Mario Kart Wii | 30 | 🟡 | C++ |
| [sonetto-rs](https://github.com/Yoshk4e/sonetto-rs) | a server software re-implementaion for R1999 | 29 | 🗄️ | Rust |
| [DoctoratePy](https://github.com/nonobject14514/DoctoratePy) | DoctoratePy | 26 | 🔴 | Python |
| [Batla-3D-server-emu](https://github.com/Serega25511s/Batla-3D-server-emu) | Clean-room server emulator for the shut-down arena shooter Batla 3D | 25 | 🟢 | C# |
| [Orchis](https://github.com/CerisWhite/Orchis) | A Dragalia Lost Private Server | 25 | 🟢 | JavaScript |
| [wow_vanilla_server](https://github.com/gtker/wow_vanilla_server) | WIP Rust server for WoW 1.12 | 23 | 🟡 | Rust |
| [OT6-Reconstruction](https://github.com/ApfelTeeSaft/OT6-Reconstruction) | Decompilation of Fortnite Alpha (2016) game server logic | 22 | 🟢 | C++ |
| [enigma](https://github.com/yoncodes/enigma) | server for that one card game | 20 | 🟢 | Rust |
| [mooege](https://github.com/mooege/mooege) | Educational Diablo III game server emulator | 20 | 🔴 |  |
| [KazusaGI_cb2](https://github.com/Hiro420/KazusaGI_cb2) | Server sofware reimplementation for an old version of a certain anime game | 18 | 🟢 | C# |
| [Lolo](https://github.com/BanterSR/Lolo) | 开放空间/OverField 服务端部分实现 | 18 | 🟢 | JavaScript |
| [assettocorsa_competizione_server](https://github.com/renaudallard/assettocorsa_competizione_server) | Assetto Corsa Competizione server | 17 | 🟢 | C |
| [spikewall](https://github.com/Ramen2X/spikewall) | An open source server for the defunct 2015 mobile game Sonic Runners. | 17 | 🟢 | C# |
| [Z7](https://github.com/Khysnik/Z7) | Reverse-engineered Blaze server for Plants vs Zombies: Garden Warfare 2 | 16 | 🟢 | C++ |
| [of-ps](https://github.com/byzp/of-ps) | overfield emu server | 12 | 🟢 | Python |
| [hk4e-go](https://github.com/Kei-Luna/hk4e-go) | 世҉̰̗͕́͢͡界҈̧̟͙̖̎̎̕遗҈͚̄̓̍̕͜忘҈̢͕̙̪̄͞我҉̛̰̯̊͢ | 9 | 🟡 | Go |
| [OpenLethe](https://github.com/LEAGUE-OF-NINE/OpenLethe) | OpenLethe | 9 | 🟢 | C# |
| [KazusaHSR_0.56](https://github.com/Hiro420/KazusaHSR_0.56) | Open-source server reimplementation for an early version of an anime game with stars and rails | 8 | 🟢 | C# |
| [Mystic-Nights-Online](https://github.com/jeremydecola/Mystic-Nights-Online) | Reverse-engineered multiplayer private server for the PS2 game Mystic Nights | 8 | 🟡 | Python |
| [ew](https://github.com/ethanaobrien/ew) | A sif2 server | 7 | 🟢 | Rust |
| [UberStrike-Reverse-Engineered](https://github.com/festivaldev/UberStrike-Reverse-Engineered) | Reverse-engineered UberStrike client and server | 7 | 🟡 | C# |
| [garcia](https://github.com/yoncodes/garcia) | server for a random 2d game | 2 | 🟢 | Rust |
| [dev_wow_auth_server](https://github.com/gtker/dev_wow_auth_server) | World of Warcraft authentication server for development | 1 | 🟡 | Rust |
| [2009scape](https://gitlab.com/2009scape/2009scape) | Open-source 2009-era RuneScape server remake |  | ⚪ |  |
| [ACEmulator](https://emulator.ac) | A custom, completely from-scratch open source server emulator for Asheron’s Call built on C#. |  | ⚪ |  |
| [mw-tools](https://gitlab.com/wander-gr/mw-tools) | Unofficial Myth War I server and tools |  | ⚪ |  |
| [opengallop](https://codeberg.org/mambosaba/opengallop) | Game server reimplementation for Umamusume (global region) |  | ⚪ |  |
| [zcure](https://gitlab.com/blrevive/zcure) | Server for Blacklight: Retribution 3.02 based on the decompiled ZCure library |  | ⚪ |  |

## Static Recompilations & PC Ports

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [N64Recomp](https://github.com/N64Recomp/N64Recomp) | Static recompiler that turns N64 binaries into portable C code | 8,264 | 🟢 | C++ |
| [Zelda64Recomp](https://github.com/Zelda64Recomp/Zelda64Recomp) | Static recompilation of Majora's Mask for PC | 7,457 | 🟢 | C |
| [XenonRecomp](https://github.com/hedge-dev/XenonRecomp) | Converts Xbox 360 PowerPC executables into C++ for recompilation on modern platforms | 6,567 | 🟡 | C++ |
| [dusk](https://github.com/TwilitRealm/dusklight) | Twilight Princess PC port based on the zeldaret tp decompilation | 5,921 | 🟢 | C++ |
| [UnleashedRecomp](https://github.com/hedge-dev/UnleashedRecomp) | Unofficial PC port of Xbox 360 Sonic Unleashed via static recompilation | 5,215 | 🟢 | C++ |
| [gen1recomp](https://github.com/bryanthaboi/gen1recomp) | Native recompilation of Pokemon Red/Blue/Yellow with mods | 3,964 | 🟢 | Lua |
| [BloodBorne for Windows](https://github.com/Supermedo/bloodborne_pc) | Recomp of BloodBorne (PS4) to Windows. | 3,630 | 🟢 | C++ |
| [SpaghettiKart](https://github.com/HarbourMasters/SpaghettiKart) | Mario Kart 64 PC port based on the mk64 decompilation, with track editor | 2,422 | 🟢 | C |
| [Starship](https://github.com/HarbourMasters/Starship) | Star Fox 64 PC port based on the sf64 decompilation | 2,104 | 🟢 | C |
| [BanjoRecomp](https://github.com/BanjoRecomp/BanjoRecomp) | Banjo-Kazooie static recompilation with mod support | 2,052 | 🟢 | C |
| [P.T. for PC](https://github.com/LoreanXavier/pt-pc) | Native PC port of Kojima's P.T. with game logic rebuilt in C++, runs from your own PS4 files | 1,924 | 🟢 | C++ |
| [sm64ex](https://github.com/sm64pc/sm64ex) | Super Mario 64 PC port fork focused on easier modding | 1,867 | 🟡 | C |
| [N64RecompLauncher](https://github.com/SirDiabo/GithubLauncher) | Installs and updates N64 static recompilation ports in one place | 1,863 | 🟢 | C# |
| [skate3recomp](https://github.com/mchughalex/skate3recomp) | Native Windows/Linux/macOS port of Skate 3 via static recompilation | 1,662 | 🟢 | C++ |
| [OpenCE](https://github.com/OpenCommunityEdition/OpenCE) | Enhanced recomp of the original Xbox Halo: Combat Evolved to all Windows, Linux and Android. | 1,652 | 🟢 | C |
| [rt64](https://github.com/rt64/rt64) | N64 graphics renderer used by emulators and native recomp ports | 1,617 | 🟢 | C++ |
| [ACGC-PC-Port](https://github.com/flyngmt/ACGC-PC-Port) | Animal Crossing (GameCube) PC port from the ac-decomp decompilation | 1,502 | 🟢 | C |
| [sm64coopdx](https://github.com/coop-deluxe/sm64coopdx) | Online multiplayer Super Mario 64 PC port based on the decompilation | 1,451 | 🟢 | C |
| [REDRIVER2](https://github.com/OpenDriver2/REDRIVER2) | Driver 2 PlayStation reverse engineering and PC port | 1,413 | 🟢 | C |
| [LASRecomp](https://github.com/peiikai/LASRecomp) | Static recompilation of Link's Awakening (Switch) to native macOS and Windows | 1,253 | 🟢 | C |
| [ReXGlue SDK](https://github.com/rexglue/rexglue-sdk) | SDK for static recompilation of Xbox 360 games from PowerPC to portable C++ | 1,104 | 🟢 | C |
| [isle-portable](https://github.com/isledecomp/isle-portable) | Portable LEGO Island source port built from the isle decompilation | 1,074 | 🟢 | C++ |
| [ps2-web-recomp](https://github.com/snuri00/ps2-web-recomp) | PS2 games statically recompiled to WebAssembly with a native runtime to run in the browser | 1,053 | 🟢 | C++ |
| [WipEout Phantom Edition](https://github.com/wipeout-phantom-edition/wipeout-phantom-edition) | WipEout PC port that runs from the original disc image | 977 | 🟡 |  |
| [SymphonyRecomp](https://github.com/BlackLabelHQ/SymphonyRecomp) | Static recompilation of Castlevania: Symphony of the Night | 918 | 🟢 | C# |
| [GoldenEye-Recomp](https://github.com/SunJaycy/GoldenEye-Recomp) | Recompilation of the cancelled Xbox 360 GoldenEye 007 for PC | 899 | 🟢 | C |
| [devilution-nx](https://github.com/lantus/devilution-nx) | Diablo port for Nintendo Switch based on Devilution | 891 | 🔴 | C++ |
| [Ghostship](https://github.com/HarbourMasters/Ghostship) | Harbour Masters Super Mario 64 source port with mods and modern graphics | 830 | 🟢 | C |
| [Blue Dragon (re:Blue)](https://github.com/zolaware/reblue) | Xbox 360 static recompilation of Blue Dragon (re:Blue) | 810 | 🟢 | C++ |
| [ZeldaWWHDRecomp](https://github.com/ZeldaWWHDRecomp/ZeldaWWHDRecomp) | Static recompilation of The Wind Waker HD (Wii U) | 744 | 🟢 | C |
| [pinyon-shift](https://github.com/arcanite24/pinyon-shift) | A playable preview of Forza Horizon static recompilation | 739 | 🟢 | Python |
| [zelda-alttp-3ds](https://github.com/EstebanPdN/zelda-alttp-3ds) | Nintendo 3DS port of Zelda: A Link to the Past based on zelda3 | 717 | 🟢 | C |
| [Silent Hill native PC port](https://github.com/SlickAmogus/silent-hill-decomp) | Multiplatform port of the Silent Hill 1 PSX decompilation | 712 | 🟢 | C |
| [LostOdysseyRecomp](https://github.com/freefrank/LostOdysseyRecomp) | Experimental native PC port of Lost Odyssey using static recompilation. No game assets included. | 692 | 🟢 | C++ |
| [Marathon Recompiled](https://github.com/sonicnext-dev/MarathonRecomp) | Static recompilation PC port of Sonic the Hedgehog (2006) | 683 | 🟢 | C++ |
| [smw](https://github.com/snesrev/smw) | Super Mario World reimplementation in C | 644 | 🟡 | C |
| [Mario Kart 64: Recompiled](https://github.com/sonicdcer/MarioKart64Recomp) | Static recompilation of Mario Kart 64 using N64Recomp and RT64 | 615 | 🟢 | C++ |
| [hells-gate-recomp](https://github.com/florinp93/hells-gate-recomp) | Xbox 360 to PC port of Dante's Inferno using ReXGlue (static recompilation) | 578 | 🟢 | C++ |
| [Ace Combat 6: Fires of Liberation](https://github.com/sal063/AC6_recomp) | Xbox 360 static recompilation of Ace Combat 6: Fires of Liberation | 537 | 🟢 | C++ |
| [Donkey Kong 64: Recompiled](https://github.com/Rainchus/Donkey-Kong-64-Recompiled) | Donkey Kong 64 static recompilation with high-framerate support | 519 | 🟢 | C |
| [Lighthouse](https://github.com/HarbourMasters/Lighthouse) | Banjo-Kazooie PC port with multiplayer, romhacks and randomizer | 510 | 🟢 | C |
| [TriAevum](https://github.com/coccofresco/TriAevum) | Native PC recompilation runtime for Ocarina of Time 3D | 505 | 🟢 | C++ |
| [BattleShip](https://github.com/JRickey/BattleShip) | AI-assisted decomp-based PC/Mac/Linux port of Super Smash Bros | 492 | 🟢 | C++ |
| [PaperBoat](https://github.com/HarbourMasters/PaperBoat) | Paper Mario source port based on the decompilation | 490 | 🟢 | C |
| [ps3recomp](https://github.com/sp00nznet/ps3recomp) | Static recompilation runtime libraries for PlayStation 3 titles | 489 | 🟢 | C |
| [MeleePC](https://github.com/999sian/melee-pc) | Recomp of Super Smash Bros Melee to PC. | 486 | 🟢 | C |
| [Fable-2-Recomp](https://github.com/himdo/Fable-2-Recomp) | Fable-2-Recomp | 476 | 🟢 | C++ |
| [Yakumo](https://github.com/TeamGDB/Yakumo) | Static recompilation of a PSP game into a native executable. Vulkan and SDL3. Bring your own copy of the game. | 467 | 🟢 | C++ |
| [Tenkaichi3Decomp](https://github.com/z3xox/Tenkaichi3Decomp) | PC port of Dragon Ball Z: Budokai Tenkaichi 3 built on its decompilation | 462 | 🟢 | C |
| [Metroid Prime Port](https://github.com/Odrannnn/MetroidPrimePort) | Recomp of Metroid Prime to PC and Android. | 460 | 🟢 | C++ |
| [gtasa_vita](https://github.com/TheOfficialFloW/gtasa_vita) | Port of GTA: San Andreas to PS Vita by loading and patching the Android binaries | 456 | 🟡 | C |
| [gb-recompiled](https://github.com/arcanite24/gb-recompiled) | Static recompiler for Game Boy/Color ROMs to portable C with SDL2 runtime | 443 | 🟢 | Python |
| [SR](https://github.com/M-HT/SR) | A project to statically recompile following games to create Windows or Linux (x86 or arm) versions of the games - Alb... | 426 | 🟢 | C |
| [CTR Native](https://github.com/CTR-tools/ctr-native) | Native PC port based on the Crash Team Racing decompilation | 416 | 🟢 | C |
| [BlueWake](https://github.com/chrissotraidis/bluewake) | The Wind Waker (GameCube) static recompilation | 399 | 🟢 | C |
| [Star Fox 64: Recompiled](https://github.com/sonicdcer/Starfox64Recomp) | Static recompilation of Star Fox 64 for Windows/Linux | 388 | 🟢 | C |
| [Fable2Recomp](https://github.com/Fable2Recomp/Fable2Recomp) | A Fable 2 Recomp | 378 | 🟢 | C++ |
| [Edge Of Time Recomp](https://github.com/goliathret/EdgeOfTimeRecomp) | Recomp of Spider Man: Edge of Time from Xbox 360. | 377 | 🟢 | C++ |
| [NocturneRecomp](https://github.com/birabittoh/NocturneRecomp) | Static recompilation of Castlevania: Symphony of the Night (XBLA) for Windows and Linux, built on the ReXGlue SDK. | 368 | 🟢 | C++ |
| [sm64rt](https://github.com/DarioSamo/sm64rt) | Super Mario 64 PC port with ray tracing | 363 | 🟡 | C |
| [speedbreaker](https://github.com/SpeedBreakerProject/speedbreaker) | Unofficial static recompilation of the Xbox 360 version of Need for Speed: Most Wanted (2005): a native port for Stea... | 362 | 🟢 | C++ |
| [TheSimpsonsGameRecomp](https://github.com/YesterMester/TheSimpsonsGameRecomp) | The Simpsons Game Xbox 360 static recompilation | 362 | 🟢 | C++ |
| [Ico-PC](https://github.com/nathanialf/ico-pc) | Recomp of ICO (PS2) to PC. | 358 | 🟢 | C |
| [psp-web-recomp](https://github.com/snuri00/psp-web-recomp) | Static recompilation of PSP games (God of War) to WebAssembly with HLE kernel | 345 | 🟢 | C++ |
| [strikers](https://github.com/new-coke/strikers) | Mario Strikers Charged native PC port / recompilation | 336 | 🟢 | C++ |
| [OpenTIE](https://github.com/elyosh/OpenTIE) | Open-source recomp of TIE Fighter. | 334 | 🟢 | C |
| [Dinosaur Planet: Recompiled](https://github.com/DinosaurPlanetRecomp/dino-recomp) | Static recompilation of the unreleased N64 Dinosaur Planet | 328 | 🟢 | C++ |
| [fifa-street-pc-port](https://github.com/samuelit0davila/fifa-street-pc-port) | Experimental Windows PC port of FIFA Street (2012, Xbox 360) built with ReXGlue | 328 | 🟢 | C# |
| [Goemon64Recomp](https://github.com/klorfmorf/Goemon64Recomp) | Mystical Ninja Starring Goemon static recompilation | 320 | 🟢 | C |
| [pokeemerald-wasm](https://github.com/tripplyons/pokeemerald-wasm) | Pokemon Emerald decompilation recompiled to WebAssembly for the browser | 312 | 🟢 | C |
| [DownpourRecomp](https://github.com/LittleBitUA/DownpourRecomp) | Silent Hill: Downpour Xbox 360 static recompilation | 304 | 🟢 | C++ |
| [BM64Recomp](https://github.com/RevoSucks/BM64Recomp) | Bomberman 64 static recompilation with mod support | 302 | 🟢 | C++ |
| [The-Darkness-Recomp](https://github.com/portingpete/The-Darkness-Recomp) | The Darkness Xbox 360 static recompilation | 299 | 🟢 | C++ |
| [G-Diffuser](https://github.com/Zorkats/G-Diffuser) | Unofficial PC port of F-Zero X based on its decompilation | 291 | 🟢 | C |
| [SMS Launcher](https://github.com/chasem-dev/sms-launcher) | Recomp of Super Mario Sunshine. | 286 | 🟢 | JavaScript |
| [CBFD-Recompiled](https://github.com/sciaschi/CBFD-Recompiled) | Static recompilation of Conker's Bad Fur Day (N64) to native PC | 282 | 🟢 | C |
| [Quest64-Recomp](https://github.com/Rainchus/Quest64-Recomp) | Quest 64 static recompilation with mod support | 281 | 🟢 | C++ |
| [MegaMan64Recompiled](https://github.com/MegaMan64Recomp/MegaMan64Recompiled) | Mega Man 64 static recompilation with mod support | 273 | 🟢 | C++ |
| [ProjectCane](https://github.com/theclub654/ProjectCane) | Playable PC port of Sly Cooper and the Thievius Raccoonus rebuilt via reverse engineering | 273 | 🟢 | C++ |
| [GoldenEye PC Port](https://github.com/jkdansereau/goldeneye-pc-port) | Recomp of GoldenEye 007 (N64). | 270 | 🟢 | C |
| [SCDA-XBERecomp](https://github.com/TGP482/SCDA-XBERecomp) | Unofficial PC port of Splinter Cell: Double Agent (original Xbox) via static recompilation | 264 | 🟢 | C++ |
| [CoD3Recomp](https://github.com/FrankHUN88453/CoD3Recomp) | Static recompilation of Call of Duty 3 (Xbox 360) with host runtime and tools | 258 | 🟢 | C++ |
| [DKC1Recomp](https://github.com/elliotttate/DKC1Recomp) | Static recompilation of Donkey Kong Country (SNES) with widescreen | 247 | 🟢 | C |
| [LCS Recomp](https://github.com/elmasas/lcs-recomp) | Recomp of the PSP game GTA: Liberty City Stories to PC. | 236 | 🟢 | C++ |
| [PSPRecomp](https://github.com/jessicanataliagta/PSPRecomp) | Static recompilation framework for PSP software | 230 | 🟢 | C++ |
| [Condemned2Recomp](https://github.com/psxrestore/Condemned2Recomp) | A static recompilation of Condemned 2: Bloodshot done with RexGlue. | 229 | 🟢 | C++ |
| [Skate3-Mobile](https://github.com/Buku313/Skate3-Mobile) | Play Skate 3 natively on Android. Download one APK, select your own ISO, and skate. ARM64 recompilation with Vulkan r... | 229 | 🟢 | C++ |
| [nebula](https://github.com/keepvaibin/nebula) | Recompilation of Super Mario Galaxy targeting Windows, with macOS and Android planned | 222 | 🟢 | C++ |
| [GoldenRecomp](https://github.com/kholdfuzion/GoldenRecomp) | WIP Recompilation of a game about a special agent who saves the world from a traitor. | 218 | 🟢 | C++ |
| [Viva Piñata: Trouble in Paradise](https://github.com/SolarCookies/TiP-Recomp) | Xbox 360 static recompilation of Viva Piñata: Trouble in Paradise | 215 | 🟢 | C++ |
| [yoyoloader_vita](https://github.com/Rinnegatamante/yoyoloader_vita) | Loader that runs Android GameMaker (YoYo Runner) games natively on PS Vita | 215 | 🟢 | C |
| [DimensionsRecomp](https://github.com/NeverCookFirst/DimensionsRecomp) | Proof that a toys-to-life game can be recompiled. A native PC build of LEGO Dimensions, made by statically recompilin... | 214 | 🟢 | C++ |
| [mario-kart-64-3ds](https://github.com/EstebanPdN/mario-kart-64-3ds) | Native Nintendo 3DS port based on the Mario Kart 64 decompilation | 213 | 🟢 | C++ |
| [daytona-xbla-recomp](https://github.com/Subarasheese/daytona-xbla-recomp) | A static recompilation of Daytona USA (Xbox 360 / XBLA, 2011) | 212 | 🟢 | C++ |
| [Daytona Arcade Recomp](https://github.com/alphanu1/daytona-arcade-recomp) | Recomp of Daytona Racing to PC. | 211 | 🟢 | C++ |
| [ForzaHorizon1-ReImagined](https://github.com/Dyotson/ForzaHorizon1-ReImagined) | Forza Horizon (Xbox 360) running natively on PC, rebuilt with online free roam and leaderboards | 207 | 🟢 | Python |
| [Crash Team Racing: High Octane](https://github.com/Rinnegatamante/Crash-Team-Racing-High-Octane) | CTR source port for PC, PS Vita and web | 202 | 🟢 | C |
| [MKW-3DS](https://github.com/MiniBandit/MKW-3DS) | Native Nintendo 3DS port of Mario Kart Wii, built from your own disc | 202 | 🟢 | C++ |
| [Yu-Gi-Oh! Forbidden Memories Recompiled](https://github.com/Unchiga/Yu-Gi-Oh-Forbidden-Memories-Recompiled) | Yu-Gi-Oh! Forbidden Memories PlayStation static recompilation | 202 | 🟢 | C |
| [ssbu-recomp](https://github.com/Denkishi/ssbu-recomp) | Static recompilation of Super Smash Bros. Ultimate 13.0.4 to a native Windows program | 197 | 🟢 | C |
| [SkyRoads-Codex](https://github.com/ammaarreshi/SkyRoads-Codex) | SkyRoads DOS game reverse engineered without source using Codex | 195 | 🟢 | Rust |
| [Duke Nukem Zero Hour: Recompiled](https://github.com/sonicdcer/DNZHRecomp) | Duke Nukem: Zero Hour static recompilation with gyro aiming and high FPS | 191 | 🟢 | C++ |
| [PGR4-Recomp](https://github.com/beatrixzy/PGR4-Recomp) | A Recompilation of Project Gotham Racing 4 | 189 | 🟢 | C++ |
| [sunpad](https://github.com/chrissotraidis/sunpad) | Super Mario Sunshine on iOS, macOS and tvOS via static recompilation | 187 | 🟢 | Objective-C++ |
| [King Kong: Recompiled](https://github.com/TekRantGaming/king-kong-recompiled) | Peter Jackson's King Kong Xbox 360 static recompilation | 186 | 🟢 | C++ |
| [Perfect Dark](https://github.com/DabDavis/perfect-dark-dabs-mod) | Recomp of the N64 game Perfect Dark to PC, with enhancements. | 186 | 🟢 | C |
| [sega-vr-disasm](https://github.com/matiaszanolli/sega-vr-disasm) | Complete static recompilation of Virtua Racing for the Sega 32X (optimization in progress) | 184 | 🟢 | Assembly |
| [goldenballoon](https://github.com/akratch/goldenballoon) | Native and browser port of the 1997 N64 kart racer Diddy Kong Racing | 181 | 🟢 | C |
| [N64ModernRuntime](https://github.com/N64Recomp/N64ModernRuntime) | Runtime for traditional ports and recompilations of N64 games | 181 | 🟢 | C++ |
| [doaxvb-re](https://github.com/NoRain211/doaxvb-re) | Dead or Alive Xtreme Beach Volleyball original-Xbox static recompilation | 179 | 🟢 | C |
| [ModernGekko](https://github.com/ExpansionPak/ModernGekko) | Runtime for recompilations of GameCube games | 172 | 🟢 | C++ |
| [Parasite Eve HD Remaster](https://github.com/faligame/Parasite-Eve-HD-Remaster) | Recomp and enhancement of the PS1 game Parasite Eve. | 172 | 🟢 |  |
| [HarvestMoon64Recomp](https://github.com/HarvestMoon64Recomp/HarvestMoon64Recomp) | PC Port of Harvest Moon 64 made using N64: Recompiled (Windows/Linux/Mac) | 169 | 🟢 | C++ |
| [DPRecomp](https://github.com/LittleBitUA/DPRecomp) | Deadly Premonition Xbox 360 static recompilation | 165 | 🟢 | C++ |
| [RingOut](https://github.com/jackpoison-prog/RingOut) | Native PC port of a GameCube fighting game via static recompilation | 164 | 🟢 | C |
| [Banjo-Kazooie: Nuts & Bolts](https://github.com/masterspike52/reNut) | Xbox 360 static recompilation of Banjo-Kazooie: Nuts & Bolts | 160 | 🟢 | C++ |
| [SDOJ-Recomp](https://github.com/eandis/SDOJ-Recomp) | SDOJ-Recomp | 157 | 🟢 | C++ |
| [Dr. Mario 64 Recomp Plus](https://github.com/theboy181/drmario64_recomp_plus) | Dr. Mario 64 static recompilation with 4-player support | 154 | 🟢 | C++ |
| [OpenXWA](https://github.com/elyosh/OpenXWA) | Open-source recomp of X-Wing Alliance. | 154 | 🟢 | C |
| [Initial-D-Arcade-Stage-3-Native-SH-4-Recompilation-WIP-](https://github.com/distilledorion-sketch/Initial-D-Arcade-Stage-3-Native-SH-4-Recompilation-WIP-) | Native SH-4 AOT recompilation of Initial D Arcade Stage 3 (NAOMI 2) — BIOS-free Vulkan public early demo (WIP). | 152 | 🟢 | C++ |
| [SwitchWakerHD](https://github.com/centollOS/SwitchWakerHD) | Wind Waker HD (Wii U) static recompilation for Nintendo Switch, deko3d renderer. Requires your own game dump. | 151 | 🟢 | C++ |
| [sms-pc-port](https://github.com/chasem-dev/sms-pc-port) | Native PC port of Super Mario Sunshine | 147 | 🟢 | C++ |
| [F-15 II](https://github.com/neuviemeporte/f15se2-re) | Recomp of MicroProse F-15 II. | 145 | 🟢 | C |
| [Xbox360-Native-Ports](https://github.com/CrownParkComputing/Xbox360-Native-Ports) | Xbox 360 titles recompiled to native Linux with Vulkan renderer; launchers only | 145 | 🟢 | C++ |
| [NFSMW-Recompiled](https://github.com/madelrandel-blip/NFSMW-Recompiled) | Static native recompilation of Need for Speed: Most Wanted (Xbox 360) | 142 | 🟢 | C++ |
| [Crash Team Racing: Turbocharged](https://github.com/CameronRedmore/Crash-Team-Racing-Turbocharged) | CTR PC source port with native 3D renderer and high frame rates | 140 | 🟢 | C |
| [YuGiOhForbiddenMemoriesRecomp](https://github.com/Unchiga/YuGiOhForbiddenMemoriesRecomp) | Static recompilation of Yu-Gi-Oh! Forbidden Memories (PS1) into a native executable - with a live duel-rank meter, a... | 140 | 🟢 | C |
| [Black-2006-Recomp](https://github.com/portingpete/Black-2006-Recomp) | Native Windows static recompilation of BLACK (2006) for the original Xbox | 138 | 🟢 | C |
| [snesrecomp](https://github.com/RetroPortingToolKit/snesrecomp) | Super Nintendo static recompiler ecosystem | 138 | 🟢 | C |
| [DBZ1](https://github.com/WistfulHopes/DBZ1) | Dragon Ball Z Budokai HD Recompiled | 130 | 🟢 | C++ |
| [Mercenaries-Recompiled](https://github.com/KraftMacAndChee/Mercenaries-Recompiled) | Recompilation of Mercenaries: Playground of Destruction | 129 | 🟢 | C |
| [AloneInTheDarkReHaunted](https://github.com/spacefarergames/AloneInTheDarkReHaunted) | A heavily enhanced port and dynamic recomp of Alone In The Dark 1, with Textured Models, HD-4K background replacement... | 127 | 🟢 | C++ |
| [burnout3-pc](https://github.com/danielgomesvieira2000/burnout3-pc) | Burnout 3: Takedown as a native Windows port via a PS2 decompilation toolchain | 127 | 🟢 | C++ |
| [BMHeroRecomp](https://github.com/RevoSucks/BMHeroRecomp) | Bomberman Hero static recompilation with mod support | 126 | 🟢 | C++ |
| [DKC3Recomp](https://github.com/elliotttate/DKC3Recomp) | Native recompilation of Donkey Kong Country 3 (SNES) | 126 | 🟢 | C |
| [projectreach](https://github.com/chrissotraidis/projectreach) | Halo: Combat Evolved on iPhone, iPad and Mac. The Xbox edition with online matches of up to 128 players and the origi... | 126 | 🟢 | C |
| [Flame](https://github.com/DiaLight/Flame) | Dungeon Keeper II partial recompilation with bug fixes. | 125 | 🟢 | C++ |
| [khdays-port](https://github.com/Yokimitsuro/khdays-port) | Experimental native PC runtime for Kingdom Hearts 358/2 Days | 124 | 🟢 | C |
| [RaceWave46](https://github.com/DomazinUS/RaceWave46) | AI-assisted Wave Race 64 recompilation for Windows | 123 | 🟢 | C++ |
| [melee-unlocked](https://github.com/Hero88go/melee-unlocked) | Native Windows source port of Super Smash Bros. Melee built from its decompiled C source | 121 | 🟢 | C++ |
| [SuperMarioWorldRecomp](https://github.com/mstan/SuperMarioWorldRecomp) | Super Mario World recompiled using snesrecomp | 120 | 🟢 | C |
| [nfsu2-recompiled](https://github.com/codepdbh/nfsu2-recompiled) | Static recompilation of Need for Speed Underground 2 (PC) | 119 | 🟢 | C++ |
| [god-of-war-recomp](https://github.com/KIexster/god-of-war-recomp) | Native PC port of God of War (PS2) via static recompilation with PS2Recomp | 116 | 🟢 | C++ |
| [Phase Distorter](https://github.com/TheRunaway5/Phase-Distorter) | Native C++20 PC port of EarthBound / Mother 2 for Linux and Windows | 115 | 🟢 | C++ |
| [Snap64Recomp](https://github.com/JackandBeans/Snap64Recomp) | Pokémon Snap static recompilation | 115 | 🟢 | C++ |
| [beanRecomp](https://github.com/Fable2Recomp/beanRecomp) | A static Recomp of 007 Goldeneye Remaster XBLA | 114 | 🟡 | C++ |
| [OpenXW](https://github.com/elyosh/OpenXW) | Open-source recomp of X-Wing. | 114 | 🟢 | C |
| [skate3-ios-setup](https://github.com/andrewnakas/skate3-ios-setup) | Builds the Skate 3 recompilation for iOS from your own disc image | 114 | 🟢 | Shell |
| [ValkyrieRecomp](https://github.com/Ed1z19/ValkyrieRecomp) | Native PC recompilation of Valkyrie Profile (PS1) | 112 | 🟢 | Python |
| [psxrecomp-ports](https://github.com/alexbeavs-ps1-ports/psxrecomp-ports) | Unofficial noncommercial PlayStation recompilation releases | 109 | 🟢 | PowerShell |
| [snowboardkids2-recomp](https://github.com/cdlewis/snowboardkids2-recomp) | Snowboard Kids 2 static recompilation with mod support | 109 | 🟢 | C |
| [silent-hill-pc-nightly](https://github.com/SlickAmogus/silent-hill-pc-nightly) | Nightly builds of a Silent Hill 1 PC port based on the PSX decompilation | 102 | 🟢 |  |
| [SSSV_Recomp](https://github.com/Cellenseres/SSSV_Recomp) | Space Station Silicon Valley static recompilation | 102 | 🟢 | C++ |
| [mw2-recompiled](https://github.com/PaulCombal/mw2-recompiled) | Call of Duty: Modern Warfare 2 (2009) for Xbox 360 recompiled for Windows & Linux | 100 | 🟢 | C++ |
| [BT3-Recomp](https://github.com/z3xox/BT3-Recomp) | Dragon Ball Z: Budokai Tenkaichi 3 PC port via static recompilation | 99 | 🟢 | C++ |
| [FFTARecomp](https://github.com/Jorge262007/FFTARecomp) | Native Windows port of Final Fantasy Tactics Advance (GBA) with widescreen | 99 | 🟢 | Rust |
| [RidgeRacer6-Recompilation](https://github.com/Sirhalo23/RidgeRacer6-Recompilation) | Recompilation of Ridge Racer 6 (Xbox 360) for PC | 98 | 🟢 | C++ |
| [Ace-Combat-5-Static-recompilation](https://github.com/sal063/Ace-Combat-5-Static-recompilation) | Static recompilation of Ace Combat 5 with native rendering | 97 | 🟢 | C |
| [ConkerBFDReloaded](https://github.com/DahSidiAbdallah/ConkerBFDReloaded) | Conker's Bad Fur Day running natively on PC: an N64 recompilation with a Classic mode true to the N64 and a Modern mo... | 97 | 🟢 | C++ |
| [driftdroid](https://github.com/dorPXP/driftdroid) | A native Android port of Mario Kart Wii and Retro Rewind. Fast, easy. | 96 | 🟢 | C++ |
| [wwe-svr2011-pc](https://github.com/KaikoClanworth1/wwe-svr2011-pc) | Unofficial native PC port of WWE SmackDown vs. Raw 2011 (Xbox 360). Bring your own disc. | 96 | 🟢 | C++ |
| [fm4-recomp](https://github.com/Alexbeav/fm4-recomp) | Experimental static recompilation of Forza Motorsport 4 using ReXGlue. No game files included. | 95 | 🟢 | PowerShell |
| [mcla-recomp](https://github.com/holdmysocks/mcla-recomp) | Static recompilation of Midnight Club: Los Angeles (Xbox 360) for PC and PS5 | 94 | 🟢 | C++ |
| [nfs-most-wanted-mac](https://github.com/elforeign/nfs-most-wanted-mac) | Need for Speed: Most Wanted native on Apple Silicon via static recompilation | 94 | 🟢 | C++ |
| [Roller](https://github.com/FatalDecomp/ROLLER) | Recomp of the game Whiplash/Fatal Racing. Adds enhancements. Playable on PC or online. | 94 | 🟢 | C |
| [Ultima 7 Decomp](https://github.com/Kitrinx/Ultima7_Decomp) | Recomp of Ultima 7. Bit exact to original. | 94 | 🟢 | C |
| [Dead Rising 2: Case Zero Recomp](https://github.com/wivi514/Dead_Rising_2_Case_Zero_Xenon_Recomp) | Dead Rising 2: Case Zero Xbox 360 static recompilation | 93 | 🟢 | C++ |
| [GalaxyQuest](https://github.com/bigmak94/GalaxyQuest) | Super Mario Galaxy native VR port for Meta Quest 3 | 93 | 🟢 | C++ |
| [Max_Vita](https://github.com/fgsfdsfgs/max_vita) | Tool for Max Payne game data (osgameclones) (C) | 93 | 🔴 | C |
| [SARecomp](https://github.com/sonicfreak1337/SARecomp) | A fully playable, work-in-progress native Sonic Adventure port for Windows, Linux and Steam Deck. Powered by KatanaRe... | 93 | 🟢 | C++ |
| [UFO50AndroidUnofficial](https://github.com/Skyline969/UFO50AndroidUnofficial) | Tool to build your own Android version of UFO 50 | 90 | 🟡 | Shell |
| [Wave Race 64 Recomp](https://github.com/danielgomesvieira2000/wave-race-64-recomp) | Native PC port of Wave Race 64 via N64 static recompilation | 90 | 🟢 | C++ |
| [Theft4](https://github.com/KoreanSeats1/Theft4) | Experimental static AOT recompilation of GTA IV's Xbox 360 build for ARM | 89 | 🟢 | C++ |
| [Free-Riders-Recompiled](https://github.com/YuutaTsubasa/Free-Riders-Recompiled) | Unofficial static recompilation of Sonic Free Riders for Windows, Linux and Android, with controller/keyboard support... | 88 | 🟢 | C++ |
| [Xerenge](https://github.com/shipa-2/Xerenge) | Burnout Revenge recompilation based on ReXGlue | 87 | 🟢 | C++ |
| [3dpinball-nds](https://github.com/headshot2017/3dpinball-nds) | Nintendo DS port of the Space Cadet Pinball decompilation | 86 | 🟡 | C++ |
| [banjo-tooie-scurvy-dog-port](https://github.com/some-scurvy-dog/banjo-tooie-scurvy-dog-port) | Banjo-Tooie Recompiled: a native Windows PC port with widescreen, resolution and FPS options, controller support, and... | 86 | 🟢 | C++ |
| [Crash2Recomp](https://github.com/Zumbo06/Crash2Recomp) | Crash Bandicoot 2 (PS1) translated to native code instead of emulated | 86 | 🟢 | Python |
| [goldeneye-metal](https://github.com/ysrdevs/goldeneye-metal) | Experimental source-only static recompilation of GoldenEye 007 | 86 | 🟢 | C |
| [OpenTricky](https://github.com/GiZcesi/OpenTricky) | OpenTricky is an unofficial PC port of SSX Tricky, made by static recompilation. Bring your own disc. | 86 | 🟢 | C |
| [Dead Rising 2: Case West Recomp](https://github.com/wivi514/Dead_Rising_2_Case_West_Xenon_Recomp) | Dead Rising 2: Case West Xbox 360 static recompilation | 85 | 🟢 | C++ |
| [wwe13-recomp](https://github.com/PromethenDev/wwe13-recomp) | Static recompilation of WWE '13 (Xbox 360) for Windows and Linux via ReXGlue | 85 | 🟢 | C++ |
| [lost-odyssey-hd-remaster](https://github.com/faligame/lost-odyssey-hd-remaster) | Lost Odyssey HD Remaster: a native PC build of Lost Odyssey (Xbox 360) via static recompilation. 720p to 4K with an e... | 84 | 🗄️ | C |
| [oracles-decomp](https://github.com/kirby-letsgo/oracles-decomp) | Native app for the Game Boy Color Zelda Oracle games | 84 | 🟢 | C |
| [hercules-recompiled](https://github.com/obaidr1/hercules-recompiled) | Native PC port and decompilation of Disney's Hercules (PlayStation, 1997) | 83 | 🟢 | Python |
| [Earthworm Jim HD: Recompiled](https://github.com/TekRantGaming/earthworm-jim-hd-recompiled) | Earthworm Jim HD (XBLA) static recompilation | 81 | 🟢 | C++ |
| [Estacado-The-Darkness-Recomp](https://github.com/invinceble55-wq/Estacado-The-Darkness-Recomp) | Estacado: a native PC recompilation of The Darkness (Xbox 360). Unofficial fan port; bring your own copy of the game. | 81 | 🟢 | C++ |
| [mk8-recomp](https://github.com/dougchansan/mk8-recomp) | Static recompilation of Mario Kart 8 AArch64 code to native x86-64 | 81 | 🟢 | C++ |
| [Ace-Combat-X-Recompilation](https://github.com/sal063/Ace-Combat-X-Recompilation) | Static recompilation of ACE COMBAT X with a native renderer | 80 | 🟢 | C |
| [Pilotwings 64 Recomp](https://github.com/danielgomesvieira2000/pilotwings-64-recomp) | Native PC port of Pilotwings 64 statically recompiled with N64Recomp, widescreen and high FPS | 79 | 🟢 | C++ |
| [halo-ce-vita](https://github.com/BirchWoodGod/halo-ce-vita) | PS Vita port of Halo: Combat Evolved built on the decompilation | 77 | 🟢 | C |
| [Ogre Battle 64 Recompiled](https://github.com/lfarroco/ogre-battle-64-recomp) | Static recompilation of Ogre Battle 64 to native PC | 77 | 🟢 | Assembly |
| [ArmyOfTwoRecomp](https://github.com/nikolaygorb/ArmyOfTwoRecomp) | Army of Two (Army of 2) 2008 [Xbox360] game static recompilation project based on RexGlue-SDK | 76 | 🟢 | C++ |
| [gears-judgement-recomp](https://github.com/OverkillLabs3/gears-judgement-recomp) | Native Windows recompilation of Gears of War: Judgment (Xbox 360) | 74 | 🟢 | C++ |
| [DefJamFFNY-recomp](https://github.com/vyanhursky/DefJamFFNY-recomp) | Def Jam: Fight for NY PC port — static recompilation of the original Xbox game for native Windows and macOS (Direct3D... | 73 | 🟢 | Python |
| [naruto-rise-recomp](https://github.com/jorjbarbosa/naruto-rise-recomp) | Static PC recompilation of Naruto: Rise of a Ninja (Xbox 360) via ReXGlue | 73 | 🟢 | C++ |
| [Project-RE-Visited-RE3](https://github.com/BrazilianHobbyist/Project-RE-Visited-RE3) | Static recompilation and native PC port of Resident Evil 3: Nemesis (PS1) | 73 | 🟢 | C++ |
| [Rayman3Readvanced](https://github.com/RayCarrot/Rayman3Readvanced) | PC port of Rayman 3 GBA | 73 | 🟢 | C# |
| [wet-recomp](https://github.com/Supermedo/wet-recomp) | Fan PC port of WET (Xbox 360) via ReXGlue static recompilation | 72 | 🟢 | C# |
| [foxhollow](https://github.com/JackPriceBurns/foxhollow) | Star Fox Adventures decompilation powering the FoxHollow native PC port | 71 | 🟢 | C |
| [MarioKartSuperCircuitRecomp](https://github.com/mstan/MarioKartSuperCircuitRecomp) | Static recompilation of Mario Kart: Super Circuit | 69 | 🟢 | PowerShell |
| [RoadRash64Recompiled](https://github.com/linkssy2/RoadRash64Recompiled) | Unofficial PC recompilation of Road Rash 64 | 69 | 🟢 | C++ |
| [BloodyRoar2Recomp](https://github.com/novapowers0/BloodyRoar2Recomp) | Bloody Roar II PlayStation static recompilation | 68 | 🟢 | C |
| [fukami](https://github.com/danisandoval/fukami) | Native macOS / Steam Deck port of Ridge Racer V by static recompilation | 68 | 🟢 | C++ |
| [NFS-CARBON-360-ANDROID-RECOMP](https://github.com/codepdbh/NFS-CARBON-360-ANDROID-RECOMP) | Static recompilation of Need for Speed Carbon (Xbox 360) for Windows and Android | 68 | 🟢 | JavaScript |
| [DQ8-Recompiled](https://github.com/Sinan-Karakaya/DQ8-Recompiled) | Recompilation of Dragon Quest VIII (PS2) to run natively on PC and Mac | 67 | 🟢 | C++ |
| [dusklight](https://github.com/HayatoG/dusklight) | Switch port of the Twilight Princess decompilation | 67 | 🟢 | C++ |
| [OpenCMR2](https://github.com/pablocpas/OpenCMR2) | Native SDL3 port of Colin McRae Rally 2.0 built from the CMR2Decomp decompilation | 67 | 🟢 | C++ |
| [beetle-adventure-racing-recomp](https://github.com/danielgomesvieira2000/beetle-adventure-racing-recomp) | Static recompilation port of Beetle Adventure Racing (N64) to native PC, with widescreen, high-FPS and modern input | 66 | 🟢 | C++ |
| [DBZ-Burst-Limit-Recompiled](https://github.com/iExplosiveRage/DBZ-Burst-Limit-Recompiled) | Dragon Ball Z: Burst Limit Recompiled - native PC port via ReXGlue static recompilation | 66 | 🟢 | C++ |
| [Project-2099](https://github.com/GenryTheFox0/Project-2099) | Spider-Man: Edge of Time Xbox 360 static recompilation | 66 | 🟢 | C# |
| [smash64r](https://github.com/zestydevy/smash64r) | Static recompilation of Super Smash Bros. for PC (Windows/Linux) | 66 | 🟡 | C++ |
| [SWROTS-PC](https://github.com/jedijosh920/SWROTS-PC) | Unofficial native Windows port of Star Wars Episode III: Revenge of the Sith (Xbox) | 66 | 🟢 | C++ |
| [OpenCrossing-Anbernic](https://github.com/TechProGabe/OpenCrossing-Anbernic) | Animal Crossing running natively on Anbernic handhelds | 64 | 🟢 | C |
| [OpenPhantom](https://github.com/OpenPhantom/OpenPhantom) | Star Wars Episode I: The Phantom Menace (1999) PC modernized with online co-op multiplayer for up to 4 players. Play... | 64 | 🟢 | C |
| [SpaceRangersHD_FPC](https://github.com/pakompom/SpaceRangersHD_FPC) | Cross-platform port of Space Rangers HD: A War Apart based on its decompilation | 64 | 🟢 | Pascal |
| [skate2-recompile-pc](https://github.com/christianortel/skate2-recompile-pc) | Community Windows PC port of Skate 2 (Xbox 360) built with ReXGlue static recompilation | 63 | 🟢 | PowerShell |
| [Chameleon Twist: Recompiled](https://github.com/Rainchus/ChameleonTwist1-JP-Recomp) | Chameleon Twist static recompilation | 62 | 🟡 | C++ |
| [Underworld Exhumed](https://github.com/abedegno/underworld-exhumed) | Bit-exact recomp of Ultima Underworld I and II. | 62 | 🟢 | C |
| [SMB-Vanilla](https://github.com/nukep/SMB-Vanilla) | C decompilation and port of NES Super Mario Bros and The Lost Levels | 61 | 🟢 | C |
| [KameoRePowered](https://github.com/birabittoh/KameoRePowered) | Static recompilation of Kameo: Elements of Power (Xbox 360) for Windows and Linux | 60 | 🟢 | Python |
| [TWIPE_00Sheven](https://github.com/riseio/TWIPE_00Sheven) | Static recompilation of the N64 game The World Is Not Enough | 60 | 🟢 | C++ |
| [sk82-recomp](https://github.com/Skate-2-Team/sk82-recomp) | A static recompilation of Skate 2 to build a PC port. | 59 | 🗄️ | C++ |
| [xenogears-recomp](https://github.com/OpokXeno/xenogears-recomp) | Static recompilation of Xenogears for PC | 59 | 🟢 | C |
| [Open Annihilation](https://github.com/open-annihilation/open-annihilation) | Recomp of Total Annihilation and Total Annihilation: Kingdoms (RTS). | 58 | 🟢 | C++ |
| [iPodClickWheelRecomps](https://github.com/DogParty/iPodClickWheelRecomps) | An assortment of iPod Classic games that have been recompiled to run on modern systems | 57 | 🟢 | Rust |
| [mkwii-ps5](https://github.com/Phi1ow/mkwii-ps5) | Mario Kart Wii PAL on PS5 via native static recompilation | 57 | 🟢 | C++ |
| [Tekken3Recompiled](https://github.com/FishB0nes98/Tekken3Recompiled) | Tekken 3 hybrid recompilation preview with Jun Kazama, widescreen, custom skins and local asset import tools. | 56 | 🟢 | C++ |
| [NaughtyBear_ReStuff](https://github.com/MaxDeadBear/NaughtyBear_ReStuff) | NaughtyBear_ReStuff | 55 | 🟢 | C++ |
| [P3P3DS](https://github.com/endercodezz/P3P3DS) | Persona 3 Portable port for the New Nintendo 3DS | 55 | 🟢 | C++ |
| [Rock Band 3 (Xbox 360)](https://github.com/ihatecompvir/band3_recomp) | Xbox 360 static recompilation of Rock Band 3 (Xbox 360) | 55 | 🟢 | C++ |
| [wc1-re](https://github.com/neuromancer/wc1-re) | Open-source recomp of Wing Commander I. | 54 | 🟢 | C |
| [WindWakerHD-Android-Plus](https://github.com/Nycolazs/WindWakerHD-Android-Plus) | The Legend of Zelda: The Wind Waker HD natively on Android (static recompilation, Vulkan). Built-in Brazilian Portugu... | 54 | 🟢 | C++ |
| [OpenXvT](https://github.com/elyosh/OpenXvT) | Open-source recomp of X-Wing vs Tie Fighter. | 52 | 🟢 | C |
| [regaiden-recomp](https://github.com/sergiomanzur/regaiden-recomp) | Native static recompilation of Resident Evil Gaiden (GBC) for PC | 52 | 🟢 | C |
| [TooTawersRecomp](https://github.com/Gumpolas/TooTawersRecomp) | Native Windows port of The Lord of the Rings: The Two Towers (Xbox, 2002) via static recompilation | 52 | 🟢 | C |
| [NHL Legacy Recomp](https://github.com/puckhead73/nhl-legacy-recomp) | Xbox 360 NHL Legacy recompiled to PC with ReXGlue | 51 | 🟢 | C++ |
| [rush2recompiled](https://github.com/bryantmh/rush2recompiled) | Recompilation of the N64 game Rush 2 | 51 | 🟢 | C++ |
| [VandalHearts-PcPort](https://github.com/HalmyLyseas/VandalHearts-PcPort) | Vandal Hearts native PC port based on a matching decompilation | 50 | 🟢 | C |
| [ac3-remix](https://github.com/i5han/ac3-remix) | PC port and remaster of Ace Combat 3: Electrosphere | 49 | 🟢 |  |
| [mscharged-port](https://github.com/previouslevelgames/recharged) | Mario Strikers Charged ported to PC, Mac and Linux from decompiled code | 49 | 🟢 | C++ |
| [asuras-wrath-recomp](https://github.com/PauloUbirajara/asuras-wrath-recomp) | Recomp of Asura's Wrath using RexGlue for PC (wip) | 48 | 🟢 | C++ |
| [IsaacRecomp](https://github.com/whylurking/IsaacRecomp) | Native C++ recompilation of The Binding of Isaac (Flash) for Windows, Linux and Switch | 48 | 🟢 | C++ |
| [MojoRecomp](https://github.com/OAleex/MojoRecomp) | Native PC recompilation project for Crash of the Titans | 48 | 🟢 | C++ |
| [pokeemerald-3d](https://github.com/tripplyons/pokeemerald-3d) | Pokemon Emerald in 3D (in WebAssembly) | 48 | 🟢 | C |
| [sf64-dc](https://github.com/jnmartin84/sf64-dc) | Sega Dreamcast port of the Star Fox 64 decompilation | 48 | 🟢 | C |
| [th06-sdl2](https://github.com/CNTianQi233/th06-sdl2) | Rebuild of the Touhou 6 decompilation on SDL2 and OpenGL | 48 | 🟢 | C++ |
| [GSRecomp](https://github.com/Shmargus/GSRecomp) | Golden Sun GBA static recompilation | 47 | 🟢 | C++ |
| [Kirby64Recomp](https://github.com/Kirby64Ret/Kirby64Recomp) | Kirby 64 Recomp (ok fine i'll use cmake) | 47 | 🟢 | C++ |
| [Little Planet](https://github.com/carlosrmz009/littleplanet) | Sonic CD (Mega-CD) byte-identical disassembly plus static recompilation into a native PC port | 47 | 🟢 | Assembly |
| [Genesis 68K Static Recompiler](https://github.com/mstan/segagenesisrecomp) | Sega Genesis / Mega Drive game static recompiler ecosystem · Part of the R.A.I.D. community | 46 | 🟢 | C |
| [Re-Cherry](https://github.com/MaxDeadBear/Re-Cherry) | Re-Cherry | 46 | 🟢 | C++ |
| [SM2-Recomp](https://github.com/SirSymo/SM2-Recomp) | Native recompilation of Spider-Man 2 (original Xbox) | 46 | 🟢 |  |
| [automobililamborghini-recomp](https://github.com/alondero/automobililamborghini-recomp) | Automobili Lamborghini (N64) static recompilation | 45 | 🟢 | C++ |
| [MegaManX2Recomp](https://github.com/mstan/MegaManX2Recomp) | Static recompilation of Mega Man X2 (SNES) | 45 | 🟢 | Python |
| [RB2](https://github.com/WistfulHopes/RB2) | Dragon Ball Raging Blast 2 Recompiled | 44 | 🟢 | C++ |
| [vf2-recomp](https://github.com/mr-finster/vf2-recomp) | Virtua Fighter 2 (Sega Model 2) arcade i960 program recompiled to native code for Mac, Windows, Steam Deck | 44 | 🟢 | C++ |
| [ChaotixRecompiled](https://github.com/YuutaTsubasa/ChaotixRecompiled) | Static recompilation of the Sega 32X game Knuckles' Chaotix into native C++ (Windows/Linux/macOS/Android), with true... | 43 | 🟢 | C++ |
| [Destroy All Humans! Path of the Furon](https://github.com/masterspike52/reDAHM) | Xbox 360 static recompilation of Destroy All Humans! Path of the Furon | 43 | 🟢 | C++ |
| [redalert2-recomp](https://github.com/sp00nznet/redalert2-recomp) | Static recompilation of Command & Conquer: Red Alert 2 / Yuri's Revenge (Westwood, 2000-01) to native C, with the rem... | 43 | 🟢 | C |
| [Halo 3 (Delta)](https://github.com/twist84/halo3_cache_release_recomp) | Xbox 360 static recompilation of Halo 3 (Delta) | 42 | 🟢 | C++ |
| [PlayStunts](https://github.com/ACatWithEbola/playstunts) | Recomp of Stunts to TypeScript, playable online. | 42 | 🟢 | TypeScript |
| [pokerecomp](https://github.com/Decryptu/pokerecomp) | A native Godot 4 reimplementation of the Gen 1 and 2 Game Boy Color games. Not an emulator, bring your own ROM. | 42 | 🟢 | GDScript |
| [Ultimate-Mortal-Kombat-3-iOS-Recomp](https://github.com/MaryNCRT/Ultimate-Mortal-Kombat-3-iOS-Decompiled) | Ultimate Mortal Kombat 3 (iOS, EA Mobile 2011), fully decompiled: all 2,572 game functions are readable C, checked ag... | 42 | 🟢 | C |
| [WCWvsNWOWorldTourRecomp](https://github.com/jessetbh/WCWvsNWOWorldTourRecomp) | WCW vs. nWo: World Tour N64 static recompilation | 42 | 🟢 | C++ |
| [aerogauge-recomp](https://github.com/alondero/aerogauge-recomp) | Static recompilation of AeroGauge for the Nintendo 64 | 41 | 🟢 | C++ |
| [Geometry Wars: Retro Evolved 2 Recompiled](https://github.com/saulob/geometry-wars-retro-evolved-2-recompiled) | Native PC port of Geometry Wars: Retro Evolved 2 (Xbox 360) via static recompilation | 41 | 🟢 | C++ |
| [MKVDCU-Recomp](https://github.com/KawaiiBunga/MKVDCU-Recomp) | Unofficial PC recompilation of Mortal Kombat vs. DC Universe | 41 | 🟢 | C++ |
| [.hack//Recompilation](https://github.com/dothacktranslate/dothack-recompilation) | Native recompilation project for the PS2 .hack//IMOQ quadrilogy | 40 | 🟢 | Python |
| [CTW-Native](https://github.com/official-kryo-to/ctw-native) | Recomp of GTA: Chinatown Wars from Android to Windows. | 40 | 🟢 | C++ |
| [nfs-carbon-recomp](https://github.com/Sampreeth004/nfs-carbon-recomp) | Static recompilation of Need for Speed: Carbon (Xbox 360) to native C++ | 40 | 🟢 | C++ |
| [Project8Recomp](https://github.com/theokyr/Project8Recomp) | Tony Hawk's Project 8 Xbox 360 static recompilation | 40 | 🟢 | C++ |
| [re-wor](https://github.com/ronniecloud/re-wor) | Native recompilation of Guitar Hero: Warriors of Rock (Xbox 360) for PC | 40 | 🟢 | C++ |
| [Rocket-R](https://github.com/ThatGuyMcd/Rocket-R) | Rocket: Robot on Wheels static recompilation | 40 | 🟢 | C++ |
| [FZeroRecomp](https://github.com/craigshaw/FZeroRecomp) | Static recompilation of F-Zero to native PC | 39 | 🟢 | C |
| [the-browsing-of-isaac](https://github.com/chiikabu/the-browsing-of-isaac) | The Binding of Isaac: Repentance+ recompiled to WebAssembly, playable in the browser. | 39 | 🟢 | JavaScript |
| [tomodachi-ltd-recomp](https://github.com/RussoPhone/tomodachi-ltd-recomp) | Native PC build of Tomodachi Life: Living the Dream via static recompilation. Bring your own copy — no game files inc... | 39 | 🟢 | Python |
| [Yakuza-Dead-Souls-EX](https://github.com/canersaka/Yakuza-Dead-Souls-Recompiled) | Yakuza: Dead Souls recompilation effort | 39 | 🟢 | C |
| [DQIV-Recompiled](https://github.com/GoldieLeGenie/DQIV-Recompiled) | Native PC version of Dragon Quest IV (DS) via recompilation | 38 | 🟢 | C++ |
| [skate3-android](https://github.com/andrewnakas/skate3-android) | Skate 3 on Android via native recompilation | 38 | 🟢 | Kotlin |
| [SotE-Recomp](https://github.com/GTTeancum/SotE-Recomp) | Static recompilation of Star Wars: Shadows of the Empire (N64) | 38 | 🟢 | C++ |
| [syphon-filter-2-recomp](https://github.com/alexbeavs-ps1-ports/syphon-filter-2-recomp) | Experimental Syphon Filter 2 static recompilation for Windows | 38 | 🟢 | Python |
| [SanRecomp](https://github.com/OZORDI/SanRecomp) | Unofficial PC port of GTA V (Xbox 360) through static recompilation | 37 | 🟢 | C++ |
| [skyroads-sdl](https://github.com/pedrocatalao/skyroads-sdl) | SkyRoads (1993) reverse-engineered and ported natively to SDL2 | 37 | 🟢 | C |
| [3dpinball-dc](https://github.com/headshot2017/3dpinball-dc) | Port of the Space Cadet Pinball decompilation to Dreamcast | 36 | 🟡 | C++ |
| [3dpinball-ps2](https://github.com/headshot2017/3dpinball-ps2) | Port of the Space Cadet Pinball decompilation to PlayStation 2 | 36 | 🟡 | C++ |
| [infinite-undiscovery-recomp](https://github.com/doc-haz/infinite-undiscovery-recomp) | Native PC recompilation of Infinite Undiscovery | 36 | 🟢 | C++ |
| [vf1-recomp](https://github.com/mr-finster/vf1-recomp) | Virtua Fighter (Sega Model 1) statically recompiled for Mac, Windows and Steam Deck | 36 | 🟢 | C++ |
| [WetRecomp](https://github.com/nikolaygorb/WetRecomp) | Wet [Xbox360] game static recompilation project based on RexGlue-SDK | 36 | 🟢 | C++ |
| [WWFNoMercyRecomp](https://github.com/jessetbh/WWFNoMercyRecomp) | WWF No Mercy N64 static recompilation | 36 | 🟢 | C |
| [gow2-recomp](https://github.com/andrebrumdev/gow2-recomp) | God of War II HD static recompilation — curated work artifacts (lift boundaries, SPU lift sources, scripts, findings)... | 35 | 🟢 | Python |
| [halo-ce-anbernic-rg35xx](https://github.com/kirklandsig/halo-ce-anbernic-rg35xx) | Halo: Combat Evolved running natively on Anbernic RG35XX H handhelds | 35 | 🟢 | C |
| [outrun2-decomp](https://github.com/r4dius/outrun2-decomp) | OutRun 2006: Coast 2 Coast decompilation ported to many platforms | 35 | 🟢 | C++ |
| [urban-reign-recomp](https://github.com/thiagordsfx/urban-reign-recomp) | Urban Reign (PS2) static recompilation: native PC port with 60 FPS and high resolution | 35 | 🟢 | C++ |
| [EcstaticaRecompiled](https://github.com/spacefarergames/EcstaticaRecompiled) | This is a recomplimation and modern port of Ecstatica 1 and Ecstatica 2 that runs on modern Windows 10 / 11 systems f... | 34 | 🟢 | Assembly |
| [HuntersRecomp](https://github.com/aabrole/HuntersRecomp) | Metroid Prime Hunters (DS) recompiled to a native dual-screen Android port | 34 | 🟢 | Java |
| [NSMB-Wii-Multiplayer-Recompilation](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation) | Static recompilation of New Super Mario Bros. Wii for Android and Windows | 34 | 🟢 | C++ |
| [Guitar Hero II](https://github.com/YoshiCrystal9/re-gh2) | Xbox 360 static recompilation of Guitar Hero II | 33 | 🟢 | C++ |
| [hard-corps-uprising-recompiled](https://github.com/saulob/hard-corps-uprising-recompiled) | Native PC port of Hard Corps: Uprising (Xbox Live Arcade) via static recompilation, with the TRG launcher | 33 | 🟢 | C++ |
| [OpenSpideyPS1](https://github.com/GTTeancum/SpideyPS1recomp) | Recomp of Spider-Man PS1 and Spider-Man 2: Enter Electro to PC. | 33 | 🟢 | C# |
| [PerfectDarkZeroRecomp](https://github.com/nikolaygorb/PerfectDarkZeroRecomp) | Perfect Dark Zero [Xbox360] game static recompilation project based on RexGlue-SDK | 33 | 🟢 | C++ |
| [beanRecomp](https://github.com/kholdfuzion/beanRecomp) | In-progress recomp repo for Bean | 32 | 🟡 |  |
| [conker64-recompiled](https://github.com/Conker64Recomp/conker64-recompiled) | Native PC port of Conker's Bad Fur Day (N64) via Static MIPS Recompilation. SDL2 engine with 3D UV texturing, N64 aud... | 32 | 🟢 | C |
| [ForzaRecomp](https://github.com/NerunSmarts/ForzaRecomp) | In-progress static recompilation of Forza Horizon 1 | 32 | 🟢 | C++ |
| [MK64 Portable](https://github.com/beckerd/psp_mk64_portable) | Native PSP port of Mario Kart 64 built on the n64decomp/mk64 decompilation | 31 | 🟢 | C |
| [RidgeRacer4Recomp](https://github.com/omegakatana92/RidgeRacer4Recomp) | Native PC port of R4: Ridge Racer Type 4 (PS1) built with PSXRecomp | 31 | 🟢 | PowerShell |
| [DragonBallZBuusFuryRecomp](https://github.com/mstan/DragonBallZBuusFuryRecomp) | Static recompilation of Dragon Ball Z: Buu's Fury with Adaptive Widescreen · Part of the R.A.I.D. community | 30 | 🟢 | C++ |
| [nfs-carbon-mac](https://github.com/vasist15-source/nfs-carbon-mac) | Need for Speed: Carbon (PC) natively on Apple Silicon Macs via static recompilation | 30 | 🟢 | C++ |
| [nfsmw-ios](https://github.com/bep1s69/nfsmw-ios) | Static recompilation port of Need for Speed Most Wanted (Xbox 360) for iOS | 30 | 🟢 | Python |
| [OpenCrossing-Xbox](https://github.com/TechProGabe/OpenCrossing-Xbox) | Native original Xbox port of Animal Crossing built from the GameCube decompilation | 30 | 🟢 | C |
| [betrayal-at-krondor](https://github.com/canassa/betrayal-at-krondor) | Betrayal at Krondor: A byte-perfect recompilation of the 1993 classic. | 29 | 🟢 | Assembly |
| [CafeRecomp](https://github.com/hardkiller2565123123/CafeRecomp) | Wii U static recompilation framework, starting with Breath of the Wild | 29 | 🟢 | C |
| [CV64-Recomp](https://github.com/spacefarergames/CV64-Recomp) | Static Recomp and Remaster of Castlevania 64 | 29 | 🟢 | C++ |
| [DB-Final-Bout-Recomp](https://github.com/novapowers0/DB-Final-Bout-Recomp) | Static recompilation of Dragon Ball GT: Final Bout (PS1) for Windows | 29 | 🟢 | Python |
| [fuc-recomp](https://github.com/elprogramadorloco-arch/fuc-recomp) | Hybrid native Fate/unlimited codes project: PSP static-recompilation/gameplay base with PS2 assets and controls in de... | 29 | 🟢 | C++ |
| [mgb64](https://github.com/akratch/mgb64) | Decompilation-based native PC runtime for GoldenEye 007 | 29 | 🗄️ | C |
| [repentogxm](https://github.com/0xl0cal/repentogxm) | PS Vita port of The Binding of Isaac: Repentance by static recompilation of the PC executable to ARM. | 29 | 🟢 | C |
| [castlevania-chronicles-recomp](https://github.com/Spicywonda/castlevania-chronicles-recomp) | Experimental Castlevania Chronicles (PS1) recompilation | 28 | 🟢 | C# |
| [issd-native](https://github.com/sergiomanzur/issd-native) | Native recompilation of International Superstar Soccer Deluxe (SNES) | 28 | 🟢 | C |
| [nox-decomp](https://github.com/neuromancer/nox-decomp) | Unofficial Linux port of Nox (2000) from decompiled code | 28 | 🗄️ | C |
| [PerfectDarkRemasterRecomp](https://github.com/nikolaygorb/PerfectDarkRemasterRecomp) | Perfect Dark Remaster 2010 [Xbox360] game static recompilation project based on RexGlue-SDK | 28 | 🟢 | C++ |
| [reo](https://github.com/sp00nznet/reo) | Static recompilation of Resident Evil Outbreak for modern Windows | 28 | 🟢 | C++ |
| [sonic-r-android](https://github.com/ZinexDa/sonic-r-android) | Native Android port of the Sonic R PC decompilation with GLES2 renderer | 28 | 🟢 | C |
| [Splatterhouse Recompiled](https://github.com/0c0de/splatterhouse-decomp) | Native PC port of Splatterhouse (2010, Xbox 360) via ReXGlue static recompilation | 28 | 🟢 | C++ |
| [Starfox Recomp](https://github.com/mstan/StarFoxSNESRecomp) | Recomp + enhancement of Starfox (SNES). | 28 | 🟢 | C |
| [WWE-AllStars-Recomp](https://github.com/shaneomac1337/WWE-AllStars-Recomp) | Unofficial Windows version of WWE All Stars (Xbox 360), recompiled with ReXGlue. Bring your own disc image. | 28 | 🟢 | C++ |
| [Birdman64](https://github.com/NoahVl/Birdman64) | Pilotwings 64 as a native PC game for Windows and Linux: widescreen, 144 Hz+, gamepads. Bring your own ROM, no emulator. | 27 | 🟢 | Rust |
| [Mother3Recomp](https://github.com/agray0425/Mother3Recomp) | Static recompilation of MOTHER 3 (GBA) to native PC on the gbarecomp framework | 27 | 🟢 | C++ |
| [Strikers-Quest-MR](https://github.com/LanceSweatpants/Strikers-Quest-MR) | Super Mario Strikers (GameCube) built from its decompilation as a native Meta Quest 3 mixed-reality app | 27 | 🟢 | C++ |
| [wc2-re](https://github.com/neuromancer/wc2-re) | Open-source recomp of Wing Commander II. | 27 | 🟢 | C |
| [xmd-recompiled](https://github.com/florinp93/xmd-recompiled) | Native PC port of X-Men Destiny via static recompilation | 27 | 🟢 | C |
| [annepad](https://github.com/chrissotraidis/annepad) | Pokémon Stadium for iPhone and iPad via static recompilation, with native Metal rendering, touch controls, and ROM-fr... | 26 | 🟢 | Shell |
| [arcade-js](https://github.com/qarl/arcade-js) | Arcade ROMs decompiled to idiomatic JavaScript with LLMs, validated against MAME | 26 | 🟢 | JavaScript |
| [doa3-recomp](https://github.com/parkerallan/doa3-recomp) | Dead or Alive 3 PC Port | 26 | 🟢 | Assembly |
| [MCX360-EDITION](https://github.com/DevZer0D4Y/MCX360-EDITION) | ReXGlue recompilation of Minecraft Xbox 360 Edition running on iOS | 26 | 🟢 | C++ |
| [oot-dc](https://github.com/jnmartin84/oot-dc) | Port of the Ocarina of Time decompilation to the Sega Dreamcast | 26 | 🟢 | C |
| [Simpsons Wrestling Recompiled](https://github.com/TekRantGaming/simpsons-wrestling-recompiled) | Recomp of Simpsons Wrestling (PS1) to PC. | 26 | 🟢 | C++ |
| [WCWnWoRevengeRecomp](https://github.com/jessetbh/WCWnWoRevengeRecomp) | WCW/nWo Revenge N64 static recompilation | 26 | 🟢 | Python |
| [Earthbound Companion](https://github.com/rages4calm/earthbound-companion) | Recomp of Earthbound (SNES) to PC. | 25 | 🟢 | Python |
| [Metal Gear Solid Recompiled](https://github.com/alexbeavs-ps1-ports/metal-gear-solid-recomp) | PSXRecomp native PC port of Metal Gear Solid (PS1) | 25 | 🟢 | Python |
| [OpenJam](https://github.com/GTTeancum/OpenJam) | Native PC port of NBA JAM: On Fire Edition (Xbox 360) via static recompilation | 25 | 🟢 | Python |
| [srw64-recomp](https://github.com/dyzz/srw64-recomp) | Experimental native recompilation of Super Robot Wars 64 with translations and HD mode | 25 | 🟢 | Python |
| [Street-Fighter-EX2-Plus-Recompiled](https://github.com/strider973/Street-Fighter-EX2-Plus-Recompiled) | Static recompilation of Street Fighter EX2 Plus (PS1) | 25 | 🟢 | Python |
| [ffta-recomp](https://github.com/james2doyle/ffta-recomp) | Native recompilation of Final Fantasy Tactics Advance (GBA) built on the gbarecomp framework | 24 | 🟢 | Python |
| [master-chef](https://github.com/mitchaiet/master-chef) | Unofficial native Halo: Combat Evolved for Apple Vision Pro. Immersive panorama, controller support, and visual mods.... | 24 | 🟢 | C |
| [skifree_sdl](https://github.com/jeff-1amstudios/skifree_sdl) | SkiFree decompiled and ported to SDL2 | 24 | 🟡 | C |
| [arwing](https://github.com/carlosrmz009/arwing) | Star Fox recompilation and PC port with quality-of-life improvements | 23 | 🟢 | Assembly |
| [ReShadowTower](https://github.com/JFryy/reshadowtower) | Recompiled native port of Shadow Tower (PS1) with modern PC controls | 23 | 🟢 | Python |
| [snowboardkids-recomp](https://github.com/cdlewis/snowboardkids-recomp) | Native PC port of Snowboard Kids (N64) for Windows, Linux and macOS | 23 | 🟢 | C |
| [ar-recomp](https://github.com/DerrickGold/ar-recomp) | ActRaiser (SNES) recompilation project | 22 | 🟢 | C |
| [demoscene-recomp](https://github.com/treylorswift/demoscene-recomp) | Classic DOS demoscene productions recompiled to run natively in the browser | 22 | 🟢 | JavaScript |
| [moonpearl](https://github.com/DoutorRaposo/moonpearl) | Android port of snesrev/zelda3 (ALttP reimplementation): widescreen, rewind, shaders, MSU-1, save states, controller... | 22 | 🟢 | Kotlin |
| [pspoke](https://github.com/IbrahimIrfan/pspoke) | Pokemon Platinum and SoulSilver running natively on the PSP | 22 | 🟢 | C |
| [Space-Channel-5](https://github.com/ZoomiesZaggy/Space-Channel-5) | Unofficial native Space Channel 5 port for Windows, Linux and macOS. Compiler-free downloads, display options, contro... | 22 | 🟢 | C |
| [twisted-metal-2012-ps3-native-port](https://github.com/franklincg/twisted-metal-2012-ps3-native-port) | Community native PC recompilation of Twisted Metal (2012, PS3) | 22 | 🟢 | C |
| [WWE-SVR2010-RECOMP](https://github.com/nefariousjosiah/WWE-SVR2010-RECOMP) | Native PC port of WWE SmackDown vs. Raw 2010 (Xbox 360) via static recompilation | 22 | 🟢 | C++ |
| [Body Harvest Recompiled](https://github.com/danielgomesvieira2000/body-harvest-recomp) | Native PC port of Body Harvest (N64) built with N64Recomp and RT64 | 21 | 🟢 | C++ |
| [midnightclub](https://github.com/zarif98/midnightclub) | Static recompilation of Midnight Club: Los Angeles (Xbox 360) using rexGlu SDK | 21 | 🟢 | C++ |
| [nfsmw-recomp](https://github.com/veritr1x/nfsmw-recomp) | Recompilation of Need for Speed: Most Wanted (the 2005 PC Black Edition) built on recomp-kit: macOS, iPad, Linux, Win... | 21 | 🟢 | C |
| [WWE-SVR2008-RECOMP](https://github.com/nefariousjosiah/WWE-SVR2008-RECOMP) | Native PC port of WWE SmackDown vs. Raw 2008 (Xbox 360) via static recompilation | 21 | 🟢 | C++ |
| [ArmyOfTwo-Recomp](https://github.com/Genesis5500/ArmyOfTwo-Recomp) | Experimental native PC port of Army of Two (Xbox 360) via ReXGlue static recompilation | 20 | 🟢 | C++ |
| [DAORecomp](https://github.com/96dot/DAORecomp) | Static recompilation of Dragon Age: Origins (Xbox 360) to native PC | 20 | 🟢 | C |
| [defjam_recomp](https://github.com/comoria08/defjam_recomp) | Static recompilation of Def Jam: Fight for NY (Xbox) for Windows | 20 | 🟢 | C |
| [gdx-3ds](https://github.com/cruxxxxxx/gdx-3ds) | Unofficial 3DS port of F-Zero X based on its decompilation | 20 | 🟢 | C |
| [project-1944](https://github.com/zenit2893-cmyk/project-1944) | Unofficial native Windows PC port of Call of Duty 3 (Xbox 360) via static recompilation. Bring your own game. EN · RU... | 20 | 🟢 | Python |
| [stunts-hd](https://github.com/mr-finster/stunts-hd) | Stunts / 4D Sports Driving (DOS, 1990) recompiled for browser and desktop with HD 3D and widescreen | 20 | 🟢 | JavaScript |
| [Test Drive Unlimited](https://github.com/testdriveupgrade/TDURE) | Xbox 360 static recompilation of Test Drive Unlimited | 20 | 🟢 | C++ |
| [weltendaemmerung](https://github.com/s-macke/weltendaemmerung) | Reverse engineering a C64 game with AI and porting it to the web | 20 | 🟢 | Assembly |
| [AkiLauncher](https://github.com/jessetbh/AkiLauncher) | Launcher for the AKI N64 wrestling static recompilations | 19 | 🟢 | C++ |
| [buffy-chaos-bleeds-pc](https://github.com/KaikoClanworth1/buffy-chaos-bleeds-pc) | Unofficial native PC port of Buffy the Vampire Slayer: Chaos Bleeds (Xbox); bring your own disc | 19 | 🟢 | C |
| [FinFanTacRecomp](https://github.com/NJH-1001/FinFanTacRecomp) | PSXRecomp native Windows port of Final Fantasy Tactics (PS1) with 16:9 option | 19 | 🟢 | Python |
| [MindOver-Recomp](https://github.com/Maxilure/MindOver-Recomp) | Unofficial native PC port of Crash: Mind Over Mutant (Xbox 360) via recompilation | 19 | 🟢 | C++ |
| [mm3-recomp](https://github.com/MattSG/mm3-recomp) | Static recompilation of Midtown Madness 3 (Xbox) to native Windows x64 with a Direct3D 11 renderer | 19 | 🟢 | C |
| [jsrf-recomp](https://github.com/andeecollard/jsrf-recomp) | Static recompilation of Jet Set Radio Future (Xbox) to native macOS — playable into chapter 2 at 60 fps via a Direct3... | 18 | 🟢 | C |
| [socom-unzipped](https://github.com/Scotho/socom-unzipped) | SOCOM II: U.S. Navy SEALs, statically recompiled for PC with self-hosted online play | 18 | 🟢 | Python |
| [WWE-SVR2009-RECOMP](https://github.com/nefariousjosiah/WWE-SVR2009-RECOMP) | Native PC port of WWE SmackDown vs. Raw 2009 (Xbox 360) via static recompilation | 18 | 🟢 | C++ |
| [miyoo64](https://github.com/mr-finster/miyoo64) | N64 games built for the Miyoo Mini handheld from community decompilation projects | 17 | 🟢 | C |
| [OpenEmperor](https://github.com/oliverjessner/OpenEmperor) | 🤴🏼 Clean-room reimplementation of Emperor: Rise of the Middle Kingdom in C++20 and SDL3. Built for modern systems, st... | 17 | 🟢 | C++ |
| [scooby-doo-mystery port](https://github.com/janezkranjc/scooby-doo-mistery-mouse-version) | Native SFML port of Sega Genesis Scooby-Doo Mystery from reverse-engineered 68000 code | 17 | 🟢 | C++ |
| [SpaceRanger](https://github.com/Capridog/SpaceRanger) | Native PC port of Toy Story 2: Buzz Lightyear to the Rescue (N64) via static recompilation | 17 | 🟢 | C++ |
| [Test Drive](https://github.com/kylofon/test-drive-sdl3) | Open-source recomp of Test Drive (1987). | 17 | 🟢 | C |
| [UrbanChaosRiotResponseBurnerEdition](https://github.com/linkssy2/UrbanChaosRiotResponseBurnerEdition) | Urban Chaos: Riot Response hybrid recompilation for Windows PC from the Xbox version | 17 | 🟢 | C |
| [xboxdashboard](https://github.com/sp00nznet/xboxdashboard) | The first-ever native PC port of the original Xbox Dashboard (build 3944) — static recompilation of xboxdash.xbe (x86... | 17 | 🟢 | C |
| [RecompiledHaloReach](https://github.com/Dyotson/RecompiledHaloReach) | Native PC port of Halo: Reach (Xbox 360) via static recompilation with ReXGlue | 16 | 🟢 | C++ |
| [Sonic '06 Demo](https://github.com/PranchaD/re-Sonic06Demo) | Xbox 360 static recompilation of Sonic '06 Demo | 16 | 🟢 | CMake |
| [SVR2011-Recomp](https://github.com/shaneomac1337/SVR2011-Recomp) | Unofficial Windows version of WWE SmackDown vs. Raw 2011 (Xbox 360), recompiled with ReXGlue. Bring your own disc image. | 16 | 🟢 | C++ |
| [WWFWrestleMania2000Recomp](https://github.com/jessetbh/WWFWrestleMania2000Recomp) | WWF WrestleMania 2000 N64 static recompilation | 16 | 🟢 | Python |
| [Banjo-Tooie: Recompiled](https://github.com/Vidanox/BanjoTooieRecompiled) | Banjo-Tooie static recompilation for Windows/Linux | 15 | 🟢 | C |
| [burnout-crash-recomp](https://github.com/kiesxoxo/burnout-crash-recomp) | Native PC port of Burnout CRASH! (Xbox 360 XBLA) via ReXGlue static recompilation | 15 | 🟢 | C++ |
| [CV64Recomp](https://github.com/RevoSucks/CV64Recomp) | A recompilation of Castlevania for the N64. | 15 | 🟢 | C |
| [Glover-R](https://github.com/ThatGuyMcd/Glover-R) | Static recompilation of the N64 game Glover to native PC | 15 | 🟢 | Python |
| [nfs-mw](https://github.com/47PADO47/nfs-mw) | 🦀 Rust rewrite of Need for Speed: Most Wanted (2005, PC v1.3 / Black Edition) with bevy engine | 15 | 🟢 | Rust |
| [re-stunts](https://github.com/CommonLoon102/restunts-bb11) | Recomp of the game Stunts. Original and enhanced versions. | 15 | 🟢 | C |
| [SacredStonesRecomp](https://github.com/Lordingard/SacredStonesRecomp) | Playable Windows and Android ARM64 recompilation of Fire Emblem: The Sacred Stones (GBA). | 15 | 🟢 | C++ |
| [X-Men Mutant Academy 2](https://github.com/GTTeancum/xmen-mutant-academy-2-pc) | Recomp of the PS1 game X-Men Mutant Academy 2. | 15 | 🟢 | Python |
| [BullyRecomp](https://github.com/coole42-pixel/BullyRecomp) | Static recompilation of Bully: Scholarship Edition (Xbox 360) to native Windows x64 using ReXGlue | 14 | 🟢 | C++ |
| [FFCCEOT-Recomp](https://github.com/JonathanDC64/FFCCEOT-Recomp) | Native PC port of Final Fantasy Crystal Chronicles: Echoes of Time (DS) by static recompilation. Bring your own ROM:... | 13 | 🟢 | C++ |
| [LibertyRecomp](https://github.com/hamishakl/LibertyRecomp) | Unofficial PC port of the Xbox 360 version of GTA IV via static recompilation | 13 | 🟢 | C++ |
| [MCLA-4iOS](https://github.com/KoreanSeats1/MCLA-4iOS) | Midnight Club: Los Angeles on iPhone and iPad — ARM64 static recompilation, native Metal, and an experimental 60 FPS... | 13 | 🟢 | Objective-C++ |
| [muscle-march-recomp](https://github.com/tmcleroy/muscle-march-recomp) | Unofficial native PC port of Muscle March (WiiWare) via static recompilation: macOS, Linux, Steam Deck, Windows. Requ... | 13 | 🟢 | C++ |
| [Project-Iron-6](https://github.com/GenryTheFox0/Project-Iron-6) | Unofficial Tekken 6 Xbox 360 to Windows static recompilation | 13 | 🟢 |  |
| [ssx-tricky-recomp](https://github.com/reindance/ssx-tricky-recomp) | Linux-first native recompilation of SSX Tricky for the original Xbox | 13 | 🟢 | C |
| [RogueSquadron64Recomp](https://github.com/MikeSemicolonD/RogueSquadron64Recomp) | A fully playable (AI assisted) static recompilation of Star Wars: Rogue Squadron on N64 for the PC, Linux & Android | 12 | 🟢 | C++ |
| [Test Drive III](https://github.com/kylofon/test-drive-3-sdl3) | Recomp of Test Drive III: The Passion. | 12 | 🟢 | C |
| [Warthog](https://github.com/ChupathingyCE/warthog) | Halo: Combat Evolved decompilation rebuilt for the original Xbox, playing online with PC builds | 12 | 🟢 | C |
| [doa3-re](https://github.com/NoRain211/doa3-re) | Native Windows port of Dead or Alive 3 (Xbox) via static recompilation with a hand-written runtime | 11 | 🟢 | C |
| [linksawakening-portable](https://github.com/sp00nznet/linksawakening-portable) | Link's Awakening DX statically recompiled to native C and ported to PlayStation 4, PlayStation 3, and Nintendo 3DS. N... | 10 | 🟢 | C |
| [midtown-madness-3-PC-Native](https://github.com/lakshya16157/midtown-madness-3-PC-Native) | Midtown Madness 3 native Windows port via Xbox static recompilation with Direct3D 11 | 10 | 🟢 | Python |
| [TheDarknessRecomp](https://github.com/nikolaygorb/TheDarknessRecomp) | The Darkness [Xbox360] game static recompilation project based on RexGlue-SDK | 10 | 🟢 | C++ |
| [Titanic: Adventure Out of Time](https://github.com/itskenny0/titanic-godot) | Recomp of Titanic Adventure Out of Time to Godot. | 10 | 🟢 | Go |
| [caesar2-port](https://github.com/second-impressions/caesar2-port) | Portable continuation of the Caesar II source reconstruction | 9 | 🟢 | C |
| [DoomSNESRecomp](https://github.com/Cacodemontube/DoomSNESRecomp) | This is a PC Recomp of the SNES Version of Doom using SNESrecomp. | 9 | 🟢 | C |
| [DragonBallZLegacyOfGokuRecomp](https://github.com/mstan/DragonBallZLegacyOfGokuRecomp) | Static recompilation of Dragon Ball Z: The Legacy of Goku with Adaptive Widescreen · Part of the R.A.I.D. community | 9 | 🟢 | C++ |
| [heavymetal](https://github.com/sp00nznet/heavymetal) | A static recompilation of Heavy Metal: FAKK2 (2000) targeting modern Windows 11 x86-64. | 9 | 🟢 | C |
| [RaymanOriginsRecomp](https://github.com/XDanfr/RaymanOriginsRecomp) | Unofficial static recompilation of Rayman Origins (Xbox 360) for Switch via XenonRecomp | 9 | 🟢 | C++ |
| [VPW64Recomp](https://github.com/jessetbh/VPW64Recomp) | Virtual Pro Wrestling 64 static recompilation | 9 | 🟢 | C++ |
| [3on3NHL-recomp](https://github.com/Wndwsqrrl/3on3NHL-recomp) | 3 on 3 NHL Arcade Xbox 360 static recompilation | 8 | 🟢 | C# |
| [Herculan](https://github.com/kevinfoley/Herculan) | Recomp of Earthsiege 2 by Dynamix. | 8 | 🟢 | C# |
| [StrikersRecomp](https://github.com/aharonahdoot/StrikersRecomp) | Super Mario Strikers (G4QE01) recompilation project — the worked example for RecompCore and DolRuntime. No game data... | 8 | 🟢 | C |
| [aerobiz-disasm](https://github.com/matiaszanolli/aerobiz-disasm) | Complete static recompilation of Aerobiz Supersonic for the Sega Genesis | 7 | 🟢 | Assembly |
| [DeepSea](https://github.com/AH64-dll/DeepSea) | Deep Sea: The Wind Waker at 60 fps. A free, open-source native Windows port you build from your own disc. | 7 | 🟢 | C |
| [RROP](https://github.com/kruzeman/RROP) | Static recompilation of Rings of Power for Linux and Windows with widescreen and smooth scrolling | 7 | 🟢 | Python |
| [SHO-GTA-VCS-PS2Recomp](https://github.com/BlackLineInteractive/SHO-GTA-VCS-PS2Recomp) | Playstation 2 Static Recompiler Silent Hill Origins & GTA Vice City Stories | 7 | 🗄️ | C++ |
| [Street Rod](https://github.com/kylofon/street-rod-sdl3) | Recomp of Street Rod. | 7 | 🟢 | C |
| [TDURecomp](https://github.com/testdriveupgrade/TDURecomp) | Recompilation of TDU | 7 | 🟢 | C++ |
| [Top-Gear-SNES-Static-Recomp](https://github.com/Junior-Jones/Top-Gear-SNES-Static-Recomp) | Static recompilation of Top Gear (SNES) for Windows 10 and 11. ROM not included. | 7 | 🟢 | C |
| [WaveRace64Recompiled](https://github.com/chronic8000/WaveRace64Recompiled) | Native Wave Race 64 port via static recompilation, no game assets included | 7 | 🟢 | C++ |
| [WiiCompiled-Switch](https://github.com/yashin-sh/WiiCompiled-Switch) | Experimental native Nintendo Switch port of WiiCompiled, with GX capture/replay and GPU diagnostics. Recognizable gam... | 7 | 🟢 | C++ |
| [WiiCompiled-Xbox-UWP](https://github.com/itzjuan612/WiiCompiled-Xbox-UWP) | Xbox Series / UWP port of WiiCompiled - a Mario Kart Wii static recompilation with a Dawn/D3D12 renderer | 7 | 🟢 | C++ |
| [Spider-Man-2-PS2-Recomp](https://github.com/saltyboosack-blip/Spider-Man-2-PS2-Recomp) | Open-source PS2 recompilation research checkpoint for Spider-Man 2 (USA), no rom included. | 6 | 🟢 | C++ |
| [Test Drive II](https://github.com/kylofon/test-drive-2-sdl3) | Open-source recomp of Test Drive II: The Duel. | 6 | 🟢 | C |
| [VeronicaRecomp](https://github.com/psxrestore/VeronicaRecomp) | A static recompilation of Resident Evil CODE:Veronica developed with RexGlue. | 6 | 🟢 | C++ |
| [ANIMANIACS-GC-RECOMP](https://github.com/ant0-blase/ANIMANIACS-GC-RECOMP) | Animaniacs: The Great Edgar Hunt — GameCube Static Recompilation | 5 | 🟢 | C++ |
| [caesar2-reconstruction](https://github.com/second-impressions/caesar2-reconstruction) | Clean-room reconstruction of Caesar II. | 5 | 🟢 | C |
| [DK64Recomp-NX](https://github.com/Trinalord777/DK64Recomp-NX) | Donkey Kong 64 (N64) static recompilation for Nintendo Switch with GLideN64 | 5 | 🟢 | C |
| [pokemon](https://github.com/sp00nznet/pokemon) | Generation I Pokémon (Red/Blue/Yellow) statically recompiled to native C — no emulator at runtime. Plus a headless bu... | 5 | 🟢 | Python |
| [portemon](https://github.com/portemon-nitro/portemon) | Getting HeartGold/SoulSilver out of the DS | 5 | 🟢 | Lua |
| [xwa](https://github.com/sp00nznet/xwa) | A static recompilation of Star Wars: X-Wing Alliance (1999) by Totally Games / LucasArts, targeting modern Windows wi... | 5 | 🟢 | C |
| [Aces of the Pacific](https://github.com/kylofon/aces-of-the-pacific-sdl3) | Recomp of Dynamix' Aces of the Pacific. | 4 | 🟢 | C |
| [CyberMage Modern](https://github.com/RoninSan369/CyberMageModern) | Recomp of the DOS game CyberMage. | 4 | 🟢 |  |
| [kf1-enhanced](https://github.com/Acranon/kf1-enhanced) | Enhanced native PC port of King's Field based on reverse engineering | 4 | 🟢 | C++ |
| [MarioGolf64](https://github.com/Rainchus/MarioGolf64) | MarioGolf64 | 4 | 🟢 | Python |
| [Metal Mutant-web](https://github.com/kznsq/metal-mutant-web) | Recomp of the Silmarils game Metal Mutant to Javascript. | 3 | 🟢 | JavaScript |
| [Bak-Again](https://github.com/stellargames/bakagain) | Recomp + enhancement of Betrayal At Krondor by Dynamix. | 2 | 🟢 | C# |
| [Gunboat](https://github.com/PlasticCog/Gunboat) | Open-source recomp of the game Gunboat. | 2 | 🟢 | C++ |
| [KnowYourRoleRecomp](https://github.com/Comfubar/KnowYourRoleRecomp) | WWF SmackDown! 2 PlayStation static recompilation | 2 | 🟢 | C# |
| [F-19](https://github.com/xor2003/f19re) | Recomp of MicroProse F-19. | 1 | 🟢 | Assembly |
| [Vette](https://github.com/PlasticCog/Vette2026) | Recomp of the game Vette by Spectrum Holobyte. | 1 | 🟢 | C++ |
| [Airborn Ranger](https://github.com/xor2003/airborn-ranger) | Recomp of Airborn Ranger by MicroProse. | 0 | 🟢 | C |
| [DNZHRecomp](https://gitlab.com/sonicdcer/DNZHRecomp) | DNZHRecomp |  | ⚪ |  |
| [Extreme-G: Recompiled](https://gitlab.com/sonicdcer/ExtremeGRecomp) | Extreme-G N64 static recompilation |  | ⚪ |  |
| [Mad TV online](https://madtvgame-tribute.com) | Recomp and enhancement/fixes to the German DOS game Mad TV. No github available yet, but playable online. Mad TV is a... |  | ⚪ |  |
| [MarioKart64Recomp](https://gitlab.com/sonicdcer/MarioKart64Recomp) | MarioKart64Recomp |  | ⚪ |  |
| [Starfox64Recomp](https://gitlab.com/sonicdcer/Starfox64Recomp) | Starfox64Recomp |  | ⚪ |  |
