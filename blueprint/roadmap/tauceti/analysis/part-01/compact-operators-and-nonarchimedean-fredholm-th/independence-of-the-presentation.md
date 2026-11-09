---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsPrCompact.charPowerSeries_eq
statement: formalized
proof: formalized
---

# Independence of the presentation

The Fredholm series of a row-compact endomorphism `u`
of a module with property (Pr) is the principal-minor series of its extension `i ∘ u ∘ r`
through any retract presentation `r ∘ i = id` of the module by a model space.

```lean
ContinuousLinearMap.IsPrCompact.charPowerSeries_eq.{u, w, u_1} {R : Type w} [NormedCommRing R]
  [NormOneClass R] [IsUltrametricDist R] [CompleteSpace R] [TauCeti.NormedRing.IsTate R]
  {M : Type u} [SeminormedAddCommGroup M] [_root_.Module R M] {u : M →L[R] M} (hu : u.IsPrCompact)
  {J : Type u_1} [TopologicalSpace J] [DiscreteTopology J] [DecidableEq J]
  {i : M →L[R] ZeroAtInftyContinuousMap J R} {r : ZeroAtInftyContinuousMap J R →L[R] M}
  (hri : r ∘SL i = ContinuousLinearMap.id R M) :
  u.charPowerSeries = (i ∘SL u ∘SL r).matrixCoeff.charPowerSeries
```

## Depends on

- [ContinuousLinearMap.charPowerSeries](continuouslinearmap-charpowerseries.md)
- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsPrCompact.charPowerSeries_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/PrModule/Basic.html#ContinuousLinearMap.IsPrCompact.charPowerSeries_eq).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsPrCompact.charPowerSeries_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/PrModule/Basic.html#ContinuousLinearMap.IsPrCompact.charPowerSeries_eq)
- [Source of `ContinuousLinearMap.IsPrCompact.charPowerSeries_eq` in TauCeti/Analysis/Normed/Operator/Nonarchimedean/PrModule/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/Nonarchimedean/PrModule/Basic.lean#L145)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CompactOperators/STATUS.md)
