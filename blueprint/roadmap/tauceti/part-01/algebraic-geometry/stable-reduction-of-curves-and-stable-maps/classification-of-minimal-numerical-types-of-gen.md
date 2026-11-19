---
declaration: theorem
origin: cited
lean: TauCeti.NumericalType.IsMinimal.isGenusOneMinimalShape
statement: formalized
proof: formalized
---

# Classification of minimal numerical types of genus one

**Classification of minimal numerical types of genus one**
([Stacks, Lemma 55.6.2](https://stacks.math.columbia.edu/tag/0C8T)). Every minimal numerical type
of arithmetic genus one belongs to one of the shape families of
`TauCeti.NumericalType.IsGenusOneMinimalShape`.

```lean
TauCeti.NumericalType.IsMinimal.isGenusOneMinimalShape.{u} {T : TauCeti.NumericalType}
  (hT : T.IsMinimal) (hg : T.arithmeticGenus = 1) : T.IsGenusOneMinimalShape
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NumericalType.IsMinimal.isGenusOneMinimalShape`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/StableReduction/NumericalType/Genus/One/Classification.html#TauCeti.NumericalType.IsMinimal.isGenusOneMinimalShape).

## Sources

- [Tau Ceti documentation: `TauCeti.NumericalType.IsMinimal.isGenusOneMinimalShape`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/StableReduction/NumericalType/Genus/One/Classification.html#TauCeti.NumericalType.IsMinimal.isGenusOneMinimalShape)
- [Source of `TauCeti.NumericalType.IsMinimal.isGenusOneMinimalShape` in TauCeti/AlgebraicGeometry/Curves/StableReduction/NumericalType/Genus/One/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Curves/StableReduction/NumericalType/Genus/One/Classification.lean#L407)
- [Tau Ceti roadmap status: Stable reduction of curves and stable maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StableReduction/STATUS.md)
