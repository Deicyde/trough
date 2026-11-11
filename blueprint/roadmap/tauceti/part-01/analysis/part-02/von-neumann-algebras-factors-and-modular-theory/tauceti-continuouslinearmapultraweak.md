---
declaration: structure
origin: cited
lean: TauCeti.ContinuousLinearMapUltraweak
statement: formalized
---

# TauCeti.ContinuousLinearMapUltraweak

The type copy of `E →L[𝕜] F` endowed with the ultraweak operator topology: the coarsest
topology for which the matrix coefficient `T ↦ ⟪η, (⊕ₙ T) ξ⟫ = ∑ₙ ⟪ηₙ, T ξₙ⟫` is continuous for all
`ξ ∈ ℓ²(ℕ, E)` and `η ∈ ℓ²(ℕ, F)`.

```lean
TauCeti.ContinuousLinearMapUltraweak.{u_1, u_2, u_3} (𝕜 : Type u_1) (E : Type u_2) (F : Type u_3)
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [NormedAddCommGroup F]
  [InnerProductSpace 𝕜 F] : Type (max u_2 u_3)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ContinuousLinearMapUltraweak`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UltraweakTopology.html#TauCeti.ContinuousLinearMapUltraweak).

## Sources

- [Tau Ceti documentation: `TauCeti.ContinuousLinearMapUltraweak`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UltraweakTopology.html#TauCeti.ContinuousLinearMapUltraweak)
- [Source of `TauCeti.ContinuousLinearMapUltraweak` in TauCeti/Analysis/InnerProductSpace/UltraweakTopology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/UltraweakTopology.lean#L54)
- [Tau Ceti roadmap status: Von Neumann algebras, factors, and modular theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/VonNeumannAlgebras/STATUS.md)
