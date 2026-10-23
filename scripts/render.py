#!/usr/bin/env python3
"""Render README.md, categories/*.md, assets/*.svg and docs/data.json from data/entries.json.

Run from anywhere: python3 scripts/render.py
"""
import collections, datetime, html, importlib.util, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = "alexgaoth/awesome-reverse-engineered"
SITE = "https://alexgaoth.github.io/awesome-reverse-engineered/"
# "Listed in" badge for projects in the index. The site's per-project button links it to the project's entry.
BADGE_IMG = "https://img.shields.io/badge/listed%20in-awesome--reverse--engineered-ffb000?style=flat-square&labelColor=0e0f0d"
BADGE_MD = f"[![Listed in Awesome Reverse-Engineered]({BADGE_IMG})](https://github.com/{REPO})"
# Files that state the index size as a rounded "12,000+". render.py keeps them in step with the data.
COUNT_FILES = ["docs/index.html", "mcp/reverse_engineered_mcp.py", "mcp/pyproject.toml", "plugin/.claude-plugin/plugin.json",
               "plugin/skills/find-reverse-engineered/SKILL.md", ".claude-plugin/marketplace.json"]
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


def table(rows, numbered=False, head=None):
    h = head or ["Project", "What it does", "★", "Health", "Lang"]
    head = ("| # " if numbered else "") + "| " + " | ".join(h) + " |"
    sep = ("|--:" if numbered else "") + "|---|---|--:|:-:|---|"
    out = [head, sep]
    for i, e in enumerate(sorted(rows, key=lambda e: (-(e.get("stars") or 0), e["name"].lower())), 1):
        d = (e.get("desc") or "").replace("|", "\\|").replace("\n", " ")
        st = f"{e['stars']:,}" if e.get("stars") is not None else ""
        name = f"[{e['name'].replace('|', '/')}]({e['url']})"
        out.append((f"| {i} " if numbered else "") + f"| {name} | {d} | {st} | {HEALTH_MD[health(e)]} | {e.get('lang') or ''} |")
    return out


def sync_mcp():
    """The MCP server ships a copy of the skill's search script so it can be installed on its own."""
    import shutil
    src = os.path.join(ROOT, "plugin", "skills", "find-reverse-engineered", "scripts", "re_index.py")
    if os.path.isdir(os.path.join(ROOT, "mcp")):
        shutil.copyfile(src, os.path.join(ROOT, "mcp", "re_index.py"))


def load_search():
    """Reuse the skill's ranking so the README demo shows real search output."""
    p = os.path.join(ROOT, "plugin", "skills", "find-reverse-engineered", "scripts", "re_index.py")
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


