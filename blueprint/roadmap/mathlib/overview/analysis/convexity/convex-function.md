# Convex function

Convexity of functions

```lean
ConvexOn.{u_1, u_2, u_5} (𝕜 : Type u_1) {E : Type u_2} {β : Type u_5} [Semiring 𝕜] [PartialOrder 𝕜]
  [AddCommMonoid E] [AddCommMonoid β] [PartialOrder β] [SMul 𝕜 E] [SMul 𝕜 β] (s : Set E)
  (f : E → β) : Prop
```

## Depends on

- [Convex subsets](../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)

## Sources

- [Mathlib documentation: `ConvexOn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Function.html#ConvexOn)
- [Source of `ConvexOn` in Mathlib/Analysis/Convex/Function.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Convex/Function.lean#L53)
- [Mathlib overview: Analysis › Convexity](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L321)
- [Mathlib undergraduate list: Single Variable Real Analysis › Convexity](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L359)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L471)
