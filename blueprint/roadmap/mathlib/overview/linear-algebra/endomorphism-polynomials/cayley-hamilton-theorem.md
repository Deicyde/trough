---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Matrix.aeval_self_charpoly
mathlib_file: Mathlib/LinearAlgebra/Matrix/Charpoly/Basic.lean
---

# Cayley-Hamilton theorem

The **Cayley-Hamilton Theorem**, that the characteristic polynomial of a matrix,
applied to the matrix itself, is zero.

This holds over any commutative ring.

See `LinearMap.aeval_self_charpoly` for the equivalent statement about endomorphisms.

```lean
Matrix.aeval_self_charpoly.{u_1, u_4} {R : Type u_1} [CommRing R] {n : Type u_4} [DecidableEq n]
  [Fintype n] (M : Matrix n n R) : (Polynomial.aeval M) M.charpoly = 0
```

## Depends on

- [Characteristic polynomial](characteristic-polynomial.md)

## Proof depends on

- [Algebra of endomorphisms of a vector space](../../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Polynomial functions](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-etc/polynomial-functions.md)
- [Tensor product of algebras](../../general-algebra/algebras-over-a-ring/tensor-product-of-algebras.md)

## Sources

- [Mathlib documentation: `Matrix.aeval_self_charpoly`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Charpoly/Basic.html#Matrix.aeval_self_charpoly)
- [Source of `Matrix.aeval_self_charpoly` in Mathlib/LinearAlgebra/Matrix/Charpoly/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Matrix/Charpoly/Basic.lean#L215)
- [Mathlib overview: Linear algebra › Endomorphism polynomials](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L197)
- [Mathlib undergraduate list: Linear algebra › Endomorphism polynomials](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L57)
- [Freek Wiedijk's 100 theorems, no. 49](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L255)
- [1000+ theorems list: Q656772](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L701)
- [1000+ theorems project: Q656772](https://1000-plus.github.io/?length=-1#Q656772)
- [Wikipedia: Cayley–Hamilton theorem](https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem)
- [Wikidata: Q656772](https://www.wikidata.org/wiki/Q656772)
