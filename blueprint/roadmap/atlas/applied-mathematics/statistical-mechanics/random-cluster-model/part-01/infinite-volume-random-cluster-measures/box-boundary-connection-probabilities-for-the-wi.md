---
declaration: section
origin: cited
lean: StatMech.FK.boxBdryConnEvent, StatMech.FK.boxBoundaryConnProfile_tendsto_of_diag
statement: formalized
proof: formalized
---

# Box-boundary connection probabilities for the wired q = 2 measure

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/box-boundary-connection-probabilities-for-the-wi/index.html).

## A. The box-boundary connection event

## Event that the box origin connects to the box boundary

The event that the origin of the box `Λ_n` is connected to the boundary `∂Λ_n` by open edges of
`Λ_n`.

Formalized by `StatMech.FK.boxBdryConnEvent`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxTailLimit.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxTailLimit.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/box-boundary-connection-probabilities-for-the-wi/index.html#box-bdry-conn-event).

## Box-boundary profile tends to $\theta(p,2)$ if wired probabilities do

If the wired `q = 2` probabilities of `{0 ↔ ∂Λ_n}` converge to `θ(p, 2)`, then so does the
Ising
box-boundary connection profile.

Formalized by `StatMech.FK.boxBoundaryConnProfile_tendsto_of_diag`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxTailLimit.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxTailLimit.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/box-boundary-connection-probabilities-for-the-wi/index.html#box-boundary-conn-profile-tendsto-of-dia).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Box-boundary connection probabilities for the wired q = 2 measure](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/box-boundary-connection-probabilities-for-the-wi/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/box-boundary-connection-probabilities-for-the-wi)
