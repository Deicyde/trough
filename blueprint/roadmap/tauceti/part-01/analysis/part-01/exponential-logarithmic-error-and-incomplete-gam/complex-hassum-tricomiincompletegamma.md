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
- [Source of `Complex.hasSum_tricomiIncompleteGamma` in TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/IncompleteGamma/Tricomi.lean#L80)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
