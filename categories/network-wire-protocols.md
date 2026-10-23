# Network & Wire Protocols

[← All categories](../README.md#whats-inside) · [Search this category on the website](https://alexgaoth.github.io/awesome-reverse-engineered/#c=network-wire-protocols) · 426 projects · [Listed here? Get the badge](../README.md#is-your-project-listed)

Health: 🟢 pushed in the last year · 🟡 1 to 3 years · 🔴 over 3 years · 🗄️ archived · ⚪ unknown

- [Aviation & Marine](#aviation--marine) (33)
- [Casting & TV Remotes](#casting--tv-remotes) (42)
- [Cellular Modem Diagnostics](#cellular-modem-diagnostics) (26)
- [Digital Voice Radio](#digital-voice-radio) (14)
- [Email & Groupware](#email--groupware) (26)
- [File Sharing & Remote Desktop](#file-sharing--remote-desktop) (29)
- [Legacy IM Revival](#legacy-im-revival) (2)
- [Messaging Protocols](#messaging-protocols) (22)
- [Other Protocols](#other-protocols) (18)
- [Proprietary Enterprise Protocols](#proprietary-enterprise-protocols) (47)
- [Radio & SDR Protocols](#radio--sdr-protocols) (63)
- [Satellite Downlinks](#satellite-downlinks) (32)
- [Sub-GHz Sensors & Meters](#sub-ghz-sensors--meters) (49)
- [VPN Clients](#vpn-clients) (23)

## Aviation & Marine

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [SoftRF](https://github.com/lyusupov/SoftRF) | DIY aviation proximity system interoperable with FLARM, OGN, P3I, FANET and other protocols | 1,030 | 🟢 | C |
| [canboat](https://github.com/canboat/canboat) | NMEA 2000 tools with a PGN database that reverse engineers proprietary marine PGNs | 664 | 🟢 | Rust |
| [RemoteIDReceiver](https://github.com/cyber-defence-campus/RemoteIDReceiver) | Monitor drones via Remote ID over Wi-Fi/BLE, incl. DJI proprietary DroneID frames | 317 | 🟢 | Python |
| [dump978 (mutability)](https://github.com/mutability/dump978) | Demodulator and decoder for 978 MHz UAT aviation transmissions | 182 | 🗄️ | C |
| [dumphfdl](https://github.com/szpajder/dumphfdl) | Multichannel decoder for HF Data Link (HFDL) aircraft messages | 162 | 🟢 | C |
| [libacars](https://github.com/szpajder/libacars) | Library decoding ACARS payloads such as FANS-1/A, MIAM and other airline applications | 156 | 🟢 | C |
| [antsdr_dji_droneid](https://github.com/alphafox02/antsdr_dji_droneid) | ANTSDR E200 firmware detecting DJI DroneID broadcasts with network output | 127 | 🗄️ | Python |
| [canboatjs](https://github.com/canboat/canboatjs) | TypeScript NMEA 2000 parser/encoder built on the canboat reverse-engineered PGN database | 119 | 🟢 | TypeScript |
| [radar_pi](https://github.com/opencpn-radar-pi/radar_pi) | OpenCPN plugin for Navico, Garmin and Raymarine radars via reverse-engineered protocols | 108 | 🟢 | C |
| [PINGMapper](https://github.com/CameronBodine/PINGMapper) | Processes Humminbird and Lowrance side-scan sonar recordings from proprietary log formats | 98 | 🟢 | Python |
| [rtl_acars_ng](https://github.com/gat3way/rtl_acars_ng) | Simple console ACARS decoder for RTL-SDR | 83 | 🔴 | C |
| [Seatalk-Autopilot-Remote-Control](https://github.com/AK-Homberger/Seatalk-Autopilot-Remote-Control) | Arduino remote that drives Raymarine autopilots over the proprietary SeaTalk1 bus | 76 | 🟡 | C++ |
| [PyHum](https://github.com/BenthicSubstrateMapping/PyHum) | Reads and analyses Humminbird side-scan sonar files in proprietary DAT/SON format | 68 | 🔴 | Python |
| [acars-message-documentation](https://github.com/airframesio/acars-message-documentation) | Community notes decoding airline-specific ACARS free-text message formats | 57 | 🟢 |  |
| [samples2djidroneid](https://github.com/anarkiwi/samples2djidroneid) | Decode DJI DroneID packets from I/Q samples | 37 | 🟢 | Python |
| [STWirelessRemote](https://github.com/nauti-control/STWirelessRemote) | Wireless remote for Raymarine ST1000/ST2000 autopilots using SeaTalk | 35 | 🟡 | C++ |
| [mayara](https://github.com/keesverruijt/mayara) | Marine yacht radar server for Navico, Furuno, Raymarine radars using RE'd network protocols | 34 | 🗄️ |  |
| [MicronetToNMEA](https://github.com/Rodemfr/MicronetToNMEA) | Converts Raymarine Micronet wireless instrument radio traffic to NMEA 0183 | 34 | 🟢 | C++ |
| [RaymarineAPtoFakeNavicoAutoPilot](https://github.com/htool/RaymarineAPtoFakeNavicoAutoPilot) | Emulates a Navico AC12 autopilot over NMEA 2000 to drive a Raymarine pilot from B&G displays | 28 | 🔴 | JavaScript |
| [acars-decoder-typescript](https://github.com/airframesio/acars-decoder-typescript) | Decoder for airline-specific ACARS message labels and formats in TypeScript | 22 | 🟢 | TypeScript |
| [ogn-rf](https://github.com/glidernet/ogn-rf) | Open Glider Network receiver that listens to glider tracker radio messages | 22 | 🔴 | C++ |
| [bt-sensors-plugin-sk](https://github.com/naugehyde/bt-sensors-plugin-sk) | Signal K plugin decoding many proprietary Bluetooth sensors (Victron, Renogy, BMS, tank sensors) | 21 | 🟢 | JavaScript |
| [OGN Tracker](https://github.com/pjalocha/ogn-tracker) | Open Glider Network tracker firmware with OGN/FLARM-compatible radio protocol | 20 | 🟢 | C++ |
| [sonaR](https://github.com/KennethTM/sonaR) | R package for reading Lowrance proprietary sonar log files | 17 | 🟡 | C++ |
| [seatalk (jamesroscoe)](https://github.com/jamesroscoe/seatalk) | Open-source library for the proprietary Raymarine SeaTalk protocol | 14 | 🔴 | C |
| [ClipperDuet2N2k](https://github.com/speters/ClipperDuet2N2k) | NASAmarine Clipper Duet echo sounder to NMEA2000 converter | 12 | 🟢 | C |
| [seatalk_wifi](https://github.com/atonizzo/seatalk_wifi) | Bridge from Raymarine SeaTalk to NMEA 0183 over Wi-Fi | 12 | 🔴 | C |
| [signalk-raymarine-autopilot](https://github.com/sbender9/signalk-raymarine-autopilot) | Signal K plugin controlling Raymarine autopilots with proprietary NMEA 2000 PGNs | 12 | 🗄️ | JavaScript |
| [dragonsdr_dji_droneid](https://github.com/alphafox02/dragonsdr_dji_droneid) | Detects DJI DroneID with DragonSDR and publishes it over ZMQ | 11 | 🟢 | Python |
| [RMRadar_pi](https://github.com/ab2nkovs/RMRadar_pi) | OpenCPN plugin for Raymarine digital radar via its undocumented network protocol | 11 | 🔴 | C |
| [parsefsh](https://github.com/rahra/parsefsh) | Decodes Raymarine ARCHIVE.FSH files and Garmin IMG/ADM archives | 10 | 🔴 | C |
| [metars_cgi](https://codeberg.org/PurpleJillybeans/metars_cgi) | Reverse-engineered data server for the NCAR Java METAR viewer |  | ⚪ |  |
| [trimpack](https://codeberg.org/jbnd/trimpack) | Utilities for Trimble Trimpack GPS receivers using their proprietary binary protocol |  | ⚪ |  |

## Casting & TV Remotes

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [miraclecast](https://github.com/albfan/miraclecast) | Miracast (Wi-Fi Display) sink and source implementation for Linux | 4,349 | 🟢 | C |
| [castnow](https://github.com/xat/castnow) | commandline chromecast player | 3,809 | 🗄️ | JavaScript |
| [catt](https://github.com/skorokithakis/catt) | Cast All The Things allows you to send videos from many, many online sources to your Chromecast. | 3,704 | 🟢 | Python |
| [go-chromecast](https://github.com/vishen/go-chromecast) | cli for Google Chromecast, Home devices and Cast Groups | 979 | 🟢 | Go |
| [ytcast](https://github.com/MarcoLucidi01/ytcast) | Casts YouTube videos to smart TVs from the command line via DIAL and Lounge API | 803 | 🟢 | Go |
| [node-castv2](https://github.com/thibauts/node-castv2) | An implementation of the Chromecast CASTV2 protocol | 793 | 🔴 | JavaScript |
| [samsungctl](https://github.com/Ape/samsungctl) | Remote control Samsung televisions via a TCP/IP connection | 741 | 🗄️ | Python |
| [node-sonos](https://github.com/bencevans/node-sonos) | Sonos Media Player Interface/Client | 723 | 🟢 | JavaScript |
| [homebridge-webos-tv](https://github.com/merdok/homebridge-webos-tv) | Homebridge plugin for LG webOS TVs | 707 | 🟢 | JavaScript |
| [homebridge-samsung-tizen](https://github.com/tavicu/homebridge-samsung-tizen) | Homebridge plugin for Samsung TV's with Tizen OS | 679 | 🟢 | TypeScript |
| [node-castv2-client](https://github.com/thibauts/node-castv2-client) | A Chromecast client based on the new (CASTV2) protocol | 657 | 🔴 | JavaScript |
| [adb_shell](https://github.com/JeffLIrion/adb_shell) | Pure Python implementation of the ADB protocol with shell and FileSync | 607 | 🟡 | Python |
| [ps4-waker](https://github.com/dhleong/ps4-waker) | Wakes and controls a PS4 over LAN using the PlayStation App protocol | 463 | 🔴 | JavaScript |
| [plex-mpv-shim](https://github.com/iwalton3/plex-mpv-shim) | Cast from Plex apps to MPV via the Plex player protocol | 412 | 🟡 | Python |
| [bscpylgtv](https://github.com/chros73/bscpylgtv) | Library to control webOS based LG TV devices | 367 | 🟢 | Roff |
| [python-roku](https://github.com/jcarbaugh/python-roku) | Screw remotes. Control your Roku with Python. | 349 | 🟢 | Python |
| [SharpCaster](https://github.com/Tapanila/SharpCaster) | Chromecast C# CLI and SDK | 336 | 🟡 | C# |
| [chromecast-java-api-v2](https://github.com/vitalidze/chromecast-java-api-v2) | Java implementation of ChromeCast V2 protocol client | 276 | 🟡 | Java |
| [lgtv.js](https://github.com/msloth/lgtv.js) | Control LG WebOS TV using node.js | 260 | 🔴 | JavaScript |
| [homebridge-harmony](https://github.com/nicoduj/homebridge-harmony) | Homebridge plugin for Logitech Harmony hubs over their undocumented websocket API | 224 | 🟢 | JavaScript |
| [samsung-tv-control](https://github.com/Toxblh/samsung-tv-control) | Remote control your TV via JS! | 197 | 🟡 | TypeScript |
| [python-androidtv](https://github.com/JeffLIrion/python-androidtv) | Communicate with an Android TV or Fire TV device via ADB over a network. | 196 | 🟡 | Python |
| [homebridge-lgwebos-tv](https://github.com/grzegorz914/homebridge-lgwebos-tv) | Homebridge plugin for LG WebOS TV, publish as independent external platform accessory. | 169 | 🟢 | JavaScript |
| [rust-cast](https://github.com/azasypkin/rust-cast) | Library written in Rust to communicate with the Google Cast devices | 159 | 🟢 | Rust |
| [playactor](https://github.com/dhleong/playactor) | Controls PS4/PS5 consoles over the PlayStation second-screen protocol | 157 | 🟢 | TypeScript |
| [GoogleCast](https://github.com/kakone/GoogleCast) | Implementation of the Google Cast protocol (.NET Standard 2.0 library) | 147 | 🟡 | C# |
| [androidtvremote2](https://github.com/tronikos/androidtvremote2) | Python library implementing the Android TV Remote protocol v2 | 135 | 🟢 | Python |
| [pyvizio](https://github.com/raman325/pyvizio) | Python client for Vizio SmartCast | 129 | 🟢 | Python |
| [lgtv-ip-control](https://github.com/WesSouza/lgtv-ip-control) | IP Control module for 2018+ LG TVs | 126 | 🟢 | TypeScript |
| [node-sonos-ts](https://github.com/svrooij/node-sonos-ts) | Sonos control library, use this library in your own appliction. | 111 | 🟢 | TypeScript |
| [spotcontrol](https://github.com/badfortrains/spotcontrol) | Open-source Spotify Connect controller in Go | 110 | 🔴 | Go |
| [androidtv-remote](https://github.com/louis49/androidtv-remote) | Node.js library implementing the Android TV Remote v2 pairing and remote protocol | 88 | 🔴 | JavaScript |
| [xbox-smartglass-csharp](https://github.com/OpenXbox/xbox-smartglass-csharp) | .NET Standard client library for the Xbox One SmartGlass protocol | 73 | 🔴 | C# |
| [sonos-api-docs](https://github.com/svrooij/sonos-api-docs) | Documentation and client generator for the Sonos local UPnP API | 60 | 🟢 | TypeScript |
| [aiowebostv](https://github.com/home-assistant-libs/aiowebostv) | Python library to control LG webOS based TV devices | 56 | 🟢 | Python |
| [aioharmony](https://github.com/Harmony-Libs/aioharmony) | Asyncio Python library for the Logitech Harmony Hub local protocol | 28 | 🟢 | Python |
| [EcpEmuServer](https://github.com/logantgt/EcpEmuServer) | Emulates a Roku ECP device so Harmony and similar remotes can trigger webhooks | 28 | 🟡 | C# |
| [go-cast](https://github.com/tristanpenman/go-cast) | An implementation of the Google Cast protocol, written in Go, with custom Chromecast Remote and Receiver apps | 24 | 🟢 | Go |
| [pylgnetcast](https://github.com/wokar/pylgnetcast) | Python client for LG NetCast (pre-webOS) TV remote control API | 13 | 🔴 | Python |
| [python-rokuecp](https://github.com/ctalkington/python-rokuecp) | Asynchronous Python client for Roku (ECP) | 9 | 🟢 | Python |
| [pybravia](https://github.com/Drafteed/pybravia) | Python async library for remote control of Sony Bravia TVs 2013 and newer. | 7 | 🟢 | Python |
| [sonos-websocket](https://github.com/jjlawren/sonos-websocket) | An asynchronous Python library to communicate with Sonos devices over websockets | 7 | 🟢 | Python |

## Cellular Modem Diagnostics

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [QCSuper](https://github.com/P1sec/QCSuper) | Capture 2G/3G/4G signaling from your own Qualcomm phone or modem via the DIAG protocol | 1,668 | 🟢 | Python |
| [FirmWire](https://github.com/FirmWire/FirmWire) | Full-system emulation of Samsung Shannon and MediaTek baseband firmware | 891 | 🟢 | Python |
| [SCAT](https://github.com/fgsect/scat) | Signaling collection from Qualcomm and Samsung Shannon modem diagnostic interfaces | 544 | 🟢 | Python |
| [xmm7360-pci](https://github.com/xmm7360/xmm7360-pci) | Reverse-engineered Linux driver for the Intel XMM7360 (Fibocom L850-GL) LTE modem | 486 | 🟡 | Python |
| [shannonRE](https://github.com/Comsecuris/shannonRE) | Scripts for reverse engineering the Samsung Shannon baseband firmware | 264 | 🔴 | Python |
| [mediatek-lte-baseband-re](https://github.com/cyrozap/mediatek-lte-baseband-re) | Notes and tools for reverse engineering the MediaTek LTE baseband and Coresonic DSP | 229 | 🟢 | Python |
| [balongflash](https://github.com/forth32/balongflash) | Flasher for Huawei modems on the Balong V7 chipset | 214 | 🔴 | C |
| [balong-usbdload](https://github.com/forth32/balong-usbdload) | Emergency USB boot loader for Huawei Balong V7 modems | 213 | 🟡 | C |
| [ShannonBaseband](https://github.com/grant-h/ShannonBaseband) | Scripts, Ghidra loaders and notes for Samsung's Shannon baseband | 188 | 🟡 | C |
| [xmm7360-usb-modeswitch](https://github.com/xmm7360/xmm7360-usb-modeswitch) | Tools for the Fibocom L850-GL / Intel XMM7360 LTE modem on Linux | 143 | 🔴 | C |
| [MobileInsight core](https://github.com/mobile-insight/mobileinsight-core) | Parses Qualcomm and MediaTek modem diagnostic logs on your own device | 140 | 🟡 | C |
| [shannon_modem_loader](https://github.com/alexander-pick/shannon_modem_loader) | IDA Pro loader for Exynos/Shannon baseband modem firmware images | 87 | 🟡 | Python |
| [mtk_bp](https://github.com/nccgroup/mtk_bp) | MediaTek baseband processor firmware tools | 82 | 🟢 | Python |
| [qc_debug_monitor](https://github.com/Cr4sh/qc_debug_monitor) | Debug message monitor for Qualcomm cellular modems | 79 | 🔴 | Python |
| [aristoteles](https://github.com/seemoo-lab/aristoteles) | Wireshark dissector for Apple's ARI protocol between iPhone and Intel basebands | 74 | 🟢 | Lua |
| [qhuaweiflash](https://github.com/forth32/qhuaweiflash) | GUI to flash Huawei modems/routers and edit their firmware files | 71 | 🔴 | C++ |
| [diag-parser](https://github.com/moiji-mobile/diag-parser) | Parses Qualcomm DIAG logs and converts them to GSMTAP | 68 | 🔴 | C |
| [shannon-dbg](https://github.com/synacktiv/shannon-dbg) | Debugger for the Samsung Shannon baseband firmware | 60 | 🔴 | C |
| [SM-A217F_forensics](https://github.com/Tomiwa-Ot/SM-A217F_forensics) | Samsung modem AT commands over USB serial and secret dialer codes extracted from system packages | 56 | 🟡 | Python |
| [ShannonEE](https://github.com/grant-h/ShannonEE) | Dynamic analysis environment for Samsung's Shannon baseband (predecessor of FirmWire) | 44 | 🗄️ |  |
| [DiagLibrary](https://github.com/sanjaywave/DiagLibrary) | Library using the Qualcomm DIAG port for band and frequency locking on your own device | 26 | 🔴 | C |
| [osmo-qcdiag](https://github.com/osmocom/osmo-qcdiag) | Osmocom tools for the Qualcomm DIAG interface | 21 | 🟡 | C |
| [dct3-gsmtap](https://gitea.osmocom.org/phone-side/dct3-gsmtap) | Obtains GSMTAP SIM and GSM messages from Nokia DCT3 phones |  | ⚪ |  |
| [imsd](https://codeberg.org/DylanVanAssche/imsd) | Reverse-engineered FOSS implementation of IMS (VoLTE) services for Linux phones |  | ⚪ |  |
| [libqmi](https://gitlab.freedesktop.org/mobile-broadband/libqmi) | Library for the Qualcomm MSM Interface (QMI) modem protocol |  | ⚪ |  |
| [libqrtr-glib](https://gitlab.freedesktop.org/mobile-broadband/libqrtr-glib) | Library for the Qualcomm IPC Router (QRTR) protocol |  | ⚪ |  |

## Digital Voice Radio

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [SDRTrunk](https://github.com/DSheirer/sdrtrunk) | Decode and follow P25, DMR, LTR, MPT1327 and other trunked radio systems | 2,210 | 🟢 | Java |
| [trunk-recorder](https://github.com/TrunkRecorder/trunk-recorder) | Record calls from P25 and Motorola SmartNet trunked radio systems | 1,153 | 🟢 | C++ |
| [MMDVMHost](https://github.com/g4klx/MMDVM-Host) | Host program for MMDVM digital voice hotspots (D-Star, DMR, YSF, P25, NXDN) | 452 | 🟢 | C++ |
| [dsdcc](https://github.com/f4exb/dsdcc) | Digital Speech Decoder rewritten as a C++ library for DMR, D-Star, YSF, dPMR and more | 330 | 🟡 | C++ |
| [mbelib](https://github.com/szechyjs/mbelib) | Implementation of the proprietary IMBE/AMBE vocoders used in P25, DMR and ProVoice | 321 | 🔴 | C++ |
| [TETRA_crypto](https://github.com/MidnightBlueLabs/TETRA_crypto) | Reverse engineered TETRA cryptographic primitives (TEA ciphers, TAA1) | 217 | 🟡 | C |
| [md380-re](https://github.com/pchickey/md380-re) | MD380 DMR radio reverse engineering | 127 | 🗄️ | C |
| [osmo-tetra-sq5bpf](https://github.com/sq5bpf/osmo-tetra-sq5bpf) | osmo-tetra with patches to decode TETRA SDS messages and feed telive | 64 | 🔴 | C |
| [gr-ysf](https://github.com/HB9UF/gr-ysf) | GNU Radio modules decoding Yaesu System Fusion C4FM packets | 61 | 🔴 | CMake |
| [tetra-listener](https://github.com/itds-consulting/tetra-listener) | Records and decodes unencrypted TETRA voice calls with an SDR | 59 | 🔴 | Python |
| [gr-smartnet](https://github.com/bistromath/gr-smartnet) | GNU Radio logging scanner for Motorola SmartNet II trunking | 48 | 🔴 | Shell |
| [tetra-rtlsdr](https://github.com/alphafox02/tetra-rtlsdr) | Single C binary RTL-SDR front-end for TETRA decoding with telive | 45 | 🟢 | C |
| [edacs-fm](https://github.com/lwvmobile/edacs-fm) | EDACS trunked radio tracking with an RTL-SDR | 13 | 🗄️ | C |
| [blip25-vocoder](https://github.com/OpenBLIP25/blip25-vocoder) | P25 Phase 1 and Phase 2 IMBE/AMBE+2 voice codec encode and decode in Rust | 12 | 🟢 | Rust |

## Email & Groupware

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [hydroxide](https://github.com/emersion/hydroxide) | Third-party ProtonMail bridge providing IMAP, SMTP and CardDAV | 2,169 | 🗄️ | Go |
| [exchangelib](https://github.com/ecederstrand/exchangelib) | Python client for Microsoft Exchange Web Services (EWS) | 1,275 | 🟢 | Python |
| [TbSync](https://github.com/jobisoft/TbSync) | [Thunderbird Add-On] Central user interface to manage cloud accounts and to synchronize their contact, task and... | 924 | 🟢 | JavaScript |
| [php-ews](https://github.com/jamesiarmes/php-ews) | PHP Exchange Web Services | 573 | 🟡 | PHP |
| [gromox](https://github.com/grommunio/gromox) | Groupware server implementing Exchange MAPI/HTTP, RPC/HTTP, EWS and IMAP | 268 | 🟢 | C++ |
| [EAS-4-TbSync](https://github.com/jobisoft/EAS-4-TbSync) | [Thunderbird Add-On] The Exchange ActiveSync provider for TbSync to sync contacts, tasks and calendars to Thunderbird. | 255 | 🟢 | JavaScript |
| [Viewpoint](https://github.com/WinRb/Viewpoint) | A Ruby client access library for Microsoft Exchange Web Services (EWS) | 249 | 🟢 | Ruby |
| [pyexchange](https://github.com/linkedin/pyexchange) | Python wrapper for Microsoft Exchange | 154 | 🔴 | Python |
| [node-ews](https://github.com/nmarus/node-ews) | A simple JSON wrapper for the Exchange Web Services (EWS) SOAP API. | 116 | 🔴 | JavaScript |
| [ruby-msg](https://github.com/aquasync/ruby-msg) | Ruby library for reading Outlook .msg and .pst (MAPI message store) files | 103 | 🟢 | Ruby |
| [protonmail-cli](https://github.com/dimkouv/protonmail-cli) | Unofficial command-line utility for ProtonMail | 98 | 🔴 | Python |
| [akonadi-ews](https://github.com/KrissN/akonadi-ews) | Akonadi resource agent for Microsoft Exchange using Exchange Web Services (EWS) protocol | 95 | 🔴 | C++ |
| [ews-cpp](https://github.com/otris/ews-cpp) | A C++11 header-only library for Microsoft Exchange Web Services | 77 | 🟢 | C++ |
| [evolution-ews](https://github.com/GNOME/evolution-ews) | Read-only mirror of https://gitlab.gnome.org/GNOME/evolution-ews | 65 | 🟢 | C |
| [evolution-activesync](https://github.com/GNOME/evolution-activesync) | Read-only mirror of https://gitlab.gnome.org/GNOME/evolution-activesync | 40 | 🟢 | C |
| [grommunio-sync](https://github.com/grommunio/grommunio-sync) | EAS (Exchange ActiveSync) interface for grommunio | 40 | 🟢 | PHP |
| [pyActiveSync](https://github.com/solbirn/pyActiveSync) | A pure python library for the ActiveSync protocol | 39 | 🔴 | Python |
| [jsas](https://github.com/mozilla-b2g/jsas) | DEPRECATED - A Javascript ActiveSync library | 36 | 🗄️ | JavaScript |
| [ews-rs](https://github.com/thunderbird/ews-rs) | A Rust crate for interacting with the Exchange Web Services API | 33 | 🟢 | Rust |
| [syncroton](https://github.com/tine20/syncroton) | Syncroton is a PHP based implementation of the Exchange ActiveSync protocol, which is licensed under the LGPL V3 | 24 | 🟢 | PHP |
| [node-asclient](https://github.com/clncln1/node-asclient) | Node.js client for Exchange ActiveSync synchronization | 20 | 🔴 | JavaScript |
| [activesync-go](https://github.com/magicmonty/activesync-go) | ActiveSync implementation for Google Go | 19 | 🔴 | Go |
| [PyWBXMLDecoder](https://github.com/davidpshaw/PyWBXMLDecoder) | Decoder for Exchange ActiveSync WAP Binary XML (WBXML) | 19 | 🔴 | Python |
| [proton-api](https://github.com/gitladen7/proton-api) | Unofficial ProtonMail API client for browser and Node.js | 9 | 🟡 | TypeScript |
| [proton-api-rs](https://github.com/LeanderBB/proton-api-rs) | Unofficial implementation of the Proton REST API in Rust | 4 | 🗄️ | Rust |
| [protonmail-rs](https://github.com/filippofinke/protonmail-rs) | Unofficial pure-Rust Proton Mail SDK with SRP auth, OpenPGP and the mail API | 3 | 🟢 | Rust |

## File Sharing & Remote Desktop

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Sunshine](https://github.com/LizardByte/Sunshine) | Self-hosted game stream host that implements the NVIDIA GameStream protocol for Moonlight clients | 42,533 | 🟢 | C++ |
| [moonlight-qt](https://github.com/moonlight-stream/moonlight-qt) | Open-source NVIDIA GameStream / Sunshine client for Windows, macOS, Linux and Steam Link | 19,206 | 🟢 | C++ |
| [Impacket](https://github.com/fortra/impacket) | Python classes for SMB, MSRPC, NTLM, Kerberos, LDAP and other Windows protocols | 16,192 | 🟢 | Python |
| [FreeRDP](https://github.com/FreeRDP/FreeRDP) | Free implementation of Microsoft's Remote Desktop Protocol (client and server libraries) | 13,875 | 🟢 | C |
| [OpenDrop](https://github.com/seemoo-lab/opendrop) | Open AirDrop implementation in Python, protocol-compatible with iOS/macOS | 9,914 | 🟢 | Python |
| [Shairport Sync](https://github.com/mikebrady/shairport-sync) | AirPlay and AirPlay 2 audio receiver for Linux/BSD | 8,910 | 🟢 | C |
| [moonlight-android](https://github.com/moonlight-stream/moonlight-android) | Open-source NVIDIA GameStream client for Android | 7,344 | 🟢 | C |
| [xrdp](https://github.com/neutrinolabs/xrdp) | Open source RDP server for Linux | 6,767 | 🟢 | C |
| [NearDrop](https://github.com/grishka/NearDrop) | Unofficial Google Nearby Share/Quick Share receiver for macOS from reversed protocol | 6,313 | 🟢 | Swift |
| [rquickshare](https://github.com/Martichou/rquickshare) | Rust implementation of Android Nearby Share / Quick Share for Linux and macOS | 3,649 | 🟢 | Rust |
| [UxPlay](https://github.com/FDH2/UxPlay) | AirPlay mirroring server for Unix (reverse-engineered AirPlay 2 protocol) | 3,251 | 🟢 | C |
| [IronRDP](https://github.com/Devolutions/IronRDP) | Rust implementation of the Microsoft Remote Desktop Protocol (RDP) | 3,243 | 🟢 | Rust |
| [RDPY](https://github.com/citronneur/rdpy) | Microsoft RDP protocol implementation in Python: client, server, MitM, honeypot | 1,735 | 🔴 | Python |
| [moonlight-ios](https://github.com/moonlight-stream/moonlight-ios) | Open-source NVIDIA GameStream client for iOS and tvOS | 1,695 | 🟢 | C |
| [OWL (Open Wireless Link)](https://github.com/seemoo-lab/owl) | Open implementation of Apple Wireless Direct Link (AWDL) for Linux and macOS | 1,572 | 🗄️ | C |
| [moonlight-tv](https://github.com/mariotaku/moonlight-tv) | Lightweight GameStream client for LG webOS TVs and embedded devices | 1,513 | 🟢 | C |
| [rdesktop](https://github.com/rdesktop/rdesktop) | Original open source RDP client for Unix, built from reverse engineering | 1,356 | 🟢 | C |
| [Samba](https://github.com/samba-team/samba) | SMB/CIFS file, print and AD domain server; SMB reverse engineered long before MS published specs | 1,144 | 🟢 | C |
| [moonlight-common-c](https://github.com/moonlight-stream/moonlight-common-c) | Core implementation of NVIDIA's reverse-engineered GameStream protocol | 581 | 🟢 | C |
| [libsmb2](https://github.com/sahlberg/libsmb2) | Userspace SMB2/3 client library in C | 433 | 🟢 | C |
| [go-smb2](https://github.com/hirochachacha/go-smb2) | SMB2/3 client library written in Go | 413 | 🟢 | Go |
| [smbprotocol](https://github.com/jborean93/smbprotocol) | Python SMBv2/v3 client implementation | 400 | 🟢 | Python |
| [uu-remote-linux](https://github.com/VallierDev/uu-remote-linux) | Unofficial native Linux host for NetEase UU Remote, from its reverse-engineered protocol | 384 | 🟢 | Rust |
| [ksmbd](https://github.com/namjaejeon/ksmbd) | In-kernel Linux SMB3 server | 375 | 🟢 | C |
| [moonlight-windows](https://github.com/moonlight-stream/moonlight-windows) | NVIDIA GameStream client for Windows Phone (discontinued) | 82 | 🗄️ | C |
| [WayShare](https://github.com/wesleygrimes/wayshare) | Shares a Hyprland desktop with a Mac's built-in Screen Sharing app via Apple's protocol | 35 | 🟢 | Rust |
| [openrad](https://github.com/gringoestrangeiro/openrad) | Open-source Rust reimplementation of Radmin VPN with a Linux app and CLI | 16 | 🟢 | Rust |
| [pippin](https://github.com/jonesy827/pippin) | Native Rust Linux client for Apple's macOS High-Performance Screen Sharing protocol (HEVC 4:4:4, audio, clipboard) | 6 | 🟢 | Rust |
| [chiaki](https://git.sr.ht/~thestr4ng3r/chiaki) | Original free and open-source PlayStation Remote Play client built from the reverse-engineered protocol |  | ⚪ |  |

## Legacy IM Revival

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [PFire](https://github.com/darcymiranda/PFire) | Emulated Xfire server for the 1.127 client | 59 | 🟢 | C# |
| [MSN](https://github.com/v1ckxy/MSN) | MSN Messenger server reimplementation | 22 | 🔴 | Python |

## Messaging Protocols

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Baileys](https://github.com/WhiskeySockets/Baileys) | Socket-based TypeScript API for WhatsApp Web | 11,426 | 🟢 | JavaScript |
| [whatsmeow](https://github.com/tulir/whatsmeow) | Go library for the WhatsApp web multi-device API | 7,635 | 🟢 | Go |
| [mautrix-whatsapp](https://github.com/mautrix/whatsapp) | Matrix-WhatsApp puppeting bridge | 1,912 | 🟢 | Go |
| [Open OSCAR Server (Retro AIM Server)](https://github.com/mk6i/open-oscar-server) | Self-hostable server compatible with classic AIM and ICQ clients (OSCAR protocol) | 1,586 | 🟢 | Go |
| [purple-facebook](https://github.com/dequis/purple-facebook) | Facebook Messenger (MQTT) protocol plugin for libpurple | 950 | 🟢 | C |
| [BitlBee](https://github.com/bitlbee/bitlbee) | IRC gateway to other chat networks (OSCAR, MSN, Jabber, Twitter...) | 645 | 🟡 | C |
| [skype4pidgin](https://github.com/EionRobb/skype4pidgin) | Skype protocol plugin for Pidgin/libpurple (SkypeWeb) | 621 | 🗄️ | C |
| [mautrix-meta](https://github.com/mautrix/meta) | Matrix bridge for Facebook Messenger and Instagram DMs | 453 | 🟢 | Go |
| [purple-discord](https://github.com/EionRobb/purple-discord) | Discord protocol plugin for Pidgin/libpurple | 432 | 🟢 | C |
| [purple-gowhatsapp](https://github.com/hoehermann/purple-gowhatsapp) | WhatsApp plugin for Pidgin/libpurple built on whatsmeow | 364 | 🟢 | C |
| [Telegram-Server-Java](https://github.com/aykutalparslan/Telegram-Server-Java) | Unofficial Telegram MTProto server in Java | 241 | 🗄️ | Java |
| [purple-teams](https://github.com/EionRobb/purple-teams) | Third-party Microsoft Teams plugin for Pidgin/libpurple | 216 | 🟢 | C |
| [Telegram-Server](https://github.com/aykutalparslan/Telegram-Server) | Unofficial Telegram server in C# with channels, media, secret chats and calls | 176 | 🟢 | C# |
| [fossteams/teams-api](https://github.com/fossteams/teams-api) | Unofficial Go library for Microsoft Teams internal APIs used by the official clients | 167 | 🔴 | Go |
| [ts3j](https://github.com/Manevolent/ts3j) | Open-source Java TeamSpeak 3 client library using the full client protocol | 132 | 🟢 | Java |
| [mautrix-googlechat](https://github.com/mautrix/googlechat) | Matrix-Google Chat puppeting bridge | 127 | 🟢 | Python |
| [telegramd](https://github.com/bluefoxah/telegramd) | Unofficial open-source Telegram server written in Go | 28 | 🔴 | Go |
| [mini-telegram](https://github.com/Yumcoder-dev/mini-telegram) | Unofficial MTProto server in Rust that works with Telegram clients | 14 | 🔴 | Rust |
| [AOL Wiretap](https://github.com/chriskearney/wiretap) | Packet capture and analysis tool for reverse engineering the AOL protocol | 12 | 🟢 | Java |
| [poggadaj](https://github.com/Oreeeee/poggadaj) | Open Source reimplementation of Gadu-Gadu backend (official mirror of https://codeberg.org/or3e/poggadaj) | 8 | 🟢 | Go |
| [zoomer](https://github.com/RealKeyboardWarrior/zoomer) | Zoom chat bots via reverse-engineered Zoom Web SDK websocket protocol | 4 | 🔴 | Go |
| [aMSN](https://sourceforge.net/projects/amsn/) | Multiplatform client for the MSN Messenger protocol |  | ⚪ |  |

## Other Protocols

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [librespot](https://github.com/librespot-org/librespot) | Open source Spotify Connect client library in Rust | 7,321 | 🟢 | Rust |
| [SteamKit2](https://github.com/SteamRE/SteamKit) | .NET library interoperating with Valve's Steam network protocol | 3,215 | 🟢 | C# |
| [SteamTracking](https://github.com/SteamTracking/SteamTracking) | Tracks Steam client files, protobufs and API changes for research | 1,110 | 🟢 | JavaScript |
| [chrome-x-browser-validation-header](https://github.com/dsekz/chrome-x-browser-validation-header) | Reverse-engineered Chrome's private X-Browser-Validation integrity header; generator toolkit | 333 | 🟡 | Python |
| [sspks](https://github.com/jdel/sspks) | Simple Synology package server reverse engineered from the official package repository protocol | 281 | 🟢 | PHP |
| [HelicopterDemod](https://github.com/proto17/HelicopterDemod) | Reverse-engineered news helicopter downlink radio protocol from audio in video | 168 | 🔴 | Python |
| [OpenChirp](https://github.com/cawfree/OpenChirp) | Reverse engineered implementation of the Chirp data-over-audio protocol | 108 | 🔴 | Java |
| [android-universal-reader](https://github.com/kormax/android-universal-reader) | Android NFC reader demo for Apple VAS and Google Smart Tap protocols | 87 | 🟢 | Kotlin |
| [AirVideo](https://github.com/jphastings/AirVideo) | Ruby library for interacting with an AirVideo server | 75 | 🔴 | Ruby |
| [open-ds](https://github.com/Boomaa23/open-ds) | Reverse engineered lightweight cross-platform FRC Driver Station | 59 | 🟢 | Java |
| [openfsd](https://github.com/renorris/openfsd) | Open FSD multiplayer flight simulation network server | 58 | 🟢 | Go |
| [ez-sniff](https://github.com/kwesthaus/ez-sniff) | Demodulate and dissect RF packets from E-ZPass toll transponders | 56 | 🟡 | C++ |
| [wow_messages](https://github.com/gtker/wow_messages) | Auto generated messages for the World of Warcraft network protocol | 53 | 🟢 | Rust |
| [nokd](https://github.com/irql/nokd) | Reverse engineering and reimplementation of the Windows NT kernel debugger protocol | 44 | 🟡 | C |
| [Wow-wireshark-dissector](https://github.com/chaodhib/Wow-wireshark-dissector) | World of Warcraft Wireshark dissector | 40 | 🔴 | C |
| [wow_srp](https://github.com/gtker/wow_srp) | Library for World of Warcraft flavor of SRP6 authentication. | 19 | 🟡 | Rust |
| [project-mayhem](https://github.com/giannitedesco/project-mayhem) | Reverse-engineered Streamate webcam protocol; native client | 7 | 🔴 | C |
| [libmms](https://sourceforge.net/projects/libmms/) | Library for the Microsoft Media Server (MMS) streaming protocol |  | ⚪ |  |

## Proprietary Enterprise Protocols

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [openfortivpn](https://github.com/adrienverge/openfortivpn) | Client for Fortinet's PPP+TLS SSL-VPN tunnels | 3,450 | 🟢 | Perl |
| [GlobalProtect-openconnect](https://github.com/yuezk/GlobalProtect-openconnect) | Palo Alto GlobalProtect VPN client for Linux/macOS, based on OpenConnect | 2,309 | 🟢 | Rust |
| [tedious](https://github.com/tediousjs/tedious) | Pure JavaScript implementation of the TDS protocol for SQL Server | 1,618 | 🟢 | TypeScript |
| [pywinrm](https://github.com/diyan/pywinrm) | Python library for Windows Remote Management (WinRM) | 1,142 | 🟢 | Python |
| [go-ora](https://github.com/sijms/go-ora) | Pure Go Oracle client implementing the TNS wire protocol | 986 | 🟢 | Go |
| [gokrb5](https://github.com/jcmturner/gokrb5) | Pure Go Kerberos library for clients and services | 781 | 🟡 | Go |
| [DavMail](https://github.com/mguessan/davmail) | POP/IMAP/SMTP/CalDAV/LDAP gateway to Exchange and Office 365 (EWS/WebDAV) | 772 | 🟢 | Java |
| [libnfs](https://github.com/sahlberg/libnfs) | NFS client library | 607 | 🟢 | C |
| [Kerberos.NET](https://github.com/dotnet/Kerberos.NET) | A Kerberos implementation built entirely in managed code. | 567 | 🟢 | C# |
| [node-dota2](https://github.com/Arcana/node-dota2) | node-steam plugin for the Dota 2 game coordinator | 555 | 🗄️ | JavaScript |
| [FreeTDS](https://github.com/FreeTDS/freetds) | Reimplementation of Sybase/Microsoft SQL Server TDS wire protocol | 506 | 🟢 | C |
| [winrm](https://github.com/masterzen/winrm) | Command-line tool and library for Windows remote command execution in Go | 479 | 🟢 | Go |
| [node-csgo](https://github.com/joshuaferrara/node-csgo) | node-steam plugin for the Counter-Strike: Global Offensive game coordinator | 464 | 🔴 | JavaScript |
| [python-fints](https://github.com/raphaelm/python-fints) | Pure-Python FinTS/HBCI banking protocol client | 427 | 🟢 | Python |
| [pypsrp](https://github.com/jborean93/pypsrp) | PowerShell Remoting Protocol for Python | 391 | 🟢 | Python |
| [network-audio-controller](https://github.com/chris-ritsen/network-audio-controller) | Unofficial Dante Controller alternative for multiple platforms | 375 | 🟢 | Python |
| [inferno](https://github.com/teodly/inferno) | Unofficial implementation of the Dante audio-over-IP protocol | 354 | 🟢 | Rust |
| [hibiscus](https://github.com/willuhn/hibiscus) | Free home-banking app for Linux, Windows and macOS built on HBCI4Java | 348 | 🟢 | Java |
| [jcifs-ng](https://github.com/AgNO3/jcifs-ng) | A cleaned-up and improved version of the jCIFS library | 347 | 🟢 | Java |
| [dota2](https://github.com/ValvePython/dota2) | Python package for interacting with the Dota 2 game coordinator | 224 | 🔴 | Python |
| [go-ntlmssp](https://github.com/Azure/go-ntlmssp) | NTLM/Negotiate authentication over HTTP | 203 | 🟢 | Go |
| [hbci4java](https://github.com/hbci4j/hbci4java) | Java FinTS/HBCI implementation with chipTAN, pushTAN and SEPA support | 195 | 🟢 | Java |
| [OpenChange](https://github.com/openchange/openchange) | Open implementation of Microsoft Exchange MAPI/RPC protocols | 175 | 🔴 | C |
| [phpFinTS](https://github.com/nemiah/phpFinTS) | PHP library to communicate with FinTS/HBCI bank servers | 164 | 🟢 | PHP |
| [eoip](https://github.com/bbonev/eoip) | Linux kernel EoIP tunnel compatible with MikroTik | 163 | 🟢 | C |
| [Z-Push](https://github.com/Z-Hub/Z-Push) | Open source Exchange ActiveSync implementation for syncing mobile devices | 158 | 🟢 | PHP |
| [JavaSteam](https://github.com/Longi94/JavaSteam) | Java library for interacting directly with Valve's Steam servers, based on SteamKit | 146 | 🟢 | Kotlin |
| [open_fints_js_client](https://github.com/jschyma/open_fints_js_client) | JavaScript FinTS/HBCI client | 135 | 🟡 | JavaScript |
| [SIPE](https://github.com/tieto/sipe) | Third-party Pidgin plugin for the Microsoft Lync/OCS protocol | 130 | 🔴 | C |
| [wycliffe](https://github.com/jsharkey/wycliffe) | Clean-room implementation of the Dante audio protocol | 128 | 🔴 | Python |
| [unifi-inform-protocol](https://github.com/jeffreykog/unifi-inform-protocol) | Documentation of the reverse engineered Ubiquiti UniFi inform protocol | 119 | 🔴 |  |
| [SAP Wireshark dissectors](https://github.com/SecureAuthCorp/SAP-Dissection-plug-in-for-Wireshark) | Wireshark dissectors for proprietary SAP NI, Diag, RFC, Router, Enqueue protocols | 114 | 🔴 | C |
| [vapor](https://github.com/scholtzm/vapor) | Lightweight Steam client framework for Node.js on the Steam CM protocol | 111 | 🔴 | JavaScript |
| [smb-rs](https://github.com/afiffon/smb-rs) | Pure Rust SMB2/3 client | 86 | 🟢 | Rust |
| [OpenURMA](https://github.com/bojieli/OpenURMA) | Clean-room open implementation of the Unified Bus protocol | 80 | 🟢 | C++ |
| [snxvpn](https://github.com/schlatterbeck/snxvpn) | Command-line client for Check Point SSL VPN | 72 | 🟡 | Python |
| [node-steamstore](https://github.com/DoctorMcKay/node-steamstore) | Node.js module for interacting with the Steam store's undocumented web endpoints | 69 | 🟡 | JavaScript |
| [libfintx](https://github.com/libfintx/libfintx) | .NET client library for HBCI, FinTS and EBICS banking protocols | 66 | 🟢 | C# |
| [pyspnego](https://github.com/jborean93/pyspnego) | Python SPNEGO authentication library | 66 | 🟢 | Python |
| [node-tf2](https://github.com/DoctorMcKay/node-tf2) | Node.js module for talking to the Team Fortress 2 game coordinator | 63 | 🟡 | JavaScript |
| [unifi-protocol-reverse-engineering](https://github.com/fxkr/unifi-protocol-reverse-engineering) | Reverse engineered docs for the protocol between UniFi APs and controller | 60 | 🔴 |  |
| [node-steam-client](https://github.com/DoctorMcKay/node-steam-client) | Node.js SteamClient implementing Valve's reverse-engineered Steam network protocol | 55 | 🗄️ | JavaScript |
| [SteamKit-Java](https://github.com/Top-Cat/SteamKit-Java) | Java port of SteamKit for Steam network protocol access | 50 | 🔴 | Java |
| [gss-ntlmssp](https://github.com/gssapi/gss-ntlmssp) | GSSAPI implementation of Microsoft NTLM (MS-NLMP) | 42 | 🟢 | C |
| [node-steam-gameserver](https://github.com/DoctorMcKay/node-steam-gameserver) | Steam client for game servers on the Steam CM protocol | 19 | 🟢 | JavaScript |
| [node-steam-crypto](https://github.com/seishun/node-steam-crypto) | Node.js implementation of Steam's session crypto | 15 | 🗄️ | JavaScript |
| [outlook-dndprotocol](https://github.com/yasoonOfficial/outlook-dndprotocol) | Reverse-engineered Outlook drag-and-drop OLE clipboard protocol | 4 | 🔴 | C# |

## Radio & SDR Protocols

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [dump1090](https://github.com/antirez/dump1090) | Dump1090 is a simple Mode S decoder for RTLSDR devices | 2,961 | 🟢 | C |
| [SatDump](https://github.com/SatDump/SatDump) | Decodes weather/earth-observation satellite downlinks and their data formats | 2,352 | 🟢 | C++ |
| [rc-switch](https://github.com/sui77/rc-switch) | Arduino library to operate cheap 433/315 MHz remote-controlled outlets and decode their protocols | 2,089 | 🟡 | C++ |
| [gr-gsm](https://github.com/ptrkrysik/gr-gsm) | Gnuradio blocks and tools for receiving GSM transmissions | 1,510 | 🟢 | C++ |
| [wmbusmeters](https://github.com/wmbusmeters/wmbusmeters) | Read the wired or wireless mbus protocol to acquire utility meter readings. | 1,351 | 🟢 | C++ |
| [multimon-ng](https://github.com/EliasOenal/multimon-ng) | Decoder for POCSAG/FLEX pagers, EAS, DTMF, AFSK and other digital radio modes | 1,144 | 🟢 | C |
| [esp-sdr](https://github.com/ESPARGOS/esp-sdr) | Uses undocumented raw I/Q capture of ESP32 chips as an SDR | 1,079 | 🟢 | C |
| [gr-lora_sdr](https://github.com/tapparelj/gr-lora_sdr) | This is the fully-functional GNU Radio software-defined radio (SDR) implementation of a LoRa transceiver with all... | 1,017 | 🟢 | C++ |
| [nrsc5](https://github.com/theori-io/nrsc5) | Receiver for the proprietary NRSC-5 (HD Radio) digital broadcast standard | 971 | 🟢 | C |
| [zwave-js](https://github.com/zwave-js/zwave-js) | Modern and standards-compliant Z-Wave device driver that runs almost anywhere | 892 | 🟢 | TypeScript |
| [dsd](https://github.com/szechyjs/dsd) | Digital Speech Decoder | 791 | 🟡 | C++ |
| [rtl_433_ESP](https://github.com/NorthernMan54/rtl_433_ESP) | Port of rtl_433 decoders to ESP32 with CC1101/SX127x radios | 737 | 🟢 | C |
| [readsb](https://github.com/wiedehopf/readsb) | ADS-B decoder swiss knife | 696 | 🟢 | C |
| [pyModeS](https://github.com/junzis/pyModeS) | Python decoder for Mode S and ADS-B signals | 673 | 🟢 | Python |
| [gr-lora](https://github.com/rpp0/gr-lora) | GNU Radio blocks for receiving LoRa modulated radio messages using SDR | 645 | 🔴 | C++ |
| [radiosonde_auto_rx](https://github.com/projecthorus/radiosonde_auto_rx) | Automatically track and decode weather radiosonde launches with an RTL-SDR | 617 | 🟢 | C |
| [protoview](https://github.com/antirez/protoview) | Flipper Zero app to display and decode known and unknown sub-GHz signals | 598 | 🟡 | C |
| [gr-lora](https://github.com/BastilleResearch/gr-lora) | GNU Radio OOT module implementing the LoRa PHY, based on... | 513 | 🔴 | C++ |
| [nrf24_multipro](https://github.com/goebish/nrf24_multipro) | nRF24L01 transmitter for reverse-engineered toy drone and RC protocols | 505 | 🟡 | C++ |
| [gr-iridium](https://github.com/muccc/gr-iridium) | Iridium burst detector and demodulator. | 494 | 🟢 | C++ |
| [op25](https://github.com/boatbod/op25) | Fork of osmocom OP25 by boatbod | 489 | 🟢 | C++ |
| [Quansheng_UV-K5_PCB_R51-V1.4_PCB_Reversing_Rev._0.9](https://github.com/mentalDetector/Quansheng_UV-K5_PCB_R51-V1.4_PCB_Reversing_Rev._0.9) | KiCad reverse engineering of the Quansheng UV-K5 handheld radio PCB | 417 | 🟡 |  |
| [acarsdec](https://github.com/TLeconte/acarsdec) | ACARS SDR decoder | 380 | 🗄️ | C |
| [tpms](https://github.com/jboone/tpms) | Tire Pressure Monitoring System decoding tools. | 370 | 🗄️ | Python |
| [rdz_ttgo_sonde](https://github.com/dl9rdz/rdz_ttgo_sonde) | ESP32/LoRa board firmware decoding RS41, RS92, DFM and M10/M20 radiosondes | 356 | 🟢 | C++ |
| [telive](https://github.com/sq5bpf/telive) | Live TETRA monitor built on osmo-tetra | 333 | 🟢 | C |
| [rtl-wmbus](https://github.com/xaelsouth/rtl-wmbus) | Software defined receiver for wireless M-Bus with RTL-SDR | 285 | 🟢 | C |
| [dspectrumgui](https://github.com/tresacton/dspectrumgui) | GUI to demodulate basic RF transmissions for reverse engineering | 280 | 🔴 | Ruby |
| [pilight](https://github.com/pilight/pilight) | Home automation daemon that decodes and sends many proprietary 433 MHz device protocols | 280 | 🟡 | C |
| [LoRa-SDR](https://github.com/myriadrf/LoRa-SDR) | SDR implementation of the proprietary LoRa PHY for research | 276 | 🔴 | C++ |
| [dumpvdl2](https://github.com/szpajder/dumpvdl2) | VDL Mode 2 message decoder and protocol analyzer | 259 | 🟢 | C |
| [Somfy_Remote](https://github.com/Nickduino/Somfy_Remote) | Arduino sketch that emulates a Somfy RTS remote (rolling-code protocol) | 239 | 🔴 | C++ |
| [decoder](https://github.com/theengs/decoder) | Library that decodes BLE advertising payloads of hundreds of proprietary sensors | 212 | 🟢 | C |
| [RS radiosonde decoders](https://github.com/rs1729/RS) | Decoders for Vaisala, Graw, Meteomodem, Intermet and other radiosonde formats | 205 | 🟢 | C |
| [LoRaPHY](https://github.com/jkadbear/LoRaPHY) | Complete LoRa physical layer (LoRa PHY) implementation in MATLAB. | 158 | 🔴 | MATLAB |
| [re-DECTed](https://github.com/znuh/re-DECTed) | RTL-SDR tools that receive DECT packets and feed them to Wireshark | 158 | 🟡 | Python |
| [Baofeng-UV-5RM-5RH-RE](https://github.com/amoxu/Baofeng-UV-5RM-5RH-RE) | Reverse engineering of the Baofeng UV-5RM/UV-5RH radios | 148 | 🟡 | C |
| [sdrpp_radiosonde](https://github.com/dbdexter-dev/sdrpp_radiosonde) | SDR++ plugin decoding RS41, DFM, M10/M20 and other radiosondes | 124 | 🔴 | C++ |
| [gr-dect2](https://github.com/pavelyazev/gr-dect2) | GNU Radio receiver and decoder for DECT (cordless phone) voice channels | 121 | 🟡 | C++ |
| [matt-knight research](https://github.com/matt-knight/research) | Publications incl. the LoRa PHY reverse engineering paper and code | 118 | 🔴 |  |
| [gr-reveng](https://github.com/tkuester/gr-reveng) | GNU Radio utilities for reverse engineering RF protocols | 95 | 🔴 | CMake |
| [gr-lora](https://github.com/jkadbear/gr-lora) | LoRa physical layer collision decoding based on GNU Radio | 84 | 🔴 | C++ |
| [osmo-tetra](https://github.com/osmocom/osmo-tetra) | Osmocom TETRA MAC/PHY receive and decode code | 83 | 🟢 | C |
| [dspectrum](https://github.com/tresacton/dspectrum) | Automated RF signal analysis for reverse engineering unknown OOK/ASK devices | 71 | 🔴 | Ruby |
| [RS41_Decoding](https://github.com/bazjo/RS41_Decoding) | Reverse engineering the Vaisala RS41 radiosonde data frame format | 71 | 🔴 |  |
| [nrsc5-gui](https://github.com/cmnybo/nrsc5-gui) | Graphical interface for the nrsc5 HD Radio receiver | 64 | 🔴 | Python |
| [PyEOT](https://github.com/ereuter/PyEOT) | GNU Radio/Python decoder for railroad End-of-Train telemetry packets | 64 | 🟡 | Python |
| [TH-D74-Kenwood](https://github.com/LA3QMA/TH-D74-Kenwood) | Rig control commands for the Kenwood TH-D74 radio | 57 | 🔴 |  |
| [OpenWXSDR](https://github.com/DL2MF/OpenWXSDR) | SDR receiver and decoder for weather radiosondes | 41 | 🟢 | Python |
| [tetra-toolkit](https://github.com/Tim---/tetra-toolkit) | Tools and documentation for decoding TETRA radio | 39 | 🟡 |  |
| [pyinsteon](https://github.com/pyinsteon/pyinsteon) | Python library for the Insteon home automation protocol | 31 | 🟢 | Python |
| [librenard](https://github.com/Jeija/librenard) | Reverse-engineered Sigfox protocol stack library | 27 | 🔴 | C |
| [Radiosonde decoder and tracker for Windows](https://github.com/9A4AM/Radiosonde-decoder-and-tracker-for-Windows) | Windows radiosonde decoder and tracker built on RTL-SDR | 25 | 🟢 |  |
| [renard-phy](https://github.com/Jeija/renard-phy) | Open Sigfox physical-layer implementation for SDR | 25 | 🔴 | Python |
| [gascop](https://github.com/yuvadm/gascop) | A lightweight POCSAG decoder for rtl-sdr devices | 24 | 🔴 | C |
| [sondedump](https://github.com/dbdexter-dev/sondedump) | Extensible decoder for proprietary radiosonde telemetry formats | 19 | 🔴 | C |
| [gr-pocsag-decoder](https://github.com/keithdoggett/gr-pocsag-decoder) | GNU Radio POCSAG Receiver and Python Decoder | 18 | 🔴 | Python |
| [EOTDecode](https://github.com/russinnes/EOTDecode) | Python decoder for railroad End-of-Train device radio telemetry | 13 | 🟡 | Python |
| [ft991a-interoperability-tools](https://github.com/j0ju/ft991a-interoperability-tools) | Tools for the Yaesu FT-991A's undocumented memory and menu formats | 5 | 🟢 | Python |
| [sirf](https://github.com/tryan/sirf) | Interpreter for the SiRF binary GPS protocol | 1 | 🔴 | C |
| [dedected](https://gitea.osmocom.org/dect/dedected) | deDECTed.org DECT sniffing tools: Com-on-Air driver, Kismet and Wireshark support |  | ⚪ |  |
| [libdect](https://gitea.osmocom.org/dect/libdect) | DECT protocol stack library from the Osmocom DECT project |  | ⚪ |  |
| [SmallStep](https://github.com/nuruposan/SmallStep) | Download and configure classic MTK GPS loggers over their binary protocol on M5Stack | 0 | 🟢 | C++ |

## Satellite Downlinks

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [gr-satellites](https://github.com/daniestevez/gr-satellites) | GNU Radio decoders for many amateur and cubesat telemetry formats, incl. undocumented ones | 998 | 🟢 | Jupyter Notebook |
| [iridium-toolkit](https://github.com/muccc/iridium-toolkit) | Tools to parse and decode Iridium satellite frames (pager, SBD, voice, ring alerts) | 583 | 🟢 | Python |
| [goestools](https://github.com/pietern/goestools) | Receive and decode GOES LRIT/HRIT satellite downlinks and their xRIT files with an RTL-SDR | 425 | 🟡 | C++ |
| [JAERO](https://github.com/jontio/JAERO) | Demodulate and decode Inmarsat Aero signals carrying SatCom ACARS from aircraft | 275 | 🟡 | C++ |
| [iridium-sniffer](https://github.com/alphafox02/iridium-sniffer) | Standalone C Iridium burst detector and demodulator without GNU Radio | 215 | 🟢 | C |
| [jupyter_notebooks (Daniel Estévez)](https://github.com/daniestevez/jupyter_notebooks) | Notebooks analysing and decoding undocumented satellite and spacecraft signals | 200 | 🟢 | Jupyter Notebook |
| [meteor_decoder](https://github.com/artlav/meteor_decoder) | Portable decoder for the Meteor-M LRPT weather satellite signal | 155 | 🔴 | Pascal |
| [meteor_demod](https://github.com/dbdexter-dev/meteor_demod) | Demodulator for the Russian Meteor-M2 LRPT weather satellite downlink | 141 | 🔴 | C |
| [L-Band-Decoders](https://github.com/altillimity/L-Band-Decoders) | Decoders for L-band HRPT satellites incl. MetOp, FengYun-3 and Meteor | 128 | 🗄️ | C++ |
| [xrit-rx](https://github.com/sam210723/xrit-rx) | Receiver and decoder for GEO-KOMPSAT-2A (GK-2A) LRIT weather satellite images | 102 | 🗄️ | Python |
| [LeanHRPT-Decode](https://github.com/Xerbo/LeanHRPT-Decode) | Decoder for HRPT downlinks from NOAA, MetOp, FengYun and Meteor weather satellites | 87 | 🗄️ | C++ |
| [free-outernet](https://github.com/daniestevez/free-outernet) | Free software receiver for the reverse-engineered Outernet L-band satellite datacast | 85 | 🟡 | Python |
| [ORBCOMM-receiver](https://github.com/fbieberly/ORBCOMM-receiver) | Software decoder for ORBCOMM satellite downlink transmissions | 84 | 🟢 | Python |
| [InmarScope](https://github.com/SarahRoseLives/InmarScope) | Multichannel Inmarsat Aero and STD-C decoder with call following | 75 | 🟢 | C++ |
| [himawari-rx](https://github.com/sam210723/himawari-rx) | Receive Himawari-8 weather images from the HimawariCast satellite broadcast | 58 | 🗄️ | Python |
| [IridiumLive](https://github.com/microp11/iridiumlive) | Web visualizer for Iridium frames decoded by gr-iridium | 58 | 🔴 | C# |
| [goesdump](https://github.com/opensatelliteproject/goesdump) | Dumper for GOES xRIT data from the Open Satellite Project demodulator | 56 | 🔴 | C# |
| [xritdemod](https://github.com/opensatelliteproject/xritdemod) | Open Satellite Project demodulator for GOES xRIT downlinks | 55 | 🔴 | C++ |
| [inmarsat-sniffer](https://github.com/alphafox02/inmarsat-sniffer) | Standalone Inmarsat L-band decoder for STD-C EGC and Aero ACARS/ADS-C/CPDLC | 52 | 🟢 | C |
| [Standalone-Demodulators](https://github.com/altillimity/Standalone-Demodulators) | Standalone demodulators for weather satellite downlinks replacing GNU Radio flowgraphs | 51 | 🗄️ | C++ |
| [grcon2020-workshop](https://github.com/daniestevez/grcon2020-workshop) | Workshop materials on decoding interplanetary spacecraft telemetry with GNU Radio | 47 | 🔴 | Jupyter Notebook |
| [starlink-rs](https://github.com/ewilken/starlink-rs) | Rust client for the undocumented Starlink user-terminal gRPC endpoint | 46 | 🟡 | Rust |
| [meteor_decode](https://github.com/dbdexter-dev/meteor_decode) | Decoder that turns Meteor-M2 LRPT soft symbols into weather images | 44 | 🔴 | C |
| [COMS-1](https://github.com/sam210723/COMS-1) | Receive and decode weather images from the COMS-1 geostationary satellite | 41 | 🗄️ | Python |
| [gr-hrpt](https://github.com/altillimity/gr-hrpt) | GNU Radio blocks for NOAA, Meteor, MetOp and FengYun HRPT downlinks | 28 | 🔴 | C++ |
| [starlink-grpc-golang](https://github.com/clarkzjw/starlink-grpc-golang) | Go bindings for the undocumented Starlink user-terminal gRPC API | 26 | 🟢 | Shell |
| [metlrpt](https://github.com/opensatelliteproject/metlrpt) | Work-in-progress Meteor LRPT weather satellite decoder | 19 | 🔴 | C++ |
| [stdcdec](https://github.com/cropinghigh/stdcdec) | Open-source Inmarsat-C (STD-C) command-line decoder | 18 | 🔴 | C++ |
| [orbcomm-rx](https://github.com/sam210723/orbcomm-rx) | Demodulator and decoder for the Orbcomm VHF subscriber transmitter downlink | 15 | 🗄️ | Python |
| [inmarsatc](https://github.com/cropinghigh/inmarsatc) | C++ Inmarsat-C decoder library | 10 | 🔴 | C++ |
| [warc-iridium-sbd-decoder](https://github.com/usgs/warc-iridium-sbd-decoder) | Java library for decoding Iridium Short Burst Data packets | 10 | 🗄️ | Java |
| [ORBCOMM-receiver-lite](https://github.com/fbieberly/ORBCOMM-receiver-lite) | C implementation of a software decoder for ORBCOMM satellite transmissions | 8 | 🟡 | C |

## Sub-GHz Sensors & Meters

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [rtlamr](https://github.com/bemasher/rtlamr) | RTL-SDR receiver for Itron ERT smart utility meters | 2,550 | 🟢 | Go |
| [rtlamr2mqtt](https://github.com/allangood/rtlamr2mqtt) | Send ERT/SCM utility meter readings from rtlamr to MQTT and Home Assistant | 643 | 🟢 | Python |
| [SzczepanLeon esphome-components](https://github.com/SzczepanLeon/esphome-components) | ESPHome wM-Bus components decoding manufacturer-specific water/heat meter telegrams | 353 | 🟢 | C++ |
| [customer-assistance-buttons-sdr](https://github.com/jimilinuxguy/customer-assistance-buttons-sdr) | Reversed encoders of retail customer assistance call buttons via SDR | 340 | 🟡 |  |
| [dingdong](https://github.com/samyk/dingdong) | Digital ding-dong-ditch: replaying a wireless doorbell signal via SDR | 252 | 🔴 | C++ |
| [rtlamr-collect](https://github.com/bemasher/rtlamr-collect) | Data aggregation for utility meter readings captured with rtlamr | 204 | 🔴 | Go |
| [RFLink32](https://github.com/cpainchaud/RFLink32) | ESP32/ESP8266 RFLink port decoding many proprietary 433/868 MHz sensor and remote protocols | 196 | 🟢 | C |
| [BresserWeatherSensorReceiver](https://github.com/matthias-bs/BresserWeatherSensorReceiver) | Receiver for Bresser 5/6/7-in-1 868 MHz weather sensor radio protocols | 192 | 🟢 | C++ |
| [rf-car](https://github.com/rgerganov/rf-car) | Controlling toy RC cars with HackRF | 176 | 🔴 | C++ |
| [gr-elster](https://github.com/argilo/gr-elster) | GNU Radio block decoding Elster R2S smart meter packets | 142 | 🟡 | CMake |
| [weewx-sdr](https://github.com/matthewwall/weewx-sdr) | WeeWX driver that reads proprietary weather sensor broadcasts via rtl_433 | 138 | 🟡 | Python |
| [ESPiLight](https://github.com/puuu/ESPiLight) | Arduino library porting pilight's 433.92 MHz device protocol decoders | 126 | 🔴 | C++ |
| [max-cube-protocol](https://github.com/Bouni/max-cube-protocol) | Documentation of the eQ-3/ELV MAX! Cube radiator thermostat protocol | 118 | 🟡 |  |
| [weewx-interceptor](https://github.com/matthewwall/weewx-interceptor) | WeeWX driver that intercepts uploads from Acurite, Ambient and other weather bridges | 115 | 🟡 | Python |
| [openmili](https://github.com/henryk/openmili) | Open implementation of the Mi-Light 2.4 GHz LED control protocol | 111 | 🔴 | C++ |
| [AskSinPP](https://github.com/pa-pa/AskSinPP) | Arduino implementation of the HomeMatic BidCoS radio protocol | 110 | 🟡 | C++ |
| [DavisRFM69](https://github.com/dekay/DavisRFM69) | RFM69 library that receives the Davis Instruments weather station radio protocol | 96 | 🔴 | C |
| [RFLink32-For-Sonoff-RF-Bridge](https://github.com/schmurtzm/RFLink32-For-Sonoff-RF-Bridge) | RFLink32 port for the Sonoff RF Bridge decoding many proprietary 433 MHz protocols | 90 | 🔴 | C |
| [everblu-meters-esp8266-improved](https://github.com/genestealer/everblu-meters-esp8266-improved) | ESP8266/ESP32 reader for Itron EverBlu Cyble meters with MQTT and ESPHome | 78 | 🟢 | C++ |
| [Acuparse](https://github.com/acuparse/acuparse) | Captures AcuRite Iris/Atlas station data from the Access/smartHUB bridge's private uploads | 64 | 🟡 | PHP |
| [LightwaveRF](https://github.com/roberttidey/LightwaveRF) | Arduino libraries for the LightwaveRF 433 MHz home automation protocol | 60 | 🔴 | C++ |
| [esphome-rtl_433-decoder](https://github.com/juanboro/esphome-rtl_433-decoder) | Runs rtl_433 decoders for proprietary 433 MHz sensors inside ESPHome | 51 | 🟢 | C++ |
| [Sparsnas](https://github.com/kodarn/Sparsnas) | Decoding the IKEA Sparsnäs energy monitor's 868 MHz radio protocol | 50 | 🔴 | Python |
| [rfcontroljs](https://github.com/pimatic/rfcontroljs) | Node.js protocol decoders for many 433 MHz switches and weather stations | 48 | 🔴 | CoffeeScript |
| [smeter](https://github.com/stef/smeter) | Read water and heat meter radio transmissions with GNU Radio | 45 | 🔴 | Python |
| [everblu-meters](https://github.com/neutrinus/everblu-meters) | Reads Itron EverBlu Cyble water/gas meters via the RADIAN protocol with a CC1101 | 41 | 🗄️ | C |
| [tuya_rf](https://github.com/olivluca/tuya_rf) | ESPHome component for the Tuya RF and IR bridge radio | 40 | 🟢 | C |
| [acurite-esphome](https://github.com/swoboda1337/acurite-esphome) | ESPHome decoder for AcuRite 433 MHz weather sensor OOK signals | 34 | 🟢 | C++ |
| [rtldavis](https://github.com/bemasher/rtldavis) | RTL-SDR receiver for the Davis Instruments weather station radio protocol | 29 | 🗄️ | Go |
| [A-OK](https://github.com/akirjavainen/A-OK) | Protocol for A-OK 433.92 MHz window shade and projector screen remotes | 28 | 🔴 | C++ |
| [markisol](https://github.com/akirjavainen/markisol) | Arduino control for Markisol 433.92 MHz window shades and BF-series remotes protocol | 24 | 🔴 | C++ |
| [Acurite_00592TX_sniffer](https://github.com/bhunting/Acurite_00592TX_sniffer) | Arduino sniffer and decoder for the AcuRite 00592TX wireless temperature probe | 23 | 🔴 | C++ |
| [weewx-rtldavis](https://github.com/lheijst/weewx-rtldavis) | WeeWX driver capturing Davis weather station radio data with rtldavis | 22 | 🔴 | Python |
| [acurite5n1arduino](https://github.com/zerog2k/acurite5n1arduino) | Arduino receiver and decoder for AcuRite 5-in-1 weather station radio messages | 21 | 🔴 | Arduino |
| [openhab-binding-wmbus](https://github.com/KuguHome/openhab-binding-wmbus) | openHAB binding that receives and decodes wM-Bus messages including Techem meters | 21 | 🟢 | Java |
| [VPTools](https://github.com/kobuki/VPTools) | Transceiver library for Davis Vantage weather station radio packets | 20 | 🟡 | C++ |
| [weather-sdr-decode](https://github.com/skaringa/weather-sdr-decode) | RTL-SDR decoders for ELV and Mebus wireless weather sensors | 18 | 🟡 | Python |
| [HoneywellSecurity](https://github.com/jhaines0/HoneywellSecurity) | Decode Honeywell/Ademco 345 MHz wireless security sensors with an SDR | 17 | 🔴 | C++ |
| [Acurite-00592TX-Decoder-ESP32a](https://github.com/trlafleur/Acurite-00592TX-Decoder-ESP32a) | ESP32/ESP8266 decoder for AcuRite 00592TX, 06044TX and 06002M sensors with MQTT | 16 | 🔴 | C++ |
| [bresser-esphome](https://github.com/charlyschulte/bresser-esphome) | ESPHome component for Bresser 7-in-1 weather stations using an SX1276 radio | 16 | 🟢 | Python |
| [acurite_decoder](https://github.com/JorjBauer/acurite_decoder) | RFM12B/RFM69 demodulator and parser for AcuRite temperature sensor data | 12 | 🔴 | C++ |
| [yngvi](https://github.com/deebloo/yngvi) | Reads, decodes and displays AcuRite weather station radio data | 10 | 🟢 | Rust |
| [Homegear-HomeMaticBidCoS](https://github.com/Homegear/Homegear-HomeMaticBidCoS) | Homegear module implementing the HomeMatic BidCoS radio protocol | 9 | 🟢 | C++ |
| [Itron-EverBlu-Cyble](https://github.com/reidys/Itron-EverBlu-Cyble) | Terminal reader for Itron EverBlu Cyble water meters over the RADIAN 433 MHz protocol | 9 | 🔴 | C |
| [weewx-meteostick](https://github.com/matthewwall/weewx-meteostick) | WeeWX driver for the Meteostick receiver of Davis wireless weather stations | 9 | 🔴 | Python |
| [AcuRiteSniffer](https://github.com/bp2008/AcuRiteSniffer) | Reads weather data packets sent by AcuRite Access devices for local use | 7 | 🟡 | C# |
| [lacrosse-mqtt-gateway](https://github.com/deveth0/lacrosse-mqtt-gateway) | MQTT gateway for LaCrosse IT+ wireless sensors | 7 | 🔴 | Python |
| [iflag](https://github.com/pwitab/iflag) | Python library for the Itron/Actaris IFLAG and Corus gas volume converter protocol | 4 | 🔴 | Python |
| [cotech](https://github.com/akirjavainen/cotech) | Arduino control for Clas Ohlson Cotech 433 MHz power plugs protocol | 1 | 🔴 | C++ |

## VPN Clients

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [wgcf](https://github.com/ViRb3/wgcf) | Unofficial CLI that registers Cloudflare WARP accounts and generates WireGuard configs | 8,827 | 🟢 | Go |
| [oblivion-desktop](https://github.com/bepass-org/oblivion-desktop) | Unofficial Cloudflare WARP client for Windows, macOS and Linux | 8,402 | 🟢 | TypeScript |
| [docker-easyconnect](https://github.com/docker-easyconnect/docker-easyconnect) | Runs Sangfor EasyConnect/aTrust VPN clients in a container exposing SOCKS5/HTTP proxy gateways | 5,570 | 🟢 | Shell |
| [oblivion](https://github.com/bepass-org/oblivion) | Unofficial Cloudflare WARP client for Android | 4,885 | 🟢 | Dart |
| [usque](https://github.com/Diniboy1123/usque) | Open-source reimplementation of the Cloudflare WARP client's MASQUE protocol | 1,493 | 🟢 | Go |
| [zju-connect](https://github.com/Mythologyli/zju-connect) | Go reimplementation of the Sangfor EasyConnect VPN protocol (ZJU RVPN client) | 803 | 🟢 | Go |
| [openconnect](https://github.com/dlenski/openconnect) | OpenConnect client extended to support Palo Alto Networks' GlobalProtect VPN | 690 | 🟡 |  |
| [NJUConnect](https://github.com/lyc8503/NJUConnect) | Go reimplementation of the Sangfor EasyConnect VPN protocol for NJU | 624 | 🗄️ | Go |
| [snx-rs](https://github.com/ancwrd1/snx-rs) | Open Source Client For Check Point VPN Tunnels | 528 | 🟢 | Rust |
| [gp-saml-gui](https://github.com/dlenski/gp-saml-gui) | Interactively authenticate to GlobalProtect VPNs that require SAML | 385 | 🟡 | Python |
| [openconnect-sso](https://github.com/vlaci/openconnect-sso) | Wrapper script for OpenConnect supporting Azure AD (SAMLv2) authentication to Cisco SSL-VPNs | 378 | 🟡 | Python |
| [radmin-vpn-linux](https://github.com/baptisterajaut/radmin-vpn-linux) | Runs Radmin VPN on Linux with a custom driver and TAP bridge | 259 | 🟢 | C |
| [openfortivpn-webview](https://github.com/gm-vm/openfortivpn-webview) | Opens a browser webview to complete Fortinet SAML login and hand the session cookie to openfortivpn | 137 | 🟢 | C++ |
| [snell-server-reversed](https://github.com/icpz/snell-server-reversed) | Reverse engineered Surge Snell proxy server | 137 | 🔴 | C++ |
| [juniper-vpn-py](https://github.com/russdill/juniper-vpn-py) | Python Juniper VPN Authenticator | 112 | 🔴 | Python |
| [pan-globalprotect-okta](https://github.com/arthepsy/pan-globalprotect-okta) | PaloAlto Networks GlobalProtect VPN (integrated with OKTA) command-line client | 102 | 🟡 | Python |
| [opensnell](https://github.com/missuo/opensnell) | Go implementation of the Snell v4/v5 proxy protocol | 97 | 🟢 | Go |
| [openaws-vpn-client](https://github.com/jhrldev/openaws-vpn-client) | Unofficial open-source AWS Client VPN client written in Rust (SAML auth) | 82 | 🟡 | Rust |
| [openconnect-gp-okta](https://github.com/zdave/openconnect-gp-okta) | OpenConnect wrapper which logs into a GlobalProtect gateway, authenticating with Okta | 38 | 🗄️ | Python |
| [f5vpn-login](https://github.com/hackedd/f5vpn-login) | F5 VPN Command-line client | 21 | 🔴 | Python |
| [gp-okta-linux](https://github.com/jeffchannell/gp-okta-linux) | Connect Linux to a GlobalProtect VPN using Okta Push 2FA. | 15 | 🔴 | Shell |
| [ocserv](https://gitlab.com/openconnect/ocserv) | OpenConnect VPN server compatible with Cisco AnyConnect clients |  | ⚪ |  |
| [openconnect](https://gitlab.com/openconnect/openconnect) | Open client for Cisco AnyConnect, GlobalProtect, Pulse/Ivanti, Fortinet, F5 and Array SSL VPN protocols |  | ⚪ |  |
