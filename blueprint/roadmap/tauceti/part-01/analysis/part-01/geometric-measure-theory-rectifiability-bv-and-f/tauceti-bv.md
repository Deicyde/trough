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
- [Source of `TauCeti.BV` in TauCeti/Analysis/BoundedVariation/Space.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/BoundedVariation/Space.lean#L123)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
