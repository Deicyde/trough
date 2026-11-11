---
declaration: theorem
origin: cited
lean: TauCeti.sq_integral_mul_le_integral_sq_mul_integral_sq, TauCeti.integral_le_sqrt_mul_sqrt_integral_sq
statement: formalized
proof: formalized
---

# The Cauchy–Schwarz inequality

**The Cauchy–Schwarz inequality** `(∫ f g)² ≤ (∫ f²) (∫ g²)` for square-integrable real
functions.

```lean
TauCeti.sq_integral_mul_le_integral_sq_mul_integral_sq.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ : MeasureTheory.Measure α} {f g : α → ℝ} (hf : MeasureTheory.MemLp f 2 μ)
  (hg : MeasureTheory.MemLp g 2 μ) :
  (∫ (x : α), f x * g x ∂μ) ^ 2 ≤ (∫ (x : α), f x ^ 2 ∂μ) * ∫ (x : α), g x ^ 2 ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sq_integral_mul_le_integral_sq_mul_integral_sq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Bochner/CauchySchwarz.html#TauCeti.sq_integral_mul_le_integral_sq_mul_integral_sq).

## Other forms

**The Cauchy–Schwarz inequality on an interval.** Formalized in Tau Ceti as [`TauCeti.integral_le_sqrt_mul_sqrt_integral_sq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/IntervalIntegral/CauchySchwarz.html#TauCeti.integral_le_sqrt_mul_sqrt_integral_sq).

```lean
TauCeti.integral_le_sqrt_mul_sqrt_integral_sq {g : ℝ → ℝ} {a b : ℝ} (hab : a ≤ b)
  (hg2 : IntervalIntegrable (fun t => g t ^ 2) MeasureTheory.volume a b) :
  ∫ (t : ℝ) in a..b, g t ≤ √(b - a) * √(∫ (t : ℝ) in a..b, g t ^ 2)
```

## Sources

- [Tau Ceti documentation: `TauCeti.sq_integral_mul_le_integral_sq_mul_integral_sq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Bochner/CauchySchwarz.html#TauCeti.sq_integral_mul_le_integral_sq_mul_integral_sq)
- [Source of `TauCeti.sq_integral_mul_le_integral_sq_mul_integral_sq` in TauCeti/MeasureTheory/Integral/Bochner/CauchySchwarz.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/Bochner/CauchySchwarz.lean#L31)
