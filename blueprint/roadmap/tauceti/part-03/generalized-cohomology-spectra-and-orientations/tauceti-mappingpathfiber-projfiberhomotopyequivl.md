---
declaration: def
origin: cited
lean: TauCeti.MappingPathFiber.projFiberHomotopyEquivLoopSpace
statement: formalized
---

# TauCeti.MappingPathFiber.projFiberHomotopyEquivLoopSpace

A reference path `α` from `f b` to `k` makes the fibre of the source projection over `b`
homotopy equivalent to the loop space `Ω K k`. A path `γ` from `f b` to `k` is sent to the loop
`α.symm.trans γ`, and the homotopy inverse sends a loop `ℓ` to the path `α.trans ℓ`.

```lean
TauCeti.MappingPathFiber.projFiberHomotopyEquivLoopSpace.{u, v} {B : Type u} {K : Type v}
  [TopologicalSpace B] [TopologicalSpace K] (f : C(B, K)) (k : K) (b : B) (α : Path (f b) k) :
  ContinuousMap.HomotopyEquiv { p // (TauCeti.MappingPathFiber.proj f k) p = b } (LoopSpace K k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MappingPathFiber.projFiberHomotopyEquivLoopSpace`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/MappingPath/Fiber.html#TauCeti.MappingPathFiber.projFiberHomotopyEquivLoopSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.MappingPathFiber.projFiberHomotopyEquivLoopSpace`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/MappingPath/Fiber.html#TauCeti.MappingPathFiber.projFiberHomotopyEquivLoopSpace)
- [Source of `TauCeti.MappingPathFiber.projFiberHomotopyEquivLoopSpace` in TauCeti/Topology/Homotopy/MappingPath/Fiber.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Homotopy/MappingPath/Fiber.lean#L154)
- [Tau Ceti roadmap status: Generalized cohomology, spectra and orientations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeneralizedCohomology/STATUS.md)
