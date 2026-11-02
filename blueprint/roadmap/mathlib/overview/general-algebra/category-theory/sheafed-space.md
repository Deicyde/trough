---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: AlgebraicGeometry.SheafedSpace
mathlib_file: Mathlib/Geometry/RingedSpace/SheafedSpace.lean
---

# Sheafed space

A `SheafedSpace C` is a topological space equipped with a sheaf of `C`s.

```lean
AlgebraicGeometry.SheafedSpace.{u, v, u_1} (C : Type u) [CategoryTheory.Category.{v, u} C] :
  Type (max (max u (u_1 + 1)) v)
```

## Depends on

- [Grothendieck topology](grothendieck-topology.md)
- [Presheafed space](presheafed-space.md)
- [Yoneda embedding](yoneda-embedding.md)

## Sources

- [Mathlib documentation: `AlgebraicGeometry.SheafedSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/RingedSpace/SheafedSpace.html#AlgebraicGeometry.SheafedSpace)
- [Source of `AlgebraicGeometry.SheafedSpace` in Mathlib/Geometry/RingedSpace/SheafedSpace.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/RingedSpace/SheafedSpace.lean#L42)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L14)
