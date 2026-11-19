---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.repeatedOddSplitTrialsPMF, CompPoly.CPolynomial.Roots.FiniteField.fallbackAfterOddAttemptsProbability, CompPoly.CPolynomial.Roots.FiniteField.fallbackAfterOddAttempts_probability_le_geometric, CompPoly.CPolynomial.Roots.FiniteField.fallbackAfterOddAttempts_probability_le_geometric_of_uniformProbe, CompPoly.CPolynomial.Roots.FiniteField.repeatedOddSplitTrialsPMF_recursiveFallbackProbabilityModel, CompPoly.CPolynomial.Roots.FiniteField.repeatedOddSplitTrialsPMF_recursiveFallbackProbabilityModel_of_uniformProbe, CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith_uniformTable_none_le_geometric, CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith_uniformTable_none_le_geometric_of_uniformProbe, CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitWithTables, CompPoly.CPolynomial.Roots.FiniteField.uniformProbeTablesPMF, CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitWithTables_length_le, CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitWithTables_rank_le_geometric, CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitWithTables_rank_eq_zero_of_budget_le, CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitWithTables_recursiveFallbackProbabilityModel, CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitWithTables_fallback_probability_le_binomialTail, CompPoly.CPolynomial.Roots.FiniteField.recursiveOddSplitWithTables, CompPoly.CPolynomial.Roots.FiniteField.recursiveOddSplitWithTables_fallback_probability_le_binomialTail, CompPoly.CPolynomial.Roots.FiniteField.lasVegasTryTableSplit, CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitWithTables, CompPoly.CPolynomial.Roots.FiniteField.lasVegasTryTableSplit_isSplitStep, CompPoly.CPolynomial.Roots.FiniteField.lasVegasTryTableSplit_uniformTable_none_le_geometric, CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitWithTables_fallback_probability_le_binomialTail
statement: formalized
proof: formalized
---

# Repeated Odd Trials and Geometric Fallback Bounds

`CompPoly.Univariate.Roots.LasVegas.Probability.Repeated`, in [CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean), by Valerii Huhnin.

> Independent repeated odd-field split trials for one unresolved factor, the
> geometric bound on reaching enumeration fallback, and the one-factor witness of
> the recursive fallback model. The `_of_uniformProbe` variants discharge the
> per-trial half-success hypothesis from the actual uniform probe source.

`CompPoly.CPolynomial.Roots.FiniteField.repeatedOddSplitTrialsPMF` (definition, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L37))

> Independent repeated odd-field split trials for one unresolved factor.

```lean
noncomputable def repeatedOddSplitTrialsPMF {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (q coefficientCount : Nat)
    (g : CPolynomial F) :
    Nat → Nat → PMF (List (TrialResult F))
```

`CompPoly.CPolynomial.Roots.FiniteField.fallbackAfterOddAttemptsProbability` (definition, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L51))

> Probability that the one-factor loop reaches fallback after all split attempts fail.

```lean
noncomputable def fallbackAfterOddAttemptsProbability {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (q coefficientCount : Nat)
    (g : CPolynomial F) (attempts offset : Nat) :
    ℝ≥0∞
```

`CompPoly.CPolynomial.Roots.FiniteField.fallbackAfterOddAttempts_probability_le_geometric` (theorem, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L114))

> If every one-factor trial succeeds with probability at least `1 / 2`, the
> probability of using fallback after `attempts` trials is at most `2^-attempts`.

```lean
theorem fallbackAfterOddAttempts_probability_le_geometric {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (q coefficientCount : Nat)
    (g : CPolynomial F) (attempts offset : Nat)
    (hstep : ∀ i, i < attempts →
      (2 : ℝ≥0∞)⁻¹ ≤
        trialSuccessProbability
          (oddSplitTrialPMF M D enumeration q coefficientCount g (offset + i))) :
    fallbackAfterOddAttemptsProbability M D enumeration q coefficientCount g attempts offset ≤
      ((2 : ℝ≥0∞)⁻¹) ^ attempts
```

`CompPoly.CPolynomial.Roots.FiniteField.fallbackAfterOddAttempts_probability_le_geometric_of_uniformProbe` (theorem, [line 157](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L157))

> For a squarefree finite-field root product over an odd field, the uniform probe
> source reaches enumeration fallback after `attempts` one-factor trials with
> probability at most `2^-attempts`.

