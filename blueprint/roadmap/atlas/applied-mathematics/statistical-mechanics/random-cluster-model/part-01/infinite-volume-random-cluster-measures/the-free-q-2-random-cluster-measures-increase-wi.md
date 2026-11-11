---
declaration: section
origin: cited
lean: StatMech.FK.inducedWiringFree, StatMech.FK.inducedWiringFree_adj, StatMech.FK.psiFreeGraph_eq_sup, StatMech.FK.fullGraphFree, StatMech.FK.innerGraphFree, StatMech.FK.outsideOpenGraph_le_fullGraphFree, StatMech.FK.innerGraphFree_reachable_of_outsideReachable, StatMech.FK.fullGraphFree_reachable_of_innerGraphFree
statement: formalized
proof: formalized
---

# The free q = 2 random-cluster measures increase with the box

49 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html).

## A. The wiring induced by an outer configuration

## Wiring induced on a box by outer open edges

The boundary wiring on `Λ_n` induced by an outer configuration `ψ` on `Λ_(n+1)`: two distinct
vertices of `Λ_n` are wired when `ψ` connects them by open edges outside `Λ_n`.

Formalized by `StatMech.FK.inducedWiringFree`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#induced-wiring-free).

## Adjacency criterion for the free induced wiring

Unfolding adjacency in the induced wiring.

Formalized by `StatMech.FK.inducedWiringFree_adj`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#induced-wiring-free-adj).

## Glued open graph is the union of inner and outer open edges

The open graph of a glued configuration is the union of the open edges of `Λ_n` and the outer
open edges.

Formalized by `StatMech.FK.psiFreeGraph_eq_sup`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#psi-free-graph-eq-sup).

## Open graph of a glued configuration

The open graph on `Λ_(n+1)` of `ω` on `Λ_n` glued into `ψ`.

Formalized by `StatMech.FK.fullGraphFree`, an abbreviation declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#full-graph-free).

## Inner open graph with the free induced wiring

The open graph of `ω` on `Λ_n` together with the wiring induced by `ψ`.

Formalized by `StatMech.FK.innerGraphFree`, an abbreviation declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#inner-graph-free).

## Outer open graph lies in the glued open graph

The outer open graph is contained in the glued open graph.

Formalized by `StatMech.FK.outsideOpenGraph_le_fullGraphFree`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#outside-open-graph-le-full-graph-free).

## Outer open connections give connections in the inner graph

Vertices of `Λ_n` connected by outer open edges are connected in `innerGraphFree`.

Formalized by `StatMech.FK.innerGraphFree_reachable_of_outsideReachable`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#inner-graph-free-reachable-of-outside-re).

## Inner-graph connections are glued-graph connections

Connections in `innerGraphFree` are connections in the glued open graph.

Formalized by `StatMech.FK.fullGraphFree_reachable_of_innerGraphFree`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#full-graph-free-reachable-of-inner-graph).

## Glued connections between inner vertices are inner-graph connections

Connections in the glued open graph between vertices of `Λ_n` are connections in
`innerGraphFree`.

Formalized by `StatMech.FK.innerGraphFree_reachable_of_fullGraphFree`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#inner-graph-free-reachable-of-full-graph).

## Glued open edges at outer vertices are outer edges

An edge of the glued open graph at a vertex outside `Λ_n` is an outer open edge.

Formalized by `StatMech.FK.fullGraphFree_adj_of_outside`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#full-graph-free-adj-of-outside).

## Outer vertex whose outer open cluster avoids the inner box

A vertex of `Λ_(n+1)` whose outer open cluster contains no vertex of `Λ_n`.

Formalized by `StatMech.FK.OutsideOnlyFree`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#outside-only-free).

## A vertex whose outer cluster avoids the inner box lies outside it

A vertex whose outer cluster avoids `Λ_n` is not in `Λ_n`.

Formalized by `StatMech.FK.outsideOnlyFree_self_not_inner`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#outside-only-free-self-not-inner).

## Avoiding the inner box is constant on outer open clusters

Avoiding `Λ_n` is constant on outer open clusters.

Formalized by `StatMech.FK.outsideOnlyFree_of_reachable`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#outside-only-free-of-reachable).

## Glued connections from an avoiding vertex are outer connections

From a vertex whose outer cluster avoids `Λ_n`, glued connections are outer connections.

Formalized by `StatMech.FK.outsideOpenGraph_reachable_of_fullGraphFree_outsideOnly`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#outside-open-graph-reachable-of-full-gra).

## Outer open cluster avoiding the inner box

An outer open cluster that contains no vertex of `Λ_n`.

Formalized by `StatMech.FK.IsOutsideOnlyFree`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#is-outside-only-free).

## An outer cluster avoids the inner box iff its representative does

