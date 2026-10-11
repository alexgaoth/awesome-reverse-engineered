#!/usr/bin/env python3
"""Refresh data/entries.json from the GitHub API.

For each GitHub entry: canonical URL, stars, archived, last push, language,
license and topics. Repos that GitHub reports as NOT_FOUND are removed and
logged in data/removed.json. Other hosts get an HTTP check; they are removed
only after failing on 3 separate runs.

Needs GITHUB_TOKEN (or GH_TOKEN). Writes a Markdown summary to
$GITHUB_STEP_SUMMARY when set, and to stdout.

Usage: python3 scripts/refresh.py [--limit N] [--dry-run]
"""
import argparse, datetime, json, os, re, sys, time, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "entries.json")
REMOVED = os.path.join(ROOT, "data", "removed.json")
BATCH = 50
MAX_REMOVE_SHARE = 0.03  # more than this in one run means something is wrong upstream: change nothing
TODAY = datetime.date.today().isoformat()


def gh_parts(url):
    m = re.match(r"https?://(?:www\.)?github\.com/([^/#?]+)/([^/#?]+)", url)
    return (m.group(1), re.sub(r"\.git$", "", m.group(2))) if m else None


def graphql(query, token):
    body = json.dumps({"query": query}).encode()
    for attempt in range(6):
        req = urllib.request.Request("https://api.github.com/graphql", data=body,
                                     headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                resp = json.load(r)
        except urllib.error.HTTPError as ex:
            if ex.code in (403, 429, 502, 503):
                time.sleep(int(ex.headers.get("Retry-After") or 30 * (attempt + 1)))
                continue
            raise
        except urllib.error.URLError:
            time.sleep(15 * (attempt + 1))
            continue
        errs = resp.get("errors") or []
        if any(e.get("type") in ("RATE_LIMITED", "INTERNAL") for e in errs) and not resp.get("data"):
            time.sleep(60 * (attempt + 1))
            continue
        return resp
    raise RuntimeError("GraphQL failed after retries")


def http_ok(url):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": "awesome-reverse-engineered-refresh"})
            with urllib.request.urlopen(req, timeout=20) as r:
                if r.status < 400:
                    return True
        except urllib.error.HTTPError as ex:
            if ex.code in (403, 405, 429) and method == "HEAD":
                continue
            if ex.code in (403, 429):
                return True  # blocked or throttled is not dead
        except Exception:
            pass
    return False


def norm(u):
    return re.sub(r"^https?://(www\.)?", "", u.strip().rstrip("/").lower())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, help="check only the first N GitHub entries (for testing)")
    ap.add_argument("--dry-run", action="store_true", help="do not write files")
    a = ap.parse_args()
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        sys.exit("error: set GITHUB_TOKEN")

    entries = json.load(open(DATA))
    before = {norm(e["url"]): dict(e) for e in entries}
    gh = [e for e in entries if gh_parts(e["url"])]
    if a.limit:
        gh = gh[: a.limit]
    gone, renamed, star_delta, newly_archived = [], [], 0, []

    for i in range(0, len(gh), BATCH):
        batch = gh[i:i + BATCH]
        q = " ".join(
            f'r{j}: repository(owner: {json.dumps(o)}, name: {json.dumps(n)}) {{ url stargazerCount isArchived pushedAt '
            f'primaryLanguage {{ name }} licenseInfo {{ spdxId }} repositoryTopics(first: 6) {{ nodes {{ topic {{ name }} }} }} }}'
            for j, (o, n) in enumerate(gh_parts(e["url"]) for e in batch))
        resp = graphql("{" + q + "}", token)
        data = resp.get("data") or {}
        notfound = {err["path"][0] for err in resp.get("errors", []) if err.get("type") == "NOT_FOUND" and err.get("path")}
        for j, e in enumerate(batch):
            r = data.get(f"r{j}")
            if r is None:
                if f"r{j}" in notfound:
                    gone.append(e)
                continue
            if "/tree/" not in e["url"] and "/blob/" not in e["url"] and norm(r["url"]) != norm(e["url"]):
                renamed.append((e["url"], r["url"]))
                e["url"] = r["url"]
            star_delta += r["stargazerCount"] - (e.get("stars") or 0)
            if r["isArchived"] and not e.get("archived"):
                newly_archived.append(e)
            e.update(stars=r["stargazerCount"], archived=r["isArchived"], pushed=(r["pushedAt"] or "")[:10],
                     lang=(r.get("primaryLanguage") or {}).get("name") or "",
                     license=(r.get("licenseInfo") or {}).get("spdxId") or "",
                     topics=[t["topic"]["name"] for t in (r.get("repositoryTopics") or {}).get("nodes", [])])
        print(f"batch {i // BATCH + 1}/{(len(gh) + BATCH - 1) // BATCH}", file=sys.stderr)

    # Non-GitHub hosts: remove only after 3 failed runs.
    other_dead = []
    if not a.limit:
        for e in entries:
            if gh_parts(e["url"]):
                continue
            if http_ok(e["url"]):
                e.pop("failures", None)
            else:
                e["failures"] = e.get("failures", 0) + 1
                if e["failures"] >= 3:
                    other_dead.append(e)

    remove = gone + other_dead
    if len(remove) > max(10, MAX_REMOVE_SHARE * len(entries)):
        sys.exit(f"error: {len(remove)} removals is more than {MAX_REMOVE_SHARE:.0%} of the index; refusing to change anything")
    drop = {id(e) for e in remove}
    kept, seen = [], set()
    for e in entries:  # also dedupe repos that converged after renames
        k = norm(e["url"])
        if id(e) in drop or k in seen:
            continue
        seen.add(k)
        kept.append(e)

    lines = [f"## Nightly refresh {TODAY}", "",
             f"- Checked {len(gh):,} GitHub repos; {len(kept):,} entries remain.",
             f"- Stars changed by {star_delta:+,} in total.",
             f"- Renamed or moved: {len(renamed)}. Newly archived: {len(newly_archived)}.",
             f"- Removed: {len(remove)} ({len(gone)} gone from GitHub, {len(other_dead)} other hosts dead 3 runs in a row)."]
    if remove:
        lines += ["", "Removed:"] + [f"- {e['name']} — {e['url']}" for e in remove]
    if renamed:
        lines += ["", "Renamed:"] + [f"- {a} → {b}" for a, b in renamed[:50]]
    if newly_archived:
        lines += ["", "Newly archived:"] + [f"- {e['name']} — {e['url']}" for e in newly_archived[:50]]
    summary = "\n".join(lines) + "\n"
    print(summary)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        open(os.environ["GITHUB_STEP_SUMMARY"], "a").write(summary)
    open(os.path.join(ROOT, "refresh-summary.md"), "w").write(summary)

    if a.dry_run:
        return
    json.dump(kept, open(DATA, "w"), indent=1, ensure_ascii=False)
    open(DATA, "a").write("\n")
    if remove:
        log = json.load(open(REMOVED)) if os.path.exists(REMOVED) else []
        log += [{"url": e["url"], "name": e["name"], "removed": TODAY,
                 "reason": "not found on GitHub" if e in gone else "unreachable on 3 runs"} for e in remove]
        json.dump(log, open(REMOVED, "w"), indent=1, ensure_ascii=False)
        open(REMOVED, "a").write("\n")


if __name__ == "__main__":
    main()
