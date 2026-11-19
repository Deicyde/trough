---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.binomialFallbackTail, CompPoly.CPolynomial.Roots.FiniteField.binomialTailCutoffPredicate, CompPoly.CPolynomial.Roots.FiniteField.RecursiveFallbackProbabilityModel, CompPoly.CPolynomial.Roots.FiniteField.recursiveFallback_probability_le_binomialTail, CompPoly.CPolynomial.Roots.FiniteField.toOuterMeasure_apply_le_one, CompPoly.CPolynomial.Roots.FiniteField.firstSuccessPMF, CompPoly.CPolynomial.Roots.FiniteField.firstSuccessPMF_apply_none_le_geometric, CompPoly.CPolynomial.Roots.FiniteField.firstSuccessPMF_support_some, CompPoly.CPolynomial.Roots.FiniteField.IsSplitStep, CompPoly.CPolynomial.Roots.FiniteField.stackSplitBudget, CompPoly.CPolynomial.Roots.FiniteField.stackSplitBudget_append, CompPoly.CPolynomial.Roots.FiniteField.stackWork_eq_two_mul_budget_add_length, CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitProcessPMF, CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitProcessPMF_support_length, CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitProcessPMF_rank_le_geometric, CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitProcessPMF_rank_eq_zero_of_budget_le, CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitProcessPMF_recursiveFallbackProbabilityModel, CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitProcessPMF_fallback_probability_le_binomialTail, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_isSplitStep, CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith_isSplitStep, CompPoly.CPolynomial.Roots.FiniteField.oddSplitTrialPMF_support_isSplitStep, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith_isSplitStep, CompPoly.CPolynomial.Roots.FiniteField.tryEvenTraceSplitAttemptsWith_isSplitStep, CompPoly.CPolynomial.Roots.FiniteField.evenTraceTrialPMF_support_isSplitStep, CompPoly.CPolynomial.Roots.FiniteField.recursiveOddSplitProcessPMF, CompPoly.CPolynomial.Roots.FiniteField.recursiveOddSplitProcessPMF_recursiveFallbackProbabilityModel, CompPoly.CPolynomial.Roots.FiniteField.recursiveOddSplitProcessPMF_fallback_probability_le_binomialTail, CompPoly.CPolynomial.Roots.FiniteField.recursiveEvenTraceSplitProcessPMF, CompPoly.CPolynomial.Roots.FiniteField.recursiveEvenTraceSplitProcessPMF_recursiveFallbackProbabilityModel, CompPoly.CPolynomial.Roots.FiniteField.recursiveEvenTraceSplitProcessPMF_fallback_probability_le_binomialTail, CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitTrialPMF, CompPoly.CPolynomial.Roots.FiniteField.LasVegasUniformFieldModel, CompPoly.CPolynomial.Roots.FiniteField.LasVegasUniformFieldModel.card_eq, CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitTrialPMF_support_isSplitStep, CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitTrialPMF_success_probability_ge_half, CompPoly.CPolynomial.Roots.FiniteField.lasVegasRecursiveSplitProcessPMF, CompPoly.CPolynomial.Roots.FiniteField.lasVegasRecursiveSplitProcessPMF_fallback_probability_le_binomialTail, CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_lasVegas_fallback_probability_le_binomialTail
statement: formalized
proof: formalized
---

# Recursive Fallback Analysis for Las Vegas Splitting

`CompPoly.Univariate.Roots.LasVegas.Probability.Recursive`, in [CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean), by Valerii Huhnin.

> The abstract binomial-tail bound for recursive fallback, together with the
> multi-factor splitting process that witnesses it: the process tracks the full
> stack of unresolved factors, gives every splittable factor its own batch of
> independent uniform probes, and records which factors fell back to enumeration.

`CompPoly.CPolynomial.Roots.FiniteField.binomialFallbackTail` (definition, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L40))

> …

```lean
noncomputable def binomialFallbackTail (attempts degree : Nat) : ℝ≥0∞
```

`CompPoly.CPolynomial.Roots.FiniteField.binomialTailCutoffPredicate` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L45))

> A cutoff meets the binomial-tail target for field cardinality `q`.

