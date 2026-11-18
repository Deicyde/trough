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
- [Rational number](../../../overview/general-algebra/numbers/rational-number.md)
- [Ring-valued matrix](../../../overview/linear-algebra/matrices/ring-valued-matrix.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)

## Sources

- [Mathlib documentation: `Matrix.Pivot.exists_list_transvec_mul_mul_list_transvec_eq_diagonal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Transvection.html#Matrix.Pivot.exists_list_transvec_mul_mul_list_transvec_eq_diagonal)
- [Source of `Matrix.Pivot.exists_list_transvec_mul_mul_list_transvec_eq_diagonal` in Mathlib/LinearAlgebra/Matrix/Transvection.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/LinearAlgebra/Matrix/Transvection.lean#L667)
- [Mathlib undergraduate list: Linear algebra › Matrices](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L51)
