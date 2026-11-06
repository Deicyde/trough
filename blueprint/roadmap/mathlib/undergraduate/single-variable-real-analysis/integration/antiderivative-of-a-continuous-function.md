# Antiderivative of a continuous function

**Fundamental theorem of calculus-1**, derivative in the right endpoint.

If `f : ℝ → E` is continuous, then the derivative of `u ↦ ∫ x in a..u, f x` at `b` is `f b`.

```lean
Continuous.deriv_integral.{u_3} {E : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [CompleteSpace E] (f : ℝ → E) (hf : Continuous f) (a b : ℝ) :
  deriv (fun u => ∫ (x : ℝ) in a..u, f x) b = f b
```

## Depends on

- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Differentials (linear tangent functions)](../../multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Lebesgue measure (Measures and integral calculus)](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)

## Proof depends on

- [Derivative at a point](../differentiability/derivative-at-a-point.md)
- [Fundamental Theorem of Integral Calculus](../../../hundred-theorems/part-01/fundamental-theorem-of-integral-calculus.md)

## Sources

- [Mathlib documentation: `Continuous.deriv_integral`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.html#Continuous.deriv_integral)
- [Source of `Continuous.deriv_integral` in Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean#L661)
- [Mathlib undergraduate list: Single Variable Real Analysis › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L342)
