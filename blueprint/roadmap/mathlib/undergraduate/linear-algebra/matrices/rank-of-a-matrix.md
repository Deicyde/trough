# Rank of a matrix

The rank of a matrix is the rank of its image.

```lean
Matrix.rank.{um, un, uR} {m : Type um} {n : Type un} {R : Type uR} [Fintype n] [CommSemiring R]
  (A : Matrix m n R) : ℕ
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Linear independence](../fundamentals/linear-independence.md)
- [Range of a linear map](../fundamentals/range-of-a-linear-map.md)
- [Ring-valued matrix](../../../overview/linear-algebra/matrices/ring-valued-matrix.md)

## Sources

- [Mathlib documentation: `Matrix.rank`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Rank.html#Matrix.rank)
- [Source of `Matrix.rank` in Mathlib/LinearAlgebra/Matrix/Rank.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/LinearAlgebra/Matrix/Rank.lean#L132)
- [Mathlib undergraduate list: Linear algebra › Matrices](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L46)
