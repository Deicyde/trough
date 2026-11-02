---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: Matrix.specialOrthogonalGroup
mathlib_file: Mathlib/LinearAlgebra/UnitaryGroup.lean
---

# Special orthogonal group

`Matrix.specialOrthogonalGroup n` is the group of orthogonal `n` by `n` where the determinant
is one. (This definition is only correct if 2 is invertible.)

```lean
Matrix.specialOrthogonalGroup.{u, v} (n : Type u) [DecidableEq n] [Fintype n] (R : Type v)
  [CommRing R] : Submonoid (Matrix n n R)
```

## Depends on

- [Special unitary group](special-unitary-group.md)

## Sources

- [Mathlib documentation: `Matrix.specialOrthogonalGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.specialOrthogonalGroup)
- [Source of `Matrix.specialOrthogonalGroup` in Mathlib/LinearAlgebra/UnitaryGroup.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/UnitaryGroup.lean#L336)
- [Mathlib undergraduate list: Group Theory › Classical automorphism groups](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L108)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Endomorphisms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L225)
