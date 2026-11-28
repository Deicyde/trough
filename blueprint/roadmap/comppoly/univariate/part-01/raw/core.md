---
catalog: module
lean: CompPoly.CPolynomial.Raw, CompPoly.CPolynomial.Raw.mk, CompPoly.CPolynomial.Raw.coeffs, CompPoly.CPolynomial.Raw.coeff, CompPoly.CPolynomial.Raw.C, CompPoly.CPolynomial.Raw.X, CompPoly.CPolynomial.Raw.monomial, CompPoly.CPolynomial.Raw.lastNonzero, CompPoly.CPolynomial.Raw.trim, CompPoly.CPolynomial.Raw.degree, CompPoly.CPolynomial.Raw.natDegree, CompPoly.CPolynomial.Raw.leadingCoeff, CompPoly.CPolynomial.Raw.IsCanonical, CompPoly.CPolynomial.Raw.canonical, CompPoly.CPolynomial.Raw.Trim.lastNonzero_none, CompPoly.CPolynomial.Raw.Trim.lastNonzero_some, CompPoly.CPolynomial.Raw.Trim.lastNonzero_spec, CompPoly.CPolynomial.Raw.Trim.lastNonzeroProp, CompPoly.CPolynomial.Raw.Trim.lastNonzero_unique, CompPoly.CPolynomial.Raw.Trim.lastNonzero_some_iff, CompPoly.CPolynomial.Raw.Trim.lastNonzero_induct, CompPoly.CPolynomial.Raw.Trim.induct, CompPoly.CPolynomial.Raw.Trim.elim, CompPoly.CPolynomial.Raw.Trim.size_eq_degree_plus_one, CompPoly.CPolynomial.Raw.Trim.size_eq_natDegree_plus_one, CompPoly.CPolynomial.Raw.Trim.size_eq_natDegree_of_zero, CompPoly.CPolynomial.Raw.Trim.size_le_size, CompPoly.CPolynomial.Raw.Trim.coeff_eq_getElem_of_lt, CompPoly.CPolynomial.Raw.Trim.coeff_eq_coeff, CompPoly.CPolynomial.Raw.Trim.coeff_eq_getElem, CompPoly.CPolynomial.Raw.Trim.equiv, CompPoly.CPolynomial.Raw.Trim.coeff_eq_zero, CompPoly.CPolynomial.Raw.Trim.eq_degree_of_equiv, CompPoly.CPolynomial.Raw.Trim.eq_of_equiv, CompPoly.CPolynomial.Raw.Trim.trim_equiv, CompPoly.CPolynomial.Raw.Trim.trim_twice, CompPoly.CPolynomial.Raw.Trim.canonical_empty, CompPoly.CPolynomial.Raw.Trim.canonical_of_size_zero, CompPoly.CPolynomial.Raw.Trim.canonical_nonempty_iff, CompPoly.CPolynomial.Raw.Trim.lastNonzero_last_iff, CompPoly.CPolynomial.Raw.Trim.canonical_iff, CompPoly.CPolynomial.Raw.Trim.isCanonical_empty, CompPoly.CPolynomial.Raw.Trim.isCanonical_of_size_zero, CompPoly.CPolynomial.Raw.Trim.isCanonical_iff_trim_eq, CompPoly.CPolynomial.Raw.Trim.isCanonical_iff_size_eq_zero_or_getLastD_ne_zero, CompPoly.CPolynomial.Raw.Trim.trim_eq_iff_size_eq_zero_or_getLastD_ne_zero, CompPoly.CPolynomial.Raw.Trim.trim_eq_of_isCanonical, CompPoly.CPolynomial.Raw.Trim.isCanonical_of_trim_eq, CompPoly.CPolynomial.Raw.Trim.isCanonical_trim, CompPoly.CPolynomial.Raw.Trim.push_trim, CompPoly.CPolynomial.Raw.Trim.non_zero_map, CompPoly.CPolynomial.Raw.Trim.canonical_ext, CompPoly.CPolynomial.Raw.Trim.isCanonical_ext
statement: formalized
proof: formalized
---

