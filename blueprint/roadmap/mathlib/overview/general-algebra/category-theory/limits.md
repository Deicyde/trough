---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: CategoryTheory.Limits.IsLimit
mathlib_file: Mathlib/CategoryTheory/Limits/IsLimit.lean
---

# Limits

A cone `t` on `F` is a limit cone if each cone on `F` admits a unique
cone morphism to `t`.

```lean
CategoryTheory.Limits.IsLimit.{v₁, v₃, u₁, u₃} {J : Type u₁} [CategoryTheory.Category.{v₁, u₁} J]
  {C : Type u₃} [CategoryTheory.Category.{v₃, u₃} C] {F : CategoryTheory.Functor J C}
  (t : CategoryTheory.Limits.Cone F) : Type (max (max u₁ u₃) v₃)
```

## Depends on

- [Natural transformation](natural-transformation.md)

## Sources

- [Mathlib documentation: `CategoryTheory.Limits.IsLimit`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Limits/IsLimit.html#CategoryTheory.Limits.IsLimit)
- [Source of `CategoryTheory.Limits.IsLimit` in Mathlib/CategoryTheory/Limits/IsLimit.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/Limits/IsLimit.lean#L46)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L12)
