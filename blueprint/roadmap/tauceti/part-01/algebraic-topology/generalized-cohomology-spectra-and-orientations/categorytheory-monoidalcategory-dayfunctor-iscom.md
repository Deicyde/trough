---
declaration: theorem
origin: cited
lean: CategoryTheory.MonoidalCategory.DayFunctor.isCommMonObj
statement: formalized
proof: formalized
---

# CategoryTheory.MonoidalCategory.DayFunctor.isCommMonObj

The Day convolution monoid of a lax braided functor out of a symmetric monoidal category is
commutative.

```lean
CategoryTheory.MonoidalCategory.DayFunctor.isCommMonObj.{v₁, v₂, u₁, u₂} {C : Type u₁}
  [CategoryTheory.Category.{v₁, u₁} C] {V : Type u₂} [CategoryTheory.Category.{v₂, u₂} V]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.MonoidalCategory V]
  [∀ (F G : CategoryTheory.Functor C V),
      (CategoryTheory.MonoidalCategory.tensor C).HasPointwiseLeftKanExtension
        (CategoryTheory.MonoidalCategory.externalProduct F G)]
  [(CategoryTheory.Functor.fromPUnit
          (CategoryTheory.MonoidalCategoryStruct.tensorUnit C)).HasPointwiseLeftKanExtension
      (CategoryTheory.Functor.fromPUnit (CategoryTheory.MonoidalCategoryStruct.tensorUnit V))]
  [∀ (v : V) (d : C),
      CategoryTheory.Limits.PreservesColimitsOfShape
        (CategoryTheory.CostructuredArrow (CategoryTheory.MonoidalCategory.tensor C) d)
        (CategoryTheory.MonoidalCategory.tensorLeft v)]
  [∀ (v : V) (d : C),
      CategoryTheory.Limits.PreservesColimitsOfShape
        (CategoryTheory.CostructuredArrow (CategoryTheory.MonoidalCategory.tensor C) d)
        (CategoryTheory.MonoidalCategory.tensorRight v)]
  [∀ (v : V) (d : C),
      CategoryTheory.Limits.PreservesColimitsOfShape
        (CategoryTheory.CostructuredArrow
          (CategoryTheory.Functor.fromPUnit (CategoryTheory.MonoidalCategoryStruct.tensorUnit C)) d)
        (CategoryTheory.MonoidalCategory.tensorLeft v)]
  [∀ (v : V) (d : C),
      CategoryTheory.Limits.PreservesColimitsOfShape
        (CategoryTheory.CostructuredArrow
          (CategoryTheory.Functor.fromPUnit (CategoryTheory.MonoidalCategoryStruct.tensorUnit C)) d)
        (CategoryTheory.MonoidalCategory.tensorRight v)]
  [∀ (v : V) (d : C × C),
      CategoryTheory.Limits.PreservesColimitsOfShape
        (CategoryTheory.CostructuredArrow
          ((CategoryTheory.Functor.id C).prod
            (CategoryTheory.Functor.fromPUnit (CategoryTheory.MonoidalCategoryStruct.tensorUnit C)))
          d)
        (CategoryTheory.MonoidalCategory.tensorRight v)]
  [∀ (v : V) (d : C × C),
      CategoryTheory.Limits.PreservesColimitsOfShape
        (CategoryTheory.CostructuredArrow
          ((CategoryTheory.MonoidalCategory.tensor C).prod (CategoryTheory.Functor.id C)) d)
        (CategoryTheory.MonoidalCategory.tensorRight v)]
  [CategoryTheory.SymmetricCategory C] [CategoryTheory.BraidedCategory V]
  (F : CategoryTheory.MonoidalCategory.DayFunctor C V) [F.functor.LaxBraided] :
  CategoryTheory.IsCommMonObj F
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.MonoidalCategory.DayFunctor.isCommMonObj`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/DayConvolution/Monoid.html#CategoryTheory.MonoidalCategory.DayFunctor.isCommMonObj).

## Sources

- [Tau Ceti documentation: `CategoryTheory.MonoidalCategory.DayFunctor.isCommMonObj`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/DayConvolution/Monoid.html#CategoryTheory.MonoidalCategory.DayFunctor.isCommMonObj)
- [Source of `CategoryTheory.MonoidalCategory.DayFunctor.isCommMonObj` in TauCeti/CategoryTheory/Monoidal/DayConvolution/Monoid.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/DayConvolution/Monoid.lean#L132)
- [Tau Ceti roadmap status: Generalized cohomology, spectra and orientations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeneralizedCohomology/STATUS.md)
