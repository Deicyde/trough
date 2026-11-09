---
declaration: theorem
origin: cited
lean: TauCeti.etvDist_sq_le_two_mul_klDiv, TauCeti.etvDist_sq_le_two_mul_mass_mul_klDiv, TauCeti.two_mul_sq_measureReal_sub_le_klDiv
statement: formalized
proof: formalized
---

# Pinsker's inequality

**Pinsker's inequality** for probability measures, with natural logarithms and no
absolute-continuity assumption. Mathlib's `etvDist` on the left is twice the usual distance
`dTV(μ, ν) = sup_s |μ s - ν s|`, so the bound is equivalently `2 * dTV(μ, ν)² ≤ klDiv μ ν`.

```lean
TauCeti.etvDist_sq_le_two_mul_klDiv.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ ν : MeasureTheory.Measure α} [MeasureTheory.IsProbabilityMeasure μ]
  [MeasureTheory.IsProbabilityMeasure ν] :
  MeasureTheory.etvDist μ ν ^ 2 ≤ 2 * InformationTheory.klDiv μ ν
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.etvDist_sq_le_two_mul_klDiv`](https://taucetiproject.org/docs/TauCeti/InformationTheory/KullbackLeibler/Pinsker.html#TauCeti.etvDist_sq_le_two_mul_klDiv).

## Other forms

**Pinsker's inequality.** Formalized in Tau Ceti as [`TauCeti.etvDist_sq_le_two_mul_mass_mul_klDiv`](https://taucetiproject.org/docs/TauCeti/InformationTheory/KullbackLeibler/Pinsker.html#TauCeti.etvDist_sq_le_two_mul_mass_mul_klDiv).

```lean
TauCeti.etvDist_sq_le_two_mul_mass_mul_klDiv.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ ν : MeasureTheory.Measure α} [MeasureTheory.IsFiniteMeasure μ]
  [MeasureTheory.IsFiniteMeasure ν] (hmass : μ Set.univ = ν Set.univ) :
  MeasureTheory.etvDist μ ν ^ 2 ≤ 2 * μ Set.univ * InformationTheory.klDiv μ ν
```

**Pinsker's inequality for events, with natural logarithms.** Formalized in Tau Ceti as [`TauCeti.two_mul_sq_measureReal_sub_le_klDiv`](https://taucetiproject.org/docs/TauCeti/InformationTheory/KullbackLeibler/Pinsker.html#TauCeti.two_mul_sq_measureReal_sub_le_klDiv).

```lean
TauCeti.two_mul_sq_measureReal_sub_le_klDiv.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ ν : MeasureTheory.Measure α} [MeasureTheory.IsProbabilityMeasure μ]
  [MeasureTheory.IsProbabilityMeasure ν] {s : Set α} (hs : MeasurableSet s) :
  ENNReal.ofReal (2 * (μ.real s - ν.real s) ^ 2) ≤ InformationTheory.klDiv μ ν
```

## Sources

- [Tau Ceti documentation: `TauCeti.etvDist_sq_le_two_mul_klDiv`](https://taucetiproject.org/docs/TauCeti/InformationTheory/KullbackLeibler/Pinsker.html#TauCeti.etvDist_sq_le_two_mul_klDiv)
- [Source of `TauCeti.etvDist_sq_le_two_mul_klDiv` in TauCeti/InformationTheory/KullbackLeibler/Pinsker.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/InformationTheory/KullbackLeibler/Pinsker.lean#L146)
