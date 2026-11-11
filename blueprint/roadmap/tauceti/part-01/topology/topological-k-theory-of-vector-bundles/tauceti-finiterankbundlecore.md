---
declaration: structure
origin: cited
lean: TauCeti.FiniteRankBundleCore
statement: formalized
---

# TauCeti.FiniteRankBundleCore

A constant finite-rank vector bundle presented by point-indexed coordinate data.
The selected chart at each base point is the chart with that label.

```lean
TauCeti.FiniteRankBundleCore.{u, v} (𝕜 : Type v) [NontriviallyNormedField 𝕜] (B : Type u)
  [TopologicalSpace B] : Type (max u v)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteRankBundleCore`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/FiniteRank/Basic.html#TauCeti.FiniteRankBundleCore).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteRankBundleCore`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/FiniteRank/Basic.html#TauCeti.FiniteRankBundleCore)
- [Source of `TauCeti.FiniteRankBundleCore` in TauCeti/Topology/VectorBundle/FiniteRank/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/VectorBundle/FiniteRank/Basic.lean#L61)
- [Tau Ceti roadmap status: Topological K-theory of vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TopologicalKTheory/STATUS.md)
