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
- [Source of `TauCeti.IsDisplacementInterpolation` in TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Geodesic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Geodesic/Basic.lean#L114)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/OptimalTransport/STATUS.md)
