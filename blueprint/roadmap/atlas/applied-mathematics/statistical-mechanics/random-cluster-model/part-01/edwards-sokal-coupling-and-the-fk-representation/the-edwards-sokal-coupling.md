---
declaration: section
origin: cited
lean: StatMech.FK.esEdgeFactor, StatMech.FK.esWeight, StatMech.FK.ConstOnOpen, StatMech.FK.constOnOpenEquiv, StatMech.FK.card_constOnOpen, StatMech.FK.esWeight_sum, StatMech.FK.esCoeff, StatMech.FK.esFirstConst
statement: formalized
proof: formalized
---

# The Edwards–Sokal coupling

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling/index.html).

## A. The joint weight

## Edwards–Sokal edge factor

The Edwards–Sokal factor of an edge `e`: `1 - p` if `e` is closed in `ω`, and `p` times the
indicator that `σ` agrees at the endpoints if `e` is open.

Formalized by `StatMech.FK.esEdgeFactor`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling/index.html#es-edge-factor).

## Edwards–Sokal joint weight

The Edwards–Sokal joint weight of a spin configuration `σ` and a bond configuration `ω`: the
product of `esEdgeFactor` over the edges of `G`.

Formalized by `StatMech.FK.esWeight`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling/index.html#es-weight).

## Spin configuration constant on open clusters

`σ` is constant on every open edge of `ω`, i.e. on every open cluster.

Formalized by `StatMech.FK.ConstOnOpen`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling/index.html#const-on-open).

## Cluster-constant colorings as colorings of clusters

Colorings constant on open clusters correspond to colorings of the connected components of the
open subgraph.

Formalized by `StatMech.FK.constOnOpenEquiv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling/index.html#const-on-open-equiv).

## There are $q^{k(\omega)}$ colorings constant on the open clusters

There are `q ^ k(ω)` colorings constant on the open clusters, where `k(ω)` is the number of
clusters.

Formalized by `StatMech.FK.card_constOnOpen`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling/index.html#card-const-on-open).

## Edwards–Sokal weight summed over spins is the random-cluster weight

Spin marginal of the Edwards–Sokal weight: summing over spins gives the random-cluster weight
`p^{o(ω)} (1 - p)^{c(ω)} q^{k(ω)}`.

Formalized by `StatMech.FK.esWeight_sum`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling/index.html#es-weight-sum).

## Edwards–Sokal factor of an arbitrary coordinate and state

The Edwards–Sokal factor of an edge `e` written for an arbitrary pair `(e, b)` with `b` the
state
of `e`; edges outside `G` get factor `1`.

Formalized by `StatMech.FK.esCoeff`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling/index.html#es-coeff).

## Normalizing constant relating the bond sum to the Potts weight

The normalizing constant `e^{-βJ |E(G)|}` relating the bond marginal to the Potts weight.

Formalized by `StatMech.FK.esFirstConst`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling/index.html#es-first-const).

## Edwards–Sokal bond sum is a multiple of the Potts weight

Bond marginal of the Edwards–Sokal weight: with `p = 1 - e^{-βJ}`, summing over bond
configurations gives `e^{-βJ |E|}` times the Potts weight of `σ`.

Formalized by `StatMech.FK.esWeight_sum_eq_pottsWeight`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling/index.html#es-weight-sum-eq-potts-weight).

## Edwards–Sokal partition function

The Edwards–Sokal partition function: the total joint weight.

Formalized by `StatMech.FK.esZ`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling/index.html#es-z).

## Bond marginal of the Edwards–Sokal measure

The bond marginal of the normalized Edwards–Sokal measure.

Formalized by `StatMech.FK.esSecondMarginal`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling/index.html#es-second-marginal).

## Spin marginal of the Edwards–Sokal measure

The spin marginal of the normalized Edwards–Sokal measure.

Formalized by `StatMech.FK.esFirstMarginal`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling/index.html#es-first-marginal).

## Edwards–Sokal bond marginal is the random-cluster measure

The bond marginal of the Edwards–Sokal measure is the random-cluster measure with parameters
`(1 - e^{-βJ}, q)`.

Formalized by `StatMech.FK.edwardsSokal_secondMarginal`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling/index.html#edwards-sokal-second-marginal).

## Edwards–Sokal spin marginal is the Potts measure

The spin marginal of the Edwards–Sokal measure is the `q`-state Potts measure at inverse
temperature `β` and coupling `J`.

Formalized by `StatMech.FK.edwardsSokal_firstMarginal`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EdwardsSokal.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling/index.html#edwards-sokal-first-marginal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The Edwards–Sokal coupling](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling)
