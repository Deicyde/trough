---
declaration: theorem
origin: cited
lean: TauCeti.exists_norm_laplacian_heatKernel_convolution_le
statement: formalized
proof: formalized
---

# Hölder bound on the Laplacian of a heat convolution

The Laplacian of the heat convolution
of a bounded `α`-Hölder function with constant `H` is `O(H τ^((α - 2)/2))`, uniformly in the
function.

```lean
TauCeti.exists_norm_laplacian_heatKernel_convolution_le.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [MeasurableSpace E] [BorelSpace E] [CompleteSpace F] {α : NNReal} :
  ∃ C ≥ 0,
    ∀ {g : E → F} {M τ : ℝ} {H : NNReal},
      MeasureTheory.AEStronglyMeasurable g MeasureTheory.volume →
        (∀ᵐ (y : E), ‖g y‖ ≤ M) →
          HolderWith H α g →
            0 < τ →
              ∀ (x : E),
                ‖Laplacian.laplacian
                      (MeasureTheory.convolution (TauCeti.heatKernel τ) g
                        (ContinuousLinearMap.lsmul ℝ ℝ) MeasureTheory.volume)
                      x‖ ≤
                  C * ↑H * τ ^ ((↑α - 2) / 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder bounds on the derivatives of a heat convolution](holder-bounds-on-the-derivatives-of-a-heat-convo.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_norm_laplacian_heatKernel_convolution_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/HeatEquation.html#TauCeti.exists_norm_laplacian_heatKernel_convolution_le).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_norm_laplacian_heatKernel_convolution_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/HeatEquation.html#TauCeti.exists_norm_laplacian_heatKernel_convolution_le)
- [Source of `TauCeti.exists_norm_laplacian_heatKernel_convolution_le` in TauCeti/Analysis/PDE/HeatKernel/HeatEquation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/HeatKernel/HeatEquation.lean#L252)
