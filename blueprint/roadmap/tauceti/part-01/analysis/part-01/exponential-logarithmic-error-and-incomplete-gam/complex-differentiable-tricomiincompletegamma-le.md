---
declaration: theorem
origin: cited
lean: Complex.differentiable_tricomiIncompleteGamma_left
statement: formalized
proof: formalized
---

# Complex.differentiable_tricomiIncompleteGamma_left

Tricomi's function is entire in its parameter.

```lean
Complex.differentiable_tricomiIncompleteGamma_left (z : ℂ) :
  Differentiable ℂ fun a => a.tricomiIncompleteGamma z
```

## Depends on

- [Complex.tricomiIncompleteGamma](complex-tricomiincompletegamma.md)

## Proof depends on

- [Complex.norm_inv_Gamma_add_natCast_le](complex-norm-inv-gamma-add-natcast-le.md)
- [Complex.tricomiIncompleteGamma_eq_mul_tricomiIncompleteGamma_add_one](complex-tricomiincompletegamma-eq-mul-tricomiinc.md)

## Lean

Formalized in Tau Ceti as [`Complex.differentiable_tricomiIncompleteGamma_left`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.differentiable_tricomiIncompleteGamma_left).

## Sources

- [Tau Ceti documentation: `Complex.differentiable_tricomiIncompleteGamma_left`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.differentiable_tricomiIncompleteGamma_left)
- [Source of `Complex.differentiable_tricomiIncompleteGamma_left` in TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean#L233)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
