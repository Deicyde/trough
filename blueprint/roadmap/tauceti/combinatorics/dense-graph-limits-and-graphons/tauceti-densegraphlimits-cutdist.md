---
declaration: def
origin: cited
lean: TauCeti.DenseGraphLimits.cutDist
statement: formalized
---

# TauCeti.DenseGraphLimits.cutDist

The **cut distance** of two graphons: the infimum, over couplings of their carriers, of the cut
norm of the overlaid difference.

The two graphons may live on different probability spaces, and no standard Borel or atomless
hypothesis is imposed on either.

```lean
TauCeti.DenseGraphLimits.cutDist.{u_1, u_2} {Ω₁ : Type u_1} {Ω₂ : Type u_2} [MeasurableSpace Ω₁]
  [MeasurableSpace Ω₂] {μ₁ : MeasureTheory.Measure Ω₁} {μ₂ : MeasureTheory.Measure Ω₂}
  [MeasureTheory.IsProbabilityMeasure μ₁] [MeasureTheory.IsProbabilityMeasure μ₂]
  (U : TauCeti.DenseGraphLimits.Graphon Ω₁ μ₁) (W : TauCeti.DenseGraphLimits.Graphon Ω₂ μ₂) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.cutDist`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/CutMetric/Distance.html#TauCeti.DenseGraphLimits.cutDist).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.cutDist`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/CutMetric/Distance.html#TauCeti.DenseGraphLimits.cutDist)
- [Source of `TauCeti.DenseGraphLimits.cutDist` in TauCeti/Combinatorics/DenseGraphLimits/CutMetric/Distance.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/DenseGraphLimits/CutMetric/Distance.lean#L120)
- [Tau Ceti roadmap status: Dense graph limits and graphons](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/DenseGraphLimits/STATUS.md)
