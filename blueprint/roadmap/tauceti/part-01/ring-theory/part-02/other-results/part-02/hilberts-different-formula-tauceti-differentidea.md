---
declaration: theorem
origin: cited
lean: TauCeti.differentIdeal_eq_pow_maximalIdeal_of_separable_residue, TauCeti.differentIdeal_eq_pow_maximalIdeal_of_adjoin_eq_top
statement: formalized
proof: formalized
---

# Hilbert's different formula (`TauCeti.differentIdeal_eq_pow_maximalIdeal_of_separable_residue`)

For a faithful finite group action on DVRs with invariants
`A` and separable residue extension, the different ideal is the power of the maximal ideal with
exponent `∑ᶠ i : ℕ, (#G_i - 1)`. Neither completeness nor a finite residue field is assumed.

```lean
TauCeti.differentIdeal_eq_pow_maximalIdeal_of_separable_residue.{u_1, u_2, u_3} (A : Type u_1)
  (B : Type u_2) [CommRing A] [IsDomain A] [CommRing B] [IsDomain B] [IsDiscreteValuationRing B]
  [Algebra A B] [FaithfulSMul A B] (G : Type u_3) [Group G] [Finite G] [MulSemiringAction G B]
  [SMulCommClass G A B] [Algebra.IsInvariant A B G] [FaithfulSMul G B] [IsDiscreteValuationRing A]
  [IsLocalHom (algebraMap A B)]
  [Algebra.IsSeparable (IsLocalRing.ResidueField A) (IsLocalRing.ResidueField B)] :
  differentIdeal A B =
    IsLocalRing.maximalIdeal B ^
      ∑ᶠ (i : ℕ), (Nat.card ↥(TauCeti.IsLocalRing.ramificationGroup G B ↑i) - 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hilbert's counting identity](../../../part-01/local-ring/hilberts-counting-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.differentIdeal_eq_pow_maximalIdeal_of_separable_residue`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/Different.html#TauCeti.differentIdeal_eq_pow_maximalIdeal_of_separable_residue).

## Other forms

**Hilbert's different formula for a monogenic DVR over an integrally closed domain.** Formalized in Tau Ceti as [`TauCeti.differentIdeal_eq_pow_maximalIdeal_of_adjoin_eq_top`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/Different.html#TauCeti.differentIdeal_eq_pow_maximalIdeal_of_adjoin_eq_top).

```lean
TauCeti.differentIdeal_eq_pow_maximalIdeal_of_adjoin_eq_top.{u_1, u_2, u_3} (A : Type u_1)
  (B : Type u_2) [CommRing A] [IsDomain A] [IsIntegrallyClosed A] [CommRing B] [IsDomain B]
  [IsDiscreteValuationRing B] [Algebra A B] [FaithfulSMul A B] (G : Type u_3) [Group G] [Finite G]
  [MulSemiringAction G B] [SMulCommClass G A B] [Algebra.IsInvariant A B G] [FaithfulSMul G B]
  {x : B} (hx : A[x] = ⊤) :
  differentIdeal A B =
    IsLocalRing.maximalIdeal B ^
      ∑ᶠ (i : ℕ), (Nat.card ↥(TauCeti.IsLocalRing.ramificationGroup G B ↑i) - 1)
```

## Sources

- [Tau Ceti documentation: `TauCeti.differentIdeal_eq_pow_maximalIdeal_of_separable_residue`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/Different.html#TauCeti.differentIdeal_eq_pow_maximalIdeal_of_separable_residue)
- [Source of `TauCeti.differentIdeal_eq_pow_maximalIdeal_of_separable_residue` in TauCeti/RingTheory/DiscreteValuationRing/Different.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/DiscreteValuationRing/Different.lean#L76)
