---
declaration: theorem
origin: cited
lean: TauCeti.quasiIso_cubicalCrossProduct, TauCeti.quasiIso_cubicalCrossProductPair
statement: formalized
proof: formalized
---

# The cubical Eilenberg–Zilber theorem

the cross product of normalized cubical chains
`N(X; k) ⊗ N(Y; k) ⟶ N(X × Y; k)` is a quasi-isomorphism.

```lean
TauCeti.quasiIso_cubicalCrossProduct.{u} (k : Type u) [CommRing k] (X Y : TopCat) :
  QuasiIso (TauCeti.cubicalCrossProduct k X Y)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Eilenberg–Zilber theorem for singular chains](the-eilenberg-zilber-theorem-for-singular-chains.md)
- [The relative cubical Eilenberg–Zilber theorem](the-relative-cubical-eilenberg-zilber-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.quasiIso_cubicalCrossProduct`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth.html#TauCeti.quasiIso_cubicalCrossProduct).

## Other forms

**The cubical Eilenberg–Zilber theorem for a product of pairs.** Formalized in Tau Ceti as [`TauCeti.quasiIso_cubicalCrossProductPair`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Pair.html#TauCeti.quasiIso_cubicalCrossProductPair).

```lean
TauCeti.quasiIso_cubicalCrossProductPair.{u} (k : Type u) [CommRing k] (P Q : TopPair) :
  QuasiIso (TauCeti.cubicalCrossProductPair k P Q)
```

## Sources

- [Tau Ceti documentation: `TauCeti.quasiIso_cubicalCrossProduct`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth.html#TauCeti.quasiIso_cubicalCrossProduct)
- [Source of `TauCeti.quasiIso_cubicalCrossProduct` in TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth.lean#L88)
