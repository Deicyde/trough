---
declaration: def
origin: cited
lean: TauCeti.IsDisplacementInterpolation
statement: formalized
---

# TauCeti.IsDisplacementInterpolation

A curve of probability laws is a displacement interpolation if it is the curve of time
marginals of a probability dynamic plan on constant-speed geodesics with optimal endpoint law.
The optimality uses `eLpNorm`, so it includes the infinite exponent and infinite values.

```lean
TauCeti.IsDisplacementInterpolation.{u_1} {X : Type u_1} [PseudoMetricSpace X] [MeasurableSpace X]
  (p : ENNReal) (μ : ↑unitInterval → MeasureTheory.ProbabilityMeasure X) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsDisplacementInterpolation`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Geodesic/Basic.html#TauCeti.IsDisplacementInterpolation).

## Sources

- [Tau Ceti documentation: `TauCeti.IsDisplacementInterpolation`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Geodesic/Basic.html#TauCeti.IsDisplacementInterpolation)
- [Source of `TauCeti.IsDisplacementInterpolation` in TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Geodesic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Geodesic/Basic.lean#L111)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OptimalTransport/STATUS.md)
