#!/usr/bin/env python3
"""Render README.md and categories/*.md from data/entries.json.

Run from anywhere: python3 scripts/render.py
"""
import collections, datetime, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDER = ["Collections & Awesome Lists", "AI Tools & LLM Clients", "Game Decompilations & Reimplementations",
         "Messaging & Social Apps", "Unofficial Web/App API Clients", "Chinese & Asian Platforms", "Alternative Frontends",
         "Mobile Apps", "Apple Ecosystem", "Devices, IoT & Hardware", "Drivers & Low-level Hardware", "Automotive",
         "Firmware & Embedded", "Network & Wire Protocols", "File Formats", "Desktop Software Reimplementations", "RE Tooling"]

slug = lambda s: re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")
anchor = lambda s: re.sub(r"[^\w\- ]", "", s.lower()).replace(" ", "-")  # GitHub heading-anchor rule


def table(rows):
    out = ["| Name | What it is | ★ | Repo |", "|---|---|--:|---|"]
    for e in sorted(rows, key=lambda e: (-(e.get("stars") or 0), e["name"].lower())):
        d = e.get("desc", "").replace("|", "\\|").replace("\n", " ")
        st = f"{e['stars']:,}" if e.get("stars") is not None else ""
        arch = " *(archived)*" if e.get("archived") else ""
        out.append(f"| {e['name'].replace('|', '/')}{arch} | {d} | {st} | <{e['url']}> |")
    return out


def main():
    entries = json.load(open(os.path.join(ROOT, "data", "entries.json")))
    by = collections.defaultdict(lambda: collections.defaultdict(list))
    for e in entries:
        by[e["category"]][e.get("subcategory") or "Other"].append(e)
    cats = [c for c in ORDER if c in by] + sorted(c for c in by if c not in ORDER)
    today = datetime.date.today().isoformat()
    cdir = os.path.join(ROOT, "categories")
    os.makedirs(cdir, exist_ok=True)
    for f in os.listdir(cdir):
        os.remove(os.path.join(cdir, f))

    readme = ["# Awesome Reverse-Engineered", "",
      "An index of open-source tools, clients, SDKs, drivers and reimplementations that exist because someone **reverse engineered** "
      "a closed app, API, protocol, file format, device, game or AI tool.", "",
      f"**{len(entries):,} projects** in {len(cats)} categories · updated {today} · sorted by GitHub stars inside each section. "
      "Stars, archived state and dead links are refreshed nightly.", "",
      "Scope: interoperability, preservation and research. Exploits, jailbreaks, cheats, DRM removal and credential tools are left out on purpose.", "",
      "## Use it from an AI agent", "",
      "The repo is also a Claude Code plugin with one skill, [`find-reverse-engineered`](skills/find-reverse-engineered/SKILL.md). "
      "When a task needs to talk to a closed app, device, API or file format, the agent searches this index and picks a project by stars, "
      "language, license and recent activity. It then reads the README or clones the project.", "",
      "```", "/plugin install reverse-engineered --marketplace alexgaoth/awesome-reverse-engineered", "```", "",
      "Any other agent or shell can use the same search script. It has no dependencies:", "",
      "```bash",
      "curl -sL https://raw.githubusercontent.com/alexgaoth/awesome-reverse-engineered/main/skills/find-reverse-engineered/scripts/re_index.py -o re_index.py",
      "python3 re_index.py search tuya local          # ranked matches",
      "python3 re_index.py info make-all/tuya-local   # entry + README excerpt",
      "python3 re_index.py clone make-all/tuya-local  # shallow clone into vendor/",
      "```", "",
      "## Categories", "", "| Category | Projects | Subcategories |", "|---|--:|---|"]
    for c in cats:
        n = sum(len(v) for v in by[c].values())
        f = f"categories/{slug(c)}.md"
        subs = sorted(by[c], key=lambda s: -len(by[c][s]))
        base, first = collections.Counter(), {}
        for s in subs:
            base[s.split(" — ")[0]] += len(by[c][s])
        for s in sorted(subs):
            first.setdefault(s.split(" — ")[0], s)
        readme.append(f"| [{c}]({f}) | {n:,} | " + ", ".join(f"[{b}]({f}#{anchor(first[b])})" for b, _ in base.most_common()) + " |")
        page = [f"# {c}", "", f"[← All categories](../README.md) · {n:,} projects", ""]
        if len(subs) > 1:
            page += [f"- [{s}](#{anchor(s)}) ({len(by[c][s])})" for s in sorted(subs)] + [""]
        for s in sorted(subs):
            if len(subs) > 1:
                page += [f"## {s}", ""]
            page += table(by[c][s]) + [""]
        open(os.path.join(ROOT, f), "w").write("\n".join(page))
    top = sorted((e for e in entries if e.get("stars")), key=lambda e: -e["stars"])[:25]
    readme += ["", "## Top 25 by stars", ""] + table(top)
    readme += ["", "## How this list is built", "",
      "Research agents (Claude) search GitHub, awesome-lists, Hacker News (Algolia API), Reddit and the web in rounds. "
      "Each repo is checked against the GitHub API (it exists, canonical URL, stars, archived flag), duplicates are removed by URL, "
      "and the list is regenerated. A [nightly workflow](.github/workflows/refresh.yml) refreshes stars and archived state and removes "
      "repos that no longer exist (logged in [`data/removed.json`](data/removed.json)). "
      "The raw data is in [`data/entries.json`](data/entries.json); imported lists and search queries are in [SOURCES.md](SOURCES.md).", "",
      "Corrections and additions are welcome — open an issue or PR.", "", "## License", "",
      "[CC0 1.0](LICENSE) — the list itself; each linked project has its own license.", ""]
    open(os.path.join(ROOT, "README.md"), "w").write("\n".join(readme))
    print(f"rendered {len(entries)} entries, {len(cats)} category pages")


if __name__ == "__main__":
    main()