```lean
def binomialTailCutoffPredicate (q degree attempts : Nat) : Prop
```

`CompPoly.CPolynomial.Roots.FiniteField.RecursiveFallbackProbabilityModel` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L52))

> …

```lean
def RecursiveFallbackProbabilityModel {Ω : Type*}
    (process : PMF Ω) (fallbackEvent : Set Ω)
    (attempts degree : Nat) : Prop
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveFallback_probability_le_binomialTail` (theorem, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L68))

> Target theorem for the full recursive splitter: under the independence and
> root-product hypotheses represented by the future recursion model, fallback is
> bounded by the binomial tail.

```lean
theorem recursiveFallback_probability_le_binomialTail {Ω : Type*}
    (process : PMF Ω) (fallbackEvent : Set Ω)
    (attempts degree : Nat)
    (hmodel : RecursiveFallbackProbabilityModel process fallbackEvent attempts degree) :
    eventProbability process fallbackEvent ≤ binomialFallbackTail attempts degree
```

`CompPoly.CPolynomial.Roots.FiniteField.toOuterMeasure_apply_le_one` (theorem, [line 104](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L104))

```lean
theorem toOuterMeasure_apply_le_one {α : Type*} (p : PMF α) (s : Set α) :
    p.toOuterMeasure s ≤ 1
```

`CompPoly.CPolynomial.Roots.FiniteField.firstSuccessPMF` (definition, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L112))

> First successful split among independent trials, or `none` after exhaustion.

```lean
noncomputable def firstSuccessPMF {F : Type*} [Zero F]
    (trial : Nat → PMF (TrialResult F)) :
    Nat → Nat → PMF (Option (Array (CPolynomial F)))
```

`CompPoly.CPolynomial.Roots.FiniteField.firstSuccessPMF_apply_none_le_geometric` (theorem, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L123))

> Trials that succeed at rate one half are all survived with probability
> at most `2 ^ -attempts`.

```lean
theorem firstSuccessPMF_apply_none_le_geometric {F : Type*} [Zero F]
    (trial : Nat → PMF (TrialResult F)) :
    ∀ attempts offset,
      (∀ i, i < attempts →
        (2 : ℝ≥0∞)⁻¹ ≤ trialSuccessProbability (trial (offset + i))) →
      (firstSuccessPMF trial attempts offset) none ≤ ((2 : ℝ≥0∞)⁻¹) ^ attempts
```

`CompPoly.CPolynomial.Roots.FiniteField.firstSuccessPMF_support_some` (theorem, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L155))

> A successful batch outcome lies in the support of some individual trial.

```lean
theorem firstSuccessPMF_support_some {F : Type*} [Zero F]
    (trial : Nat → PMF (TrialResult F)) :
    ∀ attempts offset {children : Array (CPolynomial F)},
      some children ∈ (firstSuccessPMF trial attempts offset).support →
      ∃ attempt, TrialResult.split children ∈ (trial attempt).support
```

`CompPoly.CPolynomial.Roots.FiniteField.IsSplitStep` (definition, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L185))

> Facts a split trial guarantees about successful children: at least two of them,
> each a nonzero nonconstant divisor of the parent, with total split work
> strictly below the parent's.

```lean
def IsSplitStep {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (g : CPolynomial F) (children : Array (CPolynomial F)) : Prop
```

`CompPoly.CPolynomial.Roots.FiniteField.stackSplitBudget` (definition, [line 193](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L193))

> Number of splits a stack of unresolved factors can still require.

```lean
noncomputable def stackSplitBudget {F : Type*} [Field F] [BEq F] [LawfulBEq F] :
    List (CPolynomial F) → Nat
```

`CompPoly.CPolynomial.Roots.FiniteField.stackSplitBudget_append` (theorem, [line 198](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L198))

```lean
theorem stackSplitBudget_append {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (xs ys : List (CPolynomial F)) :
    stackSplitBudget (xs ++ ys) = stackSplitBudget xs + stackSplitBudget ys
```

`CompPoly.CPolynomial.Roots.FiniteField.stackWork_eq_two_mul_budget_add_length` (theorem, [line 207](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L207))

