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

## `creators.json`

The source-of-truth list of benchmark creators (slug, name, archetype, YouTube
URL, LinkedIn URL). Editing this drives what `collect.py` fetches and keeps it in
sync with `research/sources.md`.