An outer cluster avoids `Λ_n` exactly when its representative vertex does.

Formalized by `StatMech.FK.isOutsideOnlyFree_mk`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#is-outside-only-free-mk).

## Outer open clusters avoiding the inner box

The outer open clusters that contain no vertex of `Λ_n`.

Formalized by `StatMech.FK.OutsideOnlyCompFree`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#outside-only-comp-free).

## Cluster map into the glued configuration

The map from clusters of `innerGraphFree` and outer clusters avoiding `Λ_n` to clusters of the
glued configuration.

Formalized by `StatMech.FK.fullComponentMapFree`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#full-component-map-free).

## Cluster map on inner clusters

The cluster map on an inner cluster.

Formalized by `StatMech.FK.fullComponentMapFree_inl_mk`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#full-component-map-free-inl-mk).

## Cluster map on avoiding outer clusters

The cluster map on an outer cluster avoiding `Λ_n`.

Formalized by `StatMech.FK.fullComponentMapFree_inr_mk`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#full-component-map-free-inr-mk).

## Injectivity of the free cluster map

The cluster map is injective.

Formalized by `StatMech.FK.fullComponentMapFree_injective`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#full-component-map-free-injective).

## Surjectivity of the free cluster map

The cluster map is surjective.

Formalized by `StatMech.FK.fullComponentMapFree_surjective`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#full-component-map-free-surjective).

## Cluster decomposition of the glued configuration

Clusters of the glued configuration correspond to clusters of `innerGraphFree` plus outer
clusters avoiding `Λ_n`.

Formalized by `StatMech.FK.fullComponentEquivFree`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#full-component-equiv-free).

## Number of outer open clusters avoiding the inner box

The number of outer open clusters avoiding `Λ_n`.

Formalized by `StatMech.FK.outsideShiftFree`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#outside-shift-free).

## Cluster count of a glued configuration splits additively

The cluster count of a glued configuration is the cluster count of `ω` with the induced wiring
plus the number of outer clusters avoiding `Λ_n`.

Formalized by `StatMech.FK.numClusters_psiExt_free`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#num-clusters-psi-ext-free).

## Outer factor of the weight of a glued configuration

The factor of the random-cluster weight of a glued configuration contributed by the outer
configuration.

Formalized by `StatMech.FK.psiShiftFree`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#psi-shift-free).

## Positivity of the outer weight factor

The outer weight factor is positive.

Formalized by `StatMech.FK.psiShiftFree_pos`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#psi-shift-free-pos).

## Random-cluster weight of a glued configuration factorizes

The random-cluster weight of a glued configuration factors as the outer factor times the weight
of `ω` with the induced wiring.

Formalized by `StatMech.FK.fkWeight_psiExt_free`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#fk-weight-psi-ext-free).

## Conditional partition function in terms of the induced wiring

The conditional partition function given the outer configuration, in terms of the induced-wiring
partition function.

Formalized by `StatMech.FK.inducedFkZ_innerEdgeFinset_psi_free`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#induced-fk-z-inner-edge-finset-psi-free).

## Domain Markov property

Conditionally on the configuration `ψ` outside `Λ_n`, the free
random-cluster measure on `Λ_(n+1)` restricted to `Λ_n` is the random-cluster measure on `Λ_n` with
the wiring induced by `ψ`.

Formalized by `StatMech.FK.condFkProb_psiExt_eq_bcProb_free`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#cond-fk-prob-psi-ext-eq-bc-prob-free).

## Fibre masses of the free measure sum to one

The masses of the conditioning fibres of the free measure on `Λ_(n+1)` sum to `1`.

Formalized by `StatMech.FK.sum_fibreMass_eq_one_free`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#sum-fibre-mass-eq-one-free).

## Fibre-mass factorization of random-cluster probabilities

A random-cluster probability is its fibre mass times its conditional probability.

Formalized by `StatMech.FK.fkProb_eq_fibreMass_mul_condFkProb`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#fk-prob-eq-fibre-mass-mul-cond-fk-prob).

## Conditional free probabilities depend only on the outer configuration

Configurations agreeing off `F` give the same conditional random-cluster probabilities.

Formalized by `StatMech.FK.condFkProb_congr_dom_free`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#cond-fk-prob-congr-dom-free).

## Decomposition of the free measure over the outer configuration

Decomposition of the free measure on `Λ_(n+1)` over the configuration outside `Λ_n`.

Formalized by `StatMech.FK.freeSucc_fkProb_decompose`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 468](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L468). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#free-succ-fk-prob-decompose).

## Conditional free measure as an induced-wiring measure

The conditional free measure of an event of `Λ_n` equals its probability under the
induced-wiring measure.

Formalized by `StatMech.FK.condFkProb_psiExt_sum_eq_inducedBox_free`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 500](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L500). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#cond-fk-prob-psi-ext-sum-eq-induced-box).

