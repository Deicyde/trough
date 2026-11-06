# Sylvester's determinant theorem

The **Weinstein–Aronszajn identity**. Note the `1` on the LHS is of shape m×m, while the `1` on
the RHS is of shape n×n.

```lean
Matrix.det_one_add_mul_comm.{u_2, u_3, u_4} {m : Type u_2} {n : Type u_3} {α : Type u_4} [Fintype m]
  [Fintype n] [DecidableEq m] [DecidableEq n] [CommRing α] (A : Matrix m n α) (B : Matrix n m α) :
  (1 + A * B).det = (1 + B * A).det
```

## Depends on

- [Determinant](../../../overview/linear-algebra/matrices/determinant.md)

## Proof depends on

- [Invertible elements](../../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)

## Sources

- [Mathlib documentation: `Matrix.det_one_add_mul_comm`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/SchurComplement.html#Matrix.det_one_add_mul_comm)
- [Source of `Matrix.det_one_add_mul_comm` in Mathlib/LinearAlgebra/Matrix/SchurComplement.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Matrix/SchurComplement.lean#L398)
- [1000+ theorems list: Q7660749](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3879)
- [1000+ theorems project: Q7660749](https://1000-plus.github.io/all.html?length=-1#Q7660749)
- [Wikipedia: Sylvester's determinant theorem](https://en.wikipedia.org/wiki/Sylvester's_determinant_theorem)
- [Wikidata: Q7660749](https://www.wikidata.org/wiki/Q7660749)
