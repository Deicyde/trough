---
declaration: theorem
origin: cited
lean: TauCeti.MeasureTheory.holderWith_preciseRepresentative_of_setAverage_norm_sub_le, TauCeti.MeasureTheory.holderOnWith_preciseRepresentative_restrict_of_setAverage_norm_sub_le, TauCeti.MeasureTheory.holderOnWith_preciseRepresentative_of_setAverage_norm_sub_le
statement: formalized
proof: formalized
---

# Campanato's theorem

Let `α > 0`, and let `f` be locally integrable, with mean oscillation
on every closed ball of radius `r > 0` at most `M r^α`. Then the precise representative of `f`
is `α`-Hölder continuous, with constant `2 · 2^α · 2ⁿ / (1 - 2^(-α)) · M`, where `n` is the
dimension. It agrees with `f` almost everywhere
(`TauCeti.MeasureTheory.ae_eq_preciseRepresentative`).

```lean
TauCeti.MeasureTheory.holderWith_preciseRepresentative_of_setAverage_norm_sub_le.{u_1, u_2}
  {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] {f : E → F} {α M : NNReal} (hα : 0 < α)
  (hf : MeasureTheory.LocallyIntegrable f μ)
  (hosc :
    ∀ (x : E) (r : ℝ),
      0 < r →
        ⨍ (y : E) in Metric.closedBall x r, ‖f y - ⨍ (z : E) in Metric.closedBall x r, f z ∂μ‖ ∂μ ≤
          ↑M * r ^ ↑α) :
  HolderWith ((2 * 2 ^ ↑α * (2 ^ Module.finrank ℝ E / (1 - 2 ^ (-↑α)))).toNNReal * M) α
    (TauCeti.MeasureTheory.preciseRepresentative μ f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The local Campanato estimate](the-local-campanato-estimate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MeasureTheory.holderWith_preciseRepresentative_of_setAverage_norm_sub_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Campanato.html#TauCeti.MeasureTheory.holderWith_preciseRepresentative_of_setAverage_norm_sub_le).

## Other forms

**Campanato's theorem on a set with the measure density property.** Formalized in Tau Ceti as [`TauCeti.MeasureTheory.holderOnWith_preciseRepresentative_restrict_of_setAverage_norm_sub_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Campanato.html#TauCeti.MeasureTheory.holderOnWith_preciseRepresentative_restrict_of_setAverage_norm_sub_le).

```lean
TauCeti.MeasureTheory.holderOnWith_preciseRepresentative_restrict_of_setAverage_norm_sub_le.{u_1,
    u_2}
  {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] {f : E → F} {Ω : Set E}
  {c α M : NNReal} (hα : 0 < α) (hc : 0 < c) (hf : MeasureTheory.LocallyIntegrable f (μ.restrict Ω))
  (hdens :
    ∀ x ∈ Ω,
      ∀ (r : ℝ),
        0 < r →
          ENNReal.ofReal r ≤ 2 * Metric.ediam Ω →
            ↑c * μ (Metric.closedBall x r) ≤ μ (Metric.closedBall x r ∩ Ω))
  (hosc :
    ∀ x ∈ Ω,
      ∀ (r : ℝ),
        0 < r →
          ENNReal.ofReal r ≤ 2 * Metric.ediam Ω →
            ⨍ (y : E) in Metric.closedBall x r,
                ‖f y - ⨍ (z : E) in Metric.closedBall x r, f z ∂μ.restrict Ω‖ ∂μ.restrict Ω ≤
              ↑M * r ^ ↑α) :
  HolderOnWith ((2 * 2 ^ ↑α * (2 ^ Module.finrank ℝ E / (↑c * (1 - 2 ^ (-↑α))))).toNNReal * M) α
    (TauCeti.MeasureTheory.preciseRepresentative (μ.restrict Ω) f) Ω
```

**Campanato's theorem on a set, below a fixed scale.** Formalized in Tau Ceti as [`TauCeti.MeasureTheory.holderOnWith_preciseRepresentative_of_setAverage_norm_sub_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Campanato.html#TauCeti.MeasureTheory.holderOnWith_preciseRepresentative_of_setAverage_norm_sub_le).

```lean
TauCeti.MeasureTheory.holderOnWith_preciseRepresentative_of_setAverage_norm_sub_le.{u_1, u_2}
  {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] {f : E → F} {M ρ : ℝ} {α : NNReal}
  {S : Set E} {B : ℝ} (hα : 0 < α) (hρ : 0 < ρ)
  (hf : ∀ x ∈ S, MeasureTheory.IntegrableOn f (Metric.closedBall x ρ) μ)
  (hosc :
    ∀ x ∈ S,
      ∀ (r : ℝ),
        0 < r →
          r ≤ ρ →
            ⨍ (y : E) in Metric.closedBall x r,
                ‖f y - ⨍ (z : E) in Metric.closedBall x r, f z ∂μ‖ ∂μ ≤
              M * r ^ ↑α)
  (havg : ∀ x ∈ S, ‖⨍ (y : E) in Metric.closedBall x ρ, f y ∂μ‖ ≤ B) :
  HolderOnWith
    (2 * 2 ^ ↑α * (2 ^ Module.finrank ℝ E / (1 - 2 ^ (-↑α)) * M + B * ρ ^ (-↑α))).toNNReal α
    (TauCeti.MeasureTheory.preciseRepresentative μ f) S
```

## Sources

- [Tau Ceti documentation: `TauCeti.MeasureTheory.holderWith_preciseRepresentative_of_setAverage_norm_sub_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Campanato.html#TauCeti.MeasureTheory.holderWith_preciseRepresentative_of_setAverage_norm_sub_le)
- [Source of `TauCeti.MeasureTheory.holderWith_preciseRepresentative_of_setAverage_norm_sub_le` in TauCeti/MeasureTheory/Function/Campanato.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/Campanato.lean#L609)