# Raw Computable Univariate Polynomials

`CompPoly.Univariate.Raw.Core`, in [CompPoly/Univariate/Raw/Core.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean), by Quang Dao, Gregor Mitscha-Baude, Derek Sorensen, Desmond Coles.

> Core definitions for array-backed computable univariate polynomials.

`CompPoly.CPolynomial.Raw` (definition, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L32))

> A type analogous to `Polynomial` that supports computable operations. This is defined to be a
> wrapper around `Array`.
>
> For example, the Array `#[1,2,3]` represents the polynomial `1 + 2x + 3x^2`.
> Two arrays may represent the same polynomial via zero-padding,
> for example `#[1,2,3] = #[1,2,3,0,0,0,...]`.

```lean
def CPolynomial.Raw (R : Type*)
```

`CompPoly.CPolynomial.Raw.mk` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L38))

> Construct a `CPolynomial.Raw` from an array of coefficients.

```lean
def mk {R : Type*} (coeffs : Array R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.coeffs` (definition, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L42))

> Extract the underlying array of coefficients.

```lean
def coeffs {R : Type*} (p : CPolynomial.Raw R) : Array R
```

`CompPoly.CPolynomial.Raw.coeff` (definition, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L51))

> The coefficient of `X^i` in the polynomial. Returns `0` if `i` is out of bounds.

```lean
def coeff [Zero R] (p : CPolynomial.Raw R) (i : ℕ) : R
```

`CompPoly.CPolynomial.Raw.C` (definition, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L54))

> The constant polynomial `C r`.

```lean
def C (r : R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.X` (definition, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L57))

> The variable `X`.

```lean
def X [Zero R] [One R] : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.monomial` (definition, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L66))

> Construct a monomial `c * X^n` as a `CPolynomial.Raw R`.
>
> The result is an array with `n` zeros followed by `c`.
> For example, `monomial 2 3` = `#[0, 0, 3]` represents `3 * X^2`.
>
> Note: If `c = 0`, this returns `#[]` (the zero polynomial).

```lean
def monomial [Zero R] [DecidableEq R] (n : ℕ) (c : R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.lastNonzero` (definition, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L70))

> Return the index of the last non-zero coefficient of a `CPolynomial.Raw`

```lean
def lastNonzero [Zero R] [BEq R] (p : CPolynomial.Raw R) : Option (Fin p.size)
```

`CompPoly.CPolynomial.Raw.trim` (definition, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L75))

> Remove trailing zeroes from a `CPolynomial.Raw`.
> Requires `BEq` to check if the coefficients are zero.

```lean
def trim [Zero R] [BEq R] (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.degree` (definition, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L81))

> Return the degree of a `CPolynomial.Raw`.

```lean
def degree [Zero R] [BEq R] (p : CPolynomial.Raw R) : WithBot ℕ
```

`CompPoly.CPolynomial.Raw.natDegree` (definition, [line 91](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L91))

> Natural number degree of a `CPolynomial.Raw`.
>
> Returns the degree as a natural number. For the zero polynomial, returns `0`.
> This matches Mathlib's `Polynomial.natDegree` API.

```lean
def natDegree [Zero R] [BEq R] (p : CPolynomial.Raw R) : ℕ
```

`CompPoly.CPolynomial.Raw.leadingCoeff` (definition, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L98))

> Return the leading coefficient of a `CPolynomial.Raw` as the last coefficient
> of the trimmed array, or `0` if the trimmed array is empty.

```lean
def leadingCoeff [Zero R] [BEq R] (p : CPolynomial.Raw R) : R
```

`CompPoly.CPolynomial.Raw.IsCanonical` (definition, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L103))

> Semantic canonicality for raw coefficient arrays: a polynomial is canonical iff its
> last stored coefficient, when present, is nonzero. This invariant is independent of any
> particular `BEq` instance.

