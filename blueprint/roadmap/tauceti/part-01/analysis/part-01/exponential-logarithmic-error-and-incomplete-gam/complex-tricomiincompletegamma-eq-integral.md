---
declaration: theorem
origin: cited
lean: Complex.tricomiIncompleteGamma_eq_integral
statement: formalized
proof: formalized
---

# Complex.tricomiIncompleteGamma_eq_integral

Tricomi's integral (DLMF 8.2.7): for `0 < Re a`,
`γ*(a, z) = Γ(a)⁻¹ ∫₀¹ t^{a−1} e^{−zt} dt`.

```lean
Complex.tricomiIncompleteGamma_eq_integral {a : ℂ} (ha : 0 < a.re) (z : ℂ) :
  a.tricomiIncompleteGamma z =
    (Complex.Gamma a)⁻¹ * ∫ (t : ℝ) in 0..1, ↑t ^ (a - 1) * Complex.exp (-(z * ↑t))
```

## Depends on

- [Complex.tricomiIncompleteGamma](complex-tricomiincompletegamma.md)

## Proof depends on

- [Complex.hasSum_tricomiIncompleteGamma_of_ne_neg_natCast](complex-hassum-tricomiincompletegamma-of-ne-neg.md)

## Lean

Formalized in Tau Ceti as [`Complex.tricomiIncompleteGamma_eq_integral`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.tricomiIncompleteGamma_eq_integral).

## Sources

- [Tau Ceti documentation: `Complex.tricomiIncompleteGamma_eq_integral`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.tricomiIncompleteGamma_eq_integral)
- [Source of `Complex.tricomiIncompleteGamma_eq_integral` in TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean#L278)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
