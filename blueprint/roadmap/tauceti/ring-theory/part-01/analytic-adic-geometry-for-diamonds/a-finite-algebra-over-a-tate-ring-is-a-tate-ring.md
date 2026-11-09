---
declaration: theorem
origin: cited
lean: TauCeti.Huber.IsTateRing.of_isModuleTopology
statement: formalized
proof: formalized
---

# A finite algebra over a Tate ring is a Tate ring

If `B` is a commutative `A`-algebra,
finite as an `A`-module and carrying its natural topology, then `B` is a Tate ring; the image of a
pseudouniformiser of `A` is a pseudouniformiser of `B`.

```lean
TauCeti.Huber.IsTateRing.of_isModuleTopology.{u_1, u_2} {A : Type u_1} [CommRing A]
  [TopologicalSpace A] {B : Type u_2} [CommRing B] [Algebra A B] [IsTopologicalRing A]
  [TopologicalSpace B] [IsModuleTopology A B] [Module.Finite A B] [TauCeti.Huber.IsTateRing A] :
  TauCeti.Huber.IsTateRing B
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.IsTateRing.of_isModuleTopology`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/ModuleTopology/FiniteAlgebra.html#TauCeti.Huber.IsTateRing.of_isModuleTopology).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.IsTateRing.of_isModuleTopology`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/ModuleTopology/FiniteAlgebra.html#TauCeti.Huber.IsTateRing.of_isModuleTopology)
- [Source of `TauCeti.Huber.IsTateRing.of_isModuleTopology` in TauCeti/RingTheory/Huber/ModuleTopology/FiniteAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Huber/ModuleTopology/FiniteAlgebra.lean#L134)
- [Tau Ceti roadmap status: Analytic adic geometry for diamonds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicEtaleGeometry/STATUS.md)
