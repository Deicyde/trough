---
catalog: module
lean: CompPoly.GuruswamiSudan.passesCandidateDistance_iff, CompPoly.GuruswamiSudan.mem_gsFilteredCore_iff, CompPoly.GuruswamiSudan.gsFilteredCore_sound, CompPoly.GuruswamiSudan.gsFilteredCore_complete_of_roots_all_valid_witnesses, CompPoly.GuruswamiSudan.gsFilteredCore_complete_of_enough_matches
statement: formalized
proof: formalized
---

# Guruswami-Sudan Candidate Filter Correctness

`CompPoly.Bivariate.GuruswamiSudan.FilterCorrectness`, in [CompPoly/Bivariate/GuruswamiSudan/FilterCorrectness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/FilterCorrectness.lean), by Valerii Huhnin.

> Correctness and completeness lemmas for generic packed filtering over algebraic
> `gsCore` outputs.

`CompPoly.GuruswamiSudan.passesCandidateDistance_iff` (theorem, [line 24](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/FilterCorrectness.lean#L24))

> Boolean distance filtering agrees with the executable mismatch count.

```lean
theorem passesCandidateDistance_iff {F : Type*} [Semiring F] [BEq F]
    {points : Array (Prod F F)} {radius : Nat} {p : CPolynomial F} :
    passesCandidateDistance points radius p = true ↔
      candidateMismatchCount points p ≤ radius
```

`CompPoly.GuruswamiSudan.mem_gsFilteredCore_iff` (theorem, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/FilterCorrectness.lean#L33))

> Membership in `gsFilteredCore` is membership in `gsCore` plus the packed
> distance predicate.

```lean
theorem mem_gsFilteredCore_iff {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {points : Array (Prod F F)}
    {interpContext : GSInterpContext F} {rootContext : GSRootContext F}
    {params : GSInterpParams} {radius : Nat}
    {p : CPolynomial F} :
    p ∈ (gsFilteredCore points interpContext rootContext params radius).toList ↔
      p ∈ (gsCore points interpContext rootContext params).toList ∧
        passesCandidateDistance points radius p = true
```

`CompPoly.GuruswamiSudan.gsFilteredCore_sound` (theorem, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/FilterCorrectness.lean#L47))

> Every filtered candidate is a sound algebraic core output and is within the
> packed mismatch radius.

```lean
theorem gsFilteredCore_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {points : Array (Prod F F)}
    {interpContext : GSInterpContext F} {rootContext : GSRootContext F}
    {params : GSInterpParams} {radius : Nat}
    {p : CPolynomial F}
    (hp : p ∈ (gsFilteredCore points interpContext rootContext params radius).toList) :
    exists Q,
      interpContext.interpolate points params = some Q ∧
        ValidInterpolationWitness points params Q ∧
          degreeLt p params.messageDegree ∧
            CBivariate.composeY Q p = 0 ∧
              candidateMismatchCount points p ≤ radius
```

`CompPoly.GuruswamiSudan.gsFilteredCore_complete_of_roots_all_valid_witnesses` (theorem, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/FilterCorrectness.lean#L71))

> Filtered-core completeness for candidates that root every valid
> interpolation witness and pass the packed distance filter.

```lean
theorem gsFilteredCore_complete_of_roots_all_valid_witnesses {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {points : Array (Prod F F)}
    {interpContext : GSInterpContext F} {rootContext : GSRootContext F}
    {params : GSInterpParams} {radius : Nat}
    {p : CPolynomial F}
    (hInterpExists : exists Q, ValidInterpolationWitness points params Q)
    (hdistinct : DistinctXCoordinates points)
    (hpdeg : degreeLt p params.messageDegree)
    (hrootAll :
      ∀ Q,
        ValidInterpolationWitness points params Q →
          CBivariate.composeY Q p = 0)
    (hpass : passesCandidateDistance points radius p = true) :
    p ∈ (gsFilteredCore points interpContext rootContext params radius).toList
```

`CompPoly.GuruswamiSudan.gsFilteredCore_complete_of_enough_matches` (theorem, [line 91](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/FilterCorrectness.lean#L91))

> Packed-point semantic completeness for the filtered GS core.

```lean
theorem gsFilteredCore_complete_of_enough_matches {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {points : Array (Prod F F)}
    {interpContext : GSInterpContext F} {rootContext : GSRootContext F}
    {params : GSInterpParams} {radius : Nat}
    {p : CPolynomial F}
    (hInterpExists : exists Q, ValidInterpolationWitness points params Q)
    (hpdeg : degreeLt p params.messageDegree)
    (hdistinct : DistinctXCoordinates points)
    (hmatches :
      params.weightedDegreeBound <
        params.multiplicity * matchingPointCount points p)
    (hpass : passesCandidateDistance points radius p = true) :
    p ∈ (gsFilteredCore points interpContext rootContext params radius).toList
```

## Depends on

- [Guruswami-Sudan Candidate Filtering](filter.md)

## Proof depends on

- [Guruswami-Sudan Core Correctness](corecorrectness.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/FilterCorrectness.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/FilterCorrectness.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.FilterCorrectness.json)
