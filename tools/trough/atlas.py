"""The chapter on ATLAS, Meta's library of textbook mathematics formalized with LLMs: an article per topic of its vault.

facebookresearch/atlas-lean is a Lean library of textbook mathematics generated
with AutoformBot. Its vault, on the wiki/autoform-blueprint branch of
Deicyde/atlas-lean, which the ATLAS site publishes, files the library's results
by area, subject and topic: each result is an article holding an informal
statement, and the vault's link annotations (blueprint/links) give the Lean
declaration that formalizes it. tools/refresh_atlas.py reads a checkout at a
pinned commit into data/atlas/: the areas, subjects and containers in the
vault's order, each result's statement and declaration, and where the
repository's Lean declares that declaration, read by trough.leansource without
Lean. The chapter has a part per area, a page per subject and per branch, and
an article per topic, with a block per result linking its line and its page on
the ATLAS site. The archived first release, v1/, is under a non-commercial
license and is not read. The articles have no edges.
"""

from __future__ import annotations

import json
import posixpath
import re
from collections import Counter
from collections.abc import Callable
from pathlib import Path
from urllib.parse import quote as percent

from . import leansource
from .blueprints import Built, escape
from .formal_conjectures import OPAQUE, natural, plural
from .vault import Container, Entry, Leaf, chunk, slugify

SCHEMA = "trough-atlas/v1"
REPO = "Deicyde/atlas-lean"
UPSTREAM = "facebookresearch/atlas-lean"
BRANCH = "wiki/autoform-blueprint"
SITE = "https://deicyde.github.io/atlas-lean/"
GITHUB = "https://github.com"
TITLE = "ATLAS: textbook mathematics in Lean (Meta)"
# The Lean the vault's declarations live in: the root's proved libraries, its wanted results, and the developments
# under Atlas/. The test libraries and the archived v1/ are not read.
LEAN_ROOTS = ("MathlibExt", "CSLibExt", "PhyslibExt", "WantedExt", "Atlas")
HEADING = re.compile(r"^# (?P<title>.+?)\s*$")
ITEM = re.compile(r"^- \[(?P<text>.*)\]\((?P<target>[^()\s]+)\)\s*$")
PART = re.compile(r"^## \[(?P<text>.*)\]\((?P<target>(?:part-\d+/)+README\.md)\)\s*$")
PART_DIR = re.compile(r"^part-\d+$")
INLINE_LINK = re.compile(r"(?<!!)\[(?P<text>(?:[^\[\]\n]|\[[^\[\]\n]*\])*)\]\((?P<target>[^()\s]+)\)")
UNESCAPED_BRACE = re.compile(r"(?<!\\)\{")
STRONG = re.compile(r"<strong>(?P<name>[^<]+)</strong><br\s*/?>\s*(?P<line>[^<\n]+)")


APACHE = "Apache License Version 2.0, January 2004"


def license_notice(text: str) -> str | None:
    """What a LICENSE says before the Apache License 2.0's own text, on one line ("" when nothing), or None when it
    is not the Apache License 2.0. ATLAS's opens with a sentence of its own."""
    flat = " ".join(text.split())
    index = flat.find(APACHE)
    return flat[:index].strip() if index >= 0 else None


# Reading the vault.

def read_container(roadmap: Path, path: str) -> tuple[dict, list[str]]:
    """A container's title, the prose before its entries, and its entries in order: each a child container or an
    article, by its path under the roadmap, with the text that stands before it. A transparent part's heading is
    skipped: the items under it are the container's own."""
    readme = roadmap / path / "README.md"
    problems: list[str] = []
    if not readme.is_file():
        return {}, [f"{path}/README.md is missing"]
    lines = readme.read_text(encoding="utf-8").split("\n")
    title = HEADING.match(lines[0]) if lines else None
    if not title:
        return {}, [f"{path}/README.md has no title line"]
    prose: list[str] = []
    before: list[str] = []
    entries: list[dict] = []
    started = False
    for line in lines[1:]:
        if PART.match(line):
            started = True
            continue
        item = ITEM.match(line)
        if not item:
            (before if started else prose).append(line)
            continue
        started = True
        target = posixpath.normpath(posixpath.join(path, item["target"]))
        entry = {"before": text} if (text := "\n".join(before).strip()) else {}
        before = []
        if target.endswith("/README.md"):
            entry["container"] = target[: -len("/README.md")]
            if not (roadmap / target).is_file():
                problems.append(f"{path}/README.md links {item['target']}, which is missing")
                continue
        elif target.endswith(".md"):
            entry["article"] = target
            if not (roadmap / target).is_file():
                problems.append(f"{path}/README.md links {item['target']}, which is missing")
                continue
        else:
            problems.append(f"{path}/README.md has an entry that is neither a container nor an article: {item['target']}")
            continue
        entries.append(entry)
    node = {"path": path, "title": title["title"], "prose": "\n".join(prose).strip(), "entries": entries}
    if tail := "\n".join(before).strip():
        node["tail"] = tail
    return node, problems


