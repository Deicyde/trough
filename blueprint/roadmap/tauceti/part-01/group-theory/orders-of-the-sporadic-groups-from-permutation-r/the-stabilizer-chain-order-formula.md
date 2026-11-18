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
- [Source of `Subgroup.prod_ncard_orbit_mul_card_stabilizerChain` in TauCeti/GroupTheory/GroupAction/Stabilizer/Chain.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/GroupAction/Stabilizer/Chain.lean#L134)
- [Tau Ceti roadmap status: Orders of the sporadic groups from permutation representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SporadicOrders/STATUS.md)
