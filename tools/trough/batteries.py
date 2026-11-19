"""The Batteries chapter: leanprover-community/batteries, the extended library for Lean, an article per module.

Batteries collects data structures, tactics and other tools for Lean programs and proofs, in folders under
Batteries/ (Data, Lean, Tactic, Util and smaller ones). Mathlib requires it, so every project on Mathlib builds on it
too. tools/refresh_library.py reads a checkout at a pinned commit into data/batteries/ without Lean, as
trough.library reads any library: each module's title, docstrings, the authors its header names and its declarations,
with the README's description. lean/library/LibraryDeps.lean then reads, with Lean, the modules each module's
statements and proofs use, and which of the names read from the source are public. A module that declares nothing
public by name, such as one that only imports others, a deprecated module or one that only adds syntax, is listed on
its folder's page rather than given an article. trough.library builds the chapter; this module holds what is Batteries' own: its README's
description and the chapter's intro.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from . import library
from .blueprints import Built
from .formal_conjectures import quote
from .library import GITHUB, Library, pinned, plural

SCHEMA = "trough-batteries/v1"
REPO = "leanprover-community/batteries"
ROOT = "Batteries"
TITLE = "Batteries: the extended library for Lean"


def readme_description(readme: str) -> list[str]:
    """The README's paragraphs under its `# Batteries` title, before its next section: what the library is."""
    sections = re.split(r"^# ", readme, flags=re.M)
    body = next((section.partition("\n")[2] for section in sections[1:] if section.startswith("Batteries")), "")
    return [part.strip() for part in re.split(r"\n\s*\n", body) if part.strip()]


def extras(checkout: Path) -> dict:
    """What Batteries' record keeps besides its modules: its README's description."""
    return {"readme": readme_description((checkout / "README.md").read_text(encoding="utf-8"))}


def intro(data: dict, stats: Counter) -> str:
    return library.module_intro(BATTERIES, data, stats, [
        f"[{REPO}]({GITHUB}/{REPO}) says in its README:",
        quote(pinned(BATTERIES, "\n\n".join(data["readme"]), data["rev"])),
        "Mathlib requires it, so every project built on Mathlib builds on it too.",
    ], empty=(f" The other {plural(stats['empty'], 'module')} declare nothing public by name, such as a module that "
              "only imports others, a deprecated module whose code has moved, or one that adds syntax or an elaborator; "
              "they are listed on their folders' pages."))


BATTERIES = Library(id="batteries", name="Batteries", title=TITLE, repo=REPO, root=ROOT, schema=SCHEMA, intro=intro,
                    required=("README.md", "lean-toolchain", "lake-manifest.json"), extras=extras, list_empty=True)

LIBRARY = BATTERIES  # as generate.py and refresh_library.py find it


def read(checkout: Path, paths: list[str]) -> tuple[dict, list[str]]:
    return library.read(BATTERIES, checkout, paths)


def load(data: Path) -> dict | None:
    return library.load(BATTERIES, data)


def chapter(data: dict) -> tuple[Built, dict[str, str]]:
    return library.chapter(BATTERIES, data)
