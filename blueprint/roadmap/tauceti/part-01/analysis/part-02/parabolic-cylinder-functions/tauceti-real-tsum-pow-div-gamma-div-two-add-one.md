---
declaration: theorem
origin: cited
lean: TauCeti.Real.tsum_pow_div_Gamma_div_two_add_one
statement: formalized
proof: formalized
---

# TauCeti.Real.tsum_pow_div_Gamma_div_two_add_one

Closed form for the `tsum` of the half-Gamma series (DLMF 7.6.3):
`∑_{m ≥ 0} x^m / Γ(m / 2 + 1) = exp(x²) (1 + erf x)` for all `x : ℝ`.

```lean
TauCeti.Real.tsum_pow_div_Gamma_div_two_add_one (x : ℝ) :
  ∑' (m : ℕ), x ^ m / Real.Gamma (↑m / 2 + 1) = Real.exp (x ^ 2) * (1 + TauCeti.Real.erf x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Complex.hasDerivAt_tricomiIncompleteGamma](../../part-01/exponential-logarithmic-error-and-incomplete-gam/complex-hasderivat-tricomiincompletegamma.md)
- [Complex.hasSum_tricomiIncompleteGamma](../../part-01/exponential-logarithmic-error-and-incomplete-gam/complex-hassum-tricomiincompletegamma.md)
- [Complex.tricomiIncompleteGamma](../../part-01/exponential-logarithmic-error-and-incomplete-gam/complex-tricomiincompletegamma.md)
- [Complex.tricomiIncompleteGamma_eq_mul_tricomiIncompleteGamma_add_one](../../part-01/exponential-logarithmic-error-and-incomplete-gam/complex-tricomiincompletegamma-eq-mul-tricomiinc.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Real.tsum_pow_div_Gamma_div_two_add_one`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Erf/Series.html#TauCeti.Real.tsum_pow_div_Gamma_div_two_add_one).

## Sources

- [Tau Ceti documentation: `TauCeti.Real.tsum_pow_div_Gamma_div_two_add_one`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Erf/Series.html#TauCeti.Real.tsum_pow_div_Gamma_div_two_add_one)
- [Source of `TauCeti.Real.tsum_pow_div_Gamma_div_two_add_one` in TauCeti/Analysis/SpecialFunctions/Erf/Series.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Erf/Series.lean#L227)
- [Tau Ceti roadmap status: Parabolic cylinder functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsParabolicCylinder/STATUS.md)
