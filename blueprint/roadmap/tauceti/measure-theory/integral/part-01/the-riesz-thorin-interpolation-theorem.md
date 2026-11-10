---
declaration: theorem
origin: cited
lean: TauCeti.eLpNorm_le_rpow_mul_rpow_mul_eLpNorm, TauCeti.eLpNorm_le_rpow_mul_rpow_mul_eLpNorm_of_ne_top
statement: formalized
proof: formalized
---

# The Riesz–Thorin interpolation theorem

Let `T` be a complex-linear map from simple
functions on `(α, μ)` to almost-everywhere classes on a σ-finite `(β, ν)` with
`‖T f‖_{q₀} ≤ M₀ ‖f‖_{p₀}` and `‖T f‖_{q₁} ≤ M₁ ‖f‖_{p₁}` for all simple `f`, where
`p₀, p₁ ∈ [0, ∞]` and `1 ≤ q₀, q₁ ≤ ∞`. For `0 < θ < 1` and the intermediate exponents
`1 / p = (1 - θ) / p₀ + θ / p₁`, `1 / q = (1 - θ) / q₀ + θ / q₁`,

`‖T f‖_q ≤ M₀ ^ (1 - θ) M₁ ^ θ ‖f‖_p`

for every simple `f`. σ-finiteness of `ν` is only used when `q = ∞`; for `q < ∞` see
`TauCeti.eLpNorm_le_rpow_mul_rpow_mul_eLpNorm_of_ne_top`.

```lean
TauCeti.eLpNorm_le_rpow_mul_rpow_mul_eLpNorm.{u_1, u_2} {α : Type u_1} {β : Type u_2}
  {mα : MeasurableSpace α} {mβ : MeasurableSpace β} {μ : MeasureTheory.Measure α}
  {ν : MeasureTheory.Measure β} [MeasureTheory.SigmaFinite ν]
  {T : MeasureTheory.SimpleFunc α ℂ →ₗ[ℂ] β →ₘ[ν] ℂ} {p₀ p₁ p q₀ q₁ q : ENNReal} (hq₀ : 1 ≤ q₀)
  (hq₁ : 1 ≤ q₁) {θ : ℝ} (hθ : θ ∈ Set.Ioo 0 1)
  (hp : p⁻¹ = ENNReal.ofReal (1 - θ) * p₀⁻¹ + ENNReal.ofReal θ * p₁⁻¹)
  (hq : q⁻¹ = ENNReal.ofReal (1 - θ) * q₀⁻¹ + ENNReal.ofReal θ * q₁⁻¹) {M₀ M₁ : NNReal}
  (h₀ :
    ∀ (f : MeasureTheory.SimpleFunc α ℂ),
      MeasureTheory.eLpNorm (↑(T f)) q₀ ν ≤ ↑M₀ * MeasureTheory.eLpNorm (⇑f) p₀ μ)
  (h₁ :
    ∀ (f : MeasureTheory.SimpleFunc α ℂ),
      MeasureTheory.eLpNorm (↑(T f)) q₁ ν ≤ ↑M₁ * MeasureTheory.eLpNorm (⇑f) p₁ μ)
  (f : MeasureTheory.SimpleFunc α ℂ) :
  MeasureTheory.eLpNorm (↑(T f)) q ν ≤ ↑(M₀ ^ (1 - θ) * M₁ ^ θ) * MeasureTheory.eLpNorm (⇑f) p μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for the integral of a product](../../function/holders-inequality-for-the-integral-of-a-product.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.eLpNorm_le_rpow_mul_rpow_mul_eLpNorm`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/RieszThorin.html#TauCeti.eLpNorm_le_rpow_mul_rpow_mul_eLpNorm).

## Other forms

**The Riesz–Thorin interpolation theorem.** Formalized in Tau Ceti as [`TauCeti.eLpNorm_le_rpow_mul_rpow_mul_eLpNorm_of_ne_top`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/RieszThorin.html#TauCeti.eLpNorm_le_rpow_mul_rpow_mul_eLpNorm_of_ne_top).

```lean
TauCeti.eLpNorm_le_rpow_mul_rpow_mul_eLpNorm_of_ne_top.{u_1, u_2} {α : Type u_1} {β : Type u_2}
  {mα : MeasurableSpace α} {mβ : MeasurableSpace β} {μ : MeasureTheory.Measure α}
  {ν : MeasureTheory.Measure β} {T : MeasureTheory.SimpleFunc α ℂ →ₗ[ℂ] β →ₘ[ν] ℂ}
  {p₀ p₁ p q₀ q₁ q : ENNReal} (hq₀ : 1 ≤ q₀) (hq₁ : 1 ≤ q₁) {θ : ℝ} (hθ : θ ∈ Set.Ioo 0 1)
  (hp : p⁻¹ = ENNReal.ofReal (1 - θ) * p₀⁻¹ + ENNReal.ofReal θ * p₁⁻¹)
  (hq : q⁻¹ = ENNReal.ofReal (1 - θ) * q₀⁻¹ + ENNReal.ofReal θ * q₁⁻¹) (hqtop : q ≠ ⊤)
  {M₀ M₁ : NNReal}
  (h₀ :
    ∀ (f : MeasureTheory.SimpleFunc α ℂ),
      MeasureTheory.eLpNorm (↑(T f)) q₀ ν ≤ ↑M₀ * MeasureTheory.eLpNorm (⇑f) p₀ μ)
  (h₁ :
    ∀ (f : MeasureTheory.SimpleFunc α ℂ),
      MeasureTheory.eLpNorm (↑(T f)) q₁ ν ≤ ↑M₁ * MeasureTheory.eLpNorm (⇑f) p₁ μ)
  (f : MeasureTheory.SimpleFunc α ℂ) :
  MeasureTheory.eLpNorm (↑(T f)) q ν ≤ ↑(M₀ ^ (1 - θ) * M₁ ^ θ) * MeasureTheory.eLpNorm (⇑f) p μ
```

## Sources

- [Tau Ceti documentation: `TauCeti.eLpNorm_le_rpow_mul_rpow_mul_eLpNorm`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/RieszThorin.html#TauCeti.eLpNorm_le_rpow_mul_rpow_mul_eLpNorm)
- [Source of `TauCeti.eLpNorm_le_rpow_mul_rpow_mul_eLpNorm` in TauCeti/MeasureTheory/Integral/RieszThorin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Integral/RieszThorin.lean#L541)
