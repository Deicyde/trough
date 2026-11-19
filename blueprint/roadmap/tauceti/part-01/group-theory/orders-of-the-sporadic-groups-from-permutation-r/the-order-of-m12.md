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

Formalized in Tau Ceti as [`TauCeti.Sporadic.card_M12`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/Twelve/Basic.html#TauCeti.Sporadic.card_M12).

## Sources

- [Tau Ceti documentation: `TauCeti.Sporadic.card_M12`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/Twelve/Basic.html#TauCeti.Sporadic.card_M12)
- [Source of `TauCeti.Sporadic.card_M12` in TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/Twelve/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/Twelve/Basic.lean#L458)
- [Tau Ceti roadmap status: Orders of the sporadic groups from permutation representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SporadicOrders/STATUS.md)