```lean
def IsCanonical [Zero R] (p : CPolynomial.Raw R) : Prop
```

`CompPoly.CPolynomial.Raw.canonical` (definition, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L107))

> A polynomial is canonical if it has no trailing zeros, i.e. `p.trim = p`.

```lean
def canonical [Zero R] [BEq R] (p : CPolynomial.Raw R) : Prop
```

`CompPoly.CPolynomial.Raw.Trim.lastNonzero_none` (theorem, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L114))

> If all coefficients are zero, `lastNonzero` is `none`.

```lean
theorem lastNonzero_none [Zero R] [BEq R] [LawfulBEq R] {p : CPolynomial.Raw R} :
    (∀ i, (hi : i < p.size) → p[i] = 0) → p.lastNonzero = none
```

`CompPoly.CPolynomial.Raw.Trim.lastNonzero_some` (theorem, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L123))

> If there is a non-zero coefficient, `lastNonzero` is `some`.

```lean
theorem lastNonzero_some [Zero R] [BEq R] [LawfulBEq R]
    {p : CPolynomial.Raw R} {i} (hi : i < p.size)
    (h : p[i] ≠ 0) : ∃ k, p.lastNonzero = some k
```

`CompPoly.CPolynomial.Raw.Trim.lastNonzero_spec` (theorem, [line 129](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L129))

> `lastNonzero` returns the largest index with a non-zero coefficient.

```lean
theorem lastNonzero_spec [Zero R] [BEq R] [LawfulBEq R] {p : CPolynomial.Raw R} {k} :
    p.lastNonzero = some k
  → p[k] ≠ 0 ∧ (∀ j, (hj : j < p.size) → j > k → p[j] = 0)
```

`CompPoly.CPolynomial.Raw.Trim.lastNonzeroProp` (definition, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L142))

> The property that an index is the last non-zero coefficient.

```lean
def lastNonzeroProp [Zero R] {p : CPolynomial.Raw R} (k : Fin p.size) : Prop
```

`CompPoly.CPolynomial.Raw.Trim.lastNonzero_unique` (lemma, [line 146](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L146))

> The last non-zero index is unique.

```lean
lemma lastNonzero_unique [Zero Q] {p : CPolynomial.Raw Q} {k k' : Fin p.size} :
    lastNonzeroProp k → lastNonzeroProp k' → k = k'
```

`CompPoly.CPolynomial.Raw.Trim.lastNonzero_some_iff` (theorem, [line 157](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L157))

> Characterization of `lastNonzero` via `lastNonzeroProp`.

```lean
theorem lastNonzero_some_iff [Zero R] [BEq R] [LawfulBEq R] {p : CPolynomial.Raw R} {k} :
    p.lastNonzero = some k ↔ (p[k] ≠ 0 ∧ (∀ j, (hj : j < p.size) → j > k → p[j] = 0))
```

`CompPoly.CPolynomial.Raw.Trim.lastNonzero_induct` (theorem, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L173))

> eliminator for `p.lastNonzero`, e.g. use with the induction tactic as follows:
> ```
> induction p using lastNonzero_induct with
> | case1 p h_none h_all_zero => ...
> | case2 p k h_some h_nonzero h_max => ...
> ```

```lean
theorem lastNonzero_induct [Zero R] [BEq R] [LawfulBEq R] {motive : CPolynomial.Raw R → Prop}
    (case1 : ∀ p, p.lastNonzero = none → (∀ i, (hi : i < p.size) → p[i] = 0) → motive p)
  (case2 : ∀ p : CPolynomial.Raw R, ∀ k : Fin p.size, p.lastNonzero = some k → p[k] ≠ 0 →
    (∀ j : ℕ, (hj : j < p.size) → j > k → p[j] = 0) → motive p)
  (p : CPolynomial.Raw R) : motive p
```

`CompPoly.CPolynomial.Raw.Trim.induct` (theorem, [line 192](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L192))

