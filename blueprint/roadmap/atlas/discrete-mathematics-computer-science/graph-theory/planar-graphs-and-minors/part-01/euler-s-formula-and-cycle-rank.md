---
declaration: section
origin: cited
lean: StatMech.Lattice.card_subtype_ne_add_one, StatMech.Lattice.card_edgeSet_sup_edge, StatMech.Lattice.card_components_bot, StatMech.Lattice.nullity, StatMech.Lattice.faceCount, StatMech.Lattice.euler_relation, StatMech.Lattice.connected_card_edges_ge, StatMech.Lattice.connected_card_edges_eq_iff_isAcyclic
statement: formalized
proof: formalized
---

# Euler's formula and cycle rank

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html).

## Removing one element lowers cardinality by one

Removing one element from a finite type lowers its cardinality by one. See also Mathlib's
`Fintype.card_subtype_compl`.

Formalized by `StatMech.Lattice.card_subtype_ne_add_one`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CycleRank.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CycleRank.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#card-subtype-ne-add-one).

## Adding a new edge increases the edge count by one

Adding a new edge increases the number of edges by one. This is the `Set.ncard` form of
Mathlib's `SimpleGraph.card_edgeFinset_sup_edge`.

Formalized by `StatMech.Lattice.card_edgeSet_sup_edge`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CycleRank.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CycleRank.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#card-edge-set-sup-edge).

## Edgeless graph has one component per vertex

The edgeless graph has one component per vertex.

Formalized by `StatMech.Lattice.card_components_bot`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CycleRank.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CycleRank.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#card-components-bot).

## Cycle rank of a finite graph

The cycle rank (nullity, first Betti number) `|E| + c - |V|` of a finite graph, where `c` is the
number of connected components.

Formalized by `StatMech.Lattice.nullity`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CycleRank.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CycleRank.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#nullity).

## Face count of a finite graph from its cycle rank

The face count `nullity G + 1`. For a finite subgraph of `ℤ²` it is the number of faces,
including the unbounded one (`StatMech.Lattice.jed_faithfulDiscreteJordan` counts the bounded
ones); as a definition it is purely combinatorial.

Formalized by `StatMech.Lattice.faceCount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CycleRank.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CycleRank.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#face-count).

## Combinatorial Euler relation for finite graphs

The combinatorial Euler relation `|V| + F = |E| + c + 1` for a finite graph, where `F =
faceCount G` is defined from the cycle rank.

Formalized by `StatMech.Lattice.euler_relation`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CycleRank.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CycleRank.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#euler-relation).

## Connected finite graph has at least $|V| - 1$ edges

A connected finite graph has at least `|V| - 1` edges. This is the `Fintype` form of Mathlib's
`SimpleGraph.Connected.card_vert_le_card_edgeSet_add_one`.

Formalized by `StatMech.Lattice.connected_card_edges_ge`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/Cyclomatic.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/Cyclomatic.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#connected-card-edges-ge).

## Connected graph with $|V| - 1$ edges is acyclic, and conversely

A connected finite graph has exactly `|V| - 1` edges iff it is acyclic. See also Mathlib's
`SimpleGraph.isTree_iff_connected_and_card` and `SimpleGraph.IsTree.card_edgeFinset`.

Formalized by `StatMech.Lattice.connected_card_edges_eq_iff_isAcyclic`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/Cyclomatic.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/Cyclomatic.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#connected-card-edges-eq-iff-is-acyclic).

## Cyclomatic number $|E| + 1 - |V|$ of a finite graph

The cyclomatic number `|E| + 1 - |V|` of a finite graph. For a connected graph it is the
dimension of the cycle space. See `StatMech.Lattice.nullity` for the version for arbitrary
finite graphs.

Formalized by `StatMech.Lattice.cyclomaticNumber`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/Cyclomatic.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/Cyclomatic.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#cyclomatic-number).

## Graph stays connected with a given bridge after deleting edges

After deleting the edges `B'`, the graph `A` is connected and `{a, b}` is one of its bridges.

Formalized by `StatMech.Lattice.ecc_DualCutModel`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerComponentCount.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerComponentCount.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#ecc-dual-cut-model).

