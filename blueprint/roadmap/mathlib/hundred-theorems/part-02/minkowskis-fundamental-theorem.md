---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.exists_ne_zero_mem_lattice_of_measure_mul_two_pow_lt_measure
mathlib_file: Mathlib/MeasureTheory/Group/GeometryOfNumbers.lean
---

# Minkowski’s Fundamental Theorem

The **Minkowski Convex Body Theorem**. If `s` is a convex symmetric domain of `E` whose volume
is large enough compared to the covolume of a lattice `L` of `E`, then it contains a non-zero
lattice point of `L`.

```lean
MeasureTheory.exists_ne_zero_mem_lattice_of_measure_mul_two_pow_lt_measure.{u_1} {E : Type u_1}
  [MeasurableSpace E] {μ : MeasureTheory.Measure E} {F s : Set E} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [BorelSpace E] [FiniteDimensional ℝ E] [μ.IsAddHaarMeasure] {L : AddSubgroup E}
  [Countable ↥L] (fund : MeasureTheory.IsAddFundamentalDomain (↥L) F μ) (h_symm : ∀ x ∈ s, -x ∈ s)
  (h_conv : Convex ℝ s) (h : μ F * 2 ^ Module.finrank ℝ E < μ s) : ∃ x, x ≠ 0 ∧ ↑x ∈ s
```

## Depends on

- [Almost sure convergence](../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Associative algebra over a commutative ring](../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Borel sigma-algebra](../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Cardinal](../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Compactness in terms of filters](../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Convex subsets](../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Field $\R$ of real numbers](../../undergraduate/ring-theory/field-theory/part-01/field-of-real-numbers.md)
- [Finite-dimensionality](../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Linear independence](../../undergraduate/linear-algebra/fundamentals/linear-independence.md)
- [Measurable function](../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Metric structure](../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Positive measure](../../overview/analysis/measures-and-integral-calculus/part-01/positive-measure.md)

## Proof depends on

- [Affine groups](../../undergraduate/affine-and-euclidean-geometry/general-definitions/affine-groups.md)
- [Affine span](../../overview/geometry/affine-and-euclidean-geometry/affine-span.md)
- [Arithmetic Mean/Geometric Mean](arithmetic-mean-geometric-mean.md)
- [Barycenter](../../overview/geometry/affine-and-euclidean-geometry/barycenter.md)
- [Characteristic p](../../overview/general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../overview/topology/general-topology/part-01/closed-map.md)
- [Complementary subspaces](../../undergraduate/linear-algebra/fundamentals/complementary-subspaces.md)
- [Continuity of inverse functions](../../undergraduate/single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of/continuity-of-inverse-functions.md)
- [Convex hull of a subset of an affine real space](../../undergraduate/affine-and-euclidean-geometry/convexity/convex-hull-of-a-subset-of-an-affine-real-space.md)
- [Determinant of endomorphisms](../../undergraduate/linear-algebra/multilinearity/determinant-of-endomorphisms.md)
- [Dimension theorem for vector spaces](../../thousand-plus/algebra/15-linear-and-multilinear-algebra-matrix-theory/dimension-theorem-for-vector-spaces.md)
- [Euclidean affine space](../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Finite-dimensional normed spaces over complete normed fields are complete](../../overview/analysis/normed-vector-spaces-banach-spaces/finite-dimensional-normed-spaces-over-complete-n.md)
- [Gaussian elimination](../../undergraduate/linear-algebra/matrices/gaussian-elimination.md)
- [General linear group](../../overview/linear-algebra/fundamentals/general-linear-group.md)
- [Giry monad](../../overview/analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../overview/analysis/normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Hilbert projection theorem](../../undergraduate/topology/hilbert-spaces/hilbert-projection-theorem.md)
- [Integral of positive measurable functions](../../overview/analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Lebesgue measure](../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Limit point](../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Maximal ideal](../../overview/general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../undergraduate/topology/normed-vector-spaces-on-and/norms-p-on-n-and-n.md)
- [Orthogonal projection](../../overview/analysis/hilbert-spaces/orthogonal-projection.md)
- [Pointwise convergence](../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Probability measure](../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Product of finitely many measures](../../overview/analysis/measures-and-integral-calculus/part-02/product-of-finitely-many-measures.md)
- [Quotient ring](../../overview/general-algebra/ideals-and-quotients/quotient-ring.md)
- [Self-adjoint operator](../../overview/analysis/hilbert-spaces/self-adjoint-operator.md)
- [Stieltjes measure](../../overview/analysis/measures-and-integral-calculus/part-01/stieltjes-measure.md)

## Sources

- [Mathlib documentation: `MeasureTheory.exists_ne_zero_mem_lattice_of_measure_mul_two_pow_lt_measure`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Group/GeometryOfNumbers.html#MeasureTheory.exists_ne_zero_mem_lattice_of_measure_mul_two_pow_lt_measure)
- [Source of `MeasureTheory.exists_ne_zero_mem_lattice_of_measure_mul_two_pow_lt_measure` in Mathlib/MeasureTheory/Group/GeometryOfNumbers.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Group/GeometryOfNumbers.lean#L63)
- [Freek Wiedijk's 100 theorems, no. 40](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L210)
- [1000+ theorems list: Q1097021](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1350)
- [1000+ theorems project: Q1097021](https://1000-plus.github.io/?length=-1#Q1097021)
- [Wikipedia: Minkowski's theorem](https://en.wikipedia.org/wiki/Minkowski's_theorem)
- [Wikidata: Q1097021](https://www.wikidata.org/wiki/Q1097021)
