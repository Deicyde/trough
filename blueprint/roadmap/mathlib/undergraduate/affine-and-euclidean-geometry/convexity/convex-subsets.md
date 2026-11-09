# Convex subsets

Convexity of sets.

```lean
Convex.{u_1, u_2} (𝕜 : Type u_1) {E : Type u_2} [Semiring 𝕜] [PartialOrder 𝕜] [AddCommMonoid E]
  [SMul 𝕜 E] (s : Set E) : Prop
```

## Depends on

- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Convex`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Basic.html#Convex)
- [Source of `Convex` in Mathlib/Analysis/Convex/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Convex/Basic.lean#L52)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › Convexity](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L255)
