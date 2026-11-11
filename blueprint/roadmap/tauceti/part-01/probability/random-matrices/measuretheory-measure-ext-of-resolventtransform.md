---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.ext_of_resolventTransform
statement: formalized
proof: formalized
---

# MeasureTheory.Measure.ext_of_resolventTransform

A finite measure on `ℝ` is determined by its resolvent transform on the upper half-plane.

```lean
MeasureTheory.Measure.ext_of_resolventTransform {μ : MeasureTheory.Measure ℝ}
  [MeasureTheory.IsFiniteMeasure μ] {ν : MeasureTheory.Measure ℝ} [MeasureTheory.IsFiniteMeasure ν]
  (h :
    ∀ (z : ℂ),
      0 < z.im → MeasureTheory.resolventTransform μ z = MeasureTheory.resolventTransform ν z) :
  μ = ν
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Stieltjes inversion](stieltjes-inversion.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.ext_of_resolventTransform`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/ResolventTransform/Inversion.html#MeasureTheory.Measure.ext_of_resolventTransform).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.ext_of_resolventTransform`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/ResolventTransform/Inversion.html#MeasureTheory.Measure.ext_of_resolventTransform)
- [Source of `MeasureTheory.Measure.ext_of_resolventTransform` in TauCeti/MeasureTheory/Measure/ResolventTransform/Inversion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Measure/ResolventTransform/Inversion.lean#L172)
- [Tau Ceti roadmap status: Random matrices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RandomMatrices/STATUS.md)
