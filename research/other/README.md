# research/other — collection tooling & misc materials

## `collect.py`

Pulls recent content for every creator in `creators.json` via the
[Supadata API](https://supadata.ai) and writes:

- YouTube transcripts → `research/youtube-transcripts/<slug>/<videoId>.md`
- LinkedIn posts → `research/linkedin-posts/<slug>/<postId>.md`

### Run

```bash
export SUPADATA_API_KEY=sd_xxxxxxxx        # your Supadata key
python3 research/other/collect.py --limit 10
```

Useful flags:

| Flag | Effect |
|---|---|
| `--limit N` | max items per source per creator (default 10) |
| `--only slug1,slug2` | restrict to specific creators |
| `--skip-youtube` / `--skip-linkedin` | run only one source |

The script retries on `429`/`5xx`/network errors with exponential backoff and is
defensive about response shapes (Supadata field names vary slightly by version).

### Egress requirement

`api.supadata.ai` must be reachable from wherever this runs. In this Claude Code
web environment the network policy currently blocks that host — add it to the
environment's egress allowlist, or run the script locally / in CI with outbound
access. See
[Claude Code on the web — network access](https://code.claude.com/docs/en/claude-code-on-the-web).

## `make_index.py`

Generates navigable tables of contents for collected content:

- `research/youtube-transcripts/<slug>/index.md` — per-creator video TOC
- `research/linkedin-posts/<slug>/index.md` — per-creator post TOC
- `research/index.md` — master TOC across all creators (with counts + scores)

Each entry shows the item title (linked), date, source URL, and a short preview,
parsed from the metadata `collect.py` writes. It only indexes directories that
contain content, rewrites indexes idempotently, and never fails a collection run.

```bash
python3 research/other/make_index.py
```

`collect.py` calls this automatically at the end of a run, so a fresh collection
is immediately navigable. Run it standalone any time to refresh the indexes
(e.g. after manually adding files to `research/other/` content folders).

## `creators.json`

The source-of-truth list of benchmark creators (slug, name, archetype, YouTube
URL, LinkedIn URL). Editing this drives what `collect.py` fetches and keeps it in
sync with `research/sources.md`.
