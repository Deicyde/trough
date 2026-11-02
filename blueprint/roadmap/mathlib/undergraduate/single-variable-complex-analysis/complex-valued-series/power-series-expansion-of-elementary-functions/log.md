---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Complex.hasSum_taylorSeries_log
mathlib_file: Mathlib/Analysis/SpecialFunctions/Complex/LogBounds.lean
---

# Log

The Taylor series of the complex logarithm at `1` converges to the logarithm in the
open unit disk.

```lean
Complex.hasSum_taylorSeries_log {z : ℂ} (hz : ‖z‖ < 1) :
  HasSum (fun n => (-1) ^ (n + 1) * z ^ n / ↑n) (Complex.log (1 + z))
```

## Depends on

- [Field $\C$ of complex numbers](../../../ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Infinite sum](../../../../overview/topology/topological-algebra/infinite-sum.md)
- [Inverse trigonometric functions](../../../../overview/analysis/special-functions/inverse-trigonometric-functions.md)
- [Logarithm](../../../../overview/analysis/special-functions/logarithm.md)
- [Metric space](../../../../overview/topology/metric-spaces/metric-space.md)

## Proof depends on

- [Bochner integral](../../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Characteristic p](../../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Derivative at a point](../../../single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Lebesgue measure (Measures and integral calculus)](../../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Topological ring](../../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `Complex.hasSum_taylorSeries_log`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Complex/LogBounds.html#Complex.hasSum_taylorSeries_log)
- [Source of `Complex.hasSum_taylorSeries_log` in Mathlib/Analysis/SpecialFunctions/Complex/LogBounds.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/SpecialFunctions/Complex/LogBounds.lean#L245)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Complex-valued series › power series expansion of elementary functions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L381)
