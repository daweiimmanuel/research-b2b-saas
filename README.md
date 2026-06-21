# research-b2b-saas

Research repository for studying independent creators and founder-educators in
the B2B SaaS space — collecting their recent content (LinkedIn posts, YouTube
transcripts) to benchmark **craft, point of view, and publishing cadence**.

## Why these experts

These are individuals already producing content worth studying. They were chosen
because each represents a distinct, repeatable **format archetype** — so the
list isn't "famous marketers," it's "one strong model per way of building an
audience." That makes it possible to pick the creator whose model matches what
you want to build, then study exactly how they do it.

The list was reduced from 13 candidates to the **10 strongest** using a
transparent rubric — each scored **/25** across **B2B-SaaS relevance · content
craft · cadence/volume · repurposability · archetype uniqueness.** See the full
scoring table (and the three considered-but-not-selected creators) in
[`research/sources.md`](research/sources.md). `research/other/creators.json` is
the source of truth that drives collection.

The selection is grouped by archetype:

1. **Founder / operator educators** — *the trust archetype.* Real operators
   teaching from lived experience (Dan Martell, Jason Lemkin, Adam Robinson).
   Benchmarked for experience-based authority and turning interviews/keynotes
   into evergreen libraries.
2. **Marketing / growth practitioners** — tactics and frameworks from people who
   run marketing for a living (Neil Patel, Eric Siu, Adam Erhart). Benchmarked
   for high-volume how-to production, tight single-topic scripting, and
   one-input-to-many repurposing.
3. **B2B demand-gen & positioning voices** — contrarian POV aimed squarely at
   B2B SaaS marketers (April Dunford, Dave Gerhardt). Benchmarked for
   framework-driven, category-defining opinion content.
4. **Interview / podcast-led (deep authority)** — Lenny Rachitsky. The benchmark
   for interview depth: booking great guests, tight chaptering, and atomizing
   each episode into many clips.
5. **Sales / outbound** — Josh Braun. The benchmark for weekly cadence and
   tight, single-idea videos that each teach one move.
6. **Honest review creators (BOFU benchmark)** — independent reviewers
   (HelperMan, Consumer Research Studios, Merchant Maverick) that dominate
   AI/search citations for buying-intent queries. Kept as a *reference*
   benchmark only — not part of the scored top-10 collection set.

The full table — with focus, the specific reason each is a benchmark, and
links — lives in [`research/sources.md`](research/sources.md).

> **Note on scale figures:** subscriber/follower counts are approximate and move
> constantly. Treat them as rough scale, not exact, and verify before modeling
> anyone.

## Repository structure

```
research/
├── index.md              # Auto-generated navigable TOC of all collected content
├── sources.md            # Master list: every expert with links, dates, annotations
├── linkedin-posts/       # Recent LinkedIn posts, organized by author
│   └── <author-slug>/
├── youtube-transcripts/  # Transcripts, organized by video
│   └── <author-slug>/
└── other/                # Additional materials (notes, raw dumps)
```

## Data collection

Two content types, two collection paths. Both write one file per item into
`research/<type>/<author-slug>/` and are indexed by
`research/other/make_index.py`. The creator list, slugs, channel/profile URLs,
and target videos live in [`research/other/creators.json`](research/other/creators.json).

### YouTube transcripts (automated)

Collected via the [Supadata](https://supadata.ai) `transcript` tool. Supadata
can't read YouTube's JS-rendered video lists (`map`/`scrape` only return page
chrome), so the most-recent video per creator is discovered from each channel's
**RSS feed** (`https://www.youtube.com/feeds/videos.xml?channel_id=<id>`) and
then transcribed. For local/CI runs against the REST API, use
`research/other/collect.py` (reads `SUPADATA_API_KEY`) — see
[`research/other/README.md`](research/other/README.md).

### LinkedIn posts (manual, browser-assisted)

LinkedIn requires an authenticated session — server-side/API scraping returns
`403 Forbidden`. So posts are collected with the **Claude for Chrome extension**
in a logged-in browser, using a fixed prompt whose output drops straight into the
repo format.

**Steps**

1. Log in to LinkedIn in Chrome with the Claude extension enabled.
2. Open the creator's activity feed:
   `https://www.linkedin.com/in/<handle>/recent-activity/all/`
   (handles are in `creators.json`; e.g. `josh-braun` → `josh-braun`).
3. Paste the prompt below. It scrolls to lazy-load posts, expands every "…more",
   and returns the 10 most recent **original** posts verbatim with permalink,
   date, type, and engagement counts.
4. Paste the extension's output back into this repo's Claude Code session (or save
   it yourself). Each post becomes
   `research/linkedin-posts/<slug>/<activityId>.md` — one file per post.
5. Refresh the navigable index: `python3 research/other/make_index.py`.

**Collection prompt** (run per creator on their open activity page):

```
You are looking at a LinkedIn profile's "Posts/Activity" tab in my logged-in
browser. Extract this person's 10 most recent ORIGINAL posts.

- Scroll to lazy-load until you have 10 qualifying posts (or reach the end).
- Click every "…more" so you capture FULL text, not the preview.
- Include original posts + reshares where THEY added commentary (capture only
  their commentary, note in one line what they reshared). Exclude pure reposts
  and their comments on others' posts.
- Capture text VERBATIM (keep line breaks/emojis); never summarize or invent.
  Missing value = "unknown". Convert relative timestamps to YYYY-MM-DD.

Return one block per post, newest first:

## Post N
- Post URL: <permalink>
- Activity ID: <7xxxx… from the URL>
- Posted: <YYYY-MM-DD> (<relative label>)
- Type: original | reshare-with-commentary
- Reactions: <n> | Comments: <n> | Reposts: <n>

<full verbatim text>
```

To do all 10 creators in a single run, give the extension a batch version of the
prompt with the full URL list (one entry per creator from `creators.json`) and
ask it to visit each in order. Tip: emphasize "scroll until 10 posts load" — a
feed that isn't scrolled often yields only the first post.

> **Note:** `research/other/collect.py` also includes a best-effort
> `collect_linkedin()` against Supadata's REST LinkedIn endpoint, for accounts/
> environments where that endpoint is available; the manual browser flow above is
> the reliable path when it isn't.
