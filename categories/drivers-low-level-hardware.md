# Drivers & Low-level Hardware

[← All categories](../README.md) · 377 projects

- [Apple Silicon (Asahi)](#apple-silicon-asahi) (19)
- [Drawing Tablets & Input](#drawing-tablets--input) (16)
- [Firmware/BIOS (coreboot, UEFI)](#firmwarebios-coreboot-uefi) (19)
- [GPU Drivers](#gpu-drivers) (20)
- [Gaming Laptops & Handheld PCs](#gaming-laptops--handheld-pcs) (80)
- [Headsets, Audio Interfaces & Webcams](#headsets-audio-interfaces--webcams) (31)
- [Lab Instruments & Thermal Cameras](#lab-instruments--thermal-cameras) (72)
- [Laptop EC & Peripherals](#laptop-ec--peripherals) (69)
- [Printers, Scanners & Fingerprint](#printers-scanners--fingerprint) (35)
- [Wi-Fi & Radios](#wi-fi--radios) (16)

## Apple Silicon (Asahi)

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| tinygrad | ML framework whose extra/accel/ane holds reverse-engineered Apple Neural Engine work | 33,739 | <https://github.com/tinygrad/tinygrad> |
| neural-engine | Community documentation of the Apple Neural Engine and how Core ML uses it | 2,543 | <https://github.com/hollance/neural-engine> |
| muvm | microVM runner used by Asahi to run x86 games with FEX on 4K-page hosts | 981 | <https://github.com/AsahiLinux/muvm> |
| linux-m1 | Linux kernel source tree | 871 | <https://github.com/corellium/linux-m1> |
| ane (Linux ANE driver) | Reverse-engineered Linux driver and userspace for the Apple Neural Engine | 539 | <https://github.com/eiln/ane> |
| macvdmtool | Tool to send Apple USB-PD vendor-defined messages (serial/reboot) between Macs | 375 | <https://github.com/AsahiLinux/macvdmtool> |
| asahi-audio | DSP and audio configuration for Apple Silicon Macs on Linux | 215 | <https://github.com/AsahiLinux/asahi-audio> |
| speakersafetyd | Userspace speaker protection daemon for Apple Silicon Macs under Linux | 204 | <https://github.com/AsahiLinux/speakersafetyd> |
| Asahi U-Boot | U-Boot port for Apple Silicon Macs used in the Asahi boot chain | 201 | <https://github.com/AsahiLinux/u-boot> |
| avd | Reverse-engineered Apple Video Decoder (AVD) driver work for Linux | 183 | <https://github.com/eiln/avd> |
| linux-t2-patches | Linux patches for T2-chip Intel Macs (keyboard, touchbar, audio, BCE) | 103 | <https://github.com/t2linux/linux-t2-patches> |
| apple-bce-drv | Reverse-engineered Linux driver for the Apple T2 Bridge Controller (BCE) | 101 | <https://github.com/t2linux/apple-bce-drv> |
| asahi-nvram | Tools to read and write Apple Silicon NVRAM from Linux | 77 | <https://github.com/AsahiLinux/asahi-nvram> |
| anecc | Run CoreML models on the Apple Neural Engine under Asahi Linux | 62 | <https://github.com/eiln/anecc> |
| coreml_to_ane_hwx | Converts Core ML models to Apple Neural Engine HWX binaries for analysis | 51 | <https://github.com/freedomtan/coreml_to_ane_hwx> |
| asahi-scripts | Asahi Linux support scripts (firmware extraction, boot setup) | 50 | <https://github.com/AsahiLinux/asahi-scripts> |
| mdaiter/ane | Reverse-engineering artifacts for Apple ANECompiler, Espresso and AppleNeuralEngine | 40 | <https://github.com/mdaiter/ane> |
| m1-pmu-gen | Generates Linux perf event tables for Apple Silicon PMU counters | 20 | <https://github.com/cyyself/m1-pmu-gen> |
| alsa-ucm-conf-asahi | ALSA UCM configuration for Apple Silicon audio hardware | 7 | <https://github.com/AsahiLinux/alsa-ucm-conf-asahi> |

## Drawing Tablets & Input

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| wacom-driver-fix | Patched Wacom drivers for old Bamboo, Intuos and Cintiq tablets on modern macOS | 1,608 | <https://github.com/thenickdude/wacom-driver-fix> |
| TabletDriver | Low-latency Windows graphics tablet driver for Wacom, Huion, XP-Pen and others | 1,227 | <https://github.com/hawku/TabletDriver> |
| gsl-firmware | Firmware collection for Silead touchscreen controllers, extracted from Windows drivers for Linux | 387 | <https://github.com/onitake/gsl-firmware> |
| universal-pidff | Linux PIDFF force feedback driver with fixes for Moza, Simagic and other wheelbases | 267 | <https://github.com/JacKeTUs/universal-pidff> |
| dkms-hid-nintendo *(archived)* | DKMS package of the hid-nintendo driver for Joy-Con and Switch Pro controllers | 259 | <https://github.com/nicman23/dkms-hid-nintendo> |
| Tuhi | Linux app to download drawings from Wacom SmartPad devices over a reverse engineered BLE protocol | 169 | <https://github.com/tuhiproject/tuhi> |
| veikk-linux-driver | Linux kernel driver for VEIKK graphics tablets | 142 | <https://github.com/jlam55555/veikk-linux-driver> |
| libx52 | Saitek X52/X52 Pro joystick MFD and LED driver and mapping software for Linux | 133 | <https://github.com/nirenjan/libx52> |
| TuxBox | Linux driver for TourBox controllers over USB and Bluetooth, with haptics and GUI config | 109 | <https://github.com/AndyCappDev/tuxbox> |
| inklingreader | GNU/Linux replacement for the Wacom Inkling SketchManager | 50 | <https://github.com/roelj/inklingreader> |
| waxbee | USB bridge for serial and ADB Wacom and other legacy pen tablets | 48 | <https://github.com/popbee/waxbee> |
| Logitech-G923-Linux-Kernel-Driver | Linux kernel support for the Logitech G923 steering wheel | 43 | <https://github.com/ZRtmWrJqXcjbqBLIMBYMCeUw/Logitech-G923-Linux-Kernel-Driver> |
| TabletMagic | Mac OS X driver for Wacom serial tablets and TabletPC digitizers | 43 | <https://github.com/thinkyhead/TabletMagic> |
| uclogic-tools | Diagnostic tools for UC-Logic (Huion, XP-Pen, Gaomon) graphics tablets | 41 | <https://github.com/DIGImend/uclogic-tools> |
| intuos4-oled | Send images and text to the Wacom Intuos 4 button OLEDs on Linux | 20 | <https://github.com/sanette/intuos4-oled> |
| Wacom-STU-WebHID | JavaScript library for Wacom STU signature pads over WebHID | 20 | <https://github.com/pabloko/Wacom-STU-WebHID> |

## Firmware/BIOS (coreboot, UEFI)

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| fwupd | Linux firmware updater with many reverse-engineered device update protocols | 4,188 | <https://github.com/fwupd/fwupd> |
| MEAnalyzer | Intel/AMD engine firmware (ME, TXE, CSE, PSP) analysis tool | 1,332 | <https://github.com/platomav/MEAnalyzer> |
| flashrom | Utility to read and write flash chips on mainboards, programmers and devices | 1,182 | <https://github.com/flashrom/flashrom> |
| efiXplorer | IDA plugin for UEFI firmware analysis and reverse engineering | 1,136 | <https://github.com/REhints/efiXplorer> |
| UEFI-Editor | Editor for UEFI setup IFR forms to expose hidden BIOS settings | 960 | <https://github.com/BoringBoredom/UEFI-Editor> |
| skulls | Prebuilt coreboot images and flashing docs for ThinkPad laptops | 848 | <https://github.com/merge/skulls> |
| PSPTool | Parses and modifies AMD Platform Security Processor firmware blobs | 716 | <https://github.com/PSPReverse/PSPTool> |
| IFRExtractor-RS | Extracts UEFI HII IFR setup forms into human-readable text | 487 | <https://github.com/LongSoft/IFRExtractor-RS> |
| fiano | Go tools and library for parsing and modifying UEFI firmware images | 375 | <https://github.com/linuxboot/fiano> |
| UEFI_RETool *(archived)* | Tool for analysing UEFI firmware modules | 369 | <https://github.com/yeggor/uefi_retool> |
| Dasharo coreboot | Dasharo's coreboot fork with ports for commercial desktops and laptops | 153 | <https://github.com/Dasharo/coreboot> |
| coreboot-configurator | GUI to change coreboot CBFS settings via nvramtool | 102 | <https://github.com/StarLabsLtd/coreboot-configurator> |
| MrChromebox firmware | Issue tracker for MrChromebox coreboot-based UEFI firmware for Chromebooks | 99 | <https://github.com/MrChromebox/firmware> |
| x210 | Patches, mods and docs for the 51nb X210 ThinkPad-derived board | 41 | <https://github.com/harrykipper/x210> |
| bootguard-status | List of mainboards and their Intel Boot Guard status for coreboot porting | 33 | <https://github.com/felixsinger/bootguard-status> |
| mmga *(archived)* | Flash coreboot on MacBooks without an external SPI programmer | 32 | <https://github.com/gch1p/mmga> |
| intel_ma | Inspect Intel ME/TXE/CSME management firmware images | 14 | <https://github.com/seuros/intel_ma> |
| pch-pads-parser *(archived)* | Parses inteltool PCH GPIO dumps into coreboot pad configs for board ports | 10 | <https://github.com/maxpoliak/pch-pads-parser> |
| Libreboot lbmk | Libreboot build system: coreboot board ports, blob extraction and payloads |  | <https://codeberg.org/libreboot/lbmk> |

## GPU Drivers

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| applecpu | Reverse-engineered Apple Firestorm/Icestorm CPU microarchitecture notes | 265 | <https://github.com/dougallj/applecpu> |
| mesa-lima | Development tree of the Lima Mali-400 driver before upstream Mesa merge | 164 | <https://github.com/yuq/mesa-lima> |
| gddr6 | Linux GDDR6/GDDR6X VRAM temperature reader for NVIDIA RTX cards | 157 | <https://github.com/olealgoritme/gddr6> |
| radeon-tools | AMD Radeon reverse engineering tools | 154 | <https://github.com/fail0verflow/radeon-tools> |
| grate | Reverse-engineering tools and docs for the NVIDIA Tegra 2/3 GPU (open Tegra graphics) | 90 | <https://github.com/grate-driver/grate> |
| linux_openpvrsgx | Reshaping PowerVR SGX GPL kernel drivers for mainline Linux | 65 | <https://github.com/openpvrsgx-devgroup/linux_openpvrsgx> |
| linux-cedrus | Mainline kernel tree for the Allwinner VPU (Cedrus) reverse engineering effort | 61 | <https://github.com/bootlin/linux-cedrus> |
| dlss-nr-on-intel | Independent reimplementation of the DLSS neural rendering inference pass on an Intel iGPU | 58 | <https://github.com/Uzbekunknown/dlss-nr-on-intel> |
| NVFC | Open-source tool for monitoring, configuring and overclocking NVIDIA GPUs | 50 | <https://github.com/graphitemaster/NVFC> |
| mali-isa-docs | Reverse-engineered documentation of Arm Mali GPU shader ISAs | 43 | <https://github.com/cwabbott0/mali-isa-docs> |
| tegra-re *(archived)* | Reverse engineering of NVIDIA's Tegra Linux driver | 36 | <https://github.com/kusma/tegra-re> |
| blackwell-isa | Reverse-engineered ISA database for NVIDIA SM120 Blackwell GPUs | 16 | <https://github.com/kacper-daftcode/blackwell-isa> |
| libvdpau-tegra | VDPAU video decode driver for NVIDIA Tegra built from reverse-engineered hardware | 16 | <https://github.com/grate-driver/libvdpau-tegra> |
| etna-gpu-tools | Vivante GPU debugging and reverse-engineering tools from the etnaviv project | 4 | <https://github.com/etnaviv/etna-gpu-tools> |
| Asahi Mesa driver | Mesa OpenGL/Vulkan driver for Apple AGX GPUs, with reverse-engineered ISA notes |  | <https://docs.mesa3d.org/drivers/asahi.html> |
| Freedreno / Turnip | Reverse-engineered Mesa OpenGL and Vulkan drivers for Qualcomm Adreno GPUs |  | <https://docs.mesa3d.org/drivers/freedreno.html> |
| Lima | Reverse-engineered Mesa driver for Arm Mali-400/450 (Utgard) GPUs |  | <https://docs.mesa3d.org/drivers/lima.html> |
| Mesa | Mesa 3D: hosts reverse-engineered GPU drivers (panfrost, lima, freedreno, etnaviv, nouveau, asahi, NVK) |  | <https://gitlab.freedesktop.org/mesa/mesa> |
| NVK | Open-source Mesa Vulkan driver for NVIDIA GPUs built on nouveau |  | <https://docs.mesa3d.org/drivers/nvk.html> |
| Panfrost / PanVK | Reverse-engineered Mesa driver for Arm Mali Midgard, Bifrost and Valhall GPUs |  | <https://docs.mesa3d.org/drivers/panfrost.html> |

## Gaming Laptops & Handheld PCs

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| Lenovo Legion Toolkit *(archived)* | Lightweight replacement for Lenovo Vantage and Hotkeys on Legion laptops | 7,546 | <https://github.com/BartoszCichecki/LenovoLegionToolkit> |
| Universal x86 Tuning Utility | Power, TDP and undervolt tuning for Intel/AMD laptops and handhelds | 2,874 | <https://github.com/JamesCJ60/Universal-x86-Tuning-Utility> |
| Lenovo Legion Toolkit (community) | Community continuation of Lenovo Legion Toolkit, a Vantage replacement for Legion laptops | 2,299 | <https://github.com/LenovoLegionToolkit-Team/LenovoLegionToolkit> |
| Handheld Companion | Windows tool for handheld PCs: controller emulation, gyro, TDP and fan control without vendor apps | 1,734 | <https://github.com/Valkirie/HandheldCompanion> |
| Steam Deck Tools | Windows fan, overlay, power and Steam Controller emulation for the Steam Deck hardware | 1,143 | <https://github.com/ayufan/steam-deck-tools> |
| alienfx-tools | Open tools for Alienware lights, fans and power control, replacing AWCC | 870 | <https://github.com/T-Troll/alienfx-tools> |
| Thermal Control Center for Dell G15 | Open-source alternative to Alienware Command Center for Dell G15 thermal modes | 841 | <https://github.com/AlexIII/tcc-g15> |
| rogauracore | RGB keyboard control for ASUS ROG laptops on Linux (reverse engineered USB commands) | 778 | <https://github.com/wroberts/rogauracore> |
| Div Acer Manager Max | Linux GUI for Acer Predator/Nitro laptops, replicating NitroSense/PredatorSense features | 738 | <https://github.com/PXDiv/Div-Acer-Manager-Max> |
| MControlCenter | Linux app to change MSI laptop fan, battery and performance settings via the EC | 715 | <https://github.com/dmitry-s93/MControlCenter> |
| OmenSuperHub | HP Omen performance, fan and keyboard lighting control with power limit unlock | 558 | <https://github.com/breadeding/OmenSuperHub> |
| L5P-Keyboard-RGB | Cross-platform control of the 4-zone RGB keyboard on Lenovo Legion laptops | 525 | <https://github.com/4JX/L5P-Keyboard-RGB> |
| vantage | Lenovo Vantage features (conservation mode, fn-lock, power) for Linux | 510 | <https://github.com/niizam/vantage> |
| g-helper-linux | Unofficial Linux port of G-Helper for ASUS ROG, TUF and Zephyrus laptops | 509 | <https://github.com/utajum/g-helper-linux> |
| asus-numberpad-driver | Linux driver for the illuminated NumberPad touchpad on ASUS laptops | 451 | <https://github.com/asus-linux-drivers/asus-numberpad-driver> |
| steam-deck-windows-usermode-driver *(archived)* | Windows usermode driver for the Steam Deck's built-in controller | 439 | <https://github.com/mKenfenheuer/steam-deck-windows-usermode-driver> |
| OmenMon | HP Omen fan, temperature and backlight control via WMI BIOS and EC, replacing Omen Gaming Hub | 406 | <https://github.com/OmenMon/OmenMon> |
| asus-fan-control | Fan control for ASUS laptops on Linux via ACPI calls | 392 | <https://github.com/dominiksalvet/asus-fan-control> |
| atrofac | Library and CLI to control ASUS ROG power plans and fan curves without Armoury Crate | 356 | <https://github.com/cronosun/atrofac> |
| razer-laptop-control *(archived)* | Driver and software to control fan and performance modes of Razer Blade laptops on Linux | 347 | <https://github.com/rnd-ash/razer-laptop-control> |
| alienfx | CLI and GUI to control Alienware lighting effects on Linux | 339 | <https://github.com/trackmastersteve/alienfx> |
| msi-keyboard | MSI SteelSeries laptop keyboard LED controller (reverse engineered HID) | 313 | <https://github.com/stephenlacy/msi-keyboard> |
| SimpleDeckyTDP | Decky plugin for TDP, CPU boost and GPU control on Linux PC handhelds | 297 | <https://github.com/aarron-lee/SimpleDeckyTDP> |
| avell-unofficial-control-center | Unofficial control center for Avell laptops on Linux | 289 | <https://github.com/rodgomesc/avell-unofficial-control-center> |
| LenovoController *(archived)* | Lightweight Windows alternative to Lenovo Vantage for Legion laptops | 278 | <https://github.com/ViRb3/LenovoController> |
| MSIKLM | Control the SteelSeries keyboard lighting of MSI gaming laptops on Linux | 255 | <https://github.com/Gibtnix/MSIKLM> |
| AsusFanControl | Small fan control app for ASUS laptops on Windows without Armoury Crate | 254 | <https://github.com/Karmel0x/AsusFanControl> |
| OmenCore | Performance control for HP Omen laptops replacing Omen Gaming Hub | 249 | <https://github.com/theantipopau/omencore> |
| OMEN Space | Command center for HP OMEN and Victus laptops on Linux | 245 | <https://github.com/yunusemreyl/omen-space> |
| Ayuz | Unofficial MyAsus alternative control center for Linux | 235 | <https://github.com/Traciges/Ayuz> |
| hp-omen-linux-module | Linux kernel module for HP Omen keyboard lighting and performance settings | 226 | <https://github.com/pelrun/hp-omen-linux-module> |
| AWCC (Linux) | Unofficial Linux alternative to Alienware Command Center for Dell G series | 201 | <https://github.com/tr1xem/AWCC> |
| asus-wmi-screenpad | asus-wmi kernel module variant with ScreenPad brightness support for ASUS laptops | 182 | <https://github.com/Plippo/asus-wmi-screenpad> |
| gpd-win-tricks | Info and fixes for running Linux on GPD Win devices | 165 | <https://github.com/aarron-lee/gpd-win-tricks> |
| ryzen_smu | Linux kernel driver exposing the AMD Ryzen System Management Unit mailbox to userspace | 152 | <https://github.com/leogx9r/ryzen_smu> |
| clevo-indicator | Ubuntu fan control indicator for Clevo laptops using direct EC access | 148 | <https://github.com/SkyLandTW/clevo-indicator> |
| OmenXHub | Lightweight offline replacement for HP OMEN Gaming Hub | 143 | <https://github.com/MasonDye/OmenXHub> |
| Lecoo-Control-Center | Rust daemon controlling fans, TDP and battery on Lecoo laptops | 141 | <https://github.com/LaVashikk/Lecoo-Control-Center> |
| razer-laptop-control-no-dkms *(archived)* | Userspace Razer Blade fan, power and RGB control on Linux without a kernel module | 137 | <https://github.com/Razer-Linux/razer-laptop-control-no-dkms> |
| akbl *(archived)* | Control Alienware computer lights under GNU/Linux | 132 | <https://github.com/rsm-gh/akbl> |
| omen-fan | Fan control utility for HP Omen laptops on Linux via EC registers | 111 | <https://github.com/alou-S/omen-fan> |
| RLECViewer | Custom fan control for Clevo laptops via the EC | 93 | <https://github.com/zuyan9/RLECViewer> |
| ohman | Lightweight OMEN Gaming Hub alternative with fan curves, modes and GPU power | 83 | <https://github.com/P4R1H/ohman> |
| PowerStation | TDP and performance daemon with DBus interface for x86 handheld gaming PCs | 83 | <https://github.com/ShadowBlip/PowerStation> |
| gigabyte-laptop-wmi | Linux kernel module for Gigabyte AERO/AORUS laptop fan and charge controls | 79 | <https://github.com/tangalbert919/gigabyte-laptop-wmi> |
| HandyGCCS *(archived)* | Linux controller support for handheld PCs (AYANEO, GPD, OneXPlayer, ROG Ally) built-in gamepads | 76 | <https://github.com/ShadowBlip/HandyGCCS> |
| AlienFxLite | Keyboard color management for Alienware laptops (Java with native USB) | 73 | <https://github.com/bchretien/AlienFxLite> |
| LegionGoRemapper | Decky plugin to remap Legion Go buttons and control its controller LEDs on Linux | 72 | <https://github.com/aarron-lee/LegionGoRemapper> |
| allycenter | Decky plugin adding ROG Ally controls and settings to SteamOS | 68 | <https://github.com/PixelAddictUnlocked/allycenter> |
| victus-control | Linux fan control and keyboard lighting for HP Victus/Omen laptops | 61 | <https://github.com/Batuhan4/victus-control> |
| OmenHubLight *(archived)* | Open lightweight substitute for HP Omen Hub programs | 60 | <https://github.com/determ1ne/OmenHubLight> |
| ZenStates-Core | Library for reading and tuning AMD Zen SMU, P-states and memory timings from undocumented interfaces | 60 | <https://github.com/irusanov/ZenStates-Core> |
| omen-rgb-keyboard | Linux kernel driver for HP OMEN laptop RGB keyboard lighting | 55 | <https://github.com/OmenLinux/omen-rgb-keyboard> |
| Zephyrus Control Center | Armoury Crate replacement for ASUS Zephyrus laptops | 50 | <https://github.com/vddCore/Zephyrus-Control-Center> |
| omen-fan-control | HP Omen and Victus fan control CLI and GUI for Linux | 49 | <https://github.com/arfelious/omen-fan-control> |
| OmenHwCtl | HP Omen hardware control via the BIOS WMI interface | 49 | <https://github.com/GeographicCone/OmenHwCtl> |
| tuxedo-backlight-control *(archived)* | CLI and UI for TUXEDO/Clevo keyboard backlight on Linux | 49 | <https://github.com/webketje/tuxedo-backlight-control> |
| MsiFanControl | Fan control utility for MSI laptops | 45 | <https://github.com/kykc/MsiFanControl> |
| openomen | Unofficial Linux driver and daemon for HP OMEN hardware | 44 | <https://github.com/openomen/openomen> |
| g-helper-linux (UdayaSri0) | Open control tool for ASUS laptops and ROG Ally on Linux: modes, fans, lighting | 43 | <https://github.com/UdayaSri0/g-helper-linux> |
| alfc *(archived)* | Fan control with browser UI for the Gigabyte Aorus 15G | 37 | <https://github.com/s-h-a-d-o-w/alfc> |
| ClevoECView | ECView tool to control fans on Clevo laptops | 37 | <https://github.com/SkyLandTW/ClevoECView> |
| gpd-fan-driver | Linux kernel driver for GPD handheld and mini-laptop fan control via the EC | 36 | <https://github.com/Cryolitia/gpd-fan-driver> |
| alienfx-linux | SDK for Alienware lights and fan control on Linux | 32 | <https://github.com/tr1xem/alienfx-linux> |
| clevo-keyboard-backlight *(archived)* | Driver for Clevo backlit keyboards | 31 | <https://github.com/ejcosta/clevo-keyboard-backlight> |
| CppKeyboardColour | CLI RGB keyboard backlight control for Clevo and Tongfang laptops | 31 | <https://github.com/DeviceIoControl/CppKeyboardColour> |
| LeGo2 Fan Control | Unrestricted fan control for the Lenovo Legion Go 2 | 29 | <https://github.com/Rodpad/LeGo2-Fan-Control> |
| alienfx (Aurora) | Control AlienFX lighting on Alienware Aurora desktops under Linux | 27 | <https://github.com/erlkonig/alienfx> |
| Vantage (GTK) | Native GTK4 Lenovo Vantage controls for IdeaPad, Yoga and Legion on Linux | 27 | <https://github.com/kush4gra/Vantage> |
| ayaneo-platform | Linux kernel driver for AYANEO handheld RGB and platform controls via the EC | 24 | <https://github.com/ShadowBlip/ayaneo-platform> |
| clevo-fan-control | Linux fan control service for Clevo laptops | 23 | <https://github.com/agramian/clevo-fan-control> |
| clevo-xsm-wmi | Clevo WMI keyboard backlight driver with CPU/GPU PWM fan control | 21 | <https://github.com/rafaelgieschke/clevo-xsm-wmi> |
| Legion Linux Toolkit | Native Linux power, RGB and fan dashboard for Lenovo Legion laptops | 21 | <https://github.com/armoox/Legion-Linux-Tookit> |
| VFang | Open Razer Blade control center for Linux: fans, power and lighting | 21 | <https://github.com/bladeandsoulx/vfang-razer-linux> |
| pyAlienFX | Multiplatform Python software to control AlienFX devices | 20 | <https://github.com/Xqua/pyAlienFX> |
| ROGueENEMY | ROG Ally userspace driver that merges its gamepad, keyboard and IMU into one virtual controller | 14 | <https://github.com/NeroReflex/ROGueENEMY> |
| ayn-platform | Linux hwmon driver for AYN x86 handhelds: PWM fan control, temperatures and RGB | 9 | <https://github.com/ShadowBlip/ayn-platform> |
| Adjustor *(archived)* | TDP and power control for handheld PCs via ACPI/EC calls, part of Handheld Daemon | 7 | <https://github.com/hhd-dev/adjustor> |
| oxp-sensors | Linux platform driver for OneXPlayer/AOKZOE handheld fan control and EC sensors |  | <https://gitlab.com/Samsagax/oxp-sensors> |
| supergfxctl | GPU switching daemon for ASUS ROG and other hybrid-graphics laptops on Linux |  | <https://gitlab.com/asus-linux/supergfxctl> |

## Headsets, Audio Interfaces & Webcams

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| gopro_as_webcam_on_linux | Use a GoPro as a webcam on Linux via its USB webcam mode | 704 | <https://github.com/jschmid1/gopro_as_webcam_on_linux> |
| OpenSCQ30 | Cross-platform app for Anker Soundcore headphone and earbud settings | 506 | <https://github.com/Oppzippy/OpenSCQ30> |
| OpenFreebuds | Open app for Huawei FreeBuds settings and noise control on Linux and Windows | 454 | <https://github.com/melianmiko/OpenFreebuds> |
| linux-enable-ir-emitter | Enables infrared emitters on laptop IR cameras under Linux by finding the UVC extension control | 367 | <https://github.com/EmixamPP/linux-enable-ir-emitter> |
| elgato-gchd | Reverse engineered Linux userspace driver for the Elgato Game Capture HD | 298 | <https://github.com/tolga9009/elgato-gchd> |
| Linux Arctis Manager | Open replacement for SteelSeries GG to manage Arctis headsets and ChatMix on Linux | 210 | <https://github.com/elegos/Linux-Arctis-Manager> |
| SoundcoreManager | Rust app to control Anker Soundcore headphones over Bluetooth | 183 | <https://github.com/gmallios/SoundcoreManager> |
| macbook12-audio-driver | Linux audio driver for the CS4208 codec in the 12-inch MacBook | 173 | <https://github.com/leifliddy/macbook12-audio-driver> |
| sc0710 | Linux driver for the Elgato 4K60 Pro Mk.2 capture card | 162 | <https://github.com/stoth68000/sc0710> |
| Arctis Sound Manager | SteelSeries GG and Sonar alternative for Arctis headsets on Linux with mixer and EQ | 159 | <https://github.com/loteran/Arctis-Sound-Manager> |
| sc0710 (multi-client) | Multi-client Linux driver for Elgato 4K60 Pro MK.2, 4K Pro and Cam Link Pro capture cards | 147 | <https://github.com/Nakildias/sc0710> |
| PS4 Camera Tools | Tools to load firmware and use the PlayStation 4 camera on PC | 143 | <https://github.com/ps4eye/ps4eye> |
| HyperHeadset | CLI and tray app to monitor and manage HyperX Cloud II and Stinger headsets on Linux/macOS | 126 | <https://github.com/LennardKittner/HyperHeadset> |
| Ozzy | Driver for Ploytec-based USB audio interfaces | 113 | <https://github.com/mischa85/Ozzy> |
| QuadcastRGB | Set RGB lights on HyperX QuadCast S and DuoCast microphones on Linux | 108 | <https://github.com/Ors1mer/QuadcastRGB> |
| MixiD | Unofficial Linux control panel for Audient iD interfaces using a reverse engineered USB protocol | 85 | <https://github.com/TheOnlyJoey/MixiD> |
| arctis-battery-percentage *(archived)* | Shows SteelSeries Arctis wireless headset battery as a notification | 69 | <https://github.com/atagulalan/arctis-battery-percentage> |
| snd-hdspe | New Linux ALSA driver and tools for RME HDSPe MADI, AES and RayDAT sound cards | 68 | <https://github.com/PhilippeBekaert/snd-hdspe> |
| Open Apollo | Clean-room reverse engineered Linux driver for Universal Audio Apollo Thunderbolt interfaces | 67 | <https://github.com/rolotrealanis98/open-apollo> |
| kiyoproctrls | Razer Kiyo Pro webcam controls (HDR, FOV, AF) for Linux via UVC extension units | 66 | <https://github.com/soyersoyer/kiyoproctrls> |
| ggoled | OLED integration for the SteelSeries Arctis Nova Pro base station without GG | 55 | <https://github.com/JerwuQu/ggoled> |
| HyperX-Cloud-2-Battery-Monitor | Battery monitor for HyperX Cloud II, III and Alpha wireless headsets | 54 | <https://github.com/auto94/HyperX-Cloud-2-Battery-Monitor> |
| nova-chatmix-linux | ChatMix support for the SteelSeries Arctis Nova Pro Wireless on Linux | 51 | <https://github.com/Dymstro/nova-chatmix-linux> |
| hyperx-cloud-flight-wireless | Reverse engineered Node module for HyperX Cloud Flight Wireless battery and mute events | 46 | <https://github.com/srn/hyperx-cloud-flight-wireless> |
| sonar-rev | Reverse engineering notes and client for the SteelSeries GG Sonar local API | 46 | <https://github.com/wex/sonar-rev> |
| hyperx-cloud-flight | Tray app showing battery level of the HyperX Cloud Flight Wireless headset on Linux | 42 | <https://github.com/kondinskis/hyperx-cloud-flight> |
| soundblaster-x-g6-cli | Python CLI to control the Creative Sound BlasterX G6 DAC settings on Linux | 33 | <https://github.com/nils-skowasch/soundblaster-x-g6-cli> |
| Linux-Arctis-7-Plus-ChatMix | ChatMix workaround for the SteelSeries Arctis 7+ on Linux without GG | 26 | <https://github.com/awth13/Linux-Arctis-7-Plus-ChatMix> |
| steelseries-wireless-battery-tray | Tray app showing battery of SteelSeries wireless headsets | 21 | <https://github.com/mtadin/steelseries-wireless-battery-tray> |
| corsair-void-driver | Linux kernel driver for Corsair Void headsets: battery, sidetone, mic status (upstreamed 6.13) | 6 | <https://github.com/stuarthayhurst/corsair-void-driver> |
| hyperx-cloud-II-battery | Reads HyperX Cloud II wireless headset battery level over hidraw | 6 | <https://github.com/Agustin-Jerusalinsky/hyperx-cloud-II-battery> |

## Lab Instruments & Thermal Cameras

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| stlink | Open source STM32 programming toolset for ST-Link debug probes | 5,190 | <https://github.com/stlink-org/stlink> |
| openFPGALoader | Universal FPGA programmer supporting many vendor JTAG cables and boards | 1,753 | <https://github.com/trabucayre/openFPGALoader> |
| OpenHantek6022 | DSO software for Hantek 6022BE/BL USB oscilloscopes with open firmware | 1,123 | <https://github.com/OpenHantek/OpenHantek6022> |
| OpenHantek | DSO software for Hantek, Voltcraft and similar USB oscilloscopes | 830 | <https://github.com/OpenHantek/openhantek> |
| libsigrok | Signal analysis library with drivers for many logic analyzers, scopes and meters | 443 | <https://github.com/sigrokproject/libsigrok> |
| ch341prog | Open SPI/I2C flash programmer for the CH341A USB adapter | 422 | <https://github.com/setarcos/ch341prog> |
| libseek-thermal | Linux driver for Seek Thermal Compact, CompactXR and CompactPRO cameras | 344 | <https://github.com/OpenThermal/libseek-thermal> |
| PyThermalCamera | Python software for the Topdon TC001 thermal camera on Linux and Raspberry Pi | 325 | <https://github.com/leswright1977/PyThermalCamera> |
| OWON-VDS1022 | Unofficial improved software release for the OWON VDS1022/I USB oscilloscope | 306 | <https://github.com/florentbr/OWON-VDS1022> |
| rd-usb | Web GUI for RuiDeng/Riden USB testers (UM34C, UM24C, UM25C, TC66C) | 276 | <https://github.com/kolinger/rd-usb> |
| P2Pro-Viewer | Viewer and API for the InfiRay P2 Pro thermal camera with a reverse engineered protocol | 256 | <https://github.com/LeoDJ/P2Pro-Viewer> |
| ppk2-api-python | Unofficial Python API for the Nordic Power Profiler Kit II | 255 | <https://github.com/IRNAS/ppk2-api-python> |
| fnirsi-usb-power-data-logger | Data logger for FNIRSI FNB48, C1 and FNB58 USB power meters | 244 | <https://github.com/baryluk/fnirsi-usb-power-data-logger> |
| AWG_DHO8-900 | Arbitrary waveform generator add-on for Rigol DHO800/DHO900 oscilloscopes | 216 | <https://github.com/MatthiasElectronic/AWG_DHO8-900> |
| UT210E | Reverse engineered information and data-logging for the UNI-T UT210E clamp meter | 200 | <https://github.com/af3556/UT210E> |
| FNIRSI-1013D-1014D-Hack | Reverse engineering resources and firmware for FNIRSI 1013D/1014D scopes | 155 | <https://github.com/pecostm32/FNIRSI-1013D-1014D-Hack> |
| rusty_meter | Rust app to operate OWON XDM and Victor bench multimeters without vendor software | 143 | <https://github.com/markusdd/rusty_meter> |
| Hantek6022API | Python API for the Hantek 6022BE USB scope, reverse engineered from USB traces | 137 | <https://github.com/rpcope1/Hantek6022API> |
| qrigol | Qt assistant for Rigol DS1000 series scopes over USB | 134 | <https://github.com/wd5gnr/qrigol> |
| Thermal-Camera-Redux | Topdon TC001 and clone thermal camera app for live and offline radiometric data | 131 | <https://github.com/92es/Thermal-Camera-Redux> |
| rd6006 | Python module to control Riden RD6006 programmable power supplies | 118 | <https://github.com/Baldanos/rd6006> |
| OpenScope-2C53T | Reverse engineering and open firmware for the FNIRSI 2C53T scope/multimeter | 116 | <https://github.com/DavidClawson/OpenScope-2C53T> |
| flirone-v4l2 | V4L2 bridge to use the FLIR One thermal camera on Linux | 111 | <https://github.com/fnoop/flirone-v4l2> |
| sds1004x_bode | Emulates a Siglent AWG so SDS1004X-E scopes can do Bode plots with third-party generators | 97 | <https://github.com/4x1md/sds1004x_bode> |
| ht301_hacklib | OpenCV library for the Hti HT-301 and similar USB thermal cameras with raw temperature data | 87 | <https://github.com/stawel/ht301_hacklib> |
| seek-thermal-documentation | Unofficial documentation of the Seek Thermal USB protocol | 83 | <https://github.com/lod/seek-thermal-documentation> |
| UNI-T-Thermal-Utilities | Extracts raw temperature data from UNI-T thermal camera images | 80 | <https://github.com/Santi-hr/UNI-T-Thermal-Utilities> |
| libseek | libusb-based API for the Seek Thermal imager | 76 | <https://github.com/zougloub/libseek> |
| Dokit | Cross-platform library and apps for Pokit Bluetooth measuring devices | 75 | <https://github.com/pcolby/dokit> |
| Riden | Python library for Riden RD series power supplies | 74 | <https://github.com/ShayBox/Riden> |
| thermal-cat | Cross-platform viewer app for the InfiRay P2 Pro thermal camera | 74 | <https://github.com/alufers/thermal-cat> |
| lnDSO150 | Alternative firmware for the DSO150 shell oscilloscope | 67 | <https://github.com/mean00/lnDSO150> |
| HP34401a-OLED-FW | OLED display mod firmware for the HP 34401A multimeter | 66 | <https://github.com/openscopeproject/HP34401a-OLED-FW> |
| 121gw-re | Reverse engineering the EEVblog 121GW multimeter | 64 | <https://github.com/tpwrules/121gw-re> |
| libseekthermal | Driver library for Seek Thermal imaging devices | 63 | <https://github.com/ethz-asl/libseekthermal> |
| fx2lafw | Open firmware for Cypress FX2 logic analyzers, replacing vendor firmware | 61 | <https://github.com/sigrokproject/sigrok-firmware-fx2lafw> |
| sds7102 | Port of Linux to the OWON SDS7102 oscilloscope | 57 | <https://github.com/wingel/sds7102> |
| unit_ut61eplus | Python access to the UNI-T UT61E+ multimeter via its CP2110 USB interface | 56 | <https://github.com/ljakob/unit_ut61eplus> |
| owowon | Oscilloscope UI for OWON HDS portable scopes over USB | 51 | <https://github.com/seritools/owowon> |
| Bluetooth-DMM | Protocol analysis of Aneng, ZOYI and BSIDE Bluetooth multimeters | 50 | <https://github.com/ludwich66/Bluetooth-DMM> |
| um34c | NodeJS tool to read and control UM34C/UM24C/UM25C USB testers over Bluetooth | 50 | <https://github.com/sebastianha/um34c> |
| 360nosc0pe | Open FPGA bitstreams for Siglent SDS1x0xX-E oscilloscopes | 49 | <https://github.com/360nosc0pe/scope> |
| ParksideView | Reads data from Parkside PDM-300-C2/C3 multimeters | 45 | <https://github.com/bmuessig/ParksideView> |
| SeekOFix | Windows software for Seek Thermal cameras independent of the vendor app | 42 | <https://github.com/frenkinet/SeekOFix> |
| Owon-Multimeters | Linux support for OWON Bluetooth multimeters (B35T+, B41T+, CM2100B, OW18E) | 41 | <https://github.com/sercona/Owon-Multimeters> |
| owon-sds7102-protocol | GNU/Linux software suite for OWON oscilloscopes over USB | 38 | <https://github.com/bjonnh/owon-sds7102-protocol> |
| tg165-tools | Tools for hacking on and reflashing the FLIR TG165 thermal camera | 37 | <https://github.com/ktemkin/tg165-tools> |
| owonb35 | Bluetooth client for the OWON B35 multimeter | 36 | <https://github.com/DeanCording/owonb35> |
| p2pro-live | Web app for a live radiometric stream from the InfiRay P2 Pro thermal camera | 36 | <https://github.com/ks00x/p2pro-live> |
| espBode | ESP bridge between a Siglent oscilloscope and an FY6800 AWG for Bode plots | 32 | <https://github.com/sq6sfo/espBode> |
| Owon-VDS1022 (OS X) | Run the OWON VDS1022 USB oscilloscope on macOS and Linux | 31 | <https://github.com/tinwhisker/Owon-VDS1022> |
| DSO5102P-Python | Python access to the Hantek DSO5102P oscilloscope | 27 | <https://github.com/titos-carrasco/DSO5102P-Python> |
| BK-390A | CLI data capture for BK Precision 390A series multimeters | 26 | <https://github.com/inflex/BK-390A> |
| InfiRayCapture | macOS app for viewing InfiRay P2 Pro thermal camera streams | 25 | <https://github.com/atomic14/InfiRayCapture> |
| siglent-bin2sr | Converts Siglent SDS1000X-E waveform binaries to sigrok srzip | 25 | <https://github.com/geekman/siglent-bin2sr> |
| yombir | Native C++ app for Topdon TC-001 and InfiRay P2 thermal cameras | 24 | <https://github.com/yomboprime/yombir> |
| owoncontrol-qt | Qt USB interface for OWON oscilloscopes | 23 | <https://github.com/7oxicshadow/owoncontrol-qt> |
| hantek1008py | Python driver for the Hantek 1008 USB oscilloscope | 22 | <https://github.com/mfg92/hantek1008py> |
| FlirOneControlForLinux | Qt5 libusb app to use the FLIR One thermal camera on Linux | 21 | <https://github.com/da-nie/FlirOneControlForLinux> |
| fx2adc | Use Cypress FX2-based USB oscilloscopes (Hantek) as general purpose ADCs | 21 | <https://github.com/steve-m/fx2adc> |
| Hantek 2D72 tool | Linux tool for the Hantek 2D72 handheld oscilloscope | 20 | <https://github.com/lucaoli/Hantek> |
| pyseek | Python interface for the Seek Thermal camera | 20 | <https://github.com/Fry-kun/pyseek> |
| dmm_util | Utility for Fluke 287/289 multimeters: readings, memory and settings | 19 | <https://github.com/N0ury/dmm_util> |
| hantek-365 | Open GUI and CLI for the Hantek 365 data logger | 19 | <https://github.com/mp035/hantek-365> |
| HT6022_Driver | libusb-1.0 based driver for the Hantek 6022 scope | 19 | <https://github.com/rpm2003rpm/HT6022_Driver> |
| ow | macOS and iOS tools for OWON oscilloscopes | 19 | <https://github.com/bbum/ow> |
| infiray_irg | Python module to read InfiRay C200/P200 IRG thermal image files | 18 | <https://github.com/jaseg/infiray_irg> |
| dmm-tools | Multimeter logging and graphing for UNI-T, ZOYI and other meters on Linux, Windows, macOS | 17 | <https://github.com/antoinecellerier/dmm-tools> |
| idso1070-protocol *(archived)* | Reverse engineered protocol for the Hantek iDSO1070 Wi-Fi oscilloscope | 17 | <https://github.com/hhornbacher/idso1070-protocol> |
| OpenP3 | Unofficial Linux driver for the Thermal Master P3 thermal camera | 17 | <https://github.com/Phalphy/OpenP3> |
| victor70c | Victor 70C multimeter software for Linux | 17 | <https://github.com/mvneves/victor70c> |
| owon_hds200 | Python interface to OWON HDS200 handheld oscilloscopes | 16 | <https://github.com/qwindelzorf/owon_hds200> |

## Laptop EC & Peripherals

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| MonitorControl | macOS app to control external display brightness over DDC | 34,439 | <https://github.com/MonitorControl/MonitorControl> |
| G-Helper | Lightweight open replacement for ASUS Armoury Crate laptop control | 15,531 | <https://github.com/seerge/g-helper> |
| LibreHardwareMonitor | Hardware sensor monitor with reverse-engineered Super I/O and EC readers | 9,183 | <https://github.com/LibreHardwareMonitor/LibreHardwareMonitor> |
| linux-surface | Linux kernel and drivers for Microsoft Surface devices | 7,781 | <https://github.com/linux-surface/linux-surface> |
| Lunar | macOS display brightness controller using DDC and private display APIs | 5,717 | <https://github.com/alin23/Lunar> |
| throttled | Linux daemon working around Intel firmware-induced throttling on Lenovo and other laptops | 2,988 | <https://github.com/erpalma/throttled> |
| RyzenAdj | Adjust power settings of Ryzen mobile processors via undocumented SMU calls | 2,437 | <https://github.com/FlyGoat/RyzenAdj> |
| ddcutil | Query and change monitor settings over DDC/CI and USB MCCS on Linux | 1,415 | <https://github.com/rockowitz/ddcutil> |
| intel-undervolt | Undervolting and power-limit tool for Intel CPUs using undocumented MSRs | 1,094 | <https://github.com/kitsunyan/intel-undervolt> |
| nbfc-linux | C port of NoteBook FanControl for Linux using per-model EC register configs | 786 | <https://github.com/nbfc-linux/nbfc-linux> |
| m1ddc | CLI to control external displays via DDC on Apple Silicon Macs | 741 | <https://github.com/waydabber/m1ddc> |
| ddccontrol | Linux DDC/CI monitor control tool with GUI and monitor database | 726 | <https://github.com/ddccontrol/ddccontrol> |
| thinkfan | Fan control daemon for ThinkPads and other hwmon systems | 717 | <https://github.com/vmatare/thinkfan> |
| acer-predator-turbo-and-rgb-keyboard-linux-module | Linux module for Acer Predator turbo mode and RGB keyboard | 632 | <https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module> |
| it87 | Linux driver for ITE Super I/O hardware monitoring chips | 613 | <https://github.com/frankcrawford/it87> |
| ZenStates-Linux | Tool to change AMD Zen P-states via MSRs on Linux | 569 | <https://github.com/r4m0n/ZenStates-Linux> |
| chromebook-linux-audio | Script that enables audio on many Chromebooks running mainstream Linux distributions | 551 | <https://github.com/WeirdTreeThing/chromebook-linux-audio> |
| snd_hda_macbookpro | Linux audio driver for Cirrus codecs in Intel MacBook Pros | 500 | <https://github.com/davidjo/snd_hda_macbookpro> |
| msi-ec | Linux kernel driver for MSI laptop EC features (fans, battery, LEDs) | 494 | <https://github.com/BeardOverflow/msi-ec> |
| SMUDebugTool | Windows tool to inspect AMD SMU, PCI and MSR registers | 489 | <https://github.com/irusanov/SMUDebugTool> |
| zenpower | Linux hwmon driver for AMD Zen CPU sensors | 489 | <https://github.com/ocerman/zenpower> |
| nct6687d | Linux driver for Nuvoton NCT6687-R Super I/O sensors | 474 | <https://github.com/Fred78290/nct6687d> |
| fw-fanctrl | Fan curve service for Framework laptops using the EC via ectool | 464 | <https://github.com/TamtamHero/fw-fanctrl> |
| tpacpi-bat | ThinkPad battery charge threshold control via undocumented ACPI calls | 454 | <https://github.com/teleshoes/tpacpi-bat> |
| isw (Ice-Sealed Wyvern) | Fan control for MSI laptops via the embedded controller | 414 | <https://github.com/YoyPa/isw> |
| Huawei-WMI | Linux WMI driver for Huawei MateBook hotkeys, battery protection and fn-lock | 285 | <https://github.com/aymanbagabas/Huawei-WMI> |
| samsung-galaxybook-extras | Linux platform driver for Samsung Galaxy Book fan, keyboard backlight and performance modes | 281 | <https://github.com/joshuagrisham/samsung-galaxybook-extras> |
| asus-wmi-sensors | Linux hwmon driver for ASUS Ryzen/Threadripper motherboard sensors via WMI | 263 | <https://github.com/electrified/asus-wmi-sensors> |
| ddcui | Qt graphical front end for ddcutil monitor control | 263 | <https://github.com/rockowitz/ddcui> |
| dell-bios-fan-control | Toggle Dell BIOS fan control via undocumented SMM calls | 258 | <https://github.com/TomFreudenberg/dell-bios-fan-control> |
| monitorcontrol (Python) | Python library for monitor control via DDC/CI on Linux and Windows | 244 | <https://github.com/newAM/monitorcontrol> |
| i8kutils | Fan and SMM utilities for Dell laptops | 235 | <https://github.com/vitorafsr/i8kutils> |
| galaxy-book2-pro-linux | Notes and utilities for Linux on the Samsung Galaxy Book2 Pro | 194 | <https://github.com/joshuagrisham/galaxy-book2-pro-linux> |
| zcfan | Zero-configuration fan daemon for ThinkPads via thinkpad_acpi | 165 | <https://github.com/cdown/zcfan> |
| samsung-galaxy-book-linux-fixes | Linux fixes for Samsung Galaxy Book 3/4/5 webcam, speakers and microphone | 160 | <https://github.com/Andycodeman/samsung-galaxy-book-linux-fixes> |
| iptsd | Userspace daemon for Intel Precise Touch & Stylus on Surface devices | 152 | <https://github.com/linux-surface/iptsd> |
| framework-laptop-kmod | Linux kernel module exposing Framework laptop EC features (fans, LEDs, battery) | 148 | <https://github.com/DHowett/framework-laptop-kmod> |
| framework-system | Rust tool and library to talk to the Framework laptop EC and peripherals | 147 | <https://github.com/FrameworkComputer/framework-system> |
| cros-keyboard-map | Generates keyd configs so Chromebook top-row keys work under normal Linux distros | 138 | <https://github.com/WeirdTreeThing/cros-keyboard-map> |
| mbp2018-bridge-drv | Reverse engineered Apple T2 BCE driver for keyboard, trackpad and audio on 2018+ MacBooks | 138 | <https://github.com/MCMrARM/mbp2018-bridge-drv> |
| Reverse_Engineering_BQ20z70_Laptop_BMS | Reverse engineering the BQ20z70 laptop battery management system | 132 | <https://github.com/omarKmekkawy/Reverse_Engineering_BQ20z70_Laptop_BMS> |
| zenbook-duo-2024-linux | Linux support for the ASUS Zenbook Duo 2024 dual screens, keyboard backlight and battery limit | 127 | <https://github.com/alesya-h/zenbook-duo-2024-ux8406ma-linux> |
| tiny-dfr | Minimal dynamic function row daemon for the MacBook Touch Bar on Linux | 121 | <https://github.com/AsahiLinux/tiny-dfr> |
| dell-powermanager | Cross-platform Dell Power Manager reimplementation | 115 | <https://github.com/alexVinarskis/dell-powermanager> |
| surface-aggregator-module | Linux drivers for the Microsoft Surface System Aggregator Module embedded controller | 106 | <https://github.com/linux-surface/surface-aggregator-module> |
| asus-fan *(archived)* | Linux kernel module to read and set fan speeds on ASUS Zenbooks | 97 | <https://github.com/daringer/asus-fan> |
| Open-Source-PC110 | Reconstructing the missing technical documentation of the IBM PC110 palmtop | 97 | <https://github.com/ahmadexp/Open-Source-PC110> |
| IdeapadToolkit | Lightweight Lenovo Vantage alternative for the IdeaPad Flex 5 | 91 | <https://github.com/havlif/IdeapadToolkit> |
| qnap8528 | Linux kernel module exposing the ITE8528 embedded controller on QNAP devices | 91 | <https://github.com/0xGiddi/qnap8528> |
| Framework EC (DHowett) | Framework Laptop embedded controller firmware fork with ectool used by fan-control tools | 88 | <https://github.com/DHowett/framework-ec> |
| surface-control | CLI to control Surface performance mode, dGPU power and clipboard detach on Linux | 83 | <https://github.com/linux-surface/surface-control> |
| asus-ec-sensors | Linux hwmon driver reading ASUS motherboard sensors from the embedded controller | 78 | <https://github.com/zeule/asus-ec-sensors> |
| Galaxy-Book4-Edge-linux | Linux driver and RE tools for the Samsung Galaxy Book4 Edge | 76 | <https://github.com/Saddytech/Galaxy-Book4-Edge-linux> |
| predator-sense | Unofficial Linux hardware control for Acer Predator/Helios/Nitro laptops | 71 | <https://github.com/cleyton1986/predator-sense> |
| yogabook-c930-linux-eink-driver | Reverse engineered Linux driver for the Lenovo Yoga Book C930 e-ink keyboard | 70 | <https://github.com/aleksb/yogabook-c930-linux-eink-driver> |
| turbomem | Linux driver for the Intel Turbo Memory Controller PCIe card | 60 | <https://github.com/yarrick/turbomem> |
| GhostDeck | Driver-free power and fan control for MSI laptops via EC/WMI | 58 | <https://github.com/wygodad/ghostdeck> |
| init-headphone | Initializes the headphone amplifier found in some Clevo laptops on Linux | 57 | <https://github.com/Unrud/init-headphone> |
| HallMonitor | Clean-room Galaxy S4 View Cover driver | 45 | <https://github.com/durka/HallMonitor> |
| surface-dtx-daemon | Userspace daemon for the Surface Book detachment (DTX) system on Linux | 45 | <https://github.com/linux-surface/surface-dtx-daemon> |
| qc71_laptop | Linux driver for QC71-based (Tongfang/XMG/Eluktronics) laptop EC features | 40 | <https://github.com/pobrn/qc71_laptop> |
| MsiEcRamEditor | Edit and dump MSI laptop EC RAM via ACPI-WMI | 25 | <https://github.com/timschneeb/MsiEcRamEditor> |
| OpenInputBridge | Clean-room, protocol-compatible reimplementation of the Interception keyboard/mouse driver | 25 | <https://github.com/Applet-LLC/OpenInputBridge> |
| t2-better-audio | Audio configuration files for Apple T2 Macs running Linux | 18 | <https://github.com/kekrby/t2-better-audio> |
| asus-fan-control-ec | Fan control for ASUS devices on Linux via direct EC access | 14 | <https://github.com/Keyitdev/asus-fan-control-ec> |
| gigactl | Fan and RGB keyboard control for Gigabyte/Clevo laptops on Linux, reverse-engineered | 7 | <https://github.com/smairio/gigactl> |
| TPFanCtrl2 | ThinkPad fan control for Windows 10/11 | 6 | <https://github.com/mews-se/TPFanCtrl2> |
| Mechrevo-Xingyao-14 | Reverse-engineering reference for an Insyde BIOS and ITE EC laptop | 5 | <https://github.com/YMGPwcca/Mechrevo-Xingyao-14> |
| asusctl | Control daemon for ASUS ROG/TUF laptops on Linux (fans, LEDs, profiles) |  | <https://gitlab.com/asus-linux/asusctl> |

## Printers, Scanners & Fingerprint

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| python-validity | Reverse-engineered Validity/Synaptics fingerprint sensor driver for ThinkPads | 1,245 | <https://github.com/uunicorn/python-validity> |
| catprinter | Prints to cheap BLE "cat" thermal printers via reverse-engineered protocol | 859 | <https://github.com/rbaron/catprinter> |
| brlaser | Open driver for Brother laser printers that lack PostScript support | 719 | <https://github.com/pdewacht/brlaser> |
| sane-airscan | SANE backend for driverless eSCL and WSD network scanners | 371 | <https://github.com/alexpevzner/sane-airscan> |
| goodix-fp-dump | Reverse-engineering tools and prototype drivers for Goodix fingerprint sensors | 360 | <https://github.com/goodix-fp-linux-dev/goodix-fp-dump> |
| Epson-Waste-Reset | Open-source utility to reset Epson printer waste ink pad counters | 353 | <https://github.com/RxNaison/Epson-Waste-Reset> |
| node-hp-scan-to | Enables HP All-in-One scan-to-computer without HP software | 304 | <https://github.com/manuc66/node-hp-scan-to> |
| Validity91 | Reverse engineering the Validity 138a:0091 fingerprint sensor in Dell XPS laptops | 241 | <https://github.com/hmaarrfk/Validity91> |
| labelle | Open print tool for Dymo LabelManager label printers | 189 | <https://github.com/labelle-org/labelle> |
| hp-laser-1008a-macos | Native Apple Silicon macOS driver for HP Laser 1003-1008 printers | 174 | <https://github.com/Kuberwastaken/hp-laser-1008a-macos> |
| libfprint elan | libfprint driver for Elantech fingerprint sensors | 161 | <https://github.com/iafilatov/libfprint> |
| synaTudor | Linux libfprint driver for Synaptics Tudor match-in-sensor fingerprint readers | 152 | <https://github.com/Popax21/synaTudor> |
| Goodix92 *(archived)* | Reverse engineering the Goodix 27c6:5395 fingerprint sensor in Dell XPS 9570 | 104 | <https://github.com/IDerr/Goodix92> |
| brother-in-arms | Brother printer drivers for ARM and Raspberry Pi | 80 | <https://github.com/alexivkin/brother-in-arms> |
| open-fprintd | fprintd replacement allowing standalone backends such as python-validity | 79 | <https://github.com/uunicorn/open-fprintd> |
| ql570 | Linux program for Brother QL-570/QL-700 label printers | 62 | <https://github.com/sudomesh/ql570> |
| SpliX | CUPS driver for Samsung/Xerox SPL host-based laser printers | 51 | <https://github.com/OpenPrinting/splix> |
| CatPrinterBLE | Implementation of the MXW01 cat thermal printer BLE protocol | 49 | <https://github.com/MaikelChan/CatPrinterBLE> |
| PTouchHH | Brother P-Touch label printer reverse engineering and firmware work | 46 | <https://github.com/furrtek/PTouchHH> |
| fingerprint-ocv | Linux driver for the FPC 10a5:9201 fingerprint sensor controller | 42 | <https://github.com/vrolife/fingerprint-ocv> |
| goodix-fingerprint-reversing | Notes and tools from reverse engineering the Goodix 5110 fingerprint reader | 39 | <https://github.com/tlambertz/goodix-fingerprint-reversing> |
| goodix53x5-libfprint | libfprint driver for the Goodix 27c6:5385 fingerprint sensor in the Dell XPS 13 7390 | 38 | <https://github.com/AndyHazz/goodix53x5-libfprint> |
| elanpoc | Proof of concept for talking to ELAN 04f3:0c4c fingerprint readers, basis for a libfprint driver | 35 | <https://github.com/depau/elanpoc> |
| niimbot-web-bluetooth | Web Bluetooth driver and reverse-engineered protocol docs for Niimbot label printers | 34 | <https://github.com/iscarelli/niimbot-web-bluetooth> |
| ft9201-libfprint | libfprint driver for the FocalTech FT9201 (2808:93a9) USB fingerprint reader | 26 | <https://github.com/OMGrant/ft9201-libfprint> |
| linux-fingerprint-drivers | Community hub of drivers and patches for fingerprint sensors not in libfprint | 13 | <https://github.com/jedbillyb/linux-fingerprint-drivers> |
| dell-controlvault2-fingerprint-linux | Linux driver for Dell ControlVault2 / Broadcom BCM5880 fingerprint chip | 12 | <https://github.com/grosa787/dell-controlvault2-fingerprint-linux> |
| synaTudorMiS | Development of the synatlsmoc libfprint driver for Synaptics sensors | 9 | <https://github.com/vojtapl/synaTudorMiS> |
| libfprint-egis0576 | Reverse-engineered libfprint driver for EgisTec EH576 fingerprint sensor | 7 | <https://github.com/PHILIPPDEV5396/libfprint-egis0576> |
| synaptics-00e7-fpdrv | From-scratch userspace driver for Synaptics 06cb:00e7 match-on-chip sensor | 7 | <https://github.com/HansHoogerwerf/synaptics-00e7-fpdrv> |
| goodix-spi-protocol | Goodix fingerprint scanner SPI protocol tools | 6 | <https://github.com/egormanga/goodix-spi-protocol> |
| goodix51c0_spi-reversing | Protocol reverse engineering of the Goodix 51C0 SPI fingerprint sensor | 6 | <https://github.com/lexakimov/goodix51c0_spi-reversing> |
| foo2zjs | Reverse-engineered drivers for ZjStream and other host-based "GDI" laser printers |  | <https://foo2zjs.rkkda.com> |
| libfprint | Open fingerprint reader library with many reverse-engineered sensor drivers |  | <https://gitlab.freedesktop.org/libfprint/libfprint> |
| SANE backends | SANE scanner backends, many written from reverse-engineered scanner protocols |  | <https://gitlab.com/sane-project/backends> |

## Wi-Fi & Radios

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| rtl-sdr | Turns RTL2832U DVB-T dongles into SDR receivers via reverse-engineered debug mode | 994 | <https://github.com/osmocom/rtl-sdr> |
| esp32-open-mac | Reverse-engineered open-source Wi-Fi MAC layer for the ESP32 | 855 | <https://github.com/esp32-open-mac/esp32-open-mac> |
| Hamlib | Ham radio control library for rigs, rotators and amplifiers using vendor CAT protocols | 851 | <https://github.com/Hamlib/Hamlib> |
| CHIRP | Programming tool for many handheld and mobile radios using reverse engineered cloning protocols | 591 | <https://github.com/kk7ds/chirp> |
| open-ath9k-htc-firmware | Fully open firmware for Atheros AR9271/AR7010 USB Wi-Fi chips | 484 | <https://github.com/qca/open-ath9k-htc-firmware> |
| nexmon_csi | Extract Wi-Fi channel state information from Broadcom chips via Nexmon firmware patches | 475 | <https://github.com/seemoo-lab/nexmon_csi> |
| qdmr | GUI to configure and program cheap DMR radios on Linux and macOS | 356 | <https://github.com/hmatuschek/qdmr> |
| OsmocomBB | Free GSM baseband firmware for Calypso-based phones built by reverse engineering | 333 | <https://github.com/osmocom/osmocom-bb> |
| dmrconfig | Configuration utility for DMR radios (TYT, Baofeng, Radioddity) with reverse engineered protocols | 286 | <https://github.com/OpenRTX/dmrconfig> |
| bl602-re | Reverse engineering of the BL602 Wi-Fi/BLE binary blobs | 105 | <https://github.com/pine64/bl602-re> |
| ESP32-Bluetooth-Reversing | Reverse engineering of the ESP32 Bluetooth controller | 88 | <https://github.com/TarlogicSecurity/ESP32-Bluetooth-Reversing> |
| libmirisdr-4 | Open driver for Mirics MSi001/MSi2500 SDR dongles (SDRplay-type) | 86 | <https://github.com/f4exb/libmirisdr-4> |
| bcm-public | SEEMOO Broadcom Wi-Fi firmware analysis and patching resources | 79 | <https://github.com/seemoo-lab/bcm-public> |
| Inside-EZRadioPRO | Reverse engineering the Silabs EZRadioPRO sub-GHz radios | 77 | <https://github.com/astuder/Inside-EZRadioPRO> |
| osmo-fl2k | Uses FL2000 USB-to-VGA adapters as cheap SDR transmitters | 58 | <https://github.com/osmocom/osmo-fl2k> |
| b43-tools | b43 firmware tools: fwcutter, assembler and disassembler for Broadcom Wi-Fi microcode | 39 | <https://github.com/mbuesch/b43-tools> |
