---
declaration: theorem
origin: cited
lean: Besicovitch.ae_tendsto_average_closedBall, IsUnifLocDoublingMeasure.ae_tendsto_average_closedBall_norm_sub, IsUnifLocDoublingMeasure.ae_tendsto_setLAverage_closedBall, MeasureTheory.Measure.ae_tendsto_setLAverage_ball
statement: formalized
proof: formalized
---

# Lebesgue's differentiation theorem

**Lebesgue's differentiation theorem** for a locally finite measure in a space with the
Besicovitch covering property: for a locally integrable function `f`, at almost every point `x`
the averages of `f` over the closed balls around `x` tend to `f x`.

```lean
Besicovitch.ae_tendsto_average_closedBall.{u_1, u_2} {β : Type u_1} {F : Type u_2} [MetricSpace β]
  [MeasurableSpace β] [BorelSpace β] [SecondCountableTopology β] [HasBesicovitchCovering β]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] (μ : MeasureTheory.Measure β)
  [MeasureTheory.IsLocallyFiniteMeasure μ] {f : β → F} (hf : MeasureTheory.LocallyIntegrable f μ) :
  ∀ᵐ (x : β) ∂μ,
    Filter.Tendsto (fun r => ⨍ (y : β) in Metric.closedBall x r, f y ∂μ) (nhdsWithin 0 (Set.Ioi 0))
      (nhds (f x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Besicovitch.ae_tendsto_average_closedBall`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Covering/Besicovitch.html#Besicovitch.ae_tendsto_average_closedBall).

## Other forms

**Lebesgue differentiation theorem along concentric closed balls.** Formalized in Tau Ceti as [`IsUnifLocDoublingMeasure.ae_tendsto_average_closedBall_norm_sub`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Covering/DensityTheorem.html#IsUnifLocDoublingMeasure.ae_tendsto_average_closedBall_norm_sub).

```lean
IsUnifLocDoublingMeasure.ae_tendsto_average_closedBall_norm_sub.{u_1, u_2} {α : Type u_1}
  {E : Type u_2} [PseudoMetricSpace α] [MeasurableSpace α] (μ : MeasureTheory.Measure α)
  [IsUnifLocDoublingMeasure μ] [SecondCountableTopology α] [BorelSpace α]
  [MeasureTheory.IsLocallyFiniteMeasure μ] [NormedAddCommGroup E] {f : α → E}
  (hf : MeasureTheory.LocallyIntegrable f μ) :
  ∀ᵐ (x : α) ∂μ,
    Filter.Tendsto (fun r => ⨍ (y : α) in Metric.closedBall x r, ‖f y - f x‖ ∂μ)
      (nhdsWithin 0 (Set.Ioi 0)) (nhds 0)
```

**Lebesgue differentiation theorem along concentric closed balls, for `ℝ≥0∞`-valued functions.** Formalized in Tau Ceti as [`IsUnifLocDoublingMeasure.ae_tendsto_setLAverage_closedBall`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Covering/DensityTheorem.html#IsUnifLocDoublingMeasure.ae_tendsto_setLAverage_closedBall).

```lean
IsUnifLocDoublingMeasure.ae_tendsto_setLAverage_closedBall.{u_1} {α : Type u_1}
  [PseudoMetricSpace α] [MeasurableSpace α] (μ : MeasureTheory.Measure α)
  [IsUnifLocDoublingMeasure μ] [SecondCountableTopology α] [BorelSpace α]
  [MeasureTheory.IsLocallyFiniteMeasure μ] {f : α → ENNReal} (hf : AEMeasurable f μ)
  (hfin : ∫⁻ (x : α), f x ∂μ ≠ ⊤) :
  ∀ᵐ (x : α) ∂μ,
    Filter.Tendsto (fun r => ⨍⁻ (y : α) in Metric.closedBall x r, f y ∂μ) (nhdsWithin 0 (Set.Ioi 0))
      (nhds (f x))
```

**Lebesgue differentiation theorem along concentric open balls, for an additive Haar measure.** Formalized in Tau Ceti as [`MeasureTheory.Measure.ae_tendsto_setLAverage_ball`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Covering/DensityTheorem.html#MeasureTheory.Measure.ae_tendsto_setLAverage_ball).

```lean
MeasureTheory.Measure.ae_tendsto_setLAverage_ball.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  (μ : MeasureTheory.Measure E) [μ.IsAddHaarMeasure] {f : E → ENNReal} (hf : AEMeasurable f μ)
  (hfin : ∫⁻ (x : E), f x ∂μ ≠ ⊤) :
  ∀ᵐ (x : E) ∂μ,
    Filter.Tendsto (fun r => ⨍⁻ (y : E) in Metric.ball x r, f y ∂μ) (nhdsWithin 0 (Set.Ioi 0))
      (nhds (f x))
```

## Sources

- [Tau Ceti documentation: `Besicovitch.ae_tendsto_average_closedBall`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Covering/Besicovitch.html#Besicovitch.ae_tendsto_average_closedBall)
- [Source of `Besicovitch.ae_tendsto_average_closedBall` in TauCeti/MeasureTheory/Covering/Besicovitch.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Covering/Besicovitch.lean#L134)
