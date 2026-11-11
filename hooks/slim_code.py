"""Drop the syntax highlighter's spans that change nothing on the page.

Pygments wraps every token of a highlighted code block in a span. Material
colors a whitespace span with nothing, and a name span (`n`) with the code's
own color, so those spans only add bytes and elements: on a page of Lean
statements they are about half of it. AutoformBot's stylesheet sets code in
the dark scheme in another color, so a block that loses its names' spans is
marked `plain-names`, which theme/main.html sets in the name color there.
"""

from __future__ import annotations

import re

BLOCK = re.compile(r'<div class="((?:[^"]*\s)?highlight(?:\s[^"]*)?)">(\s*<pre>.*?</pre>\s*)</div>', re.S)
PLAIN = re.compile(r'<span class="[wn]">([^<]*)</span>')
NAME = '<span class="n">'


def slim(block: re.Match) -> str:
    classes, code = block.group(1), block.group(2)
    if NAME in code:
        classes += " plain-names"
    return f'<div class="{classes}">{PLAIN.sub(r"\1", code)}</div>'


def on_page_content(html_text: str, *, page, config, files) -> str:
    return BLOCK.sub(slim, html_text)
