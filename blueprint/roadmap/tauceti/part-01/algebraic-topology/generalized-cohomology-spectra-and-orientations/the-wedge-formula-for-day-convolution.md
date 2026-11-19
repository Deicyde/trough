---
declaration: def
origin: cited
lean: CategoryTheory.MonoidalCategory.DayFunctor.isColimitShuffleCofan
statement: formalized
---

# The wedge formula for Day convolution

For functors `F` and `G` out of the
finite-bijection groupoid, the level `(F ⊗ G)(n)` of their Day convolution is the coproduct over
the subsets `S` of `Fin n` of `F(#S) ⊗ G(#Sᶜ)`, with the summand of `S` included through the Day
convolution unit followed by the action of the shuffle of `S`.

```lean
CategoryTheory.MonoidalCategory.DayFunctor.isColimitShuffleCofan.{v, u} {V : Type u}
  [CategoryTheory.Category.{v, u} V] [CategoryTheory.MonoidalCategory V]
  [∀ (F G : CategoryTheory.Functor TauCeti.FiniteBijection V),
      (CategoryTheory.MonoidalCategory.tensor TauCeti.FiniteBijection).HasPointwiseLeftKanExtension
        (CategoryTheory.MonoidalCategory.externalProduct F G)]
  [(CategoryTheory.Functor.fromPUnit
          (CategoryTheory.MonoidalCategoryStruct.tensorUnit
            TauCeti.FiniteBijection)).HasPointwiseLeftKanExtension
      (CategoryTheory.Functor.fromPUnit (CategoryTheory.MonoidalCategoryStruct.tensorUnit V))]
  [∀ (v : V) (d : TauCeti.FiniteBijection),
      CategoryTheory.Limits.PreservesColimitsOfShape
        (CategoryTheory.CostructuredArrow
          (CategoryTheory.MonoidalCategory.tensor TauCeti.FiniteBijection) d)
        (CategoryTheory.MonoidalCategory.tensorLeft v)]
  [∀ (v : V) (d : TauCeti.FiniteBijection),
      CategoryTheory.Limits.PreservesColimitsOfShape
        (CategoryTheory.CostructuredArrow
          (CategoryTheory.MonoidalCategory.tensor TauCeti.FiniteBijection) d)
        (CategoryTheory.MonoidalCategory.tensorRight v)]
  [∀ (v : V) (d : TauCeti.FiniteBijection),
      CategoryTheory.Limits.PreservesColimitsOfShape
        (CategoryTheory.CostructuredArrow
          (CategoryTheory.Functor.fromPUnit
            (CategoryTheory.MonoidalCategoryStruct.tensorUnit TauCeti.FiniteBijection))
          d)
        (CategoryTheory.MonoidalCategory.tensorLeft v)]
  [∀ (v : V) (d : TauCeti.FiniteBijection),
      CategoryTheory.Limits.PreservesColimitsOfShape
        (CategoryTheory.CostructuredArrow
          (CategoryTheory.Functor.fromPUnit
            (CategoryTheory.MonoidalCategoryStruct.tensorUnit TauCeti.FiniteBijection))
          d)
        (CategoryTheory.MonoidalCategory.tensorRight v)]
  [∀ (v : V) (d : TauCeti.FiniteBijection × TauCeti.FiniteBijection),
      CategoryTheory.Limits.PreservesColimitsOfShape
        (CategoryTheory.CostructuredArrow
          ((CategoryTheory.Functor.id TauCeti.FiniteBijection).prod
            (CategoryTheory.Functor.fromPUnit
              (CategoryTheory.MonoidalCategoryStruct.tensorUnit TauCeti.FiniteBijection)))
          d)
        (CategoryTheory.MonoidalCategory.tensorRight v)]
  [∀ (v : V) (d : TauCeti.FiniteBijection × TauCeti.FiniteBijection),
      CategoryTheory.Limits.PreservesColimitsOfShape
        (CategoryTheory.CostructuredArrow
          ((CategoryTheory.MonoidalCategory.tensor TauCeti.FiniteBijection).prod
            (CategoryTheory.Functor.id TauCeti.FiniteBijection))
          d)
        (CategoryTheory.MonoidalCategory.tensorRight v)]
  (F G : CategoryTheory.MonoidalCategory.DayFunctor TauCeti.FiniteBijection V)
  (n : TauCeti.FiniteBijection) : CategoryTheory.Limits.IsColimit (F.shuffleCofan G n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.MonoidalCategory.DayFunctor.isColimitShuffleCofan`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/FiniteBijection/Shuffle.html#CategoryTheory.MonoidalCategory.DayFunctor.isColimitShuffleCofan).

## Sources

- [Tau Ceti documentation: `CategoryTheory.MonoidalCategory.DayFunctor.isColimitShuffleCofan`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/FiniteBijection/Shuffle.html#CategoryTheory.MonoidalCategory.DayFunctor.isColimitShuffleCofan)
- [Source of `CategoryTheory.MonoidalCategory.DayFunctor.isColimitShuffleCofan` in TauCeti/CategoryTheory/FiniteBijection/Shuffle.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/FiniteBijection/Shuffle.lean#L354)
- [Tau Ceti roadmap status: Generalized cohomology, spectra and orientations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeneralizedCohomology/STATUS.md)
