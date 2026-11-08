---
declaration: theorem
origin: cited
lean: TauCeti.IsLocalRing.sum_addVal_smul_sub_eq_finsum_card_ramificationGroup_sub_one
statement: formalized
proof: formalized
---

# Hilbert's counting identity

Let a finite group `G` act faithfully on a discrete valuation
ring `S` generated over a base `R` fixed by `G` by a single element `ξ`. Then the sum over the
nontrivial `σ ∈ G` of the valuations `v (σ • ξ - ξ)` is `∑_{i ≥ 0} (#G_i - 1)`, where `G_i` is
the `i`-th ramification group: each `σ ≠ 1` lies in exactly `v (σ • ξ - ξ)` of the groups
`G_0, G_1, …`, and the sum is finite because the filtration is eventually trivial.

```lean
TauCeti.IsLocalRing.sum_addVal_smul_sub_eq_finsum_card_ramificationGroup_sub_one.{u_1, u_2, u_3}
  {G : Type u_1} [Group G] {S : Type u_2} [CommRing S] [IsDomain S] [IsDiscreteValuationRing S]
  [MulSemiringAction G S] {R : Type u_3} [CommSemiring R] [Algebra R S] [SMulCommClass G R S]
  [Fintype G] [DecidableEq G] [FaithfulSMul G S] {ξ : S} (hξ : R[ξ] = ⊤) :
  ∑ σ ∈ Finset.univ.erase 1, (IsDiscreteValuationRing.addVal S) (σ • ξ - ξ) =
    ↑(∑ᶠ (i : ℕ), (Nat.card ↥(TauCeti.IsLocalRing.ramificationGroup G S ↑i) - 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Serre's criterion](../ideal/serres-criterion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsLocalRing.sum_addVal_smul_sub_eq_finsum_card_ramificationGroup_sub_one`](https://taucetiproject.org/docs/TauCeti/RingTheory/LocalRing/RamificationGroup.html#TauCeti.IsLocalRing.sum_addVal_smul_sub_eq_finsum_card_ramificationGroup_sub_one).

## Sources

- [Tau Ceti documentation: `TauCeti.IsLocalRing.sum_addVal_smul_sub_eq_finsum_card_ramificationGroup_sub_one`](https://taucetiproject.org/docs/TauCeti/RingTheory/LocalRing/RamificationGroup.html#TauCeti.IsLocalRing.sum_addVal_smul_sub_eq_finsum_card_ramificationGroup_sub_one)
- [Source of `TauCeti.IsLocalRing.sum_addVal_smul_sub_eq_finsum_card_ramificationGroup_sub_one` in TauCeti/RingTheory/LocalRing/RamificationGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/LocalRing/RamificationGroup.lean#L464)
