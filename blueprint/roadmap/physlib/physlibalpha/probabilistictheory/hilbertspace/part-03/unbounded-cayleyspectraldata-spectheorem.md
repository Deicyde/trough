---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.cayleyRealSpectralMeasure_mem_domain, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_proj_left_restrict, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_proj_right_restrict, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.complexWeakIntegral_proj_left, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.complexWeakIntegral_proj_right, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.reconstruction_commutes_projection, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.complexWeakIntegral_one_sub, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_domain_factorization
statement: formalized
proof: formalized
---

# The spectral theorem for unbounded self-adjoint operators

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.CayleySpectralData.SpecTheorem`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean): 20 declarations, 2 with a docstring.

> The spectral theorem for unbounded self-adjoint operators via the Cayley transform.

## i. Overview

> The spectral measure on `ℝ` obtained from the Cayley transform of a self-adjoint operator `T`
> reconstructs `T`: its domain is the set of vectors `x` with `∫ λ² dμₓ < ∞`, and on it `⟪y, T x⟫ = ∫
> λ d⟪y, μ x⟫`. This is the spectral theorem for unbounded self-adjoint operators, and it also applies
> to the closure of an essentially self-adjoint operator.

## ii. Key results

> - `unboundedSpectralTheorem` : **the spectral theorem** for a self-adjoint operator.
> - `unboundedSpectralTheorem_of_essentiallySelfAdjoint` : the same for the closure of an essentially
>   self-adjoint operator.
> - `cayleyRealSpectralMeasure_eq_maximal` : the spectral measure has the maximal domain.

## iv. References

> * None.

**`ProbabilisticTheory.QuantumMechanics.cayleyRealSpectralMeasure_mem_domain`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L56).

```lean
lemma cayleyRealSpectralMeasure_mem_domain
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) (x : T.domain) :
    (x : H) ∈ spectralSquareMomentDomain
      (cayleyRealSpectralMeasure T hT)
```

## A. Restriction identities for PVM scalar measures

> These identities are independent of the Cayley transform.  They express the elementary fact
> that testing a projection-valued measure after applying one of its projections restricts the
> corresponding scalar measure.  They are the bookkeeping lemmas needed when a bounded spectral
> moment is localized to a measurable spectral set.

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_proj_left_restrict`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L158).

```lean
lemma WOTSpectralMeasure.scalarMeasure_proj_left_restrict
    {α : Type*} [MeasurableSpace α]
    (μ : QuantumMechanics.WOTSpectralMeasure α H) {S : Set α} (hS : MeasurableSet S)
    (x y : H) :
    μ.scalarMeasure (μ S x) y = (μ.scalarMeasure x y).restrict S
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_proj_right_restrict`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L172).

```lean
lemma WOTSpectralMeasure.scalarMeasure_proj_right_restrict
    {α : Type*} [MeasurableSpace α]
    (μ : QuantumMechanics.WOTSpectralMeasure α H) {S : Set α} (hS : MeasurableSet S)
    (x y : H) :
    μ.scalarMeasure x (μ S y) = (μ.scalarMeasure x y).restrict S
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.complexWeakIntegral_proj_left`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L207).

```lean
lemma WOTSpectralMeasure.complexWeakIntegral_proj_left
    {α : Type*} [MeasurableSpace α]
    (μ : QuantumMechanics.WOTSpectralMeasure α H) {S : Set α} (hS : MeasurableSet S)
    (g : α → ℂ) (x y : H)
    (_hgi : (μ.scalarMeasure x y).Integrable g) :
    μ.complexWeakIntegral g (μ S x) y =
      ∫ᵛ z, Set.indicator S g z ∂[ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ);
        μ.scalarMeasure x y]
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.complexWeakIntegral_proj_right`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L220).

```lean
lemma WOTSpectralMeasure.complexWeakIntegral_proj_right
    {α : Type*} [MeasurableSpace α]
    (μ : QuantumMechanics.WOTSpectralMeasure α H) {S : Set α} (hS : MeasurableSet S)
    (g : α → ℂ) (x y : H)
    (_hgi : (μ.scalarMeasure x y).Integrable g) :
    μ.complexWeakIntegral g x (μ S y) =
      ∫ᵛ z, Set.indicator S g z ∂[ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ);
        μ.scalarMeasure x y]
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.reconstruction_commutes_projection`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L233).

```lean
lemma WOTSpectralMeasure.reconstruction_commutes_projection
    {α : Type*} [MeasurableSpace α]
    (μ : QuantumMechanics.WOTSpectralMeasure α H) (U : H →L[ℂ] H)
    (f : α → ℂ)
    (hrec : ∀ x y, μ.complexWeakIntegral f x y = ⟪y, U x⟫_ℂ)
    (hfi : ∀ x y, (μ.scalarMeasure x y).Integrable f)
    {S : Set α} (hS : MeasurableSet S) :
    μ S * ContinuousLinearMapWOT.ofCLM U =
      ContinuousLinearMapWOT.ofCLM U * μ S
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.complexWeakIntegral_one_sub`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L275).

