---
declaration: section
origin: cited
lean: SimpleGraph.IsVertexConnected, SimpleGraph.isVertexConnected_iff, SimpleGraph.IsVertexConnected.card_gt, SimpleGraph.IsVertexConnected.connected_induce_compl, SimpleGraph.IsVertexConnected.connected, SimpleGraph.IsVertexConnected.connected_compl_singleton, SimpleGraph.isVertexConnected_two_iff, SimpleGraph.IsVertexConnected.two_le_degree
statement: formalized
proof: formalized
---

# Vertex connectivity

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/vertex-connectivity/index.html).

## $k$-vertex-connected graph

Let $k$ be a natural number. A simple graph $G$ on a finite
vertex set $V$ is $k$-vertex-connected if $V$ has more than $k$ elements and, for every set $S$ of
fewer than $k$ vertices, the subgraph of $G$ induced on $V \setminus S$ is connected.

Formalized by `SimpleGraph.IsVertexConnected`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/vertex-connectivity/index.html#is-vertex-connected).

## Characterization of $k$-vertex-connectivity by vertex deletion

Let $k$ be a natural
number and let $G$ be a simple graph on a finite vertex set $V$. Then $G$ is $k$-vertex-connected
if and only if $V$ has more than $k$ elements and, for every set $S$ of fewer than $k$ vertices,
the subgraph of $G$ induced on $V \setminus S$ is connected.

Formalized by `SimpleGraph.isVertexConnected_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/vertex-connectivity/index.html#is-vertex-connected-iff).

## Vertex count of a $k$-vertex-connected graph

Let $k$ be a natural number. If a simple
graph $G$ on a finite vertex set $V$ is $k$-vertex-connected, then $V$ has more than $k$
elements.

Formalized by `SimpleGraph.IsVertexConnected.card_gt`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/vertex-connectivity/index.html#card-gt).

## Deleting fewer than $k$ vertices from a $k$-vertex-connected graph

Let $k$ be a natural
number and let $G$ be a $k$-vertex-connected simple graph on a finite vertex set $V$. Then for
every set $S$ of fewer than $k$ vertices, the subgraph of $G$ induced on $V \setminus S$ is
connected.

Formalized by `SimpleGraph.IsVertexConnected.connected_induce_compl`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/vertex-connectivity/index.html#connected-induce-compl).

## A $k$-vertex-connected graph with $k \ge 1$ is connected

Let $k \ge 1$ be a natural
number. Every $k$-vertex-connected simple graph on a finite vertex set is connected.

Formalized by `SimpleGraph.IsVertexConnected.connected`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/vertex-connectivity/index.html#connected).

## Deleting one vertex from a $k$-vertex-connected graph with $k \ge 2$

Let $k \ge 2$ be a
natural number and let $G$ be a $k$-vertex-connected simple graph on a finite vertex set $V$.
Then for every vertex $v$, the subgraph of $G$ induced on $V \setminus \{v\}$ is connected.

Formalized by `SimpleGraph.IsVertexConnected.connected_compl_singleton`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/vertex-connectivity/index.html#connected-compl-singleton).

## Characterization of 2-vertex-connected graphs

A simple graph $G$ on a finite vertex set
$V$ is 2-vertex-connected if and only if $V$ has more than two elements, $G$ is connected, and
for every vertex $v$ the subgraph of $G$ induced on $V \setminus \{v\}$ is connected.

Formalized by `SimpleGraph.isVertexConnected_two_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/vertex-connectivity/index.html#is-vertex-connected-two-iff).

## Degrees in a 2-vertex-connected graph are at least two

Every vertex of a 2-vertex-connected
simple graph on a finite vertex set has degree at least two.

Formalized by `SimpleGraph.IsVertexConnected.two_le_degree`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/vertex-connectivity/index.html#two-le-degree).

## Cycles through each vertex of a 2-vertex-connected graph

Let $G$ be a 2-vertex-connected
simple graph on a finite vertex set. Then for every vertex $x$ of $G$ there is a cycle in $G$
that starts and ends at $x$.

Formalized by `SimpleGraph.IsVertexConnected.exists_cycle_through`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/VertexConnectivity.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/vertex-connectivity/index.html#exists-cycle-through).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Vertex connectivity](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/vertex-connectivity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/paths-cycles-connectivity/vertex-connectivity)
