---
declaration: def
origin: cited
lean: TauCeti.singularCubicalHomologyNatIso
statement: formalized
---

# Cubical singular homology is naturally isomorphic to singular homology

, as functors on
topological spaces.

```lean
TauCeti.singularCubicalHomologyNatIso.{u} (k : Type u) [Ring k] (n : ℕ) :
  (TauCeti.singularChains k).comp
      (HomologicalComplex.homologyFunctor (ModuleCat k) (ComplexShape.down ℕ) n) ≅
    (TauCeti.normalizedCubicalChainComplex k).comp
      (HomologicalComplex.homologyFunctor (ModuleCat k) (ComplexShape.down ℕ) n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.singularCubicalHomologyNatIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Comparison/Basic.html#TauCeti.singularCubicalHomologyNatIso).

## Sources

- [Tau Ceti documentation: `TauCeti.singularCubicalHomologyNatIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Cubical/Comparison/Basic.html#TauCeti.singularCubicalHomologyNatIso)
- [Source of `TauCeti.singularCubicalHomologyNatIso` in TauCeti/AlgebraicTopology/Singular/Cubical/Comparison/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Singular/Cubical/Comparison/Basic.lean#L462)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGFloer/STATUS.md)
