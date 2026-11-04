# Interop-Bench: design and decision record

## The question

Can an agent make working software talk to something closed, using only what an outside engineer would have: samples, traffic captures and a live unit?

This is the work behind most of the index: LocalTuya, python-kasa, python-miio, opendbc, python-fitparse. Existing agent benchmarks measure neighbouring skills on binaries: crackmes (CrackMeBench), malware-style analysis (AgentRE-Bench), crypto (CREBench), function decompilation (DecompileBench and others) and reimplementation from an executable (ProgramBench, Behavior2Code). A search on 2026-11-04 found none that scores protocol or format inference by interoperation.

## Why not matching decompilations

This was the first idea, and it was rejected:

1. **Answers are public.** Decomp repositories are on GitHub, so models may have trained on them. A high score could mean recall, not skill.
2. **Copyright.** Targets are assembly and data from commercial games.
3. **Community.** Many decompilation maintainers oppose AI decompiling, and they are the people this index lists.
4. **It exists.** Projects such as bigyoshi51/decomp already publish results on this.

## Principles

1. **The answer must not exist anywhere.** Every instance is generated from a random seed, so it cannot be memorized or searched. Agents may use any tools, including the network.
2. **Score by interoperation, not explanation.** A decoder is run on unseen files. A client must change the state of a unit it has never seen. No LLM judges anything.
3. **Prove the oracle.** A reference solver must score 100%, an empty submission 0%, and a replay of sample data must fail.
4. **Nothing to steal.** Hidden tests are created after the agent exits. Seeds stay in the harness's memory until scoring.
5. **Runs anywhere.** Python standard library only. No toolchains, binaries, ROMs or copyrighted data.
6. **Any agent.** The harness runs a shell command. It has no vendor API code.

## Levels

| Level | Format track | Modelled on | Protocol track | Modelled on |
|--:|---|---|---|---|
| 1 | Fixed-size records | Sensor logs | Plain frames and checksum | Hobby serial gear |
| 2 | Tag-length-value records, varints, optional fields | Protobuf, BLE advertising data | Length prefix, autokey XOR, sequence numbers | TP-Link Kasa (python-kasa) |
| 3 | Definition and data messages, redefined mid-file | Garmin FIT (python-fitparse) | Hello, per-session XOR from a nonce and unit id, stamps, CRC | Xiaomi miIO (python-miio) |
| 4 | Level 3 compressed and obfuscated, delta times, string table | Vendor export containers | Mostly unlabeled captures, fragmented messages, push telemetry, custom CRC. No keys, no encryption | Real captures |
| 5 | Write direction: produce files the hub accepts, which needs a custom CRC recovered from samples | Vendor import checks | Level 4, but the frame check exists only as generated RISC-V machine code in public firmware. No keys, no encryption | Proprietary checks in firmware |

## Known limits

- **Synthetic is not real.** Mechanisms are modelled on real protocols, but a generated device is simpler and tidier. Results describe this task family.
- **The generator is public.** Agents could learn its mechanism families. These are general reverse-engineering knowledge, and new families can be added per version.
- **Hidden tests are finite.** A pass is evidence of interoperation on the tested distribution, not proof of equivalence.

## Kill criteria (fixed on 2026-11-04, before any model ran)

The pilot is 3 models × 2 tracks × 5 levels × 1 seed. Interop-Bench ships only if all of these hold:

| # | Criterion | Fails if |
|--:|---|---|
| K1 | Oracle valid | Reference is under 100%, empty is over 0%, or replay passes |
| K2 | Reproducible | The same seed gives a different instance |
| K3 | Not saturated | Every model solves every level |
| K4 | Not impossible | No model solves level 1 on both tracks, or no model solves anything above level 1 |
| K5 | Discriminates | All three models score the same on every cell |
| K6 | Affordable | Median run exceeds 25 minutes or 400k tokens |
| K7 | Clean | Any run reads outside its job folder |
| K8 | Measurable | Any model refuses a final level, or is silently replaced by another model (added 2026-11-04, see below) |

If a criterion fails, the code stays unpublished until it is fixed or the idea is dropped.

## Change log before the pilot

An exploratory run of one model on the first four levels (v0.1) changed the design. Its results are not counted.

- **Added level 5.** The model solved most of the ladder quickly, and protocol level 4 fell to debug strings that spell out the crypto. Real machine code and the write direction are what those levels lacked.
- **Fixed a fairness bug.** One agent found an event code in unlabeled samples that no export named, so no solver could have got it. Labeled samples now show every code and flag state, and a test enforces it.

The kill criteria did not change. They now apply to five levels.

A second run (v0.2) changed the design again. Its protocol levels 4 and 5 are not counted; its other cells are, because their code did not change.

- **Removed key extraction and encryption from protocol levels 4 and 5.** Safety systems stopped runs on these levels: one Sonnet 5.5 run ended, and two Opus 5.5 runs fell back to Opus 4.8. A refusal measures policy, not skill. More importantly, the index excludes decryption and security bypasses, so the benchmark should not reward them either. The levels were not reworded to get past a filter: the sensitive content is gone. Their difficulty now comes from messy evidence and from reading a public firmware's integrity check.
- **Added K8.** Refusals are recorded separately and never counted as skill failures. A run must report the model that actually answered, not the one requested.
