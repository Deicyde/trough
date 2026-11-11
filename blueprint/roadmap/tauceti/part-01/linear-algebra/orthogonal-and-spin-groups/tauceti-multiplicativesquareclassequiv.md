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
- [Source of `TauCeti.multiplicativeSquareClassEquiv` in TauCeti/FieldTheory/SquareClassGroup/Multiplicative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/SquareClassGroup/Multiplicative.lean#L82)
- [Tau Ceti roadmap status: Orthogonal and spin groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/OrthogonalSpinGroups/STATUS.md)
