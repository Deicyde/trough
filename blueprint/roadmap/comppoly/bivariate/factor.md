---
catalog: module
lean: CompPoly.CBivariate.evalYPoly, CompPoly.CBivariate.isLinearYFactor, CompPoly.CBivariate.evalYPoly_zero, CompPoly.CBivariate.evalYPoly_add, CompPoly.CBivariate.isLinearYFactor_iff, CompPoly.CBivariate.evalYPoly_toPoly, CompPoly.CBivariate.divByLinearY, CompPoly.CBivariate.divByLinearY_const, CompPoly.CBivariate.divByLinearY_zero, CompPoly.CBivariate.divByLinearY_spec, CompPoly.CBivariate.divByLinearY_rem_eq_eval, CompPoly.CBivariate.divByLinearY_exact
statement: formalized
proof: formalized
---

# Factorisation of Computable Bivariate Polynomials

`CompPoly.Bivariate.Factor`, in [CompPoly/Bivariate/Factor.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Factor.lean), by Dimitris Mitsios.

> Defines `evalYPoly` (substitute `Y ↦ f(X)`), `isLinearYFactor` (test
> divisibility by `Y - f(X)`), and `divByLinearY` (synthetic division of a
> bivariate polynomial by the monic linear factor `Y - f(X)`).
>
> `divByLinearY` is the computable factor theorem for the nested representation
> `CBivariate R = CPolynomial (CPolynomial R)`: given a root `f(X)`, it deflates
> `Q` by `Y - f(X)` over an arbitrary commutative ring. It is
> the degree-one special case of monic Euclidean division; division by an
> arbitrary monic divisor in `Y` is available generically through
> `CPolynomial.divByMonic` / `CPolynomial.modByMonic` over the coefficient ring
> `CPolynomial R` (see `CPolynomial.modByMonic_add_mul_divByMonic`).

