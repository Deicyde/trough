---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: Distribution
mathlib_file: Mathlib/Analysis/Distribution/Distribution.lean
---

# Distributions

`𝓓'^{n}(Ω, F) = Distribution Ω F n` is the space of `F`-valued distributions on `Ω` with
order at most `n`.

In most cases you want to use the space `𝓓'(Ω, F) = Distribution Ω F ⊤`.

```lean
Distribution.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  (Ω : TopologicalSpace.Opens E) (F : Type u_2) [AddCommGroup F] [_root_.Module ℝ F]
  [TopologicalSpace F] (n : ℕ∞) : Type (max u_1 u_2)
```

## Depends on

- [Inner product space, over $R$ or $C$](../hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Test functions](test-functions.md)

## Sources

- [Mathlib documentation: `Distribution`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Distribution/Distribution.html#Distribution)
- [Source of `Distribution` in Mathlib/Analysis/Distribution/Distribution.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Distribution/Distribution.lean#L162)
- [Mathlib overview: Analysis › Distribution theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L381)
- [Mathlib undergraduate list: Distribution calculus › Distributions on $\R^d$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L596)
