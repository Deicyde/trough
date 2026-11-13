---
declaration: section
origin: cited
lean: StatMech.ConfigSpace.aeconst_of_ae_invariant, StatMech.FK.fmc_SelfMixing, StatMech.FK.fmc_exists_cylinder_symmDiff_lt, StatMech.FK.fmc_isErgodic_of_selfMixing, StatMech.FK.fmu_multiOpen, StatMech.FK.fmu_xR, StatMech.FK.fmu_moInd, StatMech.FK.fmu_traceInd
statement: formalized
proof: formalized
---

# Translation invariance and ergodicity of the q = 2 random-cluster measures

116 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html).

## Almost-invariant events are trivial under an ergodic measure

Under an ergodic measure, a measurable set invariant up to null sets has measure `0` or `1`.
See also Mathlib's `aeconst_of_forall_preimage_smul_ae_eq` for `ErgodicSMul`.

Formalized by `StatMech.ConfigSpace.aeconst_of_ae_invariant`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicIsExtreme.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicIsExtreme.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#aeconst-of-ae-invariant).

## Self-mixing on cylinder events

For every cylinder event `A` and `ε > 0` there is a translation `g` with
`|μ(A ∩ g⁻¹A) - μ(A)²| < ε`.

Formalized by `StatMech.FK.fmc_SelfMixing`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfMixing.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfMixing.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fmc-self-mixing).

## Cylinder approximation of events under a finite measure

Every measurable event is approximated by a cylinder event in symmetric difference; the general
form of `exists_cylinder_symmDiff_lt` (`Ergodicity`).

Formalized by `StatMech.FK.fmc_exists_cylinder_symmDiff_lt`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfMixing.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfMixing.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fmc-exists-cylinder-symm-diff-lt).

## Translation-invariant self-mixing measures are ergodic

A translation-invariant self-mixing probability measure is ergodic.

Formalized by `StatMech.FK.fmc_isErgodic_of_selfMixing`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfMixing.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfMixing.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fmc-is-ergodic-of-self-mixing).

## Event that every coordinate of a finite set is open

The event `O_T` that every coordinate in `T` is open. See also `cdc_multiOpenEvent` and
`med_genericMultiOpenEvent`.

Formalized by `StatMech.FK.fmu_multiOpen`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfUpperDecay.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfUpperDecay.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fmu-multi-open).

## Coordinate state as a real number

The state of coordinate `e` as a real number in `{0, 1}`.

Formalized by `StatMech.FK.fmu_xR`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfUpperDecay.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfUpperDecay.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fmu-x-r).

## Product indicator of a multi-open event

The indicator of `O_T` as the product `∏_{e ∈ T} ω(e)`.

Formalized by `StatMech.FK.fmu_moInd`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfUpperDecay.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfUpperDecay.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fmu-mo-ind).

## Indicator of agreeing with a pattern on a finite set

The indicator that `ω` agrees with `τ` on `F`.

Formalized by `StatMech.FK.fmu_traceInd`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfUpperDecay.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfUpperDecay.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fmu-trace-ind).

## Inclusion–exclusion coefficient of a multi-open event

The inclusion–exclusion coefficient of `O_T` in the expansion of the trace indicator of `τ` on
`F`.

Formalized by `StatMech.FK.fmu_traceCoef`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfUpperDecay.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfUpperDecay.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fmu-trace-coef).

## Pair mixing of multi-open events

For every finite family of finite sets `T` and `δ > 0` there is one translation `g` with
`|μ(O_T ∩ g⁻¹O_{T'}) - μ(O_T) μ(O_{T'})| < δ` for all `T, T'` in the family.

Formalized by `StatMech.FK.fmu_PairMixing`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfUpperDecay.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfUpperDecay.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fmu-pair-mixing).

## Mixing for finite families of cylinder events

The analogue of `fmu_PairMixing` for finite families of cylinder events.

Formalized by `StatMech.FK.fmu_GenMixing`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfUpperDecay.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfUpperDecay.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fmu-gen-mixing).

## Upper decay of correlations of multi-open events

The one-sided form of `fmu_PairMixing`: `μ(O_T ∩ g⁻¹O_{T'}) ≤ μ(O_T) μ(O_{T'}) + δ`.

Formalized by `StatMech.FK.fmu_UpperDecay`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfUpperDecay.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/ErgodicOfUpperDecay.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fmu-upper-decay).

## Extreme point of the invariant probability measures

`μ` is a translation-invariant probability measure that is not a nontrivial convex combination
of
two distinct translation-invariant probability measures.

Formalized by `StatMech.FK.IsInvariantExtremePoint`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ExtremeIsErgodic.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/ExtremeIsErgodic.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#is-invariant-extreme-point).

## Extreme invariant measures are ergodic

An extreme point of the translation-invariant probability measures is ergodic.

