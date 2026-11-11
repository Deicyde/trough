---
declaration: section
origin: cited
lean: StatMech.BeffaraDC.fkPc_eq_selfDualPoint, StatMech.BeffaraDC.beffaraDC_critical_point
statement: formalized
proof: formalized
---

# The critical point of the planar random-cluster model equals the self-dual point

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-critical-point-of-the-planar-random-cluster/index.html).

## $p_c(q)$ equals the self-dual point if percolation starts there, $q \ge 1$

If `θ(r, q) = 0` for `r < p_sd(q)` and `θ(r, q) > 0` for `r > p_sd(q)`, then
`p_c(q) = p_sd(q)`.

Formalized by `StatMech.BeffaraDC.fkPc_eq_selfDualPoint`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/CriticalPoint/SelfDualCritical.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/CriticalPoint/SelfDualCritical.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-critical-point-of-the-planar-random-cluster/index.html#fk-pc-eq-self-dual-point).

## Beffara–Duminil-Copin theorem, conditional form

For `q ≥ 1`, if the wired random-cluster
measure on `ℤ²` does not percolate for `p < √q / (1 + √q)` (`hNoPercBelow`) and percolates for
`p > √q / (1 + √q)` (`hPercAbove`), then `p_c(q) = √q / (1 + √q)`.

The two hypotheses are the content of the Beffara–Duminil-Copin theorem; this statement only identifies the supremum defining `p_c(q)` once they hold. They are true for
every `q ≥ 1`, so the statement is not vacuous.
(V. Beffara and H. Duminil-Copin, *The self-dual point of the two-dimensional random-cluster
model is critical for q ≥ 1*, Probab. Theory Related Fields 153, 2012.)

Formalized by `StatMech.BeffaraDC.beffaraDC_critical_point`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/CriticalPoint/SelfDualCritical.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/CriticalPoint/SelfDualCritical.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-critical-point-of-the-planar-random-cluster/index.html#beffara-dc-critical-point).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The critical point of the planar random-cluster model equals the self-dual point](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-critical-point-of-the-planar-random-cluster/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-critical-point-of-the-planar-random-cluster)
