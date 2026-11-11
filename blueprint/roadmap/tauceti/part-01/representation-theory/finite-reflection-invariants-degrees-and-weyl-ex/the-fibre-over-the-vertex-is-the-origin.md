---
declaration: theorem
origin: cited
lean: Representation.forall_homogeneous_mem_symmetricAlgebraInvariants_lift_eval_eq_zero_iff
statement: formalized
proof: formalized
---

# The fibre over the vertex is the origin

Every homogeneous invariant polynomial function
of positive degree vanishes at `v` exactly when `v = 0`.

```lean
Representation.forall_homogeneous_mem_symmetricAlgebraInvariants_lift_eval_eq_zero_iff.{u_1, u_2,
    u_3}
  {K : Type u_1} {G : Type u_2} {V : Type u_3} [Field K] [Group G] [Finite G] [AddCommGroup V]
  [_root_.Module K V] (ρ : Representation K G V) {v : V} :
  (∀ (n : ℕ),
      0 < n →
        ∀ p ∈ ρ.dual.symmetricAlgebraInvariants,
          p ∈ TauCeti.SymmetricAlgebra.homogeneousSubmodule K (Module.Dual K V) n →
            (SymmetricAlgebra.lift ((Module.Dual.eval K V) v)) p = 0) ↔
    v = 0
```

## Depends on

- [Representation.symmetricAlgebraInvariants](representation-symmetricalgebrainvariants.md)

## Proof depends on

- [Invariant polynomials detect orbits](invariant-polynomials-detect-orbits.md)

## Lean

Formalized in Tau Ceti as [`Representation.forall_homogeneous_mem_symmetricAlgebraInvariants_lift_eval_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/OrbitSeparation.html#Representation.forall_homogeneous_mem_symmetricAlgebraInvariants_lift_eval_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `Representation.forall_homogeneous_mem_symmetricAlgebraInvariants_lift_eval_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/OrbitSeparation.html#Representation.forall_homogeneous_mem_symmetricAlgebraInvariants_lift_eval_eq_zero_iff)
- [Source of `Representation.forall_homogeneous_mem_symmetricAlgebraInvariants_lift_eval_eq_zero_iff` in TauCeti/RepresentationTheory/SymmetricAlgebra/OrbitSeparation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/SymmetricAlgebra/OrbitSeparation.lean#L115)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
