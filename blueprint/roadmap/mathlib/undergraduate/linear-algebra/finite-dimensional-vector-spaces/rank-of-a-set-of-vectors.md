# Rank of a set of vectors

The rank of a set of vectors as a natural number.

```lean
Set.finrank.{u, v} (R : Type u) {M : Type v} [Semiring R] [AddCommMonoid M] [_root_.Module R M]
  (s : Set M) : ℕ
```

## Depends on

- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Generating sets](../fundamentals/generating-sets.md)
- [Linear independence](../fundamentals/linear-independence.md)

## Sources

- [Mathlib documentation: `Set.finrank`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Dimension/Constructions.html#Set.finrank)
- [Source of `Set.finrank` in Mathlib/LinearAlgebra/Dimension/Constructions.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/Dimension/Constructions.lean#L438)
- [Mathlib undergraduate list: Linear algebra › Finite-dimensional vector spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L32)
