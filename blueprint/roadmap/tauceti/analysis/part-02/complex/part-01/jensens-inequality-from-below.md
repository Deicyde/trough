---
declaration: theorem
origin: cited
lean: AnalyticOnNhd.le_circleAverage_log_norm, ConvexOn.ofReal_map_norm_convolution_le_lintegral
statement: formalized
proof: formalized
---

# Jensen's inequality from below

If `f` is analytic on the closed disc of radius `|r|`
about `c`, with `r ≠ 0`, the circle average of `log ‖f‖` is at least `k * log r + log ‖τ‖`, where
`k` is the order of `f` at `c` and `τ` its trailing coefficient there.

This is Jensen's formula `MeromorphicOn.circleAverage_log_norm` with the contributions of the zeros
other than `c` dropped, each of which is nonnegative.

```lean
AnalyticOnNhd.le_circleAverage_log_norm {f : ℂ → ℂ} {c : ℂ} {r : ℝ}
  (hf : AnalyticOnNhd ℂ f (Metric.closedBall c |r|)) (hr : r ≠ 0) :
  ↑(analyticOrderNatAt f c) * Real.log r + Real.log ‖meromorphicTrailingCoeffAt f c‖ ≤
    Real.circleAverage (fun z => Real.log ‖f z‖) c r
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AnalyticOnNhd.le_circleAverage_log_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RadialUniqueness.html#AnalyticOnNhd.le_circleAverage_log_norm).

## Other forms

**Jensen's inequality for convolution.** Formalized in Tau Ceti as [`ConvexOn.ofReal_map_norm_convolution_le_lintegral`](https://taucetiproject.org/docs/TauCeti/Analysis/Convolution/Jensen.html#ConvexOn.ofReal_map_norm_convolution_le_lintegral).

```lean
ConvexOn.ofReal_map_norm_convolution_le_lintegral.{u_1, u_2} {G : Type u_1} {F : Type u_2}
  [MeasurableSpace G] [AddGroup G] [MeasurableAdd₂ G] [MeasurableNeg G]
  {μ : MeasureTheory.Measure G} [MeasureTheory.SFinite μ] [μ.IsAddRightInvariant]
  [NormedAddCommGroup F] [NormedSpace ℝ F] {Φ : ℝ → ℝ} {ρ : G → ℝ} (hΦ : ConvexOn ℝ (Set.Ici 0) Φ)
  (hΦm : MonotoneOn Φ (Set.Ici 0)) (hρ0 : 0 ≤ᵐ[μ] ρ) (hρ1 : ∫ (t : G), ρ t ∂μ = 1) {g : G → F}
  (hg : MeasureTheory.AEStronglyMeasurable g μ) (x : G) :
  ENNReal.ofReal (Φ ‖MeasureTheory.convolution ρ g (ContinuousLinearMap.lsmul ℝ ℝ) μ x‖) ≤
    ∫⁻ (t : G), ENNReal.ofReal (ρ t) * ENNReal.ofReal (Φ ‖g (x - t)‖) ∂μ
```

## Sources

- [Tau Ceti documentation: `AnalyticOnNhd.le_circleAverage_log_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RadialUniqueness.html#AnalyticOnNhd.le_circleAverage_log_norm)
- [Source of `AnalyticOnNhd.le_circleAverage_log_norm` in TauCeti/Analysis/Complex/RadialUniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/RadialUniqueness.lean#L74)
