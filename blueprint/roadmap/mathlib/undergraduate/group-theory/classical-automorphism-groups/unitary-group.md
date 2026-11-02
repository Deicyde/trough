---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: Matrix.unitaryGroup
mathlib_file: Mathlib/LinearAlgebra/UnitaryGroup.lean
---

# Unitary group

`Matrix.unitaryGroup n` is the group of `n` by `n` matrices where the star-transpose is the
inverse.

```lean
Matrix.unitaryGroup.{u, v} (n : Type u) [DecidableEq n] [Fintype n] (α : Type v) [CommRing α]
  [StarRing α] : Submonoid (Matrix n n α)
```

## Depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Ring](../../../overview/general-algebra/rings/ring.md)
- [Ring-valued matrix](../../../overview/linear-algebra/matrices/ring-valued-matrix.md)
- [Set](../../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Matrix.unitaryGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.unitaryGroup)
- [Source of `Matrix.unitaryGroup` in Mathlib/LinearAlgebra/UnitaryGroup.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/UnitaryGroup.lean#L102)
- [Mathlib undergraduate list: Group Theory › Classical automorphism groups](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L109)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Endomorphisms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L224)
