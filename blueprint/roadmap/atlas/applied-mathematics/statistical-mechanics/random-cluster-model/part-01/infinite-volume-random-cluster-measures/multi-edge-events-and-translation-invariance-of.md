---
declaration: section
origin: cited
lean: StatMech.FK.med_genericMultiOpenEvent, StatMech.FK.med_multiMassProb, StatMech.FK.med_centred_mass_eq, StatMech.FK.med_free_centred_mass_eq, StatMech.FK.med_centred_eq_translated_wired, StatMech.FK.med_centred_eq_translated_free, StatMech.FK.med_centred_tendsto_iv, StatMech.FK.med_free_centred_tendsto_iv
statement: formalized
proof: formalized
---

# Multi-edge events and translation invariance of q = 2 FK measures

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of/index.html).

## A. Multi-edge events

## Event that all edges of a finite set are open

The event `A_t` that every edge of the finite set `t` is open. On box configurations it is
`cdc_boxMultiOpenEvent` (`med_boxMultiOpenEvent_eq`).

Formalized by `StatMech.FK.med_genericMultiOpenEvent`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of/index.html#med-generic-multi-open-event).

## Mass of the all-open event under a weight function

The mass `∑_ω 1_{A_t}(ω) μ(ω)` of the event that every edge of `t` is open, for a weight
function `μ` on a finite configuration space; it is `eventMassProb μ A_t`
(`med_multiMassProb_eq_eventMassProb`).

Formalized by `StatMech.FK.med_multiMassProb`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of/index.html#med-multi-mass-prob).

## Wired box measure of an all-open event equals its box mass

The wired box measure on `Λ_m`, pushed to `ℤ^d`, gives `A_t` the box mass of `t`.

Formalized by `StatMech.FK.med_centred_mass_eq`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of/index.html#med-centred-mass-eq).

## Free box measure of an all-open event equals its box mass

The free box measure on `Λ_m`, pushed to `ℤ^d`, gives `A_t` the box mass of `t`.

Formalized by `StatMech.FK.med_free_centred_mass_eq`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of/index.html#med-free-centred-mass-eq).

## Translation covariance of wired box masses

The wired mass of `t` in `Λ_m` equals the wired mass of `t + v` in `v + Λ_m`.

Formalized by `StatMech.FK.med_centred_eq_translated_wired`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of/index.html#med-centred-eq-translated-wired).

## Translation covariance of free box masses

The free mass of `t` in `Λ_m` equals the free mass of `t + v` in `v + Λ_m`.

Formalized by `StatMech.FK.med_centred_eq_translated_free`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of/index.html#med-centred-eq-translated-free).

## Wired all-open probabilities converge to the infinite-volume value

Restatement of `cdc_wired_multiOpenEvent_tendsto`: the wired box probabilities of `A_t`
converge to the wired infinite-volume probability.

Formalized by `StatMech.FK.med_centred_tendsto_iv`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of/index.html#med-centred-tendsto-iv).

## Free all-open probabilities converge to the infinite-volume value

Restatement of `cdc_free_multiOpenEvent_tendsto`: the free box probabilities of `A_t`
converge to the free infinite-volume probability.

Formalized by `StatMech.FK.med_free_centred_tendsto_iv`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of/index.html#med-free-centred-tendsto-iv).

## Difference of wired all-open masses of an edge set and its translate

The difference between the wired mass of `t` in `Λ_m` and the wired mass of `t + v` in
`v + Λ_m`; it vanishes by translation covariance.

Formalized by `StatMech.FK.med_offCentreMultiCarrier`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of/index.html#med-off-centre-multi-carrier).

## Equal wired probabilities from eventually equal translated masses

If the wired mass of `t + v` in `v + Λ_m` eventually equals the wired mass of `t'` in `Λ_m`,
the wired infinite-volume measure gives `A_t` and `A_{t'}` the same probability.

Formalized by `StatMech.FK.med_wiredMultiHomogeneous_of_cofinal`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of/index.html#med-wired-multi-homogeneous-of-cofinal).

## Equal free probabilities from eventually equal translated masses

If the free mass of `t + v` in `v + Λ_m` eventually equals the free mass of `t'` in `Λ_m`,
the free infinite-volume measure gives `A_t` and `A_{t'}` the same probability.

Formalized by `StatMech.FK.med_freeMultiHomogeneous_of_cofinal`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of/index.html#med-free-multi-homogeneous-of-cofinal).

## Wired placement for a shift via eventually equal box masses

A wired placement for the shift `g`: every finite edge set `s` and its shift `g⁻¹ s` are
images of box edge sets `t`, `t'` of a common box `Λ_N` such that the wired mass of `t + g` in
`g + Λ_m` eventually equals the wired mass of `t'` in `Λ_m`. See also `lmc_wiredPlacement`.

Formalized by `StatMech.FK.med_wiredPlacement`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of/index.html#med-wired-placement).

## Free placement for a shift via eventually equal box masses

A free placement for the shift `g`, defined as `med_wiredPlacement` with free masses.

Formalized by `StatMech.FK.med_freePlacement`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of/index.html#med-free-placement).

## Wired translation invariance from wired placements of every shift

The wired infinite-volume `q = 2` measure is translation invariant if every shift has a wired
placement. See also `flc_wiredIV_isTranslationInvariant`, which proves invariance without
hypotheses.

Formalized by `StatMech.FK.med_wiredIV_isTranslationInvariant_of_placement`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of/index.html#med-wired-iv-is-translation-invariant-of).

## Free translation invariance from free placements of every shift

The free infinite-volume `q = 2` measure is translation invariant if every shift has a free
placement. See also `bdp_freeIV_isTranslationInvariant`, which proves invariance without
hypotheses.

Formalized by `StatMech.FK.med_freeIV_isTranslationInvariant_of_placement`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/MultiEdgeDecay.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of/index.html#med-free-iv-is-translation-invariant-of).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multi-edge events and translation invariance of q = 2 FK measures](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/multi-edge-events-and-translation-invariance-of)
