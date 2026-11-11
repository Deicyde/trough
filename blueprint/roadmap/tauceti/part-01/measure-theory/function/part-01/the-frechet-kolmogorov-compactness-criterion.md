---
declaration: theorem
origin: cited
lean: TauCeti.totallyBounded_of_comp_add_sub_of_unifTight
statement: formalized
proof: formalized
---

# The Fréchet--Kolmogorov compactness criterion

For `1 ≤ p < ∞`, a family `S` of `Lᵖ`
functions is totally bounded as soon as it is bounded in `Lᵖ`, its translation increments are
uniformly small in `Lᵖ`, and it is uniformly tight in the sense of `MeasureTheory.UnifTight`.

Dropping either of the last two hypotheses breaks the conclusion: on `ℝ` the concentrating family
`n ^ (1/p) 1_{[0, 1/n]}` satisfies all but the smallness of translations, and the escaping family
`f(· - n)` of translates of a single nonzero `f` satisfies all but tightness, and neither is
totally bounded.

```lean
TauCeti.totallyBounded_of_comp_add_sub_of_unifTight.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [MeasurableSpace E] [BorelSpace E] [ProperSpace E] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {p : ENNReal} [Fact (1 ≤ p)] (hp' : p ≠ ⊤) {S : Set ↥(MeasureTheory.Lp F p mu)} {M : ENNReal}
  (hM : M ≠ ⊤) (hbdd : ∀ f ∈ S, MeasureTheory.eLpNorm (↑↑f) p mu ≤ M)
  (htrans :
    ∀ (ε : ENNReal),
      0 < ε →
        ∃ δ > 0,
          ∀ f ∈ S,
            ∀ (h : E), ‖h‖ < δ → MeasureTheory.eLpNorm (fun x => ↑↑f (x + h) - ↑↑f x) p mu ≤ ε)
  (htight : MeasureTheory.UnifTight (fun i => ↑↑↑i) p mu) : TotallyBounded S
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Arzelà–Ascoli theorem in `C(X, Y)`](../../../topology/other-results/the-arzela-ascoli-theorem-in-c-x-y.md)
- [Hölder's bound on an average](../../integral/part-01/holders-bound-on-an-average.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.totallyBounded_of_comp_add_sub_of_unifTight`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/FrechetKolmogorov.html#TauCeti.totallyBounded_of_comp_add_sub_of_unifTight).

## Sources

- [Tau Ceti documentation: `TauCeti.totallyBounded_of_comp_add_sub_of_unifTight`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/FrechetKolmogorov.html#TauCeti.totallyBounded_of_comp_add_sub_of_unifTight)
- [Source of `TauCeti.totallyBounded_of_comp_add_sub_of_unifTight` in TauCeti/MeasureTheory/Function/Lp/FrechetKolmogorov.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/Lp/FrechetKolmogorov.lean#L265)
