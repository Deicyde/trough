---
declaration: section
origin: cited
lean: MathlibExt.GraphTheory.CycleContinuousAntichainWanted.FGraph, MathlibExt.GraphTheory.CycleContinuousAntichainWanted.IsFiniteNontrivial, MathlibExt.GraphTheory.CycleContinuousAntichainWanted.cycleSpace, MathlibExt.GraphTheory.CycleContinuousAntichainWanted.IsCycleContinuous, MathlibExt.GraphTheory.CycleContinuousAntichainWanted.conjecture, MathlibExt.GraphTheory.CycleContinuousAntichainWanted.conjecture_holds
statement: formalized
---

# Cycle-continuous maps

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/cycle-continuous-maps/index.html).

## Multigraphs with loops and parallel edges

A multigraph $G$ consists of a type $V$ of
vertices, a type $E$ of edges, and a map assigning to each edge an ordered pair of vertices,
its two endpoints. Distinct edges may have the same endpoints (parallel edges), and the two
endpoints of an edge may coincide (a loop). Neither $V$ nor $E$ is required to be finite.

## Sources

- [OPG-323] Antichains in the cycle continuous order (URL: http://www.openproblemgarden.org/op/antichains_in_the_cycle_continuous_order).

Formalized by `MathlibExt.GraphTheory.CycleContinuousAntichainWanted.FGraph`, a structure declared in [WantedExt/GraphTheory/CycleContinuousAntichainWanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/CycleContinuousAntichainWanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/cycle-continuous-maps/index.html#fgraph).

## Finite multigraphs with at least one edge

A multigraph $G$ is finite and nontrivial
when its set of vertices and its set of edges are both finite and it has at least one edge.
These are the graphs on which the cycle-continuous order is considered.

## Sources

- [OPG-323] (URL: http://www.openproblemgarden.org/op/antichains_in_the_cycle_continuous_order).

Formalized by `MathlibExt.GraphTheory.CycleContinuousAntichainWanted.IsFiniteNontrivial`, a definition declared in [WantedExt/GraphTheory/CycleContinuousAntichainWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/CycleContinuousAntichainWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/cycle-continuous-maps/index.html#is-finite-nontrivial).

## Binary cycle space

Let $G$ be a multigraph. A set $S$ of edges of $G$ is a binary cycle
when $S$ is finite and every vertex $v$ is an endpoint of an even number of edges of $S$, where
only edges with exactly one endpoint equal to $v$ are counted; loops are not counted, which
agrees modulo $2$ with counting each loop twice. The cycle space of $G$ is the set of all
binary cycles of $G$.

## Sources

- [OPG-323] (URL: http://www.openproblemgarden.org/op/antichains_in_the_cycle_continuous_order).

Formalized by `MathlibExt.GraphTheory.CycleContinuousAntichainWanted.cycleSpace`, a definition declared in [WantedExt/GraphTheory/CycleContinuousAntichainWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/CycleContinuousAntichainWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/cycle-continuous-maps/index.html#cycle-space).

## Cycle-continuous maps

Let $G$ and $H$ be multigraphs. A map $f$ from the edges of $G$
to the edges of $H$ is cycle-continuous when, for every binary cycle $C$ of $H$, the preimage
$f^{-1}(C)$ is a binary cycle of $G$.

## Sources

- [OPG-323] (URL: http://www.openproblemgarden.org/op/antichains_in_the_cycle_continuous_order).

Formalized by `MathlibExt.GraphTheory.CycleContinuousAntichainWanted.IsCycleContinuous`, a definition declared in [WantedExt/GraphTheory/CycleContinuousAntichainWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/CycleContinuousAntichainWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/cycle-continuous-maps/index.html#is-cycle-continuous).

## Infinite antichains in the cycle-continuous order

There is a sequence
$G_0, G_1, G_2, \dots$ of pairwise distinct finite multigraphs, each with at least one edge,
such that for all $i \ne j$ there is no cycle-continuous map from the edges of $G_i$ to the
edges of $G_j$.

## Sources

- [OPG-323] (URL: http://www.openproblemgarden.org/op/antichains_in_the_cycle_continuous_order).

Formalized by `MathlibExt.GraphTheory.CycleContinuousAntichainWanted.conjecture`, a definition declared in [WantedExt/GraphTheory/CycleContinuousAntichainWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/CycleContinuousAntichainWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/cycle-continuous-maps/index.html#conjecture).

## Samal's theorem: infinite antichains in the cycle-continuous order exist

There is a
sequence $G_0, G_1, G_2, \dots$ of pairwise distinct finite multigraphs, each with at least one
edge, such that for all $i \ne j$ there is no cycle-continuous map from the edges of $G_i$ to
the edges of $G_j$.

Samal (Theorem 1.3) proves this with an infinite set of cubic bridgeless graphs that are
pairwise incomparable under cycle-continuous maps, answering the DeVos-Nesetril-Raspaud
antichain question positively.

## Sources

- Robert Samal, Cycle-continuous mappings - order structure, Journal of Graph Theory 85 (2017) 56-73, arXiv:1212.6909, https://arxiv.org/abs/1212.6909.

Stated but not proved: `MathlibExt.GraphTheory.CycleContinuousAntichainWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/GraphTheory/CycleContinuousAntichainWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/CycleContinuousAntichainWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/cycle-continuous-maps/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cycle-continuous maps](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/cycle-continuous-maps/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/algebraic-graph-theory/part-01/cycle-continuous-maps)
