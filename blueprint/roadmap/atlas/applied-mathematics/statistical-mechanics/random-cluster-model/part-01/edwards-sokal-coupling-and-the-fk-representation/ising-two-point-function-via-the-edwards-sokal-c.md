---
declaration: section
origin: cited
lean: StatMech.FK.isingSpin, StatMech.FK.Connected, StatMech.FK.connProb, StatMech.FK.eqFunEquiv, StatMech.FK.constEqEquiv, StatMech.FK.esTwoPoint, StatMech.FK.esTwoPoint_eq_connProb
statement: formalized
proof: formalized
---

# Ising two-point function via the Edwards–Sokal coupling

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/ising-two-point-function-via-the-edwards-sokal-c/index.html).

## A. Spins, connection events, and connection probabilities

## Ising spin value of a two-state color

The Ising spin value of a two-state color: `0 ↦ -1`, `1 ↦ 1`.

Formalized by `StatMech.FK.isingSpin`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EsCorrelations.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EsCorrelations.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/ising-two-point-function-via-the-edwards-sokal-c/index.html#ising-spin).

## Open connection between two vertices

`x` and `y` are joined by a path of open edges of `ω` in `G` (`x ↔ y`).

Formalized by `StatMech.FK.Connected`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EsCorrelations.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EsCorrelations.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/ising-two-point-function-via-the-edwards-sokal-c/index.html#connected).

## Random-cluster connection probability

The random-cluster connection probability `φ_{G,p,q}(x ↔ y)`.

Formalized by `StatMech.FK.connProb`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EsCorrelations.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EsCorrelations.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/ising-two-point-function-via-the-edwards-sokal-c/index.html#conn-prob).

## Functions equal at two points as functions omitting one point

For `a ≠ b`, functions `C → Fin q` with `f a = f b` correspond to functions on `C \ {b}`.

Formalized by `StatMech.FK.eqFunEquiv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EsCorrelations.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EsCorrelations.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/ising-two-point-function-via-the-edwards-sokal-c/index.html#eq-fun-equiv).

## Correspondence for cluster-constant colorings equal at two vertices

Colorings constant on open clusters with `σ x = σ y` correspond to colorings of the clusters
that agree on the clusters of `x` and `y`.

Formalized by `StatMech.FK.constEqEquiv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EsCorrelations.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EsCorrelations.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/ising-two-point-function-via-the-edwards-sokal-c/index.html#const-eq-equiv).

## Ising two-point function from the Edwards–Sokal coupling

The Ising two-point function `⟨σ_x σ_y⟩` at bond parameter `p`, computed as the
Edwards–Sokal spin marginal.

Formalized by `StatMech.FK.esTwoPoint`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EsCorrelations.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EsCorrelations.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/ising-two-point-function-via-the-edwards-sokal-c/index.html#es-two-point).

## Ising two-point function equals the $q = 2$ connection probability

The Ising two-point function equals the random-cluster connection probability with `q = 2`:
`⟨σ_x σ_y⟩ = φ_{p,2}(x ↔ y)` (Edwards–Sokal 1988; Grimmett, *The Random-Cluster Model*, 2006,
Theorem 1.16).

Formalized by `StatMech.FK.esTwoPoint_eq_connProb`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EsCorrelations.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/EsCorrelations.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/ising-two-point-function-via-the-edwards-sokal-c/index.html#es-two-point-eq-conn-prob).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ising two-point function via the Edwards–Sokal coupling](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/ising-two-point-function-via-the-edwards-sokal-c/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/ising-two-point-function-via-the-edwards-sokal-c)
