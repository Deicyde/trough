---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsRieszProjection.rankAtStalk_range
statement: formalized
proof: formalized
---

# Constant rank of the Riesz summand

At a good zero of order `h` the range of a Riesz
projection, a finitely generated projective module, has rank `h` at every point of `Spec R`.
Ranks are computed algebraically, so nilpotent coefficients are retained; at order zero the range
is zero.

```lean
ContinuousLinearMap.IsRieszProjection.rankAtStalk_range.{u_1, u_2} {I : Type u_1} {R : Type u_2}
  [TopologicalSpace I] [DiscreteTopology I] [DecidableEq I] [NormedCommRing R]
  [TauCeti.NormedRing.IsTate R] [IsUltrametricDist R] [CompleteSpace R]
  {u E : ZeroAtInftyContinuousMap I R →L[R] ZeroAtInftyContinuousMap I R} {a : R} {h : ℕ}
  (hE : u.IsRieszProjection a h E) (hu : u.IsRowCompact)
  (hH : u.matrixCoeff.charPowerSeries.IsGoodZero a h) (p : PrimeSpectrum R) :
  Module.rankAtStalk (↥(↑E).range) p = h
```

## Depends on

- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)

## Proof depends on

- [Factor theorem for entire series](../../../ring-theory/part-01/power-series/factor-theorem-for-entire-series.md)
- [Quantitative Open Mapping Theorem](../../part-03/normed/part-02/quantitative-open-mapping-theorem.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsRieszProjection.rankAtStalk_range`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/RieszProjection/Multiplicity.html#ContinuousLinearMap.IsRieszProjection.rankAtStalk_range).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsRieszProjection.rankAtStalk_range`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/RieszProjection/Multiplicity.html#ContinuousLinearMap.IsRieszProjection.rankAtStalk_range)
- [Source of `ContinuousLinearMap.IsRieszProjection.rankAtStalk_range` in TauCeti/Analysis/Normed/Operator/Nonarchimedean/RieszProjection/Multiplicity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/Nonarchimedean/RieszProjection/Multiplicity.lean#L143)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CompactOperators/STATUS.md)
