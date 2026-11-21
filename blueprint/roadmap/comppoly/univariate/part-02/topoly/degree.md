---
catalog: module
lean: CompPoly.CPolynomial.toPoly_smul, CompPoly.CPolynomial.toPolyLinearEquiv, CompPoly.CPolynomial.toPolyLinearEquiv_apply, CompPoly.CPolynomial.degree_le_iff_coeff_zero, CompPoly.CPolynomial.degree_lt_iff_coeff_zero, CompPoly.CPolynomial.degreeLE_mono, CompPoly.CPolynomial.degreeLT_mono, CompPoly.CPolynomial.degreeLT_succ_eq_degreeLE, CompPoly.CPolynomial.monomial_mem_degreeLT, CompPoly.CPolynomial.degreeLTEquiv_invFun_mem, CompPoly.CPolynomial.degreeLTEquiv_left_inv, CompPoly.CPolynomial.degreeLTEquiv_right_inv, CompPoly.CPolynomial.degreeLTEquiv, CompPoly.CPolynomial.degreeLTLinearEquiv, CompPoly.CPolynomial.degreeLTEquiv_toPoly, CompPoly.CPolynomial.degreeLTEquiv_eq_zero_iff_eq_zero, CompPoly.CPolynomial.eval_eq_sum_degreeLTEquiv, CompPoly.CPolynomial.exists_degreeLT_toPoly_iff, CompPoly.CPolynomial.forall_degreeLT_toPoly_iff, CompPoly.CPolynomial.forall₂_degreeLT_toPoly_iff, CompPoly.CPolynomial.exists_degreeLT_toPoly_iff_of_degree_lt, CompPoly.CPolynomial.degree_toPoly_ofFinCoeff_lt, CompPoly.CPolynomial.degree_C_le, CompPoly.CPolynomial.degree_C, CompPoly.CPolynomial.leadingCoeff_C, CompPoly.CPolynomial.degree_X, CompPoly.CPolynomial.natDegree_X, CompPoly.CPolynomial.leadingCoeff_X, CompPoly.CPolynomial.degree_one, CompPoly.CPolynomial.natDegree_one, CompPoly.CPolynomial.leadingCoeff_one, CompPoly.CPolynomial.degree_add_le, CompPoly.CPolynomial.degree_add_eq_left_of_degree_lt, CompPoly.CPolynomial.degree_add_eq_right_of_degree_lt, CompPoly.CPolynomial.degree_mul_le, CompPoly.CPolynomial.natDegree_mul_le, CompPoly.CPolynomial.degree_pow_le, CompPoly.CPolynomial.natDegree_pow_le, CompPoly.CPolynomial.natDegree_pow_le_of_le, CompPoly.CPolynomial.degree_neg, CompPoly.CPolynomial.natDegree_neg, CompPoly.CPolynomial.leadingCoeff_neg, CompPoly.CPolynomial.degree_sub_le, CompPoly.CPolynomial.natDegree_sub_le, CompPoly.CPolynomial.degree_X_sub_C, CompPoly.CPolynomial.natDegree_X_sub_C, CompPoly.CPolynomial.degree_mul, CompPoly.CPolynomial.natDegree_mul, CompPoly.CPolynomial.leadingCoeff_mul, CompPoly.CPolynomial.degree_pow, CompPoly.CPolynomial.natDegree_pow, CompPoly.CPolynomial.leadingCoeff_pow
statement: formalized
proof: formalized
---

# Degrees and degree bounds under `toPoly`

`CompPoly.Univariate.ToPoly.Degree`, in [CompPoly/Univariate/ToPoly/Degree.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean), by Quang Dao, Gregor Mitscha-Baude, Derek Sorensen, Julian Sutherland, Alexander Hicks.

> Degree lemmas for the computable-univariate to `Polynomial` conversion.
>
> `degreeLTEquiv` identifies computable polynomials of degree below `n` with their coefficient
> functions `Fin n → R` by a linear equivalence.
>
> The quantifier lemmas transport statements over `↥(degreeLT n)` to Mathlib polynomials.
>
> * `exists_degreeLT_toPoly_iff` transports an existential quantifier with a degree bound.
> * `forall_degreeLT_toPoly_iff` transports a universal quantifier with a degree bound.
> * `forall₂_degreeLT_toPoly_iff` transports two universal quantifiers with separate bounds.
> * `exists_degreeLT_toPoly_iff_of_degree_lt` drops the explicit bound when the predicate implies it.

