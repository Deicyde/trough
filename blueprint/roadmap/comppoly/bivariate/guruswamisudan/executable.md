---
catalog: module
lean: CompPoly.GuruswamiSudan.GSFilteredCoreContext, CompPoly.GuruswamiSudan.filteredCoreContextOfInterpRootContexts, CompPoly.GuruswamiSudan.GSReceivedWord, CompPoly.GuruswamiSudan.GSReceivedWord.length, CompPoly.GuruswamiSudan.GSExecParams, CompPoly.GuruswamiSudan.decodeWithParams, CompPoly.GuruswamiSudan.GSParamSelector, CompPoly.GuruswamiSudan.decode
statement: formalized
proof: formalized
---

# Guruswami-Sudan Executable Decoder

`CompPoly.Bivariate.GuruswamiSudan.Executable`, in [CompPoly/Bivariate/GuruswamiSudan/Executable.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Executable.lean), by Valerii Huhnin.

> Top-level executable API for the packed CompPoly Guruswami-Sudan decoder.

`CompPoly.GuruswamiSudan.GSFilteredCoreContext` (structure, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Executable.lean#L26))

> Backend-parametric filtered core exposed as a reusable executable context.
>
> The context packages an executable filtered decoder together with its CompPoly
> soundness and completeness contracts.

```lean
structure GSFilteredCoreContext
    (F : Type*) [Field F] [BEq F] [LawfulBEq F] [DecidableEq F] where
  run :
    Array (F × F) →
    GSInterpParams →
    Nat →
    Array (CPolynomial F)
  sound :
    ∀ {points params radius p},
      p ∈ (run points params radius).toList →
        ∃ Q,
          ValidInterpolationWitness points params Q ∧
            degreeLt p params.messageDegree ∧
              CBivariate.composeY Q p = 0 ∧
                candidateMismatchCount points p ≤ radius
  complete :
    ∀ {points params radius p},
      (∃ Q, ValidInterpolationWitness points params Q) →
      DistinctXCoordinates points →
      degreeLt p params.messageDegree →
      params.weightedDegreeBound <
        params.multiplicity * matchingPointCount points p →
      passesCandidateDistance points radius p = true →
        p ∈ (run points params radius).toList
```

`CompPoly.GuruswamiSudan.filteredCoreContextOfInterpRootContexts` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Executable.lean#L52))

> Filtered-core context assembled from CompPoly interpolation and root backends.

```lean
def filteredCoreContextOfInterpRootContexts
    {F : Type*} [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (interp : GSInterpContext F)
    (roots : GSRootContext F) :
    GSFilteredCoreContext F
```

`CompPoly.GuruswamiSudan.GSReceivedWord` (structure, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Executable.lean#L77))

> Packed received word accepted by the executable decoder.

```lean
structure GSReceivedWord (F : Type*) where
  points : Array (F × F)
deriving Repr
```

`CompPoly.GuruswamiSudan.GSReceivedWord.length` (definition, [line 82](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Executable.lean#L82))

> Runtime length of a packed received word.

```lean
def GSReceivedWord.length {F : Type*} (w : GSReceivedWord F) : Nat
```

`CompPoly.GuruswamiSudan.GSExecParams` (structure, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Executable.lean#L86))

> Explicit executable parameters for the parameterized decoder.

```lean
structure GSExecParams where
  interp : GSInterpParams
  radius : Nat
deriving Repr, BEq, DecidableEq
```

`CompPoly.GuruswamiSudan.decodeWithParams` (definition, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Executable.lean#L92))

> Computable executable decoder with caller-supplied parameters.

```lean
def decodeWithParams
    {F : Type*} [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (ctx : GSFilteredCoreContext F)
    (params : GSExecParams)
    (w : GSReceivedWord F) :
    Array (CPolynomial F)
```

`CompPoly.GuruswamiSudan.GSParamSelector` (structure, [line 101](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Executable.lean#L101))

> Parameter selector for the selector-backed executable decoder.

```lean
structure GSParamSelector where
  choose : Nat → Nat → Nat → Option GSExecParams
```

`CompPoly.GuruswamiSudan.decode` (definition, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Executable.lean#L105))

> Selector-backed executable decoder with parameters selected from `(k, w.length, e)`.

```lean
def decode
    {F : Type*} [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (ctx : GSFilteredCoreContext F)
    (selector : GSParamSelector)
    (k e : Nat)
    (w : GSReceivedWord F) :
    Array (CPolynomial F)
```

## Depends on

- [Guruswami-Sudan Candidate Filtering](filter.md)

## Proof depends on

- [Guruswami-Sudan Candidate Filter Correctness](filtercorrectness.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Executable.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Executable.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Executable.json)
