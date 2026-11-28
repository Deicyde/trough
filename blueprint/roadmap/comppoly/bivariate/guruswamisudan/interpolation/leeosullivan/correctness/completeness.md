---
catalog: module
lean: CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanPositiveInterpolate_complete_of_row, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanPositiveInterpolate_complete_of_span, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanInterpolate_complete, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanInterpContext
statement: formalized
proof: formalized
---

# Lee-O'Sullivan Interpolation Completeness

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Completeness`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Completeness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Completeness.lean), by Valerii Huhnin.

> Completeness theorems and public context wrapper for Lee-O'Sullivan interpolation.

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanPositiveInterpolate_complete_of_row` (theorem, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Completeness.lean#L30))

```lean
theorem leeOSullivanPositiveInterpolate_complete_of_row
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (reducer : ShiftedRowReducerContext F)
    {points : Array (F × F)} {params : GSInterpParams}
    (hdistinct : DistinctXCoordinates points)
    (hHigh : ¬ params.messageDegree ≤ 1)
    {row : PolynomialRow F} {rowDegree : Nat}
    (hrowSpan :
      row ∈ RowSpan
        (leeOSullivanBasisRowsWithRG
          (CPolynomial.interpolateCoefficientFormWithVanishing E
            (V.vanishingPolynomial (points.map fun point ↦ point.1)) points)
          (V.vanishingPolynomial (points.map fun point ↦ point.1)) params))
    (hrowDegree :
      rowShiftedDegree? row (leeOSullivanShifts params) = some rowDegree)
    (hrowBound : rowDegree ≤ params.weightedDegreeBound) :
    ∃ Q, leeOSullivanPositiveInterpolate V E reducer points params = some Q
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanPositiveInterpolate_complete_of_span` (theorem, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Completeness.lean#L123))

```lean
theorem leeOSullivanPositiveInterpolate_complete_of_span
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (reducer : ShiftedRowReducerContext F)
    {points : Array (F × F)} {params : GSInterpParams} {Q : CBivariate F}
    (hdistinct : DistinctXCoordinates points)
    (hHigh : ¬ params.messageDegree ≤ 1)
    (hQ : ValidInterpolationWitness points params Q)
    (hspan :
      koetterBasisSpanContains
        (leeOSullivanBasisPolynomials (F := F)
          (CPolynomial.interpolateCoefficientFormWithVanishing E
            (V.vanishingPolynomial (points.map fun point ↦ point.1)) points)
          (V.vanishingPolynomial (points.map fun point ↦ point.1)) params) Q) :
    ∃ Q, leeOSullivanPositiveInterpolate V E reducer points params = some Q
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanInterpolate_complete` (theorem, [line 379](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Completeness.lean#L379))

> Distinct-input completeness for the executable Lee-O'Sullivan interpolation operation.

```lean
theorem leeOSullivanInterpolate_complete
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (reducer : ShiftedRowReducerContext F)
    {points : Array (F × F)} {params : GSInterpParams}
    (hdistinct : DistinctXCoordinates points)
    (hExists : ∃ Q, ValidInterpolationWitness points params Q) :
    ∃ Q, leeOSullivanInterpolate V E reducer points params = some Q
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanInterpContext` (definition, [line 423](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Completeness.lean#L423))

> Public Lee-O'Sullivan interpolation backend context.

```lean
def leeOSullivanInterpContext
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (reducer : ShiftedRowReducerContext F) : GSInterpContext F
```

## Depends on

- [Executable Lee-O'Sullivan Interpolation](../algorithm.md)
- [Generic Basis Combination Helpers](combinations.md)
- [Lee-O'Sullivan Correctness Common Helpers](common.md)

## Proof depends on

- [Lee-O'Sullivan Divisibility Helpers](divisibility.md)
- [Lee-O'Sullivan Interpolation Soundness](soundness.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Completeness.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Completeness.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Completeness.json)
