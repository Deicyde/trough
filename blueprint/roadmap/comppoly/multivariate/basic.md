---
catalog: module
lean: CPoly.CMvPolynomial, CPoly.CMvPolynomial.C, CPoly.CMvPolynomial.X, CPoly.CMvPolynomial.coeff, CPoly.CMvPolynomial.ext, CPoly.CMvPolynomial.fromUnlawful_zero, CPoly.CMvPolynomial.add_getD?, CPoly.CMvPolynomial.coeff_zero, CPoly.CMvPolynomial.coeff_add, CPoly.CMvPolynomial.fromUnlawful_fold_eq_fold_fromUnlawful₀, CPoly.CMvPolynomial.fromUnlawful_fold_eq_fold_fromUnlawful, CPoly.CMvPolynomial.eval₂, CPoly.CMvPolynomial.HornerTerm, CPoly.CMvPolynomial.HornerGroup, CPoly.CMvPolynomial.hornerExponent, CPoly.CMvPolynomial.insertHornerTerm, CPoly.CMvPolynomial.insertHornerGroupDesc, CPoly.CMvPolynomial.collectHornerGroups, CPoly.CMvPolynomial.sortHornerGroups, CPoly.CMvPolynomial.hornerGroups, CPoly.CMvPolynomial.evalSparseHornerGroups, CPoly.CMvPolynomial.eval₂HornerTerms, CPoly.CMvPolynomial.eval₂Horner, CPoly.CMvPolynomial.eval, CPoly.CMvPolynomial.evalHorner, CPoly.CMvPolynomial.support, CPoly.CMvPolynomial.support_def, CPoly.CMvPolynomial.totalDegree, CPoly.CMvPolynomial.degreeOf, CPoly.CMvPolynomial.monomial, CPoly.CMvPolynomial.degrees, CPoly.CMvPolynomial.degreeOf_eq_count_degrees, CPoly.CMvPolynomial.vars, CPoly.CMvPolynomial.restrictBy, CPoly.CMvPolynomial.restrictTotalDegreeOf, CPoly.CMvPolynomial.restrictDegreeOf
statement: formalized
proof: formalized
---

# Computable multivariate polynomials

`CompPoly.Multivariate.Basic`, in [CompPoly/Multivariate/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean), by Frantisek Silvasi, Julian Sutherland, Andrei Burdușa, Derek Sorensen, Dimitris Mitsios.

> Polynomials of the form `α₁ * m₁ + α₂ * m₂ + ... + αₖ * mₖ` where `αᵢ` is any semiring
> and `mᵢ` is a `CMvMonomial`.
>
> This is implemented as a wrapper around `CPoly.Lawful`, which ensures that all stored
> coefficients are non-zero.
>
> This file contains the core type definition and basic operations. Higher-level definitions
> that depend on ring instances (monomial orders, `rename`, `aeval`, etc.) are in
> `CMvPolynomial.lean`. The `CommSemiring` and `CommRing` instances are in `MvPolyEquiv.lean`.
>
> ## Main definitions
>
> * `CPoly.CMvPolynomial n R`: The type of multivariate polynomials in `n` variables
>   with coefficients in `R`.
> * `CPoly.CMvPolynomial.C`: Constant polynomial constructor.
> * `CPoly.CMvPolynomial.X`: Variable polynomial constructor.
> * `CPoly.CMvPolynomial.monomial`: Monomial constructor.
> * `CPoly.CMvPolynomial.coeff`: Extract the coefficient of a monomial.
> * `CPoly.CMvPolynomial.eval₂`, `CPoly.CMvPolynomial.eval`: Polynomial evaluation.
> * `CPoly.CMvPolynomial.eval₂Horner`, `CPoly.CMvPolynomial.evalHorner`:
>   Polynomial evaluation using Horner's method.
> * `CPoly.CMvPolynomial.support`, `CPoly.CMvPolynomial.totalDegree`,
>   `CPoly.CMvPolynomial.degreeOf`, `CPoly.CMvPolynomial.degrees`,
>   `CPoly.CMvPolynomial.vars`: Degree and support queries.

