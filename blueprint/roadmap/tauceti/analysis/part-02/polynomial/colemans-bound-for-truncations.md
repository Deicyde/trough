---
declaration: theorem
origin: cited
lean: PowerSeries.norm_coeff_colemanDBounded_trunc_le
statement: formalized
proof: formalized
---

# Coleman's bound for truncations

Let `ρ` be a nonnegative antitone Newton majorant of a
power series `F`, `‖coeff j F‖ ≤ ∏ i < j, ρ i`, and let `B` be restricted at every radius `ρ i`
with `B(0) = 0`. Then the Coleman transforms of the truncations of `F` along the truncations of
`B` satisfy `‖coeff k D_(n,m)(trunc a B, trunc b F)‖ ≤ ∏ i < k, β_B(ρ i)`, uniformly in the ranks,
degree bounds and truncation orders. In particular this bounds
`D_(N,M)(trunc (M + 1) B, trunc (N + 1) F)`.

```lean
PowerSeries.norm_coeff_colemanDBounded_trunc_le.{u_1} {R : Type u_1} [NormedCommRing R]
  [NormOneClass R] [IsUltrametricDist R] {F B : PowerSeries R} {ρ : ℕ → ℝ}
  (hρ₀ : ∀ (i : ℕ), 0 ≤ ρ i) (hρ : Antitone ρ)
  (hF : ∀ (j : ℕ), ‖(PowerSeries.coeff j) F‖ ≤ ∏ i ∈ Finset.range j, ρ i)
  (hB : ∀ (i : ℕ), PowerSeries.IsRestricted (ρ i) B) (hB₀ : (PowerSeries.coeff 0) B = 0)
  (n m a b k : ℕ) :
  ‖(((PowerSeries.trunc a) B).colemanDBounded ((PowerSeries.trunc b) F) n m).coeff k‖ ≤
    ∏ i ∈ Finset.range k, B.colemanMajorant (ρ i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Coleman's coefficient bound](colemans-coefficient-bound.md)

## Lean

Formalized in Tau Ceti as [`PowerSeries.norm_coeff_colemanDBounded_trunc_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Polynomial/Coleman/Basic.html#PowerSeries.norm_coeff_colemanDBounded_trunc_le).

## Sources

- [Tau Ceti documentation: `PowerSeries.norm_coeff_colemanDBounded_trunc_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Polynomial/Coleman/Basic.html#PowerSeries.norm_coeff_colemanDBounded_trunc_le)
- [Source of `PowerSeries.norm_coeff_colemanDBounded_trunc_le` in TauCeti/Analysis/Polynomial/Coleman/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Polynomial/Coleman/Basic.lean#L391)
