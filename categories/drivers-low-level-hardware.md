# Drivers & Low-level Hardware

[← All categories](../README.md#whats-inside) · [Search this category on the website](https://alexgaoth.github.io/awesome-reverse-engineered/#c=drivers-low-level-hardware) · 442 projects · [Listed here? Get the badge](../README.md#is-your-project-listed)

Health: 🟢 pushed in the last year · 🟡 1 to 3 years · 🔴 over 3 years · 🗄️ archived · ⚪ unknown

- [Apple Silicon (Asahi)](#apple-silicon-asahi) (19)
- [Drawing Tablets & Input](#drawing-tablets--input) (16)
- [Firmware/BIOS (coreboot, UEFI)](#firmwarebios-coreboot-uefi) (21)
- [GPU Drivers](#gpu-drivers) (35)
- [Gaming Laptops & Handheld PCs](#gaming-laptops--handheld-pcs) (83)
- [Headsets, Audio Interfaces & Webcams](#headsets-audio-interfaces--webcams) (41)
- [Lab Instruments & Thermal Cameras](#lab-instruments--thermal-cameras) (84)
- [Laptop EC & Peripherals](#laptop-ec--peripherals) (82)
- [Printers, Scanners & Fingerprint](#printers-scanners--fingerprint) (40)
- [Wi-Fi & Radios](#wi-fi--radios) (21)

## Apple Silicon (Asahi)

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [tinygrad](https://github.com/tinygrad/tinygrad) | ML framework whose extra/accel/ane holds reverse-engineered Apple Neural Engine work | 33,785 | 🟢 | Python |
| [neural-engine](https://github.com/hollance/neural-engine) | Community documentation of the Apple Neural Engine and how Core ML uses it | 2,547 | 🟢 |  |
| [muvm](https://github.com/AsahiLinux/muvm) | microVM runner used by Asahi to run x86 games with FEX on 4K-page hosts | 983 | 🟢 | Rust |
| [linux-m1](https://github.com/corellium/linux-m1) | Linux kernel source tree | 871 | 🔴 | C |
| [ane (Linux ANE driver)](https://github.com/eiln/ane) | Reverse-engineered Linux driver and userspace for the Apple Neural Engine | 541 | 🟡 | C |
| [macvdmtool](https://github.com/AsahiLinux/macvdmtool) | Tool to send Apple USB-PD vendor-defined messages (serial/reboot) between Macs | 378 | 🟢 | C++ |
| [asahi-audio](https://github.com/AsahiLinux/asahi-audio) | DSP and audio configuration for Apple Silicon Macs on Linux | 216 | 🟢 | Makefile |
| [speakersafetyd](https://github.com/AsahiLinux/speakersafetyd) | Userspace speaker protection daemon for Apple Silicon Macs under Linux | 206 | 🟢 | Rust |
| [Asahi U-Boot](https://github.com/AsahiLinux/u-boot) | U-Boot port for Apple Silicon Macs used in the Asahi boot chain | 201 | 🟢 | C |
| [avd](https://github.com/eiln/avd) | Reverse-engineered Apple Video Decoder (AVD) driver work for Linux | 183 | 🟡 | C |
| [linux-t2-patches](https://github.com/t2linux/linux-t2-patches) | Linux patches for T2-chip Intel Macs (keyboard, touchbar, audio, BCE) | 103 | 🟢 |  |
| [apple-bce-drv](https://github.com/t2linux/apple-bce-drv) | Reverse-engineered Linux driver for the Apple T2 Bridge Controller (BCE) | 101 | 🟢 | C |
| [asahi-nvram](https://github.com/AsahiLinux/asahi-nvram) | Tools to read and write Apple Silicon NVRAM from Linux | 77 | 🟢 | Rust |
| [anecc](https://github.com/eiln/anecc) | Run CoreML models on the Apple Neural Engine under Asahi Linux | 62 | 🔴 | Python |
| [coreml_to_ane_hwx](https://github.com/freedomtan/coreml_to_ane_hwx) | Converts Core ML models to Apple Neural Engine HWX binaries for analysis | 53 | 🟢 | Objective-C |
| [asahi-scripts](https://github.com/AsahiLinux/asahi-scripts) | Asahi Linux support scripts (firmware extraction, boot setup) | 50 | 🟢 | Shell |
| [mdaiter/ane](https://github.com/mdaiter/ane) | Reverse-engineering artifacts for Apple ANECompiler, Espresso and AppleNeuralEngine | 40 | 🟢 | Python |
| [m1-pmu-gen](https://github.com/cyyself/m1-pmu-gen) | Generates Linux perf event tables for Apple Silicon PMU counters | 20 | 🟢 | Python |
| [alsa-ucm-conf-asahi](https://github.com/AsahiLinux/alsa-ucm-conf-asahi) | ALSA UCM configuration for Apple Silicon audio hardware | 7 | 🟢 |  |

## Drawing Tablets & Input

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [wacom-driver-fix](https://github.com/thenickdude/wacom-driver-fix) | Patched Wacom drivers for old Bamboo, Intuos and Cintiq tablets on modern macOS | 1,610 | 🟢 | Makefile |
| [TabletDriver](https://github.com/hawku/TabletDriver) | Low-latency Windows graphics tablet driver for Wacom, Huion, XP-Pen and others | 1,227 | 🟡 | C++ |
| [gsl-firmware](https://github.com/onitake/gsl-firmware) | Firmware collection for Silead touchscreen controllers, extracted from Windows drivers for Linux | 388 | 🟢 | C |
| [universal-pidff](https://github.com/JacKeTUs/universal-pidff) | Linux PIDFF force feedback driver with fixes for Moza, Simagic and other wheelbases | 267 | 🟢 | C |
| [dkms-hid-nintendo](https://github.com/nicman23/dkms-hid-nintendo) | DKMS package of the hid-nintendo driver for Joy-Con and Switch Pro controllers | 260 | 🗄️ | C |
| [Tuhi](https://github.com/tuhiproject/tuhi) | Linux app to download drawings from Wacom SmartPad devices over a reverse engineered BLE protocol | 169 | 🟡 | Python |
| [veikk-linux-driver](https://github.com/jlam55555/veikk-linux-driver) | Linux kernel driver for VEIKK graphics tablets | 142 | 🔴 | C |
| [libx52](https://github.com/nirenjan/libx52) | Saitek X52/X52 Pro joystick MFD and LED driver and mapping software for Linux | 134 | 🟢 | C |
| [TuxBox](https://github.com/AndyCappDev/tuxbox) | Linux driver for TourBox controllers over USB and Bluetooth, with haptics and GUI config | 114 | 🟢 | Python |
| [inklingreader](https://github.com/roelj/inklingreader) | GNU/Linux replacement for the Wacom Inkling SketchManager | 50 | 🟢 | C |
| [waxbee](https://github.com/popbee/waxbee) | USB bridge for serial and ADB Wacom and other legacy pen tablets | 48 | 🔴 | C++ |
| [Logitech-G923-Linux-Kernel-Driver](https://github.com/ZRtmWrJqXcjbqBLIMBYMCeUw/Logitech-G923-Linux-Kernel-Driver) | Linux kernel support for the Logitech G923 steering wheel | 43 | 🔴 |  |
| [TabletMagic](https://github.com/thinkyhead/TabletMagic) | Mac OS X driver for Wacom serial tablets and TabletPC digitizers | 43 | 🔴 | C++ |
| [uclogic-tools](https://github.com/DIGImend/uclogic-tools) | Diagnostic tools for UC-Logic (Huion, XP-Pen, Gaomon) graphics tablets | 41 | 🔴 | C |
| [intuos4-oled](https://github.com/sanette/intuos4-oled) | Send images and text to the Wacom Intuos 4 button OLEDs on Linux | 20 | 🟢 | Python |
| [Wacom-STU-WebHID](https://github.com/pabloko/Wacom-STU-WebHID) | JavaScript library for Wacom STU signature pads over WebHID | 20 | 🔴 | JavaScript |

## Firmware/BIOS (coreboot, UEFI)

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [fwupd](https://github.com/fwupd/fwupd) | Linux firmware updater with many reverse-engineered device update protocols | 4,206 | 🟢 | C |
| [MEAnalyzer](https://github.com/platomav/MEAnalyzer) | Intel/AMD engine firmware (ME, TXE, CSE, PSP) analysis tool | 1,343 | 🟢 | Python |
| [flashrom](https://github.com/flashrom/flashrom) | Utility to read and write flash chips on mainboards, programmers and devices | 1,186 | 🟢 | C |
| [efiXplorer](https://github.com/REhints/efiXplorer) | IDA plugin for UEFI firmware analysis and reverse engineering | 1,140 | 🟢 | C++ |
| [UEFI-Editor](https://github.com/BoringBoredom/UEFI-Editor) | Editor for UEFI setup IFR forms to expose hidden BIOS settings | 963 | 🟢 | TypeScript |
| [skulls](https://github.com/merge/skulls) | Prebuilt coreboot images and flashing docs for ThinkPad laptops | 851 | 🟡 | C |
| [PSPTool](https://github.com/PSPReverse/PSPTool) | Parses and modifies AMD Platform Security Processor firmware blobs | 716 | 🟢 | Python |
| [IFRExtractor-RS](https://github.com/LongSoft/IFRExtractor-RS) | Extracts UEFI HII IFR setup forms into human-readable text | 492 | 🟢 | Rust |
| [fiano](https://github.com/linuxboot/fiano) | Go tools and library for parsing and modifying UEFI firmware images | 375 | 🟢 | Go |
| [UEFI_RETool](https://github.com/yeggor/uefi_retool) | Tool for analysing UEFI firmware modules | 369 | 🗄️ | Python |
| [Dasharo coreboot](https://github.com/Dasharo/coreboot) | Dasharo's coreboot fork with ports for commercial desktops and laptops | 155 | 🟢 | C |
| [coreboot-configurator](https://github.com/StarLabsLtd/coreboot-configurator) | GUI to change coreboot CBFS settings via nvramtool | 102 | 🔴 | C++ |
| [MrChromebox firmware](https://github.com/MrChromebox/firmware) | Issue tracker for MrChromebox coreboot-based UEFI firmware for Chromebooks | 100 | 🟢 |  |
| [x210](https://github.com/harrykipper/x210) | Patches, mods and docs for the 51nb X210 ThinkPad-derived board | 41 | 🔴 |  |
| [isfl](https://github.com/tomreyn/isfl) | Insyde Software UEFI firmware flashing kernel driver | 37 | 🔴 | C |
| [bootguard-status](https://github.com/felixsinger/bootguard-status) | List of mainboards and their Intel Boot Guard status for coreboot porting | 33 | 🟢 | HTML |
| [mmga](https://github.com/gch1p/mmga) | Flash coreboot on MacBooks without an external SPI programmer | 31 | 🗄️ | Shell |
| [intel_ma](https://github.com/seuros/intel_ma) | Inspect Intel ME/TXE/CSME management firmware images | 14 | 🟢 | Rust |
| [lenovo_bios](https://github.com/root-hunter/lenovo_bios) | Reverse engineering of Lenovo IdeaPad Gaming 3 firmware: BIOS extraction and AMD PSP analysis | 12 | 🟢 | Python |
| [pch-pads-parser](https://github.com/maxpoliak/pch-pads-parser) | Parses inteltool PCH GPIO dumps into coreboot pad configs for board ports | 10 | 🗄️ | Go |
| [Libreboot lbmk](https://codeberg.org/libreboot/lbmk) | Libreboot build system: coreboot board ports, blob extraction and payloads |  | ⚪ |  |

## GPU Drivers

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [applecpu](https://github.com/dougallj/applecpu) | Reverse-engineered Apple Firestorm/Icestorm CPU microarchitecture notes | 265 | 🔴 | HTML |
| [DLSSNR-AMD](https://github.com/mochizuki0323/DLSSNR-AMD) | Reimplementation of the NVIDIA DLSS 5 neural-rendering network as Vulkan compute shaders for AMD GPUs | 185 | 🟢 | C++ |
| [mesa-lima](https://github.com/yuq/mesa-lima) | Development tree of the Lima Mali-400 driver before upstream Mesa merge | 164 | 🔴 | C |
| [gddr6](https://github.com/olealgoritme/gddr6) | Linux GDDR6/GDDR6X VRAM temperature reader for NVIDIA RTX cards | 159 | 🟢 | C |
| [radeon-tools](https://github.com/fail0verflow/radeon-tools) | AMD Radeon reverse engineering tools | 154 | 🔴 | Python |
| [PVR_PSP2](https://github.com/GrapheneCt/PVR_PSP2) | Driver-layer GPU libraries and tests for the PS Vita's PowerVR SGX | 116 | 🟡 | C |
| [grate](https://github.com/grate-driver/grate) | Reverse-engineering tools and docs for the NVIDIA Tegra 2/3 GPU (open Tegra graphics) | 90 | 🟢 | C |
| [dlss-nr-on-intel](https://github.com/Uzbekunknown/dlss-nr-on-intel) | Independent reimplementation of the DLSS neural rendering inference pass on an Intel iGPU | 67 | 🟢 | Python |
| [three-dlss-nr](https://github.com/bhouston/three-dlss-nr) | Three.js WebGPU port of OpenDLSS-NR, the reimplementation of NVIDIA's DLSS 5 neural renderer | 66 | 🟢 | TypeScript |
| [linux_openpvrsgx](https://github.com/openpvrsgx-devgroup/linux_openpvrsgx) | Reshaping PowerVR SGX GPL kernel drivers for mainline Linux | 65 | 🟢 | C |
| [linux-cedrus](https://github.com/bootlin/linux-cedrus) | Mainline kernel tree for the Allwinner VPU (Cedrus) reverse engineering effort | 61 | 🔴 | C |
| [NVFC](https://github.com/graphitemaster/NVFC) | Open-source tool for monitoring, configuring and overclocking NVIDIA GPUs | 50 | 🔴 | C |
| [mali-isa-docs](https://github.com/cwabbott0/mali-isa-docs) | Reverse-engineered documentation of Arm Mali GPU shader ISAs | 44 | 🔴 |  |
| [tegra-re](https://github.com/kusma/tegra-re) | Reverse engineering of NVIDIA's Tegra Linux driver | 36 | 🗄️ | C |
| [blackwell-isa](https://github.com/kacper-daftcode/blackwell-isa) | Reverse-engineered ISA database for NVIDIA SM120 Blackwell GPUs | 21 | 🟢 | HTML |
| [libvdpau-tegra](https://github.com/grate-driver/libvdpau-tegra) | VDPAU video decode driver for NVIDIA Tegra built from reverse-engineered hardware | 16 | 🔴 | C |
| [open-dlss](https://github.com/aloshdenny/open-dlss) | Vulkan reimplementation of NVIDIA's DLSS 5 neural rendering network, bit-exact | 11 | 🟢 | JavaScript |
| [SGX535-reMESA](https://github.com/gabrieelgama/SGX535-reMESA) | Mesa/Gallium 3D driver for Intel GMA 500 (PowerVR SGX535) built through reverse engineering | 11 | 🟢 | C |
| [etna-gpu-tools](https://github.com/etnaviv/etna-gpu-tools) | Vivante GPU debugging and reverse-engineering tools from the etnaviv project | 4 | 🔴 | C |
| [Asahi Mesa driver](https://docs.mesa3d.org/drivers/asahi.html) | Mesa OpenGL/Vulkan driver for Apple AGX GPUs, with reverse-engineered ISA notes |  | ⚪ |  |
| [bvhre](https://gitlab.freedesktop.org/bnieuwenhuizen/bvhre) | Reverse engineering the RDNA2 ray-tracing BVH format |  | ⚪ |  |
| [Freedreno / Turnip](https://docs.mesa3d.org/drivers/freedreno.html) | Reverse-engineered Mesa OpenGL and Vulkan drivers for Qualcomm Adreno GPUs |  | ⚪ |  |
| [Hercules](https://codeberg.org/btb/Hercules) | Reverse engineering of the Hercules Graphics Card |  | ⚪ |  |
| [Lima](https://docs.mesa3d.org/drivers/lima.html) | Reverse-engineered Mesa driver for Arm Mali-400/450 (Utgard) GPUs |  | ⚪ |  |
| [mali-syscall-tracker](https://gitlab.freedesktop.org/lima/mali-syscall-tracker) | Tool for dumping memory of the closed-source Mali driver, used to reverse engineer Mali GPUs |  | ⚪ |  |
| [Mesa](https://gitlab.freedesktop.org/mesa/mesa) | Mesa 3D: hosts reverse-engineered GPU drivers (panfrost, lima, freedreno, etnaviv, nouveau, asahi, NVK) |  | ⚪ |  |
| [nouveau](https://gitlab.freedesktop.org/drm/nouveau) | Nouveau kernel driver for NVIDIA GPUs, built by reverse engineering |  | ⚪ |  |
| [nv-shader-tools](https://gitlab.freedesktop.org/nouveau/nv-shader-tools) | Tools for reverse engineering NVIDIA shader ISAs using the CUDA disassembler |  | ⚪ |  |
| [NVClock](https://sourceforge.net/projects/nvclock/) | Overclocking, monitoring and tweaking tool for NVIDIA cards using undocumented registers |  | ⚪ |  |
| [NVK](https://docs.mesa3d.org/drivers/nvk.html) | Open-source Mesa Vulkan driver for NVIDIA GPUs built on nouveau |  | ⚪ |  |
| [Panfrost / PanVK](https://docs.mesa3d.org/drivers/panfrost.html) | Reverse-engineered Mesa driver for Arm Mali Midgard, Bifrost and Valhall GPUs |  | ⚪ |  |
| [recu](https://codeberg.org/tondik/recu) | Reverse engineering NVIDIA CUDA internals |  | ⚪ |  |
| [sgx540-reversing](https://codeberg.org/Garnet/sgx540-reversing) | Documentation and tooling from reverse engineering the PowerVR SGX540 GPU |  | ⚪ |  |
| [sqtt-toy](https://gitlab.freedesktop.org/ishitatsuyuki/sqtt-toy) | AMD SQTT thread trace reverse engineering experiments |  | ⚪ |  |
| [xf86-video-nouveau](https://gitlab.freedesktop.org/xorg/driver/xf86-video-nouveau) | X.Org DDX driver for NVIDIA GPUs from the nouveau project |  | ⚪ |  |

## Gaming Laptops & Handheld PCs

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [Lenovo Legion Toolkit](https://github.com/BartoszCichecki/LenovoLegionToolkit) | Lightweight replacement for Lenovo Vantage and Hotkeys on Legion laptops | 7,534 | 🗄️ | C# |
| [Universal x86 Tuning Utility](https://github.com/JamesCJ60/Universal-x86-Tuning-Utility) | Power, TDP and undervolt tuning for Intel/AMD laptops and handhelds | 2,892 | 🟢 | HLSL |
| [Lenovo Legion Toolkit (community)](https://github.com/LenovoLegionToolkit-Team/LenovoLegionToolkit) | Community continuation of Lenovo Legion Toolkit, a Vantage replacement for Legion laptops | 2,393 | 🟢 | C# |
| [Handheld Companion](https://github.com/Valkirie/HandheldCompanion) | Windows tool for handheld PCs: controller emulation, gyro, TDP and fan control without vendor apps | 1,742 | 🟢 | C# |
| [Steam Deck Tools](https://github.com/ayufan/steam-deck-tools) | Windows fan, overlay, power and Steam Controller emulation for the Steam Deck hardware | 1,144 | 🟡 | C# |
| [alienfx-tools](https://github.com/T-Troll/alienfx-tools) | Open tools for Alienware lights, fans and power control, replacing AWCC | 882 | 🟢 | C++ |
| [Thermal Control Center for Dell G15](https://github.com/AlexIII/tcc-g15) | Open-source alternative to Alienware Command Center for Dell G15 thermal modes | 845 | 🟢 | Python |
| [rogauracore](https://github.com/wroberts/rogauracore) | RGB keyboard control for ASUS ROG laptops on Linux (reverse engineered USB commands) | 778 | 🟢 | C |
| [Div Acer Manager Max](https://github.com/PXDiv/Div-Acer-Manager-Max) | Linux GUI for Acer Predator/Nitro laptops, replicating NitroSense/PredatorSense features | 748 | 🟢 | C# |
| [MControlCenter](https://github.com/dmitry-s93/MControlCenter) | Linux app to change MSI laptop fan, battery and performance settings via the EC | 720 | 🟢 | C++ |
| [OmenSuperHub](https://github.com/breadeding/OmenSuperHub) | HP Omen performance, fan and keyboard lighting control with power limit unlock | 566 | 🟢 | C# |
| [g-helper-linux](https://github.com/utajum/g-helper-linux) | Unofficial Linux port of G-Helper for ASUS ROG, TUF and Zephyrus laptops | 528 | 🟢 | C# |
| [L5P-Keyboard-RGB](https://github.com/4JX/L5P-Keyboard-RGB) | Cross-platform control of the 4-zone RGB keyboard on Lenovo Legion laptops | 524 | 🟢 | Rust |
| [vantage](https://github.com/niizam/vantage) | Lenovo Vantage features (conservation mode, fn-lock, power) for Linux | 509 | 🟡 | Shell |
| [asus-numberpad-driver](https://github.com/asus-linux-drivers/asus-numberpad-driver) | Linux driver for the illuminated NumberPad touchpad on ASUS laptops | 452 | 🟢 | Python |
| [steam-deck-windows-usermode-driver](https://github.com/mKenfenheuer/steam-deck-windows-usermode-driver) | Windows usermode driver for the Steam Deck's built-in controller | 437 | 🗄️ | C# |
| [OmenMon](https://github.com/OmenMon/OmenMon) | HP Omen fan, temperature and backlight control via WMI BIOS and EC, replacing Omen Gaming Hub | 410 | 🟡 | C# |
| [razer-blade-stealth-linux](https://github.com/rolandguelle/razer-blade-stealth-linux) | Guide and fixes for running Linux on the Razer Blade Stealth and Razer Core | 404 | 🔴 | Shell |
| [asus-fan-control](https://github.com/dominiksalvet/asus-fan-control) | Fan control for ASUS laptops on Linux via ACPI calls | 393 | 🟢 | Shell |
| [atrofac](https://github.com/cronosun/atrofac) | Library and CLI to control ASUS ROG power plans and fan curves without Armoury Crate | 357 | 🔴 | Rust |
| [razer-laptop-control](https://github.com/rnd-ash/razer-laptop-control) | Driver and software to control fan and performance modes of Razer Blade laptops on Linux | 347 | 🗄️ | Rust |
| [alienfx](https://github.com/trackmastersteve/alienfx) | CLI and GUI to control Alienware lighting effects on Linux | 338 | 🟢 | Python |
| [msi-keyboard](https://github.com/stephenlacy/msi-keyboard) | MSI SteelSeries laptop keyboard LED controller (reverse engineered HID) | 313 | 🔴 | JavaScript |
| [SimpleDeckyTDP](https://github.com/aarron-lee/SimpleDeckyTDP) | Decky plugin for TDP, CPU boost and GPU control on Linux PC handhelds | 297 | 🟢 | Python |
| [avell-unofficial-control-center](https://github.com/rodgomesc/avell-unofficial-control-center) | Unofficial control center for Avell laptops on Linux | 289 | 🔴 | Python |
| [LenovoController](https://github.com/ViRb3/LenovoController) | Lightweight Windows alternative to Lenovo Vantage for Legion laptops | 278 | 🗄️ | C# |
| [AsusFanControl](https://github.com/Karmel0x/AsusFanControl) | Small fan control app for ASUS laptops on Windows without Armoury Crate | 257 | 🟡 | C# |
| [OMEN Space](https://github.com/yunusemreyl/omen-space) | Command center for HP OMEN and Victus laptops on Linux | 256 | 🟢 | Rust |
| [MSIKLM](https://github.com/Gibtnix/MSIKLM) | Control the SteelSeries keyboard lighting of MSI gaming laptops on Linux | 255 | 🔴 | C |
| [OmenCore](https://github.com/theantipopau/omencore) | Performance control for HP Omen laptops replacing Omen Gaming Hub | 255 | 🟢 | C# |
| [Ayuz](https://github.com/Traciges/Ayuz) | Unofficial MyAsus alternative control center for Linux | 243 | 🟢 | Rust |
| [hp-omen-linux-module](https://github.com/pelrun/hp-omen-linux-module) | Linux kernel module for HP Omen keyboard lighting and performance settings | 226 | 🔴 | C |
| [AWCC (Linux)](https://github.com/tr1xem/AWCC) | Unofficial Linux alternative to Alienware Command Center for Dell G series | 207 | 🟢 | C++ |
| [asus-wmi-screenpad](https://github.com/Plippo/asus-wmi-screenpad) | asus-wmi kernel module variant with ScreenPad brightness support for ASUS laptops | 182 | 🟢 | C |
| [gpd-win-tricks](https://github.com/aarron-lee/gpd-win-tricks) | Info and fixes for running Linux on GPD Win devices | 165 | 🟢 | Shell |
| [ryzen_smu](https://github.com/leogx9r/ryzen_smu) | Linux kernel driver exposing the AMD Ryzen System Management Unit mailbox to userspace | 152 | 🔴 | C |
| [OmenXHub](https://github.com/MasonDye/OmenXHub) | Lightweight offline replacement for HP OMEN Gaming Hub | 150 | 🟢 | C# |
| [clevo-indicator](https://github.com/SkyLandTW/clevo-indicator) | Ubuntu fan control indicator for Clevo laptops using direct EC access | 147 | 🔴 | C |
| [Lecoo-Control-Center](https://github.com/LaVashikk/Lecoo-Control-Center) | Rust daemon controlling fans, TDP and battery on Lecoo laptops | 146 | 🟢 | Rust |
| [razer-laptop-control-no-dkms](https://github.com/Razer-Linux/razer-laptop-control-no-dkms) | Userspace Razer Blade fan, power and RGB control on Linux without a kernel module | 136 | 🗄️ | Rust |
| [akbl](https://github.com/rsm-gh/akbl) | Control Alienware computer lights under GNU/Linux | 132 | 🗄️ | Python |
| [omen-fan](https://github.com/alou-S/omen-fan) | Fan control utility for HP Omen laptops on Linux via EC registers | 110 | 🟢 | Python |
| [ohman](https://github.com/P4R1H/ohman) | Lightweight OMEN Gaming Hub alternative with fan curves, modes and GPU power | 98 | 🟢 | C# |
| [RLECViewer](https://github.com/zuyan9/RLECViewer) | Custom fan control for Clevo laptops via the EC | 92 | 🔴 | C++ |
| [PowerStation](https://github.com/ShadowBlip/PowerStation) | TDP and performance daemon with DBus interface for x86 handheld gaming PCs | 84 | 🟢 | Rust |
| [gigabyte-laptop-wmi](https://github.com/tangalbert919/gigabyte-laptop-wmi) | Linux kernel module for Gigabyte AERO/AORUS laptop fan and charge controls | 79 | 🟢 | ASL |
| [HandyGCCS](https://github.com/ShadowBlip/HandyGCCS) | Linux controller support for handheld PCs (AYANEO, GPD, OneXPlayer, ROG Ally) built-in gamepads | 76 | 🗄️ | Python |
| [LegionGoRemapper](https://github.com/aarron-lee/LegionGoRemapper) | Decky plugin to remap Legion Go buttons and control its controller LEDs on Linux | 74 | 🟢 | TypeScript |
| [AlienFxLite](https://github.com/bchretien/AlienFxLite) | Keyboard color management for Alienware laptops (Java with native USB) | 73 | 🔴 | Java |
| [allycenter](https://github.com/PixelAddictUnlocked/allycenter) | Decky plugin adding ROG Ally controls and settings to SteamOS | 68 | 🟢 | Python |
| [victus-control](https://github.com/Batuhan4/victus-control) | Linux fan control and keyboard lighting for HP Victus/Omen laptops | 62 | 🟢 | C++ |
| [ZenStates-Core](https://github.com/irusanov/ZenStates-Core) | Library for reading and tuning AMD Zen SMU, P-states and memory timings from undocumented interfaces | 61 | 🟢 | C# |
| [OmenHubLight](https://github.com/determ1ne/OmenHubLight) | Open lightweight substitute for HP Omen Hub programs | 60 | 🗄️ | C# |
| [omen-rgb-keyboard](https://github.com/OmenLinux/omen-rgb-keyboard) | Linux kernel driver for HP OMEN laptop RGB keyboard lighting | 54 | 🟢 | C |
| [omen-fan-control](https://github.com/arfelious/omen-fan-control) | HP Omen and Victus fan control CLI and GUI for Linux | 53 | 🟢 | Python |
| [Zephyrus Control Center](https://github.com/vddCore/Zephyrus-Control-Center) | Armoury Crate replacement for ASUS Zephyrus laptops | 50 | 🟡 | C# |
| [OmenHwCtl](https://github.com/GeographicCone/OmenHwCtl) | HP Omen hardware control via the BIOS WMI interface | 49 | 🟡 | PowerShell |
| [tuxedo-backlight-control](https://github.com/webketje/tuxedo-backlight-control) | CLI and UI for TUXEDO/Clevo keyboard backlight on Linux | 49 | 🗄️ | Python |
| [openomen](https://github.com/openomen/openomen) | Unofficial Linux driver and daemon for HP OMEN hardware | 48 | 🟢 | Python |
| [MsiFanControl](https://github.com/kykc/MsiFanControl) | Fan control utility for MSI laptops | 45 | 🔴 | C# |
| [g-helper-linux (UdayaSri0)](https://github.com/UdayaSri0/g-helper-linux) | Open control tool for ASUS laptops and ROG Ally on Linux: modes, fans, lighting | 43 | 🟢 | HTML |
| [alfc](https://github.com/s-h-a-d-o-w/alfc) | Fan control with browser UI for the Gigabyte Aorus 15G | 37 | 🗄️ | TypeScript |
| [ClevoECView](https://github.com/SkyLandTW/ClevoECView) | ECView tool to control fans on Clevo laptops | 37 | 🔴 | C# |
| [gpd-fan-driver](https://github.com/Cryolitia/gpd-fan-driver) | Linux kernel driver for GPD handheld and mini-laptop fan control via the EC | 36 | 🟢 | C |
| [alienfx-linux](https://github.com/tr1xem/alienfx-linux) | SDK for Alienware lights and fan control on Linux | 35 | 🟢 | C++ |
| [CppKeyboardColour](https://github.com/DeviceIoControl/CppKeyboardColour) | CLI RGB keyboard backlight control for Clevo and Tongfang laptops | 32 | 🟢 | C++ |
| [clevo-keyboard-backlight](https://github.com/ejcosta/clevo-keyboard-backlight) | Driver for Clevo backlit keyboards | 31 | 🗄️ | C |
| [LeGo2 Fan Control](https://github.com/Rodpad/LeGo2-Fan-Control) | Unrestricted fan control for the Lenovo Legion Go 2 | 31 | 🟢 | TypeScript |
| [alienfx (Aurora)](https://github.com/erlkonig/alienfx) | Control AlienFX lighting on Alienware Aurora desktops under Linux | 27 | 🟡 | Makefile |
| [Vantage (GTK)](https://github.com/kush4gra/Vantage) | Native GTK4 Lenovo Vantage controls for IdeaPad, Yoga and Legion on Linux | 27 | 🟢 | Python |
| [ayaneo-platform](https://github.com/ShadowBlip/ayaneo-platform) | Linux kernel driver for AYANEO handheld RGB and platform controls via the EC | 24 | 🟢 | C |
| [clevo-fan-control](https://github.com/agramian/clevo-fan-control) | Linux fan control service for Clevo laptops | 24 | 🟢 | C |
| [VFang](https://github.com/bladeandsoulx/vfang-razer-linux) | Open Razer Blade control center for Linux: fans, power and lighting | 23 | 🟢 | Rust |
| [clevo-xsm-wmi](https://github.com/rafaelgieschke/clevo-xsm-wmi) | Clevo WMI keyboard backlight driver with CPU/GPU PWM fan control | 21 | 🟡 | C |
| [pyAlienFX](https://github.com/Xqua/pyAlienFX) | Multiplatform Python software to control AlienFX devices | 20 | 🔴 |  |
| [ROGueENEMY](https://github.com/NeroReflex/ROGueENEMY) | ROG Ally userspace driver that merges its gamepad, keyboard and IMU into one virtual controller | 14 | 🟡 | C |
| [ayn-platform](https://github.com/ShadowBlip/ayn-platform) | Linux hwmon driver for AYN x86 handhelds: PWM fan control, temperatures and RGB | 9 | 🟡 | C |
| [Adjustor](https://github.com/hhd-dev/adjustor) | TDP and power control for handheld PCs via ACPI/EC calls, part of Handheld Daemon | 7 | 🗄️ | Python |
| [afx](https://gitlab.com/lynthium/afx) | Reverse-engineered AlienFX lighting control for the Alienware 15 R3 |  | ⚪ |  |
| [asus-linux reverse-engineering](https://gitlab.com/asus-linux/reverse-engineering) | Data dumps and reverse engineering notes used to support ASUS ROG laptops on Linux |  | ⚪ |  |
| [oxp-sensors](https://gitlab.com/Samsagax/oxp-sensors) | Linux platform driver for OneXPlayer/AOKZOE handheld fan control and EC sensors |  | ⚪ |  |
| [supergfxctl](https://gitlab.com/asus-linux/supergfxctl) | GPU switching daemon for ASUS ROG and other hybrid-graphics laptops on Linux |  | ⚪ |  |
| [tongfang-control](https://gitlab.com/siphomateke/tongfang-control) | Open-source control centre for Tongfang-based laptops (RGB lighting, fan speeds) |  | ⚪ |  |

## Headsets, Audio Interfaces & Webcams

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [gopro_as_webcam_on_linux](https://github.com/jschmid1/gopro_as_webcam_on_linux) | Use a GoPro as a webcam on Linux via its USB webcam mode | 706 | 🟢 | Shell |
| [OpenSCQ30](https://github.com/Oppzippy/OpenSCQ30) | Cross-platform app for Anker Soundcore headphone and earbud settings | 527 | 🟢 | Rust |
| [OpenFreebuds](https://github.com/melianmiko/OpenFreebuds) | Open app for Huawei FreeBuds settings and noise control on Linux and Windows | 463 | 🟢 | Python |
| [linux-enable-ir-emitter](https://github.com/EmixamPP/linux-enable-ir-emitter) | Enables infrared emitters on laptop IR cameras under Linux by finding the UVC extension control | 369 | 🟢 | Rust |
| [elgato-gchd](https://github.com/tolga9009/elgato-gchd) | Reverse engineered Linux userspace driver for the Elgato Game Capture HD | 298 | 🔴 | C++ |
| [Linux Arctis Manager](https://github.com/elegos/Linux-Arctis-Manager) | Open replacement for SteelSeries GG to manage Arctis headsets and ChatMix on Linux | 214 | 🟢 | Rust |
| [SoundcoreManager](https://github.com/gmallios/SoundcoreManager) | Rust app to control Anker Soundcore headphones over Bluetooth | 183 | 🟡 | Rust |
| [macbook12-audio-driver](https://github.com/leifliddy/macbook12-audio-driver) | Linux audio driver for the CS4208 codec in the 12-inch MacBook | 173 | 🟢 | C |
| [Arctis Sound Manager](https://github.com/loteran/Arctis-Sound-Manager) | SteelSeries GG and Sonar alternative for Arctis headsets on Linux with mixer and EQ | 170 | 🟢 | Python |
| [sc0710](https://github.com/stoth68000/sc0710) | Linux driver for the Elgato 4K60 Pro Mk.2 capture card | 163 | 🔴 | C |
| [sc0710 (multi-client)](https://github.com/Nakildias/sc0710) | Multi-client Linux driver for Elgato 4K60 Pro MK.2, 4K Pro and Cam Link Pro capture cards | 153 | 🟢 | C |
| [PS4 Camera Tools](https://github.com/ps4eye/ps4eye) | Tools to load firmware and use the PlayStation 4 camera on PC | 144 | 🔴 | C |
| [HyperHeadset](https://github.com/LennardKittner/HyperHeadset) | CLI and tray app to monitor and manage HyperX Cloud II and Stinger headsets on Linux/macOS | 130 | 🟢 | Rust |
| [Ozzy](https://github.com/mischa85/Ozzy) | Driver for Ploytec-based USB audio interfaces | 117 | 🟢 | C |
| [QuadcastRGB](https://github.com/Ors1mer/QuadcastRGB) | Set RGB lights on HyperX QuadCast S and DuoCast microphones on Linux | 107 | 🟢 | C |
| [pseyepy](https://github.com/bensondaled/pseyepy) | Python interface to the Sony PS3 Eye camera | 98 | 🟢 | C |
| [MixiD](https://github.com/TheOnlyJoey/MixiD) | Unofficial Linux control panel for Audient iD interfaces using a reverse engineered USB protocol | 85 | 🟢 | C++ |
| [Open Apollo](https://github.com/rolotrealanis98/open-apollo) | Clean-room reverse engineered Linux driver for Universal Audio Apollo Thunderbolt interfaces | 78 | 🟢 | Python |
| [arctis-battery-percentage](https://github.com/atagulalan/arctis-battery-percentage) | Shows SteelSeries Arctis wireless headset battery as a notification | 70 | 🗄️ | JavaScript |
| [snd-hdspe](https://github.com/PhilippeBekaert/snd-hdspe) | New Linux ALSA driver and tools for RME HDSPe MADI, AES and RayDAT sound cards | 68 | 🔴 | C |
| [kiyoproctrls](https://github.com/soyersoyer/kiyoproctrls) | Razer Kiyo Pro webcam controls (HDR, FOV, AF) for Linux via UVC extension units | 66 | 🔴 | Python |
| [ggoled](https://github.com/JerwuQu/ggoled) | OLED integration for the SteelSeries Arctis Nova Pro base station without GG | 57 | 🟢 | Rust |
| [HyperX-Cloud-2-Battery-Monitor](https://github.com/auto94/HyperX-Cloud-2-Battery-Monitor) | Battery monitor for HyperX Cloud II, III and Alpha wireless headsets | 56 | 🟢 | C++ |
| [nova-chatmix-linux](https://github.com/Dymstro/nova-chatmix-linux) | ChatMix support for the SteelSeries Arctis Nova Pro Wireless on Linux | 51 | 🟡 | Python |
| [elgato4k60sp-linux](https://github.com/Saddytech/elgato4k60sp-linux) | Unofficial Linux kernel driver for the Elgato Game Capture 4K60 S+ | 46 | 🟢 | C |
| [hyperx-cloud-flight-wireless](https://github.com/srn/hyperx-cloud-flight-wireless) | Reverse engineered Node module for HyperX Cloud Flight Wireless battery and mute events | 46 | 🔴 | JavaScript |
| [sonar-rev](https://github.com/wex/sonar-rev) | Reverse engineering notes and client for the SteelSeries GG Sonar local API | 46 | 🟡 | C# |
| [steelseries-arctis-5-pulseaudio-profile](https://github.com/DemonTPx/steelseries-arctis-5-pulseaudio-profile) | PulseAudio profile for the SteelSeries Arctis 5 headset | 43 | 🔴 | Makefile |
| [hyperx-cloud-flight](https://github.com/kondinskis/hyperx-cloud-flight) | Tray app showing battery level of the HyperX Cloud Flight Wireless headset on Linux | 42 | 🟡 | Rust |
| [soundblaster-x-g6-cli](https://github.com/nils-skowasch/soundblaster-x-g6-cli) | Python CLI to control the Creative Sound BlasterX G6 DAC settings on Linux | 33 | 🟢 | Python |
| [C920e](https://github.com/MavChtz/C920e) | Enables or disables the microphone on Logitech C920e/C925e webcams on Linux | 31 | 🟡 | Python |
| [Linux-Arctis-7-Plus-ChatMix](https://github.com/awth13/Linux-Arctis-7-Plus-ChatMix) | ChatMix workaround for the SteelSeries Arctis 7+ on Linux without GG | 27 | 🟢 | Python |
| [razer-nari-pairing](https://github.com/juanjodarko/razer-nari-pairing) | Open-source tool to pair Razer Nari headsets with USB dongles on Linux | 26 | 🟢 | Python |
| [elgato-cam-link-4k-firmware-re](https://github.com/schlarpc/elgato-cam-link-4k-firmware-re) | Firmware reverse engineering of the Elgato Cam Link 4K: vendor HID protocol and SPI flash layout | 22 | 🟢 | Python |
| [steelseries-wireless-battery-tray](https://github.com/mtadin/steelseries-wireless-battery-tray) | Tray app showing battery of SteelSeries wireless headsets | 21 | 🟢 | Go |
| [arctis7_controls](https://github.com/trevarj/arctis7_controls) | Controls for the SteelSeries Arctis 7 wireless headset in Rust or Python | 19 | 🟡 | Rust |
| [SteelSeries-NET-API](https://github.com/DataNext27/SteelSeries-NET-API) | Unofficial .NET library for the SteelSeries Sonar local API | 7 | 🟢 | C# |
| [corsair-void-driver](https://github.com/stuarthayhurst/corsair-void-driver) | Linux kernel driver for Corsair Void headsets: battery, sidetone, mic status (upstreamed 6.13) | 6 | 🟢 | C |
| [hyperx-cloud-II-battery](https://github.com/Agustin-Jerusalinsky/hyperx-cloud-II-battery) | Reads HyperX Cloud II wireless headset battery level over hidraw | 6 | 🔴 | Python |
| [ps4cam-linux](https://sr.ht/~mks-h/ps4cam-linux/) | Linux driver for the PlayStation 4 Camera |  | ⚪ |  |
| [spca50x](https://sourceforge.net/projects/spca50x/) | Linux driver for Sunplus SPCA5xx webcams, predecessor of gspca |  | ⚪ |  |

## Lab Instruments & Thermal Cameras

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [stlink](https://github.com/stlink-org/stlink) | Open source STM32 programming toolset for ST-Link debug probes | 5,204 | 🟢 | C |
| [openFPGALoader](https://github.com/trabucayre/openFPGALoader) | Universal FPGA programmer supporting many vendor JTAG cables and boards | 1,766 | 🟢 | C++ |
| [OpenHantek6022](https://github.com/OpenHantek/OpenHantek6022) | DSO software for Hantek 6022BE/BL USB oscilloscopes with open firmware | 1,137 | 🟢 | C++ |
| [OpenHantek](https://github.com/OpenHantek/openhantek) | DSO software for Hantek, Voltcraft and similar USB oscilloscopes | 830 | 🟡 | C++ |
| [libsigrok](https://github.com/sigrokproject/libsigrok) | Signal analysis library with drivers for many logic analyzers, scopes and meters | 446 | 🟢 | C |
| [ch341prog](https://github.com/setarcos/ch341prog) | Open SPI/I2C flash programmer for the CH341A USB adapter | 422 | 🟢 | C |
| [libseek-thermal](https://github.com/OpenThermal/libseek-thermal) | Linux driver for Seek Thermal Compact, CompactXR and CompactPRO cameras | 344 | 🟡 | C++ |
| [PyThermalCamera](https://github.com/leswright1977/PyThermalCamera) | Python software for the Topdon TC001 thermal camera on Linux and Raspberry Pi | 326 | 🟡 | Python |
| [OWON-VDS1022](https://github.com/florentbr/OWON-VDS1022) | Unofficial improved software release for the OWON VDS1022/I USB oscilloscope | 306 | 🟢 | Python |
| [rd-usb](https://github.com/kolinger/rd-usb) | Web GUI for RuiDeng/Riden USB testers (UM34C, UM24C, UM25C, TC66C) | 276 | 🟢 | Python |
| [P2Pro-Viewer](https://github.com/LeoDJ/P2Pro-Viewer) | Viewer and API for the InfiRay P2 Pro thermal camera with a reverse engineered protocol | 257 | 🟡 | Python |
| [ppk2-api-python](https://github.com/IRNAS/ppk2-api-python) | Unofficial Python API for the Nordic Power Profiler Kit II | 256 | 🟢 | Python |
| [fnirsi-usb-power-data-logger](https://github.com/baryluk/fnirsi-usb-power-data-logger) | Data logger for FNIRSI FNB48, C1 and FNB58 USB power meters | 245 | 🟡 | Python |
| [AWG_DHO8-900](https://github.com/MatthiasElectronic/AWG_DHO8-900) | Arbitrary waveform generator add-on for Rigol DHO800/DHO900 oscilloscopes | 219 | 🟢 |  |
| [UT210E](https://github.com/af3556/UT210E) | Reverse engineered information and data-logging for the UNI-T UT210E clamp meter | 200 | 🔴 |  |
| [FNIRSI-1013D-1014D-Hack](https://github.com/pecostm32/FNIRSI-1013D-1014D-Hack) | Reverse engineering resources and firmware for FNIRSI 1013D/1014D scopes | 155 | 🟡 | C |
| [rusty_meter](https://github.com/markusdd/rusty_meter) | Rust app to operate OWON XDM and Victor bench multimeters without vendor software | 145 | 🟢 | Rust |
| [Hantek6022API](https://github.com/rpcope1/Hantek6022API) | Python API for the Hantek 6022BE USB scope, reverse engineered from USB traces | 137 | 🔴 | Assembly |
| [qrigol](https://github.com/wd5gnr/qrigol) | Qt assistant for Rigol DS1000 series scopes over USB | 134 | 🔴 | C++ |
| [Thermal-Camera-Redux](https://github.com/92es/Thermal-Camera-Redux) | Topdon TC001 and clone thermal camera app for live and offline radiometric data | 132 | 🟡 | C++ |
| [OpenScope-2C53T](https://github.com/DavidClawson/OpenScope-2C53T) | Reverse engineering and open firmware for the FNIRSI 2C53T scope/multimeter | 121 | 🟢 | C |
| [rd6006](https://github.com/Baldanos/rd6006) | Python module to control Riden RD6006 programmable power supplies | 118 | 🟡 | Python |
| [flirone-v4l2](https://github.com/fnoop/flirone-v4l2) | V4L2 bridge to use the FLIR One thermal camera on Linux | 111 | 🔴 | C |
| [esphome-atorch-dl24](https://github.com/syssi/esphome-atorch-dl24) | ESPHome component for Atorch DL24 and other Atorch meters over their proprietary Bluetooth protocol | 110 | 🟢 | C++ |
| [sds1004x_bode](https://github.com/4x1md/sds1004x_bode) | Emulates a Siglent AWG so SDS1004X-E scopes can do Bode plots with third-party generators | 97 | 🟡 | Python |
| [CO2Meter](https://github.com/heinemml/CO2Meter) | Python module for USB CO2 meters with reversed encryption | 89 | 🔴 | Python |
| [ht301_hacklib](https://github.com/stawel/ht301_hacklib) | OpenCV library for the Hti HT-301 and similar USB thermal cameras with raw temperature data | 87 | 🟡 | Python |
| [temper](https://github.com/urwen/temper) | Python tool for reading TEMPer USB thermometers | 86 | 🟡 | Python |
| [seek-thermal-documentation](https://github.com/lod/seek-thermal-documentation) | Unofficial documentation of the Seek Thermal USB protocol | 83 | 🔴 | Python |
| [UNI-T-Thermal-Utilities](https://github.com/Santi-hr/UNI-T-Thermal-Utilities) | Extracts raw temperature data from UNI-T thermal camera images | 80 | 🟡 | Python |
| [libseek](https://github.com/zougloub/libseek) | libusb-based API for the Seek Thermal imager | 76 | 🔴 | C++ |
| [Dokit](https://github.com/pcolby/dokit) | Cross-platform library and apps for Pokit Bluetooth measuring devices | 75 | 🟢 | C++ |
| [Riden](https://github.com/ShayBox/Riden) | Python library for Riden RD series power supplies | 74 | 🟡 | Python |
| [thermal-cat](https://github.com/alufers/thermal-cat) | Cross-platform viewer app for the InfiRay P2 Pro thermal camera | 74 | 🟢 | Rust |
| [BOSCH-GLM-rangefinder](https://github.com/philipptrenz/BOSCH-GLM-rangefinder) | Remote control of the Bosch GLM 100C rangefinder over its Bluetooth serial interface | 67 | 🗄️ | Python |
| [lnDSO150](https://github.com/mean00/lnDSO150) | Alternative firmware for the DSO150 shell oscilloscope | 67 | 🟢 | C++ |
| [HP34401a-OLED-FW](https://github.com/openscopeproject/HP34401a-OLED-FW) | OLED display mod firmware for the HP 34401A multimeter | 66 | 🟢 | C++ |
| [121gw-re](https://github.com/tpwrules/121gw-re) | Reverse engineering the EEVblog 121GW multimeter | 64 | 🔴 | C |
| [fx2lafw](https://github.com/sigrokproject/sigrok-firmware-fx2lafw) | Open firmware for Cypress FX2 logic analyzers, replacing vendor firmware | 63 | 🟡 | C |
| [libseekthermal](https://github.com/ethz-asl/libseekthermal) | Driver library for Seek Thermal imaging devices | 63 | 🔴 | C++ |
| [sds7102](https://github.com/wingel/sds7102) | Port of Linux to the OWON SDS7102 oscilloscope | 57 | 🔴 | Verilog |
| [unit_ut61eplus](https://github.com/ljakob/unit_ut61eplus) | Python access to the UNI-T UT61E+ multimeter via its CP2110 USB interface | 57 | 🔴 | Python |
| [owowon](https://github.com/seritools/owowon) | Oscilloscope UI for OWON HDS portable scopes over USB | 51 | 🟢 | Rust |
| [Bluetooth-DMM](https://github.com/ludwich66/Bluetooth-DMM) | Protocol analysis of Aneng, ZOYI and BSIDE Bluetooth multimeters | 50 | 🟢 |  |
| [um34c](https://github.com/sebastianha/um34c) | NodeJS tool to read and control UM34C/UM24C/UM25C USB testers over Bluetooth | 50 | 🔴 | JavaScript |
| [360nosc0pe](https://github.com/360nosc0pe/scope) | Open FPGA bitstreams for Siglent SDS1x0xX-E oscilloscopes | 49 | 🟡 | Python |
| [ParksideView](https://github.com/bmuessig/ParksideView) | Reads data from Parkside PDM-300-C2/C3 multimeters | 45 | 🟡 | C# |
| [Owon-Multimeters](https://github.com/sercona/Owon-Multimeters) | Linux support for OWON Bluetooth multimeters (B35T+, B41T+, CM2100B, OW18E) | 42 | 🟡 | C |
| [SeekOFix](https://github.com/frenkinet/SeekOFix) | Windows software for Seek Thermal cameras independent of the vendor app | 42 | 🔴 | C# |
| [owon-sds7102-protocol](https://github.com/bjonnh/owon-sds7102-protocol) | GNU/Linux software suite for OWON oscilloscopes over USB | 38 | 🔴 | C |
| [tg165-tools](https://github.com/ktemkin/tg165-tools) | Tools for hacking on and reflashing the FLIR TG165 thermal camera | 37 | 🔴 | C |
| [owonb35](https://github.com/DeanCording/owonb35) | Bluetooth client for the OWON B35 multimeter | 36 | 🔴 | C |
| [p2pro-live](https://github.com/ks00x/p2pro-live) | Web app for a live radiometric stream from the InfiRay P2 Pro thermal camera | 36 | 🟡 | Python |
| [espBode](https://github.com/sq6sfo/espBode) | ESP bridge between a Siglent oscilloscope and an FY6800 AWG for Bode plots | 32 | 🔴 | C++ |
| [Owon-VDS1022 (OS X)](https://github.com/tinwhisker/Owon-VDS1022) | Run the OWON VDS1022 USB oscilloscope on macOS and Linux | 31 | 🔴 | Shell |
| [DSO5102P-Python](https://github.com/titos-carrasco/DSO5102P-Python) | Python access to the Hantek DSO5102P oscilloscope | 27 | 🟡 | Python |
| [BK-390A](https://github.com/inflex/BK-390A) | CLI data capture for BK Precision 390A series multimeters | 26 | 🔴 | C |
| [InfiRayCapture](https://github.com/atomic14/InfiRayCapture) | macOS app for viewing InfiRay P2 Pro thermal camera streams | 25 | 🟢 | Swift |
| [siglent-bin2sr](https://github.com/geekman/siglent-bin2sr) | Converts Siglent SDS1000X-E waveform binaries to sigrok srzip | 25 | 🔴 | Go |
| [yombir](https://github.com/yomboprime/yombir) | Native C++ app for Topdon TC-001 and InfiRay P2 thermal cameras | 24 | 🟡 | C++ |
| [owoncontrol-qt](https://github.com/7oxicshadow/owoncontrol-qt) | Qt USB interface for OWON oscilloscopes | 23 | 🔴 | C++ |
| [ha-radiacode](https://github.com/303Bryan/ha-radiacode) | Home Assistant integration for RadiaCode radiation detectors over BLE | 22 | 🟢 | Python |
| [hantek1008py](https://github.com/mfg92/hantek1008py) | Python driver for the Hantek 1008 USB oscilloscope | 22 | 🟡 | Python |
| [FlirOneControlForLinux](https://github.com/da-nie/FlirOneControlForLinux) | Qt5 libusb app to use the FLIR One thermal camera on Linux | 21 | 🔴 | C |
| [fx2adc](https://github.com/steve-m/fx2adc) | Use Cypress FX2-based USB oscilloscopes (Hantek) as general purpose ADCs | 21 | 🟡 | C |
| [dmm-tools](https://github.com/antoinecellerier/dmm-tools) | Multimeter logging and graphing for UNI-T, ZOYI and other meters on Linux, Windows, macOS | 20 | 🟢 | Rust |
| [Hantek 2D72 tool](https://github.com/lucaoli/Hantek) | Linux tool for the Hantek 2D72 handheld oscilloscope | 20 | 🟢 | C |
| [J7-C_UC96_BLE_Logger](https://github.com/adlerweb/J7-C_UC96_BLE_Logger) | BLE data logging for J7-C and UC96 USB power testers | 20 | 🟡 | Python |
| [pyseek](https://github.com/Fry-kun/pyseek) | Python interface for the Seek Thermal camera | 20 | 🔴 | Python |
| [QtDMM](https://github.com/qtdmm/QtDMM) | Reads, plots and logs digital multimeters over their serial protocols | 20 | 🟢 | C++ |
| [dmm_util](https://github.com/N0ury/dmm_util) | Utility for Fluke 287/289 multimeters: readings, memory and settings | 19 | 🔴 | Python |
| [hantek-365](https://github.com/mp035/hantek-365) | Open GUI and CLI for the Hantek 365 data logger | 19 | 🟢 | JavaScript |
| [HT6022_Driver](https://github.com/rpm2003rpm/HT6022_Driver) | libusb-1.0 based driver for the Hantek 6022 scope | 19 | 🔴 | C |
| [ow](https://github.com/bbum/ow) | macOS and iOS tools for OWON oscilloscopes | 19 | 🟢 | Swift |
| [infiray_irg](https://github.com/jaseg/infiray_irg) | Python module to read InfiRay C200/P200 IRG thermal image files | 18 | 🟢 | Python |
| [idso1070-protocol](https://github.com/hhornbacher/idso1070-protocol) | Reverse engineered protocol for the Hantek iDSO1070 Wi-Fi oscilloscope | 17 | 🗄️ | C++ |
| [OpenP3](https://github.com/Phalphy/OpenP3) | Unofficial Linux driver for the Thermal Master P3 thermal camera | 17 | 🟢 | Python |
| [victor70c](https://github.com/mvneves/victor70c) | Victor 70C multimeter software for Linux | 17 | 🔴 | C |
| [owon_hds200](https://github.com/qwindelzorf/owon_hds200) | Python interface to OWON HDS200 handheld oscilloscopes | 16 | 🔴 | Python |
| [tinySA_python](https://github.com/LC-Linkous/tinySA_python) | Unofficial Python API for the tinySA spectrum analyzer line | 16 | 🟢 | Python |
| [dl24](https://github.com/tshaddack/dl24) | Python control for Atorch DL24P and other electronic loads | 14 | 🟡 | Python |
| [nikon](https://github.com/slietar/nikon) | Python control of the Nikon Ti2-E microscope through its reverse-engineered USB protocol | 6 | 🟡 | Python |
| [minipro-rs](https://gitlab.com/arcturus8081/minipro-rs) | Rust reimplementation of minipro for XGecu TL866/T48/T56/T76 chip programmers |  | ⚪ |  |
| [pockethernet-protocol](https://gitlab.com/MartijnBraam/pockethernet-protocol) | Reverse engineering of the Pockethernet Bluetooth protocol so third-party apps can be written |  | ⚪ |  |

## Laptop EC & Peripherals

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [MonitorControl](https://github.com/MonitorControl/MonitorControl) | macOS app to control external display brightness over DDC | 34,538 | 🟢 | Swift |
| [G-Helper](https://github.com/seerge/g-helper) | Lightweight open replacement for ASUS Armoury Crate laptop control | 15,707 | 🟢 | C# |
| [LibreHardwareMonitor](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor) | Hardware sensor monitor with reverse-engineered Super I/O and EC readers | 9,259 | 🟢 | C# |
| [linux-surface](https://github.com/linux-surface/linux-surface) | Linux kernel and drivers for Microsoft Surface devices | 7,834 | 🟢 | Shell |
| [Lunar](https://github.com/alin23/Lunar) | macOS display brightness controller using DDC and private display APIs | 5,715 | 🟢 | Swift |
| [throttled](https://github.com/erpalma/throttled) | Linux daemon working around Intel firmware-induced throttling on Lenovo and other laptops | 2,995 | 🟢 | Python |
| [RyzenAdj](https://github.com/FlyGoat/RyzenAdj) | Adjust power settings of Ryzen mobile processors via undocumented SMU calls | 2,444 | 🟢 | C |
| [ddcutil](https://github.com/rockowitz/ddcutil) | Query and change monitor settings over DDC/CI and USB MCCS on Linux | 1,420 | 🟢 | C |
| [intel-undervolt](https://github.com/kitsunyan/intel-undervolt) | Undervolting and power-limit tool for Intel CPUs using undocumented MSRs | 1,098 | 🔴 | C |
| [nbfc-linux](https://github.com/nbfc-linux/nbfc-linux) | C port of NoteBook FanControl for Linux using per-model EC register configs | 791 | 🟢 | C |
| [m1ddc](https://github.com/waydabber/m1ddc) | CLI to control external displays via DDC on Apple Silicon Macs | 749 | 🟢 | Objective-C |
| [ddccontrol](https://github.com/ddccontrol/ddccontrol) | Linux DDC/CI monitor control tool with GUI and monitor database | 725 | 🟢 | Rust |
| [thinkfan](https://github.com/vmatare/thinkfan) | Fan control daemon for ThinkPads and other hwmon systems | 716 | 🟢 | C |
| [acer-predator-turbo-and-rgb-keyboard-linux-module](https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module) | Linux module for Acer Predator turbo mode and RGB keyboard | 630 | 🟢 | C |
| [it87](https://github.com/frankcrawford/it87) | Linux driver for ITE Super I/O hardware monitoring chips | 621 | 🟢 | C |
| [ZenStates-Linux](https://github.com/r4m0n/ZenStates-Linux) | Tool to change AMD Zen P-states via MSRs on Linux | 569 | 🟡 | Python |
| [chromebook-linux-audio](https://github.com/WeirdTreeThing/chromebook-linux-audio) | Script that enables audio on many Chromebooks running mainstream Linux distributions | 560 | 🟢 | Shell |
| [snd_hda_macbookpro](https://github.com/davidjo/snd_hda_macbookpro) | Linux audio driver for Cirrus codecs in Intel MacBook Pros | 504 | 🟢 | C |
| [msi-ec](https://github.com/BeardOverflow/msi-ec) | Linux kernel driver for MSI laptop EC features (fans, battery, LEDs) | 500 | 🟢 | C |
| [zenpower](https://github.com/ocerman/zenpower) | Linux hwmon driver for AMD Zen CPU sensors | 491 | 🔴 | C |
| [SMUDebugTool](https://github.com/irusanov/SMUDebugTool) | Windows tool to inspect AMD SMU, PCI and MSR registers | 490 | 🟢 | C# |
| [nct6687d](https://github.com/Fred78290/nct6687d) | Linux driver for Nuvoton NCT6687-R Super I/O sensors | 480 | 🟢 | C |
| [fw-fanctrl](https://github.com/TamtamHero/fw-fanctrl) | Fan curve service for Framework laptops using the EC via ectool | 466 | 🟢 | Python |
| [tpacpi-bat](https://github.com/teleshoes/tpacpi-bat) | ThinkPad battery charge threshold control via undocumented ACPI calls | 455 | 🟡 | Perl |
| [isw (Ice-Sealed Wyvern)](https://github.com/YoyPa/isw) | Fan control for MSI laptops via the embedded controller | 413 | 🔴 | Python |
| [Huawei-WMI](https://github.com/aymanbagabas/Huawei-WMI) | Linux WMI driver for Huawei MateBook hotkeys, battery protection and fn-lock | 287 | 🟢 | C |
| [samsung-galaxybook-extras](https://github.com/joshuagrisham/samsung-galaxybook-extras) | Linux platform driver for Samsung Galaxy Book fan, keyboard backlight and performance modes | 279 | 🟡 | ASL |
| [asus-wmi-sensors](https://github.com/electrified/asus-wmi-sensors) | Linux hwmon driver for ASUS Ryzen/Threadripper motherboard sensors via WMI | 264 | 🔴 | C |
| [ddcui](https://github.com/rockowitz/ddcui) | Qt graphical front end for ddcutil monitor control | 264 | 🟢 | C++ |
| [dell-bios-fan-control](https://github.com/TomFreudenberg/dell-bios-fan-control) | Toggle Dell BIOS fan control via undocumented SMM calls | 256 | 🔴 | C |
| [monitorcontrol (Python)](https://github.com/newAM/monitorcontrol) | Python library for monitor control via DDC/CI on Linux and Windows | 243 | 🟢 | Python |
| [i8kutils](https://github.com/vitorafsr/i8kutils) | Fan and SMM utilities for Dell laptops | 232 | 🔴 | C |
| [galaxy-book2-pro-linux](https://github.com/joshuagrisham/galaxy-book2-pro-linux) | Notes and utilities for Linux on the Samsung Galaxy Book2 Pro | 195 | 🟡 | ASL |
| [zcfan](https://github.com/cdown/zcfan) | Zero-configuration fan daemon for ThinkPads via thinkpad_acpi | 166 | 🟢 | C |
| [samsung-galaxy-book-linux-fixes](https://github.com/Andycodeman/samsung-galaxy-book-linux-fixes) | Linux fixes for Samsung Galaxy Book 3/4/5 webcam, speakers and microphone | 164 | 🟢 | Shell |
| [framework-system](https://github.com/FrameworkComputer/framework-system) | Rust tool and library to talk to the Framework laptop EC and peripherals | 152 | 🟢 | Rust |
| [iptsd](https://github.com/linux-surface/iptsd) | Userspace daemon for Intel Precise Touch & Stylus on Surface devices | 152 | 🟢 | C++ |
| [framework-laptop-kmod](https://github.com/DHowett/framework-laptop-kmod) | Linux kernel module exposing Framework laptop EC features (fans, LEDs, battery) | 148 | 🟡 | C |
| [cros-keyboard-map](https://github.com/WeirdTreeThing/cros-keyboard-map) | Generates keyd configs so Chromebook top-row keys work under normal Linux distros | 140 | 🟢 | Python |
| [mbp2018-bridge-drv](https://github.com/MCMrARM/mbp2018-bridge-drv) | Reverse engineered Apple T2 BCE driver for keyboard, trackpad and audio on 2018+ MacBooks | 138 | 🔴 | C |
| [Reverse_Engineering_BQ20z70_Laptop_BMS](https://github.com/omarKmekkawy/Reverse_Engineering_BQ20z70_Laptop_BMS) | Reverse engineering the BQ20z70 laptop battery management system | 134 | 🔴 | C |
| [zenbook-duo-2024-linux](https://github.com/alesya-h/zenbook-duo-2024-ux8406ma-linux) | Linux support for the ASUS Zenbook Duo 2024 dual screens, keyboard backlight and battery limit | 128 | 🟢 | Shell |
| [tiny-dfr](https://github.com/AsahiLinux/tiny-dfr) | Minimal dynamic function row daemon for the MacBook Touch Bar on Linux | 123 | 🟢 | Rust |
| [dell-powermanager](https://github.com/alexVinarskis/dell-powermanager) | Cross-platform Dell Power Manager reimplementation | 115 | 🟢 | Dart |
| [surface-aggregator-module](https://github.com/linux-surface/surface-aggregator-module) | Linux drivers for the Microsoft Surface System Aggregator Module embedded controller | 106 | 🟡 | C |
| [Open-Source-PC110](https://github.com/ahmadexp/Open-Source-PC110) | Reconstructing the missing technical documentation of the IBM PC110 palmtop | 98 | 🟢 | HTML |
| [asus-fan](https://github.com/daringer/asus-fan) | Linux kernel module to read and set fan speeds on ASUS Zenbooks | 97 | 🗄️ | C |
| [qnap8528](https://github.com/0xGiddi/qnap8528) | Linux kernel module exposing the ITE8528 embedded controller on QNAP devices | 92 | 🟢 | C |
| [IdeapadToolkit](https://github.com/havlif/IdeapadToolkit) | Lightweight Lenovo Vantage alternative for the IdeaPad Flex 5 | 91 | 🟡 | C# |
| [Framework EC (DHowett)](https://github.com/DHowett/framework-ec) | Framework Laptop embedded controller firmware fork with ectool used by fan-control tools | 88 | 🟡 | C |
| [surface-control](https://github.com/linux-surface/surface-control) | CLI to control Surface performance mode, dGPU power and clipboard detach on Linux | 84 | 🟢 | Rust |
| [Galaxy-Book4-Edge-linux](https://github.com/Saddytech/Galaxy-Book4-Edge-linux) | Linux driver and RE tools for the Samsung Galaxy Book4 Edge | 80 | 🟢 | Python |
| [asus-ec-sensors](https://github.com/zeule/asus-ec-sensors) | Linux hwmon driver reading ASUS motherboard sensors from the embedded controller | 78 | 🟢 | C |
| [predator-sense](https://github.com/cleyton1986/predator-sense) | Unofficial Linux hardware control for Acer Predator/Helios/Nitro laptops | 77 | 🟢 | Rust |
| [yogabook-c930-linux-eink-driver](https://github.com/aleksb/yogabook-c930-linux-eink-driver) | Reverse engineered Linux driver for the Lenovo Yoga Book C930 e-ink keyboard | 70 | 🔴 | C |
| [GhostDeck](https://github.com/wygodad/ghostdeck) | Driver-free power and fan control for MSI laptops via EC/WMI | 64 | 🟢 | C# |
| [turbomem](https://github.com/yarrick/turbomem) | Linux driver for the Intel Turbo Memory Controller PCIe card | 60 | 🔴 | C |
| [init-headphone](https://github.com/Unrud/init-headphone) | Initializes the headphone amplifier found in some Clevo laptops on Linux | 57 | 🔴 | M4 |
| [HallMonitor](https://github.com/durka/HallMonitor) | Clean-room Galaxy S4 View Cover driver | 45 | 🔴 | Java |
| [surface-dtx-daemon](https://github.com/linux-surface/surface-dtx-daemon) | Userspace daemon for the Surface Book detachment (DTX) system on Linux | 45 | 🟢 | Rust |
| [qc71_laptop](https://github.com/pobrn/qc71_laptop) | Linux driver for QC71-based (Tongfang/XMG/Eluktronics) laptop EC features | 40 | 🟡 | C |
| [MsiEcRamEditor](https://github.com/timschneeb/MsiEcRamEditor) | Edit and dump MSI laptop EC RAM via ACPI-WMI | 26 | 🔴 | C# |
| [OpenInputBridge](https://github.com/Applet-LLC/OpenInputBridge) | Clean-room, protocol-compatible reimplementation of the Interception keyboard/mouse driver | 25 | 🟢 | C++ |
| [samsung-galaxy-book5-linux-drivers](https://github.com/PsychoPunkSage/samsung-galaxy-book5-linux-drivers) | Linux drivers, hotkey patches and firmware fixes for the Samsung Galaxy Book5 | 20 | 🟢 | C |
| [t2-better-audio](https://github.com/kekrby/t2-better-audio) | Audio configuration files for Apple T2 Macs running Linux | 18 | 🔴 | Shell |
| [LOQ-24-zone-RGB-controller](https://github.com/Dhruvgoel3829/LOQ-24-zone-RGB-controller) | Controller for all 24 RGB zones of Lenovo Legion LOQ keyboards | 16 | 🟢 | Rust |
| [asus-fan-control-ec](https://github.com/Keyitdev/asus-fan-control-ec) | Fan control for ASUS devices on Linux via direct EC access | 13 | 🟢 | C |
| [zenbook-touchpad-i2c](https://github.com/larixer/zenbook-touchpad-i2c) | Reverse-engineered I2C HID protocol of ASUS ZenBook touchpads | 13 | 🔴 | JavaScript |
| [gigactl](https://github.com/smairio/gigactl) | Fan and RGB keyboard control for Gigabyte/Clevo laptops on Linux, reverse-engineered | 9 | 🟢 | Python |
| [TPFanCtrl2](https://github.com/mews-se/TPFanCtrl2) | ThinkPad fan control for Windows 10/11 | 7 | 🟢 | C++ |
| [Mechrevo-Xingyao-14](https://github.com/YMGPwcca/Mechrevo-Xingyao-14) | Reverse-engineering reference for an Insyde BIOS and ITE EC laptop | 6 | 🟢 |  |
| [VSL-DSP](https://github.com/grisuno/VSL-DSP) | Linux kernel module for PreSonus AudioBox VSL USB audio interfaces | 6 | 🟢 | HTML |
| [mipi-fixes-x1-aura](https://github.com/cschalle/mipi-fixes-x1-aura) | Linux camera tuning for the ThinkPad X1 IMX471 sensor, recovered from the Intel Windows driver | 3 | 🟢 | Python |
| [acpi4asus](https://sourceforge.net/projects/acpi4asus/) | ASUS laptop ACPI extras driver and tools for hotkeys, LEDs and backlight |  | ⚪ |  |
| [asusctl](https://gitlab.com/asus-linux/asusctl) | Control daemon for ASUS ROG/TUF laptops on Linux (fans, LEDs, profiles) |  | ⚪ |  |
| [hdaps](https://sourceforge.net/projects/hdaps/) | Driver for the ThinkPad Hard Drive Active Protection System accelerometer |  | ⚪ |  |
| [i8kutils](https://launchpad.net/i8kutils) | Fan control and monitoring utilities for Dell laptops via the SMM BIOS |  | ⚪ |  |
| [ibm-acpi](https://sourceforge.net/projects/ibm-acpi/) | ThinkPad ACPI extras driver, predecessor of the Linux thinkpad_acpi module |  | ⚪ |  |
| [ironkey_lp50_linux](https://codeberg.org/esavier/ironkey_lp50_linux) | Reverse-engineered Linux driver for the IronKey Locker+ LP50 USB drive |  | ⚪ |  |
| [omnibook](https://sourceforge.net/projects/omnibook/) | Kernel module for HP OmniBook, Pavilion and Toshiba laptop hardware features |  | ⚪ |  |
| [tpctl](https://sourceforge.net/projects/tpctl/) | ThinkPad configuration tools using the reverse-engineered SMAPI BIOS interface |  | ⚪ |  |
| [xrite-devel](https://codeberg.org/dach/xrite-devel) | Reverse engineering the X-Rite embedded colour calibration sensor in laptops |  | ⚪ |  |

## Printers, Scanners & Fingerprint

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [python-validity](https://github.com/uunicorn/python-validity) | Reverse-engineered Validity/Synaptics fingerprint sensor driver for ThinkPads | 1,244 | 🟡 | Python |
| [catprinter](https://github.com/rbaron/catprinter) | Prints to cheap BLE "cat" thermal printers via reverse-engineered protocol | 861 | 🟢 | Python |
| [brlaser](https://github.com/pdewacht/brlaser) | Open driver for Brother laser printers that lack PostScript support | 722 | 🔴 | C++ |
| [Epson-Waste-Reset](https://github.com/RxNaison/Epson-Waste-Reset) | Open-source utility to reset Epson printer waste ink pad counters | 408 | 🟢 | C++ |
| [sane-airscan](https://github.com/alexpevzner/sane-airscan) | SANE backend for driverless eSCL and WSD network scanners | 372 | 🟢 | C |
| [goodix-fp-dump](https://github.com/goodix-fp-linux-dev/goodix-fp-dump) | Reverse-engineering tools and prototype drivers for Goodix fingerprint sensors | 363 | 🔴 | Python |
| [node-hp-scan-to](https://github.com/manuc66/node-hp-scan-to) | Enables HP All-in-One scan-to-computer without HP software | 304 | 🟢 | TypeScript |
| [Validity91](https://github.com/hmaarrfk/Validity91) | Reverse engineering the Validity 138a:0091 fingerprint sensor in Dell XPS laptops | 241 | 🔴 | Python |
| [hw-harness](https://github.com/cschalle/hw-harness) | Harness that compares vendor and Linux scanner driver USB control transfers | 223 | 🟢 | Shell |
| [labelle](https://github.com/labelle-org/labelle) | Open print tool for Dymo LabelManager label printers | 191 | 🟢 | Python |
| [hp-laser-1008a-macos](https://github.com/Kuberwastaken/hp-laser-1008a-macos) | Native Apple Silicon macOS driver for HP Laser 1003-1008 printers | 176 | 🟢 | C |
| [libfprint elan](https://github.com/iafilatov/libfprint) | libfprint driver for Elantech fingerprint sensors | 161 | 🔴 | C |
| [synaTudor](https://github.com/Popax21/synaTudor) | Linux libfprint driver for Synaptics Tudor match-in-sensor fingerprint readers | 153 | 🟡 | C |
| [Goodix92](https://github.com/IDerr/Goodix92) | Reverse engineering the Goodix 27c6:5395 fingerprint sensor in Dell XPS 9570 | 104 | 🗄️ |  |
| [brother-in-arms](https://github.com/alexivkin/brother-in-arms) | Brother printer drivers for ARM and Raspberry Pi | 80 | 🟡 | Shell |
| [open-fprintd](https://github.com/uunicorn/open-fprintd) | fprintd replacement allowing standalone backends such as python-validity | 79 | 🟡 | Python |
| [ql570](https://github.com/sudomesh/ql570) | Linux program for Brother QL-570/QL-700 label printers | 62 | 🔴 | C |
| [SpliX](https://github.com/OpenPrinting/splix) | CUPS driver for Samsung/Xerox SPL host-based laser printers | 53 | 🟢 | C++ |
| [CatPrinterBLE](https://github.com/MaikelChan/CatPrinterBLE) | Implementation of the MXW01 cat thermal printer BLE protocol | 49 | 🟡 | C# |
| [PTouchHH](https://github.com/furrtek/PTouchHH) | Brother P-Touch label printer reverse engineering and firmware work | 46 | 🔴 |  |
| [fingerprint-ocv](https://github.com/vrolife/fingerprint-ocv) | Linux driver for the FPC 10a5:9201 fingerprint sensor controller | 42 | 🔴 | C++ |
| [goodix-fingerprint-reversing](https://github.com/tlambertz/goodix-fingerprint-reversing) | Notes and tools from reverse engineering the Goodix 5110 fingerprint reader | 39 | 🔴 | Lua |
| [goodix53x5-libfprint](https://github.com/AndyHazz/goodix53x5-libfprint) | libfprint driver for the Goodix 27c6:5385 fingerprint sensor in the Dell XPS 13 7390 | 38 | 🟢 | C |
| [niimbot-web-bluetooth](https://github.com/iscarelli/niimbot-web-bluetooth) | Web Bluetooth driver and reverse-engineered protocol docs for Niimbot label printers | 36 | 🟢 | JavaScript |
| [elanpoc](https://github.com/depau/elanpoc) | Proof of concept for talking to ELAN 04f3:0c4c fingerprint readers, basis for a libfprint driver | 35 | 🟡 | Python |
| [ft9201-libfprint](https://github.com/OMGrant/ft9201-libfprint) | libfprint driver for the FocalTech FT9201 (2808:93a9) USB fingerprint reader | 27 | 🟢 | C |
| [captppd](https://github.com/darkvision77/captppd) | CUPS driver for Canon CAPT v1 printers | 22 | 🟢 | C++ |
| [linux-fingerprint-drivers](https://github.com/jedbillyb/linux-fingerprint-drivers) | Community hub of drivers and patches for fingerprint sensors not in libfprint | 15 | 🟢 | Python |
| [dell-controlvault2-fingerprint-linux](https://github.com/grosa787/dell-controlvault2-fingerprint-linux) | Linux driver for Dell ControlVault2 / Broadcom BCM5880 fingerprint chip | 12 | 🟢 | Shell |
| [pi-capt](https://github.com/Limych/pi-capt) | Canon LBP CAPT printer driver for Raspberry Pi CUPS | 11 | 🔴 | C |
| [libfprint-egis0576](https://github.com/PHILIPPDEV5396/libfprint-egis0576) | Reverse-engineered libfprint driver for EgisTec EH576 fingerprint sensor | 9 | 🟢 | C |
| [synaTudorMiS](https://github.com/vojtapl/synaTudorMiS) | Development of the synatlsmoc libfprint driver for Synaptics sensors | 9 | 🟢 | Assembly |
| [goodix-spi-protocol](https://github.com/egormanga/goodix-spi-protocol) | Goodix fingerprint scanner SPI protocol tools | 6 | 🔴 | Python |
| [goodix51c0_spi-reversing](https://github.com/lexakimov/goodix51c0_spi-reversing) | Protocol reverse engineering of the Goodix 51C0 SPI fingerprint sensor | 6 | 🟢 | Python |
| [synaptics-00e7-fpdrv](https://github.com/HansHoogerwerf/synaptics-00e7-fpdrv) | From-scratch userspace driver for Synaptics 06cb:00e7 match-on-chip sensor | 6 | 🟢 | C |
| [libfprint](https://gitlab.freedesktop.org/libfprint/libfprint) | Open fingerprint reader library with many reverse-engineered sensor drivers |  | ⚪ |  |
| [m2300w](https://sourceforge.net/projects/m2300w/) | Driver for Minolta magicolor 2300W/2400W/2500W host-based colour lasers |  | ⚪ |  |
| [pnm2ppa](https://sourceforge.net/projects/pnm2ppa/) | Driver for HP PPA (Printing Performance Architecture) host-based DeskJet printers |  | ⚪ |  |
| [SANE backends](https://gitlab.com/sane-project/backends) | SANE scanner backends, many written from reverse-engineered scanner protocols |  | ⚪ |  |
| [ThinkFinger](https://sourceforge.net/projects/thinkfinger/) | Driver for the UPEK/SGS Thomson fingerprint reader found in ThinkPads |  | ⚪ |  |

## Wi-Fi & Radios

| Project | What it does | ★ | Health | Lang |
|---|---|--:|:-:|---|
| [rtl-sdr](https://github.com/osmocom/rtl-sdr) | Turns RTL2832U DVB-T dongles into SDR receivers via reverse-engineered debug mode | 997 | 🟢 | C |
| [esp32-open-mac](https://github.com/esp32-open-mac/esp32-open-mac) | Reverse-engineered open-source Wi-Fi MAC layer for the ESP32 | 859 | 🟡 | C |
| [Hamlib](https://github.com/Hamlib/Hamlib) | Ham radio control library for rigs, rotators and amplifiers using vendor CAT protocols | 855 | 🟢 | C |
| [CHIRP](https://github.com/kk7ds/chirp) | Programming tool for many handheld and mobile radios using reverse engineered cloning protocols | 598 | 🟢 | Python |
| [open-ath9k-htc-firmware](https://github.com/qca/open-ath9k-htc-firmware) | Fully open firmware for Atheros AR9271/AR7010 USB Wi-Fi chips | 485 | 🟡 | C |
| [nexmon_csi](https://github.com/seemoo-lab/nexmon_csi) | Extract Wi-Fi channel state information from Broadcom chips via Nexmon firmware patches | 480 | 🟢 | C |
| [qdmr](https://github.com/hmatuschek/qdmr) | GUI to configure and program cheap DMR radios on Linux and macOS | 359 | 🟢 | C++ |
| [OsmocomBB](https://github.com/osmocom/osmocom-bb) | Free GSM baseband firmware for Calypso-based phones built by reverse engineering | 333 | 🟢 | C |
| [dmrconfig](https://github.com/OpenRTX/dmrconfig) | Configuration utility for DMR radios (TYT, Baofeng, Radioddity) with reverse engineered protocols | 284 | 🟡 | C |
| [bl602-re](https://github.com/pine64/bl602-re) | Reverse engineering of the BL602 Wi-Fi/BLE binary blobs | 105 | 🔴 | Assembly |
| [ESP32-Bluetooth-Reversing](https://github.com/TarlogicSecurity/ESP32-Bluetooth-Reversing) | Reverse engineering of the ESP32 Bluetooth controller | 88 | 🟢 | C |
| [libmirisdr-4](https://github.com/f4exb/libmirisdr-4) | Open driver for Mirics MSi001/MSi2500 SDR dongles (SDRplay-type) | 88 | 🔴 | C |
| [bcm-public](https://github.com/seemoo-lab/bcm-public) | SEEMOO Broadcom Wi-Fi firmware analysis and patching resources | 79 | 🔴 | C |
| [Inside-EZRadioPRO](https://github.com/astuder/Inside-EZRadioPRO) | Reverse engineering the Silabs EZRadioPRO sub-GHz radios | 79 | 🟢 | Rebol |
| [osmo-fl2k](https://github.com/osmocom/osmo-fl2k) | Uses FL2000 USB-to-VGA adapters as cheap SDR transmitters | 59 | 🟢 | C |
| [b43-tools](https://github.com/mbuesch/b43-tools) | b43 firmware tools: fwcutter, assembler and disassembler for Broadcom Wi-Fi microcode | 39 | 🟢 | C |
| [madwimax](https://github.com/ago/madwimax) | Reverse-engineered Linux driver for mobile WiMAX devices on the Samsung CMC-730 chip | 20 | 🔴 | C |
| [acx100](https://sourceforge.net/projects/acx100/) | Linux driver for TI ACX100/ACX111 wireless chipsets |  | ⚪ |  |
| [at76c503a](https://sourceforge.net/projects/at76c503a/) | Linux driver for Atmel at76c503/505 USB wireless adapters |  | ⚪ |  |
| [Broadcom specs (bcm-v4)](https://bcm-v4.sipsolutions.net/) | Clean-room specifications of Broadcom 43xx wireless chips used to write the b43 driver |  | ⚪ |  |
| [libmirisdr](https://gitea.osmocom.org/sdr/libmirisdr) | Software for the Mirics MSi2500 + MSi001 SDR chipset |  | ⚪ |  |
