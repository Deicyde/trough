---
declaration: theorem
origin: cited
lean: TauCeti.OddComponentGridDiagram.gradedHomologyEulerChar_figureEight
statement: formalized
proof: formalized
---

# TauCeti.OddComponentGridDiagram.gradedHomologyEulerChar_figureEight

The graded Euler characteristic of fully blocked homology over `ZMod 2` on the size-six
figure-eight grid is `(1 - t⁻¹)^5 (-t + 3 - t⁻¹)`, where `t = T 2`.

```lean
TauCeti.OddComponentGridDiagram.gradedHomologyEulerChar_figureEight :
  TauCeti.GridDiagram.isKnot_figureEight.toOddComponentGridDiagram.gradedHomologyEulerChar =
    (1 - LaurentPolynomial.T (-2)) ^ 5 * (-LaurentPolynomial.T 2 + 3 - LaurentPolynomial.T (-2))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Euler--Poincaré in one Alexander degree](euler-poincare-in-one-alexander-degree.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.OddComponentGridDiagram.gradedHomologyEulerChar_figureEight`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/FigureEight.html#TauCeti.OddComponentGridDiagram.gradedHomologyEulerChar_figureEight).

## Sources

- [Tau Ceti documentation: `TauCeti.OddComponentGridDiagram.gradedHomologyEulerChar_figureEight`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/FigureEight.html#TauCeti.OddComponentGridDiagram.gradedHomologyEulerChar_figureEight)
- [Source of `TauCeti.OddComponentGridDiagram.gradedHomologyEulerChar_figureEight` in TauCeti/KnotTheory/Grid/FigureEight.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Grid/FigureEight.lean#L175)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
