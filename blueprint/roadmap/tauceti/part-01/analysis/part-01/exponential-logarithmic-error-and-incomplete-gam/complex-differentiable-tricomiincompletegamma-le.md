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
- [Source of `Complex.differentiable_tricomiIncompleteGamma_left` in TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean#L233)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
