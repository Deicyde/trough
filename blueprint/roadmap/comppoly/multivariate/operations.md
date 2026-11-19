---
catalog: module
lean: CPoly.CMvPolynomial.MonomialOrder, CPoly.CMvPolynomial.MonomialOrder.degree, CPoly.CMvPolynomial.leadingMonomial, CPoly.CMvPolynomial.leadingTerm, CPoly.CMvPolynomial.leadingCoeff, CPoly.CMvPolynomial.leadingCoeff_eq_zero_of_leadingMonomial_eq_none, CPoly.CMvPolynomial.leadingCoeff_eq_coeff_of_leadingMonomial_eq_some, CPoly.CMvPolynomial.leadingCoeff_eq_coeff_leadingMonomial, CPoly.CMvPolynomial.leadingTerm_eq_zero_of_leadingMonomial_eq_none, CPoly.CMvPolynomial.leadingTerm_eq_monomial_of_leadingMonomial_eq_some, CPoly.CMvPolynomial.aeval, CPoly.CMvPolynomial.aeval_eq_eval₂, CPoly.CMvPolynomial.aeval_C, CPoly.CMvPolynomial.aeval_add, CPoly.CMvPolynomial.aeval_mul, CPoly.CMvPolynomial.aeval_zero, CPoly.CMvPolynomial.aeval_one, CPoly.CMvPolynomial.aeval_pow, CPoly.CMvPolynomial.aeval_neg, CPoly.CMvPolynomial.aeval_sub, CPoly.CMvPolynomial.bind₁, CPoly.CMvPolynomial.bind₁_eq_aeval, CPoly.CMvPolynomial.bind₁_C, CPoly.CMvPolynomial.bind₁_add, CPoly.CMvPolynomial.bind₁_mul, CPoly.CMvPolynomial.rename, CPoly.CMvPolynomial.sumToIter, CPoly.CMvPolynomial.X_eq_monomial, CPoly.CMvPolynomial.toFinsupp_unitMono, CPoly.CMvPolynomial.fromCMvPolynomial_monomial, CPoly.CMvPolynomial.fromCMvPolynomial_X, CPoly.CMvPolynomial.eval₂_C, CPoly.CMvPolynomial.eval₂_X, CPoly.CMvPolynomial.eval₂Hom_C, CPoly.CMvPolynomial.eval₂Hom_X, CPoly.CMvPolynomial.ringHom_ext, CPoly.CMvPolynomial.aeval_X, CPoly.CMvPolynomial.bind₁_X, CPoly.CMvPolynomial.bind₁_id, CPoly.CMvPolynomial.list_foldl_add_comm, CPoly.CMvPolynomial.foldl_add_comm, CPoly.CMvPolynomial.fromCMvPolynomial_finsupp_sum, CPoly.CMvPolynomial.sumToIter_eq, CPoly.CMvPolynomial.coeff_sumToIter, CPoly.CMvPolynomial.sumToIter_zero, CPoly.CMvPolynomial.sumToIter_add, CPoly.CMvPolynomial.sumToIter_idempotent, CPoly.CMvPolynomial.fromCMvPolynomial_bind₁, CPoly.Lawful.npow_add, CPoly.Lawful.npowBySq_eq_npow
statement: formalized
proof: formalized
---

# Computable multivariate polynomials (extended operations)

`CompPoly.Multivariate.Operations`, in [CompPoly/Multivariate/Operations.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean), by Frantisek Silvasi, Julian Sutherland, Andrei Burdușa, Derek Sorensen, Dimitris Mitsios.

> Operations on `CMvPolynomial` that depend on ring instances from `MvPolyEquiv.lean`,
> such as monomial orders, leading terms, restriction, variable renaming, and substitution.
>
> The core type and basic operations (`CMvPolynomial`, `C`, `X`, `coeff`, `eval`, etc.)
> are in `CMvPolynomial.lean`. The `CommSemiring` and `CommRing` instances are in
> `MvPolyEquiv.lean`.
>
> ## Main definitions
>
> * `MonomialOrder`: Typeclass for comparing monomials.
> * `leadingMonomial`, `leadingCoeff`, `leadingTerm`: Leading term operations
>   according to a monomial order.
> * `rename`: Rename variables using a function `Fin n → Fin m`.
> * `aeval`: Algebra evaluation.
> * `bind₁`: Substitution of polynomials for variables.

