---
catalog: module
lean: CompPoly.GuruswamiSudan.LeeOSullivan.distinctXCoordinatesBool_iff, CompPoly.GuruswamiSudan.LeeOSullivan.leeCoefficientForm_eval_point, CompPoly.GuruswamiSudan.LeeOSullivan.leeVanishing_eval_point, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisRows_size, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisRowsWithRG_wellFormed, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisRowsWithRG_width, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisRows_wellFormed, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomials, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomials_size, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomials_getD_of_lt, CompPoly.GuruswamiSudan.LeeOSullivan.rowGet_leeOSullivanBasisRowsWithRG_getD
statement: formalized
proof: formalized
---

# Lee-O'Sullivan Correctness Common Helpers

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Common`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Common.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Common.lean), by Valerii Huhnin.

> Basic facts shared by Lee-O'Sullivan soundness and completeness proofs.

`CompPoly.GuruswamiSudan.LeeOSullivan.distinctXCoordinatesBool_iff` (theorem, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Common.lean#L30))

> Executable distinct-`x` check agrees with the semantic predicate.

```lean
theorem distinctXCoordinatesBool_iff {points : Array (F × F)} :
    distinctXCoordinatesBool points = true ↔ DistinctXCoordinates points
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeCoefficientForm_eval_point` (theorem, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Common.lean#L48))

> The coefficient-form `R` used by Lee evaluates to the packed values at distinct nodes.

```lean
theorem leeCoefficientForm_eval_point
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    {points : Array (F × F)} (hdistinct : DistinctXCoordinates points)
    {point : F × F} (hpoint : point ∈ points.toList) :
    CPolynomial.eval point.1
      (CPolynomial.interpolateCoefficientForm V E points) =
      point.2
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeVanishing_eval_point` (theorem, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Common.lean#L60))

> The vanishing `G` used by Lee vanishes on every listed `x`.

```lean
theorem leeVanishing_eval_point
    (V : CPolynomial.VanishingPolynomialContext F)
    {points : Array (F × F)} {point : F × F} (hpoint : point ∈ points.toList) :
    CPolynomial.eval point.1 (V.vanishingPolynomial (points.map fun p ↦ p.1)) = 0
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisRows_size` (theorem, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Common.lean#L70))

> Lee basis rows have exactly `ell + 1` rows.

```lean
theorem leeOSullivanBasisRows_size
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (points : Array (F × F)) (params : GSInterpParams) :
    (leeOSullivanBasisRows V E points params).size = leeOSullivanWidth params
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisRowsWithRG_wellFormed` (theorem, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Common.lean#L78))

> Lee basis rows built from fixed `R` and `G` are rectangular.

```lean
theorem leeOSullivanBasisRowsWithRG_wellFormed
    (R G : CPolynomial F) (params : GSInterpParams) :
    WellFormed (leeOSullivanBasisRowsWithRG R G params)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisRowsWithRG_width` (theorem, [line 94](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Common.lean#L94))

> The executable Lee basis matrix has width `ell + 1`.

```lean
theorem leeOSullivanBasisRowsWithRG_width
    (R G : CPolynomial F) (params : GSInterpParams) :
    MatrixWidth (leeOSullivanBasisRowsWithRG R G params) =
      leeOSullivanWidth params
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisRows_wellFormed` (theorem, [line 102](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Common.lean#L102))

> Lee basis rows built from packed points are rectangular.

```lean
theorem leeOSullivanBasisRows_wellFormed
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (points : Array (F × F)) (params : GSInterpParams) :
    WellFormed (leeOSullivanBasisRows V E points params)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomials` (definition, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Common.lean#L111))

> The Lee basis as bivariate polynomials, parallel to the executable row matrix.

```lean
def leeOSullivanBasisPolynomials
    (R G : CPolynomial F) (params : GSInterpParams) : Array (CBivariate F)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomials_size` (theorem, [line 117](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Common.lean#L117))

> The bivariate Lee basis has the same length as the row basis.

```lean
theorem leeOSullivanBasisPolynomials_size
    (R G : CPolynomial F) (params : GSInterpParams) :
    (leeOSullivanBasisPolynomials (F := F) R G params).size =
      leeOSullivanWidth params
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomials_getD_of_lt` (theorem, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Common.lean#L124))

> In-bounds reads from the bivariate Lee basis return the corresponding basis polynomial.

```lean
theorem leeOSullivanBasisPolynomials_getD_of_lt
    (R G : CPolynomial F) (params : GSInterpParams) {i : Nat}
    (hi : i < leeOSullivanWidth params) :
    (leeOSullivanBasisPolynomials (F := F) R G params).getD i 0 =
      leeOSullivanBasisPolynomial R G params i
```

`CompPoly.GuruswamiSudan.LeeOSullivan.rowGet_leeOSullivanBasisRowsWithRG_getD` (theorem, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Common.lean#L133))

> In-bounds row entries of the executable Lee basis are the `Y` coefficients
> of the corresponding bivariate basis polynomial.

```lean
theorem rowGet_leeOSullivanBasisRowsWithRG_getD
    (R G : CPolynomial F) (params : GSInterpParams) {i j : Nat}
    (hi : i < leeOSullivanWidth params) (hj : j < leeOSullivanWidth params) :
    rowGet
        ((leeOSullivanBasisRowsWithRG R G params).getD i #[]) j =
      CPolynomial.coeff (leeOSullivanBasisPolynomial R G params i) j
```

## Depends on

- [Lee-O'Sullivan Interpolation Basics](../basic.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Common.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Common.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Common.json)
