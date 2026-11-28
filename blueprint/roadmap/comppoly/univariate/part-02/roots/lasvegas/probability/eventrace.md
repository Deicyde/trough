---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.EvenTraceUniformFieldModel, CompPoly.CPolynomial.Roots.FiniteField.tracePowerSum_eq_zero_or_one, CompPoly.CPolynomial.Roots.FiniteField.tracePowerSum_pair_separated_probability_ge_half, CompPoly.CPolynomial.Roots.FiniteField.evenTraceTrialPMF, CompPoly.CPolynomial.Roots.FiniteField.evenTraceTrial_success_probability_ge_half_of_two_le, CompPoly.CPolynomial.Roots.FiniteField.evenTraceTrial_success_probability_ge_half, CompPoly.CPolynomial.Roots.FiniteField.repeatedEvenTraceTrialsPMF, CompPoly.CPolynomial.Roots.FiniteField.fallbackAfterEvenTraceAttemptsProbability, CompPoly.CPolynomial.Roots.FiniteField.fallbackAfterEvenTraceAttempts_probability_le_geometric, CompPoly.CPolynomial.Roots.FiniteField.fallbackAfterEvenTraceAttempts_probability_le_geometric_of_uniformProbe, CompPoly.CPolynomial.Roots.FiniteField.tryEvenTraceSplitAttemptsWith_uniformTable_none_le_geometric
statement: formalized
proof: formalized
---

# Probability Surface for Characteristic-Two Trace Splitting

`CompPoly.Univariate.Roots.LasVegas.Probability.EvenTrace`, in [CompPoly/Univariate/Roots/LasVegas/Probability/EvenTrace.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/EvenTrace.lean), by Valerii Huhnin.

> Probability analysis of the characteristic-two trace split branch under
> idealized uniform probes: trace power sums take only the values zero and one,
> each trace fiber has exactly half the field, so a uniform probe separates two
> distinct roots into different trace fibers with probability at least `1 / 2`
> and one trace split attempt succeeds with probability at least `1 / 2`.

