"""The wiki's authored articles, which take the place of a concept's generated text.

An article is two files side by side, such as wiki/mathlib/lagranges-theorem.md and
wiki/mathlib/lagranges-theorem.jsonl. The .md file is its text, Markdown and TeX with no front
matter. The .jsonl file is its links to Mathlib, as literature-links annotations, one per line.
The folder's _defaults.json makes each object end Mathlib, so an annotation names only the
declaration. Subject ends name the article's .md file and are `generic`, as Markdown is. The
names are for people, but each annotation names its .md file, so a rename changes both files.

The first annotation is about the whole article. Its `id` is the article's durable identity, and
its object is the concept it is about: the concept's first declaration, its statement or its module
(mathlib.concept_key).

    {"id": "af_064ef7e0970e39cb57a15219", "subject": [{"type": "generic", "uri": "lagranges-theorem.md"}],
     "object": [{"location": {"declaration": "Subgroup.card_subgroup_dvd_card"}}]}

A concept that is neither, "area:<headings>" for a section of Mathlib's overview such as
"area:General algebra/Group theory" or "<list>:<key>" for one Mathlib lacks, has "object": [] and
its key in extensions["org.trough"]["concept"].

Each other annotation is a citation. Its subject quotes the cited words, and its object is the
declaration they cite:

    {"subject": [{"type": "generic", "uri": "lagranges-theorem.md",
                  "location": {"quote": {"exact": "the order of a subgroup divides the order of the group"}}}],
     "object": [{"location": {"declaration": "Subgroup.card_subgroup_dvd_card"}}]}

A quote matches the Markdown as written, each run of white space read as one space. Words that
begin or end with a letter or digit match only where that is the edge of a word, so "group" does
not match inside "subgroup". A quote stays within one paragraph, heading or list item.
`prefix` and `suffix`, the text just before and after the words, are given only when the words
occur more than once. The words become a link to the declaration's
documentation. Loading stops when a quote matches nowhere or more than once, or overlaps another
quote or a link. CI reads every cited name in Mathlib's environment (lean/ConceptDeps.lean), and
the chapter stops on one with no record or one Mathlib deprecates.

In the Markdown, [words](trough:key) links another concept's article and becomes a relative link
once pages have paths. A lean: link, which a citation replaces, or a trough: link in any other shape
(a title, a capital scheme, spaces) is refused rather than left unlinked. "## Depends on" and
"## Proof depends on" list the concepts a reader needs, as "- [Title](trough:key)" lines; they take
the place of the edges Mathlib's declaration graph gives.

An article written in one file, with front matter (article_id, concept) and [words](lean:Name)
citations, as the article pipeline drafts them, becomes the two files with `split`; `combined` gives
that one-file form back, which is what the rest of the generator reads.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote, unquote

MATHLIB = "https://github.com/leanprover-community/mathlib4"
DEFAULTS = {"object": {"type": "lean", "uri": MATHLIB}}
NAMESPACE = "org.trough"

LEAN_LINK = re.compile(r"\]\((?:<lean:([^>]+)>|lean:([^)\s]+))\)")
TROUGH_LINK = re.compile(r"\]\(trough:([^)\s]+)\)")
SCHEME = re.compile(r"\]\(\s*<?\s*(?:lean|trough):", re.I)
LEAN_SCHEME = re.compile(r"\]\(\s*<?\s*lean:", re.I)
# A line that starts a heading, a list item or a block quote.
BLOCK_START = re.compile(r"\n[ \t]*(?:#{1,6}[ \t]|[-*+][ \t]|\d+[.)][ \t]|>)")
HEADING = re.compile(r"[ \t]{0,3}#{1,6}[ \t]")
WHITE = re.compile(r"\s+")
BLANK_LINE = re.compile(r"\n[ \t]*\n")
DEPENDENCY = re.compile(r"^- \[[^\]]*\]\(trough:([^)\s]+)\)$")
SECTIONS = {"## Depends on": "depends", "## Proof depends on": "proof_depends"}


@dataclass
class Authored:
    path: Path
    article_id: str
    concept: str
    body: str  # without the dependency sections
    depends: list[str] = field(default_factory=list)  # concept keys
    proof_depends: list[str] = field(default_factory=list)


def opening(text: str, end: int) -> int:
    """Where the [ is that opens the link words closed by the ] at text[end], or -1. Link words
    stay within a paragraph, and brackets in TeX or after a backslash don't count, since a
    half-open interval such as $(0, 1]$ leaves them unbalanced."""
    i = max((blank.end() for blank in BLANK_LINE.finditer(text, 0, end)), default=0)
    stack, math = [], None
    while i < end:
        if text[i] == "\\":
            i += 2
            continue
        if text[i] == "$":
            delimiter = "$$" if text.startswith("$$", i) else "$"
            math = delimiter if math is None else None if math == delimiter else math
            i += len(delimiter)
            continue
        if math is None and text[i] == "[":
            stack.append(i)
        elif math is None and text[i] == "]" and stack:
            stack.pop()
        i += 1
    return stack[-1] if stack else -1


def joined(text: str) -> str:
    """text with the words of every lean: and trough: link on one line. AutoformBot reads a link
    line by line, so a link whose words wrap would lose its target."""
    out, last = [], 0
    for match in re.finditer(r"\]\((?:<lean:|lean:|trough:)", text):
        start = opening(text, match.start())
        if start < last:
            continue
        out.append(text[last:start])
        out.append(re.sub(r"\s*\n\s*", " ", text[start : match.start()]))
        last = match.start()
    out.append(text[last:])
    return "".join(out)


def unlink(text: str, pattern: re.Pattern, drop) -> str:
    """text with each link whose destination pattern matches and drop(match) accepts replaced
    by its words."""
    out, last = [], 0
    for match in pattern.finditer(text):
        if not drop(match):
            continue
        start = opening(text, match.start())
        if start < last:
            continue
        out += [text[last:start], text[start + 1 : match.start()]]
        last = match.end()
    out.append(text[last:])
    return "".join(out)


def lean_target(name: str) -> str:
    """The destination that cites name: in angle brackets when it holds a space or parenthesis."""
    return f"<lean:{name}>" if re.search(r"[\s()<>]", name) else f"lean:{name}"


def parse(path: Path) -> Authored:
    """The article whose text is at path, a .md file beside its .jsonl."""
    return parse_text(path, combined(path))


def check_links(where: str, text: str) -> None:
    """Refuse a lean: or trough: link the generator would not read."""
    definition = re.search(r"(?mi)^\s{0,3}\[[^\]]+\]:\s*<?\s*(?:lean|trough):", text)
    if definition:
        raise ValueError(f"{where}: {definition.group().strip()!r} is a reference-style definition; write the link inline")
    for link in SCHEME.finditer(text):
        if not (LEAN_LINK.match(text, link.start()) or TROUGH_LINK.match(text, link.start())):
            line = text.count("\n", 0, link.start()) + 1
            shown = text[link.start():].split("\n", 1)[0][:60]
            raise ValueError(f"{where}:{line}: {shown!r} is not (lean:Name), (<lean:Name>) or (trough:key); "
                             "write the link without a title or spaces")


def parse_text(path: Path, text: str) -> Authored:
    """An article from its one-file form."""
    check_links(str(path), text)
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
    if directory.is_dir():
        texts = {path.stem for path in directory.glob("*.md")}
        stray = sorted(path.name for path in directory.iterdir()
                       if path.suffix.lower() in (".json", ".jsonl", ".ndjson") and path.name != "_defaults.json"
                       and not (path.suffix == ".jsonl" and path.stem in texts))
        if stray:
            raise ValueError(f"{directory}: annotation files the generator does not read, with no article or in "
                             f"another format than .jsonl: {', '.join(stray)}")
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


def link_spans(text: str, pattern: re.Pattern) -> list[tuple[int, int]]:
    """Where each link whose destination pattern matches runs, from its [ to its )."""
    return [(start, match.end()) for match in pattern.finditer(text) if (start := opening(text, match.start())) >= 0]


def collapsed(text: str) -> tuple[str, list[int]]:
    """text with each run of white space as one space, and where each of its characters, and its end,
    are in text."""
    out, where = [], []
    i = 0
    for match in WHITE.finditer(text):
        for j in range(i, match.start()):
            out.append(text[j])
            where.append(j)
        out.append(" ")
        where.append(match.start())
        i = match.end()
    for j in range(i, len(text)):
        out.append(text[j])
        where.append(j)
    where.append(len(text))
    return "".join(out), where


def spans(text: str, quote_: dict) -> list[tuple[int, int]]:
    """Where in text a quote's words are, once for each place its prefix, words and suffix match."""
    flat, where = collapsed(text)
    prefix, exact, suffix = (WHITE.sub(" ", quote_.get(key, "")) for key in ("prefix", "exact", "suffix"))
    found, at = [], flat.find(prefix + exact + suffix)
    while exact and at >= 0:
        start = at + len(prefix)
        end = start + len(exact)
        # A quote's own edge is a word's edge: without context, "group" is not the end of "subgroup".
        inside_before = not prefix and exact[0].isalnum() and start > 0 and flat[start - 1].isalnum()
        inside_after = not suffix and exact[-1].isalnum() and end < len(flat) and flat[end].isalnum()
        if not (inside_before or inside_after):
            found.append((where[start], where[end - 1] + 1))
        at = flat.find(prefix + exact + suffix, at + 1)
    return found


