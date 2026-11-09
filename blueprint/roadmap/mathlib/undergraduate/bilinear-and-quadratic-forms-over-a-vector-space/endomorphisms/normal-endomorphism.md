# Normal endomorphism

An element of a star monoid is normal if it commutes with its adjoint.

```lean
IsStarNormal.{u_1} {R : Type u_1} [Mul R] [Star R] (x : R) : Prop
```

## Depends on

Its statement uses no other concept on these lists.

## Sources

- [Mathlib documentation: `IsStarNormal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Star/SelfAdjoint.html#IsStarNormal)
- [Source of `IsStarNormal` in Mathlib/Algebra/Star/SelfAdjoint.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/Star/SelfAdjoint.lean#L53)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Endomorphisms](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L228)