```lean
theorem fallbackAfterOddAttempts_probability_le_geometric_of_uniformProbe {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (attempts offset : Nat)
    (hfield : OddUniformFieldModel F q enumeration)
    (hrootProduct : RootProductProbabilityInput q g)
    (hdegree : 2 ≤ CPolynomial.natDegree g) :
    fallbackAfterOddAttemptsProbability M D enumeration.toFieldEnumeration q
        (CPolynomial.natDegree g) g attempts offset ≤
      ((2 : ℝ≥0∞)⁻¹) ^ attempts
```

`CompPoly.CPolynomial.Roots.FiniteField.repeatedOddSplitTrialsPMF_recursiveFallbackProbabilityModel` (theorem, [line 177](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L177))

> The repeated one-factor odd-field trial source satisfies the recursive fallback
> model by concentrating the bad-rank mass at rank `0`.

```lean
theorem repeatedOddSplitTrialsPMF_recursiveFallbackProbabilityModel {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (q coefficientCount : Nat)
    (g : CPolynomial F) (attempts offset degree : Nat)
    (hdegree : 2 ≤ degree)
    (hstep : ∀ i, i < attempts →
      (2 : ℝ≥0∞)⁻¹ ≤
        trialSuccessProbability
          (oddSplitTrialPMF M D enumeration q coefficientCount g (offset + i))) :
    RecursiveFallbackProbabilityModel
      (repeatedOddSplitTrialsPMF M D enumeration q coefficientCount g attempts offset)
      {trials | TrialResult.allFailed trials}
      attempts degree
```

`CompPoly.CPolynomial.Roots.FiniteField.repeatedOddSplitTrialsPMF_recursiveFallbackProbabilityModel_of_uniformProbe` (theorem, [line 216](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L216))

> The one-factor recursive fallback model witness, with the per-trial
> half-success hypothesis discharged from the actual uniform probe source.

```lean
theorem repeatedOddSplitTrialsPMF_recursiveFallbackProbabilityModel_of_uniformProbe {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (attempts offset degree : Nat)
    (hdeg : 2 ≤ degree)
    (hfield : OddUniformFieldModel F q enumeration)
    (hrootProduct : RootProductProbabilityInput q g)
    (hdegree : 2 ≤ CPolynomial.natDegree g) :
    RecursiveFallbackProbabilityModel
      (repeatedOddSplitTrialsPMF M D enumeration.toFieldEnumeration q
        (CPolynomial.natDegree g) g attempts offset)
      {trials | TrialResult.allFailed trials}
      attempts degree
```

`CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith_uniformTable_none_le_geometric` (theorem, [line 244](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L244))

> Bridge to the executable retry loop: the deterministic `tryOddSplitAttemptsWith`,
> driven by a probe table whose entries are sampled independently and uniformly,
> exhausts all attempts with probability at most `2 ^ -attempts`.
>
> Unlike the trial-PMF theorems, the randomized object here is the actual
> runtime function applied to an honestly sampled `ProbeFamily`.

```lean
theorem tryOddSplitAttemptsWith_uniformTable_none_le_geometric {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (q coefficientCount : Nat) (g : CPolynomial F)
    (hstep : (2 : ℝ≥0∞)⁻¹ ≤
      trialSuccessProbability (oddSplitTrialPMF M D enumeration q coefficientCount g 0)) :
    ∀ attempts : Nat,
      eventProbability (uniformProbeTablePMF enumeration coefficientCount attempts)
        {table : List (CPolynomial F) |
          tryOddSplitAttemptsWith M D q (tableProbeFamily table) g attempts 0 = none} ≤
      ((2 : ℝ≥0∞)⁻¹) ^ attempts
```

`CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith_uniformTable_none_le_geometric_of_uniformProbe` (theorem, [line 378](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L378))

> For a squarefree odd-field root product, the executable retry loop driven by an
> honestly sampled uniform probe table reaches fallback with probability at most
> `2 ^ -attempts`.

```lean
theorem tryOddSplitAttemptsWith_uniformTable_none_le_geometric_of_uniformProbe {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (attempts : Nat)
    (hfield : OddUniformFieldModel F q enumeration)
    (hrootProduct : RootProductProbabilityInput q g)
    (hdegree : 2 ≤ CPolynomial.natDegree g) :
    eventProbability
      (uniformProbeTablePMF enumeration.toFieldEnumeration
        (CPolynomial.natDegree g) attempts)
      {table : List (CPolynomial F) |
        tryOddSplitAttemptsWith M D q (tableProbeFamily table) g attempts 0 = none} ≤
    ((2 : ℝ≥0∞)⁻¹) ^ attempts
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitWithTables` (definition, [line 405](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L405))