`CompPoly.CPolynomial.toPoly_smul` (lemma, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L44))

```lean
lemma toPoly_smul (r : R) (p : CPolynomial R) :
    (r • p).toPoly = r • p.toPoly
```

`CompPoly.CPolynomial.toPolyLinearEquiv` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L49))

```lean
noncomputable def toPolyLinearEquiv : CPolynomial R ≃ₗ[R] R[X]
```

`CompPoly.CPolynomial.toPolyLinearEquiv_apply` (theorem, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L59))

> The forward map of `toPolyLinearEquiv` is `toPoly`.

```lean
theorem toPolyLinearEquiv_apply (p : CPolynomial R) : toPolyLinearEquiv p = p.toPoly
```

`CompPoly.CPolynomial.degree_le_iff_coeff_zero` (theorem, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L62))

```lean
theorem degree_le_iff_coeff_zero (p : CPolynomial R) (n : WithBot ℕ) :
    p.degree ≤ n ↔ ∀ k : ℕ, n < k → p.coeff k = 0
```

`CompPoly.CPolynomial.degree_lt_iff_coeff_zero` (theorem, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L67))

```lean
theorem degree_lt_iff_coeff_zero (p : CPolynomial R) (n : ℕ) :
    p.degree < n ↔ ∀ k : ℕ, n ≤ k → p.coeff k = 0
```

`CompPoly.CPolynomial.degreeLE_mono` (theorem, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L73))

```lean
theorem degreeLE_mono (m n : WithBot ℕ) (h_lessThan : m ≤ n) :
    degreeLE (R := R) m ≤ degreeLE (R := R) n
```

`CompPoly.CPolynomial.degreeLT_mono` (theorem, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L78))

```lean
theorem degreeLT_mono {m n : ℕ} (h : m ≤ n) :
    degreeLT (R := R) m ≤ degreeLT (R := R) n
```

`CompPoly.CPolynomial.degreeLT_succ_eq_degreeLE` (theorem, [line 83](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L83))

```lean
theorem degreeLT_succ_eq_degreeLE {n : ℕ} :
    degreeLT (R := R) (n + 1) = degreeLE (R := R) ↑n
```

`CompPoly.CPolynomial.monomial_mem_degreeLT` (lemma, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L96))

```lean
lemma monomial_mem_degreeLT [DecidableEq R] {n : ℕ} (i : Fin n) (c : R) :
    monomial (R := R) (i : ℕ) c ∈ degreeLT (R := R) n
```

`CompPoly.CPolynomial.degreeLTEquiv_invFun_mem` (lemma, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L103))

```lean
lemma degreeLTEquiv_invFun_mem [DecidableEq R] (n : ℕ) (f : Fin n → R) :
    Finset.univ.sum (fun i : Fin n => monomial (R := R) (i : ℕ) (f i)) ∈ degreeLT (R := R) n
```

`CompPoly.CPolynomial.degreeLTEquiv_left_inv` (lemma, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L111))

```lean
lemma degreeLTEquiv_left_inv [DecidableEq R] (n : ℕ)
    (p : ↥(degreeLT (R := R) n)) :
    (⟨
      Finset.univ.sum (fun i : Fin n => monomial (R := R) (↑i) (coeff p.1 i)),
      degreeLTEquiv_invFun_mem (R := R) n (fun i => coeff p.1 i)
    ⟩ : ↥(degreeLT (R := R) n)) = p
```

`CompPoly.CPolynomial.degreeLTEquiv_right_inv` (lemma, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L132))

```lean
lemma degreeLTEquiv_right_inv [DecidableEq R] (n : ℕ)
    (f : Fin n → R) :
    (fun i : Fin n => coeff
      (Finset.univ.sum (fun j : Fin n => monomial (R := R) (↑j) (f j))) i) = f
```

`CompPoly.CPolynomial.degreeLTEquiv` (definition, [line 145](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L145))

```lean
def degreeLTEquiv [DecidableEq R] (n : ℕ) :
    ↥(degreeLT (R := R) n) ≃ₗ[R] (Fin n → R)
```

