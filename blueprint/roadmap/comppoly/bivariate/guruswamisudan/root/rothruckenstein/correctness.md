---
catalog: module
lean: CompPoly.GuruswamiSudan.rothRuckensteinRootsYDegreeLt_sound, CompPoly.GuruswamiSudan.initialCoefficientPolynomial_stripXAdicFactor_ne_zero, CompPoly.GuruswamiSudan.rothRuckensteinRootsYDegreeLt_complete, CompPoly.GuruswamiSudan.rothRuckensteinRootContext, CompPoly.GuruswamiSudan.transformedRothRuckensteinRootContext
statement: formalized
proof: formalized
---

# Roth-Ruckenstein Root Correctness

`CompPoly.Bivariate.GuruswamiSudan.Root.RothRuckenstein.Correctness`, in [CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Correctness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Correctness.lean), by Valerii Huhnin.

> Correctness statements for the Roth-Ruckenstein root backend.

`CompPoly.GuruswamiSudan.rothRuckensteinRootsYDegreeLt_sound` (theorem, [line 24](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Correctness.lean#L24))

> Soundness of Roth-Ruckenstein root filtering.

```lean
theorem rothRuckensteinRootsYDegreeLt_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {fieldRoots : FieldRootContext F} {Q : CBivariate F} {k : Nat}
    {p : CPolynomial F}
    (h : p ∈ (rothRuckensteinRootsYDegreeLt fieldRoots Q k).toList) :
    degreeLt p k ∧ CBivariate.composeY Q p = 0
```

`CompPoly.GuruswamiSudan.initialCoefficientPolynomial_stripXAdicFactor_ne_zero` (theorem, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Correctness.lean#L36))

> Normalizing a nonzero bivariate polynomial exposes a nonzero initial
> coefficient equation for the residual-transform RR step.

```lean
theorem initialCoefficientPolynomial_stripXAdicFactor_ne_zero {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {Q : CBivariate F} (hQ : Q ≠ 0) :
    initialCoefficientPolynomial (CBivariate.stripXAdicFactor Q) ≠ 0
```

`CompPoly.GuruswamiSudan.rothRuckensteinRootsYDegreeLt_complete` (theorem, [line 870](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Correctness.lean#L870))

> Completeness of Roth-Ruckenstein root finding from a complete field-root backend.
>
> The nonzero-input hypothesis matches the backend completeness contract, which
> only promises finite output for nonzero bivariate equations.

```lean
theorem rothRuckensteinRootsYDegreeLt_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {fieldRoots : FieldRootContext F}
    {Q : CBivariate F} {k : Nat} {p : CPolynomial F}
    (hQ : Q ≠ 0) (hdegree : degreeLt p k) (hroot : CBivariate.composeY Q p = 0) :
    p ∈ (rothRuckensteinRootsYDegreeLt fieldRoots Q k).toList
```

`CompPoly.GuruswamiSudan.rothRuckensteinRootContext` (definition, [line 888](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Correctness.lean#L888))

> Roth-Ruckenstein roots packaged with an explicit univariate field-root backend.

```lean
def rothRuckensteinRootContext (F : Type*)
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (fieldRoots : FieldRootContext F) : GSRootContext F
```

`CompPoly.GuruswamiSudan.transformedRothRuckensteinRootContext` (definition, [line 901](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Correctness.lean#L901))

> Residual-transform Roth-Ruckenstein roots packaged as a backend.

```lean
def transformedRothRuckensteinRootContext (F : Type*)
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (fieldRoots : FieldRootContext F) : GSRootContext F
```

## Depends on

- [Roth-Ruckenstein-Style Root Finding](algorithm.md)

## Proof depends on

- [Guruswami-Sudan Polynomial Correctness Lemmas](../../polynomialcorrectness.md)
- [Roth-Ruckenstein Correctness Support](lemmas.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Correctness.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Correctness.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Root.RothRuckenstein.Correctness.json)
