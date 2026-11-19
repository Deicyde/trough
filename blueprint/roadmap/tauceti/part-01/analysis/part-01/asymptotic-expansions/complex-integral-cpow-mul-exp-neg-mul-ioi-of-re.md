---
declaration: theorem
origin: cited
lean: Complex.integral_cpow_mul_exp_neg_mul_Ioi_of_re_pos
statement: formalized
proof: formalized
---

# Complex.integral_cpow_mul_exp_neg_mul_Ioi_of_re_pos

The Gamma integral with a complex rate: for `Re s > 0` and `Re z > 0`,
`∫₀^∞ t^{s-1} e^{-zt} dt = Γ(s) z^{-s}`. Mathlib's `Complex.integral_cpow_mul_exp_neg_mul_Ioi`
is the case of a positive real rate.

```lean
Complex.integral_cpow_mul_exp_neg_mul_Ioi_of_re_pos {s z : ℂ} (hs : 0 < s.re) (hz : 0 < z.re) :
  ∫ (t : ℝ) in Set.Ioi 0, ↑t ^ (s - 1) * Complex.exp (-(z * ↑t)) = Complex.Gamma s * z ^ (-s)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Complex.integral_cpow_mul_exp_neg_mul_Ioi_of_re_pos`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/IntegralComplexRate.html#Complex.integral_cpow_mul_exp_neg_mul_Ioi_of_re_pos).

## Sources

- [Tau Ceti documentation: `Complex.integral_cpow_mul_exp_neg_mul_Ioi_of_re_pos`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/IntegralComplexRate.html#Complex.integral_cpow_mul_exp_neg_mul_Ioi_of_re_pos)
- [Source of `Complex.integral_cpow_mul_exp_neg_mul_Ioi_of_re_pos` in TauCeti/Analysis/SpecialFunctions/Gamma/IntegralComplexRate.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Gamma/IntegralComplexRate.lean#L102)
- [Tau Ceti roadmap status: Asymptotic expansions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AsymptoticExpansions/STATUS.md)
