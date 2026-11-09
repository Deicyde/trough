---
declaration: def
origin: cited
lean: TauCeti.HeegaardRegionSystem.IsNice
statement: formalized
---

# TauCeti.HeegaardRegionSystem.IsNice

A pointed Heegaard diagram, with region Euler characteristics `χ`, is *nice* when every
region containing no basepoint is a bigon or a square: a disk, of Euler characteristic one, with
two or four corners.

```lean
TauCeti.HeegaardRegionSystem.IsNice.{u, v, w} {n : ℕ} {Point : Type u} {Region : Type v}
  {Basepoint : Type w} (H : TauCeti.HeegaardRegionSystem n Point Region Basepoint) [Fintype Point]
  [DecidableEq Region] (χ : Region → ℤ) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HeegaardRegionSystem.IsNice`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/Heegaard/Nice.html#TauCeti.HeegaardRegionSystem.IsNice).

## Sources

- [Tau Ceti documentation: `TauCeti.HeegaardRegionSystem.IsNice`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/Heegaard/Nice.html#TauCeti.HeegaardRegionSystem.IsNice)
- [Source of `TauCeti.HeegaardRegionSystem.IsNice` in TauCeti/LowDimTopology/Heegaard/Nice.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LowDimTopology/Heegaard/Nice.lean#L89)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
