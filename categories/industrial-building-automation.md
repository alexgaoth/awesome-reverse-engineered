# 🏭 Industrial & Building Automation

[← All categories](../README.md#-whats-inside) · [Search this category on the website](https://alexgaoth.github.io/awesome-reverse-engineered/#c=industrial-building-automation) · 196 projects

Health: 🟢 pushed in the last year · 🟡 1 to 3 years · 🔴 over 3 years · 🗄️ archived · ⚪ unknown

- [Building Automation](#building-automation) (1)
- [CNC & Machine Tools](#cnc--machine-tools) (10)
- [Energy Meters](#energy-meters) (15)
- [Gates, Blinds & Garage](#gates-blinds--garage) (15)
- [Heating & Heat Pump Buses](#heating--heat-pump-buses) (88)
- [Industrial Robots](#industrial-robots) (1)
- [PLC Protocols](#plc-protocols) (44)
- [Ventilation, Pool & Water](#ventilation-pool--water) (22)

## Building Automation

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [freeathome](https://github.com/jheling/freeathome) | Home Assistant component for Busch-Jaeger free@home via the SysAP | 167 | 🟢 | Python |

## CNC & Machine Tools

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [inkscape-silhouette](https://github.com/fablabnbg/inkscape-silhouette) | Inkscape extension driving Silhouette vinyl cutters via their reverse-engineered USB protocol | 681 | 🟢 | Python |
| [meerk40t](https://github.com/meerk40t/meerk40t) | Laser software for K40 (reverse-engineered M2 Nano/Lihuiyu), GRBL and fibre lasers | 436 | 🟢 | Python |
| [pyLSV2](https://github.com/drunsinn/pyLSV2) | Pure-Python implementation of Heidenhain's LSV2 CNC control protocol | 92 | 🟢 | Python |
| [cnc3018-offline-controller](https://github.com/positron96/cnc3018-offline-controller) | Open-source firmware for the CNC3018 offline controller | 89 | 🟢 | C++ |
| [ruida-laser](https://github.com/jnweiger/ruida-laser) | Reverse-engineered protocol and file format of Ruida laser controllers (RDWorks, USB, Ethernet) | 64 | 🟢 | R |
| [ruida](https://github.com/kkaempf/ruida) | Decoder and tooling for the scrambled RDWorks .rd laser file format | 44 | 🟡 | Ruby |
| [inkscape-thunderlaser](https://github.com/jnweiger/inkscape-thunderlaser) | Inkscape extension to drive Ruida-based laser cutters directly | 20 | 🟡 | Python |
| [RuiDa-Machine-Code](https://github.com/smiilaserpants/RuiDa-Machine-Code) | Notes on hacking the machine code of RuiDa laser controllers | 8 | 🔴 | JavaScript |
| [rdint](https://github.com/kallaballa/rdint) | Interpreter and renderer for Ruida .rd laser job files | 4 | 🔴 | C++ |
| [RDCAM](https://github.com/0x2b3bfa0/RDCAM) | Reverse engineering of the LaserWorks/RDCAM software from Shenzhen Reader Technology | 3 | 🗄️ | Visual Basic |

## Energy Meters

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [amsreader-firmware](https://github.com/UtilitechAS/amsreader-firmware) | ESP firmware reading HAN port data from smart electricity meters to MQTT | 465 | 🟢 | C++ |
| [Home-Assistant-custom-components-Tauron-AMIplus](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Tauron-AMIplus) | Home Assistant sensor for Tauron eLicznik energy data via unofficial API | 220 | 🟢 | Python |
| [Peacefair-PZEM-004T-](https://github.com/TheHWcave/Peacefair-PZEM-004T-) | Reverse engineered schematics and interface software for the PZEM-004T power meter | 108 | 🟡 | Python |
| [ha-kamstrup_403](https://github.com/golles/ha-kamstrup_403) | Home Assistant integration for Kamstrup 403 heat meters via the optical KMP protocol | 91 | 🟢 | Python |
| [vienna-smartmeter](https://github.com/platysma/vienna-smartmeter) | Python library for the Wiener Netze smart meter private API | 82 | 🟡 | Python |
| [emerald_electricity_advisor](https://github.com/WeekendWarrior1/emerald_electricity_advisor) | Reverse engineered tools and docs for the Emerald Electricity Advisor | 61 | 🔴 | C++ |
| [PyKamstrup](https://github.com/bsdphk/PyKamstrup) | Implementation of the Kamstrup Meter Protocol (KMP) | 61 | 🗄️ | Python |
| [kamstrup-402-mqtt](https://github.com/matthijsvisser/kamstrup-402-mqtt) | Python library reading Kamstrup Multical 402 heat meters over the optical eye | 54 | 🟢 | Python |
| [esphome_multical402](https://github.com/cenobitedk/esphome_multical402) | ESPHome component for Kamstrup Multical 402 heat meters | 43 | 🟡 | C++ |
| [Kamstrup-Radius-Interface](https://github.com/Asbjoern/Kamstrup-Radius-Interface) | ESP8266 interface for encrypted Kamstrup Omnipower meters (Radius) HAN port | 42 | 🟢 | C |
| [MeterLogger](https://github.com/nabovarme/MeterLogger) | Wireless MeterLogger for Kamstrup heat energy meters | 24 | 🟢 | C |
| [kamstrup](https://github.com/Hal9k-dk/kamstrup) | Kamstrup IR optical eye reader | 19 | 🔴 | C++ |
| [Home-Assistant-Sensor-MC66C](https://github.com/golles/Home-Assistant-Sensor-MC66C) | Home Assistant integration for Kamstrup Multical 66C heat meters | 17 | 🟢 | Python |
| [KMP382-driver](https://github.com/casperbang/KMP382-driver) | Driver for the Kamstrup 685-382 electricity meter over the KMP serial protocol | 11 | 🔴 | C# |
| [gometer](https://github.com/abrander/gometer) | Go client for Kamstrup and other power meters | 5 | 🔴 | Go |

## Gates, Blinds & Garage

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [secplus](https://github.com/argilo/secplus) | Software implementation of the Chamberlain Security+ rolling-code garage door system | 316 | 🟡 | Python |
| [iown-homecontrol](https://github.com/Velocet/iown-homecontrol) | Documentation and implementation of the io-homecontrol radio protocol (Velux, Somfy) | 287 | 🟡 | C++ |
| [Somfy_Remote_Lib](https://github.com/Legion2/Somfy_Remote_Lib) | Emulates a Somfy RTS remote with a 433.42 MHz transmitter | 158 | 🟢 | C++ |
| [HCPBridge](https://github.com/hkiam/HCPBridge) | Emulates the Hörmann HAP 1 HCP2 bus module on ESP8266/ESP32 for garage doors | 102 | 🔴 | C++ |
| [velux-cli](https://github.com/nougad/velux-cli) | Go client for the Velux Active KIX 300 cloud API | 37 | 🔴 | Go |
| [SommerESP](https://github.com/exico91/SommerESP) | Plug-and-play ESP32-C3 board to control Sommer garage doors | 28 | 🟢 | HTML |
| [iohc-flipper](https://github.com/samr037/iohc-flipper) | Flipper Zero app to sniff, pair and control io-homecontrol (Velux/Somfy) devices | 14 | 🟢 | C |
| [BiSecur](https://github.com/halacs/BiSecur) | Hörmann BiSecur Gateway CLI, Go SDK and Home Assistant integration | 12 | 🟢 | Go |
| [pysecur3](https://github.com/skelsec/pysecur3) | Python communication library for Hörmann BiSecur devices | 12 | 🔴 | Python |
| [VeluxIR](https://github.com/zschub/VeluxIR) | Decoded IR protocol for old Velux remotes | 10 | 🔴 | Arduino |
| [ha-maveo](https://github.com/yoda-jm/ha-maveo) | Python library and CLI for the Marantec Maveo smart garage door system | 9 | 🟢 | Python |
| [garagedoorcontroller](https://github.com/smhex/garagedoorcontroller) | Arduino controller for Marantec Comfort garage door openers using the Systembus | 6 | 🟢 | C++ |
| [garagedoor-dongle](https://github.com/bistromath/garagedoor-dongle) | SDR dongle and decoder for Chamberlain/LiftMaster garage door radio protocols | 5 | 🔴 | C |
| [bisecure-gateway](https://github.com/thomasletsch/bisecure-gateway) | Reverse engineering of the app to Hörmann BiSecur Gateway protocol | 3 | 🗄️ | Kotlin |
| [openers](https://github.com/zellyn/openers) | Go decoders for garage door opener radio protocols (Security+ and others) | 0 | 🔴 | Go |

## Heating & Heat Pump Buses

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [EMS-ESP32](https://github.com/emsesp/EMS-ESP32) | ESP32 firmware to read and control Bosch/Buderus/Nefit EMS and Heatronic boilers | 1,034 | 🟢 | C++ |
| [mitsubishi2MQTT](https://github.com/gysmo38/mitsubishi2MQTT) | ESP8266 bridge from Mitsubishi heat pumps (CN105 port) to MQTT | 503 | 🟢 | C |
| [esphome_aux_ac_component](https://github.com/GrKoR/esphome_aux_ac_component) | ESPHome component for AUX-based air conditioners via the reverse-engineered UART protocol | 376 | 🟢 | C++ |
| [BSB-LAN](https://github.com/fredlcore/BSB-LAN) | Monitor and control Siemens-based Brötje/Elco/Atlantic heating over the BSB/LPB bus | 350 | 🟢 | C |
| [esphome_samsung_hvac_bus](https://github.com/omerfaruk-aran/esphome_samsung_hvac_bus) | ESPHome component for Samsung HVAC units over the NASA/non-NASA RS-485 bus | 317 | 🟢 | C++ |
| [EMS-ESP](https://github.com/emsesp/EMS-ESP) | ESP8266 firmware for Bosch/Buderus EMS and Heatronic heating equipment | 310 | 🗄️ | C++ |
| [ebusd-configuration](https://github.com/john30/ebusd-configuration) | Reverse-engineered eBUS message definitions for Vaillant, Wolf and other heating devices | 286 | 🟢 | TypeSpec |
| [esphome-lg-controller](https://github.com/JanM321/esphome-lg-controller) | ESP32 wired controller for LG HVAC units emulating the wall controller protocol | 285 | 🟢 | C++ |
| [panasonic_cc](https://github.com/sockless-coding/panasonic_cc) | Home Assistant component for Panasonic Comfort Cloud air conditioners | 274 | 🟢 | Python |
| [OTGW-firmware](https://github.com/rvdbreemen/OTGW-firmware) | ESP8266 firmware for the Nodoshop OpenTherm Gateway with MQTT and REST | 207 | 🟢 | C++ |
| [haier-esphome](https://github.com/paveldn/haier-esphome) | ESPHome integration for Haier air conditioners (smartAir2 and hOn protocols) | 177 | 🟢 | C++ |
| [lennoxs30](https://github.com/PeteRager/lennoxs30) | Home Assistant integration for Lennox S30/S40/E30/M30 thermostats via local or cloud API | 144 | 🟢 | Python |
| [esp-arduino-ebus](https://github.com/danielkucera/esp-arduino-ebus) | ESP-based Wi-Fi firmware for eBUS adapter hardware | 134 | 🟢 | C++ |
| [inetbox.py](https://github.com/danielfett/inetbox.py) | Software implementation of a Truma iNet box for Truma CP Plus caravan heaters over LIN | 120 | 🟢 | Python |
| [infinitive](https://github.com/acd/infinitive) | Impersonates a SAM on the Carrier Infinity ABCD RS-485 bus for local control | 116 | 🟡 | Go |
| [ESP_Buderus_KM271](https://github.com/dewenni/ESP_Buderus_KM271) | Controls Buderus Logamatic heating via the KM271 interface with MQTT | 114 | 🟡 | C++ |
| [esphome_toshiba_suzumi](https://github.com/pedobry/esphome_toshiba_suzumi) | ESPHome component for Toshiba air conditioners via their serial protocol | 114 | 🟢 | C++ |
| [remeha_home](https://github.com/msvisser/remeha_home) | Home Assistant integration for the private Remeha Home cloud API | 114 | 🟡 | Python |
| [FujiHeatPump](https://github.com/unreality/FujiHeatPump) | Control Fujitsu air conditioners from Arduino via the reverse-engineered indoor-unit bus | 107 | 🔴 | C++ |
| [luxtronik](https://github.com/Bouni/luxtronik) | Home Assistant integration for Luxtronik heat pump controllers | 100 | 🔴 | Python |
| [esphome-truma_inetbox](https://github.com/Fabian-Schmidt/esphome-truma_inetbox) | ESPHome component to control Truma CP Plus heaters over LIN | 99 | 🟡 | C++ |
| [Nefit-Buderus-EMS-bus-Arduino-Domoticz](https://github.com/bbqkees/Nefit-Buderus-EMS-bus-Arduino-Domoticz) | Reads Nefit/Buderus EMS bus datagrams into Domoticz | 90 | 🔴 | C++ |
| [esphome-fujitsu](https://github.com/FujiHeatPump/esphome-fujitsu) | ESPHome component for Fujitsu air conditioners via the reverse-engineered indoor-unit bus | 89 | 🟢 | C++ |
| [ecodan-ha-local](https://github.com/rbroker/ecodan-ha-local) | Local Home Assistant control of Mitsubishi Ecodan heat pumps via CN105 | 85 | 🟡 | C++ |
| [python-panasonic-comfort-cloud](https://github.com/lostfields/python-panasonic-comfort-cloud) | Python module for the private Panasonic Comfort Cloud climate API | 85 | 🟡 | Python |
| [ramses_rf](https://github.com/ramses-rf/ramses_rf) | Interface for the Honeywell RAMSES-II RF protocol used by evohome and similar systems | 83 | 🟢 | Python |
| [WPalaControl](https://github.com/Domochip/WPalaControl) | D1 Mini replacement for the Palazzetti/Jotul/Godin stove ConnectionBox (Fumis serial protocol) | 76 | 🟢 | C++ |
| [Mitsubishi-CN105-Protocol-Decode](https://github.com/m000c400/Mitsubishi-CN105-Protocol-Decode) | Documentation of the Mitsubishi CN105 protocol of Ecodan air-to-water heat pumps | 74 | 🟡 | C++ |
| [OneESP32ToRuleThemAll](https://github.com/kr0ner/OneESP32ToRuleThemAll) | Open-source ISG replacement for Stiebel Eltron/Tecalor heat pumps over CAN bus | 74 | 🟢 | C++ |
| [taixia](https://github.com/tsunglung/taixia) | Home Assistant integration for appliances using the Taiwanese TaiXia SA protocol | 74 | 🟢 | C++ |
| [AquaMQTT](https://github.com/tspopp/AquaMQTT) | Monitor and control Groupe Atlantic water heat pumps (Explorer, Calypso) via MQTT | 70 | 🟢 | C++ |
| [oekofen-pellematic-compact](https://github.com/dominikamann/oekofen-pellematic-compact) | Home Assistant integration for ÖkoFEN Pellematic via its JSON/TCP interface | 70 | 🟢 | Python |
| [hass-WEM-Portal](https://github.com/erikkastelec/hass-WEM-Portal) | Home Assistant component scraping the Weishaupt WEM Portal | 68 | 🟢 | Python |
| [evofw3](https://github.com/ghoti57/evofw3) | Firmware for listening to and sending Honeywell evohome RAMSES-II radio messages | 64 | 🟢 | C |
| [esphome-hlink-ac](https://github.com/lumixen/esphome-hlink-ac) | ESPHome component for Hitachi air conditioners via the H-Link protocol | 61 | 🟢 | C++ |
| [python-luxtronik](https://github.com/Bouni/python-luxtronik) | Python library for the Luxtronik heat pump controller (Alpha Innotec, Novelan) protocol | 49 | 🟢 | Python |
| [ESPHome-Froeling-Lambdatronic_3200](https://github.com/GyroGearl00se/ESPHome-Froeling-Lambdatronic_3200) | ESPHome RS232 reader for Fröling Lambdatronic 3200 boilers | 46 | 🟢 | CSS |
| [maestrogateway](https://github.com/Chibald/maestrogateway) | Gateway for MCZ pellet stoves with Maestro technology via their websocket protocol | 46 | 🔴 | Python |
| [Diematic_to_MQTT](https://github.com/Benoit3/Diematic_to_MQTT) | MQTT interface for De Dietrich Diematic3 heating regulators | 44 | 🟢 | Python |
| [esphome_gree_ac](https://github.com/piotrva/esphome_gree_ac) | ESPHome component for Gree air conditioners over the UART wifi-module port | 43 | 🟢 | C++ |
| [CAN-Gateway](https://github.com/wladwnt/CAN-Gateway) | Wi-Fi/LAN to CAN gateway for Hoval TopTronic E devices | 42 | 🟡 |  |
| [python-thermia-online-api](https://github.com/klejejs/python-thermia-online-api) | Python API for Thermia heat pumps via the Thermia Online cloud | 42 | 🟢 | Python |
| [InsideViessmannVitosoft](https://github.com/sarnau/InsideViessmannVitosoft) | Description of Viessmann Optolink protocol and Vitosoft XML data files | 39 | 🟡 | Python |
| [nano_pk](https://github.com/TheRealKillaruna/nano_pk) | Home Assistant integration reading the Hargassner Nano-PK boiler data stream | 36 | 🟢 | Python |
| [hass-hitachi_yutaki](https://github.com/alepee/hass-hitachi_yutaki) | Home Assistant integration for Hitachi Yutaki heat pumps via the ATW-MBS gateway | 35 | 🟢 | Python |
| [ebusd-configuration-weishaupt](https://github.com/J0EK3R/ebusd-configuration-weishaupt) | ebusd configuration files for Weishaupt WTC devices | 27 | 🔴 | C++ |
| [HaierProtocol](https://github.com/paveldn/HaierProtocol) | Library implementing the Haier air-conditioner serial communication protocol | 27 | 🟢 | C++ |
| [uhomeuponor](https://github.com/dave-code-ruiz/uhomeuponor) | Home Assistant component for Uponor Smatrix underfloor heating via the Uhome API | 26 | 🟢 | Python |
| [ESPHome-Brivis-Networker](https://github.com/Makin-Things/ESPHome-Brivis-Networker) | Replacement PCB and ESPHome firmware for Brivis ducted heater networker | 23 | 🟡 | C++ |
| [oekofen-json-documentation](https://github.com/thannaske/oekofen-json-documentation) | Community documentation of the undocumented ÖkoFEN pellet heating JSON interface | 21 | 🔴 |  |
| [ha-windhager](https://github.com/vermi0ffh/ha-windhager) | Home Assistant integration for Windhager heating systems | 20 | 🟡 | Python |
| [buderus2mqtt](https://github.com/krambox/buderus2mqtt) | Gateway between the Buderus KM200 internet gateway and MQTT | 18 | 🔴 | JavaScript |
| [HLinkSniffer](https://github.com/hankerspace/HLinkSniffer) | H-LINK bus sniffer for Hitachi Yutaki heat pumps on a Raspberry Pi | 18 | 🔴 | Python |
| [ha-harvia-sauna](https://github.com/WiesiDeluxe/ha-harvia-sauna) | Home Assistant integration for Harvia sauna heaters (Xenio Wi-Fi, Fenix) | 16 | 🟢 | Python |
| [rinnaicontrolr](https://github.com/explosivo22/rinnaicontrolr) | Python interface for the private Rinnai Control-R API | 16 | 🔴 | Python |
| [Hargassner_NodeJS_Adapter](https://github.com/schuppenkarp/Hargassner_NodeJS_Adapter) | Node.js adapter for Hargassner boilers with Touch Control | 15 | 🟡 | JavaScript |
| [hoval-gateway](https://github.com/chrishrb/hoval-gateway) | Gateway for reading Hoval heating over its proprietary CAN bus | 15 | 🟡 | Python |
| [Weishaupt_CanApiJson](https://github.com/BorgNumberOne/Weishaupt_CanApiJson) | Documentation of Weishaupt WTC CanApiJson, a CAN-like protocol over JSON | 15 | 🟢 |  |
| [rinnai-control-panel-sigrok-pd](https://github.com/ayavilevich/rinnai-control-panel-sigrok-pd) | Sigrok decoder for the internal protocol of Rinnai gas heater control panels | 13 | 🔴 | Python |
| [MicronovaPelletStoveController](https://github.com/k3a/MicronovaPelletStoveController) | Code to control Micronova pellet stove controllers over their serial protocol | 12 | 🔴 | C++ |
| [Palazzetti](https://github.com/Domochip/Palazzetti) | Library to control Palazzetti (Fumis) pellet stoves over serial | 12 | 🟢 | C++ |
| [viessmann-optolink2mqtt](https://github.com/f18m/viessmann-optolink2mqtt) | Bridge between Viessmann Optolink devices and MQTT | 12 | 🟢 | Python |
| [optolink-bridge](https://github.com/kristian/optolink-bridge) | Bridges the Viessmann Optolink bus and publishes values to MQTT and Home Assistant | 11 | 🟢 | JavaScript |
| [rinnai-serial-decoder](https://github.com/genmeim/rinnai-serial-decoder) | PulseView decoder for Rinnai hot-water unit serial communication | 10 | 🔴 | Python |
| [vitalk](https://github.com/klauweg/vitalk) | Communication with Viessmann Vitodens 300 via the Optolink interface | 9 | 🔴 | C |
| [wolf_ism8](https://github.com/marcschmiedchen/wolf_ism8) | Read data from WOLF heating systems via the ISM8 module protocol | 9 | 🟢 | Python |
| [esphome_vitohome](https://github.com/SoulSolistice/esphome_vitohome) | ESPHome component for Viessmann heating controllers over Optolink | 8 | 🟢 | C++ |
| [ioBroker.e3oncan](https://github.com/MyHomeMyData/ioBroker.e3oncan) | ioBroker adapter for Viessmann E3-series heating over CAN bus | 8 | 🟢 | JavaScript |
| [vogod](https://github.com/speters/vogod) | Daemon exposing a Viessmann heating device's Optolink data as a REST API | 8 | 🟢 | Go |
| [Hoval-GW](https://github.com/zittix/Hoval-GW) | Python gateway for the Hoval CAN bus | 7 | 🟢 | Python |
| [wem-python](https://github.com/geronet1/wem-python) | Python interpreter for the Weishaupt WEM CAN bus | 7 | 🟡 | Python |
| [ebus](https://github.com/csowada/ebus) | Java eBUS library with device configs, used by the openHAB eBUS binding | 6 | 🟢 | Java |
| [mertik-fireplace-wifi-ha](https://github.com/jkfran/mertik-fireplace-wifi-ha) | Home Assistant plugin for fireplaces using the Mertik Maxitrol Wi-Fi module | 6 | 🟢 | Python |
| [node-weishaupt-api](https://github.com/foxriver76/node-weishaupt-api) | Node module for Weishaupt heaters over the WCM-COM 1.0 module | 6 | 🔴 | TypeScript |
| [py-palazzetti-api](https://github.com/dotvav/py-palazzetti-api) | Python library controlling a Palazzetti stove through its Connection Box | 6 | 🟢 | Python |
| [froeling-connect](https://github.com/Layf21/froeling-connect) | Python wrapper for the private Fröling Connect cloud API | 5 | 🟢 | Python |
| [keba_keenergy_api](https://github.com/superbox-dev/keba_keenergy_api) | Python wrapper for the KEBA KeEnergy Web HMI API used by heat pumps | 5 | 🟢 | Python |
| [ebus](https://github.com/yuhu-/ebus) | C++ library for eBUS heating bus communication | 4 | 🟢 | C++ |
| [Py-Weishaupt-WCM-COM](https://github.com/schmiegelt/Py-Weishaupt-WCM-COM) | Python package for the Weishaupt WCM-COM home module | 4 | 🔴 | Python |
| [pyatag](https://github.com/MatsNl/pyatag) | Python API to connect to the Atag One thermostat | 4 | 🟡 | Python |
| [windhager-rest-api-documentation](https://github.com/domfie/windhager-rest-api-documentation) | Documentation of the Windhager MES Infinity RC7030 web server REST API | 3 | 🔴 |  |
| [tasmota-biowin](https://github.com/aJunk/tasmota-biowin) | Tasmota app reading Windhager BioWIN data from the MES D application bus | 2 | 🟡 | Berry |
| [Wolf_ebusd_config](https://github.com/Ces1254/Wolf_ebusd_config) | ebusd configuration files for Wolf BM-2/FHA/MM-1 heating devices | 2 | 🟢 |  |
| [Froeling-HA](https://github.com/Tropaion/Froeling-HA) | Home Assistant integration for Fröling boilers using their proprietary protocol | 1 | 🟢 | Python |
| [froeling-proxy](https://github.com/mpolajnar/froeling-proxy) | Library and TCP server for communicating with Fröling wood boilers | 1 | 🟢 | Python |
| [weishaupt_modbus_rtu](https://github.com/backuprestore/weishaupt_modbus_rtu) | Reverse engineering of the Weishaupt heat pump Modbus RTU RS485 interface | 1 | 🟡 |  |
| [ParadigmaHeatingReader](https://github.com/kayr7/ParadigmaHeatingReader) | Reverse-engineered reader for Paradigma SystaComfort 2 heating controllers | 0 | 🔴 | Python |
| [Retro-Fujitsu-ESPHome](https://github.com/endofthewurst/Retro-Fujitsu-ESPHome) | ESPHome integration for a Fujitsu heat pump over its LIN bus | 0 | 🟢 | C++ |

## Industrial Robots

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [KUKAVARPROXY](https://github.com/ImtsSrl/KUKAVARPROXY) | TCP server on KUKA robots exposing variables via the OpenShowVar protocol | 136 | 🔴 | VBA |

## PLC Protocols

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [HslCommunication](https://github.com/dathlin/HslCommunication) | C# industrial comms library covering Siemens, Mitsubishi, Omron, AB, Keyence and other PLC protocols | 2,133 | 🟢 | C# |
| [plc4x](https://github.com/apache/plc4x) | Apache PLC4X: drivers for S7, Allen-Bradley, Beckhoff, Modbus and other PLC protocols in Java/Go/C | 1,755 | 🟢 | Java |
| [IoTClient](https://github.com/zhaopeiym/IoTClient) | .NET client for industrial protocols: Siemens S7, Mitsubishi MC, Omron FINS, Allen-Bradley | 1,689 | 🟢 | C# |
| [s7netplus](https://github.com/S7NetPlus/s7netplus) | S7.NET+: .NET library that talks the Siemens S7comm protocol to Step7 PLCs | 1,634 | 🟡 | C# |
| [libplctag](https://github.com/libplctag/libplctag) | Portable C library for Allen-Bradley (CIP/PCCC) and Modbus PLC tag access | 905 | 🟢 | C |
| [python-snap7](https://github.com/gijzelaerr/python-snap7) | Pure-Python client for Siemens S7comm, the undocumented protocol of S7-300/400/1200/1500 PLCs | 855 | 🟢 | Python |
| [pylogix](https://github.com/dmroeder/pylogix) | Python library to read/write tags on Allen-Bradley ControlLogix/CompactLogix PLCs | 733 | 🟢 | Python |
| [pycomm3](https://github.com/ottowayi/pycomm3) | Python EtherNet/IP library for Allen-Bradley Logix and SLC/MicroLogix PLCs, incl. undocumented services | 519 | 🟢 | Python |
| [DotNetSiemensPLCToolBoxLibrary](https://github.com/dotnetprojects/DotNetSiemensPLCToolBoxLibrary) | .NET library to access Siemens PLCs and parse Step5/Step7 project files | 481 | 🟢 | C# |
| [gos7](https://github.com/robinson/gos7) | Go implementation of the Siemens S7comm protocol | 405 | 🟢 | Go |
| [nodeS7](https://github.com/plcpeople/nodeS7) | Node.js library for Siemens S7 PLC communication over the S7comm protocol | 399 | 🔴 | JavaScript |
| [s7connector](https://github.com/s7connector/s7connector) | Java S7 PLC connector implementing the Siemens S7comm protocol | 339 | 🟡 | HTML |
| [iot-communication](https://github.com/xingshuangs/iot-communication) | Java library for Siemens S7, Mitsubishi MELSEC and Omron FINS PLC protocols | 302 | 🟢 | Java |
| [libplctag.NET](https://github.com/libplctag/libplctag.NET) | .NET wrapper for the libplctag Allen-Bradley PLC library | 299 | 🟢 | C# |
| [snap7](https://github.com/SCADACS/snap7) | Snap7 suite: open client, server and partner implementation of the Siemens S7comm protocol | 284 | 🔴 | Pascal |
| [Sharp7](https://github.com/fbarresi/Sharp7) | Sharp7: C# port of the Snap7 Siemens S7comm client packaged for NuGet | 258 | 🔴 | C# |
| [S7CommPlusDriver](https://github.com/thomas-v2/S7CommPlusDriver) | Reverse-engineered S7comm-plus driver for Siemens S7-1200/1500 PLCs | 228 | 🟢 | C# |
| [ICSREF](https://github.com/momalab/ICSREF) | Tool for reverse engineering industrial control system (CODESYS) binaries | 185 | 🟢 | Python |
| [node-snap7](https://github.com/mathiask88/node-snap7) | Node.js bindings for the Snap7 Siemens S7 communication library | 180 | 🟢 | C++ |
| [snap7](https://github.com/davenardella/snap7) | Official Snap7 repository: multi-platform Siemens S7 Ethernet communication suite | 175 | 🟡 | C++ |
| [pycomm](https://github.com/ruscito/pycomm) | Python modules to talk to Allen-Bradley PLCs (ControlLogix tags, SLC/PCCC) | 158 | 🔴 | Python |
| [SoftPlc](https://github.com/fbarresi/SoftPlc) | Software PLC that emulates a Siemens S7 server over S7comm, with Docker support | 154 | 🟡 | C# |
| [node-red-contrib-s7](https://github.com/st-one-io/node-red-contrib-s7) | Node-RED nodes to read and write Siemens S7 PLCs via a JS S7comm implementation | 135 | 🟢 | HTML |
| [libfins](https://github.com/lammertb/libfins) | Multi-platform C library for the Omron FINS PLC protocol | 133 | 🟡 | C |
| [mcprotocol](https://github.com/plcpeople/mcprotocol) | Node.js implementation of the Mitsubishi MC protocol for FX/Q/L PLCs | 121 | 🔴 | JavaScript |
| [acd](https://github.com/hutcheb/acd) | Tools to parse Rockwell Studio 5000 .ACD project files, a proprietary binary format | 112 | 🟢 | Python |
| [scada-stuff](https://github.com/nezza/scada-stuff) | Scripts and tools for reverse engineering SCADA/ICS devices | 110 | 🔴 | Python |
| [pymcprotocol](https://github.com/senrust/pymcprotocol) | Python implementation of the Mitsubishi MELSEC MC protocol | 105 | 🟡 | Python |
| [mokka7](https://github.com/comtel2000/mokka7) | Mokka7: pure-Java port of the Snap7 Siemens S7comm client | 69 | 🟢 | Java |
| [go-mcprotocol](https://github.com/future-architect/go-mcprotocol) | Go client for the Mitsubishi MELSEC MC protocol | 51 | 🔴 | Go |
| [node-omron-fins](https://github.com/ptrks/node-omron-fins) | Node.js implementation of the Omron FINS protocol | 47 | 🔴 | JavaScript |
| [ge-ethernet-SRTP](https://github.com/TheMadHatt3r/ge-ethernet-SRTP) | Working demo of the proprietary GE SRTP PLC Ethernet protocol, reverse engineered | 45 | 🟡 | Python |
| [s7commwireshark](https://github.com/moki-ics/s7commwireshark) | Wireshark dissector plugin for Siemens S7comm and S7comm-plus (export of the SourceForge project) | 33 | 🔴 | C |
| [pymelsec](https://github.com/NothinRandom/pymelsec) | Python 3 implementation of Mitsubishi MELSEC communication | 31 | 🔴 | Python |
| [jfins](https://github.com/siyka-au/jfins) | Non-blocking Omron FINS master and slave for Java | 28 | 🔴 | Java |
| [fxplc](https://github.com/KrystianD/fxplc) | Python connector for the low-level Mitsubishi FX series serial programming-port protocol | 26 | 🟡 | Python |
| [Rust7](https://github.com/davenardella/Rust7) | Native Rust Siemens S7 client in the style of Snap7, no FFI | 26 | 🟢 | Rust |
| [CoDeSys_S7Comm](https://github.com/NothinRandom/CoDeSys_S7Comm) | S7comm client implemented in CoDeSys to talk to Siemens PLCs from other PLCs | 24 | 🔴 |  |
| [omron-fins-go](https://github.com/hiroeorz/omron-fins-go) | Go client for Omron FINS commands | 18 | 🔴 | Go |
| [packet-ge-srtp](https://github.com/PalaIndustrial/packet-ge-srtp) | Wireshark dissector for the GE-Fanuc Service Request Transfer Protocol (SRTP) | 15 | 🟢 | Lua |
| [S7CommPlusV3Driver](https://github.com/lircy/S7CommPlusV3Driver) | .NET driver for Siemens S7-1200/1500 using S7comm-plus V3, with or without TLS | 14 | 🟢 | C# |
| [node-red-contrib-pccc](https://github.com/st-one-io/node-red-contrib-pccc) | Node-RED node for Allen-Bradley PLCs using the PCCC protocol | 11 | 🟡 | HTML |
| [rs-snap7](https://github.com/cool0looc/rs-snap7) | Pure-Rust async Siemens S7 library with S7comm and S7comm-plus support | 9 | 🟢 | Rust |
| [FinsToToolbusGateway](https://github.com/Vladimirek/FinsToToolbusGateway) | Gateway from Omron FINS to the undocumented Sysmac Toolbus programming protocol | 0 | 🔴 | C++ |

## Ventilation, Pool & Water

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [WiFi-remote-for-Bestway-Lay-Z-SPA](https://github.com/visualapproach/WiFi-remote-for-Bestway-Lay-Z-SPA) | ESP8266 Wi-Fi remote for Bestway Lay-Z-Spa hot tubs via the display bus | 416 | 🟢 | C++ |
| [ithowifi](https://github.com/arjenhiemstra/ithowifi) | ESP32 Wi-Fi add-on for Itho ventilation using its I2C protocol | 287 | 🟢 | HTML |
| [AqualinkD](https://github.com/aqualinkd/AqualinkD) | Daemon controlling Jandy Aqualink RS pool equipment over RS485 | 238 | 🟢 | C |
| [comfoair-esp32](https://github.com/vekexasia/comfoair-esp32) | ESP32 firmware to interact with Zehnder ComfoAir Q via CAN | 155 | 🟢 | C++ |
| [balboa_worldwide_app](https://github.com/ccutrer/balboa_worldwide_app) | Ruby library for Balboa spa Wi-Fi module and RS-485 protocol | 123 | 🟢 | Ruby |
| [aiocomfoconnect](https://github.com/michaelarnauts/aiocomfoconnect) | Async Python library for the Zehnder ComfoConnect LAN C protocol (ComfoAir Q) | 108 | 🟢 | Python |
| [esphome-zehnder-comfoair](https://github.com/yoziru/esphome-zehnder-comfoair) | ESPHome control of Zehnder ComfoAir Q over CAN bus | 96 | 🟢 | C++ |
| [comfoconnect](https://github.com/michaelarnauts/comfoconnect) | Python library for the Zehnder ComfoConnect LAN C protocol | 95 | 🗄️ | Python |
| [esphome-comfoair](https://github.com/wichers/esphome-comfoair) | ESPHome configuration for Zehnder ComfoAir units over the serial protocol | 84 | 🟢 | C++ |
| [intellicenter](https://github.com/jlvaillant/intellicenter) | Home Assistant integration for Pentair IntelliCenter pool systems | 52 | 🟡 | Python |
| [esp32-pentair-controller](https://github.com/michaelusner/esp32-pentair-controller) | Control Pentair pool equipment via RS485 from an ESP32 to MQTT | 38 | 🟡 | C |
| [zcan](https://github.com/marco-hoyer/zcan) | API proxy for Zehnder ComfoAir Q devices on the CAN bus | 36 | 🔴 | Python |
| [vallox_websocket_api](https://github.com/yozik04/vallox_websocket_api) | Async API for Vallox ventilation units via their websocket protocol | 32 | 🟢 | JavaScript |
| [ZehnderComfoair](https://github.com/eelcohn/ZehnderComfoair) | Reverse engineering the Zehnder ComfoFan ventilation RF protocol | 29 | 🟢 |  |
| [esphome-helios-kwl](https://github.com/lostcontrol/esphome-helios-kwl) | ESPHome integration for Helios KWL ventilation via RS485 | 23 | 🟢 | C++ |
| [hayward-pool-heater-mqtt](https://github.com/njanik/hayward-pool-heater-mqtt) | Control a Hayward pool heater over its bus via MQTT | 20 | 🟡 | C++ |
| [screenlogic_over_ip](https://github.com/ceisenach/screenlogic_over_ip) | IP communication with Pentair ScreenLogic2 pool controllers | 17 | 🔴 | JavaScript |
| [node-comfoair](https://github.com/coolchip/node-comfoair) | Node.js library for Zehnder ComfoAir 350 ventilation units | 16 | 🟡 | JavaScript |
| [pypentair](https://github.com/cilynx/pypentair) | Python package for Pentair pool pumps over RS-485 | 14 | 🔴 | Python |
| [ecowater-softener](https://github.com/barleybobs/ecowater-softener) | Python library pulling data from EcoWater water softeners | 10 | 🟡 | Python |
| [hayward-pool](https://github.com/ma-nathan/hayward-pool) | Scrape data from Hayward Pro Logic / Aqua Plus via the AquaConnect HomeNet | 7 | 🔴 | Go |
| [comfo](https://github.com/ti-mo/comfo) | Go implementation of the Zehnder ComfoAir serial protocol | 4 | 🟡 | Go |
