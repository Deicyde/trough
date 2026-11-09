# Differentiable functions

`Differentiable 𝕜 f` means that `f` is differentiable at any point.

```lean
Differentiable.{u_1, u_2, u_3} (𝕜 : Type u_1) [NontriviallyNormedField 𝕜] {E : Type u_2}
  [AddCommGroup E] [_root_.Module 𝕜 E] [TopologicalSpace E] {F : Type u_3} [AddCommGroup F]
  [_root_.Module 𝕜 F] [TopologicalSpace F] (f : E → F) : Prop
```

## Depends on

- [Differentiable function between normed vector spaces](../../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)

## Sources

- [Mathlib documentation: `Differentiable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/FDeriv/Defs.html#Differentiable)
- [Source of `Differentiable` in Mathlib/Analysis/Calculus/FDeriv/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Calculus/FDeriv/Defs.lean#L170)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L464)
