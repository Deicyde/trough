---
declaration: def
origin: cited
lean: TauCeti.HeegaardRegionSystem.hatDifferential
statement: formalized
---

# TauCeti.HeegaardRegionSystem.hatDifferential

The hat differential of a Heegaard diagram with region Euler characteristics `χ`: the
`ZMod 2`-linear endomorphism of the free module on generators whose coefficient from `x` to `y`
is the number, modulo two, of nonnegative domains of Maslov index one from `x` to `y` avoiding
the basepoints (`TauCeti.HeegaardRegionSystem.hatCoefficient`).

```lean
TauCeti.HeegaardRegionSystem.hatDifferential.{u, v, w} {n : ℕ} {Point : Type u} {Region : Type v}
  {Basepoint : Type w} (H : TauCeti.HeegaardRegionSystem n Point Region Basepoint) [Fintype Point]
  [DecidableEq Region] [Fintype Region] (χ : Region → ℤ) :
  (H.Generator →₀ ZMod 2) →ₗ[ZMod 2] H.Generator →₀ ZMod 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HeegaardRegionSystem.hatDifferential`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/Heegaard/HatDifferential.html#TauCeti.HeegaardRegionSystem.hatDifferential).

## Sources

- [Tau Ceti documentation: `TauCeti.HeegaardRegionSystem.hatDifferential`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/Heegaard/HatDifferential.html#TauCeti.HeegaardRegionSystem.hatDifferential)
- [Source of `TauCeti.HeegaardRegionSystem.hatDifferential` in TauCeti/LowDimTopology/Heegaard/HatDifferential.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LowDimTopology/Heegaard/HatDifferential.lean#L234)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
