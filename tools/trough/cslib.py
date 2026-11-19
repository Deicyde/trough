"""The CSLib chapter: the Lean Computer Science Library, a module per article.

leanprover/cslib organizes its Lean in folders under Cslib/, one area each (Foundations, Computability,
Languages, Logics, Algorithms, Crypto and smaller ones), and documents each module the way Mathlib does: a module
docstring with a `#` title, its main definitions and statements, and a docstring on each definition.
tools/refresh_cslib.py reads a checkout at a pinned commit into data/cslib/ without Lean: each module's title,
docstrings, the authors its header names and its public declarations, as trough.leansource reads them, with the
area READMEs' descriptions. lean/library/LibraryDeps.lean then reads, with Lean, the modules each module's statements
and proofs use, and which of those names Lean has only as private declarations: in a `module` file, a declaration
outside a `public section` and not marked `public` is private, which the source reading does not follow. The chapter
has a part per area, a page per folder and an article per module, with a block per public declaration in file order.
trough.library builds it; this module says what is CSLib's own: its README's description, the maintainers
GOVERNANCE.md names, and the chapter's intro.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from . import library
from .blueprints import Built
from .formal_conjectures import quote
# counts, header, readme_text and titles are CSLib's too, as refresh_cslib and the tests use them.
from .library import GITHUB, Library, at, counts, credit, header, listing, pinned, plural, readme_text, titles

SCHEMA = "trough-cslib/v1"
REPO = "leanprover/cslib"
LIBRARY = "Cslib"
TITLE = "CSLib: the Lean Computer Science Library"


def maintainers(governance: str) -> list[dict]:
    """The maintainers GOVERNANCE.md names, by role: the lead maintainer, technical leads and area maintainers,
    each a name as written, without the affiliation and handle after it."""
    roles = []
    for match in re.finditer(r"^### (.+?)\s*\n(.*?)(?=^#{2,3} |\Z)", governance, re.M | re.S):
        names = [re.split(r"\s*\(@|,|\.\s", item, maxsplit=1)[0].strip().rstrip(".")
                 for item in re.findall(r"^- (.+)$", match.group(2), re.M)]
        if names:
            roles.append({"role": match.group(1).strip(), "names": names})
    return roles


def readme_description(readme: str) -> list[str]:
    """The README's paragraphs before its first `#` section after the title, and those of its "What's CSLib?"
    section, without its aims, which say what the library means to offer; a paragraph "…" stands for the heading
    between them."""
    sections = re.split(r"^# ", readme, flags=re.M)
    kept = []
    for index, section in enumerate(sections[1:]):
        title, _, body = section.partition("\n")
        if index == 0 or title.strip().lower().startswith("what"):
            body = re.split(r"^##? ", body, maxsplit=1, flags=re.M)[0]
            kept += (["…"] if index else []) + [part.strip() for part in re.split(r"\n\s*\n", body) if part.strip()]
    return kept


def extras(checkout: Path) -> dict:
    """What CSLib's record keeps besides its modules: its README's description and the maintainers GOVERNANCE.md
    names."""
    return {"readme": readme_description((checkout / "README.md").read_text(encoding="utf-8")),
            "maintainers": maintainers((checkout / "GOVERNANCE.md").read_text(encoding="utf-8"))}


def intro(data: dict, stats: Counter) -> str:
    rev = data["rev"]
    roles = [f"{listing(role['names'])} as {role['role'][0].lower() + role['role'][1:]}" for role in data["maintainers"]]
    theorems = stats["theorem"] + stats["lemma"]
    definitions = sum(stats[kind] for kind in ("def", "abbrev", "structure", "class", "inductive", "opaque"))
    others = stats["declarations"] - theorems - definitions
    if data.get("deps"):
        lean = (
            "Edges come from Lean: a GitHub Actions run builds CSLib at this commit and reads, for each module, which "
            "other modules' declarations its own use. “Depends on” lists the modules its statements use, the types of "
            "its declarations and the values of its definitions, and “Proof depends on” those only its proofs use; a "
            f"dependency reached through another is left out. That gives "
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
                "from a Lean run over CSLib at this commit, which the data lack.")
    return "\n\n".join(part for part in [
        f"[{REPO}]({GITHUB}/{REPO}), the Lean Computer Science Library, says in its README:",
        quote(pinned(CSLIB, "\n\n".join(data["readme"]), rev)),
        f"Its GOVERNANCE.md names {listing(roles)}." if roles else "",
        f"This chapter maps CSLib at commit {at(CSLIB, rev)} ({data['date'][:10]}), with Lean toolchain {data['toolchain']} and "
        f"Mathlib {data['mathlib'][:8]}. It has an article for each of the {plural(stats['articles'], 'module')} under "
        f"`{LIBRARY}/`, in a part per folder of `{LIBRARY}/` and a page per folder below. They hold "
        f"{plural(stats['declarations'], 'public declaration')}, "
        + listing([plural(count, word, words) for count, word, words in (
            (theorems, "theorem", None), (definitions, "definition", None),
            (others, "instance or alias", "instances and aliases")) if count])
        + f", {stats['documented']:,} of them with a docstring"
        + (f"; {plural(stats['empty'], 'module declares', 'modules declare')} nothing public by name."
           if stats["empty"] else "."),
        "An article is titled by its module docstring, or by its file name when the docstring has no title; where "
        "modules share a title, each adds the shortest end of its path that tells them apart. It gives the module's "
        "authors as its header names them, its docstrings, and a block per public declaration in file order with its "
        "Lean statement: the text up to the `:=` or `where` that starts its value, or the whole text of a structure, "
        "class or inductive type. These are read from the source text, without Lean. Unnamed instances and the names "
        "an `alias ⟨…⟩` command gives are left out, and so are TODO notes and text about plans or inviting future "
        "work; an ellipsis marks each cut."
        + ("" if stats["sorry"] else " No declaration's value holds `sorry`."),
        lean,
        credit(CSLIB, rev),
    ] if part)


CSLIB = Library(id="cslib", name="CSLib", title=TITLE, repo=REPO, root=LIBRARY, schema=SCHEMA, intro=intro,
                required=("README.md", "GOVERNANCE.md", "lean-toolchain", "lake-manifest.json"), extras=extras)


def read_module(text: str, path: str) -> dict:
    return library.read_module(text, path, CSLIB)


def read(checkout: Path, paths: list[str]) -> tuple[dict, list[str]]:
    return library.read(CSLIB, checkout, paths)


def load(data: Path) -> dict | None:
    return library.load(CSLIB, data)


def chapter(data: dict) -> tuple[Built, dict[str, str]]:
    return library.chapter(CSLIB, data)
