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

- [The degree-zero Picard functor `Pic⁰_{X/S}`](the-degree-zero-picard-functor-pic0-x-s.md)

## Proof depends on

- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [Serre's vanishing theorem on affine opens](../other-results/serres-vanishing-theorem-on-affine-opens.md)
- [TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf](../algebraic-vector-bundles/tauceti-algebraicgeometry-finitelocallyfreesheaf-2.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.abelJacobiMapToPicZeroFppf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/PicardFunctor/Abel/Fppf.html#TauCeti.AlgebraicGeometry.abelJacobiMapToPicZeroFppf).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.abelJacobiMapToPicZeroFppf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/PicardFunctor/Abel/Fppf.html#TauCeti.AlgebraicGeometry.abelJacobiMapToPicZeroFppf)
- [Source of `TauCeti.AlgebraicGeometry.abelJacobiMapToPicZeroFppf` in TauCeti/AlgebraicGeometry/PicardFunctor/Abel/Fppf.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/PicardFunctor/Abel/Fppf.lean#L89)
- [Tau Ceti roadmap status: The Jacobian challenge (Christian Merten's AG version)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/JacobianChallenge/STATUS.md)
