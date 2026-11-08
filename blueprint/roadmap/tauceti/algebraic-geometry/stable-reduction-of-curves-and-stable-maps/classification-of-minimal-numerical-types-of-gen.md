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
- [Source of `TauCeti.NumericalType.IsMinimal.isGenusOneMinimalShape` in TauCeti/AlgebraicGeometry/Curves/StableReduction/NumericalType/Genus/One/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Curves/StableReduction/NumericalType/Genus/One/Classification.lean#L407)
- [Tau Ceti roadmap status: Stable reduction of curves and stable maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StableReduction/STATUS.md)
