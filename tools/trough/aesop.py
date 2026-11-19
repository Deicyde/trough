"""The Aesop chapter: leanprover-community/aesop, Lean's proof search tactic, an article per module.

Aesop (Automated Extensible Search for Obvious Proofs) is a proof search tactic for Lean 4, written in Lean, in
folders under Aesop/ (Search, Tree, RuleTac, Forward, Script, Builder, Frontend and smaller ones). Mathlib requires
it. tools/refresh_library.py reads a checkout at a pinned commit into data/aesop/ without Lean, as trough.library
reads any library, with the README's opening sentences; lean/library/LibraryDeps.lean then reads, with Lean, the
modules each module's statements and proofs use and which of the names read from the source are public. A module
that declares nothing public by name is listed on its folder's page. trough.library builds the chapter; this module
holds what is Aesop's own: its README's description and the opening of the chapter's intro.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from . import library
from .blueprints import Built
from .formal_conjectures import quote
from .library import GITHUB, Library, pinned

SCHEMA = "trough-aesop/v1"
REPO = "leanprover-community/aesop"
ROOT = "Aesop"
TITLE = "Aesop: proof search for Lean"


def readme_description(readme: str) -> list[str]:
    """The README's first paragraph under its `# Aesop` title, without a last sentence that introduces the list
    after it: what Aesop is."""
    body = re.split(r"^# Aesop[ \t]*\n", readme, maxsplit=1, flags=re.M)[-1]
    paragraph = " ".join(re.split(r"\n\s*\n", body.strip(), maxsplit=1)[0].split())
    sentences = re.split(r"(?<=[.!?])\s+", paragraph)
    while len(sentences) > 1 and sentences[-1].rstrip().endswith(":"):
        sentences.pop()
    return [" ".join(sentences)] if paragraph else []


def extras(checkout: Path) -> dict:
    """What Aesop's record keeps besides its modules: its README's description."""
    return {"readme": readme_description((checkout / "README.md").read_text(encoding="utf-8"))}


def intro(data: dict, stats: Counter) -> str:
    return library.module_intro(AESOP, data, stats, [
        f"[{REPO}]({GITHUB}/{REPO}) says in its README:",
        quote(pinned(AESOP, "\n\n".join(data["readme"]), data["rev"])),
        "Mathlib requires it.",
    ])


AESOP = Library(id="aesop", name="Aesop", title=TITLE, repo=REPO, root=ROOT, schema=SCHEMA, intro=intro,
                required=("README.md", "lean-toolchain", "lake-manifest.json"), extras=extras, list_empty=True)

LIBRARY = AESOP  # as generate.py and refresh_library.py find it


def load(data: Path) -> dict | None:
    return library.load(AESOP, data)


def chapter(data: dict) -> tuple[Built, dict[str, str]]:
    return library.chapter(AESOP, data)
