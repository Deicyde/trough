---
catalog: module
lean: CompPoly.CBivariate.toPoly, CompPoly.CBivariate.ofPoly, CompPoly.CBivariate.toPoly_add, CompPoly.CBivariate.toPoly_monomial, CompPoly.CBivariate.ofPoly_monomial, CompPoly.CBivariate.toImpl_add, CompPoly.CBivariate.ofPoly_add, CompPoly.CBivariate.ofPoly_coeff, CompPoly.CBivariate.toPoly_coeff, CompPoly.CBivariate.toPoly_eq_map, CompPoly.CBivariate.toPoly_mul, CompPoly.CBivariate.ofPoly_toPoly, CompPoly.CBivariate.toPoly_ofPoly, CompPoly.CBivariate.ringEquiv, CompPoly.CBivariate.toPoly_one, CompPoly.CBivariate.ofPoly_one, CompPoly.CBivariate.toPoly_zero, CompPoly.CBivariate.ofPoly_zero, CompPoly.CBivariate.toPolyRingHom, CompPoly.CBivariate.ofPolyRingHom, CompPoly.CBivariate.ofPoly_mul, CompPoly.CBivariate.evalY_toPoly, CompPoly.CBivariate.eval_y_horner_eq_eval_y, CompPoly.CBivariate.eval_eval_horner_y_then_x_eq_eval_eval, CompPoly.CBivariate.evalEval_toPoly, CompPoly.CBivariate.coeff_toPoly, CompPoly.CBivariate.support_toPoly_outer, CompPoly.CBivariate.natDegreeY_toPoly, CompPoly.CBivariate.coeff_toPoly_Y, CompPoly.CBivariate.natDegreeX_toPoly, CompPoly.CBivariate.CC_toPoly, CompPoly.CBivariate.X_toPoly, CompPoly.CBivariate.Y_toPoly, CompPoly.CBivariate.monomialXY_toPoly, CompPoly.CBivariate.supportX_toPoly, CompPoly.CBivariate.totalDegree_toPoly, CompPoly.CBivariate.evalX_toPoly_coeff, CompPoly.CBivariate.evalX_toPoly_eval_commute, CompPoly.CBivariate.evalX_toPoly_eval, CompPoly.CBivariate.eval_eval_horner_x_then_y_eq_eval_eval, CompPoly.CBivariate.evalX_toPoly_eval_commute_converse, CompPoly.CBivariate.eval_comm, CompPoly.CBivariate.leadingCoeffY_toPoly, CompPoly.CBivariate.swap_toPoly_coeff, CompPoly.CBivariate.leadingCoeffX_toPoly
statement: formalized
proof: formalized
---

# Equivalence with Mathlib Bivariate Polynomials

`CompPoly.Bivariate.ToPoly`, in [CompPoly/Bivariate/ToPoly.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean), by Derek Sorensen.

> This file establishes the conversion from `CBivariate R` to Mathlib's `R[X][Y]`
> (`Polynomial (Polynomial R)`).
>
> Main definitions:
> - `toPoly`: converts `CBivariate R` to `R[X][Y]`
> - `ofPoly`: converts `R[X][Y]` back to `CBivariate R`
>
> Main results:
> - round-trip identities: `ofPoly_toPoly`, `toPoly_ofPoly`
> - ring equivalence: `ringEquiv`
> - API correctness lemmas for evaluation, coefficients, support, and degrees

> Core conversion lemmas between `CBivariate R` and `R[X][Y]`.

`CompPoly.CBivariate.toPoly` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L46))

> Convert `CBivariate R` to Mathlib's bivariate polynomial `R[X][Y]`.
>
> Maps each Y-coefficient through `CPolynomial.toPoly`, then builds
> `Polynomial (Polynomial R)` as the sum of monomials.

```lean
noncomputable def toPoly {R : Type*} [BEq R] [LawfulBEq R] [Semiring R]
    (p : CBivariate R) : R[X][Y]
```

`CompPoly.CBivariate.ofPoly` (definition, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L56))

> Convert Mathlib's `R[X][Y]` to `CBivariate R` (inverse of `toPoly`).
>
> Extracts each Y-coefficient via `p.coeff`, converts to `CPolynomial R` via
> `toImpl` and trimming, then builds the canonical bivariate sum.

