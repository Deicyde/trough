---
declaration: theorem
origin: cited
lean: Complex.hasSum_tricomiIncompleteGamma
statement: formalized
proof: formalized
---

# Complex.hasSum_tricomiIncompleteGamma

The power series of Tricomi's function (DLMF 8.7.1):
`γ*(a, z) = e^{−z} ∑ zᵏ / Γ(a + k + 1)`, for all `a` and `z`.

```lean
Complex.hasSum_tricomiIncompleteGamma (a z : ℂ) :
  HasSum (fun k => Complex.exp (-z) * z ^ k / Complex.Gamma (a + ↑k + 1))
    (a.tricomiIncompleteGamma z)
```

## Depends on

- [Complex.tricomiIncompleteGamma](complex-tricomiincompletegamma.md)

## Lean

Formalized in Tau Ceti as [`Complex.hasSum_tricomiIncompleteGamma`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.hasSum_tricomiIncompleteGamma).

## Sources

- [Tau Ceti documentation: `Complex.hasSum_tricomiIncompleteGamma`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.html#Complex.hasSum_tricomiIncompleteGamma)
- [Source of `Complex.hasSum_tricomiIncompleteGamma` in TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean#L80)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
