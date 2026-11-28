---
catalog: module
lean: CompPoly.GuruswamiSudan.koalaBearDenseInterpContext, CompPoly.GuruswamiSudan.fastKoalaBearDenseInterpContext, CompPoly.GuruswamiSudan.koalaBearNttFastMulContext, CompPoly.GuruswamiSudan.koalaBearNttFastLowMulContext, CompPoly.GuruswamiSudan.koalaBearNttFastModContext, CompPoly.GuruswamiSudan.koalaBearNttFastBatchEvalContext, CompPoly.GuruswamiSudan.fastKoalaBearNttFastMulContext, CompPoly.GuruswamiSudan.fastKoalaBearNttFastLowMulContext, CompPoly.GuruswamiSudan.fastKoalaBearNttFastModContext, CompPoly.GuruswamiSudan.fastKoalaBearNttFastBatchEvalContext, CompPoly.GuruswamiSudan.koalaBearLeeDirectInterpContext, CompPoly.GuruswamiSudan.koalaBearLeeSubproductInterpContext, CompPoly.GuruswamiSudan.fastKoalaBearLeeDirectInterpContext, CompPoly.GuruswamiSudan.fastKoalaBearLeeSubproductInterpContext, CompPoly.GuruswamiSudan.approximantPMBasisLeafCutoff, CompPoly.GuruswamiSudan.approximantPMBasisComposeLeafCutoff, CompPoly.GuruswamiSudan.koalaBearApproximantPMBasisContext, CompPoly.GuruswamiSudan.koalaBearApproximantSolutionContext, CompPoly.GuruswamiSudan.koalaBearApproximantBasisDirectInterpContext, CompPoly.GuruswamiSudan.koalaBearApproximantBasisSubproductInterpContext, CompPoly.GuruswamiSudan.koalaBearApproximantBasisInterpContext, CompPoly.GuruswamiSudan.fastKoalaBearApproximantPMBasisContext, CompPoly.GuruswamiSudan.fastKoalaBearApproximantSolutionContext, CompPoly.GuruswamiSudan.fastKoalaBearApproximantBasisDirectInterpContext, CompPoly.GuruswamiSudan.fastKoalaBearApproximantBasisSubproductInterpContext, CompPoly.GuruswamiSudan.fastKoalaBearApproximantBasisInterpContext, CompPoly.GuruswamiSudan.hybridReductionStepBudget, CompPoly.GuruswamiSudan.koalaBearHybridInterpContext, CompPoly.GuruswamiSudan.fastKoalaBearHybridInterpContext, CompPoly.GuruswamiSudan.koalaBearRothRootContext, CompPoly.GuruswamiSudan.koalaBearRothNttFastRootContext, CompPoly.GuruswamiSudan.fastKoalaBearRothRootContext, CompPoly.GuruswamiSudan.fastKoalaBearRothNttFastRootContext, CompPoly.GuruswamiSudan.koalaBearAlekhnovichRootContext, CompPoly.GuruswamiSudan.koalaBearAlekhnovichNttFastRootContext, CompPoly.GuruswamiSudan.fastKoalaBearAlekhnovichRootContext, CompPoly.GuruswamiSudan.fastKoalaBearAlekhnovichNttFastRootContext, CompPoly.GuruswamiSudan.koalaBearDenseRothContext, CompPoly.GuruswamiSudan.koalaBearDenseRothNttFastContext, CompPoly.GuruswamiSudan.fastKoalaBearDenseRothContext, CompPoly.GuruswamiSudan.fastKoalaBearDenseRothNttFastContext, CompPoly.GuruswamiSudan.koalaBearDenseRothGsCore_sound, CompPoly.GuruswamiSudan.koalaBearDenseRothGsCore_complete_of_enough_matches, CompPoly.GuruswamiSudan.koalaBearDenseRothGsFilteredCore_sound, CompPoly.GuruswamiSudan.koalaBearDenseRothGsFilteredCore_complete_of_enough_matches, CompPoly.GuruswamiSudan.koalaBearDenseRothNttFastGsCore_sound, CompPoly.GuruswamiSudan.koalaBearDenseRothNttFastGsCore_complete_of_enough_matches, CompPoly.GuruswamiSudan.koalaBearDenseRothNttFastGsFilteredCore_sound, CompPoly.GuruswamiSudan.koalaBearDenseRothNttFastGsFilteredCore_complete_of_enough_matches, CompPoly.GuruswamiSudan.fastKoalaBearDenseRothGsCore_sound, CompPoly.GuruswamiSudan.fastKoalaBearDenseRothGsCore_complete_of_enough_matches, CompPoly.GuruswamiSudan.fastKoalaBearDenseRothGsFilteredCore_sound, CompPoly.GuruswamiSudan.fastKoalaBearDenseRothGsFilteredCore_complete_of_enough_matches, CompPoly.GuruswamiSudan.fastKoalaBearDenseRothNttFastGsCore_sound, CompPoly.GuruswamiSudan.fastKoalaBearDenseRothNttFastGsCore_complete_of_enough_matches, CompPoly.GuruswamiSudan.fastKoalaBearDenseRothNttFastGsFilteredCore_sound, CompPoly.GuruswamiSudan.fastKoalaBearDenseRothNttFastGsFilteredCore_complete_of_enough_matches
statement: formalized
proof: formalized
---

