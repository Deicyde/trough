---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.relativePicardDegreeZeroFunctor
statement: formalized
---

# The degree-zero Picard functor `Pic⁰_{X/S}` of a smooth proper geometrically connected family of curves `f : X ⟶ S`, as a presheaf of commutative groups on schemes over `S`

it sends
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

- [The Jacobian criterion for étaleness](../../ring-theory/other-results/part-01/the-jacobian-criterion-for-etaleness.md)
- [Riemann's theorem (Stichtenoth, Theorem 1.4.17)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-02/riemanns-theorem-stichtenoth-theorem-1-4-17.md)
- [The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form](../../field-theory/function-field/the-weak-approximation-theorem-for-the-places-of.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.relativePicardDegreeZeroFunctor`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/PicardFunctor/PicZero/Basic.html#TauCeti.AlgebraicGeometry.relativePicardDegreeZeroFunctor).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.relativePicardDegreeZeroFunctor`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/PicardFunctor/PicZero/Basic.html#TauCeti.AlgebraicGeometry.relativePicardDegreeZeroFunctor)
- [Source of `TauCeti.AlgebraicGeometry.relativePicardDegreeZeroFunctor` in TauCeti/AlgebraicGeometry/PicardFunctor/PicZero/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/PicardFunctor/PicZero/Basic.lean#L370)
- [Tau Ceti roadmap status: The Jacobian challenge (Christian Merten's AG version)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/JacobianChallenge/STATUS.md)