def read_article(roadmap: Path, path: str) -> tuple[dict, list[str]]:
    lines = (roadmap / path).read_text(encoding="utf-8").split("\n")
    title = HEADING.match(lines[0]) if lines else None
    if not title:
        return {}, [f"{path} has no title line"]
    return {"path": path, "title": title["title"], "statement": "\n".join(lines[1:]).strip()}, []


def read_tree(roadmap: Path, path: str, articles: dict[str, dict], problems: list[str]) -> dict:
    """The container at *path* with its descendants, each article read into *articles*."""
    node, found = read_container(roadmap, path)
    problems += found
    if not node:
        return {}
    for entry in node["entries"]:
        if "container" in entry:
            entry["node"] = read_tree(roadmap, entry.pop("container"), articles, problems)
        else:
            article, found = read_article(roadmap, entry["article"])
            problems += found
            if article:
                articles[article["path"]] = article
    node["entries"] = [entry for entry in node["entries"] if entry.get("node") or entry.get("article") in articles]
    return node


def read_links(blueprint: Path) -> tuple[dict[str, str], list[str]]:
    """Each article's Lean declaration, by its path under the roadmap, from the vault's link annotations."""
    declarations: dict[str, str] = {}
    problems: list[str] = []
    for shard in sorted((blueprint / "links").glob("*.jsonl")):
        for number, line in enumerate(shard.read_text(encoding="utf-8").split("\n"), 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
                uri = row["subject"][0]["uri"]
            except (ValueError, KeyError, IndexError, TypeError):
                problems.append(f"links/{shard.name}:{number} does not read")
                continue
            objects = [item.get("location", {}).get("declaration") for item in row.get("object") or []]
            names = [name for name in objects if isinstance(name, str) and name]
            if not names:
                continue
            path = posixpath.normpath(posixpath.join("links", uri))
            if not path.startswith("roadmap/"):
                problems.append(f"links/{shard.name}:{number} annotates {uri}, outside the roadmap")
                continue
            declarations[path[len("roadmap/"):]] = names[0]
    return declarations, problems


def lean_paths(checkout: Path) -> list[str]:
    return sorted((path.relative_to(checkout).as_posix() for root in LEAN_ROOTS if (checkout / root).is_dir()
                   for path in (checkout / root).rglob("*.lean")), key=natural)


def read_lean(checkout: Path, paths: list[str]) -> tuple[dict[str, dict], Counter]:
    """Where the Lean declares each name: its file, line and kind, and whether its value holds `sorry`; the first
    file in LEAN_ROOTS order wins. A file whose scopes don't close is counted and its names are not read."""
    declared: dict[str, dict] = {}
    counts: Counter = Counter()
    order = {root: index for index, root in enumerate(LEAN_ROOTS)}
    for path in sorted(paths, key=lambda path: (order[path.split("/", 1)[0]], natural(path))):
        counts["lean_files"] += 1
        found = leansource.declarations((checkout / path).read_text(encoding="utf-8"), relaxed=True, wanted=True)
        if found is None:
            counts["unread_files"] += 1
            continue
        for declaration in found:
            if not declaration.name or declaration.private:
                continue
            if declaration.name in declared:
                # Counted by the roots of the file that wins and of this one.
                counts[f"names_declared_twice_{declared[declaration.name]['file'].split('/', 1)[0]}_"
                       f"{path.split('/', 1)[0]}"] += 1
                continue
            declared[declaration.name] = {"file": path, "line": declaration.line, "kind": declaration.kind,
                                          "sorry": declaration.proof_sorry}
    return declared, counts


def status(found: dict | None) -> str:
    if found is None:
        return "absent"
    if found["kind"] in leansource.WANTED_KINDS:
        return "wanted"
    return "sorry" if found["sorry"] else "proved"


def read(checkout: Path) -> tuple[dict, dict[str, list[dict]], dict, list[str]]:
    """The vault's structure, its articles by subject (each with its declaration and where the Lean declares it),
    the counts, and what does not read."""
    blueprint = checkout / "blueprint"
    roadmap = blueprint / "roadmap"
    problems: list[str] = []
    try:
        config = json.loads((blueprint / "atlas.json").read_text(encoding="utf-8"))
        areas = [{"title": title, "subjects": list(subjects)} for title, subjects in config["areas"].items()]
    except (OSError, ValueError, KeyError, AttributeError) as error:
        return {}, {}, {}, [f"blueprint/atlas.json does not read: {error}"]
    articles: dict[str, dict] = {}
    subjects: dict[str, dict] = {}
    for area in areas:
        present = []
        for key in area["subjects"]:
            if not (roadmap / key / "README.md").is_file():
                continue
            node = read_tree(roadmap, key, articles, problems)
            if node:
                subjects[key] = node
                present.append(key)
        area["subjects"] = present
    areas = [area for area in areas if area["subjects"]]
    declarations, link_problems = read_links(blueprint)
    problems += link_problems
    declared, counts = read_lean(checkout, lean_paths(checkout))
    by_subject: dict[str, list[dict]] = {}
    for path, article in sorted(articles.items(), key=lambda item: natural(item[0])):
        name = declarations.get(path)
        found = declared.get(name) if name else None
        article |= {"declaration": name or "", "lean": found}
        counts["results"] += 1
        counts[f"results_{status(found) if name else 'none'}"] += 1
        by_subject.setdefault(path.split("/", 1)[0], []).append(article)
    counts["annotations_without_article"] = sum(1 for path in declarations if path not in articles)
    counts["areas"], counts["subjects"] = len(areas), len(subjects)
    structure = {"areas": areas, "subjects": subjects}
    return structure, by_subject, dict(sorted(counts.items())), problems


# The ATLAS site.

class Unreachable(Exception):
    """The site did not answer at all: a network failure, which says nothing about its pages."""


def anchor(path: str) -> str:
    """The anchor of an article's card on its page, as AutoformBot's render writes it: the article's name."""
    return posixpath.basename(path)[: -len(".md")]


def page_url(directory: str) -> str:
    return f"{SITE}roadmap/{percent(directory)}/index.html"


def article_url(path: str) -> str:
    return f"{page_url(posixpath.dirname(path))}#{anchor(path)}"


def site_problem(paths: list[str], fetch: Callable[[str, str], bytes | None]) -> str | None:
    """Why the site does not serve the articles' cards, or None when it does: each article's page answers and holds
    an element with its anchor. fetch(url, method) gives the body of a GET, None when the site answers that it has
    no such page; it raises Unreachable when the site does not answer."""
    for path in paths:
        url = page_url(posixpath.dirname(path))
        page = fetch(url, "GET")
        if page is None:
            return f"{url} answers that it has no such page"
        if f'id="{anchor(path)}"'.encode() not in page:
            return f"{url} has no card for {anchor(path)}"
    return None


def sample(paths: list[str], size: int = 30) -> list[str]:
    """*size* paths spread evenly over the sorted list, the same for the same list."""
    ordered = sorted(paths, key=natural)
    if len(ordered) <= size:
        return ordered
    return [ordered[index * len(ordered) // size] for index in range(size)]


# The chapter, from the data.

NO_DEPENDS = ("No dependencies are recorded: this chapter reads the vault and the repository's source text without "
              "running Lean, and the vault records no edges between its results.")
LEAN_NAMES = 8  # the names a card's Lean row shows
# The bytes of article Markdown a listing page folds in before its next article starts a page.
PAGE_BUDGET = 300_000
KIND_WORDS = {"theorem": "a theorem", "lemma": "a lemma", "def": "a definition", "abbrev": "an abbreviation",
              "instance": "an instance", "structure": "a structure", "class": "a class", "inductive": "an inductive type",
              "opaque": "an opaque constant", "axiom": "an axiom", "alias": "an alias"}


def load(data: Path) -> dict | None:
    """data/atlas/'s source, structure and articles, when they are there."""
    directory = data / "atlas"
    shards = sorted((directory / "articles").glob("*.json"))
    if not ((directory / "source.json").is_file() and (directory / "structure.json").is_file() and shards):
        return None
    articles = {article["path"]: article for shard in shards
                for article in json.loads(shard.read_text(encoding="utf-8"))["articles"]}
    return {"source": json.loads((directory / "source.json").read_text(encoding="utf-8")),
            "structure": json.loads((directory / "structure.json").read_text(encoding="utf-8")), "articles": articles}


def blob(source: dict, path: str, line: int | None = None) -> str:
    return f"{GITHUB}/{source['repo']}/blob/{source['rev']}/{path}" + (f"#L{line}" if line else "")


def at(source: dict) -> str:
    return f"[{source['rev'][:8]}]({GITHUB}/{source['repo']}/tree/{source['rev']})"


def logical(directory: str) -> str:
    """A directory without its transparent parts' folders."""
    return "/".join(part for part in directory.split("/") if not PART_DIR.match(part))


def key(path: str) -> str:
    return f"atlas-{path}"


def lean_line(article: dict, source: dict) -> str:
    """What formalizes a result, in words, with its line."""
    name, found = article["declaration"], article["lean"]
    if not name:
        return "The vault records no Lean declaration for it."
    if found is None:
        return f"Formalized by `{name}`, which the repository's Lean, as read here, does not declare."
    where = f"[{found['file']}, line {found['line']}]({blob(source, found['file'], found['line'])})"
    if found["kind"] in leansource.WANTED_KINDS:
        return f"Stated but not proved: `{name}` is written with `{found['kind']}` in {where}."
    kind = KIND_WORDS.get(found["kind"], f"a `{found['kind']}`")
    text = f"Formalized by `{name}`, {kind} declared in {where}."
    return text + (" Its value contains `sorry`." if found["sorry"] else "")


def relink(text: str, directory: str, targets: set[str], topics: dict[str, str], source: dict) -> str:
    """The vault's relative links pointed at this chapter's pages: a container at its page or article here, an
    article at its topic's article; anything else at the vault's file at the pin. A URL stays as it is."""
    def link(match: re.Match) -> str:
        target = match["target"]
        if "://" in target or target.startswith(("#", "mailto:")):
            return match.group()
        path = posixpath.normpath(posixpath.join(directory, target.split("#", 1)[0]))
        if path.endswith("/README.md") and key(path[: -len("/README.md")]) in targets:
            return f"[{match['text']}](trough:{key(path[: -len('/README.md')])})"
        if path in topics:
            return f"[{match['text']}](trough:{topics[path]})"
        return f"[{match['text']}]({blob(source, 'blueprint/roadmap/' + path)})"

    return INLINE_LINK.sub(link, text)


def heading(title: str) -> str:
    """A result's title as a heading, each brace outside code and formulas escaped: a heading that ends in `{...}`,
    as "cherry {0, 2}" does, would be read as an attribute list, which the site does not publish."""
    parts, last = [], 0
    for match in OPAQUE.finditer(title):
        parts += [UNESCAPED_BRACE.sub(r"\\{", title[last:match.start()]), match.group()]
        last = match.end()
    return "".join(parts) + UNESCAPED_BRACE.sub(r"\\{", title[last:])


def result_block(article: dict, source: dict, site: bool, relinked: Callable[[str, str], str]) -> str:
    lines = [f"## {heading(article['title'])}", ""]
    if article["statement"]:
        lines += [relinked(article["statement"], posixpath.dirname(article["path"])), ""]
    text = lean_line(article, source)
    if site:
        text += f" [Its page on the ATLAS site]({article_url(article['path'])})."
    lines.append(text)
    return "\n".join(lines)


def tally(articles: list[dict]) -> Counter:
    counts: Counter = Counter()
    for article in articles:
        counts["results"] += 1
        counts[status(article["lean"]) if article["declaration"] else "none"] += 1
    return counts


def described(counts: Counter) -> str:
    """How many of a topic's or a chapter's results the Lean proves, in words."""
    if counts["proved"] == counts["results"]:
        return "proved" if counts["results"] == 1 else "all proved"
    parts = [f"{counts['proved']:,} proved"] if counts["proved"] else []
    if counts["sorry"]:
        parts.append(f"{counts['sorry']:,} with `sorry` in {'its' if counts['sorry'] == 1 else 'their'} value")
    if counts["wanted"]:
        parts.append(f"{counts['wanted']:,} stated but not proved")
    if counts["absent"]:
        parts.append(f"{counts['absent']:,} whose declaration the Lean read here does not declare")
    if counts["none"]:
        parts.append(f"{counts['none']:,} without a declaration")
    if len(parts) > 1:
        return ", ".join(parts[:-1]) + " and " + parts[-1]
    return parts[0] if parts else "none"


def topic(node: dict, articles: list[dict], data: dict, links: dict[str, str], relinked: Callable[[str, str], str],
          title: str | None = None) -> Leaf:
    """A topic's article: a line placing it, the topic's prose, and a block per result in the vault's order."""
    source = data["source"]
    site = bool(source.get("site", {}).get("cards"))
    counts = tally(articles)
    opening = (f"{plural(counts['results'], 'result')}, {described(counts)}, quoted from "
               f"[{source['repo']}]({GITHUB}/{source['repo']}) at commit {at(source)}"
               + (f"; [its page on the ATLAS site]({page_url(node['path'])})" if site else "") + ".")
    parts = [opening]
    if node["prose"]:
        parts.append(relinked(node["prose"], node["path"]))
    parts += [result_block(article, source, site, relinked) for article in articles]
    names = [article["declaration"] for article in articles if article["lean"]]
    fields = [("declaration", "section"), ("origin", "cited")]
    if names:
        shown = list(dict.fromkeys(names))[:LEAN_NAMES]
        fields += [("lean", ", ".join(shown)), ("statement", "formalized")]
        if counts["proved"] == counts["results"]:
            fields.append(("proof", "formalized"))
        for article in articles:
            if article["declaration"] in shown:
                links[article["declaration"]] = blob(source, article["lean"]["file"], article["lean"]["line"])
    leaf = Leaf(escape(title or node["title"]), slugify(posixpath.basename(node["path"]) or node["title"]), fields,
                "\n\n".join(parts), no_depends=NO_DEPENDS)
    leaf.sources = ([(f"ATLAS: {node['title']}", page_url(node["path"]))] if site else []) + [
        (f"{source['repo']} at {source['rev'][:8]}", f"{GITHUB}/{source['repo']}/tree/{source['rev']}/blueprint/roadmap/"
                                                    f"{percent(node['path'])}")]
    return leaf


def credit(source: dict) -> str:
    return (f"The statements, titles and prose are quoted from [{source['repo']}]({GITHUB}/{source['repo']}) at commit "
            f"{at(source)}, under its Apache-2.0 license.")


def chapter(data: dict) -> tuple[Built, dict[str, str]]:
    """The chapter's root, with its articles and counts, and the links of the names its cards' Lean rows show (for
    hooks/lean-links.json). A part per area, a page per subject and per branch, an article per topic."""
    source, structure, articles = data["source"], data["structure"], data["articles"]
    stats: Counter = Counter()
    targets: dict[str, Leaf | Container] = {}
    links: dict[str, str] = {}
    # A container and a topic are known by their folder; an article's link goes to its topic's article.
    containers: set[str] = set()
    topics: dict[str, str] = {}

    def survey(node: dict) -> None:
        containers.add(key(node["path"]))
        for entry in node["entries"]:
            if "node" in entry:
                survey(entry["node"])
            else:
                topics[entry["article"]] = key(node["path"])

    for node in structure["subjects"].values():
        survey(node)

    def relinked(text: str, directory: str) -> str:
        return relink(text, directory, containers, topics, source)

    def build(node: dict, top: bool = False) -> Container | Leaf:
        own = [articles[entry["article"]] for entry in node["entries"] if "article" in entry]
        children = [entry for entry in node["entries"] if "node" in entry]
        if own and not children and not top:
            leaf = topic(node, own, data, links, relinked)
            targets[key(node["path"])] = leaf
            stats["articles"] += 1
            stats.update(tally(own))
            return leaf
        # A subject's folder is in CamelCase; its title gives its slug. Below it, the vault's folders are slugs already.
        container = Container(escape(node["title"]), slugify(node["title"] if top else posixpath.basename(node["path"])))
        targets[key(node["path"])] = container
        stats["containers"] += 1
        placed = False
        for entry in node["entries"]:
            if "node" in entry:
                container.entries.append(Entry(build(entry["node"]),
                                               before=relinked(entry.get("before", ""), node["path"])))
            elif not placed:
                # The container's own results, together, at the place of the first.
                leaf = topic(node, own, data, links, relinked, title=f"{node['title']}: its own results")
                stats["articles"] += 1
                stats.update(tally(own))
                container.entries.append(Entry(leaf))
                placed = True
        counts = tally(collect(node, articles))
        container.prose = "\n\n".join(filter(None, [
            f"{plural(counts['results'], 'result')} of ATLAS's vault, {described(counts)}, in "
            + ("this subject's" if top else "this branch's") + " topics.",
            relinked(node["prose"], node["path"]) if node["prose"] else "",
        ]))
        if node.get("tail"):
            container.tail = relinked(node["tail"], node["path"])
        chunk(container, budget=PAGE_BUDGET)
        return container

    parts = []
    for area in structure["areas"]:
        subjects = []
        for subject in area["subjects"]:
            subjects.append(Entry(build(structure["subjects"][subject], top=True)))
            stats["subjects"] += 1
        container = Container(escape(area["title"]), slugify(area["title"]), subjects)
        container.prose = "\n\n".join([
            f"The {plural(len(subjects), 'subject')} of ATLAS's vault in its area *{escape(area['title'])}*, "
            f"{'a page each, ' if len(subjects) > 1 else ''}in the vault's order.", credit(source)])
        chunk(container)
        parts.append(Entry(container))
        stats["parts"] += 1
    root = Container(TITLE, "atlas", parts)
    root.prose = intro(data, stats)
    return Built(root, targets, {}, dict(stats), Counter()), dict(sorted(links.items()))


def collect(node: dict, articles: dict[str, dict]) -> list[dict]:
    """Every article under a container, in the vault's order."""
    found = []
    for entry in node["entries"]:
        found += collect(entry["node"], articles) if "node" in entry else [articles[entry["article"]]]
    return found


def intro(data: dict, stats: Counter) -> str:
    source = data["source"]
    counts = source["counts"]
    site = source.get("site", {})
    readme = source.get("readme", {})
    words = f" Its README calls it “{readme['description']}”" if readme.get("description") else ""
    site_line = (f"The ATLAS site, {SITE}, publishes the vault, a card per result; each block links its card there."
                 if site.get("cards") else
                 f"The ATLAS site, {SITE}, publishes the vault, but its pages did not hold the results' cards when "
                 "checked, so the blocks do not link them.")
    unread = (f" {plural(counts['unread_files'], 'Lean file')} could not be read, as {'its' if counts['unread_files'] == 1 else 'their'} "
              "scopes do not close as they open, so the names declared there count as not declared."
              if counts.get("unread_files") else "")
    return "\n\n".join([
        f"[ATLAS]({GITHUB}/{UPSTREAM}), the Autoformalized Textbook Library At Scale from Meta, is a Lean library of "
        f"textbook mathematics formalized with LLMs, generated with [AutoformBot]({GITHUB}/facebookresearch/autoform-bot)."
        f"{words}. Its vault, the roadmap the ATLAS site publishes, is kept on the `{BRANCH}` branch of "
        f"[{source['repo']}]({GITHUB}/{source['repo']}); this chapter maps it as read at commit {at(source)} "
        f"({source['date'][:10]}), Lean toolchain {source['toolchain']}, Mathlib "
        f"{source.get('mathlib_version') or source['mathlib'][:8]}.",
        f"The vault files its results by area, subject and topic. There are {plural(stats['results'], 'result')} in "
        f"{plural(stats['articles'], 'topic')}, an article each, under {plural(stats['subjects'], 'subject')} in "
        f"{plural(stats['parts'], 'area')}, with a page for each subject and each branch between a subject and its "
        f"topics. Each result is an informal statement, and the vault's link annotations give the Lean declaration that "
        f"formalizes it. Of the results, {described(stats)}.",
        f"No Lean is run for this chapter. A declaration is found where the repository's Lean declares it, read from "
        f"the source text of {plural(counts.get('lean_files', 0), 'file')} under "
        f"{', '.join(f'`{root}/`' for root in LEAN_ROOTS[:-1])} and `{LEAN_ROOTS[-1]}/`, under the namespaces it sits "
        "in; its line is the line its keyword is on. A result is proved when its declaration's value holds no "
        "`sorry`; `theorem_wanted`, `def_wanted` and `proof_wanted` state a result whose proof is deferred, which "
        f"the blocks call stated but not proved.{unread} The articles have no dependencies: the vault records no "
        "edges between its results.",
        "The archived first release, under `v1/`, is under a non-commercial license that also forbids use for "
        "training models, so it is not read. " + site_line,
        credit(source)[:-1] + (" (its LICENSE file adds that the code is not meant for training models)."
                                if source.get("license_notice") else ".") + " Each result's line is linked.",
    ])
