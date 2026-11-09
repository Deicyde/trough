---
declaration: theorem
origin: cited
lean: MeasureTheory.lintegral_lconvolution_sq_le
statement: formalized
proof: formalized
---

# Young's inequality `L¹ ⋆ L² ⊆ L²`

For extended nonnegative functions on a group with a
left-invariant measure, `∫⁻ (f ⋆ₗ[μ] g) ^ 2 ≤ (∫⁻ f) ^ 2 * ∫⁻ g ^ 2`.

```lean
MeasureTheory.lintegral_lconvolution_sq_le.{u_1} {G : Type u_1} {mG : MeasurableSpace G}
  [AddGroup G] [MeasurableAdd₂ G] [MeasurableNeg G] {μ : MeasureTheory.Measure G}
  [MeasureTheory.SFinite μ] [μ.IsAddLeftInvariant] {f g : G → ENNReal} (hf : AEMeasurable f μ)
  (hg : AEMeasurable g μ) :
  ∫⁻ (x : G), MeasureTheory.lconvolution f g μ x ^ 2 ∂μ ≤
    (∫⁻ (y : G), f y ∂μ) ^ 2 * ∫⁻ (x : G), g x ^ 2 ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.lintegral_lconvolution_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Convolution/Young.html#MeasureTheory.lintegral_lconvolution_sq_le).

## Sources

- [Tau Ceti documentation: `MeasureTheory.lintegral_lconvolution_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Convolution/Young.html#MeasureTheory.lintegral_lconvolution_sq_le)
- [Source of `MeasureTheory.lintegral_lconvolution_sq_le` in TauCeti/Analysis/Convolution/Young.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Convolution/Young.lean#L71)
