---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsRowCompact.isUnit_one_sub_smul_iff
statement: formalized
proof: formalized
---

# Invertibility and the Fredholm series

For a row-compact endomorphism `u` of `C₀(I, R)`,
the operator `1 - a • u` is invertible if and only if the value `H_u(a)` of the Fredholm series
`det (1 - T u)` is a unit of `R`.

```lean
ContinuousLinearMap.IsRowCompact.isUnit_one_sub_smul_iff.{u_1, u_2} {I : Type u_1}
  [TopologicalSpace I] [DiscreteTopology I] [DecidableEq I] {R : Type u_2} [NormedCommRing R]
  [IsUltrametricDist R] [CompleteSpace R] [TauCeti.NormedRing.IsTate R]
  {u : ZeroAtInftyContinuousMap I R →L[R] ZeroAtInftyContinuousMap I R} (hu : u.IsRowCompact)
  {a : R} : IsUnit (1 - a • u) ↔ IsUnit (u.matrixCoeff.charPowerSeries.evalAt a)
```

## Depends on

- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsRowCompact.isUnit_one_sub_smul_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Spectrum.html#ContinuousLinearMap.IsRowCompact.isUnit_one_sub_smul_iff).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsRowCompact.isUnit_one_sub_smul_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Spectrum.html#ContinuousLinearMap.IsRowCompact.isUnit_one_sub_smul_iff)
- [Source of `ContinuousLinearMap.IsRowCompact.isUnit_one_sub_smul_iff` in TauCeti/Analysis/Normed/Operator/Nonarchimedean/Spectrum.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Spectrum.lean#L93)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CompactOperators/STATUS.md)
