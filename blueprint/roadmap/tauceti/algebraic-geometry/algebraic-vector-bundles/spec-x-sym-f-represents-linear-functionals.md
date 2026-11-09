---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.relativeSpecSymmetricAlgebraPullbackHomEquiv
statement: formalized
---

# `Spec_X (Sym F)` represents linear functionals

For a quasicoherent sheaf `F` on `X` and a
scheme `q : T ⟶ X` over `X`, morphisms `T ⟶ Spec_X (Sym F)` over `X` correspond to morphisms of
`𝒪_T`-modules `q^* F ⟶ 𝒪_T`. It is `relativeSpecSymmetricAlgebraHomEquiv` followed by the
adjunction between pullback and pushforward of modules.

```lean
TauCeti.AlgebraicGeometry.relativeSpecSymmetricAlgebraPullbackHomEquiv.{u}
  {X : AlgebraicGeometry.Scheme} (F : TauCeti.AlgebraicGeometry.QuasicoherentSheaf X)
  (T : CategoryTheory.Over X) :
  (T ⟶
      (CategoryTheory.MorphismProperty.Over.forget @AlgebraicGeometry.IsAffineHom ⊤ X).obj
        ((TauCeti.AlgebraicGeometry.relativeSpec X).obj
          (Opposite.op ((TauCeti.AlgebraicGeometry.symmetricAlgebra X).obj F)))) ≃
    ((AlgebraicGeometry.Scheme.Modules.pullback T.hom).obj F.obj ⟶
      CategoryTheory.MonoidalCategoryStruct.tensorUnit T.left.Modules)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.relativeSpecSymmetricAlgebraPullbackHomEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/RelativeSpec/SymmetricAlgebra/Basic.html#TauCeti.AlgebraicGeometry.relativeSpecSymmetricAlgebraPullbackHomEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.relativeSpecSymmetricAlgebraPullbackHomEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/RelativeSpec/SymmetricAlgebra/Basic.html#TauCeti.AlgebraicGeometry.relativeSpecSymmetricAlgebraPullbackHomEquiv)
- [Source of `TauCeti.AlgebraicGeometry.relativeSpecSymmetricAlgebraPullbackHomEquiv` in TauCeti/AlgebraicGeometry/RelativeSpec/SymmetricAlgebra/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/RelativeSpec/SymmetricAlgebra/Basic.lean#L203)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
