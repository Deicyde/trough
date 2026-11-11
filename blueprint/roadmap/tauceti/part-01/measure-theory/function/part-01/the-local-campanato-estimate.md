---
declaration: theorem
origin: cited
lean: TauCeti.MeasureTheory.dist_preciseRepresentative_le_of_setAverage_norm_sub_le, TauCeti.MeasureTheory.dist_preciseRepresentative_restrict_le_of_setAverage_norm_sub_le
statement: formalized
proof: formalized
---

# The local Campanato estimate

Let `α > 0` and `d = dist x y`. If `f` has mean oscillation
at most `M r^α` on `closedBall x r` for `0 < r ≤ 2 d` and on `closedBall y r` for `0 < r ≤ d`,
and is integrable on `closedBall x (2 d)`, then the precise representatives of `f` at `x`
and `y` differ by at most `2 · 2^α · 2ⁿ / (1 - 2^(-α)) · M d^α`, where `n` is the dimension.

```lean
TauCeti.MeasureTheory.dist_preciseRepresentative_le_of_setAverage_norm_sub_le.{u_1, u_2}
  {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] {f : E → F} {x : E} {M α : ℝ} {y : E}
  (hα : 0 < α) (hf : MeasureTheory.IntegrableOn f (Metric.closedBall x (2 * dist x y)) μ)
  (hoscx :
    ∀ (r : ℝ),
      0 < r →
        r ≤ 2 * dist x y →
          ⨍ (z : E) in Metric.closedBall x r,
              ‖f z - ⨍ (w : E) in Metric.closedBall x r, f w ∂μ‖ ∂μ ≤
            M * r ^ α)
  (hoscy :
    ∀ (r : ℝ),
      0 < r →
        r ≤ dist x y →
          ⨍ (z : E) in Metric.closedBall y r,
              ‖f z - ⨍ (w : E) in Metric.closedBall y r, f w ∂μ‖ ∂μ ≤
            M * r ^ α) :
  dist (TauCeti.MeasureTheory.preciseRepresentative μ f x)
      (TauCeti.MeasureTheory.preciseRepresentative μ f y) ≤
    2 * 2 ^ α * (2 ^ Module.finrank ℝ E / (1 - 2 ^ (-α))) * (M * dist x y ^ α)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MeasureTheory.dist_preciseRepresentative_le_of_setAverage_norm_sub_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Campanato.html#TauCeti.MeasureTheory.dist_preciseRepresentative_le_of_setAverage_norm_sub_le).

## Other forms

**The local Campanato estimate on a set with the measure density property.** Formalized in Tau Ceti as [`TauCeti.MeasureTheory.dist_preciseRepresentative_restrict_le_of_setAverage_norm_sub_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Campanato.html#TauCeti.MeasureTheory.dist_preciseRepresentative_restrict_le_of_setAverage_norm_sub_le).

```lean
TauCeti.MeasureTheory.dist_preciseRepresentative_restrict_le_of_setAverage_norm_sub_le.{u_1, u_2}
  {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] {f : E → F} {Ω : Set E} {c : NNReal}
  {x : E} {M α : ℝ} {y : E} (hα : 0 < α) (hc : 0 < c)
  (hf : MeasureTheory.IntegrableOn f (Metric.closedBall x (2 * dist x y)) (μ.restrict Ω))
  (hdensx :
    ∀ (r : ℝ),
      0 < r → r ≤ 2 * dist x y → ↑c * μ (Metric.closedBall x r) ≤ μ (Metric.closedBall x r ∩ Ω))
  (hdensy :
    ∀ (r : ℝ),
      0 < r → r ≤ dist x y → ↑c * μ (Metric.closedBall y r) ≤ μ (Metric.closedBall y r ∩ Ω))
  (hoscx :
    ∀ (r : ℝ),
      0 < r →
        r ≤ 2 * dist x y →
          ⨍ (z : E) in Metric.closedBall x r,
              ‖f z - ⨍ (w : E) in Metric.closedBall x r, f w ∂μ.restrict Ω‖ ∂μ.restrict Ω ≤
            M * r ^ α)
  (hoscy :
    ∀ (r : ℝ),
      0 < r →
        r ≤ dist x y →
          ⨍ (z : E) in Metric.closedBall y r,
              ‖f z - ⨍ (w : E) in Metric.closedBall y r, f w ∂μ.restrict Ω‖ ∂μ.restrict Ω ≤
            M * r ^ α) :
  dist (TauCeti.MeasureTheory.preciseRepresentative (μ.restrict Ω) f x)
      (TauCeti.MeasureTheory.preciseRepresentative (μ.restrict Ω) f y) ≤
    2 * 2 ^ α * (2 ^ Module.finrank ℝ E / (↑c * (1 - 2 ^ (-α)))) * (M * dist x y ^ α)
```

## Sources

- [Tau Ceti documentation: `TauCeti.MeasureTheory.dist_preciseRepresentative_le_of_setAverage_norm_sub_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Campanato.html#TauCeti.MeasureTheory.dist_preciseRepresentative_le_of_setAverage_norm_sub_le)
- [Source of `TauCeti.MeasureTheory.dist_preciseRepresentative_le_of_setAverage_norm_sub_le` in TauCeti/MeasureTheory/Function/Campanato.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/Campanato.lean#L536)
