---
declaration: theorem
origin: cited
lean: TauCeti.Probability.separatelyExchangeable_iff_exists_map_separateArray_eq
statement: formalized
proof: formalized
---

# Separately exchangeable arrays are exactly the Aldous--Hoover codings in law

An array
process with a.e.-measurable entries in a standard Borel space, on a probability space, is
separately exchangeable if and only if its law is the law of a measurable separate Aldous--Hoover
coding `X i j = F(U, U_row i, U_col j, U_cell i j)` under independent uniform noise.

```lean
TauCeti.Probability.separatelyExchangeable_iff_exists_map_separateArray_eq.{u_1, u_2} {α : Type u_1}
  [MeasurableSpace α] [StandardBorelSpace α] {Ω : Type u_2} [MeasurableSpace Ω]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsProbabilityMeasure μ] {X : ℕ × ℕ → Ω → α}
  (hX : ∀ (p : ℕ × ℕ), AEMeasurable (X p) μ) :
  TauCeti.Probability.SeparatelyExchangeable μ X ↔
    ∃ F,
      Measurable F ∧
        MeasureTheory.Measure.map (fun u p => TauCeti.Probability.AldousHoover.separateArray F p u)
            (TauCeti.Probability.AldousHoover.noiseMeasure TauCeti.Probability.AldousHoover.Axis
              (ℕ × ℕ)) =
          MeasureTheory.Measure.map (fun ω p => X p ω) μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [De Finetti's theorem](de-finettis-theorem.md)
- [De Finetti's theorem for the rows of a block of pairs](../other-results/de-finettis-theorem-for-the-rows-of-a-block-of-p.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.separatelyExchangeable_iff_exists_map_separateArray_eq`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Arrays/AldousHoover/Separate/Representation.html#TauCeti.Probability.separatelyExchangeable_iff_exists_map_separateArray_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.separatelyExchangeable_iff_exists_map_separateArray_eq`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Arrays/AldousHoover/Separate/Representation.html#TauCeti.Probability.separatelyExchangeable_iff_exists_map_separateArray_eq)
- [Source of `TauCeti.Probability.separatelyExchangeable_iff_exists_map_separateArray_eq` in TauCeti/Probability/Exchangeability/Arrays/AldousHoover/Separate/Representation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Exchangeability/Arrays/AldousHoover/Separate/Representation.lean#L245)
- [Tau Ceti roadmap status: Exchangeability and de Finetti](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/Exchangeability/STATUS.md)
