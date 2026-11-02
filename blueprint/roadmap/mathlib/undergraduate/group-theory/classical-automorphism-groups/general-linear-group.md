---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: Matrix.GeneralLinearGroup
mathlib_file: Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Defs.lean
---

# General linear group

`GL n R` is the group of `n` by `n` `R`-matrices with unit determinant.
Defined as a subtype of matrices

```lean
Matrix.GeneralLinearGroup.{u, v} (n : Type u) (R : Type v) [DecidableEq n] [Fintype n]
  [Semiring R] : Type (max v u)
```

## Depends on

- [Array](../../../overview/data-structures/list-like-structures/array.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)
- [Ring-valued matrix](../../../overview/linear-algebra/matrices/ring-valued-matrix.md)
- [Set](../../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Matrix.GeneralLinearGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Defs.html#Matrix.GeneralLinearGroup)
- [Source of `Matrix.GeneralLinearGroup` in Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Defs.lean#L41)
- [Mathlib undergraduate list: Group Theory › Classical automorphism groups](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L105)
