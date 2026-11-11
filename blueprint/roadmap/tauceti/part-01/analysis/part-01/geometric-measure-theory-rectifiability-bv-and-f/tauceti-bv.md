---
declaration: structure
origin: cited
lean: TauCeti.BV
statement: formalized
---

# TauCeti.BV

Almost-everywhere classes of integrable functions with finite total variation on `Ω`.
The wrapper gives this space its BV norm, independently of the weaker inherited `L¹` norm.

```lean
TauCeti.BV.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [OpensMeasurableSpace E] (μ : MeasureTheory.Measure E)
  (Ω : TopologicalSpace.Opens E) : Type u_1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.BV`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Space.html#TauCeti.BV).

## Sources

- [Tau Ceti documentation: `TauCeti.BV`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Space.html#TauCeti.BV)
- [Source of `TauCeti.BV` in TauCeti/Analysis/BoundedVariation/Space.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/BoundedVariation/Space.lean#L130)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
