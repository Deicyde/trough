---
declaration: theorem
origin: cited
lean: TauCeti.measureReal_le_abs_card_filter_sub_le
statement: formalized
proof: formalized
---

# Hoeffding's inequality for a color count

Color the points of a finite type `ι`
independently according to a `PMF` `q` on `κ`. The number of points of `T` with color `c`
deviates from its mean `q c * #T` by at least `a ≥ 0` with probability at most
`2 * exp (-2 a² / #T)`.

```lean
TauCeti.measureReal_le_abs_card_filter_sub_le.{u_1, u_2} {ι : Type u_1} {κ : Type u_2}
  [DecidableEq κ] [Fintype ι] [MeasurableSpace κ] [MeasurableSingletonClass κ] (q : PMF κ)
  (T : Finset ι) (c : κ) {a : ℝ} (ha : 0 ≤ a) :
  (MeasureTheory.Measure.pi fun x => q.toMeasure).real
      {x | a ≤ |↑{e ∈ T | x e = c}.card - (q c).toReal * ↑T.card|} ≤
    2 * Real.exp (-2 * a ^ 2 / ↑T.card)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.measureReal_le_abs_card_filter_sub_le`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Enumerative/RandomColoring.html#TauCeti.measureReal_le_abs_card_filter_sub_le).

## Sources

- [Tau Ceti documentation: `TauCeti.measureReal_le_abs_card_filter_sub_le`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Enumerative/RandomColoring.html#TauCeti.measureReal_le_abs_card_filter_sub_le)
- [Source of `TauCeti.measureReal_le_abs_card_filter_sub_le` in TauCeti/Combinatorics/Enumerative/RandomColoring.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Enumerative/RandomColoring.lean#L65)
