---
declaration: theorem
origin: cited
lean: TauCeti.Probability.tendsto_eLpNorm_birkhoffAverage_sub_condExp
statement: formalized
proof: formalized
---

# The mean ergodic theorem for conditional expectations

The Birkhoff time averages of an
integrable square-integrable observable converge in `L²` to its conditional expectation given the
invariant σ-algebra of the transformation.

```lean
TauCeti.Probability.tendsto_eLpNorm_birkhoffAverage_sub_condExp.{u_1} {Ω : Type u_1}
  [MeasurableSpace Ω] {μ : MeasureTheory.Measure Ω} (T : Ω → Ω)
  (hT : MeasureTheory.MeasurePreserving T μ μ) [MeasureTheory.SigmaFinite (μ.trim ⋯)] {f : Ω → ℝ}
  (hf : MeasureTheory.MemLp f 2 μ) (hf_int : MeasureTheory.Integrable f μ) :
  Filter.Tendsto
    (fun n =>
      MeasureTheory.eLpNorm (birkhoffAverage ℝ T f n - μ[f | MeasurableSpace.invariants T]) 2 μ)
    Filter.atTop (nhds 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.tendsto_eLpNorm_birkhoffAverage_sub_condExp`](https://taucetiproject.org/docs/TauCeti/Probability/Ergodic/CondExpProjection.html#TauCeti.Probability.tendsto_eLpNorm_birkhoffAverage_sub_condExp).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.tendsto_eLpNorm_birkhoffAverage_sub_condExp`](https://taucetiproject.org/docs/TauCeti/Probability/Ergodic/CondExpProjection.html#TauCeti.Probability.tendsto_eLpNorm_birkhoffAverage_sub_condExp)
- [Source of `TauCeti.Probability.tendsto_eLpNorm_birkhoffAverage_sub_condExp` in TauCeti/Probability/Ergodic/CondExpProjection.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Ergodic/CondExpProjection.lean#L137)
