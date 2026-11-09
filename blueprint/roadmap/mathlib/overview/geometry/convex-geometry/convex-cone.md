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
- [Source of `ConvexCone` in Mathlib/Geometry/Convex/Cone/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Geometry/Convex/Cone/Basic.lean#L56)
- [Mathlib overview: Geometry › Convex geometry](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L488)
