---
declaration: theorem
origin: cited
lean: TauCeti.norm_iteratedFDeriv_heatKernel_convolution_le_of_holderWith
statement: formalized
proof: formalized
---

# Hölder bounds on the derivatives of a heat convolution

If `g` is bounded and `α`-Hölder
with constant `H`, then for `m ≥ 1` and `t > 0`,
`‖D^m (K_t ⋆ g)(x)‖ ≤ H ∫ ‖D^m K_t(z)‖ ‖z‖^α dz`. By
`TauCeti.exists_integral_norm_iteratedFDeriv_heatKernel_mul_rpow_le` the right side is
`O(H t^((α - m) / 2))`, which for `m = 2` is integrable in time near `t = 0` when `α > 0`.

```lean
TauCeti.norm_iteratedFDeriv_heatKernel_convolution_le_of_holderWith.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [NormedAddCommGroup F] [NormedSpace ℝ F] {g : E → F} {M t : ℝ} [MeasurableSpace E] [BorelSpace E]
  [CompleteSpace F] (ht : 0 < t) (hg : MeasureTheory.AEStronglyMeasurable g MeasureTheory.volume)
  (hM : ∀ᵐ (y : E), ‖g y‖ ≤ M) {H α : NNReal} (hH : HolderWith H α g) {m : ℕ} (hm : m ≠ 0) (x : E) :
  ‖iteratedFDeriv ℝ m
        (MeasureTheory.convolution (TauCeti.heatKernel t) g (ContinuousLinearMap.lsmul ℝ ℝ)
          MeasureTheory.volume)
        x‖ ≤
    ↑H * ∫ (z : E), ‖iteratedFDeriv ℝ m (TauCeti.heatKernel t) z‖ * ‖z‖ ^ ↑α
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_iteratedFDeriv_heatKernel_convolution_le_of_holderWith`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/HeatEquation.html#TauCeti.norm_iteratedFDeriv_heatKernel_convolution_le_of_holderWith).

## Sources

- [Tau Ceti documentation: `TauCeti.norm_iteratedFDeriv_heatKernel_convolution_le_of_holderWith`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/HeatEquation.html#TauCeti.norm_iteratedFDeriv_heatKernel_convolution_le_of_holderWith)
- [Source of `TauCeti.norm_iteratedFDeriv_heatKernel_convolution_le_of_holderWith` in TauCeti/Analysis/PDE/HeatKernel/HeatEquation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/HeatKernel/HeatEquation.lean#L236)
