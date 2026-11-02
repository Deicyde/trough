---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: CategoryTheory.Comma
mathlib_file: Mathlib/CategoryTheory/Comma/Basic.lean
---

# Comma category

The objects of the comma category are triples of an object `left : A`, an object
`right : B` and a morphism `hom : L.obj left ⟶ R.obj right`.

```lean
CategoryTheory.Comma.{v₁, v₂, v₃, u₁, u₂, u₃} {A : Type u₁} [CategoryTheory.Category.{v₁, u₁} A]
  {B : Type u₂} [CategoryTheory.Category.{v₂, u₂} B] {T : Type u₃}
  [CategoryTheory.Category.{v₃, u₃} T] (L : CategoryTheory.Functor A T)
  (R : CategoryTheory.Functor B T) : Type (max u₁ u₂ v₃)
```

## Depends on

- [Functor](functor.md)

## Sources

- [Mathlib documentation: `CategoryTheory.Comma`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Comma/Basic.html#CategoryTheory.Comma)
- [Source of `CategoryTheory.Comma` in Mathlib/CategoryTheory/Comma/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/Comma/Basic.lean#L64)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L11)