> eliminator for `p.trim`; use with the induction tactic as follows:
> ```
> induction p using induct with
> | case1 p h_empty h_all_zero => ...
> | case2 p k h_extract h_nonzero h_max => ...
> ```

```lean
theorem induct [Zero R] [BEq R] [LawfulBEq R] {motive : CPolynomial.Raw R → Prop}
    (case1 : ∀ p, p.trim = #[] → (∀ i, (hi : i < p.size) → p[i] = 0) → motive p)
  (case2 : ∀ p : CPolynomial.Raw R, ∀ k : Fin p.size, p.trim = p.extract 0 (k + 1)
    → p[k] ≠ 0 → (∀ j : ℕ, (hj : j < p.size) → j > k → p[j] = 0) → motive p)
  (p : CPolynomial.Raw R) : motive p
```

`CompPoly.CPolynomial.Raw.Trim.elim` (theorem, [line 209](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L209))

> eliminator for `p.trim`; e.g. use for case distinction as follows:
> ```
> rcases (Trim.elim p) with ⟨ h_empty, h_all_zero ⟩ | ⟨ k, h_extract, h_nonzero, h_max ⟩
> ```

```lean
theorem elim [Zero R] [BEq R] [LawfulBEq R] (p : CPolynomial.Raw R) :
    (p.trim = #[] ∧  (∀ i, (hi : i < p.size) → p[i] = 0))
    ∨ (∃ k : Fin p.size,
        p.trim = p.extract 0 (k + 1)
      ∧ p[k] ≠ 0
      ∧ (∀ j : ℕ, (hj : j < p.size) → j > k → p[j] = 0))
```

`CompPoly.CPolynomial.Raw.Trim.size_eq_degree_plus_one` (theorem, [line 218](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L218))

```lean
theorem size_eq_degree_plus_one [Zero R] [BEq R]
    (p : CPolynomial.Raw R) (h_trim : p.trim ≠ (mk #[])) :
    p.trim.size = p.degree + 1
```

`CompPoly.CPolynomial.Raw.Trim.size_eq_natDegree_plus_one` (theorem, [line 226](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L226))

```lean
theorem size_eq_natDegree_plus_one [Zero R] [BEq R]
    (p : CPolynomial.Raw R) (h_trim : p.trim ≠ (mk #[])) :
    p.trim.size = p.natDegree + 1
```

`CompPoly.CPolynomial.Raw.Trim.size_eq_natDegree_of_zero` (theorem, [line 234](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L234))

```lean
theorem size_eq_natDegree_of_zero [Zero R] [BEq R]
    (p : CPolynomial.Raw R) (h_trim : p.trim = (mk #[])) :
    p.trim.size = p.natDegree
```

`CompPoly.CPolynomial.Raw.Trim.size_le_size` (theorem, [line 245](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L245))

```lean
theorem size_le_size [Zero R] [BEq R] (p : CPolynomial.Raw R) : p.trim.size ≤ p.size
```

`CompPoly.CPolynomial.Raw.Trim.coeff_eq_getElem_of_lt` (theorem, [line 253](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L253))

```lean
theorem coeff_eq_getElem_of_lt [Zero R] [BEq R] [LawfulBEq R]
    {p : CPolynomial.Raw R} {i} (hi : i < p.size) :
    p.trim.coeff i = p[i]
```

`CompPoly.CPolynomial.Raw.Trim.coeff_eq_coeff` (theorem, [line 272](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L272))

```lean
theorem coeff_eq_coeff [Zero R] [BEq R] [LawfulBEq R]
    (p : CPolynomial.Raw R) (i : ℕ) :
    p.trim.coeff i = p.coeff i
```

`CompPoly.CPolynomial.Raw.Trim.coeff_eq_getElem` (lemma, [line 281](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L281))

```lean
lemma coeff_eq_getElem [Zero Q] {p : CPolynomial.Raw Q} {i} (hp : i < p.size) :
    p.coeff i = p[i]
```

`CompPoly.CPolynomial.Raw.Trim.equiv` (definition, [line 286](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L286))

