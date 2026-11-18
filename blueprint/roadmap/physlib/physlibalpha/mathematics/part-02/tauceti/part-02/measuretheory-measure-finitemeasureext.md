---
declaration: module
origin: cited
lean: TauCeti.MeasureTheory.ext_of_forall_mem_submonoid_integral_eq_of_polish, TauCeti.MeasureTheory.abs_integral_mulExpNegMulSq_comp_sub_le_of_isTightMeasureSet, TauCeti.MeasureTheory.integral_eq_of_forall_mem_subalgebra_integral_eq_of_isTightMeasureSet, TauCeti.MeasureTheory.ext_of_forall_mem_subalgebra_integral_eq_of_innerRegular
statement: formalized
proof: formalized
---

# Finite measures are determined by separating test functions

The module `PhyslibAlpha.Mathematics.TauCeti.MeasureTheory.Measure.FiniteMeasureExt`, [PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Measure/FiniteMeasureExt.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Measure/FiniteMeasureExt.lean): 4 declarations, 4 with a docstring; 2 private, not shown.

> Two finite Borel measures on a Polish space are equal once their integrals agree on a family of real
> bounded continuous functions that separates points, contains the constant `1` and is closed under
> multiplication.

## i. Overview

> Two finite Borel measures on a Polish space are equal once their integrals agree on a family of
> real bounded continuous functions that separates points, contains the constant `1` and is closed
> under multiplication.
>
> This criterion applies when the known integrals are moments of a multiplicative family, such as
> coordinate monomials or graph homomorphism densities. The constant `1` ensures that the measures
> have the same total mass.
>
> Without metrizability, a point-separating star subalgebra of bounded continuous functions still
> determines the integrals of all bounded continuous functions against *tight* finite measures on a
> Hausdorff space. On a locally compact Hausdorff space it therefore determines finite inner regular
> (Radon) measures. Some regularity is needed there: a non-regular Borel measure on a non-metrizable
> compact space can integrate every continuous function like a point mass. This is the form needed
> on the Pontryagin dual of a locally compact abelian group that is not second countable.
>
> **Implementation notes.** The tight case adapts the proofs of Jakob Stiefel's
> `dist_integral_mulExpNegMulSq_comp_le` and
> `ext_of_forall_mem_subalgebra_integral_eq_of_pseudoEMetric_complete_countable` in Mathlib, which
> get their compact sets of almost full measure from complete separable metrizability. Here the
> compact sets come from tightness instead, and Hausdorffness makes them measurable. The passage to
> measures is Mathlib's uniqueness theorem `Measure.ext_of_integral_eq_on_compactlySupported` for
> regular measures.

## ii. Key results

> * `TauCeti.MeasureTheory.ext_of_forall_mem_submonoid_integral_eq_of_polish` — two finite Borel
>   measures on a Polish space with the same integrals on a point-separating submonoid of
>   `E →ᵇ ℝ` are equal.
> * `TauCeti.MeasureTheory.abs_integral_mulExpNegMulSq_comp_sub_le_of_isTightMeasureSet` — the `6 √ε`
>   comparison estimate behind the tight case.
> * `TauCeti.MeasureTheory.integral_eq_of_forall_mem_subalgebra_integral_eq_of_isTightMeasureSet` —
>   two tight finite measures on a Hausdorff space with the same integrals on a
>   point-separating star subalgebra of `E →ᵇ 𝕜` give the same integral to every real bounded
>   continuous function.
> * `TauCeti.MeasureTheory.ext_of_forall_mem_subalgebra_integral_eq_of_innerRegular` — on a locally
>   compact Hausdorff space, two finite inner regular measures with the same integrals on such a
>   subalgebra are equal.

## iv. References

> * Standard material; the statements and proofs are original to this formalization.

## A. Development

**`TauCeti.MeasureTheory.ext_of_forall_mem_submonoid_integral_eq_of_polish`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Measure/FiniteMeasureExt.lean#L87).

> **A separating submonoid of test functions determines a finite measure.** Two finite Borel
> measures on a Polish space that give the same integral to every member of a submonoid `S` of the
> real bounded continuous functions are equal, provided the members of `S` separate points.