def make_quote(text: str, start: int, end: int) -> dict:
    """The quote that selects text[start:end] alone: its words, with as many words before them, and then
    after them, as tell it apart from every other place they occur."""
    flat, where = collapsed(text)
    head = where.index(start) if start in where else next(i for i, at in enumerate(where) if at >= start)
    tail = next(i for i, at in enumerate(where) if at >= end)
    exact = flat[head:tail]
    # No context first, then context out to each word boundary.
    boundaries_before = [head] + [i for i in range(head - 1, -1, -1) if i == 0 or flat[i - 1] == " "][:40]
    boundaries_after = [tail] + [i for i in range(tail + 1, len(flat) + 1) if i == len(flat) or flat[i] == " "][:40]
    for after in boundaries_after:
        for before in boundaries_before:
            candidate = {"exact": exact}
            if before < head:
                candidate["prefix"] = flat[before:head]
            if after > tail:
                candidate["suffix"] = flat[tail:after]
            if spans(text, candidate) == [(start, end)]:
                return candidate
    raise ValueError(f"the words {exact!r} cannot be told apart from another place in the text")


def concept_end(concept: str, modules: frozenset[str] | set[str]) -> tuple[list[dict], dict | None]:
    """The object of an article's own annotation, and its extensions, for its concept key."""
    if re.match(r"[^.:]*:", concept):
        return [], {NAMESPACE: {"concept": concept}}
    return [{"location": {"module" if concept in modules else "declaration": concept}}], None


