"""The chapter on Anthropic's Lean proof of Fermat's Last Theorem: one article per landmark theorem.

github.com/anthropics/fermats-last-theorem proves Fermat's Last Theorem along
the route of Frey, Serre, Ribet, Wiles and Taylor-Wiles. Its PROOF-PATH.md
describes the route in six steps and a section on the exact strength of the
named steps. Its web pages' data, html/data/meta.js, list every theorem
(29,511), mark the landmarks and their aliases and put each theorem in a route
stage; html/data/edges.js is the citation graph, the `import Theorems.Thm_*`
lines of each proof module, which the repository documents as exactly the
theorems the proof cites. A theorem `X.y` is stated in Theorems/Thm_X_y.lean.

tools/refresh_anthropic_flt.py reads these at a pinned commit into
data/anthropic-flt/: source.json (the commit, the formalization.yaml's facts
and PROOF-PATH.md's steps) and landmarks.json (each landmark's stage, aliases
and Lean statement, and the nearest landmarks its proof reaches). No Lean runs:
the chapter records what the repository states. The generated English titles
and summaries of the web pages are left out, since the repository says they are
generated and their references not individually verified.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from collections.abc import Callable
from pathlib import Path

from . import ff, formalization, leansource
from .blueprints import Built, escape
from .mathlib import fence
from .vault import Container, Entry, Leaf, chunk, slugify, walk

SOURCE_SCHEMA = "trough-anthropic-flt-source/v1"
LANDMARKS_SCHEMA = "trough-anthropic-flt-landmarks/v1"
REPO = "anthropics/fermats-last-theorem"
GITHUB = "https://github.com"
# The Imperial College London FLT project's chapter, whose `lean` names a landmark's names are compared with.
IMPERIAL = "flt"
STEP = re.compile(r"^\*\*(?P<number>\d+)\.\s+(?P<title>.+?)\.?\*\*", re.M)
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$", re.M)
PREAMBLE = re.compile(r"^(?:import|attribute)\b")
THEOREM = re.compile(r"^[ \t]*(?:(?:private|protected|nonrec|noncomputable)\s+)*(?:theorem|lemma)\b", re.M)
PROOF_IMPORT = re.compile(r"^import\s+(P2M\.Sol\.\S+)\s*$", re.M)
OPENERS, CLOSERS = "([{⟨⦃", ")]}⟩⦄"
CODE_SPAN = re.compile(r"`[^`\n]*`")
SENTENCE_END = re.compile(r"\.(?=\s|$)")
# PROOF-PATH.md says the repository's Frey package is adapted from the Imperial FLT project, whose chapter
# has an article on its own FreyPackage.
ADAPTED = ("FreyPackage", "adapted from the Imperial College London FLT project")


def read_js(text: str) -> dict:
    """The object a data script assigns, `window.NAME = {...};`. meta.js writes JSON; edges.js writes
    arrays under bare keys."""
    body = text[text.index("=") + 1:].strip().rstrip(";")
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        return {key: json.loads(value) for key, value in re.findall(r"(\w+)\s*:\s*(\[[^\]]*\])", body)}


def statement_file(meta: dict, index: int) -> str:
    """Theorems/Thm_X_y.lean for theorem X.y; meta.js gives the file's stem where two names would share one."""
    stem = meta.get("stemx", {}).get(str(index)) or meta["names"][index].replace(".", "_")
    return f"Theorems/Thm_{stem}.lean"


def landmark_indices(meta: dict) -> list[int]:
    return [index for index, mark in enumerate(meta["lm"]) if mark]


def nearest(index: int, offsets: list[int], targets: list[int], landmarks: set[int]) -> set[int]:
    """The landmarks the proof of theorem *index* reaches through the citation graph, passing only through
    theorems that are not landmarks."""
    seen: set[int] = set()
    stack = list(targets[offsets[index]:offsets[index + 1]])
    found: set[int] = set()
    while stack:
        other = stack.pop()
        if other in seen:
            continue
        seen.add(other)
        if other in landmarks:
            found.add(other)
        else:
            stack += targets[offsets[other]:offsets[other + 1]]
    return found


