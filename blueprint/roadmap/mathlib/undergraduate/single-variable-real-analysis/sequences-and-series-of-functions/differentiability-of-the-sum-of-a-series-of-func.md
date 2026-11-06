# Differentiability of the sum of a series of functions

Consider a series of functions `∑' n, f n x`. If all functions in the series are differentiable
with a summable bound on the derivatives, then the series is differentiable.
Note that our assumptions do not ensure the pointwise convergence, but if there is no pointwise
convergence then the series is zero everywhere so the result still holds.

```lean
differentiable_tsum.{u_1, u_2, u_3, u_4} {α : Type u_1} {𝕜 : Type u_2} {E : Type u_3} {F : Type u_4}
  [NontriviallyNormedField 𝕜] [IsRCLikeNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [NormedAddCommGroup F] [CompleteSpace F] {u : α → ℝ} [NormedSpace 𝕜 F] {f : α → E → F}
  {f' : α → E → E →L[𝕜] F} (hu : Summable u) (hf : ∀ (n : α) (x : E), HasFDerivAt (f n) (f' n x) x)
  (hf' : ∀ (n : α) (x : E), ‖f' n x‖ ≤ u n) : Differentiable 𝕜 fun y => ∑' (n : α), f n y
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Differentiable functions](../../multivariable-calculus/differential-calculus/differentiable-functions.md)
- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Absolutely convergent series in Banach spaces](../../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Connectedness](../../../overview/topology/general-topology/part-01/connectedness.md)
- [Sequential space](../../../overview/topology/general-topology/part-01/sequential-space.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)
- [Topology of a metric space](../../topology/topology-and-metric-spaces/topology-of-a-metric-space.md)

## Sources

- [Mathlib documentation: `differentiable_tsum`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/SmoothSeries.html#differentiable_tsum)
- [Source of `differentiable_tsum` in Mathlib/Analysis/Calculus/SmoothSeries.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/SmoothSeries.lean#L139)
- [Mathlib undergraduate list: Single Variable Real Analysis › Sequences and series of functions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L355)
