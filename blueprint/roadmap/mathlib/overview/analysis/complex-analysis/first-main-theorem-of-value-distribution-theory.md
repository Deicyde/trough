# First Main Theorem of Value Distribution Theory

First part of the First Main Theorem, quantitative version: If `f` is meromorphic on the complex
plane, then the difference between the characteristic functions of `f` and `f⁻¹` is bounded by an
explicit constant.

```lean
ValueDistribution.characteristic_sub_characteristic_inv_le {f : ℂ → ℂ} {R : ℝ}
  (hf : Meromorphic f) :
  |ValueDistribution.characteristic f ⊤ R - ValueDistribution.characteristic f⁻¹ ⊤ R| ≤
    max |Real.log ‖f 0‖| |Real.log ‖meromorphicTrailingCoeffAt f 0‖|
```

## Depends on

- [Analytic function](../differentiability/analytic-function.md)
- [Bochner integral](../measures-and-integral-calculus/part-01/bochner-integral.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Compactness in terms of filters](../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Lebesgue measure (Measures and integral calculus)](../measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Logarithm](../special-functions/logarithm.md)

## Proof depends on

- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)

## Sources

- [Mathlib documentation: `ValueDistribution.characteristic_sub_characteristic_inv_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/ValueDistribution/FirstMainTheorem.html#ValueDistribution.characteristic_sub_characteristic_inv_le)
- [Source of `ValueDistribution.characteristic_sub_characteristic_inv_le` in Mathlib/Analysis/Complex/ValueDistribution/FirstMainTheorem.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/ValueDistribution/FirstMainTheorem.lean#L92)
- [Mathlib overview: Analysis › Complex analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L376)