Formalized by `StatMech.FK.fec_isErgodic_of_invariantExtremePoint`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/ExtremeIsErgodic.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/ExtremeIsErgodic.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fec-is-ergodic-of-invariant-extreme-poin).

## Conditional product cap for multi-open events in boxes

For every finite family of finite edge sets and box index `N`, some translation `g` satisfies,
for
all large `m`: each `O_T ∩ g⁻¹O_{T'}` is `A ∩ B` on `Λ_m` with `A` increasing and `B` depending
only
on edges outside some `F`, the conditional masses of `A` on the fibres of `F` (with a boundary
graph
containing the wired one) are at most `μ_N(O_T)`, and the mass of `B` is at most `μ_N(O_{T'})`.

Formalized by `StatMech.FK.fdb_BoxConditionalProductCap`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKDisjointBoxReduce.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKDisjointBoxReduce.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fdb-box-conditional-product-cap).

## Far-box product domination of multi-open events

For every finite family of finite edge sets, box index `m`, and `δ > 0`, some translation `g`
satisfies `μ(O_T ∩ g⁻¹O_{T'}) ≤ μ_m(O_T) μ_m(O_{T'}) + δ` for all `T, T'` in the family.

Formalized by `StatMech.FK.ftb_FarBoxProductDom`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKTwoBoxDecoupling.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKTwoBoxDecoupling.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#ftb-far-box-product-dom).

## Finite-box disjoint product domination of multi-open events

For every finite family of finite edge sets and box index `N`, some translation `g` satisfies,
for
all large `m`, `μ_m(O_T ∩ g⁻¹O_{T'}) ≤ μ_N(O_T) μ_N(O_{T'})` for all `T, T'` in the family.

Formalized by `StatMech.FK.ftb_FiniteBoxDisjointProductDom`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKTwoBoxDecoupling.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKTwoBoxDecoupling.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#ftb-finite-box-disjoint-product-dom).

## Translated wired box measure

The wired finite-volume random-cluster measure on `Λ_n` translated by `g`.

Formalized by `StatMech.FK.erg_wiredShiftedFinite`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeTranslationInvariance.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeTranslationInvariance.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#erg-wired-shifted-finite).

## Translated free box measure

The free finite-volume random-cluster measure on `Λ_n` translated by `g`.

Formalized by `StatMech.FK.erg_freeShiftedFinite`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeTranslationInvariance.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolumeTranslationInvariance.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#erg-free-shifted-finite).

## Wired integral shift decay along a box sequence

Along the box sequence `φ`, the wired box integrals of `f` and of `f ∘ θ_g` differ by a
quantity tending to zero, for every bounded continuous `f`.

Formalized by `StatMech.FK.ivt_wiredIntegralShiftDecay`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IVTranslationInvariance.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IVTranslationInvariance.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#ivt-wired-integral-shift-decay).

## Free integral shift decay along a box sequence

Along the box sequence `φ`, the free box integrals of `f` and of `f ∘ θ_g` differ by a
quantity tending to zero, for every bounded continuous `f`.

Formalized by `StatMech.FK.ivt_freeIntegralShiftDecay`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IVTranslationInvariance.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IVTranslationInvariance.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#ivt-free-integral-shift-decay).

## Wired translation invariance from integral shift decay

The wired infinite-volume FK measure is translation invariant if the integral decay
hypothesis holds for every shift and every convergent box subsequence. See also
`flc_wiredIV_isTranslationInvariant`, which proves invariance for `q = 2` without hypotheses.

Formalized by `StatMech.FK.ivt_wiredIV_isTranslationInvariant_of_decay`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IVTranslationInvariance.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IVTranslationInvariance.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#ivt-wired-iv-is-translation-invariant-of).

## Free translation invariance from integral shift decay

The free infinite-volume FK measure is translation invariant if the integral decay hypothesis
holds for every shift and every convergent box subsequence. See also
`bdp_freeIV_isTranslationInvariant`, which proves invariance for `q = 2` without hypotheses.

Formalized by `StatMech.FK.ivt_freeIV_isTranslationInvariant_of_decay`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IVTranslationInvariance.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IVTranslationInvariance.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#ivt-free-iv-is-translation-invariant-of).

## Identity shift satisfies the wired decay hypothesis

The identity shift satisfies the wired decay hypothesis, so it is not vacuous.

Formalized by `StatMech.FK.ivt_wiredIntegralShiftDecay_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IVTranslationInvariance.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IVTranslationInvariance.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#ivt-wired-integral-shift-decay-one).

## Identity shift satisfies the free decay hypothesis

The identity shift satisfies the free decay hypothesis, so it is not vacuous.

Formalized by `StatMech.FK.ivt_freeIntegralShiftDecay_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IVTranslationInvariance.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IVTranslationInvariance.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#ivt-free-integral-shift-decay-one).

## Shift-decay functional of a sequence of measures

