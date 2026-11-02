---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Complex.isConservativeOn_and_continuousOn_iff_isDifferentiableOn
mathlib_file: Mathlib/Analysis/Complex/HasPrimitives.lean
---

# Morera's theorem

Mathlib states this as `Complex.isConservativeOn_and_continuousOn_iff_isDifferentiableOn`.

```lean
Complex.isConservativeOn_and_continuousOn_iff_isDifferentiableOn.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {f : ℂ → E} [CompleteSpace E] {U : Set ℂ}
  (hU : IsOpen U) : Complex.IsConservativeOn f U ∧ ContinuousOn f U ↔ DifferentiableOn ℂ f U
```

## Depends on

- [Bochner integral](../../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Carathéodory's theorem (measure theory)](../../28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Complex number](../../../../overview/general-algebra/numbers/complex-number.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Lebesgue measure (Measures and integral calculus)](../../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)

## Proof depends on

- [Analyticity of holomorphic functions](../../../../overview/analysis/complex-analysis/analyticity-of-holomorphic-functions.md)
- [Derivative at a point](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Fundamental Theorem of Integral Calculus](../../../../hundred-theorems/part-01/fundamental-theorem-of-integral-calculus.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-05/the-triangle-inequality.md)

## Sources

- [Mathlib documentation: `Complex.isConservativeOn_and_continuousOn_iff_isDifferentiableOn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/HasPrimitives.html#Complex.isConservativeOn_and_continuousOn_iff_isDifferentiableOn)
- [Source of `Complex.isConservativeOn_and_continuousOn_iff_isDifferentiableOn` in Mathlib/Analysis/Complex/HasPrimitives.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/HasPrimitives.lean#L281)
- [1000+ theorems list: Q1140119](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1416)
- [1000+ theorems project: Q1140119](https://1000-plus.github.io/all.html?length=-1#Q1140119)
- [Wikipedia: Morera's theorem](https://en.wikipedia.org/wiki/Morera's_theorem)
- [Wikidata: Q1140119](https://www.wikidata.org/wiki/Q1140119)
