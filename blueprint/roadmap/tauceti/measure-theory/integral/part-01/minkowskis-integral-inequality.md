---
declaration: theorem
origin: cited
lean: TauCeti.lintegral_Lp_lintegral_le
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
  [MeasureTheory.SigmaFinite μ] [MeasureTheory.SFinite ν] {f : α → β → ENNReal}
  (hf : AEMeasurable (Function.uncurry f) (μ.prod ν)) {p : ℝ} (hp : 1 ≤ p) :
  (∫⁻ (x : α), (∫⁻ (y : β), f x y ∂ν) ^ p ∂μ) ^ (1 / p) ≤
    ∫⁻ (y : β), (∫⁻ (x : α), f x y ^ p ∂μ) ^ (1 / p) ∂ν
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.lintegral_Lp_lintegral_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MinkowskiIntegral.html#TauCeti.lintegral_Lp_lintegral_le).

## Sources

- [Tau Ceti documentation: `TauCeti.lintegral_Lp_lintegral_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MinkowskiIntegral.html#TauCeti.lintegral_Lp_lintegral_le)
- [Source of `TauCeti.lintegral_Lp_lintegral_le` in TauCeti/MeasureTheory/Integral/MinkowskiIntegral.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Integral/MinkowskiIntegral.lean#L195)
