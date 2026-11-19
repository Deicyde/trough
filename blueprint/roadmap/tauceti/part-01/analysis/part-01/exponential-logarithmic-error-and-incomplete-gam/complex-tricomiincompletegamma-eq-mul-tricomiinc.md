---
declaration: theorem
origin: cited
lean: Complex.tricomiIncompleteGamma_eq_mul_tricomiIncompleteGamma_add_one
statement: formalized
proof: formalized
---

# Complex.tricomiIncompleteGamma_eq_mul_tricomiIncompleteGamma_add_one

The recurrence of Tricomi's function in its parameter (DLMF §8.8):
`γ*(a, z) = z γ*(a + 1, z) + e^{−z} / Γ(a + 1)`.

```lean
Complex.tricomiIncompleteGamma_eq_mul_tricomiIncompleteGamma_add_one (a z : ℂ) :
  a.tricomiIncompleteGamma z =
    z * (a + 1).tricomiIncompleteGamma z + Complex.exp (-z) / Complex.Gamma (a + 1)
```

## Depends on

- [Complex.tricomiIncompleteGamma](complex-tricomiincompletegamma.md)

## Proof depends on

- [Complex.hasSum_tricomiIncompleteGamma](complex-hassum-tricomiincompletegamma.md)

## Lean

Formalized in Tau Ceti as [`Complex.tricomiIncompleteGamma_eq_mul_tricomiIncompleteGamma_add_one`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.tricomiIncompleteGamma_eq_mul_tricomiIncompleteGamma_add_one).

## Sources

- [Tau Ceti documentation: `Complex.tricomiIncompleteGamma_eq_mul_tricomiIncompleteGamma_add_one`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.tricomiIncompleteGamma_eq_mul_tricomiIncompleteGamma_add_one)
- [Source of `Complex.tricomiIncompleteGamma_eq_mul_tricomiIncompleteGamma_add_one` in TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean#L90)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
