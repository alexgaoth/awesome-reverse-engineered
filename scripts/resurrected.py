"""The Resurrected page: products their makers killed, kept alive by projects in the index.

Input: data/resurrected.json, a list of
  {"product", "maker", "killed" (year), "what", "revived_by": [repo urls], "source", "kind": device|game|service}
Output: docs/resurrected/index.html (static, crawlable) and assets/resurrected.svg (share card).
render.py calls build() and uses the returned rows for the README section.
"""
import html, json, os, re

esc = lambda s: html.escape(str(s or ""), quote=True)
norm = lambda u: re.sub(r"^https?://(www\.)?", "", u.strip().rstrip("/").lower())
KINDS = [("device", "Devices"), ("game", "Games"), ("service", "Services")]


def load(root, entries):
    """Records sorted newest kill first, each with its revivers resolved to index entries (most stars first)."""
    p = os.path.join(root, "data", "resurrected.json")
    if not os.path.exists(p):
        return []
    by_url = {norm(e["url"]): e for e in entries}
    out = []
    for r in json.load(open(p)):
        revs = sorted((by_url[norm(u)] for u in r.get("revived_by", []) if norm(u) in by_url),
                      key=lambda e: -(e.get("stars") or 0))
        if revs:
            out.append(dict(r, revs=revs, stars=sum(e.get("stars") or 0 for e in revs)))
    out.sort(key=lambda r: (-int(r["killed"]), r["product"].lower()))
    return out


