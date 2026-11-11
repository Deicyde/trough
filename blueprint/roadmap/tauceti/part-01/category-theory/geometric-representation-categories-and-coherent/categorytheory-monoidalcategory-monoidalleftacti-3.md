---
declaration: def
origin: cited
lean: CategoryTheory.MonoidalCategory.MonoidalLeftAction.modificationEquiv
statement: formalized
---

# CategoryTheory.MonoidalCategory.MonoidalLeftAction.modificationEquiv

Equivariant natural transformations `F₁ ⟶ F₂` correspond to modifications
`strongTrans M F₁ ⟶ strongTrans M F₂`.

```lean
CategoryTheory.MonoidalCategory.MonoidalLeftAction.modificationEquiv.{w, v, u} (M : Type u)
  [Monoid M] {C D : Type w} [CategoryTheory.Category.{v, w} C] [CategoryTheory.Category.{v, w} D]
  [CategoryTheory.MonoidalCategory.MonoidalLeftAction (CategoryTheory.Discrete M) C]
  [CategoryTheory.MonoidalCategory.MonoidalLeftAction (CategoryTheory.Discrete M) D]
  (F₁ F₂ : CategoryTheory.Functor C D) [F₁.LeftLinear (CategoryTheory.Discrete M)]
  [F₂.LeftLinear (CategoryTheory.Discrete M)] :
  { τ // CategoryTheory.NatTrans.IsLeftLinear τ (CategoryTheory.Discrete M) } ≃
    (CategoryTheory.MonoidalCategory.MonoidalLeftAction.strongTrans M F₁).Modification
      (CategoryTheory.MonoidalCategory.MonoidalLeftAction.strongTrans M F₂)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.MonoidalCategory.MonoidalLeftAction.modificationEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Action/Modification.html#CategoryTheory.MonoidalCategory.MonoidalLeftAction.modificationEquiv).

## Sources

- [Tau Ceti documentation: `CategoryTheory.MonoidalCategory.MonoidalLeftAction.modificationEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Action/Modification.html#CategoryTheory.MonoidalCategory.MonoidalLeftAction.modificationEquiv)
- [Source of `CategoryTheory.MonoidalCategory.MonoidalLeftAction.modificationEquiv` in TauCeti/CategoryTheory/Monoidal/Action/Modification.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Action/Modification.lean#L169)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
