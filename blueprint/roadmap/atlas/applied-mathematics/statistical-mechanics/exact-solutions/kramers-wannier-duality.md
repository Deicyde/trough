---
declaration: section
origin: cited
lean: StatMech.Ising.transportEdges, StatMech.Ising.incCount, StatMech.Ising.IsEvenSubgraph, StatMech.Ising.isingZ_high_temp_expansion, StatMech.Ising.DualContourMatching, StatMech.Ising.cutEdges, StatMech.Ising.CutEvenSubgraphMatching, StatMech.Ising.cutSpace
statement: formalized
proof: formalized
---

# Kramers–Wannier duality

45 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html).

## Image of an edge set under a vertex bijection

The image of an edge set under a vertex equivalence `V ≃ W`.

Formalized by `StatMech.Ising.transportEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KWDualBijection.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWDualBijection.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#transport-edges).

## Number of edges of an edge set incident to a vertex

The number of edges of `F` incident to `v`.

Formalized by `StatMech.Ising.incCount`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KWSelfDuality.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWSelfDuality.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#inc-count).

## Even subgraph condition on an edge set

Every vertex has even degree in the edge set `F`.

Formalized by `StatMech.Ising.IsEvenSubgraph`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KWSelfDuality.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWSelfDuality.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#is-even-subgraph).

## High-temperature expansion

At zero field, `Z(β) = 2^{|V|} (cosh β)^{|E|} ∑_{F even}
(tanh β)^{|F|}`.

S. Friedli and Y. Velenik, *Statistical Mechanics of Lattice Systems*, Cambridge University
Press (2017), Section 3.7.

Formalized by `StatMech.Ising.isingZ_high_temp_expansion`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/KWSelfDuality.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWSelfDuality.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#ising-z-high-temp-expansion).

## Dual high-temperature expansion proportional to the partition function

`tanh β* = exp (-2β)` and the high-temperature expansion of `Gd` at `β*` equals `c` times
`Z_{Gp}(β)`.

Formalized by `StatMech.Ising.DualContourMatching`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KWSelfDuality.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWSelfDuality.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#dual-contour-matching).

## Edges cut by a spin configuration

The edges `{x, y}` of `G` whose endpoints have different spins in `s`.

Formalized by `StatMech.Ising.cutEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierCutMatching.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierCutMatching.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#cut-edges).

## Proportionality of the cut sum and the dual even-subgraph sum

The cut sum `∑_s t^{|∂s|}` of `Gp` equals `mult` times the even-subgraph sum `∑_F t^{|F|}` of
`Gd`.

Formalized by `StatMech.Ising.CutEvenSubgraphMatching`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierCutMatching.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierCutMatching.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#cut-even-subgraph-matching).

## Cut space of a graph

The cut space: the edge sets `∂s` cut by configurations `s`.

Formalized by `StatMech.Ising.cutSpace`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierDuality.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierDuality.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#cut-space).

## Even subgraphs of a graph

The even subgraphs of `G`.

Formalized by `StatMech.Ising.evenSubgraphs`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierDuality.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierDuality.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#even-subgraphs).

## Spin disagreement test across an edge

Whether the spins of `s` differ at the endpoints of `e`.

Formalized by `StatMech.Ising.edgeDiff`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierDuality.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierDuality.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#edge-diff).

## Edges cut by a configuration via the edge disagreement test

The edges cut by `s`, defined through `edgeDiff`.

Formalized by `StatMech.Ising.cutEdgesB`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierDuality.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierDuality.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#cut-edges-b).

## Cut space defined through Boolean cut edges

The cut space, defined through `cutEdgesB`.

Formalized by `StatMech.Ising.cutSpaceB`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierDuality.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierDuality.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#cut-space-b).

## Even subgraphs defined by a Boolean test

The even subgraphs, defined with a Boolean test.

Formalized by `StatMech.Ising.evenSubgraphsB`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierDuality.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierDuality.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#even-subgraphs-b).

## Complete graph on four vertices

The complete graph `K₄` on `Fin 4`.

Formalized by `StatMech.Ising.K4`, an abbreviation declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierDuality.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierDuality.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#k4).

## Kramers–Wannier duality

