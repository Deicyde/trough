---
declaration: theorem
origin: cited
lean: TauCeti.volume_rpow_add_volume_rpow_le, TauCeti.finrank_mul_rpow_pow_mul_le_volume_real_sub
statement: formalized
proof: formalized
---

# Brunn–Minkowski inequality

**Brunn–Minkowski inequality** for nonempty Lebesgue-measurable sets
in a positive-dimensional real inner product space. The sum has its outer volume and
need not be measurable or have finite volume.

```lean
TauCeti.volume_rpow_add_volume_rpow_le.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {A B : Set E}
  (hn : Module.finrank ℝ E ≠ 0) (hAn : A.Nonempty)
  (hA : MeasureTheory.NullMeasurableSet A MeasureTheory.volume) (hBn : B.Nonempty)
  (hB : MeasureTheory.NullMeasurableSet B MeasureTheory.volume) :
  MeasureTheory.volume A ^ (↑(Module.finrank ℝ E))⁻¹ +
      MeasureTheory.volume B ^ (↑(Module.finrank ℝ E))⁻¹ ≤
    MeasureTheory.volume (A + B) ^ (↑(Module.finrank ℝ E))⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.hasPrekopaLeindler_volume](tauceti-hasprekopaleindler-volume.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.volume_rpow_add_volume_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Basic.html#TauCeti.volume_rpow_add_volume_rpow_le).

## Other forms

**Brunn–Minkowski for a shell.** Formalized in Tau Ceti as [`TauCeti.finrank_mul_rpow_pow_mul_le_volume_real_sub`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Basic.html#TauCeti.finrank_mul_rpow_pow_mul_le_volume_real_sub).

```lean
TauCeti.finrank_mul_rpow_pow_mul_le_volume_real_sub.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  (hn : Module.finrank ℝ E ≠ 0) {G F : Set E}
  (hG : MeasureTheory.NullMeasurableSet G MeasureTheory.volume) (hG0 : G.Nonempty)
  (hF : MeasureTheory.volume F ≠ ⊤) {r : ℝ} (hr : 0 < r) (hsub : G + Metric.ball 0 r ⊆ F) :
  ↑(Module.finrank ℝ E) *
        (MeasureTheory.volume.real G ^ (↑(Module.finrank ℝ E))⁻¹) ^ (Module.finrank ℝ E - 1) *
      (r * MeasureTheory.volume.real (Metric.ball 0 1) ^ (↑(Module.finrank ℝ E))⁻¹) ≤
    MeasureTheory.volume.real F - MeasureTheory.volume.real G
```

## Sources

- [Tau Ceti documentation: `TauCeti.volume_rpow_add_volume_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Basic.html#TauCeti.volume_rpow_add_volume_rpow_le)
- [Source of `TauCeti.volume_rpow_add_volume_rpow_le` in TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Basic.lean#L172)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Isoperimetry/STATUS.md)
