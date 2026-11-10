---
declaration: def
origin: cited
lean: TauCeti.LocalCoefficientSystem.twistedCubicalSingularHomotopyEquiv
statement: formalized
---

# Cubical and simplicial chains with local coefficients are chain homotopy equivalent

```lean
TauCeti.LocalCoefficientSystem.twistedCubicalSingularHomotopyEquiv.{u, v} {R : Type u} [Ring R]
  {X : TopCat} (L : TauCeti.LocalCoefficientSystem R X) :
  HomotopyEquiv L.normalizedTwistedCubicalChainComplex L.twistedChainComplex
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LocalCoefficientSystem.twistedCubicalSingularHomotopyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/LocalCoefficients/Comparison/Homotopy.html#TauCeti.LocalCoefficientSystem.twistedCubicalSingularHomotopyEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.LocalCoefficientSystem.twistedCubicalSingularHomotopyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/LocalCoefficients/Comparison/Homotopy.html#TauCeti.LocalCoefficientSystem.twistedCubicalSingularHomotopyEquiv)
- [Source of `TauCeti.LocalCoefficientSystem.twistedCubicalSingularHomotopyEquiv` in TauCeti/AlgebraicTopology/Singular/Cubical/LocalCoefficients/Comparison/Homotopy.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Singular/Cubical/LocalCoefficients/Comparison/Homotopy.lean#L455)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGFloer/STATUS.md)
