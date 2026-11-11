---
declaration: theorem
origin: cited
lean: TauCeti.CountablyRectifiable.ae_tendsto_euclideanHausdorffMeasure_inter_closedBall_div
statement: formalized
proof: formalized
---

# The density theorem for rectifiable sets

A countably `k`-rectifiable subset `E` of a
finite-dimensional real inner product space, measurable for `μHE[k]` and with locally finite
`μHE[k]` measure, has `k`-dimensional density one at `μHE[k]`-almost every point of `E`:
`μHE[k] (E ∩ closedBall x r) / (ω_k r ^ k) → 1` as `r → 0⁺`, where `ω_k r ^ k` is the volume of a
ball of radius `r` in `EuclideanSpace ℝ (Fin k)`.

```lean
TauCeti.CountablyRectifiable.ae_tendsto_euclideanHausdorffMeasure_inter_closedBall_div.{u_1}
  {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V]
  [MeasurableSpace V] [BorelSpace V] {k : ℕ} {E : Set V} (hE : TauCeti.CountablyRectifiable k E)
  (hEm : MeasureTheory.NullMeasurableSet E (MeasureTheory.Measure.euclideanHausdorffMeasure k))
  [MeasureTheory.IsLocallyFiniteMeasure
      ((MeasureTheory.Measure.euclideanHausdorffMeasure k).restrict E)] :
  ∀ᵐ (x : V) ∂MeasureTheory.Measure.euclideanHausdorffMeasure k,
    x ∈ E →
      Filter.Tendsto
        (fun r =>
          (MeasureTheory.Measure.euclideanHausdorffMeasure k) (E ∩ Metric.closedBall x r) /
            MeasureTheory.volume (Metric.closedBall 0 r))
        (nhdsWithin 0 (Set.Ioi 0)) (nhds 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Brunn–Minkowski inequality](../../../measure-theory/euclidean-isoperimetry-sharp-inequalities-and-ri/brunn-minkowski-inequality.md)
- [Lebesgue's density theorem in a `k`-plane](lebesgues-density-theorem-in-a-k-plane.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CountablyRectifiable.ae_tendsto_euclideanHausdorffMeasure_inter_closedBall_div`](https://taucetiproject.org/docs/TauCeti/Geometry/MeasureTheory/Rectifiable/Density.html#TauCeti.CountablyRectifiable.ae_tendsto_euclideanHausdorffMeasure_inter_closedBall_div).

## Sources

- [Tau Ceti documentation: `TauCeti.CountablyRectifiable.ae_tendsto_euclideanHausdorffMeasure_inter_closedBall_div`](https://taucetiproject.org/docs/TauCeti/Geometry/MeasureTheory/Rectifiable/Density.html#TauCeti.CountablyRectifiable.ae_tendsto_euclideanHausdorffMeasure_inter_closedBall_div)
- [Source of `TauCeti.CountablyRectifiable.ae_tendsto_euclideanHausdorffMeasure_inter_closedBall_div` in TauCeti/Geometry/MeasureTheory/Rectifiable/Density.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/MeasureTheory/Rectifiable/Density.lean#L179)
