# Sources — Creator / Founder-Educator Benchmarks

This file catalogs the independent creators and founder-educators selected as
benchmarks for B2B SaaS content craft, POV, and cadence. They are grouped by
**format archetype** so each can be matched to a model worth emulating.

- **Subscriber/scale figures are approximate** and move constantly — treat them
  as rough scale, not exact. Verify before modeling anyone.
- **Collection date:** content pulled via the [Supadata API](https://supadata.ai)
  on **2026-06-20**. Per-item publish dates live alongside each collected
  artifact in `linkedin-posts/` and `youtube-transcripts/`.
- **Status legend:** ⏳ = links cataloged, content collection pending API egress
  access (see README "Data collection" note).

---

## 1. Founder / operator educators

Real operators teaching from experience — the trust archetype.

| Creator / channel | Focus | Why benchmark them | YouTube | LinkedIn |
|---|---|---|---|---|
| **Dan Martell** (SaaS Academy) | Scaling SaaS founders; coaching; "Escape Velocity" interviews, keynotes | Clear, experience-based advice; strong personal brand + interview/keynote repurposing | [@DanMartell](https://www.youtube.com/@DanMartell) | [in/danmartell](https://www.linkedin.com/in/danmartell) |
| **Jason Lemkin** (SaaStr) | Long talks, keynotes, panels from major SaaS events | Turning event content into an evergreen library; real operator stories at scale | [@SaaStr](https://www.youtube.com/@SaaStr) | [in/jasonmlemkin](https://www.linkedin.com/in/jasonmlemkin) |
| **Nathan Latka** | SaaS metrics and founder interviews | Data-forward, founder-story format that's highly repurposable | [@NathanLatka](https://www.youtube.com/@NathanLatka) | [in/nathanlatka](https://www.linkedin.com/in/nathanlatka) |
| **Noah Kagan** (Noah Kagan Presents) | Building businesses/SaaS, experiments, founder interviews | Energetic, experiment-driven storytelling; strong hooks and thumbnails | [@noahkagan](https://www.youtube.com/@noahkagan) | [in/noahkagan](https://www.linkedin.com/in/noahkagan) |

## 2. Marketing / growth practitioners

Tactics and frameworks from people who run marketing for a living.

| Creator / channel | Focus | Why benchmark them | YouTube | LinkedIn |
|---|---|---|---|---|
| **Neil Patel** | SEO, content, and digital marketing tutorials | The benchmark for high-volume, actionable how-to content and search-driven topics | [@neilpatel](https://www.youtube.com/@neilpatel) | [in/neilkpatel](https://www.linkedin.com/in/neilkpatel) |
| **Eric Siu** (Leveling Up / Marketing School) | Marketing interviews + daily tactical lessons (~160–190K) | Master of podcast-to-YouTube repurposing; interview-led authority that feeds an agency | [@LevelingUpOfficial](https://www.youtube.com/@LevelingUpOfficial) | [in/ericosiu](https://www.linkedin.com/in/ericosiu) |
| **Adam Erhart** | Marketing strategy explainers (~665K) | The benchmark for clean, well-produced single-topic marketing videos with tight scripting | [@Adamerhartvideo](https://www.youtube.com/@Adamerhartvideo) | [in/adamerhart](https://www.linkedin.com/in/adamerhart) |
| **Sujan Patel** | Growth marketing for SaaS | Practitioner credibility from having built multiple SaaS companies | — (primarily LinkedIn) | [in/sujanpatel](https://www.linkedin.com/in/sujanpatel) |
| **Gary Vaynerchuk** | Marketing/business at scale | The benchmark for volume + repurposing — one input atomized into endless clips | [@garyvee](https://www.youtube.com/@garyvee) | [in/garyvaynerchuk](https://www.linkedin.com/in/garyvaynerchuk) |

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

## 6. Honest review creators (BOFU benchmark)

These dominate AI/search citations for buying-intent queries — the benchmark for
honest BOFU comparison video.

| Creator / channel | Focus | Why benchmark them |
|---|---|---|
| **HelperMan** | Honest software comparisons, "best tool for X" reviews | Buying-intent SEO; comparison-video format |
| **Consumer Research Studios** | Honest software comparisons and reviews | Buying-intent SEO; comparison-video format |
| **Merchant Maverick** | Software/payments reviews and comparisons | Editorial review authority that ranks for "best X" queries |

---

## Collection manifest

Per-creator collected content (LinkedIn posts and YouTube transcripts) is stored
under:

- `research/linkedin-posts/<author-slug>/` — recent posts, one file per post
- `research/youtube-transcripts/<author-slug>/` — recent videos, one file per video
- `research/other/` — additional materials (cross-creator notes, raw API dumps)

Collection is performed via Supadata's YouTube channel-videos + transcript
endpoints and LinkedIn endpoints. See the README for the collection script and
the current egress-access caveat.