```lean
lemma ext_of_forall_mem_submonoid_integral_eq_of_polish [PolishSpace E] [BorelSpace E]
    {P P' : Measure E} [IsFiniteMeasure P] [IsFiniteMeasure P'] {S : Submonoid (E →ᵇ ℝ)}
    (hS : ∀ ⦃x y : E⦄, x ≠ y → ∃ g ∈ S, g x ≠ g y)
    (heq : ∀ g ∈ S, ∫ x, g x ∂P = ∫ x, g x ∂P') : P = P'
```

**`TauCeti.MeasureTheory.abs_integral_mulExpNegMulSq_comp_sub_le_of_isTightMeasureSet`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Measure/FiniteMeasureExt.lean#L171).

> If two tight finite measures on a Hausdorff space integrate every member of a point-separating
> real subalgebra `A` of `E →ᵇ ℝ` equally, then their integrals of `mulExpNegMulSq ε ∘ f` differ by
> at most `6 √ε`. This is the tight form of Mathlib's `dist_integral_mulExpNegMulSq_comp_le`, which
> assumes a complete second-countable pseudo-metric space instead.

```lean
lemma abs_integral_mulExpNegMulSq_comp_sub_le_of_isTightMeasureSet
    (hP : IsTightMeasureSet {P}) (hP' : IsTightMeasureSet {P'}) (f : E →ᵇ ℝ)
    {A : Subalgebra ℝ (E →ᵇ ℝ)} (hA : (A.map (toContinuousMapₐ ℝ)).SeparatesPoints)
    (heq : ∀ g ∈ A, ∫ x, (g : E → ℝ) x ∂P = ∫ x, (g : E → ℝ) x ∂P') {ε : ℝ} (hε : 0 < ε) :
    |∫ x, mulExpNegMulSq ε (f x) ∂P - ∫ x, mulExpNegMulSq ε (f x) ∂P'| ≤ 6 * √ε
```

**`TauCeti.MeasureTheory.integral_eq_of_forall_mem_subalgebra_integral_eq_of_isTightMeasureSet`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Measure/FiniteMeasureExt.lean#L224).

> **A separating subalgebra determines the integrals of tight measures.** Two tight finite
> measures on a Hausdorff space that integrate every member of a point-separating star
> subalgebra `A` of `E →ᵇ 𝕜` equally give the same integral to every real bounded continuous
> function.

```lean
lemma integral_eq_of_forall_mem_subalgebra_integral_eq_of_isTightMeasureSet {𝕜 : Type*} [RCLike 𝕜]
    (hP : IsTightMeasureSet {P}) (hP' : IsTightMeasureSet {P'})
    {A : StarSubalgebra 𝕜 (E →ᵇ 𝕜)} (hA : (A.map (toContinuousMapStarₐ 𝕜)).SeparatesPoints)
    (heq : ∀ g ∈ A, ∫ x, (g : E → 𝕜) x ∂P = ∫ x, (g : E → 𝕜) x ∂P') (f : E →ᵇ ℝ) :
    ∫ x, f x ∂P = ∫ x, f x ∂P'
```

**`TauCeti.MeasureTheory.ext_of_forall_mem_subalgebra_integral_eq_of_innerRegular`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Measure/FiniteMeasureExt.lean#L278).

> **A separating subalgebra determines a finite inner regular measure.** On a locally compact
> Hausdorff space, two finite inner regular (equivalently, for finite Borel measures there, regular)
> measures that integrate every member of a point-separating star subalgebra `A` of `E →ᵇ 𝕜`
> equally are equal. Unlike
> `MeasureTheory.ext_of_forall_mem_subalgebra_integral_eq_of_polish`, no metrizability or
> countability is assumed.

```lean
lemma ext_of_forall_mem_subalgebra_integral_eq_of_innerRegular {𝕜 : Type*} [RCLike 𝕜]
    [BorelSpace E] [LocallyCompactSpace E] [P.InnerRegular] [P'.InnerRegular]
    {A : StarSubalgebra 𝕜 (E →ᵇ 𝕜)} (hA : (A.map (toContinuousMapStarₐ 𝕜)).SeparatesPoints)
    (heq : ∀ g ∈ A, ∫ x, (g : E → 𝕜) x ∂P = ∫ x, (g : E → 𝕜) x ∂P') : P = P'
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Measure/FiniteMeasureExt.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Measure/FiniteMeasureExt.lean)
