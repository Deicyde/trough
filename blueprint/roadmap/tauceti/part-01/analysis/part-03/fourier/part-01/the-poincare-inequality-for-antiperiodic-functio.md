---
declaration: theorem
origin: cited
lean: TauCeti.mul_integral_norm_sq_le_integral_norm_sq_of_eq_neg
statement: formalized
proof: formalized
---

# The Poincaré inequality for antiperiodic functions

If `g` is absolutely continuous on
`[a, b]`, valued in a finite-dimensional real inner product space, with square-integrable
almost-everywhere derivative `g'`, and `g b = -g a`, then
`(π / (b - a)) ^ 2 ∫ₐᵇ ‖g‖ ^ 2 ≤ ∫ₐᵇ ‖g'‖ ^ 2`. The constant is sharp: equality holds for
`g t = cos (π (t - a) / (b - a)) • v`.

```lean
TauCeti.mul_integral_norm_sq_le_integral_norm_sq_of_eq_neg.{u_1} {a b : ℝ} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] {g g' : ℝ → V}
  (hab : a < b) (hg : AbsolutelyContinuousOnInterval g a b)
  (hgg' : ∀ᵐ (t : ℝ), t ∈ Set.uIoc a b → HasDerivAt g (g' t) t)
  (hg' : MeasureTheory.MemLp g' 2 (MeasureTheory.volume.restrict (Set.Ioc a b)))
  (hgab : g b = -g a) :
  (Real.pi / (b - a)) ^ 2 * ∫ (t : ℝ) in a..b, ‖g t‖ ^ 2 ≤ ∫ (t : ℝ) in a..b, ‖g' t‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Wirtinger's inequality](../part-02/wirtingers-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mul_integral_norm_sq_le_integral_norm_sq_of_eq_neg`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/TwistedWirtinger.html#TauCeti.mul_integral_norm_sq_le_integral_norm_sq_of_eq_neg).

## Sources

- [Tau Ceti documentation: `TauCeti.mul_integral_norm_sq_le_integral_norm_sq_of_eq_neg`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/TwistedWirtinger.html#TauCeti.mul_integral_norm_sq_le_integral_norm_sq_of_eq_neg)
- [Source of `TauCeti.mul_integral_norm_sq_le_integral_norm_sq_of_eq_neg` in TauCeti/Analysis/Fourier/TwistedWirtinger.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Fourier/TwistedWirtinger.lean#L160)
