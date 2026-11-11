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
- [Source of `TauCeti.Sporadic.card_M11` in TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/Eleven.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/Eleven.lean#L381)
- [Tau Ceti roadmap status: Orders of the sporadic groups from permutation representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SporadicOrders/STATUS.md)
