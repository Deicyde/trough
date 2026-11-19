---
declaration: theorem
origin: cited
lean: Representation.map_univ_eq_of_bijective_aeval_symmetricAlgebraInvariants
statement: formalized
proof: formalized
---

# The degrees of basic invariants are intrinsic

Two systems of basic invariants, that is,
two families of homogeneous invariants on which the invariant subalgebra is a polynomial algebra,
have the same multiset of degrees.

```lean
Representation.map_univ_eq_of_bijective_aeval_symmetricAlgebraInvariants.{u_1, u_3, u_4, u_5, u_6}
  {R : Type u_1} {G : Type u_3} {M : Type u_4} {ι : Type u_5} {κ : Type u_6} [CommRing R] [Monoid G]
  [AddCommMonoid M] [_root_.Module R M] (ρ : Representation R G M)
  {f : ι → ↥ρ.symmetricAlgebraInvariants} {d : ι → ℕ} [Nontrivial R] [Fintype ι] [Fintype κ]
  {f' : κ → ↥ρ.symmetricAlgebraInvariants} {d' : κ → ℕ}
  (hf : ∀ (i : ι), ↑(f i) ∈ TauCeti.SymmetricAlgebra.homogeneousSubmodule R M (d i))
  (hbij : Function.Bijective ⇑(MvPolynomial.aeval f))
  (hf' : ∀ (j : κ), ↑(f' j) ∈ TauCeti.SymmetricAlgebra.homogeneousSubmodule R M (d' j))
  (hbij' : Function.Bijective ⇑(MvPolynomial.aeval f')) :
  Multiset.map d Finset.univ.val = Multiset.map d' Finset.univ.val
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Representation.map_univ_eq_of_bijective_aeval_symmetricAlgebraInvariants`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/Degrees.html#Representation.map_univ_eq_of_bijective_aeval_symmetricAlgebraInvariants).

## Sources

- [Tau Ceti documentation: `Representation.map_univ_eq_of_bijective_aeval_symmetricAlgebraInvariants`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/Degrees.html#Representation.map_univ_eq_of_bijective_aeval_symmetricAlgebraInvariants)
- [Source of `Representation.map_univ_eq_of_bijective_aeval_symmetricAlgebraInvariants` in TauCeti/RepresentationTheory/SymmetricAlgebra/Degrees.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/SymmetricAlgebra/Degrees.lean#L131)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
