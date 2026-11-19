---
catalog: module
lean: CompPoly.CBivariate.linearYDivisor, CompPoly.CBivariate.linearYDivisor_toPoly, CompPoly.CBivariate.linearYDivisor_monic, CompPoly.CBivariate.divByLinearY_euclid_toPoly, CompPoly.CBivariate.divByLinearY_eq_divByMonic
statement: formalized
proof: formalized
---

# Bridge: synthetic linear division equals general monic division

`CompPoly.Bivariate.FactorMonic`, in [CompPoly/Bivariate/FactorMonic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/FactorMonic.lean), by Dimitris Mitsios.

> Proves that the bespoke synthetic division `divByLinearY Q f` (Horner) coincides
> with general monic Euclidean division of `Q` by the linear factor `Y - f`, using
> the `CommRing`-general `CPolynomial.divByMonic` / `CPolynomial.modByMonic` at the
> coefficient ring `CPolynomial R` (recall `CBivariate R = CPolynomial (CPolynomial R)`).
>
> `divByLinearY_eq_divByMonic` shows the quotient equals `(divByLinearY Q f).1` and
> the remainder equals `CPolynomial.C (divByLinearY Q f).2`, so `divByLinearY` is a
> verified fast path for division by `Y - f`.
>
> The proof works in the outer polynomial ring `(CPolynomial R)[Y]` (the image of
> `CPolynomial.toPoly`): it rewrites the divisor as `X - C f`
> (`linearYDivisor_toPoly`), establishes the Euclidean identity by transporting
> `divByLinearY_spec` across the coefficient ring-equiv
> (`divByLinearY_euclid_toPoly`), and concludes via
> `Polynomial.div_modByMonic_unique`.

`CompPoly.CBivariate.linearYDivisor` (definition, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/FactorMonic.lean#L41))

> The linear monic divisor `Y - f`, as a bivariate polynomial
> (`CBivariate R = CPolynomial (CPolynomial R)`).

```lean
def linearYDivisor [CommRing R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (f : CPolynomial R) : CBivariate R
```

`CompPoly.CBivariate.linearYDivisor_toPoly` (theorem, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/FactorMonic.lean#L47))

> `toPoly` sends the linear divisor `Y - f` to `X - C f` in `(CPolynomial R)[Y]`.

```lean
theorem linearYDivisor_toPoly [CommRing R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (f : CPolynomial R) :
    CPolynomial.toPoly (linearYDivisor f) = Polynomial.X - Polynomial.C f
```

`CompPoly.CBivariate.linearYDivisor_monic` (theorem, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/FactorMonic.lean#L53))

> The linear divisor `Y - f` is monic.

```lean
theorem linearYDivisor_monic [CommRing R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (f : CPolynomial R) :
    CPolynomial.monic (linearYDivisor f) = true
```

`CompPoly.CBivariate.divByLinearY_euclid_toPoly` (theorem, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/FactorMonic.lean#L65))

> Euclidean identity for `divByLinearY` in the outer ring `(CPolynomial R)[Y]`:
> `C rem + (Y - f) * quot = Q` after `toPoly`. Transports `divByLinearY_spec`
> across the coefficient ring-equiv.

```lean
theorem divByLinearY_euclid_toPoly
    [CommRing R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (Q : CBivariate R) (f : CPolynomial R) :
    (CPolynomial.C (divByLinearY Q f).2).toPoly
        + CPolynomial.toPoly (linearYDivisor f) * CPolynomial.toPoly ((divByLinearY Q f).1)
      = CPolynomial.toPoly Q
```

`CompPoly.CBivariate.divByLinearY_eq_divByMonic` (theorem, [line 83](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/FactorMonic.lean#L83))

> The bespoke synthetic division `divByLinearY` agrees with general monic
> division by `Y - f`: the quotient matches `divByMonic`, and the constant-in-`Y`
> remainder `C (divByLinearY Q f).2` matches `modByMonic`.

```lean
theorem divByLinearY_eq_divByMonic [CommRing R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (Q : CBivariate R) (f : CPolynomial R) :
    CPolynomial.divByMonic Q (linearYDivisor f) = (divByLinearY Q f).1
      ∧ CPolynomial.modByMonic Q (linearYDivisor f)
          = CPolynomial.C (divByLinearY Q f).2
```

## Depends on

- [Factorisation of Computable Bivariate Polynomials](factor.md)

## Proof depends on

- [Univariate Division Correctness](../univariate/part-01/divisioncorrectness.md)

## Sources

- [CompPoly/Bivariate/FactorMonic.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/FactorMonic.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Bivariate.FactorMonic.json)
