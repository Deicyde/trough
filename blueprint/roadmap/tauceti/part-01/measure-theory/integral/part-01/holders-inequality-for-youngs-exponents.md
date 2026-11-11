---
declaration: theorem
origin: cited
lean: TauCeti.lintegral_mul_le_of_inv_add_inv_eq, TauCeti.MeasureTheory.norm_integral_smul_le_eLpNorm_mul_eLpNorm_mul_measureReal_rpow
statement: formalized
proof: formalized
---

# Hölder's inequality for Young's exponents

Let `1 ≤ p ≤ q` and let `r` be the exponent with
`1/p + 1/r = 1 + 1/q`. Then
`∫⁻ k g ≤ (∫⁻ k ^ r g ^ p) ^ (1/q) (∫⁻ k ^ r) ^ (1 - 1/p) (∫⁻ g ^ p) ^ (1/p - 1/q)`.

```lean
TauCeti.lintegral_mul_le_of_inv_add_inv_eq.{u_1} {β : Type u_1} [MeasurableSpace β]
  {ν : MeasureTheory.Measure β} {k g : β → ENNReal} (hk : AEMeasurable k ν) (hg : AEMeasurable g ν)
  {p q r : ℝ} (hp : 1 ≤ p) (hpq : p ≤ q) (hr : p⁻¹ + r⁻¹ = 1 + q⁻¹) :
  ∫⁻ (y : β), k y * g y ∂ν ≤
    (∫⁻ (y : β), k y ^ r * g y ^ p ∂ν) ^ q⁻¹ * (∫⁻ (y : β), k y ^ r ∂ν) ^ (1 - p⁻¹) *
      (∫⁻ (y : β), g y ^ p ∂ν) ^ (p⁻¹ - q⁻¹)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.lintegral_mul_le_of_inv_add_inv_eq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MeanInequalities.html#TauCeti.lintegral_mul_le_of_inv_add_inv_eq).

## Other forms

**Hölder's inequality for a function vanishing off a set.** Formalized in Tau Ceti as [`TauCeti.MeasureTheory.norm_integral_smul_le_eLpNorm_mul_eLpNorm_mul_measureReal_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Bochner/Holder.html#TauCeti.MeasureTheory.norm_integral_smul_le_eLpNorm_mul_eLpNorm_mul_measureReal_rpow).

```lean
TauCeti.MeasureTheory.norm_integral_smul_le_eLpNorm_mul_eLpNorm_mul_measureReal_rpow.{u_1, u_2, u_3}
  {Ω : Type u_1} {𝕜 : Type u_2} {E : Type u_3} [MeasurableSpace Ω] {μ : MeasureTheory.Measure Ω}
  [NormedRing 𝕜] [NormedAddCommGroup E] [NormedSpace ℝ E] [MulActionWithZero 𝕜 E]
  [IsBoundedSMul 𝕜 E] {f : Ω → 𝕜} {w : Ω → E} {r s : NNReal} (hr : 0 < r) (hs : 0 < s)
  (hrs : (↑r)⁻¹ + (↑s)⁻¹ ≤ 1) (hf : MeasureTheory.MemLp f (↑r) μ)
  (hw : MeasureTheory.MemLp w (↑s) μ) {A : Set Ω} (hAfin : μ A ≠ ⊤)
  (hwA : ∀ᵐ (x : Ω) ∂μ, x ∉ A → w x = 0) :
  ‖∫ (x : Ω), f x • w x ∂μ‖ ≤
    (MeasureTheory.eLpNorm f (↑r) μ).toReal * (MeasureTheory.eLpNorm w (↑s) μ).toReal *
      μ.real A ^ (1 - (↑r)⁻¹ - (↑s)⁻¹)
```

## Sources

- [Tau Ceti documentation: `TauCeti.lintegral_mul_le_of_inv_add_inv_eq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MeanInequalities.html#TauCeti.lintegral_mul_le_of_inv_add_inv_eq)
- [Source of `TauCeti.lintegral_mul_le_of_inv_add_inv_eq` in TauCeti/MeasureTheory/Integral/MeanInequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/MeanInequalities.lean#L45)