# Guruswami-Sudan Concrete Implementations

`CompPoly.Bivariate.GuruswamiSudan.Implementations`, in [CompPoly/Bivariate/GuruswamiSudan/Implementations.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean), by Valerii Huhnin.

> Named concrete dense-interpolation/Roth-Ruckenstein implementations and
> correctness theorem specializations for the implementations exercised by the
> benchmark suite.

`CompPoly.GuruswamiSudan.koalaBearDenseInterpContext` (definition, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L34))

> Dense interpolation backend over canonical KoalaBear.

```lean
def koalaBearDenseInterpContext : GSInterpContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearDenseInterpContext` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L38))

> Dense interpolation backend over native-word fast KoalaBear.

```lean
def fastKoalaBearDenseInterpContext : GSInterpContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.koalaBearNttFastMulContext` (definition, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L42))

> NTTFast-backed univariate multiplication over canonical KoalaBear.

```lean
def koalaBearNttFastMulContext : CPolynomial.MulContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.koalaBearNttFastLowMulContext` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L46))

> NTTFast-backed low univariate multiplication over canonical KoalaBear.

```lean
def koalaBearNttFastLowMulContext :
    PolynomialMatrix.MulLowContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.koalaBearNttFastModContext` (definition, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L53))

> NTTFast-backed univariate monic remainders over canonical KoalaBear.

```lean
def koalaBearNttFastModContext : CPolynomial.ModContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.koalaBearNttFastBatchEvalContext` (definition, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L57))

> NTTFast-backed subproduct batch evaluation over canonical KoalaBear.

```lean
def koalaBearNttFastBatchEvalContext : CPolynomial.BatchEvalContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearNttFastMulContext` (definition, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L62))

> NTTFast-backed univariate multiplication over native-word fast KoalaBear.

```lean
def fastKoalaBearNttFastMulContext : CPolynomial.MulContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearNttFastLowMulContext` (definition, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L66))

> NTTFast-backed low univariate multiplication over native-word fast KoalaBear.

```lean
def fastKoalaBearNttFastLowMulContext :
    PolynomialMatrix.MulLowContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearNttFastModContext` (definition, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L73))

> NTTFast-backed univariate monic remainders over native-word fast KoalaBear.

```lean
def fastKoalaBearNttFastModContext : CPolynomial.ModContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearNttFastBatchEvalContext` (definition, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L77))

> NTTFast-backed subproduct batch evaluation over native-word fast KoalaBear.

```lean
def fastKoalaBearNttFastBatchEvalContext :
    CPolynomial.BatchEvalContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.koalaBearLeeDirectInterpContext` (definition, [line 83](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L83))