## Free measure is dominated by induced-wiring measures for $q \ge 1$

For `q ≥ 1`, the free measure on `Λ_n` gives an increasing event at most its probability under
any induced wiring.

Formalized by `StatMech.FK.fkProb_le_inducedFree`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 526](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L526). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#fk-prob-le-induced-free).

## Conditional free measure dominates the smaller free box for $q \ge 1$

For `q ≥ 1`, conditionally on any outer configuration, the free measure on `Λ_(n+1)` gives an
increasing event of `Λ_n` at least its free `Λ_n` probability.

Formalized by `StatMech.FK.fkProb_le_condFkProb_innerRestrict_free`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 548](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L548). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#fk-prob-le-cond-fk-prob-inner-restrict-f).

## One-step box monotonicity of free measures for $q \ge 1$

For `q ≥ 1`, the free measure on `Λ_(n+1)` gives an increasing event of `Λ_n` at least its free
`Λ_n` probability.

Formalized by `StatMech.FK.freeSucc_fkProb_innerEvent_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 566](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L566). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#free-succ-fk-prob-inner-event-le).

## Free box measure of a cylinder event as a finite sum

The free `Λ_m` measure of a `Λ_m` cylinder event, as a finite sum.

Formalized by `StatMech.FK.freeFiniteMeasure_real_boxRestrictEvent`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 594](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L594). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#free-finite-measure-real-box-restrict-ev).

## Next-box free measure of a cylinder event as a finite sum

The free `Λ_(n+1)` measure of a `Λ_n` cylinder event, as a finite sum.

Formalized by `StatMech.FK.freeFiniteMeasure_succ_real_innerRestrictEvent`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 613](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L613). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#free-finite-measure-succ-real-inner-rest).

## Increasing box events gain free $q = 2$ probability in the next box

For `q = 2`, the free `Λ_n` probability of an increasing `Λ_n` event is at most its free
`Λ_(n+1)` measure.

Formalized by `StatMech.FK.freeFiniteMeasure_smallerBox_le_succ`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 635](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L635). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#free-finite-measure-smaller-box-le-succ).

## One-step growth of free $q = 2$ measures of increasing cylinders

For `q = 2` and `N ≤ m`, the free `Λ_m` measure of an increasing `Λ_N` cylinder event is at most
its free `Λ_(m+1)` measure.

Formalized by `StatMech.FK.fkFreeLimit_le_succ`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 648](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L648). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#fk-free-limit-le-succ).

## Free $q = 2$ box measures of increasing cylinders are monotone

For `q = 2`, the free box measures of an increasing `Λ_N` cylinder event increase with the box.

Formalized by `StatMech.FK.fkFreeLimit_monotone`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 666](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L666). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#fk-free-limit-monotone).

## Limit of free $q = 2$ box measures of a cylinder event

The limit `sup_k φ⁰_{Λ_(N+k)}(S)` of the free `q = 2` box measures of a `Λ_N` cylinder event
`S`.

Formalized by `StatMech.FK.fkFreeLimitValue`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 679](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L679). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#fk-free-limit-value).

## Free box measures are at most one

Free box measures are at most `1`.

Formalized by `StatMech.FK.freeFiniteMeasure_real_le_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 685](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L685). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#free-finite-measure-real-le-one).

## Free $q = 2$ box measures of increasing cylinders converge

For `q = 2`, the free box measures of an increasing `Λ_N` cylinder event converge to
`fkFreeLimitValue`.

Formalized by `StatMech.FK.fk_free_limit_exists`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 694](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L694). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#fk-free-limit-exists).

## Free $q = 2$ box measures are bounded by the limit value

For `q = 2`, every free box measure of a `Λ_N` cylinder event with `N ≤ m` is at most
`fkFreeLimitValue`.

Formalized by `StatMech.FK.fk_free_le_limit`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 713](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L713). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#fk-free-le-limit).

## Free $q = 2$ infinite-volume mass of increasing cylinders as a box limit

For `q = 2`, the free infinite-volume measure of an increasing cylinder event equals
`fkFreeLimitValue`.

Formalized by `StatMech.FK.fkFreeLimit_freeInfiniteVolume_eq`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 727](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L727). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#fk-free-limit-free-infinite-volume-eq).

## Free $q=2$ box masses of increasing cylinders tend to infinite volume

For `q = 2`, the free box measures of an increasing cylinder event converge, along the whole
sequence of boxes, to its free infinite-volume measure.

Formalized by `StatMech.FK.fk_free_infinite_measure`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean, line 740](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/FreeWeakLimit.lean#L740). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html#fk-free-infinite-measure).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The free q = 2 random-cluster measures increase with the box](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-free-q-2-random-cluster-measures-increase-wi)