def statement(text: str) -> dict | None:
    """The theorem a statement file states: its text from the end of the preamble (the imports and the
    `attribute` lines) to the top-level `:=`, the line of its `theorem` keyword, and its full name, with
    the namespaces the file opens before it; None when the file states no theorem. The repository's
    statement files prove by `by`, so text after the cut that does not open with `by` means the cut came
    early, at the `:=` of a `let` in the statement, say: that raises ValueError rather than quote part of a
    statement."""
    blanked = leansource.blank_attributes(leansource.blank(text))
    lines = blanked.split("\n")
    start, offset, attribute = None, 0, False
    for line in lines:
        if not line.strip() or PREAMBLE.match(line) or (attribute and line[:1].isspace()):
            attribute = line.startswith("attribute") or (attribute and line[:1].isspace())
            offset += len(line) + 1
            continue
        start = offset
        break
    if start is None:
        return None
    keyword = THEOREM.search(blanked, start)
    if not keyword:
        return None
    name = re.compile(r"\s*(" + leansource.NAME + ")").match(blanked, keyword.end())
    if not name:
        return None
    scopes: list[str] = []
    for line in blanked[start:keyword.start()].split("\n"):
        if match := leansource.NAMESPACE.match(line):
            scopes += leansource.split(match["name"])
        elif (match := leansource.END.match(line)) and match["name"]:
            del scopes[len(scopes) - len(leansource.split(match["name"])):]
    depth, i = 0, name.end()
    while i < len(blanked):
        char = blanked[i]
        if char in OPENERS:
            depth += 1
        elif char in CLOSERS:
            depth -= 1
        elif depth == 0 and blanked.startswith(":=", i):
            break
        i += 1
    else:
        return None
    own = name.group(1)
    full = own[len("_root_."):] if own.startswith("_root_.") else ".".join(scopes + [own])
    if not re.match(r"\s*by\b", blanked[i + 2:]):
        raise ValueError(f"the text after the top-level `:=` of {full} does not open a tactic proof, so the "
                         "statement may be cut short")
    return {"name": full, "line": blanked.count("\n", 0, keyword.start()) + 1, "statement": text[start:i].strip()}


def proof_path(text: str) -> dict:
    """PROOF-PATH.md as written: its title, the text before the first step, each numbered step (its number,
    its title and its whole text, the bold lead included), and each later `##` section."""
    title = HEADING.search(text)
    sections = [match for match in HEADING.finditer(text) if len(match.group(1)) == 2]
    route = text[: sections[0].start()] if sections else text
    starts = list(STEP.finditer(route))
    intro_from = title.end() if title and len(title.group(1)) == 1 else 0
    steps = []
    for number, match in enumerate(starts):
        end = starts[number + 1].start() if number + 1 < len(starts) else len(route)
        steps.append({"number": int(match["number"]), "title": " ".join(match["title"].split()),
                      "text": route[match.start():end].strip()})
    later = []
    for number, match in enumerate(sections):
        end = sections[number + 1].start() if number + 1 < len(sections) else len(text)
        later.append({"title": match.group(2), "text": text[match.end():end].strip()})
    return {"title": title.group(2) if title and len(title.group(1)) == 1 else "",
            "intro": route[intro_from: starts[0].start() if starts else len(route)].strip(),
            "steps": steps, "sections": later}


def files_to_read(checkout: Path) -> list[str]:
    """The files the refresh reads besides the index files: each landmark's statement file, which meta.js
    names, and each main result's file, which the formalization.yaml names."""
    meta = read_js((checkout / "html/data/meta.js").read_text(encoding="utf-8"))
    config = formalization.load((checkout / "formalization.yaml").read_text(encoding="utf-8"))
    files = [statement_file(meta, index) for index in landmark_indices(meta)]
    files += [str(result["file"]) for result in config.main_results if result.get("declaration") and result.get("file")]
    return list(dict.fromkeys(files))