**Kramers–Wannier duality** on the self-dual graph `K₄`: if `tanh β* = e^{-2β}` then `Z(β*) =
(2⁴ (cosh β*)^{|E|} / (e^{β|E|} · 2)) Z(β)` at zero field.

H. A. Kramers and G. H. Wannier, *Statistics of the two-dimensional ferromagnet. Part I*,
Phys. Rev. 60 (1941).

Formalized by `StatMech.Ising.isingZ_self_dual_K4`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierDuality.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierDuality.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#ising-z-self-dual-k4).

## Number of disagreeing steps along a walk

The number of steps of a walk whose endpoints have different spins in `s`.

Formalized by `StatMech.Ising.walkDis`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierGeneral.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierGeneral.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#walk-dis).

## Edge crossing between a graph and its dual

An edge bijection `ψ` from `Gp` to `Gd` carrying edges to edges, cuts to even subgraphs, and
even subgraphs back to cuts.

Formalized by `StatMech.Ising.EdgeCrossing`, a structure declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierGeneral.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierGeneral.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#edge-crossing).

## Kramers–Wannier duality

For a preconnected graph `Gp` with an edge crossing to `Gd` and
`tanh β* = e^{-2β}`, `Z_{Gd}(β*) = (2^{|V|} (cosh β*)^{|E_d|} / (e^{β|E_p|} · 2)) Z_{Gp}(β)`
at zero field.

H. A. Kramers and G. H. Wannier, *Statistics of the two-dimensional ferromagnet. Part I*,
Phys. Rev. 60 (1941).

Formalized by `StatMech.Ising.isingZ_self_dual_of_edgeCrossing`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierGeneral.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierGeneral.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#ising-z-self-dual-of-edge-crossing).

## Vertices of K₄ outside a given pair

The two vertices of `Fin 4` other than `a` and `b`.

Formalized by `StatMech.Ising.k4Missing`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierGeneral.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierGeneral.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#k4-missing).

## Complementary edge of a pair in K₄

The edge of `K₄` complementary to `{a, b}`.

Formalized by `StatMech.Ising.k4CompPair`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierGeneral.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierGeneral.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#k4-comp-pair).

## Complementary-edge map of K₄ on unordered pairs

The complementary edge of `K₄`, as a function on `Sym2 (Fin 4)`.

Formalized by `StatMech.Ising.k4Comp`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierGeneral.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierGeneral.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#k4-comp).

## Edge complementation of K₄ as an involutive equivalence

Complementation of edges of `K₄` as an involutive equivalence.

