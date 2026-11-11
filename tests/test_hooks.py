import importlib.util
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("lean_links", ROOT / "hooks" / "lean_links.py")
lean_links = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lean_links)

MISSING = '<code>{}</code> <span class="bp-missing">not found in the Lean sources</span>'


def shown(src_uri: str, name: str) -> str:
    page = SimpleNamespace(file=SimpleNamespace(src_uri=src_uri))
    return lean_links.on_page_content(MISSING.format(name), page=page, config=None, files=None)


def test_a_page_takes_the_longest_key_its_path_starts_with(monkeypatch):
    monkeypatch.setattr(lean_links, "LINKS", {
        "tauceti": {"T.a": "https://example.org/t"},
        "formal-frontier/topology/lib": {"Lib.thm": "https://example.org/lib#L3"},
        "formal-frontier/topology/other": {"Lib.thm": "https://example.org/other#L9"},
    })
    link = '<a href="https://example.org/lib#L3"><code>Lib.thm</code></a>'
    assert shown("roadmap/formal-frontier/topology/lib/the-highlight.md", "Lib.thm") == link
    assert shown("roadmap/formal-frontier/topology/lib/part-01/a-result.md", "Lib.thm") == link
    assert shown("roadmap/formal-frontier/topology/lib/README.md", "Lib.thm") == link
    # The chapter's root has no key of its own, so its names stay as they are.
    assert shown("roadmap/formal-frontier/README.md", "Lib.thm") == MISSING.format("Lib.thm")
    assert shown("roadmap/tauceti/part-01/a/b.md", "T.a") == '<a href="https://example.org/t"><code>T.a</code></a>'
    assert shown("index.md", "T.a") == MISSING.format("T.a")


SLIM = importlib.util.spec_from_file_location("slim_code", ROOT / "hooks" / "slim_code.py")
slim_code = importlib.util.module_from_spec(SLIM)
SLIM.loader.exec_module(slim_code)


def test_code_blocks_lose_the_spans_of_whitespace_and_names_only():
    code = ('<pre><span></span><code><span class="kd">theorem</span><span class="w"> </span><span class="n">foo</span>'
            '<span class="w"> </span><span class="o">:</span><span class="w">  </span><span class="n">x</span>'
            '<span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="mi">2</span>\n</code></pre>')
    slim = ('<pre><span></span><code><span class="kd">theorem</span> foo <span class="o">:</span>  x '
            '<span class="o">&lt;</span> <span class="mi">2</span>\n</code></pre>')
    prose = '<p>Text with <span class="n">a span</span> outside code.</p>'
    plain = '<div class="highlight"><pre><span></span><code>no tokens\n</code></pre></div>'
    page = slim_code.on_page_content(
        prose + f'<div class="language-lean highlight">{code}</div><div class="highlight">\n{code}\n</div>' + plain,
        page=None, config=None, files=None)
    assert page == (prose + f'<div class="language-lean highlight plain-names">{slim}</div>'
                    f'<div class="highlight plain-names">\n{slim}\n</div>' + plain)
