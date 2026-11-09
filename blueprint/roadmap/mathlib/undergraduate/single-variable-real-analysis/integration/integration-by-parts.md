# Integration by parts

**Integration by parts**. Special case of
`intervalIntegrable.integral_mul_deriv_eq_deriv_mul_of_hasDeriv_right`
where the functions have a derivative also at the endpoints.
For improper integrals, see
`MeasureTheory.integral_mul_deriv_eq_deriv_mul`,
`MeasureTheory.integral_Ioi_mul_deriv_eq_deriv_mul`,
and `MeasureTheory.integral_Iic_mul_deriv_eq_deriv_mul`.

```lean
intervalIntegral.integral_mul_deriv_eq_deriv_mul.{u_1} {a b : ℝ} {A : Type u_1} [NormedRing A]
  [NormedAlgebra ℝ A] [CompleteSpace A] {u v u' v' : ℝ → A}
  (hu : ∀ x ∈ Set.uIcc a b, HasDerivAt u (u' x) x) (hv : ∀ x ∈ Set.uIcc a b, HasDerivAt v (v' x) x)
  (hu' : IntervalIntegrable u' MeasureTheory.volume a b)
  (hv' : IntervalIntegrable v' MeasureTheory.volume a b) :
  ∫ (x : ℝ) in a..b, u x * v' x = u b * v b - u a * v a - ∫ (x : ℝ) in a..b, u' x * v x
```

## Depends on

- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Derivative at a point](../differentiability/derivative-at-a-point.md)
- [Lebesgue measure (Measures and integral calculus)](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)

## Proof depends on

- [Fundamental theorem of calculus, part 2](../../../overview/analysis/measures-and-integral-calculus/part-01/fundamental-theorem-of-calculus-part-2.md)

## Sources

- [Mathlib documentation: `intervalIntegral.integral_mul_deriv_eq_deriv_mul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/IntervalIntegral/IntegrationByParts.html#intervalIntegral.integral_mul_deriv_eq_deriv_mul)
- [Source of `intervalIntegral.integral_mul_deriv_eq_deriv_mul` in Mathlib/MeasureTheory/Integral/IntervalIntegral/IntegrationByParts.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/MeasureTheory/Integral/IntervalIntegral/IntegrationByParts.lean#L134)
- [Mathlib undergraduate list: Single Variable Real Analysis › Integration](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L344)
