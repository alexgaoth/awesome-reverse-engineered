# Network & Wire Protocols

[← All categories](../README.md) · 369 projects

- [Aviation & Marine](#aviation--marine) (29)
- [Casting & TV Remotes](#casting--tv-remotes) (40)
- [Cellular Modem Diagnostics](#cellular-modem-diagnostics) (22)
- [Digital Voice Radio](#digital-voice-radio) (13)
- [Email & Groupware](#email--groupware) (22)
- [File Sharing & Remote Desktop](#file-sharing--remote-desktop) (23)
- [Legacy IM Revival](#legacy-im-revival) (2)
- [Messaging Protocols](#messaging-protocols) (16)
- [Other Protocols](#other-protocols) (11)
- [Proprietary Enterprise Protocols](#proprietary-enterprise-protocols) (35)
- [Radio & SDR Protocols](#radio--sdr-protocols) (60)
- [Satellite Downlinks](#satellite-downlinks) (32)
- [Sub-GHz Sensors & Meters](#sub-ghz-sensors--meters) (42)
- [VPN Clients](#vpn-clients) (22)

## Aviation & Marine

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| SoftRF | DIY aviation proximity system interoperable with FLARM, OGN, P3I, FANET and other protocols | 1,030 | <https://github.com/lyusupov/SoftRF> |
| canboat | NMEA 2000 tools with a PGN database that reverse engineers proprietary marine PGNs | 660 | <https://github.com/canboat/canboat> |
| RemoteIDReceiver | Monitor drones via Remote ID over Wi-Fi/BLE, incl. DJI proprietary DroneID frames | 316 | <https://github.com/cyber-defence-campus/RemoteIDReceiver> |
| dump978 (mutability) *(archived)* | Demodulator and decoder for 978 MHz UAT aviation transmissions | 182 | <https://github.com/mutability/dump978> |
| dumphfdl | Multichannel decoder for HF Data Link (HFDL) aircraft messages | 161 | <https://github.com/szpajder/dumphfdl> |
| libacars | Library decoding ACARS payloads such as FANS-1/A, MIAM and other airline applications | 156 | <https://github.com/szpajder/libacars> |
| antsdr_dji_droneid *(archived)* | ANTSDR E200 firmware detecting DJI DroneID broadcasts with network output | 126 | <https://github.com/alphafox02/antsdr_dji_droneid> |
| canboatjs | TypeScript NMEA 2000 parser/encoder built on the canboat reverse-engineered PGN database | 119 | <https://github.com/canboat/canboatjs> |
| radar_pi | OpenCPN plugin for Navico, Garmin and Raymarine radars via reverse-engineered protocols | 107 | <https://github.com/opencpn-radar-pi/radar_pi> |
| PINGMapper | Processes Humminbird and Lowrance side-scan sonar recordings from proprietary log formats | 95 | <https://github.com/CameronBodine/PINGMapper> |
| rtl_acars_ng | Simple console ACARS decoder for RTL-SDR | 83 | <https://github.com/gat3way/rtl_acars_ng> |
| Seatalk-Autopilot-Remote-Control | Arduino remote that drives Raymarine autopilots over the proprietary SeaTalk1 bus | 76 | <https://github.com/AK-Homberger/Seatalk-Autopilot-Remote-Control> |
| PyHum | Reads and analyses Humminbird side-scan sonar files in proprietary DAT/SON format | 68 | <https://github.com/BenthicSubstrateMapping/PyHum> |
| acars-message-documentation | Community notes decoding airline-specific ACARS free-text message formats | 57 | <https://github.com/airframesio/acars-message-documentation> |
| samples2djidroneid | Decode DJI DroneID packets from I/Q samples | 37 | <https://github.com/anarkiwi/samples2djidroneid> |
| STWirelessRemote | Wireless remote for Raymarine ST1000/ST2000 autopilots using SeaTalk | 35 | <https://github.com/nauti-control/STWirelessRemote> |
| mayara *(archived)* | Marine yacht radar server for Navico, Furuno, Raymarine radars using RE'd network protocols | 34 | <https://github.com/keesverruijt/mayara> |
| MicronetToNMEA | Converts Raymarine Micronet wireless instrument radio traffic to NMEA 0183 | 34 | <https://github.com/Rodemfr/MicronetToNMEA> |
| RaymarineAPtoFakeNavicoAutoPilot | Emulates a Navico AC12 autopilot over NMEA 2000 to drive a Raymarine pilot from B&G displays | 28 | <https://github.com/htool/RaymarineAPtoFakeNavicoAutoPilot> |
| acars-decoder-typescript | Decoder for airline-specific ACARS message labels and formats in TypeScript | 22 | <https://github.com/airframesio/acars-decoder-typescript> |
| ogn-rf | Open Glider Network receiver that listens to glider tracker radio messages | 22 | <https://github.com/glidernet/ogn-rf> |
| OGN Tracker | Open Glider Network tracker firmware with OGN/FLARM-compatible radio protocol | 20 | <https://github.com/pjalocha/ogn-tracker> |
| sonaR | R package for reading Lowrance proprietary sonar log files | 17 | <https://github.com/KennethTM/sonaR> |
| seatalk (jamesroscoe) | Open-source library for the proprietary Raymarine SeaTalk protocol | 14 | <https://github.com/jamesroscoe/seatalk> |
| seatalk_wifi | Bridge from Raymarine SeaTalk to NMEA 0183 over Wi-Fi | 12 | <https://github.com/atonizzo/seatalk_wifi> |
| signalk-raymarine-autopilot *(archived)* | Signal K plugin controlling Raymarine autopilots with proprietary NMEA 2000 PGNs | 12 | <https://github.com/sbender9/signalk-raymarine-autopilot> |
| RMRadar_pi | OpenCPN plugin for Raymarine digital radar via its undocumented network protocol | 11 | <https://github.com/ab2nkovs/RMRadar_pi> |
| parsefsh | Decodes Raymarine ARCHIVE.FSH files and Garmin IMG/ADM archives | 10 | <https://github.com/rahra/parsefsh> |
| dragonsdr_dji_droneid | Detects DJI DroneID with DragonSDR and publishes it over ZMQ | 9 | <https://github.com/alphafox02/dragonsdr_dji_droneid> |

## Casting & TV Remotes

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| miraclecast | Miracast (Wi-Fi Display) sink and source implementation for Linux | 4,344 | <https://github.com/albfan/miraclecast> |
| castnow *(archived)* | commandline chromecast player | 3,810 | <https://github.com/xat/castnow> |
| catt | Cast All The Things allows you to send videos from many, many online sources to your Chromecast. | 3,701 | <https://github.com/skorokithakis/catt> |
| go-chromecast | cli for Google Chromecast, Home devices and Cast Groups | 976 | <https://github.com/vishen/go-chromecast> |
| ytcast | Casts YouTube videos to smart TVs from the command line via DIAL and Lounge API | 803 | <https://github.com/MarcoLucidi01/ytcast> |
| node-castv2 | An implementation of the Chromecast CASTV2 protocol | 792 | <https://github.com/thibauts/node-castv2> |
| samsungctl *(archived)* | Remote control Samsung televisions via a TCP/IP connection | 741 | <https://github.com/Ape/samsungctl> |
| node-sonos | Sonos Media Player Interface/Client | 724 | <https://github.com/bencevans/node-sonos> |
| homebridge-webos-tv | Homebridge plugin for LG webOS TVs | 706 | <https://github.com/merdok/homebridge-webos-tv> |
| homebridge-samsung-tizen | Homebridge plugin for Samsung TV's with Tizen OS | 677 | <https://github.com/tavicu/homebridge-samsung-tizen> |
| node-castv2-client | A Chromecast client based on the new (CASTV2) protocol | 658 | <https://github.com/thibauts/node-castv2-client> |
| adb_shell | Pure Python implementation of the ADB protocol with shell and FileSync | 607 | <https://github.com/JeffLIrion/adb_shell> |
| ps4-waker | Wakes and controls a PS4 over LAN using the PlayStation App protocol | 464 | <https://github.com/dhleong/ps4-waker> |
| plex-mpv-shim | Cast from Plex apps to MPV via the Plex player protocol | 412 | <https://github.com/iwalton3/plex-mpv-shim> |
| bscpylgtv | Library to control webOS based LG TV devices | 362 | <https://github.com/chros73/bscpylgtv> |
| python-roku | Screw remotes. Control your Roku with Python. | 348 | <https://github.com/jcarbaugh/python-roku> |
| SharpCaster | Chromecast C# CLI and SDK | 336 | <https://github.com/Tapanila/SharpCaster> |
| chromecast-java-api-v2 | Java implementation of ChromeCast V2 protocol client | 276 | <https://github.com/vitalidze/chromecast-java-api-v2> |
| lgtv.js | Control LG WebOS TV using node.js | 261 | <https://github.com/msloth/lgtv.js> |
| samsung-tv-control | Remote control your TV via JS! | 197 | <https://github.com/Toxblh/samsung-tv-control> |
| python-androidtv | Communicate with an Android TV or Fire TV device via ADB over a network. | 196 | <https://github.com/JeffLIrion/python-androidtv> |
| homebridge-lgwebos-tv | Homebridge plugin for LG WebOS TV, publish as independent external platform accessory. | 169 | <https://github.com/grzegorz914/homebridge-lgwebos-tv> |
| rust-cast | Library written in Rust to communicate with the Google Cast devices | 158 | <https://github.com/azasypkin/rust-cast> |
| playactor | Controls PS4/PS5 consoles over the PlayStation second-screen protocol | 157 | <https://github.com/dhleong/playactor> |
| GoogleCast | Implementation of the Google Cast protocol (.NET Standard 2.0 library) | 147 | <https://github.com/kakone/GoogleCast> |
| androidtvremote2 | Python library implementing the Android TV Remote protocol v2 | 133 | <https://github.com/tronikos/androidtvremote2> |
| pyvizio | Python client for Vizio SmartCast | 129 | <https://github.com/raman325/pyvizio> |
| lgtv-ip-control | IP Control module for 2018+ LG TVs | 125 | <https://github.com/WesSouza/lgtv-ip-control> |
| node-sonos-ts | Sonos control library, use this library in your own appliction. | 111 | <https://github.com/svrooij/node-sonos-ts> |
| spotcontrol | Open-source Spotify Connect controller in Go | 110 | <https://github.com/badfortrains/spotcontrol> |
| androidtv-remote | Node.js library implementing the Android TV Remote v2 pairing and remote protocol | 88 | <https://github.com/louis49/androidtv-remote> |
| sonos-api-docs | Documentation and client generator for the Sonos local UPnP API | 59 | <https://github.com/svrooij/sonos-api-docs> |
| aiowebostv | Python library to control LG webOS based TV devices | 56 | <https://github.com/home-assistant-libs/aiowebostv> |
| aioharmony | Asyncio Python library for the Logitech Harmony Hub local protocol | 28 | <https://github.com/Harmony-Libs/aioharmony> |
| EcpEmuServer | Emulates a Roku ECP device so Harmony and similar remotes can trigger webhooks | 28 | <https://github.com/logantgt/EcpEmuServer> |
| go-cast | An implementation of the Google Cast protocol, written in Go, with custom Chromecast Remote and Receiver apps | 24 | <https://github.com/tristanpenman/go-cast> |
| pylgnetcast | Python client for LG NetCast (pre-webOS) TV remote control API | 13 | <https://github.com/wokar/pylgnetcast> |
| python-rokuecp | Asynchronous Python client for Roku (ECP) | 9 | <https://github.com/ctalkington/python-rokuecp> |
| pybravia | Python async library for remote control of Sony Bravia TVs 2013 and newer. | 7 | <https://github.com/Drafteed/pybravia> |
| sonos-websocket | An asynchronous Python library to communicate with Sonos devices over websockets | 7 | <https://github.com/jjlawren/sonos-websocket> |

## Cellular Modem Diagnostics

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| QCSuper | Capture 2G/3G/4G signaling from your own Qualcomm phone or modem via the DIAG protocol | 1,662 | <https://github.com/P1sec/QCSuper> |
| FirmWire | Full-system emulation of Samsung Shannon and MediaTek baseband firmware | 887 | <https://github.com/FirmWire/FirmWire> |
| SCAT | Signaling collection from Qualcomm and Samsung Shannon modem diagnostic interfaces | 542 | <https://github.com/fgsect/scat> |
| xmm7360-pci | Reverse-engineered Linux driver for the Intel XMM7360 (Fibocom L850-GL) LTE modem | 485 | <https://github.com/xmm7360/xmm7360-pci> |
| shannonRE | Scripts for reverse engineering the Samsung Shannon baseband firmware | 264 | <https://github.com/Comsecuris/shannonRE> |
| mediatek-lte-baseband-re | Notes and tools for reverse engineering the MediaTek LTE baseband and Coresonic DSP | 227 | <https://github.com/cyrozap/mediatek-lte-baseband-re> |
| balong-usbdload | Emergency USB boot loader for Huawei Balong V7 modems | 213 | <https://github.com/forth32/balong-usbdload> |
| balongflash | Flasher for Huawei modems on the Balong V7 chipset | 213 | <https://github.com/forth32/balongflash> |
| ShannonBaseband | Scripts, Ghidra loaders and notes for Samsung's Shannon baseband | 187 | <https://github.com/grant-h/ShannonBaseband> |
| xmm7360-usb-modeswitch | Tools for the Fibocom L850-GL / Intel XMM7360 LTE modem on Linux | 143 | <https://github.com/xmm7360/xmm7360-usb-modeswitch> |
| MobileInsight core | Parses Qualcomm and MediaTek modem diagnostic logs on your own device | 139 | <https://github.com/mobile-insight/mobileinsight-core> |
| shannon_modem_loader | IDA Pro loader for Exynos/Shannon baseband modem firmware images | 87 | <https://github.com/alexander-pick/shannon_modem_loader> |
| mtk_bp | MediaTek baseband processor firmware tools | 81 | <https://github.com/nccgroup/mtk_bp> |
| qc_debug_monitor | Debug message monitor for Qualcomm cellular modems | 79 | <https://github.com/Cr4sh/qc_debug_monitor> |
| aristoteles | Wireshark dissector for Apple's ARI protocol between iPhone and Intel basebands | 74 | <https://github.com/seemoo-lab/aristoteles> |
| qhuaweiflash | GUI to flash Huawei modems/routers and edit their firmware files | 71 | <https://github.com/forth32/qhuaweiflash> |
| diag-parser | Parses Qualcomm DIAG logs and converts them to GSMTAP | 68 | <https://github.com/moiji-mobile/diag-parser> |
| shannon-dbg | Debugger for the Samsung Shannon baseband firmware | 60 | <https://github.com/synacktiv/shannon-dbg> |
| ShannonEE *(archived)* | Dynamic analysis environment for Samsung's Shannon baseband (predecessor of FirmWire) | 44 | <https://github.com/grant-h/ShannonEE> |
| DiagLibrary | Library using the Qualcomm DIAG port for band and frequency locking on your own device | 26 | <https://github.com/sanjaywave/DiagLibrary> |
| osmo-qcdiag | Osmocom tools for the Qualcomm DIAG interface | 21 | <https://github.com/osmocom/osmo-qcdiag> |
| QC-Native-Diag | Standalone C++ Qualcomm DIAG tool written from scratch | 15 | <https://github.com/alisakkaf/QC-Native-Diag> |

## Digital Voice Radio

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| SDRTrunk | Decode and follow P25, DMR, LTR, MPT1327 and other trunked radio systems | 2,206 | <https://github.com/DSheirer/sdrtrunk> |
| trunk-recorder | Record calls from P25 and Motorola SmartNet trunked radio systems | 1,151 | <https://github.com/TrunkRecorder/trunk-recorder> |
| MMDVMHost | Host program for MMDVM digital voice hotspots (D-Star, DMR, YSF, P25, NXDN) | 452 | <https://github.com/g4klx/MMDVM-Host> |
| dsdcc | Digital Speech Decoder rewritten as a C++ library for DMR, D-Star, YSF, dPMR and more | 328 | <https://github.com/f4exb/dsdcc> |
| mbelib | Implementation of the proprietary IMBE/AMBE vocoders used in P25, DMR and ProVoice | 320 | <https://github.com/szechyjs/mbelib> |
| TETRA_crypto | Reverse engineered TETRA cryptographic primitives (TEA ciphers, TAA1) | 216 | <https://github.com/MidnightBlueLabs/TETRA_crypto> |
| md380-re *(archived)* | MD380 DMR radio reverse engineering | 127 | <https://github.com/pchickey/md380-re> |
| osmo-tetra-sq5bpf | osmo-tetra with patches to decode TETRA SDS messages and feed telive | 64 | <https://github.com/sq5bpf/osmo-tetra-sq5bpf> |
| gr-ysf | GNU Radio modules decoding Yaesu System Fusion C4FM packets | 61 | <https://github.com/HB9UF/gr-ysf> |
| tetra-listener | Records and decodes unencrypted TETRA voice calls with an SDR | 59 | <https://github.com/itds-consulting/tetra-listener> |
| gr-smartnet | GNU Radio logging scanner for Motorola SmartNet II trunking | 48 | <https://github.com/bistromath/gr-smartnet> |
| tetra-rtlsdr | Single C binary RTL-SDR front-end for TETRA decoding with telive | 45 | <https://github.com/alphafox02/tetra-rtlsdr> |
| edacs-fm *(archived)* | EDACS trunked radio tracking with an RTL-SDR | 13 | <https://github.com/lwvmobile/edacs-fm> |

## Email & Groupware

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| hydroxide *(archived)* | Third-party ProtonMail bridge providing IMAP, SMTP and CardDAV | 2,170 | <https://github.com/emersion/hydroxide> |
| exchangelib | Python client for Microsoft Exchange Web Services (EWS) | 1,273 | <https://github.com/ecederstrand/exchangelib> |
| TbSync | [Thunderbird Add-On] Central user interface to manage cloud accounts and to synchronize their contact, task and... | 919 | <https://github.com/jobisoft/TbSync> |
| php-ews | PHP Exchange Web Services | 574 | <https://github.com/jamesiarmes/php-ews> |
| gromox | Groupware server implementing Exchange MAPI/HTTP, RPC/HTTP, EWS and IMAP | 264 | <https://github.com/grommunio/gromox> |
| EAS-4-TbSync | [Thunderbird Add-On] The Exchange ActiveSync provider for TbSync to sync contacts, tasks and calendars to Thunderbird. | 251 | <https://github.com/jobisoft/EAS-4-TbSync> |
| Viewpoint | A Ruby client access library for Microsoft Exchange Web Services (EWS) | 248 | <https://github.com/WinRb/Viewpoint> |
| pyexchange | Python wrapper for Microsoft Exchange | 154 | <https://github.com/linkedin/pyexchange> |
| node-ews | A simple JSON wrapper for the Exchange Web Services (EWS) SOAP API. | 116 | <https://github.com/nmarus/node-ews> |
| ruby-msg | Ruby library for reading Outlook .msg and .pst (MAPI message store) files | 103 | <https://github.com/aquasync/ruby-msg> |
| akonadi-ews | Akonadi resource agent for Microsoft Exchange using Exchange Web Services (EWS) protocol | 95 | <https://github.com/KrissN/akonadi-ews> |
| ews-cpp | A C++11 header-only library for Microsoft Exchange Web Services | 77 | <https://github.com/otris/ews-cpp> |
| evolution-ews | Read-only mirror of https://gitlab.gnome.org/GNOME/evolution-ews | 65 | <https://github.com/GNOME/evolution-ews> |
| evolution-activesync | Read-only mirror of https://gitlab.gnome.org/GNOME/evolution-activesync | 40 | <https://github.com/GNOME/evolution-activesync> |
| grommunio-sync | EAS (Exchange ActiveSync) interface for grommunio | 40 | <https://github.com/grommunio/grommunio-sync> |
| pyActiveSync | A pure python library for the ActiveSync protocol | 39 | <https://github.com/solbirn/pyActiveSync> |
| jsas *(archived)* | DEPRECATED - A Javascript ActiveSync library | 35 | <https://github.com/mozilla-b2g/jsas> |
| ews-rs | A Rust crate for interacting with the Exchange Web Services API | 34 | <https://github.com/thunderbird/ews-rs> |
| syncroton | Syncroton is a PHP based implementation of the Exchange ActiveSync protocol, which is licensed under the LGPL V3 | 24 | <https://github.com/tine20/syncroton> |
| node-asclient | Node.js client for Exchange ActiveSync synchronization | 21 | <https://github.com/clncln1/node-asclient> |
| activesync-go | ActiveSync implementation for Google Go | 19 | <https://github.com/magicmonty/activesync-go> |
| PyWBXMLDecoder | Decoder for Exchange ActiveSync WAP Binary XML (WBXML) | 19 | <https://github.com/davidpshaw/PyWBXMLDecoder> |

## File Sharing & Remote Desktop

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| Sunshine | Self-hosted game stream host that implements the NVIDIA GameStream protocol for Moonlight clients | 42,101 | <https://github.com/LizardByte/Sunshine> |
| moonlight-qt | Open-source NVIDIA GameStream / Sunshine client for Windows, macOS, Linux and Steam Link | 19,048 | <https://github.com/moonlight-stream/moonlight-qt> |
| Impacket | Python classes for SMB, MSRPC, NTLM, Kerberos, LDAP and other Windows protocols | 16,162 | <https://github.com/fortra/impacket> |
| FreeRDP | Free implementation of Microsoft's Remote Desktop Protocol (client and server libraries) | 13,812 | <https://github.com/FreeRDP/FreeRDP> |
| OpenDrop | Open AirDrop implementation in Python, protocol-compatible with iOS/macOS | 9,848 | <https://github.com/seemoo-lab/opendrop> |
| Shairport Sync | AirPlay and AirPlay 2 audio receiver for Linux/BSD | 8,886 | <https://github.com/mikebrady/shairport-sync> |
| moonlight-android | Open-source NVIDIA GameStream client for Android | 7,270 | <https://github.com/moonlight-stream/moonlight-android> |
| xrdp | Open source RDP server for Linux | 6,758 | <https://github.com/neutrinolabs/xrdp> |
| NearDrop | Unofficial Google Nearby Share/Quick Share receiver for macOS from reversed protocol | 6,294 | <https://github.com/grishka/NearDrop> |
| rquickshare | Rust implementation of Android Nearby Share / Quick Share for Linux and macOS | 3,634 | <https://github.com/Martichou/rquickshare> |
| IronRDP | Rust implementation of the Microsoft Remote Desktop Protocol (RDP) | 3,219 | <https://github.com/Devolutions/IronRDP> |
| UxPlay | AirPlay mirroring server for Unix (reverse-engineered AirPlay 2 protocol) | 3,166 | <https://github.com/FDH2/UxPlay> |
| RDPY | Microsoft RDP protocol implementation in Python: client, server, MitM, honeypot | 1,733 | <https://github.com/citronneur/rdpy> |
| moonlight-ios | Open-source NVIDIA GameStream client for iOS and tvOS | 1,686 | <https://github.com/moonlight-stream/moonlight-ios> |
| OWL (Open Wireless Link) | Open implementation of Apple Wireless Direct Link (AWDL) for Linux and macOS | 1,565 | <https://github.com/seemoo-lab/owl> |
| moonlight-tv | Lightweight GameStream client for LG webOS TVs and embedded devices | 1,495 | <https://github.com/mariotaku/moonlight-tv> |
| rdesktop | Original open source RDP client for Unix, built from reverse engineering | 1,354 | <https://github.com/rdesktop/rdesktop> |
| Samba | SMB/CIFS file, print and AD domain server; SMB reverse engineered long before MS published specs | 1,143 | <https://github.com/samba-team/samba> |
| moonlight-common-c | Core implementation of NVIDIA's reverse-engineered GameStream protocol | 579 | <https://github.com/moonlight-stream/moonlight-common-c> |
| libsmb2 | Userspace SMB2/3 client library in C | 432 | <https://github.com/sahlberg/libsmb2> |
| go-smb2 | SMB2/3 client library written in Go | 410 | <https://github.com/hirochachacha/go-smb2> |
| smbprotocol | Python SMBv2/v3 client implementation | 401 | <https://github.com/jborean93/smbprotocol> |
| ksmbd | In-kernel Linux SMB3 server | 373 | <https://github.com/namjaejeon/ksmbd> |

## Legacy IM Revival

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| PFire | Emulated Xfire server for the 1.127 client | 59 | <https://github.com/darcymiranda/PFire> |
| MSN | MSN Messenger server reimplementation | 22 | <https://github.com/v1ckxy/MSN> |

## Messaging Protocols

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| Baileys | Socket-based TypeScript API for WhatsApp Web | 11,306 | <https://github.com/WhiskeySockets/Baileys> |
| whatsmeow | Go library for the WhatsApp web multi-device API | 7,538 | <https://github.com/tulir/whatsmeow> |
| mautrix-whatsapp | Matrix-WhatsApp puppeting bridge | 1,900 | <https://github.com/mautrix/whatsapp> |
| Open OSCAR Server (Retro AIM Server) | Self-hostable server compatible with classic AIM and ICQ clients (OSCAR protocol) | 1,581 | <https://github.com/mk6i/open-oscar-server> |
| purple-facebook | Facebook Messenger (MQTT) protocol plugin for libpurple | 950 | <https://github.com/dequis/purple-facebook> |
| BitlBee | IRC gateway to other chat networks (OSCAR, MSN, Jabber, Twitter...) | 646 | <https://github.com/bitlbee/bitlbee> |
| skype4pidgin *(archived)* | Skype protocol plugin for Pidgin/libpurple (SkypeWeb) | 622 | <https://github.com/EionRobb/skype4pidgin> |
| mautrix-meta | Matrix bridge for Facebook Messenger and Instagram DMs | 446 | <https://github.com/mautrix/meta> |
| purple-discord | Discord protocol plugin for Pidgin/libpurple | 432 | <https://github.com/EionRobb/purple-discord> |
| purple-gowhatsapp | WhatsApp plugin for Pidgin/libpurple built on whatsmeow | 364 | <https://github.com/hoehermann/purple-gowhatsapp> |
| purple-teams | Third-party Microsoft Teams plugin for Pidgin/libpurple | 214 | <https://github.com/EionRobb/purple-teams> |
| fossteams/teams-api | Unofficial Go library for Microsoft Teams internal APIs used by the official clients | 164 | <https://github.com/fossteams/teams-api> |
| ts3j | Open-source Java TeamSpeak 3 client library using the full client protocol | 132 | <https://github.com/Manevolent/ts3j> |
| mautrix-googlechat | Matrix-Google Chat puppeting bridge | 127 | <https://github.com/mautrix/googlechat> |
| poggadaj | Open Source reimplementation of Gadu-Gadu backend (official mirror of https://codeberg.org/or3e/poggadaj) | 8 | <https://github.com/Oreeeee/poggadaj> |
| zoomer | Zoom chat bots via reverse-engineered Zoom Web SDK websocket protocol | 4 | <https://github.com/RealKeyboardWarrior/zoomer> |

## Other Protocols

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| librespot | Open source Spotify Connect client library in Rust | 7,275 | <https://github.com/librespot-org/librespot> |
| SteamKit2 | .NET library interoperating with Valve's Steam network protocol | 3,208 | <https://github.com/SteamRE/SteamKit> |
| SteamTracking | Tracks Steam client files, protobufs and API changes for research | 1,108 | <https://github.com/SteamTracking/SteamTracking> |
| chrome-x-browser-validation-header | Reverse-engineered Chrome's private X-Browser-Validation integrity header; generator toolkit | 333 | <https://github.com/dsekz/chrome-x-browser-validation-header> |
| sspks | Simple Synology package server reverse engineered from the official package repository protocol | 279 | <https://github.com/jdel/sspks> |
| HelicopterDemod | Reverse-engineered news helicopter downlink radio protocol from audio in video | 168 | <https://github.com/proto17/HelicopterDemod> |
| OpenChirp | Reverse engineered implementation of the Chirp data-over-audio protocol | 108 | <https://github.com/cawfree/OpenChirp> |
| open-ds | Reverse engineered lightweight cross-platform FRC Driver Station | 60 | <https://github.com/Boomaa23/open-ds> |
| wow_messages | Auto generated messages for the World of Warcraft network protocol | 53 | <https://github.com/gtker/wow_messages> |
| wow_srp | Library for World of Warcraft flavor of SRP6 authentication. | 19 | <https://github.com/gtker/wow_srp> |
| project-mayhem | Reverse-engineered Streamate webcam protocol; native client | 7 | <https://github.com/giannitedesco/project-mayhem> |

## Proprietary Enterprise Protocols

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| openfortivpn | Client for Fortinet's PPP+TLS SSL-VPN tunnels | 3,438 | <https://github.com/adrienverge/openfortivpn> |
| GlobalProtect-openconnect | Palo Alto GlobalProtect VPN client for Linux/macOS, based on OpenConnect | 2,287 | <https://github.com/yuezk/GlobalProtect-openconnect> |
| tedious | Pure JavaScript implementation of the TDS protocol for SQL Server | 1,616 | <https://github.com/tediousjs/tedious> |
| pywinrm | Python library for Windows Remote Management (WinRM) | 1,140 | <https://github.com/diyan/pywinrm> |
| go-ora | Pure Go Oracle client implementing the TNS wire protocol | 984 | <https://github.com/sijms/go-ora> |
| gokrb5 | Pure Go Kerberos library for clients and services | 781 | <https://github.com/jcmturner/gokrb5> |
| DavMail | POP/IMAP/SMTP/CalDAV/LDAP gateway to Exchange and Office 365 (EWS/WebDAV) | 766 | <https://github.com/mguessan/davmail> |
| libnfs | NFS client library | 603 | <https://github.com/sahlberg/libnfs> |
| Kerberos.NET | A Kerberos implementation built entirely in managed code. | 567 | <https://github.com/dotnet/Kerberos.NET> |
| FreeTDS | Reimplementation of Sybase/Microsoft SQL Server TDS wire protocol | 504 | <https://github.com/FreeTDS/freetds> |
| winrm | Command-line tool and library for Windows remote command execution in Go | 478 | <https://github.com/masterzen/winrm> |
| python-fints | Pure-Python FinTS/HBCI banking protocol client | 424 | <https://github.com/raphaelm/python-fints> |
| pypsrp | PowerShell Remoting Protocol for Python | 391 | <https://github.com/jborean93/pypsrp> |
| network-audio-controller | Unofficial Dante Controller alternative for multiple platforms | 370 | <https://github.com/chris-ritsen/network-audio-controller> |
| inferno | Unofficial implementation of the Dante audio-over-IP protocol | 349 | <https://github.com/teodly/inferno> |
| hibiscus | Free home-banking app for Linux, Windows and macOS built on HBCI4Java | 344 | <https://github.com/willuhn/hibiscus> |
| jcifs-ng | A cleaned-up and improved version of the jCIFS library | 344 | <https://github.com/AgNO3/jcifs-ng> |
| go-ntlmssp | NTLM/Negotiate authentication over HTTP | 203 | <https://github.com/Azure/go-ntlmssp> |
| hbci4java | Java FinTS/HBCI implementation with chipTAN, pushTAN and SEPA support | 193 | <https://github.com/hbci4j/hbci4java> |
| OpenChange | Open implementation of Microsoft Exchange MAPI/RPC protocols | 174 | <https://github.com/openchange/openchange> |
| eoip | Linux kernel EoIP tunnel compatible with MikroTik | 163 | <https://github.com/bbonev/eoip> |
| phpFinTS | PHP library to communicate with FinTS/HBCI bank servers | 162 | <https://github.com/nemiah/phpFinTS> |
| Z-Push | Open source Exchange ActiveSync implementation for syncing mobile devices | 156 | <https://github.com/Z-Hub/Z-Push> |
| open_fints_js_client | JavaScript FinTS/HBCI client | 135 | <https://github.com/jschyma/open_fints_js_client> |
| SIPE | Third-party Pidgin plugin for the Microsoft Lync/OCS protocol | 130 | <https://github.com/tieto/sipe> |
| wycliffe | Clean-room implementation of the Dante audio protocol | 128 | <https://github.com/jsharkey/wycliffe> |
| unifi-inform-protocol | Documentation of the reverse engineered Ubiquiti UniFi inform protocol | 119 | <https://github.com/jeffreykog/unifi-inform-protocol> |
| SAP Wireshark dissectors | Wireshark dissectors for proprietary SAP NI, Diag, RFC, Router, Enqueue protocols | 114 | <https://github.com/SecureAuthCorp/SAP-Dissection-plug-in-for-Wireshark> |
| smb-rs | Pure Rust SMB2/3 client | 86 | <https://github.com/afiffon/smb-rs> |
| OpenURMA | Clean-room open implementation of the Unified Bus protocol | 80 | <https://github.com/bojieli/OpenURMA> |
| pyspnego | Python SPNEGO authentication library | 66 | <https://github.com/jborean93/pyspnego> |
| libfintx | .NET client library for HBCI, FinTS and EBICS banking protocols | 65 | <https://github.com/libfintx/libfintx> |
| unifi-protocol-reverse-engineering | Reverse engineered docs for the protocol between UniFi APs and controller | 60 | <https://github.com/fxkr/unifi-protocol-reverse-engineering> |
| gss-ntlmssp | GSSAPI implementation of Microsoft NTLM (MS-NLMP) | 42 | <https://github.com/gssapi/gss-ntlmssp> |
| outlook-dndprotocol | Reverse-engineered Outlook drag-and-drop OLE clipboard protocol | 4 | <https://github.com/yasoonOfficial/outlook-dndprotocol> |

## Radio & SDR Protocols

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| dump1090 | Dump1090 is a simple Mode S decoder for RTLSDR devices | 2,952 | <https://github.com/antirez/dump1090> |
| SatDump | Decodes weather/earth-observation satellite downlinks and their data formats | 2,315 | <https://github.com/SatDump/SatDump> |
| rc-switch | Arduino library to operate cheap 433/315 MHz remote-controlled outlets and decode their protocols | 2,088 | <https://github.com/sui77/rc-switch> |
| gr-gsm | Gnuradio blocks and tools for receiving GSM transmissions | 1,506 | <https://github.com/ptrkrysik/gr-gsm> |
| wmbusmeters | Read the wired or wireless mbus protocol to acquire utility meter readings. | 1,341 | <https://github.com/wmbusmeters/wmbusmeters> |
| multimon-ng | Decoder for POCSAG/FLEX pagers, EAS, DTMF, AFSK and other digital radio modes | 1,143 | <https://github.com/EliasOenal/multimon-ng> |
| gr-lora_sdr | This is the fully-functional GNU Radio software-defined radio (SDR) implementation of a LoRa transceiver with all... | 1,012 | <https://github.com/tapparelj/gr-lora_sdr> |
| nrsc5 | Receiver for the proprietary NRSC-5 (HD Radio) digital broadcast standard | 970 | <https://github.com/theori-io/nrsc5> |
| zwave-js | Modern and standards-compliant Z-Wave device driver that runs almost anywhere | 891 | <https://github.com/zwave-js/zwave-js> |
| esp-sdr | Uses undocumented raw I/Q capture of ESP32 chips as an SDR | 841 | <https://github.com/ESPARGOS/esp-sdr> |
| dsd | Digital Speech Decoder | 790 | <https://github.com/szechyjs/dsd> |
| rtl_433_ESP | Port of rtl_433 decoders to ESP32 with CC1101/SX127x radios | 731 | <https://github.com/NorthernMan54/rtl_433_ESP> |
| readsb | ADS-B decoder swiss knife | 689 | <https://github.com/wiedehopf/readsb> |
| pyModeS | Python decoder for Mode S and ADS-B signals | 669 | <https://github.com/junzis/pyModeS> |
| gr-lora | GNU Radio blocks for receiving LoRa modulated radio messages using SDR | 643 | <https://github.com/rpp0/gr-lora> |
| radiosonde_auto_rx | Automatically track and decode weather radiosonde launches with an RTL-SDR | 615 | <https://github.com/projecthorus/radiosonde_auto_rx> |
| protoview | Flipper Zero app to display and decode known and unknown sub-GHz signals | 597 | <https://github.com/antirez/protoview> |
| gr-lora | GNU Radio OOT module implementing the LoRa PHY, based on... | 513 | <https://github.com/BastilleResearch/gr-lora> |
| nrf24_multipro | nRF24L01 transmitter for reverse-engineered toy drone and RC protocols | 505 | <https://github.com/goebish/nrf24_multipro> |
| gr-iridium | Iridium burst detector and demodulator. | 494 | <https://github.com/muccc/gr-iridium> |
| op25 | Fork of osmocom OP25 by boatbod | 486 | <https://github.com/boatbod/op25> |
| Quansheng_UV-K5_PCB_R51-V1.4_PCB_Reversing_Rev._0.9 | KiCad reverse engineering of the Quansheng UV-K5 handheld radio PCB | 414 | <https://github.com/mentalDetector/Quansheng_UV-K5_PCB_R51-V1.4_PCB_Reversing_Rev._0.9> |
| acarsdec *(archived)* | ACARS SDR decoder | 380 | <https://github.com/TLeconte/acarsdec> |
| tpms *(archived)* | Tire Pressure Monitoring System decoding tools. | 371 | <https://github.com/jboone/tpms> |
| rdz_ttgo_sonde | ESP32/LoRa board firmware decoding RS41, RS92, DFM and M10/M20 radiosondes | 356 | <https://github.com/dl9rdz/rdz_ttgo_sonde> |
| telive | Live TETRA monitor built on osmo-tetra | 333 | <https://github.com/sq5bpf/telive> |
| rtl-wmbus | Software defined receiver for wireless M-Bus with RTL-SDR | 282 | <https://github.com/xaelsouth/rtl-wmbus> |
| dspectrumgui | GUI to demodulate basic RF transmissions for reverse engineering | 280 | <https://github.com/tresacton/dspectrumgui> |
| pilight | Home automation daemon that decodes and sends many proprietary 433 MHz device protocols | 280 | <https://github.com/pilight/pilight> |
| LoRa-SDR | SDR implementation of the proprietary LoRa PHY for research | 275 | <https://github.com/myriadrf/LoRa-SDR> |
| dumpvdl2 | VDL Mode 2 message decoder and protocol analyzer | 259 | <https://github.com/szpajder/dumpvdl2> |
| Somfy_Remote | Arduino sketch that emulates a Somfy RTS remote (rolling-code protocol) | 237 | <https://github.com/Nickduino/Somfy_Remote> |
| decoder | Library that decodes BLE advertising payloads of hundreds of proprietary sensors | 210 | <https://github.com/theengs/decoder> |
| RS radiosonde decoders | Decoders for Vaisala, Graw, Meteomodem, Intermet and other radiosonde formats | 205 | <https://github.com/rs1729/RS> |
| re-DECTed | RTL-SDR tools that receive DECT packets and feed them to Wireshark | 157 | <https://github.com/znuh/re-DECTed> |
| LoRaPHY | Complete LoRa physical layer (LoRa PHY) implementation in MATLAB. | 156 | <https://github.com/jkadbear/LoRaPHY> |
| Baofeng-UV-5RM-5RH-RE | Reverse engineering of the Baofeng UV-5RM/UV-5RH radios | 148 | <https://github.com/amoxu/Baofeng-UV-5RM-5RH-RE> |
| sdrpp_radiosonde | SDR++ plugin decoding RS41, DFM, M10/M20 and other radiosondes | 123 | <https://github.com/dbdexter-dev/sdrpp_radiosonde> |
| gr-dect2 | GNU Radio receiver and decoder for DECT (cordless phone) voice channels | 121 | <https://github.com/pavelyazev/gr-dect2> |
| matt-knight research | Publications incl. the LoRa PHY reverse engineering paper and code | 118 | <https://github.com/matt-knight/research> |
| gr-reveng | GNU Radio utilities for reverse engineering RF protocols | 95 | <https://github.com/tkuester/gr-reveng> |
| gr-lora | LoRa physical layer collision decoding based on GNU Radio | 84 | <https://github.com/jkadbear/gr-lora> |
| osmo-tetra | Osmocom TETRA MAC/PHY receive and decode code | 81 | <https://github.com/osmocom/osmo-tetra> |
| dspectrum | Automated RF signal analysis for reverse engineering unknown OOK/ASK devices | 71 | <https://github.com/tresacton/dspectrum> |
| RS41_Decoding | Reverse engineering the Vaisala RS41 radiosonde data frame format | 70 | <https://github.com/bazjo/RS41_Decoding> |
| nrsc5-gui | Graphical interface for the nrsc5 HD Radio receiver | 64 | <https://github.com/cmnybo/nrsc5-gui> |
| PyEOT | GNU Radio/Python decoder for railroad End-of-Train telemetry packets | 64 | <https://github.com/ereuter/PyEOT> |
| OpenWXSDR | SDR receiver and decoder for weather radiosondes | 40 | <https://github.com/DL2MF/OpenWXSDR> |
| tetra-toolkit | Tools and documentation for decoding TETRA radio | 38 | <https://github.com/Tim---/tetra-toolkit> |
| pyinsteon | Python library for the Insteon home automation protocol | 31 | <https://github.com/pyinsteon/pyinsteon> |
| librenard | Reverse-engineered Sigfox protocol stack library | 27 | <https://github.com/Jeija/librenard> |
| renard-phy | Open Sigfox physical-layer implementation for SDR | 25 | <https://github.com/Jeija/renard-phy> |
| gascop | A lightweight POCSAG decoder for rtl-sdr devices | 24 | <https://github.com/yuvadm/gascop> |
| Radiosonde decoder and tracker for Windows | Windows radiosonde decoder and tracker built on RTL-SDR | 24 | <https://github.com/9A4AM/Radiosonde-decoder-and-tracker-for-Windows> |
| gr-pocsag-decoder | GNU Radio POCSAG Receiver and Python Decoder | 18 | <https://github.com/keithdoggett/gr-pocsag-decoder> |
| sondedump | Extensible decoder for proprietary radiosonde telemetry formats | 18 | <https://github.com/dbdexter-dev/sondedump> |
| EOTDecode | Python decoder for railroad End-of-Train device radio telemetry | 13 | <https://github.com/russinnes/EOTDecode> |
| ft991a-interoperability-tools | Tools for the Yaesu FT-991A's undocumented memory and menu formats | 5 | <https://github.com/j0ju/ft991a-interoperability-tools> |
| sirf | Interpreter for the SiRF binary GPS protocol | 1 | <https://github.com/tryan/sirf> |
| SmallStep | Download and configure classic MTK GPS loggers over their binary protocol on M5Stack | 0 | <https://github.com/nuruposan/SmallStep> |

## Satellite Downlinks

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| gr-satellites | GNU Radio decoders for many amateur and cubesat telemetry formats, incl. undocumented ones | 992 | <https://github.com/daniestevez/gr-satellites> |
| iridium-toolkit | Tools to parse and decode Iridium satellite frames (pager, SBD, voice, ring alerts) | 581 | <https://github.com/muccc/iridium-toolkit> |
| goestools | Receive and decode GOES LRIT/HRIT satellite downlinks and their xRIT files with an RTL-SDR | 424 | <https://github.com/pietern/goestools> |
| JAERO | Demodulate and decode Inmarsat Aero signals carrying SatCom ACARS from aircraft | 274 | <https://github.com/jontio/JAERO> |
| iridium-sniffer | Standalone C Iridium burst detector and demodulator without GNU Radio | 214 | <https://github.com/alphafox02/iridium-sniffer> |
| jupyter_notebooks (Daniel Estévez) | Notebooks analysing and decoding undocumented satellite and spacecraft signals | 200 | <https://github.com/daniestevez/jupyter_notebooks> |
| meteor_decoder | Portable decoder for the Meteor-M LRPT weather satellite signal | 155 | <https://github.com/artlav/meteor_decoder> |
| meteor_demod | Demodulator for the Russian Meteor-M2 LRPT weather satellite downlink | 140 | <https://github.com/dbdexter-dev/meteor_demod> |
| L-Band-Decoders *(archived)* | Decoders for L-band HRPT satellites incl. MetOp, FengYun-3 and Meteor | 128 | <https://github.com/altillimity/L-Band-Decoders> |
| xrit-rx *(archived)* | Receiver and decoder for GEO-KOMPSAT-2A (GK-2A) LRIT weather satellite images | 102 | <https://github.com/sam210723/xrit-rx> |
| LeanHRPT-Decode *(archived)* | Decoder for HRPT downlinks from NOAA, MetOp, FengYun and Meteor weather satellites | 87 | <https://github.com/Xerbo/LeanHRPT-Decode> |
| free-outernet | Free software receiver for the reverse-engineered Outernet L-band satellite datacast | 85 | <https://github.com/daniestevez/free-outernet> |
| ORBCOMM-receiver | Software decoder for ORBCOMM satellite downlink transmissions | 84 | <https://github.com/fbieberly/ORBCOMM-receiver> |
| InmarScope | Multichannel Inmarsat Aero and STD-C decoder with call following | 66 | <https://github.com/SarahRoseLives/InmarScope> |
| himawari-rx *(archived)* | Receive Himawari-8 weather images from the HimawariCast satellite broadcast | 58 | <https://github.com/sam210723/himawari-rx> |
| IridiumLive | Web visualizer for Iridium frames decoded by gr-iridium | 58 | <https://github.com/microp11/iridiumlive> |
| goesdump | Dumper for GOES xRIT data from the Open Satellite Project demodulator | 56 | <https://github.com/opensatelliteproject/goesdump> |
| xritdemod | Open Satellite Project demodulator for GOES xRIT downlinks | 55 | <https://github.com/opensatelliteproject/xritdemod> |
| Standalone-Demodulators *(archived)* | Standalone demodulators for weather satellite downlinks replacing GNU Radio flowgraphs | 51 | <https://github.com/altillimity/Standalone-Demodulators> |
| inmarsat-sniffer | Standalone Inmarsat L-band decoder for STD-C EGC and Aero ACARS/ADS-C/CPDLC | 50 | <https://github.com/alphafox02/inmarsat-sniffer> |
| grcon2020-workshop | Workshop materials on decoding interplanetary spacecraft telemetry with GNU Radio | 47 | <https://github.com/daniestevez/grcon2020-workshop> |
| starlink-rs | Rust client for the undocumented Starlink user-terminal gRPC endpoint | 46 | <https://github.com/ewilken/starlink-rs> |
| meteor_decode | Decoder that turns Meteor-M2 LRPT soft symbols into weather images | 44 | <https://github.com/dbdexter-dev/meteor_decode> |
| COMS-1 *(archived)* | Receive and decode weather images from the COMS-1 geostationary satellite | 41 | <https://github.com/sam210723/COMS-1> |
| gr-hrpt | GNU Radio blocks for NOAA, Meteor, MetOp and FengYun HRPT downlinks | 28 | <https://github.com/altillimity/gr-hrpt> |
| starlink-grpc-golang | Go bindings for the undocumented Starlink user-terminal gRPC API | 25 | <https://github.com/clarkzjw/starlink-grpc-golang> |
| metlrpt | Work-in-progress Meteor LRPT weather satellite decoder | 19 | <https://github.com/opensatelliteproject/metlrpt> |
| stdcdec | Open-source Inmarsat-C (STD-C) command-line decoder | 18 | <https://github.com/cropinghigh/stdcdec> |
| orbcomm-rx *(archived)* | Demodulator and decoder for the Orbcomm VHF subscriber transmitter downlink | 15 | <https://github.com/sam210723/orbcomm-rx> |
| inmarsatc | C++ Inmarsat-C decoder library | 10 | <https://github.com/cropinghigh/inmarsatc> |
| warc-iridium-sbd-decoder *(archived)* | Java library for decoding Iridium Short Burst Data packets | 10 | <https://github.com/usgs/warc-iridium-sbd-decoder> |
| ORBCOMM-receiver-lite | C implementation of a software decoder for ORBCOMM satellite transmissions | 8 | <https://github.com/fbieberly/ORBCOMM-receiver-lite> |

## Sub-GHz Sensors & Meters

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| rtlamr2mqtt | Send ERT/SCM utility meter readings from rtlamr to MQTT and Home Assistant | 639 | <https://github.com/allangood/rtlamr2mqtt> |
| SzczepanLeon esphome-components | ESPHome wM-Bus components decoding manufacturer-specific water/heat meter telegrams | 352 | <https://github.com/SzczepanLeon/esphome-components> |
| customer-assistance-buttons-sdr | Reversed encoders of retail customer assistance call buttons via SDR | 339 | <https://github.com/jimilinuxguy/customer-assistance-buttons-sdr> |
| dingdong | Digital ding-dong-ditch: replaying a wireless doorbell signal via SDR | 252 | <https://github.com/samyk/dingdong> |
| rtlamr-collect | Data aggregation for utility meter readings captured with rtlamr | 203 | <https://github.com/bemasher/rtlamr-collect> |
| RFLink32 | ESP32/ESP8266 RFLink port decoding many proprietary 433/868 MHz sensor and remote protocols | 196 | <https://github.com/cpainchaud/RFLink32> |
| BresserWeatherSensorReceiver | Receiver for Bresser 5/6/7-in-1 868 MHz weather sensor radio protocols | 192 | <https://github.com/matthias-bs/BresserWeatherSensorReceiver> |
| rf-car | Controlling toy RC cars with HackRF | 176 | <https://github.com/rgerganov/rf-car> |
| gr-elster | GNU Radio block decoding Elster R2S smart meter packets | 142 | <https://github.com/argilo/gr-elster> |
| weewx-sdr | WeeWX driver that reads proprietary weather sensor broadcasts via rtl_433 | 138 | <https://github.com/matthewwall/weewx-sdr> |
| ESPiLight | Arduino library porting pilight's 433.92 MHz device protocol decoders | 126 | <https://github.com/puuu/ESPiLight> |
| max-cube-protocol | Documentation of the eQ-3/ELV MAX! Cube radiator thermostat protocol | 118 | <https://github.com/Bouni/max-cube-protocol> |
| weewx-interceptor | WeeWX driver that intercepts uploads from Acurite, Ambient and other weather bridges | 115 | <https://github.com/matthewwall/weewx-interceptor> |
| openmili | Open implementation of the Mi-Light 2.4 GHz LED control protocol | 111 | <https://github.com/henryk/openmili> |
| AskSinPP | Arduino implementation of the HomeMatic BidCoS radio protocol | 110 | <https://github.com/pa-pa/AskSinPP> |
| DavisRFM69 | RFM69 library that receives the Davis Instruments weather station radio protocol | 96 | <https://github.com/dekay/DavisRFM69> |
| everblu-meters-esp8266-improved | ESP8266/ESP32 reader for Itron EverBlu Cyble meters with MQTT and ESPHome | 78 | <https://github.com/genestealer/everblu-meters-esp8266-improved> |
| Acuparse | Captures AcuRite Iris/Atlas station data from the Access/smartHUB bridge's private uploads | 64 | <https://github.com/acuparse/acuparse> |
| LightwaveRF | Arduino libraries for the LightwaveRF 433 MHz home automation protocol | 60 | <https://github.com/roberttidey/LightwaveRF> |
| rfcontroljs | Node.js protocol decoders for many 433 MHz switches and weather stations | 48 | <https://github.com/pimatic/rfcontroljs> |
| smeter | Read water and heat meter radio transmissions with GNU Radio | 45 | <https://github.com/stef/smeter> |
| everblu-meters *(archived)* | Reads Itron EverBlu Cyble water/gas meters via the RADIAN protocol with a CC1101 | 41 | <https://github.com/neutrinus/everblu-meters> |
| acurite-esphome | ESPHome decoder for AcuRite 433 MHz weather sensor OOK signals | 34 | <https://github.com/swoboda1337/acurite-esphome> |
| rtldavis *(archived)* | RTL-SDR receiver for the Davis Instruments weather station radio protocol | 29 | <https://github.com/bemasher/rtldavis> |
| A-OK | Protocol for A-OK 433.92 MHz window shade and projector screen remotes | 28 | <https://github.com/akirjavainen/A-OK> |
| markisol | Arduino control for Markisol 433.92 MHz window shades and BF-series remotes protocol | 24 | <https://github.com/akirjavainen/markisol> |
| Acurite_00592TX_sniffer | Arduino sniffer and decoder for the AcuRite 00592TX wireless temperature probe | 23 | <https://github.com/bhunting/Acurite_00592TX_sniffer> |
| acurite5n1arduino | Arduino receiver and decoder for AcuRite 5-in-1 weather station radio messages | 21 | <https://github.com/zerog2k/acurite5n1arduino> |
| weewx-rtldavis | WeeWX driver capturing Davis weather station radio data with rtldavis | 21 | <https://github.com/lheijst/weewx-rtldavis> |
| VPTools | Transceiver library for Davis Vantage weather station radio packets | 20 | <https://github.com/kobuki/VPTools> |
| weather-sdr-decode | RTL-SDR decoders for ELV and Mebus wireless weather sensors | 18 | <https://github.com/skaringa/weather-sdr-decode> |
| HoneywellSecurity | Decode Honeywell/Ademco 345 MHz wireless security sensors with an SDR | 17 | <https://github.com/jhaines0/HoneywellSecurity> |
| Acurite-00592TX-Decoder-ESP32a | ESP32/ESP8266 decoder for AcuRite 00592TX, 06044TX and 06002M sensors with MQTT | 16 | <https://github.com/trlafleur/Acurite-00592TX-Decoder-ESP32a> |
| acurite_decoder | RFM12B/RFM69 demodulator and parser for AcuRite temperature sensor data | 12 | <https://github.com/JorjBauer/acurite_decoder> |
| yngvi | Reads, decodes and displays AcuRite weather station radio data | 10 | <https://github.com/deebloo/yngvi> |
| Homegear-HomeMaticBidCoS | Homegear module implementing the HomeMatic BidCoS radio protocol | 9 | <https://github.com/Homegear/Homegear-HomeMaticBidCoS> |
| Itron-EverBlu-Cyble | Terminal reader for Itron EverBlu Cyble water meters over the RADIAN 433 MHz protocol | 9 | <https://github.com/reidys/Itron-EverBlu-Cyble> |
| weewx-meteostick | WeeWX driver for the Meteostick receiver of Davis wireless weather stations | 9 | <https://github.com/matthewwall/weewx-meteostick> |
| AcuRiteSniffer | Reads weather data packets sent by AcuRite Access devices for local use | 7 | <https://github.com/bp2008/AcuRiteSniffer> |
| lacrosse-mqtt-gateway | MQTT gateway for LaCrosse IT+ wireless sensors | 7 | <https://github.com/deveth0/lacrosse-mqtt-gateway> |
| iflag | Python library for the Itron/Actaris IFLAG and Corus gas volume converter protocol | 4 | <https://github.com/pwitab/iflag> |
| cotech | Arduino control for Clas Ohlson Cotech 433 MHz power plugs protocol | 1 | <https://github.com/akirjavainen/cotech> |

## VPN Clients

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| wgcf | Unofficial CLI that registers Cloudflare WARP accounts and generates WireGuard configs | 8,792 | <https://github.com/ViRb3/wgcf> |
| oblivion-desktop | Unofficial Cloudflare WARP client for Windows, macOS and Linux | 8,400 | <https://github.com/bepass-org/oblivion-desktop> |
| docker-easyconnect | Runs Sangfor EasyConnect/aTrust VPN clients in a container exposing SOCKS5/HTTP proxy gateways | 5,545 | <https://github.com/docker-easyconnect/docker-easyconnect> |
| oblivion | Unofficial Cloudflare WARP client for Android | 4,881 | <https://github.com/bepass-org/oblivion> |
| usque | Open-source reimplementation of the Cloudflare WARP client's MASQUE protocol | 1,467 | <https://github.com/Diniboy1123/usque> |
| zju-connect | Go reimplementation of the Sangfor EasyConnect VPN protocol (ZJU RVPN client) | 785 | <https://github.com/Mythologyli/zju-connect> |
| openconnect | OpenConnect client extended to support Palo Alto Networks' GlobalProtect VPN | 690 | <https://github.com/dlenski/openconnect> |
| NJUConnect *(archived)* | Go reimplementation of the Sangfor EasyConnect VPN protocol for NJU | 624 | <https://github.com/lyc8503/NJUConnect> |
| snx-rs | Open Source Client For Check Point VPN Tunnels | 519 | <https://github.com/ancwrd1/snx-rs> |
| gp-saml-gui | Interactively authenticate to GlobalProtect VPNs that require SAML | 385 | <https://github.com/dlenski/gp-saml-gui> |
| openconnect-sso | Wrapper script for OpenConnect supporting Azure AD (SAMLv2) authentication to Cisco SSL-VPNs | 377 | <https://github.com/vlaci/openconnect-sso> |
| radmin-vpn-linux | Runs Radmin VPN on Linux with a custom driver and TAP bridge | 244 | <https://github.com/baptisterajaut/radmin-vpn-linux> |
| openfortivpn-webview | Opens a browser webview to complete Fortinet SAML login and hand the session cookie to openfortivpn | 137 | <https://github.com/gm-vm/openfortivpn-webview> |
| snell-server-reversed | Reverse engineered Surge Snell proxy server | 137 | <https://github.com/icpz/snell-server-reversed> |
| juniper-vpn-py | Python Juniper VPN Authenticator | 112 | <https://github.com/russdill/juniper-vpn-py> |
| pan-globalprotect-okta | PaloAlto Networks GlobalProtect VPN (integrated with OKTA) command-line client | 102 | <https://github.com/arthepsy/pan-globalprotect-okta> |
| opensnell | Go implementation of the Snell v4/v5 proxy protocol | 91 | <https://github.com/missuo/opensnell> |
| openconnect-gp-okta *(archived)* | OpenConnect wrapper which logs into a GlobalProtect gateway, authenticating with Okta | 38 | <https://github.com/zdave/openconnect-gp-okta> |
| f5vpn-login | F5 VPN Command-line client | 21 | <https://github.com/hackedd/f5vpn-login> |
| gp-okta-linux | Connect Linux to a GlobalProtect VPN using Okta Push 2FA. | 15 | <https://github.com/jeffchannell/gp-okta-linux> |
| ocserv | OpenConnect VPN server compatible with Cisco AnyConnect clients |  | <https://gitlab.com/openconnect/ocserv> |
| openconnect | Open client for Cisco AnyConnect, GlobalProtect, Pulse/Ivanti, Fortinet, F5 and Array SSL VPN protocols |  | <https://gitlab.com/openconnect/openconnect> |
