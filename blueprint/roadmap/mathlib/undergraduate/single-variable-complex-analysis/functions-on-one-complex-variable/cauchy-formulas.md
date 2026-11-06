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
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Cos (extension of trigonometric functions to the complex plane)](../complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Differentiable function between normed vector spaces](../../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Differentials (linear tangent functions)](../../multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Lebesgue measure (Measures and integral calculus)](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)

## Proof depends on

- [Affine space](../../../overview/geometry/affine-and-euclidean-geometry/affine-space.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Completeness of R](../../single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Continuity (Complex-valued series)](../complex-valued-series/continuity.md)
- [Derivative of a composition of functions (Analysis)](../../../overview/analysis/differentiability/derivative-of-a-composition-of-functions.md)
- [Differentiable functions](../../multivariable-calculus/differential-calculus/differentiable-functions.md)
- [Divergence theorem](../../../overview/analysis/measures-and-integral-calculus/part-02/divergence-theorem.md)
- [Euclidean domain](../../../overview/general-algebra/divisibility-in-integral-domains/euclidean-domain.md)
- [Field $\C$ of complex numbers](../../ring-theory/field-theory/field-c-of-complex-numbers.md)
- [Homeomorphisms](../../topology/topology-and-metric-spaces/homeomorphisms.md)
- [Logarithm](../../../overview/analysis/special-functions/logarithm.md)
- [Product of vector spaces](../../linear-algebra/fundamentals/product-of-vector-spaces.md)
- [The Binomial Theorem](../../../hundred-theorems/part-02/the-binomial-theorem.md)

## Sources

- [Mathlib documentation: `Complex.two_pi_I_inv_smul_circleIntegral_sub_inv_smul_of_differentiable_on_off_countable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/CauchyIntegral.html#Complex.two_pi_I_inv_smul_circleIntegral_sub_inv_smul_of_differentiable_on_off_countable)
- [Source of `Complex.two_pi_I_inv_smul_circleIntegral_sub_inv_smul_of_differentiable_on_off_countable` in Mathlib/Analysis/Complex/CauchyIntegral.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/CauchyIntegral.lean#L512)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Functions on one complex variable](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L390)
