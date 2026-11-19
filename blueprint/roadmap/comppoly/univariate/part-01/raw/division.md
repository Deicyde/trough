---
catalog: module
lean: CompPoly.CPolynomial.Raw.divModByMonicAux, CompPoly.CPolynomial.Raw.divByMonic, CompPoly.CPolynomial.Raw.modByMonic, CompPoly.CPolynomial.Raw.subScaledShift, CompPoly.CPolynomial.Raw.modByMonicRemainderOnly, CompPoly.CPolynomial.Raw.inverseModX, CompPoly.CPolynomial.Raw.modByMonicByReversal, CompPoly.CPolynomial.Raw.div, CompPoly.CPolynomial.Raw.mod, CompPoly.CPolynomial.Raw.monicNormalize, CompPoly.CPolynomial.Raw.gcdMonicWithFuel, CompPoly.CPolynomial.Raw.gcdMonic
statement: formalized
proof: formalized
---

# Raw Univariate Polynomial Division

`CompPoly.Univariate.Raw.Division`, in [CompPoly/Univariate/Raw/Division.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Division.lean), by Quang Dao, Gregor Mitscha-Baude, Derek Sorensen, Desmond Coles, Valerii Huhnin.

> Division algorithms for raw computable univariate polynomials.

`CompPoly.CPolynomial.Raw.divModByMonicAux` (definition, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Division.lean#L31))

> Division with remainder by a monic polynomial using polynomial long division.

```lean
def divModByMonicAux [CommRing R] (p : CPolynomial.Raw R) (q : CPolynomial.Raw R) :
    CPolynomial.Raw R × CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.divByMonic` (definition, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Division.lean#L48))

> Division of `p : CPolynomial.Raw R` by a monic `q : CPolynomial.Raw R`.

```lean
def divByMonic [CommRing R] (p : CPolynomial.Raw R) (q : CPolynomial.Raw R) :
    CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.modByMonic` (definition, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Division.lean#L53))

> Modulus of `p : CPolynomial.Raw R` by a monic `q : CPolynomial.Raw R`.

```lean
def modByMonic [CommRing R] (p : CPolynomial.Raw R) (q : CPolynomial.Raw R) :
    CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.subScaledShift` (definition, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Division.lean#L59))

> Subtract `scale * q * X^shift` from `p` without using general polynomial multiplication.

```lean
def subScaledShift [Field R] (p q : CPolynomial.Raw R) (scale : R) (shift : Nat) :
    CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.modByMonicRemainderOnly` (definition, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Division.lean#L74))

> Remainder-only long division by a monic polynomial.
>
> Unlike `modByMonic`, this does not compute the quotient and avoids the general
> polynomial multiplications used by each cancellation step. It is intended as an
> executable implementation for the canonical `modByMonic` specification.

```lean
def modByMonicRemainderOnly [Field R] (p : CPolynomial.Raw R) (q : CPolynomial.Raw R) :
    CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.inverseModX` (definition, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Division.lean#L90))

> Inverse modulo `X^k`, using Newton iteration and the supplied low-product backend.

```lean
def inverseModX [Field R] [LawfulBEq R] (M : MulLowContext R) (k : Nat)
    (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.modByMonicByReversal` (definition, [line 118](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Division.lean#L118))

> Remainder by a monic polynomial through reversal and truncated products.
>
> For canonical monic inputs this computes the quotient from the reversed divisor
> inverse modulo `X^k`, then subtracts only the low coefficients needed for the
> remainder. Inputs outside the fast-path guard use the simple monic-remainder
> implementation.

```lean
def modByMonicByReversal [Field R] [LawfulBEq R] (M : MulLowContext R)
    (p : CPolynomial.Raw R) (q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.div` (definition, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Division.lean#L137))

> Division of two `CPolynomial.Raw`s.

```lean
def div [Field R] (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.mod` (definition, [line 141](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Division.lean#L141))

> Modulus of two `CPolynomial.Raw`s.

```lean
def mod [Field R] (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.monicNormalize` (definition, [line 148](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Division.lean#L148))

> Normalize a nonzero raw polynomial to monic form. The zero polynomial stays zero.

```lean
def monicNormalize [Field R] (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.gcdMonicWithFuel` (definition, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Division.lean#L156))

> Raw Euclidean gcd with explicit fuel, normalized to a monic result.

```lean
def gcdMonicWithFuel [Field R] :
    Nat → CPolynomial.Raw R → CPolynomial.Raw R → CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.gcdMonic` (definition, [line 168](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Division.lean#L168))

> Raw monic Euclidean gcd.

```lean
def gcdMonic [Field R] (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

## Depends on

- [Raw Univariate Polynomial Operations](ops.md)

## Sources

- [CompPoly/Univariate/Raw/Division.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Division.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.Raw.Division.json)
