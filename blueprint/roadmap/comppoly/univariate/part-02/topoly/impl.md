---
catalog: module
lean: CompPoly.CPolynomial.monomial_toPoly, CompPoly.CPolynomial.C_toPoly, CompPoly.CPolynomial.C_one, CompPoly.CPolynomial.X_toPoly, CompPoly.CPolynomial.eval_toPoly, CompPoly.CPolynomial.eval_C, CompPoly.CPolynomial.Raw.eval₂_toPoly, CompPoly.CPolynomial.eval₂_toPoly, CompPoly.CPolynomial.coeff_toPoly, CompPoly.CPolynomial.eval_zero_eq_coeff_zero, CompPoly.CPolynomial.divX_toPoly, CompPoly.CPolynomial.support_toPoly, CompPoly.CPolynomial.degree_toPoly, CompPoly.CPolynomial.natDegree_toPoly, CompPoly.CPolynomial.leadingCoeff_toPoly, CompPoly.CPolynomial.monic_toPoly_iff, CompPoly.CPolynomial.erase_toPoly, CompPoly.CPolynomial.C_mul_X_pow_toPoly, CompPoly.CPolynomial.lcoeff_toPoly, CompPoly.CPolynomial.degreeLE_toPoly, CompPoly.CPolynomial.degreeLT_toPoly, CompPoly.CPolynomial.eval_mul, CompPoly.CPolynomial.eval_ext, CompPoly.CPolynomial.eval_sub, CompPoly.CPolynomial.eval_one, CompPoly.CPolynomial.toPoly_eval, CompPoly.CPolynomial.toPoly_coeff, CompPoly.CPolynomial.toPoly_degree, CompPoly.CPolynomial.toPoly_natDegree, CompPoly.CPolynomial.toPoly_leadingCoeff, CompPoly.CPolynomial.eval_zero, CompPoly.CPolynomial.eval_add, CompPoly.CPolynomial.eval_neg, CompPoly.CPolynomial.eval_X, CompPoly.CPolynomial.eval_pow, CompPoly.CPolynomial.eval_monomial, CompPoly.CPolynomial.eval_divX_eq_zero_of_ne_zero_root, CompPoly.CPolynomial.divX_ne_zero_of_ne_zero_coeff_zero, CompPoly.CPolynomial.Raw.eval_sub_C_mul_X_pow_trim_eq_self_of_eval_eq_zero, CompPoly.CPolynomial.Raw.eval_divModByMonicAux_go_snd_eq_self_of_eval_eq_zero, CompPoly.CPolynomial.Raw.eval_modByMonic_eq_self_of_eval_eq_zero, CompPoly.CPolynomial.eval_modByMonic_eq_self_of_eval_eq_zero
statement: formalized
proof: formalized
---

# Proofs of Correctness for CPolynomial Operations, wrt Mathlib Specs

`CompPoly.Univariate.ToPoly.Impl`, in [CompPoly/Univariate/ToPoly/Impl.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean), by Quang Dao, Gregor Mitscha-Baude, Derek Sorensen.

> Proofs that operations defined on CPolynomial and CPolynomial.Raw are correct
> wrt the mathlib specs, using the ring equivalence

`CompPoly.CPolynomial.monomial_toPoly` (theorem, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L35))

> CPolynomial.monomial is correct wrt the Mathlib spec.

```lean
theorem monomial_toPoly [BEq R] [LawfulBEq R] [DecidableEq R] (n : ℕ) (c : R) :
    (monomial n c).toPoly = Polynomial.monomial n c
```

`CompPoly.CPolynomial.C_toPoly` (theorem, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L43))

> CPolynomial.C is correct wrt the Mathlib spec.

```lean
theorem C_toPoly [BEq R] [LawfulBEq R] (r : R) : (C r).toPoly = Polynomial.C r
```

`CompPoly.CPolynomial.C_one` (theorem, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L50))

> The constant polynomial `C 1` is `1`.

