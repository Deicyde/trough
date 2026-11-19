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
- [Source of `Complex.tricomiIncompleteGamma_ode` in TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean#L177)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
