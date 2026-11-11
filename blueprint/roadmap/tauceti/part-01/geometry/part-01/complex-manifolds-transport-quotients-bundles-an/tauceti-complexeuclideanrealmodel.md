---
declaration: def
origin: cited
lean: TauCeti.complexEuclideanRealModel
statement: formalized
---

# TauCeti.complexEuclideanRealModel

The real Euclidean model of a complex Euclidean chart, with the same chart carrier.

```lean
TauCeti.complexEuclideanRealModel (n : ℕ) :
  ModelWithCorners ℝ (EuclideanSpace ℝ (Fin (2 * n))) (EuclideanSpace ℂ (Fin n))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.complexEuclideanRealModel`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Euclidean.html#TauCeti.complexEuclideanRealModel).

## Sources

- [Tau Ceti documentation: `TauCeti.complexEuclideanRealModel`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Euclidean.html#TauCeti.complexEuclideanRealModel)
- [Source of `TauCeti.complexEuclideanRealModel` in TauCeti/Geometry/Manifold/Complex/Euclidean.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Complex/Euclidean.lean#L35)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexManifolds/STATUS.md)