```lean
theorem stackWork_eq_two_mul_budget_add_length {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] (l : List (CPolynomial F))
    (hpos : ∀ g ∈ l, 1 ≤ g.toPoly.natDegree) :
    stackWork l = 2 * stackSplitBudget l + l.length
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitProcessPMF` (definition, [line 231](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L231))

> Multi-factor Las Vegas splitting process for an abstract per-factor trial
> family.
>
> The stack of unresolved factors is processed sequentially. Every factor of
> degree at least two receives its own batch of `attempts` independent trials;
> the resulting trace records, in processing order, whether each such factor
> fell back to enumeration (`true`) or split into children that are pushed back
> onto the stack (`false`). This is the idealized-probe model of
> `lasVegasSplitLoopWith`, which retries each unresolved factor up to the
> configured cutoff before enumerating it.

```lean
noncomputable def recursiveSplitProcessPMF {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (trial : CPolynomial F → Nat → PMF (TrialResult F)) (attempts : Nat) :
    Nat → List (CPolynomial F) → PMF (List Bool)
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitProcessPMF_support_length` (theorem, [line 248](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L248))

> Process traces never exceed the split budget of the initial stack.

```lean
theorem recursiveSplitProcessPMF_support_length {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (trial : CPolynomial F → Nat → PMF (TrialResult F)) (attempts : Nat)
    (hsplit : ∀ (g : CPolynomial F), g ≠ 0 →
      ∀ (attempt : Nat) (children : Array (CPolynomial F)),
        TrialResult.split children ∈ (trial g attempt).support →
        IsSplitStep g children) :
    ∀ fuel (stack : List (CPolynomial F)) {tr2 : List Bool},
      tr2 ∈ (recursiveSplitProcessPMF trial attempts fuel stack).support →
      tr2.length ≤ stackSplitBudget stack
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitProcessPMF_rank_le_geometric` (theorem, [line 320](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L320))

> Each processed factor falls back with probability at most `2 ^ -attempts`:
> the `j`-th entry of the process trace is `true` with at most that probability.

```lean
theorem recursiveSplitProcessPMF_rank_le_geometric {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (trial : CPolynomial F → Nat → PMF (TrialResult F)) {q : Nat} (attempts : Nat)
    (hsplit : ∀ (g : CPolynomial F), g ≠ 0 →
      ∀ (attempt : Nat) (children : Array (CPolynomial F)),
        TrialResult.split children ∈ (trial g attempt).support →
        IsSplitStep g children)
    (hhalf : ∀ (g : CPolynomial F), lasVegasSplitterInput q g →
      2 ≤ CPolynomial.natDegree g → ∀ attempt : Nat,
        (2 : ℝ≥0∞)⁻¹ ≤ trialSuccessProbability (trial g attempt)) :
    ∀ fuel (stack : List (CPolynomial F)) (j : Nat),
      (∀ g ∈ stack, lasVegasSplitterInput q g) →
      eventProbability
        (recursiveSplitProcessPMF trial attempts fuel stack)
        {tr2 : List Bool | tr2[j]? = some true} ≤
      ((2 : ℝ≥0∞)⁻¹) ^ attempts
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitProcessPMF_rank_eq_zero_of_budget_le` (theorem, [line 426](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L426))

> Trace entries beyond the split budget of the stack never appear.

```lean
theorem recursiveSplitProcessPMF_rank_eq_zero_of_budget_le {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (trial : CPolynomial F → Nat → PMF (TrialResult F)) (attempts : Nat)
    (hsplit : ∀ (g : CPolynomial F), g ≠ 0 →
      ∀ (attempt : Nat) (children : Array (CPolynomial F)),
        TrialResult.split children ∈ (trial g attempt).support →
        IsSplitStep g children)
    (fuel : Nat) (stack : List (CPolynomial F)) {j : Nat}
    (hj : stackSplitBudget stack ≤ j) :
    eventProbability
      (recursiveSplitProcessPMF trial attempts fuel stack)
      {tr2 : List Bool | tr2[j]? = some true} = 0
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitProcessPMF_recursiveFallbackProbabilityModel` (theorem, [line 451](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L451))

