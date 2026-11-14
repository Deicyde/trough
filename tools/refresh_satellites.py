#!/usr/bin/env python3
"""Record what trough maps of the satellite projects, from a sparse clone of each.

    python tools/refresh_satellites.py [--newest] [SLUG ...]

For each project in data/satellites/projects.toml (or each SLUG given), this
clones the repository at the commit its record pins, or at its newest commit
when it has no record yet, and writes data/satellites/<slug>.json. The clone is
blobless, one commit deep and sparse: the README, license files, Lake files and
blueprint TeX, then the .lean files of the Lean libraries the lakefile defines,
at most MAX_FILES of them. Git over HTTPS costs no GitHub API quota; the CI state
of a new pin is one GraphQL query through the gh CLI.

With --newest, a pin moves to the newest commit only when the project's
requirements, README opening or license text changed there, or the pinned commit
is STALE_DAYS older than the newest. A repository that does not resolve keeps
its record, counting the runs it was missing; at the second, the record goes.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from trough import satellites

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "satellites"
VAULT = ROOT / "blueprint"
METADATA = ["/README*", "/readme*", "/LICEN*", "/COPYING*", "/LICENSES/", "lakefile.lean", "lakefile.toml",
            "lake-manifest.json", "lean-toolchain", "leanpkg.toml", "README.md", "**/blueprint/src/**/*.tex"]
ENV = {**os.environ, "TZ": "UTC", "GIT_TERMINAL_PROMPT": "0"}


def git(checkout: Path, *args: str, stdin: str | None = None) -> str:
    return subprocess.run(["git", "-C", str(checkout), *args], check=True, capture_output=True, text=True,
                          input=stdin, env=ENV).stdout


def newest(repo: str) -> str | None:
    result = subprocess.run(["git", "ls-remote", f"https://github.com/{repo}.git", "HEAD"], capture_output=True,
                            text=True, env=ENV)
    head = result.stdout.split("\t", 1)[0].strip()
    return head if result.returncode == 0 and re.fullmatch(r"[0-9a-f]{40}", head) else None


def pattern(path: str) -> str:
    """A sparse-checkout pattern matching one file and nothing else."""
    return "/" + re.sub(r"([\\*?\[\]!#])", r"\\\1", path)


def fetch(repo: str, rev: str, checkout: Path) -> tuple[list[str], str]:
    """Check out the metadata files of the repository at *rev*; every path the commit has, and its date."""
    checkout.mkdir(parents=True)
    git(checkout, "init", "--quiet")
    git(checkout, "remote", "add", "origin", f"https://github.com/{repo}.git")
    git(checkout, "fetch", "--quiet", "--depth", "1", "--filter=blob:none", "origin", rev)
    git(checkout, "sparse-checkout", "set", "--no-cone", "--stdin", stdin="\n".join(METADATA) + "\n")
    git(checkout, "checkout", "--quiet", "FETCH_HEAD")
    paths = [path for path in git(checkout, "ls-tree", "-r", "--name-only", "-z", "FETCH_HEAD").split("\0") if path]
    date = git(checkout, "log", "-1", "--date=format-local:%Y-%m-%dT%H:%M:%SZ", "--format=%cd", "FETCH_HEAD").strip()
    return paths, date


def ci_state(repo: str, rev: str) -> str | None:
    """The state of the checks GitHub rolls up for the commit, as the repository reports them."""
    owner, name = repo.split("/", 1)
    query = ("query($owner: String!, $name: String!, $oid: GitObjectID!) { repository(owner: $owner, name: $name) "
             "{ object(oid: $oid) { ... on Commit { statusCheckRollup { state } } } } }")
    result = subprocess.run(["gh", "api", "graphql", "-f", f"query={query}", "-F", f"owner={owner}", "-F",
                             f"name={name}", "-F", f"oid={rev}"], capture_output=True, text=True)
    if result.returncode:
        return None
    node = ((json.loads(result.stdout).get("data") or {}).get("repository") or {}).get("object") or {}
    return (node.get("statusCheckRollup") or {}).get("state")


def days(earlier: str, later: str) -> int:
    parse = lambda text: datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))  # noqa: E731
    return (parse(later) - parse(earlier)).days


def read(project: dict, rev: str, work: Path, heads: set[str], names: set[str]) -> dict:
    checkout = work / "full"
    paths, date = fetch(project["repo"], rev, checkout)
    folder = satellites.project_dir(paths)
    if folder is not None:
        libraries = satellites.lean_libraries(checkout / folder)
        files = sorted(satellites.library_files(paths, folder, libraries))[:satellites.MAX_FILES]
        if files:
            git(checkout, "sparse-checkout", "add", "--stdin", stdin="\n".join(map(pattern, files)) + "\n")
    record = satellites.read_project(checkout, project, rev, date, paths, heads, names)
    shutil.rmtree(checkout)
    return record


def refresh(projects: list[dict], newest_too: bool, out: Path) -> list[str]:
    heads = satellites.concept_heads(VAULT / "links")
    names = satellites.chapter_names(VAULT)
    problems = []
    out.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temp:
        work = Path(temp)
        for project in projects:
            path = out / f"{project['slug']}.json"
            old = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else None
            try:
                rev = old["rev"] if old else None
                if newest_too or not old:
                    head = newest(project["repo"])
                    if head is None:
                        if old:
                            missing = old.get("missing", 0) + 1
                            if missing >= 2:
                                path.unlink()
                                problems.append(f"{project['repo']}: missing on two runs; its record is removed")
                            else:
                                path.write_text(json.dumps(old | {"missing": missing}, indent=1, ensure_ascii=False)
                                                + "\n", encoding="utf-8")
                                problems.append(f"{project['repo']}: does not resolve; its record is kept")
                        else:
                            problems.append(f"{project['repo']}: does not resolve")
                        continue
                    if not old:
                        rev = head
                    elif head != old["rev"]:
                        paths, date = fetch(project["repo"], head, work / "meta")
                        moved = satellites.metadata(work / "meta", paths)["stable"] != old.get("stable")
                        shutil.rmtree(work / "meta")
                        if moved or days(old["date"], date) >= satellites.STALE_DAYS:
                            rev = head
                record = read(project, rev, work, heads, names)
                kept = old if old and old["rev"] == rev else None
                record["ci"] = kept.get("ci") if kept else ci_state(project["repo"], rev)
            except (subprocess.CalledProcessError, OSError, ValueError) as error:
                detail = error.stderr.strip() if isinstance(error, subprocess.CalledProcessError) else str(error)
                problems.append(f"{project['repo']}: {detail}")
                continue
            path.write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"{project['slug']} {rev[:8]}: "
                  + (f"{record.get('library_files', 0)} files, {record.get('declarations', 0)} declarations, "
                     f"headlines by {record.get('headline_rule')}: {len(record.get('headlines', []))}, "
                     f"{len(record.get('uses', {}))} concepts named, license {record['license']['spdx']}"
                     if record["admitted"] else f"not admitted, {record['reason']}"), file=sys.stderr)
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--newest", action="store_true", help="move pins to the newest commits that change them")
    parser.add_argument("slugs", nargs="*", help="refresh only these projects")
    args = parser.parse_args()
    projects = satellites.load_projects(OUT / "projects.toml")
    if args.slugs:
        unknown = set(args.slugs) - {project["slug"] for project in projects}
        if unknown:
            print(f"no such project: {', '.join(sorted(unknown))}", file=sys.stderr)
            return 1
        projects = [project for project in projects if project["slug"] in args.slugs]
    for problem in refresh(projects, args.newest, OUT):
        print(f"::warning::{problem}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
