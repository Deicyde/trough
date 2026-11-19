---
catalog: module
lean: CompPoly.CPolynomial.toPoly_smul, CompPoly.CPolynomial.toPolyLinearEquiv, CompPoly.CPolynomial.toPolyLinearEquiv_apply, CompPoly.CPolynomial.degree_le_iff_coeff_zero, CompPoly.CPolynomial.degree_lt_iff_coeff_zero, CompPoly.CPolynomial.degreeLE_mono, CompPoly.CPolynomial.degreeLT_mono, CompPoly.CPolynomial.degreeLT_succ_eq_degreeLE, CompPoly.CPolynomial.monomial_mem_degreeLT, CompPoly.CPolynomial.degreeLTEquiv_invFun_mem, CompPoly.CPolynomial.degreeLTEquiv_left_inv, CompPoly.CPolynomial.degreeLTEquiv_right_inv, CompPoly.CPolynomial.degreeLTEquiv, CompPoly.CPolynomial.degreeLTLinearEquiv, CompPoly.CPolynomial.degreeLTEquiv_toPoly, CompPoly.CPolynomial.degreeLTEquiv_eq_zero_iff_eq_zero, CompPoly.CPolynomial.eval_eq_sum_degreeLTEquiv, CompPoly.CPolynomial.degree_toPoly_ofFinCoeff_lt, CompPoly.CPolynomial.degree_C_le, CompPoly.CPolynomial.degree_C, CompPoly.CPolynomial.leadingCoeff_C, CompPoly.CPolynomial.degree_X, CompPoly.CPolynomial.natDegree_X, CompPoly.CPolynomial.leadingCoeff_X, CompPoly.CPolynomial.degree_one, CompPoly.CPolynomial.natDegree_one, CompPoly.CPolynomial.leadingCoeff_one, CompPoly.CPolynomial.degree_add_le, CompPoly.CPolynomial.degree_add_eq_left_of_degree_lt, CompPoly.CPolynomial.degree_add_eq_right_of_degree_lt, CompPoly.CPolynomial.degree_mul_le, CompPoly.CPolynomial.natDegree_mul_le, CompPoly.CPolynomial.degree_pow_le, CompPoly.CPolynomial.natDegree_pow_le, CompPoly.CPolynomial.natDegree_pow_le_of_le, CompPoly.CPolynomial.degree_neg, CompPoly.CPolynomial.natDegree_neg, CompPoly.CPolynomial.leadingCoeff_neg, CompPoly.CPolynomial.degree_sub_le, CompPoly.CPolynomial.natDegree_sub_le, CompPoly.CPolynomial.degree_X_sub_C, CompPoly.CPolynomial.natDegree_X_sub_C, CompPoly.CPolynomial.degree_mul, CompPoly.CPolynomial.natDegree_mul, CompPoly.CPolynomial.leadingCoeff_mul, CompPoly.CPolynomial.degree_pow, CompPoly.CPolynomial.natDegree_pow, CompPoly.CPolynomial.leadingCoeff_pow
statement: formalized
proof: formalized
---

# `toPoly` Degree Lemmas

`CompPoly.Univariate.ToPoly.Degree`, in [CompPoly/Univariate/ToPoly/Degree.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean), by Quang Dao, Gregor Mitscha-Baude, Derek Sorensen, Julian Sutherland.

> Degree lemmas for the computable-univariate to `Polynomial` conversion.

`CompPoly.CPolynomial.toPoly_smul` (lemma, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L34))

```lean
lemma toPoly_smul (r : R) (p : CPolynomial R) :
    (r • p).toPoly = r • p.toPoly
```

`CompPoly.CPolynomial.toPolyLinearEquiv` (definition, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L39))

```lean
noncomputable def toPolyLinearEquiv : CPolynomial R ≃ₗ[R] R[X]
```

`CompPoly.CPolynomial.toPolyLinearEquiv_apply` (theorem, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L49))

> The forward map of `toPolyLinearEquiv` is `toPoly`.

```lean
theorem toPolyLinearEquiv_apply (p : CPolynomial R) : toPolyLinearEquiv p = p.toPoly
```

`CompPoly.CPolynomial.degree_le_iff_coeff_zero` (theorem, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L52))

