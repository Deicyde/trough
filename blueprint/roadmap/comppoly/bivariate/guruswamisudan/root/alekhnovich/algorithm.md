---
catalog: module
lean: CompPoly.GuruswamiSudan.RootPrefix, CompPoly.GuruswamiSudan.alekhnovichPrecisionBound, CompPoly.GuruswamiSudan.AlekhnovichResidual, CompPoly.GuruswamiSudan.shiftedResidualUpTo, CompPoly.GuruswamiSudan.composeRootPrefixes, CompPoly.GuruswamiSudan.normalizeAlekhnovichInput, CompPoly.GuruswamiSudan.alekhnovichRootPrefixesWithFuel, CompPoly.GuruswamiSudan.alekhnovichRootPrefixes, CompPoly.GuruswamiSudan.finishAlekhnovichPrefixWithAlekhnovichWithFuel, CompPoly.GuruswamiSudan.alekhnovichRootCandidatesWithFuel, CompPoly.GuruswamiSudan.finishAlekhnovichPrefixWithAlekhnovich, CompPoly.GuruswamiSudan.alekhnovichRootCandidates, CompPoly.GuruswamiSudan.alekhnovichRootsYDegreeLt
statement: formalized
proof: formalized
---

# Alekhnovich Bivariate Bounded Root Search

`CompPoly.Bivariate.GuruswamiSudan.Root.Alekhnovich.Algorithm`, in [CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Algorithm.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Algorithm.lean), by Valerii Huhnin.

> Executable batched `X`-adic root lifting for the Guruswami-Sudan bivariate root
> phase. The public output is exactly filtered against `Q(X, p(X)) = 0` and
> `degree p < k`, following Alekhnovich's lattice-based root-search approach
> [Ale05].
>
> ## References
>
> * [M. Alekhnovich, *Linear Diophantine Equations Over Polynomials and Soft
>     Decoding of Reed-Solomon Codes*, IEEE Transactions on Information Theory
>     51(7), 2257-2265, 2005][Ale05]

`CompPoly.GuruswamiSudan.RootPrefix` (structure, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Algorithm.lean#L34))

> A prefix coset `prefixPoly + X^precision * g(X)`.

```lean
structure RootPrefix (F : Type*) [Zero F] where
  prefixPoly : CPolynomial F
  precision : Nat
deriving BEq, DecidableEq
```

`CompPoly.GuruswamiSudan.alekhnovichPrecisionBound` (definition, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Algorithm.lean#L43))

> Precision requested by the Alekhnovich top-level root search.
>
> This asks for a small margin over the exactness bound; exact filtering remains
> the public soundness boundary.

```lean
def alekhnovichPrecisionBound {F : Type*} [Zero F] [BEq F]
    (Q : CBivariate F) (k : Nat) : Nat
```

`CompPoly.GuruswamiSudan.AlekhnovichResidual` (structure, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Algorithm.lean#L51))

> Normalized shifted residual and its stripped `X`-adic valuation.

```lean
structure AlekhnovichResidual (F : Type*) [Zero F] where
  valuation : Nat
  residual : CBivariate F
deriving BEq, DecidableEq
```

`CompPoly.GuruswamiSudan.shiftedResidualUpTo` (definition, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Algorithm.lean#L57))

> Shift, truncate, strip the visible `X`-adic factor, and report the residual.

```lean
def shiftedResidualUpTo {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (f : CPolynomial F) (t N : Nat) :
    AlekhnovichResidual F
```

`CompPoly.GuruswamiSudan.composeRootPrefixes` (definition, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Algorithm.lean#L71))

> Compose an outer prefix with a suffix prefix returned by a residual call.

```lean
def composeRootPrefixes {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (outer suffix : RootPrefix F) : RootPrefix F
```

`CompPoly.GuruswamiSudan.normalizeAlekhnovichInput` (definition, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Algorithm.lean#L80))

> Normalize a residual by stripping an initial common `X` factor only up to the
> requested precision. Returning `none` means the current equation is
> unconstrained modulo the requested precision.

```lean
def normalizeAlekhnovichInput {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (Q : CBivariate F) (N : Nat) : Option (CBivariate F × Nat)
```

`CompPoly.GuruswamiSudan.alekhnovichRootPrefixesWithFuel` (definition, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Algorithm.lean#L92))

> Alekhnovich root prefixes with explicit fuel.

```lean
def alekhnovichRootPrefixesWithFuel {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (fieldRoots : FieldRootContext F) :
    Nat → CBivariate F → Nat → Array (RootPrefix F)
```

`CompPoly.GuruswamiSudan.alekhnovichRootPrefixes` (definition, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Algorithm.lean#L128))

> Alekhnovich root prefixes through the requested precision.

```lean
def alekhnovichRootPrefixes {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (fieldRoots : FieldRootContext F) (Q : CBivariate F) (N : Nat) :
    Array (RootPrefix F)
```

`CompPoly.GuruswamiSudan.finishAlekhnovichPrefixWithAlekhnovichWithFuel` (definition, [line 147](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Algorithm.lean#L147))

> Finish one Alekhnovich prefix with Alekhnovich-only recursive suffix
> completion. Prefixes already at precision `k` are simply truncated to the final
> degree bound.

```lean
def finishAlekhnovichPrefixWithAlekhnovichWithFuel {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (fieldRoots : FieldRootContext F) :
    Nat → CBivariate F → Nat → RootPrefix F → Array (CPolynomial F)
```

`CompPoly.GuruswamiSudan.alekhnovichRootCandidatesWithFuel` (definition, [line 168](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Algorithm.lean#L168))

> Materialize bounded-degree candidates from Alekhnovich prefixes.

```lean
def alekhnovichRootCandidatesWithFuel {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (fieldRoots : FieldRootContext F) :
    Nat → CBivariate F → Nat → Array (CPolynomial F)
```

`CompPoly.GuruswamiSudan.finishAlekhnovichPrefixWithAlekhnovich` (definition, [line 192](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Algorithm.lean#L192))

> Finish one Alekhnovich prefix with Alekhnovich-only suffix completion.

```lean
def finishAlekhnovichPrefixWithAlekhnovich {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (fieldRoots : FieldRootContext F) (Q : CBivariate F) (k : Nat)
    (rootPrefix : RootPrefix F) : Array (CPolynomial F)
```

`CompPoly.GuruswamiSudan.alekhnovichRootCandidates` (definition, [line 199](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Algorithm.lean#L199))

> Materialize bounded-degree candidates from Alekhnovich prefixes.

```lean
def alekhnovichRootCandidates {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (fieldRoots : FieldRootContext F) (Q : CBivariate F) (k : Nat) :
    Array (CPolynomial F)
```

`CompPoly.GuruswamiSudan.alekhnovichRootsYDegreeLt` (definition, [line 208](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Algorithm.lean#L208))

> Alekhnovich bounded-degree roots, with exact final filtering and
> deduplication. The zero bivariate input follows the finite-output convention
> used by the Roth backend and returns no roots.

```lean
def alekhnovichRootsYDegreeLt {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (fieldRoots : FieldRootContext F) (Q : CBivariate F) (k : Nat) :
    Array (CPolynomial F)
```

## Depends on

- [Common Guruswami-Sudan Root Helpers](../common.md)
- [Shifted Substitution for Guruswami-Sudan Root Search](../shiftedsubstitution.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Algorithm.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Algorithm.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Root.Alekhnovich.Algorithm.json)
