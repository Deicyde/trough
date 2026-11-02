---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: CategoryTheory.Adjunction
mathlib_file: Mathlib/CategoryTheory/Adjunction/Basic.lean
---

# Adjunction

`F ⊣ G` represents the data of an adjunction between two functors
`F : C ⥤ D` and `G : D ⥤ C`. `F` is the left adjoint and `G` is the right adjoint.

We use the unit-counit definition of an adjunction. There is a constructor `Adjunction.mk'`
which constructs an adjunction from the data of a hom set equivalence, a unit, and a counit,
together with proofs of the equalities `homEquiv_unit` and `homEquiv_counit` relating them to each
other.

There is also a constructor `Adjunction.mkOfHomEquiv` which constructs an adjunction from a natural
hom set equivalence.

To construct adjoints to a given functor, there are constructors `leftAdjointOfEquiv` and
`adjunctionOfEquivLeft` (as well as their duals).

```lean
CategoryTheory.Adjunction.{v₁, v₂, u₁, u₂} {C : Type u₁} [CategoryTheory.Category.{v₁, u₁} C]
  {D : Type u₂} [CategoryTheory.Category.{v₂, u₂} D] (F : CategoryTheory.Functor C D)
  (G : CategoryTheory.Functor D C) : Type (max (max (max u₁ u₂) v₁) v₂)
```

## Depends on

- [Natural transformation](natural-transformation.md)

## Sources

- [Mathlib documentation: `CategoryTheory.Adjunction`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Adjunction/Basic.html#CategoryTheory.Adjunction)
- [Source of `CategoryTheory.Adjunction` in Mathlib/CategoryTheory/Adjunction/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/Adjunction/Basic.lean#L94)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L9)