## Vertices of the grid $(-n, n)^2$

The vertices of the grid `[-n, n]²`.

Formalized by `StatMech.Lattice.boxVerts`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerFaces.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerFaces.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#box-verts).

## Horizontal edges of the grid $(-n, n)^2$

The horizontal edges of the grid `[-n, n]²`.

Formalized by `StatMech.Lattice.hEdges`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerFaces.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerFaces.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#h-edges).

## Vertical edges of the grid $(-n, n)^2$

The vertical edges of the grid `[-n, n]²`.

Formalized by `StatMech.Lattice.vEdges`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerFaces.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerFaces.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#v-edges).

## Edges of the grid $(-n, n)^2$

The edges of the grid `[-n, n]²`.

Formalized by `StatMech.Lattice.boxEdges`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerFaces.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerFaces.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#box-edges).

## Unit squares of the grid $(-n, n)^2$

The unit squares of the grid `[-n, n]²`, labelled by their lower left corners.

Formalized by `StatMech.Lattice.boxCells`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerFaces.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerFaces.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#box-cells).

## Number of faces of the grid $(-n, n)^2$

The number of faces of the grid `[-n, n]²`: its unit squares and the unbounded face.

Formalized by `StatMech.Lattice.boxFaceCount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerFaces.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerFaces.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#box-face-count).

## Euler's formula for the grid graph $(-n, n)^2$

Euler's formula `V - E + F = 2` for the planar grid graph `[-n, n]²`, with faces counted
geometrically (unit squares plus the unbounded face).

Formalized by `StatMech.Lattice.box_euler`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerFaces.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerFaces.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#box-euler).

## Square lattice induced on the box $(-n, n)^2$

The subgraph of the square lattice induced on the box `[-n, n]²`.

Formalized by `StatMech.Lattice.boxInduce`, an abbreviation declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerFaces.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerFaces.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#box-induce).

## Euler's formula

**Euler's formula** for a finite graph with `c` connected components: `|V| - |E| + F = 1 + c`,
where `F = faceCount G`.

Here `F` is defined as the cycle rank plus one, so the statement is the combinatorial Euler
relation; it agrees with `StatMech.Lattice.euler_relation_sub` up to the order of the summands. That
`F` counts the faces of a plane embedding is a separate statement; for finite subgraphs of the
square lattice the bounded faces are counted in `StatMech.Lattice.jed_faithfulDiscreteJordan`.
Reference: L. Euler, *Elementa doctrinae solidorum* (1758).

Formalized by `StatMech.Lattice.euler_general`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerGeneral.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerGeneral.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#euler-general).

## Euler's formula solved for the number of components

Euler's formula solved for the number of components: `c = |V| - |E| + F - 1`.

Formalized by `StatMech.Lattice.euler_general_disconnected_components`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerGeneral.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerGeneral.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#euler-general-disconnected-components).

## Non-bridge edge of a graph

`e` is an edge of `A` whose endpoints remain connected after `e` is deleted.

Formalized by `StatMech.Lattice.tnse_IsNonBridgeEdge`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TreeNoSepEuler.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TreeNoSepEuler.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#tnse-is-non-bridge-edge).

## Deleting a list of edges from a graph

`A` with the edges of the list `L` deleted.

Formalized by `StatMech.Lattice.tnse_deleteList`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TreeNoSepEuler.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TreeNoSepEuler.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#tnse-delete-list).

## Successive deletion of non-bridge edges

Deleting the edges of `L` from the last to the first, each edge is a non-bridge at the moment
it is deleted.

Formalized by `StatMech.Lattice.tnse_AllNonBridge`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TreeNoSepEuler.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TreeNoSepEuler.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#tnse-all-non-bridge).

## Three-step detour avoiding an edge

The edge `e = {a, b}` has a three-step detour `a, a', b', b` in `A` none of whose edges is
`e` or lies in `L`.

Formalized by `StatMech.Lattice.tnse_HasTreeFreeDetour`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TreeNoSepEuler.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TreeNoSepEuler.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html#tnse-has-tree-free-detour).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Euler's formula and cycle rank](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/planar-graphs-and-minors/euler-s-formula-and-cycle-rank)