> The multi-factor splitting process satisfies the recursive fallback model:
> the `j`-th rank event is "the `j`-th processed splittable factor fell back",
> there are at most `degree - 1` such factors, and each falls back with
> probability at most `2 ^ -attempts ≤ choose attempts j * 2 ^ -attempts`.

```lean
theorem recursiveSplitProcessPMF_recursiveFallbackProbabilityModel {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (trial : CPolynomial F → Nat → PMF (TrialResult F)) {q : Nat}
    (g : CPolynomial F) (attempts fuel : Nat)
    (hsplit : ∀ (g : CPolynomial F), g ≠ 0 →
      ∀ (attempt : Nat) (children : Array (CPolynomial F)),
        TrialResult.split children ∈ (trial g attempt).support →
        IsSplitStep g children)
    (hhalf : ∀ (g : CPolynomial F), lasVegasSplitterInput q g →
      2 ≤ CPolynomial.natDegree g → ∀ attempt : Nat,
        (2 : ℝ≥0∞)⁻¹ ≤ trialSuccessProbability (trial g attempt))
    (hvalid : lasVegasSplitterInput q g)
    (hattempts : CPolynomial.natDegree g - 2 ≤ attempts) :
    RecursiveFallbackProbabilityModel
      (recursiveSplitProcessPMF trial attempts fuel [g])
      {tr2 : List Bool | true ∈ tr2}
      attempts (CPolynomial.natDegree g)
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitProcessPMF_fallback_probability_le_binomialTail` (theorem, [line 499](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L499))

> Generic recursive fallback bound: any per-factor trial family that succeeds at
> rate one half on splitter-valid factors keeps the full recursion's fallback
> probability below the binomial tail.

```lean
theorem recursiveSplitProcessPMF_fallback_probability_le_binomialTail {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (trial : CPolynomial F → Nat → PMF (TrialResult F)) {q : Nat}
    (g : CPolynomial F) (attempts fuel : Nat)
    (hsplit : ∀ (g : CPolynomial F), g ≠ 0 →
      ∀ (attempt : Nat) (children : Array (CPolynomial F)),
        TrialResult.split children ∈ (trial g attempt).support →
        IsSplitStep g children)
    (hhalf : ∀ (g : CPolynomial F), lasVegasSplitterInput q g →
      2 ≤ CPolynomial.natDegree g → ∀ attempt : Nat,
        (2 : ℝ≥0∞)⁻¹ ≤ trialSuccessProbability (trial g attempt))
    (hvalid : lasVegasSplitterInput q g)
    (hattempts : CPolynomial.natDegree g - 2 ≤ attempts) :
    eventProbability
      (recursiveSplitProcessPMF trial attempts fuel [g])
      {tr2 : List Bool | true ∈ tr2} ≤
    binomialFallbackTail attempts (CPolynomial.natDegree g)
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_isSplitStep` (theorem, [line 521](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L521))

> Successful odd split attempts are split steps.

```lean
theorem cantorZassenhausOddAttemptWith_isSplitStep {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) (probes : ProbeFamily F) {g : CPolynomial F} (hg : g ≠ 0)
    {attempt : Nat} {children : Array (CPolynomial F)}
    (htry : cantorZassenhausOddAttemptWith M D q probes g attempt = some children) :
    IsSplitStep g children
```

`CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith_isSplitStep` (theorem, [line 542](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L542))

> Successful retry-loop results are split steps.

```lean
theorem tryOddSplitAttemptsWith_isSplitStep {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) (probes : ProbeFamily F) {g : CPolynomial F} (hg : g ≠ 0)
    {attempts offset : Nat} {children : Array (CPolynomial F)}
    (htry : tryOddSplitAttemptsWith M D q probes g attempts offset = some children) :
    IsSplitStep g children
```

`CompPoly.CPolynomial.Roots.FiniteField.oddSplitTrialPMF_support_isSplitStep` (theorem, [line 554](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L554))

> Successful odd split trials are split steps.

```lean
theorem oddSplitTrialPMF_support_isSplitStep {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (q : Nat) {g : CPolynomial F} (hg : g ≠ 0)
    {attempt : Nat} {children : Array (CPolynomial F)}
    (hmem : TrialResult.split children ∈
      (oddSplitTrialPMF M D enumeration q (CPolynomial.natDegree g) g attempt).support) :
    IsSplitStep g children
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith_isSplitStep` (theorem, [line 576](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L576))

