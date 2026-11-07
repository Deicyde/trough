---
declaration: theorem
origin: cited
lean: TauCeti.exists_finset_card_smul_symmDiff_lt_of_sum_tsum_lt
statement: formalized
proof: formalized
---

# Reiter implies Følner

If a nonnegative finitely supported function `p` on `X` satisfies
`∑_{g ∈ K} ∑_x |p (g⁻¹ • x) - p x| < ε · ∑_x p x`, then some finite nonempty set `F ⊆ X` satisfies
`|g • F ∆ F| < ε |F|` for every `g ∈ K`.

```lean
TauCeti.exists_finset_card_smul_symmDiff_lt_of_sum_tsum_lt.{u_1, u_2} {G : Type u_1} {X : Type u_2}
  [Group G] [MulAction G X] [DecidableEq X] {p : X → ℝ} (hp : 0 ≤ p)
  (hfin : Function.HasFiniteSupport p) {K : Finset G} {ε : ℝ}
  (h : ∑ g ∈ K, ∑' (x : X), |p (g⁻¹ • x) - p x| < ε * ∑' (x : X), p x) :
  ∃ F, F.Nonempty ∧ ∀ g ∈ K, ↑(symmDiff (g • F) F).card < ε * ↑F.card
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_finset_card_smul_symmDiff_lt_of_sum_tsum_lt`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Reiter.html#TauCeti.exists_finset_card_smul_symmDiff_lt_of_sum_tsum_lt).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_finset_card_smul_symmDiff_lt_of_sum_tsum_lt`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Reiter.html#TauCeti.exists_finset_card_smul_symmDiff_lt_of_sum_tsum_lt)
- [Source of `TauCeti.exists_finset_card_smul_symmDiff_lt_of_sum_tsum_lt` in TauCeti/GroupTheory/Amenable/Reiter.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Amenable/Reiter.lean#L153)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AmenableGroups/STATUS.md)
