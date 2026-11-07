---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsRowCompact.isRieszProjection_rieszProjection
statement: formalized
proof: formalized
---

# The Riesz projector at a good zero

Let `u` be row compact, and let `a` be a good zero of
order `h` of its Fredholm determinant `H_u`: `ΔʲH_u(a) = 0` for `j < h` and `ΔʰH_u(a)` is a unit.
Then `1 - (C b) ^ h` is a Riesz projection of `u` at `a` of order `h`.

```lean
ContinuousLinearMap.IsRowCompact.isRieszProjection_rieszProjection.{u_1, u_2} {I : Type u_1}
  {R : Type u_2} [TopologicalSpace I] [NormedCommRing R] [TauCeti.NormedRing.IsTate R]
  [DiscreteTopology I] [DecidableEq I] [IsUltrametricDist R] [CompleteSpace R]
  {u : ZeroAtInftyContinuousMap I R →L[R] ZeroAtInftyContinuousMap I R} (hu : u.IsRowCompact)
  {a : R} {h : ℕ}
  (hH : ∀ j < h, ((PowerSeries.hasseDeriv j) u.matrixCoeff.charPowerSeries).evalAt a = 0)
  (hc : IsUnit (((PowerSeries.hasseDeriv h) u.matrixCoeff.charPowerSeries).evalAt a)) :
  u.IsRieszProjection a h (u.rieszProjection a h)
```

## Depends on

- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)

## Proof depends on

- [The Fredholm determinant is entire](the-fredholm-determinant-is-entire.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsRowCompact.isRieszProjection_rieszProjection`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/RieszProjection/Basic.html#ContinuousLinearMap.IsRowCompact.isRieszProjection_rieszProjection).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsRowCompact.isRieszProjection_rieszProjection`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/RieszProjection/Basic.html#ContinuousLinearMap.IsRowCompact.isRieszProjection_rieszProjection)
- [Source of `ContinuousLinearMap.IsRowCompact.isRieszProjection_rieszProjection` in TauCeti/Analysis/Normed/Operator/Nonarchimedean/RieszProjection/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/Nonarchimedean/RieszProjection/Basic.lean#L371)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CompactOperators/STATUS.md)
