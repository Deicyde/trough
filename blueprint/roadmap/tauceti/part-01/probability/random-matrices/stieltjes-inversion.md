---
declaration: theorem
origin: cited
lean: MeasureTheory.tendsto_intervalIntegral_im_resolventTransform
statement: formalized
proof: formalized
---

# Stieltjes inversion

For a finite measure `μ` on `ℝ` and `a < b`,
`π⁻¹ ∫_a^b Im m_μ(x + iη) dx` tends to `μ (a, b) + (μ {a} + μ {b}) / 2` as `η → 0⁺`.

```lean
MeasureTheory.tendsto_intervalIntegral_im_resolventTransform {μ : MeasureTheory.Measure ℝ}
  [MeasureTheory.IsFiniteMeasure μ] {a b : ℝ} (hab : a < b) :
  Filter.Tendsto
    (fun η =>
      Real.pi⁻¹ * ∫ (x : ℝ) in a..b, (MeasureTheory.resolventTransform μ (↑x + ↑η * Complex.I)).im)
    (nhdsWithin 0 (Set.Ioi 0)) (nhds (μ.real (Set.Ioo a b) + (μ.real {a} + μ.real {b}) / 2))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.tendsto_intervalIntegral_im_resolventTransform`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/ResolventTransform/Inversion.html#MeasureTheory.tendsto_intervalIntegral_im_resolventTransform).

## Sources

- [Tau Ceti documentation: `MeasureTheory.tendsto_intervalIntegral_im_resolventTransform`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/ResolventTransform/Inversion.html#MeasureTheory.tendsto_intervalIntegral_im_resolventTransform)
- [Source of `MeasureTheory.tendsto_intervalIntegral_im_resolventTransform` in TauCeti/MeasureTheory/Measure/ResolventTransform/Inversion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Measure/ResolventTransform/Inversion.lean#L90)
- [Tau Ceti roadmap status: Random matrices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RandomMatrices/STATUS.md)