def split(text: str, name: str, modules: frozenset[str] | set[str] = frozenset()) -> tuple[str, list[dict]]:
    """An article's one-file form as its Markdown and its annotations; *name* is the file name, without
    .md, and *modules* the names of Mathlib's modules, which a concept key may be."""
    check_links(f"{name}.md", text)
    match = re.match(r"---\n(.*?)\n---\n\n?", text, re.S)
    fields = dict(line.split(":", 1) for line in match.group(1).splitlines() if ":" in line) if match else {}
    fields = {key.strip(): value.strip() for key, value in fields.items()}
    if set(fields) != {"article_id", "concept"} or not all(fields.values()):
        raise ValueError(f"{name}: front matter needs article_id and concept, and nothing else")
    body = text[match.end():]
    if body.startswith("---\n"):
        raise ValueError(f"{name}: the text opens with ---, which would read as front matter")
    trough_links = link_spans(body, TROUGH_LINK)
    pieces, cited, last = [], [], 0
    for link in LEAN_LINK.finditer(body):
        start = opening(body, link.start())
        if start < last:
            raise ValueError(f"{name}: a lean: link inside another link")
        if any(start < end and begin < link.end() for begin, end in trough_links):
            raise ValueError(f"{name}: a lean: link inside or around a trough: link")
        pieces.append(body[last:start])
        at = sum(len(piece) for piece in pieces)
        words = body[start + 1 : link.start()]
        if not words.strip() or words != words.strip():
            raise ValueError(f"{name}: the cited words {words!r} are empty or start or end with white space; "
                             "put the spaces outside the [ ]")
        pieces.append(words)
        cited.append((at, at + len(words), unquote(link.group(1) or link.group(2))))
        last = link.end()
    pieces.append(body[last:])
    markdown = "".join(pieces)
    uri = quote(f"{name}.md")
    obj, extensions = concept_end(fields["concept"], modules)
    rows = [{"id": fields["article_id"], "subject": [{"type": "generic", "uri": uri}], "object": obj}
            | ({"extensions": extensions} if extensions else {})]
    for start, end, declaration in cited:
        rows.append({"subject": [{"type": "generic", "uri": uri, "location": {"quote": make_quote(markdown, start, end)}}],
                     "object": [{"location": {"declaration": declaration}}]})
    return markdown, rows


def jsonl(rows: list[dict]) -> str:
    return "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows)


