#!/usr/bin/env python3
"""Search the awesome-reverse-engineered index and fetch a project.

Usage:
  re_index.py search <words...> [--category TEXT] [--lang NAME] [--min-stars N]
                                [--include-archived] [--limit N] [--json]
  re_index.py info <owner/repo | url>        # index entry + README excerpt
  re_index.py clone <owner/repo | url> [--dest DIR]
  re_index.py categories

Data source, first that works: $RE_INDEX_DATA (a local entries.json), a cache
in ~/.cache/awesome-reverse-engineered (refreshed every 24 h from GitHub), the
data/entries.json of the repo this script ships in.
Standard library only.
"""
import argparse, json, math, os, re, subprocess, sys, time, urllib.request

REPO = "alexgaoth/awesome-reverse-engineered"
RAW = f"https://raw.githubusercontent.com/{REPO}/main/data/entries.json"
CACHE = os.path.expanduser("~/.cache/awesome-reverse-engineered/entries.json")
BUNDLED = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "data", "entries.json")
SYNONYMS = {
    "twitter": ["x"], "x": ["twitter"], "ble": ["bluetooth"], "bluetooth": ["ble"],
    "car": ["vehicle", "automotive"], "vehicle": ["car"], "decomp": ["decompilation"],
    "decompile": ["decompilation"], "chatgpt": ["openai"], "openai": ["chatgpt"],
    "gemini": ["bard"], "instagram": ["meta"], "facebook": ["meta"], "imessage": ["apple"],
    "n64": ["nintendo 64"], "gamecube": ["gc"], "ps1": ["playstation 1", "psx"],
    "ps2": ["playstation 2"], "local": ["local control", "cloud-free"], "vacuum": ["robot"],
}


def load():
    path = os.environ.get("RE_INDEX_DATA")
    if path:
        return json.load(open(path))
    fresh = os.path.exists(CACHE) and time.time() - os.path.getmtime(CACHE) < 86400
    if not fresh:
        try:
            with urllib.request.urlopen(RAW, timeout=20) as r:
                data = r.read()
            os.makedirs(os.path.dirname(CACHE), exist_ok=True)
            open(CACHE, "wb").write(data)
        except Exception as ex:
            print(f"note: could not refresh index ({ex}); using local copy", file=sys.stderr)
    for p in (CACHE, BUNDLED):
        if os.path.exists(p):
            return json.load(open(p))
    sys.exit("error: no index data found (no network and no local data/entries.json)")


def fields(e):
    slug = e["url"].rstrip("/").split("/")[-1]
    return [
        (3.0, e["name"].lower()), (3.0, slug.lower().replace("-", " ").replace("_", " ")),
        (2.0, " ".join(e.get("topics") or []).lower().replace("-", " ")),
        (1.5, e.get("desc", "").lower()), (1.0, e.get("subcategory", "").lower()),
        (1.0, e.get("category", "").lower()), (1.0, (e.get("platform") or "").lower()),
    ]


def hit(term, text):
    if len(term) <= 3:
        return re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", text) is not None
    return term in text


def score(e, terms):
    fs = fields(e)
    matched, total = 0, 0.0
    for t in terms:
        best = 0.0
        for alt in [t] + SYNONYMS.get(t, []):
            for w, text in fs:
                if hit(alt, text):
                    best = max(best, w if alt == t else w * 0.7)
        if best:
            matched += 1
            total += best
    if not matched:
        return None
    total += 0.8 * math.log10((e.get("stars") or 0) + 1)
    if e.get("archived"):
        total -= 1.0
    if (e.get("pushed") or "9999") < time.strftime("%Y", time.gmtime(time.time() - 3 * 365 * 86400)):
        total -= 0.5
    return (matched, total)


def search(entries, terms, category=None, lang=None, min_stars=0, include_archived=False, limit=12):
    """Rank entries for the search terms. Returns (results, full) where full is the
    list of entries that match every term; results put those first, then partial matches."""
    res = []
    for e in entries:
        if category and category.lower() not in (e["category"] + " " + e.get("subcategory", "")).lower():
            continue
        if lang and (e.get("lang") or "").lower() != lang.lower():
            continue
        if (e.get("stars") or 0) < min_stars or (e.get("archived") and not include_archived):
            continue
        sc = score(e, terms)
        if sc:
            res.append((sc, e))
    res.sort(key=lambda x: (-x[0][0], -x[0][1]))
    full = [e for (m, _), e in res if m == len(terms)]
    partial = [e for (m, _), e in res if m < len(terms)]
    return (full + partial)[:limit], full


