---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: intervalIntegral.integral_eq_sub_of_hasDeriv_right_of_le
mathlib_file: Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean
---

# Fundamental theorem of calculus, part 2

**Fundamental theorem of calculus-2**: If `f : ℝ → E` is continuous on `[a, b]` (where `a ≤ b`)
and has a right derivative at `f' x` for all `x` in `(a, b)`, and `f'` is integrable on `[a, b]`,
then `∫ y in a..b, f' y` equals `f b - f a`.

```lean
intervalIntegral.integral_eq_sub_of_hasDeriv_right_of_le.{u_3} {E : Type u_3} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {a b : ℝ} [CompleteSpace E] {f f' : ℝ → E} (hab : a ≤ b)
  (hcont : ContinuousOn f (Set.Icc a b))
  (hderiv : ∀ x ∈ Set.Ioo a b, HasDerivWithinAt f (f' x) (Set.Ioi x) x)
  (f'int : IntervalIntegrable f' MeasureTheory.volume a b) : ∫ (y : ℝ) in a..b, f' y = f b - f a
```

## Depends on

- [Bochner integral](bochner-integral.md)
- [Lebesgue measure](lebesgue-measure.md)
- [Topological module](../../../topology/topological-algebra/topological-module.md)

## Proof depends on

- [Affine space](../../../geometry/affine-and-euclidean-geometry/affine-space.md)
- [Approximation by step functions](../../../../undergraduate/measures-and-integral-calculus/measure-theory/approximation-by-step-functions.md)
- [Arithmetic Mean/Geometric Mean](../../../../hundred-theorems/part-02/arithmetic-mean-geometric-mean.md)
- [Characteristic p](../../../general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../../topology/general-topology/part-01/closed-map.md)
- [Complementary subspaces](../../../../undergraduate/linear-algebra/fundamentals/complementary-subspaces.md)
- [Differentiable function between normed vector spaces](../../differentiability/differentiable-function-between-normed-vector-sp.md)
- [Dual of a normed space](../../normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Extended real number](../../../general-algebra/numbers/extended-real-number.md)
- [Extreme value theorem](../../../topology/topological-algebra/extreme-value-theorem.md)
- [Fatou's lemma](fatous-lemma.md)
- [Giry monad](giry-monad.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Hilbert projection theorem](../../../../undergraduate/topology/hilbert-spaces/hilbert-projection-theorem.md)
- [Local convexity](../../topological-vector-spaces/local-convexity.md)
- [M. Riesz extension theorem](../../../../thousand-plus/analysis/46-functional-analysis/part-02/m-riesz-extension-theorem.md)
- [Maximal ideal](../../../general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Monotone convergence theorem](monotone-convergence-theorem.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../../../undergraduate/topology/normed-vector-spaces-on-and/norms-p-on-n-and-n.md)
- [Orthogonal projection](../../hilbert-spaces/orthogonal-projection.md)
- [Pointwise convergence](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Probability measure](../../../probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Quotient space](../../../linear-algebra/fundamentals/quotient-space.md)
- [Self-adjoint operator](../../hilbert-spaces/self-adjoint-operator.md)
- [Stieltjes measure](stieltjes-measure.md)

## Sources

- [Mathlib documentation: `intervalIntegral.integral_eq_sub_of_hasDeriv_right_of_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.html#intervalIntegral.integral_eq_sub_of_hasDeriv_right_of_le)
- [Source of `intervalIntegral.integral_eq_sub_of_hasDeriv_right_of_le` in Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean#L1113)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L356)
