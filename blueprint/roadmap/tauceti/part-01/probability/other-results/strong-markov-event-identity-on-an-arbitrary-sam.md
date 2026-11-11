---
declaration: theorem
origin: cited
lean: ProbabilityTheory.HasLaw.markovChainLaw_inter_preimage_stoppedValue_processShift
statement: formalized
proof: formalized
---

# Strong Markov event identity on an arbitrary sample space

Conditional on a
stopped-history event and a finite stopping time, future events are evaluated by the chain law
started at the stopped state.

```lean
ProbabilityTheory.HasLaw.markovChainLaw_inter_preimage_stoppedValue_processShift.{u_1, u_2}
  {α : Type u_1} {Ω : Type u_2} [MeasurableSpace α] [MeasurableSpace Ω]
  {P : MeasureTheory.Measure Ω} {ν : MeasureTheory.Measure α} [MeasureTheory.IsFiniteMeasure ν]
  {κ : ProbabilityTheory.Kernel α α} [ProbabilityTheory.IsMarkovKernel κ] {X : ℕ → Ω → α}
  (hX : ProbabilityTheory.HasLaw (fun ω n => X n ω) (TauCeti.Probability.markovChainLaw ν κ) P)
  (hXm : ∀ (n : ℕ), Measurable (X n)) {ℱ : MeasureTheory.Filtration ℕ inst✝}
  (hℱ : ∀ (n : ℕ), ↑ℱ n ≤ MeasurableSpace.comap (fun ω i => X (↑i) ω) inferInstance)
  {τ : Ω → WithTop ℕ} (hτ : MeasureTheory.IsStoppingTime ℱ τ) {A : Set Ω} (hA : MeasurableSet A)
  {B : Set (ℕ → α)} (hB : MeasurableSet B) :
  P (A ∩ {ω | τ ω ≠ ⊤} ∩ MeasureTheory.stoppedValue (TauCeti.Probability.processShift X) τ ⁻¹' B) =
    ∫⁻ (ω : Ω) in A ∩ {ω | τ ω ≠ ⊤},
      (TauCeti.Probability.markovChainLaw
          (MeasureTheory.Measure.dirac (MeasureTheory.stoppedValue X τ ω)) κ)
        B ∂P
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.HasLaw.markovChainLaw_inter_preimage_stoppedValue_processShift`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/StrongMarkov/Process.html#ProbabilityTheory.HasLaw.markovChainLaw_inter_preimage_stoppedValue_processShift).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.HasLaw.markovChainLaw_inter_preimage_stoppedValue_processShift`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/StrongMarkov/Process.html#ProbabilityTheory.HasLaw.markovChainLaw_inter_preimage_stoppedValue_processShift)
- [Source of `ProbabilityTheory.HasLaw.markovChainLaw_inter_preimage_stoppedValue_processShift` in TauCeti/Probability/MarkovChain/StrongMarkov/Process.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/MarkovChain/StrongMarkov/Process.lean#L92)
