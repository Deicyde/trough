---
declaration: inductive
origin: cited
lean: TauCeti.LimitGroup.ICE
statement: formalized
---

# TauCeti.LimitGroup.ICE

An *iterated extension of centralizers* (ICE) over `F`: a finite chain
`F = G₀ < G₁ < ⋯ < Gₘ = G` with `Gᵢ₊₁ = Gᵢ(uᵢ, ℤ^{nᵢ})` an admissible extension of a centralizer
of `Gᵢ` (`IsAdmissibleCentralizerStep uᵢ nᵢ`), together with the coefficient inclusion
`ι : F →* G`.

```lean
TauCeti.LimitGroup.ICE.{u} (F : Type u) [Group F] (G : Type u) [Group G] : (F →* G) → Type (u + 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LimitGroup.ICE`](https://taucetiproject.org/docs/TauCeti/GroupTheory/LimitGroup/CentralizerExtension/Iterated.html#TauCeti.LimitGroup.ICE).

## Sources

- [Tau Ceti documentation: `TauCeti.LimitGroup.ICE`](https://taucetiproject.org/docs/TauCeti/GroupTheory/LimitGroup/CentralizerExtension/Iterated.html#TauCeti.LimitGroup.ICE)
- [Source of `TauCeti.LimitGroup.ICE` in TauCeti/GroupTheory/LimitGroup/CentralizerExtension/Iterated.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/LimitGroup/CentralizerExtension/Iterated.lean#L70)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
