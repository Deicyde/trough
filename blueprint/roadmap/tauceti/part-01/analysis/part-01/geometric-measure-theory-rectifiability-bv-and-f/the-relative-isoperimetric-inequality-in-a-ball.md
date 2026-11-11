---
declaration: theorem
origin: cited
lean: TauCeti.min_measure_inter_measure_sdiff_rpow_le_perimeter
statement: formalized
proof: formalized
---

# The relative isoperimetric inequality in a ball

Let `E` have dimension `n ≥ 2` and let
`ω = μ(B(0, 1))`. If the ball `B = B(c, r)` lies in the open set `Ω` and `s` is null-measurable in
`B`, then `min (μ(s ∩ B), μ(B \ s)) ^ (1 - 1/n) ≤ 2 ^ (n + 1) ω ^ (-1/n) P(s; Ω)`. The constant does
not depend on the radius, and the perimeter may be infinite.

```lean
TauCeti.min_measure_inter_measure_sdiff_rpow_le_perimeter.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {Ω : TopologicalSpace.Opens E}
  (hn : 2 ≤ Module.finrank ℝ E) {s : Set E} {c : E} {r : ℝ}
  (hs : MeasureTheory.NullMeasurableSet s (μ.restrict (Metric.ball c r)))
  (hΩ : Metric.ball c r ⊆ ↑Ω) :
  min (μ (s ∩ Metric.ball c r)) (μ (Metric.ball c r \ s)) ^ (1 - (↑(Module.finrank ℝ E))⁻¹) ≤
    ENNReal.ofReal
        (2 ^ (Module.finrank ℝ E + 1) / μ.real (Metric.ball 0 1) ^ (↑(Module.finrank ℝ E))⁻¹) *
      TauCeti.perimeter μ Ω s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Poincaré–Wirtinger inequality for functions of bounded variation, localized to a subset](../../part-02/bounded-variation/the-poincare-wirtinger-inequality-for-functions.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.min_measure_inter_measure_sdiff_rpow_le_perimeter`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/RelativeIsoperimetric.html#TauCeti.min_measure_inter_measure_sdiff_rpow_le_perimeter).

## Sources

- [Tau Ceti documentation: `TauCeti.min_measure_inter_measure_sdiff_rpow_le_perimeter`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/RelativeIsoperimetric.html#TauCeti.min_measure_inter_measure_sdiff_rpow_le_perimeter)
- [Source of `TauCeti.min_measure_inter_measure_sdiff_rpow_le_perimeter` in TauCeti/Analysis/BoundedVariation/RelativeIsoperimetric.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/BoundedVariation/RelativeIsoperimetric.lean#L106)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
