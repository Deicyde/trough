---
declaration: section
origin: cited
lean: StatMech.FK.iInter_crossingEvent_eq_percolationEvent, StatMech.FK.fkBoundaryConnReal, StatMech.FK.fkBoundaryConnReal_tendsto_fkTheta
statement: formalized
proof: formalized
---

# The FK percolation probability as a limit of crossing probabilities

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-fk-percolation-probability-as-a-limit-of-cro/index.html).

## A. Crossing events

## Crossing events intersect to the percolation event

The crossing events intersect to the percolation event. See also
`Percolation.percolationEvent_eq_iInter` (`Sharpness`), the same fact indexed from `n + 1`.

Formalized by `StatMech.FK.iInter_crossingEvent_eq_percolationEvent`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TailLimit.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/TailLimit.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-fk-percolation-probability-as-a-limit-of-cro/index.html#i-inter-crossing-event-eq-percolation-ev).

## Wired probability that the origin connects to the outside of a box

The probability, under the chosen wired infinite-volume measure, that the origin is connected to
the complement of `Λ_(n-1)`.

Formalized by `StatMech.FK.fkBoundaryConnReal`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TailLimit.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/TailLimit.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-fk-percolation-probability-as-a-limit-of-cro/index.html#fk-boundary-conn-real).

## Wired crossing probabilities converge to the percolation probability

The crossing probabilities of the wired infinite-volume measure converge to the percolation
probability `fkTheta`.

Formalized by `StatMech.FK.fkBoundaryConnReal_tendsto_fkTheta`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TailLimit.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/TailLimit.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-fk-percolation-probability-as-a-limit-of-cro/index.html#fk-boundary-conn-real-tendsto-fk-theta).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The FK percolation probability as a limit of crossing probabilities](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-fk-percolation-probability-as-a-limit-of-cro/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-fk-percolation-probability-as-a-limit-of-cro)
