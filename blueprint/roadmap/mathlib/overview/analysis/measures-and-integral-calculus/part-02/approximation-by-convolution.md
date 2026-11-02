---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ContDiffBump.convolution_tendsto_right
mathlib_file: Mathlib/Analysis/Calculus/BumpFunction/Convolution.lean
---

# Approximation by convolution

`(φ i ⋆ g i) (k i)` tends to `z₀` as `i` tends to some filter `l` if
* `φ` is a sequence of normed bump functions
  such that `(φ i).rOut` tends to `0` as `i` tends to `l`;
* `g i` is `μ`-a.e. strongly measurable as `i` tends to `l`;
* `g i x` tends to `z₀` as `(i, x)` tends to `l ×ˢ 𝓝 x₀`;
* `k i` tends to `x₀`.

```lean
ContDiffBump.convolution_tendsto_right.{uG, uE', u_1} {G : Type uG} {E' : Type uE'}
  [NormedAddCommGroup E'] [MeasurableSpace G] {μ : MeasureTheory.Measure G} [NormedSpace ℝ E']
  [NormedAddCommGroup G] [NormedSpace ℝ G] [CompleteSpace E'] [BorelSpace G] [FiniteDimensional ℝ G]
  [μ.IsAddHaarMeasure] {ι : Type u_1} {φ : ι → ContDiffBump 0} {g : ι → G → E'} {k : ι → G} {x₀ : G}
  {z₀ : E'} {l : Filter ι} (hφ : Filter.Tendsto (fun i => (φ i).rOut) l (nhds 0))
  (hig : ∀ᶠ (i : ι) in l, MeasureTheory.AEStronglyMeasurable (g i) μ)
  (hcg : Filter.Tendsto (Function.uncurry g) (l ×ˢ nhds x₀) (nhds z₀))
  (hk : Filter.Tendsto k l (nhds x₀)) :
  Filter.Tendsto
    (fun i =>
      MeasureTheory.convolution ((φ i).normed μ) (g i) (ContinuousLinearMap.lsmul ℝ ℝ) μ (k i))
    l (nhds z₀)
```

## Depends on

- [Algebra of endomorphisms of a vector space](../../../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Ball](../../../topology/metric-spaces/ball.md)
- [Borel sigma-algebra](../part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Compactness in terms of filters](../../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Convolution (Measures and integral calculus)](convolution.md)
- [Finite-dimensionality](../../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Inner product space, over $R$ or $C$](../../hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Measurable function](../part-01/measurable-function.md)
- [Product of vector spaces](../../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Radius of convergence](../../../../undergraduate/single-variable-complex-analysis/complex-valued-series/radius-of-convergence.md)
- [Ring structure $\Z$](../../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Proof depends on

- [$C^k$ function](../../differentiability/c-k-function.md)
- [Cauchy-Schwarz inequality](../../hilbert-spaces/cauchy-schwarz-inequality.md)
- [Complementary subspaces](../../../../undergraduate/linear-algebra/fundamentals/complementary-subspaces.md)
- [Completion of an abelian topological group](../../../topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Continuity (Complex-valued series)](../../../../undergraduate/single-variable-complex-analysis/complex-valued-series/continuity.md)
- [Continuity of the sum of a series of functions](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/continuity-of-the-sum-of-a-series-of-functions.md)
- [Derivative of a composition of functions (Analysis)](../../differentiability/derivative-of-a-composition-of-functions.md)
- [Derivative of the inverse of a function (Analysis)](../../differentiability/derivative-of-the-inverse-of-a-function.md)
- [Derivative of the inverse of a function (Single Variable Real Analysis)](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Determinant of endomorphisms](../../../../undergraduate/linear-algebra/multilinearity/determinant-of-endomorphisms.md)
- [Differentiability of the sum of a series of functions](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/differentiability-of-the-sum-of-a-series-of-func.md)
- [Differentials (linear tangent functions)](../../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Dimension theorem for vector spaces](../../../../thousand-plus/algebra/15-linear-and-multilinear-algebra-matrix-theory/dimension-theorem-for-vector-spaces.md)
- [Dominated convergence theorem](../part-01/dominated-convergence-theorem.md)
- [Dual of a normed space](../../normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Dual vector space](../../../linear-algebra/duality/dual-vector-space.md)
- [Extreme value theorem](../../../topology/topological-algebra/extreme-value-theorem.md)
- [Fubini's theorem](fubinis-theorem.md)
- [Gaussian elimination](../../../../undergraduate/linear-algebra/matrices/gaussian-elimination.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Hilbert projection theorem](../../../../undergraduate/topology/hilbert-spaces/hilbert-projection-theorem.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Lebesgue measure (Measures and integral calculus)](../part-01/lebesgue-measure.md)
- [Local convexity](../../topological-vector-spaces/local-convexity.md)
- [M. Riesz extension theorem](../../../../thousand-plus/analysis/46-functional-analysis/part-02/m-riesz-extension-theorem.md)
- [Maximal ideal](../../../general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../../../undergraduate/topology/normed-vector-spaces-on-r-and-c/norms-lvert-cdot-rvert-p-on-r-n-and-c-n.md)
- [Orthogonal projection](../../hilbert-spaces/orthogonal-projection.md)
- [Polynomial derivative](../../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md)
- [Polynomial functions](../../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/polynomial-functions.md)
- [Probability measure](../../../probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Product of finitely many measures](product-of-finitely-many-measures.md)
- [Quotient ring](../../../general-algebra/ideals-and-quotients/quotient-ring.md)
- [Self-adjoint operator](../../hilbert-spaces/self-adjoint-operator.md)
- [Stieltjes measure](../part-01/stieltjes-measure.md)
- [Sum of a Geometric Series](../../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [The Number of Subsets of a Set](../../../../hundred-theorems/part-03/the-number-of-subsets-of-a-set.md)

## Sources

- [Mathlib documentation: `ContDiffBump.convolution_tendsto_right`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/BumpFunction/Convolution.html#ContDiffBump.convolution_tendsto_right)
- [Source of `ContDiffBump.convolution_tendsto_right` in Mathlib/Analysis/Calculus/BumpFunction/Convolution.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/BumpFunction/Convolution.lean#L77)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L360)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L529)
