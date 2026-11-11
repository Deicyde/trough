---
declaration: section
origin: cited
lean: SimpleGraph.square, SimpleGraph.square_adj, SimpleGraph.square_mono, SimpleGraph.Connected.square, SimpleGraph.IsHamiltonian.square_mono, SimpleGraph.eq_square_iff, SimpleGraph.isChain_square_of_isChain_cons_cons, SimpleGraph.IsHamiltonian.square_of_cyclic_list
statement: formalized
proof: formalized
---

# Square of a graph

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/square-of-a-graph/index.html).

## Square of a graph

The square of a simple graph $G$ is the simple graph on the same vertex
set in which two distinct vertices $u$ and $v$ are adjacent when they are adjacent in $G$ or have
a common neighbor in $G$, that is, a vertex $w$ adjacent in $G$ to both $u$ and $v$.

Formalized by `SimpleGraph.square`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Square.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Square.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/square-of-a-graph/index.html#square).

## Adjacency in the graph square

For a simple graph $G$ and vertices $u$ and $v$, the
vertices $u$ and $v$ are adjacent in the square of $G$ if and only if $u \ne v$ and either $u$
and $v$ are adjacent in $G$ or there is a vertex $w$ with $u$ adjacent to $w$ and $w$ adjacent
to $v$ in $G$.

Formalized by `SimpleGraph.square_adj`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Square.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Square.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/square-of-a-graph/index.html#square-adj).

## Monotonicity of the graph square

Let $G$ and $H$ be simple graphs on the same vertex set
such that every edge of $G$ is an edge of $H$. Then every edge of the square of $G$ is an edge of
the square of $H$.

Formalized by `SimpleGraph.square_mono`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Square.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Square.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/square-of-a-graph/index.html#square-mono).

## The square of a connected graph is connected

If a simple graph $G$ is connected, then
the square of $G$ is connected.

Formalized by `SimpleGraph.Connected.square`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Square.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Square.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/square-of-a-graph/index.html#square-2).

## Adding edges preserves a Hamiltonian square

Let $G$ and $H$ be simple graphs on the same
finite vertex set such that every edge of $G$ is an edge of $H$. If the square of $G$ is
Hamiltonian, then the square of $H$ is Hamiltonian.

Formalized by `SimpleGraph.IsHamiltonian.square_mono`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Square.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Square.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/square-of-a-graph/index.html#square-mono-2).

## Characterization of the graph square

Let $G$ and $H$ be simple graphs on the same vertex
set. Then $H$ equals the square of $G$ if and only if, for all vertices $u$ and $v$, the vertices
$u$ and $v$ are adjacent in $H$ exactly when $u \ne v$ and either $u$ and $v$ are adjacent in $G$
or there is a vertex $w$ with $u$ adjacent to $w$ and $w$ adjacent to $v$ in $G$.

Formalized by `SimpleGraph.eq_square_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Square.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Square.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/square-of-a-graph/index.html#eq-square-iff).

## Skipping a vertex of a walk in the graph square

Let $G$ be a simple graph and let
$u, w, v, x_1, \dots, x_k$ (with $k \ge 0$) be a sequence of vertices in which consecutive
vertices are adjacent in $G$. If $u \ne v$, then in the sequence $u, v, x_1, \dots, x_k$
consecutive vertices are adjacent in the square of $G$.

Formalized by `SimpleGraph.isChain_square_of_isChain_cons_cons`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Square.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Square.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/square-of-a-graph/index.html#is-chain-square-of-is-chain-cons-cons).

## A cyclic listing by square adjacencies gives a Hamiltonian square

Let $G$ be a simple
graph on a finite vertex set $V$, and let $v_0, v_1, \dots, v_n$ be vertices with $n \ge 3$ and
$v_0 = v_n$, such that $v_1, \dots, v_n$ are pairwise distinct and every vertex of $V$ is among
them. If for each $i < n$ the vertices $v_i$ and $v_{i+1}$ are distinct and either adjacent in
$G$ or have a common neighbor in $G$, then the square of $G$ is Hamiltonian.

Formalized by `SimpleGraph.IsHamiltonian.square_of_cyclic_list`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Square.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Square.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/square-of-a-graph/index.html#square-of-cyclic-list).

## Minimum degree in the square of a 2-connected graph

In a 2-vertex-connected simple graph
on a finite vertex set with at least five vertices, every vertex has at least four neighbors in
the square of the graph.

Formalized by `SimpleGraph.IsVertexConnected.four_le_square_degree`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Square.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Square.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/square-of-a-graph/index.html#four-le-square-degree).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Square of a graph](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/square-of-a-graph/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/paths-cycles-connectivity/square-of-a-graph)
