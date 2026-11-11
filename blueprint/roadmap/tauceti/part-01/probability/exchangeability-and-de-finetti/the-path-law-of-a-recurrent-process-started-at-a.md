---
declaration: theorem
origin: cited
lean: TauCeti.Probability.Recurrent.pathLaw_eq_map_pathOfExcursions
statement: formalized
proof: formalized
---

# The path law of a recurrent process started at `a₀` is the image of its excursion law

Only the base state's singleton needs to be measurable.

```lean
TauCeti.Probability.Recurrent.pathLaw_eq_map_pathOfExcursions.{u_1, u_2} {Ω : Type u_1}
  {α : Type u_2} [MeasurableSpace Ω] [MeasurableSpace α] {μ : MeasureTheory.Measure Ω}
  {X : ℕ → Ω → α} {a₀ : α} (hrec : TauCeti.Probability.Recurrent μ X)
  (hX : ∀ (i : ℕ), AEMeasurable (X i) μ) (ha₀ : MeasurableSet {a₀})
  (h0 : ∀ᵐ (ω : Ω) ∂μ, X 0 ω = a₀) :
  TauCeti.Probability.pathLaw μ X =
    MeasureTheory.Measure.map (TauCeti.pathOfExcursions a₀)
      (TauCeti.Probability.pathLaw μ (TauCeti.Probability.excursionProcess X a₀))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.Recurrent.pathLaw_eq_map_pathOfExcursions`](https://taucetiproject.org/docs/TauCeti/Probability/Recurrent/Excursion.html#TauCeti.Probability.Recurrent.pathLaw_eq_map_pathOfExcursions).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.Recurrent.pathLaw_eq_map_pathOfExcursions`](https://taucetiproject.org/docs/TauCeti/Probability/Recurrent/Excursion.html#TauCeti.Probability.Recurrent.pathLaw_eq_map_pathOfExcursions)
- [Source of `TauCeti.Probability.Recurrent.pathLaw_eq_map_pathOfExcursions` in TauCeti/Probability/Recurrent/Excursion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Recurrent/Excursion.lean#L37)
- [Tau Ceti roadmap status: Exchangeability and de Finetti](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/Exchangeability/STATUS.md)
