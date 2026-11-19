---
declaration: instance
origin: cited
lean: TauCeti.EquivariantGroupoidLift.instBicategory
statement: formalized
---

# TauCeti.EquivariantGroupoidLift.instBicategory

The bicategory of coherent equivariant lifts of a family of categorical actions. Its
`1`-morphisms are the morphisms of lifts `EquivariantGroupoidLift.Hom` and its `2`-morphisms are
the compatible modifications `EquivariantGroupoidLift.Hom.Hom₂`. Since a `2`-morphism is
determined by its joint modification, the coherence axioms are those of the bicategory of
pseudofunctors.

```lean
TauCeti.EquivariantGroupoidLift.instBicategory.{w, v, u₂, v₁, u₁} {Γ : Type u₁}
  [CategoryTheory.Category.{v₁, u₁} Γ] {H : Type u₂} [Monoid H]
  {actions :
    Γ →
      CategoryTheory.Pseudofunctor (CategoryTheory.LocallyDiscrete (CategoryTheory.SingleObj H))
        CategoryTheory.Cat} :
  CategoryTheory.Bicategory (TauCeti.EquivariantGroupoidLift Γ actions)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.EquivariantGroupoidLift.instBicategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Bicategory/Functor/EquivariantGroupoidLift/Bicategory.html#TauCeti.EquivariantGroupoidLift.instBicategory).

## Sources

- [Tau Ceti documentation: `TauCeti.EquivariantGroupoidLift.instBicategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Bicategory/Functor/EquivariantGroupoidLift/Bicategory.html#TauCeti.EquivariantGroupoidLift.instBicategory)
- [Source of `TauCeti.EquivariantGroupoidLift.instBicategory` in TauCeti/CategoryTheory/Bicategory/Functor/EquivariantGroupoidLift/Bicategory.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Bicategory/Functor/EquivariantGroupoidLift/Bicategory.lean#L140)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
