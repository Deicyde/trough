---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsRowCompact.evalAt_charPowerSeries_eq_zero_iff_hasEigenvalue
statement: formalized
proof: formalized
---

# ContinuousLinearMap.IsRowCompact.evalAt_charPowerSeries_eq_zero_iff_hasEigenvalue

The zeros of the Fredholm series of a row-compact operator are exactly the inverses of its
nonzero eigenvalues. This conclusion concerns eigenvalues in the given coefficient field.

```lean
ContinuousLinearMap.IsRowCompact.evalAt_charPowerSeries_eq_zero_iff_hasEigenvalue.{u_1, u_2}
  {K : Type u_1} {I : Type u_2} [NontriviallyNormedField K] [CompleteSpace K] [IsUltrametricDist K]
  [TopologicalSpace I] [DiscreteTopology I] [DecidableEq I]
  {u : ZeroAtInftyContinuousMap I K →L[K] ZeroAtInftyContinuousMap I K} (hu : u.IsRowCompact)
  {a : K} : u.matrixCoeff.charPowerSeries.evalAt a = 0 ↔ a ≠ 0 ∧ Module.End.HasEigenvalue (↑u) a⁻¹
```

## Depends on

- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)

## Proof depends on

- [ContinuousLinearMap.charPowerSeries](continuouslinearmap-charpowerseries.md)
- [ContinuousLinearMap.IsCompletelyContinuous.isFredholm_one_sub](continuouslinearmap-iscompletelycontinuous-isfre.md)
- [The Fredholm determinant is entire](the-fredholm-determinant-is-entire.md)
- [Independence of the presentation](independence-of-the-presentation.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsRowCompact.evalAt_charPowerSeries_eq_zero_iff_hasEigenvalue`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Eigenvalues.html#ContinuousLinearMap.IsRowCompact.evalAt_charPowerSeries_eq_zero_iff_hasEigenvalue).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsRowCompact.evalAt_charPowerSeries_eq_zero_iff_hasEigenvalue`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Eigenvalues.html#ContinuousLinearMap.IsRowCompact.evalAt_charPowerSeries_eq_zero_iff_hasEigenvalue)
- [Source of `ContinuousLinearMap.IsRowCompact.evalAt_charPowerSeries_eq_zero_iff_hasEigenvalue` in TauCeti/Analysis/Normed/Operator/Nonarchimedean/Eigenvalues.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Eigenvalues.lean#L54)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CompactOperators/STATUS.md)