```lean
theorem degree_le_iff_coeff_zero (p : CPolynomial R) (n : WithBot ℕ) :
    p.degree ≤ n ↔ ∀ k : ℕ, n < k → p.coeff k = 0
```

`CompPoly.CPolynomial.degree_lt_iff_coeff_zero` (theorem, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L57))

```lean
theorem degree_lt_iff_coeff_zero (p : CPolynomial R) (n : ℕ) :
    p.degree < n ↔ ∀ k : ℕ, n ≤ k → p.coeff k = 0
```

`CompPoly.CPolynomial.degreeLE_mono` (theorem, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L63))

```lean
theorem degreeLE_mono (m n : WithBot ℕ) (h_lessThan : m ≤ n) :
    degreeLE (R := R) m ≤ degreeLE (R := R) n
```

`CompPoly.CPolynomial.degreeLT_mono` (theorem, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L68))

```lean
theorem degreeLT_mono {m n : ℕ} (h : m ≤ n) :
    degreeLT (R := R) m ≤ degreeLT (R := R) n
```

`CompPoly.CPolynomial.degreeLT_succ_eq_degreeLE` (theorem, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L73))

```lean
theorem degreeLT_succ_eq_degreeLE {n : ℕ} :
    degreeLT (R := R) (n + 1) = degreeLE (R := R) ↑n
```

`CompPoly.CPolynomial.monomial_mem_degreeLT` (lemma, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L86))

```lean
lemma monomial_mem_degreeLT [DecidableEq R] {n : ℕ} (i : Fin n) (c : R) :
    monomial (R := R) (i : ℕ) c ∈ degreeLT (R := R) n
```

`CompPoly.CPolynomial.degreeLTEquiv_invFun_mem` (lemma, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L93))

```lean
lemma degreeLTEquiv_invFun_mem [DecidableEq R] (n : ℕ) (f : Fin n → R) :
    Finset.univ.sum (fun i : Fin n => monomial (R := R) (i : ℕ) (f i)) ∈ degreeLT (R := R) n
```

`CompPoly.CPolynomial.degreeLTEquiv_left_inv` (lemma, [line 101](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L101))

```lean
lemma degreeLTEquiv_left_inv [DecidableEq R] (n : ℕ)
    (p : ↥(degreeLT (R := R) n)) :
    (⟨
      Finset.univ.sum (fun i : Fin n => monomial (R := R) (↑i) (coeff p.1 i)),
      degreeLTEquiv_invFun_mem (R := R) n (fun i => coeff p.1 i)
    ⟩ : ↥(degreeLT (R := R) n)) = p
```

`CompPoly.CPolynomial.degreeLTEquiv_right_inv` (lemma, [line 122](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L122))

```lean
lemma degreeLTEquiv_right_inv [DecidableEq R] (n : ℕ)
    (f : Fin n → R) :
    (fun i : Fin n => coeff
      (Finset.univ.sum (fun j : Fin n => monomial (R := R) (↑j) (f j))) i) = f
```

`CompPoly.CPolynomial.degreeLTEquiv` (definition, [line 135](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L135))

```lean
def degreeLTEquiv [DecidableEq R] (n : ℕ) :
    ↥(degreeLT (R := R) n) ≃ₗ[R] (Fin n → R)
```

`CompPoly.CPolynomial.degreeLTLinearEquiv` (abbreviation, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L155))

```lean
abbrev degreeLTLinearEquiv [DecidableEq R] (n : ℕ) :
    ↥(degreeLT (R := R) n) ≃ₗ[R] (Fin n → R)
```

`CompPoly.CPolynomial.degreeLTEquiv_toPoly` (theorem, [line 159](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L159))

```lean
theorem degreeLTEquiv_toPoly [DecidableEq R] {n : ℕ} {p : CPolynomial R}
    (hp : p ∈ degreeLT (R := R) n) (i : Fin n) :
      degreeLTEquiv (R := R) n ⟨p, hp⟩ i =
          Polynomial.degreeLTEquiv R n ⟨p.toPoly, degreeLT_toPoly.mp hp⟩ i
```

`CompPoly.CPolynomial.degreeLTEquiv_eq_zero_iff_eq_zero` (theorem, [line 165](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L165))

```lean
theorem degreeLTEquiv_eq_zero_iff_eq_zero [DecidableEq R] {n : ℕ} {p : CPolynomial R}
    (hp : p ∈ degreeLT (R := R) n) :
    degreeLTEquiv (R := R) n ⟨p, hp⟩ = 0 ↔ p = 0
```