def read_repository(checkout: Path, rev: str, date: str, paths: set[str]) -> tuple[dict, dict]:
    """The source and landmark records at a commit: *paths* are every file the commit has. Raises
    ValueError when the repository is not Apache-2.0, when PROOF-PATH.md's steps are not numbered 1, 2, ...,
    when a landmark sits in a stage with no step, when a landmark's statement file is missing, states another
    theorem or may be cut short, or when a main result's file is in the commit but not in the checkout."""
    config = formalization.load((checkout / "formalization.yaml").read_text(encoding="utf-8"))
    license_name = formalization.text_of(config.project.get("license"))
    license_file = checkout / "LICENSE"
    if license_name != "Apache-2.0" or not license_file.is_file() or not ff.is_apache(license_file.read_text(encoding="utf-8")):
        raise ValueError(f"not Apache-2.0 (formalization.yaml says {license_name!r})")
    route = proof_path((checkout / "PROOF-PATH.md").read_text(encoding="utf-8"))
    numbers = [step["number"] for step in route["steps"]]
    if not numbers or numbers != list(range(1, len(numbers) + 1)):
        raise ValueError(f"PROOF-PATH.md's steps are numbered {numbers}, not 1, 2, ...")
    meta = read_js((checkout / "html/data/meta.js").read_text(encoding="utf-8"))
    edges = read_js((checkout / "html/data/edges.js").read_text(encoding="utf-8"))
    names, offsets, targets = meta["names"], edges["off"], edges["dst"]
    if len(offsets) != len(names) + 1 or offsets[-1] != len(targets):
        raise ValueError(f"edges.js has {len(offsets)} offsets and {len(targets)} edges for {len(names)} theorems")
    marked = landmark_indices(meta)
    landmarks = set(marked)
    aliases = meta.get("aliases", {})
    records = []
    for index in marked:
        name, stage = names[index], meta["stage"][index]
        if not 0 <= stage <= len(numbers):
            raise ValueError(f"{name} is in stage {stage}, which no step of PROOF-PATH.md holds")
        file = statement_file(meta, index)
        if file not in paths or not (checkout / file).is_file():
            raise ValueError(f"{name}: {file} is missing")
        text = (checkout / file).read_text(encoding="utf-8")
        try:
            stated = statement(text)
        except ValueError as error:
            raise ValueError(f"{file}: {error}") from None
        if not stated or stated["name"] != name:
            raise ValueError(f"{file} states {stated['name'] if stated else 'no theorem'}, not {name}")
        imports = PROOF_IMPORT.findall(text)
        proof = imports[0].replace(".", "/") + ".lean" if len(imports) == 1 else ""
        others = sorted(set(leansource.scan(text) or {}) - {name})
        record = {"name": name,
                  "aliases": [alias.strip() for alias in aliases.get(name, "").split(";") if alias.strip()],
                  "stage": stage, "file": file, "line": stated["line"], "statement": stated["statement"]}
        if proof in paths:
            record["proof_file"] = proof
        if others:
            record["also_declares"] = others
        record["reaches"] = sorted(names[other] for other in nearest(index, offsets, targets, landmarks))
        records.append(record)
    manifest = json.loads((checkout / "lake-manifest.json").read_text(encoding="utf-8"))
    mathlib = next((package.get("rev", "") for package in manifest.get("packages", []) if package.get("name") == "mathlib"), "")
    text = formalization.text_of
    results = []
    for result in config.main_results:
        if not result.get("declaration"):
            continue
        file = str(result.get("file") or "")
        if file in paths and not (checkout / file).is_file():
            raise ValueError(f"{text(result['declaration'])}: {file} is in the commit but not in the checkout")
        scan = leansource.scan((checkout / file).read_text(encoding="utf-8")) if file in paths else None
        found = (scan or {}).get(text(result.get("declaration")))
        results.append({key: value for key, value in {
            "name": text(result.get("declaration")),
            "file": file,
            "found": {"line": found.line, "kind": found.kind, "stated": found.sorry} if found else None,
            "sorry_count": result.get("sorry_count"),
            "axioms": [text(axiom) for axiom in result.get("axioms") or []],
        }.items() if value not in ("", [], None)})
    source = {
        "schema": SOURCE_SCHEMA,
        "repo": REPO,
        "rev": rev,
        "date": date,
        "toolchain": (checkout / "lean-toolchain").read_text(encoding="utf-8").strip().split(":")[-1],
        "mathlib": mathlib,
        "license": license_name,
        **ff.facts_of(config),
        "scope": text(config.status.get("scope")),
        "acknowledgements": text(config.extra.get("acknowledgements")),
        "main_results": results,
        "proof_path": route,
    }
    landmark_data = {
        "schema": LANDMARKS_SCHEMA,
        "rev": rev,
        "counts": {"theorems": len(names), "landmarks": len(records), "edges": len(targets),
                   "landmark_edges": sum(len(record["reaches"]) for record in records),
                   "definition_modules": len(meta.get("defs", []))},
        "stages": meta.get("stages", {}),
        "landmarks": records,
    }
    return source, landmark_data


