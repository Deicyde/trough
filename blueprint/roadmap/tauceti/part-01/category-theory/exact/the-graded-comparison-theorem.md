---
declaration: def
origin: cited
lean: TauCeti.ExactStructure.FiniteResolution.liftShiftHomotopy
statement: formalized
---

# The graded comparison theorem

The comparison map between two finite projective
resolutions commutes with the grading shift up to homotopy: the lift of `f{1}` between the
shifted resolutions is homotopic to the shift of the lift of `f`.

```lean
TauCeti.ExactStructure.FiniteResolution.liftShiftHomotopy.{v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasZeroObject C] [CategoryTheory.Limits.HasBinaryBiproducts C]
  {E : TauCeti.GradedExactStructure C} {X Y : C} (f : X ⟶ Y)
  (r : E.FiniteResolution E.isProjective X) (r' : E.FiniteResolution E.isProjective Y) :
  Homotopy
    (TauCeti.ExactStructure.FiniteResolution.lift ⋯ (E.shift.functor.map f) r.shiftProjective
      r'.shiftProjective)
    (CategoryTheory.CategoryStruct.comp r.toChainComplexShiftProjectiveIso.hom
      (CategoryTheory.CategoryStruct.comp
        ((E.shift.functor.mapHomologicalComplex (ComplexShape.down ℕ)).map
          (TauCeti.ExactStructure.FiniteResolution.lift ⋯ f r r'))
        r'.toChainComplexShiftProjectiveIso.inv))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ExactStructure.FiniteResolution.liftShiftHomotopy`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/Graded/Projective.html#TauCeti.ExactStructure.FiniteResolution.liftShiftHomotopy).

## Sources

- [Tau Ceti documentation: `TauCeti.ExactStructure.FiniteResolution.liftShiftHomotopy`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/Graded/Projective.html#TauCeti.ExactStructure.FiniteResolution.liftShiftHomotopy)
- [Source of `TauCeti.ExactStructure.FiniteResolution.liftShiftHomotopy` in TauCeti/CategoryTheory/Exact/Graded/Projective.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Exact/Graded/Projective.lean#L279)