`CompPoly.CPolynomial.eval_eq_sum_degreeLTEquiv` (theorem, [line 180](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L180))

```lean
theorem eval_eq_sum_degreeLTEquiv [DecidableEq R] {n : ℕ} {p : CPolynomial R}
    (hp : p ∈ degreeLT (R := R) n) (x : R) :
    eval x p =
      Finset.univ.sum (fun i : Fin n => degreeLTEquiv (R := R) n ⟨p, hp⟩ i * x ^ (i : ℕ))
```

`CompPoly.CPolynomial.degree_toPoly_ofFinCoeff_lt` (theorem, [line 198](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L198))

> The polynomial built from `N` coefficients has `toPoly` of degree below `N`.

```lean
theorem degree_toPoly_ofFinCoeff_lt (N : ℕ) (c : ℕ → R) :
    (ofFinCoeff N c).toPoly.degree < (N : WithBot ℕ)
```

> ### Degree arithmetic
>
> `CPolynomial` versions of Mathlib's degree, `natDegree` and `leadingCoeff` lemmas, each
> transferred through the `toPoly` coercion. The `@[simp]` attributes follow Mathlib's.

`CompPoly.CPolynomial.degree_C_le` (theorem, [line 216](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L216))

```lean
theorem degree_C_le (r : R) : (C r).degree ≤ 0
```

`CompPoly.CPolynomial.degree_C` (theorem, [line 219](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L219))

```lean
theorem degree_C {r : R} (hr : r ≠ 0) : (C r).degree = 0
```

`CompPoly.CPolynomial.leadingCoeff_C` (theorem, [line 223](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L223))

```lean
theorem leadingCoeff_C (r : R) : (C r).leadingCoeff = r
```

`CompPoly.CPolynomial.degree_X` (theorem, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L227))

```lean
theorem degree_X [Nontrivial R] : (X : CPolynomial R).degree = 1
```

`CompPoly.CPolynomial.natDegree_X` (theorem, [line 231](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L231))

```lean
theorem natDegree_X [Nontrivial R] : (X : CPolynomial R).natDegree = 1
```

`CompPoly.CPolynomial.leadingCoeff_X` (theorem, [line 235](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L235))

```lean
theorem leadingCoeff_X [Nontrivial R] : (X : CPolynomial R).leadingCoeff = 1
```

`CompPoly.CPolynomial.degree_one` (theorem, [line 239](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L239))

```lean
theorem degree_one [Nontrivial R] : (1 : CPolynomial R).degree = 0
```

`CompPoly.CPolynomial.natDegree_one` (theorem, [line 243](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L243))

```lean
theorem natDegree_one [Nontrivial R] : (1 : CPolynomial R).natDegree = 0
```

`CompPoly.CPolynomial.leadingCoeff_one` (theorem, [line 247](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L247))

```lean
theorem leadingCoeff_one [Nontrivial R] : (1 : CPolynomial R).leadingCoeff = 1
```

`CompPoly.CPolynomial.degree_add_le` (theorem, [line 250](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L250))

```lean
theorem degree_add_le (p q : CPolynomial R) : (p + q).degree ≤ max p.degree q.degree
```

`CompPoly.CPolynomial.degree_add_eq_left_of_degree_lt` (theorem, [line 253](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L253))

```lean
theorem degree_add_eq_left_of_degree_lt {p q : CPolynomial R} (h : q.degree < p.degree) :
    (p + q).degree = p.degree
```

`CompPoly.CPolynomial.degree_add_eq_right_of_degree_lt` (theorem, [line 258](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L258))

```lean
theorem degree_add_eq_right_of_degree_lt {p q : CPolynomial R} (h : p.degree < q.degree) :
    (p + q).degree = q.degree
```

`CompPoly.CPolynomial.degree_mul_le` (theorem, [line 263](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L263))

```lean
theorem degree_mul_le (p q : CPolynomial R) : (p * q).degree ≤ p.degree + q.degree
```

`CompPoly.CPolynomial.natDegree_mul_le` (theorem, [line 266](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L266))

```lean
theorem natDegree_mul_le (p q : CPolynomial R) :
    (p * q).natDegree ≤ p.natDegree + q.natDegree
```

