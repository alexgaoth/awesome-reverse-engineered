#!/usr/bin/env python3
"""Interop-Bench command line. See README.md.

  run.py one --agent claude:claude-sonnet-5-5 --track proto --level 2
  run.py matrix --agents claude:claude-sonnet-5-5,claude:claude-opus-5-5 --seeds 3 --out results/run.jsonl
  run.py report results/run.jsonl
"""
import argparse, json, os, secrets, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from interop_bench import harness
from interop_bench.core import LEVELS

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
sub = ap.add_subparsers(dest="cmd", required=True)
o = sub.add_parser("one")
o.add_argument("--agent", required=True)
o.add_argument("--track", choices=["fmt", "proto"], required=True)
o.add_argument("--level", type=int, choices=LEVELS, required=True)
o.add_argument("--timeout", type=int, default=900)
o.add_argument("--transcripts", default="/tmp/interop-bench-transcripts")
m = sub.add_parser("matrix")
m.add_argument("--agents", required=True)
m.add_argument("--tracks", default="fmt,proto")
m.add_argument("--levels", default="1,2,3,4,5")
m.add_argument("--seeds", type=int, default=3)
m.add_argument("--parallel", type=int, default=3)
m.add_argument("--timeout", type=int, default=900)
m.add_argument("--out", required=True)
m.add_argument("--transcripts", default="/tmp/interop-bench-transcripts")
v = sub.add_parser("serve", help="for agents started by something else: lay out jobs and score each one when DONE appears")
v.add_argument("--agents", required=True)
v.add_argument("--tracks", default="fmt,proto")
v.add_argument("--levels", default="1,2,3,4,5")
v.add_argument("--seeds", type=int, default=1)
v.add_argument("--minutes", type=int, default=15)
v.add_argument("--root", required=True)
v.add_argument("--out", required=True)
r = sub.add_parser("report")
r.add_argument("path")
a = ap.parse_args()

if a.cmd == "one":
    print(json.dumps(harness.run_one(a.agent, a.track, a.level, secrets.token_hex(16), a.timeout, a.transcripts), indent=1))
elif a.cmd == "matrix":
    harness.matrix(a.agents.split(","), a.tracks.split(","), [int(x) for x in a.levels.split(",")], a.seeds,
                   a.parallel, a.timeout, a.out, a.transcripts)
elif a.cmd == "serve":
    harness.serve(a.agents.split(","), a.tracks.split(","), [int(x) for x in a.levels.split(",")], a.seeds, a.root, a.out, a.minutes)
else:
    harness.report(a.path)
