---
declaration: theorem
origin: cited
lean: Real.tsum_pow_div_Gamma_div_two_add_one_lt_two_mul_exp
statement: formalized
proof: formalized
---

# Real.tsum_pow_div_Gamma_div_two_add_one_lt_two_mul_exp

Sharp polynomial-free Gaussian majorant for the half-Gamma series:
`∑_{m ≥ 0} x^m / Γ(m / 2 + 1) < 2 exp(x²)` for every `x : ℝ`.

```lean
Real.tsum_pow_div_Gamma_div_two_add_one_lt_two_mul_exp (x : ℝ) :
  ∑' (m : ℕ), x ^ m / Real.Gamma (↑m / 2 + 1) < 2 * Real.exp (x ^ 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Real.tsum_pow_div_Gamma_div_two_add_one](tauceti-real-tsum-pow-div-gamma-div-two-add-one.md)

## Lean

Formalized in Tau Ceti as [`Real.tsum_pow_div_Gamma_div_two_add_one_lt_two_mul_exp`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Erf/Series.html#Real.tsum_pow_div_Gamma_div_two_add_one_lt_two_mul_exp).

## Sources

- [Tau Ceti documentation: `Real.tsum_pow_div_Gamma_div_two_add_one_lt_two_mul_exp`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Erf/Series.html#Real.tsum_pow_div_Gamma_div_two_add_one_lt_two_mul_exp)
- [Source of `Real.tsum_pow_div_Gamma_div_two_add_one_lt_two_mul_exp` in TauCeti/Analysis/SpecialFunctions/Erf/Series.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Erf/Series.lean#L250)
- [Tau Ceti roadmap status: Parabolic cylinder functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsParabolicCylinder/STATUS.md)
