---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.ProbeFamily, CompPoly.CPolynomial.Roots.FiniteField.seededLinearProbeFamily, CompPoly.CPolynomial.Roots.FiniteField.tableProbeFamily, CompPoly.CPolynomial.Roots.FiniteField.LasVegasConfig, CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitterInput, CompPoly.CPolynomial.Roots.FiniteField.reduceModWith, CompPoly.CPolynomial.Roots.FiniteField.powModWith, CompPoly.CPolynomial.Roots.FiniteField.tracePowerSumPolynomialLoopWith, CompPoly.CPolynomial.Roots.FiniteField.tracePowerSumPolynomialWith, CompPoly.CPolynomial.Roots.FiniteField.traceBasisProbeFamily, CompPoly.CPolynomial.Roots.FiniteField.isNontrivialProperChild, CompPoly.CPolynomial.Roots.FiniteField.nontrivialProperChildren, CompPoly.CPolynomial.Roots.FiniteField.quotientAfterChild, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith, CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith, CompPoly.CPolynomial.Roots.FiniteField.tryEvenTraceSplitAttemptsWith, CompPoly.CPolynomial.Roots.FiniteField.traceContextMatchesQ, CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitLoopWith, CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitCandidatesWithTrace?, CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitCandidatesWith, CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitCandidatesWithTrace, CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitLinearFactorsWithTrace?, CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitLinearFactorsWith, CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitLinearFactorsWithTrace, CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitLinearFactorsWith_sound, CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitLinearFactorsWithTrace_sound
statement: formalized
proof: formalized
---

# Las Vegas Linear-Factor Splitting

`CompPoly.Univariate.Roots.LasVegas.Basic`, in [CompPoly/Univariate/Roots/LasVegas/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean), by Valerii Huhnin.

> Pure, bounded Las Vegas splitting for finite-field root products. The splitter
> uses the odd-field Cantor-Zassenhaus branch for odd fields, the characteristic
> two trace branch when supplied with compatible trace metadata, and exhaustive
> enumeration after the configured probe cutoff or when no randomized branch is
> available.

`CompPoly.CPolynomial.Roots.FiniteField.ProbeFamily` (structure, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L34))

> Lazy pure probe source for deterministic Las Vegas splitting.

```lean
structure ProbeFamily (F : Type*) [Field F] [BEq F] [LawfulBEq F] where
  probe : Nat → CPolynomial F → Nat → CPolynomial F
```

`CompPoly.CPolynomial.Roots.FiniteField.seededLinearProbeFamily` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L38))

> A simple deterministic affine probe source derived from a natural seed.

```lean
def seededLinearProbeFamily {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (seed : Nat) : ProbeFamily F
```

`CompPoly.CPolynomial.Roots.FiniteField.tableProbeFamily` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L46))

> Probe family reading a finite table of probe polynomials by attempt index.

```lean
def tableProbeFamily {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (table : List (CPolynomial F)) : ProbeFamily F
```

`CompPoly.CPolynomial.Roots.FiniteField.LasVegasConfig` (structure, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L51))

> Configuration for bounded Las Vegas splitting.

```lean
structure LasVegasConfig where
  cutoff : Nat
  tryOddRandomizedSplitting : Bool := true
  tryEvenTraceSplitting : Bool := true
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitterInput` (definition, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L57))

> Root-product input predicate for the Las Vegas splitter.

```lean
def lasVegasSplitterInput {F : Type*} [Field F]
    (q : Nat) (p : CPolynomial F) : Prop
```

`CompPoly.CPolynomial.Roots.FiniteField.reduceModWith` (definition, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L62))

> Reduce a canonical polynomial modulo a canonical modulus with the selected raw backend.

```lean
def reduceModWith {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (D : CPolynomial.Raw.ModContext F) (modulus h : CPolynomial F) :
    CPolynomial F
```

`CompPoly.CPolynomial.Roots.FiniteField.powModWith` (definition, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L71))

> `base^exponent mod modulus`, lifted through the selected raw arithmetic backends.

