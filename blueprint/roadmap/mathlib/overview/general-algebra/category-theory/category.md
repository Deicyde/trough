---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: CategoryTheory.Category
mathlib_file: Mathlib/CategoryTheory/Category/Basic.lean
---

# Category

The typeclass `Category C` describes morphisms associated to objects of type `C`.
The universe levels of the objects and morphisms are unconstrained, and will often need to be
specified explicitly, as `Category.{v} C`. (See also `LargeCategory` and `SmallCategory`.)

```lean
CategoryTheory.Category.{v, u} (obj : Type u) : Type (max u (v + 1))
```

## Depends on

Its statement uses no other concept on these lists.

## Sources

- [Mathlib documentation: `CategoryTheory.Category`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Basic.html#CategoryTheory.Category)
- [Source of `CategoryTheory.Category` in Mathlib/CategoryTheory/Category/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/Category/Basic.lean#L226)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L3)
