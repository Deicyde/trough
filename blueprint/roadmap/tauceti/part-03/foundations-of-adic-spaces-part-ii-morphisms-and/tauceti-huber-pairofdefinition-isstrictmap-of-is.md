---
declaration: theorem
origin: cited
lean: TauCeti.Huber.PairOfDefinition.isStrictMap_of_isNoetherianRing
statement: formalized
proof: formalized
---

# TauCeti.Huber.PairOfDefinition.isStrictMap\_of\_isNoetherianRing

**Linear maps of finite modules over a Huber ring with a noetherian ring of definition are
strict** (Huber, Lemma 2.3(i)). If `A₀` is noetherian, every `A`-linear map between finitely
generated `A`-modules with their natural topologies is continuous and open onto its image.

```lean
TauCeti.Huber.PairOfDefinition.isStrictMap_of_isNoetherianRing.{u_1, u_2, u_3} {A : Type u_1}
  [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] {M : Type u_2} [AddCommGroup M]
  [_root_.Module A M] [Module.Finite A M] [TopologicalSpace M] [IsModuleTopology A M] {N : Type u_3}
  [AddCommGroup N] [_root_.Module A N] [Module.Finite A N] [TopologicalSpace N]
  [IsModuleTopology A N] (P : TauCeti.Huber.PairOfDefinition A)
  [IsNoetherianRing ↥P.ringOfDefinition] (u : M →ₗ[A] N) : Topology.IsStrictMap ⇑u
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.PairOfDefinition.isStrictMap_of_isNoetherianRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/ModuleTopology/Strict.html#TauCeti.Huber.PairOfDefinition.isStrictMap_of_isNoetherianRing).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.PairOfDefinition.isStrictMap_of_isNoetherianRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/ModuleTopology/Strict.html#TauCeti.Huber.PairOfDefinition.isStrictMap_of_isNoetherianRing)
- [Source of `TauCeti.Huber.PairOfDefinition.isStrictMap_of_isNoetherianRing` in TauCeti/RingTheory/Huber/ModuleTopology/Strict.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Huber/ModuleTopology/Strict.lean#L53)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
