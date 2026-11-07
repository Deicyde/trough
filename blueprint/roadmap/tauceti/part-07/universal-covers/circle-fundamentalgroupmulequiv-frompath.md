---
declaration: theorem
origin: cited
lean: Circle.fundamentalGroupMulEquiv_fromPath
statement: formalized
proof: formalized
---

# Circle.fundamentalGroupMulEquiv\_fromPath

**The isomorphism `π₁(S¹) ≃* ℤ` is the degree.** The class of a loop is sent to its degree
`Circle.degree`, the number of full turns of any continuous angle lift.

```lean
Circle.fundamentalGroupMulEquiv_fromPath {x : Circle} (γ : Path x x) :
  x.fundamentalGroupMulEquiv (FundamentalGroup.fromPath (Path.Homotopic.Quotient.mk γ)) =
    Multiplicative.ofAdd (Circle.degree γ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [AddCircle.fundamentalGroupMulEquiv\_eq\_windingNumberIso](addcircle-fundamentalgroupmulequiv-eq-windingnum.md)

## Lean

Formalized in Tau Ceti as [`Circle.fundamentalGroupMulEquiv_fromPath`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/Circle/FundamentalGroup.html#Circle.fundamentalGroupMulEquiv_fromPath).

## Sources

- [Tau Ceti documentation: `Circle.fundamentalGroupMulEquiv_fromPath`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/Circle/FundamentalGroup.html#Circle.fundamentalGroupMulEquiv_fromPath)
- [Source of `Circle.fundamentalGroupMulEquiv_fromPath` in TauCeti/AlgebraicTopology/UniversalCover/Circle/FundamentalGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/UniversalCover/Circle/FundamentalGroup.lean#L404)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/UniversalCovers/STATUS.md)
