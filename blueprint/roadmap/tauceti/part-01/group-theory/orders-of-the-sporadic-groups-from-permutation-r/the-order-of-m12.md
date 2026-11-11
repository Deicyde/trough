---
declaration: theorem
origin: cited
lean: TauCeti.Sporadic.card_M12
statement: formalized
proof: formalized
---

# The order of `M₁₂`

The permutation model `M12` has `95040 = 12 * 11 * 10 * 9 * 8`
elements: along the base `0, 1, 2, 3, 4` its basic orbits have lengths `12`, `11`, `10`, `9` and
`8`.

```lean
TauCeti.Sporadic.card_M12 : Nat.card ↥TauCeti.Sporadic.M12 = 95040
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The order of a group from sifting checks](the-order-of-a-group-from-sifting-checks.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Sporadic.card_M12`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/Twelve.html#TauCeti.Sporadic.card_M12).

## Sources

- [Tau Ceti documentation: `TauCeti.Sporadic.card_M12`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/Twelve.html#TauCeti.Sporadic.card_M12)
- [Source of `TauCeti.Sporadic.card_M12` in TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/Twelve.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/Twelve.lean#L458)
- [Tau Ceti roadmap status: Orders of the sporadic groups from permutation representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SporadicOrders/STATUS.md)
