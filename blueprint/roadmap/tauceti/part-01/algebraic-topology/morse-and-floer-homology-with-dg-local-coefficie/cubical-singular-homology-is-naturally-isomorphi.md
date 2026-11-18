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
- [Source of `TauCeti.singularCubicalHomologyNatIso` in TauCeti/AlgebraicTopology/Singular/Cubical/Comparison/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/Cubical/Comparison/Basic.lean#L461)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DGFloer/STATUS.md)
