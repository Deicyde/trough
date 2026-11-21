---
catalog: module
lean: CompPoly.GuruswamiSudan.initialCoefficientPolynomial, CompPoly.GuruswamiSudan.isRootYDegreeLtBool, CompPoly.GuruswamiSudan.rootsYDegreeLtFromCandidates, CompPoly.GuruswamiSudan.extendPrefix, CompPoly.GuruswamiSudan.polynomialPrefix, CompPoly.GuruswamiSudan.rootsInFieldForNonzeroEquation
statement: formalized
proof: formalized
---

# Common Guruswami-Sudan Root Helpers

`CompPoly.Bivariate.GuruswamiSudan.Root.Common`, in [CompPoly/Bivariate/GuruswamiSudan/Root/Common.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Common.lean), by Valerii Huhnin.

> Executable helpers shared by bounded bivariate root backends.

`CompPoly.GuruswamiSudan.initialCoefficientPolynomial` (definition, [line 24](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Common.lean#L24))

> The coefficient of `Y^j` in `Q(0, Y)`, as a polynomial in the next root
> coefficient.

```lean
def initialCoefficientPolynomial {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) : CPolynomial F
```

`CompPoly.GuruswamiSudan.isRootYDegreeLtBool` (definition, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Common.lean#L32))

> Executable final check for the GS root condition.

```lean
def isRootYDegreeLtBool {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (Q : CBivariate F) (k : Nat) (p : CPolynomial F) : Bool
```

`CompPoly.GuruswamiSudan.rootsYDegreeLtFromCandidates` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Common.lean#L38))

> Filter a candidate family to exact bounded-degree roots.

```lean
def rootsYDegreeLtFromCandidates {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (candidates : Array (CPolynomial F)) (Q : CBivariate F) (k : Nat) :
    Array (CPolynomial F)
```

`CompPoly.GuruswamiSudan.extendPrefix` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Common.lean#L45))

> Extend one candidate prefix by one coefficient at `X^depth`.

```lean
def extendPrefix {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (pref : CPolynomial F) (depth : Nat) (coeff : F) : CPolynomial F
```

`CompPoly.GuruswamiSudan.polynomialPrefix` (definition, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Common.lean#L51))

> Truncate a polynomial to its first `n` coefficients.

```lean
def polynomialPrefix {R : Type*} [Zero R] [BEq R] [LawfulBEq R]
    (p : CPolynomial R) (n : Nat) : CPolynomial R
```

`CompPoly.GuruswamiSudan.rootsInFieldForNonzeroEquation` (definition, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Common.lean#L61))

> Query a field-root backend only for nonzero equations.
>
> A zero equation imposes no restriction on the next coefficient. Enumerating all
> field elements is unsuitable for large fields, so bounded-root backends use
> residual normalization to avoid zero equations for nonzero bivariate inputs.

```lean
def rootsInFieldForNonzeroEquation {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (fieldRoots : FieldRootContext F) (p : CPolynomial F) : Array F
```

## Depends on

- [Guruswami-Sudan Field Roots](fieldroots.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Root/Common.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Common.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Root.Common.json)
