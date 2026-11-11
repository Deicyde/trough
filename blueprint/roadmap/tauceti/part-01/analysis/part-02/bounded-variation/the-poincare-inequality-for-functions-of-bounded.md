---
declaration: theorem
origin: cited
lean: TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_totalVariationOn_of_eq_ball, TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_totalVariationOn_of_convex, TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_totalVariationOn
statement: formalized
proof: formalized
---

# The Poincaré inequality for functions of bounded variation on a ball

A function locally
integrable on a ball of radius `R` in a space of dimension `n` deviates from its mean over the
ball in `L¹` by at most `2 ^ (n + 1) R` times its total variation on the ball. The constant is
proportional to `R`, as the scaling of both sides forces.

```lean
TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_totalVariationOn_of_eq_ball.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {Ω : TopologicalSpace.Opens E}
  {u : E → ℝ} {c : E} {R : ℝ} (hΩ : ↑Ω = Metric.ball c R)
  (hu : MeasureTheory.LocallyIntegrableOn u (Metric.ball c R) μ) :
  ∫⁻ (x : E) in Metric.ball c R, ‖u x - ⨍ (y : E) in Metric.ball c R, u y ∂μ‖ₑ ∂μ ≤
    ENNReal.ofReal (2 ^ (Module.finrank ℝ E + 1) * R) * TauCeti.totalVariationOn μ Ω u
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_totalVariationOn_of_eq_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Poincare.html#TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_totalVariationOn_of_eq_ball).

## Other forms

**The Poincaré inequality for functions of bounded variation on a bounded convex set.** Formalized in Tau Ceti as [`TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_totalVariationOn_of_convex`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Poincare.html#TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_totalVariationOn_of_convex).

```lean
TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_totalVariationOn_of_convex.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {Ω : TopologicalSpace.Opens E}
  {u : E → ℝ} {S : Set E} (hconv : Convex ℝ ↑Ω) (hb : Bornology.IsBounded ↑Ω)
  (hu : MeasureTheory.LocallyIntegrableOn u (↑Ω) μ) (hS : S ⊆ ↑Ω) (hS₀ : μ S ≠ 0) :
  ∫⁻ (x : E) in ↑Ω, ‖u x - ⨍ (y : E) in S, u y ∂μ‖ₑ ∂μ ≤
    ENNReal.ofReal
        (μ.real (Metric.ball 0 1) * Metric.diam ↑Ω ^ (Module.finrank ℝ E + 1) / μ.real S) *
      TauCeti.totalVariationOn μ Ω u
```

**The Poincaré inequality for functions of bounded variation on a convex set.** Formalized in Tau Ceti as [`TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_totalVariationOn`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Poincare.html#TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_totalVariationOn).

```lean
TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_totalVariationOn.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {Ω : TopologicalSpace.Opens E}
  {u : E → ℝ} {S : Set E} (hconv : Convex ℝ ↑Ω) (hu : MeasureTheory.LocallyIntegrableOn u (↑Ω) μ)
  (hS : S ⊆ ↑Ω) (hS₀ : μ S ≠ 0) (hS_top : μ S ≠ ⊤) :
  ∫⁻ (x : E) in ↑Ω, ‖u x - ⨍ (y : E) in S, u y ∂μ‖ₑ ∂μ ≤
    (∫⁻ (h : E) in ↑Ω - ↑Ω, ‖h‖ₑ ∂μ) / μ S * TauCeti.totalVariationOn μ Ω u
```

## Sources

- [Tau Ceti documentation: `TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_totalVariationOn_of_eq_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Poincare.html#TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_totalVariationOn_of_eq_ball)
- [Source of `TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_totalVariationOn_of_eq_ball` in TauCeti/Analysis/BoundedVariation/Poincare.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/BoundedVariation/Poincare.lean#L251)
