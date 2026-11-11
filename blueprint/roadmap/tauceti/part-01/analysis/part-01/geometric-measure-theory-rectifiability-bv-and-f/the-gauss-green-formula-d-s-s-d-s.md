---
declaration: theorem
origin: cited
lean: TauCeti.integral_trace_fderiv_mul_indicator_eq_integral_inner_outerNormal
statement: formalized
proof: formalized
---

# The Gauss–Green formula, `Dχ_s = -ν_s |Dχ_s|`

For a set `s` of locally finite perimeter
in `Ω`, the outer normal `ν_s` represents the distributional derivative of the indicator against
the perimeter measure: `∫_s div φ dμ = ∫ ⟪φ, ν_s⟫ d|Dχ_s|` for every `C¹` vector field `φ` with
compact support in `Ω`, where `div φ = tr (Dφ)`.

```lean
TauCeti.integral_trace_fderiv_mul_indicator_eq_integral_inner_outerNormal.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ : MeasureTheory.Measure E} {Ω : TopologicalSpace.Opens E} {s : Set E}
  (hu : MeasureTheory.LocallyIntegrableOn (s.indicator 1) (↑Ω) μ)
  (hfin :
    ∀ (K : Set E),
      IsCompact K → K ⊆ ↑Ω → ∃ U, K ⊆ ↑U ∧ TauCeti.totalVariationOn μ U (s.indicator 1) ≠ ⊤)
  {φ : E → E} (hφ : ContDiff ℝ 1 φ) (hc : HasCompactSupport φ) (hs : tsupport φ ⊆ ↑Ω) :
  ∫ (x : E), (LinearMap.trace ℝ E) ↑(fderiv ℝ φ x) * s.indicator 1 x ∂μ =
    ∫ (y : ↥Ω),
      inner ℝ (φ ↑y) (TauCeti.outerNormal μ Ω s ↑y) ∂TauCeti.variationMeasure μ Ω (s.indicator 1)
```

## Depends on

- [TauCeti.outerNormal](tauceti-outernormal.md)
- [TauCeti.variationMeasure](tauceti-variationmeasure.md)

## Proof depends on

- [Lebesgue's differentiation theorem](../../../measure-theory/other-results/lebesgues-differentiation-theorem.md)
- [The polar decomposition `Du = σ_u |Du|`](the-polar-decomposition-du-u-du.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_trace_fderiv_mul_indicator_eq_integral_inner_outerNormal`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/ReducedBoundary.html#TauCeti.integral_trace_fderiv_mul_indicator_eq_integral_inner_outerNormal).

## Sources

- [Tau Ceti documentation: `TauCeti.integral_trace_fderiv_mul_indicator_eq_integral_inner_outerNormal`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/ReducedBoundary.html#TauCeti.integral_trace_fderiv_mul_indicator_eq_integral_inner_outerNormal)
- [Source of `TauCeti.integral_trace_fderiv_mul_indicator_eq_integral_inner_outerNormal` in TauCeti/Analysis/BoundedVariation/ReducedBoundary.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/BoundedVariation/ReducedBoundary.lean#L272)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
