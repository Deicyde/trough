---
declaration: section
origin: cited
lean: SimpleGraph.IsSaturatingNonedge, SimpleGraph.IsSaturatingNonedge.newCopy_of_free, SimpleGraph.saturatingNonedgeGraph, SimpleGraph.numSaturatingNonedges, SimpleGraph.IsSaturated, SimpleGraph.isSaturated_iff_forall_gt, SimpleGraph.isSaturated_iff_missing_edge, SimpleGraph.isSaturated_top
statement: formalized
proof: formalized
---

# Graph saturation

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/graph-saturation/index.html).

## Saturating non-edge

Let $F$ and $G$ be simple graphs. A pair of vertices $x, y$ of $G$ is
an $F$-saturating non-edge of $G$ if $x \ne y$, $x$ and $y$ are not adjacent in $G$, and the graph
$G + xy$ obtained from $G$ by adding the edge $xy$ contains a copy of $F$ (a subgraph isomorphic
to $F$, not necessarily induced).

Formalized by `SimpleGraph.IsSaturatingNonedge`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/SaturatingNonedge.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/SaturatingNonedge.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/graph-saturation/index.html#is-saturating-nonedge).

## A saturating non-edge of an $F$-free graph creates a copy of $F$

Let $F$ and $G$ be simple
graphs, and let $xy$ be an $F$-saturating non-edge of $G$. If $G$ is $F$-free, that is, $G$
contains no copy of $F$, then the graph $G + xy$ obtained from $G$ by adding the edge $xy$
contains a copy of $F$, and $G$ does not.

Formalized by `SimpleGraph.IsSaturatingNonedge.newCopy_of_free`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/SaturatingNonedge.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/SaturatingNonedge.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/graph-saturation/index.html#new-copy-of-free).

## Graph of saturating non-edges

Let $F$ and $G$ be simple graphs. The graph of $F$-saturating
non-edges of $G$ is the simple graph on the vertices of $G$ whose edges are exactly the
$F$-saturating non-edges of $G$.

Formalized by `SimpleGraph.saturatingNonedgeGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/SaturatingNonedge.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/SaturatingNonedge.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/graph-saturation/index.html#saturating-nonedge-graph).

## Number of saturating non-edges

Let $F$ and $G$ be simple graphs such that $G$ has only
finitely many $F$-saturating non-edges. Then $f_F(G)$ is the number of $F$-saturating non-edges
of $G$, counted as unordered pairs $\{x, y\}$, that is, the number of edges of the graph of
$F$-saturating non-edges of $G$.

Formalized by `SimpleGraph.numSaturatingNonedges`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/SaturatingNonedge.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/SaturatingNonedge.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/graph-saturation/index.html#num-saturating-nonedges).

## $H$-saturated graphs

Let $H$ be a simple graph. A simple graph $G$ is $H$-saturated if $G$
is $H$-free (it contains no copy of $H$ as a subgraph) and is maximal with this property: every
$H$-free simple graph $G'$ on the same vertex set as $G$ with $G \subseteq G'$ equals $G$.

Formalized by `SimpleGraph.IsSaturated`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Saturation.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Saturation.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/graph-saturation/index.html#is-saturated).

## Saturation via strict supergraphs

Let $H$ be a simple graph. A simple graph $G$ is
$H$-saturated if and only if $G$ is $H$-free and every simple graph $G'$ on the same vertex set
with $G \subsetneq G'$ contains a copy of $H$.

Formalized by `SimpleGraph.isSaturated_iff_forall_gt`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Saturation.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Saturation.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/graph-saturation/index.html#is-saturated-iff-forall-gt).

## Saturation via missing edges

Let $H$ be a simple graph. A simple graph $G$ is
$H$-saturated if and only if $G$ is $H$-free and, for all distinct vertices $s$ and $t$ of $G$
that are not adjacent in $G$, the graph $G + st$ obtained from $G$ by adding the edge $st$
contains a copy of $H$.

This is the usual missing-edge definition of $H$-saturation.

Formalized by `SimpleGraph.isSaturated_iff_missing_edge`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Saturation.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Saturation.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/graph-saturation/index.html#is-saturated-iff-missing-edge).

## Saturation of complete graphs

Let $H$ be a simple graph. The complete graph on any vertex
set is $H$-saturated if and only if it is $H$-free.

A complete graph has no missing edge, so only $H$-freeness matters. The vertex set of the complete
graph is independent of that of $H$, so this condition is not vacuous: $H$ need not embed in a
complete graph with fewer vertices.

Formalized by `SimpleGraph.isSaturated_top`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Saturation.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Saturation.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/graph-saturation/index.html#is-saturated-top).

## Edge counts of saturated graphs

Let $H$ be a simple graph and $n$ a natural number.
The set of saturated edge counts of $H$ on $n$ vertices is the set of natural numbers $m$ such
that some $H$-saturated simple graph on the vertex set $\{0, 1, \dots, n - 1\}$ has exactly $m$
edges.

Formalized by `SimpleGraph.satCounts`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Saturation.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Saturation.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/graph-saturation/index.html#sat-counts).

## Saturation number

Let $H$ be a simple graph and $n$ a natural number. The saturation
number $\operatorname{sat}(n, H)$ is the minimum number of edges of an $H$-saturated simple graph
on the vertex set $\{0, 1, \dots, n - 1\}$, and is $0$ when no such graph exists.

Formalized by `SimpleGraph.sat`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Saturation.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Saturation.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/graph-saturation/index.html#sat).

## The saturation number is zero when no saturated graph exists

Let $H$ be a simple graph,
$n$ a natural number, and $\operatorname{sat}(n, H)$ the saturation number of $H$ on $n$
vertices. If the set of saturated edge counts of $H$ on $n$ vertices is empty, that is, no
$H$-saturated simple graph on the vertex set $\{0, 1, \dots, n - 1\}$ exists, then
$\operatorname{sat}(n, H) = 0$.

Formalized by `SimpleGraph.sat_eq_zero_of_counts_empty`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Saturation.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Saturation.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/graph-saturation/index.html#sat-eq-zero-of-counts-empty).

## Saturated graphs bound the saturation number

Let $H$ be a simple graph, $n$ a natural
number, and $\operatorname{sat}(n, H)$ the saturation number of $H$ on $n$ vertices. Every
$H$-saturated simple graph on the vertex set $\{0, 1, \dots, n - 1\}$ has at least
$\operatorname{sat}(n, H)$ edges.

Formalized by `SimpleGraph.sat_le_card_of_isSaturated`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Saturation.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Saturation.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/graph-saturation/index.html#sat-le-card-of-is-saturated).

## Saturation number is attained by a saturated graph

Attainment: when a saturated graph exists, some saturated graph has exactly
`sat(n, H)` edges.

Formalized by `SimpleGraph.exists_isSaturated_card_eq_sat`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Saturation.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Saturation.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/graph-saturation/index.html#exists-is-saturated-card-eq-sat).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Graph saturation](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/graph-saturation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/extremal-graph-theory/graph-saturation)