> Successful trace split attempts are split steps.

```lean
theorem cantorZassenhausEvenTraceAttemptWith_isSplitStep {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (q : Nat) (probes : ProbeFamily F) {g : CPolynomial F} (hg : g ≠ 0)
    {attempt : Nat} {children : Array (CPolynomial F)}
    (htry : cantorZassenhausEvenTraceAttemptWith M D traceCtx q probes g attempt =
      some children) :
    IsSplitStep g children
```

`CompPoly.CPolynomial.Roots.FiniteField.tryEvenTraceSplitAttemptsWith_isSplitStep` (theorem, [line 602](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L602))

> Successful trace retry-loop results are split steps.

```lean
theorem tryEvenTraceSplitAttemptsWith_isSplitStep {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (q : Nat) (probes : ProbeFamily F) {g : CPolynomial F} (hg : g ≠ 0)
    {attempts offset : Nat} {children : Array (CPolynomial F)}
    (htry : tryEvenTraceSplitAttemptsWith M D traceCtx q probes g attempts offset =
      some children) :
    IsSplitStep g children
```

`CompPoly.CPolynomial.Roots.FiniteField.evenTraceTrialPMF_support_isSplitStep` (theorem, [line 617](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L617))

> Successful trace split trials are split steps.

```lean
theorem evenTraceTrialPMF_support_isSplitStep {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (enumeration : FieldEnumeration F) (q : Nat) {g : CPolynomial F} (hg : g ≠ 0)
    {attempt : Nat} {children : Array (CPolynomial F)}
    (hmem : TrialResult.split children ∈
      (evenTraceTrialPMF M D traceCtx enumeration q (CPolynomial.natDegree g)
        g attempt).support) :
    IsSplitStep g children
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveOddSplitProcessPMF` (definition, [line 642](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L642))

> Multi-factor odd Cantor-Zassenhaus splitting under uniform probes.

```lean
noncomputable def recursiveOddSplitProcessPMF {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (q attempts : Nat) :
    Nat → List (CPolynomial F) → PMF (List Bool)
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveOddSplitProcessPMF_recursiveFallbackProbabilityModel` (theorem, [line 652](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L652))

> The odd multi-factor process satisfies the recursive fallback model.

```lean
theorem recursiveOddSplitProcessPMF_recursiveFallbackProbabilityModel {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (attempts fuel : Nat)
    (hfield : OddUniformFieldModel F q enumeration)
    (hvalid : lasVegasSplitterInput q g)
    (hattempts : CPolynomial.natDegree g - 2 ≤ attempts) :
    RecursiveFallbackProbabilityModel
      (recursiveOddSplitProcessPMF M D enumeration.toFieldEnumeration q attempts fuel [g])
      {tr2 : List Bool | true ∈ tr2}
      attempts (CPolynomial.natDegree g)
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveOddSplitProcessPMF_fallback_probability_le_binomialTail` (theorem, [line 678](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L678))

> Full recursive fallback bound for the odd branch: starting from a root product
> of degree `d`, the probability that any factor anywhere in the recursion falls
> back to exhaustive enumeration is at most the binomial tail
> `2 ^ -attempts * ∑_{j ≤ d - 2} C(attempts, j)`.

```lean
theorem recursiveOddSplitProcessPMF_fallback_probability_le_binomialTail {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (attempts fuel : Nat)
    (hfield : OddUniformFieldModel F q enumeration)
    (hvalid : lasVegasSplitterInput q g)
    (hattempts : CPolynomial.natDegree g - 2 ≤ attempts) :
    eventProbability
      (recursiveOddSplitProcessPMF M D enumeration.toFieldEnumeration q attempts fuel [g])
      {tr2 : List Bool | true ∈ tr2} ≤
    binomialFallbackTail attempts (CPolynomial.natDegree g)
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveEvenTraceSplitProcessPMF` (definition, [line 695](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L695))

> Multi-factor characteristic-two trace splitting under uniform probes.

