---
declaration: theorem
origin: cited
lean: TauCeti.Real.hasSum_erf
statement: formalized
proof: formalized
---

# TauCeti.Real.hasSum_erf

The alternating Maclaurin series of the error function (DLMF 7.6.1):
`erf x = ∑_{n ≥ 0} (2 / √π) (-1)^n x^{2n + 1} / (n! (2n + 1))` for all `x : ℝ`.

```lean
TauCeti.Real.hasSum_erf (x : ℝ) :
  HasSum (fun n => 2 / √Real.pi * ((-1) ^ n * x ^ (2 * n + 1) / (↑n.factorial * (2 * ↑n + 1))))
    (TauCeti.Real.erf x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Complex.hasDerivAt_tricomiIncompleteGamma](../../part-01/exponential-logarithmic-error-and-incomplete-gam/complex-hasderivat-tricomiincompletegamma.md)
- [Complex.hasSum_tricomiIncompleteGamma_of_ne_neg_natCast](../../part-01/exponential-logarithmic-error-and-incomplete-gam/complex-hassum-tricomiincompletegamma-of-ne-neg.md)
- [Complex.tricomiIncompleteGamma](../../part-01/exponential-logarithmic-error-and-incomplete-gam/complex-tricomiincompletegamma.md)
- [Complex.tricomiIncompleteGamma_eq_mul_tricomiIncompleteGamma_add_one](../../part-01/exponential-logarithmic-error-and-incomplete-gam/complex-tricomiincompletegamma-eq-mul-tricomiinc.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Real.hasSum_erf`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Erf/Series.html#TauCeti.Real.hasSum_erf).

## Sources

- [Tau Ceti documentation: `TauCeti.Real.hasSum_erf`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Erf/Series.html#TauCeti.Real.hasSum_erf)
- [Source of `TauCeti.Real.hasSum_erf` in TauCeti/Analysis/SpecialFunctions/Erf/Series.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Erf/Series.lean#L117)
- [Tau Ceti roadmap status: Parabolic cylinder functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsParabolicCylinder/STATUS.md)
