---
declaration: theorem
origin: cited
lean: Representation.sum_eq_finrank_add_card_of_bijective_aeval_symmetricAlgebraInvariants_dual
statement: formalized
proof: formalized
---

# The sum of the degrees of basic polynomial functions counts the pseudoreflections

Let a
finite group act faithfully and linearly on a finite-dimensional vector space `M` over a field of
characteristic zero. If the polynomial functions invariant under the contragredient action,
`Sym(M*)^G`, form a polynomial algebra on invariants `f i` homogeneous of degrees `d i`, then
`∑ d i = dim M + N`, where `N` is the number of pseudoreflections of `G` on `M`. This is
`Representation.sum_eq_finrank_add_card_of_bijective_aeval_symmetricAlgebraInvariants` for
`ρ.dual`, which has the same pseudoreflections as `ρ`.

```lean
Representation.sum_eq_finrank_add_card_of_bijective_aeval_symmetricAlgebraInvariants_dual.{u_1, u_2,
    u_3, u_4}
  {K : Type u_1} {G : Type u_2} {M : Type u_3} [Field K] [Group G] [Fintype G] [AddCommGroup M]
  [_root_.Module K M] [FiniteDimensional K M] (ρ : Representation K G M) [CharZero K] {ι : Type u_4}
  [Fintype ι] {d : ι → ℕ} (hρ : Function.Injective ⇑ρ) {f : ι → ↥ρ.dual.symmetricAlgebraInvariants}
  (hf : ∀ (i : ι), ↑(f i) ∈ TauCeti.SymmetricAlgebra.homogeneousSubmodule K (Module.Dual K M) (d i))
  (hbij : Function.Bijective ⇑(MvPolynomial.aeval f)) :
  ∑ i, d i = Module.finrank K M + {g | Module.finrank K (M ⧸ (ρ g).fixedSubmodule) = 1}.card
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Molien's formula](../symmetric-algebra/moliens-formula.md)

## Lean

Formalized in Tau Ceti as [`Representation.sum_eq_finrank_add_card_of_bijective_aeval_symmetricAlgebraInvariants_dual`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/ProductOfDegrees.html#Representation.sum_eq_finrank_add_card_of_bijective_aeval_symmetricAlgebraInvariants_dual).

## Sources

- [Tau Ceti documentation: `Representation.sum_eq_finrank_add_card_of_bijective_aeval_symmetricAlgebraInvariants_dual`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/ProductOfDegrees.html#Representation.sum_eq_finrank_add_card_of_bijective_aeval_symmetricAlgebraInvariants_dual)
- [Source of `Representation.sum_eq_finrank_add_card_of_bijective_aeval_symmetricAlgebraInvariants_dual` in TauCeti/RepresentationTheory/SymmetricAlgebra/ProductOfDegrees.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/SymmetricAlgebra/ProductOfDegrees.lean#L423)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
