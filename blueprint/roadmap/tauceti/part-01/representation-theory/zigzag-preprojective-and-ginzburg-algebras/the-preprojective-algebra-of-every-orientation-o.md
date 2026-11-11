---
declaration: theorem
origin: cited
lean: TauCeti.moduleInjective_preprojectiveAlgebra_of_iso
statement: formalized
proof: formalized
---

# The preprojective algebra of every orientation of a graph isomorphic to a standard Dynkin diagram is left self-injective, over every field

```lean
TauCeti.moduleInjective_preprojectiveAlgebra_of_iso.{u_1, u_2} (k : Type u_1) [Field k]
  {V : Type u_2} [Finite V] {G : SimpleGraph V} {t : TauCeti.DynkinType}
  (e : G ≃g TauCeti.diagramGraph t.cartanMatrix) (o : TauCeti.DoubledQuiver.Orientation G) :
  Module.Injective (TauCeti.preprojectiveAlgebra k (TauCeti.DoubledQuiver.OrientedQuiver G o))
    (TauCeti.preprojectiveAlgebra k (TauCeti.DoubledQuiver.OrientedQuiver G o))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.moduleInjective_preprojectiveAlgebra_of_iso`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Preprojective/ADE/SelfInjective.html#TauCeti.moduleInjective_preprojectiveAlgebra_of_iso).

## Sources

- [Tau Ceti documentation: `TauCeti.moduleInjective_preprojectiveAlgebra_of_iso`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Preprojective/ADE/SelfInjective.html#TauCeti.moduleInjective_preprojectiveAlgebra_of_iso)
- [Source of `TauCeti.moduleInjective_preprojectiveAlgebra_of_iso` in TauCeti/RepresentationTheory/Quiver/Preprojective/ADE/SelfInjective.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Quiver/Preprojective/ADE/SelfInjective.lean#L41)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
