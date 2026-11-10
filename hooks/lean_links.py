"""Link the Lean names of the blueprint libraries' articles to their documentation.

AutoformBot looks an article's `lean:` names up only in this repository's Lean
sources, which hold none of these libraries' declarations, so each card calls
them "not found in the Lean sources". tools/generate.py writes
hooks/lean-links.json, each chapter's names and their documentation pages, and
this hook makes those rows links. scripts/check_site.py fails if one is left. A key
names a directory under roadmap/, a chapter or one library of a chapter, and a page
takes the longest key its path starts with.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

LINKS = json.loads((Path(__file__).with_name("lean-links.json")).read_text(encoding="utf-8"))
MISSING = re.compile(r'<code>([^<]*)</code> <span class="bp-missing">not found in the Lean sources</span>')


def on_page_content(html_text: str, *, page, config, files) -> str:
    parts = page.file.src_uri.split("/")
    keys = ("/".join(parts[1:end]) for end in range(len(parts) - 1, 1, -1)) if parts[0] == "roadmap" else ()
    links = next((LINKS[key] for key in keys if key in LINKS), {})
    if not links:
        return html_text

    def link(match: re.Match) -> str:
        url = links.get(html.unescape(match.group(1)))
        if url is None:
            return match.group()
        return f'<a href="{html.escape(url, quote=True)}"><code>{match.group(1)}</code></a>'

    return MISSING.sub(link, html_text)
