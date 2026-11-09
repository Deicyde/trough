# Test functions

The type of bundled `n`-times continuously differentiable maps with compact support

```lean
TestFunction.{u_3, u_4} {E : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  (Ω : TopologicalSpace.Opens E) (F : Type u_4) [NormedAddCommGroup F] [NormedSpace ℝ F] (n : ℕ∞) :
  Type (max u_3 u_4)
```

## Depends on

- [$C^k$ function](../differentiability/c-k-function.md)
- [Closure](../../topology/general-topology/part-01/closure.md)
- [Compactness in terms of filters](../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)

## Sources

- [Mathlib documentation: `TestFunction`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Distribution/TestFunction.html#TestFunction)
- [Source of `TestFunction` in Mathlib/Analysis/Distribution/TestFunction.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Distribution/TestFunction.lean#L66)
- [Mathlib overview: Analysis › Distribution theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L379)
- [Mathlib undergraduate list: Distribution calculus › Spaces $\mathcal{D}(\R^d)$](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L590)
