---
declaration: theorem
origin: cited
lean: TauCeti.HasWeakFDerivOn.lintegral_ofReal_map_norm_fderiv_convolution_le
statement: formalized
proof: formalized
---

# Jensen's bound for the gradient of a mollification

If `U` is a weak derivative field of
`u` on the whole space and `rho` is a smooth compactly supported probability kernel, then
`∫ Φ(‖D(u ⋆ rho)‖) ≤ ∫ Φ(‖U‖)` for every `Φ` convex and monotone on `[0, ∞)`, in extended
nonnegative form.

```lean
TauCeti.HasWeakFDerivOn.lintegral_ofReal_map_norm_fderiv_convolution_le.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [MeasurableSpace E] [NormedAddCommGroup E] [NormedSpace ℝ E] [BorelSpace E]
  [NormedAddCommGroup F] [NormedSpace ℝ F] {mu : MeasureTheory.Measure E} [mu.IsAddLeftInvariant]
  [MeasureTheory.SFinite mu] [SecondCountableTopology E] [mu.IsNegInvariant] {u : E → F}
  {U : E → E →L[ℝ] F} (h : TauCeti.HasWeakFDerivOn mu ⊤ u U)
  (hu : MeasureTheory.LocallyIntegrable u mu) (hU : MeasureTheory.LocallyIntegrable U mu)
  {Φ : ℝ → ℝ} (hΦ : ConvexOn ℝ (Set.Ici 0) Φ) (hΦm : MonotoneOn Φ (Set.Ici 0)) {rho : E → ℝ}
  (hrho : ContDiff ℝ (↑⊤) rho) (hrho_cpt : HasCompactSupport rho) (hrho0 : 0 ≤ᵐ[mu] rho)
  (hrho1 : ∫ (x : E), rho x ∂mu = 1) :
  ∫⁻ (x : E),
      ENNReal.ofReal
        (Φ
          ‖fderiv ℝ (MeasureTheory.convolution u rho (ContinuousLinearMap.lsmul ℝ ℝ).flip mu)
              x‖) ∂mu ≤
    ∫⁻ (x : E), ENNReal.ofReal (Φ ‖U x‖) ∂mu
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jensen's inequality for convolution](../../other-results/jensens-inequality-for-convolution.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HasWeakFDerivOn.lintegral_ofReal_map_norm_fderiv_convolution_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Mollification/Basic.html#TauCeti.HasWeakFDerivOn.lintegral_ofReal_map_norm_fderiv_convolution_le).

## Sources

- [Tau Ceti documentation: `TauCeti.HasWeakFDerivOn.lintegral_ofReal_map_norm_fderiv_convolution_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Mollification/Basic.html#TauCeti.HasWeakFDerivOn.lintegral_ofReal_map_norm_fderiv_convolution_le)
- [Source of `TauCeti.HasWeakFDerivOn.lintegral_ofReal_map_norm_fderiv_convolution_le` in TauCeti/Analysis/Sobolev/Mollification/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/Mollification/Basic.lean#L135)
