---
declaration: theorem
origin: cited
lean: LipschitzOnWith.lintegral_hausdorffMeasure_inter_preimage_le, LipschitzOnWith.exists_measurable_hausdorffMeasure_inter_preimage_le
statement: formalized
proof: formalized
---

# Eilenberg's inequality, integral form

for `f` `K`-Lipschitz on `A` with values in an
`m`-dimensional real normed space with additive Haar measure `μ`, and `t` real,
`∫⁻ y, μH[t] (A ∩ f ⁻¹' {y}) ∂μ ≤ μ (ball 0 1) * K ^ m * μH[m + t] A`.

The fiber-measure function `y ↦ μH[t] (A ∩ f ⁻¹' {y})` need not be measurable, and for a
non-measurable integrand `∫⁻` is the *lower* Lebesgue integral (the supremum of the integrals of
the measurable functions below it). So this bounds the lower integral of the fiber measures. The
upper-integral form is `LipschitzOnWith.exists_measurable_hausdorffMeasure_inter_preimage_le`: a
measurable `G` dominating the fiber measures with
`∫⁻ y, G y ∂μ ≤ μ (ball 0 1) * K ^ m * μH[m + t] A`.

```lean
LipschitzOnWith.lintegral_hausdorffMeasure_inter_preimage_le.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [EMetricSpace X] [NormedAddCommGroup Y] [NormedSpace ℝ Y] [FiniteDimensional ℝ Y]
  [MeasurableSpace Y] [BorelSpace Y] (μ : MeasureTheory.Measure Y) [μ.IsAddHaarMeasure] {K : NNReal}
  {f : X → Y} {A : Set X} {t : ℝ} [MeasurableSpace X] [BorelSpace X] (hf : LipschitzOnWith K f A) :
  ∫⁻ (y : Y), (MeasureTheory.Measure.hausdorffMeasure t) (A ∩ f ⁻¹' {y}) ∂μ ≤
    μ (Metric.ball 0 1) * ↑K ^ Module.finrank ℝ Y *
      (MeasureTheory.Measure.hausdorffMeasure (↑(Module.finrank ℝ Y) + t)) A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LipschitzOnWith.lintegral_hausdorffMeasure_inter_preimage_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Coarea/Eilenberg.html#LipschitzOnWith.lintegral_hausdorffMeasure_inter_preimage_le).

## Other forms

**Eilenberg's inequality, in its strong form.** Formalized in Tau Ceti as [`LipschitzOnWith.exists_measurable_hausdorffMeasure_inter_preimage_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Coarea/Eilenberg.html#LipschitzOnWith.exists_measurable_hausdorffMeasure_inter_preimage_le).

```lean
LipschitzOnWith.exists_measurable_hausdorffMeasure_inter_preimage_le.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [EMetricSpace X] [NormedAddCommGroup Y] [NormedSpace ℝ Y] [FiniteDimensional ℝ Y]
  [MeasurableSpace Y] [BorelSpace Y] (μ : MeasureTheory.Measure Y) [μ.IsAddHaarMeasure] {K : NNReal}
  {f : X → Y} {A : Set X} {t : ℝ} [MeasurableSpace X] [BorelSpace X] (hf : LipschitzOnWith K f A) :
  ∃ G,
    Measurable G ∧
      (∀ (y : Y), (MeasureTheory.Measure.hausdorffMeasure t) (A ∩ f ⁻¹' {y}) ≤ G y) ∧
        ∫⁻ (y : Y), G y ∂μ ≤
          μ (Metric.ball 0 1) * ↑K ^ Module.finrank ℝ Y *
            (MeasureTheory.Measure.hausdorffMeasure (↑(Module.finrank ℝ Y) + t)) A
```

## Sources

- [Tau Ceti documentation: `LipschitzOnWith.lintegral_hausdorffMeasure_inter_preimage_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Coarea/Eilenberg.html#LipschitzOnWith.lintegral_hausdorffMeasure_inter_preimage_le)
- [Source of `LipschitzOnWith.lintegral_hausdorffMeasure_inter_preimage_le` in TauCeti/MeasureTheory/Function/Coarea/Eilenberg.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/Coarea/Eilenberg.lean#L216)
