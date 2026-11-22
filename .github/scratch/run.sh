set -uo pipefail
mkdir -p out
ref=$(cat .github/autoform-ref)
AF="uvx --from git+${AUTOFORM_SOURCE}@${ref} autoform"
uv run pytest -q 2>&1 | tail -15 | tee out/pytest.log
time uv run --no-dev python tools/refresh_satellites.py > out/refresh.log 2>&1
grep '::warning' out/refresh.log > out/refresh-warnings.txt
uv run --no-dev python tools/generate.py > out/generate-full.log 2>&1; gen=$?
tail -30 out/generate-full.log > out/generate.log
git add -A data blueprint hooks README.md
git diff --cached --binary -- blueprint hooks data README.md > out/patch.diff
git diff --cached --stat | tail -5 > out/stat.txt
if [ $gen -ne 0 ]; then echo "generate exit $gen" | tee -a out/generate.log; exit 1; fi
uv run --no-dev python tools/generate.py --check && echo CHECK-OK | tee -a out/generate.log
uv run pytest -q 2>&1 | tail -8 | tee -a out/pytest.log
python3 .github/scratch/placements.py out/placements-after.json
python3 - <<'PY' > out/homes.txt
import pathlib
rows = []
for page in sorted(pathlib.Path("blueprint/roadmap").glob("**/projects/README.md")):
    folder = page.parent
    leaves = [p for p in folder.rglob("*.md") if p.name != "README.md"]
    nodes = sum(1 for p in leaves if "\ndeclaration: module\n" in p.read_text()[:400])
    listed = sum(1 for p in folder.rglob("README.md") for line in p.read_text().splitlines() if line.startswith("- [") and "lean files" in line)
    size = sum(p.stat().st_size for p in folder.rglob("*.md"))
    rows.append((len(leaves) - nodes, nodes, listed, str(folder.relative_to("blueprint/roadmap")), size))
rows.sort(key=lambda r: -(r[0] + r[1] + r[2]))
print("homes", len(rows), "cards", sum(r[0] for r in rows), "root-module cards", sum(r[1] for r in rows), "listed", sum(r[2] for r in rows))
for r in rows: print(*r)
PY
cat out/homes.txt
python3 .github/scratch/gt.py 20261119 > out/ground-truth.txt 2>&1; tail -1 out/ground-truth.txt
$AF check blueprint > out/check.txt 2>&1; echo "check exit $?" | tee -a out/check.txt
$AF audit blueprint > out/audit.txt 2>&1; echo "audit exit $?" >> out/audit.txt
{ echo "errors $(grep -c '^error' out/audit.txt)"; echo "duplicate-lean-target $(grep -c 'duplicate-lean-target' out/audit.txt)";
  grep '^error' out/audit.txt | sed -E 's/^error: [^:]*: ([a-z-]+):.*/\1/' | sort | uniq -c; } > out/audit-counts.txt
grep "projects/" out/check.txt out/audit.txt | head -80 > out/satellite-findings.txt
$AF render blueprint --output site-src --repository-url "https://github.com/Deicyde/trough" --ref HEAD > out/render.txt 2>&1; echo "render exit $?" | tee -a out/render.txt
grep "projects/" out/render.txt | grep -v "declaration not found" | head -50 >> out/satellite-findings.txt
uvx --from mkdocs==1.6.1 --with mkdocs-material==9.7.7 --with mkdocs-literate-nav==0.6.2 --with markdown==3.10.3 --with pymdown-extensions==11.0.1 mkdocs build --strict > out/mkdocs.txt 2>&1; echo "mkdocs exit $?" | tee -a out/mkdocs.txt
python3 scripts/check_site.py site-src site > out/check_site.txt 2>&1; echo "check_site exit $?" | tee -a out/check_site.txt
find site -type f | wc -l > out/site-files.txt
du -sh site >> out/site-files.txt
find site -path '*projects*' -name '*.html' -exec ls -l {} \; | awk '{print $5, $9}' | sort -n | tail -8 > out/sizes.txt
ls -l site/dependencies/map/data/search.json >> out/sizes.txt
python3 - <<'PY' > out/map.txt
import json, pathlib, glob, collections
data = pathlib.Path("site/dependencies/map/data")
search = (data / "search.json").read_text()
results = {}
for f in sorted(glob.glob(str(data / "parts" / "*.json"))):
    for pid, entry in json.loads(pathlib.Path(f).read_text())["parts"].items():
        for result in entry.get("results", []):
            results[result["id"]] = result
cards = [r for r in results if "/projects/" in r]
print("cards on map", len(cards), "missing from search", [c for c in cards if c.rsplit("/", 1)[-1] not in search][:10])
print("status", collections.Counter((results[c]["caption"], results[c]["status"]) for c in cards).most_common())
node = next(c for c in cards if c.startswith("mathlib/overview/analysis/projects") and results[c]["caption"] == "Module")
listing = next(str(p.parent.relative_to("blueprint")) for p in sorted(pathlib.Path("blueprint/roadmap").glob("**/projects/README.md"))
               if "## Projects without a named main result" in p.read_text())
shots = [
    ["01-overview", "dependencies/map/#part=mathlib/overview", False],
    ["02-host-analysis", "dependencies/map/#part=mathlib/overview/analysis", False],
    ["03-box-analysis", "dependencies/map/#part=mathlib/overview/analysis/projects", False],
    ["04-module-node", f"dependencies/map/#result={node}", False],
    ["05-module-node-local", f"dependencies/map/#result={node}", False, "local"],
    ["06-listed-project", f"{listing}/#projects-without-a-named-main-result", False],
    ["07-host-batteries", "dependencies/map/#part=batteries", False],
    ["08-box-batteries", "dependencies/map/#part=batteries/projects", False],
    ["09-batteries-projects-page", "roadmap/batteries/projects/", False],
]
pathlib.Path("out/shots.json").write_text(json.dumps(shots))
print(json.dumps(shots))
PY
cat out/map.txt
python3 -m http.server 8765 --directory site > /dev/null 2>&1 &
sleep 2
uv run --with playwright==1.56.0 python -m playwright install --with-deps chromium > out/playwright.txt 2>&1
uv run --with playwright==1.56.0 python .github/scratch/shots.py http://127.0.0.1:8765 out/shots out/shots.json 2>&1 | tee out/shots.txt
