---
declaration: section
origin: cited
lean: StatMech.BeffaraDC.dualParam, StatMech.BeffaraDC.selfDualPoint
statement: formalized
proof: formalized
---

# The self-dual point of the planar random-cluster model

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-self-dual-point-of-the-planar-random-cluster/index.html).

## Planar dual parameter $p^{\ast}$

The planar dual parameter `p* = (1 - p) q / ((1 - p) q + p)`, characterized by
`p* p / ((1 - p*)(1 - p)) = q`.

Formalized by `StatMech.BeffaraDC.dualParam`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/CriticalPoint/SelfDualValue.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/CriticalPoint/SelfDualValue.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-self-dual-point-of-the-planar-random-cluster/index.html#dual-param).

## Self-dual point $p_{sd}(q) = \sqrt q/(1 + \sqrt q)$

The self-dual point `p_sd(q) = √q / (1 + √q)`.

Formalized by `StatMech.BeffaraDC.selfDualPoint`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/CriticalPoint/SelfDualValue.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/CriticalPoint/SelfDualValue.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-self-dual-point-of-the-planar-random-cluster/index.html#self-dual-point).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The self-dual point of the planar random-cluster model](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-self-dual-point-of-the-planar-random-cluster/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/the-self-dual-point-of-the-planar-random-cluster)
