---
declaration: theorem
origin: cited
lean: Complex.hasDerivAt_tricomiIncompleteGamma
statement: formalized
proof: formalized
---

# Complex.hasDerivAt_tricomiIncompleteGamma

The derivative of Tricomi's function in its argument:
`∂γ*(a, z)/∂z = −a γ*(a + 1, z)`.

```lean
Complex.hasDerivAt_tricomiIncompleteGamma (a z : ℂ) :
  HasDerivAt a.tricomiIncompleteGamma (-a * (a + 1).tricomiIncompleteGamma z) z
```

## Depends on

- [Complex.tricomiIncompleteGamma](complex-tricomiincompletegamma.md)

## Proof depends on

- [Complex.hasSum_deriv_regularizedHGFun](complex-hassum-deriv-regularizedhgfun.md)

## Lean

Formalized in Tau Ceti as [`Complex.hasDerivAt_tricomiIncompleteGamma`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.hasDerivAt_tricomiIncompleteGamma).

## Sources

- [Tau Ceti documentation: `Complex.hasDerivAt_tricomiIncompleteGamma`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.hasDerivAt_tricomiIncompleteGamma)
- [Source of `Complex.hasDerivAt_tricomiIncompleteGamma` in TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean#L143)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
