# Orientation of a $\R$-vector space

An orientation of a module, intended to be used when `ι` is a `Fintype` with the same
cardinality as a basis.

```lean
Orientation.{u_1, u_2, u_4} (R : Type u_1) [CommSemiring R] [PartialOrder R] [IsStrictOrderedRing R]
  (M : Type u_2) [AddCommMonoid M] [_root_.Module R M] (ι : Type u_4) : Type (max (max u_4 u_1) u_2)
```

## Depends on

- [Alternating map](../../../overview/linear-algebra/fundamentals/alternating-map.md)
- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)

## Sources

- [Mathlib documentation: `Orientation`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Orientation.html#Orientation)
- [Source of `Orientation` in Mathlib/LinearAlgebra/Orientation.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/LinearAlgebra/Orientation.lean#L48)
- [Mathlib undergraduate list: Linear algebra › Multilinearity](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L40)
