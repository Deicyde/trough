# Tempered distributions

The space of tempered distribution is the space of continuous linear maps from the Schwartz to
a normed space, equipped with the topology of pointwise convergence.

```lean
TemperedDistribution.{u_3, u_4} (E : Type u_3) (F : Type u_4) [NormedAddCommGroup E]
  [NormedSpace ℝ E] [TopologicalSpace F] [AddCommGroup F] [_root_.Module ℂ F] : Type (max u_3 u_4)
```

## Depends on

- [Complex number](../../general-algebra/numbers/complex-number.md)
- [Inner product space, over $R$ or $C$](../hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Schwartz space](schwartz-space.md)

## Sources

- [Mathlib documentation: `TemperedDistribution`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Distribution/TemperedDistribution.html#TemperedDistribution)
- [Source of `TemperedDistribution` in Mathlib/Analysis/Distribution/TemperedDistribution.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Analysis/Distribution/TemperedDistribution.lean#L51)
- [Mathlib overview: Analysis › Distribution theory](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L382)
- [Mathlib undergraduate list: Distribution calculus › Tempered distributions](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L614)
