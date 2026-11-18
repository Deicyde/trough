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
- [Source of `Complex.tricomiIncompleteGamma_neg_natCast` in TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean#L120)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
