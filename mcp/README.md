# reverse-engineered MCP server

MCP server for [awesome-reverse-engineered](https://github.com/alexgaoth/awesome-reverse-engineered): 12,000+ open-source projects that exist because someone reverse engineered a closed app, API, device, protocol, file format, game or AI product.

Don't reverse engineer it twice: your agent searches the index before it starts.

## Tools

| Tool | What it does |
|---|---|
| `search_reverse_engineered` | Ranked search by product, vendor, protocol or task (`tuya local`, `psd parser`, `n64 decomp`). Filters: category, language, minimum stars, archived. |
| `get_reverse_engineered_project` | One entry (stars, license, last push, archived) plus the start of its README. |
| `list_reverse_engineered_categories` | Categories and subcategories with counts. |

## Install

Needs [uv](https://docs.astral.sh/uv/). No other dependencies (Python standard library only).

Claude Code:

```bash
claude mcp add reverse-engineered -- uvx --from "git+https://github.com/alexgaoth/awesome-reverse-engineered#subdirectory=mcp" reverse-engineered-mcp
```

Claude Desktop, Cursor and other clients:

```json
{
  "mcpServers": {
    "reverse-engineered": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/alexgaoth/awesome-reverse-engineered#subdirectory=mcp", "reverse-engineered-mcp"]
    }
  }
}
```

Without uv: download `reverse_engineered_mcp.py` and `re_index.py` into one folder and run `python3 reverse_engineered_mcp.py`.

## Data

The server downloads `data/entries.json` (CC0) on first use and caches it for 24 hours in `~/.cache/awesome-reverse-engineered/`. Set `RE_INDEX_DATA=/path/to/entries.json` to use a local copy. `get_reverse_engineered_project` reads READMEs through the GitHub API; set `GITHUB_TOKEN` for a higher rate limit.

`re_index.py` is a copy of the agent skill's script; `scripts/render.py` keeps it in step.
