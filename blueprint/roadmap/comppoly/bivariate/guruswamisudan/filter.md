---
catalog: module
lean: CompPoly.GuruswamiSudan.candidateMismatchCount, CompPoly.GuruswamiSudan.matchingPointCount, CompPoly.GuruswamiSudan.passesCandidateDistance, CompPoly.GuruswamiSudan.gsFilteredCore
statement: formalized
proof: formalized
---

# Guruswami-Sudan Candidate Filtering

`CompPoly.Bivariate.GuruswamiSudan.Filter`, in [CompPoly/Bivariate/GuruswamiSudan/Filter.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Filter.lean), by Valerii Huhnin.

> Generic packed-point filtering for algebraic `gsCore` outputs.

`CompPoly.GuruswamiSudan.candidateMismatchCount` (definition, [line 23](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Filter.lean#L23))

> Number of packed points where `p(x)` differs from the supplied `y`.

```lean
def candidateMismatchCount {F : Type*} [Semiring F] [BEq F]
    (points : Array (Prod F F)) (p : CPolynomial F) : Nat
```

`CompPoly.GuruswamiSudan.matchingPointCount` (definition, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Filter.lean#L31))

> Number of packed points where `p(x)` matches the supplied `y`.

```lean
def matchingPointCount {F : Type*} [Semiring F] [BEq F]
    (points : Array (Prod F F)) (p : CPolynomial F) : Nat
```

`CompPoly.GuruswamiSudan.passesCandidateDistance` (definition, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Filter.lean#L39))

> Boolean distance predicate for packed candidate filtering.

```lean
def passesCandidateDistance {F : Type*} [Semiring F] [BEq F]
    (points : Array (Prod F F)) (radius : Nat) (p : CPolynomial F) : Bool
```

`CompPoly.GuruswamiSudan.gsFilteredCore` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Filter.lean#L45))

> Run the algebraic GS core and keep only candidates within the packed
> mismatch radius.

```lean
def gsFilteredCore {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (points : Array (Prod F F))
    (interpContext : GSInterpContext F)
    (rootContext : GSRootContext F)
    (params : GSInterpParams)
    (radius : Nat) : Array (CPolynomial F)
```

## Depends on

- [Guruswami-Sudan Core](core.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Filter.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Filter.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Filter.json)
