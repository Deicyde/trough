---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.relativePicardFppfSheaf
statement: formalized
---

# TauCeti.AlgebraicGeometry.relativePicardFppfSheaf

The **relative Picard fppf sheaf** of `f : X ⟶ S`, obtained by sheafifying the presheaf
`T ↦ Pic(X_T) / Pic(T)` on the fppf site of schemes over `S`.

This definition does not assert that the resulting sheaf is representable.

```lean
TauCeti.AlgebraicGeometry.relativePicardFppfSheaf.{u} {S X : AlgebraicGeometry.Scheme} (f : X ⟶ S) :
  CategoryTheory.Sheaf (AlgebraicGeometry.Scheme.fppfTopology.over S) AddCommGrpCat
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.relativePicardFppfSheaf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/PicardFunctor/Fppf.html#TauCeti.AlgebraicGeometry.relativePicardFppfSheaf).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.relativePicardFppfSheaf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/PicardFunctor/Fppf.html#TauCeti.AlgebraicGeometry.relativePicardFppfSheaf)
- [Source of `TauCeti.AlgebraicGeometry.relativePicardFppfSheaf` in TauCeti/AlgebraicGeometry/PicardFunctor/Fppf.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/PicardFunctor/Fppf.lean#L100)
- [Tau Ceti roadmap status: The Jacobian challenge (Christian Merten's AG version)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/JacobianChallenge/STATUS.md)
