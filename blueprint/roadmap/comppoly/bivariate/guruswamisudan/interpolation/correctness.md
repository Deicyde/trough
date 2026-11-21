---
catalog: module
lean: CompPoly.GuruswamiSudan.interpolationWitnessIsValidBool_iff, CompPoly.GuruswamiSudan.lowMessageDegreeInterpolation_sound
statement: formalized
proof: formalized
---

# Shared Guruswami-Sudan Interpolation Correctness

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.Correctness`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/Correctness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Correctness.lean), by Valerii Huhnin.

> Backend-neutral correctness facts for executable interpolation helpers.

`CompPoly.GuruswamiSudan.interpolationWitnessIsValidBool_iff` (theorem, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Correctness.lean#L26))

> The executable witness recognizer is equivalent to the semantic witness contract.

```lean
theorem interpolationWitnessIsValidBool_iff {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {points : Array (F × F)} {params : GSInterpParams} {Q : CBivariate F} :
    interpolationWitnessIsValidBool points params Q = true ↔
      ValidInterpolationWitness points params Q
```

`CompPoly.GuruswamiSudan.lowMessageDegreeInterpolation_sound` (theorem, [line 287](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Correctness.lean#L287))

> Constructive low-message interpolation returns a semantic GS interpolation witness.

```lean
theorem lowMessageDegreeInterpolation_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {points : Array (Prod F F)} {params : GSInterpParams}
    (hLow : params.messageDegree ≤ 1) :
    let Q := lowMessageDegreeInterpolation points params.multiplicity
    ValidInterpolationWitness points params Q
```

## Depends on

- [Guruswami-Sudan Interpolation Basics](basic.md)

## Proof depends on

- [Guruswami-Sudan Polynomial Correctness Lemmas](../polynomialcorrectness.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/Correctness.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Correctness.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.Correctness.json)
