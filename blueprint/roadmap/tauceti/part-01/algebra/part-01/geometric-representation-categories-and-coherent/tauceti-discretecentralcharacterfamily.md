---
declaration: def
origin: cited
lean: TauCeti.discreteCentralCharacterFamily
statement: formalized
---

# TauCeti.discreteCentralCharacterFamily

The strict discrete character fibers `x ↦ discreteCentralCharacterModules (χ x)` over the
action category `G ⋉ X`, with the twists along `(a g)⁻¹` as transport functors. It is the
restriction of `actionCategoryTwist` to these fibers, so its unit and composition comparisons
are restrictions of those of `ModuleCat.restrictScalars`.

```lean
TauCeti.discreteCentralCharacterFamily.{v, u, u_1, u_2, u_3} {G : Type u_1} [Monoid G]
  (X : Type u_2) [MulAction G X] {R : Type u_3} [CommRing R] {A : Type u} [Ring A] [Algebra R A]
  (a : G →* A ≃ₐ[R] A) [TopologicalSpace A] (ha : ∀ (g : G), Continuous ⇑(a g).symm)
  (χ : X → ↥(Subalgebra.center R A) →ₐ[R] R)
  (hχ : ∀ (g : G) (x : X), χ (g • x) = (χ x).comp ↑(Subalgebra.centerCongr (a g).symm)) :
  CategoryTheory.Pseudofunctor (CategoryTheory.LocallyDiscrete (CategoryTheory.ActionCategory G X))
    CategoryTheory.Cat
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.discreteCentralCharacterFamily`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/CentralCharacter/ActionCategory.html#TauCeti.discreteCentralCharacterFamily).

## Sources

- [Tau Ceti documentation: `TauCeti.discreteCentralCharacterFamily`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/CentralCharacter/ActionCategory.html#TauCeti.discreteCentralCharacterFamily)
- [Source of `TauCeti.discreteCentralCharacterFamily` in TauCeti/Algebra/Category/ModuleCat/CentralCharacter/ActionCategory.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Category/ModuleCat/CentralCharacter/ActionCategory.lean#L131)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
