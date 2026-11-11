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
- [Source of `Complex.hasSum_tricomiIncompleteGamma_of_ne_neg_natCast` in TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean#L255)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
