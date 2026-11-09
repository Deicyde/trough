---
declaration: theorem
origin: cited
lean: Isometry.ae_tendsto_euclideanHausdorffMeasure_inter_closedBall_div
statement: formalized
proof: formalized
---

# Lebesgue's density theorem in a `k`-plane

Let `ι` be an isometry from `k`-dimensional
Euclidean space into `X`. Every subset `S` of its range has `k`-dimensional density one at
`μHE[k]`-almost every point of `S`. No measurability of `S` is needed.

```lean
Isometry.ae_tendsto_euclideanHausdorffMeasure_inter_closedBall_div.{u_1} {X : Type u_1}
  [MetricSpace X] [MeasurableSpace X] [BorelSpace X] {k : ℕ} {ι : EuclideanSpace ℝ (Fin k) → X}
  (hι : Isometry ι) {S : Set X} (hS : S ⊆ Set.range ι) :
  ∀ᵐ (x : X) ∂MeasureTheory.Measure.euclideanHausdorffMeasure k,
    x ∈ S →
      Filter.Tendsto
        (fun r =>
          (MeasureTheory.Measure.euclideanHausdorffMeasure k) (S ∩ Metric.closedBall x r) /
            MeasureTheory.volume (Metric.closedBall 0 r))
        (nhdsWithin 0 (Set.Ioi 0)) (nhds 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Isometry.ae_tendsto_euclideanHausdorffMeasure_inter_closedBall_div`](https://taucetiproject.org/docs/TauCeti/Geometry/Euclidean/Volume/Density.html#Isometry.ae_tendsto_euclideanHausdorffMeasure_inter_closedBall_div).

## Sources

- [Tau Ceti documentation: `Isometry.ae_tendsto_euclideanHausdorffMeasure_inter_closedBall_div`](https://taucetiproject.org/docs/TauCeti/Geometry/Euclidean/Volume/Density.html#Isometry.ae_tendsto_euclideanHausdorffMeasure_inter_closedBall_div)
- [Source of `Isometry.ae_tendsto_euclideanHausdorffMeasure_inter_closedBall_div` in TauCeti/Geometry/Euclidean/Volume/Density.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Euclidean/Volume/Density.lean#L201)
