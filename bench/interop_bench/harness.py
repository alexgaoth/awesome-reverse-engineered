"""Run one agent on one instance, then score its work against hidden tests.

Hidden tests are generated only after the agent has exited, and the live unit's secrets exist only
in this process's memory. The seed is never on disk or in argv during a run, so there is nothing to
find. The agent may use any tools it likes, including the network: the instance is new, so the
answer does not exist anywhere.
"""
import json, os, platform, random, re, secrets, shutil, signal, subprocess, sys, tempfile, threading, time
from concurrent.futures import ThreadPoolExecutor
from . import fmt, proto
from .core import VERSION

BENCH_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPT = "Read TASK.md in the current directory and do the job it describes. Work only in this directory."

FMT_TASK = """# Job: read this vendor's log files

A smart-home hub exports its logs in an undocumented binary format. The vendor has no public spec, and no library for it exists.

- `samples/*.bin` are real log files from the hub.
- `samples/*.export.json` show what the vendor's app displays for some of them.

Write `decode.py` in this directory. `python3 decode.py PATH` must print one JSON document for the log file at PATH, in exactly the same structure as the exports (same keys, same types, same units).

It will be checked against log files you have not seen, from the same hub. Use only the Python standard library in `decode.py`. You have about {minutes} minutes.
"""

WRITE_TASK = """# Job: write files this hub will accept

A smart-home hub exports its logs in an undocumented binary format, and it can import the same format again. It refuses any file that fails its integrity checks. The vendor has no public spec, and no library for it exists.

- `samples/*.bin` are real log files from the hub.
- `samples/*.export.json` show what the vendor's app displays for some of them.

Write `encode.py` in this directory. `python3 encode.py IN.json OUT.bin` must read a document in exactly the structure of the exports and write a log file that the hub accepts and that displays the same values.

It will be checked by importing files you produce into the hub, for documents you have not seen. Use only the Python standard library in `encode.py`. You have about {minutes} minutes.
"""

PROTO_TASK = """# Job: control this device locally

A smart thermostat only talks to its vendor's app, over an undocumented local protocol. The vendor has no public spec, and no library for it exists.

- `capture.txt` holds traffic between the app and two units. Annotations show what the user did and what the app showed, where they were recorded.{extra}
- A live unit is listening at 127.0.0.1:{port}. You can talk to it as much as you like.

Write `client.py` in this directory:

    python3 client.py --port PORT status          prints JSON: {{"power": true, "temp": 21.5, "mode": "eco", "name": "den"}}
    python3 client.py --port PORT set_power on|off
    python3 client.py --port PORT set_temp 21.5
    python3 client.py --port PORT set_mode eco
    python3 client.py --port PORT rename NAME

Each call opens its own connection. It will be checked against a different unit of the same model, whose identity and state differ. Use only the Python standard library in `client.py`. You have about {minutes} minutes.
"""


def prepare(track, level, seed, minutes, work=None):
    work = work or tempfile.mkdtemp(prefix="job-")
    live = None
    if track == "fmt":
        _, files = fmt.instance(seed, level)
        task = (WRITE_TASK if level == 5 else FMT_TASK).format(minutes=minutes)
    else:
        _, files = proto.instance(seed, level)
        live = proto.Live(proto.live_unit(seed, level, "public"))
        extra = "\n- `firmware.bin` is the vendor's public firmware image for this model. The chip is a little-endian RV32IM core." if level == 5 else ""
        task = PROTO_TASK.format(minutes=minutes, port=live.port, extra=extra)
    for name, data in files.items():
        path = os.path.join(work, name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "wb").write(data)
    open(os.path.join(work, "TASK.md"), "w").write(task)
    return work, live


def _run(argv, cwd, timeout=20):
    try:
        p = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout
    except (subprocess.TimeoutExpired, OSError):
        return -1, ""