```lean
theorem C_one [BEq R] [LawfulBEq R] [Nontrivial R] : (C 1 : CPolynomial R) = 1
```

`CompPoly.CPolynomial.X_toPoly` (theorem, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L55))

> CPolynomial.X is correct wrt the Mathlib spec.

```lean
theorem X_toPoly [BEq R] [LawfulBEq R] [Nontrivial R] :
    (X : CPolynomial R).toPoly = Polynomial.X
```

`CompPoly.CPolynomial.eval_toPoly` (theorem, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L61))

> CPolynomial.eval is correct wrt the Mathlib spec.

```lean
theorem eval_toPoly [BEq R] [LawfulBEq R] (x : R) (p : CPolynomial R) :
    eval x p = p.toPoly.eval x
```

`CompPoly.CPolynomial.eval_C` (theorem, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L68))

> Evaluation of a constant computable polynomial.

```lean
theorem eval_C [BEq R] [LawfulBEq R] (a c : R) :
    CPolynomial.eval a (CPolynomial.C c) = c
```

`CompPoly.CPolynomial.Raw.eval₂_toPoly` (theorem, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L73))

> Raw.eval₂ is correct wrt the Mathlib spec.

```lean
theorem Raw.eval₂_toPoly {S : Type*} [Semiring S]
    (f : R →+* S) (x : S) (p : CPolynomial.Raw R) :
    p.eval₂ f x = p.toPoly.eval₂ f x
```

`CompPoly.CPolynomial.eval₂_toPoly` (theorem, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L86))

> CPolynomial.eval₂ is correct wrt the Mathlib spec.

```lean
theorem eval₂_toPoly {S : Type*} [Semiring S]
    (f : R →+* S) (x : S) (p : CPolynomial R) :
    eval₂ f x p = p.toPoly.eval₂ f x
```

`CompPoly.CPolynomial.coeff_toPoly` (theorem, [line 94](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L94))

> CPolynomial.coeff is correct wrt the Mathlib spec.

```lean
theorem coeff_toPoly [BEq R] [LawfulBEq R] (p : CPolynomial R) (i : ℕ) :
    p.coeff i = p.toPoly.coeff i
```

`CompPoly.CPolynomial.eval_zero_eq_coeff_zero` (theorem, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L100))

> Evaluation at zero returns the constant coefficient.

```lean
theorem eval_zero_eq_coeff_zero [BEq R] [LawfulBEq R]
    (p : CPolynomial R) : CPolynomial.eval 0 p = p.coeff 0
```

`CompPoly.CPolynomial.divX_toPoly` (theorem, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L107))

> CPolynomial.divX is correct wrt the Mathlib spec.

```lean
theorem divX_toPoly [BEq R] [LawfulBEq R] (p : CPolynomial R) :
    (divX p).toPoly = p.toPoly.divX
```

`CompPoly.CPolynomial.support_toPoly` (theorem, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L114))

> CPolynomial.support is correct wrt the Mathlib spec.

```lean
theorem support_toPoly [BEq R] [LawfulBEq R] (p : CPolynomial R) :
    p.support = p.toPoly.support
```

`CompPoly.CPolynomial.degree_toPoly` (theorem, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L137))

> CPolynomial.degree is correct wrt the Mathlib spec.

```lean
theorem degree_toPoly [BEq R] [LawfulBEq R] (p : CPolynomial R) :
    p.degree = p.toPoly.degree
```

`CompPoly.CPolynomial.natDegree_toPoly` (theorem, [line 154](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L154))

> CPolynomial.natDegree is correct wrt the Mathlib spec.

```lean
theorem natDegree_toPoly [BEq R] [LawfulBEq R] (p : CPolynomial R) :
    p.natDegree = p.toPoly.natDegree
```

`CompPoly.CPolynomial.leadingCoeff_toPoly` (theorem, [line 176](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L176))

> CPolynomial.leadingCoeff is correct wrt the Mathlib spec.

