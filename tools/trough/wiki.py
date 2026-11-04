"""The wiki's authored articles, which take the place of a concept's generated text.

wiki/mathlib/<name>.md is one article. Its front matter names the concept it is
about and gives the article a durable identity:

    ---
    article_id: af_064ef7e0970e39cb57a15219
    concept: Subgroup.card_subgroup_dvd_card
    ---

A concept's key is its article's first declaration, its statement or module, or
"<list>:<item key>" for one Mathlib lacks (mathlib.concept_key); "area:<headings>"
is the overview page of a section of Mathlib's overview, such as
"area:General algebra/Group theory". The file's name is for people only.

The body is Markdown and TeX. [words](lean:Full.Name) cites a Mathlib declaration,
and becomes a link to its documentation; a name with spaces or parentheses goes in
angle brackets, [words](<lean:Foo.«bar baz»>). CI reads every cited name in
Mathlib's environment (lean/ConceptDeps.lean), and the chapter stops on one with no
record or one Mathlib deprecates. [words](trough:key) links another concept's
article, and becomes a relative link once pages have paths. A lean: or trough:
link in any other shape (a title, a capital scheme, spaces) is refused rather than
left unlinked. "## Depends on" and "## Proof depends on" list the concepts a reader
needs, as "- [Title](trough:key)" lines; they take the place of the edges Mathlib's
declaration graph gives.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote

LEAN_LINK = re.compile(r"\]\((?:<lean:([^>]+)>|lean:([^)\s]+))\)")
TROUGH_LINK = re.compile(r"\]\(trough:([^)\s]+)\)")
SCHEME = re.compile(r"\]\(\s*<?\s*(?:lean|trough):", re.I)
DEPENDENCY = re.compile(r"^- \[[^\]]*\]\(trough:([^)\s]+)\)")
SECTIONS = {"## Depends on": "depends", "## Proof depends on": "proof_depends"}


@dataclass
class Authored:
    path: Path
    article_id: str
    concept: str
    body: str  # without the dependency sections
    depends: list[str] = field(default_factory=list)  # concept keys
    proof_depends: list[str] = field(default_factory=list)


def joined(text: str) -> str:
    """text with the words of every lean: and trough: link on one line. AutoformBot reads a link
    line by line, so a link whose words wrap would lose its target."""
    out, last = [], 0
    for match in re.finditer(r"\]\((?:<lean:|lean:|trough:)", text):
        depth, start = 0, match.start()
        while start > 0:
            start -= 1
            if text[start - 1 : start] == "\\":
                continue
            if text[start] == "]":
                depth += 1
            elif text[start] == "[":
                if depth == 0:
                    break
                depth -= 1
        if start < last:
            continue
        out.append(text[last:start])
        out.append(re.sub(r"\s*\n\s*", " ", text[start : match.start()]))
        last = match.start()
    out.append(text[last:])
    return "".join(out)


def parse(path: Path) -> Authored:
    text = path.read_text(encoding="utf-8")
    definition = re.search(r"(?m)^\s{0,3}\[[^\]]+\]:\s*<?(?:lean|trough):", text)
    if definition:
        raise ValueError(f"{path}: {definition.group().strip()!r} is a reference-style definition; write the link inline")
    for link in SCHEME.finditer(text):
        if not (LEAN_LINK.match(text, link.start()) or TROUGH_LINK.match(text, link.start())):
            line = text.count("\n", 0, link.start()) + 1
            shown = text[link.start():].split("\n", 1)[0][:60]
            raise ValueError(f"{path}:{line}: {shown!r} is not (lean:Name), (<lean:Name>) or (trough:key); "
                             "write the link without a title or spaces")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    fields = dict(line.split(":", 1) for line in match.group(1).splitlines() if ":" in line) if match else {}
    fields = {key.strip(): value.strip() for key, value in fields.items()}
    if not fields.get("article_id") or not fields.get("concept"):
        raise ValueError(f"{path}: front matter needs article_id and concept")
    article = Authored(path, fields["article_id"], fields["concept"], "")
    body: list[str] = []
    section = None
    for line in text[match.end():].splitlines():
        if line.startswith("## "):
            section = SECTIONS.get(line.strip())
            if section:
                continue
        if section is None:
            body.append(line)
        elif line.strip():
            dependency = DEPENDENCY.match(line.strip())
            if not dependency:
                raise ValueError(f"{path}: under ## Depends on or ## Proof depends on, {line.strip()!r} is not "
                                 "a '- [Title](trough:key)' line")
            getattr(article, section).append(unquote(dependency.group(1)))
    article.body = joined("\n".join(body).strip())
    return article


def load(directory: Path) -> dict[str, Authored]:
    """The articles under directory, by the concept each is about."""
    articles: dict[str, Authored] = {}
    for path in sorted(directory.glob("*.md")) if directory.is_dir() else []:
        article = parse(path)
        if article.concept in articles:
            raise ValueError(f"{path} and {articles[article.concept].path} are both about {article.concept}")
        articles[article.concept] = article
    ids = [article.article_id for article in articles.values()]
    if len(ids) != len(set(ids)):
        raise ValueError(f"two articles under {directory} share an article_id")
    return articles


def cited(articles: dict[str, Authored]) -> list[str]:
    """Every declaration the articles cite."""
    return sorted({unquote(match.group(1) or match.group(2)) for article in articles.values()
                   for match in LEAN_LINK.finditer(article.body)})


def linked(article: Authored) -> list[str]:
    """The keys of the concepts the article's text links."""
    return [unquote(match.group(1)) for match in TROUGH_LINK.finditer(article.body)]


def link_citations(text: str, url: dict[str, str]) -> str:
    """text with each lean: link pointing at the documentation url gives for its name."""

    def link(match: re.Match) -> str:
        name = unquote(match.group(1) or match.group(2))
        return f"]({url[name]})"

    return LEAN_LINK.sub(link, text)
