---
declaration: def
origin: cited
lean: CategoryTheory.MonoidalCategory.MonoidalLeftAction.strongTransEquiv
statement: formalized
---

# CategoryTheory.MonoidalCategory.MonoidalLeftAction.strongTransEquiv

Equivariant functors are the strong transformations between the pseudofunctors attached to
the actions: functors `C ⥤ D` equipped with a left-linear structure for the actions of
`Discrete M` correspond to strong transformations `pseudofunctor M C ⟶ pseudofunctor M D`. The
correspondence keeps the lineators: the naturality isomorphisms of `strongTrans M F` have
components the lineators of `F`.

```lean
CategoryTheory.MonoidalCategory.MonoidalLeftAction.strongTransEquiv.{w, v, u} (M : Type u)
  [Monoid M] (C D : Type w) [CategoryTheory.Category.{v, w} C] [CategoryTheory.Category.{v, w} D]
  [CategoryTheory.MonoidalCategory.MonoidalLeftAction (CategoryTheory.Discrete M) C]
  [CategoryTheory.MonoidalCategory.MonoidalLeftAction (CategoryTheory.Discrete M) D] :
  (F : CategoryTheory.Functor C D) × F.LeftLinear (CategoryTheory.Discrete M) ≃
    (CategoryTheory.MonoidalCategory.MonoidalLeftAction.pseudofunctor M C).StrongTrans
      (CategoryTheory.MonoidalCategory.MonoidalLeftAction.pseudofunctor M D)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.MonoidalCategory.MonoidalLeftAction.strongTransEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Action/StrongTrans.html#CategoryTheory.MonoidalCategory.MonoidalLeftAction.strongTransEquiv).

## Sources

- [Tau Ceti documentation: `CategoryTheory.MonoidalCategory.MonoidalLeftAction.strongTransEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Action/StrongTrans.html#CategoryTheory.MonoidalCategory.MonoidalLeftAction.strongTransEquiv)
- [Source of `CategoryTheory.MonoidalCategory.MonoidalLeftAction.strongTransEquiv` in TauCeti/CategoryTheory/Monoidal/Action/StrongTrans.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/Monoidal/Action/StrongTrans.lean#L283)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
