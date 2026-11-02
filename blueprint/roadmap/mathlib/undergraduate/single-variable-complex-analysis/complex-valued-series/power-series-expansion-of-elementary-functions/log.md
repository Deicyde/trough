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

- [Field $\C$ of complex numbers](../../../ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Infinite sum](../../../../overview/topology/topological-algebra/infinite-sum.md)
- [Inverse trigonometric functions](../../../../overview/analysis/special-functions/inverse-trigonometric-functions.md)
- [Logarithm](../../../../overview/analysis/special-functions/logarithm.md)
- [Metric space](../../../../overview/topology/metric-spaces/metric-space.md)

## Proof depends on

- [$C^k$ function](../../../../overview/analysis/differentiability/c-k-function.md)
- [Absolutely convergent series in Banach spaces](../../../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Affine function](../../../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Completion of an abelian topological group](../../../../overview/topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Derivative at a point](../../../single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Derivative of the inverse of a function](../../../single-variable-real-analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Differentials (linear tangent functions)](../../../multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Euclidean affine space](../../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Fundamental Theorem of Integral Calculus](../../../../hundred-theorems/part-01/fundamental-theorem-of-integral-calculus.md)
- [Holomorphic functions](../../functions-on-one-complex-variable/holomorphic-functions.md)
- [Matrix exponential](../../../linear-algebra/exponential/matrix-exponential.md)
- [Sequential space](../../../../overview/topology/general-topology/part-01/sequential-space.md)
- [Sum of a Geometric Series](../../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [The Number of Subsets of a Set](../../../../hundred-theorems/part-03/the-number-of-subsets-of-a-set.md)

## Sources

- [Mathlib documentation: `Complex.hasSum_taylorSeries_log`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Complex/LogBounds.html#Complex.hasSum_taylorSeries_log)
- [Source of `Complex.hasSum_taylorSeries_log` in Mathlib/Analysis/SpecialFunctions/Complex/LogBounds.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/SpecialFunctions/Complex/LogBounds.lean#L245)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Complex-valued series › power series expansion of elementary functions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L381)
