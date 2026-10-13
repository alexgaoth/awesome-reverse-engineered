#!/usr/bin/env python3
"""Render README.md, categories/*.md, assets/*.svg and docs/data.json from data/entries.json.

Run from anywhere: python3 scripts/render.py
"""
import collections, datetime, html, importlib.util, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = "alexgaoth/awesome-reverse-engineered"
SITE = "https://alexgaoth.github.io/awesome-reverse-engineered/"
TODAY = datetime.date.today()

# Category order and icon. Categories not listed here go last, sorted by name.
CATS = [
    ("AI Tools & LLM Clients", "🤖"), ("Game Decompilations & Reimplementations", "🎮"),
    ("Devices, IoT & Hardware", "📡"), ("Unofficial Web/App API Clients", "🔌"),
    ("Messaging & Social Apps", "💬"), ("Third-party Clients", "🧩"),
    ("Chinese & Asian Platforms", "🌏"), ("Apple Ecosystem", "🍎"),
    ("Drivers & Low-level Hardware", "🖥️"), ("Automotive", "🚗"),
    ("Industrial & Building Automation", "🏭"), ("Firmware & Embedded", "💾"),
    ("Network & Wire Protocols", "🌐"), ("File Formats", "📄"),
    ("Online Service Revivals", "🔁"), ("Desktop Software Reimplementations", "🧱"),
    ("Alternative Frontends", "🪞"), ("Mobile Apps", "📱"),
    ("RE Tooling", "🛠️"), ("Collections & Awesome Lists", "📚"),
]
ICON = dict(CATS)
ORDER = [c for c, _ in CATS]

slug = lambda s: re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")
anchor = lambda s: re.sub(r"[^\w\- ]", "", s.lower()).replace(" ", "-")  # GitHub heading-anchor rule
esc = lambda s: html.escape(s or "", quote=True)


def health(e):
    """active / slow / dormant / archived / unknown, from the archived flag and last push date."""
    if e.get("archived"):
        return "archived"
    p = e.get("pushed")
    if not p:
        return "unknown"
    days = (TODAY - datetime.date.fromisoformat(p)).days
    return "active" if days <= 365 else "slow" if days <= 1095 else "dormant"


HEALTH_MD = {"active": "🟢", "slow": "🟡", "dormant": "🔴", "archived": "🗄️", "unknown": "⚪"}


def table(rows, numbered=False):
    head = ("| # " if numbered else "") + "| Project | What it does | ★ | Health | Lang |"
    sep = ("|--:" if numbered else "") + "|---|---|--:|:-:|---|"
    out = [head, sep]
    for i, e in enumerate(sorted(rows, key=lambda e: (-(e.get("stars") or 0), e["name"].lower())), 1):
        d = (e.get("desc") or "").replace("|", "\\|").replace("\n", " ")
        st = f"{e['stars']:,}" if e.get("stars") is not None else ""
        name = f"[{e['name'].replace('|', '/')}]({e['url']})"
        out.append((f"| {i} " if numbered else "") + f"| {name} | {d} | {st} | {HEALTH_MD[health(e)]} | {e.get('lang') or ''} |")
    return out


