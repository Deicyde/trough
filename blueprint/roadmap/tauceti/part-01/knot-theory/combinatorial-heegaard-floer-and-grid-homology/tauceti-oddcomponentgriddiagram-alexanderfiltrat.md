---
declaration: def
origin: cited
lean: TauCeti.OddComponentGridDiagram.alexanderFiltration
statement: formalized
---

# TauCeti.OddComponentGridDiagram.alexanderFiltration

The level `F_a` of the Alexander filtration of the grid chain module `GC⁻`: the chains all of
whose monomials `V^e · x` have Alexander grading `A(x) - |e| ≤ a`. Each variable lowers the
Alexander grading, so this is a submodule over the polynomial ring.

```lean
TauCeti.OddComponentGridDiagram.alexanderFiltration.{u_1} {n : ℕ}
  (G : TauCeti.OddComponentGridDiagram n) (R : Type u_1) [CommSemiring R] (a : ℤ) :
  Submodule (MvPolynomial (Fin n) R) (TauCeti.GridChainMinus R n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.OddComponentGridDiagram.alexanderFiltration`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Filtered/Alexander.html#TauCeti.OddComponentGridDiagram.alexanderFiltration).

## Sources

- [Tau Ceti documentation: `TauCeti.OddComponentGridDiagram.alexanderFiltration`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Filtered/Alexander.html#TauCeti.OddComponentGridDiagram.alexanderFiltration)
- [Source of `TauCeti.OddComponentGridDiagram.alexanderFiltration` in TauCeti/KnotTheory/Grid/Filtered/Alexander.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/KnotTheory/Grid/Filtered/Alexander.lean#L95)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
