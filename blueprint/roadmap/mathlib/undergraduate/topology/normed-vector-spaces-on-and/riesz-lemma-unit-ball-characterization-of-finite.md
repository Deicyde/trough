---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: FiniteDimensional.of_isCompact_closedBall
mathlib_file: Mathlib/Analysis/Normed/Module/FiniteDimension.lean
---

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

- [Affine space](../../../overview/geometry/affine-and-euclidean-geometry/affine-space.md)
- [Finite-dimensional normed spaces over complete normed fields are complete](../../../overview/analysis/normed-vector-spaces-banach-spaces/finite-dimensional-normed-spaces-over-complete-n.md)
- [Open map](../../../overview/topology/general-topology/part-01/open-map.md)

## Sources

- [Mathlib documentation: `FiniteDimensional.of_isCompact_closedBall`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Module/FiniteDimension.html#FiniteDimensional.of_isCompact_closedBall)
- [Source of `FiniteDimensional.of_isCompact_closedBall` in Mathlib/Analysis/Normed/Module/FiniteDimension.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Module/FiniteDimension.lean#L473)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L435)
