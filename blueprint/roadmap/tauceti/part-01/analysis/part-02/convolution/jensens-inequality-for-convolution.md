---
declaration: theorem
origin: cited
lean: ConvexOn.ofReal_map_norm_convolution_le_lintegral
statement: formalized
proof: formalized
---

# Jensen's inequality for convolution

If `Φ` is convex and monotone on `[0, ∞)` and `ρ`
is a probability kernel, then at every point `Φ(‖(ρ ⋆ g)(x)‖) ≤ ∫ ρ(t) Φ(‖g(x - t)‖) dt`, in
extended nonnegative form.

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

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ConvexOn.ofReal_map_norm_convolution_le_lintegral`](https://taucetiproject.org/docs/TauCeti/Analysis/Convolution/Jensen.html#ConvexOn.ofReal_map_norm_convolution_le_lintegral).

## Sources

- [Tau Ceti documentation: `ConvexOn.ofReal_map_norm_convolution_le_lintegral`](https://taucetiproject.org/docs/TauCeti/Analysis/Convolution/Jensen.html#ConvexOn.ofReal_map_norm_convolution_le_lintegral)
- [Source of `ConvexOn.ofReal_map_norm_convolution_le_lintegral` in TauCeti/Analysis/Convolution/Jensen.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Convolution/Jensen.lean#L80)
