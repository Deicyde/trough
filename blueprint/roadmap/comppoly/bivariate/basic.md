---
catalog: module
lean: CompPoly.CBivariate, CompPoly.CBivariate.ext, CompPoly.CBivariate.CC, CompPoly.CBivariate.X, CompPoly.CBivariate.Y, CompPoly.CBivariate.monomialXY, CompPoly.CBivariate.coeff, CompPoly.CBivariate.supportY, CompPoly.CBivariate.supportX, CompPoly.CBivariate.natDegreeY, CompPoly.CBivariate.natDegreeX, CompPoly.CBivariate.totalDegree, CompPoly.CBivariate.natWeightedDegree, CompPoly.CBivariate.evalX, CompPoly.CBivariate.evalY, CompPoly.CBivariate.evalYHorner, CompPoly.CBivariate.evalEval, CompPoly.CBivariate.evalEvalHornerYThenX, CompPoly.CBivariate.evalEvalHornerXThenY, CompPoly.CBivariate.swap, CompPoly.CBivariate.leadingCoeffY, CompPoly.CBivariate.leadingCoeffX, CompPoly.CBivariate.coeff_eq_coeff_coeff, CompPoly.CBivariate.coeff_add, CompPoly.CBivariate.coeff_finset_sum, CompPoly.CBivariate.coeff_monomialXY, CompPoly.CBivariate.coeff_monomialY, CompPoly.CBivariate.eq_iff_coeff, CompPoly.CBivariate.totalDegree_eq_natWeightedDegree, CompPoly.CBivariate.natDegreeX_eq_natWeightedDegree, CompPoly.CBivariate.natDegreeY_eq_natWeightedDegree, CompPoly.CBivariate.natWeightedDegree_monomialXY, CompPoly.CBivariate.natWeightedDegree_zero, CompPoly.CBivariate.natWeightedDegree_le_iff, CompPoly.CBivariate.natWeightedDegree_le_iff_coeff, CompPoly.CBivariate.natWeightedDegree_CC, CompPoly.CBivariate.natWeightedDegree_add_le
statement: formalized
proof: formalized
---

# Computable Bivariate Polynomials

`CompPoly.Bivariate.Basic`, in [CompPoly/Bivariate/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean), by Derek Sorensen, Dimitris Mitsios.

> This file defines `CBivariate R`, the computable representation of bivariate polynomials with
> coefficients in `R`. The type is `CPolynomial (CPolynomial R)`, i.e. polynomials in `Y` with
> coefficients that are polynomials in `X`, matching Mathlib's `R[X][Y]`
> (i.e. `Polynomial (Polynomial R)`).
>
> The design is intended to be compatible with:
> - Mathlib's `Polynomial.Bivariate` (see `CompPoly/Bivariate/ToPoly.lean`)
> - ArkLib's `Polynomial.Bivariate` interface (see ArkLib/Data/Polynomial/Bivariate.lean and
>   ArkLib/Data/CodingTheory/PolishchukSpielman/Degrees.lean, BCIKS20.lean, etc.)

`CompPoly.CBivariate` (definition, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L35))

> Computable bivariate polynomials: `F[X][Y]` as `CPolynomial (CPolynomial R)`.
>
> Each `p : CBivariate R` is a polynomial in `Y` whose coefficients are univariate polynomials
> in `X`. The outer structure is indexed by powers of `Y`, the inner by powers of `X`.

```lean
def CBivariate (R : Type*) [Zero R]
```

`CompPoly.CBivariate.ext` (theorem, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L45))

> Extensionality: two bivariate polynomials are equal if their underlying values are.

```lean
theorem ext {p q : CBivariate R} (h : p.val = q.val) : p = q
```

`CompPoly.CBivariate.CC` (definition, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L123))

> Constant as a bivariate polynomial. Mathlib: `Polynomial.Bivariate.CC`.

```lean
def CC {R : Type*} [Zero R] [BEq R] [LawfulBEq R] (r : R) : CBivariate R
```

`CompPoly.CBivariate.X` (definition, [line 127](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L127))

> The variable X (inner variable). As bivariate: polynomial in Y with single coeff `X` at Y^0.

```lean
def X {R : Type*} [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] : CBivariate R
```