```lean
def powModWith {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (modulus base : CPolynomial F) (exponent : Nat) :
    CPolynomial F
```

`CompPoly.CPolynomial.Roots.FiniteField.tracePowerSumPolynomialLoopWith` (definition, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L77))

```lean
def tracePowerSumPolynomialLoopWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (modulus : CPolynomial F) (p : Nat) :
    Nat → CPolynomial F → CPolynomial F → CPolynomial F
```

`CompPoly.CPolynomial.Roots.FiniteField.tracePowerSumPolynomialWith` (definition, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L89))

> Polynomial-residue analogue of Shoup's trace power sum.

```lean
def tracePowerSumPolynomialWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (modulus : CPolynomial F) (p k : Nat) (h : CPolynomial F) :
    CPolynomial F
```

`CompPoly.CPolynomial.Roots.FiniteField.traceBasisProbeFamily` (definition, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L103))

> Deterministic trace-coordinate probe family cycling through the Shoup basis.
>
> For characteristic-two contexts this produces probes `beta * X` in basis order,
> which makes the Las Vegas trace branch a bounded randomized-style splitter for
> fixed deterministic benchmark and adapter contexts.

```lean
def traceBasisProbeFamily {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (ctx : SmallPrimeTraceContext F) :
    ProbeFamily F
```

`CompPoly.CPolynomial.Roots.FiniteField.isNontrivialProperChild` (definition, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L111))

> Keep only nonconstant children with strictly smaller representation size than the parent.

```lean
def isNontrivialProperChild {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (parent child : CPolynomial F) : Bool
```

`CompPoly.CPolynomial.Roots.FiniteField.nontrivialProperChildren` (definition, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L116))

> Filter candidate children down to nonconstant, proper children.

```lean
def nontrivialProperChildren {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (parent : CPolynomial F) (children : Array (CPolynomial F)) :
    Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.quotientAfterChild` (definition, [line 121](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L121))

```lean
def quotientAfterChild {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (parent child : CPolynomial F) : CPolynomial F
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith` (definition, [line 136](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L136))

> One odd-field Cantor-Zassenhaus degree-one split attempt.
>
> The probe is reduced modulo `g`, then the split candidates are
> `gcd(g, h)`, `gcd(g / zeroPart, h^((q - 1) / 2) - 1)`, and the remaining
> quotient. The attempt succeeds only when at least two nonconstant proper
> distinct children are produced.

```lean
def cantorZassenhausOddAttemptWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) (probes : ProbeFamily F) (g : CPolynomial F) (attempt : Nat) :
    Option (Array (CPolynomial F))
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith` (definition, [line 160](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L160))

> One characteristic-two trace split attempt.
>
> The probe is reduced modulo `g`, then the trace power sum
> `h + h^2 + ... + h^(2^(m-1))` is computed modulo `g` using the supplied Shoup
> small-prime trace metadata. The attempt succeeds only when `gcd(g, Tr(h))` and
> the remaining quotient are both nonconstant proper children.

```lean
def cantorZassenhausEvenTraceAttemptWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (q : Nat) (probes : ProbeFamily F) (g : CPolynomial F) (attempt : Nat) :
    Option (Array (CPolynomial F))
```

`CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith` (definition, [line 174](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L174))

```lean
def tryOddSplitAttemptsWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) (probes : ProbeFamily F) (g : CPolynomial F) :
    Nat → Nat → Option (Array (CPolynomial F))
```

`CompPoly.CPolynomial.Roots.FiniteField.tryEvenTraceSplitAttemptsWith` (definition, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L185))

```lean
def tryEvenTraceSplitAttemptsWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (q : Nat) (probes : ProbeFamily F) (g : CPolynomial F) :
    Nat → Nat → Option (Array (CPolynomial F))
```

`CompPoly.CPolynomial.Roots.FiniteField.traceContextMatchesQ` (definition, [line 197](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L197))

```lean
def traceContextMatchesQ {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (traceCtx : SmallPrimeTraceContext F) (q : Nat) : Bool
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitLoopWith` (definition, [line 201](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L201))

