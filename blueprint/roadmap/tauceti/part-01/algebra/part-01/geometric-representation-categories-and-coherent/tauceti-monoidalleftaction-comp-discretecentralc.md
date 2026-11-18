---
declaration: theorem
origin: cited
lean: TauCeti.monoidalLeftAction_comp_discreteCentralCharacterFamily
statement: formalized
proof: formalized
---

# TauCeti.monoidalLeftAction_comp_discreteCentralCharacterFamily

At a point `x` fixed by the image of `φ : K →* G`, the restriction of the fiber family along
`CategoryTheory.ActionCategory.singleObjFunctor` is the coherent twisting action of `K` through
`a ∘ φ` on the fiber of `x`, `MonoidHom.discreteCentralCharacterMonoidalLeftAction`. The two
actions agree in all their data: action functors, associators and unitors.

```lean
TauCeti.monoidalLeftAction_comp_discreteCentralCharacterFamily.{v, u, u_1, u_2, u_3, u_4}
  {G : Type u_1} [Monoid G] {X : Type u_2} [MulAction G X] {R : Type u_3} [CommRing R] {A : Type u}
  [Ring A] [Algebra R A] {a : G →* A ≃ₐ[R] A} [TopologicalSpace A]
  {ha : ∀ (g : G), Continuous ⇑(a g).symm} {χ : X → ↥(Subalgebra.center R A) →ₐ[R] R}
  {hχ : ∀ (g : G) (x : X), χ (g • x) = (χ x).comp ↑(Subalgebra.centerCongr (a g).symm)}
  {K : Type u_4} [Monoid K] (φ : K →* G) (x : X) (hx : ∀ (k : K), φ k • x = x) :
  ((CategoryTheory.ActionCategory.singleObjFunctor φ x hx).toPseudofunctor.comp
        (TauCeti.discreteCentralCharacterFamily X a ha χ hχ)).monoidalLeftAction =
    (a.comp φ).discreteCentralCharacterMonoidalLeftAction (χ x) ⋯ ⋯
```

## Depends on

- [TauCeti.discreteCentralCharacterFamily](tauceti-discretecentralcharacterfamily.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.monoidalLeftAction_comp_discreteCentralCharacterFamily`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/CentralCharacter/ActionCategory.html#TauCeti.monoidalLeftAction_comp_discreteCentralCharacterFamily).

## Sources

- [Tau Ceti documentation: `TauCeti.monoidalLeftAction_comp_discreteCentralCharacterFamily`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/CentralCharacter/ActionCategory.html#TauCeti.monoidalLeftAction_comp_discreteCentralCharacterFamily)
- [Source of `TauCeti.monoidalLeftAction_comp_discreteCentralCharacterFamily` in TauCeti/Algebra/Category/ModuleCat/CentralCharacter/ActionCategory.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Category/ModuleCat/CentralCharacter/ActionCategory.lean#L342)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
