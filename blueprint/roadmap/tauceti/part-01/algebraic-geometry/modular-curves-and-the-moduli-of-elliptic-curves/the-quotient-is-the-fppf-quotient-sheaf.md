---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.isColimitFppfYonedaDoubleQuotientCofork
statement: formalized
---

# The quotient is the fppf quotient sheaf

If `𝒫` is rigid, then under the Yoneda embedding
into fppf sheaves, the projection `𝕄(𝒫, δ) ⟶ 𝕄(𝒫)` is the coequalizer of the two forgetful
projections from the scheme of two rigidifications.

```lean
TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.isColimitFppfYonedaDoubleQuotientCofork.{u}
  {B : AlgebraicGeometry.Scheme} {P Q : TauCeti.AlgebraicGeometry.ModuliProblem B}
  (D : Q.RelRepData) {V : TauCeti.AlgebraicGeometry.EllObj B}
  (R :
    CategoryTheory.Functor.RepresentableBy (CategoryTheory.MonoidalCategoryStruct.tensorObj P Q) V)
  [AlgebraicGeometry.IsAffine V.base] [AlgebraicGeometry.IsFinite (D.rep V).hom]
  [AlgebraicGeometry.Flat (D.rep V).hom]
  [AlgebraicGeometry.LocallyOfFinitePresentation (D.rep V).hom] (hP : P.IsRigid) :
  CategoryTheory.Limits.IsColimit
    (CategoryTheory.Limits.Cofork.ofπ
      (AlgebraicGeometry.Scheme.fppfTopology.yoneda.map (D.doubleQuotientπ R)) ⋯)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cayley–Hamilton on a finite projective module](../../linear-algebra/part-02/other-results/cayley-hamilton-on-a-finite-projective-module.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.isColimitFppfYonedaDoubleQuotientCofork`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Rigidifier/Quotient.html#TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.isColimitFppfYonedaDoubleQuotientCofork).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.isColimitFppfYonedaDoubleQuotientCofork`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Rigidifier/Quotient.html#TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.isColimitFppfYonedaDoubleQuotientCofork)
- [Source of `TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.isColimitFppfYonedaDoubleQuotientCofork` in TauCeti/AlgebraicGeometry/ModularCurve/Rigidifier/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/ModularCurve/Rigidifier/Quotient.lean#L200)
- [Tau Ceti roadmap status: Modular curves and the moduli of elliptic curves with level structure](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ModularCurves/STATUS.md)