```lean
def ofPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    [DecidableEq R] [Semiring (Polynomial R)] (p : R[X][Y]) : CBivariate R
```

`CompPoly.CBivariate.toPoly_add` (lemma, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L64))

> `toPoly` preserves addition.

```lean
lemma toPoly_add {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    (p q : CBivariate R) : toPoly (p + q) = toPoly p + toPoly q
```

`CompPoly.CBivariate.toPoly_monomial` (lemma, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L100))

> `toPoly` sends a Y-monomial to the corresponding monomial in `R[X][Y]`.

```lean
lemma toPoly_monomial {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    [DecidableEq R]
    (n : ℕ) (c : CPolynomial R) :
    toPoly (CPolynomial.monomial n c) = monomial n (c.toPoly)
```

`CompPoly.CBivariate.ofPoly_monomial` (lemma, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L114))

> `ofPoly` sends a Y-monomial in `R[X][Y]` to a bivariate monomial.

```lean
lemma ofPoly_monomial {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    [DecidableEq R]
    (n : ℕ) (c : R[X]) :
    ofPoly (monomial n c) =
    CPolynomial.monomial n ⟨c.toImpl, CPolynomial.Raw.isCanonical_toImpl c⟩
```

`CompPoly.CBivariate.toImpl_add` (lemma, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L128))

> `Polynomial.toImpl` preserves addition, accounting for trimming in the raw representation.

```lean
lemma toImpl_add {R : Type*} [BEq R] [LawfulBEq R] [Semiring R] (p q : R[X]) :
    p.toImpl + q.toImpl = (p + q).toImpl
```

`CompPoly.CBivariate.ofPoly_add` (lemma, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L155))

> `ofPoly` preserves addition in `R[X][Y]`.

```lean
lemma ofPoly_add {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    [DecidableEq R]
    (p q : R[X][Y]) : ofPoly (p + q) = ofPoly p + ofPoly q
```

`CompPoly.CBivariate.ofPoly_coeff` (theorem, [line 184](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L184))

> The outer coefficient of `ofPoly p` converts back to the corresponding `R[X]` coefficient.

```lean
theorem ofPoly_coeff {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    [DecidableEq R]
    (p : R[X][Y]) (n : ℕ) : (CPolynomial.coeff (ofPoly p) n).toPoly = p.coeff n
```

`CompPoly.CBivariate.toPoly_coeff` (theorem, [line 209](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L209))

> The outer coefficient of `toPoly p` is `CPolynomial.coeff p n` converted to `R[X]`.

```lean
theorem toPoly_coeff {R : Type*} [BEq R] [LawfulBEq R] [Semiring R]
    (p : CBivariate R) (n : ℕ) : (toPoly p).coeff n = (CPolynomial.coeff p n).toPoly
```

`CompPoly.CBivariate.toPoly_eq_map` (theorem, [line 218](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L218))

> `toPoly` is the map of the outer polynomial via `CPolynomial.ringEquiv`.

```lean
theorem toPoly_eq_map {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    (p : CBivariate R) :
    toPoly p = (CPolynomial.toPoly p).map (CPolynomial.ringEquiv (R := R))
```

`CompPoly.CBivariate.toPoly_mul` (theorem, [line 234](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L234))

> `toPoly` preserves multiplication.

```lean
theorem toPoly_mul {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    (p q : CBivariate R) :
    toPoly (p * q) = toPoly p * toPoly q
```

> Ring equivalence between bivariate representations.

`CompPoly.CBivariate.ofPoly_toPoly` (theorem, [line 250](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L250))

> Round-trip from Mathlib: converting a polynomial to `CBivariate` and back is the identity.

```lean
theorem ofPoly_toPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    [DecidableEq R]
    (p : R[X][Y]) : toPoly (ofPoly p) = p
```

`CompPoly.CBivariate.toPoly_ofPoly` (theorem, [line 262](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L262))

> Round-trip from `CBivariate`: converting to Mathlib and back is the identity.

```lean
theorem toPoly_ofPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    [DecidableEq R]
    (p : CBivariate R) : ofPoly (toPoly p) = p
```

`CompPoly.CBivariate.ringEquiv` (definition, [line 278](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L278))

> Ring equivalence between `CBivariate R` and Mathlib's `R[X][Y]`.

