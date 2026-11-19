---
catalog: module
lean: CompPoly.CPolynomial.Raw.Roots.FiniteField.finiteFieldRootProductWith, CompPoly.CPolynomial.Raw.Roots.FiniteField.finiteFieldRootProduct, CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith, CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProduct, CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_toPoly_eq_normalize_gcd, CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_dvd_frobenius_of_context, CompPoly.CPolynomial.Roots.FiniteField.monicNormalize_ne_zero_of_ne_zero, CompPoly.CPolynomial.Roots.FiniteField.gcdMonic_ne_zero_of_left, CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_ne_zero_of_ne_zero
statement: formalized
proof: formalized
---

# Finite-Field Root Products

`CompPoly.Univariate.Roots.RootProduct`, in [CompPoly/Univariate/Roots/RootProduct.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/RootProduct.lean), by Valerii Huhnin.

> Executable construction of `gcd(p, X^q - X)` as
> `gcd(p, (X^q mod p) - (X mod p))`, so large finite fields never materialize the
> dense polynomial `X^q - X`.

`CompPoly.CPolynomial.Raw.Roots.FiniteField.finiteFieldRootProductWith` (definition, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/RootProduct.lean#L35))

> Raw squarefree product of the linear factors of `p` whose roots lie in the field.

```lean
def finiteFieldRootProductWith {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : CPolynomial.Roots.FiniteField.FiniteFieldContext F)
    (p : CPolynomial.Raw F) : CPolynomial.Raw F
```

`CompPoly.CPolynomial.Raw.Roots.FiniteField.finiteFieldRootProduct` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/RootProduct.lean#L46))

> Raw squarefree product using the default raw backends.

```lean
def finiteFieldRootProduct {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (ctx : CPolynomial.Roots.FiniteField.FiniteFieldContext F)
    (p : CPolynomial.Raw F) : CPolynomial.Raw F
```

`CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith` (definition, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/RootProduct.lean#L63))

> The squarefree product of the linear factors of `p` whose roots lie in the field.

```lean
def finiteFieldRootProductWith {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : FiniteFieldContext F) (p : CPolynomial F) : CPolynomial F
```

`CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProduct` (definition, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/RootProduct.lean#L69))

> The squarefree product of the linear factors of `p` using the default raw backends.

```lean
def finiteFieldRootProduct {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (ctx : FiniteFieldContext F) (p : CPolynomial F) : CPolynomial F
```

`CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_toPoly_eq_normalize_gcd` (theorem, [line 153](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/RootProduct.lean#L153))

> The finite-field root product agrees with the normalized Mathlib gcd of the
> monic input and its represented Frobenius witness.

```lean
theorem finiteFieldRootProductWith_toPoly_eq_normalize_gcd {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : FiniteFieldContext F) {p : CPolynomial F}
    (hp : p ≠ 0) :
    let pMonic := CPolynomial.monicNormalize p
    (finiteFieldRootProductWith M D ctx p).toPoly =
      normalize (EuclideanDomain.gcd pMonic.toPoly
        (CPolynomial.ofArray
          (CPolynomial.Raw.xPowSubXModWith M D ctx.q pMonic.val)).toPoly)
```

`CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_dvd_frobenius_of_context` (theorem, [line 489](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/RootProduct.lean#L489))

> The finite-field root product divides the finite-field Frobenius polynomial.
>
> This is the modular-gcd bridge: the executable root product uses the congruent
> modular witness `(X^q mod p) - (X mod p)` instead of materializing `X^q - X`.

```lean
theorem finiteFieldRootProductWith_dvd_frobenius_of_context {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : FiniteFieldContext F) {p : CPolynomial F} (_hp : p ≠ 0) :
    (finiteFieldRootProductWith M D ctx p).toPoly ∣
      ((Polynomial.X : Polynomial F) ^ ctx.q - Polynomial.X)
```

`CompPoly.CPolynomial.Roots.FiniteField.monicNormalize_ne_zero_of_ne_zero` (theorem, [line 584](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/RootProduct.lean#L584))

> Monic normalization preserves nonzeroness.

```lean
theorem monicNormalize_ne_zero_of_ne_zero {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {p : CPolynomial F} (hp : p ≠ 0) :
    CPolynomial.monicNormalize p ≠ 0
```

`CompPoly.CPolynomial.Roots.FiniteField.gcdMonic_ne_zero_of_left` (theorem, [line 603](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/RootProduct.lean#L603))

> The monic gcd of a nonzero left operand is nonzero.

```lean
theorem gcdMonic_ne_zero_of_left {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    {p q : CPolynomial F} (hp : p ≠ 0) :
    CPolynomial.gcdMonic p q ≠ 0
```

`CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_ne_zero_of_ne_zero` (theorem, [line 621](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/RootProduct.lean#L621))

> The finite-field root product of a nonzero polynomial is nonzero.

```lean
theorem finiteFieldRootProductWith_ne_zero_of_ne_zero {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : FiniteFieldContext F) {p : CPolynomial F}
    (hp : p ≠ 0) :
    finiteFieldRootProductWith M D ctx p ≠ 0
```

## Depends on

- [Raw Modular Operations on Univariate Polynomials](../../part-01/raw/modular.md)
- [Finite-Field Root Contexts](context.md)
- [Computable Univariate To `Polynomial`](../topoly/core.md)

## Proof depends on

- [Extended Euclidean Algorithm for `CPolynomial`](../../part-01/euclideanalgorithm.md)

## Sources

- [CompPoly/Univariate/Roots/RootProduct.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/RootProduct.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.Roots.RootProduct.json)
