---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitLinearFactorsWith_complete, CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitLinearFactorsWithTrace_complete, CompPoly.CPolynomial.Roots.FiniteField.lasVegasLinearFactorProductSplitterWith, CompPoly.CPolynomial.Roots.FiniteField.lasVegasLinearFactorProductSplitterWithTrace, CompPoly.CPolynomial.Roots.FiniteField.rootProduct_satisfies_lasVegasSplitterInput
statement: formalized
proof: formalized
---

# Loop Correctness Surface for Las Vegas Splitting

`CompPoly.Univariate.Roots.LasVegas.Correctness.Loop`, in [CompPoly/Univariate/Roots/LasVegas/Correctness/Loop.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Loop.lean), by Valerii Huhnin.

> Completeness and packaging lemmas for the bounded Las Vegas splitter loop and
> its enumeration fallback.

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitLinearFactorsWith_complete` (theorem, [line 424](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Loop.lean#L424))

> Completeness surface for bounded Las Vegas splitting plus enumeration fallback.

```lean
theorem lasVegasSplitLinearFactorsWith_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (cfg : LasVegasConfig)
    (probes : ProbeFamily F) (q : Nat)
    {p : CPolynomial F} {a : F}
    (hvalid : lasVegasSplitterInput q p) (hp : p ≠ 0)
    (hroot : CPolynomial.eval a p = 0) :
    ∃ factor,
      factor ∈
          (lasVegasSplitLinearFactorsWith M D enumeration cfg probes q p).toList ∧
        IsLinearRootFactorCandidate factor a
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitLinearFactorsWithTrace_complete` (theorem, [line 441](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Loop.lean#L441))

> Completeness surface for bounded Las Vegas splitting with characteristic-two trace metadata.

```lean
theorem lasVegasSplitLinearFactorsWithTrace_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (traceCtx : SmallPrimeTraceContext F)
    (cfg : LasVegasConfig) (probes : ProbeFamily F) (q : Nat)
    {p : CPolynomial F} {a : F}
    (hvalid : lasVegasSplitterInput q p) (hp : p ≠ 0)
    (hroot : CPolynomial.eval a p = 0) :
    ∃ factor,
      factor ∈
          (lasVegasSplitLinearFactorsWithTrace M D enumeration traceCtx cfg probes q p).toList ∧
        IsLinearRootFactorCandidate factor a
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasLinearFactorProductSplitterWith` (definition, [line 458](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Loop.lean#L458))

> Package bounded Las Vegas splitting as a finite-field linear-factor splitter.

```lean
def lasVegasLinearFactorProductSplitterWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (_ctx : FiniteFieldContext F) (enumeration : FieldEnumeration F)
    (cfg : LasVegasConfig) (probes : ProbeFamily F) :
    LinearFactorProductSplitter F
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasLinearFactorProductSplitterWithTrace` (definition, [line 476](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Loop.lean#L476))

> Package bounded Las Vegas trace splitting as a finite-field linear-factor splitter.

```lean
def lasVegasLinearFactorProductSplitterWithTrace {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (_ctx : FiniteFieldContext F) (enumeration : FieldEnumeration F)
    (traceCtx : SmallPrimeTraceContext F)
    (cfg : LasVegasConfig) (probes : ProbeFamily F) :
    LinearFactorProductSplitter F
```

`CompPoly.CPolynomial.Roots.FiniteField.rootProduct_satisfies_lasVegasSplitterInput` (theorem, [line 495](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Loop.lean#L495))

> Alias emphasizing the root-product precondition used by Las Vegas completeness.

```lean
theorem rootProduct_satisfies_lasVegasSplitterInput {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : FiniteFieldContext F) (enumeration : FieldEnumeration F)
    (cfg : LasVegasConfig) (probes : ProbeFamily F)
    {p : CPolynomial F} (hp : p ≠ 0) :
    (lasVegasLinearFactorProductSplitterWith M D ctx enumeration cfg probes).validInput ctx.q
      (finiteFieldRootProductWith M D ctx p)
```

## Depends on

- [Las Vegas Linear-Factor Splitting](../basic.md)
- [Finite-Field Root Products](../../rootproduct.md)

## Proof depends on

- [Even-Trace Split Correctness for Las Vegas Splitting](eventrace.md)
- [Odd Split Correctness for Las Vegas Splitting](odd.md)

## Sources

- [CompPoly/Univariate/Roots/LasVegas/Correctness/Loop.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Loop.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Univariate.Roots.LasVegas.Correctness.Loop.json)
