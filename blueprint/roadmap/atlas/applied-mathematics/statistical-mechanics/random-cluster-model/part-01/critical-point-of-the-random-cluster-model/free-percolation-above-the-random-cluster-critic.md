---
declaration: section
origin: cited
lean: StatMech.FK.frp_fkTheta_pos_of_gt_fkPc, StatMech.FK.frp_measurableSet_percolationEvent, StatMech.FK.frp_isIncreasing_percolationEvent, StatMech.FK.frp_free_percolation_above_pc, StatMech.FK.frp_free_percolation_above_pc_of_countable_agreement
statement: formalized
proof: formalized
---

# Free percolation above the random-cluster critical point

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/free-percolation-above-the-random-cluster-critic/index.html).

## A. Wired percolation above the critical point

## Wired percolation above the random-cluster critical point

Above the critical point the wired measure percolates: `θ¹(p, q) > 0` for `p > p_c(q, d)`.

Formalized by `StatMech.FK.frp_fkTheta_pos_of_gt_fkPc`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreePercolationAbovePc.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FreePercolationAbovePc.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/free-percolation-above-the-random-cluster-critic/index.html#frp-fk-theta-pos-of-gt-fk-pc).

## Measurability of the percolation event

The percolation event is measurable.

Formalized by `StatMech.FK.frp_measurableSet_percolationEvent`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreePercolationAbovePc.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FreePercolationAbovePc.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/free-percolation-above-the-random-cluster-critic/index.html#frp-measurable-set-percolation-event).

## The percolation event is increasing

The percolation event is increasing.

Formalized by `StatMech.FK.frp_isIncreasing_percolationEvent`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreePercolationAbovePc.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FreePercolationAbovePc.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/free-percolation-above-the-random-cluster-critic/index.html#frp-is-increasing-percolation-event).

## Free percolation from domination and free–wired agreement at $p'$

If `p_c < p'`, the free measure at `p'` is dominated by the free measure at `p`, and `θ⁰(p', q)
= θ¹(p', q)`, then `θ⁰(p, q) > 0`.

Formalized by `StatMech.FK.frp_free_percolation_above_pc`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreePercolationAbovePc.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FreePercolationAbovePc.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/free-percolation-above-the-random-cluster-critic/index.html#frp-free-percolation-above-pc).

## Free percolation above $p_c$ from monotonicity and countable agreement

For `p > p_c(q, d)`, the free measure percolates, `θ⁰(p, q) > 0`, assuming monotonicity of the
free measures in `p` on `(p_c, p)` (`hmono`) and `θ⁰ = θ¹` off a countable set (`hagree`).

Formalized by `StatMech.FK.frp_free_percolation_above_pc_of_countable_agreement`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreePercolationAbovePc.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FreePercolationAbovePc.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/free-percolation-above-the-random-cluster-critic/index.html#frp-free-percolation-above-pc-of-countab).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Free percolation above the random-cluster critical point](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/free-percolation-above-the-random-cluster-critic/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/free-percolation-above-the-random-cluster-critic)
