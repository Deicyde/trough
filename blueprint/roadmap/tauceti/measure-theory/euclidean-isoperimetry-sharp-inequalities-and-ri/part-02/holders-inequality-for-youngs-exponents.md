---
declaration: theorem
origin: cited
lean: TauCeti.lintegral_mul_le_of_inv_add_inv_eq, TauCeti.enorm_integral_inner_le, TauCeti.enorm_integral_mul_le, TauCeti.MeasureTheory.abs_integral_mul_le_eLpNorm_mul_eLpNorm_mul_measureReal_rpow, TauCeti.rpow_lintegral_le_measure_univ_rpow_mul
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

**Hölder's inequality for the integral of an inner product.** Formalized in Tau Ceti as [`TauCeti.enorm_integral_inner_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/Duality.html#TauCeti.enorm_integral_inner_le).

```lean
TauCeti.enorm_integral_inner_le.{u_1, u_4, u_5} {α : Type u_1} {mα : MeasurableSpace α}
  {μ : MeasureTheory.Measure α} {𝕜 : Type u_4} {H : Type u_5} [RCLike 𝕜] [NormedAddCommGroup H]
  [InnerProductSpace 𝕜 H] {p q : ENNReal} [p.HolderConjugate q] {u v : α → H} :
  ‖∫ (x : α), inner 𝕜 (u x) (v x) ∂μ‖ₑ ≤ MeasureTheory.eLpNorm u p μ * MeasureTheory.eLpNorm v q μ
```

**Hölder's inequality for the integral of a product.** Formalized in Tau Ceti as [`TauCeti.enorm_integral_mul_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/Duality.html#TauCeti.enorm_integral_mul_le).

```lean
TauCeti.enorm_integral_mul_le.{u_1, u_4} {α : Type u_1} {mα : MeasurableSpace α}
  {μ : MeasureTheory.Measure α} {𝕜 : Type u_4} [NonUnitalNormedRing 𝕜] [NormedSpace ℝ 𝕜]
  {p q : ENNReal} [p.HolderConjugate q] {u v : α → 𝕜} :
  ‖∫ (x : α), u x * v x ∂μ‖ₑ ≤ MeasureTheory.eLpNorm u p μ * MeasureTheory.eLpNorm v q μ
```

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

**Hölder's inequality in extended-valued `∫⁻` form, raised to the power `r`.** Formalized in Tau Ceti as [`TauCeti.rpow_lintegral_le_measure_univ_rpow_mul`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/LIntegralRpow.html#TauCeti.rpow_lintegral_le_measure_univ_rpow_mul).

```lean
TauCeti.rpow_lintegral_le_measure_univ_rpow_mul.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ : MeasureTheory.Measure α} {u : α → ENNReal} (hu : AEMeasurable u μ) {r : ℝ} (hr : 1 ≤ r) :
  (∫⁻ (x : α), u x ∂μ) ^ r ≤ μ Set.univ ^ (r - 1) * ∫⁻ (x : α), u x ^ r ∂μ
```

## Sources

- [Tau Ceti documentation: `TauCeti.lintegral_mul_le_of_inv_add_inv_eq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MeanInequalities.html#TauCeti.lintegral_mul_le_of_inv_add_inv_eq)
- [Source of `TauCeti.lintegral_mul_le_of_inv_add_inv_eq` in TauCeti/MeasureTheory/Integral/MeanInequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Integral/MeanInequalities.lean#L45)
