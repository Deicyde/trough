---
declaration: theorem
origin: cited
lean: TauCeti.integral_divergenceCLM_mul_eq_neg_integral_inner_acDerivativeDensity_sub_singularPart
statement: formalized
proof: formalized
---

# Lebesgue decomposition of the BV derivative

The distributional derivative is the sum
of the density `acDerivativeDensity μ Ω u ν` against `ν` and the polar field against the singular
part of `|Du|`. Both pairings are integrable because the test field has compact support.

```lean
TauCeti.integral_divergenceCLM_mul_eq_neg_integral_inner_acDerivativeDensity_sub_singularPart.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {μ : MeasureTheory.Measure E} {Ω : TopologicalSpace.Opens E}
  {u : E → ℝ} (hu : MeasureTheory.LocallyIntegrableOn u (↑Ω) μ)
  (hfin : ∀ (K : Set E), IsCompact K → K ⊆ ↑Ω → ∃ U, K ⊆ ↑U ∧ TauCeti.totalVariationOn μ U u ≠ ⊤)
  (ν : MeasureTheory.Measure ↥Ω) [MeasureTheory.SigmaFinite ν] (φ : TestFunction Ω E ⊤) :
  ∫ (x : E), (TestFunction.divergenceCLM φ) x * u x ∂μ =
    -∫ (x : ↥Ω), inner ℝ (φ ↑x) (TauCeti.acDerivativeDensity μ Ω u ν x) ∂ν -
      ∫ (x : ↥Ω),
        inner ℝ (φ ↑x)
          (TauCeti.polarDensity μ Ω u x) ∂(TauCeti.variationMeasure μ Ω u).singularPart ν
```

## Depends on

- [TauCeti.totalVariationOn](../../part-01/geometric-measure-theory-rectifiability-bv-and-f/tauceti-totalvariationon.md)

## Proof depends on

- [The directional derivatives of a function of locally finite variation are signed Radon measures](../../part-01/geometric-measure-theory-rectifiability-bv-and-f/the-directional-derivatives-of-a-function-of-loc.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_divergenceCLM_mul_eq_neg_integral_inner_acDerivativeDensity_sub_singularPart`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/LebesgueDecomposition.html#TauCeti.integral_divergenceCLM_mul_eq_neg_integral_inner_acDerivativeDensity_sub_singularPart).

## Sources

- [Tau Ceti documentation: `TauCeti.integral_divergenceCLM_mul_eq_neg_integral_inner_acDerivativeDensity_sub_singularPart`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/LebesgueDecomposition.html#TauCeti.integral_divergenceCLM_mul_eq_neg_integral_inner_acDerivativeDensity_sub_singularPart)
- [Source of `TauCeti.integral_divergenceCLM_mul_eq_neg_integral_inner_acDerivativeDensity_sub_singularPart` in TauCeti/Analysis/BoundedVariation/LebesgueDecomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/BoundedVariation/LebesgueDecomposition.lean#L137)
