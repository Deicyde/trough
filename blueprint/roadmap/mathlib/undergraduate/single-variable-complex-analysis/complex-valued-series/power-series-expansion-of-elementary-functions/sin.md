---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Complex.hasSum_sin
mathlib_file: Mathlib/Analysis/SpecialFunctions/Trigonometric/Series.lean
---

# Sin (power series expansion of elementary functions)

The power series expansion of `Complex.sin`.

```lean
Complex.hasSum_sin (z : ℂ) :
  HasSum (fun n => (-1) ^ n * z ^ (2 * n + 1) / ↑(2 * n + 1).factorial) (Complex.sin z)
```

## Depends on

- [Infinite sum](../../../../overview/topology/topological-algebra/infinite-sum.md)
- [Metric space](../../../../overview/topology/metric-spaces/metric-space.md)
- [Sin (extension of trigonometric functions to the complex plane)](../extension-of-trigonometric-functions-to-the-comp/sin.md)

## Proof depends on

- [Characteristic zero](../../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Completeness of R](../../../single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Field $\C$ of complex numbers](../../../ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Matrix exponential](../../../linear-algebra/exponential/matrix-exponential.md)

## Sources

- [Mathlib documentation: `Complex.hasSum_sin`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Trigonometric/Series.html#Complex.hasSum_sin)
- [Source of `Complex.hasSum_sin` in Mathlib/Analysis/SpecialFunctions/Trigonometric/Series.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/SpecialFunctions/Trigonometric/Series.lean#L76)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Complex-valued series › power series expansion of elementary functions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L380)
