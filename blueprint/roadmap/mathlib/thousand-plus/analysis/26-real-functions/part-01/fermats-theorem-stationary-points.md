---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: IsLocalExtr.deriv_eq_zero, IsLocalExtr.fderiv_eq_zero
mathlib_file: Mathlib/Analysis/Calculus/LocalExtr/Basic.lean
---

# Fermat's theorem (stationary points)

Mathlib records this with 2 declarations.

`IsLocalExtr.deriv_eq_zero`: **Fermat's Theorem**: the derivative of a function at a local extremum equals zero.

```lean
IsLocalExtr.deriv_eq_zero {f : ℝ → ℝ} {a : ℝ} (h : IsLocalExtr f a) : deriv f a = 0
```

`IsLocalExtr.fderiv_eq_zero`: **Fermat's Theorem**: the derivative of a function at a local extremum equals zero.

```lean
IsLocalExtr.fderiv_eq_zero.{u} {E : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] {f : E → ℝ}
  {a : E} (h : IsLocalExtr f a) : fderiv ℝ f a = 0
```

## Depends on

- [Differentials (linear tangent functions)](../../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Field $\R$ of real numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Derivative at a point](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Local extrema](../../../../overview/analysis/differentiability/local-extrema.md)

## Sources

- [Mathlib documentation: `IsLocalExtr.deriv_eq_zero`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/LocalExtr/Basic.html#IsLocalExtr.deriv_eq_zero)
- [Source of `IsLocalExtr.deriv_eq_zero` in Mathlib/Analysis/Calculus/LocalExtr/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/LocalExtr/Basic.lean#L260)
- [Mathlib documentation: `IsLocalExtr.fderiv_eq_zero`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/LocalExtr/Basic.html#IsLocalExtr.fderiv_eq_zero)
- [Source of `IsLocalExtr.fderiv_eq_zero` in Mathlib/Analysis/Calculus/LocalExtr/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/LocalExtr/Basic.lean#L200)
- [1000+ theorems list: Q727102](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L789)
- [1000+ theorems project: Q727102](https://1000-plus.github.io/?length=-1#Q727102)
- [Wikipedia: Fermat's theorem (stationary points)](https://en.wikipedia.org/wiki/Fermat's_theorem_%28stationary_points%29)
- [Wikidata: Q727102](https://www.wikidata.org/wiki/Q727102)
