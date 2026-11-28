---
catalog: module
lean: CompPoly.GuruswamiSudan.finiteFieldRootContextWith, CompPoly.GuruswamiSudan.finiteFieldRootContext, CompPoly.GuruswamiSudan.smoothFiniteFieldRootContextWith, CompPoly.GuruswamiSudan.smoothFiniteFieldRootContext
statement: formalized
proof: formalized
---

# Guruswami-Sudan Finite-Field Root Adapter

`CompPoly.Bivariate.GuruswamiSudan.Root.FieldRoots.FiniteField`, in [CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/FiniteField.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/FiniteField.lean), by Valerii Huhnin.

> Adapter from the reusable finite-field univariate root operation to the certified
> `FieldRootContext` context consumed by Roth-Ruckenstein root finding.

`CompPoly.GuruswamiSudan.finiteFieldRootContextWith` (definition, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/FiniteField.lean#L26))

> Package the generic finite-field root finder as a GS field-root backend.

```lean
def finiteFieldRootContextWith (F : Type*) [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : CPolynomial.Roots.FiniteField.FiniteFieldContext F)
    (splitter : CPolynomial.Roots.FiniteField.LinearFactorProductSplitter F)
    (splitterValid :
      ∀ {p : CPolynomial F}, p ≠ 0 →
        splitter.validInput ctx.q
          (CPolynomial.Roots.FiniteField.finiteFieldRootProductWith M D ctx p)) :
    FieldRootContext F
```

`CompPoly.GuruswamiSudan.finiteFieldRootContext` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/FiniteField.lean#L45))

> Package the generic finite-field root finder with the default raw arithmetic backends.

```lean
def finiteFieldRootContext (F : Type*) [Field F] [BEq F] [LawfulBEq F]
    (ctx : CPolynomial.Roots.FiniteField.FiniteFieldContext F)
    (splitter : CPolynomial.Roots.FiniteField.LinearFactorProductSplitter F)
    (splitterValid :
      ∀ {p : CPolynomial F}, p ≠ 0 →
        splitter.validInput ctx.q (CPolynomial.Roots.FiniteField.finiteFieldRootProduct ctx p)) :
    FieldRootContext F
```

`CompPoly.GuruswamiSudan.smoothFiniteFieldRootContextWith` (definition, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/FiniteField.lean#L58))

> Package a smooth cyclic splitter as a GS field-root backend.

```lean
def smoothFiniteFieldRootContextWith (F : Type*) [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : CPolynomial.Roots.FiniteField.FiniteFieldContext F)
    (smoothCtx : CPolynomial.Roots.FiniteField.SmoothCyclicRootContext F)
    (smoothValid :
      ∀ {p : CPolynomial F}, p ≠ 0 →
        smoothCtx.validInput
          (CPolynomial.Roots.FiniteField.finiteFieldRootProductWith M D ctx p)) :
    FieldRootContext F
```

`CompPoly.GuruswamiSudan.smoothFiniteFieldRootContext` (definition, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/FiniteField.lean#L74))

> Package a smooth cyclic splitter with default raw arithmetic as a GS field-root backend.

```lean
def smoothFiniteFieldRootContext (F : Type*) [Field F] [BEq F] [LawfulBEq F]
    (ctx : CPolynomial.Roots.FiniteField.FiniteFieldContext F)
    (smoothCtx : CPolynomial.Roots.FiniteField.SmoothCyclicRootContext F)
    (smoothValid :
      ∀ {p : CPolynomial F}, p ≠ 0 →
        smoothCtx.validInput
          (CPolynomial.Roots.FiniteField.finiteFieldRootProduct ctx p)) :
    FieldRootContext F
```

## Depends on

- [Guruswami-Sudan Backend Contexts](../../context.md)
- [Finite-Field Root Backend](../../../../univariate/part-02/roots/backend.md)
- [Smooth Multiplicative-Subgroup Linear-Factor Splitting](../../../../univariate/part-02/roots/smoothsubgroup/basic.md)

## Proof depends on

- [Finite-Field Root Correctness](../../../../univariate/part-02/roots/correctness.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/FiniteField.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/FiniteField.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Root.FieldRoots.FiniteField.json)