> Lee-O'Sullivan interpolation over canonical KoalaBear with direct vanishing setup.

```lean
def koalaBearLeeDirectInterpContext : GSInterpContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.koalaBearLeeSubproductInterpContext` (definition, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L90))

> Lee-O'Sullivan interpolation over canonical KoalaBear with subproduct-tree vanishing setup.

```lean
def koalaBearLeeSubproductInterpContext : GSInterpContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearLeeDirectInterpContext` (definition, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L98))

> Lee-O'Sullivan interpolation over native-word fast KoalaBear with direct vanishing setup.

```lean
def fastKoalaBearLeeDirectInterpContext : GSInterpContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearLeeSubproductInterpContext` (definition, [line 106](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L106))

> Lee-O'Sullivan interpolation over native-word fast KoalaBear with
> subproduct-tree vanishing setup.

```lean
def fastKoalaBearLeeSubproductInterpContext : GSInterpContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.approximantPMBasisLeafCutoff` (definition, [line 118](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L118))

> PM-basis scalar-kernel cutoff for the approximant-basis interpolation backend.
>
> The recursive solver handles all larger orders with low-product residuals and
> block matrix composition; dense scalar linear algebra is reserved for
> small bounded leaves.

```lean
def approximantPMBasisLeafCutoff : Nat
```

`CompPoly.GuruswamiSudan.approximantPMBasisComposeLeafCutoff` (definition, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L123))

> Polynomial-matrix basis-composition cutoff for the approximant backend.
> The current GS interpolation shapes are narrow enough that direct bounded
> composition is faster than recursing Strassen down to unit blocks.

```lean
def approximantPMBasisComposeLeafCutoff : Nat
```

`CompPoly.GuruswamiSudan.koalaBearApproximantPMBasisContext` (definition, [line 126](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L126))

> Recursive approximant-basis PM-basis context over canonical KoalaBear.

```lean
def koalaBearApproximantPMBasisContext :
    PolynomialMatrix.Approximant.PMBasisContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.koalaBearApproximantSolutionContext` (definition, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L133))

> Diagonal modular-equation solution context over canonical KoalaBear.

```lean
def koalaBearApproximantSolutionContext :
    PolynomialMatrix.Approximant.ModularSolutionBasisContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.koalaBearApproximantBasisDirectInterpContext` (definition, [line 140](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L140))

> Approximant-basis interpolation over canonical KoalaBear.

```lean
def koalaBearApproximantBasisDirectInterpContext : GSInterpContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.koalaBearApproximantBasisSubproductInterpContext` (definition, [line 148](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L148))

> Approximant-basis interpolation over canonical KoalaBear with
> subproduct-tree vanishing setup.

```lean
def koalaBearApproximantBasisSubproductInterpContext : GSInterpContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.koalaBearApproximantBasisInterpContext` (definition, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L156))

> Default approximant-basis interpolation over canonical KoalaBear.

```lean
def koalaBearApproximantBasisInterpContext : GSInterpContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearApproximantPMBasisContext` (definition, [line 160](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L160))

> Recursive approximant-basis PM-basis context over native-word fast KoalaBear.

```lean
def fastKoalaBearApproximantPMBasisContext :
    PolynomialMatrix.Approximant.PMBasisContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearApproximantSolutionContext` (definition, [line 167](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L167))

> Diagonal modular-equation solution context over native-word fast KoalaBear.

```lean
def fastKoalaBearApproximantSolutionContext :
    PolynomialMatrix.Approximant.ModularSolutionBasisContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearApproximantBasisDirectInterpContext` (definition, [line 174](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L174))

> Approximant-basis interpolation over native-word fast KoalaBear.

```lean
def fastKoalaBearApproximantBasisDirectInterpContext :
    GSInterpContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearApproximantBasisSubproductInterpContext` (definition, [line 183](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L183))

> Approximant-basis interpolation over native-word fast KoalaBear with
> subproduct-tree vanishing setup.

```lean
def fastKoalaBearApproximantBasisSubproductInterpContext :
    GSInterpContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearApproximantBasisInterpContext` (definition, [line 192](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L192))

