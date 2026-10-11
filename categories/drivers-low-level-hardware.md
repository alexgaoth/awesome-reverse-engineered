# Drivers & Low-level Hardware

[← All categories](../README.md) · 119 projects

- [Apple Silicon (Asahi)](#apple-silicon-asahi) (18)
- [Firmware/BIOS (coreboot, UEFI)](#firmwarebios-coreboot-uefi) (19)
- [GPU Drivers](#gpu-drivers) (14)
- [Laptop EC & Peripherals](#laptop-ec--peripherals) (40)
- [Printers, Scanners & Fingerprint](#printers-scanners--fingerprint) (20)
- [Wi-Fi & Radios](#wi-fi--radios) (8)

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
| coreml_to_ane_hwx | Converts Core ML models to Apple Neural Engine HWX binaries for analysis | 51 | <https://github.com/freedomtan/coreml_to_ane_hwx> |
| asahi-scripts | Asahi Linux support scripts (firmware extraction, boot setup) | 50 | <https://github.com/AsahiLinux/asahi-scripts> |
| mdaiter/ane | Reverse-engineering artifacts for Apple ANECompiler, Espresso and AppleNeuralEngine | 40 | <https://github.com/mdaiter/ane> |
| m1-pmu-gen | Generates Linux perf event tables for Apple Silicon PMU counters | 20 | <https://github.com/cyyself/m1-pmu-gen> |
| alsa-ucm-conf-asahi | ALSA UCM configuration for Apple Silicon audio hardware | 7 | <https://github.com/AsahiLinux/alsa-ucm-conf-asahi> |

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
| grate | Reverse-engineering tools and docs for the NVIDIA Tegra 2/3 GPU (open Tegra graphics) | 90 | <https://github.com/grate-driver/grate> |
| mali-isa-docs | Reverse-engineered documentation of Arm Mali GPU shader ISAs | 43 | <https://github.com/cwabbott0/mali-isa-docs> |
| libvdpau-tegra | VDPAU video decode driver for NVIDIA Tegra built from reverse-engineered hardware | 16 | <https://github.com/grate-driver/libvdpau-tegra> |
| etna-gpu-tools | Vivante GPU debugging and reverse-engineering tools from the etnaviv project | 4 | <https://github.com/etnaviv/etna-gpu-tools> |
| Asahi Mesa driver | Mesa OpenGL/Vulkan driver for Apple AGX GPUs, with reverse-engineered ISA notes |  | <https://docs.mesa3d.org/drivers/asahi.html> |
| Freedreno / Turnip | Reverse-engineered Mesa OpenGL and Vulkan drivers for Qualcomm Adreno GPUs |  | <https://docs.mesa3d.org/drivers/freedreno.html> |
| Lima | Reverse-engineered Mesa driver for Arm Mali-400/450 (Utgard) GPUs |  | <https://docs.mesa3d.org/drivers/lima.html> |
| Mesa | Mesa 3D: hosts reverse-engineered GPU drivers (panfrost, lima, freedreno, etnaviv, nouveau, asahi, NVK) |  | <https://gitlab.freedesktop.org/mesa/mesa> |
| Nouveau | Reverse-engineered open-source driver stack for NVIDIA GPUs (kernel DRM + Mesa) |  | <https://nouveau.freedesktop.org> |
| nouveau kernel tree | Nouveau DRM kernel driver development tree for NVIDIA GPUs |  | <https://gitlab.freedesktop.org/drm/nouveau> |
| NVK | Open-source Mesa Vulkan driver for NVIDIA GPUs built on nouveau |  | <https://docs.mesa3d.org/drivers/nvk.html> |
| Panfrost / PanVK | Reverse-engineered Mesa driver for Arm Mali Midgard, Bifrost and Valhall GPUs |  | <https://docs.mesa3d.org/drivers/panfrost.html> |

## Laptop EC & Peripherals

| Name | What it is | ★ | Repo |
|---|---|--:|---|
| MonitorControl | macOS app to control external display brightness over DDC | 34,439 | <https://github.com/MonitorControl/MonitorControl> |
| G-Helper | Lightweight open replacement for ASUS Armoury Crate laptop control | 15,531 | <https://github.com/seerge/g-helper> |
| LibreHardwareMonitor | Hardware sensor monitor with reverse-engineered Super I/O and EC readers | 9,183 | <https://github.com/LibreHardwareMonitor/LibreHardwareMonitor> |
| linux-surface | Linux kernel and drivers for Microsoft Surface devices | 7,781 | <https://github.com/linux-surface/linux-surface> |
| Lunar | macOS display brightness controller using DDC and private display APIs | 5,717 | <https://github.com/alin23/Lunar> |
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
| snd_hda_macbookpro | Linux audio driver for Cirrus codecs in Intel MacBook Pros | 500 | <https://github.com/davidjo/snd_hda_macbookpro> |
| msi-ec | Linux kernel driver for MSI laptop EC features (fans, battery, LEDs) | 494 | <https://github.com/BeardOverflow/msi-ec> |
| SMUDebugTool | Windows tool to inspect AMD SMU, PCI and MSR registers | 489 | <https://github.com/irusanov/SMUDebugTool> |
| zenpower | Linux hwmon driver for AMD Zen CPU sensors | 489 | <https://github.com/ocerman/zenpower> |
| nct6687d | Linux driver for Nuvoton NCT6687-R Super I/O sensors | 474 | <https://github.com/Fred78290/nct6687d> |
| fw-fanctrl | Fan curve service for Framework laptops using the EC via ectool | 464 | <https://github.com/TamtamHero/fw-fanctrl> |
| tpacpi-bat | ThinkPad battery charge threshold control via undocumented ACPI calls | 454 | <https://github.com/teleshoes/tpacpi-bat> |
| isw (Ice-Sealed Wyvern) | Fan control for MSI laptops via the embedded controller | 414 | <https://github.com/YoyPa/isw> |
| ddcui | Qt graphical front end for ddcutil monitor control | 263 | <https://github.com/rockowitz/ddcui> |
| dell-bios-fan-control | Toggle Dell BIOS fan control via undocumented SMM calls | 258 | <https://github.com/TomFreudenberg/dell-bios-fan-control> |
| monitorcontrol (Python) | Python library for monitor control via DDC/CI on Linux and Windows | 244 | <https://github.com/newAM/monitorcontrol> |
| i8kutils | Fan and SMM utilities for Dell laptops | 235 | <https://github.com/vitorafsr/i8kutils> |
| zcfan | Zero-configuration fan daemon for ThinkPads via thinkpad_acpi | 165 | <https://github.com/cdown/zcfan> |
| iptsd | Userspace daemon for Intel Precise Touch & Stylus on Surface devices | 152 | <https://github.com/linux-surface/iptsd> |
| framework-laptop-kmod | Linux kernel module exposing Framework laptop EC features (fans, LEDs, battery) | 148 | <https://github.com/DHowett/framework-laptop-kmod> |
| framework-system | Rust tool and library to talk to the Framework laptop EC and peripherals | 147 | <https://github.com/FrameworkComputer/framework-system> |
| Framework EC (DHowett) | Framework Laptop embedded controller firmware fork with ectool used by fan-control tools | 88 | <https://github.com/DHowett/framework-ec> |
| GhostDeck | Driver-free power and fan control for MSI laptops via EC/WMI | 58 | <https://github.com/wygodad/ghostdeck> |
| qc71_laptop | Linux driver for QC71-based (Tongfang/XMG/Eluktronics) laptop EC features | 40 | <https://github.com/pobrn/qc71_laptop> |
| MsiEcRamEditor | Edit and dump MSI laptop EC RAM via ACPI-WMI | 25 | <https://github.com/timschneeb/MsiEcRamEditor> |
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
| labelle | Open print tool for Dymo LabelManager label printers | 189 | <https://github.com/labelle-org/labelle> |
| libfprint elan | libfprint driver for Elantech fingerprint sensors | 161 | <https://github.com/iafilatov/libfprint> |
| synaTudor | Linux libfprint driver for Synaptics Tudor match-in-sensor fingerprint readers | 152 | <https://github.com/Popax21/synaTudor> |
| SpliX | CUPS driver for Samsung/Xerox SPL host-based laser printers | 51 | <https://github.com/OpenPrinting/splix> |
| goodix-fingerprint-reversing | Notes and tools from reverse engineering the Goodix 5110 fingerprint reader | 39 | <https://github.com/tlambertz/goodix-fingerprint-reversing> |
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
| open-ath9k-htc-firmware | Fully open firmware for Atheros AR9271/AR7010 USB Wi-Fi chips | 484 | <https://github.com/qca/open-ath9k-htc-firmware> |
| nexmon_csi | Extract Wi-Fi channel state information from Broadcom chips via Nexmon firmware patches | 475 | <https://github.com/seemoo-lab/nexmon_csi> |
| OsmocomBB | Free GSM baseband firmware for Calypso-based phones built by reverse engineering | 333 | <https://github.com/osmocom/osmocom-bb> |
| bcm-public | SEEMOO Broadcom Wi-Fi firmware analysis and patching resources | 79 | <https://github.com/seemoo-lab/bcm-public> |
| osmo-fl2k | Uses FL2000 USB-to-VGA adapters as cheap SDR transmitters | 58 | <https://github.com/osmocom/osmo-fl2k> |
| b43-tools | b43 firmware tools: fwcutter, assembler and disassembler for Broadcom Wi-Fi microcode | 39 | <https://github.com/mbuesch/b43-tools> |
