---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsRowCompact.charPowerSeries_eq_colemanDEntire
statement: formalized
proof: formalized
---

# Entire spectral mapping for Fredholm series

Evaluating a zero-constant entire
function at a row-compact operator transforms its Fredholm series by Coleman's entire
transform. This includes empty model spaces and coefficient rings with nilpotents.

```lean
ContinuousLinearMap.IsRowCompact.charPowerSeries_eq_colemanDEntire.{u_1, u_2} {I : Type u_1}
  {R : Type u_2} [TopologicalSpace I] [DiscreteTopology I] [DecidableEq I] [NormedCommRing R]
  [NormOneClass R] [IsUltrametricDist R] [CompleteSpace R] [TauCeti.NormedRing.IsTate R]
  {u : ZeroAtInftyContinuousMap I R →L[R] ZeroAtInftyContinuousMap I R} {B : PowerSeries R}
  (hu : u.IsRowCompact) (hB : B.IsEntire) (hB₀ : (PowerSeries.coeff 0) B = 0) :
  (B.evalAt u).matrixCoeff.charPowerSeries = B.colemanDEntire u.matrixCoeff.charPowerSeries
```

## Depends on

- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)
- [PowerSeries.colemanDEntire](powerseries-colemandentire.md)

## Proof depends on

- [Cauchy–Hadamard for entire series](../../../ring-theory/part-01/power-series/cauchy-hadamard-for-entire-series.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsRowCompact.charPowerSeries_eq_colemanDEntire`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/FunctionalCalculus.html#ContinuousLinearMap.IsRowCompact.charPowerSeries_eq_colemanDEntire).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsRowCompact.charPowerSeries_eq_colemanDEntire`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/FunctionalCalculus.html#ContinuousLinearMap.IsRowCompact.charPowerSeries_eq_colemanDEntire)
- [Source of `ContinuousLinearMap.IsRowCompact.charPowerSeries_eq_colemanDEntire` in TauCeti/Analysis/Normed/Operator/Nonarchimedean/FunctionalCalculus.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/Nonarchimedean/FunctionalCalculus.lean#L45)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CompactOperators/STATUS.md)
