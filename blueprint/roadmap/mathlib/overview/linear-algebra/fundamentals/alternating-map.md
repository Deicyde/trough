# Alternating map

An alternating map from `ι → M` to `N`, denoted `M [⋀^ι]→ₗ[R] N`,
is a multilinear map that vanishes when two of its arguments are equal.

```lean
AlternatingMap.{u_1, u_2, u_3, u_7} (R : Type u_1) [Semiring R] (M : Type u_2) [AddCommMonoid M]
  [_root_.Module R M] (N : Type u_3) [AddCommMonoid N] [_root_.Module R N] (ι : Type u_7) :
  Type (max (max u_2 u_3) u_7)
```

## Depends on

- [Multilinear map](multilinear-map.md)

## Sources

- [Mathlib documentation: `AlternatingMap`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Alternating/Basic.html#AlternatingMap)
- [Source of `AlternatingMap` in Mathlib/LinearAlgebra/Alternating/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/Alternating/Basic.lean#L66)
- [Mathlib overview: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L178)
