---
declaration: theorem
origin: cited
lean: Representation.forall_mem_symmetricAlgebraInvariants_lift_eval_eq_iff
statement: formalized
proof: formalized
---

# Invariant polynomials detect orbits

Two vectors have the same value on every invariant
polynomial function exactly when they lie in the same orbit.

```lean
Representation.forall_mem_symmetricAlgebraInvariants_lift_eval_eq_iff.{u_1, u_2, u_3} {K : Type u_1}
  {G : Type u_2} {V : Type u_3} [Field K] [Group G] [Finite G] [AddCommGroup V] [_root_.Module K V]
  (ρ : Representation K G V) {v w : V} :
  (∀ p ∈ ρ.dual.symmetricAlgebraInvariants,
      (SymmetricAlgebra.lift ((Module.Dual.eval K V) v)) p =
        (SymmetricAlgebra.lift ((Module.Dual.eval K V) w)) p) ↔
    ∃ g, (ρ g) v = w
```

## Depends on

- [Representation.symmetricAlgebraInvariants](representation-symmetricalgebrainvariants.md)

## Lean

Formalized in Tau Ceti as [`Representation.forall_mem_symmetricAlgebraInvariants_lift_eval_eq_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/OrbitSeparation.html#Representation.forall_mem_symmetricAlgebraInvariants_lift_eval_eq_iff).

## Sources

- [Tau Ceti documentation: `Representation.forall_mem_symmetricAlgebraInvariants_lift_eval_eq_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/OrbitSeparation.html#Representation.forall_mem_symmetricAlgebraInvariants_lift_eval_eq_iff)
- [Source of `Representation.forall_mem_symmetricAlgebraInvariants_lift_eval_eq_iff` in TauCeti/RepresentationTheory/SymmetricAlgebra/OrbitSeparation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/SymmetricAlgebra/OrbitSeparation.lean#L98)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