def shard(name: str, shards: int = 256) -> str:
    """The data shard of the repository's web pages that holds a theorem's record: FNV-1a of its name, over
    UTF-16 code points as the pages' script reads it."""
    value = 2166136261
    for char in name:
        value = ((value ^ ord(char)) * 16777619) & 0xFFFFFFFF
    return f"{value % shards:03d}"


class Unreachable(Exception):
    """The documentation site did not answer at all: a network failure, which says nothing about its pages."""


def docs_problem(url: str, landmarks: dict, fetch: Callable[[str, str], bytes | None]) -> str | None:
    """Why the documentation site at *url* does not serve the landmarks' pages, or None when it does: its
    theorem page answers, its meta.js marks the same landmarks, and each landmark's data shard answers.
    fetch(url, method) gives the body of a GET, b"" for a HEAD that answers, and None when the site answers
    that it has no such page; it raises Unreachable when the site does not answer."""
    page = fetch(url + "thm.html", "GET")
    if not page or b'id="thm-main"' not in page:
        return f"{url}thm.html does not serve the theorem page"
    data = fetch(url + "data/meta.js", "GET")
    try:
        meta = read_js(data.decode("utf-8")) if data else None
    except (ValueError, UnicodeDecodeError):
        meta = None
    if not meta or "names" not in meta or "lm" not in meta:
        return f"{url}data/meta.js does not serve the theorems"
    served = {meta["names"][index] for index in landmark_indices(meta)}
    names = {record["name"] for record in landmarks["landmarks"]}
    if served != names:
        return f"{url}data/meta.js marks {len(served)} landmarks, not the {len(names)} of the pin"
    for number in sorted({shard(name) for name in names}):
        if fetch(f"{url}data/shard/{number}.js", "HEAD") is None:
            return f"{url}data/shard/{number}.js does not answer"
    return None


# The chapter, from the records.

NO_STATEMENT_EDGES = ("The repository's citation graph records the theorems each proof cites, not what statements "
                      "use, so no statement dependencies are listed.")


def load(data: Path) -> tuple[dict, dict] | None:
    directory = data / "anthropic-flt"
    if not (directory / "source.json").is_file() or not (directory / "landmarks.json").is_file():
        return None
    return (json.loads((directory / "source.json").read_text(encoding="utf-8")),
            json.loads((directory / "landmarks.json").read_text(encoding="utf-8")))


def blob(source: dict, path: str, line: int | None = None) -> str:
    return f"{GITHUB}/{source['repo']}/blob/{source['rev']}/{path}" + (f"#L{line}" if line else "")


def at(source: dict) -> str:
    return f"[{source['rev'][:8]}]({GITHUB}/{source['repo']}/tree/{source['rev']})"