The difference `∫ f dμ_n - ∫ f ∘ θ_g dμ_n` between the integrals of `f` and of its shift by
`g` against the `n`-th measure.

Formalized by `StatMech.FK.isd_decayFun`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IntegralShiftDecay.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IntegralShiftDecay.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#isd-decay-fun).

## Shift decay extends from a dense set of test functions

If `D_n(f') → 0` for all `f'` in a dense set of bounded continuous functions, then
`D_n(f) → 0` for every bounded continuous `f`. This is the equicontinuity argument of
`EquicontinuousAt.tendsto_of_mem_closure`, specialized to the uniformly Lipschitz family
`f ↦ D_n(f)`.

Formalized by `StatMech.FK.isd_tendsto_decay_of_dense`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IntegralShiftDecay.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IntegralShiftDecay.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#isd-tendsto-decay-of-dense).

## Wired shift decay on a dense set of test functions

Decay of `D_n` along the wired box measures `φ^1_{Λ_{φ(n)}}` on some dense set of bounded
continuous functions.

Formalized by `StatMech.FK.isd_wiredDenseDecay`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IntegralShiftDecay.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IntegralShiftDecay.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#isd-wired-dense-decay).

## Free shift decay on a dense set of test functions

Decay of `D_n` along the free box measures `φ^0_{Λ_{φ(n)}}` on some dense set of bounded
continuous functions.

Formalized by `StatMech.FK.isd_freeDenseDecay`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IntegralShiftDecay.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IntegralShiftDecay.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#isd-free-dense-decay).

## Wired translation invariance from decay on a dense set

The wired infinite-volume FK measure is translation invariant if, for every shift and every
convergent box subsequence, `D_n` decays on a dense set. See also
`flc_wiredIV_isTranslationInvariant` (unconditional for `q = 2`).

Formalized by `StatMech.FK.isd_wiredIV_isTranslationInvariant_of_denseDecay`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IntegralShiftDecay.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IntegralShiftDecay.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#isd-wired-iv-is-translation-invariant-of).

## Free translation invariance from decay on a dense set

The free infinite-volume FK measure is translation invariant if, for every shift and every
convergent box subsequence, `D_n` decays on a dense set. See also
`bdp_freeIV_isTranslationInvariant` (unconditional for `q = 2`).

Formalized by `StatMech.FK.isd_freeIV_isTranslationInvariant_of_denseDecay`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/IntegralShiftDecay.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/IntegralShiftDecay.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#isd-free-iv-is-translation-invariant-of).

## Edge-open indicator as a continuous function

The indicator `ω ↦ 1{ω_e = 1}` of the edge `e` being open, as a continuous function.

Formalized by `StatMech.FK.idc_coordCM`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#idc-coord-cm).

## Edge-open indicator as a bounded continuous function

The edge indicator `ω ↦ 1{ω_e = 1}` as a bounded continuous function.

Formalized by `StatMech.FK.idc_coordBcf`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#idc-coord-bcf).

## Wired box integral of an edge indicator is the wired edge marginal

The integral of the indicator of a box edge against the wired box measure on `Λ_m` is the
wired edge marginal.

Formalized by `StatMech.FK.idc_integral_coordBcf_wired`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#idc-integral-coord-bcf-wired).

## Free box integral of an edge indicator is the free edge marginal

The integral of the indicator of a box edge against the free box measure on `Λ_m` is the
free edge marginal.

Formalized by `StatMech.FK.idc_integral_coordBcf_free`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#idc-integral-coord-bcf-free).

## Decay of the edge-indicator functional from equal wired densities

If the box edge `e` and its shift `g⁻¹ e` have the same wired `q = 2` density, the decay
functional of the indicator of `e` along the wired box measures tends to zero.

Formalized by `StatMech.FK.idc_wired_coord_decay_of_density_eq`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#idc-wired-coord-decay-of-density-eq).

## Cylinder algebra generated by edge indicators

The subalgebra of continuous functions generated by the edge indicators.

Formalized by `StatMech.FK.idc_cylinderAlg`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#idc-cylinder-alg).

## Cylinder algebra as bounded continuous functions

The cylinder algebra viewed as a set of bounded continuous functions.

Formalized by `StatMech.FK.idc_cylinderBcfSet`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#idc-cylinder-bcf-set).

## Density of cylinder functions among bounded continuous functions

The cylinder functions are dense in the bounded continuous functions, by Stone–Weierstrass
on the compact configuration space.

Formalized by `StatMech.FK.idc_cylinderBcfSet_dense`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#idc-cylinder-bcf-set-dense).

## Cylinder decay along the wired box measures

The decay functional tends to zero along the wired box measures for every cylinder
function.

Formalized by `StatMech.FK.idc_wiredCylinderDecay`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#idc-wired-cylinder-decay).

## Cylinder decay along the free box measures

The decay functional tends to zero along the free box measures for every cylinder
function.

