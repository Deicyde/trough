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
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Inner product space, over $R$ or $C$](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../../undergraduate/topology/normed-vector-spaces-on-and/norms-p-on-n-and-n.md)
- [Smooth map between manifolds](../../../overview/geometry/differentiable-manifolds/part-01/smooth-map-between-manifolds.md)
- [Smooth or analytic manifold (with boundary and corners)](../../../overview/geometry/differentiable-manifolds/part-01/smooth-or-analytic-manifold-with-boundary-and-co.md)

## Proof depends on

- [$C^k$ function](../../../overview/analysis/differentiability/c-k-function.md)
- [Cauchy-Schwarz inequality](../../../overview/analysis/hilbert-spaces/cauchy-schwarz-inequality.md)
- [Complementary subspaces](../../../undergraduate/linear-algebra/fundamentals/complementary-subspaces.md)
- [Completion of an abelian topological group](../../../overview/topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Continuity](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/continuity.md)
- [Continuity of the sum of a series of functions](../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/continuity-of-the-sum-of-a-series-of-functions.md)
- [Convolution](../../../overview/analysis/measures-and-integral-calculus/part-02/convolution.md)
- [Derivative of a composition of functions](../../../overview/analysis/differentiability/derivative-of-a-composition-of-functions.md)
- [Derivative of the inverse of a function](../../../overview/analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Derivative of the inverse of a function](../../../undergraduate/single-variable-real-analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Determinant of endomorphisms](../../../undergraduate/linear-algebra/multilinearity/determinant-of-endomorphisms.md)
- [Differentiability of the sum of a series of functions](../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/differentiability-of-the-sum-of-a-series-of-func.md)
- [Differentials (linear tangent functions)](../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Dimension theorem for vector spaces](../../algebra/15-linear-and-multilinear-algebra-matrix-theory/dimension-theorem-for-vector-spaces.md)
- [Dominated convergence theorem](../../../overview/analysis/measures-and-integral-calculus/part-01/dominated-convergence-theorem.md)
- [Dual of a normed space](../../../overview/analysis/normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Dual vector space](../../../overview/linear-algebra/duality/dual-vector-space.md)
- [Extreme value theorem](../../../overview/topology/topological-algebra/extreme-value-theorem.md)
- [Fubini's theorem](../../../overview/analysis/measures-and-integral-calculus/part-02/fubinis-theorem.md)
- [Gaussian elimination](../../../undergraduate/linear-algebra/matrices/gaussian-elimination.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../../overview/analysis/normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Hilbert projection theorem](../../../undergraduate/topology/hilbert-spaces/hilbert-projection-theorem.md)
- [Holomorphic functions](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Lebesgue measure](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Local convexity](../../../overview/analysis/topological-vector-spaces/local-convexity.md)
- [M. Riesz extension theorem](../../analysis/46-functional-analysis/part-02/m-riesz-extension-theorem.md)
- [Maximal ideal](../../../overview/general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Orthogonal projection](../../../overview/analysis/hilbert-spaces/orthogonal-projection.md)
- [Polynomial derivative](../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md)
- [Polynomial functions](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-etc/polynomial-functions.md)
- [Probability measure](../../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Product of finitely many measures](../../../overview/analysis/measures-and-integral-calculus/part-02/product-of-finitely-many-measures.md)
- [Quotient ring](../../../overview/general-algebra/ideals-and-quotients/quotient-ring.md)
- [Self-adjoint operator](../../../overview/analysis/hilbert-spaces/self-adjoint-operator.md)
- [Stieltjes measure](../../../overview/analysis/measures-and-integral-calculus/part-01/stieltjes-measure.md)
- [Sum of a Geometric Series](../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [The Number of Subsets of a Set](../../../hundred-theorems/part-03/the-number-of-subsets-of-a-set.md)

## Sources

- [Mathlib documentation: `exists_embedding_euclidean_of_compact`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/WhitneyEmbedding.html#exists_embedding_euclidean_of_compact)
- [Source of `exists_embedding_euclidean_of_compact` in Mathlib/Geometry/Manifold/WhitneyEmbedding.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/WhitneyEmbedding.lean#L129)
- [1000+ theorems list: Q1306095](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1589)
- [1000+ theorems project: Q1306095](https://1000-plus.github.io/?length=-1#Q1306095)
- [Wikipedia: Whitney embedding theorem](https://en.wikipedia.org/wiki/Whitney_embedding_theorem)
- [Wikidata: Q1306095](https://www.wikidata.org/wiki/Q1306095)
