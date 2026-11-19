---
declaration: def
origin: cited
lean: TauCeti.multiplicativeSquareClassEquiv
statement: formalized
---

# TauCeti.multiplicativeSquareClassEquiv

The canonical equivalence from the literal multiplicative quotient of units by squares to
the multiplicative form of the additive square-class group.

```lean
TauCeti.multiplicativeSquareClassEquiv.{u_1} {K : Type u_1} [Field K] :
  TauCeti.MultiplicativeSquareClassGroup K ≃* Multiplicative (TauCeti.SquareClassGroup K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.multiplicativeSquareClassEquiv`](https://taucetiproject.org/docs/TauCeti/FieldTheory/SquareClassGroup/Multiplicative.html#TauCeti.multiplicativeSquareClassEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.multiplicativeSquareClassEquiv`](https://taucetiproject.org/docs/TauCeti/FieldTheory/SquareClassGroup/Multiplicative.html#TauCeti.multiplicativeSquareClassEquiv)
- [Source of `TauCeti.multiplicativeSquareClassEquiv` in TauCeti/FieldTheory/SquareClassGroup/Multiplicative.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/FieldTheory/SquareClassGroup/Multiplicative.lean#L94)
- [Tau Ceti roadmap status: Orthogonal and spin groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/OrthogonalSpinGroups/STATUS.md)