Formalized by `StatMech.Ising.k4CompEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierGeneral.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierGeneral.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#k4-comp-equiv).

## Self-dual edge crossing of K₄ by complementary edges

The edge crossing of the self-dual graph `K₄` given by complementary edges.

Formalized by `StatMech.Ising.k4EdgeCrossing`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierGeneral.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierGeneral.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#k4-edge-crossing).

## Crossing parity of a walk with respect to an edge set

The parity of the number of steps of a walk that use an edge of `δ`.

Formalized by `StatMech.Ising.walkParity`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#walk-parity).

## Evenness of an edge set on every closed walk

Every closed walk of `Gp` uses edges of `δ` an even number of times.

Formalized by `StatMech.Ising.EvenOnCycles`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#even-on-cycles).

## Spin configuration from crossing parities along walks

The configuration assigning to `v` the crossing parity of `δ` along a walk from `v₀` to `v`.

Formalized by `StatMech.Ising.parityConfig`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#parity-config).

## Cycle-parity compatibility of a dual edge set

Every closed walk of `Gp` crosses the pullback of `F` an even number of times.

Formalized by `StatMech.Ising.CycleParityCompatible`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#cycle-parity-compatible).

## Edge crossing from cycle-parity compatibility of even subgraphs

An edge crossing built from cycle-parity compatibility of all even subgraphs of `Gd`.

Formalized by `StatMech.Ising.edgeCrossing_of_cycleParity`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#edge-crossing-of-cycle-parity).

## Cycle-parity compatibility of a family of dual cycle sets

Every edge set in `cycleSets` is cycle-parity compatible.

Formalized by `StatMech.Ising.SingleDualCycleParity`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#single-dual-cycle-parity).

## Cycle-parity compatibility of closed dual walks

Every closed walk of `Gd` has edge set whose pullback is cycle-parity compatible.

Formalized by `StatMech.Ising.ClosedDualWalkParity`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#closed-dual-walk-parity).

## Closed-walk decomposition property of even subgraphs

Every even subgraph of `Gd` is a symmetric difference of edge sets of closed walks.

Formalized by `StatMech.Ising.EvenSubgraphWalkDecomp`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#even-subgraph-walk-decomp).

## Edge crossing from closed-walk parities and walk decompositions

An edge crossing built from closed-walk parities and the decomposition of even subgraphs into
closed walks.

Formalized by `StatMech.Ising.edgeCrossing_of_closedWalkParity`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KramersWannierEvenToCut.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#edge-crossing-of-closed-walk-parity).

## Side-colouring property of closed dual walks

Every closed walk of `Gd` has a two-colouring of the vertices of `Gp` whose boundary is the
pullback of its edges.

Formalized by `StatMech.Ising.DualWalkHasSideColouring`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#dual-walk-has-side-colouring).

## Edge crossing from side colourings of dual walks

An edge crossing built from side colourings of dual walks.

Formalized by `StatMech.Ising.edgeCrossing_of_sideColouring`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#edge-crossing-of-side-colouring).

## Simple graph spanned by an edge set

The simple graph with edge set `F`.

Formalized by `StatMech.Ising.subgraphF`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#subgraph-f).

## Component of a vertex in the graph spanned by an edge set

The component of `f` in the graph spanned by `F`.

Formalized by `StatMech.Ising.compF`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#comp-f).

## Vertex set of a component of the graph spanned by an edge set

The vertices of the component of `f` in the graph spanned by `F`.

Formalized by `StatMech.Ising.compSuppF`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#comp-supp-f).

## Closed Eulerian walk of a component of an even edge set

A closed Eulerian walk of the component of `f` in an even edge set `F`.

Formalized by `StatMech.Ising.compEulerWalk`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#comp-euler-walk).

## Even subgraphs of a finite graph decompose into closed walks

Every even subgraph decomposes into closed walks.

Formalized by `StatMech.Ising.evenSubgraphWalkDecomp_general`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean, line 545](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean#L545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#even-subgraph-walk-decomp-general).

## Edge boundary of a region in a graph

The edges of `Gp` whose endpoints lie on different sides of the region `S`.

Formalized by `StatMech.Ising.regionBoundary`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#region-boundary).

## Region-bounding property of closed dual walks

Every closed walk of `Gd` pulls back to the boundary of a region of `Gp`.

Formalized by `StatMech.Ising.DualWalkBoundsRegion`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean, line 593](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean#L593). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#dual-walk-bounds-region).

## Edge crossing from region-bounding dual walks and a walk decomposition

An edge crossing built from dual walks bounding regions.

Formalized by `StatMech.Ising.edgeCrossing_of_boundsRegion`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean, line 628](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean#L628). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#edge-crossing-of-bounds-region).

## Boolean indicator of a set of sites of ℤ²

The indicator of a set of sites of `ℤ²`, as a Boolean function.

Formalized by `StatMech.Ising.latticeSide`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean, line 662](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean#L662). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#lattice-side).

## Edge crossing from region-bounding dual walks, no decomposition needed

An edge crossing built from dual walks bounding regions (variant using
`even_to_cut_of_boundsRegion'`).

Formalized by `StatMech.Ising.edgeCrossing_of_boundsRegion'`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean, line 736](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean#L736). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#edge-crossing-of-bounds-region-2).

## Kramers–Wannier duality

**Kramers–Wannier duality** for a preconnected graph `Gp` and a graph `Gd` whose closed walks
pull back to region boundaries, for `tanh β* = e^{-2β}`.

H. A. Kramers and G. H. Wannier, *Statistics of the two-dimensional ferromagnet. Part I*,
Phys. Rev. 60 (1941).

Formalized by `StatMech.Ising.isingZ_self_dual_of_boundsRegion`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean, line 750](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/KWClosedWalkParity.lean#L750). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html#ising-z-self-dual-of-bounds-region).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kramers–Wannier duality](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/exact-solutions/kramers-wannier-duality)
