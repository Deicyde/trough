---
declaration: theorem
origin: cited
lean: TauCeti.IsProP.surjective_of_forall_inv_mul_mem_pLowerCentralSeries_one
statement: formalized
proof: formalized
---

# Burnside's criterion modulo `λ_1`

A continuous endomorphism of a pro-`p` group congruent
to the identity modulo `λ_1 = Φ` is surjective.

```lean
TauCeti.IsProP.surjective_of_forall_inv_mul_mem_pLowerCentralSeries_one.{u_1} {p : ℕ} {G : Type u_1}
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] [Fact (Nat.Prime p)] (hG : TauCeti.IsProP p G) {φ : G →* G}
  (hφ : Continuous ⇑φ) (h : ∀ (g : G), g⁻¹ * φ g ∈ TauCeti.pLowerCentralSeries p G 1) :
  Function.Surjective ⇑φ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.surjective_of_forall_inv_mul_mem_pLowerCentralSeries_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/LowerCentralSeries.html#TauCeti.IsProP.surjective_of_forall_inv_mul_mem_pLowerCentralSeries_one).

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.surjective_of_forall_inv_mul_mem_pLowerCentralSeries_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/LowerCentralSeries.html#TauCeti.IsProP.surjective_of_forall_inv_mul_mem_pLowerCentralSeries_one)
- [Source of `TauCeti.IsProP.surjective_of_forall_inv_mul_mem_pLowerCentralSeries_one` in TauCeti/Topology/Algebra/Group/Profinite/ProP/LowerCentralSeries.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/Profinite/ProP/LowerCentralSeries.lean#L167)