`CPoly.CMvPolynomial` (abbreviation, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L48))

> A computable multivariate polynomial in `n` variables with coefficients in `R`.

```lean
abbrev CMvPolynomial (n : ℕ) (R : Type*) [Zero R] : Type _
```

`CPoly.CMvPolynomial.C` (definition, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L55))

> Construct a constant polynomial.

```lean
def C {n : ℕ} {R : Type*} [BEq R] [LawfulBEq R] [Zero R] (c : R) : CMvPolynomial n R
```

`CPoly.CMvPolynomial.X` (definition, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L59))

> Construct the polynomial $X_i$.

```lean
def X {n : ℕ} {R : Type*} [Zero R] [One R] [BEq R] [LawfulBEq R]
    (i : Fin n) : CMvPolynomial n R
```

`CPoly.CMvPolynomial.coeff` (definition, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L65))

> Extract the coefficient of a monomial.

```lean
def coeff {R : Type*} {n : ℕ} [Zero R] (m : CMvMonomial n) (p : CMvPolynomial n R) : R
```

`CPoly.CMvPolynomial.ext` (theorem, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L72))

> Extensionality: two polynomials are equal if all their coefficients are equal.

```lean
theorem ext {n : ℕ} [Zero R] (p q : CMvPolynomial n R)
    (h : ∀ m, coeff m p = coeff m q) : p = q
```

`CPoly.CMvPolynomial.fromUnlawful_zero` (lemma, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L88))

```lean
lemma fromUnlawful_zero {n : ℕ} [Zero R] : Lawful.fromUnlawful 0 = (0 : Lawful n R)
```

`CPoly.CMvPolynomial.add_getD?` (lemma, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L95))

```lean
lemma add_getD? : (p + q).val[m]?.getD 0 = p.val[m]?.getD 0 + q.val[m]?.getD 0
```

`CPoly.CMvPolynomial.coeff_zero` (lemma, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L100))

```lean
lemma coeff_zero : ∀ σ, coeff σ (0 : CMvPolynomial n R) = 0
```

`CPoly.CMvPolynomial.coeff_add` (lemma, [line 106](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L106))

```lean
lemma coeff_add : coeff m (p + q) = coeff m p + coeff m q
```

`CPoly.CMvPolynomial.fromUnlawful_fold_eq_fold_fromUnlawful₀` (lemma, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L109))

> Auxiliary lemma showing that conversion from unlawful polynomials respects the sum fold.

```lean
lemma fromUnlawful_fold_eq_fold_fromUnlawful₀
    {t : List (CMvMonomial n × R)} {f : CMvMonomial n → R → Unlawful n R} :
    ∀ init : Unlawful n R,
    Lawful.fromUnlawful (List.foldl (fun u term => (f term.1 term.2) + u) init t) =
    List.foldl (fun l term => (Lawful.fromUnlawful (f term.1 term.2)) + l)
               (Lawful.fromUnlawful init) t
```

`CPoly.CMvPolynomial.fromUnlawful_fold_eq_fold_fromUnlawful` (lemma, [line 127](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L127))

> Auxiliary lemma showing that conversion from unlawful polynomials respects
> the fold over terms.

```lean
lemma fromUnlawful_fold_eq_fold_fromUnlawful {t : Unlawful n R}
    {f : CMvMonomial n → R → Unlawful n R} :
  Lawful.fromUnlawful (ExtTreeMap.foldl (fun u m c => (f m c) + u) 0 t) =
  ExtTreeMap.foldl (fun l m c => (Lawful.fromUnlawful (f m c)) + l) 0 t
```

`CPoly.CMvPolynomial.eval₂` (definition, [line 139](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L139))

> Evaluate a polynomial at a point given by a ring homomorphism `f`
> and variable assignments `vs`.

```lean
def eval₂ {R S : Type*} {n : ℕ} [Semiring R] [CommSemiring S] :
    (R →+* S) → (Fin n → S) → CMvPolynomial n R → S
```

`CPoly.CMvPolynomial.HornerTerm` (abbreviation, [line 144](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L144))

> Term representation used by the fixed-order multivariate Horner evaluator.