```lean
theorem leadingCoeff_toPoly [BEq R] [LawfulBEq R] (p : CPolynomial R) :
    p.leadingCoeff = p.toPoly.leadingCoeff
```

`CompPoly.CPolynomial.monic_toPoly_iff` (theorem, [line 196](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L196))

> CPolynomial.monic is correct wrt the Mathlib spec

```lean
theorem monic_toPoly_iff [BEq R] [LawfulBEq R] (p : CPolynomial R) :
    p.monic ↔ p.toPoly.Monic
```

`CompPoly.CPolynomial.erase_toPoly` (theorem, [line 201](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L201))

> CPolynomial.erase is correct wrt the Mathlib spec.

```lean
theorem erase_toPoly {R : Type*} [Ring R] [BEq R] [LawfulBEq R] [DecidableEq R]
    (n : ℕ) (p : CPolynomial R) :
    (erase n p).toPoly = p.toPoly.erase n
```

`CompPoly.CPolynomial.C_mul_X_pow_toPoly` (theorem, [line 208](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L208))

> CPolynomial.C r mul CPolynomial.X ^ n is correct wrt the Mathlib spec.

```lean
theorem C_mul_X_pow_toPoly [BEq R] [LawfulBEq R] [DecidableEq R] [Nontrivial R] (r : R) (n : ℕ) :
    (C r * X ^ n).toPoly = Polynomial.monomial n r
```

`CompPoly.CPolynomial.lcoeff_toPoly` (theorem, [line 214](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L214))

> CPolynomial.lcoeff is correct wrt the Mathlib spec.

```lean
theorem lcoeff_toPoly [BEq R] [LawfulBEq R] (n : ℕ) (p : CPolynomial R) :
    lcoeff (R := R) n p = Polynomial.lcoeff R n (toPoly p)
```

`CompPoly.CPolynomial.degreeLE_toPoly` (theorem, [line 219](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L219))

> CPolynomial.degreeLE is correct wrt the Mathlib spec.

```lean
theorem degreeLE_toPoly {n : WithBot ℕ} [BEq R] [LawfulBEq R] {p : CPolynomial R} :
    p ∈ degreeLE (R := R) n ↔ p.toPoly ∈ Polynomial.degreeLE R n
```

`CompPoly.CPolynomial.degreeLT_toPoly` (theorem, [line 226](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L226))

> CPolynomial.degreeLT is correct wrt the Mathlib spec.

```lean
theorem degreeLT_toPoly {n : ℕ} [BEq R] [LawfulBEq R] {p : CPolynomial R} :
    p ∈ degreeLT (R := R) n ↔ p.toPoly ∈ Polynomial.degreeLT R n
```

`CompPoly.CPolynomial.eval_mul` (theorem, [line 240](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L240))

> Evaluation preserves multiplication.

```lean
theorem eval_mul [CommSemiring R] [BEq R] [LawfulBEq R]
    (p q : CPolynomial R) (x : R) :
    (p * q).eval x = p.eval x * q.eval x
```

`CompPoly.CPolynomial.eval_ext` (theorem, [line 251](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L251))

> **Univariate eval-extensionality (degree-bounded).** Two `CPolynomial`s
> over an integral domain that agree on more than $d$ points of a `Finset S` are
> equal, when $d$ bounds the natural degree of their difference.
>
> The degree bound is needed over finite fields, where two distinct polynomials
> may agree on every field element.

```lean
theorem eval_ext
    [CommRing R] [DecidableEq R] [BEq R] [LawfulBEq R] [IsDomain R]
    {p q : CPolynomial R} {d : ℕ} {S : Finset R}
    (hdeg : (p - q).natDegree ≤ d)
    (hagree :
      d < (S.filter
              (fun r ↦ p.eval r = q.eval r)).card) :
    p = q
```

`CompPoly.CPolynomial.eval_sub` (theorem, [line 283](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L283))

> Evaluation preserves subtraction.

