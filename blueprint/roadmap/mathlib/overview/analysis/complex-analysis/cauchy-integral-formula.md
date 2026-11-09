# Cauchy integral formula

**Cauchy integral formula**: if `f : ℂ → E` is complex differentiable on an open disc and is
continuous on its closure, then for any `w` in this open ball we have
$\oint_{|z-c|=R}(z-w)^{-1}f(z)\,dz=2πif(w)$.

```lean
DiffContOnCl.circleIntegral_sub_inv_smul.{u} {E : Type u} [NormedAddCommGroup E] [NormedSpace ℂ E]
  [CompleteSpace E] {R : ℝ} {c w : ℂ} {f : ℂ → E} (h : DiffContOnCl ℂ f (Metric.ball c R))
  (hw : w ∈ Metric.ball c R) :
  ∮ (z : ℂ) in C(c, R), (z - w)⁻¹ • f z = (2 * ↑Real.pi * Complex.I) • f w
```

## Depends on

- [Ball](../../topology/metric-spaces/ball.md)
- [Bochner integral](../measures-and-integral-calculus/part-01/bochner-integral.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Differentials (linear tangent functions)](../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Holomorphic functions](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Lebesgue measure (Measures and integral calculus)](../measures-and-integral-calculus/part-01/lebesgue-measure.md)

## Proof depends on

- [Cauchy formulas](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/cauchy-formulas.md)

## Sources

- [Mathlib documentation: `DiffContOnCl.circleIntegral_sub_inv_smul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/CauchyIntegral.html#DiffContOnCl.circleIntegral_sub_inv_smul)
- [Source of `DiffContOnCl.circleIntegral_sub_inv_smul` in Mathlib/Analysis/Complex/CauchyIntegral.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Complex/CauchyIntegral.lean#L560)
- [Mathlib overview: Analysis › Complex analysis](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L366)