> Deterministic multi-factor splitter driven by per-factor probe tables: the
> `n`-th processed splittable factor is handed the `n`-th table through the
> abstract per-factor split function `tryTable`. This is a table-driven, fully
> computable mirror of the randomized branch of `lasVegasSplitLoopWith`,
> recording per-factor fallback flags.

```lean
def recursiveSplitWithTables {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (tryTable : List (CPolynomial F) → CPolynomial F → Option (Array (CPolynomial F))) :
    Nat → List (CPolynomial F) → List (List (CPolynomial F)) → List Bool
```

`CompPoly.CPolynomial.Roots.FiniteField.uniformProbeTablesPMF` (definition, [line 424](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L424))

> Independent uniform probe tables, one per processed factor.

```lean
noncomputable def uniformProbeTablesPMF {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (enumeration : FieldEnumeration F) (coefficientCount attempts : Nat) :
    Nat → PMF (List (List (CPolynomial F)))
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitWithTables_length_le` (theorem, [line 479](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L479))

> Table-driven traces never exceed the split budget of the initial stack.

```lean
theorem recursiveSplitWithTables_length_le
    (hsplit : ∀ (g : CPolynomial F), g ≠ 0 →
      ∀ (table : List (CPolynomial F)) (children : Array (CPolynomial F)),
        tryTable table g = some children → IsSplitStep g children) :
    ∀ fuel (stack : List (CPolynomial F)) (tables : List (List (CPolynomial F))),
      (recursiveSplitWithTables tryTable fuel stack tables).length ≤
        stackSplitBudget stack
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitWithTables_rank_le_geometric` (theorem, [line 542](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L542))

> Each processed factor of the table-driven splitter falls back with probability
> at most `2 ^ -attempts` under independently sampled uniform probe tables.

```lean
theorem recursiveSplitWithTables_rank_le_geometric {q : Nat}
    (enumeration : FieldEnumeration F) (coefficientCount attempts : Nat)
    (hsplit : ∀ (g : CPolynomial F), g ≠ 0 →
      ∀ (table : List (CPolynomial F)) (children : Array (CPolynomial F)),
        tryTable table g = some children → IsSplitStep g children)
    (hfail : ∀ (g : CPolynomial F), lasVegasSplitterInput q g →
      2 ≤ CPolynomial.natDegree g →
      (uniformProbeTablePMF enumeration coefficientCount attempts).toOuterMeasure
        {table : List (CPolynomial F) | tryTable table g = none} ≤
      ((2 : ℝ≥0∞)⁻¹) ^ attempts) :
    ∀ fuel (stack : List (CPolynomial F)) (j n : Nat),
      (∀ g ∈ stack, lasVegasSplitterInput q g) →
      eventProbability
        (uniformProbeTablesPMF enumeration coefficientCount attempts n)
        {tables : List (List (CPolynomial F)) |
          (recursiveSplitWithTables tryTable fuel stack tables)[j]? = some true} ≤
      ((2 : ℝ≥0∞)⁻¹) ^ attempts
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitWithTables_rank_eq_zero_of_budget_le` (theorem, [line 696](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L696))

> Table-driven trace entries beyond the split budget never appear.

```lean
theorem recursiveSplitWithTables_rank_eq_zero_of_budget_le
    (enumeration : FieldEnumeration F) (coefficientCount attempts fuel n : Nat)
    (stack : List (CPolynomial F)) {j : Nat}
    (hsplit : ∀ (g : CPolynomial F), g ≠ 0 →
      ∀ (table : List (CPolynomial F)) (children : Array (CPolynomial F)),
        tryTable table g = some children → IsSplitStep g children)
    (hj : stackSplitBudget stack ≤ j) :
    eventProbability
      (uniformProbeTablesPMF enumeration coefficientCount attempts n)
      {tables : List (List (CPolynomial F)) |
        (recursiveSplitWithTables tryTable fuel stack tables)[j]? = some true} =
    0
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitWithTables_recursiveFallbackProbabilityModel` (theorem, [line 723](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L723))

