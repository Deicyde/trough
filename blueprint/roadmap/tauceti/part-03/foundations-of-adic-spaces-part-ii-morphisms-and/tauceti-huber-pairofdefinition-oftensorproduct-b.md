---
declaration: theorem
origin: cited
lean: TauCeti.Huber.PairOfDefinition.ofTensorProduct_bijective
statement: formalized
proof: formalized
---

# TauCeti.Huber.PairOfDefinition.ofTensorProduct_bijective

**Completion of a finite module is base change to the completed ring** (Huber, Lemma
2.3(iii)). If `A` is a Huber ring with a noetherian ring of definition and `M` is a finitely
generated `A`-module with its natural topology, the canonical map `Â ⊗[A] M → M̂` is bijective.

```lean
TauCeti.Huber.PairOfDefinition.ofTensorProduct_bijective.{u_1, u_2} {A : Type u_1} [CommRing A]
  [UniformSpace A] [IsUniformAddGroup A] [IsTopologicalRing A] {M : Type u_2} [AddCommGroup M]
  [_root_.Module A M] [Module.Finite A M] [UniformSpace M] [IsUniformAddGroup M]
  [IsModuleTopology A M] [UniformContinuousConstSMul A M] (P : TauCeti.Huber.PairOfDefinition A)
  [IsNoetherianRing ↥P.ringOfDefinition] :
  Function.Bijective ⇑(UniformSpace.Completion.ofTensorProduct A M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Noetherianity of complete rings](noetherianity-of-complete-rings.md)
- [TauCeti.Huber.PairOfDefinition.isClosed_of_isNoetherianRing](tauceti-huber-pairofdefinition-isclosed-of-isnoe.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.PairOfDefinition.ofTensorProduct_bijective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/ModuleTopology/Completion.html#TauCeti.Huber.PairOfDefinition.ofTensorProduct_bijective).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.PairOfDefinition.ofTensorProduct_bijective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/ModuleTopology/Completion.html#TauCeti.Huber.PairOfDefinition.ofTensorProduct_bijective)
- [Source of `TauCeti.Huber.PairOfDefinition.ofTensorProduct_bijective` in TauCeti/RingTheory/Huber/ModuleTopology/Completion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Huber/ModuleTopology/Completion.lean#L186)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
