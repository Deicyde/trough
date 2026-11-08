---
declaration: theorem
origin: cited
lean: TauCeti.quasiIso_cubicalCrossProduct
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

- [The Eilenberg–Zilber theorem](../other-results/the-eilenberg-zilber-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.quasiIso_cubicalCrossProduct`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth.html#TauCeti.quasiIso_cubicalCrossProduct).

## Sources

- [Tau Ceti documentation: `TauCeti.quasiIso_cubicalCrossProduct`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth.html#TauCeti.quasiIso_cubicalCrossProduct)
- [Source of `TauCeti.quasiIso_cubicalCrossProduct` in TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth.lean#L88)
