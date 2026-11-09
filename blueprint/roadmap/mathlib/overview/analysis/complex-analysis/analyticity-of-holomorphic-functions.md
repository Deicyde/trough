# Analyticity of holomorphic functions

If `f : ℂ → E` is complex differentiable on some set `s`, then it is analytic at any point `z`
such that `s ∈ 𝓝 z` (equivalently, `z ∈ interior s`).

```lean
DifferentiableOn.analyticAt.{u} {E : Type u} [NormedAddCommGroup E] [NormedSpace ℂ E]
  [CompleteSpace E] {s : Set ℂ} {f : ℂ → E} {z : ℂ} (hd : DifferentiableOn ℂ f s)
  (hz : s ∈ nhds z) : AnalyticAt ℂ f z
```

## Depends on

- [Analytic function](../differentiability/analytic-function.md)
- [Complex number](../../general-algebra/numbers/complex-number.md)
- [Holomorphic functions](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Inner product space, over $R$ or $C$](../hilbert-spaces/inner-product-space-over-r-or-c.md)

## Proof depends on

- [Cauchy formulas](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/cauchy-formulas.md)

## Sources

- [Mathlib documentation: `DifferentiableOn.analyticAt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/CauchyIntegral.html#DifferentiableOn.analyticAt)
- [Source of `DifferentiableOn.analyticAt` in Mathlib/Analysis/Complex/CauchyIntegral.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Complex/CauchyIntegral.lean#L721)
- [Mathlib overview: Analysis › Complex analysis](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L371)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Functions on one complex variable](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L391)
