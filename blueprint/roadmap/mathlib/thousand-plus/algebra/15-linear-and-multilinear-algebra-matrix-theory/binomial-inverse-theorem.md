# Binomial inverse theorem

The **Binomial Inverse Theorem** (`⅟` version).

See `Matrix.invOf_add_mul_mul` for the Woodbury identity.

```lean
Matrix.invOf_add_mul_mul'.{u_1, u_2, u_3} {m : Type u_1} {n : Type u_2} {α : Type u_3} [Fintype n]
  [DecidableEq n] [Fintype m] [DecidableEq m] [Ring α] (A : Matrix n n α) (U : Matrix n m α)
  (C : Matrix m m α) (V : Matrix m n α) [Invertible A] [Invertible (C + C * V * ⅟A * U * C)]
  [Invertible (A + U * C * V)] :
  ⅟(A + U * C * V) = ⅟A - ⅟A * U * C * ⅟(C + C * V * ⅟A * U * C) * C * V * ⅟A
```

## Depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Integer](../../../overview/general-algebra/numbers/integer.md)
- [Invertible elements](../../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Ring](../../../overview/general-algebra/rings/ring.md)
- [Ring-valued matrix](../../../overview/linear-algebra/matrices/ring-valued-matrix.md)

## Sources

- [Mathlib documentation: `Matrix.invOf_add_mul_mul'`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Invertible.html#Matrix.invOf_add_mul_mul')
- [Source of `Matrix.invOf_add_mul_mul'` in Mathlib/LinearAlgebra/Matrix/Invertible.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Matrix/Invertible.lean#L241)
- [1000+ theorems list: Q1551745](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1755)
- [1000+ theorems project: Q1551745](https://1000-plus.github.io/all.html?length=-1#Q1551745)
- [Wikipedia: Binomial inverse theorem](https://en.wikipedia.org/wiki/Binomial_inverse_theorem)
- [Wikidata: Q1551745](https://www.wikidata.org/wiki/Q1551745)
