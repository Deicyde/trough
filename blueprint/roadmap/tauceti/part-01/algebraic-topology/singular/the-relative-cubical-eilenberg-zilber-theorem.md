---
declaration: theorem
origin: cited
lean: TauCeti.quasiIso_cubicalCrossProductRel
statement: formalized
proof: formalized
---

# The relative cubical Eilenberg–Zilber theorem

the relative cross product
`N(X) ⊗ N(Y, B) ⟶ N(X × Y, X × B)` is a quasi-isomorphism. By the five lemma, this follows from
the absolute Eilenberg–Zilber theorem for `X × B` and `X × Y`.

```lean
TauCeti.quasiIso_cubicalCrossProductRel.{u} (k : Type u) [CommRing k] (X : TopCat) (P : TopPair) :
  QuasiIso (TauCeti.cubicalCrossProductRel k X P)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The cubical Eilenberg–Zilber theorem](the-cubical-eilenberg-zilber-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.quasiIso_cubicalCrossProductRel`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Relative.html#TauCeti.quasiIso_cubicalCrossProductRel).

## Sources

- [Tau Ceti documentation: `TauCeti.quasiIso_cubicalCrossProductRel`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Relative.html#TauCeti.quasiIso_cubicalCrossProductRel)
- [Source of `TauCeti.quasiIso_cubicalCrossProductRel` in TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Relative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Singular/Cubical/Kunneth/Relative.lean#L219)
