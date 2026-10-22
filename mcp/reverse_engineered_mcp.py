#!/usr/bin/env python3
"""MCP server (stdio) for the awesome-reverse-engineered index.

Tools: search_reverse_engineered, get_reverse_engineered_project, list_reverse_engineered_categories.
Standard library only. Search and data loading come from re_index.py (a copy of the
agent skill's script, kept in step by scripts/render.py).

Run: python3 reverse_engineered_mcp.py
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import re_index  # noqa: E402

NAME, VERSION = "reverse-engineered", "0.1.0"
PROTOCOLS = ("2025-06-18", "2025-03-26", "2024-11-05")

TOOLS = [
    {
        "name": "search_reverse_engineered",
        "description": (
            "Search 12,000+ open-source projects that exist because someone reverse engineered a closed app, "
            "API, device, protocol, file format, game or AI product: unofficial API clients, local-control "
            "libraries, drivers, format parsers, protocol docs, game decompilations. Use it before you reverse "
            "engineer something, or when a task needs a product that has no official API or SDK. Search by "
            "product, vendor, protocol or task, for example 'tuya local', 'psd parser', 'bambu printer', 'n64 decomp'."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Product, vendor, protocol or task words."},
                "category": {"type": "string", "description": "Optional text that the category or subcategory must contain, for example 'Automotive'."},
                "language": {"type": "string", "description": "Optional primary language, for example 'Python'."},
                "min_stars": {"type": "integer", "minimum": 0, "default": 0},
                "include_archived": {"type": "boolean", "default": False},
                "limit": {"type": "integer", "minimum": 1, "maximum": 50, "default": 10},
            },
            "required": ["query"],
        },
        "annotations": {"readOnlyHint": True, "openWorldHint": True},
    },
    {
        "name": "get_reverse_engineered_project",
        "description": "Return one project's index entry (stars, license, last push, archived, category) and the start of its README.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "repo": {"type": "string", "description": "owner/repo or a repository URL."},
                "readme_lines": {"type": "integer", "minimum": 0, "maximum": 400, "default": 80},
            },
            "required": ["repo"],
        },
        "annotations": {"readOnlyHint": True, "openWorldHint": True},
    },
    {
        "name": "list_reverse_engineered_categories",
        "description": "List the index's categories and subcategories with project counts.",
        "inputSchema": {"type": "object", "properties": {}},
        "annotations": {"readOnlyHint": True},
    },
]

_entries = None


def entries():
    global _entries
    if _entries is None:
        _entries = re_index.load()
    return _entries


def slim(e):
    keep = ("name", "url", "desc", "category", "subcategory", "platform", "stars", "lang", "license", "pushed", "archived")
    return {k: e[k] for k in keep if e.get(k) not in (None, "")}


def call(name, args):
    if name == "search_reverse_engineered":
        terms = [t for t in re.split(r"[\s,]+", str(args.get("query", "")).lower()) if t]
        if not terms:
            raise ValueError("query is empty")
        out, full = re_index.search(entries(), terms, args.get("category"), args.get("language"),
                                    int(args.get("min_stars") or 0), bool(args.get("include_archived")),
                                    max(1, min(50, int(args.get("limit") or 10))))
        if not out:
            text = "No matches. Try fewer or broader words, a vendor name, or list_reverse_engineered_categories."
        else:
            head = "" if full else f"(no project matches all of: {' '.join(terms)}; showing partial matches)\n\n"
            text = head + "\n\n".join(re_index.fmt(i, e) for i, e in enumerate(out, 1))
        return text, {"results": [slim(e) for e in out], "all_terms_matched": bool(full)}
    if name == "get_reverse_engineered_project":
        ref = str(args.get("repo", "")).strip()
        if not ref:
            raise ValueError("repo is empty")
        e = re_index.find(entries(), ref)
        url = e["url"] if e else (ref if ref.startswith("http") else "https://github.com/" + ref)
        n = max(0, min(400, int(args.get("readme_lines", 80))))
        text = re_index.fmt(1, e) if e else f"(not in the index) {url}"
        readme = re_index.github_readme(url) if n else None
        if readme:
            lines = readme.splitlines()
            text += f"\n\n--- README (first {min(n, len(lines))} of {len(lines)} lines) ---\n" + "\n".join(lines[:n])
        return text, {"entry": slim(e) if e else None, "url": url}
    if name == "list_reverse_engineered_categories":
        counts = {}
        for e in entries():
            sub = counts.setdefault(e["category"], {})
            sub[e.get("subcategory", "")] = sub.get(e.get("subcategory", ""), 0) + 1
        lines = []
        for cat in sorted(counts):
            lines.append(f"{cat} ({sum(counts[cat].values())})")
            lines += [f"  - {s} ({n})" for s, n in sorted(counts[cat].items(), key=lambda x: -x[1])]
        return "\n".join(lines), {"categories": {c: sum(v.values()) for c, v in counts.items()}}
    raise KeyError(name)


def handle(msg):
    method, mid, params = msg.get("method"), msg.get("id"), msg.get("params") or {}
    if mid is None:  # notification
        return None
    if method == "initialize":
        asked = params.get("protocolVersion")
        return {"protocolVersion": asked if asked in PROTOCOLS else PROTOCOLS[0],
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": NAME, "version": VERSION},
                "instructions": "Search this index before reverse engineering a closed product: someone may have done it already."}
    if method == "ping":
        return {}
    if method == "tools/list":
        return {"tools": TOOLS}
    if method == "tools/call":
        name, args = params.get("name"), params.get("arguments") or {}
        if name not in {t["name"] for t in TOOLS}:
            raise LookupError(f"unknown tool: {name}")
        try:
            text, data = call(name, args)
            return {"content": [{"type": "text", "text": text}], "structuredContent": data, "isError": False}
        except Exception as ex:
            return {"content": [{"type": "text", "text": f"error: {ex}"}], "isError": True}
    raise NotImplementedError(method)


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except ValueError:
            reply = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "parse error"}}
        else:
            try:
                result = handle(msg)
                if result is None:
                    continue
                reply = {"jsonrpc": "2.0", "id": msg.get("id"), "result": result}
            except NotImplementedError as ex:
                reply = {"jsonrpc": "2.0", "id": msg.get("id"), "error": {"code": -32601, "message": f"method not found: {ex}"}}
            except LookupError as ex:
                reply = {"jsonrpc": "2.0", "id": msg.get("id"), "error": {"code": -32602, "message": str(ex)}}
        sys.stdout.write(json.dumps(reply, ensure_ascii=False) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
