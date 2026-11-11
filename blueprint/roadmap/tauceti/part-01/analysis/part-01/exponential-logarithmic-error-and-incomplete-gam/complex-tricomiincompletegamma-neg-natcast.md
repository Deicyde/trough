---
declaration: theorem
origin: cited
lean: Complex.tricomiIncompleteGamma_neg_natCast
statement: formalized
proof: formalized
---

# Complex.tricomiIncompleteGamma_neg_natCast

At a nonpositive integer parameter, Tricomi's function is a monomial (DLMF 8.4.12):
`γ*(−n, z) = zⁿ`.

```lean
Complex.tricomiIncompleteGamma_neg_natCast (n : ℕ) (z : ℂ) : (-↑n).tricomiIncompleteGamma z = z ^ n
```

## Depends on

- [Complex.tricomiIncompleteGamma](complex-tricomiincompletegamma.md)

## Proof depends on

- [Complex.hasSum_tricomiIncompleteGamma](complex-hassum-tricomiincompletegamma.md)
- [Complex.tricomiIncompleteGamma_eq_mul_tricomiIncompleteGamma_add_one](complex-tricomiincompletegamma-eq-mul-tricomiinc.md)

## Lean

Formalized in Tau Ceti as [`Complex.tricomiIncompleteGamma_neg_natCast`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.tricomiIncompleteGamma_neg_natCast).

## Sources

- [Tau Ceti documentation: `Complex.tricomiIncompleteGamma_neg_natCast`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.tricomiIncompleteGamma_neg_natCast)
- [Source of `Complex.tricomiIncompleteGamma_neg_natCast` in TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean#L120)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