def credit(source: dict, file: str, what: str = "", note: str = "") -> str:
    return (f"*Quoted from {what + ' ' if what else ''}[{file}]({blob(source, file)}) of [{source['repo']}]"
            f"({GITHUB}/{source['repo']}) at commit {at(source)}, Apache-2.0{': ' + note if note else ''}.*")


def quote(markdown: str) -> str:
    """Quoted Markdown as a block quote, read as GitHub reads it: each underscore outside code is escaped, as
    the source writes E_P and F_p as plain text, and a list that follows a paragraph line gets the blank line
    before it that the site's Markdown needs to start a list."""
    out, last = [], 0
    for match in CODE_SPAN.finditer(markdown):
        out += [markdown[last:match.start()].replace("_", "\\_"), match.group()]
        last = match.end()
    lines: list[str] = []
    for line in ff.safe("".join(out) + markdown[last:].replace("_", "\\_")).split("\n"):
        if ff.ITEM.match(line) and lines and lines[-1].strip() and not lines[-1][:1].isspace() \
                and not ff.ITEM.match(lines[-1]):
            lines.append("")
        lines.append(line)
    return "\n".join(f"> {line}" if line.strip() else ">" for line in lines)


def span_name(span: str, names: set[str]) -> str | None:
    """The name a code span writes: the whole span, or its first word when a signature follows, as in
    `FreyPackage.no_frey_package (P : FreyPackage) : False`; None when that is none of *names*."""
    head = re.split(r"\s", span.strip("`"), maxsplit=1)[0]
    return head if head in names else None


def mentions(text: str, names: set[str]) -> list[str]:
    """The names a text writes in backticks, alone or with a signature after them, in the order it first does."""
    return list(dict.fromkeys(name for match in CODE_SPAN.finditer(text) if (name := span_name(match.group(), names))))


def step_theorem(step: dict, stage_names: set[str]) -> str | None:
    """The landmark a step opens with, in backticks right after its bold lead, when the step's stage holds it:
    the theorem that carries the step."""
    match = re.match(r"\*\*.+?\*\*\s*(`[^`]+`)", step["text"], re.S)
    return span_name(match.group(1), stage_names) if match else None


def proved_only(markdown: str) -> str:
    """A section's entries with each one's “Proved:” clause kept, to the end of its sentence, and the rest
    cut, marked with …: the map records what the repository proves, not what it leaves out. An entry with no
    such clause is kept whole, unless it says what is not proved, when it is left out."""
    out = []
    for item in re.split(r"(?m)^(?=[-*+] )", markdown):
        body = item.rstrip()
        start = body.find("Proved:")
        if start < 0:
            if "Not proved:" not in body:
                out.append(item)
            continue
        end = SENTENCE_END.search(CODE_SPAN.sub(lambda span: " " * len(span.group()), body), start)
        cut = end.end() if end else len(body)
        out.append(body[:cut].rstrip() + (" …" if body[cut:].strip() else "") + item[len(body):])
    return "".join(out)


def imperial_names(root: Container | None) -> dict[str, Leaf]:
    """Each Lean name of an article in the Imperial FLT chapter, with its article."""
    names: dict[str, Leaf] = {}
    for node in walk(root) if root else ():
        if isinstance(node, Leaf):
            for name in filter(None, dict(node.fields).get("lean", "").split(", ")):
                names.setdefault(name, node)
    return names


