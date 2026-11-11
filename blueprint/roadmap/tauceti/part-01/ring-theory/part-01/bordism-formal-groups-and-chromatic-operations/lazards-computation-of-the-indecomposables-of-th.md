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

## Proof depends on

- [Nakayama's lemma over `ℤ`](../../part-02/other-results/part-02/nakayamas-lemma-over-z.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LazardRing.cotangentBasis`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/LazardRing/Indecomposable.html#TauCeti.LazardRing.cotangentBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.LazardRing.cotangentBasis`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/LazardRing/Indecomposable.html#TauCeti.LazardRing.cotangentBasis)
- [Source of `TauCeti.LazardRing.cotangentBasis` in TauCeti/RingTheory/FormalGroup/LazardRing/Indecomposable.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/FormalGroup/LazardRing/Indecomposable.lean#L399)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