> Default approximant-basis interpolation over native-word fast KoalaBear.

```lean
def fastKoalaBearApproximantBasisInterpContext :
    GSInterpContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.hybridReductionStepBudget` (definition, [line 202](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L202))

> Mulders-Storjohann step budget for the hybrid interpolation backend: the
> ski-rental rent/buy break-even, set near the cost ratio between one
> approximant-fallback solve and one reduction step. Both scale with the input
> mass, so the ratio is proportional to `ℓ^(ω−1)` (with `ℓ + 1` the module
> width) and independent of `n` and `m` under softly-linear multiplication;
> the constant is calibrated from the `n = 5040` long-code benchmark shape.

```lean
def hybridReductionStepBudget (params : GSInterpParams) : Nat
```

`CompPoly.GuruswamiSudan.koalaBearHybridInterpContext` (definition, [line 207](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L207))

> Hybrid interpolation (budgeted Lee-O'Sullivan reduction with approximant
> fallback) over canonical KoalaBear.

```lean
def koalaBearHybridInterpContext : GSInterpContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearHybridInterpContext` (definition, [line 216](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L216))

> Hybrid interpolation (budgeted Lee-O'Sullivan reduction with approximant
> fallback) over native-word fast KoalaBear.

```lean
def fastKoalaBearHybridInterpContext : GSInterpContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.koalaBearRothRootContext` (definition, [line 225](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L225))

> Roth-Ruckenstein root backend over canonical KoalaBear.

```lean
def koalaBearRothRootContext : GSRootContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.koalaBearRothNttFastRootContext` (definition, [line 229](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L229))

> Roth-Ruckenstein root backend over canonical KoalaBear with NTTFast field roots.

```lean
def koalaBearRothNttFastRootContext : GSRootContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearRothRootContext` (definition, [line 233](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L233))

> Roth-Ruckenstein root backend over native-word fast KoalaBear.

```lean
def fastKoalaBearRothRootContext : GSRootContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearRothNttFastRootContext` (definition, [line 237](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L237))

> Roth-Ruckenstein root backend over native-word fast KoalaBear with NTTFast field roots.

```lean
def fastKoalaBearRothNttFastRootContext : GSRootContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.koalaBearAlekhnovichRootContext` (definition, [line 241](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L241))

> Alekhnovich root backend over canonical KoalaBear.

```lean
def koalaBearAlekhnovichRootContext : GSRootContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.koalaBearAlekhnovichNttFastRootContext` (definition, [line 245](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L245))

> Alekhnovich root backend over canonical KoalaBear with NTTFast field roots.

```lean
def koalaBearAlekhnovichNttFastRootContext : GSRootContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearAlekhnovichRootContext` (definition, [line 249](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L249))

> Alekhnovich root backend over native-word fast KoalaBear.

```lean
def fastKoalaBearAlekhnovichRootContext : GSRootContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearAlekhnovichNttFastRootContext` (definition, [line 253](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L253))

> Alekhnovich root backend over native-word fast KoalaBear with NTTFast field roots.

```lean
def fastKoalaBearAlekhnovichNttFastRootContext : GSRootContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.koalaBearDenseRothContext` (definition, [line 257](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L257))

> Filtered dense/Roth context over canonical KoalaBear.

```lean
def koalaBearDenseRothContext : GSFilteredCoreContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.koalaBearDenseRothNttFastContext` (definition, [line 261](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L261))

> Filtered dense/Roth context over canonical KoalaBear with NTTFast field roots.

```lean
def koalaBearDenseRothNttFastContext : GSFilteredCoreContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearDenseRothContext` (definition, [line 266](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L266))

> Filtered dense/Roth context over native-word fast KoalaBear.

```lean
def fastKoalaBearDenseRothContext : GSFilteredCoreContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearDenseRothNttFastContext` (definition, [line 271](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L271))

> Filtered dense/Roth context over native-word fast KoalaBear with NTTFast field roots.

