---
declaration: theorem
origin: cited
lean: AddCircle.fundamentalGroupMulEquiv_eq_windingNumberIso
statement: formalized
proof: formalized
---

# AddCircle.fundamentalGroupMulEquiv_eq_windingNumberIso

For positive periods, the chosen-lift equivalence agrees with Mathlib's winding-number
isomorphism. In particular it is independent of the chosen lift and has the same orientation.

```lean
AddCircle.fundamentalGroupMulEquiv_eq_windingNumberIso (p : ℝ) [hp : Fact (0 < p)] {x : AddCircle p}
  (e : ↑(QuotientAddGroup.mk ⁻¹' {x})) :
  AddCircle.fundamentalGroupMulEquiv p ⋯ e = x.windingNumberIso
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AddCircle.fundamentalGroupMulEquiv_eq_windingNumberIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/Circle/FundamentalGroup.html#AddCircle.fundamentalGroupMulEquiv_eq_windingNumberIso).

## Sources

- [Tau Ceti documentation: `AddCircle.fundamentalGroupMulEquiv_eq_windingNumberIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/Circle/FundamentalGroup.html#AddCircle.fundamentalGroupMulEquiv_eq_windingNumberIso)
- [Source of `AddCircle.fundamentalGroupMulEquiv_eq_windingNumberIso` in TauCeti/AlgebraicTopology/UniversalCover/Circle/FundamentalGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/UniversalCover/Circle/FundamentalGroup.lean#L262)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/UniversalCovers/STATUS.md)
