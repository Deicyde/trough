# Normal endomorphism

An element of a star monoid is normal if it commutes with its adjoint.

```lean
IsStarNormal.{u_1} {R : Type u_1} [Mul R] [Star R] (x : R) : Prop
```

## Depends on

Its statement uses no other concept on these lists.

## Sources

- [Mathlib documentation: `IsStarNormal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Star/SelfAdjoint.html#IsStarNormal)
- [Source of `IsStarNormal` in Mathlib/Algebra/Star/SelfAdjoint.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Algebra/Star/SelfAdjoint.lean#L52)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Endomorphisms](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L228)