`CompPoly.CPolynomial.Roots.FiniteField.EvenTraceUniformFieldModel` (structure, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/EvenTrace.lean#L42))

> Probability-facing model for the characteristic-two trace splitter: the trace
> context has base prime two and its cardinality matches both the uniform
> enumeration size and the field cardinality.

```lean
structure EvenTraceUniformFieldModel (F : Type*) (q : Nat)
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (traceCtx : SmallPrimeTraceContext F)
    (enumeration : UniformFieldEnumeration F q) : Prop where
  p_eq : traceCtx.p = 2
  q_eq : traceCtx.q = q
  card_eq : Fintype.card F = q
```

`CompPoly.CPolynomial.Roots.FiniteField.tracePowerSum_eq_zero_or_one` (theorem, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/EvenTrace.lean#L73))

> Trace power sums over a binary field take only the values zero and one.

```lean
theorem tracePowerSum_eq_zero_or_one {F : Type*} [Field F] [Fintype F]
    {k : Nat} (hcard : Fintype.card F = 2 ^ k) (hchar : ringChar F = 2) (x : F) :
    tracePowerSum 2 k x = 0 ∨ tracePowerSum 2 k x = 1
```

`CompPoly.CPolynomial.Roots.FiniteField.tracePowerSum_pair_separated_probability_ge_half` (theorem, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/EvenTrace.lean#L155))

> Two independent uniform field values land in different trace fibers with
> probability at least `1 / 2`.

```lean
theorem tracePowerSum_pair_separated_probability_ge_half {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    {q k : Nat} (enumeration : UniformFieldEnumeration F q)
    (hcard : Fintype.card F = q) (hq : q = 2 ^ k) (hk : 1 ≤ k) :
    (2 : ℝ≥0∞)⁻¹ ≤
      eventProbability
        ((uniformFieldElementPMF enumeration.toFieldEnumeration).bind
          fun x ↦ (uniformFieldElementPMF enumeration.toFieldEnumeration).map
            fun y ↦ (x, y))
        {xy : F × F | tracePowerSum 2 k xy.1 ≠ tracePowerSum 2 k xy.2}
```

`CompPoly.CPolynomial.Roots.FiniteField.evenTraceTrialPMF` (definition, [line 177](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/EvenTrace.lean#L177))

> One characteristic-two trace split trial under a uniform probe distribution.

```lean
noncomputable def evenTraceTrialPMF {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (enumeration : FieldEnumeration F) (q coefficientCount : Nat)
    (g : CPolynomial F) (attempt : Nat) :
    PMF (TrialResult F)
```

`CompPoly.CPolynomial.Roots.FiniteField.evenTraceTrial_success_probability_ge_half_of_two_le` (theorem, [line 197](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/EvenTrace.lean#L197))

> Uniform probe polynomials make one characteristic-two trace split attempt
> succeed with probability at least `1 / 2`: probe values at two distinct roots
> are an independent uniform pair, the pair lands in different trace fibers with
> probability at least `1 / 2`, and trace-separated probes force the executable
> attempt to succeed.

```lean
theorem evenTraceTrial_success_probability_ge_half_of_two_le {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (coefficientCount attempt : Nat)
    (hcount : 2 ≤ coefficientCount)
    (hfield : EvenTraceUniformFieldModel F q traceCtx enumeration)
    (hroots : HasTwoDistinctRoots g)
    (hg : g ≠ 0) :
    (2 : ℝ≥0∞)⁻¹ ≤
      trialSuccessProbability
        (evenTraceTrialPMF M D traceCtx enumeration.toFieldEnumeration q
          coefficientCount g attempt)
```

`CompPoly.CPolynomial.Roots.FiniteField.evenTraceTrial_success_probability_ge_half` (theorem, [line 286](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/EvenTrace.lean#L286))

> Uniform probe polynomials make one characteristic-two trace split attempt
> succeed with probability at least `1 / 2`.

```lean
theorem evenTraceTrial_success_probability_ge_half {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (attempt : Nat)
    (hfield : EvenTraceUniformFieldModel F q traceCtx enumeration)
    (hroots : HasTwoDistinctRoots g)
    (hdegree : 2 ≤ CPolynomial.natDegree g) :
    (2 : ℝ≥0∞)⁻¹ ≤
      trialSuccessProbability
        (evenTraceTrialPMF M D traceCtx enumeration.toFieldEnumeration q
          (CPolynomial.natDegree g) g attempt)
```

`CompPoly.CPolynomial.Roots.FiniteField.repeatedEvenTraceTrialsPMF` (definition, [line 308](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/EvenTrace.lean#L308))

> Independent repeated trace split trials for one unresolved factor.

```lean
noncomputable def repeatedEvenTraceTrialsPMF {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (enumeration : FieldEnumeration F) (q coefficientCount : Nat)
    (g : CPolynomial F) :
    Nat → Nat → PMF (List (TrialResult F))
```

`CompPoly.CPolynomial.Roots.FiniteField.fallbackAfterEvenTraceAttemptsProbability` (definition, [line 323](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/EvenTrace.lean#L323))

> Probability that the trace branch reaches fallback after all attempts fail.

```lean
noncomputable def fallbackAfterEvenTraceAttemptsProbability {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (enumeration : FieldEnumeration F) (q coefficientCount : Nat)
    (g : CPolynomial F) (attempts offset : Nat) :
    ℝ≥0∞
```

`CompPoly.CPolynomial.Roots.FiniteField.fallbackAfterEvenTraceAttempts_probability_le_geometric` (theorem, [line 390](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/EvenTrace.lean#L390))

> If every trace trial succeeds with probability at least `1 / 2`, the
> probability of using fallback after `attempts` trials is at most `2^-attempts`.

```lean
theorem fallbackAfterEvenTraceAttempts_probability_le_geometric {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (enumeration : FieldEnumeration F) (q coefficientCount : Nat)
    (g : CPolynomial F) (attempts offset : Nat)
    (hstep : ∀ i, i < attempts →
      (2 : ℝ≥0∞)⁻¹ ≤
        trialSuccessProbability
          (evenTraceTrialPMF M D traceCtx enumeration q coefficientCount g (offset + i))) :
    fallbackAfterEvenTraceAttemptsProbability M D traceCtx enumeration q coefficientCount g
        attempts offset ≤
      ((2 : ℝ≥0∞)⁻¹) ^ attempts
```

`CompPoly.CPolynomial.Roots.FiniteField.fallbackAfterEvenTraceAttempts_probability_le_geometric_of_uniformProbe` (theorem, [line 436](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/EvenTrace.lean#L436))

> For a squarefree root product over a binary field, the uniform probe source
> reaches enumeration fallback after `attempts` trace trials with probability at
> most `2^-attempts`.

```lean
theorem fallbackAfterEvenTraceAttempts_probability_le_geometric_of_uniformProbe {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (attempts offset : Nat)
    (hfield : EvenTraceUniformFieldModel F q traceCtx enumeration)
    (hrootProduct : RootProductProbabilityInput q g)
    (hdegree : 2 ≤ CPolynomial.natDegree g) :
    fallbackAfterEvenTraceAttemptsProbability M D traceCtx
        enumeration.toFieldEnumeration q (CPolynomial.natDegree g) g attempts offset ≤
      ((2 : ℝ≥0∞)⁻¹) ^ attempts
```

`CompPoly.CPolynomial.Roots.FiniteField.tryEvenTraceSplitAttemptsWith_uniformTable_none_le_geometric` (theorem, [line 459](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/EvenTrace.lean#L459))

> Bridge to the executable trace retry loop: the deterministic
> `tryEvenTraceSplitAttemptsWith`, driven by a probe table whose entries are
> sampled independently and uniformly, exhausts all attempts with probability at
> most `2 ^ -attempts`.

```lean
theorem tryEvenTraceSplitAttemptsWith_uniformTable_none_le_geometric {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (enumeration : FieldEnumeration F) (q coefficientCount : Nat) (g : CPolynomial F)
    (hstep : (2 : ℝ≥0∞)⁻¹ ≤
      trialSuccessProbability
        (evenTraceTrialPMF M D traceCtx enumeration q coefficientCount g 0)) :
    ∀ attempts : Nat,
      eventProbability (uniformProbeTablePMF enumeration coefficientCount attempts)
        {table : List (CPolynomial F) |
          tryEvenTraceSplitAttemptsWith M D traceCtx q (tableProbeFamily table) g
            attempts 0 = none} ≤
      ((2 : ℝ≥0∞)⁻¹) ^ attempts
```

## Depends on

- [One Odd Cantor-Zassenhaus Trial Under Uniform Probes](oddtrial.md)

## Proof depends on

- [Even-Trace Split Correctness for Las Vegas Splitting](../correctness/eventrace.md)

## Sources

- [CompPoly/Univariate/Roots/LasVegas/Probability/EvenTrace.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/EvenTrace.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Univariate.Roots.LasVegas.Probability.EvenTrace.json)
