---
declaration: theorem
origin: cited
lean: TauCeti.integral_norm_rpow_neg_finrank_mul_fderiv_apply_self
statement: formalized
proof: formalized
---

# Radial fundamental theorem of calculus

For a `C¹` function `f` with compact support on a
nontrivial finite-dimensional real normed space of dimension `d`,
`∫ ‖x‖ ^ (-d) * f' x x ∂μ = -(d * μ (ball 0 1)) * f 0`.

In the language of distributions, `div (x / ‖x‖ ^ d) = d μ(ball 0 1) δ₀`.

```lean
TauCeti.integral_norm_rpow_neg_finrank_mul_fderiv_apply_self.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [Nontrivial E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {f : E → ℝ}
  (hf : ContDiff ℝ 1 f) (hc : HasCompactSupport f) :
  ∫ (x : E), ‖x‖ ^ (-↑(Module.finrank ℝ E)) * (fderiv ℝ f x) x ∂μ =
    -(↑(Module.finrank ℝ E) * μ.real (Metric.ball 0 1)) * f 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_norm_rpow_neg_finrank_mul_fderiv_apply_self`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Constructions/HaarToSphere.html#TauCeti.integral_norm_rpow_neg_finrank_mul_fderiv_apply_self).

## Sources

- [Tau Ceti documentation: `TauCeti.integral_norm_rpow_neg_finrank_mul_fderiv_apply_self`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Constructions/HaarToSphere.html#TauCeti.integral_norm_rpow_neg_finrank_mul_fderiv_apply_self)
- [Source of `TauCeti.integral_norm_rpow_neg_finrank_mul_fderiv_apply_self` in TauCeti/MeasureTheory/Constructions/HaarToSphere.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Constructions/HaarToSphere.lean#L328)
