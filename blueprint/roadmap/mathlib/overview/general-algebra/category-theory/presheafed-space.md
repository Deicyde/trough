---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: AlgebraicGeometry.PresheafedSpace
mathlib_file: Mathlib/Geometry/RingedSpace/PresheafedSpace.lean
---

# Presheafed space

A `PresheafedSpace C` is a topological space equipped with a presheaf of `C`s.

```lean
AlgebraicGeometry.PresheafedSpace.{v_1, u_1, u} (C : Type u_1)
  [CategoryTheory.Category.{v_1, u_1} C] : Type (max (max (u + 1) u_1) v_1)
```

## Depends on

- [Functor](functor.md)
- [Small category](small-category.md)
- [The category of topological spaces](../../topology/general-topology/part-01/the-category-of-topological-spaces.md)

## Sources

- [Mathlib documentation: `AlgebraicGeometry.PresheafedSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/RingedSpace/PresheafedSpace.html#AlgebraicGeometry.PresheafedSpace)
- [Source of `AlgebraicGeometry.PresheafedSpace` in Mathlib/Geometry/RingedSpace/PresheafedSpace.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/RingedSpace/PresheafedSpace.lean#L41)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L13)
