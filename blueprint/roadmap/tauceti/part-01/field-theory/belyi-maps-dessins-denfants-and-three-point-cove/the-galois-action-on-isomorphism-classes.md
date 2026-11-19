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
- [Source of `TauCeti.AlgebraicBelyiPair.IsoClass.instMulAction` in TauCeti/FieldTheory/FunctionField/Belyi/GaloisAction.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/FieldTheory/FunctionField/Belyi/GaloisAction.lean#L247)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BelyiMaps/STATUS.md)
