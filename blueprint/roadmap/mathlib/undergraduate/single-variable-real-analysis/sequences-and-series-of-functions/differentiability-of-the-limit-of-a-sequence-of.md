---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: hasFDerivAt_of_tendstoUniformly
mathlib_file: Mathlib/Analysis/Calculus/UniformLimitsDeriv.lean
---

# Differentiability of the limit of a sequence of functions

`(d/dx) lim_{n → ∞} f n x = lim_{n → ∞} f' n x` when the `f' n` converge
_uniformly_ to their limit.

```lean
hasFDerivAt_of_tendstoUniformly.{u_1, u_2, u_3, u_4} {ι : Type u_1} {l : Filter ι} {E : Type u_2}
  [NormedAddCommGroup E] {𝕜 : Type u_3} [NontriviallyNormedField 𝕜] [IsRCLikeNormedField 𝕜]
  [NormedSpace 𝕜 E] {G : Type u_4} [NormedAddCommGroup G] [NormedSpace 𝕜 G] {f : ι → E → G}
  {g : E → G} {f' : ι → E → E →L[𝕜] G} {g' : E → E →L[𝕜] G} [l.NeBot]
  (hf' : TendstoUniformly f' g' l) (hf : ∀ (n : ι) (x : E), HasFDerivAt (f n) (f' n x) x)
  (hfg : ∀ (x : E), Filter.Tendsto (fun n => f n x) l (nhds (g x))) (x : E) : HasFDerivAt g (g' x) x
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Differentiable function between normed vector spaces](../../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Field $\R$ of real numbers](../../ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Induced topology](../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Metric structure](../topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Permutation group of a type](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Uniform convergence](../../../overview/topology/uniform-notions/uniform-convergence.md)

## Proof depends on

- [Affine function](../../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Completeness of R](../topology-of-r/completeness-of-r.md)
- [Convex function](../../../overview/analysis/convexity/convex-function.md)
- [Derivative at a point](../differentiability/derivative-at-a-point.md)
- [Euclidean affine space](../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../topology/topology-and-metric-spaces/homeomorphisms.md)
- [Lipschitz continuity](../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Norm of a continuous linear map](../../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Open map](../../../overview/topology/general-topology/part-01/open-map.md)
- [Product of vector spaces](../../linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `hasFDerivAt_of_tendstoUniformly`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/UniformLimitsDeriv.html#hasFDerivAt_of_tendstoUniformly)
- [Source of `hasFDerivAt_of_tendstoUniformly` in Mathlib/Analysis/Calculus/UniformLimitsDeriv.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/UniformLimitsDeriv.lean#L427)
- [Mathlib undergraduate list: Single Variable Real Analysis › Sequences and series of functions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L354)
