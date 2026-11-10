---
declaration: def
origin: cited
lean: TauCeti.GromovWassersteinSpace
statement: formalized
---

# TauCeti.GromovWassersteinSpace

Finite-size standard Borel measured kernels modulo weak isomorphism, with the full
Gromov–Wasserstein metric. The carrier universe is fixed, but is independent of the target.

```lean
TauCeti.GromovWassersteinSpace.{u, v} (p : ENNReal) (Z : Type v) [MetricSpace Z] [Fact (1 ≤ p)] :
  Type (max (u + 1) v)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GromovWassersteinSpace`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/GromovWasserstein/Space.html#TauCeti.GromovWassersteinSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.GromovWassersteinSpace`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/GromovWasserstein/Space.html#TauCeti.GromovWassersteinSpace)
- [Source of `TauCeti.GromovWassersteinSpace` in TauCeti/MeasureTheory/OptimalTransport/GromovWasserstein/Space.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/GromovWasserstein/Space.lean#L210)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OptimalTransport/STATUS.md)
