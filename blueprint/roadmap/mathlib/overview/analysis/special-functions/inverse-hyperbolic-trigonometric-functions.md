# Inverse hyperbolic trigonometric functions

`arsinh` is defined using a logarithm, `arsinh x = log (x + √(1 + x^2))`.

```lean
Real.arsinh (x : ℝ) : ℝ
```

## Depends on

- [Logarithm](logarithm.md)

## Sources

- [Mathlib documentation: `Real.arsinh`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Arsinh.html#Real.arsinh)
- [Source of `Real.arsinh` in Mathlib/Analysis/SpecialFunctions/Arsinh.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Analysis/SpecialFunctions/Arsinh.lean#L52)
- [Mathlib overview: Analysis › Special functions](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L334)
- [Mathlib undergraduate list: Single Variable Real Analysis › Elementary functions (trigonometric, rational, $\exp$, $\log$, etc)](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L338)
