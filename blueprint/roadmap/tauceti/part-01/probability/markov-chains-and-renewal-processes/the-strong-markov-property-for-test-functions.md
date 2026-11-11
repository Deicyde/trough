---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.condExp_stoppedValue_shift_iterate_markovChainLaw
statement: formalized
proof: formalized
---

# The strong Markov property, for test functions

For a stopping time `τ` of the natural
filtration and a function `f` of paths that is integrable for the law of the future path on
`{τ < ∞}`, the conditional expectation given `𝓕_τ` of `f (θ_τ X)` on `{τ < ∞}` is `∫ f dℙ_{X τ}`
there.

```lean
MeasureTheory.Measure.condExp_stoppedValue_shift_iterate_markovChainLaw.{u_1, u_2} {α : Type u_1}
  [MeasurableSpace α] (ν : MeasureTheory.Measure α) (κ : ProbabilityTheory.Kernel α α)
  [ProbabilityTheory.IsMarkovKernel κ] {τ : (ℕ → α) → WithTop ℕ} {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E] [MeasureTheory.IsFiniteMeasure ν]
  (hτ : MeasureTheory.IsStoppingTime MeasureTheory.Filtration.piLE τ) {f : (ℕ → α) → E}
  (hf :
    MeasureTheory.Integrable f
      (TauCeti.Probability.markovChainLaw
        (MeasureTheory.Measure.map (MeasureTheory.stoppedValue (fun n x => x n) τ)
          ((TauCeti.Probability.markovChainLaw ν κ).restrict {x | τ x ≠ ⊤}))
        κ)) :
  (TauCeti.Probability.markovChainLaw ν
        κ)[{x | τ x ≠ ⊤}.indicator fun x =>
        f (MeasureTheory.stoppedValue (fun n => (TauCeti.Probability.shift α)^[n]) τ x) |
      hτ.measurableSpace] =ᵐ[TauCeti.Probability.markovChainLaw ν κ]
    {x | τ x ≠ ⊤}.indicator fun x =>
      ∫ (y : ℕ → α),
        f
          y ∂TauCeti.Probability.markovChainLaw
          (MeasureTheory.Measure.dirac (MeasureTheory.stoppedValue (fun n x => x n) τ x)) κ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.condExp_stoppedValue_shift_iterate_markovChainLaw`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/StrongMarkov/Basic.html#MeasureTheory.Measure.condExp_stoppedValue_shift_iterate_markovChainLaw).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.condExp_stoppedValue_shift_iterate_markovChainLaw`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/StrongMarkov/Basic.html#MeasureTheory.Measure.condExp_stoppedValue_shift_iterate_markovChainLaw)
- [Source of `MeasureTheory.Measure.condExp_stoppedValue_shift_iterate_markovChainLaw` in TauCeti/Probability/MarkovChain/StrongMarkov/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/MarkovChain/StrongMarkov/Basic.lean#L164)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
