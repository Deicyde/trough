---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.eval_shoupModularXPowerWith_eq_pow, CompPoly.CPolynomial.Roots.FiniteField.eval_traceCoordinatePolynomialWith, CompPoly.CPolynomial.Roots.FiniteField.traceValue_sub, CompPoly.CPolynomial.Roots.FiniteField.traceValue_mul_sub_eq_zero_of_eq, CompPoly.CPolynomial.Roots.FiniteField.eq_of_traceValue_eq_on_basis, CompPoly.CPolynomial.Roots.FiniteField.shoup_gcdBucket_root, CompPoly.CPolynomial.Roots.FiniteField.shoup_gcdBucket_root_iff, CompPoly.CPolynomial.Roots.FiniteField.shoupSplitCandidatesWith_root, CompPoly.CPolynomial.Roots.FiniteField.shoupSplitCandidatesWith_dvd_input, CompPoly.CPolynomial.Roots.FiniteField.shoupSplitLinearFactorsWith_complete, CompPoly.CPolynomial.Roots.FiniteField.shoupLinearFactorProductSplitterWith, CompPoly.CPolynomial.Roots.FiniteField.shoupLinearFactorProductSplitter, CompPoly.CPolynomial.Roots.FiniteField.shoupLinearFactorProductSplitterWith_sound, CompPoly.CPolynomial.Roots.FiniteField.shoupLinearFactorProductSplitterWith_complete, CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_dvd_frobenius, CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_shoupSplitterInput, CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProduct_shoupSplitterInput, CompPoly.CPolynomial.Roots.FiniteField.rootProduct_satisfies_shoupSplitterInput
statement: formalized
proof: formalized
---

# Correctness Surface for Shoup-Style Trace Splitting

`CompPoly.Univariate.Roots.Shoup.Correctness`, in [CompPoly/Univariate/Roots/Shoup/Correctness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean), by Valerii Huhnin.

> This file states the proof obligations for the executable Shoup trace splitter.
> The main completeness contract is intentionally limited to valid root products:
> nonzero divisors of `X^q - X`, as produced by the finite-field root-product
> construction.

`CompPoly.CPolynomial.Roots.FiniteField.eval_shoupModularXPowerWith_eq_pow` (theorem, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L43))

> Evaluation of a Shoup modular power at a root of the modulus.

```lean
theorem eval_shoupModularXPowerWith_eq_pow {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) {modulus : CPolynomial F} {a : F}
    (hroot : CPolynomial.eval a modulus = 0) (i : Nat) :
    CPolynomial.eval a (xPowModWith M D modulus (ctx.p ^ i)) = a ^ (ctx.p ^ i)
```

`CompPoly.CPolynomial.Roots.FiniteField.eval_traceCoordinatePolynomialWith` (theorem, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L52))

> Trace-coordinate polynomial evaluation at a root of the modulus.

```lean
theorem eval_traceCoordinatePolynomialWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) {modulus : CPolynomial F} {a beta : F}
    (hroot : CPolynomial.eval a modulus = 0) :
    CPolynomial.eval a (traceCoordinatePolynomialWith M D ctx modulus beta) =
      ctx.traceValue (beta * a)
```

`CompPoly.CPolynomial.Roots.FiniteField.traceValue_sub` (theorem, [line 104](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L104))

> The trace power-sum is additive for subtraction.

```lean
theorem traceValue_sub {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (ctx : SmallPrimeTraceContext F) (x y : F) :
    ctx.traceValue (x - y) = ctx.traceValue x - ctx.traceValue y
```

`CompPoly.CPolynomial.Roots.FiniteField.traceValue_mul_sub_eq_zero_of_eq` (theorem, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L133))

> Trace coordinates convert equal bucket values into zero trace on differences.

```lean
theorem traceValue_mul_sub_eq_zero_of_eq {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (ctx : SmallPrimeTraceContext F) {beta a b : F}
    (htrace : ctx.traceValue (beta * a) = ctx.traceValue (beta * b)) :
    ctx.traceValue (beta * (a - b)) = 0
```

`CompPoly.CPolynomial.Roots.FiniteField.eq_of_traceValue_eq_on_basis` (theorem, [line 141](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L141))

> Matching every trace coordinate in the separating basis forces equality.

```lean
theorem eq_of_traceValue_eq_on_basis {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (ctx : SmallPrimeTraceContext F) {a b : F}
    (htrace : ∀ beta, beta ∈ ctx.basis.toList →
      ctx.traceValue (beta * a) = ctx.traceValue (beta * b)) :
    a = b
```

`CompPoly.CPolynomial.Roots.FiniteField.shoup_gcdBucket_root` (theorem, [line 152](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L152))

> The trace-coordinate gcd bucket preserves roots whose trace coordinate matches the bucket.

```lean
theorem shoup_gcdBucket_root {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) {u : CPolynomial F} {a beta c : F}
    (hroot : CPolynomial.eval a u = 0)
    (htrace : ctx.traceValue (beta * a) = c) :
    CPolynomial.eval a
        (CPolynomial.monicNormalize
          (CPolynomial.gcdMonic u
            (traceCoordinatePolynomialWith M D ctx u beta - CPolynomial.C c))) = 0
```

`CompPoly.CPolynomial.Roots.FiniteField.shoup_gcdBucket_root_iff` (theorem, [line 171](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L171))

> Roots of a trace-coordinate gcd bucket are roots of the parent in that bucket.

