# Inverse hyperbolic trigonometric functions

`arsinh` is defined using a logarithm, `arsinh x = log (x + √(1 + x^2))`.

```lean
Real.arsinh (x : ℝ) : ℝ
```

## Depends on

- [Logarithm](logarithm.md)

## Sources

- [Mathlib documentation: `Real.arsinh`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Arsinh.html#Real.arsinh)
- [Source of `Real.arsinh` in Mathlib/Analysis/SpecialFunctions/Arsinh.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/SpecialFunctions/Arsinh.lean#L52)
- [Mathlib overview: Analysis › Special functions](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L334)
- [Mathlib undergraduate list: Single Variable Real Analysis › Elementary functions (trigonometric, rational, $\exp$, $\log$, etc)](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L338)
