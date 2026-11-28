---
catalog: module
lean: CPoly.coeff_restrictBy, CPoly.coeff_restrictTotalDegreeOf, CPoly.coeff_restrictDegreeOf, CPoly.coeff_restrictTotalDegreeOf_eq_self_of_le, CPoly.coeff_restrictTotalDegreeOf_eq_zero_of_lt, CPoly.coeff_restrictDegreeOf_eq_self_of_le, CPoly.coeff_restrictDegreeOf_eq_zero_of_not_le, CPoly.totalDegree_le_of_mem_monomials_restrictTotalDegreeOf, CPoly.degreeOf_le_of_mem_monomials_restrictDegreeOf, CPoly.totalDegree_restrictTotalDegreeOf_le, CPoly.degreeOf_restrictDegreeOf_le, CPoly.restrictTotalDegreeOf_zero, CPoly.restrictDegreeOf_zero, CPoly.restrictTotalDegreeOf_restrictTotalDegreeOf, CPoly.restrictDegreeOf_restrictDegreeOf, CPoly.restrictTotalDegreeOf_restrictDegreeOf_comm, CPoly.fromCMvPolynomial_restrictTotalDegreeOf_mem, CPoly.fromCMvPolynomial_restrictDegreeOf_mem, CPoly.restrictDegree, CPoly.restrictDegree_elem
statement: formalized
proof: formalized
---

# Lemmas for `CMvPolynomial.restrictBy`, `restrictTotalDegreeOf`, and `restrictDegreeOf`

`CompPoly.Multivariate.Restrict`, in [CompPoly/Multivariate/Restrict.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean), by Fawad Haider, Pablo Martin.

> Degree-bounded restriction of multivariate polynomials: filtering monomials by total degree
> or per-variable degree bounds.
>
> Also proves correctness against Mathlib: transporting these restrictions across
> `fromCMvPolynomial` lands in Mathlib's degree-bounded submodules.

`CPoly.coeff_restrictBy` (lemma, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L31))

> Coefficient of `restrictBy keep p` at `m`: `p.coeff m` if `keep m`, else `0`.

```lean
lemma coeff_restrictBy (keep : CMvMonomial n → Prop) [DecidablePred keep]
    (m : CMvMonomial n) (p : CMvPolynomial n R) :
    (CMvPolynomial.restrictBy keep p).coeff m = if keep m then p.coeff m else 0
```

`CPoly.coeff_restrictTotalDegreeOf` (lemma, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L59))

> Coeff at `m`: `p.coeff m` if `m.totalDegree ≤ d`, else `0`.

```lean
lemma coeff_restrictTotalDegreeOf (d : ℕ) (m : CMvMonomial n) (p : CMvPolynomial n R) :
    (restrictTotalDegreeOf d p).coeff m =
      if m.totalDegree ≤ d then p.coeff m else 0
```

`CPoly.coeff_restrictDegreeOf` (lemma, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L68))

> Coefficient of `restrictDegreeOf d p` at `m`: `p.coeff m` if `∀ i, m.degreeOf i ≤ d`,
> else `0`.

```lean
lemma coeff_restrictDegreeOf (d : ℕ) (m : CMvMonomial n) (p : CMvPolynomial n R) :
    (restrictDegreeOf d p).coeff m =
      if ∀ i : Fin n, m.degreeOf i ≤ d then p.coeff m else 0
```

`CPoly.coeff_restrictTotalDegreeOf_eq_self_of_le` (lemma, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L75))

> When `m.totalDegree ≤ d`, coeff at `m` is unchanged by `restrictTotalDegreeOf d`.

```lean
lemma coeff_restrictTotalDegreeOf_eq_self_of_le {d : ℕ} {m : CMvMonomial n}
    {p : CMvPolynomial n R} (h : m.totalDegree ≤ d) :
    (restrictTotalDegreeOf d p).coeff m = p.coeff m
```

`CPoly.coeff_restrictTotalDegreeOf_eq_zero_of_lt` (lemma, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L81))