> The table-driven splitter satisfies the recursive fallback model under
> independently sampled uniform probe tables.

```lean
theorem recursiveSplitWithTables_recursiveFallbackProbabilityModel {q : Nat}
    (enumeration : FieldEnumeration F)
    (g : CPolynomial F) (coefficientCount attempts fuel n : Nat)
    (hsplit : ∀ (g : CPolynomial F), g ≠ 0 →
      ∀ (table : List (CPolynomial F)) (children : Array (CPolynomial F)),
        tryTable table g = some children → IsSplitStep g children)
    (hfail : ∀ (g : CPolynomial F), lasVegasSplitterInput q g →
      2 ≤ CPolynomial.natDegree g →
      (uniformProbeTablePMF enumeration coefficientCount attempts).toOuterMeasure
        {table : List (CPolynomial F) | tryTable table g = none} ≤
      ((2 : ℝ≥0∞)⁻¹) ^ attempts)
    (hvalid : lasVegasSplitterInput q g)
    (hattempts : CPolynomial.natDegree g - 2 ≤ attempts) :
    RecursiveFallbackProbabilityModel
      (uniformProbeTablesPMF enumeration coefficientCount attempts n)
      {tables : List (List (CPolynomial F)) |
        true ∈ recursiveSplitWithTables tryTable fuel [g] tables}
      attempts (CPolynomial.natDegree g)
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveSplitWithTables_fallback_probability_le_binomialTail` (theorem, [line 776](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L776))

> Generic recursive table bridge: the deterministic table-driven splitter, with
> one independently sampled uniform probe table per processed factor, reaches
> exhaustive enumeration anywhere in the recursion with probability at most the
> binomial tail.

```lean
theorem recursiveSplitWithTables_fallback_probability_le_binomialTail {q : Nat}
    (enumeration : FieldEnumeration F)
    (g : CPolynomial F) (coefficientCount attempts fuel n : Nat)
    (hsplit : ∀ (g : CPolynomial F), g ≠ 0 →
      ∀ (table : List (CPolynomial F)) (children : Array (CPolynomial F)),
        tryTable table g = some children → IsSplitStep g children)
    (hfail : ∀ (g : CPolynomial F), lasVegasSplitterInput q g →
      2 ≤ CPolynomial.natDegree g →
      (uniformProbeTablePMF enumeration coefficientCount attempts).toOuterMeasure
        {table : List (CPolynomial F) | tryTable table g = none} ≤
      ((2 : ℝ≥0∞)⁻¹) ^ attempts)
    (hvalid : lasVegasSplitterInput q g)
    (hattempts : CPolynomial.natDegree g - 2 ≤ attempts) :
    eventProbability
      (uniformProbeTablesPMF enumeration coefficientCount attempts n)
      {tables : List (List (CPolynomial F)) |
        true ∈ recursiveSplitWithTables tryTable fuel [g] tables} ≤
    binomialFallbackTail attempts (CPolynomial.natDegree g)
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveOddSplitWithTables` (definition, [line 801](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L801))

> Multi-factor odd Cantor-Zassenhaus splitting driven by probe tables.

```lean
def recursiveOddSplitWithTables {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q attempts : Nat) :
    Nat → List (CPolynomial F) → List (List (CPolynomial F)) → List Bool
```

`CompPoly.CPolynomial.Roots.FiniteField.recursiveOddSplitWithTables_fallback_probability_le_binomialTail` (theorem, [line 818](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L818))

> Recursive table bridge for the odd branch: the deterministic table-driven
> splitter, run on a splitter-valid input of degree `d` with one independently
> sampled uniform probe table per processed factor, reaches exhaustive
> enumeration anywhere in the recursion with probability at most the binomial
> tail `2 ^ -attempts * ∑_{j ≤ d - 2} C(attempts, j)`.
>
> The number `n` of supplied tables is arbitrary: missing tables only truncate
> the run, and `d - 1` tables always suffice.

```lean
theorem recursiveOddSplitWithTables_fallback_probability_le_binomialTail {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (coefficientCount attempts fuel n : Nat)
    (hcount : 2 ≤ coefficientCount)
    (hfield : OddUniformFieldModel F q enumeration)
    (hvalid : lasVegasSplitterInput q g)
    (hattempts : CPolynomial.natDegree g - 2 ≤ attempts) :
    eventProbability
      (uniformProbeTablesPMF enumeration.toFieldEnumeration coefficientCount attempts n)
      {tables : List (List (CPolynomial F)) |
        true ∈ recursiveOddSplitWithTables M D q attempts fuel [g] tables} ≤
    binomialFallbackTail attempts (CPolynomial.natDegree g)
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasTryTableSplit` (definition, [line 853](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L853))

