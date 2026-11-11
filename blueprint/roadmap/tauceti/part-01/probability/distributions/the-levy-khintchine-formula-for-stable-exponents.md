---
declaration: theorem
origin: cited
lean: TauCeti.Probability.integral_exp_sub_one_sub_sin_stableLevyMeasure
statement: formalized
proof: formalized
---

# The Lévy–Khintchine formula for stable exponents

For `0 < α < 2` and `|β| ≤ 1`,
integrating the sine-compensated characteristic kernel against the stable Lévy measure gives
the stable characteristic exponent in Nolan's `S₀` parameterization.

```lean
TauCeti.Probability.integral_exp_sub_one_sub_sin_stableLevyMeasure {α β : ℝ} (hα : α ∈ Set.Ioo 0 2)
  (hβ : |β| ≤ 1) (t : ℝ) :
  ∫ (x : ℝ),
      Complex.exp (↑(t * x) * Complex.I) - 1 -
        ↑(t * Real.sin x) * Complex.I ∂TauCeti.Probability.stableLevyMeasure α β =
    TauCeti.Probability.stableCharacteristicExponent α β t
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.integral_exp_sub_one_sub_sin_stableLevyMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Stable/LevyKhintchine.html#TauCeti.Probability.integral_exp_sub_one_sub_sin_stableLevyMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.integral_exp_sub_one_sub_sin_stableLevyMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Stable/LevyKhintchine.html#TauCeti.Probability.integral_exp_sub_one_sub_sin_stableLevyMeasure)
- [Source of `TauCeti.Probability.integral_exp_sub_one_sub_sin_stableLevyMeasure` in TauCeti/Probability/Distributions/Stable/LevyKhintchine.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Distributions/Stable/LevyKhintchine.lean#L106)
