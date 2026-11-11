---
declaration: theorem
origin: cited
lean: TauCeti.integral_divergenceCLM_mul_eq_neg_integral_inner_polarDensity
statement: formalized
proof: formalized
---

# The polar decomposition `Du = σ_u |Du|`

For `u` locally integrable on `Ω` with locally
finite variation, `∫ u div φ dμ = -∫ ⟪φ, σ_u⟫ d|Du|` for every test vector field `φ` on `Ω`.

```lean
TauCeti.integral_divergenceCLM_mul_eq_neg_integral_inner_polarDensity.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ : MeasureTheory.Measure E} {Ω : TopologicalSpace.Opens E} {u : E → ℝ}
  (hu : MeasureTheory.LocallyIntegrableOn u (↑Ω) μ)
  (hfin : ∀ (K : Set E), IsCompact K → K ⊆ ↑Ω → ∃ U, K ⊆ ↑U ∧ TauCeti.totalVariationOn μ U u ≠ ⊤)
  (φ : TestFunction Ω E ⊤) :
  ∫ (x : E), (TestFunction.divergenceCLM φ) x * u x ∂μ =
    -∫ (x : ↥Ω), inner ℝ (φ ↑x) (TauCeti.polarDensity μ Ω u x) ∂TauCeti.variationMeasure μ Ω u
```

## Depends on

- [TauCeti.variationMeasure](tauceti-variationmeasure.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_divergenceCLM_mul_eq_neg_integral_inner_polarDensity`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/PolarDecomposition.html#TauCeti.integral_divergenceCLM_mul_eq_neg_integral_inner_polarDensity).

## Sources

- [Tau Ceti documentation: `TauCeti.integral_divergenceCLM_mul_eq_neg_integral_inner_polarDensity`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/PolarDecomposition.html#TauCeti.integral_divergenceCLM_mul_eq_neg_integral_inner_polarDensity)
- [Source of `TauCeti.integral_divergenceCLM_mul_eq_neg_integral_inner_polarDensity` in TauCeti/Analysis/BoundedVariation/PolarDecomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/BoundedVariation/PolarDecomposition.lean#L229)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
