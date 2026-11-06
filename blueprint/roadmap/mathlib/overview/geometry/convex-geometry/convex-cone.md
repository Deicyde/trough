# Convex cone

A convex cone is a subset `s` of an `R`-module such that `a • x + b • y ∈ s` whenever `a, b > 0`
and `x, y ∈ s`.

```lean
ConvexCone.{u_2, u_4} (R : Type u_2) (M : Type u_4) [Semiring R] [PartialOrder R] [AddCommMonoid M]
  [SMul R M] : Type u_4
```

## Depends on

- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `ConvexCone`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Convex/Cone/Basic.html#ConvexCone)
- [Source of `ConvexCone` in Mathlib/Geometry/Convex/Cone/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Convex/Cone/Basic.lean#L56)
- [Mathlib overview: Geometry › Convex geometry](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L488)
