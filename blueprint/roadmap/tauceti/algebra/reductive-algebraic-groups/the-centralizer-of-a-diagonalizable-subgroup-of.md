---
declaration: theorem
origin: cited
lean: BialgHom.smoothCommHopfAlgProperty_quotient_centralizerHopfIdeal
statement: formalized
proof: formalized
---

# The centralizer of a diagonalizable subgroup of a smooth affine group of finite type is smooth, over any base ring

```lean
BialgHom.smoothCommHopfAlgProperty_quotient_centralizerHopfIdeal.{u, v, w} {R : Type u} {X : Type w}
  [CommRing R] [CommGroup X] {H : TauCeti.FiniteTypeCommHopfAlgCat R} [Algebra.Smooth R ↑H.obj]
  (π : ↑H.obj →ₐc[R] MonoidAlgebra R X) :
  TauCeti.smoothCommHopfAlgProperty R (H.quotient π.centralizerHopfIdeal).obj
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`BialgHom.smoothCommHopfAlgProperty_quotient_centralizerHopfIdeal`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/DiagonalizableGroup/Centralizer/Smooth.html#BialgHom.smoothCommHopfAlgProperty_quotient_centralizerHopfIdeal).

## Sources

- [Tau Ceti documentation: `BialgHom.smoothCommHopfAlgProperty_quotient_centralizerHopfIdeal`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/DiagonalizableGroup/Centralizer/Smooth.html#BialgHom.smoothCommHopfAlgProperty_quotient_centralizerHopfIdeal)
- [Source of `BialgHom.smoothCommHopfAlgProperty_quotient_centralizerHopfIdeal` in TauCeti/Algebra/AlgebraicGroup/DiagonalizableGroup/Centralizer/Smooth.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/AlgebraicGroup/DiagonalizableGroup/Centralizer/Smooth.lean#L321)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ReductiveGroups/STATUS.md)
