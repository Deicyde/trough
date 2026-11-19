---
catalog: module
lean: CompPoly.CPolynomial.derivative, CompPoly.CPolynomial.coeff_derivative, CompPoly.CPolynomial.derivative_zero, CompPoly.CPolynomial.derivative_C, CompPoly.CPolynomial.derivative_monomial, CompPoly.CPolynomial.derivative_add, CompPoly.CPolynomial.derivative_toPoly, CompPoly.CPolynomial.derivative_mul, CompPoly.CPolynomial.taylor, CompPoly.CPolynomial.taylor_toPoly, CompPoly.CPolynomial.taylor_zero, CompPoly.CPolynomial.taylor_coeff_zero
statement: formalized
proof: formalized
---

# Formal Derivative and Taylor Shift of Computable Univariate Polynomials

`CompPoly.Univariate.Deriv`, in [CompPoly/Univariate/Deriv.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Deriv.lean), by Dimitris Mitsios.

> Defines the formal derivative `CPolynomial.derivative` and the Taylor shift
> `CPolynomial.taylor`, with proofs of their core properties.

`CompPoly.CPolynomial.derivative` (definition, [line 28](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Deriv.lean#L28))

> The formal derivative of a computable polynomial.
> Coefficient `n` of the result is `coeff p (n+1) * (n+1)`.

```lean
def derivative [Semiring R] [BEq R] [LawfulBEq R]
    (p : CPolynomial R) : CPolynomial R
```

`CompPoly.CPolynomial.coeff_derivative` (theorem, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Deriv.lean#L36))

> Coefficient formula for the derivative.

```lean
theorem coeff_derivative [Semiring R] [BEq R] [LawfulBEq R]
    (p : CPolynomial R) (n : ℕ) :
    coeff (derivative p) n = coeff p (n + 1) * (↑(n + 1) : R)
```

`CompPoly.CPolynomial.derivative_zero` (theorem, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Deriv.lean#L56))

> The derivative of the zero polynomial is zero.

```lean
theorem derivative_zero [Semiring R] [BEq R] [LawfulBEq R] :
    derivative (0 : CPolynomial R) = 0
```

`CompPoly.CPolynomial.derivative_C` (theorem, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Deriv.lean#L64))

> The derivative of a constant is zero.

```lean
theorem derivative_C [Semiring R] [BEq R] [LawfulBEq R] (r : R) :
    derivative (C r) = 0
```

`CompPoly.CPolynomial.derivative_monomial` (theorem, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Deriv.lean#L72))

> The derivative of a monomial.

```lean
theorem derivative_monomial [Semiring R] [BEq R] [LawfulBEq R]
    [DecidableEq R] (n : ℕ) (r : R) :
    derivative (monomial n r) =
      monomial (n - 1) (r * (↑n : R))
```

`CompPoly.CPolynomial.derivative_add` (theorem, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Deriv.lean#L85))

> The derivative distributes over addition.

```lean
theorem derivative_add [Semiring R] [BEq R] [LawfulBEq R] [DecidableEq R]
    (p q : CPolynomial R) :
    derivative (p + q) = derivative p + derivative q
```

`CompPoly.CPolynomial.derivative_toPoly` (theorem, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Deriv.lean#L95))

> The computable derivative matches Mathlib's `Polynomial.derivative` under `toPoly`.

```lean
theorem derivative_toPoly [Semiring R] [BEq R] [LawfulBEq R] (p : CPolynomial R) :
    (derivative p).toPoly = Polynomial.derivative (R := R) p.toPoly
```

`CompPoly.CPolynomial.derivative_mul` (theorem, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Deriv.lean#L103))

> The derivative satisfies the Leibniz product rule.

```lean
theorem derivative_mul [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] (p q : CPolynomial R) :
    derivative (p * q) = derivative p * q + p * derivative q
```

`CompPoly.CPolynomial.taylor` (definition, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Deriv.lean#L111))

> The Taylor shift `taylor a p = p(X + a)`.

```lean
def taylor [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a : R) (p : CPolynomial R) : CPolynomial R
```

`CompPoly.CPolynomial.taylor_toPoly` (theorem, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Deriv.lean#L116))

> The computable Taylor shift matches `Polynomial.taylor` under `toPoly`.

```lean
theorem taylor_toPoly [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a : R) (p : CPolynomial R) :
    (taylor a p).toPoly = Polynomial.taylor a p.toPoly
```

`CompPoly.CPolynomial.taylor_zero` (theorem, [line 127](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Deriv.lean#L127))

> The Taylor shift of zero is zero.

```lean
theorem taylor_zero [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a : R) : taylor a (0 : CPolynomial R) = 0
```

`CompPoly.CPolynomial.taylor_coeff_zero` (theorem, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Deriv.lean#L133))

> The constant coefficient of the Taylor shift is evaluation at the shift point.

```lean
theorem taylor_coeff_zero [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a : R) (p : CPolynomial R) : coeff (taylor a p) 0 = eval a p
```

## Depends on

- [Computable Univariate To `Polynomial`](../part-02/topoly/core.md)

## Proof depends on

- [Proofs of Correctness for CPolynomial Operations, wrt Mathlib Specs](../part-02/topoly/impl.md)

## Sources

- [CompPoly/Univariate/Deriv.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Deriv.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Univariate.Deriv.json)
