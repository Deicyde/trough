---
declaration: section
origin: cited
lean: StatMech.FK.ivTwoPointSup, StatMech.FK.ivTwoPointInf, StatMech.FK.ivTwoPointInf_isLimit, StatMech.FK.boxRestrict, StatMech.FK.isClopen_boxRestrict_preimage, StatMech.FK.measurableSet_boxRestrict_preimage, StatMech.FK.isIncreasing_boxRestrict_preimage, StatMech.FK.boxConnEvent
statement: formalized
proof: formalized
---

# Two-point functions of infinite-volume FK measures

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-functions-of-infinite-volume-fk-measur/index.html).

## A. Monotone limits along chains of measures

## Supremum of the masses of an event along a measure sequence

The supremum over `n` of the masses `μ n A` of an event `A`.

Formalized by `StatMech.FK.ivTwoPointSup`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-functions-of-infinite-volume-fk-measur/index.html#iv-two-point-sup).

## Infimum of the masses of an event along a measure sequence

The infimum over `n` of the masses `μ n A` of an event `A`.

Formalized by `StatMech.FK.ivTwoPointInf`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-functions-of-infinite-volume-fk-measur/index.html#iv-two-point-inf).

## Masses of clopen increasing events converge along decreasing measures

Along a stochastically decreasing sequence of measures, the mass of a clopen increasing event
converges to its infimum.

Formalized by `StatMech.FK.ivTwoPointInf_isLimit`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-functions-of-infinite-volume-fk-measur/index.html#iv-two-point-inf-is-limit).

## Restriction of a configuration of $\mathbb{Z}^d$ to a box

Restriction of a configuration of `ℤ^d` to the edges of the box `Λ_n`.

Formalized by `StatMech.FK.boxRestrict`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-functions-of-infinite-volume-fk-measur/index.html#box-restrict).

## Cylinder events of a box are clopen

Cylinder events of the box `Λ_N` are clopen.

Formalized by `StatMech.FK.isClopen_boxRestrict_preimage`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-functions-of-infinite-volume-fk-measur/index.html#is-clopen-box-restrict-preimage).

## Cylinder events of a box are measurable

Cylinder events of the box `Λ_N` are measurable.

Formalized by `StatMech.FK.measurableSet_boxRestrict_preimage`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-functions-of-infinite-volume-fk-measur/index.html#measurable-set-box-restrict-preimage).

## Box restriction pulls increasing events back to increasing events

The preimage of an increasing event under box restriction is increasing.

Formalized by `StatMech.FK.isIncreasing_boxRestrict_preimage`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-functions-of-infinite-volume-fk-measur/index.html#is-increasing-box-restrict-preimage).

## Event that two sites are joined by open edges inside a box

The event that `x` and `y` are joined by open edges inside the box `Λ_n`.

Formalized by `StatMech.FK.boxConnEvent`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-functions-of-infinite-volume-fk-measur/index.html#box-conn-event).

## Free box measure of a box connection event is the two-point function

The free box measure of the connection event in `Λ_n` is the finite-volume two-point function.

Formalized by `StatMech.FK.freeFiniteMeasure_real_boxConnEvent`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-functions-of-infinite-volume-fk-measur/index.html#free-finite-measure-real-box-conn-event).

## Wired random-cluster probabilities are positive

Every configuration has positive wired random-cluster probability.

Formalized by `StatMech.FK.wiredFkProb_pos`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-functions-of-infinite-volume-fk-measur/index.html#wired-fk-prob-pos).

## Free infinite-volume two-point function in a box

The free infinite-volume two-point function in `Λ_N`: the supremum over `n` of `φ⁰_n(x ↔ y in
Λ_N)`.

Formalized by `StatMech.FK.freeIvTwoPoint`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-functions-of-infinite-volume-fk-measur/index.html#free-iv-two-point).

## Wired infinite-volume two-point function in a box

The wired infinite-volume two-point function in `Λ_N`: the infimum over `n` of `φ¹_n(x ↔ y in
Λ_N)`.

Formalized by `StatMech.FK.wiredIvTwoPoint`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-functions-of-infinite-volume-fk-measur/index.html#wired-iv-two-point).

## Convergence to the free two-point function under stochastic increase

If the free box measures increase stochastically in `n`, then `φ⁰_n(x ↔ y in Λ_N)` converges to
`freeIvTwoPoint`.

Formalized by `StatMech.FK.freeIvTwoPoint_isLimit`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-functions-of-infinite-volume-fk-measur/index.html#free-iv-two-point-is-limit).

## Convergence to the wired two-point function under stochastic decrease

If the wired box measures decrease stochastically in `n`, then `φ¹_n(x ↔ y in Λ_N)` converges to
`wiredIvTwoPoint`.

Formalized by `StatMech.FK.wiredIvTwoPoint_isLimit`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointInfinite.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-functions-of-infinite-volume-fk-measur/index.html#wired-iv-two-point-is-limit).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Two-point functions of infinite-volume FK measures](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-functions-of-infinite-volume-fk-measur/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-functions-of-infinite-volume-fk-measur)
