---
declaration: theorem
origin: cited
lean: TauCeti.Sporadic.card_M11
statement: formalized
proof: formalized
---

# The order of `M₁₁`

The permutation model `M11` has `7920 = 11 * 10 * 9 * 8` elements: along
the base `0, 1, 2, 3` its basic orbits have lengths `11`, `10`, `9` and `8`.

```lean
TauCeti.Sporadic.card_M11 : Nat.card ↥TauCeti.Sporadic.M11 = 7920
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The order of a group from sifting checks](the-order-of-a-group-from-sifting-checks.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Sporadic.card_M11`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/Eleven.html#TauCeti.Sporadic.card_M11).

## Sources

- [Tau Ceti documentation: `TauCeti.Sporadic.card_M11`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/Eleven.html#TauCeti.Sporadic.card_M11)
- [Source of `TauCeti.Sporadic.card_M11` in TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/Eleven.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/Eleven.lean#L381)
- [Tau Ceti roadmap status: Orders of the sporadic groups from permutation representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SporadicOrders/STATUS.md)
