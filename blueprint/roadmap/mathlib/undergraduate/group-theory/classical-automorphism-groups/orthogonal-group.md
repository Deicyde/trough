---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: Matrix.orthogonalGroup
mathlib_file: Mathlib/LinearAlgebra/UnitaryGroup.lean
---

# Orthogonal group

`Matrix.orthogonalGroup n` is the group of `n` by `n` matrices where the transpose is the
inverse.

```lean
Matrix.orthogonalGroup.{u, v} (n : Type u) [DecidableEq n] [Fintype n] (R : Type v) [CommRing R] :
  Submonoid (Matrix n n R)
```

## Depends on

- [Unitary group](unitary-group.md)

## Sources

- [Mathlib documentation: `Matrix.orthogonalGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.orthogonalGroup)
- [Source of `Matrix.orthogonalGroup` in Mathlib/LinearAlgebra/UnitaryGroup.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/UnitaryGroup.lean#L316)
- [Mathlib undergraduate list: Group Theory › Classical automorphism groups](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L107)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Endomorphisms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L223)