```lean
noncomputable def ringEquiv
    {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R] [DecidableEq R] :
    CBivariate R ≃+* R[X][Y]
```

`CompPoly.CBivariate.toPoly_one` (theorem, [line 290](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L290))

> `toPoly` preserves `1`.

```lean
theorem toPoly_one
    {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R] [DecidableEq R] :
    toPoly (1 : CBivariate R) = 1
```

`CompPoly.CBivariate.ofPoly_one` (theorem, [line 296](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L296))

> `ofPoly` preserves `1`.

```lean
theorem ofPoly_one
    {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R] [DecidableEq R] :
    ofPoly (1 : R[X][Y]) = 1
```

`CompPoly.CBivariate.toPoly_zero` (lemma, [line 305](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L305))

> `toPoly` maps the zero bivariate polynomial to `0`.

```lean
lemma toPoly_zero {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R] :
    toPoly (0 : CBivariate R) = 0
```

`CompPoly.CBivariate.ofPoly_zero` (lemma, [line 313](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L313))

> `ofPoly` maps `0` in `R[X][Y]` to the zero bivariate polynomial.

```lean
lemma ofPoly_zero {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R] [DecidableEq R] :
    ofPoly (0 : R[X][Y]) = 0
```

`CompPoly.CBivariate.toPolyRingHom` (definition, [line 319](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L319))

> Ring hom from computable bivariates to Mathlib bivariates.

```lean
noncomputable def toPolyRingHom
    {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R] [DecidableEq R] :
    CBivariate R →+* R[X][Y]
```

`CompPoly.CBivariate.ofPolyRingHom` (definition, [line 325](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L325))

> Ring hom from Mathlib bivariates to computable bivariates.

```lean
noncomputable def ofPolyRingHom
    {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R] [DecidableEq R] :
    R[X][Y] →+* CBivariate R
```

`CompPoly.CBivariate.ofPoly_mul` (theorem, [line 331](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L331))

> `ofPoly` preserves multiplication.

```lean
theorem ofPoly_mul
    {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R] [DecidableEq R]
    (p q : R[X][Y]) :
    ofPoly (p * q) = ofPoly p * ofPoly q
```

> ### Shared helper: deferred-trim Horner foldr commutes with `toPoly`
>
> `evalY` and (transitively) `evalEval` fold the Y-coefficients of `f : CBivariate R`
> with a raw Horner pattern (`smulRight a` then `addRaw`) and trim once at the end.
> The helper below bridges that raw fold's `toPoly` image with the `Finset.sum` form
> of the polynomial evaluation.

> Correctness lemmas for evaluation, coefficients, support, and degrees.

`CompPoly.CBivariate.evalY_toPoly` (theorem, [line 372](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L372))

> `evalY a` corresponds to outer evaluation at `Polynomial.C a`.

```lean
theorem evalY_toPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    (a : R) (f : CBivariate R) :
    (evalY (R := R) a f).toPoly = (toPoly f).eval (Polynomial.C a)
```

`CompPoly.CBivariate.eval_y_horner_eq_eval_y` (theorem, [line 391](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L391))

> Horner evaluation in Y agrees with the deferred-trim sum-of-powers evaluator.
>
> Both `evalYHorner` and the new `evalY` reduce to the same `Polynomial` under
> `toPoly`, and `toPoly` is injective on canonical polynomials, so the two
> canonical results coincide.

```lean
theorem eval_y_horner_eq_eval_y {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] (a : R) (p : CBivariate R) :
    evalYHorner a p = evalY a p
```

`CompPoly.CBivariate.eval_eval_horner_y_then_x_eq_eval_eval` (theorem, [line 415](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L415))

> `Y`-then-`X` Horner full evaluation agrees with the existing evaluator.

```lean
theorem eval_eval_horner_y_then_x_eq_eval_eval {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (x y : R) (p : CBivariate R) :
    evalEvalHornerYThenX x y p = evalEval x y p
```

`CompPoly.CBivariate.evalEval_toPoly` (theorem, [line 423](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L423))

> `toPoly` preserves full evaluation: `evalEval x y f = (toPoly f).evalEval x y`.

```lean
theorem evalEval_toPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    (x y : R) (f : CBivariate R) :
    @CBivariate.evalEval R _ _ _ _ x y f = (toPoly f).evalEval x y
```

