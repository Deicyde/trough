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
- [Carathéodory's theorem (measure theory)](../../28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Compactness in terms of filters](../../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Continuous linear map](../../../../overview/topology/topological-algebra/continuous-linear-map.md)
- [Finite-dimensionality](../../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Measurable function](../../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Normed vector space over a normed field](../../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Positive measure](../../../../overview/analysis/measures-and-integral-calculus/part-01/positive-measure.md)

## Proof depends on

- [$C^k$ function](../../../../overview/analysis/differentiability/c-k-function.md)
- [Characteristic zero](../../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Complementary subspaces](../../../../undergraduate/linear-algebra/fundamentals/complementary-subspaces.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Derivative at a point](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Derivative of a composition of functions (Analysis)](../../../../overview/analysis/differentiability/derivative-of-a-composition-of-functions.md)
- [Differentiable functions](../../../../undergraduate/multivariable-calculus/differential-calculus/differentiable-functions.md)
- [Directional derivative](../../../../undergraduate/multivariable-calculus/differential-calculus/directional-derivative.md)
- [Dominated convergence theorem](../../../../overview/analysis/measures-and-integral-calculus/part-01/dominated-convergence-theorem.md)
- [Dual of a normed space](../../../../overview/analysis/normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../../../overview/analysis/normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Homeomorphisms](../../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Isomorphism with $K^n$](../../../../overview/linear-algebra/finite-dimensional-vector-spaces/isomorphism-with-k-n.md)
- [Lebesgue measure (Measures and integral calculus)](../../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Lipschitz continuity](../../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Order topology](../../../../overview/topology/topological-algebra/order-topology.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-04/the-triangle-inequality.md)
- [Topology of a metric space](../../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)

## Sources

- [Mathlib documentation: `LipschitzOnWith.ae_differentiableWithinAt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Rademacher.html#LipschitzOnWith.ae_differentiableWithinAt)
- [Source of `LipschitzOnWith.ae_differentiableWithinAt` in Mathlib/Analysis/Calculus/Rademacher.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Rademacher.lean#L374)
- [1000+ theorems list: Q132427](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L45)
- [1000+ theorems project: Q132427](https://1000-plus.github.io/all.html?length=-1#Q132427)
- [Wikipedia: Rademacher's theorem](https://en.wikipedia.org/wiki/Rademacher's_theorem)
- [Wikidata: Q132427](https://www.wikidata.org/wiki/Q132427)
