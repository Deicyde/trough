---
declaration: theorem
origin: cited
lean: TauCeti.hasSum_sq_frequency_mul_sq_fourierCoeffOn
statement: formalized
proof: formalized
---

# Parseval's energy identity

**Parseval's energy identity** for an absolutely continuous closed complex curve with
square-integrable derivative. Each frequency contributes its squared frequency times the
squared norm of the corresponding Fourier coefficient.

```lean
TauCeti.hasSum_sq_frequency_mul_sq_fourierCoeffOn {a b : ℝ} {f f' : ℝ → ℂ} (hab : a < b)
  (hf : AbsolutelyContinuousOnInterval f a b)
  (hff' : ∀ᵐ (t : ℝ), t ∈ Set.uIoc a b → HasDerivAt f (f' t) t) (hfab : f a = f b)
  (hf' : MeasureTheory.MemLp f' 2 (MeasureTheory.volume.restrict (Set.Ioc a b))) :
  HasSum (fun n => (2 * Real.pi * ↑n / (b - a)) ^ 2 * ‖fourierCoeffOn hab f n‖ ^ 2)
    ((b - a)⁻¹ * ∫ (t : ℝ) in a..b, ‖f' t‖ ^ 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.hasSum_sq_frequency_mul_sq_fourierCoeffOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/AbsolutelyContinuous.html#TauCeti.hasSum_sq_frequency_mul_sq_fourierCoeffOn).

## Sources

- [Tau Ceti documentation: `TauCeti.hasSum_sq_frequency_mul_sq_fourierCoeffOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/AbsolutelyContinuous.html#TauCeti.hasSum_sq_frequency_mul_sq_fourierCoeffOn)
- [Source of `TauCeti.hasSum_sq_frequency_mul_sq_fourierCoeffOn` in TauCeti/Analysis/Fourier/AbsolutelyContinuous.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Fourier/AbsolutelyContinuous.lean#L122)