```lean
def fastKoalaBearDenseRothNttFastContext : GSFilteredCoreContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.koalaBearDenseRothGsCore_sound` (theorem, [line 276](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L276))

> Concrete soundness for the canonical KoalaBear dense/Roth core.

```lean
theorem koalaBearDenseRothGsCore_sound {points : Array (KoalaBear.Field × KoalaBear.Field)}
    {params : GSInterpParams} {p : CPolynomial KoalaBear.Field}
    (hp : p ∈ (gsCore points koalaBearDenseInterpContext koalaBearRothRootContext params).toList) :
    ∃ Q,
      koalaBearDenseInterpContext.interpolate points params = some Q ∧
        ValidInterpolationWitness points params Q ∧
          degreeLt p params.messageDegree ∧
            CBivariate.composeY Q p = 0
```

`CompPoly.GuruswamiSudan.koalaBearDenseRothGsCore_complete_of_enough_matches` (theorem, [line 288](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L288))

> Concrete completeness for the canonical KoalaBear dense/Roth core.

```lean
theorem koalaBearDenseRothGsCore_complete_of_enough_matches
    {points : Array (KoalaBear.Field × KoalaBear.Field)}
    {params : GSInterpParams} {p : CPolynomial KoalaBear.Field}
    (hInterpExists : ∃ Q, ValidInterpolationWitness points params Q)
    (hpdeg : degreeLt p params.messageDegree)
    (hdistinct : DistinctXCoordinates points)
    (hmatches : params.weightedDegreeBound < params.multiplicity * matchingPointCount points p) :
    p ∈ (gsCore points koalaBearDenseInterpContext koalaBearRothRootContext params).toList
```

`CompPoly.GuruswamiSudan.koalaBearDenseRothGsFilteredCore_sound` (theorem, [line 300](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L300))

> Concrete soundness for the canonical KoalaBear dense/Roth filtered core.

```lean
theorem koalaBearDenseRothGsFilteredCore_sound
    {points : Array (KoalaBear.Field × KoalaBear.Field)}
    {params : GSInterpParams} {radius : Nat} {p : CPolynomial KoalaBear.Field}
    (hp :
      p ∈ (gsFilteredCore points koalaBearDenseInterpContext koalaBearRothRootContext
        params radius).toList) :
    ∃ Q,
      koalaBearDenseInterpContext.interpolate points params = some Q ∧
        ValidInterpolationWitness points params Q ∧
          degreeLt p params.messageDegree ∧
            CBivariate.composeY Q p = 0 ∧
              candidateMismatchCount points p ≤ radius
```

`CompPoly.GuruswamiSudan.koalaBearDenseRothGsFilteredCore_complete_of_enough_matches` (theorem, [line 316](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L316))

> Concrete completeness for the canonical KoalaBear dense/Roth filtered core.

```lean
theorem koalaBearDenseRothGsFilteredCore_complete_of_enough_matches
    {points : Array (KoalaBear.Field × KoalaBear.Field)}
    {params : GSInterpParams} {radius : Nat} {p : CPolynomial KoalaBear.Field}
    (hInterpExists : ∃ Q, ValidInterpolationWitness points params Q)
    (hpdeg : degreeLt p params.messageDegree)
    (hdistinct : DistinctXCoordinates points)
    (hmatches : params.weightedDegreeBound < params.multiplicity * matchingPointCount points p)
    (hpass : passesCandidateDistance points radius p = true) :
    p ∈ (gsFilteredCore points koalaBearDenseInterpContext koalaBearRothRootContext
      params radius).toList
```

`CompPoly.GuruswamiSudan.koalaBearDenseRothNttFastGsCore_sound` (theorem, [line 330](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L330))

> Concrete soundness for the canonical KoalaBear dense/Roth-NTTFast core.

