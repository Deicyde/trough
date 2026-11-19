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
from .library import GITHUB, Library, at, credit, listing, pinned, plural

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
    rev = data["rev"]
    theorems = stats["theorem"] + stats["lemma"]
    definitions = sum(stats[kind] for kind in ("def", "abbrev", "structure", "class", "inductive", "opaque"))
    others = stats["declarations"] - theorems - definitions
    if data.get("deps"):
        lean = (
            "Edges come from Lean: a GitHub Actions run builds Batteries at this commit and reads, for each module, "
            "which other modules' declarations its own use. “Depends on” lists the modules its statements use, the "
            "types of its declarations and the values of its definitions, and “Proof depends on” those only its proofs "
            f"use; a dependency reached through another is left out. That gives "
            f"{plural(stats['statement_edges'], 'statement edge')} and {plural(stats['proof_edges'], 'proof edge')}."
            + (f" The run has no record of {plural(stats['unrecorded'], 'module')}, whose dependencies are unknown."
               if stats["unrecorded"] else "")
            + " The same run checks the names read from the source"
            + (f": Lean marks {stats['private']:,} of them as private to their modules (in a `module` file, a "
               "declaration outside a `public section` and not marked `public` is private), and these are left out"
               + (f", as {'is' if stats['unresolved'] == 1 else 'are'} {plural(stats['unresolved'], 'name')} Lean does "
                  "not have" if stats["unresolved"] else "")
               + "." if stats["private"] or stats["unresolved"] else ", and Lean has each as a public declaration."))
    else:
        lean = ("The articles have no edges, and the names read from the source are not checked against Lean: both come "
                "from a Lean run over Batteries at this commit, which the data lack.")
    return "\n\n".join(part for part in [
        f"[{REPO}]({GITHUB}/{REPO}) says in its README:",
        quote(pinned(BATTERIES, "\n\n".join(data["readme"]), rev)),
        "Mathlib requires it, so every project built on Mathlib builds on it too.",
        f"This chapter maps Batteries at commit {at(BATTERIES, rev)} ({data['date'][:10]}), with Lean toolchain "
        f"{data['toolchain']}. It has an article for each of the {plural(stats['articles'], 'module')} under `{ROOT}/` "
        f"that declare something public by name, in a part per folder of `{ROOT}/` and a page per folder below. They "
        f"hold {plural(stats['declarations'], 'public declaration')}, "
        + listing([plural(count, word, words) for count, word, words in (
            (theorems, "theorem", None), (definitions, "definition", None),
            (others, "instance or alias", "instances and aliases")) if count])
        + f", {stats['documented']:,} of them with a docstring."
        + (f" The other {plural(stats['empty'], 'module')} declare nothing public by name, such as a module that only "
           "imports others, a deprecated module whose code has moved, or one that adds syntax or an elaborator; they "
           "are listed on their folders' pages." if stats["empty"] else ""),
        "An article is titled by its module docstring, or by its file name when the docstring has no title; where "
        "modules share a title, each adds the shortest end of its path that tells them apart. It gives the module's "
        "authors as its header names them, its docstrings, and a block per public declaration in file order with its "
        "Lean statement: the text up to the `:=` or `where` that starts its value, or the whole text of a structure, "
        "class or inductive type. These are read from the source text, without Lean. Unnamed instances and the names "
        "an `alias ⟨…⟩` command gives are left out, and so are TODO notes and text about plans or inviting future "
        "work; an ellipsis marks each cut."
        + ("" if stats["sorry"] else " No declaration's value holds `sorry`."),
        lean,
        credit(BATTERIES, rev),
    ] if part)


BATTERIES = Library(id="batteries", name="Batteries", title=TITLE, repo=REPO, root=ROOT, schema=SCHEMA, intro=intro,
                    required=("README.md", "lean-toolchain", "lake-manifest.json"), extras=extras, list_empty=True)


def read(checkout: Path, paths: list[str]) -> tuple[dict, list[str]]:
    return library.read(BATTERIES, checkout, paths)


def load(data: Path) -> dict | None:
    return library.load(BATTERIES, data)


def chapter(data: dict) -> tuple[Built, dict[str, str]]:
    return library.chapter(BATTERIES, data)