`CompPoly.CBivariate.evalYPoly` (definition, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Factor.lean#L40))

> Substitute `Y ↦ f(X)` into a bivariate polynomial `Q`, i.e. evaluate `Q` at
> `f` in the `Y` variable. The result is the univariate polynomial `Q(X, f(X))`.

```lean
def evalYPoly [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (f : CPolynomial R) (Q : CBivariate R) : CPolynomial R
```

`CompPoly.CBivariate.isLinearYFactor` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Factor.lean#L46))

> Decide whether `Y - f(X)` divides `Q`, i.e. whether `Q(X, f(X)) = 0`. By the
> factor theorem this is exactly the test for `f(X)` being a `Y`-root of `Q`.

```lean
def isLinearYFactor [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (Q : CBivariate R) (f : CPolynomial R) : Bool
```

`CompPoly.CBivariate.evalYPoly_zero` (theorem, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Factor.lean#L51))

> `evalYPoly` sends the zero polynomial to `0`.

```lean
theorem evalYPoly_zero [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (f : CPolynomial R) :
    evalYPoly f (0 : CBivariate R) = 0
```

`CompPoly.CBivariate.evalYPoly_add` (theorem, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Factor.lean#L60))

> `evalYPoly` is additive in the polynomial being evaluated.

```lean
theorem evalYPoly_add [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (f : CPolynomial R) (P Q : CBivariate R) :
    evalYPoly f (P + Q) = evalYPoly f P + evalYPoly f Q
```

`CompPoly.CBivariate.isLinearYFactor_iff` (theorem, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Factor.lean#L71))

> The `isLinearYFactor` boolean test agrees with the proposition `Q(X, f(X)) = 0`.

```lean
theorem isLinearYFactor_iff [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (Q : CBivariate R) (f : CPolynomial R) :
    isLinearYFactor Q f = true ↔ evalYPoly f Q = 0
```

`CompPoly.CBivariate.evalYPoly_toPoly` (theorem, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Factor.lean#L78))

> Bridge to Mathlib: evaluating `Q` at `f` and mapping to `Polynomial R` agrees
> with evaluating the mapped `toPoly Q : R[X][Y]` at `f.toPoly`.

```lean
theorem evalYPoly_toPoly [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (f : CPolynomial R) (Q : CBivariate R) :
    (evalYPoly f Q).toPoly = (toPoly Q).eval (f.toPoly)
```

`CompPoly.CBivariate.divByLinearY` (definition, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Factor.lean#L99))

> Synthetic (Horner) division of a bivariate polynomial `Q` by the linear factor
> `Y - f(X)`, performed in the `Y` variable. Returns the pair `(quotient, remainder)`
> where the quotient is a `CBivariate R` and the remainder is a `CPolynomial R`.
>
> Writing `Q = Σ_{j=0}^n aⱼ Yʲ` with `aⱼ = coeff Q j`, the quotient coefficients
> `bⱼ` and the remainder `r` satisfy the synthetic-division recurrence
> `b_{n-1} = aₙ`, `b_{j-1} = aⱼ + f · bⱼ`, `r = a₀ + f · b₀`, so that
> `Q = quotient · (Y - f) + r`. See `divByLinearY_spec`.

```lean
def divByLinearY [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (Q : CBivariate R) (f : CPolynomial R) : CBivariate R × CPolynomial R
```

`CompPoly.CBivariate.divByLinearY_const` (theorem, [line 115](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Factor.lean#L115))

```lean
theorem divByLinearY_const [CommRing R] [BEq R] [LawfulBEq R]
    [Nontrivial R] [DecidableEq R] (a f : CPolynomial R) :
  divByLinearY (CPolynomial.C a : CBivariate R) f = (0, a)
```

`CompPoly.CBivariate.divByLinearY_zero` (theorem, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Factor.lean#L227))

```lean
theorem divByLinearY_zero [CommRing R] [BEq R] [LawfulBEq R]
    [Nontrivial R] [DecidableEq R] (f : CPolynomial R) :
  divByLinearY (0 : CBivariate R) f = (0, 0)
```

`CompPoly.CBivariate.divByLinearY_spec` (theorem, [line 518](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Factor.lean#L518))

> Correctness of `divByLinearY`: in `R[X][Y]` the computed quotient and
> remainder satisfy the Euclidean division identity
> `Q = quotient · (Y - f) + remainder`, over any commutative ring.

```lean
theorem divByLinearY_spec [CommRing R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (Q : CBivariate R) (f : CPolynomial R) :
    let quot := (divByLinearY Q f).1
    let rem := (divByLinearY Q f).2
    toPoly Q = toPoly quot * (Polynomial.X - Polynomial.C (f.toPoly)) +
        Polynomial.C (rem.toPoly)
```

`CompPoly.CBivariate.divByLinearY_rem_eq_eval` (theorem, [line 563](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Factor.lean#L563))

> The remainder of dividing `Q` by `Y - f` is the substitution `Q(X, f(X))`
> (`evalYPoly f Q`), by the factor/remainder theorem.

```lean
theorem divByLinearY_rem_eq_eval [CommRing R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (Q : CBivariate R) (f : CPolynomial R) :
    (divByLinearY Q f).2 = evalYPoly f Q
```

`CompPoly.CBivariate.divByLinearY_exact` (theorem, [line 579](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Factor.lean#L579))

> If `Y - f` divides `Q` (`isLinearYFactor Q f`), the division is exact:
> the remainder is `0`.

```lean
theorem divByLinearY_exact [CommRing R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (Q : CBivariate R) (f : CPolynomial R) (h : isLinearYFactor Q f = true) :
    (divByLinearY Q f).2 = 0
```

## Depends on

- [Equivalence with Mathlib Bivariate Polynomials](topoly.md)

## Sources

- [CompPoly/Bivariate/Factor.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Factor.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Bivariate.Factor.json)
