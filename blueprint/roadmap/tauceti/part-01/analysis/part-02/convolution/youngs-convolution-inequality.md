---
declaration: theorem
origin: cited
lean: MeasureTheory.eLpNorm_convolution_le_of_inv_add_inv_eq, MeasureTheory.eLpNorm_lconvolution_le
statement: formalized
proof: formalized
---

# Young's convolution inequality

**Young's convolution inequality** for the convolution `f ⋆[L, μ] g` along a continuous
bilinear map `L`: for `1 ≤ p, r ≤ ∞` and `1/p + 1/r = 1 + 1/q`,
`‖f ⋆[L, μ] g‖_q ≤ ‖L‖ ‖f‖_p ‖g‖_r`. Where the integral defining the convolution does not
converge, its value is `0`, so no integrability hypothesis is needed.

```lean
MeasureTheory.eLpNorm_convolution_le_of_inv_add_inv_eq.{u_1, u_2, u_3, u_4, u_5} {G : Type u_1}
  {mG : MeasurableSpace G} [AddCommGroup G] [MeasurableAdd₂ G] [MeasurableNeg G]
  {μ : MeasureTheory.Measure G} [MeasureTheory.SFinite μ] [μ.IsAddLeftInvariant] [μ.IsNegInvariant]
  {𝕜 : Type u_2} {E : Type u_3} {E' : Type u_4} {F : Type u_5} [NontriviallyNormedField 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup E'] [NormedSpace 𝕜 E']
  [NormedAddCommGroup F] [NormedSpace ℝ F] [NormedSpace 𝕜 F] (L : E →L[𝕜] E' →L[𝕜] F) {f : G → E}
  {g : G → E'} {p q r : ENNReal} (hp : 1 ≤ p) (hr : 1 ≤ r) (hpqr : p⁻¹ + r⁻¹ = 1 + q⁻¹)
  (hf : MeasureTheory.AEStronglyMeasurable f μ) (hg : MeasureTheory.AEStronglyMeasurable g μ) :
  MeasureTheory.eLpNorm (MeasureTheory.convolution f g L μ) q μ ≤
    ‖L‖ₑ * MeasureTheory.eLpNorm f p μ * MeasureTheory.eLpNorm g r μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Young's inequality for integral kernels](../../../measure-theory/integral/part-02/youngs-inequality-for-integral-kernels.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.eLpNorm_convolution_le_of_inv_add_inv_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Convolution/Young.html#MeasureTheory.eLpNorm_convolution_le_of_inv_add_inv_eq).

## Other forms

**Young's convolution inequality.** Formalized in Tau Ceti as [`MeasureTheory.eLpNorm_lconvolution_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Convolution/Young.html#MeasureTheory.eLpNorm_lconvolution_le).

```lean
MeasureTheory.eLpNorm_lconvolution_le.{u_1} {G : Type u_1} {mG : MeasurableSpace G} [AddCommGroup G]
  [MeasurableAdd₂ G] [MeasurableNeg G] {μ : MeasureTheory.Measure G} [MeasureTheory.SFinite μ]
  [μ.IsAddLeftInvariant] [μ.IsNegInvariant] {f g : G → ENNReal} {p q r : ENNReal} (hp : 1 ≤ p)
  (hr : 1 ≤ r) (hpqr : p⁻¹ + r⁻¹ = 1 + q⁻¹) (hf : AEMeasurable f μ) (hg : AEMeasurable g μ) :
  MeasureTheory.eLpNorm (MeasureTheory.lconvolution f g μ) q μ ≤
    MeasureTheory.eLpNorm f p μ * MeasureTheory.eLpNorm g r μ
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.eLpNorm_convolution_le_of_inv_add_inv_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Convolution/Young.html#MeasureTheory.eLpNorm_convolution_le_of_inv_add_inv_eq)
- [Source of `MeasureTheory.eLpNorm_convolution_le_of_inv_add_inv_eq` in TauCeti/Analysis/Convolution/Young.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Convolution/Young.lean#L337)
