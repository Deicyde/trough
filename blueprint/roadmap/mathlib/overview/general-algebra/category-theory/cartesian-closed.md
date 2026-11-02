---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: CategoryTheory.MonoidalClosed
mathlib_file: Mathlib/CategoryTheory/Monoidal/Closed/Basic.lean
---

# Cartesian closed

A monoidal category `C` is (right) monoidal closed if every object is (right) closed.

```lean
CategoryTheory.MonoidalClosed.{v, u} (C : Type u) [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.MonoidalCategory C] : Type (max u v)
```

## Depends on

- [Adjunction](adjunction.md)
- [Monoidal category](monoidal-category.md)

## Sources

- [Mathlib documentation: `CategoryTheory.MonoidalClosed`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Monoidal/Closed/Basic.html#CategoryTheory.MonoidalClosed)
- [Source of `CategoryTheory.MonoidalClosed` in Mathlib/CategoryTheory/Monoidal/Closed/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/Monoidal/Closed/Basic.lean#L45)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L16)