def combined(path: Path) -> str:
    """The one-file form of the article whose text is at path: front matter from its own annotation,
    and each citation as a [words](lean:Name) link."""
    markdown = path.read_text(encoding="utf-8")
    annotations = path.with_suffix(".jsonl")
    if markdown.startswith("---\n"):
        raise ValueError(f"{path}: has front matter; an article's id and concept go in {annotations.name}")
    for link in LEAN_SCHEME.finditer(markdown):
        line = markdown.count("\n", 0, link.start()) + 1
        raise ValueError(f"{path}:{line}: a citation goes in {annotations.name}, not in a lean: link")
    check_links(str(path), markdown)  # line numbers in the .md itself
    if not annotations.is_file():
        raise ValueError(f"{path}: {annotations.name}, its id, concept and citations, is missing")
    defaults_path = path.parent / "_defaults.json"
    defaults = json.loads(defaults_path.read_text(encoding="utf-8")) if defaults_path.is_file() else None
    if defaults != DEFAULTS:
        raise ValueError(f"{defaults_path} must be {json.dumps(DEFAULTS)}")
    uri = quote(path.name)
    own, citations, problems = None, [], []
    for number, line in enumerate(annotations.read_text(encoding="utf-8").splitlines(), 1):
        where = f"{annotations}:{number}"
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as error:
            problems.append(f"{where}: not JSON ({error})")
            continue
        subject = row.get("subject")
        if not (isinstance(subject, list) and len(subject) == 1 and isinstance(subject[0], dict)
                and subject[0].get("type") == "generic" and subject[0].get("uri") == uri):
            problems.append(f"{where}: the subject must be one generic end, {{\"type\": \"generic\", \"uri\": \"{uri}\"}}")
            continue
        ends = row.get("object")
        if not isinstance(ends, list) or any(not isinstance(end, dict) or {"type", "uri"} & end.keys()
                                             or not isinstance(end.get("location"), dict) for end in ends):
            problems.append(f"{where}: each object end is a Mathlib location, with type and uri from _defaults.json")
            continue
        location = subject[0].get("location")
        if location is None:
            if own is not None:
                problems.append(f"{where}: a second annotation about the whole article")
            own = row
            continue
        words = location.get("quote") if isinstance(location, dict) else None
        names = [end["location"].get("declaration") for end in ends]
        if not isinstance(words, dict) or not words.get("exact") or len(names) != 1 or not names[0]:
            problems.append(f"{where}: a citation quotes words and names one declaration")
            continue
        found = spans(markdown, words)
        if len(found) != 1:
            problems.append(f"{where}: the quote {words['exact']!r} matches {len(found)} places in {path.name}")
            continue
        start, end = found[0]
        line_start = markdown.rfind("\n", 0, start) + 1
        if BLANK_LINE.search(markdown, start, end) or BLOCK_START.search(markdown, start, end) \
                or HEADING.match(markdown, line_start):
            problems.append(f"{where}: the quote {words['exact']!r} runs across paragraphs, headings or list items, "
                            "or sits in a heading")
            continue
        citations.append((start, end, names[0], where))
    if own is None:
        problems.append(f"{annotations}: no annotation about the whole article, with its id and concept")
    if problems:
        raise ValueError("\n".join(problems))
    article_id = own.get("id")
    extension = (own.get("extensions") or {}).get(NAMESPACE) or {}
    targets = [end["location"].get("declaration") or end["location"].get("module") for end in own["object"]]
    concept = targets[0] if len(targets) == 1 and targets[0] and not extension else extension.get("concept")
    if not article_id or not concept or (targets and extension):
        raise ValueError(f"{annotations}: the article's own annotation needs an id and one concept: "
                         "one declaration or module, or extensions.org.trough.concept with an empty object")
    taken = link_spans(markdown, TROUGH_LINK)
    citations.sort()
    for (start, end, _, where), following in zip(citations, citations[1:] + [None]):
        if following and following[0] < end:
            raise ValueError(f"{where} and {following[3]}: quotes overlap")
        if any(start < link_end and link_start < end for link_start, link_end in taken):
            raise ValueError(f"{where}: the quote overlaps a trough: link")
    out, last = [], 0
    for start, end, name, _ in citations:
        out += [markdown[last:start], "[", markdown[start:end], "](", lean_target(name), ")"]
        last = end
    out.append(markdown[last:])
    return f"---\narticle_id: {article_id}\nconcept: {concept}\n---\n\n" + "".join(out)