def score_fmt(seed, level, work):
    tmp = tempfile.mkdtemp(prefix="check-")
    scores = []
    spec = fmt.Spec(seed, level)
    try:
        for i, (data, expected) in enumerate(fmt.hidden_tests(seed, level)):
            path = os.path.join(tmp, f"t{i}.bin")
            if level == 5:  # the hub imports what the agent wrote; a refused file scores nothing
                src = os.path.join(tmp, f"t{i}.json")
                open(src, "w").write(json.dumps(expected))
                rc, _ = _run([sys.executable, "encode.py", src, path], work)
                try:
                    got = spec.validate(open(path, "rb").read())
                except Exception:
                    got, rc = None, 1
                scores.append(fmt.score_doc(expected, got) if rc == 0 else 0.0)
                continue
            open(path, "wb").write(data)
            rc, out = _run([sys.executable, "decode.py", path], work)
            try:
                got = json.loads(out)
            except ValueError:
                got = None
            scores.append(fmt.score_doc(expected, got) if rc == 0 else 0.0)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return sum(scores) / len(scores), sum(s == 1.0 for s in scores) == len(scores)


def _target(op, r):
    """The field an operation should change, its wanted value, and a different valid value."""
    v = op[-1]
    if op[0] == "set_power":
        return "power", v == "on", v != "on"
    if op[0] == "set_temp":
        return "temp", float(v), float(v) + 1
    if op[0] == "set_mode":
        return "mode", v, r.choice([m for m in proto.MODES if m != v])
    return "name", v, v + "x"


def score_proto(seed, level, work):
    dev = proto.live_unit(seed, level, "hidden")
    live = proto.Live(dev)
    r = random.Random(f"{seed}:flip")
    ok = 0
    ops = proto.hidden_ops(seed, level)
    try:
        for op in ops:
            st = dev.state
            if op[0] != "status":  # move the field first, so a client that does nothing cannot score
                key, want, moved = _target(op, r)
                st[key] = moved
            rc, out = _run([sys.executable, "client.py", "--port", str(live.port), *op], work)
            if op[0] == "status":
                try:
                    got = json.loads(out)
                    ok += rc == 0 and set(got) == set(st) and all(fmt.same(st[k], got[k]) for k in st)
                except (ValueError, TypeError):
                    pass
            else:
                ok += rc == 0 and fmt.same(st[key], want)
    finally:
        live.close()
    return ok / len(ops), ok == len(ops)


def install_reference(track, level, seed, work):
    """Test double: a perfect solution that reads the secret spec. Proves the scorer can reach 100%."""
    head = f"import json, random, sys\nsys.path.insert(0, {BENCH_DIR!r})\n"
    if track == "fmt" and level == 5:
        src = head + (f"from interop_bench import fmt\nspec = fmt.Spec({seed!r}, 5)\ndoc = json.load(open(sys.argv[1]))\n"
                      "open(sys.argv[2], 'wb').write(spec.encode(spec.unshow(doc), random.Random()))\n")
        open(os.path.join(work, "encode.py"), "w").write(src)
    elif track == "fmt":
        src = head + f"from interop_bench import fmt\nprint(json.dumps(fmt.Spec({seed!r}, {level}).decode(open(sys.argv[1], 'rb').read())))\n"
        open(os.path.join(work, "decode.py"), "w").write(src)
    else:
        src = head + (f"from interop_bench import proto\nspec = proto.Spec({seed!r}, {level})\n"
                      "sock, c = proto.tcp_client(spec, int(sys.argv[2]), random.Random())\n"
                      "out = getattr(c, sys.argv[3])(*sys.argv[4:])\nif out: print(json.dumps(out))\n")
        open(os.path.join(work, "client.py"), "w").write(src)


def install_replay(track, work, level=1):
    """Test double: a cheater that replays captured or sample data. Must not score well."""
    if track == "fmt" and level == 5:
        src = "import glob, shutil, sys\nshutil.copy(sorted(glob.glob('samples/*.bin'))[0], sys.argv[2])\n"
        open(os.path.join(work, "encode.py"), "w").write(src)
    elif track == "fmt":
        src = ("import glob, sys\nprint(open(sorted(glob.glob('samples/*.export.json'))[0]).read())\n")
        open(os.path.join(work, "decode.py"), "w").write(src)
    else:
        src = ("import json, sys\nif sys.argv[3] == 'status':\n    print(json.dumps({'power': True, 'temp': 21.5, 'mode': 'eco', 'name': 'den'}))\n")
        open(os.path.join(work, "client.py"), "w").write(src)


