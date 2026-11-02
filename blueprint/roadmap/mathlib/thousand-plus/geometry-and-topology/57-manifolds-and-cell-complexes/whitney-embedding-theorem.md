---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: exists_embedding_euclidean_of_compact
mathlib_file: Mathlib/Geometry/Manifold/WhitneyEmbedding.lean
---

# Whitney embedding theorem

Baby version of the Whitney weak embedding theorem: if `M` admits a finite covering by
supports of bump functions, then for some `n` it can be embedded into the `n`-dimensional
Euclidean space.

```lean
exists_embedding_euclidean_of_compact.{uE, uH, uM} {E : Type uE} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type uH} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type uM} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [T2Space M] [CompactSpace M] :
  ∃ n e,
    ContMDiff I (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin n))) (↑⊤) e ∧
      Topology.IsClosedEmbedding e ∧ ∀ (x : M), Function.Injective ⇑(mfderiv% e x)
```

baby version: for compact manifolds; embedding into some *n*.

## Depends on

- [Compactness in terms of filters](../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Induced topology](../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Inner product space, over $R$ or $C$](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../../undergraduate/topology/normed-vector-spaces-on-r-and-c/norms-lvert-cdot-rvert-p-on-r-n-and-c-n.md)
- [Smooth map between manifolds](../../../overview/geometry/differentiable-manifolds/part-01/smooth-map-between-manifolds.md)
- [Smooth or analytic manifold (with boundary and corners)](../../../overview/geometry/differentiable-manifolds/part-01/smooth-or-analytic-manifold-with-boundary-and-co.md)

## Proof depends on

- [Basis](../../../overview/linear-algebra/fundamentals/basis.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Differentiable function between normed vector spaces](../../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Equivalence of norms in finite dimension](../../../overview/analysis/normed-vector-spaces-banach-spaces/equivalence-of-norms-in-finite-dimension.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Linear independence](../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Noetherian ring](../../../overview/general-algebra/rings/noetherian-ring.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `exists_embedding_euclidean_of_compact`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/WhitneyEmbedding.html#exists_embedding_euclidean_of_compact)
- [Source of `exists_embedding_euclidean_of_compact` in Mathlib/Geometry/Manifold/WhitneyEmbedding.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/WhitneyEmbedding.lean#L129)
- [1000+ theorems list: Q1306095](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1589)
- [1000+ theorems project: Q1306095](https://1000-plus.github.io/all.html?length=-1#Q1306095)
- [Wikipedia: Whitney embedding theorem](https://en.wikipedia.org/wiki/Whitney_embedding_theorem)
- [Wikidata: Q1306095](https://www.wikidata.org/wiki/Q1306095)
