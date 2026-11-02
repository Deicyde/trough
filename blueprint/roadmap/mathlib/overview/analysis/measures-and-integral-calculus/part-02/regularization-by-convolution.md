---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: HasCompactSupport.contDiff_convolution_left
mathlib_file: Mathlib/Analysis/Calculus/ContDiff/Convolution.lean
---

# Regularization by convolution

Mathlib states this as `HasCompactSupport.contDiff_convolution_left`.

```lean
HasCompactSupport.contDiff_convolution_left.{u𝕜, uG, uE, uE', uF} {𝕜 : Type u𝕜} {G : Type uG}
  {E : Type uE} {E' : Type uE'} {F : Type uF} [NormedAddCommGroup E] [NormedAddCommGroup E']
  [NormedAddCommGroup F] {f : G → E} {g : G → E'} [RCLike 𝕜] [NormedSpace 𝕜 E] [NormedSpace 𝕜 E']
  [NormedSpace ℝ F] [NormedSpace 𝕜 F] [MeasurableSpace G] [NormedAddCommGroup G] [BorelSpace G]
  [NormedSpace 𝕜 G] {μ : MeasureTheory.Measure G} (L : E →L[𝕜] E' →L[𝕜] F) [μ.IsAddLeftInvariant]
  [μ.IsNegInvariant] {n : ℕ∞} (hcf : HasCompactSupport f) (hf : ContDiff 𝕜 (↑n) f)
  (hg : MeasureTheory.LocallyIntegrable g μ) : ContDiff 𝕜 (↑n) (MeasureTheory.convolution f g L μ)
```

## Depends on

- [$C^k$ function](../../differentiability/c-k-function.md)
- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Borel sigma-algebra](../part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Compactness in terms of filters](../../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Convolution](convolution.md)
- [Measurable function](../part-01/measurable-function.md)

## Proof depends on

- [Absolutely convergent series in Banach spaces](../../normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Affine function](../../../geometry/affine-and-euclidean-geometry/affine-function.md)
- [Aleph numbers](../../../logic-and-computation/set-theory/cardinals/aleph-numbers.md)
- [Approximation by step functions](../../../../undergraduate/measures-and-integral-calculus/measure-theory/approximation-by-step-functions.md)
- [Arithmetic Mean/Geometric Mean](../../../../hundred-theorems/part-02/arithmetic-mean-geometric-mean.md)
- [Characteristic p](../../../general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../../topology/general-topology/part-01/closed-map.md)
- [Completion of an abelian topological group](../../../topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Derivative at a point](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Derivative of a composition of functions](../../differentiability/derivative-of-a-composition-of-functions.md)
- [Differentials (linear tangent functions)](../../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Dual of a normed space](../../normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Dual vector space](../../../linear-algebra/duality/dual-vector-space.md)
- [Euclidean affine space](../../../geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Existence of bases](../../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Extreme value theorem](../../../topology/topological-algebra/extreme-value-theorem.md)
- [Fatou's lemma](../part-01/fatous-lemma.md)
- [Finite product of metric spaces](../../../../undergraduate/topology/topology-and-metric-spaces/finite-product-of-metric-spaces.md)
- [Finite-dimensionality](../../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Fundamental sequences](../../../logic-and-computation/set-theory/ordinals/fundamental-sequences.md)
- [Hilbert basis theorem](../../../general-algebra/polynomials-and-power-series/hilbert-basis-theorem.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Inner product space, over $R$ or $C$](../../hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Isomorphism with $K^n$](../../../linear-algebra/finite-dimensional-vector-spaces/isomorphism-with-k-n.md)
- [Limits of sequences](../../../../undergraduate/topology/topology-and-metric-spaces/limits-of-sequences.md)
- [Local convexity](../../topological-vector-spaces/local-convexity.md)
- [Local ring](../../../general-algebra/rings/local-ring.md)
- [M. Riesz extension theorem](../../../../thousand-plus/analysis/46-functional-analysis/part-02/m-riesz-extension-theorem.md)
- [Maximal ideal](../../../general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Monotone convergence theorem](../part-01/monotone-convergence-theorem.md)
- [Pointwise convergence](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Polynomial in several indeterminates](../../../general-algebra/polynomials-and-power-series/polynomial-in-several-indeterminates.md)
- [Quotient space](../../../linear-algebra/fundamentals/quotient-space.md)
- [Sequential space](../../../topology/general-topology/part-01/sequential-space.md)
- [Subring](../../../general-algebra/rings/subring.md)
- [Sum of a Geometric Series](../../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [The Fundamental Theorem of Arithmetic](../../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)
- [The Number of Subsets of a Set](../../../../hundred-theorems/part-03/the-number-of-subsets-of-a-set.md)
- [Well-ordering theorem](../../../../thousand-plus/general-topics-history-and-foundations/03-mathematical-logic-and-foundations/part-03/well-ordering-theorem.md)

## Sources

- [Mathlib documentation: `HasCompactSupport.contDiff_convolution_left`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/ContDiff/Convolution.html#HasCompactSupport.contDiff_convolution_left)
- [Source of `HasCompactSupport.contDiff_convolution_left` in Mathlib/Analysis/Calculus/ContDiff/Convolution.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/ContDiff/Convolution.lean#L428)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L361)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L530)
