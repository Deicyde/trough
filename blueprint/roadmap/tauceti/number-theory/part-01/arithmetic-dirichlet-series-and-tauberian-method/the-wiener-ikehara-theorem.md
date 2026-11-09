---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.wienerIkehara, TauCeti.LSeries.wienerIkehara_nat, TauCeti.LSeries.wienerIkehara_rpow, TauCeti.LSeries.wienerIkehara_of_forall_monotone_dual, TauCeti.LSeries.wienerIkehara_of_eventually_nonneg, TauCeti.LSeries.wienerIkehara_zero
statement: formalized
proof: formalized
---

# The Wiener--Ikehara theorem

Let `a n ≥ 0` have Dirichlet series with sum `F s` on
`Re s > 1`, and let `G` be continuous on `Re s ≥ 1` with `G s = F s - κ / (s - 1)` on `Re s > 1`.
Then `x⁻¹ ∑_{1 ≤ n ≤ x} a n → κ` as `x → ∞`.

```lean
TauCeti.LSeries.wienerIkehara {a : ℕ → ℝ} {F G : ℂ → ℂ} {κ : ℝ} (ha : 0 ≤ a)
  (hF : ∀ (s : ℂ), 1 < s.re → LSeriesHasSum (fun n => ↑(a n)) s (F s))
  (hG : ContinuousOn G {s | 1 ≤ s.re}) (hGF : ∀ (s : ℂ), 1 < s.re → G s = F s - ↑κ / (s - 1)) :
  Filter.Tendsto (fun x => x⁻¹ * ∑ n ∈ Finset.Icc 1 ⌊x⌋₊, a n) Filter.atTop (nhds κ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Abel's inequality, comparison form](../../../algebra/other-results/abels-inequality-comparison-form.md)
- [The Chebyshev bound](../../part-02/l-series/the-chebyshev-bound.md)
- [Riemann--Lebesgue on a vertical line](../../../analysis/part-02/fourier/riemann-lebesgue-on-a-vertical-line.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.wienerIkehara`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/WienerIkehara/SharpCutoff.html#TauCeti.LSeries.wienerIkehara).

## Other forms

