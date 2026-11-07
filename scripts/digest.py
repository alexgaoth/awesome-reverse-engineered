#!/usr/bin/env python3
"""Weekly digest: what was added, what is rising, what was archived or removed this week.

Usage: digest.py <previous stars.json or ""> <out dir>
Writes <out dir>/notes.md (the release notes) and <out dir>/stars.json (this week's
snapshot, {url: [stars, archived]}), which the next run compares against.
The workflow .github/workflows/digest.yml publishes them as a GitHub Release.
"""
import datetime, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://awesome.alexgaoth.com/"
TODAY = datetime.date.today()
WEEK_AGO = (TODAY - datetime.timedelta(days=7)).isoformat()

prev_path, out = sys.argv[1], sys.argv[2]
entries = json.load(open(os.path.join(ROOT, "data", "entries.json")))
removed = json.load(open(os.path.join(ROOT, "data", "removed.json")))
prev = json.load(open(prev_path)) if prev_path and os.path.exists(prev_path) else {}
pr = os.path.join(ROOT, "data", "resurrected.json")
resurrected = json.load(open(pr)) if os.path.exists(pr) else []

link = lambda e: f"[{e['name'].replace('|', '/')}]({e['url']})"
stars = lambda e: e.get("stars") or 0
first_day = min(e.get("added", "9999") for e in entries)
added = sorted((e for e in entries if e.get("added", "") > WEEK_AGO and e.get("added") != first_day), key=lambda e: -stars(e))
rising = sorted(((stars(e) - prev[e["url"]][0], e) for e in entries if e["url"] in prev),
                key=lambda x: -x[0]) if prev else []
rising = [(d, e) for d, e in rising if d > 0][:15]
archived = [e for e in entries if e.get("archived") and e["url"] in prev and not prev[e["url"]][1]]
gone = [r for r in removed if r.get("removed", "") > WEEK_AGO]

N = []
N += [f"**{len(entries):,} open-source projects built by reverse engineering** · [search]({SITE}) · "
      f"[{len(resurrected)} resurrected products]({SITE}resurrected/)", ""]
if rising:
    N += ["### Rising this week", "", "| Project | ★ gained | ★ | Category |", "|---|--:|--:|---|"]
    N += [f"| {link(e)} | +{d:,} | {stars(e):,} | {e['category']} |" for d, e in rising] + [""]
if added:
    N += [f"### Added this week ({len(added):,})", "", "| Project | What it does | ★ |", "|---|---|--:|"]
    N += [f"| {link(e)} | {(e.get('desc') or '').replace('|', '/')} | {stars(e):,} |" for e in added[:20]]
    if len(added) > 20:
        N += ["", f"…and {len(added) - 20:,} more. See the [search site]({SITE})."]
    N += [""]
if archived or gone:
    N += ["### Archived or removed", ""]
    N += [f"- {link(e)}: archived by its owner" for e in archived[:20]]
    N += [f"- [{r['name']}]({r['url']}): {r.get('reason', 'removed')}" for r in gone[:20]] + [""]
if not (rising or added or archived or gone):
    N += ["A quiet week: no new entries and no changes worth listing.", ""]
N += ["Data: [`data/entries.json`](https://github.com/alexgaoth/awesome-reverse-engineered/blob/main/data/entries.json) (CC0). "
      "Follow these digests with the [releases feed](https://github.com/alexgaoth/awesome-reverse-engineered/releases.atom) "
      "or *Watch → Custom → Releases*."]

os.makedirs(out, exist_ok=True)
open(os.path.join(out, "notes.md"), "w").write("\n".join(N) + "\n")
json.dump({e["url"]: [stars(e), bool(e.get("archived"))] for e in entries}, open(os.path.join(out, "stars.json"), "w"))
print(f"added {len(added)}, rising {len(rising)}, archived {len(archived)}, removed {len(gone)}")
