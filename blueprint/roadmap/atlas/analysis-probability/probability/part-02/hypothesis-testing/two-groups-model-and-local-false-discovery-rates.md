---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel, MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.mixtureDensity, MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.nullLaw, MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.altLaw, MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.jointLaw, MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.localFdr, MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.tailFdr, MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.mixtureDensity_nonneg
statement: formalized
proof: formalized
---

# Two-groups model and local false discovery rates

38 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html).

## The two-groups model

## Two-groups model

The two-groups model of Efron et al. (2001): prior null probability `π₀ ∈ [0, 1]`, null
density `f₀` and non-null density `f₁` of the z-value (probability densities on `ℝ`).

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel`, a structure declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#two-groups-model).

## Mixture density of the two-groups model

The mixture density `f = π₀ f₀ + (1 - π₀) f₁` of the z-values.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.mixtureDensity`, a definition declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#mixture-density).

## Law of a null z-value

The law `P₀` of a null z-value.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.nullLaw`, a definition declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#null-law).

## Law of a non-null z-value

The law `P₁` of a non-null z-value.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.altLaw`, a definition declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#alt-law).

## Joint law of null indicator and z-value

Joint law of (null indicator, z-value) on `Bool × ℝ`; `true` means the case is null.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.jointLaw`, a definition declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#joint-law).

## Local false discovery rate

Efron's local false discovery rate `fdr(z) = π₀ f₀(z) / f(z)` (zero where `f(z) = 0`).

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.localFdr`, a definition declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#local-fdr).

## Tail-area false discovery rate

The tail-area false discovery rate of a region `Γ`: `Fdr(Γ) = π₀ P₀(Γ) / P(Γ)`, written with
the densities. Efron's `Fdr(z)` is `tailFdr (Set.Iic z)`. It is `0` when `P(Γ) = 0`.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.tailFdr`, a definition declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#tail-fdr).

## Mixture density is nonnegative

The mixture density is nonnegative.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.mixtureDensity_nonneg`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#mixture-density-nonneg).

## Null part of the mixture is dominated by the mixture

The null part of the mixture is dominated by the mixture: `π₀ f₀ ≤ f`.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.mul_f₀_le_mixtureDensity`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#mul-f-le-mixture-density).

## Mixture density is measurable

The mixture density is measurable.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.measurable_mixtureDensity`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#measurable-mixture-density).

## Mixture density is integrable

The mixture density is integrable.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.integrable_mixtureDensity`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#integrable-mixture-density).

## Local false discovery rate is measurable

The local false discovery rate is measurable.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.measurable_localFdr`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#measurable-local-fdr).

## Local fdr times mixture density equals the null part

The basic identity `fdr(z) f(z) = π₀ f₀(z)`, for every `z` (where `f(z) = 0` both sides
vanish because `π₀ f₀ ≤ f`).

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.localFdr_mul_mixtureDensity`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#local-fdr-mul-mixture-density).

## Local false discovery rate is nonnegative

The local false discovery rate is nonnegative.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.localFdr_nonneg`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#local-fdr-nonneg).

## Local false discovery rate is at most one

The local false discovery rate is at most one.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.localFdr_le_one`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#local-fdr-le-one).

## Null law as the integral of the null density

`P₀(A) = ∫_A f₀`.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.nullLaw_apply`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#null-law-apply).

## Non-null law as the integral of the non-null density

`P₁(A) = ∫_A f₁`.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.altLaw_apply`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#alt-law-apply).

## Joint probability of a null case in a set

`P(H = 0, Z ∈ A) = π₀ P₀(A)`.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.jointLaw_null_prod`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#joint-law-null-prod).

## Joint probability of a non-null case in a set

`P(H = 1, Z ∈ A) = (1 - π₀) P₁(A)`.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.jointLaw_alt_prod`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#joint-law-alt-prod).

## z-value has the mixture law

The z-value has the mixture law: `P(Z ∈ A) = ∫_A f`.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.jointLaw_univ_prod`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#joint-law-univ-prod).

## Marginal z-value law of the joint law is the mixture

The law of the z-value under the joint law is the mixture `f · Lebesgue`.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.map_snd_jointLaw`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#map-snd-joint-law).

## Null probability as an integral of the local fdr

Efron et al. (2001): `P(H = 0, Z ∈ A) = ∫_A fdr(z) dP_Z(z)` for every measurable `A`, so
`fdr(Z)` is a version of the posterior null probability `P(H = 0 | Z)`.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.jointLaw_null_prod_eq_lintegral_localFdr`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#joint-law-null-prod-eq-lintegral-local-f).

## Local fdr is the posterior null probability

Efron et al. (2001): `fdr(Z) = P(H = 0 | Z)` almost surely, as a conditional expectation
of the null indicator given the z-value.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.condExp_null_eq_localFdr`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#cond-exp-null-eq-local-fdr).

