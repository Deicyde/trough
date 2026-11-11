---
declaration: def
origin: cited
lean: TauCeti.Huber.PairOfDefinition.completionTensorHomeomorph
statement: formalized
---

# Completion of a finite module is completed scalar extension, as a topological `Â`-module (Huber, Lemma 2.3(iii))

The tensor product has its natural `Â`-module topology.

```lean
TauCeti.Huber.PairOfDefinition.completionTensorHomeomorph.{u_1, u_2} {A : Type u_1} [CommRing A]
  [UniformSpace A] [IsUniformAddGroup A] [IsTopologicalRing A] {M : Type u_2} [AddCommGroup M]
  [_root_.Module A M] [Module.Finite A M] [UniformSpace M] [IsUniformAddGroup M]
  [IsModuleTopology A M] [UniformContinuousConstSMul A M] (P : TauCeti.Huber.PairOfDefinition A)
  [IsNoetherianRing ↥P.ringOfDefinition]
  [TopologicalSpace (TensorProduct A (UniformSpace.Completion A) M)]
  [IsModuleTopology (UniformSpace.Completion A) (TensorProduct A (UniformSpace.Completion A) M)] :
  TensorProduct A (UniformSpace.Completion A) M ≃L[UniformSpace.Completion A]
    UniformSpace.Completion M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.PairOfDefinition.completionTensorHomeomorph`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/ModuleTopology/CompletedScalars.html#TauCeti.Huber.PairOfDefinition.completionTensorHomeomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.PairOfDefinition.completionTensorHomeomorph`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/ModuleTopology/CompletedScalars.html#TauCeti.Huber.PairOfDefinition.completionTensorHomeomorph)
- [Source of `TauCeti.Huber.PairOfDefinition.completionTensorHomeomorph` in TauCeti/RingTheory/Huber/ModuleTopology/CompletedScalars.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Huber/ModuleTopology/CompletedScalars.lean#L107)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
