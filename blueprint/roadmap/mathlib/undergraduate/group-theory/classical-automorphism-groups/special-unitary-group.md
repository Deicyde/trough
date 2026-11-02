---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Matrix.specialUnitaryGroup
mathlib_file: Mathlib/LinearAlgebra/UnitaryGroup.lean
---

# Special unitary group

`Matrix.specialUnitaryGroup` is the group of unitary `n` by `n` matrices where the determinant
is 1. (This definition is only correct if 2 is invertible.)

```lean
Matrix.specialUnitaryGroup.{u, v} (n : Type u) [DecidableEq n] [Fintype n] (α : Type v) [CommRing α]
  [StarRing α] : Submonoid (Matrix n n α)
```

## Depends on

- [Determinant](../../../overview/linear-algebra/matrices/determinant.md)
- [Unitary group](unitary-group.md)

## Sources

- [Mathlib documentation: `Matrix.specialUnitaryGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.specialUnitaryGroup)
- [Source of `Matrix.specialUnitaryGroup` in Mathlib/LinearAlgebra/UnitaryGroup.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/UnitaryGroup.lean#L276)
- [Mathlib undergraduate list: Group Theory › Classical automorphism groups](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L110)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Endomorphisms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L226)
