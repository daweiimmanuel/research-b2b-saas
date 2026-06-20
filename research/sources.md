# Sources — Creator / Founder-Educator Benchmarks

This file catalogs the **top 10** independent creators and founder-educators
selected as benchmarks for B2B SaaS content craft, POV, and cadence. They are
grouped by **format archetype** so each can be matched to a model worth
emulating.

- **Subscriber/scale figures are approximate** and move constantly — treat them
  as rough scale, not exact. Verify before modeling anyone.
- **Collection date:** content pulled via the [Supadata API](https://supadata.ai)
  on **2026-06-20**. Per-item publish dates live alongside each collected
  artifact in `linkedin-posts/` and `youtube-transcripts/`.

## Selection & scoring

The list was reduced from 13 candidates to the **10 strongest** by a transparent
rubric. Each creator is scored **/25** across five equally-weighted dimensions:
**B2B-SaaS relevance · content craft · cadence/volume · repurposability ·
archetype uniqueness.** `creators.json` is the source of truth that drives
`collect.py`.

| Rank | Creator | Archetype | Score /25 |
|---|---|---|---|
| 1 | Lenny Rachitsky | Interview / podcast-led | 24 |
| 2 | Dan Martell | Founder / operator educator | 23 |
| 3 | Neil Patel | Marketing / growth practitioner | 23 |
| 4 | Josh Braun | Sales / outbound | 23 |
| 5 | Chris Walker | B2B demand-gen & positioning | 22 |
| 6 | Jason Lemkin | Founder / operator educator | 22 |
| 7 | Eric Siu | Marketing / growth practitioner | 22 |
| 8 | Adam Erhart | Marketing / growth practitioner | 21 |
| 9 | Dave Gerhardt | B2B demand-gen & positioning | 21 |
| 10 | Noah Kagan | Founder / operator educator | 19 |

**Considered but not selected:**

- **Gary Vaynerchuk** (19) — elite volume/repurposing, but mass-market reach
  dilutes B2B-SaaS relevance.
- **Nathan Latka** (18) — SaaS-relevant, but his founder-interview lane overlaps
  Lemkin/Martell and craft is inconsistent.
- **Sujan Patel** (13) — strong practitioner credibility, but no real YouTube
  presence and low publishing cadence/repurposability.

---

## 1. Founder / operator educators

Real operators teaching from experience — the trust archetype.

| Creator / channel | Focus | Why benchmark them | YouTube | LinkedIn |
|---|---|---|---|---|
| **Dan Martell** (SaaS Academy) | Scaling SaaS founders; coaching; "Escape Velocity" interviews, keynotes | Clear, experience-based advice; strong personal brand + interview/keynote repurposing | [@DanMartell](https://www.youtube.com/@DanMartell) | [in/danmartell](https://www.linkedin.com/in/danmartell) |
| **Jason Lemkin** (SaaStr) | Long talks, keynotes, panels from major SaaS events | Turning event content into an evergreen library; real operator stories at scale | [@SaaStr](https://www.youtube.com/@SaaStr) | [in/jasonmlemkin](https://www.linkedin.com/in/jasonmlemkin) |
| **Noah Kagan** (Noah Kagan Presents) | Building businesses/SaaS, experiments, founder interviews | Energetic, experiment-driven storytelling; strong hooks and thumbnails | [@noahkagan](https://www.youtube.com/@noahkagan) | [in/noahkagan](https://www.linkedin.com/in/noahkagan) |

## 2. Marketing / growth practitioners

Tactics and frameworks from people who run marketing for a living.

| Creator / channel | Focus | Why benchmark them | YouTube | LinkedIn |
|---|---|---|---|---|
| **Neil Patel** | SEO, content, and digital marketing tutorials | The benchmark for high-volume, actionable how-to content and search-driven topics | [@neilpatel](https://www.youtube.com/@neilpatel) | [in/neilkpatel](https://www.linkedin.com/in/neilkpatel) |
| **Eric Siu** (Leveling Up / Marketing School) | Marketing interviews + daily tactical lessons (~160–190K) | Master of podcast-to-YouTube repurposing; interview-led authority that feeds an agency | [@LevelingUpOfficial](https://www.youtube.com/@LevelingUpOfficial) | [in/ericosiu](https://www.linkedin.com/in/ericosiu) |
| **Adam Erhart** | Marketing strategy explainers (~665K) | The benchmark for clean, well-produced single-topic marketing videos with tight scripting | [@Adamerhartvideo](https://www.youtube.com/@Adamerhartvideo) | [in/adamerhart](https://www.linkedin.com/in/adamerhart) |

## 3. B2B demand-gen & positioning voices

Contrarian POV and frameworks aimed squarely at B2B SaaS marketers.

| Creator / channel | Focus | Why benchmark them | YouTube | LinkedIn |
|---|---|---|---|---|
| **Chris Walker** (Revenue Vitals / Refine Labs) | Demand generation, dark social, GTM measurement | The benchmark for contrarian POV + framework content that drives a category conversation | [@RefineLabs](https://www.youtube.com/@RefineLabs) | [in/chriswalker171](https://www.linkedin.com/in/chriswalker171) |
| **Dave Gerhardt** (Exit Five) | B2B positioning, messaging, brand, sales-marketing alignment | Community-led B2B marketing content; strong narrative and opinion | [@exitfive](https://www.youtube.com/@exitfive) | [in/davegerhardt](https://www.linkedin.com/in/davegerhardt) |

## 4. Interview / podcast-led (deep authority)

| Creator / channel | Focus | Why benchmark them | YouTube | LinkedIn |
|---|---|---|---|---|
| **Lenny Rachitsky** (Lenny's Podcast) | Product, growth, and career interviews with top operators (~1M+) | The benchmark for interview-led depth — booking great guests, tight chaptering, and atomizing each episode into many clips | [@LennysPodcast](https://www.youtube.com/@LennysPodcast) | [in/lennyrachitsky](https://www.linkedin.com/in/lennyrachitsky) |

## 5. Sales / outbound

| Creator / channel | Focus | Why benchmark them | YouTube | LinkedIn |
|---|---|---|---|---|
| **Josh Braun** | Sales/prospecting, cold outreach | Weekly cadence; tight, single-idea videos that each teach one move | [@JoshBraun](https://www.youtube.com/@JoshBraun) | [in/josh-braun](https://www.linkedin.com/in/josh-braun) |

## Honest review creators (BOFU benchmark — reference, not collected)

Not part of the scored top-10 collection set, but kept here as a reference
benchmark. These dominate AI/search citations for buying-intent queries — the
benchmark for honest BOFU comparison video: **HelperMan**, **Consumer Research
Studios**, **Merchant Maverick** (honest software comparisons, "best tool for X"
reviews).

---

## Collection manifest

Per-creator collected content (LinkedIn posts and YouTube transcripts) is stored
under:

- `research/linkedin-posts/<author-slug>/` — recent posts, one file per post
- `research/youtube-transcripts/<author-slug>/` — recent videos, one file per video
- `research/other/` — additional materials (collection script, raw API dumps)

Collection is performed via Supadata's YouTube channel-videos + transcript
endpoints and LinkedIn endpoints. See the README for the collection script and
the current egress-access caveat.
