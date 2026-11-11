---
declaration: section
origin: cited
lean: StatMech.FK.fkTheta, StatMech.FK.fkSubcriticalSet, StatMech.FK.fkPc
statement: formalized
proof: formalized
---

# The critical point of the random-cluster model

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-critical-point-of-the-random-cluster-model/index.html).

## A. The percolation probability

## Wired random-cluster percolation probability $\theta(p, q)$

The percolation probability `θ(p, q) = φ^1_{p,q}(0 ↔ ∞)` of the wired infinite-volume
random-cluster measure on `ℤ^d`.

Formalized by `StatMech.FK.fkTheta`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/CriticalPoint.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/CriticalPoint.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-critical-point-of-the-random-cluster-model/index.html#fk-theta).

## Non-percolating parameters of the wired random-cluster measure

The parameters `p ∈ (0, 1)` at which the wired measure does not percolate (`θ(p, q) = 0`).

Formalized by `StatMech.FK.fkSubcriticalSet`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/CriticalPoint.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/CriticalPoint.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-critical-point-of-the-random-cluster-model/index.html#fk-subcritical-set).

## Critical parameter $p_c(q)$ of the random-cluster model

The critical parameter `p_c(q) = sup {p ∈ (0, 1) : θ(p, q) = 0}` of the random-cluster model on
`ℤ^d` (equal to `0` when the set is empty, e.g. for `q ≤ 0`).

Formalized by `StatMech.FK.fkPc`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/CriticalPoint.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/CriticalPoint.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-critical-point-of-the-random-cluster-model/index.html#fk-pc).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The critical point of the random-cluster model](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-critical-point-of-the-random-cluster-model/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-critical-point-of-the-random-cluster-model)
