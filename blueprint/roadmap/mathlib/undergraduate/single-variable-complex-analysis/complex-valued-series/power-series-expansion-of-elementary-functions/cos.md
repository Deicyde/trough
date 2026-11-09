# Cos (power series expansion of elementary functions)

The power series expansion of `Complex.cos`.

```lean
Complex.hasSum_cos (z : ℂ) :
  HasSum (fun n => (-1) ^ n * z ^ (2 * n) / ↑(2 * n).factorial) (Complex.cos z)
```

## Depends on

- [Cos (extension of trigonometric functions to the complex plane)](../extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Infinite sum](../../../../overview/topology/topological-algebra/infinite-sum.md)
- [Metric space](../../../../overview/topology/metric-spaces/metric-space.md)

## Proof depends on

- [Characteristic zero](../../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Completeness of R](../../../single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Field $\C$ of complex numbers](../../../ring-theory/field-theory/field-c-of-complex-numbers.md)
- [Matrix exponential](../../../linear-algebra/exponential/matrix-exponential.md)

## Sources

- [Mathlib documentation: `Complex.hasSum_cos`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Trigonometric/Series.html#Complex.hasSum_cos)
- [Source of `Complex.hasSum_cos` in Mathlib/Analysis/SpecialFunctions/Trigonometric/Series.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/SpecialFunctions/Trigonometric/Series.lean#L70)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Complex-valued series › power series expansion of elementary functions](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L379)
