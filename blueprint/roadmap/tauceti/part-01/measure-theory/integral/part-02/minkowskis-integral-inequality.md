---
declaration: theorem
origin: cited
lean: TauCeti.lintegral_Lp_lintegral_le, TauCeti.lintegral_mul_setLIntegral_rpow_le
statement: formalized
proof: formalized
---

# Minkowski's integral inequality

For `1 ≤ p` and a jointly a.e. measurable
`f : α → β → ℝ≥0∞`, the `Lᵖ(μ)` seminorm of `x ↦ ∫⁻ y, f x y ∂ν` is at most the integral over `ν`
of the `Lᵖ(μ)` seminorms of the functions `x ↦ f x y`:
`(∫⁻ x, (∫⁻ y, f x y ∂ν) ^ p ∂μ) ^ (1 / p) ≤ ∫⁻ y, (∫⁻ x, f x y ^ p ∂μ) ^ (1 / p) ∂ν`.

```lean
TauCeti.lintegral_Lp_lintegral_le.{u_1, u_2} {α : Type u_1} {β : Type u_2} [MeasurableSpace α]
  [MeasurableSpace β] {μ : MeasureTheory.Measure α} {ν : MeasureTheory.Measure β}
  [MeasureTheory.SFinite μ] [MeasureTheory.SFinite ν] {f : α → β → ENNReal}
  (hf : AEMeasurable (Function.uncurry f) (μ.prod ν)) {p : ℝ} (hp : 1 ≤ p) :
  (∫⁻ (x : α), (∫⁻ (y : β), f x y ∂ν) ^ p ∂μ) ^ (1 / p) ≤
    ∫⁻ (y : β), (∫⁻ (x : α), f x y ^ p ∂μ) ^ (1 / p) ∂ν
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.lintegral_Lp_lintegral_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MinkowskiIntegral.html#TauCeti.lintegral_Lp_lintegral_le).

## Other forms

**Minkowski's integral inequality for weighted truncations.** Formalized in Tau Ceti as [`TauCeti.lintegral_mul_setLIntegral_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MinkowskiIntegral.html#TauCeti.lintegral_mul_setLIntegral_rpow_le).

```lean
TauCeti.lintegral_mul_setLIntegral_rpow_le.{u_1, u_2} {α : Type u_1} {β : Type u_2}
  [MeasurableSpace α] [MeasurableSpace β] {μ : MeasureTheory.Measure α}
  {ν : MeasureTheory.Measure β} [MeasureTheory.SFinite ν] [MeasureTheory.SFinite μ]
  {R : β → α → Prop} (hR : MeasurableSet {z | R z.1 z.2}) {w : β → ENNReal} (hw : AEMeasurable w ν)
  {g : α → ENNReal} (hg : AEMeasurable g μ) {r : ℝ} (hr : 1 ≤ r) :
  ∫⁻ (t : β), w t * (∫⁻ (x : α) in {x | R t x}, g x ∂μ) ^ r ∂ν ≤
    (∫⁻ (x : α), g x * (∫⁻ (t : β), {t | R t x}.indicator w t ∂ν) ^ r⁻¹ ∂μ) ^ r
```

## Sources

- [Tau Ceti documentation: `TauCeti.lintegral_Lp_lintegral_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MinkowskiIntegral.html#TauCeti.lintegral_Lp_lintegral_le)
- [Source of `TauCeti.lintegral_Lp_lintegral_le` in TauCeti/MeasureTheory/Integral/MinkowskiIntegral.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/MinkowskiIntegral.lean#L149)
