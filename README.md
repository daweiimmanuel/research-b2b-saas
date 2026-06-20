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
   teaching from lived experience (Dan Martell, Jason Lemkin, Noah Kagan).
   Benchmarked for experience-based authority and turning interviews/keynotes
   into evergreen libraries.
2. **Marketing / growth practitioners** — tactics and frameworks from people who
   run marketing for a living (Neil Patel, Eric Siu, Adam Erhart). Benchmarked
   for high-volume how-to production, tight single-topic scripting, and
   one-input-to-many repurposing.
3. **B2B demand-gen & positioning voices** — contrarian POV aimed squarely at
   B2B SaaS marketers (Chris Walker, Dave Gerhardt). Benchmarked for
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
├── sources.md            # Master list: every expert with links, dates, annotations
├── linkedin-posts/       # Recent LinkedIn posts, organized by author
│   └── <author-slug>/
├── youtube-transcripts/  # Transcripts, organized by video
│   └── <author-slug>/
└── other/                # Additional materials (notes, raw dumps)
```

## Data collection

Recent content is collected through the [Supadata API](https://supadata.ai)
(YouTube channel-videos + transcript endpoints, and LinkedIn endpoints). The
collection script lives in `research/other/` and reads the API key from the
`SUPADATA_API_KEY` environment variable.

> ⚠️ **Egress access required.** This environment's network policy currently
> blocks `api.supadata.ai`, so the live collection step cannot run from here yet.
> The creator catalog, links, and structure are in place; once `api.supadata.ai`
> is added to the environment's network egress allowlist (or the script is run in
> an environment with outbound access), the `linkedin-posts/` and
> `youtube-transcripts/` directories will be populated. See
> [Claude Code on the web — network access](https://code.claude.com/docs/en/claude-code-on-the-web).