Formalized by `StatMech.FK.idc_freeCylinderDecay`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#idc-free-cylinder-decay).

## Translation invariance of the wired FK measure from cylinder decay

The wired infinite-volume FK measure is translation invariant if cylinder decay holds for
every shift and every convergent box subsequence. See also `flc_wiredIV_isTranslationInvariant`
(unconditional for `q = 2`).

Formalized by `StatMech.FK.idc_wiredIV_isTranslationInvariant_of_cylinderDecay`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#idc-wired-iv-is-translation-invariant-of).

## Translation invariance of the free FK measure from cylinder decay

The free infinite-volume FK measure is translation invariant if cylinder decay holds for
every shift and every convergent box subsequence. See also `bdp_freeIV_isTranslationInvariant`
(unconditional for `q = 2`).

Formalized by `StatMech.FK.idc_freeIV_isTranslationInvariant_of_cylinderDecay`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/EdgeIndicatorShiftDecay.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#idc-free-iv-is-translation-invariant-of).

## Translation of $\mathbb{Z}^d$ by a vector

Translation `x ↦ x + v` as a permutation of `ℤ^d`.

Formalized by `StatMech.FK.fktc_translate`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fktc-translate).

## Unit translations are not box symmetries

Translation by a unit vector does not preserve the centered boxes, so it is not a `BoxSym`.

Formalized by `StatMech.FK.fktc_translate_not_box_mem`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fktc-translate-not-box-mem).

## A site and its translate lie in a common centered box

A site and its translate lie in a common centered box.

Formalized by `StatMech.FK.fktc_point_and_translate_in_box`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fktc-point-and-translate-in-box).

## An edge and its translate lie in a common centered box

The endpoints of an edge and of its translate lie in a common centered box.

Formalized by `StatMech.FK.fktc_edge_and_translate_in_box`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fktc-edge-and-translate-in-box).

## Unordered pair of two sites of a box $\Lambda_N$

The pair `{x, y}` as an element of `Sym2 Λ_N`, for sites `x, y ∈ Λ_N`.

Formalized by `StatMech.FK.fktc_boxEdge`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fktc-box-edge).

## Wired edge density is constant on orbits of a box symmetry

The wired edge density is constant on each orbit of a box symmetry.

Formalized by `StatMech.FK.fktc_wired_box_density_const_of_orbit`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fktc-wired-box-density-const-of-orbit).

## Free edge density is constant on orbits of a box symmetry

The free edge density is constant on each orbit of a box symmetry.

Formalized by `StatMech.FK.fktc_free_box_density_const_of_orbit`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fktc-free-box-density-const-of-orbit).

## Equal wired densities from merging wired marginals

If the wired marginals of two box edges on `Λ_{N+k}` differ by a quantity tending to zero,
the two edges have the same wired density.

Formalized by `StatMech.FK.fktc_wired_density_eq_of_marg_decay`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fktc-wired-density-eq-of-marg-decay).

## Equal free densities from merging free marginals

If the free marginals of two box edges on `Λ_{N+k}` differ by a quantity tending to zero, the
two edges have the same free density.

Formalized by `StatMech.FK.fktc_free_density_eq_of_marg_decay`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fktc-free-density-eq-of-marg-decay).

## Translation invariance of the wired density given merging marginals

An edge and its translate have the same wired density if their wired marginals merge along
the boxes. See also `bdp_wiredEdgeDensity_translation_inv`, which proves the conclusion without
the merging hypothesis.

Formalized by `StatMech.FK.fktc_wired_density_translation_inv`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fktc-wired-density-translation-inv).

## Translation invariance of the free density given merging marginals

An edge and its translate have the same free density if their free marginals merge along the
boxes. See also `bdp_freeEdgeDensity_translation_inv`, which proves the conclusion without the
merging hypothesis.

Formalized by `StatMech.FK.fktc_free_density_translation_inv`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fktc-free-density-translation-inv).

## Translation invariance of free and wired densities if marginals merge

Translation invariance of the free and wired densities of an edge under the merging
hypotheses of `fktc_wired_density_translation_inv` and `fktc_free_density_translation_inv`.

Formalized by `StatMech.FK.fktc_density_translation_inv`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fktc-density-translation-inv).

## Constant wired density gives a lower bound on expected open edges

If the wired density is constant on a set `EB` of box edges, `|EB|` times that density is at
most the expected number of open edges of `EB` under the wired measure on any larger box.

Formalized by `StatMech.FK.fktc_wired_density_eq_const`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fktc-wired-density-eq-const).

## Constant free density gives an upper bound on expected open edges

If the free density is constant on a set `EB` of box edges, the expected number of open edges
of `EB` under the free measure on any larger box is at most `|EB|` times that density.

Formalized by `StatMech.FK.fktc_free_density_eq_const`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fktc-free-density-eq-const).

## Wired lower bound on expected open edges along a box-symmetry orbit