```lean
abbrev HornerTerm (n : ℕ) (S : Type*)
```

`CPoly.CMvPolynomial.HornerGroup` (abbreviation, [line 147](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L147))

> Terms grouped by one variable exponent.

```lean
abbrev HornerGroup (n : ℕ) (S : Type*)
```

`CPoly.CMvPolynomial.hornerExponent` (definition, [line 150](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L150))

> Read the exponent for a variable index represented as a natural number.

```lean
def hornerExponent {n : ℕ} (k : ℕ) (m : CMvMonomial n) : ℕ
```

`CPoly.CMvPolynomial.insertHornerTerm` (definition, [line 154](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L154))

> Add a term to an association list keyed by the current variable exponent.

```lean
def insertHornerTerm {n : ℕ} {S : Type*}
    (exponent : ℕ) (term : HornerTerm n S) :
    List (HornerGroup n S) → List (HornerGroup n S)
```

`CPoly.CMvPolynomial.insertHornerGroupDesc` (definition, [line 165](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L165))

> Insert an exponent group into descending exponent order.

```lean
def insertHornerGroupDesc {n : ℕ} {S : Type*}
    (group : HornerGroup n S) : List (HornerGroup n S) → List (HornerGroup n S)
```

`CPoly.CMvPolynomial.collectHornerGroups` (definition, [line 175](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L175))

> Collect terms into association-list groups keyed by the current variable exponent.

```lean
def collectHornerGroups {n : ℕ} {S : Type*}
    (k : ℕ) (terms : List (HornerTerm n S)) : List (HornerGroup n S)
```

`CPoly.CMvPolynomial.sortHornerGroups` (definition, [line 181](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L181))

> Sort exponent groups from high exponent to low exponent.

```lean
def sortHornerGroups {n : ℕ} {S : Type*}
    (groups : List (HornerGroup n S)) : List (HornerGroup n S)
```

`CPoly.CMvPolynomial.hornerGroups` (definition, [line 186](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L186))

> Group terms by the current variable exponent, sorted from high to low exponent.

```lean
def hornerGroups {n : ℕ} {S : Type*}
    (k : ℕ) (terms : List (HornerTerm n S)) : List (HornerGroup n S)
```

`CPoly.CMvPolynomial.evalSparseHornerGroups` (definition, [line 191](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L191))

> Sparse Horner fold for already-evaluated coefficient groups.

```lean
def evalSparseHornerGroups {S : Type*} [CommSemiring S]
    (x : S) : List (ℕ × S) → S
```

`CPoly.CMvPolynomial.eval₂HornerTerms` (definition, [line 205](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L205))

> Evaluate sparse multivariate terms by fixed-order Horner in variables `0, 1, ..., n-1`.

```lean
def eval₂HornerTerms {n : ℕ} {S : Type*} [CommSemiring S]
    (xs : ℕ → S) : ℕ → ℕ → List (HornerTerm n S) → S
```

`CPoly.CMvPolynomial.eval₂Horner` (definition, [line 215](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L215))

> Evaluate a polynomial using fixed-order multivariate Horner evaluation.

```lean
def eval₂Horner {R S : Type*} {n : ℕ} [Semiring R] [CommSemiring S] :
    (R →+* S) → (Fin n → S) → CMvPolynomial n R → S
```

`CPoly.CMvPolynomial.eval` (definition, [line 223](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L223))

> Evaluate a polynomial at a given point.

```lean
def eval {R : Type*} {n : ℕ} [CommSemiring R] : (Fin n → R) → CMvPolynomial n R → R
```

`CPoly.CMvPolynomial.evalHorner` (definition, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L227))

> Evaluate a polynomial at a given point using fixed-order multivariate Horner evaluation.

```lean
def evalHorner {R : Type*} {n : ℕ} [CommSemiring R] :
    (Fin n → R) → CMvPolynomial n R → R
```

`CPoly.CMvPolynomial.support` (definition, [line 233](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L233))

> The support of a polynomial (set of monomials with non-zero coefficients),
> represented as Finsupps.

