---
declaration: theorem
origin: cited
lean: TauCeti.exists_probabilityMeasure_of_tendsto_charFun
statement: formalized
proof: formalized
---

# Lévy's continuity theorem, including existence

If the characteristic functions of a
sequence of probability measures converge pointwise to a function continuous at zero, there is
a unique probability measure with that characteristic function, and the sequence converges
weakly to it. Continuity is required only at zero; normalization of the limit follows from the
probability measures in the sequence.

```lean
TauCeti.exists_probabilityMeasure_of_tendsto_charFun.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ : ℕ → MeasureTheory.ProbabilityMeasure E} {f : E → ℂ} (hf : ContinuousAt f 0)
  (h :
    ∀ (t : E),
      Filter.Tendsto (fun n => MeasureTheory.charFun (↑(μ n)) t) Filter.atTop (nhds (f t))) :
  ∃! μ₀, MeasureTheory.charFun ↑μ₀ = f ∧ Filter.Tendsto μ Filter.atTop (nhds μ₀)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_probabilityMeasure_of_tendsto_charFun`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/LevyConvergence.html#TauCeti.exists_probabilityMeasure_of_tendsto_charFun).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_probabilityMeasure_of_tendsto_charFun`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/LevyConvergence.html#TauCeti.exists_probabilityMeasure_of_tendsto_charFun)
- [Source of `TauCeti.exists_probabilityMeasure_of_tendsto_charFun` in TauCeti/MeasureTheory/Measure/LevyConvergence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Measure/LevyConvergence.lean#L43)
