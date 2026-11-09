# Stability by derivation

The Fréchet derivative on Schwartz space as a continuous `𝕜`-linear map.

```lean
SchwartzMap.fderivCLM.{u_2, u_4, u_7} (𝕜 : Type u_2) (E : Type u_4) (F : Type u_7)
  [NormedAddCommGroup E] [NormedAddCommGroup F] [NormedSpace ℝ F] [NormedSpace ℝ E] [RCLike 𝕜]
  [NormedSpace 𝕜 F] [SMulCommClass ℝ 𝕜 F] : SchwartzMap E F →L[𝕜] SchwartzMap E (E →L[ℝ] F)
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Schwartz space](../../../overview/analysis/distribution-theory/schwartz-space.md)

## Sources

- [Mathlib documentation: `SchwartzMap.fderivCLM`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Distribution/SchwartzSpace/Deriv.html#SchwartzMap.fderivCLM)
- [Source of `SchwartzMap.fderivCLM` in Mathlib/Analysis/Distribution/SchwartzSpace/Deriv.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Distribution/SchwartzSpace/Deriv.lean#L81)
- [Mathlib undergraduate list: Distribution calculus › Spaces $\mathcal{S}(\R^d)$](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L608)
