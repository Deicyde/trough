---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.markovChainLaw_map_eval
statement: formalized
proof: formalized
---

# The time-`n` marginal of the chain

the state at time `n` has law `(κ ^ n) ∘ₘ ν`, the
initial law propagated by the `n`-step transition kernel. This holds for every initial measure
`ν`.

```lean
MeasureTheory.Measure.markovChainLaw_map_eval.{u_1} {α : Type u_1} [MeasurableSpace α]
  (ν : MeasureTheory.Measure α) (κ : ProbabilityTheory.Kernel α α)
  [ProbabilityTheory.IsMarkovKernel κ] (n : ℕ) :
  MeasureTheory.Measure.map (fun w => w n) (TauCeti.Probability.markovChainLaw ν κ) =
    ν.bind ⇑(κ ^ n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The path-law kernel of a homogeneous Markov chain](the-path-law-kernel-of-a-homogeneous-markov-chai.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.markovChainLaw_map_eval`](https://taucetiproject.org/docs/TauCeti/Probability/Process/MarkovChain.html#MeasureTheory.Measure.markovChainLaw_map_eval).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.markovChainLaw_map_eval`](https://taucetiproject.org/docs/TauCeti/Probability/Process/MarkovChain.html#MeasureTheory.Measure.markovChainLaw_map_eval)
- [Source of `MeasureTheory.Measure.markovChainLaw_map_eval` in TauCeti/Probability/Process/MarkovChain.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Process/MarkovChain.lean#L340)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
