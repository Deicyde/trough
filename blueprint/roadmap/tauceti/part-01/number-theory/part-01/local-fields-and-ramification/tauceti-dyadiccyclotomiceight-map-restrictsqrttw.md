---
declaration: theorem
origin: cited
lean: TauCeti.DyadicCyclotomicEight.map_restrictSqrtTwo_lowerRamificationGroup_three_ne
statement: formalized
proof: formalized
---

# TauCeti.DyadicCyclotomicEight.map_restrictSqrtTwo_lowerRamificationGroup_three_ne

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

- [Serre's criterion](../../../ring-theory/part-01/ideal/serres-criterion.md)
- [TauCeti.algebraicExtensionNormedField](tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DyadicCyclotomicEight.map_restrictSqrtTwo_lowerRamificationGroup_three_ne`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WorkedExamples/CyclotomicEight/Quotient.html#TauCeti.DyadicCyclotomicEight.map_restrictSqrtTwo_lowerRamificationGroup_three_ne).

## Sources

- [Tau Ceti documentation: `TauCeti.DyadicCyclotomicEight.map_restrictSqrtTwo_lowerRamificationGroup_three_ne`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WorkedExamples/CyclotomicEight/Quotient.html#TauCeti.DyadicCyclotomicEight.map_restrictSqrtTwo_lowerRamificationGroup_three_ne)
- [Source of `TauCeti.DyadicCyclotomicEight.map_restrictSqrtTwo_lowerRamificationGroup_three_ne` in TauCeti/NumberTheory/LocalField/WorkedExamples/CyclotomicEight/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/WorkedExamples/CyclotomicEight/Quotient.lean#L214)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/LocalFieldsRamification/STATUS.md)
