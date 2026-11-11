---
declaration: theorem
origin: cited
lean: TauCeti.totallyBounded_of_comp_add_sub_of_isBounded_of_ae_eq_zero_compl
statement: formalized
proof: formalized
---

# The Fréchet--Kolmogorov criterion for a family vanishing almost everywhere off a fixed bounded set

**The Fréchet--Kolmogorov criterion for a family vanishing almost everywhere off a fixed bounded
set**, the form that Rellich--Kondrachov for `W^{1,p}_0(Ω)` consumes. For such functions the
tightness hypothesis is automatic, so an `Lᵖ`-bounded family whose translation increments are
uniformly small in `Lᵖ` is totally bounded.

```lean
TauCeti.totallyBounded_of_comp_add_sub_of_isBounded_of_ae_eq_zero_compl.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [MeasurableSpace E] [BorelSpace E] [ProperSpace E]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {mu : MeasureTheory.Measure E}
  [mu.IsAddHaarMeasure] {p : ENNReal} [Fact (1 ≤ p)] (hp' : p ≠ ⊤)
  {S : Set ↥(MeasureTheory.Lp F p mu)} {s : Set E} (hs : Bornology.IsBounded s)
  (hsupp : ∀ f ∈ S, ∀ᵐ (x : E) ∂mu, x ∉ s → ↑↑f x = 0) {M : ENNReal} (hM : M ≠ ⊤)
  (hbdd : ∀ f ∈ S, MeasureTheory.eLpNorm (↑↑f) p mu ≤ M)
  (htrans :
    ∀ (ε : ENNReal),
      0 < ε →
        ∃ δ > 0,
          ∀ f ∈ S,
            ∀ (h : E), ‖h‖ < δ → MeasureTheory.eLpNorm (fun x => ↑↑f (x + h) - ↑↑f x) p mu ≤ ε) :
  TotallyBounded S
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Fréchet--Kolmogorov compactness criterion](the-frechet-kolmogorov-compactness-criterion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.totallyBounded_of_comp_add_sub_of_isBounded_of_ae_eq_zero_compl`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/FrechetKolmogorov.html#TauCeti.totallyBounded_of_comp_add_sub_of_isBounded_of_ae_eq_zero_compl).

## Sources

- [Tau Ceti documentation: `TauCeti.totallyBounded_of_comp_add_sub_of_isBounded_of_ae_eq_zero_compl`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/FrechetKolmogorov.html#TauCeti.totallyBounded_of_comp_add_sub_of_isBounded_of_ae_eq_zero_compl)
- [Source of `TauCeti.totallyBounded_of_comp_add_sub_of_isBounded_of_ae_eq_zero_compl` in TauCeti/MeasureTheory/Function/Lp/FrechetKolmogorov.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/Lp/FrechetKolmogorov.lean#L345)