def leaf(source: dict, record: dict, title: str, named_in: list[tuple[str, str]], carries: str | None,
         matches: list[str]) -> Leaf:
    name = record["name"]
    fields = [("declaration", "theorem"), ("origin", "cited"), ("lean", name), ("statement", "formalized"),
              ("proof", "formalized")]
    url = blob(source, record["file"], record["line"])
    body = [fence(record["statement"]),
            f"*Quoted from [{record['file']}, line {record['line']}]({url}) of [{source['repo']}]({GITHUB}/{source['repo']}) "
            f"at commit {at(source)}, Apache-2.0: the file's text from the end of its imports and `attribute` lines to "
            "the top-level `:=`.*"]
    if record["aliases"]:
        body.append("Aliases on the repository's web pages: " + ", ".join(f"“{ff.safe(alias)}”" for alias in record["aliases"]) + ".")
    if named_in:
        places = " and ".join(f"[{escape(step)}](trough:{key})" for step, key in named_in)
        body.append(f"PROOF-PATH.md names it in {places}" + (f", as the theorem that carries {carries}." if carries else "."))
    lean = f"`{name}`, stated in [{record['file']}, line {record['line']}]({url})"
    lean += (f" and proved in [{record['proof_file']}]({blob(source, record['proof_file'])})." if record.get("proof_file")
             else ".")
    notes = [("Lean", lean + f" Read at commit {at(source)}, without running Lean.")]
    if matches:
        notes.append(("Imperial FLT", "\n".join(
            f"- `{other}`, {'its name' if other == name else 'which its statement file also declares'}, is also the "
            f"Lean name of [{escape(other)}](trough:imperial:{other}) in the Imperial FLT chapter." for other in matches)))
    result = Leaf(title, slugify(name), fields, "\n\n".join(body), notes=notes)
    result.sources = [(f"Statement of `{name}` in {record['file']}", url)]
    if record.get("proof_file"):
        result.sources.append((f"Proof of `{name}` in {record['proof_file']}", blob(source, record["proof_file"])))
    if source.get("docs"):
        result.sources.append((f"The repository's documentation page for `{name}`", f"{source['docs']}thm.html#{name}"))
    result.no_depends = NO_STATEMENT_EDGES
    return result


