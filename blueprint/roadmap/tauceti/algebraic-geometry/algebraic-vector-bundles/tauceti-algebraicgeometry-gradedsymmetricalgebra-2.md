---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.gradedSymmetricAlgebraEquiv
statement: formalized
---

# TauCeti.AlgebraicGeometry.gradedSymmetricAlgebraEquiv

The graded symmetric algebra functor is an equivalence between quasicoherent sheaves and
graded quasicoherent algebras freely generated in degree one. Its inverse takes the degree-one
component, and its unit is the identification `F ≅ Sym¹ F`.

```lean
TauCeti.AlgebraicGeometry.gradedSymmetricAlgebraEquiv.{u} (X : AlgebraicGeometry.Scheme) :
  TauCeti.AlgebraicGeometry.QuasicoherentSheaf X ≌
    TauCeti.AlgebraicGeometry.FreeGradedQuasicoherentAlgebra X
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.gradedSymmetricAlgebraEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Modules/Quasicoherent/GradedAlgebra/Free.html#TauCeti.AlgebraicGeometry.gradedSymmetricAlgebraEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.gradedSymmetricAlgebraEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Modules/Quasicoherent/GradedAlgebra/Free.html#TauCeti.AlgebraicGeometry.gradedSymmetricAlgebraEquiv)
- [Source of `TauCeti.AlgebraicGeometry.gradedSymmetricAlgebraEquiv` in TauCeti/AlgebraicGeometry/Modules/Quasicoherent/GradedAlgebra/Free.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Modules/Quasicoherent/GradedAlgebra/Free.lean#L61)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
