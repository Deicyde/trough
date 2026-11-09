---
declaration: def
origin: cited
lean: TauCeti.directSumIsotypicTensorEquiv
statement: formalized
---

# The isotypic decomposition of a semisimple module

Let `S j` be pairwise non-isomorphic
simple modules, finite-dimensional over the algebraically closed field `k`, such that every simple
submodule of the semisimple module `M` is isomorphic to one of them. Then evaluation
`s ⊗ f ↦ f s` is an isomorphism `⨁ⱼ S j ⊗[k] (S j →ₗ[A] M) ≃ M` of `A`-modules.

```lean
TauCeti.directSumIsotypicTensorEquiv.{u_1, u_2, u_3, u_4, u_5} (k : Type u_1) {A : Type u_2}
  [Field k] [IsAlgClosed k] [Ring A] [Algebra k A] {κ : Type u_3} [DecidableEq κ] (S : κ → Type u_4)
  [(j : κ) → AddCommGroup (S j)] [(j : κ) → _root_.Module k (S j)] [(j : κ) → _root_.Module A (S j)]
  [∀ (j : κ), IsScalarTower k A (S j)] [∀ (j : κ), IsSimpleModule A (S j)]
  [∀ (j : κ), FiniteDimensional k (S j)] {M : Type u_5} [AddCommGroup M] [_root_.Module k M]
  [_root_.Module A M] [IsScalarTower k A M] [IsSemisimpleModule A M]
  (hS : ∀ (i j : κ), Nonempty (S i ≃ₗ[A] S j) → i = j)
  (hcover : ∀ (m : Submodule A M), IsSimpleModule A ↥m → ∃ j, Nonempty (S j ≃ₗ[A] ↥m)) :
  (Π₀ (j : κ), TensorProduct k (S j) (S j →ₗ[A] M)) ≃ₗ[A] M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The multiplicity theorem](../../ring-theory/part-02/semisimple/the-multiplicity-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.directSumIsotypicTensorEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Semisimple/IsotypicTensor.html#TauCeti.directSumIsotypicTensorEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.directSumIsotypicTensorEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Semisimple/IsotypicTensor.html#TauCeti.directSumIsotypicTensorEquiv)
- [Source of `TauCeti.directSumIsotypicTensorEquiv` in TauCeti/RingTheory/Semisimple/IsotypicTensor.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Semisimple/IsotypicTensor.lean#L358)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuantumGroups/STATUS.md)
