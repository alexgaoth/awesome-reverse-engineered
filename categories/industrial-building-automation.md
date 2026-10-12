# Industrial & Building Automation

[← All categories](../README.md) · 187 projects

- [Building Automation](#building-automation) (1)
- [CNC & Machine Tools](#cnc--machine-tools) (9)
- [Energy Meters](#energy-meters) (11)
- [Gates, Blinds & Garage](#gates-blinds--garage) (15)
- [Heating & Heat Pump Buses](#heating--heat-pump-buses) (86)
- [Industrial Robots](#industrial-robots) (1)
- [PLC Protocols](#plc-protocols) (42)
- [Ventilation, Pool & Water](#ventilation-pool--water) (22)

## Building Automation

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| freeathome | Home Assistant component for Busch-Jaeger free@home via the SysAP | 167 | <https://github.com/jheling/freeathome> |

## CNC & Machine Tools

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| inkscape-silhouette | Inkscape extension driving Silhouette vinyl cutters via their reverse-engineered USB protocol | 680 | <https://github.com/fablabnbg/inkscape-silhouette> |
| meerk40t | Laser software for K40 (reverse-engineered M2 Nano/Lihuiyu), GRBL and fibre lasers | 435 | <https://github.com/meerk40t/meerk40t> |
| pyLSV2 | Pure-Python implementation of Heidenhain's LSV2 CNC control protocol | 92 | <https://github.com/drunsinn/pyLSV2> |
| ruida-laser | Reverse-engineered protocol and file format of Ruida laser controllers (RDWorks, USB, Ethernet) | 64 | <https://github.com/jnweiger/ruida-laser> |
| ruida | Decoder and tooling for the scrambled RDWorks .rd laser file format | 44 | <https://github.com/kkaempf/ruida> |
| inkscape-thunderlaser | Inkscape extension to drive Ruida-based laser cutters directly | 20 | <https://github.com/jnweiger/inkscape-thunderlaser> |
| RuiDa-Machine-Code | Notes on hacking the machine code of RuiDa laser controllers | 8 | <https://github.com/smiilaserpants/RuiDa-Machine-Code> |
| rdint | Interpreter and renderer for Ruida .rd laser job files | 4 | <https://github.com/kallaballa/rdint> |
| RDCAM *(archived)* | Reverse engineering of the LaserWorks/RDCAM software from Shenzhen Reader Technology | 3 | <https://github.com/0x2b3bfa0/RDCAM> |

## Energy Meters

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| amsreader-firmware | ESP firmware reading HAN port data from smart electricity meters to MQTT | 465 | <https://github.com/UtilitechAS/amsreader-firmware> |
| ha-kamstrup_403 | Home Assistant integration for Kamstrup 403 heat meters via the optical KMP protocol | 91 | <https://github.com/golles/ha-kamstrup_403> |
| PyKamstrup *(archived)* | Implementation of the Kamstrup Meter Protocol (KMP) | 61 | <https://github.com/bsdphk/PyKamstrup> |
| kamstrup-402-mqtt | Python library reading Kamstrup Multical 402 heat meters over the optical eye | 54 | <https://github.com/matthijsvisser/kamstrup-402-mqtt> |
| esphome_multical402 | ESPHome component for Kamstrup Multical 402 heat meters | 43 | <https://github.com/cenobitedk/esphome_multical402> |
| Kamstrup-Radius-Interface | ESP8266 interface for encrypted Kamstrup Omnipower meters (Radius) HAN port | 42 | <https://github.com/Asbjoern/Kamstrup-Radius-Interface> |
| MeterLogger | Wireless MeterLogger for Kamstrup heat energy meters | 24 | <https://github.com/nabovarme/MeterLogger> |
| kamstrup | Kamstrup IR optical eye reader | 19 | <https://github.com/Hal9k-dk/kamstrup> |
| Home-Assistant-Sensor-MC66C | Home Assistant integration for Kamstrup Multical 66C heat meters | 17 | <https://github.com/golles/Home-Assistant-Sensor-MC66C> |
| KMP382-driver | Driver for the Kamstrup 685-382 electricity meter over the KMP serial protocol | 11 | <https://github.com/casperbang/KMP382-driver> |
| gometer | Go client for Kamstrup and other power meters | 5 | <https://github.com/abrander/gometer> |

## Gates, Blinds & Garage

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| secplus | Software implementation of the Chamberlain Security+ rolling-code garage door system | 315 | <https://github.com/argilo/secplus> |
| iown-homecontrol | Documentation and implementation of the io-homecontrol radio protocol (Velux, Somfy) | 286 | <https://github.com/Velocet/iown-homecontrol> |
| Somfy_Remote_Lib | Emulates a Somfy RTS remote with a 433.42 MHz transmitter | 158 | <https://github.com/Legion2/Somfy_Remote_Lib> |
| HCPBridge | Emulates the Hörmann HAP 1 HCP2 bus module on ESP8266/ESP32 for garage doors | 102 | <https://github.com/hkiam/HCPBridge> |
| velux-cli | Go client for the Velux Active KIX 300 cloud API | 37 | <https://github.com/nougad/velux-cli> |
| SommerESP | Plug-and-play ESP32-C3 board to control Sommer garage doors | 28 | <https://github.com/exico91/SommerESP> |
| iohc-flipper | Flipper Zero app to sniff, pair and control io-homecontrol (Velux/Somfy) devices | 13 | <https://github.com/samr037/iohc-flipper> |
| BiSecur | Hörmann BiSecur Gateway CLI, Go SDK and Home Assistant integration | 12 | <https://github.com/halacs/BiSecur> |
| pysecur3 | Python communication library for Hörmann BiSecur devices | 12 | <https://github.com/skelsec/pysecur3> |
| VeluxIR | Decoded IR protocol for old Velux remotes | 10 | <https://github.com/zschub/VeluxIR> |
| ha-maveo | Python library and CLI for the Marantec Maveo smart garage door system | 9 | <https://github.com/yoda-jm/ha-maveo> |
| garagedoorcontroller | Arduino controller for Marantec Comfort garage door openers using the Systembus | 6 | <https://github.com/smhex/garagedoorcontroller> |
| garagedoor-dongle | SDR dongle and decoder for Chamberlain/LiftMaster garage door radio protocols | 5 | <https://github.com/bistromath/garagedoor-dongle> |
| bisecure-gateway *(archived)* | Reverse engineering of the app to Hörmann BiSecur Gateway protocol | 3 | <https://github.com/thomasletsch/bisecure-gateway> |
| openers | Go decoders for garage door opener radio protocols (Security+ and others) | 0 | <https://github.com/zellyn/openers> |

## Heating & Heat Pump Buses

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| EMS-ESP32 | ESP32 firmware to read and control Bosch/Buderus/Nefit EMS and Heatronic boilers | 1,032 | <https://github.com/emsesp/EMS-ESP32> |
| mitsubishi2MQTT | ESP8266 bridge from Mitsubishi heat pumps (CN105 port) to MQTT | 503 | <https://github.com/gysmo38/mitsubishi2MQTT> |
| esphome_aux_ac_component | ESPHome component for AUX-based air conditioners via the reverse-engineered UART protocol | 375 | <https://github.com/GrKoR/esphome_aux_ac_component> |
| BSB-LAN | Monitor and control Siemens-based Brötje/Elco/Atlantic heating over the BSB/LPB bus | 349 | <https://github.com/fredlcore/BSB-LAN> |
| esphome_samsung_hvac_bus | ESPHome component for Samsung HVAC units over the NASA/non-NASA RS-485 bus | 317 | <https://github.com/omerfaruk-aran/esphome_samsung_hvac_bus> |
| EMS-ESP *(archived)* | ESP8266 firmware for Bosch/Buderus EMS and Heatronic heating equipment | 310 | <https://github.com/emsesp/EMS-ESP> |
| ebusd-configuration | Reverse-engineered eBUS message definitions for Vaillant, Wolf and other heating devices | 286 | <https://github.com/john30/ebusd-configuration> |
| esphome-lg-controller | ESP32 wired controller for LG HVAC units emulating the wall controller protocol | 285 | <https://github.com/JanM321/esphome-lg-controller> |
| panasonic_cc | Home Assistant component for Panasonic Comfort Cloud air conditioners | 274 | <https://github.com/sockless-coding/panasonic_cc> |
| OTGW-firmware | ESP8266 firmware for the Nodoshop OpenTherm Gateway with MQTT and REST | 207 | <https://github.com/rvdbreemen/OTGW-firmware> |
| haier-esphome | ESPHome integration for Haier air conditioners (smartAir2 and hOn protocols) | 177 | <https://github.com/paveldn/haier-esphome> |
| lennoxs30 | Home Assistant integration for Lennox S30/S40/E30/M30 thermostats via local or cloud API | 144 | <https://github.com/PeteRager/lennoxs30> |
| esp-arduino-ebus | ESP-based Wi-Fi firmware for eBUS adapter hardware | 133 | <https://github.com/danielkucera/esp-arduino-ebus> |
| inetbox.py | Software implementation of a Truma iNet box for Truma CP Plus caravan heaters over LIN | 120 | <https://github.com/danielfett/inetbox.py> |
| infinitive | Impersonates a SAM on the Carrier Infinity ABCD RS-485 bus for local control | 116 | <https://github.com/acd/infinitive> |
| remeha_home | Home Assistant integration for the private Remeha Home cloud API | 114 | <https://github.com/msvisser/remeha_home> |
| esphome_toshiba_suzumi | ESPHome component for Toshiba air conditioners via their serial protocol | 113 | <https://github.com/pedobry/esphome_toshiba_suzumi> |
| FujiHeatPump | Control Fujitsu air conditioners from Arduino via the reverse-engineered indoor-unit bus | 107 | <https://github.com/unreality/FujiHeatPump> |
| esphome-truma_inetbox | ESPHome component to control Truma CP Plus heaters over LIN | 99 | <https://github.com/Fabian-Schmidt/esphome-truma_inetbox> |
| luxtronik | Home Assistant integration for Luxtronik heat pump controllers | 99 | <https://github.com/Bouni/luxtronik> |
| esphome-fujitsu | ESPHome component for Fujitsu air conditioners via the reverse-engineered indoor-unit bus | 89 | <https://github.com/FujiHeatPump/esphome-fujitsu> |
| ecodan-ha-local | Local Home Assistant control of Mitsubishi Ecodan heat pumps via CN105 | 85 | <https://github.com/rbroker/ecodan-ha-local> |
| python-panasonic-comfort-cloud | Python module for the private Panasonic Comfort Cloud climate API | 85 | <https://github.com/lostfields/python-panasonic-comfort-cloud> |
| ramses_rf | Interface for the Honeywell RAMSES-II RF protocol used by evohome and similar systems | 83 | <https://github.com/ramses-rf/ramses_rf> |
| WPalaControl | D1 Mini replacement for the Palazzetti/Jotul/Godin stove ConnectionBox (Fumis serial protocol) | 76 | <https://github.com/Domochip/WPalaControl> |
| Mitsubishi-CN105-Protocol-Decode | Documentation of the Mitsubishi CN105 protocol of Ecodan air-to-water heat pumps | 74 | <https://github.com/m000c400/Mitsubishi-CN105-Protocol-Decode> |
| OneESP32ToRuleThemAll | Open-source ISG replacement for Stiebel Eltron/Tecalor heat pumps over CAN bus | 74 | <https://github.com/kr0ner/OneESP32ToRuleThemAll> |
| taixia | Home Assistant integration for appliances using the Taiwanese TaiXia SA protocol | 73 | <https://github.com/tsunglung/taixia> |
| AquaMQTT | Monitor and control Groupe Atlantic water heat pumps (Explorer, Calypso) via MQTT | 70 | <https://github.com/tspopp/AquaMQTT> |
| oekofen-pellematic-compact | Home Assistant integration for ÖkoFEN Pellematic via its JSON/TCP interface | 70 | <https://github.com/dominikamann/oekofen-pellematic-compact> |
| hass-WEM-Portal | Home Assistant component scraping the Weishaupt WEM Portal | 68 | <https://github.com/erikkastelec/hass-WEM-Portal> |
| evofw3 | Firmware for listening to and sending Honeywell evohome RAMSES-II radio messages | 64 | <https://github.com/ghoti57/evofw3> |
| esphome-hlink-ac | ESPHome component for Hitachi air conditioners via the H-Link protocol | 61 | <https://github.com/lumixen/esphome-hlink-ac> |
| python-luxtronik | Python library for the Luxtronik heat pump controller (Alpha Innotec, Novelan) protocol | 49 | <https://github.com/Bouni/python-luxtronik> |
| ESPHome-Froeling-Lambdatronic_3200 | ESPHome RS232 reader for Fröling Lambdatronic 3200 boilers | 46 | <https://github.com/GyroGearl00se/ESPHome-Froeling-Lambdatronic_3200> |
| maestrogateway | Gateway for MCZ pellet stoves with Maestro technology via their websocket protocol | 46 | <https://github.com/Chibald/maestrogateway> |
| Diematic_to_MQTT | MQTT interface for De Dietrich Diematic3 heating regulators | 44 | <https://github.com/Benoit3/Diematic_to_MQTT> |
| esphome_gree_ac | ESPHome component for Gree air conditioners over the UART wifi-module port | 43 | <https://github.com/piotrva/esphome_gree_ac> |
| CAN-Gateway | Wi-Fi/LAN to CAN gateway for Hoval TopTronic E devices | 42 | <https://github.com/wladwnt/CAN-Gateway> |
| python-thermia-online-api | Python API for Thermia heat pumps via the Thermia Online cloud | 42 | <https://github.com/klejejs/python-thermia-online-api> |
| InsideViessmannVitosoft | Description of Viessmann Optolink protocol and Vitosoft XML data files | 39 | <https://github.com/sarnau/InsideViessmannVitosoft> |
| nano_pk | Home Assistant integration reading the Hargassner Nano-PK boiler data stream | 36 | <https://github.com/TheRealKillaruna/nano_pk> |
| hass-hitachi_yutaki | Home Assistant integration for Hitachi Yutaki heat pumps via the ATW-MBS gateway | 35 | <https://github.com/alepee/hass-hitachi_yutaki> |
| ebusd-configuration-weishaupt | ebusd configuration files for Weishaupt WTC devices | 27 | <https://github.com/J0EK3R/ebusd-configuration-weishaupt> |
| HaierProtocol | Library implementing the Haier air-conditioner serial communication protocol | 27 | <https://github.com/paveldn/HaierProtocol> |
| uhomeuponor | Home Assistant component for Uponor Smatrix underfloor heating via the Uhome API | 26 | <https://github.com/dave-code-ruiz/uhomeuponor> |
| ESPHome-Brivis-Networker | Replacement PCB and ESPHome firmware for Brivis ducted heater networker | 23 | <https://github.com/Makin-Things/ESPHome-Brivis-Networker> |
| oekofen-json-documentation | Community documentation of the undocumented ÖkoFEN pellet heating JSON interface | 21 | <https://github.com/thannaske/oekofen-json-documentation> |
| ha-windhager | Home Assistant integration for Windhager heating systems | 20 | <https://github.com/vermi0ffh/ha-windhager> |
| buderus2mqtt | Gateway between the Buderus KM200 internet gateway and MQTT | 18 | <https://github.com/krambox/buderus2mqtt> |
| HLinkSniffer | H-LINK bus sniffer for Hitachi Yutaki heat pumps on a Raspberry Pi | 18 | <https://github.com/hankerspace/HLinkSniffer> |
| ha-harvia-sauna | Home Assistant integration for Harvia sauna heaters (Xenio Wi-Fi, Fenix) | 16 | <https://github.com/WiesiDeluxe/ha-harvia-sauna> |
| rinnaicontrolr | Python interface for the private Rinnai Control-R API | 16 | <https://github.com/explosivo22/rinnaicontrolr> |
| Hargassner_NodeJS_Adapter | Node.js adapter for Hargassner boilers with Touch Control | 15 | <https://github.com/schuppenkarp/Hargassner_NodeJS_Adapter> |
| hoval-gateway | Gateway for reading Hoval heating over its proprietary CAN bus | 15 | <https://github.com/chrishrb/hoval-gateway> |
| Weishaupt_CanApiJson | Documentation of Weishaupt WTC CanApiJson, a CAN-like protocol over JSON | 15 | <https://github.com/BorgNumberOne/Weishaupt_CanApiJson> |
| rinnai-control-panel-sigrok-pd | Sigrok decoder for the internal protocol of Rinnai gas heater control panels | 13 | <https://github.com/ayavilevich/rinnai-control-panel-sigrok-pd> |
| MicronovaPelletStoveController | Code to control Micronova pellet stove controllers over their serial protocol | 12 | <https://github.com/k3a/MicronovaPelletStoveController> |
| Palazzetti | Library to control Palazzetti (Fumis) pellet stoves over serial | 12 | <https://github.com/Domochip/Palazzetti> |
| viessmann-optolink2mqtt | Bridge between Viessmann Optolink devices and MQTT | 12 | <https://github.com/f18m/viessmann-optolink2mqtt> |
| optolink-bridge | Bridges the Viessmann Optolink bus and publishes values to MQTT and Home Assistant | 11 | <https://github.com/kristian/optolink-bridge> |
| rinnai-serial-decoder | PulseView decoder for Rinnai hot-water unit serial communication | 10 | <https://github.com/genmeim/rinnai-serial-decoder> |
| vitalk | Communication with Viessmann Vitodens 300 via the Optolink interface | 9 | <https://github.com/klauweg/vitalk> |
| wolf_ism8 | Read data from WOLF heating systems via the ISM8 module protocol | 9 | <https://github.com/marcschmiedchen/wolf_ism8> |
| esphome_vitohome | ESPHome component for Viessmann heating controllers over Optolink | 8 | <https://github.com/SoulSolistice/esphome_vitohome> |
| ioBroker.e3oncan | ioBroker adapter for Viessmann E3-series heating over CAN bus | 8 | <https://github.com/MyHomeMyData/ioBroker.e3oncan> |
| vogod | Daemon exposing a Viessmann heating device's Optolink data as a REST API | 8 | <https://github.com/speters/vogod> |
| Hoval-GW | Python gateway for the Hoval CAN bus | 7 | <https://github.com/zittix/Hoval-GW> |
| wem-python | Python interpreter for the Weishaupt WEM CAN bus | 7 | <https://github.com/geronet1/wem-python> |
| ebus | Java eBUS library with device configs, used by the openHAB eBUS binding | 6 | <https://github.com/csowada/ebus> |
| mertik-fireplace-wifi-ha | Home Assistant plugin for fireplaces using the Mertik Maxitrol Wi-Fi module | 6 | <https://github.com/jkfran/mertik-fireplace-wifi-ha> |
| node-weishaupt-api | Node module for Weishaupt heaters over the WCM-COM 1.0 module | 6 | <https://github.com/foxriver76/node-weishaupt-api> |
| py-palazzetti-api | Python library controlling a Palazzetti stove through its Connection Box | 6 | <https://github.com/dotvav/py-palazzetti-api> |
| froeling-connect | Python wrapper for the private Fröling Connect cloud API | 5 | <https://github.com/Layf21/froeling-connect> |
| keba_keenergy_api | Python wrapper for the KEBA KeEnergy Web HMI API used by heat pumps | 5 | <https://github.com/superbox-dev/keba_keenergy_api> |
| ebus | C++ library for eBUS heating bus communication | 4 | <https://github.com/yuhu-/ebus> |
| Py-Weishaupt-WCM-COM | Python package for the Weishaupt WCM-COM home module | 4 | <https://github.com/schmiegelt/Py-Weishaupt-WCM-COM> |
| pyatag | Python API to connect to the Atag One thermostat | 4 | <https://github.com/MatsNl/pyatag> |
| windhager-rest-api-documentation | Documentation of the Windhager MES Infinity RC7030 web server REST API | 3 | <https://github.com/domfie/windhager-rest-api-documentation> |
| tasmota-biowin | Tasmota app reading Windhager BioWIN data from the MES D application bus | 2 | <https://github.com/aJunk/tasmota-biowin> |
| Wolf_ebusd_config | ebusd configuration files for Wolf BM-2/FHA/MM-1 heating devices | 2 | <https://github.com/Ces1254/Wolf_ebusd_config> |
| Froeling-HA | Home Assistant integration for Fröling boilers using their proprietary protocol | 1 | <https://github.com/Tropaion/Froeling-HA> |
| froeling-proxy | Library and TCP server for communicating with Fröling wood boilers | 1 | <https://github.com/mpolajnar/froeling-proxy> |
| weishaupt_modbus_rtu | Reverse engineering of the Weishaupt heat pump Modbus RTU RS485 interface | 1 | <https://github.com/backuprestore/weishaupt_modbus_rtu> |
| ParadigmaHeatingReader | Reverse-engineered reader for Paradigma SystaComfort 2 heating controllers | 0 | <https://github.com/kayr7/ParadigmaHeatingReader> |
| Retro-Fujitsu-ESPHome | ESPHome integration for a Fujitsu heat pump over its LIN bus | 0 | <https://github.com/endofthewurst/Retro-Fujitsu-ESPHome> |

## Industrial Robots

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| KUKAVARPROXY | TCP server on KUKA robots exposing variables via the OpenShowVar protocol | 136 | <https://github.com/ImtsSrl/KUKAVARPROXY> |

## PLC Protocols

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| HslCommunication | C# industrial comms library covering Siemens, Mitsubishi, Omron, AB, Keyence and other PLC protocols | 2,134 | <https://github.com/dathlin/HslCommunication> |
| plc4x | Apache PLC4X: drivers for S7, Allen-Bradley, Beckhoff, Modbus and other PLC protocols in Java/Go/C | 1,755 | <https://github.com/apache/plc4x> |
| IoTClient | .NET client for industrial protocols: Siemens S7, Mitsubishi MC, Omron FINS, Allen-Bradley | 1,689 | <https://github.com/zhaopeiym/IoTClient> |
| s7netplus | S7.NET+: .NET library that talks the Siemens S7comm protocol to Step7 PLCs | 1,634 | <https://github.com/S7NetPlus/s7netplus> |
| libplctag | Portable C library for Allen-Bradley (CIP/PCCC) and Modbus PLC tag access | 905 | <https://github.com/libplctag/libplctag> |
| python-snap7 | Pure-Python client for Siemens S7comm, the undocumented protocol of S7-300/400/1200/1500 PLCs | 855 | <https://github.com/gijzelaerr/python-snap7> |
| pylogix | Python library to read/write tags on Allen-Bradley ControlLogix/CompactLogix PLCs | 733 | <https://github.com/dmroeder/pylogix> |
| pycomm3 | Python EtherNet/IP library for Allen-Bradley Logix and SLC/MicroLogix PLCs, incl. undocumented services | 519 | <https://github.com/ottowayi/pycomm3> |
| DotNetSiemensPLCToolBoxLibrary | .NET library to access Siemens PLCs and parse Step5/Step7 project files | 481 | <https://github.com/dotnetprojects/DotNetSiemensPLCToolBoxLibrary> |
| gos7 | Go implementation of the Siemens S7comm protocol | 405 | <https://github.com/robinson/gos7> |
| nodeS7 | Node.js library for Siemens S7 PLC communication over the S7comm protocol | 399 | <https://github.com/plcpeople/nodeS7> |
| s7connector | Java S7 PLC connector implementing the Siemens S7comm protocol | 339 | <https://github.com/s7connector/s7connector> |
| iot-communication | Java library for Siemens S7, Mitsubishi MELSEC and Omron FINS PLC protocols | 302 | <https://github.com/xingshuangs/iot-communication> |
| libplctag.NET | .NET wrapper for the libplctag Allen-Bradley PLC library | 299 | <https://github.com/libplctag/libplctag.NET> |
| snap7 | Snap7 suite: open client, server and partner implementation of the Siemens S7comm protocol | 284 | <https://github.com/SCADACS/snap7> |
| Sharp7 | Sharp7: C# port of the Snap7 Siemens S7comm client packaged for NuGet | 258 | <https://github.com/fbarresi/Sharp7> |
| S7CommPlusDriver | Reverse-engineered S7comm-plus driver for Siemens S7-1200/1500 PLCs | 228 | <https://github.com/thomas-v2/S7CommPlusDriver> |
| node-snap7 | Node.js bindings for the Snap7 Siemens S7 communication library | 180 | <https://github.com/mathiask88/node-snap7> |
| snap7 | Official Snap7 repository: multi-platform Siemens S7 Ethernet communication suite | 175 | <https://github.com/davenardella/snap7> |
| pycomm | Python modules to talk to Allen-Bradley PLCs (ControlLogix tags, SLC/PCCC) | 158 | <https://github.com/ruscito/pycomm> |
| SoftPlc | Software PLC that emulates a Siemens S7 server over S7comm, with Docker support | 154 | <https://github.com/fbarresi/SoftPlc> |
| node-red-contrib-s7 | Node-RED nodes to read and write Siemens S7 PLCs via a JS S7comm implementation | 135 | <https://github.com/st-one-io/node-red-contrib-s7> |
| libfins | Multi-platform C library for the Omron FINS PLC protocol | 133 | <https://github.com/lammertb/libfins> |
| mcprotocol | Node.js implementation of the Mitsubishi MC protocol for FX/Q/L PLCs | 121 | <https://github.com/plcpeople/mcprotocol> |
| acd | Tools to parse Rockwell Studio 5000 .ACD project files, a proprietary binary format | 112 | <https://github.com/hutcheb/acd> |
| pymcprotocol | Python implementation of the Mitsubishi MELSEC MC protocol | 105 | <https://github.com/senrust/pymcprotocol> |
| mokka7 | Mokka7: pure-Java port of the Snap7 Siemens S7comm client | 69 | <https://github.com/comtel2000/mokka7> |
| go-mcprotocol | Go client for the Mitsubishi MELSEC MC protocol | 51 | <https://github.com/future-architect/go-mcprotocol> |
| node-omron-fins | Node.js implementation of the Omron FINS protocol | 47 | <https://github.com/ptrks/node-omron-fins> |
| ge-ethernet-SRTP | Working demo of the proprietary GE SRTP PLC Ethernet protocol, reverse engineered | 45 | <https://github.com/TheMadHatt3r/ge-ethernet-SRTP> |
| s7commwireshark | Wireshark dissector plugin for Siemens S7comm and S7comm-plus (export of the SourceForge project) | 33 | <https://github.com/moki-ics/s7commwireshark> |
| pymelsec | Python 3 implementation of Mitsubishi MELSEC communication | 31 | <https://github.com/NothinRandom/pymelsec> |
| jfins | Non-blocking Omron FINS master and slave for Java | 28 | <https://github.com/siyka-au/jfins> |
| fxplc | Python connector for the low-level Mitsubishi FX series serial programming-port protocol | 26 | <https://github.com/KrystianD/fxplc> |
| Rust7 | Native Rust Siemens S7 client in the style of Snap7, no FFI | 26 | <https://github.com/davenardella/Rust7> |
| CoDeSys_S7Comm | S7comm client implemented in CoDeSys to talk to Siemens PLCs from other PLCs | 24 | <https://github.com/NothinRandom/CoDeSys_S7Comm> |
| omron-fins-go | Go client for Omron FINS commands | 18 | <https://github.com/hiroeorz/omron-fins-go> |
| packet-ge-srtp | Wireshark dissector for the GE-Fanuc Service Request Transfer Protocol (SRTP) | 15 | <https://github.com/PalaIndustrial/packet-ge-srtp> |
| S7CommPlusV3Driver | .NET driver for Siemens S7-1200/1500 using S7comm-plus V3, with or without TLS | 14 | <https://github.com/lircy/S7CommPlusV3Driver> |
| node-red-contrib-pccc | Node-RED node for Allen-Bradley PLCs using the PCCC protocol | 11 | <https://github.com/st-one-io/node-red-contrib-pccc> |
| rs-snap7 | Pure-Rust async Siemens S7 library with S7comm and S7comm-plus support | 9 | <https://github.com/cool0looc/rs-snap7> |
| FinsToToolbusGateway | Gateway from Omron FINS to the undocumented Sysmac Toolbus programming protocol | 0 | <https://github.com/Vladimirek/FinsToToolbusGateway> |

## Ventilation, Pool & Water

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| WiFi-remote-for-Bestway-Lay-Z-SPA | ESP8266 Wi-Fi remote for Bestway Lay-Z-Spa hot tubs via the display bus | 416 | <https://github.com/visualapproach/WiFi-remote-for-Bestway-Lay-Z-SPA> |
| ithowifi | ESP32 Wi-Fi add-on for Itho ventilation using its I2C protocol | 287 | <https://github.com/arjenhiemstra/ithowifi> |
| AqualinkD | Daemon controlling Jandy Aqualink RS pool equipment over RS485 | 238 | <https://github.com/aqualinkd/AqualinkD> |
| comfoair-esp32 | ESP32 firmware to interact with Zehnder ComfoAir Q via CAN | 155 | <https://github.com/vekexasia/comfoair-esp32> |
| balboa_worldwide_app | Ruby library for Balboa spa Wi-Fi module and RS-485 protocol | 123 | <https://github.com/ccutrer/balboa_worldwide_app> |
| aiocomfoconnect | Async Python library for the Zehnder ComfoConnect LAN C protocol (ComfoAir Q) | 108 | <https://github.com/michaelarnauts/aiocomfoconnect> |
| esphome-zehnder-comfoair | ESPHome control of Zehnder ComfoAir Q over CAN bus | 96 | <https://github.com/yoziru/esphome-zehnder-comfoair> |
| comfoconnect *(archived)* | Python library for the Zehnder ComfoConnect LAN C protocol | 95 | <https://github.com/michaelarnauts/comfoconnect> |
| esphome-comfoair | ESPHome configuration for Zehnder ComfoAir units over the serial protocol | 84 | <https://github.com/wichers/esphome-comfoair> |
| intellicenter | Home Assistant integration for Pentair IntelliCenter pool systems | 52 | <https://github.com/jlvaillant/intellicenter> |
| esp32-pentair-controller | Control Pentair pool equipment via RS485 from an ESP32 to MQTT | 38 | <https://github.com/michaelusner/esp32-pentair-controller> |
| zcan | API proxy for Zehnder ComfoAir Q devices on the CAN bus | 36 | <https://github.com/marco-hoyer/zcan> |
| vallox_websocket_api | Async API for Vallox ventilation units via their websocket protocol | 32 | <https://github.com/yozik04/vallox_websocket_api> |
| ZehnderComfoair | Reverse engineering the Zehnder ComfoFan ventilation RF protocol | 29 | <https://github.com/eelcohn/ZehnderComfoair> |
| esphome-helios-kwl | ESPHome integration for Helios KWL ventilation via RS485 | 23 | <https://github.com/lostcontrol/esphome-helios-kwl> |
| hayward-pool-heater-mqtt | Control a Hayward pool heater over its bus via MQTT | 20 | <https://github.com/njanik/hayward-pool-heater-mqtt> |
| screenlogic_over_ip | IP communication with Pentair ScreenLogic2 pool controllers | 17 | <https://github.com/ceisenach/screenlogic_over_ip> |
| node-comfoair | Node.js library for Zehnder ComfoAir 350 ventilation units | 16 | <https://github.com/coolchip/node-comfoair> |
| pypentair | Python package for Pentair pool pumps over RS-485 | 14 | <https://github.com/cilynx/pypentair> |
| ecowater-softener | Python library pulling data from EcoWater water softeners | 10 | <https://github.com/barleybobs/ecowater-softener> |
| hayward-pool | Scrape data from Hayward Pro Logic / Aqua Plus via the AquaConnect HomeNet | 7 | <https://github.com/ma-nathan/hayward-pool> |
| comfo | Go implementation of the Zehnder ComfoAir serial protocol | 4 | <https://github.com/ti-mo/comfo> |
