---
declaration: instance
origin: cited
lean: TauCeti.AlgebraicGeometry.modObjRelativeSpecSymmetricAlgebra
statement: formalized
---

# `Spec_X (Sym F)` is a module over the affine line

The scalar multiplication
`relativeSpecSymmetricAlgebraSMul` is an action of the multiplicative monoid object `𝔸¹_X` of
`Over X`.

```lean
TauCeti.AlgebraicGeometry.modObjRelativeSpecSymmetricAlgebra.{u} {X : AlgebraicGeometry.Scheme}
  (F : TauCeti.AlgebraicGeometry.QuasicoherentSheaf X) :
  CategoryTheory.ModObj ((AlgebraicGeometry.AffineSpace PUnit.{u + 1} X).asOver X)
    ((CategoryTheory.MorphismProperty.Over.forget @AlgebraicGeometry.IsAffineHom ⊤ X).obj
      ((TauCeti.AlgebraicGeometry.relativeSpec X).obj
        (Opposite.op ((TauCeti.AlgebraicGeometry.symmetricAlgebra X).obj F))))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.modObjRelativeSpecSymmetricAlgebra`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/RelativeSpec/SymmetricAlgebra/Module.html#TauCeti.AlgebraicGeometry.modObjRelativeSpecSymmetricAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.modObjRelativeSpecSymmetricAlgebra`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/RelativeSpec/SymmetricAlgebra/Module.html#TauCeti.AlgebraicGeometry.modObjRelativeSpecSymmetricAlgebra)
- [Source of `TauCeti.AlgebraicGeometry.modObjRelativeSpecSymmetricAlgebra` in TauCeti/AlgebraicGeometry/RelativeSpec/SymmetricAlgebra/Module.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/RelativeSpec/SymmetricAlgebra/Module.lean#L129)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
