# Riesz' lemma (unit-ball characterization of finite dimension)

**Riesz's theorem**: if a closed ball of positive radius is compact in a vector space, then the
space is finite-dimensional.

```lean
FiniteDimensional.of_isCompact_closedBall.{u, u_1} (𝕜 : Type u) [NontriviallyNormedField 𝕜]
  [CompleteSpace 𝕜] {V : Type u_1} [NormedAddCommGroup V] [_root_.Module 𝕜 V] [ContinuousSMul 𝕜 V]
  {r : ℝ} (rpos : 0 < r) {c : V} (h : IsCompact (Metric.closedBall c r)) : FiniteDimensional 𝕜 V
```

## Depends on

- [Compactness in terms of filters](../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)

## Proof depends on

- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Topology of a metric space](../topology-and-metric-spaces/topology-of-a-metric-space.md)

## Sources

- [Mathlib documentation: `FiniteDimensional.of_isCompact_closedBall`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Module/FiniteDimension.html#FiniteDimensional.of_isCompact_closedBall)
- [Source of `FiniteDimensional.of_isCompact_closedBall` in Mathlib/Analysis/Normed/Module/FiniteDimension.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Normed/Module/FiniteDimension.lean#L476)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L435)
