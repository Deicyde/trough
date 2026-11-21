---
catalog: module
lean: CompPoly.CPolynomial.Raw.mulModWith, CompPoly.CPolynomial.Raw.powModBinaryAuxWith, CompPoly.CPolynomial.Raw.powModWith, CompPoly.CPolynomial.Raw.xModWith, CompPoly.CPolynomial.Raw.xPowSubXModWith
statement: formalized
proof: formalized
---

# Raw Modular Operations on Univariate Polynomials

`CompPoly.Univariate.Raw.Modular`, in [CompPoly/Univariate/Raw/Modular.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Modular.lean), by Valerii Huhnin.

> Context-parametric modular multiplication and exponentiation over raw
> univariate polynomials.

`CompPoly.CPolynomial.Raw.mulModWith` (definition, [line 24](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Modular.lean#L24))

> Raw multiplication modulo a polynomial, treating zero modulus as no reduction.

```lean
def mulModWith {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (modulus p q : CPolynomial.Raw F) : CPolynomial.Raw F
```

`CompPoly.CPolynomial.Raw.powModBinaryAuxWith` (definition, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Modular.lean#L34))

> Raw binary modular exponentiation accumulator.

```lean
def powModBinaryAuxWith {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (modulus : CPolynomial.Raw F) :
    Nat → CPolynomial.Raw F → CPolynomial.Raw F → CPolynomial.Raw F
```

`CompPoly.CPolynomial.Raw.powModWith` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Modular.lean#L52))

> Raw modular exponentiation by repeated squaring.

```lean
def powModWith {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (modulus base : CPolynomial.Raw F) (exponent : Nat) : CPolynomial.Raw F
```

`CompPoly.CPolynomial.Raw.xModWith` (definition, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Modular.lean#L63))

> Raw `X mod modulus`, with zero modulus treated as no reduction.

```lean
def xModWith {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (D : CPolynomial.Raw.ModContext F) : CPolynomial.Raw F → CPolynomial.Raw F
```

`CompPoly.CPolynomial.Raw.xPowSubXModWith` (definition, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Modular.lean#L72))

> Raw `(X^q mod modulus) - (X mod modulus)`, without materializing `X^q - X`.

```lean
def xPowSubXModWith {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) (modulus : CPolynomial.Raw F) : CPolynomial.Raw F
```

## Depends on

- [Raw Univariate Algorithm Contexts](context.md)

## Sources

- [CompPoly/Univariate/Raw/Modular.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Modular.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.Raw.Modular.json)