def fmt(i, e):
    meta = [f"★{e['stars']:,}" if e.get("stars") is not None else None, e.get("lang") or None,
            e.get("license") or None, f"pushed {e['pushed']}" if e.get("pushed") else None,
            "ARCHIVED" if e.get("archived") else None]
    where = e["category"] + (f" › {e['subcategory']}" if e.get("subcategory") else "")
    return (f"{i}. {e['name']}  " + " · ".join(m for m in meta if m) + f"\n   {e['url']}\n"
            f"   {e.get('desc', '')}  [{where}]")


def find(entries, ref):
    ref = ref.strip().rstrip("/").lower()
    ref = re.sub(r"^https?://(www\.)?", "", ref)
    if "/" in ref and not ref.startswith(("github.com", "gitlab.com", "codeberg.org")):
        ref = "github.com/" + ref
    for e in entries:
        if re.sub(r"^https?://(www\.)?", "", e["url"].rstrip("/").lower()) == ref:
            return e
    return None


def github_readme(url):
    m = re.match(r"https?://github\.com/([^/]+)/([^/#?]+)", url)
    if not m:
        return None
    req = urllib.request.Request(f"https://api.github.com/repos/{m[1]}/{m[2]}/readme",
                                 headers={"Accept": "application/vnd.github.raw"})
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        try:
            token = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10).stdout.strip()
        except Exception:
            token = ""
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.read().decode("utf-8", "replace")
    except Exception as ex:
        return f"(could not fetch README: {ex})"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("words", nargs="+")
    s.add_argument("--category"); s.add_argument("--lang"); s.add_argument("--min-stars", type=int, default=0)
    s.add_argument("--include-archived", action="store_true"); s.add_argument("--limit", type=int, default=12)
    s.add_argument("--json", action="store_true")
    i = sub.add_parser("info"); i.add_argument("repo"); i.add_argument("--lines", type=int, default=80)
    c = sub.add_parser("clone"); c.add_argument("repo"); c.add_argument("--dest")
    sub.add_parser("categories")
    a = ap.parse_args()
    entries = load()

    if a.cmd == "categories":
        counts = {}
        for e in entries:
            counts.setdefault(e["category"], {}).setdefault(e.get("subcategory", ""), 0)
            counts[e["category"]][e.get("subcategory", "")] += 1
        for cat in sorted(counts):
            print(f"{cat} ({sum(counts[cat].values())})")
            for sc, n in sorted(counts[cat].items(), key=lambda x: -x[1]):
                print(f"  - {sc} ({n})")
        return

    if a.cmd == "search":
        terms = [t for t in re.split(r"[\s,]+", " ".join(a.words).lower()) if t]
        out, full = search(entries, terms, a.category, a.lang, a.min_stars, a.include_archived, a.limit)
        if a.json:
            print(json.dumps(out, indent=1, ensure_ascii=False)); return
        if not out:
            print("No matches. Try fewer or broader words, a synonym, or `categories`."); return
        if not full:
            print(f"(no project matches all of: {' '.join(terms)} — showing partial matches)\n")
        for n, e in enumerate(out, 1):
            print(fmt(n, e)); print()
        return

    e = find(entries, a.repo)
    url = e["url"] if e else ("https://github.com/" + a.repo if not a.repo.startswith("http") else a.repo)
    if a.cmd == "info":
        print(fmt(1, e) if e else f"(not in index) {url}")
        readme = github_readme(url)
        if readme:
            lines = readme.splitlines()
            print("\n--- README (first %d of %d lines) ---" % (min(a.lines, len(lines)), len(lines)))
            print("\n".join(lines[: a.lines]))
        return

    if a.cmd == "clone":
        dest = a.dest or os.path.join("vendor", url.rstrip("/").split("/")[-1])
        subprocess.run(["git", "clone", "--depth", "1", url, dest], check=True)
        lic = (e or {}).get("license") or "unknown — check the repo"
        print(f"\ncloned to {dest}\nlicense: {lic}")


if __name__ == "__main__":
    main()