def card_svg(n, makers, mono, sans):
    """1280x640 share card for the page."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="640" viewBox="0 0 1280 640">
<style>
.k{{font:600 30px {mono};fill:#ffb000}} .t{{font:700 84px {sans};fill:#f2f0e8;letter-spacing:-2.5px}}
.s{{font:400 30px {sans};fill:#a8a597}} .u{{font:600 26px {mono};fill:#f2f0e8}}
.x{{font:700 34px {mono};fill:#f87171}} .ok{{font:700 34px {mono};fill:#4ade80}}
</style>
<rect width="1280" height="640" fill="#0e0f0d"/>
<path d="M880 560 V250 a150 150 0 0 1 300 0 V560 Z" fill="#151613" stroke="#2a2b26" stroke-width="3"/>
<text x="1030" y="300" text-anchor="middle" class="x">KILLED</text>
<line x1="950" y1="330" x2="1110" y2="330" stroke="#2a2b26" stroke-width="3"/>
<text x="1030" y="390" text-anchor="middle" class="ok">ALIVE</text>
<text x="1030" y="440" text-anchor="middle" class="u" style="font-size:22px;fill:#8b8878">open source</text>
<text x="80" y="140" class="k">awesome-reverse-engineered</text>
<text x="76" y="250" class="t">Resurrected.</text>
<text x="80" y="330" class="s">{n} products their makers killed,</text>
<text x="80" y="372" class="s">kept alive by open source.</text>
<rect x="80" y="470" width="5" height="40" fill="#ffb000"/>
<text x="104" y="500" class="u">{makers} companies · awesome.alexgaoth.com/resurrected</text>
</svg>
'''


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Resurrected: {n} products their makers killed, kept alive by open source</title>
<meta name="description" content="{n} devices, games and online services that companies shut down, bricked or abandoned, and the open-source projects built by reverse engineering that keep them running.">
<link rel="canonical" href="https://awesome.alexgaoth.com/resurrected/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Awesome Reverse-Engineered">
<meta property="og:title" content="Resurrected: {n} products their makers killed, kept alive by open source">
<meta property="og:description" content="Nest, Pebble, Stadia, the Wii's online play, GameSpy, Club Penguin and more: shut down by their makers, brought back by reverse engineering.">
<meta property="og:image" content="https://awesome.alexgaoth.com/resurrected/og.png">
<meta property="og:image:width" content="1280">
<meta property="og:image:height" content="640">
<meta property="og:url" content="https://awesome.alexgaoth.com/resurrected/">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://awesome.alexgaoth.com/resurrected/og.png">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='7' fill='%230e0f0d'/><text x='16' y='22' font-family='monospace' font-size='15' font-weight='700' fill='%23ffb000' text-anchor='middle'>0x</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {{
  color-scheme: light;
  --bg: #fafaf9; --surface: #ffffff; --raised: #f2f2ef; --line: #e4e4e0;
  --ink: #18181b; --ink-2: #52525b; --ink-3: #71717a;
  --accent: #a16207; --dead: #b91c1c; --alive: #15803d;
  --sans: "Geist", ui-sans-serif, system-ui, sans-serif;
  --mono: "Geist Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    color-scheme: dark;
    --bg: #0e0f0d; --surface: #151613; --raised: #1c1d19; --line: #2a2b26;
    --ink: #f2f0e8; --ink-2: #b4b1a4; --ink-3: #8b8878;
    --accent: #ffb000; --dead: #f87171; --alive: #4ade80;
  }}
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--bg); color: var(--ink); font: 15px/1.55 var(--sans); }}
a {{ color: inherit; }}
:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 6px; }}
.wrap {{ max-width: 1180px; margin: 0 auto; padding: 0 24px; }}
nav {{ height: 64px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--line); }}
.mark {{ font: 600 15px var(--mono); text-decoration: none; }}
.mark b {{ color: var(--accent); font-weight: 600; }}
.navlinks {{ display: flex; gap: 6px; }}
.navlinks a {{ padding: 7px 12px; border-radius: 999px; text-decoration: none; color: var(--ink-2); font-size: 14px; }}
.navlinks a:hover {{ background: var(--raised); color: var(--ink); }}
header {{ padding: 64px 0 32px; }}
.kicker {{ font: 600 13px var(--mono); color: var(--accent); letter-spacing: .5px; text-transform: uppercase; margin: 0 0 14px; }}
h1 {{ font-size: clamp(36px, 5.4vw, 64px); line-height: 1.02; letter-spacing: -2px; margin: 0 0 18px; max-width: 16ch; }}
.lede {{ color: var(--ink-2); font-size: 18px; max-width: 60ch; margin: 0 0 28px; }}
.stats {{ display: flex; flex-wrap: wrap; gap: 28px; font: 13px var(--mono); color: var(--ink-3); }}
.stats b {{ display: block; font: 700 28px var(--sans); color: var(--ink); letter-spacing: -.5px; }}
.bar {{ position: sticky; top: 0; z-index: 5; background: color-mix(in srgb, var(--bg) 92%, transparent); backdrop-filter: blur(8px); border-bottom: 1px solid var(--line); padding: 12px 0; margin-bottom: 28px; }}
.chips {{ display: flex; gap: 8px; flex-wrap: wrap; }}
.chip {{ font: 500 13px var(--sans); padding: 6px 12px; border-radius: 999px; border: 1px solid var(--line); background: var(--surface); color: var(--ink-2); cursor: pointer; }}
.chip span {{ font: 12px var(--mono); color: var(--ink-3); margin-left: 4px; }}
.chip[aria-pressed="true"] {{ background: var(--ink); color: var(--bg); border-color: var(--ink); }}
.chip[aria-pressed="true"] span {{ color: var(--bg); opacity: .7; }}
.grid {{ list-style: none; padding: 0; margin: 0 0 64px; display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; }}
.card {{ background: var(--surface); border: 1px solid var(--line); border-radius: 26px 26px 10px 10px; padding: 22px 22px 18px; display: flex; flex-direction: column; gap: 10px; }}
.card[hidden] {{ display: none; }}
.life {{ display: flex; align-items: center; gap: 8px; font: 600 12px var(--mono); }}
.life .d {{ color: var(--dead); }} .life .a {{ color: var(--alive); }} .life .arrow {{ color: var(--ink-3); }}
.card h3 {{ margin: 0; font-size: 18px; line-height: 1.25; letter-spacing: -.3px; }}
.maker {{ font: 13px var(--mono); color: var(--ink-3); }}
.what {{ margin: 0; color: var(--ink-2); font-size: 14px; }}
.revs {{ margin: 4px 0 0; padding: 12px 0 0; border-top: 1px dashed var(--line); list-style: none; display: flex; flex-direction: column; gap: 6px; }}
.revs li {{ display: flex; justify-content: space-between; gap: 12px; font-size: 14px; }}
.revs a {{ text-decoration: none; font-weight: 600; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
.revs a:hover {{ text-decoration: underline; text-decoration-color: var(--accent); }}
.revs .st {{ font: 12px var(--mono); color: var(--ink-3); white-space: nowrap; }}
.src {{ font: 12px var(--mono); color: var(--ink-3); margin-top: auto; }}
footer {{ border-top: 1px solid var(--line); padding: 28px 0 48px; color: var(--ink-3); font-size: 14px; display: flex; flex-wrap: wrap; gap: 8px 24px; }}
footer a {{ color: var(--accent); }}
@media (max-width: 600px) {{ .wrap {{ padding: 0 16px; }} header {{ padding: 40px 0 24px; }} .navlinks .hide-sm {{ display: none; }} }}
</style>
</head>
<body>
<div class="wrap">
  <nav aria-label="Main">
    <a class="mark" href="../"><b>awesome-</b>reverse-engineered</a>
    <div class="navlinks">
      <a href="../">Search the index</a>
      <a class="hide-sm" href="https://github.com/alexgaoth/awesome-reverse-engineered">GitHub</a>
    </div>
  </nav>
  <header>
    <p class="kicker">Resurrected</p>
    <h1>They killed it. Open source brought it back.</h1>
    <p class="lede">{n} devices, games and online services that their makers shut down, bricked or abandoned, and the open-source projects, built by reverse engineering, that keep them running today.</p>
    <div class="stats">
      <div><b>{n}</b>products revived</div>
      <div><b>{makers}</b>companies</div>
      <div><b>{projects}</b>revival projects</div>
      <div><b>{stars}</b>GitHub stars</div>
    </div>
  </header>
  <div class="bar"><div class="chips" role="group" aria-label="Filter by kind">{chips}</div></div>
  <ol class="grid">
{cards}
  </ol>
  <footer>
    <span>Know another one? <a href="https://github.com/alexgaoth/awesome-reverse-engineered/issues/new?title=Resurrected%3A%20">Open an issue</a>.</span>
    <span>Data: <a href="https://github.com/alexgaoth/awesome-reverse-engineered/blob/main/data/resurrected.json">data/resurrected.json</a> (CC0). Each year links to its source.</span>
    <span>Part of <a href="../">awesome-reverse-engineered</a>: {total} open-source tools built by reverse engineering.</span>
  </footer>
</div>
<script>
const chips = document.querySelectorAll(".chip");
chips.forEach((c) => c.addEventListener("click", () => {{
  chips.forEach((x) => x.setAttribute("aria-pressed", String(x === c)));
  document.querySelectorAll(".card").forEach((card) => {{ card.hidden = !!c.dataset.k && card.dataset.k !== c.dataset.k; }});
}}));
</script>
</body>
</html>
"""


