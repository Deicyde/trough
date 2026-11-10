---
declaration: theorem
origin: cited
lean: Besicovitch.ae_tendsto_average_closedBall, IsUnifLocDoublingMeasure.ae_tendsto_average_closedBall_norm_sub
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

## Sources

- [Tau Ceti documentation: `Besicovitch.ae_tendsto_average_closedBall`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Covering/Besicovitch.html#Besicovitch.ae_tendsto_average_closedBall)
- [Source of `Besicovitch.ae_tendsto_average_closedBall` in TauCeti/MeasureTheory/Covering/Besicovitch.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Covering/Besicovitch.lean#L134)