def chapter(source: dict, landmarks: dict, imperial: Container | None = None) -> tuple[Built, dict[str, str]]:
    """The chapter's root, with its articles and counts, and each landmark's statement line (for
    hooks/lean-links.json). A part per step of PROOF-PATH.md, and one per later section."""
    route = source["proof_path"]
    records = {record["name"]: record for record in landmarks["landmarks"]}
    by_stage: dict[int, list[str]] = {}
    for record in landmarks["landmarks"]:
        by_stage.setdefault(record["stage"], []).append(record["name"])
    imperial_leaves = imperial_names(imperial)
    targets: dict[str, Leaf | Container] = {}
    if imperial is not None:
        targets["imperial"] = imperial
    keys = {step["number"]: f"step-{step['number']}" for step in route["steps"]}
    titles: dict[str, str] = {name: escape(name) for name in records}
    carries: dict[str, str] = {}
    for step in route["steps"]:
        theorem = step_theorem(step, set(by_stage.get(step["number"], [])))
        if theorem:
            titles[theorem] = ff.safe(step["title"])
            carries[theorem] = f"step {step['number']}"
    sections = [(f"section-{number}", section, proved_only(section["text"]))
                for number, section in enumerate(route["sections"], 1)]
    named_in: dict[str, list[tuple[str, str]]] = {name: [] for name in records}
    for step in route["steps"]:
        for name in mentions(step["text"], set(records)):
            named_in[name].append((f"{step['number']}. {step['title']}", keys[step["number"]]))
    for key, section, text in sections:
        for name in mentions(text, set(records)):
            named_in[name].append((section["title"], key))
    adapted = ADAPTED[0] in imperial_leaves and any(ADAPTED[1] in step["text"] for step in route["steps"])
    if adapted:
        targets[f"imperial:{ADAPTED[0]}"] = imperial_leaves[ADAPTED[0]]
    leaves: dict[str, Leaf] = {}
    stats = {"imperial_matches": 0}
    for name, record in records.items():
        matches = [other for other in [name, *record.get("also_declares", [])] if other in imperial_leaves]
        for other in matches:
            targets[f"imperial:{other}"] = imperial_leaves[other]
        stats["imperial_matches"] += len(matches)
        leaves[name] = leaf(source, record, titles[name], named_in[name], carries.get(name), matches)
        targets[name] = leaves[name]
    for name, record in records.items():
        leaves[name].proof_depends = [leaves[other] for other in record["reaches"] if other in leaves]
    parts = []
    for step in route["steps"]:
        number = step["number"]
        # The statement itself, which the web pages put in a stage before the first step, opens the first step.
        before = by_stage.get(0, []) if number == 1 else []
        groups = [mentions(step["text"], set(group)) for group in (before, by_stage.get(number, []))]
        unnamed = [sorted(set(group) - set(order)) for group, order in zip((before, by_stage.get(number, [])), groups)]
        members = groups[0] + unnamed[0] + groups[1] + unnamed[1]
        part = Container(f"{number}. {ff.safe(step['title'])}", slugify(f"{number} {step['title']}"),
                         [Entry(leaves[name]) for name in members])
        targets[keys[number]] = part
        placed = ((("The theorem itself" if len(before) == 1 else "The theorems") + ", which the repository's web pages "
                   "place before this step, then the landmarks they place in it" if before else
                   "The landmarks the repository's web pages place in this step")
                  + ", in the order this step names them" + (", then by name:" if unnamed[0] or unnamed[1] else ":"))
        part.prose = "\n\n".join([quote(step["text"]), credit(source, "PROOF-PATH.md", "the route of the proof in"),
                                  placed if members else "The repository's web pages place no landmark in this step."])
        parts.append(Entry(chunk(part)))
    for key, section, text in sections:
        named = mentions(text, set(records))
        part = Container(ff.safe(section["title"]), slugify(section["title"]),
                         [Entry(leaves[name], owned=False) for name in named])
        targets[key] = part
        note = "each “Proved:” clause, cut with … where the text goes on" if text != section["text"] else ""
        part.prose = "\n\n".join([quote(text), credit(source, "PROOF-PATH.md", f"the section “{ff.safe(section['title'])}” of",
                                                      note),
                                  "No landmark is placed in this section"
                                  + (". The landmarks it names, placed in the steps:" if named else ", and it names none.")])
        parts.append(Entry(part))
    root = Container("Fermat's Last Theorem (Anthropic)", "anthropic-flt", parts)
    counts = landmarks["counts"]
    stats |= {"articles": len(leaves), "landmark_edges": sum(len(leaf.proof_depends) for leaf in leaves.values()),
              "parts": len(parts), "theorems": counts["theorems"], "edges": counts["edges"]}
    root.prose = intro(source, counts, stats, imperial is not None, by_stage.get(0, []), adapted)
    parts[0].before = "## The route"
    root.tail = "\n\n".join([ff.facts(source) + (f"\n- Scope, as its status states: “{ff.safe(source['scope'])}”"
                                                 if source.get("scope") else ""),
                             main_results(source, records), ff.literature(source)])
    links = {name: blob(source, record["file"], record["line"]) for name, record in records.items()}
    return Built(root, targets, {}, stats, Counter()), links


def main_results(source: dict, records: dict[str, dict]) -> str:
    lines = []
    for result in source["main_results"]:
        found = result.get("found")
        where = (f"stated in [{result['file']}, line {found['line']}]({blob(source, result['file'], found['line'])})"
                 if found else f"which the source text of [{result['file']}]({blob(source, result['file'])}) does not declare")
        details = []
        if result["name"] in records:
            details.append(f"its article: [{escape(result['name'])}](trough:{result['name']})")
        if "sorry_count" in result:
            details.append(f"sorry count {result['sorry_count']}")
        if result.get("axioms"):
            details.append("axioms " + ", ".join(f"`{axiom}`" for axiom in result["axioms"]))
        lines.append(f"- `{result['name']}`, {where}" + "".join(f"; {detail}" for detail in details) + ".")
    return "\n".join(["## Main results", "", "The main results its formalization.yaml lists, with the sorry count and "
                      "axioms it gives for each, and where the source text declares them.", "", *lines])


