---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegralOfUniformApprox_inner, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.weakIntegral, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.complexWeakIntegral, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.weakIntegral_map, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.complexWeakIntegral_map, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConjSpectralMeasure_weakIntegral
statement: formalized
proof: formalized
---

# The vector-measure integral against a scalar matrix coefficient

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.WeakIntegral`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/WeakIntegral.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/WeakIntegral.lean): 6 declarations, 2 with a docstring.

> Weak integrals `∫ f d⟪y, μS(·) x⟫` of possibly unbounded functions against a spectral measure.

## i. Overview

> For a bounded multiplier `f`, testing the spectral integral against two vectors and integrating
> the scalar spectral measure give the same result:
> `⟪y, (∫ f dμS) x⟫ = ∫ f d(μS.scalarMeasure x y)`. The right-hand side makes sense for unbounded
> `f` as well, which gives the weak integrals `∫ f d⟪y, μS(·) x⟫` used to state `T = ∫ λ dE(λ)`
> vector by vector.

## ii. Key results

> - `weakIntegral`, `complexWeakIntegral` : `∫ f d⟪y, μS(·)x⟫`, for real- and complex-valued `f`.
> - `boundedIntegralOfUniformApprox_inner` : the weak integral of a bounded multiplier is the matrix
>   coefficient of its spectral integral.
> - `weakIntegral_map`, `complexWeakIntegral_map` : weak integrals against a pushforward measure.
> - `unitaryConjSpectralMeasure_weakIntegral` : compatibility with unitary transport.

## iv. References

> * None.

## A. Bounded integrals agree with the vector-measure integral

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegralOfUniformApprox_inner`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/WeakIntegral.lean#L64).

```lean
lemma boundedIntegralOfUniformApprox_inner
    [Nonempty α]
    {f : α → ℂ} {s : ℕ → SimpleFunc α ℂ}
    (hs : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖s n x - f x‖ < ε)
    (hsBound : ∃ C : ℝ, ∀ n x, ‖s n x‖ ≤ C)
    (x y : H)
    (hfinite : IsFiniteMeasure (μS.scalarMeasure x y).variation) :
    ⟪y, boundedIntegralOfUniformApprox μS f s hs x⟫_ℂ =
      ∫ᵛ z, f z ∂[ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ);
        μS.scalarMeasure x y]
```

## B. The weak integral of a possibly-unbounded multiplier

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.weakIntegral`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/WeakIntegral.lean#L133).

> The pairing is real-scalar multiplication on the complex scalar measure.

```lean
def weakIntegral (f : α → ℝ) (x y : H) : ℂ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.complexWeakIntegral`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/WeakIntegral.lean#L140).

> The complex weak integral of a complex-valued spectral multiplier. The real-valued integral
> above is retained for the self-adjoint reconstruction API; this companion is the bounded-unitary
> side of the Cayley construction.

```lean
def complexWeakIntegral (f : α → ℂ) (x y : H) : ℂ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.weakIntegral_map`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/WeakIntegral.lean#L144).

```lean
lemma weakIntegral_map {β : Type*} [MeasurableSpace β]
    (f : α → β) (hf : Measurable f) (g : β → ℝ)
    (x y : H) (hgm : AEStronglyMeasurable g ((μS.scalarMeasure x y).variation.map f))
    (hgi : (μS.scalarMeasure x y).Integrable (g ∘ f)) :
    (μS.map f hf).weakIntegral g x y = μS.weakIntegral (g ∘ f) x y
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.complexWeakIntegral_map`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/WeakIntegral.lean#L153).

```lean
lemma complexWeakIntegral_map {β : Type*} [MeasurableSpace β]
    (f : α → β) (hf : Measurable f) (g : β → ℂ)
    (x y : H) (hgm : AEStronglyMeasurable g ((μS.scalarMeasure x y).variation.map f))
    (hgi : (μS.scalarMeasure x y).Integrable (g ∘ f)) :
    (μS.map f hf).complexWeakIntegral g x y =
      μS.complexWeakIntegral (g ∘ f) x y
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConjSpectralMeasure_weakIntegral`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/WeakIntegral.lean#L163).

```lean
lemma unitaryConjSpectralMeasure_weakIntegral
    {H' : Type*} [NormedAddCommGroup H'] [InnerProductSpace ℂ H'] [CompleteSpace H']
    (u : H ≃ₗᵢ[ℂ] H') (μS : WOTSpectralMeasure α H) (f : α → ℝ) (x y : H') :
    (unitaryConjSpectralMeasure u μS).weakIntegral f x y =
      μS.weakIntegral f (u.symm x) (u.symm y)
```

## Depends on

- [Integrating bounded functions against a spectral measure](unbounded-boundedintegral.md)
- [Transporting spectral measures along unitaries](unbounded-conjugation.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/WeakIntegral.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/WeakIntegral.lean)
