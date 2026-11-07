---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.relativeSpecPullbackIso_comp
statement: formalized
proof: formalized
---

# Relative Spec commutes with base change, compatibly with composition

For `g : Z ⟶ Y`
and `f : Y ⟶ X`, the isomorphism `Spec_Z ((g ≫ f)^* A) ≅ Z ×_X Spec_X A` is the composite of the
identification `Spec_Z ((g ≫ f)^* A) ≅ Spec_Z (g^* f^* A)`, the isomorphisms for `g` and for `f`,
and the canonical isomorphism `Z ×_Y (Y ×_X Spec_X A) ≅ Z ×_X Spec_X A`.

```lean
TauCeti.AlgebraicGeometry.relativeSpecPullbackIso_comp.{u} {X Y : AlgebraicGeometry.Scheme}
  (A : TauCeti.AlgebraicGeometry.QuasicoherentAlgebra X) (f : Y ⟶ X) {Z : AlgebraicGeometry.Scheme}
  (g : Z ⟶ Y) :
  (TauCeti.AlgebraicGeometry.relativeSpecPullbackIso A
        (CategoryTheory.CategoryStruct.comp g f)).hom =
    CategoryTheory.CategoryStruct.comp
      ((TauCeti.AlgebraicGeometry.relativeSpec Z).map
        ((TauCeti.AlgebraicGeometry.QuasicoherentAlgebra.pullbackComp g f).hom.app A).op)
      (CategoryTheory.CategoryStruct.comp
        (TauCeti.AlgebraicGeometry.relativeSpecPullbackIso
            ((TauCeti.AlgebraicGeometry.QuasicoherentAlgebra.pullback f).obj A) g).hom
        (CategoryTheory.CategoryStruct.comp
          ((TauCeti.AlgebraicGeometry.baseChangeAffineSchemeOver g).map
            (TauCeti.AlgebraicGeometry.relativeSpecPullbackIso A f).hom)
          ((CategoryTheory.MorphismProperty.Over.pullbackComp g f
                  (CategoryTheory.CategoryStruct.comp g f) ⋯).inv.app
            ((TauCeti.AlgebraicGeometry.relativeSpec X).obj (Opposite.op A)))))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.relativeSpecPullbackIso_comp`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/RelativeSpec/BaseChange.html#TauCeti.AlgebraicGeometry.relativeSpecPullbackIso_comp).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.relativeSpecPullbackIso_comp`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/RelativeSpec/BaseChange.html#TauCeti.AlgebraicGeometry.relativeSpecPullbackIso_comp)
- [Source of `TauCeti.AlgebraicGeometry.relativeSpecPullbackIso_comp` in TauCeti/AlgebraicGeometry/RelativeSpec/BaseChange.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/RelativeSpec/BaseChange.lean#L435)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
