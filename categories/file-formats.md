# File Formats

[← All categories](../README.md#whats-inside) · [Search this category on the website](https://alexgaoth.github.io/awesome-reverse-engineered/#c=file-formats) · 439 projects · [Listed here? Get the badge](../README.md#is-your-project-listed)

Health: 🟢 pushed in the last year · 🟡 1 to 3 years · 🔴 over 3 years · 🗄️ archived · ⚪ unknown

- [Audio & Music Production](#audio--music-production) (40)
- [Camera RAW & Video Metadata](#camera-raw--video-metadata) (25)
- [Databases](#databases) (27)
- [Design Tools (PSD, Sketch, Figma, Affinity)](#design-tools-psd-sketch-figma-affinity) (21)
- [E-books](#e-books) (9)
- [EDA & PCB](#eda--pcb) (13)
- [Filesystems & Archives](#filesystems--archives) (48)
- [Format Description Tools](#format-description-tools) (24)
- [Graphics & CAD](#graphics--cad) (52)
- [Maps & GIS](#maps--gis) (19)
- [Media Codecs & Containers](#media-codecs--containers) (9)
- [Office & Documents](#office--documents) (76)
- [Other](#other) (7)
- [Windows & Forensic Artifacts](#windows--forensic-artifacts) (69)

## Audio & Music Production

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [alphaTab](https://github.com/CoderLine/alphaTab) | Music notation and tab rendering library that imports Guitar Pro 3-8 files | 1,881 | 🟢 | TypeScript |
| [TuxGuitar](https://github.com/helge17/tuxguitar) | Open-source tablature editor with Guitar Pro and Power Tab importers | 1,584 | 🟢 | Java |
| [Power Tab Editor](https://github.com/powertab/powertabeditor) | Guitar tablature editor that imports Power Tab and Guitar Pro files | 635 | 🟢 | C++ |
| [PyGuitarPro](https://github.com/Perlence/PyGuitarPro) | Reads, writes and manipulates Guitar Pro GP3/GP4/GP5 tablature files | 371 | 🟢 | Python |
| [Crate Digger](https://github.com/Deep-Symmetry/crate-digger) | Java library for parsing Pioneer rekordbox export databases and track analysis files | 236 | 🟢 | Java |
| [dawtool](https://github.com/offlinemark/dawtool) | Reverse engineered parsers for Ableton Live and FL Studio project files | 225 | 🟡 | Python |
| [PyFLP](https://github.com/demberto/PyFLP) | Parser and editor for FL Studio project (.flp) files | 219 | 🟢 | Python |
| [rekordcrate](https://github.com/Holzhaus/rekordcrate) | Rust library for parsing Pioneer rekordbox device exports | 215 | 🟢 | Rust |
| [Ruxguitar](https://github.com/agourlay/ruxguitar) | Guitar Pro tablature player written in Rust | 211 | 🟢 | Rust |
| [abletoolz](https://github.com/elixirbeats/abletoolz) | Tools for editing and analyzing Ableton Live sets | 128 | 🟢 | Python |
| [bitwig-nitro-tools](https://github.com/blakebratcher/bitwig-nitro-tools) | Offline toolchain for Bitwig Studio's Nitro DSP format | 99 | 🟢 | Python |
| [ptformat](https://github.com/zamaudio/ptformat) | Parser for Avid Pro Tools session files, used by Ardour for import | 95 | 🟢 | C++ |
| [serato-tags](https://github.com/Holzhaus/serato-tags) | Documentation and parsers for Serato DJ Pro GEOB metadata tags | 93 | 🔴 | Python |
| [parse-gp5](https://github.com/juliangruber/parse-gp5) | JavaScript parser for the Guitar Pro 5 file format | 65 | 🔴 | JavaScript |
| [BZRPlayer](https://github.com/bzr-player/bzr-player) | Audio player supporting many exotic multi-platform game and tracker music formats | 60 | 🟢 | C |
| [TraktorMappingFileFormat](https://github.com/ivanz/TraktorMappingFileFormat) | Reverse engineered Traktor Pro .tsi controller mapping file format | 57 | 🔴 |  |
| [GuitarPro-to-Midi](https://github.com/alexsteb/GuitarPro-to-Midi) | Converts Guitar Pro 3-7 files to MIDI, simulating bends and effects | 55 | 🟡 | C# |
| [guitarpro (Rust)](https://github.com/slundi/guitarpro) | Rust library to parse and write Guitar Pro files | 52 | 🟢 | Rust |
| [logic2ableton](https://github.com/Evilander/logic2ableton) | Converts Logic Pro .logicx projects to Ableton Live .als sets | 49 | 🟢 | Python |
| [gp-parser](https://github.com/dwursteisen/gp-parser) | Guitar Pro file parser | 45 | 🔴 | Java |
| [MPC Maid](https://github.com/cyriux/mpcmaid) | Editor for Akai MPC 1000/2500/500 program files and samples | 45 | 🔴 | Java |
| [nkxtract](https://github.com/maxton/nkxtract) | Extracts Native Instruments Kontakt NKX monolith sample containers | 31 | 🔴 | C# |
| [miragetools](https://github.com/gordonjcp/miragetools) | Tools and reverse-engineering documentation for the Ensoniq Mirage sampler | 30 | 🔴 | C |
| [musx2mxl](https://github.com/joris-vaneyghen/musx2mxl) | Converts Finale .musx scores to MusicXML | 29 | 🟡 | Python |
| [seratojs](https://github.com/bcollazo/seratojs) | Node.js library to manage Serato crates programmatically | 23 | 🟡 | JavaScript |
| [flp-viewer](https://github.com/RyanScottLewis/flp-viewer) | FL Studio FLP file format parser and viewer | 21 | 🔴 | Crystal |
| [serato-crater](https://github.com/Rickgg/serato-crater) | Reads Serato .crate files and returns columns and songs | 21 | 🔴 | JavaScript |
| [EpsLinNeo](https://github.com/handsthatstrike/EpsLinNeo) | File utility for Ensoniq EPS/ASR sampler disks and images | 18 | 🔴 | C |
| [Denigma](https://github.com/openmusx/denigma) | Converter that extracts and translates Finale .musx files to open formats | 11 | 🟢 | C++ |
| [logicx-analyzer](https://github.com/geoffmyers/logicx-analyzer) | Reverse-engineering toolkit for Logic Pro .logicx project bundles | 9 | 🟢 | Python |
| [libflp](https://github.com/codecat/libflp) | C library for parsing FL Studio .flp project files | 8 | 🔴 | C++ |
| [snd2wav](https://github.com/uliwitness/snd2wav) | Converts classic Mac OS 'snd ' resources and System 7 sound files to WAV | 8 | 🔴 | C++ |
| [python-serato-crates](https://github.com/stephanlensky/python-serato-crates) | Python library for reading and writing Serato DJ crates | 7 | 🟡 | Python |
| [sexypsf](https://github.com/CoreDumpling/sexypsf) | PlayStation Sound Format (PSF) player with unofficial patches | 7 | 🔴 | C |
| [biab-library](https://github.com/andreamust/biab-library) | Python library for opening Band-in-a-Box song files | 6 | 🟢 | C++ |
| [musxdom](https://github.com/openmusx/musxdom) | C++17 object model for the EnigmaXML data inside Finale .musx files | 6 | 🟢 | C++ |
| [AKAI-CD-ISO-MAKER](https://github.com/yuyoi/AKAI-CD-ISO-MAKER) | Builds, reads and exports Akai S1000/S2000/S3000 sampler CD images | 2 | 🟢 | Python |
| [Data::BiaB](https://github.com/sciurius/perl-Data-BiaB) | Perl module to analyse Band-in-a-Box data files | 1 | 🔴 | Perl |
| [cpr2rpp](https://github.com/daniel-lynch/cpr2rpp) | Converts Cubase .cpr projects to REAPER .RPP via a reverse-engineered project format | 0 | 🟢 | Python |
| [minymize](https://codeberg.org/jbqueru/minymize) | Handler for MaxYMiser .MYS/.MYV chiptune files, documenting their reverse-engineered format |  | ⚪ |  |

## Camera RAW & Video Metadata

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [ExifTool](https://github.com/exiftool/exiftool) | Metadata reader/writer with extensive reverse-engineered camera maker notes | 5,200 | 🟢 | Perl |
| [LibRaw](https://github.com/LibRaw/LibRaw) | Library for decoding RAW files from hundreds of digital camera models | 1,612 | 🟢 | C++ |
| [Exiv2](https://github.com/Exiv2/exiv2) | C++ image metadata library including proprietary maker note decoding | 1,168 | 🟢 | C++ |
| [dnglab](https://github.com/dnglab/dnglab) | Converts camera RAW files to DNG with its own reverse-engineered decoders (Rust) | 700 | 🟢 | Rust |
| [rawspeed](https://github.com/darktable-org/rawspeed) | Fast camera RAW decoding library used by darktable | 461 | 🟢 | C++ |
| [MLV-App](https://github.com/ilia3101/MLV-App) | Processing app for Magic Lantern MLV raw video files | 352 | 🟢 | C++ |
| [canon_cr3](https://github.com/lclevy/canon_cr3) | Reverse-engineered description of the Canon CR3 RAW file format | 330 | 🟢 | Python |
| [gopro-utils](https://github.com/stilldavid/gopro-utils) | Tools to parse GPMF metadata from GoPro cameras | 255 | 🟡 | Go |
| [dji-log-parser](https://github.com/lvauvillier/dji-log-parser) | Rust library that parses records from DJI flight log .txt files | 124 | 🟡 | Rust |
| [thermal_parser](https://github.com/SanNianYiSi/thermal_parser) | Parser for FLIR and DJI infrared camera radiometric image data | 106 | 🟡 | Python |
| [x3f tools](https://github.com/Kalpanika/x3f) | Tools for decoding Sigma/Foveon X3F RAW files | 103 | 🟡 | C |
| [libcraw2](https://github.com/lclevy/libcraw2) | Minimal library that decodes Canon CR2 RAW files, with format notes | 102 | 🔴 | C |
| [pyavb](https://github.com/markreidvfx/pyavb) | Reads and writes Avid Media Composer bin (.avb) files | 77 | 🟡 | Python |
| [DJI_SRT_Parser](https://github.com/JuanIrache/DJI_SRT_Parser) | Parses telemetry from DJI drone SRT metadata files | 55 | 🟡 | JavaScript |
| [xavc_rtmd2srt](https://github.com/SK-Hardwired/xavc_rtmd2srt) | Extracts real-time metadata and GPS tracks from Sony XAVC video files | 48 | 🔴 | Python |
| [DatCon](https://github.com/BudWalkerJava/DatCon) | Converts DJI drone .DAT flight logs to CSV and KML | 32 | 🔴 | Java |
| [blackclue](https://github.com/gandy92/blackclue) | Extracts GPS and accelerometer data from BlackVue dashcam MP4 recordings | 18 | 🟡 | Python |
| [djiLogParser](https://github.com/shaofanqi/djiLogParser) | Python parser for DJI drone flight logs | 18 | 🔴 | Python |
| [nikon-flexible-color-picture-control](https://github.com/ssssota/nikon-flexible-color-picture-control) | Reads and writes Nikon Flexible Color Picture Control (NP3) files | 18 | 🟢 | TypeScript |
| [flighttrack](https://github.com/lvauvillier/flighttrack) | Simple viewer for DJI flight logs | 14 | 🔴 | JavaScript |
| [quicklook_d411](https://github.com/sheepdoll/quicklook_d411) | QuickLook plugin that previews Sony Mavica .411 thumbnail images | 4 | 🔴 | Objective-C |
| [insvtool](https://github.com/ke4ukz/insvtool) | Dumps metadata from Insta360 .insv video files | 1 | 🟢 | Python |
| [mavica_411_decoder](https://github.com/G2-Games/mavica_411_decoder) | Decodes Sony Mavica floppy-camera .411 thumbnail images | 1 | 🟡 | Rust |
| [dcraw](https://dechifro.org/dcraw/) | Decoder for raw photos from hundreds of digital cameras |  | ⚪ |  |
| [libopenraw](https://gitlab.freedesktop.org/libopenraw/libopenraw) | Library for decoding camera RAW files |  | ⚪ |  |

## Databases

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [pyreadstat](https://github.com/Roche/pyreadstat) | Python package to read/write SAS, SPSS and Stata files (wraps ReadStat) | 429 | 🟢 | C |
| [ReadStat](https://github.com/WizardMac/ReadStat) | C library and CLI for reading SAS, Stata and SPSS data files, including reverse-engineered SAS7BDAT | 309 | 🟢 | C |
| [dbf (Ruby)](https://github.com/infused/dbf) | Ruby library for reading dBase, xBase, Clipper and FoxPro DBF files | 281 | 🟢 | Ruby |
| [dbfread](https://github.com/olemb/dbfread) | Python library for reading dBase/FoxPro DBF files | 244 | 🟡 | Python |
| [OrcaMDF](https://github.com/improvedk/OrcaMDF) | C# parser that reads SQL Server MDF data files without SQL Server | 190 | 🔴 | C# |
| [Jackcess](https://github.com/jahlborn/jackcess) | Pure Java library for reading and writing Microsoft Access (.mdb/.accdb) databases | 122 | 🟢 | Java |
| [fmptools](https://github.com/evanmiller/fmptools) | Converts FileMaker Pro databases (.fp5/.fp7/.fmp12) to open formats | 107 | 🟢 | C |
| [dbf (Python)](https://github.com/ethanfurman/dbf) | Pure Python dBase/FoxPro DBF reader and writer | 102 | 🟡 | Python |
| [access_parser](https://github.com/claroty/access_parser) | Python parser for Microsoft Access database files | 93 | 🟡 | Python |
| [sas7bdat](https://github.com/BioStatMatt/sas7bdat) | The original reverse engineering of the SAS sas7bdat file format, with an R reader | 84 | 🗄️ | R |
| [tps-parse](https://github.com/ctrl-alt-dev/tps-parse) | Parses Clarion TopSpeed (.tps) database files and converts them to CSV | 83 | 🔴 | Java |
| [Parso](https://github.com/epam/parso) | Lightweight Java library for reading SAS7BDAT datasets | 80 | 🟢 | Java |
| [mdb-reader](https://github.com/andipaetzold/mdb-reader) | JavaScript library to read Microsoft Access databases | 66 | 🟢 | TypeScript |
| [pypxlib](https://github.com/mherrmann/pypxlib) | Python bindings for pxlib to read and write Paradox databases | 44 | 🔴 | Python |
| [pxtools](https://github.com/ustramooner/pxtools) | Converts Paradox databases to MySQL, PostgreSQL, CSV or XML | 34 | 🔴 | C |
| [go-ese](https://github.com/Velocidex/go-ese) | Go parser for the Microsoft Extensible Storage Engine (ESE/JET Blue) database | 32 | 🟢 | Go |
| [dissect.esedb](https://github.com/fox-it/dissect.esedb) | Python parser for Microsoft ESE (Extensible Storage Engine) databases | 24 | 🗄️ | Python |
| [PxView](https://github.com/CoolmanCZ/pxview) | GUI application to open and edit Paradox database files | 18 | 🟢 | C |
| [Paradox-Reader](https://github.com/kymuweb/Paradox-Reader) | Native .NET reader for Paradox database files | 13 | 🟢 | C# |
| [btrieve-vdd](https://github.com/leecher1337/btrieve-vdd) | Btrieve database virtual device driver for DOS virtual machines | 12 | 🔴 | C |
| [OpenQBW](https://github.com/Sigilweaver/OpenQBW) | Pure Rust reader for QuickBooks QBW company files, with Python bindings | 12 | 🟢 | Rust |
| [MBBSEmu.Btrieve](https://github.com/mbbsemu/MBBSEmu.Btrieve) | Reads and recovers data from Btrieve .DAT files into SQLite | 10 | 🟡 | C# |
| [wbtrv32](https://github.com/mbbsemu/wbtrv32) | Drop-in Btrieve v5/v6 driver replacement that stores data in SQLite | 10 | 🟢 | C |
| [sbdf](https://github.com/pod2co/sbdf) | Unofficial reader and writer for the Spotfire Binary Data Format (SBDF) | 3 | 🟡 | Rust |
| [unraveling_sql_server_bak](https://github.com/klandermans/unraveling_sql_server_bak) | Research and tooling for reading SQL Server .bak backup files without SQL Server | 2 | 🟡 |  |
| [JMPReader](https://github.com/BreakOnExecute/JMPReader) | Reads SAS JMP data files directly in Python | 1 | 🔴 | Python |
| [pxlib](https://sourceforge.net/projects/pxlib/) | Library for reading Borland Paradox database files |  | ⚪ |  |

## Design Tools (PSD, Sketch, Figma, Affinity)

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [psd.js](https://github.com/meltingice/psd.js) | Photoshop PSD parser for Node.js and browsers | 2,839 | 🟡 | CoffeeScript |
| [ag-psd](https://github.com/Agamnentzar/ag-psd) | JavaScript library for reading and writing Photoshop PSD files, including layers and effects | 734 | 🟢 | TypeScript |
| [acextract](https://github.com/bartoszj/acextract) | Lists and extracts content from Apple Assets.car compiled asset catalogs | 436 | 🔴 | Swift |
| [psd (Rust)](https://github.com/chinedufn/psd) | Rust crate for parsing Photoshop PSD files and their layers | 283 | 🟡 | Rust |
| [fig2sketch](https://github.com/sketch-hq/fig2sketch) | Converts Figma .fig files into Sketch documents by parsing the undocumented .fig format | 172 | 🟢 | Python |
| [PureRef-format](https://github.com/FyorDev/PureRef-format) | Reverse engineered PureRef .pur file format library | 167 | 🟢 | Python |
| [psd (Go)](https://github.com/oov/psd) | PSD/PSB Photoshop file reader for Go | 160 | 🟢 | Go |
| [aftereffects-aep-parser](https://github.com/boltframe/aftereffects-aep-parser) | Unofficial Go parser for Adobe After Effects .aep project files | 131 | 🔴 | Go |
| [libsai](https://github.com/Wunkolo/libsai) | Library for reading the encrypted PaintTool SAI .sai file format | 130 | 🟢 | C++ |
| [pytoshop](https://github.com/mdboom/pytoshop) | Python library for reading and writing Photoshop PSD and PSB files | 128 | 🔴 | Python |
| [clip_to_psd](https://github.com/dobrokot/clip_to_psd) | Converts Clip Studio Paint .clip files to PSD by reading the proprietary .clip container | 84 | 🟡 | Python |
| [Silicate](https://github.com/axaril/silicate) | Pure Rust GPU compositor that opens and renders Procreate files | 73 | 🟢 | Rust |
| [ProcreateViewer](https://github.com/jaromvogel/ProcreateViewer) | macOS QuickLook plugin that renders full previews of .procreate files | 72 | 🔴 | Python |
| [xdtools](https://github.com/umar-ahmed/xdtools) | Unofficial Python API for reading and writing Adobe XD files | 53 | 🔴 | Python |
| [abrupng](https://github.com/scurest/abrupng) | Dumps brush tip images from Photoshop ABR brush files | 38 | 🔴 | Rust |
| [pypdn](https://github.com/addisonElliott/pypdn) | Python package to read Paint.NET (.pdn) layered images | 37 | 🟡 | Python |
| [AFDesignLoad](https://github.com/NickBeeuwsaert/AFDesignLoad) | Loads and parses Affinity Designer files | 35 | 🔴 | Python |
| [afread](https://github.com/VMDevCpp/afread) | Library for reading Affinity Designer, Photo and Publisher (.afdesign/.afphoto/.afpub) files | 27 | 🔴 | C++ |
| [procreate-rs](https://github.com/m1guelpf/procreate-rs) | Rust library for parsing Procreate files | 13 | 🟡 | Rust |
| [XdParser](https://github.com/kyubuns/XdParser) | Adobe XD file parser for C# | 8 | 🔴 | C# |
| [libfreehand](https://git.libreoffice.org/libfreehand) | Library for importing Aldus/Macromedia FreeHand drawings |  | ⚪ |  |

## E-books

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [calibre](https://github.com/kovidgoyal/calibre) | E-book manager with readers for many proprietary formats (MOBI, LIT, LRF, PDB, KFX via plugin) | 26,232 | 🟢 | Python |
| [kepubify](https://github.com/pgaskin/kepubify) | Standalone EPUB to Kobo KEPUB converter replicating Kobo's own conversion | 898 | 🟢 | Go |
| [libmobi](https://github.com/bfabiszewski/libmobi) | C library for handling Kindle MOBI/AZW3/KF8 e-book formats | 487 | 🟡 | C |
| [fb2cng](https://github.com/rupor-github/fb2cng) | FB2 converter to EPUB, KEPUB and Kindle AZW8/KFX formats | 82 | 🟢 | Go |
| [mobi](https://github.com/iscc/mobi) | Python library to unpack Kindle (kindlegen) e-books | 78 | 🟡 | Python |
| [boko](https://github.com/zacharydenton/boko) | Rust converter from EPUB to Kindle KFX, AZW3 and MOBI | 66 | 🟢 | Rust |
| [KFX Output (mirror)](https://github.com/dstaley/calibre-kfx-output) | Mirror of jhowell's calibre plugin that writes Kindle KFX books | 29 | 🔴 | Python |
| [kdegraphics-mobipocket](https://invent.kde.org/graphics/kdegraphics-mobipocket) | Library for reading Mobipocket e-book files |  | ⚪ |  |
| [libe-book](https://sourceforge.net/projects/libebook) | Document Liberation library for legacy e-book formats (eReader, Plucker, TealDoc, LRF and more) |  | ⚪ |  |

## EDA & PCB

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [OpenBoardView](https://github.com/OpenBoardView/OpenBoardView) | Viewer for proprietary laptop/phone boardview files (.brd, .bdv, .fz and others) | 1,901 | 🟢 | C |
| [easyeda2kicad.py](https://github.com/uPesy/easyeda2kicad.py) | Converts EasyEDA/LCSC component symbols, footprints and 3D models to KiCad | 1,717 | 🟢 | Python |
| [altium2kicad](https://github.com/thesourcerer8/altium2kicad) | Converts Altium PCB and schematic files to KiCad | 956 | 🗄️ | Perl |
| [easyeda2kicad](https://github.com/wokwi/easyeda2kicad) | Converts EasyEDA schematics and PCB designs to KiCad | 338 | 🟡 | TypeScript |
| [altium.js](https://github.com/gsuberland/altium_js) | Browser-based parser and renderer for Altium SchDoc schematics | 145 | 🟡 | JavaScript |
| [OpenOrCadParser](https://github.com/Werni2A/OpenOrCadParser) | FOSS parser for Cadence OrCAD Capture binary design files | 69 | 🗄️ | C++ |
| [Altium-Schematic-Parser](https://github.com/a3ng7n/Altium-Schematic-Parser) | Converts Altium .SchDoc files to JSON | 52 | 🟢 | Python |
| [BoardRipper](https://github.com/AlexeyInwerp/BoardRipper) | Web-based viewer for 14 boardview formats (BVR, BRD, BDV, FZ, GenCAD and more) | 43 | 🟢 | TypeScript |
| [altium-cli](https://github.com/akiselev/altium-cli) | Rust library and CLI that reads and writes Altium SchDoc, PcbDoc, SchLib, PcbLib and IntLib | 17 | 🟢 | Rust |
| [ExtractAltiumSTEPModels](https://github.com/braincodec/ExtractAltiumSTEPModels) | Extracts embedded 3D STEP models from Altium PCB files | 14 | 🔴 | Python |
| [pyAltiumLib](https://github.com/ChrisHoyer/pyAltiumLib) | Reads Altium schematic and PCB library files in Python | 13 | 🟢 | Python |
| [bv2bvr](https://github.com/inflex/bv2bvr) | Converts BV boardview files to the BVR format readable by OpenBoardView | 12 | 🔴 | C |
| [PyAltium](https://github.com/pluots/PyAltium) | Python package to read Altium design files | 11 | 🔴 | Python |

## Filesystems & Archives

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [android-backup-extractor](https://github.com/nelenkov/android-backup-extractor) | Unpacks and repacks Android adb backup (.ab) files | 2,605 | 🟢 | Java |
| [apfs-fuse](https://github.com/sgan81/apfs-fuse) | FUSE driver for reading Apple APFS volumes | 2,164 | 🟡 | C++ |
| [dislocker](https://github.com/Aorimn/dislocker) | FUSE driver to read/write BitLocker-encrypted volumes on Linux/macOS | 1,950 | 🟢 | C |
| [lessmsi](https://github.com/activescott/lessmsi) | Views and extracts the contents of Windows Installer (.msi) files | 1,772 | 🟢 | C# |
| [NTFS-3G](https://github.com/tuxera/ntfs-3g) | Read/write NTFS driver for Linux/macOS | 1,528 | 🟢 | C |
| [innoextract](https://github.com/dscharrer/innoextract) | Unpacks installers created by Inno Setup without running them | 1,395 | 🟡 | C++ |
| [exfat (relan)](https://github.com/relan/exfat) | Free FUSE exFAT implementation, written before Microsoft published the spec | 888 | 🟢 | C |
| [linux-apfs-rw](https://github.com/linux-apfs/linux-apfs-rw) | Linux kernel APFS module with experimental write support | 808 | 🟢 | C |
| [unshield](https://github.com/twogood/unshield) | Extracts CAB files from InstallShield installers | 435 | 🟢 | C |
| [libfsapfs](https://github.com/libyal/libfsapfs) | Library and tools to access Apple File System (APFS) | 429 | 🟢 | C |
| [ubidump](https://github.com/nlitsme/ubidump) | Tool to view and extract files from UBIFS images | 293 | 🟡 | Python |
| [libbde](https://github.com/libyal/libbde) | Library and tools for BitLocker Drive Encryption volumes | 262 | 🟢 | C |
| [libevtx](https://github.com/libyal/libevtx) | Library and tools for Windows XML Event Log (EVTX) format | 243 | 🟢 | C |
| [libfsntfs](https://github.com/libyal/libfsntfs) | Library and tools to access NTFS | 238 | 🟢 | C |
| [wimlib](https://github.com/ebiggers/wimlib) | Library and tools for the Windows Imaging Format (WIM), including its proprietary compression | 223 | 🟢 | C |
| [libmspack](https://github.com/kyz/libmspack) | Library for Microsoft compression formats: CAB, CHM, HLP, LIT, KWAJ, SZDD | 217 | 🟢 | C |
| [dtformats](https://github.com/libyal/dtformats) | Collection of data formats | 201 | 🟢 | Python |
| [libfsrefs](https://github.com/libyal/libfsrefs) | Library and tools to access Microsoft ReFS | 201 | 🟢 | C |
| [vpk](https://github.com/ValvePython/vpk) | Open, search, extract and create Valve VPK archives in Python | 191 | 🔴 | Python |
| [fatx](https://github.com/XboxDev/fatx) | Original Xbox FATX filesystem library with Python bindings, FUSE driver and GUI | 183 | 🟢 | C |
| [AmiFUSE](https://github.com/reinauer/AmiFUSE) | Native Amiga filesystems on macOS, Linux and Windows via FUSE | 152 | 🟢 | Python |
| [libregf](https://github.com/libyal/libregf) | Library and tools for the Windows NT Registry file (REGF) format | 142 | 🟢 | C |
| [XADMaster](https://github.com/MacPaw/XADMaster) | Unarchiver engine supporting StuffIt, DiskDoubler, Compact Pro and many legacy archive formats | 136 | 🟢 | C |
| [libvshadow](https://github.com/libyal/libvshadow) | Library and tools for Windows Volume Shadow Snapshot (VSS) format | 119 | 🟢 | C |
| [gho](https://github.com/nyarime/gho) | Pure Go Norton Ghost GHO disk image parser | 90 | 🟢 | Go |
| [apfs.ksy](https://github.com/cugu/apfs.ksy) | APFS filesystem format for Kaitai Struct | 82 | 🗄️ |  |
| [go-ntfs](https://github.com/Velocidex/go-ntfs) | Pure Go NTFS file system parser | 77 | 🟢 | Go |
| [hbkit](https://github.com/YordiLorenzo/hbkit) | Recovers files from Synology Hyper Backup archives without Synology software | 69 | 🟢 | Python |
| [titl](https://github.com/josephw/titl) | Tools for iTunes Libraries | 66 | 🟡 | Java |
| [DynamicDiskPartitioner](https://github.com/TalAloni/DynamicDiskPartitioner) | Manage Windows dynamic disks and volumes (LDM) | 64 | 🟡 | C# |
| [unshieldv3](https://github.com/wfr/unshieldv3) | Extract InstallShield V3 (*.Z) archives | 61 | 🟡 | C |
| [libzbitmap](https://github.com/eafer/libzbitmap) | Library for Apple's LZBITMAP compression | 59 | 🔴 | C |
| [castools](https://github.com/joyrex2001/castools) | Reads sampled MSX cassette tapes and converts them to standard CAS images | 45 | 🟢 | C |
| [rsrcfork](https://github.com/dgelessus/python-rsrcfork) | Pure Python reader for classic Macintosh resource forks | 32 | 🔴 | Python |
| [libmodi](https://github.com/libyal/libmodi) | Library for Mac OS disk image formats (UDIF, sparse image, sparse bundle) | 22 | 🟢 | C |
| [NbuExplorer](https://github.com/jdsn/nbuexplorer) | Extracts Nokia NBU, NFB, NFC and ARC phone backup files | 19 | 🔴 | C# |
| [bom](https://github.com/iineva/bom) | Apple iOS / macOS Assets.car decoder, write in golang | 18 | 🟡 | Go |
| [libitlp](https://github.com/jeanthom/libitlp) | iTunes "itl" database parsing | 17 | 🗄️ | C |
| [dissect.hypervisor](https://github.com/fox-it/dissect.hypervisor) | Parsers for VMware, Hyper-V and other hypervisor disk, backup and config formats | 12 | 🟢 | Python |
| [dissect.ntfs](https://github.com/fox-it/dissect.ntfs) | Python parser for the NTFS file system | 11 | 🟢 | Python |
| [dissect.fve](https://github.com/fox-it/dissect.fve) | Parsers for BitLocker and LUKS full-volume encryption, for use with known keys | 8 | 🟢 | Python |
| [dissect.apfs](https://github.com/fox-it/dissect.apfs) | Python parser for the Apple File System (APFS) | 6 | 🟢 | Python |
| [libphdi](https://github.com/libyal/libphdi) | Library for the Parallels Hard Disk image format | 6 | 🟢 | C |
| [dissect.vmfs](https://github.com/fox-it/dissect.vmfs) | Python parser for VMware's VMFS file system | 5 | 🟢 | Python |
| [nokia-nbu-tools](https://github.com/thouters/nokia-nbu-tools) | Dumper for Nokia PC Suite NBU backup files | 3 | 🔴 | Python |
| [cabextract](https://www.cabextract.org.uk/) | Tool for extracting Microsoft cabinet files |  | ⚪ |  |
| [libmspack](https://www.cabextract.org.uk/libmspack/) | Library for Microsoft compression formats: CAB, CHM, LIT, HLP, KWAJ, SZDD |  | ⚪ |  |
| [unrar-free](https://gitlab.com/bgermann/unrar-free) | Free software extractor for RAR archives |  | ⚪ |  |

## Format Description Tools

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [ImHex](https://github.com/WerWolv/ImHex) | Hex editor for reverse engineers with a pattern language for binary formats | 55,543 | 🟢 | C++ |
| [fq](https://github.com/wader/fq) | jq-like tool, language and decoders for inspecting binary formats | 10,618 | 🟢 | Go |
| [Kaitai Struct](https://github.com/kaitai-io/kaitai_struct) | Declarative language to describe binary formats and generate parsers | 4,720 | 🟢 | Shell |
| [ImHex-Patterns](https://github.com/WerWolv/ImHex-Patterns) | Pattern files describing many binary file formats for ImHex | 1,039 | 🟢 | ImHex Pattern Language |
| [Kaitai Struct Formats](https://github.com/kaitai-io/kaitai_struct_formats) | Library of .ksy descriptions of hundreds of binary file formats | 796 | 🟢 | Kaitai Struct |
| [kaitai_struct_compiler](https://github.com/kaitai-io/kaitai_struct_compiler) | Compiler that turns Kaitai Struct .ksy format descriptions into parsers for many languages | 667 | 🟢 | Scala |
| [Deark](https://github.com/jsummers/deark) | Extracts and decodes hundreds of legacy file, archive and image formats | 231 | 🟢 | C |
| [kbdasm](https://github.com/grompe/kbdasm) | Assembler/disassembler for Windows keyboard layout DLLs | 95 | 🔴 | Assembly |
| [serum-preset-packager](https://github.com/KennethWussmann/serum-preset-packager) | Reverse-engineered Serum 2 synth preset format; converts to/from JSON | 68 | 🟢 | Python |
| [bitfiltrator](https://github.com/epfl-vlsc/bitfiltrator) | General approach for reverse-engineering Xilinx FPGA bitstream formats | 60 | 🔴 | Python |
| [nextion-font-editor](https://github.com/hagronnestad/nextion-font-editor) | Nextion .zi font format documentation, parser, generator and editor | 59 | 🔴 | C# |
| [xnb_parse](https://github.com/fesh0r/xnb_parse) | XNA xnb/xact file parser and FEZ extractor/viewer | 49 | 🔴 | Python |
| [libyal assorted](https://github.com/libyal/assorted) | Format documentation and scripts from the libyal project | 40 | 🟢 | C |
| [flipnote-studio-3d-docs](https://github.com/Flipnote-Collective/flipnote-studio-3d-docs) | Documentation for Flipnote Studio 3D formats | 37 | 🔴 |  |
| [gameformats](https://github.com/dstien/gameformats) | Tools and specs for reverse-engineered game file formats | 31 | 🔴 | C++ |
| [pyxbe](https://github.com/XboxDev/pyxbe) | Python 3 library to read and write XBE, the original Xbox executable format | 28 | 🟢 | Python |
| [fseq-file-format](https://github.com/Cryptkeeper/fseq-file-format) | Reverse-engineered documentation of the Falcon sequence (FSEQ) v2 file format | 24 | 🟡 |  |
| [murmelbahn](https://github.com/lfrancke/murmelbahn) | Reverse-engineered Gravitrax marble run course file format | 8 | 🟢 | Rust |
| [packet-tracer-pkt-format](https://github.com/aacanadaa/packet-tracer-pkt-format) | Byte-exact codec for Cisco Packet Tracer .pkt/.pka lab files | 8 | 🟢 | Python |
| [XBEpy](https://github.com/LoveMHz/XBEpy) | Library for viewing, extracting and validating data inside original Xbox XBE executables | 8 | 🔴 | Python |
| [RKD Telemetry Extractor](https://github.com/sam-dumont/rkd-telemetry-extractor) | Decoder for the proprietary .rkd telemetry format of Race-Keeper video recorders | 6 | 🟢 | Go |
| [shockwave-reversing](https://github.com/JrMasterModelBuilder/shockwave-reversing) | Notes and resources for reverse engineering Shockwave/Director files | 5 | 🔴 |  |
| [remus-rlf-reader](https://github.com/isaacgerg/remus-rlf-reader) | Reverse-engineered RLF log format of REMUS underwater drones | 1 | 🟢 | Python |
| [GarminSettingsFileParser](https://github.com/cyberang3l/GarminSettingsFileParser) | Reads and writes Garmin's undocumented GARMIN.SET device settings file | 0 | 🟡 | Python |

## Graphics & CAD

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [AssetStudio](https://github.com/Perfare/AssetStudio) | Explore and extract Unity assets and assetbundles | 15,587 | 🗄️ | C# |
| [Assimp](https://github.com/assimp/assimp) | Asset importer for 40+ 3D formats, including proprietary FBX, 3DS and Blender files | 13,283 | 🟢 | C++ |
| [FModel](https://github.com/4sval/FModel) | Unreal Engine archive (.pak/.utoc) explorer | 3,284 | 🟢 | C# |
| [psd.rb](https://github.com/layervault/psd.rb) | Parse Photoshop PSD files in Ruby | 3,114 | 🔴 | Ruby |
| [LibreDWG](https://github.com/LibreDWG/libredwg) | GNU library to read and write Autodesk DWG CAD files | 1,638 | 🟢 | C |
| [psd-tools](https://github.com/psd-tools/psd-tools) | Python package for reading Adobe Photoshop PSD files | 1,483 | 🟢 | Python |
| [ufbx](https://github.com/ufbx/ufbx) | Single-file loader for Autodesk FBX files | 1,421 | 🟢 | C |
| [@webtoon/psd](https://github.com/webtoon/psd) | Fast zero-dependency PSD parser for the web and Node.js | 1,352 | 🟡 | TypeScript |
| [OpenFBX](https://github.com/nem0/OpenFBX) | Lightweight open source FBX importer | 1,352 | 🟢 | C |
| [CUE4Parse](https://github.com/FabianFG/CUE4Parse) | C# parser for Unreal Engine 4/5 archives and assets | 668 | 🟢 | C# |
| [Embroidermodder](https://github.com/Embroidermodder/Embroidermodder) | Free machine embroidery editor supporting many proprietary embroidery formats | 636 | 🟢 | C |
| [sK1](https://github.com/sk1-project/sk1-wx) | Vector graphics editor with reverse-engineered CorelDRAW CDR and other proprietary importers | 335 | 🟢 | Python |
| [figma-to-json](https://github.com/yagudaev/figma-to-json) | Reads and writes Figma's binary .fig (Kiwi) files as JSON | 332 | 🟡 | TypeScript |
| [pyembroidery](https://github.com/EmbroidePy/pyembroidery) | Reads and writes many proprietary machine embroidery formats (PES, DST, JEF, EXP and more) | 313 | 🟡 | Python |
| [SWFTools](https://github.com/swftools/swftools) | Utilities for editing and generating Adobe Flash SWF files | 309 | 🟢 | C |
| [mviewer](https://github.com/majimboo/mviewer) | Viewer, converter and glTF exporter for Marmoset .mview scenes | 306 | 🟢 | Rust |
| [libdxfrw](https://github.com/LibreCAD/libdxfrw) | C++ library to read/write DXF and read AutoCAD DWG files, used by LibreCAD | 295 | 🟢 | C++ |
| [MHC2](https://github.com/dantmnf/MHC2) | Information on Windows next-generation color management and the MHC2 ICC tag | 289 | 🟡 | C# |
| [UniConvertor](https://github.com/sk1-project/uniconvertor) | Universal vector graphics translator with reverse-engineered CorelDRAW CDR/CMX importers | 177 | 🟢 | Python |
| [InventorLoader](https://github.com/jmplonka/InventorLoader) | FreeCAD workbench that imports Autodesk Inventor files | 169 | 🟡 | Python |
| [OpenSKP](https://github.com/iamahsanmehmood/openskp) | Open-source SketchUp .skp reader/writer and converter that does not need the Trimble SDK | 148 | 🟢 | Python |
| [MobiclipDecoder](https://github.com/Gericom/MobiclipDecoder) | Decoder for the proprietary Mobiclip video codec used in Nintendo DS and Wii games | 113 | 🔴 | C# |
| [Rainbow](https://github.com/marco-calautti/Rainbow) | Texture format converter for various game consoles' graphics formats | 99 | 🔴 | C# |
| [libembroidery](https://github.com/Embroidermodder/libembroidery) | C library for reading and writing machine embroidery design files | 82 | 🟢 | C |
| [libredwg-web](https://github.com/mlightcad/libredwg-web) | WebAssembly/JavaScript DWG/DXF parser built on LibreDWG | 82 | 🟢 | C |
| [voxel-viewer](https://github.com/denysdovhan/voxel-viewer) | Web viewer for CBCT volumes and scan folders, including Sirona GALILEOS formats | 82 | 🟢 | TypeScript |
| [nd2](https://github.com/tlambert03/nd2) | Full-featured reader for Nikon NIS-Elements .nd2 microscopy files | 81 | 🟢 | Python |
| [rvt-rs](https://github.com/DrunkOnJava/rvt-rs) | Clean-room reader for Autodesk Revit files without Revit | 73 | 🟢 | Rust |
| [warcraft-rs](https://github.com/wowemulation-dev/warcraft-rs) | Unified CLI tool for World of Warcraft file formats. Integrates file format libraries for parsing, conversion, and va... | 65 | 🟢 | Rust |
| [ColorPaletteCodable](https://github.com/dagronf/ColorPaletteCodable) | Reader/writer for many color palette and gradient file formats | 57 | 🟢 | Swift |
| [OpenAllegroParser](https://github.com/Werni2A/OpenAllegroParser) | Open-source parser for Cadence Allegro PCB designs | 57 | 🗄️ | C++ |
| [MascotCapsule](https://github.com/j2me-preservation/MascotCapsule) | MascotCapsule Micro3D research, libraries and tools | 47 | 🔴 | Python |
| [swf-parser](https://github.com/open-flash/swf-parser) | Rust and TypeScript parsers for the SWF format | 33 | 🔴 | Rust |
| [lib3ds](https://github.com/vkocheryzhkin/lib3ds) | Library for reading and writing Autodesk 3D Studio .3DS model files | 30 | 🔴 | C |
| [drxtract](https://github.com/System25/drxtract) | Extracts data from Macromedia Director 5 DRI and DRX files | 26 | 🟢 | Python |
| [3mf-to-glb](https://github.com/SamiSalah221/3mf-to-glb) | Reverse-engineered Bambu/Orca 3MF multi-color format; converts to GLB keeping colors | 25 | 🟢 | TypeScript |
| [libcdr](https://github.com/LibreOffice/libcdr) | Parser for CorelDRAW documents | 21 | 🟢 | C++ |
| [wow_dbc](https://github.com/gtker/wow_dbc) | Rust library for reading and writing World of Warcraft 1.12, 2.4.3 and 3.3.5 DBC files. | 16 | 🟢 | Rust |
| [pvr2image](https://github.com/VincentNLOBJ/pvr2image) | Universal decoder for Sega PowerVR (PVR) textures | 12 | 🟡 | Python |
| [skp2tri](https://github.com/julfla/skp2tri) | Parses SketchUp .skp files into a simple triangle format | 12 | 🔴 | C |
| [continuity](https://github.com/scummvm-director/continuity) | Tools for inspecting and working with Macromedia Director movies | 11 | 🔴 | Python |
| [image-blp](https://github.com/zloy-tulen/image-blp) | Tool to encode/decode Blizzard BLP textures for Rust language | 10 | 🔴 | Rust |
| [ps2-tim2-tool](https://github.com/PS2HomeDeveloper/ps2-tim2-tool) | Converter between images and PlayStation 2 TIM2 (.tm2) textures | 10 | 🟢 | Python |
| [jDwgParser](https://github.com/ebandal/jDwgParser) | Java reader for the AutoCAD DWG file format | 8 | 🟢 | Java |
| [arw6_decode](https://github.com/abbradar/arw6_decode) | Reverse-engineered Sony ARW6 (LLVC v3) RAW image decoder | 4 | 🟢 | Python |
| [ShockwaveParser](https://github.com/datagutten/ShockwaveParser) | Python class to parse and extract data from Shockwave/Director movies | 4 | 🟢 | Python |
| [worgen-rs](https://github.com/nocthir/worgen-rs) | worgen-rs | 4 | 🟢 | Rust |
| [wow_chunky](https://github.com/bigglesss/wow_chunky) | A pure Rust parsing library for World of Warcraft's chunked files (and some additional binary files), targeting versi... | 1 | 🔴 | Rust |
| [CTP9Decode](https://codeberg.org/dcurrie/CTP9Decode) | Reverse-engineered decoder for old Corel CPT9 (Corel Photo-Paint) files |  | ⚪ |  |
| [libwpg](https://sourceforge.net/projects/libwpg) | Library to read WordPerfect Graphics (.wpg) images |  | ⚪ |  |
| [libzmf](https://git.libreoffice.org/libzmf) | Document Liberation library for Zoner Callisto/Draw (.zmf) vector drawings |  | ⚪ |  |
| [sldprt-format-research](https://gitlab.com/blussy/sldprt-format-research) | Reverse engineering the undocumented SolidWorks SLDPRT format |  | ⚪ |  |

## Maps & GIS

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [GDAL](https://github.com/OSGeo/gdal) | Geospatial format library including the reverse-engineered OpenFileGDB and MapInfo drivers | 6,113 | 🟢 | C++ |
| [GPXSee](https://github.com/tumic0/GPXSee) | GPS log and map viewer that reads Garmin IMG, OziExplorer, TrekBuddy and many other formats | 1,253 | 🟢 | C++ |
| [GPSBabel](https://github.com/GPSBabel/gpsbabel) | Converts between many proprietary GPS formats (Garmin, Magellan, OziExplorer, TomTom) | 553 | 🟢 | C++ |
| [QMapShack](https://github.com/Maproom/qmapshack) | GIS and trip-planning app that renders Garmin IMG vector maps and reads many GPS formats | 446 | 🟢 | C++ |
| [dump_gdbtable](https://github.com/rouault/dump_gdbtable) | Script and reverse-engineered spec for Esri File Geodatabase .gdbtable files | 153 | 🟡 | Python |
| [gimgtools](https://github.com/wuyongzheng/gimgtools) | Tools to inspect, split, merge and unlock-free extract Garmin IMG map files | 91 | 🔴 | C |
| [Androzic](https://github.com/andreynovikov/Androzic) | Android navigation app that reads OziExplorer ozf2/ozfx3 raster maps | 54 | 🔴 | Java |
| [mkgmap](https://github.com/openstreetmap/mkgmap) | Compiler that writes Garmin .img maps from OpenStreetMap data (reverse-engineered format) | 49 | 🔴 | Java |
| [qdc-converter](https://github.com/interlark/qdc-converter) | Converter for Garmin QuickDraw Contours (QDC) files to CSV tables and GRD rasters | 18 | 🔴 | Python |
| [python-sllib](https://github.com/opensounder/python-sllib) | Python library for reading Lowrance SL2, SL3 and SLG sonar logs | 16 | 🔴 | Python |
| [sl2decode](https://github.com/Chris78/sl2decode) | Decodes Lowrance SL2 sonar log files with Ruby | 10 | 🔴 | Ruby |
| [imgdecode-mb](https://github.com/burto/imgdecode-mb) | Decoder for Garmin IMG map files, derived from imgdecode | 5 | 🔴 | C++ |
| [jnxutil](https://github.com/apr2504/jnxutil) | Linux utility for manipulating Garmin JNX raster map files | 5 | 🔴 | C |
| [sl2json](https://github.com/hrbrmstr/sl2json) | Standalone converter from Lowrance SL2 sonar logs to ndjson | 4 | 🔴 | C++ |
| [garmin-img](https://github.com/TomasHubelbauer/garmin-img) | JavaScript parser and renderer for Garmin IMG maps | 3 | 🔴 | JavaScript |
| [imageio-ozf](https://github.com/nikolaybespalov/imageio-ozf) | Java ImageIO plugin for OziExplorer ozf2/ozf3 raster map files | 3 | 🔴 | Java |
| [HumminbirdSonarFileViewer](https://github.com/petervalencic/HumminbirdSonarFileViewer) | Java viewer for Humminbird side-scan sonar recordings | 2 | 🟢 | Java |
| [kolibrie](https://github.com/yschaeff/kolibrie) | Dissector for Humminbird sonar .SON recordings | 1 | 🟢 | Python |
| [locus-poi-db](https://gitlab.com/noschinl/locus-poi-db) | Reverse engineering of the POI database format used by Locus Map LoMaps |  | ⚪ |  |

## Media Codecs & Containers

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Multimedia framework with many reverse-engineered proprietary codecs and containers | 65,627 | 🟢 | C |
| [OpenJOC](https://github.com/chyinan/OpenJOC) | Independent clean-room E-AC-3 JOC decoder in Rust, with OAMD metadata and reconstruction-basis decoding. | 259 | 🟢 | Rust |
| [openaptx](https://github.com/arkq/openaptx) | Reverse engineered aptX and aptX HD audio codec | 165 | 🟢 | C |
| [MQA_identifier](https://github.com/purpl3F0x/MQA_identifier) | Tool to identify MQA encoded audio via codec reverse engineering | 139 | 🟢 | C++ |
| [samsung-ssc-reversed](https://github.com/Vinchethescript/samsung-ssc-reversed) | Partial reverse engineering of the Samsung Seamless Codec (SSC) Bluetooth audio codec | 10 | 🟡 | C |
| [libbluray](https://code.videolan.org/videolan/libbluray) | Library for Blu-ray disc navigation, playlists and menus |  | ⚪ |  |
| [libdvdnav](https://code.videolan.org/videolan/libdvdnav) | Library for DVD-Video menu navigation |  | ⚪ |  |
| [libdvdread](https://code.videolan.org/videolan/libdvdread) | Library for reading DVD-Video discs and IFO structures |  | ⚪ |  |
| [libsmacker](https://sourceforge.net/projects/libsmacker/) | Library for decoding RAD Game Tools Smacker video files |  | ⚪ |  |

## Office & Documents

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [SheetJS](https://github.com/SheetJS/sheetjs) | Spreadsheet toolkit reading XLS, XLSB, Lotus, Quattro Pro and many legacy formats | 36,341 | 🟡 |  |
| [LibreOffice](https://github.com/LibreOffice/core) | Office suite with import filters for reverse-engineered MS Office and other formats | 4,554 | 🟢 | C++ |
| [oletools](https://github.com/decalage2/oletools) | Python tools to analyze MS OLE2 files and Office documents | 3,439 | 🟢 | Python |
| [Apache POI](https://github.com/apache/poi) | Java API for Microsoft binary and OOXML Office formats | 2,280 | 🟢 | Java |
| [xlrd](https://github.com/python-excel/xlrd) | Python library for reading legacy Excel BIFF (.xls) files | 2,206 | 🟢 | Python |
| [hwp.js](https://github.com/hahnlee/hwp.js) | Open-source web viewer and parser for Hancom HWP documents | 1,307 | 🟡 | TypeScript |
| [MDB Tools](https://github.com/mdbtools/mdbtools) | Read Microsoft Access databases on Unix | 1,180 | 🟢 | C |
| [KindleUnpack](https://github.com/kevinhendricks/KindleUnpack) | Unpacks Amazon Kindle/Kindlegen MOBI/AZW3 ebooks | 1,103 | 🟢 | Python |
| [msg-extractor](https://github.com/TeamMsgExtractor/msg-extractor) | Extracts emails and attachments from Outlook .msg files | 855 | 🟢 | Python |
| [MSGReader](https://github.com/Sicos1977/MSGReader) | C# reader for Outlook .msg and .eml files without Outlook | 556 | 🟢 | C# |
| [apple_cloud_notes_parser](https://github.com/threeplanetssoftware/apple_cloud_notes_parser) | Parser for Apple Notes databases from iOS/macOS backups | 544 | 🟢 | Ruby |
| [libesedb](https://github.com/libyal/libesedb) | Library and tools for Extensible Storage Engine (ESE/EDB) databases | 381 | 🟢 | C |
| [libpff](https://github.com/libyal/libpff) | Library and tools for Outlook PFF/OFF (PST/OST) files | 373 | 🟢 | C |
| [MPXJ](https://github.com/joniles/mpxj) | Reads Microsoft Project MPP files and other schedule formats (Primavera, Asta, Phoenix) | 360 | 🟢 | Java |
| [pyhwp](https://github.com/mete0r/pyhwp) | Python parser for Hancom HWP v5 word processor files | 301 | 🟢 | Python |
| [java-libpst](https://github.com/rjohnsondev/java-libpst) | Pure Java library for reading Outlook PST files | 274 | 🔴 | Java |
| [olefile](https://github.com/decalage2/olefile) | Python package to parse, read and write Microsoft OLE2/Compound File Binary files | 274 | 🟡 | Python |
| [iWorkFileFormat](https://github.com/obriensp/iWorkFileFormat) | Documentation of the reverse-engineered iWork '13 file format | 273 | 🔴 | C++ |
| [CHMLib](https://github.com/jedwing/CHMLib) | Library for reading Microsoft ITSS/CHM compiled help files | 268 | 🔴 | C |
| [hwp-rs](https://github.com/hahnlee/hwp-rs) | Rust parser and tools for Hancom HWP documents | 232 | 🔴 | Rust |
| [reMarkableSync](https://github.com/jamesf91/reMarkableSync) | OneNote add-in that imports notes by parsing reMarkable's proprietary notebook format | 179 | 🟡 | C# |
| [pbixray](https://github.com/Hugoberry/pbixray) | Power BI .pbix and PowerPivot data model parser | 174 | 🟢 | Python |
| [pyOneNote](https://github.com/DissectMalware/pyOneNote) | Python parser for OneNote .one files that extracts embedded objects | 152 | 🟡 | Python |
| [HyperCardPreview](https://github.com/PierreLorenzi/HyperCardPreview) | macOS app that opens and displays HyperCard stacks from the reverse-engineered format | 143 | 🔴 | Swift |
| [remarkable-layers](https://github.com/bsdz/remarkable-layers) | Python module for reading and writing reMarkable lines files | 121 | 🗄️ | Python |
| [ProPresenter7-Proto](https://github.com/greyshirtguy/ProPresenter7-Proto) | Reverse engineered protobuf definitions for ProPresenter 7 file formats | 119 | 🟢 |  |
| [OnyxNoteRenderer](https://github.com/RobertCsordas/OnyxNoteRenderer) | Renders PDFs from Onyx Boox Note backup files (proprietary note format) | 114 | 🔴 | Python |
| [lines-are-beautiful](https://github.com/ax3l/lines-are-beautiful) | C++ file API for the reMarkable tablet's proprietary .lines notebook format | 113 | 🔴 | C++ |
| [onenote.rs](https://github.com/msiemens/onenote.rs) | Rust parser for Microsoft OneNote .one/.onetoc2 files (MS-ONESTORE) | 91 | 🟢 | Rust |
| [catdoc](https://github.com/petewarden/catdoc) | Command-line converter of legacy Microsoft Word documents to text | 89 | 🔴 | C |
| [cronodump](https://github.com/alephdata/cronodump) | Converter for the proprietary Cronos database format | 87 | 🔴 | Python |
| [remarkable-fs](https://github.com/nick8325/remarkable-fs) | FUSE filesystem exposing reMarkable's internal xochitl document store as normal files | 87 | 🔴 | Python |
| [re-lab](https://github.com/renyxa/re-lab) | Joint effort reverse engineering proprietary file formats for open source apps | 85 | 🔴 | Python |
| [rm-dl-annotated](https://github.com/jmpinit/rm-dl-annotated) | Export annotated PDFs by rendering reMarkable's proprietary annotation layers | 84 | 🔴 | Shell |
| [Onyx-Boox-Annotation-Highlight-Extractor](https://github.com/akosbalasko/Onyx-Boox-Annotation-Highlight-Extractor) | Extracts highlights and annotations from Onyx Boox reading-notes exports | 83 | 🟡 | TypeScript |
| [Antiword](https://github.com/grobian/antiword) | Free reader for Microsoft Word binary documents | 82 | 🟢 | C |
| [libolecf](https://github.com/libyal/libolecf) | Library and tools for the OLE 2 Compound File format | 80 | 🟢 | C |
| [kindling](https://github.com/ciscoriordan/kindling) | Reverse-engineered kindlegen MOBI/KF8 builder in Rust, ~7,000x faster | 61 | 🟢 | Rust |
| [BabylonToHtml](https://github.com/alonrotem/BabylonToHtml) | Convert Babylon .bgl dictionaries to structured HTML | 58 | 🟡 | C# |
| [pychm](https://github.com/dottedmag/pychm) | Python bindings for CHMLib to read Microsoft CHM help files | 58 | 🟡 | Python |
| [msgreader (JS)](https://github.com/HiraokaHyperTools/msgreader) | JavaScript reader for Outlook .msg files | 57 | 🟢 | TypeScript |
| [libpst](https://github.com/pst-format/libpst) | Library for reading Microsoft Outlook PST files | 51 | 🟡 | C |
| [libvisio](https://github.com/LibreOffice/libvisio) | Parser for Microsoft Visio file formats (re-lab reverse engineering) | 47 | 🟢 | C++ |
| [stackimport](https://github.com/uliwitness/stackimport) | Reads HyperCard stacks and converts them to XML and images | 43 | 🔴 | C++ |
| [helpdeco](https://github.com/pmachapman/helpdeco) | Decompiles Windows WinHelp (.hlp) files back to RTF and project files | 38 | 🟢 | C |
| [sdocx](https://github.com/twangodev/sdocx) | Reverse-engineered tooling and SDK for Samsung Notes (.sdocx) files | 31 | 🟢 | Rust |
| [boox-notes-backup-parser](https://github.com/DAmesberger/boox-notes-backup-parser) | Parses Onyx Boox Notes backup folders and extracts pages | 29 | 🟡 | Python |
| [wsconvert](https://github.com/kbarni/wsconvert) | Converts WordStar documents to Markdown | 20 | 🟢 | Python |
| [FileMaker-XMLsnippet-Claude-Skill](https://github.com/andykear/FileMaker-XMLsnippet-Claude-Skill) | Reverse-engineered spec of FileMaker's undocumented script XML clipboard format | 19 | 🟢 |  |
| [libetonyek](https://github.com/LibreOffice/libetonyek) | Parser for Apple Keynote, Pages and Numbers documents | 19 | 🟢 | C++ |
| [hypercard-stack-uploader](https://github.com/hyperhello/hypercard-stack-uploader) | Imports classic HyperCard stacks and exports them as HTML or JSON | 16 | 🔴 | HTML |
| [reMarkable-kaitai](https://github.com/matomatical/reMarkable-kaitai) | Kaitai Struct specifications for the reMarkable binary .rm notebook format | 16 | 🔴 | Kaitai Struct |
| [libmspub](https://github.com/LibreOffice/libmspub) | Parser for Microsoft Publisher documents | 14 | 🟢 | C++ |
| [MisterDiagram](https://github.com/MisterDiagram/MisterDiagram) | Clean-room Rust core for Microsoft Visio .vsdx files and ShapeSheet, with a CLI | 14 | 🟢 | Rust |
| [libfole](https://github.com/libyal/libfole) | Library for Object Linking and Embedding (OLE) data types | 13 | 🟢 | C |
| [zee-rp](https://github.com/LilZeeCN/zee-rp) | Reader and writer for native Axure RP 11 documents via a reverse-engineered binary-record codec | 13 | 🟢 | JavaScript |
| [wv](https://github.com/AbiWord/wv) | Library for importing Microsoft Word 2-2003 binary documents | 12 | 🔴 | C |
| [ezpzfile-xdw](https://github.com/ezpzfile/ezpzfile-xdw) | Open-source reader and annotator for Fuji Xerox DocuWorks .xdw/.xbd files with a format spec | 11 | 🟢 | Rust |
| [librm_lines](https://github.com/RedTTGMoss/librm_lines) | C++ library to read, write and render reMarkable v6 .rm lines files | 10 | 🟢 | C++ |
| [parser-for-goodnotes](https://github.com/Kaih1825/parser-for-goodnotes) | Parser for the closed GoodNotes document format, reverse-engineered with LLMs | 9 | 🟢 | HTML |
| [libstaroffice](https://github.com/fosnola/libstaroffice) | Import filter for legacy binary StarOffice/StarWriter/StarCalc documents | 8 | 🟢 | C++ |
| [OpenJTD rjtd](https://github.com/OpenJTD/rjtd) | Reverse-engineered Ichitaro JTD/JTT word processor format; Rust reader/renderer | 7 | 🟢 | Rust |
| [libabw](https://github.com/LibreOffice/libabw) | Document Liberation library that reads AbiWord documents (GitHub mirror) | 5 | 🟢 | C++ |
| [dissect.ole](https://github.com/fox-it/dissect.ole) | Python parser for the OLE compound file format | 4 | 🟢 | Python |
| [libhlp](https://github.com/trypsynth/libhlp) | Pure Rust reader for WinHelp (.hlp) files including LZ77 and phrase decompression | 2 | 🟢 | Rust |
| [Tika-JTD](https://github.com/KHiyowa/Tika-JTD) | Apache Tika parser that extracts text from Ichitaro (.jtd/.jtt) documents | 2 | 🟢 | Kotlin |
| [libetonyek](https://git.libreoffice.org/libetonyek) | Library for importing Apple Keynote, Pages and Numbers documents |  | ⚪ |  |
| [libgsf](https://gitlab.gnome.org/GNOME/libgsf) | Structured file I/O library including Microsoft OLE2 compound document support |  | ⚪ |  |
| [libmspub](https://git.libreoffice.org/libmspub) | Library for importing Microsoft Publisher documents, from LibreOffice's Document Liberation Project |  | ⚪ |  |
| [libmwaw](https://sourceforge.net/projects/libmwaw) | Imports many legacy Mac document formats (MacWrite, ClarisWorks, MacDraw, WriteNow and more) |  | ⚪ |  |
| [libpagemaker](https://git.libreoffice.org/libpagemaker) | Document Liberation library that imports Adobe/Aldus PageMaker documents |  | ⚪ |  |
| [libqxp](https://git.libreoffice.org/libqxp) | Document Liberation library that imports QuarkXPress 3.1-4.1 documents |  | ⚪ |  |
| [libstaroffice](https://git.libreoffice.org/libstaroffice) | Library for importing legacy StarOffice binary documents |  | ⚪ |  |
| [libwpd](https://sourceforge.net/projects/libwpd) | Library for importing reverse-engineered WordPerfect documents |  | ⚪ |  |
| [libwps](https://sourceforge.net/projects/libwps) | Imports Microsoft Works, Lotus 1-2-3, Quattro Pro and other legacy DOS/Windows documents |  | ⚪ |  |
| [wvWare](https://sourceforge.net/projects/wvware/) | Library and tools for reading Microsoft Word binary documents |  | ⚪ |  |

## Other

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [capcut-cli](https://github.com/renezander030/capcut-cli) | Unofficial CLI to edit CapCut and JianYing project files | 948 | 🟢 | JavaScript |
| [pylabview](https://github.com/mefistotelis/pylabview) | Python reader of LabVIEW RSRC files (VI, CTL, LLB) | 171 | 🟢 | Python |
| [pka2xml](https://github.com/mircodz/pka2xml) | Converts Cisco Packet Tracer .pka/.pkt files to XML | 78 | 🔴 | C++ |
| [WinCCflexLogViewer](https://github.com/yuriqdev/WinCCflexLogViewer) | Viewer and parser for WinCC Flexible and TIA Portal data log files | 31 | 🔴 | C# |
| [SBU-Extractor](https://github.com/Luncher91/SBU-Extractor) | Exports data from Samsung KIES backup (SBU) files | 21 | 🔴 | C# |
| [KItinerary](https://invent.kde.org/pim/kitinerary) | Extracts travel data from airline, rail and event tickets, including proprietary barcode formats |  | ⚪ |  |
| [perception-pnrf](https://codeberg.org/Apollo3zehn/perception-pnrf) | Reverse-engineered specification and parser for HBK Perception PNRF measurement files |  | ⚪ |  |

## Windows & Forensic Artifacts

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [plaso](https://github.com/log2timeline/plaso) | Super-timeline tool with parsers for hundreds of Windows, macOS and app artifacts | 2,180 | 🟢 | Python |
| [Dissect](https://github.com/fox-it/dissect) | Forensics framework with parsers for many proprietary disk, file system and artifact formats | 1,176 | 🟢 | Python |
| [ALEAPP](https://github.com/abrignoni/ALEAPP) | Android Logs, Events and Protobuf Parser for app databases and artifacts | 1,017 | 🟢 | Python |
| [evtx (Rust)](https://github.com/omerbenamram/evtx) | Fast, safe Rust parser for the Windows XML Event Log (EVTX) format | 967 | 🟢 | Rust |
| [python-evtx](https://github.com/williballenthin/python-evtx) | Pure Python parser for Windows XML Event Log (.evtx) files | 785 | 🟢 | Python |
| [srum-dump](https://github.com/MarkBaggett/srum-dump) | Converts the Windows SRUM (System Resource Usage Monitor) database to spreadsheets | 766 | 🟢 | Python |
| [RegRipper 3.0](https://github.com/keydet89/RegRipper3.0) | Plugin-based extraction of data from Windows registry hives | 725 | 🟢 | Perl |
| [Python-dsstore](https://github.com/gehaxelt/Python-dsstore) | Parses macOS .DS_Store files and extracts file names | 510 | 🔴 | Python |
| [python-registry](https://github.com/williballenthin/python-registry) | Pure Python parser for Windows Registry hive files | 448 | 🟡 | Python |
| [flare-wmi](https://github.com/mandiant/flare-wmi) | Parser and tools for the undocumented WMI CIM repository format | 434 | 🗄️ | C++ |
| [evtx (Zimmerman)](https://github.com/EricZimmerman/evtx) | C# EVTX event log parser with extra maps | 377 | 🟢 | C# |
| [LECmd](https://github.com/EricZimmerman/LECmd) | Command-line parser for Windows LNK shortcut files | 349 | 🟢 | C# |
| [MFTECmd](https://github.com/EricZimmerman/MFTECmd) | Parser for NTFS $MFT, $J, $Boot and $SDS | 342 | 🟢 | C# |
| [WMI_Forensics](https://github.com/davidpany/WMI_Forensics) | Scripts to parse the WMI CIM repository for persistence artifacts | 320 | 🔴 | Python |
| [libewf](https://github.com/libyal/libewf) | Library for the EnCase Expert Witness Compression Format (EWF/E01) disk images | 318 | 🟢 | C |
| [PECmd](https://github.com/EricZimmerman/PECmd) | Windows Prefetch file parser | 310 | 🟢 | C# |
| [FSEventsParser](https://github.com/dlcowen/FSEventsParser) | Parser for macOS/iOS FSEvents logs | 282 | 🟡 | Python |
| [ShimCacheParser](https://github.com/mandiant/ShimCacheParser) | Parses the Windows Application Compatibility Cache from registry hives | 279 | 🗄️ | Python |
| [regipy](https://github.com/mkorman90/regipy) | OS-independent Python library for parsing offline Windows registry hives | 277 | 🟢 | Python |
| [Registry (Zimmerman)](https://github.com/EricZimmerman/Registry) | Full-featured offline Windows Registry parser in C# | 260 | 🟢 | C# |
| [ccl_chromium_reader](https://github.com/cclgroupltd/ccl_chromium_reader) | Python reimplementations of Chromium storage formats for forensics | 259 | 🟢 | Python |
| [INDXParse](https://github.com/williballenthin/INDXParse) | Tools for NTFS INDX records and other NTFS artifacts | 229 | 🟡 | Python |
| [liblnk](https://github.com/libyal/liblnk) | Library and tools for the Windows Shortcut (LNK) file format | 219 | 🟢 | C |
| [clfs-docs](https://github.com/ionescu007/clfs-docs) | Unofficial Common Log File System (CLFS) documentation | 192 | 🔴 |  |
| [Thumbcache Viewer](https://github.com/thumbcacheviewer/thumbcacheviewer) | Extracts images from Windows thumbcache and thumbs.db databases | 172 | 🟡 | C++ |
| [mft (Rust)](https://github.com/omerbenamram/mft) | Rust parser for the NTFS Master File Table ($MFT) | 160 | 🟢 | Rust |
| [shellbags](https://github.com/williballenthin/shellbags) | Cross-platform parser for Windows ShellBag registry artifacts | 160 | 🔴 | Python |
| [etl-parser](https://github.com/airbus-cert/etl-parser) | Pure Python parser for Windows Event Trace Log (ETL) files | 157 | 🟢 | Python |
| [rifiuti2](https://github.com/abelcheung/rifiuti2) | Analyses Windows Recycle Bin INFO2 and $I files | 156 | 🟢 | C |
| [BitsParser](https://github.com/fireeye/BitsParser) | Parses Windows BITS database files and job records | 152 | 🟡 | Python |
| [LnkParse3](https://github.com/Matmaus/LnkParse3) | Python parser for Windows LNK shortcut files | 146 | 🟢 | Python |
| [SIDR](https://github.com/strozfriedberg/sidr) | Search Index Database Reporter: parses the Windows Search index database | 145 | 🟢 | Rust |
| [yarp](https://github.com/msuhanov/yarp) | Yet Another Registry Parser: Windows registry hive parser with transaction log recovery | 142 | 🔴 | Python |
| [spotlight_parser](https://github.com/ydkhatri/spotlight_parser) | Reads macOS Spotlight store.db databases | 138 | 🟢 | Python |
| [AppCompatCacheParser](https://github.com/EricZimmerman/AppCompatCacheParser) | Parser for the Windows AppCompatCache (ShimCache) | 130 | 🟢 | C# |
| [JLECmd](https://github.com/EricZimmerman/JLECmd) | Parser for Windows Automatic and Custom Destinations jump lists | 124 | 🟢 | C# |
| [forensicsim](https://github.com/lxndrblz/forensicsim) | Autopsy parser extracting Microsoft Teams messages, posts and contacts from its LevelDB stores | 123 | 🟢 | Python |
| [Windows-Prefetch-Parser](https://github.com/PoorBillionaire/Windows-Prefetch-Parser) | Parses Windows Prefetch files from XP to Windows 10 | 123 | 🟡 | Python |
| [USN-Journal-Parser](https://github.com/PoorBillionaire/USN-Journal-Parser) | Python script to parse the NTFS USN change journal | 119 | 🔴 | Python |
| [Lnk](https://github.com/EricZimmerman/Lnk) | C# library for parsing Windows LNK shortcut files | 100 | 🟢 | C# |
| [ds_store](https://github.com/dmgbuild/ds_store) | Python library to read and write Finder .DS_Store files | 95 | 🟢 | Python |
| [libscca](https://github.com/libyal/libscca) | Library and tools for the Windows Prefetch (SCCA) file format | 90 | 🟢 | C |
| [libfwsi](https://github.com/libyal/libfwsi) | Library for the Windows Shell Item format used in ShellBags and LNK files | 75 | 🟢 | C |
| [bits_parser](https://github.com/ANSSI-FR/bits_parser) | Extracts BITS jobs from Windows QMGR queue files | 74 | 🟡 | Python |
| [libevt](https://github.com/libyal/libevt) | Library and tools for the legacy Windows Event Log (EVT) format | 60 | 🟢 | C |
| [libfwnt](https://github.com/libyal/libfwnt) | Library for Windows NT data types including LZXPRESS Huffman decompression | 58 | 🟢 | C |
| [libmdmp](https://github.com/libyal/libmdmp) | Library and tools for the Windows Minidump (MDMP) format | 45 | 🟢 | C |
| [ExtensionBlocks](https://github.com/EricZimmerman/ExtensionBlocks) | Parser for shell item extension blocks found in ShellBags | 26 | 🟢 | C# |
| [mac_alias](https://github.com/dmgbuild/mac_alias) | Generates and parses macOS Alias and Bookmark records in Python | 26 | 🟢 | Python |
| [RustyUsn](https://github.com/forensicmatt/RustyUsn) | Rust parser that converts NTFS USN journal records to JSON | 22 | 🔴 | Rust |
| [go-prefetch](https://github.com/Velocidex/go-prefetch) | Go parser for Windows Prefetch files | 20 | 🟢 | Go |
| [regparser](https://github.com/Velocidex/regparser) | Go parser for Windows registry hives | 20 | 🟡 | Go |
| [libmsiecf](https://github.com/libyal/libmsiecf) | Library for Internet Explorer cache (index.dat) files | 19 | 🟢 | C |
| [libfwevt](https://github.com/libyal/libfwevt) | Library for Windows XML Event Log (EVTX) binary XML data types | 18 | 🟢 | C |
| [libwtcdb](https://github.com/libyal/libwtcdb) | Library for the Windows Explorer thumbnail cache database (thumbcache) format | 16 | 🟢 | C |
| [libagdb](https://github.com/libyal/libagdb) | Library for the Windows SuperFetch database format | 13 | 🟢 | C |
| [libftxf](https://github.com/libyal/libftxf) | Library for Transactional NTFS (TxF) data types | 8 | 🟢 | C |
| [libmapidb](https://github.com/libyal/libmapidb) | Library for the Exchange MAPI database format | 7 | 🟢 | C |
| [libfwps](https://github.com/libyal/libfwps) | Library for Windows Property Store data types | 6 | 🟢 | C |
| [dissect.cim](https://github.com/fox-it/dissect.cim) | Python parser for the Windows WMI CIM repository database | 5 | 🟢 | Python |
| [dissect.etl](https://github.com/fox-it/dissect.etl) | Python parser for Windows Event Trace Log (ETL) files | 5 | 🟢 | Python |
| [libcreg](https://github.com/libyal/libcreg) | Library for the Windows 9x/Me registry (CREG) file format | 5 | 🟢 | C |
| [dissect.regf](https://github.com/fox-it/dissect.regf) | Python parser for the Windows registry hive format | 4 | 🟢 | Python |
| [libnk2](https://github.com/libyal/libnk2) | Library for the Microsoft Outlook Nickfile (NK2) format | 4 | 🟢 | C |
| [libwrc](https://github.com/libyal/libwrc) | Library for the Windows Resource Compiler (WRC) resource format | 4 | 🟢 | C |
| [dissect.shellitem](https://github.com/fox-it/dissect.shellitem) | Python parser for Windows Shell Item structures | 3 | 🟢 | Python |
| [dissect.thumbcache](https://github.com/fox-it/dissect.thumbcache) | Python parser for Windows thumbcache databases | 3 | 🟢 | Python |
| [libpst](https://www.five-ten-sg.com/libpst/) | Library and readpst tool for reading Microsoft Outlook PST files |  | ⚪ |  |
| [msitools](https://gitlab.gnome.org/GNOME/msitools) | Tools to inspect and build Windows Installer (.MSI) files on Linux |  | ⚪ |  |
