---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: CategoryTheory.Functor
mathlib_file: Mathlib/CategoryTheory/Functor/Basic.lean
---

# Functor

`Functor C D` represents a functor between categories `C` and `D`.

To apply a functor `F` to an object use `F.obj X`, and to a morphism use `F.map f`.

The axiom `map_id` expresses preservation of identities, and
`map_comp` expresses functoriality.

```lean
CategoryTheory.Functor.{v₁, v₂, u₁, u₂} (C : Type u₁) [CategoryTheory.Category.{v₁, u₁} C]
  (D : Type u₂) [CategoryTheory.Category.{v₂, u₂} D] : Type (max v₁ v₂ u₁ u₂)
```

## Depends on

- [Category](category.md)

## Sources

- [Mathlib documentation: `CategoryTheory.Functor`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Functor/Basic.html#CategoryTheory.Functor)
- [Source of `CategoryTheory.Functor` in Mathlib/CategoryTheory/Functor/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/Functor/Basic.lean#L33)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L5)
