---
declaration: section
origin: cited
lean: StatMech.FK.occ_translated_tendsto_wiredDensity, StatMech.FK.occ_translated_between_iv, StatMech.FK.occ_free_eq_wired_off_countable, StatMech.FK.occ_offCentreCarrier_eq_zero, StatMech.FK.occ_offCentreCarrier, StatMech.FK.occ_wired_density_eq_of_translation_cofinal
statement: formalized
proof: formalized
---

# The off-centre carrier for wired q = 2 FK marginals

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-off-centre-carrier-for-wired-q-2-fk-marginal/index.html).

## A. Translated wired marginals

## Translated wired marginals converge to the wired density

The wired marginals of the translated edge `e + v` in `v + Λ_{N+k}` converge to the wired
`q = 2` density of `e`.

Formalized by `StatMech.FK.occ_translated_tendsto_wiredDensity`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreCarrier.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreCarrier.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-off-centre-carrier-for-wired-q-2-fk-marginal/index.html#occ-translated-tendsto-wired-density).

## Free density is at most each translated wired marginal

The free `q = 2` density of `e` is at most the wired marginal of `e + v` in `v + Λ_{N+k}`.

Formalized by `StatMech.FK.occ_translated_between_iv`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreCarrier.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreCarrier.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-off-centre-carrier-for-wired-q-2-fk-marginal/index.html#occ-translated-between-iv).

## Secant bound gives free–wired density agreement off a countable set

Under the secant comparison `wired(p') ≤ free(p)` for `p' < p`, the free and wired densities
of a box edge agree for all `p ∈ (0, 1)` outside a countable set, namely the discontinuities of
the monotone wired density.

Formalized by `StatMech.FK.occ_free_eq_wired_off_countable`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreCarrier.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreCarrier.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-off-centre-carrier-for-wired-q-2-fk-marginal/index.html#occ-free-eq-wired-off-countable).

## Off-centre carrier vanishes by translation covariance

The off-centre carrier vanishes for every `k`, by translation covariance of the wired box
measures.

Formalized by `StatMech.FK.occ_offCentreCarrier_eq_zero`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreCarrier.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreCarrier.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-off-centre-carrier-for-wired-q-2-fk-marginal/index.html#occ-off-centre-carrier-eq-zero).

## Off-centre carrier tends to zero

The off-centre carrier tends to zero, for every `p`.

Formalized by `StatMech.FK.occ_offCentreCarrier`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreCarrier.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreCarrier.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-off-centre-carrier-for-wired-q-2-fk-marginal/index.html#occ-off-centre-carrier).

## Equal wired densities from equal translated marginals

If for every `k` the wired marginal of `e' + v` in `v + Λ_{N+k}` equals the wired marginal of
`e` in `Λ_{N+k}`, then `e` and `e'` have the same wired density.

Formalized by `StatMech.FK.occ_wired_density_eq_of_translation_cofinal`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreCarrier.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreCarrier.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-off-centre-carrier-for-wired-q-2-fk-marginal/index.html#occ-wired-density-eq-of-translation-cofi).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The off-centre carrier for wired q = 2 FK marginals](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-off-centre-carrier-for-wired-q-2-fk-marginal/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-off-centre-carrier-for-wired-q-2-fk-marginal)
