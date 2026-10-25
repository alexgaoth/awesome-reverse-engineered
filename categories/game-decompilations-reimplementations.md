# Game Decompilations & Reimplementations

[← All categories](../README.md#whats-inside) · [Search this category on the website](https://alexgaoth.github.io/awesome-reverse-engineered/#c=game-decompilations-reimplementations) · 6,071 projects · [Listed here? Get the badge](../README.md#is-your-project-listed)

Health: 🟢 pushed in the last year · 🟡 1 to 3 years · 🔴 over 3 years · 🗄️ archived · ⚪ unknown

- [Asset & File-Format Tools](#asset--file-format-tools) (393)
- [Console Emulators](#console-emulators) (219)
- [Engine Reimplementations](#engine-reimplementations) (845)
- [Fan Patches & Enhancements](#fan-patches--enhancements) (22)
- [Game Network Protocols & APIs](#game-network-protocols--apis) (143)
- [Launchers & Store Clients](#launchers--store-clients) (47)
- [Matching Decompilations — Arcade](#matching-decompilations--arcade) (58)
- [Matching Decompilations — Atari](#matching-decompilations--atari) (3)
- [Matching Decompilations — Game Boy / GBA / DS](#matching-decompilations--game-boy--gba--ds) (379)
- [Matching Decompilations — GameCube & Wii](#matching-decompilations--gamecube--wii) (220)
- [Matching Decompilations — Mobile](#matching-decompilations--mobile) (72)
- [Matching Decompilations — Nintendo 64](#matching-decompilations--nintendo-64) (141)
- [Matching Decompilations — Other / Multi-platform](#matching-decompilations--other--multi-platform) (336)
- [Matching Decompilations — PC / DOS / Windows](#matching-decompilations--pc--dos--windows) (422)
- [Matching Decompilations — PSP / Vita / PS3](#matching-decompilations--psp--vita--ps3) (15)
- [Matching Decompilations — PlayStation 1](#matching-decompilations--playstation-1) (142)
- [Matching Decompilations — PlayStation 2](#matching-decompilations--playstation-2) (115)
- [Matching Decompilations — SNES / NES](#matching-decompilations--snes--nes) (204)
- [Matching Decompilations — Sega](#matching-decompilations--sega) (98)
- [Matching Decompilations — Switch](#matching-decompilations--switch) (20)
- [Matching Decompilations — Xbox](#matching-decompilations--xbox) (37)
- [Mod Loaders & Script Extenders](#mod-loaders--script-extenders) (292)
- [Open-source Game Clones](#open-source-game-clones) (283)
- [Other](#other) (48)
- [Private Servers](#private-servers) (219)
- [Static Recompilations & PC Ports](#static-recompilations--pc-ports) (1298)

## Asset & File-Format Tools

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [PKHeX](https://github.com/kwsch/PKHeX) | Pokemon save file editor built on reverse-engineered save formats | 5,221 | 🟢 | C# |
| [gdsdecomp (GDRE Tools)](https://github.com/GDRETools/gdsdecomp) | Godot reverse-engineering tools: PCK extraction and GDScript decompiler | 4,378 | 🟢 | C++ |
| [noclip.website](https://github.com/magcius/noclip.website) | Web-based viewer for levels from many games via reverse-engineered formats | 4,291 | 🟢 | TypeScript |
| [UABE](https://github.com/SeriousCache/UABE) | Unity Asset Bundle Extractor (archived) | 4,130 | 🗄️ | C++ |
| [repkg](https://github.com/notscuffed/repkg) | Wallpaper Engine PKG extractor and TEX-to-image converter | 3,816 | 🟡 | C# |
| [GARbro](https://github.com/morkt/GARbro) | Resource browser and extractor for visual novel archive formats | 3,345 | 🟡 | C# |
| [uTinyRipper](https://github.com/mafaca/UtinyRipper) | GUI and library to extract Unity serialized and bundle assets | 3,105 | 🔴 | C# |
| [UE Viewer (UModel)](https://github.com/gildor2/UEViewer) | Viewer and exporter for Unreal Engine 1-4 assets | 2,956 | 🟡 | C++ |
| [DisUnity](https://github.com/ata4/disunity) | Experimental toolset for Unity asset and bundle files (archived) | 2,699 | 🗄️ | Java |
| [Source 2 Viewer](https://github.com/ValveResourceFormat/ValveResourceFormat) | Browse VPKs and view, extract and decompile Source 2 assets | 2,532 | 🟢 | C# |
| [vgmstream](https://github.com/vgmstream/vgmstream) | Library for playback of hundreds of streamed video game audio formats | 2,303 | 🟢 | C |
| [UndertaleModTool](https://github.com/UnderminersTeam/UndertaleModTool) | Modding, decompiling and unpacking tool for GameMaker games such as Undertale | 2,098 | 🟢 | C# |
| [KrkrExtract](https://github.com/xmoezzz/KrkrExtract) | Extracts and packs Kirikiri (krkr2/krkrz) XP3 archives | 1,427 | 🗄️ | C++ |
| [vgmtrans](https://github.com/vgmtrans/vgmtrans) | Converts proprietary sequenced video game music formats to MIDI and SoundFont | 1,291 | 🟢 | C++ |
| [unrpyc](https://github.com/CensoredUsername/unrpyc) | Ren'Py compiled script (.rpyc) decompiler | 1,274 | 🟢 | Ren'Py |
| [SwitchThemeInjector](https://github.com/exelix11/SwitchThemeInjector) | Create custom Nintendo Switch home-menu themes from the closed SZS layout format | 1,262 | 🟢 | C |
| [extract-xiso](https://github.com/XboxDev/extract-xiso) | Xbox ISO creation and extraction utility | 1,258 | 🟢 | C |
| [NHSE](https://github.com/kwsch/NHSE) | Animal Crossing: New Horizons save editor | 1,257 | 🟢 | C# |
| [WolvenKit](https://github.com/WolvenKit/WolvenKit) | Mod editor/creator for REDengine games (Cyberpunk 2077, Witcher 3) | 1,223 | 🟢 | C# |
| [Switch Toolbox](https://github.com/KillzXGaming/Switch-Toolbox) | Tool to edit many Nintendo game file formats | 1,215 | 🟢 | C# |
| [UAssetGUI](https://github.com/atenfyr/UAssetGUI) | Tool for low-level examination and editing of Unreal Engine assets | 1,093 | 🟢 | C# |
| [demoinfocs-golang](https://github.com/markus-wa/demoinfocs-golang) | Counter-Strike 2 and CS:GO demo parser for Go | 1,072 | 🟢 | Go |
| [SourceIO](https://github.com/REDxEYE/SourceIO) | Blender addon importing Source engine textures, models and maps | 981 | 🟢 | Python |
| [LSLib](https://github.com/Norbyte/lslib) | Tools for Larian Studios game formats (Divinity: Original Sin, Baldur's Gate 3) | 947 | 🟢 | C# |
| [xEdit](https://github.com/TES5Edit/TES5Edit) | Module editor and conflict detector for Bethesda games | 907 | 🟢 | Pascal |
| [BSPSource](https://github.com/ata4/bspsrc) | Source engine map decompiler (BSP to VMF) | 878 | 🟢 | Java |
| [SLADE (Doom)](https://github.com/sirjuddington/SLADE) | SLADE, a Doom WAD and game data editor | 876 | 🟢 | C++ |
| [Crowbar](https://github.com/ZeqMacaw/Crowbar) | GoldSource and Source engine modding tool: model decompiler and compiler front-end | 840 | 🟢 | Visual Basic .NET |
| [PalworldSaveTools](https://github.com/deafdudecomputers/PalworldSaveTools) | Toolkit to fix, transfer and edit Palworld save files | 822 | 🟢 | Python |
| [Wwise-Unpacker](https://github.com/Vextil/Wwise-Unpacker) | Unpacks Wwise .pck/.bnk audio into playable files | 806 | 🟢 | Batchfile |
| [Frosty Toolsuite](https://github.com/CadeEvs/FrostyToolsuite) | Modding tools for Frostbite engine games | 782 | 🟡 | C# |
| [VPKEdit](https://github.com/craftablescience/VPKEdit) | CLI/GUI tool to create, read and write VPK and other pack formats | 778 | 🟢 | C++ |
| [clarity](https://github.com/skadistats/clarity) | Fast replay parser for Dota 2, CS:GO, CS2 and Deadlock in Java | 773 | 🟢 | Java |
| [unrpa](https://github.com/Lattyware/unrpa) | Extracts files from the Ren'Py RPA archive format | 770 | 🔴 | Python |
| [CodeWalker](https://github.com/dexyfex/CodeWalker) | Interactive 3D map and asset editor for GTA V files | 763 | 🟡 | C# |
| [UnityPack](https://github.com/HearthSim/UnityPack) | Python deserialization library for Unity3D asset bundles | 752 | 🔴 | Python |
| [Smithbox](https://github.com/vawser/Smithbox) | Modding tool for Elden Ring, Sekiro, Dark Souls and Armored Core VI | 750 | 🟢 | C# |
| [demoparser](https://github.com/LaihoE/demoparser) | Counter-Strike 2 replay parser for Python and JavaScript | 736 | 🟢 | Rust |
| [manta](https://github.com/dotabuff/manta) | Dota 2 replay parser in Go | 694 | 🟢 | Go |
| [AssetsTools.NET](https://github.com/nesrak1/AssetsTools.NET) | Library to read and write Unity assets and bundle files | 693 | 🟢 | C# |
| [DSMapStudio](https://github.com/soulsmods/DSMapStudio) | Map and level editor for Demon's Souls, Dark Souls, Bloodborne, Sekiro and Elden Ring | 676 | 🟡 | C# |
| [Obsidian](https://github.com/Crauzer/Obsidian) | WAD archive editor for League of Legends | 666 | 🟢 | TypeScript |
| [StormLib](https://github.com/ladislav-zezula/StormLib) | Library for reading and writing Blizzard MPQ archives | 655 | 🟢 | C |
| [NifSkope](https://github.com/niftools/nifskope) | Viewer and editor for NetImmerse/Gamebryo NIF files | 639 | 🟡 | C++ |
| [rpatool](https://github.com/shizmob/rpatool) | Tool to work with Ren'Py RPA archives | 631 | 🗄️ | Python |
| [OWLib / DataTool](https://github.com/overtools/OWLib) | Overwatch game data extraction library and tools | 621 | 🟢 | C# |
| [jPSXdec](https://github.com/m35/jpsxdec) | Cross-platform PlayStation 1 audio and video converter | 607 | 🟢 | Java |
| [DS Anim Studio](https://github.com/Meowmaritus/DSAnimStudio) | Dark Souls TAE animation event editor | 590 | 🟢 | C# |
| [repak](https://github.com/trumank/repak) | Unreal Engine .pak archive library and CLI in Rust | 588 | 🟢 | Rust |
| [wow.export](https://github.com/Kruithne/wow.export) | Export toolkit for World of Warcraft models, textures and maps | 573 | 🟢 | JavaScript |
| [io_import_psk_psa](https://github.com/Befzz/blender3d_import_psk_psa) | Blender addon to import Unreal PSK/PSA meshes, skeletons and animations | 566 | 🟡 | Python |
| [Godot PCK Explorer](https://github.com/DmitriySalnikov/GodotPCKExplorer) | Explorer, extractor and packer for Godot .pck files | 565 | 🟢 | C# |
| [u4pak](https://github.com/panzi/u4pak) | Unpack, pack and mount Unreal Engine 4 .pak archives | 562 | 🔴 | Python |
| [NSTool](https://github.com/jakcron/nstool) | General-purpose read/extract tool for Nintendo Switch file formats | 554 | 🟡 | C++ |
| [Enigma](https://github.com/FabricMC/Enigma) | Deobfuscation and mapping tool for Java programs, used for Minecraft | 552 | 🟢 | Java |
| [fast64](https://github.com/Fast-64/fast64) | Blender editor for scenes and meshes in first-party N64 game formats | 548 | 🟢 | Python |
| [ninfs](https://github.com/ihaveamac/ninfs) | FUSE filesystem for Nintendo console file formats (3DS, Wii U, Switch) | 544 | 🟢 | Python |
| [redscript](https://github.com/jac3km4/redscript) | Compiler/decompiler toolkit for Cyberpunk 2077's redscript | 533 | 🟢 | Rust |
| [RPFM](https://github.com/Frodo45127/rpfm) | Rusted PackFile Manager for Total War game PackFiles | 528 | 🟢 | Rust |
| [UAssetAPI](https://github.com/atenfyr/UAssetAPI) | Low-level .NET library for reading and writing Unreal Engine assets | 512 | 🟢 | C# |
| [QuickBMS](https://github.com/LittleBigBug/QuickBMS) | GitHub mirror of QuickBMS game archive extractor | 504 | 🟡 | C |
| [Pandora Behaviour Engine (Skyrim)](https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus) | Behaviour engine and animation patcher for Skyrim | 503 | 🟢 | C# |
| [CascLib](https://github.com/ladislav-zezula/CascLib) | Library for reading Blizzard CASC storages | 501 | 🟢 | C++ |
| [demofile](https://github.com/saul/demofile) | Node.js parser for CS:GO demo files | 495 | 🗄️ | JavaScript |
| [HiveWE](https://github.com/stijnherfst/HiveWE) | A Warcraft III world editor. | 486 | 🟢 | C++ |
| [OpenKH](https://github.com/OpenKH/OpenKh) | Kingdom Hearts libraries, tools, game engine and format documentation | 457 | 🟢 | C# |
| [pkNX](https://github.com/kwsch/pkNX) | Pokemon (Nintendo Switch) ROM editor and randomizer | 454 | 🟢 | C# |
| [Kuriimu2](https://github.com/FanTranslatorsInternational/Kuriimu2) | Fan translation project manager and game format toolkit | 447 | 🟢 | C# |
| [Blender Niftools Addon](https://github.com/niftools/blender_niftools_addon) | Blender import/export of NetImmerse/Gamebryo NIF files | 438 | 🟡 | Python |
| [FFXIV TexTools](https://github.com/TexTools/FFXIV_TexTools_UI) | Texture and model modding tool for Final Fantasy XIV | 433 | 🟢 | C# |
| [tinke](https://github.com/pleonex/tinke) | Viewer and editor for the files of Nintendo DS games | 429 | 🗄️ | C# |
| [VNTranslationTools](https://github.com/arcusmaximus/VNTranslationTools) | Text extraction and reinsertion tools for many visual novel engines | 423 | 🗄️ | C# |
| [REE.PAK.Tool](https://github.com/Ekey/REE.PAK.Tool) | Extract and repack PAK archives from RE Engine games | 421 | 🟢 | C# |
| [3dstool](https://github.com/dnasdw/3dstool) | All-in-one tool for extracting and creating 3DS ROM formats | 414 | 🟢 | C |
| [ww2ogg](https://github.com/hcs64/ww2ogg) | Converts Wwise RIFF/RIFX Vorbis to standard Ogg Vorbis | 403 | 🟡 | C++ |
| [SaintCoinach](https://github.com/xivapi/SaintCoinach) | .NET library for extracting Final Fantasy XIV game assets and data | 386 | 🟢 | C# |
| [wwiser](https://github.com/bnnm/wwiser) | Audiokinetic Wwise .bnk explorer and audio simulator | 376 | 🟢 | Python |
| [Kuriimu](https://github.com/IcySon55/Kuriimu) | General purpose game file and translation toolkit for fan translators | 374 | 🔴 | C# |
| [LibOrbisPkg](https://github.com/maxton/LibOrbisPkg) | Library and tools for PS4 PKG, SFO and PFS formats | 370 | 🔴 | C# |
| [LibGGPK3](https://github.com/aianlinb/LibGGPK3) | Library for Path of Exile Content.ggpk and bundle files | 344 | 🟢 | C# |
| [gsc-tool](https://github.com/xensik/gsc-tool) | Compiler and decompiler for Call of Duty IW engine GSC game scripts | 342 | 🟢 | C++ |
| [N64-Tools](https://github.com/jombo23/N64-Tools) | Tools for ripping and editing N64 game audio, graphics and data formats | 337 | 🟢 | C++ |
| [WoWDBDefs](https://github.com/wowdev/WoWDBDefs) | Client database (DB2) definitions for World of Warcraft | 330 | 🟢 | C# |
| [demoinfo](https://github.com/StatsHelix/demoinfo) | C# library to analyze CS:GO demos | 320 | 🗄️ | C# |
| [SC2k-docs](https://github.com/OpenCity2k/SC2k-docs) | Documentation of SimCity 2000 internals and file formats | 288 | 🟡 |  |
| [Assembly](https://github.com/XboxChaos/Assembly) | Multi-generation Blam engine (Halo) map research and editing tool | 269 | 🟢 | C# |
| [Decima Workshop](https://github.com/ShadelessFox/decima-workshop) | Asset viewer and modding tool for Decima engine games | 269 | 🟢 | Java |
| [VGAudio](https://github.com/Thealexbarney/VGAudio) | Library for encoding and decoding video game audio formats (ADX, HCA, DSP, etc.) | 265 | 🔴 | C# |
| [NMSE](https://github.com/vectorcmdr/NMSE) | Open source save editor for No Man's Sky | 264 | 🟢 | C# |
| [CriPakTools](https://github.com/esperknight/CriPakTools) | List, extract and update CRIWARE CPK archives | 259 | 🔴 | C# |
| [Sims4Tools](https://github.com/s4ptacle/Sims4Tools) | s4pe package editor and tools for The Sims 4 formats | 252 | 🟡 | C# |
| [retoc](https://github.com/trumank/retoc) | Tool for packing and unpacking Unreal Engine IoStore (.utoc/.ucas) containers | 251 | 🟢 | Rust |
| [aoc-mgz](https://github.com/happyleavesaoc/aoc-mgz) | Age of Empires II recorded game parser in Python | 234 | 🟢 | Python |
| [apicula](https://github.com/scurest/apicula) | Extract, view and convert Nintendo DS .nsbmd models | 230 | 🟡 | Rust |
| [godotdec](https://github.com/Bioruebe/godotdec) | Unpacker for Godot Engine .pck package files | 228 | 🟡 | C# |
| [NebulaFD](https://github.com/AITYunivers/NebulaFD) | Decompiler for Clickteam Fusion games | 228 | 🟢 | C# |
| [RE-Mesh-Editor](https://github.com/NSACloud/RE-Mesh-Editor) | Blender addon to import/export RE Engine mesh and mdf2 files | 218 | 🗄️ | Python |
| [Tools](https://github.com/bartlomiejduda/Tools) | Tools to extract and modify files from many games | 218 | 🟢 | Python |
| [lsdpatch](https://github.com/jkotlinski/lsdpatch) | LSDj ROM patcher for replacing kits, fonts and palettes | 217 | 🟡 | Java |
| [MeltyTool](https://github.com/MeltyPlayer/MeltyTool) | Multitool to view and extract assets from N64, GameCube, 3DS and PC games | 215 | 🟢 | GLSL |
| [vdf](https://github.com/ValvePython/vdf) | Python package for Valve's text and binary KeyValue (VDF) format | 214 | 🟡 | Python |
| [wow.tools.local](https://github.com/Marlamin/wow.tools.local) | Locally runnable version of wow.tools for browsing WoW data | 211 | 🟢 | C# |
| [BrawlCrate](https://github.com/soopercool101/BrawlCrate) | Wii file editor for Super Smash Bros. Brawl and other BRRES-format games | 209 | 🟢 | C# |
| [Yabber](https://github.com/JKAnderson/Yabber) | Unpacker/repacker for FromSoftware container formats | 206 | 🗄️ | C# |
| [Documentation](https://github.com/Team-Lodestone/Documentation) | Documentation of file formats and mechanics across many Minecraft versions and editions | 203 | 🟢 | TypeScript |
| [GM8Decompiler](https://github.com/OpenGMK/GM8Decompiler) | Decompiler for GameMaker 8.x executables | 202 | 🟡 |  |
| [sm64tools](https://github.com/queueRAM/sm64tools) | Collection of tools for Super Mario 64 ROM hacking | 200 | 🟢 | C |
| [EveryFileExplorer](https://github.com/Gericom/EveryFileExplorer) | EveryFileExplorer, a viewer and editor for many Nintendo DS and 3DS file formats | 199 | 🔴 | C# |
| [SoulsFormats](https://github.com/JKAnderson/SoulsFormats) | .NET library for reading and writing FromSoftware file formats | 197 | 🗄️ | C# |
| [ValveKeyValue](https://github.com/ValveResourceFormat/ValveKeyValue) | .NET library for Valve's KeyValues text and binary formats | 195 | 🟢 | C# |
| [NDSFactory](https://github.com/Luca1991/NDSFactory) | Unpack and repack Nintendo DS ROMs | 194 | 🟢 | C++ |
| [CTR-tools](https://github.com/CTR-tools/CTR-tools) | C# framework and tools to parse Crash Team Racing (PS1) game files | 191 | 🟢 | C# |
| [soulstruct-blender](https://github.com/Grimrukh/soulstruct-blender) | Blender plugins for FromSoftware game formats via soulstruct | 191 | 🟢 | Python |
| [PDTools](https://github.com/Nenkai/PDTools) | Tools and libraries for Gran Turismo (Polyphony Digital) file formats | 183 | 🟢 | C# |
| [xvdtool](https://github.com/emoose/xvdtool) | Command-line tool for manipulating Xbox One XVD and XVC files | 180 | 🟢 | C# |
| [Mutagen](https://github.com/Mutagen-Modding/Mutagen) | .NET library for analyzing and creating Bethesda plugin files | 179 | 🟢 | C# |
| [Charm](https://github.com/MontagueM/Charm) | Destiny 2 reverse engineering tool for extracting game files | 177 | 🟢 | C# |
| [GCFT](https://github.com/LagoLunatic/GCFT) | GameCube File Tools GUI for common GameCube game formats | 174 | 🟢 | Python |
| [klo-gba.js](https://github.com/macabeus/klo-gba.js) | Reverse engineering tool and level editor for Klonoa GBA | 167 | 🔴 | JavaScript |
| [seq64](https://github.com/sauraen/seq64) | Sequenced music editor for first-party N64 games | 166 | 🟢 | C++ |
| [DSLuaDecompiler](https://github.com/katalash/DSLuaDecompiler) | Lua/HavokScript decompiler for Dark Souls, Bloodborne and Sekiro scripts | 165 | 🟡 | C# |
| [rust-u4pak](https://github.com/panzi/rust-u4pak) | Rust tool to unpack, pack and mount Unreal Engine 4 .pak archives | 165 | 🔴 | Rust |
| [d2s](https://github.com/nokka/d2s) | Diablo II save file binary parser in Go | 163 | 🔴 | Go |
| [Ruri.ShaderDecompiler](https://github.com/ShiyumeMeguri/Ruri.ShaderDecompiler) | Unity shader decompiler | 163 | 🟢 | C# |
| [stove](https://github.com/bananaturtlesandwich/stove) | Editor for cooked Unreal Engine 4/5 maps | 163 | 🟡 | Rust |
| [cobra-tools](https://github.com/OpenNaja/cobra-tools) | Tools for extracting and modifying OVL/OVS archives from Planet Coaster, Planet Zoo and Jurassic World | 158 | 🟢 | Python |
| [Cyberpunk-Blender-add-on](https://github.com/WolvenKit/Cyberpunk-Blender-add-on) | Blender add-on for Cyberpunk 2077 asset formats | 157 | 🟢 | Python |
| [GBFRDataTools](https://github.com/Nenkai/GBFRDataTools) | Data tools for Granblue Fantasy: Relink archives and formats | 157 | 🟢 | C# |
| [UnrealLocres](https://github.com/akintos/UnrealLocres) | Reads and writes Unreal Engine .locres localization files | 157 | 🔴 | C# |
| [wt-tools (War Thunder)](https://github.com/klensy/wt-tools) | Resource extraction tools for War Thunder | 157 | 🔴 | Python |
| [Legendary Explorer](https://github.com/ME3Tweaks/LegendaryExplorer) | Editor toolset for Mass Effect Trilogy and Legendary Edition packages | 156 | 🟢 | C# |
| [MafiaToolkit](https://github.com/Greavesy1899/MafiaToolkit) | Open source toolkit for Mafia II, III and Definitive Edition files | 156 | 🟢 | C# |
| [Halo Asset Blender Toolset](https://github.com/General-101/Halo-Asset-Blender-Development-Toolset) | Blender exporter for Halo CE, Halo 2, Halo 3 and ODST model and animation formats | 155 | 🟢 | Python |
| [CDTB](https://github.com/CommunityDragon/CDTB) | CommunityDragon toolbox for extracting League of Legends client files | 154 | 🟢 | Python |
| [boxcars](https://github.com/nickbabcock/boxcars) | Rocket League replay parser in Rust | 152 | 🟢 | Rust |
| [Smash Forge](https://github.com/jam1garner/Smash-Forge) | Open-source editor for Smash 4 file types | 152 | 🟢 | C# |
| [Reverence](https://github.com/ntt/reverence) | Python library for EVE Online cache and bulkdata files | 151 | 🔴 | Python |
| [MidiConverters](https://github.com/ValleyBell/MidiConverters) | Tools converting game music data into MIDI files | 146 | 🟢 | C |
| [ariane](https://github.com/Dryxio/ariane) | Map editor for GTA III, Vice City and San Andreas | 144 | 🟢 | C |
| [liblcf](https://github.com/EasyRPG/liblcf) | Library to read and write RPG Maker 2000/2003 data formats | 144 | 🟢 | C++ |
| [sourcepp](https://github.com/craftablescience/sourcepp) | C++ parsers for Source engine and related formats (VPK, VTF, MDL, BSP) | 143 | 🟢 | C++ |
| [FortniteReplayDecompressor](https://github.com/Shiqan/FortniteReplayDecompressor) | Reads Fortnite replay files | 142 | 🟢 | C# |
| [Atian CoD Tools](https://github.com/ate47/atian-cod-tools) | Tools for Call of Duty games: script decompilers, asset dumpers and format utilities | 141 | 🟢 | C++ |
| [Wrench (Ratchet & Clank)](https://github.com/chaoticgd/wrench) | Modding toolset and asset editor for the PS2 Ratchet & Clank games | 141 | 🗄️ | C++ |
| [StarBreaker](https://github.com/diogotr7/StarBreaker) | Star Citizen game file reverse engineering toolkit (P4k, DCB) | 140 | 🟢 | Rust |
| [d2s-format](https://github.com/krisives/d2s-format) | Diablo II save file format documentation | 136 | 🟡 |  |
| [Lumina](https://github.com/NotAdam/Lumina) | Framework for reading Final Fantasy XIV game data | 134 | 🟢 | C# |
| [vstools](https://github.com/morris/vstools) | Toolset for Vagrant Story file formats in JavaScript | 132 | 🔴 | JavaScript |
| [Sonic Adventure Toolset](https://github.com/X-Hax/sa_tools) | Sonic Adventure Toolset | 131 | 🟢 | C# |
| [RocketLeagueReplayParser](https://github.com/jjbott/RocketLeagueReplayParser) | Rocket League replay parser in C# | 130 | 🟢 | C# |
| [ModdingDiablo2Resurrected](https://github.com/HighTechLowIQ/ModdingDiablo2Resurrected) | Tools and guides for modding Diablo II: Resurrected | 129 | 🔴 |  |
| [Quad64](https://github.com/DavidSM64/Quad64) | An open-source Super Mario 64 level editor | 129 | 🔴 | C# |
| [mhrice](https://github.com/wwylele/mhrice) | Monster Hunter Rise data extraction and information website | 128 | 🟢 | Rust |
| [OpenMF-Archived](https://github.com/MafiaHub/OpenMF-Archived) | Format utilities and parsers for Mafia: The City of Lost Heaven | 127 | 🗄️ | C++ |
| [CommunityDragon Docs](https://github.com/CommunityDragon/Docs) | Documentation of League of Legends file formats and data | 124 | 🟡 |  |
| [DSVEdit](https://github.com/LagoLunatic/DSVEdit) | Multi-purpose ROM hacking editor for DS and GBA Castlevania games | 124 | 🟡 | Ruby |
| [FrostyToolsuite](https://github.com/FrostyToolsuite/FrostyToolsuite) | Modding platform for games on DICE's Frostbite engine | 124 | 🟡 | C# |
| [LeagueToolkit](https://github.com/LeagueToolkit/LeagueToolkit) | Library for parsing and editing League of Legends assets | 124 | 🟢 | C# |
| [gbx-net](https://github.com/BigBang1112/gbx-net) | Library for Gbx files from Nadeo games like Trackmania | 122 | 🟢 | C# |
| [kismet-analyzer](https://github.com/trumank/kismet-analyzer) | Unreal Engine Blueprint/Kismet script reverse engineering and modding utility | 122 | 🟢 | C# |
| [HedgeLib](https://github.com/Radfordhound/HedgeLib) | C++ library and tools for Sonic the Hedgehog game formats | 121 | 🟢 | C++ |
| [puyotools](https://github.com/nickworonekin/puyotools) | Tools and libraries to access archives and textures in various Sega games' formats | 121 | 🟢 | C# |
| [ForzaTech-extraction-tools](https://github.com/Doliman100/ForzaTech-extraction-tools) | Reverse engineered .carbin and .modelbin formats from Forza games | 119 | 🟢 | Python |
| [GTA-V-Script-Decompiler](https://github.com/njames93/GTA-V-Script-Decompiler) | Decompiles GTA V script resources (xsc, csc, ysc) | 118 | 🔴 | C# |
| [libLSDJ](https://github.com/stijnfrishert/libLSDJ) | Library for working with the LSDj (Little Sound Dj) save file format | 113 | 🟡 | C |
| [NitroPaint](https://github.com/Garhoogin/NitroPaint) | General-purpose Nintendo DS sprite, background and texture editor | 111 | 🟢 | C |
| [Atlus Script Tools](https://github.com/tge-was-taken/Atlus-Script-Tools) | Compiler/decompiler for Atlus flowscript and message script formats | 106 | 🟢 | C# |
| [grand-theft-auto-for-unity](https://github.com/mukaschultze/grand-theft-auto-for-unity) | Loads original Grand Theft Auto map and model formats into Unity | 106 | 🟡 | C# |
| [pfs_upk](https://github.com/nextgal/pfs_upk) | Artemis engine PFS archive packer and unpacker | 105 | 🔴 | C++ |
| [MwareStuff](https://github.com/marcussacana/MwareStuff) | Tools for the Mware visual novel engine | 104 | 🟢 | C# |
| [screp](https://github.com/icza/screp) | StarCraft: Brood War replay parser in Go | 104 | 🟢 | Go |
| [playnote-studio](https://github.com/jaames/playnote-studio) | Unofficial Flipnote Studio animation player for the Playdate | 103 | 🟢 | Lua |
| [MassEffectModder](https://github.com/MassEffectModder/MassEffectModder) | Texture modding tool for the Mass Effect trilogy | 101 | 🟢 | C++ |
| [Texture64](https://github.com/queueRAM/Texture64) | N64 texture ripper and editor | 101 | 🔴 | C# |
| [alkahest](https://github.com/cohaereo/alkahest) | Destiny 2 asset viewer with accurate rendering recreation | 96 | 🟢 | Rust |
| [Raymap](https://github.com/byvar/raymap) | Map viewer for Ubisoft OpenSpace games (Rayman 2, Rayman 3 and others) | 96 | 🟢 | C# |
| [vgm_ripping](https://github.com/hcs64/vgm_ripping) | Tools for ripping video game music formats | 96 | 🔴 | C |
| [Amicitia](https://github.com/tge-was-taken/Amicitia) | Editor for file formats used in Atlus' Persona games | 92 | 🟡 | C# |
| [UnPSARC](https://github.com/rm-NoobInCoding/UnPSARC) | Unpacker and packer for PlayStation Archive (PSARC) files | 91 | 🟡 | C# |
| [Meddle (FFXIV)](https://github.com/PassiveModding/Meddle) | Plugin for exporting models from Final Fantasy XIV | 90 | 🟢 | C# |
| [ndspy](https://github.com/RoadrunnerWMC/ndspy) | Python library for many Nintendo DS file formats | 90 | 🟢 | Python |
| [AFSPacker](https://github.com/MaikelChan/AFSPacker) | Creator and extractor for CRI AFS archives used in many console games | 89 | 🟡 | C# |
| [PS1-Argonaut-Reverse](https://github.com/OverSurge/PS1-Argonaut-Reverse) | Reverse engineering of Argonaut PS1 game formats (Harry Potter, Croc 2) | 89 | 🟡 | Python |
| [source-engine-model-loader](https://github.com/gkjohnson/source-engine-model-loader) | Three.js loader for Valve Source engine models | 87 | 🟡 | JavaScript |
| [retro (OTR tool)](https://github.com/HarbourMasters/retro) | Tool that generates OTR asset archives for HarbourMasters PC ports such as Ship of Harkinian | 86 | 🟢 | Dart |
| [runescape-cache-tools](https://github.com/villermen/runescape-cache-tools) | .NET library and CLI for the RuneScape cache | 86 | 🔴 | C# |
| [SporeModder FX](https://github.com/Spore-Community/SporeModder-FX) | Modding tool for Spore package and data formats | 86 | 🟢 | Java |
| [XAT (FFXIV)](https://github.com/Etheirys/XAT) | Animation and skeleton toolkit for Final Fantasy XIV | 85 | 🟢 | C# |
| [The Lost Vikings/Blackthorne Tools](https://github.com/RyanMallon/TheLostVikingsTools) | Reverse Engineered Tools/Library for the DOS game The Lost Vikings | 83 | 🔴 | C |
| [invader (Halo CE)](https://github.com/SnowyMouse/invader) | Free toolkit for creating Halo: Combat Evolved maps and assets | 82 | 🟢 | C++ |
| [GuildWarsMapBrowser](https://github.com/Jonathan-Greve/GuildWarsMapBrowser) | Browse Guild Wars maps from the game's .dat file | 81 | 🟢 | C++ |
| [Makou Reactor](https://github.com/myst6re/makoureactor) | Final Fantasy VII field archive editor | 81 | 🟢 | C++ |
| [xbox-reversing](https://github.com/emoose/xbox-reversing) | Information and parsers for under-documented Xbox 360 structures and file formats | 81 | 🟡 | Python |
| [dat-schema](https://github.com/poe-tool-dev/dat-schema) | Community schema for Path of Exile .dat data files | 79 | 🟢 | TypeScript |
| [RPKG Tool](https://github.com/glacier-modding/RPKG-Tool) | Extracts and repacks Glacier 2 engine RPKG archives (Hitman) | 79 | 🟢 | C++ |
| [HSDLib](https://github.com/Ploaj/HSDLib) | Library for HAL Sysdolphin (HSD) DAT files used in Melee and others | 76 | 🟢 | C# |
| [ree-pak-rs (RE Engine)](https://github.com/eigeen/ree-pak-rs) | Package tools for Capcom RE Engine .pak archives | 75 | 🟢 | Rust |
| [ImageMagitek](https://github.com/stevemonaco/ImageMagitek) | .NET library for viewing and editing retro console game graphics in ROMs | 74 | 🟢 | C# |
| [NeoXResearch](https://github.com/ZhangFengze/NeoXResearch) | Reverse engineering of NetEase's NeoX game engine | 73 | 🔴 | Python |
| [w3gjs](https://github.com/PBug90/w3gjs) | Warcraft III replay parser in JavaScript | 73 | 🟢 | TypeScript |
| [Alpha](https://github.com/NotNite/Alpha) | Final Fantasy XIV toolkit for modding and datamining | 72 | 🟢 | C# |
| [dungeon-siege-re](https://github.com/glampert/dungeon-siege-re) | Reverse engineering of Dungeon Siege game asset formats | 72 | 🟢 | C++ |
| [mymcplus](https://github.com/thestr4ng3r/mymcplus) | PlayStation 2 memory card image manager (mymcplus) | 72 | 🗄️ | Python |
| [HZDCoreEditor](https://github.com/Nukem9/HZDCoreEditor) | Tools for editing Decima engine files (Horizon Zero Dawn) | 69 | 🔴 | C# |
| [NewWorldUnpacker](https://github.com/MontagueM/NewWorldUnpacker) | .pak unpacker for Amazon's New World | 66 | 🟡 | Python |
| [ZenKit (Gothic)](https://github.com/GothicKit/ZenKit) | Library for reading ZenGin file formats used by Gothic and Gothic II | 66 | 🟢 | C++ |
| [IG_tools](https://github.com/lennylxx/IG_tools) | Tools to process Innocent Grey and Noesis game files | 65 | 🟢 | C++ |
| [NSMB-Editor](https://github.com/Dirbaio/NSMB-Editor) | Level editor for New Super Mario Bros. DS | 65 | 🔴 | C# |
| [agsutils](https://github.com/rofl0r/agsutils) | Extractor, repacker, disassembler and assembler for Adventure Game Studio games | 63 | 🟢 | C |
| [Foundry (Halo)](https://github.com/ILoveAGoodCrisp/Foundry) | Blender add-on for Halo Reach, Halo 4 and Halo 2 Anniversary asset formats | 63 | 🟢 | Python |
| [il2cpp-stringliteral-patcher](https://github.com/jozsefsallai/il2cpp-stringliteral-patcher) | Extracts and patches string literals in Unity global-metadata.dat files | 63 | 🟡 | Python |
| [blender-i3d-importer](https://github.com/nadine-brinkmann/blender-i3d-importer) | Blender add-on for importing Farming Simulator .i3d files | 62 | 🟢 | Python |
| [god_of_war_browser](https://github.com/mogaika/god_of_war_browser) | Browser and extractor for God of War (PS2) game files | 61 | 🟢 | Go |
| [odradek (Decima)](https://github.com/ShadelessFox/odradek) | Asset viewer and extractor for Horizon Forbidden West and Death Stranding 2 | 61 | 🟢 | Java |
| [UnrealLocresEditor](https://github.com/Snoozeds/UnrealLocresEditor) | Editor for Unreal Engine .locres localization files | 61 | 🟢 | C# |
| [gctools](https://github.com/fuzziqersoftware/gctools) | Video game file translation tools | 60 | 🟡 |  |
| [DarkSoulsIII.FileFormats](https://github.com/Atvaark/DarkSoulsIII.FileFormats) | Dark Souls III archive file format information | 59 | 🔴 |  |
| [SM64DSe](https://github.com/Arisotura/SM64DSe) | Level, text and model editor for Super Mario 64 DS | 59 | 🔴 | C# |
| [DecimaTools](https://github.com/Wunkolo/DecimaTools) | Tools and research for reverse engineering the Decima game engine | 57 | 🔴 | C++ |
| [bayonetta_tools](https://github.com/Kerilk/bayonetta_tools) | Tools for PlatinumGames formats (Bayonetta, Nier Automata) | 56 | 🟢 | Ruby |
| [papyrus-compiler (V)](https://github.com/russo-2025/papyrus-compiler) | Open-source compiler for Bethesda's Papyrus scripting language (Skyrim SE/AE) | 56 | 🟢 | V |
| [NitroStudio2](https://github.com/Gota7/NitroStudio2) | Editor for Nintendo DS Nitro sound archives (SDAT, SSEQ, SBNK) | 55 | 🟢 | C# |
| [phoenixtools](https://github.com/Missingmew/phoenixtools) | Tools and documentation for the Ace Attorney game series | 55 | 🟡 | C++ |
| [OpenDriver2Tools](https://github.com/OpenDriver2/OpenDriver2Tools) | Tools for Driver 1 and Driver 2 game formats | 54 | 🟢 | C++ |
| [PboViewer](https://github.com/SteezCram/PboViewer) | Cross-platform maker and unpacker for Arma PBO archives | 54 | 🟡 | C# |
| [Silent-Hill](https://github.com/Sparagas/Silent-Hill) | Silent Hill file format reverse engineering | 54 | 🟢 | C |
| [silent-hill-museum](https://github.com/dreamingmoths/silent-hill-museum) | Web museum and viewer of Silent Hill models from the original game files | 54 | 🟢 | TypeScript |
| [gbcamextract](https://github.com/jkbenaim/gbcamextract) | Extracts photos from Game Boy Camera save files | 53 | 🔴 | C |
| [KingsFieldRE](https://github.com/IvanDSM/KingsFieldRE) | King's Field II reverse engineering tools and documentation | 53 | 🔴 | C++ |
| [reevengi-tools](https://github.com/pmandin/reevengi-tools) | Tools to check reverse engineering of Resident Evil file formats | 53 | 🟢 | C |
| [Deling](https://github.com/myst6re/deling) | Final Fantasy VIII field and worldmap archive editor | 52 | 🟢 | C++ |
| [oead](https://github.com/zeldamods/oead) | Library for Nintendo EPD file formats (SARC, BYML, AAMP, Yaz0) | 52 | 🟢 | C++ |
| [Xbox-Live-Save-Exporter](https://github.com/Tom60chat/Xbox-Live-Save-Exporter) | Exports local saves from Xbox Live and Game Pass PC game containers | 52 | 🟢 | C# |
| [gmbt (Gothic)](https://github.com/Szmyk/gmbt) | Build tool for testing and packing Gothic and Gothic II mods | 51 | 🟡 | C# |
| [Vagrant-Story-Unity-Parser](https://github.com/korobetski/Vagrant-Story-Unity-Parser) | Unity editor scripts that read original Vagrant Story data | 51 | 🟡 | C# |
| [driver-tools](https://github.com/Fireboyd78/driver-tools) | Modding tools for DRIV3R, Driver: Parallel Lines and Driver: San Francisco | 49 | 🔴 | C# |
| [Fmod5Sharp](https://github.com/SamboyCoding/Fmod5Sharp) | Managed decoder for FMOD 5 sound banks (FSB files) | 49 | 🟢 | C# |
| [RAGE-StringsDatabase](https://github.com/OpenIV-Team/RAGE-StringsDatabase) | Known strings and file names for RAGE engine games (GTA IV, GTA V, RDR) | 49 | 🔴 | C# |
| [SnowRunner-Save-Editor](https://github.com/MrBoxik/SnowRunner-Save-Editor) | Save editor for SnowRunner | 48 | 🟢 | Python |
| [DogScepter](https://github.com/colinator27/DogScepter) | Modding tool for Undertale and Deltarune (GameMaker data files) | 47 | 🗄️ | C# |
| [Mamar](https://github.com/bates64/mamar) | Music editor for Paper Mario (N64) | 47 | 🟢 | TypeScript |
| [Medal-Of-Honor-PSX-File-Viewer](https://github.com/AdrianoDiDio/Medal-Of-Honor-PSX-File-Viewer) | Tools to open and view files from the PSX Medal of Honor games | 46 | 🟢 | C |
| [StudioSB](https://github.com/Ploaj/StudioSB) | Model application for Super Smash Bros. Ultimate formats | 46 | 🔴 | C# |
| [FFXIV_Modding_Tool](https://github.com/lillelilje/FFXIV_Modding_Tool) | Command-line modding tool for Final Fantasy XIV (TexTools alternative) | 45 | 🗄️ | C# |
| [gecko (Fallout 2)](https://github.com/JanSimek/gecko) | Fallout 2 map editor | 45 | 🟢 | C++ |
| [JFortniteParse](https://github.com/FabianFG/JFortniteParse) | Kotlin/Java library to parse Unreal Engine pak/asset files from Fortnite | 45 | 🟢 | Kotlin |
| [ltd-save-editor](https://github.com/alexislours/ltd-save-editor) | Reader, writer and reverse-engineered field schema for Tomodachi Life .sav save files | 45 | 🟢 | TypeScript |
| [Ray1Map](https://github.com/BinarySerializer/Ray1Map) | Map viewer and editor for Rayman 1 and other Ubisoft games | 45 | 🟡 | C# |
| [NDS_Banner_Editor](https://github.com/TheGameratorT/NDS_Banner_Editor) | Tool to make animated Nintendo DS banners | 43 | 🟡 | C++ |
| [wc3libs](https://github.com/inwc3/wc3libs) | Java library for reading and modifying Warcraft III maps and game files | 43 | 🟢 | Java |
| [Macaron](https://github.com/Azukee/Macaron) | Lightweight unpacker for various game archive formats | 42 | 🔴 | C# |
| [Nanoforge (Red Faction Guerrilla)](https://github.com/rfg-modding/Nanoforge) | Modding tool for Red Faction Guerrilla Re-Mars-tered | 42 | 🟡 | C# |
| [libpandadna](https://github.com/loblao/libpandadna) | Parser for Disney's DNA scene files used by Toontown Online | 41 | 🔴 | C++ |
| [Marathon (Sonic 2006)](https://github.com/hyperbx/Marathon) | Toolkit and library for Sonic the Hedgehog (2006) file formats | 41 | 🟢 | C# |
| [mhw_armor_edit](https://github.com/fre-sch/mhw_armor_edit) | Equipment and armor editor for Monster Hunter: World | 40 | 🔴 | Python |
| [RevilLib](https://github.com/PredatorCZ/RevilLib) | Library and toolset for Capcom MT Framework and RE Engine formats | 40 | 🟢 | C++ |
| [DRV3-Sharp](https://github.com/CaptainSwag101/DRV3-Sharp) | Tools for working with Danganronpa V3 PC files | 39 | 🟡 | C# |
| [SilentHillMapExaminer](https://github.com/ItEndsWithTens/SilentHillMapExaminer) | BizHawk utility to reverse engineer the Silent Hill map format | 39 | 🟢 | C# |
| [botw-editor](https://github.com/handsomematt/botw-editor) | Editor for The Legend of Zelda: Breath of the Wild | 38 | 🔴 | C# |
| [DestinyUnpacker](https://github.com/MontagueM/DestinyUnpacker) | Destiny 2 .pkg unpacker used for reverse engineering | 38 | 🔴 | Python |
| [Inject-pictures-in-your-Game-Boy-Camera-saves](https://github.com/Raphael-Boichot/Inject-pictures-in-your-Game-Boy-Camera-saves) | The Game Boy Camera save format explained, with tools to inject pictures | 38 | 🟢 | MATLAB |
| [Torch](https://github.com/HarbourMasters/Torch) | N64 ROM asset extractor and converter used by fan PC ports | 38 | 🟢 | C++ |
| [yukatool](https://github.com/AtomCrafty/yukatool) | Tools for the Yuka System visual novel engine | 37 | 🔴 | C# |
| [JSRF_ModTool](https://github.com/neodoso/JSRF_ModTool) | Modding tool for Jet Set Radio Future (Xbox) | 36 | 🟢 | C# |
| [Naruto-GNT-Modding](https://github.com/NicholasMoser/Naruto-GNT-Modding) | Modding tools for Naruto: Clash of Ninja (Gekitou Ninja Taisen) on GameCube | 36 | 🟢 | Python |
| [project-igi-toolkit](https://github.com/heaven-hm/project-igi-toolkit) | Toolkit to edit maps, AI, graphs and missions in Project I.G.I. | 36 | 🟢 | C# |
| [homm3-unpacker](https://github.com/neunato/homm3-unpacker) | Parser for Heroes of Might and Magic III game files | 35 | 🟡 | JavaScript |
| [project-igi-research](https://github.com/heaven-hm/project-igi-research) | Research data on Project I.G.I. file formats and internals | 35 | 🟢 | Assembly |
| [XXL-Editor](https://github.com/AdrienTD/XXL-Editor) | Level editor for Etranges Libellules Kal engine games (Asterix XXL) | 35 | 🟢 | C++ |
| [gbcam2png](https://github.com/raphnet/gbcam2png) | Convert Game Boy Camera save RAM photos to PNG | 34 | 🔴 | C |
| [Gibbed.LetUsClingTogether](https://github.com/gibbed/Gibbed.LetUsClingTogether) | Tools for Tactics Ogre: Let Us Cling Together (PSP and remake) | 34 | 🟢 | C# |
| [HiOctaneTools](https://github.com/movAX13h/HiOctaneTools) | Tools to inspect and modify levels of Hi-Octane (Bullfrog, 1995) | 34 | 🟢 | C# |
| [SlyTools](https://github.com/VelocityRa/SlyTools) | Modding tools and research for the Sly Cooper games | 34 | 🟡 | Python |
| [Telltale-Texture-Tool](https://github.com/Telltale-Modding-Group/Telltale-Texture-Tool) | Converts Telltale Tool D3DTX textures for texture mods | 34 | 🟢 | C# |
| [Gibbed.Dunia](https://github.com/gibbed/Gibbed.Dunia) | Tools for Dunia engine games (Far Cry series) | 32 | 🔴 | C# |
| [MiiJS](https://github.com/Stewared/MiiJS) | JavaScript library for reading, writing and rendering Nintendo Mii data | 32 | 🟢 | JavaScript |
| [PS1-Argonaut-Assets](https://github.com/OverSurge/PS1-Argonaut-Assets) | Extracted textures and 3D models from Argonaut's Croc 2 and Harry Potter PS1 formats | 32 | 🔴 |  |
| [N-Gage_stuff](https://github.com/1upus/N-Gage_stuff) | Tools for translating and modding Nokia N-Gage games | 30 | 🟡 | Batchfile |
| [blender-vagrant-story](https://github.com/korobetski/blender-vagrant-story) | Blender add-on importing and exporting Vagrant Story file formats | 29 | 🟡 | Python |
| [mii-js](https://github.com/PretendoNetwork/mii-js) | JavaScript library to read and render Mii data from Wii U and 3DS | 29 | 🟢 | TypeScript |
| [silver-reversing-sct](https://github.com/nadavshemesh/silver-reversing-sct) | Tool to read, write and modify scripts of the 1999 RPG Silver | 29 | 🟡 | C |
| [UnityTexTool](https://github.com/wmltogether/UnityTexTool) | Converts Unity Texture2D files unpacked from asset packs | 29 | 🗄️ | C# |
| [AWTools](https://github.com/Nostritius/AWTools) | Tools for reverse-engineered file formats of Alan Wake and later Remedy games | 28 | 🔴 | Python |
| [thps2-tools](https://github.com/JayFoxRox/thps2-tools) | Tools for Tony Hawk's Pro Skater 2 (Neversoft Big Guns engine) | 28 | 🔴 | Python |
| [Urgon (Indiana Jones)](https://github.com/smlu/Urgon) | Tools for Indiana Jones and the Infernal Machine | 28 | 🟡 | C++ |
| [ZenTools](https://github.com/WistfulHopes/ZenTools-UE4) | Tools for extracting Unreal Engine IoStore (Zen) packages | 28 | 🟡 | C++ |
| [albam](https://github.com/Brachi/albam) | Modding tool for Capcom MT Framework games | 27 | 🟢 | Python |
| [Light.vnTools](https://github.com/bungaku-moe/Light.vnTools) | Unpacker and repacker for games made with the Light.vn engine | 27 | 🟡 | C# |
| [sarc](https://github.com/zeldamods/sarc) | Reader and writer for the Nintendo SARC archive format | 27 | 🟡 | Python |
| [tailslab (Need for Speed)](https://github.com/AndyGura/tailslab) | Editor, converter and byte-level specs for classic Need for Speed file formats | 27 | 🟢 | Python |
| [ubiart-secure-fat](https://github.com/wukko/ubiart-secure-fat) | UbiArt secure_fat.gf generator for modding Just Dance and Rayman Legends | 27 | 🔴 | Python |
| [dftools (Dark Forces)](https://github.com/njankowski/dftools) | Tools for Star Wars: Dark Forces assets | 26 | 🔴 | Python |
| [SL2Bonfire](https://github.com/mi5hmash/SL2Bonfire) | Unpacks, packs and re-signs SL2 save data from FromSoftware games | 26 | 🟡 | C# |
| [SnowRunnerTools](https://github.com/chase-000/SnowRunnerTools) | Tools for SnowRunner game files | 26 | 🔴 | C# |
| [channelzss](https://github.com/Octocontrabass/channelzss) | Tools for the Sega Channel LZSS compression format | 25 | 🔴 | C |
| [igArchiveExtractor](https://github.com/NefariousTechSupport/igArchiveExtractor) | Extracts and repacks .arc/.bld/.pak archives from Alchemy engine games | 25 | 🗄️ | C# |
| [PakWorkbench (Arma Reforger)](https://github.com/Rendszerguru/PakWorkbench) | Asset analysis tool and PAK extractor for Arma Reforger | 25 | 🟢 | C# |
| [yukatool2](https://github.com/AtomCrafty/yukatool2) | Rewritten toolset for the Yuka System visual novel engine | 25 | 🟡 | C# |
| [FF8 Rinoa's Toolset](https://github.com/MaKiPL/FF8-Rinoa-s-Toolset) | All-in-one modding toolkit for Final Fantasy VIII | 24 | 🗄️ | C# |
| [game-boy-camera-manager](https://github.com/marcrobledo/game-boy-camera-manager) | Swiss-army-knife manager for Game Boy Camera save SRAM and ROM | 24 | 🟢 | JavaScript |
| [Gibbed.SleepingDogs](https://github.com/gibbed/Gibbed.SleepingDogs) | Tools for Sleeping Dogs: Definitive Edition | 24 | 🔴 | C# |
| [R3ditor (Resident Evil 3)](https://github.com/themitosan/R3ditor) | Reverse-engineering tool for Resident Evil 3 files | 24 | 🟡 | JavaScript |
| [saveeditor](https://github.com/paradoxie/saveeditor) | Online save file editor for RPG Maker, Unity, Ren'Py and Unreal Engine games | 24 | 🟢 | TypeScript |
| [sg-sprite (MAGES engine)](https://github.com/AbsurdlySuspicious/sg-sprite) | Sprite decoder for MAGES engine games (Steins;Gate 0, Chaos;Child) | 24 | 🟡 | Rust |
| [fallout-shelter-save-editor](https://github.com/dneverson/fallout-shelter-save-editor) | Browser-based save editor for Fallout Shelter | 23 | 🟢 | TypeScript |
| [cathedral-assets-optimizer](https://github.com/Guekka/cathedral-assets-optimizer) | Ports Skyrim mods between LE and SE, creates Bethesda archives and compresses textures | 22 | 🟢 | C++ |
| [FEZRepacker](https://github.com/FEZModding/FEZRepacker) | Tool and library for unpacking and repacking FEZ assets | 22 | 🟢 | C# |
| [darkstone-re](https://github.com/glampert/darkstone-re) | Tools to reverse engineer the file formats of the game Darkstone | 21 | 🟢 | C |
| [driver_psx_level](https://github.com/SoapyMan/driver_psx_level) | Level loader for Driver 1 and 2 (PS1) | 21 | 🗄️ | C++ |
| [fxc-converter (GTA)](https://github.com/gtasnail/fxc-converter) | Unpacks and repacks GTA .fxc shader files | 21 | 🟡 | Rust |
| [leotools](https://github.com/jkbenaim/leotools) | Tools for 64DD disk images and the files they contain | 21 | 🔴 | C |
| [lfgfx](https://github.com/ethteck/lfgfx) | Detection and analysis of N64 graphics data in ROMs | 21 | 🔴 | Python |
| [SharpNeedle](https://github.com/hedge-dev/SharpNeedle) | C# library for reading and writing Sonic Hedgehog Engine file formats | 21 | 🟢 | C# |
| [TalesOfTools](https://github.com/DaZombieKiller/TalesOfTools) | Tools for the Tales of series (Xillia, Zestiria, Berseria, Graces f) | 21 | 🟢 | C# |
| [WAD-Tool (Neversoft)](https://github.com/DCxDemo/WAD-Tool) | Packer and unpacker for Neversoft Big Guns engine WAD archives (Tony Hawk's Pro Skater) | 21 | 🔴 | C# |
| [AJT-Tools](https://github.com/Aclios/AJT-Tools) | Capcom RE Engine modding tools | 20 | 🟡 | Python |
| [Empire-Earth-Studio-2](https://github.com/EE-modders/Empire-Earth-Studio-2) | Editor for Empire Earth game data | 20 | 🟡 | Python |
| [GCNToolKit](https://github.com/Cuyler36/GCNToolKit) | Toolkit for modifying and creating GameCube file formats | 20 | 🔴 | C# |
| [kanim-explorer](https://github.com/romen-h/kanim-explorer) | Viewer and editor for Oxygen Not Included .kanim files | 20 | 🟢 | C# |
| [ShinDataUtil](https://github.com/DCNick3/ShinDataUtil) | This is an utility for working with game files of Higurashi no Naku Koro ni and Kono Subarashii Sekai ni Shukufuku wo... | 20 | 🟢 | C# |
| [Princed Resources](https://github.com/NagyD/PR) | Princed Resources is a tool to export and import graphics and other data from and to DAT files of Prince of Persia 1... | 19 | 🔴 | C |
| [Siege Studio](https://github.com/open-siege/siege-studio) | Siege Studio is a desktop application for previewing, modifying and converting reverse engineered file formats for ga... | 19 | 🟢 | C++ |
| [Flipnote-Player](https://github.com/pbsds/Flipnote-Player) | Player for Flipnote Studio DSi files from storage or Hatena private servers | 17 | 🔴 | Python |
| [MApRX](https://github.com/wwylele/MApRX) | Map editor for Kirby Super Star Ultra (DS) | 17 | 🔴 | C++ |
| [BSFlashManager](https://github.com/devinacker/BSFlashManager) | Tool to manage Satellaview BS-X memory packs | 16 | 🔴 | C |
| [HedgehogEngineBlenderIO](https://github.com/hedge-dev/HedgehogEngineBlenderIO) | Blender add-on to import and export Sonic Hedgehog Engine 3D file formats | 16 | 🟢 | Python |
| [pso_tools](https://github.com/Sylverant/pso_tools) | Command-line tools for Phantasy Star Online data files | 16 | 🔴 | C |
| [utkencode](https://github.com/daddesio/utkencode) | Encoder for EA MicroTalk, a speech codec based on multi-pulse linear prediction used in various EA games. This encode... | 16 | 🔴 | C |
| [IGI QVM Editor](https://github.com/heaven-hm/project-igi-qvm-editor) | Script (QVM) editor for Project IGI 1 and 2 | 15 | 🗄️ | C# |
| [moonglow-toolset](https://github.com/jadzziaa/moonglow-toolset) | Reimplementation of the Neverwinter Nights: Enhanced Edition Aurora Toolset in Rust | 15 | 🟢 | Rust |
| [SM64SaveEditor](https://github.com/MaikelChan/SM64SaveEditor) | Save editor for Super Mario 64 | 15 | 🟢 | C++ |
| [vmu-tools](https://github.com/slurmking/vmu-tools) | Tools to read and modify Dreamcast VMU save files and file types | 15 | 🔴 | Python |
| [dpoly_js (Flashback)](https://github.com/cyxx/dpoly_js) | HTML5 player for Flashback DPoly cutscenes | 14 | 🗄️ | JavaScript |
| [MHDataParser](https://github.com/Crypto137/MHDataParser) | Parser for Marvel Heroes game data files | 14 | 🟡 | C# |
| [TACTSharp](https://github.com/wowdev/TACTSharp) | C# library for Blizzard's TACT/CASC content distribution | 13 | 🟢 | C# |
| [LibGM](https://github.com/BioTomateDE/LibGM) | Tool for unpacking and modding GameMaker games such as Undertale and Deltarune | 12 | 🟢 | Rust |
| [libpsoarchive](https://github.com/Sylverant/libpsoarchive) | Library for archive formats used in the Phantasy Star Online series | 12 | 🔴 | C |
| [nitro-g3d-tools](https://github.com/Ermelber/nitro-g3d-tools) | Tools to convert models into the Nitro 3D formats used by DS games | 12 | 🔴 | C# |
| [badpiggies-editor](https://github.com/LambdaEd1th/badpiggies-editor) | Bad Piggies level and save editor for desktop and WebAssembly | 11 | 🟢 | Rust |
| [uasset_read](https://github.com/soatori/uasset_read) | Python parser for Unreal Engine .uasset files with Kismet bytecode decompilation | 11 | 🟢 | Python |
| [romman](https://github.com/israpps/romman) | Image manager for PlayStation 2 BIOS ROM and IOPRP images | 10 | 🟢 | C++ |
| [Nexus.Archive](https://github.com/NexusForever/Nexus.Archive) | Library to load and save WildStar index/archive files | 9 | 🟡 | C# |
| [nintendo-file-formats](https://github.com/PretendoNetwork/nintendo-file-formats) | TypeScript library for several Nintendo Wii U and 3DS file formats | 9 | 🟢 | TypeScript |
| [sctools](https://github.com/nfroggy/sctools) | Tools for Sega Channel data | 9 | 🟡 | C |
| [smash-arc](https://github.com/jam1garner/smash-arc) | Library for Super Smash Bros. Ultimate's ARC archive format | 9 | 🟡 | Rust |
| [boss-crypto](https://github.com/PretendoNetwork/boss-crypto) | Crypto functions for creating and reading Wii U and 3DS BOSS (SpotPass) files | 8 | 🟢 | TypeScript |
| [F3DEX2Decoder](https://github.com/Mr-Wiseguy/F3DEX2Decoder) | C# decoder for N64 F3DEX2 display lists | 8 | 🔴 | C# |
| [MKSM Studio](https://github.com/OGmidway/Mortal-Kombat-Shaolin-Monks-Modding-Tool) | Modding tool for Mortal Kombat: Shaolin Monks: models, textures, audio and ISO builds | 8 | 🟢 | Python |
| [mo2mp4](https://github.com/RiiConnect24/mo2mp4) | Converts Nintendo Wii Mobiclip .mo videos to MP4 | 8 | 🔴 | C# |
| [OpenCalligraphy](https://github.com/Crypto137/OpenCalligraphy) | Browser for Calligraphy framework data used in Marvel Heroes | 8 | 🟢 | C# |
| [UnityWebTools.NET](https://github.com/kiraio-moe/UnityWebTools.NET) | C# library for reading and writing UnityWebData files | 8 | 🔴 | C# |
| [Duke2Edit](https://github.com/lethal-guitar/Duke2Edit) | Level editor for Duke Nukem II | 7 | 🔴 | C |
| [faf-scfa-replay-parser](https://github.com/FAForever/faf-scfa-replay-parser) | Parser for Supreme Commander: Forged Alliance binary replay streams | 7 | 🔴 | Python |
| [HedgeMatEdit](https://github.com/hedge-dev/HedgeMatEdit) | Material editor for Sonic Hedgehog Engine games | 7 | 🟢 | C# |
| [obscura](https://github.com/svendahlstrand/obscura) | Salvage photographs from a Game Boy Camera save file | 7 | 🔴 | C |
| [TD3Extract](https://github.com/yuv422/TD3Extract) | A tool for extracting data files from the game - Test Drive III "The Passion" | 7 | 🔴 | C++ |
| [yyc-toolbox](https://github.com/Valkyrians/yyc-toolbox) | Mod tool and decompiler for GameMaker YYC-compiled games | 7 | 🟢 | C |
| [DimensionsSaveConverter](https://github.com/NeverCookFirst/DimensionsSaveConverter) | Converts LEGO Dimensions saves between Xbox 360, PS3 and PS4 formats | 6 | 🟢 | C# |
| [extract_fb_genesis (Flashback)](https://github.com/cyxx/extract_fb_genesis) | Extracts data files from the Flashback Sega Genesis ROM | 6 | 🗄️ | C |
| [Fantastic Dizzy Tools](https://github.com/RyanMallon/dizzy) | Reverse engineering tools for Fantastic Dizzy | 6 | 🔴 | Python |
| [ita-bag](https://github.com/PretendoNetwork/ita-bag) | Tool for Nintendo Badge Arcade PrizeCollection archives on 3DS | 6 | 🔴 | JavaScript |
| [MiiTube](https://github.com/RiiConnect24/MiiTube) | Tools for the MiiTube.dat SpotPass file from the 3DS game Miitopia | 6 | 🔴 | Shell |
| [mpromtool](https://github.com/gamemasterplc/mpromtool) | Mario Party 1-3 ROM Extractor/Rebuilder Tool | 6 | 🟡 | C++ |
| [OTRExporter](https://github.com/HarbourMasters/OTRExporter) | Exports game assets from N64 ROMs into OTR archives for HarbourMasters PC ports | 6 | 🟢 | C++ |
| [blueshell](https://github.com/bbomb64/blueshell) | Cross-platform level editor for New Super Mario Bros. DS | 5 | 🔴 | C++ |
| [bmgconv](https://github.com/WiiLink24/bmgconv) | Converter for Nintendo Wii BMG message files | 5 | 🔴 | Go |
| [brlytlib](https://github.com/WiiLink24/brlytlib) | Converts Nintendo Wii BRLYT layout files to and from XML | 5 | 🟡 | Go |
| [FDB-Converter](https://github.com/IAmMajo/FDB-Converter) | Converts LEGO Universe FDB database files to and from SQLite | 5 | 🟡 | CSS |
| [FLATool](https://github.com/psforever/FLATool) | Extractor and packer for PlanetSide 1 .FAT flat files | 5 | 🔴 | C |
| [FNT-Tool](https://github.com/RoadrunnerWMC/FNT-Tool) | Converts Nintendo DS fnt.bin filename tables to and from JSON | 5 | 🔴 | Python |
| [OpenApe](https://github.com/Rex109/OpenApe) | Open reimplementation of the CoD4 Asset Property Editor with live 3D preview | 5 | 🟢 | C++ |
| [PokemonDungeonExplorers](https://github.com/pleonex/PokemonDungeonExplorers) | Tools and documentation for the Pokemon Mystery Dungeon Explorers DS games | 5 | 🗄️ | C# |
| [VengeanceRipper](https://github.com/suXinjke/VengeanceRipper) | Extracts files and converts 3D models from Colony Wars: Vengeance (PS1) | 5 | 🔴 | JavaScript |
| [NerdFontTerminatoR](https://github.com/pleonex/NerdFontTerminatoR) | Create, modify and view NFTR font files from Nintendo DS games | 4 | 🗄️ | C# |
| [SADL-Audio-format](https://github.com/pleonex/SADL-Audio-format) | Documentation and tools for the SADL audio format in Nintendo DS games | 4 | 🗄️ | C# |
| [NSBMD-NSBTX_Converter](https://github.com/TheGameratorT/NSBMD-NSBTX_Converter) | Converts models and textures to Nintendo DS NSBMD/NSBTX files | 3 | 🗄️ | C++ |
| [raxicore-editor](https://github.com/psforever/raxicore-editor) | Game asset viewer, editor and unpacker for PlanetSide 1 | 3 | 🟢 | C# |
| [V1TicketGenerator](https://github.com/OpenShopChannel/V1TicketGenerator) | Creates the Nintendo Wii V1 ticket format for shop downloads | 3 | 🔴 | Go |
| [kaitais](https://github.com/WiiLink24/kaitais) | Kaitai Struct definitions for Nintendo Wii channel file formats | 2 | 🟢 | Kaitai Struct |
| [PopResourceEditor (Populous: The Beginning)](https://github.com/Toksisitee/PopResourceEditor) | Asset editor for Populous: The Beginning game files | 2 | 🟡 | C++ |
| [Project IGI Editor](https://github.com/heaven-hm/project-igi-editor) | 3D level editor for Project IGI 1 | 2 | 🟢 | C++ |
| [pes21-ml-editor](https://github.com/felipemikeias/pes21-ml-editor) | Editor for eFootball PES 2021 Master League save files | 1 | 🟢 | Rust |
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
| [shadPS4](https://github.com/shadps4-emu/shadPS4) | PlayStation 4 emulator for Windows, Linux and macOS | 33,909 | 🟢 | C++ |
| [v86](https://github.com/copy/v86) | v86, an x86 PC emulator and x86-to-wasm JIT running in the browser | 23,629 | 🟢 | JavaScript |
| [RPCS3](https://github.com/RPCS3/rpcs3) | PlayStation 3 emulator and debugger | 20,185 | 🟢 | C++ |
| [PCSX2](https://github.com/PCSX2/pcsx2) | PlayStation 2 emulator | 15,908 | 🟢 | C++ |
| [Dolphin](https://github.com/dolphin-emu/dolphin) | GameCube and Wii emulator | 15,715 | 🟢 | C++ |
| [ppsspp](https://github.com/hrydgard/ppsspp) | PPSSPP, a PSP emulator for Android, Windows, macOS, Linux and iOS | 14,746 | 🟢 | C++ |
| [DuckStation](https://github.com/stenzek/duckstation) | PlayStation 1 emulator focused on accuracy and speed | 10,882 | 🟢 | C++ |
| [mame](https://github.com/mamedev/mame) | MAME, the multi-system arcade and computer emulator | 10,665 | 🟢 | C++ |
| [Cemu](https://github.com/cemu-project/Cemu) | Cemu, a Wii U emulator | 10,028 | 🟢 | C++ |
| [mgba](https://github.com/mgba-emu/mgba) | mGBA, an accurate Game Boy Advance emulator | 7,525 | 🟢 | C |
| [jsnes](https://github.com/bfirsh/jsnes) | jsnes, a JavaScript NES emulator | 6,431 | 🟢 | JavaScript |
| [Vita3K](https://github.com/Vita3K/Vita3K) | Experimental PlayStation Vita emulator | 5,887 | 🟢 | C++ |
| [PyBoy](https://github.com/Baekalfen/PyBoy) | Game Boy emulator written in Python, with an API for scripting and AI agents | 5,231 | 🟢 | Python |
| [melonDS](https://github.com/melonDS-emu/melonDS) | melonDS, a Nintendo DS emulator with DSi and local wireless support | 5,146 | 🟢 | C++ |
| [SimpleNES](https://github.com/amhndu/SimpleNES) | SimpleNES, an NES emulator in C++ | 5,114 | 🟡 | C++ |
| [86Box](https://github.com/86Box/86Box) | 86Box, an emulator of x86-based machines | 4,951 | 🟢 | C |
| [xemu](https://github.com/xemu-project/xemu) | xemu, an original Xbox emulator built on low-level hardware emulation | 4,215 | 🟢 | C |
| [visualboyadvance-m](https://github.com/visualboyadvance-m/visualboyadvance-m) | VisualBoyAdvance-M, a Game Boy Advance emulator | 3,940 | 🟢 | C++ |
| [dosbox-x](https://github.com/joncampbell123/dosbox-x) | DOSBox-X, a DOS and PC-98 emulator | 3,786 | 🟢 | C |
| [desmume](https://github.com/TASEmulators/desmume) | DeSmuME, a Nintendo DS emulator | 3,671 | 🟢 | C++ |
| [orbital](https://github.com/AlexAltea/orbital) | Orbital, an experimental PlayStation 4 emulator | 3,652 | 🟡 | C |
| [snes9x](https://github.com/snes9xgit/snes9x) | Snes9x, a portable Super Nintendo emulator | 3,378 | 🟢 | C++ |
| [Main_MiSTer](https://github.com/MiSTer-devel/Main_MiSTer) | Main binary of MiSTer, the open FPGA platform for recreating retro consoles and computers | 3,304 | 🟢 | C++ |
| [project64](https://github.com/project64/project64) | Project64, a long-running Nintendo 64 emulator for Windows | 3,068 | 🟢 | C++ |
| [BizHawk](https://github.com/TASEmulators/BizHawk) | BizHawk, a multi-system emulator with TAS tools | 2,805 | 🟢 | C# |
| [Play-](https://github.com/jpd002/Play-) | Play!, a PlayStation 2 emulator | 2,723 | 🟢 | C++ |
| [Xenia Canary](https://github.com/xenia-canary/xenia-canary) | Experimental fork of the Xenia Xbox 360 emulator | 2,687 | 🟢 | C++ |
| [flycast](https://github.com/flyinghead/flycast) | Flycast, a Sega Dreamcast, Naomi and Atomiswave emulator | 2,621 | 🟢 | C++ |
| [Mesen2](https://github.com/SourMesen/Mesen2) | Mesen 2, a multi-system emulator (NES, SNES, GB, GBA, PCE, SMS, WS) | 2,416 | 🗄️ | C++ |
| [strato](https://github.com/strato-emu/strato) | Strato, a Nintendo Switch emulator for Android | 2,352 | 🟡 | C++ |
| [SameBoy](https://github.com/LIJI32/SameBoy) | Accuracy-focused Game Boy and Game Boy Color emulator written in C | 2,232 | 🟢 | C |
| [EKA2L1](https://github.com/EKA2L1/EKA2L1) | EKA2L1, a Symbian OS and N-Gage emulator | 2,061 | 🟢 | C++ |
| [GPCS4](https://github.com/Inori/GPCS4) | GPCS4, a work-in-progress PlayStation 4 emulator | 2,032 | 🔴 | C++ |
| [bsnes](https://github.com/bsnes-emu/bsnes) | bsnes, an accuracy-focused Super Nintendo emulator | 2,008 | 🟢 | C++ |
| [metalnes](https://github.com/iaddis/metalnes) | Transistor-level NES simulation | 1,954 | 🔴 | JavaScript |
| [pcem](https://github.com/sarah-walker-pcem/pcem) | PCem, an emulator of vintage x86 PCs | 1,945 | 🟢 | C |
| [simh](https://github.com/simh/simh) | SIMH, the Computer History Simulation Project for historic minicomputers and mainframes | 1,888 | 🟢 | C |
| [melonDS-android](https://github.com/rafaelvcaetano/melonDS-android) | Android port of the melonDS Nintendo DS emulator | 1,718 | 🟢 | Kotlin |
| [macemu](https://github.com/cebix/macemu) | Basilisk II and SheepShaver classic Macintosh emulators | 1,637 | 🟡 | C++ |
| [FBNeo](https://github.com/finalburnneo/FBNeo) | FinalBurn Neo, an arcade and console emulator | 1,549 | 🟢 | C++ |
| [LaiNES](https://github.com/AndreaOrru/LaiNES) | LaiNES, a compact cycle-accurate NES emulator | 1,519 | 🟢 | C++ |
| [Panda3DS](https://github.com/wheremyfoodat/Panda3DS) | HLE 3DS emulator | 1,413 | 🟢 | C++ |
| [higan](https://github.com/higan-emu/higan) | higan, an accuracy-focused multi-system emulator | 1,361 | 🟡 | GLSL |
| [js-dos](https://github.com/caiiiycuk/js-dos) | js-dos, an API for running DOS programs in the browser | 1,344 | 🟢 | TypeScript |
| [Mesen](https://github.com/SourMesen/Mesen) | Mesen, a cross-platform NES/Famicom emulator | 1,324 | 🗄️ | C++ |
| [gopher64](https://github.com/gopher64/gopher64) | gopher64, a highly compatible Nintendo 64 emulator | 1,315 | 🟢 | Rust |
| [SkyEmu](https://github.com/skylersaleh/SkyEmu) | SkyEmu, a Game Boy Advance, Game Boy and DS emulator | 1,313 | 🟢 | C |
| [NanoBoyAdvance](https://github.com/nba-emu/NanoBoyAdvance) | NanoBoyAdvance, a cycle-accurate Game Boy Advance emulator | 1,310 | 🗄️ | C++ |
| [decaf-emu](https://github.com/decaf-emu/decaf-emu) | decaf-emu, a Wii U emulator research project | 1,278 | 🟡 | C++ |
| [pcjs](https://github.com/jeffpar/pcjs) | PCjs, emulations of the original IBM PC and other machines in JavaScript | 1,225 | 🟢 | JavaScript |
| [Gearboy](https://github.com/drhelius/Gearboy) | Gearboy, a Game Boy / Color emulator and debugger | 1,219 | 🟢 | C++ |
| [dosbox-pure](https://github.com/schellingb/dosbox-pure) | DOSBox Pure, a DOSBox fork for libretro | 1,181 | 🟢 |  |
| [simple64](https://github.com/simple64/simple64) | simple64, an accuracy-focused Nintendo 64 emulator based on mupen64plus | 1,178 | 🗄️ | C |
| [metroboy](https://github.com/aappleby/metroboy) | Gate-level simulators and tools for the original Game Boy | 1,174 | 🟡 | C++ |
| [NooDS](https://github.com/Hydr8gon/NooDS) | NooDS, a fast Nintendo DS emulator | 1,165 | 🟢 | C++ |
| [CLK](https://github.com/TomHarte/CLK) | Clock Signal, an emulator of many 8- and 16-bit computers and consoles | 1,148 | 🟢 | C++ |
| [reicast-emulator](https://github.com/skmp/reicast-emulator) | Reicast, a multiplatform Sega Dreamcast emulator | 1,135 | 🗄️ | C++ |
| [RMG](https://github.com/Rosalie241/RMG) | Rosalie's Mupen GUI, a cross-platform mupen64plus-based N64 emulator | 1,133 | 🟢 | C++ |
| [gbajs](https://github.com/endrift/gbajs) | Game Boy Advance emulator in the browser | 1,091 | 🗄️ | JavaScript |
| [ProjectPSX](https://github.com/BluestormDNA/ProjectPSX) | ProjectPSX, an experimental PlayStation emulator in C# | 1,083 | 🟢 | C# |
| [pcsx-redux](https://github.com/grumpycoders/pcsx-redux) | PlayStation 1 emulator and toolset for development and reverse engineering | 1,029 | 🟢 | C++ |
| [mooneye-gb](https://github.com/Gekkio/mooneye-gb) | Game Boy research project and emulator written in Rust | 971 | 🔴 | Rust |
| [Genesis-Plus-GX](https://github.com/ekeeke/Genesis-Plus-GX) | Genesis Plus GX, an accurate Sega 8/16-bit and Mega CD emulator | 970 | 🟢 | C |
| [martypc](https://github.com/dbalsom/martypc) | MartyPC, a cycle-accurate IBM PC/XT/PCjr/Tandy emulator | 947 | 🟢 | Rust |
| [nestopia](https://github.com/0ldsk00l/nestopia) | Nestopia, a cross-platform NES emulator core with GUI | 945 | 🟢 | C++ |
| [AppleWin](https://github.com/AppleWin/AppleWin) | AppleWin, an Apple II emulator for Windows | 937 | 🟢 | C |
| [pce](https://github.com/jsdf/pce) | PCE, emulating the Mac Plus, IBM PC and Atari ST in the browser via WebAssembly | 917 | 🟢 | C |
| [fake-08](https://github.com/jtothebell/fake-08) | Pico-8 player and emulator for console homebrew | 885 | 🟢 | C++ |
| [cen64](https://github.com/n64dev/cen64) | Cycle-accurate Nintendo 64 emulator | 842 | 🟢 | C |
| [puNES](https://github.com/punesemu/puNES) | puNES, a Qt-based NES emulator and NSF player | 826 | 🟢 | C |
| [obliteration](https://github.com/obhq/obliteration) | Experimental open-source PlayStation 4 kernel reimplementation and emulator | 822 | 🟢 | Rust |
| [pinky](https://github.com/koute/pinky) | NES emulator written in Rust | 810 | 🟡 | Rust |
| [halfix](https://github.com/nepx/halfix) | Halfix, an x86 PC emulator that runs natively and in the browser | 791 | 🔴 | C |
| [stella](https://github.com/stella-emu/stella) | Stella, a multi-platform Atari 2600 emulator | 770 | 🟢 | C |
| [jsGB](https://github.com/Two9A/jsGB) | JavaScript emulation of the Game Boy | 752 | 🔴 | JavaScript |
| [bsnes-hd](https://github.com/DerKoun/bsnes-hd) | bsnes fork adding HD Mode 7 and widescreen features | 710 | 🟢 | GLSL |
| [WinUAE](https://github.com/tonioni/WinUAE) | WinUAE, an Amiga emulator for Windows | 693 | 🟢 | C++ |
| [daedalus](https://github.com/DaedalusX64/daedalus) | DaedalusX64, a Nintendo 64 emulator for PSP, Vita and desktop | 687 | 🟢 | C++ |
| [boytacean](https://github.com/joamag/boytacean) | Boytacean, a Game Boy emulator written in Rust | 683 | 🟢 | Rust |
| [N64Wasm](https://github.com/nbarkhina/N64Wasm) | Web-based Nintendo 64 emulator | 679 | 🟡 | C++ |
| [Supermodel](https://github.com/trzy/Supermodel) | Sega Model 3 arcade emulator | 673 | 🟢 | C++ |
| [xqemu](https://github.com/xqemu/xqemu) | XQEMU, an original Xbox emulator based on QEMU | 672 | 🔴 | C |
| [n64js](https://github.com/hulkholden/n64js) | n64js, a Nintendo 64 emulator in JavaScript | 656 | 🟢 | JavaScript |
| [binjgb](https://github.com/binji/binjgb) | Game Boy emulator in C that also runs in the browser | 612 | 🟢 | C |
| [gbe-plus](https://github.com/shonumi/gbe-plus) | DMG/GBC/GBA emulator with experimental NDS support and many peripheral emulations | 600 | 🟢 | C++ |
| [rustation](https://github.com/simias/rustation) | Rustation, a PlayStation emulator in Rust | 586 | 🟢 | Rust |
| [Avocado](https://github.com/JaCzekanski/Avocado) | Avocado, a PlayStation 1 emulator | 583 | 🔴 | C++ |
| [openMSX](https://github.com/openMSX/openMSX) | openMSX, an accuracy-focused MSX emulator | 560 | 🟢 | C++ |
| [VerilogBoy](https://github.com/zephray/VerilogBoy) | VerilogBoy, a Game Boy implemented in Verilog for FPGAs | 549 | 🔴 | Verilog |
| [DSVita](https://github.com/Grarak/DSVita) | Fast Nintendo DS emulator for ARM32 and PS Vita | 530 | 🟢 | Rust |
| [DobieStation](https://github.com/PSI-Rockin/DobieStation) | DobieStation, a PlayStation 2 emulator | 517 | 🔴 | C++ |
| [WebMSX](https://github.com/ppeccin/WebMSX) | WebMSX, an online MSX emulator | 484 | 🟢 | HTML |
| [GameLad](https://github.com/Dooskington/GameLad) | GameLad, an almost fully featured Game Boy emulator | 464 | 🟢 | C++ |
| [jsmess](https://github.com/jsmess/jsmess) | Efforts to port MESS to JavaScript | 447 | 🔴 | Shell |
| [pearpc](https://github.com/sebastianbiallas/pearpc) | PearPC, a PowerPC architecture emulator | 443 | 🟢 | C++ |
| [zesarux](https://github.com/chernandezba/zesarux) | ZEsarUX, a ZX Spectrum and Z88 emulator | 440 | 🟢 | C |
| [NP2kai](https://github.com/AZO234/NP2kai) | Neko Project II kai, an NEC PC-9801 emulator | 437 | 🟢 | C |
| [atari800](https://github.com/atari800/atari800) | Atari 8-bit computer and 5200 console emulator | 432 | 🟢 | C |
| [DaedalusX64-vitaGL](https://github.com/Rinnegatamante/DaedalusX64-vitaGL) | DaedalusX64 Nintendo 64 emulator ported to PS Vita through vitaGL | 430 | 🟢 | C++ |
| [mikage-dev](https://github.com/mikage-emu/mikage-dev) | Mikage Developer Edition | 421 | 🟡 | C++ |
| [Mesen-S](https://github.com/SourMesen/Mesen-S) | Mesen-S, a cross-platform SNES emulator | 417 | 🗄️ | C++ |
| [vAmiga](https://github.com/dirkwhoffmann/vAmiga) | vAmiga, an Amiga 500/1000/2000 emulator for macOS | 413 | 🟢 | C++ |
| [prosperity](https://github.com/Force67/prosperity) | Experimental emulator for Sony PS4 and PS5 consoles | 405 | 🟢 | C++ |
| [ANESE](https://github.com/daniel5151/ANESE) | ANESE, an NES emulator and first implementation of wideNES | 403 | 🔴 | C++ |
| [gambatte](https://github.com/sinamas/gambatte) | Gambatte, an accuracy-focused Game Boy Color emulator | 401 | 🔴 |  |
| [Gearsystem](https://github.com/drhelius/Gearsystem) | Gearsystem, a Sega Master System / Game Gear / SG-1000 emulator and debugger | 397 | 🟢 | C++ |
| [jsbeeb](https://github.com/mattgodbolt/jsbeeb) | jsbeeb, a JavaScript BBC Micro emulator | 395 | 🟢 | JavaScript |
| [Ishiiruka](https://github.com/Tinob/Ishiiruka) | Ishiiruka, a performance-focused Dolphin-based GameCube/Wii emulator | 373 | 🔴 | C++ |
| [not64](https://github.com/extremscorner/not64) | not64, an N64 emulator for GameCube and Wii based on Mupen64GC | 369 | 🟢 | C |
| [bsnes-plus](https://github.com/devinacker/bsnes-plus) | Debug-oriented fork of the bsnes SNES emulator | 365 | 🟡 | C++ |
| [meka](https://github.com/ocornut/meka) | MEKA, a Sega 8-bit emulator with debugging and hacking tools | 356 | 🟢 | C++ |
| [ScriptedAmigaEmulator](https://github.com/naTmeg/ScriptedAmigaEmulator) | Scripted Amiga Emulator in JavaScript and HTML5 | 354 | 🟢 | JavaScript |
| [wabbitemu](https://github.com/sputt/wabbitemu) | Wabbitemu, a Z80 TI calculator emulator | 335 | 🟢 | C |
| [sodium64](https://github.com/Hydr8gon/sodium64) | SNES emulator for the Nintendo 64, written in assembly | 333 | 🟡 | Assembly |
| [1964GEPD](https://github.com/Graslu/1964GEPD) | 1964 N64 emulator build tuned for GoldenEye 007 and Perfect Dark | 321 | 🗄️ | C |
| [Nuked-MD-FPGA](https://github.com/nukeykt/Nuked-MD-FPGA) | Mega Drive/Genesis Verilog core derived from die-level reverse engineering | 317 | 🟡 | Verilog |
| [Xenon](https://github.com/xenon-emu/xenon) | Low-level Xbox 360 emulator for researching Xenon hardware | 317 | 🟢 | C++ |
| [gameroy](https://github.com/Rodrigodd/gameroy) | Game Boy emulator, disassembler and debugger in Rust | 314 | 🟡 | Rust |
| [pinmame](https://github.com/vpinball/pinmame) | PinMAME, an emulator for pinball machine hardware | 314 | 🟢 | C |
| [IodineGBA](https://github.com/taisel/IodineGBA) | IodineGBA, a JavaScript Game Boy Advance emulator | 296 | 🔴 | JavaScript |
| [FBAlpha](https://github.com/barry65536/FBAlpha) | FB Alpha, an arcade emulator | 283 | 🗄️ | C++ |
| [Corgi3DS](https://github.com/PSI-Rockin/Corgi3DS) | Corgi3DS, a low-level Nintendo 3DS emulator | 250 | 🔴 | C++ |
| [enge-js](https://github.com/kootstra-rene/enge-js) | eNGE, a JavaScript PlayStation emulator | 246 | 🟢 | JavaScript |
| [flycast-dojo](https://github.com/blueminder/flycast-dojo) | Flycast fork with online netplay for Dreamcast, Naomi and Atomiswave games | 244 | 🟢 | C++ |
| [ContrAlto](https://github.com/livingcomputermuseum/ContrAlto) | ContrAlto, an emulator of the Xerox Alto | 242 | 🟢 | C# |
| [javatari.js](https://github.com/ppeccin/javatari.js) | Javatari, an online Atari 2600 emulator | 242 | 🟡 | HTML |
| [rustual-boy](https://github.com/emu-rs/rustual-boy) | Rustual Boy, a Virtual Boy emulator | 232 | 🗄️ | Rust |
| [MedNES](https://github.com/wpmed92/MedNES) | MedNES, a cycle-accurate cross-platform NES emulator | 226 | 🔴 | C++ |
| [breaks](https://github.com/emu-russia/breaks) | Transistor-level reverse engineering of NES/Famicom chips | 221 | 🟢 | Verilog |
| [xnes](https://github.com/tjwei/xnes) | JavaScript SNES emulator | 213 | 🔴 | C++ |
| [giibiiadvance](https://github.com/AntonioND/giibiiadvance) | GB, GBC and GBA emulator with Game Boy Camera support | 208 | 🟢 | C |
| [Mu](https://github.com/meepingsnesroms/Mu) | Mu, a Palm OS emulator | 206 | 🟡 | C |
| [pureikyubu](https://github.com/emu-russia/pureikyubu) | Nintendo GameCube emulator | 196 | 🟢 | C++ |
| [fpg1](https://github.com/hrvach/fpg1) | FPGA implementation of the DEC PDP-1 in Verilog | 195 | 🔴 | Verilog |
| [XTulator](https://github.com/mikechambers84/XTulator) | XTulator, a portable open-source 8086 PC emulator | 192 | 🟡 | C |
| [3dmoo](https://github.com/plutooo/3dmoo) | Early Nintendo 3DS emulator prototype | 186 | 🔴 | C |
| [Emulator.NES](https://github.com/Xyene/Emulator.NES) | Nintendo Entertainment System emulator written in C# | 186 | 🔴 | C# |
| [nullDC-v1](https://github.com/skmp/nullDC-v1) | nullDC, a Sega Dreamcast emulator | 186 | 🗄️ | C++ |
| [n64](https://github.com/Dillonb/n64) | Experimental low-level Nintendo 64 emulator | 185 | 🟢 | C++ |
| [Nuked-MD](https://github.com/nukeykt/Nuked-MD) | Cycle-accurate Mega Drive emulator from die-level reverse engineering | 185 | 🟢 | C |
| [GBA_MiSTer](https://github.com/MiSTer-devel/GBA_MiSTer) | Game Boy Advance core for the MiSTer FPGA platform | 177 | 🟢 | VHDL |
| [r64emu](https://github.com/rasky/r64emu) | Nintendo 64 emulator written in Rust | 177 | 🔴 | Rust |
| [jsspeccy3](https://github.com/gasman/jsspeccy3) | jsspeccy, a ZX Spectrum emulator for the browser | 169 | 🟢 | JavaScript |
| [vice.js](https://github.com/rjanicek/vice.js) | VICE Commodore emulator compiled to JavaScript | 166 | 🔴 | Shell |
| [psxrev](https://github.com/emu-russia/psxrev) | Sony PlayStation PCB and chip reverse engineering | 160 | 🟡 | C# |
| [jsSMS](https://github.com/gmarty/jsSMS) | JavaScript Sega Master System and Game Gear dynamic recompiling emulator | 152 | 🔴 | JavaScript |
| [neschan](https://github.com/yizhang82/neschan) | NES emulator written in C++ | 151 | 🟡 | C++ |
| [b2](https://github.com/tom-seddon/b2) | b2, a BBC Micro emulator for Windows, macOS and Linux | 140 | 🟢 | C++ |
| [jsgs](https://github.com/burakcan/jsgs) | JavaScript reimplementation of the closed Pico-8 fantasy console | 140 | 🔴 | JavaScript |
| [b-em](https://github.com/stardot/b-em) | B-em, a BBC Micro emulator | 137 | 🟢 | C |
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
| [simcoupe](https://github.com/simonowen/simcoupe) | SimCoupe, a SAM Coupe emulator | 80 | 🟢 | C++ |
| [ChonkyStation](https://github.com/liuk7071/ChonkyStation) | ChonkyStation, a PlayStation 1 emulator | 79 | 🟡 | C++ |
| [1964js](https://github.com/schibo/1964js) | Nintendo 64 emulator in JavaScript | 77 | 🟡 | CoffeeScript |
| [libevmu](https://github.com/gyrovorbis/libevmu) | Accurate cross-platform library emulating the Dreamcast Visual Memory Unit (VMU) | 77 | 🟢 | C |
| [VisualNes](https://github.com/SourMesen/VisualNes) | Visual NES, simulating the NES CPU and PPU at transistor level | 77 | 🗄️ | C# |
| [Cxbx-Reloaded](https://github.com/Cxbx-Reloaded/Cxbx-Reloaded) | Original Xbox emulator via HLE of reverse engineered XDK libraries | 76 | 🟢 | C++ |
| [NitroSwan](https://github.com/FluBBaOfWard/NitroSwan) | WonderSwan and PocketChallenge V2 emulator for the Nintendo DS | 76 | 🟢 | C |
| [kpspemu](https://github.com/soywiz-archive/kpspemu) | PSP emulator written in Kotlin for JVM, JS and native | 75 | 🗄️ | Kotlin |
| [DSHBA](https://github.com/DenSinH/DSHBA) | Highly performant GBA emulator with a hardware renderer | 71 | 🔴 | C++ |
| [SEGAChips](https://github.com/emu-russia/SEGAChips) | Reverse engineering of SEGA chips | 69 | 🟢 | Verilog |
| [ColecoDS](https://github.com/wavemotion-dave/ColecoDS) | ColecoVision emulator for the Nintendo DS/DSi | 63 | 🟢 | C |
| [PCSX-Reloaded](https://github.com/pcsxr/PCSX-Reloaded) | Mirror of PCSX-Reloaded, a PlayStation emulator | 62 | 🔴 | C |
| [nintendulator](https://github.com/quietust/nintendulator) | Nintendulator, an accurate NES emulator for Windows | 58 | 🟢 | C++ |
| [cor64](https://github.com/bdragoncore/cor64) | N64 Emulator written in C# | 56 | 🟡 | C# |
| [gngeo](https://github.com/linuxlinks/gngeo) | GnGeo, a Neo Geo emulator for Linux | 56 | 🔴 | Assembly |
| [StrikeBox](https://github.com/StrikerX3/StrikeBox) | StrikeBox, an original Xbox emulator | 55 | 🔴 | C++ |
| [Felix](https://github.com/laoo/Felix) | Felix, an Atari Lynx emulator | 54 | 🟡 | C++ |
| [js99er-angular](https://github.com/Rasmus-M/js99er-angular) | TI-99/4A emulator written in TypeScript | 52 | 🟢 | TypeScript |
| [dmgcpu](https://github.com/emu-russia/dmgcpu) | Reverse engineering of the Game Boy DMG CPU from the die | 48 | 🟢 | Verilog |
| [StoicGoose](https://github.com/xdanieldzd/StoicGoose) | WonderSwan and WonderSwan Color emulator in C# | 48 | 🟢 | C# |
| [Ryu64](https://github.com/Ryu64Emulator/Ryu64) | Nintendo 64 emulator written in C# | 45 | 🗄️ | C# |
| [FreeIntv](https://github.com/libretro/FreeIntv) | Libretro emulation core for the Mattel Intellivision | 44 | 🟢 | C |
| [lxdream](https://github.com/lxdream/lxdream) | Lxdream, a Sega Dreamcast emulator | 41 | 🔴 | C |
| [ProSystem1_3](https://github.com/gstanton/ProSystem1_3) | ProSystem, an Atari 7800 emulator | 40 | 🔴 | C++ |
| [SNES_S-CPU_Schematics](https://github.com/rgalland/SNES_S-CPU_Schematics) | Reverse engineering of the SNES CPU from die shots | 40 | 🟡 | KiCad Schematic |
| [KanaStation](https://github.com/noumidev/KanaStation) | Experimental low-level PlayStation Portable emulator | 39 | 🟢 | C++ |
| [mvs64](https://github.com/rasky/mvs64) | Neo Geo emulator for the Nintendo 64 | 39 | 🟡 | C |
| [DotN64](https://github.com/Nabile-Rahmani/DotN64) | Nintendo 64 emulator in C# | 38 | 🔴 | C# |
| [hyperscan-emulator](https://github.com/LiraNuna/hyperscan-emulator) | Emulator for the Mattel HyperScan console | 34 | 🟢 | C++ |
| [unununium](https://github.com/RebeccaRGB/unununium) | Disassembler and emulator for the Sunplus u'nSP CPU used in V.Smile and other toys | 34 | 🔴 | C |
| [zakuro](https://github.com/fearkov/zakuro) | A Nintendo 3DS emulator in Rust, using AOT recompilation | 32 | 🟢 | Rust |
| [kamo64](https://github.com/kmc-jp/kamo64) | Low-level Nintendo 64 emulator | 30 | 🟢 | C++ |
| [QuickNES](https://github.com/kode54/QuickNES) | QuickNES, a fast NES emulator | 27 | 🗄️ |  |
| [biostation](https://github.com/Ravenslofty/biostation) | Clean-room PlayStation 2 BIOS | 26 | 🔴 | Assembly |
| [pockystation](https://github.com/simias/pockystation) | Sony PocketStation emulator | 23 | 🟢 | Rust |
| [FPGA-DENDY](https://github.com/andkorzh/FPGA-DENDY) | Clock-precise FPGA reimplementation of the Dendy (Famicom clone) 8-bit console | 21 | 🟢 | Verilog |
| [MoRePhun](https://github.com/Luca1991/MoRePhun) | Experimental emulator for the MoPhun mobile game platform | 19 | 🔴 | C++ |
| [Model2EmuEx](https://github.com/octavioCuatrochio/Model2EmuEx) | Decompiled Sega Model 2 emulator modified to run on Linux and Android | 18 | 🟢 | C |
| [Space Invaders Emulator](https://github.com/Justin-Credible/space-invaders-emulator) | Emulator for the Space Invaders arcade machine (Intel 8080) | 18 | 🟢 | C# |
| [papiGB](https://github.com/diegovalverde/papiGB) | Game Boy Classic FPGA implementation built from scratch | 16 | 🔴 | Verilog |
| [GA330-libretro](https://github.com/minexew/GA330-libretro) | Libretro core emulating the Gemei A330 handheld | 15 | 🔴 | C |
| [libgpu2](https://github.com/aap/libgpu2) | Reverse-engineered reference implementation of the PS2 Graphics Synthesizer | 15 | 🟢 | C |
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
| [OpenRA](https://github.com/OpenRA/OpenRA) | RTS engine reimplementing early Westwood games such as C&C Red Alert | 17,645 | 🟢 | C# |
| [OpenRCT2](https://github.com/OpenRCT2/OpenRCT2) | Open-source reimplementation of RollerCoaster Tycoon 2 | 16,498 | 🟢 | C++ |
| [openage](https://github.com/SFTtech/openage) | Free clone of the Genie engine used by Age of Empires II | 14,548 | 🟢 | Python |
| [OpenDiablo2](https://github.com/OpenDiablo2/OpenDiablo2) | Open-source re-implementation of Diablo 2 | 11,104 | 🗄️ | Go |
| [DevilutionX](https://github.com/diasurgical/DevilutionX) | Diablo and Hellfire port for modern systems built on the Devilution reverse engineering | 9,937 | 🟢 | C++ |
| [OpenTTD](https://github.com/OpenTTD/OpenTTD) | Open-source transport simulation game based on Transport Tycoon Deluxe | 8,422 | 🟢 | C++ |
| [OpenMW](https://github.com/OpenMW/openmw) | Open-source engine reimplementation for The Elder Scrolls III: Morrowind | 6,678 | 🟢 | C++ |
| [VCMI](https://github.com/vcmi/vcmi) | Open-source engine for Heroes of Might and Magic III | 5,983 | 🟢 | C++ |
| [RuneLite](https://github.com/runelite/runelite) | Open source Old School RuneScape client | 5,503 | 🟢 | Java |
| [OpenSC2K](https://github.com/OpenSC2K/OpenSC2K) | OpenSC2K - Open Source remake of Sim City 2000 using rust and godot. Available for macOS, Windows and Linux | 5,320 | 🟢 | Rust |
| [OpenLara](https://github.com/XProger/OpenLara) | Classic Tomb Raider open-source engine | 5,137 | 🟢 | C |
| [zelda3](https://github.com/snesrev/zelda3) | C reimplementation of Zelda: A Link to the Past from reverse-engineered SNES code | 4,906 | 🟢 | C |
| [CorsixTH](https://github.com/CorsixTH/CorsixTH) | Open-source clone of Theme Hospital | 4,617 | 🟢 | Lua |
| [PythonPlantsVsZombies](https://github.com/marblexu/PythonPlantsVsZombies) | a simple PlantsVsZombies game | 3,771 | 🟡 | Python |
| [OpenGOAL (jak-project)](https://github.com/open-goal/jak-project) | Reimplements the GOAL language/runtime to port Jak and Daxter 1-3 to PC | 3,613 | 🟢 | Common Lisp |
| [OpenXRay](https://github.com/OpenXRay/xray-16) | Improved version of the X-Ray Engine, the game engine used in the world-famous S.T.A.L.K.E.R. game series by GSC Game... | 3,595 | 🟢 | C++ |
| [Daggerfall Unity](https://github.com/Interkarma/daggerfall-unity) | Recreation of The Elder Scrolls II: Daggerfall in Unity | 3,545 | 🟢 | C# |
| [fheroes2](https://github.com/ihhub/fheroes2) | Recreation of the Heroes of Might and Magic II game engine | 3,516 | 🟢 | C++ |
| [Julius](https://github.com/bvschaik/julius) | Open-source reimplementation of Caesar III with the original game logic | 3,417 | 🟢 | C |
| [Super Mario Bros Remastered](https://github.com/JHDev2006/Super-Mario-Bros.-Remastered-Public) | A Remake / Celebration of the original 'Super Mario Bros.' games. Features new levels, custom modes, new characters,... | 3,268 | 🟢 | GDScript |
| [WipEout (wipeout-rewrite)](https://github.com/phoboslab/wipeout-rewrite) | Reverse-engineered reimplementation / port of WipEout (wipeout-rewrite) | 2,992 | 🟢 | C |
| [kys-cpp](https://github.com/scarsty/kys-cpp) | 《金庸群侠传》c++复刻版，已完工 | 2,974 | 🟢 | C++ |
| [Fallout Community Edition](https://github.com/alexbatalov/fallout1-ce) | Fully working reimplementation of Fallout 1 engine | 2,953 | 🟡 | C++ |
| [Xash3D FWGS](https://github.com/FWGS/xash3d-fwgs) | Open-source reimplementation of the GoldSrc engine that runs Half-Life | 2,886 | 🟢 | C |
| [ScummVM](https://github.com/scummvm/scummvm) | Reimplements engines of classic point-and-click adventure games | 2,865 | 🟢 | C++ |
| [ioquake3](https://github.com/ioquake/ioq3) | Community continuation of id's Quake III Arena engine | 2,854 | 🟢 | C |
| [SanAndreasUnity](https://github.com/in0finite/SanAndreasUnity) | Open source reimplementation of GTA San Andreas game engine in Unity | 2,667 | 🔴 | C# |
| [Fallout 2 CE](https://github.com/alexbatalov/fallout2-ce) | Fallout 2 engine re-implementation for modern desktop and mobile | 2,476 | 🟡 | C++ |
| [OpenJK](https://github.com/JACoders/OpenJK) | Community-maintained Jedi Academy / Jedi Outcast engine | 2,312 | 🟢 | C++ |
| [OpenRW](https://github.com/rwengine/openrw) | Open-source re-implementation of Rockstar's GTA III | 2,253 | 🟡 | C++ |
| [OpenXcom](https://github.com/OpenXcom/OpenXcom) | Open-source clone of UFO: Enemy Unknown and X-COM: Terror from the Deep | 2,242 | 🟢 | C++ |
| [Freeablo](https://github.com/wheybags/freeablo) | Open-source implementation of the Diablo engine. | 2,170 | 🔴 | C++ |
| [Augustus](https://github.com/Keriew/augustus) | An open source re-implementation of Caesar III | 2,128 | 🟢 | C |
| [ClassiCube](https://github.com/ClassiCube/ClassiCube) | Custom Minecraft Classic-compatible game client in C | 2,083 | 🟢 | C |
| [SDLPAL](https://github.com/sdlpal/sdlpal) | SDL-based reimplementation of the classic Chinese-language RPG known as PAL. | 1,990 | 🟢 | C |
| [OpenLoco](https://github.com/OpenLoco/OpenLoco) | Open-source reimplementation of Chris Sawyer's Locomotion | 1,955 | 🟢 | C++ |
| [Hematite](https://github.com/PistonDevelopers/hematite) | A simple Minecraft written in Rust with the Piston game engine | 1,918 | 🟢 | Rust |
| [OpenDUNE](https://github.com/OpenDUNE/OpenDUNE) | Recreation of the popular game Dune II. | 1,696 | 🟢 | C |
| [Pokémon Polished Crystal](https://github.com/Rangi42/polishedcrystal) | An upgrade to Pokémon Crystal. Brings features and content up to date, and adds some original content. | 1,681 | 🟢 | Assembly |
| [roBrowser](https://github.com/vthibault/roBrowser) | Ragnarok Online client reimplemented for web browsers in JavaScript/WebGL | 1,660 | 🗄️ | JavaScript |
| [Ikemen GO](https://github.com/ikemen-engine/Ikemen-GO) | Open-source reimplementation of the MUGEN fighting game engine | 1,637 | 🟢 | Go |
| [OpenGothic](https://github.com/Try/OpenGothic) | Open-source reimplementation of Gothic I and II | 1,637 | 🟢 | C++ |
| [Clumsy Bird](https://github.com/ellisonleao/clumsy-bird) | :bird: :video_game: A MelonJS port of the famous Flappy Bird Game | 1,630 | 🗄️ | JavaScript |
| [openblack](https://github.com/openblack/openblack) | Open-source reimplementation of Black & White (2001) | 1,592 | 🟢 | C++ |
| [horizon](https://github.com/ludovic111/horizon) | Minecraft: Java Edition rewritten in Rust and checked against vanilla with differential tests | 1,478 | 🟢 | Rust |
| [OpenTomb](https://github.com/opentomb/OpenTomb) | Open-source Tomb Raider 1-5 engine remake (archived) | 1,445 | 🗄️ | C++ |
| [OpenTESArena](https://github.com/afritz1/OpenTESArena) | Modern engine reimplementation of The Elder Scrolls: Arena by Bethesda Softworks. | 1,435 | 🟢 | C++ |
| [doukutsu-rs](https://github.com/doukutsu-rs/doukutsu-rs) | Rust reimplementation of the Cave Story engine | 1,318 | 🟢 | Rust |
| [Minosoft](https://github.com/Bixilon/Minosoft) | Open source Minecraft client reimplementation written from scratch | 1,317 | 🟢 | Kotlin |
| [GemRB](https://github.com/gemrb/gemrb) | Portable open-source reimplementation of the Infinity Engine (used by Baldur's Gate, Icewind Dale and more). | 1,264 | 🟢 | C++ |
| [OpenSpades](https://github.com/yvt/openspades) | Open-source client compatible with Ace of Spades 0.75 (PC) | 1,248 | 🟡 | C++ |
| [Diablerie](https://github.com/mofr/Diablerie) | Diablo 2 reimplementation on unity | 1,242 | 🔴 | C# |
| [Player](https://github.com/EasyRPG/Player) | EasyRPG Player, an open reimplementation of the RPG Maker 2000/2003 runtime | 1,239 | 🟢 | C++ |
| [Carmageddon (dethrace)](https://github.com/dethrace-labs/dethrace) | Reverse-engineered reimplementation / port of Carmageddon (dethrace) | 1,232 | 🟢 | C |
| [xoreos](https://github.com/xoreos/xoreos) | Reimplementation of BioWare's Aurora engine (KotOR, NWN, Jade Empire) | 1,192 | 🟢 | C++ |
| [The Force Engine](https://github.com/TheForceEngine/TheForceEngine) | Reimplementation of LucasArts' Jedi engine for Dark Forces and Outlaws | 1,170 | 🟢 | C++ |
| [Call of Duty: Modern Warfare 2 (IW4L)](https://github.com/vladtrc/iw4L) | Standalone Rust runtime for Call of Duty: Modern Warfare 2 (PC), built on bevy and wgpu | 1,160 | 🟢 | Rust |
| [RA2](https://github.com/OpenRA/ra2) | A Red Alert 2 mod for the OpenRA game engine | 1,143 | 🟢 | C# |
| [SurrealEngine](https://github.com/dpjudas/SurrealEngine) | Open-source reimplementation of Unreal Engine 1 that plays Unreal Tournament 99 | 1,127 | 🟢 | C++ |
| [Riiablo](https://github.com/collinsmith/riiablo) | Diablo II remade using Java and LibGDX | 1,106 | 🟡 | Java |
| [pikachu-volleyball](https://github.com/gorisanson/pikachu-volleyball) | Pikachu Volleyball reimplemented in JavaScript by reverse engineering the original game | 1,094 | 🟢 | JavaScript |
| [OpenHV](https://github.com/OpenHV/OpenHV) | Open-source implementation of Hard Vacuum. | 1,088 | 🟢 | C# |
| [Pal3.Unity](https://github.com/0x7c13/Pal3.Unity) | Unity reimplementation of The Legend of Sword and Fairy 3 and its expansion | 1,058 | 🟢 | C# |
| [Tomb Raider I & II (TRX)](https://github.com/LostArtefacts/TRX) | Reverse-engineered reimplementation / port of Tomb Raider I & II (TRX) | 1,024 | 🟢 | C |
| [RA2Web React](https://github.com/huangkaoya/ts-redalert2) | 红色警戒2源代码 Red Alert2 Source Code | 1,017 | 🟢 | TypeScript |
| [RigelEngine](https://github.com/lethal-guitar/RigelEngine) | Modern re-implementation of Duke Nukem II | 1,013 | 🟢 | C++ |
| [FreeSO](https://github.com/riperiperi/FreeSO) | Reimplementation of The Sims Online, targetted mainly at mobile devices. | 989 | 🟢 | C# |
| [WoWee (World of Warcraft)](https://github.com/Kelsidavis/WoWee) | Open-source World of Warcraft client engine written from scratch | 988 | 🟢 | C++ |
| [Crispy Doom](https://github.com/fabiangreffrath/crispy-doom) | Crispy Doom is a limit-removing enhanced-resolution Doom source port based on Chocolate Doom. | 965 | 🟢 | C |
| [NEO-RAW](https://github.com/fabiensanglard/Another-World-Bytecode-Interpreter) | "Fabother World" an interpreter for Another World (Out of this world). | 919 | 🟡 | C++ |
| [PICOLOVE](https://github.com/picolove/picolove) | PICO-8 fantasy console reimplementation in LÖVE | 891 | 🟡 | Lua |
| [Raze](https://github.com/ZDoom/Raze) | Build engine port backed by GZDoom tech. Currently supports Duke Nukem 3D, Blood, Shadow Warrior, Redneck Rampage and... | 891 | 🟢 | C++ |
| [Cannonball](https://github.com/djyt/cannonball) | OutRun arcade engine reimplementation | 887 | 🟡 | C++ |
| [Falltergeist](https://github.com/falltergeist/falltergeist) | Opensource crossplatform Fallout 2™ game engine writen in C++ and SDL. | 886 | 🔴 | C++ |
| [OpenEnroth](https://github.com/OpenEnroth/OpenEnroth) | Open reimplementation of the Might and Magic 6/7/8 game engine | 875 | 🟢 | C++ |
| [ReHLDS](https://github.com/rehlds/ReHLDS) | Reverse engineered, enhanced Half-Life Dedicated Server engine | 867 | 🟢 | C++ |
| [OpenNFS](https://github.com/OpenNFS/OpenNFS) | Attempt to recreate the classic Need for Speed Games (1-6). | 861 | 🟢 | C++ |
| [OpenMoHAA](https://github.com/openmoh/openmohaa) | Open re-implementation of Medal of Honor: Allied Assault | 849 | 🟢 | C |
| [PvZ-Portable](https://github.com/wszqkzqk/PvZ-Portable) | Cross-platform reimplementation of Plants vs. Zombies | 845 | 🟢 | C++ |
| [librw](https://github.com/aap/librw) | A re-implementation of the RenderWare Graphics engine | 830 | 🟢 | C++ |
| [NBlood](https://github.com/NBlood/NBlood) | Reverse-engineered ports of Build games using EDuke32 engine technology and development principles (NBlood/Rednukem/P... | 816 | 🟢 | C++ |
| [OpenTTD (OpenTTD-patches)](https://github.com/JGRennison/OpenTTD-patches) | OpenTTD (Transport Tycoon Deluxe reimplementation) with additional patches (PC) | 808 | 🟢 | C++ |
| [World of Warcraft 1.12 (benilla)](https://github.com/samwhosung/benilla) | World of Warcraft 1.12.1 client written from scratch in Rust and Bevy (PC) | 806 | 🟢 | Rust |
| [uMario](https://github.com/jakowskidev/uMario_Jakowski) | uMario C++/SDL2 Game by Łykasz Jakowski | 802 | 🔴 | C++ |
| [ReGameDLL_CS](https://github.com/rehlds/ReGameDLL_CS) | Reverse engineered server-side GameDLL for Counter-Strike 1.6 | 801 | 🟢 | C++ |
| [si78c](https://github.com/loadzero/si78c) | Memory-accurate C reimplementation of the Space Invaders arcade ROM | 797 | 🔴 | C |
| [SuperMarioBros-C](https://github.com/MitchellSternke/SuperMarioBros-C) | An attempt to translate the original Super Mario Bros. for the NES to readable C/C++ | 789 | 🔴 | C++ |
| [skate-3-rust-engine](https://github.com/SK8-ENGINE/skate-3-rust-engine) | Rust/Bevy skating engine based on Skate 3 reverse engineering research | 780 | 🟢 | Rust |
| [OpenJKDF2](https://github.com/shinyquagsire23/OpenJKDF2) | Cross-platform reimplementation of Star Wars Jedi Knight: Dark Forces II in C | 778 | 🟢 | C |
| [NFSIISE](https://github.com/zaps166/NFSIISE) | Need For Speed™ II SE - Cross-platform wrapper with 3D acceleration and TCP protocol! | 777 | 🟢 | C |
| [Stratagus](https://github.com/Wargus/stratagus) | Strategy game engine used by Wargus, Stargus and War1gus to run Blizzard RTS data | 743 | 🟢 | C++ |
| [ClassicUO](https://github.com/ClassicUO/ClassicUO) | Open-source reimplementation of the Ultima Online Classic client | 737 | 🟢 | C# |
| [jazz2-native](https://github.com/deathkiller/jazz2-native) | 🎮 · Jazz² Resurrection: Native C++ reimplementation of Jazz Jackrabbit 2 | 720 | 🟢 | C++ |
| [Memoria](https://github.com/Albeoris/Memoria) | Final Fantasy IX tools | 717 | 🟢 | C# |
| [OTClient](https://github.com/edubart/otclient) | Alternative Tibia client for OpenTibia servers in C++ and Lua | 707 | 🟡 | C++ |
| [Exult](https://github.com/exult/exult) | Engine reimplementation for Ultima VII: The Black Gate and Serpent Isle | 697 | 🟢 | C++ |
| [Thyme](https://github.com/TheAssemblyArmada/Thyme) | Open-source re-implementation of Command & Conquer Generals: Zero Hour | 696 | 🟡 | C++ |
| [OpenVIII](https://github.com/MaKiPL/OpenVIII-monogame) | Open source Final Fantasy VIII engine implementation in C# working on Windows and Linux (Android and iOS planned too!... | 672 | 🗄️ | C# |
| [Sonic 3 A.I.R.](https://github.com/Eukaryot/sonic3air) | Sonic 3 & Knuckles engine reimplementation (Angel Island Revisited) | 667 | 🟢 | C++ |
| [REGoth](https://github.com/REGoth-project/REGoth) | OpenSource-Reimplementation of the zEngine, used by the game "Gothic" | 654 | 🔴 | C++ |
| [GLSMAC](https://github.com/afwbkbc/glsmac) | Open-source reimplementation of Sid Meier's Alpha Centauri | 646 | 🟢 | C++ |
| [Portal 64: Still Alive](https://github.com/mwpenny/portal64-still-alive) | A demake of Portal for the Nintendo 64 | 632 | 🟢 | C |
| [Librelancer](https://github.com/Librelancer/Librelancer) | Reimplementation of the 2003 space game Freelancer. | 612 | 🗄️ |  |
| [OpenFodder](https://github.com/OpenFodder/openfodder) | Open-source reimplementation of Cannon Fodder | 612 | 🟢 | C++ |
| [OpenD2](https://github.com/eezstreet/OpenD2) | A project to open source Diablo 2. | 603 | 🔴 | C |
| [mkxp](https://github.com/Ancurio/mkxp) | mkxp, a free implementation of the RPG Maker Ruby Game Scripting System (RGSS) | 595 | 🟢 | C++ |
| [OpenSkyscraper](https://github.com/fabianschuiki/OpenSkyscraper) | Open source tower simulation game inspired by SimTower. | 591 | 🔴 | C++ |
| [OpenTS](https://github.com/OpenTS-Developers/OpenTS) | Open-source, reverse-engineered rebuild of the Command & Conquer: Tiberian Sun engine | 590 | 🟢 | C++ |
| [Warsmash](https://github.com/Retera/WarsmashModEngine) | Warcraft III engine emulation for modding | 585 | 🟢 | Java |
| [Jazz² Resurrection](https://github.com/deathkiller/jazz2) | Reimplementation of Jazz Jackrabbit 2. | 583 | 🟢 |  |
| [Helion (Doom)](https://github.com/Helion-Engine/Helion) | Doom engine written from scratch in C# that plays the original WAD data | 574 | 🟢 | C# |
| [Carnage3D](https://github.com/codenamecpp/carnage3d) | Reimplementation of Grand Theft Auto 1 | 573 | 🟢 | C++ |
| [The Legend of Dragoon (Severed Chains)](https://github.com/Legend-of-Dragoon-Modding/Severed-Chains) | Reverse-engineered reimplementation / port of The Legend of Dragoon (Severed Chains) | 569 | 🟢 | Java |
| [Project Alice](https://github.com/schombert/Project-Alice) | Project Alice, an open-source reimplementation of Victoria II that uses the original data | 561 | 🟢 | C++ |
| [sm (Super Metroid)](https://github.com/snesrev/sm) | C reimplementation of Super Metroid from reverse-engineered SNES code | 560 | 🔴 | C |
| [NXEngine-evo](https://github.com/nxengine/nxengine-evo) | Engine rewrite of Cave Story (Doukutsu Monogatari) | 553 | 🟢 | C |
| [Ambermoon.net](https://github.com/Pyrdacor/Ambermoon.net) | Ambermoon rewrite in C# | 544 | 🟢 | C# |
| [OTClient (Redemption)](https://github.com/opentibiabr/otclient) | Modern C++20 fork-successor of OTClient for Tibia-compatible servers | 540 | 🟢 | Lua |
| [KisakCOD](https://github.com/SwagSoftware/KisakCOD) | Open-source reimplementation of Call of Duty 4 multiplayer | 528 | 🟢 | C++ |
| [Akhenaten](https://github.com/dalerank/Akhenaten) | Open-source reimplementation of Pharaoh (Impressions Games) | 520 | 🟢 | C++ |
| [OpenClaw](https://github.com/pjasicek/OpenClaw) | Reimplementation of the Captain Claw (1997) platformer | 520 | 🔴 | C++ |
| [TOMB5](https://github.com/TOMB5/TOMB5) | Tomb Raider: Chronicles Disassembly translated to C source code. | 520 | 🔴 | C |
| [Simitone](https://github.com/riperiperi/Simitone) | Re-implementation of The Sims 1, based off of FreeSO. | 502 | 🟡 | C# |
| [REGoth](https://github.com/REGoth-project/REGoth-bs) | An open source reimplementation of zEngine the engine behind Gothic and Gothic II. | 500 | 🔴 | C++ |
| [FreeSpace 2 Source Code Project](https://github.com/scp-fs2open/fs2open.github.com) | Origin Repository for SCP FreeSpace 2 Open | 496 | 🟢 | C++ |
| [Miu2D](https://github.com/luckyyyyy/miu2d) | Miu2D is a 2D RPG game engine built with Rust + TypeScript + React + Canvas, designed for the Web platform. 剑侠情缘2/月影传... | 490 | 🟢 | TypeScript |
| [Vange-rs](https://github.com/kvark/vange-rs) | Rusty Vangers clone | 488 | 🟢 | Rust |
| [donut](https://github.com/plowteam/donut) | Reimplementation of The Simpsons: Hit & Run in modern C++ and modern OpenGL. | 487 | 🟡 | C++ |
| [OpenLiberty](https://github.com/openfw-game/OpenLiberty) | GTA III reimplementation in the Godot engine loading original assets | 478 | 🟢 | GDScript |
| [OpenVic](https://github.com/OpenVicProject/OpenVic) | Main Repo for the OpenVic Project | 478 | 🟢 | GDScript |
| [Nanosaur](https://github.com/jorio/Nanosaur) | Nanosaur source port 🦖 | 475 | 🟢 | C |
| [cs16-client](https://github.com/FWGS/cs16-client) | Reverse engineered Counter-Strike 1.6 client for the Xash3D engine | 471 | 🟢 | C++ |
| [McOsu](https://github.com/McKay42/McOsu) | Unofficial osu! practice client with VR support | 470 | 🟢 | C++ |
| [Super Mario 64 (DualShock Version)](https://github.com/malucard/sm64-psx) | A very WIP port of https://www.github.com/n64decomp/sm64 for the PlayStation 1 | 464 | 🗄️ | C |
| [Wargus](https://github.com/Wargus/wargus) | Importer and scripts for Warcraft II: Tides of Darkness, the expansion Beyond the Dark Portal, and Aleonas Tales | 445 | 🟢 | C |
| [Alive Reversing](https://github.com/AliveTeam/alive_reversing) | Reimplementation of Oddworld: Abe's Exoddus. | 444 | 🟢 | C++ |
| [OpenTS2](https://github.com/LazyDuchess/OpenTS2) | Open source re-implementation of The Sims 2 in Unity | 438 | 🟢 | C# |
| [Chariot](https://github.com/ChariotEngine/Chariot) | Reimplementation of the Age of Empires (1997) engine in Rust | 427 | 🔴 | Rust |
| [cinnamon](https://github.com/Project-Sunshine-Native/cinnamon) | GameMaker GML runner reimplementation in C for 3DS and Wii U | 420 | 🟢 | C |
| [OpenJazz](https://github.com/AlisterT/openjazz) | Engine reimplementation of Jazz Jackrabbit; uses original game data (C++) | 414 | 🟢 | C |
| [OpenGMK](https://github.com/OpenGMK/OpenGMK) | Open-source runner for GameMaker 8.1 and earlier games, with TAS tools | 410 | 🟢 | Rust |
| [Butterscotch](https://github.com/ButterscotchRunner/Butterscotch) | Open source reimplementation of the GameMaker: Studio runner | 401 | 🟢 | C |
| [ResidualVM](https://github.com/residualvm/residualvm) | Engine reimplementation for 3D adventures like Grim Fandango (archived; merged into ScummVM) | 401 | 🗄️ | C++ |
| [OpenBVE](https://github.com/leezer3/OpenBVE) | Open-source train simulator that runs BVE Trainsim routes and trains | 380 | 🟢 | C# |
| [BStone](https://github.com/bibendovsky/bstone) | Unofficial source port for Blake Stone series | 373 | 🟢 | C |
| [Duke Nukem II (Reconstructed)](https://github.com/lethal-guitar/Duke2Reconstructed) | Reverse-engineered reimplementation / port of Duke Nukem II (Reconstructed) | 373 | 🟡 | C |
| [PokeSwift](https://github.com/Dimillian/PokeSwift) | Reimplementation of the Pokemon Red/Blue engine in Swift | 363 | 🟢 | Assembly |
| [OpenMW for Android](https://github.com/xyzz/openmw-android) | OpenMW for Android | 362 | 🗄️ | Java |
| [3SX](https://github.com/crowded-street/3sx) | "The Third of the Third" ported to modern platforms | 361 | 🟢 | C |
| [open-realm](https://github.com/corepunch/open-realm) | Open-source reimplementation of the Warcraft III engine | 356 | 🟢 | C |
| [OpenSWE1R](https://github.com/OpenSWE1R/openswe1r) | Open-source reimplementation of Star Wars Episode I: Racer | 350 | 🔴 | C |
| [Tomb Engine](https://github.com/TombEngine/TombEngine) | A new and modern engine for custom Tomb Raider levels incorporating classic features and new enhancements. | 347 | 🟢 | C++ |
| [pikachu-volleyball-p2p-online](https://github.com/gorisanson/pikachu-volleyball-p2p-online) | Peer-to-peer online play for the reverse engineered Pikachu Volleyball | 343 | 🟢 | JavaScript |
| [Freeserf](https://github.com/freeserf/freeserf) | Settlers 1 (Serf City) clone. | 341 | 🟢 | C++ |
| [UnderworldExporter](https://github.com/hankmorgan/UnderworldExporter) | Updated Release 27th Oct 2018 Unity based port of Ultima Underworld I and II. Download under releases | 340 | 🗄️ | C# |
| [F.LF (Little Fighter 2)](https://github.com/Project-F/F.LF) | Open-source engine reimplementation of Little Fighter 2 that runs on the original game data | 338 | 🟡 | JavaScript |
| [FreeSims](https://github.com/francot514/FreeSims) | Open source engine used for The Sims | 333 | 🟢 | C# |
| [UnderworldGodot](https://github.com/hankmorgan/UnderworldGodot) | An engine recreation of Ultima Underworld and Ultima Underworld 2 in the Godot Engine. | 332 | 🟢 | C# |
| [open-ig](https://github.com/akarnokd/open-ig) | Open-source reimplementation of Imperium Galactica | 326 | 🟢 | Java |
| [FreeHL](https://github.com/eukara/freehl) | Clean-room reimplementation of Half-Life and HL: Deathmatch in QuakeC | 321 | 🟢 | QuakeC |
| [Abyss Engine](https://github.com/AbyssEngine/AbyssEngine) | Abyss Engine clean-room reimplementation of Diablo 2, written in C. The goal is to recreate the original game engine,... | 320 | 🟡 | C |
| [reone](https://github.com/seedhartha/reone) | Game engine reimplementation for Star Wars: KotOR I and II | 320 | 🟡 | C++ |
| [Omnispeak](https://github.com/sulix/omnispeak) | Reimplementation of Commander Keen in Goodbye Galaxy. | 318 | 🟢 | C |
| [Theseus](https://github.com/MrMilenko/Theseus) | Reverse-engineered reconstruction of the original Xbox 5960 dashboard | 313 | 🟢 | C++ |
| [open-supaplex](https://github.com/sergiou87/open-supaplex) | Reverse engineered open source port of Supaplex | 312 | 🟢 | C |
| [CroftEngine](https://github.com/stohrendorf/CroftEngine) | An open-source Tomb Raider 1 engine remake | 311 | 🟢 | C++ |
| [freecs](https://github.com/eukara/freecs) | Clean-room Counter-Strike 1.5 in QuakeC using the Nuclide SDK | 303 | 🟡 | QuakeC |
| [Resident Evil 2 (OpenBiohazard2)](https://github.com/OpenBiohazard2/OpenBiohazard2) | Reverse-engineered reimplementation / port of Resident Evil 2 (OpenBiohazard2) | 302 | 🟢 | Go |
| [MafiaUnity](https://github.com/MafiaHub/MafiaUnity) | 🕹 Open-source Mafia game framework | 294 | 🗄️ | C# |
| [lba2remake](https://github.com/LBALab/lba2remake) | A Little Big Adventure 2 / Twinsen's Odyssey reimplementation in JavaScript / Three.js / React | 288 | 🟢 | TypeScript |
| [Wowser](https://github.com/wowserhq/wowser) | World of Warcraft client in the browser using JavaScript and WebGL | 287 | 🔴 | JavaScript |
| [BetterSpades](https://github.com/xtreme8000/BetterSpades) | Ace of Spades 0.75 compatible game client for low-end systems (PC) | 286 | 🟡 | C |
| [type-pal (Legend of Sword and Fairy)](https://github.com/IllegalCreed/type-pal) | From-scratch TypeScript remake of The Legend of Sword and Fairy (1995) that runs in the browser | 286 | 🟢 | TypeScript |
| [PrinceJS](https://github.com/ultrabolido/PrinceJS) | Prince of Persia reimplementation in HTML5/JavaScript | 282 | 🟡 | JavaScript |
| [spearmint](https://github.com/clover-moe/spearmint) | Spearmint — an updated id Tech 3 engine for continuing the classics and creating new games. | 282 | 🟢 | C |
| [Moondust Project](https://github.com/WohlSoft/Moondust-Project) | Moondust, an open-source engine reimplementation of Super Mario Bros. X (SMBX) | 281 | 🟢 | C++ |
| [Sourcehold](https://github.com/sourcehold/Sourcehold) | Open source re-implementation of Stronghold 1 | 281 | 🟡 | C++ |
| [Super-Mario-World-Remastered-Public](https://github.com/JHDev2006/Super-Mario-World-Remastered-Public) | A Remake / Remaster of the original Super Mario World, in Godot. Adds new features / improvements! | 281 | 🗄️ | GDScript |
| [Doom64EX](https://github.com/svkaiser/Doom64EX) | Reverse engineered recreation of Doom 64 with modding features | 274 | 🟢 | C++ |
| [The Eternity Engine](https://github.com/team-eternity/eternity) | The Eternity Engine | 274 | 🟢 | C++ |
| [Heretic2R](https://github.com/m-x-d/Heretic2R) | Heretic II (1998, Raven Software) reverse-engineered source port. | 272 | 🟢 | C |
| [DGEngine](https://github.com/dgcor/DGEngine) | Implementation of the Diablo game engine. | 270 | 🟡 | C++ |
| [CivOne](https://github.com/Solen1985/CivOne) | Implementation of Sid Meier's Civilization. | 261 | 🔴 | C# |
| [OpenBW](https://github.com/OpenBW/openbw) | Open-source StarCraft: Brood War engine reimplementation | 261 | 🟢 | C++ |
| [OpenMBU](https://github.com/MBU-Team/OpenMBU) | OpenMBU is a revival of Marble Blast Ultra, the 2006 Xbox 360 arcade classic. | 261 | 🟢 | C++ |
| [pokemon-tbje (Pokémon)](https://github.com/zachMahan64/pokemon-tbje) | Open-source engine reimplementation of Pokémon that runs on the original game data | 252 | 🟢 | Java |
| [OpenGD](https://github.com/Open-GD/OpenGD) | Open source implementation of Geometry Dash | 249 | 🟡 | C++ |
| [undertale](https://github.com/fachinformatiker/undertale) | Undertale src code | 249 | 🔴 | Game Maker Language |
| [2006scape](https://github.com/2006-Scape/2006Scape) | A 2006 Runescape Emulation Server | 246 | 🟢 | Java |
| [freeaoe](https://github.com/sandsmark/freeaoe) | A free game engine capable of running Age of Empires 2 and Star Wars: Galactic Battlegrounds | 241 | 🔴 | C++ |
| [Kinoko](https://github.com/vabold/Kinoko) | Reimplementation of Mario Kart Wii's physics engine in C++ | 238 | 🟢 | C++ |
| [KisakBlack](https://github.com/SwagSoftware/KisakBlack) | Open source reimplementation of Call of Duty: Black Ops | 237 | 🟢 | C++ |
| [srceng-android](https://github.com/nillerusr/srceng-android) | Android launcher for source engine | 234 | 🔴 | Java |
| [nanolathe](https://github.com/nanolathe-gg/nanolathe) | Total Annihilation engine reimplementation in Go | 231 | 🟢 | Go |
| [Doom 64 EX+](https://github.com/atsb/Doom64EX-Plus) | An improved modern version of Doom64EX. | 230 | 🗄️ | C |
| [OpenAWE](https://github.com/OpenAWE-Project/OpenAWE) | A reimplementation of Remedy Entertainments Alan Wake Engine, in later iterations known as the Northlight Engine | 221 | 🟢 | C++ |
| [cssDOOM](https://github.com/NielsLeenheer/cssDOOM) | Doom engine implemented in CSS; plays the original WAD data in a browser | 211 | 🟢 | JavaScript |
| [rawgl](https://github.com/cyxx/rawgl) | Another World/Out of This World engine reimplementation (SDL, OpenGL) | 209 | 🗄️ | C++ |
| [MegaManXSNESRecomp](https://github.com/mstan/MegaManXSNESRecomp) | Mega Man X recompiled for the Super Nintendo using snesrecomp · Part of the R.A.I.D. community | 207 | 🟢 | C |
| [impacto](https://github.com/CommitteeOfZero/impacto) | Reimplementation of the MAGES. visual novel engine | 206 | 🟢 | C++ |
| [Cave Story (CSE2)](https://github.com/gameblabla/CSE2) | Reverse-engineered reimplementation / port of Cave Story (CSE2) | 203 | 🟢 | C++ |
| [Galaxy on Fire 2 Unity Remake](https://github.com/JoppieToppie/Galaxy-on-Fire-2-Unity-Remake) | Galaxy on Fire 2 decompilation and Unity remake | 202 | 🟢 | C |
| [Duck Game Rebuilt](https://github.com/TheFlyingFoool/DuckGameRebuilt) | Duck Game decompiled & rebuilt with some added features, | 199 | 🟢 | C# |
| [NXEngine (Cave Story)](https://github.com/EXL/NXEngine) | NXEngine, an open-source rewrite of the Cave Story engine; ports for various platforms | 199 | 🔴 | C++ |
| [OpenNFS1](https://github.com/jeff-1amstudios/OpenNFS1) | Remake of the original EA Need for Speed 1 using c# and Monogame | 198 | 🔴 | C# |
| [Reburn 3](https://github.com/reburndev/reburn3) | A work-in-progress open source reimplementation of Burnout 3: Takedown. | 196 | 🟡 | C++ |
| [z2rs](https://github.com/troyedwardsjr/z2rs) | Clean-room reconstruction of Zelda II: The Adventure of Link in Rust | 195 | 🟢 | Rust |
| [FreeFT](https://github.com/nadult/FreeFT) | Isometric action game engine | 194 | 🟢 | C++ |
| [Vib-Ribbon (open-ribbon)](https://github.com/open-ribbon/open-ribbon) | Reverse-engineered reimplementation / port of Vib-Ribbon (open-ribbon) | 193 | 🟡 | C |
| [XL Engine](https://github.com/Mindwerks/XLEngine) | XLEngine allows you to play Dark Forces, Daggerfall and soon Outlaws and Blood with modern technology. | 193 | 🔴 | C++ |
| [KaM Remake](https://github.com/reyandme/kam_remake) | "KaM Remake" is an RTS game remake written in Delphi from scratch. | 188 | 🟢 | Pascal |
| [Open Panzer](https://github.com/nicupavel/openpanzer) | JavaScript/HTML5 rewrite of Panzer General 2 (PC) | 188 | 🔴 | JavaScript |
| [sh3redux](https://github.com/Palm-Studios/sh3redux) | SILENT HILL 3 Engine Remake in OpenGL and C++ | 188 | 🟡 | C++ |
| [Panzer Dragoon Saga (Azel)](https://github.com/yaz0r/Azel) | Reverse-engineered reimplementation / port of Panzer Dragoon Saga (Azel) | 184 | 🟢 | C++ |
| [Powerslave EX](https://github.com/svkaiser/PowerslaveEX) | Powerslave EX is a unofficial recreation of Lobotomy Software’s obscured FPS game, Powerslave (also known as Exhumed... | 184 | 🔴 | C |
| [lofp](https://github.com/metavert-io/lofp) | Recreation of Legends of Future Past, the 1990s commercial MUD | 183 | 🟢 | HTML |
| [nv-rs](https://github.com/slaterain/nv-rs) | Experimental Fallout: New Vegas engine reimplementation in Rust and Bevy | 183 | 🟢 | Rust |
| [pokered-gbc](https://github.com/dannye/pokered-gbc) | Pokémon Red/Blue overhauled with full GBC support. Made by FroggestSpirit, Drenn, and dannye. Also check out the crys... | 182 | 🟢 | Assembly |
| [eZeus](https://github.com/MaurycyLiebner/eZeus) | Open-source implementation of Zeus: Master of Olympus. | 181 | 🟢 | C++ |
| [Chasm-Reverse](https://github.com/Panzerschrek/Chasm-Reverse) | "PanzerChasm" is a free recreation of the game "Chash: - The Rift" by "ActionForms" using the original game data (CSM... | 180 | 🟢 | C++ |
| [Vault13](https://github.com/pingw33n/vault13) | Reimplementation of the Fallout 2 engine in Rust | 179 | 🗄️ | Rust |
| [CrossUO (Ultima Online)](https://github.com/crossuo/crossuo) | Open-source cross-platform Ultima Online client | 177 | 🟢 | C++ |
| [Open Horizon](https://github.com/undefined-darkness/open-horizon) | Engine reimplementation of Ace Combat: Assault Horizon; uses original game data (C++) | 177 | 🔴 | C++ |
| [Legacy of Kain: Soul Reaver Decompile](https://github.com/Gh0stBlade/KAIN2) | Legacy of Kain: Soul Reaver Decompile | 176 | 🟡 | C |
| [JXQY-all-in-one](https://github.com/Upwinded/JXQY-all-in-one) | 剑侠情缘 Sword Heroes' Fate | 175 | 🟢 | C++ |
| [openDarkEngine (Thief)](https://github.com/volca02/openDarkEngine) | Rewrite of the Looking Glass Dark Engine (Thief) that uses the original data | 174 | 🔴 | C++ |
| [OpenMC2](https://github.com/OpenMC2/OpenMC2) | An Open Source Re-Implementation of Midnight Club 2 | 174 | 🔴 | C++ |
| [OUO](https://github.com/draxinar/ouo) | OUO: reverse engineering of Ultima Online: The Second Age server | 173 | 🟢 | C |
| [Arcanum Community Edition](https://github.com/alexbatalov/arcanum-ce) | Arcanum for modern operating systems | 172 | 🟢 | C |
| [openc2e (Creatures)](https://github.com/openc2e/openc2e) | openc2e, open-source engine for the Creatures games that uses the original data | 170 | 🟢 | C++ |
| [OpenHoW](https://github.com/hogsy/OpenHoW) | Open-source reimplementation of Gremlin's Hogs of War (PC/PSX). | 170 | 🗄️ | C |
| [rlvm](https://github.com/eglaysher/rlvm) | RealLive clone for Linux and OSX | 170 | 🟡 | C++ |
| [whoa](https://github.com/whoahq/whoa) | Unofficial open-source reimplementation of the World of Warcraft 3.3.5 client | 170 | 🟢 | C++ |
| [Citadel (System Shock)](https://github.com/JosiahJack/Citadel) | System Shock fan remake that uses the original game data | 169 | 🟢 | C# |
| [OpenC1](https://github.com/jeff-1amstudios/OpenC1) | Remake of Carmageddon 1 engine | 168 | 🔴 | C# |
| [openQ4](https://github.com/themuffinator/openQ4) | Open-source reimplementation of Quake 4 | 167 | 🟢 | C++ |
| [ElonaFoobar](https://github.com/elonafoobar/elonafoobar) | One of the Elona variants | 165 | 🗄️ | C++ |
| [Nuvie](https://github.com/nuvie/nuvie) | Nuvie - New Ultima VI Engine | 165 | 🟡 | C++ |
| [dunedynasty](https://github.com/gameflorist/dunedynasty) | Remaster of Dune II built on the OpenDUNE reverse engineered codebase | 164 | 🟢 | C |
| [OpenTPW](https://github.com/OpenTPW/OpenTPW) | An open-source re-implementation of Bullfrog's Sim Theme Park / Theme Park World (1999). | 162 | 🟢 | C# |
| [vitaXash3D](https://github.com/fgsfdsfgs/vitaXash3D) | Port of the Xash3D FWGS GoldSrc-compatible engine to the PS Vita | 162 | 🔴 | C |
| [SeriousSamClassic-VK](https://github.com/tx00100xt/SeriousSamClassic-VK) | Open source game engine for Serious Sam Classic with Vulkan support. | 161 | 🟢 | C++ |
| [OpenNefia](https://github.com/OpenNefia/OpenNefia) | Moddable engine reimplementation of the Japanese roguelike Elona. | 160 | 🟡 | C# |
| [PlantsVsZombies.NET](https://github.com/Mewnojs/PlantsVsZombies.NET) | C# reimplementation of Plants vs. Zombies (PC) | 160 | 🟢 | C# |
| [Free in the Dark](https://github.com/yaz0r/FITD) | Free in the Dark, a Alone in the Dark engine reimplementation. | 159 | 🟡 | C++ |
| [Stargus](https://github.com/Wargus/stargus) | Importer and scripts for Starcraft | 158 | 🟢 | C++ |
| [Zuma-Deluxe-HD](https://github.com/GalaxyShad/Zuma-Deluxe-HD) | A remake of the legendary 2003 PopCap game with improved textures and support for 16:9 aspect ratio. | 156 | 🟢 | C |
| [OGS](https://github.com/headcrab-junkyard/OGS) | An open-source GoldSrc engine clone (Clean authentic reimplementation without using reverse-engineered code) | 155 | 🟡 | C |
| [OpenAG](https://github.com/YaLTeR/OpenAG) | Open-source reimplementation of the Adrenaline Gamer client library | 154 | 🟡 | C++ |
| [remc2](https://github.com/turican0/remc2) | Reverse engineering of Magic Carpet 2 from Assembler. | 153 | 🟢 | C++ |
| [engge](https://github.com/scemino/engge) | Open source remake of Thimbleweed Park's engine | 151 | 🗄️ | C++ |
| [hode](https://github.com/usineur/hode) | hode is a rewrite (made by Grégory Montoir) of the engine used in the game Heart of Darkness made by Amazing Studio. | 151 | 🟡 | C++ |
| [KotOR.js](https://github.com/KobaltBlu/KotOR.js) | A remake of the Odyssey Game Engine that powered KotOR I & II written in JavaScript | 151 | 🟢 | TypeScript |
| [rfvp](https://github.com/xmoezzz/rfvp) | Non-official Rust implementation of the FVP visual novel engine | 150 | 🟢 | Rust |
| [kys-pascal](https://github.com/scarsty/kys-pascal) | 《金庸群侠传》Pascal重制版 | 149 | 🟢 | Pascal |
| [Test Drive Unlimited (OpenTestDriveUnlimited)](https://github.com/opentestdriveunlimited/OpenTestDriveUnlimited) | Reverse-engineered reimplementation / port of Test Drive Unlimited (OpenTestDriveUnlimited) | 146 | 🟢 | C++ |
| [darkfo](https://github.com/darkf/darkfo) | DarkFO, a post-nuclear RPG remake (of Fallout 2) | 145 | 🗄️ | TypeScript |
| [Elite: The New Kind](https://github.com/fesh0r/newkind) | Elite: The New Kind, a C reimplementation of BBC Micro Elite built by reverse engineering | 145 | 🔴 | C |
| [OpenMB](https://github.com/cookgreen/OpenMB) | Role-playing game engine for Taleworlds' Mount&Blade Series. | 145 | 🟢 | C# |
| [JSettlers](https://github.com/paulwedeck/settlers-remake) | A Remake of "The Settlers III" for Windows, Linux and Android | 144 | 🗄️ | Java |
| [Ratchet & Clank](https://github.com/re-rac/rerac-launcher) | Launcher for ReRAC, a rewrite of Ratchet & Clank (PS2) | 143 | 🟢 | Rust |
| [Strife: Veteran Edition](https://github.com/svkaiser/strife-ve) | Strife Veteran Edition GPL Source Release | 143 | 🔴 | C |
| [Q-Gears](https://github.com/q-gears/q-gears) | Q-Gears is an RPG engine for games like Squaresoft's Final Fantasy 7, 8, 9, or Xenogears. It is designed to be cross-... | 142 | 🔴 | C++ |
| [unity-arcanum](https://github.com/Suvitruf/unity-arcanum) | Fan-made reimplementation of the Arcanum engine in Unity | 142 | 🟢 | C# |
| [UA_source](https://github.com/Marisa-Chan/UA_source) | Mod for UrbanAssault (Replace original game engine) | 139 | 🟡 | C++ |
| [Litecraft](https://github.com/KernelFreeze/Litecraft) | Clean-room open source Minecraft client implementation | 138 | 🗄️ | Rust |
| [Uncharted waters 2 remake](https://github.com/JohanLi/uncharted-waters-2) | Browser-based remake of Uncharted Waters: New Horizons (大航海時代II) | 138 | 🟢 | TypeScript |
| [War1gus](https://github.com/Wargus/war1gus) | Importer and scripts for Warcraft: Orcs and Humans | 136 | 🟢 | Lua |
| [Free Heroes 2 - Enhanced](https://github.com/ciplogic/fheroes2enh) | Free Heroes 2 - Enhanced | 135 | 🔴 | C++ |
| [MikuPan](https://github.com/Mikompilation/MikuPan) | PC Port Of Fatal Frame 1 Based On Himuro | 134 | 🟢 | C++ |
| [The-Great-Escape-in-C](https://github.com/dpt/The-Great-Escape-in-C) | Classic ZX Spectrum game "The Great Escape" rewritten in portable C | 134 | 🟢 | C |
| [Raptor](https://github.com/skynettx/raptor) | Reversed-engineered source port from Raptor Call Of The Shadows | 133 | 🟢 | C |
| [aoe](https://github.com/FolkertVanVerseveld/aoe) | Re-implementation of Age of Empires and the Rise of Rome expansion | 132 | 🟢 | C++ |
| [Yukon](https://github.com/wizguin/yukon) | HTML5 Club Penguin client reimplementation | 131 | 🟡 | JavaScript |
| [OpenRoads (SkyRoads)](https://github.com/anprogrammer/OpenRoads) | Open-source reimplementation of SkyRoads (DOS) | 130 | 🔴 | JavaScript |
| [Umineko Project](https://github.com/umineko-project/onscripter-ru) | ONScripter-RU game engine | 129 | 🔴 | C++ |
| [lttp-phaser](https://github.com/englercj/lttp) | An incomplete remake of The Legend of Zelda - A Link to the Past using WebGL and the browser. | 126 | 🔴 | TypeScript |
| [OpenATDeluxe (Airline Tycoon)](https://github.com/openairlinetycoon/OpenATDeluxe) | Open-source remake of Airline Tycoon Deluxe that uses the original game data | 126 | 🔴 | C# |
| [Ozymandias (Julius)](https://github.com/Banderi/Ozymandias_Julius) | An open source re-implementation of Pharaoh (1999) in the Julius/Augustus engine | 126 | 🟢 | C++ |
| [Prey 2006: A Talon Brave Game](https://github.com/FriskTheFallenHuman/Prey2006) | Prey 2006 SDK integrated with Doom 3 GPL release | 126 | 🟢 | C |
| [Robot War Engine](https://github.com/MHeasell/rwe) | Robot War Engine - Real-time strategy game engine compatible with Total Annihilation | 126 | 🟢 | C++ |
| [Paper Mario DX](https://github.com/bates64/papermario-dx) | Improved Paper Mario (N64) engine for your next romhack | 125 | 🟢 | C |
| [CrossCraft](https://github.com/CrossCraft/CrossCraft) | Open-source Minecraft reimplementation | 124 | 🟢 | Zig |
| [OpenNefia](https://github.com/Ruin0x11/OpenNefia) | Moddable engine reimplementation of the roguelike Elona | 122 | 🟡 | Lua |
| [lain-bootleg-bootleg](https://github.com/ad044/lain-bootleg-bootleg) | Reverse engineering and remake of Lain Bootleg | 121 | 🟢 | C |
| [siglus_rs](https://github.com/xmoezzz/siglus_rs) | Unofficial Rust implementation of the SiglusEngine visual novel engine | 121 | 🟢 | Rust |
| [OpenMoM (Master of Magic)](https://github.com/Jakz/openmom) | Open-source reimplementation of Master of Magic | 117 | 🟡 | C++ |
| [Apolyton Call to Power II Source Code Project](https://github.com/civctp2/civctp2) | Call to Power II: Apolyton Edition source code project. Call to Power II (CTP2) is a civilization computer game, whos... | 116 | 🟢 | C |
| [OpenUG2](https://github.com/whoismept/OpenUG2) | From-scratch reimplementation of Need for Speed: Underground 2 | 116 | 🟢 | C |
| [Magic Carpet 2 HD](https://github.com/thobbsinteractive/magic-carpet-2-hd) | Recode Binary code of game Magic Carpet2 to C/C++ language(remake MC2 for any platform) | 114 | 🟢 | C++ |
| [opendpr](https://github.com/TeamLumi/opendpr) | Reverse engineered recreation of Pokemon Brilliant Diamond and Shining Pearl | 114 | 🟢 | C# |
| [Tapir (RPG Maker)](https://github.com/qnighy/tapir) | Tapir, an RGSS-compatible runtime for RPG Maker XP, VX and VX Ace games | 113 | 🗄️ | C |
| [1oom](https://github.com/1oom-fork/1oom) | 1oom is a Master of Orion Classic (1993) game engine recreation that requires the original files to run. | 112 | 🟢 | C |
| [Ambermoon](https://github.com/Pyrdacor/Ambermoon) | Resources and reimplementation for the Amiga game Ambermoon | 112 | 🟢 | Assembly |
| [Dune2JS](https://github.com/oklemenz/Dune2JS) | Dune II reimplementation in HTML5/JavaScript | 112 | 🟡 | JavaScript |
| [Javascript BoulderDash](https://github.com/jakesgordon/javascript-boulderdash) | An HTML5 implementation of the c64 classic Boulderdash game | 112 | 🟡 | JavaScript |
| [Gorc](https://github.com/jdmclark/gorc) | Early-development Jedi Knight: Dark Forces 2 game engine recreation | 110 | 🔴 | C++ |
| [Civ2-clone](https://github.com/axx0/Civ2-clone) | Open-source re-implementation of Civilization 2 | 109 | 🟢 | C# |
| [Ikemen-Plus-Ultra (M.U.G.E.N)](https://github.com/CableDorado2/Ikemen-Plus-Ultra) | IKEMEN, an open-source reimplementation of the M.U.G.E.N fighting game engine | 109 | 🟢 | C |
| [Lemmings.ts](https://github.com/tomsoftware/Lemmings.ts) | A Web Lemmings Clone/Remake in TypeScript | 109 | 🔴 | TypeScript |
| [MegaManX4Recomp](https://github.com/mstan/MegaManX4Recomp) | Mega Man X4 (USA, SLUS-00561) statically recompiled to a native PC executable with PSXRecomp | 108 | 🟢 | C |
| [libRealSpace (Strike Commander)](https://github.com/fabiensanglard/libRealSpace) | Reimplementation of the Origin RealSpace engine for Strike Commander | 107 | 🗄️ | C++ |
| [Knytt Stories (YKnytt)](https://github.com/youkaicountry/yknytt) | Reimplementation of Knytt Stories in Godot that plays original levels (PC) | 105 | 🟢 | C# |
| [neo](https://github.com/NeotokyoRebuild/neo) | NEOTOKYO;REBUILD: reimplementation and continuation of the NEOTOKYO mod on a TF2 engine branch | 103 | 🟢 | C++ |
| [lithtech](https://github.com/Katana-Steel/lithtech) | Engine reimplementation of F.E.A.R., The Operative: No One Lives Forever; uses original game data (C++) | 102 | 🟢 | C++ |
| [cavestory-sdl2](https://github.com/JIghtuse/cavestory-sdl2) | Reconstructing Cave Story with SDL 2.0 and C++14 | 101 | 🔴 | C++ |
| [DreeRally](https://github.com/enriquesomolinos/DreeRally) | Death Rally engine reimplementation | 101 | 🔴 | C |
| [tf15-client](https://github.com/FWGS/tf15-client) | Reverse engineered Team Fortress Classic client for Xash3D | 100 | 🟡 | C++ |
| [Barnyard (OpenBarnyard)](https://github.com/InfiniteC0re/OpenBarnyard) | Reverse-engineered reimplementation / port of Barnyard (OpenBarnyard) | 98 | 🟢 | C++ |
| [OpenCity2k](https://github.com/OpenCity2k/OpenCity2k) | Open source reimplementation of SimCity 2000 | 98 | 🟡 | Python |
| [Redguard Unity](https://github.com/RGUnity/redguard-unity) | Main repository containing the Unity project and the wiki | 98 | 🟢 | C# |
| [ko](https://github.com/ko4life-net/ko) | Open source reverse engineered recreation of an old Knight Online version | 94 | 🟡 | C++ |
| [OpenCrystalCaves](https://github.com/OpenCrystalCaves/OpenCrystalCaves) | OCC is an unofficial open source engine reimplementation of the game trilogy Crystal Caves. | 93 | 🟢 | C++ |
| [PC port of Animal Crossing](https://github.com/ACreTeam/forest) | PC Port of Animal Crossing | 93 | 🟢 | C |
| [UchuServer](https://github.com/UchuServer/Uchu) | LEGO Universe server written in C# | 93 | 🟡 | C# |
| [Executive Man](https://github.com/CamHenlin/ExecutiveMan) | ExecutiveMan, a JavaScript MegaMan clone | 92 | 🔴 | JavaScript |
| [OpenSC4](https://github.com/OpenSC4-org/OpenSC4) | Open source reimplementation of SimCity 4 | 92 | 🟡 | GDScript |
| [OpenVice](https://github.com/clashbyte/openvice) | Grand Theft Auto: Vice City Open Source port to C# | 92 | 🟡 | C# |
| [twin-e](https://github.com/LBALab/twin-e) | TwinEngine: open-source reimplementation of the Little Big Adventure engine (DOS) | 92 | 🟡 | C |
| [The Great Escape](https://github.com/dpt/The-Great-Escape) | Classic ZX Spectrum game "The Great Escape" reverse engineered | 90 | 🟡 | Assembly |
| [dejavu](https://github.com/rpjohnst/dejavu) | Game Maker runtime reimplementation | 89 | 🟡 | Rust |
| [librwgta](https://github.com/aap/librwgta) | GTA-specific extensions to librw (RenderWare reimplementation) and tools using it | 89 | 🟢 | C++ |
| [Pizza Tower (OpenTower)](https://github.com/femloy/OpenTower) | Reverse-engineered reimplementation / port of Pizza Tower (OpenTower) | 89 | 🟢 | Game Maker Language |
| [glfrontier](https://github.com/pcercuei/glfrontier) | Reverse engineered version of Frontier: Elite II | 88 | 🔴 | C |
| [OpenRaider](https://github.com/xythobuz/OpenRaider) | Open Source Tomb Raider Engine | 86 | 🟡 | C++ |
| [u4-decompiled](https://github.com/ergonomy-joe/u4-decompiled) | Decompiled source code for the PC version of Ultima IV - Quest Of The Avatar | 82 | 🔴 | C |
| [Worldstone](https://github.com/Lectem/Worldstone) | Diablo 2 tools and engine reimplementation in C++ | 82 | 🔴 | C++ |
| [f2bgl](https://github.com/cyxx/f2bgl) | Fade To Black engine reimplementation (SDL, OpenGL) | 81 | 🗄️ | C++ |
| [MeitouClient](https://github.com/VlcekM/MeitouClient) | Open-source reimplementation of the Kenshi engine in C#/.NET (needs your own Kenshi) | 81 | 🟢 | C# |
| [NFS Recompiled](https://github.com/motor-dev/nfs-recompiled) | Engine reimplementation of Need For Speed II, Need For Speed III: Hot Pursuit; uses original game data (C++) | 81 | 🟢 | C++ |
| [OpenDriverEngine](https://github.com/OpenDriver2/OpenDriverEngine) | Research engine running Driver 1 and Driver 2 (PS1) on one codebase | 81 | 🟡 | C++ |
| [xoreos-tools](https://github.com/xoreos/xoreos-tools) | Tools for BioWare Aurora engine game formats, companion to the xoreos reimplementation | 81 | 🟢 | C++ |
| [openbgi](https://github.com/Cytlan/openbgi) | Open source reimplementation of the Ethornell Buriko General Interpreter | 80 | 🟢 | C |
| [Ultima 5 Redux](https://github.com/bradhannah/Ultima5Redux) | A mostly true to the original Ultima 5 remake in C# using the original U5 data files. | 80 | 🟢 |  |
| [WinWar](https://github.com/CAMongrel/WinWar) | WarCraft Orcs & Humans remake using the original assets | 80 | 🗄️ | C# |
| [tower-together](https://github.com/phulin/tower-together) | Clone of the 1993 game SimTower | 79 | 🟢 | TypeScript |
| [opendf (The Elder Scrolls II: Daggerfall)](https://github.com/kcat/opendf) | Open-source engine for The Elder Scrolls II: Daggerfall that uses the original data | 78 | 🟢 | C++ |
| [Xenogears (Noah, non-matching)](https://github.com/yaz0r/Noah) | Reverse-engineered reimplementation / port of Xenogears (Noah, non-matching) | 78 | 🟢 | C++ |
| [MegaManX6Recomp](https://github.com/mstan/MegaManX6Recomp) | Mega Man X6 (USA) recompiled for the Sony PlayStation using psxrecomp · Part of the R.A.I.D. community | 77 | 🟢 | Python |
| [OpenSR](https://github.com/ObKo/OpenSR) | Opensource multi-genre game based upon "Space Rangers 2: Dominators" | 77 | 🗄️ | C++ |
| [openstrike](https://github.com/AMDmi3/openstrike) | Libre reimplementation of Jungle and Desert Strike games | 76 | 🟡 | C++ |
| [Snipes](https://github.com/Davidebyzero/Snipes) | The classic 1982 text-mode game Snipes, ported from the original DOS executable with 100% identical game logic, with... | 76 | 🟡 | C++ |
| [TombaRecomp](https://github.com/mstan/TombaRecomp) | Tomba! (USA) recompiled for the Sony PlayStation using psxrecomp · Part of the R.A.I.D. community | 76 | 🟢 | Python |
| [FreeHeroes](https://github.com/mapron/FreeHeroes) | FreeHeroes is a free engine for Heroes of Might and Magic 3, similar to VCMI project. | 75 | 🟢 | C++ |
| [OpenMoonstone](https://github.com/joetsoi/OpenMoonstone) | Open source reimplementation of Moonstone: A Hard Day's Knight | 75 | 🔴 | Rust |
| [ppengine](https://github.com/jonathanopalise/ppengine) | 3D remake of Pole Position using game logic reverse engineered from the arcade ROMs | 75 | 🔴 | C |
| [Underworld Adventures](https://github.com/vividos/UnderworldAdventures) | Underworld Adventures is a project to recreate Ultima Underworld 1 on modern operating systems, using the original ga... | 75 | 🟢 | C++ |
| [dRally](https://github.com/urxp/dRally) | Open Source Engine / Death Rally [1996] | 74 | 🔴 | C |
| [OpenAOE](https://github.com/angered-ghandi/OpenAOE) | Open source reimplementation of Age of Empires (1997) | 74 | 🔴 | Rust |
| [LTJS](https://github.com/bibendovsky/ltjs) | LithTech Jupiter System | 73 | 🟢 | C++ |
| [SCSharp](https://github.com/toshok/scsharp) | Starcraft reimplementation in C# | 73 | 🔴 | C# |
| [xu4 (Ultima IV)](https://github.com/xu4-engine/u4) | xu4, a recreation of Ultima IV that uses the original game data | 73 | 🗄️ | C++ |
| [Wolfenshine](https://github.com/deanthecoder/Wolfenshine) | Modern C# reimplementation of Wolfenstein 3D | 72 | 🟢 | C# |
| [Mario Kart 64 for Dreamcast](https://github.com/jnmartin84/mk64-dc) | Sega Dreamcast port of Mario Kart 64 decompilation | 71 | 🟢 | C |
| [OpenFNaF](https://github.com/MotoLegacy/OpenFNaF) | Open source reimplementation of Five Nights at Freddy's | 71 | 🔴 | C |
| [VitalWear](https://github.com/cfogrady/VitalWear) | Wear OS engine recreation of the Bandai Vital Bracelet BE | 71 | 🟡 | Kotlin |
| [steins-gate](https://github.com/FGRE/steins-gate) | Reimplementation of Steins;Gate visual novel | 70 | 🔴 | C++ |
| [Another World JS](https://github.com/cyxx/another_js) | Another World/Out of This World (HTML5) | 69 | 🗄️ | JavaScript |
| [chronon](https://github.com/hogsy/chronon) | Open-source reimplementation of Anachronox | 69 | 🟡 | C++ |
| [OpenPigeon](https://github.com/OpenBubbles/OpenPigeon) | Open-source GamePigeon reimplementation | 69 | 🟢 | Kotlin |
| [Test-Drive-3-Maps](https://github.com/s-macke/Test-Drive-3-Maps) | Reverse-engineered and extracted the world maps of the 1990 DOS game Test Drive III | 69 | 🟢 | Assembly |
| [Loderunner](https://github.com/Piddewitt/Loderunner) | Reverse engineered C64 assembler source code to recreate a bit for bit identical version of the original game. | 68 | 🟡 | Assembly |
| [Game Creator](https://github.com/joshwyant/game-creator) | Open-source reimplementation of the GameMaker (classic) runner and editor | 67 | 🟡 | C# |
| [Cosmo-Engine](https://github.com/yuv422/cosmo-engine) | A new game engine to play the MS-DOS game "Cosmo's Cosmic Adventure" on modern systems | 66 | 🟢 | C |
| [Dangerous Dave 2: Modification Edition](https://github.com/Harchvertelol/Dangerous-Dave-2-Modification-Edition) | This is an open-source remake of a well-known platform game Dangerous Dave 2 with flexible and highly customizable co... | 66 | 🟢 | HTML |
| [OpenDance](https://github.com/WodsonKun/OpenDance) | Recreation of the Just Dance engine in GameMaker | 66 | 🟢 | Game Maker Language |
| [Another World Suite](https://github.com/malandrin/another-world-suite) | A Rust implementation of the "Another World" ("Out of This World" in the USA) game engine, compiled to WebAssembly to... | 65 | 🔴 | Rust |
| [DirkSimple](https://github.com/icculus/DirkSimple) | DirkSimple, a minimal player for the Dragon's Lair laserdisc game | 65 | 🟢 | Assembly |
| [libnpengine](https://github.com/FGRE/libnpengine) | Free implementation of Nitroplus/5pb. Visual Novel game engine | 65 | 🔴 | C++ |
| [Street Fighter III: 3rd Strike [3SXW]](https://github.com/guimaraf/3sxw) | Native port of Street Fighter III: 3rd Strike based on the 3sx decompilation (PS2) | 64 | 🟢 | C |
| [Total Annihilation 3D](https://github.com/zuzuf/TA3D) | Portable remake of Total Annihilation in 3D | 64 | 🔴 | C |
| [Open76](https://github.com/r1sc/Open76) | Interstate '76 engine reimplementation | 63 | 🔴 | C# |
| [Pocket Wormhole (FTL)](https://github.com/adamkulik/pocket-wormhole) | Native Android port of Project Wormhole, a reimplementation of the FTL engine | 63 | 🟢 | Kotlin |
| [ReChan](https://github.com/SilverwireGames/ReChan) | Jackie Chan Stuntmaster reimplementation | 63 | 🟢 | C++ |
| [shin](https://github.com/DCNick3/shin) | A reimplementation of VN engine primarily used by 07-th expansion releases on consoles (and some other entergram games) | 63 | 🟢 | Rust |
| [OpenGML](https://github.com/maiple/opengml) | Open-source interpreter for GameMaker Studio 1 GML games | 62 | 🔴 | C++ |
| [scion](https://github.com/nsgomez/scion) | Reimplementation of the Maxis engine used by The Sims 2 and SimCity 4 | 62 | 🟡 | C++ |
| [Nitro](https://github.com/billsonnn/nitro-react) | HTML5 Habbo Hotel client reimplementation in React | 61 | 🟢 | TypeScript |
| [Open Kick-Off](https://github.com/ssenegas/kickoff) | Open-source rewrite of the football game Kick Off 2 (Amiga) | 61 | 🟡 | Java |
| [OpenDrakan](https://github.com/Zalasus/opendrakan) | A work-in-progress recreation of Surreal Software's Riot Engine | 61 | 🟡 | C++ |
| [openPREY](https://github.com/themuffinator/openPREY) | Source port and game binary replacement to run PREY (2006) on modern systems | 61 | 🟢 | C++ |
| [Blues](https://github.com/cyxx/blues) | Blues Brothers, Jukebox Adventure & Prehistorik 2 engine reimplementation (PSP, SDL2) | 60 | 🗄️ | C |
| [FPC Atomic](https://github.com/PascalCorpsman/fpc_atomic) | Playable clone of the legendary Atomic Bomberman including Network and Ai https://en.wikipedia.org/wiki/Atomic_Bomberman | 60 | 🟢 | Pascal |
| [redstone-js](https://github.com/LostMyCode/redstone-js) | Play RED STONE ONLINE in the browser | 60 | 🟢 | JavaScript |
| [Cryogenic](https://github.com/OpenRakis/Cryogenic) | An open-source reimplementation of Cryo's DUNE game (WIP) | 59 | 🟢 | C# |
| [lilium-voyager](https://github.com/clover-moe/lilium-voyager) | An engine replacement for Star Trek Voyager: Elite Force Holomatch (multiplayer). | 59 | 🟢 | C |
| [OpenWar](https://github.com/andreas-jonsson/openwar) | Classic fantasy RTS game in the spirit of Warcraft: Orcs & Humans. | 59 | 🔴 | Go |
| [Colditz Escape](https://github.com/aperture-software/colditz-escape) | Amiga's "Escape From Colditz" ported to Windows, Linux, macOS and PSP | 58 | 🟡 | C |
| [LasMarionetas](https://github.com/OmniBlade/LasMarionetas) | Open-source reimplementation of The Sims | 58 | 🔴 | C++ |
| [Mikompilation](https://github.com/Mikompilation/Mikompilation) | Reimplementation project for the Fatal Frame 2 : Crimson Butterfly (Project Zero 2/零～紅い蝶) game engine | 58 | 🟡 | C |
| [REminiscence / REinforced](https://github.com/chermenin/REminiscence) | REminiscence is a re-implementation of the engine used in the game Flashback made by Delphine Software. | 58 | 🟢 | C++ |
| [rock-raiders-remake](https://github.com/rystills/rock-raiders-remake) | Partial HTML5 remake of the classic game "Lego Rock Raiders". | 58 | 🔴 | JavaScript |
| [u6-decompiled](https://github.com/ergonomy-joe/u6-decompiled) | Decompiled code for PC/MSDOS version of Ultima VI - The False Prophet | 58 | 🔴 | C |
| [freeage](https://github.com/puzzlepaint/freeage) | Open-source reimplementation of the Age of Empires 2: Definitive Edition engine | 57 | 🗄️ |  |
| [MegaManX5Recomp](https://github.com/mstan/MegaManX5Recomp) | Mega Man X5 (USA, SLUS-01334) statically recompiled to a native Windows executable with the PSXRecomp framework. | 57 | 🟢 | PowerShell |
| [Nitrosharp](https://github.com/CommitteeOfZero/nitrosharp) | Open-source N2System reimplementation | 57 | 🟢 | C# |
| [OpenCrashWOC](https://github.com/Open-Travelers/closeopenCWOC) | Reverse engineered reimplementation of Crash Bandicoot: The Wrath of Cortex | 57 | 🟢 | C |
| [WolfensteinRPG-RE](https://github.com/Erick194/WolfensteinRPG-RE) | Wolfenstein RPG reverse engineering and reimplementation | 57 | 🟡 | C++ |
| [OpenBattlefield2](https://github.com/Moxnatiy/OpenBattlefield2) | Clean-room reimplementation of DICE's Refractor 2 engine (Battlefield 2) | 56 | 🟢 | C++ |
| [RSDKv2 Decompilation](https://github.com/RSDKModding/RSDKv2-Decompilation) | a Decompilation of the 2008 Retro-Sonic Engine Demo of Sonic Nexus | 56 | 🟢 | C++ |
| [sioux](https://github.com/hanatos/sioux) | Open-source reimplementation of the Comanche 3 helicopter sim engine | 56 | 🟡 | C |
| [TOD_tools](https://github.com/Michael0ne/TOD_tools) | Reversed engine and tools of Total Overdose (2005, PC) | 56 | 🟡 | C++ |
| [BOOM: Remake](https://github.com/silverweed/lifish) | Open-source engine reimplementation of BOOM that runs on the original game data | 55 | 🟢 | C++ |
| [Prince-Monogame](https://github.com/salvadorc17/Prince-Monogame) | Monogame implementation of Prince of Persia 2. | 55 | 🟢 | C# |
| [SF2DISASM](https://github.com/ShiningForceCentral/SF2DISASM) | A disassembly of the game "Shining Force II" for documentation and fan-project purposes. | 55 | 🟢 | Assembly |
| [Stardust rebuilt](https://github.com/TheJare/stardust-48k) | Reverse engineered source for the 1987 Sinclair Spectrum game "Stardust" | 55 | 🔴 | Assembly |
| [MDK Sdl](https://github.com/nautilusbits/mdk-sdl) | Port of MDK (Shiny Entertainment, 1997) to C# and SDL3, based on reverse engineering (PC) | 54 | 🟢 | C# |
| [open-rct3](https://github.com/open-rct3/open-rct3) | Open-source re-implementation of RollerCoaster Tycoon 3 | 54 | 🟢 | C# |
| [Airline Tycoon](https://github.com/openairlinetycoon/AirlineTycoon) | Source code of Airline Tycoon based on the GOG source code release | 53 | 🔴 | C++ |
| [engge2](https://github.com/scemino/engge2) | Open source remake of Thimbleweed Park's engine | 53 | 🟡 | Nim |
| [libRealSpace](https://github.com/remileonard/libRealSpace) | Tools to parse and render Origin Systems RealSpace engine assets. | 53 | 🟢 | C++ |
| [ReksioEngine](https://github.com/ReksioEngine/ReksioEngine) | Reimplementation of the BlooMoo and Piklib engines for the Reksio PC games | 53 | 🟢 | TypeScript |
| [wacki](https://github.com/mszula/wacki) | From-scratch C/SDL2 reimplementation of Wacki (1998) from reverse-engineered opcodes | 53 | 🟢 | C |
| [femto8](https://github.com/benbaker76/femto8) | Open-source reimplementation of the PICO-8 fantasy console for embedded systems | 52 | 🟢 | C |
| [open-reckless-drivin](https://github.com/natecraddock/open-reckless-drivin) | Open-source reimplementation of the Macintosh shareware game Reckless Drivin' | 52 | 🟡 | Zig |
| [OpenRayman](https://github.com/imaginaryPineapple/OpenRayman) | Open-source reimplementation of the Rayman 2 engine | 52 | 🔴 | C |
| [SimUnity2](https://github.com/LazyDuchess/SimUnity2) | Attempt at a reimplementation of The Sims 2 Ultimate Collection in the Unity Engine... | 52 | 🗄️ | C# |
| [BtBuilder](https://github.com/dulsi/btbuilder) | An open source implementation of the Bard's Tale Construction Set. | 51 | 🟢 | C |
| [de Blob (OpenToshi)](https://github.com/AdventureT/OpenToshi) | Reverse-engineered reimplementation / port of de Blob (OpenToshi) | 51 | 🟢 | C++ |
| [OpenNitemare3D](https://github.com/BBQGiraffe/OpenNitemare3D) | reimplementation of the 1994 FPS Nitemare 3D | 51 | 🔴 | C# |
| [serflings (The Settlers)](https://github.com/nicymike/serflings) | Remake of The Settlers (Serf City) that uses the original data | 51 | 🟢 |  |
| [caesarpad (Caesar III)](https://github.com/chrissotraidis/caesarpad) | Caesar III on iPad, built on the Augustus engine reimplementation | 50 | 🟢 | Swift |
| [DesktopAdventures](https://github.com/shinyquagsire23/DesktopAdventures) | A recreation of the Desktop Adventures engine in C | 50 | 🔴 | C |
| [Mechanized Assault & eXploration Reloaded](https://github.com/maxr-dot-org/maxr) | A turn based strategy game | 50 | 🟢 | C++ |
| [Pentagram (Ultima VIII)](https://github.com/pentagram-u8/pentagram) | Reimplementation of the Ultima VIII: Pagan engine | 50 | 🟡 | C++ |
| [RuZZT](https://github.com/yokljo/ruzzt) | RuZZT, a ZZT game engine reimplementation in Rust | 50 | 🔴 | Rust |
| [CorrinoEngine](https://github.com/cookgreen/CorrinoEngine) | CorrinoEngine is an open-source RTS engine inspired by Emperor: Battle for Dune, with Emperor: Battle for Dune compat... | 49 | 🟢 | C# |
| [OpenSHC](https://github.com/sourcehold/OpenSHC) | An open source re-implementation of Stronghold Crusader | 49 | 🟢 | C++ |
| [ZGloom](https://github.com/Swizpig/ZGloom) | ZGloom, a reimplementation of the Amiga FPS Gloom that uses the original data | 49 | 🔴 | C++ |
| [jsFO](https://github.com/ajxs/jsFO) | Fallout 2 Javascript port | 48 | 🟢 | JavaScript |
| [OpenAdhoc](https://github.com/Nenkai/OpenAdhoc) | Open-source re-implementation of Gran Turismo Adhoc scripts | 48 | 🟢 | C |
| [OpenLGR](https://github.com/james-knippes/openlgr) | Engine reimplementation of Lego Racers; uses original game data (C) | 48 | 🗄️ | C |
| [TurokEX](https://github.com/svkaiser/TurokEX) | TurokEX, a rewrite of the Turok: Dinosaur Hunter engine that uses the original data | 48 | 🔴 | C |
| [Benilla-Wotlk (World of Warcraft 3.3.5)](https://github.com/Onixaz/benilla-wotlk) | World of Warcraft 3.3.5 client written from scratch | 47 | 🟢 | Rust |
| [DOOM64-EX-Plus-Enhanced](https://github.com/Styd051/DOOM64-EX-Plus-Enhanced) | Enhanced build of the DOOM64 EX+ reverse-engineered Doom 64 engine (N64) | 46 | 🟢 | C |
| [GT3-revisited](https://github.com/matt-pulsipher/GT3-revisited) | Gran Turismo 3 A-Spec engine reimplementation for modern platforms (PS2) | 46 | 🟢 | C++ |
| [sacengine](https://github.com/tg-2/sacengine) | Engine reimplementation for Sacrifice by Shiny Entertainment | 46 | 🟢 | D |
| [Blast Corps](https://github.com/retroplastic/blastcorps) | A Blast Corps decompilation. | 45 | 🔴 | C |
| [GLKeeper](https://github.com/codenamecpp/GLKeeper) | Open Source Dungeon Keeper 2 Reimplementation | 45 | 🟢 | C++ |
| [Lemmix](https://github.com/ericlangedijk/Lemmix) | Lemmix Main Source Code - Lemmings Clone | 45 | 🔴 | Pascal |
| [abyssal](https://github.com/TheWWWorm/abyssal) | Godot engine edition of Deep 3D: Submarine Odyssey by Fishlabs | 44 | 🟢 | GDScript |
| [OpenGTA](https://github.com/madebr/OpenGTA) | OpenGTA: copy of http://ogta.fifengine.de/ | 44 | 🔴 | C++ |
| [RAD](https://github.com/jval1972/Rad-X) | RAD: Remake of the game "Radix - Beyond the void" | 44 | 🟡 | Pascal |
| [reevengi](https://github.com/pmandin/reevengi) | Resident Evil engine reimplementation | 44 | 🔴 | C |
| [ectopad (Metroid Prime)](https://github.com/chrissotraidis/ectopad) | Metroid Prime via the Metaforce reimplementation for macOS, iOS and iPadOS | 43 | 🟢 | C++ |
| [Jurassic Park: Operation Genesis (OpenJPOG)](https://github.com/AdventureT/OpenJPOG) | Reverse-engineered reimplementation / port of Jurassic Park: Operation Genesis (OpenJPOG) | 42 | 🟢 | C++ |
| [peonpad (Warcraft II)](https://github.com/chrissotraidis/peonpad) | Warcraft II on iPad via the Stratagus engine | 42 | 🟢 | C++ |
| [Chrono Trigger C](https://github.com/buzzer-re/Chrono-Trigger-C) | A simple remake of Chrono Trigger written in C, using the SDL API | 41 | 🗄️ | C |
| [F-Zero X (USA)](https://github.com/BttrDrgn/f-zerox) | F-Zero X Decompilation | 41 | 🔴 | C |
| [OpenSith](https://github.com/r1sc/OpenSith) | Jedi Knight: Dark Forces II engine reimplementation | 41 | 🟡 | C# |
| [pfr](https://github.com/wanda-phi/pfr) | Pinball Fantasies (1992) reverse engineered and re-created | 41 | 🟡 | Rust |
| [Phoenix](https://github.com/joulupunikki/Phoenix) | Java clone/remake/patch of the game Emperor of the Fading Suns | 41 | 🔴 | Java |
| [Clone Dash](https://github.com/marchc1/CloneDash) | Open-source engine reimplementation of Muse Dash (Windows) that runs on the original game data | 40 | 🟢 | C# |
| [FelineSystem2](https://github.com/kokseen1/FelineSystem2) | Open-source remake of the CatSystem2 visual novel engine | 40 | 🔴 | C++ |
| [JLud2D](https://github.com/rafael-esper/JLud2D) | 2D old-school Engine for Games | 40 | 🟢 | TypeScript |
| [ChronoStorm](https://github.com/cookgreen/ChronoStorm) | Open-source engine reimplementation of Command & Conquer: Red Alert 2 and Yuri's Revenge | 39 | 🟢 | Python |
| [openSMB2](https://github.com/Matriks404/openSMB2) | Open-source reimplementation of Super Mario Bros. 2 in Lua and LOVE | 39 | 🗄️ | Lua |
| [Project Carrot](https://github.com/soulweaver91/project-carrot) | Project Carrot, an open-source reimplementation of Jazz Jackrabbit 2 that uses the original data | 39 | 🔴 | C++ |
| [Quest 64 Decompilation](https://github.com/Mallos31/Quest) | decompilation of Quest64 | 39 | 🟡 | C |
| [Settlers.ts](https://github.com/tomsoftware/Settlers.ts) | Web remake of The Settlers IV in TypeScript | 39 | 🟡 | TypeScript |
| [smb1-disasm](https://github.com/laura240406/smb1-disasm) | A collection to build SMB1 from the disassembly | 39 | 🔴 | Assembly |
| [Super Mario Bros. 3Mix](https://github.com/captainsouthbird/3Mix) | Super Mario Bros 3Mix hack | 39 | 🔴 | Assembly |
| [earthbound](https://github.com/Herringway/earthbound) | attempt at decompiling+porting earthbound | 38 | 🟡 | D |
| [freevgui](https://github.com/FWGS/freevgui) | Free and open-source reimplementation of the Half-Life VGUI library | 38 | 🟢 | C++ |
| [openzt](https://github.com/openzt1/openzt) | WIP Reimplimentation of Zoo Tycoon (2001) | 38 | 🟢 | Rust |
| [ChaseHQ](https://github.com/dpt/ChaseHQ) | Chase H.Q. for ZX Spectrum — reverse-engineered and reconstructed in portable C | 37 | 🟢 | C |
| [OMF-2097-Remastered](https://github.com/Jared-woodruff/OMF-2097-Remastered) | One Must Fall 2097 rebuilt in TypeScript and WebGL2, using the original game data | 37 | 🟢 | TypeScript |
| [OpenDeathValley (Desperados: Wanted Dead or Alive)](https://github.com/OpenDeathValley/OpenDeathValley) | Open-source engine for Desperados: Wanted Dead or Alive that uses the original data | 37 | 🔴 | C |
| [OpenRakis](https://github.com/OpenRakis/OpenRakis) | Tools for an open-source reimplementation of Cryo's Dune (1992) | 37 | 🟢 | Assembly |
| [OpenXeen](https://github.com/busyDuckman/OpenXeen) | Might and Magic engine rewrite. | 37 | 🔴 | Java |
| [JJFFE](https://github.com/videogamepreservation/jjffe) | John Jordan's reverse engineering of Frontier: First Encounters. | 35 | 🗄️ | Assembly |
| [Pokémon Anniversary Red](https://github.com/TwitchPlaysPokemon/pokemonAnniversaryRed) | Anniversary Red dissassembly | 35 | 🔴 | Assembly |
| [reb3](https://github.com/lolz0r/reb3) | Partial reverse-engineered rebuild of Burnout 3: Takedown | 35 | 🟢 | C |
| [sadx_decomp](https://github.com/FraGag/sadx_decomp) | Sonic Adventure DX Decompilation | 35 | 🗄️ | C |
| [xrick (Rick Dangerous)](https://github.com/zpqrtbnk/xrick) | xrick, an open-source reimplementation of Rick Dangerous | 35 | 🟢 | C |
| [GLSpeed (Speed Haste)](https://github.com/jval1972/Speed) | Open-source reimplementation of Speed Haste (DOS) | 34 | 🔴 | Pascal |
| [rsc-remastered](https://github.com/Danjb1/rsc-remastered) | Reverse-engineered implementation of the RuneScape Classic client | 34 | 🔴 | Java |
| [burntime](https://github.com/jakobharder/burntime) | Remaster and expansion of Max Design's Burntime (1993) that uses the original data | 33 | 🟢 | C# |
| [Contra_remake](https://github.com/EmileSonneveld/Contra_remake) | The first level of a cool arcade game remade in c++ | 33 | 🔴 | JavaScript |
| [F.LF](https://github.com/tyt2y3/F.LF) | Clean-room implementation of the fighting game Little Fighter 2 | 33 | 🔴 | HTML |
| [OpenTitus](https://github.com/stople/OpenTitus) | A port of the game engine behind the DOS versions of Titus the Fox and Moktar | 33 | 🔴 |  |
| [PyTouhou](https://github.com/GovanifY/PyTouhou) | Open-source reimplementation of the Touhou Generation 1 Windows engine | 33 | 🔴 | Python |
| [Mario-Bros.-Dis](https://github.com/RussianManSMWC/Mario-Bros.-Dis) | Mario Bros. (NES) Disassembly | 32 | 🟢 | Assembly |
| [Re-Comprehend](https://github.com/RyanMallon/recomprehend) | Open source implementation of the Comprehend adventure game engine used by the games Transylvania, Crimson Crown, and... | 32 | 🔴 | C |
| [Rosebed](https://github.com/mdmrk/rosebed) | From-scratch Zig reimplementation of Minecraft Beta 1.7.3 client and server, protocol-compatible | 32 | 🟢 | Zig |
| [Sonic R (sonic-r (jnmartin84))](https://github.com/jnmartin84/sonic-r) | Reimplementation of Sonic R for multiple platforms (Saturn) | 32 | 🟢 | C |
| [The Castles of Dr. Creep](https://github.com/segrax/DrCreep) | The Castles of Dr. Creep | 32 | 🔴 | C++ |
| [Unity Underground](https://github.com/Kweepa/OpenUnderground) | Unity-based update of Ultima Underworld that uses the original game data (DOS) | 32 | 🟢 | C# |
| [BeefRaiderXR (Tomb Raider)](https://github.com/Team-Beef-Studios/BeefRaiderXR) | OpenXR build of OpenLara, the Tomb Raider engine reimplementation | 31 | 🟡 | C |
| [Doom 64 for Dreamcast](https://github.com/jnmartin84/doom64-dc) | Doom 64 port for Sega Dreamcast / KallistiOS | 31 | 🟢 | C |
| [Dungeon Craft](https://github.com/grannypron/uaf) | Engine reimplementation of Forgotten Realms: Unlimited Adventures; uses original game data (C++) | 31 | 🟢 | C++ |
| [Lode Runner 2020](https://github.com/Ma-Pe-Ma/Lode-Runner-2020) | A remake of the classic '80s puzzle game! | 31 | 🟢 | C++ |
| [REminiscence](https://github.com/cyxx/REminiscence) | Flashback engine reimplementation (Android, SDL) | 31 | 🗄️ | C++ |
| [Shining Force 2 Reverse Engineer (SF2RE)](https://github.com/ShiningForceCentral/SF2RE) | Collaborative work on reverse-engineering Shining Force II, and source of main project SF2DISASM (see website link) | 31 | 🟡 | C |
| [SiegeFX](https://github.com/codingncaffeine/SiegeFX) | Open-source reimplementation of Dungeon Siege (2002) in C# | 31 | 🟢 | C# |
| [OpenMM2](https://github.com/0x1F9F1/OpenMM2) | Open-source re-implementation of Midtown Madness 2 | 30 | 🗄️ | C |
| [OpenOrion2](https://github.com/nextghost/openorion2) | Open-source remake of Master of Orion II: Battle at Antares | 30 | 🟢 | C++ |
| [xbox-boot-re](https://github.com/bennyborn/xbox-boot-re) | Original Xbox boot animation reconstructed from the retail BIOS in C with a WebGPU viewer | 30 | 🟢 | Python |
| [coney](https://github.com/Ryubara/coney) | AI-driven reimplementation of The Warriors (PS2) | 29 | 🟢 | C++ |
| [Future Cop: MIT](https://github.com/Ghoster738/Future-Cop-MIT) | Open Source Game Engine Project | 29 | 🟢 | C++ |
| [OpenSolomonsKey (Solomon's Key)](https://github.com/mdodis/OpenSolomonsKey) | Open-source reimplementation of Solomon's Key (Arcade) | 29 | 🔴 | C++ |
| [beatfever](https://github.com/Sulunia/beatfever) | Partial open-source reimplementation of the osu! game engine in Lua/LOVE | 28 | 🔴 | Lua |
| [Bermuda Syndrome](https://github.com/cyxx/bermuda) | Bermuda Syndrome engine reimplementation (Emscripten, libretro, SDL2) | 28 | 🗄️ | C++ |
| [Heroes Of JinYong](https://github.com/soarqin/HeroesOfJinYong) | A reimplementation of the DOS game `The legend of Jin Yong Heroes(金庸群侠传)` | 28 | 🟢 | C++ |
| [Magnetar](https://github.com/joankaradimov/Magnetar) | Magnetar is a StarCraft: Brood War mod/reimplementation. | 28 | 🟡 | C++ |
| [mengde](https://github.com/wateret/mengde) | A turn-based RPG game engine inspired by 三國志曹操傳. | 28 | 🔴 | C++ |
| [mortar-eng (TT Games)](https://github.com/leftmostcat/mortar-eng) | Reimplementation of the TT Games LEGO game engine | 28 | 🔴 | C++ |
| [Sheep, Dog 'n' Wolf](https://github.com/SDW-Community/Sheep-Dog-n-Wolf-Rewooled) | PC port of Sheep, Dog 'n' Wolf that replaces its Windows dependencies (PC) | 28 | 🟢 | C++ |
| [WoodyRE](https://github.com/jjmhalew/WoodyRE) | Engine reimplementation of Woody Woodpecker: Escape from Buzz Buzzard Park (PC, 2001) - plays the original game from... | 28 | 🟢 | C |
| [freetfc](https://github.com/eukara/freetfc) | Clean-room reimplementation of Team Fortress Classic in QuakeC | 27 | 🟡 | C |
| [kys-js](https://github.com/kt2/kys-js) | 《金庸群侠传》kys-js (pixijs) | 27 | 🔴 | JavaScript |
| [linyaga](https://github.com/cyxx/linyaga) | Humongous Yaga engine reimplementation | 27 | 🗄️ | C |
| [OpenCloud](https://github.com/Gundorada-Workshop/OpenCloud) | Open source reimplementation of the Dark Cloud games | 27 | 🟡 | C++ |
| [opengta2](https://github.com/ikkentim/opengta2) | Open-source re-implementation of GTA II in C# using the original assets | 27 | 🟢 | C# |
| [Thirdeye](https://github.com/psi29a/thirdeye) | Reimplementation of AESOP that runs Eye of the Beholder 3 and Dungeon Hack. | 27 | 🟢 | C++ |
| [UltimaVRedux](https://github.com/bradhannah/UltimaVRedux) | Ultima V Redux, a modern recreation that requires the original game data | 27 | 🟢 | Go |
| [WinTex](https://github.com/ElakaSnarne/WinTex) | Engine reimplementation of Under a Killing Moon; uses original game data (C++) | 27 | 🟢 | C++ |
| [piney_apples](https://github.com/Toyz/piney_apples) | Native Rust port of the PS2 .hack engine from reverse engineering | 26 | 🟢 | Rust |
| [skyroads-port](https://github.com/ammaarreshi/skyroads-port) | 1:1 reverse-engineered portable port of SkyRoads (1993) in C11 + SDL2 | 26 | 🟢 | C |
| [Test Drive III Enhanced](https://github.com/kylofon/testdrive3-enhanced) | Enhanced native SDL3 port of Test Drive III: The Passion (DOS) | 26 | 🟢 | C |
| [Ultima 5](https://github.com/synthwave-pixel/ultima5) | Modern engine for Ultima 5. | 26 | 🟢 | TypeScript |
| [vigasocosdl-la-abadia-del-crimen](https://github.com/luzbel/vigasocosdl-la-abadia-del-crimen) | Automatically exported from code.google.com/p/vigasocosdl-la-abadia-del-crimen | 26 | 🔴 | Assembly |
| [COD4-Rewrite](https://github.com/Nilbong/COD4-Rewrite) | Call of Duty 4 multiplayer reimplemented in Rust on Bevy. Bring your own game files. | 25 | 🟢 | Rust |
| [DungeonMaster.NET](https://github.com/ggrrin/DungeonMaster.NET) | Reimplementation of famous old Dungeon Master game. | 25 | 🔴 | C# |
| [freegunman](https://github.com/eukara/freegunman) | Clean-room reimplementation of Gunman Chronicles in QuakeC | 25 | 🟡 | C |
| [Iris2](https://github.com/kblaschke/Iris2) | An Open-Source 3D Ultima Online(tm) Client. No active development, mostly for archival purposes as the original proje... | 25 | 🔴 | C |
| [OpenRedAlert (Command & Conquer: Red Alert)](https://github.com/damiencarol/openredalert) | Open-source reimplementation of Command & Conquer: Red Alert | 25 | 🔴 | C++ |
| [Railroad Tycoon](https://github.com/bluddy/rails) | Remake of Railroad Tycoon in OCaml (DOS) | 25 | 🟢 | OCaml |
| [goldsrc-reversed-steam_api](https://github.com/oxiKKK/goldsrc-reversed-steam_api) | Reverse-engineered steam_api module shipped with the GoldSource engine | 24 | 🔴 | C++ |
| [Harold](https://github.com/OldGamesLab/Harold) | Open-source Fallout 2 engine implementation, a revival of darkfo project | 24 | 🔴 | TypeScript |
| [Legend of Legaia](https://github.com/AndrewAltimit/legend-of-legaia-re) | Reverse engineering and format documentation of Legend of Legaia (PS1) | 24 | 🟢 | Rust |
| [Roton (Super ZZT)](https://github.com/SaxxonPike/roton) | Roton, cross-platform ZZT and Super ZZT engine reimplementation in C# | 24 | 🟢 | C# |
| [shiloh](https://github.com/Asterber/shiloh) | Engine that runs The X-Files Game (1998) on modern PCs and in the browser | 24 | 🟢 | Rust |
| [The Wing of Madoola](https://github.com/nfroggy/openmadoola) | Reimplementation of The Wing of Madoola (NES) in C | 24 | 🟢 | C |
| [zztjs](https://github.com/bstreiff/zztjs) | ZZT game engine reimplemented in JavaScript | 24 | 🗄️ | JavaScript |
| [Bagman (bagman (arcade -> 68k transcode))](https://github.com/jotd666/bagman) | Bagman arcade code transcoded for Windows, Nintendo DS and Amiga (Arcade) | 23 | 🟢 | C |
| [Bedlam 2: Absolute Bedlam](https://github.com/8street/Bedlam2) | Source code for Bedlam 2 (1997) game executable file. | 23 | 🔴 | Assembly |
| [BelthasarProject](https://github.com/TemplarServant/BelthasarProject) | Chrono Trigger (SNES) reimplemented as a native PC game in C, using your own ROM | 23 | 🟢 | C |
| [F-Zero Clone](https://github.com/chipbell4/F-Zero-Clone) | A WebGL F-Zero clone. Show ya moves! | 23 | 🔴 | JavaScript |
| [Gran Turismo 4](https://github.com/MrGoodGuy2144/OpenGT4) | Unofficial native PC port of Gran Turismo 4, reimplemented in C (PS2) | 23 | 🟢 | C |
| [OpenFMV](https://github.com/Rinnegatamante/OpenFMV) | Open-source FMV game engine compatible with Wales Interactive games | 23 | 🟡 | C |
| [OpenMM1](https://github.com/0x1F9F1/OpenMM1) | Open-source re-implementation of Midtown Madness 1 | 23 | 🗄️ | C++ |
| [OpenNox](https://github.com/noxworld-dev/opennox) | Open-source reimplementation of Nox | 23 | 🗄️ | C |
| [SF1DISASM](https://github.com/ShiningForceCentral/SF1DISASM) | A disassembly of the game "Shining Force" for documentation and fan-project purposes. | 23 | 🟢 | Assembly |
| [cc94](https://github.com/institution/cc94) | Remake of 1994 Sid Meier's Colonization game | 22 | 🔴 | C++ |
| [DuckHunt](https://github.com/grosbouddha/duckhunt) | Canvas based remake of the NES DuckHunt game. | 22 | 🔴 | JavaScript |
| [Igor](https://github.com/cyxx/igor) | Igor: Objetivo Uikokahonia game interpreter (Android, SDL) | 22 | 🗄️ | C++ |
| [mc-classic-c](https://github.com/degradka/mc-classic-c) | Minecraft Classic rewritten in C | 22 | 🟢 | C |
| [shock2quest](https://github.com/tommy-xr/shock2quest) | Unofficial recreation of the Dark engine for System Shock 2 on Quest | 22 | 🟢 | Rust |
| [vaultpad (Fallout 2)](https://github.com/chrissotraidis/vaultpad) | Touch-enabled Fallout 2 for iPad based on the Fallout 2 reimplementation | 22 | 🟢 | Swift |
| [wkbre2](https://github.com/AdrienTD/wkbre2) | WK Engine Reimplementation Rewrite with Multiplayer support! | 22 | 🟢 | C++ |
| [captain-bible-re](https://github.com/peterkelly/captain-bible-re) | Reverse engineering of the 1994 DOS game Captain Bible in the Dome of Darkness | 21 | 🟢 | Rust |
| [Looking Glass](https://github.com/looking-glass-project/LookingGlass) | Open-source reimplementation of American McGee's Alice (Windows) | 21 | 🟢 | Rust |
| [LOZ](https://github.com/aldonunez/Loz) | A remake of The Legend of Zelda | 21 | 🔴 | C++ |
| [OpenChasm](https://github.com/alexey-lysiuk/OpenChasm) | Free software reconstruction of Chasm: The Rift (DOS) | 21 | 🗄️ | C++ |
| [Q2RTXPerimental](https://github.com/PolyhedronStudio/Q2RTXPerimental) | My 'Experimental' fork of NVIDIA’s implementation of RTX ray-tracing in Quake II | 21 | 🟢 | C++ |
| [REminiscence](https://github.com/libretro/REminiscence) | Flashback engine reimplementation | 21 | 🟢 | C++ |
| [T.O.R.E Fighters](https://github.com/john-overton/T.O.R.E-Fighters) | Reverse-engineered rebuild of Jane's Fighters Anthology flight sim | 21 | 🟢 | Rust |
| [7k2](https://github.com/7k2/7k2) | Experimental fork of Seven Kingdoms II: The Fryhtan Wars | 20 | 🔴 | C++ |
| [Chocolate Blood](https://github.com/NBlood/chocolate-blood) | Chocolate Doom inspired Blood port (heavily WIP) | 20 | 🟡 | C |
| [CSVM (Crimson Skies)](https://github.com/Laeresh/CSVM) | Open-source remake of Crimson Skies (2000) that plays the original game files | 20 | 🟢 | C# |
| [Daikatana Restoration Project](https://github.com/atsb/daikatana-restoration-project) | Daikatana restoration aiming to have a clean 1.2 source and to support modern systems | 20 | 🟢 | C++ |
| [OpenBreed](https://github.com/mrpetro/OpenBreed) | Open source reimplementation of classic Alien Breed 2D games and editor. | 20 | 🟢 | C# |
| [RPG-X](https://github.com/UberGames/rpgxEF) | A modifaction of ioEF with increased limits for RPG-X2, now including the gamecode | 20 | 🟢 | C |
| [Sonic Lost World (OpenLW)](https://github.com/Radfordhound/OpenLW) | Reverse-engineered reimplementation / port of Sonic Lost World (OpenLW) | 20 | 🟡 | C++ |
| [wkbre](https://github.com/AdrienTD/wkbre) | Warrior Kings (Battles) game engine reimplementation / recreation | 20 | 🟡 | C++ |
| [Amiga Cannonball-C](https://github.com/lantus/Cannonball-C) | Cannonball for the Amiga ported to C | 19 | 🔴 | C |
| [Concilia Tower](https://github.com/Jonahss/concilia-tower) | Ground-up rewrite of SimTower (1994) from decompilation, playable in the browser | 19 | 🟢 | C |
| [Flipendo](https://github.com/kroplabeskidu/flipendo) | Open-source engine for Harry Potter and the Philosopher's Stone (PC) | 19 | 🟢 | C++ |
| [hobbitgfx](https://github.com/richcarl/hobbitgfx) | The Hobbit graphics engine | 19 | 🔴 | JavaScript |
| [jy-remake](https://github.com/scarsty/jy-remake) | Zgames制作的《金庸群侠传》复刻版 | 19 | 🟢 | C |
| [Realms of Arkania: Blade of Destiny ( Bright-Eyes)](https://github.com/Henne/BrightEyes) | Engine rewrite of Realms of Arkania: Blade of Destiny (DOS) | 19 | 🟢 | C++ |
| [zorkClone](https://github.com/vatbub/zorkClone) | Reimplementation of the original Zork game developed by Infocom. | 19 | 🔴 | Java |
| [I26 (Interstate '76)](https://github.com/vahokif/I26) | Godot engine reimplementation of Interstate '76 | 18 | 🟢 |  |
| [libd2](https://github.com/jaenster/libd2) | Zig libraries reconstructing Diablo II 1.14d maps, item generation, saves and simulation | 18 | 🟢 | Zig |
| [relith (LithTech)](https://github.com/alex-nax/relith) | Reimplementation of the LithTech 2.x engine | 18 | 🟢 |  |
| [Underworld Revisited](https://github.com/PQMarine/UnderworldRevisited) | Open-source reimplementation of Ultima Underworld: The Stygian Abyss (DOS) | 18 | 🟢 | C# |
| [DownHill-Port-PC](https://github.com/Pedroj-64/DownHill-Port-PC) | Native PC port of Downhill Domination (PS2) via an engine reimplementation using game data | 17 | 🟢 | C++ |
| [GTA4Unity](https://github.com/Infinity-Loops/GTA4Unity) | Open-source reimplementation of the GTA IV engine in Unity | 17 | 🟢 | C# |
| [invaders (in C)](https://github.com/herrecito/invaders) | A Space Invaders / Intel 8080 emulator | 17 | 🔴 | C |
| [Octopus](https://github.com/roger-wetzel/Octopus) | Remake of Nintendo's Octopus Game & Watch device for Apple TV 4 | 17 | 🔴 | Swift |
| [OpenDW (Dragon Wars)](https://github.com/devinsmith/opendw) | Open-source reimplementation of the Dragon Wars (1989) engine that uses the original data | 17 | 🟢 | C |
| [Pokémon Red++](https://github.com/jayceekaycee/RedPlusPlus) | An upgrade to Pokémon Red. Fixes several bugs and adds a lot of new features. Now a standalone repository, so you can... | 17 | 🔴 | Assembly |
| [realice](https://github.com/FWGS/realice) | Heavy Metal F.A.K.K. 2 / American McGee's Alice reverse engineered. | 17 | 🟢 | C |
| [sims-3-bevy](https://github.com/Eamo5/sims-3-bevy) | Work-in-progress reimplementation of The Sims 3 in the Bevy game engine | 17 | 🟢 | Rust |
| [The Legend of Zelda: Oracle of Ages (ooa-godot)](https://github.com/SHOEGAZEssb/ooa-godot) | Reimplementation of Zelda: Oracle of Ages/Seasons in C# and Godot (Game Boy Color) | 17 | 🟢 | C# |
| [Urban Chaos (OpenChaos)](https://github.com/UltimaBeaR/OpenChaos) | Fan modernization of Urban Chaos built on its code (PC) | 17 | 🟢 | C++ |
| [Aces of the Pacific Enhanced](https://github.com/kylofon/acesofthepacific-enhanced) | Enhanced native SDL3 port of Aces of the Pacific (DOS) | 16 | 🟢 | C |
| [Arcanum on iOS](https://github.com/arcanum-project/game) | Engine reimplementation of Arcanum: Of Steamworks and Magick Obscura; uses original game data (C++) | 16 | 🔴 | C++ |
| [benilla-re](https://github.com/samwhosung/benilla-re) | Reverse engineering of the World of Warcraft 1.12.1 client behind the benilla client | 16 | 🟢 | Rust |
| [Castlekeep](https://github.com/leidav/Castlekeep) | Reimplementation of Stronghold 1 | 16 | 🔴 | C++ |
| [Command Series Engine](https://github.com/pwiecz/command_series) | Engine for playing Command Series games by Sid Meier/Microprose | 16 | 🟢 | Go |
| [Desktop Adventures Engine for ScummVM](https://github.com/digitall/scummvm-deskadv) | Desktop Adventures Engine for ScummVM | 16 | 🔴 | C++ |
| [hode (Heart of Darkness)](https://github.com/cyxx/hode) | Reimplementation of the Heart of Darkness engine that uses the original data | 16 | 🗄️ | C++ |
| [KlingonWin10WPF](https://github.com/Teravus/KlingonWin10WPF) | Reimplementation of the Star Trek: Klingon Immersion Studies FMV engine for Windows 10 | 16 | 🔴 | C# |
| [ktes2](https://github.com/sonicretro/ktes2) | Knucles the Echidna in Sonic 2 | 16 | 🔴 | Assembly |
| [Minecraft: Pocket Edition (mcpe-engine)](https://github.com/BrentDaMage/mcpe-engine) | Reverse-engineered reimplementation / port of Minecraft: Pocket Edition (mcpe-engine) | 16 | 🟢 | C++ |
| [OpenOP2](https://github.com/OpenOP2/OpenOP2) | OpenOP2 is a re-implementation of the gameplay inspired by colony building games like Outpost 2, using the OpenRA eng... | 16 | 🟢 | C# |
| [Project ANISE](https://github.com/tomyun/anise) | 🦋 Project ANISE (A Newly Implemented Scripting Engine for AI5V) | 16 | 🔴 | C++ |
| [sena-rs (SoftPAL)](https://github.com/xmoezzz/sena-rs) | Cross-platform reimplementation of the SoftPAL visual novel engine | 16 | 🟢 | Rust |
| [Friking Shark](https://github.com/ptitSeb/friking-shark) | Open-source reimplementation of Flying Shark | 15 | 🔴 | C |
| [OpenBound](https://github.com/WickedPeanuts/OpenBound) | This project aims to mimic the older PC versions of Gunbound with optimized behavior, engine and gameplay elements. T... | 15 | 🟡 | C# |
| [OpenRakis_old (Dune)](https://github.com/OpenRakis/OpenRakis_old) | Open-source reimplementation of Cryo's Dune (1992) | 15 | 🗄️ | Assembly |
| [openzt2](https://github.com/overyonder/openzt2) | Open-source engine reimplementation of Zoo Tycoon 2 | 15 | 🟢 | Rust |
| [re2ds](https://github.com/eray1605/re2ds) | Native Nintendo DS engine for Resident Evil 2 that reimplements its PS1 game rules | 15 | 🟢 | C |
| [SFCDDISASM](https://github.com/ShiningForceCentral/SFCDDISASM) | A disassembly of the game "Shining Force CD" for documentation and fan-project purposes. | 15 | 🔴 | Assembly |
| [Zuma Portable](https://github.com/kyle-sylvestre/CircleShootApp) | Zuma Deluxe (1.0.0) decompilation ported to newer platforms | 15 | 🟢 | C++ |
| [earth-shaker](https://github.com/Palevolg/earth-shaker) | Remake of an old ZX-spectrum game "EarthShaker" on Unity | 14 | 🔴 | C# |
| [FreeSynd (Syndicate)](https://github.com/videogamepreservation/freesynd) | Reimplementation of the engine for Bullfrog's Syndicate | 14 | 🔴 | C++ |
| [hi-octane202x (Hi-Octane)](https://github.com/woalexan/hi-octane202x) | Recreation of Hi-Octane (Bullfrog, 1995) that uses the original game data | 14 | 🟢 | C++ |
| [OpenKingdoms](https://github.com/OpenKingdoms/OpenKingdoms) | Open-source engine reimplementation of Total Annihilation: Kingdoms (C11, native + WebAssembly). Bring your own game... | 14 | 🟢 | C |
| [openrecet](https://github.com/Francesco149/openrecet) | Open drop-in exe replacement for Recettear with engine documentation | 14 | 🟢 | C |
| [OpenUT2k4](https://github.com/GloriousEggroll/OpenUT2k4) | Open-source reimplementation of Unreal Tournament 2004 in Unreal Engine 5 | 14 | 🟢 | C++ |
| [Tile World 2](https://github.com/SicklySilverMoon/tworld) | The current fork of Tile World 2, including Qt6 support, and other game patches | 14 | 🟢 | C |
| [unbanished](https://github.com/tanepiper/unbanished) | From-scratch Rust reimplementation of the Banished engine, native and in the browser | 14 | 🟢 | Rust |
| [Atari8bit_StarRaiders](https://github.com/sidneycadot/Atari8bit_StarRaiders) | A repository dedicated to reverse engineering the classic 1979 game Star Raiders for the Atari 400/800/XL/XE platform. | 13 | 🔴 | Assembly |
| [Cannon Fodder](https://github.com/krazyjakee/CannonFodder) | HTML5 Remake of an Amiga Classic | 13 | 🔴 | JavaScript |
| [coduomp](https://github.com/opencoduo/coduomp) | Reconstruction of Call of Duty: United Offensive multiplayer | 13 | 🟢 | C |
| [DejaVu-llvm](https://github.com/rpjohnst/dejavu-llvm) | Compiler and runtime for GameMaker Studio 1 games built on LLVM | 13 | 🔴 | C++ |
| [inFAMOUS reimplementation](https://github.com/bucketcomps/infamous) | Clean-room native PC reimplementation of inFAMOUS (2009, PS3) | 13 | 🟢 |  |
| [mhlib](https://github.com/Theaninova/mhlib) | A project to make the old classic Moorhuhn Games playable on modern systems via an engine reimplementation, written i... | 13 | 🔴 | Rust |
| [ReDMCSB](https://github.com/gondur/ReDMCSB_Release2) | ReDMCSB Release2 source code by Christophe Fontanel | 13 | 🔴 | Assembly |
| [reGML](https://github.com/TimGoTheCreator/reGML) | C++ reimplementation of the GameMaker (GML) runtime, tested with Undertale | 13 | 🟢 | C++ |
| [remc1](https://github.com/turican0/remc1) | Recode Binary code of game Magic Carpet1 to C/C++ language(remake MC1 for any platform) | 13 | 🔴 | C++ |
| [Arkanum](https://github.com/vleon1/Arkanum) | Arcanum game engine recreation | 12 | 🔴 | Python |
| [DNF-reimposition](https://github.com/vini1264/DNF-Enhanced) | Set of gameplay enhancements for Duke Nukem Forever (2011) | 12 | 🔴 | C |
| [EF2GameSource](https://github.com/UberGames/EF2GameSource) | The original EF2GameSource updated so it compiles under Visual Studio 2012 and Linux | 12 | 🔴 | C++ |
| [erampage](https://github.com/ttyborg/erampage) | Automatically exported from code.google.com/p/erampage | 12 | 🔴 | C |
| [Free-BBN](https://github.com/jegesmedve09/Free-BBN) | Open-source reimplementation of the PlayStation 2 Broadband Navigator | 12 | 🟢 | C |
| [gta1_re](https://github.com/CriminalRETeam/gta1_re) | Engine reimplementation of Grand Theft Auto; uses original game data (C++) | 12 | 🟢 | C++ |
| [Icewind Dale II decomp](https://github.com/thierbig/iwd2r) | Cross-platform engine for Icewind Dale II built on its decompilation | 12 | 🟢 | C++ |
| [LibertyFlux](https://github.com/monstercameron/LibertyFlux) | GTA IV engine rewritten in Rust function by function by AI agents for Windows x64 and ARM | 12 | 🟢 | Rust |
| [open-sosaria (Ultima)](https://github.com/delcodigo/open-sosaria) | Engine reimplementation of Ultima (1981) for the Apple II | 12 | 🟢 | C |
| [openDOW](https://github.com/rofl0r/openDOW) | remake of the classic amiga game "dogs of war" (C) 1989 elite | 12 | 🟡 | C |
| [OpenRow (Saints Row)](https://github.com/Itismrwonderful/OpenRow) | Open-source reimplementation of Saints Row 1 | 12 | 🟢 |  |
| [Plants vs. Zombies GOTY (re-plants-vs-zombies)](https://github.com/Bamcane/re-plants-vs-zombies) | Reverse-engineered reimplementation / port of Plants vs. Zombies GOTY (re-plants-vs-zombies) | 12 | 🟢 | C++ |
| [remech2-rs (MechWarrior 2)](https://github.com/anpage/remech2-rs) | Open-source reimplementation of the MechWarrior 2 engine in Rust | 12 | 🟢 | C |
| [SuperLemminiToo](https://github.com/Blazingstix/SuperLemminiToo) | My personal fork of SuperLemmini, which itself is a fork of Lemmini | 12 | 🔴 | Java |
| [abadia (La Abadía del Crimen)](https://github.com/ultrabolido/abadia) | Open-source reimplementation of La Abadía del Crimen (ZX Spectrum) | 11 | 🟡 | JavaScript |
| [Amber](https://github.com/Pyrdacor/Amber) | Engine for the Amber trilogy | 11 | 🟢 | C# |
| [e17p (Infinity Engine)](https://github.com/uyjulian/e17p) | Infinity Engine reimplementation in Python | 11 | 🗄️ | Python |
| [evnova-decomp](https://github.com/wraitii/evnova-decomp) | Reimplementation of the Escape Velocity Nova engine from decompilation (SDL3) | 11 | 🟢 | C++ |
| [firestaff](https://github.com/yeager/firestaff) | 🔥 Source-faithful Dungeon Master engine — DM1, CSB, DM2, DM Nexus and Theron's Quest on modern hardware. macOS, Windo... | 11 | 🟢 | C |
| [Megaman3NESRecomp](https://github.com/mstan/Megaman3NESRecomp) | Mega Man 3 recompiled for the NES using nesrecomp · Part of the R.A.I.D. community | 11 | 🟢 | C |
| [mgcarpet (Magic Carpet)](https://github.com/raincz/mgcarpet) | From-scratch engine port of Magic Carpet 1, Hidden Worlds and 2 | 11 | 🟢 | Rust |
| [Ms. Pac-Man (mspacman500 (arcade -> 68k transcode))](https://github.com/jotd666/mspacman500) | Ms. Pac-Man arcade code transcoded to 68k assembly for the Amiga 500 (Arcade) | 11 | 🟢 | Assembly |
| [open-northland](https://github.com/s-nems/open-northland) | A modern, open-source reimplementation of the Cultures game series | 11 | 🟢 | TypeScript |
| [TS-ReSplit](https://github.com/GoomiiV2/TS-ReSplit) | Reverse engineering of the TimeSplitters games toward an asset-compatible engine | 11 | 🔴 | C# |
| [X-Settlers](https://github.com/skarmux/x-settlers) | Re-implementation of classic "TheSettlers" game series using modern technologies like hardware accelerated graphics a... | 11 | 🔴 | C++ |
| [DCSpeedBall2](https://github.com/LemonHaze420/DCSpeedBall2) | SpeedBall 2 for Pocket PC/Dreamcast (WCE), with special thanks to Comby Laurent and LemonHaze | 10 | 🔴 | C++ |
| [Etervale](https://github.com/bencz-games/Etervale) | Open-source reimplementation of Priston Tale in C# and MonoGame | 10 | 🟢 | C# |
| [Heart of the Alien Redux](https://github.com/carstene1ns/hota-redux) | Heart of The Alien - Redux (forked from https://hota.sf.net) | 10 | 🟢 | C |
| [KrabbyQuestEmu](https://github.com/JDrocks450/KrabbyQuestEmu) | Restores SpongeBob: Krabby Quest by reimplementing the original game engine | 10 | 🟡 | C# |
| [ladder (Go)](https://github.com/mengstr/ladder) | Open-source reimplementation of Ladder | 10 | 🔴 | Go |
| [opendw (Deepworld)](https://github.com/kuroppoi/opendw) | Open-source reimplementation of the macOS Deepworld client | 10 | 🟢 | C++ |
| [OpenYR (Yuri's Revenge)](https://github.com/Sovietianqi/OpenYR) | Open-source engine reimplementation of Command & Conquer: Yuri's Revenge | 10 | 🟢 | C++ |
| [rerbr](https://github.com/JodusNodus/rerbr) | Reimplementation of Richard Burns Rally that runs natively on Linux, Mac and Windows | 10 | 🟢 | Rust |
| [RoseRevolution](https://github.com/Akrelia/RoseRevolution) | Unity client reimplementation for the MMORPG ROSE Online | 10 | 🟢 | C# |
| [sm64js](https://github.com/sm64jsarchive/sm64jsarchive) | Super Mario 64 reimplementation in JavaScript. | 10 | 🔴 | JavaScript |
| [Cut the Rope](https://github.com/Bingies24/cuttherope-dx) | Reverse-engineered reimplementation / port of Cut the Rope | 9 | 🟢 | C# |
| [dizgruntled-java](https://github.com/Hugheth/dizgruntled-java) | A java open source remake of Monolith Gruntz (1999) | 9 | 🔴 | Java |
| [ebbsrc](https://github.com/Herringway/ebbsrc) | earthbound beginnings source recreation | 9 | 🟡 | Assembly |
| [farcry-3-bevy](https://github.com/Eamo5/farcry-3-bevy) | Reimplementation of Far Cry 3 in the Bevy game engine | 9 | 🟢 | Rust |
| [olduvai](https://github.com/ksokolowski/olduvai) | From-scratch C++/SDL2 reimplementation of the Prehistorik (1991) engine — bring your own game files. | 9 | 🟢 | C++ |
| [opendaed](https://github.com/AMDmi3/opendaed) | Libre reimplementation of The Daedalus Encounter game | 9 | 🔴 | C++ |
| [OpenLF2](https://github.com/OpenLF2/OpenLF2) | Open-source reimplementation of Little Fighter 2 | 9 | 🟢 | Lua |
| [opensims2](https://github.com/opensims2/opensims2-public) | Native reimplementation of The Sims 2 engine for macOS (Metal) and Windows (D3D12) | 9 | 🟢 | C++ |
| [Powerslide remake](https://github.com/dm999/powerslideremake) | Project remakes main features of video game Powerslide | 9 | 🟢 | C++ |
| [re3-Resurrected](https://github.com/cinchitsolutions/re3-Resurrected) | Clean-room reverse engineering of GTA III / Vice City for PC | 9 | 🟡 | C++ |
| [rust-theft-auto](https://github.com/gaudecker/rust-theft-auto) | Grand Theft Auto engine reimplementation in Rust | 9 | 🔴 | Rust |
| [Chuckie-Egg](https://github.com/pbrook/Chuckie-Egg) | Reverse-engineered Chuckie Egg with ASCII and 3D renderers | 8 | 🔴 | C |
| [daggerpad (Daggerfall)](https://github.com/chrissotraidis/daggerpad) | The Elder Scrolls II: Daggerfall via Daggerfall Unity, rebuilt for iPad | 8 | 🟢 | C# |
| [free-heroes4](https://github.com/tallowmere/free-heroes4) | Open-source C++23 reimplementation of the Heroes of Might and Magic IV engine | 8 | 🟢 | C++ |
| [i76-everywhere](https://github.com/therealjkvalentine/i76-everywhere) | Interstate '76 on Apple Silicon, Steam Deck and modern Windows, with save editor and RE notes | 8 | 🟢 | Python |
| [infernal_js (Infernal Runner)](https://github.com/cyxx/infernal_js) | HTML5 reimplementation of Infernal Runner (Amstrad CPC) | 8 | 🗄️ | Assembly |
| [jspacman](https://github.com/jrhollis/jspacman) | Pac-Man and Ms. Pac-Man reverse engineered in JavaScript | 8 | 🟢 | JavaScript |
| [Lupin Sansei - Pandora no Isan](https://github.com/PavelSha/Lupin-Sansei---Pandora-no-Isan) | An annotated disassembly of the famicom game "Lupin Sansei - Pandora no Isan" (1987). | 8 | 🟢 | Assembly |
| [Prehistorik_js](https://github.com/cyxx/prehistorik_js) | Prehistorik (Demo) engine reimplementation (Emscripten, SDL2) | 8 | 🗄️ | C |
| [ra2-engine](https://github.com/omarelarab/ra2-engine) | Open-source Red Alert 2 / Yuri's Revenge engine for Windows and Android using your game files | 8 | 🟢 | C++ |
| [Railroad Tycoon II reimplementation](https://github.com/pedryvo/rrt2-decomp) | Reverse engineering and Rust reimplementation of Railroad Tycoon II | 8 | 🟢 | Rust |
| [rustyworld](https://github.com/EdMcBane/rustyworld) | Frame-accurate Another World engine reimplementation in Rust | 8 | 🟡 | Rust |
| [th10](https://github.com/Ritosa2333/th10) | A high-fidelity, portable reimplementation of 東方風神録 ～ Mountain of Faith ver 1.00a. | 8 | 🟢 | C++ |
| [TheForceEngineXbox](https://github.com/GTTeancum/TheForceEngineXbox) | The Force Engine (Dark Forces reimplementation) ported to the original Xbox | 8 | 🟢 | C++ |
| [WAGE](https://github.com/asvitkine/wage-engine) | World Builder game engine | 8 | 🔴 | Java |
| [Balloon Fight](https://github.com/MikeDX/balloon-fight) | Remake of Balloon fight by Groovy Gecko, created for the Retro Remakes competition 2003 | 7 | 🔴 | xBase |
| [Call of Duty decomp](https://github.com/opencod1/opencod1) | Open-source reconstruction of Call of Duty (2003) multiplayer | 7 | 🟢 | C |
| [chaos-head](https://github.com/FGRE/chaos-head) | Reimplementation of Chaos;Head visual novel | 7 | 🔴 | CMake |
| [CR1-U](https://github.com/DuIslingr/CR1-U) | From-scratch reimplementation of Chaos Rings (iOS, PS Vita) | 7 | 🟢 | C++ |
| [Dungeon Strikes Back](https://github.com/sparkletwist/DSB) | Dungeon Strikes Back | 7 | 🟡 | C |
| [Minecraft-4K-Decompilation](https://github.com/CelestialAmber/Minecraft-4K-Decompilation) | Decompilation of Minecraft 4K, updated to be a regular application | 7 | 🟢 | Java |
| [open-kf](https://github.com/Scronkfinkle/open-kf) | From-scratch Rust and Bevy reimplementation of Killing Floor (2009) | 7 | 🟢 | Rust |
| [opendana](https://github.com/dvilelaf/opendana) | C11 reimplementation of Solomon's Key 2 / Fire 'n Ice (NES) using your ROM | 7 | 🟢 | C |
| [OpenRedRacing](https://github.com/nynjardin/OpenRedRacing) | Reimplementation of Big Red Racing with quality-of-life improvements | 7 | 🟢 | C++ |
| [Ozymandias](https://github.com/Banderi/Ozymandias) | An open source re-implementation of Pharaoh (1999)'s game engine in Godot 3.6 | 7 | 🟢 | GDScript |
| [pokemon-yellow-typescript](https://github.com/gididaf/pokemon-yellow-typescript) | Pokémon Yellow rewritten in TypeScript for the browser, using data from your own ROM | 7 | 🟢 | TypeScript |
| [re3bevy](https://github.com/imbevystar/rust-gta-3) | Unofficial GTA III reimplementation in Rust with the Bevy engine and ECS | 7 | 🟢 | Rust |
| [rechelon](https://github.com/pkulev/rechelon) | Echelon: free engine reimplementation | 7 | 🔴 | C# |
| [remc1hw](https://github.com/turican0/remc1hw) | Recode Binary code of game/datadisk Magic Carpet1 Hidden Words to C/C++ language(remake MC1 for any platform) | 7 | 🔴 | C++ |
| [sly2-bevy-of-thieves](https://github.com/Campfirecrucifix/sly2-bevy-of-thieves) | From-scratch Rust and Bevy rewrite of Sly 2: Band of Thieves (PS2) | 7 | 🗄️ | Rust |
| [Starfox 64: Recompiled](https://github.com/worleydl/Starfox64Recomp-uwp) | Static recompilation of Starfox 64 for PC (Windows/Linux) (Unofficial UWP) | 7 | 🟢 | C |
| [SuperStarTrek25thGMS](https://github.com/JeodC/SuperStarTrek25thGMS) | A port of Super Star Trek Meets 25th Anniversary to Game Maker Studio 2 | 7 | 🟢 | Game Maker Language |
| [TetrisGBRecomp](https://github.com/mstan/TetrisGBRecomp) | Tetris recompiled for the Game Boy using a fork of gb-recompiled · Part of the R.A.I.D. community | 7 | 🟢 | C |
| [timeco](https://github.com/LBALab/timeco) | Time Commando Reimplementation | 7 | 🟢 | C |
| [TsumuLightRecomp](https://github.com/mstan/TsumuLightRecomp) | Tsumu Light (Japan) recompiled for the Sony PlayStation using psxrecomp, with an English fan-translation · Part of th... | 7 | 🟢 | PowerShell |
| [YodaStoriesNG (Yoda Stories)](https://github.com/sp00nznet/YodaStoriesNG) | Reimplementation of Star Wars: Yoda Stories (1997) in C# and SDL2 | 7 | 🟢 | C# |
| [hulabee](https://github.com/cyxx/hulabee) | Tools and virtual machine for Hulabee Entertainment games | 6 | 🗄️ | C |
| [jy2-copy](https://github.com/MngYou/jy2-copy) | Engine reimplementation of Heroes of Jin Yong 2; uses original game data (JavaScript) | 6 | 🔴 | JavaScript |
| [OpenJill](https://github.com/emeric-martineau/openjill) | Official OpenJill project source repository to understand how Jill of the Jungle game engine work and rewrite it in J... | 6 | 🗄️ | Java |
| [openscreamer](https://github.com/ItsDanik/openscreamer) | Screamer (1995, DOS) reimplemented for Linux from the original program | 6 | 🟢 | C |
| [retruxx](https://github.com/mindflower/retruxx) | Reverse engineered Hard Truck Apocalypse. | 6 | 🟢 | C++ |
| [sekiro-rs](https://github.com/AKJama/sekiro-rs) | Rust/Bevy reimplementation of Sekiro that runs on your own game data | 6 | 🟢 | Rust |
| [sm_rewrite](https://github.com/enderandrew/sm_rewrite) | Super Metroid rewrite project | 6 | 🟡 | C |
| [The Bard's Tale III](https://github.com/Drunella/bt3-easyflash) | Bard's Tale III Easyflash Version | 6 | 🔴 | C |
| [wanderer](https://github.com/vinceh121/wanderer) | A reimplementation of the 2002 video game Project Nomads by Radon Labs | 6 | 🟢 | Java |
| [blues-sdl1](https://github.com/twojstaryzdomu/blues-sdl1) | SDL1 engine reimplementation for Blues Brothers, Jukebox Adventure and Prehistorik 2 | 5 | 🟡 | C |
| [demcstify](https://github.com/stevefan1999-personal/demcstify) | Decompiles Minecraft with Vineflower and reconstructs code with an LLM | 5 | 🟢 | Shell |
| [diablo-2-recompilation](https://github.com/IgorKonovalov/diablo-2-recompilation) | Reimplementation spec of Diablo II LoD 1.14d item, monster and level generation | 5 | 🟢 | Python |
| [duperhex](https://github.com/DavidBuchanan314/duperhex) | Super Hexagon game engine reimplementation | 5 | 🟢 | Rust |
| [GumshoeNESRecomp](https://github.com/mstan/GumshoeNESRecomp) | Gumshoe recompiled for the NES using nesrecomp · Part of the R.A.I.D. community | 5 | 🟢 | C |
| [mdk-godot](https://github.com/nautilusbits/mdk-godot) | Port of MDK (Shiny, 1997) to the Godot engine based on reverse engineering | 5 | 🟢 | GDScript |
| [openchrome](https://github.com/fluidmstr/openchrome) | Clean-room runtime for Dying Light 1 (Chrome Engine 6) using your own assets | 5 | 🟢 | C++ |
| [openpol](https://github.com/jstasiak/openpol) | An open source reimplementation of the first Polish RTS video game Polanie (also known as VICTORY, OSADNICI) | 5 | 🟡 | Rust |
| [opentennis (Hot Shots Tennis)](https://github.com/FIZL0/opentennis) | Remaster of Hot Shots Tennis (Everybody's Tennis) for PC and browser | 5 | 🟢 | Rust |
| [RetroLemmini](https://github.com/Willicious/RetroLemmini) | A newly-maintained version of Lemmini | 5 | 🟢 | Java |
| [RodLegacy](https://github.com/grovdata/RodLegacy) | Modern reimplementation of Street Rod (DOS) | 5 | 🟢 | C++ |
| [rook](https://github.com/AsyncFinn/rook) | Open-source Rust reimplementation of the Roblox engine | 5 | 🟢 | Rust |
| [rugrats](https://github.com/Toyz/rugrats) | Rugrats: Search for Reptar (PS1) rebuilt as a native PC game in Rust | 5 | 🟢 | Rust |
| [scale-miniatures](https://github.com/hivvu/scale-miniatures) | Micro Machines (PC, 1994) rewritten in TypeScript from the disassembly, running natively in the browser. No emulator.... | 5 | 🟢 | TypeScript |
| [Soul Blazer (RustyBlazer)](https://github.com/hellow554/RustyBlazer) | Reverse-engineered reimplementation / port of Soul Blazer (RustyBlazer) | 5 | 🟡 | Assembly |
| [th11](https://github.com/Ritosa2333/th11) | Portable reimplementation of Touhou 11: Subterranean Animism 1.00a | 5 | 🟢 | JavaScript |
| [widebrim (Professor Layton)](https://github.com/bullbin/widebrim) | Playable reimplementation of the engine for Professor Layton and the Diabolical Box (DS) | 5 | 🔴 | Python |
| [hugo.js](https://github.com/cyxx/hugo_js) | Hugo pa Nye Eventyr/Hugo Délire player (Emscripten) | 4 | 🗄️ | C |
| [Jet-Story](https://github.com/adamenkov/jet-story) | Remake of the ZX Spectrum game "Jet-Story" | 4 | 🟢 | Assembly |
| [lilium-salvation](https://github.com/clover-moe/lilium-salvation) | An engine replacement for Dark Salvation | 4 | 🟢 | C |
| [LostVikings](https://github.com/akaWolf/LostVikings) | Translated and rewritten DOS version of Lost Vikings | 4 | 🟢 | C++ |
| [Marble Love](https://github.com/magno73/marble-love) | TypeScript reimplementation of Atari's Marble Madness (1984), incl. Slapstic behaviour | 4 | 🟢 | TypeScript |
| [mb-decomp](https://github.com/Yoshimaster96/mb-decomp) | Engine reimplementation of Super Monkey Ball; uses original game data (C, Assembly) | 4 | 🔴 | C |
| [SuperFoulEgg](https://github.com/ant512/SuperFoulEgg) | Port of Super Foul Egg to MacOSX. | 4 | 🔴 | Objective-C |
| [Trashman](https://github.com/pobtastic/trashman) | A disassembly of Trashman, created using SkoolKit. | 4 | 🟡 | Visual Basic 6.0 |
| [v64tng](https://github.com/mattseabrook/v64tng) | Game Engine re-creation of The 7th Guest | 4 | 🟢 | Assembly |
| [xclannad](https://github.com/weimingtom/xclannad_fork) | My xclannad fork for study | 4 | 🔴 | C |
| [bully-re](https://github.com/LiquidSnake0/bully-re) | Reimplementation of the Bully: Scholarship Edition engine based on the original binary | 3 | 🟢 | C++ |
| [cyrus (Redguard)](https://github.com/michidk/cyrus) | Reimplementation of The Elder Scrolls Adventures: Redguard (1998) in Rust and Bevy | 3 | 🟢 | Rust |
| [FFED3D](https://github.com/corpsofengineers/ffed3d) | Automatically exported from code.google.com/p/ffed3d | 3 | 🔴 | Assembly |
| [GunZRs](https://github.com/OpenRsG/GunZRs) | Rust and Bevy rewrite of GunZ: The Duel that reads the Steam install | 3 | 🟢 | Rust |
| [Hopmon (OpenHopmon)](https://github.com/Teofil98/OpenHopmon) | Reverse-engineered reimplementation / port of Hopmon (OpenHopmon) | 3 | 🟢 | C++ |
| [kys-promise](https://github.com/scarsty/kys-promise) | Engine reimplementation of Heroes of Jin Yong; uses original game data (Pascal) | 3 | 🟢 | Pascal |
| [Oblivion-Reconstructed](https://github.com/themuffinator/Oblivion-Reconstructed) | Reverse-engineered Oblivion Extension Pack source code for original Quake II. | 3 | 🟢 | C |
| [S2HD](https://github.com/SonicOrcaModding/S2HD) | A decompile of Sonic 2 HD (Build 2.0.1012-rc2) and port to Linux, Android and iOS. | 3 | 🟢 | C# |
| [SF1RE](https://github.com/ShiningForceCentral/SF1RE) | Collaborative work on reverse-engineering Shining Force. | 3 | 🟡 | C |
| [Another World for the Commander X16](https://github.com/cosmicr/anotherx16) | Commander X16 Port of the Amiga Game Another World | 2 | 🟢 | Assembly |
| [MechCommander2HD](https://github.com/Ariemeth/MechCommander2HD) | Pending approval, this will be the place where the HD revamp will be tracked. | 2 | 🔴 | C++ |
| [NHL94](https://github.com/abdulahmad/NHL94Genesis) | Work In Progress reverse engineered source of NHL 94 for Sega Genesis. Requires original ROM file to build. | 2 | 🟢 | Assembly |
| [NHLPA93Genesis](https://github.com/abdulahmad/NHLPA93Genesis) | Work In Progress reverse engineered source of NHLPA Hockey 93 for Sega Genesis. Requires original ROM file to build. | 2 | 🟢 | Assembly |
| [Open76](https://github.com/rob518183/Open76) | Interstate '76 engine reimplementation | 2 | 🟢 | C# |
| [Ozymandias](https://github.com/dalerank/Ozymandias) | An open source re-implementation of Pharaoh in the Julius/Augustus engine. | 2 | 🔴 |  |
| [Quarantine](https://github.com/mattseabrook/Quarantine) | Game Engine re-creation of Quarantine by Imagexcel | 2 | 🟢 |  |
| [SITDDISASM](https://github.com/ShiningForceCentral/SITDDISASM) | A disassembly of the game "Shining in the Darkness" for documentation and fan-project purposes. | 2 | 🟡 | Assembly |
| [Snowball War (Ski or Die)](https://github.com/tuunanet/rea-ski-or-die-reconstruction) | REA-assisted reconstruction of the Snowball War minigame from the DOS game Ski or Die | 2 | 🟢 | Rust |
| [Super Star Trek meets 25th Anniversary](https://github.com/emabolo/sst25th) | source code of Super Star Trek 1978 meets 25th Anniversary | 2 | 🟡 | AGS Script |
| [tetris_nes](https://github.com/sanghoonio/nes-tetris) | NES Tetris decompiled and rebuilt in readable Rust | 2 | 🟢 | Rust |
| [Travel With Trashman](https://github.com/pobtastic/travelwithtrashman) | A disassembly of Travel With Trashman, created using SkoolKit. | 2 | 🟡 | Visual Basic 6.0 |
| [ult3src](https://github.com/gondur/ult3src) | ultima 3 exodus reverse enigneered by Sven Carlberg for GBC http://sven.50webs.org/ultima3.html | 2 | 🔴 | C |
| [Uplink](https://github.com/AdrUlb/Uplink) | Decompilation of Uplink by Introversion Software (GOG Linux version, installer gog_uplink_hacker_elite_2.0.0.4.sh) | 2 | 🟢 | C++ |
| [xkanon](https://github.com/weimingtom/xkanon_fork) | My fork of xkanon | 2 | 🔴 | C |
| [Acolyte](https://github.com/gm-archive/acolyte) | Open-source runner for GameMaker Studio 1 games | 1 | 🔴 | C++ |
| [bumpy-reverse](https://github.com/GeReV/bumpy-reverse) | Decompilation of Bumpy's Arcade Fantasy, lead by Claude | 1 | 🟢 | C |
| [Chameleon Twist 2: Recompiled](https://github.com/Rainchus/ChameleonTwist2-JP-Recomp) | Engine reimplementation of Chameleon Twist 2; uses original game data (C++) | 1 | 🟡 | C |
| [earthbound_beginnings](https://github.com/Herringway/earthbound_beginnings) | Unfinished port of Earthbound Beginnings | 1 | 🟢 | D |
| [EarthShakerDS](https://github.com/ant512/EarthShakerDS) | Port of the classic ZX Spectrum game Earth Shaker to the Nintendo DS. | 1 | 🔴 | C++ |
| [ff1snes](https://github.com/Entroper/ff1snes) | FF1 for SNES, written from scratch. | 1 | 🟡 | Assembly |
| [OpenGG (Gearhead Garage)](https://github.com/tymsky/OpenGG) | Open-source engine for Gearhead Garage: The Virtual Mechanic (1999) | 1 | 🟢 | C# |
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
| [Firefighter](https://gitlab.com/esr/firefighter) | Unix port of the 1985 DOS shareware game Firefighter, rebuilt in Rust from its binary |  | ⚪ |  |
| [FreeCS](https://sourceforge.net/projects/freecs-1-5/) | Free-software re-implementation of Counter-Strike 1.5 running on the FTEQW engine. |  | ⚪ |  |
| [Freenukum (Duke Nukem)](https://gitlab.com/silwol/freenukum) | Reimplementation of the 1991 Duke Nukem episodes that uses the original game data |  | ⚪ |  |
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
| [Stone Kingdoms (Stronghold)](https://gitlab.com/stone-kingdoms/stone-kingdoms) | Real-time strategy game in LÖVE based on Stronghold (2001); uses the original assets |  | ⚪ |  |
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
| [project-restoration](https://github.com/leoetlino/project-restoration) | Majora's Mask 3D patch restoring original mechanics via reverse engineering | 810 | 🔴 | C++ |
| [Silent Hill 2 Enhanced Edition](https://github.com/elishacloud/Silent-Hill-2-Enhancements) | A project designed to enhance Silent Hill 2 (SH2) graphics and audio for the PC. It also includes scripts to build or... | 717 | 🟢 | C |
| [Plants-vs.-Zombies-Online-Battle](https://github.com/Zhuagenborn/Plants-vs.-Zombies-Online-Battle) | Two-player online battle mode for Plants vs. Zombies built via reverse engineering and DLL injection | 626 | 🟡 | C++ |
| [HaloCEVR](https://github.com/LivingFray/HaloCEVR) | VR conversion of the original PC Halo: Combat Evolved | 448 | 🟢 | C++ |
| [UnofficialCrusaderPatch2](https://github.com/UnofficialCrusaderPatch/UnofficialCrusaderPatch2) | Unofficial balancing and bugfix patch installer for Stronghold Crusader | 434 | 🟡 | C# |
| [Wind Waker Randomizer](https://github.com/LagoLunatic/wwrando) | Wind Waker Randomizer | 427 | 🟢 | Python |
| [mgs2sos](https://github.com/oct0xor/mgs2sos) | Mod adding third-person camera and controls to MGS2: Substance | 311 | 🔴 | C++ |
| [PAL3patch](https://github.com/zhangboyang/PAL3patch) | Resolution patch for Chinese Paladin 3 | 250 | 🟡 | C |
| [sc2kfix](https://github.com/sc2kfix/sc2kfix) | Bugfix and modding plugin for SimCity 2000 Special Edition | 223 | 🟢 | C++ |
| [popcap-patches](https://github.com/cheez3d/popcap-patches) | Patched executables and research notes for PopCap games | 195 | 🔴 |  |
| [gb-save-states](https://github.com/mattcurrie/gb-save-states) | Patches that add save-state support to Game Boy games on original hardware | 193 | 🟡 | Assembly |
| [Ultima IV Remastered](https://github.com/MagerValp/u4remastered) | Ultima IV Remastered for the C64 | 123 | 🔴 | Assembly |
| [tekken3-expanded](https://github.com/omarma/tekken3-expanded) | Adds Tekken Tag Tournament characters to Tekken 3 | 108 | 🟢 | C++ |
| [magicka-patch](https://github.com/Alexander-Aue-Johr/magicka-patch) | Reverse engineered fixes and optimisations for Magicka | 90 | 🟢 | C# |
| [nge_2_re](https://github.com/rezual/nge_2_re) | Neon Genesis Evangelion 2 reverse engineering and translation | 79 | 🟢 | Python |
| [sf4e](https://github.com/fabeloper/sf4e) | Rollback netcode mod for Ultra Street Fighter IV (Steam) | 63 | 🟢 | C++ |
| [v-on-patcher](https://github.com/pairomaniac/v-on-patcher) | Patcher for Cyber Troopers Virtual-On (PC, 1997) with modern hardware and online support | 63 | 🟢 | Python |
| [Lotus STE](https://github.com/jonathanopalise/lotus-ste) | Enhancements to the Atari ST version of Lotus Esprit Turbo Challenge to support STE hardware features | 42 | 🔴 | Assembly |
| [NewerSMBDS](https://github.com/Newer-Team/NewerSMBDS) | Newer Super Mario Bros. DS, a total-conversion mod built on reverse-engineered NSMB code | 39 | 🟢 | C |
| [Ultima V Remastered](https://github.com/Drunella/u5remastered) | Ultima V remastered for EasyFlash and 1581 | 32 | 🟡 | Assembly |
| [Beasts and Bumpkins Fan Patch](https://github.com/bb-patch/bb-patch) | Tool for Beasts and Bumpkins game data (osgameclones) (Go) | 29 | 🔴 | Go |
| [TTDPatch](https://github.com/ttdpatch/ttdpatch) | The master TTDPatch repository | 11 | 🔴 | Assembly |

## Game Network Protocols & APIs

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [mineflayer](https://github.com/PrismarineJS/mineflayer) | High-level JavaScript API for creating Minecraft bots | 7,642 | 🟢 | JavaScript |
| [Geyser](https://github.com/GeyserMC/Geyser) | Proxy translating Minecraft Bedrock clients to Java Edition servers | 5,929 | 🟢 | Java |
| [Hearthstone Deck Tracker](https://github.com/HearthSim/Hearthstone-Deck-Tracker) | Deck tracker for Hearthstone on Windows that reads game logs and memory | 4,924 | 🟢 | C# |
| [Greenlight](https://github.com/unknownskl/greenlight) | Open-source client for Xbox Cloud Gaming (xCloud) and Xbox home streaming | 2,905 | 🟢 | TypeScript |
| [Velocity](https://github.com/PaperMC/Velocity) | High-performance Minecraft Java proxy server | 2,285 | 🟢 | Java |
| [Minecraft Console Client](https://github.com/MCCTeam/Minecraft-Console-Client) | Lightweight console Minecraft client for chat and automated scripts | 2,170 | 🟢 | C# |
| [Deceive](https://github.com/molenzwiebel/Deceive) | XMPP proxy that lets you appear offline in League of Legends, VALORANT and LoR | 1,737 | 🟢 | C# |
| [ViaVersion](https://github.com/ViaVersion/ViaVersion) | Lets newer Minecraft clients connect to older server versions by translating packets | 1,647 | 🟢 | Java |
| [OpenKore](https://github.com/OpenKore/openkore) | Open-source custom client and automation tool for Ragnarok Online | 1,539 | 🟢 | Perl |
| [node-minecraft-protocol](https://github.com/PrismarineJS/node-minecraft-protocol) | Parse and serialize Minecraft Java packets, with auth and encryption | 1,423 | 🟢 | JavaScript |
| [HSTracker](https://github.com/HearthSim/HSTracker) | Hearthstone deck tracker for macOS | 1,258 | 🟢 | Swift |
| [PokeGOAPI-Java](https://github.com/Grover-c13/PokeGOAPI-Java) | Pokemon Go API | 1,046 | 🔴 | Java |
| [node-steam](https://github.com/seishun/node-steam) | Interface directly with Steam CM servers from Node.js (archived) | 1,000 | 🗄️ | JavaScript |
| [go-mc](https://github.com/Tnze/go-mc) | Collection of Go libraries for the Minecraft Java protocol and data formats | 983 | 🟡 | Go |
| [GameTracking-CS2](https://github.com/SteamTracking/GameTracking-CS2) | Automated tracking of Counter-Strike 2 game file, string and protobuf changes | 975 | 🟢 | Slang |
| [minecraft-data](https://github.com/PrismarineJS/minecraft-data) | Language-independent Minecraft protocol and game data for clients, servers and libraries | 957 | 🟢 | JavaScript |
| [MCProtocolLib](https://github.com/GeyserMC/MCProtocolLib) | Java library for Minecraft Java client/server protocol communication | 908 | 🟢 | Java |
| [pyCraft](https://github.com/ammaraskar/pyCraft) | Minecraft Java client networking library in Python | 845 | 🟡 | Python |
| [pgoapi](https://github.com/pogodevorg/pgoapi) | Unofficial Pokemon GO API in Python (archived) | 840 | 🗄️ | Python |
| [NintendoClients](https://github.com/kinnay/NintendoClients) | Python package to communicate with Switch, Wii U and 3DS servers | 768 | 🟢 | Python |
| [steampy](https://github.com/bukson/steampy) | Python Steam trading library using Steam's internal web endpoints | 666 | 🟡 | Python |
| [ViaProxy](https://github.com/ViaVersion/ViaProxy) | Standalone proxy translating between Minecraft protocol versions, including Bedrock and classic | 663 | 🟢 | Java |
| [NintendoSwitchRESTAPI](https://github.com/ZekeSnider/NintendoSwitchRESTAPI) | Reverse engineered REST API of the Nintendo Switch iOS app | 658 | 🔴 |  |
| [nxapi](https://github.com/samuelthomas2774/nxapi) | Nintendo Switch Online/Parental Controls app APIs. Show your Nintendo Switch presence in Discord, get friend... | 633 | 🟢 | TypeScript |
| [steam-tradeoffer-manager](https://github.com/DoctorMcKay/node-steam-tradeoffer-manager) | Node.js Steam trade offer management library | 605 | 🟢 | JavaScript |
| [valorant-api-docs](https://github.com/techchrism/valorant-api-docs) | Documentation for internal VALORANT client API endpoints | 595 | 🟡 | TypeScript |
| [SteamTracking Protobufs](https://github.com/SteamTracking/Protobufs) | Auto-tracked protobuf definitions extracted from Steam, CS2, Dota 2, Deadlock and TF2 | 586 | 🟢 | Shell |
| [gophertunnel](https://github.com/Sandertv/gophertunnel) | Go library for Minecraft Bedrock Edition networking, clients and proxies | 578 | 🟢 | Go |
| [node-steamcommunity](https://github.com/DoctorMcKay/node-steamcommunity) | Node.js module to interact with Steam Community web interfaces | 578 | 🟢 | JavaScript |
| [unofficial-valorant-api](https://github.com/Henrik-3/unofficial-valorant-api) | Unofficial VALORANT API built on the in-game API endpoints | 561 | 🟢 | JavaScript |
| [Fortnite Endpoints Documentation](https://github.com/LeleDerGrasshalmi/FortniteEndpointsDocumentation) | Unofficial documentation of Fortnite and Epic Games API endpoints | 487 | 🟢 |  |
| [bedrock-protocol](https://github.com/PrismarineJS/bedrock-protocol) | Minecraft Bedrock protocol library with authentication and encryption | 485 | 🟢 | JavaScript |
| [s3s](https://github.com/frozenpandaman/s3s) | Successor to splatnet2statink. Takes battle data from the SplatNet 3 app and uploads it to stat.ink! | 463 | 🟡 | Python |
| [go-steam](https://github.com/Philipp15b/go-steam) | Steam's network protocol implemented in Go for automation without a Steam client | 433 | 🟡 | Go |
| [psn-api](https://github.com/achievements-app/psn-api) | JavaScript library to get trophy, user and game data from the PlayStation Network | 430 | 🟢 | TypeScript |
| [EpicResearch](https://github.com/MixV2/EpicResearch) | Research and documentation of Epic Games' undocumented APIs | 426 | 🟡 |  |
| [Cloudburst Protocol](https://github.com/CloudburstMC/Protocol) | Java protocol library for Minecraft Bedrock Edition | 416 | 🟢 | Java |
| [prismarine-viewer](https://github.com/PrismarineJS/prismarine-viewer) | Web-based 3D viewer for Minecraft servers and bots | 402 | 🟢 | JavaScript |
| [NSO-RPC](https://github.com/MCMi460/NSO-RPC) | Shows Nintendo Switch playing status in Discord using the Nintendo Switch Online app API | 385 | 🟡 | Python |
| [psn-php](https://github.com/Tustin/psn-php) | PHP wrapper for the PlayStation Network API | 373 | 🟢 | PHP |
| [node-globaloffensive](https://github.com/DoctorMcKay/node-globaloffensive) | Node.js client for the CS2 game coordinator protocol | 367 | 🟢 | JavaScript |
| [gumer-psn](https://github.com/jhewt/gumer-psn) | PlayStation Network API written in Node.js | 348 | 🗄️ | JavaScript |
| [splatnet2statink](https://github.com/frozenpandaman/splatnet2statink) | Fetches Splatoon 2 battle data from the SplatNet 2 app API and uploads to stat.ink | 343 | 🟡 | Python |
| [rustplus.js](https://github.com/liamcottle/rustplus.js) | Unofficial Node.js library for the Rust+ companion protocol | 322 | 🟢 | JavaScript |
| [GameTracking](https://github.com/SteamTracking/GameTracking) | Automated dumps of Valve game files and protos to track changes | 308 | 🟢 | Shell |
| [RiiConnect24 Patcher](https://github.com/KcrPL/RiiConnect24-Patcher) | Patches Wii channels to use RiiConnect24's revived WiiConnect24 services | 306 | 🟢 | Batchfile |
| [api](https://github.com/helldivers-2/api) | Community API for Helldivers 2 game data | 300 | 🟢 | C# |
| [python-hearthstone](https://github.com/HearthSim/python-hearthstone) | Hearthstone Python library: card defs, DBF, enums and log parser | 277 | 🟢 | Python |
| [steam-totp](https://github.com/DoctorMcKay/node-steam-totp) | Node.js generator for Steam Guard mobile TOTP codes and confirmation keys | 257 | 🔴 | JavaScript |
| [steam.py](https://github.com/Gobot1234/steam.py) | Async Python wrapper for the Steam API and Steam CM protocol | 239 | 🟢 | Python |
| [Inkay](https://github.com/PretendoNetwork/Inkay) | Wii U Aroma plugin that patches the console to use Pretendo Network servers | 234 | 🟢 | C++ |
| [rustplus-desktop](https://github.com/Pronwan/rustplus-desktop) | Unofficial Rust+ desktop app | 217 | 🟢 | C# |
| [xbox-webapi-python](https://github.com/OpenXbox/xbox-webapi-python) | A python library to authenticate with Xbox Live via your Microsoft Account and provides Xbox related Web-API. | 209 | 🟢 | Python |
| [steam-session](https://github.com/DoctorMcKay/node-steam-session) | Node.js module implementing Steam's auth server login to obtain refresh and web tokens | 198 | 🟢 | TypeScript |
| [psnawp](https://github.com/isFakeAccount/psnawp) | [Mirror] PlayStation Network API Python | 195 | 🟢 | Python |
| [go-dota2](https://github.com/paralin/go-dota2) | Go client for the Dota 2 game coordinator protocol | 184 | 🟢 | Go |
| [BedrockProtocol](https://github.com/pmmp/BedrockProtocol) | PHP implementation of the Minecraft Bedrock network protocol | 177 | 🗄️ | PHP |
| [slippi-js](https://github.com/project-slippi/slippi-js) | JavaScript parser for Super Smash Bros. Melee Slippi replay files | 168 | 🟢 | TypeScript |
| [GOG DB](https://github.com/Yepoleb/gogdb) | Website and scraper collecting GOG game data from GOG's internal APIs | 164 | 🟢 | Python |
| [LCU and Riot Client API docs](https://github.com/KebsCS/lcu-and-riotclient-api) | Documentation of League of Legends LCU and Riot Client local API endpoints | 160 | 🟢 | HTML |
| [psn-api (Python)](https://github.com/mgp25/psn-api) | PlayStation Network API client in Python | 134 | 🗄️ | Python |
| [squid-tracks](https://github.com/hymm/squid-tracks) | Unofficial desktop client for Nintendo SplatNet 2 | 134 | 🔴 | JavaScript |
| [SteamWebPipes](https://github.com/xPaw/SteamWebPipes) | Pipes Steam PICS changelist events to websockets using SteamKit | 134 | 🗄️ | C# |
| [csgo (python)](https://github.com/ValvePython/csgo) | Python module to interact with the CS:GO game coordinator | 133 | 🔴 | Python |
| [lcu-driver](https://github.com/sousa-andre/lcu-driver) | Python interface for the League of Legends client local API | 123 | 🟡 | Python |
| [SAMP-Mobile](https://github.com/kuzia15/SAMP-Mobile) | Open-source SA:MP mobile multiplayer client | 122 | 🟢 |  |
| [green-vita](https://github.com/Day-OS/green-vita) | Xbox Cloud Gaming client for PlayStation Vita | 120 | 🟢 | Rust |
| [lcu-connector](https://github.com/Pupix/lcu-connector) | Node.js connector for the League of Legends client (LCU) local API | 116 | 🟢 | JavaScript |
| [ShinraMeter](https://github.com/neowutran/ShinraMeter) | TERA DPS meter based on decoded game packets | 115 | 🟡 | C# |
| [xboxlive-auth](https://github.com/XboxReplay/xboxlive-auth) | Xbox Live authentication library for Node.js | 115 | 🟢 | TypeScript |
| [valorant.js](https://github.com/liamcottle/valorant.js) | Unofficial Node.js library for the VALORANT client API | 111 | 🟡 | JavaScript |
| [Kasumi](https://github.com/p0mpurin/Kasumi) | Unofficial native GeForce NOW and Xbox Cloud Gaming client for the New Nintendo 3DS | 110 | 🟢 | C |
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
| [hass-psn](https://github.com/JackJPowell/hass-psn) | Home Assistant integration for the PlayStation Network via its unofficial API | 80 | 🟢 | Python |
| [HearthDb](https://github.com/HearthSim/HearthDb) | .NET Hearthstone card database extracted from game data | 80 | 🟢 | C# |
| [prismarine-auth](https://github.com/PrismarineJS/prismarine-auth) | Microsoft/Xbox Live authentication flow for Minecraft clients | 77 | 🟢 | JavaScript |
| [xbox-smartglass-core-python](https://github.com/OpenXbox/xbox-smartglass-core-python) | Python implementation of the Xbox One SmartGlass core protocol | 75 | 🗄️ | Python |
| [FFXIVOpcodeWizard](https://github.com/karashiiro/FFXIVOpcodeWizard) | Automated Final Fantasy XIV network opcode discovery | 68 | 🔴 | C# |
| [MoeXCOM](https://github.com/hdk5/MoeXCOM) | Reverse engineering Blue Archive | 67 | 🔴 | C# |
| [Haruki-Sekai-API](https://github.com/Team-Haruki/Haruki-Sekai-API) | Unofficial API proxy for Project Sekai game data | 64 | 🟢 | Rust |
| [node-epicgames-fortnite-client](https://github.com/SzymonLisowiec/node-epicgames-fortnite-client) | Unofficial Fortnite client in JavaScript built on the Epic Games launcher protocol | 64 | 🔴 | JavaScript |
| [node-haxball](https://github.com/wxyz-abcd/node-haxball) | API to build Haxball clients and bots via its reversed protocol | 63 | 🟢 | JavaScript |
| [rlapi](https://github.com/dank/rlapi) | Reverse engineered Rocket League internal HTTP and WebSocket API | 61 | 🟢 | Go |
| [pyremoteplay](https://github.com/ktnrg45/pyremoteplay) | Python library implementing the PlayStation Remote Play protocol | 56 | 🗄️ | Python |
| [diveharder_api.py](https://github.com/helldivers-2/diveharder_api.py) | FastAPI proxy exposing Helldivers 2 API data for community developers | 55 | 🟡 | Python |
| [XiPackets](https://github.com/atom0s/XiPackets) | Reverse engineered packet documentation for Final Fantasy XI | 55 | 🟢 |  |
| [fut-api](https://github.com/lorenzh/fut-api) | Unofficial FIFA Ultimate Team API client | 54 | 🗄️ | JavaScript |
| [CPPS-PCL](https://github.com/turicfr/CPPS-PCL) | Python client library for Club Penguin private servers | 48 | 🔴 | Python |
| [UniSpySDK](https://github.com/GameProgressive/UniSpySDK) | Cleaned-up GameSpy SDK used to build GameSpy replacement servers | 46 | 🟢 | C |
| [openfoxwq_client](https://github.com/openfoxwq/openfoxwq_client) | Multiplatform unofficial client for the Fox Go server | 45 | 🗄️ | Dart |
| [wot-api-description](https://github.com/thunder-spb/wot-api-description) | World of Tanks unofficial API description | 45 | 🗄️ | PHP |
| [xboxlive-api](https://github.com/XboxReplay/xboxlive-api) | Simple Xbox Live API wrapper for Node.js | 44 | 🔴 | TypeScript |
| [trackmania2020apidocumentation](https://github.com/The-Firexx/trackmania2020apidocumentation) | Trackmania 2020 unofficial API documentation | 43 | 🗄️ |  |
| [Useful-ValorantAPI-Info](https://github.com/Soneliem/Useful-ValorantAPI-Info) | Resources and code for Valorant's unofficial API | 40 | 🔴 | Python |
| [Agar.io Protocol](https://github.com/dollthing/Agar.io-Protocol) | Reverse-engineered client/server protocol of the browser game Agar.io | 38 | 🔴 |  |
| [BNETDocs](https://github.com/BNETDocs/bnetdocs-web) | Documentation website for Blizzard's Battle.net classic protocols | 36 | 🟢 | JavaScript |
| [Booma.Proxy](https://github.com/HelloKitty/Booma.Proxy) | .NET libraries for the Phantasy Star Online: Blue Burst protocol | 36 | 🔴 | C# |
| [HyCraft](https://github.com/EdwardBelt/HyCraft) | Protocol bridge that lets Minecraft 1.21 clients join Hytale servers (PC) | 35 | 🟢 | Java |
| [nex-protocols-common-go](https://github.com/PretendoNetwork/nex-protocols-common-go) | Go implementations of common Nintendo NEX methods shared by Pretendo game servers | 31 | 🟢 | Go |
| [psn100](https://github.com/Ragowit/psn100) | PlayStation trophy tracking site with leaderboards built on the PSN API | 28 | 🟢 | PHP |
| [Steam-Client-Docs](https://github.com/Bluscream/Steam-Client-Docs) | Unofficial documentation of the Steam client | 28 | 🟡 |  |
| [fc27-clubs-api](https://github.com/1erkandogan/fc27-clubs-api) | Unofficial Python client for the EA Sports FC 27 Pro Clubs API | 24 | 🟢 | Python |
| [GameSpyDocs](https://github.com/GameProgressive/GameSpyDocs) | Protocol documentation of GameSpy services for replacement servers | 23 | 🔴 | TeX |
| [market-pricing](https://github.com/node-steam/market-pricing) | Wrapper for the unofficial Steam Market pricing API | 22 | 🔴 | TypeScript |
| [Utinni](https://github.com/ptklatt/Utinni) | Plugin and injection framework for the Star Wars Galaxies client | 21 | 🔴 | C# |
| [pyps4-2ndscreen](https://github.com/ktnrg45/pyps4-2ndscreen) | Python library to control a PS4 via the PS4 Second Screen protocol | 20 | 🗄️ | Python |
| [OpenSpartan Workshop](https://github.com/OpenSpartan/openspartan-workshop) | Desktop app to track Halo Infinite stats and progression via the unofficial Halo API | 19 | 🟢 | C# |
| [krunker.io](https://github.com/fasetto/krunker.io) | Unofficial API for the krunker.io game social page | 13 | 🔴 | JavaScript |
| [node-mojang](https://github.com/astra137/node-mojang) | Unofficial Node.js library for Mojang's HTTP APIs (auth, profiles, skins) | 12 | 🔴 | JavaScript |
| [hytale-protocol](https://github.com/soksx/hytale-protocol) | Documentation of Hytale's QUIC/UDP network protocol, extracted from the game | 11 | 🟢 | TypeScript |
| [Nanocraft](https://github.com/HeathLoganCampbell/Nanocraft) | Server that mimics the Minecraft 1.8.9 network protocol | 11 | 🟢 | Java |
| [Splix.io Protocol](https://github.com/JosefKuchar/Splix.io-Protocol) | Reverse-engineered network protocol of the browser game splix.io | 11 | 🔴 |  |
| [pvpgn-hash](https://github.com/pvpgn/pvpgn-hash) | Battle.net v1.0 password hash algorithm in several languages | 10 | 🟡 | JavaScript |
| [NPTicket](https://github.com/LittleBigRefresh/NPTicket) | C# library to read and verify PSN authentication tickets for custom servers | 9 | 🟡 | C# |
| [a2kit](https://github.com/nuriland/a2kit) | Passive protocol decoder and analysis toolkit for AION 2 | 8 | 🟢 | Go |
| [SniffSniffSquared](https://github.com/Miou-zora/SniffSniffSquared) | Passive network sniffer and protobuf decoder for the Dofus 3 game protocol | 8 | 🟢 | TypeScript |
| [CheckRevision](https://github.com/pvpgn/CheckRevision) | CheckRevision implementation for Classic Battle.net game version checks | 7 | 🔴 | C++ |
| [growtopia-api](https://github.com/H-pun/growtopia-api) | Unofficial Growtopia API for item data and sprites | 7 | 🟢 | Python |
| [access-key-extractor](https://github.com/PretendoNetwork/access-key-extractor) | Extracts NEX server access keys from Wii U and 3DS game dumps | 6 | 🟢 | Go |
| [Durango](https://github.com/AlexArchive/Durango) | Unofficial read-only API client for Xbox LIVE | 6 | 🔴 | C# |
| [PSCrypto](https://github.com/psforever/PSCrypto) | Crypto library for the PlanetSide 1 client protocol | 5 | 🔴 | C++ |
| [ffxiv](https://github.com/ffxiv/ffxiv) | Unofficial Final Fantasy XIV toolkit for Ruby with a Lodestone scraper | 4 | 🔴 | Ruby |
| [GameLogger](https://github.com/psforever/GameLogger) | PlanetSide 1 event logger GUI for protocol analysis | 4 | 🔴 | C# |
| [medius-wireshark](https://github.com/hashsploit/medius-wireshark) | Wireshark dissector for Sony's Medius online protocol | 4 | 🔴 | Lua |
| [valorant-xmpp-watcher](https://github.com/techchrism/valorant-xmpp-watcher) | Connects to and logs VALORANT XMPP presence and roster events | 4 | 🟡 | TypeScript |
| [BFH-Master-Protocol](https://github.com/M0THERB0ARD/BFH-Master-Protocol) | Technical specification of the Battlefield Heroes master server protocol | 3 | 🔴 |  |
| [ddl-parser](https://github.com/PretendoNetwork/ddl-parser) | Parses NEX DDL protocol definitions out of Wii U and 3DS game dumps | 3 | 🔴 | JavaScript |
| [eo-captured-packets](https://github.com/ethanmoffat/eo-captured-packets) | JSON captures of Endless Online protocol packets for server emulator work | 3 | 🟢 |  |
| [halo_api](https://github.com/nuzzles/halo_api) | Unofficial Halo Infinite REST API client for Rust: service record and match history | 3 | 🟢 | Rust |
| [nex-documentation-generator](https://github.com/PretendoNetwork/nex-documentation-generator) | Builds docs for NEX protocols from DDL parse trees in Wii U and 3DS game dumps | 3 | 🟡 | JavaScript |
| [NexusForever.PacketParser](https://github.com/NexusForever/NexusForever.PacketParser) | Packet parser for WildStar, from the NexusForever emulator project | 3 | 🔴 |  |
| [Grunt](https://github.com/dend/grunt) | Unofficial API wrapper and documentation for the Halo Infinite web services | 0 | 🟢 | C# |

## Launchers & Store Clients

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Playnite](https://github.com/JosefNemec/Playnite) | Open-source game library manager integrating Steam, Epic, GOG, EA, Ubisoft and more store libraries | 14,351 | 🟢 | C# |
| [ArchiSteamFarm](https://github.com/JustArchiNET/ArchiSteamFarm) | C# Steam client application built on SteamKit2 for multi-account card farming and automation | 13,768 | 🟢 | C# |
| [Heroic Games Launcher](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher) | Open-source launcher for Epic, GOG and Amazon Games libraries on Linux, Windows and macOS | 12,509 | 🟢 | TypeScript |
| [Prism Launcher](https://github.com/PrismLauncher/PrismLauncher) | Open-source Minecraft launcher managing multiple instances and Microsoft account login | 10,905 | 🟢 | C++ |
| [HMCL](https://github.com/HMCL-dev/HMCL) | Hello Minecraft! Launcher, a cross-platform third-party Minecraft launcher | 10,712 | 🟢 | Java |
| [Decky Loader](https://github.com/SteamDeckHomebrew/decky-loader) | Plugin loader for the Steam Deck that injects into the Steam client UI | 7,420 | 🟢 | TypeScript |
| [Legendary](https://github.com/legendary-gl/legendary) | Open-source CLI replacement for the Epic Games Launcher built on Epic's undocumented APIs | 5,344 | 🟢 | Python |
| [MultiMC](https://github.com/MultiMC/Launcher) | Custom Minecraft launcher for managing multiple isolated installations | 4,684 | 🟢 | C++ |
| [Millennium](https://github.com/SteamClientHomebrew/Millennium) | Framework for Steam client themes and plugins via injection into the CEF UI | 4,503 | 🟢 | C++ |
| [Steam Desktop Authenticator](https://github.com/Jessecar96/SteamDesktopAuthenticator) | Desktop implementation of Steam's mobile authenticator (Steam Guard) app | 3,828 | 🟡 | C# |
| [DepotDownloader](https://github.com/SteamRE/DepotDownloader) | Steam depot downloader built on the SteamKit2 reverse-engineered Steam protocol library | 3,483 | 🟢 | C# |
| [XIVLauncher](https://github.com/goatcorp/FFXIVQuickLauncher) | Custom third-party launcher for Final Fantasy XIV that reimplements the login flow | 3,194 | 🟢 | C# |
| [Bloxstrap](https://github.com/bloxstraplabs/bloxstrap) | Alternative bootstrapper for the Roblox client with extra configuration | 3,185 | 🟢 | C# |
| [chiaki-ng](https://github.com/chiaki-ng/chiaki-ng) | Open-source PlayStation 4/5 Remote Play client, successor of Chiaki | 2,894 | 🟢 | C |
| [GameHub](https://github.com/tkashkin/GameHub) | Unified game library for Steam, GOG and Humble Bundle (archived) | 2,858 | 🗄️ | Vala |
| [BoilR](https://github.com/PhilipK/BoilR) | Syncs games from Epic, GOG, Origin, Amazon and other launchers into the Steam library | 1,921 | 🟢 | Rust |
| [Pluvia](https://github.com/oxters168/Pluvia) | Lightweight unofficial Steam client for Android | 1,724 | 🟢 | C |
| [mcpelauncher](https://github.com/minecraft-linux/mcpelauncher-manifest) | Runs the Android build of Minecraft Bedrock natively on Linux and macOS | 1,703 | 🟢 | CMake |
| [Minigalaxy](https://github.com/sharkwouter/minigalaxy) | Simple unofficial GOG client for Linux | 1,332 | 🟢 | Python |
| [steamguard-cli](https://github.com/dyc3/steamguard-cli) | Linux CLI for Steam Guard 2FA codes and trade/market confirmations | 1,073 | 🟢 | Rust |
| [MC Bedrock Version Launcher](https://github.com/MCMrARM/mc-w10-version-launcher) | Installs and switches between multiple Minecraft Bedrock (Windows 10) versions | 1,062 | 🟢 | C++ |
| [steam-tui](https://github.com/dmadisetti/steam-tui) | Rust TUI Steam client driving steamcmd | 1,039 | 🟢 | Rust |
| [Rare](https://github.com/RareDevs/Rare) | Qt GUI alternative to the Epic Games Launcher, built on Legendary | 941 | 🟢 | Python |
| [LGOGDownloader](https://github.com/Sude-/lgogdownloader) | Unofficial GOG.com downloader for Linux using the same API as GOG Galaxy | 919 | 🟢 | C++ |
| [Vinegar](https://github.com/vinegarhq/vinegar) | Open-source launcher/manager for running Roblox Studio on Linux | 799 | 🟢 | Go |
| [humblebundle-downloader](https://github.com/xtream1101/humblebundle-downloader) | Downloads a Humble Bundle library via Humble's internal API | 610 | 🗄️ | Python |
| [gogrepo](https://github.com/eddie3/gogrepo) | Python tool to download a full GOG.com game and bonus collection for offline use | 544 | 🔴 | Python |
| [SBRW GameLauncher](https://github.com/SoapboxRaceWorld/GameLauncher_NFSW) | Unofficial launcher for Need for Speed: World community servers | 536 | 🟡 | C# |
| [steamctl](https://github.com/ValvePython/steamctl) | Command-line tool to control Steam: download depots, workshop items, manage apps and accounts | 377 | 🟡 | Python |
| [comet](https://github.com/imLinguin/comet) | Open source implementation of the GOG Galaxy communication service | 372 | 🟢 | Rust |
| [nile](https://github.com/imLinguin/nile) | Unofficial Amazon Games client (CLI) reimplementing the Amazon Games app's protocol | 361 | 🟢 | Python |
| [CnCNet Client](https://github.com/CnCNet/xna-cncnet-client) | Online multiplayer client for classic Command & Conquer games on the CnCNet service | 320 | 🟢 | C# |
| [Slippi Launcher](https://github.com/project-slippi/slippi-launcher) | Launcher for Project Slippi, the rollback netplay and replay system for Super Smash Bros. Melee | 310 | 🟢 | TypeScript |
| [open-steamworks](https://github.com/SteamRE/open-steamworks) | Reverse engineered headers for Valve's Steam client interfaces | 263 | 🗄️ | C# |
| [cordial](https://github.com/luohoa97/cordial) | Open-source runtime to run the Roblox client natively on Linux | 242 | 🟢 | Rust |
| [xcloud-shield](https://github.com/mistertest/xcloud-shield) | Unofficial Xbox Cloud Gaming app for Nvidia Shield TV | 236 | 🔴 | Java |
| [Maxima](https://github.com/ArmchairDevelopers/Maxima) | Free open-source replacement for the EA Desktop launcher for Linux and Windows | 234 | 🟢 | Rust |
| [xbox-xcloud-player](https://github.com/unknownskl/xbox-xcloud-player) | Library implementing the Xbox Cloud Gaming / home streaming WebRTC protocol | 197 | 🟢 | TypeScript |
| [heroic-gogdl](https://github.com/Heroic-Games-Launcher/heroic-gogdl) | GOG download/install module for Heroic using GOG Galaxy's content-system APIs | 179 | 🟢 | Python |
| [games_nebula](https://github.com/yancharkin/games_nebula) | Unofficial GOG client for Linux | 160 | 🟡 | Python |
| [SteamAppInfo](https://github.com/xPaw/SteamAppInfo) | Parser for Steam client appinfo.vdf and packageinfo.vdf files | 144 | 🟢 | C# |
| [libnxbox](https://github.com/ursusworks/libnxbox) | Xbox Cloud Gaming streaming client for Nintendo Switch homebrew | 131 | 🟢 |  |
| [RA3Bar-RA3Launcher](https://github.com/lanyizi/RA3Bar-RA3Launcher) | Reimplementation of the Red Alert 3 game launcher | 131 | 🔴 | C++ |
| [jetisteam](https://github.com/iTaysonLab/jetisteam) | Unofficial Steam mobile client | 125 | 🟢 | Kotlin |
| [node-epicgames-client](https://github.com/SzymonLisowiec/node-epicgames-client) | Unofficial Epic Games Launcher client in JavaScript (login, friends, party, chat) | 112 | 🔴 | JavaScript |
| [wyvern](https://github.com/nicohman/wyvern) | Simple CLI client for installing and maintaining Linux GOG games | 100 | 🔴 | Rust |
| [steam-store](https://github.com/autarc/steam-store) | Client for the unofficial Steam storefront and Big Picture web API | 35 | 🔴 | JavaScript |

## Matching Decompilations — Arcade

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [namco22-decompile](https://github.com/spacestate1/namco22-decompile) | Decompilation of Namco System 22 arcade games | 253 | 🟢 | C |
| [Sonic the Fighters](https://github.com/biggestsonicfan/stfdecomp) | Matching decompilation of Sonic the Fighters (Sega Model 2 arcade, 1996) | 110 | 🟢 | Assembly |
| [Time Crisis (Time Crisis VR)](https://github.com/DR-89/time-crisis-vr) | Decompilation of Time Crisis (Arcade) | 82 | 🟢 | C |
| [Asteroids arcade game firmware disassembly](https://github.com/nmikstas/asteroids-disassembly) | Disassembly of the Asteroids arcade game firmware | 55 | 🔴 | Assembly |
| [stfdisasm](https://github.com/biggestsonicfan/stfdisasm) | Sonic the Fighters Disassembly | 49 | 🟢 | Assembly |
| [Donkey Kong hacking kit](https://github.com/furrykef/dkdasm) | Disassembly and hacking kit for Donkey Kong (arcade) | 46 | 🔴 | Assembly |
| [1983 Sinistar arcade game decomp](https://github.com/synamaxmusic/sinistar) | Source code reconstruction of the 1983 Sinistar arcade game | 45 | 🟢 | Assembly |
| [Street Fighter III: 3rd Strike decomp](https://github.com/gibletto/sfIII3-cps3-decomp) | Byte-matched decompilation of Street Fighter III: 3rd Strike (CPS3 arcade) | 18 | 🟢 | C |
| [Jackal (UEFI_Jackal)](https://github.com/MikeWuPing/UEFI_Jackal) | Decompilation of Jackal (Arcade) | 16 | 🟢 | C |
| [mslug-disasm](https://github.com/neogeodev/mslug-disasm) | Disassembly and analysis of Metal Slug (Neo Geo) | 13 | 🔴 | Assembly |
| [ARCADE! (Galaga)](https://github.com/neiderm/arcade) | Commented disassembly of the Galaga arcade game with a C translation | 11 | 🟢 | C |
| [Defender-Source-Code](https://github.com/AaronBottegal/Defender-Source-Code) | Defender arcade game code reverse engineered back into source | 11 | 🔴 |  |
| [Major Havoc arcade game disassembly](https://github.com/historicalsource/major-havoc-dasm) | Disassembly of the Major Havoc arcade game (Atari) | 9 | 🔴 | Assembly |
| [Riptide](https://github.com/solarfren69420/Riptide) | Rust decompilation port of Hydro Thunder and H2Overdrive | 7 | 🟢 | Rust |
| [star-wars-arcade-audio](https://github.com/nmikstas/star-wars-arcade-audio) | Disassembled audio firmware of the Star Wars arcade game (Atari, 1983) | 7 | 🔴 | Assembly |
| [Commando arcade game disassembly](https://github.com/mikeybabes/commando) | Annotated disassembly of the Commando arcade game | 6 | 🟡 | Assembly |
| [Galaxian arcade game disassembly](https://github.com/ScottTunstall/Galaxian) | Annotated disassembly of the Galaxian arcade game | 4 | 🟡 | Assembly |
| [SegaSonic the Hedgehog decomp](https://github.com/cheviman/segasonic-decomp) | Decompilation of SegaSonic the Hedgehog (Sega System 32 arcade, 1993) | 4 | 🟢 | C |
| [F-Zero AX](https://github.com/TheInfiniteLegend/f-0-ax) | Matching decompilation of F-Zero AX (Triforce arcade, 2003) | 3 | 🟡 | C |
| [Gorf disassembly](https://github.com/astrocadester/Gorf) | Disassembly of Gorf (Bally Astrocade) | 3 | 🟢 | Assembly |
| [Robotron: 2084 arcade game disassembly](https://github.com/ScottTunstall/Robotron2084) | Annotated disassembly of the Robotron: 2084 arcade game | 3 | 🟡 | Assembly |
| [a 2000s arcade rhythm game decomp](https://github.com/Roganis/2EZDecomp) | Matching decompilation of a 2000s arcade rhythm game (EZ2DJ) | 2 | 🟢 | C++ |
| [Mario Kart Arcade GP 2 main.dol decomp](https://github.com/naari3/mkgp2-decomp) | Matching decompilation of Mario Kart Arcade GP 2 main.dol (Triforce arcade) | 2 | 🟢 | C |
| [stf-sharc](https://github.com/biggestsonicfan/stf-sharc) | Disassembled SHARC code of the Sonic the Fighters arcade game | 2 | 🟢 | Assembly |
| [Altered Beast arcade game disassembly](https://github.com/mikeybabes/alteredbeast) | Disassembly of the Altered Beast arcade game | 1 | 🟡 | Assembly |
| [Battlezone disassembly](https://github.com/tcottrill/BattleZone-Full-Disassembly-and-C-Port) | Byte-exact disassembly and C port of Battlezone (Atari arcade, 1980) | 1 | 🟢 | C |
| [Bubble Bobble arcade PS4 microcontroller code disassembly](https://github.com/luxocrates/bubbleBobblePs4Disasm) | Disassembly of the Bubble Bobble arcade PS4 microcontroller code | 1 | 🟡 | Assembly |
| [Hydro Thunder decomp](https://github.com/b3dllc/hydrothunder) | Decompilation of Hydro Thunder (1999) | 1 | 🟢 | C |
| [Lunar Lander arcade game disassembly](https://github.com/tcottrill/Lunar-Lander-Full-Disassembly-and-C-Port) | Full disassembly and C port of the Lunar Lander arcade game (Atari, 1979) | 1 | 🟢 | C |
| [Marvel vs. Capcom 2 decomp](https://github.com/g-guthrie/mvc2-naomi-decomp) | Decompilation of Marvel vs. Capcom 2 (Sega NAOMI arcade) | 1 | 🟢 | C |
| [Mega Play arcade version of Sonic the Hedgehog disassembly](https://github.com/Iso-Kilo/Sonic-1-Mega-Play-Disassembly) | 68K disassembly of the Mega Play arcade version of Sonic the Hedgehog | 1 | 🔴 |  |
| [Namco's Dig Dug arcade game decomp](https://github.com/Suspence00/digdug-decomp) | Clean-room Rust decompilation of Namco's Dig Dug arcade game (1982) | 1 | 🟢 | Rust |
| [Omega Race disassembly](https://github.com/tcottrill/Omega-Race-Full-Disassembly-and-C-Port) | Annotated disassembly and C port of Omega Race (Midway arcade, 1981) | 1 | 🟢 | C |
| [Punch-Out!! arcade game disassembly](https://github.com/DeathEngine2/punchout-arcade-disasm) | Disassembly of the Punch-Out!! arcade game (1984) | 1 | 🔴 | Assembly |
| [Rhythm Tengoku decomp](https://github.com/Toritan123/rhytngk-arcade-decomp) | Experimental decompilation of Rhythm Tengoku (arcade) | 1 | 🟢 | Assembly |
| [Space Invaders arcade game into native C decomp](https://github.com/ArnoKalavent/Space-Invaders-Decomp) | Recompilation of the Space Invaders arcade game into native C | 1 | 🟢 | C++ |
| [Splatterhouse decomp](https://github.com/indieindie7/splatterhouse-decomp) | Function maps and decompilation of Splatterhouse (arcade) and its Genesis sequels | 1 | 🟢 | Python |
| [Star Wars arcade game disassembly](https://github.com/tcottrill/Star-Wars-Full-Disassembly-and-C-Port) | Full disassembly and C port of the Star Wars arcade game (Atari, 1983) | 1 | 🟢 | C |
| [Street Fighter III: 2nd Impact decomp](https://github.com/gibletto/sfIII2-cps3-decomp) | Byte-matching decompilation of Street Fighter III: 2nd Impact (CPS3 arcade) | 1 | 🟢 | C |
| [Super Street Fighter II Turbo decomp](https://github.com/nikodindon/ssf2t-decomp) | Decompilation of Super Street Fighter II Turbo | 1 | 🟢 | Python |
| [Tempest disassembly](https://github.com/tcottrill/Tempest-Full-Disassembly-and-C-Port) | Full disassembly and C port of Tempest (Atari arcade, 1981) | 1 | 🟢 | C |
| [The Empire Strikes Back arcade game disassembly](https://github.com/tcottrill/Empire-Strikes-Back-Full-Disassembly-and-Slapstic-Removal) | Commented 6809 disassembly of The Empire Strikes Back arcade game (Atari, 1985) | 1 | 🟢 | C |
| [Asteroids Deluxe disassembly](https://github.com/tcottrill/Asteroids-Deluxe-Full-Disassembly-and-C-Port) | Full disassembly and C port of Asteroids Deluxe (Atari arcade, 1981) | 0 | 🟢 | C |
| [Berzerk arcade game disassembly](https://github.com/ScottTunstall/Berzerk) | Annotated disassembly of the Berzerk arcade game | 0 | 🟢 | Assembly |
| [Clowns disassembly](https://github.com/tcottrill/Midway-Clowns-Full-Disassembly-and-C-Port) | Annotated disassembly and C port of Clowns (Midway arcade, 1978) | 0 | 🟢 | C |
| [dk](https://gitlab.com/segaloco/dk) | Comprehensive disassembly of arcade Donkey Kong |  | ⚪ |  |
| [Gravitar disassembly](https://github.com/tcottrill/Gravitar-Full-Disassembly-and-C-Port) | Full disassembly and C port of Gravitar (Atari arcade, 1982) | 0 | 🟢 | C |
| [Jungle King arcade game disassembly](https://github.com/YellowTodd/jungle_king) | Disassembly of the Jungle King arcade game | 0 | 🟢 | Assembly |
| [mb](https://gitlab.com/segaloco/mb) | Comprehensive disassembly of arcade Mario Bros. |  | ⚪ |  |
| [Neo Turf Masters decomp](https://github.com/blakebratcher/ntm-decomp) | Byte-exact decompilation research for Neo Turf Masters (Neo Geo) | 0 | 🟢 | Python |
| [November 1982 pre-release version of Sinistar decomp](https://github.com/synamaxmusic/sinistar-amoa) | Reconstructed source of the November 1982 pre-release version of Sinistar (arcade) | 0 | 🟡 | Assembly |
| [Rampage arcade game disassembly](https://github.com/mikeybabes/Rampage) | Semi-annotated disassembly of the Rampage arcade game | 0 | 🟡 | Python |
| [sound ROM of Blaster disassembly](https://github.com/synamaxmusic/Blaster-Sound-ROM) | Disassembly of the sound ROM of Blaster (Williams arcade, 1983) | 0 | 🟢 | Assembly |
| [sound ROM of Inferno disassembly](https://github.com/synamaxmusic/Inferno-Sound-Rom) | Disassembly of the sound ROM of Inferno (Williams arcade, 1984) | 0 | 🔴 | Assembly |
| [sound ROM of Mystic Marathon disassembly](https://github.com/synamaxmusic/mystic-marathon-sound-rom) | Disassembly of the sound ROM of Mystic Marathon (Williams arcade, 1984) | 0 | 🔴 |  |
| [Space Duel disassembly](https://github.com/tcottrill/Space-Duel-Full-Disassembly-and-C-Port) | Full disassembly and C port of Space Duel (Atari arcade, 1982) | 0 | 🟢 | C |
| [Tetris: The Absolute The Grand Master 2 PLUS decomp](https://github.com/masonc15/tgm2p-decomp) | Matching decompilation of Tetris: The Absolute The Grand Master 2 PLUS (Psikyo arcade) | 0 | 🟢 | C |
| [Warlords disassembly](https://github.com/tcottrill/Warlords-Full-Disassembly) | Annotated disassembly of Warlords (Atari arcade, 1980) | 0 | 🟢 | HTML |

## Matching Decompilations — Atari

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [StarRaiders](https://github.com/lwiest/StarRaiders) | Reverse-engineered, fully documented 6502 source of Star Raiders | 183 | 🟡 |  |
| [Raiders2600](https://github.com/halkuncode/Raiders2600) | Reverse-engineered, commented source of Raiders of the Lost Ark for Atari 2600 | 176 | 🟢 | Assembly |
| [a26_mb](https://gitlab.com/segaloco/a26_mb) | Comprehensive disassembly of Mario Bros. for the Atari 2600 |  | ⚪ |  |

## Matching Decompilations — Game Boy / GBA / DS

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [pokered](https://github.com/pret/pokered) | Disassembly of Pokemon Red/Blue | 5,009 | 🟢 | Assembly |
| [pokeemerald](https://github.com/pret/pokeemerald) | Decompilation of Pokemon Emerald | 3,640 | 🟢 | C |
| [pokecrystal](https://github.com/pret/pokecrystal) | Disassembly of Pokemon Crystal | 2,540 | 🟢 | Assembly |
| [Pokémon FireRed/LeafGreen](https://github.com/pret/pokefirered) | Matching decompilation of Pokémon FireRed/LeafGreen (Game Boy Advance, 2004) | 1,687 | 🟢 | C |
| [Pokémon Ruby/Sapphire](https://github.com/pret/pokeruby) | Matching decompilation of Pokémon Ruby/Sapphire (Game Boy Advance, 2002) | 1,007 | 🟢 | C |
| [The Legend of Zelda: The Minish Cap](https://github.com/zeldaret/tmc) | Matching decompilation of The Legend of Zelda: The Minish Cap (Game Boy Advance, 2004) | 930 | 🟢 | C |
| [LADX-Disassembly](https://github.com/zladx/LADX-Disassembly) | Disassembly of The Legend of Zelda: Link's Awakening DX | 918 | 🟢 | Assembly |
| [Pokémon Yellow](https://github.com/pret/pokeyellow) | Disassembly of Pokémon Yellow (Game Boy, 1998) | 898 | 🟢 | Assembly |
| [Pokémon HeartGold/SoulSilver](https://github.com/pret/pokeheartgold) | Matching decompilation of Pokémon HeartGold/SoulSilver (Nintendo DS, 2009) | 740 | 🟢 | Assembly |
| [Pokémon Gold/Silver](https://github.com/pret/pokegold) | Disassembly of Pokémon Gold/Silver (Game Boy Color, 1999) | 732 | 🟢 | Assembly |
| [sa2](https://github.com/SAT-R/sa2) | Decompilation and port of Sonic Advance 1 & 2 (GBA) | 686 | 🟢 | C |
| [pokeplatinum](https://github.com/pret/pokeplatinum) | Decompilation of Pokemon Platinum | 586 | 🟢 | C |
| [Pokémon Diamond/Pearl](https://github.com/pret/pokediamond) | Matching decompilation of Pokémon Diamond/Pearl (Nintendo DS, 2006) | 544 | 🟢 | Assembly |
| [Pokémon Gold (SpaceWorld Demo)](https://github.com/pret/pokegold-spaceworld) | Disassembly of Pokémon Gold and Silver (Game Boy, 1997; Space World 1997 demo) | 403 | 🟢 | Assembly |
| [Pokémon TCG](https://github.com/pret/poketcg) | Disassembly of Pokémon Trading Card Game (Game Boy Color, 1998) | 333 | 🟢 | Assembly |
| [Pokémon Mystery Dungeon: Red Rescue Team](https://github.com/pret/pmd-red) | Matching decompilation of Pokémon Mystery Dungeon: Red Rescue Team (Game Boy Advance, 2005) | 290 | 🟢 | C |
| [Fire Emblem: The Sacred Stones (FEU)](https://github.com/FireEmblemUniverse/fireemblem8u) | Matching decompilation of Fire Emblem: The Sacred Stones (Game Boy Advance, 2004) | 229 | 🟢 | Assembly |
| [sm64ds-decomp](https://github.com/tangosdev/sm64ds-decomp) | Byte-matching decompilation of Super Mario 64 DS | 224 | 🟢 | C++ |
| [oracles-disasm](https://github.com/Stewmath/oracles-disasm) | Disassembly of Zelda: Oracle of Ages and Seasons | 221 | 🟢 | Assembly |
| [Pokémon Pinball](https://github.com/pret/pokepinball) | Disassembly of Pokémon Pinball (Game Boy Color, 1999) | 204 | 🟢 | Assembly |
| [Golden Sun](https://github.com/PascalPixel/alchemy) | Matching decompilation of Golden Sun (Game Boy Advance, 2001) | 174 | 🟢 | C |
| [Kirby & The Amazing Mirror](https://github.com/jiangzhengwenjz/katam) | Matching decompilation of Kirby & The Amazing Mirror (Game Boy Advance, 2004) | 160 | 🟢 | C |
| [Metroid: Zero Mission](https://github.com/metroidret/mzm) | Matching decompilation of Metroid: Zero Mission (Game Boy Advance, 2004) | 158 | 🟢 | C |
| [Pokémon Pinball Ruby & Sapphire](https://github.com/pret/pokepinballrs) | Matching decompilation of Pokémon Pinball Ruby & Sapphire (Game Boy Advance, 2003) | 149 | 🟢 | Assembly |
| [Pokémon Mystery Dungeon: Explorers of Sky](https://github.com/pret/pmd-sky) | Matching decompilation of Pokémon Mystery Dungeon: Explorers of Sky (Nintendo DS, 2009) | 148 | 🟢 | Assembly |
| [Pokémon Emerald](https://github.com/Pokabbie/pokeemerald-rogue) | Decompilation of Pokémon Emerald (GBA) | 143 | 🟢 | C |
| [Pokémon Platinum disassembly](https://github.com/JimB16/PokePlat) | Disassembly of Pokémon Platinum (Nintendo DS) | 116 | 🔴 | Assembly |
| [The Legend of Zelda: Phantom Hourglass](https://github.com/zeldaret/ph) | Matching decompilation of The Legend of Zelda: Phantom Hourglass (Nintendo DS, 2007) | 116 | 🟢 | C++ |
| [Pokémon Snap](https://github.com/ethteck/pokemonsnap) | Decompilation of Pokémon Snap | 112 | 🟢 | C |
| [Super Mario 3D Land](https://github.com/3dsdecomp/RedPepper) | Matching decompilation of Super Mario 3D Land (Nintendo 3DS, 2011) | 112 | 🟡 | C++ |
| [Telefang disassembly](https://github.com/telefang/telefang) | Partial disassembly of Telefang (Game Boy Color) with an English translation patch | 103 | 🟢 | Assembly |
| [Kingdom Hearts 358/2 Days](https://github.com/Yokimitsuro/khdays-decomp) | Matching decompilation of Kingdom Hearts 358/2 Days (Nintendo DS, 2009) | 100 | 🟢 | C |
| [Pokémon TCG 2](https://github.com/pret/poketcg2) | Disassembly of Pokémon Card GB2 (Game Boy Color, 2001) | 96 | 🟢 | Assembly |
| [Mother 3 decomp](https://github.com/Kurausukun/mother3) | Decompilation of Mother 3 (GBA) | 90 | 🟢 | Assembly |
| [The Legend of Zelda: Ocarina of Time 3D](https://github.com/zeldaret/oot3d) | Matching decompilation of The Legend of Zelda: Ocarina of Time 3D (Nintendo 3DS, 2011) | 90 | 🟢 | C++ |
| [Sonic Advance 3](https://github.com/SAT-R/sa3) | Matching decompilation of Sonic Advance 3 (Game Boy Advance, 2004) | 88 | 🟢 | C |
| [Tetris disassembly](https://github.com/osnr/tetris) | Disassembly of Tetris (Game Boy) | 85 | 🔴 | Assembly |
| [Pokémon Puzzle Challenge](https://github.com/pret/pokepuzzle) | Disassembly of Pokémon Puzzle Challenge | 81 | 🟢 | Assembly |
| [Sonic Advance](https://github.com/SAT-R/sa1) | Matching decompilation of Sonic Advance (Game Boy Advance, 2001) | 77 | 🗄️ | C |
| [Metroid Fusion](https://github.com/metroidret/mf) | Matching decompilation of Metroid Fusion (Game Boy Advance, 2002) | 76 | 🟢 | C |
| [The Legend of Zelda: Spirit Tracks](https://github.com/zeldaret/st) | Matching decompilation of The Legend of Zelda: Spirit Tracks (Nintendo DS, 2009) | 72 | 🟢 | C++ |
| [Pokémon Red and Blue (pokemon-claude-red)](https://github.com/levy-street/pokemon-claude-red) | Decompilation of Pokémon Red and Blue (Game Boy) | 70 | 🟢 | JavaScript |
| [Super Mario Land disassembly](https://github.com/kaspermeerts/supermarioland) | Disassembly of Super Mario Land (Game Boy) | 70 | 🔴 | Assembly |
| [New Super Mario Bros.](https://github.com/NSMB-Decomp/nsmb) | Matching decompilation of New Super Mario Bros. (Nintendo DS, 2006) | 69 | 🟢 | C++ |
| [Pokémon Emerald (JP)](https://github.com/pret/pokeemerald-jp) | Matching decompilation of Pokémon Emerald (Game Boy Advance, 2004; Japanese version) | 69 | 🔴 | Assembly |
| [Pokémon Black](https://github.com/squiddonaut/pokeblack) | Matching decompilation of Pokémon Black (Nintendo DS, 2010) | 66 | 🟢 | Assembly |
| [Mario Kart DS](https://github.com/XorTroll/mkds-re) | Decompilation of Mario Kart DS | 64 | 🟡 | C |
| [Kingdom Hearts: Chain of Memories](https://github.com/MatyMeatBoy/ReKHCoM) | Decompilation of Kingdom Hearts: Chain of Memories (GBA) | 63 | 🟢 | C |
| [Pokémon Black 2 and White 2](https://github.com/fuddlesworth/pokebw2) | Matching decompilation of Pokémon Black 2 and White 2 (Nintendo DS, 2012) | 57 | 🟢 | C |
| [Kingdom Hearts: Chain of Memories](https://github.com/Pheenoh/khcom) | Matching decompilation of Kingdom Hearts: Chain of Memories (Game Boy Advance, 2004) | 56 | 🟢 | C |
| [Phoenix Wright: Ace Attorney](https://github.com/atasro2/pwaa1) | Matching decompilation of Phoenix Wright: Ace Attorney (Game Boy Advance, 2001; Japanese Gyakuten Saiban) | 56 | 🟢 | C |
| [Kirby's Dream Land disassembly](https://github.com/huderlem/kirbydreamland) | Disassembly of Kirby's Dream Land (Game Boy) | 54 | 🔴 | Assembly |
| [The Legend of Zelda: A Link to the Past & Four Swords disassembly](https://github.com/camthesaxman/zeldaalttp) | Disassembly of The Legend of Zelda: A Link to the Past & Four Swords (GBA) | 54 | 🔴 | Assembly |
| [Dragon Quest IX](https://github.com/DQIX/dqix-decomp) | Matching decompilation of Dragon Quest IX: Sentinels of the Starry Skies (Nintendo DS, 2009) | 53 | 🟢 | C++ |
| [Tetris disassembly](https://github.com/alexsteb/tetris_disassembly) | Disassembly of Tetris (Game Boy) | 52 | 🟡 | Assembly |
| [Rhythm Heaven (DS)](https://github.com/patataofcourse/rhgold) | Decompilation of Rhythm Heaven (DS) | 51 | 🟢 | C |
| [MH4UltimateDC](https://github.com/CompaLarios18/MH4UltimateDC) | Decompilation of Monster Hunter 4 Ultimate (3DS) | 50 | 🟢 | Python |
| [medarot1](https://github.com/Medabots/medarot1) | Disassembly and English translation of Medarot (Game Boy) | 49 | 🟢 | Assembly |
| [medarot3](https://github.com/Medabots/medarot3) | Disassembly and translation of Medarot 3 (Game Boy Color) | 49 | 🟢 | Assembly |
| [Super Mario Land 3: Wario Land disassembly](https://github.com/Kak2X/wl) | Disassembly of Super Mario Land 3: Wario Land (Game Boy) | 48 | 🟢 | Assembly |
| [hmfomt](https://github.com/not-alons/hmfomt) | Disassembly/decompilation of Harvest Moon: Friends of Mineral Town | 47 | 🔴 | Assembly |
| [Mega Man Zero 3](https://github.com/mmzret/rmz3) | Matching decompilation of Mega Man Zero 3 (Game Boy Advance, 2004) | 47 | 🟢 | Assembly |
| [Fire Emblem: The Binding Blade decomp](https://github.com/StanHash/fe6) | Decompilation of Fire Emblem: The Binding Blade (GBA) | 46 | 🟢 | C |
| [Sonic Rush Adventure](https://github.com/RushRE/SonicRushAdventure-Decomp) | Matching decompilation of Sonic Rush Adventure (Nintendo DS, 2007) | 46 | 🟢 | C |
| [Banjo-Kazooie: Grunty's Revenge](https://github.com/jellees/bkgr) | Matching decompilation of Banjo-Kazooie: Grunty's Revenge (Game Boy Advance, 2003) | 45 | 🟢 | Assembly |
| [bn6f](https://github.com/dism-exe/bn6f) | Disassembly of MegaMan Battle Network 6 Cybeast Falzar | 44 | 🟢 | Assembly |
| [Harvest Moon: Friends of Mineral Town](https://github.com/StanHash/fomt) | Matching decompilation of Harvest Moon: Friends of Mineral Town (Game Boy Advance, 2003) | 44 | 🟢 | Assembly |
| [pokeheartgold-single-screen](https://github.com/ClickingMaster/pokeheartgold-single-screen) | Single-screen build of the Pokémon HeartGold/SoulSilver decompilation (DS) | 42 | 🟢 | C |
| [pokemonstadium](https://github.com/ethteck/pokemonstadium) | Decompilation of Pokemon Stadium | 41 | 🔴 | Assembly |
| [berry-fix](https://github.com/pret/berry-fix) | Decompilation of the Berry Fix Program in Pokemon Emerald and FireRed/LeafGreen | 39 | 🔴 | C |
| [Mario & Luigi: Superstar Saga](https://github.com/jellees/mlss) | Matching decompilation of Mario & Luigi: Superstar Saga (Game Boy Advance, 2003) | 38 | 🟢 | Assembly |
| [Fire Emblem: The Blazing Blade (JP)](https://github.com/MokhaLeee/FireEmblem7J) | Matching decompilation of Fire Emblem: Rekka no Ken (Game Boy Advance, 2003; Japanese Blazing Blade) | 37 | 🟢 | Assembly |
| [Pokémon FireRed disassembly](https://github.com/shinyquagsire23/DisFire) | Compilable disassembly of Pokémon FireRed (GBA) | 37 | 🔴 | Assembly |
| [Sakura Wars GB disassembly](https://github.com/vinheim3/sakuraWars1-disasm) | Disassembly of Sakura Wars GB with an English translation (Game Boy Color) | 36 | 🔴 | Assembly |
| [Golden Sun disassembly](https://github.com/gsret/goldensun) | Disassembly of Golden Sun (GBA) | 35 | 🟡 | Assembly |
| [Mario Kart: Super Circuit](https://github.com/jellees/mksc) | Matching decompilation of Mario Kart: Super Circuit (Game Boy Advance, 2001) | 35 | 🟡 | Assembly |
| [Castlevania: Order of Ecclesia](https://github.com/LagoLunatic/ooe) | Matching decompilation of Castlevania: Order of Ecclesia (Nintendo DS, 2008) | 34 | 🟡 | C |
| [colosseum-mb](https://github.com/pret/colosseum-mb) | Decompilation of the GBA multiboot for Pokemon Colosseum | 34 | 🟡 | C++ |
| [The World Ends With You](https://github.com/Yotona/twewy) | Matching decompilation of The World Ends With You (Nintendo DS, 2007) | 33 | 🟢 | C |
| [Metroid II: Return of Samus disassembly](https://github.com/metroidret/M2RoS) | Disassembly of Metroid II: Return of Samus (Game Boy) | 32 | 🟢 | Assembly |
| [mksc-decompilation](https://github.com/XOlifreX/mksc-decompilation) | Decompilation of Mario Kart Super Circuit (GBA) | 32 | 🔴 | Assembly |
| [tetris-gb-disasm](https://github.com/vinheim3/tetris-gb-disasm) | Complete disassembly of the Game Boy Tetris ROM | 32 | 🔴 | Assembly |
| [DS Protect](https://github.com/taxicat1/dsprot) | Decompilation of DS Protect (DS) | 31 | 🟢 | C |
| [NSMB-Code-Reference](https://github.com/MammaMiaTeam/NSMB-Code-Reference) | Public code reference for patching New Super Mario Bros. DS (US) | 31 | 🟢 | C++ |
| [Golden Sun: The Broken Seal](https://github.com/Coaltergeist/goldensun-decomp) | Matching decompilation of Golden Sun: The Broken Seal (Game Boy Advance, 2001) | 30 | 🟢 | Assembly |
| [Mother 1+2](https://github.com/Normmatt/m12) | Matching decompilation of Mother 1+2 (Game Boy Advance, 2003) | 30 | 🟢 | C |
| [Castlevania: Aria of Sorrow](https://github.com/testyourmine/cvaos) | Matching decompilation of Castlevania: Aria of Sorrow (Game Boy Advance, 2003) | 29 | 🟢 | Assembly |
| [The Legend of Zelda: The Minish Cap decomp](https://github.com/HayatoG/tmc) | Decompilation of The Legend of Zelda: The Minish Cap (GBA) | 29 | 🟢 | C |
| [Donkey Kong '94](https://github.com/CelestialAmber/DKGBDisasm) | Disassembly of Donkey Kong (Game Boy, 1994) | 28 | 🔴 | Assembly |
| [Pokémon Red/Green disassembly](https://github.com/Narishma-gb/pokegreen) | Disassembly of Pokémon Red/Green (Game Boy, Japan) | 28 | 🟢 | Assembly |
| [Reverse-Engineering-the-GameBoy-Tetris](https://github.com/h3nnn4n/Reverse-Engineering-the-GameBoy-Tetris) | Reverse engineering of the Game Boy Tetris ROM | 27 | 🔴 | Shell |
| [Mario Party DS](https://github.com/mariopartyrd/mariopartyDS) | Decompilation of Mario Party DS | 26 | 🟡 | Python |
| [Pokémon Version Rouge disassembly](https://github.com/einstein95/pokered-fr) | Disassembly of Pokémon Version Rouge (Game Boy, French) | 25 | 🟢 | Assembly |
| [totkol](https://github.com/jiangzhengwenjz/totkol) | Decompilation of Tactics Ogre: The Knight of Lodis (USA) | 25 | 🟡 | Assembly |
| [Monster Hunter 4 Ultimate](https://github.com/mhvuze/mh4u-decomp) | Matching decompilation of Monster Hunter 4 Ultimate (Nintendo 3DS, 2014) | 24 | 🟢 |  |
| [Pokémon Crystal disassembly](https://github.com/PikalaxALT/pokekuristaru) | Disassembly of Pokémon Crystal (Game Boy Color, Japan) | 24 | 🔴 | Assembly |
| [ZoidsLegacyDecomp](https://github.com/jmacato/ZoidsLegacyDecomp) | Matched decompilation of Zoids Legacy (GBA) | 23 | 🟢 | C |
| [Final Fantasy Adventure disassembly](https://github.com/daid/FFA-Disassembly) | Disassembly of Final Fantasy Adventure (Game Boy) | 22 | 🟢 | Assembly |
| [pokemoon](https://github.com/gradenGnostic/pokemoon) | Decompilation of Pokemon Moon | 22 | 🟢 | C++ |
| [Hamtaro: Ham-Hams Unite! disassembly](https://github.com/obskyr/hamtaro-in-pieces) | Disassembly of Hamtaro: Ham-Hams Unite! (Game Boy Color) | 21 | 🔴 | Crystal |
| [Harry Potter and the Sorcerer's Stone (HPSS-Disassembly)](https://github.com/terinjokes/HPSS-Disassembly) | Disassembly of Harry Potter and the Sorcerer's Stone (Game Boy Color) | 21 | 🟡 | Assembly |
| [Mario vs. Donkey Kong](https://github.com/camthesaxman/mariovsdk) | Disassembly of Mario vs. Donkey Kong | 21 | 🟡 | Assembly |
| [Wario Land 3 disassembly](https://github.com/froggestspirit/wland3) | Disassembly of Wario Land 3 (Game Boy Color) | 21 | 🗄️ | Assembly |
| [Wario Land 4](https://github.com/TsilaAllaoui/warioland4) | Matching decompilation of Wario Land 4 (Game Boy Advance, 2001) | 21 | 🟢 | C |
| [Crash Bandicoot XS / The Huge Adventure decomp](https://github.com/Almamu/CrashBandicootXS-decomp) | Decompilation of Crash Bandicoot XS / The Huge Adventure (GBA) | 20 | 🟢 | Assembly |
| [Fire Emblem: The Sacred Stones](https://github.com/laqieer/fireemblem8u) | Matching decompilation of Fire Emblem: The Sacred Stones (Game Boy Advance, 2004) | 20 | 🗄️ | Assembly |
| [Metroid II: Return of Samus decomp](https://github.com/Vashy777/metroid2) | Decompilation of Metroid II: Return of Samus (Game Boy) | 20 | 🔴 | Assembly |
| [hm3](https://github.com/Sanqui/hm3) | Partial disassembly of Harvest Moon 3 for Game Boy Color | 19 | 🔴 | Assembly |
| [Japanese Pokémon Red disassembly](https://github.com/luckytyphlosion/pokered-jp) | Disassembly of the Japanese Pokémon Red (Game Boy) | 19 | 🔴 | Assembly |
| [Kingdom Hearts 358/2 Days (khdays-vita)](https://github.com/ggdrn/KH-DAYS-VITA) | Decompilation of Kingdom Hearts 358/2 Days (DS) | 19 | 🟢 | C |
| [Klonoa: Empire of Dreams](https://github.com/testyourmine/kleod) | Matching decompilation of Klonoa: Empire of Dreams (Game Boy Advance, 2001) | 19 | 🟢 | C |
| [Star Ocean: Blue Sphere](https://github.com/animaone/star-ocean-blue-sphere-source-code) | Source code of Star Ocean: Blue Sphere (Game Boy Color, 2001) | 19 | 🟡 | Assembly |
| [Breath of Fire disassembly](https://github.com/Normmatt/bof) | Disassembly of Breath of Fire (GBA) | 18 | 🔴 | Assembly |
| [Fire Emblem disassembly](https://github.com/StanHash/fe7_us) | Disassembly and partial decompilation of Fire Emblem (GBA, US) | 18 | 🟡 | Assembly |
| [Inazuma Eleven 3: The Ogre](https://github.com/CacaBueno64/ie3ogres) | Matching decompilation of Inazuma Eleven 3: The Ogre (Nintendo DS, 2011) | 18 | 🟢 | Assembly |
| [Kirby: Nightmare in Dream Land](https://github.com/overjt/knidl) | Matching decompilation of Kirby: Nightmare in Dream Land (Game Boy Advance, 2002) | 18 | 🟢 | C |
| [Mega Man: Dr. Wily's Revenge disassembly](https://github.com/iimarckus/megaman) | Disassembly of Mega Man: Dr. Wily's Revenge (Game Boy) | 18 | 🔴 | Assembly |
| [Phoenix Wright: Ace Attorney – Justice for All](https://github.com/atasro2/pwaa2) | Matching decompilation of Phoenix Wright: Ace Attorney – Justice for All (Game Boy Advance, 2002; Japanese Gyakuten Saiban 2) | 18 | 🟢 | Assembly |
| [Rockman EXE 6 Dennoujuu Falzer disassembly](https://github.com/dism-exe/exe6f) | Disassembly of Rockman EXE 6 Dennoujuu Falzer (GBA, Japan) | 18 | 🔴 | C++ |
| [Summon Night: Craft Sword Monogatari](https://github.com/jiangzhengwenjz/csm3) | Matching decompilation of Summon Night: Craft Sword Monogatari (Game Boy Advance, 2003) | 18 | 🟡 | Assembly |
| [Super Mario Advance 2: Super Mario World disassembly](https://github.com/atasro2/sma2) | Disassembly of Super Mario Advance 2: Super Mario World (GBA) | 18 | 🔴 | Assembly |
| [Tetris decomp](https://github.com/Normmatt/agbtetris) | Decompilation and GBA port of Tetris (Game Boy, 1989) | 18 | 🔴 | C |
| [Fire Emblem: Shadow Dragon](https://github.com/Eebit/fe11-us) | Matching decompilation of Fire Emblem: Shadow Dragon (Nintendo DS, 2008) | 17 | 🟢 | C++ |
| [Klonoa: Empire of Dreams](https://github.com/Dream-Atelier/kl-eod-decomp) | Matching decompilation of Klonoa: Empire of Dreams (Game Boy Advance, 2001) | 17 | 🟢 | C |
| [Kingdom Hearts: Chain of Memories (KH_COM_VITA)](https://github.com/ggdrn/KH_COM_VITA) | Decompilation of Kingdom Hearts: Chain of Memories (GBA) | 16 | 🟢 | C |
| [Mario & Luigi: Superstar Saga disassembly](https://github.com/nstearns96/MLSuperstarSaga) | Disassembly of Mario & Luigi: Superstar Saga (GBA) | 16 | 🔴 | Assembly |
| [medarot4](https://github.com/Medabots/medarot4) | Disassembly and translation of Medarot 4 (Game Boy Color) | 16 | 🟡 | Assembly |
| [Super Mario Land 2: 6 Golden Coins disassembly](https://github.com/froggestspirit/marioland2) | Disassembly of Super Mario Land 2: 6 Golden Coins (Game Boy) | 16 | 🗄️ | Assembly |
| [Tetris disassembly](https://github.com/meithecatte/gbtetris) | Compilable labeled disassembly of Tetris (Game Boy) | 16 | 🔴 | Assembly |
| [Advance Wars 2: Black Hole Rising](https://github.com/Eebit/aw2bhr) | Matching decompilation of Advance Wars 2: Black Hole Rising (Game Boy Advance, 2003) | 15 | 🟡 | Assembly |
| [Animal Crossing: Wild World decomp](https://github.com/7ucina/acww-decomp) | Matching decompilation of Animal Crossing: Wild World (Nintendo DS, USA) | 15 | 🟢 | C++ |
| [Dragon Quest IV](https://github.com/GoldieLeGenie/DQIV-DECOMP) | Matching decompilation of Dragon Quest IV (Nintendo DS, 2007) | 15 | 🟢 | C++ |
| [Kingdom Hearts Re:coded](https://github.com/kh-recoded-decomp/kh-recoded-decomp) | Matching decompilation of Kingdom Hearts Re:coded (Nintendo DS, 2010) | 15 | 🟢 | C |
| [Kingdom Hearts Re:coded decomp](https://github.com/Yokimitsuro/khrecoded-decomp) | Matching decompilation of Kingdom Hearts Re:coded (Nintendo DS) | 15 | 🟢 | C |
| [Looney Tunes: Carrot Crazy disassembly](https://github.com/huderlem/carrotcrazy) | Disassembly of Looney Tunes: Carrot Crazy (Game Boy Color) | 15 | 🟢 | Assembly |
| [Super Mario Advance 4: Super Mario Bros. 3 disassembly](https://github.com/KarisaAdvynia/sma4-disasm) | Disassembly of Super Mario Advance 4: Super Mario Bros. 3 (GBA) | 15 | 🟡 | Assembly |
| [Wario Land 3 disassembly](https://github.com/ElectroDeoxys/warioland3) | Disassembly of Wario Land 3 (Game Boy Color) | 15 | 🟢 | Assembly |
| [AGS Aging Cartridge 7.0 GBA test cartridge decomp](https://github.com/Normmatt/ags_aging) | Decompilation of the AGS Aging Cartridge 7.0 GBA test cartridge | 14 | 🔴 | C |
| [LSDj disassembly](https://github.com/rbong/LSDisJ) | Disassembly of LSDj (Game Boy) | 14 | 🔴 | Assembly |
| [Mario & Luigi: Partners in Time](https://github.com/Rainchus/PartnersInTime-Decomp) | Matching decompilation of Mario & Luigi: Partners in Time (Nintendo DS, 2005) | 14 | 🟢 | Python |
| [Pokered-Pro](https://github.com/Kamy41/Pokered-Pro) | Disassembly of Pokémon Red/Blue with some fixies and improvements (and a little surprise at Vermilion Dock if you tal... | 14 | 🟢 | Assembly |
| [Pokémon Blue disassembly](https://github.com/Narishma-gb/pokeblue) | Disassembly of Pokémon Blue (Game Boy, Japan) | 14 | 🟢 | Assembly |
| [Robot Poncots Sun and Star disassembly](https://github.com/PikalaxALT/robopon) | Disassembly of Robot Poncots Sun and Star (Game Boy Color, Japan) | 14 | 🟢 | Assembly |
| [Shi Kong Xing Shou disassembly](https://github.com/pizdex/shi-kong-xing-shou) | Disassembly of Shi Kong Xing Shou, an unlicensed Taiwanese Game Boy RPG | 14 | 🗄️ | Assembly |
| [Dragon Quest IX decomp](https://github.com/0bAndyWirus/DQ9-Decomp) | Decompilation tooling and research for Dragon Quest IX (Nintendo DS, EU) | 13 | 🟢 | C++ |
| [Dragon Warrior III disassembly](https://github.com/VariantXYZ/dragon-warrior-3-gbc) | Disassembly of Dragon Warrior III (Game Boy Color) | 13 | 🟡 | Assembly |
| [NitroSDK library decomp](https://github.com/nitro-decomp/nitro) | Decompilation of Nintendo's NitroSDK library from Nintendo DS games | 13 | 🟢 | C |
| [Pokémon Pinball: Ruby & Sapphire disassembly](https://github.com/Normmatt/Pokemon-Pinball-RS-Disassembly-Project) | Disassembly of Pokémon Pinball: Ruby & Sapphire (GBA) | 13 | 🔴 | Assembly |
| [Pokémon Rumble](https://github.com/KooShnoo/pokemon-rumble) | Decompilation of Pokémon Rumble | 13 | 🟢 | C++ |
| [Sonic Advance 2 disassembly](https://github.com/froggestspirit/SoAdvance2) | Disassembly of Sonic Advance 2 (GBA) | 13 | 🗄️ | Assembly |
| [Tetris disassembly](https://github.com/davFaithid/tetris-disassembly) | Disassembly of Tetris (Game Boy) buildable with RGBDS | 13 | 🔴 | Assembly |
| [Wario Land 4 (lilDavid)](https://github.com/lilDavid/warioland4) | Matching decompilation of Wario Land 4 (Game Boy Advance, 2001) | 13 | 🟢 | Assembly |
| [WarioWare, Inc.: Mega Microgames!](https://github.com/ShaffySwitcher/wariowareinc) | Matching decompilation of WarioWare, Inc.: Mega Microgames! (Game Boy Advance, 2003) | 13 | 🟢 | Assembly |
| [Advance Wars decomp](https://github.com/ketsuban/advancewars) | Decompilation of Advance Wars (GBA) | 12 | 🗄️ | Assembly |
| [Mario & Luigi: Dream Team decomp](https://github.com/Mario-and-Luigi-3Ds-R-D/MILLI4C) | Decompilation of Mario & Luigi: Dream Team (3DS, 1.0 US) | 12 | 🟢 | Python |
| [Paper Mario: Sticker Star](https://github.com/Darxoon/leaflitter) | Matching decompilation of Paper Mario: Sticker Star (Nintendo 3DS, 2012) | 12 | 🗄️ | Python |
| [pokefirered](https://github.com/cosarara/pokefirered) | Early disassembly project of Pokémon FireRed (GBA) | 11 | 🔴 | Assembly |
| [Pokémon Gold/Silver disassembly](https://github.com/Narishma-gb/pokesilver) | Disassembly of Pokémon Gold/Silver (Game Boy Color, Japan) | 11 | 🟢 | Assembly |
| [Rockman World 2 / Mega Man II disassembly](https://github.com/Kak2X/rw2) | Disassembly of Rockman World 2 / Mega Man II (Game Boy) | 11 | 🟢 | Assembly |
| [The Legend of Zelda: A Link Between Worlds decomp](https://github.com/7akeem0/albw-decomp-ai) | Matching decompilation of The Legend of Zelda: A Link Between Worlds (3DS, USA) | 11 | 🟢 | C |
| [The Legend of Zelda: Ocarina of Time 3D decomp](https://github.com/gamestabled/oot3d_before_public) | Decompilation of The Legend of Zelda: Ocarina of Time 3D (3DS) | 11 | 🟡 | C++ |
| [Yu-Gi-Oh! The Eternal Duelist Soul](https://github.com/CosmicScribe64/eds-decomp) | Matching decompilation of Yu-Gi-Oh! The Eternal Duelist Soul (Game Boy Advance, 2002) | 11 | 🟢 | Assembly |
| [Keitai Denjuu Telefang Speed and Power disassembly](https://github.com/PikalaxALT/telefang_gb) | Disassembly of Keitai Denjuu Telefang Speed and Power (Game Boy Color) | 10 | 🔴 | Assembly |
| [Kirby's Dream Land disassembly](https://github.com/Cleverking2003/kdreamlanddis) | Disassembly of Kirby's Dream Land (Game Boy) | 10 | 🔴 | Assembly |
| [LEGO Battles](https://github.com/LiruJ/Lego-Battles-Decomp) | Matching decompilation of LEGO Battles (Nintendo DS, 2009) | 10 | 🟡 | C++ |
| [Mario Golf disassembly](https://github.com/DarkRTA/mgolf) | Disassembly of Mario Golf (Game Boy Color) | 10 | 🔴 | Assembly |
| [Pokémon Mystery Dungeon: Red Rescue Team disassembly](https://github.com/PikalaxALT/pokemdred) | Disassembly of Pokémon Mystery Dungeon: Red Rescue Team (GBA) | 10 | 🔴 | Assembly |
| [Rockman EXE 4 Tournament Red Sun disassembly](https://github.com/dism-exe/exe4rs) | Disassembly of Rockman EXE 4 Tournament Red Sun (GBA, Japan) | 10 | 🔴 | C |
| [Sonic Battle](https://github.com/cypressru/SonicBattleDecomp) | Matching decompilation of Sonic Battle (Game Boy Advance, 2003) | 10 | 🟢 | C++ |
| [Super Mario 64 DS](https://github.com/matty45/sm64ds-decomp) | Decompilation of Super Mario 64 DS | 10 | 🗄️ | Assembly |
| [Animal Crossing: New Leaf - Welcome amiibo decomp](https://github.com/RedShyGuy/acnl-decomp) | Decompilation of Animal Crossing: New Leaf - Welcome amiibo (3DS, USA) | 9 | 🟢 | C++ |
| [Custom Robo GX](https://github.com/pizdex/robogx) | Matching decompilation of Custom Robo GX (Game Boy Advance, 2004) | 9 | 🟢 | Assembly |
| [Dragon Warrior Monsters](https://github.com/NiyaDev/DWM) | Matching decompilation of Dragon Warrior Monsters (Game Boy Color, 1998) | 9 | 🟢 | Assembly |
| [DWM](https://github.com/Mallos31/dwm) | Disassembly of Dragon Warrior Monsters 1 for the GBC | 9 | 🔴 | Assembly |
| [FXHammer-Disasm](https://github.com/DevEd2/FXHammer-Disasm) | Disassembly of the FX Hammer Game Boy sound driver | 9 | 🔴 | Assembly |
| [Ikachan decomp](https://github.com/hax0kartik/ikachan) | Decompilation of Ikachan for Nintendo 3DS | 9 | 🟢 | Python |
| [Mega Man Battle Network disassembly](https://github.com/Silenthal/bn1) | Disassembly of Mega Man Battle Network (GBA) | 9 | 🟢 | Assembly |
| [PictoChat decomp](https://github.com/tangOS-decomps/pictochat-decomp) | Matching decompilation of PictoChat (Nintendo DSi system title) | 9 | 🟢 | C |
| [Pokémon Aurora Ticket distribution cartridge decomp](https://github.com/jiangzhengwenjz/auroraticket) | Decompilation of the Pokémon Aurora Ticket distribution cartridge (GBA, USA) | 9 | 🔴 | C |
| [Pokémon Yellow disassembly](https://github.com/Narishma-gb/pokeyellow-jp) | Disassembly of Pokémon Yellow (Game Boy, Japan) | 9 | 🟢 | Assembly |
| [The Urbz: Sims in the City (GBA)](https://github.com/SimsAdvanceRet/UrbzGBADecomp) | Decompilation of The Urbz: Sims in the City (GBA) | 9 | 🟡 |  |
| [X / Lunar Chase disassembly](https://github.com/2Tie/X-disasm) | Disassembly of X / Lunar Chase (Game Boy) | 9 | 🔴 | Assembly |
| [Beyblade VForce: Ultimate Blader Jam](https://github.com/marijnvdwerf/gba-beyblade-vforce) | Decompilation of Beyblade VForce: Ultimate Blader Jam | 8 | 🟢 | C |
| [Boktai 2 decomp](https://github.com/akatsuki105/boktai2) | Decompilation of Boktai 2 (GBA, Japan v1.1) | 8 | 🟢 | Assembly |
| [Breath of Fire decomp](https://github.com/StanHash/bof_old) | Decompilation of Breath of Fire (GBA) | 8 | 🗄️ | Assembly |
| [Card e-Reader+ ROM disassembly](https://github.com/PikalaxALT/ereader) | Disassembly of the Card e-Reader+ ROM (GBA, US) | 8 | 🔴 | Assembly |
| [Mysterious GBA Fire Emblem MultiBoot Payload decomp](https://github.com/StanHash/mgfembp) | Decompilation of the Mysterious GBA Fire Emblem MultiBoot Payload | 8 | 🔴 | C |
| [Nettou King of Fighters '95 disassembly](https://github.com/Kak2X/kof95) | Disassembly of Nettou King of Fighters '95 (Game Boy) | 8 | 🟡 | Assembly |
| [Tetris disassembly](https://github.com/kaspermeerts/tetris) | Comprehensive disassembly of Tetris (Game Boy) | 8 | 🔴 | Assembly |
| [Bomberman Land Touch! 2](https://github.com/gamemasterplc/bltouch2) | Matching decompilation of Bomberman Land Touch! 2 (Nintendo DS, 2008) | 7 | 🟢 | C |
| [Dragon Warrior Monsters 2 decomp](https://github.com/NiyaDev/DWM2) | Decompilation of Dragon Warrior Monsters 2 (Game Boy Color) | 7 | 🔴 | Assembly |
| [Final Fantasy Legend II / SaGa 2 disassembly](https://github.com/Bananattack/fflsaga2) | Disassembly of Final Fantasy Legend II / SaGa 2 (Game Boy) | 7 | 🔴 | Assembly |
| [Hamtaro: Ham-Ham Games decomp](https://github.com/XOlifreX/hhg-decompilation) | pret-style decompilation of Hamtaro: Ham-Ham Games (GBA) | 7 | 🔴 | Assembly |
| [Magi-Nation disassembly](https://github.com/GauChoob/magination) | Disassembly of Magi-Nation (Game Boy Color) | 7 | 🟡 | Assembly |
| [medarot](https://github.com/Sanqui/medarot) | Disassembly and English translation of Medarot (Game Boy) | 7 | 🔴 | Assembly |
| [Nettou King of Fighters '96 disassembly](https://github.com/Kak2X/kof96) | Disassembly of Nettou King of Fighters '96 (Game Boy) | 7 | 🟡 | Assembly |
| [NintendoWare decomp](https://github.com/ctrdecomp/NintendoWare4Ctr) | Decompilation of NintendoWare for CTR (NW4C), the C++ engine used in most 3DS games | 7 | 🟢 | C++ |
| [Pokémon Gold and Silver debug ROMs disassembly](https://github.com/pizdex/pokegold-debug) | Disassembly of the Pokémon Gold and Silver debug ROMs (Game Boy Color, Japan) | 7 | 🗄️ | Assembly |
| [Super Mario Land 2 disassembly](https://github.com/stag019/marioland2) | Disassembly of Super Mario Land 2 (Game Boy) | 7 | 🔴 | Assembly |
| [Super Mario World: Super Mario Advance 2 disassembly](https://github.com/KarisaAdvynia/sma2-disasm) | Disassembly of Super Mario World: Super Mario Advance 2 (GBA) | 7 | 🟡 | Assembly |
| [Wii connection program in Pokémon Diamond and Pearl disassembly](https://github.com/PikalaxALT/eoo) | Disassembly of the Wii connection program in Pokémon Diamond and Pearl (Nintendo DS) | 7 | 🔴 | Assembly |
| [Yoshi's Island: Super Mario Advance 3 disassembly](https://github.com/KarisaAdvynia/sma3-disasm) | Disassembly of Yoshi's Island: Super Mario Advance 3 (GBA) | 7 | 🟢 | Assembly |
| [Animal Crossing: New Leaf decomp](https://github.com/AlgebraManiacABC/acnlwa-decomp) | Decompilation of Animal Crossing: New Leaf (3DS) | 6 | 🟢 | C |
| [Animal Crossing: Wild World decomp](https://github.com/banatic/acww-decomp) | Matching decompilation of Animal Crossing: Wild World (Nintendo DS, Korea) ARM9 code | 6 | 🟢 | C |
| [ARM9 binary of Fire Emblem: Shadow Dragon decomp](https://github.com/MokhaLeee/fe11us-arm9) | Decompilation of the ARM9 binary of Fire Emblem: Shadow Dragon (Nintendo DS, US) | 6 | 🟢 | Assembly |
| [Bugsite disassembly](https://github.com/telefang/bugsite) | Disassembly of Bugsite (Game Boy Color, Smilesoft) | 6 | 🟢 | Python |
| [Dragon Warrior Monsters disassembly](https://github.com/ketsuban/dwm1) | Disassembly of Dragon Warrior Monsters (Game Boy Color) | 6 | 🟡 | Assembly |
| [eCrew Development Program](https://github.com/imavie/ecdpdecomp) | Matching decompilation of eCrew Development Program (Nintendo DS, 2010; McDonald's training game) | 6 | 🟡 |  |
| [Frogger's Adventures: Temple of the Frog](https://github.com/JRickey/frog-adv-temple-decomp) | Matching decompilation of Frogger's Adventures: Temple of the Frog (Game Boy Advance, 2001) | 6 | 🟢 | Assembly |
| [Korean Pokémon Gold/Silver disassembly](https://github.com/Greatpriceman/pokegold-ko) | Disassembly of the Korean Pokémon Gold/Silver (Game Boy Color) | 6 | 🔴 | Assembly |
| [Mario & Luigi: Bowser's Inside Story decomp](https://github.com/istornz/bowsers-inside-story-decomp) | Matching decompilation of Mario & Luigi: Bowser's Inside Story (Nintendo DS) | 6 | 🟢 | C++ |
| [OpenTS3-DS](https://github.com/luispolis124/OpenTS3-DS) | Decompilation and native PC port project for The Sims 3 (Nintendo DS) | 6 | 🟢 | C |
| [Pokémon Ranger: Shadows of Almia decomp](https://github.com/Kuruyia/pokeranger2) | Decompilation of Pokémon Ranger: Shadows of Almia (Nintendo DS) | 6 | 🟢 | Assembly |
| [Shin'en Multimedia's GAX sound engine decomp](https://github.com/beanieaxolotl/shinen-gax-decomp) | Decompilation of Shin'en Multimedia's GAX sound engine (GBA) | 6 | 🟢 | C |
| [Spanish release of Pokémon Crystal disassembly](https://github.com/erosunica/pokecrystal-es) | Disassembly of the Spanish release of Pokémon Crystal (Game Boy Color) | 6 | 🔴 | Assembly |
| [The Legend of Zelda: Link's Awakening disassembly](https://github.com/alexsteb/zelda_gb_disassembly) | Disassembly of The Legend of Zelda: Link's Awakening (Game Boy) | 6 | 🔴 | Assembly |
| [The Sims 2 (GBA)](https://github.com/SimsAdvanceRet/S2GBADecomp) | Decompilation of The Sims 2 (GBA) | 6 | 🟡 |  |
| [The Sims 2 disassembly](https://github.com/tssoret/S2GBADecomp) | Disassembly and decompilation of The Sims 2 (GBA) | 6 | 🔴 |  |
| [The Sims: Bustin' Out (GBA)](https://github.com/SimsAdvanceRet/BustinOutGBADecomp) | Decompilation of The Sims: Bustin' Out (GBA) | 6 | 🟡 |  |
| [Tomodachi Life decomp](https://github.com/dylanpdx/TomodachiLifeDecomp) | Decompilation of Tomodachi Life (3DS) | 6 | 🟢 | Python |
| [Yu-Gi-Oh! Duel Monsters disassembly](https://github.com/ElectroDeoxys/ygodm) | Disassembly of Yu-Gi-Oh! Duel Monsters (Game Boy) | 6 | 🟢 | Assembly |
| [Yu-Gi-Oh! GX Spirit Caller decomp](https://github.com/cntrl-alt-lenny/gx-spirit-caller) | Matching decompilation of Yu-Gi-Oh! GX Spirit Caller (Nintendo DS) | 6 | 🟢 | Assembly |
| [a GBA multiboot ROM found in Animal Crossing disassembly](https://github.com/BluRosie/needle-loader-mb) | Disassembly of a GBA multiboot ROM found in Animal Crossing | 5 | 🟢 | C |
| [Berry Fix Program bundled disassembly](https://github.com/PikalaxALT/berry_fix_program) | Disassembly of the Berry Fix Program bundled with Pokémon FireRed (GBA) | 5 | 🔴 | C |
| [Elite demo decomp](https://github.com/Villagerjj/Elite-GB-Decomp) | Decompilation of the Elite demo for Game Boy | 5 | 🟡 | Assembly |
| [Flipull disassembly](https://github.com/tobiasvl/flipull-disassembly) | Disassembly of Flipull (Game Boy) | 5 | 🔴 | Assembly |
| [GTPD-Code-Reference](https://github.com/Ed-1T/GTPD-Code-Reference) | Public decompilation reference for Ghost Trick: Phantom Detective (DS) | 5 | 🟡 | C++ |
| [Harvest Moon GB disassembly](https://github.com/H0smax/HMGB-Disassembly) | Disassembly of Harvest Moon GB (Game Boy) | 5 | 🟢 | Assembly |
| [jungle-book-gb-disassembly](https://github.com/not-chciken/jungle-book-gb-disassembly) | Disassembly of The Jungle Book (1994) for Game Boy | 5 | 🟢 | Assembly |
| [Kirby Tilt 'n' Tumble disassembly](https://github.com/davFaithid/tilt-n-tumble) | Disassembly of Kirby Tilt 'n' Tumble (Game Boy Color) | 5 | 🔴 | Assembly |
| [Kirby's Dream Land disassembly](https://github.com/ElectroDeoxys/kirbydreamland) | Disassembly of Kirby's Dream Land (Game Boy) | 5 | 🟢 | Assembly |
| [LEGO Star Wars II: The Original Trilogy decomp](https://github.com/liolu/lego-star-wars-ii-the-original-trilogy-decomp) | Matching decompilation of LEGO Star Wars II: The Original Trilogy (Nintendo DS) | 5 | 🟢 | C |
| [medarot1-pc](https://github.com/Medabots/medarot1-pc) | Disassembly and translation of Medarot Parts Collection (Game Boy) | 5 | 🟢 | Python |
| [Nintendo nnsdk library decomp](https://github.com/3dsdecomp/nnsdk) | Decompilation of the Nintendo nnsdk library from 3DS games | 5 | 🔴 | C++ |
| [Princess Maker 4](https://github.com/Yanis002/pm4) | Matching decompilation of Princess Maker 4 (Nintendo DS; Japanese version) | 5 | 🟢 | C |
| [Resident Evil Gaiden disassembly](https://github.com/wowjinxy/RE-Gaiden) | Disassembly of Resident Evil Gaiden (Game Boy Color) | 5 | 🟢 | Assembly |
| [Tetris disassembly](https://github.com/dctucker/gb-tetris) | Disassembly of Tetris (Game Boy) | 5 | 🔴 | Assembly |
| [Tomodachi Life decomp](https://github.com/akiramusic000/tl) | Decompilation of Tomodachi Life (3DS, USA) | 5 | 🟢 | Python |
| [Wario Land 4 decomp](https://github.com/wario-land/warioland4) | Non-standard decompilation of Wario Land 4 (GBA) | 5 | 🟢 | C |
| [999-Code-Reference](https://github.com/Ed-1T/999-Code-Reference) | Decompilation reference for Nine Hours, Nine Persons, Nine Doors (Nintendo DS) | 4 | 🔴 | RPC |
| [Advance Wars: Dual Strike decomp](https://github.com/sturmds/advance-wars-dual-strike-decomp) | Decompilation of Advance Wars: Dual Strike (Nintendo DS) | 4 | 🟢 | C |
| [Batman disassembly](https://github.com/alex-west/batGB) | Disassembly of Batman (Game Boy) | 4 | 🔴 | Assembly |
| [Croc 2 disassembly](https://github.com/anmart/croc2) | Disassembly of Croc 2 (Game Boy Color) | 4 | 🔴 | Python |
| [Devil Children Black disassembly](https://github.com/Tauwasser/debichiru) | Disassembly of Devil Children Black, Red and White Book (Game Boy Color) | 4 | 🔴 | Assembly |
| [Final Fantasy Legend II disassembly](https://github.com/relic374/final-fantasy-legends-2-disassembly) | Disassembly of Final Fantasy Legend II (Game Boy) | 4 | 🟡 | Assembly |
| [German Dragon Warrior Monsters disassembly](https://github.com/Ebernacher90/DragonQuestMonstersGerman) | Disassembly of the German Dragon Warrior Monsters (Game Boy Color) | 4 | 🔴 | Assembly |
| [Harry Potter and the Prisoner of Azkaban (GBA)](https://github.com/holly-hacker/hp3-gba-decomp) | Decompilation of Harry Potter and the Prisoner of Azkaban (GBA) | 4 | 🟢 | C |
| [LEGO Island 2 decomp](https://github.com/minirop/lego-island-gba) | Decompilation of LEGO Island 2 (GBA) | 4 | 🟢 | C |
| [Mario Kart DS decomp](https://github.com/ai-tdd-labs/mkds-decomp) | AI-assisted matching decompilation of Mario Kart DS (Nintendo DS, EUR) | 4 | 🟢 | C |
| [Mole Mania disassembly](https://github.com/froggestspirit/mmania) | Disassembly of Mole Mania (Game Boy) | 4 | 🟡 | Assembly |
| [Nintendo e-Reader cards disassembly](https://github.com/d1x/ereader-card-disassemblies) | Disassemblies of Nintendo e-Reader cards (GBA) | 4 | 🔴 | Assembly |
| [Out of Gas disassembly](https://github.com/JimB16/OutOfGas) | Disassembly of Out of Gas (Game Boy) | 4 | 🔴 | Assembly |
| [Pikachu ga Pokeboru o Aishimasu decomp](https://github.com/easyaspi314/pikaaishimasu) | Decompilation of Pikachu ga Pokeboru o Aishimasu | 4 | 🔴 | C |
| [Pokémon BUUJ event distribution cartridges decomp](https://github.com/FreakedOutGamer/pokeBUUJ) | Decompilation of the Pokémon BUUJ event distribution cartridges (GBA) | 4 | 🟢 | C |
| [Pokémon Sodateyasan Mini disassembly](https://github.com/notyourav/pokesoda) | Disassembly of Pokémon Sodateyasan Mini (Japan) | 4 | 🔴 | Assembly |
| [Rayman Raving Rabbids decomp](https://github.com/liolu/Rayman-RR-usa-decomp) | Matching decompilation of Rayman Raving Rabbids (Nintendo DS, USA) | 4 | 🟢 | C |
| [Resident Evil: Deadly Silence decomp](https://github.com/liolu/resident-evil-deadly-silence-decomp) | Matching decompilation of Resident Evil: Deadly Silence (Nintendo DS) | 4 | 🟢 | C |
| [sead library decomp](https://github.com/3dsdecomp/sead) | Decompilation of Nintendo's sead library for 3DS | 4 | 🔴 | C++ |
| [Winx Club disassembly](https://github.com/Matt-Hurd/WinxClub) | Disassembly of Winx Club (GBA) | 4 | 🟢 | Assembly |
| [Alleyway disassembly](https://github.com/islander0/alleyway-decomp) | Annotated disassembly and decompilation of Alleyway (Game Boy, 1989) | 3 | 🟢 | Assembly |
| [Digimon World DS](https://github.com/ReGame-Labs/dwds_decomp) | Decompilation of Digimon World DS | 3 | 🟢 | C |
| [Eltale Monsters decomp](https://github.com/Mallos31/EM) | Decompilation of Eltale Monsters (Game Boy Color) | 3 | 🟡 | Assembly |
| [Gex: Deep Pocket Gecko disassembly](https://github.com/exodus122/gex3gbc) | Disassembly of Gex: Deep Pocket Gecko (Game Boy Color) | 3 | 🟢 | Assembly |
| [Harvest Moon DS decomp](https://github.com/liolu/harvest-moon-ds-decomp) | Matching decompilation of Harvest Moon DS (Nintendo DS) | 3 | 🟢 | C |
| [Harvest Moon GBC disassembly](https://github.com/Xillicis/Harvest-Moon-GBC-Disassembly) | Disassembly of Harvest Moon GBC (Game Boy Color) | 3 | 🟢 | Assembly |
| [Kirby's Dream Land 2 disassembly](https://github.com/Ebernacher90/kirbydreamland2) | Disassembly of Kirby's Dream Land 2 (Game Boy) | 3 | 🔴 | Assembly |
| [Korean Pokémon Gold/Silver disassembly](https://github.com/Narishma-gb/pokegold-kr) | Disassembly of the Korean Pokémon Gold/Silver (Game Boy Color) | 3 | 🟢 | Assembly |
| [Mario & Luigi: Partners in Time decomp](https://github.com/aricloverEXTRA/PartnersInTimeDECOMP) | Matching decompilation of Mario & Luigi: Partners in Time (Nintendo DS) | 3 | 🟢 | C |
| [Nintendogs: Dachshund & Friends decomp](https://github.com/liolu/nintendogs-dachshund-decomp) | Matching decompilation of Nintendogs: Dachshund & Friends (Nintendo DS) | 3 | 🟢 | C |
| [Okamiden](https://github.com/dothacktranslate/okamiden-decomp) | Matching decompilation of Okamiden (Nintendo DS, 2010) | 3 | 🟢 | C |
| [Pocket Love disassembly](https://github.com/RussianManSMWC/Pocket-Love-Disassembly) | Disassembly of Pocket Love (Game Boy) | 3 | 🟢 | Assembly |
| [sakura-wars-gb2](https://github.com/VariantXYZ/sakura-wars-gb2) | Disassembly and translation of Sakura Wars GB2 (Game Boy Color) | 3 | 🟢 | Assembly |
| [Sutte Hakkun disassembly](https://github.com/pizdex/suttehakkun) | Disassembly of Sutte Hakkun (Game Boy) | 3 | 🗄️ | Assembly |
| [Tetris disassembly](https://github.com/taylus/gb-tetris-dasm) | Annotated disassembly of Tetris (Game Boy) | 3 | 🗄️ | Assembly |
| [Ultimate Spider-Man decomp](https://github.com/liolu/ultimate-spider-man-decomp) | Matching decompilation of Ultimate Spider-Man (Nintendo DS) | 3 | 🟢 | C |
| [UNO! disassembly](https://github.com/PikalaxALT/uno) | Disassembly of UNO! (Game Boy Color) | 3 | 🔴 | C |
| [a GBA multiboot island loader ROM disassembly](https://github.com/BluRosie/island-loader-mb) | Disassembly of a GBA multiboot island loader ROM from Animal Crossing | 2 | 🟡 | C |
| [Cooking Mama decomp](https://github.com/liolu/cooking-mama-decomp) | Matching decompilation of Cooking Mama (Nintendo DS) | 2 | 🟢 | C |
| [Dragon Ball Z: Buu's Fury disassembly](https://github.com/siruiusamory-cmyk/buusfury-disasm) | Byte-exact disassembly of Dragon Ball Z: Buu's Fury (GBA, USA) | 2 | 🟢 | Assembly |
| [Dragon Quest Monsters: Joker decomp](https://github.com/FantasmaGlad/DQMJ1_Ultimate_Decompilation) | C decompilation of Dragon Quest Monsters: Joker (Nintendo DS) | 2 | 🟢 | Assembly |
| [DuckTales (Game Boy) Disassembly](https://github.com/RussianManSMWC/DuckTales-of-Disassembly-GB) | A disassembly of DuckTales for the Game Boy | 2 | 🟢 | Assembly |
| [Game Boy Camera ROM disassembly](https://github.com/Raphael-Boichot/Game-Boy-Camera-disassembly) | Disassembly of the Game Boy Camera ROM | 2 | 🟢 | Python |
| [GT Advance 3: Pro Concept Racing](https://github.com/722rsr/gtadv3-decomp) | Matching decompilation of GT Advance 3: Pro Concept Racing (Game Boy Advance, 2003) | 2 | 🟢 | C |
| [Harvest Moon: Friends of Mineral Town to C decomp](https://github.com/Denisovich728/FIO-DECOMP-HMFOMT) | Decompilation of Harvest Moon: Friends of Mineral Town to C (GBA) | 2 | 🟢 | C |
| [Luigi's Mansion decomp](https://github.com/pancakers2001/lm3ds-decomp) | Decompilation of Luigi's Mansion (3DS) | 2 | 🟢 | C |
| [Marchen Awakens Romance decomp](https://github.com/name1esshero/Marchen-Awakens-Romance) | Decompilation of Marchen Awakens Romance (GBA) | 2 | 🟢 | Assembly |
| [Mario & Luigi: Superstar Saga decomp](https://github.com/JohnSoellnerDev/mlss-decomp) | Decompilation of Mario & Luigi: Superstar Saga (GBA) | 2 | 🟢 | C |
| [Money Idol Exchanger disassembly](https://github.com/gabe-k/money-idol-exchanger-re) | Disassembly of Money Idol Exchanger (Game Boy) | 2 | 🔴 | Assembly |
| [My Pokémon Ranch DS client ROM decomp](https://github.com/taxicat1/pl-mpr-client) | Decompilation of the My Pokémon Ranch DS client ROM | 2 | 🟢 | C |
| [Ocarina of Time 3D decomp](https://github.com/SomeoneIsWorking/oot3d-decomp) | Reverse engineering and decompilation of Ocarina of Time 3D (3DS) | 2 | 🟢 | C |
| [Pokémon 10th Anniversary distribution cartridge decomp](https://github.com/lzeduardo64/buuj) | Decompilation of the Pokémon 10th Anniversary distribution cartridge (GBA) | 2 | 🟢 | C |
| [Pokémon Gelbe Edition disassembly](https://github.com/Brianum/pokeyellow-de) | Disassembly of Pokémon Gelbe Edition (Game Boy, German) | 2 | 🟢 | Assembly |
| [Pokémon Version Jaune disassembly](https://github.com/Narishma-gb/pokeyellow-fr) | Disassembly of Pokémon Version Jaune (Game Boy, French) | 2 | 🟢 | Assembly |
| [SolarStriker disassembly](https://github.com/pizdex/solarstriker) | Disassembly of SolarStriker (Game Boy) | 2 | 🔴 | Assembly |
| [Soukoban disassembly](https://github.com/HazeSystem/Soukoban-Disassembly) | Disassembly of Soukoban (Game Boy) | 2 | 🔴 | Assembly |
| [sound driver of Mario's Picross disassembly](https://github.com/DevEd2/DSEQ) | Disassembly of the sound driver of Mario's Picross (Game Boy) | 2 | 🔴 | Assembly |
| [Spider-Man: Web of Shadows decomp](https://github.com/liolu/spider-man-web-of-shadows-decomp) | Matching decompilation of Spider-Man: Web of Shadows (Nintendo DS) | 2 | 🟢 | C |
| [Super Mario 64 DS decomp](https://github.com/tangOS-decomps/sm64ds-decomp) | Decompilation of Super Mario 64 DS (Nintendo DS) | 2 | 🟢 | Zig |
| [Tetris Attack disassembly](https://github.com/tobiasvl/tetris-attack-disassembly) | Disassembly of Tetris Attack (Game Boy) | 2 | 🟢 | Assembly |
| [The Legend of Zelda: Link's Awakening DX decomp](https://github.com/Hysm25/LADX-Decompile) | Decompilation of The Legend of Zelda: Link's Awakening DX (Game Boy Color) | 2 | 🟢 | C |
| [The Legend of Zelda: Oracle of Seasons disassembly](https://github.com/Stewmath/seasons-disasm) | Disassembly of The Legend of Zelda: Oracle of Seasons (Game Boy Color) | 2 | 🗄️ | Assembly |
| [The Legend of Zelda: Oracle of Seasons disassembly](https://github.com/AmbiSykhar/oos-disassembly) | Disassembly of The Legend of Zelda: Oracle of Seasons (Game Boy Color) | 2 | 🔴 | Assembly |
| [The Sims: Bustin' Out decomp](https://github.com/DaBrown95/tsbodp) | Matching decompilation of The Sims: Bustin' Out (GBA) | 2 | 🟢 | C |
| [UltraSunnyMoon](https://github.com/tylergraydev/UltraSunnyMoon) | Partial REA-assisted decompilation of Pokémon Ultra Sun (3DS) | 2 | 🟢 | Python |
| [Yo-kai Watch 2 decomp](https://github.com/ChaconMoon/yokai-watch-2-decompiled) | Decompilation of Yo-kai Watch 2 (3DS) | 2 | 🟢 | Python |
| [a GBA multiboot island program ROM disassembly](https://github.com/BluRosie/island-program-mb) | Disassembly of a GBA multiboot island program ROM from Animal Crossing | 1 | 🟡 | Assembly |
| [Advance Wars: Dual Strike decomp](https://github.com/ozyz/awds-decomp) | Matching decompilation of Advance Wars: Dual Strike (Nintendo DS, Europe) | 1 | 🟢 | Python |
| [Alleyway disassembly](https://github.com/Wit-MKW/alleyway-gb) | Disassembly of Alleyway (Game Boy, World) | 1 | 🟢 | Assembly |
| [BattleTanx disassembly](https://github.com/TheGh0stShip/BattleTanx-GBC) | Byte-exact annotated disassembly of BattleTanx (Game Boy Color) | 1 | 🟢 | Assembly |
| [Catrap decomp](https://github.com/nefelibatacfg/Catrap---game-boy-decompilation) | AI-assisted decompilation of Catrap (Game Boy) | 1 | 🟢 | Assembly |
| [Deja Vu I & II disassembly](https://github.com/Hoshiruna/djv1-2disasm) | Disassembly of Deja Vu I & II (Game Boy Color) | 1 | 🟢 | Assembly |
| [Dragon Ball: Origins decomp](https://github.com/liolu/dragon-ball-origins-decomp) | Matching decompilation of Dragon Ball: Origins (Nintendo DS) | 1 | 🟢 | C |
| [Dragon Warrior Monsters disassembly](https://github.com/banner88/dwm1_disassembly) | Disassembly of Dragon Warrior Monsters (Game Boy Color) | 1 | 🟢 | Assembly |
| [Eltale Monsters decomp](https://github.com/Rainchus/EltaleMonsters-Decomp) | Decompilation of Eltale Monsters (Game Boy Color) | 1 | 🟢 | C |
| [Fairy Tail: Madoushi decomp](https://github.com/liolu/fairy-tail-madoushi-decomp) | Matching decompilation of Fairy Tail: Madoushi (Nintendo DS) | 1 | 🟢 | C |
| [Final Fantasy Tactics Advance decomp](https://github.com/charlie-troy/ffta-decomp) | Decompilation of Final Fantasy Tactics Advance (GBA) | 1 | 🟢 | Python |
| [Fire Emblem decomp](https://github.com/7ucina/fireemblem7u) | Matching decompilation of Fire Emblem (GBA, USA/Australia) | 1 | 🟢 | C |
| [Fossil Fighters decomp](https://github.com/Sojews/fossil-fighters-decomp) | Matching decompilation of Fossil Fighters (Nintendo DS) | 1 | 🟢 | C++ |
| [Fossil Fighters: Champions decomp](https://github.com/arcnid/ffc-decomp) | Matching decompilation of Fossil Fighters: Champions (Nintendo DS) | 1 | 🟢 | Assembly |
| [Hamtaro: Ham-Ham Heartbreak decomp](https://github.com/josealmon/hamtaro-heartbreak) | Matching decompilation of Hamtaro: Ham-Ham Heartbreak (GBA, Europe) | 1 | 🟢 | C |
| [Heroes of Mana decomp](https://github.com/liolu/heroes-of-mana-decomp) | Matching decompilation of Heroes of Mana (Nintendo DS) | 1 | 🟢 | C |
| [Kirby: Nightmare in Dream Land decomp](https://github.com/andrewnakas/knidl-web) | Byte-matching decompilation of Kirby: Nightmare in Dream Land (GBA) | 1 | 🟢 | Python |
| [Koto Battle: Tengai no Moribito disassembly](https://github.com/pizdex/kotobattle) | Disassembly of Koto Battle: Tengai no Moribito (Game Boy Color) | 1 | 🗄️ | Assembly |
| [LSDj 9.4.0 disassembly](https://github.com/gmoben/lsdj-decompiled) | pret-style disassembly of LSDj 9.4.0 (Game Boy) | 1 | 🟢 | C |
| [Mario Kart DS decomp](https://github.com/RonyxDumb/mkds) | Decompilation of Mario Kart DS (Nintendo DS, EU) | 1 | 🟢 | Python |
| [Mario Tennis disassembly](https://github.com/gerbiljames/mario-tennis-gbc-disasm) | Disassembly of Mario Tennis (Game Boy Color) | 1 | 🟢 | Assembly |
| [Mario vs. Donkey Kong e-Reader cards decomp](https://github.com/camthehaxman/mariovsdk-carde) | Decompilation of the Mario vs. Donkey Kong e-Reader cards | 1 | 🟡 | C |
| [Mega Man Battle Network 6 Cybeast Gregar decomp](https://github.com/st4rk/mmbn6_decomp) | Reverse engineering of Mega Man Battle Network 6 Cybeast Gregar (GBA) | 1 | 🔴 | Assembly |
| [NASCAR Heat 2002](https://github.com/shohamc1/heat2002) | Matching decompilation of NASCAR Heat 2002 (Game Boy Advance, 2001) | 1 | 🟢 | C |
| [Nintendo 3DS SDK libraries decomp](https://github.com/RE-Pepper/ctrsdk) | Decompilation of the Nintendo 3DS SDK libraries | 1 | 🟢 | C++ |
| [Pokémon Versione Rossa and Blu disassembly](https://github.com/alechieffi/pokered-it) | Disassembly of Pokémon Versione Rossa and Blu (Game Boy, Italian) | 1 | 🟢 | Assembly |
| [Quest RPG: Brian's Journey decomp](https://github.com/nefelibatacfg/Quest-RPG---Brian-s-Journey-USA-Decompilation.) | AI-assisted decompilation of Quest RPG: Brian's Journey (Game Boy Color, USA) | 1 | 🟢 |  |
| [Resident Evil Game Boy Color prototype disassembly](https://github.com/ecruells/residentevilgbc) | Disassembly of the Resident Evil Game Boy Color prototype | 1 | 🔴 | Assembly |
| [sead library decomp](https://github.com/RE-Pepper/sead_ctr) | Decompilation of Nintendo's sead library for 3DS | 1 | 🟢 | C++ |
| [Shin Bokura no Taiyou: Gyakushuu no Sabata](https://github.com/moozilla/boktai3-decomp) | Matching decompilation of Shin Bokura no Taiyou: Gyakushuu no Sabata (Game Boy Advance, 2005) | 1 | 🟢 | C |
| [Shin Megami Tensei IV and IV: Apocalypse decomp](https://github.com/Megami-Decomps/smt4-decomp) | Matching decompilation of Shin Megami Tensei IV and IV: Apocalypse (3DS) | 1 | 🟢 | C++ |
| [Spiritual Warfare disassembly](https://github.com/vinheim3/spiritualWarfare-disasm) | Disassembly of Spiritual Warfare (Game Boy) | 1 | 🔴 | Assembly |
| [Spyro: Shadow Legacy decomp](https://github.com/liolu/spyro-shadow-legacy-decomp) | Matching decompilation of Spyro: Shadow Legacy (Nintendo DS) | 1 | 🟢 | C |
| [Super Mario Bros. Deluxe disassembly](https://github.com/KarisaAdvynia/smbdx-disasm) | Disassembly of Super Mario Bros. Deluxe (Game Boy Color) | 1 | 🟡 | Assembly |
| [Tetris Plus disassembly](https://github.com/VinceIP/tetris-plus-disassembly) | Disassembly of Tetris Plus (Game Boy) | 1 | 🟢 | Assembly |
| [The Simpsons Game decomp](https://github.com/liolu/simpsons-game-decomp) | Matching decompilation of The Simpsons Game (Nintendo DS) | 1 | 🟢 | C |
| [Yoshi's Island DS decomp](https://github.com/yoshidonoshi/yids-decomp) | Decompilation of Yoshi's Island DS (Nintendo DS) | 1 | 🟡 | C |
| [Zoids Saga decomp](https://github.com/jmacato/ZoidsSagaOneDecomp) | Matching decompilation of Zoids Saga (GBA, Japan) | 1 | 🟢 | C |
| [Zoids Saga Fuzors decomp](https://github.com/jmacato/ZoidsSagaFuzorsDecomp) | Matching decompilation of Zoids Saga Fuzors (GBA, Japan) | 1 | 🟢 | C |
| [Advance Wars decomp](https://github.com/pizdex/advancewars) | Decompilation of Advance Wars (GBA) | 0 | 🔴 | Assembly |
| [Alleyway](https://github.com/CelestialAmber/alleyway) | Disassembly of Alleyway | 0 | 🔴 | Assembly |
| [Alleyway disassembly](https://github.com/vinheim3/alleyway-disasm) | Disassembly of Alleyway (Game Boy) | 0 | 🔴 | Assembly |
| [Bakugan: Battle Brawlers decomp](https://github.com/tylzars/bakubrawlers) | Matching decompilation of Bakugan: Battle Brawlers (Nintendo DS) | 0 | 🟢 | C++ |
| [Blue Dragon: Awakened Shadow decomp](https://github.com/liolu/blue-dragon-awakened-shadow-decomp) | Matching decompilation of Blue Dragon: Awakened Shadow (Nintendo DS) | 0 | 🟢 | C |
| [Code Lyoko decomp](https://github.com/liolu/code-lyoko-decomp) | Matching decompilation of Code Lyoko (Nintendo DS) | 0 | 🟢 | C |
| [Densha de Go! 2 disassembly](https://github.com/vinheim3/densha-2-disasm) | Disassembly of Densha de Go! 2 (Game Boy Color) | 0 | 🔴 | Assembly |
| [Dragon Ball Z: The Legacy of Goku II disassembly](https://github.com/siruiusamory-cmyk/legacyofgoku2-disasm) | Byte-exact disassembly of Dragon Ball Z: The Legacy of Goku II (GBA, USA) | 0 | 🟢 | Python |
| [DWM](https://codeberg.org/Emnity/DWM) | Decompilation of Dragon Warrior Monsters (Game Boy Color) |  | ⚪ |  |
| [Eyeshield 21 decomp](https://github.com/liolu/eyeshield-21-decomp) | Matching decompilation of Eyeshield 21 (Nintendo DS) | 0 | 🟢 | C |
| [Fairy Tail: Kardia decomp](https://github.com/liolu/fairy-tail-kardia-decomp) | Matching decompilation of Fairy Tail: Kardia (Nintendo DS) | 0 | 🟢 | C |
| [Farm Frenzy decomp](https://github.com/liolu/farm-frenzy-decomp) | Matching decompilation of Farm Frenzy (Nintendo DS) | 0 | 🟢 | C |
| [Fire Emblem decomp](https://github.com/rrafifnanda/fe7eu-decomp) | Matching decompilation of Fire Emblem (GBA, Europe) | 0 | 🟢 | C |
| [Harry Potter and the Chamber of Secrets disassembly](https://github.com/goofbrush/HPCoS) | Disassembly of Harry Potter and the Chamber of Secrets (Game Boy Color) | 0 | 🟡 | Assembly |
| [Kanken Training 2 decomp](https://github.com/mschienbein/kanken-training-2-decomp) | Matching decompilation of Kanken Training 2 (Nintendo 3DS) | 0 | 🟢 | C++ |
| [kh-com](https://codeberg.org/aryan-sinhala349/kh-com) | Decompilation of Kingdom Hearts: Chain of Memories (GBA) |  | ⚪ |  |
| [Kid Icarus: Of Myths and Monsters disassembly](https://github.com/ordinary-hacker/kid-icarus-omm) | Disassembly of Kid Icarus: Of Myths and Monsters (Game Boy) | 0 | 🟢 | Assembly |
| [Kwirk disassembly](https://github.com/vinheim3/kwirk-disasm) | Disassembly of Kwirk (Game Boy) | 0 | 🔴 | Assembly |
| [Livly Garden decomp](https://github.com/liolu/livly-garden-decomp) | Matching decompilation of Livly Garden (Nintendo DS) | 0 | 🟢 | C |
| [Lock's Quest](https://github.com/redraincatching/locksmith) | Matching decompilation of Lock's Quest (Nintendo DS, 2008) | 0 | 🟡 |  |
| [LSDj 9.4.2 decomp](https://github.com/tetrisgm/lsdj-decomp) | Byte-matching decompilation of LSDj 9.4.2 (Game Boy) | 0 | 🟢 | Python |
| [Mario & Luigi: Bowser's Inside Story decomp](https://github.com/weaversworkshop/mlbis-decomp) | Matching decompilation of Mario & Luigi: Bowser's Inside Story (Nintendo DS) | 0 | 🟢 | C++ |
| [Medabots Rokusho decomp](https://github.com/rommerhacks/medabots-rokusho) | AI-assisted byte-identical decompilation of Medabots Rokusho (GBA) | 0 | 🟢 | C |
| [Monsters decomp](https://github.com/eddieburke/monstersincgba-audioengine) | Decompilation and reconstruction of the Monsters, Inc. GBA audio engine | 0 | 🟢 | Python |
| [MySims decomp](https://github.com/liolu/mysims-decomp) | Matching decompilation of MySims (Nintendo DS) | 0 | 🟢 | C |
| [ninjacop](https://gitlab.com/Fexean/ninjacop) | Disassembly of Ninja Cop (GBA) |  | ⚪ |  |
| [NNSDK library used decomp](https://github.com/LeafReverse/NNSDK-ACNLWA) | Decompilation of the NNSDK library used by Animal Crossing: New Leaf - Welcome amiibo (3DS) | 0 | 🟢 | C++ |
| [Pocket Puyo Puyo 2 disassembly](https://github.com/pizdex/pocketpuyotsuu) | Disassembly of Pocket Puyo Puyo 2 (Game Boy) | 0 | 🔴 | Assembly |
| [Powerpuff Girls Z decomp](https://github.com/liolu/powerpuff-girls-z-decomp) | Matching decompilation of Powerpuff Girls Z (Nintendo DS) | 0 | 🟢 | C |
| [robogx](https://gitlab.com/Fexean/robogx) | Disassembly of Custom Robo GX (GBA) |  | ⚪ |  |
| [smbjr](https://gitlab.com/Fexean/smbjr) | Disassembly of Super Monkey Ball Jr. (GBA) |  | ⚪ |  |
| [Sonic Battle decomp](https://github.com/nicklesimba/sonic-battle-decomp) | Matching decompilation of Sonic Battle (GBA, USA Rev 0) | 0 | 🟢 | C |
| [The Urbz: Sims in the City decomp](https://github.com/baker339/urbz-re) | Decompilation of The Urbz: Sims in the City (Nintendo DS) | 0 | 🟢 | Python |
| [Tingle Tuner GBA client decomp](https://github.com/DMiller0090/tingle_tuner) | Matching decompilation of the Tingle Tuner GBA client from The Wind Waker | 0 | 🟢 | C |
| [ygowct06](https://github.com/testyourmine/ygowct06) | Disassembly of Yu-Gi-Oh! Ultimate Masters: World Championship Tournament 2006 (GBA, USA) | 0 | 🟢 | Assembly |

## Matching Decompilations — GameCube & Wii

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Super Smash Bros. Melee](https://github.com/doldecomp/melee) | Matching decompilation of Super Smash Bros. Melee (GameCube, 2001) | 2,440 | 🟢 | C |
| [Twilight Princess decomp](https://github.com/zeldaret/tp) | Decompilation of The Legend of Zelda: Twilight Princess | 2,110 | 🟢 | C++ |
| [ac-decomp](https://github.com/ACreTeam/ac-decomp) | Decompilation of Animal Crossing for GameCube | 1,425 | 🟢 | C |
| [Super Mario Galaxy](https://github.com/SMGCommunity/Petari) | Matching decompilation of Super Mario Galaxy (Wii, 2007) | 1,305 | 🟢 | C++ |
| [Wind Waker decomp](https://github.com/zeldaret/tww) | Decompilation of The Legend of Zelda: The Wind Waker | 1,128 | 🟢 | C++ |
| [Mario Party 4](https://github.com/mariopartyrd/marioparty4) | Matching decompilation of Mario Party 4 (GameCube, 2002) | 880 | 🟢 | C |
| [Mario Kart Wii (riidefi)](https://github.com/snailspeed3/mkw) | Decompilation of Mario Kart Wii (riidefi) | 476 | 🟡 | C |
| [Pikmin 2](https://github.com/projectPiki/pikmin2) | Matching decompilation of Pikmin 2 (GameCube, 2004) | 390 | 🟢 | C++ |
| [Super Mario Sunshine](https://github.com/doldecomp/sms) | Matching decompilation of Super Mario Sunshine (GameCube, 2002) | 369 | 🟢 | C++ |
| [re4 decomp](https://github.com/adonis-singh/re4) | Byte-identical decompilation of Resident Evil 4 (GameCube debug build) to C/C++ | 359 | 🟢 | C++ |
| [Pikmin](https://github.com/projectPiki/pikmin) | Matching decompilation of Pikmin (GameCube, 2001) | 327 | 🟢 | C |
| [Wii Menu](https://github.com/koopthekoopa/wii-ipl) | Decompilation of Wii Menu | 221 | 🟢 | C |
| [The Legend of Zelda: Skyward Sword](https://github.com/zeldaret/ss) | Matching decompilation of The Legend of Zelda: Skyward Sword (Wii, 2011) | 216 | 🟢 | C++ |
| [Mario Kart: Double Dash!!](https://github.com/doldecomp/mkdd) | Matching decompilation of Mario Kart: Double Dash!! (GameCube, 2003) | 206 | 🟢 | C++ |
| [SpongeBob SquarePants: Battle for Bikini Bottom](https://github.com/bfbbdecomp/bfbb) | Matching decompilation of SpongeBob SquarePants: Battle for Bikini Bottom (GameCube, 2003) | 195 | 🟢 | C++ |
| [Wii Sports](https://github.com/doldecomp/ogws) | Decompilation of Wii Sports | 179 | 🟢 | C |
| [Paper Mario: The Thousand-Year Door](https://github.com/doldecomp/ttyd) | Matching decompilation of Paper Mario: The Thousand-Year Door (GameCube, 2004) | 149 | 🟢 | C |
| [New Super Mario Bros. Wii](https://github.com/NSMBW-Community/NSMBW-Decomp) | Decompilation of New Super Mario Bros. Wii | 148 | 🟢 | C |
| [Xenoblade Chronicles](https://github.com/xbret/xenoblade) | Matching decompilation of Xenoblade Chronicles (Wii, 2010) | 148 | 🟢 | C |
| [Rock Band 3 decomp](https://github.com/DarkRTA/rb3) | Decompilation of Rock Band 3 (Wii) | 126 | 🟢 | C++ |
| [Super Smash Bros. Brawl](https://github.com/doldecomp/brawl) | Matching decompilation of Super Smash Bros. Brawl (Wii, 2008) | 108 | 🟢 | C |
| [Super Mario Strikers](https://github.com/yannicksuter/smstrikers-decomp) | Matching decompilation of Super Mario Strikers (GameCube, 2005) | 106 | 🟢 | C++ |
| [Super Paper Mario](https://github.com/SeekyCt/spm-decomp) | Matching decompilation of Super Paper Mario (Wii, 2007) | 104 | 🟢 | C |
| [SMGDecompilation](https://github.com/snailspeed3/SMGDecompilation) | Work-in-progress decompilation of Super Mario Galaxy | 97 | 🔴 | Assembly |
| [FRAY](https://github.com/PsiLupan/FRAY) | Recompilable Super Smash Bros. Melee 1.02 based on libOGC | 94 | 🔴 | C |
| [Kirby Air Ride (doldecomp)](https://github.com/doldecomp/kar) | Matching decompilation of Kirby Air Ride (GameCube, 2003) | 90 | 🟡 | Assembly |
| [Super Mario Galaxy 2](https://github.com/SMGCommunity/Garigari) | Matching decompilation of Super Mario Galaxy 2 (Wii, 2010) | 88 | 🟢 | C |
| [Star Fox Adventures](https://github.com/zcanann/SFA-Decomp) | Matching decompilation of Star Fox Adventures (GameCube, 2002) | 80 | 🟢 | C |
| [Pokémon Battle Revolution decomp](https://github.com/pret/pokerevo) | Decompilation of Pokémon Battle Revolution (Wii, PAL) | 77 | 🟡 | Assembly |
| [Paper Mario: The Thousand-Year Door decomp](https://github.com/NWPlayer123/PaperMario2) | Decompilation of Paper Mario: The Thousand-Year Door (GameCube) | 71 | 🔴 | C |
| [smb-decomp](https://github.com/camthesaxman/smb-decomp) | Decompilation of Super Monkey Ball | 64 | 🔴 | Assembly |
| [Mario Kart Wii](https://github.com/doldecomp/mkw) | Decompilation of Mario Kart Wii | 58 | 🟢 | C |
| [Kirby's Epic Yarn](https://github.com/Swiftshine/key) | Matching decompilation of Kirby's Epic Yarn (Wii, 2010) | 54 | 🟢 | C++ |
| [Animal Forest e+](https://github.com/ACreTeam/afe-decomp) | Matching decompilation of Animal Forest e+ (GameCube, 2003) | 53 | 🟢 | C |
| [Sonic Adventure DX](https://github.com/doldecomp/sadx) | Matching decompilation of Sonic Adventure DX (GameCube, 2003) | 51 | 🟡 | Python |
| [Final Fantasy Crystal Chronicles](https://github.com/zcanann/FFCC-Decomp) | Matching decompilation of Final Fantasy Crystal Chronicles (GameCube, 2003) | 46 | 🟢 | C |
| [New Super Mario Bros. U](https://github.com/aboood40091/red-pro2) | Matching decompilation of New Super Mario Bros. U (Wii U, 2012; v1.3.0) | 46 | 🟢 | C++ |
| [Pokémon XD: Gale of Darkness](https://github.com/TeamOrre/xd-decomp) | Matching decompilation of Pokémon XD: Gale of Darkness (GameCube, 2005) | 42 | 🟢 | C |
| [Mario Party 5](https://github.com/mariopartyrd/marioparty5) | Matching decompilation of Mario Party 5 (GameCube, 2003) | 41 | 🟢 | C |
| [Need for Speed: Underground](https://github.com/dbalatoni13/nfsug) | Matching decompilation of Need for Speed: Underground (GameCube, 2003) | 39 | 🟢 | C |
| [Sonic Riders](https://github.com/doldecomp/sonicriders) | Matching decompilation of Sonic Riders (GameCube, 2006) | 39 | 🔴 | Assembly |
| [Mario Strikers Charged](https://github.com/yannicksuter/mscharged-decomp) | Matching decompilation of Mario Strikers Charged (Wii, 2007) | 38 | 🟢 | C++ |
| [recvx-gc-decomp](https://github.com/fmil95/recvx-gc-decomp) | Decompilation of Resident Evil Code: Veronica X (GameCube) | 37 | 🟢 | C |
| [TY the Tasmanian Tiger](https://github.com/1superchip/ty-decomp) | Matching decompilation of TY the Tasmanian Tiger (GameCube, 2002) | 37 | 🟢 | C++ |
| [lm-decomp](https://github.com/ThePlayerRolo/lm-decomp) | Decompilation of Luigi's Mansion | 36 | 🗄️ | C |
| [Luigi's Mansion (zmansion)](https://github.com/Sage-of-Mirrors/zmansion) | Matching decompilation of Luigi's Mansion (GameCube, 2001) | 36 | 🟡 | C |
| [Sonic Heroes](https://github.com/Jovinull/sonicheroes) | Matching decompilation of Sonic Heroes (GameCube, 2003) | 33 | 🟢 | C++ |
| [dolsdk2001](https://github.com/doldecomp/dolsdk2001) | Decompilation of the 2001 Dolphin (GameCube) SDK libraries | 32 | 🟡 | C |
| [Phantasy Star Online Episode I & II Plus decomp](https://github.com/zeroz41/pso-decomp) | Decompilation of Phantasy Star Online Episode I & II Plus (GameCube) | 32 | 🟢 | C++ |
| [Mario Party 7](https://github.com/mariopartyrd/marioparty7) | Matching decompilation of Mario Party 7 (GameCube, 2005) | 31 | 🟢 | C |
| [Pokémon Colosseum](https://github.com/dougchansan/pkmn-colosseum) | Matching decompilation of Pokémon Colosseum (GameCube, 2003) | 31 | 🟢 | C |
| [The Legend of Zelda: The Wind Waker HD decomp](https://github.com/ZeldaWWHDDecomp/wwhd) | Decompilation of The Legend of Zelda: The Wind Waker HD (Wii U) | 31 | 🟢 | C++ |
| [Rhythm Heaven Fever](https://github.com/conhlee/rhf) | Matching decompilation of Rhythm Heaven Fever (Wii, 2011) | 29 | 🟢 | C++ |
| [Ratchet & Clank: Going Commando (USA v1.01)](https://github.com/OpenRAC/rac2-decomp) | Decompilation of Ratchet & Clank: Going Commando (USA v1.01) | 27 | 🟢 | C |
| [Star Fox Adventures (sfadebug)](https://github.com/RenaKunisaki/sfadebug) | Matching decompilation of Star Fox Adventures (GameCube, 2002; debug version) | 27 | 🟢 | C |
| [Eternal Darkness: Sanity's Requiem decomp](https://github.com/psdwizzard/Eternal-Darkness---Decompile) | Matching decompilation of Eternal Darkness: Sanity's Requiem (GameCube, GEDE01) | 26 | 🟢 | C |
| [Gauntlet: Dark Legacy](https://github.com/sabishii-bit/Gauntlet-Dark-Legacy-Decompilation) | Matching decompilation of Gauntlet: Dark Legacy (GameCube, 2001) | 26 | 🟢 | C |
| [Mario Party 6 (mariopartyrd)](https://github.com/mariopartyrd/marioparty6) | Matching decompilation of Mario Party 6 (GameCube, 2004) | 26 | 🟢 | C |
| [Mario Party 8](https://github.com/mariopartyrd/marioparty8) | Matching decompilation of Mario Party 8 (Wii, 2007) | 26 | 🟢 | Python |
| [Metal Gear Solid: The Twin Snakes decomp](https://github.com/GirianSeed/mgstts) | Decompilation of Metal Gear Solid: The Twin Snakes (GameCube) | 26 | 🟢 | C |
| [Pokémon Battle Revolution](https://github.com/pbr-ret/pbr-decomp) | Matching decompilation of Pokémon Battle Revolution (Wii, 2006) | 26 | 🟢 | C |
| [Naruto: Gekitō Ninja Taisen! 4](https://github.com/doldecomp/gnt4) | Matching decompilation of Naruto: Gekitō Ninja Taisen! 4 (GameCube, 2005) | 25 | 🔴 | Assembly |
| [The SpongeBob SquarePants Movie](https://github.com/bfbbdecomp/tssm) | Matching decompilation of The SpongeBob SquarePants Movie (GameCube, 2004) | 25 | 🟢 | C++ |
| [Forecast Channel (Wii)](https://github.com/doldecomp/forecast) | Decompilation of Forecast Channel (Wii) | 24 | 🟢 | C |
| [Harvest Moon: A Wonderful Life](https://github.com/ChrisNonyminus/hmawl) | Matching decompilation of Harvest Moon: A Wonderful Life (GameCube, 2003) | 24 | 🔴 | Assembly |
| [Mario Party 9 (mariopartyrd)](https://github.com/mariopartyrd/marioparty9) | Matching decompilation of Mario Party 9 (Wii, 2012) | 24 | 🟡 | C |
| [The Incredibles](https://github.com/seilc/incredibles) | Matching decompilation of The Incredibles (GameCube, 2004) | 24 | 🟢 | C |
| [The Sims 2 (GameCube)](https://github.com/natebag/Sims2DECOMP) | Decompilation of The Sims 2 (GameCube) | 23 | 🟢 | C++ |
| [New Play Control! Pikmin 2](https://github.com/projectPiki/pik2wii) | Matching decompilation of New Play Control! Pikmin 2 (Wii, 2009) | 22 | 🟢 | C++ |
| [open_rvl](https://github.com/kiwi515/open_rvl) | Decompilation of the Wii RVL SDK | 22 | 🗄️ | C |
| [LEGO Star Wars III: The Clone Wars (Wii)](https://github.com/ThePlayerRolo/LegoCloneWarsWii) | Decompilation of LEGO Star Wars III: The Clone Wars (Wii) | 21 | 🟢 | C |
| [Wii Virtual Console N64 emulator used disassembly](https://github.com/nim-ka/vc64-decomp) | Disassembly of the Wii Virtual Console N64 emulator used by Ocarina of Time | 21 | 🟡 | Assembly |
| [main DOL of Super Mario Sunshine disassembly](https://github.com/JimB16/SMS) | Disassembly of the main DOL of Super Mario Sunshine (GameCube) | 20 | 🔴 | Assembly |
| [Mario Kart Wii disassembly](https://github.com/aplumafreak500/DisMKW) | pret-style disassembly of Mario Kart Wii (Wii) | 20 | 🔴 | Assembly |
| [Splatoon decomp](https://github.com/sdlfoundation/splatoon-decomp) | Decompilation of Splatoon (Wii U) | 20 | 🟡 | Lua |
| [April 2004 Dolphin SDK libraries decomp](https://github.com/doldecomp/dolsdk2004) | Decompilation of the April 2004 Dolphin SDK libraries (GameCube) | 19 | 🟡 | C |
| [Hagi (GameCube/Wii emulator in Super Mario 3D All-Stars)](https://github.com/GRAnimated/Hagi) | Decompilation of Hagi (GameCube/Wii emulator in Super Mario 3D All-Stars) | 18 | 🟢 | C |
| [Splatoon](https://github.com/Dexx-io/Splatoon-Decomp) | Matching decompilation of Splatoon (Wii U, 2015) | 18 | 🟡 |  |
| [The Legend of Zelda: Twilight Princess](https://github.com/BgbrhrWatchinOVO/dusklight-ps4) | Decompilation of The Legend of Zelda: Twilight Princess (GameCube) | 18 | 🟢 | Python |
| [The Sims 2: Castaway](https://github.com/HaydnTrigg/Castaway) | Matching decompilation of The Sims 2: Castaway (Wii, 2007) | 18 | 🟢 | C |
| [Tiger Woods PGA Tour 2004](https://github.com/mitsevox/tw2004) | Matching decompilation of Tiger Woods PGA Tour 2004 (GameCube, 2003) | 18 | 🟢 | C |
| [Crash Bandicoot: The Wrath of Cortex (GameCube)](https://github.com/denzi-gh/crashwoc-decomp-gc) | Decompilation of Crash Bandicoot: The Wrath of Cortex (GameCube) | 17 | 🟢 | C |
| [Disney's Piglet's Big Game](https://github.com/tgsm/pbg) | Matching decompilation of Disney's Piglet's Big Game (GameCube, 2003) | 17 | 🟢 | C |
| [PokéPark Wii: Pikachu's Adventure](https://github.com/SephDB/pokepark-wii-decomp) | Decompilation of PokéPark Wii: Pikachu's Adventure | 17 | 🟢 | C |
| [RFL decomp](https://github.com/koopthekoopa/RFL) | Decompilation of RFL, the Mii library used in Wii games | 17 | 🟢 | C |
| [Skies of Arcadia Legends](https://github.com/Rainchus/SkiesOfArcadiaLegends) | Matching decompilation of Skies of Arcadia Legends (GameCube, 2002) | 17 | 🟡 | Python |
| [Crash Tag Team Racing](https://github.com/bluisblu/cttr) | Matching decompilation of Crash Tag Team Racing (GameCube, 2005) | 16 | 🟢 | C |
| [F-Zero GX (alt)](https://github.com/karamzov123/fzero-gx-decomp) | Matching decompilation of F-Zero GX (GameCube, 2003) | 16 | 🟢 | C |
| [Inazuma Eleven Strikers](https://github.com/SwareJonge/IEStrikers) | Matching decompilation of Inazuma Eleven Strikers (Wii, 2012) | 16 | 🟡 | C |
| [Mario Superstar Baseball (dtk)](https://github.com/roeming/mssb-dtk) | Matching decompilation of Mario Superstar Baseball (GameCube, 2005) | 16 | 🟢 | C |
| [Mortal Kombat: Deception](https://github.com/ShulkMaster/mk-deception) | Matching decompilation of Mortal Kombat: Deception (GameCube, 2004) | 16 | 🟢 | C |
| [Ratatouille January 2006 prototype decomp](https://github.com/seilc/rat) | Decompilation of the Ratatouille January 2006 prototype (GameCube) | 16 | 🟢 | C |
| [Sonic Adventure 2: Battle](https://github.com/roeming/SA2B) | Matching decompilation of Sonic Adventure 2: Battle (GameCube, 2001) | 16 | 🟢 | C |
| [Tom and Jerry in War of the Whiskers decomp](https://github.com/cohaereo/wotwdecomp) | Decompilation of Tom and Jerry in War of the Whiskers (GameCube) | 16 | 🟡 | Assembly |
| [Wii Play](https://github.com/akiramusic000/Rhae) | Decompilation of Wii Play | 16 | 🟢 | C |
| [Sonic Riders: Zero Gravity](https://github.com/KidWizardOfTheWeb/SRZGDecomp) | Matching decompilation of Sonic Riders: Zero Gravity (Wii, 2008) | 15 | 🔴 | Assembly |
| [Alice in Wonderland (2010)](https://github.com/Alice-2010/Decomp) | Matching decompilation of Alice in Wonderland (Wii, 2010) | 14 | 🟢 | C |
| [Kirby's Dream Collection Special Edition](https://github.com/Swiftshine/kdc) | Matching decompilation of Kirby's Dream Collection Special Edition (Wii, 2012) | 14 | 🟢 | C |
| [New Play Control! Pikmin](https://github.com/projectPiki/pik1wii) | Matching decompilation of New Play Control! Pikmin (Wii, 2008) | 14 | 🟢 | C |
| [Super Smash Bros. Brawl (BrawlModules)](https://github.com/Sammi-Husky/BrawlModules) | Experimental C++ reimplementation of Super Smash Bros. Brawl module (.rel) files (Wii) | 14 | 🟢 | Assembly |
| [Doshin the Giant](https://github.com/break-core/doshin-gc) | Decompilation of Doshin the Giant | 13 | 🟢 | Python |
| [Eft effects library decomp](https://github.com/open-ead/NW4F-Eft) | Decompilation of the Eft effects library from NintendoWare for Cafe (Wii U) | 13 | 🔴 | C++ |
| [Kirby's Return to Dream Land decomp](https://github.com/AP-NJA/KRTDL-Decomp) | Decompilation of Kirby's Return to Dream Land (Wii) | 13 | 🟢 | Assembly |
| [LEGO Star Wars: The Video Game decomp](https://github.com/ellierocks/lsw1-decomp) | Decompilation of LEGO Star Wars: The Video Game (GameCube) | 13 | 🟢 | Python |
| [Luigi's Mansion](https://github.com/SomeJakeGuy/lm-decomp) | Matching decompilation of Luigi's Mansion (GameCube, 2001) | 13 | 🟢 | C |
| [Sonic Riders Tournament Edition disassembly](https://github.com/RidersBoulevard/sonicriderste) | Disassembly and decompilation of Sonic Riders Tournament Edition (GameCube) | 12 | 🟢 | Assembly |
| [Mario Kart Wii decomp](https://github.com/vabold/mkw) | Decompilation of Mario Kart Wii (Wii) | 11 | 🟢 | C |
| [Need decomp](https://github.com/cobanov/nfsu2-decomp) | Matching decompilation of Need for Speed: Underground 2 (GameCube and PC) | 11 | 🟢 | Python |
| [Super Mario Sunshine](https://github.com/griches/PS5_Sunshine) | Decompilation of Super Mario Sunshine (GameCube) | 11 | 🟢 | C |
| [Digimon World 4](https://github.com/ivanno4317/dw4-gc) | Decompilation of Digimon World 4 | 10 | 🟢 | C |
| [EGG library used across Wii games decomp](https://github.com/vabold/EGG) | Decompilation of Nintendo's EGG library used across Wii games | 10 | 🟡 | Python |
| [F-Zero GX](https://github.com/rayanht/fzgx) | Matching decompilation of F-Zero GX (GameCube, 2003) | 10 | 🟢 | C |
| [GameCube tech demo NDDEMO decomp](https://github.com/cualquiercosa327/nddemo) | Decompilation of the GameCube tech demo NDDEMO | 10 | 🔴 | C++ |
| [Peach's Castle GameCube tech demo decomp](https://github.com/CelestialAmber/nddemo) | Decompilation of the Peach's Castle GameCube tech demo | 10 | 🟢 | Assembly |
| [Super Mario Sunshine decomp](https://github.com/QbeRoot/sms) | Decompilation of Super Mario Sunshine (GameCube) | 9 | 🗄️ | Assembly |
| [Yoshi's Woolly World](https://github.com/Swiftshine/yww) | Matching decompilation of Yoshi's Woolly World (Wii U, 2015) | 9 | 🟡 | C++ |
| [April 2001 Character Pipeline SDK component decomp](https://github.com/doldecomp/dolcp-apr2001) | Decompilation of the April 2001 Character Pipeline SDK component (GameCube) | 8 | 🟡 | C |
| [Eternal Darkness: Sanity's Requiem](https://github.com/PattyTrish/unending-occlusion) | Matching decompilation of Eternal Darkness: Sanity's Requiem (GameCube, 2002) | 8 | 🟢 | C |
| [Kirby Air Ride](https://github.com/wowjinxy/KAR) | Matching decompilation of Kirby Air Ride (GameCube, 2003) | 8 | 🟢 | C |
| [Medal of Honor: Frontline](https://github.com/kyleckroeger/moh-frontline-decomp) | Matching decompilation of Medal of Honor: Frontline (GameCube, 2002) | 8 | 🟢 | C |
| [Medal of Honor: Rising Sun](https://github.com/lifewillbeokay/moh-rising-sun) | Matching decompilation of Medal of Honor: Rising Sun (GameCube, 2003) | 8 | 🟢 | C |
| [Metrowerks CodeWarrior for GameCube (compiler)](https://github.com/rayanht/mwcc) | Decompilation of Metrowerks CodeWarrior for GameCube (compiler) | 8 | 🟢 | C |
| [Spyro: A Hero's Tail decomp](https://github.com/LivewireCB/Hero-s-Tail-Decomp) | Decompilation of Spyro: A Hero's Tail (GameCube and PS2) | 8 | 🟢 | C |
| [Summoner: A Goddess Reborn](https://github.com/Charlese2/sgr) | Matching decompilation of Summoner: A Goddess Reborn (GameCube, 2002) | 8 | 🟢 | C |
| [2001 Dolphin SDK libraries decomp](https://github.com/doldecomp/dolsdk2001-dec) | Decompilation of the 2001 Dolphin SDK libraries (GameCube) | 7 | 🟡 | C |
| [Big Brain Academy: Wii Degree](https://github.com/vabold/bba-wd) | Decompilation of Big Brain Academy: Wii Degree | 7 | 🟡 | Python |
| [Mario Party 6](https://github.com/iirg4x/marioparty6) | Matching decompilation of Mario Party 6 (GameCube, 2004) | 7 | 🟢 | C |
| [NFL Street 2](https://github.com/mitsevox/nflstreet2) | Matching decompilation of NFL Street 2 (GameCube, 2004) | 7 | 🟢 | C++ |
| [Super Mario Sunshine decomp](https://github.com/ryanbevins/Graffito-Decomp) | Matching decompilation of Super Mario Sunshine (GameCube, GMSJ01) | 7 | 🟢 | C++ |
| [Super Monkey Ball 2 decomp](https://github.com/ComplexPlane/libmkb) | Functionally matching embeddable decompilation of Super Monkey Ball 2 (GameCube) | 7 | 🔴 | C++ |
| [Wario World](https://github.com/sabishii-bit/wwdcmp) | Matching decompilation of Wario World (GameCube, 2003) | 7 | 🟡 | Assembly |
| [Donkey Kong Country Returns](https://github.com/Wexos/DKCR-Decompilation) | Matching decompilation of Donkey Kong Country Returns (Wii, 2010) | 6 | 🟡 | Python |
| [GameCube SocketLibrary decomp](https://github.com/Cuyler36/dolsocketlibrary) | Decompilation of the GameCube SocketLibrary | 6 | 🟢 | C |
| [Gyakuten Saiban 3 kiosk demo disassembly](https://github.com/atasro2/pwaa3demo) | Disassembly of the Gyakuten Saiban 3 kiosk demo (GameCube, Japan) | 6 | 🟢 | C |
| [Homeland](https://github.com/BttrDrgn/homeland) | Matching decompilation of HomeLand (GameCube, 2005) | 6 | 🔴 | Assembly |
| [Mario Superstar Baseball decomp](https://github.com/roeming/mssbDecomp) | Decompilation of Mario Superstar Baseball (GameCube) | 6 | 🟡 | C |
| [Nintendo Puzzle Collection: Dr. Mario 64](https://github.com/NewGBAXL/drmario64-gc) | Decompilation of Nintendo Puzzle Collection: Dr. Mario 64 | 6 | 🟢 | C |
| [Speed Racer disassembly](https://github.com/farisawan-2000/speedracer) | Disassembly and decompilation of Speed Racer (Wii) | 6 | 🔴 | Assembly |
| [Dragon Ball Z: Budokai 2](https://github.com/TotallyNotMichael-GH/dbz2) | Matching decompilation of Dragon Ball Z: Budokai 2 (GameCube, 2004) | 5 | 🟡 | Python |
| [G3d library decomp](https://github.com/nw4f/G3d) | Decompilation of the G3d library from NintendoWare for Cafe (Wii U) | 5 | 🟢 | C++ |
| [GameCube NetworkBasePackage library decomp](https://github.com/Cuyler36/dolnetbp) | Decompilation of the GameCube NetworkBasePackage library | 5 | 🟡 | C |
| [Sonic CD port decomp](https://github.com/Clownacy/Sonic-CD-Decompilation) | Decompilation of the Sonic CD port from Sonic Gems Collection (GameCube) | 5 | 🟢 | C |
| [Go Vacation](https://github.com/Moddimation/GoVacation-Decompilation) | Matching decompilation of Go Vacation (Wii, 2011) | 4 | 🗄️ | C |
| [Kirby Air Ride decomp](https://github.com/SeanMott/KAR-Decomp) | Decompilation of Kirby Air Ride (GameCube) | 4 | 🟢 | Assembly |
| [Shadow the Hedgehog decomp](https://github.com/dev-camo/shadow-decomp) | Decompilation of Shadow the Hedgehog (GameCube) | 4 | 🟢 | C |
| [Animal Crossing decomp](https://github.com/fraser125/Animal-Crossing-Decomp) | Decompilation of Animal Crossing (GameCube) | 3 | 🔴 | Assembly |
| [Dolphin SDK GX graphics library decomp](https://github.com/ogamespec/gx) | Decompilation of the Dolphin SDK GX graphics library (GameCube) | 3 | 🔴 | C |
| [Fortune Street](https://github.com/FortuneStreetModding/boom-street-decomp) | Matching decompilation of Fortune Street (Wii, 2011; Boom Street) | 3 | 🟡 | C |
| [Freedom Fighters](https://github.com/andresj-sanchez/frfi-decomp) | Matching decompilation of Freedom Fighters (GameCube, 2003) | 3 | 🟢 | Python |
| [GameCube Dolphin SDK libraries decomp](https://github.com/ogamespec/DolphinSDK_Decompile) | Decompilation of the GameCube Dolphin SDK libraries | 3 | 🔴 | C |
| [I Spy Spooky Mansion](https://github.com/AM7999/ISpy-SM-Decomp) | Decompilation of I Spy Spooky Mansion (Wii), based on the included debug executable | 3 | 🟡 | C++ |
| [Mario Party 9](https://github.com/ricky074game/marioparty9) | Matching decompilation of Mario Party 9 (Wii, 2012) | 3 | 🟢 | C++ |
| [Mario Sports Mix](https://github.com/EltyDev/MSM-decomp) | Matching decompilation of Mario Sports Mix (Wii, 2010) | 3 | 🟡 | Python |
| [MVP Baseball 2005](https://github.com/mitsevox/mvp2005) | Matching decompilation of MVP Baseball 2005 (GameCube, 2005) | 3 | 🟢 | C |
| [MVP Baseball 2005 decomp](https://github.com/ptitty12/mvp2005-decomp) | Matching decompilation of MVP Baseball 2005 (GameCube, GV4E69) | 3 | 🟢 | C++ |
| [Rayman 3: Hoodlum Havoc decomp](https://github.com/SplaatSites/rayman-3) | Decompilation of Rayman 3: Hoodlum Havoc (GameCube) | 3 | 🟢 | Python |
| [SSX 3 decomp](https://github.com/ssxdecomp/ssx3_gc) | Decompilation of SSX 3 (GameCube) | 3 | 🟡 | Python |
| [The Sims: Bustin' Out decomp](https://github.com/daftblazer/bustin-out-decomp) | Decompilation of The Sims: Bustin' Out (GameCube) | 3 | 🟢 | C++ |
| [Wii MotionPlus demo video player decomp](https://github.com/RootCubed/mpls_movie-decomp) | Decompilation of the Wii MotionPlus demo video player (Wii) | 3 | 🟢 | Python |
| [World of Goo (WiiWare)](https://github.com/Fancy2209/wog-wiiware) | Matching decompilation of World of Goo (Wii, 2008; WiiWare) | 3 | 🟡 | C++ |
| [Castlevania: The Adventure ReBirth decomp](https://github.com/dxgamer955/cvrebirth-decomp-and-pc-port) | Decompilation and PC port of Castlevania: The Adventure ReBirth (WiiWare) | 2 | 🟢 | C++ |
| [Chibi-Robo!](https://github.com/eavpsp/cbr_decomp) | Matching decompilation of Chibi-Robo! (GameCube, 2005) | 2 | 🟢 | C++ |
| [Excite Truck](https://github.com/orangedude27/excite-truck) | Matching decompilation of Excite Truck (Wii, 2006) | 2 | 🟢 | C |
| [Hot Wheels: Velocity X decomp](https://github.com/Duckxz/hwvx-gcn-decomp) | Decompilation of Hot Wheels: Velocity X (GameCube) | 2 | 🟢 | Python |
| [Little King's Story decomp](https://github.com/axiinyaa/lks_decomp) | Decompilation of Little King's Story (Wii, RO3EXJ) | 2 | 🟢 | C |
| [Mario Golf: Toadstool Tour decomp](https://github.com/MORImementos/mgtt-decomp) | Decompilation of Mario Golf: Toadstool Tour (GameCube) | 2 | 🔴 |  |
| [Radio Helicopter](https://github.com/Bsquo/pcopter_wii) | Decompilation of Radio Helicopter | 2 | 🟡 | C |
| [Shadow the Hedgehog decomp](https://github.com/2Balanced/Shadow-GC-Decomp) | Matching decompilation of Shadow the Hedgehog (GameCube, GUPE8P) | 2 | 🟢 | C++ |
| [Snd sound library decomp](https://github.com/nw4f/Snd) | Decompilation of the Snd sound library from NintendoWare for Cafe (Wii U) | 2 | 🟢 | C++ |
| [Super Mario All-Stars 25th Anniversary Edition](https://github.com/ThePlayerRolo/Super-Mario-All-Star-Decomp) | Matching decompilation of Super Mario All-Stars 25th Anniversary Edition (Wii, 2010) | 2 | 🟢 | C |
| [Sys library decomp](https://github.com/nw4f/Sys) | Decompilation of the Sys library from NintendoWare for Cafe (Wii U) | 2 | 🟢 | C++ |
| [Wii Fit Plus](https://github.com/Tanline666/veryfat-dungeon) | Decompilation of Wii Fit Plus | 2 | 🟢 | C |
| [a GameCube physics tech demo decomp](https://github.com/doldecomp/physdemo) | Decompilation of a GameCube physics tech demo | 1 | 🟢 | C |
| [a Sonic Riders: Zero Gravity Wii prototype decomp](https://github.com/bluisblu/SR2Wii) | Decompilation of a Sonic Riders: Zero Gravity Wii prototype | 1 | 🟢 | Python |
| [a Wii U game decomp](https://github.com/giada0019/glam-bytes) | Public decompilation of a Wii U game | 1 | 🟡 | Roff |
| [Amazing Island](https://github.com/EltaleLibrarian/Amazing) | Matching decompilation of Amazing Island (GameCube, 2004) | 1 | 🟡 | Python |
| [boot menu of the Zelda: Ocarina of Time Master Quest disc decomp](https://github.com/Yanis002/MultiBootSystem) | Decompilation of the boot menu of the Zelda: Ocarina of Time Master Quest disc (GameCube) | 1 | 🟡 | C |
| [Club Penguin: Game Day! decomp](https://github.com/iRodNCP/gameday-decomp) | Decompilation of Club Penguin: Game Day! (Wii) | 1 | 🔴 | Assembly |
| [Dragon Ball Z: Budokai 2 decomp](https://github.com/TotallyNotMichael-GH/DBZ2_GC) | Decompilation of Dragon Ball Z: Budokai 2 (GameCube) | 1 | 🟡 | C |
| [GoldenEye: Rogue Agent decomp](https://github.com/ant0-blase/goldeneye-rag-decomp) | Byte-identical decompilation of GoldenEye: Rogue Agent (GameCube) | 1 | 🗄️ | Assembly |
| [Gradius ReBirth decomp](https://github.com/darkuni/gradius-rebirth-recomp) | Decompilation and recompilation of Gradius ReBirth (WiiWare) | 1 | 🟢 | C++ |
| [Kirby's Return to Dream Land decomp](https://github.com/Etrainquandt17/Whippy) | Decompilation of Kirby's Return to Dream Land (Wii) | 1 | 🟢 | C++ |
| [Mega Man 9 decomp](https://github.com/arceuss/mm9decomp) | Matching decompilation of Mega Man 9 (WiiWare) | 1 | 🟢 | C |
| [Mega Man X: Command Mission disassembly](https://github.com/Pyrochrome/mmcm-decomp) | Disassembly of Mega Man X: Command Mission (GameCube) | 1 | 🟡 | Python |
| [Monster Hunter Tri decomp](https://github.com/InusualZ/mhtri-decomp) | Decompilation of Monster Hunter Tri (Wii) | 1 | 🟢 | C++ |
| [Mortal Kombat: Deadly Alliance](https://github.com/ShulkMaster/mk-da) | Matching decompilation of Mortal Kombat: Deadly Alliance (GameCube, 2002) | 1 | 🟢 | C |
| [Paper Mario: The Thousand-Year Door decomp](https://github.com/Rainchus/ttyd-decomp-us) | Decompilation of Paper Mario: The Thousand-Year Door (GameCube, US) | 1 | 🔴 | Python |
| [Sukeban Shachou Rena Wii decomp](https://github.com/spaghettic/renawii) | Decompilation of Sukeban Shachou Rena Wii (Wii) | 1 | 🟢 | Python |
| [Super Monkey Ball 2 decomp](https://github.com/ComplexPlane/mkb2-decomp) | Decompilation of Super Monkey Ball 2 (GameCube) | 1 | 🟢 | Python |
| [Taiko no Tatsujin Wii: Ketteiban](https://github.com/CalebPancake/Taiko-No-Tatsujin-Wii-Ketteiban) | Decompilation of Taiko no Tatsujin Wii: Ketteiban | 1 | 🟡 |  |
| [The Legend of Zelda: Four Swords Adventures decomp](https://github.com/sh1ftmaker/fsa-decomp) | Decompilation of The Legend of Zelda: Four Swords Adventures (GameCube) | 1 | 🟢 | C |
| [Wario Land: Shake It!](https://github.com/Swiftshine/wlsi) | Matching decompilation of Wario Land: Shake It! (Wii, 2008) | 1 | 🟢 | C |
| [a Rayman Origins Wii prototype executable decomp](https://github.com/Fancy2209/RAY-Decomp) | Decompilation of a Rayman Origins Wii prototype executable | 0 | 🟢 | Python |
| [BIT.TRIP COMPLETE decomp](https://github.com/Fatih120/bittrip) | Decompilation of BIT.TRIP COMPLETE (Wii) | 0 | 🟢 | Python |
| [default.dol decomp](https://github.com/Francessco121/sfa-kiosk-default-dol) | Decompilation of the default.dol from the Star Fox Adventures kiosk demo (GameCube) | 0 | 🟢 | C |
| [Despicable Me: The Game decomp](https://github.com/SplaatSites/despicable-me) | Decompilation of Despicable Me: The Game (Wii, 2010) | 0 | 🟢 | Python |
| [Disney-Pixar Ratatouille decomp](https://github.com/Mhanna112-code/RatDecomp) | Decompilation of Disney-Pixar Ratatouille (GameCube, USA) | 0 | 🟢 | C++ |
| [F-Zero GX decomp](https://github.com/nkhoit/fzgx) | Matching decompilation of F-Zero GX (GameCube) | 0 | 🟢 | C |
| [Fortune Street disassembly](https://github.com/FortuneStreetModding/Disassembly) | Disassembly of Fortune Street (Wii) | 0 | 🗄️ |  |
| [Giftpia decomp](https://github.com/wowjinxy/GiftpiaDecomp) | Decompilation of Giftpia (GameCube) | 0 | 🟡 | Python |
| [Giftpia disassembly](https://github.com/BttrDrgn/giftpia) | Disassembly of Giftpia (GameCube) | 0 | 🔴 | Assembly |
| [Mario Party 6 decomp](https://github.com/cualquiercosa327/MarioParty6) | Documentation and decompilation of Mario Party 6 (GameCube) | 0 | 🔴 | C |
| [Mario Superstar Baseball](https://github.com/nlopez99/mssb-decomp) | Matching decompilation of Mario Superstar Baseball (GameCube, 2005) | 0 | 🟢 | C |
| [Mega Man Anniversary Collection decomp](https://github.com/bluisblu/megaman-anniversary) | Decompilation of Mega Man Anniversary Collection (GameCube) | 0 | 🟢 | Python |
| [Pokémon Colosseum decomp](https://github.com/grant-might/Colosseum_Decomp) | Decompilation of Pokémon Colosseum (GameCube) | 0 | 🟢 | C |
| [Pokémon XD: Gale of Darkness decomp](https://github.com/DonovanMontoya/pokemon-xd-decomp) | Matching decompilation of Pokémon XD: Gale of Darkness (GameCube) | 0 | 🟢 | C++ |
| [pso-gc](https://gitlab.com/mrb0nk500/pso-gc) | Decompilation of Phantasy Star Online Episode I & II for the GameCube |  | ⚪ |  |
| [Puyo Puyo!! 20th Anniversary decomp](https://github.com/Fatih120/puyo20th-rvl) | Decompilation of Puyo Puyo!! 20th Anniversary (Wii) | 0 | 🟢 | Python |
| [pyssg-decomp](https://codeberg.org/retreev/pyssg-decomp) | Work-in-progress decompilation of PangYa: Super Swing Golf (Wii) |  | ⚪ |  |
| [RenderWare 3.5 engine decomp](https://github.com/LivewireCB/RW-3.5_Decomp) | Decompilation of the RenderWare 3.5 engine for GameCube | 0 | 🟢 | C++ |
| [Skies of Arcadia Legends decomp](https://github.com/ogdanimal/SkiesOfArcadiaLegends-Decomp) | Matching decompilation of Skies of Arcadia Legends (GameCube) | 0 | 🟢 | Python |
| [Sonic-Riders-GC-Decompilation](https://github.com/Carlsonic/Sonic-Riders-GC-Decompilation) | Decompilation tooling and function index for Sonic Riders (GameCube) | 0 | 🟢 | Python |
| [splatoon-1-decomp-test](https://github.com/MicroG-mes/splatoon-1-decomp-test) | Decompilation and native PC port test of Splatoon (Wii U) | 0 | 🟢 | Python |
| [SpongeBob SquarePants: Creature decomp](https://github.com/LivewireCB/CFTKK-Decomp) | Decompilation of SpongeBob SquarePants: Creature from the Krusty Krab (GameCube) | 0 | 🟢 | Python |
| [SpongeBob's Truth or Square decomp](https://github.com/LivewireCB/TOS-Decomp) | Decompilation of SpongeBob's Truth or Square | 0 | 🟡 | C |
| [The Sims Bustin' Out decomp](https://github.com/Vivian-Green/sims-bustin-out) | Matching decompilation of The Sims Bustin' Out (GameCube) | 0 | 🟢 | Python |
| [The Urbz: Sims in the City decomp](https://github.com/samtaylorr/urbz-sims-decomp-gc) | Decompilation of The Urbz: Sims in the City (GameCube) | 0 | 🟢 | C |
| [Turbo: Super Stunt Squad decomp](https://github.com/ItsNiklas/tsss) | Decompilation of Turbo: Super Stunt Squad (Wii) | 0 | 🟢 | Python |
| [Wii News Channel decomp](https://github.com/hotlandsoftware/wii-news-channel) | Decompilation and PC port of the Wii News Channel | 0 | 🟢 | C |
| [WPSE01_DECOMP](https://github.com/emannotava/WPSE01_DECOMP) | Decompilation attempt of Pokémon Rumble (WiiWare, US) | 0 | 🟡 | Python |

## Matching Decompilations — Mobile

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Sonic CD (2011 mobile)](https://github.com/RSDKModding/RSDKv3-Decompilation) | Decompilation of Sonic CD (2011 remaster) and Retro Engine v3 (Mobile, 2011) | 712 | 🟢 | C++ |
| [NBCraft](https://github.com/nbcraft-org/nbcraft) | Cross-platform game based on a decompilation of Minecraft: Pocket Edition 0.1.3 (Android) | 597 | 🟢 | C++ |
| [Sonic Runners](https://github.com/itsmattkc/RunnersDecomp) | Matching decompilation of Sonic Runners (Mobile, 2015) | 246 | 🔴 | C# |
| [DoomRPG-RE](https://github.com/Erick194/DoomRPG-RE) | Reverse engineered source of Doom RPG | 161 | 🟡 | C |
| [Cut the Rope (Cut the Rope: DX)](https://github.com/yell0wsuit/cuttherope-dx) | Decompilation of Cut the Rope (Mobile) | 131 | 🟢 | C# |
| [DoomIIRPG-RE](https://github.com/Erick194/DoomIIRPG-RE) | Reverse engineered source of Doom II RPG | 100 | 🟡 | C++ |
| [PvZ-TV-Touch](https://github.com/WuDi-ZhanShen/PvZ-TV-Touch) | Decompiled Java source of Android Plants vs. Zombies TV edition, adapted for touch | 82 | 🟡 |  |
| [Angry Birds](https://github.com/jooapa/Angry_Birds_Decompilation) | Decompilation scripts and instructions for the six classic Angry Birds games (Mobile, 2009–2014) | 54 | 🟡 | Python |
| [BounceTales](https://github.com/HelloOO7/BounceTales) | Decompilation of Rovio's Bounce Tales (2008) for Nokia phones | 53 | 🔴 | Java |
| [Ultimate Mortal Kombat 3 decomp](https://github.com/MaryNCRT/Ultimate-Mortal-Kombat-3-iOS-Decompiled) | Decompilation of Ultimate Mortal Kombat 3 for iOS (EA Mobile, 2011) | 50 | 🟢 | C |
| [Geometry Dash](https://github.com/aloaf812/GD) | Decompilation of Geometry Dash v1.710 (Mobile, 2013) | 36 | 🟢 | C++ |
| [Sonic the Hedgehog (J2ME)](https://github.com/Iso-Kilo/Sonic-1-J2ME-Decompilation) | Matching decompilation of Sonic the Hedgehog (J2ME mobile, 2005) | 36 | 🔴 | Java |
| [Samurai vs Zombies Defense](https://github.com/Decomp-And-Recomp/Samurai-Vs-Zombies) | Decompilation of Samurai vs Zombies Defense by Glu (Mobile, 2012) | 27 | 🟢 | C# |
| [Samurai-Vs-Zombies-2](https://github.com/Decomp-And-Recomp/Samurai-Vs-Zombies-2) | Decompiled Samurai vs Zombies 2 mobile game made playable on PC | 25 | 🟢 | C# |
| [DiamondRushSource](https://github.com/kubikaugustyn/DiamondRushSource) | Decompilation of Gameloft's Diamond Rush (2006) for Nokia phones | 23 | 🟡 | Java |
| [Bounce decomp](https://github.com/rndtrash/nokia-bounce-decomp) | Decompiled and commented source of Bounce for Nokia J2ME phones | 19 | 🔴 | Java |
| [Brave Frontier](https://github.com/decompfrontier/client) | Decompilation of the Brave Frontier client (Mobile, 2013) | 16 | 🟡 | C |
| [Dragon Ball Legends](https://github.com/GodkuHacking/Dragon-Ball-Legends) | APK decompilation of Dragon Ball Legends (Mobile, 2018) | 16 | 🟡 | Smali |
| [N-Gage game Ashen decomp](https://github.com/nenikitov/ashen-decomp) | Reverse engineering of the N-Gage game Ashen | 16 | 🟢 | Rust |
| [SpongeBob Moves In!](https://github.com/Juanen100/SBMI-Decomp) | Decompilation of the Android client of SpongeBob Moves In! (Mobile, 2013) | 15 | 🟢 | C# |
| [Star-Warfare](https://github.com/Decomp-And-Recomp/Star-Warfare) | Decompiled Star Warfare mobile game by Triniti Interactive | 13 | 🟡 | C# |
| [Sonic The Hedgehog: Part One decomp](https://github.com/yowari/sonic-j2me-decompilation) | Decompilation of Sonic The Hedgehog: Part One for J2ME phones | 12 | 🟡 | Java |
| [Call-Of-Mini-Squad](https://github.com/Decomp-And-Recomp/Call-Of-Mini-Squad) | Decompiled Call of Mini: Squad mobile game | 11 | 🟢 | C# |
| [Diamond Rush](https://github.com/palaceswitcher/Diamond-Rush-Decomp) | Matching decompilation of Diamond Rush (J2ME mobile, 2006) | 11 | 🟢 | Java |
| [BejeweledLivePlusDecomp-MonoGame](https://github.com/bognarit80/BejeweledLivePlusDecomp-MonoGame) | Windows Phone 7 Bejeweled Live+ decompiled and ported to MonoGame | 9 | 🟡 | C# |
| [Call-of-Mini-Zombies](https://github.com/Decomp-And-Recomp/Call-of-Mini-Zombies) | Decompiled client of Call of Mini: Zombies 4.3.4 with PC support | 8 | 🟢 | C# |
| [Angry Birds 1.4.2 decomp](https://github.com/WhiteMsf/angry-birds-arm64) | ARM64 source reconstruction of Angry Birds 1.4.2 for Android | 7 | 🟢 | C++ |
| [digimon-linkz-client](https://github.com/astiob/digimon-linkz-client) | Decompiled client of the Digimon Linkz mobile game | 7 | 🔴 | C# |
| [Gameloft's Green Farm 3 decomp](https://github.com/IceburgLettuce17/Greenier-Farm-3-NEW) | Decompilation of Gameloft's Green Farm 3 for Samsung S8000 Jet phones | 7 | 🟢 | Java |
| [Call-Of-Mini-Dino-Hunter](https://github.com/Decomp-And-Recomp/Call-Of-Mini-Dino-Hunter) | Decompiled client of Call of Mini: Dino Hunter (mobile) | 6 | 🟡 | C# |
| [Idle Office Tycoon](https://github.com/Avenze/ios_reverse_engineering) | Reverse engineering notes and decompilation of the iOS game Idle Office Tycoon (Mobile) | 6 | 🟡 | Lua |
| [Minecraft Pocket Edition Lite decomp](https://github.com/Koichive/mcpelite-decomp) | Decompilation of Minecraft Pocket Edition Lite (Android) | 6 | 🗄️ | Java |
| [mobile release of Doki Doki Literature Club Plus decomp](https://github.com/HiroStuff/DDLC-Plus-Mobile) | Decompilation of the mobile release of Doki Doki Literature Club Plus | 6 | 🟢 | Ren'Py |
| [Ratchet & Clank: Going Mobile v1.1.0 decomp](https://github.com/Clank700/going-mobile-decomp) | Output-exact Java reconstruction of Ratchet & Clank: Going Mobile v1.1.0 (J2ME) | 5 | 🟢 | Java |
| [Rovio Mobile's version of the KA3D engine decomp](https://github.com/RebirdEngineering/Fusion) | Decompilation of Rovio Mobile's version of the KA3D engine (Angry Birds) | 5 | 🟢 | C++ |
| [Teeter](https://github.com/honoz/Teeter) | Rebuilt version of HTC's Teeter maze ball game based on its decompiled code (Android) | 5 | 🟢 | Kotlin |
| [Zombie Farm mobile game decomp](https://github.com/jeb495/Zombie-Farm-Decompiled) | Decompiled source of the Zombie Farm mobile game | 5 | 🔴 |  |
| [first version of Geometry Dash decomp](https://github.com/CallocGD/GD-1.0-Decompiled) | Decompilation of the first version of Geometry Dash | 4 | 🟡 | Zeek |
| [Flappy Bird](https://github.com/fr3dsp/FlappyBird-Decomp) | Decompilation of Flappy Bird (Windows Phone, 2013) | 4 | 🟢 | C# |
| [Skylanders: Cloud Patrol](https://github.com/spyrosadventure/cloud-patrol-decomp) | Decompilation of Skylanders: Cloud Patrol (Mobile, 2012) | 4 | 🟡 | C# |
| [Sonic Dream Team v1.1.2 decomp](https://github.com/icecapdx/SDreamTeam-Git) | Decompilation of Sonic Dream Team v1.1.2 (Apple Arcade) | 4 | 🟢 | C |
| [Zombieville-USA-2](https://github.com/Decomp-And-Recomp/Zombieville-USA-2) | Decompiled Zombieville USA 2 mobile game made playable on PC | 4 | 🟡 | C# |
| [2011 Android game Apparatus decomp](https://github.com/rollerozxa/apparatus-decomp) | Decompilation of the 2011 Android game Apparatus | 3 | 🟢 | Java |
| [Bounce](https://github.com/misterjdrg/Bouncer) | Decompilation of Bounce (J2ME mobile, 2001) | 3 | 🟡 | Java |
| [Fast Future Race decomp](https://github.com/Katamaran21/ffrace-decomp) | Decompilation and C/SDL2 port of Fast Future Race (Windows Mobile / Pocket PC) | 3 | 🟢 | C |
| [JumpyBall reimplementation](https://github.com/Katamaran21/jumpyball-decomp) | Decompilation and C/SDL2 reimplementation of JumpyBall (Pocket PC) | 3 | 🟢 | C |
| [Ancient Empires](https://github.com/Atomk/ancient-empires-1-decompilation) | Matching decompilation of Ancient Empires (J2ME mobile, 2004) | 2 | 🟡 | Java |
| [Bloons TD 4 v3.6.1 decomp](https://github.com/polavux/BTD4MobileDecomp) | Decompilation of Bloons TD 4 v3.6.1 (iOS) | 2 | 🟢 | Objective-C++ |
| [Defenders & Dragons](https://github.com/Lindarychwalski/Defenders-Dragons) | Decompilation of Defenders & Dragons by Glu (Mobile) | 2 | 🟡 |  |
| [Five Nights at Freddy's](https://github.com/fr3dsp/FNaF-Decomp) | Decompilation of Five Nights at Freddy's (Windows Phone, 2014) | 2 | 🟢 | C# |
| [Five Nights at Freddy's 2](https://github.com/fr3dsp/FNaF-2-Decomp) | Decompilation of Five Nights at Freddy's 2 (Windows Phone, 2014) | 2 | 🟢 | C# |
| [Green Farm 3](https://github.com/SmithGoll/Greenier-Farm-3-Decomp) | Non-matching decompilation of Gameloft's Green Farm 3 (J2ME mobile) | 2 | 🟡 | Java |
| [Hybrid Animals mobile game decomp](https://github.com/Segually/HADecompiled) | Decompilation of the Hybrid Animals mobile game | 2 | 🟢 | C# |
| [Mixels Rush](https://github.com/Nugetinc/MixelsRushDecompilation) | Experimental decompilation of Mixels Rush (Mobile, 2015) | 2 | 🟡 |  |
| [a lost beta of Big Bang Racing decomp](https://github.com/Dodonickey/WOE-Decompiled) | Decompilation of a lost beta of Big Bang Racing by Traplight (mobile) | 1 | 🟢 | C# |
| [Chernobyl Neighbor: Clown Gang](https://github.com/smolkrieger/nuclear-neighbor) | Decompilation of Chernobyl Neighbor: Clown Gang | 1 | 🟡 |  |
| [Chiki's Chase](https://github.com/gays-studio/ChikisChaseAPK) | Decompiled (apktool) Android build of Chiki's Chase (Mobile) | 1 | 🟡 | Smali |
| [Disney's Where's My Water? decomp](https://github.com/Mahooked/wmw-decomp) | Decompilation of Disney's Where's My Water? (Android 1.18.9) | 1 | 🟢 | C++ |
| [Geometry Dash 2.2 decomp](https://github.com/apersonwhomakesstuff/GD-2.2-Android-DECOMP) | Decompilation of Geometry Dash 2.2 (Android) | 1 | 🟢 | C++ |
| [mobile-eggbert-legacy](https://github.com/openeggbert/mobile-eggbert-legacy) | C# MonoGame code of Mobile Eggbert (Speedy Blupi) decompiled from the 2013 Windows Phone release | 1 | 🟢 | C# |
| [The Blockheads mobile game decomp](https://github.com/noxthewildshadow/TheBlockheads-Source-Reconstruction) | Source reconstruction of The Blockheads mobile game | 1 | 🗄️ | Objective-C |
| [a lost beta of The Great Escape decomp](https://github.com/Dodonickey/The-Great-Escape-Decomp) | Decompilation of a lost beta of The Great Escape by Traplight Games (mobile) | 0 | 🟢 | C# |
| [Attack Breaker Pro decomp](https://github.com/rollerozxa/attack-breaker-pro) | Decompilation of Attack Breaker Pro (mobile) | 0 | 🟡 | Java |
| [Battle Bears Gold decomp](https://github.com/Virjoinga/Battle-Bears-Gold-Decomp) | Decompilation of Battle Bears Gold (mobile) | 0 | 🗄️ | C# |
| [Gameloft's Gangstar: West Coast Hustle decomp](https://github.com/Virjoinga/gangstar-wch-decomp) | Decompilation of Gameloft's Gangstar: West Coast Hustle (Android, 2013) | 0 | 🟢 | Assembly |
| [Gameloft's Rayman Kart decomp](https://github.com/IceburgLettuce17/RayKart) | Decompilation of Gameloft's Rayman Kart (J2ME) | 0 | 🟡 | Java |
| [iSniper-Arctic-Warfare](https://github.com/Decomp-And-Recomp/iSniper-Arctic-Warfare) | Decompiled iSniper: Arctic Warfare mobile game by Triniti Interactive | 0 | 🟢 | C# |
| [Pea Shootin' Pete decomp](https://github.com/bImPatman/pea-shootin-pete-decomp) | Matching decompilation of Pea Shootin' Pete (mobile) | 0 | 🟢 | Python |
| [PREDATORS](https://github.com/Decomp-And-Recomp/PREDATORS) | Decompiled PREDATORS mobile game (2010, Angry Mob Games) | 0 | 🟢 | C# |
| [Smash-Hit-Decomp](https://codeberg.org/Shards/Smash-Hit-Decomp) | Decompilation of the mobile game Smash Hit |  | ⚪ |  |
| [Super Cat Tales: PAWS](https://codeberg.org/heathercat123/PAWS-Decomp) | Decompilation of Super Cat Tales: PAWS (Mobile) |  | ⚪ |  |
| [Tiny-Legends-Crazy-Knight](https://github.com/Decomp-And-Recomp/Tiny-Legends-Crazy-Knight) | Decompiled Tiny Legends: Crazy Knight mobile game | 0 | 🟢 | GLSL |

## Matching Decompilations — Nintendo 64

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Super Mario 64 decomp](https://github.com/n64decomp/sm64) | Matching decompilation of Super Mario 64 | 8,929 | 🟡 | C |
| [Ocarina of Time decomp](https://github.com/zeldaret/oot) | Decompilation of The Legend of Zelda: Ocarina of Time | 5,620 | 🟢 | C |
| [Perfect Dark PC port](https://github.com/perfect-dark-pc-port/perfect_dark) | Port of the Perfect Dark N64 decompilation to modern platforms | 2,081 | 🟢 | C |
| [Majora's Mask decomp](https://github.com/zeldaret/mm) | Decompilation of The Legend of Zelda: Majora's Mask | 1,760 | 🟢 | C |
| [Paper Mario](https://github.com/pmret/papermario) | Matching decompilation of Paper Mario (Nintendo 64, 2000) | 1,638 | 🟢 | C |
| [Mario Kart 64](https://github.com/n64decomp/mk64) | Matching decompilation of Mario Kart 64 (Nintendo 64, 1996) | 1,315 | 🟢 | C |
| [Perfect Dark decompilation (n64decomp)](https://github.com/n64decomp/perfect_dark) | Matching decompilation of Perfect Dark (N64) | 876 | 🟡 | C |
| [GoldenEye 007 decomp](https://github.com/n64decomp/007) | Matching decompilation of GoldenEye 007 | 805 | 🟢 | C |
| [banjo-kazooie](https://github.com/n64decomp/banjo-kazooie) | Decompilation of Banjo-Kazooie | 659 | 🟢 | C |
| [HackerSM64](https://github.com/HackerN64/HackerSM64) | Super Mario 64 decompilation fork tuned for romhacking | 540 | 🟢 | C |
| [Diddy Kong Racing](https://github.com/DavidSM64/Diddy-Kong-Racing) | Matching decompilation of Diddy Kong Racing (Nintendo 64, 1997) | 424 | 🟢 | C |
| [Star Fox 64](https://github.com/sonicdcer/sf64) | Matching decompilation of Star Fox 64 (Nintendo 64, 1997) | 355 | 🟢 | C |
| [Animal Forest](https://github.com/zeldaret/af) | Matching decompilation of Animal Forest (Nintendo 64, 2001) | 303 | 🟢 | C |
| [oot](https://github.com/n64decomp/oot) | Decompilation of Ocarina of Time Master Quest debug build | 285 | 🗄️ | Assembly |
| [Duke Nukem: Zero Hour](https://github.com/Gillou68310/DukeNukemZeroHour) | Matching decompilation of Duke Nukem: Zero Hour (Nintendo 64, 1999) | 277 | 🟢 | C |
| [Super Smash Bros.](https://github.com/VetriTheRetri/ssb-decomp-re) | Matching decompilation of Super Smash Bros. (Nintendo 64, 1999) | 271 | 🟢 | C |
| [Conker's Bad Fur Day (mkst)](https://github.com/mkst/conker) | Matching decompilation of Conker's Bad Fur Day (Nintendo 64, 2001) | 239 | 🗄️ | C |
| [Doom 64 (DOOM64-RE)](https://github.com/Erick194/DOOM64-RE) | Reverse-engineered source of Doom 64 (Nintendo 64, 1997) | 237 | 🟡 | C |
| [Kirby 64: The Crystal Shards](https://github.com/Kirby64Ret/kirby64) | Matching decompilation of Kirby 64: The Crystal Shards (Nintendo 64, 2000) | 235 | 🟢 | C |
| [Harvest Moon 64](https://github.com/harvestwhisperer/hm64-decomp) | Matching decompilation of Harvest Moon 64 (Nintendo 64, 1999) | 224 | 🟢 | C |
| [Dinosaur Planet](https://github.com/zestydevy/dinosaur-planet) | Matching decompilation of Dinosaur Planet (Nintendo 64, unreleased 2000 build) | 218 | 🟢 | C |
| [Pokémon Stadium](https://github.com/pret/pokestadium) | Matching decompilation of Pokémon Stadium (Nintendo 64, 1999) | 213 | 🟢 | C |
| [Snowboard Kids 2](https://github.com/cdlewis/snowboardkids2-decomp) | Matching decompilation of Snowboard Kids 2 (Nintendo 64, 1999) | 196 | 🟢 | C |
| [libreultra](https://github.com/n64decomp/libreultra) | Matching decompilation of the N64 libultra SDK library | 185 | 🔴 | C |
| [Banjo-Tooie](https://github.com/Mr-Wiseguy/banjo-tooie) | Matching decompilation of Banjo-Tooie (Nintendo 64, 2000) | 152 | 🟢 | C |
| [N64 Emulator for GameCube (OoT Master Quest)](https://github.com/zeldaret/oot-gc) | Decompilation of N64 Emulator for GameCube (OoT Master Quest) | 150 | 🟡 | C |
| [sdk-tools](https://github.com/n64decomp/sdk-tools) | Decompilation of the Nintendo 64 SDK developer tools | 147 | 🔴 | C |
| [majora](https://github.com/n64decomp/majora) | Decompilation of The Legend of Zelda: Majora's Mask | 138 | 🗄️ | C |
| [Wave Race 64](https://github.com/LLONSIT/Wave-Race-64) | Matching decompilation of Wave Race 64 (Nintendo 64, 1996) | 111 | 🟢 | Assembly |
| [F-Zero X](https://github.com/inspectredc/fzerox) | Matching decompilation of F-Zero X (Nintendo 64, 1998) | 109 | 🟢 | C |
| [N64 Emulator for Wii (OoT Virtual Console)](https://github.com/zeldaret/oot-vc) | Decompilation of N64 Emulator for Wii (OoT Virtual Console) | 96 | 🟢 | C |
| [HackerOoT](https://github.com/HackerN64/HackerOoT) | Ocarina of Time decompilation fork tuned for romhacking | 93 | 🟢 | C |
| [Mario Party](https://github.com/mariopartyrd/marioparty) | Matching decompilation of Mario Party (Nintendo 64, 1998) | 84 | 🟢 | C |
| [Pilotwings 64](https://github.com/n64decomp/pw64) | Matching decompilation of Pilotwings 64 (Nintendo 64, 1996) | 83 | 🟢 | C |
| [Yoshi's Story](https://github.com/decompals/yoshis-story) | Matching decompilation of Yoshi's Story (Nintendo 64, 1997) | 82 | 🟢 | C |
| [Dr. Mario 64](https://github.com/AngheloAlf/drmario64) | Matching decompilation of Dr. Mario 64 (Nintendo 64, 2001) | 81 | 🟢 | C |
| [Mario Party 3](https://github.com/mariopartyrd/marioparty3) | Matching decompilation of Mario Party 3 (Nintendo 64, 2000) | 76 | 🟢 | C |
| [Mischief Makers](https://github.com/Drahsid/mischief-makers) | Matching decompilation of Mischief Makers (Nintendo 64, 1997) | 72 | 🟢 | C |
| [ultralib](https://github.com/decompals/ultralib) | Reverse engineering of the N64 libultra library | 68 | 🟢 | C |
| [Castlevania 64](https://github.com/k64ret/cv64) | Matching decompilation of Castlevania 64 (Nintendo 64, 1999) | 67 | 🟢 | C |
| [Space Station Silicon Valley](https://github.com/mkst/sssv) | Matching decompilation of Space Station Silicon Valley (Nintendo 64, 1998) | 66 | 🟢 | C |
| [Bomberman Hero](https://github.com/Bomberhackers/bmhero) | Matching decompilation of Bomberman Hero (Nintendo 64, 1998) | 62 | 🟢 | C |
| [Pokémon Stadium 2](https://github.com/pret/pokestadiumgs) | Matching decompilation of Pokémon Stadium 2 (Nintendo 64, 2000) | 60 | 🟢 | C |
| [Snowboard Kids](https://github.com/cdlewis/snowboardkids-decomp) | Matching decompilation of Snowboard Kids (Nintendo 64, 1997) | 58 | 🟢 | C |
| [Jet Force Gemini](https://github.com/Ryan-Myers/Jet-Force-Gemini) | Matching decompilation of Jet Force Gemini (Nintendo 64, 1999) | 56 | 🟢 | C |
| [Mario Party 2](https://github.com/mariopartyrd/marioparty2) | Matching decompilation of Mario Party 2 (Nintendo 64, 1999) | 55 | 🟢 | C |
| [f3dex2](https://github.com/Mr-Wiseguy/f3dex2) | Matching, mostly documented disassemblies of the F3DEX2/F3DZEX2 N64 RSP microcode | 50 | 🟢 | C |
| [mp3](https://github.com/PartyPlanner64/mp3) | Mario Party 3 decompilation | 47 | 🗄️ | C |
| [Body Harvest](https://github.com/jaytheham/body-harvest-decompilation) | Matching decompilation of Body Harvest (Nintendo 64, 1998) | 46 | 🟢 | C |
| [mariokart64](https://github.com/RenaKunisaki/mariokart64) | Mario Kart 64 disassembly, hacking notes and research | 46 | 🔴 | Assembly |
| [Rocket: Robot on Wheels](https://github.com/RocketRet/Rocket-Robot-On-Wheels) | Matching decompilation of Rocket: Robot on Wheels (Nintendo 64, 1999) | 46 | 🔴 | C |
| [zelda_ocarina_mq_debug](https://github.com/camthesaxman/zelda_ocarina_mq_debug) | Disassembly of The Legend of Zelda: Ocarina of Time Master Quest debug build (N64/GameCube) | 45 | 🔴 | Assembly |
| [Aidyn Chronicles](https://github.com/blackgamma7/Aidyn) | Matching decompilation of Aidyn Chronicles: The First Mage (Nintendo 64, 2001) | 42 | 🟢 | C++ |
| [Pokémon Puzzle League](https://github.com/AngheloAlf/puzzleleague64) | Matching decompilation of Pokémon Puzzle League (Nintendo 64, 1999) | 42 | 🟢 | C |
| [Bomberman 64](https://github.com/Bomberhackers/bm64) | Matching decompilation of Bomberman 64 (Nintendo 64, 1997) | 35 | 🟢 | C |
| [AeroGauge](https://github.com/LLONSIT/AeroGauge) | Matching decompilation of AeroGauge (Nintendo 64, 1997) | 32 | 🟢 | C |
| [Conker's Bad Fur Day](https://github.com/DevOldSchool/conkers-bfd-decomp) | Matching decompilation of Conker's Bad Fur Day (Nintendo 64, 2001) | 32 | 🟢 | Python |
| [F-Zero X (Expansion Kit)](https://github.com/inspectredc/fzerox-expansion-kit) | Matching decompilation of F-Zero X Expansion Kit (Nintendo 64, 2000) | 31 | 🟢 | C |
| [Gauntlet Legends](https://github.com/Drahsid/gauntlet-legends) | Matching decompilation of Gauntlet Legends (Nintendo 64, 1999) | 29 | 🟢 | C |
| [Virtual Pro Wrestling 2](https://github.com/AKI-Club/vpw2) | Matching decompilation of Virtual Pro Wrestling 2 (Nintendo 64, 2000) | 29 | 🟢 | Assembly |
| [Gex: Enter the Gecko (N64)](https://github.com/MatBourgon/Gex64Decomp) | Decompilation of Gex: Enter the Gecko (N64) | 28 | 🟢 | C |
| [sbk-decomp](https://github.com/tenry92/sbk-decomp) | Snowboard Kids decompilation | 28 | 🔴 | C |
| [PaperMarioDecompilation](https://github.com/RetroReversing/PaperMarioDecompilation) | Early decompilation project for Paper Mario (N64) | 26 | 🔴 | Assembly |
| [Turok 3: Shadow of Oblivion](https://github.com/Drahsid/turok3) | Matching decompilation of Turok 3: Shadow of Oblivion (Nintendo 64, 2000) | 26 | 🗄️ | C |
| [Mario Golf (N64)](https://github.com/monde-lointain/mariogolf64) | Decompilation of Mario Golf (N64) | 25 | 🟢 | C |
| [bomberman-64](https://github.com/MarioMaster96/bomberman-64) | Bomberman 64 decompilation | 23 | 🔴 | Assembly |
| [Star Wars: Shadows of the Empire](https://github.com/EltaleLibrarian/SotE) | Matching decompilation of Star Wars: Shadows of the Empire (Nintendo 64, 1996) | 22 | 🟡 | C |
| [Super Mario 64 (sm64-decomp)](https://github.com/justinwash/sm64-decomp) | Decompilation of Super Mario 64 (N64) | 22 | 🔴 | Assembly |
| [Superman 64](https://github.com/farisawan-2000/superman) | Matching decompilation of Superman 64 (Nintendo 64, 1999) | 22 | 🔴 | Assembly |
| [n64dd](https://github.com/Decompollaborate/n64dd) | Decompilation of the n64dd file in Ocarina of Time | 20 | 🟡 | C |
| [Star Wars: Rogue Squadron](https://github.com/Tmcg2/rogue_squadron64) | Matching decompilation of Star Wars: Rogue Squadron (Nintendo 64, 1998) | 20 | 🟢 | C |
| [Duke Nukem 64](https://github.com/NBlood/Duke64-RE) | Matching decompilation of Duke Nukem 64 (Nintendo 64, 1997) | 19 | 🟡 | C |
| [1080° Snowboarding decomp](https://github.com/djsaunde/1080-decomp) | Decompilation of 1080° Snowboarding (N64) | 18 | 🟢 | Assembly |
| [Beetle Adventure Racing!](https://github.com/synamaxmusic/bar-decomp) | Matching decompilation of Beetle Adventure Racing! (Nintendo 64, 1999) | 18 | 🟢 | C |
| [Destruction-Decomp-64](https://github.com/murkantor/Destruction-Decomp-64) | AI-driven decompilation experiment for Destruction Derby 64 (N64) | 18 | 🟢 | C |
| [Mario Kart 64 disassembly](https://github.com/RevoSucks/mk64_old) | Early disassembly of Mario Kart 64 (N64) | 18 | 🟡 | Assembly |
| [Quest 64](https://github.com/Rainchus/Quest64-Decomp) | Matching decompilation of Quest 64 (Nintendo 64, 1998) | 18 | 🟢 | C |
| [Blast Corps](https://github.com/SlaveOfIDO/blastcorps) | Matching decompilation of Blast Corps (Nintendo 64, 1997) | 16 | 🟢 | C |
| [The Legend of Zelda: Ocarina of Time disassembly](https://github.com/camthesaxman/zelda_oot) | Disassembly of The Legend of Zelda: Ocarina of Time (N64) | 15 | 🔴 | Assembly |
| [Bomberman 64: The Second Attack!](https://github.com/Bomberhackers/bm64tsa) | Matching decompilation of Bomberman 64: The Second Attack! (Nintendo 64, 2000) | 14 | 🟢 | C |
| [Mario Artist: Paint Studio decomp](https://github.com/LuigiBlood/paintstudio_decomp) | Decompilation of Mario Artist: Paint Studio (Nintendo 64DD) | 14 | 🟢 | C |
| [Banjo-Tooie decomp](https://github.com/wedarobi/banjo2) | Prototyping decompilation of Banjo-Tooie (N64) | 13 | 🔴 | C |
| [Chameleon Twist](https://github.com/chameleonTwistRet/chameleonTwistv1.0-JP) | Matching decompilation of Chameleon Twist (Nintendo 64, 1997) | 12 | 🟢 | C |
| [Doubutsu no Mori / Animal Forest decomp](https://github.com/BluRosie/doubutsu-no-mori) | Decompilation of Doubutsu no Mori / Animal Forest (N64) | 12 | 🗄️ | C |
| [Glover (rainchus)](https://github.com/Rainchus/Glover) | Matching decompilation of Glover (Nintendo 64, 1998) | 12 | 🟡 | C |
| [Mario Tennis (N64)](https://github.com/DellM-79/MarioTennisN64) | Decompilation of Mario Tennis (N64) | 12 | 🟡 | C |
| [Top Gear Rally / Boss Rally decomp](https://github.com/jeff-strutb/brally) | Decompilation of Top Gear Rally / Boss Rally (N64) | 12 | 🟢 | C |
| [Turok 2: Seeds of Evil decomp](https://github.com/mgrz18/turok2-decomp) | Decompilation of Turok 2: Seeds of Evil (N64) | 12 | 🟢 | C |
| [Mystical Ninja Starring Goemon](https://github.com/klorfmorf/mnsg) | Matching decompilation of Mystical Ninja Starring Goemon (Nintendo 64, 1997) | 11 | 🟢 | C |
| [Hey You decomp](https://github.com/farisawan-2000/hey_you_pikachu) | Decompilation of Hey You, Pikachu! (N64) | 10 | 🔴 | Assembly |
| [Doraemon: Nobita to Mittsu no Seireiseki](https://github.com/adipocira/doraemon1) | Matching decompilation of Doraemon: Nobita to Mittsu no Seireiseki (Nintendo 64, 1997) | 9 | 🟢 | C |
| [The Legend of Zelda: Ocarina of Time 1.0 disassembly](https://github.com/Roman971/oot-disassembly) | Disassembly of The Legend of Zelda: Ocarina of Time 1.0 (N64) | 9 | 🔴 | Assembly |
| [Conker's Bad Fur Day decomp](https://github.com/gipson-dev/64CBFD) | Decompilation of Conker's Bad Fur Day (N64) | 8 | 🟢 | C |
| [LEGO Racers](https://github.com/marijnvdwerf/lego-racers) | Matching decompilation of LEGO Racers (Nintendo 64, 1999) | 8 | 🟡 | Python |
| [San Francisco Rush 2049 decomp](https://github.com/cabi24/SFRush2049-decomp) | Decompilation of San Francisco Rush 2049 (N64) | 8 | 🟢 | C |
| [Virtual Pool 64](https://github.com/LLONSIT/VirtualPool64) | Matching decompilation of Virtual Pool 64 (Nintendo 64, 1998) | 8 | 🔴 | Assembly |
| [Wonder Project J2](https://github.com/LLONSIT-glitch/wonder) | Matching decompilation of Wonder Project J2 (Nintendo 64, 1996) | 8 | 🟢 | C |
| [BattleTanx decomp](https://github.com/TheGh0stShip/BattleTanx) | Matching decompilation of BattleTanx (N64, USA Rev 0) | 7 | 🟢 | C |
| [BattleTanx: Global Assault](https://github.com/TheGh0stShip/BattleTanx-Global-Assault) | Matching decompilation of BattleTanx: Global Assault (Nintendo 64, 1999) | 7 | 🟢 | C |
| [Castlevania decomp](https://github.com/moisesPC/cv64_overlays_decomp) | Decompilation of Castlevania (N64) overlays | 7 | 🗄️ | C |
| [KE-NG_Reversing](https://github.com/disi33/KE-NG_Reversing) | Reverse engineering of the N64 game Knife Edge: Nose Gunner | 7 | 🔴 | Shell |
| [Shadowgate 64](https://github.com/Rainchus/ShadowGate64) | Matching decompilation of Shadowgate 64 (Nintendo 64, 1999) | 7 | 🔴 | C |
| [Turok: Rage Wars decomp](https://github.com/thejunkman9000/Turok-Rage-Wars-Decomp) | Matching decompilation of Turok: Rage Wars (N64), all releases | 7 | 🟢 | C |
| [BodyHarvestDecomp](https://github.com/DeltaniumIndustries/BodyHarvestDecomp) | Decompilation of the N64 game Body Harvest | 6 | 🗄️ |  |
| [Chameleon Twist 2](https://github.com/chameleonTwistRet/chameleonTwist2v1.0-JP) | Matching decompilation of Chameleon Twist 2 (Nintendo 64, 1998) | 6 | 🟢 | C |
| [Mega Man 64 decomp](https://github.com/MegaMan64Recomp/MegaMan64Decomp) | Decompilation of Mega Man 64 (N64) | 6 | 🟢 | C |
| [The Legend of Zelda: Ocarina of Time disassembly](https://github.com/shawlucas/oot_src_1.0) | Disassembly of The Legend of Zelda: Ocarina of Time (NTSC 1.0) | 6 | 🔴 | Assembly |
| [The New Tetris](https://github.com/KiritoDv/tnt) | Matching decompilation of The New Tetris (Nintendo 64, 1999) | 6 | 🗄️ | C |
| [The New Tetris decomp](https://github.com/chris-gilmore/tnt-splat) | Decompilation of The New Tetris (N64) | 6 | 🟢 | C |
| [Blast Corps decomp](https://github.com/Doridian/BlastCorps) | Decompilation and port of Blast Corps (N64) | 5 | 🟢 | C |
| [Excitebike 64 decomp](https://github.com/chasmlol/excitebike64) | Matching decompilation of Excitebike 64 (N64, USA LodgeNet) | 5 | 🟢 | C |
| [Mario Artist: Paint Studio decomp](https://github.com/zestydevy/paint-studio) | Decompilation of Mario Artist: Paint Studio (Nintendo 64DD) | 5 | 🔴 | Assembly |
| [Paperboy (N64)](https://github.com/marijnvdwerf/paperboy-n64) | Decompilation of Paperboy (N64) | 5 | 🟢 | C |
| [Ridge Racer 64](https://github.com/jvicu2001/rr64-decomp) | Matching decompilation of Ridge Racer 64 (Nintendo 64, 2000) | 5 | 🟡 | Linker Script |
| [Snowboard Kids (sonicdcer)](https://github.com/sonicdcer/sk) | Matching decompilation of Snowboard Kids (Nintendo 64, 1997) | 5 | 🟡 | C |
| [Superman 64 decomp](https://github.com/gcsmith/Superman64Decomp) | Decompilation of Superman 64 (N64) | 5 | 🟢 | C |
| [Beetle Adventure Racing! decomp](https://github.com/bryankruman/BeetleDecomp) | Matching decompilation of Beetle Adventure Racing! (N64, USA) | 4 | 🟢 | C |
| [Dark Rift](https://github.com/Unnunu/darkrift) | Matching decompilation of Dark Rift (Nintendo 64, 1997) | 4 | 🟢 | C |
| [Onegai Monsters](https://github.com/Ryan-Myers/onegaimonsters) | Matching decompilation of Onegai Monsters (Nintendo 64, 1999) | 4 | 🟢 | C |
| [Tony Hawk's Pro Skater decomp](https://github.com/andrewnakas/thps64) | Matching decompilation of Tony Hawk's Pro Skater (N64) | 4 | 🟢 | C |
| [Turok: Rage Wars decomp](https://github.com/AbuN64/ragewars-decomp) | Decompilation of Turok: Rage Wars (N64) | 4 | 🟢 | C |
| [BattleTanx](https://github.com/AbuN64/battletanx-decomp) | Matching decompilation of BattleTanx (Nintendo 64, 1998) | 3 | 🟢 | C |
| [Hybrid Heaven](https://github.com/southcitycapture/hybridheaven-decomp) | Matching decompilation of Hybrid Heaven (Nintendo 64, 1999) | 3 | 🟢 | C |
| [Rockman Dash / Mega Man 64 decomp](https://github.com/Rainchus/RockmanDash-Decomp) | Decompilation of Rockman Dash / Mega Man 64 (N64, NTSC-J) | 3 | 🟡 | C |
| [Glover](https://github.com/djsaunde/glover-decomp-1) | Matching decompilation of Glover (Nintendo 64, 1998) | 2 | 🟢 | C |
| [Pokémon Stadium 2 decomp](https://github.com/lincoln-lm/stad2) | Partial decompilation of Pokémon Stadium 2 (N64, USA 1.0) | 2 | 🔴 | Python |
| [Shiren the Wanderer 2](https://github.com/mschienbein/shiren2-decomp) | Matching decompilation of Shiren the Wanderer 2 (Nintendo 64, 2000) | 2 | 🟢 | C |
| [The Legend of Zelda: Ocarina of Time 1.0 disassembly](https://github.com/GlitterBerri/oot) | Disassembly of The Legend of Zelda: Ocarina of Time 1.0 (N64) | 2 | 🔴 | Assembly |
| [Top Gear Rally decomp](https://github.com/Tatsh/tgr-decomp) | Decompilation of Top Gear Rally (N64) | 2 | 🟢 | C |
| [Hey You decomp](https://github.com/ornata/hey-you-pikachu-decomp) | Decompilation of Hey You, Pikachu! (N64, US) | 1 | 🟢 | C |
| [Hey You disassembly](https://github.com/Decompollaborate/hypdisasm) | Disassembly of Hey You, Pikachu! (N64) | 1 | 🔴 | Assembly |
| [Ogre Battle 64 decomp](https://github.com/rempred/OB64-Decomp) | Decompilation of Ogre Battle 64 (N64) | 1 | 🟢 | Assembly |
| [xg-2-decomp](https://github.com/Teraunce/xg-2-decomp) | Decompilation attempt of Extreme-G 2 (N64) | 1 | 🟢 | Assembly |
| [Banjo-Kazooie](https://gitlab.com/banjo.decomp/banjo-kazooie) | Matching decompilation of Banjo-Kazooie (Nintendo 64, 1998) |  | ⚪ |  |
| [Donkey Kong 64](https://gitlab.com/dk64_decomp/dk64) | Matching decompilation of Donkey Kong 64 (Nintendo 64, 1999) |  | ⚪ |  |
| [GoldenEye 007](https://gitlab.com/kholdfuzion/goldeneye_src) | Matching decompilation of GoldenEye 007 (Nintendo 64, 1997) |  | ⚪ |  |
| [NBA Live 2000 decomp](https://github.com/Rainchus/NbaLive2000-N64-Decomp) | Decompilation of NBA Live 2000 (N64) | 0 | 🟡 | Python |
| [ogrebattle64](https://codeberg.org/hijsje/ogrebattle64) | Decompilation of Ogre Battle 64 for the Nintendo 64 |  | ⚪ |  |
| [Perfect Dark](https://gitlab.com/ryandwyer/perfect-dark) | Matching decompilation of Perfect Dark (Nintendo 64, 2000) |  | ⚪ |  |
| [Top Gear Rally decomp](https://github.com/Tatsh/coastline) | Reconstructed source of Top Gear Rally (N64) | 0 | 🟢 | C |
| [Wave Race 64 decomp](https://github.com/bkruskie/Wave-Race-64) | Decompilation of Wave Race 64 (N64, USA rev1) with byte-exact ROM rebuild | 0 | 🟢 | Assembly |

## Matching Decompilations — Other / Multi-platform

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [UnityDecompiled](https://github.com/MattRix/UnityDecompiled) | Decompiled C# source of the Unity editor and engine assemblies (now superseded by official reference source) | 1,484 | 🗄️ |  |
| [sm64-port](https://github.com/sm64-port/sm64-port) | Port of the SM64 decompilation to modern devices | 1,324 | 🟡 | C |
| [RSDKv4 Decompilation](https://github.com/RSDKModding/RSDKv4-Decompilation) | Decompilation of Sonic 1 & 2 (2013) and Retro Engine v4 | 1,154 | 🟢 | C++ |
| [RSDKv5-Decompilation](https://github.com/RSDKModding/RSDKv5-Decompilation) | Complete decompilation of Retro Engine v5 (Sonic Mania) | 571 | 🟢 | C++ |
| [Elite decomp](https://github.com/markmoxon/elite-source-code-commodore-64) | Fully documented reverse-engineered source code of Elite (Commodore 64) | 474 | 🟢 | Assembly |
| [Metal Gear disassembly](https://github.com/GuillianSeed/MetalGear) | Fully annotated disassembly of Metal Gear (MSX2, Konami) | 327 | 🔴 | Assembly |
| [bo1-zombies-decompiled](https://github.com/MisaDev4/bo1-zombies-decompiled) | Decompiled GSC scripts of Call of Duty: Black Ops 1 Zombies | 295 | 🟢 | C++ |
| [overpy](https://github.com/Zezombye/overpy) | High-level language for the Overwatch Workshop with compile and decompile support | 237 | 🟢 | OverPy |
| [v-decompiled-scripts](https://github.com/root-cause/v-decompiled-scripts) | Decompiled GTA V game scripts | 160 | 🗄️ | C |
| [Paleblood](https://github.com/Yharnam-Hunters/Paleblood) | Decompilation of Bloodborne v1.09 with its own runtime | 140 | 🟢 | Python |
| [RSDKv4-Script-Decompilation](https://github.com/RSDKModding/RSDKv4-Script-Decompilation) | Decompiled scripts of Retro Engine v4 games (Sonic 1/2 mobile) | 140 | 🟢 |  |
| [RSDKv3-Script-Decompilation](https://github.com/RSDKModding/RSDKv3-Script-Decompilation) | Decompiled scripts of Retro Engine v3 (Sonic CD) | 139 | 🟢 |  |
| [RuneScape Classic client (2003scape rsc-c)](https://github.com/2003scape/rsc-c) | RuneScape Classic client ported to C, with builds for PC, Wii, 3DS and Switch | 136 | 🟢 | C |
| [Lander decomp](https://github.com/markmoxon/lander-source-code-acorn-archimedes) | Fully documented reverse-engineered source code of Lander (Acorn Archimedes) | 111 | 🟢 | Assembly |
| [ChoplifterReverse](https://github.com/blondie7575/ChoplifterReverse) | Full reverse engineered source of the Apple II game Choplifter | 100 | 🟡 | Assembly |
| [lode_runner_reveng](https://github.com/XekriRedmane/lode_runner_reveng) | Reverse engineering of Lode Runner for the Apple II | 97 | 🟢 | TeX |
| [Elite (c64-elite-flicker-free (Mark Moxon))](https://github.com/markmoxon/c64-elite-flicker-free) | Decompilation of Elite (BBC Micro/Acorn) | 96 | 🟢 | Assembly |
| [GTA-V-Decompiled-Scripts](https://github.com/calamity-inc/GTA-V-Decompiled-Scripts) | All decompiled GTA V .ysc game scripts, including native tables | 85 | 🟢 | C |
| [jetpac-disassembly](https://github.com/mrcook/jetpac-disassembly) | Fully annotated disassembly of JETPAC (ZX Spectrum) | 77 | 🟢 | Assembly |
| [gridrunner](https://github.com/mwenge/gridrunner) | Reverse-engineered source of Gridrunner (1982) by Jeff Minter | 75 | 🔴 | Assembly |
| [Terraria (Old-Gen Console)](https://github.com/PPrism/TerrariaOGC) | Functional decompilation and PC port of the Xbox 360 / PS3 version of Terraria (2013) | 68 | 🟢 | C# |
| [Elite-A decomp](https://github.com/markmoxon/elite-a-source-code-bbc-micro) | Fully documented reverse-engineered source code of Elite-A (BBC Micro) | 60 | 🟢 | Assembly |
| [Aviator decomp](https://github.com/markmoxon/aviator-source-code-bbc-micro) | Fully documented reverse-engineered source code of Aviator (BBC Micro) | 59 | 🟢 | Assembly |
| [The Sentinel decomp](https://github.com/markmoxon/the-sentinel-source-code-bbc-micro) | Fully documented reverse-engineered source code of The Sentinel (BBC Micro) | 59 | 🟢 | Assembly |
| [classic arcade disassembly](https://github.com/topherCantrell/computerarcheology) | Commented disassemblies of classic arcade, console and computer games behind computerarcheology.com | 57 | 🟢 | Assembly |
| [Guitar Hero: Warriors of Rock](https://github.com/kernaltrap8/WoR-Plus) | Quality-of-life mod for Guitar Hero: Warriors of Rock (PS3 / Xbox 360, 2010) | 57 | 🟡 | HiveQL |
| [Atari 2600 and Atari 8-bit games disassembly](https://github.com/DNSDEBRO/Disassemblies) | Commented disassemblies of Atari 2600 and Atari 8-bit games | 54 | 🟡 | Assembly |
| [sead](https://github.com/aboood40091/sead) | Decompilation of Nintendo EAD's sead engine library | 54 | 🟢 | C++ |
| [disc Elite decomp](https://github.com/markmoxon/elite-source-code-bbc-micro-disc) | Fully documented reverse-engineered source code of disc Elite (BBC Micro) | 53 | 🟢 | Assembly |
| [fe2-intro](https://github.com/watsonmw/fe2-intro) | Reverse-engineered renderer and audio of Frontier: Elite II (Amiga) | 51 | 🟡 | C++ |
| [music drivers of various video games disassembly](https://github.com/loveemu/vgm-disasm) | Disassemblies of the music drivers of various video games | 51 | 🟢 | Assembly |
| [Maniac Mansion disassembly](https://github.com/pditincho/mm-explained) | Explained disassembly of Maniac Mansion (Commodore 64) | 50 | 🟢 | Assembly |
| [Cobra decomp](https://github.com/Paulie68000/ZXSpectrumCobra) | Reverse-engineered source code of Cobra by Jonathan Smith (ZX Spectrum) | 47 | 🟡 | Assembly |
| [Stunt Car Racer (Vesuri stuntcarracer (Framerate Unleashed))](https://github.com/Vesuri/stuntcarracer) | Decompilation of Stunt Car Racer (Amiga) | 45 | 🟢 | Assembly |
| [Elite decomp](https://github.com/markmoxon/elite-source-code-apple-ii) | Fully documented reverse-engineered source code of Elite (Apple II) | 43 | 🟢 | Assembly |
| [Maniac Mansion game scripts disassembly](https://github.com/segrax/Maniac.Mansion.Disassembly) | Commented disassembly of Maniac Mansion game scripts (Commodore 64) | 43 | 🔴 | C |
| [GD-2.206-Decompiled](https://github.com/CallocGD/GD-2.206-Decompiled) | Decompilation attempt of Geometry Dash 2.206 | 42 | 🟡 | C++ |
| [Revs decomp](https://github.com/markmoxon/revs-source-code-bbc-micro) | Fully documented reverse-engineered source code of Revs (BBC Micro) | 42 | 🟢 | Assembly |
| [Elite decomp](https://github.com/markmoxon/elite-source-code-6502-second-processor) | Fully documented reverse-engineered source code of Elite (BBC Micro 6502 Second Processor) | 41 | 🟢 | Assembly |
| [newer 4J Studios Minecraft Legacy Console Edition releases decomp](https://github.com/Patoke/LCERenewed) | Decompilation of newer 4J Studios Minecraft Legacy Console Edition releases | 40 | 🟢 | C++ |
| [habbo_src](https://github.com/Quackster/habbo_src) | Archive of decompiled Habbo client files from 2001-2009 | 37 | 🟢 | LiveScript |
| [Elite decomp](https://github.com/markmoxon/elite-source-code-bbc-master) | Fully documented reverse-engineered source code of Elite (BBC Master) | 35 | 🟢 | Assembly |
| [C64 Wizard of Wor Disassembly](https://github.com/dabadab/wizardofwor) | Wizard of Wor for C64 disassembly | 34 | 🔴 | Assembly |
| [Elite decomp](https://github.com/markmoxon/elite-source-code-acorn-electron) | Fully documented reverse-engineered source code of Elite (Acorn Electron) | 34 | 🟢 | Assembly |
| [Pyramid Warp Ex disassembly](https://github.com/theNestruo/msx-pyramidwarpex) | Disassembly and reverse engineering of Pyramid Warp Ex (MSX) | 34 | 🗄️ | Assembly |
| [Nether Earth disassembly](https://github.com/santiontanon/netherearth-disassembly) | Disassembly of Nether Earth (ZX Spectrum, 1986) | 33 | 🔴 | HTML |
| [Head Over Heels decomp](https://github.com/simon-frankau/head-over-heels) | Reverse engineering of Head Over Heels (ZX Spectrum) | 32 | 🔴 | Assembly |
| [Castle Master II: The Crypt disassembly](https://github.com/santiontanon/castlemaster2-disassembly) | Disassembly of Castle Master II: The Crypt (ZX Spectrum, 1990) | 30 | 🔴 | Assembly |
| [Exile disassembly](https://github.com/tom-seddon/exile_disassembly) | Commented, buildable disassembly of the classic BBC Micro game | 29 | 🗄️ | TypeScript |
| [Iridis Alpha disassembly](https://github.com/mwenge/iridisalpha) | Disassembled source code of Iridis Alpha by Jeff Minter (Commodore 64) | 29 | 🟡 | Assembly |
| [RDR3-Decompiled-Scripts](https://github.com/kepmehz/RDR3-Decompiled-Scripts) | Red Dead Redemption 2 .ysc game scripts decompiled to C with natives and strings | 28 | 🔴 | C |
| [Prince of Persia (SDLPoP-Dreamcast)](https://github.com/Memorix101/SDLPoP-Dreamcast) | Disassembly of Prince of Persia (Apple II) | 27 | 🟡 | C |
| [Thrust Disassembly](https://github.com/kieranhj/thrust-disassembly) | Reverse engineered source to BBC Thrust | 27 | 🟢 | Assembly |
| [Uridium disassembly](https://github.com/mwenge/uridium) | Disassembled source of Uridium by Andrew Braybrook (Commodore 64) | 26 | 🟢 | Assembly |
| [Manic Miner disassembly](https://github.com/skoolkid/manicminer) | A disassembly of Manic Miner, created using SkoolKit. | 25 | 🟢 | Python |
| [Hyper Active decomp](https://github.com/Paulie68000/ZXSpectrumHyperActive) | Reverse-engineered source code of Hyper Active by Jonathan Smith (ZX Spectrum) | 24 | 🟡 | Assembly |
| [Burnout Paradise](https://github.com/BurnoutHints/b5-decomp) | Decompilation of Burnout Paradise | 23 | 🟡 | C++ |
| [Ghost Town disassembly](https://github.com/Esshahn/Ghost-Town) | Disassembly of Ghost Town (Commodore 16) | 23 | 🔴 | Assembly |
| [Stunt Car Racer (stunt-car-racer-ste)](https://github.com/jonathanopalise/stunt-car-racer-ste) | Decompilation of Stunt Car Racer (Amiga) | 23 | 🔴 | Assembly |
| [Arkanoid disassembly](https://github.com/mcolom/arkanoid_msx_disasm) | Disassembly of Arkanoid (MSX) | 22 | 🟢 | Assembly |
| [gcx_decompiler](https://github.com/oct0xor/gcx_decompiler) | Decompiler for GCX/GCL scripts in Metal Gear Solid games | 22 | 🔴 | Python |
| [Ultimate Play the Game disassemblies](https://github.com/pobtastic/ultimate) | A disassembly of various "Ultimate Play the Game" games, created using SkoolKit. | 22 | 🟡 | Visual Basic 6.0 |
| [Alien Breed Special Edition disassembly](https://github.com/hitchhikr/alienbreed) | Complete disassembly of Alien Breed Special Edition (Amiga CD32) | 21 | 🟢 | Assembly |
| [Booga-Boo disassembly](https://github.com/mcolom/boogaboo_disasm_msx) | Disassembly of Booga-Boo (MSX) | 21 | 🟡 | Assembly |
| [Jet Set Willy disassembly](https://github.com/skoolkid/jetsetwilly) | A disassembly of Jet Set Willy, created using SkoolKit. | 20 | 🟢 | Python |
| [Attack of the Mutant Camels decomp](https://github.com/C64-Mark/Attack-of-the-Mutant-Camels) | Reverse engineering of Attack of the Mutant Camels by Jeff Minter (Commodore 64) | 19 | 🔴 | Assembly |
| [Chuckie Egg decomp](https://github.com/Paulie68000/ZXSpectrumChuckieEgg) | Documented reverse-engineered source code of Chuckie Egg (ZX Spectrum) | 19 | 🟡 | Assembly |
| [Speedball 2: Brutal Deluxe decomp](https://github.com/simon-frankau/speedball2-re-amiga) | Reverse engineering of Speedball 2: Brutal Deluxe (Amiga) | 18 | 🔴 | Assembly |
| [Manic Miner (BBC)](https://github.com/TobyLobster/ManicMiner) | Disassembly of the original BBC Micro version of Manic Miner | 17 | 🟡 |  |
| [Psychedelia/Colourspace disassembly](https://github.com/mwenge/psychedelia) | Disassembled source of Psychedelia/Colourspace by Jeff Minter (C64, Atari 800) | 17 | 🟡 | Assembly |
| [The Lords of Midnight disassembly](https://github.com/mrcook/lords-of-midnight-disassembly) | Disassembly of The Lords of Midnight (ZX Spectrum and DOS) | 17 | 🟡 | Assembly |
| [music code disassembly](https://github.com/ZoomTen/chronos-zxbeeper) | Disassembly of the music code from Chronos (ZX Spectrum) | 16 | 🔴 | Assembly |
| [Exolon disassembly](https://github.com/rusarh/exolon-esl) | Disassembly of Exolon (ZX Spectrum) | 15 | 🔴 | Assembly |
| [Mercenary disassembly](https://github.com/mikedailly/MercenaryDisassembly) | Disassembly of Mercenary (ZX Spectrum) | 15 | 🟢 | Assembly |
| [River Raid disassembly](https://github.com/river-raid/river-raid-disasm) | Disassembly of River Raid (ZX Spectrum) | 15 | 🟢 | Assembly |
| [The Sims disassembly](https://github.com/simdecomp/sims1_mac_decomp) | Disassembly and decompilation of The Sims (Mac) | 15 | 🔴 | Assembly |
| [UrnaDecomp](https://github.com/macabeus/UrnaDecomp) | Matching decompilation of the Brazilian TSE electronic voting machine simulator | 15 | 🟢 | C++ |
| [Beyond Dark Castle disassembly](https://github.com/r41n60w/bdc_disasm) | Disassembly of Beyond Dark Castle (Macintosh, 1987) in 68000 assembly | 14 | 🔴 | Assembly |
| [Crossroads II disassembly](https://github.com/MarkRdgOx/crossroads-2-disassembly) | Commented disassembly of Crossroads II (Commodore 64) | 14 | 🟢 | Assembly |
| [Repton disassembly](https://github.com/ajgbarnes/bbc-micro-repton) | Disassembly of Repton (BBC Micro) | 14 | 🔴 | Assembly |
| [The Hobbit disassembly](https://github.com/pobtastic/hobbit) | A disassembly of The Hobbit, created using SkoolKit. | 13 | 🔴 | Visual Basic 6.0 |
| [Batman The Movie disassembly](https://github.com/MarkyTurtle/Batman---Amiga) | Full disassembly of Batman The Movie (Amiga, Ocean) | 12 | 🟢 | Assembly |
| [Fred disassembly](https://github.com/kmatveev/zx-fred-reveng) | Reverse engineering and disassembly of Fred (ZX Spectrum) | 12 | 🟡 | Java |
| [Green Beret decomp](https://github.com/Paulie68000/ZXSpectrumGreenBeret) | Reverse-engineered source code of Green Beret (ZX Spectrum) | 12 | 🟡 | Assembly |
| [Haunted House disassembly](https://github.com/brandonrobertz/haunted_house_disassembly) | Commented disassembly of Haunted House (Atari 2600) | 12 | 🔴 | Assembly |
| [Green Beret disassembly](https://github.com/cadaver/greenberet-disassembly) | Disassembly of Green Beret (Commodore 64) | 11 | 🟢 | Assembly |
| [Rex disassembly](https://github.com/ultrabolido/skRex) | A disassembly of Rex, created using SkoolKit. | 11 | 🔴 | CSS |
| [Sargon II Chess disassembly](https://github.com/jamarju/vic20-sargon-ii-chess) | Disassembly of Sargon II Chess (VIC-20) | 11 | 🟢 | Assembly |
| [Soldier of Fortune decomp](https://github.com/kmatveev/zx-sof-reveng) | Reverse engineering of Soldier of Fortune (ZX Spectrum) | 11 | 🔴 |  |
| [The Way of the Exploding Fist disassembly](https://github.com/pobtastic/wayoftheexplodingfist) | A disassembly of The Way of the Exploding Fist, created using SkoolKit. | 11 | 🔴 | Visual Basic 6.0 |
| [Deathchase disassembly](https://github.com/Ritchie333/deathchase) | Annotated disassembly of Deathchase (ZX Spectrum, 1983) | 10 | 🟡 |  |
| [Skate](https://github.com/Skate-Modding-Team/Skate-Decompilation-Project) | Decompilation of Skate | 10 | 🟢 | C++ |
| [atari-vcs-disassembly](https://github.com/milnak/atari-vcs-disassembly) | Collection of Atari 2600 game disassemblies | 9 | 🟢 | Assembly |
| [Chuckie Egg disassembly](https://github.com/mrcook/chuckie-egg-disassembly) | Annotated disassembly of Chuckie Egg (ZX Spectrum, 1983) | 9 | 🔴 | Assembly |
| [Disassembly of Boulder Dash for the BBC Micro](https://github.com/TobyLobster/Boulderdash) | Disassembly of the game Boulderdash on the BBC Micro | 9 | 🟡 | Assembly |
| [Jetpac disassembly](https://github.com/phillipeaton/JETPAC_VIC-20_disassembly) | Reverse-engineered disassembly of Jetpac (VIC-20) | 9 | 🟡 | Assembly |
| [Mortal Kombat 3D-era](https://github.com/cScarletter/MK-3D-Era-Decompilation) | Research and decompilation of Mortal Kombat: Deadly Alliance, Deception and Armageddon (multi-platform, 2002–2006) | 9 | 🟡 | C |
| [Soulcalibur II](https://github.com/Soulcalibur-II-Research-Group/scII_re) | Decompilation of Soulcalibur II | 9 | 🟢 |  |
| [UridiumFraktion](https://github.com/mwenge/UridiumFraktion) | Annotated code, data and pixels of Uridium (Commodore 64) | 9 | 🟢 | Jupyter Notebook |
| [Antarctic Adventure disassembly](https://github.com/ricbit/antarctic) | Disassembly of Antarctic Adventure (MSX) | 8 | 🟢 | Assembly |
| [Apple II games disassembly](https://github.com/Michaelangel007/apple2_games_disassembly_project) | Reverse engineering and disassembly of Apple II games | 8 | 🟢 | Assembly |
| [Burnout 2: Point of Impact decomp](https://github.com/b3dllc/burnout2) | Decompilation of Burnout 2: Point of Impact (2002) | 8 | 🟢 | C++ |
| [chuckie](https://github.com/Ritchie333/chuckie) | Disassembly of the classic 1983 ZX Spectrum game "Chuckie Egg" | 8 | 🟡 | Visual Basic 6.0 |
| [Robotron: 2084 disassembly](https://github.com/fschuhi/Robotron_2084) | 6502 disassembly of Robotron: 2084 (Apple II) | 8 | 🔴 | Assembly |
| [The Bard's Tale disassembly](https://github.com/Bedazzle/Bards-tale) | Disassembly of The Bard's Tale (ZX Spectrum) | 8 | 🟢 | Assembly |
| [The Sims 2 decomp](https://github.com/ChrisNonyminus/sims2_mac_decomp) | Decompilation of The Sims 2 (Mac) | 8 | 🔴 | Python |
| [ZX Spectrum code disassembly](https://github.com/nwoeanhinnogaehr/bandersnatch) | Annotated disassembly of the ZX Spectrum code from Black Mirror: Bandersnatch | 8 | 🔴 | Assembly |
| [Batty disassembly](https://github.com/pobtastic/batty) | A disassembly of Batty, created using SkoolKit. | 7 | 🟡 | Visual Basic 6.0 |
| [Driller disassembly](https://github.com/hitchhikr/driller) | Complete disassembly of Driller (Amiga) | 7 | 🔴 | Assembly |
| [Dynamite Dan disassembly](https://github.com/Ritchie333/dynamitedan) | Annotated disassembly of Dynamite Dan (ZX Spectrum, 1985) | 7 | 🟡 | Visual Basic 6.0 |
| [Elite disassembly](https://github.com/ricbit/elite) | Complete disassembly of Elite (MSX) | 7 | 🟢 | Assembly |
| [Fairlight disassembly](https://github.com/VilleKrumlinde/FairlightZ80) | Commented disassembly of Fairlight (ZX Spectrum, 1985) | 7 | 🟢 | Assembly |
| [Imogen disassembly](https://github.com/ZornsLemma/Imogen) | Disassembly of Imogen (BBC Micro) | 7 | 🟡 | Assembly |
| [k240](https://github.com/tetracorp/k240) | Disassembly project for K240 (Amiga, 1994) | 7 | 🟢 | Assembly |
| [Monty on the Run decomp](https://github.com/Dave-Agent/monty-on-the-run) | Commented KickAssembler reconstruction of Monty on the Run (Commodore 64) | 7 | 🟢 | Assembly |
| [Pokéwalker firmware decomp](https://github.com/UnrealPowerz/pw_firm) | Decompilation of the Pokéwalker firmware | 7 | 🟢 | C |
| [The Lord of the Rings: The Return of the King](https://github.com/crimsonmagick/lotr-rotk) | Decompilation of The Lord of the Rings: The Return of the King | 7 | 🟡 |  |
| [West Bank](https://github.com/pobtastic/westbank) | A disassembly of West Bank, created using SkoolKit. | 7 | 🔴 | Visual Basic 6.0 |
| [Alphabet Park Adventure](https://github.com/unspDecomp/abcParkDecomp) | Matching decompilation of Alphabet Park Adventure (V.Smile, 2004) | 6 | 🟡 | C |
| [Back to Skool disassembly](https://github.com/skoolkid/backtoskool) | A disassembly of Back to Skool, created using SkoolKit. | 6 | 🟢 | Python |
| [Booty disassembly](https://github.com/pobtastic/booty) | A disassembly of Booty, created using SkoolKit. | 6 | 🟢 | Visual Basic 6.0 |
| [Eric and the Floaters disassembly](https://github.com/Bedazzle/EATF) | Disassembly of Eric and the Floaters (ZX Spectrum) | 6 | 🟢 | Assembly |
| [Everyone's A Wally disassembly](https://github.com/Ritchie333/wally) | Disassembly of Everyone's A Wally (ZX Spectrum) | 6 | 🟡 | Visual Basic 6.0 |
| [Halo decomp](https://github.com/ChrisNonyminus/halo_mac_decomp) | Decompilation of Halo (Mac OS X PowerPC) | 6 | 🔴 | Python |
| [Hungry Horace disassembly](https://github.com/skoolkid/hungryhorace) | A disassembly of Hungry Horace, created using SkoolKit. | 6 | 🟢 | Shell |
| [Road Fighter disassembly](https://github.com/howprice/road-fighter-msx) | Annotated disassembly of Road Fighter (MSX, Konami, 1985) | 6 | 🟢 | Assembly |
| [Skool Daze disassembly](https://github.com/skoolkid/skooldaze) | A disassembly of Skool Daze, created using SkoolKit. | 6 | 🟢 | Python |
| [Technician Ted disassembly](https://github.com/Ritchie333/chipfact) | Annotated disassembly of Technician Ted (ZX Spectrum, 1984) | 6 | 🟡 | Visual Basic 6.0 |
| [Wanted: Monty Mole disassembly](https://github.com/Ritchie333/monty) | Disassembly of Wanted: Monty Mole (ZX Spectrum, 1984) | 6 | 🔴 | Visual Basic 6.0 |
| [Antarctic Adventure disassembly](https://github.com/antxiko/AntarcticAdventure-disassembly) | Commented byte-exact disassembly of Antarctic Adventure (MSX) | 5 | 🟢 | Assembly |
| [Battlezone disassembly (ZX Spectrum)](https://github.com/pobtastic/battlezone) | A disassembly of Battlezone, created using SkoolKit. | 5 | 🟡 | Visual Basic 6.0 |
| [Colt 36 disassembly](https://github.com/antxiko/Colt36-disassembly) | Commented byte-exact disassembly of Colt 36 (MSX) | 5 | 🟢 | Assembly |
| [dungeons-of-avalon](https://github.com/tetracorp/dungeons-of-avalon) | Disassembly and analysis of Dungeons of Avalon (Amiga, 1991) | 5 | 🟢 | HTML |
| [Head Over Heels disassembly](https://github.com/fphenix/HeadOverHeels_CPC) | Disassembly of Head Over Heels (Amstrad CPC) | 5 | 🟢 | Assembly |
| [Hunchback disassembly](https://github.com/Ritchie333/hunch) | Disassembly of Hunchback (ZX Spectrum) | 5 | 🟡 | Visual Basic 6.0 |
| [Jason's Gem disassembly](https://github.com/pobtastic/jasons-gem) | A disassembly of Jason's Gem, created using SkoolKit. | 5 | 🔴 | Visual Basic 6.0 |
| [Lode Runner disassembly](https://github.com/Bedazzle/Lode-runner) | Disassembly of Lode Runner (ZX Spectrum) | 5 | 🟢 | Assembly |
| [Rampage disassembly](https://github.com/pobtastic/rampage) | A disassembly of Rampage, created using SkoolKit. | 5 | 🟡 | Visual Basic 6.0 |
| [Road Rash decomp](https://github.com/trapexit/3do-decomp-road-rash) | Decompilation and reconstruction of Road Rash (3DO, USA) | 5 | 🟢 | C |
| [Spy vs Spy II: The Island Caper disassembly](https://github.com/hitchhikr/spyvsspy2) | Complete disassembly of Spy vs Spy II: The Island Caper (Amiga) | 5 | 🟢 | Assembly |
| [Starquake disassembly](https://github.com/Ritchie333/starquake) | Disassembly of Starquake (ZX Spectrum, 1985) | 5 | 🟡 | Visual Basic 6.0 |
| [Wheelie disassembly](https://github.com/pobtastic/wheelie) | A disassembly of Wheelie, created using SkoolKit. | 5 | 🟡 | Visual Basic 6.0 |
| [Ale Hop! disassembly](https://github.com/antxiko/AleHop-disassembly) | Commented byte-exact disassembly of Ale Hop! (MSX) | 4 | 🟢 | Assembly |
| [Contact Sam Cruise disassembly](https://github.com/skoolkid/contactsamcruise) | A disassembly of Contact Sam Cruise, created using SkoolKit. | 4 | 🟢 | Python |
| [Elite disassembly](https://github.com/Rasmus-M/elite-skoolkit) | SkoolKit disassembly of Elite (ZX Spectrum) | 4 | 🟢 | HTML |
| [Everyone's A Wally disassembly](https://github.com/pobtastic/everyonesawally) | SkoolKit disassembly of Everyone's A Wally (ZX Spectrum) | 4 | 🟡 | Visual Basic 6.0 |
| [Fate/EXTELLA](https://github.com/bIue9076r/fate-extella-decompilation) | Decompilation of Fate/EXTELLA | 4 | 🟡 | C |
| [Galaxy on Fire 2 HD decomp](https://github.com/fionera/gof2hd-decomp) | Decompilation of Galaxy on Fire 2 HD | 4 | 🟢 | C++ |
| [Harrier Attack disassembly](https://github.com/pobtastic/harrierattack) | A disassembly of Harrier Attack, created using SkoolKit. | 4 | 🟡 | Visual Basic 6.0 |
| [Head Over Heels disassembly](https://github.com/mkrivos/Head-Over-Heels) | Reverse-engineered disassembly of Head Over Heels (ZX Spectrum) | 4 | 🟢 | Assembly |
| [Herbert's Dummy Run disassembly](https://github.com/Ritchie333/dummyrun) | Disassembly of Herbert's Dummy Run (ZX Spectrum, 1985) | 4 | 🟡 | Visual Basic 6.0 |
| [Knightmare disassembly](https://github.com/antxiko/Knightmare-disassembly) | Commented byte-exact disassembly of Knightmare (MSX) | 4 | 🟢 | Assembly |
| [simcity_z80](https://github.com/suborb/simcity_z80) | Disassembly and rebuild of SimCity for the ZX Spectrum and other Z80 machines | 4 | 🟢 | Assembly |
| [Sonic X decomp](https://github.com/Iso-Kilo/Sonic-X-Leapster-Decompilation) | Decompilation of Sonic X for the Leapster (2005) | 4 | 🔴 |  |
| [Stardust disassembly](https://github.com/antxiko/Stardust-MSX-disassembly) | Commented byte-exact disassembly of Stardust (MSX) | 4 | 🟢 | Assembly |
| [Super Cobra disassembly](https://github.com/antxiko/SuperCobra-disassembly) | Commented byte-exact disassembly of Super Cobra (MSX) | 4 | 🟢 | Python |
| [Temptations disassembly](https://github.com/antxiko/temptations-disassembly) | Commented disassembly of Temptations (MSX, Topo Soft, 1988) | 4 | 🟢 | Assembly |
| [Vampire Killer / Akumajo Dracula disassembly](https://github.com/antxiko/VampireKiller-disassembly) | Commented byte-exact disassembly of Vampire Killer / Akumajo Dracula (MSX) | 4 | 🟢 | Assembly |
| [Zool 2 disassembly](https://github.com/hitchhikr/zool2) | Complete disassembly of Zool 2 (Amiga CD32) | 4 | 🔴 | Assembly |
| [1987 Radio-86RK game Volcano disassembly](https://github.com/begoon/volcano) | Byte-exact annotated disassembly of the 1987 Radio-86RK game Volcano | 3 | 🟢 | Assembly |
| [Acornsoft Planetoid disassembly](https://github.com/r41n60w/planetoid-disasm) | Disassembly of Acornsoft Planetoid (BBC Micro) | 3 | 🔴 | Assembly |
| [Armored Unit](https://github.com/Normmatt/unarmoredunit) | Matching decompilation of Armored Unit (WonderSwan, 2000) | 3 | 🟢 | C |
| [Bruce Lee disassembly](https://github.com/fizgog/Bruce-Lee-Disassembly) | Disassembly of Bruce Lee (8-bit) | 3 | 🟡 | Assembly |
| [Bubsy in Fractured Furry Tales disassembly](https://github.com/scarleyyXD/bubsy3_disasm) | Disassembly-based source of Bubsy in Fractured Furry Tales (Atari Jaguar, 1994) | 3 | 🟢 | Assembly |
| [Call of Duty 3 decomp](https://github.com/L2KSolkov/cod3-decomp) | Decompilation of Call of Duty 3 | 3 | 🟢 | C++ |
| [Championship Manager Italia decomp](https://github.com/GRHOnline/Decomp_ChampionshipManagerItalia_ST) | Assembler decompilation of Championship Manager Italia (Atari ST) | 3 | 🟢 | Assembly |
| [Chaos: The Battle of Wizards disassembly](https://github.com/lewster32/chaos-disassembly) | Annotated disassembly of Chaos: The Battle of Wizards (ZX Spectrum, 1985) | 3 | 🟢 | Assembly |
| [F-1 Spirit disassembly](https://github.com/antxiko/F1Spirit-disassembly) | Commented byte-exact disassembly of F-1 Spirit (MSX) | 3 | 🟢 | Assembly |
| [Horace Goes Skiing disassembly](https://github.com/Ritchie333/skiing) | Disassembly of Horace Goes Skiing (ZX Spectrum) | 3 | 🟡 | Visual Basic 6.0 |
| [Into the Eagle's Nest disassembly](https://github.com/hitchhikr/eaglenest) | Complete disassembly of Into the Eagle's Nest (Amiga) | 3 | 🔴 | Assembly |
| [King's Valley II disassembly](https://github.com/antxiko/KingsValley2-disassembly) | Commented disassembly of King's Valley II (MSX/MSX2, Konami, 1988) | 3 | 🟢 | Assembly |
| [Konami's Game Master cartridge disassembly](https://github.com/ricbit/game-master) | Full disassembly of Konami's Game Master cartridge (MSX) | 3 | 🟢 | Assembly |
| [Legends of Valour disassembly](https://github.com/AzazelN28/lov-disasm) | Disassembly of Legends of Valour | 3 | 🔴 | Assembly |
| [Lemans disassembly](https://github.com/ricardoquesada/c64-lemans) | Disassembly of Lemans (Commodore 64) with gamepad rumble support | 3 | 🔴 | Assembly |
| [Matrix disassembly](https://github.com/mwenge/matrix) | Disassembled source of Matrix by Jeff Minter (Commodore 64) | 3 | 🟡 | Assembly |
| [Nemesis / Gradius disassembly](https://github.com/antxiko/Nemesis-disassembly) | Commented byte-exact disassembly of Nemesis / Gradius (MSX) | 3 | 🟢 | Assembly |
| [Nemesis 2 disassembly](https://github.com/antxiko/Nemesis2-disassembly) | Commented byte-exact disassembly of Nemesis 2 (MSX) | 3 | 🟢 | Assembly |
| [Parodius disassembly](https://github.com/antxiko/Parodius-disassembly) | Commented disassembly of Parodius (MSX, Konami, 1988) | 3 | 🟢 | Assembly |
| [Pippols disassembly](https://github.com/antxiko/Pippols-disassembly) | Commented byte-exact disassembly of Pippols (MSX) | 3 | 🟢 | Assembly |
| [Salamander disassembly](https://github.com/antxiko/Salamander-disassembly) | Commented byte-exact disassembly of Salamander (MSX) | 3 | 🟢 | Assembly |
| [Sky Jaguar disassembly](https://github.com/antxiko/SkyJaguar-disassembly) | Commented byte-exact disassembly of Sky Jaguar (MSX) | 3 | 🟢 | Assembly |
| [The Maze of Galious / Knightmare II disassembly](https://github.com/antxiko/MazeOfGalious-disassembly) | Commented byte-exact disassembly of The Maze of Galious / Knightmare II (MSX) | 3 | 🟢 | Assembly |
| [The Need decomp](https://github.com/trapexit/3do-decomp-nfs) | Decompilation of The Need for Speed (3DO) | 3 | 🟢 | C |
| [Thexder disassembly](https://github.com/hitchhikr/thexder) | Complete disassembly of Thexder (Amiga) | 3 | 🟢 | Assembly |
| [Time Pilot disassembly](https://github.com/antxiko/TimePilot-disassembly) | Commented byte-exact disassembly of Time Pilot (MSX) | 3 | 🟢 | Assembly |
| [Top Spin 4 decomp](https://github.com/g-guthrie/topspin4-decomp) | Clean-room decompilation and source reconstruction of Top Spin 4 | 3 | 🟢 | Python |
| [Twin Bee disassembly](https://github.com/antxiko/TwinBee-disassembly) | Commented byte-exact disassembly of Twin Bee (MSX, Konami, 1986) | 3 | 🟢 | Assembly |
| [Vampire Killer disassembly](https://github.com/0xe1f/VampireKiller) | Disassembly of Vampire Killer (MSX2) | 3 | 🟢 | Assembly |
| [various ZX Spectrum adventure games disassembly](https://github.com/pobtastic/adventure-games) | SkoolKit disassemblies of various ZX Spectrum adventure games | 3 | 🟢 | Visual Basic 6.0 |
| [180 disassembly](https://github.com/pobtastic/180) | A disassembly of 180, created using SkoolKit. | 2 | 🟢 | Visual Basic 6.0 |
| [3D Golf Simulation disassembly](https://github.com/antxiko/3DGolfSimulation-disassembly) | Commented disassembly of 3D Golf Simulation (MSX, T&E Soft, 1983) | 2 | 🟢 | Python |
| [Acornsoft Planetoid disassembly](https://github.com/mikroman/planet) | Disassembly of Acornsoft Planetoid (BBC Micro) | 2 | 🔴 | Assembly |
| [Athletic Land disassembly](https://github.com/antxiko/AthleticLand-disassembly) | Commented byte-exact disassembly of Athletic Land (MSX) | 2 | 🟢 | Assembly |
| [Bomber Man disassembly](https://github.com/antxiko/Bomberman-disassembly) | Commented byte-exact disassembly of Bomber Man (MSX) | 2 | 🟢 | Python |
| [Cabbage Patch Kids disassembly](https://github.com/antxiko/CabbagePatchKids-disassembly) | Commented byte-exact disassembly of Cabbage Patch Kids (MSX) | 2 | 🟢 | Assembly |
| [Casio World Open disassembly](https://github.com/antxiko/CasioWorldOpen-disassembly) | Commented disassembly of Casio World Open (MSX, Casio, 1985) | 2 | 🟢 | Assembly |
| [Circus Charlie disassembly](https://github.com/antxiko/CircusCharlie-disassembly) | Commented byte-exact disassembly of Circus Charlie (MSX) | 2 | 🟢 | Python |
| [Comic Bakery disassembly](https://github.com/antxiko/ComicBakery-disassembly) | Commented byte-exact disassembly of Comic Bakery (MSX) | 2 | 🟢 | Python |
| [Contra disassembly](https://github.com/antxiko/Contra-disassembly) | Commented byte-exact disassembly of Contra (MSX) | 2 | 🟢 | Assembly |
| [Demonia disassembly](https://github.com/antxiko/Demonia-disassembly) | Commented byte-exact disassembly of Demonia (MSX) | 2 | 🟢 | Assembly |
| [Dragster-Disassembly](https://github.com/CelestialAmber/Dragster-Disassembly) | Disassembly of Dragster | 2 | 🔴 | Assembly |
| [Dunk Shot disassembly](https://github.com/antxiko/DunkShot-disassembly) | Commented byte-exact disassembly of Dunk Shot (MSX) | 2 | 🟢 | Assembly |
| [Earth Shaker disassembly](https://github.com/Bedazzle/Earth-shaker) | Disassembly of Earth Shaker (ZX Spectrum) | 2 | 🟢 | Assembly |
| [El Descubrimiento de America disassembly](https://github.com/antxiko/Descubrimiento-disassembly) | Commented byte-exact disassembly of El Descubrimiento de America (MSX) | 2 | 🟢 | Assembly |
| [Feud disassembly](https://github.com/hitchhikr/feud) | Complete disassembly of Feud (Amiga) | 2 | 🔴 | Assembly |
| [Frogger disassembly](https://github.com/antxiko/Frogger-disassembly) | Commented byte-exact disassembly of Frogger (MSX) | 2 | 🟢 | Python |
| [Frontier: Elite II decomp](https://github.com/neozeed/frontvm-20040517) | Decompilation of Frontier: Elite II (Atari ST) running without direct OS and hardware calls | 2 | 🔴 | Assembly |
| [Ganbare Goemon! Karakuri Dochu disassembly](https://github.com/antxiko/GanbareGoemon-disassembly) | Commented byte-exact disassembly of Ganbare Goemon! Karakuri Dochu (MSX) | 2 | 🟢 | Assembly |
| [Genetic Drift disassembly](https://github.com/scottschram/apple_ii_genetic_drift_disassembly) | Disassembly of Genetic Drift (Apple II) | 2 | 🟢 | Assembly |
| [Hinotori / Firebird disassembly](https://github.com/antxiko/Hinotori-disassembly) | Commented byte-exact disassembly of Hinotori / Firebird (MSX) | 2 | 🟢 | Assembly |
| [Hole in One disassembly](https://github.com/antxiko/HoleInOne-disassembly) | Commented disassembly of Hole in One (MSX, HAL Laboratory, 1984) | 2 | 🟢 | Assembly |
| [Hole in One Professional disassembly](https://github.com/antxiko/HoleInOnePro-disassembly) | Commented byte-exact disassembly of Hole in One Professional (MSX) | 2 | 🟢 | Assembly |
| [Hollywood Poker disassembly](https://github.com/pobtastic/hollywoodpoker) | A disassembly of Hollywood Poker, created using SkoolKit. | 2 | 🟡 | Visual Basic 6.0 |
| [How to be a Complete Bastard disassembly](https://github.com/pobtastic/howtobeacompletebastard) | A disassembly of How To Be A Complete Bastard, created using SkoolKit. | 2 | 🟢 | Python |
| [Hyper Olympic 1 disassembly](https://github.com/antxiko/HyperOlympic1-disassembly) | Commented byte-exact disassembly of Hyper Olympic 1 (MSX) | 2 | 🟢 | Python |
| [Hyper Olympic 2 disassembly](https://github.com/antxiko/HyperOlympic2-disassembly) | Commented byte-exact disassembly of Hyper Olympic 2 (MSX) | 2 | 🟢 | Python |
| [Hyper Rally disassembly](https://github.com/antxiko/HyperRally-disassembly) | Commented byte-exact disassembly of Hyper Rally (MSX) | 2 | 🟢 | Python |
| [Hyper Sports 1 disassembly](https://github.com/antxiko/HyperSports1-disassembly) | Commented byte-exact disassembly of Hyper Sports 1 (MSX) | 2 | 🟢 | Python |
| [Hyper Sports 2 disassembly](https://github.com/antxiko/HyperSports2-disassembly) | Commented byte-exact disassembly of Hyper Sports 2 (MSX) | 2 | 🟢 | Assembly |
| [Hyper Sports 3 disassembly](https://github.com/antxiko/HyperSports3-disassembly) | Commented byte-exact disassembly of Hyper Sports 3 (MSX) | 2 | 🟢 | Assembly |
| [King Kong 2 disassembly](https://github.com/antxiko/KingKong2-disassembly) | Commented byte-exact disassembly of King Kong 2 (MSX) | 2 | 🟢 | Assembly |
| [King's Valley disassembly](https://github.com/antxiko/KingsValley-disassembly) | Commented byte-exact disassembly of King's Valley (MSX) | 2 | 🟢 | Assembly |
| [knightmare](https://github.com/tetracorp/knightmare) | Disassembly and analysis of Knightmare (Amiga RPG, 1991) | 2 | 🟡 | Assembly |
| [Konami's Baseball disassembly](https://github.com/antxiko/KonamisBaseball-disassembly) | Commented byte-exact disassembly of Konami's Baseball (MSX) | 2 | 🟢 | Assembly |
| [Konami's Billiards disassembly](https://github.com/antxiko/KonamisBilliards-disassembly) | Commented byte-exact disassembly of Konami's Billiards (MSX) | 2 | 🟢 | Assembly |
| [Konami's Boxing disassembly](https://github.com/antxiko/Boxing-disassembly) | Commented byte-exact disassembly of Konami's Boxing (MSX) | 2 | 🟢 | Assembly |
| [Konami's Game Master 2 disassembly](https://github.com/antxiko/GameMaster2-disassembly) | Commented byte-exact disassembly of Konami's Game Master 2 (MSX) | 2 | 🟢 | Assembly |
| [Konami's Game Master disassembly](https://github.com/antxiko/GameMaster-disassembly) | Commented byte-exact disassembly of Konami's Game Master (MSX) | 2 | 🟢 | Assembly |
| [Konami's Golf disassembly](https://github.com/antxiko/KonamisGolf-disassembly) | Commented byte-exact disassembly of Konami's Golf (MSX) | 2 | 🟢 | Assembly |
| [Konami's Mahjong Dojo disassembly](https://github.com/antxiko/KonamisMahjongDojo-disassembly) | Commented byte-exact disassembly of Konami's Mahjong Dojo (MSX) | 2 | 🟢 | Assembly |
| [Konami's Ping Pong disassembly](https://github.com/antxiko/KonamisPingPong-disassembly) | Commented byte-exact disassembly of Konami's Ping Pong (MSX) | 2 | 🟢 | Python |
| [Konami's Soccer disassembly](https://github.com/antxiko/KonamisSoccer-disassembly) | Commented byte-exact disassembly of Konami's Soccer (MSX) | 2 | 🟢 | Assembly |
| [Konami's Tennis disassembly](https://github.com/antxiko/KonamisTennis-disassembly) | Commented byte-exact disassembly of Konami's Tennis (MSX) | 2 | 🟢 | Assembly |
| [Magical Tree disassembly](https://github.com/antxiko/MagicalTree-disassembly) | Commented byte-exact disassembly of Magical Tree (MSX) | 2 | 🟢 | Python |
| [MASK III: VENOM Strikes Back disassembly](https://github.com/Bedazzle/Mask-3-Venom) | Disassembly of MASK III: VENOM Strikes Back (ZX Spectrum) | 2 | 🟢 | Assembly |
| [Mercenaries 2: World in Flames decomp](https://github.com/bstoney-yt/Mercenaries-2-Decompilation) | Reverse engineering of Mercenaries 2: World in Flames | 2 | 🟢 | Rust |
| [Metal Gear disassembly](https://github.com/antxiko/MetalGear-disassembly) | Commented byte-exact disassembly of Metal Gear (MSX) | 2 | 🟢 | Assembly |
| [Monkey Academy disassembly](https://github.com/antxiko/MonkeyAcademy-disassembly) | Commented byte-exact disassembly of Monkey Academy (MSX) | 2 | 🟢 | Assembly |
| [Mopi Ranger disassembly](https://github.com/antxiko/MopiRanger-disassembly) | Commented byte-exact disassembly of Mopi Ranger (MSX) | 2 | 🟢 | Python |
| [Nemesis 3 disassembly](https://github.com/antxiko/Nemesis3-disassembly) | Commented byte-exact disassembly of Nemesis 3 (MSX) | 2 | 🟢 | Assembly |
| [Penguin Adventure / Yume Tairiku Adventure disassembly](https://github.com/antxiko/PenguinAdventure-disassembly) | Commented byte-exact disassembly of Penguin Adventure / Yume Tairiku Adventure (MSX) | 2 | 🟢 | Assembly |
| [Pheenix disassembly](https://github.com/pobtastic/pheenix) | SkoolKit disassembly of Pheenix (ZX Spectrum) | 2 | 🟢 | Visual Basic 6.0 |
| [Pitfall! disassembly](https://github.com/antxiko/Pitfall-MSX-disassembly) | Commented byte-exact disassembly of Pitfall! (MSX) | 2 | 🟢 | Assembly |
| [Plan B disassembly](https://github.com/TobyLobster/PlanB) | Disassembly of Plan B (BBC Micro) | 2 | 🟡 | Assembly |
| [Q*bert disassembly](https://github.com/antxiko/Qbert-disassembly) | Commented byte-exact disassembly of Q*bert (MSX) | 2 | 🟢 | Assembly |
| [Rastan Saga disassembly](https://github.com/antxiko/RastanSaga-disassembly) | Commented byte-exact disassembly of Rastan Saga (MSX) | 2 | 🟢 | Assembly |
| [Rescue Raiders disassembly](https://github.com/iolo/apple2-rescue-raiders-disasm) | Disassembly of Rescue Raiders (Apple II) | 2 | 🟢 | Assembly |
| [Road Fighter disassembly](https://github.com/antxiko/RoadFighter-disassembly) | Commented byte-exact disassembly of Road Fighter (MSX) | 2 | 🟢 | Python |
| [Robotron: 2084 disassembly](https://github.com/pobtastic/robotron2084) | SkoolKit disassembly of Robotron: 2084 (ZX Spectrum) | 2 | 🟢 | Visual Basic 6.0 |
| [Sea Wolf / Missile disassembly](https://github.com/astrocadester/SeaWolf-Missile) | Disassembly of Sea Wolf / Missile (Bally Astrocade) | 2 | 🟢 | Assembly |
| [Sea Wolf II disassembly](https://github.com/astrocadester/SeaWolfII) | Disassembly of Sea Wolf II (Bally Astrocade) | 2 | 🟢 | Assembly |
| [Shalom disassembly](https://github.com/antxiko/Shalom-disassembly) | Commented byte-exact disassembly of Shalom (MSX) | 2 | 🟢 | Assembly |
| [Space Zap disassembly](https://github.com/astrocadester/SpaceZap) | Disassembly of Space Zap (Bally Astrocade) | 2 | 🟢 | Assembly |
| [Splitting Images/ Split Personalities disassembly](https://github.com/pobtastic/splittingimages) | A disassembly of Splitting Images, created using SkoolKit. | 2 | 🟡 | Visual Basic 6.0 |
| [Spy vs Spy III: Arctic Antics disassembly](https://github.com/hitchhikr/spyvsspy3) | Complete disassembly of Spy vs Spy III: Arctic Antics (Amiga) | 2 | 🟢 | Assembly |
| [Terminator Salvation](https://github.com/connieprice/Terminator-Salvation-Lua) | Decompilation of Terminator Salvation | 2 | 🟡 | Lua |
| [The Adventures of Robby Roto disassembly](https://github.com/astrocadester/RobbyRoto) | Disassembly of The Adventures of Robby Roto (Bally Astrocade) | 2 | 🟢 | Assembly |
| [The Goonies disassembly](https://github.com/antxiko/Goonies-disassembly) | Commented byte-exact disassembly of The Goonies (MSX) | 2 | 🟢 | Assembly |
| [The Incredible Hulk: Ultimate Destruction decomp](https://github.com/matthewfcarlson/thunderclap) | Decompilation of The Incredible Hulk: Ultimate Destruction | 2 | 🟢 | C++ |
| [The Treasure of Usas disassembly](https://github.com/antxiko/TreasureOfUsas-disassembly) | Commented byte-exact disassembly of The Treasure of Usas (MSX) | 2 | 🟢 | Assembly |
| [Tony Hawk's Underground 2 decomp](https://github.com/CanuckAussieKev/thug2-decomp) | Decompilation of Tony Hawk's Underground 2 | 2 | 🟢 | C++ |
| [Trailblazer disassembly](https://github.com/antxiko/Trailblazer-disassembly) | Commented byte-exact disassembly of Trailblazer (MSX) | 2 | 🟢 | Assembly |
| [War in Middle Earth disassembly](https://github.com/antxiko/WarinMiddleEarth-MSX-disassembly) | Commented byte-exact disassembly of War in Middle Earth (MSX) | 2 | 🟢 | Assembly |
| [Wizard of Wor disassembly](https://github.com/astrocadester/WizardOfWor) | Disassembly of Wizard of Wor (Bally Astrocade) | 2 | 🟢 | Assembly |
| [Yie Ar Kung-Fu disassembly](https://github.com/antxiko/YieArKungFu-disassembly) | Commented byte-exact disassembly of Yie Ar Kung-Fu (MSX) | 2 | 🟢 | Assembly |
| [Yie Ar Kung-Fu II disassembly](https://github.com/antxiko/YieArKungFu2-disassembly) | Commented byte-exact disassembly of Yie Ar Kung-Fu II (MSX) | 2 | 🟢 | Assembly |
| [ZX Spectrum games disassembly](https://github.com/jonsole/zx-spectrum-disassemblies) | Reproducible SkoolKit disassemblies of ZX Spectrum games, including Atic Atac | 2 | 🟢 | Python |
| [1987 Radio-86RK game Lestnica disassembly](https://github.com/begoon/lestnica) | Annotated Intel 8080 disassembly of the 1987 Radio-86RK game Lestnica | 1 | 🟢 | Assembly |
| [3do-decomp-pdwt](https://github.com/trapexit/3do-decomp-pdwt) | Decompiled version of Plumbers Don't Wear Ties (3DO, USA) | 1 | 🟢 | C |
| [Alien vs Predator decomp](https://github.com/Joshua-1248/Alien-V.S.-Predator-Atari-Jaguar-Decompilation) | Reconstructed decompilation of Alien vs Predator (Atari Jaguar) | 1 | 🟢 | Assembly |
| [Alien vs Predator decomp](https://github.com/Joshua-1248/Alien-V.S.-Predator-Atari-Jaguar-C-Decompilation) | C decompilation of Alien vs Predator (Atari Jaguar) | 1 | 🟢 | C |
| [Arkanoid disassembly](https://github.com/0xe1f/Arkanoid) | Disassembly of Arkanoid (MSX) | 1 | 🟢 | Assembly |
| [BBC Micro game Pipeline disassembly](https://github.com/mattgodbolt/pipeline-disasm) | Annotated disassembly of the BBC Micro game Pipeline | 1 | 🟢 | Python |
| [Bowling disassembly](https://github.com/munsie/bowling-2600-disassembly) | Disassembly of Bowling (Atari 2600) | 1 | 🔴 | Assembly |
| [Dino Eggs disassembly](https://github.com/mikroman/dinoeggs) | Disassembly of Dino Eggs (Commodore 64) | 1 | 🟡 | Assembly |
| [Dodge It disassembly](https://github.com/alex-west/ves-16) | Disassembly of Dodge It (Channel F Videocart 16) | 1 | 🔴 | Assembly |
| [Extra Bases disassembly](https://github.com/astrocadester/ExtraBases) | Disassembly of Extra Bases (Bally Astrocade) | 1 | 🟢 | Assembly |
| [Green Beret disassembly](https://github.com/1888games/GreenBeretC16) | Disassembly of Green Beret (Commodore 16) | 1 | 🟡 | Assembly |
| [Heartlight disassembly](https://github.com/Quaerendir/Heartlight) | Disassembly of Heartlight (Atari 8-bit, 1990) | 1 | 🟢 | Python |
| [King's Valley 2 disassembly](https://github.com/0xe1f/KingsValley2) | Disassembly of King's Valley 2 (MSX) | 1 | 🟢 | Assembly |
| [Madagascar decomp](https://github.com/MaxStache/MadagascarDecomp) | Decompilation of Madagascar (2005) | 1 | 🟢 | C++ |
| [Marvel Nemesis: Rise of the Imperfects decomp](https://github.com/Esoteric-Engineer/mnroi) | Decompilation of Marvel Nemesis: Rise of the Imperfects | 1 | 🟢 | C |
| [Percy the Potty Pigeon disassembly](https://github.com/pobtastic/percythepottypigeon) | A disassembly of Percy The Potty Pigeon, created using SkoolKit. | 1 | 🟢 | Visual Basic 6.0 |
| [populous](https://github.com/tetracorp/populous) | Disassembly and analysis of Populous (Amiga) | 1 | 🟡 | Assembly |
| [Rally-X disassembly](https://github.com/ricbit/rallyx) | Full disassembly of Rally-X (MSX) | 1 | 🟢 | Assembly |
| [Redhawk disassembly](https://github.com/Ritchie333/redhawk) | Disassembly of Redhawk (ZX Spectrum, 1986) | 1 | 🟢 | Visual Basic 6.0 |
| [Saboteur disassembly](https://github.com/Bedazzle/spectrum-saboteur1-rev) | Full disassembly of Saboteur (ZX Spectrum) | 1 | 🟢 | Assembly |
| [Sargon III disassembly](https://github.com/Oric4ever/sargon3_disassembly) | Commented disassembly of Sargon III (Apple II) | 1 | 🟡 | C |
| [Snatcher CD-ROMantic disassembly](https://github.com/buranko-kun/snatcher) | Disassembly of Snatcher CD-ROMantic (PC Engine CD) | 1 | 🟢 | C++ |
| [Sonic the Hedgehog (DIDJ)](https://github.com/ArchiverXP/sncdecomp) | Matching decompilation of Sonic the Hedgehog (LeapFrog Didj, 2008) | 1 | 🟡 | C++ |
| [Sparkplug engine used decomp](https://github.com/AnDi-SD/SparkplugEngineResearch) | Reverse engineering and decompilation of the Sparkplug engine used by Winx Club games | 1 | 🟢 | C++ |
| [The Hobbit v1.0 disassembly](https://github.com/basf-c60/thehobbitv1.0) | Disassembly of The Hobbit v1.0 (ZX Spectrum, 1982) | 1 | 🟢 | HTML |
| [The Pro Yakyuu Gekitotsu Pennant Race disassembly](https://github.com/antxiko/PennantRace-disassembly) | Commented byte-exact disassembly of The Pro Yakyuu Gekitotsu Pennant Race (MSX) | 1 | 🟢 | Assembly |
| [Twin Kingdom Valley disassembly](https://github.com/mcnalu/twinkingdomvalley-dasm) | Disassembly of Twin Kingdom Valley (BBC Micro) | 1 | 🔴 | C |
| [VIC-20 games disassembly](https://github.com/dhansel/vic20games) | Disassemblies of VIC-20 games | 1 | 🔴 | Assembly |
| [Zaxxon disassembly](https://github.com/mikroman/ZAXXON) | Disassembly of Zaxxon (Commodore 64) | 1 | 🟢 | Assembly |
| [1997 Digimon virtual pet firmware disassembly](https://github.com/willmcginnis/digimon-vpet-1997-disassembly) | Literate disassembly of the 1997 Digimon virtual pet firmware (Ver. 1 and 2) | 0 | 🟢 | Python |
| [ABM Disassembly](https://6502disassembly.com/a2-abm/ABM.html) | Disassembly of ABM (Assembly) |  | ⚪ |  |
| [Adventure Disassembly](https://www.qotile.net/minidig/disassembly/adventure.asm) | Disassembly of Adventure (Assembly) |  | ⚪ |  |
| [Air-Sea Battle Disassembly](https://www.qotile.net/minidig/disassembly/air_sea_battle.asm) | Disassembly of Air-Sea Battle (Assembly) |  | ⚪ |  |
| [Amiga game Flood decomp](https://github.com/VonKossa/ReFlood) | Source reconstruction of the Amiga game Flood | 0 | 🟢 | C |
| [Another World that rebuilds byte-matching binaries decomp](https://github.com/ArqueologiaDigital/another-world-source-reconstruction) | Source reconstruction of Another World that rebuilds byte-matching binaries for many versions | 0 | 🟢 | Assembly |
| [Berzerk Disassembly](https://www.qotile.net/minidig/disassembly/berzerk.asm) | Disassembly of Berzerk (Assembly) |  | ⚪ |  |
| [Bomber Disassembly](https://6502disassembly.com/a2-bomber/Bomber.html) | Disassembly of Bomber (Assembly) |  | ⚪ |  |
| [CJ's Elephant Antics disassembly](https://github.com/petemoore/cjs_elephant_antics_disassembly) | Disassembly of CJ's Elephant Antics (ZX Spectrum) | 0 | 🔴 | Go |
| [Combat Disassembly](https://www.qotile.net/minidig/disassembly/dicombat.asm) | Disassembly of Combat (Assembly) |  | ⚪ |  |
| [Cosmic Ark Disassembly](https://www.qotile.net/minidig/disassembly/CosmicArk.asm) | Disassembly of Cosmic Ark (Assembly) |  | ⚪ |  |
| [Cruising on Broadway disassembly](https://github.com/georgeprout/Cruising-on-Broadway) | SkoolKit disassembly of Cruising on Broadway (ZX Spectrum) | 0 | 🔴 | HTML |
| [CSBwin](http://www.dianneandpaul.net/CSBwin/) | Disassembly of Dungeon Master (C++) |  | ⚪ |  |
| [Disassemblies of classic BBC Micro games](https://www.level7.org.uk/miscellany) | Disassembly of Atic Atac, Boffin (Assembly) |  | ⚪ |  |
| [Donkey Kong Disassembly](https://www.qotile.net/minidig/disassembly/dk.asm) | Disassembly of Donkey Kong (Assembly) |  | ⚪ |  |
| [Elite: Harmless](https://codeberg.org/Kroc/elite-harmless) | Disassembly of the Commodore 64 port of Elite, with improvements |  | ⚪ |  |
| [Exile (Enhanced version) disassembly](https://level7.org.uk/miscellany/exile-enhanced-disassembly.txt) | Disassembly of Exile (Assembly) |  | ⚪ |  |
| [FAC](https://github.com/Quaerendir/FAC) | FAC (Atari 8-bit, 1992) reconstructed from its BASIC type-in listing | 0 | 🟢 | Python |
| [Indy 500 Disassembly](https://www.qotile.net/minidig/disassembly/indy_500_pass_01.asm) | Disassembly of Indy 500 (Assembly) |  | ⚪ |  |
| [Jawbreaker Disassembly](https://www.qotile.net/minidig/disassembly/jaw_breaker.asm) | Disassembly of Jawbreaker (Assembly) |  | ⚪ |  |
| [Kaboom! Disassembly](https://www.qotile.net/minidig/disassembly/kaboom.asm) | Disassembly of Kaboom! (Assembly) |  | ⚪ |  |
| [Karateka disassembly](https://github.com/gmegidish/karateka-disassembly) | Disassembly of Karateka | 0 | 🟢 | Assembly |
| [m1-decomp](https://codeberg.org/marathon-speedrun-developers/m1-decomp) | Decompilation of PPC Marathon to compare Aleph One with the original Mac version |  | ⚪ |  |
| [Maniac Mansion decomp](https://github.com/kernaltrap8/mansiondecomp) | Reverse engineering and decompilation of Maniac Mansion (Enhanced) | 0 | 🟡 |  |
| [Moonlight Madness disassembly](https://github.com/pobtastic/moonlightmadness) | SkoolKit disassembly of Moonlight Madness (ZX Spectrum) | 0 | 🟢 | Visual Basic 6.0 |
| [Mystery House decomp](https://github.com/kDylanHayes/mystery-house-decompilation) | Decompilation of Mystery House (Apple II, 1980) | 0 | 🟢 | Python |
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
| [TheJet](https://github.com/Quaerendir/TheJet) | The Jet (Atari 8-bit, 1992) reconstructed from its 6502 type-in listing | 0 | 🟢 | Python |
| [Venture Disassembly](https://www.qotile.net/minidig/disassembly/venture.asm) | Disassembly of Venture (Assembly) |  | ⚪ |  |
| [ZX Spectrum games disassembly](https://github.com/georgeprout/disassembly) | Disassemblies of ZX Spectrum games | 0 | 🔴 | HTML |

## Matching Decompilations — PC / DOS / Windows

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Devilution](https://github.com/diasurgical/devilution) | Reverse-engineered Diablo 1 source reconstructed from the original binary | 9,014 | 🟡 | C++ |
| [Ship of Harkinian](https://github.com/HarbourMasters/Shipwright) | PC port of Ocarina of Time built on the OoT decompilation | 5,753 | 🟢 | C |
| [Space Cadet Pinball](https://github.com/k4zmu2a/SpaceCadetPinball) | Decompilation of 3D Pinball for Windows – Space Cadet (PC, 1995) | 4,738 | 🟡 | C++ |
| [LEGO Island](https://github.com/isledecomp/isle) | Matching decompilation of LEGO Island (PC, 1997) | 3,495 | 🟢 | C++ |
| [2 Ship 2 Harkinian](https://github.com/2ship2harkinian/2ship2harkinian) | PC port of Majora's Mask built on the MM decompilation | 2,375 | 🟢 | C |
| [SDLPoP](https://github.com/NagyD/SDLPoP) | An open-source port of Prince of Persia, based on the disassembly of the DOS version. | 1,301 | 🟢 | C |
| [gta-reversed](https://github.com/gta-reversed/gta-reversed) | Reimplementation of GTA San Andreas 1.0 US via reverse engineering | 1,159 | 🟢 | C++ |
| [Touhou (PC-98) (ReC98)](https://github.com/nmlgc/ReC98) | Decompilation of Touhou (PC-98) (ReC98) | 882 | 🟢 | Assembly |
| [Sonic Mania (RSDKModding)](https://github.com/RSDKModding/Sonic-Mania-Decompilation) | Matching decompilation of Sonic Mania and its Retro Engine (RSDKv5) (PC, 2017) | 825 | 🟢 | C |
| [nox-decomp (Nox)](https://github.com/opennox/opennox) | Decompilation of Nox (Westwood, 2000) | 635 | 🟢 | C |
| [Touhou 06: The Embodiment of Scarlet Devil](https://github.com/GensokyoClub/th06) | Matching decompilation of Touhou 06: The Embodiment of Scarlet Devil (PC, 2002) | 621 | 🟢 | C++ |
| [reVC](https://github.com/mrxenginner/reVC) | Reverse engineered source of GTA Vice City (reVC) | 450 | 🟢 | C++ |
| [Fallout 2 (fallout2-re)](https://github.com/alexbatalov/fallout2-re) | Reverse-engineered source of Fallout 2 (PC, 1998) | 411 | 🟡 | C |
| [wowdecomp (World of Warcraft)](https://github.com/SatyPardus/wowdecomp) | Decompilation of the World of Warcraft client | 406 | 🟢 | C++ |
| [reconstruction-of-zzt](https://github.com/asiekierka/reconstruction-of-zzt) | Reconstructed source code of ZZT | 386 | 🟡 | Pascal |
| [Deus Ex: Human Revolution (cdcEngine)](https://github.com/rrika/cdcEngineDXHR) | Decompilation of Deus Ex: Human Revolution and its cdcEngine (PC, 2011) | 326 | 🟢 | C++ |
| [starflight-reverse](https://github.com/s-macke/starflight-reverse) | Reverse-engineered Forth source of the 1986 DOS game Starflight | 242 | 🟢 | C |
| [re-plants-vs-zombies](https://github.com/Patoke/re-plants-vs-zombies) | Rebuild of Plants vs. Zombies GOTY functionality via reverse engineering | 241 | 🟢 | C++ |
| [Need for Speed: Most Wanted](https://github.com/dbalatoni13/nfsmw) | Matching decompilation of Need for Speed: Most Wanted (PC, 2005) | 236 | 🟢 | C++ |
| [D2MOO](https://github.com/ThePhrozenKeep/D2MOO) | Reimplementation of Diablo II game code with patching facilities for modders | 193 | 🟢 | C++ |
| [Crimsonland](https://github.com/banteg/crimson) | Matching decompilation of Crimsonland (PC, 2003) | 192 | 🟢 | Python |
| [fallout1-re](https://github.com/alexbatalov/fallout1-re) | Reverse engineered source of Fallout 1 | 179 | 🔴 | C |
| [Chronoshift](https://github.com/TheAssemblyArmada/Chronoshift) | Open source reimplementation of Red Alert in C++ | 175 | 🗄️ | C++ |
| [Command & Conquer: Red Alert 2 (Ares)](https://github.com/Ares-Developers/Ares) | Decompilation of Command & Conquer: Red Alert 2 (PC) | 168 | 🟡 | HTML |
| [Ultima VII: The Black Gate (UltimaHacks)](https://github.com/JohnGlassmyer/UltimaHacks) | Decompilation of Ultima VII: The Black Gate (DOS) | 166 | 🔴 | Assembly |
| [sci-scripts](https://github.com/sluicebox/sci-scripts) | Decompiled scripts of Sierra SCI adventure games | 156 | 🟢 | SuperCollider |
| [resident-evil-pc-decomp](https://github.com/ecruells/resident-evil-pc-decomp) | Decompilation of the Resident Evil 1 PC port | 152 | 🟢 | C++ |
| [SA-MP](https://github.com/dashr9230/SA-MP) | Matching decompilation of San Andreas Multiplayer 0.3.7 | 152 | 🟢 | C |
| [Neverwinter Nights: Enhanced Edition (NWNX:EE unified)](https://github.com/nwnxee/unified) | Decompilation of Neverwinter Nights: Enhanced Edition (PC) | 151 | 🟢 | C++ |
| [Chinese board game Richman 4 decomp](https://github.com/mytbk/rich4) | Reverse engineering of the Chinese board game Richman 4 (DOS) | 150 | 🟢 | Assembly |
| [WorldOfTanks-Decompiled](https://github.com/StranikS-Scan/WorldOfTanks-Decompiled) | Unpacked and decompiled versions of xml- and pyc-files of WorldOfTanks | 150 | 🟢 | Python |
| [Cosmo's Cosmic Adventure](https://github.com/smitelli/cosmore) | Matching decompilation of Cosmo's Cosmic Adventure (DOS, 1992) | 146 | 🟡 | C |
| [GD-Decompiled](https://github.com/Wyliemaster/GD-Decompiled) | Attempt to recover Geometry Dash 2.11 source through reverse engineering | 146 | 🗄️ | C++ |
| [Spider-Man (2000)](https://github.com/krystalgamer/spidey-decomp) | Decompilation of the PC port of Neversoft's Spider-Man (PC, 2000) | 142 | 🟢 | C |
| [devilution](https://github.com/galaxyhaxz/devilution) | Original Devilution reverse engineered Diablo source | 133 | 🔴 | C |
| [Grand Theft Auto 2 (gta2_re)](https://github.com/CriminalRETeam/gta2_re) | Reimplementation of Grand Theft Auto 2 v10.5 from the PC version (PC, 1999) | 131 | 🟢 | C++ |
| [PlantsVsZombies-decompilation](https://github.com/ruslan831/PlantsVsZombies-decompilation) | Decompilation of Plants vs. Zombies 0.9.9 | 122 | 🟢 | C |
| [Tomb Raider III decomp](https://github.com/Trxyebeep/tomb3) | Decompilation of Tomb Raider III (PC) | 118 | 🟡 | C++ |
| [nfsu2-re](https://github.com/yugecin/nfsu2-re) | Reverse engineering project for Need for Speed Underground 2 | 117 | 🟡 | C |
| [Darktide-Source-Code](https://github.com/Aussiemon/Darktide-Source-Code) | Decompiled game scripts of Warhammer 40,000: Darktide (PC) | 115 | 🟢 | Lua |
| [Black & White](https://github.com/openblack/bw1-decomp) | Matching decompilation of Black & White (PC, 2001) | 113 | 🟢 | C++ |
| [Magic: The Gathering – Shandalar (Shandalar (patched))](https://github.com/ShandalarMagic/Shandalar) | Decompilation of Magic: The Gathering – Shandalar (PC) | 106 | 🔴 | C |
| [RBXGSdecomp](https://github.com/RBLXDecomp/RBXGSdecomp) | Decompilation of the November 2007 Roblox client | 105 | 🟢 | C++ |
| [The Temple of Elemental Evil (TemplePlus)](https://github.com/GrognardsFromHell/TemplePlus) | Decompilation of The Temple of Elemental Evil (PC) | 105 | 🟢 | C++ |
| [YandereSimulatorDecompiled](https://github.com/LordEnma/YandereSimulatorDecompiled) | Decompiled code of the game Yandere Simulator | 104 | 🟢 | C# |
| [CircleShootApp](https://github.com/alula/CircleShootApp) | Zuma Deluxe 1.0.0 decompilation | 103 | 🟢 | C++ |
| [racers](https://github.com/isledecomp/racers) | Decompilation of LEGO Racers (1999) | 102 | 🟢 | C++ |
| [Baldur's Gate: Enhanced Edition (EEex)](https://github.com/Bubb13/EEex) | Decompilation of Baldur's Gate: Enhanced Edition (PC) | 99 | 🟢 | Lua |
| [Vermintide-2-Source-Code](https://github.com/Aussiemon/Vermintide-2-Source-Code) | Decompiled LuaJIT game scripts of Warhammer: Vermintide 2 (PC) | 98 | 🟢 | Lua |
| [Command & Conquer: Tiberian Sun (Vinifera)](https://github.com/Vinifera-Developers/Vinifera) | Decompilation of Command & Conquer: Tiberian Sun (PC) | 97 | 🟢 | C++ |
| [nolfsrc](https://github.com/nolffan/nolfsrc) | Decompiled source code of No One Lives Forever | 97 | 🟢 | C++ |
| [Tomb Raider: The Last Revelation decomp](https://github.com/Trxyebeep/TOMB4) | Decompilation of Tomb Raider: The Last Revelation (PC) | 96 | 🟡 | C++ |
| [msgi](https://github.com/MrSapps/msgi) | Metal Gear Solid Integral PC reverse engineering | 95 | 🗄️ | C++ |
| [Tomb Raider Chronicles decomp](https://github.com/Trxyebeep/TOMB5) | Decompilation of Tomb Raider Chronicles (PC) | 94 | 🟡 | C++ |
| [dangerous-dave-re](https://github.com/gmegidish/dangerous-dave-re) | Reverse engineering of Dangerous Dave in the Haunted Mansion | 90 | 🔴 | Python |
| [iwd2-re](https://github.com/alexbatalov/iwd2-re) | Reverse engineered source of Icewind Dale 2 | 90 | 🟡 | C++ |
| [OpenLRR](https://github.com/trigger-segfault/OpenLRR) | Open source reimplementation of LEGO Rock Raiders | 88 | 🟡 | C++ |
| [Stronghold Crusader (Unofficial Crusader Patch)](https://github.com/UnofficialCrusaderPatch/UnofficialCrusaderPatch) | Decompilation of Stronghold Crusader (PC) | 85 | 🟢 |  |
| [chocolatekeen](https://github.com/jamesfmackenzie/chocolatekeen) | Reverse engineered Commander Keen in C/C++ and SDL | 83 | 🟢 | C |
| [Star Wars Episode I: Racer](https://github.com/tim-tim707/SW_RACER_RE) | Matching decompilation of Star Wars Episode I: Racer (PC, 1999) | 83 | 🟢 | C |
| [StardewValleyDecompiled](https://github.com/Dannode36/StardewValleyDecompiled) | Stardew Valley 1.6 decompiled to .NET 6 | 82 | 🟡 | C# |
| [dx-ball](https://github.com/N0zoM1z0/dx-ball) | Source reconstruction of DX-Ball 1.07 verified against the original binary | 76 | 🟢 | Python |
| [re47](https://github.com/0danny/re47) | Hitman: Codename 47 decompilation project (archived) | 74 | 🗄️ | C++ |
| [saga](https://github.com/opensagadev/saga) | Matching decompilation of LEGO Star Wars: The Complete Saga | 74 | 🟢 | C++ |
| [gdp](https://github.com/camila314/gdp) | Decompilations of Geometry Dash physics functions | 73 | 🟡 | C++ |
| [ReHitman](https://github.com/ReGlacier/ReHitman) | Hitman Codename 47 reverse engineering project | 73 | 🟢 | C++ |
| [TR2X](https://github.com/LostArtefacts/TR2X) | Decompilation project for Tomb Raider II (1997) | 72 | 🗄️ | C |
| [SkiFree](https://github.com/yuv422/skifree_decomp) | Matching decompilation of SkiFree (PC, 1991) | 71 | 🔴 | Assembly |
| [Curse of the Azure Bonds decomp](https://github.com/simeonpilgrim/coab) | Reverse-engineered source of Curse of the Azure Bonds (DOS) converted to C# | 70 | 🟡 | C |
| [Jones3D engine of Indiana Jones and the Infernal Machine decomp](https://github.com/smlu/OpenJones3D) | Reverse engineering of the Jones3D engine of Indiana Jones and the Infernal Machine (PC) | 69 | 🟢 | C |
| [DokiDoki-Decompile](https://github.com/judge2020/DokiDoki-Decompile) | Decompiled Ren'Py scripts of Doki Doki Literature Club (PC) | 66 | 🗄️ | Ren'Py |
| [LEGO1.DLL disassembly](https://github.com/itsmattkc/LEGO1Disassemble) | Machine-automated compilable disassembly of LEGO1.DLL from LEGO Island (PC) | 63 | 🗄️ | C++ |
| [th07](https://github.com/some100/th07) | Decompilation of Touhou 7 Perfect Cherry Blossom 1.00b | 63 | 🟢 | C++ |
| [half-life1_win32_722](https://github.com/ScriptedSnark/half-life1_win32_722) | Reverse-engineered source of Half-Life 1 Net Test 1 (build 722) | 62 | 🟢 | C |
| [bookstory-en](https://github.com/xraymemory/bookstory-en) | Decompilation and English translation of the game BookStory | 61 | 🔴 | VBA |
| [classic DOS game Digger decomp](https://github.com/sobomax/digger) | Digger Remastered, a source reconstruction of the classic DOS game Digger | 59 | 🟢 | C |
| [Space Rangers HD: A War Apart](https://github.com/pakompom/SpaceRangersHD_decomp) | Matching decompilation of Space Rangers HD: A War Apart (PC, 2013) | 58 | 🟢 | Pascal |
| [BldMystery](https://github.com/smartblade/BldMystery) | Source code recovery of Severance: Blade of Darkness | 57 | 🟢 | Assembly |
| [RimWorld alpha builds made decomp](https://github.com/josh-m/RW-Decompile) | Decompiled source of RimWorld alpha builds made with ILSpy (PC) | 56 | 🔴 | C# |
| [Thunderball](https://github.com/teampopwork/Thunderball) | Decompilation of Peggle Deluxe 1.01 | 54 | 🟢 | C++ |
| [Carmageddon II: Carpocalypse Now decomp](https://github.com/madebr/rec2) | Reverse engineering of Carmageddon II: Carpocalypse Now (PC) | 53 | 🟢 | C |
| [th08](https://github.com/N0zoM1z0/th08) | Source reconstruction of Touhou 8 Imperishable Night | 53 | 🟢 | C++ |
| [Buckshot Roulette](https://github.com/uncreativeCultist/buckshot-decomp-public) | Decompilation of Buckshot Roulette (PC, 2023) | 52 | 🟡 | GDScript |
| [FEZ 1.0.6 decomp](https://github.com/dptug/FEZ) | Decompiled source code of FEZ 1.0.6 (PC) | 52 | 🔴 | C# |
| [Command & Conquer: Tiberian Sun (ts-patches)](https://github.com/CnCNet/ts-patches) | Decompilation of Command & Conquer: Tiberian Sun (PC) | 50 | 🟢 | C |
| [byte-tactics](https://github.com/HectorBailey/byte-tactics) | Matching decompilation of Total Annihilation | 48 | 🟢 | C++ |
| [Ballanced](https://github.com/doyaGu/Ballanced) | Reversed source code of the game Ballance | 47 | 🟢 | CMake |
| [Battlefield 2](https://github.com/kiwidoggie/breadflowerdos) | Matching decompilation of Battlefield 2 and Battlefield 2142 (PC, 2005) | 47 | 🟢 | C++ |
| [FlatOut 2](https://github.com/ZackWilde27/FlatOut-2-decomp) | Decompilation of FlatOut 2 (PC, 2006) | 46 | 🟡 | C |
| [Age of Wonders (aow-patch)](https://github.com/int19h/aow-patch) | Decompilation of Age of Wonders (PC) | 45 | 🔴 | C++ |
| [Celeste_Decompiled](https://github.com/TheCyndaquilDecompilers/Celeste_Decompiled) | Decompiled source of Celeste (XNA build 1.4.0.0) | 45 | 🔴 | C# |
| [Source-2-Decompiler](https://github.com/Dingf/Source-2-Decompiler) | Decompiler for Source 2 file formats | 45 | 🔴 | C++ |
| [Super ZZT decomp](https://github.com/asiekierka/reconstruction-of-super-zzt) | Source reconstruction of Super ZZT (DOS) | 45 | 🟡 | Pascal |
| [Freelancer-Decomp](https://github.com/FreelancerDecomp/Freelancer-Decomp) | Source code of Freelancer (2003) restored from the original binaries | 44 | 🟢 | C++ |
| [ShortLine (reSL)](https://github.com/konovalov-aleks/reSL) | Reversed source code of ShortLine v1.1 (DOS) | 44 | 🟢 | C++ |
| [wowdecomp15595 (World of Warcraft 4.3.4)](https://github.com/SatyPardus/wowdecomp15595) | Decompilation of the World of Warcraft 4.3.4 (build 15595) client | 43 | 🟢 | C++ |
| [Colin McRae Rally 2.0 (CMR2Decomp)](https://github.com/CMR2Decomp/CMR2Decomp) | Matching decompilation of Colin McRae Rally 2.0 (PC, 2000) | 42 | 🟢 | HTML |
| [EoSDecomp](https://github.com/wearrrrr/EoSDecomp) | Byte-accurate decompilation of Touhou 6 Embodiment of Scarlet Devil | 42 | 🟡 | C++ |
| [SCI-Decompilation-Archive](https://github.com/EricOakford/SCI-Decompilation-Archive) | Collection of decompiled source code for Sierra's SCI games | 42 | 🟡 | Scala |
| [samp-source](https://github.com/Dryxio/samp-source) | Byte-for-byte source rebuild of SA-MP 0.3.7 R5 | 40 | 🟢 | C++ |
| [SCUMM-Decompilation-Archive](https://github.com/EricOakford/SCUMM-Decompilation-Archive) | Collection of decompiled source code for Lucasfilm's SCUMM games | 40 | 🟡 | C |
| [deltamodkit](https://github.com/deltamodders/deltamodkit) | DELTARUNE GameMaker decompilation/port with modding support | 38 | 🟢 | Game Maker Language |
| [Carmageddon (dethrace-ported-to-web)](https://github.com/Carter54git/dethrace-ported-to-web) | Decompilation of Carmageddon (DOS) | 37 | 🟢 | C |
| [MapleStory GMS v95 client decomp](https://github.com/jon-zu/shroom95-decomp) | Decompilation of the MapleStory GMS v95 client (PC) | 37 | 🟡 | C++ |
| [Blood-RE](https://github.com/NBlood/Blood-RE) | Blood source code reconstruction (matching decompilation) | 35 | 🟢 | C++ |
| [Supaplex disassembly](https://github.com/cilliemalan/supaplex) | Disassembly of Supaplex (DOS) | 35 | 🟡 | Assembly |
| [decomp](https://github.com/cuellius/decomp) | Mount & Blade: Warband module decompiler | 34 | 🔴 | C# |
| [Most-Wanted-Vehicles-Decomp](https://github.com/Brawltendo/Most-Wanted-Vehicles-Decomp) | Matching decompilation of Need for Speed Most Wanted vehicle physics | 33 | 🔴 | C++ |
| [SADX-cutscene-decompilation](https://github.com/X-Hax/SADX-cutscene-decompilation) | Decompilation of Sonic Adventure DX cutscenes | 31 | 🟡 | C++ |
| [Bullfrog's Tube decomp](https://github.com/rep-stosw/tube-game-dos) | Reverse engineering and decompilation of Bullfrog's Tube (DOS) | 30 | 🔴 | C++ |
| [ReMoM](https://github.com/jbalcomb/ReMoM) | Re-assembly of Master of Magic v1.31 (DOS) | 30 | 🟢 | C |
| [Deltarune](https://github.com/TeamBlossomDevs/DeltaruneDecomp_beta) | Decompilation of Deltarune (PC, 2018) | 29 | 🟡 | Game Maker Language |
| [FUEL](https://github.com/widberg/FUELDecompilation) | Matching decompilation of FUEL (PC, 2009) | 29 | 🟢 | C++ |
| [Buckshot Roulette decomp](https://github.com/uncreativeCultist/buckshot-decomp-private) | Decompilation of Buckshot Roulette (PC) | 28 | 🟡 | GDScript |
| [Colin McRae Rally 2.0](https://github.com/pablocpas/CMR2Decomp) | Matching decompilation of Colin McRae Rally 2.0 (PC, 2000) | 27 | 🟢 | C++ |
| [Dungeon Master II: Skullkeep decomp](https://github.com/gbsphenx/skproject) | Reverse-engineered port of Dungeon Master II: Skullkeep for Windows | 27 | 🟢 | C++ |
| [Mafia: The City of Lost Heaven](https://github.com/Marvisak/mafia-re) | Matching decompilation of Mafia: The City of Lost Heaven (PC, 2002) | 27 | 🟢 | C++ |
| [Pizza-Tower-EXtracted](https://github.com/setupwitch/Pizza-Tower-EXtracted) | Semi-accurate decompilation of Pizza Tower | 27 | 🟢 | Game Maker Language |
| [th04](https://github.com/N0zoM1z0/th04) | Source reconstruction of Touhou 4 Lotus Land Story | 27 | 🟢 | Python |
| [Commander Keen 4-6 decomp](https://github.com/sparky4/keen4-6) | Source code reconstruction of Commander Keen 4-6 (DOS) | 26 | 🔴 | C |
| [Touhou 08: Imperishable Night](https://github.com/GensokyoClub/th08) | Matching decompilation of Touhou 08: Imperishable Night (PC, 2004) | 26 | 🟢 | C++ |
| [Tube](https://github.com/rep-stosw/tube64) | 64-bit port of the decompiled DOS game Tube (DOS, 1994) | 26 | 🟡 | C++ |
| [Sonic & Knuckles Collection disassembly](https://github.com/sonicretro/skc_disasm) | Disassembly of Sonic & Knuckles Collection (PC) | 25 | 🔴 | Batchfile |
| [Heroes of Might and Magic III decomp](https://github.com/sushi-shi/homm3-decomp) | Matching decompilation of Heroes of Might and Magic III (PC) | 24 | 🟢 | C++ |
| [Tomb Raider: Legend (cdcEngine)](https://github.com/TheIndra55/cdcEngine) | Decompilation of Tomb Raider: Legend (PC, 2006) | 24 | 🟡 | C++ |
| [WinFish](https://github.com/Vindirect/WinFish) | Insaniquarium Deluxe 1.1 decompilation | 24 | 🟢 | C |
| [Chip's Challenge disassembly](https://github.com/magical/CHIPS.EXE) | Disassembly of Chip's Challenge for Windows (1992) | 23 | 🔴 | Assembly |
| [DELTARUNE chapters decomp](https://github.com/TeamBlossomDevs/DeltaruneDecomp) | Decompilation of DELTARUNE chapters for modding (PC) | 23 | 🟢 | Game Maker Language |
| [Eushully-Decompiler](https://github.com/Kelebek1/Eushully-Decompiler) | Decompiler and recompiler for Eushully AGE engine scripts | 23 | 🟡 | C++ |
| [Fallout (F1DP)](https://github.com/Edw590/F1DP) | Decompilation of Fallout (DOS) | 23 | 🟡 | C |
| [Oregon Trail II](https://github.com/katstasaph/otii) | Matching decompilation of Oregon Trail II (PC, 1995) | 23 | 🟡 | C |
| [Cuphead-Decomp](https://github.com/tanosshi/Cuphead-Decomp) | Unofficial decompilation of Cuphead | 22 | 🟢 | C# |
| [Plants vs. Zombies](https://github.com/bluisblu/pvz) | Matching decompilation of Plants vs. Zombies (PC, 2009) | 22 | 🟢 | C |
| [Stunts decomp](https://github.com/4d-stunts/restunts) | Reverse engineering of Stunts (DOS) into reassemblable source | 22 | 🟢 | Assembly |
| [BBTools](https://github.com/JonMagon/BBTools) | Disassembly analysis and collection of tools for Beasts and Bumpkins (1997) | 21 | 🟢 | C++ |
| [bl-decompiled](https://github.com/Elletra/bl-decompiled) | Decompiled default TorqueScript files of Blockland (PC) | 21 | 🟡 | C# |
| [Restunts](https://github.com/xor2003/restunts) | Reverse-engineered source of Stunts (4D Sports Driving) for DOS | 21 | 🔴 | Assembly |
| [Sonic CD disassembly](https://github.com/sonicretro/scdpc_disasm) | Disassembly of Sonic CD (PC) | 21 | 🔴 | C# |
| [2.0.7 client decomp](https://github.com/xrip/uo-client) | Ultima Online T2A client recreated from a decompilation of the 2.0.7 client (PC) | 20 | 🟢 | C++ |
| [Cave-Story-Decompilation](https://github.com/GabrielRavier/Cave-Story-Decompilation) | Decompilation of Cave Story | 20 | 🗄️ | Assembly |
| [Bugs Bunny: Lost in Time](https://github.com/quantumdude836/BugsDecomp) | Matching decompilation of Bugs Bunny: Lost in Time (PC, 1999) | 19 | 🟡 | C |
| [Disney's Toontown Online decomp](https://github.com/open-toontown/toontown-online-2013-decompiled) | Reverse-engineered client and server source of Disney's Toontown Online (2013) | 19 | 🗄️ | Python |
| [Fallout Tactics: Brotherhood of Steel (FTSE)](https://github.com/melindil/FTSE) | Decompilation of Fallout Tactics: Brotherhood of Steel (PC) | 19 | 🟢 | C++ |
| [Ikachan 1.5.2 decomp](https://github.com/cuckydev/Ikachan) | Decompilation of Ikachan 1.5.2 (PC) | 19 | 🔴 | C++ |
| [Indiana Jones and the Infernal Machine decomp](https://github.com/andrewspode/infernal-machine-decomp-public) | Byte-matched decompilation of Indiana Jones and the Infernal Machine (PC) | 19 | 🟢 | C |
| [Sheep decomp](https://github.com/SDW-Community/sdw-decomp) | Byte-matching decompilation of Sheep, Dog 'n' Wolf (PC, 2001) | 19 | 🟢 | C++ |
| [psychonauts-decomp](https://github.com/DrDecki/psychonauts-decomp) | Decompilation project for Psychonauts | 18 | 🟢 | C |
| [Sonic Dream Team](https://github.com/dev-camo/project-lucid) | Decompilation of Sonic Dream Team (Mac) | 18 | 🟢 | C# |
| [Space Rangers](https://github.com/pakompom/SpaceRangers1_decomp) | Matching decompilation of Space Rangers (PC, 2002) | 18 | 🟢 | Pascal |
| [Syndicate (SyndicatFX)](https://github.com/swfans/syndicatfx) | Disassembly of Syndicate (DOS) | 18 | 🟢 | C |
| [Alien vs. Predator 2](https://github.com/lemiur/AVP2-Reconstructed) | Matching decompilation of Alien vs. Predator 2 (PC, 2001) | 17 | 🟢 | C++ |
| [Bio Menace](https://github.com/lethal-guitar/BioMenaceDecomp) | Matching decompilation of Bio Menace (DOS, 1993) | 16 | 🟡 | C |
| [Bloons TD 5](https://github.com/NKHook/BTD5-Decomp) | Matching decompilation of Bloons TD 5 (PC, 2011) | 16 | 🟡 | C++ |
| [LEGO Rock Raiders decomp](https://github.com/ProjectReversio/LegoRockRaiders) | Reverse engineering of LEGO Rock Raiders (PC) | 16 | 🟢 | C |
| [MicroProse's Magic: The Gathering decomp](https://github.com/benprew/microprose-shandalar-source) | Decompilation of MicroProse's Magic: The Gathering (Shandalar) | 16 | 🟢 | C |
| [Sid Meier's Civilization decomp](https://github.com/sjmelia/civd) | Reverse-engineered source code of Sid Meier's Civilization (DOS, 1991) | 16 | 🟢 | C |
| [th105](https://github.com/N0zoM1z0/th105) | Source reconstruction of Touhou Scarlet Weather Rhapsody 1.06a | 16 | 🟢 | C++ |
| [Carmageddon 2 decomp](https://github.com/Link4Electronics/Carpocalypse2) | Decompilation and native port of Carmageddon 2 (PC) | 15 | 🟢 | C |
| [Objects in Space decomp](https://github.com/Voidless7125/OIS-Decompile) | Decompilation of Objects in Space (PC) | 15 | 🟢 | C |
| [PC version of Cut the Rope decomp](https://github.com/CtRHome/CutTheRope-WindowsDecomp) | Decompilation of the PC version of Cut the Rope | 15 | 🗄️ | C# |
| [Real War](https://github.com/Francessco121/real-war-decomp) | Matching decompilation of Real War (PC, 2001) | 15 | 🟡 | Dart |
| [Vermintide-1-Source-Code](https://github.com/Aussiemon/Vermintide-1-Source-Code) | Decompiled LuaJIT game scripts of Warhammer: End Times - Vermintide (PC) | 15 | 🔴 | Lua |
| [zztasm](https://github.com/cknave/zztasm) | ZZT disassembly project (DOS) | 15 | 🔴 | C |
| [Crusader: No Remorse decomp](https://github.com/sebsebseb1982/crusader-no-remorse-decomp) | Decompilation of Crusader: No Remorse (DOS) | 14 | 🟢 | C++ |
| [FlatOut: Ultimate Carnage](https://github.com/ZackWilde27/FlatOut-UC-Decomp) | Decompilation of FlatOut: Ultimate Carnage (PC, 2008) | 14 | 🟡 | C++ |
| [LEGO Stunt Rally decomp](https://github.com/OpenLSR/OpenLSR) | Reverse engineering of LEGO Stunt Rally (PC) | 14 | 🟢 | C++ |
| [raymanarenadecomp](https://github.com/zZeck/raymanarenadecomp) | Rayman Arena decompilation early WIP made possible with Frida, Ghidra, Clang tools, and brains. | 14 | 🔴 | C++ |
| [Sheep decomp](https://github.com/lace22l/sheep-dog-n-wolf-decomp) | Decompilation of Sheep, Dog 'n' Wolf (PC) | 14 | 🟢 | Makefile |
| [Zuma Deluxe (ZumaTAS)](https://github.com/9933fa/Zuma-Deluxe-TAS) | Decompilation of Zuma Deluxe (PC) | 14 | 🟢 | JavaScript |
| [Final Fantasy XIV 1.23b Windows client decomp](https://github.com/swstegall/meteor-decomp) | Clean-room decompilation of the Final Fantasy XIV 1.23b Windows client | 13 | 🟢 | C++ |
| [Happy Wheels](https://github.com/Afterflash/HappyWheels) | Decompilation of Happy Wheels (Flash, 2010) | 13 | 🟡 | ActionScript |
| [Silent Storm decomp](https://github.com/met-nikita/Silent-Storm-Reconstruction) | Source reconstruction of Silent Storm (PC) | 13 | 🟢 | C++ |
| [Sonic Mania (Sonic-Mania-25MB)](https://github.com/ThisKwasior/Sonic-Mania-25MB) | Decompilation of Sonic Mania (PC) | 13 | 🟢 | C |
| [Touhou 8: Imperishable Night (th08-web)](https://github.com/N0zoM1z0/th08-web) | Decompilation of Touhou 8: Imperishable Night (PC) | 13 | 🟢 | C++ |
| [Ys VI: The Ark of Napishtim](https://github.com/GrantBenR/YsViDecomp) | Ghidra decompilation of Ys VI: The Ark of Napishtim, Steam version (PC, 2003) | 13 | 🟡 |  |
| [Arc System Works' Team Red battle engine decomp](https://github.com/WistfulHopes/REDEngine) | Decompilation of Arc System Works' Team Red battle engine (PC) | 12 | 🔴 | C++ |
| [Diablo II decomp](https://github.com/psi29a/d2decomped) | Decompilation of Diablo II (PC) | 12 | 🟢 | C++ |
| [LEGO Batman: The Videogame (mariopossamato)](https://github.com/mariopossamato/LEGO-Batman) | Matching decompilation of LEGO Batman: The Videogame (Mac OS X, 2008) | 12 | 🟡 |  |
| [Okami HD](https://github.com/Shintensu/OkamiHD-Decomp) | Decompilation of Okami HD (PC, 2017) | 12 | 🟡 | C++ |
| [Purble Place (PurblePlaceDecomp)](https://github.com/simontime/PurblePlaceDecomp) | Decompilation of Purble Place (PC) | 12 | 🔴 | C++ |
| [Redneck Rampage decomp](https://github.com/NBlood/Redneck-Rampage-RE) | Source code reconstruction of Redneck Rampage (DOS) | 12 | 🟢 | C |
| [Undertale Yellow](https://github.com/burnedpopcorn/UnderTale-Yellow-Decompilation) | Decompilation of Undertale Yellow v1.2.1 (PC, 2023) | 12 | 🟡 | Game Maker Language |
| [Cuphead](https://github.com/jmxamongusmodder/cuphead-decomp) | Decompilation of Cuphead (PC, 2017) | 11 | 🟡 | GLSL |
| [Duke1Decomp](https://github.com/lethal-guitar/Duke1Decomp) | Decompiled and reconstructed source snippets of Duke Nukem 1 (DOS) | 11 | 🟡 | Assembly |
| [FableDecomp](https://github.com/BuffJesus/FableDecomp) | Reconstruction of Fable: The Lost Chapters for 32-bit Windows | 11 | 🟢 | C++ |
| [GDDecompProject](https://github.com/melowody/GDDecompProject) | Decompilation project for Geometry Dash (PC) | 11 | 🔴 | C++ |
| [Legoland](https://github.com/marijnvdwerf/legoland) | Matching decompilation of Legoland (PC, 1999) | 11 | 🟢 | C |
| [Sonic Mania (Sonic-Mania-Decompilation)](https://github.com/DropSonic0/Sonic-Mania-Decompilation) | Decompilation of Sonic Mania (PC) | 11 | 🟢 | C |
| [Bloodborne PSX (BBPSX-Decompilation)](https://github.com/SonyEntertainmentNetwork/BBPSX-Decompilation) | Decompilation of Bloodborne PSX, Lilith Walther's demake of Bloodborne (PC) | 10 | 🔴 |  |
| [Hexen's ACS level scripts decomp](https://github.com/fragglet/hexen-acs-reconstructed) | Decompiled and reconstructed source of Hexen's ACS level scripts (DOS) | 10 | 🟢 | C |
| [Mortal Kombat 4 decomp](https://github.com/nathan-casabieille/mk4decomp) | Decompilation of Mortal Kombat 4 (PC, 1998) | 10 | 🟢 | C |
| [Nocturne](https://github.com/NearlyTRex/NocturneDecomp) | Decompilation of Nocturne (PC, 1999) | 10 | 🟢 | Assembly |
| [Red Alert 2: Yuri's Revenge engine gamemd.exe 1.001 decomp](https://github.com/r-melvin/gagarin) | Decompilation of the Red Alert 2: Yuri's Revenge engine gamemd.exe 1.001 (PC) | 10 | 🟢 | C++ |
| [The King of Fighters XIV decomp](https://github.com/WistfulHopes/KOFXIVDecomp) | Decompilation of The King of Fighters XIV (PC) | 10 | 🔴 | C++ |
| [Ultima V: Warriors of Destiny decomp](https://github.com/raldi/u5-decomp) | Decompilation of Ultima V: Warriors of Destiny (DOS) | 10 | 🔴 | C |
| [WarbladeSR](https://github.com/bbepis/WarbladeSR) | Decompilation and servicing patch for Warblade (PC) | 10 | 🟢 | C |
| [Civilization II decomp](https://github.com/richardpenman/civ2) | Decompilation of Civilization II (PC) | 9 | 🟢 | C |
| [Heroes of Might and Magic II decomp](https://github.com/sushi-shi/homm2-decomp) | Matching decompilation of Heroes of Might and Magic II (PC) | 9 | 🟢 | C++ |
| [Need decomp](https://github.com/melroy89/nfs3-re) | Reverse engineering and decompilation of Need for Speed III: Hot Pursuit (PC) | 9 | 🟢 | Python |
| [SCP - Containment Breach Multiplayer decomp](https://github.com/juanjp600/SCPCB-Multiplayer-decompiled) | Decompiled Blitz3D source of SCP - Containment Breach Multiplayer (PC) | 9 | 🟢 | BlitzBasic |
| [Snail Mail](https://github.com/banteg/snail) | Matching decompilation of Snail Mail (PC) | 9 | 🟢 | C |
| [th095](https://github.com/N0zoM1z0/th095) | Source reconstruction of Touhou Shoot the Bullet 1.02a | 9 | 🟢 | C++ |
| [Vice City Multiplayer 0.3z decomp](https://github.com/dashr9230/VC-MP) | Matching decompilation of Vice City Multiplayer 0.3z (GTA Vice City mod, PC) | 9 | 🟡 | C |
| [Final Fantasy IV (3D Remake)](https://github.com/GlitchedDeveloper/Babil-Decompilation-Project) | Decompilation of Final Fantasy IV (3D Remake) Steam version (PC, 2014) | 8 | 🟡 | C++ |
| [Freelancer decomp](https://github.com/HaydnTrigg/Freelancer) | Decompilation of Freelancer (PC) | 8 | 🟢 | C++ |
| [Krush Kill 'N Destroy Xtreme](https://github.com/Wyrelade/KKND-Decomp) | Matching decompilation of Krush Kill 'N Destroy Xtreme (PC, 1997) | 8 | 🟢 | C |
| [LEGO Creator: Knights' Kingdom](https://github.com/DavidGrice/knightskingdom) | Matching decompilation of LEGO Creator: Knights' Kingdom (PC, 2000) | 8 | 🟢 | JavaScript |
| [Lemmings Paintball](https://github.com/vonhoff/lemball-decomp) | Matching decompilation of Lemmings Paintball (PC, 1996) | 8 | 🟢 | C++ |
| [Magic: The Gathering decomp](https://github.com/rlerrr/shandalar-decomp) | Decompilation of Magic: The Gathering (Shandalar, MicroProse) | 8 | 🟢 | C |
| [Retro Engine v4 revision used decomp](https://github.com/RifiGD/RSDKv4-CD18) | Decompilation of the Retro Engine v4 revision used for Sonic CD (2018) | 8 | 🗄️ | C++ |
| [Sierra's AGI adventure games decomp](https://github.com/EricOakford/AGI-Decompilation-Archive) | Decompiled source code of Sierra's AGI adventure games | 8 | 🟡 | C |
| [Thief: Deadly Shadows](https://github.com/Veradictus/Thief3-Decomp) | Matching decompilation of Thief: Deadly Shadows (PC, 2004) | 8 | 🟢 | C++ |
| [Ultima V: Warriors of Destiny decomp](https://github.com/wonst719/u5d) | Decompilation of Ultima V: Warriors of Destiny (DOS) | 8 | 🟢 | C |
| [dishonoredrecompiled](https://github.com/ectrc/dishonoredrecompiled) | Agent-driven decompilation and rebuild of Dishonored (PC) | 7 | 🟢 | C++ |
| [OpenRED](https://github.com/WistfulHopes/OpenRED) | Decompilation and recreation of the Guilty Gear -Strive- battle system (PC) | 7 | 🔴 | C++ |
| [PvZ-Decomp](https://github.com/lvplay2/PvZ-Decomp) | Original Plants vs. Zombies decompilation (PC) | 7 | 🟢 | C |
| [SpaceRangersHD_CPP](https://github.com/pakompom/SpaceRangersHD_CPP) | C++ translation of the Space Rangers HD: A War Apart decompilation (PC) | 7 | 🟢 | C++ |
| [Terraria-1.4.5.8-decomp-recomp](https://github.com/11NU0/Terraria-1.4.5.8-decomp-recomp) | Decompiled and recompilable C# codebase of Terraria 1.4.5.8 (PC) | 7 | 🟢 | C# |
| [Thandor: Die Invasion decomp](https://github.com/idkFoxes/open-thandor) | Decompilation of Thandor: Die Invasion (2000, PC) | 7 | 🟢 | C++ |
| [BattleTech: The Crescent Hawk's Inception decomp](https://github.com/Elthial/Reko-Btech) | Decompilation of BattleTech: The Crescent Hawk's Inception (DOS) | 6 | 🔴 | C++ |
| [Cut the Rope: Experiments decomp](https://github.com/CtRHome/CtRExperiments-WindowsDecomp) | Decompilation and port of Cut the Rope: Experiments (PC) | 6 | 🗄️ | C# |
| [Eden](https://github.com/mercat0r/Eden) | Decompilation project for Project Eden (2001, Core Design) | 6 | 🔴 | C++ |
| [Fallout 2 disassembly](https://github.com/ChrisNonyminus/fallout2) | Disassembly and decompilation of Fallout 2 (PC) | 6 | 🔴 | Assembly |
| [Heroes of Might and Magic I decomp](https://github.com/sushi-shi/homm1-decomp) | Matching decompilation of Heroes of Might and Magic I (PC) | 6 | 🟢 | C++ |
| [Homeworld 2](https://github.com/HaydnTrigg/Homeworld2Classic) | Matching decompilation of Homeworld 2 (PC, 2003) | 6 | 🟢 | C++ |
| [LEGO Batman: The Videogame](https://github.com/wasdhjklxyz/lbtvg) | Matching decompilation of LEGO Batman: The Videogame (PC, 2008) | 6 | 🟢 | C++ |
| [Need decomp](https://github.com/troikoss/speed-re) | Source reconstruction of Need for Speed: Underground 2 (PC) | 6 | 🟢 | Python |
| [Retro-Sonic 3D: Sky Worlds decomp](https://github.com/RSDKModding/RSonic3D-Decompilation) | Decompilation of Retro-Sonic 3D: Sky Worlds (2005, PC) | 6 | 🟢 | C++ |
| [Russian BYOND game Neekothing decomp](https://github.com/CryoSpacewalk/neekothing) | Decompiled source of the Russian BYOND game Neekothing | 6 | 🟢 | DM |
| [Star Wars Episode I: Racer decomp](https://github.com/DeonPoncini/swep1r_decomp) | Decompilation of Star Wars Episode I: Racer (PC) | 6 | 🟡 | C |
| [StarCraft: Brood War 1.16.1 decomp](https://github.com/nicodlz/starcraft-match) | Matching decompilation research for StarCraft: Brood War 1.16.1 (PC) | 6 | 🟢 | C |
| [Supaplex](https://github.com/eigenco/Supaplex) | Disassembly and bug fixes for Supaplex (DOS) | 6 | 🔴 | Assembly |
| [Touhou 10 Mountain of Faith 1.00a decomp](https://github.com/N0zoM1z0/th10) | Source reconstruction of Touhou 10 Mountain of Faith 1.00a (PC) | 6 | 🟢 | Python |
| [Touhou 7 Perfect Cherry Blossom 1.00b decomp](https://github.com/N0zoM1z0/th07) | Source reconstruction of Touhou 7 Perfect Cherry Blossom 1.00b (PC) | 6 | 🟢 | C++ |
| [4X strategy game Stars! decomp](https://github.com/sirgwain/stars-decompile) | Decompilation and recompilation of the 4X strategy game Stars! (PC) | 5 | 🟢 | C |
| [Echo Arena and the RAD15/14 engine decomp](https://github.com/N3rdL0rd/EchoDecomp) | Decompilation of Echo Arena and the RAD15/14 engine (PC VR) | 5 | 🟡 | C |
| [Five Nights at Freddy's: Help Wanted decomp](https://github.com/TechnicalFNaF/HW1Decomp) | Decompilation of Five Nights at Freddy's: Help Wanted (PC) | 5 | 🟢 | C++ |
| [GameDevStory-Decomp](https://github.com/Red-K0/GameDevStory-Decomp) | Decompilation and translation of Kairosoft's original Game Dev Story (1997, Windows) | 5 | 🟡 |  |
| [Ikachan decomp](https://github.com/GabrielRavier/Ikachan-Decompilation) | Decompilation of Ikachan by Studio Pixel (PC) | 5 | 🔴 | Assembly |
| [OregonTrailII](https://github.com/ot-ii/OregonTrailII) | Decompilation of Oregon Trail II | 5 | 🟢 | C |
| [PangYa decomp](https://github.com/hsreina/YaPang) | Decompilation of PangYa (PC) | 5 | 🟢 | C++ |
| [Touhou 9 Phantasmagoria of Flower View 1.50a decomp](https://github.com/N0zoM1z0/th09) | Source reconstruction of Touhou 9 Phantasmagoria of Flower View 1.50a (PC) | 5 | 🟢 | Python |
| [touhou-reverse-engineering](https://github.com/N0zoM1z0/touhou-reverse-engineering) | Reverse engineering notes and runtime experiments for Touhou 8 and Touhou 10 (Windows) | 5 | 🟢 | Python |
| [Vostok engine used decomp](https://github.com/srp-survarium/vostok) | Decompilation of the Vostok engine used by Survarium (PC) | 5 | 🟢 | C++ |
| [Wizardry 8 decomp](https://github.com/agluszak/wizardry-8-decomp) | Source reconstruction of Wizardry 8 (2001) from the Windows binaries | 5 | 🟢 | C++ |
| [Wizardry-6-reverse-engineering](https://github.com/martydill/Wizardry-6-reverse-engineering) | Reverse engineering of Wizardry 6: Bane of the Cosmic Forge | 5 | 🟢 | Python |
| [a Will Rock beta build decomp](https://github.com/player0601/WillRock-Beta-Source-Reconstruction) | Source reconstruction of a Will Rock beta build (PC) | 4 | 🟢 | C++ |
| [Age of Empires II decomp](https://github.com/samuelcaldas/age-of-empires-2-decomp) | Matching decompilation of Age of Empires II (PC and PS2) | 4 | 🟢 | C |
| [Alley Cat disassembly](https://github.com/gmegidish/alleycat-disassembly) | AI-assisted disassembly of Alley Cat (DOS, 1983) | 4 | 🟢 | Assembly |
| [Blasterball Revolution 2](https://github.com/KoboDev/BBR2Decompile) | Decompilation of Blasterball Revolution 2 (PC) | 4 | 🟡 |  |
| [Cave Story options program DoConfig decomp](https://github.com/GabrielRavier/DoConfig-Decompilation) | Recompilable decompilation of the Cave Story options program DoConfig (PC) | 4 | 🔴 | C++ |
| [Grand Prix 4 decomp](https://github.com/leighrobertabbott/decomp-grandprix4) | Verified decompilation of Grand Prix 4 (GP4.exe, 2002, PC) | 4 | 🟢 | C++ |
| [Gruntz decomp](https://github.com/sushi-shi/gruntz-decomp) | Matching decompilation of Gruntz (1999, PC) | 4 | 🟢 | C++ |
| [Guxt v1.0.2.0 decomp](https://github.com/alula/GuxtDecomp) | Decompilation of Guxt v1.0.2.0 by Studio Pixel (PC, 2007) | 4 | 🔴 | C++ |
| [Habbo Origins decomp](https://github.com/Quackster/habbo_origins_src) | Decompiled launch-day client source of Habbo Origins | 4 | 🗄️ | LiveScript |
| [Israeli DOS game Socher Hayam decomp](https://github.com/ashdnazg/socher) | Matching decompilation of the Israeli DOS game Socher Hayam | 4 | 🟢 | Pascal |
| [Karlson decomp](https://github.com/1flxm3/KarlsonDecompiled) | Decompilation of Karlson by Dani (PC) | 4 | 🟢 | C# |
| [Luxor decomp](https://github.com/HW12Dev/LuxorDecomp) | Decompilation of Luxor (PC) | 4 | 🟢 | C++ |
| [Magiczna Kula Papatki](https://github.com/regratka/mkp) | Matching decompilation of Magiczna Kula Papatki (PC) | 4 | 🟢 | C++ |
| [Motocross Madness 2 decomp](https://github.com/andrewboudreau/motocross-madness-2-decomp) | Decompilation of Motocross Madness 2 (PC) | 4 | 🟢 | C++ |
| [New Star Soccer 5 decomp](https://github.com/pr0sc0per9000/nss5-forge) | Source reconstruction of New Star Soccer 5 from its executable (PC) | 4 | 🟢 | BlitzMax |
| [PC release of EDGE decomp](https://github.com/SplaatSites/EDGE) | Decompilation of the PC release of EDGE | 4 | 🟢 |  |
| [Purble Place mini-games decomp](https://github.com/Areshkew/purble-place-decomp) | C++20 reconstruction of the Purble Place mini-games (Windows) | 4 | 🟢 | C++ |
| [Red Faction decomp](https://github.com/GTTeancum/OpenRedFaction) | C reconstruction of Red Faction (2001) for PC and original Xbox | 4 | 🟢 | C |
| [Sonic Generations](https://github.com/Luigi587/GenerationsDecomp) | Matching decompilation of Sonic Generations (PC, 2011) | 4 | 🟢 |  |
| [Speedy Eggbert 2 decomp](https://github.com/HMVocaloid/Speedy-Eggbert-2-Source-Code-Decomp) | Decompilation of Speedy Eggbert 2 (Blupi) (PC) | 4 | 🟡 | C |
| [Stronghold (1993)](https://github.com/NancySadkov/dest) | Matching decompilation of AD&D Stronghold (DOS, 1993) | 4 | 🟡 | C |
| [Supreme Commander: Forged Alliance decomp](https://github.com/Hdt80bro/SupComDecomp) | Decompilation of Supreme Commander: Forged Alliance (PC) | 4 | 🟡 | C++ |
| [The Italian Job](https://github.com/dashr9230/Caper) | Non-matching decompilation of The Italian Job (PC, 2001) | 4 | 🟢 | C |
| [Touhou 12 Undefined Fantastic Object decomp](https://github.com/11NU0/th12-decomp) | Source reconstruction of Touhou 12 Undefined Fantastic Object (th12.exe) | 4 | 🟢 | C |
| [TrackMania Nations Forever decomp](https://github.com/rockenrooster/TMNationsDecomp) | Clean-room reconstruction and Android port of TrackMania Nations Forever | 4 | 🟢 | C++ |
| [TrackMania United Forever physics decomp](https://github.com/Teero888/tmuf_physics) | 1:1 decompilation of the TrackMania United Forever physics (PC) | 4 | 🟢 | C |
| [2009 Portal 2 beta decomp](https://github.com/apersonwhomakesstuff/Portal-2-Beta-Decompilation) | Decompilation of the 2009 Portal 2 beta (PC) | 3 | 🟢 | C++ |
| [2014 Steam release of Sonic Adventure DX decomp](https://github.com/LuckyLuke00/sadx-decomp) | Matching decompilation of the 2014 Steam release of Sonic Adventure DX | 3 | 🟢 | C |
| [A2 Racer decomp](https://github.com/xvilo/a2-racer-davilex-decomp) | Decompilation of A2 Racer by Davilex (PC) | 3 | 🟢 | C |
| [castle-crashers-decomp](https://github.com/genizy/castle-crashers-decomp) | Decompilation attempt of Castle Crashers (PC) | 3 | 🟡 |  |
| [cod4map.exe decomp](https://github.com/prd0nja/cod4map) | Source reconstruction of cod4map.exe from the Call of Duty 4 mod tools | 3 | 🟢 | C++ |
| [Creatures 2](https://github.com/adamcolquhoun/Creatures-2-Decompilation) | Matching decompilation of Creatures 2 (PC, 1998) | 3 | 🟢 |  |
| [Die Gilde / Europa 1400 decomp](https://github.com/maci0/gilde-decomp) | Decompilation of Die Gilde / Europa 1400 (PC) | 3 | 🟡 | C |
| [DOMA Days](https://github.com/iestyn129/DOMADays) | Decompilation of the Ren'Py game DOMA Days by Big Blue Bubble (PC) | 3 | 🟢 | Ren'Py |
| [Fire & Forget II decomp](https://github.com/n0isy/fire-and-forget-2-recomp) | Decompilation and recompilation of Fire & Forget II (DOS, Titus, 1990) | 3 | 🟢 | C |
| [Ford Racing](https://github.com/dashr9230/Gt2) | Non-matching decompilation of Ford Racing (PC, 2000) | 3 | 🟢 | C |
| [Fuzzy's World of Miniature Space Golf decomp](https://github.com/mills32/Fuzzy-s-World-of-Miniature-Space-Golf-Decomp) | Decompilation of Fuzzy's World of Miniature Space Golf (DOS) | 3 | 🟢 | C |
| [Harvest: Massive Encounter](https://github.com/banteg/harvest) | Matching decompilation of Harvest: Massive Encounter (PC, 2008) | 3 | 🟢 | C++ |
| [Heartbound demo decomp](https://github.com/genizy/Heartbound-Source-Code) | Decompilation of the Heartbound demo (PC) | 3 | 🟡 | Game Maker Language |
| [Imperialism decomp](https://github.com/agluszak/imperialism-decomp) | Decompilation of Imperialism (PC) | 3 | 🟢 | C++ |
| [Jazz Jackrabbit 2](https://github.com/Mustafa1177/jazzjackrabbit2-decompiled) | Ghidra decompilation project of Jazz Jackrabbit 2: The Secret Files (PC, 1998) | 3 | 🟡 |  |
| [Jurassic Park: Operation Genesis and the Toshi Engine 1.0 decomp](https://github.com/TekRantGaming/OpenJPOG) | Decompilation of Jurassic Park: Operation Genesis and the Toshi Engine 1.0 (PC) | 3 | 🟢 | C++ |
| [linker_pc.exe decomp](https://github.com/prd0nja/linker_pc) | Source reconstruction of linker_pc.exe from the Call of Duty 4 mod tools | 3 | 🟢 | C |
| [Mad Max decomp](https://github.com/plyd823/MadMax2015) | Decompilation of Mad Max (2015, PC) | 3 | 🟢 | C++ |
| [Mario Teaches Typing 3](https://github.com/EliasFever/MarioTeachesTyping3Decomp) | Decompilation of Mario Teaches Typing 3 | 3 | 🟢 | GDScript |
| [my-teacher-is-an-alien-re](https://github.com/neuromancer/my-teacher-is-an-alien-re) | Reconstruction of My Teacher is an Alien (1997, PC) | 3 | 🟢 | C++ |
| [OpenJPB](https://github.com/GTTeancum/OpenJPB) | Reconstruction of Star Wars Episode I: Jedi Power Battles for PC | 3 | 🟢 | C |
| [PC version of 3DO Road Rash decomp](https://github.com/PlasticCog/RoadRash_Decomp) | Reverse engineering of the PC version of 3DO Road Rash | 3 | 🟢 | Assembly |
| [Rise of Nations decomp](https://github.com/StackAndPointer/Rise-of-Nations-Decomp) | Decompilation of Rise of Nations (PC) | 3 | 🟢 | C++ |
| [Sonic Adventure DX story sequence functions decomp](https://github.com/SPEEPSHighway/sadx-sequence-decompilation) | Decompilation of Sonic Adventure DX story sequence functions (PC) | 3 | 🟢 | C |
| [Sonic the Hedgehog 4: Episode I (Windows Phone)](https://github.com/fr3dsp/Sonic4Ep1-Decomp) | Decompilation of Sonic the Hedgehog 4: Episode I (Windows Phone) | 3 | 🟢 | C# |
| [Star Wars Episode I: Racer binary decomp](https://github.com/everalert/swe1r-decomp) | Reverse engineering of the Star Wars Episode I: Racer binary (PC) | 3 | 🟡 | C |
| [Summoner](https://github.com/AARosson48/SummonerDecomp) | Matching decompilation of Summoner (PC, 2000) | 3 | 🟢 | C++ |
| [The Hobbit decomp](https://github.com/sushi-shi/hobbit-decomp) | C++ reconstruction of The Hobbit (2003, PC v1.3) with binary checks | 3 | 🟢 | C++ |
| [Touhou 10 Mountain of Faith decomp](https://github.com/levzzz5154/th10-decomp) | Decompilation of Touhou 10 Mountain of Faith (PC) | 3 | 🟢 | Assembly |
| [Touhou 3 Phantasmagoria of Dim.Dream decomp](https://github.com/N0zoM1z0/th03) | Source reconstruction of Touhou 3 Phantasmagoria of Dim.Dream (PC-98) | 3 | 🟢 | Python |
| [Touhou 7.5 Immaterial and Missing Power 1.11 decomp](https://github.com/N0zoM1z0/th075) | Source reconstruction of Touhou 7.5 Immaterial and Missing Power 1.11 (PC) | 3 | 🟢 | Python |
| [Webfishing decomp](https://github.com/BlizzardfurMeow/Webfishing-Decompiled) | Decompiled source of Webfishing (PC) | 3 | 🟢 | GDScript |
| [3D Pinball disassembly](https://github.com/Brian151/disassemball3d) | Disassembly of 3D Pinball for Windows | 2 | 🔴 | Assembly |
| [3D Pinball Space Cadet decomp](https://github.com/Randomno/pinball-decomp) | Matching decompilation of 3D Pinball Space Cadet (Windows) | 2 | 🟢 | C++ |
| [Achtung decomp](https://github.com/SimonAlling/zatacka-decomp) | Matching decompilation of Achtung, die Kurve! (ZATACKA.EXE, DOS) | 2 | 🟢 | C++ |
| [Adventure Game Studio 2.x engine decomp](https://github.com/adm244/ags2_decomp) | Matching decompilation of the Adventure Game Studio 2.x engine (PC) | 2 | 🟢 | C |
| [Ascendancy decomp](https://github.com/coco875/ascendancy-decomp) | Decompilation of Ascendancy (DOS) | 2 | 🟡 | Assembly |
| [boss code of Sonic Adventure DX decomp](https://github.com/Sora-yx/SADX-Boss-Decompilation) | Decompilation of the boss code of Sonic Adventure DX (PC) | 2 | 🔴 | C++ |
| [Crazy Cattle 3D decomp](https://github.com/Desyncfy/CrazyCattle3Decomp) | Decompiled source of Crazy Cattle 3D (PC) | 2 | 🟢 | GDScript |
| [DAGGER.EXE decomp](https://github.com/DecompFall/DAGGER) | Decompilation of DAGGER.EXE from The Elder Scrolls II: Daggerfall (DOS) | 2 | 🟡 |  |
| [Europa 1400: The Guild server.dll decomp](https://github.com/maci0/guild-rebrew) | Byte-identical C89 reconstruction of Europa 1400: The Guild server.dll (PC) | 2 | 🟢 | C |
| [Game-Dev-Studio-Source-Code](https://github.com/Aussiemon/Game-Dev-Studio-Source-Code) | Decompiled game scripts of Game Dev Studio (PC) | 2 | 🟡 | Lua |
| [Granny](https://github.com/scd5dev/GrannyDecompilationLegacy) | Decompilation of Granny PC v1.2.2 (PC) | 2 | 🗄️ | C# |
| [Harry Potter and the Half-Blood Prince](https://github.com/MidacoYT/HarryPotterAndTheHalfBloodPrince-Decompilation) | Matching decompilation of Harry Potter and the Half-Blood Prince (PC, 2009) | 2 | 🟢 | C |
| [Hazard](https://github.com/EuclidVsGauss/HazardRevenge) | Matching decompilation of Hazard (PC) | 2 | 🟢 | C++ |
| [HOVER! decomp](https://github.com/Link4Electronics/FlyingDodgem) | Decompilation and native port of HOVER! (Windows) | 2 | 🟢 | C |
| [HyperBlade decomp](https://github.com/zach2good/hyperblade-decomp) | Decompilation of HyperBlade (1996, PC) | 2 | 🟢 | C++ |
| [LineWarsII-DOS](https://github.com/fredangstadt-lang/LineWarsII-DOS) | LineWars II (1994, DOS) reconstructed in C from its shipped binary | 2 | 🟢 | C |
| [London Racer decomp](https://github.com/Davilex-Reverse-Engineering/london-racer-decomp) | Decompilation of London Racer (PC) | 2 | 🟢 | C++ |
| [LyN engine decomp](https://github.com/charlobrown/RGH-PC-LyN-Decomp) | Decompilation of the LyN engine from the PC version of Rabbids Go Home | 2 | 🟢 | C |
| [MechWarrior 2 decomp](https://github.com/anpage/demech2) | Decompilation of MechWarrior 2 (Windows 95, 1996) | 2 | 🟢 | C |
| [NavyField 2000](https://github.com/rbxrootx/MissionFleet) | Matching decompilation of NavyField 2000 (PC) | 2 | 🟢 | C++ |
| [Need decomp](https://github.com/GermanAizek/nfs5-decomp) | Reverse engineering of Need for Speed: Porsche Unleashed (PC) | 2 | 🟢 | Python |
| [Need decomp](https://github.com/Hanz0Hatt0r1/nfs-shift-decompilation) | Decompilation of Need for Speed: Shift (PC) | 2 | 🟢 | Python |
| [Neversoft's Spider-Man decomp](https://github.com/PatrikScully/OpenSpidey) | Decompilation of Neversoft's Spider-Man (PC port) | 2 | 🟢 | C++ |
| [Plants vs. Zombies decomp](https://github.com/person6423/pvz-vanilla-recon) | Clean decompilation and reconstruction of Plants vs. Zombies (PC) | 2 | 🟢 | C |
| [Rage of Mages / Allods decomp](https://github.com/sushi-shi/rom1-decomp) | Matching decompilation of Rage of Mages / Allods (1998, PC) | 2 | 🟢 | Python |
| [Redline decomp](https://github.com/NicksWorld/redline_decomp) | Decompilation of Redline (1999, PC) | 2 | 🟢 | C++ |
| [Rumble Fighter](https://github.com/Primitheus/rumbledecomp) | Decompilation of Rumble Fighter (PC, 2006) | 2 | 🟡 | C++ |
| [Saints Row 2 PC decomp](https://github.com/thegliffy/OpenRow2) | Decompilation of the Saints Row 2 PC (Steam) executable | 2 | 🟢 | C |
| [Sid Meier's SimGolf decomp](https://github.com/SMSG-decomp/SMSG-decomp) | Decompilation of Sid Meier's SimGolf (PC) | 2 | 🟢 | C++ |
| [Smash Up Derby decomp](https://github.com/doyaGu/SmashUpDerby) | Reverse-engineered source code of Smash Up Derby (PC) | 2 | 🔴 | C++ |
| [The Journeyman Project Turbo!](https://github.com/disinvite/jman-decomp) | Matching decompilation of The Journeyman Project Turbo! (PC, 1994) | 2 | 🟢 | C++ |
| [The Oregon Trail (Windows 95)](https://github.com/emoluvjd2/oregontrail-win32-decomp) | Decompilation of The Oregon Trail (Windows 95) | 2 | 🟢 | C++ |
| [Theme Hospital decomp](https://github.com/matteo-pacini/theme-hospital-decomp) | Matching decompilation of Theme Hospital (DOS, 1997) | 2 | 🟢 | C++ |
| [Tony & Friends: New Adventures decomp](https://github.com/foxtacles/tony2) | Decompilation of Tony & Friends: New Adventures (1999, PC) | 2 | 🟢 | C |
| [Touhou 20 Fossilized Wonders 1.00a decomp](https://github.com/N0zoM1z0/th20) | Source reconstruction of Touhou 20 Fossilized Wonders 1.00a (PC) | 2 | 🟢 | C++ |
| [1991 DOS game Fallout decomp](https://github.com/lardratboy/fallout_decomp) | Decompilation of the 1991 DOS game Fallout (Beyond Columns sequel) | 1 | 🟢 | C |
| [2014 Steam release of Sonic Adventure DX decomp](https://github.com/yuriaaaaa/sadx-decomp) | Matching decompilation of the 2014 Steam release of Sonic Adventure DX (PC) | 1 | 🟢 | Python |
| [Aargon Deluxe disassembly](https://github.com/Jenna1337/Aargon) | Disassembly of Aargon Deluxe (PC) | 1 | 🟡 | C |
| [Age of Empires decomp](https://github.com/dcostap/aoe1-decomp) | Decompilation of Age of Empires (PC) | 1 | 🟢 | C++ |
| [Age of Speed 2](https://github.com/Llamaware/age-of-speed2) | Decompilation of the Shockwave racing game Age of Speed 2 (Macromedia Director, PC) | 1 | 🟡 | Python |
| [Alley Cat disassembly](https://github.com/dk8827/alleycat-remastered) | Byte-exact disassembly of Alley Cat (DOS, 1984) with a JavaScript translation | 1 | 🟢 | Assembly |
| [Barkley1_Original (Barkley, Shut Up and Jam: Gaiden)](https://github.com/sanlor/Barkley1_Original) | Decompiled source of Barkley, Shut Up and Jam: Gaiden (PC) | 1 | 🗄️ | Game Maker Language |
| [Battlestations: Pacific decomp](https://github.com/sqz269/battlestations-pacific-decompile) | Reverse engineering and C++ reconstruction of Battlestations: Pacific (PC) | 1 | 🟢 | C++ |
| [Bulánci reimplementation](https://github.com/lofcz/bulanci-decomp) | Matching decompilation of Bulánci (2001, PC) with a Rust reimplementation | 1 | 🟢 | C |
| [Call of Duty: Black Ops III decomp](https://github.com/lizardpeter/black-ops-3-decomp) | Decompilation of Call of Duty: Black Ops III (PC) | 1 | 🟢 | Assembly |
| [Cube World alpha decomp](https://github.com/voximity/cw-decomp) | Decompilation and Rust port of the Cube World alpha (PC) | 1 | 🟢 | Rust |
| [December 1995 build of Prey decomp](https://github.com/DeathEngine2/prey1995-reconstruction) | Source reconstruction of the December 1995 build of Prey (PC) | 1 | 🔴 | C |
| [DOS Pool of Radiance engine in portable C decomp](https://github.com/huntergdavis/poolrad-decomp) | Source reconstruction of the DOS Pool of Radiance engine in portable C | 1 | 🟢 | Python |
| [DOS version of Karateka decomp](https://github.com/ergonomy-joe/karateka-decompiled) | Buildable decompiled source of the DOS version of Karateka | 1 | 🟡 | Assembly |
| [Dr. Brain Action Reaction](https://github.com/SirHenricus/DrBrainActionReaction_PackageDecomp) | Decompiled assets and UnrealScript from Dr. Brain Action Reaction (PC, 1999) | 1 | 🟡 | UnrealScript |
| [Farming Simulator 15 and GIANTS Engine 6 decomp](https://github.com/nat649/fs15-reconstruction) | Decompilation and reconstruction of Farming Simulator 15 and GIANTS Engine 6 (PC) | 1 | 🟢 | C++ |
| [Heroes of Might and Magic III map editor decomp](https://github.com/crackedmind/h3maped-decomp) | Decompilation of the Heroes of Might and Magic III map editor | 1 | 🟢 | C++ |
| [Hot Wheels: Velocity X decomp](https://github.com/Alaxend0l/HWVX-PC-Decomp) | Decompilation of Hot Wheels: Velocity X (PC) | 1 | 🟢 | C++ |
| [Jurassic Park: Operation Genesis reimplementation](https://github.com/Voikanaa/jpog-decomp) | Decompilation and native reimplementation of Jurassic Park: Operation Genesis (2003, PC) | 1 | 🟢 | C++ |
| [Legend of Grimrock Linux engine decomp](https://github.com/morgothaufheroin88/LibreGrimrock) | 64-bit source reconstruction of the Legend of Grimrock Linux engine | 1 | 🟢 | C++ |
| [LEGOLAND decomp](https://github.com/adamXbot/brickpark-decomp) | Matching decompilation of LEGOLAND (Windows, 2000) | 1 | 🟢 | C |
| [MechWarrior 4: Mercenaries decomp](https://github.com/mech4decomp/Mech4MercDecomp) | Byte-identical recompilation of MechWarrior 4: Mercenaries (PC) | 1 | 🟢 | C |
| [Metal Gear Rising: Revengeance decomp](https://github.com/ZooLSmith/mgrr-decomp) | Decompilation of Metal Gear Rising: Revengeance (PC) | 1 | 🟢 | C++ |
| [On The Run 2](https://github.com/caramelcupcakes842/On-The-Run-2-Decomp) | Decompilation of Miniclip's On The Run 2 (Adobe Shockwave, PC) | 1 | 🟡 |  |
| [On The Run: The Getaway](https://github.com/caramelcupcakes842/On-The-Run-The-Getaway) | Decompilation of Miniclip's On The Run: The Getaway (Adobe Shockwave, PC) | 1 | 🟡 |  |
| [Portal 2 decomp](https://github.com/ipfsd-acc/p2-decomp) | Reverse engineering of Portal 2 (PC) | 1 | 🟢 | C++ |
| [Red Alert 2: Yuri's Revenge gamemd.exe 1.001 decomp](https://github.com/gibbo101/ra2-decomp) | Matching decompilation of Red Alert 2: Yuri's Revenge gamemd.exe 1.001 (PC) | 1 | 🟢 | C++ |
| [Rome: Total War decomp](https://github.com/YunataSavior/RTWDecomp) | Decompilation of Rome: Total War (PC) | 1 | 🟢 | C++ |
| [Shaiya Episode 1 binaries decomp](https://github.com/Spelunkern/shaiya-ep1-reconstruction) | Community source reconstruction of the Shaiya Episode 1 binaries (PC) | 1 | 🟢 | Python |
| [Touhou 11 Subterranean Animism 1.00a decomp](https://github.com/AgentMystia/th11) | Source reconstruction of Touhou 11 Subterranean Animism 1.00a (PC) | 1 | 🟢 | C++ |
| [TwinBee Paradise in Donburi Shima](https://github.com/Jhuyghue/donburi-recomp) | Decompilation of TwinBee Paradise in Donburi Shima (Windows 95) | 1 | 🟢 |  |
| [Vermintide-VR-Source-Code](https://github.com/Aussiemon/Vermintide-VR-Source-Code) | Decompiled scripts of Warhammer: Vermintide VR - Hero Trials (PC) | 1 | 🟡 | Lua |
| [WotR-Source-Code](https://github.com/Aussiemon/WotR-Source-Code) | Decompiled scripts of the defunct War of the Roses (PC) | 1 | 🟡 | Lua |
| [Zeliard decomp](https://github.com/awkto/zeliard-decomp) | Reverse engineering of Zeliard (DOS, 1990) | 1 | 🟢 | C |
| [4D Sports Boxing decomp](https://github.com/ToolAssisted-run/Open4DBoxing) | Source reconstruction of 4D Sports Boxing (DOS, 1991) | 0 | 🟢 | C |
| [AldoReconstruction](https://github.com/RaceTheMaSe/AldoReconstruction) | Reconstruction of the DOS games Aldo's Adventure and Aldo Again | 0 | 🟢 | C |
| [amrts-decomp](https://github.com/andresj-sanchez/amrts-decomp) | Decompilation project of Army Men RTS | 0 | 🟢 | Python |
| [Battle Engine Aquila decomp](https://github.com/dlprentice/onslaught-decomp) | Byte-matching decompilation of Battle Engine Aquila (2003, PC) | 0 | 🟢 | C++ |
| [BBS door game Legend of the Red Dragon decomp](https://github.com/aardvarkk/lordsrc) | Source reconstruction of the BBS door game Legend of the Red Dragon | 0 | 🟢 | Pascal |
| [blackhack](https://gitlab.com/bwrsandman/blackhack) | Launcher for and decompilation of Black & White's runblack.exe |  | ⚪ |  |
| [Brawlhalla v0.2.1 alpha decomp](https://github.com/HiroStuff/bhair-alpha) | Decompilation of Brawlhalla v0.2.1 alpha (PC) | 0 | 🟢 | ActionScript |
| [Curse of the Azure Bonds v1.3 decomp](https://github.com/retro-ware/cotab-re) | Byte-perfect Turbo Pascal source reconstruction of Curse of the Azure Bonds v1.3 (DOS) | 0 | 🟢 | C |
| [DeusEx.dll decomp](https://github.com/LoadLineCalibration/DeusEx) | Reconstructed source of DeusEx.dll from Deus Ex (PC) | 0 | 🟢 | C++ |
| [Elevator_Action (Elevator Action)](https://github.com/Evenball-8bit/Elevator_Action) | Decompilation/disassembly of Elevator Action (Arcade) | 0 | 🔴 | Assembly |
| [endless-online-archive](https://github.com/ExileStudios/endless-online-archive) | Byte-exact source reconstructions of Endless Online client, server and tools | 0 | 🟢 | C++ |
| [Final Fantasy XIV 1.23b decomp](https://github.com/Drahsid/ffxiv_1_23b_decomp) | Byte-matching decompilation of Final Fantasy XIV 1.23b (PC) | 0 | 🟢 | C++ |
| [game Total Miner decomp](https://github.com/Fhoughton/OpenMiner) | Decompilation of the game Total Miner (PC) | 0 | 🔴 | C# |
| [Giten Megami Tensei decomp](https://github.com/sushi-shi/giten-decomp) | Matching decompilation of Giten Megami Tensei (PC-98) | 0 | 🟢 | Python |
| [Guilty Gear XX Accent Core Plus R disassembly](https://github.com/WistfulHopes/GGXXACPR_Win_Disasm) | Disassembly of Guilty Gear XX Accent Core Plus R (Windows) | 0 | 🟡 |  |
| [Hard Truck 2: King of the Road decomp](https://github.com/KudryavtsevDmitry/ht2-rev) | Source reconstruction and reverse engineering of Hard Truck 2: King of the Road (PC) | 0 | 🟢 | C++ |
| [In Search of Dr. Riptide decomp](https://github.com/xor2003/riptide-re) | Reconstructed source of In Search of Dr. Riptide (DOS) | 0 | 🟢 | Assembly |
| [LEGIE decomp](https://github.com/lofcz/legie_decomp) | Decompilation of LEGIE (2009, PC) | 0 | 🟢 | Pascal |
| [legord](https://codeberg.org/kant2002/legord) | Decompilation efforts for the BBS door game Legend of the Red Dragon |  | ⚪ |  |
| [Microsoft InkBall decomp](https://github.com/arceuss/InkBall) | Reverse-engineered reconstruction of Microsoft InkBall from Windows Vista | 0 | 🟢 | C++ |
| [Might and Magic III decomp](https://github.com/retro-ware/mm3-decomp) | Byte-exact C/ASM decompilation of Might and Magic III (DOS, 1991) | 0 | 🟢 | C |
| [MMath.exe decomp](https://github.com/Quackster/MMath_decompile) | Decompiled source code of MMath.exe, a mid-1990s Windows game | 0 | 🟢 | C |
| [MS-DOS shareware game Pacwars decomp](https://github.com/yuv422/pacwars_decomp) | Decompilation of the MS-DOS shareware game Pacwars | 0 | 🟢 | C |
| [Nancy Drew: Curse of Blackmoor Manor decomp](https://github.com/albovsky/nd-blackmoor-decomp) | Source reconstruction of Nancy Drew: Curse of Blackmoor Manor (PC) | 0 | 🟢 | Assembly |
| [On The Run Vegas](https://github.com/caramelcupcakes842/On-The-Run-Vegas-Decomp) | Decompilation of Miniclip's On The Run Vegas (Adobe Shockwave, PC) | 0 | 🟡 |  |
| [openmtv](https://github.com/openmtv/openmtv) | Mad TV (Rainbow Arts, 1991, DOS) decompiled to C, native on Windows, macOS and Linux | 0 | 🟢 | C |
| [por-re](https://github.com/retro-ware/por-re) | Disassembly and overlay map of Pool of Radiance (DOS) | 0 | 🟢 | Assembly |
| [Prince of Persia 2 decomp](https://github.com/ToolAssisted-run/SDLPoP2) | Source reconstruction of Prince of Persia 2 (DOS 1.0) | 0 | 🟢 | C |
| [Robin Hood: The Legend of Sherwood decomp](https://github.com/sergio-asenjo/Greenwood) | Matching decompilation of Robin Hood: The Legend of Sherwood (PC) | 0 | 🟢 | C++ |
| [SCP - Containment Breach Remastered decomp](https://github.com/juanjp600/SCPCB-Remastered-decompiled) | Decompiled source of SCP - Containment Breach Remastered (PC) | 0 | 🟡 | BlitzBasic |
| [SCP - Containment Breach v0.2 to v0.6.4 decomp](https://github.com/juanjp600/SCPCB-decompiled) | Decompiled source of SCP - Containment Breach v0.2 to v0.6.4 (PC) | 0 | 🟡 |  |
| [SimCopter decomp](https://github.com/phire/simcopter_auto_decomp) | Automated decompilation of SimCopter (PC) | 0 | 🟢 | C++ |
| [Sonic & Knuckles Collection (1997)](https://git.sr.ht/~benoitren/skccport) | Matching decompilation of Sonic & Knuckles Collection (PC, 1997) |  | ⚪ |  |
| [Sonic CD (PC / Gems Collection)](https://git.sr.ht/~benoitren/soniccddecompilation) | Decompilation of Sonic CD (PC / Gems Collection) |  | ⚪ |  |
| [ssgdecomp](https://codeberg.org/shuppy/ssgdecomp) | Decompilation of Super Solvers: Gizmos & Gadgets! (DOS) |  | ⚪ |  |
| [Star Wars: Republic Commando decomp](https://github.com/iannett/deltasquad) | Non-matching decompilation of Star Wars: Republic Commando (PC) | 0 | 🟢 | C++ |
| [Steam release of Gazillionaire decomp](https://github.com/calibancode/gazillionaire) | Decompilation of the Steam release of Gazillionaire (PC) | 0 | 🟢 | Python |
| [Sword of the Samurai decomp](https://github.com/ToolAssisted-run/OpenSamurai) | Source reconstruction of Sword of the Samurai (MicroProse, DOS, 1989) | 0 | 🟢 | C |
| [Syndicate decomp](https://github.com/WildPress/vibesynd) | Byte-exact matching decompilation of Syndicate (DOS, Bullfrog, 1995) | 0 | 🟢 | C |
| [The Bard's Tale decomp](https://github.com/retro-ware/bt1-re) | Matching decompilation of The Bard's Tale (DOS) | 0 | 🟢 | Assembly |
| [The Elder Scrolls II: Daggerfall FALL.EXE 1.07.213 decomp](https://github.com/brotchie/daggerfall-decomp) | Matching decompilation of The Elder Scrolls II: Daggerfall FALL.EXE 1.07.213 (DOS) | 0 | 🟢 | C |
| [The-Right-Mix-Decomp](https://github.com/Clank700/The-Right-Mix-Decomp) | Bytecode-matching decompilation and native ports of the Flash game The Right Mix | 0 | 🟢 | C |
| [Titanic: Adventure Out of Time decomp](https://github.com/operationostrich/DeTAOOT) | Decompilation of Titanic: Adventure Out of Time (1996, PC) | 0 | 🟢 | C |
| [Total Annihilation decomp](https://github.com/ozgb/byte-tactics) | Matching decompilation of Total Annihilation (PC) | 0 | 🟢 | C++ |
| [Touhou 16 Hidden Star in Four Seasons v1.00a decomp](https://github.com/johnthreekay/th16) | Matching decompilation of Touhou 16 Hidden Star in Four Seasons v1.00a (PC) | 0 | 🟢 | C++ |
| [Uprising: Join or Die decomp](https://github.com/pdromnt/uprising_decomp) | Reverse engineering and decompilation of Uprising: Join or Die (PC) | 0 | 🟢 | C |
| [Vermintide-2-Versus-Source-Code](https://github.com/Aussiemon/Vermintide-2-Versus-Source-Code) | Decompiled scripts of Warhammer: Vermintide 2 - Versus (PC) | 0 | 🟡 | Lua |
| [Wings decomp](https://github.com/Wyrelade/OpenWINGS) | Behavioural decompilation of Wings (1996, DOS) | 0 | 🟢 | Python |
| [Wobbledogs decomp](https://github.com/calibancode/wobbledogs) | Decompilation of Wobbledogs by Tom Astle (PC) | 0 | 🟢 | Python |

## Matching Decompilations — PSP / Vita / PS3

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Monster Hunter Portable 2nd G](https://github.com/tclamb/mhp2g-decomp) | Matching decompilation of Monster Hunter Portable 2nd G (PSP, 2008) | 36 | 🟢 | C++ |
| [Folklore decomp](https://github.com/Mava-b/folklore-decomp) | AI-assisted decompilation of Folklore (PS3) | 33 | 🟢 | C |
| [Bakugan: Defenders of the Core](https://github.com/Vawlpe/BakuganDotC-decomp) | Decompilation of Bakugan: Defenders of the Core (PSP, 2010) | 10 | 🟡 | C |
| [Yu-Gi-Oh! 5D's Tag Force 5 decomp](https://github.com/angelof-exe/ygo-tf-5-decomp) | Decompilation of Yu-Gi-Oh! 5D's Tag Force 5 (PSP, ULES-01474) | 7 | 🟢 | C |
| [Pursuit Force decomp](https://github.com/itasimo/Pursuit-Force-Decomp) | Decompilation of Pursuit Force (PSP) | 5 | 🔴 |  |
| [Decompilation-Project](https://github.com/BRS-PSP-Research-Initiative/Decompilation-Project) | Ghidra-aided decompiled code of Black Rock Shooter: The Game (PSP) | 4 | 🟢 | C |
| [Dissidia 012 Duodecim Final Fantasy decomp](https://github.com/RocherBrockas/DissidiaDecompProject) | Decompilation of Dissidia 012 Duodecim Final Fantasy (PSP) | 4 | 🟢 | C++ |
| [Ratchet & Clank Future: Tools of Destruction decomp](https://github.com/llesieur99/rac6-totd-decomp) | Matching decompilation of Ratchet & Clank Future: Tools of Destruction (PS3) | 2 | 🟢 | Python |
| [Ratchet & Clank: Secret Agent Clank decomp](https://github.com/OpenRAC/rac-sac-decomp) | Matching decompilation of Ratchet & Clank: Secret Agent Clank (PSP) | 2 | 🟢 | C |
| [Yu-Gi-Oh! Tag Force decomp](https://github.com/thiago-cipitelli/tagforce-decomp) | Decompilation of Yu-Gi-Oh! Tag Force (PSP) | 2 | 🟢 | C |
| [Bakugan Battle Brawlers: Defenders of the Core decomp](https://github.com/JeSaisPaz/BakuganDotC-src) | Readable C decompilation of Bakugan Battle Brawlers: Defenders of the Core (PSP) | 1 | 🟢 | C |
| [Daxter decomp](https://github.com/llesieur99/daxter-psp-decomp) | Matching decompilation of Daxter (PSP, 2006) | 1 | 🟢 | Python |
| [Hot Shots Tennis: Get a Grip decomp](https://github.com/Jstar269/hst-decomp) | Matching decompilation of Hot Shots Tennis: Get a Grip (PSP) | 0 | 🟢 | C |
| [rac-collection-decomp](https://github.com/llesieur99/rac-collection-decomp) | Matching decompilation workspace for the Ratchet & Clank Collection (PS3) | 0 | 🟢 | Python |
| [Ridge Racer decomp](https://github.com/jeff-strutb/ridgeracerpsp) | Byte-exact decompilation of Ridge Racer (PSP) | 0 | 🟢 | C++ |

## Matching Decompilations — PlayStation 1

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Castlevania: Symphony of the Night](https://github.com/Xeeynamo/sotn-decomp) | Matching decompilation of Castlevania: Symphony of the Night (PlayStation, 1997) | 1,175 | 🟢 | C |
| [Silent Hill](https://github.com/shdecompilations/silent-hill-decomp) | Matching decompilation of Silent Hill (PlayStation, 1999) | 958 | 🟢 | C |
| [Metal Gear Solid](https://github.com/FoxdieTeam/mgs_reversing) | Reimplementation of Metal Gear Solid (PlayStation, 1998) | 822 | 🟢 | C |
| [Crash Team Racing (CTR-ModSDK)](https://github.com/CTR-tools/CTR-ModSDK) | Mod SDK and decompilation of Crash Team Racing (PlayStation, 1999) | 455 | 🟢 | C |
| [Vagrant Story](https://github.com/ser-pounce/rood-reverse) | Matching decompilation of Vagrant Story (PlayStation, 2000) | 186 | 🟢 | C |
| [Spyro the Dragon](https://github.com/TheMobyCollective/spyro-1) | Matching decompilation of Spyro the Dragon (PlayStation, 1998) | 179 | 🟢 | C |
| [Final Fantasy VII](https://github.com/Xeeynamo/ff7-decomp) | Matching decompilation of Final Fantasy VII (PlayStation, 1997) | 178 | 🟢 | C |
| [PSX Doom (PSXDOOM-RE)](https://github.com/Erick194/PSXDOOM-RE) | Decompilation of PSX Doom (PSXDOOM-RE) | 163 | 🟡 | C |
| [Serial Experiments Lain](https://github.com/Y0oshi/lain-psx-decompiled) | Decompilation of Serial Experiments Lain | 134 | 🟢 | C |
| [Xenogears](https://github.com/ladysilverberg/xenogears-decomp) | Matching decompilation of Xenogears (PlayStation, 1998) | 126 | 🗄️ | C |
| [Crash Bandicoot 2: Cortex Strikes Back](https://github.com/ughman/c2c) | Matching decompilation of Crash Bandicoot 2: Cortex Strikes Back (PlayStation, 1997) | 94 | 🔴 | C |
| [Digimon World](https://github.com/jype0/dw_decomp) | Matching decompilation of Digimon World (PlayStation, 1999) | 86 | 🟢 | C |
| [mml1](https://github.com/ChrisNonyminus/mml1) | Decompilation of Mega Man Legends for PlayStation | 86 | 🔴 | C |
| [Legacy of Kain: Soul Reaver](https://github.com/fmil95/soul-re) | Matching decompilation of Legacy of Kain: Soul Reaver (PlayStation, 1999) | 85 | 🟢 | C |
| [Brave Fencer Musashi](https://github.com/Druthulu/BFM-decomp) | Matching decompilation of Brave Fencer Musashi (PlayStation, 1998) | 83 | 🟢 | C |
| [Chrono Cross](https://github.com/jdperos/chrono-cross-decomp) | Matching decompilation of Chrono Cross (PlayStation, 1999) | 81 | 🟢 | C |
| [Parasite Eve II](https://github.com/GabeRealB/parasite-eve-2-decomp) | Matching decompilation of Parasite Eve II (PlayStation, 1999) | 74 | 🟢 | C |
| [MediEvil](https://github.com/MediEvilDecompilation/medievil-decomp) | Matching decompilation of MediEvil (PlayStation, 1998) | 73 | 🟢 | C |
| [Parasite Eve](https://github.com/khasinski/parasite-eve-decomp) | Matching decompilation of Parasite Eve (PlayStation, 1998) | 69 | 🟢 | C |
| [Final Fantasy VIII](https://github.com/roengstrom/ff8-decomp) | Matching decompilation of Final Fantasy VIII (PlayStation, 1999) | 60 | 🟢 | C |
| [Frogger (1997)](https://github.com/HighwayFrogs/frogger-psx) | Decompilation of Frogger (1997) | 60 | 🟡 | C |
| [NFSHSX](https://github.com/OpenNFS/NFSHSX) | Need for Speed: High Stakes (PS1) disassembly translated to C source | 58 | 🔴 | C++ |
| [Need for Speed: High Stakes](https://github.com/Caesar0007/NFSHS-PSX-decomp) | Decompilation of Need for Speed: High Stakes | 56 | 🟢 | Assembly |
| [Harvest Moon: Back to Nature decomp](https://github.com/coalslav/hmbtn-decomp) | Decompilation of Harvest Moon: Back to Nature (PS1) | 48 | 🟢 | C |
| [Legend of Mana](https://github.com/celophi/lom-decomp) | Matching decompilation of Legend of Mana (PlayStation, 1999) | 45 | 🟢 | C |
| [Digimon World 3 (ddw3)](https://github.com/markisha64/ddw3) | Matching decompilation of Digimon World 3 (PlayStation, 2002) | 44 | 🟢 | Assembly |
| [rr-decomp](https://github.com/kazuyette/rr-decomp) | Matching decompilation of Ridge Racer (PlayStation, Namco, 1994, SLPS-00001), and a static recompilation that boots a... | 44 | 🟢 | C |
| [ffvii](https://github.com/Drahsid/ffvii) | In-progress matching decompilation of Final Fantasy VII (PSX) | 43 | 🗄️ | C |
| [Gran Turismo 2 decomp](https://github.com/ginryuoku/gt2-reversing) | Reverse engineering of Gran Turismo 2 (PS1) | 42 | 🟡 | C |
| [PlayStation Final Doom decomp](https://github.com/Erick194/PSXFINALDOOM-RE) | Reverse engineering of PlayStation Final Doom by GEC | 41 | 🟡 | C |
| [Croc: Legend of the Gobbos](https://github.com/Xeeynamo/croc) | Matching decompilation of Croc: Legend of the Gobbos (PlayStation, 1997) | 39 | 🟡 | C |
| [Mega Man X4](https://github.com/sozud/mmx4) | Matching decompilation of Mega Man X4 (PlayStation, 1997) | 36 | 🟢 | C |
| [PaRappaSource](https://github.com/cuckydev/PaRappaSource) | PaRappa the Rapper decompilation | 34 | 🔴 | C |
| [Brightis-fan-translation](https://github.com/Dickdebonair/Brightis-fan-translation) | Decompilation and fan translation of the PSX game Brightis | 33 | 🟢 | Assembly |
| [Rage Racer](https://github.com/khasinski/rage-racer-decomp) | Matching decompilation of Rage Racer (PlayStation, 1996) | 33 | 🟢 | C |
| [Vandal Hearts](https://github.com/shao113/vh) | Matching decompilation of Vandal Hearts (PlayStation, 1996) | 31 | 🟡 | C |
| [Final Fantasy VII decomp](https://github.com/ergonomy-joe/ff7-worldmap) | Decompiled world map engine of Final Fantasy VII (PS1) | 30 | 🟡 | C++ |
| [PS1 Psy-Q SDK Libraries](https://github.com/sozud/psy-q-decomp) | Decompilation of PS1 Psy-Q SDK Libraries | 29 | 🟢 | C |
| [q-gears_reverse](https://github.com/Akari1982/q-gears_reverse) | Reverse-engineered code and data of Final Fantasy VII and Xenogears (PS1) | 28 | 🟢 | Assembly |
| [Tomba!](https://github.com/hansbonini/psx_tomba) | Decompilation of Tomba! | 28 | 🟢 | C |
| [Twisted Metal](https://github.com/OpenTrac/tm1_Re-Arc) | Matching decompilation of Twisted Metal (PlayStation, 1995) | 27 | 🟢 | C |
| [fft_decomp](https://github.com/adamrt/fft_decomp) | Decompilation of Final Fantasy Tactics (PlayStation, NA) | 26 | 🟢 | C |
| [spyro-3](https://github.com/TheMobyCollective/spyro-3) | Spyro: Year of the Dragon decompilation project | 26 | 🟢 | Assembly |
| [dw2003recomp](https://github.com/gascarcella/dw2003recomp) | Decompilation of Digimon World 2003 (PS1, EU) with reference tests; PC port in progress | 23 | 🟢 | C |
| [Jumping Flash!](https://github.com/NotExactlySiev/aloha) | Matching decompilation of Jumping Flash! (PlayStation, 1995) | 23 | 🟢 | Assembly |
| [Crash Bash decomp](https://github.com/mateusfavarin/crashbash) | Reverse engineering of Crash Bash (PS1) | 22 | 🟡 | C |
| [LSD: Dream Emulator](https://github.com/brian-oblivion/lsddecomp) | Matching decompilation of LSD: Dream Emulator (PlayStation, 1998) | 19 | 🟢 | C |
| [Rayman decomp](https://github.com/fuerchter/rayman-ps1-decomp) | Decompilation of Rayman (PS1) | 19 | 🟢 | C |
| [Resident Evil 2 Dual Shock Ver. disassembly](https://github.com/MeganGrass/bio2-ds) | Disassembly and decompilation of Resident Evil 2 Dual Shock Ver. (PS1) | 19 | 🟢 | C |
| [Digimon World 2](https://github.com/Wyrelade/Digimon-World-2-Decomp) | Matching decompilation of Digimon World 2 (PlayStation, 2000) | 16 | 🟢 | C |
| [Digimon World 3 (2003)](https://github.com/ReGame-Labs/dw3_decomp) | Matching decompilation of Digimon World 3 (PlayStation, 2002) | 16 | 🟢 | C |
| [LSD: Dream Emulator (FirecatFG)](https://github.com/FirecatFG/lsddecomp) | Matching decompilation of LSD: Dream Emulator (PlayStation, 1998) | 15 | 🟡 | C |
| [Lunar 2: Eternal Blue Complete](https://github.com/Zackmon/lunar2-psx-decomp) | Decompilation of Lunar 2: Eternal Blue Complete | 15 | 🔴 | C |
| [anothermind-decomp](https://github.com/halkuncode/anothermind-decomp) | Source code recovery of Squaresoft's visual novel Another Mind (PS1) | 14 | 🟢 | C |
| [Evo's Space Adventures](https://github.com/mkst/esa) | Matching decompilation of Evo's Space Adventures (PlayStation, 1999) | 14 | 🟢 | C |
| [Megami Ibunroku Persona](https://github.com/daanhenke/persona-psx) | Decompilation of Megami Ibunroku Persona | 14 | 🟢 | C |
| [Shin Megami Tensei decomp](https://github.com/TheCommandoChicken/smt-decomp) | Decompilation of Shin Megami Tensei (PS1) | 14 | 🗄️ | C |
| [ff7-coaster](https://github.com/ergonomy-joe/ff7-coaster) | Decompiled code of the Final Fantasy VII Jet Coaster minigame (PS1) | 12 | 🟡 | C++ |
| [Spyro the Dragon decomp](https://github.com/C0mposer/spyro1-reverse-engineering) | Reverse engineering of Spyro the Dragon (PS1) | 12 | 🟡 | C |
| [Yu-Gi-Oh! Forbidden Memories decomp](https://github.com/krystalgamer/memories-decomp) | Decompilation of Yu-Gi-Oh! Forbidden Memories (PS1) | 12 | 🟢 | C |
| [Digimon World (solidheron)](https://github.com/solidheron/Digimon_World_1_decompolation) | Matching decompilation of Digimon World (PlayStation, 1999) | 11 | 🟡 | C |
| [Legacy of Kain: Soul Reaver disassembly](https://github.com/MicroTransactionsMatterToo/Kain-Disassembly) | Disassembly of Legacy of Kain: Soul Reaver (PS1) | 11 | 🔴 | C |
| [Xenogears decomp](https://github.com/Blizz127/xenogears-decomp-port) | Decompilation and port of Xenogears (PS1) | 11 | 🟢 | C |
| [Spyro 2: Ripto's Rage decomp](https://github.com/TheMobyCollective/spyro-2) | Decompilation of Spyro 2: Ripto's Rage (PS1) | 10 | 🟢 | Assembly |
| [Alien Trilogy decomp](https://github.com/lemiur/alien-trilogy-decomp) | Matching decompilation of Alien Trilogy (PS1, SLUS-00007) | 8 | 🟢 | C |
| [Armored Core](https://github.com/Wyrelade/Armored-Core-Decomp) | Matching decompilation of Armored Core (PlayStation, 1997) | 8 | 🟢 | C |
| [Azure Dreams](https://github.com/forestbelton/azure) | Matching decompilation of Azure Dreams (PlayStation, 1997) | 8 | 🟢 | C |
| [Brave Fencer Musashi decomp](https://github.com/Blizz127/Brave-Fencer-Musashi-decomp-port) | Decompilation and port of Brave Fencer Musashi (PS1) | 8 | 🟢 | C |
| [Harvest Moon: Back to Nature decomp](https://github.com/beruanglaut-com/backtonature-decompiled) | Decompiled source of Harvest Moon: Back to Nature (PS1, SLUS-01115) | 8 | 🟢 | C |
| [LSD: Dream Emulator decomp](https://github.com/cawfee/lsd_decompiled) | Decompilation of LSD: Dream Emulator (PlayStation) | 8 | 🟢 | C |
| [Parasite Eve decomp](https://github.com/Blizz127/parasite-eve-decomp-port) | Decompilation and Linux/Windows port of Parasite Eve (PS1) | 8 | 🟢 | C |
| [Pop'n Music](https://github.com/Erizur/slpm86183) | Matching decompilation of Pop'n Music (PlayStation, 1999) | 8 | 🟢 | C |
| [Resident Evil: Director's Cut Dual Shock Ver. decomp](https://github.com/ThePerfectVale/Resident-Evil-Directors-Cut-Dualshock-Decompilation) | Decompilation of Resident Evil: Director's Cut Dual Shock Ver. (PS1) | 8 | 🟢 | C |
| [WCW/nWo Thunder](https://github.com/martinbean/thunder) | Matching decompilation of WCW/nWo Thunder (PlayStation, 1999) | 8 | 🟡 | Makefile |
| [Ace Combat 3: Electrosphere decomp](https://github.com/vzepec/ac3-decomp) | Reverse engineering and decompilation of Ace Combat 3: Electrosphere (PS1) | 7 | 🟢 | C |
| [Kula World decomp](https://github.com/dezgeg/kula-world-decomp) | Decompilation of Kula World (PS1) | 7 | 🟢 | C |
| [Spyro the Dragon decomp](https://github.com/theMagicalKarp/open-spyro) | Decompilation of Spyro the Dragon (PS1, NTSC SCUS-94228) | 7 | 🟢 | Assembly |
| [Team Buddies decomp](https://github.com/hcbt/tbuddies-decomp) | Matching decompilation of Team Buddies (PS1, SLUS-00869) | 7 | 🟢 | Assembly |
| [Tony Hawk's Pro Skater 2 (Competition Demo)](https://github.com/emoluvjd2/thps2-demo-decomp) | Matching decompilation of Tony Hawk's Pro Skater 2 (PlayStation, 2000; competition demo) | 7 | 🟢 | C++ |
| [Aironauts](https://github.com/bismurphy/Aironauts-decomp) | Matching decompilation of Aironauts (PlayStation, 1999) | 6 | 🟡 | C |
| [Breath of Fire III decomp](https://github.com/loopyd/bof3-decompilation) | Reverse engineering and decompilation of Breath of Fire III (PS1) | 6 | 🟢 | Python |
| [Final Fantasy Tactics decomp](https://github.com/FFT-RE/FFT-1997-Decomp) | Decompilation of Final Fantasy Tactics (PS1, SCUS-94221) | 6 | 🟢 | C |
| [KAIN2](https://github.com/0-vortex/KAIN2) | Legacy of Kain: Soul Reaver alpha disassembly translated to C (PS1) | 6 | 🗄️ | C |
| [BattleTanx: Global Assault decomp](https://github.com/TheGh0stShip/BattleTanx-Global-Assault-PS1) | Matching decompilation of BattleTanx: Global Assault (PS1) | 5 | 🟢 | C |
| [Digimon Rumble Arena](https://github.com/ReGame-Labs/dtbe_decomp) | Matching decompilation of Digimon Rumble Arena (PlayStation, 2001) | 5 | 🟢 | C |
| [Digimon: Digital Card Battle](https://github.com/ReGame-Labs/dcb_decomp) | Matching decompilation of Digimon: Digital Card Battle (PlayStation, 2000) | 5 | 🟢 | C |
| [SHDecompilation](https://github.com/nikita600/SHDecompilation) | Decompilation attempt of Silent Hill (PS1) | 5 | 🔴 | C# |
| [Wild 9](https://github.com/plinkr/Wild9-Decompilation) | Matching decompilation of Wild 9 (PlayStation, 1998) | 5 | 🟢 | C |
| [Bushido Blade decomp](https://github.com/tgg12321/BushidoBladeDecompile) | Decompilation of Bushido Blade (PS1) | 4 | 🟢 | Assembly |
| [Final Fantasy IX decomp](https://github.com/maurizi/ff9-decomp) | Matching decompilation of Final Fantasy IX (PS1, NTSC-U) | 4 | 🟢 | C |
| [Tenchu: Stealth Assassins decomp](https://github.com/Fuuzetsu/tenchu-decomp) | Decompilation of Tenchu: Stealth Assassins (PS1) | 4 | 🟢 | C |
| [Tokimeki Memorial: Forever with You](https://github.com/CosmicScribe64/tokimemo-ps1-decomp) | Decompilation of Tokimeki Memorial: Forever with You | 4 | 🟢 | C |
| [WCW Nitro](https://github.com/martinbean/nitro) | Matching decompilation of WCW Nitro (PlayStation, 1998) | 4 | 🟢 | C |
| [Yu-Gi-Oh! Forbidden Memories decomp](https://github.com/gonzaloberteri/ygofm-decomp) | Matching decompilation of Yu-Gi-Oh! Forbidden Memories (PS1, SLUS-01411) | 4 | 🟢 | Python |
| [Azure Dreams decomp](https://github.com/thingstuffs/azure-dreams-decomp) | Byte-exact C decompilation of Azure Dreams (PS1, SLUS-00614) | 3 | 🟢 | C |
| [Bubsy 3D: Furbitten Planet](https://github.com/EiscremeWaffle/bubsy3d-decomp) | Matching decompilation of Bubsy 3D: Furbitten Planet (PlayStation, 1996) | 3 | 🟢 | C |
| [Diablo decomp](https://github.com/diabpsx/psx_decomp) | Decompilation of Diablo (PS1) | 3 | 🟢 | Assembly |
| [Digimon World disassembly](https://github.com/wowjinxy/DigimonWorldDisassembly) | Disassembly of Digimon World (PS1) | 3 | 🟡 | C++ |
| [Dino Crisis 2](https://github.com/anzaldoivan/dino-crisis-2-decomp) | Matching decompilation of Dino Crisis 2 (PlayStation, 2000) | 3 | 🟢 | Python |
| [Driver: You Are the Wheelman decomp](https://github.com/olink9/driver1-decomp) | Matching decompilation of Driver: You Are the Wheelman (PS1, 1999) | 3 | 🟢 | C |
| [GT2-Decomp](https://github.com/CurtisSlone/GT2-Decomp) | Source code reverse engineered from Gran Turismo 2 (PS1) | 3 | 🟢 | C |
| [King's Field decomp](https://github.com/sushi-shi/kings-field-decomp) | Matching decompilation of King's Field (PS1, Japan SLPS-00017) | 3 | 🟢 | Python |
| [Moto Racer World Tour decomp](https://github.com/Almamu/MotoRacerWorldTour-decomp) | Decompilation of Moto Racer World Tour (PS1) | 3 | 🟢 | Assembly |
| [Winning Eleven 3: Final Ver. decomp](https://github.com/coffeeconleche/winning-eleven-3-final-ver-decomp) | Decompilation of Winning Eleven 3: Final Ver. (PS1) | 3 | 🟢 | Assembly |
| [Gran Turismo 2 Simulation Mode decomp](https://github.com/vairacing-tech/GT2-DECOMP) | Decompilation of the Gran Turismo 2 Simulation Mode (PS1) | 2 | 🟢 | C |
| [Hybrid decomp](https://github.com/Joshua-1248/Hybrid-PS1-Decompilation) | Decompilation of Hybrid (PS1, Japan) | 2 | 🟢 | Assembly |
| [Mega Man X6](https://github.com/anzaldoivan/mmx6) | Matching decompilation of Mega Man X6 (PlayStation, 2001) | 2 | 🟢 | C |
| [Yu-Gi-Oh! Forbidden Memories decomp](https://github.com/MaChInEgUn3/ygofm-decomp) | Matching decompilation of Yu-Gi-Oh! Forbidden Memories (PS1, SLUS-01411) | 2 | 🟢 | Assembly |
| [Crash Bandicoot decomp](https://github.com/khasinski/crash-bandicoot-decomp) | Matching decompilation of Crash Bandicoot (PS1, USA SCUS-94900) | 1 | 🟢 | C |
| [Digimon World 3 decomp](https://github.com/grant-might/DW3_Decomp) | Decompilation of Digimon World 3 (PS1) | 1 | 🟢 | C |
| [Kaze no Notam](https://github.com/aaaaaaaaaaway/kaze-no-notam-decomp) | Matching decompilation of Kaze no Notam (PlayStation, 2001) | 1 | 🟢 | C |
| [Pepsiman decomp](https://github.com/brian-oblivion/pepsiman-decomp) | Decompilation of Pepsiman (PS1) | 1 | 🟢 | C |
| [Pepsiman decomp](https://github.com/wowjinxy/PepsiMan-Decomp) | Decompilation of Pepsiman (PS1) | 1 | 🟡 | Assembly |
| [Persona 2: Innocent Sin decomp](https://github.com/kaikecarlos/philemon) | Decompilation of Persona 2: Innocent Sin (PS1) | 1 | 🟡 | Assembly |
| [Pipe Dreams 3D decomp](https://github.com/bismurphy/pipedreams_decomp) | Decompilation of Pipe Dreams 3D (PS1) | 1 | 🟢 | C |
| [Spyro the Dragon to C decomp](https://github.com/celophi/spyro-decompilation) | Decompilation of Spyro the Dragon to C (PS1) | 1 | 🟡 | C |
| [Star Wars Episode I: The Phantom Menace decomp](https://github.com/esp-cpp/tpm-decomp) | Decompilation of Star Wars Episode I: The Phantom Menace (PS1, USA Rev 1) | 1 | 🟢 | C |
| [The Flintstones: Bedrock Bowling decomp](https://github.com/thearchivalone/YabaDaba-Bowling-Decomp) | Byte-matched decompilation of The Flintstones: Bedrock Bowling (PS1) | 1 | 🟢 | Makefile |
| [Tokimeki Memorial: Forever With You (CelestialAmber)](https://github.com/CelestialAmber/tokimemo) | Matching decompilation of Tokimeki Memorial: Forever With You (PlayStation, 1995) | 1 | 🟡 | Python |
| [Tomba! 2: The Evil Swine Return decomp](https://github.com/erneztox/tomba2-decomp) | Matching decompilation of Tomba! 2: The Evil Swine Return (PS1) | 1 | 🟢 | C |
| [Tombi!](https://github.com/afsenovilla/Tombi-Decomp) | Matching decompilation of Tombi! (PlayStation, 1997) | 1 | 🟢 | C |
| [Toy Story Racer decomp](https://github.com/mateusfavarin/tsr) | Decompilation of Toy Story Racer (PS1) | 1 | 🟢 | C |
| [Ape Escape decomp](https://github.com/SSZero88/apes-escaped) | Decompilation of Ape Escape (PS1) | 0 | 🟢 | C |
| [Ape Escape decomp](https://github.com/DeprivedPeasant/ape-escape-decomp-port) | Readable decompilation and native port of Ape Escape (PS1, SCUS-94423) | 0 | 🟢 | C |
| [Civilization II decomp](https://github.com/nikitastaf1996/civ2_decomp) | Matching decompilation of Civilization II (PS1, SLUS-00792) | 0 | 🟢 | Assembly |
| [croc_psx](https://codeberg.org/misbk/croc_psx) | Decompilation of the PSX demo of Croc: Legend of the Gobbos |  | ⚪ |  |
| [Digimon World 2003 / Digimon World 3 decomp](https://github.com/mateusgiordani/dw3-decomp-expanded) | Matching decompilation of Digimon World 2003 / Digimon World 3 (PS1, PAL) | 0 | 🟢 | C |
| [Final Fantasy VII decomp](https://github.com/armstrca/ff7-decomp-old) | Matching decompilation of Final Fantasy VII (PS1) | 0 | 🟢 | C |
| [Galaxian3: Project Dragoon decomp](https://github.com/s-ilent/cannon-seed) | Matching decompilation of Galaxian3: Project Dragoon (PS1) | 0 | 🟢 | Assembly |
| [King's Field II decomp](https://github.com/auser1337/kf2-decomp) | Decompilation of King's Field II (PS1) | 0 | 🗄️ | Makefile |
| [King's Field II decomp](https://github.com/sushi-shi/kings-field-2-decomp) | Matching decompilation of King's Field II (PS1, Japan SLPS-00069) | 0 | 🟢 | Python |
| [LSD: Dream Emulator decomp](https://github.com/klNuno/lsd-decomp) | Matching decompilation of LSD: Dream Emulator (PS1) | 0 | 🟢 | C |
| [Mega Man X5](https://github.com/anzaldoivan/mmx5) | Matching decompilation of Mega Man X5 (PlayStation, 2000) | 0 | 🟢 | C |
| [Nightmare Creatures decomp](https://github.com/kirby-letsgo/nightmare-creatures-decomp) | Decompilation of Nightmare Creatures (PS1) | 0 | 🟢 | C |
| [Rampage 2: Universal Tour decomp](https://github.com/ReGame-Labs/rmpg2-ut_decomp) | Matching decompilation of Rampage 2: Universal Tour (PS1, USA) | 0 | 🟢 | C |
| [Shin Megami Tensei](https://codeberg.org/chickenzes/smt-decomp) | Matching decompilation of Shin Megami Tensei (PlayStation, 2001) |  | ⚪ |  |
| [Sled Storm decomp](https://github.com/Dosalock/sled-storm-decomp) | Decompilation of Sled Storm (PS1) | 0 | 🟡 | Assembly |
| [Spyro 2: Gateway to Glimmer decomp](https://github.com/marcovoc/spyro2-decomp) | Matching decompilation of Spyro 2: Gateway to Glimmer (PS1, SCES-02104) | 0 | 🟢 | C |
| [tactical-decomp](https://github.com/Kyagara/tactical-decomp) | Final Fantasy Tactics decompilation and recompilation projects (PS1) | 0 | 🟢 | C |
| [Valkyrie Profile decomp](https://github.com/waterrr1389/valkyrie-profile-decomp) | Partial matching decompilation of Valkyrie Profile (PS1, Japan Rev 1) | 0 | 🟢 | C |
| [WWF SmackDown! 2: Know Your Role decomp](https://github.com/martinbean/smackdown2) | Decompilation of WWF SmackDown! 2: Know Your Role (PS1) | 0 | 🟢 | BitBake |
| [Xena: Warrior Princess decomp](https://github.com/filippgl/xena-psx-decomp) | Decompilation and native PC port of Xena: Warrior Princess (PS1, SLUS-00977) | 0 | 🟢 | C |

## Matching Decompilations — PlayStation 2

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Resident Evil – Code: Veronica X](https://github.com/AshfordFamily/recvx-decomp) | Matching decompilation of Resident Evil – Code: Veronica X (PlayStation 2, 2001) | 297 | 🟢 | C |
| [Street Fighter III: 3rd Strike](https://github.com/crowded-street/3s-decomp) | Matching decompilation of Street Fighter III: 3rd Strike (PlayStation 2, 2004) | 283 | 🟢 | C |
| [Sly Cooper and the Thievius Raccoonus](https://github.com/TheOnlyZac/sly1) | Matching decompilation of Sly Cooper and the Thievius Raccoonus (PlayStation 2, 2002) | 279 | 🟢 | C++ |
| [PaRappa the Rapper 2](https://github.com/parappadev/parappa2) | Matching decompilation of PaRappa the Rapper 2 (PlayStation 2, 2001) | 207 | 🟢 | C |
| [Silent Hill 3](https://github.com/dreamingmoths/memory-of-alessa) | Matching decompilation of Silent Hill 3 (PlayStation 2, 2003) | 160 | 🟢 | C |
| [Shadow of the Colossus](https://github.com/Fantaskink/SOTC) | Matching decompilation of Shadow of the Colossus (PlayStation 2, 2005; preview build) | 143 | 🟢 | C |
| [Fatal Frame](https://github.com/Mikompilation/Himuro) | Matching decompilation of Fatal Frame (PlayStation 2, 2001) | 133 | 🟢 | C |
| [Kingdom Hearts](https://github.com/ethteck/kh1) | Matching decompilation of Kingdom Hearts (PlayStation 2, 2002) | 112 | 🟢 | C |
| [Dark Cloud](https://github.com/TheMoonPeople/Chronicle) | Matching decompilation of Dark Cloud (PlayStation 2, 2000) | 104 | 🟢 | C++ |
| [Gran Turismo 4](https://github.com/gustavocanepa/gt4-decomp) | Matching decompilation of Gran Turismo 4 (PlayStation 2, 2004) | 91 | 🟢 | C |
| [God Hand](https://github.com/LucasPicoli/god-hand-decomp) | Matching decompilation of God Hand (PlayStation 2, 2006) | 75 | 🟢 | C |
| [Persona3-FES-Decompilation](https://github.com/snaku/Persona3-FES-Decompilation) | Decompilation of Shin Megami Tensei: Persona 3 FES | 70 | 🟢 | C |
| [Ratchet & Clank (PAL)](https://github.com/OpenRAC/rac1-decomp) | Matching decompilation of Ratchet & Clank (PlayStation 2, 2002; PAL version) | 61 | 🟢 | C |
| [Shin Megami Tensei: Persona 4](https://github.com/Raikaru/Persona4-Decompilation) | Matching decompilation of Shin Megami Tensei: Persona 4 (PlayStation 2, 2008) | 49 | 🟢 | C |
| [ico](https://github.com/nathanialf/ico) | Decompilation of ICO (PS2) | 48 | 🟢 | C |
| [Ratchet & Clank (USA)](https://github.com/lombyte-project/Lombyte) | Matching decompilation of Ratchet & Clank (PlayStation 2, 2002; USA version) | 47 | 🟢 | C |
| [Klonoa 2: Lunatea's Veil](https://github.com/entriphy/kl2_lv_decomp) | Matching decompilation of Klonoa 2: Lunatea's Veil (PlayStation 2, 2001) | 45 | 🟡 | C |
| [Monster Hunter (JP)](https://github.com/2Tie/mh1j) | Matching decompilation of Monster Hunter (PlayStation 2, 2004; Japanese version) | 44 | 🟢 | C |
| [twinsanity-reversed](https://github.com/Smartkin/twinsanity-reversed) | Reverse-engineered code of Crash Twinsanity (PS2) | 40 | 🟢 | C++ |
| [OpenRAC](https://github.com/OpenRAC/OpenRAC) | Matching decompilation and PC port effort for the Ratchet & Clank series (PS2) | 38 | 🟢 | C |
| [SSX 3](https://github.com/ssxdecomp/ssx3) | Matching decompilation of SSX 3 (PlayStation 2, 2003) | 38 | 🟢 | Python |
| [Dark Cloud 2](https://github.com/TheMoonPeople/ChronicleTwo) | Matching decompilation of Dark Cloud 2 (PlayStation 2, 2002) | 35 | 🟢 | C++ |
| [Ratchet & Clank 3: Up Your Arsenal decomp](https://github.com/vetusmagnus/rac3-uya-decomp) | Decompilation of Ratchet & Clank 3: Up Your Arsenal (PS2) | 35 | 🟢 | C |
| [Shin Megami Tensei: Digital Devil Saga](https://github.com/Megami-Decomps/dds-decomp) | Matching decompilation of Shin Megami Tensei: Digital Devil Saga (PlayStation 2, 2004) | 35 | 🟢 | C |
| [Ico](https://github.com/RossyDoubleUnderscore/ICO-decomp) | Matching decompilation of Ico (PlayStation 2, 2001) | 33 | 🟢 | C |
| [REOF2](https://github.com/caprado/REOF2) | Resident Evil Outbreak File #2 (PS2) decompilation and preservation project | 32 | 🟢 | C |
| [Yakuza](https://github.com/Hamzaxx370/Ogre-Decomp) | Matching decompilation of Yakuza (PlayStation 2, 2005) | 31 | 🟢 | C++ |
| [Metal Gear Solid 3 decomp](https://github.com/GirianSeed/mgs3) | Decompilation of Metal Gear Solid 3 (PS2) | 29 | 🟢 | C |
| [Silent Hill 2 (sh23ds)](https://github.com/ankushKun/sh23ds) | Decompilation of Silent Hill 2 (PS2) | 28 | 🟢 | C |
| [SSX 3 decomp](https://github.com/andersfischernielsen/ssx3-decomp) | Decompilation and Rust port of SSX 3 (PS2) | 27 | 🟢 | Rust |
| [BT3-Decompiled](https://github.com/z3xox/BT3-Decompiled) | Matching decompilation of Dragon Ball Z: Budokai Tenkaichi 3 (PS2) | 26 | 🟢 | C |
| [Twisted Metal: Black](https://github.com/OpenTrac/tmb_Re-Arc) | Matching decompilation of Twisted Metal: Black (PlayStation 2, 2001) | 22 | 🟢 | C |
| [Crash Twinsanity](https://github.com/GioPixelGH/Crash-Twinsanity-Windows) | Decompilation of Crash Twinsanity (PS2) | 21 | 🟢 | C++ |
| [OpenHuey](https://github.com/ArnautDaniel/OpenHuey) | Haunting Ground (PS2) decompilation, PC port and actor-based rewrite | 21 | 🟢 | C |
| [Ratchet: Deadlocked](https://github.com/OpenRAC/rac4-decomp) | Matching decompilation of Ratchet: Deadlocked (PlayStation 2, 2005) | 21 | 🟢 | C |
| [Shadow of the Colossus decomp](https://github.com/TheRealestNwah/sotc-decomp) | Matching decompilation of Shadow of the Colossus (PS2, NTSC-U) | 21 | 🟢 | C |
| [SSX](https://github.com/ssxdecomp/ssx) | Matching decompilation of SSX (PlayStation 2, 2000) | 21 | 🟢 | Python |
| [Crash Bandicoot: The Wrath of Cortex (PS2)](https://github.com/denzi-gh/crashwoc-decomp-ps2) | Decompilation of Crash Bandicoot: The Wrath of Cortex (PS2) | 20 | 🟢 | C |
| [Resident Evil: Dead Aim](https://github.com/cakehonolulu/Bullseye) | Matching decompilation of Resident Evil: Dead Aim (PlayStation 2, 2003) | 20 | 🟢 | C++ |
| [SNESstation-Decomp](https://github.com/ReyFxck/SNESstation-Decomp) | Decompilation of the SNESStation PS2 emulator based on SNES9X 1.41 | 19 | 🟢 | Python |
| [Twisted Metal: Harbor City](https://github.com/jacobleeharris/tmhc) | Matching decompilation of Twisted Metal: Harbor City (PlayStation 2, unreleased) | 19 | 🟢 | C |
| [Way of the Samurai 2 decomp](https://github.com/acklavidian/decomp_wots2) | Decompilation and native Linux port of Way of the Samurai 2 (PS2) | 18 | 🟢 | C++ |
| [Xenosaga Episode I](https://github.com/OpokXeno/xsg-i-decomp) | Matching decompilation of Xenosaga Episode I (PlayStation 2, 2002) | 18 | 🟢 | Java |
| [Xenosaga Episode I (squareman)](https://github.com/SquareMan/xenosaga) | Matching decompilation of Xenosaga Episode I (PlayStation 2, 2002) | 18 | 🟡 | C |
| [Dog's Life](https://github.com/IWILLCRAFT-M0d/dogcomp) | Matching decompilation of Dog's Life (PlayStation 2, 2003) | 16 | 🟢 | C++ |
| [PS2 OSDSYS system menu decomp](https://github.com/JeanxPereira/CrystalOSD-Decomp-Legacy) | Matching decompilation of the PS2 OSDSYS system menu (archived) | 16 | 🗄️ | Assembly |
| [Silent Hill 2](https://github.com/dreamingmoths/mirror-of-alessa) | Matching decompilation of Silent Hill 2 (PlayStation 2, 2001) | 16 | 🟢 |  |
| [Marvel vs. Capcom 2 (PS2)](https://github.com/g-guthrie/mvc2-ps2-decomp) | Decompilation of Marvel vs. Capcom 2 (PS2) | 15 | 🟢 | C |
| [Resident Evil Outbreak and File 2 decomp](https://github.com/GalaxyNostalgia/Outbreak-decomp) | Decompilation of Resident Evil Outbreak and File 2 (PS2) | 15 | 🟢 | C |
| [Star Ocean: Till the End of Time](https://github.com/celophi/so3-decomp) | Matching decompilation of Star Ocean: Till the End of Time (PlayStation 2, 2003) | 15 | 🟢 | C++ |
| [Crash Bandicoot: The Wrath of Cortex (crash-ps2)](https://github.com/calmsacibis995/crash-ps2) | Decompilation of Crash Bandicoot: The Wrath of Cortex (crash-ps2) | 14 | 🟡 | C |
| [King's Field: The Ancient City decomp](https://github.com/Voicedrew11/kfiv-decomp) | Decompilation of King's Field: The Ancient City (PS2) | 14 | 🟢 | C |
| [Guilty Gear X Plus](https://github.com/WistfulHopes/ggx) | Matching decompilation of Guilty Gear X Plus (PlayStation 2, 2001; Korean version) | 11 | 🟡 | Python |
| [Ratchet & Clank PS2 quadrilogy (Pyrocitor)](https://github.com/VELD-Dev/Pyrocitor) | Decompilation of Ratchet & Clank PS2 quadrilogy (Pyrocitor) | 11 | 🗄️ | C++ |
| [SSX Tricky](https://github.com/ssxdecomp/ssxtricky) | Matching decompilation of SSX Tricky (PlayStation 2, 2001) | 11 | 🟢 | Python |
| [Baroque-Decomp](https://github.com/Arch61s/Baroque-Decomp) | Decompilation of Baroque (2004) with quality-of-life features (PS2) | 10 | 🟢 | C++ |
| [Kingdom Hearts II decomp](https://github.com/GovanifY/kh2) | Decompilation of Kingdom Hearts II (PS2) | 9 | 🟢 | C++ |
| [Monster Hunter 2 decomp](https://github.com/Batenkaitos-dev/mh2-decomp) | Byte-matching decompilation of Monster Hunter 2 (Dos) (PS2) | 9 | 🟢 | C |
| [Champions of Norrath decomp](https://github.com/ensapra/champions-of-norrath) | Matching decompilation of Champions of Norrath (PS2) | 8 | 🟢 | C |
| [Gran Turismo 3: A-Spec decomp](https://github.com/gustavocanepa/gt3-decomp) | Matching decompilation of Gran Turismo 3: A-Spec (PS2) | 8 | 🟢 | C |
| [Pro Evolution Soccer 6 decomp](https://github.com/Subarasheese/pes6decomp) | Decompilation of Pro Evolution Soccer 6 (PS2) | 7 | 🟢 | C |
| [Shaun Palmer's Pro Snowboarder](https://github.com/Daniel-McCarthy/SPPS) | Matching decompilation of Shaun Palmer's Pro Snowboarder (PlayStation 2, 2001) | 7 | 🟢 | C |
| [Sonic Riders: Zero Gravity (PS2 prototype)](https://github.com/KidWizardOfTheWeb/SR2) | Decompilation of Sonic Riders: Zero Gravity (PS2 prototype) | 7 | 🟢 | C++ |
| [.hack//IMOQ games decomp](https://github.com/dothacktranslate/dothack-decompilation) | Decompilation of the .hack//IMOQ games (PS2) | 6 | 🟢 | Python |
| [Fahrenheit / Indigo Prophecy decomp](https://github.com/fmil95/santamonica) | Decompilation of Fahrenheit / Indigo Prophecy (PS2) | 6 | 🟢 | C++ |
| [Saint Seiya: The Hades decomp](https://github.com/matpdev/SaintSeiyaRecomp) | Matching decompilation of Saint Seiya: The Hades (PS2, Europe SLES-54162) | 6 | 🟢 | C |
| [Xenosaga Episode I: Der Wille zur Macht decomp](https://github.com/ValakTurtle/Xenosaga-I-Decomp) | Decompilation of Xenosaga Episode I: Der Wille zur Macht (PS2) | 6 | 🟢 | Python |
| [Amplitude](https://github.com/ieee802dot11ac/amp) | Matching decompilation of Amplitude (PlayStation 2, 2003) | 5 | 🟡 | Python |
| [CoD2-BRO-Decomp](https://github.com/SmokeDoggy044/CoD2-BRO-Decomp) | Decompilation of Call of Duty 2: Big Red One toward a native build | 5 | 🟢 | C++ |
| [Devil May Cry 3: Dante's Awakening decomp](https://github.com/WadeWinningWilson/dmc3-decomp) | Decompilation of Devil May Cry 3: Dante's Awakening (PS2) | 5 | 🟢 | C++ |
| [ffx](https://github.com/Rozelette/ffx) | Decompilation of Final Fantasy X (PS2) | 5 | 🟢 | Python |
| [Phantasy Star II Disassembly](https://github.com/jon13doe/SEGA_ps2_disasm) | Phantasy Star II Disassembly | 5 | 🔴 | Assembly |
| [PS2 OSDSYS (system menu)](https://github.com/JeanxPereira/CrystalOSD) | Decompilation of PS2 OSDSYS (system menu) | 5 | 🟢 | JavaScript |
| [Ratchet & Clank: Going Commando decomp](https://github.com/platypet2217-star/RAC2Decomp) | Decompilation and reverse engineering of Ratchet & Clank: Going Commando (PS2) | 5 | 🟢 | C |
| [Rogue Galaxy decomp](https://github.com/Dorgengoa/RGDecomp) | Decompilation of Rogue Galaxy (PS2) | 5 | 🟢 | C |
| [Syphon Filter: The Omega Strain](https://github.com/zm2283145/syphon-filter-omega-strain-decomp) | Matching decompilation of Syphon Filter: The Omega Strain (PlayStation 2, 2004) | 5 | 🟢 | C |
| [Zone of the Enders decomp](https://github.com/GirianSeed/zoe1) | Decompilation of Zone of the Enders (PS2) | 5 | 🟢 | C |
| [Burnout 3: Takedown decomp](https://github.com/siddharthakumar-98/Burnout3) | Byte-matching decompilation of Burnout 3: Takedown (PS2, NTSC-U) | 4 | 🟢 | Python |
| [C kernel of Jak X: Combat Racing decomp](https://github.com/yodaxtah/jakx-c-kernel-decompiled) | Decompilation of the C kernel of Jak X: Combat Racing (PS2) | 4 | 🟡 | C |
| [Crash Nitro Kart decomp](https://github.com/YacaloX-Studios/cnk-decomp) | Decompilation of Crash Nitro Kart (PS2) | 4 | 🟢 | Assembly |
| [Drakan: The Ancients' Gates](https://github.com/cScarletter/Drakan-The-Ancient-Gates-Decompilation-) | Matching decompilation of Drakan: The Ancients' Gates (PlayStation 2, 2002) | 4 | 🟡 |  |
| [Naruto Shippuden: Ultimate Ninja 5 decomp](https://github.com/MiguelQueiroz010/Decomp-no-Me-UN5Decomp) | Decompilation of Naruto Shippuden: Ultimate Ninja 5 (PS2) | 4 | 🟢 | Python |
| [Over the Hedge decomp](https://github.com/dantekall/Over-The-Hedge---Decompilation) | Decompilation of Over the Hedge (PS2) | 4 | 🟢 | Assembly |
| [Ratchet & Clank: Size Matters decomp](https://github.com/OpenRAC/rac5-sm-decomp) | Matching decompilation of Ratchet & Clank: Size Matters (PS2, USA) | 4 | 🟢 | C |
| [Tourist Trophy](https://github.com/gustavocanepa/tt-decomp) | Matching decompilation of Tourist Trophy (PlayStation 2, 2006) | 4 | 🟢 | C |
| [Yu-Gi-Oh! The Duelists of the Roses decomp](https://github.com/kira-502/dotr-decomp) | Matching decompilation of Yu-Gi-Oh! The Duelists of the Roses (PS2, SLUS-20515) | 4 | 🟢 | C |
| [Zone of the Enders: The 2nd Runner decomp](https://github.com/GirianSeed/zoe2) | Decompilation of Zone of the Enders: The 2nd Runner (PS2) | 4 | 🟢 | C |
| [Guitar Hero III: Legends of Rock decomp](https://github.com/Ketbome/gh3-decomp) | Matching decompilation of Guitar Hero III: Legends of Rock (PS2, SLUS-21672) | 3 | 🟢 | C++ |
| [Ratchet & Clank: Up Your Arsenal decomp](https://github.com/OpenRAC/rac3-decomp) | Decompilation of Ratchet & Clank: Up Your Arsenal (PS2) | 3 | 🟢 | C |
| [Rayman 3 decomp](https://github.com/LawlessCowboy/ray3) | Matching decompilation of Rayman 3 (PS2, Korean version) | 3 | 🟢 | C |
| [Treasure Planet](https://github.com/Colt-Zero/Thousand-Worlds) | Asset and level editor for Disney's Treasure Planet (PlayStation 2, 2002) | 3 | 🟡 | Python |
| [Are You Smarter Than a 5th Grader: Make the Grade](https://github.com/Gmon20/makethedecomp) | Matching decompilation of Are You Smarter Than a 5th Grader: Make the Grade (PlayStation 2, 2009) | 2 | 🟡 | C |
| [Chulip](https://github.com/aaaaaaaaaaway/chulip-decomp) | Matching decompilation of Chulip (PlayStation 2, 2002) | 2 | 🟢 | C |
| [EverQuest Online Adventures: Frontiers decomp](https://github.com/DabDavis/eqoa-decomp) | Matching decompilation of EverQuest Online Adventures: Frontiers (PS2) | 2 | 🟢 | C++ |
| [Legaia 2: Duel Saga decomp](https://github.com/WeAreTommyBruh/Legaia2-Decomp) | Reverse engineering and decompilation of Legaia 2: Duel Saga (PS2, PAL) | 2 | 🟢 | C |
| [Monster Hunter decomp](https://github.com/itsbigcforme67/mh1-xbox) | Matching decompilation of Monster Hunter (PS2, Japan) aimed at an original Xbox port | 2 | 🟢 | C |
| [Shox: Rally Reinvented decomp](https://github.com/cblackler19/shox-rr-decomp) | Byte-matched decompilation of Shox: Rally Reinvented (PS2) | 2 | 🟢 | C++ |
| [Stretch Panic](https://github.com/Harskov/stretch-panic-usa) | Matching decompilation of Stretch Panic (PlayStation 2, 2001) | 2 | 🟢 | C |
| [The Sims 2: Castaways decomp](https://github.com/simdecomp/ts2c) | Decompilation of The Sims 2: Castaways | 2 | 🔴 | Assembly |
| [Ar tonelico II: Melody of Metafalica](https://github.com/USED255/artonelico2-decomp) | Matching decompilation of Ar tonelico II: Melody of Metafalica (PlayStation 2, 2007) | 1 | 🟢 | C |
| [Champions: Return to Arms decomp](https://github.com/Open-Champions/champions-return-to-arms) | Byte-exact C++ source reconstruction of Champions: Return to Arms (PS2) | 1 | 🟢 | Python |
| [Extermination decomp](https://github.com/FastestMolasses/Extermination) | Decompilation of Extermination (PS2, 2001) | 1 | 🟢 | C |
| [George of the Jungle and the Search for the Secret](https://github.com/2gifts/george-decomp) | Matching decompilation of George of the Jungle and the Search for the Secret (PlayStation 2, 2008) | 1 | 🟢 | C |
| [Gregory Horror Show decomp](https://github.com/Nathan-R-Og/ghs) | Decompilation of Gregory Horror Show (PS2) | 1 | 🟢 | C |
| [Midnight Club 3: DUB Edition Remix decomp](https://github.com/siddharthakumar-98/MC3DER) | Byte-matching decompilation of Midnight Club 3: DUB Edition Remix (PS2, NTSC-U) | 1 | 🟢 | Rust |
| [Shin Megami Tensei III: Nocturne decomp](https://github.com/Megami-Decomps/smt3-decomp) | Decompilation of Shin Megami Tensei III: Nocturne (PS2) | 1 | 🟢 | C |
| [Summoner 2 decomp](https://github.com/mikegoforth/summoner-2-decomp) | Decompilation of Summoner 2 (PS2) | 1 | 🟢 | C++ |
| [Amplitude decomp](https://github.com/Tatsh/wavelength) | Reconstructed source of Amplitude (PS2) | 0 | 🟢 | C++ |
| [Bokura no Kazoku decomp](https://github.com/conor-sometimes/bokura-no-kazoku-decomp) | Matching decompilation of Bokura no Kazoku (PS2, Japan) | 0 | 🟢 | C++ |
| [Fate/Unlimited Codes decomp](https://github.com/Harskov/fate-unlimited-codes-jp) | Matching decompilation of Fate/Unlimited Codes (PS2, Japan) | 0 | 🟢 | C |
| [FreQuency decomp](https://github.com/Tatsh/resonance) | Reconstructed source of FreQuency (PS2) | 0 | 🟢 | C++ |
| [Marchen Awakens Romance: Arm Fight Dream decomp](https://github.com/name1esshero/Marchen-Awakens-Romance-PS2) | Decompilation of Marchen Awakens Romance: Arm Fight Dream (PS2) | 0 | 🟢 | Python |
| [Shadow Hearts](https://git.sr.ht/~benoitren/shadowheartsdecompilation) | Matching decompilation of Shadow Hearts (PlayStation 2, 2001) |  | ⚪ |  |
| [Shadow of the Colossus decomp](https://github.com/NathanFahey23/Shadow-of-the-Colossus-Decomp) | Matching decompilation of Shadow of the Colossus (PS2, NTSC-U) | 0 | 🗄️ | C |
| [ts-ps2-decomp](https://codeberg.org/OpenMonkey/ts-ps2-decomp) | Decompilation of TimeSplitters 1 and 2 (PS2), part of the OpenMonkey project |  | ⚪ |  |

## Matching Decompilations — SNES / NES

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Elite decomp](https://github.com/markmoxon/elite-source-code-nes) | Fully documented reverse-engineered source code of Elite (NES) | 409 | 🟢 | Assembly |
| [Battle City (NES disassembly)](https://github.com/cyneprepou4uk/NES-Games-Disassembly) | Disassembly / decompilation of Battle City (NES disassembly) | 302 | 🟢 | Assembly |
| [zelda1-disassembly](https://github.com/aldonunez/zelda1-disassembly) | A complete disassembly of The Legend of Zelda | 278 | 🔴 | Assembly |
| [smb3](https://github.com/captainsouthbird/smb3) | Disassembly of Super Mario Bros 3 | 255 | 🟡 | Assembly |
| [Contra (NES)](https://github.com/vermiceli/nes-contra-us) | Decompilation of Contra (NES) | 233 | 🟢 | Assembly |
| [EarthBound](https://github.com/Herringway/ebsrc) | Source code recreation of EarthBound (SNES, 1994) | 187 | 🟢 | Assembly |
| [SMWDisX](https://github.com/IsoFrieze/SMWDisX) | Super Mario World disassembly X (SNES) | 182 | 🟢 | Assembly |
| [Super Mario World 2: Yoshi's Island (SNES) Disassembly](https://github.com/brunovalads/yoshisisland-disassembly) | Full disassembly of Yoshi's Island (SNES) version U 1.0 | 162 | 🟢 | Assembly |
| [supermetroid](https://github.com/strager/supermetroid) | Super Metroid SNES disassembly | 161 | 🔴 | Assembly |
| [Star Fox](https://github.com/kandowontu2/starfox-enhanced) | Decompilation of Star Fox (SNES) | 111 | 🟢 | C++ |
| [superbomberman](https://github.com/LIJI32/superbomberman) | Disassembly and remade build system for SNES game Super Bomberman | 111 | 🟢 | Assembly |
| [FF Disassembly](https://github.com/Entroper/FF1Disassembly) | Disassembly of Final Fantasy (Assembly) | 110 | 🟢 | Assembly |
| [TetrisNESDisasm](https://github.com/CelestialAmber/TetrisNESDisasm) | Disassembly of Tetris (NES) | 110 | 🟡 | Assembly |
| [smb2](https://github.com/Xkeeper0/smb2) | Super Mario Bros. 2 (NES) disassembly | 102 | 🔴 | Assembly |
| [Final Fantasy VI Disassembly](https://github.com/everything8215/ff6) | Disassembly and ROM info for Final Fantasy VI | 90 | 🟢 | Assembly |
| [dragon-warrior-disassembly](https://github.com/nmikstas/dragon-warrior-disassembly) | NES Dragon Warrior software disassembly | 89 | 🔴 | Assembly |
| [The Legend of Zelda](https://github.com/camthesaxman/zeldasource) | Disassembly of Legend of Zelda | 77 | 🔴 | Assembly |
| [Donkey Kong Country 2](https://github.com/p4plus2/DKC2-disassembly) | Disassembly of Donkey Kong Country 2 (SNES, 1995) | 76 | 🟡 | Assembly |
| [Tecmo_Super_Bowl_NES_Disassembly](https://github.com/bruddog/Tecmo_Super_Bowl_NES_Disassembly) | Rebuildable 6502 disassembly of Tecmo Super Bowl (NES) | 63 | 🟡 | Assembly |
| [smw-src](https://github.com/galaxyhaxz/smw-src) | Source code of Super Mario World from its SNES disassembly | 58 | 🔴 | Assembly |
| [Mega Man 3 (NES) Disassembly](https://github.com/refreshing-lemonade/megaman3-disassembly) | Full disassembly of Mega Man 3 (NES) | 52 | 🔴 | Assembly |
| [Super Mario RPG disassembly](https://github.com/Yoshifanatic1/Super-Mario-RPG-Disassembly) | Disassembly of Super Mario RPG (SNES) | 49 | 🔴 | Assembly |
| [mike-tysons-punch-out-disassembly](https://github.com/nmikstas/mike-tysons-punch-out-disassembly) | Reverse engineering effort of the NES game Mike Tyson's Punch-Out. | 46 | 🔴 | Assembly |
| [Balloon Fight](https://github.com/LuigiBlood/balloonfight_dis) | Disassembly of Balloon Fight (NES, 1984) | 44 | 🔴 | Assembly |
| [Super Mario Bros. disassembly](https://github.com/Xkeeper0/smb1) | Disassembly of Super Mario Bros. (NES) | 41 | 🔴 | Assembly |
| [Zelda no Densetsu: Kamigami no Triforce disassembly](https://github.com/spannerisms/jpdasm) | Annotated disassembly of Zelda no Densetsu: Kamigami no Triforce (SNES, Japan) | 38 | 🟢 | Assembly |
| [Final Fantasy IV Disassembly](https://github.com/everything8215/ff4) | Final Fantasy IV Disassembly | 35 | 🔴 | Assembly |
| [Fire Emblem: Thracia 776 disassembly](https://github.com/ZaneAvernathy/FireEmblem5) | Disassembly of Fire Emblem: Thracia 776 (Super Famicom) | 35 | 🟡 | Assembly |
| [Mega Man 5 (NES) Disassembly](https://github.com/refreshing-lemonade/megaman5-disassembly) | Full disassembly of Mega Man 5 (NES) | 34 | 🟡 | Assembly |
| [Metroid Disassembly](https://github.com/nmikstas/metroid-disassembly) | Metroid software disassembly | 33 | 🟡 | Assembly |
| [Bomberman decomp](https://github.com/emu-russia/bomberman-nes) | Reverse-engineered source code of Bomberman (NES) | 32 | 🟢 | Assembly |
| [SMAS-Disassembly](https://github.com/Maseya/SMAS-Disassembly) | Disassembly of the Super Mario All-Stars SNES ROM | 32 | 🟢 | Assembly |
| [Zelda II: The Adventure of Link disassembly](https://github.com/FiendsOfTheElements/z2disassembly) | Disassembly of Zelda II: The Adventure of Link (NES) | 32 | 🔴 | Assembly |
| [Donkey Kong Country](https://github.com/Yoshifanatic1/Donkey-Kong-Country-1-Disassembly) | Disassembly of Donkey Kong Country (SNES, 1994) | 30 | 🔴 | Assembly |
| [Donkey Kong (NES)](https://github.com/RussianManSMWC/Donkey-Kong-NES-Disassembly) | Disassembly / decompilation of Donkey Kong (NES) | 29 | 🟡 | Assembly |
| [Game Genie](https://github.com/qalle2/nes-gg-disassembly) | Disassembly of Game Genie (NES) | 29 | 🗄️ | Assembly |
| [Mega Man 4 (NES) Disassembly](https://github.com/refreshing-lemonade/megaman4-disassembly) | Full disassembly of Mega Man 4 (NES) | 29 | 🔴 | Assembly |
| [Jackal disassembly](https://github.com/RayofJay/NES-Jackal_Disassembly_Fully_Commented) | Fully commented disassembly of Jackal (NES) | 28 | 🔴 | Assembly |
| [smb-disassembly](https://github.com/threecreepio/smb-disassembly) | ca65 disassembly of Super Mario Bros. for the NES | 28 | 🔴 | Assembly |
| [Super C / Probotector (NES)](https://github.com/vermiceli/nes-super-c) | Decompilation of Super C / Probotector (NES) | 28 | 🟢 | Assembly |
| [Super Mario World and its All-Stars releases disassembly](https://github.com/Yoshifanatic1/SMW-SMAS-SMASW-Disassembly) | Disassembly of Super Mario World and its All-Stars releases (SNES) | 28 | 🔴 | Assembly |
| [Shin Megami Tensei v1.0 disassembly](https://github.com/spannerisms/smt1dasm) | Disassembly of Shin Megami Tensei v1.0 (SNES) | 26 | 🔴 | Assembly |
| [ff3](https://github.com/everything8215/ff3) | Disassembly and ROM info for Final Fantasy III (NES) | 24 | 🔴 | Assembly |
| [SMWDisC](https://github.com/gnaghi/SMWDisC) | Super Mario World disassembly SMWDisC (SNES) | 24 | 🔴 |  |
| [Super Metroid disassembly](https://github.com/InsaneFirebat/sm_disassembly) | Relocatable disassembly of Super Metroid (SNES) | 24 | 🟢 | Assembly |
| [Satellaview BS-X BIOS cartridge disassembly](https://github.com/LuigiBlood/bsxbios_dis) | Disassembly of the Satellaview BS-X BIOS cartridge (Super Famicom) | 23 | 🔴 | Assembly |
| [Dr. Mario (NES)](https://github.com/Nostaljipi/dr-mario-disassembly) | Disassembly / decompilation of Dr. Mario (NES) | 22 | 🔴 | Assembly |
| [ff2](https://github.com/everything8215/ff2) | Disassembly and ROM Info for Final Fantasy II (NES) | 22 | 🔴 | Assembly |
| [Final Fantasy V Disassembly](https://github.com/everything8215/ff5) | Disassembly and ROM info for Final Fantasy V | 22 | 🟢 | Assembly |
| [Super Mario Bros. disassembly](https://github.com/pgattic/smb1-disasm) | Disassembly of Super Mario Bros. (NES) | 22 | 🗄️ | Assembly |
| [Donkey Kong Country 3](https://github.com/Yoshifanatic1/Donkey-Kong-Country-3-Disassembly) | Disassembly of Donkey Kong Country 3 (SNES, 1996) | 21 | 🔴 | Assembly |
| [Final Fantasy (FF1-MMC5)](https://github.com/JiggeryPonkery/FF1-MMC5) | Disassembly of Final Fantasy (NES) | 21 | 🔴 | Assembly |
| [Ghosts and Graves](https://github.com/AnthonyBongers/GhostsAndGraves) | Ghosts and Graves, a Tents and Trees demake written in 6502 assembly (NES homebrew) | 21 | 🟢 | Assembly |
| [Hummer Team's unlicensed NES port of Super Mario World disassembly](https://github.com/palaceswitcher/SMW-NES-Disassembly) | Disassembly of Hummer Team's unlicensed NES port of Super Mario World | 20 | 🟢 | Assembly |
| [Mega Man 6 (NES) Disassembly](https://github.com/refreshing-lemonade/megaman6-disassembly) | Full disassembly of Mega Man 6 (NES) | 20 | 🔴 | Assembly |
| [Mother / EarthBound Beginnings disassembly](https://github.com/Nathan-R-Og/mother) | Disassembly of Mother / EarthBound Beginnings (NES) | 20 | 🟢 | Assembly |
| [Donkey-Kong-Country-2-Disassembly](https://github.com/Yoshifanatic1/Donkey-Kong-Country-2-Disassembly) | Disassembly of Donkey Kong Country 2 (Assembly) | 19 | 🔴 | Assembly |
| [Final Fantasy disassembly](https://github.com/BenWenger/FinalFantasyDisassembly) | Fully commented disassembly of Final Fantasy (NES) | 19 | 🔴 | Assembly |
| [Harvest Moon disassembly](https://github.com/ElisaS-Codes/HM-Decomp) | Decompilation and disassembly of Harvest Moon (SNES) | 19 | 🟡 | Assembly |
| [Star Fox disassembly](https://github.com/SpyderTL/StarFoxDisassembly) | Disassembly of Star Fox (SNES, US v1.2) | 18 | 🔴 | Assembly |
| [The Legend of Zelda: A Link to the Past disassembly](https://github.com/walkingeyerobot/alttp-disassembly) | Disassembly of The Legend of Zelda: A Link to the Past (SNES) | 18 | 🔴 | Assembly |
| [smb2j-disassembly](https://github.com/threecreepio/smb2j-disassembly) | ca65 version of doppelgangers fantastic smb2j disassembly | 17 | 🟡 | Assembly |
| [Super Ghouls 'n Ghosts disassembly](https://github.com/FredYeye/Super-Ghouls-n-Ghosts-Disassembly) | Disassembly of Super Ghouls 'n Ghosts (SNES) | 17 | 🟢 | Assembly |
| [Super Mario World 2: Yoshi's Island disassembly](https://github.com/ahoustonpsych/YoshiDis) | Disassembly of Super Mario World 2: Yoshi's Island (SNES) | 17 | 🔴 | Assembly |
| [Tengen Tetris disassembly](https://github.com/zohassadar/TengenTetrisDisasm) | Disassembly of Tengen Tetris (NES, 1989) | 17 | 🟡 | Assembly |
| [Donald Land](https://github.com/brunovalads/donald-land) | Disassembly of Donald Land (NES, 1988) | 16 | 🔴 | Assembly |
| [shiren](https://github.com/CelestialAmber/shiren) | Disassembly of Fushigi no Dungeon 2: Fuurai no Shiren | 16 | 🔴 | Assembly |
| [Fire Emblem: Ankoku Ryu to Hikari no Tsurugi disassembly](https://github.com/StanHash/fe1) | Disassembly of Fire Emblem: Ankoku Ryu to Hikari no Tsurugi (Famicom) | 15 | 🔴 | Assembly |
| [crystalisdisassembly](https://github.com/crystalisdisassembly/crystalisdisassembly) | Disassembly of the NES Game Crystalis | 14 | 🔴 | Assembly |
| [English Translation of Captain Tsubasa 2](https://github.com/cyneprepou4uk/Captain-Tsubasa-2-English-Translation) | Captain Tsubasa 2 [NES] disassembly | 14 | 🟢 | Assembly |
| [Mega Man / Rockman disassembly](https://github.com/TheRealQuantam/mm1dasm) | Compilable disassembly of Mega Man / Rockman (NES) | 14 | 🟢 | Assembly |
| [Mega Man 7 disassembly](https://github.com/Yoshifanatic1/Mega-Man-7-Disassembly) | Disassembly of Mega Man 7 (SNES) | 14 | 🔴 | Assembly |
| [Metroid disassembly](https://github.com/metroidret/m1disasm) | Disassembly of Metroid (NES) | 14 | 🟢 | Assembly |
| [Super Mario Kart disassembly](https://github.com/Yoshifanatic1/Super-Mario-Kart-Disassembly) | Disassembly of Super Mario Kart (SNES) | 14 | 🔴 | Assembly |
| [Dr. Mario disassembly](https://github.com/brianhuffman/drmario) | Disassembly of Dr. Mario (NES) | 13 | 🟡 | Makefile |
| [EarthBound disassembly](https://github.com/Yoshifanatic1/EarthBound-Disassembly) | Disassembly of EarthBound (SNES) | 13 | 🔴 | Assembly |
| [Kirby Super Star disassembly](https://github.com/Ankouno/KSS-disassembly) | Disassembly of Kirby Super Star (SNES) | 13 | 🔴 | Assembly |
| [BS Zelda no Densetsu disassembly](https://github.com/Yoshifanatic1/BS-Zelda-no-Densetsu-Disassembly) | Disassembly of BS Zelda no Densetsu (Satellaview) | 12 | 🔴 | Assembly |
| [International Superstar Soccer Deluxe disassembly](https://github.com/Yoshifanatic1/International-Superstar-Soccer-Deluxe-SNES-Disassembly) | Disassembly of International Superstar Soccer Deluxe (SNES) | 12 | 🔴 | Assembly |
| [Milon's Secret Castle disassembly](https://github.com/jasonmray/MilonsSecretCastle) | Reverse-engineered disassembly of Milon's Secret Castle (NES) | 12 | 🟢 | Assembly |
| [Super Mario World 2: Yoshi's Island disassembly](https://github.com/Yoshifanatic1/Yoshi-s-Island-Disassembly) | Disassembly of Super Mario World 2: Yoshi's Island (SNES) | 12 | 🔴 | Assembly |
| [Battle City](https://github.com/vgrichina/battlecity) | Disassembly of Battle City (NES, 1985) | 11 | 🟢 | JavaScript |
| [Goof Troop disassembly](https://github.com/Yoshifanatic1/Goof-Troop-Disassembly) | Disassembly of Goof Troop (SNES) | 10 | 🔴 | Assembly |
| [Jurassic Park disassembly](https://github.com/Yoshifanatic1/Jurassic-Park-1-SNES-disassembly) | Disassembly of Jurassic Park (SNES) | 10 | 🔴 | Assembly |
| [Star Fox SPC sound driver disassembly](https://github.com/phonymike/starfox_spc_driver) | Disassembly of the Star Fox SPC sound driver (SNES) | 10 | 🟢 | Assembly |
| [Final Fantasy II disassembly](https://github.com/JiggeryPonkery/FF2-Disassembly) | Disassembly of Final Fantasy II (Famicom) | 9 | 🔴 | Assembly |
| [Mario Paint disassembly](https://github.com/Yoshifanatic1/Mario-Paint-Disassembly) | Disassembly of Mario Paint (SNES) | 9 | 🔴 | Assembly |
| [Mega Man X disassembly](https://github.com/MarkAlarm/MMX1-Disassembly) | Disassembly of Mega Man X (SNES) | 9 | 🔴 | Assembly |
| [Atlantis no Nazo disassembly](https://github.com/Xkeeper0/atlantis-no-nazo) | Disassembly of Atlantis no Nazo (Famicom, Sunsoft) | 8 | 🟡 | Assembly |
| [EarthBound Beginnings](https://github.com/GrasonHumphrey/Earthbound-Zero-Decomp) | Ghidra decompilation of EarthBound Beginnings / Mother (NES, 1989) | 8 | 🟡 | HTML |
| [Earthworm Jim 2 disassembly](https://github.com/Yoshifanatic1/Earthworm-Jim-2-Disassembly) | Disassembly of Earthworm Jim 2 (SNES) | 8 | 🔴 | Assembly |
| [The Legend of Zelda: A Link to the Past disassembly](https://github.com/JaredBrian/AsarUSALTTPDisassembly) | Disassembly of The Legend of Zelda: A Link to the Past (SNES, US) | 8 | 🟢 | Assembly |
| [unlicensed Waixing BioHazard decomp](https://github.com/nikita600/BioHazard_NES) | Decompilation of the unlicensed Waixing BioHazard for NES | 8 | 🔴 | Assembly |
| [Arcana disassembly](https://github.com/SarahShinespark/arcana-disassembly) | Disassembly of Arcana (SNES) | 7 | 🟢 | Assembly |
| [ffmq-info](https://github.com/TheAnsarya/ffmq-info) | Disassembly and information for Final Fantasy: Mystic Quest (SNES) | 7 | 🟢 | Assembly |
| [Hong Kong 97 disassembly](https://github.com/ItsT3K/Hong-Kong-97-Disassembly) | Disassembly of Hong Kong 97 (SNES) | 7 | 🔴 | Assembly |
| [Kirby's Dream Land 3 Disassembly](https://github.com/Yoshifanatic1/Kirbys-Dream-Land-3-Disassembly) | Disassembly of Kirby's Dream Land 3 (Assembly) | 7 | 🔴 | Assembly |
| [Ultima 3 Disassembly](https://github.com/nmikstas/nes_ultima_3_disassembly) | Disassembly of the nes version of Ultima Exodus | 7 | 🔴 | Assembly |
| [unlicensed Street Fighter III disassembly](https://github.com/cyneprepou4uk/Street-Fighter-3) | Disassembly of the unlicensed Street Fighter III (9 Fighter) for NES | 7 | 🔴 | Assembly |
| [Wario's Woods disassembly](https://github.com/Yoshifanatic1/Wario-s-Woods-SNES-Disassembly) | Disassembly of Wario's Woods (SNES) | 7 | 🔴 | Assembly |
| [Mega Man 2 disassembly](https://github.com/lsmmega/mm2) | Disassembly of Mega Man 2 (NES) | 6 | 🟢 | Assembly |
| [Mega Man disassembly](https://github.com/lsmmega/mm1) | Disassembly of Mega Man (NES) | 6 | 🟢 | Assembly |
| [mm4](https://github.com/captainsouthbird/mm4) | Disassembly of Mega Man 4 | 6 | 🔴 | Assembly |
| [Ms. Pac-Man NES Tengen Disassembly](https://github.com/RussianManSMWC/Ms.-Pac-Man-NES-Tengen-Disassembly) | A disassembly of Ms. Pac-Man for NES, Tengen version. | 6 | 🟢 | Assembly |
| [Plok disassembly](https://github.com/Yoshifanatic1/Plok-Disassembly) | Disassembly of Plok (SNES) | 6 | 🔴 | Assembly |
| [SimCity (SNES) Disassembly](https://github.com/Yoshifanatic1/SimCity-SNES-Disassembly) | Disassembly of SimCity (Assembly) | 6 | 🔴 | Assembly |
| [TMNT IV: Turtles in Time disassembly](https://github.com/Yoshifanatic1/TMNT-IV---Turtles-In-Time-SNES-Disassembly) | Disassembly of TMNT IV: Turtles in Time (SNES) | 6 | 🟡 | Assembly |
| [unreleased SNES version of Puggsy disassembly](https://github.com/zestydevy/puggsy-disassembly) | Rebuildable disassembly of the unreleased SNES version of Puggsy | 6 | 🔴 | Assembly |
| [Contra disassembly](https://github.com/ZReC/contraj-disasm) | Disassembly of Contra (NES, Japan) | 5 | 🔴 | Assembly |
| [dizProjects](https://github.com/bogaa/dizProjects) | Disassembly projects of commercial SNES and NES games made with DiztinGUIsh | 5 | 🟢 | Assembly |
| [Donkey Kong Country 3 disassembly](https://github.com/BlueImp78/DKC3-Disassembly) | Disassembly of Donkey Kong Country 3 (SNES) | 5 | 🟢 | Assembly |
| [Faceball 2000 disassembly](https://github.com/Yoshifanatic1/Faceball-2000-Disassembly) | Disassembly of Faceball 2000 (SNES) | 5 | 🔴 | Assembly |
| [Mighty Bomb Jack disassembly](https://github.com/Xkeeper0/mighty-bomb-jack) | Disassembly of Mighty Bomb Jack (NES) | 5 | 🟡 | Assembly |
| [Ms. Pac-Man (SNES) Disassembly](https://github.com/Yoshifanatic1/Ms-Pac-Man-SNES-Disassembly) | Disassembly of Ms. Pac-Man (Assembly) | 5 | 🔴 | Assembly |
| [Super Punch-Out!! disassembly](https://github.com/Yoshifanatic1/Super-Punch-Out-Disassembly) | Disassembly of Super Punch-Out!! (SNES) | 5 | 🔴 | Assembly |
| [Castlevania III: Dracula's Curse disassembly](https://github.com/vinheim3/castlevania3-disasm) | Disassembly of Castlevania III: Dracula's Curse (NES) | 4 | 🔴 | Assembly |
| [Chrono Trigger disassembly](https://github.com/dscotton/ct_disassembly) | 65816 disassembly of Chrono Trigger (SNES) | 4 | 🟢 | Assembly |
| [Godzilla: Monster of Monsters disassembly](https://github.com/Nintorch/GMoM-disassembly) | Disassembly of Godzilla: Monster of Monsters (NES) | 4 | 🟡 | Assembly |
| [Kirby's Adventure disassembly](https://github.com/yay58/Kirby-s-Adventure-Disassembly) | Disassembly of Kirby's Adventure (NES) | 4 | 🟡 | Assembly |
| [Legacy of the Wizard disassembly](https://github.com/seufet/Legacy-of-the-Wizard-Disassembly) | Complete disassembly of Legacy of the Wizard (NES) | 4 | 🟢 | Assembly |
| [Mega Man 2 disassembly](https://github.com/plasticsmoke/megaman2-disassembly-ca65) | Annotated ca65 disassembly of Mega Man 2 (NES) | 4 | 🟢 | Assembly |
| [Pac-Man 2: The New Adventures disassembly](https://github.com/Yoshifanatic1/Pac-Man-2-The-New-Adventures-SNES-Disassembly) | Disassembly of Pac-Man 2: The New Adventures (SNES) | 4 | 🔴 | Assembly |
| [Pocky & Rocky 2 disassembly](https://github.com/spannerisms/pr2dasm) | Disassembly of Pocky & Rocky 2 (SNES, USA) | 4 | 🟡 | Assembly |
| [Speedy Gonzales: Los Gatos Banditos Disassembly](https://github.com/Yoshifanatic1/Speedy-Gonzales-Los-Gatos-Banditos-Disassembly) | Disassembly of Speedy Gonzales: Los Gatos Bandidos (Assembly) | 4 | 🔴 | Assembly |
| [TFRom-Recreation](https://github.com/Fixatron/TFRom-Recreation) | Source recreation of Transformers: Mystery of Convoy (Famicom) | 4 | 🟢 | Assembly |
| [dragon-warrior-4-info](https://github.com/TheAnsarya/dragon-warrior-4-info) | Disassembly and asset extraction for Dragon Warrior IV (NES, US) | 3 | 🟢 | Assembly |
| [Duck Hunt Disassembly](https://github.com/RussianManSMWC/Duck-ssembly-Hunt) | A disassembly of Duck Hunt for the NES. | 3 | 🟡 | Assembly |
| [Fire Emblem: Genealogy of the Holy War disassembly](https://github.com/ulti-mage/FireEmblem4) | Partial disassembly of Fire Emblem: Genealogy of the Holy War (Super Famicom) | 3 | 🟢 | Assembly |
| [Fire Emblem: Mystery of the Emblem disassembly](https://github.com/minirop/fe3) | Disassembly of Fire Emblem: Mystery of the Emblem (Super Famicom) | 3 | 🟢 | Assembly |
| [Ganbare Goemon 3 disassembly](https://github.com/gocha/sfc-goemon-3-disassembly) | Disassembly of Ganbare Goemon 3 (Super Famicom, Konami, 1994) | 3 | 🟢 | Assembly |
| [J.R.R. Tolkien's The Lord of the Rings: Volume 1 disassembly](https://github.com/patrickmollohan/lotr-snes-disassembly) | Disassembly of J.R.R. Tolkien's The Lord of the Rings: Volume 1 (SNES) | 3 | 🟡 | Assembly |
| [Mega Man X3 disassembly](https://github.com/vinheim3/megaManX3-disasm) | Disassembly of Mega Man X3 (SNES) | 3 | 🔴 | Assembly |
| [Monster in My Pocket disassembly](https://github.com/Yoshimaster96/monster-disasm) | Disassembly of Monster in My Pocket (NES) | 3 | 🟢 | Assembly |
| [Ms. Pac-Man NES Namco Disassembly](https://github.com/RussianManSMWC/Ms.-Pac-Man-NES-Namco-Disassembly) | A disassembly of Ms. Pac-Man for NES, Namco/Now Production version. | 3 | 🟡 | Assembly |
| [Rise of the Robots disassembly](https://github.com/Yoshifanatic1/Rise-Of-The-Robots-SNES-Disassembly) | Disassembly of Rise of the Robots (SNES) | 3 | 🟡 | Assembly |
| [SNES games including Demon's Crest disassembly](https://github.com/FredYeye/various-game-disassembly) | Disassemblies of SNES games including Demon's Crest | 3 | 🟡 | Assembly |
| [Stunt Race FX decomp](https://github.com/jeff-strutb/stuntracefx) | Byte-exact decompilation of Stunt Race FX (SNES) | 3 | 🟢 | C |
| [Super Mario All-Stars disassembly](https://github.com/bonimy/SMAS-Disassembly) | Disassembly of Super Mario All-Stars (SNES) | 3 | 🔴 | Assembly |
| [Super Mario Bros. All Night Nippon disassembly](https://github.com/threecreepio/smbann-disassembly) | Disassembly of Super Mario Bros. All Night Nippon (Famicom Disk System) | 3 | 🔴 | Assembly |
| [Zanac decomp](https://github.com/ogamespec/zanac) | Decompilation of Zanac (Famicom) | 3 | 🟢 | C |
| [Blaster Master disassembly](https://github.com/MetaFight/blaster-master-disasm-public) | Disassembly of Blaster Master (NES, US) | 2 | 🟢 | Assembly |
| [Bubble Bobble Part 2 disassembly](https://github.com/bobschneeder45/Bubble-Bobble-2-NES-Disassembly) | Disassembly of Bubble Bobble Part 2 (NES, US and JP) | 2 | 🟢 | Assembly |
| [Donkey Kong Country disassembly](https://github.com/DKC-Recomp/DKC-disassembly) | Reverse engineering and disassembly of Donkey Kong Country (SNES) | 2 | 🟢 | Assembly |
| [Final Fantasy disassembly](https://github.com/daegiM/NES-disassembly-final-fantasy-1) | Disassembly of Final Fantasy (NES) | 2 | 🔴 | Assembly |
| [Fire Emblem Gaiden disassembly](https://github.com/minirop/fe2) | Disassembly of Fire Emblem Gaiden (Famicom) | 2 | 🟢 | Assembly |
| [Frogger disassembly](https://github.com/Yoshifanatic1/Frogger-SNES-Disassembly) | Disassembly of Frogger (SNES) | 2 | 🔴 | Assembly |
| [Harvest Moon decomp](https://github.com/dzik87/HarvestMoonSNES) | Decompiled source of Harvest Moon (SNES, US) | 2 | 🟢 | Assembly |
| [Japanese Gimmick! disassembly](https://github.com/LucianoTheWindowsFan/gimmick) | Disassembly of the Japanese Gimmick! (Famicom) | 2 | 🔴 | Assembly |
| [Legacy of the Wizard disassembly](https://github.com/threecreepio/lotw-disassembly) | Disassembly of Legacy of the Wizard (NES) | 2 | 🟢 | Assembly |
| [Mega Man 3 disassembly](https://github.com/lsmmega/mm3) | Disassembly of Mega Man 3 (NES) | 2 | 🟢 | Assembly |
| [Mega Man 3 disassembly](https://github.com/plasticsmoke/megaman3-disassembly-ca65) | Annotated ca65 disassembly of Mega Man 3 (NES) | 2 | 🟢 | Assembly |
| [Mega Man 5 disassembly](https://github.com/lsmmega/mm5) | Disassembly of Mega Man 5 (NES) | 2 | 🟢 | Assembly |
| [Solomon's Key decomp](https://github.com/RetrolariumLab/solomon_no_kagi_src) | Byte-identical ca65 source reconstruction of Solomon's Key (NES, US and Europe) | 2 | 🟢 | Assembly |
| [Spider-Man & the X-Men in Arcade's Revenge (SNES) Disassembly](https://github.com/Yoshifanatic1/Spider-Man-X-Men-Arcades-Revenge-SNES-Disassembly) | Disassembly of Spider-Man and the X-Men in Arcade's Revenge (Assembly) | 2 | 🔴 | Assembly |
| [Super Mario Brothers High Level Disassembly](https://github.com/NexusEast/Console_Development) | My attempt to develop every single console i can | 2 | 🔴 | Assembly |
| [The Goonies disassembly](https://github.com/MikeWuPing/disasm_Goonies) | Complete disassembly of The Goonies (Famicom, Konami 1986) | 2 | 🟢 | Assembly |
| [Williams Arcade's Greatest Hits disassembly](https://github.com/Yoshifanatic1/Williams-Arcades-Greatest-Hits-Disassembly) | Disassembly of Williams Arcade's Greatest Hits (SNES) | 2 | 🔴 | Assembly |
| [Breath of Fire disassembly](https://github.com/vinheim3/bof-disasm) | Disassembly of Breath of Fire (SNES) | 1 | 🔴 | Assembly |
| [Bucky O'Hare disassembly](https://github.com/Yoshimaster96/bucky-disasm) | Disassembly of Bucky O'Hare (NES) | 1 | 🟢 | Assembly |
| [Castle Excellent and Castlequest decomp](https://github.com/RetrolariumLab/castle_excellent_src) | Byte-identical source reconstruction of Castle Excellent and Castlequest (Famicom/NES) | 1 | 🟢 | Assembly |
| [Doraemon decomp](https://github.com/RetrolariumLab/doraemon_src) | Byte-identical ca65 source reconstruction of Doraemon (Famicom) | 1 | 🟢 | Assembly |
| [Dragon Ball Z: Super Saiya Densetsu decomp](https://github.com/Paint-The-Night/dbz-super-saiya-densetsu-native) | C reconstruction and native port research for Dragon Ball Z: Super Saiya Densetsu (Super Famicom) | 1 | 🟢 | C++ |
| [Dragon Warrior II disassembly](https://github.com/Nathan-R-Og/dq2) | Disassembly of Dragon Warrior II (NES) | 1 | 🟢 | Assembly |
| [Dragon Warrior IV disassembly](https://github.com/JEschete/DW4_Disassembly) | Disassembly of Dragon Warrior IV (NES) | 1 | 🟢 | Assembly |
| [Duck Hunt disassembly](https://github.com/jpeisach/DuckHuntDisassembly) | Disassembly of Duck Hunt (NES, 1984) | 1 | 🔴 | Assembly |
| [Family Feud disassembly](https://github.com/threecreepio/nes-familyfeud) | Disassembly of Family Feud (NES) | 1 | 🟡 | Assembly |
| [Japanese Super Mario Bros. disassembly](https://github.com/threecreepio/smb1j-disassembly) | Disassembly of the Japanese Super Mario Bros. (Famicom) | 1 | 🟢 | Assembly |
| [Kirby Super Star disassembly](https://github.com/yay58/Kirby-Super-Star-Kirby-Fun-Pak-Disassembly) | Disassembly of Kirby Super Star (SNES) | 1 | 🟡 | Assembly |
| [Kirby's Adventure disassembly](https://github.com/Nathan-R-Og/kirbyadventure) | Disassembly of Kirby's Adventure (NES, USA) | 1 | 🟢 | Assembly |
| [Lester the Unlikely disassembly](https://github.com/Yoshifanatic1/Lester-The-Unlikely-Disassembly) | Disassembly of Lester the Unlikely (SNES) | 1 | 🔴 | Assembly |
| [Lufia II: Rise of the Sinistrals disassembly](https://github.com/vinheim3/lufia2-disasm) | Disassembly of Lufia II: Rise of the Sinistrals (SNES) | 1 | 🔴 | Assembly |
| [Mega Man 4 disassembly](https://github.com/lsmmega/mm4) | Disassembly of Mega Man 4 (NES) | 1 | 🟢 | Assembly |
| [Mega Man 4 disassembly](https://github.com/plasticsmoke/megaman4-disassembly-ca65) | Annotated ca65 disassembly of Mega Man 4 (NES) | 1 | 🟢 | Assembly |
| [Mega Man 6 disassembly](https://github.com/lsmmega/mm6) | Disassembly of Mega Man 6 (NES) | 1 | 🟢 | Assembly |
| [Mega Man disassembly](https://github.com/plasticsmoke/megaman1-disassembly-ca65) | Annotated ca65 disassembly of Mega Man (NES) | 1 | 🟢 | Assembly |
| [Milon's Secret Castle disassembly](https://github.com/spannerisms/milondasm) | Annotated disassembly of Milon's Secret Castle (NES) | 1 | 🟡 | Assembly |
| [Ninja Gaiden disassembly](https://github.com/0xe1f/NinjaGaidenNES) | Disassembly of Ninja Gaiden (NES) | 1 | 🟢 | Assembly |
| [Ninja Gaiden II disassembly](https://github.com/benolee/ninja-gaiden-ii-disassembly) | Disassembly of Ninja Gaiden II (NES) | 1 | 🔴 | Assembly |
| [Pinball disassembly](https://github.com/rbmichael/pinball_nes_disassembly) | Disassembly of Pinball (NES) | 1 | 🟢 | Assembly |
| [Pocky & Rocky disassembly](https://github.com/gewballs/pocky) | Disassembly of Pocky & Rocky (SNES) | 1 | 🔴 | Assembly |
| [Pro Wrestling disassembly](https://github.com/rbmichael/pro_wrestling_nes_disassembly) | Disassembly of Pro Wrestling (NES) | 1 | 🟢 | Assembly |
| [Radia Senki: Reimeihen disassembly](https://github.com/relic374/radia-senki) | Disassembly of Radia Senki: Reimeihen (NES) | 1 | 🟡 | Assembly |
| [Rare's unreleased Dream disassembly](https://github.com/H4v0c21/Dream-disassembly) | Disassembly of Rare's unreleased Dream (SNES) | 1 | 🟢 | Assembly |
| [seven Super Mario Bros. releases decomp](https://github.com/RetrolariumLab/smb1_src) | Byte-identical ca65 source reconstruction of seven Super Mario Bros. releases (NES) | 1 | 🟢 | Assembly |
| [StarTropics disassembly](https://github.com/jogalleciez/StarTropics-decomp) | Labelled ca65 disassembly of StarTropics (NES) that rebuilds the original ROM | 1 | 🟢 | Assembly |
| [Super Metroid disassembly](https://github.com/thijsrijkers/super_metroid_disassembly) | Disassembly of Super Metroid (SNES) | 1 | 🔴 | Assembly |
| [Super Pitfall disassembly](https://github.com/rbmichael/super_pitfall_nes_disassembly) | Disassembly of Super Pitfall (NES, USA) | 1 | 🟢 | Assembly |
| [Thexder disassembly](https://github.com/Xkeeper0/thexder) | Disassembly of Thexder (NES/Famicom) | 1 | 🔴 | PHP |
| [Willow disassembly](https://github.com/vinheim3/willow-disasm) | Disassembly of Willow (NES) | 1 | 🔴 | Assembly |
| [Ys disassembly](https://github.com/daegiM/NES-disassembly-ys-1) | Disassembly of Ys (NES) | 1 | 🔴 | Assembly |
| [Ys II disassembly](https://github.com/daegiM/NES-disassembly-ys-2) | Disassembly of Ys II (NES) | 1 | 🔴 | Assembly |
| [doki](https://gitlab.com/segaloco/doki) | Comprehensive disassembly of Yume Kojo: Doki Doki Panic (Famicom Disk System) |  | ⚪ |  |
| [dq1disasm](https://gitlab.com/segaloco/dq1disasm) | Comprehensive disassembly of Dragon Quest 1 for the Famicom |  | ⚪ |  |
| [Dream: Land of Giants disassembly](https://github.com/nathanialf/dream) | Disassembly of Dream: Land of Giants (unreleased SNES prototype, Rare, 1995) | 0 | 🟢 | C |
| [fc_dk](https://gitlab.com/segaloco/fc_dk) | Comprehensive disassembly of Donkey Kong for the Famicom |  | ⚪ |  |
| [fdsboot](https://gitlab.com/segaloco/fdsboot) | 6502 disassembly of the Famicom Disk System boot ROM |  | ⚪ |  |
| [Ganbare Goemon Kirakira Douchuu disassembly](https://github.com/gocha/sfc-goemon-4-disassembly) | Disassembly of Ganbare Goemon Kirakira Douchuu (Super Famicom, Konami, 1995) | 0 | 🟢 | Assembly |
| [Lufia II: Rise of the Sinistrals decomp](https://github.com/Cellenseres/Lufia2Decomp) | Decompilation of Lufia II: Rise of the Sinistrals (SNES) | 0 | 🟢 | C |
| [seven Pac-Man NES revisions decomp](https://github.com/RetrolariumLab/pacman_src) | Byte-identical ca65 source reconstruction of seven Pac-Man NES revisions | 0 | 🟢 | Assembly |
| [smb](https://gitlab.com/segaloco/smb) | Disassembly combining multiple 8-bit versions of Super Mario Bros. |  | ⚪ |  |
| [smb3](https://gitlab.com/segaloco/smb3) | Disassembly of Super Mario Bros. 3 for the Famicom/NES |  | ⚪ |  |
| [Super Mario Bros. 2 disassembly](https://github.com/vinheim3/smb2j-disasm) | Disassembly of Super Mario Bros. 2 (Famicom Disk System, Japan) | 0 | 🔴 | Assembly |
| [Ufouria: The Saga disassembly](https://github.com/vinheim3/ufouria-disasm) | Disassembly of Ufouria: The Saga (NES) | 0 | 🔴 | Assembly |
| [zel2](https://gitlab.com/segaloco/zel2) | Disassembly of Zelda II: The Adventure of Link |  | ⚪ |  |

## Matching Decompilations — Sega

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [s1disasm](https://github.com/sonicretro/s1disasm) | Sonic 1 Disassembly | 456 | 🟢 | Assembly |
| [s2disasm](https://github.com/sonicretro/s2disasm) | Sonic 2 Disassembly | 320 | 🟢 | Assembly |
| [Sonic 3/Sonic & Knuckles Disassembly](https://github.com/sonicretro/skdisasm) | Sonic and Knuckles Disassembly | 265 | 🟢 | Assembly |
| [Sonic-Clean-Engine-S.C.E.-](https://github.com/TheBlad768/Sonic-Clean-Engine-S.C.E.-) | Cleaned-up engine based on the Sonic 3 & Knuckles disassembly (Mega Drive) | 62 | 🟢 | Assembly |
| [s2smsdisasm](https://github.com/sonicretro/s2smsdisasm) | Sonic 2 SMS Disassembly | 60 | 🔴 | Assembly |
| [Sonic the Hedgehog disassembly](https://github.com/cvghivebrain/s1disasm) | Hivebrain 2022 disassembly of Sonic the Hedgehog (Mega Drive) | 49 | 🟡 | Assembly |
| [unreleased Half-Life port decomp](https://github.com/maximqaxd/halflife_dc) | Reverse engineering of the unreleased Half-Life port for Sega Dreamcast | 48 | 🟢 | C |
| [Kid Chameleon disassembly](https://github.com/sonicretro/kid-chameleon-disasm) | Split disassembly of Kid Chameleon (Mega Drive) | 43 | 🟢 | Assembly |
| [Knuckles' Chaotix Disassembly](https://github.com/sonicretro/chaotix) | Knuckles' Chaotix Disassembly & Toolkit | 41 | 🟢 | Assembly |
| [spindisasm](https://github.com/sonicretro/spindisasm) | Sonic Spinball Disassembly | 41 | 🔴 | Assembly |
| [Resident Evil – Code: Veronica (Dreamcast)](https://github.com/fmil95/recv-dc-decomp) | Decompilation of Resident Evil – Code: Veronica (Dreamcast) | 40 | 🟢 | C |
| [Neon Genesis Evangelion 64](https://github.com/farisawan-2000/evangelion) | Decompilation of Neon Genesis Evangelion 64 | 38 | 🟡 | C |
| [Tokyo Bus Guide](https://github.com/lhsazevedo/tbg-decomp) | Matching decompilation of Tokyo Bus Guide (Dreamcast, 1999) | 36 | 🟢 | PHP |
| [Ristar disassembly](https://github.com/sonicretro/ristar) | Disassembly of Ristar (Mega Drive) | 34 | 🔴 | Assembly |
| [s3ddisasm](https://github.com/sonicretro/s3ddisasm) | Sonic 3D Blast Disassembly | 31 | 🔴 | Assembly |
| [Panzer Dragoon Saga decomp](https://github.com/Aeonitis/Reverse-Engineer-Azel) | Reverse engineering and decompilation of Panzer Dragoon Saga (Sega Saturn) | 30 | 🔴 | Assembly |
| [released Sonic the Hedgehog prototype disassembly](https://github.com/Mega-Drive-Developers-Collective/Sonic-1-Prototype) | Research disassembly of the released Sonic the Hedgehog prototype (Mega Drive) | 29 | 🔴 | Assembly |
| [Alex Kidd in Miracle World disassembly](https://github.com/lhsazevedo/akmw) | Disassembly of Alex Kidd in Miracle World (Sega Master System) | 27 | 🟢 | Assembly |
| [Sonic Adventure disassembly](https://github.com/sonicretro/sad_disasm) | Disassembly of Sonic Adventure (Dreamcast) | 26 | 🔴 |  |
| [Sonic CD Disassembly](https://github.com/sonicretro/scddisasm) | Disassembly of Sonic CD (Assembly) | 21 | 🟢 | Assembly |
| [Sonic-Clean-Engine-S.C.E.-Extended-](https://github.com/TheBlad768/Sonic-Clean-Engine-S.C.E.-Extended-) | Extended Sonic Clean Engine based on the Sonic 3 & Knuckles disassembly (Mega Drive) | 21 | 🟢 | Assembly |
| [Simon Wai prototype of Sonic the Hedgehog 2 disassembly](https://github.com/AlexField442/Sonic-2-Simon-Wai-Disassembly) | Disassembly of the Simon Wai prototype of Sonic the Hedgehog 2 (Mega Drive) | 17 | 🗄️ | Assembly |
| [Puyo Puyo disassembly](https://github.com/Nasina7/puyodisasm) | Disassembly of Puyo Puyo (Mega Drive) | 16 | 🟢 | Assembly |
| [Sonic the Hedgehog 2 targeting ASM68K disassembly](https://github.com/OrionNavattan/Sonic-2-ASM68K) | Disassembly of Sonic the Hedgehog 2 targeting ASM68K (Mega Drive) | 15 | 🟢 | Assembly |
| [QuackShot Starring Donald Duck decomp](https://github.com/lab313ru/quackshot_src) | Reassemblable source of QuackShot Starring Donald Duck (Mega Drive) | 14 | 🔴 | Assembly |
| [Sonic the Hedgehog prototype disassembly](https://github.com/Filter011/s1-proto-disasm) | Split disassembly of the Sonic the Hedgehog prototype (Mega Drive) | 14 | 🟢 | Assembly |
| [Sonic the Hedgehog disassembly](https://github.com/TheRavenfreak/Sonic-1-Game-Gear-Disassembly) | Split disassembly of Sonic the Hedgehog (Game Gear) | 13 | 🔴 | Assembly |
| [ToeJam & Earl disassembly](https://github.com/bstreiff/tje-disasm) | Disassembly of ToeJam & Earl (Mega Drive) | 12 | 🔴 | Assembly |
| [Landstalker disassembly](https://github.com/lordmir/landstalker_disasm) | Disassembly of Landstalker (Mega Drive) | 11 | 🟢 | Assembly |
| [Sonic the Hedgehog 2 Nick Arcade prototype disassembly](https://github.com/AlexField442/Sonic-2-Nick-Arcade-Disassembly) | Disassembly of the Sonic the Hedgehog 2 Nick Arcade prototype (Mega Drive) | 11 | 🟢 | Assembly |
| [Virtua Fighter 2 v2.1 decomp](https://github.com/celsowm/vf2-decomp) | Clean-room C decompilation of Virtua Fighter 2 v2.1 (Sega Saturn) | 10 | 🟢 | C |
| [Dragon Crystal disassembly](https://github.com/trykaar/dc-sms-dasm) | Disassembly of Dragon Crystal (Sega Master System) | 9 | 🔴 | Assembly |
| [Panzer Dragoon Saga reimplementation](https://github.com/blythos/pds-tools) | Decompilation and modern reimplementation of Panzer Dragoon Saga (Sega Saturn) | 9 | 🟢 | Python |
| [nhl94-disassembly](https://github.com/Chaos81/nhl94-disassembly) | Attempt to reverse engineer the disassembled ROM of NHL94 using the NHL Hockey source code | 8 | 🟢 | Assembly |
| [November 1993 Sonic 3 prototype disassembly](https://github.com/Awuwunya/Sonic-3-93-Nov-03) | Split disassembly of the November 1993 Sonic 3 prototype (Mega Drive) | 8 | 🔴 | Assembly |
| [Puyo Puyo disassembly](https://github.com/Scrambled-Beans/puyo1-md-translation) | Partial disassembly of Puyo Puyo (Mega Drive) for translation | 8 | 🟢 | Assembly |
| [Alien Soldier decomp](https://github.com/RetrolariumLab/alien_soldier_src) | Byte-identical source reconstruction of Alien Soldier (Mega Drive) | 7 | 🟢 | Assembly |
| [Flicky-Disassembly](https://github.com/Dandaman955/Flicky-Disassembly) | Disassembly of Flicky on the Mega Drive. | 7 | 🔴 | Assembly |
| [Sonic the Hedgehog 2 August 21st prototype disassembly](https://github.com/Clownacy/Sonic-2-Aug-21st-Disassembly) | Disassembly of the Sonic the Hedgehog 2 August 21st prototype (Mega Drive) | 7 | 🟡 | Assembly |
| [Sonic the Hedgehog disassembly](https://github.com/JarrettBillingsley/DecompilingSonic1) | Decompilation of Sonic the Hedgehog (Mega Drive) from its disassembly into C++ | 7 | 🔴 | C++ |
| [December 2020 Sonic the Hedgehog prototype disassembly](https://github.com/Iso-Kilo/Sonic-1-Prototype-Disassembly) | Split disassembly of the December 2020 Sonic the Hedgehog prototype (Mega Drive) | 6 | 🔴 |  |
| [Earthworm Jim disassembly](https://github.com/anatsvit/erathworm-jim-disasm) | Disassembly of Earthworm Jim (Sega Genesis) | 6 | 🟢 | Assembly |
| [Landstalker disassembly](https://github.com/LandstalkerCentral/LSUSDISASM) | Disassembly of Landstalker (Mega Drive, US) | 6 | 🔴 | Assembly |
| [Phantasy Star IV Disassembly](https://github.com/squidfeatures/ps4disasm) | Phantasy Star IV Disassembly | 6 | 🔴 | Assembly |
| [Crazy Taxi decomp](https://github.com/consolesplayingconsoles/crazy-taxi-decomp) | Decompilation of Crazy Taxi (Sega Dreamcast) | 5 | 🟢 | C |
| [Dr. Robotnik's Mean Bean Machine disassembly](https://github.com/Scrambled-Beans/drmbm-md-disasm) | Disassembly of Dr. Robotnik's Mean Bean Machine (Mega Drive) | 5 | 🟢 | Assembly |
| [Dr. Robotnik's Mean Bean Machine disassembly](https://github.com/DevsArchive/mean-bean-machine-disassembly) | Disassembly of Dr. Robotnik's Mean Bean Machine (Mega Drive) | 5 | 🗄️ | Assembly |
| [Lord of the Sword disassembly](https://github.com/Isotarge/lotsdisasm) | Disassembly of Lord of the Sword (Sega Master System) | 5 | 🔴 | Assembly |
| [Puyo Puyo Tsuu disassembly](https://github.com/Nasina7/puyo2disasm) | Disassembly of Puyo Puyo Tsuu (Mega Drive) | 5 | 🟡 | Assembly |
| [Streets of Rage disassembly](https://github.com/Dandaman955/Streets-of-Rage-1-Disassembly-Redux) | Disassembly of Streets of Rage (Mega Drive) | 5 | 🔴 | Assembly |
| [Altered Beast disassembly](https://github.com/hansbonini/smd_alteredbeast) | Disassembly of Altered Beast (Sega Genesis) | 4 | 🟡 | GLSL |
| [Columns disassembly](https://github.com/lhsazevedo/columns) | Disassembly of Columns (Sega Master System) | 4 | 🔴 | Assembly |
| [Sonic the Hedgehog 2 in the style of s1disasm disassembly](https://github.com/RetroKoH/s2disasm-split) | Split disassembly of Sonic the Hedgehog 2 in the style of s1disasm (Mega Drive) | 4 | 🟡 | Assembly |
| [Sonic the Hedgehog disassembly](https://github.com/iamgreaser/s1smsdisasm-gm) | Disassembly of Sonic the Hedgehog (Sega Master System) | 4 | 🟢 | Assembly |
| [Virtua Fighter 3tb decomp](https://github.com/celsowm/vf3-decomp) | Clean-room C source of Virtua Fighter 3tb (Sega Dreamcast) | 4 | 🟢 | C |
| [Kraftwerk prototype of Dr. Robotnik's Mean Bean Machine disassembly](https://github.com/Rose-Group/kraftwerkdisasm) | Disassembly of the Kraftwerk prototype of Dr. Robotnik's Mean Bean Machine (Mega Drive) | 3 | 🟢 | Assembly |
| [Panzer Dragoon Saga decomp](https://github.com/blythos/atolm) | Byte-matching decompilation of Panzer Dragoon Saga (Sega Saturn) | 3 | 🟢 | Python |
| [Phantasy Star Disassembly](https://github.com/sung3r/ps1disasm) | Phantasy Star Disassembly | 3 | 🔴 | Assembly |
| [Satellite 7 disassembly](https://github.com/lhsazevedo/satellite7) | Disassembly of Satellite 7 (Sega) | 3 | 🔴 | Assembly |
| [Super Monaco GP disassembly](https://github.com/RAMPKORV/smgp-disassembly) | Disassembly of Super Monaco GP (Mega Drive) | 3 | 🟢 | Assembly |
| [bootleg Super Mario 2 1998 decomp](https://github.com/Victor2i/sm21998decomp) | Decompilation of the bootleg Super Mario 2 1998 (Sega Mega Drive) | 2 | 🟢 | Assembly |
| [Flicky decomp](https://github.com/RetrolariumLab/flicky_src) | Byte-identical source reconstruction of Flicky (Mega Drive) | 2 | 🟢 | Assembly |
| [Pebble Beach Golf Links disassembly](https://github.com/JeremyPerbost/pebble-beach-golf-links-md-disasm) | Byte-perfect disassembly of Pebble Beach Golf Links (Mega Drive) | 2 | 🟢 | Assembly |
| [Phantasy Star III Disassembly](https://github.com/brecert/ps3disasm) | Phantasy Star III Disassembly | 2 | 🔴 | Assembly |
| [Phantasy Star Online Ver. 2 decomp](https://github.com/finalbillybong/pso_ver2_dc_decomp) | Decompilation of Phantasy Star Online Ver. 2 (Sega Dreamcast) | 2 | 🟢 | C |
| [Solomon's Key disassembly](https://github.com/Strugglemeat/solomonsms-disasm) | Disassembly of Solomon's Key (Sega Master System) | 2 | 🔴 | Assembly |
| [Sonic CD 0.02 prototype disassembly](https://github.com/Iso-Kilo/Dark-Wizard) | Disassembly of the Sonic CD 0.02 prototype (Sega CD) | 2 | 🔴 | Assembly |
| [Super Columns disassembly](https://github.com/Strugglemeat/supercolumnsgg-disasm) | Disassembly of Super Columns (Game Gear) | 2 | 🔴 | Assembly |
| [ToeJam & Earl decomp](https://github.com/mschienbein/toejam-earl-decomp) | Matching decompilation of ToeJam & Earl (Sega Genesis, 1991) | 2 | 🟢 | C |
| [Virtua Tennis decomp](https://github.com/consolesplayingconsoles/virtua-tennis-decomp) | Decompilation of Virtua Tennis (Sega Dreamcast) | 2 | 🟢 | C |
| [Alisia Dragoon disassembly](https://github.com/rgalland/alisia_dragoon_disassembly) | Complete disassembly of Alisia Dragoon (Mega Drive) | 1 | 🟢 | Assembly |
| [an August 21 Sonic 2 prototype disassembly](https://github.com/Filter011/s2-821-disasm) | Disassembly of an August 21 Sonic 2 prototype (Mega Drive) | 1 | 🟢 | Assembly |
| [Beyond Oasis disassembly](https://github.com/tylerphotos/beyondoasis-disasm) | Bit-perfect disassembly of Beyond Oasis (Genesis, US) | 1 | 🟢 | Assembly |
| [Chao Adventure 2 disassembly](https://github.com/Exant64/ChaoAdventure2) | Disassembly of Chao Adventure 2 (Dreamcast VMU) | 1 | 🔴 | Assembly |
| [Dragon Ball Z: Buyuu Retsuden disassembly](https://github.com/consolesplayingconsoles/dbzbr-disasm) | Disassembly of Dragon Ball Z: Buyuu Retsuden (Sega Mega Drive) | 1 | 🟢 | Python |
| [Dragon's Dream decomp](https://github.com/likeagfeld/DragonsDreamDecomp) | Decompilation of Dragon's Dream (Sega Saturn) | 1 | 🟢 | Python |
| [Knuckles' Chaotix disassembly](https://github.com/KatKuriN/incomplete_chaotix_disassembly) | Buildable partial disassembly of Knuckles' Chaotix (Sega 32X) | 1 | 🟡 | Assembly |
| [Marvel vs. Capcom 2 decomp](https://github.com/devin-thomas/mvc2-dc) | Matching decompilation of Marvel vs. Capcom 2 (Sega Dreamcast, NTSC-U) | 1 | 🟢 | Python |
| [Mega-Drive-Disassembly-Project](https://github.com/Dandaman955/Mega-Drive-Disassembly-Project) | Project to disassemble released Mega Drive games | 1 | 🔴 |  |
| [September 14 disassembly](https://github.com/desiresin/Sonic-2-9-14-92-Disassembly) | ASM68K disassembly of the September 14, 1992 Sonic 2 prototype (Mega Drive) | 1 | 🔴 | Assembly |
| [Shinobi Legions decomp](https://github.com/kazuyette/shino-legion-decomp) | Decompilation of Shinobi Legions (Sega Saturn) | 1 | 🟢 | C |
| [Sonic Adventure decomp](https://github.com/consolesplayingconsoles/sonic-adventure-decomp) | Decompilation of Sonic Adventure (Sega Dreamcast) | 1 | 🟢 | Python |
| [Sonic the Hedgehog disassembly](https://github.com/mdrubin/Sonic1-Z80-ASM) | Disassembly of Sonic the Hedgehog (Sega Master System) | 1 | 🔴 | Assembly |
| [Super Tennis disassembly](https://github.com/FlorianCassayre/sms-super-tennis) | Disassembly of Super Tennis (Sega Master System) | 1 | 🟢 | Assembly |
| [Toy Story disassembly](https://github.com/consolesplayingconsoles/toy-story-disasm) | Disassembly of Toy Story (Sega Mega Drive) | 1 | 🟢 | Python |
| [Twin Cobra disassembly](https://github.com/crapola/twin_cobra_disasm) | Disassembly of Twin Cobra (Sega Genesis) | 1 | 🟡 | Assembly |
| [Ultima IV decomp](https://github.com/alexdia25/u4-sms-recompiled) | Decompilation and recompilation of Ultima IV (Sega Master System) | 1 | 🟢 | C |
| [Wonder Boy in Monster World disassembly](https://github.com/RAMPKORV/wonderboy-in-monster-world-disassembly) | Disassembly of Wonder Boy in Monster World (Mega Drive) | 1 | 🟢 | Assembly |
| [X-Treme-Boss-Engine-Restoration](https://github.com/klattalytic-converter/X-Treme-Boss-Engine-Restoration) | Decompilation attempt of the leaked Sonic X-treme 718 build (Sega Saturn) | 1 | 🟢 | C |
| [Boku Doraemon decomp](https://github.com/consolesplayingconsoles/boku-doraemon-decomp) | Matching decompilation of Boku Doraemon (Sega Dreamcast) | 0 | 🟢 | Python |
| [dataeast_snddrv](https://codeberg.org/techmetx11/dataeast_snddrv) | Reverse-engineered source of Data East's Sega Mega Drive sound driver |  | ⚪ |  |
| [Golden-Axe-2-Disassembly](https://gitlab.com/paulmcquad/Golden-Axe-2-Disassembly) | Disassembly of Golden Axe II for the Mega Drive |  | ⚪ |  |
| [Guzzler disassembly](https://github.com/vinheim3/guzzler-disasm) | Disassembly of Guzzler (Sega SG-1000) | 0 | 🔴 | Assembly |
| [Hang-On decomp](https://github.com/xrip/hangon) | Byte-exact recompilation of Hang-On (Sega Master System) | 0 | 🟢 | Assembly |
| [Illbleed decomp](https://github.com/consolesplayingconsoles/illbleed-decomp) | Decompilation of Illbleed (Sega Dreamcast) | 0 | 🟢 | Python |
| [scd-disasm](https://gitlab.com/segaloco/scd-disasm) | Disassembly of Sonic CD for the Sega Mega CD |  | ⚪ |  |
| [Spy vs Spy decomp](https://github.com/xrip/spy-vs-spy) | Byte-exact recompilation of Spy vs Spy (Sega Master System) | 0 | 🟢 | Assembly |
| [Zombie Revenge decomp](https://github.com/consolesplayingconsoles/zombie-revenge-decomp) | Decompilation of Zombie Revenge (Sega Dreamcast) | 0 | 🟢 | Python |

## Matching Decompilations — Switch

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Breath of the Wild decomp](https://github.com/zeldaret/botw) | Decompilation of The Legend of Zelda: Breath of the Wild (Switch 1.5.0) | 2,370 | 🟢 | C++ |
| [Minecraft: Nintendo Switch Edition](https://github.com/GRAnimated/MinecraftLCE) | Decompilation of Minecraft: Nintendo Switch Edition | 624 | 🟢 | C++ |
| [Super Mario Odyssey](https://github.com/MonsterDruide1/OdysseyDecomp) | Matching decompilation of Super Mario Odyssey (Switch, 2017) | 487 | 🟢 | C++ |
| [sead](https://github.com/open-ead/sead) | Decompilation of sead, Nintendo's first-party C++ standard library | 254 | 🟢 | C++ |
| [agl](https://github.com/open-ead/agl) | Decompilation of agl, a graphics library used in first-party Nintendo games | 47 | 🟢 | C++ |
| [LEGO City Undercover](https://github.com/Nintendocustom/Lego-City-Undercover-Decompilation) | Matching decompilation of LEGO City Undercover (Switch, 2017) | 31 | 🟢 | C++ |
| [RedCarpet-S](https://github.com/fruityloops1/RedCarpet-S) | Super Mario 3D World + Bowser's Fury 1.1 decompilation | 30 | 🟡 | C++ |
| [Super Smash Bros. Ultimate decomp](https://github.com/sbergeron42/ssbu-decomp) | Matching decompilation of Super Smash Bros. Ultimate (Switch, AArch64) | 19 | 🟢 | C++ |
| [Super Mario Odyssey 1.0.0 decomp](https://github.com/odyssey-modding/odyssey) | Decompilation of Super Mario Odyssey 1.0.0 (Switch) | 18 | 🗄️ | C++ |
| [EventFlow decomp](https://github.com/open-ead/EventFlow) | Decompilation of Nintendo's EventFlow (evfl) library used in Switch games | 17 | 🟢 | C++ |
| [The Legend of Zelda: Link's Awakening (Switch)](https://github.com/Owen-Splat/las-decomp) | Decompilation of The Legend of Zelda: Link's Awakening (Switch) | 11 | 🟢 |  |
| [Pokémon Sword](https://github.com/charlieduzstuf/pokesword) | Matching decompilation of Pokémon Sword (Switch, 2019) | 10 | 🟢 | C |
| [Splatoon 2 3.1.0 decomp](https://github.com/YoshiCrystal9/Blitz_MasterVer22-Decomp) | Decompilation of Splatoon 2 3.1.0 (Switch) | 6 | 🔴 | C++ |
| [Scott Pilgrim vs. The World: The Game - Complete Edition decomp](https://github.com/jwfeniello/scott-pilgrim-switch-decomp) | Matching reconstruction of Scott Pilgrim vs. The World: The Game - Complete Edition (Switch) | 5 | 🟢 | C |
| [Xenoblade Chronicles 2 decomp](https://github.com/KevinBonnoron/xc2-decomp) | Matching decompilation of Xenoblade Chronicles 2 (Switch, v1.0.0) | 5 | 🟢 | C++ |
| [Pokémon Sword and Shield pawn .amx scripts decomp](https://github.com/lincoln-lm/swsh-pawn-decomp) | Matching decompilation of Pokémon Sword and Shield pawn .amx scripts (Switch) | 3 | 🟡 | OpenEdge ABL |
| [Xenoblade Chronicles 2 decomp](https://github.com/masterofshadow90/xenoblade2-decomp) | Decompilation of Xenoblade Chronicles 2 (Switch) | 3 | 🟢 | Python |
| [The Legend of Zelda: Tears of the Kingdom decomp](https://github.com/oxodx/totk-decomp) | Decompilation of The Legend of Zelda: Tears of the Kingdom (Switch) | 2 | 🟢 | Python |
| [Captain Toad: Treasure Tracker decomp](https://github.com/GRAnimated/cttt-decomp) | Decompilation of Captain Toad: Treasure Tracker (Switch, v1.3.0) | 0 | 🔴 | C++ |
| [Hyrule Warriors: Definitive Edition decomp](https://github.com/MusohSlop/HWDE-decomp) | Matching decompilation of Hyrule Warriors: Definitive Edition (Switch) | 0 | 🟢 | C++ |

## Matching Decompilations — Xbox

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Halo CE decomp](https://github.com/halo-re/halo) | Halo: Combat Evolved (Xbox) decompilation research project | 459 | 🔴 | C |
| [Halo: Combat Evolved (Xbox)](https://github.com/punpckhdq/halo) | Decompilation of Halo: Combat Evolved (Xbox) | 198 | 🟢 | C |
| [Undertale (Xbox One)](https://github.com/kittibyte/UndertaleDecomp) | Decompilation of Undertale (Xbox One) | 127 | 🟡 | Game Maker Language |
| [halo2-decompiled](https://github.com/kirklandsig/halo2-decompiled) | Matching decompilation of Halo 2 for the original Xbox | 114 | 🟢 | C++ |
| [Halo: Reach](https://github.com/ChimpsAtSea/Reach) | Matching decompilation of Halo: Reach (Xbox 360, 2010) | 75 | 🟢 | C++ |
| [Minecraft: Xbox 360 Edition](https://github.com/LCERD/Minecraft-Xbox-360-Decompilation) | Decompilation of Minecraft: Xbox 360 Edition | 69 | 🟡 | C++ |
| [Dance Central 3](https://github.com/rjkiv/dc3-decomp) | Matching decompilation of Dance Central 3 (Xbox 360, 2012) | 43 | 🟢 | C++ |
| [Fallout: New Vegas](https://github.com/ieee802dot11ac/fnv) | Matching decompilation of Fallout: New Vegas (Xbox 360, 2010) | 36 | 🟢 | C++ |
| [TerrariaXDK](https://github.com/dptug/TerrariaXDK) | Decompiled Terraria Xbox 360 Edition source code | 36 | 🟢 | C# |
| [halocea](https://github.com/surreptitiousresearch/halocea) | Decompiled source of Halo: Combat Evolved Anniversary (Xbox 360) | 34 | 🟢 | C |
| [Xbox 360 Kernel](https://github.com/AleBello7276/xkrnl-decomp) | Decompilation of Xbox 360 Kernel | 24 | 🟢 | Python |
| [Banjo-Kazooie (Xbox 360)](https://github.com/banjo360/bk360) | Decompilation of Banjo-Kazooie (Xbox 360) | 22 | 🟢 | C |
| [Sonic the Hedgehog (2006)](https://github.com/rjkiv/sonic06) | Matching decompilation of Sonic the Hedgehog (Xbox 360, 2006) | 15 | 🟢 | C |
| [Quake 4 decomp](https://github.com/cyberheater/Xbox-360-Quake4-decomp) | Decompilation of Quake 4 (Xbox 360) | 14 | 🟢 | C++ |
| [Rockstar Table Tennis decomp](https://github.com/OZORDI/tt-decomp) | Decompilation of Rockstar Table Tennis (2006, Xbox 360) | 13 | 🟢 | C++ |
| [Halo 2 decomp](https://github.com/TheRunaway5/Halo-2-Decompiled) | Decompilation of Halo 2 (Xbox) | 11 | 🟢 | C++ |
| [halo2-decomp](https://github.com/BirchWoodGod/halo2-decomp) | Engine recovery of Halo 2 (original Xbox) for Linux | 7 | 🟢 | Python |
| [Ninja Gaiden Black and Ninja Gaiden 2 decomp](https://github.com/mehmetalinya/DECOMP__Ninja) | Decompilation of Ninja Gaiden Black and Ninja Gaiden 2 (Xbox) | 6 | 🔴 | C++ |
| [Project Haggar decomp](https://github.com/kirklandsig/halo-mega-bloks-decompiled) | Decompilation and PC port of Project Haggar, the cancelled Halo Mega Bloks game (Xbox 360) | 6 | 🟢 | UnrealScript |
| [Kinect Sports](https://github.com/SebaaMG/Kinect-Sports-Decomp) | Matching decompilation of Kinect Sports (Xbox 360, 2010) | 5 | 🟢 | C |
| [pgr2decompiled](https://github.com/x11x00x00x/pgr2decompiled) | Decompilation project to rebuild Project Gotham Racing 2 (Xbox) | 4 | 🟡 | C |
| [Rock Band 3 decomp](https://github.com/freeqaz/rb3-xenon) | Decompilation of Rock Band 3 (Xbox 360, retail) | 4 | 🟢 | C++ |
| [Teen Titans decomp](https://github.com/Cwf1997/teentitans) | Decompilation of Teen Titans (Xbox) | 4 | 🟢 |  |
| [Street Fighter III: 3rd Strike decomp](https://github.com/Manya3084/3s-decomp-ogxb) | Decompilation of Street Fighter III: 3rd Strike (original Xbox) | 3 | 🟢 | C |
| [Minecraft: Xbox 360 Edition decomp](https://github.com/AleBello7276/mc360-decomp) | Decompilation of Minecraft: Xbox 360 Edition | 2 | 🟢 | C |
| [Rock Band 3 + TU5 decomp](https://github.com/rjkiv/rb3-xenon) | Decompilation of Rock Band 3 + TU5 (Xbox 360) | 2 | 🟢 | Python |
| [Viva Piñata decomp](https://github.com/mparisi20/paradise) | Matching decompilation of Viva Piñata (Xbox 360) | 2 | 🟢 | Python |
| [Dance Central 3 decomp](https://github.com/rjkiv/DComp3) | Decompilation of Dance Central 3 (Xbox 360) | 1 | 🗄️ | C++ |
| [Grabbed decomp](https://github.com/luboise/ghoulies-decomp) | Decompilation of Grabbed by the Ghoulies (Xbox) | 1 | 🟢 | C++ |
| [Jet Set Radio Future decomp](https://github.com/silveriviere/Project-Graffiti-Soul) | Decompilation of Jet Set Radio Future (Xbox) | 1 | 🟢 | C++ |
| [Kinect Adventures decomp](https://github.com/SplaatSites/kinect-adventures) | Decompilation of Kinect Adventures (Xbox 360) | 1 | 🟢 | Python |
| [GG-Notebook](https://codeberg.org/KeybadeBlox/GG-Notebook) | Reverse engineering notes for Jet Set Radio Future, companion to the JSRF decompilation |  | ⚪ |  |
| [Jet Set Radio Future](https://codeberg.org/KeybadeBlox/JSRF-Decompilation) | Matching decompilation of Jet Set Radio Future (Xbox, 2002) |  | ⚪ |  |
| [saints-row-1-decomp](https://gitlab.com/HttpAnimations/saints-row-1-decomp) | Matching decompilation of Saints Row (Xbox 360) |  | ⚪ |  |
| [The Simpsons Game decomp](https://github.com/SplaatSites/the-simpsons-game) | Decompilation of The Simpsons Game (Xbox 360) | 0 | 🟢 | Python |
| [Xbox Live Arcade release of Peggle decomp](https://github.com/SplaatSites/peggle) | Decompilation of the Xbox Live Arcade release of Peggle (Xbox 360) | 0 | 🟢 | Python |
| [XDemos-Decomp](https://codeberg.org/KeybadeBlox/XDemos-Decomp) | Decompilation of the original Xbox demo disc launcher |  | ⚪ |  |

## Mod Loaders & Script Extenders

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [LunaTranslator](https://github.com/HIllya51/LunaTranslator) | Visual novel translator that hooks game text from running Windows games | 13,891 | 🟢 | C++ |
| [BepInEx](https://github.com/BepInEx/BepInEx) | Plugin/modding framework for Unity Mono, IL2CPP and XNA games | 8,902 | 🟢 | C# |
| [Minecraft Forge](https://github.com/MinecraftForge/MinecraftForge) | Modding API and loader for Minecraft: Java Edition | 7,834 | 🟢 | Java |
| [Harmony](https://github.com/pardeike/Harmony) | Library for patching and decorating .NET/Mono methods at runtime, widely used for game mods | 6,713 | 🟢 | C# |
| [tModLoader](https://github.com/tModLoader/tModLoader) | Mod loader and API for Terraria | 5,755 | 🟢 | C# |
| [REFramework](https://github.com/praydog/REFramework) | Mod loader, scripting platform and VR support for Capcom RE Engine games | 5,672 | 🟢 | C++ |
| [dlssg-to-fsr3](https://github.com/Nukem9/dlssg-to-fsr3) | Replaces DLSS Frame Generation with FSR 3 frame generation in games | 4,977 | 🟡 | C++ |
| [Cyber Engine Tweaks](https://github.com/maximegmd/CyberEngineTweaks) | Cyberpunk 2077 scripting framework and fixes | 4,818 | 🟢 | C++ |
| [UEVR](https://github.com/praydog/UEVR) | Universal VR mod injector for Unreal Engine 4.8-5.x games | 4,642 | 🟢 | C++ |
| [FiveM / Cfx.re](https://github.com/citizenfx/fivem) | Multiplayer modification frameworks for GTA V (FiveM) and RDR2 (RedM) | 4,296 | 🟢 | C++ |
| [MelonLoader](https://github.com/LavaGang/MelonLoader) | Universal mod loader for Unity games (Il2Cpp and Mono) | 4,295 | 🟢 | C# |
| [cnc-ddraw](https://github.com/FunkyFr3sh/cnc-ddraw) | DirectDraw reimplementation fixing old games such as Command & Conquer on modern systems | 3,549 | 🟢 | C |
| [FusionFix (GTA IV)](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix) | Fixes and enhancements for Grand Theft Auto IV: Complete Edition | 3,443 | 🟢 | C++ |
| [Widescreen Fixes Pack](https://github.com/ThirteenAG/WidescreenFixesPack) | Plugins adding or fixing widescreen support and bugs in many PC games | 3,268 | 🟢 | C++ |
| [UnityExplorer](https://github.com/sinai-dev/UnityExplorer) | In-game UI for exploring and modifying IL2CPP and Mono Unity games | 3,147 | 🗄️ | C# |
| [RE-UE4SS](https://github.com/UE4SS-RE/RE-UE4SS) | Injectable Lua scripting, SDK generator and live property editor for UE4/UE5 games | 3,056 | 🟢 | C++ |
| [TShock](https://github.com/Pryaxis/TShock) | Terraria server modification and plugin API | 2,901 | 🟢 | C# |
| [SMAPI](https://github.com/Pathoschild/SMAPI) | Modding API and loader for Stardew Valley | 2,772 | 🟢 | C# |
| [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader) | Proxy DLL that loads custom .asi plugins into any game process | 2,377 | 🟢 | C++ |
| [Special K](https://github.com/SpecialKO/SpecialK) | Game modding and enhancement framework for Windows games | 2,137 | 🟢 | C++ |
| [NeoForge (Minecraft)](https://github.com/neoforged/NeoForge) | Modding API and loader for Minecraft: Java Edition | 2,115 | 🟢 | Java |
| [Multi Theft Auto](https://github.com/multitheftauto/mtasa-blue) | Multiplayer engine for GTA: San Andreas | 1,882 | 🟢 | C++ |
| [BWAPI](https://github.com/bwapi/bwapi) | Brood War API for writing StarCraft: Brood War AI bots | 1,714 | 🟢 | C++ |
| [LeviLamina](https://github.com/LiteLDev/LeviLamina) | Mod loader for Minecraft Bedrock Edition dedicated server | 1,700 | 🟢 | C++ |
| [Dalamud](https://github.com/goatcorp/Dalamud) | Plugin framework and API for Final Fantasy XIV | 1,644 | 🟢 | C |
| [MCP-Reborn](https://github.com/Hexeption/MCP-Reborn) | Modern Mod Coder Pack for decompiling and modding Minecraft Java | 1,568 | 🟢 |  |
| [BG3SE](https://github.com/Norbyte/bg3se) | Baldur's Gate 3 Script Extender | 1,530 | 🟢 | C++ |
| [CounterStrikeSharp](https://github.com/roflmuffin/CounterStrikeSharp) | C# server plugin framework for Counter-Strike 2 built on reverse engineered Source 2 internals | 1,379 | 🟢 | C# |
| [ScriptHookVDotNet (GTA V)](https://github.com/scripthookvdotnet/scripthookvdotnet) | .NET scripting runtime for Grand Theft Auto V on top of Script Hook V | 1,375 | 🟢 | C# |
| [3Dmigoto](https://github.com/bo3b/3Dmigoto) | DirectX 11 wrapper for shader modding and stereo 3D fixes in games | 1,250 | 🟢 | C++ |
| [Yarn](https://github.com/FabricMC/yarn) | Open Minecraft deobfuscation mappings for modding | 1,227 | 🟢 | Java |
| [SilentPatch (GTA)](https://github.com/CookiePLMonster/SilentPatch) | Fixes for GTA III, Vice City and San Andreas made by patching the game binaries | 1,222 | 🟢 | C++ |
| [TiltedEvolution](https://github.com/tiltedphoques/TiltedEvolution) | Skyrim Together multiplayer mod built on reverse engineered engine internals | 1,190 | 🟢 | C++ |
| [ModEngine2](https://github.com/soulsmods/ModEngine2) | Runtime injection library for modding FromSoftware Souls games | 1,144 | 🗄️ | C++ |
| [RuntimeUnityEditor](https://github.com/ManlyMarco/RuntimeUnityEditor) | In-game inspector and debugging tools for Unity games | 1,127 | 🟢 | C# |
| [Reloaded-II](https://github.com/Reloaded-Project/Reloaded-II) | Universal .NET-powered modding framework for native x86/x64 games | 1,052 | 🟢 | C# |
| [Steamodded](https://github.com/Steamodded/smods) | Mod loader for Balatro | 1,000 | 🟢 | Lua |
| [libsm64](https://github.com/libsm64/libsm64) | Super Mario 64 (N64) as a library for use in other game engines, from the decompilation | 972 | 🟢 | C |
| [Luxtorpeda](https://github.com/luxtorpeda-dev/luxtorpeda) | Steam Play compatibility tool that runs games with native Linux engine reimplementations | 955 | 🗄️ | Rust |
| [2010 Rust Rewrite Mashup](https://github.com/chasmlol/2010-rust-rewrite-mashup) | Rust mashup of the IW4L Modern Warfare 2 rewrite with Skate 3 and Minecraft modes (PC) | 918 | 🟢 | Rust |
| [Fabric Loader (Minecraft)](https://github.com/FabricMC/fabric-loader) | Mod loader for Minecraft: Java Edition | 893 | 🟢 | Java |
| [xNVSE](https://github.com/xNVSE/NVSE) | New Vegas Script Extender | 853 | 🟢 | C++ |
| [Penumbra](https://github.com/xivdev/Penumbra) | Runtime mod loader for Final Fantasy XIV | 792 | 🟢 | C# |
| [thcrap (Touhou)](https://github.com/thpatch/thcrap) | Touhou Community Reliant Automatic Patcher: patching and translation framework for Touhou games | 774 | 🟢 | C++ |
| [Pengu Loader](https://github.com/PenguLoader/PenguLoader) | JavaScript plugin loader for the League of Legends client | 747 | 🟢 | C++ |
| [Godot Mod Loader](https://github.com/GodotModding/godot-mod-loader) | Generic mod loader for Godot games | 687 | 🟢 | GDScript |
| [plugin-sdk](https://github.com/DK22Pac/plugin-sdk) | SDK for ASI/CLEO plugins for GTA III, Vice City and San Andreas | 676 | 🟢 | C |
| [open.mp](https://github.com/openmultiplayer/open.mp) | Multiplayer mod for GTA San Andreas, backwards compatible with SA-MP | 658 | 🟢 | C++ |
| [me3](https://github.com/garyttierney/me3) | Mod Engine 3, a framework for modding and instrumenting FromSoftware games | 657 | 🟢 | Rust |
| [Xenia game patches](https://github.com/xenia-canary/game-patches) | Game patches such as frame-rate and resolution fixes for the Xenia Xbox 360 emulator | 627 | 🟢 | Python |
| [Lovely](https://github.com/ethangreen-dev/lovely-injector) | Runtime Lua injector for LOVE2D games such as Balatro | 616 | 🟢 | Rust |
| [Unity Mod Manager](https://github.com/newman55/unity-mod-manager) | Mod manager and loader for Unity games | 551 | 🟢 | C# |
| [Il2CppAssemblyUnhollower](https://github.com/knah/Il2CppAssemblyUnhollower) | Generates managed proxy assemblies for IL2CPP Unity games so they can be modded | 545 | 🗄️ | C# |
| [FFNx](https://github.com/julianxhokaxhiu/FFNx) | Next-generation modding platform and driver for Final Fantasy VII and VIII PC | 526 | 🟢 | C++ |
| [Everest](https://github.com/EverestAPI/Everest) | Celeste mod loader and mod API | 520 | 🟢 | C# |
| [ModTheSpire](https://github.com/kiooeht/ModTheSpire) | External mod loader for Slay the Spire | 519 | 🟡 | Java |
| [HedgeModManager](https://github.com/thesupersonic16/HedgeModManager) | Mod loader and manager for Sonic Hedgehog Engine games | 500 | 🟢 | C# |
| [RED4ext](https://github.com/wopss/RED4ext) | Script extender for REDengine 4 (Cyberpunk 2077) | 500 | 🟢 | C++ |
| [BDSX](https://github.com/bdsx/bdsx) | Minecraft Bedrock Dedicated Server modding with Node.js | 490 | 🗄️ | TypeScript |
| [Phobos](https://github.com/Phobos-developers/Phobos) | Engine extension for C&C Red Alert 2: Yuri's Revenge | 474 | 🟢 | C++ |
| [mint (Deep Rock Galactic)](https://github.com/trumank/mint) | Mod loader and integration for Deep Rock Galactic | 456 | 🟢 | Rust |
| [sfall](https://github.com/sfall-team/sfall) | sfall - Engine modifications for Fallout 2 | 445 | 🟢 | C++ |
| [Mod Loader (GTA III / VC / SA)](https://github.com/thelink2012/modloader) | Mod loader for Grand Theft Auto III, Vice City and San Andreas | 437 | 🟢 | C++ |
| [KH-ReFined](https://github.com/KH-ReFined/KH-ReFined) | Fixes and improvements for the PC ports of Kingdom Hearts | 436 | 🗄️ | C++ |
| [RetroMCP](https://github.com/MCPHackers/RetroMCP-Java) | Mod Coder Pack for decompiling and recompiling old Minecraft versions | 414 | 🟢 | Java |
| [DivaModLoader](https://github.com/blueskythlikesclouds/DivaModLoader) | Mod loader for Hatsune Miku: Project DIVA Mega Mix+ | 411 | 🟡 | C++ |
| [ARCropolis](https://github.com/Raytwo/ARCropolis) | Modding framework for Super Smash Bros. Ultimate file replacement | 392 | 🟢 | Rust |
| [Oxide.Rust](https://github.com/OxideMod/Oxide.Rust) | Rust game extension for the Oxide modding framework | 387 | 🟢 | C# |
| [anno1800-mod-loader](https://github.com/magicalcookie/anno1800-mod-loader) | Mod loader for Anno 1800 | 368 | 🗄️ | C++ |
| [REPENTOGON](https://github.com/TeamREPENTOGON/REPENTOGON) | Script extender for The Binding of Isaac: Repentance | 359 | 🟢 | C++ |
| [SFSE](https://github.com/ianpatt/sfse) | Starfield Script Extender | 359 | 🟢 | C++ |
| [SKSE64](https://github.com/ianpatt/skse64) | Skyrim Special Edition Script Extender | 358 | 🟢 | C++ |
| [SatisfactoryModLoader](https://github.com/satisfactorymodding/SatisfactoryModLoader) | Unofficial mod loader for Satisfactory | 346 | 🟢 | C++ |
| [Hollow Knight Modding API](https://github.com/hk-modding/api) | Modding API for Hollow Knight built by patching game assemblies | 344 | 🟢 | C# |
| [FFXIVClientStructs](https://github.com/aers/FFXIVClientStructs) | Reverse engineered native class layouts of the Final Fantasy XIV client | 343 | 🟢 | C# |
| [VorpalFix](https://github.com/Wemino/VorpalFix) | Binary patch that fixes technical issues in American McGee's Alice (PC) | 338 | 🟢 | C++ |
| [BCML (Breath of the Wild)](https://github.com/NiceneNerd/BCML) | Cross-platform mod loader and merger for The Legend of Zelda: Breath of the Wild | 332 | 🟢 | Python |
| [xOBSE](https://github.com/llde/xOBSE) | Oblivion Script Extender | 315 | 🟢 | C++ |
| [Skyline](https://github.com/skyline-dev/skyline) | Runtime hooking and code patching environment for Nintendo Switch games | 312 | 🟢 | C++ |
| [Better-Endfield](https://github.com/Dr-hydra/Better-Endfield) | Modding toolkit for Arknights: Endfield on Windows and Android | 301 | 🟢 | C# |
| [unreal-vr](https://github.com/TheNewJavaman/unreal-vr) | Adds VR support to flatscreen Unreal Engine games | 301 | 🔴 | C++ |
| [ZHMModSDK](https://github.com/OrfeasZ/ZHMModSDK) | Modding SDK and mod loader for Hitman World of Assassination | 287 | 🟢 | C++ |
| [BakkesModSDK](https://github.com/bakkesmodorg/BakkesModSDK) | Unofficial SDK for Rocket League modding with BakkesMod | 284 | 🟢 | C++ |
| [MetaHookSv](https://github.com/MetaHookSv/MetaHookSv) | MetaHook plugin loader ported to the Sven Co-op GoldSrc engine | 260 | 🟢 | Python |
| [Reactor](https://github.com/NuclearPowered/Reactor) | Modding API for Among Us | 254 | 🟢 | C# |
| [UnrealModLoader](https://github.com/RussellJerome/UnrealModLoader) | Universal mod loader for Unreal Engine 4 games | 247 | 🔴 | C++ |
| [CommonLibSSE](https://github.com/Ryan-rsm-McKenzie/CommonLibSSE) | Reverse-engineered C++ library of Skyrim SE game types for plugin development | 241 | 🔴 | C++ |
| [MetaMystia](https://github.com/MetaMystia/MetaMystia) | Multiplayer mod for Touhou Mystia's Izakaya | 211 | 🟢 | C# |
| [BSIPA](https://github.com/nike4613/BeatSaber-IPA-Reloaded) | Unity mod injector built for Beat Saber | 204 | 🟢 | C# |
| [The Legend of Zelda: Majora's Mask 3D (mm3d-dekui)](https://github.com/tgacquin/mm3d-dekui) | Single-screen and frame interpolation patch for Majora's Mask 3D (3DS) | 203 | 🟢 | C++ |
| [D2RMM](https://github.com/olegbl/d2rmm) | Mod manager for Diablo II: Resurrected | 201 | 🟢 | TypeScript |
| [Hedge Mod Manager](https://github.com/hedge-dev/HedgeModManager) | Mod manager and code loader for Sonic the Hedgehog PC games | 201 | 🟢 | C# |
| [Engine Fixes (Skyrim SE)](https://github.com/aers/EngineFixesSkyrim64) | SKSE plugin that fixes Skyrim Special Edition engine bugs | 200 | 🟢 | C++ |
| [ER Mario](https://github.com/deltarooo/er-mario) | Elden Ring mod that adds Super Mario 64's Mario via libsm64 (PC) | 196 | 🟢 | C |
| [GDWeave](https://github.com/NotNite/GDWeave) | Mod loader and runtime script patching for Godot games | 191 | 🗄️ | C# |
| [CLEO 5](https://github.com/cleolibrary/CLEO5) | Script extension library for GTA San Andreas | 186 | 🟢 | C++ |
| [PriconneRe-TL](https://github.com/ImaterialC/PriconneRe-TL) | English translation patch for Princess Connect! Re:Dive (JP Windows client, IL2CPP) | 186 | 🟢 |  |
| [ME3Tweaks Mod Manager](https://github.com/ME3Tweaks/ME3TweaksModManager) | Mod manager for Mass Effect trilogy and Legendary Edition | 184 | 🟢 | C# |
| [ThunderKit](https://github.com/PassivePicasso/ThunderKit) | Mod project development environment for Unity games | 182 | 🟢 | C# |
| [UXM (FromSoftware)](https://github.com/JKAnderson/UXM) | Unpacks FromSoftware game archives so mods can load loose files | 182 | 🗄️ | C# |
| [ArkWeb](https://github.com/luki-1/ArkWeb) | Experiment that runs Spider-Man Remastered and Arkham Knight together with shared collision | 179 | 🟢 | C++ |
| [MSCLoader (My Summer Car)](https://github.com/piotrulos/MSCModLoader) | Mod loader for My Summer Car and My Winter Car | 179 | 🟢 | C# |
| [EldenRingModLoader](https://github.com/techiew/EldenRingModLoader) | Mod loader for Elden Ring | 173 | 🟡 | C++ |
| [Hacknet-Pathfinder](https://github.com/Arkhist/Hacknet-Pathfinder) | Mod loader for Hacknet: Labyrinths | 169 | 🟡 | C# |
| [Retro64](https://github.com/Retro64Mod/Retro64Mod) | Minecraft mod that adds Super Mario 64's Mario via libsm64 (PC) | 169 | 🟢 | Java |
| [RE_Kenshi](https://github.com/BFrizzleFoShizzle/RE_Kenshi) | Plugin loader and engine fixes for Kenshi | 168 | 🟢 | C++ |
| [R2API](https://github.com/risk-of-thunder/R2API) | Modding API for Risk of Rain 2 | 167 | 🟢 | C# |
| [balamod (Balatro)](https://github.com/balamod/balamod) | Mod loader, injector and decompiler for Balatro | 161 | 🟡 | Rust |
| [kanan-new](https://github.com/cursey/kanan-new) | Quality-of-life mod framework for Mabinogi | 161 | 🗄️ | C++ |
| [F4SE](https://github.com/ianpatt/f4se) | Fallout 4 Script Extender | 156 | 🟢 | C++ |
| [SageMetaTool](https://github.com/MetaIdea/SageMetaTool) | Launcher that adds engine updates to SAGE engine games (C&C Generals, Battle for Middle-earth) | 156 | 🟡 | Lua |
| [thinker](https://github.com/induktio/thinker) | Engine patch with fixes and AI improvements for Sid Meier's Alpha Centauri: Alien Crossfire (PC) | 156 | 🟢 | C++ |
| [Slippi ASM](https://github.com/project-slippi/slippi-ssbm-asm) | ASM codes adding rollback netplay and replay recording to Super Smash Bros. Melee | 154 | 🟢 | Assembly |
| [Jötunn (Valheim)](https://github.com/Valheim-Modding/Jotunn) | Modding library for Valheim | 151 | 🟢 | C# |
| [W2-Plus (Worms 2)](https://github.com/Carlmundo/W2-Plus) | Patch that makes Worms 2 run on modern computers with extra features | 150 | 🟢 | Inno Setup |
| [QModManager (Subnautica)](https://github.com/SubnauticaModding/QModManager) | Mod loader for Subnautica and Below Zero | 149 | 🗄️ | C# |
| [Creation-Kit-Platform-Extended](https://github.com/Perchik71/Creation-Kit-Platform-Extended) | Fixes and extensions for Bethesda's Creation Kit built from reverse engineering | 148 | 🟢 | C++ |
| [CLEO-iOS (GTA San Andreas)](https://github.com/squ1dd13/CLEO-iOS) | Mod loader for GTA: San Andreas on iOS | 145 | 🗄️ | Rust |
| [Dark-Souls-1-Overhaul](https://github.com/metal-crow/Dark-Souls-1-Overhaul) | Gameplay overhaul mod for Dark Souls built via reverse engineering | 143 | 🟢 | C++ |
| [WorldBox ModLoader](https://github.com/WorldBoxOpenMods/ModLoader) | Mod loader for WorldBox | 143 | 🟢 | C# |
| [TweakXL (Cyberpunk 2077)](https://github.com/psiberx/cp2077-tweak-xl) | Cyberpunk 2077 modding tool for TweakDB edits | 140 | 🟢 | C++ |
| [AutomataMP](https://github.com/praydog/AutomataMP) | NieR: Automata multiplayer mod | 138 | 🟡 | C++ |
| [FF8_demaster](https://github.com/MaKiPL/FF8_demaster) | Unofficial Final Fantasy VIII Remastered core mod | 137 | 🟢 | C |
| [skyrimse-test](https://github.com/Nukem9/skyrimse-test) | Reverse engineering and fixes for Skyrim Special Edition | 137 | 🟡 | C++ |
| [ArchiveXL (Cyberpunk 2077)](https://github.com/psiberx/cp2077-archive-xl) | Cyberpunk 2077 modding tool for loading custom resources without archive conflicts | 134 | 🟢 | C++ |
| [MWSE](https://github.com/MWSE/MWSE) | Morrowind Script Extender with Lua scripting | 133 | 🟢 | C++ |
| [G64](https://github.com/ckosmic/g64) | Garry's Mod addon that adds Super Mario 64's Mario via libsm64 (PC) | 128 | 🔴 | Lua |
| [OTAPI](https://github.com/SignatureBeef/Open-Terraria-API) | Patched Terraria server assembly exposing hooks for modding | 125 | 🟢 | C# |
| [Rift (Minecraft)](https://github.com/DimensionalDevelopment/Rift) | Lightweight mod loader and API for Minecraft 1.13 | 124 | 🗄️ | Java |
| [StringReloads](https://github.com/Hydrooxzgen/EnderBridge) | Tool to inject translated strings into games through low-level code hooks | 124 | 🗄️ | Python |
| [ResoniteModLoader](https://github.com/resonite-modding-group/ResoniteModLoader) | Mod loader for Resonite | 118 | 🟢 | C# |
| [ACUFixes](https://github.com/NameTaken3125/ACUFixes) | Add-on and fixes for Assassin's Creed Unity | 116 | 🟡 | C++ |
| [sm64-san-andreas (Super Mario 64 in GTA San Andreas)](https://github.com/headshot2017/sm64-san-andreas) | GTA San Andreas mod that adds Super Mario 64's Mario via libsm64 (PC) | 116 | 🟡 | C |
| [TRLAU-menu-hook](https://github.com/TheIndra55/TRLAU-menu-hook) | Reverse engineering, menu and patches for Tomb Raider Legend/Anniversary/Underworld | 114 | 🟢 | C++ |
| [AndroidModLoader (AML)](https://github.com/RusJJ/AndroidModLoader) | Mod loader for Android games and applications | 112 | 🟢 | C++ |
| [RedLoader (Sons of the Forest)](https://github.com/ToniMacaroni/RedLoader) | Mod loader for Sons of the Forest | 110 | 🟡 | C# |
| [umamusume-localify](https://github.com/Kimjio/umamusume-localify) | Localization and enhancement mod for the Uma Musume Windows client | 110 | 🟢 | C++ |
| [OWML](https://github.com/ow-mods/owml) | Mod loader and library for Outer Wilds | 109 | 🟢 | C# |
| [Carbon (Rust)](https://github.com/CarbonCommunity/Carbon) | Mod loader for Rust game servers | 105 | 🟢 | C# |
| [server-modloader (Minecraft Bedrock)](https://github.com/minecraft-linux/server-modloader) | Mod loader for the Minecraft Bedrock dedicated server | 104 | 🟡 | C++ |
| [MKW-SP](https://github.com/mkw-sp/mkw-sp) | Mario Kart Wii mod with features built on reverse-engineered game code | 102 | 🟢 | C++ |
| [M2TWEOP-library](https://github.com/EOP-Labs/M2TWEOP-library) | Medieval II: Total War Engine Overhaul Project | 101 | 🟢 | C++ |
| [CommonLibSF](https://github.com/Starfield-Reverse-Engineering/CommonLibSF) | Collaborative reverse engineered library for Starfield modding | 100 | 🗄️ | C++ |
| [RB3Enhanced](https://github.com/RBEnhanced/RB3Enhanced) | Open-source plugin providing fixes and features for Rock Band 3 | 100 | 🟢 | C |
| [Installer](https://github.com/SteamClientHomebrew/Installer) | Installer for Millennium, a Steam client theming and plugin loader | 97 | 🟢 | C++ |
| [PolyMod](https://github.com/PolyModdingTeam/PolyMod) | Mod loader for The Battle of Polytopia | 96 | 🟢 | C# |
| [CommonLibF4](https://github.com/Ryan-rsm-McKenzie/CommonLibF4) | Reverse engineered library for Fallout 4 modding | 93 | 🟢 | C++ |
| [WA-Plus (Worms Armageddon)](https://github.com/Carlmundo/WA-Plus) | Patch for Worms Armageddon that modernizes the game | 92 | 🟢 | Inno Setup |
| [GDPatch](https://github.com/GDPatch/GDPatch) | Cross-platform, cross-version mod loader for Godot games | 90 | 🟢 | Rust |
| [FA2sp](https://github.com/secsome/FA2sp) | Extension for the Red Alert 2 Final Alert 2 map editor | 88 | 🗄️ | C++ |
| [unrealmodding](https://github.com/AstroTechies/unrealmodding) | Rust tools and integrator for modding Unreal Engine games | 88 | 🟢 | Rust |
| [OneLoader (OMORI)](https://github.com/rphsoftware/OneLoader) | Mod loader for OMORI | 87 | 🟡 | JavaScript |
| [sh2cammod (Silent Hill 2)](https://github.com/zealottormunds/sh2cammod) | Silent Hill 2 mod loader and camera mod | 87 | 🟡 |  |
| [Spore ModAPI](https://github.com/Spore-Community/Spore-ModAPI) | C++ SDK for creating code mods for Spore | 87 | 🟢 | C++ |
| [MuseDashModLoader](https://github.com/mo10/MuseDashModLoader) | Mod loader for Muse Dash | 84 | 🔴 | C |
| [PitCrew (The Crew)](https://github.com/Telonof/PitCrew) | Mod loader for The Crew and The Crew 2 | 81 | 🟢 | C# |
| [Chairloader (Prey)](https://github.com/thelivingdiamond/Chairloader) | Modding framework for Prey (2017) | 78 | 🟢 | C++ |
| [fromsoftware-rs](https://github.com/vswarte/fromsoftware-rs) | Rust bindings to Elden Ring, Dark Souls 3, Nightreign and Sekiro internals | 78 | 🟢 | Rust |
| [libER](https://github.com/Dasaav-dsv/libER) | Elden Ring API library focused on binary compatibility | 77 | 🟡 | C++ |
| [ONI-Modloader](https://github.com/javisar/ONI-Modloader) | Mod loader for Oxygen Not Included | 75 | 🟡 | C# |
| [zmod](https://github.com/Fragonite/zmod) | Mod loader for Dynasty Warriors 8: Xtreme Legends and Warriors Orochi 4 | 74 | 🟡 | C++ |
| [ModLoader64](https://github.com/hylian-modding/ModLoader64) | Game-agnostic N64 mod loader built on Mupen64Plus | 71 | 🔴 | TypeScript |
| [SADX Mod Loader](https://github.com/X-Hax/sadx-mod-loader) | Mod loader for Sonic Adventure DX PC | 70 | 🟢 | C |
| [Multivoid](https://github.com/VOTV-MP/Multivoid) | Multiplayer co-op mod for Voices of the Void (UE4SS) | 67 | 🟢 | C++ |
| [BallanceModLoader](https://github.com/Gamepiaynmo/BallanceModLoader) | Mod loader for Ballance | 66 | 🔴 | C++ |
| [SharpPluginLoader](https://github.com/Fexty12573/SharpPluginLoader) | C# plugin loader for Monster Hunter World | 66 | 🟢 | C# |
| [ITB-ModLoader](https://github.com/itb-community/ITB-ModLoader) | Lua mod loader for Into the Breach | 65 | 🟢 | Lua |
| [OBSE64](https://github.com/ianpatt/obse64) | Oblivion Remastered Script Extender | 65 | 🟡 | C++ |
| [bg3se-macos](https://github.com/tdimino/bg3se-macos) | Baldur's Gate 3 Script Extender replication for macOS | 64 | 🟢 | C |
| [CCLoader (CrossCode)](https://github.com/CCDirectLink/CCLoader) | Mod loader for CrossCode | 64 | 🟢 | JavaScript |
| [SA2 Mod Loader](https://github.com/X-Hax/sa2-mod-loader) | Mod loader for Sonic Adventure 2 PC | 64 | 🟢 | C++ |
| [MGE XE (Morrowind)](https://github.com/Hrnchamd/MGE-XE) | Morrowind Graphics Extender XE: renderer and engine extensions for The Elder Scrolls III: Morrowind | 63 | 🟡 | C++ |
| [SRML (Slime Rancher)](https://github.com/SlimeRancherModding/SRML) | Mod loader for Slime Rancher | 62 | 🟡 | C# |
| [umamusume-localify-android](https://github.com/Kimjio/umamusume-localify-android) | Android port of the umamusume-localify localization mod | 62 | 🟢 | C++ |
| [EDFModLoader](https://github.com/BlueAmulet/EDFModLoader) | Mod loader for Earth Defense Force 4.1, 5 and 6 | 59 | 🟡 | C++ |
| [besiege-modloader](https://github.com/spaar/besiege-modloader) | Mod loader for Besiege | 57 | 🔴 | C# |
| [Final-Fantasy-Type-0-HD-Unlocker](https://github.com/Banz99/Final-Fantasy-Type-0-Hd-Unlocker) | ASI plugin that adds custom resolutions and frame rates to Final Fantasy Type-0 HD | 56 | 🟡 | C++ |
| [JIP LN NVSE](https://github.com/jazzisparis/JIP-LN-NVSE) | Extension plugin for the New Vegas Script Extender | 56 | 🟡 | C++ |
| [NeosModLoader](https://github.com/neos-modding-group/NeosModLoader) | Mod loader for Neos VR | 56 | 🗄️ | C# |
| [BuckshotRouletteModLoader](https://github.com/AGO061/BuckshotRouletteModLoader) | Mod loader for Buckshot Roulette | 55 | 🟢 |  |
| [SMC64 — Mario in Halo: CE](https://github.com/KodyJKing/smc64) | Halo: CE (MCC) mod that adds Super Mario 64's Mario via libsm64 (PC) | 55 | 🟢 | C++ |
| [Bannerlord.Harmony](https://github.com/BUTR/Bannerlord.Harmony) | Harmony patching library packaged for Mount & Blade II: Bannerlord mods | 54 | 🟢 | C# |
| [XNFSMusicPlayer](https://github.com/xan1242/XNFSMusicPlayer) | Custom music player replacement for Need for Speed games | 54 | 🔴 | C++ |
| [FMMLoader-26](https://github.com/jal-co/FMMLoader-26) | Mod loader for Football Manager 26 | 53 | 🟢 | TypeScript |
| [mania-mod-loader (Sonic Mania)](https://github.com/sonicretro/mania-mod-loader) | Mod loader for Sonic Mania | 52 | 🔴 | C++ |
| [NFSPluginSDK](https://github.com/berkayylmao/NFSPluginSDK) | Reversed types of BlackBox-era Need for Speed games for plugin and script mods | 52 | 🟡 | C++ |
| [chaudloader](https://github.com/RockmanEXEZone/chaudloader) | Mod loader for Mega Man Battle Network Legacy Collection | 50 | 🟢 | Rust |
| [BattleTechModLoader](https://github.com/BattletechModders/BattleTechModLoader) | Mod loader and injector for BattleTech | 49 | 🗄️ | C# |
| [ETGMod (Enter the Gungeon)](https://github.com/ModTheGungeon/ETGMod) | Mod loader and API for Enter the Gungeon | 49 | 🔴 | C# |
| [CrateModLoader](https://github.com/TheBetaM/CrateModLoader) | Randomizer and mod loader for various games | 48 | 🔴 | C# |
| [bedrock-headers](https://github.com/mcbedrock/bedrock-headers) | Reverse-engineered modding headers for Minecraft: Bedrock Edition | 47 | 🔴 | C++ |
| [Riftwii](https://github.com/KakarottoCake/Riftwii) | Clean-room Wii disc mod loader with SD packages, runtime patching and save redirection | 47 | 🟢 | C++ |
| [sh4modloader (Silent Hill 4)](https://github.com/lowleveldesign/lldext) | Mod loader for Silent Hill 4: The Room | 47 | 🟡 | JavaScript |
| [Darktide-Mod-Loader](https://github.com/Darktide-Mod-Framework/Darktide-Mod-Loader) | Mod loader for Warhammer 40,000: Darktide | 46 | 🟢 | Lua |
| [gomori (OMORI)](https://github.com/Gilbert142/gomori) | Mod loader for OMORI | 46 | 🗄️ | JavaScript |
| [p4gpc.modloader](https://github.com/tge-was-taken/p4gpc.modloader) | Mod loader for the Steam version of Persona 4 Golden | 46 | 🔴 | C# |
| [astro_modloader (Astroneer)](https://github.com/AstroTechies/astro_modloader) | Astroneer mod loader written in Rust | 45 | 🟢 | Rust |
| [Reloaded-Mod-Loader](https://github.com/Sewer56/Reloaded-Mod-Loader) | Deprecated universal C# DLL injection mod loader (predecessor of Reloaded II) | 44 | 🗄️ | C# |
| [H2Codez (Halo 2)](https://github.com/Project-Cartographer/H2Codez) | Mod that restores and adds functionality to the Halo 2 Editing Kit | 42 | 🔴 | C++ |
| [PluginMH (Manhunt)](https://github.com/ermaccer/Manhunt.PluginMH) | Free camera, first-person mode and other additions for Manhunt | 41 | 🟡 | C |
| [ThMouseX](https://github.com/Meigyoku-Thmn/ThMouseX) | Adds mouse control to Touhou Project games | 39 | 🟢 | C++ |
| [Stationeers.Addons](https://github.com/StationeersAddons/Stationeers.Addons) | Modding framework for Stationeers | 38 | 🔴 | C# |
| [yrpp-spawner (Red Alert 2)](https://github.com/CnCNet/yrpp-spawner) | CnCNet spawner DLL for Command & Conquer: Yuri's Revenge | 38 | 🟢 | C++ |
| [Faucet (Minecraft LCE)](https://github.com/ytsodacan/Faucet) | Mod loader for Minecraft Legacy Console Edition | 37 | 🟢 | C++ |
| [VostokMods](https://github.com/Ryhon0/VostokMods) | Mod loader for Road to Vostok | 37 | 🟢 | GDScript |
| [fastman92 limit adjuster (GTA)](https://github.com/abhiaiyer91/recompose-apollo) | Limit adjuster that patches GTA III, Vice City and San Andreas executables | 36 | 🟡 | JavaScript |
| [plugin-sdk-sa](https://github.com/Dryxio/plugin-sdk-sa) | GTA San Andreas plugin SDK extended from a fully reverse-engineered codebase | 36 | 🟢 | C |
| [alien-shooter-multiplayer](https://github.com/ep1h/alien-shooter-multiplayer) | Multiplayer mode for Alien Shooter (2003) | 35 | 🟢 | C |
| [p5rpc.modloader](https://github.com/Sewer56/p5rpc.modloader) | Mod loader for the PC versions of Persona 3, 4 and 5 Royal | 35 | 🟢 | C# |
| [pulsar-mod-loader](https://github.com/PULSAR-Modders/pulsar-mod-loader) | Unofficial mod support for PULSAR: Lost Colony | 35 | 🟡 | C# |
| [spaghetti](https://github.com/bananaturtlesandwich/spaghetti) | Function hooker for cooked Unreal Engine blueprints | 35 | 🟢 | Rust |
| [beatsaber-hook](https://github.com/jakibaki/beatsaber-hook) | Function hooking and mod loader for Beat Saber on Oculus Quest (IL2CPP) | 34 | 🔴 | C |
| [shroudtopia](https://github.com/s0t7x/shroudtopia) | Experimental mod loader for Enshrouded | 33 | 🟢 | C++ |
| [gdmod](https://github.com/arthuro555/gdmod) | Mod loader and modding API for GDevelop games | 32 | 🔴 | TypeScript |
| [ggxrd-mod](https://github.com/super-continent/ggxrd-mod) | Character script mod loader and QoL mod for Guilty Gear Xrd Rev 2 | 32 | 🟢 | C++ |
| [NoMansSky.Api](https://github.com/gurrenm3/NoMansSky.Api) | C# modding API for No Man's Sky built on Reloaded II | 32 | 🔴 | C# |
| [Synapse (SCP:SL)](https://github.com/SynapseSL/Synapse) | Mod loader for SCP: Secret Laboratory | 32 | 🗄️ | C# |
| [Yet-Another-BG3-Native-Mod-Loader](https://github.com/MolotovCherry/Yet-Another-BG3-Native-Mod-Loader) | Native mod loader for Baldur's Gate 3 | 31 | 🟢 | Rust |
| [CrabeLoader](https://github.com/LucasLhomme/CrabeLoader) | Mod loader for Disney Infinity 3.0 (PC, Octane engine) | 30 | 🟢 | C++ |
| [crus-modloader](https://github.com/CruS-Modding-Infrastructure/crus-modloader) | Mod loader for Cruelty Squad | 30 | 🟡 | GDScript |
| [DemonsSoulsDebug](https://github.com/gibbed/DemonsSoulsDebug) | Patches for Demon's Souls that enable debug menus and other functions | 30 | 🔴 | C# |
| [JaLoader](https://github.com/theLeaxx/JaLoader) | Mod loader for Jalopy | 30 | 🟢 | C# |
| [EmperorReborn](https://github.com/azmawee/EmperorReborn) | Widescreen and compatibility patch for Emperor: Battle for Dune on modern Windows (PC) | 29 | 🟢 | C |
| [SGG-Mod-Format](https://github.com/SGG-Modding/SGG-Mod-Format) | Mod format and loader for Supergiant Games titles (Bastion, Transistor, Pyre, Hades) | 29 | 🟡 | Python |
| [naneINF Balatro Modloader](https://github.com/3XPLwastaken/naneINF-Balatro-Modloader) | Balatro mod loader and injector for PC, iOS and Android | 28 | 🟡 | Lua |
| [Reality](https://github.com/whatdahopper-archive/Reality) | Modular Unreal Engine mod loader written in C# | 28 | 🗄️ | C# |
| [sonicr-mod-loader](https://github.com/sonicretro/sonicr-mod-loader) | Mod loader for the 2004 PC version of Sonic R | 28 | 🔴 | C++ |
| [grimmod](https://github.com/TheHexagonCodes/grimmod) | Mod loader for Grim Fandango Remastered | 27 | 🟡 | Rust |
| [HAT (FEZ)](https://github.com/FEZModding/HAT) | Mod loader for FEZ | 27 | 🟢 | C# |
| [ps3-ckit](https://github.com/tge-was-taken/ps3-ckit) | C code injection framework for PS3 games | 26 | 🔴 | C |
| [BallanceModLoaderPlus](https://github.com/doyaGu/BallanceModLoaderPlus) | Renovated mod loader for Ballance | 25 | 🟢 | C++ |
| [Cave-Story-Mod-Loader](https://github.com/Clownacy/Cave-Story-Mod-Loader) | DLL mod loader for freeware Cave Story | 25 | 🟢 | C |
| [RogueLibs](https://github.com/Chasmical/RogueLibs) | Modding library for Streets of Rogue | 25 | 🗄️ | C# |
| [SporeModLoader](https://github.com/Rosalie241/SporeModLoader) | Mod loader and manager for Spore | 25 | 🟢 | C++ |
| [ACSE (Cobra engine)](https://github.com/OpenNaja/ACSE) | Script extender for Frontier's Cobra engine games | 24 | 🟢 | Lua |
| [FortRise (TowerFall)](https://github.com/FortRise/FortRise) | Mod loader for TowerFall | 24 | 🟢 | C# |
| [Kuribo](https://github.com/DotKuribo/Kuribo) | Embedded mod loader for Wii games | 24 | 🟡 | C++ |
| [wkRealTime (Worms Armageddon)](https://github.com/rm-rf-worms/wkRealTime) | Real-time online multiplayer for Worms Armageddon | 24 | 🗄️ | C++ |
| [Hell2Modding (Hades II)](https://github.com/SGG-Modding/Hell2Modding) | Mod loader for Hades II | 23 | 🟢 | C++ |
| [m2sdk (Mafia II)](https://github.com/mafia2online/m2sdk) | Software development kit for modding the Steam version of Mafia II | 23 | 🗄️ | C++ |
| [Middle-Earth-Mod-Loader](https://github.com/ReaperAnon/Middle-Earth-Mod-Loader) | Mod loader for Middle-earth: Shadow of War | 23 | 🟢 | C++ |
| [X4-rest-server](https://github.com/Alia5/X4-rest-server) | REST server for X4: Foundations game state | 23 | 🔴 | C++ |
| [CivilizationVI_CommunityExtension](https://github.com/Wild-W/CivilizationVI_CommunityExtension) | Script extender DLL patch for Civilization VI | 22 | 🟡 | C++ |
| [DW2ModLoader](https://github.com/DW2MC/DW2ModLoader) | Mod loader for Distant Worlds 2 | 22 | 🔴 | C# |
| [OpenModManager (A Hat in Time)](https://github.com/mcu8/OpenModManager) | Mod manager and loader for A Hat in Time | 22 | 🟡 | C# |
| [Quintessential (Opus Magnum)](https://github.com/QuintessentialOM/Quintessential) | Mod loader for Opus Magnum | 22 | 🟢 | C# |
| [ror2-modloader](https://github.com/meepen/ror2-modloader) | Mod loader for Risk of Rain 2 | 22 | 🔴 | C# |
| [FallenOrderModLoader](https://github.com/RussellJerome/FallenOrderModLoader) | Loads blueprint pak mods for Star Wars Jedi: Fallen Order | 21 | 🔴 | C++ |
| [Playlunky (Spelunky 2)](https://github.com/spelunky-fyi/Playlunky) | Mod management for Spelunky 2 via DLL injection | 21 | 🟢 | C |
| [PSPModBase](https://github.com/xan1242/PSPModBase) | Plugin base for PSP game modding and code injection | 21 | 🟢 | C |
| [RatataR (Ratatouille)](https://github.com/0x5abe/RatataR) | Custom launcher for Ratatouille (PC) | 21 | 🟢 | C++ |
| [Resident-Doom](https://github.com/Drelvak/Resident-Doom) | Resident Evil 1 gameplay systems ported into GZDoom using the RE1 PC decompilation | 21 | 🟢 | ZenScript |
| [Construction-Set-Extender](https://github.com/shadeMe/Construction-Set-Extender) | OBSE plugin that overhauls the Oblivion Construction Set | 20 | 🟢 | C++ |
| [nier-mod-loader](https://github.com/xxk-i/nier-mod-loader) | Loads CPK mods and DLL plugins into NieR:Automata | 20 | 🔴 | Rust |
| [RED3ext (The Witcher 3)](https://github.com/wopss/RED3ext) | Script extender for REDengine 3 (The Witcher 3) | 20 | 🟡 | C++ |
| [ReturnOfModding](https://github.com/return-of-modding/ReturnOfModding) | Lua mod loader for Risk of Rain Returns | 20 | 🟢 | C++ |
| [Sonic4_ModLoader](https://github.com/OSA413/Sonic4_ModLoader) | Mod loader for Sonic 4 Episode 1 and 2 | 20 | 🟢 | Rust |
| [Bannerlord.BLSE](https://github.com/BUTR/Bannerlord.BLSE) | Bannerlord Software Extender: loader for Mount & Blade II: Bannerlord | 18 | 🟢 | C# |
| [PerfectDarkZeroReworked](https://github.com/zerocoregithub/PerfectDarkZeroReworked) | Controls, gameplay and presentation enhancements for the Perfect Dark Zero recompilation | 18 | 🟢 | C |
| [WorldMachineLoader](https://github.com/ref-err/WorldMachineLoader) | Mod loader for OneShot: World Machine Edition | 17 | 🟢 | C# |
| [holocure-launcher](https://github.com/hcdotnet/holocure-launcher) | Launcher and mod loader for HoloCure | 16 | 🗄️ | C# |
| [Avrix (Project Zomboid)](https://github.com/Brov3r/Avrix) | Java mod loader for Project Zomboid based on Mixins | 15 | 🟢 | Java |
| [Modnix (Phoenix Point)](https://github.com/Sheep-y/Modnix) | Mod loader and manager for Phoenix Point | 14 | 🔴 | C# |
| [CobbAPI (Skyrim)](https://github.com/DavidJCobb/tesv-cobb-api) | Script-extending resource for Skyrim mod authors | 13 | 🔴 | C++ |
| [GML-Mod-Loader](https://github.com/BlurOne-GIT/GML-Mod-Loader) | Mod loader for GameMaker Studio games built on UndertaleModLib | 13 | 🗄️ | C# |
| [holocure-modloader](https://github.com/steviegt6/holocure-modloader) | HoloCure mod loader written in C# | 13 | 🗄️ | C# |
| [deus-ex-coop](https://github.com/cranebeaker/deus-ex-coop) | Co-op play of the Deus Ex campaign over Steam: HX mod fixes and a Steam relay | 12 | 🟢 | UnrealScript |
| [LuckyAPI](https://github.com/ItsVerday/LuckyAPI) | Mod loader for Luck be a Landlord | 11 | 🔴 | GDScript |
| [aoc-mmmod](https://github.com/SiegeEngineers/aoc-mmmod) | DLL mod loader for Age of Empires II: The Conquerors | 10 | 🔴 | C |
| [drg (Deep Rock Galactic)](https://github.com/rkr35/drg) | Injectable DLL for writing custom Deep Rock Galactic modifications | 10 | 🗄️ | Rust |
| [Fireflower](https://github.com/MammaMiaTeam/Fireflower) | Patching toolchain for injecting code into Nintendo DS games | 10 | 🔴 | C++ |
| [Kenshi-Script-Extender](https://github.com/alexliyu7352/Kenshi-Script-Extender) | Script extender for Kenshi | 10 | 🔴 | C |
| [KenshiLua](https://github.com/Genpretz/KenshiLua) | Lua scripting extension for Kenshi | 10 | 🟢 | C++ |
| [MySimsModLoader](https://github.com/ThuverX/MySimsModLoader) | Mod loader for MySims | 9 | 🟢 | C++ |
| [NVSE (Fallout: New Vegas)](https://github.com/ianpatt/nvse) | Original script extender for Fallout: New Vegas | 9 | 🔴 |  |
| [SNKMD](https://github.com/sharpdev-me/SNKMD) | Mod loader for SNKRX | 9 | 🔴 | Lua |
| [jeode](https://github.com/Paficent/jeode) | Mod loader and framework for My Singing Monsters (PC) | 8 | 🟢 | C++ |
| [spacerangershd-fpc-fixes](https://github.com/giantplaceholder/spacerangershd-fpc-fixes) | Patches for the reverse-engineered Space Rangers HD source for Linux and Windows builds | 8 | 🟢 | Batchfile |
| [Winch (DREDGE)](https://github.com/Ashiepaws/Winch) | Harmony-based mod loader for DREDGE | 8 | 🟡 | C# |
| [F1-25-RE-Optimization](https://github.com/xanpavle/F1-25-RE-Optimization) | Runtime renderer optimization for F1 25 via reverse-engineered settings hooks | 7 | 🟢 | C++ |
| [c2-mod-loader (Croc 2)](https://github.com/Zed-z/c2-mod-loader) | ASI mod loader and modding API for Croc 2 | 6 | 🟢 | C |
| [openomori](https://github.com/dazacode/openomori) | Runtime and modding toolkit for OMORI that plays your own copy in the browser | 6 | 🟢 | TypeScript |
| [RL2.ModLoader](https://github.com/RL2-API/RL2.ModLoader) | Mod loader for Rogue Legacy 2 | 6 | 🟢 | C# |
| [Subsystem](https://github.com/Majiir/Subsystem) | Mod loader for Homeworld: Deserts of Kharak | 6 | 🔴 | C# |
| [AsteraLoader](https://github.com/wowo-dot/AsteraLoader) | Plugin loader for Monster Hunter: World (PC) | 5 | 🟢 | C++ |
| [BKRecompRomhackTool](https://github.com/Mr-Wiseguy/BKRecompRomhackTool) | Converts Banjo-Kazooie ROM hacks into Banjo: Recompiled mods | 5 | 🟢 | C++ |
| [GEEcore](https://github.com/wopss/GEEcore) | Core utilities library for building game script extenders | 5 | 🟡 | C++ |
| [KnShim](https://github.com/knot126/KnShim) | Mod loader for Android games (Smash Hit, Granny Smith) | 5 | 🗄️ | C |
| [ps2-modloader](https://github.com/VelocityRa/ps2-modloader) | PS2 modding toolchain experiment | 5 | 🟡 | Assembly |
| [world-of-kartcraft](https://github.com/duxanlol/world-of-kartcraft) | Crash Team Racing kart physics from its decompilation, ported into the benilla WoW client | 5 | 🟢 | Rust |
| [th08-mods](https://github.com/N0zoM1z0/th08-mods) | Gameplay modifiers for Touhou 8, built on its reconstructed source | 3 | 🟢 | C++ |
| [sro_devkit](https://gitlab.com/florian0/sro_devkit) | Whitebox reverse-engineered codebase of the Silkroad Online client |  | ⚪ |  |

## Open-source Game Clones

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Unciv](https://github.com/yairm210/Unciv) | Open-source Android/Desktop remake of Civ V. | 11,486 | 🟢 | Kotlin |
| [Spring (Total Annihilation)](https://github.com/spring/spring) | Open-source remake of Total Annihilation | 4,026 | 🟡 | C++ |
| [Space Station 14](https://github.com/space-wizards/space-station-14) | Space Station 14 is a revived attempt at a Space Station 13 remake. | 3,883 | 🟢 | C# |
| [TrueCraft (Minecraft)](https://github.com/ddevault/TrueCraft) | TrueCraft, a clean-room implementation of Minecraft beta 1.7.3 | 2,455 | 🗄️ | C# |
| [Taisei](https://github.com/taisei-project/taisei) | Fan-made, open-source clone of the Touhou series. | 1,659 | 🟢 | C |
| [Pacman 吃豆游戏](https://github.com/mumuy/pacman) | Open-source remake of Pac-Man | 1,646 | 🟢 | JavaScript |
| [KeeperFX](https://github.com/dkfans/keeperfx) | Open source remake and Fan Expansion of Dungeon Keeper. | 1,028 | 🟢 | C |
| [Command & Conquer - HTML5](https://github.com/adityaravishankar/command-and-conquer) | Open-source remake of Command & Conquer | 810 | 🔴 | JavaScript |
| [pacman (Pac-Man)](https://github.com/daleharvey/pacman) | Open-source remake of Pac-Man | 732 | 🔴 | JavaScript |
| [OpenCiv3](https://github.com/C7-Game/OpenCiv3) | OpenCiv3 is an open-source, cross-platform, mod-oriented, modernized remake of Civilization III by the fan community... | 677 | 🟢 | C# |
| [Duck Hunt JS](https://github.com/MattSurabian/DuckHunt-JS) | Open-source remake of Duck Hunt | 635 | 🟢 | JavaScript |
| [OpenApocalypse](https://github.com/OpenApoc/OpenApoc) | Rebuild of the X-COM: Apocalypse engine. | 601 | 🟢 | C++ |
| [pacman.c (Pac-Man)](https://github.com/floooh/pacman.c) | Pac-Man clone written in C99 | 595 | 🟢 | C |
| [ZQuest Classic](https://github.com/ZQuestClassic/ZQuestClassic) | Open-source remake of Legend of Zelda | 558 | 🟢 | C++ |
| [skifree.js](https://github.com/basicallydan/skifree.js) | Open-source remake of SkiFree | 552 | 🟢 | JavaScript |
| [OpenKeeper](https://github.com/tonihele/OpenKeeper) | Dungeon Keeper II remake in Java. | 510 | 🟢 | Java |
| [openomf](https://github.com/omf2097/openomf) | One Must Fall 2097 Remake. | 489 | 🟢 | C |
| [KaM Remake](https://github.com/Kromster80/kam_remake) | RTS game remake of Knights and Merchants written in Delphi from scratch. | 377 | 🗄️ | Pascal |
| [Dune-II---The-Maker](https://github.com/stefanhendriks/Dune-II---The-Maker) | A remake of the classic Dune 2 - The Building of a Dynasty (by Westwood Studios) with several enhancements. Like: hig... | 372 | 🟢 | C++ |
| [pacman-canvas (Pac-Man)](https://github.com/platzhersh/pacman-canvas) | Open-source remake of Pac-Man | 351 | 🟢 | JavaScript |
| [Romanov's Vengeance](https://github.com/MustaphaTR/Romanovs-Vengeance) | Remake of C&C Red Alert 2 based on the OpenRA engine | 345 | 🟡 | C# |
| [OpenLieroX](https://github.com/openlierox/openlierox) | Open-source remake of Liero | 304 | 🟢 | C++ |
| [Sonic and the Secret Rings (Project Reignition)](https://github.com/kumapauz/project-reignition) | Open-source remake of Sonic and the Secret Rings (Wii) | 303 | 🟢 | C# |
| [CaesarIA (Caesar III)](https://github.com/dalerank/caesaria-game) | Open-source remake of Caesar III | 298 | 🔴 | C |
| [pacman.zig (Pac-Man)](https://github.com/floooh/pacman.zig) | Pac-Man clone written in Zig | 297 | 🟢 | Zig |
| [orona (Bolo)](https://github.com/stephank/orona) | Open-source remake of Bolo | 272 | 🗄️ | CoffeeScript |
| [Syndicate Wars](https://github.com/swfans/syndwarsfx) | Syndicate Wars Fan Expansion, Open Source remake of the classic Bullfrog game. | 265 | 🟢 | C |
| [Counter-Strike-Nintendo-DS](https://github.com/Fewnity/Counter-Strike-Nintendo-DS) | Counter-Strike demake for the Nintendo DS | 240 | 🟢 | C |
| [Lode Runner - Total Recall](https://github.com/SimonHung/LodeRunner_TotalRecall) | Open-source remake of Lode Runner (Arcade) | 234 | 🟡 | JavaScript |
| [Mr.Boom](https://github.com/Javanaise/mrboom-libretro) | 8-player Bomberman clone for RetroArch/Libretro. | 230 | 🟢 | C |
| [vera20k](https://github.com/YuriPlanet/vera20k) | Red Alert 2: Yuri's Revenge — rebuilt from scratch in Rust for large multiplayer battles. | 218 | 🟢 | Rust |
| [GoldenEye: Source](https://github.com/goldeneye-source/ges-code) | Open-source remake of GoldenEye 007 (N64) | 207 | 🗄️ | C++ |
| [PokemonBattleEngine](https://github.com/Kermalis/PokemonBattleEngine) | C# library that emulates Pokémon battles | 189 | 🔴 | C# |
| [freeserf.net](https://github.com/Pyrdacor/freeserf.net) | Settlers 1 clone written in C# | 178 | 🟢 | C# |
| [BattleCity (Battle City)](https://github.com/newagebegins/BattleCity) | Open-source remake of Battle City (Arcade) | 172 | 🟢 | JavaScript |
| [UAlbion](https://github.com/csinkers/ualbion) | Remake of 1995 Albion. | 171 | 🟢 | C# |
| [Enigma (Oxyd)](https://github.com/Enigma-Game/Enigma) | Open-source remake of Oxyd | 170 | 🟢 | C++ |
| [Tails Adventure (Tails Adventure Remake)](https://github.com/mechakotik/tails-adventure) | Open-source remake of Tails Adventure (Game Gear) | 156 | 🟢 | C++ |
| [war1](https://github.com/acoto87/war1) | A remake of Warcraft: Orcs & Humans written in C | 156 | 🟢 | C |
| [OpenGoo (World of Goo)](https://github.com/Mandarancio/OpenGOO) | Open-source remake of World of Goo | 153 | 🔴 | C |
| [OPHD](https://github.com/OutpostUniverse/OPHD) | OutpostHD - Open source remake of Sierra On-Line's Outpost. | 146 | 🟢 | C++ |
| [Mininim (Prince of Persia)](https://github.com/oitofelix/mininim) | Open-source remake of Prince of Persia | 142 | 🔴 | C |
| [TVTower (Mad TV)](https://github.com/TVTower/TVTower) | Open-source remake of Mad TV | 135 | 🟢 | BlitzMax |
| [Armor Alley: Remastered](https://github.com/scottschiller/ArmorAlley) | Open-source remake of Armor Alley | 130 | 🟢 | JavaScript |
| [Survivor (Survivor (1986))](https://github.com/scottschiller/SURVIVOR) | Open-source remake of Survivor (1986) | 129 | 🔴 | JavaScript |
| [OpenKrush](https://github.com/IceReaper/OpenKrush) | Remake of KKnD (Krush, Kill 'n' Destroy) and KKnD2 based on the OpenRA engine | 128 | 🟢 | C# |
| [OpenSA](https://github.com/Dzierzan/OpenSA) | Remake of Swarm Assault based on the OpenRA engine | 124 | 🔴 | C# |
| [Duck Marines](https://github.com/SimonLarsen/duckmarines) | Open-source remake of ChuChu Rocket! (Game Boy) | 122 | 🔴 | Lua |
| [Dope Wars](https://github.com/benmwebb/dopewars) | Open-source remake of Drugwars (DOS) | 118 | 🟢 | C |
| [Iceball (Ace of Spades)](https://github.com/iamgreaser/iceball) | Open-source remake of Ace of Spades | 118 | 🔴 | C |
| [Antares](https://github.com/arescentral/antares) | Remake of Ares, a tactical space combat game. | 113 | 🟢 | C++ |
| [Castle of the Winds in Elm](https://github.com/mordrax/cotwelm) | Open-source remake of Castle of the Winds | 109 | 🟢 | Elm |
| [stuntcarremake (Stunt Car Racer)](https://github.com/ptitSeb/stuntcarremake) | Open-source remake of Stunt Car Racer (C64) | 108 | 🟢 | C++ |
| [Jactorio (Factorio)](https://github.com/jaihysc/Jactorio) | Open-source remake of Factorio | 105 | 🟢 | C++ |
| [Metroid for MMC3](https://github.com/ZaneDubya/MetroidMMC3) | Open-source remake of Metroid (Arcade) | 97 | 🟡 | Assembly |
| [Digger (Boulder Dash)](https://github.com/lutzroeder/digger) | Open-source remake of Boulder Dash (Arcade) | 95 | 🗄️ | HTML |
| [OutRun](https://github.com/ZgzInfinity/OutRun) | Open-source remake of OutRun (PC) | 95 | 🟢 | C++ |
| [janitorial-android (LEGO Junkbot)](https://github.com/1j01/janitorial-android) | Detailed remake of LEGO Junkbot with a level editor | 94 | 🟡 | JavaScript |
| [Orbium (Log!cal)](https://github.com/bni/orbium) | Open-source remake of Log!cal | 90 | 🟡 | JavaScript |
| [Lionheart Remake](https://github.com/b3dgs/lionheart-remake) | Java remake of Lionheart Amiga game. | 87 | 🟢 | Java |
| [Hurrican (Turrican)](https://github.com/HurricanGame/Hurrican) | Open-source remake of Turrican | 86 | 🟢 | C++ |
| [Moon Child (Moon Child FE)](https://github.com/MorsGames/MoonChildFE) | Open-source remake of Moon Child (PC) | 83 | 🟢 | C++ |
| [Shattered Paradise](https://github.com/ABrandau/Shattered-Paradise-SDK) | Remake of C&C Tiberian Sun based on the OpenRA engine | 83 | 🟡 | C# |
| [OpenEtG (Elements)](https://github.com/serprex/openEtG) | Open-source remake of Elements | 82 | 🟢 | Rust |
| [OpenDR (Dark Reign: The Future of War)](https://github.com/drogoganor/OpenDR) | Open-source remake of Dark Reign: The Future of War (Windows) | 78 | 🟢 | C# |
| [BaKGL (Betrayal at Krondor)](https://github.com/xavieran/BaKGL) | Open-source remake of Betrayal at Krondor | 75 | 🟢 | C++ |
| [OpenE2140](https://github.com/OpenE2140/OpenE2140) | Remake of Earth 2140 based on the OpenRA engine | 75 | 🟢 | C# |
| [coUclient (Glitch)](https://github.com/ChildrenOfUr/coUclient) | Open-source remake of Glitch (Web) | 74 | 🗄️ | Dart |
| [FreeRails (Railroad Tycoon)](https://github.com/Trilarion/freerails) | Open-source remake of Railroad Tycoon | 69 | 🟡 | Java |
| [Zatacka X](https://github.com/simenheg/zatackax) | Open-source remake of Achtung, die Kurve! | 69 | 🟡 | C |
| [Dijeweled Remastered](https://github.com/LDinos/Dijeweled) | Open-source remake of Bejeweled (Windows) | 68 | 🟡 | Game Maker Language |
| [Dune 2 - The Maker - Java version](https://github.com/Fundynamic/dune2themaker4j) | Open-source remake of Dune 2 | 63 | 🔴 | Java |
| [rd-131655 (Minecraft)](https://github.com/thecodeofnotch/rd-131655) | Remake of the first version of Minecraft (rd-131655 cave game tech test) | 63 | 🟡 | Java |
| [Imperialism Remake](https://github.com/Trilarion/imperialism-remake) | Open-source remake of Imperialism | 59 | 🔴 | Python |
| [DRRP (Doom RPG)](https://github.com/DRRP-Team/DRRP) | Doom RPG Remake Project, a total conversion of the mobile Doom RPG for GZDoom | 58 | 🔴 | HTML |
| [Alien Breed 3D II The Killing Grounds](https://github.com/mheyer32/alienbreed3d2) | Open-source remake of Alien Breed 3D II: The Killing Grounds (Amiga) | 57 | 🟢 | Assembly |
| [Cattle Bity](https://github.com/dogballs/cattle-bity) | Open-source remake of Battle City (Arcade) | 57 | 🔴 | TypeScript |
| [Digimon World Project Ark](https://github.com/dwProjectark/Digimon-World-Project-Ark) | Open-source remake of Digimon World | 55 | 🔴 | ASP |
| [Exolon](https://github.com/newagebegins/exolon) | Open-source remake of Exolon | 55 | 🔴 | JavaScript |
| [Dungeon Eye](https://github.com/iliak/dungeoneye) | Open-source remake of Eye of the Beholder II (Amiga) | 52 | 🔴 | C# |
| [Encounter (Encounter!)](https://github.com/air/encounter) | Open-source remake of Encounter! (C64) | 52 | 🟢 | JavaScript |
| [FOnline (Fallout Online)](https://github.com/sir-wabbit/fonline) | Open-source remake of Fallout Online | 51 | 🔴 | C |
| [Gods Deluxe](https://github.com/jotd666/gods-deluxe) | Open-source remake of Gods | 51 | 🟡 | Java |
| [Head over Heels](https://github.com/dougmencken/HeadOverHeels) | Open-source remake of Head over Heels | 51 | 🟢 | C++ |
| [Javascript Delta](https://github.com/jakesgordon/javascript-delta) | Open-source remake of Delta (C64) | 51 | 🟡 | JavaScript |
| [Wario-Land-3 (Wario Land 3)](https://github.com/Nearoo/Wario-Land-3) | Open-source remake of Wario Land 3 | 51 | 🔴 | Python |
| [OpenTriad](https://github.com/benjaminfoo/OpenTriad) | Reimplementation of the Triple Triad card game from Final Fantasy VIII | 49 | 🟡 | Java |
| [elifoot98web (Elifoot 98)](https://github.com/elifoot98web/elifoot98web) | Open-source remake of Elifoot 98 (Windows) | 48 | 🟢 | TypeScript |
| [NorseWorld: Ragnarok](https://github.com/Serg-Norseman/NorseWorld-Ragnarok) | Open-source remake of Ragnarok (DOS) | 48 | 🟢 | C# |
| [Shrek 2 Remake](https://github.com/Kaboms/Shrek-2-Remake) | Open-source remake of Shrek 2 (Windows) | 48 | 🟢 | C++ |
| [Gikopoipoi](https://github.com/iccanobif/gikopoi2) | Open-source remake of Gikopoi (Web) | 46 | 🟢 | TypeScript |
| [Hardwar](https://github.com/andrewfenn/Hardwar) | Open-source remake of Hardwar | 45 | 🔴 | C++ |
| [pitfall-js (Pitfall!)](https://github.com/meatfighter/pitfall-js) | Open-source remake of Pitfall! | 45 | 🟡 | TypeScript |
| [DreamZZT](https://github.com/c99koder/DreamZZT) | Open-source remake of ZZT (DOS) | 44 | 🔴 | C |
| [Space Ace IIgs](https://github.com/Olde-Skuul/spaceaceiigs) | Open-source remake of Space Ace (Arcade) | 43 | 🔴 | Python |
| [Wizznic! (Puzznic)](https://github.com/DusteDdk/Wizznic) | Open-source remake of Puzznic | 43 | 🔴 | C |
| [FreedroidClassic (Paradroid)](https://github.com/ReinhardPrix/FreedroidClassic) | Open-source remake of Paradroid (C64) | 42 | 🟢 | C |
| [Castlevania (NES remake)](https://github.com/NearHuscarl/Castlevania) | Remake of Castlevania (NES) block 1 in C++ and DirectX 9 | 41 | 🔴 | C++ |
| [thiefcatcher (Where in the World Is Carmen Sandiego? (1985))](https://github.com/Ponup/thiefcatcher) | Open-source remake of Where in the World Is Carmen Sandiego? (1985) | 40 | 🟢 | C++ |
| [CommandoJS](https://github.com/commandojs/CommandoJS) | Open-source remake of Commando (Arcade) | 39 | 🔴 | JavaScript |
| [OpenReliant](https://github.com/OpenReliant/openreliant) | Rebuild of Starlancer in Zig and SDL3. | 39 | 🟢 | Zig |
| [Dungeon Keeper Remake](https://github.com/Themperror/Dungeon-Keeper-Remake) | A modern remake of Dungeon Keeper | 38 | 🟢 | C++ |
| [Robbo](https://github.com/Zibx/robbo) | Open-source remake of Robbo (C64) | 38 | 🟢 | HTML |
| [Deadly Dave](https://github.com/skoperst/deadly-dave) | Open-source remake of Dangerous Dave (Apple II) | 37 | 🟢 | C |
| [lemmings.js](https://github.com/tomsoftware/lemmings.js) | HTML5 Lemmings remake | 34 | 🔴 | JavaScript |
| [Open Rodent's Revenge](https://github.com/pierreyoda/o2r) | Open-source remake of Rodent's Revenge (Windows) | 34 | 🔴 | C++ |
| [Duck Hunt Remake](https://github.com/dave-symons/duckhunt) | Open-source remake of Duck Hunt | 32 | 🔴 | Python |
| [rebellion2](https://github.com/davidadas/rebellion2) | Remake of the classic Star Wars Rebellion game for PC using Unity | 32 | 🟢 | C# |
| [SeriousSamAlphaRemake](https://github.com/tx00100xt/SeriousSamAlphaRemake) | Serious Sam Alpha Remake open source project based. | 32 | 🟡 | C++ |
| [O21](https://github.com/ForNeVeR/O21) | FOSS remake of U95, an old submarine arcade game from 1995. | 31 | 🟢 | F# |
| [Return of Dr. Destructo](https://github.com/MaxSavenkov/drdestructo2) | Open-source remake of Destructo | 30 | 🔴 | C++ |
| [BananiaJS](https://github.com/BenjaminRi/Banania) | Open-source remake of Banania (Windows) | 29 | 🔴 | JavaScript |
| [Deathlord Relorded](https://github.com/hasseily/Deathlord-Relorded) | Open-source remake of Deathlord (C64) | 29 | 🟢 | C |
| [sccopter (SimCopter)](https://github.com/fr0zi/sccopter) | Open-source remake of SimCopter | 29 | 🔴 | C++ |
| [doom64DS (Doom 64)](https://github.com/svkaiser/doom64DS) | Open-source remake of Doom 64 (N64) | 28 | 🔴 | C |
| [parabellum](https://github.com/andreapavoni/parabellum) | An attempt to build a #Travian 3.x clone written in #Rust. | 28 | 🟢 | Rust |
| [Diggers](https://github.com/Mhatxotic/Diggers) | Open-source remake of Diggers (Amiga) | 27 | 🟢 | Lua |
| [OpenZ](https://github.com/playopenz/OpenZ) | Open-source 3D fan remake of Z (The Bitmap Brothers, 1996) (PC) | 27 | 🟢 | C# |
| [Raptor: Call of the Shadows](https://github.com/aroldanju/raptor-call-of-the-shadows) | Open-source remake of Raptor: Call of the Shadows | 27 | 🔴 | C |
| [warcraft (Warcraft II remake)](https://github.com/paulomenezes/warcraft) | Remake of Warcraft II | 26 | 🔴 | C# |
| [Diamonds](https://github.com/mblaine/Diamonds) | Open-source remake of Diamonds (Apple II) | 25 | 🔴 | C++ |
| [pacman (harto)](https://github.com/harto/pacman) | Open-source remake of Pac-Man | 25 | 🗄️ | JavaScript |
| [Rot Magus](https://github.com/kosinaz/Rot-Magus) | Open-source remake of Magus (DOS) | 25 | 🔴 | JavaScript |
| [Encounter HD](https://github.com/Dhebug/Encounter) | Open-source remake of Encounter | 24 | 🟢 | Assembly |
| [OpenGGS (The Great Giana Sisters)](https://github.com/bugix/OpenGGS) | Open-source remake of The Great Giana Sisters | 23 | 🔴 | C++ |
| [FinFan (Final Fantasy)](https://github.com/aldonunez/FinFan) | Remake of Final Fantasy (NES) | 22 | 🔴 | C++ |
| [Missile Command](https://github.com/chadpaulson/missile-command) | Open-source remake of Missile Command (Arcade) | 22 | 🟡 | Lua |
| [roadfighter (Road Fighter)](https://github.com/ptitSeb/roadfighter) | Open-source remake of Road Fighter | 22 | 🔴 | C++ |
| [Skifree-HTML5-clone](https://github.com/andymason/Skifree-HTML5-clone) | Open-source remake of SkiFree | 22 | 🔴 | JavaScript |
| [Starship Command 2022 Edition](https://github.com/TobyLobster/StarshipCommand2022) | Open-source remake of Starship Command (BBC Micro) | 22 | 🟡 | Assembly |
| [Arashi-JS (Tempest)](https://github.com/stephank/arashi-js) | Open-source remake of Tempest (Arcade) | 21 | 🗄️ | JavaScript |
| [NewSettlers4Project](https://github.com/PaweX/NewSettlers4Project) | Remake of The Settlers IV | 21 | 🔴 | C++ |
| [BlakedAwesomenaughts (Awesomenauts)](https://github.com/zombieman1041/BlakedAwesomenaughts) | Open-source remake of Awesomenauts | 20 | 🔴 | JavaScript |
| [Space Harrier Clone](https://github.com/BrunoAOR/Space-Harrier-Clone) | Open-source remake of Space Harrier (Arcade) | 20 | 🔴 | C |
| [coUserver (Glitch)](https://github.com/ChildrenOfUr/coUserver) | Open-source remake of Glitch (Web) | 19 | 🗄️ | Dart |
| [Pyskool (Skool Daze)](https://github.com/skoolkid/pyskool) | Open-source remake of Skool Daze and Back to Skool (ZX Spectrum) | 19 | 🟢 | Python |
| [Stunt Car Racer](https://github.com/kieranhj/scr-beeb) | Open-source remake of Stunt Car Racer (C64) | 19 | 🔴 | Assembly |
| [XSwing Plus](https://github.com/TobseF/XSwing-Plus) | Open-source remake of Swing | 19 | 🟢 | Java |
| [Aladdin_DirectX](https://github.com/roycephan/Aladdin_DirectX) | Open-source remake of Aladdin | 18 | 🔴 | C++ |
| [boulder-dash (Boulder Dash)](https://github.com/valeriansaliou/boulder-dash) | Open-source remake of Boulder Dash (Arcade) | 18 | 🗄️ | Java |
| [Castle-Combat (Rampart)](https://github.com/karlb/castle-combat) | Open-source remake of Rampart | 18 | 🟢 | Python |
| [Taipan (Taipan!)](https://github.com/ebassett/taipan) | Open-source remake of Taipan! (Apple II) | 18 | 🔴 | C |
| [Castle Adventure](https://github.com/elishacloud/Castle-Adventure) | Open-source remake of Castle Adventure (DOS) | 17 | 🔴 | C |
| [Jet Set Willy 2021 Edition (BBC Micro)](https://github.com/TobyLobster/jsw2021) | Open-source remake of Jet Set Willy (C64) | 17 | 🟡 | C# |
| [OpenMOO2 (Master of Orion 2)](https://github.com/mimi1vx/openmoo2) | Open-source remake of Master of Orion 2 | 17 | 🔴 | Python |
| [splexhd (Supaplex)](https://github.com/radu124/splexhd) | Open-source remake of Supaplex | 17 | 🔴 | C++ |
| [Super Mario Remake](https://github.com/minirop/Super-Mario-Remake) | Open-source remake of Super Mario Bros. (Arcade) | 17 | 🔴 | C |
| [Atari Asteroids](https://github.com/TheBeachLab/asteroids) | Open-source remake of Asteroids | 16 | 🔴 | Python |
| [BloonsTowerDefense6 (Bloons Tower Defense)](https://github.com/wtfaremyinitials/BloonsTowerDefense6) | Open-source remake of Bloons Tower Defense | 16 | 🔴 | Java |
| [Dizgruntled (Gruntz)](https://github.com/Dizgruntled/Dizgruntled) | Open-source remake of Gruntz (Windows) | 16 | 🔴 | TypeScript |
| [Mr.Bomber (Bomberman)](https://github.com/rinrab/mr-bomber) | Open-source remake of Bomberman | 16 | 🟡 | C# |
| [OpenGL Test Drive Remake](https://github.com/capnramses/opengl_test_drive_clone) | Open-source remake of Test Drive | 16 | 🗄️ | C |
| [Phantasy (Phantasy Star)](https://github.com/rafael-esper/Phantasy) | Open-source remake of Phantasy Star (Mega Drive) | 16 | 🔴 | Java |
| [Benno4j (Anno 1602)](https://github.com/stwe/Benno4j) | Unofficial Java remake of Anno 1602 | 15 | 🔴 | Java |
| [Robotron (Robotron: 2084)](https://github.com/Ernir/robotron) | Open-source remake of Robotron: 2084 (Arcade) | 15 | 🔴 | JavaScript |
| [Space Empires 4](https://github.com/lowlevelmetal/OpenSE4) | Spec-based remake of Space Empires 4. | 15 | 🟢 | C++ |
| [Supercars III](https://github.com/jotd666/supercars3) | Open-source remake of Super Cars and Super Cars II (NES) | 15 | 🔴 | Java |
| [terraria-classic](https://github.com/JamzOJamz/terraria-classic) | Remake of Terraria 1.0 | 15 | 🟡 | Zig |
| [UnityPacmania (Pac-Mania)](https://github.com/stuart73/UnityPacmania) | Open-source remake of Pac-Mania (Arcade) | 15 | 🟡 | C# |
| [Jet Lee](https://github.com/Uvadzucumi/JetLee) | Open-source remake of Bruce Lee (C64) | 14 | 🔴 | C++ |
| [pq2 (Progress Quest)](https://github.com/nbollom/pq2) | Open-source remake of Progress Quest | 14 | 🟡 | C++ |
| [ReQbert (Q*bert)](https://github.com/leonicolas/ReQbert) | Open-source remake of Q*bert | 14 | 🔴 | TypeScript |
| [Tyrian Remake](https://github.com/b3dgs/tyrian-remake) | Open-source remake of Tyrian | 14 | 🟢 | Java |
| [aquastax](https://github.com/LongSteve/aquastax) | Open-source remake of Aquastax | 13 | 🔴 | JavaScript |
| [bratwurst](https://github.com/sabetts/bratwurst) | Open-source remake of Bratwurst | 13 | 🔴 | Common Lisp |
| [chipdx (Chip's Challenge)](https://github.com/CasualX/chipdx) | Browser-playable Chip's Challenge remaster | 13 | 🟢 | Rust |
| [donkey_kong_arcade (Donkey Kong)](https://github.com/ianmurfinxyz/donkey_kong_arcade) | Open-source remake of Donkey Kong (Arcade) | 13 | 🔴 | C++ |
| [Kathodos (Descent)](https://github.com/jvranish/Kathodos) | Open-source remake of Descent and Descent II (PlayStation) | 13 | 🔴 | Python |
| [Football Manager](https://github.com/autismuk/Football-Manager) | Open-source remake of Football Manager | 12 | 🔴 | C |
| [KnightOfWor (Wizard of Wor)](https://github.com/Sanguinik/KnightOfWor) | Open-source remake of Wizard of Wor (Arcade) | 12 | 🔴 | Java |
| [Mayhem](https://github.com/devpack/mayhem) | Open-source remake of Mayhem (Amiga) | 12 | 🔴 | C |
| [div-pitfall (Pitfall!)](https://github.com/MikeDX/div-pitfall) | Open-source remake of Pitfall! | 11 | 🔴 | xBase |
| [Duck Rehunt](https://github.com/Serioussam24/Duck-Rehunt) | Open-source remake of Duck Hunt | 11 | 🔴 | Python |
| [galaxian](https://github.com/codedrive/galaxian) | Open-source remake of Galaxian | 11 | 🔴 | ActionScript |
| [Goemon64Remastered](https://github.com/spacefarergames/Goemon64Remastered) | Remake of Mystical Ninja Starring Goemon using data extracted from the ROM | 11 | 🟢 |  |
| [grid-leader (Pole Position)](https://github.com/jonathanopalise/grid-leader) | Open-source remake of Pole Position (Arcade) | 11 | 🗄️ | Python |
| [LGeneral-Deluxe (Panzer General)](https://github.com/AndO3131/LGeneral-Deluxe) | Open-source reimplementation of the Panzer General strategy game | 11 | 🔴 | C |
| [spaceroads (SkyRoads)](https://github.com/sebhd/spaceroads) | Open-source remake of SkyRoads (DOS) | 11 | 🔴 | C++ |
| [Star-Wars-III (Star Wars (1983 arcade game))](https://github.com/abhinandanramesh/Star-Wars-III) | Open-source remake of Star Wars (1983 arcade game) (Arcade) | 11 | 🔴 | Python |
| [BOMBERWARRIORS OF WOR](https://github.com/vranki/Warriors-of-Wor) | Open-source remake of Wizard of Wor (Arcade) | 10 | 🟢 | C++ |
| [Daggerfall.NET (The Elder Scrolls II: Daggerfall)](https://github.com/JohnathanGreen/Daggerfall.NET) | Open-source remake of The Elder Scrolls II: Daggerfall | 10 | 🔴 | C# |
| [DCNebulous (Nebulus)](https://github.com/LemonHaze420/DCNebulous) | Open-source remake of Nebulus (NES) | 10 | 🔴 | C |
| [dodger-remake](https://github.com/funchal/dodger-remake) | Open-source remake of Dodger | 10 | 🔴 | C++ |
| [Enduro tribute](https://github.com/rafaelcastrocouto/enduro) | Open-source remake of Enduro (ZX Spectrum) | 10 | 🔴 | JavaScript |
| [Open Greedy](https://github.com/atroel/open-greedy) | Open-source remake of Pac-Man | 10 | 🔴 | C |
| [openDWU (Distant Worlds: Universe)](https://github.com/jfj-oss/openDWU) | Recreation of Distant Worlds: Universe (1.9.5) in TypeScript and PixiJS | 10 | 🟢 | TypeScript |
| [Rtype (R-Type)](https://github.com/leurqum/Rtype) | Open-source remake of R-Type (Arcade) | 10 | 🔴 | C++ |
| [Scorched Moon](https://github.com/Scorched-Moon/client) | Open-source remake of Moonbase Commander | 10 | 🔴 | Python |
| [shadow-of-the-beast-html5 (Shadow of the Beast)](https://github.com/spleennooname/shadow-of-the-beast-html5) | Open-source remake of Shadow of the Beast (Mega Drive) | 10 | 🟡 | JavaScript |
| [Spongebob_Resurrected_Remake](https://github.com/ParallelProductions/Spongebob_Resurrected_Remake) | Remake of SpongeBob SquarePants: Revenge of the Flying Dutchman | 10 | 🔴 |  |
| [viper](https://github.com/bjornharrtell/viper) | Open-source remake of Viper | 10 | 🗄️ | CoffeeScript |
| [Wizball](https://github.com/craigchandler/wizball-remake) | Open-source remake of Wizball (C64) | 10 | 🟢 | C++ |
| [Archaos (Chaos: The Battle of Wizards)](https://github.com/lewster32/archaos) | Open-source remake of Chaos: The Battle of Wizards (ZX Spectrum) | 9 | 🟢 | TypeScript |
| [c64-nuclearreaction (Nuclear Reaction)](https://github.com/maikmerten/c64-nuclearreaction) | Open-source remake of Nuclear Reaction (Amiga) | 9 | 🔴 | C |
| [CrystalQuest (Crystal Quest)](https://github.com/haleymt/CrystalQuest) | Open-source remake of Crystal Quest | 9 | 🔴 | JavaScript |
| [datastorm (Turmoil)](https://github.com/haroldo-ok/datastorm) | Open-source remake of Turmoil | 9 | 🔴 | C |
| [DXBall (DX-Ball)](https://github.com/nomanHasan/DXBall) | Open-source remake of DX-Ball | 9 | 🔴 | Java |
| [JetPac](https://github.com/ian-wigley/JetPac) | Open-source remake of Jetpac (ZX Spectrum) | 9 | 🟢 | C# |
| [KidChameleonRemake (Kid Chameleon)](https://github.com/mp1011/KidChameleonRemake) | Open-source remake of Kid Chameleon | 9 | 🔴 | C# |
| [Knight Lore](https://github.com/Rasmus-M/Knight-lore) | Open-source remake of Knight Lore (ZX Spectrum) | 9 | 🔴 | Java |
| [Mice Men Remix](https://github.com/synkarius/micemen) | Open-source remake of Mice Men | 9 | 🗄️ | Java |
| [movbizz (Movie Business)](https://github.com/teruk/movbizz) | Open-source remake of Movie Business | 9 | 🔴 | PHP |
| [New Utopia](https://github.com/GameJs/newutopia) | Open-source remake of Utopia | 9 | 🔴 | JavaScript |
| [open-konstruktor](https://github.com/ief015/open-konstruktor) | Remake of the KOHCTPYKTOP: Engineer of the People circuit simulator game | 9 | 🟢 | TypeScript |
| [qpop.js](https://github.com/Frunit/qpop.js) | Reimplementation of the 1995 game Q-Pop in JavaScript | 9 | 🟡 | JavaScript |
| [Space-rangers (Space Rangers)](https://github.com/markevich/Space-rangers) | Open-source remake of Space Rangers | 9 | 🔴 | C# |
| [The Legend of Zelda: A Link to the Past](https://github.com/KaKaShUruKioRa/A-Link-to-the-Past-Project) | Open-source remake of Legend of Zelda - A Link to the Past | 9 | 🟡 | Lua |
| [Z-Steel-Soldiers](https://github.com/sha5b/Z-Steel-Soldiers) | Fan remake of Z (The Bitmap Brothers, 1996) in Godot 4 | 9 | 🟢 | GDScript |
| [Chaos Groove](https://github.com/adamjimenez/ChaosGroove) | Open-source remake of Chaos: The Battle of Wizards (ZX Spectrum) | 8 | 🔴 | C |
| [HTML5-Space-Invaders (Space Invaders)](https://github.com/toivjon/html5-space-invaders) | Open-source remake of Space Invaders | 8 | 🗄️ | JavaScript |
| [open-iw](https://github.com/TambourineReindeer/open-iw) | Remake/rebuild of Sleepless Software's fantasy platformer Inner Worlds. | 8 | 🔴 | C++ |
| [re-Overboard](https://github.com/Beelzenef/re-Overboard) | Remake of the PS1 game Overboard! | 8 | 🔴 | C# |
| [Shining Soul Remake](https://github.com/CharlieIsMyName/ShiningSoulRemake) | Open-source remake of Shining Soul | 8 | 🔴 | Python |
| [AB3D-RTG (Alien Breed 3D)](https://github.com/mheyer32/ab3d-rtg) | Open-source remake of Alien Breed 3D (Amiga) | 7 | 🔴 | Assembly |
| [Elevator Action 500](https://github.com/jotd666/elevator_action) | Open-source remake of Elevator Action (Arcade) | 7 | 🟢 | Assembly |
| [Galaga500](https://github.com/jotd666/galaga) | Open-source remake of Galaga (Arcade) | 7 | 🟢 | C |
| [Gift Grabber](https://github.com/ceva24/gift-grabber) | Open-source remake of Flag Catcher | 7 | 🔴 | JavaScript |
| [jspacman-canvas (Pac-Man)](https://github.com/hguillermo/jspacman-canvas) | Open-source remake of Pac-Man | 7 | 🟡 | JavaScript |
| [l-echo (Echochrome)](https://github.com/LibreGamesArchive/l-echo) | Open-source remake of Echochrome | 7 | 🟡 | C++ |
| [LegionGame](https://github.com/bsoja/LegionGame) | Open-source remake of Legion | 7 | 🔴 | C# |
| [Master-Of-Olympus-Java-Remake](https://github.com/Exiro1/Master-Of-Olympus-Java-Remake) | Java remake of Master of Olympus: Zeus | 7 | 🟢 | Java |
| [pacman (NES)](https://github.com/furrykef/pacman) | Open-source remake of Pac-Man | 7 | 🔴 | Assembly |
| [Stunts](https://github.com/csabahruska/lambdacube-stunts) | Open-source remake of Stunts (Amiga) | 7 | 🔴 | Haskell |
| [Supaxl (Supaplex)](https://github.com/eguneys/supaxl) | Open-source remake of Supaplex | 7 | 🔴 | JavaScript |
| [vr-sentinel](https://github.com/SteveSmith16384/vr-sentinel) | Remake of The Sentinel in VR using Three.js | 7 | 🔴 | JavaScript |
| [xit (X-It)](https://github.com/qfel13/xit) | Open-source remake of X-It | 7 | 🔴 | JavaScript |
| [Alien Breed 3D I](https://github.com/Agrigaatti/Alien-Breed-3D-I) | Open-source remake of Alien Breed 3D (Amiga) | 6 | 🟡 | Assembly |
| [back-to-nature-c64-remake (Frog!)](https://github.com/gborp/back-to-nature-c64-remake) | Open-source remake of Frog! | 6 | 🔴 | Java |
| [Bad Dudes vs Dragonninja](https://github.com/jotd666/baddudes) | Open-source remake of Bad Dudes Vs. DragonNinja (Arcade) | 6 | 🟢 | Python |
| [chainreaction (Nuclear Reaction)](https://github.com/maikmerten/chainreaction) | Open-source remake of Nuclear Reaction (Amiga) | 6 | 🔴 | Java |
| [DetectiveDS](https://github.com/benbaker76/DetectiveDS) | A remake of the original C64 classic The Detective Game for Nintendo DS. | 6 | 🟢 | C++ |
| [F-1 Spirit](https://github.com/ptitSeb/f1spirit) | Open-source remake of F-1 Spirit | 6 | 🔴 | C++ |
| [Historyline (History Line: 1914-1918)](https://github.com/oliverdb/Historyline) | Open-source remake of History Line: 1914-1918 | 6 | 🔴 | C# |
| [Inertia Blast](https://github.com/dulsi/thrust) | Open-source remake of Thrust (C64) | 6 | 🟡 | C |
| [mewl (M.U.L.E.)](https://github.com/LionsPhil/mewl) | Open-source remake of M.U.L.E. | 6 | 🔴 | C++ |
| [nes-caves (Crystal Caves)](https://github.com/DrKylstein/nes-caves) | Open-source remake of Crystal Caves | 6 | 🔴 | Assembly |
| [OpenCurseOfSherwood](https://github.com/esn83/OpenCurseOfSherwood) | Open-source remake of the C64 game The Curse of Sherwood | 6 | 🟡 | C# |
| [openStrato (Stratosphere: Conquest of the Skies)](https://github.com/gerdl/openStrato) | Open-source remake of Stratosphere: Conquest of the Skies | 6 | 🔴 | JavaScript |
| [Re-Logical](https://github.com/BlurOne-GIT/Re-Logical) | Remake of the 1991 Amiga game Logical by Rainbow Arts | 6 | 🟡 | C# |
| [Sea-Wolf (Sea Wolf)](https://github.com/DanJP2016/Sea-Wolf) | Open-source remake of Sea Wolf (Arcade) | 6 | 🔴 | JavaScript |
| [starcup](https://github.com/teamstarcup/starcup) | A fork of the multiplayer game Space Station 14, a remake of the cult-classic Space Station 13. | 6 | 🟢 | C# |
| [A Mouse's Vengeance](https://github.com/maxxboehme/A_Mouses_Vengeance) | Open-source remake of Rodent's Revenge (Windows) | 5 | 🔴 | Java |
| [ascend-free (Ascendancy)](https://github.com/swearfish/ascend-free) | Modern remake of the DOS game Ascendancy | 5 | 🟢 | Go |
| [div-columns](https://github.com/MikeDX/div-columns) | Open-source remake of Columns (Arcade) | 5 | 🔴 | xBase |
| [Donkey Kong 500](https://github.com/jotd666/donkey_kong) | Open-source remake of Donkey Kong (Arcade) | 5 | 🟢 | Assembly |
| [Galaxian500](https://github.com/jotd666/galaxian500) | Open-source remake of Galaxian | 5 | 🟢 | Assembly |
| [Heart-of-Africa-Remake](https://github.com/PatrickVonMassow/Heart-of-Africa-Remake) | Single-player 3D web remake of the 1985 classic The Heart of Africa: real ~1890 geography, living wildlife, period jo... | 5 | 🟢 | JavaScript |
| [Kye for C64](https://github.com/cobbpg/kye-c64) | Open-source remake of Kye (Windows) | 5 | 🔴 | Assembly |
| [luminesk5](https://github.com/kaikai2/luminesk5) | Open-source remake of Lumines | 5 | 🔴 | C |
| [magiccarpet (Magic Carpet)](https://github.com/wonea/magiccarpet) | Open-source remake of Magic Carpet (PlayStation) | 5 | 🔴 | C++ |
| [minerbold (Boulder Dash)](https://github.com/hugeping/minerbold) | Open-source remake of Boulder Dash (Arcade) | 5 | 🔴 | Lua |
| [Open BattleChess](https://github.com/blueveno/openbattlechess) | Open-source remake of Battle Chess | 5 | 🔴 | C# |
| [rust-imperialism](https://github.com/agluszak/rust-imperialism) | Reimplementation of the 1997 strategy game Imperialism in Rust and Bevy | 5 | 🟢 | Rust |
| [Scramble 500](https://github.com/jotd666/scramble500) | Open-source remake of Scramble (Arcade) | 5 | 🟡 | Assembly |
| [sensitive-js](https://github.com/bylexus/sensitive-js) | Open-source remake of Sensitive (C64) | 5 | 🔴 | JavaScript |
| [Telengard Remastered](https://github.com/gondur/Telengard) | Open-source remake of Telengard (C64) | 5 | 🔴 | Visual Basic |
| [TypeScript Xenon](https://github.com/ian-wigley/Xenon) | Open-source remake of Xenon 2 Megablast | 5 | 🟢 | TypeScript |
| [Transarctica-2](https://github.com/SembeiNorimaki/Transarctica-2) | Remake of the classic game Transarctica (In development) | 3 | 🟢 | GDScript |
| [atomiks](https://github.com/carstene1ns/atomiks) | A remake of the classic Atomix game for modern platforms. | 2 | 🟢 | C |
| [galaxy-eggbert](https://github.com/openeggbert/galaxy-eggbert) | 3D remake of Speedy Blupi / Mobile Eggbert, moving from Urho3D toward a native CNA + Easy3D engine. | 2 | 🟢 | C++ |
| [Retro-Arcade-Remakes](https://github.com/danywaked/Retro-Arcade-Remakes) | C++ retro arcade remakes showcasing clean OOP design, game loops, collision systems, and state management. | 2 | 🟢 | C++ |
| [WarhawkDS](https://github.com/benbaker76/WarhawkDS) | Warhawk DS remake of the C64 game Warhawk to the Nintendo DS in native assembler. | 2 | 🟢 | Assembly |
| [AcidDrop](https://github.com/lostjared/AcidDrop) | Remake of classic Atari 2600 game "Acid Drop". | 1 | 🟢 | C++ |
| [blips](https://github.com/joyrider3774/blips) | A Remake of the dos Bips, Bips Gold and Bips Platinum game from Bryant Brownell. It is a Puzzle game which is a varia... | 1 | 🟢 | C++ |
| [wedges-trial](https://github.com/begiedz/wedges-trial) | [WIP] Browser logic puzzle game inspired by Gothic's Remake lockpicking mechanism. | 1 | 🟢 | TypeScript |
| [2004scape](https://2004scape.org) | A free & open-source remake of 2004 era RuneScape 2. |  | ⚪ |  |
| [2009scape](https://2009scape.org) | A free & open-source remake of 2009 era RuneScape 2. |  | ⚪ |  |
| [A Link to the Dream (Link's Awakening)](https://gitlab.com/zeldaforce/zelda-alttd) | Fan remake of The Legend of Zelda: Link's Awakening on the Solarus engine |  | ⚪ |  |
| [Barbarian](http://barbarian.1987.free.fr/indexEN.htm) | Open-source clone of Barbarian: The Ultimate Warrior. |  | ⚪ |  |
| [darknova2](https://github.com/deadjim/darknova2) | Dark Nova ][ — cross-platform space trading game (Space Trader remake) | 0 | 🟢 | Dart |
| [Domino-Chain (Pushover)](https://gitlab.com/domino-chain/domino-chain.gitlab.io) | Open-source remake of the puzzle game Pushover (1992) |  | ⚪ |  |
| [Dune Legacy](https://sourceforge.net/projects/dunelegacy/) | Updated clone of Westood Studios' Dune2 which uses data files from the original game. |  | ⚪ |  |
| [GradiusRemake](https://github.com/luisfae/GradiusRemake) | Remake of the game Gradius (NES - 1986) | 0 | 🟢 | GDScript |
| [guardian](https://github.com/LaughingInPurgatory/guardian) | A modern, endless remake of the classic arcade game Defender | 0 | 🟢 | JavaScript |
| [Maze-Runner-FPS](https://github.com/IbsYoussef/Maze-Runner-FPS) | Remake of classic Maze Runner game from the 70s -- written in Rust | 0 | 🟢 | Rust |
| [Opengate](https://sourceforge.net/projects/opengate/) | Remake of Jumpgate. |  | ⚪ |  |
| [OpenPrivateer](https://openprivateer.org/) | Open-source remake of Wing Commander: Privateer (1993). Requires original game files. |  | ⚪ |  |
| [OrbitalDecay](https://github.com/LeineckerGames/OrbitalDecay) | This is a 3D remake of the old Lunar Lander game | 0 | 🟢 | HTML |
| [Project Wormhole](https://gitlab.com/znixian/xftl) | Rebuild of FTL (Subset Games). Ported to Android in Pocket Wormhole. |  | ⚪ |  |
| [Sunny-Survival-Remake-Code](https://github.com/Kynwi/Sunny-Survival-Remake-Code) | Code for my game called "Sunny Survival Remake" | 0 | 🟢 | C# |
| [Tower Toppler (Nebulus)](https://gitlab.com/roever/toppler) | Open-source remake of Nebulus / Tower Toppler for modern systems |  | ⚪ |  |
| [VoxeLibre](https://git.minetest.land/VoxeLibre/VoxeLibre) | Stable, moddable & free/libre clone of Minecraft based on the Luanti engine. |  | ⚪ |  |
| [Zed Online](https://sourceforge.net/projects/zedonline/) | Remake of the 1996 classic game Z. |  | ⚪ |  |

## Other

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [VoxelSpace](https://github.com/s-macke/VoxelSpace) | Reverse engineered Comanche Voxel Space terrain rendering algorithm | 6,821 | 🟡 | C |
| [libdragon](https://github.com/DragonMinded/libdragon) | libdragon, an open-source Nintendo 64 SDK written without Nintendo's libultra | 1,252 | 🗄️ | C |
| [pspsdk](https://github.com/pspdev/pspsdk) | Open-source PSP SDK for homebrew development, written without Sony's SDK | 1,198 | 🟢 | C |
| [rust-psp](https://github.com/overdrivenpotato/rust-psp) | Rust on the PSP with access to the system libraries | 828 | 🟢 | Rust |
| [GameTracking-Dota2](https://github.com/SteamTracking/GameTracking-Dota2) | Automated tracker of Dota 2 game file and protobuf changes | 770 | 🟢 | C++ |
| [vitaGL](https://github.com/Rinnegatamante/vitaGL) | OpenGL wrapper for PS Vita built on the reverse-engineered sceGxm GPU API | 654 | 🟢 | C |
| [Roblox-Client-Tracker](https://github.com/MaximumADHD/Roblox-Client-Tracker) | Automated tracker extracting information about each Roblox client version | 566 | 🟢 | Assembly |
| [ps2dev](https://github.com/ps2dev/ps2dev) | Open-source PlayStation 2 SDK (ps2sdk and toolchain) written without Sony's SDK | 501 | 🟢 | Shell |
| [Prepare Carefully](https://github.com/edbmods/EdBPrepareCarefully) | EdB Prepare Carefully, a RimWorld mod | 249 | 🟡 | C# |
| [gb-photo](https://github.com/untoxa/gb-photo) | Photo!, a full custom replacement ROM for the Game Boy Camera | 226 | 🟢 | C |
| [psx-spx.github.io](https://github.com/psx-spx/psx-spx.github.io) | Technical reference for the original PlayStation hardware | 166 | 🟢 | Awk |
| [wiki](https://github.com/xboxoneresearch/wiki) | Xbox One research wiki | 154 | 🟢 | Dockerfile |
| [ReversingMinesweeper](https://github.com/repnz/ReversingMinesweeper) | Reverse Engineering Minesweeper: Reconstruct Minesweeper Source Code | 146 | 🔴 | C |
| [x360-research](https://github.com/InvoxiPlayGames/x360-research) | Xbox 360 reverse engineering notes and utilities | 139 | 🟢 |  |
| [prussia](https://github.com/Ravenslofty/prussia) | Prussia, a Rust SDK for the PlayStation 2 | 132 | 🟡 | Rust |
| [Grit Game Engine](https://github.com/grit-engine/grit-engine) | Grit Game Engine | 125 | 🔴 | C++ |
| [2bit-pxlr-studio](https://github.com/HerrZatacke/2bit-pxlr-studio) | Custom ROM for the Game Boy Camera | 110 | 🗄️ | C |
| [botw-re-notes](https://github.com/leoetlino/botw-re-notes) | Reverse engineering notes and tools for Zelda: Breath of the Wild | 110 | 🔴 | C |
| [Chunithm-Research](https://github.com/Suprnova/Chunithm-Research) | In-depth reverse engineering documentation of SEGA Chunithm | 94 | 🔴 |  |
| [VTXCart](https://github.com/xvortex/VTXCart) | Reverse engineering a Neo Geo 161-in-1 cartridge to change ROMs | 90 | 🟡 | C |
| [GameTracking-TF2](https://github.com/SteamTracking/GameTracking-TF2) | Automated tracker of Team Fortress 2 game file changes | 89 | 🟢 | Shell |
| [re_nfpii](https://github.com/GaryOderNichts/re_nfpii) | Reimplementation of the Wii U nn_nfp amiibo library | 88 | 🟡 | C++ |
| [GameTracking-Deadlock](https://github.com/SteamTracking/GameTracking-Deadlock) | Automated tracker of Deadlock game file and protobuf changes | 86 | 🟢 | C++ |
| [ReMasters](https://github.com/kwsch/ReMasters) | Reverse engineering Pokemon Masters | 74 | 🔴 | C# |
| [xbox-tools](https://github.com/JayFoxRox/xbox-tools) | Collection of reverse-engineering tools for the original Xbox | 70 | 🔴 | Python |
| [xbox-board-re](https://github.com/LoveMHz/xbox-board-re) | Board-level reverse engineering of the original Xbox | 62 | 🔴 | Python |
| [3DSort](https://github.com/SalustLab/3DSort) | Rearrange the Nintendo 3DS HOME menu from a PC | 61 | 🟢 | Python |
| [mkw-structures](https://github.com/SeekyCt/mkw-structures) | Documentation of Mario Kart Wii internal structures | 47 | 🟡 | C++ |
| [Super-Mario-64-DS-Remastered](https://github.com/ExcellentGamer/Super-Mario-64-DS-Remastered) | **OPEN SOURCE EPIC** | 46 | 🔴 | C |
| [psp-media-engine-custom-core](https://github.com/mcidclan/psp-media-engine-custom-core) | PSP Media Engine library exposing the ME core's native functions | 41 | 🟢 | C |
| [ExCrypt](https://github.com/emoose/ExCrypt) | Open-source replacement for the Xbox 360 XeCrypt suite | 38 | 🟢 | C |
| [lba-engine-architecture](https://github.com/LBALab/lba-engine-architecture) | Little Big Adventure engine architecture documentation | 35 | 🟡 | Ruby |
| [osdbits](https://github.com/aap/osdbits) | Parts of the PlayStation 2 OSDSYS reverse engineered | 33 | 🟢 | C |
| [nnsdk-rs](https://github.com/ultimate-research/nnsdk-rs) | Unofficial Rust bindings for the Nintendo SDK, used for Switch game modding | 26 | 🟢 | Rust |
| [dump-dvd-kit](https://github.com/XboxDev/dump-dvd-kit) | Tool to dump the ROM of the Xbox DVD Movie Playback Kit dongle | 21 | 🔴 | Python |
| [DarkReignLauncher](https://github.com/Nielk1/DarkReignLauncher) | Tool for Dark Reign: The Future of War game data (osgameclones) (C#) | 19 | 🔴 | C# |
| [psp-media-engine-reload](https://github.com/mcidclan/psp-media-engine-reload) | Unofficial technical documentation and code for the Sony PSP Media Engine | 14 | 🗄️ |  |
| [re-virtua-cop-2](https://github.com/jevarg/re-virtua-cop-2) | Reverse engineering of Virtua Cop 2 PC (1997) | 14 | 🟢 | TypeScript |
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
| [TrinityCore](https://github.com/TrinityCore/TrinityCore) | World of Warcraft server emulator (MaNGOS fork) | 10,843 | 🟢 | C++ |
| [AzerothCore](https://github.com/azerothcore/azerothcore-wotlk) | Modular World of Warcraft 3.3.5a server emulator | 9,094 | 🟢 | C++ |
| [Cuberite](https://github.com/cuberite/cuberite) | Lightweight extensible Minecraft server in C++ | 5,457 | 🟢 | C++ |
| [rAthena](https://github.com/rathena/rathena) | Ragnarok Online server emulator in C++ | 3,630 | 🟢 | C++ |
| [PocketMine-MP](https://github.com/pmmp/PocketMine-MP) | Minecraft Bedrock server software built from scratch in PHP | 3,578 | 🗄️ | PHP |
| [Minestom](https://github.com/Minestom/Minestom) | Lightweight Minecraft Java server written from scratch without vanilla code | 3,310 | 🟢 | Java |
| [Valence](https://github.com/valence-rs/valence) | Rust framework for building Minecraft Java servers | 3,282 | 🟢 | Rust |
| [FerrumC](https://github.com/ferrumc-rs/ferrumc) | Reimplementation of the Minecraft server in Rust | 2,442 | 🟢 | Rust |
| [Impostor](https://github.com/Impostor/Impostor) | Open-source reimplementation of the Among Us game server | 2,373 | 🟢 | C# |
| [Glowstone](https://github.com/GlowstoneMC/Glowstone) | Open-source Minecraft Java server implementation | 2,014 | 🟢 | Java |
| [The Forgotten Server](https://github.com/otland/forgottenserver) | Open Tibia MMORPG server emulator in C++ | 1,844 | 🟢 | C++ |
| [LunarCore](https://github.com/Melledy/LunarCore) | A game server reimplementation for a certain turn-based anime game | 1,433 | 🟢 | Java |
| [YgoMaster](https://github.com/pixeltris/YgoMaster) | Offline Yu-Gi-Oh! Master Duel | 1,392 | 🟢 | C# |
| [Nukkit](https://github.com/CloudburstMC/Nukkit) | Minecraft Bedrock Edition server software in Java | 1,363 | 🟢 | Java |
| [OpenMU](https://github.com/MUnique/OpenMU) | Server for the MMORPG MU Online | 1,249 | 🟢 | C# |
| [HeavenMS](https://github.com/ronancpl/HeavenMS) | MapleStory v83 private server emulator (archived) | 1,216 | 🗄️ | Java |
| [DWC Network Server Emulator](https://github.com/barronwaffles/dwc_network_server_emulator) | Nintendo Wi-Fi Connection server emulator for DS and Wii games | 1,183 | 🟡 | Python |
| [CMaNGOS Classic](https://github.com/cmangos/mangos-classic) | Continued MaNGOS World of Warcraft Classic server emulator | 1,095 | 🟢 | C++ |
| [lunar-tear](https://github.com/Walter-Sparrow/lunar-tear) | Private server research project for a certain discontinued mobile game | 1,091 | 🟢 | Go |
| [MaNGOS Zero](https://github.com/mangoszero/server) | World of Warcraft vanilla server emulator | 1,035 | 🟢 | C++ |
| [Hercules](https://github.com/HerculesWS/Hercules) | Ragnarok Online server emulator | 1,023 | 🟢 | C++ |
| [VMaNGOS](https://github.com/vmangos/core) | Progressive vanilla World of Warcraft server emulator for patches 1.2-1.12 | 967 | 🟢 | C++ |
| [Dragonfly](https://github.com/df-mc/dragonfly) | Minecraft Bedrock Edition server software in Go | 856 | 🟢 | Go |
| [Sapphire](https://github.com/SapphireServer/Sapphire) | Final Fantasy XIV server emulator (4.0+) in C++ | 842 | 🟢 | C++ |
| [ds3os](https://github.com/TLeonardUK/ds3os) | Dark Souls 3 and Dark Souls 2 private server emulator | 787 | 🟢 | CMake |
| [Darkflame Server](https://github.com/DarkflameUniverse/DarkflameServer) | LEGO Universe server emulator | 761 | 🟢 | C++ |
| [ServUO](https://github.com/ServUO/ServUO) | Ultima Online server emulator in C# | 760 | 🟢 | C# |
| [ageLANServer](https://github.com/luskaner/ageLANServer) | Web server and launcher for offline/LAN multiplayer in Age of Empires titles | 749 | 🟢 | Go |
| [Peacock](https://github.com/thepeacockproject/Peacock) | Server replacement for the HITMAN World of Assassination trilogy | 704 | 🟢 | TypeScript |
| [NexusForever](https://github.com/NexusForever/NexusForever) | Server emulator for the defunct MMORPG WildStar | 680 | 🟢 | C# |
| [Canary](https://github.com/opentibiabr/canary) | OpenTibia server emulator for modern Tibia protocol versions | 661 | 🟢 | Lua |
| [PvPGN](https://github.com/pvpgn/pvpgn-server) | Player vs Player Gaming Network: Battle.net and Westwood Online server emulator | 650 | 🟢 | C++ |
| [EQEmu](https://github.com/EQEmu/EQEmu) | EverQuest server emulator | 636 | 🟢 | C++ |
| [flying-squid](https://github.com/PrismarineJS/flying-squid) | Minecraft Java server implemented in Node.js | 611 | 🟢 | JavaScript |
| [EpinelPS](https://github.com/EpinelPS/EpinelPS) | A private server for some anime game | 576 | 🟢 | C# |
| [MHServerEmu](https://github.com/Crypto137/MHServerEmu) | Server emulator for Marvel Heroes | 566 | 🟢 | C# |
| [CMaNGOS WotLK](https://github.com/cmangos/mangos-wotlk) | World of Warcraft 3.3.5 server emulator (C(ontinued)-MaNGOS) | 561 | 🟢 | C++ |
| [CMaNGOS TBC](https://github.com/cmangos/mangos-tbc) | World of Warcraft 2.4.3 server emulator (C(ontinued)-MaNGOS) | 525 | 🟢 | C++ |
| [LandSandBoat](https://github.com/LandSandBoat/server) | Final Fantasy XI server emulator | 513 | 🟢 | Lua |
| [Arcaea-server](https://github.com/Lost-MSth/Arcaea-server) | 一个微型的 Arcaea 本地服务器 A small local server for Arcaea | 493 | 🟢 | Python |
| [OpenCoreMMO](https://github.com/OpenCoreMMO/OpenCoreMMO) | Modern C# MMORPG server emulator for an OpenTibia-style client | 486 | 🟢 | C# |
| [POGOserver](https://github.com/maierfelix/POGOserver) | Pokemon GO server emulator | 479 | 🔴 | JavaScript |
| [PyRoyale](https://github.com/Igoorx/PyRoyale) | Open-source server emulator for the Mario Royale browser game | 456 | 🗄️ | Python |
| [Darkstar Project](https://github.com/DarkstarProject/darkstar) | Deprecated Final Fantasy XI server emulator | 450 | 🗄️ | TSQL |
| [Houdini](https://github.com/solero/houdini) | Club Penguin private server written in Python 3 | 426 | 🟢 | Python |
| [2004Scape server](https://github.com/2004Scape/Server) | Server emulator for RuneScape 2 as it was in 2004 | 387 | 🗄️ | TypeScript |
| [OpenKO](https://github.com/Open-KO/KnightOnline) | Knight Online server and client reimplementation project | 374 | 🟢 | C++ |
| [ModernUO](https://github.com/modernuo/ModernUO) | High-performance Ultima Online server emulator in C# | 362 | 🟢 | C# |
| [ACE](https://github.com/ACEmulator/ACE) | Asheron's Call server emulator | 346 | 🟢 | C# |
| [Kepler](https://github.com/Quackster/Kepler) | Java server reviving Habbo Hotel v14 (2007 era) | 332 | 🟢 | Java |
| [Lost City Server](https://github.com/LostCityRS/Server) | RuneScape 2004-era server emulator | 324 | 🟢 | JavaScript |
| [entralinked](https://github.com/kuroppoi/entralinked) | Standalone Game Sync server emulator for Pokémon Black & White | 323 | 🟢 | Java |
| [Melia](https://github.com/NoCode-NoLife/Melia) | Open-source MMORPG server emulator (Tree of Savior) | 301 | 🟢 | C# |
| [starpoint](https://github.com/duosii/starpoint) | Server emulator for a mobile pinball game. | 292 | 🟡 | TypeScript |
| [bancho.py](https://github.com/osuAkatsuki/bancho.py) | A private osu! server for everyone. Simpler than Akatsuki's production stack, while maintaining core functionality, p... | 287 | 🟢 | Python |
| [newserv](https://github.com/fuzziqersoftware/newserv) | Phantasy Star Online game server, proxy and reverse-engineering tools | 282 | 🟢 | C++ |
| [dndserver](https://github.com/Snaacky/dndserver) | Dark and Darker private server implementation in Python | 274 | 🗄️ | Python |
| [Erupe](https://github.com/Mezeporta/Erupe) | Monster Hunter Frontier server emulator in Go | 274 | 🗄️ | Go |
| [RPCN](https://github.com/RipleyTom/rpcn) | PSN-compatible server used by RPCS3 for online play | 272 | 🟢 | Rust |
| [bemaniutils](https://github.com/DragonMinded/bemaniutils) | Hobby game services network for Konami Bemani arcade games | 265 | 🟢 | Python |
| [RunUO](https://github.com/runuo/runuo) | Classic Ultima Online server emulator in C# | 258 | 🟡 | C# |
| [MCGalaxy](https://github.com/ClassiCube/MCGalaxy) | Minecraft Classic protocol server software | 233 | 🟢 | C# |
| [PayCheck3](https://github.com/SlejmUr/PayCheck3) | Payday 3 server emulator | 216 | 🟢 | C# |
| [Open Toontown](https://github.com/open-toontown/open-toontown) | Open-source Toontown Online based on the final Disney client version | 207 | 🟢 | Python |
| [bravo](https://github.com/bravoserver/bravo) | Reverse engineered Minecraft server implementation (1.4.x protocol) | 205 | 🔴 | Python |
| [Apollo](https://github.com/apollo-rsps/apollo) | RuneScape private server suite in Java | 194 | 🔴 | Java |
| [rsmod](https://github.com/rsmod/rsmod) | Old School RuneScape game server emulator | 193 | 🟡 | Kotlin |
| [OpenSpy Core](https://github.com/openspy/openspy-core) | GameSpy replacement backend services (master server, NAT negotiation, presence) | 192 | 🟢 | C++ |
| [SWGEmu Core3](https://github.com/swgemu/Core3) | Star Wars Galaxies pre-CU server emulator core | 191 | 🟢 | Lua |
| [LawinServer](https://github.com/Lawin0129/LawinServer) | Local single-user Fortnite backend server emulator | 189 | 🟢 | JavaScript |
| [Maple2](https://github.com/MS2Community/Maple2) | Server emulator for MapleStory 2 | 189 | 🟢 | C# |
| [Classic-Brawl](https://github.com/PhoenixFire6934/Classic-Brawl) | Python Brawl Stars server emulator for v26 | 187 | 🟡 | Python |
| [Graphite (Minecraft)](https://github.com/Moulberry/Graphite) | High-performance Minecraft Java Edition server implementation | 181 | 🟡 | Rust |
| [AGS-GC](https://github.com/Anime-Game-Servers/AGS-GC) | A server software implementation, ineroperable with a certain anime game client. The code in this repository is fully... | 178 | 🟢 | Java |
| [aion-server](https://github.com/beyond-aion/aion-server) | Aion server emulator | 177 | 🟢 | Java |
| [cuwo](https://github.com/matpow2/cuwo) | Open server and utilities for Cube World | 173 | 🔴 | C |
| [topaz](https://github.com/project-topaz/topaz) | Final Fantasy XI server emulator | 164 | 🗄️ | Lua |
| [OregonCore](https://github.com/OregonCore/OregonCore) | World of Warcraft 2.4.3 server emulator | 163 | 🔴 | C++ |
| [VanillaReimplementation](https://github.com/Minestom/VanillaReimplementation) | Reimplementation of vanilla Minecraft features on Minestom | 160 | 🗄️ | Java |
| [LawinServerV2](https://github.com/Lawin0129/LawinServerV2) | Fortnite backend emulator with matchmaking and XMPP support | 159 | 🟡 | JavaScript |
| [L2dotNET](https://github.com/Elfocrash/L2dotNET) | Lineage II Interlude server emulator in C# | 157 | 🔴 | C# |
| [UniSpyServer](https://github.com/GameProgressive/UniSpyServer) | Open-source GameSpy backend emulator | 156 | 🟢 | Python |
| [Dawnshard](https://github.com/SapiensAnatis/Dawnshard) | Server emulator for Dragalia Lost | 153 | 🟢 | C# |
| [desse](https://github.com/ymgve/desse) | Demon's Souls private server emulator | 153 | 🔴 | Python |
| [MuEmu](https://github.com/Yomalex/MuEmu) | C# MU Online server supporting multiple client versions | 153 | 🟢 | C# |
| [POL](https://github.com/polserver/polserver) | PenUltima Online server compatible with most Ultima Online clients | 147 | 🟢 | C++ |
| [Nebula](https://github.com/Melledy/Nebula) | A server emulator for the game Stella Sora | 139 | 🟢 | Java |
| [Dawn of Light](https://github.com/Dawn-of-Light/DOLSharp) | Dark Age of Camelot server emulator | 137 | 🟢 | C# |
| [server](https://github.com/sp-tarkov/server) | The Server project for SPT | 134 | 🗄️ | TypeScript |
| [WiiLink WFC Server](https://github.com/WiiLink24/wfc-server) | Nintendo Wi-Fi Connection replacement server by WiiLink | 130 | 🟢 | Go |
| [Kawari](https://github.com/redstrate/Kawari) | Unofficial Final Fantasy XIV server emulator for 7.x | 127 | 🗄️ | Rust |
| [Project Dollhouse](https://github.com/Afr0Games/Project-Dollhouse) | Project Dollhouse, a reimplementation of The Sims Online client and server | 124 | 🟢 | C# |
| [belfast](https://github.com/catgirl-systems/belfast) | Reimplementation of a server for Azur Lane | 120 | 🟢 | Go |
| [Edelstein](https://github.com/Kaioru/Edelstein) | MapleStory v95 server emulator in C# | 115 | 🟢 | C# |
| [zombie-cafe-revival](https://github.com/Airyzz/zombie-cafe-revival) | Reverse engineering and reviving the mobile game Zombie Cafe | 115 | 🟡 | Smali |
| [SeventhUmbral](https://github.com/jpd002/SeventhUmbral) | Final Fantasy XIV v1.23b server emulator | 112 | 🔴 | C |
| [BaPs](https://github.com/gucooing/BaPs) | BaPs | 109 | 🗄️ | Go |
| [Pretendo account server](https://github.com/PretendoNetwork/account) | Replacement Nintendo Network account server for Wii U and 3DS | 108 | 🟢 | TypeScript |
| [quantum-core-x](https://github.com/MeikelLP/quantum-core-x) | Metin2 open source server emulator in C# | 108 | 🟢 | C# |
| [Cypress](https://github.com/PvZ-Cypress/Cypress) | Dedicated servers for Plants vs. Zombies: Garden Warfare 1, 2 and Battle for Neighborville | 106 | 🟢 | C++ |
| [EVESharp](https://github.com/Almamu/EVESharp) | EVE Online server emulator in C# | 104 | 🟡 | C# |
| [Orpheus](https://github.com/aatxe/Orpheus) | Open source MapleStory v83 server emulator | 104 | 🗄️ | Java |
| [kinoko](https://github.com/iw2d/kinoko) | MapleStory v95 server emulator | 102 | 🟢 | Java |
| [butterfly](https://github.com/skogaby/butterfly) | e-amusement server emulator for Dance Dance Revolution A | 99 | 🔴 | Java |
| [Prospect](https://github.com/AeonLucid/Prospect) | Server emulation for The Cycle: Frontier | 98 | 🟡 | C# |
| [Pirates-Online-Rewritten](https://github.com/PiratesOnlineRewritten/Pirates-Online-Rewritten) | Revival of Disney's Pirates of the Caribbean Online with a rewritten server | 96 | 🔴 | Python |
| [RestoRoom](https://github.com/RestoRoom/RestoRoom) | Community reimplementation of the Rec Room servers | 95 | 🟢 |  |
| [AscNet](https://github.com/rafi1212122/AscNet) | Punishing: Gray Raven private server! | 93 | 🟢 | C# |
| [rsc-server (RuneScape Classic)](https://github.com/2003scape/rsc-server) | RuneScape Classic private server emulator | 91 | 🔴 | JavaScript |
| [soapbox-race-core](https://github.com/SoapboxRaceWorld/soapbox-race-core) | Need for Speed: World server emulator core | 90 | 🔴 | Java |
| [_archive_lineage2js](https://github.com/space2pacman-misc/_archive_lineage2js) | Node.js Lineage 2 server emulator (Chronicle 1) | 88 | 🗄️ | JavaScript |
| [SphereServer Source-X](https://github.com/Sphereserver/Source-X) | Ultima Online server emulator | 86 | 🟢 | C |
| [server-csharp](https://github.com/sp-tarkov/server-csharp) | A C# rewrite of the SPT server project. | 85 | 🗄️ | C# |
| [SharpMC (Minecraft)](https://github.com/SharpMC/SharpMC) | SharpMC, a Minecraft server written in C# | 82 | 🔴 | C# |
| [oxide](https://github.com/T-x-T/oxide) | Reimplementation of the Minecraft server in pure Rust | 79 | 🟢 | Rust |
| [NetspherePirates](https://github.com/wtfblub/NetspherePirates) | Experimental S4 League server emulator | 78 | 🗄️ | C# |
| [BlueRebirth](https://github.com/LunarConcerto/BlueRebirth) | Offline restoration project for a discontinued mobile game | 75 | 🟢 | C# |
| [UOX3](https://github.com/UOX3DevTeam/UOX3) | Ultima Offline eXperiment 3 Ultima Online server emulator | 75 | 🟢 | C++ |
| [Juxtaposition](https://github.com/PretendoNetwork/juxtaposition) | Pretendo's Miiverse replacement service for Wii U and 3DS | 74 | 🟢 | TypeScript |
| [Bayshore](https://github.com/ProjectAsakura/Bayshore) | Server reimplementation for Wangan Midnight Maximum Tune 6 | 71 | 🟢 | TypeScript |
| [DBOGLOBAL](https://github.com/dboglobal/DBOGLOBAL) | Dragon Ball Online Global client and server emulator | 71 | 🟡 | C++ |
| [Hitman-5-Server](https://github.com/LennardF1989/Hitman-5-Server) | Emulated server for Hitman: Absolution and Hitman: Sniper Challenge | 70 | 🗄️ | HTML |
| [OpenDAoC](https://github.com/OpenDAoC/OpenDAoC-Core) | Free Dark Age of Camelot server emulator | 69 | 🟢 | C# |
| [Hoshimi](https://github.com/Enigfrank/Hoshimi) | Unofficial local game emulation server for Hoshimi | 68 | 🟢 | PowerShell |
| [w3l](https://github.com/w3lh/w3l) | Warcraft III loader that connects the game to PvPGN Battle.net servers | 67 | 🔴 | C |
| [perlica-rs](https://github.com/Yoshk4e/perlica-rs) | A server software reimplementation for an old version of a certain anime game about factories. | 66 | 🟢 | Rust |
| [mxoemu](https://github.com/rajkosto/mxoemu) | Server emulator for the shut-down MMO The Matrix Online | 65 | 🔴 | C |
| [NFS-Online-Server](https://github.com/moio9/NFS-Online-Server) | Online server emulator for NFS Most Wanted, Underground 2 and Carbon | 61 | 🟢 | Python |
| [ZOVserver](https://github.com/ZOVserver/ZOVserver) | Private server emulator for Brawl Stars v24 in C# | 61 | 🟢 | C# |
| [cwk-server](https://github.com/shishkabob27/cwk-server) | Reverse engineered server for Card Wars Kingdom | 60 | 🗄️ | Python |
| [Freya](https://github.com/ubis/Freya) | Cabal Online server emulator | 60 | 🟡 | Go |
| [puniemu](https://github.com/SuperTavor/puniemu) | Server emulator for Yo-kai Watch Puni Puni | 60 | 🟢 | C# |
| [rsc-client (RuneScape Classic)](https://github.com/2003scape/rsc-client) | RuneScape Classic web client | 60 | 🔴 | JavaScript |
| [DragonFable-Private-Server](https://github.com/hiperesp/DragonFable-Private-Server) | DragonFable private server emulator for the current client | 59 | 🟢 | PHP |
| [OpenRS2](https://github.com/openrs2/openrs2) | Open-source multiplayer game server compatible with the RuneScape client | 59 | 🟢 | Kotlin |
| [titanic](https://github.com/osuTitanic/titanic) | A private server that supports all osu! clients (2007-2026) | 59 | 🟢 | Go |
| [remielle](https://github.com/thexeondev/remielle) | Zenless Zone Zero server emulator focused on efficiency, stability and correctness. | 56 | 🟢 | Zig |
| [CycloneIO](https://github.com/itsezc/CycloneIO) | HTML5 Habbo Hotel package with server, client and CMS | 55 | 🔴 | TypeScript |
| [topaz](https://github.com/topaz-next/topaz) | Server emulator for Final Fantasy XI | 55 | 🗄️ | Lua |
| [Cubic Server](https://github.com/CubicMC/cubic-server) | Minecraft server implementation in C++ | 54 | 🟡 | C++ |
| [dream-server](https://github.com/NDSLink/dream-server) | Server for Pokemon Dream World | 54 | 🔴 | SCSS |
| [Maelstrom](https://github.com/Rawaho/Maelstrom) | Server emulator for Final Fantasy XIV (Stormblood 4.10) | 54 | 🔴 | C# |
| [BetrockPlusPlus](https://github.com/OpenBetaGroup/BetrockPlusPlus) | Minecraft Beta 1.7.3 compatible server written in C++ | 53 | 🟢 | C++ |
| [Hardline Dreams](https://github.com/hdneo/mxo-hd) | C# server emulator for The Matrix Online | 53 | 🟢 | C# |
| [Infantry-Online-Server](https://github.com/InfantryOnline/Infantry-Online-Server) | Free Infantry Online server emulator | 53 | 🟢 | C# |
| [NTRSimulator](https://github.com/raphaeIl/NTRSimulator) | Server Emulator for a certain NTR game | 53 | 🟢 | C# |
| [Holocore](https://github.com/ProjectSWGCore/Holocore) | Star Wars Galaxies server emulator for the JVM | 52 | 🟢 | Kotlin |
| [Sunrise](https://github.com/SunriseCommunity/Sunrise) | 🌅 Sunrise - osu! server written in C# | 52 | 🟢 | C# |
| [wrath-rs](https://github.com/Victov/wrath-rs) | A very functionally incomplete World of Warcraft: Wrath of the Lich King server emulator written in pure rust. | 52 | 🟢 | Rust |
| [Maple2](https://github.com/kOchirasu/Maple2) | Server emulator for MapleStory 2 | 51 | 🟡 | C# |
| [Modern-Brawl](https://github.com/PhoenixFire6934/Modern-Brawl) | Python Brawl Stars server emulator for version 28.189 | 51 | 🔴 | Python |
| [tpp-server-emulator](https://github.com/alicealys/tpp-server-emulator) | Reimplementation of the Metal Gear Solid V: The Phantom Pain backend server | 50 | 🟢 | C++ |
| [LibreKO](https://github.com/ZeusAFK/LibreKO) | From-scratch reimplementation of the Knight Online game server and client | 49 | 🟢 | C# |
| [waygate-server](https://github.com/vswarte/waygate-server) | Elden Ring custom matchmaking server implementation | 48 | 🟢 | Rust |
| [XboxLive.Server](https://github.com/zzVertigo/XboxLive.Server) | Revival server for Xbox Live 1.0 | 44 | 🗄️ | C# |
| [OpenBachelorS](https://github.com/pfyy/OpenBachelorS) | OpenBachelorS | 43 | 🟢 | Python |
| [protanki-server](https://github.com/Assasans/protanki-server) | Open-source reimplementation of the ProTanki server | 43 | 🗄️ | Kotlin |
| [SporeServer](https://github.com/Rosalie241/SporeServer) | A WIP Spore Server Replacement | 42 | 🟡 | C# |
| [DIRTSAND (Myst Online: Uru Live)](https://github.com/H-uru/dirtsand) | Server reimplementation for Myst Online: Uru Live (D'ni in Real-Time Server) | 41 | 🟢 | C++ |
| [LuxonServer](https://github.com/niansa/LuxonServer) | Clean-room reimplementation of the Photon LoadBalancing server | 41 | 🟢 | C |
| [Pocket Relay](https://github.com/PocketRelay/Server) | Mass Effect 3 EA Blaze server emulator for LAN and WAN play | 41 | 🟢 | Rust |
| [shiro](https://github.com/mellowagain/shiro) | High-performance osu! Bancho server re-implementation in C++ | 40 | 🗄️ | C++ |
| [azerust](https://github.com/arlyon/azerust) | An experimental World of Warcraft emulator in Rust | 39 | 🟡 | Rust |
| [g0v0-server](https://github.com/GooGuTeam/g0v0-server) | An osu!(lazer) private server that is easy to deploy, highly scalable, and fully featured to meet diverse operational... | 39 | 🟢 | Python |
| [ProjectObsidian (Minecraft Classic)](https://github.com/EdwardJXLi/ProjectObsidian) | Minecraft Classic server software written in Python | 39 | 🟡 | Python |
| [PTCGP-Private-Server](https://github.com/Layen-lang/PTCGP-Private-Server) | Unofficial local compatibility server and profile editor for Pokémon TCG Pocket | 38 | 🟢 | Go |
| [2006rebotted](https://github.com/dginovker/2006rebotted) | A 2006 RuneScape 2 Emulation Server. | 36 | 🔴 | Java |
| [summit (World of Warcraft)](https://github.com/paalgyula/summit) | World of Warcraft server emulator written in Go | 36 | 🟢 | Go |
| [EVEmu](https://github.com/evemuproject/evemu_crucible) | EVE Online server emulator for the Crucible client | 32 | 🔴 | C++ |
| [OpenPayload](https://github.com/CLF78/OpenPayload) | Open-source reimplementation of the Wiimmfi payload for Mario Kart Wii | 30 | 🟡 | C++ |
| [sonetto-rs](https://github.com/Yoshk4e/sonetto-rs) | a server software re-implementaion for R1999 | 30 | 🗄️ | Rust |
| [d2-research](https://github.com/isinternets/d2-research) | Research report on reconstructing the archived Destiny 2 build 86657 client (Sunrise/Dawn) | 29 | 🟢 | Python |
| [Atlas](https://github.com/BNETDocs/Atlas) | Server that emulates Classic Battle.net for Diablo, StarCraft and Warcraft II/III | 28 | 🟢 | C# |
| [BlazeServer](https://github.com/pedromartins1/BlazeServer) | EA Blaze server emulator for Battlefield 3 | 27 | 🔴 | C# |
| [DoctoratePy](https://github.com/nonobject14514/DoctoratePy) | DoctoratePy | 26 | 🔴 | Python |
| [Batla-3D-server-emu](https://github.com/Serega25511s/Batla-3D-server-emu) | Clean-room server emulator for the shut-down arena shooter Batla 3D | 25 | 🟢 | C# |
| [Orchis](https://github.com/CerisWhite/Orchis) | A Dragalia Lost Private Server | 25 | 🟢 | JavaScript |
| [Roseau](https://github.com/Quackster/Roseau) | Habbo Hotel emulator for the 2001 v1 client | 24 | 🟢 | Java |
| [wow_vanilla_server](https://github.com/gtker/wow_vanilla_server) | WIP Rust server for WoW 1.12 | 23 | 🟡 | Rust |
| [Habbo](https://github.com/jadenmitchell/Habbo) | Habbo Hotel server for the Flash production client | 22 | 🔴 | JavaScript |
| [OT6-Reconstruction](https://github.com/ApfelTeeSaft/OT6-Reconstruction) | Decompilation of Fortnite Alpha (2016) game server logic | 22 | 🟢 | C++ |
| [enigma](https://github.com/yoncodes/enigma) | server for that one card game | 21 | 🟢 | Rust |
| [HavanaR39](https://github.com/jeppe9821/HavanaR39) | Habbo Hotel R39 server emulator | 21 | 🟡 | Java |
| [KazusaGI_cb2](https://github.com/Hiro420/KazusaGI_cb2) | Server sofware reimplementation for an old version of a certain anime game | 19 | 🟢 | C# |
| [mooege](https://github.com/mooege/mooege) | Educational Diablo III game server emulator | 19 | 🔴 |  |
| [Lolo](https://github.com/BanterSR/Lolo) | 开放空间/OverField 服务端部分实现 | 18 | 🟢 | JavaScript |
| [SadieEmulator](https://github.com/sadie-group/SadieEmulator) | Habbo Hotel emulation server | 18 | 🟢 | C# |
| [assettocorsa_competizione_server](https://github.com/renaudallard/assettocorsa_competizione_server) | Assetto Corsa Competizione server | 17 | 🟢 | C |
| [habbokt](https://github.com/ultraviolet-jordan/habbokt) | Habbo Hotel v31 private server in Kotlin | 17 | 🔴 | HTML |
| [spikewall](https://github.com/Ramen2X/spikewall) | An open source server for the defunct 2015 mobile game Sonic Runners. | 17 | 🟢 | C# |
| [VirtueOS (Old School RuneScape)](https://github.com/clienthax/VirtueOS) | VirtueOS, an Old School RuneScape private server | 16 | 🔴 | Java |
| [Z7](https://github.com/Khysnik/Z7) | Reverse-engineered Blaze server for Plants vs Zombies: Garden Warfare 2 | 16 | 🟢 | C++ |
| [d3b-emu](https://github.com/Crypto137/d3b-emu) | Server emulator for the Diablo 3 beta client | 15 | 🟡 | C# |
| [HayDay-1.5.42](https://github.com/frmnnet/HayDay-1.5.42) | Open-source private server for Hay Day 1.5.42 | 14 | 🟢 | Python |
| [Shittim-Server](https://github.com/KiyoEditz/Shittim-Server) | Private server for Blue Archive (Steam) | 14 | 🟢 | C# |
| [of-ps](https://github.com/byzp/of-ps) | overfield emu server | 12 | 🟢 | Python |
| [SharpMC-Rewritten (Minecraft)](https://github.com/SharpMC/SharpMC-Rewritten) | Rewritten SharpMC Minecraft Java Edition 1.11 server in C# | 12 | 🔴 | C# |
| [blaze-server](https://github.com/squaredx/blaze-server) | Battlefield 3 LAN server emulator | 11 | 🔴 | C# |
| [OpenLethe](https://github.com/LEAGUE-OF-NINE/OpenLethe) | OpenLethe | 11 | 🟢 | C# |
| [hk4e-go](https://github.com/Kei-Luna/hk4e-go) | 世҉̰̗͕́͢͡界҈̧̟͙̖̎̎̕遗҈͚̄̓̍̕͜忘҈̢͕̙̪̄͞我҉̛̰̯̊͢ | 9 | 🟡 | Go |
| [KazusaHSR_0.56](https://github.com/Hiro420/KazusaHSR_0.56) | Open-source server reimplementation for an early version of an anime game with stars and rails | 8 | 🟢 | C# |
| [Mystic-Nights-Online](https://github.com/jeremydecola/Mystic-Nights-Online) | Reverse-engineered multiplayer private server for the PS2 game Mystic Nights | 8 | 🟡 | Python |
| [ew](https://github.com/ethanaobrien/ew) | A sif2 server | 7 | 🟢 | Rust |
| [gaucho](https://github.com/co-stuff/gaucho) | Conquer Online private server skeleton | 7 | 🟢 | Rust |
| [MOULArs (Myst Online: Uru Live)](https://github.com/zrax/moulars) | Myst Online: Uru Live server written in Rust | 7 | 🟢 | Rust |
| [UberStrike-Reverse-Engineered](https://github.com/festivaldev/UberStrike-Reverse-Engineered) | Reverse-engineered UberStrike client and server | 7 | 🟡 | C# |
| [Snowlight](https://github.com/xTYTY/Snowlight) | Habbo Hotel emulator in C# .NET 4.0 | 6 | 🔴 | C# |
| [vsro-server-decomp](https://github.com/skillman1337/vsro-server-decomp) | C++ reconstruction of Silkroad Online's SR_GameServer | 6 | 🟢 | C++ |
| [Finlay](https://github.com/Quackster/Finlay) | Habbo Hotel emulator for the V9 protocol, based on Kepler | 5 | 🗄️ | Java |
| [Pangya-Mobile](https://github.com/victti/Pangya-Mobile) | Private server for the shut-down mobile game Pangya Mobile | 5 | 🟢 | TypeScript |
| [D2DBSDotNet](https://github.com/tesseract2048/D2DBSDotNet) | C# reconstruction of d2dbs, the Diablo II database server from bnetd/PvPGN | 4 | 🔴 | C# |
| [garcia](https://github.com/yoncodes/garcia) | server for a random 2d game | 2 | 🟢 | Rust |
| [dev_wow_auth_server](https://github.com/gtker/dev_wow_auth_server) | World of Warcraft authentication server for development | 1 | 🟡 | Rust |
| [2009scape](https://gitlab.com/2009scape/2009scape) | Open-source 2009-era RuneScape server remake |  | ⚪ |  |
| [ACEmulator](https://emulator.ac) | A custom, completely from-scratch open source server emulator for Asheron’s Call built on C#. |  | ⚪ |  |
| [mw-tools](https://gitlab.com/wander-gr/mw-tools) | Unofficial Myth War I server and tools |  | ⚪ |  |
| [Open RSC (RuneScape Classic)](https://gitlab.com/openrsc/openrsc) | Server and client framework that recreates RuneScape Classic |  | ⚪ |  |
| [opengallop](https://codeberg.org/mambosaba/opengallop) | Game server reimplementation for Umamusume (global region) |  | ⚪ |  |
| [zcure](https://gitlab.com/blrevive/zcure) | Server for Blacklight: Retribution 3.02 based on the decompiled ZCure library |  | ⚪ |  |

## Static Recompilations & PC Ports

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [N64Recomp](https://github.com/N64Recomp/N64Recomp) | Static recompiler that turns N64 binaries into portable C code | 8,295 | 🟢 | C++ |
| [Zelda64Recomp](https://github.com/Zelda64Recomp/Zelda64Recomp) | Static recompilation of Majora's Mask for PC | 7,521 | 🟢 | C |
| [XenonRecomp](https://github.com/hedge-dev/XenonRecomp) | Converts Xbox 360 PowerPC executables into C++ for recompilation on modern platforms | 6,618 | 🟡 | C++ |
| [dusk](https://github.com/TwilitRealm/dusklight) | Twilight Princess PC port based on the zeldaret tp decompilation | 6,062 | 🟢 | C++ |
| [UnleashedRecomp](https://github.com/hedge-dev/UnleashedRecomp) | Unofficial PC port of Xbox 360 Sonic Unleashed via static recompilation | 5,265 | 🟢 | C++ |
| [D2R Mobile](https://github.com/jhaizhou-ops/d2r-mobile) | Runs the Switch build of Diablo II: Resurrected natively on iPhone, iPad and Apple silicon Macs | 4,598 | 🟢 | C |
| [BloodBorne for Windows](https://github.com/Supermedo/bloodborne_pc) | Recomp of BloodBorne (PS4) to Windows. | 4,580 | 🟢 | C++ |
| [gen1recomp](https://github.com/bryanthaboi/gen1recomp) | Native recompilation of Pokemon Red/Blue/Yellow with mods | 4,035 | 🟢 | Lua |
| [Diablo (diabloweb)](https://github.com/d07RiV/diabloweb) | Browser (WebAssembly) port of Diablo (PC) | 2,892 | 🔴 | JavaScript |
| [SpaghettiKart](https://github.com/HarbourMasters/SpaghettiKart) | Mario Kart 64 PC port based on the mk64 decompilation, with track editor | 2,447 | 🟢 | C |
| [P.T. for PC](https://github.com/LoreanXavier/pt-pc) | Native PC port of Kojima's P.T. with game logic rebuilt in C++, runs from your own PS4 files | 2,167 | 🟢 | C++ |
| [Starship](https://github.com/HarbourMasters/Starship) | Star Fox 64 PC port based on the sf64 decompilation | 2,119 | 🟢 | C |
| [BanjoRecomp](https://github.com/BanjoRecomp/BanjoRecomp) | Banjo-Kazooie static recompilation with mod support | 2,088 | 🟢 | C |
| [N64RecompLauncher](https://github.com/SirDiabo/GithubLauncher) | Installs and updates N64 static recompilation ports in one place | 1,975 | 🟢 | C# |
| [Uncharted: The Nathan Drake Collection](https://github.com/Supermedo/uncharted_pc) | Unofficial native port of Uncharted: The Nathan Drake Collection (PS4) | 1,945 | 🟢 | C++ |
| [sm64ex](https://github.com/sm64pc/sm64ex) | Super Mario 64 PC port fork focused on easier modding | 1,873 | 🟡 | C |
| [OpenCE](https://github.com/OpenCommunityEdition/OpenCE) | Enhanced recomp of the original Xbox Halo: Combat Evolved to all Windows, Linux and Android. | 1,809 | 🟢 | C |
| [LASRecomp](https://github.com/peiikai/LASRecomp) | Static recompilation of Link's Awakening (Switch) to native macOS and Windows | 1,776 | 🟢 | C |
| [skate3recomp](https://github.com/mchughalex/skate3recomp) | Native Windows/Linux/macOS port of Skate 3 via static recompilation | 1,723 | 🟢 | C++ |
| [rt64](https://github.com/rt64/rt64) | N64 graphics renderer used by emulators and native recomp ports | 1,626 | 🟢 | C++ |
| [ACGC-PC-Port](https://github.com/flyngmt/ACGC-PC-Port) | Animal Crossing (GameCube) PC port from the ac-decomp decompilation | 1,517 | 🟢 | C |
| [sm64coopdx](https://github.com/coop-deluxe/sm64coopdx) | Online multiplayer Super Mario 64 PC port based on the decompilation | 1,483 | 🟢 | C |
| [Shadow of the Colossus](https://github.com/AjncSystem/ShadowOfTheColossus-PC) | Unofficial native port of Shadow of the Colossus (PS4) | 1,470 | 🟢 | C++ |
| [REDRIVER2](https://github.com/OpenDriver2/REDRIVER2) | Driver 2 PlayStation reverse engineering and PC port | 1,430 | 🟢 | C |
| [SavageWindRecomp](https://github.com/Revivedx/SavageWindRecomp) | Static recompilation of Zelda: Breath of the Wild (Switch 1.8.2) for Windows and Linux | 1,299 | 🟢 | C |
| [ps2-web-recomp](https://github.com/snuri00/ps2-web-recomp) | PS2 games statically recompiled to WebAssembly with a native runtime to run in the browser | 1,282 | 🟢 | C++ |
| [Mario Kart Wii](https://github.com/patchzyy/Wiicompiled) | Unofficial native port of Mario Kart Wii (Wii) | 1,265 | 🟢 | C# |
| [ReXGlue SDK](https://github.com/rexglue/rexglue-sdk) | SDK for static recompilation of Xbox 360 games from PowerPC to portable C++ | 1,168 | 🟢 | C |
| [isle-portable](https://github.com/isledecomp/isle-portable) | Portable LEGO Island source port built from the isle decompilation | 1,079 | 🟢 | C++ |
| [ZeldaWWHDRecomp](https://github.com/ZeldaWWHDRecomp/ZeldaWWHDRecomp) | Static recompilation of The Wind Waker HD (Wii U) | 1,046 | 🟢 | C++ |
| [Bloodborne](https://github.com/Awakenchan/LanternEngine) | Unofficial native port of Bloodborne (PS4) | 1,026 | 🟢 | C++ |
| [WipEout Phantom Edition](https://github.com/wipeout-phantom-edition/wipeout-phantom-edition) | WipEout PC port that runs from the original disc image | 985 | 🟡 |  |
| [SymphonyRecomp](https://github.com/BlackLabelHQ/SymphonyRecomp) | Static recompilation of Castlevania: Symphony of the Night | 976 | 🟢 | C# |
| [GoldenEye-Recomp](https://github.com/SunJaycy/GoldenEye-Recomp) | Recompilation of the cancelled Xbox 360 GoldenEye 007 for PC | 908 | 🟢 | C |
| [pinyon-shift](https://github.com/arcanite24/pinyon-shift) | A playable preview of Forza Horizon static recompilation | 893 | 🟢 | Python |
| [devilution-nx](https://github.com/lantus/devilution-nx) | Diablo port for Nintendo Switch based on Devilution | 890 | 🔴 | C++ |
| [inFAMOUS Second Son](https://github.com/HayatoG/iss_pc) | Unofficial native port of inFAMOUS Second Son (PS4) | 884 | 🟢 | C++ |
| [Ghostship](https://github.com/HarbourMasters/Ghostship) | Harbour Masters Super Mario 64 source port with mods and modern graphics | 853 | 🟢 | C |
| [Blue Dragon (re:Blue)](https://github.com/zolaware/reblue) | Xbox 360 static recompilation of Blue Dragon (re:Blue) | 843 | 🟢 | C++ |
| [LostOdysseyRecomp](https://github.com/freefrank/LostOdysseyRecomp) | Experimental native PC port of Lost Odyssey using static recompilation. No game assets included. | 804 | 🟢 | C++ |
| [The Legend of Zelda: The Minish Cap based on Project Picori port](https://github.com/EstebanPdN/zelda-tmc-3ds) | Native Nintendo 3DS port of The Legend of Zelda: The Minish Cap based on Project Picori | 778 | 🟢 | C |
| [Silent Hill native PC port](https://github.com/SlickAmogus/silent-hill-decomp) | Multiplatform port of the Silent Hill 1 PSX decompilation | 763 | 🟢 | C |
| [Black (Black - XBE Recomp)](https://github.com/TGP482/BLACK-XBERecomp) | Static recompilation of Black (og xbox) into a native PC port | 738 | 🟢 | C++ |
| [zelda-alttp-3ds](https://github.com/EstebanPdN/zelda-alttp-3ds) | Nintendo 3DS port of Zelda: A Link to the Past based on zelda3 | 732 | 🟢 | C |
| [Mario Kart Wii](https://github.com/chrissotraidis/kartpad) | Unofficial native port of Mario Kart Wii (Wii) | 712 | 🟢 | Python |
| [Marathon Recompiled](https://github.com/sonicnext-dev/MarathonRecomp) | Static recompilation PC port of Sonic the Hedgehog (2006) | 705 | 🟢 | C++ |
| [The Legend of Zelda: Ocarina of Time](https://github.com/blawar/ooot) | Unofficial native port of The Legend of Zelda: Ocarina of Time (N64) | 704 | 🟡 | C++ |
| [hells-gate-recomp](https://github.com/florinp93/hells-gate-recomp) | Xbox 360 to PC port of Dante's Inferno using ReXGlue (static recompilation) | 700 | 🟢 | C++ |
| [DriveClub (DriveClub Recomp)](https://github.com/OverkillLabs3/driveclub-recomp) | Static recompilation of DriveClub (PS4) into a native PC port | 696 | 🟢 | C++ |
| [smw](https://github.com/snesrev/smw) | Super Mario World reimplementation in C | 648 | 🟡 | C |
| [Crash Team Racing Nitro-Fueled](https://github.com/GetLostIn/CTR-NitroFueled-PC) | Unofficial native port of Crash Team Racing Nitro-Fueled (PS4) | 633 | 🟢 | C++ |
| [Mario Kart 64: Recompiled](https://github.com/sonicdcer/MarioKart64Recomp) | Static recompilation of Mario Kart 64 using N64Recomp and RT64 | 620 | 🟢 | C++ |
| [Pokémon Emerald](https://github.com/ZallaxDev/emerald-3ds) | Unofficial native port of Pokémon Emerald (GBA) | 612 | 🟢 | C |
| [ps3recomp](https://github.com/sp00nznet/ps3recomp) | Static recompilation runtime libraries for PlayStation 3 titles | 578 | 🟢 | C |
| [The Legend of Zelda: The Wind Waker](https://github.com/elliotttate/Wind-Waker-Recomp) | Static recompilation of The Legend of Zelda: The Wind Waker (GameCube) into a native PC port | 578 | 🟢 | C |
| [Tenkaichi3Decomp](https://github.com/z3xox/Tenkaichi3Decomp) | PC port of Dragon Ball Z: Budokai Tenkaichi 3 built on its decompilation | 577 | 🟢 | C |
| [TriAevum](https://github.com/coccofresco/TriAevum) | Native PC recompilation runtime for Ocarina of Time 3D | 563 | 🟢 | C++ |
| [Ace Combat 6: Fires of Liberation](https://github.com/sal063/AC6_recomp) | Xbox 360 static recompilation of Ace Combat 6: Fires of Liberation | 557 | 🟢 | C++ |
| [MeleePC](https://github.com/999sian/melee-pc) | Recomp of Super Smash Bros Melee to PC. | 551 | 🟢 | C |
| [PsyDoom](https://github.com/BodbDearg/PsyDoom) | PC backport of PlayStation Doom based on reverse engineering of the original code | 547 | 🟡 | C++ |
| [Donkey Kong 64: Recompiled](https://github.com/Rainchus/Donkey-Kong-64-Recompiled) | Donkey Kong 64 static recompilation with high-framerate support | 543 | 🟢 | C |
| [Fable-2-Recomp](https://github.com/himdo/Fable-2-Recomp) | Fable-2-Recomp | 533 | 🟢 | C++ |
| [Uncharted: The Nathan Drake Collection](https://github.com/bc160201983/Uncharted-The-Nathan-Drake-Collection-PC-port) | Unofficial native port of Uncharted: The Nathan Drake Collection (PS4) | 528 | 🟢 | C++ |
| [Lighthouse](https://github.com/HarbourMasters/Lighthouse) | Banjo-Kazooie PC port with multiplayer, romhacks and randomizer | 524 | 🟢 | C |
| [Yakumo](https://github.com/TeamGDB/Yakumo) | Static recompilation of a PSP game into a native executable. Vulkan and SDL3. Bring your own copy of the game. | 522 | 🟢 | C++ |
| [Metroid Prime Port](https://github.com/Odrannnn/MetroidPrimePort) | Recomp of Metroid Prime to PC and Android. | 521 | 🟢 | C++ |
| [PaperBoat](https://github.com/HarbourMasters/PaperBoat) | Paper Mario source port based on the decompilation | 517 | 🟢 | C |
| [BattleShip](https://github.com/JRickey/BattleShip) | AI-assisted decomp-based PC/Mac/Linux port of Super Smash Bros | 515 | 🟢 | C++ |
| [BlueWake](https://github.com/chrissotraidis/bluewake) | The Wind Waker (GameCube) static recompilation | 483 | 🟢 | C |
| [speedbreaker](https://github.com/SpeedBreakerProject/speedbreaker) | Unofficial static recompilation of the Xbox 360 version of Need for Speed: Most Wanted (2005): a native port for Stea... | 479 | 🟢 | C++ |
| [Zelda 3 Launcher](https://github.com/RadzPrower/Zelda-3-Launcher) | GUI tool to download, build and launch the zelda3 C reimplementation of A Link to the Past | 479 | 🟢 | C# |
| [gtasa_vita](https://github.com/TheOfficialFloW/gtasa_vita) | Port of GTA: San Andreas to PS Vita by loading and patching the Android binaries | 465 | 🟡 | C |
| [ssbu-recomp](https://github.com/OpenSmash-Ultimate/ssbu-recomp) | Static recompilation of Super Smash Bros. Ultimate 13.0.4 to a native Windows program | 463 | 🟢 | C |
| [MadnessPatch](https://github.com/Wemino/MadnessPatch) | Unofficial native port of MadnessPatch (PC) | 453 | 🟢 | C++ |
| [gb-recompiled](https://github.com/arcanite24/gb-recompiled) | Static recompiler for Game Boy/Color ROMs to portable C with SDL2 runtime | 447 | 🟢 | Python |
| [Ico-PC](https://github.com/nathanialf/ico-pc) | Recomp of ICO (PS2) to PC. | 440 | 🟢 | C |
| [Edge Of Time Recomp](https://github.com/goliathret/EdgeOfTimeRecomp) | Recomp of Spider Man: Edge of Time from Xbox 360. | 438 | 🟢 | C++ |
| [Bayonetta 2 (B2recomp)](https://github.com/K0NL/B2recomp) | Static recompilation of Bayonetta 2 (Switch) into a native PC port | 435 | 🟢 | C |
| [The Last Guardian](https://github.com/HayatoG/tlg_pc) | Unofficial native port of The Last Guardian (PS4) | 428 | 🟢 | C++ |
| [CTR Native](https://github.com/CTR-tools/ctr-native) | Native PC port based on the Crash Team Racing decompilation | 427 | 🟢 | C |
| [SR](https://github.com/M-HT/SR) | A project to statically recompile following games to create Windows or Linux (x86 or arm) versions of the games - Alb... | 426 | 🟢 | C |
| [fifa-street-pc-port](https://github.com/samuelit0davila/fifa-street-pc-port) | Experimental Windows PC port of FIFA Street (2012, Xbox 360) built with ReXGlue | 424 | 🟢 | C# |
| [The Legend of Zelda: Skyward Sword HD (Sky Recomp)](https://github.com/Apolinario-coder/SkyRecomp) | Static recompilation of The Legend of Zelda: Skyward Sword HD (Switch) into a native PC port | 420 | 🟢 | C |
| [Pokemon Gold / Silver / Crystal (Gen2Recomped)](https://github.com/UNDERdecoded/Gen2Recomped) | Static recompilation of Pokemon Gold / Silver / Crystal (Game Boy Color) into a native PC port | 417 | 🟢 | Lua |
| [WindowSmash](https://github.com/OpenSmash-Ultimate/WindowSmash) | Native Windows porting toolkit for Super Smash Bros. Ultimate via static AArch64 recompilation | 402 | 🟢 | C |
| [Star Fox 64: Recompiled](https://github.com/sonicdcer/Starfox64Recomp) | Static recompilation of Star Fox 64 for Windows/Linux | 399 | 🟢 | C |
| [Fable2Recomp](https://github.com/Fable2Recomp/Fable2Recomp) | A Fable 2 Recomp | 396 | 🟢 | C++ |
| [harkinianpad (Ocarina of Time)](https://github.com/chrissotraidis/harkinianpad) | Ocarina of Time on iOS and iPadOS via Ship of Harkinian with Metal rendering | 396 | 🟢 | Python |
| [Burnout 3: Takedown](https://github.com/xenophobentx/takedawn) | Static recompilation of Burnout 3: Takedown (Xbox) into a native PC port | 395 | 🟢 | C |
| [psp-web-recomp](https://github.com/snuri00/psp-web-recomp) | Static recompilation of PSP games (God of War) to WebAssembly with HLE kernel | 392 | 🟢 | C++ |
| [NocturneRecomp](https://github.com/birabittoh/NocturneRecomp) | Static recompilation of Castlevania: Symphony of the Night (XBLA) for Windows and Linux, built on the ReXGlue SDK. | 385 | 🟢 | C++ |
| [TheSimpsonsGameRecomp](https://github.com/YesterMester/TheSimpsonsGameRecomp) | The Simpsons Game Xbox 360 static recompilation | 380 | 🟢 | C++ |
| [SMS Launcher](https://github.com/chasem-dev/sms-launcher) | Recomp of Super Mario Sunshine. | 379 | 🟢 | JavaScript |
| [Tekken6-native-online](https://github.com/Ekspym/Tekken6-native-online) | Unofficial native port of Tekken 6 (Xbox 360) | 375 | 🟢 |  |
| [psxrecomp](https://github.com/RetroPortingToolKit/psxrecomp) | PlayStation 1 game static recompiler ecosystem | 365 | 🟢 | C |
| [libultraship](https://github.com/Kenix3/libultraship) | Library for porting N64 decompilations to PC, used by Ship of Harkinian and other ports | 364 | 🟢 | C++ |
| [sm64rt](https://github.com/DarioSamo/sm64rt) | Super Mario 64 PC port with ray tracing | 364 | 🟡 | C |
| [strikers](https://github.com/new-coke/strikers) | Mario Strikers Charged native PC port / recompilation | 357 | 🟢 | C++ |
| [MinecraftC](https://github.com/johnpayne-dev/MinecraftC) | C port of Minecraft Classic 0.0.30a with ray tracing, based on the decompiled Java game | 350 | 🟡 | C |
| [SCDA-XBERecomp](https://github.com/TGP482/SCDA-XBERecomp) | Unofficial PC port of Splinter Cell: Double Agent (original Xbox) via static recompilation | 349 | 🟢 | C++ |
| [CoD3Recomp](https://github.com/FrankHUN88453/CoD3Recomp) | Static recompilation of Call of Duty 3 (Xbox 360) with host runtime and tools | 343 | 🟢 | C++ |
| [GoldenEye 007 port](https://github.com/murkantor/Project-Midas) | PC port of GoldenEye 007 for Windows and Linux built from the N64 decompilation | 342 | 🟢 | C |
| [nebula](https://github.com/keepvaibin/nebula) | Recompilation of Super Mario Galaxy targeting Windows, with macOS and Android planned | 342 | 🟢 | C++ |
| [OpenTIE](https://github.com/elyosh/OpenTIE) | Open-source recomp of TIE Fighter. | 341 | 🟢 | C |
| [The-Darkness-Recomp](https://github.com/portingpete/The-Darkness-Recomp) | The Darkness Xbox 360 static recompilation | 339 | 🟢 | C++ |
| [DownpourRecomp](https://github.com/LittleBitUA/DownpourRecomp) | Silent Hill: Downpour Xbox 360 static recompilation | 334 | 🟢 | C++ |
| [BLACK (black-pc)](https://github.com/Spark198rus/black-pc) | Unofficial native port of BLACK (og xbox) | 333 | 🟢 | C++ |
| [Dinosaur Planet: Recompiled](https://github.com/DinosaurPlanetRecomp/dino-recomp) | Static recompilation of the unreleased N64 Dinosaur Planet | 332 | 🟢 | C++ |
| [Goemon64Recomp](https://github.com/klorfmorf/Goemon64Recomp) | Mystical Ninja Starring Goemon static recompilation | 326 | 🟢 | C |
| [inFamous](https://github.com/whompay/inFAMOUSreborn) | Static recompilation of inFamous (PS3) into a native PC port | 317 | 🟢 | C |
| [ProjectCane](https://github.com/theclub654/ProjectCane) | Playable PC port of Sly Cooper and the Thievius Raccoonus rebuilt via reverse engineering | 317 | 🟢 | C++ |
| [Grand-V](https://github.com/SebasKitten/Grand-V) | GTA V reverse engineered to run in a Chromium browser with WebAssembly and WebGPU | 312 | 🟢 | Rust |
| [pokeemerald-wasm](https://github.com/tripplyons/pokeemerald-wasm) | Pokemon Emerald decompilation recompiled to WebAssembly for the browser | 312 | 🟢 | C |
| [BM64Recomp](https://github.com/RevoSucks/BM64Recomp) | Bomberman 64 static recompilation with mod support | 308 | 🟢 | C++ |
| [CBFD-Recompiled](https://github.com/sciaschi/CBFD-Recompiled) | Static recompilation of Conker's Bad Fur Day (N64) to native PC | 307 | 🟢 | C |
| [ForzaHorizon1-ReImagined](https://github.com/Dyotson/ForzaHorizon1-ReImagined) | Forza Horizon (Xbox 360) running natively on PC, rebuilt with online free roam and leaderboards | 304 | 🟢 | Python |
| [Paper Mario](https://github.com/SMCGames/Paper-Mario-ReCut-Deprecated) | Unofficial native port of Paper Mario (N64) | 304 | 🟢 | C++ |
| [G-Diffuser](https://github.com/Zorkats/G-Diffuser) | Unofficial PC port of F-Zero X based on its decompilation | 295 | 🟢 | C |
| [GoldenEye PC Port](https://github.com/jkdansereau/goldeneye-pc-port) | Recomp of GoldenEye 007 (N64). | 290 | 🟢 | C |
| [Quest64-Recomp](https://github.com/Rainchus/Quest64-Recomp) | Quest 64 static recompilation with mod support | 281 | 🟢 | C++ |
| [MegaMan64Recompiled](https://github.com/MegaMan64Recomp/MegaMan64Recompiled) | Mega Man 64 static recompilation with mod support | 277 | 🟢 | C++ |
| [Pikmin & Pikmin 2 (Open Nectar)](https://github.com/SSunnKing/Open-Nectar---Pikmin-Native-PC-Mobile-Port) | Unofficial native port of Pikmin & Pikmin 2 (GameCube) | 276 | 🟢 | Assembly |
| [Killzone: Shadow Fall (killzone-shadowfall-pc)](https://github.com/lesca-191204/killzone-shadowfall-pc) | Unofficial native port of Killzone: Shadow Fall (PlayStation 4) | 275 | 🟢 | C++ |
| [Metroid Prime Hunters](https://github.com/mstan/MetroidPrimeHuntersRecomp) | Static recompilation of Metroid Prime Hunters (DS) into a native PC port | 269 | 🟢 | Python |
| [Super Mario Galaxy (Galaxy Android)](https://github.com/OpenPort-Labs/Galaxy-Android) | Unofficial native port of Super Mario Galaxy (Wii) | 267 | 🟢 | C++ |
| [DKC1Recomp](https://github.com/elliotttate/DKC1Recomp) | Static recompilation of Donkey Kong Country (SNES) with widescreen | 265 | 🟢 | C |
| [God of War: Ascension](https://github.com/arnaldolima1/gow-ascension-pc) | Static recompilation of God of War: Ascension (PS3) into a native PC port | 263 | 🟢 | Python |
| [Condemned2Recomp](https://github.com/psxrestore/Condemned2Recomp) | A static recompilation of Condemned 2: Bloodshot done with RexGlue. | 260 | 🟢 | C++ |
| [LCS Recomp](https://github.com/elmasas/lcs-recomp) | Recomp of the PSP game GTA: Liberty City Stories to PC. | 259 | 🟢 | C++ |
| [Need for Speed: Most Wanted](https://github.com/StevensND/nfsmw-nx) | Static recompilation of Need for Speed: Most Wanted (Xbox 360) into a native PC port | 252 | 🟢 | C |
| [Half-Life (Lambda1VR (Xash3D VR port))](https://github.com/Team-Beef-Studios/Lambda1VR) | Unofficial native port of Half-Life (PC) | 250 | 🟢 | C |
| [Crash Bandicoot](https://github.com/wurlyfox/c1) | Unofficial native port of Crash Bandicoot (PS1) | 249 | 🟡 | C++ |
| [Luigi's Mansion (Luigi's Mansion Recompiled)](https://github.com/rob646464/luigis-mansion-recompiled) | Static recompilation of Luigi's Mansion (GameCube) into a native PC port | 248 | 🟢 | C++ |
| [Skate3-Mobile](https://github.com/Buku313/Skate3-Mobile) | Play Skate 3 natively on Android. Download one APK, select your own ISO, and skate. ARM64 recompilation with Vulkan r... | 248 | 🟢 | C++ |
| [nfsu2-recompiled](https://github.com/codepdbh/nfsu2-recompiled) | Static recompilation of Need for Speed Underground 2 (PC) | 247 | 🟢 | C++ |
| [MKW-3DS](https://github.com/MiniBandit/MKW-3DS) | Native Nintendo 3DS port of Mario Kart Wii, built from your own disc | 245 | 🟢 | C++ |
| [Plants vs. Zombies 2 (pvzge_web)](https://github.com/Gzh0821/pvzge_web) | Unofficial native port of Plants vs. Zombies 2 (Mobile) | 243 | 🟢 | Dockerfile |
| [Yu-Gi-Oh! Forbidden Memories Recompiled](https://github.com/Unchiga/Yu-Gi-Oh-Forbidden-Memories-Recompiled) | Yu-Gi-Oh! Forbidden Memories PlayStation static recompilation | 243 | 🟢 | C |
| [Parasite-Eve-2-HD-Remaster (Parasite Eve II)](https://github.com/faligame/Parasite-Eve-2-HD-Remaster) | Static recompilation of Parasite Eve II (PS1) into a native port | 238 | 🟢 |  |
| [PSPRecomp](https://github.com/jessicanataliagta/PSPRecomp) | Static recompilation framework for PSP software | 237 | 🟢 | C++ |
| [Diddy Kong Racing](https://github.com/ThatGuyMcd/DKR-R) | Static recompilation of Diddy Kong Racing (N64) into a native PC port | 236 | 🟢 | C++ |
| [mario-kart-64-3ds](https://github.com/EstebanPdN/mario-kart-64-3ds) | Native Nintendo 3DS port based on the Mario Kart 64 decompilation | 230 | 🟢 | C++ |
| [SpelunkyClassicHD](https://github.com/yancharkin/SpelunkyClassicHD) | Unofficial native port of Spelunky (PC) | 230 | 🟢 | Game Maker Language |
| [DimensionsRecomp](https://github.com/NeverCookFirst/DimensionsRecomp) | Proof that a toys-to-life game can be recompiled. A native PC build of LEGO Dimensions, made by statically recompilin... | 229 | 🟢 | C++ |
| [Sonic Unleashed](https://github.com/SansNope/UnleashedRecomp-Android) | Static recompilation of Sonic Unleashed (Xbox 360) into a native PC port | 228 | 🟢 | C |
| [Viva Piñata: Trouble in Paradise](https://github.com/SolarCookies/TiP-Recomp) | Xbox 360 static recompilation of Viva Piñata: Trouble in Paradise | 228 | 🟢 | C++ |
| [Daytona Arcade Recomp](https://github.com/alphanu1/daytona-arcade-recomp) | Recomp of Daytona Racing to PC. | 223 | 🟢 | C++ |
| [Marble Blast Gold](https://github.com/RandomityGuy/MBHaxe) | Unofficial native port of Marble Blast Gold (PC) | 223 | 🟢 | Haxe |
| [GoldenRecomp](https://github.com/kholdfuzion/GoldenRecomp) | WIP Recompilation of a game about a special agent who saves the world from a traitor. | 219 | 🟢 | C++ |
| [Super Mario 64 (libsm64-godot)](https://github.com/Brawmario/libsm64-godot) | Unofficial native port of Super Mario 64 (N64) | 219 | 🟢 | GDScript |
| [Dragon's Crown Pro](https://github.com/saulob/dragons-crown-pro-pc) | Unofficial native port of Dragon's Crown Pro (PS4) | 218 | 🟢 | C++ |
| [doaxvb-re](https://github.com/NoRain211/doaxvb-re) | Dead or Alive Xtreme Beach Volleyball original-Xbox static recompilation | 217 | 🟢 | C |
| [Silent Hill](https://github.com/Sezzary/SilentEngine) | Unofficial native port of Silent Hill (PS1) | 217 | 🟢 | C++ |
| [daytona-xbla-recomp](https://github.com/Subarasheese/daytona-xbla-recomp) | A static recompilation of Daytona USA (Xbox 360 / XBLA, 2011) | 216 | 🟢 | C++ |
| [Mortal Kombat: Shaolin Monks](https://github.com/OAleex/ShaolinMonksRecomp) | Static recompilation of Mortal Kombat: Shaolin Monks (Xbox) into a native PC port | 215 | 🟢 | C++ |
| [yoyoloader_vita](https://github.com/Rinnegatamante/yoyoloader_vita) | Loader that runs Android GameMaker (YoYo Runner) games natively on PS Vita | 215 | 🟢 | C |
| [Super Metroid Launcher](https://github.com/RadzPrower/Super-Metroid-Launcher) | GUI tool to download, build and launch the Super Metroid C reimplementation (sm) | 213 | 🟢 | C# |
| [Crash Team Racing: High Octane](https://github.com/Rinnegatamante/Crash-Team-Racing-High-Octane) | CTR source port for PC, PS Vita and web | 211 | 🟢 | C |
| [King Kong: Recompiled](https://github.com/TekRantGaming/king-kong-recompiled) | Peter Jackson's King Kong Xbox 360 static recompilation | 211 | 🟢 | C++ |
| [PGR4-Recomp](https://github.com/beatrixzy/PGR4-Recomp) | A Recompilation of Project Gotham Racing 4 | 211 | 🟢 | CMake |
| [MediEvil](https://github.com/BlackLabelHQ/MediEvilRecomp) | Static recompilation of MediEvil (PS1) into a native PC port | 210 | 🟢 | C# |
| [Dragon Ball Z: Budokai HD Collection](https://github.com/novapowers0/DBZ-Budokai-3-HD-Collection) | Static recompilation of Dragon Ball Z: Budokai HD Collection (Xbox 360) into a native PC port | 209 | 🟢 | C++ |
| [The Legend of Zelda: A Link to the Past](https://github.com/Waterdish/zelda3-android) | Unofficial native port of The Legend of Zelda: A Link to the Past (SNES) | 208 | 🟡 | C |
| [DolRecomp](https://github.com/ExpansionPak/DolRecomp) | Static recompiler for GameCube and Wii games | 203 | 🟢 | C |
| [khdays-port](https://github.com/Yokimitsuro/khdays-port) | Experimental native PC runtime for Kingdom Hearts 358/2 Days | 203 | 🟢 | C |
| [Midnight Club: Los Angeles](https://github.com/mzzvxm/LARecomp) | Static recompilation of Midnight Club: Los Angeles (Xbox 360) into a native PC port | 201 | 🟢 | C++ |
| [Minecraft: Java Edition (Minecraft PSP)](https://github.com/Pencea-Flavius/Minecraft-PE-PSP) | Unofficial native port of Minecraft: Java Edition (PC) | 201 | 🟢 | C++ |
| [Parasite Eve HD Remaster](https://github.com/faligame/Parasite-Eve-HD-Remaster) | Recomp and enhancement of the PS1 game Parasite Eve. | 201 | 🟢 |  |
| [sunpad](https://github.com/chrissotraidis/sunpad) | Super Mario Sunshine on iOS, macOS and tvOS via static recompilation | 197 | 🟢 | Objective-C++ |
| [Perfect Dark](https://github.com/DabDavis/perfect-dark-dabs-mod) | Recomp of the N64 game Perfect Dark to PC, with enhancements. | 196 | 🟢 | C |
| [SkyRoads-Codex](https://github.com/ammaarreshi/SkyRoads-Codex) | SkyRoads DOS game reverse engineered without source using Codex | 195 | 🟢 | Rust |
| [Duke Nukem Zero Hour: Recompiled](https://github.com/sonicdcer/DNZHRecomp) | Duke Nukem: Zero Hour static recompilation with gyro aiming and high FPS | 194 | 🟢 | C++ |
| [GoldenEye 007](https://github.com/chrissotraidis/goldenpad) | Unofficial native port of GoldenEye 007 (N64) | 189 | 🟢 | Swift |
| [god-of-war-recomp](https://github.com/KIexster/god-of-war-recomp) | Native PC port of God of War (PS2) via static recompilation with PS2Recomp | 187 | 🟢 | C++ |
| [goldenballoon](https://github.com/akratch/goldenballoon) | Native and browser port of the 1997 N64 kart racer Diddy Kong Racing | 185 | 🟢 | C |
| [sega-vr-disasm](https://github.com/matiaszanolli/sega-vr-disasm) | Complete static recompilation of Virtua Racing for the Sega 32X (optimization in progress) | 185 | 🟢 | Assembly |
| [Saints Row](https://github.com/whompay/SaintsReborn) | Unofficial native port of Saints Row (Xbox 360) | 184 | 🟢 | C++ |
| [SwitchWakerHD](https://github.com/centollOS/SwitchWakerHD) | Wind Waker HD (Wii U) static recompilation for Nintendo Switch, deko3d renderer. Requires your own game dump. | 184 | 🟢 | C++ |
| [N64ModernRuntime](https://github.com/N64Recomp/N64ModernRuntime) | Runtime for traditional ports and recompilations of N64 games | 183 | 🟢 | C++ |
| [Pokémon: Let's Go, Eevee! (Let's Go Recomp)](https://github.com/raulzrrs/letsgo-recomp) | Static recompilation of Pokémon: Let's Go, Eevee! (Switch) into a native PC port | 182 | 🟢 | C |
| [Black-2006-Recomp](https://github.com/portingpete/Black-2006-Recomp) | Native Windows static recompilation of BLACK (2006) for the original Xbox | 181 | 🟢 | C |
| [Wipeout](https://github.com/jnmartin84/wipeout-dc) | Unofficial native port of Wipeout (PS1) | 180 | 🟢 | C |
| [DPRecomp](https://github.com/LittleBitUA/DPRecomp) | Deadly Premonition Xbox 360 static recompilation | 179 | 🟢 | C++ |
| [EA Sports UFC 3](https://github.com/GNSB/UFC-3-PS4-PORT-LINUX-WINDOWS) | Unofficial native port of EA Sports UFC 3 (PS4) | 179 | 🟢 | C++ |
| [Banjo-Kazooie: Nuts & Bolts](https://github.com/masterspike52/reNut) | Xbox 360 static recompilation of Banjo-Kazooie: Nuts & Bolts | 178 | 🟢 | C++ |
| [Half-Life (webXash))](https://github.com/x8BitRain/webXash) | Unofficial native port of Half-Life (webXash)) (PC) | 178 | 🟢 | TypeScript |
| [ModernGekko](https://github.com/ExpansionPak/ModernGekko) | Runtime for recompilations of GameCube games | 178 | 🟢 | C++ |
| [RingOut](https://github.com/jackpoison-prog/RingOut) | Native PC port of a GameCube fighting game via static recompilation | 177 | 🟢 | C |
| [sms-pc-port](https://github.com/chasem-dev/sms-pc-port) | Native PC port of Super Mario Sunshine | 177 | 🟢 | C++ |
| [Tekken Tag Tournament 2](https://github.com/shihabal3amri/tekken-tag-tournament-2-pc) | Static recompilation of Tekken Tag Tournament 2 (Xbox 360) into a native PC port | 175 | 🟢 | C++ |
| [burnout3-pc](https://github.com/danielgomesvieira2000/burnout3-pc) | Burnout 3: Takedown as a native Windows port via a PS2 decompilation toolchain | 173 | 🟢 | C++ |
| [FFTARecomp](https://github.com/Jorge262007/FFTARecomp) | Native Windows port of Final Fantasy Tactics Advance (GBA) with widescreen | 173 | 🟢 | Rust |
| [HarvestMoon64Recomp](https://github.com/HarvestMoon64Recomp/HarvestMoon64Recomp) | PC Port of Harvest Moon 64 made using N64: Recompiled (Windows/Linux/Mac) | 173 | 🟢 | C++ |
| [NFSMW-Recompiled](https://github.com/madelrandel-blip/NFSMW-Recompiled) | Static native recompilation of Need for Speed: Most Wanted (Xbox 360) | 172 | 🟢 | C |
| [Need for Speed: Underground 2 (Switch port)](https://github.com/antoxa2584x/nfsu2-sw) | Unofficial native port of Need for Speed: Underground 2 (Xbox) | 169 | 🟢 | C |
| [Super Mario Maker 2 (SMM2 Recomp)](https://github.com/smm2recomp/smm2recomp) | Static recompilation of Super Mario Maker 2 (Switch) into a native PC port | 168 | 🟢 | Rust |
| [Crash Team Racing: Turbocharged](https://github.com/CameronRedmore/Crash-Team-Racing-Turbocharged) | CTR PC source port with native 3D renderer and high frame rates | 167 | 🟢 | C |
| [MediEvil](https://github.com/bc160201983/medievil_2019_pc_port) | Unofficial native port of MediEvil (PS4) | 166 | 🟢 | C++ |
| [SDOJ-Recomp](https://github.com/eandis/SDOJ-Recomp) | SDOJ-Recomp | 166 | 🟢 | C++ |
| [DefJamFFNY-recomp](https://github.com/vyanhursky/DefJamFFNY-recomp) | Def Jam: Fight for NY PC port — static recompilation of the original Xbox game for native Windows and macOS (Direct3D... | 165 | 🟢 | Python |
| [halo-64](https://github.com/JackTulli/halo-64) | Halo: Combat Evolved multiplayer on the N64, built from the Halo CE decompilation | 164 | 🟢 | C |
| [hit-and-run-web (The Simpsons: Hit & Run)](https://github.com/Vheissu/hit-and-run-web) | Browser (WebAssembly) port of The Simpsons: Hit & Run | 164 | 🟢 | TypeScript |
| [Eternal Sonata](https://github.com/birabittoh/EternalSonataReprise) | Static recompilation of Eternal Sonata (Xbox 360) into a native PC port | 163 | 🟢 | C++ |
| [Jet Set Radio Future (Jet Set Radio Future Unleashed)](https://github.com/JuMatt/JetSetRadioFuture-Unleashed) | Unofficial native port of Jet Set Radio Future (og xbox) | 162 | 🟢 | C |
| [Super Smash Bros. Melee (OpenSmash (Melee engine: opensmash-melee-pc))](https://github.com/turtlesoupy/opensmash) | Unofficial native port of Super Smash Bros. Melee (GameCube) | 161 | 🟢 | HTML |
| [Xerenge](https://github.com/shipa-2/Xerenge) | Burnout Revenge recompilation based on ReXGlue | 161 | 🟢 | C++ |
| [Drakengard 3 (Drakengard 3 Recompiled)](https://github.com/soyjxck/dod3-recomp) | Static recompilation of Drakengard 3 (PS3) into a native PC port | 160 | 🟢 | C++ |
| [Initial-D-Arcade-Stage-3-Native-SH-4-Recompilation-WIP-](https://github.com/distilledorion-sketch/Initial-D-Arcade-Stage-3-Native-SH-4-Recompilation-WIP-) | Native SH-4 AOT recompilation of Initial D Arcade Stage 3 (NAOMI 2) — BIOS-free Vulkan public early demo (WIP). | 160 | 🟢 | C++ |
| [OpenXWA](https://github.com/elyosh/OpenXWA) | Open-source recomp of X-Wing Alliance. | 160 | 🟢 | C |
| [mcla-recomp](https://github.com/holdmysocks/mcla-recomp) | Static recompilation of Midnight Club: Los Angeles (Xbox 360) for PC and PS5 | 159 | 🟢 | C++ |
| [Xbox360-Native-Ports](https://github.com/CrownParkComputing/Xbox360-Native-Ports) | Xbox 360 titles recompiled to native Linux with Vulkan renderer; launchers only | 159 | 🟢 | C++ |
| [naruto-rise-recomp](https://github.com/jorjbarbosa/naruto-rise-recomp) | Static PC recompilation of Naruto: Rise of a Ninja (Xbox 360) via ReXGlue | 158 | 🟢 | C++ |
| [WWE SmackDown vs. Raw 2007](https://github.com/HollywoodAkeem/SVR07-Recomp) | Static recompilation of WWE SmackDown vs. Raw 2007 (Xbox 360) into a native PC port | 158 | 🟢 | C++ |
| [Ninja Gaiden Black (Ninja Gaiden Black Recompiled)](https://github.com/gamboozino/ngbrecomp) | Static recompilation of Ninja Gaiden Black (og xbox) into a native PC port | 157 | 🟢 | C |
| [Dr. Mario 64 Recomp Plus](https://github.com/theboy181/drmario64_recomp_plus) | Dr. Mario 64 static recompilation with 4-player support | 156 | 🟢 | C++ |
| [Eternal Darkness: Sanity's Requiem](https://github.com/griches/EternalDarknessRecomp) | Static recompilation of Eternal Darkness: Sanity's Requiem (GameCube) into a native PC port | 156 | 🟢 | C |
| [God of War: Sons of Sparta (Sons Of Sparta PS5 Native)](https://github.com/OverkillLabs3/SoS-PS5) | Unofficial native port of God of War: Sons of Sparta (PS5) | 152 | 🟢 | C++ |
| [Mercenaries-Recompiled](https://github.com/KraftMacAndChee/Mercenaries-Recompiled) | Recompilation of Mercenaries: Playground of Destruction | 152 | 🟢 | C |
| [Gran Turismo 2 (gt-2-pc)](https://github.com/dubrovskiy-yevhen-stakelogic/gt-2-pc) | Unofficial native port of Gran Turismo 2 (PS1) | 151 | 🟢 | C++ |
| [Resident Evil - Code: Veronica X (recvx-enhanced-recomp)](https://github.com/aikatore/recvx-enhanced-port) | Static recompilation of Resident Evil - Code: Veronica X (PS2) into a native PC port | 150 | 🟢 | C |
| [snesrecomp](https://github.com/RetroPortingToolKit/snesrecomp) | Super Nintendo static recompiler ecosystem | 148 | 🟢 | C |
| [F-15 II](https://github.com/neuviemeporte/f15se2-re) | Recomp of MicroProse F-15 II. | 147 | 🟢 | C |
| [Half-Life (Xash3D-Emscripten)](https://github.com/btarg/Xash3D-Emscripten) | Browser (WebAssembly) port of Half-Life (PC) | 146 | 🔴 | HTML |
| [YuGiOhForbiddenMemoriesRecomp](https://github.com/Unchiga/YuGiOhForbiddenMemoriesRecomp) | Static recompilation of Yu-Gi-Oh! Forbidden Memories (PS1) into a native executable - with a live duel-rank meter, a... | 145 | 🟢 | C |
| [Burnout 3: Takedown](https://github.com/sp00nznet/burnout3) | Static recompilation of Burnout 3: Takedown (Xbox) into a native PC port | 142 | 🟢 | C |
| [DKC3Recomp](https://github.com/elliotttate/DKC3Recomp) | Native recompilation of Donkey Kong Country 3 (SNES) | 139 | 🟢 | C |
| [Castlevania: Legacy of Darkness](https://github.com/fliperama86/cvlod_recomp) | Static recompilation of Castlevania: Legacy of Darkness (N64) into a native PC port | 138 | 🟢 | C |
| [Syphon Filter (PC Recomp)](https://github.com/Madxbio97/SF-pc-port) | Static recompilation of Syphon Filter (PS1) into a native PC port | 136 | 🟢 | C++ |
| [cricket07-browser](https://github.com/Dhaiwat10/cricket07-browser) | EA Sports Cricket 07 statically recompiled from x86 to C and WebAssembly for the browser | 134 | 🟢 | C |
| [SuperMarioWorldRecomp](https://github.com/mstan/SuperMarioWorldRecomp) | Super Mario World recompiled using snesrecomp | 134 | 🟢 | C |
| [Retro-Launcher](https://github.com/RetroPortingToolKit/Retro-Launcher) | Launcher that updates, manages and distributes static recompilation projects | 133 | 🟢 | C++ |
| [mw2-recompiled](https://github.com/PaulCombal/mw2-recompiled) | Call of Duty: Modern Warfare 2 (2009) for Xbox 360 recompiled for Windows & Linux | 132 | 🟢 | C++ |
| [Rage Racer port](https://github.com/khasinski/rage-racer-pc) | Native PC port of Rage Racer (PS1) built from a decompilation | 132 | 🟢 | C |
| [melee-unlocked](https://github.com/Hero88go/melee-unlocked) | Native Windows source port of Super Smash Bros. Melee built from its decompiled C source | 131 | 🟢 | C++ |
| [Ratchet & Clank (rac-rs)](https://github.com/AsobiCodes/rac-rs) | Static recompilation of Ratchet & Clank (PS2) into a native PC port | 131 | 🟢 | Rust |
| [Unicorn Overlord (unicorn_overlord_pc)](https://github.com/hachi23/unicorn_overlord_pc) | Unofficial native port of Unicorn Overlord (PlayStation 4) | 131 | 🟢 | C++ |
| [DBZ1](https://github.com/WistfulHopes/DBZ1) | Dragon Ball Z Budokai HD Recompiled | 130 | 🟢 | C++ |
| [projectreach](https://github.com/chrissotraidis/projectreach) | Halo: Combat Evolved on iPhone, iPad and Mac. The Xbox edition with online matches of up to 128 players and the origi... | 130 | 🟢 | C |
| [Super Paper Mario](https://github.com/josiahg2502-glitch/NewSuperPaperBros) | Static recompilation of Super Paper Mario (Wii) into a native PC port | 130 | 🟢 | C++ |
| [RaceWave46](https://github.com/DomazinUS/RaceWave46) | AI-assisted Wave Race 64 recompilation for Windows | 129 | 🟢 | C++ |
| [wwe-svr2011-pc](https://github.com/KaikoClanworth1/wwe-svr2011-pc) | Unofficial native PC port of WWE SmackDown vs. Raw 2011 (Xbox 360). Bring your own disc. | 129 | 🟢 | C++ |
| [AloneInTheDarkReHaunted](https://github.com/spacefarergames/AloneInTheDarkReHaunted) | A heavily enhanced port and dynamic recomp of Alone In The Dark 1, with Textured Models, HD-4K background replacement... | 127 | 🟢 | C++ |
| [Flame](https://github.com/DiaLight/Flame) | Dungeon Keeper II partial recompilation with bug fixes. | 127 | 🟢 | C++ |
| [BMHeroRecomp](https://github.com/RevoSucks/BMHeroRecomp) | Bomberman Hero static recompilation with mod support | 126 | 🟢 | C++ |
| [Driveclub](https://github.com/BlackLineInteractive/Driveclub-Port) | Unofficial native port of Driveclub (PS4) | 125 | 🗄️ | C++ |
| [nesrecomp](https://github.com/mstan/nesrecomp) | Static recompiler for NES games | 125 | 🟢 | C |
| [Phase Distorter](https://github.com/TheRunaway5/Phase-Distorter) | Native C++20 PC port of EarthBound / Mother 2 for Linux and Windows | 125 | 🟢 | C++ |
| [Super Metroid](https://github.com/mstan/SuperMetroidRecomp) | Static recompilation of Super Metroid (SNES) into a native PC port | 124 | 🟢 | C |
| [ConkerBFDReloaded](https://github.com/DahSidiAbdallah/ConkerBFDReloaded) | Conker's Bad Fur Day running natively on PC: an N64 recompilation with a Classic mode true to the N64 and a Modern mo... | 123 | 🟢 | C++ |
| [Darkwatch (DarkwatchDarkerEdition)](https://github.com/linkssy2/DarkwatchDarkerEdition) | Static recompilation of Darkwatch (Xbox) into a native PC port | 123 | 🟢 | C++ |
| [doukutsupsx (Cave Story)](https://github.com/fgsfdsfgs/doukutsupsx) | Port of Cave Story to the PlayStation, based on the CSE2 decompilation | 123 | 🔴 | C |
| [fm4-recomp](https://github.com/Alexbeav/fm4-recomp) | Experimental static recompilation of Forza Motorsport 4 using ReXGlue. No game files included. | 122 | 🟢 | PowerShell |
| [Skies of Arcadia Legends](https://github.com/ogdanimal/SkiesOfArcadiaLegends-Recomp) | Static recompilation of Skies of Arcadia Legends (GameCube) into a native PC port | 122 | 🟢 | C |
| [Snap64Recomp](https://github.com/JackandBeans/Snap64Recomp) | Pokémon Snap static recompilation | 122 | 🟢 | C++ |
| [Killzone](https://github.com/drakolordx7/KillzoneRecomp) | Static recompilation of Killzone (PS2) into a native PC port | 121 | 🟢 | C++ |
| [OpenXW](https://github.com/elyosh/OpenXW) | Open-source recomp of X-Wing. | 121 | 🟢 | C |
| [Pokémon Stadium](https://github.com/mstan/PokemonStadiumRecomp) | Static recompilation of Pokémon Stadium (N64) into a native PC port | 121 | 🗄️ | C++ |
| [Forza Horizon 2](https://github.com/Gabrick75/fh2-recompiled) | Static recompilation of Forza Horizon 2 (Xbox 360) into a native PC port | 120 | 🟢 | C |
| [Half-Life (hl (Xash3D FWGS Emscripten port))](https://github.com/Pixelsuft/hl) | Browser (WebAssembly) port of Half-Life (PC) | 120 | 🔴 | HTML |
| [GalaxyQuest](https://github.com/bigmak94/GalaxyQuest) | Super Mario Galaxy native VR port for Meta Quest 3 | 118 | 🟢 | C++ |
| [nfs-most-wanted-mac](https://github.com/elforeign/nfs-most-wanted-mac) | Need for Speed: Most Wanted native on Apple Silicon via static recompilation | 118 | 🟢 | C++ |
| [skate3-ios-setup](https://github.com/andrewnakas/skate3-ios-setup) | Builds the Skate 3 recompilation for iOS from your own disc image | 118 | 🟢 | Shell |
| [ValkyrieRecomp](https://github.com/Ed1z19/ValkyrieRecomp) | Native PC recompilation of Valkyrie Profile (PS1) | 118 | 🟢 | Python |
| [OpenTricky](https://github.com/GiZcesi/OpenTricky) | OpenTricky is an unofficial PC port of SSX Tricky, made by static recompilation. Bring your own disc. | 117 | 🟢 | C |
| [beanRecomp](https://github.com/Fable2Recomp/beanRecomp) | A static Recomp of 007 Goldeneye Remaster XBLA | 114 | 🟡 | C++ |
| [hl360-forza4 (Forza Motorsport 4)](https://github.com/0herculabs/hl360-forza4) | Forza Motorsport 4 (Xbox 360) running natively on PC | 114 | 🟢 | C++ |
| [psxrecomp-ports](https://github.com/alexbeavs-ps1-ports/psxrecomp-ports) | Unofficial noncommercial PlayStation recompilation releases | 114 | 🟢 | PowerShell |
| [Army of Two](https://github.com/OpenPortroid/ArmyOfTwoRecompilation) | Static recompilation of Army of Two (Xbox 360) into a native PC port | 113 | 🟢 | C++ |
| [BT3-Recomp](https://github.com/z3xox/BT3-Recomp) | Dragon Ball Z: Budokai Tenkaichi 3 PC port via static recompilation | 113 | 🟢 | C++ |
| [The Return of the King (Athelas)](https://github.com/Shagg88/Athelas) | Unofficial native port of The Return of the King (PC) | 113 | 🟢 | C++ |
| [Pokémon SoulSilver](https://github.com/ClickingMaster/ssrecomp) | Static recompilation of Pokémon SoulSilver (DS) into a native PC port | 111 | 🟢 | C++ |
| [driftdroid](https://github.com/dorPXP/driftdroid) | A native Android port of Mario Kart Wii and Retro Rewind. Fast, easy. | 110 | 🟢 | C++ |
| [gears-judgement-recomp](https://github.com/OverkillLabs3/gears-judgement-recomp) | Native Windows recompilation of Gears of War: Judgment (Xbox 360) | 110 | 🟢 | C++ |
| [snowboardkids2-recomp](https://github.com/cdlewis/snowboardkids2-recomp) | Snowboard Kids 2 static recompilation with mod support | 110 | 🟢 | C |
| [wwe13-recomp](https://github.com/PromethenDev/wwe13-recomp) | Static recompilation of WWE '13 (Xbox 360) for Windows and Linux via ReXGlue | 110 | 🟢 | C++ |
| [Halo: Combat Evolved based on the Halo CE decomp port](https://github.com/ChupathingyCE/chupathingyce) | Native Windows, Mac, Linux and Android port of Halo: Combat Evolved based on the Halo CE decomp | 109 | 🟢 | C |
| [Ace-Combat-5-Static-recompilation](https://github.com/sal063/Ace-Combat-5-Static-recompilation) | Static recompilation of Ace Combat 5 with native rendering | 108 | 🟢 | C |
| [RidgeRacer6-Recompilation](https://github.com/Sirhalo23/RidgeRacer6-Recompilation) | Recompilation of Ridge Racer 6 (Xbox 360) for PC | 108 | 🟢 | C++ |
| [SARecomp](https://github.com/sonicfreak1337/SARecomp) | A fully playable, work-in-progress native Sonic Adventure port for Windows, Linux and Steam Deck. Powered by KatanaRe... | 106 | 🟢 | C++ |
| [SSSV_Recomp](https://github.com/Cellenseres/SSSV_Recomp) | Space Station Silicon Valley static recompilation | 106 | 🟢 | C++ |
| [gr2_pc (Gravity Rush 2)](https://github.com/HayatoG/gr2_pc) | Native PC port (Linux/Windows) of Gravity Rush 2 (PS4) that runs your own game dump | 105 | 🟢 | C++ |
| [DBZ-Burst-Limit-Recompiled](https://github.com/iExplosiveRage/DBZ-Burst-Limit-Recompiled) | Dragon Ball Z: Burst Limit Recompiled - native PC port via ReXGlue static recompilation | 104 | 🟢 | C++ |
| [Forza Motorsport 2 (hl360-Forza2)](https://github.com/0herculabs/hl360-Forza2) | Unofficial native port of Forza Motorsport 2 (Xbox 360) | 104 | 🟢 | C++ |
| [mk8-recomp](https://github.com/dougchansan/mk8-recomp) | Static recompilation of Mario Kart 8 AArch64 code to native x86-64 | 104 | 🟢 | C++ |
| [silent-hill-pc-nightly](https://github.com/SlickAmogus/silent-hill-pc-nightly) | Nightly builds of a Silent Hill 1 PC port based on the PSX decompilation | 104 | 🟢 |  |
| [Demon's Souls](https://github.com/JonathanDC64/DemonsSoulsRecomp) | Static recompilation of Demon's Souls (PS3) into a native PC port | 103 | 🟢 | C++ |
| [Estacado-The-Darkness-Recomp](https://github.com/invinceble55-wq/Estacado-The-Darkness-Recomp) | Estacado: a native PC recompilation of The Darkness (Xbox 360). Unofficial fan port; bring your own copy of the game. | 103 | 🟢 | C++ |
| [Dead Rising 2: Case Zero Recomp](https://github.com/wivi514/Dead_Rising_2_Case_Zero_Xenon_Recomp) | Dead Rising 2: Case Zero Xbox 360 static recompilation | 102 | 🟢 | C++ |
| [God of War: Chains of Olympus (God of War PSP: native PC ports)](https://github.com/DrummingBird1/gow-psp-recomp) | Static recompilation of God of War: Chains of Olympus (PSP) into a native PC port | 102 | 🟢 | C |
| [hercules-recompiled](https://github.com/obaidr1/hercules-recompiled) | Native PC port and decompilation of Disney's Hercules (PlayStation, 1997) | 102 | 🟢 | Python |
| [mscharged-port](https://github.com/previouslevelgames/recharged) | Mario Strikers Charged ported to PC, Mac and Linux from decompiled code | 101 | 🟢 | C++ |
| [NSMB-Wii-Multiplayer-Recompilation](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation) | Static recompilation of New Super Mario Bros. Wii for Android and Windows | 101 | 🟢 | C++ |
| [Roller](https://github.com/FatalDecomp/ROLLER) | Recomp of the game Whiplash/Fatal Racing. Adds enhancements. Playable on PC or online. | 101 | 🟢 | C |
| [NFS-CARBON-360-ANDROID-RECOMP](https://github.com/codepdbh/NFS-CARBON-360-ANDROID-RECOMP) | Static recompilation of Need for Speed Carbon (Xbox 360) for Windows and Android | 99 | 🟢 | JavaScript |
| [Super Mario Galaxy ( PS4 recomp)](https://github.com/chrissotraidis/galaxypad) | Static recompilation of Super Mario Galaxy (Wii) into a native PC port | 99 | 🟢 | Python |
| [banjo-tooie-scurvy-dog-port](https://github.com/some-scurvy-dog/banjo-tooie-scurvy-dog-port) | Banjo-Tooie Recompiled: a native Windows PC port with widescreen, resolution and FPS options, controller support, and... | 98 | 🟢 | C++ |
| [Free-Riders-Recompiled](https://github.com/YuutaTsubasa/Free-Riders-Recompiled) | Unofficial static recompilation of Sonic Free Riders for Windows, Linux and Android, with controller/keyboard support... | 98 | 🟢 | C++ |
| [Theft4](https://github.com/KoreanSeats1/Theft4) | Experimental static AOT recompilation of GTA IV's Xbox 360 build for ARM | 98 | 🟢 | C++ |
| [Dead Rising 2: Case West Recomp](https://github.com/wivi514/Dead_Rising_2_Case_West_Xenon_Recomp) | Dead Rising 2: Case West Xbox 360 static recompilation | 97 | 🟢 | C++ |
| [Hollow Knight: Silksong (Silksong Android)](https://github.com/jakobkhansen/SilksongAndroid) | Unofficial native port of Hollow Knight: Silksong (Mobile) | 97 | 🟢 | C# |
| [Mischief Makers](https://github.com/ThiagoLira/trouble-makers-pc-recomp) | Static recompilation of Mischief Makers (N64) into a native PC port | 97 | 🟢 | C++ |
| [Sundog: Frozen Legacy](https://github.com/laanwj/sundog) | Port of the Atari ST game SunDog: Frozen Legacy (1984) to modern systems | 97 | 🟢 | C |
| [Ultima 7 Decomp](https://github.com/Kitrinx/Ultima7_Decomp) | Recomp of Ultima 7. Bit exact to original. | 97 | 🟢 | C++ |
| [oracles-decomp](https://github.com/kirby-letsgo/oracles-decomp) | Native app for the Game Boy Color Zelda Oracle games | 95 | 🟢 | C |
| [wipeout_pc (WipEout Omega Collection)](https://github.com/AbdelmoumenDeghbouche/wipeout_pc) | Native Windows port of WipEout Omega Collection (PS4) | 95 | 🟢 | C++ |
| [Wave Race 64 Recomp](https://github.com/danielgomesvieira2000/wave-race-64-recomp) | Native PC port of Wave Race 64 via N64 static recompilation | 94 | 🟢 | C++ |
| [Max_Vita](https://github.com/fgsfdsfgs/max_vita) | Tool for Max Payne game data (osgameclones) (C) | 93 | 🔴 | C |
| [wet-recomp](https://github.com/Supermedo/wet-recomp) | Fan PC port of WET (Xbox 360) via ReXGlue static recompilation | 93 | 🟢 | C# |
| [Ape Escape](https://github.com/mstan/ApeEscapeRecomp) | Static recompilation of Ape Escape (PS1) into a native PC port | 92 | 🟢 | C |
| [Earthworm Jim HD: Recompiled](https://github.com/TekRantGaming/earthworm-jim-hd-recompiled) | Earthworm Jim HD (XBLA) static recompilation | 92 | 🟢 | C++ |
| [Einhänder](https://github.com/strider973/Einhander-Recompiled) | Static recompilation of Einhänder (PS1) into a native PC port | 92 | 🟢 | Python |
| [Forza Motorsport 3 (hl360-forza3)](https://github.com/0herculabs/hl360-forza3) | Unofficial native port of Forza Motorsport 3 (Xbox 360) | 92 | 🟢 | C++ |
| [UFO50AndroidUnofficial](https://github.com/Skyline969/UFO50AndroidUnofficial) | Tool to build your own Android version of UFO 50 | 92 | 🟡 | Shell |
| [Crash2Recomp](https://github.com/Zumbo06/Crash2Recomp) | Crash Bandicoot 2 (PS1) translated to native code instead of emulated | 91 | 🟢 | Python |
| [halo-ce-vita](https://github.com/BirchWoodGod/halo-ce-vita) | PS Vita port of Halo: Combat Evolved built on the decompilation | 91 | 🟢 | C |
| [The Legend of Zelda: Ocarina of Time (oot-PSP)](https://github.com/z2442/oot-PSP) | Unofficial native port of The Legend of Zelda: Ocarina of Time (N64) | 91 | 🟢 | C |
| [goldeneye-metal](https://github.com/ysrdevs/goldeneye-metal) | Experimental source-only static recompilation of GoldenEye 007 | 88 | 🟢 | C |
| [ArmyOfTwoRecomp](https://github.com/nikolaygorb/ArmyOfTwoRecomp) | Army of Two (Army of 2) 2008 [Xbox360] game static recompilation project based on RexGlue-SDK | 87 | 🟢 | C++ |
| [redalert2-recomp](https://github.com/sp00nznet/redalert2-recomp) | Static recompilation of Command & Conquer: Red Alert 2 / Yuri's Revenge (Westwood, 2000-01) to native C, with the rem... | 87 | 🟢 | C |
| [SpaceRangersHD_FPC](https://github.com/pakompom/SpaceRangersHD_FPC) | Cross-platform port of Space Rangers HD: A War Apart based on its decompilation | 87 | 🟢 | Pascal |
| [3dpinball-nds](https://github.com/headshot2017/3dpinball-nds) | Nintendo DS port of the Space Cadet Pinball decompilation | 86 | 🟡 | C++ |
| [Ace-Combat-X-Recompilation](https://github.com/sal063/Ace-Combat-X-Recompilation) | Static recompilation of ACE COMBAT X with a native renderer | 86 | 🟢 | C |
| [cartridge](https://github.com/TriwindBryan/fulton) | Launcher for decomp, recomp and remake PC ports of classic games | 86 | 🟢 | JavaScript |
| [OpenCMR2](https://github.com/pablocpas/OpenCMR2) | Native SDL3 port of Colin McRae Rally 2.0 built from the CMR2Decomp decompilation | 86 | 🟢 | C++ |
| [PoN_PC (Rockman EXE Phantom of Network)](https://github.com/StraDaMa/PoN_PC) | Unofficial native port of Rockman EXE Phantom of Network (Mobile) | 85 | 🟢 |  |
| [pcrecomp](https://github.com/sp00nznet/pcrecomp) | Toolbox for statically recompiling old PC (DOS/Windows) software to native code | 84 | 🟢 | C |
| [Project-RE-Visited-RE3](https://github.com/BrazilianHobbyist/Project-RE-Visited-RE3) | Static recompilation and native PC port of Resident Evil 3: Nemesis (PS1) | 84 | 🟢 | C++ |
| [DQ8-Recompiled](https://github.com/Sinan-Karakaya/DQ8-Recompiled) | Recompilation of Dragon Quest VIII (PS2) to run natively on PC and Mac | 83 | 🟢 | C++ |
| [F-Zero](https://github.com/mstan/FZeroSNESRecomp) | Static recompilation of F-Zero (SNES) into a native PC port | 83 | 🟢 | C |
| [Fight Night Champion](https://github.com/whompay/FNCReborn) | Static recompilation of Fight Night Champion (Xbox 360) into a native PC port | 83 | 🟢 | Rust |
| [lost-odyssey-hd-remaster](https://github.com/faligame/lost-odyssey-hd-remaster) | Lost Odyssey HD Remaster: a native PC build of Lost Odyssey (Xbox 360) via static recompilation. 720p to 4K with an e... | 83 | 🗄️ | C |
| [SWROTS-PC](https://github.com/jedijosh920/SWROTS-PC) | Unofficial native Windows port of Star Wars Episode III: Revenge of the Sith (Xbox) | 83 | 🟢 | C++ |
| [fukami](https://github.com/danisandoval/fukami) | Native macOS / Steam Deck port of Ridge Racer V by static recompilation | 82 | 🟢 | C++ |
| [WindWakerHD-Android-Plus](https://github.com/Nycolazs/WindWakerHD-Android-Plus) | The Legend of Zelda: The Wind Waker HD natively on Android (static recompilation, Vulkan). Built-in Brazilian Portugu... | 82 | 🟢 | C++ |
| [foxhollow](https://github.com/JackPriceBurns/foxhollow) | Star Fox Adventures decompilation powering the FoxHollow native PC port | 81 | 🟢 | C |
| [Pilotwings 64 Recomp](https://github.com/danielgomesvieira2000/pilotwings-64-recomp) | Native PC port of Pilotwings 64 statically recompiled with N64Recomp, widescreen and high FPS | 81 | 🟢 | C++ |
| [The Legend of Zelda: The Wind Waker](https://github.com/centollOS/SwitchWaker) | Unofficial native port of The Legend of Zelda: The Wind Waker (GameCube) | 81 | 🟢 | C++ |
| [doa3-recomp](https://github.com/parkerallan/doa3-recomp) | Dead or Alive 3 PC Port | 80 | 🟢 | Assembly |
| [Street Fighter Alpha 3](https://github.com/TechnicallyComputers/Street-Fighter-Alpha-3-Recomp) | Static recompilation of Street Fighter Alpha 3 (PS1) into a native PC port | 80 | 🟢 | C |
| [BloodyRoar2Recomp](https://github.com/novapowers0/BloodyRoar2Recomp) | Bloody Roar II PlayStation static recompilation | 79 | 🟢 | C |
| [Ogre Battle 64 Recompiled](https://github.com/lfarroco/ogre-battle-64-recomp) | Static recompilation of Ogre Battle 64 to native PC | 79 | 🟢 | Assembly |
| [Ports-Launcher](https://github.com/Nyaldee/Ports-Launcher) | Library manager and installer for unofficial native game ports | 79 | 🟢 | Rust |
| [CPS-2 Recomp](https://github.com/tmcleroy/cps2recomp) | Static recompilation of Capcom CPS-2 arcade games into native PC ports | 77 | 🟢 | C++ |
| [naruto-storm-generations-port](https://github.com/Masterllgod/naruto-storm-generations-port-nativo) | Naruto Shippuden: Ultimate Ninja Storm Generations (Xbox 360) running natively on Android and PC | 77 | 🟢 |  |
| [RoadRash64Recompiled](https://github.com/linkssy2/RoadRash64Recompiled) | Unofficial PC recompilation of Road Rash 64 | 77 | 🟢 | C++ |
| [skate2-recompile-pc](https://github.com/christianortel/skate2-recompile-pc) | Community Windows PC port of Skate 2 (Xbox 360) built with ReXGlue static recompilation | 77 | 🟢 | PowerShell |
| [Ratchet & Clank (rac1-native)](https://github.com/RAC-Native/rac1-native-game) | Unofficial native port of Ratchet & Clank (PS2) | 76 | 🟢 | C++ |
| [Project-2099](https://github.com/GenryTheFox0/Project-2099) | Spider-Man: Edge of Time Xbox 360 static recompilation | 75 | 🟢 | C# |
| [The Legend of Zelda: Oracle of Ages/Seasons](https://github.com/thibautbus/top) | Unofficial native port of The Legend of Zelda: Oracle of Ages/Seasons (Game Boy Color) | 75 | 🟢 | C |
| [TooTawersRecomp](https://github.com/Gumpolas/TooTawersRecomp) | Native Windows port of The Lord of the Rings: The Two Towers (Xbox, 2002) via static recompilation | 75 | 🟢 | C |
| [FIFA 09 (FIFA 09 PC)](https://github.com/ChunchunQ/fifa09-recomp) | Static recompilation of FIFA 09 (Xbox 360) into a native PC port | 74 | 🟢 | C++ |
| [Rayman3Readvanced](https://github.com/RayCarrot/Rayman3Readvanced) | PC port of Rayman 3 GBA | 74 | 🟢 | C# |
| [WWE 2K14 (WWE 2K14 Recomp)](https://github.com/PromethenDev/wwe2k14-recomp) | Static recompilation of WWE 2K14 (Xbox 360) into a native PC port | 74 | 🟢 | C++ |
| [Paper Mario port](https://github.com/SecondaryLifer/StarHaven) | Native Nintendo 3DS port of Paper Mario (N64) built from the decompilation | 73 | 🟢 | C |
| [MarioKartSuperCircuitRecomp](https://github.com/mstan/MarioKartSuperCircuitRecomp) | Static recompilation of Mario Kart: Super Circuit | 72 | 🟢 | C++ |
| [Need for Speed: Most Wanted (NFS Most Wanted PC Recompiled (NFS Android Evolved))](https://github.com/codepdbh/nfsmwpc-recompiled) | Static recompilation of Need for Speed: Most Wanted (PC) into a native PC port | 72 | 🟢 | C++ |
| [asuras-wrath-recomp](https://github.com/PauloUbirajara/asuras-wrath-recomp) | Recomp of Asura's Wrath using RexGlue for PC (wip) | 71 | 🟢 | C++ |
| [dusklight](https://github.com/HayatoG/dusklight) | Switch port of the Twilight Princess decompilation | 71 | 🟢 | C++ |
| [ac3-remix](https://github.com/i5han/ac3-remix) | PC port and remaster of Ace Combat 3: Electrosphere | 70 | 🟢 |  |
| [auto-tmc (The Minish Cap)](https://github.com/StonedModder/auto-tmc) | GUI that automates building the Minish Cap decompilation PC port from your own ROM | 70 | 🟢 | Python |
| [OpenPhantom](https://github.com/OpenPhantom/OpenPhantom) | Star Wars Episode I: The Phantom Menace (1999) PC modernized with online co-op multiplayer for up to 4 players. Play... | 70 | 🟢 | C |
| [TWIPE_00Sheven](https://github.com/riseio/TWIPE_00Sheven) | Static recompilation of the N64 game The World Is Not Enough | 70 | 🟢 | C++ |
| [UrbanChaosRiotResponseBurnerEdition](https://github.com/linkssy2/UrbanChaosRiotResponseBurnerEdition) | Urban Chaos: Riot Response hybrid recompilation for Windows PC from the Xbox version | 70 | 🟢 | C |
| [Jet Force Gemini](https://github.com/TK22-26/JetForceGemini-Recomp) | Static recompilation of Jet Force Gemini (N64) into a native PC port | 69 | 🟢 | Python |
| [Prince of Persia: The Sands of Time (reSOT)](https://github.com/FulGerNet/rePOP) | Static recompilation of Prince of Persia: The Sands of Time (Xbox) into a native PC port | 69 | 🟢 | C |
| [Underworld Exhumed](https://github.com/abedegno/underworld-exhumed) | Bit-exact recomp of Ultima Underworld I and II. | 69 | 🟢 | C |
| [Hyrule Warriors: Definitive Edition (Hyrule Warriors: Definitive Edition Recomp)](https://github.com/sonsegajp/HWDER) | Static recompilation of Hyrule Warriors: Definitive Edition (Switch) into a native PC port | 68 | 🟢 | C++ |
| [OpenCrossing-Anbernic](https://github.com/TechProGabe/OpenCrossing-Anbernic) | Animal Crossing running natively on Anbernic handhelds | 68 | 🟢 | C |
| [ShaolinMonks-Android](https://github.com/RanggaCasper/ShaolinMonks-Android) | Android port of Mortal Kombat: Shaolin Monks (Xbox), statically recompiled with XboxXBE-Recomp | 68 | 🟢 | C++ |
| [beetle-adventure-racing-recomp](https://github.com/danielgomesvieira2000/beetle-adventure-racing-recomp) | Static recompilation port of Beetle Adventure Racing (N64) to native PC, with widescreen, high-FPS and modern input | 67 | 🟢 | C++ |
| [Open Annihilation](https://github.com/open-annihilation/open-annihilation) | Recomp of Total Annihilation and Total Annihilation: Kingdoms (RTS). | 67 | 🟢 | C++ |
| [Tekken3Recompiled](https://github.com/FishB0nes98/Tekken3Recompiled) | Tekken 3 hybrid recompilation preview with Jun Kazama, widescreen, custom skins and local asset import tools. | 67 | 🟢 | C++ |
| [vf2-recomp](https://github.com/mr-finster/vf2-recomp) | Virtua Fighter 2 (Sega Model 2) arcade i960 program recompiled to native code for Mac, Windows, Steam Deck | 67 | 🟢 | C++ |
| [gears-of-war-2-pc-port](https://github.com/santiquiroz/gears-of-war-2-pc-port) | Static recompilation of Gears of War 2 (Xbox 360) into a native PC port | 66 | 🟢 | C++ |
| [gow2-recomp](https://github.com/andrebrumdev/gow2-recomp) | God of War II HD static recompilation — curated work artifacts (lift boundaries, SPU lift sources, scripts, findings)... | 66 | 🟢 | Python |
| [Kameo: Elements of Power](https://github.com/MaxDeadBear/KameoRePowered) | Static recompilation of Kameo: Elements of Power (Xbox 360) into a native PC port | 66 | 🟢 | Python |
| [smash64r](https://github.com/zestydevy/smash64r) | Static recompilation of Super Smash Bros. for PC (Windows/Linux) | 66 | 🟡 | C++ |
| [TLG-Port (The Last Guardian)](https://github.com/SulphurS16/TLG-Port) | Unofficial native Windows port of The Last Guardian (PS4) | 66 | 🟢 | Rust |
| [MOTHER 3](https://github.com/josiahg2502-glitch/Mother3Recomp) | Static recompilation of MOTHER 3 (GBA) into a native PC port | 65 | 🟢 | C |
| [Super Street Fighter II Turbo HD Remix](https://github.com/saulob/ssf2t-hd-remix-recompiled) | Static recompilation of Super Street Fighter II Turbo HD Remix (Xbox 360) into a native PC port | 65 | 🟢 | C++ |
| [xenogears-recomp](https://github.com/OpokXeno/xenogears-recomp) | Static recompilation of Xenogears for PC | 65 | 🟢 | C |
| [2014 FIFA World Cup Brazil](https://github.com/HossEz/fifa-world-cup-2014-recompiled) | Static recompilation of 2014 FIFA World Cup Brazil (Xbox 360) into a native PC port | 64 | 🟢 | C++ |
| [GSRecomp](https://github.com/Shmargus/GSRecomp) | Golden Sun GBA static recompilation | 64 | 🟢 | C++ |
| [Super Mario 64 (libsm64-unity)](https://github.com/libsm64/libsm64-unity) | Unofficial native port of Super Mario 64 (N64) | 64 | 🔴 | C# |
| [Chameleon Twist: Recompiled](https://github.com/Rainchus/ChameleonTwist1-JP-Recomp) | Chameleon Twist static recompilation | 63 | 🟡 | C++ |
| [Diablo (diablo_web))](https://github.com/JohnImril/diablo_web) | Unofficial native port of Diablo (diablo_web)) (PC) | 63 | 🟢 | TypeScript |
| [MojoRecomp](https://github.com/OAleex/MojoRecomp) | Native PC recompilation project for Crash of the Titans | 63 | 🟢 | C++ |
| [Rallisport Challenge 2 decomp](https://github.com/Mortify7612/RallisportChallenge2-decomp) | Recompilation of Rallisport Challenge 2 (2004) for Linux and Windows | 63 | 🟢 | C |
| [gbarecomp (mstan)](https://github.com/mstan/gbarecomp) | Static recompiler for Game Boy Advance games | 62 | 🟢 | C++ |
| [NaughtyBear_ReStuff](https://github.com/MaxDeadBear/NaughtyBear_ReStuff) | NaughtyBear_ReStuff | 62 | 🟢 | C++ |
| [ndsrecomp](https://github.com/RetroPortingToolKit/ndsrecomp) | Early Nintendo DS static recompiler research | 62 | 🟢 | C++ |
| [SMB-Vanilla](https://github.com/nukep/SMB-Vanilla) | C decompilation and port of NES Super Mario Bros and The Lost Levels | 62 | 🟢 | C |
| [Super Mario World (SMAS_Launcher)](https://github.com/stephini/SMAS_Launcher) | Unofficial native port of Super Mario World (SNES) | 62 | 🔴 | Python |
| [NHL 24 PC](https://github.com/HajDEO/nhl24pc) | Unofficial native port of NHL 24 PC (PS4) | 61 | 🟢 | C++ |
| [vf1-recomp](https://github.com/mr-finster/vf1-recomp) | Virtua Fighter (Sega Model 1) statically recompiled for Mac, Windows and Steam Deck | 61 | 🟢 | C++ |
| [HaloCE DecompRemix VR](https://github.com/moistman42069/HaloCE-DecompRemix-VR-PC-Android) | OpenCE-based Halo: Combat Evolved port for standalone VR headsets, PC and Android | 59 | 🟢 | C |
| [max_nx (Max Payne)](https://github.com/fgsfdsfgs/max_nx) | Nintendo Switch port of Max Payne that loads the Android version's binaries | 59 | 🟢 | C |
| [sk82-recomp](https://github.com/Skate-2-Team/sk82-recomp) | A static recompilation of Skate 2 to build a PC port. | 59 | 🗄️ | C++ |
| [spaghettipad (Mario Kart 64)](https://github.com/chrissotraidis/spaghettipad) | Mario Kart 64 on iPhone and iPad via SpaghettiKart with Metal rendering | 59 | 🟢 | Objective-C++ |
| [The Legend of Zelda: Breath of the Wild (BotW Recompiled)](https://github.com/IshaanKalra2103/BotWRecomp) | Static recompilation of The Legend of Zelda: Breath of the Wild (Switch) into a native PC port | 59 | 🟢 | C++ |
| [King's Field](https://github.com/Voicedrew11/verdite2) | Static recompilation of King's Field (PS1) into a native PC port | 58 | 🟢 | C# |
| [mcdub3-nx](https://github.com/laureladastra/mcdub3-nx) | Midnight Club 3: DUB Edition recompiled to run natively on Switch, Linux and Mac | 58 | 🟢 | C |
| [mkwii-ps5](https://github.com/Phi1ow/mkwii-ps5) | Mario Kart Wii PAL on PS5 via native static recompilation | 58 | 🟢 | C++ |
| [OpenXvT](https://github.com/elyosh/OpenXvT) | Open-source recomp of X-Wing vs Tie Fighter. | 58 | 🟢 | C |
| [Rock Band 3 (Xbox 360)](https://github.com/ihatecompvir/band3_recomp) | Xbox 360 static recompilation of Rock Band 3 (Xbox 360) | 58 | 🟢 | C++ |
| [rush2recompiled](https://github.com/bryantmh/rush2recompiled) | Recompilation of the N64 game Rush 2 | 58 | 🟢 | C++ |
| [snprecomp](https://github.com/wootbeer/snprecomp) | Static recompilation of Sin and Punishment (N64) | 58 | 🟢 | C++ |
| [The Legend of Zelda: A Link to the Past](https://github.com/mstan/ZeldaAlttPSNESRecomp) | Static recompilation of The Legend of Zelda: A Link to the Past (SNES) into a native PC port | 58 | 🟢 | C |
| [wc1-re](https://github.com/neuromancer/wc1-re) | Open-source recomp of Wing Commander I. | 58 | 🟢 | C |
| [iPodClickWheelRecomps](https://github.com/DogParty/iPodClickWheelRecomps) | An assortment of iPod Classic games that have been recompiled to run on modern systems | 57 | 🟢 | Rust |
| [New Super Mario Bros. U](https://github.com/nsmbu-recomp/nsmbu-recomp) | Static recompilation of New Super Mario Bros. U (Wii U) into a native PC port | 57 | 🟢 | C++ |
| [P3P3DS](https://github.com/endercodezz/P3P3DS) | Persona 3 Portable port for the New Nintendo 3DS | 57 | 🟢 | C++ |
| [time-crisis-2-vr](https://github.com/DR-89/time-crisis-2-vr) | Native Time Crisis II VR port for Quest 3 and PCVR built on the Namco System 22 decompilation | 57 | 🟢 | C |
| [urban-reign-recomp](https://github.com/thiagordsfx/urban-reign-recomp) | Urban Reign (PS2) static recompilation: native PC port with 60 FPS and high resolution | 57 | 🟢 | C++ |
| [LEGO Island (isle.pizza (Emscripten build of isle-portable))](https://github.com/isledecomp/isle.pizza) | Browser (WebAssembly) port of LEGO Island (PC) | 56 | 🟢 | JavaScript |
| [Plants vs. Zombies (pvz-ps2-wii)](https://github.com/OptiJuegos/pvz-ps2-wii) | Unofficial native port of Plants vs. Zombies (PC) | 56 | 🟢 | C++ |
| [Splatterhouse Recompiled](https://github.com/0c0de/splatterhouse-decomp) | Native PC port of Splatterhouse (2010, Xbox 360) via ReXGlue static recompilation | 56 | 🟢 | C++ |
| [GameCubeRecompiled](https://github.com/KaiserGranatapfel/GameCubeRecompiled) | Experimental static recompilation of GameCube games into Rust | 55 | 🟢 | Rust |
| [GoldenEye 007 (GoldenEye 007 XBLA PC Recomp)](https://github.com/CaiusCodes/GoldenEye-007-XBLA-PC-Recomp) | Static recompilation of GoldenEye 007 (Xbox 360) into a native PC port | 55 | 🟢 | C++ |
| [IsaacRecomp](https://github.com/whylurking/IsaacRecomp) | Native C++ recompilation of The Binding of Isaac (Flash) for Windows, Linux and Switch | 55 | 🟢 | C++ |
| [Mario Party 4 (Party Board (zeranemesis port))](https://github.com/zeranemesis/Marioparty4) | Unofficial native port of Mario Party 4 (GameCube) | 55 | 🟢 | C |
| [nfsu1-recompiled](https://github.com/codepdbh/nfsu1-recompiled) | Need for Speed: Underground (2003) statically recompiled for Windows and Android | 55 | 🟢 | C++ |
| [regaiden-recomp](https://github.com/sergiomanzur/regaiden-recomp) | Native static recompilation of Resident Evil Gaiden (GBC) for PC | 55 | 🟢 | C |
| [50 Cent: Blood on the Sand](https://github.com/nlwstein/skullburglar) | Static recompilation of 50 Cent: Blood on the Sand (Xbox 360) into a native PC port | 54 | 🟢 | C++ |
| [Armored Core: For Answer (ACFA-Port)](https://github.com/SulphurS16/ACFA-Port) | Unofficial native port of Armored Core: For Answer (Xbox 360) | 54 | 🟢 | C++ |
| [Far Cry Instincts (fci-recomp)](https://github.com/VinceIP/fci-recomp) | Static recompilation of Far Cry Instincts (Xbox) into a native PC port | 54 | 🟢 | C++ |
| [Re-Cherry](https://github.com/MaxDeadBear/Re-Cherry) | Re-Cherry | 54 | 🟢 | C++ |
| [SM2-Recomp](https://github.com/SirSymo/SM2-Recomp) | Native recompilation of Spider-Man 2 (original Xbox) | 54 | 🟢 |  |
| [Geometry Wars: Retro Evolved 2 Recompiled](https://github.com/saulob/geometry-wars-retro-evolved-2-recompiled) | Native PC port of Geometry Wars: Retro Evolved 2 (Xbox 360) via static recompilation | 53 | 🟢 | C++ |
| [PerfectDarkZeroRecomp](https://github.com/nikolaygorb/PerfectDarkZeroRecomp) | Perfect Dark Zero [Xbox360] game static recompilation project based on RexGlue-SDK | 53 | 🟢 | C++ |
| [VandalHearts-PcPort](https://github.com/HalmyLyseas/VandalHearts-PcPort) | Vandal Hearts native PC port based on a matching decompilation | 53 | 🟢 | C |
| [DQIV-Recompiled](https://github.com/GoldieLeGenie/DQIV-Recompiled) | Native PC version of Dragon Quest IV (DS) via recompilation | 52 | 🟢 | C++ |
| [Genesis 68K Static Recompiler](https://github.com/mstan/segagenesisrecomp) | Sega Genesis / Mega Drive game static recompiler ecosystem · Part of the R.A.I.D. community | 52 | 🟢 | C |
| [Mario Party 4](https://github.com/mariopartyrd/partyboard) | Unofficial native port of Mario Party 4 (GameCube) | 52 | 🟢 | C |
| [Astral Chain (Astral Chain PC)](https://github.com/Puddz/AstralChain-PC) | Static recompilation of Astral Chain (Switch) into a native PC port | 51 | 🟢 | C |
| [NHL Legacy Recomp](https://github.com/puckhead73/nhl-legacy-recomp) | Xbox 360 NHL Legacy recompiled to PC with ReXGlue | 51 | 🟢 | C++ |
| [Spider-Man: Web of Shadows](https://github.com/toowasmir/WebOfShadowsRecomp) | Static recompilation of Spider-Man: Web of Shadows (Xbox 360) into a native PC port | 51 | 🟢 | C++ |
| [Super Mario Bros. Wonder (SMW)](https://github.com/iHaiDeeZ/SMW) | Static recompilation of Super Mario Bros. Wonder (Switch) into a native PC port | 51 | 🟢 | C |
| [SuperMarioAllStarsRecomp](https://github.com/TanookiStudios/SuperMarioAllStarsRecomp) | Static recompilation of Super Mario All-Stars (SNES) for Mac, Windows and Linux | 51 | 🟢 | Java |
| [Tekken 6 (tekken6-recomp)](https://github.com/mahmoud-mess/tekken6-recomp) | Static recompilation of Tekken 6 (Arcade) into a native PC port | 51 | 🟢 | C++ |
| [The Legend of Zelda: Majora's Mask (MaskPad)](https://github.com/chrissotraidis/maskpad) | Unofficial native port of The Legend of Zelda: Majora's Mask (N64) | 51 | 🟢 | Objective-C++ |
| [Little Planet](https://github.com/carl0srmz/littleplanet) | Sonic CD (Mega-CD) byte-identical disassembly plus static recompilation into a native PC port | 50 | 🟢 | Assembly |
| [meleepad (Super Smash Bros. Melee)](https://github.com/chrissotraidis/meleepad) | Super Smash Bros. Melee port running natively on iOS and iPadOS | 50 | 🟢 | Python |
| [nfs-carbon-recomp](https://github.com/Sampreeth004/nfs-carbon-recomp) | Static recompilation of Need for Speed: Carbon (Xbox 360) to native C++ | 50 | 🟢 | C++ |
| [WetRecomp](https://github.com/nikolaygorb/WetRecomp) | Wet [Xbox360] game static recompilation project based on RexGlue-SDK | 50 | 🟢 | C++ |
| [360tools](https://github.com/sp00nznet/360tools) | Toolkit to statically recompile Xbox 360 games to native PC executables | 49 | 🟢 | Python |
| [ChaotixRecompiled](https://github.com/YuutaTsubasa/ChaotixRecompiled) | Static recompilation of the Sega 32X game Knuckles' Chaotix into native C++ (Windows/Linux/macOS/Android), with true... | 49 | 🟢 | C++ |
| [God of War](https://github.com/YYOzcan/Tobiichi-Port) | Unofficial native port of God of War (PS2) | 49 | 🟢 | C++ |
| [God of War: Ghost of Sparta](https://github.com/arnaldolima1/gow-ghost-of-sparta-pc) | Static recompilation of God of War: Ghost of Sparta (PSP) into a native PC port | 49 | 🟢 | Shell |
| [Need for Speed III: Hot Pursuit (nfs3recompiled-android)](https://github.com/ZloiKILLER/nfs3recompiled-android) | Static recompilation of Need for Speed III: Hot Pursuit (PC) into a native PC port | 49 | 🟢 | C++ |
| [Project8Recomp](https://github.com/theokyr/Project8Recomp) | Tony Hawk's Project 8 Xbox 360 static recompilation | 49 | 🟢 | C++ |
| [Rockstar Table Tennis](https://github.com/davidptrssvea/Table-Tennis-Rockstar-PC) | Static recompilation of Rockstar Table Tennis (Xbox 360) into a native PC port | 49 | 🟢 | C++ |
| [sf64-dc](https://github.com/jnmartin84/sf64-dc) | Sega Dreamcast port of the Star Fox 64 decompilation | 49 | 🟢 | C |
| [th06-sdl2](https://github.com/CNTianQi233/th06-sdl2) | Rebuild of the Touhou 6 decompilation on SDL2 and OpenGL | 49 | 🟢 | C++ |
| [WWE '12 (wwe12-pc)](https://github.com/iMrBurn/wwe12-pc) | Static recompilation of WWE '12 (Xbox 360) into a native PC port | 49 | 🟢 | C++ |
| [Kirby64Recomp](https://github.com/Kirby64Ret/Kirby64Recomp) | Kirby 64 Recomp (ok fine i'll use cmake) | 48 | 🟢 | C++ |
| [MegaManX2Recomp](https://github.com/mstan/MegaManX2Recomp) | Static recompilation of Mega Man X2 (SNES) | 48 | 🟢 | Python |
| [pokeemerald-3d](https://github.com/tripplyons/pokeemerald-3d) | Pokemon Emerald in 3D (in WebAssembly) | 48 | 🟢 | C |
| [Super Mario 64 in Scratch (sm64-scratch)](https://github.com/naegoxdev/sm64-scratch) | Unofficial native port of Super Mario 64 in Scratch (N64) | 48 | 🟢 | Python |
| [Wipeout XL (Wipeout XL Recompiled)](https://github.com/NJH-1001/Wipeout2K97XL) | Static recompilation of Wipeout XL (PS1) into a native PC port | 48 | 🟢 | C |
| [.hack//Recompilation](https://github.com/dothacktranslate/dothack-recompilation) | Native recompilation project for the PS2 .hack//IMOQ quadrilogy | 47 | 🟢 | Python |
| [automobililamborghini-recomp](https://github.com/alondero/automobililamborghini-recomp) | Automobili Lamborghini (N64) static recompilation | 47 | 🟢 | C++ |
| [Hollow Knight (HK: Dual Souls)](https://github.com/igawa6/dualsouls) | Unofficial native port of Hollow Knight (Mobile) | 47 | 🟢 | C# |
| [pocket-native](https://github.com/whovian64/pocket-native) | Nintendo 3DS games recompiled for the R36S and other Linux handhelds | 47 | 🟢 | Rust |
| [RB2](https://github.com/WistfulHopes/RB2) | Dragon Ball Raging Blast 2 Recompiled | 47 | 🟢 | C++ |
| [SSX 3](https://github.com/koenhendriks/SSX3-recomp) | Static recompilation of SSX 3 (Xbox) into a native PC port | 47 | 🟢 | C |
| [The Legend of Zelda: Majora's Mask (MMRecompRando)](https://github.com/RecompRando/MMRecompRando) | Static recompilation of The Legend of Zelda: Majora's Mask (N64) into a native PC port | 47 | 🟢 | C |
| [Destroy All Humans! Path of the Furon](https://github.com/masterspike52/reDAHM) | Xbox 360 static recompilation of Destroy All Humans! Path of the Furon | 46 | 🟢 | C++ |
| [hard-corps-uprising-recompiled](https://github.com/saulob/hard-corps-uprising-recompiled) | Native PC port of Hard Corps: Uprising (Xbox Live Arcade) via static recompilation, with the TRG launcher | 46 | 🟢 | C++ |
| [MKVDCU-Recomp](https://github.com/KawaiiBunga/MKVDCU-Recomp) | Unofficial PC recompilation of Mortal Kombat vs. DC Universe | 46 | 🟢 | C++ |
| [Project Gotham Racing 2 (pgr2-recomp)](https://github.com/hk21x/pgr2-recomp) | Static recompilation of Project Gotham Racing 2 (Xbox) into a native PC port | 46 | 🟢 | C++ |
| [Silent Hill 2 (sh2-nx)](https://github.com/cutarev/sh2-nx) | Static recompilation of Silent Hill 2 (PS2) into a native PC port | 46 | 🟢 | C |
| [skate3-android](https://github.com/andrewnakas/skate3-android) | Skate 3 on Android via native recompilation | 46 | 🟢 | Kotlin |
| [Halo 3 (Delta)](https://github.com/twist84/halo3_cache_release_recomp) | Xbox 360 static recompilation of Halo 3 (Delta) | 45 | 🟢 | C++ |
| [pokerecomp](https://github.com/Decryptu/pokerecomp) | A native Godot 4 reimplementation of the Gen 1 and 2 Game Boy Color games. Not an emulator, bring your own ROM. | 45 | 🟢 | GDScript |
| [Super Mario 64 (libsm64-rust)](https://github.com/nickmass/libsm64-rust) | Unofficial native port of Super Mario 64 (N64) | 45 | 🟢 | Rust |
| [tomodachi-ltd-recomp](https://github.com/RussoPhone/tomodachi-ltd-recomp) | Native PC build of Tomodachi Life: Living the Dream via static recompilation. Bring your own copy — no game files inc... | 45 | 🟢 | Python |
| [infinite-undiscovery-recomp](https://github.com/doc-haz/infinite-undiscovery-recomp) | Native PC recompilation of Infinite Undiscovery | 44 | 🟢 | C++ |
| [PlayStunts](https://github.com/ACatWithEbola/playstunts) | Recomp of Stunts to TypeScript, playable online. | 44 | 🟢 | TypeScript |
| [re-wor](https://github.com/ronniecloud/re-wor) | Native recompilation of Guitar Hero: Warriors of Rock (Xbox 360) for PC | 44 | 🟢 | C++ |
| [Sensible World of Soccer 96/97 (OpenSWOS)](https://github.com/benbaker76/OpenSWOS) | Unofficial native port of Sensible World of Soccer 96/97 (Amiga) | 44 | 🟢 | C |
| [syphon-filter-2-recomp](https://github.com/alexbeavs-ps1-ports/syphon-filter-2-recomp) | Experimental Syphon Filter 2 static recompilation for Windows | 44 | 🟢 | Python |
| [Yakuza-Dead-Souls-EX](https://github.com/canersaka/Yakuza-Dead-Souls-Recompiled) | Yakuza: Dead Souls recompilation effort | 44 | 🟢 | C |
| [buffy-chaos-bleeds-pc](https://github.com/KaikoClanworth1/buffy-chaos-bleeds-pc) | Unofficial native PC port of Buffy the Vampire Slayer: Chaos Bleeds (Xbox); bring your own disc | 43 | 🟢 | C |
| [FZeroRecomp](https://github.com/craigshaw/FZeroRecomp) | Static recompilation of F-Zero to native PC | 43 | 🟢 | C |
| [Metal Gear Solid (mgs-reintegral)](https://github.com/Drommedhar/mgs-reintegral) | Unofficial native port of Metal Gear Solid (PS1) | 43 | 🟢 | C |
| [OpenSpideyPS1](https://github.com/GTTeancum/SpideyPS1recomp) | Recomp of Spider-Man PS1 and Spider-Man 2: Enter Electro to PC. | 43 | 🟢 | C# |
| [SotE-Recomp](https://github.com/GTTeancum/SotE-Recomp) | Static recompilation of Star Wars: Shadows of the Empire (N64) | 43 | 🟢 | C++ |
| [The Legend of Zelda: Echoes of Wisdom (EoWRecomp)](https://github.com/Nycolazs/EoWRecomp) | Static recompilation of The Legend of Zelda: Echoes of Wisdom (Switch) into a native PC port | 43 | 🟢 | C |
| [Virtua Fighter 3](https://github.com/mr-finster/vf3-recomp) | Static recompilation of Virtua Fighter 3 (Arcade) into a native PC port | 43 | 🟢 | C++ |
| [WCWvsNWOWorldTourRecomp](https://github.com/jessetbh/WCWvsNWOWorldTourRecomp) | WCW vs. nWo: World Tour N64 static recompilation | 43 | 🟢 | C++ |
| [WWE-AllStars-Recomp](https://github.com/shaneomac1337/WWE-AllStars-Recomp) | Unofficial Windows version of WWE All Stars (Xbox 360), recompiled with ReXGlue. Bring your own disc image. | 43 | 🟢 | C++ |
| [Armored Core 4 (AC4-Port)](https://github.com/SulphurS16/AC4-Port) | Unofficial native port of Armored Core 4 (PS3) | 42 | 🟢 | C++ |
| [Decomp Buddy](https://github.com/TanookiStudios/decomp-buddy) | Tool that sets up fan-made PC ports and decompilation builds from your own game files | 42 | 🟢 | JavaScript |
| [Grand Theft Auto IV](https://github.com/luisxl15/GTA-IV-RECOMP-XBOX-360) | Static recompilation of Grand Theft Auto IV (Xbox 360) into a native PC port | 42 | 🟢 | Python |
| [nfsmw-ios](https://github.com/bep1s69/nfsmw-ios) | Static recompilation port of Need for Speed Most Wanted (Xbox 360) for iOS | 42 | 🟢 | Python |
| [paperpad (Paper Mario)](https://github.com/chrissotraidis/paperpad) | Paper Mario (N64) port for macOS, iOS and iPadOS | 42 | 🟢 | Objective-C++ |
| [Rocket-R](https://github.com/ThatGuyMcd/Rocket-R) | Rocket: Robot on Wheels static recompilation | 42 | 🟢 | C++ |
| [Super Mario Bros.](https://github.com/mstan/SuperMarioBrosNESRecomp) | Static recompilation of Super Mario Bros. (NES) into a native PC port | 42 | 🟢 | C |
| [the-browsing-of-isaac](https://github.com/chiikabu/the-browsing-of-isaac) | The Binding of Isaac: Repentance+ recompiled to WebAssembly, playable in the browser. | 42 | 🟢 | JavaScript |
| [aerogauge-recomp](https://github.com/alondero/aerogauge-recomp) | Static recompilation of AeroGauge for the Nintendo 64 | 41 | 🟢 | C++ |
| [CafeRecomp](https://github.com/hardkiller2565123123/CafeRecomp) | Wii U static recompilation framework, starting with Breath of the Wild | 41 | 🟢 | C |
| [Diablo III](https://github.com/Boron853/Souls-of-the-Reaper) | Unofficial native port of Diablo III (Xbox 360) | 41 | 🟢 | HTML |
| [ffta-recomp](https://github.com/james2doyle/ffta-recomp) | Native recompilation of Final Fantasy Tactics Advance (GBA) built on the gbarecomp framework | 41 | 🟢 | Python |
| [Forza Motorsport 2 (Forza Motorsport 2 ReGPU)](https://github.com/zer0ducksgiven/Forza-Motorsport-2-ReGPU) | Static recompilation of Forza Motorsport 2 (Xbox 360) into a native PC port | 41 | 🟢 | C++ |
| [Magic-Sushi (MTK)](https://github.com/EXL/Magic-Sushi) | Port of the Magic Sushi game from MediaTek feature-phone OS to SDL and the web | 41 | 🔴 | C |
| [Pokémon Emerald](https://github.com/mstan/EmeraldRecomp) | Static recompilation of Pokémon Emerald (GBA) into a native PC port | 41 | 🟢 | C++ |
| [Street Fighter EX Plus Alpha](https://github.com/guimaraf/plusalpha-recomp) | Static recompilation of Street Fighter EX Plus Alpha (PS1) into a native PC port | 41 | 🟢 | C |
| [The Terminator: SkyNET (skynet-godot)](https://github.com/nautilusbits/skynet-godot) | Unofficial native port of The Terminator: SkyNET (DOS) | 41 | 🟢 | GDScript |
| [deviltouch (Diablo)](https://github.com/chrissotraidis/deviltouch) | DevilutionX (Diablo) port for iPad with direct touch controls | 40 | 🟢 | Python |
| [Downhill Domination port](https://github.com/skuza-oss/downhill-revived) | PC port of Downhill Domination (PS2) built on a matching decompilation | 40 | 🟢 | C |
| [God of War](https://github.com/Waffle565/God-Of-War-Native-Port) | Unofficial native port of God of War (PS2) | 40 | 🟢 | C++ |
| [Grand Theft Auto IV (GTA IV for PS5)](https://github.com/elripalda/gta4-ps5) | Static recompilation of Grand Theft Auto IV (Xbox 360) into a native PC port | 40 | 🟢 | C++ |
| [Grand Theft Auto: Vice City Stories (PSPRecomp-VCS-Android)](https://github.com/codepdbh/PSPRecomp-VCS-Android) | Static recompilation of Grand Theft Auto: Vice City Stories (PSP) into a native PC port | 40 | 🟢 | C++ |
| [Klonoa: Door to Phantomile](https://github.com/TechnicallyComputers/Klonoa-Door-to-Phantomile) | Static recompilation of Klonoa: Door to Phantomile (PS1) into a native PC port | 40 | 🟢 | C |
| [NFSU2Recomp](https://github.com/TalhaMudo/NFSU2Recomp) | Need for Speed: Underground 2 (PC) statically recompiled for Apple Silicon Macs | 40 | 🟢 | C |
| [SoulCalibur II HD Online (Soulcalibur2HD-recomp)](https://github.com/n0madic/Soulcalibur2HD-recomp) | Static recompilation of SoulCalibur II HD Online (Xbox 360) into a native PC port | 40 | 🟢 | C |
| [The Legend of Zelda](https://github.com/mstan/LegendOfZeldaNESRecomp) | Static recompilation of The Legend of Zelda (NES) into a native PC port | 40 | 🟢 | C |
| [Animal Crossing ( animalcrossing-visionos)](https://github.com/chrissotraidis/bellpad) | Unofficial native port of Animal Crossing (GameCube) | 39 | 🟢 | Objective-C++ |
| [ff4_vita (Final Fantasy IV)](https://github.com/Rinnegatamante/ff4_vita) | PS Vita port of Final Fantasy IV (3D remake) via the Android version loader | 39 | 🔴 | C |
| [HuntersRecomp](https://github.com/aabrole/HuntersRecomp) | Metroid Prime Hunters (DS) recompiled to a native dual-screen Android port | 39 | 🟢 | Java |
| [Knightmare (KnightmareAmiga (h0ffman))](https://github.com/djh0ffman/KnightmareAmiga) | Unofficial native port of Knightmare (Amiga) | 39 | 🔴 | Assembly |
| [raider-vita (Tomb Raider)](https://github.com/Rinnegatamante/raider-vita) | PS Vita port of Tomb Raider I and II Classic (Android) via the Android version loader | 39 | 🟡 | C |
| [SanRecomp](https://github.com/OZORDI/SanRecomp) | Unofficial PC port of GTA V (Xbox 360) through static recompilation | 39 | 🟢 | C++ |
| [Strider 2](https://github.com/strider973/STRIDER-2-Recompiled) | Static recompilation of Strider 2 (PS1) into a native PC port | 39 | 🟢 | Python |
| [Animal Crossing (ACGC-Android-Port)](https://github.com/zwaetschge/ACGC-Android-Port) | Unofficial native port of Animal Crossing (GameCube) | 38 | 🟢 | C |
| [Birdman64](https://github.com/NoahVl/Birdman64) | Pilotwings 64 as a native PC game for Windows and Linux: widescreen, 144 Hz+, gamepads. Bring your own ROM, no emulator. | 38 | 🟢 | Rust |
| [Call of Duty 4: Modern Warfare (kisakcod-port (web))](https://github.com/slqntdevss/kisakcod-port) | Unofficial native port of Call of Duty 4: Modern Warfare (PC) | 38 | 🟢 | GSC |
| [EcstaticaRecompiled](https://github.com/spacefarergames/EcstaticaRecompiled) | This is a recomplimation and modern port of Ecstatica 1 and Ecstatica 2 that runs on modern Windows 10 / 11 systems f... | 38 | 🟢 | Assembly |
| [Gran Turismo 2](https://github.com/GTTeancum/OpenGTPS1) | Static recompilation of Gran Turismo 2 (PS1) into a native PC port | 38 | 🟢 | C++ |
| [MHForever](https://github.com/Mango77x/MHForever) | Static recompilation of Monster Hunter Freedom Unite (PSP) into a native PC port | 38 | 🟢 | C++ |
| [outrun2-decomp](https://github.com/r4dius/outrun2-decomp) | OutRun 2006: Coast 2 Coast decompilation ported to many platforms | 38 | 🟢 | C++ |
| [skyroads-sdl](https://github.com/pedrocatalao/skyroads-sdl) | SkyRoads (1993) reverse-engineered and ported natively to SDL2 | 38 | 🟢 | C |
| [3dpinball-dc](https://github.com/headshot2017/3dpinball-dc) | Port of the Space Cadet Pinball decompilation to Dreamcast | 37 | 🟡 | C++ |
| [Earthbound Companion](https://github.com/rages4calm/earthbound-companion) | Recomp of Earthbound (SNES) to PC. | 37 | 🟢 | Python |
| [halo-ce-anbernic-rg35xx](https://github.com/kirklandsig/halo-ce-anbernic-rg35xx) | Halo: Combat Evolved running natively on Anbernic RG35XX H handhelds | 37 | 🟢 | C |
| [Mass Effect (masseffect-nx)](https://github.com/nebadasSwifty/masseffect-nx) | Static recompilation of Mass Effect (Xbox 360) into a native PC port | 37 | 🟢 | C++ |
| [Naruto: The Broken Bond PC Port](https://github.com/Auremana666/Naruto-The-Broken-Bond-PC-Port) | Static recompilation of Naruto: The Broken Bond (Xbox 360) into a native PC port | 37 | 🟢 | C++ |
| [project-bumble (Buck Bumble)](https://github.com/riseio/project-bumble) | Static recompilation of Buck Bumble (N64) into a native port | 37 | 🟢 |  |
| [reo](https://github.com/sp00nznet/reo) | Static recompilation of Resident Evil Outbreak for modern Windows | 37 | 🟢 | C++ |
| [Sensible World of Soccer 96/97 (swos-port)](https://github.com/zlatkok/swos-port) | Unofficial native port of Sensible World of Soccer 96/97 (Amiga) | 37 | 🟢 | Assembly |
| [Shadow of the Colossus](https://github.com/HenryKun55/celosia) | Static recompilation of Shadow of the Colossus (PS2) into a native PC port | 37 | 🟢 | C++ |
| [WWFNoMercyRecomp](https://github.com/jessetbh/WWFNoMercyRecomp) | WWF No Mercy N64 static recompilation | 37 | 🟢 | C |
| [3dpinball-ps2](https://github.com/headshot2017/3dpinball-ps2) | Port of the Space Cadet Pinball decompilation to PlayStation 2 | 36 | 🟡 | C++ |
| [Burnout 2: Point of Impact](https://github.com/timftw21/burnout2-recompilation) | Static recompilation of Burnout 2: Point of Impact (Xbox) into a native PC port | 36 | 🟢 | C++ |
| [conker64-recompiled](https://github.com/Conker64Recomp/conker64-recompiled) | Native PC port of Conker's Bad Fur Day (N64) via Static MIPS Recompilation. SDL2 engine with 3D UV texturing, N64 aud... | 36 | 🟢 | C |
| [Guitar Hero II](https://github.com/YoshiCrystal9/re-gh2) | Xbox 360 static recompilation of Guitar Hero II | 36 | 🟢 | C++ |
| [infamous-first-light-pc](https://github.com/VantageEX/infamous-first-light-pc) | Unofficial native PC port of inFAMOUS First Light (PS4) | 36 | 🟢 | C++ |
| [nfs-carbon-mac](https://github.com/vasist15-source/nfs-carbon-mac) | Need for Speed: Carbon (PC) natively on Apple Silicon Macs via static recompilation | 36 | 🟢 | C++ |
| [PerfectDarkRemasterRecomp](https://github.com/nikolaygorb/PerfectDarkRemasterRecomp) | Perfect Dark Remaster 2010 [Xbox360] game static recompilation project based on RexGlue-SDK | 36 | 🟢 | C++ |
| [Resident Evil 4 (Dreamcast port, re4dc)](https://github.com/lamb2k/re4dc) | Unofficial native port of Resident Evil 4 (Dreamcast) | 36 | 🟢 | C++ |
| [Super Mario Bros. (UEFI_SuperMario)](https://github.com/MikeWuPing/UEFI_SuperMario) | Unofficial native port of Super Mario Bros. (NES) | 36 | 🟢 | C |
| [Tekken Tag Tournament 2 Wii U Edition](https://github.com/Petexy/Tekken-Tag-2-Ultimate-Edition) | Static recompilation of Tekken Tag Tournament 2 Wii U Edition (Wii U) into a native PC port | 36 | 🟢 | C++ |
| [CyPort](https://github.com/Thijs2004/CyPort) | Runs your own copy of Cyberpunk 2077 for Mac natively on iPhone and iPad | 35 | 🟢 | Objective-C |
| [Dark Cloud 2 (DC2-PS2RECOMP)](https://github.com/Red-tv141/DC2-PS2RECOMP) | Static recompilation of Dark Cloud 2 (PS2) into a native PC port | 35 | 🟢 | C++ |
| [Grand Theft Auto: Vice City Stories (Vice City Stories Recomp)](https://github.com/OverkillLabs3/vice-city-stories-recomp) | Static recompilation of Grand Theft Auto: Vice City Stories (PSP) into a native PC port | 35 | 🟢 | C++ |
| [Metal Slug XX](https://github.com/FluffyQuack/rexglue-MetalSlugXX) | Static recompilation of Metal Slug XX (Xbox 360) into a native PC port | 35 | 🟢 | C |
| [MGS2 for Android](https://github.com/luisxl15/METAL-GEAR-SOLID-2-Sons-of-Liberty-for-Android) | Metal Gear Solid 2 HD (NVIDIA Shield build) statically recompiled from ARM32 to ARM64 Android | 35 | 🟢 | C |
| [pokemon-red-sdl2](https://github.com/zacharyvincze/pokemon-red-sdl2) | Pokémon Red reconstructed in C with SDL2 | 35 | 🔴 | C++ |
| [racers-portable](https://github.com/isledecomp/racers-portable) | Portable version of LEGO Racers (1999) built from its decompilation | 35 | 🟢 | C++ |
| [Rayman (Rayverse)](https://github.com/Falcury/rayverse) | Unofficial native port of Rayman (Atari Jaguar) | 35 | 🟢 | C |
| [Silent Hill 3 (sh3-nx, Switch)](https://github.com/cutarev/sh3-nx) | Static recompilation of Silent Hill 3 (PC) into a native PC port | 35 | 🟢 | C |
| [Sonic the Hedgehog](https://github.com/foreverWIP/s1-port) | Unofficial native port of Sonic the Hedgehog (Genesis) | 35 | 🟡 | C |
| [WWE-SVR2010-RECOMP](https://github.com/nefariousjosiah/WWE-SVR2010-RECOMP) | Native PC port of WWE SmackDown vs. Raw 2010 (Xbox 360) via static recompilation | 35 | 🟢 | C++ |
| [castlevania-chronicles-recomp](https://github.com/Spicywonda/castlevania-chronicles-recomp) | Experimental Castlevania Chronicles (PS1) recompilation | 34 | 🟢 | C# |
| [DragonBallZBuusFuryRecomp](https://github.com/mstan/DragonBallZBuusFuryRecomp) | Static recompilation of Dragon Ball Z: Buu's Fury with Adaptive Widescreen · Part of the R.A.I.D. community | 34 | 🟢 | C++ |
| [MindOver-Recomp](https://github.com/Maxilure/MindOver-Recomp) | Unofficial native PC port of Crash: Mind Over Mutant (Xbox 360) via recompilation | 34 | 🟢 | C++ |
| [WWE-SVR2008-RECOMP](https://github.com/nefariousjosiah/WWE-SVR2008-RECOMP) | Native PC port of WWE SmackDown vs. Raw 2008 (Xbox 360) via static recompilation | 34 | 🟢 | C++ |
| [ForzaRecomp](https://github.com/NerunSmarts/ForzaRecomp) | In-progress static recompilation of Forza Horizon 1 | 33 | 🟢 | C++ |
| [fuc-recomp](https://github.com/elprogramadorloco-arch/fuc-recomp) | Hybrid native Fate/unlimited codes project: PSP static-recompilation/gameplay base with PS2 assets and controls in de... | 33 | 🟢 | C++ |
| [gdx-3ds](https://github.com/cruxxxxxx/gdx-3ds) | Unofficial 3DS port of F-Zero X based on its decompilation | 33 | 🟢 | C |
| [MK64 Portable](https://github.com/beckerd/psp_mk64_portable) | Native PSP port of Mario Kart 64 built on the n64decomp/mk64 decompilation | 33 | 🟢 | C |
| [pinball-fantasies-encore](https://github.com/pedrocatalao/pinball-fantasies-encore) | Native remake of Pinball Fantasies (1994 DOS) for macOS, Linux and Windows | 33 | 🟢 | C++ |
| [repentogxm](https://github.com/0xl0cal/repentogxm) | PS Vita port of The Binding of Isaac: Repentance by static recompilation of the PC executable to ARM. | 33 | 🟢 | C |
| [RidgeRacer4Recomp](https://github.com/omegakatana92/RidgeRacer4Recomp) | Native PC port of R4: Ridge Racer Type 4 (PS1) built with PSXRecomp | 33 | 🟢 | PowerShell |
| [Vagrant Story (VS-NativePort)](https://github.com/JEschete/VS-NativePort) | Unofficial native port of Vagrant Story (PS1) | 33 | 🟢 | C |
| [beanRecomp](https://github.com/kholdfuzion/beanRecomp) | In-progress recomp repo for Bean | 32 | 🟡 |  |
| [betrayal-at-krondor](https://github.com/canassa/betrayal-at-krondor) | Betrayal at Krondor: A byte-perfect recompilation of the 1993 classic. | 32 | 🟢 | Assembly |
| [CV64-Recomp](https://github.com/spacefarergames/CV64-Recomp) | Static Recomp and Remaster of Castlevania 64 | 32 | 🟢 | C++ |
| [RecompiledHaloReach](https://github.com/Dyotson/RecompiledHaloReach) | Native PC port of Halo: Reach (Xbox 360) via static recompilation with ReXGlue | 32 | 🟢 | C++ |
| [Sonic Adventure 2: Battle (OpenSA2)](https://github.com/kittycache9/OpenSA2) | Static recompilation of Sonic Adventure 2: Battle (GameCube) into a native PC port | 32 | 🟢 | Python |
| [Timesplitters recomp](https://github.com/GTTeancum/Timesplitters) | Static recompilation of TimeSplitters (PS2) | 32 | 🟢 | C++ |
| [Yoshi's Story (DinoTale)](https://github.com/wootbeer/dinotale) | Static recompilation of Yoshi's Story (N64) into a native PC port | 32 | 🟢 | C++ |
| [Championship Manager: Season 01/02 (02: Bosman Edition)](https://github.com/maxevans60/cm0102-bosman-edition) | Static recompilation of Championship Manager: Season 01/02 (PC) into a native PC port | 31 | 🟢 | C |
| [DB-Final-Bout-Recomp](https://github.com/novapowers0/DB-Final-Bout-Recomp) | Static recompilation of Dragon Ball GT: Final Bout (PS1) for Windows | 31 | 🟢 | Python |
| [Def Jam Vendetta](https://github.com/jcsix694/def-jam-vendetta-recomp) | Static recompilation of Def Jam Vendetta (PS2) into a native PC port | 31 | 🟢 | C++ |
| [F1-Race (MTK)](https://github.com/EXL/F1-Race) | Port of the F1 Race game from MediaTek feature-phone OS to SDL2 and the web | 31 | 🔴 | C |
| [fahrenheit-vita (Fahrenheit)](https://github.com/Rinnegatamante/fahrenheit-vita) | PS Vita port of Fahrenheit: Indigo Prophecy via the Android version loader | 31 | 🟢 | C |
| [goo_vita (World of Goo)](https://github.com/Rinnegatamante/goo_vita) | PS Vita port of World of Goo via the Android version loader | 31 | 🔴 | C |
| [issd-native](https://github.com/sergiomanzur/issd-native) | Native recompilation of International Superstar Soccer Deluxe (SNES) | 31 | 🟢 | C |
| [OpenCrossing-Xbox](https://github.com/TechProGabe/OpenCrossing-Xbox) | Native original Xbox port of Animal Crossing built from the GameCube decompilation | 31 | 🟢 | C |
| [Pokémon FireRed and Pokémon LeafGreen](https://github.com/mstan/FireRedLeafGreenRecomp) | Static recompilation of Pokémon FireRed and Pokémon LeafGreen (GBA) into a native PC port | 31 | 🟢 | Python |
| [Simpsons Wrestling Recompiled](https://github.com/TekRantGaming/simpsons-wrestling-recompiled) | Recomp of Simpsons Wrestling (PS1) to PC. | 31 | 🟢 | C++ |
| [sonic-r-android](https://github.com/ZinexDa/sonic-r-android) | Native Android port of the Sonic R PC decompilation with GLES2 renderer | 31 | 🟢 | C |
| [Super Mario 64 (SM64-PC-Port-WebGL)](https://github.com/NotAn127/SM64-PC-Port-WebGL) | Unofficial native port of Super Mario 64 (N64) | 31 | 🟢 | JavaScript |
| [Super Smash Bros. 64 via the BattleShip decompilation decomp](https://github.com/rockenrooster/Smash64DS_Port) | Nintendo DS port of Super Smash Bros. 64 via the BattleShip decompilation | 31 | 🟢 | C |
| [Alien Resurrection (AlienReRecomp)](https://github.com/DiegoDeDios/AlienReRecomp) | Static recompilation of Alien Resurrection (PS1) into a native PC port | 30 | 🟢 | C |
| [King's Field II](https://github.com/Voicedrew11/verdite3) | Unofficial native port of King's Field II (PS1) | 30 | 🟢 | C# |
| [Metal Gear Solid Recompiled](https://github.com/alexbeavs-ps1-ports/metal-gear-solid-recomp) | PSXRecomp native PC port of Metal Gear Solid (PS1) | 30 | 🟢 | Python |
| [Prince of Persia 2](https://github.com/Supermedo/prince-of-persia-2-windows) | Static recompilation of Prince of Persia 2 (DOS) into a native PC port | 30 | 🟢 | C |
| [Project Gotham Racing 4 (MTR-PGR4)](https://github.com/MissingThePixel/MTR-PGR4) | Static recompilation of Project Gotham Racing 4 (Xbox 360) into a native PC port | 30 | 🟢 | C# |
| [srw64-recomp](https://github.com/dyzz/srw64-recomp) | Experimental native recompilation of Super Robot Wars 64 with translations and HD mode | 30 | 🟢 | Python |
| [Starfox Recomp](https://github.com/mstan/StarFoxSNESRecomp) | Recomp + enhancement of Starfox (SNES). | 30 | 🟢 | C |
| [Strikers-Quest-MR](https://github.com/LanceSweatpants/Strikers-Quest-MR) | Super Mario Strikers (GameCube) built from its decompilation as a native Meta Quest 3 mixed-reality app | 30 | 🟢 | C++ |
| [stunts-hd](https://github.com/mr-finster/stunts-hd) | Stunts / 4D Sports Driving (DOS, 1990) recompiled for browser and desktop with HD 3D and widescreen | 30 | 🟢 | JavaScript |
| [Super Smash Bros. Melee](https://github.com/TechProGabe/Melee-X) | Unofficial native port of Super Smash Bros. Melee (GameCube) | 30 | 🟢 | C |
| [Twisted Metal 4 (TwistedMetal4 Recompiled)](https://github.com/TechnicallyComputers/TwistedMetal4Recomp) | Static recompilation of Twisted Metal 4 (PS1) into a native PC port | 30 | 🟢 | C |
| [WWE-SVR2009-RECOMP](https://github.com/nefariousjosiah/WWE-SVR2009-RECOMP) | Native PC port of WWE SmackDown vs. Raw 2009 (Xbox 360) via static recompilation | 30 | 🟢 | C++ |
| [DAORecomp](https://github.com/96dot/Dragon-Age-Origins-Recomp) | Static recompilation of Dragon Age: Origins (Xbox 360) to native PC | 29 | 🟢 | C |
| [mgb64](https://github.com/akratch/mgb64) | Decompilation-based native PC runtime for GoldenEye 007 | 29 | 🗄️ | C |
| [moonpearl](https://github.com/DoutorRaposo/moonpearl) | Android port of snesrev/zelda3 (ALttP reimplementation): widescreen, rewind, shaders, MSU-1, save states, controller... | 29 | 🟢 | Kotlin |
| [OpenJam](https://github.com/GTTeancum/OpenJam) | Native PC port of NBA JAM: On Fire Edition (Xbox 360) via static recompilation | 29 | 🟢 | Python |
| [Prototype (Prototype and Prototype 2 for Nintendo Switch)](https://github.com/fungalspores/prototype-switch) | Static recompilation of Prototype (Xbox 360) into a native PC port | 29 | 🟢 | C++ |
| [Scooby-Doo! Night of 100 Frights](https://github.com/josiahg2502-glitch/Scooby-Doo-Refrightened) | Static recompilation of Scooby-Doo! Night of 100 Frights (GameCube) into a native PC port | 29 | 🟢 | C++ |
| [Soulcalibur IV](https://github.com/FluffyQuack/rexglue-SoulCaliburIV) | Static recompilation of Soulcalibur IV (Xbox 360) into a native PC port | 29 | 🟢 | C |
| [StarCraft 64](https://github.com/n0madic/StarCraft64-recomp) | Static recompilation of StarCraft 64 (N64) into a native PC port | 29 | 🟢 | C++ |
| [wc2-re](https://github.com/neuromancer/wc2-re) | Open-source recomp of Wing Commander II. | 29 | 🟢 | C |
| [xmd-recompiled](https://github.com/florinp93/xmd-recompiled) | Native PC port of X-Men Destiny via static recompilation | 29 | 🟢 | C |
| [f15se2-ex](https://github.com/neuviemeporte/f15se2-ex) | Port of the reconstructed DOS game F-15 Strike Eagle II to modern platforms | 28 | 🟢 | C |
| [Gran Turismo 2 (gt2-multiplayer)](https://github.com/ianitsky/gt2-multiplayer) | Static recompilation of Gran Turismo 2 (PS1) into a native PC port | 28 | 🟢 | C# |
| [midtown-madness-3-PC-Native](https://github.com/lakshya16157/midtown-madness-3-PC-Native) | Midtown Madness 3 native Windows port via Xbox static recompilation with Direct3D 11 | 28 | 🟢 | Python |
| [Mother3Recomp](https://github.com/agray0425/Mother3Recomp) | Static recompilation of MOTHER 3 (GBA) to native PC on the gbarecomp framework | 28 | 🟢 | C++ |
| [nox-decomp](https://github.com/neuromancer/nox-decomp) | Unofficial Linux port of Nox (2000) from decompiled code | 28 | 🗄️ | C |
| [project-1944](https://github.com/zenit2893-cmyk/project-1944) | Unofficial native Windows PC port of Call of Duty 3 (Xbox 360) via static recompilation. Bring your own game. EN · RU... | 28 | 🟢 | Python |
| [socom-unzipped](https://github.com/Scotho/socom-unzipped) | SOCOM II: U.S. Navy SEALs, statically recompiled for PC with self-hosted online play | 28 | 🟢 | Python |
| [MCX360-EDITION](https://github.com/DevZer0D4Y/MCX360-EDITION) | ReXGlue recompilation of Minecraft Xbox 360 Edition running on iOS | 27 | 🟢 | C++ |
| [Metroid](https://github.com/mstan/MetroidNESRecomp) | Static recompilation of Metroid (NES) into a native PC port | 27 | 🟢 | C |
| [nfsmw-recomp](https://github.com/veritr1x/nfsmw-recomp) | Recompilation of Need for Speed: Most Wanted (the 2005 PC Black Edition) built on recomp-kit: macOS, iPad, Linux, Win... | 27 | 🟢 | C |
| [oot-dc](https://github.com/jnmartin84/oot-dc) | Port of the Ocarina of Time decompilation to the Sega Dreamcast | 27 | 🟢 | C |
| [Parasite Eve](https://github.com/alexbeavs-ps1-ports/parasite-eve-recomp) | Static recompilation of Parasite Eve (PS1) into a native PC port | 27 | 🟢 | Shell |
| [ReShadowTower](https://github.com/JFryy/reshadowtower) | Recompiled native port of Shadow Tower (PS1) with modern PC controls | 27 | 🟢 | Python |
| [Street-Fighter-EX2-Plus-Recompiled](https://github.com/strider973/Street-Fighter-EX2-Plus-Recompiled) | Static recompilation of Street Fighter EX2 Plus (PS1) | 27 | 🟢 | Python |
| [Super Mario 64 (SMUE5)](https://github.com/TheEnbyWitch/SMUE5) | Unofficial native port of Super Mario 64 (N64) | 27 | 🔴 | C++ |
| [Tiny Toon Adventures: Buster Busts Loose! (Buster Busts Loose! (PC port))](https://github.com/Darhkfox/BusterBustsLoose) | Unofficial native port of Tiny Toon Adventures: Buster Busts Loose! (SNES) | 27 | 🟢 | C |
| [Alien Resurrection](https://github.com/Heromachine/AlienResurrection-Recompilation) | Static recompilation of Alien Resurrection (PS1) into a native PC port | 26 | 🟢 | C# |
| [annepad](https://github.com/chrissotraidis/annepad) | Pokémon Stadium for iPhone and iPad via static recompilation, with native Metal rendering, touch controls, and ROM-fr... | 26 | 🟢 | Shell |
| [Castlevania](https://github.com/rumbleminze/castlevania-snes) | Unofficial native port of Castlevania (NES) | 26 | 🟢 | Assembly |
| [Digimon World 2 port](https://github.com/Wyrelade/DW2-PC) | PC port of Digimon World 2 (PS1) built from the matching decompilation | 26 | 🟢 | C++ |
| [master-chef](https://github.com/mitchaiet/master-chef) | Unofficial native Halo: Combat Evolved for Apple Vision Pro. Immersive panorama, controller support, and visual mods.... | 26 | 🟢 | C |
| [smt-nine-recomp](https://github.com/gymzatan/smt-nine-recomp) | Native Windows recompilation of Shin Megami Tensei NINE (Xbox) | 26 | 🟢 | C |
| [snowboardkids-recomp](https://github.com/cdlewis/snowboardkids-recomp) | Native PC port of Snowboard Kids (N64) for Windows, Linux and macOS | 26 | 🟢 | C |
| [soulcalibur_vita (Soulcalibur)](https://github.com/Rinnegatamante/soulcalibur_vita) | PS Vita port of Soulcalibur (mobile) via the Android version loader | 26 | 🟡 | C |
| [Super Mario Galaxy (PS5_MarioGalaxy)](https://github.com/griches/PS5_MarioGalaxy) | Static recompilation of Super Mario Galaxy (Wii) into a native PC port | 26 | 🟢 | C++ |
| [Super Mario Strikers (BallPad)](https://github.com/chrissotraidis/ballpad) | Unofficial native port of Super Mario Strikers (GameCube) | 26 | 🟢 | Objective-C++ |
| [TimeSplitters 2](https://github.com/phobos665/split2-recomp) | Static recompilation of TimeSplitters 2 (Xbox) into a native PC port | 26 | 🟢 | Python |
| [WCWnWoRevengeRecomp](https://github.com/jessetbh/WCWnWoRevengeRecomp) | WCW/nWo Revenge N64 static recompilation | 26 | 🟢 | Python |
| [Ace Combat 3](https://github.com/sal063/Ace-Combat-3-static-recompilation) | Static recompilation of Ace Combat 3 (PS1) into a native PC port | 25 | 🟢 | C |
| [arcade-js](https://github.com/qarl/arcade-js) | Arcade ROMs decompiled to idiomatic JavaScript with LLMs, validated against MAME | 25 | 🟢 | JavaScript |
| [arizona-vamp-recomp](https://github.com/Clergyman0013/arizona-vamp-recomp) | Native PC port of Darkwatch (Xbox) by static recompilation | 25 | 🟢 | C++ |
| [arwing](https://github.com/carl0srmz/arwing) | Star Fox recompilation and PC port with quality-of-life improvements | 25 | 🟢 | Assembly |
| [ds2-nx (Dead Space 2)](https://github.com/VasilkovND/ds2-nx) | Dead Space 2 (Xbox 360) running natively on Nintendo Switch | 25 | 🟢 | C++ |
| [jsrf-recomp](https://github.com/andeecollard/jsrf-recomp) | Static recompilation of Jet Set Radio Future (Xbox) to native macOS — playable into chapter 2 at 60 fps via a Direct3... | 25 | 🟢 | C |
| [Life Force](https://github.com/rumbleminze/lifeforce-snes) | Unofficial native port of Life Force (NES) | 25 | 🟡 | Assembly |
| [midnightclub](https://github.com/zarif98/midnightclub) | Static recompilation of Midnight Club: Los Angeles (Xbox 360) using rexGlu SDK | 25 | 🟢 | C++ |
| [miyoo64](https://github.com/mr-finster/miyoo64) | N64 games built for the Miyoo Mini handheld from community decompilation projects | 25 | 🟢 | C |
| [naruto-rise-of-a-ninja-port](https://github.com/Masterllgod/naruto-rise-of-a-ninja-port-nativo) | Naruto: Rise of a Ninja (Xbox 360) running natively on Android ARM64 via static recompilation | 25 | 🟢 |  |
| [SSBU (PS4)](https://github.com/iHaiDeeZ/SSBU) | Super Smash Bros. Ultimate WindowSmash recompilation ported to jailbroken PS4 | 25 | 🟢 | C++ |
| [The Legend of Zelda: The Minish Cap](https://github.com/mstan/MinishCapRecomp) | Static recompilation of The Legend of Zelda: The Minish Cap (GBA) into a native PC port | 25 | 🟢 | C++ |
| [Vagrant Story port](https://github.com/noprompt/rood-boi) | Native PC port of Vagrant Story built on the rood-reverse decompilation | 25 | 🟢 | C |
| [ar-recomp](https://github.com/DerrickGold/ar-recomp) | ActRaiser (SNES) recompilation project | 24 | 🟢 | C |
| [dk64-recomp-android (Donkey Kong 64)](https://github.com/deivid22srk/dk64-recomp-android) | Android port of Donkey Kong 64: Recompiled using RT64 and N64ModernRuntime | 24 | 🟢 | C |
| [Jet Force Gemini](https://github.com/VibinToast/JetForceGemini-Recomp) | Static recompilation of Jet Force Gemini (N64) into a native PC port | 24 | 🟢 | C++ |
| [keensource456tandy (Commander Keen in Goodbye, Galaxy!)](https://github.com/FrenkelS/keensource456tandy) | Unofficial native port of Commander Keen in Goodbye, Galaxy! (DOS) | 24 | 🟡 | C |
| [skifree_sdl](https://github.com/jeff-1amstudios/skifree_sdl) | SkiFree decompiled and ported to SDL2 | 24 | 🟡 | C |
| [Stuntman: Ignition (Stunt Double: Reignition)](https://github.com/giangra/stuntdouble-reignition) | Static recompilation of Stuntman: Ignition (Xbox 360) into a native PC port | 24 | 🟢 | C++ |
| [The Legend of Zelda: The Wind Waker HD (Wind Waker HD for PlayStation 5)](https://github.com/griches/PS5_WindWakerHD) | Static recompilation of The Legend of Zelda: The Wind Waker HD (Wii U) into a native PC port | 24 | 🟢 | C |
| [Vampire Savior: The Lord of Vampire](https://github.com/tmcleroy/vampire-savior-recomp) | Static recompilation of Vampire Savior: The Lord of Vampire (Arcade) into a native PC port | 24 | 🟢 | C++ |
| [White Knight Chronicles II (White Knight Chronicles II Recomp)](https://github.com/WK2D/White-Knight-Chronicles-2-Recomp) | Static recompilation of White Knight Chronicles II (PS3) into a native PC port | 24 | 🟢 | C++ |
| [WWE 2K14 (WWE2K14-PC)](https://github.com/itsbybanshee/wwe2k14-pc) | Static recompilation of WWE 2K14 (Xbox 360) into a native PC port | 24 | 🟢 | C# |
| [Ace Combat 3: Electrosphere](https://github.com/alexbeavs-ps1-ports/ace-combat-3-electrosphere-usa-recomp) | Static recompilation of Ace Combat 3: Electrosphere (PS1) into a native PC port | 23 | 🟢 | Python |
| [demoscene-recomp](https://github.com/treylorswift/demoscene-recomp) | Classic DOS demoscene productions recompiled to run natively in the browser | 23 | 🟢 | JavaScript |
| [Jiggle-or-Physics (Dead or Alive ++)](https://github.com/3dge7161/Jiggle-or-Physics) | Static recompilation of Dead or Alive ++ (Arcade) into a native port | 23 | 🟢 |  |
| [Metal Gear Solid: The Twin Snakes](https://github.com/alphanu1/msg-twinsnakes-recomp) | Static recompilation of Metal Gear Solid: The Twin Snakes (GameCube) into a native PC port | 23 | 🟢 | C |
| [Pokémon Ruby and Pokémon Sapphire](https://github.com/mstan/RubySapphireRecomp) | Static recompilation of Pokémon Ruby and Pokémon Sapphire (GBA) into a native PC port | 23 | 🟢 | Python |
| [psprecomp](https://github.com/sp00nznet/psprecomp) | Static recompilation toolkit for PSP games (Allegrex MIPS to C) | 23 | 🟢 | C |
| [Shin Megami Tensei IV (smt4-recomp)](https://github.com/Invictus-potens/smt4-recomp) | Static recompilation of Shin Megami Tensei IV (3DS) into a native PC port | 23 | 🟢 | Rust |
| [Sonic the Hedgehog 2](https://github.com/mstan/SonicTheHedgehog2Recomp) | Static recompilation of Sonic the Hedgehog 2 (Genesis) into a native PC port | 23 | 🟢 | C |
| [Space-Channel-5](https://github.com/ZoomiesZaggy/Space-Channel-5) | Unofficial native Space Channel 5 port for Windows, Linux and macOS. Compiler-free downloads, display options, contro... | 23 | 🟢 | C |
| [Super Mario Bros.](https://github.com/pwsqrd/lynx_smb) | Unofficial native port of Super Mario Bros. (NES) | 23 | 🟢 | Assembly |
| [tekken6-native-online-source](https://github.com/Ekspym/tekken6-native-online-source) | Launcher, rollback netplay runtime and build tools for the native PC port of Tekken 6 (Xbox 360) | 23 | 🟢 | C++ |
| [Tenchu: Stealth Assassins](https://github.com/Heromachine/Tenchu-SA-Recomp) | Static recompilation of Tenchu: Stealth Assassins (PS1) into a native PC port | 23 | 🟢 | C# |
| [twisted-metal-2012-ps3-native-port](https://github.com/franklincg/twisted-metal-2012-ps3-native-port) | Community native PC recompilation of Twisted Metal (2012, PS3) | 23 | 🟢 | C |
| [voldorium](https://github.com/enrique363/voldorium) | Native Windows port of SoulCalibur (Dreamcast) by static recompilation with rollback netcode | 23 | 🟢 | C |
| [Animal Crossing (Animal Crossing PC Port - Deluxe Edition)](https://github.com/imcynic/ACGC-Deluxe-PC-Port) | Unofficial native port of Animal Crossing (GameCube) | 22 | 🟢 | C |
| [AstroSmash (J2ME)](https://github.com/EXL/AstroSmash) | Port of the AstroSmash J2ME game to Android | 22 | 🔴 | Java |
| [Body Harvest Recompiled](https://github.com/danielgomesvieira2000/body-harvest-recomp) | Native PC port of Body Harvest (N64) built with N64Recomp and RT64 | 22 | 🟢 | C++ |
| [defjam_recomp](https://github.com/comoria08/defjam_recomp) | Static recompilation of Def Jam: Fight for NY (Xbox) for Windows | 22 | 🟢 | C |
| [mm3-recomp](https://github.com/MattSG/mm3-recomp) | Static recompilation of Midtown Madness 3 (Xbox) to native Windows x64 with a Direct3D 11 renderer | 22 | 🟢 | C |
| [Modern Combat 2: Black Pegasus ( BackStabRecomp)](https://github.com/jessicanataliagta/AndroidRecomp) | Static recompilation of Modern Combat 2: Black Pegasus (Mobile) into a native PC port | 22 | 🟢 | Python |
| [NBA Street V3](https://github.com/recomp-code/street-recomp-v3) | Static recompilation of NBA Street V3 (GameCube) into a native PC port | 22 | 🟢 | PowerShell |
| [ps1-recomp](https://github.com/PS1Recomp/ps1-recomp) | Tool that statically recompiles PS1 game binaries into native C++ executables | 22 | 🟢 | C++ |
| [pspoke](https://github.com/IbrahimIrfan/pspoke) | Pokemon Platinum and SoulSilver running natively on the PSP | 22 | 🟢 | C |
| [SacredStonesRecomp](https://github.com/Lordingard/SacredStonesRecomp) | Playable Windows and Android ARM64 recompilation of Fire Emblem: The Sacred Stones (GBA). | 22 | 🟢 | C++ |
| [Sonic 3 & Knuckles](https://github.com/mstan/Sonic3AndKnucklesRecomp) | Static recompilation of Sonic 3 & Knuckles (Genesis) into a native PC port | 22 | 🟢 | C |
| [Super Mario Advance 2: Super Mario World](https://github.com/mstan/SuperMarioAdvance2Recomp) | Static recompilation of Super Mario Advance 2: Super Mario World (GBA) into a native PC port | 22 | 🟢 | PowerShell |
| [The Legend of Zelda: Oracle of Ages / Oracle of Seasons](https://github.com/ZakyPew/epoch-equinox) | Static recompilation of The Legend of Zelda: Oracle of Ages / Oracle of Seasons (Game Boy Color) into a... | 22 | 🟢 | C |
| [Wario Land: Super Mario Land 3](https://github.com/GABRIELNNK/Bigodao) | Static recompilation of Wario Land: Super Mario Land 3 (Game Boy) into a native PC port | 22 | 🟢 | C |
| [WarioWare: Twisted!](https://github.com/mstan/WarioWareTwistedRecomp) | Static recompilation of WarioWare: Twisted! (GBA) into a native PC port | 22 | 🟢 | Python |
| [AkiLauncher](https://github.com/jessetbh/AkiLauncher) | Launcher for the AKI N64 wrestling static recompilations | 21 | 🟢 | C++ |
| [ArmyOfTwo-Recomp](https://github.com/Genesis5500/ArmyOfTwo-Recomp) | Experimental native PC port of Army of Two (Xbox 360) via ReXGlue static recompilation | 21 | 🟢 | C++ |
| [ff4a_vita (Final Fantasy IV: The After Years)](https://github.com/Rinnegatamante/ff4a_vita) | PS Vita port of Final Fantasy IV: The After Years via the Android version loader | 21 | 🔴 | C |
| [Forza Horizon](https://github.com/deivid22srk/pinyon-shift-android) | Static recompilation of Forza Horizon (Xbox 360) into a native PC port | 21 | 🟢 | C++ |
| [GoldenEye 007](https://github.com/cblock85/GoldenEye64Recomp) | Static recompilation of GoldenEye 007 (N64) into a native PC port | 21 | 🟢 | C++ |
| [Guitar Hero III: Legends of Rock](https://github.com/luisxl15/Guitar-Hero-3-Recomp-) | Static recompilation of Guitar Hero III: Legends of Rock (Xbox 360) into a native PC port | 21 | 🟢 | Java |
| [Hexagon-recomp](https://github.com/arvo-concept/Hexagon-recomp) | Static recompiler that turns PS3 PowerPC executables into native Android (AArch64) apps | 21 | 🟢 |  |
| [layton-vita (Professor Layton)](https://github.com/Rinnegatamante/layton-vita) | PS Vita port of Professor Layton and the Curious Village HD via the Android version loader | 21 | 🔴 | C |
| [Mega Man Zero](https://github.com/mstan/MegaManZeroRecomp) | Static recompilation of Mega Man Zero (GBA) into a native PC port | 21 | 🟢 | C++ |
| [Skate (2007)](https://github.com/cookingwithsimon/Skate1Recompiled) | Static recompilation of Skate (Xbox 360) into a native PC port | 21 | 🟢 | PowerShell |
| [Sonic the Hedgehog](https://github.com/mstan/SonicTheHedgehogRecomp) | Static recompilation of Sonic the Hedgehog (Genesis) into a native PC port | 21 | 🟢 | Python |
| [Test Drive Unlimited](https://github.com/testdriveupgrade/TDURE) | Xbox 360 static recompilation of Test Drive Unlimited | 21 | 🟢 | C++ |
| [Wii Party](https://github.com/arelkair/wiiparty-recomp) | Static recompilation of Wii Party (Wii) into a native PC port | 21 | 🟢 | C++ |
| [Zombies Ate My Neighbors (Zombies Ate My Neighbors PC Port)](https://github.com/moshferatu/zombies-ate-my-neighbors-pc-port) | Unofficial native port of Zombies Ate My Neighbors (SNES) | 21 | 🟢 | C |
| [Apocalypse-PC-Native-Port](https://github.com/MustafaSamer93/Apocalypse-PC-Native-Port) | Unofficial native port of Apocalypse (PS1) | 20 | 🟢 |  |
| [Armored Core](https://github.com/omegakatana92/Armored-Core-Recomp) | Static recompilation of Armored Core (PS1) into a native PC port | 20 | 🟢 | C |
| [Burnout 3](https://github.com/mxmstr/Burnout3Recomp) | Static recompilation of Burnout 3 (Xbox) into a native PC port | 20 | 🟢 | C++ |
| [Earthworm Jim 2 (Earthworm Jim 2 Recompiled)](https://github.com/elprogramadorloco-arch/jim2-recomp) | Static recompilation of Earthworm Jim 2 (PS1) into a native PC port | 20 | 🟢 | PowerShell |
| [Halo 3: Mythic](https://github.com/GTTeancum/OpenH3M) | Static recompilation of Halo 3: Mythic (Xbox 360) into a native PC port | 20 | 🟢 | C++ |
| [Mario Party 3](https://github.com/Rainchus/MarioParty3-Recomp) | Static recompilation of Mario Party 3 (N64) into a native PC port | 20 | 🟢 | C++ |
| [Mario's Tennis](https://github.com/mstan/MarioTennisVirtualBoyRecomp) | Static recompilation of Mario's Tennis (Virtual Boy) into a native PC port | 20 | 🟢 | C |
| [OpenEmperor](https://github.com/oliverjessner/OpenEmperor) | 🤴🏼 Clean-room reimplementation of Emperor: Rise of the Middle Kingdom in C++20 and SDL3. Built for modern systems, st... | 20 | 🟢 | C++ |
| [Project Arwing 2](https://github.com/carl0srmz/arwing2) | Native rebuild of Star Fox 2 (SNES) from a 65816 and SuperFX disassembly | 20 | 🟢 | Assembly |
| [starshippad (Star Fox 64)](https://github.com/chrissotraidis/starshippad) | Star Fox 64 (Starship) port for iPhone and iPad with Metal rendering | 20 | 🟢 | Shell |
| [Tomba! 2: The Evil Swine Return](https://github.com/mstan/Tomba2Recomp) | Static recompilation of Tomba! 2: The Evil Swine Return (PS1) into a native PC port | 20 | 🟢 | C++ |
| [weltendaemmerung](https://github.com/s-macke/weltendaemmerung) | Reverse engineering a C64 game with AI and porting it to the web | 20 | 🟢 | Assembly |
| [Black & White](https://github.com/sp00nznet/bw) | Static recompilation of Black & White (PC) into a native PC port | 19 | 🟢 | C++ |
| [Breath of Fire III (Breath of Fire III - PC Port)](https://github.com/kerokline/BreathOfFire3PCPort) | Unofficial native port of Breath of Fire III (PS1) | 19 | 🟢 | C++ |
| [Call of Duty: Future Warfare](https://github.com/goshavindtburg/NX1recomp) | Static recompilation of Call of Duty: Future Warfare (Xbox 360) into a native PC port | 19 | 🟢 | C |
| [drmario64_recomp (Dr. Mario 64)](https://github.com/AngheloAlf/drmario64_recomp) | Static recompilation of Dr. Mario 64 (N64) | 19 | 🗄️ | C++ |
| [FinFanTacRecomp](https://github.com/NJH-1001/FinFanTacRecomp) | PSXRecomp native Windows port of Final Fantasy Tactics (PS1) with 16:9 option | 19 | 🟢 | Python |
| [Flappy Bird (reFlappy)](https://github.com/THEN00P/reFlappy) | Static recompilation of Flappy Bird (Mobile) into a native PC port | 19 | 🟡 | Java |
| [LibertyRecomp](https://github.com/hamishakl/LibertyRecomp) | Unofficial PC port of the Xbox 360 version of GTA IV via static recompilation | 19 | 🟢 | C++ |
| [Mario Kart 64 (MK64Recomp)](https://github.com/arefdsg/MK64Recomp) | Static recompilation of Mario Kart 64 (N64) into a native PC port | 19 | 🟢 | C++ |
| [psp_jgr_portable](https://github.com/beckerd/psp_jgr_portable) | Native PSP port of Jet Grind Radio | 19 | 🟢 | C |
| [RogueSquadron64Recomp](https://github.com/MikeSemicolonD/RogueSquadron64Recomp) | A fully playable (AI assisted) static recompilation of Star Wars: Rogue Squadron on N64 for the PC, Linux & Android | 19 | 🟢 | C++ |
| [snesrecomp (sp00nznet)](https://github.com/sp00nznet/snesrecomp) | SNES hardware layer for static recompilation projects | 19 | 🟢 | C |
| [Sonic Advance decomp](https://github.com/ImmutableOctet/sonicgba) | Cross-platform port of Sonic Advance (GBA) | 19 | 🔴 | Monkey |
| [SpaceRanger](https://github.com/Capridog/SpaceRanger) | Native PC port of Toy Story 2: Buzz Lightyear to the Rescue (N64) via static recompilation | 19 | 🟢 | C++ |
| [testdrive-enhanced (Test Drive)](https://github.com/kylofon/testdrive-enhanced) | Enhanced native SDL3 port of Test Drive (1987, DOS) | 19 | 🟢 | C |
| [TTT2-Recomp (Tekken Tag Tournament 2)](https://github.com/thatcalikid760/TTT2-Recomp) | Static recompilation of Tekken Tag Tournament 2 | 19 | 🟢 | C++ |
| [xboxdashboard](https://github.com/sp00nznet/xboxdashboard) | The first-ever native PC port of the original Xbox Dashboard (build 3944) — static recompilation of xboxdash.xbe (x86... | 19 | 🟢 | C |
| [BadCompanyRecomp](https://github.com/crabinacrabic/BadCompanyRecomp) | ReXGlue static recompilation of Battlefield: Bad Company (Xbox 360) | 18 | 🟢 | C++ |
| [Bloodborne](https://github.com/bloodborne-native/bloodborne-recomp) | Static recompilation of Bloodborne (PS4) into a native PC port | 18 | 🟢 | C |
| [brawlerpad (Super Smash Bros.)](https://github.com/chrissotraidis/brawlerpad) | Super Smash Bros. (N64) port for macOS, iOS and iPadOS | 18 | 🟢 | Shell |
| [BullyRecomp](https://github.com/coole42-pixel/BullyRecomp) | Static recompilation of Bully: Scholarship Edition (Xbox 360) to native Windows x64 using ReXGlue | 18 | 🟢 | C++ |
| [Dead or Alive Extreme 2](https://github.com/Revan67/DOAX2-Recomp) | Static recompilation of Dead or Alive Extreme 2 (Xbox 360) into a native PC port | 18 | 🟢 | PowerShell |
| [Death-Road-to-Canada-Lite](https://github.com/Rinnegatamante/Death-Road-to-Canada-Lite) | PS Vita port of Death Road to Canada via the Android version loader | 18 | 🔴 | C |
| [Digimon World 2003](https://github.com/alexbeavs-ps1-ports/digimon-world-2003-recomp) | Static recompilation of Digimon World 2003 (PS1) into a native PC port | 18 | 🟢 | Python |
| [Dino Crisis](https://github.com/alexbeavs-ps1-ports/dino-crisis-recomp) | Static recompilation of Dino Crisis (PS1) into a native PC port | 18 | 🟢 | Python |
| [FFCCEOT-Recomp](https://github.com/JonathanDC64/FFCCEOT-Recomp) | Native PC port of Final Fantasy Crystal Chronicles: Echoes of Time (DS) by static recompilation. Bring your own ROM:... | 18 | 🟢 | C++ |
| [Final Fantasy XI](https://github.com/rubymatrix/xi-on-anything) | Static recompilation of Final Fantasy XI (PC) into a native PC port | 18 | 🟢 | C |
| [Glover-R](https://github.com/ThatGuyMcd/Glover-R) | Static recompilation of the N64 game Glover to native PC | 18 | 🟢 | Python |
| [GoldenEye 007 (GoldenEye-Recomp-Server (online play for GoldenEye recomp))](https://github.com/SunJaycy/GoldenEye-Recomp-Server) | Static recompilation of GoldenEye 007 (N64) into a native PC port | 18 | 🟢 | C++ |
| [gt4-native](https://github.com/gustavocanepa/gt4-native) | Native PC port of Gran Turismo 4 built on the decompilation (early planning) | 18 | 🟢 | C++ |
| [ido-static-recomp](https://github.com/Emill/ido-static-recomp) | Static recompilation of the SGI IDO compiler used to build N64 decompilations | 18 | 🔴 | C++ |
| [Legend of Legaia](https://github.com/SamSteProjects/legend-of-legaia-recomp) | Static recompilation of Legend of Legaia (PS1) into a native PC port | 18 | 🟢 | PowerShell |
| [Manic Miner (mrcook manic-miner (Manic Miner: Retro!))](https://github.com/mrcook/manic-miner) | Unofficial native port of Manic Miner (ZX Spectrum) | 18 | 🔴 | C++ |
| [Marble Blast Gold (OpenMBG)](https://github.com/The-New-Platinum-Team/OpenMBG) | Unofficial native port of Marble Blast Gold (PC) | 18 | 🟢 | C++ |
| [nfs-mw](https://github.com/47PADO47/nfs-mw) | 🦀 Rust rewrite of Need for Speed: Most Wanted (2005, PC v1.3 / Black Edition) with bevy engine | 18 | 🟢 | Rust |
| [ResidentEvilOutbreakRecompiled](https://github.com/RaccoonRecomp/ResidentEvilOutbreakRecompiled) | Static recompilation of Resident Evil Outbreak (PS2) into a native port | 18 | 🟢 |  |
| [SVR2011-Recomp](https://github.com/shaneomac1337/SVR2011-Recomp) | Unofficial Windows version of WWE SmackDown vs. Raw 2011 (Xbox 360), recompiled with ReXGlue. Bring your own disc image. | 18 | 🟢 | C++ |
| [The Simpsons Game (the-simpsons-game-nx)](https://github.com/R-drg/the-simpsons-game-nx) | Static recompilation of The Simpsons Game (Xbox 360) into a native PC port | 18 | 🟢 | C++ |
| [WWFWrestleMania2000Recomp](https://github.com/jessetbh/WWFWrestleMania2000Recomp) | WWF WrestleMania 2000 N64 static recompilation | 18 | 🟢 | Python |
| [bearbirdpad (Banjo-Kazooie)](https://github.com/chrissotraidis/bearbirdpad) | Banjo-Kazooie on iPhone and iPad via BanjoRecomp with Metal rendering | 17 | 🟢 | Objective-C++ |
| [Bloody Roar Extreme (Bloody Roar Extreme - XBE Recomp)](https://github.com/bromurok/BloodyRoarExtremeRecomp) | Static recompilation of Bloody Roar Extreme (Xbox) into a native PC port | 17 | 🟢 | C++ |
| [Breath of Fire III](https://github.com/kerokline/BreathOfFire3Recomp) | Static recompilation of Breath of Fire III (PS1) into a native PC port | 17 | 🟢 | Python |
| [Burnout CRASH!](https://github.com/kiesxoxo/burnout-crash-recomp) | Static recompilation of Burnout CRASH! (Xbox 360) into a native PC port | 17 | 🟢 | C++ |
| [Crash Bandicoot 3: Warped](https://github.com/alexbeavs-ps1-ports/crash-bandicoot-3-warped-recomp) | Static recompilation of Crash Bandicoot 3: Warped (PS1) into a native PC port | 17 | 🟢 | Python |
| [Dino Crisis 2](https://github.com/alexbeavs-ps1-ports/dino-crisis-2-recomp) | Static recompilation of Dino Crisis 2 (PS1) into a native PC port | 17 | 🟢 | Python |
| [Dragon Ball Z: Super Saiya Densetsu](https://github.com/JackRushante/DBZ-Super-Saiya-Densetsu-Rust) | Static recompilation of Dragon Ball Z: Super Saiya Densetsu (SNES) into a native PC port | 17 | 🟢 | Rust |
| [Dragon Ball Z: The Legacy of Goku II](https://github.com/mstan/DragonBallZLegacyofGokuIIRecomp) | Static recompilation of Dragon Ball Z: The Legacy of Goku II (GBA) into a native PC port | 17 | 🟢 | C++ |
| [flOw](https://github.com/sp00nznet/flow) | Static recompilation of flOw (PS3) into a native PC port | 17 | 🟢 | C++ |
| [Forza Horizon 2](https://github.com/fabioap-cpu/Forza-Horizon-2-Recomp) | Static recompilation of Forza Horizon 2 (Xbox 360) into a native PC port | 17 | 🟢 | C |
| [gd-melee-workspace](https://github.com/GurekamDhillon/gd-melee-workspace) | Native PC port of Super Smash Bros. Melee with rollback netplay and mod support | 17 | 🟢 | Python |
| [infamous2-pc](https://github.com/ThiagoFraga761/infamous2-pc) | Static recompilation of inFAMOUS 2 (PS3) for Linux with a Vulkan renderer | 17 | 🟢 | C |
| [MidnightclubLA-Recomp](https://github.com/BeemerCodes/MidnightclubLA-Recomp) | Unofficial native PC port of Midnight Club: Los Angeles (Xbox 360) via static recompilation | 17 | 🟢 | C# |
| [Mystical Ninja Starring Goemon](https://github.com/ogdanimal/Goemon64Recomp-Android) | Static recompilation of Mystical Ninja Starring Goemon (N64) into a native PC port | 17 | 🟢 | C |
| [Project-Iron-6](https://github.com/GenryTheFox0/Project-Iron-6) | Unofficial Tekken 6 Xbox 360 to Windows static recompilation | 17 | 🟢 |  |
| [prototype-pc (PS4)](https://github.com/petrishevgeorgii-debug/prototype-pc-slop) | Experimental native PC port of PROTOTYPE and PROTOTYPE 2 from the PS4 bundle | 17 | 🟢 | C++ |
| [rawpsx (Another World)](https://github.com/fgsfdsfgs/rawpsx) | Port of the rawgl Another World engine to the PlayStation | 17 | 🔴 | C |
| [Road Trip](https://github.com/silentsudin/RoadTripAdventure-recomp) | Static recompilation of Road Trip (PS2) into a native PC port | 17 | 🟢 | C++ |
| [Saints Row](https://github.com/sp00nznet/saintsrow) | Static recompilation of Saints Row (Xbox 360) into a native PC port | 17 | 🟢 | C++ |
| [scooby-doo-mystery port](https://github.com/janezkranjc/scooby-doo-mistery-mouse-version) | Native SFML port of Sega Genesis Scooby-Doo Mystery from reverse-engineered 68000 code | 17 | 🟢 | C++ |
| [Sonic Advance](https://github.com/smiluredev/SonicAdvanceRecomp) | Static recompilation of Sonic Advance (GBA) into a native PC port | 17 | 🟢 | C |
| [StarCraft: Ghost](https://github.com/aknavj/scghost-recomp) | Static recompilation of StarCraft: Ghost (Xbox) into a native PC port | 17 | 🟢 | C |
| [Super Dodge Ball (super-super-dodgeball)](https://github.com/rumbleminze/super-super-dodgeball) | Unofficial native port of Super Dodge Ball (NES) | 17 | 🟡 | Assembly |
| [Super Mario Advance 4: Super Mario Bros. 3](https://github.com/mstan/SuperMarioAdvance4Recomp) | Static recompilation of Super Mario Advance 4: Super Mario Bros. 3 (GBA) into a native PC port | 17 | 🟢 | PowerShell |
| [Test Drive](https://github.com/kylofon/test-drive-sdl3) | Open-source recomp of Test Drive (1987). | 17 | 🟢 | C |
| [The Legend of Zelda: A Link to the Past](https://github.com/YeOldPress/alttp-dx) | Unofficial native port of The Legend of Zelda: A Link to the Past (SNES) | 17 | 🟢 | Zig |
| [The Legend of Zelda: The Wind Waker](https://github.com/sp00nznet/ww) | Static recompilation of The Legend of Zelda: The Wind Waker (GameCube) into a native PC port | 17 | 🟢 | C++ |
| [The Legend of Zelda: Twilight Princess (tp-port (mbayonal))](https://github.com/mbayonal/tp-port) | Unofficial native port of The Legend of Zelda: Twilight Princess (GameCube) | 17 | 🟢 | C++ |
| [Thrill Drive 2 (konami-viper-recomp)](https://github.com/spita90/konami-viper-recomp) | Static recompilation of Thrill Drive 2 (Arcade) into a native PC port | 17 | 🟢 | C++ |
| [War of the Monsters](https://github.com/yanm1103/War_of_the_Monsters_recomp) | Static recompilation of War of the Monsters (PS2) into a native PC port | 17 | 🟢 | C++ |
| [X-Men Mutant Academy 2](https://github.com/GTTeancum/xmen-mutant-academy-2-pc) | Recomp of the PS1 game X-Men Mutant Academy 2. | 17 | 🟢 | Python |
| [Yoshi's Island: Super Mario Advance 3 (SMA3 Recomp Android – Yoshi's Island: Super Mario Advance 3 PC port)](https://github.com/Edwin2929/sma3-recomp-android.) | Static recompilation of Yoshi's Island: Super Mario Advance 3 (GBA) into a native PC port | 17 | 🟢 | C++ |
| [Banjo-Tooie: Recompiled](https://github.com/Vidanox/BanjoTooieRecompiled) | Banjo-Tooie static recompilation for Windows/Linux | 16 | 🟢 | C |
| [BattleTanx: Global Assault (Native PC Port)](https://github.com/TheGh0stShip/BattleTanx-Global-Assault-PC-Port) | Unofficial native port of BattleTanx: Global Assault (N64) | 16 | 🟢 | C |
| [Crash Team Racing](https://github.com/NyperYuhgard/CTR-PC-Port) | Unofficial native port of Crash Team Racing (PS1) | 16 | 🟢 | C |
| [Crash Twinsanity](https://github.com/menaman123/NativeEE) | Static recompilation of Crash Twinsanity (PS2) into a native PC port | 16 | 🟢 | C++ |
| [CV64Recomp](https://github.com/RevoSucks/CV64Recomp) | A recompilation of Castlevania for the N64. | 16 | 🟢 | C |
| [dantes-inferno-nx](https://github.com/VasilkovND/dantes-inferno-nx) | Dante's Inferno (Xbox 360) running natively on Nintendo Switch | 16 | 🟢 | C++ |
| [Die Hard Trilogy](https://github.com/alexbeavs-ps1-ports/die-hard-trilogy-recomp) | Static recompilation of Die Hard Trilogy (PS1) into a native PC port | 16 | 🟢 | Python |
| [Digimon World 3 (D-W-3-Recomp)](https://github.com/Xive080/D-W-3-Recomp) | Static recompilation of Digimon World 3 (PS1) into a native PC port | 16 | 🟢 |  |
| [doa2u-recomp](https://github.com/parkerallan/doa2u-recomp) | PC port of Dead or Alive 2 Ultimate (Xbox), in progress | 16 | 🟢 | Assembly |
| [doa3-re](https://github.com/NoRain211/doa3-re) | Native Windows port of Dead or Alive 3 (Xbox) via static recompilation with a hand-written runtime | 16 | 🟢 | C |
| [Genma Onimusha (Genma Onimusha - PC port)](https://github.com/rafaelkenedy/genma-recomp) | Static recompilation of Genma Onimusha (Xbox) into a native PC port | 16 | 🟢 | C++ |
| [godhand-recomp](https://github.com/LasVola/godhand-recomp) | Native PC port of God Hand (PS2) via static recompilation | 16 | 🟢 | C++ |
| [Into-The-Breach-Vita](https://github.com/Rinnegatamante/Into-The-Breach-Vita) | PS Vita port of Into the Breach | 16 | 🟡 | C |
| [KillzoneLiberation-Recomp](https://github.com/Tzeentchnet/KillzoneLiberation-Recomp) | Static recompilation of Killzone: Liberation (PSP) for Windows/Direct3D 12 | 16 | 🟢 | Python |
| [Mario Party 6 port](https://github.com/iirg4x/mp6-native-port) | Native Windows and Android port of Mario Party 6 built on the GameCube decompilation | 16 | 🟢 | Python |
| [Medal-Of-Honor-PSX-Recomp](https://github.com/FractalEngineer/Medal-Of-Honor-PSX-Recomp) | Static recompilation of Medal of Honor (PS1) | 16 | 🟢 | C |
| [nes-to-snes-template](https://github.com/rumbleminze/nes-to-snes-template) | Template for porting NES games to the SNES | 16 | 🟢 | Assembly |
| [opencmr2-vr (Colin McRae Rally 2.0)](https://github.com/DR-89/opencmr2-vr) | Experimental native Colin McRae Rally 2.0 VR port for Meta Quest 3 and PCVR | 16 | 🟢 | C++ |
| [Parasite Eve port](https://github.com/khasinski/parasite-eve-pc) | Native PC port of Parasite Eve (PS1) built on the matching decompilation | 16 | 🟢 | C |
| [Prehistorik 2 (missingno7 pre2_port (dos_re))](https://github.com/missingno7/pre2_port) | Unofficial native port of Prehistorik 2 (DOS) | 16 | 🟢 | Python |
| [Sega Superstars Tennis](https://github.com/m1ndcrap/Sega-Superstars-Tennis-ReMatch) | Static recompilation of Sega Superstars Tennis (Xbox 360) into a native PC port | 16 | 🟢 | C++ |
| [Shadow of the Colossus](https://github.com/sp00nznet/shadowofthecolossus) | Static recompilation of Shadow of the Colossus (PS3) into a native PC port | 16 | 🟢 | CMake |
| [Sonic '06 Demo](https://github.com/PranchaD/re-Sonic06Demo) | Xbox 360 static recompilation of Sonic '06 Demo | 16 | 🟢 | CMake |
| [SonicCD-WindowsPhone-Decompilation](https://github.com/tge-was-taken/SonicCD-WindowsPhone-Decompilation) | Decompilation and PC port of the Windows Phone version of Sonic CD | 16 | 🗄️ | C# |
| [starwing-3ds (Star Fox)](https://github.com/EstebanPdN/starwing-3ds) | Nintendo 3DS dual-screen port of Star Fox / Starwing (SNES) | 16 | 🟢 | C++ |
| [Super Mario Odyssey (smo-recomp)](https://github.com/Coz-0/smo-recomp) | Static recompilation of Super Mario Odyssey (Switch) into a native PC port | 16 | 🟢 | C |
| [testdrive2-enhanced (Test Drive II)](https://github.com/kylofon/testdrive2-enhanced) | Enhanced native SDL3 port of Test Drive II: The Duel (1989, DOS) | 16 | 🟢 | C |
| [The Urbz: Sims in the City](https://github.com/abilliontokens/urbz-recomp) | Static recompilation of The Urbz: Sims in the City (Xbox) into a native PC port | 16 | 🟢 | C++ |
| [Viva Piñata](https://github.com/crabinacrabic/VivaPinataRecomp) | Static recompilation of Viva Piñata (Xbox 360) into a native PC port | 16 | 🟢 | C++ |
| [Warthog](https://github.com/ChupathingyCE/warthog-xbox) | Halo: Combat Evolved decompilation rebuilt for the original Xbox, playing online with PC builds | 16 | 🟢 | C |
| [WWE-SVR2007-RECOMP](https://github.com/nefariousjosiah/WWE-SVR2007-RECOMP) | Static recompilation of WWE SmackDown vs. Raw 2007 (Xbox 360) for Windows | 16 | 🟢 | C++ |
| [Alisa-Vita](https://github.com/Rinnegatamante/Alisa-Vita) | PS Vita port of Alisa: Developer's Cut | 15 | 🟢 |  |
| [Battle Arena Toshinden (Battle Arena Toshinden Recompiled)](https://github.com/mstan/BattleArenaToshindenRecomp) | Static recompilation of Battle Arena Toshinden (PS1) into a native PC port | 15 | 🟢 | C |
| [BlackKnightRecomp](https://github.com/yunophilia/BlackKnightRecomp) | Static recompilation of Sonic and the Black Knight (Wii) for Windows | 15 | 🟢 | C++ |
| [Conan](https://github.com/crazyriddler/Conan2007Recomp) | Static recompilation of Conan (Xbox 360) into a native PC port | 15 | 🟢 | HLSL |
| [Dance Dance Revolution 1st Mix](https://github.com/bmbelo87/ddr-1st-recomp) | Static recompilation of Dance Dance Revolution 1st Mix (PS1) into a native PC port | 15 | 🟢 | C |
| [hazard-vita (Beat Hazard 2)](https://github.com/Rinnegatamante/hazard-vita) | PS Vita port of Beat Hazard 2 | 15 | 🟢 | C |
| [Midnight Club: Los Angeles](https://github.com/luisxl15/Midnight-Club-L.A-RECOMP) | Static recompilation of Midnight Club: Los Angeles (Xbox 360) into a native PC port | 15 | 🟢 | C |
| [re-stunts](https://github.com/CommonLoon102/restunts-bb11) | Recomp of the game Stunts. Original and enhanced versions. | 15 | 🟢 | C |
| [Scooby-Doo! Unmasked](https://github.com/josiahg2502-glitch/Scooby-Doo-ReMasked) | Static recompilation of Scooby-Doo! Unmasked (GameCube) into a native PC port | 15 | 🟢 | C++ |
| [Skate3-Port](https://github.com/darchap/Skate3-Port) | Skate 3 running natively on ARM64 without emulation | 15 | 🟢 | C++ |
| [sm64-gba](https://github.com/Kodoque1/sm64-gba) | Super Mario 64 movement and collision code on the GBA, bit-exact with the original | 15 | 🟢 | C |
| [smb2se-vita (Super Monkey Ball 2)](https://github.com/Rinnegatamante/smb2se-vita) | PS Vita port of Super Monkey Ball 2: Sakura Edition via the Android version loader | 15 | 🟢 | C |
| [Sonic Adventure 2: Battle (sa2-nx)](https://github.com/ChanseyIsTheBest/sa2-nx) | Static recompilation of Sonic Adventure 2: Battle (GameCube) into a native PC port | 15 | 🟢 | C++ |
| [Sonic CD (SonicCD-DC)](https://github.com/DCRSDK/SonicCD-DC) | Unofficial native port of Sonic CD (PC) | 15 | 🟢 | C++ |
| [Sonic Generations (Sonic-Generations-recomp-android-and-pc-edition)](https://github.com/Player124413/Sonic-Generations-recomp-android-and-pc-edition) | Static recompilation of Sonic Generations (Xbox 360) into a native PC port | 15 | 🟢 | C++ |
| [Super Mario Bros.](https://github.com/nathsou/smb) | Static recompilation of Super Mario Bros. (NES) into a native PC port | 15 | 🟢 | MoonBit |
| [Super Mario Land 2: 6 Golden Coins (SuperMarioLand2Recomp)](https://github.com/mstan/SuperMarioLand2Recomp) | Static recompilation of Super Mario Land 2: 6 Golden Coins (Game Boy) into a native PC port | 15 | 🟢 | Python |
| [Super Smash Bros.](https://github.com/beigeceleron/ssb64-dc) | Unofficial native port of Super Smash Bros. (N64) | 15 | 🟢 | C |
| [Turok: Rage Wars (rage-wars-recompiled)](https://github.com/ArtfulRascal8/rage-wars-recompiled) | Static recompilation of Turok: Rage Wars (N64) into a native PC port | 15 | 🟢 | C++ |
| [UT99-Vita (Unreal Tournament)](https://github.com/Rinnegatamante/UT99-Vita) | Launcher for the Android port of Unreal Tournament 99 on PS Vita | 15 | 🟢 | C++ |
| [Ace Combat 6: Fires of Liberation](https://github.com/rapidsamphire/AC6Recomp) | Static recompilation of Ace Combat 6: Fires of Liberation (Xbox 360) into a native PC port | 14 | 🟢 | C++ |
| [Breakdown](https://github.com/Heromachine/Breakdown-Recompilation) | Static recompilation of Breakdown (Xbox) into a native PC port | 14 | 🟢 | C |
| [callofrecomp](https://github.com/Dr3amyBerry/callofrecomp) | Static recompilation of Call of Duty 1.5 (PC) for Android | 14 | 🟢 | Python |
| [DoomSNESRecomp](https://github.com/Cacodemontube/DoomSNESRecomp) | This is a PC Recomp of the SNES Version of Doom using SNESrecomp. | 14 | 🟢 | C |
| [Dr. Mario](https://github.com/mstan/DrMarioNesRecomp) | Static recompilation of Dr. Mario (NES) into a native PC port | 14 | 🟢 | C |
| [Duck Hunt](https://github.com/mstan/DuckHuntNESRecomp) | Static recompilation of Duck Hunt (NES) into a native PC port | 14 | 🟢 | C |
| [Exit / Exit 2](https://github.com/FluffyQuack/ReXGlue-EXIT) | Static recompilation of Exit / Exit 2 (Xbox 360) into a native PC port | 14 | 🟢 | C |
| [Faxanadu](https://github.com/mstan/FaxanaduRecomp) | Static recompilation of Faxanadu (NES) into a native PC port | 14 | 🟢 | C |
| [fear-nx](https://github.com/infriker/fear-nx) | F.E.A.R. (Xbox 360) running natively on Switch with ReXGlue and Vulkan | 14 | 🟢 | C++ |
| [Final Fantasy VIII](https://github.com/alexbeavs-ps1-ports/final-fantasy-viii-recomp) | Static recompilation of Final Fantasy VIII (PS1) into a native PC port | 14 | 🟢 | Python |
| [Guitar Hero II (reGH2)](https://github.com/jillsandwich1998/reGH2) | Static recompilation of Guitar Hero II (PS2) into a native PC port | 14 | 🟢 | C++ |
| [Import Tuner Challenge](https://github.com/Spooky098529/ITC-Recomp) | Static recompilation of Import Tuner Challenge (Xbox 360) into a native PC port | 14 | 🟢 | C++ |
| [Kirby's Dream Land](https://github.com/omegakatana92/Kirby-Dream-Land-Recomp) | Static recompilation of Kirby's Dream Land (Game Boy) into a native PC port | 14 | 🟢 | C |
| [Mabecs International Superstar Soccer 2000](https://github.com/Mabec-games/iss2000-recomp) | Static recompilation of Mabecs International Superstar Soccer 2000 (N64) into a native PC port | 14 | 🟢 | C++ |
| [MCLA-4iOS](https://github.com/KoreanSeats1/MCLA-4iOS) | Midnight Club: Los Angeles on iPhone and iPad — ARM64 static recompilation, native Metal, and an experimental 60 FPS... | 14 | 🟢 | Objective-C++ |
| [Metal Gear Solid (mgsone-recomp)](https://github.com/coccofresco/mgsone-recomp) | Static recompilation of Metal Gear Solid (PS1) into a native PC port | 14 | 🟢 | C++ |
| [muscle-march-recomp](https://github.com/tmcleroy/muscle-march-recomp) | Unofficial native PC port of Muscle March (WiiWare) via static recompilation: macOS, Linux, Steam Deck, Windows. Requ... | 14 | 🟢 | C++ |
| [neogeorecomp](https://github.com/sp00nznet/neogeorecomp) | Static recompilation runtime for SNK Neo Geo MVS/AES games | 14 | 🟢 | C |
| [Nightmare Creatures II](https://github.com/alexbeavs-ps1-ports/nightmare-creatures-ii-recomp) | Static recompilation of Nightmare Creatures II (PS1) into a native PC port | 14 | 🟢 | Python |
| [Pac-Man](https://github.com/Mr-Shizzy/PacManRecomp) | Static recompilation of Pac-Man (NES) into a native PC port | 14 | 🟢 | C |
| [Pokémon Mystery Dungeon: Red Rescue Team](https://github.com/Asphaltian/pmd-green) | Static recompilation of Pokémon Mystery Dungeon: Red Rescue Team (GBA) into a native PC port | 14 | 🟢 | C# |
| [Quest 64 (Quest 64 Tale: Recompiled)](https://github.com/boricuapab/quest64tale-recompiled) | Static recompilation of Quest 64 (N64) into a native PC port | 14 | 🟢 | C++ |
| [Ratchet-and-Clank-Recomp](https://github.com/MarcPique/Ratchet-and-Clank-Recomp) | Native PC port of Ratchet & Clank (PS2) based on ReRAC, with an ISO installer | 14 | 🟢 | Rust |
| [rct-vita (RollerCoaster Tycoon Classic)](https://github.com/Rinnegatamante/rct-vita) | PS Vita port of RollerCoaster Tycoon Classic via the Android version loader | 14 | 🟡 | C |
| [Scooby-Doo! Mystery Mayhem](https://github.com/Campfirecrucifix/scooby-doo-mystery-mayhem-pc) | Unofficial native port of Scooby-Doo! Mystery Mayhem (PS2) | 14 | 🟢 | Rust |
| [SEGA Rally Championship 96](https://github.com/xandoxan65/segarally95-recomp) | Static recompilation of SEGA Rally Championship 96 (Arcade) into a native PC port | 14 | 🟢 | C |
| [Sonic4Ep1-WindowsPhone-Decompilation](https://github.com/tge-was-taken/Sonic4Ep1-WindowsPhone-Decompilation) | Decompilation and PC port of Sonic 4 Episode 1 for Windows Phone 7 | 14 | 🔴 | C# |
| [ssx-tricky-recomp](https://github.com/reindance/ssx-tricky-recomp) | Linux-first native recompilation of SSX Tricky for the original Xbox | 14 | 🟢 | C |
| [Streets of Rage](https://github.com/RuiNelson/StreetsOfRageProject) | Static recompilation of Streets of Rage (Genesis) into a native PC port | 14 | 🟢 | Python |
| [Super Mario 64 DS](https://github.com/mstan/supermario64dsrecomp) | Static recompilation of Super Mario 64 DS (DS) into a native PC port | 14 | 🟢 | Python |
| [Test Drive III](https://github.com/kylofon/test-drive-3-sdl3) | Recomp of Test Drive III: The Passion. | 14 | 🟢 | C |
| [Tetris (Kirpich)](https://github.com/etroimcasso/Kirpich) | Unofficial native port of Tetris (Game Boy) | 14 | 🟢 | C++ |
| [Twisted Metal](https://github.com/sp00nznet/twistedmetal) | Static recompilation of Twisted Metal (PS3) into a native PC port | 14 | 🟢 | C++ |
| [wwe2k16-pc](https://github.com/itsbybanshee/wwe2k16-pc) | Static recompilation of WWE 2K16 for PC | 14 | 🟢 | C# |
| [Animal Forest (animal_forest_psp)](https://github.com/bruder-grimm/animal_forest_psp) | Unofficial native port of Animal Forest (N64) | 13 | 🟢 | C |
| [Blinx 2: Masters of Time and Space](https://github.com/apexJCL/blinx2-recomp) | Static recompilation of Blinx 2: Masters of Time and Space (Xbox) into a native PC port | 13 | 🟢 | C |
| [Bomberman Fantasy Race (Bomberman Fantasy Race Recompiled)](https://github.com/TechnicallyComputers/Bomberman-Fantasy-Race-Recomp) | Static recompilation of Bomberman Fantasy Race (PS1) into a native PC port | 13 | 🟢 | C |
| [Dead Space 2](https://github.com/bifftannen1/Dead-Space-2-Recomp) | Static recompilation of Dead Space 2 (Xbox 360) into a native PC port | 13 | 🟢 | C++ |
| [Defender (Falcon)](https://github.com/therealsark02/defender) | Unofficial native port of Defender (Arcade) | 13 | 🟡 | C |
| [Double Dragon (double-dragon-snes)](https://github.com/rumbleminze/double-dragon-snes) | Unofficial native port of Double Dragon (Arcade) | 13 | 🟢 | Assembly |
| [Final Fantasy IX](https://github.com/alexbeavs-ps1-ports/final-fantasy-ix-recomp) | Static recompilation of Final Fantasy IX (PS1) into a native PC port | 13 | 🟢 | Python |
| [God of War: Chains of Olympus](https://github.com/Simeony2007/VibeRecomp-for-GoW-CoO) | Static recompilation of God of War: Chains of Olympus (PSP) into a native PC port | 13 | 🟢 | C |
| [GoldenEye 007 (XBLA remaster) (GoldenEye-Recomp-rexglue)](https://github.com/SunJaycy/GoldenEye-Recomp-rexglue) | Static recompilation of GoldenEye 007 (XBLA remaster) (Xbox 360) into a native PC port | 13 | 🟢 | C |
| [GoldenEye007ReloadedRecomp](https://github.com/nikolaygorb/GoldenEye007ReloadedRecomp) | RexGlue static recompilation of GoldenEye 007: Reloaded (Xbox 360) | 13 | 🟢 | C++ |
| [Grand Theft Auto / GTA: London](https://github.com/sp00nznet/gta) | Static recompilation of Grand Theft Auto / GTA: London (PC) into a native PC port | 13 | 🟢 | C |
| [Hybrid Heaven](https://github.com/danielgomesvieira2000/hybrid-heaven-recomp) | Static recompilation of Hybrid Heaven (N64) into a native PC port | 13 | 🟢 | C++ |
| [Hybrid Heaven](https://github.com/ogdanimal/HybridHeaven-Recomp) | Static recompilation of Hybrid Heaven (N64) into a native PC port | 13 | 🟢 | C++ |
| [kotor-recomp](https://github.com/sp00nznet/kotor-recomp) | Static recompilation of Star Wars: Knights of the Old Republic (PC) to native C | 13 | 🟢 | C |
| [MediEvil](https://github.com/alexbeavs-ps1-ports/medievil-recomp) | Static recompilation of MediEvil (PS1) into a native PC port | 13 | 🟢 | Python |
| [MediEvil II](https://github.com/alexbeavs-ps1-ports/medievil-ii-recomp) | Static recompilation of MediEvil II (PS1) into a native PC port | 13 | 🟢 | C++ |
| [Mega Man X3](https://github.com/mstan/MegamanX3SNESRecomp) | Static recompilation of Mega Man X3 (SNES) into a native PC port | 13 | 🟢 | C |
| [NFS3-HP-AndroidEvolved](https://github.com/codepdbh/NFS3-HP-AndroidEvolved) | Android ARM64 port of Need for Speed III: Hot Pursuit based on nfs-recompiled | 13 | 🟢 | C++ |
| [Resident Evil 3: Nemesis](https://github.com/alexbeavs-ps1-ports/resident-evil-3-recomp) | Static recompilation of Resident Evil 3: Nemesis (PS1) into a native PC port | 13 | 🟢 | Python |
| [Shadow of the Colossus](https://github.com/InconspicuousCactus/SotCStaticRecompilation) | Static recompilation of Shadow of the Colossus (PS2) into a native PC port | 13 | 🟡 | C |
| [so_util](https://github.com/Rinnegatamante/so_util) | Android ELF (.so) loader for running Android games on the PS Vita | 13 | 🟢 | C |
| [Spider-Man-3-Recomp](https://github.com/b4ttycre4se/Spider-Man-3-Recomp) | ReXGlue recompilation of Spider-Man 3 (Xbox 360) for Windows x64 | 13 | 🟢 | CMake |
| [Super Mario 64 (libsm64-sharp)](https://github.com/MeltyPlayer/libsm64-sharp) | Unofficial native port of Super Mario 64 (N64) | 13 | 🟡 | C# |
| [Super Metroid (sm-3ds)](https://github.com/CharlesAverill/sm-3ds) | Unofficial native port of Super Metroid (SNES) | 13 | 🟢 | Makefile |
| [tlou_pc (The Last of Us)](https://github.com/HayatoG/tlou_pc) | Native PC port of The Last of Us (PS4) | 13 | 🟢 | C++ |
| [Vigilante 8 Arcade](https://github.com/sp00nznet/vig8) | Static recompilation of Vigilante 8 Arcade (Xbox 360) into a native PC port | 13 | 🟢 | C++ |
| [X-Men Legends](https://github.com/GTTeancum/XML1-recomp) | Static recompilation of X-Men Legends (Xbox) into a native PC port | 13 | 🟢 | C |
| [AndroLayer](https://github.com/Rinnegatamante/AndroLayer) | HLE compatibility layer for porting Android games to PC | 12 | 🟢 | C |
| [Backstab HD (BackStabRecomp (AndroidRecomp))](https://github.com/jessicanataliagta/BackStabRecomp) | Static recompilation of Backstab HD (Mobile) into a native PC port | 12 | 🟢 | C++ |
| [Balloon Fight (Balloon-fight-VS-for-NES)](https://github.com/tvoybro/Balloon-fight-VS-for-NES) | Unofficial native port of Balloon Fight (NES) | 12 | 🔴 | Assembly |
| [bananapad (Donkey Kong 64)](https://github.com/chrissotraidis/bananapad) | Donkey Kong 64 recompilation running natively on iOS and iPadOS | 12 | 🟢 | Shell |
| [BattleTanx: Global Assault (BTGARecomp)](https://github.com/wootbeer/btgarecomp) | Static recompilation of BattleTanx: Global Assault (N64) into a native PC port | 12 | 🟢 | C++ |
| [Blue Dragon (reblue)](https://github.com/WeiGustavo/reblue) | Static recompilation of Blue Dragon (Xbox 360) into a native PC port | 12 | 🟢 | C++ |
| [BOTWRecomp](https://github.com/vasist15-source/BOTWRecomp) | Breath of the Wild (Wii U 1.5.0) statically recompiled to native macOS/Metal | 12 | 🟢 | C |
| [BurnoutDominatorReversed](https://github.com/literalynn/BurnoutDominatorReversed) | Burnout Dominator (PS2) recompiled into a native PC game | 12 | 🟢 | C++ |
| [Dragon Ball Z: Budokai Tenkaichi 2 (BT2 Recomp)](https://github.com/oric212/BT2-Recomp) | Static recompilation of Dragon Ball Z: Budokai Tenkaichi 2 (PS2) into a native PC port | 12 | 🟢 | C++ |
| [Gauntlet-Dark-Legacy-PC-Port](https://github.com/sabishii-bit/Gauntlet-Dark-Legacy-PC-Port) | Fan-made unofficial PC port of Gauntlet: Dark Legacy | 12 | 🟢 | C++ |
| [Gears of War](https://github.com/SomeoneIsWorking/gears1) | Static recompilation of Gears of War (Xbox 360) into a native PC port | 12 | 🟢 | C++ |
| [gravityrush_pc](https://github.com/Prathewsh/gravityrush_pc) | Experimental native Windows runtime for Gravity Rush Remastered and Gravity Rush 2 (PS4) | 12 | 🟢 | C++ |
| [gsrandroid](https://github.com/wootbeer/gsrandroid) | Golden Sun (GBA) recompiled as a native Android port | 12 | 🟢 | C++ |
| [helix](https://github.com/retrofoundry/helix) | Library that simplifies running N64 software on PC | 12 | 🟢 | C++ |
| [infamous2-recomp](https://github.com/erikomis/infamous2-recomp) | Static recompilation of inFAMOUS 2 (PS3) to native macOS with ps3recomp | 12 | 🟢 | Rust |
| [Legends-Recomp (Rayman Legends)](https://github.com/edeegg/Legends-Recomp) | Static recompilation of Rayman Legends (Xbox 360) into a native port | 12 | 🟢 |  |
| [lego-dimensions-pc](https://github.com/vascon-es/lego-dimensions-pc) | Unofficial native Windows port of LEGO Dimensions (PS4) | 12 | 🟢 | C++ |
| [Marvel Nemesis: Rise of the Imperfects (Marvel Nemesis: Rise of the Imperfects - PC Recomp)](https://github.com/15Cyber/marvel-nemesis-recomp) | Static recompilation of Marvel Nemesis: Rise of the Imperfects (Xbox) into a native PC port | 12 | 🟢 | C++ |
| [New Super Mario Bros. Wii](https://github.com/ral1009/NSMBWiicompiled) | Static recompilation of New Super Mario Bros. Wii (Wii) into a native PC port | 12 | 🟢 | C++ |
| [Pacman-CE-PC-Recomp](https://github.com/jedeyesniv-art/Pacman-CE-PC-Recomp) | Recompilation of Pac-Man Championship Edition (Xbox 360) for PC and Steam Deck | 12 | 🟢 | C++ |
| [Paper Mario ( pmvita)](https://github.com/versacepapermario/papermario-pc-upload) | Unofficial native port of Paper Mario (N64) | 12 | 🟢 | C |
| [Point Blank](https://github.com/TekRantGaming/point-blank-recompiled) | Static recompilation of Point Blank (PS1) into a native PC port | 12 | 🟢 | PowerShell |
| [Pokémon Platinum port](https://github.com/GabeSud0/pokeplatinum-3ds) | Native Nintendo 3DS port of Pokémon Platinum built from the pret decompilation | 12 | 🟢 | C |
| [Pokémon Snap](https://github.com/chrissotraidis/snappad) | Static recompilation of Pokémon Snap (N64) into a native PC port | 12 | 🟢 | Python |
| [racer (Star Wars Episode I: Racer)](https://github.com/sp00nznet/racer) | Static recompilation of Star Wars Episode I: Racer (N64) to native PC | 12 | 🟢 | C++ |
| [reNut (Banjo-Kazooie: Nuts & Bolts)](https://github.com/etonedemid/reNut_linuxfixes) | Banjo-Kazooie: Nuts & Bolts (Xbox 360) recompilation with ReXGlue, with Linux fixes | 12 | 🗄️ | C++ |
| [Ridge Racer port](https://github.com/kazuyette/rr-pc-port) | PC port of Ridge Racer (PS1) derived from the byte-matched rr-decomp | 12 | 🟢 | C |
| [Skate 3](https://github.com/HelmXGaming/Skate-3-Recompiled--Work-in-Progress-) | Static recompilation of Skate 3 (Xbox 360) into a native PC port | 12 | 🟢 | C++ |
| [sms-android](https://github.com/jbcgames/sms-android) | Native Android port of Super Mario Sunshine (GameCube) with touch controls | 12 | 🟢 | C++ |
| [SSB-X](https://github.com/Team-Resurgent/SSB-X) | Super Smash Bros. port to the original Xbox from the N64 decompilation | 12 | 🟢 | C |
| [streetrod-enhanced (Street Rod)](https://github.com/kylofon/streetrod-enhanced) | Enhanced native SDL3 port of Street Rod (1989, DOS) | 12 | 🟢 | C |
| [Super Bomberman](https://github.com/elliotttate/BombermanRecomp) | Static recompilation of Super Bomberman (SNES) into a native PC port | 12 | 🟢 | C |
| [Super Mario Kart](https://github.com/jvipond/super_mario_kart_recompilation) | Static recompilation of Super Mario Kart (SNES) into a native PC port | 12 | 🔴 | C++ |
| [Super Mario RPG: Legend of the Seven Stars](https://github.com/mstan/SuperMarioRPGRecomp) | Static recompilation of Super Mario RPG: Legend of the Seven Stars (SNES) into a native PC port | 12 | 🟢 | C |
| [The Sims 2](https://github.com/abilliontokens/sims2-recomp) | Static recompilation of The Sims 2 (Xbox) into a native PC port | 12 | 🟢 | C++ |
| [the-3rd-birthday-recomp](https://github.com/BasedYuki/the-3rd-birthday-recomp) | Native PC port of The 3rd Birthday (PSP) via static recompilation | 12 | 🟢 | C |
| [Tokyo Jungle](https://github.com/sp00nznet/tokyojungle) | Static recompilation of Tokyo Jungle (PS3) into a native PC port | 12 | 🟢 | C++ |
| [unreal_nx (Unreal)](https://github.com/fgsfdsfgs/unreal_nx) | Nintendo Switch port and loader for Unreal (1998) and Unreal Gold | 12 | 🔴 | C |
| [utp (Unreal Tournament)](https://github.com/chrissotraidis/utp) | Unreal Tournament 99 hosted natively on iPhone and iPad with Metal rendering | 12 | 🟢 | Swift |
| [valiant-vita (Valiant Hearts)](https://github.com/Rinnegatamante/valiant-vita) | PS Vita port of Valiant Hearts: The Great War via the Android version loader | 12 | 🟡 | C |
| [Vigilante 8 / Vigilante 8: 2nd Offense](https://github.com/GTTeancum/Vigilante-8-recomp) | Static recompilation of Vigilante 8 / Vigilante 8: 2nd Offense (PS1) into a native PC port | 12 | 🟢 | C |
| [Wipeout Pure](https://github.com/erreib/pure-recomp) | Static recompilation of Wipeout Pure (PSP) into a native PC port | 12 | 🟢 | Python |
| [Xevious (xevious (arcade -> 68k transcode))](https://github.com/jotd666/xevious) | Unofficial native port of Xevious (Arcade) | 12 | 🟢 | C |
| [Astral Chain (AC-Recomp)](https://github.com/swaymun/AC-Recomp) | Static recompilation of Astral Chain (Switch) into a native PC port | 11 | 🟢 | Python |
| [barrelpad (Diddy Kong Racing)](https://github.com/chrissotraidis/barrelpad) | Diddy Kong Racing recompilation for macOS, iOS and iPadOS | 11 | 🟢 | Objective-C++ |
| [Blast Corps (Power Dozer)](https://github.com/djultra64/Power-Dozer) | Static recompilation of Blast Corps (N64) into a native PC port | 11 | 🟢 | C++ |
| [clockwork](https://github.com/clockwork-recompdev/clockwork) | Native PC versions of the Yo-kai Watch 3DS games by static recompilation | 11 | 🟢 | C++ |
| [dinopad (Dinosaur Planet)](https://github.com/chrissotraidis/dinopad) | Dinosaur Planet recompilation for macOS, iOS and iPadOS | 11 | 🟢 | Objective-C++ |
| [DragonBallZLegacyOfGokuRecomp](https://github.com/mstan/DragonBallZLegacyOfGokuRecomp) | Static recompilation of Dragon Ball Z: The Legacy of Goku with Adaptive Widescreen · Part of the R.A.I.D. community | 11 | 🟢 | C++ |
| [Duke Nukem: Zero Hour (DukeNukemZeroHourPort (Gillou68310))](https://github.com/Gillou68310/DukeNukemZeroHourPort) | Unofficial native port of Duke Nukem: Zero Hour (N64) | 11 | 🟢 | C |
| [Herculan](https://github.com/kevinfoley/Herculan) | Recomp of Earthsiege 2 by Dynamix. | 11 | 🟢 | C# |
| [linksawakening-portable](https://github.com/sp00nznet/linksawakening-portable) | Link's Awakening DX statically recompiled to native C and ported to PlayStation 4, PlayStation 3, and Nintendo 3DS. N... | 11 | 🟢 | Shell |
| [mh3u-port](https://github.com/glinesbdev/mh3u-port) | Static recompilation of Monster Hunter 3 Ultimate (Wii U) for Windows and Linux | 11 | 🟢 | Rust |
| [PokeRecomp](https://github.com/sonsegajp/PokeRecomp) | Native PC ports of Pokémon games via static recompilation | 11 | 🟢 | C |
| [Puyo Puyo BOX](https://github.com/kirby1237/PuyoPuyoBoxRecomp) | Static recompilation of Puyo Puyo BOX (PS1) into a native PC port | 11 | 🟢 | Shell |
| [RaymanOriginsRecomp](https://github.com/XDanfr/RaymanOriginsRecomp) | Unofficial static recompilation of Rayman Origins (Xbox 360) for Switch via XenonRecomp | 11 | 🟢 | C++ |
| [Super Mario Bros. 35 (SM35 Recomp)](https://github.com/sm35recomp/sm35recomp) | Static recompilation of Super Mario Bros. 35 (Switch) into a native PC port | 11 | 🟢 | C |
| [SuperRecomp](https://github.com/dreamsailing59-ops/SuperRecomp) | Tool to statically recompile SNES games into native executables | 11 | 🟢 | C++ |
| [Tekken 3](https://github.com/Mabec-games/Tekken-3-for-Linux) | Static recompilation of Tekken 3 (PS1) into a native PC port | 11 | 🟢 | C++ |
| [Tekken: Dark Resurrection (tkdr-recomp)](https://github.com/gasparegas/tkdr-recomp) | Static recompilation of Tekken: Dark Resurrection (PSP) into a native PC port | 11 | 🟢 | C |
| [The Simpsons Arcade Game](https://github.com/sp00nznet/simpsonsarcade-ps3) | Static recompilation of The Simpsons Arcade Game (PS3) into a native PC port | 11 | 🟢 | C |
| [thimbleweed-vita (Thimbleweed Park)](https://github.com/Rinnegatamante/thimbleweed-vita) | PS Vita port of Thimbleweed Park via the Android version loader | 11 | 🟡 | C |
| [Titanic: Adventure Out of Time](https://github.com/itskenny0/titanic-godot) | Recomp of Titanic Adventure Out of Time to Godot. | 11 | 🟢 | Go |
| [trials-hd-recompiled](https://github.com/snufflyyy/trials-hd-recompiled) | Static recompilation of Trials HD (Xbox 360) | 11 | 🟢 | C++ |
| [VeronicaRecomp](https://github.com/psxrestore/VeronicaRecomp) | A static recompilation of Resident Evil CODE:Veronica developed with RexGlue. | 11 | 🟢 | C++ |
| [wwe2k14-recomp (Jarrodfeng)](https://github.com/Jarrodfeng/wwe2k14-recomp) | Native PC recompilation of WWE 2K14 (Xbox 360) | 11 | 🟢 | C++ |
| [3on3NHL-recomp](https://github.com/Wndwsqrrl/3on3NHL-recomp) | 3 on 3 NHL Arcade Xbox 360 static recompilation | 10 | 🟢 | C# |
| [Alone in the Dark: The New Nightmare](https://github.com/alexbeavs-ps1-ports/alone-in-the-dark-the-new-nightmare-recomp) | Static recompilation of Alone in the Dark: The New Nightmare (PS1) into a native PC port | 10 | 🟢 | Shell |
| [Alundra](https://github.com/alexbeavs-ps1-ports/alundra-recomp) | Static recompilation of Alundra (PS1) into a native PC port | 10 | 🟢 | Python |
| [ArmyOfTwo40thDay-Recomp](https://github.com/crabscrab650-sketch/ArmyOfTwo40thDay-Recomp) | ReXGlue PC recompilation of Army of Two: The 40th Day (Xbox 360) | 10 | 🟢 | C++ |
| [bo2-recompiled](https://github.com/officialmelon/bo2-recompiled) | Call of Duty: Black Ops II (Xbox 360) recompiled to native PC | 10 | 🟢 | C++ |
| [chip8recompiled](https://github.com/arcanite24/chip8recompiled) | Static recompilation toolchain that turns CHIP-8 ROMs into native executables | 10 | 🟢 | C |
| [cod3-recomp](https://github.com/jxnplays/cod3-recomp) | Call of Duty 3 (Xbox 360) recompiled to native x86-64 for Windows | 10 | 🟢 | C++ |
| [dcrecomp](https://github.com/sp00nznet/dcrecomp) | Static recompilation framework for Dreamcast and NAOMI games (SH-4 to C) | 10 | 🟢 | C |
| [defjam-sw](https://github.com/R-drg/defjam-sw) | Def Jam: Fight for NY (Xbox) statically recompiled for Switch and Linux | 10 | 🟢 | C |
| [doa2u-re](https://github.com/NoRain211/doa2u-re) | Native Windows port of Dead or Alive 2 Ultimate (Xbox) by static recompilation | 10 | 🟢 | C |
| [Dragon-Burst](https://github.com/dfdx047/Dragon-Burst) | ReXGlue static recompilation of Dragon Ball Z: Burst Limit (Xbox 360) for Android | 10 | 🟢 | Kotlin |
| [f0x (F-Zero X)](https://github.com/chrissotraidis/f0x) | Native F-Zero X source port via G-Diffuser for Apple Silicon Macs, iPhone and iPad | 10 | 🟢 | Shell |
| [FNV-nx](https://github.com/CypherNoodle/FNV-nx) | Experimental native Switch port of Fallout: New Vegas from the Xbox 360 version | 10 | 🟢 | C |
| [FrontschweineRecomp](https://github.com/Nero2611/FrontschweineRecomp) | Native PC port of Hogs of War (PS1) via static recompilation | 10 | 🟢 | C |
| [gbarecomp (sp00nznet)](https://github.com/sp00nznet/gbarecomp) | Static recompilation toolkit for Game Boy Advance ROMs | 10 | 🟢 | C |
| [GoW2-nativo-PS2 (God of War II)](https://github.com/cxldsakeb/GoW2-nativo-PS2) | Native PC port of God of War II (PS2) via PS2Recomp | 10 | 🟢 | C++ |
| [hctp-recomp](https://github.com/BigDaddyJRich/hctp-recomp) | Static recompilation of WWE SmackDown! Here Comes the Pain (PS2) for PC | 10 | 🟢 | C++ |
| [heavymetal](https://github.com/sp00nznet/heavymetal) | A static recompilation of Heavy Metal: FAKK2 (2000) targeting modern Windows 11 x86-64. | 10 | 🟢 | C |
| [Jet Moto 2](https://github.com/goodshepherd23/JetMoto2-Recomp) | Static recompilation of Jet Moto 2 (PS1) into a native PC port | 10 | 🟢 | C# |
| [layton2-vita (Professor Layton)](https://github.com/Rinnegatamante/layton2-vita) | PS Vita port of Professor Layton and Pandora's Box HD via the Android version loader | 10 | 🔴 | C |
| [lordran-native](https://github.com/Nishikori-Yui/lordran-native) | Experimental native port of Dark Souls Remastered (Switch) to macOS and iOS | 10 | 🟢 | C |
| [Marvel vs. Capcom: Clash of Super Heroes (Marvel vs. Capcom: Clash of Super Heroes Recompiled)](https://github.com/TechnicallyComputers/Marvel-vs.-Capcom-Clash-of-Super-Heroes-Recomp) | Static recompilation of Marvel vs. Capcom: Clash of Super Heroes (PS1) into a native PC port | 10 | 🟢 | C |
| [pc-thelaststory](https://github.com/vs-sr-dev/pc-thelaststory) | Work toward a native PC port of The Last Story (Wii) by recompiling its executable | 10 | 🟢 | Python |
| [Pokémon Red and Blue (PokemonRedAndBlueRecomp)](https://github.com/mstan/PokemonRedAndBlueRecomp) | Static recompilation of Pokémon Red and Blue (Game Boy) into a native PC port | 10 | 🟢 | C |
| [PS5_Ghostship (Super Mario 64)](https://github.com/griches/PS5_Ghostship) | Super Mario 64 for PS5 homebrew, built from Ghostship (libultraship) | 10 | 🟢 | C |
| [ReCompiledSteel](https://github.com/tokeneffortports/ReCompiledSteel) | Real Steel (Xbox 360) recompiled to native code for Windows, Linux and Android | 10 | 🟢 | C++ |
| [San Francisco Rush 2049](https://github.com/n64hub/rush-2049-recomp) | Static recompilation of San Francisco Rush 2049 (N64) into a native PC port | 10 | 🟢 | C++ |
| [smsggrecomp](https://github.com/mstan/smsggrecomp) | Static recompiler for Sega Master System and Game Gear games | 10 | 🟢 | C |
| [snatcher-port](https://github.com/bgyss/snatcher-port) | Native Mac/Windows build of Konami's Snatcher (Sega CD) from reverse engineering | 10 | 🟢 | C++ |
| [Star wars - Episode I - Jedi Power Battles](https://github.com/TechnicallyComputers/Star-wars---Episode-I---Jedi-Power-Battles-Recomp) | Static recompilation of Star wars - Episode I - Jedi Power Battles (PS1) into a native PC port | 10 | 🟢 | C |
| [swordigo-vita (Swordigo)](https://github.com/Rinnegatamante/swordigo-vita) | PS Vita port of Swordigo via the Android version loader | 10 | 🟡 | C |
| [The Dishwasher: Dead Samurai (DishSoap)](https://github.com/Hdmaniak/DishSoap) | Unofficial native port of The Dishwasher: Dead Samurai (Xbox 360) | 10 | 🟢 | C# |
| [the-simpsons-game-android](https://github.com/codepdbh/the-simpsons-game-android) | Groundwork for a native Android port of The Simpsons Game via static recompilation | 10 | 🟢 | Java |
| [the-simpsons-recomp](https://github.com/portingpete/the-simpsons-recomp) | Native Windows port of The Simpsons Game (Xbox 360) via PowerPC-to-C++ recompilation | 10 | 🟢 | C++ |
| [tomodachi-native](https://github.com/kuosuko/tomodachi-native) | Tomodachi Life: Living the Dream running natively on Apple Silicon Macs and iPads | 10 | 🟢 | C |
| [ToyStory2](https://github.com/PeriBluGaming/ToyStory2Recomp) | Static recompilation of ToyStory2 (PS1) into a native PC port | 10 | 🟢 | C |
| [Wild9Recomp](https://github.com/plinkr/Wild9Recomp) | Native PC port of Wild 9 (PS1) via static recompilation | 10 | 🟢 | C |
| [Yoshi's Cookie](https://github.com/mstan/YoshisCookieRecomp) | Static recompilation of Yoshi's Cookie (NES) into a native PC port | 10 | 🟢 | C |
| [afterburner-vita (After Burner Climax)](https://github.com/Rinnegatamante/afterburner-vita) | PS Vita port of After Burner Climax via the Android version loader | 9 | 🟢 | C |
| [ben10-omniverse-recomp](https://github.com/andrebrumdev/ben10-omniverse-recomp) | Native macOS port of Ben 10 Omniverse (PS3) by static recompilation | 9 | 🟢 | Python |
| [caesar2-port](https://github.com/second-impressions/caesar2-port) | Portable continuation of the Caesar II source reconstruction | 9 | 🟢 | C |
| [Cars-Race-O-Rama-Recompiled](https://github.com/m1ndcrap/Cars-Race-O-Rama-Recompiled) | Recompilation of Cars Race-O-Rama (Xbox 360) with ReXGlue | 9 | 🟢 | CMake |
| [DisruptorRecomp](https://github.com/RecompTeam/DisruptorRecomp) | Static recompilation of Disruptor (PS1) | 9 | 🟢 | C++ |
| [dream-recomp](https://github.com/phobos665/dream-recomp) | Static recompilation tool for Dreamcast games | 9 | 🟢 | C++ |
| [dreams-to-reality-re](https://github.com/jlagedo/dreams-to-reality-re) | Static recompilation of Dreams to Reality (Cryo, 1997) to C for modern PCs | 9 | 🟢 | Python |
| [ForzaHorizon2Recomp-Android](https://github.com/deivid22srk/ForzaHorizon2Recomp-Android) | Forza Horizon 2 (Xbox 360) static recompilation for Android arm64 | 9 | 🟢 | C++ |
| [GalaxyFrame](https://github.com/PodeCaradox/GalaxyFrame) | Super Mario Galaxy in VR on Steam Frame, built on the Petari decompilation | 9 | 🟢 | C++ |
| [HobbitRecompiled](https://github.com/itsdunintime104/HobbitRecompiled) | LEGO The Hobbit recompiled to run natively on Apple Silicon Macs | 9 | 🟢 | Shell |
| [HPCOS-GC-RECOMP](https://github.com/ant0-blase/HPCOS-GC-RECOMP) | Static recompilation of Harry Potter and the Chamber of Secrets (GameCube) | 9 | 🗄️ | C |
| [HydroThunderPORT](https://github.com/monscriser/HydroThunderPORT) | Experimental Windows and Linux recompilation of Hydro Thunder Hurricane (Xbox 360) | 9 | 🟢 | GLSL |
| [layton3-vita (Professor Layton)](https://github.com/Rinnegatamante/layton3-vita) | PS Vita port of Professor Layton and the Lost Future HD via the Android version loader | 9 | 🔴 | C |
| [LinksAwakening (Link's Awakening DX)](https://github.com/sp00nznet/LinksAwakening) | Static recompilation of The Legend of Zelda: Link's Awakening DX (GBC) to native code | 9 | 🟢 | C |
| [Mario-Kart-64-X](https://github.com/Team-Resurgent/Mario-Kart-64-X) | Mario Kart 64 port to the original Xbox from the N64 decompilation | 9 | 🟢 | C |
| [Mega Man Legends](https://github.com/alexbeavs-ps1-ports/mega-man-legends-recomp) | Static recompilation of Mega Man Legends (PS1) into a native PC port | 9 | 🟢 | Python |
| [Minecraft Xbox 360 Edition Recompiled](https://github.com/HiroStuff/minecraft) | Minecraft: Xbox 360 Edition recompiled to native PC | 9 | 🗄️ | C++ |
| [PokemonYellowRecomp (Pokémon Yellow)](https://github.com/mstan/PokemonYellowRecomp) | Static recompilation of Pokémon Yellow (Game Boy) | 9 | 🟢 | Python |
| [PS5_Burnout3](https://github.com/griches/PS5_Burnout3) | Burnout 3: Takedown on PS5 homebrew, ported from the Takedawn static recompilation | 9 | 🟢 | C |
| [psx-spyro (Spyro the Dragon)](https://github.com/SomeoneIsWorking/psx-spyro) | Native PC port of Spyro the Dragon (PS1) built on a static-recompilation framework | 9 | 🟢 | C++ |
| [Rampage Through Time (Rampage Through Time Recompiled)](https://github.com/TechnicallyComputers/Rampage---Through-Time-Recomp) | Static recompilation of Rampage Through Time (PS1) into a native PC port | 9 | 🟢 | C |
| [Rumble Roses XX](https://github.com/Revan67/RumbleRosesXX-Recomp) | Static recompilation of Rumble Roses XX (Xbox 360) into a native PC port | 9 | 🟢 | CMake |
| [Shantae](https://github.com/vibecodekun/shantaerecomp) | Static recompilation of Shantae (Game Boy Color) into a native PC port | 9 | 🟢 | C |
| [simpsonsarcade (The Simpsons Arcade)](https://github.com/sp00nznet/simpsonsarcade) | Static recompilation of The Simpsons Arcade (Xbox 360 XBLA) to native Windows | 9 | 🟢 | C++ |
| [SNESRecomp (blueberry077)](https://github.com/blueberry077/SNESRecomp) | Experimental reassembler that rebuilds SNES games from execution traces | 9 | 🟢 | C++ |
| [SonicTheHedgehogSMSRecomp](https://github.com/mstan/SonicTheHedgehogSMSRecomp) | Static recompilation of Sonic the Hedgehog (Master System) | 9 | 🟢 | PowerShell |
| [StarWars-CloneWars-PC](https://github.com/GTTeancum/StarWars-CloneWars-PC) | Native Windows port of Star Wars: The Clone Wars (Xbox) via static recompilation | 9 | 🟢 | C++ |
| [StrikersRecomp](https://github.com/aharonahdoot/StrikersRecomp) | Super Mario Strikers (G4QE01) recompilation project — the worked example for RecompCore and DolRuntime. No game data... | 9 | 🟢 | C |
| [TDURecomp](https://github.com/testdriveupgrade/TDURecomp) | Recompilation of TDU | 9 | 🟢 | C++ |
| [Tetrisphere](https://github.com/djultra64/Blocksphere) | Static recompilation of Tetrisphere (N64) into a native PC port | 9 | 🟢 | C++ |
| [Top-Gear-SNES-Static-Recomp](https://github.com/Junior-Jones/Top-Gear-SNES-Static-Recomp) | Static recompilation of Top Gear (SNES) for Windows 10 and 11. ROM not included. | 9 | 🟢 | C |
| [VagrantStory](https://github.com/riotashley81-jpg/vagrantstory_recomp) | Static recompilation of VagrantStory (PS1) into a native PC port | 9 | 🟢 | C |
| [Virtual Pro Wrestling 2: Ōdō Keishō](https://github.com/jessetbh/VPW2Recomp) | Static recompilation of Virtual Pro Wrestling 2: Ōdō Keishō (N64) into a native PC port | 9 | 🟢 | C |
| [VPW64Recomp](https://github.com/jessetbh/VPW64Recomp) | Virtual Pro Wrestling 64 static recompilation | 9 | 🟢 | C++ |
| [WhiteAlbum2_iOS](https://github.com/galhack/WhiteAlbum2_iOS) | Native port of WHITE ALBUM 2 for iPhone, iPad, Vision Pro, Apple TV and Mac | 9 | 🟢 | C# |
| [wipeout-xl-recomp (Wipeout XL)](https://github.com/alexbeavs-ps1-ports/wipeout-xl-recomp) | Static recompilation setup for Wipeout XL (PS1) | 9 | 🟢 | Python |
| [Xenon-Recomp (nimauria)](https://github.com/nimauria/Xenon-Recomp) | Experimental Xbox 360 ahead-of-time recompilation framework and native runtime | 9 | 🟢 | C++ |
| [YoshiNESRecomp (Yoshi)](https://github.com/mstan/YoshiNESRecomp) | Static recompilation of Yoshi (NES) | 9 | 🟢 | C |
| [ace-combat-3-electrosphere-recomp](https://github.com/alexbeavs-ps1-ports/ace-combat-3-electrosphere-recomp) | Static recompilation setup for Ace Combat 3: Electrosphere (PS1, Japan) | 8 | 🟢 | Python |
| [aerobiz-disasm](https://github.com/matiaszanolli/aerobiz-disasm) | Complete static recompilation of Aerobiz Supersonic for the Sega Genesis | 8 | 🟢 | Assembly |
| [Animal Crossing decomp](https://github.com/TechProGabe/OpenCrossing-Dreamcast) | Dreamcast port of Animal Crossing (GameCube) built on the ACreTeam decompilation | 8 | 🟢 | C |
| [aw64 (Another World)](https://github.com/jnmartin84/aw64) | Nintendo 64 port of the Another World bytecode interpreter | 8 | 🔴 | C++ |
| [Bomberman Party Edition (Bomberman Party Edition Recomp)](https://github.com/TechnicallyComputers/BombermanPartyEditionRecomp) | Static recompilation of Bomberman Party Edition (PS1) into a native PC port | 8 | 🟢 | C |
| [Bomberman World (Bomberman World Recompiled)](https://github.com/TechnicallyComputers/Bomberman-World-Recomp) | Static recompilation of Bomberman World (PS1) into a native PC port | 8 | 🟢 | C |
| [bushido-blade-2-recomp (Bushido Blade 2)](https://github.com/alexbeavs-ps1-ports/bushido-blade-2-recomp) | Static recompilation of Bushido Blade 2 (PS1) | 8 | 🟢 | Python |
| [Call-of-Duty-3-Recompilation](https://github.com/zombiedestroyer29/Call-of-Duty-3-Recompilation) | Recompilation of Call of Duty 3 multiplayer (Xbox 360) with ReXGlue | 8 | 🟢 | C++ |
| [cdirecomp](https://github.com/mstan/cdirecomp) | Static recompiler for Philips CD-i games | 8 | 🟢 | C |
| [colin-mcrae-rally-2-0-recomp](https://github.com/alexbeavs-ps1-ports/colin-mcrae-rally-2-0-recomp) | Static recompilation setup for Colin McRae Rally 2.0 (PS1) | 8 | 🟢 | Python |
| [DeepSea](https://github.com/AH64-dll/DeepSea) | Deep Sea: The Wind Waker at 60 fps. A free, open-source native Windows port you build from your own disc. | 8 | 🟢 | C |
| [dksnes (Donkey Kong)](https://github.com/furrykef/dksnes) | Port of the NES Donkey Kong to the SNES built from a disassembly | 8 | 🔴 | Assembly |
| [Doraemon: Nobita to Mittsu no Seireiseki](https://github.com/citrongames/Dora64) | Static recompilation of Doraemon: Nobita to Mittsu no Seireiseki (N64) into a native PC port | 8 | 🟢 | C++ |
| [Driver Recompiled](https://github.com/alexbeavs-ps1-ports/driver-recomp) | psxrecomp static recompilation of Driver (PS1) packaged as a native PC port | 8 | 🟢 | Python |
| [ffd-vita (Final Fantasy Dimensions)](https://github.com/Rinnegatamante/ffd-vita) | PS Vita port of Final Fantasy Dimensions via the Android version loader | 8 | 🟡 | C |
| [FuseRecomp](https://github.com/nikolaygorb/FuseRecomp) | RexGlue static recompilation of Fuse (Xbox 360) | 8 | 🟢 | C++ |
| [gcrecomp](https://github.com/sp00nznet/gcrecomp) | Static recompilation toolkit for GameCube games | 8 | 🟢 | C++ |
| [GoldenEye-Recomp (XBLA)](https://github.com/ericksa1417/GoldenEye-Recomp) | Runs GoldenEye 007 (Xbox 360 XBLA) natively on Windows through static recompilation | 8 | 🟢 | C++ |
| [Gow2HD-Windows](https://github.com/sethlikepie/Gow2HD-Windows) | Static recompilation of God of War II HD (PS3) to Windows | 8 | 🟢 | Python |
| [HIRAKU](https://github.com/Roganis/HIRAKU) | Konami BEMANI arcade games (Firebeat, DJ Main) recompiled as native Linux and Windows programs | 8 | 🟢 | C++ |
| [hobbit-1982-native](https://github.com/7ucina/hobbit-1982-native) | The Hobbit (ZX Spectrum, 1982) ported to C routine by routine | 8 | 🟢 | C |
| [htrecomp (Hydro Thunder Hurricane)](https://github.com/visibou/htrecomp) | Native PC build of Hydro Thunder Hurricane (Xbox 360) | 8 | 🟢 | C++ |
| [icerage-native-arm (Ice Rage)](https://github.com/EapRules/icerage-native-arm) | Ice Rage running natively on Linux ARM handhelds through an Android ELF loader | 8 | 🟢 | C++ |
| [Jak and Daxter port](https://github.com/chrissotraidis/ottsel) | Native iPad, iPhone and Mac port of Jak and Daxter built on OpenGOAL | 8 | 🟢 | C++ |
| [Jungle Strike](https://github.com/Junior-Jones/Jungle-Strike-SNES-Static-Recomp) | Static recompilation of Jungle Strike (SNES) into a native PC port | 8 | 🟢 | C |
| [MegaMan64Recompiled-Mobile](https://github.com/DevZer0D4Y/MegaMan64Recompiled-Mobile) | Android and iOS port of Mega Man 64 Recompiled with touch controls | 8 | 🟢 | C++ |
| [mksm-recomp](https://github.com/OGmidway/mksm-recomp) | Native recompilation of Mortal Kombat: Shaolin Monks (NTSC) | 8 | 🟢 | C++ |
| [NFS-Carbon-NX](https://github.com/zofo007/NFS-Carbon-NX) | Need for Speed Carbon (Xbox 360) statically recompiled for Nintendo Switch | 8 | 🟢 | C++ |
| [nfsmw-recomp-android](https://github.com/DEBARSHI-SARKAR/nfsmw-recomp-android) | Recompilation of Need for Speed: Most Wanted (2005 PC) for Android and Linux | 8 | 🟢 | Assembly |
| [OpenPopTB-MacOS](https://github.com/iagodemacedo/OpenPopTB-MacOS) | Native Apple Silicon port of Populous: The Beginning via static recompilation | 8 | 🟢 | C |
| [oracles-nx](https://github.com/toniisound/oracles-nx) | Switch homebrew port of oracles-decomp, the C reimplementation of the Zelda Oracle games | 8 | 🟢 | C |
| [payne-recomp](https://github.com/phobos665/payne-recomp) | Recompilation of Max Payne (Xbox) | 8 | 🟢 | C |
| [portemon](https://github.com/portemon-nitro/portemon) | Getting HeartGold/SoulSilver out of the DS | 8 | 🟢 | Lua |
| [PSP2I_Recomp](https://github.com/zmbkilla/PSP2I_Recomp) | Recompilation of Phantasy Star Portable 2 Infinity (PSP) | 8 | 🟢 | C |
| [puzzleleague64_recomp](https://github.com/AngheloAlf/puzzleleague64_recomp) | Static recompilation of Pokémon Puzzle League (N64) | 8 | 🗄️ | C++ |
| [reach_cache_debug_recomp (Halo: Reach)](https://github.com/twist84/reach_cache_debug_recomp) | Recompilation of a Halo: Reach (Xbox 360) debug build | 8 | 🟢 | C++ |
| [RROP](https://github.com/kruzeman/RROP) | Static recompilation of Rings of Power for Linux and Windows with widescreen and smooth scrolling | 8 | 🟢 | Python |
| [rygar-snes (Rygar)](https://github.com/rumbleminze/rygar-snes) | SNES port of the NES game Rygar | 8 | 🟡 | Assembly |
| [sfiii-native](https://github.com/mattkuhnQAAI/sfiii-native) | Native Windows static recompilation of Shining Force III Scenario 1 (Saturn) | 8 | 🟢 | Python |
| [sh4-nx](https://github.com/72ak/sh4-nx) | Silent Hill 4: The Room (PC) statically recompiled to run natively on Switch | 8 | 🟢 | C |
| [shadow-the-hedgehog-recomp](https://github.com/nicolasserpa/shadow-the-hedgehog-recomp) | Static recompilation of Shadow the Hedgehog (PS2) into a native PC port | 8 | 🟢 | CMake |
| [sotn-vita (Symphony of the Night)](https://github.com/Rinnegatamante/sotn-vita) | PS Vita port of Castlevania: Symphony of the Night (Android) via the Android version loader | 8 | 🟢 | C |
| [South Park Tower Defense Recompiled](https://github.com/TekRantGaming/south-park-tower-defense-recompiled) | Static recompilation of South Park: Let's Go Tower Defense Play! (Xbox 360 XBLA) | 8 | 🟢 | C++ |
| [South Park: Tenorman's Revenge Recompiled](https://github.com/TekRantGaming/south-park-tenormans-revenge-recompiled) | Static recompilation of South Park: Tenorman's Revenge (Xbox 360 XBLA) for Windows and Linux | 8 | 🟢 | C++ |
| [Street Rod](https://github.com/kylofon/street-rod-sdl3) | Recomp of Street Rod. | 8 | 🟢 | C |
| [Suikoden II](https://github.com/alexbeavs-ps1-ports/suikoden-ii-recomp) | Static recompilation of Suikoden II (PS1) into a native PC port | 8 | 🟢 | Python |
| [superman_returns_recomp](https://github.com/MrPowerUp82/superman_returns_recomp) | ReXGlue static recompilation of Superman Returns (Xbox 360) for PC | 8 | 🟢 | C++ |
| [SuperSmashBrosRecomp](https://github.com/sonicdcer/SuperSmashBrosRecomp) | Static recompilation of Super Smash Bros. (N64) for Windows, Linux and macOS | 8 | 🟢 | C++ |
| [Tony-Hawks-Project-8-Recomp](https://github.com/SunJaycy/Tony-Hawks-Project-8-Recomp) | Recompilation of Tony Hawk's Project 8 (Xbox 360) | 8 | 🟢 | CMake |
| [TwistedMetal1234Recomp](https://github.com/jcoker85/TwistedMetal1234Recomp) | Twisted Metal 1-4 (PS1) recompiled for PC using psxrecomp | 8 | 🟢 | C |
| [Zeliard disassembly](https://github.com/nolanvenhola/zeliard) | C and WebAssembly port of Zeliard (DOS) based on its disassembly | 8 | 🟢 | Assembly |
| [2ship2harkinian-ps4](https://github.com/alechurri/2ship2harkinian-ps4) | Majora's Mask (2 Ship 2 Harkinian) native port for jailbroken PS4 | 7 | 🟢 | Shell |
| [armored-core-recomp (Armored Core)](https://github.com/alexbeavs-ps1-ports/armored-core-recomp) | Static recompilation setup for Armored Core (PS1) | 7 | 🟢 | Python |
| [Bakugan-NX](https://github.com/Wiredlainn-afk/Bakugan-NX) | Native Nintendo Switch port of Bakugan Battle Brawlers | 7 | 🟢 | C |
| [Banjo-Tooie](https://github.com/iron-jay/banjo_tooie_xbla_recomp) | Static recompilation of Banjo-Tooie (Xbox 360) into a native PC port | 7 | 🟢 | Python |
| [BeetleRecomp](https://github.com/bryankruman/BeetleRecomp) | Native PC port of Beetle Adventure Racing (N64) via N64Recomp and RT64 | 7 | 🟢 | C++ |
| [black-macos-recomp](https://github.com/elpetese/black-macos-recomp) | Static recompilation of Black (Xbox) to native macOS on Apple Silicon | 7 | 🟢 | C |
| [burnout-revenge](https://github.com/secretpray/burnout-revenge) | Native Burnout Revenge (Xbox 360) port for Apple silicon Macs by static recompilation | 7 | 🟢 | C++ |
| [colony-wars-red-sun-recomp](https://github.com/alexbeavs-ps1-ports/colony-wars-red-sun-recomp) | Static recompilation of Colony Wars: Red Sun (PS1) | 7 | 🟢 | Python |
| [crazytaxi (Crazy Taxi)](https://github.com/sp00nznet/crazytaxi) | Static recompilation of Crazy Taxi from the Dreamcast SH-4 binary to native PC | 7 | 🟢 | Python |
| [crimsonskies (Crimson Skies)](https://github.com/sp00nznet/crimsonskies) | Static recompilation of Crimson Skies (PC, 2000) to native modern Windows | 7 | 🟢 | C |
| [dariusburst-vita (Darius Burst)](https://github.com/Rinnegatamante/dariusburst-vita) | PS Vita port of DARIUSBURST SP via the Android version loader | 7 | 🟢 | C |
| [DBZ-Budokai-1-HD-Collection](https://github.com/novapowers0/DBZ-Budokai-1-HD-Collection) | Recompilation of Dragon Ball Z: Budokai HD (Xbox 360) with ReXGlue | 7 | 🟢 | C++ |
| [destruction-derby-2-recomp](https://github.com/alexbeavs-ps1-ports/destruction-derby-2-recomp) | Static recompilation setup for Destruction Derby 2 (PS1) | 7 | 🟢 | Python |
| [destruction-derby-raw-recomp](https://github.com/alexbeavs-ps1-ports/destruction-derby-raw-recomp) | Static recompilation of Destruction Derby Raw (PS1) | 7 | 🟢 | Python |
| [diddykongracing (Diddy Kong Racing)](https://github.com/sp00nznet/diddykongracing) | Static recompilation of Diddy Kong Racing (N64) for Windows using N64Recomp | 7 | 🟢 | C++ |
| [digdug-native (Dig Dug)](https://github.com/TekRantGaming/digdug-native) | Native Windows and Linux port of Namco's Dig Dug arcade game (bring your own ROMs) | 7 | 🟢 | C# |
| [fc3-nx](https://github.com/barbaruiva25/fc3-nx) | Far Cry 3 (Xbox 360) statically recompiled with ReXGlue for Nintendo Switch | 7 | 🟢 | C |
| [future-cop-lapd-recomp](https://github.com/alexbeavs-ps1-ports/future-cop-lapd-recomp) | Static recompilation of Future Cop: L.A.P.D. (PS1) | 7 | 🟢 | Python |
| [haze-recomp](https://github.com/zdiemer/haze-recomp) | Experimental native Windows port of Haze (PS3) using ps3recomp | 7 | 🟢 | C++ |
| [JerseyDevilRecomp (Jersey Devil)](https://github.com/mstan/JerseyDevilRecomp) | Static recompilation of Jersey Devil (PS1) with psxrecomp | 7 | 🟢 | C |
| [JUSDecomp (Jump Ultimate Stars)](https://github.com/piuzera/JUSDecomp) | Static recompilation of Jump Ultimate Stars (Nintendo DS) | 7 | 🟢 | Assembly |
| [koudelka-recomp (Koudelka)](https://github.com/alexbeavs-ps1-ports/koudelka-recomp) | Static recompilation setup for Koudelka (PS1) | 7 | 🟢 | Python |
| [Lord of the Rings; The Third Age](https://github.com/Revan67/ThirdAge-Recomp) | Static recompilation of Lord of the Rings; The Third Age (Xbox) into a native PC port | 7 | 🟢 | C |
| [MacioGalaxy](https://github.com/classicrob/MacioGalaxy) | Native macOS port of Super Mario Galaxy built on the Petari decompilation | 7 | 🟢 | C++ |
| [mega-man-legends-2-recomp](https://github.com/alexbeavs-ps1-ports/mega-man-legends-2-recomp) | Static recompilation of Mega Man Legends 2 (PS1) | 7 | 🟢 | Python |
| [MOHFrontline-GC-RECOMP](https://github.com/ant0-blase/MOHFrontline-GC-RECOMP) | Static recompilation of Medal of Honor: Frontline (GameCube) | 7 | 🗄️ | C++ |
| [mtm (Monster Truck Madness)](https://github.com/sp00nznet/mtm) | Static recompilation of Monster Truck Madness 1 and 2 (PC) to native modern Windows | 7 | 🟢 | C |
| [Outpost Kaloki X](https://github.com/TekRantGaming/outpost-kaloki-x-recompiled) | Static recompilation of Outpost Kaloki X (Xbox 360) into a native PC port | 7 | 🟢 | C++ |
| [peggle2-mac](https://github.com/macprotips/peggle2-mac) | Native macOS port of Peggle 2 (Xbox 360) via static recompilation | 7 | 🟢 | C++ |
| [pret decompilation decomp](https://github.com/dnllnoe/pokeemerald-ps2) | Pokémon Emerald on PlayStation 2, a port of the pret decompilation | 7 | 🟢 | C |
| [pvz-console-edition](https://github.com/ITSeniy/pvz-console-edition) | Unofficial Windows port of Plants vs. Zombies (Xbox 360), statically recompiled with ReXGlue | 7 | 🟢 | C++ |
| [Sexy Parodius](https://github.com/NJH-1001/SexyParoRecomp) | Static recompilation of Sexy Parodius (PS1) into a native PC port | 7 | 🟢 | CMake |
| [SHO-GTA-VCS-PS2Recomp](https://github.com/BlackLineInteractive/SHO-GTA-VCS-PS2Recomp) | Playstation 2 Static Recompiler Silent Hill Origins & GTA Vice City Stories | 7 | 🗄️ | C++ |
| [sin-punishment-recompiled](https://github.com/maximilianoide/sin-punishment-recompiled) | Native PC port of Sin and Punishment (N64) via N64Recomp and RT64 | 7 | 🟢 | C++ |
| [StarWars-RenegadeSquadron-PC](https://github.com/GTTeancum/StarWars-RenegadeSquadron-PC) | Native Windows port of Star Wars Battlefront: Renegade Squadron (PSP) via static recompilation | 7 | 🟢 | C++ |
| [Super Smash Bros. Melee based on the decompilation port](https://github.com/sonsegajp/YAMPP) | Native PC port of Super Smash Bros. Melee based on the decompilation | 7 | 🟢 | C++ |
| [themepark-recomp](https://github.com/sp00nznet/themepark-recomp) | Static recompilation of Bullfrog's Theme Park (DOS) to native Windows with pcrecomp | 7 | 🟢 | C |
| [tiberiansun-recomp](https://github.com/sp00nznet/tiberiansun-recomp) | Static recompilation of Command & Conquer: Tiberian Sun and Firestorm | 7 | 🟢 | C |
| [tribespad (Tribes 2)](https://github.com/chrissotraidis/tribespad) | Tribes 2 on iPad, iPhone and Mac, with the x86 game code translated ahead of time to ARM | 7 | 🟢 | Python |
| [twilight-princess-hd-recomp](https://github.com/AsadSi/twilight-princess-hd-recomp) | Twilight Princess HD (Wii U) statically recompiled for Apple Silicon macOS | 7 | 🟢 | C++ |
| [Unwiished-Recomp (Sonic Unleashed Wii)](https://github.com/K-r0zen/Unwiished-Recomp) | Unofficial native PC port of the Wii version of Sonic Unleashed via static recompilation | 7 | 🟢 | C++ |
| [WaveRace64Recompiled](https://github.com/chronic8000/WaveRace64Recompiled) | Native Wave Race 64 port via static recompilation, no game assets included | 7 | 🟢 | C++ |
| [WiiCompiled-Switch](https://github.com/yashin-sh/WiiCompiled-Switch) | Experimental native Nintendo Switch port of WiiCompiled, with GX capture/replay and GPU diagnostics. Recognizable gam... | 7 | 🟢 | C++ |
| [WiiCompiled-Xbox-UWP](https://github.com/itzjuan612/WiiCompiled-Xbox-UWP) | Xbox Series / UWP port of WiiCompiled - a Mario Kart Wii static recompilation with a Dawn/D3D12 renderer | 7 | 🟢 | C++ |
| [wwe2k14-recomp (mikeflare007)](https://github.com/mikeflare007/wwe2k14-recomp) | Unofficial native PC port of WWE 2K14 (Xbox 360) by static recompilation | 7 | 🟢 | C++ |
| [007 recomp](https://github.com/furqanagwan/007) | Xbox 360 James Bond games statically recompiled for Windows with ReXGlue | 6 | 🟢 | PowerShell |
| [adam](https://github.com/evaa-01/adam) | Static recompilation of Neon Genesis Evangelion (N64) into a native Windows program | 6 | 🟢 | C++ |
| [Apocalypse](https://github.com/alexbeavs-ps1-ports/apocalypse-recomp) | Static recompilation of Apocalypse (PS1) into a native PC port | 6 | 🟢 | Python |
| [AstraRecomp](https://github.com/mirou1611/AstraRecomp) | PC-assisted PS2 static recompilation research targeting the PS Vita | 6 | 🟢 | C++ |
| [bar-recomp (Beetle Adventure Racing)](https://github.com/synamaxmusic/bar-recomp) | Static recompilation of Beetle Adventure Racing (N64) | 6 | 🟢 |  |
| [Burnout](https://github.com/Heromachine/Burnout-Recompilation) | Static recompilation of Burnout (Xbox) into a native PC port | 6 | 🟢 | C++ |
| [caesar2-reconstruction](https://github.com/second-impressions/caesar2-reconstruction) | Clean-room reconstruction of Caesar II. | 6 | 🟢 | C |
| [castlevania-ii-snes](https://github.com/rumbleminze/castlevania-ii-snes) | SNES port of the NES game Castlevania II: Simon's Quest | 6 | 🟢 | Assembly |
| [Daytona-USA-Web](https://github.com/johannruiz/Daytona-USA-Web) | Browser port of Daytona USA based on daytona-arcade-recomp, using WebAssembly and WebGPU | 6 | 🟢 | JavaScript |
| [dbz-budokai-hd (PS3)](https://github.com/gnome41/dbz-budokai-hd) | Static recompilation of Dragon Ball Z: Budokai HD (PS3) to native Windows | 6 | 🟢 | C++ |
| [DK64Recomp-NX](https://github.com/Trinalord777/DK64Recomp-NX) | Donkey Kong 64 (N64) static recompilation for Nintendo Switch with GLideN64 | 6 | 🟢 | C |
| [dmc-recomp (Devil May Cry)](https://github.com/Gui-Tora/dmc-recomp) | Experimental static recompilation of Devil May Cry (PS2) via PS2Recomp | 6 | 🟢 | Python |
| [FightersRecomp](https://github.com/Rayz0rum/FightersRecomp) | Sonic the Fighters (XBLA) recompiled on ReXGlue with path tracing | 6 | 🟢 | C++ |
| [FNAF1-Recomp-proj](https://github.com/Sergey004/FNAF1-Recomp-proj) | Experimental C++ reconstruction and recompilation of Five Nights at Freddy's 1-4 | 6 | 🟢 | C++ |
| [genrecomp](https://github.com/sp00nznet/genrecomp) | Toolkit to statically recompile Sega Genesis / Mega Drive (68000) games to native code | 6 | 🟢 | C |
| [ghost-in-the-shell-recomp](https://github.com/alexbeavs-ps1-ports/ghost-in-the-shell-recomp) | Static recompilation setup for Ghost in the Shell (PS1) | 6 | 🟢 | Python |
| [GT5P (Gran Turismo 5 Prologue)](https://github.com/sp00nznet/GT5P) | Static recompilation of Gran Turismo 5 Prologue (PS3) to native x86-64 with ps3recomp | 6 | 🟢 | C++ |
| [Gundam SEED: Battle Assault](https://github.com/omegakatana92/Gundam-Seed-Battle-Assault-Recomp) | Static recompilation of Gundam SEED: Battle Assault (GBA) into a native PC port | 6 | 🟢 | C++ |
| [harvest-moon-64-recompiled](https://github.com/ai-tdd-labs/harvest-moon-64-recompiled) | Work-in-progress PC port of Harvest Moon 64 via recompilation | 6 | 🟢 | C++ |
| [HarvestMoon64-Recomp](https://github.com/Rainchus/HarvestMoon64-Recomp) | Static recompilation of Harvest Moon 64 (N64) | 6 | 🟢 | C++ |
| [Hellnight-Recompiled](https://github.com/goodshepherd23/Hellnight-Recompiled) | Native PC build of Hell Night (PS1) via PSXRecomp static recompilation | 6 | 🟢 | Python |
| [in-cold-blood-recomp (In Cold Blood)](https://github.com/alexbeavs-ps1-ports/in-cold-blood-recomp) | Static recompilation setup for In Cold Blood (PS1) | 6 | 🟢 | Python |
| [Jet-Force-Capricorn](https://github.com/riseio/Jet-Force-Capricorn) | Static recompilation of Jet Force Gemini (N64) | 6 | 🟢 | C++ |
| [jumping-flash-collection](https://github.com/BluePointDigital/jumping-flash-collection) | Native recompilation of Jumping Flash! 1, 2 and Robbit Mon Dieu (PS1) | 6 | 🟢 | Python |
| [Lufia2SNESRecomp](https://github.com/Cellenseres/Lufia2SNESRecomp) | Static recompilation of Lufia II (SNES) | 6 | 🟢 | C |
| [mariokartdd-recomp](https://github.com/ethannicholas/mariokartdd-recomp) | Recompilation of Mario Kart: Double Dash (GameCube) | 6 | 🟢 | C++ |
| [Metal Slug X (Metal Slug X Recompiled)](https://github.com/TechnicallyComputers/Metal-Slug-X-Recomp) | Static recompilation of Metal Slug X (PS1) into a native PC port | 6 | 🟢 | C |
| [MLBPowerPros2008Recomp](https://github.com/HopeAero/MLBPowerPros2008Recomp) | Native recompilation of MLB Power Pros 2008 (Wii) on Wiicompiled | 6 | 🟢 | Python |
| [mpatrol (Moon Patrol)](https://github.com/jotd666/mpatrol) | Amiga port of the Moon Patrol arcade game, transcoded from the original code | 6 | 🟢 | C |
| [MTR-GWRE2 (Geometry Wars)](https://github.com/MissingThePixel/MTR-GWRE2) | Recompilation of Geometry Wars: Retro Evolved 2 (Xbox 360) | 6 | 🟢 | Java |
| [MusashiRecomp](https://github.com/saironbusatto/MusashiRecomp) | Static recompilation of Brave Fencer Musashi (PS1) | 6 | 🟢 | C++ |
| [naughtybear-restuff-android](https://github.com/deivid22srk/naughtybear-restuff-android) | Android port of Naughty Bear (Xbox 360) via ReXGlue static recompilation | 6 | 🟢 | C++ |
| [NumWorks-Super-Mario-64](https://github.com/Mason363/NumWorks-Super-Mario-64) | Super Mario 64 on the NumWorks calculator from the n64decomp decompilation | 6 | 🟢 | C |
| [PaRappaTheRapper](https://github.com/kirby1237/PaRappaTheRapperRecomp) | Static recompilation of PaRappaTheRapper (PS1) into a native PC port | 6 | 🟢 | C |
| [PaxDino](https://github.com/wootbeer/PaxDino) | Turok: Rage Wars recompilation and modern PC port | 6 | 🟢 | C++ |
| [pop2-port](https://github.com/dmucli/pop2-port) | Native port of the 1993 Macintosh Prince of Persia 2 for macOS, Linux and handhelds | 6 | 🟢 | C |
| [PS5_EternalDarkness](https://github.com/griches/PS5_EternalDarkness) | Eternal Darkness on PS5 homebrew, built from Eternal Darkness Recomp | 6 | 🟢 | C |
| [rexauto](https://github.com/Player124413/rexauto) | Desktop app and pipeline that turns an Xbox 360 game container into a recompiled PC build | 6 | 🟢 | Python |
| [Samurai Shodown: Warriors Rage](https://github.com/omegakatana92/Samuai-Shodown-Warriors-Rage-Recomp) | Static recompilation of Samurai Shodown: Warriors Rage (PS1) into a native PC port | 6 | 🟢 | Shell |
| [SD Gundam Dimension War Recomp](https://github.com/mstan/SDGundamDimensionWarVirtualBoyRecomp) | Static recompilation of SD Gundam Dimension War (Virtual Boy) | 6 | 🟢 | Python |
| [Skate3VR](https://github.com/whachuvr/Skate3VR) | Native VR port of EA's Skate 3 | 6 | 🟢 | C++ |
| [skybreak (The Legend of Zelda: Skyward Sword)](https://github.com/Kyra422/skybreak) | Unofficial native port of The Legend of Zelda: Skyward Sword (Wii) | 6 | 🟢 |  |
| [Sonic-Generations-Recomp](https://github.com/Player124413/Sonic-Generations-Recomp) | PC and Android recompilation of Sonic Generations (Xbox 360) with XenonRecomp | 6 | 🟢 | C++ |
| [sonic-the-fighters-pc](https://github.com/GoGurtPrime/sonic-the-fighters-pc) | ReXGlue-based build of the Xbox Live Arcade Sonic the Fighters for PC | 6 | 🟢 | CMake |
| [SonicBlastGGRecomp (Sonic Blast)](https://github.com/mstan/SonicBlastGGRecomp) | Static recompilation of Sonic Blast (Game Gear) | 6 | 🟢 | PowerShell |
| [spider-man-2-enter-electro-recomp](https://github.com/alexbeavs-ps1-ports/spider-man-2-enter-electro-recomp) | Static recompilation of Spider-Man 2: Enter Electro (PS1) | 6 | 🟢 | Python |
| [Spider-Man-2-PS2-Recomp](https://github.com/saltyboosack-blip/Spider-Man-2-PS2-Recomp) | Open-source PS2 recompilation research checkpoint for Spider-Man 2 (USA), no rom included. | 6 | 🟢 | C++ |
| [SSX-Tricky-PC](https://github.com/MatiasRiveraC/SSX-Tricky-PC) | Unofficial native PC port of SSX Tricky (Xbox), statically recompiled with xboxrecomp | 6 | 🟢 | C |
| [Star Wars: Masters of Teräs Käsi (MastersOfTerasKasiRecomp)](https://github.com/TechnicallyComputers/MastersOfTerasKasiRecomp) | Static recompilation of Star Wars: Masters of Teräs Käsi (PS1) into a native PC port | 6 | 🟢 | C |
| [Star-Fox-64-X](https://github.com/Team-Resurgent/Star-Fox-64-X) | Star Fox 64 port to the original Xbox from the N64 decompilation | 6 | 🟢 | C |
| [Suikoden](https://github.com/alexbeavs-ps1-ports/suikoden-recomp) | Static recompilation of Suikoden (PS1) into a native PC port | 6 | 🟢 | Python |
| [Super Mario Sunshine for Switch (sms-switch)](https://github.com/chasem-dev/sms-switch) | Super Mario Sunshine decomp-based PC port as Nintendo Switch homebrew (GameCube) | 6 | 🟢 | C++ |
| [Test Drive II](https://github.com/kylofon/test-drive-2-sdl3) | Open-source recomp of Test Drive II: The Duel. | 6 | 🟢 | C |
| [The Bigs 2](https://github.com/mdomangue26/thebigs2) | Static recompilation of The Bigs 2 (Xbox 360) into a native PC port | 6 | 🟢 | C++ |
| [tony-hawk-s-pro-skater-recomp](https://github.com/alexbeavs-ps1-ports/tony-hawk-s-pro-skater-recomp) | Static recompilation setup for Tony Hawk's Pro Skater (PS1) | 6 | 🟢 | Python |
| [vbrecomp](https://github.com/mstan/vbrecomp) | Static recompiler for Virtual Boy games | 6 | 🟢 | C |
| [Wipeout 3 Special Edition Recomp](https://github.com/mstan/Wipeout-3-Special-Edition-Recomp) | Static recompilation of Wipeout 3 Special Edition (PS1) with PSXrecomp | 6 | 🟢 | Python |
| [wreckless (Wreckless: The Yakuza Missions)](https://github.com/sp00nznet/wreckless) | Static recompilation of Wreckless: The Yakuza Missions (Xbox) | 6 | 🟢 | C |
| [xena-warrior-princess-recomp](https://github.com/alexbeavs-ps1-ports/xena-warrior-princess-recomp) | Static recompilation setup for Xena: Warrior Princess (PS1) | 6 | 🟢 | Python |
| [Aces of the Pacific](https://github.com/kylofon/aces-of-the-pacific-sdl3) | Recomp of Dynamix' Aces of the Pacific. | 5 | 🟢 | C |
| [AlbionRecomp (Fable 2)](https://github.com/OswaldNotOz/AlbionRecomp05_03_25) | Fable II (Xbox 360) recompilation project | 5 | 🟡 |  |
| [Alley Cat](https://github.com/petarov/alleycat.exe) | Static recompilation of Alley Cat (DOS) into a native PC port | 5 | 🟢 | C |
| [ANIMANIACS-GC-RECOMP](https://github.com/ant0-blase/ANIMANIACS-GC-RECOMP) | Animaniacs: The Great Edgar Hunt — GameCube Static Recompilation | 5 | 🗄️ | C++ |
| [ArmyOfTwo40thDayRecomp](https://github.com/crabinacrabic/ArmyOfTwo40thDayRecomp) | ReXGlue static recompilation of Army of Two: The 40th Day (Xbox 360) | 5 | 🟢 | C++ |
| [AvatarEditorRecomp](https://github.com/panedivitasei/AvatarEditorRecomp) | Static recompilation of the 2010 Xbox 360 Avatar Editor for PC | 5 | 🟢 | C++ |
| [Bubble-Bobble-NES-Static-Recomp](https://github.com/Junior-Jones/Bubble-Bobble-NES-Static-Recomp) | Static recompilation of Bubble Bobble (NES) for Windows | 5 | 🟢 | C |
| [Captain-America-Super-Soldier-Recompiled](https://github.com/m1ndcrap/Captain-America-Super-Soldier-Recompiled) | Recompilation of Captain America: Super Soldier (Xbox 360) with ReXGlue | 5 | 🟢 | CMake |
| [comixzone (Comix Zone)](https://github.com/sp00nznet/comixzone) | Static recompilation of Comix Zone (Xbox 360 XBLA) to native PC | 5 | 🟢 | C++ |
| [cosmo (Cosmo's Cosmic Adventure)](https://github.com/digows/cosmo) | Native source port of Cosmo's Cosmic Adventure (Apogee, 1992) | 5 | 🟢 | C |
| [ddg-recomp](https://github.com/resterle/ddg-recomp) | Static recompilation of Densha de Go! Final (PS2) | 5 | 🟢 | C++ |
| [DOA3 (Android)](https://github.com/Wannamingo/DOA3) | Unofficial native Android port of Dead or Alive 3 (Xbox) | 5 | 🟢 | C |
| [extremeg (Extreme-G)](https://github.com/sp00nznet/extremeg) | Static recompilation of Extreme-G (N64, 1998) to native PC | 5 | 🟢 | C++ |
| [fm4-recomp (Forza Motorsport 4)](https://github.com/GabrielCRadu/fm4-recomp) | Native 64-bit Windows static recompilation of Forza Motorsport 4 (Xbox 360) | 5 | 🟢 | C++ |
| [gh2 (Guitar Hero II)](https://github.com/sp00nznet/gh2) | Static recompilation of Guitar Hero II (Xbox 360) to native Windows | 5 | 🟢 | Python |
| [hl2-recomp (Half-Life 2 Xbox)](https://github.com/sp00nznet/hl2-recomp) | Static recompilation of Half-Life 2 (Xbox, 2005) to native Windows | 5 | 🟢 | C |
| [HotelMarioRecomp (Hotel Mario)](https://github.com/mstan/HotelMarioRecomp) | Static recompilation of Hotel Mario (Philips CD-i) | 5 | 🟢 | PowerShell |
| [imabikisou-pc](https://github.com/yasindevs/imabikisou-pc) | Experimental Imabikisou PS3-to-PC recompilation using ps3recomp | 5 | 🟢 | C++ |
| [jojo-hftf-native](https://github.com/MenuuTUX/jojo-hftf-native) | Native macOS port of JoJo's Bizarre Adventure: Heritage for the Future (PS1) | 5 | 🟢 | C |
| [KnowYourRoleRecomp](https://github.com/Comfubar/KnowYourRoleRecomp) | WWF SmackDown! 2 PlayStation static recompilation | 5 | 🟢 | C# |
| [L4D-PC-Recomp (Left 4 Dead)](https://github.com/KeithKirenai/L4D-PC-Recomp) | Left 4 Dead (Xbox 360) static recompilation runtime for PC with XenonRecomp | 5 | 🟢 | C++ |
| [Libre40 (Army of Two: The 40th Day)](https://github.com/automoto/Libre40) | Recompilation and preservation project for Army of Two: The 40th Day (Xbox 360) | 5 | 🟢 | Python |
| [LineWars II SDL](https://github.com/fredangstadt-lang/LineWarsII-SDL) | SDL3 backend for a portable-C reconstruction of the 1994 DOS game LineWars II | 5 | 🟢 | C |
| [luigismansion (Luigi's Mansion)](https://github.com/sp00nznet/luigismansion) | Static recompilation of Luigi's Mansion (GameCube) to native PC | 5 | 🟢 | C++ |
| [megarocket (Commander Keen)](https://github.com/CrossplayGaming/megarocket) | All seven Commander Keen games in one native app for Windows and Android | 5 | 🟢 | GDScript |
| [metal-slug-x-recomp](https://github.com/AlmazProud/metal-slug-x-recomp) | Native Windows port of Metal Slug X (Neo Geo) by static 68000 recompilation | 5 | 🟢 | C |
| [minigore2-native-arm](https://github.com/EapRules/minigore2-native-arm) | Minigore 2: Zombies running natively on Linux ARM handhelds through an Android ELF loader | 5 | 🟢 | C++ |
| [oot-recompiled](https://github.com/JonB-Dev/oot-recompiled) | Static recompilation of Ocarina of Time into a native Windows executable | 5 | 🟢 | C++ |
| [p3fes-recompiled](https://github.com/poopoocacacacaca/p3fes-recompiled) | AI-assisted static recompilation of Persona 3 FES (PS2, USA) | 5 | 🟢 | C++ |
| [PacmanRecomp](https://github.com/Wilson-Flores/PacmanRecomp) | Static recompilation of the original Pac-Man arcade game for Windows, Linux and Mac | 5 | 🟢 | C++ |
| [pc-virtualhydlide](https://github.com/vs-sr-dev/pc-virtualhydlide) | Work toward a native PC port of Virtual Hydlide (Saturn) with its programs recompiled to C++ | 5 | 🟢 | Python |
| [peggle360-decomp](https://github.com/JosueMora918/peggle360-decomp) | ReXGlue static recompilation of Peggle (Xbox 360 XBLA) | 5 | 🟢 | CMake |
| [pokemon](https://github.com/sp00nznet/pokemon) | Generation I Pokémon (Red/Blue/Yellow) statically recompiled to native C — no emulator at runtime. Plus a headless bu... | 5 | 🟢 | Python |
| [project-petunia (Kid Icarus)](https://github.com/rumbleminze/project-petunia) | SNES port of the NES game Kid Icarus | 5 | 🟡 | Assembly |
| [ProvingGroundRecomp](https://github.com/SunJaycy/ProvingGroundRecomp) | Recompilation of Tony Hawk's Proving Ground (Xbox 360) | 5 | 🟢 | CMake |
| [ps2-recompiler](https://github.com/InconspicuousCactus/ps2-recompiler) | Experimental tool to recompile PS2 games to run natively on PC | 5 | 🟡 | C |
| [Rampage (N64)](https://github.com/sp00nznet/Rampage) | Native Windows ports of Rampage: World Tour and Rampage 2 (N64) via static recompilation | 5 | 🟢 | C++ |
| [RockmanDash-Recompiled](https://github.com/Rainchus/RockmanDash-Recompiled) | Static recompilation of Rockman Dash (Mega Man Legends, PS1) | 5 | 🟡 | C++ |
| [rushrecomp](https://github.com/Tekkra-Pi/rushrecomp) | Static recompilation of Sonic Rush (DS) with an ndsrecomp ARM/Thumb-to-C pipeline | 5 | 🟢 | C |
| [sf2 (Street Fighter II)](https://github.com/sp00nznet/sf2) | Static recompilation of Street Fighter II from the CPS1 arcade board to native PC | 5 | 🟢 | C |
| [sfrush (San Francisco Rush)](https://github.com/sp00nznet/sfrush) | Static recompilation of San Francisco Rush: Extreme Racing (N64) for PC | 5 | 🟢 | JavaScript |
| [SimCity-SNES-Static-Recomp](https://github.com/Junior-Jones/SimCity-SNES-Static-Recomp) | Static recompilation of SimCity (SNES) for Windows | 5 | 🟢 | C |
| [SMG-3DS](https://github.com/cmyksoda/SMG-3DS) | Unfinished New 3DS port of Super Mario Galaxy based on the Petari decompilation | 5 | 🗄️ | C++ |
| [SuperBomberman5SNESRecomp](https://github.com/MauricioSuporte/SuperBomberman5SNESRecomp) | Super Bomberman 5 (SNES) Windows prototype using SNESRecomp | 5 | 🟢 | C |
| [Tekken3-PC](https://github.com/Muqaddas12/Tekken3-PC) | Native static recompilation PC port of Tekken 3 (PS1) | 5 | 🟢 | Python |
| [tetris (Atari Tetris)](https://github.com/jotd666/tetris) | Transcode of the Atari Tetris arcade game to 68000 for the Amiga | 5 | 🟢 | C |
| [TLKRecomp](https://github.com/kinduff/TLKRecomp) | Static recompilation of The Lion King (SNES) with snesrecomp | 5 | 🟢 | C |
| [VivaPinataRecomp (org)](https://github.com/VivaPinataRecomp/VivaPinataRecomp) | Recompilation project for Viva Piñata (Xbox 360) | 5 | 🟡 | Python |
| [Woody-Portable](https://github.com/wendersondiazx/Woody-Portable) | Native PSP port of Woody Woodpecker: Escape from Buzz Buzzard Park | 5 | 🟢 | C++ |
| [WWF No Mercy for Meta Quest 3](https://github.com/VistaLargaGames/WWF-No-Mercy-Quest-3-Standalone-) | Standalone Meta Quest 3 port of the WWF No Mercy N64 recompilation (N64) | 5 | 🟢 |  |
| [xwa](https://github.com/sp00nznet/xwa) | A static recompilation of Star Wars: X-Wing Alliance (1999) by Totally Games / LucasArts, targeting modern Windows wi... | 5 | 🟢 | C |
| [CyberMage Modern](https://github.com/RoninSan369/CyberMageModern) | Recomp of the DOS game CyberMage. | 4 | 🟢 |  |
| [Digimon World 2003 port](https://github.com/Feerdus95/dw3-native-port) | Native PC port of Digimon World 2003 (PS1) built from the dw3_decomp code | 4 | 🟢 | C |
| [GoldenEye 007 based on the N64 decompilation port](https://github.com/kylebrussell/goldeneye-3ds) | Native Nintendo 3DS port of GoldenEye 007 based on the N64 decompilation | 4 | 🟢 | C |
| [kf1-enhanced](https://github.com/Acranon/kf1-enhanced) | Enhanced native PC port of King's Field based on reverse engineering | 4 | 🟢 | C++ |
| [Kirby 64: The Crystal Shards port](https://github.com/JR3DFUL/HALBERD) | PC port of Kirby 64: The Crystal Shards built on the decompilation | 4 | 🟢 | C |
| [LEGOLAND port](https://github.com/facundosterzerforino/legoland-port) | Native Windows 11 port of LEGOLAND (1999) built from its matching decompilation | 4 | 🟢 | C |
| [MarioGolf64](https://github.com/Rainchus/MarioGolf64) | MarioGolf64 | 4 | 🟢 | Python |
| [Perfect Dark decompilation port](https://github.com/Mr4xd3mn/perfect-dark-android) | Native Android port of the Perfect Dark decompilation (N64) | 4 | 🟢 | C |
| [Pokémon Black 2 and White 2 port](https://github.com/CallanCampos/Frigate) | Native PC and Mac port of Pokémon Black 2 and White 2 built from the decompilation | 4 | 🟢 | C |
| [The New Tetris decomp](https://github.com/chris-gilmore/tnt-allegro) | Linux port of The New Tetris (N64) based on its decompilation | 4 | 🟢 | C |
| [Vigilante 8 port](https://github.com/psxports/Vigilante8-xport) | PC port of Vigilante 8 (PS1) built from a decompilation | 4 | 🟢 | C |
| [Bak-Again](https://github.com/stellargames/bakagain) | Recomp + enhancement of Betrayal At Krondor by Dynamix. | 3 | 🟢 | C# |
| [F-19](https://github.com/xor2003/f19re) | Recomp of MicroProse F-19. | 3 | 🟢 | Assembly |
| [Gunboat](https://github.com/PlasticCog/Gunboat) | Open-source recomp of the game Gunboat. | 3 | 🟢 | C++ |
| [Metal Mutant-web](https://github.com/kznsq/metal-mutant-web) | Recomp of the Silmarils game Metal Mutant to Javascript. | 3 | 🟢 | JavaScript |
| [Overboard! / Shipwreckers! port](https://github.com/psxports/Overboard-xport) | PC port of Overboard! / Shipwreckers! (PS1) built from a decompilation | 3 | 🟢 | C |
| [Pandemonium 2 port](https://github.com/psxports/Pandemonium2-xport) | PC port of Pandemonium 2 (PS1) built from a decompilation | 3 | 🟢 | C++ |
| [Syphon Filter port](https://github.com/psxports/SyphonFilter-xport) | PC port of Syphon Filter (PS1) built from a decompilation | 3 | 🟢 | C |
| [Agent Armstrong port](https://github.com/psxports/AgentArmstrong-xport) | PC port of Agent Armstrong (PS1) built from a decompilation | 2 | 🟢 | C |
| [Crash Bandicoot port](https://github.com/khasinski/crash-bandicoot-pc) | Native PC port of Crash Bandicoot (PS1) built on the matching decompilation | 2 | 🟢 | C |
| [Need decomp](https://github.com/pablonolascoo/nfs-mw-2005-ps2-port) | Decompilation and native port of Need for Speed: Most Wanted (2005, PS2) | 2 | 🟢 | Swift |
| [Twisted Metal 3 port](https://github.com/psxports/TwistedMetal3-xport) | PC port of Twisted Metal 3 (PS1) built from a decompilation | 2 | 🟢 | C |
| [win-port](https://github.com/OpenCol/win-port) | Port of Sid Meier's Colonization (Windows 3.1) built from a byte-accurate decompilation | 2 | 🟢 | C |
| [Ace Combat 3: Electrosphere port](https://github.com/psxports/AceCombat3-xport) | PC port of Ace Combat 3: Electrosphere (PS1) built from a decompilation | 1 | 🟢 | C |
| [Airborn Ranger](https://github.com/xor2003/airborn-ranger) | Recomp of Airborn Ranger by MicroProse. | 1 | 🟢 | C |
| [Apocalypse port](https://github.com/psxports/Apocalypse-xport) | PC port of Apocalypse (PS1) built from a decompilation | 1 | 🟢 | C++ |
| [Diddy Kong Racing port](https://github.com/RyoSaeba89/DKR-GC) | Native GameCube port of Diddy Kong Racing built on the N64 decompilation | 1 | 🟢 | C |
| [Fighting Force port](https://github.com/psxports/FightingForce-xport) | PC port of Fighting Force (PS1) built from a decompilation | 1 | 🟢 | C |
| [Rapid Racer port](https://github.com/psxports/RapidRacer-xport) | PC port of Rapid Racer (PS1) built from a decompilation | 1 | 🟢 | C |
| [SSX on Tour (ssx-on-tour-psp-recomp)](https://github.com/highcmd/ssx-on-tour-psp-recomp) | Static recompilation of SSX on Tour (GameCube) into a native PC port | 1 | 🟢 | C++ |
| [Vette](https://github.com/PlasticCog/Vette2026) | Recomp of the game Vette by Spectrum Holobyte. | 1 | 🟢 | C++ |
| [Auto Destruct port](https://github.com/psxports/AutoDestruct-xport) | PC port of Auto Destruct (PS1) built from a decompilation | 0 | 🟢 | C |
| [Demolition Racer port](https://github.com/psxports/DemolitionRacer-xport) | PC port of Demolition Racer (PS1) built from a decompilation | 0 | 🟢 | C |
| [DNZHRecomp](https://gitlab.com/sonicdcer/DNZHRecomp) | DNZHRecomp |  | ⚪ |  |
| [Extreme-G: Recompiled](https://gitlab.com/sonicdcer/ExtremeGRecomp) | Extreme-G N64 static recompilation |  | ⚪ |  |
| [Mad TV online](https://madtvgame-tribute.com) | Recomp and enhancement/fixes to the German DOS game Mad TV. No github available yet, but playable online. Mad TV is a... |  | ⚪ |  |
| [Magic-Carpet-port](https://github.com/jessperler88/Magic-Carpet-port) | Bullfrog's Magic Carpet (1994) decompiled and ported to native Windows x64 | 0 | 🟢 | C++ |
| [MarioKart64Recomp](https://gitlab.com/sonicdcer/MarioKart64Recomp) | MarioKart64Recomp |  | ⚪ |  |
| [MechWarrior decomp](https://github.com/Elthial/Mechwarrior-sdl-port) | SDL3 port of MechWarrior (1989) from decompiled sources | 0 | 🟢 | C |
| [Medal of Honor port](https://github.com/psxports/MedalOfHonor-xport) | PC port of Medal of Honor (PS1) built from a decompilation | 0 | 🟢 | C |
| [OpenCivOne (Civilization)](https://codeberg.org/rhorvat/OpenCivOne) | Preservation rewrite of Sid Meier's Civilization (DOS) based on the decompiled game |  | ⚪ |  |
| [Overblood port](https://github.com/psxports/OverBlood-xport) | PC port of Overblood (PS1) built from a decompilation | 0 | 🟢 | C |
| [Starfox64Recomp](https://gitlab.com/sonicdcer/Starfox64Recomp) | Starfox64Recomp |  | ⚪ |  |
| [Super Mario Bros. disassembly](https://github.com/ewanc26/smbc) | Native C port of Super Mario Bros. (NES) translated from its disassembly | 0 | 🟢 | C |
