---
declaration: def
origin: cited
lean: TauCeti.OddComponentGridDiagram.alexanderFiltrationComplex
statement: formalized
---

# TauCeti.OddComponentGridDiagram.alexanderFiltrationComplex

Alexander filtration level `a` as a Maslov-graded chain complex.

```lean
TauCeti.OddComponentGridDiagram.alexanderFiltrationComplex.{u_1} {n : ℕ}
  (G : TauCeti.OddComponentGridDiagram n) (R : Type u_1) [CommRing R] [CharP R 2] (a : ℤ) :
  ChainComplex (ModuleCat R) ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.OddComponentGridDiagram.alexanderFiltrationComplex`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Filtered/Complex.html#TauCeti.OddComponentGridDiagram.alexanderFiltrationComplex).

## Sources

- [Tau Ceti documentation: `TauCeti.OddComponentGridDiagram.alexanderFiltrationComplex`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Filtered/Complex.html#TauCeti.OddComponentGridDiagram.alexanderFiltrationComplex)
- [Source of `TauCeti.OddComponentGridDiagram.alexanderFiltrationComplex` in TauCeti/KnotTheory/Grid/Filtered/Complex.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Grid/Filtered/Complex.lean#L185)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
