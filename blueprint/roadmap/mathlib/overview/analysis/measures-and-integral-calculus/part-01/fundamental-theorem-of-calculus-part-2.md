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
- [Carathéodory's theorem (measure theory)](../../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Lebesgue measure (Measures and integral calculus)](lebesgue-measure.md)
- [Topological module](../../../topology/topological-algebra/topological-module.md)

## Proof depends on

- [Affine space](../../../geometry/affine-and-euclidean-geometry/affine-space.md)
- [Compactness in terms of filters](../../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Differentiable function between normed vector spaces](../../differentiability/differentiable-function-between-normed-vector-sp.md)
- [Dual of a normed space](../../normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Extended real number](../../../general-algebra/numbers/extended-real-number.md)
- [Local convexity](../../topological-vector-spaces/local-convexity.md)
- [Measurable function](measurable-function.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Order topology](../../../topology/topological-algebra/order-topology.md)
- [Topological ring](../../../topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `intervalIntegral.integral_eq_sub_of_hasDeriv_right_of_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.html#intervalIntegral.integral_eq_sub_of_hasDeriv_right_of_le)
- [Source of `intervalIntegral.integral_eq_sub_of_hasDeriv_right_of_le` in Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean#L1113)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L356)