`CompPoly.CPolynomial.degreeLTLinearEquiv` (abbreviation, [line 165](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L165))

```lean
abbrev degreeLTLinearEquiv [DecidableEq R] (n : ℕ) :
    ↥(degreeLT (R := R) n) ≃ₗ[R] (Fin n → R)
```

`CompPoly.CPolynomial.degreeLTEquiv_toPoly` (theorem, [line 169](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L169))

```lean
theorem degreeLTEquiv_toPoly [DecidableEq R] {n : ℕ} {p : CPolynomial R}
    (hp : p ∈ degreeLT (R := R) n) (i : Fin n) :
      degreeLTEquiv (R := R) n ⟨p, hp⟩ i =
          Polynomial.degreeLTEquiv R n ⟨p.toPoly, degreeLT_toPoly.mp hp⟩ i
```

`CompPoly.CPolynomial.degreeLTEquiv_eq_zero_iff_eq_zero` (theorem, [line 175](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L175))

```lean
theorem degreeLTEquiv_eq_zero_iff_eq_zero [DecidableEq R] {n : ℕ} {p : CPolynomial R}
    (hp : p ∈ degreeLT (R := R) n) :
    degreeLTEquiv (R := R) n ⟨p, hp⟩ = 0 ↔ p = 0
```

`CompPoly.CPolynomial.eval_eq_sum_degreeLTEquiv` (theorem, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L190))

```lean
theorem eval_eq_sum_degreeLTEquiv [DecidableEq R] {n : ℕ} {p : CPolynomial R}
    (hp : p ∈ degreeLT (R := R) n) (x : R) :
    eval x p =
      Finset.univ.sum (fun i : Fin n => degreeLTEquiv (R := R) n ⟨p, hp⟩ i * x ^ (i : ℕ))
```

> ### Quantifiers over bounded-degree polynomials
>
> `toPoly` maps `degreeLT n` onto the Mathlib polynomials of degree below `n`. The lemmas in this
> section use this fact to restate a quantifier over `↥(degreeLT n)` as a quantifier over Mathlib
> polynomials. They serve only in proofs, because `toPoly` is noncomputable. A typical use decides
> an executable predicate `P` by a search over the enumeration `instFintypeDegreeLT`. Suppose that
> `P p` holds exactly when `Q p.toPoly` holds. The lemmas then relate the search to the corresponding
> quantifier over Mathlib polynomials of degree below `n`.

`CompPoly.CPolynomial.exists_degreeLT_toPoly_iff` (theorem, [line 212](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L212))

> Some polynomial of degree below `n` satisfies `Q` after `toPoly` exactly when some Mathlib
> polynomial of degree below `n` satisfies `Q`.

```lean
theorem exists_degreeLT_toPoly_iff (n : ℕ) (Q : R[X] → Prop) :
    (∃ p : ↥(degreeLT (R := R) n), Q p.val.toPoly) ↔ ∃ p : R[X], p.degree < n ∧ Q p
```

`CompPoly.CPolynomial.forall_degreeLT_toPoly_iff` (theorem, [line 224](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L224))

> Every polynomial of degree below `n` satisfies `Q` after `toPoly` exactly when every Mathlib
> polynomial of degree below `n` satisfies `Q`.

```lean
theorem forall_degreeLT_toPoly_iff (n : ℕ) (Q : R[X] → Prop) :
    (∀ p : ↥(degreeLT (R := R) n), Q p.val.toPoly) ↔ ∀ p : R[X], p.degree < n → Q p
```

`CompPoly.CPolynomial.forall₂_degreeLT_toPoly_iff` (theorem, [line 230](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L230))

> Transport two universal quantifiers through `toPoly`. The first polynomial has degree below
> `m`, and the second has degree below `n`.

```lean
theorem forall₂_degreeLT_toPoly_iff (m n : ℕ) (Q : R[X] → R[X] → Prop) :
    (∀ f : ↥(degreeLT (R := R) m), ∀ g : ↥(degreeLT (R := R) n),
      Q f.val.toPoly g.val.toPoly) ↔
      ∀ f g : R[X], f.degree < m → g.degree < n → Q f g
```

`CompPoly.CPolynomial.exists_degreeLT_toPoly_iff_of_degree_lt` (theorem, [line 241](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L241))