`CompPoly.CPolynomial.degree_pow_le` (theorem, [line 270](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L270))

```lean
theorem degree_pow_le [Nontrivial R] (p : CPolynomial R) (n : ℕ) :
    (p ^ n).degree ≤ n • p.degree
```

`CompPoly.CPolynomial.natDegree_pow_le` (theorem, [line 274](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L274))

```lean
theorem natDegree_pow_le [Nontrivial R] (p : CPolynomial R) (n : ℕ) :
    (p ^ n).natDegree ≤ n * p.natDegree
```

`CompPoly.CPolynomial.natDegree_pow_le_of_le` (theorem, [line 278](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L278))

```lean
theorem natDegree_pow_le_of_le [Nontrivial R] {p : CPolynomial R} {m : ℕ} (n : ℕ)
    (h : p.natDegree ≤ m) : (p ^ n).natDegree ≤ n * m
```

`CompPoly.CPolynomial.degree_neg` (theorem, [line 289](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L289))

```lean
theorem degree_neg (p : CPolynomial S) : (-p).degree = p.degree
```

`CompPoly.CPolynomial.natDegree_neg` (theorem, [line 293](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L293))

```lean
theorem natDegree_neg (p : CPolynomial S) : (-p).natDegree = p.natDegree
```

`CompPoly.CPolynomial.leadingCoeff_neg` (theorem, [line 297](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L297))

```lean
theorem leadingCoeff_neg (p : CPolynomial S) : (-p).leadingCoeff = -p.leadingCoeff
```

`CompPoly.CPolynomial.degree_sub_le` (theorem, [line 300](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L300))

```lean
theorem degree_sub_le (p q : CPolynomial S) : (p - q).degree ≤ max p.degree q.degree
```

`CompPoly.CPolynomial.natDegree_sub_le` (theorem, [line 303](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L303))

```lean
theorem natDegree_sub_le (p q : CPolynomial S) :
    (p - q).natDegree ≤ max p.natDegree q.natDegree
```

`CompPoly.CPolynomial.degree_X_sub_C` (theorem, [line 308](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L308))

```lean
theorem degree_X_sub_C [Nontrivial S] (a : S) : (X - C a).degree = 1
```

`CompPoly.CPolynomial.natDegree_X_sub_C` (theorem, [line 312](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L312))

```lean
theorem natDegree_X_sub_C [Nontrivial S] (a : S) : (X - C a).natDegree = 1
```

`CompPoly.CPolynomial.degree_mul` (theorem, [line 322](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L322))

```lean
theorem degree_mul (p q : CPolynomial R) : (p * q).degree = p.degree + q.degree
```

`CompPoly.CPolynomial.natDegree_mul` (theorem, [line 325](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L325))

```lean
theorem natDegree_mul {p q : CPolynomial R} (hp : p ≠ 0) (hq : q ≠ 0) :
    (p * q).natDegree = p.natDegree + q.natDegree
```

`CompPoly.CPolynomial.leadingCoeff_mul` (theorem, [line 331](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L331))

```lean
theorem leadingCoeff_mul (p q : CPolynomial R) :
    (p * q).leadingCoeff = p.leadingCoeff * q.leadingCoeff
```

`CompPoly.CPolynomial.degree_pow` (theorem, [line 336](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L336))

```lean
theorem degree_pow [Nontrivial R] (p : CPolynomial R) (n : ℕ) :
    (p ^ n).degree = n • p.degree
```

`CompPoly.CPolynomial.natDegree_pow` (theorem, [line 341](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L341))

```lean
theorem natDegree_pow [Nontrivial R] (p : CPolynomial R) (n : ℕ) :
    (p ^ n).natDegree = n * p.natDegree
```

`CompPoly.CPolynomial.leadingCoeff_pow` (theorem, [line 346](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean#L346))

```lean
theorem leadingCoeff_pow [Nontrivial R] (p : CPolynomial R) (n : ℕ) :
    (p ^ n).leadingCoeff = p.leadingCoeff ^ n
```

## Depends on

- [`toPoly` Equivalence](equiv.md)
- [Proofs of Correctness for CPolynomial Operations, wrt Mathlib Specs](impl.md)

## Sources

- [CompPoly/Univariate/ToPoly/Degree.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Degree.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.ToPoly.Degree.json)
