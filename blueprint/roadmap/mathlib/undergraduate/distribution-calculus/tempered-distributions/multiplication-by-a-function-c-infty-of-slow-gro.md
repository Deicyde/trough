# Multiplication by a function $C^\infty$ of slow growth

Multiplication with a temperate growth function as a continuous linear map on `𝓢'(E, F)`.

```lean
TemperedDistribution.smulLeftCLM.{u_3, u_4} {E : Type u_3} (F : Type u_4) [NormedAddCommGroup E]
  [NormedSpace ℝ E] [AddCommGroup F] [_root_.Module ℂ F] [TopologicalSpace F]
  [IsTopologicalAddGroup F] [ContinuousConstSMul ℂ F] (g : E → ℂ) :
  TemperedDistribution E F →L[ℂ] TemperedDistribution E F
```

## Depends on

- [Algebra of endomorphisms of a vector space](../../linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Stability by multiplication by a slowly growing smooth function](../spaces-s-r-d/stability-by-multiplication-by-a-slowly-growing.md)
- [Tempered distributions](../../../overview/analysis/distribution-theory/tempered-distributions.md)

## Sources

- [Mathlib documentation: `TemperedDistribution.smulLeftCLM`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Distribution/TemperedDistribution.html#TemperedDistribution.smulLeftCLM)
- [Source of `TemperedDistribution.smulLeftCLM` in Mathlib/Analysis/Distribution/TemperedDistribution.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Distribution/TemperedDistribution.lean#L247)
- [Mathlib undergraduate list: Distribution calculus › Tempered distributions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L616)