> Suppose that every Mathlib polynomial that satisfies `Q` has degree below `n`. Then some
> polynomial of degree below `n` satisfies `Q` after `toPoly` exactly when some Mathlib polynomial
> satisfies `Q`.

```lean
theorem exists_degreeLT_toPoly_iff_of_degree_lt (n : ℕ) (Q : R[X] → Prop)
    (hQ : ∀ p, Q p → p.degree < n) :
    (∃ p : ↥(degreeLT (R := R) n), Q p.val.toPoly) ↔ ∃ p : R[X], Q p
```

`CompPoly.CPolynomial.degree_toPoly_ofFinCoeff_lt` (theorem, [line 254](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L254))

> The polynomial built from `N` coefficients has `toPoly` of degree below `N`.

```lean
theorem degree_toPoly_ofFinCoeff_lt (N : ℕ) (c : ℕ → R) :
    (ofFinCoeff N c).toPoly.degree < (N : WithBot ℕ)
```

> ### Degree arithmetic
>
> `CPolynomial` versions of Mathlib's degree, `natDegree` and `leadingCoeff` lemmas, each
> transferred through the `toPoly` coercion. The `@[simp]` attributes follow Mathlib's.

`CompPoly.CPolynomial.degree_C_le` (theorem, [line 272](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L272))

```lean
theorem degree_C_le (r : R) : (C r).degree ≤ 0
```

`CompPoly.CPolynomial.degree_C` (theorem, [line 275](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L275))

```lean
theorem degree_C {r : R} (hr : r ≠ 0) : (C r).degree = 0
```

`CompPoly.CPolynomial.leadingCoeff_C` (theorem, [line 279](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L279))

```lean
theorem leadingCoeff_C (r : R) : (C r).leadingCoeff = r
```

`CompPoly.CPolynomial.degree_X` (theorem, [line 283](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L283))

```lean
theorem degree_X [Nontrivial R] : (X : CPolynomial R).degree = 1
```

`CompPoly.CPolynomial.natDegree_X` (theorem, [line 287](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L287))

```lean
theorem natDegree_X [Nontrivial R] : (X : CPolynomial R).natDegree = 1
```

`CompPoly.CPolynomial.leadingCoeff_X` (theorem, [line 291](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L291))

```lean
theorem leadingCoeff_X [Nontrivial R] : (X : CPolynomial R).leadingCoeff = 1
```

`CompPoly.CPolynomial.degree_one` (theorem, [line 295](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L295))

```lean
theorem degree_one [Nontrivial R] : (1 : CPolynomial R).degree = 0
```

`CompPoly.CPolynomial.natDegree_one` (theorem, [line 299](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L299))

```lean
theorem natDegree_one [Nontrivial R] : (1 : CPolynomial R).natDegree = 0
```

`CompPoly.CPolynomial.leadingCoeff_one` (theorem, [line 303](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L303))

```lean
theorem leadingCoeff_one [Nontrivial R] : (1 : CPolynomial R).leadingCoeff = 1
```

`CompPoly.CPolynomial.degree_add_le` (theorem, [line 306](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L306))

```lean
theorem degree_add_le (p q : CPolynomial R) : (p + q).degree ≤ max p.degree q.degree
```

`CompPoly.CPolynomial.degree_add_eq_left_of_degree_lt` (theorem, [line 309](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L309))

```lean
theorem degree_add_eq_left_of_degree_lt {p q : CPolynomial R} (h : q.degree < p.degree) :
    (p + q).degree = p.degree
```

`CompPoly.CPolynomial.degree_add_eq_right_of_degree_lt` (theorem, [line 314](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L314))

```lean
theorem degree_add_eq_right_of_degree_lt {p q : CPolynomial R} (h : p.degree < q.degree) :
    (p + q).degree = q.degree
```

`CompPoly.CPolynomial.degree_mul_le` (theorem, [line 319](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L319))

```lean
theorem degree_mul_le (p q : CPolynomial R) : (p * q).degree ≤ p.degree + q.degree
```

`CompPoly.CPolynomial.natDegree_mul_le` (theorem, [line 322](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L322))

```lean
theorem natDegree_mul_le (p q : CPolynomial R) :
    (p * q).natDegree ≤ p.natDegree + q.natDegree
```

