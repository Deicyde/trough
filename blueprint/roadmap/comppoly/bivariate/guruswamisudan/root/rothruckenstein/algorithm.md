---
catalog: module
lean: CompPoly.GuruswamiSudan.substituteYRootPlusXY, CompPoly.GuruswamiSudan.transformedRothRuckensteinResidual, CompPoly.GuruswamiSudan.nextCoefficientSlope, CompPoly.GuruswamiSudan.nextCoefficientPolynomial, CompPoly.GuruswamiSudan.rootPrefixExtensionsWithFieldRootContext, CompPoly.GuruswamiSudan.rothRuckensteinRootPrefixes, CompPoly.GuruswamiSudan.transformedRothRuckensteinRootPrefixesWithFuel, CompPoly.GuruswamiSudan.transformedRothRuckensteinRootPrefixes, CompPoly.GuruswamiSudan.transformedRothRuckensteinRootsYDegreeLt, CompPoly.GuruswamiSudan.rothRuckensteinRootsYDegreeLt
statement: formalized
proof: formalized
---

# Roth-Ruckenstein-Style Root Finding

`CompPoly.Bivariate.GuruswamiSudan.Root.RothRuckenstein.Algorithm`, in [CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Algorithm.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Algorithm.lean), by Valerii Huhnin.

> Executable bounded-degree roots for `CBivariate F` using recursive coefficient
> reconstruction and an explicit univariate field-root backend, following the
> Roth-Ruckenstein root-search step [RR00].
>
> ## References
>
> * [Roth, R. M., and Ruckenstein, G., *Efficient decoding of Reed-Solomon codes
>     beyond half the minimum distance*][RR00]

`CompPoly.GuruswamiSudan.substituteYRootPlusXY` (definition, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Algorithm.lean#L32))

> Substitute `Y = a + X * Y` into a bivariate polynomial.

```lean
def substituteYRootPlusXY {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (a : F) : CBivariate F
```

`CompPoly.GuruswamiSudan.transformedRothRuckensteinResidual` (definition, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Algorithm.lean#L48))

> One residual step in the transformed Roth-Ruckenstein recursion.

```lean
def transformedRothRuckensteinResidual {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (a : F) : CBivariate F
```

`CompPoly.GuruswamiSudan.nextCoefficientSlope` (definition, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Algorithm.lean#L54))

> The linear coefficient of the next recursive root equation after depth zero.

```lean
def nextCoefficientSlope {F : Type*} [Field F]
    (Q : CBivariate F) (pref : CPolynomial F) : F
```

`CompPoly.GuruswamiSudan.nextCoefficientPolynomial` (definition, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Algorithm.lean#L62))

> Polynomial equation for the next coefficient in the prefix recursion.

```lean
def nextCoefficientPolynomial {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (pref : CPolynomial F) (depth : Nat) : CPolynomial F
```

`CompPoly.GuruswamiSudan.rootPrefixExtensionsWithFieldRootContext` (definition, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Algorithm.lean#L77))

> Ordered recursive candidate extensions using a field-root backend.
>
> This direct coefficient-equation helper does not expand zero equations. The
> residual-transform Roth-Ruckenstein backend uses residual normalization before
> field-root queries.

```lean
def rootPrefixExtensionsWithFieldRootContext {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (fieldRoots : FieldRootContext F) (Q : CBivariate F) (depth : Nat)
    (prefixes : Array (CPolynomial F)) : List (CPolynomial F)
```

`CompPoly.GuruswamiSudan.rothRuckensteinRootPrefixes` (definition, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Algorithm.lean#L88))

> Candidate prefixes after choosing coefficients through depth `< k` in the
> direct coefficient-equation recursion. Zero equations are not expanded.

```lean
def rothRuckensteinRootPrefixes {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (fieldRoots : FieldRootContext F) (Q : CBivariate F) : Nat → Array (CPolynomial F)
```

`CompPoly.GuruswamiSudan.transformedRothRuckensteinRootPrefixesWithFuel` (definition, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Algorithm.lean#L97))

> Residual-transform Roth-Ruckenstein prefixes with explicit recursion fuel.

```lean
def transformedRothRuckensteinRootPrefixesWithFuel {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (fieldRoots : FieldRootContext F) :
    Nat → CBivariate F → Nat → CPolynomial F → Array (CPolynomial F)
```

`CompPoly.GuruswamiSudan.transformedRothRuckensteinRootPrefixes` (definition, [line 117](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Algorithm.lean#L117))

> Candidate prefixes from the residual-transform recursion through precision `X^k`.

```lean
def transformedRothRuckensteinRootPrefixes {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (fieldRoots : FieldRootContext F) (Q : CBivariate F) (k : Nat) :
    Array (CPolynomial F)
```

`CompPoly.GuruswamiSudan.transformedRothRuckensteinRootsYDegreeLt` (definition, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Algorithm.lean#L124))

> Residual-transform Roth-Ruckenstein bounded-degree roots.

```lean
def transformedRothRuckensteinRootsYDegreeLt {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (fieldRoots : FieldRootContext F) (Q : CBivariate F) (k : Nat) :
    Array (CPolynomial F)
```

`CompPoly.GuruswamiSudan.rothRuckensteinRootsYDegreeLt` (definition, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Algorithm.lean#L137))

> Roth-Ruckenstein bounded-degree roots.
>
> The public backend uses the residual-transform recursion, which strips common
> `X`-adic factors before each field-root query. Zero univariate equations are
> excluded from the field-root dependency for nonzero bivariate inputs.

```lean
def rothRuckensteinRootsYDegreeLt {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (fieldRoots : FieldRootContext F) (Q : CBivariate F) (k : Nat) :
    Array (CPolynomial F)
```

## Depends on

- [Common Guruswami-Sudan Root Helpers](../common.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Algorithm.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Algorithm.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Root.RothRuckenstein.Algorithm.json)
