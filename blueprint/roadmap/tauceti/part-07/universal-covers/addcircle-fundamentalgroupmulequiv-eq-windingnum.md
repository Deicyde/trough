---
declaration: theorem
origin: cited
lean: AddCircle.fundamentalGroupMulEquiv_eq_windingNumberIso
statement: formalized
proof: formalized
---

# AddCircle.fundamentalGroupMulEquiv\_eq\_windingNumberIso

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
- [Source of `AddCircle.fundamentalGroupMulEquiv_eq_windingNumberIso` in TauCeti/AlgebraicTopology/UniversalCover/Circle/FundamentalGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/UniversalCover/Circle/FundamentalGroup.lean#L262)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/UniversalCovers/STATUS.md)
