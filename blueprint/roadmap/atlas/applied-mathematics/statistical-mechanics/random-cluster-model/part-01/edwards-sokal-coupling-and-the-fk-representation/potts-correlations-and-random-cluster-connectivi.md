---
declaration: section
origin: cited
lean: StatMech.FK.pottsAgreeProb, StatMech.FK.edwards_sokal_correlation, StatMech.FK.edwards_sokal_correlation', StatMech.FK.pottsAgreeProb_ge
statement: formalized
proof: formalized
---

# Potts correlations and random-cluster connectivity

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/potts-correlations-and-random-cluster-connectivi/index.html).

## Potts two-point agreement probability

The Potts two-point agreement probability `μ_{G,β,J,q}(σ_x = σ_y)`.

Formalized by `StatMech.FK.pottsAgreeProb`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PottsCorrelation.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PottsCorrelation.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/potts-correlations-and-random-cluster-connectivi/index.html#potts-agree-prob).

## Edwards–Sokal correlation identity

For the `q`-state Potts model on a finite graph with
`p = 1 - e^{-βJ} ∈ (0, 1)`,
`μ_{β,J,q}(σ_x = σ_y) - 1/q = (1 - 1/q) φ_{p,q}(x ↔ y)`.
The hypothesis `hp1` holds for every real `βJ` and `hq` follows from `[NeZero q]`; the only
restriction is `hp`, i.e. `βJ > 0` (ferromagnetic).
(Edwards–Sokal, Phys. Rev. D 38, 1988; Grimmett, *The Random-Cluster Model*, 2006, Theorem
1.16.)

Formalized by `StatMech.FK.edwards_sokal_correlation`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PottsCorrelation.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PottsCorrelation.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/potts-correlations-and-random-cluster-connectivi/index.html#edwards-sokal-correlation).

## Edwards–Sokal correlation identity in $(q-1)/q$ form

The Edwards–Sokal correlation identity with the prefactor written as `(q - 1)/q`.

Formalized by `StatMech.FK.edwards_sokal_correlation'`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PottsCorrelation.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PottsCorrelation.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/potts-correlations-and-random-cluster-connectivi/index.html#edwards-sokal-correlation-2).

## Potts two-point agreement at least $1/q$ for $q \ge 2$, $\beta J > 0$

For `q ≥ 2` and `βJ > 0`, two Potts spins agree with probability at least `1/q`.

Formalized by `StatMech.FK.pottsAgreeProb_ge`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PottsCorrelation.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PottsCorrelation.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/potts-correlations-and-random-cluster-connectivi/index.html#potts-agree-prob-ge).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Potts correlations and random-cluster connectivity](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/potts-correlations-and-random-cluster-connectivi/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/potts-correlations-and-random-cluster-connectivi)
