# Ring-valued matrix

`Matrix m n R` is the type of matrices with entries in `R`, whose rows are indexed by `m`
and whose columns are indexed by `n`.

```lean
Matrix.{u, u', v} (m : Type u) (n : Type u') (α : Type v) : Type (max u u' v)
```

## Depends on

Its statement uses no other concept on these lists.

## Sources

- [Mathlib documentation: `Matrix`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Defs.html#Matrix)
- [Source of `Matrix` in Mathlib/LinearAlgebra/Matrix/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Matrix/Defs.lean#L52)
- [Mathlib overview: Linear algebra › Matrices](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L190)
- [Mathlib undergraduate list: Linear algebra › Matrices](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L42)
- [Mathlib undergraduate list: Linear algebra › Matrices](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L43)