```lean
def lasVegasSplitLoopWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (traceCtx? : Option (SmallPrimeTraceContext F))
    (cfg : LasVegasConfig)
    (probes : ProbeFamily F) (q : Nat) :
    Nat → List (CPolynomial F) → Array (CPolynomial F) → Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitCandidatesWithTrace?` (definition, [line 246](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L246))

> Candidate linear factors from bounded Las Vegas splitting plus enumeration fallback.

```lean
def lasVegasSplitCandidatesWithTrace? {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (traceCtx? : Option (SmallPrimeTraceContext F))
    (cfg : LasVegasConfig)
    (probes : ProbeFamily F) (q : Nat) (p : CPolynomial F) :
    Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitCandidatesWith` (definition, [line 258](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L258))

> Candidate linear factors using odd splitting only, plus enumeration fallback.

```lean
def lasVegasSplitCandidatesWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (cfg : LasVegasConfig)
    (probes : ProbeFamily F) (q : Nat) (p : CPolynomial F) :
    Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitCandidatesWithTrace` (definition, [line 267](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L267))

> Candidate linear factors using supplied characteristic-two trace metadata when applicable.

```lean
def lasVegasSplitCandidatesWithTrace {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (traceCtx : SmallPrimeTraceContext F)
    (cfg : LasVegasConfig) (probes : ProbeFamily F) (q : Nat) (p : CPolynomial F) :
    Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitLinearFactorsWithTrace?` (definition, [line 276](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L276))

> Las Vegas splitting with optional trace metadata, returning only represented linear factors.

```lean
def lasVegasSplitLinearFactorsWithTrace? {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (traceCtx? : Option (SmallPrimeTraceContext F))
    (cfg : LasVegasConfig)
    (probes : ProbeFamily F) (q : Nat) (p : CPolynomial F) :
    Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitLinearFactorsWith` (definition, [line 287](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L287))

> Las Vegas splitting, returning only represented linear factors.

```lean
def lasVegasSplitLinearFactorsWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (cfg : LasVegasConfig)
    (probes : ProbeFamily F) (q : Nat) (p : CPolynomial F) :
    Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitLinearFactorsWithTrace` (definition, [line 296](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L296))

> Las Vegas splitting using supplied characteristic-two trace metadata when applicable.

```lean
def lasVegasSplitLinearFactorsWithTrace {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (traceCtx : SmallPrimeTraceContext F)
    (cfg : LasVegasConfig) (probes : ProbeFamily F) (q : Nat) (p : CPolynomial F) :
    Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitLinearFactorsWith_sound` (theorem, [line 305](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L305))

> The final Las Vegas filter only keeps represented linear factors.

```lean
theorem lasVegasSplitLinearFactorsWith_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (cfg : LasVegasConfig)
    (probes : ProbeFamily F) (q : Nat) {p factor : CPolynomial F}
    (h : factor ∈
      (lasVegasSplitLinearFactorsWith M D enumeration cfg probes q p).toList) :
    IsLinearFactor factor
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitLinearFactorsWithTrace_sound` (theorem, [line 316](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean#L316))

> The final Las Vegas filter with trace metadata only keeps represented linear factors.

```lean
theorem lasVegasSplitLinearFactorsWithTrace_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (traceCtx : SmallPrimeTraceContext F)
    (cfg : LasVegasConfig) (probes : ProbeFamily F) (q : Nat) {p factor : CPolynomial F}
    (h : factor ∈
      (lasVegasSplitLinearFactorsWithTrace M D enumeration traceCtx cfg probes q p).toList) :
    IsLinearFactor factor
```

## Depends on

- [Exhaustive Finite-Field Root Enumeration](../enumeration.md)
- [Shoup-Style Small-Characteristic Linear-Factor Splitting](../shoup/basic.md)

## Sources

- [CompPoly/Univariate/Roots/LasVegas/Basic.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Basic.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Univariate.Roots.LasVegas.Basic.json)
