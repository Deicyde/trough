---
declaration: theorem
origin: cited
lean: TauCeti.abs_aeval_hermite_mul_exp_div_factorial_le
statement: formalized
proof: formalized
---

# TauCeti.abs_aeval_hermite_mul_exp_div_factorial_le

The Gaussian-weighted probabilists' Hermite polynomial is bounded by the absolute
Gaussian moment, expressed using the Gamma function after division by `n!`.

```lean
TauCeti.abs_aeval_hermite_mul_exp_div_factorial_le (n : ℕ) (y : ℝ) :
  |(Polynomial.aeval y) (Polynomial.hermite n)| * Real.exp (-y ^ 2 / 2) / ↑n.factorial ≤
    2 ^ (-↑n / 2) / Real.Gamma (↑n / 2 + 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.integral_pow_mul_cexp_neg_sq_div_two_sub_I_mul](tauceti-integral-pow-mul-cexp-neg-sq-div-two-sub.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.abs_aeval_hermite_mul_exp_div_factorial_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Bound.html#TauCeti.abs_aeval_hermite_mul_exp_div_factorial_le).

## Sources

- [Tau Ceti documentation: `TauCeti.abs_aeval_hermite_mul_exp_div_factorial_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Bound.html#TauCeti.abs_aeval_hermite_mul_exp_div_factorial_le)
- [Source of `TauCeti.abs_aeval_hermite_mul_exp_div_factorial_le` in TauCeti/Analysis/SpecialFunctions/Hermite/Bound.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Hermite/Bound.lean#L53)
- [Tau Ceti roadmap status: Parabolic cylinder functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsParabolicCylinder/STATUS.md)
