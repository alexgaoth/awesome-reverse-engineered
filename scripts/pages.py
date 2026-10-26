"""Static, crawlable pages for search engines: one per category and one per subcategory,
plus docs/sitemap.xml and docs/robots.txt. The search page (docs/index.html) is a JS app with
hash routes, so search engines see none of its 16,000+ entries; these pages fix that.

render.py calls build(). Output: docs/c/<category>/index.html, docs/c/<category>/<subcategory>/index.html.
"""
import datetime, html, os, re, shutil

BASE = "https://awesome.alexgaoth.com/"
REPO = "https://github.com/alexgaoth/awesome-reverse-engineered"
esc = lambda s: html.escape(str(s or ""), quote=True)
slug = lambda s: re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")
HEALTH = {"active": "active", "slow": "slowing", "dormant": "dormant", "archived": "archived", "unknown": ""}

CSS = """:root{color-scheme:light;--bg:#fafaf9;--surface:#fff;--raised:#f2f2ef;--line:#e4e4e0;--ink:#18181b;--ink-2:#52525b;--ink-3:#71717a;--accent:#a16207;--good:#15803d;--bad:#b91c1c;--sans:"Geist",ui-sans-serif,system-ui,sans-serif;--mono:"Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace}
@media (prefers-color-scheme:dark){:root{color-scheme:dark;--bg:#0e0f0d;--surface:#151613;--raised:#1c1d19;--line:#2a2b26;--ink:#f2f0e8;--ink-2:#b4b1a4;--ink-3:#8b8878;--accent:#ffb000;--good:#4ade80;--bad:#f87171}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 var(--sans)}a{color:inherit}
.wrap{max-width:1000px;margin:0 auto;padding:0 24px}nav{height:64px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--line);gap:12px}
.mark{font:600 15px var(--mono);text-decoration:none}.mark b{color:var(--accent);font-weight:600}nav .links a{color:var(--ink-2);text-decoration:none;font-size:14px;margin-left:14px}
.crumbs{font:13px var(--mono);color:var(--ink-3);margin:28px 0 8px}.crumbs a{color:var(--ink-3)}
h1{font-size:clamp(28px,4vw,40px);line-height:1.1;letter-spacing:-1px;margin:0 0 12px}.lede{color:var(--ink-2);max-width:70ch;margin:0 0 24px}
.cta{display:inline-block;margin:0 0 28px;color:var(--accent);font-weight:600;text-decoration:none}
h2{font-size:20px;margin:36px 0 10px;letter-spacing:-.3px}h2 a{text-decoration:none}h2 span{font:13px var(--mono);color:var(--ink-3);margin-left:8px}
ul.subs{list-style:none;padding:0;margin:0 0 24px;display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:8px}
ul.subs a{display:flex;justify-content:space-between;gap:8px;padding:10px 12px;border:1px solid var(--line);border-radius:10px;background:var(--surface);text-decoration:none}
ul.subs span{font:12px var(--mono);color:var(--ink-3)}
ol.items{list-style:none;padding:0;margin:0}ol.items li{padding:12px 0;border-bottom:1px solid var(--line);display:grid;grid-template-columns:1fr auto;gap:2px 16px}
ol.items a{font-weight:600;text-decoration:none}ol.items a:hover{text-decoration:underline;text-decoration-color:var(--accent)}
ol.items p{grid-column:1;margin:0;color:var(--ink-2);font-size:14px}ol.items .m{grid-column:2;grid-row:1/span 2;text-align:right;font:12px var(--mono);color:var(--ink-3);white-space:nowrap}
.h-active{color:var(--good)}.h-archived,.h-dormant{color:var(--bad)}
footer{border-top:1px solid var(--line);margin-top:48px;padding:24px 0 48px;color:var(--ink-3);font-size:14px}footer a{color:var(--accent)}
@media (max-width:600px){.wrap{padding:0 16px}nav .links .hide-sm{display:none}ol.items li{grid-template-columns:1fr}ol.items .m{grid-column:1;grid-row:auto;text-align:left}}"""

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Awesome Reverse-Engineered">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{base}og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='7' fill='%230e0f0d'/><text x='16' y='22' font-family='monospace' font-size='15' font-weight='700' fill='%23ffb000' text-anchor='middle'>0x</text></svg>">
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600;700&family=Geist+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<div class="wrap">
<nav aria-label="Main"><a class="mark" href="{root}"><b>awesome-</b>reverse-engineered</a>
<div class="links"><a href="{root}">Search</a><a class="hide-sm" href="{root}resurrected/">Resurrected</a><a class="hide-sm" href="{repo}">GitHub</a></div></nav>
"""

FOOT = """<footer>Part of <a href="{root}">Awesome Reverse-Engineered</a>: {total} open-source projects that exist because someone reverse engineered a closed product. Stars and activity refreshed nightly. Data <a href="{repo}/blob/main/data/entries.json">CC0</a>. Missing a project? <a href="{repo}#contributing">Add it</a>.</footer>
</div>
</body>
</html>
"""


def item(e, health):
    h = health(e)
    meta = f'★ {e.get("stars") or 0:,}' + (f' · <span class="h-{h}">{HEALTH[h]}</span>' if HEALTH.get(h) else "") + (f' · {esc(e["lang"])}' if e.get("lang") else "")
    return (f'<li><a href="{esc(e["url"])}" rel="noopener">{esc(e["name"])}</a>'
            f'<span class="m">{meta}</span><p>{esc(e.get("desc"))}</p></li>')


def page(path, title, desc, body, depth, total):
    root = "../" * depth
    url = BASE + path
    out = HEAD.format(title=esc(title), desc=esc(desc), url=url, base=BASE, css=CSS, root=root, repo=REPO)
    return out + body + FOOT.format(root=root, total=f"{total:,}", repo=REPO)


def build(root, by, cats, ccount, total, health):
    """by: {category: {subcategory: [entries]}}. Returns the list of page paths written."""
    out_dir = os.path.join(root, "docs", "c")
    shutil.rmtree(out_dir, ignore_errors=True)
    stars = lambda e: -(e.get("stars") or 0)
    paths = []
    for c in cats:
        cs = slug(c)
        subs = sorted(by[c].items(), key=lambda kv: -len(kv[1]))
        top = sorted((e for v in by[c].values() for e in v), key=stars)
        body = [f'<div class="crumbs"><a href="../../">Home</a> / {esc(c)}</div>',
                f"<h1>{ccount[c]:,} open-source {esc(c)} projects built by reverse engineering</h1>",
                f'<p class="lede">Open-source projects in <b>{esc(c)}</b> that exist because someone reverse engineered a closed product. '
                f'Most-starred: {", ".join(esc(e["name"]) for e in top[:5])}.</p>',
                f'<a class="cta" href="../../#c={cs}">Search and filter this category →</a>']
        if len(subs) > 1:
            body.append('<ul class="subs">' + "".join(
                f'<li><a href="{slug(s)}/">{esc(s)}<span>{len(v):,}</span></a></li>' for s, v in subs) + "</ul>")
        for s, v in subs:
            v = sorted(v, key=stars)
            more = f' <span><a href="{slug(s)}/">all {len(v):,} →</a></span>' if len(subs) > 1 and len(v) > 10 else ""
            body.append(f'<h2>{esc(s)}<span>{len(v):,}</span>{more}</h2>' if len(subs) > 1 else "")
            body.append('<ol class="items">' + "".join(item(e, health) for e in (v[:10] if len(subs) > 1 else v)) + "</ol>")
        p = f"c/{cs}/"
        os.makedirs(os.path.join(root, "docs", p), exist_ok=True)
        open(os.path.join(root, "docs", p, "index.html"), "w").write(page(
            p, f"{ccount[c]:,} open-source {c} projects built by reverse engineering",
            f"{ccount[c]:,} open-source {c} projects built by reverse engineering closed products, with stars and activity. "
            f"Includes {', '.join(e['name'] for e in top[:3])}.", "\n".join(body), 2, total))
        paths.append(p)
        if len(subs) < 2:
            continue
        for s, v in subs:
            v = sorted(v, key=stars)
            ps = f"c/{cs}/{slug(s)}/"
            body = [f'<div class="crumbs"><a href="../../../">Home</a> / <a href="../">{esc(c)}</a> / {esc(s)}</div>',
                    f"<h1>{len(v):,} open-source {esc(s)} projects</h1>",
                    f'<p class="lede">{esc(s)} ({esc(c)}): open-source projects that exist because someone reverse engineered a closed product, '
                    f"sorted by GitHub stars.</p>",
                    '<ol class="items">' + "".join(item(e, health) for e in v) + "</ol>"]
            os.makedirs(os.path.join(root, "docs", ps), exist_ok=True)
            open(os.path.join(root, "docs", ps, "index.html"), "w").write(page(
                ps, f"{len(v):,} open-source {s} projects ({c}) built by reverse engineering",
                f"{len(v):,} open-source {s} projects built by reverse engineering, sorted by stars. "
                f"Includes {', '.join(e['name'] for e in v[:3])}.", "\n".join(body), 3, total))
            paths.append(ps)
    today = datetime.date.today().isoformat()
    urls = ["", "resurrected/"] + paths
    open(os.path.join(root, "docs", "sitemap.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{BASE}{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    open(os.path.join(root, "docs", "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
    return paths
