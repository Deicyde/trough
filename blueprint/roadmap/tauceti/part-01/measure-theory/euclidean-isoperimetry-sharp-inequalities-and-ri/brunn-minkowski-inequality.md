---
declaration: theorem
origin: cited
lean: TauCeti.volume_rpow_add_volume_rpow_le
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

- [Prékopa–Leindler inequality for the minimum on `ℝ`](../integral/part-02/prekopa-leindler-inequality-for-the-minimum-on-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.volume_rpow_add_volume_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Basic.html#TauCeti.volume_rpow_add_volume_rpow_le).

## Sources

- [Tau Ceti documentation: `TauCeti.volume_rpow_add_volume_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Basic.html#TauCeti.volume_rpow_add_volume_rpow_le)
- [Source of `TauCeti.volume_rpow_add_volume_rpow_le` in TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Basic.lean#L172)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Isoperimetry/STATUS.md)