`CompPoly.CPolynomial.degree_pow_le` (theorem, [line 326](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L326))

```lean
theorem degree_pow_le [Nontrivial R] (p : CPolynomial R) (n : ℕ) :
    (p ^ n).degree ≤ n • p.degree
```

`CompPoly.CPolynomial.natDegree_pow_le` (theorem, [line 330](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L330))

```lean
theorem natDegree_pow_le [Nontrivial R] (p : CPolynomial R) (n : ℕ) :
    (p ^ n).natDegree ≤ n * p.natDegree
```

`CompPoly.CPolynomial.natDegree_pow_le_of_le` (theorem, [line 334](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L334))

```lean
theorem natDegree_pow_le_of_le [Nontrivial R] {p : CPolynomial R} {m : ℕ} (n : ℕ)
    (h : p.natDegree ≤ m) : (p ^ n).natDegree ≤ n * m
```

`CompPoly.CPolynomial.degree_neg` (theorem, [line 345](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L345))

```lean
theorem degree_neg (p : CPolynomial S) : (-p).degree = p.degree
```

`CompPoly.CPolynomial.natDegree_neg` (theorem, [line 349](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L349))

```lean
theorem natDegree_neg (p : CPolynomial S) : (-p).natDegree = p.natDegree
```

`CompPoly.CPolynomial.leadingCoeff_neg` (theorem, [line 353](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L353))

```lean
theorem leadingCoeff_neg (p : CPolynomial S) : (-p).leadingCoeff = -p.leadingCoeff
```

`CompPoly.CPolynomial.degree_sub_le` (theorem, [line 356](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L356))

```lean
theorem degree_sub_le (p q : CPolynomial S) : (p - q).degree ≤ max p.degree q.degree
```

`CompPoly.CPolynomial.natDegree_sub_le` (theorem, [line 359](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L359))

```lean
theorem natDegree_sub_le (p q : CPolynomial S) :
    (p - q).natDegree ≤ max p.natDegree q.natDegree
```

`CompPoly.CPolynomial.degree_X_sub_C` (theorem, [line 364](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L364))

```lean
theorem degree_X_sub_C [Nontrivial S] (a : S) : (X - C a).degree = 1
```

`CompPoly.CPolynomial.natDegree_X_sub_C` (theorem, [line 368](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L368))

```lean
theorem natDegree_X_sub_C [Nontrivial S] (a : S) : (X - C a).natDegree = 1
```

`CompPoly.CPolynomial.degree_mul` (theorem, [line 378](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L378))

```lean
theorem degree_mul (p q : CPolynomial R) : (p * q).degree = p.degree + q.degree
```

`CompPoly.CPolynomial.natDegree_mul` (theorem, [line 381](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L381))

```lean
theorem natDegree_mul {p q : CPolynomial R} (hp : p ≠ 0) (hq : q ≠ 0) :
    (p * q).natDegree = p.natDegree + q.natDegree
```

`CompPoly.CPolynomial.leadingCoeff_mul` (theorem, [line 387](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L387))

```lean
theorem leadingCoeff_mul (p q : CPolynomial R) :
    (p * q).leadingCoeff = p.leadingCoeff * q.leadingCoeff
```

`CompPoly.CPolynomial.degree_pow` (theorem, [line 392](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L392))

```lean
theorem degree_pow [Nontrivial R] (p : CPolynomial R) (n : ℕ) :
    (p ^ n).degree = n • p.degree
```

`CompPoly.CPolynomial.natDegree_pow` (theorem, [line 397](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L397))

```lean
theorem natDegree_pow [Nontrivial R] (p : CPolynomial R) (n : ℕ) :
    (p ^ n).natDegree = n * p.natDegree
```

`CompPoly.CPolynomial.leadingCoeff_pow` (theorem, [line 402](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean#L402))

```lean
theorem leadingCoeff_pow [Nontrivial R] (p : CPolynomial R) (n : ℕ) :
    (p ^ n).leadingCoeff = p.leadingCoeff ^ n
```

## Depends on

- [`toPoly` Equivalence](equiv.md)
- [Proofs of Correctness for CPolynomial Operations, wrt Mathlib Specs](impl.md)

## Sources

- [CompPoly/Univariate/ToPoly/Degree.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Degree.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.ToPoly.Degree.json)
