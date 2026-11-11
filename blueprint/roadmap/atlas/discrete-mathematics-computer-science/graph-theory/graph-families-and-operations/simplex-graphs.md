---
declaration: section
origin: cited
lean: SimpleGraph.SimplexVertex, SimpleGraph.emptyVertex, SimpleGraph.singletonVertex, SimpleGraph.simplexGraph, SimpleGraph.adj_iff, SimpleGraph.empty_adj_singleton
statement: formalized
proof: formalized
---

# Simplex graphs

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/simplex-graphs/index.html).

## Simplex vertices

Let $G$ be a simple graph on a vertex type $V$. A simplex vertex
of $G$ is a finite set $s$ of vertices that is a clique of $G$, meaning that any two distinct
elements of $s$ are adjacent in $G$.

Formalized by `SimpleGraph.SimplexVertex`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/SimplexGraph.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/SimplexGraph.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/simplex-graphs/index.html#simplex-vertex).

## Empty simplex vertex

Let $G$ be a simple graph. The empty simplex vertex of $G$ is
the empty set of vertices, which is a clique of $G$.

Formalized by `SimpleGraph.emptyVertex`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/SimplexGraph.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/SimplexGraph.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/simplex-graphs/index.html#empty-vertex).

## Singleton simplex vertex

Let $G$ be a simple graph. For a vertex $v$ of $G$, the
singleton simplex vertex of $v$ is the one-element set containing $v$, which is a clique of
$G$.

Formalized by `SimpleGraph.singletonVertex`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/SimplexGraph.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/SimplexGraph.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/simplex-graphs/index.html#singleton-vertex).

## Simplex graph

Let $G$ be a simple graph. The simplex graph of $G$ is the simple graph
whose vertices are the simplex vertices of $G$ (the finite cliques of $G$), in which two cliques
$s$ and $t$ are adjacent exactly when their symmetric difference $s \triangle t$ has exactly one
element.

The vertex type of $G$ is not required to be finite.

Formalized by `SimpleGraph.simplexGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/SimplexGraph.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/SimplexGraph.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/simplex-graphs/index.html#simplex-graph).

## Adjacency in the simplex graph

Let $G$ be a simple graph. Two simplex vertices $s$ and
$t$ of $G$ are adjacent in the simplex graph of $G$ if and only if their symmetric difference
$s \triangle t$ has exactly one element.

Formalized by `SimpleGraph.adj_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/SimplexGraph.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/SimplexGraph.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/simplex-graphs/index.html#adj-iff).

## The empty clique is adjacent to every singleton

Let $G$ be a simple graph. For every
vertex $v$ of $G$, the empty simplex vertex of $G$ and the singleton simplex vertex of $v$ are
adjacent in the simplex graph of $G$.

Formalized by `SimpleGraph.empty_adj_singleton`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/SimplexGraph.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/SimplexGraph.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/simplex-graphs/index.html#empty-adj-singleton).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Simplex graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/simplex-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-families-and-operations/simplex-graphs)
