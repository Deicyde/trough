# Self-adjoint operator

An element is self-adjoint if it is equal to its star.

```lean
IsSelfAdjoint.{u_1} {R : Type u_1} [Star R] (x : R) : Prop
```

## Depends on

Its statement uses no other concept on these lists.

## Sources

- [Mathlib documentation: `IsSelfAdjoint`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Star/SelfAdjoint.html#IsSelfAdjoint)
- [Source of `IsSelfAdjoint` in Mathlib/Algebra/Star/SelfAdjoint.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Star/SelfAdjoint.lean#L49)
- [Mathlib overview: Analysis › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L297)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Endomorphisms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L227)