> ## Leading-term operations

`CPoly.CMvPolynomial.MonomialOrder` (class, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L46))

> Monomial ordering typeclass for `n` variables.
>
> Provides a way to compare monomials for determining leading terms.

```lean
class MonomialOrder (n : ℕ) where
  compare : CMvMonomial n → CMvMonomial n → Ordering
```

`CPoly.CMvPolynomial.MonomialOrder.degree` (definition, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L55))

> Baseline degree of a monomial.
>
> Currently this is the ordinary total degree and is independent of
> `MonomialOrder.compare`.

```lean
def MonomialOrder.degree {n : ℕ} (m : CMvMonomial n) : ℕ
```

`CPoly.CMvPolynomial.leadingMonomial` (definition, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L62))

> Leading monomial of a polynomial according to a monomial order.
>
> Returns `none` for the zero polynomial.

```lean
def leadingMonomial {n : ℕ} {R : Type*} [Zero R] [MonomialOrder n]
    (p : CMvPolynomial n R) : Option (CMvMonomial n)
```

`CPoly.CMvPolynomial.leadingTerm` (definition, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L79))

> Leading term of a polynomial according to a monomial order.
>
> Returns `0` for the zero polynomial, and otherwise returns the monomial with
> leading monomial and leading coefficient.

```lean
def leadingTerm {n : ℕ} {R : Type*} [Zero R] [BEq R] [LawfulBEq R] [MonomialOrder n]
    (p : CMvPolynomial n R) : CMvPolynomial n R
```

`CPoly.CMvPolynomial.leadingCoeff` (definition, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L89))

> Leading coefficient of a polynomial according to a monomial order.
>
> Returns `0` for the zero polynomial.

```lean
def leadingCoeff {n : ℕ} {R : Type*} [Zero R] [MonomialOrder n]
    (p : CMvPolynomial n R) : R
```

`CPoly.CMvPolynomial.leadingCoeff_eq_zero_of_leadingMonomial_eq_none` (lemma, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L95))

```lean
lemma leadingCoeff_eq_zero_of_leadingMonomial_eq_none
    {n : ℕ} {R : Type*} [Zero R] [MonomialOrder n] {p : CMvPolynomial n R}
    (h : leadingMonomial p = none) : leadingCoeff p = 0
```

`CPoly.CMvPolynomial.leadingCoeff_eq_coeff_of_leadingMonomial_eq_some` (lemma, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L100))

```lean
lemma leadingCoeff_eq_coeff_of_leadingMonomial_eq_some
    {n : ℕ} {R : Type*} [Zero R] [MonomialOrder n] {p : CMvPolynomial n R}
    {m : CMvMonomial n} (h : leadingMonomial p = some m) : leadingCoeff p = coeff m p
```

`CPoly.CMvPolynomial.leadingCoeff_eq_coeff_leadingMonomial` (lemma, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L107))

> Packaged form of `leadingCoeff`: it is the coefficient at the optional leading monomial,
> defaulting to `0` when no leading monomial exists.

```lean
lemma leadingCoeff_eq_coeff_leadingMonomial
    {n : ℕ} {R : Type*} [Zero R] [MonomialOrder n] (p : CMvPolynomial n R) :
    leadingCoeff p = (leadingMonomial p).elim 0 (fun m => coeff m p)
```

`CPoly.CMvPolynomial.leadingTerm_eq_zero_of_leadingMonomial_eq_none` (lemma, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L112))

```lean
lemma leadingTerm_eq_zero_of_leadingMonomial_eq_none
    {n : ℕ} {R : Type*} [Zero R] [BEq R] [LawfulBEq R] [MonomialOrder n]
    {p : CMvPolynomial n R} (h : leadingMonomial p = none) :
    leadingTerm p = 0
```

`CPoly.CMvPolynomial.leadingTerm_eq_monomial_of_leadingMonomial_eq_some` (lemma, [line 118](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L118))

```lean
lemma leadingTerm_eq_monomial_of_leadingMonomial_eq_some
    {n : ℕ} {R : Type*} [Zero R] [BEq R] [LawfulBEq R] [MonomialOrder n]
    {p : CMvPolynomial n R} {m : CMvMonomial n} (h : leadingMonomial p = some m) :
    leadingTerm p = monomial m (coeff m p)
```