def build(root, entries, total, mono, sans):
    recs = load(root, entries)
    if not recs:
        return []
    cards = []
    for r in recs:
        revs = "".join(f'<li><a href="{esc(e["url"])}" rel="noopener">{esc(e["name"])}</a>'
                       f'<span class="st">★ {e.get("stars") or 0:,}</span></li>' for e in r["revs"][:4])
        cards.append(f'''    <li class="card" data-k="{esc(r.get("kind", "service"))}">
      <div class="life"><span class="d">† {int(r["killed"])}</span><span class="arrow">→</span><span class="a">alive</span></div>
      <h3>{esc(r["product"])}</h3>
      <div class="maker">killed by {esc(r["maker"])}</div>
      <p class="what">{esc(r.get("what"))}</p>
      <ul class="revs">{revs}</ul>
      <a class="src" href="{esc(r.get("source"))}" rel="noopener">source</a>
    </li>''')
    counts = {k: sum(1 for r in recs if r.get("kind") == k) for k, _ in KINDS}
    chips = f'<button class="chip" data-k="" aria-pressed="true">All<span>{len(recs)}</span></button>' + "".join(
        f'<button class="chip" data-k="{k}" aria-pressed="false">{lab}<span>{counts[k]}</span></button>'
        for k, lab in KINDS if counts[k])
    makers = len({r["maker"] for r in recs})
    projects = len({e["url"] for r in recs for e in r["revs"]})
    stars = sum(e.get("stars") or 0 for e in {e["url"]: e for r in recs for e in r["revs"]}.values())
    out = os.path.join(root, "docs", "resurrected")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w").write(PAGE.format(
        n=len(recs), makers=makers, projects=projects, stars=f"{stars:,}", chips=chips,
        cards="\n".join(cards), total=f"{total:,}"))
    open(os.path.join(root, "assets", "resurrected.svg"), "w").write(card_svg(len(recs), makers, mono, sans))
    return recs
