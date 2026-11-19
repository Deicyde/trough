---
declaration: def
origin: cited
lean: TauCeti.Probability.deFinettiEquiv
statement: formalized
---

# The de Finetti correspondence

Over a standard Borel state space, the de Finetti
barycenter is a bijection from mixing laws — probability measures on `ProbabilityMeasure α` — onto
exchangeable probability measures on `ℕ → α`.

The forward map is `Measure.deFinettiBarycenter`; the inverse sends an exchangeable law to its
mixing law.
Injectivity is uniqueness of the mixing law and surjectivity is de Finetti's theorem, so the
equivalence is exactly the content of `ExchangeableLaw.existsUnique_mixingLaw` in bijective
form.

```lean
TauCeti.Probability.deFinettiEquiv.{u_1} {α : Type u_1} [MeasurableSpace α] [StandardBorelSpace α] :
  MeasureTheory.ProbabilityMeasure (MeasureTheory.ProbabilityMeasure α) ≃
    { ρ // TauCeti.Probability.ExchangeableLaw ↑ρ }
```

## Depends on

- [MeasureTheory.Measure.deFinettiBarycenter](measuretheory-measure-definettibarycenter.md)

## Proof depends on

- [De Finetti's theorem](de-finettis-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.deFinettiEquiv`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Correspondence.html#TauCeti.Probability.deFinettiEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.deFinettiEquiv`](https://taucetiproject.org/docs/TauCeti/Probability/DeFinetti/Correspondence.html#TauCeti.Probability.deFinettiEquiv)
- [Source of `TauCeti.Probability.deFinettiEquiv` in TauCeti/Probability/DeFinetti/Correspondence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/DeFinetti/Correspondence.lean#L93)
- [Tau Ceti roadmap status: Exchangeability and de Finetti](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/Exchangeability/STATUS.md)
