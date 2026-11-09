from pathlib import Path

from trough.vault import Container, Entry, Leaf, assign_paths, chunk, frontmatter, link_text, rel, render_container, slugify


def leaf(title: str) -> Leaf:
    return Leaf(title, slugify(title), [("declaration", "theorem")], "Body.")


def test_slugify_reads_math_accents_dashes_and_apostrophes():
    assert slugify(r"$\C$ is algebraically closed") == "c-is-algebraically-closed"
    assert slugify("Gödel’s Incompleteness Theorem") == "godels-incompleteness-theorem"
    assert slugify("Lyapunov–Malkin theorem") == "lyapunov-malkin-theorem"
    assert slugify("!!!") == "untitled"


def test_chunk_keeps_every_page_at_twenty_entries():
    container = Container("Many", "many", [Entry(leaf(f"Item {n:03d}")) for n in range(401)])
    chunk(container)
    assert len(container.entries) <= 20

    def pages(node: Container):
        yield node
        for entry in node.entries:
            if isinstance(entry.node, Container):
                yield from pages(entry.node)

    assert all(len(page.entries) <= 20 for page in pages(container))
    leaves = [node for page in pages(container) for node in page.children if isinstance(node, Leaf)]
    assert len(leaves) == 401
    # A part holding one entry is titled by it.
    assert container.entries[-1].node.title == "Item 400"


def test_references_stay_out_of_a_containers_directory():
    home = Container("Home", "home", [Entry(leaf("Shared"))])
    other = Container("Other", "other", [Entry(home.entries[0].node, owned=False, label="Shared, listed again")])
    root = Container("Root", "root", [Entry(home), Entry(other)])
    assign_paths(root, Path("vault/roadmap/root"))
    shared = home.entries[0].node
    assert shared.path == Path("vault/roadmap/root/home/shared.md")
    page = render_container(other, Path("vault"), None)
    assert "- [Shared, listed again](../home/shared.md)" in page


def test_rel_and_frontmatter():
    assert rel(Path("roadmap/a/b.md"), Path("roadmap/c/d.md")) == "../c/d.md"
    previous = "---\narticle_id: af_0123456789abcdef01234567\n---\n"
    assert frontmatter([("declaration", "def")], previous).startswith("---\narticle_id: af_0123456789abcdef01234567\n")
    assert frontmatter([], None) == ""


def test_link_text_escapes_brackets_outside_code_spans_only():
    assert link_text("A [b] and `[Γ(N)]` over `k[X]`") == "A \\[b\\] and `[Γ(N)]` over `k[X]`"


def test_entries_after_pagination_parts_are_lines_of_their_own():
    library = Container("Library", "library", [Entry(leaf(f"Item {n:02d}")) for n in range(21)])
    chunk(library)
    library.entries += [Entry(Container("Main results", "main-results"), before="## Main results\n\nOn a page."),
                        Entry(leaf("After"))]
    assign_paths(library, Path("vault/roadmap/library"))
    page = render_container(library, Path("vault"), None)
    assert page.startswith("# Library\n\n## [Item 00 to Item 19](part-01/README.md)\n\n- [Item 00](part-01/item-00.md)\n")
    assert ("- [Item 20](part-02/item-20.md)\n\n## Main results\n\nOn a page.\n\n- [Main results](main-results/README.md)\n"
            "- [After](after.md)\n") in page