```lean
theorem eval_sub [Ring R] [BEq R] [LawfulBEq R]
    (a : R) (p q : CPolynomial R) :
    CPolynomial.eval a (p - q) = CPolynomial.eval a p - CPolynomial.eval a q
```

`CompPoly.CPolynomial.eval_one` (theorem, [line 291](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L291))

> Evaluation of the constant one computable polynomial.

```lean
theorem eval_one [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (a : R) : CPolynomial.eval a (1 : CPolynomial R) = 1
```

> ### Cast-oriented forms of the lift lemmas
>
> The lift lemmas (`eval_toPoly`, `coeff_toPoly`, …) rewrite a `CPolynomial` query into a
> Mathlib one. These are the same facts in the orientation `norm_cast` wants, with the coercion
> on the left, so that `exact_mod_cast` pulls a Mathlib statement about `↑p` back to one about
> `p`.

`CompPoly.CPolynomial.toPoly_eval` (theorem, [line 303](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L303))

```lean
theorem toPoly_eval [Semiring R] [BEq R] [LawfulBEq R] (p : CPolynomial R) (x : R) :
    (p : Polynomial R).eval x = p.eval x
```

`CompPoly.CPolynomial.toPoly_coeff` (theorem, [line 308](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L308))

```lean
theorem toPoly_coeff [Semiring R] [BEq R] [LawfulBEq R] (p : CPolynomial R) (i : ℕ) :
    (p : Polynomial R).coeff i = p.coeff i
```

`CompPoly.CPolynomial.toPoly_degree` (theorem, [line 313](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L313))

```lean
theorem toPoly_degree [Semiring R] [BEq R] [LawfulBEq R] (p : CPolynomial R) :
    (p : Polynomial R).degree = p.degree
```

`CompPoly.CPolynomial.toPoly_natDegree` (theorem, [line 318](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L318))

```lean
theorem toPoly_natDegree [Semiring R] [BEq R] [LawfulBEq R] (p : CPolynomial R) :
    (p : Polynomial R).natDegree = p.natDegree
```

`CompPoly.CPolynomial.toPoly_leadingCoeff` (theorem, [line 323](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L323))

```lean
theorem toPoly_leadingCoeff [Semiring R] [BEq R] [LawfulBEq R] (p : CPolynomial R) :
    (p : Polynomial R).leadingCoeff = p.leadingCoeff
```

`CompPoly.CPolynomial.eval_zero` (theorem, [line 329](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L329))

> Evaluation of the zero polynomial.

```lean
theorem eval_zero [Semiring R] [BEq R] [LawfulBEq R] (a : R) :
    CPolynomial.eval a (0 : CPolynomial R) = 0
```

`CompPoly.CPolynomial.eval_add` (theorem, [line 335](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L335))

> Evaluation preserves addition.

```lean
theorem eval_add [Semiring R] [BEq R] [LawfulBEq R] (a : R) (p q : CPolynomial R) :
    CPolynomial.eval a (p + q) = CPolynomial.eval a p + CPolynomial.eval a q
```

`CompPoly.CPolynomial.eval_neg` (theorem, [line 342](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L342))

> Evaluation preserves negation.

```lean
theorem eval_neg [Ring R] [BEq R] [LawfulBEq R] (a : R) (p : CPolynomial R) :
    CPolynomial.eval a (-p) = -CPolynomial.eval a p
```

`CompPoly.CPolynomial.eval_X` (theorem, [line 349](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L349))

> Evaluation of the variable.

```lean
theorem eval_X [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] (a : R) :
    CPolynomial.eval a (CPolynomial.X : CPolynomial R) = a
```

`CompPoly.CPolynomial.eval_pow` (theorem, [line 355](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L355))

> Evaluation preserves powers.

```lean
theorem eval_pow [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R] (a : R)
    (p : CPolynomial R) (n : ℕ) :
    CPolynomial.eval a (p ^ n) = CPolynomial.eval a p ^ n
```

