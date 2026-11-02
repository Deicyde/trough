---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Complex.two_pi_I_inv_smul_circleIntegral_sub_inv_smul_of_differentiable_on_off_countable
mathlib_file: Mathlib/Analysis/Complex/CauchyIntegral.lean
---

# Cauchy formulas

**Cauchy integral formula**: if `f : ℂ → E` is continuous on a closed disc of radius `R` and is
complex differentiable at all but countably many points of its interior, then for any `w` in this
interior we have $\frac{1}{2πi}\oint_{|z-c|=R}(z-w)^{-1}f(z)\,dz=f(w)$.

```lean
Complex.two_pi_I_inv_smul_circleIntegral_sub_inv_smul_of_differentiable_on_off_countable.{u}
  {E : Type u} [NormedAddCommGroup E] [NormedSpace ℂ E] [CompleteSpace E] {R : ℝ} {c w : ℂ}
  {f : ℂ → E} {s : Set ℂ} (hs : s.Countable) (hw : w ∈ Metric.ball c R)
  (hc : ContinuousOn f (Metric.closedBall c R))
  (hd : ∀ x ∈ Metric.ball c R \ s, DifferentiableAt ℂ f x) :
  (2 * ↑Real.pi * Complex.I)⁻¹ • ∮ (z : ℂ) in C(c, R), (z - w)⁻¹ • f z = f w
```

## Depends on

- [Ball](../../../overview/topology/metric-spaces/ball.md)
- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Differentiable function between normed vector spaces](../../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Differentials (linear tangent functions)](../../multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Field $\C$ of complex numbers](../../ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Lebesgue measure](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)

## Proof depends on

- [$C^k$ function](../../../overview/analysis/differentiability/c-k-function.md)
- [Absolutely convergent series in Banach spaces](../../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Affine function](../../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Completion of an abelian topological group](../../../overview/topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Continuity](../complex-valued-series/continuity.md)
- [Decomposition into transpositions](../../group-theory/permutation-group/decomposition-into-transpositions.md)
- [Derivative at a point](../../single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Derivative of a composition of functions](../../../overview/analysis/differentiability/derivative-of-a-composition-of-functions.md)
- [Derivative of the inverse of a function](../../single-variable-real-analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Determinant of endomorphisms](../../linear-algebra/multilinearity/determinant-of-endomorphisms.md)
- [Determinant of vectors](../../linear-algebra/multilinearity/determinant-of-vectors.md)
- [Differentiable functions](../../multivariable-calculus/differential-calculus/differentiable-functions.md)
- [Dimension theorem for vector spaces](../../../thousand-plus/algebra/15-linear-and-multilinear-algebra-matrix-theory/dimension-theorem-for-vector-spaces.md)
- [Divergence theorem](../../../overview/analysis/measures-and-integral-calculus/part-02/divergence-theorem.md)
- [Euclidean affine space](../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Fubini's theorem](../../../overview/analysis/measures-and-integral-calculus/part-02/fubinis-theorem.md)
- [Fundamental Theorem of Integral Calculus](../../../hundred-theorems/part-01/fundamental-theorem-of-integral-calculus.md)
- [Gaussian elimination](../../linear-algebra/matrices/gaussian-elimination.md)
- [Holomorphic functions](holomorphic-functions.md)
- [Invertibility](../../../overview/linear-algebra/matrices/invertibility.md)
- [Matrix exponential](../../linear-algebra/exponential/matrix-exponential.md)
- [Orientation of a $\R$-vector space](../../linear-algebra/multilinearity/orientation-of-a-vector-space.md)
- [Quotient ring](../../../overview/general-algebra/ideals-and-quotients/quotient-ring.md)
- [Sequential space](../../../overview/topology/general-topology/part-01/sequential-space.md)
- [Sum of a Geometric Series](../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [Unitary group](../../group-theory/classical-automorphism-groups/unitary-group.md)

## Sources

- [Mathlib documentation: `Complex.two_pi_I_inv_smul_circleIntegral_sub_inv_smul_of_differentiable_on_off_countable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/CauchyIntegral.html#Complex.two_pi_I_inv_smul_circleIntegral_sub_inv_smul_of_differentiable_on_off_countable)
- [Source of `Complex.two_pi_I_inv_smul_circleIntegral_sub_inv_smul_of_differentiable_on_off_countable` in Mathlib/Analysis/Complex/CauchyIntegral.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/CauchyIntegral.lean#L512)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Functions on one complex variable](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L390)