```lean
noncomputable def recursiveEvenTraceSplitProcessPMF {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (enumeration : FieldEnumeration F) (q attempts : Nat) :
    Nat → List (CPolynomial F) → PMF (List Bool)
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveEvenTraceSplitProcessPMF_recursiveFallbackProbabilityModel` (theorem, [line 707](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L707))

> The trace multi-factor process satisfies the recursive fallback model.

```lean
theorem recursiveEvenTraceSplitProcessPMF_recursiveFallbackProbabilityModel {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (attempts fuel : Nat)
    (hfield : EvenTraceUniformFieldModel F q traceCtx enumeration)
    (hvalid : lasVegasSplitterInput q g)
    (hattempts : CPolynomial.natDegree g - 2 ≤ attempts) :
    RecursiveFallbackProbabilityModel
      (recursiveEvenTraceSplitProcessPMF M D traceCtx enumeration.toFieldEnumeration q
        attempts fuel [g])
      {tr2 : List Bool | true ∈ tr2}
      attempts (CPolynomial.natDegree g)
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveEvenTraceSplitProcessPMF_fallback_probability_le_binomialTail` (theorem, [line 734](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L734))

> Full recursive fallback bound for the characteristic-two trace branch.

```lean
theorem recursiveEvenTraceSplitProcessPMF_fallback_probability_le_binomialTail {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (attempts fuel : Nat)
    (hfield : EvenTraceUniformFieldModel F q traceCtx enumeration)
    (hvalid : lasVegasSplitterInput q g)
    (hattempts : CPolynomial.natDegree g - 2 ≤ attempts) :
    eventProbability
      (recursiveEvenTraceSplitProcessPMF M D traceCtx enumeration.toFieldEnumeration q
        attempts fuel [g])
      {tr2 : List Bool | true ∈ tr2} ≤
    binomialFallbackTail attempts (CPolynomial.natDegree g)
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitTrialPMF` (definition, [line 757](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L757))

> Per-factor trial of the full Las Vegas backend: the odd Cantor-Zassenhaus
> branch for odd `q`, the characteristic-two trace branch when trace metadata is
> supplied, mirroring the branch selection of `lasVegasSplitLoopWith`.

```lean
noncomputable def lasVegasSplitTrialPMF {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx? : Option (SmallPrimeTraceContext F))
    (enumeration : FieldEnumeration F) (q : Nat)
    (g : CPolynomial F) (attempt : Nat) : PMF (TrialResult F)
```

`CompPoly.CPolynomial.Roots.FiniteField.LasVegasUniformFieldModel` (inductive type, [line 776](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L776))

> Probability-facing model for the full Las Vegas backend: either the field has
> odd cardinality, or it is a binary field presented with matching trace
> metadata.

```lean
inductive LasVegasUniformFieldModel (F : Type*) (q : Nat)
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (traceCtx? : Option (SmallPrimeTraceContext F))
    (enumeration : UniformFieldEnumeration F q) : Prop
  | odd (hodd : q % 2 = 1) (hfield : OddUniformFieldModel F q enumeration)
  | evenTrace (traceCtx : SmallPrimeTraceContext F)
      (hctx : traceCtx? = some traceCtx) (heven : q % 2 = 0)
      (hfield : EvenTraceUniformFieldModel F q traceCtx enumeration)
```

`CompPoly.CPolynomial.Roots.FiniteField.LasVegasUniformFieldModel.card_eq` (theorem, [line 785](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L785))

```lean
theorem LasVegasUniformFieldModel.card_eq {F : Type*} {q : Nat}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    {traceCtx? : Option (SmallPrimeTraceContext F)}
    {enumeration : UniformFieldEnumeration F q}
    (hmodel : LasVegasUniformFieldModel F q traceCtx? enumeration) :
    Fintype.card F = q
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitTrialPMF_support_isSplitStep` (theorem, [line 796](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L796))

> Successful backend trials are split steps.

```lean
theorem lasVegasSplitTrialPMF_support_isSplitStep {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx? : Option (SmallPrimeTraceContext F))
    (enumeration : FieldEnumeration F) (q : Nat) {g : CPolynomial F} (hg : g ≠ 0)
    {attempt : Nat} {children : Array (CPolynomial F)}
    (hmem : TrialResult.split children ∈
      (lasVegasSplitTrialPMF M D traceCtx? enumeration q g attempt).support) :
    IsSplitStep g children
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitTrialPMF_success_probability_ge_half` (theorem, [line 817](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L817))

