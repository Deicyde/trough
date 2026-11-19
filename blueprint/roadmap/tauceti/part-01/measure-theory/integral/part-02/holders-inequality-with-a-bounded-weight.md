---
declaration: theorem
origin: cited
lean: TauCeti.integral_sq_mul_norm_sq_le_of_ae_le, TauCeti.MeasureTheory.norm_integral_smul_le_eLpNorm_mul_eLpNorm_mul_measureReal_rpow, TauCeti.lintegral_ofReal_rpow_mul_eNorm_le, TauCeti.lintegral_mul_le_of_inv_add_inv_eq
statement: formalized
proof: formalized
---

# Hölder's inequality with a bounded weight

On a finite measure space, let `θ` be a
measurable weight with `0 ≤ θ ≤ K` almost everywhere, and let `‖g‖ ∈ L^{2q}` for a pair of Hölder
conjugate exponents `q, q'`. Then
`∫ θ² ‖g‖² ≤ (K^(2q' - 1) ∫ θ)^(1/q') (∫ ‖g‖^(2q))^(1/q)`.

```lean
TauCeti.integral_sq_mul_norm_sq_le_of_ae_le.{u_1, u_2} {β : Type u_1} [MeasurableSpace β]
  {ν : MeasureTheory.Measure β} {E : Type u_2} [NormedAddCommGroup E]
  [MeasureTheory.IsFiniteMeasure ν] {θ : β → ℝ} {g : β → E} {K q q' : ℝ} (hq : q.HolderConjugate q')
  (hθm : MeasureTheory.AEStronglyMeasurable θ ν) (hθ : ∀ᵐ (x : β) ∂ν, 0 ≤ θ x ∧ θ x ≤ K)
  (hg : MeasureTheory.MemLp g (ENNReal.ofReal (2 * q)) ν) :
  ∫ (x : β), θ x ^ 2 * ‖g x‖ ^ 2 ∂ν ≤
    (K ^ (2 * q' - 1) * ∫ (x : β), θ x ∂ν) ^ q'⁻¹ * (∫ (x : β), ‖g x‖ ^ (2 * q) ∂ν) ^ q⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_sq_mul_norm_sq_le_of_ae_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MeanInequalities.html#TauCeti.integral_sq_mul_norm_sq_le_of_ae_le).

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

**Hölder's inequality for a power times a norm.** Formalized in Tau Ceti as [`TauCeti.lintegral_ofReal_rpow_mul_eNorm_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MeanInequalities.html#TauCeti.lintegral_ofReal_rpow_mul_eNorm_le).

```lean
TauCeti.lintegral_ofReal_rpow_mul_eNorm_le.{u_1, u_2} {β : Type u_1} [MeasurableSpace β]
  {ν : MeasureTheory.Measure β} {F : Type u_2} [NormedAddCommGroup F] {w : β → ℝ} {g : β → F}
  (hw : AEMeasurable w ν) (hg : MeasureTheory.AEStronglyMeasurable g ν) {p : ENNReal} {γ p' q : ℝ}
  (hconj : p'.HolderConjugate p.toReal) (hγp' : (γ - 1) * p' = q) :
  ∫⁻ (x : β), ENNReal.ofReal (w x) ^ (γ - 1) * ‖g x‖ₑ ∂ν ≤
    (∫⁻ (x : β), ENNReal.ofReal (w x) ^ q ∂ν) ^ p'⁻¹ * MeasureTheory.eLpNorm g p ν
```

**Hölder's inequality for Young's exponents.** Formalized in Tau Ceti as [`TauCeti.lintegral_mul_le_of_inv_add_inv_eq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MeanInequalities.html#TauCeti.lintegral_mul_le_of_inv_add_inv_eq).

```lean
TauCeti.lintegral_mul_le_of_inv_add_inv_eq.{u_1} {β : Type u_1} [MeasurableSpace β]
  {ν : MeasureTheory.Measure β} {k g : β → ENNReal} (hk : AEMeasurable k ν) (hg : AEMeasurable g ν)
  {p q r : ℝ} (hp : 1 ≤ p) (hpq : p ≤ q) (hr : p⁻¹ + r⁻¹ = 1 + q⁻¹) :
  ∫⁻ (y : β), k y * g y ∂ν ≤
    (∫⁻ (y : β), k y ^ r * g y ^ p ∂ν) ^ q⁻¹ * (∫⁻ (y : β), k y ^ r ∂ν) ^ (1 - p⁻¹) *
      (∫⁻ (y : β), g y ^ p ∂ν) ^ (p⁻¹ - q⁻¹)
```

## Sources

- [Tau Ceti documentation: `TauCeti.integral_sq_mul_norm_sq_le_of_ae_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MeanInequalities.html#TauCeti.integral_sq_mul_norm_sq_le_of_ae_le)
- [Source of `TauCeti.integral_sq_mul_norm_sq_le_of_ae_le` in TauCeti/MeasureTheory/Integral/MeanInequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Integral/MeanInequalities.lean#L165)
