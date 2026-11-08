---
declaration: theorem
origin: cited
lean: TauCeti.summatory_mul_le_of_summatory_le, TauCeti.tsum_mul_le_of_summatory_le
statement: formalized
proof: formalized
---

# A one-sided Abel bound

Let every index have `N`-value at least the cutoff `a ≥ 0`, and
let `g` be nonincreasing on `[a, x]` with `0 ≤ g x`.  If the summatory function of a real weight `w`
is at most `C` at every cutoff in `[a, x]`, then the summatory function at `x` of the twisted weight
`i ↦ w i * g (N i)` is at most `C * g a`.

No sign condition is imposed on `w` or on `C`: only the partial sums of `w` are controlled.

```lean
TauCeti.summatory_mul_le_of_summatory_le.{u_1} {ι : Type u_1} (N : ι → ℕ) [Northcott N] {a : ℝ}
  (ha : 0 ≤ a) (hN : ∀ (i : ι), a ≤ ↑(N i)) (w : ι → ℝ) {g : ℝ → ℝ} {C x : ℝ} (hx : a ≤ x)
  (hC : ∀ t ∈ Set.Icc a x, TauCeti.summatory N w t ≤ C)
  (hg_diff : ∀ t ∈ Set.Icc a x, DifferentiableAt ℝ g t)
  (hg_int : MeasureTheory.IntegrableOn (deriv g) (Set.Icc a x) MeasureTheory.volume)
  (hg_deriv : ∀ t ∈ Set.Icc a x, deriv g t ≤ 0) (hg_nonneg : 0 ≤ g x) :
  TauCeti.summatory N (fun i => w i * g ↑(N i)) x ≤ C * g a
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.summatory_mul_le_of_summatory_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/AbelSummation.html#TauCeti.summatory_mul_le_of_summatory_le).

## Other forms

**A one-sided Abel bound for the full series.** Formalized in Tau Ceti as [`TauCeti.tsum_mul_le_of_summatory_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/AbelSummation.html#TauCeti.tsum_mul_le_of_summatory_le).

```lean
TauCeti.tsum_mul_le_of_summatory_le.{u_1} {ι : Type u_1} (N : ι → ℕ) [Northcott N] {a : ℝ}
  (ha : 0 ≤ a) (hN : ∀ (i : ι), a ≤ ↑(N i)) (w : ι → ℝ) {g : ℝ → ℝ} {C : ℝ}
  (hC : ∀ (t : ℝ), a ≤ t → TauCeti.summatory N w t ≤ C)
  (hg_diff : ∀ (t : ℝ), a ≤ t → DifferentiableAt ℝ g t)
  (hg_int :
    ∀ (x : ℝ), a ≤ x → MeasureTheory.IntegrableOn (deriv g) (Set.Icc a x) MeasureTheory.volume)
  (hg_deriv : ∀ (t : ℝ), a ≤ t → deriv g t ≤ 0) (hg_nonneg : ∀ (t : ℝ), a ≤ t → 0 ≤ g t)
  (hsum : Summable fun i => w i * g ↑(N i)) : ∑' (i : ι), w i * g ↑(N i) ≤ C * g a
```

## Sources

- [Tau Ceti documentation: `TauCeti.summatory_mul_le_of_summatory_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/AbelSummation.html#TauCeti.summatory_mul_le_of_summatory_le)
- [Source of `TauCeti.summatory_mul_le_of_summatory_le` in TauCeti/NumberTheory/ArithmeticDirichletSeries/AbelSummation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ArithmeticDirichletSeries/AbelSummation.lean#L339)