`CompPoly.CBivariate.Y` (definition, [line 131](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L131))

> The variable Y (outer variable). Monomial `Y^1` with coefficient 1.

```lean
def Y {R : Type*} [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R] :
    CBivariate R
```

`CompPoly.CBivariate.monomialXY` (definition, [line 136](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L136))

> Monomial `c * X^n * Y^m`. ArkLib: `Polynomial.Bivariate.monomialXY`.

```lean
def monomialXY {R : Type*} [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (n m : ℕ) (c : R) : CBivariate R
```

`CompPoly.CBivariate.coeff` (definition, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L142))

> Coefficient of `X^i Y^j` in the bivariate polynomial. Here `i` is the X-exponent (inner)
> and `j` is the Y-exponent (outer). ArkLib: `Polynomial.Bivariate.coeff f i j`.

```lean
def coeff {R : Type*} [Zero R] (f : CBivariate R) (i j : ℕ) : R
```

`CompPoly.CBivariate.supportY` (definition, [line 146](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L146))

> The Y-support: indices j such that the coefficient of Y^j is nonzero.

```lean
def supportY {R : Type*} [Zero R] [BEq R] (f : CBivariate R) : Finset ℕ
```

`CompPoly.CBivariate.supportX` (definition, [line 150](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L150))

> The X-support: indices i such that the coefficient of X^i is nonzero
> (i.e. some monomial X^i Y^j has nonzero coefficient).

```lean
def supportX {R : Type*} [Zero R] [BEq R] (f : CBivariate R) : Finset ℕ
```

`CompPoly.CBivariate.natDegreeY` (definition, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L155))

> The `Y`-degree (degree when viewed as a polynomial in `Y`).
> ArkLib: `Polynomial.Bivariate.natDegreeY`.

```lean
def natDegreeY {R : Type*} [Zero R] (f : CBivariate R) : ℕ
```

`CompPoly.CBivariate.natDegreeX` (definition, [line 160](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L160))

> The `X`-degree: maximum over all Y-coefficients of their degree in X.
> ArkLib: `Polynomial.Bivariate.natDegreeX`.

```lean
def natDegreeX {R : Type*} [Zero R] [BEq R] (f : CBivariate R) : ℕ
```

`CompPoly.CBivariate.totalDegree` (definition, [line 165](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L165))

> Total degree: max over monomials of (deg_X + deg_Y).
> ArkLib: `Polynomial.Bivariate.totalDegree`.

```lean
def totalDegree {R : Type*} [Zero R] [BEq R] (f : CBivariate R) : ℕ
```

`CompPoly.CBivariate.natWeightedDegree` (definition, [line 169](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L169))

> The `(u, v)`-weighted degree: max over monomials of `u * deg_X + v * deg_Y`.

```lean
def natWeightedDegree {R : Type*} [Zero R] [BEq R] (f : CBivariate R) (u v : ℕ) : ℕ
```

`CompPoly.CBivariate.evalX` (definition, [line 174](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L174))

> Evaluate in the first variable (X) at `a`, yielding a univariate polynomial in Y.
> ArkLib: `Polynomial.Bivariate.evalX`.

```lean
def evalX {R : Type*} [Semiring R] [BEq R] [LawfulBEq R] [DecidableEq R]
    (a : R) (f : CBivariate R) : CPolynomial R
```

`CompPoly.CBivariate.evalY` (definition, [line 184](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L184))

> Evaluate in the second variable (Y) at `a`, yielding a univariate polynomial in X.
> ArkLib: `Polynomial.Bivariate.evalY`.
>
> Folds the Y-coefficients of `f` with a raw Horner pattern (`smulRight a` then
> `addRaw`), trimming once at the end. This avoids paying one `CPolynomial.mul`
> and one `CPolynomial.add` trim per Y-coefficient.

```lean
def evalY {R : Type*} [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (a : R) (f : CBivariate R) : CPolynomial R
```

`CompPoly.CBivariate.evalYHorner` (definition, [line 194](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L194))

> Evaluate in the second variable (Y) at `a` using Horner's method,
> yielding a univariate polynomial in X.

```lean
def evalYHorner {R : Type*} [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (a : R) (p : CBivariate R) : CPolynomial R
```

`CompPoly.CBivariate.evalEval` (definition, [line 203](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L203))

