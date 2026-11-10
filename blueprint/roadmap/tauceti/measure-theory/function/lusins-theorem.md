---
declaration: theorem
origin: cited
lean: Measurable.exists_isClosed_measure_sdiff_lt_continuousOn, AEMeasurable.exists_isClosed_measure_sdiff_lt_continuousOn, MeasureTheory.AEStronglyMeasurable.exists_isClosed_measure_sdiff_lt_continuousOn, MeasureTheory.StronglyMeasurable.exists_isClosed_measure_sdiff_lt_continuousOn
statement: formalized
proof: formalized
---

# Lusin's theorem

A measurable map `f` from a weakly regular measure space into a
second-countable topological space is continuous on a closed set `F ⊆ s` with `μ (s \ F) < ε`,
for every measurable set `s` of finite measure and every `ε > 0`.

```lean
Measurable.exists_isClosed_measure_sdiff_lt_continuousOn.{u_1, u_2} {X : Type u_1} {Y : Type u_2}
  [TopologicalSpace X] [MeasurableSpace X] [OpensMeasurableSpace X] [TopologicalSpace Y]
  [SecondCountableTopology Y] [MeasurableSpace Y] [OpensMeasurableSpace Y]
  {μ : MeasureTheory.Measure X} [μ.WeaklyRegular] {f : X → Y} {s : Set X} {ε : ENNReal}
  (hf : Measurable f) (hs : MeasurableSet s) (hμs : μ s ≠ ⊤) (hε : ε ≠ 0) :
  ∃ F ⊆ s, IsClosed F ∧ μ (s \ F) < ε ∧ ContinuousOn f F
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Measurable.exists_isClosed_measure_sdiff_lt_continuousOn`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lusin.html#Measurable.exists_isClosed_measure_sdiff_lt_continuousOn).

## Other forms

**Lusin's theorem for an almost-everywhere measurable map.** Formalized in Tau Ceti as [`AEMeasurable.exists_isClosed_measure_sdiff_lt_continuousOn`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lusin.html#AEMeasurable.exists_isClosed_measure_sdiff_lt_continuousOn).

```lean
AEMeasurable.exists_isClosed_measure_sdiff_lt_continuousOn.{u_1, u_2} {X : Type u_1} {Y : Type u_2}
  [TopologicalSpace X] [MeasurableSpace X] [OpensMeasurableSpace X] [TopologicalSpace Y]
  [SecondCountableTopology Y] [MeasurableSpace Y] [OpensMeasurableSpace Y]
  {μ : MeasureTheory.Measure X} [μ.WeaklyRegular] {f : X → Y} {s : Set X} {ε : ENNReal}
  (hf : AEMeasurable f μ) (hs : MeasurableSet s) (hμs : μ s ≠ ⊤) (hε : ε ≠ 0) :
  ∃ F ⊆ s, IsClosed F ∧ μ (s \ F) < ε ∧ ContinuousOn f F
```

**Lusin's theorem.** Formalized in Tau Ceti as [`MeasureTheory.AEStronglyMeasurable.exists_isClosed_measure_sdiff_lt_continuousOn`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lusin.html#MeasureTheory.AEStronglyMeasurable.exists_isClosed_measure_sdiff_lt_continuousOn).

```lean
MeasureTheory.AEStronglyMeasurable.exists_isClosed_measure_sdiff_lt_continuousOn.{u_1, u_3}
  {X : Type u_1} [TopologicalSpace X] [MeasurableSpace X] [OpensMeasurableSpace X]
  {μ : MeasureTheory.Measure X} [μ.WeaklyRegular] {s : Set X} {ε : ENNReal} {Z : Type u_3}
  [TopologicalSpace Z] [TopologicalSpace.PseudoMetrizableSpace Z] {g : X → Z}
  (hg : MeasureTheory.AEStronglyMeasurable g μ) (hs : MeasurableSet s) (hμs : μ s ≠ ⊤)
  (hε : ε ≠ 0) : ∃ F ⊆ s, IsClosed F ∧ μ (s \ F) < ε ∧ ContinuousOn g F
```

**Lusin's theorem for a strongly measurable map into a pseudometrizable space.** Formalized in Tau Ceti as [`MeasureTheory.StronglyMeasurable.exists_isClosed_measure_sdiff_lt_continuousOn`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lusin.html#MeasureTheory.StronglyMeasurable.exists_isClosed_measure_sdiff_lt_continuousOn).

```lean
MeasureTheory.StronglyMeasurable.exists_isClosed_measure_sdiff_lt_continuousOn.{u_1, u_3}
  {X : Type u_1} [TopologicalSpace X] [MeasurableSpace X] [OpensMeasurableSpace X]
  {μ : MeasureTheory.Measure X} [μ.WeaklyRegular] {s : Set X} {ε : ENNReal} {Z : Type u_3}
  [TopologicalSpace Z] [TopologicalSpace.PseudoMetrizableSpace Z] {g : X → Z}
  (hg : MeasureTheory.StronglyMeasurable g) (hs : MeasurableSet s) (hμs : μ s ≠ ⊤) (hε : ε ≠ 0) :
  ∃ F ⊆ s, IsClosed F ∧ μ (s \ F) < ε ∧ ContinuousOn g F
```

## Sources

- [Tau Ceti documentation: `Measurable.exists_isClosed_measure_sdiff_lt_continuousOn`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lusin.html#Measurable.exists_isClosed_measure_sdiff_lt_continuousOn)
- [Source of `Measurable.exists_isClosed_measure_sdiff_lt_continuousOn` in TauCeti/MeasureTheory/Function/Lusin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Function/Lusin.lean#L89)
