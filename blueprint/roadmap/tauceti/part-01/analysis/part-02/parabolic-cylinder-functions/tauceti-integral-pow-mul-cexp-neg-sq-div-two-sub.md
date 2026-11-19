---
declaration: theorem
origin: cited
lean: TauCeti.integral_pow_mul_cexp_neg_sq_div_two_sub_I_mul
statement: formalized
proof: formalized
---

# TauCeti.integral_pow_mul_cexp_neg_sq_div_two_sub_I_mul

Fourier representation of the probabilists' Hermite polynomial times its Gaussian weight,
valid at every complex frequency.

```lean
TauCeti.integral_pow_mul_cexp_neg_sq_div_two_sub_I_mul (n : ℕ) (y : ℂ) :
  ∫ (s : ℝ), ↑s ^ n * Complex.exp (-↑s ^ 2 / 2 - Complex.I * y * ↑s) =
    ↑√(2 * Real.pi) * (-Complex.I) ^ n * (Polynomial.aeval y) (Polynomial.hermite n) *
      Complex.exp (-y ^ 2 / 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_pow_mul_cexp_neg_sq_div_two_sub_I_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/FourierIntegral.html#TauCeti.integral_pow_mul_cexp_neg_sq_div_two_sub_I_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.integral_pow_mul_cexp_neg_sq_div_two_sub_I_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/FourierIntegral.html#TauCeti.integral_pow_mul_cexp_neg_sq_div_two_sub_I_mul)
- [Source of `TauCeti.integral_pow_mul_cexp_neg_sq_div_two_sub_I_mul` in TauCeti/Analysis/SpecialFunctions/Hermite/FourierIntegral.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Hermite/FourierIntegral.lean#L113)
- [Tau Ceti roadmap status: Parabolic cylinder functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsParabolicCylinder/STATUS.md)
