---
declaration: theorem
origin: cited
lean: Polynomial.inv_le_norm_ratCast_sub, IsAlgebraic.inv_le_norm_ratCast_sub, NumberField.one_le_norm_mul_house_pow, IsDedekindDomain.HeightOneSpectrum.abs_log_valuation_mul_log_absNorm_le_logHeight₁, IsAlgebraic.exists_pos_le_norm_aeval_mul_supNorm_pow, IsDedekindDomain.HeightOneSpectrum.neg_log_valuation_aeval_mul_log_absNorm_le, NumberField.eq_zero_of_norm_le_exp_of_house_le_exp
statement: formalized
proof: formalized
---

# Liouville's inequality

Let `f ∈ ℤ[X]` have degree `d` and a complex root `α`. Every
rational number `ξ` with `f(ξ) ≠ 0` satisfies `|ξ - α| ≥ (2 ^ (d - 1) M(f) H(ξ) ^ d)⁻¹`, where
`M(f)` is the Mahler measure of `f` and `H(ξ)` the height of `ξ`.

```lean
Polynomial.inv_le_norm_ratCast_sub (f : Polynomial ℤ) {α : ℂ}
  (hα : (Polynomial.map (Int.castRingHom ℂ) f).IsRoot α) {ξ : ℚ} (hξ : (Polynomial.aeval ξ) f ≠ 0) :
  (2 ^ (f.natDegree - 1) * (Polynomial.map (Int.castRingHom ℂ) f).mahlerMeasure *
        Height.mulHeight₁ ξ ^ f.natDegree)⁻¹ ≤
    ‖↑ξ - α‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.inv_le_norm_ratCast_sub`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Liouville.html#Polynomial.inv_le_norm_ratCast_sub).

## Other forms

**Liouville's inequality for an algebraic number.** Formalized in Tau Ceti as [`IsAlgebraic.inv_le_norm_ratCast_sub`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Liouville.html#IsAlgebraic.inv_le_norm_ratCast_sub).

```lean
IsAlgebraic.inv_le_norm_ratCast_sub {α : ℂ} (hα : IsAlgebraic ℚ α) {ξ : ℚ} (hξ : ↑ξ ≠ α) :
  (2 ^ ((minpoly ℚ α).natDegree - 1) *
          (Polynomial.map (Int.castRingHom ℂ) (TauCeti.primitiveMinpoly α)).mahlerMeasure *
        Height.mulHeight₁ ξ ^ (minpoly ℚ α).natDegree)⁻¹ ≤
    ‖↑ξ - α‖
```

**Liouville's inequality in a number field `K` of degree `d`.** Formalized in Tau Ceti as [`NumberField.one_le_norm_mul_house_pow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/House.html#NumberField.one_le_norm_mul_house_pow).

```lean
NumberField.one_le_norm_mul_house_pow.{u_3} {K : Type u_3} [Field K] [NumberField K] {x : K}
  (hx : IsIntegral ℤ x) (h0 : x ≠ 0) (σ : K →+* ℂ) :
  1 ≤ ‖σ x‖ * NumberField.house x ^ (Module.finrank ℚ K - 1)
```

**Liouville's inequality at a finite place.** Formalized in Tau Ceti as [`IsDedekindDomain.HeightOneSpectrum.abs_log_valuation_mul_log_absNorm_le_logHeight₁`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Places/Height.html#IsDedekindDomain.HeightOneSpectrum.abs_log_valuation_mul_log_absNorm_le_logHeight%E2%82%81).

```lean
IsDedekindDomain.HeightOneSpectrum.abs_log_valuation_mul_log_absNorm_le_logHeight₁.{u_1}
  {K : Type u_1} [Field K] [NumberField K]
  (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)) (x : K) :
  ↑|((IsDedekindDomain.HeightOneSpectrum.valuation K v) x).log| *
      Real.log ↑(Ideal.absNorm v.asIdeal) ≤
    Height.logHeight₁ x
```

**Liouville's inequality for the value of an integer polynomial.** Formalized in Tau Ceti as [`IsAlgebraic.exists_pos_le_norm_aeval_mul_supNorm_pow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/MahlerExponent.html#IsAlgebraic.exists_pos_le_norm_aeval_mul_supNorm_pow).

```lean
IsAlgebraic.exists_pos_le_norm_aeval_mul_supNorm_pow {ξ : ℂ} (hξ : IsAlgebraic ℚ ξ) (n : ℕ) :
  ∃ c > 0,
    ∀ (P : Polynomial ℤ),
      P.natDegree ≤ n →
        (Polynomial.aeval ξ) P ≠ 0 →
          c ≤ ‖(Polynomial.aeval ξ) P‖ * P.supNorm ^ ((minpoly ℚ ξ).natDegree - 1)
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

**Liouville's inequality in exponential form.** Formalized in Tau Ceti as [`NumberField.eq_zero_of_norm_le_exp_of_house_le_exp`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/House.html#NumberField.eq_zero_of_norm_le_exp_of_house_le_exp).

```lean
NumberField.eq_zero_of_norm_le_exp_of_house_le_exp.{u_3} {K : Type u_3} [Field K] [NumberField K]
  (σ : K →+* ℂ) {y : K} {m : ℤ} (hm : m ≠ 0) {N : ℕ} (hint : IsIntegral ℤ (↑m ^ N * y)) {A B C : ℝ}
  (hσ : ‖σ y‖ ≤ Real.exp A) (hy : NumberField.house y ≤ Real.exp B) (hmC : |↑m| ^ N ≤ Real.exp C)
  (h : C + A + ↑(Module.finrank ℚ K - 1) * (C + B) < 0) : y = 0
```

## Sources

- [Tau Ceti documentation: `Polynomial.inv_le_norm_ratCast_sub`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Liouville.html#Polynomial.inv_le_norm_ratCast_sub)
- [Source of `Polynomial.inv_le_norm_ratCast_sub` in TauCeti/NumberTheory/DiophantineApproximation/Liouville.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/DiophantineApproximation/Liouville.lean#L44)
