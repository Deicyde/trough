---
catalog: module
lean: CompPoly.GuruswamiSudan.alekhnovichRootsYDegreeLt_sound, CompPoly.GuruswamiSudan.alekhnovichRootsYDegreeLt_complete_of_candidate_mem, CompPoly.GuruswamiSudan.RootMod.substituteYPolynomialPlusXPowerY, CompPoly.GuruswamiSudan.RootMod.substituteYPolynomialPlusXPowerYTruncated, CompPoly.GuruswamiSudan.RootMod.stripXAdicFactor, CompPoly.GuruswamiSudan.alekhnovichRootPrefixesWithFuel_complete, CompPoly.GuruswamiSudan.alekhnovichRootCandidatesWithFuel_complete, CompPoly.GuruswamiSudan.composeY_eq_zero_of_rootMod_of_substitutionDegreeBound, CompPoly.GuruswamiSudan.alekhnovichRootCandidates_complete, CompPoly.GuruswamiSudan.alekhnovichRootsYDegreeLt_complete, CompPoly.GuruswamiSudan.alekhnovichRootContext
statement: formalized
proof: formalized
---

# Alekhnovich Root Search Correctness

`CompPoly.Bivariate.GuruswamiSudan.Root.Alekhnovich.Correctness`, in [CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Correctness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Correctness.lean), by Valerii Huhnin.

> Public correctness surface for the Alekhnovich bounded bivariate root backend
> [Ale05].
>
> ## References
>
> * [M. Alekhnovich, *Linear Diophantine Equations Over Polynomials and Soft
>     Decoding of Reed-Solomon Codes*, IEEE Transactions on Information Theory
>     51(7), 2257-2265, 2005][Ale05]