> Backend trials on splitter-valid factors succeed at rate one half.

```lean
theorem lasVegasSplitTrialPMF_success_probability_ge_half {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx? : Option (SmallPrimeTraceContext F))
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (hmodel : LasVegasUniformFieldModel F q traceCtx? enumeration)
    (g : CPolynomial F) (hvalid : lasVegasSplitterInput q g)
    (hdegree : 2 ≤ CPolynomial.natDegree g) (attempt : Nat) :
    (2 : ℝ≥0∞)⁻¹ ≤
      trialSuccessProbability
        (lasVegasSplitTrialPMF M D traceCtx? enumeration.toFieldEnumeration q g attempt)
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasRecursiveSplitProcessPMF` (definition, [line 858](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L858))

> The full Las Vegas backend recursion under idealized uniform probes,
> dispatching between the odd and trace branches by field characteristic.

```lean
noncomputable def lasVegasRecursiveSplitProcessPMF {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx? : Option (SmallPrimeTraceContext F))
    (enumeration : FieldEnumeration F) (q attempts : Nat) :
    Nat → List (CPolynomial F) → PMF (List Bool)
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasRecursiveSplitProcessPMF_fallback_probability_le_binomialTail` (theorem, [line 872](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L872))

> Backend-level recursive fallback bound: over any finite field — odd, or binary
> with matching trace metadata — the full Las Vegas recursion on a splitter-valid
> input of degree `d` reaches exhaustive enumeration anywhere with probability at
> most the binomial tail `2 ^ -attempts * ∑_{j ≤ d - 2} C(attempts, j)`.

```lean
theorem lasVegasRecursiveSplitProcessPMF_fallback_probability_le_binomialTail {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx? : Option (SmallPrimeTraceContext F))
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (attempts fuel : Nat)
    (hmodel : LasVegasUniformFieldModel F q traceCtx? enumeration)
    (hvalid : lasVegasSplitterInput q g)
    (hattempts : CPolynomial.natDegree g - 2 ≤ attempts) :
    eventProbability
      (lasVegasRecursiveSplitProcessPMF M D traceCtx? enumeration.toFieldEnumeration q
        attempts fuel [g])
      {tr2 : List Bool | true ∈ tr2} ≤
    binomialFallbackTail attempts (CPolynomial.natDegree g)
```

`CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_lasVegas_fallback_probability_le_binomialTail` (theorem, [line 901](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean#L901))

> Headline backend theorem: for any nonzero polynomial over a finite field — odd,
> or binary with matching trace metadata — the Las Vegas backend run on its
> finite-field root product reaches exhaustive enumeration anywhere in the
> recursion with probability at most the binomial tail in the attempt cutoff.

```lean
theorem finiteFieldRootProductWith_lasVegas_fallback_probability_le_binomialTail
    {F : Type*} [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : FiniteFieldContext F) (traceCtx? : Option (SmallPrimeTraceContext F))
    (enumeration : UniformFieldEnumeration F ctx.q)
    {p : CPolynomial F} (attempts fuel : Nat)
    (hmodel : LasVegasUniformFieldModel F ctx.q traceCtx? enumeration)
    (hp : p ≠ 0)
    (hattempts :
      CPolynomial.natDegree (finiteFieldRootProductWith M D ctx p) - 2 ≤ attempts) :
    eventProbability
      (lasVegasRecursiveSplitProcessPMF M D traceCtx? enumeration.toFieldEnumeration
        ctx.q attempts fuel [finiteFieldRootProductWith M D ctx p])
      {tr2 : List Bool | true ∈ tr2} ≤
    binomialFallbackTail attempts
      (CPolynomial.natDegree (finiteFieldRootProductWith M D ctx p))
```

## Depends on

- [Shared Correctness Lemmas for Las Vegas Splitting](../correctness/common.md)
- [Probability Surface for Characteristic-Two Trace Splitting](eventrace.md)

## Sources

- [CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Recursive.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Univariate.Roots.LasVegas.Probability.Recursive.json)
