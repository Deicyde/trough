#!/usr/bin/env python3
"""Record what trough maps of ATLAS's vault, from a checkout.

    python tools/refresh_atlas.py CHECKOUT [--site]

CHECKOUT is a git checkout of Deicyde/atlas-lean at the commit to pin; a sparse
checkout is enough: blueprint/roadmap/, blueprint/links/, blueprint/atlas.json,
the Lean under MathlibExt/, CSLibExt/, PhyslibExt/, WantedExt/ and Atlas/,
lean-toolchain, lake-manifest.json and LICENSE. This writes
data/atlas/source.json (the commit, its date, toolchain and Mathlib, and the
counts), structure.json (the vault's areas and subjects, and its containers in
order with their titles and prose) and articles/XX.json, the results of subject
XX: each one's title, statement and Lean declaration, and where the
repository's Lean declares it, read by trough.leansource without Lean. With
--site, the blocks link the results' cards on the ATLAS site when its pages hold
them; when it does not answer at all, the last record's value is kept if its
results are the same.

The LICENSE's own words before the Apache License's text are kept, to quote with
the credit. Nothing is written when the license is not Apache-2.0, when the
vault's atlas.json, a container's README, an entry it links or an article's
title does not read, when a link annotation does not read, or when the results
drop under half of those the last record has.
"""

from __future__ import annotations

import argparse
import http.client
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from trough import atlas

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "atlas"
# Answers that say to try again later, not that the page is missing.
RETRY = {408, 429}


def git(checkout: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(checkout), *args], check=True, capture_output=True, text=True,
                          env={**os.environ, "TZ": "UTC"}).stdout.strip()


def fetch(url: str, method: str, attempts: int = 3, wait: float = 10.0) -> bytes | None:
    """The body of a GET, None when the site answers that it has no such page (any 4xx but a timeout or a rate
    limit). A request the site does not answer, drops, or answers with a timeout, a rate limit or a server error is
    tried *attempts* times, then raises atlas.Unreachable."""
    request = urllib.request.Request(url, method=method, headers={"User-Agent": "trough (github.com/Deicyde/trough)"})
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.read()
        except urllib.error.HTTPError as error:
            if error.code < 500 and error.code not in RETRY:
                return None
        except (urllib.error.URLError, http.client.HTTPException, OSError):
            pass
        if attempt + 1 < attempts:
            time.sleep(wait)
    raise atlas.Unreachable(url)


def last_paths(out: Path) -> set[str]:
    return {article["path"] for shard in sorted((out / "articles").glob("*.json"))
            for article in json.loads(shard.read_text(encoding="utf-8"))["articles"]}


def refresh(checkout: Path, out: Path, site: bool = False, fetcher=fetch) -> list[str]:
    """Write source.json, structure.json and the article records under *out*, or nothing when there is a problem;
    return the problems."""
    rev = git(checkout, "rev-parse", "HEAD")
    license_file = checkout / "LICENSE"
    notice = atlas.license_notice(license_file.read_text(encoding="utf-8")) if license_file.is_file() else None
    if notice is None:
        return [f"{atlas.REPO} at {rev[:8]}: its LICENSE is not Apache-2.0"]
    structure, articles, counts, problems = atlas.read(checkout)
    previous = last_paths(out) if (out / "articles").is_dir() else set()
    paths = sorted(path for records in articles.values() for path in (record["path"] for record in records))
    if not problems and not paths:
        problems.append(f"{atlas.REPO} at {rev[:8]}: the vault has no articles")
    if len(paths) * 2 < len(previous):
        problems.append(f"{len(paths)} results, under half the {len(previous)} of the last record")
    if problems:
        return problems
    manifest = checkout / "lake-manifest.json"
    mathlib = next((package for package in json.loads(manifest.read_text(encoding="utf-8")).get("packages", [])
                    if package.get("name") == "mathlib"), {}) if manifest.is_file() else {}
    toolchain = checkout / "lean-toolchain"
    source = {
        "repo": atlas.REPO, "branch": atlas.BRANCH, "rev": rev,
        # In UTC, as git versions print %cI differently.
        "date": git(checkout, "log", "-1", "--date=format-local:%Y-%m-%dT%H:%M:%SZ", "--format=%cd", "HEAD"),
        "toolchain": toolchain.read_text(encoding="utf-8").strip().split(":")[-1] if toolchain.is_file() else "",
        "mathlib": mathlib.get("rev", ""), "mathlib_version": mathlib.get("inputRev", ""),
        "license": "Apache-2.0", "license_notice": notice,
        "counts": counts,
    }
    if site:
        try:
            problem = atlas.site_problem(atlas.sample(paths), fetcher)
        except atlas.Unreachable as error:
            # The last record's check holds only for the results it checked.
            last = out / "source.json"
            kept = json.loads(last.read_text(encoding="utf-8")).get("site", {}) if last.is_file() else {}
            same = kept.get("url") == atlas.SITE and previous == set(paths)
            print(f"The site does not answer at {error}; "
                  + ("keeping the last record's value." if same else "not linking its cards."), file=sys.stderr)
            source["site"] = {"url": atlas.SITE, "cards": bool(same and kept.get("cards"))}
        else:
            if problem:
                print(f"Not linking the site's cards: {problem}", file=sys.stderr)
            source["site"] = {"url": atlas.SITE, "cards": problem is None}
    structure = {"schema": atlas.SCHEMA, "repo": atlas.REPO, "rev": rev, **structure}
    (out / "articles").mkdir(parents=True, exist_ok=True)
    shards = {re.sub(r"[^A-Za-z0-9]", "", subject): records for subject, records in articles.items()}
    for stale in (out / "articles").glob("*.json"):
        if stale.stem not in shards:
            stale.unlink()
    for name, records in shards.items():
        (out / "articles" / f"{name}.json").write_text(
            json.dumps({"schema": atlas.SCHEMA, "rev": rev, "articles": records}, indent=1, ensure_ascii=False) + "\n",
            encoding="utf-8")
    for name, record in (("source.json", source), ("structure.json", structure)):
        (out / name).write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{atlas.REPO} {rev[:8]}: " + ", ".join(f"{count} {key}" for key, count in counts.items())
          + (f"; site cards linked: {source['site']['cards']}" if "site" in source else ""), file=sys.stderr)
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("checkout", type=Path, help="a checkout of Deicyde/atlas-lean")
    parser.add_argument("--site", action="store_true", help="check whether the ATLAS site holds the results' cards")
    args = parser.parse_args()
    problems = refresh(args.checkout, OUT, args.site)
    if problems:
        shown = problems[:200]
        print("\n".join(shown) + (f"\n... and {len(problems) - len(shown)} more" if len(problems) > len(shown) else "")
              + "\nnothing written", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
