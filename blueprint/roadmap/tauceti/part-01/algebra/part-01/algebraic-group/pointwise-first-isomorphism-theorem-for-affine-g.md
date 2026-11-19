---
declaration: def
origin: cited
lean: TauCeti.CommHopfAlgCat.kernelPointwiseQuotientIso
statement: formalized
---

# Pointwise first isomorphism theorem for affine groups

If the morphism represented by
`f` is surjective on `A`-points, the target group of points is isomorphic to the pointwise
quotient of source points by the scheme-theoretic kernel.

```lean
TauCeti.CommHopfAlgCat.kernelPointwiseQuotientIso.{u, v, w} {R : Type u} [CommRing R]
  {H K : CommHopfAlgCat R} (f : H ⟶ K) (A : CommAlgCat R)
  (hsurj :
    Function.Surjective
      ⇑(CategoryTheory.ConcreteCategory.hom ((CommHopfAlgCat.Hom.mapPointsFunctor f).app A))) :
  TauCeti.CommHopfAlgCat.pointwiseQuotientGroup K (TauCeti.CommHopfAlgCat.kernelHopfIdeal f) ⋯ A ≅
    TauCeti.HopfAlgebra.points A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CommHopfAlgCat.kernelPointwiseQuotientIso`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/HopfIdeal/Quotient/Kernel/Presheaf.html#TauCeti.CommHopfAlgCat.kernelPointwiseQuotientIso).

## Sources

- [Tau Ceti documentation: `TauCeti.CommHopfAlgCat.kernelPointwiseQuotientIso`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/HopfIdeal/Quotient/Kernel/Presheaf.html#TauCeti.CommHopfAlgCat.kernelPointwiseQuotientIso)
- [Source of `TauCeti.CommHopfAlgCat.kernelPointwiseQuotientIso` in TauCeti/Algebra/AlgebraicGroup/HopfIdeal/Quotient/Kernel/Presheaf.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/AlgebraicGroup/HopfIdeal/Quotient/Kernel/Presheaf.lean#L242)
