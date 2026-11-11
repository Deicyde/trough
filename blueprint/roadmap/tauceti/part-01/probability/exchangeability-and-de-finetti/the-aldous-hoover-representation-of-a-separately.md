---
declaration: theorem
origin: cited
lean: TauCeti.Probability.SeparatelyExchangeable.exists_map_separateArray_eq
statement: formalized
proof: formalized
---

# The Aldous--Hoover representation of a separately exchangeable array

Every separately
exchangeable probability law `ρ` on arrays with values in a standard Borel space is the law of a
measurable separate Aldous--Hoover coding: there is a measurable `F : I × I × I × I → α` with `ρ`
the law of `X i j = F(U, U_row i, U_col j, U_cell i j)` under independent uniform noise.

```lean
TauCeti.Probability.SeparatelyExchangeable.exists_map_separateArray_eq.{u_1} {α : Type u_1}
  [MeasurableSpace α] [StandardBorelSpace α] {ρ : MeasureTheory.Measure (ℕ × ℕ → α)}
  [MeasureTheory.IsProbabilityMeasure ρ]
  (hρ : TauCeti.Probability.SeparatelyExchangeable ρ fun p x => x p) :
  ∃ F,
    Measurable F ∧
      MeasureTheory.Measure.map (fun u p => TauCeti.Probability.AldousHoover.separateArray F p u)
          (TauCeti.Probability.AldousHoover.noiseMeasure TauCeti.Probability.AldousHoover.Axis
            (ℕ × ℕ)) =
        ρ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [De Finetti's theorem](de-finettis-theorem.md)
- [De Finetti's theorem for the rows of a block of pairs](../other-results/de-finettis-theorem-for-the-rows-of-a-block-of-p.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.SeparatelyExchangeable.exists_map_separateArray_eq`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Arrays/AldousHoover/Separate/Representation.html#TauCeti.Probability.SeparatelyExchangeable.exists_map_separateArray_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.SeparatelyExchangeable.exists_map_separateArray_eq`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/Arrays/AldousHoover/Separate/Representation.html#TauCeti.Probability.SeparatelyExchangeable.exists_map_separateArray_eq)
- [Source of `TauCeti.Probability.SeparatelyExchangeable.exists_map_separateArray_eq` in TauCeti/Probability/Exchangeability/Arrays/AldousHoover/Separate/Representation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Exchangeability/Arrays/AldousHoover/Separate/Representation.lean#L182)
- [Tau Ceti roadmap status: Exchangeability and de Finetti](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/Exchangeability/STATUS.md)
