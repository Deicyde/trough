---
catalog: module
lean: CompPoly.GuruswamiSudan.ApproximantBasis.gsModularEquation_row_iff_multiplicity, CompPoly.GuruswamiSudan.ApproximantBasis.approximantBasisInterpolate_sound, CompPoly.GuruswamiSudan.ApproximantBasis.approximantBasisInterpolate_complete, CompPoly.GuruswamiSudan.ApproximantBasis.approximantBasisInterpContext
statement: formalized
proof: formalized
---

# Approximant-Basis Interpolation Correctness Surface

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.ApproximantBasis.Correctness`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Correctness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Correctness.lean), by Valerii Huhnin.

> Theorem statements for the modular-equation reduction and the public
> `GSInterpContext` boundary.

> ## Width truncation helpers

> ## The modular-equation layer

`CompPoly.GuruswamiSudan.ApproximantBasis.gsModularEquation_row_iff_multiplicity` (theorem, [line 189](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Correctness.lean#L189))

> The executable GS modular row predicate is equivalent to packed
> multiplicity constraints for the bivariate coefficient-row view, for distinct
> interpolation nodes and rows inside the interpolation width.

```lean
theorem gsModularEquation_row_iff_multiplicity
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (modCtx : CPolynomial.ModContext F)
    (mulCtx : CPolynomial.MulContext F)
    (points : Array (F × F)) (params : GSInterpParams)
    (row : PolynomialRow F)
    (hdistinct : DistinctXCoordinates points)
    (hwidth : row.size ≤ interpolationWidth params) :
    let data := buildGSModularData V E mulCtx modCtx points params
    rowSatisfiesModularBool mulCtx modCtx row data.matrix data.moduli = true ↔
      CBivariate.satisfiesMultiplicityConstraintsBool
        (CBivariate.ofCoeffRow row) points params.multiplicity = true
```

> ## Soundness

`CompPoly.GuruswamiSudan.ApproximantBasis.approximantBasisInterpolate_sound` (theorem, [line 230](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Correctness.lean#L230))

> Soundness for executable approximant-basis interpolation.

```lean
theorem approximantBasisInterpolate_sound
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (solver : ModularSolutionBasisContext F)
    {points : Array (F × F)} {params : GSInterpParams} {Q : CBivariate F}
    (h :
      approximantBasisInterpolate V E solver points params = some Q) :
    ValidInterpolationWitness points params Q
```

> ## Completeness

`CompPoly.GuruswamiSudan.ApproximantBasis.approximantBasisInterpolate_complete` (theorem, [line 452](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Correctness.lean#L452))

> Completeness for executable approximant-basis interpolation on distinct
> input `x`-coordinates.

```lean
theorem approximantBasisInterpolate_complete
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (solver : ModularSolutionBasisContext F)
    (points : Array (F × F)) (params : GSInterpParams)
    (hdistinct : DistinctXCoordinates points)
    (hexists : ∃ Q, ValidInterpolationWitness points params Q) :
    ∃ Q, approximantBasisInterpolate V E solver points params = some Q
```

`CompPoly.GuruswamiSudan.ApproximantBasis.approximantBasisInterpContext` (definition, [line 630](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Correctness.lean#L630))

> Public approximant-basis interpolation backend context.

```lean
def approximantBasisInterpContext
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (solver : ModularSolutionBasisContext F) : GSInterpContext F
```

## Depends on

- [Executable Approximant-Basis Interpolation](algorithm.md)

## Proof depends on

- [Executable GS Modular-Data Bridges](modulardata.md)
- [Shear Equivalence for Guruswami-Sudan Multiplicity Constraints](multiplicity.md)
- [Lee-O'Sullivan Candidate Normalization](../leeosullivan/correctness/normalization.md)
- [Lee-O'Sullivan Row-Span Transport Helpers](../leeosullivan/correctness/rows.md)
- [Least-Shifted-Degree Row Selection Helpers](../../../../linearalgebra/polynomialmatrix/rowselection.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Correctness.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Correctness.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.ApproximantBasis.Correctness.json)
