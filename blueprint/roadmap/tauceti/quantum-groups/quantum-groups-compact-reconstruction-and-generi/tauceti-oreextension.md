---
declaration: structure
origin: cited
lean: TauCeti.OreExtension
statement: formalized
---

# TauCeti.OreExtension

The Ore extension `R[X; σ, δ]`, represented by its finitely supported left coefficients.

```lean
TauCeti.OreExtension.{u, v} {k : Type u} {R : Type v} [CommSemiring k] [Semiring R] [Algebra k R]
  (σ : R →ₐ[k] R) (δ : TauCeti.SigmaDerivation σ) : Type v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.OreExtension`](https://taucetiproject.org/docs/TauCeti/Algebra/OreExtension/Basic.html#TauCeti.OreExtension).

## Sources

- [Tau Ceti documentation: `TauCeti.OreExtension`](https://taucetiproject.org/docs/TauCeti/Algebra/OreExtension/Basic.html#TauCeti.OreExtension)
- [Source of `TauCeti.OreExtension` in TauCeti/Algebra/OreExtension/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/OreExtension/Basic.lean#L122)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuantumGroups/STATUS.md)