def social_svg(n):
    """1280x640 share card (site og:image and GitHub social preview). Convert to docs/og.png with scripts/og.sh."""
    data = b"don't reverse engineer it twice. " * 30
    rows = []
    for r in range(24):
        chunk = data[r * 16:(r + 1) * 16]
        hexs = " ".join(f"{b:02x}" for b in chunk)
        asc = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        rows.append(f'<text x="790" y="{36 + r * 26}" class="hex">{r * 16:08x}  {esc(hexs)}  {esc(asc)}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="640" viewBox="0 0 1280 640">
<style>
.hex{{font:13px {MONO};fill:#ffb000;white-space:pre}}
.k{{font:600 30px {MONO};fill:#ffb000}}
.t{{font:700 78px {SANS};fill:#f2f0e8;letter-spacing:-2px}}
.s{{font:400 30px {SANS};fill:#a8a597}}
.u{{font:600 26px {MONO};fill:#f2f0e8;white-space:pre}}
</style>
<defs><linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".4" stop-color="#fff" stop-opacity=".13"/><stop offset="1" stop-color="#fff" stop-opacity=".18"/></linearGradient>
<mask id="m"><rect x="760" width="520" height="640" fill="url(#fade)"/></mask></defs>
<rect width="1280" height="640" fill="#0e0f0d"/>
<g mask="url(#m)">{"".join(rows)}</g>
<text x="80" y="140" class="k">awesome-reverse-engineered</text>
<text x="76" y="260" class="t">Don't reverse engineer</text>
<text x="76" y="350" class="t">it twice.</text>
<text x="80" y="420" class="s">{n // 1000 * 1000:,}+ open-source tools for closed apps, APIs,</text>
<text x="80" y="460" class="s">devices, file formats, games and AI tools.</text>
<rect x="80" y="520" width="5" height="40" fill="#ffb000"/>
<text x="104" y="550" class="u">awesome.alexgaoth.com   ·   agent skill   ·   nightly refresh</text>
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


def sync_counts(n):
    """Replace every "10,000+"-style count in COUNT_FILES with the current rounded-down size."""
    rounded = f"{n // 1000 * 1000:,}+"
    for f in COUNT_FILES:
        p = os.path.join(ROOT, f)
        old = open(p).read()
        new = re.sub(r"\b\d{1,3}(?:,\d{3})+\+", rounded, old)
        if new != old:
            open(p, "w").write(new)


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
    # Research counters written by the pipeline (searches, imported lists, scope-filter drops).
    sp = os.path.join(ROOT, "data", "stats.json")
    stats = json.load(open(sp)) if os.path.exists(sp) else {}
    rp = os.path.join(ROOT, "data", "removed.json")
    removed = json.load(open(rp)) if os.path.exists(rp) else []

    sync_counts(n)
    sync_mcp()
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    open(os.path.join(ROOT, "assets", "banner.svg"), "w").write(banner_svg(n, len(cats)))
    open(os.path.join(ROOT, "assets", "social.svg"), "w").write(social_svg(n))
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
        page = [f"# {c}", "",
                f"[← All categories](../README.md#whats-inside) · [Search this category on the website]({SITE}#c={slug(c)}) · {ccount[c]:,} projects · [Listed here? Get the badge](../README.md#is-your-project-listed)", "",
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

    # READMEs, one per language (scripts/i18n.py). Project names and descriptions stay in English.
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from i18n import LANGS, S, CAT
    import resurrected  # the Resurrected page (docs/resurrected/) and its README teaser
    res = resurrected.build(ROOT, entries, n, MONO, SANS)

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
    issue = (f"https://github.com/{REPO}/issues/new?title=Add%3A%20&body=Repo%3A%20%0AWhat%20it%20reverse%20engineers%3A%20")

    for code, fname, _label in LANGS:
        t = S[code]
        cn = lambda c: CAT.get(code, {}).get(c, c)
        th = t["th_proj"]
        a_agent, a_inside, a_hot, a_contrib = (anchor(t[k]) for k in ("h_agent", "h_inside", "h_hot", "h_contrib"))
        switch = " · ".join(f"<b>{lab}</b>" if f == fname else f'<a href="{f}">{lab}</a>' for _, f, lab in LANGS)
        R = ['<div align="center">', "",
             f'<a href="{SITE}"><img src="assets/banner.svg" alt="Awesome Reverse-Engineered" width="100%"></a>', "",
             f"<p>{switch}</p>", "",
             f"## {t['pitch']}", "",
             t["tagline"].format(n=f"{n:,}"), "",
             t["quick"].format(site=SITE), "",
             "[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) "
             f"[![Projects]({badge('projects', f'{n:,}'.replace(',', '%2C'))})](#{a_inside}) "
             f"[![Nightly refresh](https://img.shields.io/github/actions/workflow/status/{REPO}/refresh.yml?style=flat-square&label=nightly%20refresh&labelColor=0e0f0d)](.github/workflows/refresh.yml) "
             f"[![Stars](https://img.shields.io/github/stars/{REPO}?style=flat-square&labelColor=0e0f0d&color=ffb000)](https://github.com/{REPO}/stargazers) "
             f"[![License: MIT + CC0 data]({badge('license', 'MIT%20%2B%20CC0%20data', '30363d')})](LICENSE)", "",
             f"**[{t['nav'][1]}](#{a_agent})** · **[{t['nav'][2]}](#{a_inside})** · **[{t['nav'][3]}](#{a_hot})** · **[{t['nav'][4]}](#{a_contrib})**", ""]
        if t["note"]:
            R += [f"<sub>{t['note']}</sub>", ""]
        R += ["</div>", "", "---", ""]

        R += [f"## {t['h_before']}", "", t["before_p"], ""]
        R += [f"{i}. " + x.format(site=SITE, a_agent=a_agent, a_contrib=a_contrib) for i, x in enumerate(t["before_steps"], 1)] + [""]

        R += [f"## {t['h_inside']}", "",
              t["inside_p"].format(n=f"{n:,}", stars=f"{total_stars / 1e6:.1f}", a=f"{hc['active']:,}", s=f"{hc['slow']:,}",
                                   d=f"{hc['dormant']:,}", ar=f"{hc['archived']:,}",
                                   langs=", ".join(f"{l} ({c:,})" for l, c in langs.most_common(5))), "",
              f"| {t['th_cat'][0]} | {t['th_cat'][1]} | {t['th_cat'][2]} |", "|---|--:|---|"]
        for c in cats:
            picks = sorted((e for v in by[c].values() for e in v), key=lambda e: -(e.get("stars") or 0))[:3]
            R.append(f"| [**{cn(c)}**](categories/{slug(c)}.md) | {ccount[c]:,} | "
                     + ", ".join(f"[{p['name'].replace('|', '/')}]({p['url']})" for p in picks) + " |")
        R.append("")

        if res:
            R += [f"## {t['h_res']}", "", t["res_p"].format(n=len(res)), "",
                  f"| {' | '.join(t['th_res'])} |", "|---|---|--:|---|"]
            for r in sorted(res, key=lambda r: -r["stars"])[:8]:
                e = r["revs"][0]
                R.append(f"| {r['product'].replace('|', '/')} | {r['maker']} | {int(r['killed'])} | [{e['name'].replace('|', '/')}]({e['url']}) |")
            R += ["", f"**[{t['res_link'].format(n=len(res))} →]({SITE}resurrected/)**", ""]

        R += [f"## {t['h_agent']}", "", t["agent_p"], "",
              "```bash", "npx skills add alexgaoth/awesome-reverse-engineered", "```", "",
              f"<details><summary><b>{t['other_ways']}</b></summary>", "",
              f"**{t['plugin']}**", "", "```", f"/plugin install reverse-engineered --marketplace {REPO}", "```", "",
              f"**{t['mcp']}**", "", "```bash",
              f'claude mcp add reverse-engineered -- uvx --from "git+https://github.com/{REPO}#subdirectory=mcp" reverse-engineered-mcp',
              "```", "", "```json",
              '{"mcpServers": {"reverse-engineered": {"command": "uvx", "args": ["--from", '
              f'"git+https://github.com/{REPO}#subdirectory=mcp", "reverse-engineered-mcp"]}}}}}}',
              "```", "",
              f"**{t['any_shell']}**", "", "```bash",
              f"curl -sL https://raw.githubusercontent.com/{REPO}/main/plugin/skills/find-reverse-engineered/scripts/re_index.py -o re_index.py",
              "python3 re_index.py search tuya local          # ranked matches",
              "python3 re_index.py info make-all/tuya-local   # entry + README excerpt",
              "python3 re_index.py clone make-all/tuya-local  # shallow clone into vendor/",
              "```", "", "</details>", ""]
        if demo:
            R += ['<p align="center"><img src="assets/demo.svg" alt="find-reverse-engineered" width="820"></p>',
                  f'<p align="center"><sub>{t["demo_caption"]}</sub></p>', ""]

        R += [f"## {t['h_web']}", "", t["web_p"].format(n=f"{n:,}"), ""]
        if os.path.exists(os.path.join(ROOT, "assets", "site.png")):
            R += [f'<p align="center"><a href="{SITE}"><img src="assets/site.png" alt="{t["h_web"]}" width="820"></a></p>', ""]
        R += [f'<p align="center"><a href="{SITE}"><b>{t["open_search"]} →</b></a></p>', ""]

        if hot:
            R += [f"## {t['h_hot']}", "", t["hot_p"], ""] + table(hot, head=th) + [""]
        if just_added:
            R += [f"## {t['h_new']}", ""] + table(sorted(just_added, key=lambda e: -(e.get("stars") or 0))[:15], head=th) + [""]
        R += [f"## {t['h_top']}", ""] + table(top, numbered=True, head=th) + [""]

        lg = t["legend"]
        R += [f"## {t['h_health']}", "", f"| | {lg[0]} |", "|:-:|---|",
              f"| 🟢 | {lg[1]} |", f"| 🟡 | {lg[2]} |", f"| 🔴 | {lg[3]} |", f"| 🗄️ | {lg[4]} |", f"| ⚪ | {lg[5]} |", "",
              t["health_p"], ""]

        R += [f"## {t['h_built']}", "", "```mermaid", "flowchart LR",
              "  A[Research agents<br/>GitHub, HN, Reddit,<br/>awesome-lists] --> B[Scope filter<br/>interoperability only]",
              "  B --> C[GitHub API check<br/>exists, stars, license]",
              "  C --> D[(data/entries.json)]",
              "  D --> E[README and<br/>category pages]", "  D --> F[Search website]", "  D --> G[Agent skill]",
              "  H[Nightly refresh<br/>GitHub Action] -->|stars, archived,<br/>dead links| D", "```", "", t["built_p"], ""]
        fl = t["filter"]
        R += [f"### {t['h_filter']}", "", "| | |", "|--:|---|"]
        R += [f"| {v:,} | {lab} |" for v, lab in zip(
            (stats.get("searches", 0), stats.get("sources", 0), stats.get("scope_dropped", 0), n, hc["archived"], len(removed)), fl) if v]
        R += ["", '<p align="center"><img src="assets/categories.svg" alt="Projects per category" width="820"></p>', ""]

        R += [f"## {t['h_scope']}", ""] + [x for p in t["scope"] for x in (p, "")]
        R += [f"## {t['h_contrib']}", "", t["contrib"].format(issue=issue), "", t["curated"], ""]
        R += [f"## {t['h_badge']}", "", BADGE_MD, "", t["badge_p"].format(site=SITE), "", "```markdown", BADGE_MD, "```", ""]
        R += [f"## {t['h_star']}", "",
              f'<a href="https://star-history.com/#{REPO}&Date"><img src="https://api.star-history.com/svg?repos={REPO}&type=Date" alt="Star history" width="600"></a>', ""]
        R += [f"## {t['h_license']}", "", t["license"], "",
              '<div align="center">', "", f"**{t['cta'].format(repo=f'https://github.com/{REPO}')}**", "", "</div>", ""]
        open(os.path.join(ROOT, fname), "w").write("\n".join(R))
    print(f"rendered {n} entries, {len(cats)} category pages")


if __name__ == "__main__":
    main()
