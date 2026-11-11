---
declaration: theorem
origin: cited
lean: TauCeti.DenseGraphLimits.cutDist_triangle
statement: formalized
proof: formalized
---

# TauCeti.DenseGraphLimits.cutDist_triangle

The coupling-primary graphon cut distance satisfies the triangle inequality on arbitrary
probability carriers.

```lean
TauCeti.DenseGraphLimits.cutDist_triangle.{u_1, u_2, u_3} {Ω₁ : Type u_1} {Ω₂ : Type u_2}
  {Ω₃ : Type u_3} [MeasurableSpace Ω₁] [MeasurableSpace Ω₂] [MeasurableSpace Ω₃]
  {μ₁ : MeasureTheory.Measure Ω₁} {μ₂ : MeasureTheory.Measure Ω₂} {μ₃ : MeasureTheory.Measure Ω₃}
  [MeasureTheory.IsProbabilityMeasure μ₁] [MeasureTheory.IsProbabilityMeasure μ₂]
  [MeasureTheory.IsProbabilityMeasure μ₃] (U : TauCeti.DenseGraphLimits.Graphon Ω₁ μ₁)
  (W : TauCeti.DenseGraphLimits.Graphon Ω₂ μ₂) (X : TauCeti.DenseGraphLimits.Graphon Ω₃ μ₃) :
  TauCeti.DenseGraphLimits.cutDist U X ≤
    TauCeti.DenseGraphLimits.cutDist U W + TauCeti.DenseGraphLimits.cutDist W X
```

## Depends on

- [TauCeti.DenseGraphLimits.cutDist](tauceti-densegraphlimits-cutdist.md)

## Proof depends on

- [Frieze--Kannan weak regularity](frieze-kannan-weak-regularity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.cutDist_triangle`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/CutMetric/Triangle.html#TauCeti.DenseGraphLimits.cutDist_triangle).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.cutDist_triangle`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/CutMetric/Triangle.html#TauCeti.DenseGraphLimits.cutDist_triangle)
- [Source of `TauCeti.DenseGraphLimits.cutDist_triangle` in TauCeti/Combinatorics/DenseGraphLimits/CutMetric/Triangle.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/DenseGraphLimits/CutMetric/Triangle.lean#L190)
- [Tau Ceti roadmap status: Dense graph limits and graphons](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/DenseGraphLimits/STATUS.md)
