---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.isRepresentedLinearFactor, CompPoly.CPolynomial.Roots.FiniteField.isRepresentedLinearFactor_sound, CompPoly.CPolynomial.Roots.FiniteField.representedLinearFactorArray, CompPoly.CPolynomial.Roots.FiniteField.xPowModWith
statement: formalized
proof: formalized
---

# Linear-Factor Splitter Helpers

`CompPoly.Univariate.Roots.Splitter`, in [CompPoly/Univariate/Roots/Splitter.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Splitter.lean), by Valerii Huhnin.

> Shared executable helpers for finite-field linear-factor splitters.

`CompPoly.CPolynomial.Roots.FiniteField.isRepresentedLinearFactor` (definition, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Splitter.lean#L29))

> Boolean recognizer for represented nonconstant linear factors.

```lean
def isRepresentedLinearFactor {F : Type*} [Field F] [BEq F]
    (p : CPolynomial F) : Bool
```

`CompPoly.CPolynomial.Roots.FiniteField.isRepresentedLinearFactor_sound` (theorem, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Splitter.lean#L34))

> The represented-linear Boolean recognizer is sound.

```lean
theorem isRepresentedLinearFactor_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {p : CPolynomial F} (h : isRepresentedLinearFactor p = true) :
    IsLinearFactor p
```

`CompPoly.CPolynomial.Roots.FiniteField.representedLinearFactorArray` (definition, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Splitter.lean#L43))

> Return `p` as a singleton array if it is represented as a nonconstant linear factor.

```lean
def representedLinearFactorArray {F : Type*} [Field F] [BEq F]
    (p : CPolynomial F) : Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.xPowModWith` (definition, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Splitter.lean#L48))

> `X^exponent mod modulus`, lifted back to canonical polynomials.

```lean
def xPowModWith {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (modulus : CPolynomial F) (exponent : Nat) : CPolynomial F
```

## Depends on

- [Raw Modular Operations on Univariate Polynomials](../../part-01/raw/modular.md)
- [Finite-Field Root Contexts](context.md)

## Sources

- [CompPoly/Univariate/Roots/Splitter.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Splitter.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.Roots.Splitter.json)
