---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsRowCompact.isEntire_charPowerSeries
statement: formalized
proof: formalized
---

# The Fredholm determinant is entire

For a row-compact `u`, the principal-minor series
`det (1 - T u)` is a restricted power series at every radius.

```lean
ContinuousLinearMap.IsRowCompact.isEntire_charPowerSeries.{u_1, u_2} {I : Type u_1} {R : Type u_2}
  [TopologicalSpace I] [DiscreteTopology I] [DecidableEq I] [NormedCommRing R] [NormOneClass R]
  [IsUltrametricDist R] {u : ZeroAtInftyContinuousMap I R →L[R] ZeroAtInftyContinuousMap I R}
  (hu : u.IsRowCompact) : u.matrixCoeff.charPowerSeries.IsEntire
```

## Depends on

- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsRowCompact.isEntire_charPowerSeries`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Resolvent.html#ContinuousLinearMap.IsRowCompact.isEntire_charPowerSeries).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsRowCompact.isEntire_charPowerSeries`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Resolvent.html#ContinuousLinearMap.IsRowCompact.isEntire_charPowerSeries)
- [Source of `ContinuousLinearMap.IsRowCompact.isEntire_charPowerSeries` in TauCeti/Analysis/Normed/Operator/Nonarchimedean/Resolvent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Resolvent.lean#L263)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CompactOperators/STATUS.md)
