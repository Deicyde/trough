---
declaration: theorem
origin: cited
lean: TauCeti.Sporadic.card_M22
statement: formalized
proof: formalized
---

# The order of `M₂₂`

The permutation model `M22` has `443520 = 22 * 21 * 20 * 16 * 3`
elements: along the base `0, 1, 2, 3, 4` its basic orbits have lengths `22`, `21`, `20`, `16` and
`3`.

```lean
TauCeti.Sporadic.card_M22 : Nat.card ↥TauCeti.Sporadic.M22 = 443520
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The order of a group from sifting checks](the-order-of-a-group-from-sifting-checks.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Sporadic.card_M22`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/TwentyTwo.html#TauCeti.Sporadic.card_M22).

## Sources

- [Tau Ceti documentation: `TauCeti.Sporadic.card_M22`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/TwentyTwo.html#TauCeti.Sporadic.card_M22)
- [Source of `TauCeti.Sporadic.card_M22` in TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/TwentyTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/TwentyTwo.lean#L509)
- [Tau Ceti roadmap status: Orders of the sporadic groups from permutation representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SporadicOrders/STATUS.md)
