---
catalog: module
lean: CompPoly.CPolynomial.mulModWith, CompPoly.CPolynomial.powModBinaryAuxWith, CompPoly.CPolynomial.powModWith, CompPoly.CPolynomial.xModWith, CompPoly.CPolynomial.xPowSubXModWith
statement: formalized
proof: formalized
---

# Modular Operations on Univariate Polynomials

`CompPoly.Univariate.Modular`, in [CompPoly/Univariate/Modular.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Modular.lean), by Valerii Huhnin.

> Reusable executable modular arithmetic for canonical `CPolynomial`s over public
> `CPolynomial.MulContext` and `CPolynomial.ModContext` backends.

`CompPoly.CPolynomial.mulModWith` (definition, [line 24](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Modular.lean#L24))

> Multiply modulo a polynomial, treating zero modulus as no reduction.

```lean
def mulModWith {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : MulContext F) (D : ModContext F)
    (modulus p q : CPolynomial F) : CPolynomial F
```

`CompPoly.CPolynomial.powModBinaryAuxWith` (definition, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Modular.lean#L34))

> Binary modular exponentiation accumulator.

```lean
def powModBinaryAuxWith {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : MulContext F) (D : ModContext F)
    (modulus : CPolynomial F) :
    Nat → CPolynomial F → CPolynomial F → CPolynomial F
```

`CompPoly.CPolynomial.powModWith` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Modular.lean#L52))

> Modular exponentiation by repeated squaring.

```lean
def powModWith {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : MulContext F) (D : ModContext F)
    (modulus base : CPolynomial F) (exponent : Nat) : CPolynomial F
```

`CompPoly.CPolynomial.xModWith` (definition, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Modular.lean#L63))

> `X mod modulus`, with zero modulus treated as no reduction.

```lean
def xModWith {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (D : ModContext F) : CPolynomial F → CPolynomial F
```

`CompPoly.CPolynomial.xPowSubXModWith` (definition, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Modular.lean#L72))

> `(X^q mod modulus) - (X mod modulus)`, without materializing `X^q - X`.

```lean
def xPowSubXModWith {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : MulContext F) (D : ModContext F)
    (q : Nat) (modulus : CPolynomial F) : CPolynomial F
```

## Depends on

- [Univariate Algorithm Contexts](context.md)

## Sources

- [CompPoly/Univariate/Modular.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Modular.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Univariate.Modular.json)
