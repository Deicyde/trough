---
declaration: theorem
origin: cited
lean: TauCeti.ae_tendsto_setLAverage_dyadicCube, IsUnifLocDoublingMeasure.ae_tendsto_average_closedBall_norm_sub, Besicovitch.ae_tendsto_average_closedBall
statement: formalized
proof: formalized
---

# Lebesgue's differentiation theorem along dyadic cubes

for an integrable `g`, at almost
every `x` the averages of `g` over the dyadic cubes containing `x` converge to `g x` as the level
tends to `-∞`.

```lean
TauCeti.ae_tendsto_setLAverage_dyadicCube.{u_1} {ι : Type u_1} [Fintype ι] {g : (ι → ℝ) → ENNReal}
  (hg : AEMeasurable g MeasureTheory.volume) (hg' : ∫⁻ (x : ι → ℝ), g x ≠ ⊤) :
  ∀ᵐ (x : ι → ℝ),
    Filter.Tendsto (fun k => ⨍⁻ (y : ι → ℝ) in TauCeti.dyadicCube k (TauCeti.dyadicIndex k x), g y)
      Filter.atBot (nhds (g x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ae_tendsto_setLAverage_dyadicCube`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/DyadicCube.html#TauCeti.ae_tendsto_setLAverage_dyadicCube).

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

**Lebesgue's differentiation theorem for a locally finite measure in a space with the Besicovitch covering property.** Formalized in Tau Ceti as [`Besicovitch.ae_tendsto_average_closedBall`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Covering/Besicovitch.html#Besicovitch.ae_tendsto_average_closedBall).

```lean
Besicovitch.ae_tendsto_average_closedBall.{u_1, u_2} {β : Type u_1} {F : Type u_2} [MetricSpace β]
  [MeasurableSpace β] [BorelSpace β] [SecondCountableTopology β] [HasBesicovitchCovering β]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] (μ : MeasureTheory.Measure β)
  [MeasureTheory.IsLocallyFiniteMeasure μ] {f : β → F} (hf : MeasureTheory.LocallyIntegrable f μ) :
  ∀ᵐ (x : β) ∂μ,
    Filter.Tendsto (fun r => ⨍ (y : β) in Metric.closedBall x r, f y ∂μ) (nhdsWithin 0 (Set.Ioi 0))
      (nhds (f x))
```

## Sources

- [Tau Ceti documentation: `TauCeti.ae_tendsto_setLAverage_dyadicCube`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/DyadicCube.html#TauCeti.ae_tendsto_setLAverage_dyadicCube)
- [Source of `TauCeti.ae_tendsto_setLAverage_dyadicCube` in TauCeti/MeasureTheory/Measure/Lebesgue/DyadicCube.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Measure/Lebesgue/DyadicCube.lean#L208)