`CompPoly.CBivariate.coeff_toPoly` (theorem, [line 430](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L430))

> `toPoly` preserves coefficients: coefficient of `X^i Y^j` matches.

```lean
theorem coeff_toPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    (f : CBivariate R) (i j : ℕ) :
    ((toPoly f).coeff j).coeff i = CBivariate.coeff (R := R) f i j
```

`CompPoly.CBivariate.support_toPoly_outer` (theorem, [line 438](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L438))

> The outer support of `toPoly f` equals the Y-support of `f`.

```lean
theorem support_toPoly_outer {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    (f : CBivariate R) : (toPoly f).support = f.supportY
```

`CompPoly.CBivariate.natDegreeY_toPoly` (theorem, [line 448](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L448))

> `toPoly` preserves Y-degree.

```lean
theorem natDegreeY_toPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    (f : CBivariate R) : (toPoly f).natDegree = f.natDegreeY
```

`CompPoly.CBivariate.coeff_toPoly_Y` (theorem, [line 463](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L463))

> The outer `Y`-coefficient formula used for X-degree transport.

```lean
theorem coeff_toPoly_Y {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    (f : CBivariate R) (j : ℕ) :
    (toPoly f).coeff j = CPolynomial.toPoly (f.val.coeff j)
```

`CompPoly.CBivariate.natDegreeX_toPoly` (theorem, [line 473](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L473))

> `toPoly` preserves X-degree (max over Y-coefficients of their degree in X).

```lean
theorem natDegreeX_toPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    (f : CBivariate R) :
    (toPoly f).support.sup (fun j ↦ ((toPoly f).coeff j).natDegree) = f.natDegreeX
```

`CompPoly.CBivariate.CC_toPoly` (theorem, [line 486](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L486))

> `CC` corresponds to the nested constant polynomial in `R[X][Y]`.

```lean
theorem CC_toPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R] (r : R) :
    toPoly (CC (R := R) r) = Polynomial.C (Polynomial.C r)
```

`CompPoly.CBivariate.X_toPoly` (theorem, [line 496](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L496))

> `X` (inner variable) corresponds to `Polynomial.C Polynomial.X` in `R[X][Y]`.

```lean
theorem X_toPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R] :
    toPoly (X (R := R)) = Polynomial.C Polynomial.X
```

`CompPoly.CBivariate.Y_toPoly` (theorem, [line 505](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L505))

> `Y` (outer variable) corresponds to `Polynomial.X` in `R[X][Y]`.

```lean
theorem Y_toPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R] [DecidableEq R] :
    toPoly (CBivariate.Y (R := R)) = (Polynomial.X : Polynomial (Polynomial R))
```

`CompPoly.CBivariate.monomialXY_toPoly` (theorem, [line 514](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L514))

> `monomialXY n m c` corresponds to `Y^m` with inner coefficient `X^n * c`.

```lean
theorem monomialXY_toPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    [DecidableEq R] (n m : ℕ) (c : R) :
    toPoly (monomialXY (R := R) n m c) = Polynomial.monomial m (Polynomial.monomial n c)
```

`CompPoly.CBivariate.supportX_toPoly` (theorem, [line 525](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L525))

> `supportX` corresponds to the union of inner supports of outer coefficients.

```lean
theorem supportX_toPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    (f : CBivariate R) :
    CBivariate.supportX (R := R) f =
      (toPoly f).support.biUnion (fun j ↦ ((toPoly f).coeff j).support)
```

`CompPoly.CBivariate.totalDegree_toPoly` (theorem, [line 538](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L538))

> `totalDegree` corresponds to the supremum over `j` of `natDegree ((toPoly f).coeff j) + j`.

```lean
theorem totalDegree_toPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    (f : CBivariate R) :
    CBivariate.totalDegree (R := R) f =
      (toPoly f).support.sup (fun j ↦ ((toPoly f).coeff j).natDegree + j)
```

`CompPoly.CBivariate.evalX_toPoly_coeff` (theorem, [line 552](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L552))

> `evalX a` evaluates each inner coefficient at `a`.

```lean
theorem evalX_toPoly_coeff {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    [DecidableEq R] (a : R) (f : CBivariate R) (j : ℕ) :
    ((evalX (R := R) a f).toPoly).coeff j = ((toPoly f).coeff j).eval a
```

