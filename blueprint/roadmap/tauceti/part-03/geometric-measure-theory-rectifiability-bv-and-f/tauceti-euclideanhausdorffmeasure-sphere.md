---
declaration: theorem
origin: cited
lean: TauCeti.euclideanHausdorffMeasure_sphere
statement: formalized
proof: formalized
---

# TauCeti.euclideanHausdorffMeasure\_sphere

A sphere of radius `r > 0` in an `n`-dimensional real inner product space has
`(n - 1)`-dimensional Hausdorff measure `n ω_n r ^ (n - 1)`, where `ω_n` is the volume of the
unit ball.

```lean
TauCeti.euclideanHausdorffMeasure_sphere.{u_2} {E : Type u_2} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] (c : E) {r : ℝ}
  (hr : 0 < r) :
  (MeasureTheory.Measure.euclideanHausdorffMeasure (Module.finrank ℝ E - 1)) (Metric.sphere c r) =
    ↑(Module.finrank ℝ E) * MeasureTheory.volume (Metric.ball 0 1) *
      ENNReal.ofReal r ^ (Module.finrank ℝ E - 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.euclideanHausdorffMeasure_sphere`](https://taucetiproject.org/docs/TauCeti/Geometry/Euclidean/Volume/Sphere.html#TauCeti.euclideanHausdorffMeasure_sphere).

## Sources

- [Tau Ceti documentation: `TauCeti.euclideanHausdorffMeasure_sphere`](https://taucetiproject.org/docs/TauCeti/Geometry/Euclidean/Volume/Sphere.html#TauCeti.euclideanHausdorffMeasure_sphere)
- [Source of `TauCeti.euclideanHausdorffMeasure_sphere` in TauCeti/Geometry/Euclidean/Volume/Sphere.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Euclidean/Volume/Sphere.lean#L364)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
