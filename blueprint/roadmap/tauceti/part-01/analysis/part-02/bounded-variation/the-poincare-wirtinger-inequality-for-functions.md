---
declaration: theorem
origin: cited
lean: TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_measure_rpow_mul_totalVariationOn_of_convex
statement: formalized
proof: formalized
---

# The Poincaré–Wirtinger inequality for functions of bounded variation, localized to a subset

Let `Ω` be a bounded convex open set in a finite-dimensional real inner product space of
dimension `n`, and let `S ⊆ Ω` have positive measure. For every `u` locally integrable on `Ω`
and every `A ⊆ Ω`, the integral over `A` of the deviation of `u` from its mean over `S` is at most
`μ(B(0, 1)) ^ (1 - 1/n) * (diam Ω) ^ n / μ(S) * μ(A) ^ (1/n)` times the total variation
`|Du|(Ω)`, finite or infinite.

```lean
TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_measure_rpow_mul_totalVariationOn_of_convex.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure]
  {Ω : TopologicalSpace.Opens E} {u : E → ℝ} {S A : Set E} (hΩc : Convex ℝ ↑Ω)
  (hb : Bornology.IsBounded ↑Ω) (hu : MeasureTheory.LocallyIntegrableOn u (↑Ω) μ) (hS : S ⊆ ↑Ω)
  (hS₀ : μ S ≠ 0) (hA : A ⊆ ↑Ω) :
  ∫⁻ (x : E) in A, ‖u x - ⨍ (y : E) in S, u y ∂μ‖ₑ ∂μ ≤
    ENNReal.ofReal
          (μ.real (Metric.ball 0 1) ^ (1 - (↑(Module.finrank ℝ E))⁻¹) *
              Metric.diam ↑Ω ^ Module.finrank ℝ E /
            μ.real S) *
        μ A ^ (↑(Module.finrank ℝ E))⁻¹ *
      TauCeti.totalVariationOn μ Ω u
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Poincaré inequality for functions of bounded variation on a ball](the-poincare-inequality-for-functions-of-bounded.md)
- [The Poincaré–Wirtinger inequality on a ball](../../part-03/sobolev/part-02/the-poincare-wirtinger-inequality-on-a-ball.md)
- [Rademacher's theorem for locally Lipschitz functions](../calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_measure_rpow_mul_totalVariationOn_of_convex`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Poincare.html#TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_measure_rpow_mul_totalVariationOn_of_convex).

## Sources

- [Tau Ceti documentation: `TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_measure_rpow_mul_totalVariationOn_of_convex`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Poincare.html#TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_measure_rpow_mul_totalVariationOn_of_convex)
- [Source of `TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_measure_rpow_mul_totalVariationOn_of_convex` in TauCeti/Analysis/BoundedVariation/Poincare.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/BoundedVariation/Poincare.lean#L445)
