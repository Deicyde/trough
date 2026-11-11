---
declaration: section
origin: cited
lean: MetaMathlibExt.menger_vertex, MathlibExt.Combinatorics.SimpleGraph.MengerVertexWanted.IsInternallyVertexDisjointSTPaths, MathlibExt.Combinatorics.SimpleGraph.MengerVertexWanted.IsSTVertexCut, MathlibExt.Combinatorics.SimpleGraph.MengerVertexWanted.isSTVertexCut_iff_walkSeparator, MathlibExt.Combinatorics.SimpleGraph.MengerVertexWanted.menger_vertex_max_min, MathlibExt.Combinatorics.SimpleGraph.MengerEdgeWanted.IsEdgeDisjointSTPaths, MathlibExt.Combinatorics.SimpleGraph.MengerEdgeWanted.IsSTEdgeCut, MathlibExt.Combinatorics.SimpleGraph.MengerEdgeWanted.menger_edge_max_min
statement: formalized
proof: formalized
---

# Menger's theorem

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/menger-s-theorem/index.html).

## Menger's theorem, vertex form

Let $G$ be a simple graph on a finite vertex set and let
$s$ and $t$ be distinct, nonadjacent vertices of $G$. Then there is a natural number $n$ with
the following two properties. First, there is a set $C$ of exactly $n$ vertices with
$s \notin C$ and $t \notin C$ such that every walk from $s$ to $t$ passes through a vertex of
$C$, and every set of vertices with these three properties has at least $n$ elements. Second,
there are $n$ paths $P_1, \dots, P_n$ from $s$ to $t$ (walks that repeat no vertex) such that
every vertex lying on both $P_i$ and $P_j$ for some $i \ne j$ is $s$ or $t$, and every finite
family of paths from $s$ to $t$ with this property has at most $n$ members. Thus the minimum
number of vertices other than $s$ and $t$ whose removal separates $s$ from $t$ equals the
maximum number of pairwise internally disjoint paths from $s$ to $t$.

## Sources

- K. Menger, *Zur allgemeinen Kurventheorie*, Fund. Math. 10 (1927), 96–115, doi:10.4064/fm-10-1-96-115; statement as in https://en.wikipedia.org/wiki/Menger%27s_theorem (`menger-s1`).

Formalized by `MetaMathlibExt.menger_vertex`, a theorem declared in [MathlibExt/Combinatorics/Graph/MengerVertex.lean, line 1887](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/MengerVertex.lean#L1887). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/menger-s-theorem/index.html#menger-vertex).

## Internally vertex-disjoint paths

Let $G$ be a simple graph with vertices $s$ and $t$,
and let $P_0, \dots, P_{n-1}$ be a family of paths from $s$ to $t$ in $G$, indexed by
$\{0, \dots, n-1\}$. The family is internally vertex-disjoint when for all indices $i \ne j$,
every vertex lying on both $P_i$ and $P_j$ is $s$ or $t$.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MengerVertexWanted.IsInternallyVertexDisjointSTPaths`, a definition declared in [MathlibExt/Combinatorics/Graph/MengerVertex.lean, line 1946](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/MengerVertex.lean#L1946). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/menger-s-theorem/index.html#is-internally-vertex-disjoint-stpaths).

## Vertex cuts separating two vertices

Let $G$ be a simple graph on a finite vertex set, let
$s$ and $t$ be vertices of $G$, and let $C$ be a set of vertices of $G$. Then $C$ is an $s$-$t$
vertex cut when $s \notin C$, $t \notin C$, and $t$ is not reachable from $s$ in the graph
obtained from $G$ by deleting every edge that has an endpoint in $C$.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MengerVertexWanted.IsSTVertexCut`, a definition declared in [MathlibExt/Combinatorics/Graph/MengerVertex.lean, line 1952](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/MengerVertex.lean#L1952). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/menger-s-theorem/index.html#is-stvertex-cut).

## Vertex cuts are walk separators

Let $G$ be a simple graph on a finite vertex set, let $s$
and $t$ be vertices of $G$, and let $C$ be a set of vertices of $G$. Then $C$ is an $s$-$t$ vertex
cut if and only if $s \notin C$, $t \notin C$, and every walk from $s$ to $t$ in $G$ passes
through a vertex of $C$.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MengerVertexWanted.isSTVertexCut_iff_walkSeparator`, a theorem declared in [MathlibExt/Combinatorics/Graph/MengerVertex.lean, line 2032](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/MengerVertex.lean#L2032). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/menger-s-theorem/index.html#is-stvertex-cut-iff-walk-separator).

## Menger's theorem for vertex cuts and internally disjoint paths

Let $G$ be a simple graph on a
finite vertex set and let $s$ and $t$ be distinct, nonadjacent vertices of $G$. Then there is a
natural number $k$ such that there exist $k$ internally vertex-disjoint paths from $s$ to $t$ and
an $s$-$t$ vertex cut with exactly $k$ vertices, every family of internally vertex-disjoint
paths from $s$ to $t$ has at most $k$ members, and every $s$-$t$ vertex cut has at least $k$
vertices. In words, the maximum number of internally vertex-disjoint paths from $s$ to $t$
equals the minimum size of an $s$-$t$ vertex cut.

## Sources

- K. Menger, Fund. Math. 10 (1927), DOI 10.4064/fm-10-1-96-115.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MengerVertexWanted.menger_vertex_max_min`, a theorem declared in [MathlibExt/Combinatorics/Graph/MengerVertex.lean, line 2055](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/MengerVertex.lean#L2055). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/menger-s-theorem/index.html#menger-vertex-max-min).

## Edge-disjoint paths

Let $G$ be a simple graph with vertices $s$ and $t$. A family
$P_0, \dots, P_{n-1}$ of paths from $s$ to $t$ in $G$ is edge-disjoint when, for all indices
$i \ne j$, no edge of $P_i$ is an edge of $P_j$.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MengerEdgeWanted.IsEdgeDisjointSTPaths`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/MengerEdge.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/MengerEdge.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/menger-s-theorem/index.html#is-edge-disjoint-stpaths).

## Edge cuts separating two vertices

Let $G$ be a simple graph on a finite vertex set and let
$s$ and $t$ be vertices of $G$. A finite set $C$ of unordered pairs of vertices is an $s$-$t$ edge
cut when every element of $C$ is an edge of $G$ and $t$ is not reachable from $s$ in the graph
obtained from $G$ by deleting the edges in $C$.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MengerEdgeWanted.IsSTEdgeCut`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/MengerEdge.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/MengerEdge.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/menger-s-theorem/index.html#is-stedge-cut).

## Menger's theorem for edge cuts and edge-disjoint paths

Let $G$ be a simple graph on a finite
vertex set and let $s$ and $t$ be distinct vertices of $G$. Then there is a natural number $k$ such
that there exist $k$ edge-disjoint paths from $s$ to $t$ and an $s$-$t$ edge cut with exactly $k$
edges, every family of edge-disjoint paths from $s$ to $t$ has at most $k$ members, and every
$s$-$t$ edge cut has at least $k$ edges. In words, the maximum number of edge-disjoint paths from
$s$ to $t$ equals the minimum size of an $s$-$t$ edge cut.

## Sources

- K. Menger, Zur allgemeinen Kurventheorie, Fund. Math. 10 (1927), 96-115, DOI 10.4064/FM-10-1-96-115.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.MengerEdgeWanted.menger_edge_max_min`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/MengerEdge.lean, line 1305](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/MengerEdge.lean#L1305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/menger-s-theorem/index.html#menger-edge-max-min).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Menger's theorem](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/menger-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/paths-cycles-connectivity/menger-s-theorem)
