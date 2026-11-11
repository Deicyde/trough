---
declaration: theorem
origin: cited
lean: MeasureTheory.setLIntegral_regionBetween, MeasureTheory.setLIntegral_regionBetween_symm
statement: formalized
proof: formalized
---

# Tonelli's theorem on the region between two functions

**Tonelli's theorem on the region between two functions**, integrating first along the
vertical intervals `Ioo (f x) (g x)`.

```lean
MeasureTheory.setLIntegral_regionBetween.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ : MeasureTheory.Measure α} {ν : MeasureTheory.Measure ℝ} [MeasureTheory.SFinite ν]
  {f g : α → ℝ} {s : Set α} {F : α × ℝ → ENNReal} (hs : MeasurableSet s)
  (hR : MeasurableSet (regionBetween f g s))
  (hF : AEMeasurable F ((μ.prod ν).restrict (regionBetween f g s))) :
  ∫⁻ (z : α × ℝ) in regionBetween f g s, F z ∂μ.prod ν =
    ∫⁻ (x : α) in s, ∫⁻ (y : ℝ) in Set.Ioo (f x) (g x), F (x, y) ∂ν ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.setLIntegral_regionBetween`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/RegionBetween.html#MeasureTheory.setLIntegral_regionBetween).

## Other forms

**Tonelli's theorem on the region between two functions.** Formalized in Tau Ceti as [`MeasureTheory.setLIntegral_regionBetween_symm`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/RegionBetween.html#MeasureTheory.setLIntegral_regionBetween_symm).

```lean
MeasureTheory.setLIntegral_regionBetween_symm.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ : MeasureTheory.Measure α} {ν : MeasureTheory.Measure ℝ} [MeasureTheory.SFinite ν]
  {f g : α → ℝ} {s : Set α} {F : α × ℝ → ENNReal} [MeasureTheory.SFinite μ]
  (hR : MeasurableSet (regionBetween f g s))
  (hF : AEMeasurable F ((μ.prod ν).restrict (regionBetween f g s))) :
  ∫⁻ (z : α × ℝ) in regionBetween f g s, F z ∂μ.prod ν =
    ∫⁻ (y : ℝ), ∫⁻ (x : α) in {x | x ∈ s ∧ y ∈ Set.Ioo (f x) (g x)}, F (x, y) ∂μ ∂ν
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.setLIntegral_regionBetween`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/RegionBetween.html#MeasureTheory.setLIntegral_regionBetween)
- [Source of `MeasureTheory.setLIntegral_regionBetween` in TauCeti/MeasureTheory/Integral/RegionBetween.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/RegionBetween.lean#L38)