**The Wiener--Ikehara theorem at natural cutoffs.** Formalized in Tau Ceti as [`TauCeti.LSeries.wienerIkehara_nat`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/WienerIkehara/Variants.html#TauCeti.LSeries.wienerIkehara_nat).

```lean
TauCeti.LSeries.wienerIkehara_nat {a : ℕ → ℝ} {F G : ℂ → ℂ} {κ : ℝ}
  (ha : ∀ᶠ (n : ℕ) in Filter.atTop, 0 ≤ a n)
  (hF : ∀ (s : ℂ), 1 < s.re → LSeriesHasSum (fun n => ↑(a n)) s (F s))
  (hG : ContinuousOn G {s | 1 ≤ s.re}) (hGF : ∀ (s : ℂ), 1 < s.re → G s = F s - ↑κ / (s - 1)) :
  Filter.Tendsto (fun N => (↑N)⁻¹ * ∑ n ∈ Finset.Icc 1 N, a n) Filter.atTop (nhds κ)
```

**The Wiener--Ikehara theorem for a pole at a positive abscissa.** Formalized in Tau Ceti as [`TauCeti.LSeries.wienerIkehara_rpow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/WienerIkehara/Variants.html#TauCeti.LSeries.wienerIkehara_rpow).

```lean
TauCeti.LSeries.wienerIkehara_rpow {a : ℕ → ℝ} {F G : ℂ → ℂ} {κ σ : ℝ} (hσ : 0 < σ)
  (ha : ∀ᶠ (n : ℕ) in Filter.atTop, 0 ≤ a n)
  (hF : ∀ (s : ℂ), σ < s.re → LSeriesHasSum (fun n => ↑(a n)) s (F s))
  (hG : ContinuousOn G {s | σ ≤ s.re}) (hGF : ∀ (s : ℂ), σ < s.re → G s = F s - ↑κ / (s - ↑σ)) :
  Filter.Tendsto (fun x => (x ^ σ)⁻¹ * ∑ n ∈ Finset.Icc 1 ⌊x⌋₊, a n) Filter.atTop (nhds (κ / σ))
```

**The Wiener--Ikehara theorem for coefficients in an ordered vector space.** Formalized in Tau Ceti as [`TauCeti.LSeries.wienerIkehara_of_forall_monotone_dual`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/WienerIkehara/Ordered.html#TauCeti.LSeries.wienerIkehara_of_forall_monotone_dual).

```lean
TauCeti.LSeries.wienerIkehara_of_forall_monotone_dual.{u_1, u_2} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [PartialOrder E]
  [IsOrderedAddMonoid E] [PosSMulMono ℝ E] [OrderClosedTopology E] {ι : Type u_2}
  {φ : ι → StrongDual ℝ E} (hφ : ∀ (i : ι), Monotone ⇑(φ i))
  (hspan : ∀ (ψ : StrongDual ℝ E), Monotone ⇑ψ → ψ ∈ Submodule.span ℝ (Set.range φ)) {a : ℕ → E}
  {κ : E} (ha : ∀ᶠ (n : ℕ) in Filter.atTop, 0 ≤ a n)
  (hFG :
    ∀ (i : ι),
      ∃ F G,
        (∀ (s : ℂ), 1 < s.re → LSeriesHasSum (fun n => ↑((φ i) (a n))) s (F s)) ∧
          ContinuousOn G {s | 1 ≤ s.re} ∧ ∀ (s : ℂ), 1 < s.re → G s = F s - ↑((φ i) κ) / (s - 1)) :
  Filter.Tendsto (fun x => x⁻¹ • ∑ n ∈ Finset.Icc 1 ⌊x⌋₊, a n) Filter.atTop (nhds κ)
```

**The Wiener--Ikehara theorem for eventually nonnegative coefficients.** Formalized in Tau Ceti as [`TauCeti.LSeries.wienerIkehara_of_eventually_nonneg`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/WienerIkehara/Variants.html#TauCeti.LSeries.wienerIkehara_of_eventually_nonneg).

```lean
TauCeti.LSeries.wienerIkehara_of_eventually_nonneg {a : ℕ → ℝ} {F G : ℂ → ℂ} {κ : ℝ}
  (ha : ∀ᶠ (n : ℕ) in Filter.atTop, 0 ≤ a n)
  (hF : ∀ (s : ℂ), 1 < s.re → LSeriesHasSum (fun n => ↑(a n)) s (F s))
  (hG : ContinuousOn G {s | 1 ≤ s.re}) (hGF : ∀ (s : ℂ), 1 < s.re → G s = F s - ↑κ / (s - 1)) :
  Filter.Tendsto (fun x => x⁻¹ * ∑ n ∈ Finset.Icc 1 ⌊x⌋₊, a n) Filter.atTop (nhds κ)
```

**The Wiener--Ikehara theorem with zero residue.** Formalized in Tau Ceti as [`TauCeti.LSeries.wienerIkehara_zero`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/WienerIkehara/SharpCutoff.html#TauCeti.LSeries.wienerIkehara_zero).

```lean
TauCeti.LSeries.wienerIkehara_zero {a : ℕ → ℝ} {F G : ℂ → ℂ} (ha : 0 ≤ a)
  (hF : ∀ (s : ℂ), 1 < s.re → LSeriesHasSum (fun n => ↑(a n)) s (F s))
  (hG : ContinuousOn G {s | 1 ≤ s.re}) (hGF : ∀ (s : ℂ), 1 < s.re → G s = F s) :
  Filter.Tendsto (fun x => x⁻¹ * ∑ n ∈ Finset.Icc 1 ⌊x⌋₊, a n) Filter.atTop (nhds 0)
```

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.wienerIkehara`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/WienerIkehara/SharpCutoff.html#TauCeti.LSeries.wienerIkehara)
- [Source of `TauCeti.LSeries.wienerIkehara` in TauCeti/NumberTheory/LSeries/WienerIkehara/SharpCutoff.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LSeries/WienerIkehara/SharpCutoff.lean#L297)
- [Tau Ceti roadmap status: Arithmetic Dirichlet series and Tauberian methods](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ArithmeticDirichletSeries/STATUS.md)