> ## Evaluation and substitution

`CPoly.CMvPolynomial.aeval` (definition, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L130))

> Algebra evaluation: evaluates polynomial in an algebra.
>
> Given an algebra `σ` over `R` and a function `f : Fin n → σ`, evaluates the polynomial.

```lean
def aeval {n : ℕ} {R σ : Type*} [CommSemiring R] [CommSemiring σ] [Algebra R σ]
    (f : Fin n → σ) (p : CMvPolynomial n R) : σ
```

`CPoly.CMvPolynomial.aeval_eq_eval₂` (lemma, [line 134](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L134))

```lean
lemma aeval_eq_eval₂ {n : ℕ} {R σ : Type*}
    [CommSemiring R] [CommSemiring σ] [Algebra R σ]
    (f : Fin n → σ) (p : CMvPolynomial n R) :
    aeval f p = eval₂ (algebraMap R σ) f p
```

`CPoly.CMvPolynomial.aeval_C` (lemma, [line 139](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L139))

```lean
lemma aeval_C {n : ℕ} {R σ : Type*}
    [CommSemiring R] [BEq R] [LawfulBEq R]
    [CommSemiring σ] [Algebra R σ]
    (f : Fin n → σ) (c : R) :
    aeval f (CMvPolynomial.C (n := n) c) = algebraMap R σ c
```

`CPoly.CMvPolynomial.aeval_add` (lemma, [line 148](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L148))

```lean
lemma aeval_add {n : ℕ} {R σ : Type*}
    [CommSemiring R] [BEq R] [LawfulBEq R]
    [CommSemiring σ] [Algebra R σ]
    (f : Fin n → σ) (p q : CMvPolynomial n R) :
    aeval f (p + q) = aeval f p + aeval f q
```

`CPoly.CMvPolynomial.aeval_mul` (lemma, [line 157](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L157))

```lean
lemma aeval_mul {n : ℕ} {R σ : Type*}
    [CommSemiring R] [BEq R] [LawfulBEq R]
    [CommSemiring σ] [Algebra R σ]
    (f : Fin n → σ) (p q : CMvPolynomial n R) :
    aeval f (p * q) = aeval f p * aeval f q
```

`CPoly.CMvPolynomial.aeval_zero` (lemma, [line 166](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L166))

```lean
lemma aeval_zero {n : ℕ} {R σ : Type*}
    [CommSemiring R] [BEq R] [LawfulBEq R]
    [CommSemiring σ] [Algebra R σ]
    (f : Fin n → σ) :
    aeval f (0 : CMvPolynomial n R) = 0
```

`CPoly.CMvPolynomial.aeval_one` (lemma, [line 175](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L175))

```lean
lemma aeval_one {n : ℕ} {R σ : Type*}
    [CommSemiring R] [BEq R] [LawfulBEq R]
    [CommSemiring σ] [Algebra R σ]
    (f : Fin n → σ) :
    aeval f (1 : CMvPolynomial n R) = 1
```

`CPoly.CMvPolynomial.aeval_pow` (lemma, [line 184](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L184))

```lean
lemma aeval_pow {n : ℕ} {R σ : Type*}
    [CommSemiring R] [BEq R] [LawfulBEq R]
    [CommSemiring σ] [Algebra R σ]
    (f : Fin n → σ) (p : CMvPolynomial n R) (k : ℕ) :
    aeval f (p ^ k) = (aeval f p) ^ k
```

`CPoly.CMvPolynomial.aeval_neg` (lemma, [line 193](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L193))

```lean
lemma aeval_neg {n : ℕ} {R σ : Type*}
    [CommRing R] [BEq R] [LawfulBEq R]
    [CommRing σ] [Algebra R σ]
    (f : Fin n → σ) (p : CMvPolynomial n R) :
    aeval f (-p) = -(aeval f p)
```

`CPoly.CMvPolynomial.aeval_sub` (lemma, [line 202](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L202))

