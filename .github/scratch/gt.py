"""Ground truth for satellite cards: 30 sampled cards checked against the raw files at their pins.

Shares no code with trough: its own front matter reader, comment stripper and declaration regex.
    python gt.py SEED
"""
import json, random, re, subprocess, sys
from pathlib import Path

seed = int(sys.argv[1])
cards = []
for page in sorted(Path("blueprint/roadmap").glob("**/projects/**/*.md")):
    if page.name == "README.md":
        continue
    text = page.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        continue
    front = dict(line.split(": ", 1) for line in text.split("\n---\n", 1)[0].splitlines()[1:] if ": " in line)
    cards.append((page, front, text))
nodes = [c for c in cards if c[1].get("declaration") == "module"]
theorems = [c for c in cards if c[1].get("declaration") != "module"]
rng = random.Random(seed)
sample = rng.sample(theorems, min(20, len(theorems))) + rng.sample(nodes, min(10, len(nodes)))
cache = {}


def raw(repo, rev, path):
    key = (repo, rev, path)
    if key not in cache:
        result = subprocess.run(["gh", "api", "-H", "Accept: application/vnd.github.raw",
                                 f"repos/{repo}/contents/{path}?ref={rev}"], capture_output=True, text=True)
        cache[key] = result.stdout if result.returncode == 0 else None
    return cache[key]


def code(text):
    text = re.sub(r"/-.*?-/", " ", text, flags=re.S)
    return re.sub(r"--[^\n]*", "", text)


DECL = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)*(?:(?:public|private|protected|noncomputable|nonrec)\s+)*(theorem|lemma|def|abbrev|instance|structure|class|inductive|opaque)\s+(\S+)")
passed = failed = 0
for page, front, text in sample:
    slug = page.stem
    record = json.loads(Path(f"data/satellites/{slug}.json").read_text())
    repo, rev = record["repo"], record["rev"]
    names = [n for n in front.get("lean", "").split(", ") if n]
    problems = []
    proved = front.get("proof") == "formalized"
    if front.get("declaration") == "module":
        roots = {r["name"]: r["file"] for r in record.get("root_modules", [])}
        lakefile = (raw(repo, rev, (record["folder"] + "/" if record["folder"] else "") + "lakefile.toml")
                    or raw(repo, rev, (record["folder"] + "/" if record["folder"] else "") + "lakefile.lean") or "")
        for name in names:
            path = roots.get(name)
            if not path:
                problems.append(f"{name}: not a root module in the record")
                continue
            source = raw(repo, rev, path)
            if source is None:
                problems.append(f"{name}: {path} missing at the pin")
                continue
            if not path.endswith(name.replace(".", "/") + ".lean"):
                problems.append(f"{name}: file {path} does not match the module name")
            if name.split(".")[0] not in lakefile:
                problems.append(f"{name}: its root is not named in the lakefile")
            if proved and re.search(r"\b(sorry|admit)\b", code(source)):
                problems.append(f"{name}: proof claimed but the root file holds sorry")
        kind = "module"
    else:
        heads = {h["name"]: h for h in record["headlines"]}
        for name in names[:2]:
            head = heads.get(name)
            if not head:
                problems.append(f"{name}: not a headline in the record")
                continue
            source = raw(repo, rev, head["file"])
            if source is None:
                problems.append(f"{name}: {head['file']} missing at the pin")
                continue
            line = source.splitlines()[head["line"] - 1] if head["line"] <= len(source.splitlines()) else ""
            match = DECL.match(line)
            if not match:
                problems.append(f"{name}: line {head['line']} declares nothing: {line.strip()[:80]!r}")
            else:
                if match.group(1) != head["kind"]:
                    problems.append(f"{name}: kind {match.group(1)} at the pin, {head['kind']} on the card")
                declared = match.group(2).strip("«»")
                if not (name == declared or name.endswith("." + declared)):
                    problems.append(f"{name}: the line declares {declared}")
            if proved and re.search(r"\b(sorry|admit)\b", code(source)):
                problems.append(f"{name}: proof claimed but its file holds sorry")
            if record["headline_rule"] == "readme":
                readme = (raw(repo, rev, record["readme"]["file"]) or "") + "\n" + (
                    raw(repo, rev, record["folder"] + "/README.md") or "" if record["folder"] else "")
                tail = name.split(".")[-1]
                if f"`{name}`" not in readme and not re.search(rf"`[\w.']*{re.escape(tail)}`", readme):
                    problems.append(f"{name}: the README does not name it in code")
        kind = front.get("declaration")
    title = re.search(r"^# (.+)$", text, re.M).group(1)
    readme_title = (record["readme"].get("title") or "").strip()
    generic = readme_title.casefold().strip(" :") in {"license", "overview", "introduction", "installation", "usage",
                                                       "contents", "readme", "about"}
    expected = readme_title if readme_title and len(readme_title) <= 50 and not generic else repo.split("/")[1]
    if title.replace("\\", "") != expected:
        problems.append(f"title {title!r}, expected {expected!r}")
    status = "PASS" if not problems else "FAIL"
    passed += not problems
    failed += bool(problems)
    print(f"{status} {slug} ({kind}{', proof' if proved else ''}): {', '.join(names[:3])}" +
          ("" if not problems else "\n    " + "\n    ".join(problems)))
print(f"{passed} of {passed + failed} pass ({len(nodes)} root-module cards and {len(theorems)} cards in all)")
