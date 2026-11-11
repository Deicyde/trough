---
declaration: def
origin: cited
lean: TauCeti.singularCubicalHomologyNatIso
statement: formalized
---

# Cubical singular homology is naturally isomorphic to singular homology, as functors on topological spaces

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
- [Source of `TauCeti.singularCubicalHomologyNatIso` in TauCeti/AlgebraicTopology/Singular/Cubical/Comparison/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Singular/Cubical/Comparison/Basic.lean#L461)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGFloer/STATUS.md)
