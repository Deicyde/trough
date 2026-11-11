---
declaration: theorem
origin: cited
lean: SchwartzMap.integral_bilinear_laplacian_right_eq_neg_sum
statement: formalized
proof: formalized
---

# Green's identity on Schwartz space

for a continuous bilinear map `B` and an orthonormal
basis `b`, `∫ B(f, Δg) = -∑ᵢ ∫ B(∂_{bᵢ} f, ∂_{bᵢ} g)`.

```lean
SchwartzMap.integral_bilinear_laplacian_right_eq_neg_sum.{u_3, u_4, u_5, u_6, u_7} {E : Type u_3}
  {F₁ : Type u_4} {F₂ : Type u_5} {F₃ : Type u_6} {ι : Type u_7} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] [NormedAddCommGroup F₁] [NormedSpace ℝ F₁]
  [NormedAddCommGroup F₂] [NormedSpace ℝ F₂] [NormedAddCommGroup F₃] [NormedSpace ℝ F₃] [Fintype ι]
  (b : OrthonormalBasis ι ℝ E) (f : SchwartzMap E F₁) (g : SchwartzMap E F₂)
  (B : F₁ →L[ℝ] F₂ →L[ℝ] F₃) :
  ∫ (x : E), (B (f x)) ((Laplacian.laplacian g) x) ∂μ =
    -∑ i, ∫ (x : E), (B ((LineDeriv.lineDerivOp (b i) f) x)) ((LineDeriv.lineDerivOp (b i) g) x) ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SchwartzMap.integral_bilinear_laplacian_right_eq_neg_sum`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/SchwartzSpace/Deriv.html#SchwartzMap.integral_bilinear_laplacian_right_eq_neg_sum).

## Sources

- [Tau Ceti documentation: `SchwartzMap.integral_bilinear_laplacian_right_eq_neg_sum`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/SchwartzSpace/Deriv.html#SchwartzMap.integral_bilinear_laplacian_right_eq_neg_sum)
- [Source of `SchwartzMap.integral_bilinear_laplacian_right_eq_neg_sum` in TauCeti/Analysis/Distribution/SchwartzSpace/Deriv.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/SchwartzSpace/Deriv.lean#L142)
