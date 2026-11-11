---
declaration: section
origin: cited
lean: StatMech.FK.freeFiniteMeasure_fkg, StatMech.FK.ivp_iv_fkg, StatMech.FK.wiredFkProb_FKGLatticeCondition, StatMech.FK.wiredFkProb_positively_associated_events, StatMech.FK.wiredFiniteMeasure_fkg, StatMech.FK.ivp_iv_fkg_wired, StatMech.FK.ivp_iv_monotone
statement: formalized
proof: formalized
---

# FKG inequality and ordering for infinite-volume FK measures at q = 2

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/fkg-inequality-and-ordering-for-infinite-volume/index.html).

## A. The FKG inequality for the free measures

## FKG inequality for free $q = 2$ box measures on smaller-box events

FKG inequality for the free box measure `φ⁰_m` (`q = 2`) on two increasing cylinder events of a
smaller box `Λ_N`, `N ≤ m`.

Formalized by `StatMech.FK.freeFiniteMeasure_fkg`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeFKG.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeFKG.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/fkg-inequality-and-ordering-for-infinite-volume/index.html#free-finite-measure-fkg).

## FKG inequality for the free $q = 2$ infinite-volume measure

FKG inequality for the free infinite-volume measure at `q = 2` on increasing cylinder events of
a box.

Formalized by `StatMech.FK.ivp_iv_fkg`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeFKG.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeFKG.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/fkg-inequality-and-ordering-for-infinite-volume/index.html#ivp-iv-fkg).

## FKG lattice condition for the wired measure when $q \ge 1$

The wired random-cluster measure satisfies the FKG lattice condition when `q ≥ 1`.

Formalized by `StatMech.FK.wiredFkProb_FKGLatticeCondition`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeFKG.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeFKG.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/fkg-inequality-and-ordering-for-infinite-volume/index.html#wired-fk-prob-fkglattice-condition).

## FKG inequality for the wired measure when $q \ge 1$

FKG inequality for the wired random-cluster measure on a finite graph: increasing events are
positively correlated when `q ≥ 1`.

Formalized by `StatMech.FK.wiredFkProb_positively_associated_events`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeFKG.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeFKG.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/fkg-inequality-and-ordering-for-infinite-volume/index.html#wired-fk-prob-positively-associated-even).

## FKG inequality for wired $q = 2$ box measures on smaller-box events

FKG inequality for the wired box measure `φ¹_m` (`q = 2`) on two increasing cylinder events of a
smaller box `Λ_N`, `N ≤ m`.

Formalized by `StatMech.FK.wiredFiniteMeasure_fkg`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeFKG.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeFKG.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/fkg-inequality-and-ordering-for-infinite-volume/index.html#wired-finite-measure-fkg).

## FKG inequality for the wired $q = 2$ infinite-volume measure

FKG inequality for the wired infinite-volume measure at `q = 2` on increasing cylinder events of
a box.

Formalized by `StatMech.FK.ivp_iv_fkg_wired`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeFKG.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeFKG.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/fkg-inequality-and-ordering-for-infinite-volume/index.html#ivp-iv-fkg-wired).

## Wired $q = 2$ measure dominates the free one on increasing cylinders

At `q = 2` the free infinite-volume measure gives every increasing cylinder event at most the
probability the wired one gives it.

Formalized by `StatMech.FK.ivp_iv_monotone`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeFKG.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeFKG.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/fkg-inequality-and-ordering-for-infinite-volume/index.html#ivp-iv-monotone).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: FKG inequality and ordering for infinite-volume FK measures at q = 2](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/fkg-inequality-and-ordering-for-infinite-volume/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/fkg-inequality-and-ordering-for-infinite-volume)