```lean
theorem koalaBearDenseRothNttFastGsCore_sound
    {points : Array (KoalaBear.Field × KoalaBear.Field)}
    {params : GSInterpParams} {p : CPolynomial KoalaBear.Field}
    (hp :
      p ∈ (gsCore points koalaBearDenseInterpContext koalaBearRothNttFastRootContext
        params).toList) :
    ∃ Q,
      koalaBearDenseInterpContext.interpolate points params = some Q ∧
        ValidInterpolationWitness points params Q ∧
          degreeLt p params.messageDegree ∧
            CBivariate.composeY Q p = 0
```

`CompPoly.GuruswamiSudan.koalaBearDenseRothNttFastGsCore_complete_of_enough_matches` (theorem, [line 345](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L345))

> Concrete completeness for the canonical KoalaBear dense/Roth-NTTFast core.

```lean
theorem koalaBearDenseRothNttFastGsCore_complete_of_enough_matches
    {points : Array (KoalaBear.Field × KoalaBear.Field)}
    {params : GSInterpParams} {p : CPolynomial KoalaBear.Field}
    (hInterpExists : ∃ Q, ValidInterpolationWitness points params Q)
    (hpdeg : degreeLt p params.messageDegree)
    (hdistinct : DistinctXCoordinates points)
    (hmatches : params.weightedDegreeBound < params.multiplicity * matchingPointCount points p) :
    p ∈ (gsCore points koalaBearDenseInterpContext koalaBearRothNttFastRootContext params).toList
```

`CompPoly.GuruswamiSudan.koalaBearDenseRothNttFastGsFilteredCore_sound` (theorem, [line 357](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L357))

> Concrete soundness for the canonical KoalaBear dense/Roth-NTTFast filtered core.

```lean
theorem koalaBearDenseRothNttFastGsFilteredCore_sound
    {points : Array (KoalaBear.Field × KoalaBear.Field)}
    {params : GSInterpParams} {radius : Nat} {p : CPolynomial KoalaBear.Field}
    (hp :
      p ∈ (gsFilteredCore points koalaBearDenseInterpContext koalaBearRothNttFastRootContext
        params radius).toList) :
    ∃ Q,
      koalaBearDenseInterpContext.interpolate points params = some Q ∧
        ValidInterpolationWitness points params Q ∧
          degreeLt p params.messageDegree ∧
            CBivariate.composeY Q p = 0 ∧
              candidateMismatchCount points p ≤ radius
```

`CompPoly.GuruswamiSudan.koalaBearDenseRothNttFastGsFilteredCore_complete_of_enough_matches` (theorem, [line 373](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L373))

> Concrete completeness for the canonical KoalaBear dense/Roth-NTTFast filtered core.

```lean
theorem koalaBearDenseRothNttFastGsFilteredCore_complete_of_enough_matches
    {points : Array (KoalaBear.Field × KoalaBear.Field)}
    {params : GSInterpParams} {radius : Nat} {p : CPolynomial KoalaBear.Field}
    (hInterpExists : ∃ Q, ValidInterpolationWitness points params Q)
    (hpdeg : degreeLt p params.messageDegree)
    (hdistinct : DistinctXCoordinates points)
    (hmatches : params.weightedDegreeBound < params.multiplicity * matchingPointCount points p)
    (hpass : passesCandidateDistance points radius p = true) :
    p ∈ (gsFilteredCore points koalaBearDenseInterpContext koalaBearRothNttFastRootContext
      params radius).toList
```

`CompPoly.GuruswamiSudan.fastKoalaBearDenseRothGsCore_sound` (theorem, [line 387](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L387))

> Concrete soundness for the fast KoalaBear dense/Roth core.

```lean
theorem fastKoalaBearDenseRothGsCore_sound
    {points : Array (KoalaBear.Fast.Field × KoalaBear.Fast.Field)}
    {params : GSInterpParams} {p : CPolynomial KoalaBear.Fast.Field}
    (hp :
      p ∈ (gsCore points fastKoalaBearDenseInterpContext fastKoalaBearRothRootContext
        params).toList) :
    ∃ Q,
      fastKoalaBearDenseInterpContext.interpolate points params = some Q ∧
        ValidInterpolationWitness points params Q ∧
          degreeLt p params.messageDegree ∧
            CBivariate.composeY Q p = 0
```

