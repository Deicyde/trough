---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsRieszProjection.charPowerSeries_matrixCoeff_eq_pow_mul
statement: formalized
proof: formalized
---

# Factorisation along a Riesz splitting

At a good zero of order `h`, the Fredholm series
factors as `(1 - a⁻¹ X) ^ h`, with `a⁻¹ = Ring.inverse a`, times the Fredholm factor of the
complementary summand, which is a unit at `a`
(`ContinuousLinearMap.IsRieszProjection.isUnit_evalAt_charPowerSeries_complement`).

```lean
ContinuousLinearMap.IsRieszProjection.charPowerSeries_matrixCoeff_eq_pow_mul.{u_1, u_2}
  {I : Type u_1} {R : Type u_2} [TopologicalSpace I] [DiscreteTopology I] [DecidableEq I]
  [NormedCommRing R] [TauCeti.NormedRing.IsTate R] [IsUltrametricDist R] [CompleteSpace R]
  {u E : ZeroAtInftyContinuousMap I R →L[R] ZeroAtInftyContinuousMap I R} {a : R} {h : ℕ}
  (hE : u.IsRieszProjection a h E) (hu : u.IsRowCompact)
  (hH : u.matrixCoeff.charPowerSeries.IsGoodZero a h) :
  u.matrixCoeff.charPowerSeries =
    (1 - PowerSeries.C (Ring.inverse a) * PowerSeries.X) ^ h *
      (u * (1 - E)).matrixCoeff.charPowerSeries
```

## Depends on

- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)

## Proof depends on

- [Factor theorem for entire series](../../../ring-theory/part-01/power-series/factor-theorem-for-entire-series.md)
- [Quantitative Open Mapping Theorem](../../part-03/normed/part-02/quantitative-open-mapping-theorem.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsRieszProjection.charPowerSeries_matrixCoeff_eq_pow_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/RieszProjection/Multiplicity.html#ContinuousLinearMap.IsRieszProjection.charPowerSeries_matrixCoeff_eq_pow_mul).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsRieszProjection.charPowerSeries_matrixCoeff_eq_pow_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/RieszProjection/Multiplicity.html#ContinuousLinearMap.IsRieszProjection.charPowerSeries_matrixCoeff_eq_pow_mul)
- [Source of `ContinuousLinearMap.IsRieszProjection.charPowerSeries_matrixCoeff_eq_pow_mul` in TauCeti/Analysis/Normed/Operator/Nonarchimedean/RieszProjection/Multiplicity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/Nonarchimedean/RieszProjection/Multiplicity.lean#L182)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CompactOperators/STATUS.md)
