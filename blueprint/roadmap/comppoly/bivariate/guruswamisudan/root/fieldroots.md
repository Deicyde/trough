---
catalog: module
lean: CompPoly.GuruswamiSudan.degreeLtBool, CompPoly.GuruswamiSudan.ContainsAllFieldElements, CompPoly.GuruswamiSudan.rootsInFieldByEnumeration, CompPoly.GuruswamiSudan.enumeratingFieldRootContext
statement: formalized
proof: formalized
---

# Guruswami-Sudan Field Roots

`CompPoly.Bivariate.GuruswamiSudan.Root.FieldRoots`, in [CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots.lean), by Valerii Huhnin.

> Executable univariate field-root helpers used by Roth-Ruckenstein recursion.
> The explicit `FieldRootContext` context makes this dependency replaceable for
> large concrete fields.

`CompPoly.GuruswamiSudan.degreeLtBool` (definition, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots.lean#L27))

> Executable degree-`< k` check for canonical polynomials.

```lean
def degreeLtBool {F : Type*} [Zero F] (p : CPolynomial F) (k : Nat) : Bool
```

`CompPoly.GuruswamiSudan.ContainsAllFieldElements` (abbreviation, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots.lean#L31))

> Compatibility alias for the univariate exhaustive-enumeration predicate.

```lean
abbrev ContainsAllFieldElements {F : Type*} (elements : Array F) : Prop
```

`CompPoly.GuruswamiSudan.rootsInFieldByEnumeration` (definition, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots.lean#L35))

> Compatibility wrapper for roots by exhaustive evaluation over an explicit field list.

```lean
def rootsInFieldByEnumeration {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (elements : Array F) (hElements : ContainsAllFieldElements elements)
    (p : CPolynomial F) : Array F
```

`CompPoly.GuruswamiSudan.enumeratingFieldRootContext` (definition, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots.lean#L43))

> Field roots by explicit enumeration over a supplied field-element list.

```lean
def enumeratingFieldRootContext (F : Type*) [Field F] [BEq F] [LawfulBEq F]
    (elements : Array F) (hElements : ContainsAllFieldElements elements) :
    FieldRootContext F
```

## Depends on

- [Guruswami-Sudan Backend Contexts](../context.md)
- [Exhaustive Finite-Field Root Enumeration](../../../univariate/part-02/roots/enumeration.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Root.FieldRoots.json)
