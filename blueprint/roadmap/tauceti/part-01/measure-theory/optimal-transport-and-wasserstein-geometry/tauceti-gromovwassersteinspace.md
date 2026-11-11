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
- [Source of `TauCeti.GromovWassersteinSpace` in TauCeti/MeasureTheory/OptimalTransport/GromovWasserstein/Space.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/OptimalTransport/GromovWasserstein/Space.lean#L209)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OptimalTransport/STATUS.md)
