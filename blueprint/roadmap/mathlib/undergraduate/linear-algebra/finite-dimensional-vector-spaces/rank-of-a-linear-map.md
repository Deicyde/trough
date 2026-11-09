# Rank of a linear map

`rank f` is the rank of a `LinearMap` `f`, defined as the dimension of `f.range`.

```lean
LinearMap.rank.{u, v, v'} {K : Type u} {V : Type v} {V' : Type v'} [Semiring K] [AddCommMonoid V]
  [_root_.Module K V] [AddCommMonoid V'] [_root_.Module K V'] (f : V →ₗ[K] V') : Cardinal.{v'}
```

## Depends on

- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Linear independence](../fundamentals/linear-independence.md)
- [Range of a linear map](../fundamentals/range-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `LinearMap.rank`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Dimension/LinearMap.html#LinearMap.rank)
- [Source of `LinearMap.rank` in Mathlib/LinearAlgebra/Dimension/LinearMap.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/Dimension/LinearMap.lean#L39)
- [Mathlib undergraduate list: Linear algebra › Finite-dimensional vector spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L31)
