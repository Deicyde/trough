---
declaration: theorem
origin: cited
lean: TauCeti.integral_inner_gradient_eq_neg_integral_mul_laplacian
statement: formalized
proof: formalized
---

# Green's first identity against a compactly supported function

For a `C²` function `u`
and a compactly supported `C¹` function `v`, `∫ ⟪∇u, ∇v⟫ = -∫ v Δu`. No integrability or decay
of `u` is needed.

```lean
TauCeti.integral_inner_gradient_eq_neg_integral_mul_laplacian.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {u v : E → ℝ}
  (hu : ContDiff ℝ 2 u) (hv : ContDiff ℝ 1 v) (hvc : HasCompactSupport v) :
  ∫ (x : E), inner ℝ (gradient u x) (gradient v x) ∂μ = -∫ (x : E), v x * Laplacian.laplacian u x ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_inner_gradient_eq_neg_integral_mul_laplacian`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Laplacian/Integral.html#TauCeti.integral_inner_gradient_eq_neg_integral_mul_laplacian).

## Sources

- [Tau Ceti documentation: `TauCeti.integral_inner_gradient_eq_neg_integral_mul_laplacian`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Laplacian/Integral.html#TauCeti.integral_inner_gradient_eq_neg_integral_mul_laplacian)
- [Source of `TauCeti.integral_inner_gradient_eq_neg_integral_mul_laplacian` in TauCeti/Analysis/InnerProductSpace/Laplacian/Integral.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/Laplacian/Integral.lean#L56)
