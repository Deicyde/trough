#!/usr/bin/env python3
"""Record what trough maps of Axiom's Lean formalization of the Stacks Project, from checkouts.

    python tools/refresh_stacks.py CHECKOUT PROJECT [--site URL]

CHECKOUT is a git checkout of AxiomMath/Stacks at the commit to pin; a sparse
checkout is enough: StacksCore/, StacksFrontier/, formalization.yaml,
README.md, lean-toolchain, lake-manifest.json and LICENSE. PROJECT is a
checkout of the Stacks Project (stacks/stacks-project) with its top-level .tex
files and tags/tags. This writes data/stacks/source.json (the commit, its date,
toolchain and Mathlib, the formalization.yaml's facts, the README's words on the
tiers, and the counts), structure.json (the Stacks Project's parts, chapters and
sections, and the place of each tag the repository uses) and tags/XX.json, the
tags starting XX: each tag's declarations as trough.leansource reads them
without Lean (name, kind, file, line, tier, the attribute's comment, docstring,
statement, whether the value holds `sorry`, and EGA and SGA references), and
the declarations registered for it. With --site, the blocks link the site's tag
pages when the site serves them; when it does not answer at all, the last
record's value is kept if the URL and the tags are the same.

Nothing is written when the repository is not Apache-2.0, when a file the
commit lists is not checked out, when a `@[stacks]`, `@[ega]` or `@[sga]`
attribute, a registration or an `attribute` command does not read (a file whose
scopes don't close counts as one), when the Stacks Project's checkout gives no
parts or tags, or when the tags drop under half of those the last record has.
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

import yaml

from trough import ff, formalization, stacks

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "stacks"
TIER_ITEM = re.compile(r"^\*\s*\[(StacksCore|StacksFrontier)\]\([^)]*\):\s*(.+)$")
# Answers that say to try again later, not that the page is missing.
RETRY = {408, 429}


def git(checkout: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(checkout), *args], check=True, capture_output=True, text=True,
                          env={**os.environ, "TZ": "UTC"}).stdout.strip()


def fetch(url: str, method: str, attempts: int = 3, wait: float = 10.0) -> bytes | None:
    """The body of a GET, None when the site answers that it has no such page (any 4xx but a timeout or a rate
    limit). A request the site does not answer, drops, or answers with a timeout, a rate limit or a server error is
    tried *attempts* times, then raises stacks.Unreachable."""
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
    raise stacks.Unreachable(url)


def readme_words(text: str) -> dict:
    """The README's words on the tiers: the paragraph that opens its Structure section, and each tier's first
    sentence."""
    section = ff.section(text, "Structure")
    paragraphs = [" ".join(block.split()) for block in "\n".join(section).split("\n\n") if block.strip()]
    tiers = {}
    for line in section:
        if match := TIER_ITEM.match(line.strip()):
            tiers[match.group(1)] = re.split(r"(?<=\.)\s+", match.group(2).strip(), maxsplit=1)[0]
    lead = next((paragraph for paragraph in paragraphs if not paragraph.startswith("*")), "")
    return {"structure": lead, "tiers": tiers}


def last_tags(out: Path) -> set[str]:
    return {record["tag"] for shard in sorted((out / "tags").glob("*.json"))
            for record in json.loads(shard.read_text(encoding="utf-8"))["tags"]}


def refresh(checkout: Path, project: Path, out: Path, site: str | None = None, fetcher=fetch) -> list[str]:
    """Write source.json, structure.json and the tag records under *out*, or nothing when there is a problem;
    return the problems."""
    rev = git(checkout, "rev-parse", "HEAD")
    paths = sorted((path for path in git(checkout, "ls-tree", "-r", "--name-only", "HEAD", "--", *stacks.TIERS)
                    .splitlines() if path.endswith(".lean")), key=stacks.natural)
    problems = []
    license_file = checkout / "LICENSE"
    try:
        config = formalization.load((checkout / "formalization.yaml").read_text(encoding="utf-8"))
    except (OSError, ValueError, yaml.YAMLError) as error:
        return [f"{stacks.REPO} at {rev[:8]}: its formalization.yaml does not read: {error}"]
    license_name = formalization.text_of(config.project.get("license"))
    if license_name != "Apache-2.0" or not license_file.is_file() or not ff.is_apache(license_file.read_text(encoding="utf-8")):
        problems.append(f"{stacks.REPO} at {rev[:8]}: not Apache-2.0 (formalization.yaml says {license_name!r})")
    missing = [path for path in paths if not (checkout / path).is_file()]
    if missing:
        problems.append(f"not checked out: {missing[0]}"
                        + (f" and {len(missing) - 1:,} other files" if len(missing) > 1 else ""))
    if not paths:
        problems.append(f"{stacks.REPO} at {rev[:8]} has no .lean files under {' or '.join(stacks.TIERS)}")
    if problems:
        return problems
    tags, counts, unread = stacks.read(checkout, paths)
    problems += unread
    structure, project_problems = stacks.read_project(project, {record["tag"] for record in tags})
    problems += project_problems
    previous = last_tags(out) if (out / "tags").is_dir() else set()
    if len(tags) * 2 < len(previous):
        problems.append(f"{len(tags)} tags, under half the {len(previous)} of the last record")
    if problems:
        return problems
    text = formalization.text_of
    manifest = checkout / "lake-manifest.json"
    mathlib = next((package for package in json.loads(manifest.read_text(encoding="utf-8")).get("packages", [])
                    if package.get("name") == "mathlib"), {}) if manifest.is_file() else {}
    toolchain = checkout / "lean-toolchain"
    readme = checkout / "README.md"
    source = {
        "repo": stacks.REPO, "rev": rev,
        # In UTC, as git versions print %cI differently.
        "date": git(checkout, "log", "-1", "--date=format-local:%Y-%m-%dT%H:%M:%SZ", "--format=%cd", "HEAD"),
        "toolchain": toolchain.read_text(encoding="utf-8").strip().split(":")[-1] if toolchain.is_file() else "",
        "mathlib": mathlib.get("rev", ""), "mathlib_version": mathlib.get("inputRev", ""),
        "license": license_name,
        "project": {"name": text(config.project.get("name")), "description": text(config.project.get("description")),
                    "authors": [text(author) for author in config.project.get("authors") or []],
                    "maintainers": [text(name) for name in config.project.get("responsible_maintainers") or []]},
        "review": {"status": text(config.review.get("status")), "notes": text(config.review.get("notes")),
                   "reviewers": [text(reviewer) for reviewer in config.review.get("reviewers") or []]},
        "automation": {
            "methods": [{key: text(method.get(key)) for key in ff.AUTOMATION if method.get(key)}
                        | ({"models": [text(model) for model in method["models"]]} if method.get("models") else {})
                        for method in config.automation.get("methods") or [] if isinstance(method, dict)],
            "notes": text(config.automation.get("notes")),
        },
        "sources": [{"title": text(item.get("title")), "location": text(item.get("location")),
                     "note": text(item.get("note"))} for item in config.sources],
        "readme": readme_words(readme.read_text(encoding="utf-8")) if readme.is_file() else {},
        "counts": counts,
    }
    if site:
        names = [record["tag"] for record in tags]
        try:
            problem = stacks.site_problem(site, stacks.sample(names), fetcher)
        except stacks.Unreachable as error:
            # The last record's check holds only for the tags it checked.
            last = out / "source.json"
            kept = json.loads(last.read_text(encoding="utf-8")).get("site", {}) if last.is_file() else {}
            same = kept.get("url") == site and previous == set(names)
            print(f"The site does not answer at {error}; "
                  + ("keeping the last record's value." if same else "not linking its tag pages."), file=sys.stderr)
            source["site"] = {"url": site, "tags": bool(same and kept.get("tags"))}
        else:
            if problem:
                print(f"Not linking the site's tag pages: {problem}", file=sys.stderr)
            source["site"] = {"url": site, "tags": problem is None}
    project_rev = git(project, "rev-parse", "HEAD")
    structure = {"schema": stacks.SCHEMA, "repo": stacks.PROJECT, "rev": project_rev,
                 "date": git(project, "log", "-1", "--date=format-local:%Y-%m-%dT%H:%M:%SZ", "--format=%cd", "HEAD"),
                 **structure}
    shards: dict[str, list[dict]] = {}
    for record in tags:
        shards.setdefault(record["tag"][:2], []).append(record)
    (out / "tags").mkdir(parents=True, exist_ok=True)
    for stale in (out / "tags").glob("*.json"):
        if stale.stem not in shards:
            stale.unlink()
    for prefix, records in shards.items():
        (out / "tags" / f"{prefix}.json").write_text(
            json.dumps({"schema": stacks.SCHEMA, "rev": rev, "tags": records}, indent=1, ensure_ascii=False) + "\n",
            encoding="utf-8")
    for name, record in (("source.json", source), ("structure.json", structure)):
        (out / name).write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    placed = sum(1 for record in tags if record["tag"] in structure["tags"])
    print(f"{stacks.REPO} {rev[:8]}: {len(tags)} tags ({placed} placed in the Stacks Project at {project_rev[:8]}); "
          + ", ".join(f"{count} {key}" for key, count in counts.items())
          + (f"; site tag pages linked: {source['site']['tags']}" if "site" in source else ""), file=sys.stderr)
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("checkout", type=Path, help="a checkout of AxiomMath/Stacks")
    parser.add_argument("project", type=Path, help="a checkout of stacks/stacks-project")
    parser.add_argument("--site", help="the repository's site, ending in /, whose tag pages to link when it serves them")
    args = parser.parse_args()
    problems = refresh(args.checkout, args.project, OUT, args.site)
    if problems:
        shown = problems[:200]
        print("\n".join(shown) + (f"\n... and {len(problems) - len(shown)} more" if len(problems) > len(shown) else "")
              + "\nnothing written", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
