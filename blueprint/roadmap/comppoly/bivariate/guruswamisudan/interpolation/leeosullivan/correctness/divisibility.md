---
catalog: module
lean: CompPoly.GuruswamiSudan.LeeOSullivan.coeffY_dvd_vanishingPolynomial_pow_of_multiplicity
statement: formalized
proof: formalized
---

# Lee-O'Sullivan Divisibility Helpers

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Divisibility`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Divisibility.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Divisibility.lean), by Valerii Huhnin.

> Hasse-derivative and vanishing-polynomial divisibility bridges used in completeness.

`CompPoly.GuruswamiSudan.LeeOSullivan.coeffY_dvd_vanishingPolynomial_pow_of_multiplicity` (theorem, [line 208](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Divisibility.lean#L208))

```lean
theorem coeffY_dvd_vanishingPolynomial_pow_of_multiplicity
    (V : CPolynomial.VanishingPolynomialContext F)
    {points : Array (F × F)} {P : CBivariate F} {m n : Nat}
    (hdistinct : DistinctXCoordinates points)
    (hn : n < m)
    (hY : ∀ j, n < j → P.val.coeff j = 0)
    (hmult : CBivariate.SatisfiesMultiplicityConstraints P points m) :
    ∃ W : CPolynomial F,
      P.val.coeff n =
        W * (V.vanishingPolynomial (points.map fun point ↦ point.1)) ^ (m - n)
```

## Depends on

- [Guruswami-Sudan Backend Contexts](../../../context.md)
- [Vanishing Polynomials for Array Nodes](../../../../../univariate/part-02/vanishing.md)

## Proof depends on

- [Guruswami-Sudan Polynomial Correctness Lemmas](../../../polynomialcorrectness.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Divisibility.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Divisibility.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Divisibility.json)
