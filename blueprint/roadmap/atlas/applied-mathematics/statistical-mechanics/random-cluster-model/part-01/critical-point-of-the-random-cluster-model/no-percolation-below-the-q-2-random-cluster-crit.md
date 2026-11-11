---
declaration: section
origin: cited
lean: StatMech.FK.tzp_fkTheta_iv_monotone_boxBdry, StatMech.FK.tzp_fkTheta_monotone_in_p, StatMech.FK.tzp_fkTheta_eq_zero_of_lt_pc, StatMech.FK.tzp_fkTheta_eq_zero_of_le_pc_of_pc
statement: formalized
proof: formalized
---

# No percolation below the q = 2 random-cluster critical point

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/no-percolation-below-the-q-2-random-cluster-crit/index.html).

## A. Monotonicity of the percolation probability in `p`

## Wired box-boundary connection probability is monotone in $p$ at $q = 2$

For `q = 2`, the wired infinite-volume probability that the origin is connected to the boundary
of the box of radius `n` is monotone in `p`.

Formalized by `StatMech.FK.tzp_fkTheta_iv_monotone_boxBdry`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ThetaZeroBelowPc.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/ThetaZeroBelowPc.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/no-percolation-below-the-q-2-random-cluster-crit/index.html#tzp-fk-theta-iv-monotone-box-bdry).

## Monotonicity of $\theta^1(p, 2)$ in $p$

For `q = 2`, the wired percolation probability `θ¹(p, 2)` is monotone in `p`.

Formalized by `StatMech.FK.tzp_fkTheta_monotone_in_p`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ThetaZeroBelowPc.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/ThetaZeroBelowPc.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/no-percolation-below-the-q-2-random-cluster-crit/index.html#tzp-fk-theta-monotone-in-p).

## No percolation below the critical point at $q = 2$

For `q = 2`, there is no percolation below the critical point: `θ¹(p, 2) = 0` for `p < p_c(2,
d)`.

Formalized by `StatMech.FK.tzp_fkTheta_eq_zero_of_lt_pc`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ThetaZeroBelowPc.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/ThetaZeroBelowPc.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/no-percolation-below-the-q-2-random-cluster-crit/index.html#tzp-fk-theta-eq-zero-of-lt-pc).

## No percolation for $p \le p_c$ at $q = 2$, given $\theta^1(p_c, 2) = 0$

For `q = 2`, if `θ¹(p_c, 2) = 0`, then `θ¹(p, 2) = 0` for
every `p ≤ p_c(2, d)`.

Formalized by `StatMech.FK.tzp_fkTheta_eq_zero_of_le_pc_of_pc`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ThetaZeroBelowPc.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/ThetaZeroBelowPc.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/no-percolation-below-the-q-2-random-cluster-crit/index.html#tzp-fk-theta-eq-zero-of-le-pc-of-pc).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: No percolation below the q = 2 random-cluster critical point](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/no-percolation-below-the-q-2-random-cluster-crit/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/no-percolation-below-the-q-2-random-cluster-crit)
