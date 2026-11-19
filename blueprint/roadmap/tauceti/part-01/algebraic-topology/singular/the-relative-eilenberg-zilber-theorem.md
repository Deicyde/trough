---
declaration: theorem
origin: cited
lean: TopCat.quasiIso_shuffleRel, TopPair.quasiIso_cubicalCrossProduct
statement: formalized
proof: formalized
---

# The relative Eilenberg–Zilber theorem

the relative shuffle map
`C(X, B; R) ⊗ C(Y; S) ⟶ C(X × Y, fst⁻¹(B); R ⊗ S)` is a quasi-isomorphism. By the five lemma, this
follows from the absolute Eilenberg–Zilber theorem for `B × Y` and `X × Y`.

```lean
TopCat.quasiIso_shuffleRel.{w, v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Abelian C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.MonoidalPreadditive C] [CategoryTheory.Limits.HasCoproducts C]
  [∀ (T : C) (J : Type w),
      CategoryTheory.Limits.PreservesColimitsOfShape (CategoryTheory.Discrete J)
        (CategoryTheory.MonoidalCategory.tensorLeft T)]
  [∀ (T : C) (J : Type w),
      CategoryTheory.Limits.PreservesColimitsOfShape (CategoryTheory.Discrete J)
        (CategoryTheory.MonoidalCategory.tensorRight T)]
  (X Y : TopCat) (B : Set ↑X) (R S : C) : QuasiIso (X.shuffleRel Y B R S)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The cubical Eilenberg–Zilber theorem](the-cubical-eilenberg-zilber-theorem.md)
- [The Eilenberg–Zilber theorem for singular chains](the-eilenberg-zilber-theorem-for-singular-chains.md)

## Lean

Formalized in Tau Ceti as [`TopCat.quasiIso_shuffleRel`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Kunneth/Relative.html#TopCat.quasiIso_shuffleRel).

## Other forms

**The relative Eilenberg–Zilber theorem.** Formalized in Tau Ceti as [`TopPair.quasiIso_cubicalCrossProduct`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Comparison/Relative/Kunneth.html#TopPair.quasiIso_cubicalCrossProduct).

```lean
TopPair.quasiIso_cubicalCrossProduct.{u} (k : Type u) [CommRing k] (P : TopPair) (Y : TopCat) :
  QuasiIso (TopPair.cubicalCrossProduct k P Y)
```

## Sources

- [Tau Ceti documentation: `TopCat.quasiIso_shuffleRel`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Kunneth/Relative.html#TopCat.quasiIso_shuffleRel)
- [Source of `TopCat.quasiIso_shuffleRel` in TauCeti/AlgebraicTopology/Singular/Kunneth/Relative.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/Kunneth/Relative.lean#L257)