```lean
lemma WOTSpectralMeasure.complexWeakIntegral_one_sub
    (μ : QuantumMechanics.WOTSpectralMeasure ℂ H) (U : H →L[ℂ] H)
    (hrec : ∀ x y, μ.complexWeakIntegral id x y = ⟪y, U x⟫_ℂ)
    (hfi : ∀ x y, (μ.scalarMeasure x y).Integrable id)
    (hfinite : ∀ x y, IsFiniteMeasure (μ.scalarMeasure x y).variation) (x y : H) :
    μ.complexWeakIntegral (fun z => (1 : ℂ) - z) x y =
      ⟪y, x - U x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_domain_factorization`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L306).

```lean
lemma WOTSpectralMeasure.scalarMeasure_domain_factorization
    (μ : QuantumMechanics.WOTSpectralMeasure ℂ H) (U : H →L[ℂ] H)
    (hrec : ∀ x y, μ.complexWeakIntegral id x y = ⟪y, U x⟫_ℂ)
    (hfi : ∀ x y, (μ.scalarMeasure x y).Integrable id)
    (hfinite : ∀ x y, IsFiniteMeasure (μ.scalarMeasure x y).variation)
    (hcomm : ∀ {S : Set ℂ}, MeasurableSet S →
      μ S * ContinuousLinearMapWOT.ofCLM U =
        ContinuousLinearMapWOT.ofCLM U * μ S)
    (x v y : H) (hx : x = v - U v) {S : Set ℂ} (hS : MeasurableSet S) :
    μ.scalarMeasure x y S =
      μ.complexWeakIntegral (fun z => (1 : ℂ) - z) (μ S v) y
```

## B. Complex vector-measure density transport

> The scalar measures of a complex PVM are complex vector measures, rather than positive
> measures.  This is the reusable density-integral theorem needed by the inverse Cayley step.

**`ProbabilisticTheory.QuantumMechanics.VectorMeasure.integral_real_withDensity_mul`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L330).

```lean
lemma VectorMeasure.integral_real_withDensity_mul
    {α : Type*} [MeasurableSpace α] (μ : MeasureTheory.VectorMeasure α ℂ)
    {q : α → ℂ} (hq : μ.Integrable q) {g : α → ℝ}
    (hg : (μ.withDensity q (ContinuousLinearMap.mul ℝ ℂ)).Integrable g)
    (hvar0 : (μ.withDensity q (ContinuousLinearMap.mul ℝ ℂ)).variation =
      μ.variation.withDensity (fun x => ‖q x‖ₑ)) :
    ∫ᵛ x, g x ∂[ContinuousLinearMap.lsmul ℝ ℝ (E := ℂ);
        μ.withDensity q (ContinuousLinearMap.mul ℝ ℂ)] =
      ∫ᵛ x, (g x : ℂ) * q x ∂[ContinuousLinearMap.lsmul ℝ ℂ; μ]
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_eq_withDensity_one_sub`**, a lemma, [line 505](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L505).

```lean
lemma WOTSpectralMeasure.scalarMeasure_eq_withDensity_one_sub
    (μ : QuantumMechanics.WOTSpectralMeasure ℂ H) (U : H →L[ℂ] H)
    (hrec : ∀ x y, μ.complexWeakIntegral id x y = ⟪y, U x⟫_ℂ)
    (hfi : ∀ x y, (μ.scalarMeasure x y).Integrable id)
    (hfinite : ∀ x y, IsFiniteMeasure (μ.scalarMeasure x y).variation)
    (hcomm : ∀ {S : Set ℂ}, MeasurableSet S →
      μ S * ContinuousLinearMapWOT.ofCLM U =
        ContinuousLinearMapWOT.ofCLM U * μ S)
    (x v y : H) (hx : x = v - U v) :
    μ.scalarMeasure x y =
      (μ.scalarMeasure v y).withDensity (fun z => (1 : ℂ) - z)
        (ContinuousLinearMap.mul ℝ ℂ)
```

**`ProbabilisticTheory.QuantumMechanics.cayleyBoundedSpectralMeasure_commutes_operator`**, a lemma, [line 537](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L537).

```lean
lemma cayleyBoundedSpectralMeasure_commutes_operator
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T)
    {S : Set ℂ} (hS : MeasurableSet S) :
    cayleyBoundedSpectralMeasure T hT S *
        ContinuousLinearMapWOT.ofCLM (cayleyBoundedOperator T hT) =
      ContinuousLinearMapWOT.ofCLM (cayleyBoundedOperator T hT) *
        cayleyBoundedSpectralMeasure T hT S
```