```lean
theorem shoup_gcdBucket_root_iff {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) {u : CPolynomial F} {a beta c : F}
    (hu : u ≠ 0) :
    CPolynomial.eval a
        (CPolynomial.monicNormalize
          (CPolynomial.gcdMonic u
            (traceCoordinatePolynomialWith M D ctx u beta - CPolynomial.C c))) = 0 ↔
      CPolynomial.eval a u = 0 ∧ ctx.traceValue (beta * a) = c
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupSplitCandidatesWith_root` (theorem, [line 806](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L806))

```lean
theorem shoupSplitCandidatesWith_root {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) {p : CPolynomial F} {a : F}
    (hp : p ≠ 0) (hroot : CPolynomial.eval a p = 0) :
    ∃ factor,
      factor ∈ (shoupSplitCandidatesWith M D ctx p).toList ∧
        factor ≠ 0 ∧
        CPolynomial.eval a factor = 0
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupSplitCandidatesWith_dvd_input` (theorem, [line 837](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L837))

```lean
theorem shoupSplitCandidatesWith_dvd_input {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) {p factor : CPolynomial F}
    (hmem : factor ∈ (shoupSplitCandidatesWith M D ctx p).toList) :
    factor.toPoly ∣ p.toPoly
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupSplitLinearFactorsWith_complete` (theorem, [line 922](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L922))

> The Shoup splitter is complete for valid root-product inputs.

```lean
theorem shoupSplitLinearFactorsWith_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) {p : CPolynomial F} {a : F}
    (hvalid : shoupSplitterInput ctx p)
    (hp : p ≠ 0) (hroot : CPolynomial.eval a p = 0) :
    ∃ factor,
      factor ∈ (shoupSplitLinearFactorsWith M D ctx p).toList ∧
        IsLinearRootFactorCandidate factor a
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupLinearFactorProductSplitterWith` (definition, [line 941](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L941))

> Adapt the Shoup trace splitter to the generic linear-factor-product interface.

```lean
def shoupLinearFactorProductSplitterWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) :
    LinearFactorProductSplitter F
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupLinearFactorProductSplitter` (definition, [line 956](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L956))

> Shoup trace splitter using the default raw multiplication and remainder backends.

```lean
def shoupLinearFactorProductSplitter {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (ctx : SmallPrimeTraceContext F) :
    LinearFactorProductSplitter F
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupLinearFactorProductSplitterWith_sound` (theorem, [line 964](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L964))

> The Shoup splitter only emits represented linear factors.

```lean
theorem shoupLinearFactorProductSplitterWith_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) {q : Nat} {p factor : CPolynomial F}
    (h : factor ∈
      ((shoupLinearFactorProductSplitterWith M D ctx).splitLinearFactors q p).toList) :
    IsLinearFactor factor
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupLinearFactorProductSplitterWith_complete` (theorem, [line 974](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L974))

> The Shoup splitter is complete for valid root-product inputs.

```lean
theorem shoupLinearFactorProductSplitterWith_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) {q : Nat} {p : CPolynomial F} {a : F}
    (hvalid : (shoupLinearFactorProductSplitterWith M D ctx).validInput q p)
    (hp : p ≠ 0) (hroot : CPolynomial.eval a p = 0) :
    ∃ factor,
      factor ∈
          ((shoupLinearFactorProductSplitterWith M D ctx).splitLinearFactors q p).toList ∧
        IsLinearRootFactorCandidate factor a
```

`CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_dvd_frobenius` (theorem, [line 1325](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L1325))

> The finite-field root product divides the finite-field Frobenius polynomial.
>
> This is the modular-gcd bridge: the executable root product uses the congruent
> modular witness `(X^q mod p) - (X mod p)` instead of materializing `X^q - X`.

```lean
theorem finiteFieldRootProductWith_dvd_frobenius {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) {p : CPolynomial F} (_hp : p ≠ 0) :
    (finiteFieldRootProductWith M D ctx.toFiniteFieldContext p).toPoly ∣
      ((Polynomial.X : Polynomial F) ^ ctx.q - Polynomial.X)
```

`CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_shoupSplitterInput` (theorem, [line 1379](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L1379))

> Finite-field root products satisfy the Shoup splitter's valid-input predicate.

```lean
theorem finiteFieldRootProductWith_shoupSplitterInput {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) {p : CPolynomial F} (hp : p ≠ 0) :
    shoupSplitterInput ctx (finiteFieldRootProductWith M D ctx.toFiniteFieldContext p)
```

`CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProduct_shoupSplitterInput` (theorem, [line 1388](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L1388))

> Default-backend finite-field root products satisfy the Shoup valid-input predicate.

```lean
theorem finiteFieldRootProduct_shoupSplitterInput {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (ctx : SmallPrimeTraceContext F) {p : CPolynomial F} (hp : p ≠ 0) :
    shoupSplitterInput ctx (finiteFieldRootProduct ctx.toFiniteFieldContext p)
```

`CompPoly.CPolynomial.Roots.FiniteField.rootProduct_satisfies_shoupSplitterInput` (theorem, [line 1396](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean#L1396))

> Alias emphasizing the root-product precondition used by Shoup completeness.

```lean
theorem rootProduct_satisfies_shoupSplitterInput {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) {p : CPolynomial F} (hp : p ≠ 0) :
    (shoupLinearFactorProductSplitterWith M D ctx).validInput ctx.q
      (finiteFieldRootProductWith M D ctx.toFiniteFieldContext p)
```

## Depends on

- [Finite-Field Root Products](../rootproduct.md)
- [Shoup-Style Small-Characteristic Linear-Factor Splitting](basic.md)

## Proof depends on

- [Finite-Field Root Correctness](../correctness.md)
- [Frobenius Divisors with One Root are Linear](frobeniuslinear.md)

## Sources

- [CompPoly/Univariate/Roots/Shoup/Correctness.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Correctness.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Univariate.Roots.Shoup.Correctness.json)
