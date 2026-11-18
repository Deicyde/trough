---
declaration: def
origin: cited
lean: CategoryTheory.Functor.towerDifference
statement: formalized
---

# CategoryTheory.Functor.towerDifference

The *product–difference map* `1 - s` of a tower `F₀ ← F₁ ← ⋯`: the endomorphism of `∏ₙ Fₙ` whose
`n`-th component is the projection to `Fₙ` minus the projection to `Fₙ₊₁` followed by the
transition `Fₙ₊₁ ⟶ Fₙ` (`towerDifference_π`). Its kernel is the limit of the tower
(`isLimitConeOfTowerDifference`).

```lean
CategoryTheory.Functor.towerDifference.{v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Preadditive C] (F : CategoryTheory.Functor ℕᵒᵖ C)
  [CategoryTheory.Limits.HasProduct fun n => F.obj (Opposite.op n)] :
  (∏ᶜ fun n => F.obj (Opposite.op n)) ⟶ ∏ᶜ fun n => F.obj (Opposite.op n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Functor.towerDifference`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Preadditive/TowerDifference.html#CategoryTheory.Functor.towerDifference).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Functor.towerDifference`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Preadditive/TowerDifference.html#CategoryTheory.Functor.towerDifference)
- [Source of `CategoryTheory.Functor.towerDifference` in TauCeti/CategoryTheory/Preadditive/TowerDifference.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Preadditive/TowerDifference.lean#L73)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
