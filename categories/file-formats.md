# File Formats

[← All categories](../README.md) · 200 projects

- [Audio & Music Production](#audio--music-production) (8)
- [Camera RAW & Video Metadata](#camera-raw--video-metadata) (10)
- [Databases](#databases) (8)
- [Design Tools (PSD, Sketch, Figma, Affinity)](#design-tools-psd-sketch-figma-affinity) (9)
- [E-books](#e-books) (4)
- [EDA & PCB](#eda--pcb) (5)
- [Filesystems & Archives](#filesystems--archives) (30)
- [Format Description Tools](#format-description-tools) (7)
- [Graphics & CAD](#graphics--cad) (27)
- [Maps & GIS](#maps--gis) (4)
- [Office & Documents](#office--documents) (39)
- [Other](#other) (1)
- [Windows & Forensic Artifacts](#windows--forensic-artifacts) (48)

## Audio & Music Production

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| alphaTab | Music notation and tab rendering library that imports Guitar Pro 3-8 files | 1,864 | <https://github.com/CoderLine/alphaTab> |
| TuxGuitar | Open-source tablature editor with Guitar Pro and Power Tab importers | 1,556 | <https://github.com/helge17/tuxguitar> |
| PyGuitarPro | Reads, writes and manipulates Guitar Pro GP3/GP4/GP5 tablature files | 370 | <https://github.com/Perlence/PyGuitarPro> |
| Crate Digger | Java library for parsing Pioneer rekordbox export databases and track analysis files | 235 | <https://github.com/Deep-Symmetry/crate-digger> |
| PyFLP | Parser and editor for FL Studio project (.flp) files | 218 | <https://github.com/demberto/PyFLP> |
| rekordcrate | Rust library for parsing Pioneer rekordbox device exports | 212 | <https://github.com/Holzhaus/rekordcrate> |
| ptformat | Parser for Avid Pro Tools session files, used by Ardour for import | 94 | <https://github.com/zamaudio/ptformat> |
| serato-tags | Documentation and parsers for Serato DJ Pro GEOB metadata tags | 93 | <https://github.com/Holzhaus/serato-tags> |

## Camera RAW & Video Metadata

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| ExifTool | Metadata reader/writer with extensive reverse-engineered camera maker notes | 5,146 | <https://github.com/exiftool/exiftool> |
| LibRaw | Library for decoding RAW files from hundreds of digital camera models | 1,601 | <https://github.com/LibRaw/LibRaw> |
| Exiv2 | C++ image metadata library including proprietary maker note decoding | 1,166 | <https://github.com/Exiv2/exiv2> |
| dnglab | Converts camera RAW files to DNG with its own reverse-engineered decoders (Rust) | 692 | <https://github.com/dnglab/dnglab> |
| rawspeed | Fast camera RAW decoding library used by darktable | 458 | <https://github.com/darktable-org/rawspeed> |
| MLV-App | Processing app for Magic Lantern MLV raw video files | 351 | <https://github.com/ilia3101/MLV-App> |
| canon_cr3 | Reverse-engineered description of the Canon CR3 RAW file format | 329 | <https://github.com/lclevy/canon_cr3> |
| dji-log-parser | Rust library that parses records from DJI flight log .txt files | 123 | <https://github.com/lvauvillier/dji-log-parser> |
| DJI_SRT_Parser | Parses telemetry from DJI drone SRT metadata files | 55 | <https://github.com/JuanIrache/DJI_SRT_Parser> |
| DatCon | Converts DJI drone .DAT flight logs to CSV and KML | 32 | <https://github.com/BudWalkerJava/DatCon> |

## Databases

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| pyreadstat | Python package to read/write SAS, SPSS and Stata files (wraps ReadStat) | 428 | <https://github.com/Roche/pyreadstat> |
| ReadStat | C library and CLI for reading SAS, Stata and SPSS data files, including reverse-engineered SAS7BDAT | 310 | <https://github.com/WizardMac/ReadStat> |
| dbfread | Python library for reading dBase/FoxPro DBF files | 244 | <https://github.com/olemb/dbfread> |
| OrcaMDF | C# parser that reads SQL Server MDF data files without SQL Server | 190 | <https://github.com/improvedk/OrcaMDF> |
| Jackcess | Pure Java library for reading and writing Microsoft Access (.mdb/.accdb) databases | 122 | <https://github.com/jahlborn/jackcess> |
| fmptools | Converts FileMaker Pro databases (.fp5/.fp7/.fmp12) to open formats | 103 | <https://github.com/evanmiller/fmptools> |
| Parso | Lightweight Java library for reading SAS7BDAT datasets | 80 | <https://github.com/epam/parso> |
| go-ese | Go parser for the Microsoft Extensible Storage Engine (ESE/JET Blue) database | 32 | <https://github.com/Velocidex/go-ese> |

## Design Tools (PSD, Sketch, Figma, Affinity)

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| psd.js | Photoshop PSD parser for Node.js and browsers | 2,842 | <https://github.com/meltingice/psd.js> |
| ag-psd | JavaScript library for reading and writing Photoshop PSD files, including layers and effects | 728 | <https://github.com/Agamnentzar/ag-psd> |
| psd (Rust) | Rust crate for parsing Photoshop PSD files and their layers | 284 | <https://github.com/chinedufn/psd> |
| fig2sketch | Converts Figma .fig files into Sketch documents by parsing the undocumented .fig format | 171 | <https://github.com/sketch-hq/fig2sketch> |
| psd (Go) | PSD/PSB Photoshop file reader for Go | 159 | <https://github.com/oov/psd> |
| libsai | Library for reading the encrypted PaintTool SAI .sai file format | 130 | <https://github.com/Wunkolo/libsai> |
| aftereffects-aep-parser | Unofficial Go parser for Adobe After Effects .aep project files | 129 | <https://github.com/boltframe/aftereffects-aep-parser> |
| pytoshop | Python library for reading and writing Photoshop PSD and PSB files | 128 | <https://github.com/mdboom/pytoshop> |
| clip_to_psd | Converts Clip Studio Paint .clip files to PSD by reading the proprietary .clip container | 83 | <https://github.com/dobrokot/clip_to_psd> |

## E-books

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| calibre | E-book manager with readers for many proprietary formats (MOBI, LIT, LRF, PDB, KFX via plugin) | 26,121 | <https://github.com/kovidgoyal/calibre> |
| libmobi | C library for handling Kindle MOBI/AZW3/KF8 e-book formats | 483 | <https://github.com/bfabiszewski/libmobi> |
| mobi | Python library to unpack Kindle (kindlegen) e-books | 78 | <https://github.com/iscc/mobi> |
| libe-book | Document Liberation library for legacy e-book formats (eReader, Plucker, TealDoc, LRF and more) |  | <https://sourceforge.net/projects/libebook> |

## EDA & PCB

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| OpenBoardView | Viewer for proprietary laptop/phone boardview files (.brd, .bdv, .fz and others) | 1,857 | <https://github.com/OpenBoardView/OpenBoardView> |
| altium2kicad *(archived)* | Converts Altium PCB and schematic files to KiCad | 955 | <https://github.com/thesourcerer8/altium2kicad> |
| altium.js | Browser-based parser and renderer for Altium SchDoc schematics | 143 | <https://github.com/gsuberland/altium_js> |
| OpenOrCadParser *(archived)* | FOSS parser for Cadence OrCAD Capture binary design files | 69 | <https://github.com/Werni2A/OpenOrCadParser> |
| Altium-Schematic-Parser | Converts Altium .SchDoc files to JSON | 52 | <https://github.com/a3ng7n/Altium-Schematic-Parser> |

## Filesystems & Archives

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| android-backup-extractor | Unpacks and repacks Android adb backup (.ab) files | 2,599 | <https://github.com/nelenkov/android-backup-extractor> |
| apfs-fuse | FUSE driver for reading Apple APFS volumes | 2,159 | <https://github.com/sgan81/apfs-fuse> |
| dislocker | FUSE driver to read/write BitLocker-encrypted volumes on Linux/macOS | 1,939 | <https://github.com/Aorimn/dislocker> |
| lessmsi | Views and extracts the contents of Windows Installer (.msi) files | 1,765 | <https://github.com/activescott/lessmsi> |
| NTFS-3G | Read/write NTFS driver for Linux/macOS | 1,511 | <https://github.com/tuxera/ntfs-3g> |
| innoextract | Unpacks installers created by Inno Setup without running them | 1,382 | <https://github.com/dscharrer/innoextract> |
| exfat (relan) | Free FUSE exFAT implementation, written before Microsoft published the spec | 886 | <https://github.com/relan/exfat> |
| linux-apfs-rw | Linux kernel APFS module with experimental write support | 802 | <https://github.com/linux-apfs/linux-apfs-rw> |
| unshield | Extracts CAB files from InstallShield installers | 436 | <https://github.com/twogood/unshield> |
| libfsapfs | Library and tools to access Apple File System (APFS) | 427 | <https://github.com/libyal/libfsapfs> |
| libbde | Library and tools for BitLocker Drive Encryption volumes | 260 | <https://github.com/libyal/libbde> |
| libevtx | Library and tools for Windows XML Event Log (EVTX) format | 242 | <https://github.com/libyal/libevtx> |
| libfsntfs | Library and tools to access NTFS | 239 | <https://github.com/libyal/libfsntfs> |
| wimlib | Library and tools for the Windows Imaging Format (WIM), including its proprietary compression | 219 | <https://github.com/ebiggers/wimlib> |
| libmspack | Library for Microsoft compression formats: CAB, CHM, HLP, LIT, KWAJ, SZDD | 215 | <https://github.com/kyz/libmspack> |
| dtformats | Collection of data formats | 201 | <https://github.com/libyal/dtformats> |
| libfsrefs | Library and tools to access Microsoft ReFS | 200 | <https://github.com/libyal/libfsrefs> |
| libregf | Library and tools for the Windows NT Registry file (REGF) format | 141 | <https://github.com/libyal/libregf> |
| XADMaster | Unarchiver engine supporting StuffIt, DiskDoubler, Compact Pro and many legacy archive formats | 135 | <https://github.com/MacPaw/XADMaster> |
| libvshadow | Library and tools for Windows Volume Shadow Snapshot (VSS) format | 119 | <https://github.com/libyal/libvshadow> |
| synology-decrypt | Open implementation/description of Synology Cloud Sync encryption format | 105 | <https://github.com/marnix/synology-decrypt> |
| apfs.ksy *(archived)* | APFS filesystem format for Kaitai Struct | 82 | <https://github.com/cugu/apfs.ksy> |
| go-ntfs | Pure Go NTFS file system parser | 76 | <https://github.com/Velocidex/go-ntfs> |
| titl | Tools for iTunes Libraries | 66 | <https://github.com/josephw/titl> |
| encrypteddmg | Tool for analyzing and decrypting apple encrypted disk images | 45 | <https://github.com/nlitsme/encrypteddmg> |
| rsrcfork | Pure Python reader for classic Macintosh resource forks | 32 | <https://github.com/dgelessus/python-rsrcfork> |
| libmodi | Library for Mac OS disk image formats (UDIF, sparse image, sparse bundle) | 22 | <https://github.com/libyal/libmodi> |
| bom | Apple iOS / macOS Assets.car decoder, write in golang | 18 | <https://github.com/iineva/bom> |
| libitlp *(archived)* | iTunes "itl" database parsing | 17 | <https://github.com/jeanthom/libitlp> |
| libphdi | Library for the Parallels Hard Disk image format | 6 | <https://github.com/libyal/libphdi> |

## Format Description Tools

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| ImHex | Hex editor for reverse engineers with a pattern language for binary formats | 55,051 | <https://github.com/WerWolv/ImHex> |
| Kaitai Struct | Declarative language to describe binary formats and generate parsers | 4,696 | <https://github.com/kaitai-io/kaitai_struct> |
| ImHex-Patterns | Pattern files describing many binary file formats for ImHex | 1,032 | <https://github.com/WerWolv/ImHex-Patterns> |
| Kaitai Struct Formats | Library of .ksy descriptions of hundreds of binary file formats | 798 | <https://github.com/kaitai-io/kaitai_struct_formats> |
| serum-preset-packager | Reverse-engineered Serum 2 synth preset format; converts to/from JSON | 67 | <https://github.com/KennethWussmann/serum-preset-packager> |
| murmelbahn | Reverse-engineered Gravitrax marble run course file format | 8 | <https://github.com/lfrancke/murmelbahn> |
| remus-rlf-reader | Reverse-engineered RLF log format of REMUS underwater drones | 1 | <https://github.com/isaacgerg/remus-rlf-reader> |

## Graphics & CAD

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| AssetStudio *(archived)* | Explore and extract Unity assets and assetbundles | 15,588 | <https://github.com/Perfare/AssetStudio> |
| Assimp | Asset importer for 40+ 3D formats, including proprietary FBX, 3DS and Blender files | 13,258 | <https://github.com/assimp/assimp> |
| FModel | Unreal Engine archive (.pak/.utoc) explorer | 3,234 | <https://github.com/4sval/FModel> |
| psd.rb | Parse Photoshop PSD files in Ruby | 3,115 | <https://github.com/layervault/psd.rb> |
| LibreDWG | GNU library to read and write Autodesk DWG CAD files | 1,620 | <https://github.com/LibreDWG/libredwg> |
| psd-tools | Python package for reading Adobe Photoshop PSD files | 1,475 | <https://github.com/psd-tools/psd-tools> |
| ufbx | Single-file loader for Autodesk FBX files | 1,414 | <https://github.com/ufbx/ufbx> |
| @webtoon/psd | Fast zero-dependency PSD parser for the web and Node.js | 1,351 | <https://github.com/webtoon/psd> |
| OpenFBX | Lightweight open source FBX importer | 1,351 | <https://github.com/nem0/OpenFBX> |
| CUE4Parse | C# parser for Unreal Engine 4/5 archives and assets | 653 | <https://github.com/FabianFG/CUE4Parse> |
| figma-to-json | Reads and writes Figma's binary .fig (Kiwi) files as JSON | 332 | <https://github.com/yagudaev/figma-to-json> |
| SWFTools | Utilities for editing and generating Adobe Flash SWF files | 308 | <https://github.com/swftools/swftools> |
| libdxfrw | C++ library to read/write DXF and read AutoCAD DWG files, used by LibreCAD | 294 | <https://github.com/LibreCAD/libdxfrw> |
| UniConvertor | Universal vector graphics translator with reverse-engineered CorelDRAW CDR/CMX importers | 177 | <https://github.com/sk1-project/uniconvertor> |
| InventorLoader | FreeCAD workbench that imports Autodesk Inventor files | 169 | <https://github.com/jmplonka/InventorLoader> |
| libredwg-web | WebAssembly/JavaScript DWG/DXF parser built on LibreDWG | 81 | <https://github.com/mlightcad/libredwg-web> |
| warcraft-rs | Unified CLI tool for World of Warcraft file formats. Integrates file format libraries for parsing, conversion, and va... | 63 | <https://github.com/wowemulation-dev/warcraft-rs> |
| swf-parser | Rust and TypeScript parsers for the SWF format | 33 | <https://github.com/open-flash/swf-parser> |
| 3mf-to-glb | Reverse-engineered Bambu/Orca 3MF multi-color format; converts to GLB keeping colors | 23 | <https://github.com/SamiSalah221/3mf-to-glb> |
| libcdr | Parser for CorelDRAW documents | 20 | <https://github.com/LibreOffice/libcdr> |
| wow_dbc | Rust library for reading and writing World of Warcraft 1.12, 2.4.3 and 3.3.5 DBC files. | 16 | <https://github.com/gtker/wow_dbc> |
| image-blp | Tool to encode/decode Blizzard BLP textures for Rust language | 10 | <https://github.com/zloy-tulen/image-blp> |
| arw6_decode | Reverse-engineered Sony ARW6 (LLVC v3) RAW image decoder | 4 | <https://github.com/abbradar/arw6_decode> |
| worgen-rs | worgen-rs | 4 | <https://github.com/nocthir/worgen-rs> |
| wow_chunky | A pure Rust parsing library for World of Warcraft's chunked files (and some additional binary files), targeting versi... | 1 | <https://github.com/bigglesss/wow_chunky> |
| libwpg | Library to read WordPerfect Graphics (.wpg) images |  | <https://sourceforge.net/projects/libwpg> |
| libzmf | Document Liberation library for Zoner Callisto/Draw (.zmf) vector drawings |  | <https://git.libreoffice.org/libzmf> |

## Maps & GIS

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| GDAL | Geospatial format library including the reverse-engineered OpenFileGDB and MapInfo drivers | 6,093 | <https://github.com/OSGeo/gdal> |
| GPSBabel | Converts between many proprietary GPS formats (Garmin, Magellan, OziExplorer, TomTom) | 552 | <https://github.com/GPSBabel/gpsbabel> |
| SLYR | Converts Esri LYR, MXD, style and other ArcGIS files to QGIS | 250 | <https://github.com/north-road/slyr> |
| dump_gdbtable | Script and reverse-engineered spec for Esri File Geodatabase .gdbtable files | 153 | <https://github.com/rouault/dump_gdbtable> |

## Office & Documents

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| SheetJS | Spreadsheet toolkit reading XLS, XLSB, Lotus, Quattro Pro and many legacy formats | 36,347 | <https://github.com/SheetJS/sheetjs> |
| LibreOffice | Office suite with import filters for reverse-engineered MS Office and other formats | 4,492 | <https://github.com/LibreOffice/core> |
| oletools | Python tools to analyze MS OLE2 files and Office documents | 3,428 | <https://github.com/decalage2/oletools> |
| Apache POI | Java API for Microsoft binary and OOXML Office formats | 2,276 | <https://github.com/apache/poi> |
| xlrd | Python library for reading legacy Excel BIFF (.xls) files | 2,206 | <https://github.com/python-excel/xlrd> |
| hwp.js | Open-source web viewer and parser for Hancom HWP documents | 1,306 | <https://github.com/hahnlee/hwp.js> |
| MDB Tools | Read Microsoft Access databases on Unix | 1,177 | <https://github.com/mdbtools/mdbtools> |
| KindleUnpack | Unpacks Amazon Kindle/Kindlegen MOBI/AZW3 ebooks | 1,101 | <https://github.com/kevinhendricks/KindleUnpack> |
| msg-extractor | Extracts emails and attachments from Outlook .msg files | 852 | <https://github.com/TeamMsgExtractor/msg-extractor> |
| apple_cloud_notes_parser | Parser for Apple Notes databases from iOS/macOS backups | 543 | <https://github.com/threeplanetssoftware/apple_cloud_notes_parser> |
| libesedb | Library and tools for Extensible Storage Engine (ESE/EDB) databases | 381 | <https://github.com/libyal/libesedb> |
| libpff | Library and tools for Outlook PFF/OFF (PST/OST) files | 370 | <https://github.com/libyal/libpff> |
| MPXJ | Reads Microsoft Project MPP files and other schedule formats (Primavera, Asta, Phoenix) | 350 | <https://github.com/joniles/mpxj> |
| pyhwp | Python parser for Hancom HWP v5 word processor files | 301 | <https://github.com/mete0r/pyhwp> |
| java-libpst | Pure Java library for reading Outlook PST files | 274 | <https://github.com/rjohnsondev/java-libpst> |
| olefile | Python package to parse, read and write Microsoft OLE2/Compound File Binary files | 274 | <https://github.com/decalage2/olefile> |
| iWorkFileFormat | Documentation of the reverse-engineered iWork '13 file format | 273 | <https://github.com/obriensp/iWorkFileFormat> |
| CHMLib | Library for reading Microsoft ITSS/CHM compiled help files | 268 | <https://github.com/jedwing/CHMLib> |
| hwp-rs | Rust parser and tools for Hancom HWP documents | 232 | <https://github.com/hahnlee/hwp-rs> |
| pyOneNote | Python parser for OneNote .one files that extracts embedded objects | 153 | <https://github.com/DissectMalware/pyOneNote> |
| onenote.rs | Rust parser for Microsoft OneNote .one/.onetoc2 files (MS-ONESTORE) | 86 | <https://github.com/msiemens/onenote.rs> |
| libolecf | Library and tools for the OLE 2 Compound File format | 80 | <https://github.com/libyal/libolecf> |
| pychm | Python bindings for CHMLib to read Microsoft CHM help files | 58 | <https://github.com/dottedmag/pychm> |
| kindling | Reverse-engineered kindlegen MOBI/KF8 builder in Rust, ~7,000x faster | 57 | <https://github.com/ciscoriordan/kindling> |
| libpst | Library for reading Microsoft Outlook PST files | 51 | <https://github.com/pst-format/libpst> |
| libvisio | Parser for Microsoft Visio file formats (re-lab reverse engineering) | 47 | <https://github.com/LibreOffice/libvisio> |
| stackimport | Reads HyperCard stacks and converts them to XML and images | 43 | <https://github.com/uliwitness/stackimport> |
| libetonyek | Parser for Apple Keynote, Pages and Numbers documents | 19 | <https://github.com/LibreOffice/libetonyek> |
| libmspub | Parser for Microsoft Publisher documents | 14 | <https://github.com/LibreOffice/libmspub> |
| libfole | Library for Object Linking and Embedding (OLE) data types | 13 | <https://github.com/libyal/libfole> |
| libstaroffice | Import filter for legacy binary StarOffice/StarWriter/StarCalc documents | 8 | <https://github.com/fosnola/libstaroffice> |
| OpenJTD rjtd | Reverse-engineered Ichitaro JTD/JTT word processor format; Rust reader/renderer | 7 | <https://github.com/OpenJTD/rjtd> |
| parser-for-goodnotes | Parser for the closed GoodNotes document format, reverse-engineered with LLMs | 7 | <https://github.com/Kaih1825/parser-for-goodnotes> |
| libabw | Document Liberation library that reads AbiWord documents (GitHub mirror) | 5 | <https://github.com/LibreOffice/libabw> |
| libmwaw | Imports many legacy Mac document formats (MacWrite, ClarisWorks, MacDraw, WriteNow and more) |  | <https://sourceforge.net/projects/libmwaw> |
| libpagemaker | Document Liberation library that imports Adobe/Aldus PageMaker documents |  | <https://git.libreoffice.org/libpagemaker> |
| libqxp | Document Liberation library that imports QuarkXPress 3.1-4.1 documents |  | <https://git.libreoffice.org/libqxp> |
| libwpd | Library for importing reverse-engineered WordPerfect documents |  | <https://sourceforge.net/projects/libwpd> |
| libwps | Imports Microsoft Works, Lotus 1-2-3, Quattro Pro and other legacy DOS/Windows documents |  | <https://sourceforge.net/projects/libwps> |

## Other

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| OpenJOC | Independent clean-room E-AC-3 JOC decoder in Rust, with OAMD metadata and reconstruction-basis decoding. | 223 | <https://github.com/chyinan/OpenJOC> |

## Windows & Forensic Artifacts

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| ALEAPP | Android Logs, Events and Protobuf Parser for app databases and artifacts | 994 | <https://github.com/abrignoni/ALEAPP> |
| evtx (Rust) | Fast, safe Rust parser for the Windows XML Event Log (EVTX) format | 966 | <https://github.com/omerbenamram/evtx> |
| python-evtx | Pure Python parser for Windows XML Event Log (.evtx) files | 781 | <https://github.com/williballenthin/python-evtx> |
| srum-dump | Converts the Windows SRUM (System Resource Usage Monitor) database to spreadsheets | 766 | <https://github.com/MarkBaggett/srum-dump> |
| RegRipper 3.0 | Plugin-based extraction of data from Windows registry hives | 723 | <https://github.com/keydet89/RegRipper3.0> |
| Python-dsstore | Parses macOS .DS_Store files and extracts file names | 507 | <https://github.com/gehaxelt/Python-dsstore> |
| python-registry | Pure Python parser for Windows Registry hive files | 448 | <https://github.com/williballenthin/python-registry> |
| flare-wmi *(archived)* | Parser and tools for the undocumented WMI CIM repository format | 434 | <https://github.com/mandiant/flare-wmi> |
| evtx (Zimmerman) | C# EVTX event log parser with extra maps | 376 | <https://github.com/EricZimmerman/evtx> |
| LECmd | Command-line parser for Windows LNK shortcut files | 349 | <https://github.com/EricZimmerman/LECmd> |
| MFTECmd | Parser for NTFS $MFT, $J, $Boot and $SDS | 340 | <https://github.com/EricZimmerman/MFTECmd> |
| WMI_Forensics | Scripts to parse the WMI CIM repository for persistence artifacts | 320 | <https://github.com/davidpany/WMI_Forensics> |
| libewf | Library for the EnCase Expert Witness Compression Format (EWF/E01) disk images | 318 | <https://github.com/libyal/libewf> |
| PECmd | Windows Prefetch file parser | 308 | <https://github.com/EricZimmerman/PECmd> |
| FSEventsParser | Parser for macOS/iOS FSEvents logs | 283 | <https://github.com/dlcowen/FSEventsParser> |
| ShimCacheParser *(archived)* | Parses the Windows Application Compatibility Cache from registry hives | 279 | <https://github.com/mandiant/ShimCacheParser> |
| regipy | OS-independent Python library for parsing offline Windows registry hives | 277 | <https://github.com/mkorman90/regipy> |
| Registry (Zimmerman) | Full-featured offline Windows Registry parser in C# | 260 | <https://github.com/EricZimmerman/Registry> |
| INDXParse | Tools for NTFS INDX records and other NTFS artifacts | 228 | <https://github.com/williballenthin/INDXParse> |
| liblnk | Library and tools for the Windows Shortcut (LNK) file format | 219 | <https://github.com/libyal/liblnk> |
| Thumbcache Viewer | Extracts images from Windows thumbcache and thumbs.db databases | 171 | <https://github.com/thumbcacheviewer/thumbcacheviewer> |
| mft (Rust) | Rust parser for the NTFS Master File Table ($MFT) | 162 | <https://github.com/omerbenamram/mft> |
| shellbags | Cross-platform parser for Windows ShellBag registry artifacts | 160 | <https://github.com/williballenthin/shellbags> |
| etl-parser | Pure Python parser for Windows Event Trace Log (ETL) files | 157 | <https://github.com/airbus-cert/etl-parser> |
| rifiuti2 | Analyses Windows Recycle Bin INFO2 and $I files | 156 | <https://github.com/abelcheung/rifiuti2> |
| BitsParser | Parses Windows BITS database files and job records | 152 | <https://github.com/fireeye/BitsParser> |
| LnkParse3 | Python parser for Windows LNK shortcut files | 145 | <https://github.com/Matmaus/LnkParse3> |
| yarp | Yet Another Registry Parser: Windows registry hive parser with transaction log recovery | 141 | <https://github.com/msuhanov/yarp> |
| spotlight_parser | Reads macOS Spotlight store.db databases | 137 | <https://github.com/ydkhatri/spotlight_parser> |
| AppCompatCacheParser | Parser for the Windows AppCompatCache (ShimCache) | 129 | <https://github.com/EricZimmerman/AppCompatCacheParser> |
| JLECmd | Parser for Windows Automatic and Custom Destinations jump lists | 124 | <https://github.com/EricZimmerman/JLECmd> |
| Windows-Prefetch-Parser | Parses Windows Prefetch files from XP to Windows 10 | 123 | <https://github.com/PoorBillionaire/Windows-Prefetch-Parser> |
| USN-Journal-Parser | Python script to parse the NTFS USN change journal | 119 | <https://github.com/PoorBillionaire/USN-Journal-Parser> |
| Lnk | C# library for parsing Windows LNK shortcut files | 99 | <https://github.com/EricZimmerman/Lnk> |
| ds_store | Python library to read and write Finder .DS_Store files | 95 | <https://github.com/dmgbuild/ds_store> |
| libscca | Library and tools for the Windows Prefetch (SCCA) file format | 90 | <https://github.com/libyal/libscca> |
| libfwsi | Library for the Windows Shell Item format used in ShellBags and LNK files | 75 | <https://github.com/libyal/libfwsi> |
| bits_parser | Extracts BITS jobs from Windows QMGR queue files | 74 | <https://github.com/ANSSI-FR/bits_parser> |
| libevt | Library and tools for the legacy Windows Event Log (EVT) format | 60 | <https://github.com/libyal/libevt> |
| libfwnt | Library for Windows NT data types including LZXPRESS Huffman decompression | 58 | <https://github.com/libyal/libfwnt> |
| ExtensionBlocks | Parser for shell item extension blocks found in ShellBags | 26 | <https://github.com/EricZimmerman/ExtensionBlocks> |
| libmsiecf | Library for Internet Explorer cache (index.dat) files | 19 | <https://github.com/libyal/libmsiecf> |
| libwtcdb | Library for the Windows Explorer thumbnail cache database (thumbcache) format | 16 | <https://github.com/libyal/libwtcdb> |
| libagdb | Library for the Windows SuperFetch database format | 13 | <https://github.com/libyal/libagdb> |
| libmapidb | Library for the Exchange MAPI database format | 7 | <https://github.com/libyal/libmapidb> |
| libcreg | Library for the Windows 9x/Me registry (CREG) file format | 5 | <https://github.com/libyal/libcreg> |
| libnk2 | Library for the Microsoft Outlook Nickfile (NK2) format | 4 | <https://github.com/libyal/libnk2> |
| libwrc | Library for the Windows Resource Compiler (WRC) resource format | 4 | <https://github.com/libyal/libwrc> |