> When `d < m.totalDegree`, coeff at `m` is `0` in `restrictTotalDegreeOf d p`.

```lean
lemma coeff_restrictTotalDegreeOf_eq_zero_of_lt {d : ℕ} {m : CMvMonomial n}
    {p : CMvPolynomial n R} (h : d < m.totalDegree) :
    (restrictTotalDegreeOf d p).coeff m = 0
```

`CPoly.coeff_restrictDegreeOf_eq_self_of_le` (lemma, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L87))

> When `∀ i, m.degreeOf i ≤ d`, coeff at `m` is unchanged by `restrictDegreeOf d`.

```lean
lemma coeff_restrictDegreeOf_eq_self_of_le {d : ℕ} {m : CMvMonomial n}
    {p : CMvPolynomial n R} (h : ∀ i : Fin n, m.degreeOf i ≤ d) :
    (restrictDegreeOf d p).coeff m = p.coeff m
```

`CPoly.coeff_restrictDegreeOf_eq_zero_of_not_le` (lemma, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L93))

> When `¬(∀ i, m.degreeOf i ≤ d)`, coeff at `m` is `0` in `restrictDegreeOf d p`.

```lean
lemma coeff_restrictDegreeOf_eq_zero_of_not_le {d : ℕ} {m : CMvMonomial n}
    {p : CMvPolynomial n R} (h : ¬ (∀ i : Fin n, m.degreeOf i ≤ d)) :
    (restrictDegreeOf d p).coeff m = 0
```

`CPoly.totalDegree_le_of_mem_monomials_restrictTotalDegreeOf` (lemma, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L99))

> Monomials in `restrictTotalDegreeOf d p` have `totalDegree ≤ d`.

```lean
lemma totalDegree_le_of_mem_monomials_restrictTotalDegreeOf {d : ℕ} {m : CMvMonomial n}
    {p : CMvPolynomial n R}
    (hm : m ∈ Lawful.monomials (restrictTotalDegreeOf d p)) :
    m.totalDegree ≤ d
```

`CPoly.degreeOf_le_of_mem_monomials_restrictDegreeOf` (lemma, [line 115](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L115))

> Monomials in `restrictDegreeOf d p` have `degreeOf i ≤ d` for each variable `i`.

```lean
lemma degreeOf_le_of_mem_monomials_restrictDegreeOf {d : ℕ} {m : CMvMonomial n}
    {p : CMvPolynomial n R}
    (hm : m ∈ Lawful.monomials (restrictDegreeOf d p)) :
    ∀ i : Fin n, m.degreeOf i ≤ d
```

`CPoly.totalDegree_restrictTotalDegreeOf_le` (lemma, [line 180](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L180))

> `restrictTotalDegreeOf d p` has `totalDegree ≤ d`.

```lean
lemma totalDegree_restrictTotalDegreeOf_le
    {R' : Type*} [CommSemiring R'] [BEq R'] [LawfulBEq R']
    (d : ℕ) (p : CMvPolynomial n R') :
    (restrictTotalDegreeOf d p).totalDegree ≤ d
```

`CPoly.degreeOf_restrictDegreeOf_le` (lemma, [line 197](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L197))

> `restrictDegreeOf d p` has `degreeOf i ≤ d` for each variable `i`.

```lean
lemma degreeOf_restrictDegreeOf_le (d : ℕ) (p : CMvPolynomial n R) (i : Fin n) :
    (restrictDegreeOf d p).degreeOf i ≤ d
```

`CPoly.restrictTotalDegreeOf_zero` (lemma, [line 207](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L207))

> `restrictTotalDegreeOf d 0 = 0`.

```lean
lemma restrictTotalDegreeOf_zero (d : ℕ) :
    restrictTotalDegreeOf d (0 : CMvPolynomial n R) = 0
```

`CPoly.restrictDegreeOf_zero` (lemma, [line 215](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L215))

> `restrictDegreeOf d 0 = 0`.

```lean
lemma restrictDegreeOf_zero (d : ℕ) :
    restrictDegreeOf d (0 : CMvPolynomial n R) = 0
```

