---
declaration: instance
origin: cited
lean: TauCeti.AlgebraicBelyiPair.IsoClass.instMulAction
statement: formalized
---

# The Galois action on isomorphism classes

a group `G` acting on `k` by ring automorphisms
acts on the isomorphism classes of algebraic Belyi pairs over `k` by conjugation,
`g • c = c.conj (MulSemiringAction.toRingEquiv G k g)`. For `G = Gal(AlgebraicClosure ℚ/ℚ)`
acting on `AlgebraicClosure ℚ` this is the action of the absolute Galois group on Belyi maps.

```lean
TauCeti.AlgebraicBelyiPair.IsoClass.instMulAction.{u, u_1} {k : Type u} [Field k] [CharZero k]
  {G : Type u_1} [Group G] [MulSemiringAction G k] :
  MulAction G (TauCeti.AlgebraicBelyiPair.IsoClass k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicBelyiPair.IsoClass.instMulAction`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Belyi/GaloisAction.html#TauCeti.AlgebraicBelyiPair.IsoClass.instMulAction).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicBelyiPair.IsoClass.instMulAction`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Belyi/GaloisAction.html#TauCeti.AlgebraicBelyiPair.IsoClass.instMulAction)
- [Source of `TauCeti.AlgebraicBelyiPair.IsoClass.instMulAction` in TauCeti/FieldTheory/FunctionField/Belyi/GaloisAction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/FunctionField/Belyi/GaloisAction.lean#L247)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BelyiMaps/STATUS.md)
