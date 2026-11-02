---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: DiffContOnCl.circleIntegral_sub_inv_smul
mathlib_file: Mathlib/Analysis/Complex/CauchyIntegral.lean
---

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
- [Differentials (linear tangent functions)](../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Field $\C$ of complex numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Holomorphic functions](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Lebesgue measure](../measures-and-integral-calculus/part-01/lebesgue-measure.md)

## Proof depends on

- [Cauchy formulas](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/cauchy-formulas.md)

## Sources

- [Mathlib documentation: `DiffContOnCl.circleIntegral_sub_inv_smul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/CauchyIntegral.html#DiffContOnCl.circleIntegral_sub_inv_smul)
- [Source of `DiffContOnCl.circleIntegral_sub_inv_smul` in Mathlib/Analysis/Complex/CauchyIntegral.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/CauchyIntegral.lean#L560)
- [Mathlib overview: Analysis › Complex analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L366)
