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
- [Source of `Complex.tricomiIncompleteGamma` in TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean#L69)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