> Per-factor table-driven split attempt of the full Las Vegas backend: the odd
> Cantor-Zassenhaus retry loop for odd `q`, the characteristic-two trace retry
> loop when trace metadata is supplied, mirroring the branch selection of
> `lasVegasSplitLoopWith`.

```lean
def lasVegasTryTableSplit {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx? : Option (SmallPrimeTraceContext F)) (q attempts : Nat)
    (table : List (CPolynomial F)) (g : CPolynomial F) :
    Option (Array (CPolynomial F))
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitWithTables` (definition, [line 868](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L868))

> The full Las Vegas backend driven by per-factor probe tables.

```lean
def lasVegasSplitWithTables {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx? : Option (SmallPrimeTraceContext F)) (q attempts : Nat) :
    Nat → List (CPolynomial F) → List (List (CPolynomial F)) → List Bool
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasTryTableSplit_isSplitStep` (theorem, [line 875](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L875))

> Successful backend table attempts are split steps.

```lean
theorem lasVegasTryTableSplit_isSplitStep {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx? : Option (SmallPrimeTraceContext F)) (q attempts : Nat)
    {g : CPolynomial F} (hg : g ≠ 0)
    {table : List (CPolynomial F)} {children : Array (CPolynomial F)}
    (htry : lasVegasTryTableSplit M D traceCtx? q attempts table g = some children) :
    IsSplitStep g children
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasTryTableSplit_uniformTable_none_le_geometric` (theorem, [line 896](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L896))

> Backend table attempts on splitter-valid factors fail with probability at
> most `2 ^ -attempts`.

```lean
theorem lasVegasTryTableSplit_uniformTable_none_le_geometric {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx? : Option (SmallPrimeTraceContext F))
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (coefficientCount attempts : Nat)
    (hcount : 2 ≤ coefficientCount)
    (hmodel : LasVegasUniformFieldModel F q traceCtx? enumeration)
    (g : CPolynomial F) (hvalid : lasVegasSplitterInput q g)
    (hdegree : 2 ≤ CPolynomial.natDegree g) :
    (uniformProbeTablePMF enumeration.toFieldEnumeration coefficientCount
      attempts).toOuterMeasure
      {table : List (CPolynomial F) |
        lasVegasTryTableSplit M D traceCtx? q attempts table g = none} ≤
    ((2 : ℝ≥0∞)⁻¹) ^ attempts
```

`CompPoly.CPolynomial.Roots.FiniteField.lasVegasSplitWithTables_fallback_probability_le_binomialTail` (theorem, [line 960](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean#L960))

> Backend recursive table bridge: over any finite field — odd, or binary with
> matching trace metadata — the deterministic table-driven Las Vegas backend, run
> on a splitter-valid input of degree `d` with one independently sampled uniform
> probe table per processed factor, reaches exhaustive enumeration anywhere in
> the recursion with probability at most the binomial tail
> `2 ^ -attempts * ∑_{j ≤ d - 2} C(attempts, j)`.

```lean
theorem lasVegasSplitWithTables_fallback_probability_le_binomialTail {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx? : Option (SmallPrimeTraceContext F))
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (coefficientCount attempts fuel n : Nat)
    (hcount : 2 ≤ coefficientCount)
    (hmodel : LasVegasUniformFieldModel F q traceCtx? enumeration)
    (hvalid : lasVegasSplitterInput q g)
    (hattempts : CPolynomial.natDegree g - 2 ≤ attempts) :
    eventProbability
      (uniformProbeTablesPMF enumeration.toFieldEnumeration coefficientCount attempts n)
      {tables : List (List (CPolynomial F)) |
        true ∈ lasVegasSplitWithTables M D traceCtx? q attempts fuel [g] tables} ≤
    binomialFallbackTail attempts (CPolynomial.natDegree g)
```

## Depends on

- [Recursive Fallback Analysis for Las Vegas Splitting](recursive.md)

## Sources

- [CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Probability/Repeated.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Univariate.Roots.LasVegas.Probability.Repeated.json)
