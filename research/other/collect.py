#!/usr/bin/env python3
"""Collect recent creator content via the Supadata API.

Reads research/other/creators.json and, for each creator, pulls:
  - recent YouTube videos + transcripts -> research/youtube-transcripts/<slug>/
  - recent LinkedIn posts               -> research/linkedin-posts/<slug>/

Supadata API (https://supadata.ai):
  Base URL : https://api.supadata.ai/v1
  Auth     : x-api-key: <SUPADATA_API_KEY>

Usage:
  export SUPADATA_API_KEY=sd_xxx
  python3 research/other/collect.py --limit 10
  python3 research/other/collect.py --only josh-braun --skip-linkedin

Notes:
  - The exact response shapes can differ slightly between API versions, so the
    parsers below are defensive (they accept several common field names).
  - LinkedIn listing support varies by plan; if the LinkedIn call fails the
    script logs it and continues with YouTube. Confirm the current LinkedIn
    endpoint in the Supadata docs for your account.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://api.supadata.ai/v1"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # research/
YT_DIR = os.path.join(ROOT, "youtube-transcripts")
LI_DIR = os.path.join(ROOT, "linkedin-posts")


def api_get(path: str, params: dict, api_key: str, retries: int = 4) -> dict:
    """GET BASE+path with x-api-key, exponential backoff on 429/5xx/network."""
    url = f"{BASE}{path}?{urllib.parse.urlencode(params)}"
    delay = 2
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers={"x-api-key": api_key})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")
            if e.code in (429, 500, 502, 503, 504) and attempt < retries:
                time.sleep(delay)
                delay *= 2
                continue
            raise RuntimeError(f"HTTP {e.code} for {url}\n{body}") from e
        except urllib.error.URLError as e:
            if attempt < retries:
                time.sleep(delay)
                delay *= 2
                continue
            raise RuntimeError(f"Network error for {url}: {e}") from e
    raise RuntimeError(f"Exhausted retries for {url}")


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", (text or "").lower()).strip()
    return re.sub(r"[\s_-]+", "-", text)[:80] or "untitled"


def write(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# --------------------------- YouTube ---------------------------

def list_channel_videos(channel: str, limit: int, api_key: str) -> list[str]:
    """Return up to `limit` recent video IDs for a channel URL/handle."""
    data = api_get("/youtube/channel/videos", {"id": channel, "limit": limit}, api_key)
    # Accept several documented/observed shapes.
    for key in ("videoIds", "videos", "ids"):
        if key in data:
            vids = data[key]
            return [v if isinstance(v, str) else v.get("id") or v.get("videoId") for v in vids]
    return []


def get_transcript(video_id: str, api_key: str) -> dict:
    return api_get("/youtube/transcript", {"videoId": video_id, "text": "true", "lang": "en"}, api_key)


def collect_youtube(creator: dict, limit: int, api_key: str) -> int:
    channel = creator.get("youtube")
    if not channel:
        return 0
    out_dir = os.path.join(YT_DIR, creator["slug"])
    print(f"  YouTube: listing up to {limit} videos for {channel}")
    try:
        video_ids = list_channel_videos(channel, limit, api_key)
    except RuntimeError as e:
        print(f"  ! channel list failed: {e}")
        return 0
    count = 0
    for vid in video_ids:
        if not vid:
            continue
        try:
            tr = get_transcript(vid, api_key)
        except RuntimeError as e:
            print(f"  ! transcript {vid} failed: {e}")
            continue
        content = tr.get("content")
        if isinstance(content, list):  # segmented form
            content = " ".join(seg.get("text", "") for seg in content)
        url = f"https://www.youtube.com/watch?v={vid}"
        body = (
            f"# {creator['name']} — YouTube video {vid}\n\n"
            f"- Source: {url}\n"
            f"- Language: {tr.get('lang', 'en')}\n"
            f"- Collected: {time.strftime('%Y-%m-%d')}\n\n"
            f"## Transcript\n\n{content or '(no transcript available)'}\n"
        )
        write(os.path.join(out_dir, f"{vid}.md"), body)
        count += 1
        print(f"    + {vid}.md")
        time.sleep(0.3)
    return count


# --------------------------- LinkedIn ---------------------------

def collect_linkedin(creator: dict, limit: int, api_key: str) -> int:
    """Best-effort LinkedIn recent-posts pull.

    Supadata's LinkedIn surface differs by plan. We try the documented
    person/posts shapes; on failure we log and move on so YouTube still runs.
    """
    profile = creator.get("linkedin")
    if not profile:
        return 0
    out_dir = os.path.join(LI_DIR, creator["slug"])
    print(f"  LinkedIn: pulling up to {limit} posts for {profile}")
    data = None
    for path, params in (
        ("/linkedin/posts", {"url": profile, "limit": limit}),
        ("/linkedin/person", {"url": profile}),
        ("/scrape", {"url": profile.rstrip("/") + "/recent-activity/all/"}),
    ):
        try:
            data = api_get(path, params, api_key)
            print(f"    using {path}")
            break
        except RuntimeError as e:
            print(f"    {path} unavailable: {str(e).splitlines()[0]}")
    if not data:
        print("  ! no LinkedIn endpoint succeeded; skipping")
        return 0

    posts = data.get("posts") or data.get("items") or ([data] if data.get("text") else [])
    count = 0
    for i, post in enumerate(posts[:limit], 1):
        text = post.get("text") or post.get("content") or ""
        pid = post.get("id") or post.get("urn") or f"post-{i:03d}"
        date = post.get("date") or post.get("postedAt") or "unknown"
        url = post.get("url") or profile
        body = (
            f"# {creator['name']} — LinkedIn post {pid}\n\n"
            f"- Source: {url}\n"
            f"- Posted: {date}\n"
            f"- Collected: {time.strftime('%Y-%m-%d')}\n\n"
            f"{text}\n"
        )
        write(os.path.join(out_dir, f"{slugify(pid)}.md"), body)
        count += 1
        print(f"    + {slugify(pid)}.md")
    return count


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=10, help="max items per source per creator")
    ap.add_argument("--only", help="comma-separated creator slugs to include")
    ap.add_argument("--skip-youtube", action="store_true")
    ap.add_argument("--skip-linkedin", action="store_true")
    args = ap.parse_args()

    api_key = os.environ.get("SUPADATA_API_KEY")
    if not api_key:
        print("ERROR: set SUPADATA_API_KEY in the environment.", file=sys.stderr)
        return 1

    with open(os.path.join(os.path.dirname(__file__), "creators.json"), encoding="utf-8") as f:
        creators = json.load(f)["creators"]

    if args.only:
        wanted = {s.strip() for s in args.only.split(",")}
        creators = [c for c in creators if c["slug"] in wanted]

    totals = {"youtube": 0, "linkedin": 0}
    for c in creators:
        print(f"\n=== {c['name']} ({c['slug']}) ===")
        if not args.skip_youtube:
            totals["youtube"] += collect_youtube(c, args.limit, api_key)
        if not args.skip_linkedin:
            totals["linkedin"] += collect_linkedin(c, args.limit, api_key)

    print(f"\nDone. YouTube files: {totals['youtube']}, LinkedIn files: {totals['linkedin']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