`CompPoly.CBivariate.evalX_toPoly_eval_commute` (theorem, [line 579](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L579))

> `evalX` is compatible with full bivariate evaluation when `a` and `y` commute.

```lean
theorem evalX_toPoly_eval_commute {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    [DecidableEq R] (a y : R) (hc : Commute a y) (f : CBivariate R) :
    (evalX (R := R) a f).eval y = (toPoly f).evalEval a y
```

`CompPoly.CBivariate.evalX_toPoly_eval` (theorem, [line 619](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L619))

> `evalX_toPoly_eval_commute` specialized to commutative rings.

```lean
theorem evalX_toPoly_eval {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [CommSemiring R]
    [DecidableEq R] (a y : R) (f : CBivariate R) :
    (evalX (R := R) a f).eval y = (toPoly f).evalEval a y
```

`CompPoly.CBivariate.eval_eval_horner_x_then_y_eq_eval_eval` (theorem, [line 627](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L627))

> `X`-then-`Y` Horner full evaluation agrees with the existing evaluator over
> commutative coefficient semirings.

```lean
theorem eval_eval_horner_x_then_y_eq_eval_eval {R : Type*}
    [BEq R] [LawfulBEq R] [Nontrivial R] [CommSemiring R] [DecidableEq R]
    (x y : R) (p : CBivariate R) :
    evalEvalHornerXThenY x y p = evalEval x y p
```

`CompPoly.CBivariate.evalX_toPoly_eval_commute_converse` (theorem, [line 666](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L666))

> The `Commute` hypothesis in `evalX_toPoly_eval_commute` is necessary:
> if the identity holds for every bivariate polynomial then `a` and `y` commute.

```lean
theorem evalX_toPoly_eval_commute_converse
    {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R] [DecidableEq R]
    (a y : R)
    (h : ∀ f : CBivariate R,
      (evalX (R := R) a f).eval y = (toPoly f).evalEval a y) :
    Commute a y
```

`CompPoly.CBivariate.eval_comm` (theorem, [line 696](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L696))

> Computable analogue of `Polynomial.map_evalRingHom_eval`:
> evaluating `Y` at `a` and then `X` at `x` agrees with first applying the
> `X = x` evaluation through the inner coefficients and then evaluating `Y`
> at `a`.

```lean
theorem eval_comm {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [CommSemiring R]
    [DecidableEq R] (a x : R) (f : CBivariate R) :
    (evalY (R := R) a f).eval x = (evalX (R := R) x f).eval a
```

`CompPoly.CBivariate.leadingCoeffY_toPoly` (theorem, [line 704](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L704))

> `leadingCoeffY` corresponds to the leading coefficient in the outer variable.

```lean
theorem leadingCoeffY_toPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    (f : CBivariate R) :
    (leadingCoeffY (R := R) f).toPoly = (toPoly f).leadingCoeff
```

`CompPoly.CBivariate.swap_toPoly_coeff` (theorem, [line 720](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L720))

> `swap` exchanges X- and Y-exponents.

```lean
theorem swap_toPoly_coeff {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    [DecidableEq R] (f : CBivariate R) (i j : ℕ) :
    ((toPoly (swap (R := R) f)).coeff j).coeff i = ((toPoly f).coeff i).coeff j
```

`CompPoly.CBivariate.leadingCoeffX_toPoly` (theorem, [line 827](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean#L827))

> `leadingCoeffX` is the Y-leading coefficient of the swapped polynomial.

```lean
theorem leadingCoeffX_toPoly {R : Type*} [BEq R] [LawfulBEq R] [Nontrivial R] [Semiring R]
    [DecidableEq R] (f : CBivariate R) :
    (leadingCoeffX (R := R) f).toPoly = (toPoly (swap (R := R) f)).leadingCoeff
```

## Depends on

- [Computable Bivariate Polynomials](basic.md)
- [`toPoly` Equivalence](../univariate/part-02/topoly/equiv.md)

## Proof depends on

- [Proofs of Correctness for CPolynomial Operations, wrt Mathlib Specs](../univariate/part-02/topoly/impl.md)

## Sources

- [CompPoly/Bivariate/ToPoly.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/ToPoly.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Bivariate.ToPoly.json)
