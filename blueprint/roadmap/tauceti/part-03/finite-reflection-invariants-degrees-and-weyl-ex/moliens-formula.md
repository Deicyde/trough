---
declaration: theorem
origin: cited
lean: Representation.mk_finrank_symmetricAlgebraInvariants_inf_homogeneousSubmodule_eq_sum_inv_reverse_charpoly
statement: formalized
proof: formalized
---

# Molien's formula

the image in `K⟦X⟧` of the Hilbert series of the invariant subalgebra
is the average over the group of the inverses of `det(1 - t g | M)`, the reverse of the
characteristic polynomial of `ρ g`:
`Hilb(Sym(M)^G, t) = #G⁻¹ ∑_{g ∈ G} det(1 - t g | M)⁻¹`.

The field `K` is arbitrary, subject only to `#G` being invertible in it; in characteristic zero
this determines the Hilbert series.

```lean
Representation.mk_finrank_symmetricAlgebraInvariants_inf_homogeneousSubmodule_eq_sum_inv_reverse_charpoly.{u_1,
    u_2, u_3}
  {K : Type u_1} {G : Type u_2} {M : Type u_3} [Field K] [Group G] [AddCommGroup M]
  [_root_.Module K M] [FiniteDimensional K M] (ρ : Representation K G M) [Fintype G]
  [Invertible ↑(Fintype.card G)] :
  (PowerSeries.mk fun n =>
      ↑(Module.finrank K
          ↥(Subalgebra.toSubmodule ρ.symmetricAlgebraInvariants ⊓
              TauCeti.SymmetricAlgebra.homogeneousSubmodule K M n))) =
    ⅟↑(Fintype.card G) • ∑ g, (↑(ρ g).charpoly.reverse)⁻¹
```

## Depends on

- [Representation.symmetricAlgebraInvariants](representation-symmetricalgebrainvariants.md)

## Proof depends on

- [Module.End.mk_trace_homogeneousSubmoduleMapₛₗ_mul_reverse_charpoly_of_pow_eq_one](module-end-mk-trace-homogeneoussubmodulemapsl-mu.md)

## Lean

Formalized in Tau Ceti as [`Representation.mk_finrank_symmetricAlgebraInvariants_inf_homogeneousSubmodule_eq_sum_inv_reverse_charpoly`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/Molien.html#Representation.mk_finrank_symmetricAlgebraInvariants_inf_homogeneousSubmodule_eq_sum_inv_reverse_charpoly).

## Sources

- [Tau Ceti documentation: `Representation.mk_finrank_symmetricAlgebraInvariants_inf_homogeneousSubmodule_eq_sum_inv_reverse_charpoly`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/Molien.html#Representation.mk_finrank_symmetricAlgebraInvariants_inf_homogeneousSubmodule_eq_sum_inv_reverse_charpoly)
- [Source of `Representation.mk_finrank_symmetricAlgebraInvariants_inf_homogeneousSubmodule_eq_sum_inv_reverse_charpoly` in TauCeti/RepresentationTheory/SymmetricAlgebra/Molien.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/SymmetricAlgebra/Molien.lean#L132)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
