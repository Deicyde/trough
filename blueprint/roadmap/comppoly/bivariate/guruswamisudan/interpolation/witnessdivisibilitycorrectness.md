---
catalog: module
lean: CompPoly.GuruswamiSudan.satisfiesMultiplicityConstraintsViaDivisibilityBool_eq, CompPoly.GuruswamiSudan.interpolationWitnessIsValidViaDivisibilityBool_eq
statement: formalized
proof: formalized
---

# Correctness of Divisibility-Based Witness Checking

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.WitnessDivisibilityCorrectness`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/WitnessDivisibilityCorrectness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/WitnessDivisibilityCorrectness.lean), by Valerii Huhnin.

> `satisfiesMultiplicityConstraintsViaDivisibilityBool` agrees with the
> pointwise Hasse checker `CBivariate.satisfiesMultiplicityConstraintsBool`
> on point sets with distinct `x`-coordinates, and consequently
> `interpolationWitnessIsValidViaDivisibilityBool` agrees with
> `interpolationWitnessIsValidBool`.
>
> The proof peels one base-`(Y - R)` digit per multiplicity level.
>
> * Soundness: from `Q = C c + (Y - R) * Q'` with `c = W * G^(m+1)`, the digit
>   term gains multiplicity `m + 1` from the `G`-power
>   (`hasMultiplicityAtLeast_ofYConstant_pow_mul_eval_zero`), the quotient term
>   gains one from `Y - R` (`hasMultiplicityAtLeast_linearYDivisor_mul`) on top
>   of the inductive hypothesis, and multiplicity is closed under addition.
>
> * Completeness: the quotient `Q'` keeps multiplicity `m` at every point
>   (`witness_hasMultiplicity_quot`, by a strong induction on the
>   `X`-coefficients of the Taylor-shifted division identity), so the digit
>   `C c = Q - (Y - R) * Q'` has multiplicity `m + 1` with `Y`-degree zero, and
>   `coeffY_dvd_vanishingPolynomial_pow_of_multiplicity` forces
>   `G^(m+1) ∣ c`.

> ### Generic helpers

> ### The division identity

> ### The shifted division identity

> ### The quotient keeps multiplicity

> ### Multiplicity closure helpers

> ### Main equivalence

`CompPoly.GuruswamiSudan.satisfiesMultiplicityConstraintsViaDivisibilityBool_eq` (theorem, [line 472](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/WitnessDivisibilityCorrectness.lean#L472))

> The divisibility-based multiplicity checker agrees with the pointwise
> Hasse checker on point sets with distinct `x`-coordinates.

```lean
theorem satisfiesMultiplicityConstraintsViaDivisibilityBool_eq
    (Mul : CPolynomial.MulContext F) (Mod : CPolynomial.ModContext F)
    {points : Array (F × F)} (R : CPolynomial F)
    (hdistinct : DistinctXCoordinates points)
    (hR : ∀ point, point ∈ points.toList → CPolynomial.eval point.1 R = point.2)
    (m : Nat) (Q : CBivariate F) :
    satisfiesMultiplicityConstraintsViaDivisibilityBool Mul Mod
        (CPolynomial.vanishingPolynomialArray (points.map fun p ↦ p.1)) R m Q =
      CBivariate.satisfiesMultiplicityConstraintsBool Q points m
```

`CompPoly.GuruswamiSudan.interpolationWitnessIsValidViaDivisibilityBool_eq` (theorem, [line 488](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/WitnessDivisibilityCorrectness.lean#L488))

> The divisibility-based witness recognizer agrees with
> `interpolationWitnessIsValidBool` on point sets with distinct
> `x`-coordinates.

```lean
theorem interpolationWitnessIsValidViaDivisibilityBool_eq
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (Mul : CPolynomial.MulContext F) (Mod : CPolynomial.ModContext F)
    {points : Array (F × F)} (params : GSInterpParams)
    (hdistinct : DistinctXCoordinates points) (Q : CBivariate F) :
    interpolationWitnessIsValidViaDivisibilityBool V E Mul Mod points params Q =
      interpolationWitnessIsValidBool points params Q
```

## Depends on

- [Guruswami-Sudan Interpolation Basics](basic.md)
- [Divisibility-Based Interpolation Witness Checking](witnessdivisibility.md)

## Proof depends on

- [Lee-O'Sullivan Basis Correctness Helpers](leeosullivan/correctness/basis.md)
- [Lee-O'Sullivan Divisibility Helpers](leeosullivan/correctness/divisibility.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/WitnessDivisibilityCorrectness.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/WitnessDivisibilityCorrectness.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.WitnessDivisibilityCorrectness.json)
