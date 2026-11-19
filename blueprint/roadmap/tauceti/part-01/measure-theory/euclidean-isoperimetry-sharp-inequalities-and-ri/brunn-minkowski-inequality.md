---
declaration: theorem
origin: cited
lean: TauCeti.volume_rpow_add_volume_rpow_le
statement: formalized
proof: formalized
---

# Brunn–Minkowski inequality

**Brunn–Minkowski inequality** for a nonempty set `A` and a nonempty Lebesgue-measurable set
`B` in a positive-dimensional real inner product space. The set `A` and the sum have their outer
volumes and need not be measurable or have finite volume.

```lean
TauCeti.volume_rpow_add_volume_rpow_le.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {A B : Set E}
  (hn : Module.finrank ℝ E ≠ 0) (hAn : A.Nonempty) (hBn : B.Nonempty)
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
- [Source of `TauCeti.volume_rpow_add_volume_rpow_le` in TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Basic.lean#L208)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Isoperimetry/STATUS.md)