def intro(source: dict, counts: dict, stats: dict, imperial: bool, before_first: list[str], adapted: bool) -> str:
    repo = f"[{source['repo']}]({GITHUB}/{source['repo']})"
    date = f" ({source['date'][:10]})" if source.get("date") else ""
    route = source["proof_path"]
    matches = stats["imperial_matches"]
    paragraphs = [
        f"{repo}, by {', '.join(source['project']['authors'])}, read at commit {at(source)}{date}. The repository "
        "states that it proves Fermat's Last Theorem in Lean 4 along the route of Frey, Serre, Ribet, Wiles and "
        "Taylor-Wiles. This chapter runs no Lean and checks none of it: what it says about the proof is what the "
        "repository states. Its formalization.yaml describes the project so:",
        f"> {ff.safe(source['project']['description'])}",
        credit(source, "formalization.yaml", "the project description in"),
    ]
    if route["intro"]:
        paragraphs += [f"Its PROOF-PATH.md, “{ff.safe(route['title'])}”, opens:", quote(route["intro"]),
                       credit(source, "PROOF-PATH.md")]
    if source.get("acknowledgements"):
        paragraphs += [f"> {ff.safe(source['acknowledgements'])}", credit(source, "formalization.yaml", "the acknowledgements in")]
    steps = len(route["steps"])
    others = counts["theorems"] - stats["articles"]
    paragraphs.append(
        f"The repository's web pages list {counts['theorems']:,} theorems and mark {counts['landmarks']} of them as "
        f"landmarks. This chapter maps the {stats['articles']} landmarks, one article each, in a part for each of the "
        f"{steps} steps of PROOF-PATH.md, as the web pages place them, and quotes from its other sections; "
        + ("the other theorem is" if others == 1 else f"the other {others:,} theorems are")
        + " counted, not mapped. An article quotes its theorem's Lean statement, from the end of the file's "
        "imports and `attribute` lines to the top-level `:=`, lists the aliases the web pages give it, and links its "
        "line in the repository at the commit above. A theorem a step opens with, when the web pages place it in "
        "that step, takes the step's name as its title; any other has its Lean name."
        + (f" The web pages put {' and '.join(f'`{name}`' for name in before_first)} in a stage before the first "
           f"step, so {'it opens' if len(before_first) == 1 else 'they open'} part 1." if before_first else ""))
    paragraphs.append(
        f"The repository's citation graph has {counts['edges']:,} edges: the `import Theorems.Thm_…` lines of each "
        "proof module, which the repository documents as exactly the theorems the proof cites. Under *Proof depends "
        "on*, an article lists the landmarks its proof reaches through theorems that are not landmarks, "
        f"{stats['landmark_edges']} edges in all.")
    if imperial:
        found = ("At this commit none does." if not matches else
                 f"At this commit {matches} {'name does' if matches == 1 else 'names do'}.")
        paragraphs.append(
            "Where a landmark's name, or another declaration its statement file makes, is also the Lean name of an "
            "article in the [Imperial FLT chapter](trough:imperial), the landmark's article says so and links it. The "
            "names are compared as written, so a match says only that the names agree. " + found
            + (f" The repository's `{ADAPTED[0]}` is {ADAPTED[1]}, as PROOF-PATH.md says, and the Imperial FLT "
               f"chapter has an article on its [`{ADAPTED[0]}`](trough:imperial:{ADAPTED[0]})." if adapted else ""))
    paragraphs.append(
        f"The repository's README points to its documentation website, {source['docs']}, which it says has a page for "
        "each theorem; each article links its theorem's page there, and the data workflow links them only when the "
        "site serves the landmarks' pages."
        if source.get("docs") else
        "Articles link the repository's files at the commit above.")
    paragraphs.append(
        "The web pages also give each theorem an English title and summary, and suggested references. The repository "
        "says the English text is generated automatically from the Lean source, with the Lean statement authoritative, "
        "and that the references have not been individually verified, so this chapter leaves them out. PROOF-PATH.md, "
        "the formalization.yaml and the Lean statements are quoted as written, under the repository's Apache-2.0 "
        "license, with the repository and commit named where they are quoted.")
    return "\n\n".join(paragraphs)
