---
declaration: theorem
origin: cited
lean: Subgroup.prod_ncard_orbit_mul_card_stabilizerChain
statement: formalized
proof: formalized
---

# The stabilizer-chain order formula

The order of `H` is the product of the lengths of the
first `k` basic orbits times the order of the `k`-th member of the chain. No finiteness is
needed: when `H` is infinite, both sides are `0`.

```lean
Subgroup.prod_ncard_orbit_mul_card_stabilizerChain.{u_1, u_2} {G : Type u_1} {α : Type u_2}
  [Group G] [MulAction G α] (H : Subgroup G) (b : ℕ → α) (k : ℕ) :
  (∏ i ∈ Finset.range k, (MulAction.orbit (↥(H.stabilizerChain b i)) (b i)).ncard) *
      Nat.card ↥(H.stabilizerChain b k) =
    Nat.card ↥H
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Subgroup.prod_ncard_orbit_mul_card_stabilizerChain`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAction/Stabilizer/Chain.html#Subgroup.prod_ncard_orbit_mul_card_stabilizerChain).

## Sources

- [Tau Ceti documentation: `Subgroup.prod_ncard_orbit_mul_card_stabilizerChain`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAction/Stabilizer/Chain.html#Subgroup.prod_ncard_orbit_mul_card_stabilizerChain)
- [Source of `Subgroup.prod_ncard_orbit_mul_card_stabilizerChain` in TauCeti/GroupTheory/GroupAction/Stabilizer/Chain.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/GroupAction/Stabilizer/Chain.lean#L116)
- [Tau Ceti roadmap status: Orders of the sporadic groups from permutation representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SporadicOrders/STATUS.md)
