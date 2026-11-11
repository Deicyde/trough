---
declaration: theorem
origin: cited
lean: TauCeti.lintegral_rpow_le_of_rpow_mul_meas_lt_le_rpow
statement: formalized
proof: formalized
---

# The off-diagonal Marcinkiewicz interpolation theorem

Let `T` be a subadditive operator of
weak type `(p₀, q₀)` with constant `A₀` and of weak type `(p₁, q₁)` with constant `A₁`:

`r ^ qᵢ * ν {T g > r} ≤ Aᵢ * (∫⁻ ‖g‖ ^ pᵢ ∂μ) ^ (qᵢ / pᵢ)` for every `g` and every `r`,

with `0 < pᵢ ≤ qᵢ < ∞`, `p₀ ≠ p₁` and `q₀ ≠ q₁`. For `0 < θ < 1` let
`1 / p = (1 - θ) / p₀ + θ / p₁` and `1 / q = (1 - θ) / q₀ + θ / q₁`. Then `T` is of strong
type `(p, q)`:

`∫⁻ (T v) ^ q ∂ν ≤ (q / |q - q₀| · A₀ d ^ (-q₀) + q / |q - q₁| · A₁ e ^ (-q₁)) *
  (∫⁻ ‖v‖ ^ p ∂μ) ^ (q / p)`,

for any splitting parameters `d, e > 0` with `d + e ≤ 1`.

```lean
TauCeti.lintegral_rpow_le_of_rpow_mul_meas_lt_le_rpow.{u_1, u_2, u_3} {α : Type u_1} {β : Type u_2}
  [MeasurableSpace α] [MeasurableSpace β] {μ : MeasureTheory.Measure α}
  {ν : MeasureTheory.Measure β} {p p₀ p₁ q q₀ q₁ : ℝ} {A₀ A₁ : ENNReal} {G : Type u_3}
  [MeasurableSpace G] [TopologicalSpace G] [OpensMeasurableSpace G] [ESeminormedAddMonoid G]
  {T : (α → G) → β → ENNReal} {v : α → G} {d e : ℝ} (hv : AEMeasurable v μ)
  (hTv : AEMeasurable (T v) ν) (hpp : p₀ ≠ p₁) (hp₀ : 0 < p₀) (hp₁ : 0 < p₁) (hpq₀ : p₀ ≤ q₀)
  (hpq₁ : p₁ ≤ q₁) (hqq : q₀ ≠ q₁) {θ : ℝ} (hθ₀ : 0 < θ) (hθ₁ : θ < 1)
  (hp : p⁻¹ = (1 - θ) / p₀ + θ / p₁) (hq : q⁻¹ = (1 - θ) / q₀ + θ / q₁) (hd : 0 < d) (he : 0 < e)
  (hde : d + e ≤ 1)
  (hadd : ∀ (g h : α → G), AEMeasurable g μ → AEMeasurable h μ → T (g + h) ≤ᵐ[ν] T g + T h)
  (hweak₀ :
    ∀ (g : α → G),
      AEMeasurable g μ →
        ∀ (r : ENNReal), r ^ q₀ * ν {y | r < T g y} ≤ A₀ * (∫⁻ (x : α), ‖g x‖ₑ ^ p₀ ∂μ) ^ (q₀ / p₀))
  (hweak₁ :
    ∀ (g : α → G),
      AEMeasurable g μ →
        ∀ (r : ENNReal),
          r ^ q₁ * ν {y | r < T g y} ≤ A₁ * (∫⁻ (x : α), ‖g x‖ₑ ^ p₁ ∂μ) ^ (q₁ / p₁)) :
  ∫⁻ (y : β), T v y ^ q ∂ν ≤
    (ENNReal.ofReal (q / |q - q₀|) * (A₀ * ENNReal.ofReal (d ^ (-q₀))) +
        ENNReal.ofReal (q / |q - q₁|) * (A₁ * ENNReal.ofReal (e ^ (-q₁)))) *
      (∫⁻ (x : α), ‖v x‖ₑ ^ p ∂μ) ^ (q / p)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Minkowski's integral inequality](minkowskis-integral-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.lintegral_rpow_le_of_rpow_mul_meas_lt_le_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Marcinkiewicz/OffDiagonal.html#TauCeti.lintegral_rpow_le_of_rpow_mul_meas_lt_le_rpow).

## Sources

- [Tau Ceti documentation: `TauCeti.lintegral_rpow_le_of_rpow_mul_meas_lt_le_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Marcinkiewicz/OffDiagonal.html#TauCeti.lintegral_rpow_le_of_rpow_mul_meas_lt_le_rpow)
- [Source of `TauCeti.lintegral_rpow_le_of_rpow_mul_meas_lt_le_rpow` in TauCeti/MeasureTheory/Integral/Marcinkiewicz/OffDiagonal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/Marcinkiewicz/OffDiagonal.lean#L530)
