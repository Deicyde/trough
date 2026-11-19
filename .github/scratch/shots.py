import json, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

url, out = sys.argv[1], Path(sys.argv[2])
shots = json.loads(Path(sys.argv[3]).read_text())
out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    browser = p.chromium.launch()
    for name, target, full, *action in shots:
        page = browser.new_page(viewport={"width": 1440, "height": 900}, reduced_motion="reduce")
        page.route(lambda requested: not requested.startswith(url), lambda route: route.abort())
        page.goto(f"{url}/{target}")
        try:
            if "dependencies/map" in target:
                page.locator(".pm-part").first.wait_for(timeout=60000)
                if "#result=" in target:
                    page.locator(".pm-result.pm-selected").first.wait_for(timeout=60000)
            page.wait_for_load_state("networkidle", timeout=60000)
        except Exception as error:
            print(f"{name}: {error}", file=sys.stderr)
        time.sleep(2)
        try:
            if action and action[0] == "local":
                page.locator(".pm-result.pm-selected").first.click()
                page.locator(".pm-local").first.wait_for(state="visible", timeout=60000)
                time.sleep(2)
            elif action and action[0].startswith("pick:"):
                page.locator(f'.pm-part[aria-label^="{action[0][5:]}"]').first.click()
                time.sleep(3)
        except Exception as error:
            print(f"{name} action: {error}", file=sys.stderr)
        page.screenshot(path=str(out / f"{name}.png"), full_page=full)
        if "dependencies/map" in target:
            reader = page.locator(".pm-reader h2")
            print(name, "reader:", reader.first.inner_text() if reader.count() else None)
        page.close()
    browser.close()
