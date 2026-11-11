---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.relativePicardDegreeZeroFunctor
statement: formalized
---

# The degree-zero Picard functor `Pic⁰_{X/S}`

**The degree-zero Picard functor `Pic⁰_{X/S}`** of a smooth proper geometrically connected
family of curves `f : X ⟶ S`, as a presheaf of commutative groups on schemes over `S`: it sends
`T` to the subgroup `relativePicardDegreeZeroSubgroup f T` of `Pic(X_T) / Pic(T)`, and a morphism
over `S` to the restriction of the pullback map of the relative Picard presheaf.

```lean
TauCeti.AlgebraicGeometry.relativePicardDegreeZeroFunctor.{u} {S X : AlgebraicGeometry.Scheme}
  (f : X ⟶ S) [AlgebraicGeometry.IsProper f] [AlgebraicGeometry.SmoothOfRelativeDimension 1 f]
  [AlgebraicGeometry.GeometricallyConnected f] :
  CategoryTheory.Functor (CategoryTheory.Over S)ᵒᵖ CommGrpCat
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.relativePicardDegreeZeroFunctor`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/PicardFunctor/PicZero/Basic.html#TauCeti.AlgebraicGeometry.relativePicardDegreeZeroFunctor).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.relativePicardDegreeZeroFunctor`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/PicardFunctor/PicZero/Basic.html#TauCeti.AlgebraicGeometry.relativePicardDegreeZeroFunctor)
- [Source of `TauCeti.AlgebraicGeometry.relativePicardDegreeZeroFunctor` in TauCeti/AlgebraicGeometry/PicardFunctor/PicZero/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/PicardFunctor/PicZero/Basic.lean#L363)
- [Tau Ceti roadmap status: The Jacobian challenge (Christian Merten's AG version)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/JacobianChallenge/STATUS.md)
