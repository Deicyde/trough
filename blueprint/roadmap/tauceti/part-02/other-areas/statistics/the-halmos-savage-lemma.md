---
declaration: theorem
origin: cited
lean: TauCeti.exists_absolutelyContinuous_countableMixture
statement: formalized
proof: formalized
---

# The Halmos–Savage lemma

A nonempty family of measures dominated by an s-finite measure
`μ` is dominated by one of its countable mixtures. A family with real densities with respect to
`μ` is dominated by `μ`, by `TauCeti.HasDensity.absolutelyContinuous`.

```lean
TauCeti.exists_absolutelyContinuous_countableMixture.{u_1, u_2} {Θ : Type u_1} {X : Type u_2}
  [MeasurableSpace X] [Nonempty Θ] (P : Θ → MeasureTheory.Measure X) (μ : MeasureTheory.Measure X)
  [MeasureTheory.SFinite μ] (hP : ∀ (θ : Θ), (P θ).AbsolutelyContinuous μ) :
  ∃ θs, ∀ (θ : Θ), (P θ).AbsolutelyContinuous (TauCeti.countableMixture P θs)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_absolutelyContinuous_countableMixture`](https://taucetiproject.org/docs/TauCeti/Statistics/Experiments/Mixture.html#TauCeti.exists_absolutelyContinuous_countableMixture).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_absolutelyContinuous_countableMixture`](https://taucetiproject.org/docs/TauCeti/Statistics/Experiments/Mixture.html#TauCeti.exists_absolutelyContinuous_countableMixture)
- [Source of `TauCeti.exists_absolutelyContinuous_countableMixture` in TauCeti/Statistics/Experiments/Mixture.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Statistics/Experiments/Mixture.lean#L149)
