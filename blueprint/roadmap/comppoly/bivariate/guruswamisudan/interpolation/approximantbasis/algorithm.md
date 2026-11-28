---
catalog: module
lean: CompPoly.GuruswamiSudan.ApproximantBasis.normalizeApproximantCandidate?, CompPoly.GuruswamiSudan.ApproximantBasis.approximantBasisPositiveInterpolate, CompPoly.GuruswamiSudan.ApproximantBasis.approximantBasisInterpolate
statement: formalized
proof: formalized
---

# Executable Approximant-Basis Interpolation

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.ApproximantBasis.Algorithm`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Algorithm.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Algorithm.lean), by Valerii Huhnin.

> This backend constructs the GS diagonal modular equations, calls an explicit
> solution-basis context, selects a least shifted-degree solution row, and
> normalizes the resulting bivariate polynomial.
>
> ## References
>
> * [Chowdhury, M. F. I., Jeannerod, C.-P., Neiger, V., Schost, E., and
>     Villard, G., *Faster algorithms for multivariate interpolation with
>     multiplicities and simultaneous polynomial approximations*][CJNSV15]

`CompPoly.GuruswamiSudan.ApproximantBasis.normalizeApproximantCandidate?` (definition, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Algorithm.lean#L40))

> Normalize a row-derived approximant candidate using the shared interpolation
> vector policy.

```lean
def normalizeApproximantCandidate? (params : GSInterpParams) (Q : CBivariate F) :
    Option (CBivariate F)
```

`CompPoly.GuruswamiSudan.ApproximantBasis.approximantBasisPositiveInterpolate` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Algorithm.lean#L46))

> Positive-`Y`-weight approximant-basis interpolation branch.

```lean
def approximantBasisPositiveInterpolate
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (solver : ModularSolutionBasisContext F)
    (points : Array (F × F)) (params : GSInterpParams) :
    Option (CBivariate F)
```

`CompPoly.GuruswamiSudan.ApproximantBasis.approximantBasisInterpolate` (definition, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Algorithm.lean#L70))

> Approximant-basis interpolation with the shared low-message branch.

```lean
def approximantBasisInterpolate
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (solver : ModularSolutionBasisContext F)
    (points : Array (F × F)) (params : GSInterpParams) :
    Option (CBivariate F)
```

## Depends on

- [Approximant-Basis Guruswami-Sudan Modular Data](basic.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Algorithm.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Algorithm.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.ApproximantBasis.Algorithm.json)
