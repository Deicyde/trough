---
declaration: theorem
origin: cited
lean: MeasureTheory.lintegral_lconvolution_sq_le, MeasureTheory.eLpNorm_convolution_le
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

## Proof depends on

- [Minkowski's integral inequality](../../../measure-theory/integral/part-02/minkowskis-integral-inequality.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.lintegral_lconvolution_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Convolution/Young.html#MeasureTheory.lintegral_lconvolution_sq_le).

## Other forms

**Young's inequality for convolution with an integrable function.** Formalized in Tau Ceti as [`MeasureTheory.eLpNorm_convolution_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Convolution/Young.html#MeasureTheory.eLpNorm_convolution_le).

```lean
MeasureTheory.eLpNorm_convolution_le.{u_1, u_2, u_3, u_4, u_5} {𝕜 : Type u_1} {G : Type u_2}
  {E : Type u_3} {E' : Type u_4} {F : Type u_5} [NontriviallyNormedField 𝕜] [NormedAddCommGroup E]
  [NormedSpace 𝕜 E] [NormedAddCommGroup E'] [NormedSpace 𝕜 E'] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] [NormedSpace ℝ F] (L : E →L[𝕜] E' →L[𝕜] F) {f : G → E} {g : G → E'} [AddGroup G]
  [MeasurableSpace G] [MeasurableAdd₂ G] [MeasurableNeg G] {μ : MeasureTheory.Measure G}
  [MeasureTheory.SigmaFinite μ] [μ.IsAddRightInvariant]
  (hf : MeasureTheory.AEStronglyMeasurable f μ) (hg : MeasureTheory.AEStronglyMeasurable g μ)
  {p : ENNReal} (hp : 1 ≤ p) :
  MeasureTheory.eLpNorm (MeasureTheory.convolution f g L μ) p μ ≤
    ‖L‖ₑ * MeasureTheory.eLpNorm f 1 μ * MeasureTheory.eLpNorm g p μ
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.lintegral_lconvolution_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Convolution/Young.html#MeasureTheory.lintegral_lconvolution_sq_le)
- [Source of `MeasureTheory.lintegral_lconvolution_sq_le` in TauCeti/Analysis/Convolution/Young.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Convolution/Young.lean#L127)