**`ProbabilisticTheory.QuantumMechanics.cayleyBoundedSpectralMeasure_inverse_moment`**, a lemma, [line 553](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L553).

```lean
lemma cayleyBoundedSpectralMeasure_inverse_moment
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) :
    ∀ x : T.domain, ∀ y : H,
      ((cayleyBoundedSpectralMeasure T hT).scalarMeasure (x : H) y).Integrable
          cayleyInverse ∧
        ⟪y, T x⟫_ℂ =
          (cayleyBoundedSpectralMeasure T hT).weakIntegral
            cayleyInverse (x : H) y
```

## C. The inverse-moment transport lemma

> The bounded spectral measure of the Cayley transform reconstructs `z`. An integral identity for the
> inverse Cayley transform on the bounded measure transports to the real spectral measure.

**`ProbabilisticTheory.QuantumMechanics.cayleyRealSpectralMeasure_isWeakSpectralResolution_of_inverse_moment`**, a lemma, [line 722](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L722).

```lean
lemma cayleyRealSpectralMeasure_isWeakSpectralResolution_of_inverse_moment
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T)
    (hinv : ∀ x : T.domain, ∀ y : H,
      ((cayleyBoundedSpectralMeasure T hT).scalarMeasure (x : H) y).Integrable cayleyInverse ∧
        ⟪y, T x⟫_ℂ =
          (cayleyBoundedSpectralMeasure T hT).weakIntegral cayleyInverse (x : H) y) :
    IsWeakSpectralResolution T (cayleyRealSpectralMeasure T hT)
```

**`ProbabilisticTheory.QuantumMechanics.cayleyRealSpectralMeasure_isWeakSpectralResolution`**, a lemma, [line 752](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L752).

```lean
lemma cayleyRealSpectralMeasure_isWeakSpectralResolution
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) :
    IsWeakSpectralResolution T (cayleyRealSpectralMeasure T hT)
```

**`ProbabilisticTheory.QuantumMechanics.cayleySelfAdjointSpectralTheorem`**, a lemma, [line 758](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L758).

```lean
lemma cayleySelfAdjointSpectralTheorem
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) :
    SelfAdjointSpectralTheorem T (cayleyRealSpectralMeasure T hT)
```

**`ProbabilisticTheory.QuantumMechanics.cayleyRealSpectralMeasure_le_maximal`**, a lemma, [line 764](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L764).

```lean
lemma cayleyRealSpectralMeasure_le_maximal
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) :
    T ≤ QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral
      (cayleyRealSpectralMeasure T hT)
```

**`ProbabilisticTheory.QuantumMechanics.cayleyRealSpectralMeasure_eq_maximal`**, a lemma, [line 833](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L833).

```lean
lemma cayleyRealSpectralMeasure_eq_maximal
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) :
    maximalSpectralIntegral
        (cayleyRealSpectralMeasure T hT) = T
```

**`ProbabilisticTheory.QuantumMechanics.cayleyDomainAwareSelfAdjointSpectralTheorem`**, a lemma, [line 842](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L842).

```lean
lemma cayleyDomainAwareSelfAdjointSpectralTheorem
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) :
    DomainAwareSelfAdjointSpectralTheorem T (cayleyRealSpectralMeasure T hT)
```

**`ProbabilisticTheory.QuantumMechanics.unboundedSpectralTheorem`**, a lemma, [line 853](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L853).

> **The spectral theorem for unbounded self-adjoint operators.** A self-adjoint operator is the
> integral of the identity against its spectral measure, with domain the vectors of finite second
> moment.

```lean
lemma unboundedSpectralTheorem
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) :
    DomainAwareSelfAdjointSpectralTheorem T (cayleyRealSpectralMeasure T hT)
```

**`ProbabilisticTheory.QuantumMechanics.unboundedSpectralTheorem_of_essentiallySelfAdjoint`**, a lemma, [line 859](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean#L859).

> The spectral theorem for the closure of an essentially self-adjoint operator.

```lean
lemma unboundedSpectralTheorem_of_essentiallySelfAdjoint
    (T : H →ₗ.[ℂ] H) (hT : LinearPMap.IsEssentiallySelfAdjoint T) :
    DomainAwareSelfAdjointSpectralTheorem T.closure
      (cayleyRealSpectralMeasure T.closure hT)
```

## Depends on

- [The spectral measure of the Cayley transform](unbounded-cayleyspectraldata-basic.md)
- [Integrating unbounded functions against a spectral measure](unbounded-spectralintegral-construction.md)

## Proof depends on

- [The integral of the identity is self-adjoint](../part-04/unbounded-spectralintegral-spectheorem.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/SpecTheorem.lean)