def agent_argv(agent):
    if agent.startswith("claude:"):
        return ["claude", "-p", PROMPT, "--model", agent.split(":", 1)[1], "--output-format", "stream-json", "--verbose",
                "--no-session-persistence", "--strict-mcp-config", "--setting-sources", "project",
                "--tools", "Bash,Read,Write,Edit,Glob,Grep",
                "--allowedTools", "Read,Write,Edit,Glob,Grep,Bash(python3:*),Bash(xxd:*),Bash(hexdump:*),Bash(od:*),Bash(ls:*),Bash(cat:*),Bash(head:*),Bash(tail:*),Bash(strings:*),Bash(grep:*),Bash(wc:*),Bash(file:*),Bash(sed:*),Bash(sort:*),Bash(diff:*),Bash(cmp:*)"]
    if agent.startswith("cmd:"):  # any other agent: cmd:codex exec {prompt}
        return ["/bin/sh", "-c", agent[4:].replace("{prompt}", "'" + PROMPT + "'")]
    raise ValueError(agent)


def run_agent(agent, work, timeout, transcript):
    env = {k: v for k, v in os.environ.items() if not k.startswith(("CLAUDECODE", "CLAUDE_CODE_", "BENCH"))}
    t0 = time.time()
    with open(transcript, "w") as log:
        p = subprocess.Popen(agent_argv(agent), cwd=work, env=env, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        timed_out = False
        try:
            p.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(p.pid, signal.SIGKILL)
            p.wait()
    return {"seconds": round(time.time() - t0, 1), "timed_out": timed_out, "exit": p.returncode}


def read_transcript(path):
    """Cost, turns and a contamination audit from a Claude Code stream-json transcript."""
    meta, tools, suspect, refused, models = {}, 0, [], False, set()
    for line in open(path, errors="replace"):
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        if ev.get("type") == "result":
            u = ev.get("usage") or {}
            meta = {"cost_usd": ev.get("total_cost_usd"), "turns": ev.get("num_turns"), "subtype": ev.get("subtype"),
                    "output_tokens": u.get("output_tokens")}
        elif ev.get("type") == "assistant":
            refused = refused or (ev.get("message") or {}).get("stop_reason") == "refusal"
            models.add((ev.get("message") or {}).get("model"))
            for c in (ev.get("message") or {}).get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_use":
                    tools += 1
                    text = json.dumps(c.get("input"))
                    if re.search(r"interop_bench|awesome-reverse-engineered|bench/", text):
                        suspect.append(text[:200])
    return dict(meta, tool_calls=tools, suspect=suspect, refused=refused, models=sorted(m for m in models if m))


def run_one(agent, track, level, seed, timeout, outdir):
    """One agent on one instance. Returns the result record."""
    minutes = max(1, timeout // 60)
    work, live = prepare(track, level, seed, minutes)
    rec = {"bench": VERSION, "agent": agent, "track": track, "level": level, "python": platform.python_version()}
    try:
        if agent == "null":
            run = {"seconds": 0, "timed_out": False, "exit": 0}
        elif agent == "reference":
            install_reference(track, level, seed, work)
            run = {"seconds": 0, "timed_out": False, "exit": 0}
        elif agent == "replay":
            install_replay(track, work, level)
            run = {"seconds": 0, "timed_out": False, "exit": 0}
        else:
            os.makedirs(outdir, exist_ok=True)
            transcript = os.path.join(outdir, f"{agent.split(':')[-1]}-{track}{level}-{seed[:8]}.jsonl")
            run = run_agent(agent, work, timeout, transcript)
            run.update(read_transcript(transcript))
        if live:
            live.close()
            live = None
        score, solved = (score_fmt if track == "fmt" else score_proto)(seed, level, work)
        rec.update(run, score=round(score, 4), solved=bool(solved), seed=seed)  # the seed is revealed only now
    finally:
        if live:
            live.close()
        shutil.rmtree(work, ignore_errors=True)
    return rec


def matrix(agents, tracks, levels, seeds, parallel, timeout, out, outdir):
    """Every agent gets the same seeds, so results compare pair by pair."""
    plan = [(t, l, secrets.token_hex(16)) for t in tracks for l in levels for _ in range(seeds)]
    jobs = [(a, *p) for a in agents for p in plan]
    lock = threading.Lock()

    def go(job):
        a, t, l, s = job
        try:
            rec = run_one(a, t, l, s, timeout, outdir)
        except Exception as ex:  # one broken run must not stop the matrix
            rec = {"agent": a, "track": t, "level": l, "seed": s, "error": repr(ex), "score": 0.0, "solved": False}
        with lock:
            with open(out, "a") as f:
                f.write(json.dumps(rec) + "\n")
            print(f"{a} {t}{l}: score {rec['score']} solved {rec['solved']} {rec.get('seconds', '?')}s ${rec.get('cost_usd', '?')}", flush=True)
    with ThreadPoolExecutor(parallel) as pool:
        list(pool.map(go, jobs))


def serve(agents, tracks, levels, seeds, root, out, minutes):
    """For agents this harness cannot start itself. Lays out one folder per job, keeps the live units
    up, and scores a folder once a file named DONE appears in it. Seeds stay in this process's memory
    until a job is scored, and every agent gets the same seeds."""
    plan = [(t, l, i, secrets.token_hex(16)) for t in tracks for l in levels for i in range(seeds)]
    jobs = {}
    for a in agents:
        for t, l, i, s in plan:
            work = os.path.join(root, f"{a}-{t}{l}-{i}")
            os.makedirs(work, exist_ok=True)
            _, live = prepare(t, l, s, minutes, work)
            jobs[work] = (a, t, l, s, live)
    print(f"ready: {len(jobs)} jobs in {root}", flush=True)
    while jobs:
        for work in [w for w in jobs if os.path.exists(os.path.join(w, "DONE"))]:
            a, t, l, s, live = jobs.pop(work)
            if live:
                live.close()
            score, solved = (score_fmt if t == "fmt" else score_proto)(s, l, work)
            rec = {"bench": VERSION, "agent": a, "track": t, "level": l, "score": round(score, 4), "solved": bool(solved), "seed": s,
                   "python": platform.python_version()}
            with open(out, "a") as f:
                f.write(json.dumps(rec) + "\n")
            print(f"{a} {t}{l}: score {rec['score']} solved {rec['solved']}", flush=True)
        time.sleep(3)


def report(path):
    rows = [json.loads(x) for x in open(path)]
    key = lambda r: (r["track"], r["level"], r["agent"])
    groups = {}
    for r in rows:
        groups.setdefault(key(r), []).append(r)
    med = lambda v: sorted(v)[len(v) // 2] if v else None
    print("| Track | Level | Agent | Solved | Refused | Mean score | Median minutes | Median cost |\n|---|--:|---|--:|--:|--:|--:|--:|")
    for k in sorted(groups):
        refused = sum(bool(r.get("refused")) for r in groups[k])
        g = [r for r in groups[k] if not r.get("refused")] or groups[k]  # a refusal is not a failure of skill
        solved = sum(r["solved"] for r in g)
        mean = sum(r["score"] for r in g) / len(g)
        mins = med([r["seconds"] / 60 for r in g if "seconds" in r])
        cost = med([r["cost_usd"] for r in g if r.get("cost_usd") is not None])
        print(f"| {k[0]} | {k[1]} | {k[2].split(':')[-1]} | {solved}/{len(g)} | {refused} | {mean:.2f} | "
              f"{'' if mins is None else f'{mins:.1f}'} | {'' if cost is None else f'${cost:.2f}'} |")
    flagged = [r for r in rows if r.get("suspect")]
    swapped = [r for r in rows if len(r.get("models", [])) > 1]  # a refusal can silently change the model mid-run
    print(f"\nRuns: {len(rows)}. Timed out: {sum(bool(r.get('timed_out')) for r in rows)}. Errors: {sum('error' in r for r in rows)}. "
          f"Flagged by audit: {len(flagged)}. Model replaced mid-run: {len(swapped)}.")
