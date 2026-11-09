---
declaration: theorem
origin: cited
lean: TauCeti.lintegral_mul_le_of_inv_add_inv_eq, TauCeti.MeasureTheory.abs_integral_mul_le_eLpNorm_mul_eLpNorm_mul_measureReal_rpow
statement: formalized
proof: formalized
---

# Hölder's inequality for Young's exponents

Let `1 ≤ p ≤ q` and let `r` be the exponent with
`1/p + 1/r = 1 + 1/q`. Then
`∫⁻ k g ≤ (∫⁻ k ^ r g ^ p) ^ (1/q) (∫⁻ k ^ r) ^ (1 - 1/p) (∫⁻ g ^ p) ^ (1/p - 1/q)`.

This is Hölder's inequality with the three exponents `1/q`, `1 - 1/p` and `1/p - 1/q`, which add
up to `1`, applied to the factorization
`k g = (k ^ r g ^ p) ^ (1/q) (k ^ r) ^ (1 - 1/p) (g ^ p) ^ (1/p - 1/q)`.

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

**Hölder's inequality for a function vanishing off a set.** Formalized in Tau Ceti as [`TauCeti.MeasureTheory.abs_integral_mul_le_eLpNorm_mul_eLpNorm_mul_measureReal_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Bochner/Holder.html#TauCeti.MeasureTheory.abs_integral_mul_le_eLpNorm_mul_eLpNorm_mul_measureReal_rpow).

```lean
TauCeti.MeasureTheory.abs_integral_mul_le_eLpNorm_mul_eLpNorm_mul_measureReal_rpow.{u_1}
  {Ω : Type u_1} [MeasurableSpace Ω] {μ : MeasureTheory.Measure Ω} {f w : Ω → ℝ} {r s : NNReal}
  (hr : 0 < r) (hs : 0 < s) (hrs : (↑r)⁻¹ + (↑s)⁻¹ ≤ 1) (hf : MeasureTheory.MemLp f (↑r) μ)
  (hw : MeasureTheory.MemLp w (↑s) μ) {A : Set Ω} (hA : MeasurableSet A) (hAfin : μ A ≠ ⊤)
  (hwA : ∀ᵐ (x : Ω) ∂μ, x ∉ A → w x = 0) :
  |∫ (x : Ω), f x * w x ∂μ| ≤
    (MeasureTheory.eLpNorm f (↑r) μ).toReal * (MeasureTheory.eLpNorm w (↑s) μ).toReal *
      μ.real A ^ (1 - (↑r)⁻¹ - (↑s)⁻¹)
```

## Sources

- [Tau Ceti documentation: `TauCeti.lintegral_mul_le_of_inv_add_inv_eq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MeanInequalities.html#TauCeti.lintegral_mul_le_of_inv_add_inv_eq)
- [Source of `TauCeti.lintegral_mul_le_of_inv_add_inv_eq` in TauCeti/MeasureTheory/Integral/MeanInequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Integral/MeanInequalities.lean#L45)
