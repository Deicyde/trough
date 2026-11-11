---
declaration: theorem
origin: cited
lean: TauCeti.memVMO_iff_exists_tendsto_bmoSeminorm_sub, TauCeti.MemVMO.exists_tendsto_bmoSeminorm_sub
statement: formalized
proof: formalized
---

# Sarason's theorem

A function has vanishing mean oscillation if and only if it is locally
integrable and a limit, in the BMO seminorm, of uniformly continuous functions of bounded mean
oscillation.

```lean
TauCeti.memVMO_iff_exists_tendsto_bmoSeminorm_sub.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] [NormedAddCommGroup F]
  [NormedSpace ℝ F] {f : E → F} [CompleteSpace F] :
  TauCeti.MemVMO f μ ↔
    MeasureTheory.LocallyIntegrable f μ ∧
      ∃ g,
        (∀ (k : ℕ), UniformContinuous (g k)) ∧
          (∀ (k : ℕ), TauCeti.MemBMO (g k) μ) ∧
            Filter.Tendsto (fun k => TauCeti.bmoSeminorm (f - g k) μ) Filter.atTop (nhds 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.memVMO_iff_exists_tendsto_bmoSeminorm_sub`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/BoundedMeanOscillation/Sarason.html#TauCeti.memVMO_iff_exists_tendsto_bmoSeminorm_sub).

## Other forms

**Sarason's theorem, the approximation half.** Formalized in Tau Ceti as [`TauCeti.MemVMO.exists_tendsto_bmoSeminorm_sub`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/BoundedMeanOscillation/Sarason.html#TauCeti.MemVMO.exists_tendsto_bmoSeminorm_sub).

```lean
TauCeti.MemVMO.exists_tendsto_bmoSeminorm_sub.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] [NormedAddCommGroup F]
  [NormedSpace ℝ F] {f : E → F} [CompleteSpace F] (hf : TauCeti.MemVMO f μ) :
  ∃ g,
    (∀ (k : ℕ), UniformContinuous (g k)) ∧
      (∀ (k : ℕ), TauCeti.MemBMO (g k) μ) ∧
        Filter.Tendsto (fun k => TauCeti.bmoSeminorm (f - g k) μ) Filter.atTop (nhds 0)
```

## Sources

- [Tau Ceti documentation: `TauCeti.memVMO_iff_exists_tendsto_bmoSeminorm_sub`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/BoundedMeanOscillation/Sarason.html#TauCeti.memVMO_iff_exists_tendsto_bmoSeminorm_sub)
- [Source of `TauCeti.memVMO_iff_exists_tendsto_bmoSeminorm_sub` in TauCeti/MeasureTheory/Function/BoundedMeanOscillation/Sarason.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/BoundedMeanOscillation/Sarason.lean#L541)
