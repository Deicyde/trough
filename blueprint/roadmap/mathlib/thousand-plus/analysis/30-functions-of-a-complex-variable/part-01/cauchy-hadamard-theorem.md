---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: FormalMultilinearSeries.radius_inv_eq_limsup
mathlib_file: Mathlib/Analysis/Analytic/RadiusLiminf.lean
---

# Cauchy–Hadamard theorem

The **Cauchy-Hadamard theorem** for formal multilinear series: The inverse of the radius
is equal to $\limsup_{n\to\infty} \sqrt[n]{‖p n‖}$.

```lean
FormalMultilinearSeries.radius_inv_eq_limsup.{u_1, u_2, u_3} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {F : Type u_3}
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] (p : FormalMultilinearSeries 𝕜 E F) :
  p.radius⁻¹ = Filter.limsup (fun n => ↑(‖p n‖₊ ^ (1 / ↑n))) Filter.atTop
```

## Depends on

- [Power functions](../../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/power-functions.md)
- [Radius of convergence](../../../../undergraduate/single-variable-complex-analysis/complex-valued-series/radius-of-convergence.md)
- [Ring structure $\Z$](../../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Cluster point](../../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Field $\C$ of complex numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Intermediate value theorem](../../../../overview/topology/topological-algebra/intermediate-value-theorem.md)
- [Lipschitz continuity](../../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Norm of a continuous linear map](../../../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Open map](../../../../overview/topology/general-topology/part-01/open-map.md)
- [Squeeze theorem](../../26-real-functions/part-03/squeeze-theorem.md)
- [The Binomial Theorem](../../../../hundred-theorems/part-03/the-binomial-theorem.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological module](../../../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `FormalMultilinearSeries.radius_inv_eq_limsup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Analytic/RadiusLiminf.html#FormalMultilinearSeries.radius_inv_eq_limsup)
- [Source of `FormalMultilinearSeries.radius_inv_eq_limsup` in Mathlib/Analysis/Analytic/RadiusLiminf.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Analytic/RadiusLiminf.lean#L64)
- [1000+ theorems list: Q859122](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1000)
- [1000+ theorems project: Q859122](https://1000-plus.github.io/?length=-1#Q859122)
- [Wikipedia: Cauchy–Hadamard theorem](https://en.wikipedia.org/wiki/Cauchy%E2%80%93Hadamard_theorem)
- [Wikidata: Q859122](https://www.wikidata.org/wiki/Q859122)
