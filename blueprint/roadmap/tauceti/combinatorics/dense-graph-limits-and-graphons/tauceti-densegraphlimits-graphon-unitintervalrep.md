---
declaration: def
origin: cited
lean: TauCeti.DenseGraphLimits.Graphon.unitIntervalRepr
statement: formalized
---

# TauCeti.DenseGraphLimits.Graphon.unitIntervalRepr

A graphon on the unit interval at cut distance zero from `W`, for `W` on an arbitrary
probability carrier.

The representative is an arbitrary choice; `cutDist_unitIntervalRepr_left` and
`cutDist_unitIntervalRepr_right` show that no cut distance depends on it.

```lean
TauCeti.DenseGraphLimits.Graphon.unitIntervalRepr.{u_1} {Ω : Type u_1} [MeasurableSpace Ω]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsProbabilityMeasure μ]
  (W : TauCeti.DenseGraphLimits.Graphon Ω μ) :
  TauCeti.DenseGraphLimits.Graphon (↑unitInterval) MeasureTheory.volume
```

## Depends on

- [TauCeti.DenseGraphLimits.cutDist](tauceti-densegraphlimits-cutdist.md)

## Proof depends on

- [TauCeti.DenseGraphLimits.cutDist_triangle](tauceti-densegraphlimits-cutdist-triangle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.Graphon.unitIntervalRepr`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/UnitIntervalEmbedding.html#TauCeti.DenseGraphLimits.Graphon.unitIntervalRepr).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.Graphon.unitIntervalRepr`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/UnitIntervalEmbedding.html#TauCeti.DenseGraphLimits.Graphon.unitIntervalRepr)
- [Source of `TauCeti.DenseGraphLimits.Graphon.unitIntervalRepr` in TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/UnitIntervalEmbedding.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/UnitIntervalEmbedding.lean#L80)
- [Tau Ceti roadmap status: Dense graph limits and graphons](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/DenseGraphLimits/STATUS.md)
