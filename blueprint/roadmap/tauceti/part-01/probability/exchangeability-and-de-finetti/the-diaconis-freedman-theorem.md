---
declaration: theorem
origin: cited
lean: TauCeti.Probability.markovExchangeable_iff_mixedMarkovChain, TauCeti.Probability.MarkovExchangeable.mixedMarkovChain, TauCeti.Probability.MarkovExchangeable.mixedMarkovChain_of_ae_initial_eq
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

- [De Finetti's theorem](de-finettis-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.markovExchangeable_iff_mixedMarkovChain`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Recurrence/InitialState.html#TauCeti.Probability.markovExchangeable_iff_mixedMarkovChain).

## Other forms

**The Diaconis--Freedman representation theorem.** Formalized in Tau Ceti as [`TauCeti.Probability.MarkovExchangeable.mixedMarkovChain`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Recurrence/InitialState.html#TauCeti.Probability.MarkovExchangeable.mixedMarkovChain).

```lean
TauCeti.Probability.MarkovExchangeable.mixedMarkovChain.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  [MeasurableSpace Ω] [MeasurableSpace α] {μ : MeasureTheory.Measure Ω} {X : ℕ → Ω → α}
  [MeasureTheory.IsFiniteMeasure μ] [NeZero μ] (h : TauCeti.Probability.MarkovExchangeable μ X)
  (hrec : TauCeti.Probability.Recurrent μ X) : TauCeti.Probability.MixedMarkovChain μ X
```

**The Diaconis--Freedman representation theorem at a fixed start.** Formalized in Tau Ceti as [`TauCeti.Probability.MarkovExchangeable.mixedMarkovChain_of_ae_initial_eq`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Recurrence/RowExchangeable.html#TauCeti.Probability.MarkovExchangeable.mixedMarkovChain_of_ae_initial_eq).

```lean
TauCeti.Probability.MarkovExchangeable.mixedMarkovChain_of_ae_initial_eq.{u_1, u_2} {Ω : Type u_1}
  {α : Type u_2} [MeasurableSpace Ω] [MeasurableSpace α] {μ : MeasureTheory.Measure Ω}
  {X : ℕ → Ω → α} [MeasureTheory.IsProbabilityMeasure μ] {a₀ : α}
  (h : TauCeti.Probability.MarkovExchangeable μ X) (hrec : TauCeti.Probability.Recurrent μ X)
  (h0 : ∀ᵐ (ω : Ω) ∂μ, X 0 ω = a₀) : TauCeti.Probability.MixedMarkovChain μ X
```

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.markovExchangeable_iff_mixedMarkovChain`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Recurrence/InitialState.html#TauCeti.Probability.markovExchangeable_iff_mixedMarkovChain)
- [Source of `TauCeti.Probability.markovExchangeable_iff_mixedMarkovChain` in TauCeti/Probability/Exchangeability/Recurrence/InitialState.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Exchangeability/Recurrence/InitialState.lean#L90)
- [Tau Ceti roadmap status: Exchangeability and de Finetti](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/Exchangeability/STATUS.md)