> Equivalence relation: two polynomials are equivalent if all coefficients agree.

```lean
def equiv [Zero R] (p q : CPolynomial.Raw R) : Prop
```

`CompPoly.CPolynomial.Raw.Trim.coeff_eq_zero` (lemma, [line 289](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L289))

```lean
lemma coeff_eq_zero [Zero Q] {p : CPolynomial.Raw Q} :
    (∀ i, (hi : i < p.size) → p[i] = 0) ↔ ∀ i, p.coeff i = 0
```

`CompPoly.CPolynomial.Raw.Trim.eq_degree_of_equiv` (lemma, [line 295](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L295))

```lean
lemma eq_degree_of_equiv [Zero R] [BEq R] [LawfulBEq R] {p q : CPolynomial.Raw R} :
    equiv p q → p.degree = q.degree
```

`CompPoly.CPolynomial.Raw.Trim.eq_of_equiv` (theorem, [line 326](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L326))

```lean
theorem eq_of_equiv [Zero R] [BEq R] [LawfulBEq R] {p q : CPolynomial.Raw R} :
    equiv p q → p.trim = q.trim
```

`CompPoly.CPolynomial.Raw.Trim.trim_equiv` (theorem, [line 349](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L349))

```lean
theorem trim_equiv [Zero R] [BEq R] [LawfulBEq R] (p : CPolynomial.Raw R) :
    equiv p.trim p
```

`CompPoly.CPolynomial.Raw.Trim.trim_twice` (theorem, [line 353](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L353))

```lean
theorem trim_twice [Zero R] [BEq R] [LawfulBEq R] (p : CPolynomial.Raw R) :
    p.trim.trim = p.trim
```

`CompPoly.CPolynomial.Raw.Trim.canonical_empty` (theorem, [line 358](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L358))

```lean
theorem canonical_empty [Zero R] [BEq R] : (mk (R := R) #[]).trim = #[]
```

`CompPoly.CPolynomial.Raw.Trim.canonical_of_size_zero` (theorem, [line 365](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L365))

```lean
theorem canonical_of_size_zero [Zero R] [BEq R] {p : CPolynomial.Raw R} :
    p.size = 0 → p.trim = p
```

`CompPoly.CPolynomial.Raw.Trim.canonical_nonempty_iff` (theorem, [line 371](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L371))

```lean
theorem canonical_nonempty_iff [Zero R] [BEq R] [LawfulBEq R]
    {p : CPolynomial.Raw R} (hp : p.size > 0) :
    p.trim = p ↔ p.lastNonzero = some ⟨ p.size - 1, Nat.pred_lt_self hp ⟩
```

`CompPoly.CPolynomial.Raw.Trim.lastNonzero_last_iff` (theorem, [line 397](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L397))

```lean
theorem lastNonzero_last_iff [Zero R] [BEq R] [LawfulBEq R]
    {p : CPolynomial.Raw R} (hp : p.size > 0) :
    p.lastNonzero = some ⟨ p.size - 1, Nat.pred_lt_self hp ⟩ ↔ p.getLast hp ≠ 0
```

`CompPoly.CPolynomial.Raw.Trim.canonical_iff` (theorem, [line 418](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L418))

```lean
theorem canonical_iff [Zero R] [BEq R] [LawfulBEq R] {p : CPolynomial.Raw R} :
    p.trim = p ↔ IsCanonical p
```

`CompPoly.CPolynomial.Raw.Trim.isCanonical_empty` (theorem, [line 429](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L429))

```lean
theorem isCanonical_empty [Zero R] : IsCanonical (mk (R := R) #[])
```

`CompPoly.CPolynomial.Raw.Trim.isCanonical_of_size_zero` (theorem, [line 433](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L433))

```lean
theorem isCanonical_of_size_zero [Zero R] {p : CPolynomial.Raw R} (hp : p.size = 0) :
    IsCanonical p
```

`CompPoly.CPolynomial.Raw.Trim.isCanonical_iff_trim_eq` (theorem, [line 439](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L439))

