---
declaration: theorem
origin: cited
lean: TauCeti.isCompact_closure_of_isTightMeasureSet_of_mass_le, TauCeti.exists_tendsto_finiteMeasure_of_eventually_measure_compl_eq_zero
statement: formalized
proof: formalized
---

# Prokhorov's theorem for finite measures

A tight set of finite measures with uniformly
bounded total mass has compact closure in the topology of weak convergence.

This is the finite-measure counterpart of Mathlib's `isCompact_closure_of_isTightMeasureSet`
for probability measures.

```lean
TauCeti.isCompact_closure_of_isTightMeasureSet_of_mass_le.{u_1} {α : Type u_1} [MeasurableSpace α]
  [TopologicalSpace α] [T2Space α] [BorelSpace α] {S : Set (MeasureTheory.FiniteMeasure α)}
  {C : NNReal} (hTight : MeasureTheory.IsTightMeasureSet {x | ∃ μ ∈ S, ↑μ = x})
  (hmass : ∀ μ ∈ S, μ.mass ≤ C) : IsCompact (closure S)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isCompact_closure_of_isTightMeasureSet_of_mass_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Prokhorov.html#TauCeti.isCompact_closure_of_isTightMeasureSet_of_mass_le).

## Other forms

**Prokhorov's theorem along an ultrafilter, for measures carried by a compact set.** Formalized in Tau Ceti as [`TauCeti.exists_tendsto_finiteMeasure_of_eventually_measure_compl_eq_zero`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Prokhorov.html#TauCeti.exists_tendsto_finiteMeasure_of_eventually_measure_compl_eq_zero).

```lean
TauCeti.exists_tendsto_finiteMeasure_of_eventually_measure_compl_eq_zero.{u_1, u_2} {α : Type u_1}
  [MeasurableSpace α] [TopologicalSpace α] [T2Space α] [BorelSpace α] {ι : Type u_2}
  {U : Ultrafilter ι} {μs : ι → MeasureTheory.FiniteMeasure α} {K : Set α} (hK : IsCompact K)
  {C : ℝ} (h : ∀ᶠ (i : ι) in ↑U, ↑(μs i) Kᶜ = 0 ∧ (↑(μs i)).real Set.univ ≤ C) :
  ∃ μ, ↑μ Kᶜ = 0 ∧ Filter.Tendsto μs (↑U) (nhds μ)
```

## Sources

- [Tau Ceti documentation: `TauCeti.isCompact_closure_of_isTightMeasureSet_of_mass_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Prokhorov.html#TauCeti.isCompact_closure_of_isTightMeasureSet_of_mass_le)
- [Source of `TauCeti.isCompact_closure_of_isTightMeasureSet_of_mass_le` in TauCeti/MeasureTheory/Measure/Prokhorov.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Measure/Prokhorov.lean#L60)