`CPoly.restrictTotalDegreeOf_restrictTotalDegreeOf` (lemma, [line 223](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L223))

> Double `restrictTotalDegreeOf` equals `restrictTotalDegreeOf (min d d')`.

```lean
lemma restrictTotalDegreeOf_restrictTotalDegreeOf (d d' : ℕ) (p : CMvPolynomial n R) :
    restrictTotalDegreeOf d (restrictTotalDegreeOf d' p) =
      restrictTotalDegreeOf (min d d') p
```

`CPoly.restrictDegreeOf_restrictDegreeOf` (lemma, [line 232](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L232))

> Double `restrictDegreeOf` equals `restrictDegreeOf (min d d')`.

```lean
lemma restrictDegreeOf_restrictDegreeOf (d d' : ℕ) (p : CMvPolynomial n R) :
    restrictDegreeOf d (restrictDegreeOf d' p) =
      restrictDegreeOf (min d d') p
```

`CPoly.restrictTotalDegreeOf_restrictDegreeOf_comm` (lemma, [line 256](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L256))

> `restrictTotalDegreeOf d` and `restrictDegreeOf d'` commute.

```lean
lemma restrictTotalDegreeOf_restrictDegreeOf_comm (d d' : ℕ) (p : CMvPolynomial n R) :
    restrictTotalDegreeOf d (CMvPolynomial.restrictDegreeOf d' p) =
      restrictDegreeOf d' (restrictTotalDegreeOf d p)
```

> ### Correspondence with Mathlib's degree-bounded submodules

`CPoly.fromCMvPolynomial_restrictTotalDegreeOf_mem` (theorem, [line 267](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L267))

> `fromCMvPolynomial (restrictTotalDegreeOf d p) ∈
> MvPolynomial.restrictTotalDegree (Fin n) R d`.

```lean
theorem fromCMvPolynomial_restrictTotalDegreeOf_mem {R : Type*} [CommSemiring R] [BEq R]
    [LawfulBEq R] (d : ℕ) (p : CMvPolynomial n R) :
    fromCMvPolynomial (restrictTotalDegreeOf d p) ∈
      MvPolynomial.restrictTotalDegree (Fin n) R d
```

`CPoly.fromCMvPolynomial_restrictDegreeOf_mem` (theorem, [line 275](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L275))

> `fromCMvPolynomial (restrictDegreeOf d p) ∈ MvPolynomial.restrictDegree (Fin n) R d`.

```lean
theorem fromCMvPolynomial_restrictDegreeOf_mem {R : Type*} [CommSemiring R] [BEq R]
    [LawfulBEq R] (d : ℕ) (p : CMvPolynomial n R) :
    fromCMvPolynomial (restrictDegreeOf d p) ∈
      MvPolynomial.restrictDegree (Fin n) R d
```

`CPoly.restrictDegree` (definition, [line 287](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L287))

> The `Submodule` of polynomials all of whose support monomials have every variable's
> exponent at most `degree`.

```lean
def restrictDegree (R : Type v) [CommSemiring R] [BEq R] [LawfulBEq R] (n degree : ℕ) :
    Submodule R (CMvPolynomial n R)
```

`CPoly.restrictDegree_elem` (lemma, [line 320](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean#L320))

> `p ∈ restrictDegree R n degree` iff every variable's exponent in every support
> monomial of `p` is at most `degree`.

```lean
lemma restrictDegree_elem {R : Type v} [CommSemiring R] [BEq R] [LawfulBEq R] {n degree : ℕ} :
    ∀ p, p ∈ restrictDegree R n degree ↔ ∀ σ ∈ p.support, ∀ i, σ i ≤ degree
```

## Depends on

- [`CMvPolynomial`/`MvPolynomial` Instances](mvpolyequiv/instances.md)

## Proof depends on

- [`CMvPolynomial`/`MvPolynomial` Evaluation](mvpolyequiv/eval.md)

## Sources

- [CompPoly/Multivariate/Restrict.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Restrict.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multivariate.Restrict.json)
