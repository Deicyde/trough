---
declaration: def
origin: cited
lean: TauCeti.LazardRing.cotangentBasis
statement: formalized
---

# Lazard's computation of the indecomposables of the Lazard ring

The `ℤ`-module
`I ⧸ I²` of indecomposables of `L`, for `I` the augmentation ideal, is free with basis the classes
of the generators `xₙ ∈ L₂ₙ`, `n ≥ 1`.

```lean
TauCeti.LazardRing.cotangentBasis : Module.Basis ℕ+ ℤ TauCeti.LazardRing.augmentationIdeal.Cotangent
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LazardRing.cotangentBasis`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/LazardRing/Indecomposable.html#TauCeti.LazardRing.cotangentBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.LazardRing.cotangentBasis`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/LazardRing/Indecomposable.html#TauCeti.LazardRing.cotangentBasis)
- [Source of `TauCeti.LazardRing.cotangentBasis` in TauCeti/RingTheory/FormalGroup/LazardRing/Indecomposable.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/FormalGroup/LazardRing/Indecomposable.lean#L399)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
