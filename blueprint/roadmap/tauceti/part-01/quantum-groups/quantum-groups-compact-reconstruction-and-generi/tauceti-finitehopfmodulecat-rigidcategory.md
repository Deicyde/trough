---
declaration: def
origin: cited
lean: TauCeti.FiniteHopfModuleCat.rigidCategory
statement: formalized
---

# TauCeti.FiniteHopfModuleCat.rigidCategory

Finite-dimensional modules over a Hopf algebra with bijective antipode form a rigid monoidal
category. The left dual of `M` is its inverse-antipode contragredient `leftDual hS M`, with
evaluation `leftDualEvaluation` and coevaluation `leftDualCoevaluation`. The right duals are the
contragredients of `instRightRigidCategory`. Not an instance, as the left duals depend on the
explicit bijectivity hypothesis `hS`.

```lean
TauCeti.FiniteHopfModuleCat.rigidCategory.{u, v} {k : Type u} [Field k] {H : Type v} [Ring H]
  [HopfAlgebra k H] (hS : Function.Bijective ⇑(HopfAlgebraStruct.antipode k)) :
  CategoryTheory.RigidCategory (TauCeti.FiniteHopfModuleCat k H)
```

## Depends on

- [TauCeti.FiniteHopfModuleCat](tauceti-finitehopfmodulecat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteHopfModuleCat.rigidCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FiniteHopfModuleCat/Rigid.html#TauCeti.FiniteHopfModuleCat.rigidCategory).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteHopfModuleCat.rigidCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FiniteHopfModuleCat/Rigid.html#TauCeti.FiniteHopfModuleCat.rigidCategory)
- [Source of `TauCeti.FiniteHopfModuleCat.rigidCategory` in TauCeti/Algebra/Category/FiniteHopfModuleCat/Rigid.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Category/FiniteHopfModuleCat/Rigid.lean#L140)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuantumGroups/STATUS.md)
