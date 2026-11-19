---
declaration: theorem
origin: cited
lean: Circle.fundamentalGroupMulEquiv_fromPath
statement: formalized
proof: formalized
---

# The isomorphism `π₁(S¹) ≃* ℤ` is the degree

The class of a loop is sent to its degree
`Circle.degree`, the number of full turns of any continuous angle lift.

```lean
Circle.fundamentalGroupMulEquiv_fromPath {x : Circle} (γ : Path x x) :
  x.fundamentalGroupMulEquiv (FundamentalGroup.fromPath (Path.Homotopic.Quotient.mk γ)) =
    Multiplicative.ofAdd (Circle.degree γ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [AddCircle.fundamentalGroupMulEquiv_eq_windingNumberIso](addcircle-fundamentalgroupmulequiv-eq-windingnum.md)

## Lean

Formalized in Tau Ceti as [`Circle.fundamentalGroupMulEquiv_fromPath`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/Circle/FundamentalGroup.html#Circle.fundamentalGroupMulEquiv_fromPath).

## Sources

- [Tau Ceti documentation: `Circle.fundamentalGroupMulEquiv_fromPath`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/Circle/FundamentalGroup.html#Circle.fundamentalGroupMulEquiv_fromPath)
- [Source of `Circle.fundamentalGroupMulEquiv_fromPath` in TauCeti/AlgebraicTopology/UniversalCover/Circle/FundamentalGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/UniversalCover/Circle/FundamentalGroup.lean#L411)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/UniversalCovers/STATUS.md)
