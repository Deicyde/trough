---
catalog: module
lean: CompPoly.GuruswamiSudan.Hybrid.hybridPositiveInterpolate_eq_lee_or_approximant, CompPoly.GuruswamiSudan.Hybrid.hybridInterpolate_eq_lee_or_approximant, CompPoly.GuruswamiSudan.Hybrid.hybridInterpContext
statement: formalized
proof: formalized
---

# Correctness of Hybrid Guruswami-Sudan Interpolation

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.Hybrid.Correctness`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/Hybrid/Correctness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Hybrid/Correctness.lean), by Valerii Huhnin.

> The hybrid's fuel/fallback dispatch affects performance only: its result
> always coincides with the result of one of the two verified backends
> (`hybridPositiveInterpolate_eq_lee_or_approximant`). Soundness and
> completeness of `hybridInterpContext` follow by case analysis from the
> corresponding backend theorems.
>
> The only reduction-level fact needed is determinism of the fueled
> Mulders-Storjohann loop (`muldersStorjohannReduceWithFuel_eq_of_no_conflict`):
> when the budgeted probe ends without a shifted leading conflict, it stopped at
> the same matrix as the full reduction, so the kept Lee branch is literally the
> Lee-O'Sullivan backend run with the fast reducer context.

`CompPoly.GuruswamiSudan.Hybrid.hybridPositiveInterpolate_eq_lee_or_approximant` (theorem, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Hybrid/Correctness.lean#L64))

> The hybrid branch result always coincides with one of the two verified
> backends.

```lean
theorem hybridPositiveInterpolate_eq_lee_or_approximant
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (solver : ModularSolutionBasisContext F)
    (budget : GSInterpParams → Nat)
    (points : Array (F × F)) (params : GSInterpParams) :
    hybridPositiveInterpolate V E solver budget points params =
        LeeOSullivan.leeOSullivanPositiveInterpolate V E
          (muldersStorjohannFastReducerContext F) points params ∨
      hybridPositiveInterpolate V E solver budget points params =
        ApproximantBasis.approximantBasisPositiveInterpolate V E solver
          points params
```

`CompPoly.GuruswamiSudan.Hybrid.hybridInterpolate_eq_lee_or_approximant` (theorem, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Hybrid/Correctness.lean#L95))

> The hybrid result always coincides with one of the two verified
> backends.

```lean
theorem hybridInterpolate_eq_lee_or_approximant
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (solver : ModularSolutionBasisContext F)
    (budget : GSInterpParams → Nat)
    (points : Array (F × F)) (params : GSInterpParams) :
    hybridInterpolate V E solver budget points params =
        LeeOSullivan.leeOSullivanInterpolate V E
          (muldersStorjohannFastReducerContext F) points params ∨
      hybridInterpolate V E solver budget points params =
        ApproximantBasis.approximantBasisInterpolate V E solver points params
```

`CompPoly.GuruswamiSudan.Hybrid.hybridInterpContext` (definition, [line 117](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Hybrid/Correctness.lean#L117))

> Public hybrid interpolation backend context: adaptive Lee-O'Sullivan
> reduction under a step budget with an approximant-basis fallback.

```lean
def hybridInterpContext
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (solver : ModularSolutionBasisContext F)
    (budget : GSInterpParams → Nat) : GSInterpContext F
```

## Depends on

- [Hybrid Guruswami-Sudan Interpolation](algorithm.md)
- [Fast Mulders-Storjohann Reduction Agrees With the Direct Definition](../../../../linearalgebra/polynomialmatrix/muldersstorjohanncorrectness/fast.md)

## Proof depends on

- [Approximant-Basis Interpolation Correctness Surface](../approximantbasis/correctness.md)
- [Lee-O'Sullivan Interpolation Completeness](../leeosullivan/correctness/completeness.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/Hybrid/Correctness.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Hybrid/Correctness.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.Hybrid.Correctness.json)