`CompPoly.GuruswamiSudan.fastKoalaBearDenseRothGsCore_complete_of_enough_matches` (theorem, [line 402](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L402))

> Concrete completeness for the fast KoalaBear dense/Roth core.

```lean
theorem fastKoalaBearDenseRothGsCore_complete_of_enough_matches
    {points : Array (KoalaBear.Fast.Field × KoalaBear.Fast.Field)}
    {params : GSInterpParams} {p : CPolynomial KoalaBear.Fast.Field}
    (hInterpExists : ∃ Q, ValidInterpolationWitness points params Q)
    (hpdeg : degreeLt p params.messageDegree)
    (hdistinct : DistinctXCoordinates points)
    (hmatches : params.weightedDegreeBound < params.multiplicity * matchingPointCount points p) :
    p ∈ (gsCore points fastKoalaBearDenseInterpContext fastKoalaBearRothRootContext
      params).toList
```

`CompPoly.GuruswamiSudan.fastKoalaBearDenseRothGsFilteredCore_sound` (theorem, [line 415](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L415))

> Concrete soundness for the fast KoalaBear dense/Roth filtered core.

```lean
theorem fastKoalaBearDenseRothGsFilteredCore_sound
    {points : Array (KoalaBear.Fast.Field × KoalaBear.Fast.Field)}
    {params : GSInterpParams} {radius : Nat} {p : CPolynomial KoalaBear.Fast.Field}
    (hp :
      p ∈ (gsFilteredCore points fastKoalaBearDenseInterpContext fastKoalaBearRothRootContext
        params radius).toList) :
    ∃ Q,
      fastKoalaBearDenseInterpContext.interpolate points params = some Q ∧
        ValidInterpolationWitness points params Q ∧
          degreeLt p params.messageDegree ∧
            CBivariate.composeY Q p = 0 ∧
              candidateMismatchCount points p ≤ radius
```

`CompPoly.GuruswamiSudan.fastKoalaBearDenseRothGsFilteredCore_complete_of_enough_matches` (theorem, [line 431](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L431))

> Concrete completeness for the fast KoalaBear dense/Roth filtered core.

```lean
theorem fastKoalaBearDenseRothGsFilteredCore_complete_of_enough_matches
    {points : Array (KoalaBear.Fast.Field × KoalaBear.Fast.Field)}
    {params : GSInterpParams} {radius : Nat} {p : CPolynomial KoalaBear.Fast.Field}
    (hInterpExists : ∃ Q, ValidInterpolationWitness points params Q)
    (hpdeg : degreeLt p params.messageDegree)
    (hdistinct : DistinctXCoordinates points)
    (hmatches : params.weightedDegreeBound < params.multiplicity * matchingPointCount points p)
    (hpass : passesCandidateDistance points radius p = true) :
    p ∈ (gsFilteredCore points fastKoalaBearDenseInterpContext fastKoalaBearRothRootContext
      params radius).toList
```

`CompPoly.GuruswamiSudan.fastKoalaBearDenseRothNttFastGsCore_sound` (theorem, [line 445](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L445))

> Concrete soundness for the fast KoalaBear dense/Roth-NTTFast core.

```lean
theorem fastKoalaBearDenseRothNttFastGsCore_sound
    {points : Array (KoalaBear.Fast.Field × KoalaBear.Fast.Field)}
    {params : GSInterpParams} {p : CPolynomial KoalaBear.Fast.Field}
    (hp :
      p ∈ (gsCore points fastKoalaBearDenseInterpContext fastKoalaBearRothNttFastRootContext
        params).toList) :
    ∃ Q,
      fastKoalaBearDenseInterpContext.interpolate points params = some Q ∧
        ValidInterpolationWitness points params Q ∧
          degreeLt p params.messageDegree ∧
            CBivariate.composeY Q p = 0
```

`CompPoly.GuruswamiSudan.fastKoalaBearDenseRothNttFastGsCore_complete_of_enough_matches` (theorem, [line 460](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L460))