`fktc_wired_density_eq_const` for a set of edges contained in one orbit of a box symmetry.

Formalized by `StatMech.FK.fktc_wired_density_eq_const_orbit`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fktc-wired-density-eq-const-orbit).

## Free upper bound on expected open edges along a box-symmetry orbit

`fktc_free_density_eq_const` for a set of edges contained in one orbit of a box symmetry.

Formalized by `StatMech.FK.fktc_free_density_eq_const_orbit`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationCofinal.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fktc-free-density-eq-const-orbit).

## Event that every edge of a finite set is open

The event that every edge of `s` is open. Equal to `fmu_multiOpen` (see
`ftb_fmu_eq_cdc_multiOpen`).

Formalized by `StatMech.FK.cdc_multiOpenEvent`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvarianceFromHomogeneity.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvarianceFromHomogeneity.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#cdc-multi-open-event).

## Continuous monomial indicator that every edge of a set is open

The continuous function `ω ↦ ∏_{e ∈ s} ω(e)`, the indicator of `cdc_multiOpenEvent s`.

Formalized by `StatMech.FK.cdc_monomialCM`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvarianceFromHomogeneity.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvarianceFromHomogeneity.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#cdc-monomial-cm).

## Monomial indicator as a bounded continuous function

`cdc_monomialCM s` as a bounded continuous function.

Formalized by `StatMech.FK.cdc_monomialBcf`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvarianceFromHomogeneity.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvarianceFromHomogeneity.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#cdc-monomial-bcf).

## Event that every edge of a set of box edges is open, on a box

The event that every edge of `t ⊆ E(Λ_N)` is open, on configurations of `Λ_N`.

Formalized by `StatMech.FK.cdc_boxMultiOpenEvent`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvarianceFromHomogeneity.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvarianceFromHomogeneity.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#cdc-box-multi-open-event).

## Wired $q = 2$ multi-edge homogeneity under a translation

The wired `q = 2` infinite-volume measure gives every multi-open event the same mass as its
translate by `g⁻¹`.

Formalized by `StatMech.FK.cdc_wiredMultiHomogeneous`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvarianceFromHomogeneity.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvarianceFromHomogeneity.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#cdc-wired-multi-homogeneous).

## Free $q = 2$ multi-edge homogeneity under a translation

The free `q = 2` infinite-volume measure gives every multi-open event the same mass as its
translate by `g⁻¹`.

Formalized by `StatMech.FK.cdc_freeMultiHomogeneous`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvarianceFromHomogeneity.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvarianceFromHomogeneity.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#cdc-free-multi-homogeneous).

## Submodule of functions with vanishing wired shift decay

The continuous functions whose shift-decay functional along the wired box measures (on the
subsequence `φ`) tends to `0`, as a submodule.

Formalized by `StatMech.FK.cdc_wiredDecaySet`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvarianceFromHomogeneity.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvarianceFromHomogeneity.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#cdc-wired-decay-set).

## Submodule of functions with vanishing free shift decay

The continuous functions whose shift-decay functional along the free box measures (on the
subsequence `φ`) tends to `0`, as a submodule.

Formalized by `StatMech.FK.cdc_freeDecaySet`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvarianceFromHomogeneity.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TranslationInvarianceFromHomogeneity.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#cdc-free-decay-set).

## Disjoint-box cap hypothesis for multi-open events

For every finite family of finite edge sets and scale `N`, some translation `g` and margin `r`
realize each pair `T`, `g⁻¹T'` in `Λ_{N+r}` with `g⁻¹T'` outside a set `F`, such that the
conditional masses of `O_T` on fibres of `F` (with a boundary graph containing the wired one)
are at
most `μ_N(O_T)` and the box mass of `g⁻¹O_{T'}` is at most `μ_N(O_{T'})`.

Formalized by `StatMech.FK.dgf_DisjointBoxAnalyticCap`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/DisjointBoxFactorization.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/DisjointBoxFactorization.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#dgf-disjoint-box-analytic-cap).

## Edge inclusion of a translated box into $\mathbb{Z}^d$

The inclusion of edges of the translated box `v + Λ_m` into the edges of `ℤ^d`.

Formalized by `StatMech.FK.lmc_transEdgeIncl`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-trans-edge-incl).

## Translated box edges are shifted centered box edges

Including a translated box edge equals shifting the included centered box edge by `v`.

Formalized by `StatMech.FK.lmc_transEdgeIncl_sigma_eq_smul`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-trans-edge-incl-sigma-eq-smul).

## Images of translated edge sets are shifted images

The image of a translated edge set in `ℤ^d` is the shift by `v` of the image of the centered
set.

Formalized by `StatMech.FK.lmc_transImage_eq_smulImage`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-trans-image-eq-smul-image).

## Wired all-open probability on a translated box

The probability, under the wired `q = 2` FK measure on the translated box `v + Λ_m`, that all
edges of the translated copy of `t ⊆ E(Λ_N)` are open.

