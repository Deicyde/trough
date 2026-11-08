---
declaration: theorem
origin: cited
lean: TauCeti.two_mul_sq_measureReal_sub_le_klDiv, TauCeti.etvDist_sq_le_two_mul_klDiv, TauCeti.etvDist_sq_le_two_mul_mass_mul_klDiv
statement: formalized
proof: formalized
---

# Pinsker's inequality for events, with natural logarithms

The extended-valued right
side includes infinite relative entropy, without an absolute-continuity hypothesis.

```lean
TauCeti.two_mul_sq_measureReal_sub_le_klDiv.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ ν : MeasureTheory.Measure α} [MeasureTheory.IsProbabilityMeasure μ]
  [MeasureTheory.IsProbabilityMeasure ν] {s : Set α} (hs : MeasurableSet s) :
  ENNReal.ofReal (2 * (μ.real s - ν.real s) ^ 2) ≤ InformationTheory.klDiv μ ν
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.two_mul_sq_measureReal_sub_le_klDiv`](https://taucetiproject.org/docs/TauCeti/InformationTheory/KullbackLeibler/Pinsker.html#TauCeti.two_mul_sq_measureReal_sub_le_klDiv).

## Other forms

**Pinsker's inequality for probability measures, with natural logarithms and no absolute-continuity assumption.** Formalized in Tau Ceti as [`TauCeti.etvDist_sq_le_two_mul_klDiv`](https://taucetiproject.org/docs/TauCeti/InformationTheory/KullbackLeibler/Pinsker.html#TauCeti.etvDist_sq_le_two_mul_klDiv).

```lean
TauCeti.etvDist_sq_le_two_mul_klDiv.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ ν : MeasureTheory.Measure α} [MeasureTheory.IsProbabilityMeasure μ]
  [MeasureTheory.IsProbabilityMeasure ν] :
  MeasureTheory.etvDist μ ν ^ 2 ≤ 2 * InformationTheory.klDiv μ ν
```

**Pinsker's inequality for finite measures of equal mass, using Mathlib's total variation distance `etvDist`, the signed-measure norm.** Formalized in Tau Ceti as [`TauCeti.etvDist_sq_le_two_mul_mass_mul_klDiv`](https://taucetiproject.org/docs/TauCeti/InformationTheory/KullbackLeibler/Pinsker.html#TauCeti.etvDist_sq_le_two_mul_mass_mul_klDiv).

```lean
TauCeti.etvDist_sq_le_two_mul_mass_mul_klDiv.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ ν : MeasureTheory.Measure α} [MeasureTheory.IsFiniteMeasure μ]
  [MeasureTheory.IsFiniteMeasure ν] (hmass : μ Set.univ = ν Set.univ) :
  MeasureTheory.etvDist μ ν ^ 2 ≤ 2 * μ Set.univ * InformationTheory.klDiv μ ν
```

## Sources

- [Tau Ceti documentation: `TauCeti.two_mul_sq_measureReal_sub_le_klDiv`](https://taucetiproject.org/docs/TauCeti/InformationTheory/KullbackLeibler/Pinsker.html#TauCeti.two_mul_sq_measureReal_sub_le_klDiv)
- [Source of `TauCeti.two_mul_sq_measureReal_sub_le_klDiv` in TauCeti/InformationTheory/KullbackLeibler/Pinsker.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/InformationTheory/KullbackLeibler/Pinsker.lean#L45)