def load_search():
    """Reuse the skill's ranking so the README demo shows real search output."""
    p = os.path.join(ROOT, "skills", "find-reverse-engineered", "scripts", "re_index.py")
    spec = importlib.util.spec_from_file_location("re_index", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def search(mod, entries, q, n=3):
    terms = q.lower().split()
    res = [(mod.score(e, terms), e) for e in entries if not e.get("archived")]
    res = [(s, e) for s, e in res if s and s[0] == len(terms)]
    res.sort(key=lambda x: (-x[0][0], -x[0][1]))
    return [e for _, e in res[:n]]


# ---------- SVG assets ----------

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"


def banner_svg(n, ncat):
    """Typographic banner: wordmark over a faint hex dump of a phrase."""
    data = b"reverse engineered so you don't have to. " * 20
    rows = []
    for r in range(13):
        chunk = data[r * 16:(r + 1) * 16]
        hexs = " ".join(f"{b:02x}" for b in chunk)
        asc = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        rows.append(f'<text x="700" y="{40 + r * 24}" class="hex">{r * 16:08x}  {esc(hexs)}  {esc(asc)}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="360" viewBox="0 0 1280 360" role="img" aria-label="Awesome Reverse-Engineered: {n:,} projects">
<style>
.hex{{font:12.5px {MONO};fill:#ffb000;white-space:pre}}
.t{{font:700 64px {SANS};fill:#f2f0e8;letter-spacing:-1.5px}}
.k{{font:600 24px {MONO};fill:#ffb000}}
.s{{font:400 24px {SANS};fill:#a8a597}}
.n{{font:600 22px {MONO};fill:#f2f0e8;white-space:pre}}
</style>
<defs><linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="#ffb000" stop-opacity="0"/><stop offset=".35" stop-color="#ffb000" stop-opacity=".16"/><stop offset="1" stop-color="#ffb000" stop-opacity=".2"/></linearGradient>
<mask id="m"><rect x="680" width="600" height="360" fill="url(#fade)"/></mask></defs>
<rect width="1280" height="360" rx="16" fill="#0e0f0d"/>
<g mask="url(#m)" style="filter:none">{"".join(rows).replace('class="hex"', 'class="hex" fill="#fff"')}</g>
<text x="64" y="96" class="k">awesome-</text>
<text x="60" y="172" class="t">Reverse-Engineered</text>
<text x="64" y="220" class="s">Open-source clients, drivers, parsers and decompilations</text>
<text x="64" y="252" class="s">for closed apps, APIs, devices, games and AI tools.</text>
<rect x="64" y="284" width="4" height="34" fill="#ffb000"/>
<text x="84" y="309" class="n">{n:,} projects   {ncat} categories   refreshed nightly</text>
</svg>
'''


def bars_svg(counts):
    """Single-series horizontal bar chart with direct value labels; theme-aware via prefers-color-scheme."""
    W, rowh, left, right = 900, 30, 330, 80
    H = 24 + rowh * len(counts) + 12
    mx = max(v for _, v in counts)
    out = []
    for i, (c, v) in enumerate(counts):
        y = 24 + i * rowh
        w = max(4, (W - left - right) * v / mx)
        out.append(f'<text x="{left - 14}" y="{y + 19}" class="lab" text-anchor="end">{esc(c)}</text>')
        out.append(f'<rect x="{left}" y="{y + 6}" width="{w:.1f}" height="18" rx="4" class="bar"><title>{esc(c)}: {v:,}</title></rect>')
        out.append(f'<text x="{left + w + 8:.1f}" y="{y + 20}" class="val">{v:,}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Projects per category">
<style>
.lab{{font:14px {SANS};fill:#1f2328}} .val{{font:600 13px {MONO};fill:#59636e}} .bar{{fill:#c98500}}
@media (prefers-color-scheme: dark){{ .lab{{fill:#e6edf3}} .val{{fill:#9198a1}} .bar{{fill:#ffb000}} }}
</style>
{"".join(out)}
</svg>
'''


def demo_svg(query, prompt, results):
    """Terminal render of a real skill search over the current data."""
    lines = [("p", "$ npx skills add alexgaoth/awesome-reverse-engineered"),
             ("ok", "  installed find-reverse-engineered"), ("", ""),
             ("u", f"> {prompt}"), ("", ""),
             ("a", f"  find-reverse-engineered  search {query}")]
    for i, e in enumerate(results, 1):
        meta = f"★{e.get('stars') or 0:,}  {e.get('lang') or '?'}  {e.get('license') or 'no license'}  {health(e)}"
        d = e.get("desc", "")
        lines += [("r", f"  {i}. {e['name']}"), ("m", f"     {meta}"),
                  ("d", f"     {d[:78] + ('...' if len(d) > 78 else '')}")]
    lines += [("", ""), ("a", f"  Best fit: {results[0]['name']}. Reading its README before installing.")]
    H = 70 + 24 * len(lines)
    body = "".join(f'<text x="28" y="{78 + i * 24}" class="{c}">{esc(t)}</text>' for i, (c, t) in enumerate(lines) if t)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{H}" viewBox="0 0 900 {H}" role="img" aria-label="An agent using the find-reverse-engineered skill">
<style>
text{{font:15px {MONO};fill:#c9c6b8;white-space:pre}}
.p{{fill:#f2f0e8}} .ok{{fill:#7ee787}} .u{{fill:#f2f0e8;font-weight:600}} .a{{fill:#ffb000}}
.r{{fill:#f2f0e8;font-weight:600}} .m{{fill:#8b8878}} .d{{fill:#c9c6b8}} .bar{{font:13px {SANS};fill:#8b8878}}
</style>
<rect width="900" height="{H}" rx="14" fill="#0e0f0d"/>
<circle cx="28" cy="26" r="6" fill="#3a3b36"/><circle cx="48" cy="26" r="6" fill="#3a3b36"/><circle cx="68" cy="26" r="6" fill="#3a3b36"/>
<text x="450" y="31" text-anchor="middle" class="bar">agent session</text>
{body}
</svg>
'''


# ---------- main ----------

def main():
    entries = json.load(open(os.path.join(ROOT, "data", "entries.json")))
    by = collections.defaultdict(lambda: collections.defaultdict(list))
    for e in entries:
        by[e["category"]][e.get("subcategory") or "Other"].append(e)
    cats = [c for c in ORDER if c in by] + sorted(c for c in by if c not in ORDER)
    ccount = {c: sum(len(v) for v in by[c].values()) for c in cats}
    n = len(entries)
    hc = collections.Counter(health(e) for e in entries)
    langs = collections.Counter(e.get("lang") for e in entries if e.get("lang"))
    total_stars = sum(e.get("stars") or 0 for e in entries)

    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    open(os.path.join(ROOT, "assets", "banner.svg"), "w").write(banner_svg(n, len(cats)))
    open(os.path.join(ROOT, "assets", "categories.svg"), "w").write(bars_svg(sorted(ccount.items(), key=lambda x: -x[1])))
    demo = search(load_search(), entries, "tuya local")
    if demo:
        open(os.path.join(ROOT, "assets", "demo.svg"), "w").write(
            demo_svg("tuya local", "control my Tuya smart plug locally, no cloud", demo))

    # Category pages.
    cdir = os.path.join(ROOT, "categories")
    os.makedirs(cdir, exist_ok=True)
    for f in os.listdir(cdir):
        os.remove(os.path.join(cdir, f))
    for c in cats:
        f = f"categories/{slug(c)}.md"
        subs = sorted(by[c])
        page = [f"# {ICON.get(c, '')} {c}", "",
                f"[← All categories](../README.md#-whats-inside) · [Search this category on the website]({SITE}#c={slug(c)}) · {ccount[c]:,} projects", "",
                "Health: 🟢 pushed in the last year · 🟡 1 to 3 years · 🔴 over 3 years · 🗄️ archived · ⚪ unknown", ""]
        if len(subs) > 1:
            page += [f"- [{s}](#{anchor(s)}) ({len(by[c][s])})" for s in subs] + [""]
        for s in subs:
            if len(subs) > 1:
                page += [f"## {s}", ""]
            page += table(by[c][s]) + [""]
        open(os.path.join(ROOT, f), "w").write("\n".join(page))

    # Website data: compact rows, loaded by docs/index.html.
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
    rows = [[e["name"], e["url"], e.get("desc", ""), e["category"], e.get("subcategory") or "",
             e.get("stars") or 0, e.get("lang") or "", e.get("license") or "", e.get("pushed") or "",
             health(e), e.get("topics") or [], e.get("platform") or ""] for e in entries]
    meta = {"n": n, "updated": TODAY.isoformat(), "cats": [[c, ICON.get(c, ""), slug(c), ccount[c]] for c in cats]}
    with open(os.path.join(ROOT, "docs", "data.json"), "w") as fh:
        json.dump({"meta": meta, "rows": rows}, fh, ensure_ascii=False, separators=(",", ":"))

    # README.
    def badge(label, msg, color="ffb000"):
        return f"https://img.shields.io/badge/{label}-{msg}-{color}?style=flat-square&labelColor=0e0f0d"
    hot = sorted((e for e in entries if e.get("pushed") and not e.get("archived")
                  and (TODAY - datetime.date.fromisoformat(e["pushed"])).days <= 7
                  and e["category"] != "Collections & Awesome Lists"), key=lambda e: -(e.get("stars") or 0))[:10]
    top = sorted((e for e in entries if e.get("stars") and e["category"] != "Collections & Awesome Lists"),
                 key=lambda e: -e["stars"])[:25]
    recent_cut = (TODAY - datetime.timedelta(days=7)).isoformat()
    first_day = min(e.get("added", "9999") for e in entries)
    just_added = [e for e in entries if e.get("added", "") >= recent_cut and e.get("added") != first_day]

    R = ['<div align="center">', "",
         f'<a href="{SITE}"><img src="assets/banner.svg" alt="Awesome Reverse-Engineered" width="100%"></a>', "",
         f"### {n:,} open-source tools that exist because someone reverse engineered a closed app, API, device, protocol, file format, game or AI product.", "",
         "[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) "
         f"[![Projects]({badge('projects', f'{n:,}'.replace(',', '%2C'))})](#-whats-inside) "
         f"[![Categories]({badge('categories', len(cats))})](#-whats-inside) "
         f"[![Nightly refresh](https://img.shields.io/github/actions/workflow/status/{REPO}/refresh.yml?style=flat-square&label=nightly%20refresh&labelColor=0e0f0d)](.github/workflows/refresh.yml) "
         f"[![Updated]({badge('updated', TODAY.isoformat().replace('-', '--'), '30363d')})](data/entries.json) "
         f"[![License: CC0]({badge('license', 'CC0', '30363d')})](LICENSE)", "",
         f"[![Agent skill]({badge('agent%20skill', 'npx%20skills%20add', '7ee787')})](#-give-your-ai-agent-the-whole-index) "
         f"[![Claude Code plugin]({badge('Claude%20Code', 'plugin', 'd97757')})](#-give-your-ai-agent-the-whole-index) "
         f"[![Stars](https://img.shields.io/github/stars/{REPO}?style=flat-square&labelColor=0e0f0d&color=ffb000)](https://github.com/{REPO}/stargazers)", "",
         f"**[🔎 Search the index]({SITE})** · **[🤖 Agent skill](#-give-your-ai-agent-the-whole-index)** · **[📚 Categories](#-whats-inside)** · **[🔥 Hot this week](#-hot-this-week)** · **[➕ Add a project](#-contributing)**", "",
         "</div>", "", "---", ""]

    R += ["## 🤖 Give your AI agent the whole index", "",
          "When a task needs to talk to something with no official API (a smart plug, a car, a chat app, a file format), "
          "your agent searches this index, ranks by stars, activity and license, reads the README, and picks the right tool.", "",
          "```bash", "npx skills add alexgaoth/awesome-reverse-engineered", "```", "",
          "<details><summary><b>Other ways to install</b></summary>", "",
          "**Claude Code plugin**", "", "```", f"/plugin install reverse-engineered --marketplace {REPO}", "```", "",
          "**Any agent or shell** (one file, Python standard library only)", "", "```bash",
          f"curl -sL https://raw.githubusercontent.com/{REPO}/main/skills/find-reverse-engineered/scripts/re_index.py -o re_index.py",
          "python3 re_index.py search tuya local          # ranked matches",
          "python3 re_index.py info make-all/tuya-local   # entry + README excerpt",
          "python3 re_index.py clone make-all/tuya-local  # shallow clone into vendor/",
          "```", "", "</details>", ""]
    if demo:
        R += ['<p align="center"><img src="assets/demo.svg" alt="An agent using the find-reverse-engineered skill" width="820"></p>',
              '<p align="center"><sub>Real output of the skill on the current data.</sub></p>', ""]

    R += ["## 🔎 Search it on the web", "",
          f"Filter {n:,} projects by category, language and health, sorted by stars or recent activity. Every search has a shareable link.", ""]
    if os.path.exists(os.path.join(ROOT, "assets", "site.png")):
        R += [f'<p align="center"><a href="{SITE}"><img src="assets/site.png" alt="The search website" width="820"></a></p>', ""]
    R += [f'<p align="center"><a href="{SITE}"><b>Open the search →</b></a></p>', ""]

    R += ["## 📚 What's inside", "",
          f"**{n:,} projects** with **{total_stars / 1e6:.1f}M** GitHub stars between them. "
          f"🟢 {hc['active']:,} active · 🟡 {hc['slow']:,} slowing down · 🔴 {hc['dormant']:,} dormant · 🗄️ {hc['archived']:,} archived. "
          "Top languages: " + ", ".join(f"{l} ({c:,})" for l, c in langs.most_common(5)) + ".", "",
          '<p align="center"><img src="assets/categories.svg" alt="Projects per category" width="820"></p>', "",
          "| | Category | Projects | Top picks |", "|:-:|---|--:|---|"]
    for c in cats:
        picks = sorted((e for v in by[c].values() for e in v), key=lambda e: -(e.get("stars") or 0))[:3]
        R.append(f"| {ICON.get(c, '')} | [**{c}**](categories/{slug(c)}.md) | {ccount[c]:,} | "
                 + ", ".join(f"[{p['name'].replace('|', '/')}]({p['url']})" for p in picks) + " |")
    R.append("")

    if hot:
        R += ["## 🔥 Hot this week", "", "The most-starred projects with commits in the last 7 days.", ""] + table(hot) + [""]
    if just_added:
        R += ["## 🆕 Just added", ""] + table(sorted(just_added, key=lambda e: -(e.get("stars") or 0))[:15]) + [""]

    R += ["## 🏆 Most starred", ""] + table(top, numbered=True) + [""]

    R += ["## 🩺 Health", "",
          "| | Meaning |", "|:-:|---|",
          "| 🟢 | Active: pushed in the last 12 months |", "| 🟡 | Slowing: last push 1 to 3 years ago |",
          "| 🔴 | Dormant: no push for over 3 years |", "| 🗄️ | Archived by its owner |",
          "| ⚪ | Unknown: not hosted on GitHub |", "",
          "Unofficial APIs break when the vendor changes their side, so check health before you depend on a project.", ""]

    R += ["## 🛠️ How it's built", "", "```mermaid", "flowchart LR",
          "  A[Research agents<br/>GitHub, HN, Reddit,<br/>awesome-lists] --> B[Scope filter<br/>interoperability only]",
          "  B --> C[GitHub API check<br/>exists, stars, license]",
          "  C --> D[(data/entries.json)]",
          "  D --> E[README and<br/>category pages]", "  D --> F[Search website]", "  D --> G[Agent skill]",
          "  H[Nightly refresh<br/>GitHub Action] -->|stars, archived,<br/>dead links| D", "```", "",
          "Raw data: [`data/entries.json`](data/entries.json). Removed repos: [`data/removed.json`](data/removed.json). "
          "Imported lists and searches: [SOURCES.md](SOURCES.md).", ""]

    R += ["## ⚖️ Scope", "",
          "This index lists **interoperability, preservation and research** projects: unofficial clients and SDKs, open drivers, "
          "local-control libraries, file-format parsers, protocol documentation, reimplementations and decompilations. "
          "Reverse engineering for interoperability is protected in many places (for example 17 U.S.C. §1201(f) and Article 6 of the EU Software Directive).", "",
          "**Left out on purpose:** exploits and jailbreaks, security or certificate-pinning bypasses, decryption tools, cheats, "
          "DRM or paywall removal, CAPTCHA solvers, account bots and credential tools.", "",
          "Using an unofficial client can break a service's terms of use. Use these projects with your own accounts, devices and data.", ""]

    R += ["## ➕ Contributing", "",
          f"Know a project that belongs here? [Open an issue](https://github.com/{REPO}/issues/new?title=Add%3A%20&body=Repo%3A%20%0AWhat%20it%20reverse%20engineers%3A%20) "
          "with the repo link and one line on what it reverse engineers, or send a PR that adds it to `data/entries.json`. "
          "Wrong category, dead link, or out of scope? Open an issue too.", "",
          f"Curated by [@alexgaoth](https://github.com/alexgaoth) with research agents. Every entry is checked against the GitHub API.", ""]

    R += ["## ⭐ Star history", "",
          f'<a href="https://star-history.com/#{REPO}&Date"><img src="https://api.star-history.com/svg?repos={REPO}&type=Date" alt="Star history" width="600"></a>', ""]

    R += ["## License", "", "[CC0 1.0](LICENSE) for the list itself. Each linked project has its own license.", "",
          '<div align="center">', "", f"**If this saved you from reverse engineering something yourself, [give it a ⭐](https://github.com/{REPO}).**", "", "</div>", ""]

    open(os.path.join(ROOT, "README.md"), "w").write("\n".join(R))
    print(f"rendered {n} entries, {len(cats)} category pages")


if __name__ == "__main__":
    main()
