---
declaration: theorem
origin: cited
lean: TauCeti.isWeakHomotopyEquivalence_sigmaCWApproximationMap
statement: formalized
proof: formalized
---

# CW approximation (Hatcher, Proposition 4.13)

For every space `X`, the map
`TauCeti.sigmaCWApproximationMap X` from the CW complex `TauCeti.sigmaCWApproximation X` to `X` is a
weak homotopy equivalence.

```lean
TauCeti.isWeakHomotopyEquivalence_sigmaCWApproximationMap.{u} (X : TopCat) :
  (TopCat.Hom.hom (TauCeti.sigmaCWApproximationMap X)).IsWeakHomotopyEquivalence
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isWeakHomotopyEquivalence_sigmaCWApproximationMap`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/CWApproximation/Sigma.html#TauCeti.isWeakHomotopyEquivalence_sigmaCWApproximationMap).

## Sources

- [Tau Ceti documentation: `TauCeti.isWeakHomotopyEquivalence_sigmaCWApproximationMap`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/CWApproximation/Sigma.html#TauCeti.isWeakHomotopyEquivalence_sigmaCWApproximationMap)
- [Source of `TauCeti.isWeakHomotopyEquivalence_sigmaCWApproximationMap` in TauCeti/AlgebraicTopology/Homotopy/CWApproximation/Sigma.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Homotopy/CWApproximation/Sigma.lean#L147)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGFloer/STATUS.md)