`CompPoly.GuruswamiSudan.alekhnovichRootsYDegreeLt_sound` (theorem, [line 913](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Correctness.lean#L913))

> Soundness of Alekhnovich root filtering.

```lean
theorem alekhnovichRootsYDegreeLt_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {fieldRoots : FieldRootContext F} {Q : CBivariate F} {k : Nat}
    {p : CPolynomial F}
    (h : p ∈ (alekhnovichRootsYDegreeLt fieldRoots Q k).toList) :
    degreeLt p k ∧ CBivariate.composeY Q p = 0
```

`CompPoly.GuruswamiSudan.alekhnovichRootsYDegreeLt_complete_of_candidate_mem` (theorem, [line 927](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Correctness.lean#L927))

> The exact final filter keeps any true bounded root that the Alekhnovich
> candidate generator has already produced.

```lean
theorem alekhnovichRootsYDegreeLt_complete_of_candidate_mem {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {fieldRoots : FieldRootContext F} {Q : CBivariate F} {k : Nat}
    {p : CPolynomial F}
    (hQ : Q ≠ 0)
    (hmem : p ∈ (alekhnovichRootCandidates fieldRoots Q k).toList)
    (hdegree : degreeLt p k) (hroot : CBivariate.composeY Q p = 0) :
    p ∈ (alekhnovichRootsYDegreeLt fieldRoots Q k).toList
```

`CompPoly.GuruswamiSudan.RootMod.substituteYPolynomialPlusXPowerY` (theorem, [line 945](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Correctness.lean#L945))

> Shifted substitution preserves modular roots below `N` before truncation.

```lean
theorem RootMod.substituteYPolynomialPlusXPowerY {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {Q : CBivariate F} {f g : CPolynomial F} {t N : Nat}
    (hroot : RootMod Q (f + shiftPolynomialByXPower g t) N) :
    RootMod (substituteYPolynomialPlusXPowerY Q f t) g N
```

`CompPoly.GuruswamiSudan.RootMod.substituteYPolynomialPlusXPowerYTruncated` (theorem, [line 956](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Correctness.lean#L956))

> Truncated shifted substitution has the same coefficients below `N` as exact
> shifted substitution, so it preserves modular roots below `N`.

```lean
theorem RootMod.substituteYPolynomialPlusXPowerYTruncated {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {Q : CBivariate F} {f g : CPolynomial F} {t N : Nat}
    (hroot : RootMod Q (f + shiftPolynomialByXPower g t) N) :
    RootMod (substituteYPolynomialPlusXPowerYTruncated Q f t N) g N
```

`CompPoly.GuruswamiSudan.RootMod.stripXAdicFactor` (theorem, [line 978](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Correctness.lean#L978))

> Stripping a visible `X`-adic valuation transports a modular root of `Q` to
> a shorter modular root of the stripped residual.

```lean
theorem RootMod.stripXAdicFactor {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {Q : CBivariate F} {p : CPolynomial F} {s N : Nat}
    (horder : CBivariate.xAdicOrder? Q = some s)
    (hroot : RootMod Q p (s + N)) :
    RootMod (CBivariate.stripXAdicFactor Q) p N
```

`CompPoly.GuruswamiSudan.alekhnovichRootPrefixesWithFuel_complete` (theorem, [line 1411](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Correctness.lean#L1411))

> Recursive Alekhnovich prefix coverage for modular roots.

```lean
theorem alekhnovichRootPrefixesWithFuel_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {fieldRoots : FieldRootContext F} {Q : CBivariate F} {N fuel : Nat}
    {p : CPolynomial F}
    (hfuel : N < fuel)
    (hroot : RootMod Q p N) :
    ∃ rootPrefix,
      rootPrefix ∈ (alekhnovichRootPrefixesWithFuel fieldRoots fuel Q N).toList ∧
        MatchesRootPrefix p rootPrefix
```

`CompPoly.GuruswamiSudan.alekhnovichRootCandidatesWithFuel_complete` (theorem, [line 2235](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Correctness.lean#L2235))

> Candidate generation coverage for the Alekhnovich-only recursive suffix
> completion.

```lean
theorem alekhnovichRootCandidatesWithFuel_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {fieldRoots : FieldRootContext F} {Q : CBivariate F} {k fuel : Nat}
    {p : CPolynomial F}
    (hfuel : k < fuel)
    (hQ : Q ≠ 0)
    (hdegree : degreeLt p k)
    (hroot : CBivariate.composeY Q p = 0) :
    p ∈ (alekhnovichRootCandidatesWithFuel fieldRoots fuel Q k).toList
```

`CompPoly.GuruswamiSudan.composeY_eq_zero_of_rootMod_of_substitutionDegreeBound` (theorem, [line 2318](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Correctness.lean#L2318))

> The finite modular-root predicate is exact once the substitution degree is
> bounded below the checked precision.

```lean
theorem composeY_eq_zero_of_rootMod_of_substitutionDegreeBound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {Q : CBivariate F} {p : CPolynomial F} {k N : Nat}
    (hbound : SubstitutionDegreeBound Q k N)
    (hdegree : degreeLt p k)
    (hroot : RootMod Q p N) :
    CBivariate.composeY Q p = 0
```

`CompPoly.GuruswamiSudan.alekhnovichRootCandidates_complete` (theorem, [line 2363](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Correctness.lean#L2363))

> Completeness of Alekhnovich candidate generation for exact bounded roots.

```lean
theorem alekhnovichRootCandidates_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {fieldRoots : FieldRootContext F} {Q : CBivariate F} {k : Nat}
    {p : CPolynomial F}
    (hQ : Q ≠ 0)
    (hdegree : degreeLt p k)
    (hroot : CBivariate.composeY Q p = 0) :
    p ∈ (alekhnovichRootCandidates fieldRoots Q k).toList
```

`CompPoly.GuruswamiSudan.alekhnovichRootsYDegreeLt_complete` (theorem, [line 2378](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Correctness.lean#L2378))

> Completeness of Alekhnovich bounded-degree root finding from a complete
> field-root backend.

```lean
theorem alekhnovichRootsYDegreeLt_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {fieldRoots : FieldRootContext F}
    {Q : CBivariate F} {k : Nat} {p : CPolynomial F}
    (hQ : Q ≠ 0) (hdegree : degreeLt p k) (hroot : CBivariate.composeY Q p = 0) :
    p ∈ (alekhnovichRootsYDegreeLt fieldRoots Q k).toList
```

`CompPoly.GuruswamiSudan.alekhnovichRootContext` (definition, [line 2390](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Correctness.lean#L2390))

> Alekhnovich roots packaged with an explicit univariate field-root backend.

```lean
def alekhnovichRootContext (F : Type*)
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (fieldRoots : FieldRootContext F) : GSRootContext F
```

## Depends on

- [Alekhnovich Root Search Lemmas](lemmas.md)

## Proof depends on

- [Guruswami-Sudan Polynomial Correctness Lemmas](../../polynomialcorrectness.md)
- [Roth-Ruckenstein Correctness Support](../rothruckenstein/lemmas.md)
- [Shifted Substitution Lemmas](../shiftedsubstitution-2/lemmas.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Correctness.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Correctness.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Root.Alekhnovich.Correctness.json)