> Concrete completeness for the fast KoalaBear dense/Roth-NTTFast core.

```lean
theorem fastKoalaBearDenseRothNttFastGsCore_complete_of_enough_matches
    {points : Array (KoalaBear.Fast.Field × KoalaBear.Fast.Field)}
    {params : GSInterpParams} {p : CPolynomial KoalaBear.Fast.Field}
    (hInterpExists : ∃ Q, ValidInterpolationWitness points params Q)
    (hpdeg : degreeLt p params.messageDegree)
    (hdistinct : DistinctXCoordinates points)
    (hmatches : params.weightedDegreeBound < params.multiplicity * matchingPointCount points p) :
    p ∈ (gsCore points fastKoalaBearDenseInterpContext fastKoalaBearRothNttFastRootContext
      params).toList
```

`CompPoly.GuruswamiSudan.fastKoalaBearDenseRothNttFastGsFilteredCore_sound` (theorem, [line 473](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L473))

> Concrete soundness for the fast KoalaBear dense/Roth-NTTFast filtered core.

```lean
theorem fastKoalaBearDenseRothNttFastGsFilteredCore_sound
    {points : Array (KoalaBear.Fast.Field × KoalaBear.Fast.Field)}
    {params : GSInterpParams} {radius : Nat} {p : CPolynomial KoalaBear.Fast.Field}
    (hp :
      p ∈ (gsFilteredCore points fastKoalaBearDenseInterpContext
        fastKoalaBearRothNttFastRootContext params radius).toList) :
    ∃ Q,
      fastKoalaBearDenseInterpContext.interpolate points params = some Q ∧
        ValidInterpolationWitness points params Q ∧
          degreeLt p params.messageDegree ∧
            CBivariate.composeY Q p = 0 ∧
              candidateMismatchCount points p ≤ radius
```

`CompPoly.GuruswamiSudan.fastKoalaBearDenseRothNttFastGsFilteredCore_complete_of_enough_matches` (theorem, [line 489](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean#L489))

> Concrete completeness for the fast KoalaBear dense/Roth-NTTFast filtered core.

```lean
theorem fastKoalaBearDenseRothNttFastGsFilteredCore_complete_of_enough_matches
    {points : Array (KoalaBear.Fast.Field × KoalaBear.Fast.Field)}
    {params : GSInterpParams} {radius : Nat} {p : CPolynomial KoalaBear.Fast.Field}
    (hInterpExists : ∃ Q, ValidInterpolationWitness points params Q)
    (hpdeg : degreeLt p params.messageDegree)
    (hdistinct : DistinctXCoordinates points)
    (hmatches : params.weightedDegreeBound < params.multiplicity * matchingPointCount points p)
    (hpass : passesCandidateDistance points radius p = true) :
    p ∈ (gsFilteredCore points fastKoalaBearDenseInterpContext
      fastKoalaBearRothNttFastRootContext params radius).toList
```

## Depends on

- [Guruswami-Sudan Executable Decoder](executable.md)
- [Approximant-Basis Interpolation Correctness Surface](interpolation/approximantbasis/correctness.md)
- [Dense Guruswami-Sudan Interpolation Correctness](interpolation/dense/correctness.md)
- [Correctness of Hybrid Guruswami-Sudan Interpolation](interpolation/hybrid/correctness.md)
- [Lee-O'Sullivan Interpolation Completeness](interpolation/leeosullivan/correctness/completeness.md)
- [Alekhnovich Root Search Correctness](root/alekhnovich/correctness.md)
- [KoalaBear Guruswami-Sudan Field-Root Backends](root/fieldroots-2/koalabear.md)
- [Roth-Ruckenstein Root Correctness](root/rothruckenstein/correctness.md)
- [Diagonal Modular Equation Solver Context](../../linearalgebra/polynomialmatrix/approximant/modularequation.md)
- [Recursive PM-Basis](../../linearalgebra/polynomialmatrix/approximant/pmbasis.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Implementations.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Implementations.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Implementations.json)
