---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.doubleRepresentableBy
statement: formalized
---

# TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.doubleRepresentableBy

The relative representing scheme of `Q` over the universal `(P, Q)`-family represents
`(P, Q, Q)`. The last `Q`-structure is the additional relative structure.

```lean
TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.doubleRepresentableBy.{u}
  {B : AlgebraicGeometry.Scheme} {P Q : TauCeti.AlgebraicGeometry.ModuliProblem B}
  (D : Q.RelRepData) {V : TauCeti.AlgebraicGeometry.EllObj B}
  (R :
    CategoryTheory.Functor.RepresentableBy (CategoryTheory.MonoidalCategoryStruct.tensorObj P Q)
      V) :
  CategoryTheory.Functor.RepresentableBy
    (CategoryTheory.MonoidalCategoryStruct.tensorObj P
      (CategoryTheory.MonoidalCategoryStruct.tensorObj Q Q))
    (V.baseChangeFunctor.obj (D.rep V))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.doubleRepresentableBy`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Rigidifier/Double.html#TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.doubleRepresentableBy).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.doubleRepresentableBy`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Rigidifier/Double.html#TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.doubleRepresentableBy)
- [Source of `TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.doubleRepresentableBy` in TauCeti/AlgebraicGeometry/ModularCurve/Rigidifier/Double.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/ModularCurve/Rigidifier/Double.lean#L45)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularCurves/STATUS.md)