> Full evaluation at `(x, y)`: `p(x, y)`. Inner variable X at `x`, outer variable Y at `y`.
> Equivalently `(evalY y f).eval x`. Mathlib: `Polynomial.evalEval`.
>
> See `CBivariate.eval_y_horner_eq_eval_y` in `CompPoly/Bivariate/ToPoly.lean` for
> agreement between `evalY` and `evalYHorner`.

```lean
def evalEval {R : Type*} [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (x y : R) (f : CBivariate R) : R
```

`CompPoly.CBivariate.evalEvalHornerYThenX` (definition, [line 209](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L209))

> Full evaluation at `(x, y)` using Horner in Y, then Horner in X on the
> intermediate univariate polynomial.

```lean
def evalEvalHornerYThenX {R : Type*} [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (x y : R) (p : CBivariate R) : R
```

`CompPoly.CBivariate.evalEvalHornerXThenY` (definition, [line 215](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L215))

> Full evaluation at `(x, y)` by evaluating each X-coefficient polynomial at
> `x`, then Horner-evaluating the resulting scalar polynomial in Y.

```lean
def evalEvalHornerXThenY {R : Type*} [Semiring R] (x y : R) (p : CBivariate R) : R
```

`CompPoly.CBivariate.swap` (definition, [line 222](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L222))

> Swap the roles of X and Y.
> ArkLib/Mathlib: `Polynomial.Bivariate.swap`.
> …

```lean
def swap {R : Type*} [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (f : CBivariate R) : CBivariate R
```

`CompPoly.CBivariate.leadingCoeffY` (definition, [line 230](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L230))

> Leading coefficient when viewed as a polynomial in Y.
> ArkLib: `Polynomial.Bivariate.leadingCoeffY`.

```lean
def leadingCoeffY {R : Type*} [Zero R] (f : CBivariate R) : CPolynomial R
```

`CompPoly.CBivariate.leadingCoeffX` (definition, [line 235](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L235))

> Leading coefficient when viewed as a polynomial in X.
> The coefficient of X^(degreeX f): a polynomial in Y.

```lean
def leadingCoeffX {R : Type*} [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (f : CBivariate R) : CPolynomial R
```

`CompPoly.CBivariate.coeff_eq_coeff_coeff` (theorem, [line 247](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L247))

> `CBivariate.coeff` as two composed `CPolynomial.coeff`.

```lean
theorem coeff_eq_coeff_coeff [Zero R] (f : CBivariate R) (i j : ℕ) :
    coeff f i j = CPolynomial.coeff (CPolynomial.coeff f j) i
```

`CompPoly.CBivariate.coeff_add` (theorem, [line 252](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L252))

> Bivariate coefficients are additive.

```lean
theorem coeff_add [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (p q : CBivariate R) (i j : ℕ) :
    coeff (p + q) i j = coeff p i j + coeff q i j
```

`CompPoly.CBivariate.coeff_finset_sum` (theorem, [line 260](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L260))

> Bivariate coefficients distribute over finite sums.

```lean
theorem coeff_finset_sum [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    {ι : Type*} [DecidableEq ι] (s : Finset ι) (f : ι → CBivariate R) (i j : ℕ) :
    coeff (s.sum f) i j = s.sum (fun t => coeff (f t) i j)
```

`CompPoly.CBivariate.coeff_monomialXY` (theorem, [line 273](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L273))

> Coefficient of a bivariate monomial `c * X^a * Y^b`.

```lean
theorem coeff_monomialXY [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a b : ℕ) (c : R) (i j : ℕ) :
    coeff (monomialXY a b c) i j = if i = a ∧ j = b then c else 0
```

`CompPoly.CBivariate.coeff_monomialY` (theorem, [line 287](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L287))

> Coefficient of `Y^m * c(X)` as a bivariate polynomial.

```lean
theorem coeff_monomialY [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (m : ℕ) (c : CPolynomial R) (i j : ℕ) :
    coeff (CPolynomial.monomial m c) i j = if j = m then CPolynomial.coeff c i else 0
```

`CompPoly.CBivariate.eq_iff_coeff` (theorem, [line 296](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L296))

> Two bivariate polynomials are equal iff all their coefficients agree.

