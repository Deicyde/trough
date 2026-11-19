---
declaration: theorem
origin: cited
lean: TauCeti.ClassificationStatement.of_universe
statement: formalized
proof: formalized
---

# TauCeti.ClassificationStatement.of_universe

The classification statement in one universe implies the statement in every universe: a
finite group can be transported to a carrier in any universe.

```lean
TauCeti.ClassificationStatement.of_universe.{u, v} (h : TauCeti.ClassificationStatement) :
  TauCeti.ClassificationStatement
```

## Depends on

- [Classification of finite simple groups, statement only](classification-of-finite-simple-groups-statement.md)

## Proof depends on

- [The ambient group of a valid Lie-type index](the-ambient-group-of-a-valid-lie-type-index.md)
- [Cauchy--Binet for `2 × 2` minors](../../linear-algebra/part-01/matrix/cauchy-binet-for-2-2-minors.md)
- [TauCeti.SporadicName.presentation](tauceti-sporadicname-presentation.md)
- [TauCeti.ValidLieTypeIndex.Group](tauceti-validlietypeindex-group.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassificationStatement.of_universe`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/Classification.html#TauCeti.ClassificationStatement.of_universe).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassificationStatement.of_universe`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/Classification.html#TauCeti.ClassificationStatement.of_universe)
- [Source of `TauCeti.ClassificationStatement.of_universe` in TauCeti/GroupTheory/SpecificGroups/CFSG/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/SpecificGroups/CFSG/Classification.lean#L66)
- [Tau Ceti roadmap status: Stating the classification of finite simple groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CFSGStatement/STATUS.md)
