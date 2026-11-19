---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith_child_proper, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith_stackWork_le, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith_child_normSplitWork_pos, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith_probe_congr, CompPoly.CPolynomial.Roots.FiniteField.tryEvenTraceSplitAttemptsWith_probe_congr, CompPoly.CPolynomial.Roots.FiniteField.tryEvenTraceSplitAttemptsWith_eq_some_exists_attempt, CompPoly.CPolynomial.Roots.FiniteField.tryEvenTraceSplitAttemptsWith_root, CompPoly.CPolynomial.Roots.FiniteField.tryEvenTraceSplitAttemptsWith_stackWork_le, CompPoly.CPolynomial.Roots.FiniteField.tryEvenTraceSplitAttemptsWith_child_normSplitWork_pos, CompPoly.CPolynomial.Roots.FiniteField.eval_tracePowerSumPolynomialWith_eq, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith_size_ge_two, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith_child_dvd_input, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith_success_of_trace_separated
statement: formalized
proof: formalized
---

# Even-Trace Split Correctness for Las Vegas Splitting

`CompPoly.Univariate.Roots.LasVegas.Correctness.EvenTrace`, in [CompPoly/Univariate/Roots/LasVegas/Correctness/EvenTrace.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/EvenTrace.lean), by Valerii Huhnin.

