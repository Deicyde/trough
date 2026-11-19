---
declaration: theorem
origin: cited
lean: Representation.prod_eq_card_of_bijective_aeval_symmetricAlgebraInvariants
statement: formalized
proof: formalized
---

# The product of the degrees of basic invariants is the order of the group

Let a finite
group act faithfully and linearly on a finite-dimensional vector space `M` over a field of
characteristic zero. If the invariant subalgebra `Sym(M)^G` is a polynomial algebra on invariants
`f i` homogeneous of degrees `d i`, then `∏ d i = #G`.

```lean
Representation.prod_eq_card_of_bijective_aeval_symmetricAlgebraInvariants.{u_1, u_2, u_3, u_4}
  {K : Type u_1} {G : Type u_2} {M : Type u_3} [Field K] [Group G] [Fintype G] [AddCommGroup M]
  [_root_.Module K M] [FiniteDimensional K M] (ρ : Representation K G M) [CharZero K] {ι : Type u_4}
  [Fintype ι] {d : ι → ℕ} {f : ι → ↥ρ.symmetricAlgebraInvariants} (hρ : Function.Injective ⇑ρ)
  (hf : ∀ (i : ι), ↑(f i) ∈ TauCeti.SymmetricAlgebra.homogeneousSubmodule K M (d i))
  (hbij : Function.Bijective ⇑(MvPolynomial.aeval f)) : ∏ i, d i = Fintype.card G
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Molien's formula](../symmetric-algebra/moliens-formula.md)

## Lean

Formalized in Tau Ceti as [`Representation.prod_eq_card_of_bijective_aeval_symmetricAlgebraInvariants`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/ProductOfDegrees.html#Representation.prod_eq_card_of_bijective_aeval_symmetricAlgebraInvariants).

## Sources

- [Tau Ceti documentation: `Representation.prod_eq_card_of_bijective_aeval_symmetricAlgebraInvariants`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/ProductOfDegrees.html#Representation.prod_eq_card_of_bijective_aeval_symmetricAlgebraInvariants)
- [Source of `Representation.prod_eq_card_of_bijective_aeval_symmetricAlgebraInvariants` in TauCeti/RepresentationTheory/SymmetricAlgebra/ProductOfDegrees.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/SymmetricAlgebra/ProductOfDegrees.lean#L381)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