Formalized by `StatMech.FK.lmc_transBoxMass`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-trans-box-mass).

## Translated wired box mass equals the centered box mass

The translated wired box mass equals the probability of the unshifted event under the wired
finite-volume measure on the centered box `Λ_m`.

Formalized by `StatMech.FK.lmc_transBoxMass_eq_centred`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-trans-box-mass-eq-centred).

## Translated wired box masses converge to the infinite-volume mass

The translated wired box masses converge to the wired infinite-volume probability that all
edges of `t` are open.

Formalized by `StatMech.FK.lmc_transBoxMass_tendsto_centred_iv`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-trans-box-mass-tendsto-centred-iv).

## Wired shift invariance of an all-open event from matching limits

If the translated wired box masses also converge to the wired infinite-volume probability of
the shifted set `v + t`, the wired infinite-volume measure gives `t` and `v + t` the same
probability.

Formalized by `StatMech.FK.lmc_wiredMultiHomogeneous_of_cofinal`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-wired-multi-homogeneous-of-cofinal).

## Wired shift invariance of an all-open event from decaying differences

If the translated wired box masses differ from the centered box masses of a set `t'` with `v +
t = t'` by a sequence tending to zero, the wired infinite-volume measure gives `t` and `v + t`
the same probability.

Formalized by `StatMech.FK.lmc_wiredMultiHomogeneous_of_decay`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-wired-multi-homogeneous-of-decay).

## Wired placement hypothesis for a shift

The placement hypothesis for the shift `g`: every finite edge set lies in a box whose
translated wired box masses converge to the wired infinite-volume probability of the set
shifted by `g⁻¹`.

Formalized by `StatMech.FK.lmc_wiredPlacement`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-wired-placement).

## Wired placement gives shift homogeneity on all-open events

The placement hypothesis for `g` gives `g`-homogeneity of the wired infinite-volume measure on
all events "every edge of `s` is open".

Formalized by `StatMech.FK.lmc_wiredMultiHomogeneous`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-wired-multi-homogeneous).

## Identity shift satisfies the wired placement hypothesis

The identity shift satisfies the wired placement hypothesis.

Formalized by `StatMech.FK.lmc_wiredPlacement_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-wired-placement-one).

## Wired infinite-volume measure is homogeneous under the identity shift

The wired infinite-volume measure is homogeneous under the identity shift.

Formalized by `StatMech.FK.lmc_wiredMultiHomogeneous_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-wired-multi-homogeneous-one).

## Wired translation invariance from the placement hypothesis

The wired `q = 2` infinite-volume FK measure on `ℤ^d` is translation invariant if every shift
satisfies the wired placement hypothesis.

Formalized by `StatMech.FK.lmc_wiredIV_isTranslationInvariant_of_placement`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-wired-iv-is-translation-invariant-of).

## Translated free box mass of an edge set

The probability, under the free `q = 2` FK measure on the translated box `v + Λ_m`, that all
edges of the translated copy of `t ⊆ E(Λ_N)` are open.

Formalized by `StatMech.FK.lmc_transBoxMassFree`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-trans-box-mass-free).

## Translated free box mass equals the centred box probability

The translated free box mass equals the probability of the unshifted event under the free
finite-volume measure on the centered box `Λ_m`.

Formalized by `StatMech.FK.lmc_transBoxMassFree_eq_centred`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-trans-box-mass-free-eq-centred).

## Translated free box masses converge to the free infinite-volume value

The translated free box masses converge to the free infinite-volume probability that all edges
of `t` are open.

Formalized by `StatMech.FK.lmc_transBoxMassFree_tendsto_centred_iv`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-trans-box-mass-free-tendsto-centred).

## Equal free probabilities for $t$ and $v + t$ from matching box limits

If the translated free box masses also converge to the free infinite-volume probability of the
shifted set `v + t`, the free infinite-volume measure gives `t` and `v + t` the same
probability.

Formalized by `StatMech.FK.lmc_freeMultiHomogeneous_of_cofinal`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-free-multi-homogeneous-of-cofinal).

## Free placement hypothesis for a shift via box-mass limits

The placement hypothesis for the shift `g` and the free measure: every finite edge set lies in
a box whose translated free box masses converge to the free infinite-volume probability of the
set shifted by `g⁻¹`.

Formalized by `StatMech.FK.lmc_freePlacement`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-free-placement).

## Free placement gives shift homogeneity on all-open events

The free placement hypothesis for `g` gives `g`-homogeneity of the free infinite-volume
measure on all events "every edge of `s` is open".

Formalized by `StatMech.FK.lmc_freeMultiHomogeneous`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-free-multi-homogeneous).

## Identity shift satisfies the free placement hypothesis

The identity shift satisfies the free placement hypothesis.

