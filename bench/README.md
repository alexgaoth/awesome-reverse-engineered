# Interop-Bench

Can an agent make working software talk to something closed, using only what an outside engineer has: sample files, traffic captures and a live unit?

That is the work behind most of this index. Interop-Bench measures it on generated targets:

- **The answer exists nowhere.** Each instance comes from a random seed, so it cannot be memorized or found online.
- **Code is scored by running it.** A decoder reads files it has never seen. A client changes the state of a unit it has never seen. No LLM judges anything.
- **The oracle is tested.** A reference solver scores 100%, an empty submission scores 0, and replaying the samples fails.
- **It runs anywhere.** Python standard library only, with no vendor API code.

**Status: pilot.** The results below cover three Claude configurations. This is not a cross-vendor leaderboard. To read the design, the rejected ideas and the kill criteria, see [DESIGN.md](DESIGN.md).

## Pilot results

Runs solved out of runs counted, 2026-11-04. A run counts as solved only if every hidden test passes. The effort in each header is part of the configuration: see finding 2.

| Track | Level | Haiku 5.5 (medium) | Sonnet 5.5 (medium) | Opus 5.5 (xhigh) |
|---|--:|--:|--:|--:|
| Format | 1 | 1/1 | 1/1 | 1/1 |
| Format | 2 | 1/1 | 1/1 | 1/1 |
| Format | 3 | 0/3 | 2/3 | 2/2 |
| Format | 4 | 0/3 | 0/3 | 3/3 |
| Format | 5 | 0/3 | 1/2 | 2/2 |
| Protocol | 1 | 1/1 | 1/1 | 1/1 |
| Protocol | 2 | 1/1 | 1/1 | 1/1 |
| Protocol | 3 | 1/1 | 1/1 | 1/1 |
| Protocol | 4 | 1/1 | 1/1 | 1/1 |
| Protocol | 5 | 2/3 | 3/3 | 3/3 |

Raw rows are in [`results/pilot-2026-11.jsonl`](results/pilot-2026-11.jsonl). Ten runs were excluded for touching a path outside their job folder. All ten solved their task, so excluding them raised no rate: Sonnet on format level 5 would be 4/5 with them. They are in [`results/pilot-2026-11-excluded.jsonl`](results/pilot-2026-11-excluded.jsonl).

## Findings

1. **The format track separated the configurations. The protocol track barely did.** On format, Haiku solved 2 of 11 runs, Sonnet 5 of 10 and Opus 9 of 9. On protocol, all three together solved 20 of 21. Protocol tasks have a live unit that answers, and format tasks have only files. That feedback may explain the gap, but the pilot did not test it, and the protocol levels may simply be easier.
2. **Opus's lead cannot be read as a model result.** Opus ran at xhigh effort, Haiku and Sonnet at medium. These were the defaults in the environment, and nothing corrected for them. Equal effort is the first thing to run next.
3. **Haiku stopped early.** Its unsolved format runs ended after a median of 2.9 minutes of a stated 20. Two of them said they had used the budget, after 2.4 and 3.6 minutes. So these scores measure when an agent gives up, as well as what it can do.
4. **Agents reported their own failures accurately.** Of 15 unsolved runs, 14 said they had failed. One said "about 85%" and crashed on 1 of 25 hidden files. False claims of success were rare in this pilot, so the hidden tests mostly confirmed what agents already said.
5. **Key extraction was removed.** Early versions of protocol levels 4 and 5 needed keys and encryption. Safety systems stopped those runs: one model ended the run, and another was replaced by an older model mid-run. A refusal measures policy, not skill, and the index itself excludes decryption and security bypasses. So the content was removed, not reworded. The final levels had no refusals and no model changes.

## Limits

- **Few runs.** Each cell has 1 to 3 runs. Treat a single solved run as a data point, and treat small differences as noise.
- **Self-graded.** Claude Code built this benchmark, ran it on Claude models and audited the runs. Nobody has checked it independently.
- **Not run through the harness.** The pilot used Claude Code subagents with `serve` mode, because `claude -p` was blocked in that environment. The `claude:` adapter is untested.
- **The budget was stated, not enforced.** Agents read "20 minutes" in the task, but nothing stopped them.
- **Instances are not always paired.** Reruns used new seeds, so two models in a cell did not always see the same instance.
- **Tokens and cost are partial.** Subagent runs report peak context, not total tokens or cost. The median run took 4.2 minutes and peaked at 110k tokens of context, which includes about 70k of startup context. The longest took 19 minutes.
- **Levels are task types, not a strict ladder.** Level 5 is not always harder than level 4.
- **Synthetic is not real.** Targets are modelled on real protocols and formats, but a generated device is simpler and tidier. Results describe this task family.
- **The generator is public from now on.** Pilot agents could not read it, but future agents can learn its mechanism families. Instances stay fresh, and new families can be added per version.

## Run it

Check the oracle. No agent or key is needed:

```bash
python3 -m unittest discover -s bench/tests
python3 bench/run.py one --agent reference --track proto --level 5
```

Run your own agent. The harness starts any shell command in the job folder and puts the prompt at `{prompt}`:

```bash
python3 bench/run.py one --agent 'cmd:your-agent {prompt}' --track fmt --level 3
python3 bench/run.py matrix --agents 'cmd:your-agent {prompt}' --seeds 3 --out mine.jsonl
python3 bench/run.py report mine.jsonl
```

If something else starts your agents, `serve` lays out the job folders, keeps the live units up and scores a folder when a file named `DONE` appears in it:

```bash
python3 bench/run.py serve --agents a,b --tracks fmt --levels 3,4,5 --seeds 2 --root jobs --out mine.jsonl --minutes 20
```

The harness does not sandbox agents. Run untrusted agents in a container or a VM.

## Levels

| Level | Format track | Protocol track |
|--:|---|---|
| 1 | Fixed-size records | Plain frames and a checksum |
| 2 | Tag-length-value records, varints | Length prefix, autokey XOR, sequence numbers |
| 3 | Definition and data messages, like Garmin FIT | Hello, per-session XOR, stamps, CRC, like Xiaomi miIO |
| 4 | Level 3 compressed and obfuscated, delta times, string table | Mostly unlabeled captures, fragments, push telemetry, custom CRC |
| 5 | Write files the hub accepts, which needs a custom CRC | Level 4, with a frame check that exists only as RISC-V machine code in public firmware |

Levels 4 and 5 of the protocol track use no keys and no encryption.