```lean
lemma aeval_sub {n : ℕ} {R σ : Type*}
    [CommRing R] [BEq R] [LawfulBEq R]
    [CommRing σ] [Algebra R σ]
    (f : Fin n → σ) (p q : CMvPolynomial n R) :
    aeval f (p - q) = aeval f p - aeval f q
```

`CPoly.CMvPolynomial.bind₁` (definition, [line 215](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L215))

> Substitution: substitutes polynomials for variables.
>
> Given `f : Fin n → CMvPolynomial m R`, substitutes `f i` for variable `X i`.

```lean
def bind₁ {n m : ℕ} {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    (f : Fin n → CMvPolynomial m R) (p : CMvPolynomial n R) : CMvPolynomial m R
```

`CPoly.CMvPolynomial.bind₁_eq_aeval` (lemma, [line 222](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L222))

> The computable substitution `bind₁` agrees with algebraic evaluation.

```lean
lemma bind₁_eq_aeval {n m : ℕ} {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    (f : Fin n → CMvPolynomial m R) (p : CMvPolynomial n R) :
    bind₁ f p = aeval (σ := CMvPolynomial m R) f p
```

`CPoly.CMvPolynomial.bind₁_C` (lemma, [line 232](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L232))

```lean
lemma bind₁_C {n m : ℕ} {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    (f : Fin n → CMvPolynomial m R) (c : R) :
    bind₁ f (CMvPolynomial.C (n := n) c) = CMvPolynomial.C (n := m) c
```

`CPoly.CMvPolynomial.bind₁_add` (lemma, [line 239](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L239))

```lean
lemma bind₁_add {n m : ℕ} {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    (f : Fin n → CMvPolynomial m R) (p q : CMvPolynomial n R) :
    bind₁ f (p + q) = bind₁ f p + bind₁ f q
```

`CPoly.CMvPolynomial.bind₁_mul` (lemma, [line 245](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L245))

```lean
lemma bind₁_mul {n m : ℕ} {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    (f : Fin n → CMvPolynomial m R) (p q : CMvPolynomial n R) :
    bind₁ f (p * q) = bind₁ f p * bind₁ f q
```

> ## Core operations

`CPoly.CMvPolynomial.rename` (definition, [line 257](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L257))

> Rename variables using a function.
>
> Given `f : Fin n → Fin m`, renames variable `X i` to `X (f i)`.

```lean
def rename {n m : ℕ} {R : Type*} [Zero R] [Add R] [BEq R] [LawfulBEq R]
    (f : Fin n → Fin m) (p : CMvPolynomial n R) : CMvPolynomial m R
```

`CPoly.CMvPolynomial.sumToIter` (definition, [line 266](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L266))

> Iterative reconstruction of a polynomial by folding over terms.

```lean
def sumToIter {n : ℕ} {R : Type*} [Zero R] [Add R] [BEq R] [LawfulBEq R]
    (p : CMvPolynomial n R) : CMvPolynomial n R
```

> ## Bridge and transport lemmas (technical)

`CPoly.CMvPolynomial.X_eq_monomial` (lemma, [line 272](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L272))

```lean
lemma X_eq_monomial {k : ℕ} {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    (i : Fin k) :
    CMvPolynomial.X (R := R) i = CMvPolynomial.monomial
      (Vector.ofFn (fun j => if j = i then 1 else 0))
      (1 : R)
```

`CPoly.CMvPolynomial.toFinsupp_unitMono` (lemma, [line 284](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L284))

```lean
lemma toFinsupp_unitMono {k : ℕ}
    (i : Fin k) :
    CMvMonomial.toFinsupp
      (Vector.ofFn (fun j : Fin k =>
        if j = i then 1 else 0)) =
    Finsupp.single i 1
```

`CPoly.CMvPolynomial.fromCMvPolynomial_monomial` (lemma, [line 295](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L295))

```lean
lemma fromCMvPolynomial_monomial {k : ℕ} {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    (mono : CMvMonomial k) (c : R) :
    fromCMvPolynomial (CMvPolynomial.monomial mono c) =
    MvPolynomial.monomial (CMvMonomial.toFinsupp mono) c
```

`CPoly.CMvPolynomial.fromCMvPolynomial_X` (lemma, [line 322](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L322))

```lean
lemma fromCMvPolynomial_X {k : ℕ} {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    (i : Fin k) :
    fromCMvPolynomial (CMvPolynomial.X (R := R) i) =
    MvPolynomial.X i
```

