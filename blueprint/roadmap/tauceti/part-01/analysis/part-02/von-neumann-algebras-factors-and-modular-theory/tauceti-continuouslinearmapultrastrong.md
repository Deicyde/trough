---
declaration: structure
origin: cited
lean: TauCeti.ContinuousLinearMapUltrastrong
statement: formalized
---

# TauCeti.ContinuousLinearMapUltrastrong

The type copy of `E →L[𝕜] F` endowed with the ultrastrong operator topology: the coarsest
topology for which `T ↦ (⊕ₙ T) ξ` is continuous into `ℓ²(ℕ, F)` for every `ξ ∈ ℓ²(ℕ, E)`.

```lean
TauCeti.ContinuousLinearMapUltrastrong.{u_1, u_2, u_3} (𝕜 : Type u_1) (E : Type u_2) (F : Type u_3)
  [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] : Type (max u_2 u_3)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ContinuousLinearMapUltrastrong`](https://taucetiproject.org/docs/TauCeti/Analysis/LocallyConvex/UltrastrongTopology.html#TauCeti.ContinuousLinearMapUltrastrong).

## Sources

- [Tau Ceti documentation: `TauCeti.ContinuousLinearMapUltrastrong`](https://taucetiproject.org/docs/TauCeti/Analysis/LocallyConvex/UltrastrongTopology.html#TauCeti.ContinuousLinearMapUltrastrong)
- [Source of `TauCeti.ContinuousLinearMapUltrastrong` in TauCeti/Analysis/LocallyConvex/UltrastrongTopology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/LocallyConvex/UltrastrongTopology.lean#L58)
- [Tau Ceti roadmap status: Von Neumann algebras, factors, and modular theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/VonNeumannAlgebras/STATUS.md)
