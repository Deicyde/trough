# Stability by multiplication by a slowly growing smooth function

The map `f ↦ (x ↦ B (f x) (g x))` as a continuous `𝕜`-linear map on Schwartz space,
where `B` is a continuous `𝕜`-linear map and `g` is a function of temperate growth.

```lean
SchwartzMap.bilinLeftCLM.{u_2, u_4, u_5, u_6, u_7} {𝕜 : Type u_2} {D : Type u_4} {E : Type u_5}
  {F : Type u_6} {G : Type u_7} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [NontriviallyNormedField 𝕜] [NormedAlgebra ℝ 𝕜] [NormedAddCommGroup D]
  [NormedSpace ℝ D] [NormedAddCommGroup G] [NormedSpace ℝ G] [NormedSpace 𝕜 F] [NormedSpace 𝕜 E]
  [NormedSpace 𝕜 G] (B : E →L[𝕜] F →L[𝕜] G) {g : D → F} (hg : Function.HasTemperateGrowth g) :
  SchwartzMap D E →L[𝕜] SchwartzMap D G
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Schwartz space](../../../overview/analysis/distribution-theory/schwartz-space.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)

## Sources

- [Mathlib documentation: `SchwartzMap.bilinLeftCLM`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Distribution/SchwartzSpace/Basic.html#SchwartzMap.bilinLeftCLM)
- [Source of `SchwartzMap.bilinLeftCLM` in Mathlib/Analysis/Distribution/SchwartzSpace/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Distribution/SchwartzSpace/Basic.lean#L671)
- [Mathlib undergraduate list: Distribution calculus › Spaces $\mathcal{S}(\R^d)$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L609)
