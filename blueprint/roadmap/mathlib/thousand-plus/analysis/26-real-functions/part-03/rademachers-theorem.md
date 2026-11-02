---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: LipschitzOnWith.ae_differentiableWithinAt
mathlib_file: Mathlib/Analysis/Calculus/Rademacher.lean
---

# Rademacher's theorem

*Rademacher's theorem*: a function between finite-dimensional real vector spaces which is
Lipschitz on a set is differentiable almost everywhere in this set.

```lean
LipschitzOnWith.ae_differentiableWithinAt.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [MeasurableSpace E] [BorelSpace E] {F : Type u_2} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {C : NNReal} {s : Set E} {μ : MeasureTheory.Measure E} [FiniteDimensional ℝ E]
  [FiniteDimensional ℝ F] [μ.IsAddHaarMeasure] {f : E → F} (hf : LipschitzOnWith C f s)
  (hs : MeasurableSet s) : ∀ᵐ (x : E) ∂μ.restrict s, DifferentiableWithinAt ℝ f s x
```

## Depends on

- [Almost sure convergence](../../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Borel sigma-algebra](../../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Compactness in terms of filters](../../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Continuous linear map](../../../../overview/topology/topological-algebra/continuous-linear-map.md)
- [Field $\R$ of real numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-of-real-numbers.md)
- [Finite-dimensionality](../../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Induced topology](../../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Measurable function](../../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Positive measure](../../../../overview/analysis/measures-and-integral-calculus/part-01/positive-measure.md)

## Proof depends on

- [Cauchy-Schwarz inequality](../../../../overview/analysis/hilbert-spaces/cauchy-schwarz-inequality.md)
- [Compactness in terms of open covers (Borel-Lebesgue)](../../../../overview/topology/general-topology/part-01/compactness-in-terms-of-open-covers-borel-lebesg.md)
- [Complementary subspaces](../../../../undergraduate/linear-algebra/fundamentals/complementary-subspaces.md)
- [Continuity](../../../../undergraduate/single-variable-complex-analysis/complex-valued-series/continuity.md)
- [Continuity of the sum of a series of functions](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/continuity-of-the-sum-of-a-series-of-functions.md)
- [Convolution](../../../../overview/analysis/measures-and-integral-calculus/part-02/convolution.md)
- [Derivative of a composition of functions](../../../../overview/analysis/differentiability/derivative-of-a-composition-of-functions.md)
- [Derivative of the inverse of a function](../../../../overview/analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Derivative of the inverse of a function](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Determinant of endomorphisms](../../../../undergraduate/linear-algebra/multilinearity/determinant-of-endomorphisms.md)
- [Differentiability of the sum of a series of functions](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/differentiability-of-the-sum-of-a-series-of-func.md)
- [Dimension theorem for vector spaces](../../../algebra/15-linear-and-multilinear-algebra-matrix-theory/dimension-theorem-for-vector-spaces.md)
- [Directional derivative](../../../../undergraduate/multivariable-calculus/differential-calculus/directional-derivative.md)
- [Dominated convergence theorem](../../../../overview/analysis/measures-and-integral-calculus/part-01/dominated-convergence-theorem.md)
- [Extreme value theorem](../../../../overview/topology/topological-algebra/extreme-value-theorem.md)
- [Fubini's theorem](../../../../overview/analysis/measures-and-integral-calculus/part-02/fubinis-theorem.md)
- [Gaussian elimination](../../../../undergraduate/linear-algebra/matrices/gaussian-elimination.md)
- [Hahn-Banach theorem](../../../../overview/analysis/normed-vector-spaces-banach-spaces/hahn-banach-theorem.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../../../overview/analysis/normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Hilbert projection theorem](../../../../undergraduate/topology/hilbert-spaces/hilbert-projection-theorem.md)
- [Lebesgue measure](../../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Lebesgue's decomposition theorem](../../../geometry-and-topology/54-general-topology/part-01/lebesgues-decomposition-theorem.md)
- [Local convexity](../../../../overview/analysis/topological-vector-spaces/local-convexity.md)
- [Maximal ideal](../../../../overview/general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../../../undergraduate/topology/normed-vector-spaces-on-and/norms-p-on-n-and-n.md)
- [Orthogonal projection](../../../../overview/analysis/hilbert-spaces/orthogonal-projection.md)
- [Polynomial derivative](../../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md)
- [Polynomial functions](../../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-etc/polynomial-functions.md)
- [Probability measure](../../../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Product of finitely many measures](../../../../overview/analysis/measures-and-integral-calculus/part-02/product-of-finitely-many-measures.md)
- [Product of manifolds](../../../../overview/geometry/differentiable-manifolds/part-01/product-of-manifolds.md)
- [Quotient ring](../../../../overview/general-algebra/ideals-and-quotients/quotient-ring.md)
- [Self-adjoint operator](../../../../overview/analysis/hilbert-spaces/self-adjoint-operator.md)
- [Smooth map between manifolds](../../../../overview/geometry/differentiable-manifolds/part-01/smooth-map-between-manifolds.md)
- [Stieltjes measure](../../../../overview/analysis/measures-and-integral-calculus/part-01/stieltjes-measure.md)
- [Urysohn's lemma](../../../../overview/topology/general-topology/part-02/urysohns-lemma.md)
- [Vitali covering theorem](../../28-measure-and-integration/part-02/vitali-covering-theorem.md)

## Sources

- [Mathlib documentation: `LipschitzOnWith.ae_differentiableWithinAt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Rademacher.html#LipschitzOnWith.ae_differentiableWithinAt)
- [Source of `LipschitzOnWith.ae_differentiableWithinAt` in Mathlib/Analysis/Calculus/Rademacher.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Rademacher.lean#L374)
- [1000+ theorems list: Q132427](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L45)
- [1000+ theorems project: Q132427](https://1000-plus.github.io/?length=-1#Q132427)
- [Wikipedia: Rademacher's theorem](https://en.wikipedia.org/wiki/Rademacher's_theorem)
- [Wikidata: Q132427](https://www.wikidata.org/wiki/Q132427)
