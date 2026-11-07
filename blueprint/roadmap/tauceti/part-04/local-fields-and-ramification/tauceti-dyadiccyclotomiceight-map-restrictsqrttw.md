---
declaration: theorem
origin: cited
lean: TauCeti.DyadicCyclotomicEight.map_restrictSqrtTwo_lowerRamificationGroup_three_ne
statement: formalized
proof: formalized
---

# TauCeti.DyadicCyclotomicEight.map\_restrictSqrtTwo\_lowerRamificationGroup\_three\_ne

Lower numbering fails to commute with this restriction: the image at depth three is
the whole quadratic Galois group, but the quadratic lower group at depth three is trivial.

```lean
TauCeti.DyadicCyclotomicEight.map_restrictSqrtTwo_lowerRamificationGroup_three_ne :
  Subgroup.map TauCeti.DyadicCyclotomicEight.restrictSqrtTwo
      (TauCeti.LocalFieldsRamification.lowerRamificationGroup ℚ_[2] TauCeti.DyadicCyclotomicEight
        3) ≠
    TauCeti.LocalFieldsRamification.lowerRamificationGroup ℚ_[2] TauCeti.DyadicSqrtTwo 3
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.algebraicExtensionNormedField](tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DyadicCyclotomicEight.map_restrictSqrtTwo_lowerRamificationGroup_three_ne`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WorkedExamples/CyclotomicEight/Quotient.html#TauCeti.DyadicCyclotomicEight.map_restrictSqrtTwo_lowerRamificationGroup_three_ne).

## Sources

- [Tau Ceti documentation: `TauCeti.DyadicCyclotomicEight.map_restrictSqrtTwo_lowerRamificationGroup_three_ne`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WorkedExamples/CyclotomicEight/Quotient.html#TauCeti.DyadicCyclotomicEight.map_restrictSqrtTwo_lowerRamificationGroup_three_ne)
- [Source of `TauCeti.DyadicCyclotomicEight.map_restrictSqrtTwo_lowerRamificationGroup_three_ne` in TauCeti/NumberTheory/LocalField/WorkedExamples/CyclotomicEight/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/WorkedExamples/CyclotomicEight/Quotient.lean#L214)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalFieldsRamification/STATUS.md)
