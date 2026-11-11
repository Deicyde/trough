---
declaration: def
origin: cited
lean: Complex.tricomiIncompleteGamma
statement: formalized
---

# Complex.tricomiIncompleteGamma

Tricomi's entire incomplete Gamma function `γ*(a, z) = e^{−z} 𝐌(1, a + 1, z)` (DLMF 8.5.2),
written through Mathlib's regularized Kummer function `𝐌(1, b, z) = ∑ zⁿ / Γ(b + n)`. It is
entire in each of `a` and `z`; for `a ∉ −ℕ` and `z` off the cut, the lower incomplete Gamma
function is `γ(a, z) = Γ(a) z^a γ*(a, z)`.

```lean
Complex.tricomiIncompleteGamma (a z : ℂ) : ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Complex.tricomiIncompleteGamma`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.tricomiIncompleteGamma).

## Sources

- [Tau Ceti documentation: `Complex.tricomiIncompleteGamma`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.tricomiIncompleteGamma)
- [Source of `Complex.tricomiIncompleteGamma` in TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean#L69)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