Formalized by `StatMech.FK.lmc_freePlacement_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-free-placement-one).

## Free infinite-volume measure is homogeneous under the identity shift

The free infinite-volume measure is homogeneous under the identity shift.

Formalized by `StatMech.FK.lmc_freeMultiHomogeneous_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-free-multi-homogeneous-one).

## Free translation invariance from the placement hypothesis

The free `q = 2` infinite-volume FK measure on `ℤ^d` is translation invariant if every shift
satisfies the free placement hypothesis.

Formalized by `StatMech.FK.lmc_freeIV_isTranslationInvariant_of_placement`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitCommutation.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#lmc-free-iv-is-translation-invariant-of).

## Sup norm of a site of $\mathbb{Z}^d$

The sup-norm `max_i |v_i|` of a site `v`.

Formalized by `StatMech.FK.flc_vrad`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredTranslationInvariance.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredTranslationInvariance.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#flc-vrad).

## Inclusion of a subset of sites into a larger one

The inclusion of a subset of sites into a larger one, as a map of subtypes.

Formalized by `StatMech.FK.flc_incl`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredTranslationInvariance.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredTranslationInvariance.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#flc-incl).

## Box edge set included into $\Lambda_m$ and translated by $v$

The edge set `t` of `Λ_N`, included into `Λ_m` and translated by `v`.

Formalized by `StatMech.FK.flc_transEdges`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredTranslationInvariance.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredTranslationInvariance.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#flc-trans-edges).

## Translation invariance of the wired $q = 2$ infinite-volume measure

The wired `q = 2` infinite-volume random-cluster measure on `ℤ^d` is translation invariant.

Formalized by `StatMech.FK.flc_wiredIV_isTranslationInvariant`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredTranslationInvariance.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredTranslationInvariance.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#flc-wired-iv-is-translation-invariant).

## Domain monotonicity of wired $q = 2$ box measures

For `q = 2` and `N ≤ m`, the wired `Λ_m` measure of an increasing `Λ_N` cylinder event is at
most its wired `Λ_N` measure.

Formalized by `StatMech.FK.fwm_wired_box_domain_monotone`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fwm-wired-box-domain-monotone).

## Domain monotonicity of wired multi-open probabilities

For `q = 2` and `N ≤ m`, the wired `Λ_m` probability that a set of `Λ_N` edges is open is at
most its wired `Λ_N` probability.

Formalized by `StatMech.FK.fwm_wired_multiOpen_domain_monotone`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fwm-wired-multi-open-domain-monotone).

## Domain monotonicity for edge sets realized in a box

The same for an edge set of `ℤ^d` given as the image of `Λ_N` edges.

Formalized by `StatMech.FK.fwm_wired_domain_monotone_of_realised`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fwm-wired-domain-monotone-of-realised).

## Domain monotonicity for translated pairs of multi-open events

The same for the event "`T` open and `g·T'` open", when `T ∪ g⁻¹·T'` lies in `Λ_N`.

Formalized by `StatMech.FK.fwm_wired_cross_le_box_domain`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fwm-wired-cross-le-box-domain).

## Disjoint-box factorization bound for box measures

The disjoint-box factorization bound for a family of box measures `μbox`: for every finite
family `P` of edge sets realized in `Λ_N` there are a translation `g` and `r` such that each
`T ∪ g⁻¹·T'` lies in `Λ_(N+r)` and `μbox (N+r) (T open, g·T' open) ≤ μbox N (T open) ·
μbox N (T' open)`. The parameters `p` only index the family.

Formalized by `StatMech.FK.fwm_WiredDisjointBoxFactorise`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fwm-wired-disjoint-box-factorise).

## Finite-box product domination from the factorization bound

Under the factorization bound for the wired measures, for some translation `g` and all large
`m`, `φ¹_{Λ_m}(T open, g·T' open) ≤ φ¹_{Λ_N}(T open) φ¹_{Λ_N}(T' open)` for all `T, T' ∈ P`.

Formalized by `StatMech.FK.fwm_finiteBoxDisjointProductDom_conclusion_of_factorise`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fwm-finite-box-disjoint-product-dom-conc).

## Realized edge sets stay realized in larger boxes

An edge set realized in `Λ_(N₀)` is realized in every larger box.

Formalized by `StatMech.FK.fwm_realised_box_mono`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fwm-realised-box-mono).

## Every finite family of edge sets is realized in some box

Every finite family of finite edge sets is realized in some box.

Formalized by `StatMech.FK.fwm_exists_realising_box`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fwm-exists-realising-box).

## Wired box products approximate infinite-volume products

For `q = 2`, products of wired box probabilities of open-edge events approximate the wired
infinite-volume products within `δ`, for some box `Λ_m` with `m ≥ N₀`.

Formalized by `StatMech.FK.fwm_exists_common_box_ge_wired`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fwm-exists-common-box-ge-wired).