```lean
def support {R : Type*} {n : ℕ} [Zero R] (p : CMvPolynomial n R) : Finset (Fin n →₀ ℕ)
```

`CPoly.CMvPolynomial.support_def` (lemma, [line 237](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L237))

```lean
lemma support_def {R : Type*} {n : ℕ} [Zero R] {p : CMvPolynomial n R} :
    ∀ σ, σ ∈ p.support ↔ p.coeff (CMvMonomial.ofFinsupp σ) ≠ 0
```

`CPoly.CMvPolynomial.totalDegree` (definition, [line 254](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L254))

> The total degree of a polynomial (maximum total degree of its monomials).

```lean
def totalDegree {R : Type*} {n : ℕ} [Zero R] : CMvPolynomial n R → ℕ
```

`CPoly.CMvPolynomial.degreeOf` (definition, [line 259](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L259))

> The degree of a polynomial in a specific variable.

```lean
def degreeOf {R : Type*} {n : ℕ} [Zero R] (i : Fin n) : CMvPolynomial n R → ℕ
```

`CPoly.CMvPolynomial.monomial` (definition, [line 266](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L266))

> Construct a monomial `c * m` as a `CMvPolynomial n R`.
>
> Creates a polynomial with a single monomial term. If `c = 0`, returns the zero polynomial.

```lean
def monomial {n : ℕ} {R : Type*} [BEq R] [LawfulBEq R] [Zero R]
    (m : CMvMonomial n) (c : R) : CMvPolynomial n R
```

`CPoly.CMvPolynomial.degrees` (definition, [line 274](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L274))

> Multiset of all variable degrees appearing in the polynomial.
>
> Each variable `i` appears `degreeOf i p` times in the multiset.

```lean
def degrees {n : ℕ} {R : Type*} [Zero R] (p : CMvPolynomial n R) : Multiset (Fin n)
```

`CPoly.CMvPolynomial.degreeOf_eq_count_degrees` (lemma, [line 278](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L278))

> `degreeOf` is the multiplicity of a variable in `degrees`.

```lean
lemma degreeOf_eq_count_degrees {n : ℕ} {R : Type*} [Zero R]
    (i : Fin n) (p : CMvPolynomial n R) :
    p.degreeOf i = Multiset.count i p.degrees
```

`CPoly.CMvPolynomial.vars` (definition, [line 299](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L299))

> Extract the set of variables that appear in a polynomial.
>
> Returns the set of variable indices `i : Fin n` such that `degreeOf i p > 0`.

```lean
def vars {n : ℕ} {R : Type*} [Zero R] (p : CMvPolynomial n R) : Finset (Fin n)
```

`CPoly.CMvPolynomial.restrictBy` (definition, [line 303](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L303))

> Filter a polynomial, keeping only monomials for which `keep m` is true.

```lean
def restrictBy {n : ℕ} {R : Type*} [BEq R] [LawfulBEq R] [Zero R]
    (keep : CMvMonomial n → Prop) [DecidablePred keep]
    (p : CMvPolynomial n R) : CMvPolynomial n R
```

`CPoly.CMvPolynomial.restrictTotalDegreeOf` (definition, [line 312](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L312))

> Restrict polynomial to monomials with total degree ≤ d.
>
> Filters out all monomials where `m.totalDegree > d`.

```lean
def restrictTotalDegreeOf {n : ℕ} {R : Type*} [BEq R] [LawfulBEq R] [Zero R]
    (d : ℕ) (p : CMvPolynomial n R) : CMvPolynomial n R
```

`CPoly.CMvPolynomial.restrictDegreeOf` (definition, [line 320](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean#L320))

> Restrict polynomial to monomials whose degree in each variable is ≤ d.
>
> Filters out all monomials where `m.degreeOf i > d` for some variable `i`.

```lean
def restrictDegreeOf {n : ℕ} {R : Type*} [BEq R] [LawfulBEq R] [Zero R]
    (d : ℕ) (p : CMvPolynomial n R) : CMvPolynomial n R
```

## Depends on

- ['Lawful' finite supports](lawful.md)

## Sources

- [CompPoly/Multivariate/Basic.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Basic.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multivariate.Basic.json)
