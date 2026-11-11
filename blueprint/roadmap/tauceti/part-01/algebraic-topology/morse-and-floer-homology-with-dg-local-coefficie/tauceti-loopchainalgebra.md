---
declaration: abbrev
origin: cited
lean: TauCeti.loopChainAlgebra
statement: formalized
---

# TauCeti.loopChainAlgebra

The **chain algebra of the Moore loop space**: `C_*(Ω_b B; R)`, the normalized cubical chains
of the Moore loops at `b`, with the Pontryagin product.

```lean
TauCeti.loopChainAlgebra.{u_1, u_2} (B : Type u_1) [TopologicalSpace B] (b : B) (R : Type u_2)
  [CommRing R] : Type (max u_2 u_1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.loopChainAlgebra`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/DGLocalSystem/LoopAlgebra.html#TauCeti.loopChainAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.loopChainAlgebra`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/DGLocalSystem/LoopAlgebra.html#TauCeti.loopChainAlgebra)
- [Source of `TauCeti.loopChainAlgebra` in TauCeti/AlgebraicTopology/DGLocalSystem/LoopAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/DGLocalSystem/LoopAlgebra.lean#L82)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGFloer/STATUS.md)
