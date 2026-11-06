# Determinant

The determinant of a matrix given by the Leibniz formula.

This is available in bundled forms as:
* `Matrix.detMonoidHom`
* `Matrix.detRowAlternating`

```lean
Matrix.det.{v, u_2} {n : Type u_2} [DecidableEq n] [Fintype n] {R : Type v} [CommRing R]
  (M : Matrix n n R) : R
```

## Depends on

- [Alternating map](../fundamentals/alternating-map.md)
- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Integer](../../general-algebra/numbers/integer.md)
- [Linear map](../fundamentals/linear-map.md)
- [Ring-valued matrix](ring-valued-matrix.md)
- [Signature](../../../undergraduate/group-theory/permutation-group/signature.md)

## Sources

- [Mathlib documentation: `Matrix.det`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.html#Matrix.det)
- [Source of `Matrix.det` in Mathlib/LinearAlgebra/Matrix/Determinant/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.lean#L56)
- [Mathlib overview: Linear algebra › Matrices](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L192)
- [Mathlib undergraduate list: Linear algebra › Matrices](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L47)
