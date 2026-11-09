---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.gradedSymmetricAlgebraAdjunction
statement: formalized
---

# TauCeti.AlgebraicGeometry.gradedSymmetricAlgebraAdjunction

The graded symmetric algebra functor is left adjoint to the degree-one functor: morphisms of
graded quasicoherent algebras `Sym F ⟶ A` correspond to morphisms of quasicoherent sheaves
`F ⟶ A₁`, by restriction to degree one along `F ≅ Sym¹ F` and by `gradedSymmetricAlgebraLift`.

```lean
TauCeti.AlgebraicGeometry.gradedSymmetricAlgebraAdjunction.{u} (X : AlgebraicGeometry.Scheme) :
  TauCeti.AlgebraicGeometry.gradedSymmetricAlgebra X ⊣
    TauCeti.AlgebraicGeometry.GradedQuasicoherentAlgebra.degreeOne
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.gradedSymmetricAlgebraAdjunction`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Modules/Quasicoherent/GradedAlgebra/SymmetricAlgebra/Adjunction.html#TauCeti.AlgebraicGeometry.gradedSymmetricAlgebraAdjunction).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.gradedSymmetricAlgebraAdjunction`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Modules/Quasicoherent/GradedAlgebra/SymmetricAlgebra/Adjunction.html#TauCeti.AlgebraicGeometry.gradedSymmetricAlgebraAdjunction)
- [Source of `TauCeti.AlgebraicGeometry.gradedSymmetricAlgebraAdjunction` in TauCeti/AlgebraicGeometry/Modules/Quasicoherent/GradedAlgebra/SymmetricAlgebra/Adjunction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Modules/Quasicoherent/GradedAlgebra/SymmetricAlgebra/Adjunction.lean#L317)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
