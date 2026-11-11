---
declaration: theorem
origin: cited
lean: Complex.tricomiIncompleteGamma_ode
statement: formalized
proof: formalized
---

# Complex.tricomiIncompleteGamma_ode

The differential equation of Tricomi's function (DLMF 8.2.14):
`z w'' + (a + 1 + z) w' + a w = 0` for `w = γ*(a, ·)`.

```lean
Complex.tricomiIncompleteGamma_ode (a z : ℂ) :
  z * deriv (deriv a.tricomiIncompleteGamma) z + (a + 1 + z) * deriv a.tricomiIncompleteGamma z +
      a * a.tricomiIncompleteGamma z =
    0
```

## Depends on

- [Complex.tricomiIncompleteGamma](complex-tricomiincompletegamma.md)

## Proof depends on

- [Complex.hasDerivAt_tricomiIncompleteGamma](complex-hasderivat-tricomiincompletegamma.md)
- [Complex.tricomiIncompleteGamma_eq_mul_tricomiIncompleteGamma_add_one](complex-tricomiincompletegamma-eq-mul-tricomiinc.md)

## Lean

Formalized in Tau Ceti as [`Complex.tricomiIncompleteGamma_ode`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.tricomiIncompleteGamma_ode).

## Sources

- [Tau Ceti documentation: `Complex.tricomiIncompleteGamma_ode`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.tricomiIncompleteGamma_ode)
- [Source of `Complex.tricomiIncompleteGamma_ode` in TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean#L177)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
