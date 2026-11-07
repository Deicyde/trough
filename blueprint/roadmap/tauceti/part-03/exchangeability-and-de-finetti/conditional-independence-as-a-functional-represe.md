---
declaration: theorem
origin: cited
lean: ProbabilityTheory.CondIndepFun.exists_independent_coding
statement: formalized
proof: formalized
---

# Conditional independence as a functional representation

If `X` and `Y` are conditionally
independent given `Z`, then their joint law with `Z` is obtained by keeping `Z` and applying two
measurable coding functions to separate uniform coordinates. When `μ` is a probability measure,
the noises are independent both of one another and of the original sample carrying `Z`.

```lean
ProbabilityTheory.CondIndepFun.exists_independent_coding.{u_1, u_2, u_3, u_4} {Ω : Type u_1}
  {β : Type u_2} {γ : Type u_3} {δ : Type u_4} [MeasurableSpace Ω] [StandardBorelSpace Ω]
  [MeasurableSpace β] [MeasurableSpace γ] [MeasurableSpace δ] [StandardBorelSpace β] [Nonempty β]
  [StandardBorelSpace γ] [Nonempty γ] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsFiniteMeasure μ] {X : Ω → β} {Y : Ω → γ} {Z : Ω → δ} {hZ : Measurable Z}
  (h : ProbabilityTheory.CondIndepFun (MeasurableSpace.comap Z inferInstance) ⋯ X Y μ)
  (hX : Measurable X) (hY : Measurable Y) :
  ∃ f g,
    Measurable (Function.uncurry f) ∧
      Measurable (Function.uncurry g) ∧
        MeasureTheory.Measure.map (fun p => (Z p.1, f (Z p.1) p.2.1, g (Z p.1) p.2.2))
            (μ.prod (MeasureTheory.volume.prod MeasureTheory.volume)) =
          MeasureTheory.Measure.map (fun ω => (Z ω, X ω, Y ω)) μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.CondIndepFun.exists_independent_coding`](https://taucetiproject.org/docs/TauCeti/Probability/Kernel/ConditionalRandomization.html#ProbabilityTheory.CondIndepFun.exists_independent_coding).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.CondIndepFun.exists_independent_coding`](https://taucetiproject.org/docs/TauCeti/Probability/Kernel/ConditionalRandomization.html#ProbabilityTheory.CondIndepFun.exists_independent_coding)
- [Source of `ProbabilityTheory.CondIndepFun.exists_independent_coding` in TauCeti/Probability/Kernel/ConditionalRandomization.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Kernel/ConditionalRandomization.lean#L61)
- [Tau Ceti roadmap status: Exchangeability and de Finetti](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Exchangeability/STATUS.md)
