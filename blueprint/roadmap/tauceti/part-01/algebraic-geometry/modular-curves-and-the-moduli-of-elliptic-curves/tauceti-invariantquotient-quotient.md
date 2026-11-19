---
declaration: def
origin: cited
lean: TauCeti.InvariantQuotient.quotient
statement: formalized
---

# TauCeti.InvariantQuotient.quotient

The **quotient of `X` by `G`**: the gluing of the affine invariant quotients `Spec Γ(X, U)ᴳ` of
the invariant affine opens `U` of `X` along the open immersions induced by restriction.

```lean
TauCeti.InvariantQuotient.quotient.{u, v} {X : AlgebraicGeometry.Scheme} {G : Type v} [Group G]
  (σ : G →* CategoryTheory.Aut X) [Finite G] : AlgebraicGeometry.Scheme
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.InvariantQuotient.quotient`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Quotient/FiniteGroup/Glued/Basic.html#TauCeti.InvariantQuotient.quotient).

## Sources

- [Tau Ceti documentation: `TauCeti.InvariantQuotient.quotient`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Quotient/FiniteGroup/Glued/Basic.html#TauCeti.InvariantQuotient.quotient)
- [Source of `TauCeti.InvariantQuotient.quotient` in TauCeti/AlgebraicGeometry/Quotient/FiniteGroup/Glued/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Quotient/FiniteGroup/Glued/Basic.lean#L436)
- [Tau Ceti roadmap status: Modular curves and the moduli of elliptic curves with level structure](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ModularCurves/STATUS.md)
