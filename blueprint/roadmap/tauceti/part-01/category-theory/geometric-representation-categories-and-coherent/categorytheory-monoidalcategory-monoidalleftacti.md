---
declaration: def
origin: cited
lean: CategoryTheory.MonoidalCategory.MonoidalLeftAction.pseudofunctorEquiv
statement: formalized
---

# CategoryTheory.MonoidalCategory.MonoidalLeftAction.pseudofunctorEquiv

Left actions of `Discrete M` on categories correspond bijectively to pseudofunctors
`LocallyDiscrete (SingleObj M) ⥤ᵖ Cat`: an action on `C` is sent to `pseudofunctor M C`, and a
pseudofunctor `F` to the action `F.monoidalLeftAction` on its value at the unique object.

```lean
CategoryTheory.MonoidalCategory.MonoidalLeftAction.pseudofunctorEquiv.{w, v, u} (M : Type u)
  [Monoid M] :
  (C : CategoryTheory.Cat) ×
      CategoryTheory.MonoidalCategory.MonoidalLeftAction (CategoryTheory.Discrete M) ↑C ≃
    CategoryTheory.Pseudofunctor (CategoryTheory.LocallyDiscrete (CategoryTheory.SingleObj M))
      CategoryTheory.Cat
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.MonoidalCategory.MonoidalLeftAction.pseudofunctorEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Action/Pseudofunctor.html#CategoryTheory.MonoidalCategory.MonoidalLeftAction.pseudofunctorEquiv).

## Sources

- [Tau Ceti documentation: `CategoryTheory.MonoidalCategory.MonoidalLeftAction.pseudofunctorEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Action/Pseudofunctor.html#CategoryTheory.MonoidalCategory.MonoidalLeftAction.pseudofunctorEquiv)
- [Source of `CategoryTheory.MonoidalCategory.MonoidalLeftAction.pseudofunctorEquiv` in TauCeti/CategoryTheory/Monoidal/Action/Pseudofunctor.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Action/Pseudofunctor.lean#L267)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
