---
declaration: def
origin: cited
lean: TauCeti.PreAdicSpace.analyticPoints
statement: formalized
---

# Analytic points of a pre-adic space (Wedhorn, Proposition and Definition 8.36)

the points
`x` having an open neighbourhood `U` such that `𝒪_X(U)` contains a pseudouniformiser, that is, a
topologically nilpotent unit. On `Spa(A, A⁺)` these are the points whose support is not open
(`TauCeti.ValuationSpectrum.analyticPoints_presentationLimitPreAdicSpace`).

```lean
TauCeti.PreAdicSpace.analyticPoints.{u} (X : TauCeti.PreAdicSpace) : Set ↑X.toTopCat
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PreAdicSpace.analyticPoints`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Analytic.html#TauCeti.PreAdicSpace.analyticPoints).

## Sources

- [Tau Ceti documentation: `TauCeti.PreAdicSpace.analyticPoints`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Analytic.html#TauCeti.PreAdicSpace.analyticPoints)
- [Source of `TauCeti.PreAdicSpace.analyticPoints` in TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Analytic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Analytic.lean#L112)
- [Tau Ceti roadmap status: Analytic adic geometry for diamonds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicEtaleGeometry/STATUS.md)
