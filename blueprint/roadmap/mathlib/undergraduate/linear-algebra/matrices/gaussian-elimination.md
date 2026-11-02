---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Matrix.Pivot.exists_list_transvec_mul_mul_list_transvec_eq_diagonal
mathlib_file: Mathlib/LinearAlgebra/Matrix/Transvection.lean
---

# Gaussian elimination

Any matrix can be reduced to diagonal form by elementary operations.

```lean
Matrix.Pivot.exists_list_transvec_mul_mul_list_transvec_eq_diagonal.{u_1, u_3} {n : Type u_1}
  {𝕜 : Type u_3} [Field 𝕜] [DecidableEq n] [Fintype n] (M : Matrix n n 𝕜) :
  ∃ L L' D,
    (List.map Matrix.TransvectionStruct.toMatrix L).prod * M *
        (List.map Matrix.TransvectionStruct.toMatrix L').prod =
      Matrix.diagonal D
```

## Depends on

- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Ring-valued matrix](../../../overview/linear-algebra/matrices/ring-valued-matrix.md)
- [Set](../../../overview/data-structures/sets/set.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Module](../../../overview/linear-algebra/fundamentals/module.md)

## Sources

- [Mathlib documentation: `Matrix.Pivot.exists_list_transvec_mul_mul_list_transvec_eq_diagonal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Transvection.html#Matrix.Pivot.exists_list_transvec_mul_mul_list_transvec_eq_diagonal)
- [Source of `Matrix.Pivot.exists_list_transvec_mul_mul_list_transvec_eq_diagonal` in Mathlib/LinearAlgebra/Matrix/Transvection.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Matrix/Transvection.lean#L664)
- [Mathlib undergraduate list: Linear algebra › Matrices](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L51)