> ### `C` and `eval₂` as ring homomorphisms

`CPoly.CMvPolynomial.eval₂_C` (theorem, [line 331](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L331))

```lean
theorem eval₂_C {n : ℕ} {R S : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    [CommSemiring S] (f : R →+* S) (vs : Fin n → S) (c : R) :
    CMvPolynomial.eval₂ f vs (CMvPolynomial.C c) = f c
```

`CPoly.CMvPolynomial.eval₂_X` (theorem, [line 336](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L336))

```lean
theorem eval₂_X {n : ℕ} {R S : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    [CommSemiring S] (f : R →+* S) (vs : Fin n → S) (i : Fin n) :
    CMvPolynomial.eval₂ f vs (CMvPolynomial.X i) = vs i
```

`CPoly.CMvPolynomial.eval₂Hom_C` (theorem, [line 341](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L341))

```lean
theorem eval₂Hom_C {n : ℕ} {R S : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    [CommSemiring S] (f : R →+* S) (vs : Fin n → S) (c : R) :
    CMvPolynomial.eval₂Hom f vs (CMvPolynomial.C c) = f c
```

`CPoly.CMvPolynomial.eval₂Hom_X` (theorem, [line 346](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L346))

```lean
theorem eval₂Hom_X {n : ℕ} {R S : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    [CommSemiring S] (f : R →+* S) (vs : Fin n → S) (i : Fin n) :
    CMvPolynomial.eval₂Hom f vs (CMvPolynomial.X i) = vs i
```

`CPoly.CMvPolynomial.ringHom_ext` (theorem, [line 353](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L353))

> Two ring homomorphisms out of `CMvPolynomial n R` are equal once they agree on the constants
> and on every variable.

```lean
theorem ringHom_ext {n : ℕ} {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    {T : Type*} [Semiring T] {f g : CMvPolynomial n R →+* T}
    (hC : ∀ c, f (CMvPolynomial.C c) = g (CMvPolynomial.C c))
    (hX : ∀ i, f (CMvPolynomial.X i) = g (CMvPolynomial.X i)) : f = g
```

`CPoly.CMvPolynomial.aeval_X` (lemma, [line 374](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L374))

```lean
lemma aeval_X {n : ℕ} {R σ : Type*}
    [CommSemiring R] [BEq R] [LawfulBEq R]
    [CommSemiring σ] [Algebra R σ]
    (f : Fin n → σ) (i : Fin n) :
    aeval f (CMvPolynomial.X (R := R) i) = f i
```

`CPoly.CMvPolynomial.bind₁_X` (lemma, [line 383](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L383))

```lean
lemma bind₁_X {n m : ℕ} {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    (f : Fin n → CMvPolynomial m R) (i : Fin n) :
    bind₁ f (CMvPolynomial.X (R := R) i) = f i
```

`CPoly.CMvPolynomial.bind₁_id` (lemma, [line 388](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L388))

```lean
lemma bind₁_id {n : ℕ} {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    (p : CMvPolynomial n R) :
    bind₁ (fun i => CMvPolynomial.X (R := R) i) p = p
```

`CPoly.CMvPolynomial.list_foldl_add_comm` (lemma, [line 444](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L444))

```lean
lemma list_foldl_add_comm {β K V : Type*} [AddCommMonoid β]
    (g : K → V → β) (l : List (K × V)) (init : β) :
    List.foldl (fun acc pair => acc + g pair.1 pair.2) init l =
    List.foldl (fun acc pair => g pair.1 pair.2 + acc) init l
```

`CPoly.CMvPolynomial.foldl_add_comm` (lemma, [line 455](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L455))

```lean
lemma foldl_add_comm {β : Type*} [AddCommMonoid β] {k : ℕ}
    {R' : Type*} (g : CMvMonomial k → R' → β)
    (t : Std.ExtTreeMap (CMvMonomial k) R') :
    Std.ExtTreeMap.foldl (fun acc m c => acc + g m c) (0 : β) t =
    Std.ExtTreeMap.foldl (fun acc m c => g m c + acc) (0 : β) t
```

`CPoly.CMvPolynomial.fromCMvPolynomial_finsupp_sum` (lemma, [line 463](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L463))

