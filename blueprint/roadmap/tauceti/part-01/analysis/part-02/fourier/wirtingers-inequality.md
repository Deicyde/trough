---
declaration: theorem
origin: cited
lean: TauCeti.integral_norm_sub_average_sq_le, TauCeti.mul_integral_norm_sq_le_integral_norm_sq_of_eq_exp_mul
statement: formalized
proof: formalized
---

# Wirtinger's inequality

An absolutely continuous function on `[a, b]` with `f a = f b`,
valued in a finite-dimensional real inner product space and with square-integrable
almost-everywhere derivative, deviates from its mean in `L²` by at most `(b - a) / (2π)` times
the `L²` norm of its derivative.

```lean
TauCeti.integral_norm_sub_average_sq_le.{u_1} {a b : ℝ} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] {f f' : ℝ → V} (hab : a < b)
  (hf : AbsolutelyContinuousOnInterval f a b)
  (hff' : ∀ᵐ (t : ℝ), t ∈ Set.uIoc a b → HasDerivAt f (f' t) t) (hfab : f a = f b)
  (hf' : MeasureTheory.MemLp f' 2 (MeasureTheory.volume.restrict (Set.Ioc a b))) :
  ∫ (x : ℝ) in a..b, ‖f x - ⨍ (y : ℝ) in a..b, f y‖ ^ 2 ≤
    ((b - a) / (2 * Real.pi)) ^ 2 * ∫ (x : ℝ) in a..b, ‖f' x‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Parseval's energy identity](parsevals-energy-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_norm_sub_average_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Wirtinger.html#TauCeti.integral_norm_sub_average_sq_le).

## Other forms

**Wirtinger's inequality for twisted periodic functions.** Formalized in Tau Ceti as [`TauCeti.mul_integral_norm_sq_le_integral_norm_sq_of_eq_exp_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/TwistedWirtinger.html#TauCeti.mul_integral_norm_sq_le_integral_norm_sq_of_eq_exp_mul).

```lean
TauCeti.mul_integral_norm_sq_le_integral_norm_sq_of_eq_exp_mul {a b : ℝ} {f f' : ℝ → ℂ}
  (hab : a < b) (hf : AbsolutelyContinuousOnInterval f a b)
  (hff' : ∀ᵐ (t : ℝ), t ∈ Set.uIoc a b → HasDerivAt f (f' t) t)
  (hf' : MeasureTheory.MemLp f' 2 (MeasureTheory.volume.restrict (Set.Ioc a b))) {θ : ℝ}
  (hfab : f b = Complex.exp (2 * ↑Real.pi * ↑θ * Complex.I) * f a) :
  (2 * Real.pi * |θ - ↑(round θ)| / (b - a)) ^ 2 * ∫ (t : ℝ) in a..b, ‖f t‖ ^ 2 ≤
    ∫ (t : ℝ) in a..b, ‖f' t‖ ^ 2
```

## Sources

- [Tau Ceti documentation: `TauCeti.integral_norm_sub_average_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Wirtinger.html#TauCeti.integral_norm_sub_average_sq_le)
- [Source of `TauCeti.integral_norm_sub_average_sq_le` in TauCeti/Analysis/Fourier/Wirtinger.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Fourier/Wirtinger.lean#L235)
