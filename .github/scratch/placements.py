"""Each satellite on the site: its home, whether it is a card or listed, and its placement sentence, as JSON.
    python placements.py OUT.json
"""
import json, posixpath, re, subprocess, sys
from pathlib import Path

files = subprocess.run(["git", "ls-files", "-co", "--exclude-standard", "blueprint/roadmap"], capture_output=True,
                       text=True, check=True).stdout.split()
out = {}
for name in files:
    if "/projects/" not in name or not name.endswith(".md"):
        continue
    path = Path(name)
    home = name.split("/projects/")[0].removeprefix("blueprint/roadmap/")
    text = path.read_text(encoding="utf-8")
    if path.name == "README.md":
        if "## Projects without a named main result" in text:
            for repo in re.findall(r"^- \[([^\]]+/[^\]]+)\]\(https://github\.com/", text.split("## Projects without a named main result", 1)[1], re.M):
                out[repo.lower()] = {"home": home, "kind": "listed", "placement": ""}
        continue
    repo = re.search(r"^\[([^\]]+/[^\]]+)\]\(https://github\.com/", text, re.M)
    placement = re.search(r"^## Placement\n\n(.*?)\n(?:\n|$)", text, re.M | re.S)
    def edges(title):
        section = re.search(rf"^## {title}\n\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        return sorted(link if "://" in link else posixpath.normpath(posixpath.join(posixpath.dirname(name), link))
                      for link in re.findall(r"\]\(([^)]+)\)", section.group(1))) if section else []
    out[(repo.group(1) if repo else path.stem).lower()] = {
        "home": home, "kind": "card", "placement": placement.group(1).strip() if placement else "",
        "depends": edges("Depends on"), "proof": edges("Proof depends on")}
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, sort_keys=True))
print(len(out), "satellites")
