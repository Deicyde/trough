---
declaration: theorem
origin: cited
lean: TauCeti.Probability.markovExchangeable_iff_mixedMarkovChain
statement: formalized
proof: formalized
---

# The Diaconis--Freedman theorem

A recurrent process is Markov exchangeable if and only if it
is a mixture of Markov chains.

```lean
TauCeti.Probability.markovExchangeable_iff_mixedMarkovChain.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  [MeasurableSpace Ω] [MeasurableSpace α] {μ : MeasureTheory.Measure Ω} {X : ℕ → Ω → α}
  [MeasureTheory.IsFiniteMeasure μ] [NeZero μ] (hrec : TauCeti.Probability.Recurrent μ X) :
  TauCeti.Probability.MarkovExchangeable μ X ↔ TauCeti.Probability.MixedMarkovChain μ X
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Diaconis--Freedman representation theorem](the-diaconis-freedman-representation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.markovExchangeable_iff_mixedMarkovChain`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Recurrence/InitialState.html#TauCeti.Probability.markovExchangeable_iff_mixedMarkovChain).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.markovExchangeable_iff_mixedMarkovChain`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Recurrence/InitialState.html#TauCeti.Probability.markovExchangeable_iff_mixedMarkovChain)
- [Source of `TauCeti.Probability.markovExchangeable_iff_mixedMarkovChain` in TauCeti/Probability/Exchangeability/Recurrence/InitialState.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Exchangeability/Recurrence/InitialState.lean#L90)
- [Tau Ceti roadmap status: Exchangeability and de Finetti](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Exchangeability/STATUS.md)
