---
declaration: theorem
origin: cited
lean: Complex.hasSum_tricomiIncompleteGamma_of_ne_neg_natCast
statement: formalized
proof: formalized
---

# Complex.hasSum_tricomiIncompleteGamma_of_ne_neg_natCast

The power series of Tricomi's function in `−z` (DLMF 8.7.1): for `a ∉ −ℕ`,
`γ*(a, z) = Γ(a)⁻¹ ∑ (−z)ᵏ / (k! (a + k))`.

```lean
Complex.hasSum_tricomiIncompleteGamma_of_ne_neg_natCast {a : ℂ} (ha : ∀ (n : ℕ), a ≠ -↑n) (z : ℂ) :
  HasSum (fun k => (Complex.Gamma a)⁻¹ * ((-z) ^ k / (↑k.factorial * (a + ↑k))))
    (a.tricomiIncompleteGamma z)
```

## Depends on

- [Complex.tricomiIncompleteGamma](complex-tricomiincompletegamma.md)

## Proof depends on

- [Complex.summable_norm_regularizedHGFun](complex-summable-norm-regularizedhgfun.md)

## Lean

Formalized in Tau Ceti as [`Complex.hasSum_tricomiIncompleteGamma_of_ne_neg_natCast`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.hasSum_tricomiIncompleteGamma_of_ne_neg_natCast).

## Sources

- [Tau Ceti documentation: `Complex.hasSum_tricomiIncompleteGamma_of_ne_neg_natCast`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.hasSum_tricomiIncompleteGamma_of_ne_neg_natCast)
- [Source of `Complex.hasSum_tricomiIncompleteGamma_of_ne_neg_natCast` in TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean#L255)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