> Correctness lemmas for the characteristic-two trace split attempt and retry loop.

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith_child_proper` (theorem, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/EvenTrace.lean#L74))

```lean
theorem cantorZassenhausEvenTraceAttemptWith_child_proper {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (q : Nat) (probes : ProbeFamily F) {g child : CPolynomial F}
    {attempt : Nat} {children : Array (CPolynomial F)}
    (htry :
      cantorZassenhausEvenTraceAttemptWith M D traceCtx q probes g attempt = some children)
    (hmem : child ∈ children.toList) :
    isNontrivialProperChild (CPolynomial.monicNormalize g) child = true
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith_stackWork_le` (theorem, [line 94](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/EvenTrace.lean#L94))

```lean
theorem cantorZassenhausEvenTraceAttemptWith_stackWork_le {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (q : Nat) (probes : ProbeFamily F) {g : CPolynomial F}
    {attempt : Nat} {children : Array (CPolynomial F)}
    (htry :
      cantorZassenhausEvenTraceAttemptWith M D traceCtx q probes g attempt = some children)
    (hg : g ≠ 0) :
    stackWork children.toList ≤ splitWork (CPolynomial.monicNormalize g) - 1
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith_child_normSplitWork_pos` (theorem, [line 160](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/EvenTrace.lean#L160))

```lean
theorem cantorZassenhausEvenTraceAttemptWith_child_normSplitWork_pos {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (q : Nat) (probes : ProbeFamily F) {g child : CPolynomial F}
    {attempt : Nat} {children : Array (CPolynomial F)}
    (htry :
      cantorZassenhausEvenTraceAttemptWith M D traceCtx q probes g attempt = some children)
    (hg : g ≠ 0) (hmem : child ∈ children.toList) :
    1 ≤ normSplitWork child
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith_probe_congr` (theorem, [line 238](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/EvenTrace.lean#L238))

> The trace split attempt depends on the probe family only through the probe
> it actually draws.

```lean
theorem cantorZassenhausEvenTraceAttemptWith_probe_congr {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (q : Nat) {p1 p2 : ProbeFamily F} {g : CPolynomial F} {a1 a2 : Nat}
    (hprobe : p1.probe q (CPolynomial.monicNormalize g) a1 =
      p2.probe q (CPolynomial.monicNormalize g) a2) :
    cantorZassenhausEvenTraceAttemptWith M D traceCtx q p1 g a1 =
      cantorZassenhausEvenTraceAttemptWith M D traceCtx q p2 g a2
```

`CompPoly.CPolynomial.Roots.FiniteField.tryEvenTraceSplitAttemptsWith_probe_congr` (theorem, [line 253](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/EvenTrace.lean#L253))

> The trace retry loop depends on the probe family only through the probes it
> actually draws.

```lean
theorem tryEvenTraceSplitAttemptsWith_probe_congr {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (q : Nat) {p1 p2 : ProbeFamily F} {g : CPolynomial F} :
    ∀ (attempts offset1 offset2 : Nat),
      (∀ i, i < attempts →
        p1.probe q (CPolynomial.monicNormalize g) (offset1 + i) =
          p2.probe q (CPolynomial.monicNormalize g) (offset2 + i)) →
      tryEvenTraceSplitAttemptsWith M D traceCtx q p1 g attempts offset1 =
        tryEvenTraceSplitAttemptsWith M D traceCtx q p2 g attempts offset2
```

`CompPoly.CPolynomial.Roots.FiniteField.tryEvenTraceSplitAttemptsWith_eq_some_exists_attempt` (theorem, [line 285](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/EvenTrace.lean#L285))

> A successful trace retry loop result is produced by some single attempt.

```lean
theorem tryEvenTraceSplitAttemptsWith_eq_some_exists_attempt {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (q : Nat) (probes : ProbeFamily F) {g : CPolynomial F} :
    ∀ (attempts offset : Nat) {children : Array (CPolynomial F)},
      tryEvenTraceSplitAttemptsWith M D traceCtx q probes g attempts offset =
        some children →
      ∃ attempt,
        cantorZassenhausEvenTraceAttemptWith M D traceCtx q probes g attempt =
          some children
```

`CompPoly.CPolynomial.Roots.FiniteField.tryEvenTraceSplitAttemptsWith_root` (theorem, [line 314](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/EvenTrace.lean#L314))

```lean
theorem tryEvenTraceSplitAttemptsWith_root {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (q : Nat) (probes : ProbeFamily F) {g : CPolynomial F} {a : F}
    (hg : g ≠ 0) (hroot : CPolynomial.eval a g = 0) :
    ∀ attempts offset {children : Array (CPolynomial F)},
      tryEvenTraceSplitAttemptsWith M D traceCtx q probes g attempts offset = some children →
        ∃ child, child ∈ children.toList ∧ CPolynomial.eval a child = 0
```

`CompPoly.CPolynomial.Roots.FiniteField.tryEvenTraceSplitAttemptsWith_stackWork_le` (theorem, [line 370](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/EvenTrace.lean#L370))

```lean
theorem tryEvenTraceSplitAttemptsWith_stackWork_le {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (q : Nat) (probes : ProbeFamily F) {g : CPolynomial F}
    (hg : g ≠ 0) :
    ∀ attempts offset {children : Array (CPolynomial F)},
      tryEvenTraceSplitAttemptsWith M D traceCtx q probes g attempts offset = some children →
        stackWork children.toList ≤ splitWork (CPolynomial.monicNormalize g) - 1
```

`CompPoly.CPolynomial.Roots.FiniteField.tryEvenTraceSplitAttemptsWith_child_normSplitWork_pos` (theorem, [line 398](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/EvenTrace.lean#L398))

```lean
theorem tryEvenTraceSplitAttemptsWith_child_normSplitWork_pos {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (q : Nat) (probes : ProbeFamily F) {g child : CPolynomial F}
    (hg : g ≠ 0) :
    ∀ attempts offset {children : Array (CPolynomial F)},
      tryEvenTraceSplitAttemptsWith M D traceCtx q probes g attempts offset = some children →
        child ∈ children.toList →
          1 ≤ normSplitWork child
```

`CompPoly.CPolynomial.Roots.FiniteField.eval_tracePowerSumPolynomialWith_eq` (theorem, [line 463](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/EvenTrace.lean#L463))

> Evaluating the modular trace power sum at a root of the modulus computes
> the field-level trace power sum of the probe value.

```lean
theorem eval_tracePowerSumPolynomialWith_eq {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    {modulus : CPolynomial F} {z : F}
    (hroot : CPolynomial.eval z modulus = 0) (p k : Nat) (h : CPolynomial F) :
    CPolynomial.eval z (tracePowerSumPolynomialWith M D modulus p k h) =
      tracePowerSum p k (CPolynomial.eval z h)
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith_size_ge_two` (theorem, [line 487](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/EvenTrace.lean#L487))

```lean
theorem cantorZassenhausEvenTraceAttemptWith_size_ge_two {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (q : Nat) (probes : ProbeFamily F) {g : CPolynomial F}
    {attempt : Nat} {children : Array (CPolynomial F)}
    (htry :
      cantorZassenhausEvenTraceAttemptWith M D traceCtx q probes g attempt = some children) :
    2 ≤ children.size
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith_child_dvd_input` (theorem, [line 506](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/EvenTrace.lean#L506))

```lean
theorem cantorZassenhausEvenTraceAttemptWith_child_dvd_input {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (q : Nat) (probes : ProbeFamily F) {g child : CPolynomial F}
    {attempt : Nat} {children : Array (CPolynomial F)}
    (htry :
      cantorZassenhausEvenTraceAttemptWith M D traceCtx q probes g attempt = some children)
    (hmem : child ∈ children.toList) :
    child.toPoly ∣ g.toPoly
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausEvenTraceAttemptWith_success_of_trace_separated` (theorem, [line 552](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/EvenTrace.lean#L552))

> A fixed probe whose trace power sums separate two roots of `g` forces the
> characteristic-two trace split attempt to succeed: the root with trace zero
> lands in `gcd(g, Tr(h))` and the root with nonzero trace survives into the
> complement, so both candidates are nontrivial proper children.

```lean
theorem cantorZassenhausEvenTraceAttemptWith_success_of_trace_separated {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (traceCtx : SmallPrimeTraceContext F)
    (q : Nat) {g h : CPolynomial F} {a b : F} (attempt : Nat)
    (hg : g ≠ 0)
    (hrootA : CPolynomial.eval a g = 0)
    (hrootB : CPolynomial.eval b g = 0)
    (hsepA : tracePowerSum traceCtx.p traceCtx.k (CPolynomial.eval a h) = 0)
    (hsepB : tracePowerSum traceCtx.p traceCtx.k (CPolynomial.eval b h) ≠ 0) :
    ∃ children,
      cantorZassenhausEvenTraceAttemptWith M D traceCtx q
        ({ probe := fun _q _factor _attempt ↦ h } : ProbeFamily F)
        g attempt = some children
```

## Depends on

- [Shared Correctness Lemmas for Las Vegas Splitting](common.md)

## Sources

- [CompPoly/Univariate/Roots/LasVegas/Correctness/EvenTrace.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/EvenTrace.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Univariate.Roots.LasVegas.Correctness.EvenTrace.json)