```lean
theorem eq_iff_coeff [Zero R] [BEq R] [LawfulBEq R] {p q : CBivariate R} :
    p = q ↔ ∀ i j, coeff p i j = coeff q i j
```

`CompPoly.CBivariate.totalDegree_eq_natWeightedDegree` (theorem, [line 314](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L314))

> The total degree is the `(1, 1)`-weighted degree.

```lean
theorem totalDegree_eq_natWeightedDegree (f : CBivariate R) :
    CBivariate.totalDegree (R := R) f = CBivariate.natWeightedDegree (R := R) f 1 1
```

`CompPoly.CBivariate.natDegreeX_eq_natWeightedDegree` (theorem, [line 320](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L320))

> The X-degree is the `(1, 0)`-weighted degree.

```lean
theorem natDegreeX_eq_natWeightedDegree (f : CBivariate R) :
    CBivariate.natDegreeX (R := R) f = CBivariate.natWeightedDegree (R := R) f 1 0
```

`CompPoly.CBivariate.natDegreeY_eq_natWeightedDegree` (theorem, [line 326](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L326))

> The Y-degree is the `(0, 1)`-weighted degree.

```lean
theorem natDegreeY_eq_natWeightedDegree (f : CBivariate R) :
    CBivariate.natDegreeY (R := R) f = CBivariate.natWeightedDegree (R := R) f 0 1
```

`CompPoly.CBivariate.natWeightedDegree_monomialXY` (theorem, [line 333](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L333))

> The weighted degree of a nonzero monomial `c * X^n * Y^m`
> is `u * n + v * m` where `u` is the weight of `X` and `v` the weight of `Y`.

```lean
theorem natWeightedDegree_monomialXY [DecidableEq R]
    {n m : ℕ} {c : R} (hc : c ≠ 0) (u v : ℕ) :
    CBivariate.natWeightedDegree
      (CBivariate.monomialXY n m c) u v
      = u * n + v * m
```

`CompPoly.CBivariate.natWeightedDegree_zero` (theorem, [line 350](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L350))

> The weighted degree of the zero polynomial is zero.

```lean
theorem natWeightedDegree_zero (u v : ℕ) :
    CBivariate.natWeightedDegree (0 : CBivariate R) u v = 0
```

`CompPoly.CBivariate.natWeightedDegree_le_iff` (theorem, [line 360](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L360))

> The weighted degree is at most `d` iff every Y-support index
> satisfies the weighted bound.

```lean
theorem natWeightedDegree_le_iff (f : CBivariate R) (u v d : ℕ) :
    natWeightedDegree f u v ≤ d ↔
    ∀ j ∈ f.supportY , u * (f.val.coeff j).natDegree + v * j ≤ d
```

`CompPoly.CBivariate.natWeightedDegree_le_iff_coeff` (theorem, [line 368](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L368))

> The weighted degree is at most `d` iff every monomial index
> satisfies the weighted bound.

```lean
theorem natWeightedDegree_le_iff_coeff (f : CBivariate R) (u v d : ℕ) :
    f.natWeightedDegree u v ≤ d ↔
    ∀ i j, CBivariate.coeff f i j ≠ 0 → u * i + v * j ≤ d
```

`CompPoly.CBivariate.natWeightedDegree_CC` (theorem, [line 393](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L393))

> The natWeightedDegree of a constant bivariate polynomial `CBivariate.CC` is zero.

```lean
theorem natWeightedDegree_CC {r : R} (u v : ℕ) :
    CBivariate.natWeightedDegree (CBivariate.CC r) u v = 0
```

`CompPoly.CBivariate.natWeightedDegree_add_le` (theorem, [line 406](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean#L406))

> The weighted degree of a sum is at most the max of the weighted degrees.

```lean
theorem natWeightedDegree_add_le [DecidableEq R] (p q : CBivariate R) (u v : ℕ) :
    CBivariate.natWeightedDegree (p + q) u v ≤
      max (CBivariate.natWeightedDegree p u v) (CBivariate.natWeightedDegree q u v)
```

## Depends on

- [Computable Univariate Polynomials](../univariate/part-01/basic.md)

## Sources

- [CompPoly/Bivariate/Basic.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/Basic.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Bivariate.Basic.json)
