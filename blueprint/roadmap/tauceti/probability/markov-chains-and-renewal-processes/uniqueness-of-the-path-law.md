---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.eq_markovChainLaw
statement: formalized
proof: formalized
---

# Uniqueness of the path law

For a finite initial measure `ν`, a measure on path space whose
time-zero marginal is `ν` and whose prefix laws satisfy the Markov recursion of
`markovChainLaw_map_prefix_succ_eq_compProd` is the path law `markovChainLaw ν κ`.

```lean
MeasureTheory.Measure.eq_markovChainLaw.{u_1} {α : Type u_1} [MeasurableSpace α]
  (ν : MeasureTheory.Measure α) (κ : ProbabilityTheory.Kernel α α)
  [ProbabilityTheory.IsMarkovKernel κ] [MeasureTheory.IsFiniteMeasure ν]
  {μ : MeasureTheory.Measure (ℕ → α)} (h₀ : MeasureTheory.Measure.map (fun x => x 0) μ = ν)
  (hstep :
    ∀ (n : ℕ),
      MeasureTheory.Measure.map (fun x => (fun i => x ↑i, x (n + 1))) μ =
        (MeasureTheory.Measure.map (fun x i => x ↑i) μ).compProd
          (κ.comap (fun w => w (Fin.last n)) ⋯)) :
  μ = TauCeti.Probability.markovChainLaw ν κ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.eq_markovChainLaw`](https://taucetiproject.org/docs/TauCeti/Probability/Process/MarkovChain.html#MeasureTheory.Measure.eq_markovChainLaw).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.eq_markovChainLaw`](https://taucetiproject.org/docs/TauCeti/Probability/Process/MarkovChain.html#MeasureTheory.Measure.eq_markovChainLaw)
- [Source of `MeasureTheory.Measure.eq_markovChainLaw` in TauCeti/Probability/Process/MarkovChain.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Process/MarkovChain.lean#L437)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