> Canonicality bridge (semantic view to computational view).

```lean
theorem isCanonical_iff_trim_eq [Zero R] [BEq R] [LawfulBEq R]
    {p : CPolynomial.Raw R} :
    IsCanonical p ↔ p.trim = p
```

`CompPoly.CPolynomial.Raw.Trim.isCanonical_iff_size_eq_zero_or_getLastD_ne_zero` (theorem, [line 445](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L445))

> Non-dependent canonicality criterion using `getLastD`.

```lean
theorem isCanonical_iff_size_eq_zero_or_getLastD_ne_zero [Zero R]
    {p : CPolynomial.Raw R} :
    IsCanonical p ↔ p.size = 0 ∨ p.getLastD 0 ≠ 0
```

`CompPoly.CPolynomial.Raw.Trim.trim_eq_iff_size_eq_zero_or_getLastD_ne_zero` (theorem, [line 459](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L459))

> Computational canonicality criterion in non-dependent form.

```lean
theorem trim_eq_iff_size_eq_zero_or_getLastD_ne_zero [Zero R] [BEq R] [LawfulBEq R]
    {p : CPolynomial.Raw R} :
    p.trim = p ↔ p.size = 0 ∨ p.getLastD 0 ≠ 0
```

`CompPoly.CPolynomial.Raw.Trim.trim_eq_of_isCanonical` (theorem, [line 464](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L464))

```lean
theorem trim_eq_of_isCanonical [Zero R] [BEq R] [LawfulBEq R]
    {p : CPolynomial.Raw R} (hp : IsCanonical p) :
    p.trim = p
```

`CompPoly.CPolynomial.Raw.Trim.isCanonical_of_trim_eq` (theorem, [line 469](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L469))

```lean
theorem isCanonical_of_trim_eq [Zero R] [BEq R] [LawfulBEq R]
    {p : CPolynomial.Raw R} (hp : p.trim = p) :
    IsCanonical p
```

`CompPoly.CPolynomial.Raw.Trim.isCanonical_trim` (theorem, [line 474](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L474))

```lean
theorem isCanonical_trim [Zero R] [BEq R] [LawfulBEq R]
    (p : CPolynomial.Raw R) : IsCanonical p.trim
```

`CompPoly.CPolynomial.Raw.Trim.push_trim` (lemma, [line 479](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L479))

```lean
lemma push_trim [Zero R] [BEq R] [LawfulBEq R] (arr : Array R) (c : R) :
    ¬c = 0 → trim (arr.push c) = arr.push c
```

`CompPoly.CPolynomial.Raw.Trim.non_zero_map` (theorem, [line 486](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L486))

```lean
theorem non_zero_map [Zero R] [BEq R] [LawfulBEq R]
    (f : R → R) (hf : ∀ r, f r = 0 → r = 0) (p : CPolynomial.Raw R) :
    let fp := mk (p.map f);
  p.trim = p → fp.trim = fp
```

`CompPoly.CPolynomial.Raw.Trim.canonical_ext` (theorem, [line 507](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L507))

> Canonical polynomials enjoy a stronger extensionality theorem:
> they just need to agree at all coefficients (without assuming equal sizes)

```lean
theorem canonical_ext [Zero R] [BEq R] [LawfulBEq R]
    {p q : CPolynomial.Raw R} (hp : p.trim = p) (hq : q.trim = q) :
    equiv p q → p = q
```

`CompPoly.CPolynomial.Raw.Trim.isCanonical_ext` (theorem, [line 514](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean#L514))

```lean
theorem isCanonical_ext [Zero R] [BEq R] [LawfulBEq R] {p q : CPolynomial.Raw R}
    (hp : IsCanonical p) (hq : IsCanonical q) :
    equiv p q → p = q
```

## Depends on

- [Auxiliary lemmas for `Array`](../../../data/array/lemmas.md)

## Sources

- [CompPoly/Univariate/Raw/Core.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Raw/Core.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.Raw.Core.json)
