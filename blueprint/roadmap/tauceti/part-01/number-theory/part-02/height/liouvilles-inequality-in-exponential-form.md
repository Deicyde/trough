---
declaration: theorem
origin: cited
lean: NumberField.eq_zero_of_norm_le_exp_of_house_le_exp, NumberField.one_le_norm_mul_house_pow, IsDedekindDomain.HeightOneSpectrum.neg_log_valuation_aeval_mul_log_absNorm_le
statement: formalized
proof: formalized
---

# Liouville's inequality in exponential form

Let `K` be a number field of degree `d`,
`σ : K →+* ℂ`, `y ∈ K` and `m ≠ 0` an integer with `m ^ N y` an algebraic integer. If
`‖σ y‖ ≤ exp A`, `⌈y⌉ ≤ exp B` and `|m| ^ N ≤ exp C` with `C + A + (d - 1) (C + B) < 0`,
then `y = 0`.

```lean
NumberField.eq_zero_of_norm_le_exp_of_house_le_exp.{u_3} {K : Type u_3} [Field K] [NumberField K]
  (σ : K →+* ℂ) {y : K} {m : ℤ} (hm : m ≠ 0) {N : ℕ} (hint : IsIntegral ℤ (↑m ^ N * y)) {A B C : ℝ}
  (hσ : ‖σ y‖ ≤ Real.exp A) (hy : NumberField.house y ≤ Real.exp B) (hmC : |↑m| ^ N ≤ Real.exp C)
  (h : C + A + ↑(Module.finrank ℚ K - 1) * (C + B) < 0) : y = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Liouville's inequality at a finite place](../number-field/liouvilles-inequality-at-a-finite-place.md)

## Lean

Formalized in Tau Ceti as [`NumberField.eq_zero_of_norm_le_exp_of_house_le_exp`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/House.html#NumberField.eq_zero_of_norm_le_exp_of_house_le_exp).

## Other forms

**Liouville's inequality in a number field `K` of degree `d`.** Formalized in Tau Ceti as [`NumberField.one_le_norm_mul_house_pow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/House.html#NumberField.one_le_norm_mul_house_pow).

```lean
NumberField.one_le_norm_mul_house_pow.{u_3} {K : Type u_3} [Field K] [NumberField K] {x : K}
  (hx : IsIntegral ℤ x) (h0 : x ≠ 0) (σ : K →+* ℂ) :
  1 ≤ ‖σ x‖ * NumberField.house x ^ (Module.finrank ℚ K - 1)
```

**Liouville's inequality for values of integer polynomials at a finite place.** Formalized in Tau Ceti as [`IsDedekindDomain.HeightOneSpectrum.neg_log_valuation_aeval_mul_log_absNorm_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Evaluation.html#IsDedekindDomain.HeightOneSpectrum.neg_log_valuation_aeval_mul_log_absNorm_le).

```lean
IsDedekindDomain.HeightOneSpectrum.neg_log_valuation_aeval_mul_log_absNorm_le.{u_1, u_2}
  {ι : Type u_1} [Fintype ι] {K : Type u_2} [Field K] [NumberField K]
  (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)) {P : MvPolynomial ι ℤ}
  {L : ι → ℕ} (hL : ∀ (i : ι), MvPolynomial.degreeOf i P ≤ L i) (x : ι → K) :
  -↑((IsDedekindDomain.HeightOneSpectrum.valuation K v) ((MvPolynomial.aeval x) P)).log *
      Real.log ↑(Ideal.absNorm v.asIdeal) ≤
    ↑(Module.finrank ℚ K) * Real.log (∑ s ∈ P.support, |↑(P.coeff s)|) +
      ∑ i, ↑(L i) * Height.logHeight₁ (x i)
```

## Sources

- [Tau Ceti documentation: `NumberField.eq_zero_of_norm_le_exp_of_house_le_exp`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/House.html#NumberField.eq_zero_of_norm_le_exp_of_house_le_exp)
- [Source of `NumberField.eq_zero_of_norm_le_exp_of_house_le_exp` in TauCeti/NumberTheory/Height/House.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Height/House.lean#L404)
