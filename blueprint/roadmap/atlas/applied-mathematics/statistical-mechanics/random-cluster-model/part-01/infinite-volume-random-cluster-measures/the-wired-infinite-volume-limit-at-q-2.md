---
declaration: section
origin: cited
lean: StatMech.FK.fkWiredLimit_succ_le, StatMech.FK.fkWiredLimitValue, StatMech.FK.fk_wired_limit_exists, StatMech.FK.fkWiredLimit_wiredInfiniteVolume_eq, StatMech.FK.fk_wired_infinite_measure
statement: formalized
proof: formalized
---

# The wired infinite-volume limit at q = 2

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-infinite-volume-limit-at-q-2/index.html).

## A. Monotonicity in the volume

## Wired $q = 2$ increasing-event probabilities do not grow with the box

At `q = 2`, enlarging the wired box from `Λ_m` to `Λ_(m+1)` does not increase the probability of
an increasing cylinder event of `Λ_N`, `N ≤ m`.

Formalized by `StatMech.FK.fkWiredLimit_succ_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MonotoneWeakLimit.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MonotoneWeakLimit.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-infinite-volume-limit-at-q-2/index.html#fk-wired-limit-succ-le).

## Infimum of wired box probabilities of a box event

The infimum over `k` of `φ¹_(N+k)(S)` for an event `S` of the box `Λ_N`, at `q = 2`.

Formalized by `StatMech.FK.fkWiredLimitValue`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MonotoneWeakLimit.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MonotoneWeakLimit.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-infinite-volume-limit-at-q-2/index.html#fk-wired-limit-value).

## Wired box probabilities of increasing cylinder events converge

At `q = 2` the wired box probabilities of an increasing cylinder event converge to
`fkWiredLimitValue`.

Formalized by `StatMech.FK.fk_wired_limit_exists`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MonotoneWeakLimit.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MonotoneWeakLimit.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-infinite-volume-limit-at-q-2/index.html#fk-wired-limit-exists).

## Wired infinite-volume probability equals the infimum over boxes

At `q = 2` the chosen wired infinite-volume measure gives an increasing cylinder event the value
`fkWiredLimitValue`.

Formalized by `StatMech.FK.fkWiredLimit_wiredInfiniteVolume_eq`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MonotoneWeakLimit.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MonotoneWeakLimit.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-infinite-volume-limit-at-q-2/index.html#fk-wired-limit-wired-infinite-volume-eq).

## Wired infinite-volume measure as limit on increasing cylinder events

Existence of the wired infinite-volume random-cluster measure as the limit of wired box
measures, on increasing cylinder events at `q = 2`: `φ¹_m(S) → φ¹(S)` as `m → ∞`. The general
statement (all `q ≥ 1`, weak convergence) is in Grimmett, *The Random-Cluster Model* (2006), Chapter
4.

Formalized by `StatMech.FK.fk_wired_infinite_measure`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MonotoneWeakLimit.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MonotoneWeakLimit.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-infinite-volume-limit-at-q-2/index.html#fk-wired-infinite-measure).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The wired infinite-volume limit at q = 2](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-infinite-volume-limit-at-q-2/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-infinite-volume-limit-at-q-2)
