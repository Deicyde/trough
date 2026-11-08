---
declaration: theorem
origin: cited
lean: TauCeti.Probability.MarkovExchangeable.mixedMarkovChain, TauCeti.Probability.MarkovExchangeable.mixedMarkovChain_of_ae_initial_eq
statement: formalized
proof: formalized
---

# The Diaconis--Freedman representation theorem

A recurrent Markov exchangeable process is a
mixture of Markov chains. The initial state may be random: the representations conditional on the
individual initial states are glued into a single pair of mixing witnesses. The measure is finite
and nonzero, as in the gluing theorem `TauCeti.Probability.mixedMarkovChain_of_forall_cond`.

```lean
TauCeti.Probability.MarkovExchangeable.mixedMarkovChain.{u_1, u_2} {Ω : Type u_1} {α : Type u_2}
  [MeasurableSpace Ω] [MeasurableSpace α] {μ : MeasureTheory.Measure Ω} {X : ℕ → Ω → α}
  [MeasureTheory.IsFiniteMeasure μ] [NeZero μ] (h : TauCeti.Probability.MarkovExchangeable μ X)
  (hrec : TauCeti.Probability.Recurrent μ X) : TauCeti.Probability.MixedMarkovChain μ X
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [De Finetti's theorem](de-finettis-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.MarkovExchangeable.mixedMarkovChain`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Recurrence/InitialState.html#TauCeti.Probability.MarkovExchangeable.mixedMarkovChain).

## Other forms

**The Diaconis--Freedman representation theorem at a fixed start.** Formalized in Tau Ceti as [`TauCeti.Probability.MarkovExchangeable.mixedMarkovChain_of_ae_initial_eq`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Recurrence/RowExchangeable.html#TauCeti.Probability.MarkovExchangeable.mixedMarkovChain_of_ae_initial_eq).

```lean
TauCeti.Probability.MarkovExchangeable.mixedMarkovChain_of_ae_initial_eq.{u_1, u_2} {Ω : Type u_1}
  {α : Type u_2} [MeasurableSpace Ω] [MeasurableSpace α] {μ : MeasureTheory.Measure Ω}
  {X : ℕ → Ω → α} [MeasureTheory.IsProbabilityMeasure μ] {a₀ : α}
  (h : TauCeti.Probability.MarkovExchangeable μ X) (hrec : TauCeti.Probability.Recurrent μ X)
  (h0 : ∀ᵐ (ω : Ω) ∂μ, X 0 ω = a₀) : TauCeti.Probability.MixedMarkovChain μ X
```

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.MarkovExchangeable.mixedMarkovChain`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Recurrence/InitialState.html#TauCeti.Probability.MarkovExchangeable.mixedMarkovChain)
- [Source of `TauCeti.Probability.MarkovExchangeable.mixedMarkovChain` in TauCeti/Probability/Exchangeability/Recurrence/InitialState.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Exchangeability/Recurrence/InitialState.lean#L69)
