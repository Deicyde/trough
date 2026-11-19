---
catalog: module
lean: CompPoly.GuruswamiSudan.gsCore_sound, CompPoly.GuruswamiSudan.gsCore_complete_of_interpolate, CompPoly.GuruswamiSudan.gsCore_complete_of_roots_all_valid_witnesses, CompPoly.GuruswamiSudan.composeY_eq_zero_of_enough_matching_multiplicity_points, CompPoly.GuruswamiSudan.gsCore_complete_of_enough_matches
statement: formalized
proof: formalized
---

# Guruswami-Sudan Core Correctness

`CompPoly.Bivariate.GuruswamiSudan.CoreCorrectness`, in [CompPoly/Bivariate/GuruswamiSudan/CoreCorrectness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/CoreCorrectness.lean), by Valerii Huhnin.

> Public correctness theorems for the backend-parametric CompPoly
> Guruswami-Sudan core.

`CompPoly.GuruswamiSudan.gsCore_sound` (theorem, [line 28](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/CoreCorrectness.lean#L28))

> Every polynomial returned by `gsCore` is a bounded-degree root of the
> interpolation polynomial produced by the interpolation backend.

```lean
theorem gsCore_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {points : Array (Prod F F)}
    {interpContext : GSInterpContext F} {rootContext : GSRootContext F}
    {params : GSInterpParams}
    {p : CPolynomial F}
    (hp : p ∈ (gsCore points interpContext rootContext params).toList) :
    exists Q,
      interpContext.interpolate points params = some Q ∧
        ValidInterpolationWitness points params Q ∧
          degreeLt p params.messageDegree ∧
            CBivariate.composeY Q p = 0
```

`CompPoly.GuruswamiSudan.gsCore_complete_of_interpolate` (theorem, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/CoreCorrectness.lean#L51))

> Completeness for the concrete interpolation polynomial returned by the
> interpolation backend.

```lean
theorem gsCore_complete_of_interpolate {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {points : Array (Prod F F)}
    {interpContext : GSInterpContext F} {rootContext : GSRootContext F}
    {params : GSInterpParams}
    {Q : CBivariate F} {p : CPolynomial F}
    (hQ : interpContext.interpolate points params = some Q)
    (hpdeg : degreeLt p params.messageDegree)
    (hroot : CBivariate.composeY Q p = 0) :
    p ∈ (gsCore points interpContext rootContext params).toList
```

`CompPoly.GuruswamiSudan.gsCore_complete_of_roots_all_valid_witnesses` (theorem, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/CoreCorrectness.lean#L68))

> Backend-parametric completeness for candidates that root every valid
> interpolation witness.

```lean
theorem gsCore_complete_of_roots_all_valid_witnesses {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {points : Array (Prod F F)}
    {interpContext : GSInterpContext F} {rootContext : GSRootContext F}
    {params : GSInterpParams}
    {p : CPolynomial F}
    (hInterpExists : exists Q, ValidInterpolationWitness points params Q)
    (hdistinct : DistinctXCoordinates points)
    (hpdeg : degreeLt p params.messageDegree)
    (hrootAll :
      ∀ Q,
        ValidInterpolationWitness points params Q →
          CBivariate.composeY Q p = 0) :
    p ∈ (gsCore points interpContext rootContext params).toList
```

`CompPoly.GuruswamiSudan.composeY_eq_zero_of_enough_matching_multiplicity_points` (theorem, [line 510](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/CoreCorrectness.lean#L510))

> If a bounded-degree candidate agrees with enough distinct packed
> multiplicity-constrained points, it roots any valid interpolation witness.

```lean
theorem composeY_eq_zero_of_enough_matching_multiplicity_points {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {points : Array (Prod F F)} {params : GSInterpParams}
    {Q : CBivariate F} {p : CPolynomial F}
    (hQ : ValidInterpolationWitness points params Q)
    (hpdeg : degreeLt p params.messageDegree)
    (hdistinct : DistinctXCoordinates points)
    (hmatches :
      params.weightedDegreeBound <
        params.multiplicity * matchingPointCount points p) :
    CBivariate.composeY Q p = 0
```

`CompPoly.GuruswamiSudan.gsCore_complete_of_enough_matches` (theorem, [line 570](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/CoreCorrectness.lean#L570))

> Packed-point semantic completeness for the algebraic GS core.

```lean
theorem gsCore_complete_of_enough_matches {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {points : Array (Prod F F)}
    {interpContext : GSInterpContext F} {rootContext : GSRootContext F}
    {params : GSInterpParams}
    {p : CPolynomial F}
    (hInterpExists : exists Q, ValidInterpolationWitness points params Q)
    (hpdeg : degreeLt p params.messageDegree)
    (hdistinct : DistinctXCoordinates points)
    (hmatches :
      params.weightedDegreeBound <
        params.multiplicity * matchingPointCount points p) :
    p ∈ (gsCore points interpContext rootContext params).toList
```

## Depends on

- [Guruswami-Sudan Candidate Filtering](filter.md)

## Proof depends on

- [Guruswami-Sudan Polynomial Correctness Lemmas](polynomialcorrectness.md)
- [Common Guruswami-Sudan Root Helper Lemmas](root/common-2/lemmas.md)
- [Mathlib-Facing Bivariate Weighted-Degree Helpers](../../tomathlib/polynomial/bivariateweighteddegree.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/CoreCorrectness.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/CoreCorrectness.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.CoreCorrectness.json)