```lean
lemma fromCMvPolynomial_finsupp_sum {n k : ℕ} [CommSemiring R] [BEq R] [LawfulBEq R]
    (g : (Fin n →₀ ℕ) → R → CMvPolynomial k R)
    (a : CMvPolynomial n R) :
    fromCMvPolynomial (Finsupp.sum (AddMonoidAlgebra.coeff (fromCMvPolynomial a)) g) =
    Finsupp.sum (AddMonoidAlgebra.coeff (fromCMvPolynomial a))
      (fun μ c => fromCMvPolynomial (g μ c))
```

> ## API lemmas for `sumToIter`

`CPoly.CMvPolynomial.sumToIter_eq` (lemma, [line 474](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L474))

```lean
lemma sumToIter_eq {n : ℕ} {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    (p : CMvPolynomial n R) : sumToIter p = p
```

`CPoly.CMvPolynomial.coeff_sumToIter` (lemma, [line 485](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L485))

```lean
lemma coeff_sumToIter {n : ℕ} {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    (m : CMvMonomial n) (p : CMvPolynomial n R) :
    coeff m (sumToIter p) = coeff m p
```

`CPoly.CMvPolynomial.sumToIter_zero` (lemma, [line 490](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L490))

```lean
lemma sumToIter_zero {n : ℕ} {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R] :
    sumToIter (0 : CMvPolynomial n R) = 0
```

`CPoly.CMvPolynomial.sumToIter_add` (lemma, [line 494](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L494))

```lean
lemma sumToIter_add {n : ℕ} {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    (p q : CMvPolynomial n R) :
    sumToIter (p + q) = sumToIter p + sumToIter q
```

`CPoly.CMvPolynomial.sumToIter_idempotent` (lemma, [line 499](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L499))

```lean
lemma sumToIter_idempotent {n : ℕ} {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    (p : CMvPolynomial n R) :
    sumToIter (sumToIter p) = sumToIter p
```

`CPoly.CMvPolynomial.fromCMvPolynomial_bind₁` (theorem, [line 510](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L510))

> The computable substitution `bind₁` agrees with Mathlib substitution after
> transporting through `fromCMvPolynomial`.

```lean
theorem fromCMvPolynomial_bind₁ {n m : ℕ} {R : Type*} [CommSemiring R] [BEq R]
    [LawfulBEq R] (f : Fin n → CMvPolynomial m R) (p : CMvPolynomial n R) :
    fromCMvPolynomial (bind₁ f p) =
      MvPolynomial.eval₂ MvPolynomial.C (fun i => fromCMvPolynomial (f i))
        (fromCMvPolynomial p)
```

> ### Equivalence between `npow` and `npowBySq`
>
> `Lawful.npow` (defined in `Multivariate/Lawful.lean`) is the naive `O(k)`
> specification; `Lawful.npowBySq` is the `O(log k)` repeated-squaring
> implementation. We prove pointwise equality here so that the `NatPow` instance
> can be safely routed through the fast version.
>
> The proofs need `mul_assoc` / `mul_one` / `mul_comm`, which are only available
> once the `CommSemiring (CMvPolynomial n R)` instance has been built — that is
> why these lemmas live in `Operations.lean` rather than in `Lawful.lean`.

`CPoly.Lawful.npow_add` (lemma, [line 564](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L564))

> Additive law for the naive `npow`: $p^{a+b} = p^a \cdot p^b$.

```lean
lemma npow_add (p : Lawful n R) (a b : ℕ) :
    npow (a + b) p = npow a p * npow b p
```

`CPoly.Lawful.npowBySq_eq_npow` (theorem, [line 576](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean#L576))

> The fast repeated-squaring `npowBySq` agrees pointwise with the naive
> `npow`. This is the equivalence that lets the `NatPow (Lawful n R)` instance
> be routed through `npowBySq` without changing observable behavior.

```lean
theorem npowBySq_eq_npow (p : Lawful n R) : ∀ k : ℕ, npowBySq p k = npow k p
```

## Depends on

- [`CMvPolynomial`/`MvPolynomial` Evaluation](mvpolyequiv/eval.md)

## Sources

- [CompPoly/Multivariate/Operations.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Operations.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multivariate.Operations.json)