## Tail-area fdr is the posterior null probability given a region

`P(H = 0 | Z ∈ Γ) = Fdr(Γ)`: the tail-area false discovery rate is the posterior null
probability given `Z ∈ Γ` (Storey 2002, Theorem 1; Efron 2010, ch. 2). Both sides are `0` when
`P(Z ∈ Γ) = 0`.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.cond_null_eq_tailFdr`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#cond-null-eq-tail-fdr).

## Tail-area fdr is the average local fdr over the region

`E[fdr(Z) | Z ∈ Γ] = Fdr(Γ)`, written with densities: the tail-area false discovery rate is
the `f`-weighted average of the local false discovery rate over `Γ` (Efron 2010, ch. 5).

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.tailFdr_eq_setIntegral_localFdr`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#tail-fdr-eq-set-integral-local-fdr).

## True-null set of a test outcome vector

The true-null set of an outcome vector `x : Fin m → Bool × Bool`, where `(x i).1` records
that hypothesis `i` is null and `(x i).2` that it is rejected.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.nullSet`, a definition declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#null-set).

## Rejection set of a test outcome vector

The rejection set of an outcome vector.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.rejectedSet`, a definition declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#rejected-set).

## Probability of a test outcome vector

The probability `∏ᵢ q(xᵢ)` of an outcome vector when the `m` (null, rejected) pairs are
i.i.d. with law `q`.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.outcomeWeight`, a definition declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#outcome-weight).

## Storey's positive false discovery rate

Storey's positive false discovery rate `pFDR = E[V / R | R > 0]` for `m` tests whose
(null, rejected) indicator pairs are i.i.d. with law `q`: `V / R` is the false discovery
proportion.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.positiveFDR`, a definition declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#positive-fdr).

## Storey's theorem: pFDR is a posterior null probability

Storey (2002), Theorem 1: for `m ≥ 1` i.i.d. tests, `pFDR = P(H = 0 | T ∈ Γ)`, where
`q (true, true) = P(H = 0, T ∈ Γ)` and `q (false, true) = P(H = 1, T ∈ Γ)`. The identity is
homogeneous in `q`, so only `q ≥ 0` is assumed; when `P(T ∈ Γ) = 0` both sides are `0`.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.positiveFDR_eq`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#positive-fdr-eq).

## Law of a test's null and rejection pair

The law of one test's (null, rejected) pair in the two-groups model when the test rejects
iff its z-value lies in `Γ`.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.pairLaw`, a definition declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 520](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L520). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#pair-law).

## Storey's theorem in the two-groups model

Storey (2002), Theorem 1, in the two-groups model: for `m ≥ 1` i.i.d. tests rejecting on
`Γ`, `pFDR(Γ) = π₀ P₀(Γ) / P(Γ) = Fdr(Γ)`.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.TwoGroupsModel.positiveFDR_pairLaw_eq_tailFdr`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 525](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L525). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#positive-fdr-pair-law-eq-tail-fdr).

## Storey's estimator of the null proportion

Storey's estimator `π̂₀(t) = #{i | pᵢ > t} / (m (1 - t))` of the proportion of true nulls,
for a tuning parameter `t ∈ [0, 1)`.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.storeyPi0`, a definition declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 545](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#storey-pi0).

## Conservative bias of Storey's null proportion estimator

Conservative bias of Storey's (2002) estimator for a fixed set `H0` of true nulls: if their
p-values are valid, then `E[π̂₀(t)] ≥ m₀ / m` for every `t ∈ [0, 1)`. No independence is
assumed; the non-null p-values are arbitrary measurable functions.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.le_integral_storeyPi0`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#le-integral-storey-pi0).

## Storey's q-value

Storey's (2003) q-value for a nested family of rejection regions `Γ_s = {T ≤ s}` with
`pFDR(Γ_s) = pfdr s`: `q(t) = inf_{s ≥ t} pfdr s`, the smallest pFDR over the regions that
contain the observed statistic `t`.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.qValue`, a definition declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 591](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L591). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#q-value).

## q-value is at most the pFDR of the smallest region

The q-value is at most the pFDR of the smallest region containing the statistic.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.qValue_le`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 598](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L598). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#q-value-le).

## q-value is monotone in the statistic

The q-value is monotone in the statistic.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.monotone_qValue`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 602](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L602). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#monotone-q-value).

## q-value equals the pFDR when the pFDR is monotone

When the pFDR is nondecreasing along the nested regions, the q-value is the pFDR.

Formalized by `MathlibExt.Probability.Statistics.TwoGroupsTesting.qValue_eq_of_monotone`, a theorem declared in [MathlibExt/Probability/Statistics/TwoGroupsTesting.lean, line 608](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/TwoGroupsTesting.lean#L608). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html#q-value-eq-of-monotone).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Two-groups model and local false discovery rates](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/hypothesis-testing/two-groups-model-and-local-false-discovery-rates)
