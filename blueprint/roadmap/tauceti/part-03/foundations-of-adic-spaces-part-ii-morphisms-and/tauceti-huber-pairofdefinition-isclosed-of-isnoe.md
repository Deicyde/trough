---
declaration: theorem
origin: cited
lean: TauCeti.Huber.PairOfDefinition.isClosed_of_isNoetherianRing
statement: formalized
proof: formalized
---

# TauCeti.Huber.PairOfDefinition.isClosed_of_isNoetherianRing

**Submodules of finite modules over a complete Huber ring with a noetherian ring of definition
are closed** (Huber, Lemma 2.3(ii)). If `A` is complete and Hausdorff with a noetherian ring of
definition, every `A`-submodule of a finite `A`-module is closed in its natural topology.

```lean
TauCeti.Huber.PairOfDefinition.isClosed_of_isNoetherianRing.{u_1, u_2} {A : Type u_1} [CommRing A]
  {M : Type u_2} [AddCommGroup M] [_root_.Module A M] [UniformSpace A] [IsUniformAddGroup A]
  [CompleteSpace A] [T0Space A] [IsTopologicalRing A] [Module.Finite A M] [TopologicalSpace M]
  [IsModuleTopology A M] (P : TauCeti.Huber.PairOfDefinition A)
  [IsNoetherianRing ↥P.ringOfDefinition] (N : Submodule A M) : IsClosed ↑N
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.PairOfDefinition.isClosed_of_isNoetherianRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/ModuleTopology/Complete.html#TauCeti.Huber.PairOfDefinition.isClosed_of_isNoetherianRing).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.PairOfDefinition.isClosed_of_isNoetherianRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/ModuleTopology/Complete.html#TauCeti.Huber.PairOfDefinition.isClosed_of_isNoetherianRing)
- [Source of `TauCeti.Huber.PairOfDefinition.isClosed_of_isNoetherianRing` in TauCeti/RingTheory/Huber/ModuleTopology/Complete.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Huber/ModuleTopology/Complete.lean#L85)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
