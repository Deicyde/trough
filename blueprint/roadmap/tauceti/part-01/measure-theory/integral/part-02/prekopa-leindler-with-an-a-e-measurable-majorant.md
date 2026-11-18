---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.HasPrekopaLeindler.lintegral, MeasureTheory.Measure.integral_rpow_mul_integral_rpow_le_integral
statement: formalized
proof: formalized
---

# Prékopa–Leindler with an a.e. measurable majorant

At a weight in `[0,1]`, the
lower-integral inequality holds for arbitrary input functions and an a.e. measurable upper
function. The hypothesis still concerns the supplied representatives at every pair of points.
Zero and infinite integrals use the extended nonnegative power and product conventions.

```lean
MeasureTheory.Measure.HasPrekopaLeindler.lintegral.{u_1} {E : Type u_1} [MeasurableSpace E]
  [AddCommMonoid E] [_root_.Module ℝ E] {μ : MeasureTheory.Measure E} {θ : ℝ}
  (hμ : μ.HasPrekopaLeindler θ) (hθ₀ : 0 ≤ θ) (hθ₁ : θ ≤ 1) {f g h : E → ENNReal}
  (hh : AEMeasurable h μ) (hfg : ∀ (x y : E), f x ^ (1 - θ) * g y ^ θ ≤ h ((1 - θ) • x + θ • y)) :
  (∫⁻ (x : E), f x ∂μ) ^ (1 - θ) * (∫⁻ (x : E), g x ∂μ) ^ θ ≤ ∫⁻ (x : E), h x ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Prékopa–Leindler inequality for the minimum on `ℝ`](prekopa-leindler-inequality-for-the-minimum-on-r.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.HasPrekopaLeindler.lintegral`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/PrekopaLeindler/Basic.html#MeasureTheory.Measure.HasPrekopaLeindler.lintegral).

## Other forms

**Prékopa–Leindler for real functions on a finite-dimensional real space.** Formalized in Tau Ceti as [`MeasureTheory.Measure.integral_rpow_mul_integral_rpow_le_integral`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/PrekopaLeindler/Real.html#MeasureTheory.Measure.integral_rpow_mul_integral_rpow_le_integral).

```lean
MeasureTheory.Measure.integral_rpow_mul_integral_rpow_le_integral.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] (μ : MeasureTheory.Measure E) [μ.IsAddHaarMeasure] {θ : ℝ} (hθ₀ : 0 ≤ θ)
  (hθ₁ : θ ≤ 1) {f g h : E → ℝ} (hh : MeasureTheory.Integrable h μ) (hf₀ : ∀ (x : E), 0 ≤ f x)
  (hg₀ : ∀ (x : E), 0 ≤ g x)
  (hfg : ∀ (x y : E), f x ^ (1 - θ) * g y ^ θ ≤ h ((1 - θ) • x + θ • y)) :
  (∫ (x : E), f x ∂μ) ^ (1 - θ) * (∫ (x : E), g x ∂μ) ^ θ ≤ ∫ (x : E), h x ∂μ
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.HasPrekopaLeindler.lintegral`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/PrekopaLeindler/Basic.html#MeasureTheory.Measure.HasPrekopaLeindler.lintegral)
- [Source of `MeasureTheory.Measure.HasPrekopaLeindler.lintegral` in TauCeti/MeasureTheory/Integral/PrekopaLeindler/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Integral/PrekopaLeindler/Basic.lean#L134)