## Upper decorrelation of the wired measure from factorization

The factorization bound for the wired `q = 2` box measures gives upper decorrelation of the
wired infinite-volume measure.

Formalized by `StatMech.FK.fwm_upperDecay_of_factorise`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fwm-upper-decay-of-factorise).

## Wired $q = 2$ measure is ergodic under the factorization bound

If the wired `q = 2` box measures satisfy the factorization bound, the wired infinite-volume measure is ergodic under translations of `ℤ^d`.

Formalized by `StatMech.FK.fwm_wiredIV_isErgodic_of_factorise`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fwm-wired-iv-is-ergodic-of-factorise).

## All-open Dirac mass satisfies the factorization bound

The factorization bound is satisfiable: the Dirac mass on the all-open configuration satisfies
it.

Formalized by `StatMech.FK.fwm_wiredDisjointBoxFactorise_dirac`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FKWiredDomainMonotone.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#fwm-wired-disjoint-box-factorise-dirac).

## Empty boundary predicate

The empty boundary predicate.

Formalized by `StatMech.FK.bdp_noBdry`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeTranslationInvariance.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FreeTranslationInvariance.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#bdp-no-bdry).

## Translation invariance of the free $q = 2$ infinite-volume measure

The free `q = 2` infinite-volume random-cluster measure on `ℤ^d` is translation invariant.

Formalized by `StatMech.FK.bdp_freeIV_isTranslationInvariant`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeTranslationInvariance.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FreeTranslationInvariance.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#bdp-free-iv-is-translation-invariant).

## Free $q = 2$ box edge marginals are at most the free density

Edge marginals of the free box measure are at most the free infinite-volume density (the case
`N = n` of `dfi_free_per_edge_le`).

Formalized by `StatMech.FK.bdp_free_per_edge_upper`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeTranslationInvariance.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FreeTranslationInvariance.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#bdp-free-per-edge-upper).

## Wired $q = 2$ box edge marginals are at least the wired density

Edge marginals of the wired box measure are at least the wired infinite-volume density (the
case
`N = n` of `dfi_wired_per_edge_ge`).

Formalized by `StatMech.FK.bdp_wired_per_edge_lower`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeTranslationInvariance.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FreeTranslationInvariance.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#bdp-wired-per-edge-lower).

## Free off-centre sandwich hypothesis

For every edge `e'` of `Λ_N` and every `t`, there are interior edge sets `I_n` of `Λ_n`
carrying
asymptotically all edges on which the free density equals that of `e'` and the free box
marginals
are at least that density minus `δ_n → 0`.

Formalized by `StatMech.FK.bdp_FreeOffCentreSandwich`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeTranslationInvariance.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FreeTranslationInvariance.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#bdp-free-off-centre-sandwich).

## Wired off-centre sandwich hypothesis

For every edge `e'` of `Λ_N` and every `t`, there are interior edge sets `I_n` of `Λ_n`
carrying
asymptotically all edges on which the wired density equals that of `e'` and the wired box
marginals
are at most that density plus `δ_n → 0`.

Formalized by `StatMech.FK.bdp_WiredOffCentreSandwich`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/FreeTranslationInvariance.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/FreeTranslationInvariance.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#bdp-wired-off-centre-sandwich).

## Shift vector moving $\Lambda_N$ to a disjoint box

The vector `(2N + 1) e_{i₀}`, which translates `Λ_N` to a disjoint box.

Formalized by `StatMech.FK.cbk_shiftVec`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredErgodicity.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredErgodicity.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#cbk-shift-vec).

## Translate of a vertex of $\Lambda_N$ as a vertex of $\Lambda_{N+r}$

The vertex of `Λ_{N+r}` obtained by translating a vertex of `Λ_N` by `v` with `‖v‖_∞ ≤ r`.

Formalized by `StatMech.FK.cbk_shiftBoxVert`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredErgodicity.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredErgodicity.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#cbk-shift-box-vert).

## Translate of an edge of $\Lambda_N$ as an edge of $\Lambda_{N+r}$

The edge of `Λ_{N+r}` obtained by translating an edge of `Λ_N` by `v` with `‖v‖_∞ ≤ r`.

Formalized by `StatMech.FK.cbk_shiftEdge`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredErgodicity.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredErgodicity.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#cbk-shift-edge).

## Ergodicity of the wired random-cluster measure

For `d ≥ 1` and `p ∈ (0, 1)`, the wired `q = 2`
infinite-volume random-cluster measure on `ℤ^d` is ergodic under translations
(Grimmett, *The Random-Cluster Model*, 2006, Theorem 4.19).

Formalized by `StatMech.FK.cbk_wiredIV_isErgodic`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredErgodicity.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredErgodicity.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html#cbk-wired-iv-is-ergodic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Translation invariance and ergodicity of the q = 2 random-cluster measures](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/translation-invariance-and-ergodicity-of-the-q-2)
