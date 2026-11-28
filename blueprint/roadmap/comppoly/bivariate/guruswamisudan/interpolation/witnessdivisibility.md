---
catalog: module
lean: CompPoly.CBivariate.divByLinearYWith, CompPoly.CBivariate.divByLinearYWith_eq_divByLinearY, CompPoly.GuruswamiSudan.satisfiesMultiplicityConstraintsViaDivisibilityBool, CompPoly.GuruswamiSudan.interpolationWitnessIsValidViaDivisibilityBool
statement: formalized
proof: formalized
---

# Divisibility-Based Interpolation Witness Checking

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.WitnessDivisibility`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/WitnessDivisibility.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/WitnessDivisibility.lean), by Valerii Huhnin.

> A fast full recognizer for the Guruswami-Sudan multiplicity constraints.
>
> The pointwise check (`CBivariate.satisfiesMultiplicityConstraintsBool`)
> evaluates every Hasse derivative of order below `m` at every interpolation
> point, costing `O(n * m^2 * terms(Q))` field operations. For point sets with
> distinct `x`-coordinates the same property has a module-theoretic
> characterization: writing `Q = Σ_t c_t * (Y - R)^t` for the base-`(Y - R)`
> expansion of `Q`, where `R` interpolates the points, `Q` has a zero of
> multiplicity at least `m` at every point if and only if
> `G^(m - t) ∣ c_t` for all `t < m`, with `G = Π_i (X - x_i)` the vanishing
> polynomial of the `x`-coordinates.
>
> `satisfiesMultiplicityConstraintsViaDivisibilityBool` checks the right-hand
> side directly: it peels `m` digits off `Q` by synthetic division by `Y - R`
> and tests each digit for divisibility by the corresponding power of `G` with
> a monic remainder. With NTT-backed multiplication and remainder contexts the
> whole check is quasi-linear in the input size, with no per-point loop.
>
> `interpolationWitnessIsValidViaDivisibilityBool` combines the divisibility
> check with the nonzero and weighted-degree witness conditions, mirroring
> `interpolationWitnessIsValidBool`.

`CompPoly.CBivariate.divByLinearYWith` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/WitnessDivisibility.lean#L52))

> `divByLinearY` with the inner univariate products supplied by an explicit
> multiplication context, for callers that want NTT-backed Horner steps.

```lean
def divByLinearYWith {R : Type*} [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (M : CPolynomial.MulContext R) (Q : CBivariate R) (f : CPolynomial R) :
    CBivariate R × CPolynomial R
```

`CompPoly.CBivariate.divByLinearYWith_eq_divByLinearY` (theorem, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/WitnessDivisibility.lean#L70))

> The context-parametric synthetic division agrees with `divByLinearY`.

```lean
theorem divByLinearYWith_eq_divByLinearY {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (M : CPolynomial.MulContext R) (Q : CBivariate R) (f : CPolynomial R) :
    divByLinearYWith M Q f = divByLinearY Q f
```

`CompPoly.GuruswamiSudan.satisfiesMultiplicityConstraintsViaDivisibilityBool` (definition, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/WitnessDivisibility.lean#L90))

> Divisibility form of the multiplicity constraints: the digit `c_t` of the
> base-`(Y - R)` expansion of `Q` must be divisible by `G^(m - t)` for every
> `t < m`. The recursion peels one digit per step by synthetic division, so the
> step at recursion depth `t` checks `G^(m - t) ∣ c_t` on the running quotient.
>
> For `G` the vanishing polynomial of the (distinct) `x`-coordinates of a point
> set and `R` its interpolant, this is equivalent to
> `CBivariate.satisfiesMultiplicityConstraintsBool` on the same point set; see
> `satisfiesMultiplicityConstraintsViaDivisibilityBool_eq`.

```lean
def satisfiesMultiplicityConstraintsViaDivisibilityBool {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (Mul : CPolynomial.MulContext F) (Mod : CPolynomial.ModContext F)
    (G R : CPolynomial F) : Nat → CBivariate F → Bool
```

`CompPoly.GuruswamiSudan.interpolationWitnessIsValidViaDivisibilityBool` (definition, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/WitnessDivisibility.lean#L103))

> Divisibility-based recognizer for the semantic interpolation witness
> contract, agreeing with `interpolationWitnessIsValidBool` on point sets with
> distinct `x`-coordinates but avoiding its per-point Hasse derivative loop.

```lean
def interpolationWitnessIsValidViaDivisibilityBool {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (Mul : CPolynomial.MulContext F) (Mod : CPolynomial.ModContext F)
    (points : Array (F × F)) (params : GSInterpParams) (Q : CBivariate F) : Bool
```

## Depends on

- [Factorisation of Computable Bivariate Polynomials](../../factor.md)
- [Guruswami-Sudan Backend Contexts](../context.md)
- [Coefficient-Form Interpolation from a Vanishing Polynomial](../../../univariate/part-01/coefficientinterpolation.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/WitnessDivisibility.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/WitnessDivisibility.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.WitnessDivisibility.json)
