---
declaration: theorem
origin: cited
lean: TauCeti.integral_norm_sub_average_sq_eq_iff
statement: formalized
proof: formalized
---

# Equality in Wirtinger's inequality

Equality holds exactly when, on `[a, b]`, the function
is its mean plus a first harmonic `cos (2π t / (b - a)) • u + sin (2π t / (b - a)) • v`.

```lean
TauCeti.integral_norm_sub_average_sq_eq_iff.{u_1} {a b : ℝ} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] {f f' : ℝ → V} (hab : a < b)
  (hf : AbsolutelyContinuousOnInterval f a b)
  (hff' : ∀ᵐ (t : ℝ), t ∈ Set.uIoc a b → HasDerivAt f (f' t) t) (hfab : f a = f b)
  (hf' : MeasureTheory.MemLp f' 2 (MeasureTheory.volume.restrict (Set.Ioc a b))) :
  ∫ (x : ℝ) in a..b, ‖f x - ⨍ (y : ℝ) in a..b, f y‖ ^ 2 =
      ((b - a) / (2 * Real.pi)) ^ 2 * ∫ (x : ℝ) in a..b, ‖f' x‖ ^ 2 ↔
    ∃ u v,
      ∀ t ∈ Set.Icc a b,
        f t - ⨍ (y : ℝ) in a..b, f y =
          Real.cos (2 * Real.pi * t / (b - a)) • u + Real.sin (2 * Real.pi * t / (b - a)) • v
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Parseval's energy identity](parsevals-energy-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_norm_sub_average_sq_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Wirtinger.html#TauCeti.integral_norm_sub_average_sq_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.integral_norm_sub_average_sq_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Wirtinger.html#TauCeti.integral_norm_sub_average_sq_eq_iff)
- [Source of `TauCeti.integral_norm_sub_average_sq_eq_iff` in TauCeti/Analysis/Fourier/Wirtinger.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Fourier/Wirtinger.lean#L250)
