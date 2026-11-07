---
declaration: theorem
origin: cited
lean: ConvexBody.hasDerivWithinAt_volume_real_add_smul_closedBall_rpow_iff_exists_eq_closedBall
statement: formalized
proof: formalized
---

# Ball rigidity from the sharp first variation of parallel volume

A convex body `K` of
positive volume has parallel-volume root `t ↦ volume (K + t • closedBall 0 1) ^ (1 / n)` with
right derivative `volume (closedBall 0 1) ^ (1 / n)` at zero exactly when `K` is a closed ball
of positive radius.

```lean
ConvexBody.hasDerivWithinAt_volume_real_add_smul_closedBall_rpow_iff_exists_eq_closedBall.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] (K : ConvexBody E) (hn : Module.finrank ℝ E ≠ 0)
  (hK : MeasureTheory.volume ↑K ≠ 0) :
  HasDerivWithinAt
      (fun t =>
        MeasureTheory.volume.real (↑K + t • Metric.closedBall 0 1) ^ (↑(Module.finrank ℝ E))⁻¹)
      (MeasureTheory.volume.real (Metric.closedBall 0 1) ^ (↑(Module.finrank ℝ E))⁻¹) (Set.Ioi 0)
      0 ↔
    ∃ c r, 0 < r ∧ ↑K = Metric.closedBall c r
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.hasPrekopaLeindler\_volume](tauceti-hasprekopaleindler-volume.md)

## Lean

Formalized in Tau Ceti as [`ConvexBody.hasDerivWithinAt_volume_real_add_smul_closedBall_rpow_iff_exists_eq_closedBall`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Parallel.html#ConvexBody.hasDerivWithinAt_volume_real_add_smul_closedBall_rpow_iff_exists_eq_closedBall).

## Sources

- [Tau Ceti documentation: `ConvexBody.hasDerivWithinAt_volume_real_add_smul_closedBall_rpow_iff_exists_eq_closedBall`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Parallel.html#ConvexBody.hasDerivWithinAt_volume_real_add_smul_closedBall_rpow_iff_exists_eq_closedBall)
- [Source of `ConvexBody.hasDerivWithinAt_volume_real_add_smul_closedBall_rpow_iff_exists_eq_closedBall` in TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Parallel.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Parallel.lean#L164)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Isoperimetry/STATUS.md)