`CompPoly.CPolynomial.eval_monomial` (theorem, [line 363](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L363))

> Evaluation of a monomial.

```lean
theorem eval_monomial [Semiring R] [BEq R] [LawfulBEq R] [DecidableEq R] (a c : R) (n : ℕ) :
    CPolynomial.eval a (CPolynomial.monomial n c) = c * a ^ n
```

`CompPoly.CPolynomial.eval_divX_eq_zero_of_ne_zero_root` (theorem, [line 368](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L368))

> Dividing by `X` preserves a nonzero root when the constant coefficient vanishes.

```lean
theorem eval_divX_eq_zero_of_ne_zero_root [Field R] [BEq R] [LawfulBEq R]
    {p : CPolynomial R} {a : R} (ha : a ≠ 0)
    (hcoeff : p.coeff 0 = 0) (hroot : CPolynomial.eval a p = 0) :
    CPolynomial.eval a (CPolynomial.divX p) = 0
```

`CompPoly.CPolynomial.divX_ne_zero_of_ne_zero_coeff_zero` (theorem, [line 388](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L388))

> If a nonzero polynomial has zero constant coefficient, its quotient by `X` is nonzero.

```lean
theorem divX_ne_zero_of_ne_zero_coeff_zero [Field R] [BEq R] [LawfulBEq R]
    {p : CPolynomial R} (hp : p ≠ 0) (hcoeff : p.coeff 0 = 0) :
    CPolynomial.divX p ≠ 0
```

`CompPoly.CPolynomial.Raw.eval_sub_C_mul_X_pow_trim_eq_self_of_eval_eq_zero` (theorem, [line 403](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L403))

```lean
theorem eval_sub_C_mul_X_pow_trim_eq_self_of_eval_eq_zero
    [Field R] [BEq R] [LawfulBEq R] (p q : CPolynomial.Raw R) (scale : R)
    (shift : ℕ) {x : R} (hq : q.eval x = 0) :
    ((p - C scale * (q * X ^ shift)).trim).eval x = p.eval x
```

`CompPoly.CPolynomial.Raw.eval_divModByMonicAux_go_snd_eq_self_of_eval_eq_zero` (theorem, [line 414](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L414))

```lean
theorem eval_divModByMonicAux_go_snd_eq_self_of_eval_eq_zero
    [Field R] [BEq R] [LawfulBEq R] :
    ∀ (fuel : ℕ) (p q : CPolynomial.Raw R) {x : R}, q.eval x = 0 →
      (divModByMonicAux.go fuel p q).2.eval x = p.eval x
```

`CompPoly.CPolynomial.Raw.eval_modByMonic_eq_self_of_eval_eq_zero` (theorem, [line 435](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L435))

> Reducing by a polynomial that vanishes at `x` preserves evaluation at `x`.

```lean
theorem eval_modByMonic_eq_self_of_eval_eq_zero
    [Field R] [BEq R] [LawfulBEq R] (p q : CPolynomial.Raw R) {x : R}
    (hq : q.eval x = 0) :
    (modByMonic p q).eval x = p.eval x
```

`CompPoly.CPolynomial.eval_modByMonic_eq_self_of_eval_eq_zero` (theorem, [line 444](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean#L444))

> Reducing by a polynomial that vanishes at `x` preserves evaluation at `x`.

```lean
theorem eval_modByMonic_eq_self_of_eval_eq_zero
    [Field R] [BEq R] [LawfulBEq R] (p q : CPolynomial R) {x : R}
    (hq : q.eval x = 0) :
    (CPolynomial.modByMonic p q).eval x = p.eval x
```

## Depends on

- [Linear Algebra API for Computable Univariate Polynomials](../../part-01/linear.md)
- [Computable Univariate To `Polynomial`](core.md)

## Proof depends on

- [`toPoly` Equivalence](equiv.md)

## Sources

- [CompPoly/Univariate/ToPoly/Impl.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/Impl.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.ToPoly.Impl.json)
