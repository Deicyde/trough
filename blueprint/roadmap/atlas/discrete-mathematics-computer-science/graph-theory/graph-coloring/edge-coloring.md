---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SimpleGraph.EdgeColoringWanted.IsProperEdgeColoring, MathlibExt.Combinatorics.SimpleGraph.EdgeColoringWanted.multigraph_regular_color, MathlibExt.Combinatorics.SimpleGraph.EdgeColoringWanted.multigraph_bounded_color, MathlibExt.Combinatorics.SimpleGraph.EdgeColoringWanted.konig_line_coloring, MathlibExt.Combinatorics.SimpleGraph.EdgeColoringWanted.IsProperSym2Coloring, MathlibExt.Combinatorics.SimpleGraph.EdgeColoringWanted.isProperEdgeColoring_of_isProperSym2Coloring, MathlibExt.Combinatorics.SimpleGraph.EdgeColoringWanted.IsProperSym2Coloring.mono, MathlibExt.Combinatorics.SimpleGraph.EdgeColoringWanted.vizing
statement: formalized
proof: formalized
---

# Edge coloring

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/edge-coloring/index.html).

## Proper edge coloring

Let $G$ be a simple graph on $V$. An edge labeling $C$ of $G$ with
colors in $K$ is a proper edge coloring when any two distinct edges of $G$ that share a vertex
receive different colors: whenever a vertex $v$ is adjacent to $w_1$ and to $w_2$ with
$w_1 \ne w_2$, the edges $v w_1$ and $v w_2$ have different colors under $C$.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.EdgeColoringWanted.IsProperEdgeColoring`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeColoring.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeColoring.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/edge-coloring/index.html#is-proper-edge-coloring).

## König's edge coloring theorem for regular bipartite multigraphs

König's line coloring, regular multigraph case: a `d`-regular bipartite
multigraph (given by endpoint projections) is `d`-edge-colorable. The proof
extracts a perfect matching by Hall's theorem and inducts. Shared API also
used by the multigraph Galvin development.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.EdgeColoringWanted.multigraph_regular_color`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeColoring.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeColoring.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/edge-coloring/index.html#k-nig-s-edge-coloring-theorem-for-regula).

## König's edge coloring theorem for bounded-degree bipartite multigraphs

König's line coloring, bounded-degree multigraph case: a bipartite
multigraph of maximum degree at most `d` is `d`-edge-colorable. The proof
pads both sides with dummy edges to reach the regular case. Shared API also
used by the multigraph Galvin development.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.EdgeColoringWanted.multigraph_bounded_color`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeColoring.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeColoring.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/edge-coloring/index.html#k-nig-s-edge-coloring-theorem-for-bounde).

## König's line coloring theorem

Every finite bipartite simple graph $G$ has a proper edge
coloring with $\Delta(G)$ colors, where $\Delta(G)$ is the maximum degree of $G$.

Since every proper edge coloring of $G$ needs at least $\Delta(G)$ colors, the edge chromatic
number of $G$ equals $\Delta(G)$.

## Sources

- D. Konig, Theorie der endlichen und unendlichen Graphen, Akademische Verlagsgesellschaft (1936).

Formalized by `MathlibExt.Combinatorics.SimpleGraph.EdgeColoringWanted.konig_line_coloring`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeColoring.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeColoring.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/edge-coloring/index.html#konig-line-coloring).

## Proper coloring of unordered pairs

Let $G$ be a simple graph on $V$. A map $c$ that
assigns a color in $K$ to every unordered pair of elements of $V$ is a proper coloring of
unordered pairs for $G$ when, for all vertices $x, y, z$ such that $x$ is adjacent to both $y$ and
$z$ and $y \ne z$, the pairs $\{x, y\}$ and $\{x, z\}$ receive different colors under $c$.

Only pairs that are edges of $G$ are constrained, so the same map $c$ can be compared across
different graphs on $V$.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.EdgeColoringWanted.IsProperSym2Coloring`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeColoring.lean, line 717](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeColoring.lean#L717). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/edge-coloring/index.html#is-proper-sym2-coloring).

## Proper colorings of unordered pairs restrict to proper edge colorings

Let $G$ be a
simple graph on $V$ and let $c$ assign a color in $K$ to every unordered pair of elements of $V$.
If $c$ is a proper coloring of unordered pairs for $G$, then the edge labeling of $G$ that gives
each edge $e$ the color $c(e)$ is a proper edge coloring of $G$.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.EdgeColoringWanted.isProperEdgeColoring_of_isProperSym2Coloring`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeColoring.lean, line 723](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeColoring.lean#L723). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/edge-coloring/index.html#is-proper-edge-coloring-of-is-proper-sym).

## Proper colorings of unordered pairs pass to subgraphs

Let $G$ and $H$ be simple graphs
on $V$ such that every edge of $H$ is an edge of $G$. If a map $c$ from unordered pairs of
elements of $V$ to $K$ is a proper coloring of unordered pairs for $G$, then it is also a proper
coloring of unordered pairs for $H$.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.EdgeColoringWanted.IsProperSym2Coloring.mono`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeColoring.lean, line 731](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeColoring.lean#L731). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/edge-coloring/index.html#mono).

## Vizing's theorem

Let $G$ be a simple graph on a finite vertex set and let $\Delta$ be its
maximum degree. Then $G$ has a proper edge coloring with $\Delta + 1$ colors: there is an
assignment of colors from $\{0, 1, \dots, \Delta\}$ to the edges of $G$ such that any two
distinct edges sharing a vertex receive different colors.

## Sources

- V. G. Vizing, Diskret. Analiz 3 (1964), 25-30.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.EdgeColoringWanted.vizing`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Vizing.lean, line 1183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Vizing.lean#L1183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/edge-coloring/index.html#vizing).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Edge coloring](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/edge-coloring/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-coloring/part-01/edge-coloring)
