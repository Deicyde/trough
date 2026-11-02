---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: TestFunction
mathlib_file: Mathlib/Analysis/Distribution/TestFunction.lean
---

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
- [Source of `TestFunction` in Mathlib/Analysis/Distribution/TestFunction.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Distribution/TestFunction.lean#L66)
- [Mathlib overview: Analysis › Distribution theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L379)
- [Mathlib undergraduate list: Distribution calculus › Spaces $\mathcal{D}(\R^d)$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L590)
