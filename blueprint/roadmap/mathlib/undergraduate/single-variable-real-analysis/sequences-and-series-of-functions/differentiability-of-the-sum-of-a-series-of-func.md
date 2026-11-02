---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: differentiable_tsum
mathlib_file: Mathlib/Analysis/Calculus/SmoothSeries.lean
---

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
- [Field $\R$ of real numbers](../../ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Metric structure](../topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Permutation group of a type](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)

## Proof depends on

- [Absolutely convergent series in Banach spaces](../../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Affine function](../../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Connected components](../../topology/topology-and-metric-spaces/connected-components.md)
- [Connectedness](../../../overview/topology/general-topology/part-01/connectedness.md)
- [Convex function](../../../overview/analysis/convexity/convex-function.md)
- [Derivative at a point](../differentiability/derivative-at-a-point.md)
- [Euclidean affine space](../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Existence of bases](../../linear-algebra/fundamentals/existence-of-bases.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../topology/topology-and-metric-spaces/homeomorphisms.md)
- [Kernel of a linear map](../../linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Norm of a continuous linear map](../../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Open map](../../../overview/topology/general-topology/part-01/open-map.md)
- [Path connectedness](../../topology/topology-and-metric-spaces/path-connectedness.md)
- [Product of vector spaces](../../linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Sequential space](../../../overview/topology/general-topology/part-01/sequential-space.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [Sum of subspaces](../../linear-algebra/fundamentals/sum-of-subspaces.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `differentiable_tsum`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/SmoothSeries.html#differentiable_tsum)
- [Source of `differentiable_tsum` in Mathlib/Analysis/Calculus/SmoothSeries.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/SmoothSeries.lean#L139)
- [Mathlib undergraduate list: Single Variable Real Analysis › Sequences and series of functions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L355)
