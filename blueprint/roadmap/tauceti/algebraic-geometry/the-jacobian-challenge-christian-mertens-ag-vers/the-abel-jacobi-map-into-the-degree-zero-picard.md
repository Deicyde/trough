---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.abelJacobiMapToPicZeroFppf
statement: formalized
---

# The Abel–Jacobi map into the degree-zero Picard fppf sheaf

It sends an `S`-point
`x : T ⟶ X` to the fppf-local class of `𝒪(Γₓ - x₀,T)`.

```lean
TauCeti.AlgebraicGeometry.abelJacobiMapToPicZeroFppf.{u} {S X : AlgebraicGeometry.Scheme}
  (f : X ⟶ S) [AlgebraicGeometry.IsProper f] [AlgebraicGeometry.SmoothOfRelativeDimension 1 f]
  [AlgebraicGeometry.GeometricallyConnected f] {x₀ : S ⟶ X}
  (hx₀ : CategoryTheory.CategoryStruct.comp x₀ f = CategoryTheory.CategoryStruct.id S) :
  (CategoryTheory.yoneda.obj (CategoryTheory.Over.mk f)).comp
      CategoryTheory.uliftFunctor.{u + 1, u} ⟶
    (TauCeti.AlgebraicGeometry.relativePicardDegreeZeroFppfSheaf f).obj.comp
      (CategoryTheory.forget AddCommGrpCat)
```

## Depends on

- [The degree-zero Picard functor `Pic⁰_{X/S}` of a smooth proper geometrically connected family of curves `f : X ⟶ S`, as a presheaf of commutative groups on schemes over `S`](the-degree-zero-picard-functor-pic0-x-s-of-a-smo.md)

## Proof depends on

- [The Jacobian criterion for étaleness](../../ring-theory/other-results/part-01/the-jacobian-criterion-for-etaleness.md)
- [Riemann's theorem (Stichtenoth, Theorem 1.4.17)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-02/riemanns-theorem-stichtenoth-theorem-1-4-17.md)
- [Serre's vanishing theorem on affine schemes](../other-results/serres-vanishing-theorem-on-affine-schemes.md)
- [TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf](../algebraic-vector-bundles/tauceti-algebraicgeometry-finitelocallyfreesheaf-3.md)
- [The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form](../../field-theory/function-field/the-weak-approximation-theorem-for-the-places-of.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.abelJacobiMapToPicZeroFppf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/PicardFunctor/Abel/Fppf.html#TauCeti.AlgebraicGeometry.abelJacobiMapToPicZeroFppf).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.abelJacobiMapToPicZeroFppf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/PicardFunctor/Abel/Fppf.html#TauCeti.AlgebraicGeometry.abelJacobiMapToPicZeroFppf)
- [Source of `TauCeti.AlgebraicGeometry.abelJacobiMapToPicZeroFppf` in TauCeti/AlgebraicGeometry/PicardFunctor/Abel/Fppf.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/PicardFunctor/Abel/Fppf.lean#L89)
- [Tau Ceti roadmap status: The Jacobian challenge (Christian Merten's AG version)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/JacobianChallenge/STATUS.md)
