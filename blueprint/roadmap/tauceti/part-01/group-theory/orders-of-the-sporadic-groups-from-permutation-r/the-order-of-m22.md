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

Formalized in Tau Ceti as [`TauCeti.Sporadic.card_M22`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/TwentyTwo/Basic.html#TauCeti.Sporadic.card_M22).

## Sources

- [Tau Ceti documentation: `TauCeti.Sporadic.card_M22`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/TwentyTwo/Basic.html#TauCeti.Sporadic.card_M22)
- [Source of `TauCeti.Sporadic.card_M22` in TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/TwentyTwo/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/SpecificGroups/Sporadic/Mathieu/TwentyTwo/Basic.lean#L539)
- [Tau Ceti roadmap status: Orders of the sporadic groups from permutation representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SporadicOrders/STATUS.md)
